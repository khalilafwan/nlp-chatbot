import json
from datetime import datetime

# Fungsi untuk mencatat performa chatbot
def log_chatbot_performance(intent, confidence, success, sentiment=None):
    report_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "intent": intent,
        "confidence": confidence,  # Skor confidence dari model
        "success": success,        # True jika confidence >= threshold
        "sentiment": sentiment     # Opsional: hasil analisis sentimen
    }

    # Simpan laporan ke file JSON (per baris)
    with open('chatbot_performance.json', 'a') as f:
        f.write(json.dumps(report_data) + "\n")

# Fungsi untuk membaca semua laporan performa
def get_chatbot_report():
    try:
        with open('chatbot_performance.json', 'r') as f:
            logs = [json.loads(line) for line in f]
        return logs
    except FileNotFoundError:
        return {"error": "Laporan tidak ditemukan."}
