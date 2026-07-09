from pydantic import BaseModel, Field

from app.schemas.resume import CapabilityEvidence
from app.schemas.role import RoleRequirement, RoleTemplate


class CandidateCapabilityInput(BaseModel):
    name: str
    category: str = "general"
    evidence: str = ""
    confidence: float = Field(default=0.65, ge=0, le=1)


class CandidateProfileInput(BaseModel):
    headline: str | None = None
    target_direction: str | None = None
    capabilities: list[str] = Field(default_factory=list)
    evidence: list[str] = Field(default_factory=list)


class AlignmentAnalysisRequest(BaseModel):
    candidate_profile: CandidateProfileInput | None = None
    resume_evidence: list[CapabilityEvidence] = Field(default_factory=list)
    selected_role_template: RoleTemplate | None = None
    role_requirement: RoleRequirement | None = None
    candidate_capabilities: list[CandidateCapabilityInput] = Field(default_factory=list)


class EvidenceLink(BaseModel):
    evidence_id: str
    source_section: str
    excerpt: str
    relevance: str
    confidence: float = Field(ge=0, le=1)


class CapabilityMatch(BaseModel):
    capability: str
    category: str
    score: float = Field(ge=0, le=100)
    confidence: float = Field(ge=0, le=1)
    why_it_matches: str
    supporting_evidence: list[EvidenceLink] = Field(default_factory=list)
    missing_evidence: str | None = None


class GapAnalysis(BaseModel):
    capability: str
    category: str
    impact_level: str
    what_is_missing: str
    evidence_needed: str
    recommended_action: str


class EvidenceMapping(BaseModel):
    requirement: str
    evidence_links: list[EvidenceLink] = Field(default_factory=list)
    assessment: str
    confidence: float = Field(ge=0, le=1)


class AlignmentReport(BaseModel):
    overall_score: float = Field(ge=0, le=100)
    confidence: float = Field(ge=0, le=1)
    summary: str
    matched_capabilities: list[CapabilityMatch]
    capability_gaps: list[GapAnalysis]
    evidence_mapping: list[EvidenceMapping]
    recommended_actions: list[str]
    model_metadata: dict[str, str]
