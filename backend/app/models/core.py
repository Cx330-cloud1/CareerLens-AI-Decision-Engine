from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    id: UUID
    email: EmailStr
    display_name: str | None = None
    locale: str = "en-US"


class TalentProfile(BaseModel):
    id: UUID
    user_id: UUID
    headline: str | None = None
    target_seniority: str | None = None
    primary_path: str | None = None
    completeness_score: float = Field(default=0, ge=0, le=100)


class Resume(BaseModel):
    id: UUID
    user_id: UUID | None = None
    title: str
    source_type: str = "pdf_upload"
    raw_text: str | None = None
    parsing_status: str = "pending"


class Capability(BaseModel):
    id: UUID
    name: str
    category: str
    level: str
    confidence: float = Field(ge=0, le=1)
    rationale: str


class ResumeEvidence(BaseModel):
    id: UUID
    resume_id: UUID
    evidence_type: str
    text: str
    confidence: float = Field(ge=0, le=1)


class Company(BaseModel):
    id: UUID
    name: str
    slug: str
    industry: str | None = None
    ai_strategy: str | None = None


class Role(BaseModel):
    id: UUID
    role_name: str
    role_family: str
    seniority: str | None = None
    required_skills: list[str] = Field(default_factory=list)


class RoleRequirement(BaseModel):
    id: UUID
    role_id: UUID | None = None
    role_identity: dict[str, str | float]
    responsibilities: list[str] = Field(default_factory=list)
    required_capabilities: list[dict[str, str | float]] = Field(default_factory=list)
    hidden_expectations: list[str] = Field(default_factory=list)
    work_context: dict[str, str | list[str]] = Field(default_factory=dict)


class AlignmentReport(BaseModel):
    id: UUID
    role_requirement_id: UUID | None = None
    resume_id: UUID | None = None
    overall_score: float = Field(ge=0, le=100)
    confidence: float = Field(ge=0, le=1)
    summary: str
    matched_capabilities: list["CapabilityMatch"] = Field(default_factory=list)
    capability_gaps: list["GapAnalysis"] = Field(default_factory=list)
    evidence_mapping: list[dict[str, str | float | list["EvidenceLink"]]] = Field(
        default_factory=list
    )
    recommended_actions: list[str] = Field(default_factory=list)
    created_at: datetime


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


class MatchReport(BaseModel):
    id: UUID
    user_id: UUID
    profile_id: UUID
    target_id: UUID
    overall_score: float = Field(ge=0, le=100)
    confidence_level: str
    recommendation: str
    created_at: datetime


class CareerPlan(BaseModel):
    id: UUID
    user_id: UUID
    profile_id: UUID
    title: str
    summary: str | None = None


class KnowledgeSource(BaseModel):
    id: UUID
    source_type: str
    title: str
    uri: str | None = None
    freshness_label: str | None = None
