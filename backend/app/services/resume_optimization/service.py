from app.schemas.matching import GapAnalysis
from app.schemas.optimization import (
    CapabilityPriority,
    EvidenceImprovement,
    ExperienceReframing,
    MissingEvidence,
    ResumeOptimization,
    ResumeOptimizationRequest,
    ResumeOptimizationResponse,
)
from app.schemas.resume import CapabilityEvidence
from app.schemas.role import RoleCapabilityRequirement


class ResumeOptimizationService:
    """Structured mock optimizer that turns fit gaps into resume positioning work."""

    def optimize(self, payload: ResumeOptimizationRequest) -> ResumeOptimizationResponse:
        gaps = payload.alignment_gaps
        if not gaps and payload.alignment_report:
            gaps = payload.alignment_report.capability_gaps
        requirements = payload.target_role.required_capabilities

        optimization = ResumeOptimization(
            capability_priorities=self._capability_priorities(requirements, gaps),
            evidence_improvements=self._evidence_improvements(payload.resume_evidence, requirements),
            experience_reframing=self._experience_reframing(payload.resume_evidence, requirements),
            missing_evidence=self._missing_evidence(gaps, requirements),
        )

        return ResumeOptimizationResponse(
            resume_optimization=optimization,
            model_metadata={
                "provider": "mock",
                "workflow": "resume_optimization",
                "version": "v1-foundation",
            },
        )

    def _capability_priorities(
        self,
        requirements: list[RoleCapabilityRequirement],
        gaps: list[GapAnalysis],
    ) -> list[CapabilityPriority]:
        gap_names = {gap.capability.lower(): gap for gap in gaps}
        priorities: list[CapabilityPriority] = []

        for requirement in requirements:
            gap = gap_names.get(requirement.name.lower())
            priority = "high" if gap else self._priority_from_importance(requirement.importance)
            reason = (
                gap.what_is_missing
                if gap
                else f"{requirement.name} is a {requirement.importance} role requirement and should be visible in the first resume scan."
            )
            priorities.append(
                CapabilityPriority(
                    capability=requirement.name,
                    category=requirement.category,
                    priority=priority,
                    reason=reason,
                    confidence=round(min(0.92, requirement.confidence + (0.08 if gap else 0.02)), 2),
                )
            )

        return priorities[:6]

    def _evidence_improvements(
        self,
        evidence: list[CapabilityEvidence],
        requirements: list[RoleCapabilityRequirement],
    ) -> list[EvidenceImprovement]:
        if not evidence:
            return []

        improvements: list[EvidenceImprovement] = []
        for index, item in enumerate(evidence[:6]):
            requirement = requirements[index % len(requirements)] if requirements else None
            capability = requirement.name if requirement else item.source_section.title()
            improvements.append(
                EvidenceImprovement(
                    evidence_id=item.evidence_id,
                    capability=capability,
                    current_signal=item.excerpt,
                    improvement=(
                        f"Make this proof point explicitly show {capability.lower()} through context, "
                        "candidate decision, tool or method, and measurable outcome."
                    ),
                    quality_target=self._quality_target(item.strength),
                    confidence=round(min(0.9, item.confidence + 0.08), 2),
                )
            )

        return improvements

    def _experience_reframing(
        self,
        evidence: list[CapabilityEvidence],
        requirements: list[RoleCapabilityRequirement],
    ) -> list[ExperienceReframing]:
        reframes: list[ExperienceReframing] = []
        target_requirements = requirements[: max(1, min(3, len(requirements)))]

        for index, requirement in enumerate(target_requirements):
            source = evidence[index % len(evidence)] if evidence else None
            before = source.excerpt if source else "No resume evidence supplied for this capability."
            reframes.append(
                ExperienceReframing(
                    source_section=source.source_section if source else "resume",
                    target_capability=requirement.name,
                    framing_guidance=(
                        "Position the experience around role capability proof, not task completion. "
                        "Lead with the business or user problem, then the decision and result."
                    ),
                    before_signal=before,
                    after_positioning=(
                        f"Demonstrated {requirement.name.lower()} by solving a scoped problem, "
                        "choosing an approach, and reporting a measurable outcome."
                    ),
                )
            )

        return reframes

    def _missing_evidence(
        self,
        gaps: list[GapAnalysis],
        requirements: list[RoleCapabilityRequirement],
    ) -> list[MissingEvidence]:
        if gaps:
            return [
                MissingEvidence(
                    capability=gap.capability,
                    evidence_needed=gap.evidence_needed,
                    suggested_proof=gap.recommended_action,
                    impact_level=gap.impact_level,
                )
                for gap in gaps[:6]
            ]

        return [
            MissingEvidence(
                capability=requirement.name,
                evidence_needed=requirement.evidence_signal,
                suggested_proof=(
                    f"Add one quantified project bullet that proves {requirement.name.lower()} "
                    "under realistic role constraints."
                ),
                impact_level=self._impact_from_importance(requirement.importance),
            )
            for requirement in requirements[:3]
        ]

    def _priority_from_importance(self, importance: str) -> str:
        if importance == "critical":
            return "high"
        if importance == "important":
            return "medium"
        return "low"

    def _impact_from_importance(self, importance: str) -> str:
        if importance == "critical":
            return "high"
        if importance == "important":
            return "medium"
        return "low"

    def _quality_target(self, strength: str) -> str:
        if strength == "strong":
            return "Connect this strong proof to the exact target role requirement and keep the metric visible."
        if strength == "moderate":
            return "Add missing scope or result so the evidence becomes independently verifiable."
        return "Rewrite with context, action, tools, and outcome; weak claims should become proof points."
