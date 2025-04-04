# 🧠 NLP API Demo (FastAPI + Redis + NLP)

A simple API built with FastAPI, demonstrating NLP (Natural Language Processing) topic prediction and Redis caching mechanism.

---
# NLP Topic Classification API

[![CI](https://github.com/LING-6150/nlp-api-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/LING-6150/nlp-api-demo/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Dockerized](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/)
[![Redis](https://img.shields.io/badge/cache-Redis-informational?logo=redis)](https://redis.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## 🚀 Features:

- FastAPI for fast and efficient API creation.
- Redis caching for faster responses.
- Simulated NLP predictions (you can integrate real NLP models easily).

---

## 🛠 Tech Stack:

| Tech | Usage |
|------|-------|
| [FastAPI](https://fastapi.tiangolo.com/) | API Framework |
| [Redis](https://redis.io/) | Caching system |
| Python | Programming language |

---
📝 Logging:
- Real-time logs using Python's logging module.
- Saved in `logs/app.log` for persistent tracking.


## 🔧 Installation:

Clone repository and install dependencies:

```bash
pip install fastapi uvicorn redis
brew install redis
brew services start redis
# nlp-api-demo
