from goalstack_agent.benchmarks.base import Benchmark  # noqa: F401
from goalstack_agent.benchmarks.bfcl.benchmark_stub import BFCLStubBenchmark
from goalstack_agent.benchmarks.synthetic.benchmark import SyntheticSmokeBenchmark
from goalstack_agent.benchmarks.tau_bench.benchmark_stub import TauBenchStubBenchmark

BENCHMARKS = {
    "synthetic_smoke": SyntheticSmokeBenchmark,
    "tau_airline_stub": lambda: TauBenchStubBenchmark(domain="airline"),
    "tau_retail_stub": lambda: TauBenchStubBenchmark(domain="retail"),
    "bfcl_stub": BFCLStubBenchmark,
}


def get_benchmark(name: str):
    try:
        factory = BENCHMARKS[name]
    except KeyError as exc:
        raise KeyError(f"Unknown benchmark: {name}") from exc
    return factory()

