from goalstack_agent.capabilities.synthetic.calculate_area.capability import (
    CalculateAreaCapability,
)
from goalstack_agent.capabilities.synthetic.get_table_height.capability import (
    GetTableHeightCapability,
)
from goalstack_agent.capabilities.synthetic.get_table_width.capability import (
    GetTableWidthCapability,
)


def test_calculate_area_capability_returns_area() -> None:
    capability = CalculateAreaCapability()

    result = capability.invoke(facts={"width": 4, "height": 7})

    assert result.success is True
    assert result.output == {"area": 28}


def test_get_table_width_capability_returns_width() -> None:
    capability = GetTableWidthCapability()

    result = capability.invoke(facts={"table_id": "T1"})

    assert result.success is True
    assert result.output == {"width": 4}


def test_get_table_height_capability_returns_height() -> None:
    capability = GetTableHeightCapability()

    result = capability.invoke(facts={"table_id": "T1"})

    assert result.success is True
    assert result.output == {"height": 7}
