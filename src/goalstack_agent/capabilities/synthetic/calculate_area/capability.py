from dataclasses import dataclass
from typing import Any

from goalstack_agent.capabilities.base import CapabilityResult, FactRequirement


@dataclass
class CalculateAreaCapability:
    name: str = "calculate_area"
    description: str = "Calculate area from width and height."

    def required_facts(
        self,
        *,
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> list[FactRequirement]:
        return [

            FactRequirement(name="width", description="Table width", type_hint="number"),
            FactRequirement(name="height", description="Table height", type_hint="number"),
        ]

    def invoke(
        self,
        *,
        facts: dict[str, Any],
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> CapabilityResult:
        missing = [name for name in ("width", "height") if name not in facts]
        if missing:
            return CapabilityResult(
                capability_name=self.name,
                output={},
                success=False,
                error=f"Missing facts: {', '.join(missing)}",
            )
        width = facts["width"]
        height = facts["height"]
        try:
            area = width * height
        except Exception as exc:  # pragma: no cover - defensive
            return CapabilityResult(
                capability_name=self.name,
                output={},
                success=False,
                error=str(exc),
            )
        return CapabilityResult(
            capability_name=self.name,
            output={"area": area},
            success=True,
        )
