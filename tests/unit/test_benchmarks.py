from goalstack_agent.benchmarks.synthetic.benchmark import SyntheticSmokeBenchmark


def test_synthetic_smoke_benchmark_scores_correctly() -> None:
    benchmark = SyntheticSmokeBenchmark()

    hello_case = benchmark.load_case("echo_001")
    math_case = benchmark.load_case("math_001")
    tools_case = benchmark.load_case("tool_schema_001")

    assert benchmark.eval(hello_case, "hello")["passed"] is True
    assert benchmark.eval(math_case, "4")["passed"] is True
    assert benchmark.eval(tools_case, "calculate_area, get_table_width")["passed"] is True
