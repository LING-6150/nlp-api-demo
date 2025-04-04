

[![CI](https://github.com/LING-6150/nlp-api-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/LING-6150/nlp-api-demo/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Dockerized](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/)
[![Redis](https://img.shields.io/badge/cache-Redis-informational?logo=redis)](https://redis.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


# 🧠 NLP Topic Classification API

A lightweight **FastAPI-based microservice** for predicting the topic of a given abstract. It supports **real-time inference**, **Redis caching**, **logging**, **Dockerization**, and **automated deployment** via Render.

---

## 🔍 Features

- `GET /predict?text=...` → Predicts topic and confidence from a single abstract
- `POST /batch_predict` → Batch predictions from multiple abstracts
- Redis caching to reduce repeated inference latency
- Real-time logging into `logs/prediction_log.csv`
- Dockerized and deployed on [Render](https://render.com)
- Integrated CI with GitHub Actions for testing and linting

---

## ⚙️ Tech Stack

| Category    | Tools/Tech                            |
|-------------|----------------------------------------|
| Web API     | FastAPI, Uvicorn                      |
| Caching     | Redis                                 |
| Deployment  | Docker, Render                        |
| CI/CD       | GitHub Actions                        |
| Language    | Python 3.10+                          |
| Testing     | Pytest + FastAPI TestClient           |

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py               # FastAPI entrypoint
│   ├── config.py             # Redis + app config
│   ├── services/
│   │   ├── predictor.py      # Topic prediction logic
│   │   └── logger.py         # CSV logging
│   └── utils/
│       └── redis_client.py   # Redis abstraction
├── Dockerfile
├── render.yaml               # Render deployment spec
├── requirements.txt
├── tests/
│   └── test_api.py           # Unit tests
└── .github/
    └── workflows/
        └── ci.yml            # GitHub Actions CI pipeline
```

---

## 🐳 Local Development

1. **Install Redis locally** or use Docker:

```bash
docker run -d -p 6379:6379 redis
```

2. **Run app locally**

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit http://127.0.0.1:8000/docs to test endpoints via Swagger UI.

---

## 🚀 Deployment on Render

1. Push code to GitHub with `render.yaml` included.
2. Create a **Web Service** and attach your GitHub repo.
3. (Optional) Add a **Redis Key-Value Instance** and configure the `REDIS_URL` environment variable.

---

## ✅ CI/CD Pipeline

This project uses **GitHub Actions** to automatically:

- Install dependencies
- Run unit tests with Redis mocking
- Show test coverage

Check `.github/workflows/ci.yml` for configuration.

---

## 📌 Sample Prediction Response

```json
{
  "topic": "AI",
  "confidence": 0.92,
  "source": "model_inference"
}
```

---

## 👨‍💻 Author & Use Case

This project simulates a **real-world backend microservice** and is designed to demonstrate:

- API Design & Testing
- Docker-based deployment
- Redis caching in real apps
- CI/CD skills (useful for cloud engineering/SWE roles)

> Perfect for showcasing backend system building in job interviews or portfolio.

---

## 📬 Contact

Built by [Ling Duan](https://github.com/LING-6150).  
Deployed project: [https://nlp-api-demo.onrender.com](https://nlp-api-demo.onrender.com)

---
