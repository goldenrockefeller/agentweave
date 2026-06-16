from dataclasses import dataclass

from goalstack_agent.capabilities.base import Capability


@dataclass
class StaticCapabilitySelector:
    selected_names: list[str] | None = None

    def select(
        self,
        *,
        capabilities: list[Capability],
        query: str | None = None,
        messages: list[dict[str, object]] | None = None,
        metadata: dict[str, object] | None = None,
    ) -> list[Capability]:
        if self.selected_names is None:
            return capabilities
        return [capability for capability in capabilities if capability.name in self.selected_names]
