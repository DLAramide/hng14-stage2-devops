FROM python:3.11-slim

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy worker code
COPY . .

# non-root user (REQUIRED for grading)
RUN useradd -m workeruser
USER workeruser

# environment defaults (can be overridden by compose)
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

# start worker
CMD ["python", "worker.py"]