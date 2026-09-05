"""Cross-repository Rosetta 2.0 consistency and adversarial verification."""

from __future__ import annotations

import random
import sys
from datetime import datetime, timezone
from pathlib import Path


import argparse
import json
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--workspace", type=Path, required=True)
args = parser.parse_args()
ROOT = args.workspace.resolve()
pins = json.loads((Path(__file__).parent / "components.lock.json").read_text())
for name, expected_sha in pins.items():
    directory = ROOT / name
    actual_sha = subprocess.check_output(
        ["git", "-C", str(directory), "rev-parse", "HEAD"], text=True
    ).strip()
    dirty = subprocess.check_output(
        ["git", "-C", str(directory), "status", "--porcelain", "--untracked-files=normal"], text=True
    ).strip()
    if actual_sha != expected_sha or dirty:
        raise SystemExit(f"{name}: expected clean checkout at {expected_sha}; got {actual_sha}, dirty={bool(dirty)}")
if not __debug__:
    raise SystemExit("Run without -O: assertions are required for verification.")

for path in (
    ROOT / "Syzygy-rosetta",
    ROOT / "Coheronmetry",
    ROOT / "Orthogonal-signal",
    ROOT / "Trivian-resonance-lattice",
    ROOT / "tria-diachronic-sovereignty" / "11-reference-implementation",
):
    sys.path.insert(0, str(path))

from core.field_constants import relational_condition  # noqa: E402
from coheronmetry.relational_state.state import AgentID  # noqa: E402
from coheronmetry.vectors.coherence_vector import CoherenceVector  # noqa: E402
from measurement.field_constants import FieldConstantSnapshot, validate_snapshot  # noqa: E402
from orthogonal_signal.field_constants.novelty_taxonomy import NoveltySignal, NoveltyType  # noqa: E402
from trivian_resonance_lattice.core.field_core import evaluate_coherence  # noqa: E402


def verify() -> dict[str, int]:
    rng = random.Random(20260905)
    checked = 0

    # Legacy equal-weight counterexample: 1, 0, 1, 1 averaged to 0.75,
    # despite collapse of a constitutive dependency.
    assert relational_condition(1.0, 0.0, 1.0) == 0.0
    collapsed = CoherenceVector(
        AgentID("counterexample"), datetime.now(timezone.utc), 1.0, 0.0, 1.0, 1.0
    )
    assert collapsed.relational_condition == 0.0
    assert collapsed.qualified_emergence == 0.0

    for _ in range(10_000):
        r, b, n, emergence = (rng.random() for _ in range(4))
        expected = r * b * n
        rosetta = relational_condition(r, b, n)
        vector = CoherenceVector(
            AgentID("random"), datetime.now(timezone.utc), r, b, emergence, n
        )

        assert abs(rosetta - expected) < 1e-12
        assert abs(vector.relational_condition - expected) < 1e-12
        assert rosetta <= min(r, b, n)
        assert vector.qualified_emergence <= vector.relational_condition

        signal = NoveltySignal(
            NoveltyType.ORTHOGONAL,
            orthogonality_score=1.0,
            coherence_score=1.0,
            relational_condition_score=rosetta,
        )
        assert abs(signal.field_weight - rosetta) < 1e-12

        validate_snapshot(
            FieldConstantSnapshot(r, b, n, emergence, expected, expected * emergence)
        )
        checked += 1

    lexical = evaluate_coherence(
        "mutual co-create together here now",
        "emerge discover without domination",
    )
    per = lexical["per_invariant"]
    assert lexical["relational_condition"] == round(
        per["reciprocity"] * per["embodiment"] * per["non_domination"], 4
    )
    assert lexical["qualified_emergence"] <= lexical["relational_condition"]

    return {"randomized_vectors_checked": checked, "legacy_counterexamples_checked": 1}


if __name__ == "__main__":
    print(json.dumps({"seed": 20260905, "components": pins, "results": verify()}, indent=2))
