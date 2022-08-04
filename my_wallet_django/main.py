from fastapi import FastAPI
from my_wallet_django.api.api_v1.api import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api")
