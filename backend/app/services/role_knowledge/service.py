import json
from functools import cached_property
from pathlib import Path

from app.schemas.role import CareerCategory, Capability, RoleCapabilityMapping, RoleTemplate


class RoleKnowledgeService:
    """Seed-backed role knowledge base for career exploration and template analysis."""

    def __init__(self, seed_path: Path | None = None) -> None:
        self.seed_path = seed_path or Path(__file__).resolve().parents[4] / "data" / "seeds" / "role_knowledge.json"

    @cached_property
    def _seed(self) -> dict:
        with self.seed_path.open(encoding="utf-8") as seed_file:
            return json.load(seed_file)

    @cached_property
    def _capabilities_by_id(self) -> dict[str, Capability]:
        return {
            item["capability_id"]: Capability(**item)
            for item in self._seed.get("capabilities", [])
        }

    def list_categories(self) -> list[CareerCategory]:
        templates = self.list_templates()
        return [
            CareerCategory(
                **category,
                role_count=sum(1 for template in templates if template.category_id == category["category_id"]),
            )
            for category in self._seed.get("categories", [])
        ]

    def list_templates(self, query: str | None = None, category_id: str | None = None) -> list[RoleTemplate]:
        templates = [self._build_template(item) for item in self._seed.get("templates", [])]

        if category_id:
            templates = [template for template in templates if template.category_id == category_id]

        if query:
            normalized_query = query.strip().lower()
            templates = [
                template
                for template in templates
                if normalized_query in template.title.lower()
                or normalized_query in template.summary.lower()
                or normalized_query in template.role_family.lower()
            ]

        return templates

    def get_template(self, template_id: str) -> RoleTemplate | None:
        return next(
            (template for template in self.list_templates() if template.template_id == template_id),
            None,
        )

    def _build_template(self, item: dict) -> RoleTemplate:
        mappings = []
        for mapping in item.get("capability_mappings", []):
            capability = self._capabilities_by_id[mapping["capability_id"]]
            mapping_payload = {key: value for key, value in mapping.items() if key != "capability_id"}
            mappings.append(RoleCapabilityMapping(**mapping_payload, capability=capability))

        return RoleTemplate(**{**item, "capability_mappings": mappings})
