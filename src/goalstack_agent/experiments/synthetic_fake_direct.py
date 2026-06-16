from goalstack_agent.assemblies.synthetic import fake_direct_assembly
from goalstack_agent.benchmarks.synthetic.benchmark import SyntheticSmokeBenchmark
from goalstack_agent.experiments.runner import ExperimentRunner
from goalstack_agent.reporting.json_reporter import JsonReporter


def main() -> None:
    assembly = fake_direct_assembly()
    benchmark = SyntheticSmokeBenchmark()
    runner = ExperimentRunner()
    experiment_result = runner.run(assembly=assembly, benchmark=benchmark)
    reporter = JsonReporter()
    report = reporter.write(
        experiment_result=experiment_result,
        benchmark_name=benchmark.name,
        assembly_name=assembly.name,
    )
    print(report.summary)
    print(report.path)


if __name__ == "__main__":
    main()
