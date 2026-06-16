from typing import Any, Protocol


class AgentCore(Protocol):
    def run(
        self,
        *,
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Any:
        ...
