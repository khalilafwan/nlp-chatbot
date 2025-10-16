from textblob import TextBlob

# Fungsi untuk menganalisis sentimen pesan
def analyze_sentiment(message):
    analysis = TextBlob(message)
    if analysis.sentiment.polarity > 0:
        return "positif"
    elif analysis.sentiment.polarity < 0:
        return "negatif"
    else:
        return "netral"
