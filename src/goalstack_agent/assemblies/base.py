from dataclasses import dataclass
from typing import Any

from goalstack_agent.agent_core.base import AgentCore


@dataclass
class Assembly:
    name: str
    agent_core: AgentCore
    metadata: dict[str, Any] | None = None
