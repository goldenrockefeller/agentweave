from dataclasses import dataclass
from typing import Any


@dataclass
class ExperimentReport:
    summary: str
    path: str
    raw: dict[str, Any]
