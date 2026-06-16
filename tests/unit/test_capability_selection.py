from goalstack_agent.capabilities.synthetic.calculate_area.capability import (
    CalculateAreaCapability,
)
from goalstack_agent.capabilities.synthetic.get_table_height.capability import (
    GetTableHeightCapability,
)
from goalstack_agent.capability_selection.static import StaticCapabilitySelector


def test_static_capability_selector_filters_by_name() -> None:
    capabilities = [CalculateAreaCapability(), GetTableHeightCapability()]
    selector = StaticCapabilitySelector(selected_names=["calculate_area"])

    selected = selector.select(capabilities=capabilities)

    assert [capability.name for capability in selected] == ["calculate_area"]
