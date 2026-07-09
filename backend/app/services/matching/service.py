from app.schemas.matching import (
    AlignmentAnalysisRequest,
    AlignmentReport,
    CapabilityMatch,
    CandidateCapabilityInput,
    EvidenceLink,
    EvidenceMapping,
    GapAnalysis,
)
from app.schemas.role import RoleCapabilityRequirement


class MatchingService:
    """Structured mock creator for explainable candidate-role alignment."""

    def analyze(self, payload: AlignmentAnalysisRequest) -> AlignmentReport:
        requirements = self._requirements(payload)
        candidate_capabilities = self._candidate_capabilities(payload)

        matched_capabilities: list[CapabilityMatch] = []
        capability_gaps: list[GapAnalysis] = []
        evidence_mapping: list[EvidenceMapping] = []

        for requirement in requirements:
            best_candidate = self._best_candidate(requirement, candidate_capabilities)
            evidence_links = self._evidence_links(requirement, best_candidate, payload)
            candidate_signal = self._candidate_signal(best_candidate, evidence_links)
            score = self._score(requirement.name, candidate_signal)
            confidence = self._confidence(requirement, best_candidate, evidence_links, score)

            if score >= 45 and best_candidate:
                missing_evidence = None
                if score < 72:
                    missing_evidence = (
                        f"Evidence supports {requirement.name}, but needs clearer scope, decisions, "
                        "or measurable outcome to validate depth."
                    )

                matched_capabilities.append(
                    CapabilityMatch(
                        capability=requirement.name,
                        category=requirement.category,
                        score=score,
                        confidence=confidence,
                        why_it_matches=(
                            f"The candidate shows {best_candidate.name.lower()} signals that overlap "
                            f"with this {requirement.importance} {requirement.category} requirement."
                        ),
                        supporting_evidence=evidence_links,
                        missing_evidence=missing_evidence,
                    )
                )
                evidence_mapping.append(
                    EvidenceMapping(
                        requirement=requirement.name,
                        evidence_links=evidence_links,
                        assessment=self._evidence_assessment(score),
                        confidence=confidence,
                    )
                )
            else:
                capability_gaps.append(
                    GapAnalysis(
                        capability=requirement.name,
                        category=requirement.category,
                        impact_level=self._impact_level(requirement.importance),
                        what_is_missing=(
                            "No strong candidate capability signal was found for this role requirement."
                        ),
                        evidence_needed=(
                            requirement.evidence_signal
                            or "Project, work, or coursework proof with tools, decisions, and outcome."
                        ),
                        recommended_action=(
                            f"Create a targeted proof point for {requirement.name.lower()} with context, "
                            "action, and measurable result."
                        ),
                    )
                )
                evidence_mapping.append(
                    EvidenceMapping(
                        requirement=requirement.name,
                        evidence_links=evidence_links,
                        assessment="Requirement is currently unsupported by candidate evidence.",
                        confidence=0.56,
                    )
                )

        overall_score = self._overall_score(matched_capabilities, len(requirements))
        confidence = self._overall_confidence(
            matched_capabilities,
            capability_gaps,
            bool(candidate_capabilities),
        )

        return AlignmentReport(
            overall_score=overall_score,
            confidence=confidence,
            summary=self._summary(overall_score, confidence, matched_capabilities, capability_gaps),
            matched_capabilities=matched_capabilities,
            capability_gaps=capability_gaps,
            evidence_mapping=evidence_mapping,
            recommended_actions=self._suggestions(capability_gaps, matched_capabilities),
            model_metadata={
                "provider": "mock",
                "workflow": "alignment_engine",
                "version": "v3-foundation",
            },
        )

    def _requirements(self, payload: AlignmentAnalysisRequest) -> list[RoleCapabilityRequirement]:
        if payload.role_requirement:
            return payload.role_requirement.required_capabilities

        if payload.selected_role_template:
            return [
                RoleCapabilityRequirement(
                    requirement_id=mapping.mapping_id,
                    name=mapping.capability.name,
                    category=mapping.capability.category,
                    importance=mapping.importance,
                    evidence_signal=", ".join(mapping.evidence_examples[:2]),
                    confidence=mapping.confidence,
                )
                for mapping in payload.selected_role_template.capability_mappings
            ]

        return []

    def _candidate_capabilities(
        self,
        payload: AlignmentAnalysisRequest,
    ) -> list[CandidateCapabilityInput]:
        capabilities = list(payload.candidate_capabilities)

        if payload.candidate_profile:
            capabilities.extend(
                CandidateCapabilityInput(
                    name=capability,
                    evidence=" ".join(payload.candidate_profile.evidence),
                    confidence=0.64,
                )
                for capability in payload.candidate_profile.capabilities
            )

        if payload.resume_evidence and not capabilities:
            capabilities.extend(
                CandidateCapabilityInput(
                    name=item.source_section.title(),
                    category=item.source_section,
                    evidence=item.excerpt,
                    confidence=item.confidence,
                )
                for item in payload.resume_evidence
            )

        return capabilities

    def _best_candidate(
        self,
        requirement: RoleCapabilityRequirement,
        candidates: list[CandidateCapabilityInput],
    ) -> CandidateCapabilityInput | None:
        scored = [
            (
                self._score(
                    f"{requirement.name} {requirement.category} {requirement.evidence_signal}",
                    f"{candidate.name} {candidate.category} {candidate.evidence}",
                ),
                candidate,
            )
            for candidate in candidates
        ]
        if not scored:
            return None
        return max(scored, key=lambda item: item[0])[1]

    def _evidence_links(
        self,
        requirement: RoleCapabilityRequirement,
        candidate: CandidateCapabilityInput | None,
        payload: AlignmentAnalysisRequest,
    ) -> list[EvidenceLink]:
        links: list[EvidenceLink] = []

        for item in payload.resume_evidence:
            score = self._score(requirement.name, item.excerpt)
            if score >= 30 or not links:
                links.append(
                    EvidenceLink(
                        evidence_id=item.evidence_id,
                        source_section=item.source_section,
                        excerpt=item.excerpt,
                        relevance=self._evidence_assessment(score),
                        confidence=round(min(0.92, item.confidence + score / 500), 2),
                    )
                )
            if len(links) == 2:
                return links

        if candidate and candidate.evidence:
            links.append(
                EvidenceLink(
                    evidence_id=f"candidate-{self._slug(candidate.name)}",
                    source_section=candidate.category,
                    excerpt=candidate.evidence,
                    relevance="Candidate-provided capability evidence is the closest available signal.",
                    confidence=candidate.confidence,
                )
            )

        return links[:2]

    def _candidate_signal(
        self,
        candidate: CandidateCapabilityInput | None,
        evidence_links: list[EvidenceLink],
    ) -> str:
        evidence_text = " ".join(link.excerpt for link in evidence_links)
        if not candidate:
            return evidence_text
        return f"{candidate.name} {candidate.category} {candidate.evidence} {evidence_text}"

    def _score(self, requirement: str, candidate_signal: str) -> float:
        requirement_tokens = self._tokens(requirement)
        candidate_tokens = self._tokens(candidate_signal)
        if not requirement_tokens or not candidate_tokens:
            return 0
        overlap = len(requirement_tokens & candidate_tokens)
        related = self._related_overlap(requirement_tokens, candidate_tokens)
        return round(min(100, ((overlap + related * 0.65) / len(requirement_tokens)) * 100), 1)

    def _related_overlap(self, requirement_tokens: set[str], candidate_tokens: set[str]) -> int:
        groups = [
            {"ai", "llm", "model", "machine", "learning", "workflow"},
            {"data", "analysis", "analytics", "sql", "dashboard", "metric"},
            {"product", "user", "requirement", "roadmap"},
            {"software", "engineering", "api", "backend", "frontend", "python", "typescript"},
            {"stakeholder", "communication", "collaboration", "client", "cross", "functional"},
        ]
        return sum(
            1
            for group in groups
            if requirement_tokens & group and candidate_tokens & group
        )

    def _tokens(self, value: str) -> set[str]:
        return {
            token.strip(".,:;()[]{}").lower()
            for token in value.replace("-", " ").split()
            if len(token.strip(".,:;()[]{}")) >= 3
        }

    def _overall_score(self, matches: list[CapabilityMatch], requirement_count: int) -> float:
        if requirement_count == 0:
            return 0
        matched_score = sum(match.score for match in matches)
        return round(matched_score / requirement_count, 1)

    def _confidence(
        self,
        requirement: RoleCapabilityRequirement,
        candidate: CandidateCapabilityInput | None,
        evidence_links: list[EvidenceLink],
        score: float,
    ) -> float:
        if not candidate and not evidence_links:
            return 0.42

        candidate_confidence = candidate.confidence if candidate else 0.5
        evidence_confidence = (
            sum(item.confidence for item in evidence_links) / len(evidence_links)
            if evidence_links
            else candidate_confidence
        )
        score_factor = min(0.16, score / 600)
        base_confidence = (
            candidate_confidence + evidence_confidence + requirement.confidence
        ) / 3
        return round(min(0.94, base_confidence + score_factor), 2)

    def _overall_confidence(
        self,
        matches: list[CapabilityMatch],
        gaps: list[GapAnalysis],
        has_candidate_input: bool,
    ) -> float:
        if not has_candidate_input:
            return 0.38
        if not matches:
            return 0.5
        base = sum(match.confidence for match in matches) / len(matches)
        gap_penalty = min(0.18, len(gaps) * 0.03)
        return round(max(0.36, base - gap_penalty), 2)

    def _summary(
        self,
        score: float,
        confidence: float,
        matches: list[CapabilityMatch],
        gaps: list[GapAnalysis],
    ) -> str:
        if not matches and not gaps:
            return "No role requirements were available for alignment."

        if score >= 75:
            stance = "Strong alignment"
        elif score >= 50:
            stance = "Plausible alignment with visible development areas"
        else:
            stance = "Early alignment that needs stronger proof"

        return (
            f"{stance}: {len(matches)} capabilities have supporting evidence and "
            f"{len(gaps)} capability gaps need attention. Report confidence is "
            f"{round(confidence * 100)}% based on the supplied resume evidence."
        )

    def _evidence_assessment(self, score: float) -> str:
        if score >= 50:
            return "Evidence directly supports the role requirement."
        if score >= 30:
            return "Evidence partially supports the requirement but needs clearer role context."
        return "Evidence is weakly related and should not be treated as proof yet."

    def _impact_level(self, importance: str) -> str:
        if importance == "critical":
            return "high"
        if importance == "important":
            return "medium"
        return "low"

    def _suggestions(
        self,
        gaps: list[GapAnalysis],
        matches: list[CapabilityMatch],
    ) -> list[str]:
        if not gaps:
            return [
                "Convert matched capabilities into interview stories with context, action, and measurable impact.",
                "Prepare one risk narrative for the weakest matched requirement.",
            ]

        actions = [gap.recommended_action for gap in gaps[:4]]
        if matches:
            actions.append(
                f"Strengthen {matches[0].capability.lower()} by adding one metric-backed outcome."
            )
        return actions

    def _slug(self, value: str) -> str:
        tokens = self._tokens(value)
        return "-".join(sorted(tokens)) or "evidence"
