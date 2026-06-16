from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def test_run_experiment_fake_direct_synthetic_smoke_passes() -> None:
    root = Path(__file__).resolve().parents[2]
    report_path = root / "data" / "reports" / "synthetic_smoke__fake_direct.json"
    if report_path.exists():
        report_path.unlink()

    completed = subprocess.run(
        [
            sys.executable,
            str(root / "scripts" / "run_experiment.py"),
            "--assembly",
            "fake_direct",
            "--benchmark",
            "synthetic_smoke",
        ],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )

    assert "3/3 passed" in completed.stdout
    assert report_path.exists()
    payload = json.loads(report_path.read_text(encoding="utf-8"))
    assert payload["num_passed"] == 3
    assert payload["num_failed"] == 0
