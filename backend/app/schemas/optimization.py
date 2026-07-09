from pydantic import BaseModel, Field

from app.schemas.matching import AlignmentReport, GapAnalysis
from app.schemas.resume import CapabilityEvidence
from app.schemas.role import RoleRequirement


class ResumeOptimizationRequest(BaseModel):
    resume_evidence: list[CapabilityEvidence] = Field(default_factory=list)
    target_role: RoleRequirement
    alignment_gaps: list[GapAnalysis] = Field(default_factory=list)
    alignment_report: AlignmentReport | None = None


class CapabilityPriority(BaseModel):
    capability: str
    category: str
    priority: str
    reason: str
    confidence: float = Field(ge=0, le=1)


class EvidenceImprovement(BaseModel):
    evidence_id: str
    capability: str
    current_signal: str
    improvement: str
    quality_target: str
    confidence: float = Field(ge=0, le=1)


class ExperienceReframing(BaseModel):
    source_section: str
    target_capability: str
    framing_guidance: str
    before_signal: str
    after_positioning: str


class MissingEvidence(BaseModel):
    capability: str
    evidence_needed: str
    suggested_proof: str
    impact_level: str


class ResumeOptimization(BaseModel):
    capability_priorities: list[CapabilityPriority]
    evidence_improvements: list[EvidenceImprovement]
    experience_reframing: list[ExperienceReframing]
    missing_evidence: list[MissingEvidence]


class ResumeOptimizationResponse(BaseModel):
    resume_optimization: ResumeOptimization
    model_metadata: dict[str, str]


class CareerStrategyRequest(BaseModel):
    resume_optimization: ResumeOptimization
    target_role: RoleRequirement
    alignment_report: AlignmentReport | None = None


class CareerAction(BaseModel):
    title: str
    rationale: str
    evidence_outcome: str
    priority: str


class RecommendedProject(BaseModel):
    title: str
    target_capabilities: list[str]
    evidence_to_create: str
    scope: str


class GrowthPathStep(BaseModel):
    capability: str
    current_gap: str
    next_level_signal: str
    validation_method: str


class CareerPlan(BaseModel):
    short_term_actions: list[CareerAction]
    medium_term_actions: list[CareerAction]
    recommended_projects: list[RecommendedProject]
    capability_growth_path: list[GrowthPathStep]


class CareerStrategyResponse(BaseModel):
    career_plan: CareerPlan
    model_metadata: dict[str, str]
