from goalstack_agent.agent_core.direct import DirectAgentCore
from goalstack_agent.agent_core.goalstack import GoalStackAgentCore
from goalstack_agent.assemblies.base import Assembly
from goalstack_agent.capabilities.synthetic.calculate_area.capability import (
    CalculateAreaCapability,
)
from goalstack_agent.capabilities.synthetic.get_table_height.capability import (
    GetTableHeightCapability,
)
from goalstack_agent.capabilities.synthetic.get_table_width.capability import (
    GetTableWidthCapability,
)
from goalstack_agent.capability_selection.static import StaticCapabilitySelector
from goalstack_agent.fact_management.in_memory import InMemoryFactManager
from goalstack_agent.model_clients.fake import FakeModelClient
from goalstack_agent.response_composition.direct import DirectResponseComposer


def fake_direct_assembly() -> Assembly:
    model = FakeModelClient(behavior="synthetic_smoke")
    agent_core = DirectAgentCore(model=model)
    return Assembly(name="fake_direct", agent_core=agent_core, metadata={"kind": "synthetic"})


def synthetic_goalstack_placeholder_assembly() -> Assembly:
    agent_core = GoalStackAgentCore(
        capabilities=[
            CalculateAreaCapability(),
            GetTableWidthCapability(),
            GetTableHeightCapability(),
        ],
        capability_selector=StaticCapabilitySelector(),
        fact_manager=InMemoryFactManager(initial_facts={"table_id": "T1"}),
        response_composer=DirectResponseComposer(),
    )
    return Assembly(
        name="synthetic_goalstack_placeholder",
        agent_core=agent_core,
        metadata={"kind": "goalstack_placeholder"},
    )
