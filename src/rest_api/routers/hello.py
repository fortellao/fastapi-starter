from fastapi import APIRouter

router = APIRouter(
    prefix="/hello",
    tags=["hello"]
)

@router.get("/")
async def hello_world():
    """
    A simple hello world endpoint.
    """
    return {"message": "Hello, World!"}

@router.get("/{name}")
async def hello_name(name: str):
    """
    A personalized hello endpoint.
    """
    return {"message": f"Hello, {name}!"}
