from fastapi import APIRouter

from app.schemas.matching import AlignmentAnalysisRequest, AlignmentReport
from app.services.matching import MatchingService

router = APIRouter(prefix="/matching", tags=["matching"])
matching_service = MatchingService()


@router.post("/analyze", response_model=AlignmentReport)
async def analyze_alignment(payload: AlignmentAnalysisRequest) -> AlignmentReport:
    return matching_service.analyze(payload)
