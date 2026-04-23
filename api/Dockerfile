# ---------- Stage 1: builder ----------
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------- Stage 2: runtime ----------
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -r -m -s /bin/bash apiuser

COPY --from=builder /install /usr/local

COPY . .

USER apiuser

EXPOSE 8000

HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD curl --fail http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]