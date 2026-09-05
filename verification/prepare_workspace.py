"""Clone immutable component revisions into a new, non-overwritten workspace."""
import json
import subprocess
from pathlib import Path

pins = json.loads((Path(__file__).parent / "components.lock.json").read_text())
workspace = Path("verification-workspace")
workspace.mkdir(exist_ok=False)
for name, sha in pins.items():
    target = workspace / name
    subprocess.run(["git", "clone", "https://github.com/TrivianInstitute/" + name + ".git", str(target)], check=True)
    subprocess.run(["git", "-C", str(target), "checkout", "--detach", sha], check=True)
print("Prepared", workspace.resolve())
