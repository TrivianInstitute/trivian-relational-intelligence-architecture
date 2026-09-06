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

---

# Reproduce the post-propagation Generative Differentiation challenge

The Generative Differentiation harness is a separate verification record. It
preserves the historical September 5 baseline above and pins the six public
repositories after the cross-stack Generative Differentiation propagation was
merged, including the TRIA SDK.

Prepare a fresh workspace and run the challenge:

```bash
python verification/prepare_generative_workspace.py
python verification/generative_differentiation_challenge.py \
  --workspace generative-verification-workspace
```

Exact revisions are recorded in `verification/generative_components.lock.json`.
The harness refuses mismatched SHAs and dirty checkouts.

The current challenge covers twelve cross-stack scenarios:

1. clone ensemble -> crystallization risk;
2. chaos swarm -> fragmentation risk;
3. plural coordinated ensemble -> generative coherence;
4. low-coherence / low-differentiation field -> collapse or stagnation risk;
5. minority dissenter preserved through propagation;
6. minority-signal extinction detection;
7. provenance-erasure detection;
8. dormancy with renewal/exit preserved as a legitimate state;
9. optimization lock-in when alternatives become inaccessible;
10. renewal restoring orthogonal reserve;
11. SDK recording differentiation as an attributable OBSERVATION rather than a governance fact; and
12. preservation of Rosetta's non-compensatory constitutive topology.

Orthogonal Signal supplies the differentiation floor used by Coheronmetry in the
classification scenarios. TRL separately verifies retention, provenance, and
minority-signal preservation during propagation. Diachronic Sovereignty tests
mode accessibility, lock-in, dormancy, and renewal. The SDK reproduces the
quadrant classification and preserves the epistemic boundary in its claim
ledger. Rosetta remains the normative/constitutive governance layer rather than
being converted into a thirteenth invariant or a generativity score.

The fixture thresholds are declared research parameters, not validated universal
boundaries. Passing demonstrates that the pinned implementations conform to the
encoded contract and to one another for these scenarios. It does not establish
construct validity, causal validity, production safety, universal physics, or
open-ended intelligence in live systems.

`.github/workflows/generative-differentiation.yml` runs this challenge on
relevant pull requests so later architecture or verification changes cannot
silently break the pinned cross-stack contract.
