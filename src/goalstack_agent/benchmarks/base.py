from typing import Any, Protocol


class Benchmark(Protocol):
    name: str

    def list_cases(self) -> list[str]:
        ...

    def load_case(self, case_id: str) -> dict[str, Any]:
        ...

    def eval(self, case: dict[str, Any], prediction: Any) -> dict[str, Any]:
        ...
