# 🧠 NLP-API-DEMO

A full-stack **NLP microservice** built with FastAPI, Redis, Docker, and Kubernetes.  
This project demonstrates real-world API design, Redis caching, DevOps practices, and automated testing.

---

## ✨ Features

- **GET `/predict?text=...`** → Predicts topic and confidence from a single abstract  
- **POST `/batch_predict`** → Batch predictions for multiple abstracts  
- **Redis caching** → Reduce repeated inference latency  
- **Real-time CSV logging** → Logs predictions to `logs/prediction_log.csv`  
- **Dockerized** → For both local and cloud deployment  
- **Kubernetes deployment support** → FastAPI + Redis services on K8s  
- **CI/CD integration** → GitHub Actions for testing, linting, and coverage  

---

## ⚙️ Tech Stack

| Category     | Tools/Tech                              |
|--------------|------------------------------------------|
| Web API      | FastAPI, Uvicorn                        |
| Caching      | Redis                                   |
| Deployment   | Docker, Kubernetes, Render              |
| CI/CD        | GitHub Actions                          |
| Language     | Python 3.10+                            |
| Testing      | Pytest, FastAPI TestClient              |
| Monitoring   | Prometheus (via ServiceMonitor on K8s)  |

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py                 # FastAPI entrypoint
│   ├── config.py               # Redis + app config
│   ├── services/
│   │   ├── predictor.py        # Topic prediction logic
│   │   └── logger.py           # CSV logging
│   └── utils/
│       └── redis_client.py     # Redis abstraction
├── k8s/
│   ├── fastapi-deployment.yaml     # FastAPI Deployment
│   ├── fastapi-service.yaml        # FastAPI Service
│   ├── fastapi-servicemonitor.yaml # Prometheus monitoring
│   ├── redis-deployment.yaml       # Redis Deployment
│   └── redis-service.yaml          # Redis Service
├── logs/
│   └── prediction_log.csv
├── docker-compose.yml
├── Dockerfile
├── render.yaml
├── requirements.txt
├── test_api.py
└── .github/
    └── workflows/
        └── ci.yml                 # GitHub Actions CI pipeline
```

---

## 🐳 Local Development

Start Redis with Docker:

```bash
docker run -d -p 6379:6379 redis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app locally:

```bash
uvicorn app.main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the endpoints via Swagger UI.

---

## ☸️ Kubernetes Deployment

This project supports K8s deployment for FastAPI and Redis microservices.

```bash
# Apply FastAPI Deployment & Service
kubectl apply -f k8s/fastapi-deployment.yaml
kubectl apply -f k8s/fastapi-service.yaml

# Apply Redis Deployment & Service
kubectl apply -f k8s/redis-deployment.yaml
kubectl apply -f k8s/redis-service.yaml

# (Optional) Apply Prometheus Monitoring
kubectl apply -f k8s/fastapi-servicemonitor.yaml
```

---

## ✅ CI/CD with GitHub Actions

This project uses GitHub Actions to automatically:

- ✅ Install dependencies
- ✅ Run tests with `pytest`
- ✅ Mock Redis in unit tests
- ✅ Measure test coverage
- ✅ Lint Python code

Workflow file: `.github/workflows/ci.yml`

---

## 📌 Sample API Response

```json
{
  "topic": "AI",
  "confidence": 0.92,
  "source": "model_inference"
}
```

---

## 👨‍💻 Author & Use Case

> Built by Ling Duan  
> Date: 2025-04-05  
> Deployed demo: [https://nlp-api-demo.onrender.com](https://nlp-api-demo.onrender.com)

This project simulates a production-ready backend service and is ideal for showcasing:

- 🔧 Backend API Development (FastAPI)
- 📦 Docker + Kubernetes Deployment
- ⚡ Redis Caching for Repeated Inference
- 🧪 Automated Testing and CI/CD
- ☁️ Real-World DevOps and Observability

Perfect for SWE, backend, or DevOps engineer portfolios.

---
