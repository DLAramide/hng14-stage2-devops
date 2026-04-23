#!/bin/bash
set -e

docker compose up -d

sleep 10

timeout 30 curl --fail http://localhost:8000/health

docker compose down