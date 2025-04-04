import os
import csv
from datetime import datetime

CSV_PATH = "logs/prediction_log.csv"

def init_csv():
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["text", "topic", "confidence", "source", "timestamp"])

def write_log(text, topic, confidence, source):
    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([text, topic, confidence, source, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
