from typing import Any, Protocol


class ModelClient(Protocol):
    def invoke(
        self,
        messages: list[dict[str, Any]],
        *,
        tools: list[dict[str, Any]] | None = None,
        response_format: Any | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        ...
