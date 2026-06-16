from dataclasses import dataclass
from typing import Any

from goalstack_agent.benchmarks.synthetic.cases import SYNTHETIC_SMOKE_CASES
from goalstack_agent.errors import BenchmarkError


@dataclass
class SyntheticSmokeBenchmark:
    name: str = "synthetic_smoke"

    def list_cases(self) -> list[str]:
        return [case["id"] for case in SYNTHETIC_SMOKE_CASES]

    def load_case(self, case_id: str) -> dict[str, Any]:
        for case in SYNTHETIC_SMOKE_CASES:
            if case["id"] == case_id:
                return dict(case)
        raise BenchmarkError(f"Unknown synthetic smoke case: {case_id}")

    def eval(self, case: dict[str, Any], prediction: Any) -> dict[str, Any]:
        text = prediction if isinstance(prediction, str) else str(prediction)
        if "expected" in case:
            passed = text == case["expected"]
        elif "expected_contains" in case:
            passed = case["expected_contains"] in text
        else:
            passed = False
        return {
            "case_id": case.get("id"),
            "passed": passed,
            "prediction": prediction,
            "expected": case.get("expected"),
            "expected_contains": case.get("expected_contains"),
        }

