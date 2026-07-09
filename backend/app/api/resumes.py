from fastapi import APIRouter

from app.schemas.optimization import ResumeOptimizationRequest, ResumeOptimizationResponse
from app.schemas.resume import ResumeAnalysisResponse, ResumeUploadRequest
from app.services.resume_optimization import ResumeOptimizationService
from app.services.resume_intelligence import ResumeIntelligenceService

router = APIRouter(prefix="/resumes", tags=["resumes"])
resume_service = ResumeIntelligenceService()
optimization_service = ResumeOptimizationService()


@router.post("/analyze", response_model=ResumeAnalysisResponse)
async def analyze_resume(payload: ResumeUploadRequest) -> ResumeAnalysisResponse:
    return resume_service.analyze(payload)


@router.post("/optimize", response_model=ResumeOptimizationResponse)
async def optimize_resume(payload: ResumeOptimizationRequest) -> ResumeOptimizationResponse:
    return optimization_service.optimize(payload)
