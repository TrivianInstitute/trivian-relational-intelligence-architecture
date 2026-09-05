# Reproduce the 2026-09-05 cross-stack check

This publishes the previously local harness with the exact five component
revisions used in the final audit. These historical pins intentionally precede
the subsequent invalid-input hardening patch. This is a reproduction baseline,
not a claim that these revisions are the latest or free of defects.

Use Python 3.11 or newer and Git. From the architecture repository root:

```bash
python -m venv .venv
# Activate .venv for your platform.
python -m pip install -r verification/requirements.txt
python verification/prepare_workspace.py
python verification/stack_verification.py --workspace verification-workspace
```

The preparation script creates a NEW workspace and clones only the five public
repositories named in the lock file. It refuses to overwrite an existing path.
The harness refuses mismatched revisions and dirty component checkouts.
It prints the pinned revisions, seed, and successful case counts. Failed
assertions or import errors exit nonzero. Do not run Python with -O.

Coverage: 10,000 deterministic positive unit-interval vectors compare Rosetta
and Coheronmetry RCD, Orthogonal Signal's supplied-RCD weighting, and Diachronic
snapshot arithmetic. One legacy zero-collapse counterexample is checked.
TRL receives one separate lexical-input formula check, NOT 10,000 randomized
end-to-end trials. The SDK is not exercised by this harness.

This does not test live models, consent legitimacy, measurement calibration,
causal topology, all malformed inputs, or complete cross-repository adapters.
Passing is implementation evidence only. Package versions are pinned; OS,
Python patch version and transitive dependencies are not fully locked.

For the five repository suites, run `python -m pytest -q` inside each checkout.
The historical baseline totals 311 repository tests. Invalid-input regressions
belong to the newer Coheronmetry patch, not to these historical pins.
