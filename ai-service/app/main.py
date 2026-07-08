from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    docs_url="/docs",
    openapi_url="/openapi.json",
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "ai-service"}
