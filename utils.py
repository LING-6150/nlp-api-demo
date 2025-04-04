# utils.py

# 关键词规则：根据关键词分类话题
TOPIC_KEYWORDS = {
    "AI": ["artificial intelligence", "neural network", "machine learning", "deep learning", "AI"],
    "Biotech": ["gene", "crispr", "biotechnology", "genomics"],
    "Economics": ["inflation", "interest rate", "GDP", "macroeconomics", "unemployment"],
    "Environment": ["climate change", "sustainability", "carbon", "pollution"],
    "Cybersecurity": ["encryption", "cyber attack", "firewall", "zero trust", "phishing"]
}

def fake_nlp_prediction(text: str) -> str:
    text_lower = text.lower()
    for topic, keywords in TOPIC_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text_lower:
                return topic
    return "General Research"
