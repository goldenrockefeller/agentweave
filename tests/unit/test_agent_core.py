from goalstack_agent.agent_core.direct import DirectAgentCore
from goalstack_agent.model_clients.fake import FakeModelClient


def test_direct_agent_core_calls_model_and_returns_content() -> None:
    core = DirectAgentCore(model=FakeModelClient(behavior="synthetic_smoke"))

    result = core.run(query="Say hello.")

    assert result == "hello"
