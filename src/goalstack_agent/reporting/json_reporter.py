import json
from pathlib import Path
from typing import Any

from goalstack_agent.experiments.result import ExperimentReport


class JsonReporter:
    def __init__(self, output_dir: str = "data/reports"):
        self.output_dir = Path(output_dir)

    def write(
        self,
        *,
        experiment_result: dict[str, Any],
        benchmark_name: str,
        assembly_name: str,
    ) -> ExperimentReport:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        path = self.output_dir / f"{benchmark_name}__{assembly_name}.json"
        payload = {
            "benchmark_name": benchmark_name,
            "assembly_name": assembly_name,
            "num_cases": experiment_result["num_cases"],
            "num_passed": experiment_result["num_passed"],
            "num_failed": experiment_result["num_failed"],
            "results": experiment_result["results"],
        }
        path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        summary = (
            f"{benchmark_name} vs {assembly_name}: "
            f"{payload['num_passed']}/{payload['num_cases']} passed"
        )
        return ExperimentReport(summary=summary, path=str(path), raw=payload)
