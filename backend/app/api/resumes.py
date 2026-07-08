from fastapi import APIRouter

from app.schemas.resume import ResumeAnalysisResponse, ResumeUploadRequest
from app.services.resume_intelligence import ResumeIntelligenceService

router = APIRouter(prefix="/resumes", tags=["resumes"])
resume_service = ResumeIntelligenceService()


@router.post("/analyze", response_model=ResumeAnalysisResponse)
async def analyze_resume(payload: ResumeUploadRequest) -> ResumeAnalysisResponse:
    return resume_service.analyze(payload)
