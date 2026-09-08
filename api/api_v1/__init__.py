from fastapi import APIRouter

from core.config import settings

from .users_router import router as u_router

router = APIRouter(prefix=settings.api.v1.prefix)

router.include_router(u_router)
