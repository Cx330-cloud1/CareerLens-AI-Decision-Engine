from pydantic import BaseModel, Field


class ProfileAnalysisRequest(BaseModel):
    education: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    projects: list[str] = Field(default_factory=list)
    target_roles: list[str] = Field(default_factory=list)


class ProfileAnalysisResponse(BaseModel):
    career_identity: str
    capabilities: list[str]
    evidence: list[str]
    strengths: list[str]
    gaps: list[str]
    recommended_roles: list[str]
