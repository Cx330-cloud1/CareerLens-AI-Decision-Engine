from app.schemas.profile import ProfileAnalysisRequest, ProfileAnalysisResponse


class ProfileService:
    """Structured mock analyzer for talent profile commands."""

    def analyze(self, payload: ProfileAnalysisRequest) -> ProfileAnalysisResponse:
        primary_role = self._first(payload.target_roles, "target role")
        primary_skill = self._first(payload.skills, "core capability")
        education_summary = self._first(payload.education, "documented education background")
        project_summary = self._first(payload.projects, "project evidence")

        capabilities = self._build_capabilities(payload.skills, payload.projects)
        evidence = self._build_evidence(payload.education, payload.projects)
        strengths = self._build_strengths(payload.skills, payload.projects)
        gaps = self._build_gaps(payload)
        recommended_roles = self._build_roles(payload.target_roles, payload.skills)

        career_identity = (
            f"A {primary_role} candidate with a foundation in {education_summary}, "
            f"practical exposure through {project_summary}, and a strongest current signal in "
            f"{primary_skill}. The profile is best positioned for roles that value structured "
            "problem solving, evidence-backed execution, and fast learning in applied work."
        )

        return ProfileAnalysisResponse(
            career_identity=career_identity,
            capabilities=capabilities,
            evidence=evidence,
            strengths=strengths,
            gaps=gaps,
            recommended_roles=recommended_roles,
        )

    def _build_capabilities(self, skills: list[str], projects: list[str]) -> list[str]:
        capabilities = [
            f"Applied capability in {skill}" for skill in skills[:6]
        ]

        if projects:
            capabilities.append("Can translate project experience into business-facing outcomes")

        return capabilities or [
            "Baseline professional capability needs more concrete skill evidence",
            "Initial profile is ready for structured enrichment",
        ]

    def _build_evidence(self, education: list[str], projects: list[str]) -> list[str]:
        evidence = [f"Education signal: {item}" for item in education[:3]]
        evidence.extend(f"Project signal: {item}" for item in projects[:4])

        return evidence or [
            "No education or project evidence was provided; add dated examples and measurable outcomes"
        ]

    def _build_strengths(self, skills: list[str], projects: list[str]) -> list[str]:
        strengths: list[str] = []

        if len(skills) >= 3:
            strengths.append("Broad skill base with enough material for role-specific positioning")
        if projects:
            strengths.append("Project experience provides concrete proof points for interviews")
        if any(self._mentions_data_or_ai(skill) for skill in skills):
            strengths.append("Clear technical signal in data, AI, or analytical workflows")

        return strengths or [
            "Early-stage profile with room to develop a sharper professional narrative"
        ]

    def _build_gaps(self, payload: ProfileAnalysisRequest) -> list[str]:
        gaps: list[str] = []

        if not payload.target_roles:
            gaps.append("Define target roles to make the analysis and positioning more precise")
        if len(payload.projects) < 2:
            gaps.append("Add at least two projects with scope, tools, decisions, and measurable results")
        if len(payload.skills) < 5:
            gaps.append("Expand the skill inventory with role-critical tools and domain keywords")
        if not payload.education:
            gaps.append("Add education, certificates, or training signals to support baseline credibility")

        return gaps or [
            "Next improvement is to quantify impact and map each project to the selected roles"
        ]

    def _build_roles(self, target_roles: list[str], skills: list[str]) -> list[str]:
        roles = target_roles[:4]

        skill_text = " ".join(skills).lower()
        if not roles:
            if "python" in skill_text or "sql" in skill_text or "data" in skill_text:
                roles = ["Data Analyst", "Business Intelligence Analyst"]
            elif "product" in skill_text:
                roles = ["Associate Product Manager", "Product Operations Analyst"]
            else:
                roles = ["Junior Business Analyst", "Operations Analyst"]

        return roles

    def _first(self, values: list[str], fallback: str) -> str:
        return values[0] if values else fallback

    def _mentions_data_or_ai(self, value: str) -> bool:
        lowered = value.lower()
        return any(keyword in lowered for keyword in ("data", "ai", "ml", "python", "sql"))
