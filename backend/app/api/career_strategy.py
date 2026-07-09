from fastapi import APIRouter

from app.schemas.optimization import CareerStrategyRequest, CareerStrategyResponse
from app.services.career_strategy import CareerStrategyService

router = APIRouter(prefix="/career-strategy", tags=["career-strategy"])
career_strategy_service = CareerStrategyService()


@router.post("/generate", response_model=CareerStrategyResponse)
async def generate_career_strategy(payload: CareerStrategyRequest) -> CareerStrategyResponse:
    return career_strategy_service.generate(payload)
