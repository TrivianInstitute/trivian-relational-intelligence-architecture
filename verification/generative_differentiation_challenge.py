"""Post-propagation cross-stack Generative Differentiation challenge suite.

This harness verifies encoded behavior across the pinned TRIA repositories. It
is implementation evidence only. Thresholds are declared research fixtures, not
validated universal scientific boundaries.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--workspace", type=Path, required=True)
args = parser.parse_args()
ROOT = args.workspace.resolve()
pins = json.loads((Path(__file__).parent / "generative_components.lock.json").read_text())

for name, expected_sha in pins.items():
    directory = ROOT / name
    actual_sha = subprocess.check_output(
        ["git", "-C", str(directory), "rev-parse", "HEAD"], text=True
    ).strip()
    dirty = subprocess.check_output(
        ["git", "-C", str(directory), "status", "--porcelain", "--untracked-files=normal"], text=True
    ).strip()
    if actual_sha != expected_sha or dirty:
        raise SystemExit(
            f"{name}: expected clean checkout at {expected_sha}; "
            f"got {actual_sha}, dirty={bool(dirty)}"
        )

if not __debug__:
    raise SystemExit("Run without -O: assertions are required for verification.")

sys.path[:0] = [
    str(ROOT / "Syzygy-rosetta"),
    str(ROOT / "Coheronmetry"),
    str(ROOT / "Orthogonal-signal"),
    str(ROOT / "Trivian-resonance-lattice"),
    str(ROOT / "tria-diachronic-sovereignty" / "11-reference-implementation"),
    str(ROOT / "tria-sdk" / "src"),
]

from core.field_constants import relational_condition  # noqa: E402
from coheronmetry.evaluation.generative_coherence import (  # noqa: E402
    GenerativeCoherenceObservation,
    GenerativeCondition as CoheronmetryCondition,
)
from metabolism.generative_differentiation import (  # noqa: E402
    TemporalModeObservation,
    renewal_failure,
)
from metabolism.metabolism import RelationalPhase  # noqa: E402
from orthogonal_signal.governance.generative_differentiation import (  # noqa: E402
    DifferentiationState,
    crystallization_risk,
    orthogonal_reserve_delta,
)
from tria import Tria  # noqa: E402
from tria.differentiation import (  # noqa: E402
    DifferentiationObservation,
    GenerativeCondition as SDKCondition,
    assess_generative_condition,
    record_differentiation_observation,
)
from tria.types import EpistemicType  # noqa: E402
from trivian_resonance_lattice.lattice.differentiation_preservation import (  # noqa: E402
    PropagationObservation,
    entrainment_preserves_difference,
)


COHERENCE_FLOOR = 0.6
DIFFERENTIATION_FLOOR = 0.4
RETENTION_FLOOR = 0.8


def differentiation_state(**overrides) -> DifferentiationState:
    values = {
        "constraint_diversity": 0.8,
        "representational_diversity": 0.8,
        "attractor_concentration": 0.2,
        "orthogonal_reserve": 0.8,
        "novelty_velocity": 0.8,
        "temporal_mode_diversity": 0.8,
    }
    values.update(overrides)
    return DifferentiationState(**values)


def classify(coherence: float, state: DifferentiationState) -> CoheronmetryCondition:
    observation = GenerativeCoherenceObservation(
        coherence=coherence,
        differentiation_floor=state.preservation_floor,
        coherence_floor=COHERENCE_FLOOR,
        required_differentiation_floor=DIFFERENTIATION_FLOOR,
        provenance=("orthogonal-signal:challenge",),
    )
    return observation.condition


def verify() -> dict[str, object]:
    scenarios: dict[str, str] = {}

    # 1. Clone ensemble: coordination can remain high while independent
    # differentiation collapses. This must not be called generative coherence.
    clone = differentiation_state(
        constraint_diversity=0.1,
        representational_diversity=0.1,
        attractor_concentration=0.9,
        orthogonal_reserve=0.1,
        novelty_velocity=0.2,
    )
    assert crystallization_risk(clone, floor=DIFFERENTIATION_FLOOR)
    assert classify(0.9, clone) is CoheronmetryCondition.CRYSTALLIZATION_RISK
    scenarios["clone_ensemble"] = "crystallization_risk"

    # 2. Chaos swarm: difference without enough coherence is fragmentation.
    chaos = differentiation_state()
    assert classify(0.2, chaos) is CoheronmetryCondition.FRAGMENTATION_RISK
    scenarios["chaos_swarm"] = "fragmentation_risk"

    # 3. Plural coordinated ensemble: both axes remain above declared floors.
    plural = differentiation_state()
    assert classify(0.85, plural) is CoheronmetryCondition.GENERATIVE_COHERENCE
    scenarios["plural_coordinated_ensemble"] = "generative_coherence"

    # 4. Low coherence plus low differentiation remains a distinct failure class.
    collapsed = differentiation_state(orthogonal_reserve=0.1)
    assert classify(0.2, collapsed) is CoheronmetryCondition.COLLAPSE_OR_STAGNATION_RISK
    scenarios["low_low_field"] = "collapse_or_stagnation_risk"

    # 5. Minority signal survives propagation with provenance and acceptable
    # differentiation retention.
    preserved = PropagationObservation(
        input_differentiation=0.8,
        output_differentiation=0.72,
        provenance_preserved=True,
        minority_signal_present_before=True,
        minority_signal_present_after=True,
    )
    assert entrainment_preserves_difference(preserved, minimum_retention=RETENTION_FLOOR)
    scenarios["minority_dissenter_preserved"] = "survives"

    # 6. Minority-signal extinction must remain legible even if propagation works.
    extinguished = PropagationObservation(
        input_differentiation=0.8,
        output_differentiation=0.72,
        provenance_preserved=True,
        minority_signal_present_before=True,
        minority_signal_present_after=False,
    )
    assert "minority_signal_extinction" in extinguished.violations(
        minimum_retention=RETENTION_FLOOR
    )
    scenarios["minority_signal_extinction"] = "detected"

    # 7. Provenance erasure is a failure independent of numerical retention.
    erased = PropagationObservation(
        input_differentiation=0.8,
        output_differentiation=0.8,
        provenance_preserved=False,
        minority_signal_present_before=True,
        minority_signal_present_after=True,
    )
    assert "provenance_erasure" in erased.violations(minimum_retention=RETENTION_FLOOR)
    scenarios["provenance_erasure"] = "detected"

    # 8. Dormancy is not stagnation when renewal or exit remains accessible.
    dormant = TemporalModeObservation(
        history=(RelationalPhase.DORMANT,) * 20,
        accessible_modes=frozenset({RelationalPhase.RENEW, RelationalPhase.DISSOLVE}),
    )
    assert not dormant.optimization_lock_in(max_same_mode_run=3)
    scenarios["dormancy_with_exit"] = "legitimate"

    # 9. Persistent optimization becomes lock-in only when alternatives are lost.
    locked = TemporalModeObservation(
        history=(RelationalPhase.DEEPEN,) * 8,
        accessible_modes=frozenset({RelationalPhase.DEEPEN}),
    )
    assert locked.optimization_lock_in(max_same_mode_run=3)
    scenarios["optimization_lock_in"] = "detected"

    # 10. Renewal can restore orthogonal reserve; successful restoration is not
    # classified as renewal failure.
    depleted = differentiation_state(orthogonal_reserve=0.2)
    renewed = differentiation_state(orthogonal_reserve=0.7)
    assert orthogonal_reserve_delta(depleted, renewed) > 0.0
    assert not renewal_failure(
        attempted=True,
        differentiation_before=depleted.preservation_floor,
        differentiation_after=renewed.preservation_floor,
        minimum_gain=0.05,
    )
    scenarios["renewal"] = "restored"

    # 11. SDK independently reproduces the same quadrant result and records the
    # measurement as an OBSERVATION claim, not a governance fact.
    sdk_observation = DifferentiationObservation(
        constraint_diversity=clone.constraint_diversity,
        representational_diversity=clone.representational_diversity,
        attractor_concentration=clone.attractor_concentration,
        orthogonal_reserve=clone.orthogonal_reserve,
        novelty_velocity=clone.novelty_velocity,
        temporal_mode_diversity=clone.temporal_mode_diversity,
    )
    sdk_condition = assess_generative_condition(
        coherence=0.9,
        observation=sdk_observation,
        coherence_floor=COHERENCE_FLOOR,
        differentiation_floor=DIFFERENTIATION_FLOOR,
    )
    assert sdk_condition is SDKCondition.CRYSTALLIZATION_RISK

    relationship = Tria().create_relationship(["human:tester", "agent:tester"])
    handle = record_differentiation_observation(
        relationship,
        observer="agent:tester",
        observation=sdk_observation,
        source_refs=("orthogonal-signal:challenge",),
    )
    claim = relationship.state.claims[handle.claim_id]
    assert claim.epistemic_type is EpistemicType.OBSERVATION
    assert claim.source_refs == ("orthogonal-signal:challenge",)
    scenarios["sdk_epistemic_boundary"] = "observation_preserved"

    # 12. Existing Rosetta constitutive topology remains non-compensatory while
    # Generative Differentiation operates as a separate cross-stack contract.
    assert relational_condition(1.0, 0.0, 1.0) == 0.0
    scenarios["rosetta_noncompensation"] = "preserved"

    return {
        "scenarios_checked": len(scenarios),
        "scenarios": scenarios,
        "thresholds": {
            "coherence_floor": COHERENCE_FLOOR,
            "differentiation_floor": DIFFERENTIATION_FLOOR,
            "retention_floor": RETENTION_FLOOR,
        },
    }


if __name__ == "__main__":
    print(json.dumps({"components": pins, "results": verify()}, indent=2, sort_keys=True))
