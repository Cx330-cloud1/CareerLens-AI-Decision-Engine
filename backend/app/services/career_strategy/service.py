from app.schemas.optimization import (
    CareerAction,
    CareerPlan,
    CareerStrategyRequest,
    CareerStrategyResponse,
    GrowthPathStep,
    RecommendedProject,
)


class CareerStrategyService:
    """Structured mock planner for capability growth and evidence building."""

    def generate(self, payload: CareerStrategyRequest) -> CareerStrategyResponse:
        plan = CareerPlan(
            short_term_actions=self._short_term_actions(payload),
            medium_term_actions=self._medium_term_actions(payload),
            recommended_projects=self._recommended_projects(payload),
            capability_growth_path=self._growth_path(payload),
        )

        return CareerStrategyResponse(
            career_plan=plan,
            model_metadata={
                "provider": "mock",
                "workflow": "career_strategy",
                "version": "v1-foundation",
            },
        )

    def _short_term_actions(self, payload: CareerStrategyRequest) -> list[CareerAction]:
        optimization = payload.resume_optimization
        actions: list[CareerAction] = []

        for priority in optimization.capability_priorities[:3]:
            actions.append(
                CareerAction(
                    title=f"Reposition evidence for {priority.capability}",
                    rationale=priority.reason,
                    evidence_outcome=(
                        f"Resume contains a visible proof point for {priority.capability.lower()} "
                        "with scope, method, and result."
                    ),
                    priority=priority.priority,
                )
            )

        for missing in optimization.missing_evidence[:2]:
            actions.append(
                CareerAction(
                    title=f"Create missing proof for {missing.capability}",
                    rationale=missing.evidence_needed,
                    evidence_outcome=missing.suggested_proof,
                    priority=missing.impact_level,
                )
            )

        return actions[:5]

    def _medium_term_actions(self, payload: CareerStrategyRequest) -> list[CareerAction]:
        requirements = payload.target_role.required_capabilities
        missing = payload.resume_optimization.missing_evidence

        actions = [
            CareerAction(
                title=f"Build a role-aligned portfolio narrative for {item.capability}",
                rationale=(
                    "Medium-term readiness improves when capability claims are backed by durable "
                    "artifacts, not only resume wording."
                ),
                evidence_outcome=item.suggested_proof,
                priority=item.impact_level,
            )
            for item in missing[:3]
        ]

        if len(actions) < 3:
            actions.extend(
                CareerAction(
                    title=f"Deepen {requirement.name} signal",
                    rationale=f"{requirement.name} remains a {requirement.importance} requirement for the target role.",
                    evidence_outcome=(
                        "Publish or document one artifact that shows problem framing, execution, "
                        "tradeoffs, and measured impact."
                    ),
                    priority="medium",
                )
                for requirement in requirements[: 3 - len(actions)]
            )

        return actions[:4]

    def _recommended_projects(self, payload: CareerStrategyRequest) -> list[RecommendedProject]:
        priorities = payload.resume_optimization.capability_priorities
        target_title = payload.target_role.role_identity.title
        projects: list[RecommendedProject] = []

        for index, priority in enumerate(priorities[:3]):
            projects.append(
                RecommendedProject(
                    title=f"{priority.capability} proof project for {target_title}",
                    target_capabilities=[priority.capability],
                    evidence_to_create=(
                        "A concise case study with problem, constraints, decisions, implementation, "
                        "metric, and reflection."
                    ),
                    scope=self._project_scope(index, priority.category),
                )
            )

        return projects

    def _growth_path(self, payload: CareerStrategyRequest) -> list[GrowthPathStep]:
        missing = payload.resume_optimization.missing_evidence
        priorities = payload.resume_optimization.capability_priorities
        steps: list[GrowthPathStep] = []

        for item in missing[:4]:
            steps.append(
                GrowthPathStep(
                    capability=item.capability,
                    current_gap=item.evidence_needed,
                    next_level_signal=item.suggested_proof,
                    validation_method="Validate through a resume proof point, portfolio artifact, and interview story.",
                )
            )

        if len(steps) < 4:
            steps.extend(
                GrowthPathStep(
                    capability=priority.capability,
                    current_gap=priority.reason,
                    next_level_signal=(
                        f"Evidence makes {priority.capability.lower()} legible within the first resume scan."
                    ),
                    validation_method="Compare the proof point against the target role requirement and expected evidence signal.",
                )
                for priority in priorities[: 4 - len(steps)]
            )

        return steps[:4]

    def _project_scope(self, index: int, category: str) -> str:
        if "technical" in category.lower():
            return "Two-week build with a working artifact, architecture notes, and outcome metrics."
        if "analysis" in category.lower() or "data" in category.lower():
            return "One-week analysis case with dataset, decision memo, dashboard, and insight quality review."
        if index == 0:
            return "Ten-day flagship case study focused on the highest-priority target capability."
        return "Five-day scoped project designed to produce one credible resume proof point."
