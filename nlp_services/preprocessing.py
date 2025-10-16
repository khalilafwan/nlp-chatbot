import re
import pkg_resources
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from symspellpy import SymSpell

# === Setup preprocessing tools ===
# Stopwords & stemming
stemmer = StemmerFactory().create_stemmer()
stop_words = set(stopwords.words("indonesian"))

# Spell checker (SymSpell)
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

# === Preprocessing ringan untuk SBERT (tanpa stemming/spell check)
def preprocess_for_sbert(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)           # ganti multiple space
    text = re.sub(r"[^\w\s]", "", text)        # hilangkan tanda baca
    return text.strip()

# === Spell correction
def correct_spelling(text: str) -> str:
    suggestions = sym_spell.lookup_compound(text, max_edit_distance=2)
    return suggestions[0].term if suggestions else text
