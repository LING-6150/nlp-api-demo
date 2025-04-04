import random

TOPIC_KEYWORDS = {
    "AI": ["artificial intelligence", "neural network", "machine learning", "deep learning", "AI"],
    "Biotech": ["gene", "crispr", "biotechnology", "genomics"],
    "Economics": ["inflation", "interest rate", "GDP", "macroeconomics", "unemployment"],
    "Environment": ["climate change", "sustainability", "carbon", "pollution"],
    "Cybersecurity": ["encryption", "cyber attack", "firewall", "zero trust", "phishing"]
}

def predict_topic(text: str):
    lower_text = text.lower()
    match_counts = {}

    for topic, keywords in TOPIC_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in lower_text:
                match_counts[topic] = match_counts.get(topic, 0) + 1

    if match_counts:
        best_topic = max(match_counts, key=match_counts.get)
        confidence = round(min(0.7 + match_counts[best_topic] * 0.05, 0.99), 2)
    else:
        best_topic = random.choice(list(TOPIC_KEYWORDS.keys()))
        confidence = round(random.uniform(0.7, 0.9), 2)

    return {"topic": best_topic, "confidence": confidence}
