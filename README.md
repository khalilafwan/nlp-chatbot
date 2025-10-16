# 🧠 RANCANG BANGUN CHATBOT MULTIMODAL – NLP ENGINE

API NLP berbasis **Flask** yang menjadi komponen utama dalam sistem chatbot multimodal. Bagian ini menangani proses **Natural Language Processing (NLP)** dan **Intent Recognition**, sebagai bagian dari tugas akhir berjudul **“Rancang Bangun Fitur Chatbot Multimodal Terintegrasi Teks dan Suara untuk Meningkatkan Pelayanan Nasabah di Bank Nagari.”**

---

## 🚀 Teknologi Utama

- 🐍 **Python 3.x + Flask** – Framework API untuk komunikasi antar modul.  
- 🧠 **Sentence-BERT (SBERT)** – Representasi semantik teks dengan embedding kontekstual.  
- 🌲 **Random Forest / Logistic Regression** – Klasifikasi intent berbasis machine learning.  
- ✍️ **TF-IDF Vectorizer** – Representasi numerik kata berdasarkan bobot frekuensi.  
- 🧹 **NLP Toolkit (NLTK, Scikit-learn)** – Preprocessing teks dan analisis intent.  

---

## 💡 Fitur Utama

- 🔤 Preprocessing teks otomatis (tokenisasi, stopword removal, stemming).  
- 🧠 Pengenalan intent menggunakan model gabungan **SBERT + Random Forest**.  
- 💬 Menghasilkan respons dinamis berdasarkan *knowledge base* produk dan layanan Bank Nagari.  
- ⚡ Endpoint REST API yang terintegrasi langsung dengan backend Go.  
- 🔁 Dapat di-*train* ulang menggunakan file dataset `.py` atau `.json`.  

---

## ⚙️ Cara Menjalankan

Pastikan Python 3 dan pip sudah terpasang di sistem kamu.

```bash
# Clone repository
git clone https://github.com/<username>/nlp-chatbot.git
cd nlp-chatbot

# Buat virtual environment
python -m venv venv
venv\Scripts\activate   # untuk Windows
# source venv/bin/activate  # untuk macOS/Linux

# Install dependency
pip install -r requirements.txt

# Jalankan server Flask
python app.py
