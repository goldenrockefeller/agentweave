from typing import Any, Protocol

from goalstack_agent.capabilities.base import CapabilityResult


class ResponseComposer(Protocol):
    def compose(
        self,
        *,
        results: list[CapabilityResult],
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Any:
        ...
