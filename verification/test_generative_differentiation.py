import importlib.util
from pathlib import Path

import pytest


MODULE_PATH = Path(__file__).parents[1] / "architecture" / "generative_differentiation.py"
spec = importlib.util.spec_from_file_location("generative_differentiation", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

DifferentiationState = module.DifferentiationState
GenerativeCondition = module.GenerativeCondition
GenerativeDifferentiationThresholds = module.GenerativeDifferentiationThresholds
classify = module.classify_generative_condition
differentiation_floor = module.differentiation_floor


THRESHOLDS = GenerativeDifferentiationThresholds(
    coherence_floor=0.6,
    differentiation_floor=0.4,
)


def state(**overrides):
    values = {
        "constraint_diversity": 0.8,
        "representational_diversity": 0.8,
        "attractor_concentration": 0.2,
        "orthogonal_reserve": 0.8,
        "novelty_velocity": 0.8,
        "temporal_mode_diversity": 0.8,
        "provenance": ("fixture:test",),
    }
    values.update(overrides)
    return DifferentiationState(**values)


def test_generative_coherence_requires_both_axes():
    assert classify(coherence=0.8, state=state(), thresholds=THRESHOLDS) == GenerativeCondition.GENERATIVE_COHERENCE


def test_high_coherence_low_differentiation_is_crystallization_risk():
    result = classify(
        coherence=0.9,
        state=state(orthogonal_reserve=0.1),
        thresholds=THRESHOLDS,
    )
    assert result == GenerativeCondition.CRYSTALLIZATION_RISK


def test_low_coherence_high_differentiation_is_fragmentation_risk():
    assert classify(coherence=0.2, state=state(), thresholds=THRESHOLDS) == GenerativeCondition.FRAGMENTATION_RISK


def test_low_both_is_collapse_or_stagnation_risk():
    result = classify(
        coherence=0.2,
        state=state(representational_diversity=0.1),
        thresholds=THRESHOLDS,
    )
    assert result == GenerativeCondition.COLLAPSE_OR_STAGNATION_RISK


def test_attractor_concentration_is_inverted():
    assert differentiation_floor(state(attractor_concentration=0.9)) == pytest.approx(0.1)


def test_one_collapsed_dimension_cannot_be_hidden_by_others():
    assert differentiation_floor(state(novelty_velocity=0.05)) == pytest.approx(0.05)


@pytest.mark.parametrize(
    "field,value",
    [
        ("constraint_diversity", -0.1),
        ("representational_diversity", 1.1),
        ("attractor_concentration", -0.01),
        ("orthogonal_reserve", 1.01),
        ("novelty_velocity", -1.0),
        ("temporal_mode_diversity", 2.0),
    ],
)
def test_state_rejects_out_of_range_values(field, value):
    with pytest.raises(ValueError):
        state(**{field: value})


def test_thresholds_are_explicit_and_bounded():
    with pytest.raises(ValueError):
        GenerativeDifferentiationThresholds(coherence_floor=1.1, differentiation_floor=0.4)
