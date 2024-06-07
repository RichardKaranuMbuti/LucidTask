import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from core.fastapi_app import app as fastapi_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lucidtask.settings')

django_app = get_asgi_application()

app = FastAPI()

@app.middleware("http")
async def django_middleware(request, call_next):
    if request.url.path.startswith("/api/"):
        return await fastapi_app(request.scope, request.receive, request.send)
    else:
        return await django_app(request.scope, request.receive, request.send)
