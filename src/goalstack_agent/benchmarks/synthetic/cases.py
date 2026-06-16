SYNTHETIC_SMOKE_CASES = [
    {
        "id": "echo_001",
        "query": "Say hello.",
        "expected": "hello",
    },
    {
        "id": "math_001",
        "query": "What is 2 + 2?",
        "expected": "4",
    },
    {
        "id": "tool_schema_001",
        "query": "What tools are available?",
        "expected_contains": "calculate_area",
    },
]
