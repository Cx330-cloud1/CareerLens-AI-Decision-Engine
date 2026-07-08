from pydantic import BaseModel, Field


class ResumeUploadRequest(BaseModel):
    file_name: str = Field(min_length=1)
    content_type: str | None = None
    file_size: int = Field(default=0, ge=0)
    resume_text: str = ""


class CandidateIdentity(BaseModel):
    name: str | None = None
    headline: str
    target_direction: str
    summary: str
    confidence: float = Field(ge=0, le=1)


class CapabilityEvidence(BaseModel):
    evidence_id: str
    excerpt: str
    source_section: str
    strength: str
    confidence: float = Field(ge=0, le=1)


class CapabilityCard(BaseModel):
    capability_id: str
    name: str
    category: str
    level: str
    confidence: float = Field(ge=0, le=1)
    rationale: str
    evidence_ids: list[str] = Field(default_factory=list)


class ImprovementSuggestion(BaseModel):
    suggestion_id: str
    title: str
    rationale: str
    priority: str
    confidence: float = Field(ge=0, le=1)


class ResumeAnalysisResponse(BaseModel):
    resume_id: str
    parsing_status: str
    candidate_identity: CandidateIdentity
    capabilities: list[CapabilityCard]
    experience_evidence: list[CapabilityEvidence]
    improvement_suggestions: list[ImprovementSuggestion]
    model_metadata: dict[str, str]
