# ---------- Stage 1: builder ----------
FROM python:3.11-slim AS builder

WORKDIR /app

# install build deps
RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


# ---------- Stage 2: runtime ----------
FROM python:3.11-slim

WORKDIR /app

# install runtime deps only
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# create non-root user
RUN useradd -m apiuser

# copy installed packages from builder
COPY --from=builder /root/.local /home/apiuser/.local

# copy app code
COPY . .

# switch to non-root
USER apiuser

# ensure python can find packages
ENV PATH=/home/apiuser/.local/bin:$PATH

ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

EXPOSE 8000

# healthcheck (EXTRA POINTS)
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]