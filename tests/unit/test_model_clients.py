from goalstack_agent.model_clients.fake import FakeModelClient


def test_fake_model_client_answers_synthetic_queries() -> None:
    model = FakeModelClient(behavior="synthetic_smoke")

    hello = model.invoke(messages=[{"role": "user", "content": "Say hello."}])
    math = model.invoke(messages=[{"role": "user", "content": "What is 2 + 2?"}])
    tools = model.invoke(messages=[{"role": "user", "content": "What tools are available?"}])

    assert hello["content"] == "hello"
    assert math["content"] == "4"
    assert "calculate_area" in tools["content"]
