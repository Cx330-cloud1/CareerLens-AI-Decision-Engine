from fastapi import APIRouter, HTTPException, Query

from app.schemas.role import (
    CareerCategory,
    RoleAnalysisRequest,
    RoleAnalysisResponse,
    RoleTemplate,
    RoleTemplateListResponse,
)
from app.services.role_knowledge import RoleKnowledgeService
from app.services.role_intelligence import RoleIntelligenceService

router = APIRouter(prefix="/roles", tags=["roles"])
role_knowledge_service = RoleKnowledgeService()
role_service = RoleIntelligenceService(role_knowledge_service)


@router.get("/categories", response_model=list[CareerCategory])
async def list_role_categories() -> list[CareerCategory]:
    return role_knowledge_service.list_categories()


@router.get("/templates", response_model=RoleTemplateListResponse)
async def list_role_templates(
    query: str | None = Query(default=None, min_length=1),
    category_id: str | None = Query(default=None, min_length=1),
) -> RoleTemplateListResponse:
    return RoleTemplateListResponse(
        categories=role_knowledge_service.list_categories(),
        templates=role_knowledge_service.list_templates(query=query, category_id=category_id),
    )


@router.get("/templates/{template_id}", response_model=RoleTemplate)
async def get_role_template(template_id: str) -> RoleTemplate:
    template = role_knowledge_service.get_template(template_id)
    if not template:
        raise HTTPException(status_code=404, detail="Role template not found.")
    return template


@router.post("/analyze", response_model=RoleAnalysisResponse)
async def analyze_role(payload: RoleAnalysisRequest) -> RoleAnalysisResponse:
    try:
        return role_service.analyze(payload)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
