from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["overview"])
async def health():
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.get("/{path:path}")
async def catch_all():
    return "unsupported request"