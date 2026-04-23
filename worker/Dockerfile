# ---------- Stage 1: builder ----------
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


# ---------- Stage 2: runtime ----------
FROM python:3.11-slim

WORKDIR /app

RUN useradd -m workeruser

COPY --from=builder /root/.local /home/workeruser/.local

COPY . .

USER workeruser

ENV PATH=/home/workeruser/.local/bin:$PATH
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

CMD ["python", "worker.py"]