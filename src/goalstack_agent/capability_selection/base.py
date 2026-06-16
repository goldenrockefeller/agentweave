from typing import Any, Protocol

from goalstack_agent.capabilities.base import Capability


class CapabilitySelector(Protocol):
    def select(
        self,
        *,
        capabilities: list[Capability],
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> list[Capability]:
        ...
