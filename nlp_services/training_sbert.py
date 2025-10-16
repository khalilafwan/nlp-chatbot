import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from nlp_services.preprocessing import preprocess_for_sbert
from sentence_transformers import SentenceTransformer
from dataset.dataset import training_data, intent_labels

# Inisialisasi model SBERT (mendukung Bahasa Indonesia)
sbert_model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Ambil data dan label
texts = [preprocess_for_sbert(item['text']) for item in training_data]
labels = [intent_labels.index(item['intent']) for item in training_data]

# Encode teks menjadi vektor dengan SBERT
print("🔄 Mengubah teks menjadi embedding dengan SBERT...")
embeddings = sbert_model.encode(texts, show_progress_bar=True)

# Split data ke training & testing
X_train, X_test, y_train, y_test = train_test_split(
    embeddings, labels, test_size=0.2, random_state=42, stratify=labels
)

# Random Forest Classifier
print("🌲 Melatih Random Forest Classifier...")
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Prediksi dan evaluasi
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n✅ Akurasi model Random Forest + SBERT: {accuracy * 100:.2f}%\n")
print("📊 Laporan klasifikasi:")
print(classification_report(
    y_test,
    y_pred, 
    labels=sorted(set(y_test)),
    target_names=[intent_labels[i] for i in sorted(set(y_test))]
    ))

# Simpan model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/intent_rf_sbert.pkl")
print("💾 Model Random Forest disimpan di 'models/intent_rf_sbert.pkl'")
