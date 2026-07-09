from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.career_strategy import router as career_strategy_router
from app.api.health import router as health_router
from app.api.matching import router as matching_router
from app.api.profile import router as profile_router
from app.api.resumes import router as resumes_router
from app.api.roles import router as roles_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api")
app.include_router(profile_router, prefix="/api")
app.include_router(resumes_router, prefix="/api")
app.include_router(roles_router, prefix="/api")
app.include_router(matching_router, prefix="/api")
app.include_router(career_strategy_router, prefix="/api")
