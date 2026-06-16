from dataclasses import dataclass
from typing import Any

from goalstack_agent.assemblies.base import Assembly
from goalstack_agent.benchmarks.base import Benchmark


@dataclass
class ExperimentRunner:
    def run(
        self,
        *,
        assembly: Assembly,
        benchmark: Benchmark,
        case_id: str | None = None,
    ) -> dict[str, Any]:
        case_ids = [case_id] if case_id is not None else benchmark.list_cases()
        results: list[dict[str, Any]] = []
        for current_case_id in case_ids:
            case = benchmark.load_case(current_case_id)
            prediction = assembly.agent_core.run(
                query=case.get("query"),
                messages=case.get("messages"),
                metadata=case.get("metadata"),
            )
            result = benchmark.eval(case, prediction)
            results.append({"case": case, "prediction": prediction, "result": result})
        num_passed = sum(1 for item in results if item["result"].get("passed"))
        num_failed = len(results) - num_passed
        return {
            "benchmark_name": getattr(benchmark, "name", benchmark.__class__.__name__),
            "assembly_name": assembly.name,
            "num_cases": len(results),
            "num_passed": num_passed,
            "num_failed": num_failed,
            "results": results,
        }
