import nltk
nltk.download('stopwords')  # Bisa dipindah ke training saja jika tidak perlu di runtime
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from nlp_services.nlp_processing import process_message
from utils.reporting import get_chatbot_report
from dotenv import load_dotenv
import os

# === Setup ===

load_dotenv()

app = Flask(__name__)
api = Api(app)

# === Endpoint Prediksi NLP ===

class NLPService(Resource):
    def post(self):
        data = request.get_json()

        if not data or 'message' not in data:
            return {"error": "Message is required"}, 400

        if not isinstance(data['message'], str):
            return {"error": "Message must be a string"}, 400

        try:
            response = process_message(data['message'])  # ini seharusnya panggil predict_intent() + ambil jawaban
            return jsonify(response)
        except Exception as e:
            return {"error": str(e)}, 500

# === Endpoint Laporan Chatbot (opsional) ===

class ChatbotReport(Resource):
    def get(self):
        report = get_chatbot_report()
        return jsonify(report)

# === Register Routes ===

api.add_resource(NLPService, '/nlp')
api.add_resource(ChatbotReport, '/chatbot_report')

# === Run Server ===

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
