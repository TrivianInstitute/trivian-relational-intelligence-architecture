"""Experimental reference model for TRIA Generative Differentiation.

This module implements a transparent, non-validated classification surface for
research and falsification. It does not claim universal thresholds or a safety
score. Callers must supply explicitly calibrated thresholds for their context.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class GenerativeCondition(str, Enum):
    GENERATIVE_COHERENCE = "generative_coherence"
    CRYSTALLIZATION_RISK = "crystallization_risk"
    FRAGMENTATION_RISK = "fragmentation_risk"
    COLLAPSE_OR_STAGNATION_RISK = "collapse_or_stagnation_risk"


@dataclass(frozen=True)
class DifferentiationState:
    constraint_diversity: float
    representational_diversity: float
    attractor_concentration: float
    orthogonal_reserve: float
    novelty_velocity: float
    temporal_mode_diversity: float
    provenance: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for name in (
            "constraint_diversity",
            "representational_diversity",
            "attractor_concentration",
            "orthogonal_reserve",
            "novelty_velocity",
            "temporal_mode_diversity",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be in [0.0, 1.0]")

    def dimensions(self) -> dict[str, float]:
        return {
            "constraint_diversity": self.constraint_diversity,
            "representational_diversity": self.representational_diversity,
            "attractor_concentration": self.attractor_concentration,
            "orthogonal_reserve": self.orthogonal_reserve,
            "novelty_velocity": self.novelty_velocity,
            "temporal_mode_diversity": self.temporal_mode_diversity,
        }


@dataclass(frozen=True)
class GenerativeDifferentiationThresholds:
    coherence_floor: float
    differentiation_floor: float

    def __post_init__(self) -> None:
        for name in ("coherence_floor", "differentiation_floor"):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be in [0.0, 1.0]")


def differentiation_floor(state: DifferentiationState) -> float:
    """Return the weakest preserved differentiation dimension.

    Attractor concentration is inverted because greater concentration implies
    less preserved differentiation. A minimum operator is used deliberately so
    strong values elsewhere cannot hide collapse of one declared dimension.
    This is a research choice, not an empirically validated universal operator.
    """

    values = (
        state.constraint_diversity,
        state.representational_diversity,
        1.0 - state.attractor_concentration,
        state.orthogonal_reserve,
        state.novelty_velocity,
        state.temporal_mode_diversity,
    )
    return min(values)


def classify_generative_condition(
    *,
    coherence: float,
    state: DifferentiationState,
    thresholds: GenerativeDifferentiationThresholds,
) -> GenerativeCondition:
    """Classify the coherence/differentiation quadrant.

    Thresholds are caller-supplied so deployment-specific calibration is never
    mistaken for a universal scientific boundary.
    """

    if not 0.0 <= coherence <= 1.0:
        raise ValueError("coherence must be in [0.0, 1.0]")

    coherent = coherence >= thresholds.coherence_floor
    differentiated = differentiation_floor(state) >= thresholds.differentiation_floor

    if coherent and differentiated:
        return GenerativeCondition.GENERATIVE_COHERENCE
    if coherent and not differentiated:
        return GenerativeCondition.CRYSTALLIZATION_RISK
    if not coherent and differentiated:
        return GenerativeCondition.FRAGMENTATION_RISK
    return GenerativeCondition.COLLAPSE_OR_STAGNATION_RISK
