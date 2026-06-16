from dataclasses import dataclass
from typing import Any, Protocol


@dataclass
class FactRequirement:
    name: str
    description: str | None = None
    type_hint: str | None = None
    required: bool = True


@dataclass
class CapabilityResult:
    capability_name: str
    output: dict[str, Any]
    success: bool
    error: str | None = None


class Capability(Protocol):
    name: str
    description: str

    def required_facts(
        self,
        *,
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> list[FactRequirement]:
        ...

    def invoke(
        self,
        *,
        facts: dict[str, Any],
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> CapabilityResult:
        ...
