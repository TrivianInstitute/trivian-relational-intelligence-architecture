"""Clone pinned post-propagation component revisions into a fresh workspace."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--workspace",
    type=Path,
    default=Path("generative-verification-workspace"),
    help="New directory to create; existing paths are refused.",
)
args = parser.parse_args()

pins = json.loads((Path(__file__).parent / "generative_components.lock.json").read_text())
workspace = args.workspace
workspace.mkdir(exist_ok=False)

for name, sha in pins.items():
    target = workspace / name
    subprocess.run(
        ["git", "clone", "https://github.com/TrivianInstitute/" + name + ".git", str(target)],
        check=True,
    )
    subprocess.run(["git", "-C", str(target), "checkout", "--detach", sha], check=True)

print("Prepared", workspace.resolve())
