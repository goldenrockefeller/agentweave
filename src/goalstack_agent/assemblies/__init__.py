from goalstack_agent.assemblies.base import Assembly
from goalstack_agent.assemblies.synthetic import (
    fake_direct_assembly,
    synthetic_goalstack_placeholder_assembly,
)

ASSEMBLIES = {
    "fake_direct": fake_direct_assembly,
    "synthetic_goalstack_placeholder": synthetic_goalstack_placeholder_assembly,
}


def get_assembly(name: str) -> Assembly:
    try:
        factory = ASSEMBLIES[name]
    except KeyError as exc:
        raise KeyError(f"Unknown assembly: {name}") from exc
    return factory()

