import time

def fake_nlp_prediction(text: str) -> str:
    text = text.lower()
    time.sleep(1)
    if "crispr" in text or "gene" in text:
        return "Biotech / CRISPR"
    elif "nlp" in text or "language" in text:
        return "Natural Language Processing"
    elif "ai" in text or "learning" in text:
        return "Machine Learning"
    else:
        return "General Research"
