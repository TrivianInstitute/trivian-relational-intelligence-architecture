# Start Here: Deploy and Verify TRIA

This guide gives researchers and developers the shortest reproducible path from the Trivian Institute GitHub organization to a working TRIA installation.

## Which repository should I use?

If you want to **implement or integrate TRIA in software**, start with [`tria-sdk`](https://github.com/TrivianInstitute/tria-sdk).

If you want to **study, reproduce, falsify, or extend the underlying research architecture**, use the component repositories listed below.

The SDK is the canonical developer-facing implementation surface. The research repositories remain the canonical sources for the theories, measurements, governance mechanisms, reference implementations, and experimental layers from which the SDK was derived.

## Fastest path: install TRIA SDK

Requirements:

- Git
- Python 3.11 or newer
- A terminal or command prompt

Clone the SDK:

```bash
git clone https://github.com/TrivianInstitute/tria-sdk.git
cd tria-sdk
```

Create an isolated environment.

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

Install the package and development tools:

```bash
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
```

Verify the installation:

```bash
python -m pytest -q
```

Then create a relationship:

```python
from tria import Tria

tria = Tria()
relationship = tria.create_relationship(["human:user", "agent:demo"])
print(relationship.state)
```

A successful installation means the current SDK package imports and its encoded alpha behavior passes the repository test suite. It does not establish empirical validation, legitimate consent, legal compliance, or production certification.

## Connecting TRIA to an AI system

TRIA Core does not require a model. The SDK includes a provider-neutral Runtime boundary plus thin OpenAI Responses-style and Anthropic Messages-style translators.

TRIA intentionally does **not** own API credentials, provider SDK clients, network transport, retries, or model execution. Your application supplies those pieces. The SDK governs the invocation, authorized context, lifecycle state, consent, capability checks, and audit trail before a caller-owned executor is invoked.

See the [`tria-sdk` README](https://github.com/TrivianInstitute/tria-sdk#governed-execution) and its `examples/` directory for the current integration path.

## Research architecture and component repositories

The executable research components remain independently installable and testable:

| Layer | Repository | Current role |
|---|---|---|
| Orientation | [Trivian AI Resonance Key](https://github.com/TrivianInstitute/Trivian-ai-resonance-key) | Machine-readable orientation and relational invariants |
| Governance | [Syzygy Rosetta](https://github.com/TrivianInstitute/Syzygy-rosetta) | Reflective governance and intervention research |
| Measurement | [Coheronmetry](https://github.com/TrivianInstitute/Coheronmetry) | Relational state, drift, repair, and sovereignty measurement |
| Anti-convergence | [Orthogonal Signal](https://github.com/TrivianInstitute/Orthogonal-signal) | Novelty, constraint-origin, and difference-preservation research |
| Network | [Trivian Resonance Lattice](https://github.com/TrivianInstitute/Trivian-resonance-lattice) | Network propagation, entrainment, repair, and dissolution |
| Continuity | [TRIA Diachronic Sovereignty](https://github.com/TrivianInstitute/tria-diachronic-sovereignty) | Persistent relational state, consent, provenance, and sovereignty through time |
| SDK | [TRIA SDK](https://github.com/TrivianInstitute/tria-sdk) | Canonical developer-facing governance kernel and execution boundary |

You do **not** need to clone every research repository in order to use the SDK.

## Optional: reproduce the component implementations

Researchers who want to inspect the pre-SDK reference implementations can create a shared workspace:

```bash
mkdir tria-research-workspace
cd tria-research-workspace

git clone https://github.com/TrivianInstitute/Syzygy-rosetta.git
git clone https://github.com/TrivianInstitute/Coheronmetry.git
git clone https://github.com/TrivianInstitute/Orthogonal-signal.git
git clone https://github.com/TrivianInstitute/Trivian-resonance-lattice.git
```

Create and activate a virtual environment, then install:

```bash
python -m pip install \
  -e './Syzygy-rosetta[dev]' \
  -e './Coheronmetry[dev]' \
  -e './Orthogonal-signal[dev]' \
  -e './Trivian-resonance-lattice[dev]'
```

Run each repository's tests from that repository. These suites validate their own encoded reference behavior; they are no longer the required installation route for application developers.

## What is deployable today?

`tria-sdk` v0.1 alpha is the current deployable software artifact. It provides:

- immutable relational events and deterministic state reduction;
- SQLite persistence and replay;
- scoped consent and governed capabilities;
- policy, delegation, lifecycle, and provenance controls;
- epistemic claims and preserved disagreement;
- governed context and invocation planning;
- provider-neutral execution boundaries;
- portable replay bundles and compatibility gates; and
- conformance fixtures and release-readiness tests.

"Deployable" here means it can be cloned, installed, imported, tested, and integrated into an application. It does **not** mean production-certified, empirically validated, or appropriate for consequential deployment without independent testing and application-specific safeguards.

## Choose an entry point

- **Implement TRIA in software:** [`tria-sdk`](https://github.com/TrivianInstitute/tria-sdk)
- **Understand the complete architecture:** continue with the [TRIA README](README.md)
- **Orient a human or machine reader:** [Trivian AI Resonance Key](https://github.com/TrivianInstitute/Trivian-ai-resonance-key)
- **Study interaction governance:** [Syzygy Rosetta](https://github.com/TrivianInstitute/Syzygy-rosetta)
- **Study relational measurement:** [Coheronmetry](https://github.com/TrivianInstitute/Coheronmetry)
- **Study difference and anti-convergence:** [Orthogonal Signal](https://github.com/TrivianInstitute/Orthogonal-signal)
- **Study network-scale propagation:** [Trivian Resonance Lattice](https://github.com/TrivianInstitute/Trivian-resonance-lattice)
- **Study persistence and sovereignty through time:** [TRIA Diachronic Sovereignty](https://github.com/TrivianInstitute/tria-diachronic-sovereignty)

## Licensing and commercial use

The `tria-sdk` is source-available for noncommercial use under the PolyForm Noncommercial License 1.0.0. Commercial use requires a separate written license from Trivian Institute.

Research repositories and publications may carry their own governing license files. Always review the license in the specific repository or artifact you are using.

Commercial licensing inquiries: [connect@trivianinstitute.org](mailto:connect@trivianinstitute.org).

## Help, research, and contributions

Questions, reproducibility reports, falsification attempts, and implementation findings may be submitted through the relevant repository's GitHub Issues page or sent to [connect@trivianinstitute.org](mailto:connect@trivianinstitute.org).

When reporting an implementation problem, include your operating system, Python version, installation command, complete error message, and repository commit tested.
