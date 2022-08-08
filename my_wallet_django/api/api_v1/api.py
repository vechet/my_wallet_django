from fastapi import APIRouter
from my_wallet_django.api.api_v1.endpoints import items, authentication, device, account_type, currency, category, payment_method

api_router = APIRouter()
api_router.include_router(authentication.router,
                          prefix="/v1", tags=["authentication"])
api_router.include_router(device.router, prefix="/v1", tags=["device"])
api_router.include_router(
    account_type.router, prefix="/v1", tags=["account type"])
api_router.include_router(
    currency.router, prefix="/v1", tags=["currency"])
api_router.include_router(
    category.router, prefix="/v1", tags=["category"])
api_router.include_router(
    payment_method.router, prefix="/v1", tags=["payment method"])
