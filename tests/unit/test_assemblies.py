from goalstack_agent.assemblies.synthetic import fake_direct_assembly


def test_fake_direct_assembly_constructs_successfully() -> None:
    assembly = fake_direct_assembly()

    assert assembly.name == "fake_direct"
    assert assembly.agent_core.run(query="Say hello.") == "hello"
