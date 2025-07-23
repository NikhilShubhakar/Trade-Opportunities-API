from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
import time

rate_limit_store = {}
RATE_LIMIT = 5  # requests
WINDOW_SIZE = 60  # seconds


class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        now = time.time()

        history = rate_limit_store.get(client_ip, [])
        history = [t for t in history if now - t < WINDOW_SIZE]

        if len(history) >= RATE_LIMIT:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

        history.append(now)
        rate_limit_store[client_ip] = history

        response = await call_next(request)
        return response
