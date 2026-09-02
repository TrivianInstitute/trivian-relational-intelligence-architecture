# Start Here: Install and Verify TRIA

This guide gives researchers and developers a reproducible way to install the four executable TRIA components in one Python environment and verify that they can be imported together.

## What this proves

Completing this guide verifies that:

- each component installs as a Python package;
- the current public interfaces can be imported together;
- each repository's automated test suite can run locally; and
- your environment is ready for component-level experimentation.

It does **not** establish that TRIA's theoretical claims have been empirically validated, or that the four components already form a production-ready end-to-end runtime. Independent falsification, cross-component behavioral tests, and live-model integrations remain active research and engineering work.

## Components

| Layer | Repository | Current role |
|---|---|---|
| 1 | [Syzygy Rosetta](https://github.com/TrivianInstitute/Syzygy-rosetta) | Interaction-boundary governance and invariants |
| 2 | [Coheronmetry](https://github.com/TrivianInstitute/Coheronmetry) | Relational state, drift, repair, and sovereignty measurement |
| 3 | [Orthogonal Signal](https://github.com/TrivianInstitute/Orthogonal-signal) | Novelty, constraint-origin, and anti-convergence primitives |
| 4 | [Trivian Resonance Lattice](https://github.com/TrivianInstitute/Trivian-resonance-lattice) | Network-scale propagation, entrainment, repair, and dissolution |

The [Trivian AI Resonance Key](https://github.com/TrivianInstitute/Trivian-ai-resonance-key) is the orientation layer. Read it first when you need the conceptual and machine-readable framing, but it is not installed as a Python package.

## Requirements

- Git
- Python 3.10 or newer
- A terminal or command prompt

The repositories are currently tested on Python 3.10 and 3.12.

## 1. Create a workspace

```bash
mkdir tria-workspace
cd tria-workspace

git clone https://github.com/TrivianInstitute/trivian-relational-intelligence-architecture.git
git clone https://github.com/TrivianInstitute/Syzygy-rosetta.git
git clone https://github.com/TrivianInstitute/Coheronmetry.git
git clone https://github.com/TrivianInstitute/Orthogonal-signal.git
git clone https://github.com/TrivianInstitute/Trivian-resonance-lattice.git
```

## 2. Create and activate an isolated environment

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Your terminal should now show `(.venv)` at the beginning of the prompt.

## 3. Install the four components

From the `tria-workspace` directory:

```bash
python -m pip install --upgrade pip
python -m pip install \
  -e ./Syzygy-rosetta \
  -e ./Coheronmetry \
  -e ./Orthogonal-signal \
  -e ./Trivian-resonance-lattice
```

The `-e` flag creates an editable installation. If you modify a cloned repository, Python uses that working copy without requiring a new installation.

## 4. Verify the shared environment

```bash
python trivian-relational-intelligence-architecture/scripts/verify_installation.py
```

A successful result ends with:

```text
TRIA installation verified: 4/4 components import successfully.
```

## 5. Run every component test suite

Install the development dependencies:

```bash
python -m pip install \
  -e './Syzygy-rosetta[dev]' \
  -e './Coheronmetry[dev]' \
  -e './Orthogonal-signal[dev]' \
  -e './Trivian-resonance-lattice[dev]'
```

Then run:

```bash
(cd Syzygy-rosetta && python -m pytest -q)
(cd Coheronmetry && python -m pytest -q)
(cd Orthogonal-signal && python -m pytest -q)
(cd Trivian-resonance-lattice && python -m pytest -q)
```

At the current baseline, the repositories contain 5, 34, 150, and 68 tests respectively. GitHub Actions also runs these suites whenever their repositories change.

## 6. Run the examples

```bash
python Syzygy-rosetta/examples/basic_usage.py
python Coheronmetry/examples/two_agent_coherence.py
python Coheronmetry/examples/syzygy_ensemble.py
python Trivian-resonance-lattice/examples/demo.py
```

The Resonance Lattice demo is interactive. Use `Ctrl+C` to leave it.

## Choose an entry point

- **Understand the full research architecture:** continue with the [TRIA README](README.md).
- **Orient a human or machine reader:** begin with the [Resonance Key](https://github.com/TrivianInstitute/Trivian-ai-resonance-key).
- **Instrument relational state:** begin with Coheronmetry.
- **Study difference and anti-convergence:** begin with Orthogonal Signal.
- **Explore network-scale coordination:** begin with the Resonance Lattice.
- **Evaluate interaction-boundary governance:** begin with Syzygy Rosetta.

## Current maturity

TRIA is an experimental research architecture. Its component implementations are installable and tested, but the present test counts demonstrate software behavior against their specifications—not empirical proof that the proposed relational variables measure real-world human–AI dynamics.

The next engineering milestone is a canonical end-to-end integration harness linking all four executable layers around a shared interaction trace.

## Licensing and commercial use

Review the license file in each component repository before redistribution, deployment, or adaptation. Repository summaries are not substitutes for the governing license text.

For commercial licensing inquiries, contact [connect@trivianinstitute.org](mailto:connect@trivianinstitute.org).

## Help, research, and contributions

Questions, reproducibility reports, falsification attempts, and implementation findings may be submitted through the relevant repository's GitHub Issues page or sent to [connect@trivianinstitute.org](mailto:connect@trivianinstitute.org).

When reporting a problem, include your operating system, Python version, installation command, complete error message, and the repository commit you tested.
