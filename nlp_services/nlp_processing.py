import os
import joblib
import numpy as np
import logging
import datetime
from typing import Dict, Tuple, Optional, Any

from sentence_transformers import SentenceTransformer

# === Preprocessing ===
from nlp_services.preprocessing import preprocess_for_sbert

# === Knowledge base ===
from knowledge_base.produk_bank import get_product_info, products
from knowledge_base.promo import get_promo_info, promotions
from knowledge_base.branch_info import (
    get_capem_info,
    get_kas_info,
    get_cabang_info,
    get_atm_info,
    branch_info,
)

# === info-type detectors ===
from knowledge_base.helper import (
    detect_product_info_type,
    detect_branch_info_type,
    detect_promo_info_type,
    detect_entity_hint
)

# === Synonyms (entity matching) ===
from knowledge_base.synonym import (
    promo_synonyms,
    product_synonyms,
    location_synonyms
)

# === Intent classifier (RF on SBERT embeddings) ===
from dataset.dataset import intent_labels

# === Utilities ===
from utils.sentiment_analysis import analyze_sentiment
from utils.reporting import log_chatbot_performance


# -------------------------------
# Global setup
# -------------------------------
_SBERT_MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
_RF_MODEL_PATH = "models/intent_rf_sbert.pkl"

logging.basicConfig(level=logging.INFO)

try:
    sbert_model = SentenceTransformer(_SBERT_MODEL_NAME)
except Exception as e:
    raise RuntimeError(f"Gagal load SBERT '{_SBERT_MODEL_NAME}': {e}")

if not os.path.exists(_RF_MODEL_PATH):
    raise FileNotFoundError(
        "Model Random Forest belum ada. Jalankan training_sbert.py terlebih dahulu."
    )

# Load RF sekali
_rf_model = joblib.load(_RF_MODEL_PATH)

# Threshold default
confidence_threshold = 0.40


# -------------------------------
# Helper kecil
# -------------------------------
def _normalize(s: str) -> str:
    return " ".join(s.lower().split())


def _pretty(s: str) -> str:
    return s.replace("_", " ").title()


def _encode(text: str) -> np.ndarray:
    return sbert_model.encode([text])


def _predict_intent(message: str) -> Tuple[str, float]:
    """
    Prediksi intent dengan SBERT + RF (cached).
    Return: (predicted_intent_label, confidence_score)
    """
    cleaned = preprocess_for_sbert(message)
    emb = _encode(cleaned)  # shape (1, 512)
    y_pred = _rf_model.predict(emb)[0]
    y_prob = float(np.max(_rf_model.predict_proba(emb)))
    return intent_labels[y_pred], y_prob


def adjust_confidence_threshold(feedback: str, adjustment: float = 0.05) -> float:
    global confidence_threshold
    if feedback == "good":
        confidence_threshold = min(confidence_threshold + adjustment, 1.0)
    elif feedback == "bad":
        confidence_threshold = max(confidence_threshold - adjustment, 0.40)
    return confidence_threshold


# -------------------------------
# Entity extraction (pakai synonyms)
# -------------------------------
def _match_by_synonyms(text: str, synonyms_map: Dict[str, list], canonical_dict: Dict) -> Optional[str]:
    """
    Cari canonical key berdasarkan synonyms_map.
    - Langsung cocokkan canonical key (snake_case & dengan spasi).
    - Lalu cek alias di synonyms_map.
    """
    t = _normalize(text)

    # 1) cocokkan nama canonical langsung
    for key in canonical_dict.keys():
        if key in t or key.replace("_", " ") in t:
            return key

    # 2) cocokkan via synonyms
    for canonical, aliases in synonyms_map.items():
        if canonical in t or canonical.replace("_", " ") in t:
            return canonical
        for alias in aliases:
            a = alias.lower()
            if a in t:
                return canonical

    return None


def extract_entities(message: str) -> Dict[str, str]:
    msg = _normalize(message)
    entities: Dict[str, str] = {}

    hint = detect_entity_hint(message)
    if hint:
        entities["entity_hint"] = hint

    # Produk
    prod = _match_by_synonyms(msg, product_synonyms, products)
    if prod:
        entities["product_name"] = prod

    # Promo
    promo = _match_by_synonyms(msg, promo_synonyms, promotions)
    if promo:
        entities["promo_name"] = promo

    # Lokasi
    for entity_type in ["branch", "capem", "branch_kas", "atm"]:
        name = _match_by_synonyms(
            msg,
            location_synonyms.get(entity_type, {}),
            branch_info.get(entity_type, {})
        )
        if name:
            entities[f"{entity_type}_name"] = name

    # Fallback sederhana (tanpa synonyms) untuk branch_info, jika belum ada synonyms
    for entity_type in ["branch", "capem", "branch_kas", "atm"]:
        for key in branch_info.get(entity_type, {}).keys():
            if key in msg or key.replace("_", " ") in msg:
                entities[f"{entity_type}_name"] = key
                break

    # print(f"[DEBUG] Detected entities: {entities}")
    return entities


def validate_intent_by_entities(intent: str, entities: Dict[str, str]) -> str:
    hint = entities.get("entity_hint")
    """
    Perbaiki intent berbasis entitas yang ditemukan.
    """
    if hint == "atm" and intent not in ["atm_inquiry"]:
        return "atm_inquiry"
    if hint == "capem" and intent not in ["capem_inquiry"]:
        return "capem_inquiry"
    if hint == "branch_kas" and intent not in ["branch_kas_inquiry"]:
        return "branch_kas_inquiry"
    if hint == "branch" and intent not in ["branch_inquiry"]:
        return "branch_inquiry"

    if intent == "atm_inquiry" and not entities.get("atm_name"):
        if entities.get("branch_name"):
            return "branch_inquiry"
        if entities.get("capem_name"):
            return "capem_inquiry"
        if entities.get("branch_kas_name"):
            return "branch_kas_inquiry"

    if intent == "branch_inquiry" and not entities.get("branch_name"):
        if entities.get("atm_name"):
            return "atm_inquiry"

    if intent == "promo_inquiry" and not entities.get("promo_name"):
        # tetap promo_inquiry, tapi nanti kita respon general list promo
        return "promo_inquiry"

    if intent == "product_inquiry" and not entities.get("product_name"):
        # tetap product_inquiry, tapi nanti respon tanya produk mana
        return "product_inquiry"

    return intent


# -------------------------------
# Responder utama per intent
# -------------------------------
def get_response_by_intent(intent: str, message: str, entities: Optional[Dict[str, str]] = None) -> str:
    entities = entities or {}
    hint = entities.get("entity_hint")

    if intent == "greeting":
        return "Halo! Ada yang bisa saya bantu? 😊"

    if intent == "thanks":
        return "Sama-sama! Senang bisa membantu. 🙌"

    if intent == "product_inquiry":
        info_type = detect_product_info_type(message)
        product_name = entities.get("product_name")
        if product_name:
            return get_product_info(product_name, info_type)
        return "Produk apa yang ingin kamu ketahui? Contoh: Tabungan Sikoci, Simpeda, Giro, dll."

    if intent == "promo_inquiry":
        info_type = detect_promo_info_type(message)
        promo_name = entities.get("promo_name")
        if promo_name:
            return get_promo_info(promo_name, info_type)
        # kalau user tanya promo tapi tidak sebut nama → list semua
        return get_promo_info()  # list semua promo

    if intent == "atm_inquiry":
        info_type = detect_branch_info_type(message)
        name = entities.get("atm_name")
        if name:
            return get_atm_info(name, info_type)

        # fallback lebih spesifik bila ada hint
        if hint == "atm":
            return "ATM mana yang kamu maksud? Coba sebutkan nama gedung/lokasi (mis. 'SJS Plaza Lapai Padang')."

        # fallback ke lokasi lain kalau yang disebut bukan ATM
        if entities.get("branch_name"):
            return get_cabang_info(entities["branch_name"], info_type)
        if entities.get("capem_name"):
            return get_capem_info(entities["capem_name"], info_type)
        if entities.get("branch_kas_name"):
            return get_kas_info(entities["branch_kas_name"], info_type)
        return "ATM mana yang kamu maksud? Coba sebutkan gedung/lokasi, misalnya: 'SJS Plaza Lapai Padang'."

    if intent == "capem_inquiry":
        info_type = detect_branch_info_type(message)
        name = entities.get("capem_name")
        if name:
            return get_capem_info(name, info_type)
        if hint == "capem":
            return "Capem mana yang kamu maksud? Misalnya: Capem A. Yani Pekanbaru, Capem Ulak Karang, dll."
        return "Kantor Cabang Pembantu mana yang kamu maksud?"

    if intent == "branch_inquiry":
        info_type = detect_branch_info_type(message)
        name = entities.get("branch_name")
        if name:
            return get_cabang_info(name, info_type)
        if entities.get("atm_name"):
            return get_atm_info(entities["atm_name"], info_type)
        if hint == "branch":
            return "Cabang mana yang kamu maksud? Misalnya: Cabang Payakumbuh, Cabang Pekanbaru, dll."
        return "Kantor cabang mana yang ingin kamu cari tahu?"

    if intent == "branch_kas_inquiry":
        info_type = detect_branch_info_type(message)
        name = entities.get("branch_kas_name")
        if name:
            return get_kas_info(name, info_type)
        if hint == "branch_kas":
            return "Unit Kas mana yang kamu maksud? Misalnya: Kas Balaikota Padang, Kas Tabing, Kas Parit Malintang, dll."
        return "Unit kas mana yang ingin kamu tahu?"

    return "Maaf, saya belum memahami maksudmu. Bisa dijelaskan lagi?"


# -------------------------------
# Logging
# -------------------------------
def log_interaction(message: str, response: str, confidence_score: float) -> None:
    log_message = (
        f"{datetime.datetime.now()}: "
        f"Message: {message} | Response: {response} | Confidence: {confidence_score}\n"
    )
    logging.info(log_message)


# -------------------------------
# Pipeline utama
# -------------------------------
def process_message(message: str) -> Dict[str, any]:
    predicted_intent, confidence_score = _predict_intent(message)
    sentiment = analyze_sentiment(message)
    entities = extract_entities(message)
    final_intent = validate_intent_by_entities(predicted_intent, entities)

    if confidence_score < confidence_threshold:
        response_message = "Maaf, saya kurang yakin dengan pertanyaan kamu. Bisa diperjelas lagi?"
        intent_used = None
    else:
        response_message = get_response_by_intent(
            final_intent, message, entities=entities)
        intent_used = final_intent

    log_interaction(message, response_message, confidence_score)
    log_chatbot_performance(
        intent=predicted_intent,
        confidence=confidence_score,
        success=(confidence_score >= confidence_threshold),
        sentiment=sentiment,
    )

    # Debug prints untuk dev
    # print(f"[DEBUG] Predicted Intent: {predicted_intent}")
    # print(f"[DEBUG] Final Intent: {final_intent}")
    # print(f"[DEBUG] Entities: {entities}")

    return {
        "intent": intent_used,
        "tokens": preprocess_for_sbert(message).split(),
        "confidence": confidence_score,
        "response_message": response_message,
        "sentiment": sentiment,
    }


def receive_feedback(feedback: str) -> float:
    new_threshold = adjust_confidence_threshold(feedback)
    print(f"Threshold confidence diperbarui menjadi: {new_threshold}")
    return new_threshold
