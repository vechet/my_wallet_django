from fastapi import APIRouter
from my_wallet_django.api.api_v1.endpoints import authentication, device, account_type, currency, category, payment_method, account, income_or_expense, demo

api_router = APIRouter()
api_router.include_router(demo.router, prefix="/v1", tags=["demo"])
api_router.include_router(authentication.router,
                          prefix="/v1", tags=["authentication"])
api_router.include_router(device.router, prefix="/v1", tags=["device"])
api_router.include_router(
    category.router, prefix="/v1", tags=["category"])
api_router.include_router(
    payment_method.router, prefix="/v1", tags=["payment method"])
api_router.include_router(
    currency.router, prefix="/v1", tags=["currency"])
api_router.include_router(
    account_type.router, prefix="/v1", tags=["account type"])
api_router.include_router(
    account.router, prefix="/v1", tags=["account"])
api_router.include_router(
    income_or_expense.router, prefix="/v1", tags=["income or expense"])
