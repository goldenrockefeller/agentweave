from dataclasses import dataclass
from typing import Any

from goalstack_agent.model_clients.base import ModelClient


@dataclass
class DirectAgentCore:
    model: ModelClient
    system_prompt: str = "Answer the task directly."

    def run(
        self,
        *,
        query: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Any:
        if messages is None:
            if query is None:
                raise ValueError("DirectAgentCore requires query or messages.")
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": query},
            ]
        response = self.model.invoke(messages=messages)
        return response.get("content", response)
