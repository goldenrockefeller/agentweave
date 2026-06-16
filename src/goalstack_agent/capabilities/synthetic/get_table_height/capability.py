from dataclasses import dataclass
from typing import Any

from goalstack_agent.capabilities.base import CapabilityResult, FactRequirement


@dataclass
class GetTableHeightCapability:
    name: str = "get_table_height"
    description: str = "Get synthetic table height from table_id."

    def required_facts(
        self,
        *,
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> list[FactRequirement]:
        return [FactRequirement(name="table_id", description="Synthetic table identifier")]

    def invoke(
        self,
        *,
        facts: dict[str, Any],
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> CapabilityResult:
        table_id = facts.get("table_id")
        if table_id is None:
            return CapabilityResult(
                capability_name=self.name,
                output={},
                success=False,
                error="Missing facts: table_id",
            )
        if table_id != "T1":
            return CapabilityResult(
                capability_name=self.name,
                output={},
                success=False,
                error=f"Unsupported table_id: {table_id}",
            )
        return CapabilityResult(
            capability_name=self.name,
            output={"height": 7},
            success=True,
        )
