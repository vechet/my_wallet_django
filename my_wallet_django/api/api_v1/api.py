from fastapi import APIRouter
from api.api_v1.endpoints import items, authentication, device, account_type

api_router = APIRouter()
api_router.include_router(authentication.router,
                          prefix="/v1", tags=["authentication"])
api_router.include_router(device.router, prefix="/v1", tags=["devices"])
api_router.include_router(
    account_type.router, prefix="/v1", tags=["account types"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/v1", tags=["items"])
