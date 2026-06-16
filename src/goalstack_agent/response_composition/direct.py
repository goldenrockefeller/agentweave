from dataclasses import dataclass

from goalstack_agent.capabilities.base import CapabilityResult


@dataclass
class DirectResponseComposer:
    def compose(
        self,
        *,
        results: list[CapabilityResult],
        query: str | None = None,
        messages: list[dict[str, object]] | None = None,
        metadata: dict[str, object] | None = None,
    ) -> object:
        if not results:
            return ""
        return results[-1].output
