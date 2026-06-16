from typing import Any

from goalstack_agent.capabilities.base import FactRequirement


class InMemoryFactManager:
    def __init__(self, initial_facts: dict[str, Any] | None = None):
        self._facts = dict(initial_facts or {})

    def add(self, facts: dict[str, Any]) -> None:
        self._facts.update(facts)

    def remove(self, keys: list[str]) -> None:
        for key in keys:
            self._facts.pop(key, None)

    def get(
        self,
        requirements: list[FactRequirement],
        *,
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        return {
            requirement.name: self._facts[requirement.name]
            for requirement in requirements
            if requirement.name in self._facts
        }

