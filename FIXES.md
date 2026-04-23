API/main.py line 12
Problem:
Redis host hardcoded to localhost → breaks in containers
Fix:
Changed to read from REDIS_HOST environment variable.

File: api/main.py line 7
Problem:
Redis host was hardcoded to "localhost". This breaks inside Docker because
services communicate via container DNS names.
Fix:
Changed Redis connection to use environment variables REDIS_HOST and REDIS_PORT.

File: api/main.py line 20
Problem:
Manual byte decoding was required because Redis returned bytes.
This creates unnecessary complexity and is error-prone.
Fix:
Enabled decode_responses=True in Redis client and removed manual decoding.

File: api/main.py line 7
Problem:
Application did not verify Redis connection on startup. Failures would
occur during runtime instead of at boot.
Fix:
Added startup event to verify Redis connectivity using ping().

File: api/main.py line 1
Problem:
No health check endpoint existed. Required for Docker HEALTHCHECK and
deployment rolling updates.
Fix:
Added /health endpoint that verifies API and Redis availability.

File: api/main.py line 17
Problem:
API returned 200 OK when job was not found.
Fix:
Replaced with HTTPException(404).

File: api/main.py line 1
Problem:
No structured logging was configured.
Fix:
Added Python logging for observability.

File: frontend/server.js line 1
Problem:
Frontend service lacked a health check endpoint required for Docker
HEALTHCHECK and rolling deployments.
Fix:
Added GET /health route.

File: worker/worker.py line 5
Problem:
Redis host hardcoded to localhost, which breaks container networking.
Fix:
Use REDIS_HOST and REDIS_PORT environment variables.

File: worker/worker.py line 1
Problem:
Worker did not retry Redis connection. Container would crash if Redis
was not ready at startup.
Fix:
Added Redis connection retry loop.

File: worker/worker.py line 1
Problem:
Worker did not handle SIGTERM/SIGINT, risking job loss during deployments.
Fix:
Implemented graceful shutdown with signal handlers.

File: worker/worker.py line 14
Problem:
Infinite loop prevented graceful shutdown.
Fix:
Loop now respects shutdown flag.

File: worker/worker.py line 8
Problem:
Worker did not mark jobs as "processing", causing lost jobs on crash.
Fix:
Set job status to "processing" before processing.

File: worker/worker.py line 16
Problem:
No error handling around job execution could crash the worker.
Fix:
Wrapped job processing in try/except and mark job as failed.

File: worker/worker.py line 1
Problem:
Worker had no mechanism for Docker HEALTHCHECK.
Fix:
Added Redis heartbeat key updated every loop iteration.