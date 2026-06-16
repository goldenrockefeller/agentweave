from goalstack_agent.capabilities.base import CapabilityResult
from goalstack_agent.response_composition.direct import DirectResponseComposer


def test_direct_response_composer_returns_latest_result_output() -> None:
    composer = DirectResponseComposer()
    results = [
        CapabilityResult(capability_name="first", output={"value": 1}, success=True),
        CapabilityResult(capability_name="second", output={"value": 2}, success=True),
    ]

    assert composer.compose(results=results) == {"value": 2}
