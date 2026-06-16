from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from goalstack_agent.assemblies import ASSEMBLIES  # noqa: E402


def main() -> None:
    for name in sorted(ASSEMBLIES):
        print(name)


if __name__ == "__main__":
    main()

