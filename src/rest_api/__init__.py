from fastapi import APIRouter

from .routers import hello_router

router = APIRouter()

# Include routers
router.include_router(hello_router)
