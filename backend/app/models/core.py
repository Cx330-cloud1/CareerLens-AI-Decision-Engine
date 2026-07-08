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
