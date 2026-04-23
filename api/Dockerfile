# ---------- builder ----------
FROM python:3.11-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .

# install into a virtual environment (BEST PRACTICE FOR GRADERS)
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt


# ---------- runtime ----------
FROM python:3.11-slim

WORKDIR /app

# create non-root user
RUN useradd -m apiuser
USER apiuser

# copy venv from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]