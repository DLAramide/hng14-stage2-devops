# ---------- Stage 1: builder ----------
FROM python:3.11-slim AS builder

WORKDIR /app

# install build deps (only here)
RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


# ---------- Stage 2: runtime ----------
FROM python:3.11-slim

WORKDIR /app

# create non-root user
RUN useradd -m workeruser

# copy installed packages
COPY --from=builder /root/.local /home/workeruser/.local

# copy app code
COPY . .

# switch to non-root
USER workeruser

# ensure python sees installed packages
ENV PATH=/home/workeruser/.local/bin:$PATH

# env config
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

# run worker
CMD ["python", "worker.py"]