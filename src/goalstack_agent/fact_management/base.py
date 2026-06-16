from typing import Any, Protocol

from goalstack_agent.capabilities.base import FactRequirement


class FactManager(Protocol):
    def add(self, facts: dict[str, Any]) -> None:
        ...

    def remove(self, keys: list[str]) -> None:
        ...

    def get(
        self,
        requirements: list[FactRequirement],
        *,
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        ...
