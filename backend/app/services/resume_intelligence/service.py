from hashlib import sha1
from uuid import uuid4

from app.schemas.resume import (
    CandidateIdentity,
    CapabilityCard,
    CapabilityEvidence,
    ImprovementSuggestion,
    ResumeAnalysisResponse,
    ResumeUploadRequest,
)


class ResumeIntelligenceService:
    """Mock structured resume analyzer prepared for future AI service delegation."""

    def analyze(self, payload: ResumeUploadRequest) -> ResumeAnalysisResponse:
        resume_text = payload.resume_text.strip()
        evidence = self._build_evidence(resume_text)
        capabilities = self._build_capabilities(resume_text, evidence)
        identity = self._build_identity(payload.file_name, resume_text)
        suggestions = self._build_suggestions(resume_text, capabilities)

        return ResumeAnalysisResponse(
            resume_id=self._stable_resume_id(payload),
            parsing_status="succeeded" if resume_text else "artifact_received",
            candidate_identity=identity,
            capabilities=capabilities,
            experience_evidence=evidence,
            improvement_suggestions=suggestions,
            model_metadata={
                "provider": "mock",
                "workflow": "resume_intelligence",
                "version": "v2-foundation",
            },
        )

    def _build_identity(self, file_name: str, resume_text: str) -> CandidateIdentity:
        role_direction = self._infer_direction(resume_text)
        evidence_note = (
            "Resume text was parsed into early capability signals."
            if resume_text
            else "The uploaded artifact is registered; detailed extraction will improve when PDF parsing is connected."
        )

        return CandidateIdentity(
            headline=f"{role_direction} candidate",
            target_direction=role_direction,
            summary=(
                f"{file_name} indicates a candidate best reviewed through evidence-backed "
                f"{role_direction.lower()} capabilities. {evidence_note}"
            ),
            confidence=0.72 if resume_text else 0.48,
        )

    def _build_evidence(self, resume_text: str) -> list[CapabilityEvidence]:
        lines = [
            line.strip(" -•\t")
            for line in resume_text.splitlines()
            if len(line.strip(" -•\t")) >= 24
        ]
        selected_lines = lines[:5] or [
            "Uploaded resume artifact is available for analysis, but no extractable text was provided.",
            "Use pasted resume text to preview evidence-level analysis before PDF extraction is implemented.",
        ]

        return [
            CapabilityEvidence(
                evidence_id=f"ev-{index + 1}",
                excerpt=line,
                source_section=self._infer_section(line),
                strength=self._infer_strength(line),
                confidence=0.78 if resume_text else 0.42,
            )
            for index, line in enumerate(selected_lines)
        ]

    def _build_capabilities(
        self,
        resume_text: str,
        evidence: list[CapabilityEvidence],
    ) -> list[CapabilityCard]:
        lowered = resume_text.lower()
        capability_specs = [
            ("cap-technical", "Technical execution", "technical", ("python", "sql", "api", "model", "data")),
            ("cap-analysis", "Analytical problem solving", "analysis", ("analysis", "metric", "insight", "dashboard")),
            ("cap-product", "Product and user reasoning", "product", ("product", "user", "market", "requirement")),
            ("cap-collaboration", "Cross-functional collaboration", "collaboration", ("stakeholder", "team", "client", "partner")),
        ]

        cards: list[CapabilityCard] = []
        for capability_id, name, category, keywords in capability_specs:
            keyword_hits = sum(1 for keyword in keywords if keyword in lowered)
            if keyword_hits or len(cards) < 2:
                confidence = min(0.9, 0.52 + keyword_hits * 0.12 + len(evidence) * 0.02)
                cards.append(
                    CapabilityCard(
                        capability_id=capability_id,
                        name=name,
                        category=category,
                        level=self._level_from_confidence(confidence),
                        confidence=round(confidence, 2),
                        rationale=(
                            f"Inferred from {keyword_hits} keyword signals and "
                            f"{len(evidence)} evidence records."
                        ),
                        evidence_ids=[item.evidence_id for item in evidence[:3]],
                    )
                )

        return cards

    def _build_suggestions(
        self,
        resume_text: str,
        capabilities: list[CapabilityCard],
    ) -> list[ImprovementSuggestion]:
        suggestions = [
            ImprovementSuggestion(
                suggestion_id="sug-evidence-metrics",
                title="Add measurable outcomes to key experience bullets",
                rationale="Evidence strength improves when achievements include scope, metric, and business result.",
                priority="high",
                confidence=0.86,
            ),
            ImprovementSuggestion(
                suggestion_id="sug-role-map",
                title="Map strongest projects to target role capabilities",
                rationale="Capability cards should connect each project to explicit role requirements in the next workflow.",
                priority="medium",
                confidence=0.78,
            ),
        ]

        if not resume_text:
            suggestions.insert(
                0,
                ImprovementSuggestion(
                    suggestion_id="sug-paste-text",
                    title="Provide extracted or pasted resume text",
                    rationale="The mock analyzer can register a PDF, but stronger evidence cards require text extraction.",
                    priority="high",
                    confidence=0.9,
                ),
            )

        if len(capabilities) < 4:
            suggestions.append(
                ImprovementSuggestion(
                    suggestion_id="sug-broaden-evidence",
                    title="Add evidence for collaboration, product, or domain capabilities",
                    rationale="Current evidence concentrates on a narrow capability set and may understate role readiness.",
                    priority="medium",
                    confidence=0.72,
                )
            )

        return suggestions

    def _stable_resume_id(self, payload: ResumeUploadRequest) -> str:
        if not payload.resume_text:
            return str(uuid4())

        digest = sha1(payload.resume_text.encode("utf-8")).hexdigest()[:12]
        return f"resume-{digest}"

    def _infer_direction(self, resume_text: str) -> str:
        lowered = resume_text.lower()
        if any(keyword in lowered for keyword in ("machine learning", "ml", "model", "llm", "ai")):
            return "AI Engineering"
        if any(keyword in lowered for keyword in ("product", "roadmap", "user research")):
            return "AI Product"
        if any(keyword in lowered for keyword in ("sql", "dashboard", "analytics", "bi")):
            return "Data Analytics"
        return "Technology"

    def _infer_section(self, text: str) -> str:
        lowered = text.lower()
        if any(keyword in lowered for keyword in ("university", "degree", "gpa", "course")):
            return "education"
        if any(keyword in lowered for keyword in ("project", "built", "developed", "launched")):
            return "project"
        if any(keyword in lowered for keyword in ("intern", "company", "team", "client")):
            return "experience"
        return "resume"

    def _infer_strength(self, text: str) -> str:
        lowered = text.lower()
        has_metric = any(character.isdigit() for character in text) or "%" in text
        has_action = any(keyword in lowered for keyword in ("built", "led", "improved", "reduced", "launched"))
        if has_metric and has_action:
            return "strong"
        if has_metric or has_action:
            return "moderate"
        return "weak"

    def _level_from_confidence(self, confidence: float) -> str:
        if confidence >= 0.78:
            return "strong"
        if confidence >= 0.62:
            return "working"
        return "emerging"
