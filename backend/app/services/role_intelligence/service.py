from hashlib import sha1

from app.schemas.role import (
    RoleAnalysisRequest,
    RoleAnalysisResponse,
    RoleCapabilityRequirement,
    RoleIdentity,
    RoleTemplate,
    WorkContext,
)
from app.services.role_knowledge import RoleKnowledgeService


class RoleIntelligenceService:
    """Structured mock JD analyzer prepared for future AI service delegation."""

    def __init__(self, role_knowledge_service: RoleKnowledgeService | None = None) -> None:
        self.role_knowledge_service = role_knowledge_service or RoleKnowledgeService()

    def analyze(self, payload: RoleAnalysisRequest) -> RoleAnalysisResponse:
        if payload.role_template_id:
            template = self.role_knowledge_service.get_template(payload.role_template_id)
            if template:
                return self._analyze_template(template)
            raise ValueError(f"Unknown role template: {payload.role_template_id}")

        jd_text = (payload.job_description or "").strip()
        lowered = jd_text.lower()
        title = payload.target_role or self._infer_title(jd_text)
        role_family = self._infer_family(lowered)
        seniority = self._infer_seniority(lowered)

        capabilities = self._build_required_capabilities(lowered)
        responsibilities = self._build_responsibilities(jd_text, role_family)
        hidden_expectations = self._build_hidden_expectations(lowered, seniority)
        work_context = self._build_work_context(lowered, role_family)

        return RoleAnalysisResponse(
            role_id=self._stable_role_id(jd_text, title),
            role_identity=RoleIdentity(
                title=title,
                role_family=role_family,
                seniority=seniority,
                business_context=self._infer_context(lowered),
                confidence=0.78,
            ),
            responsibilities=responsibilities,
            required_capabilities=capabilities,
            hidden_expectations=hidden_expectations,
            work_context=work_context,
            model_metadata={
                "provider": "mock",
                "workflow": "role_intelligence",
                "version": "v2-foundation",
            },
            source="custom_jd",
        )

    def _analyze_template(self, template: RoleTemplate) -> RoleAnalysisResponse:
        capabilities = [
            RoleCapabilityRequirement(
                requirement_id=mapping.mapping_id,
                name=mapping.capability.name,
                category=mapping.capability.category,
                importance=mapping.importance,
                evidence_signal="; ".join(mapping.evidence_examples[:2]),
                confidence=mapping.confidence,
            )
            for mapping in template.capability_mappings
        ]

        return RoleAnalysisResponse(
            role_id=template.template_id,
            role_identity=RoleIdentity(
                title=template.title,
                role_family=template.role_family,
                seniority=template.seniority,
                business_context=template.business_context,
                confidence=0.86,
            ),
            responsibilities=template.responsibilities,
            required_capabilities=capabilities,
            hidden_expectations=[
                "Hiring teams will expect evidence that maps directly to the role's critical capabilities.",
                "Recommendations should be explained with assumptions, tradeoffs, and confidence signals.",
                *template.common_gaps[:2],
            ],
            work_context=WorkContext(
                environment=template.business_context,
                collaboration_model=self._template_collaboration_model(template.role_family),
                pace="Structured discovery and execution cadence with measurable capability development.",
                success_measures=[
                    "Critical capabilities are supported by concrete project or work evidence.",
                    "Common gaps are converted into targeted development actions.",
                    *template.development_actions[:2],
                ],
            ),
            model_metadata={
                "provider": "seed",
                "workflow": "role_intelligence",
                "version": "role-knowledge-foundation",
                "template_id": template.template_id,
            },
            source="role_template",
        )

    def _template_collaboration_model(self, role_family: str) -> str:
        if role_family == "Engineering":
            return "Engineering execution with product, design, and stakeholder review loops."
        if role_family in {"Product", "Data"}:
            return "Cross-functional collaboration across product, data, design, business, and engineering."
        return "Business coordination across operating teams, leadership, and delivery owners."

    def _build_required_capabilities(self, lowered: str) -> list[RoleCapabilityRequirement]:
        specs = [
            ("req-ai", "AI workflow fluency", "technical", ("ai", "llm", "machine learning", "model")),
            ("req-data", "Data analysis and SQL", "analysis", ("sql", "analytics", "dashboard", "metric")),
            ("req-product", "Product requirement reasoning", "product", ("product", "roadmap", "user", "requirement")),
            ("req-engineering", "Software delivery", "technical", ("api", "python", "typescript", "backend", "frontend")),
            ("req-stakeholder", "Stakeholder communication", "collaboration", ("stakeholder", "client", "partner", "cross-functional")),
        ]

        requirements: list[RoleCapabilityRequirement] = []
        for requirement_id, name, category, keywords in specs:
            hits = sum(1 for keyword in keywords if keyword in lowered)
            if hits or len(requirements) < 3:
                requirements.append(
                    RoleCapabilityRequirement(
                        requirement_id=requirement_id,
                        name=name,
                        category=category,
                        importance="critical" if hits >= 2 else "important",
                        evidence_signal=f"{hits} direct JD signal(s) mapped to this capability.",
                        confidence=round(min(0.92, 0.58 + hits * 0.12), 2),
                    )
                )

        return requirements

    def _build_responsibilities(self, jd_text: str, role_family: str) -> list[str]:
        lines = [
            line.strip(" -\t")
            for line in jd_text.splitlines()
            if len(line.strip(" -\t")) >= 28
        ]
        responsibilities = lines[:5]
        if responsibilities:
            return responsibilities

        return [
            f"Deliver measurable outcomes across {role_family.lower()} workflows.",
            "Translate ambiguous business needs into structured execution plans.",
            "Partner with stakeholders to validate priorities, risks, and success metrics.",
        ]

    def _build_hidden_expectations(self, lowered: str, seniority: str) -> list[str]:
        hidden = [
            "Can explain tradeoffs and assumptions, not only list tools.",
            "Shows evidence of ownership through scoped outcomes and measurable impact.",
        ]
        if seniority in {"Senior", "Lead"}:
            hidden.append("Expected to influence direction and unblock others without heavy supervision.")
        if any(keyword in lowered for keyword in ("startup", "fast-paced", "ambiguous")):
            hidden.append("Comfort with ambiguity and rapid reprioritization is likely important.")
        return hidden

    def _build_work_context(self, lowered: str, role_family: str) -> WorkContext:
        if any(keyword in lowered for keyword in ("startup", "fast-paced", "ambiguous")):
            pace = "Fast-moving environment with shifting priorities."
        elif any(keyword in lowered for keyword in ("enterprise", "compliance", "stakeholder")):
            pace = "Structured delivery cadence with heavier alignment overhead."
        else:
            pace = "Moderate delivery cadence with room for discovery and iteration."

        if role_family in {"Product", "Data"}:
            collaboration_model = "Cross-functional work with business, design, data, and engineering partners."
        elif role_family == "Engineering":
            collaboration_model = "Engineering-led execution with product and stakeholder review loops."
        else:
            collaboration_model = "Business-technology coordination across multiple stakeholder groups."

        return WorkContext(
            environment=self._infer_context(lowered),
            collaboration_model=collaboration_model,
            pace=pace,
            success_measures=[
                "Clear requirement-to-outcome traceability.",
                "Evidence of independent prioritization and execution.",
                "Measurable impact on users, operations, revenue, or delivery quality.",
            ],
        )

    def _infer_title(self, jd_text: str) -> str:
        first_line = next((line.strip() for line in jd_text.splitlines() if line.strip()), "")
        if 4 <= len(first_line) <= 80:
            return first_line.strip("#: ")
        return "Target Role"

    def _infer_family(self, lowered: str) -> str:
        if any(keyword in lowered for keyword in ("product", "roadmap", "user research")):
            return "Product"
        if any(keyword in lowered for keyword in ("sql", "analytics", "dashboard", "insight")):
            return "Data"
        if any(keyword in lowered for keyword in ("backend", "frontend", "api", "typescript", "python")):
            return "Engineering"
        return "Business Technology"

    def _infer_seniority(self, lowered: str) -> str:
        if any(keyword in lowered for keyword in ("lead", "principal", "staff")):
            return "Lead"
        if "senior" in lowered or "5+" in lowered:
            return "Senior"
        if any(keyword in lowered for keyword in ("intern", "entry", "junior", "graduate")):
            return "Entry"
        return "Mid"

    def _infer_context(self, lowered: str) -> str:
        if any(keyword in lowered for keyword in ("enterprise", "b2b", "saas")):
            return "B2B SaaS environment with stakeholder-heavy delivery."
        if any(keyword in lowered for keyword in ("consumer", "growth", "mobile")):
            return "Consumer product context with growth and user behavior signals."
        return "Technology role with cross-functional execution expectations."

    def _stable_role_id(self, jd_text: str, title: str) -> str:
        digest = sha1(f"{title}:{jd_text}".encode("utf-8")).hexdigest()[:12]
        return f"role-{digest}"
