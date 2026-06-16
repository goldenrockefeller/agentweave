from dataclasses import dataclass
from typing import Any


@dataclass
class FakeModelClient:
    behavior: str = "synthetic_smoke"

    def invoke(
        self,
        messages: list[dict[str, Any]],
        *,
        tools: list[dict[str, Any]] | None = None,
        response_format: Any | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        if self.behavior == "synthetic_smoke":
            content = self._invoke_synthetic_smoke(messages, tools=tools)
        else:
            content = self._default_response(messages)
        return {"content": content}

    def _default_response(self, messages: list[dict[str, Any]]) -> str:
        return self._join_messages(messages)

    def _invoke_synthetic_smoke(
        self,
        messages: list[dict[str, Any]],
        *,
        tools: list[dict[str, Any]] | None = None,
    ) -> str:
        user_text = self._last_user_text(messages)
        if user_text == "Say hello.":
            return "hello"
        if user_text == "What is 2 + 2?":
            return "4"
        if user_text == "What tools are available?":
            tool_names = self._tool_names(tools)
            if tool_names:
                return ", ".join(tool_names)
            return "calculate_area"
        return self._join_messages(messages)

    def _last_user_text(self, messages: list[dict[str, Any]]) -> str:
        for message in reversed(messages):
            if message.get("role") == "user":
                return str(message.get("content", ""))
        return self._join_messages(messages)

    def _join_messages(self, messages: list[dict[str, Any]]) -> str:
        parts = [str(message.get("content", "")) for message in messages if message.get("content")]
        return " ".join(parts)

    def _tool_names(self, tools: list[dict[str, Any]] | None) -> list[str]:
        if not tools:
            return ["calculate_area", "get_table_width", "get_table_height"]
        names: list[str] = []
        for tool in tools:
            name = tool.get("name") if isinstance(tool, dict) else None
            if name:
                names.append(str(name))
        return names
