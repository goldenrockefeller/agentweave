from dataclasses import dataclass
from typing import Any

from goalstack_agent.capabilities.base import Capability
from goalstack_agent.capability_selection.base import CapabilitySelector
from goalstack_agent.fact_management.base import FactManager
from goalstack_agent.response_composition.base import ResponseComposer


@dataclass
class GoalStackAgentCore:
    capabilities: list[Capability]
    capability_selector: CapabilitySelector
    fact_manager: FactManager
    response_composer: ResponseComposer

    def run(
        self,
        *,
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Any:
        raise NotImplementedError(
            "GoalStackAgentCore is planned but not implemented in the first scaffold."
        )
