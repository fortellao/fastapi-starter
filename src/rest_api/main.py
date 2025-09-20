from dotenv import load_dotenv
from fastapi import FastAPI
from . import router as api_router
import os

load_dotenv()

app = FastAPI(
    title="FastAPI Starter",
    description="A Production-Ready FastAPI starter application",
    version="0.1.0"
)

http_prefix = os.getenv("HTTP_PREFIX")

# Include API routes
app.include_router(api_router, prefix=http_prefix)