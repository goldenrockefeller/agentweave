from goalstack_agent.capabilities.base import FactRequirement
from goalstack_agent.fact_management.in_memory import InMemoryFactManager


def test_in_memory_fact_manager_add_remove_get_works() -> None:
    manager = InMemoryFactManager(initial_facts={"table_id": "T1"})
    manager.add({"width": 4, "height": 7})

    facts = manager.get([FactRequirement(name="table_id"), FactRequirement(name="width")])
    assert facts == {"table_id": "T1", "width": 4}

    manager.remove(["width"])
    assert manager.get([FactRequirement(name="width")]) == {}
