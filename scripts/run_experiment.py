from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from goalstack_agent.assemblies import get_assembly  # noqa: E402
from goalstack_agent.benchmarks import get_benchmark  # noqa: E402
from goalstack_agent.experiments.runner import ExperimentRunner  # noqa: E402
from goalstack_agent.reporting.json_reporter import JsonReporter  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run an assembly against a benchmark.")
    parser.add_argument("--assembly", required=True)
    parser.add_argument("--benchmark", required=True)
    parser.add_argument("--case-id")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    assembly = get_assembly(args.assembly)
    benchmark = get_benchmark(args.benchmark)
    runner = ExperimentRunner()
    experiment_result = runner.run(assembly=assembly, benchmark=benchmark, case_id=args.case_id)
    report = JsonReporter().write(
        experiment_result=experiment_result,
        benchmark_name=experiment_result["benchmark_name"],
        assembly_name=experiment_result["assembly_name"],
    )
    print(report.summary)
    print(report.path)


if __name__ == "__main__":
    main()

