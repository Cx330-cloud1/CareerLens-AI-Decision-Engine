from fastapi import APIRouter

from app.schemas.profile import ProfileAnalysisRequest, ProfileAnalysisResponse
from app.services.profile.service import ProfileService

router = APIRouter(prefix="/profile", tags=["profile"])
profile_service = ProfileService()


@router.post("/analyze", response_model=ProfileAnalysisResponse)
async def analyze_profile(payload: ProfileAnalysisRequest) -> ProfileAnalysisResponse:
    return profile_service.analyze(payload)
