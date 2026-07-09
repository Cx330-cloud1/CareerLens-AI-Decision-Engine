from pydantic import BaseModel, Field, model_validator


class RoleAnalysisRequest(BaseModel):
    job_description: str | None = None
    target_role: str | None = None
    role_template_id: str | None = None

    @model_validator(mode="after")
    def validate_role_input(self) -> "RoleAnalysisRequest":
        has_jd = bool(self.job_description and len(self.job_description.strip()) >= 20)
        has_template = bool(self.role_template_id)
        if not has_jd and not has_template:
            raise ValueError("Provide a role_template_id or a job_description with at least 20 characters.")
        return self


class RoleIdentity(BaseModel):
    title: str
    role_family: str
    seniority: str
    business_context: str
    confidence: float = Field(ge=0, le=1)


class RoleCapabilityRequirement(BaseModel):
    requirement_id: str
    name: str
    category: str
    importance: str
    evidence_signal: str
    confidence: float = Field(ge=0, le=1)


class WorkContext(BaseModel):
    environment: str
    collaboration_model: str
    pace: str
    success_measures: list[str]


class RoleRequirement(BaseModel):
    role_identity: RoleIdentity
    responsibilities: list[str]
    required_capabilities: list[RoleCapabilityRequirement]
    hidden_expectations: list[str]
    work_context: WorkContext
    model_metadata: dict[str, str]


class RoleAnalysisResponse(RoleRequirement):
    role_id: str
    source: str = "custom_jd"


class CareerCategory(BaseModel):
    category_id: str
    name: str
    description: str
    role_count: int = 0


class Capability(BaseModel):
    capability_id: str
    name: str
    category: str
    description: str


class RoleCapabilityMapping(BaseModel):
    mapping_id: str
    capability: Capability
    importance: str
    evidence_examples: list[str]
    common_gaps: list[str]
    development_actions: list[str]
    confidence: float = Field(ge=0, le=1)


class RoleTemplate(BaseModel):
    template_id: str
    category_id: str
    title: str
    role_family: str
    seniority: str
    summary: str
    business_context: str
    responsibilities: list[str]
    capability_mappings: list[RoleCapabilityMapping]
    common_gaps: list[str]
    development_actions: list[str]


class RoleTemplateListResponse(BaseModel):
    categories: list[CareerCategory]
    templates: list[RoleTemplate]
