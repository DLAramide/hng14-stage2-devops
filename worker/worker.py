import redis
import time
import os
import signal
import sys

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, decode_responses=True  # important fix
)

running = True


def shutdown(sig, frame):
    global running
    print("Shutting down worker...")
    running = False
    sys.exit(0)


signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)


def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}")


while running:
    job = r.brpop("job", timeout=5)

    if job:
        _, job_id = job
        process_job(job_id)
