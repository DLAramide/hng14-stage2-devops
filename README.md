# HNG14 Stage 2 DevOps Project

## Overview

This project is a containerized microservices system built with:

* FastAPI (API service)
* Background Worker service
* Redis (queue/broker)
* Frontend application
* CI/CD pipeline using GitHub Actions
* Container registry: GHCR
* Security scanning: Trivy

# Prerequisites

Before running this project, ensure you have:

* Docker (v24+ recommended)
* Docker Compose (v2+)
* Git
* Internet connection (for pulling images)

Verify installation:

```bash
docker --version
docker compose version
```

# Environment Setup (.env)

Create a `.env` file in the root directory:

```env
REDIS_HOST=redis
REDIS_PORT=6379

API_PORT=8000
FRONTEND_PORT=3000
```

> These values are used by Docker Compose to connect services.

---

# 🐳 How to Run the Project

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/hng14-stage2-devops.git
cd hng14-stage2-devops
```

## 2. Build and start services

```bash
docker compose up --build
```


## 3. Run in detached mode (recommended)

```bash
docker compose up -d
```


## 4. Stop services

```bash
docker compose down
```

---

# Service Access

Once running, access services:

| Service  | URL                                            |
| -------- | ---------------------------------------------- |
| API      | [http://localhost:8000](http://localhost:8000) |
| Frontend | [http://localhost:3000](http://localhost:3000) |
| Redis    | localhost:6379                                 |


# Expected Output

When fully running, you should see:

### API

* Uvicorn running successfully

```text
Uvicorn running on http://0.0.0.0:8000
```

### Worker

* Worker actively processing jobs

```text
Worker started and listening for tasks
```

### Redis

* Healthy container

```text
Up (healthy)
```

### Frontend

* UI accessible in browser

```text
React/Vite app running on port 3000
```

# CI/CD Pipeline

Every push triggers:

### 1. Lint Stage

* Flake8 checks Python code

### 2. Test Stage

* Pytest runs with coverage

### 3. Build Stage

* Docker images built for:

  * API
  * Worker
  * Frontend

### 4. Security Stage

* Trivy scans images for vulnerabilities

### 5. Push Stage

* Images pushed to GHCR

# Security

* Images are scanned using Trivy
* Only CRITICAL vulnerabilities fail the pipeline
* Docker images run as non-root users

# Architecture

```
Frontend → API → Redis → Worker
```

* Frontend sends requests
* API processes and queues tasks
* Redis stores job queue
* Worker consumes and executes jobs


# Testing

Run tests locally:

```bash
pytest -q
```

With coverage:

```bash
pytest -q --cov=api --cov-report=xml
```



# Notes

* All Docker images are versioned using Git SHA
* GHCR is used for container registry
* CI/CD is fully automated via GitHub Actions


# Status

✔ Build system working
✔ CI/CD pipeline configured
✔ Security scanning enabled
✔ Multi-service architecture deployed



## If you want next step (important):

I can help you:

### 🔥 upgrade this to “distinction-level README”

(add badges, architecture diagram, deployment section, API docs)

or

### 🧪 simulate grading checklist so you KNOW if you’ll pass

Just say.
