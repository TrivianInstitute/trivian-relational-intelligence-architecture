"""Verify that the four executable TRIA components share one environment."""

from __future__ import annotations

from importlib import import_module


COMPONENTS = {
    "Syzygy Rosetta": "core.reflex",
    "Coheronmetry": "coheronmetry",
    "Orthogonal Signal": "orthogonal_signal",
    "Trivian Resonance Lattice": "trivian_resonance_lattice",
}


def main() -> int:
    failures: list[tuple[str, str]] = []

    for component, module_name in COMPONENTS.items():
        try:
            import_module(module_name)
        except Exception as exc:  # Report the import boundary exactly as encountered.
            failures.append((component, f"{type(exc).__name__}: {exc}"))
            print(f"[FAIL] {component}: {failures[-1][1]}")
        else:
            print(f"[ OK ] {component}: {module_name}")

    if failures:
        print(f"\nTRIA installation incomplete: {len(failures)}/4 components failed.")
        return 1

    print("\nTRIA installation verified: 4/4 components import successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
