"""
Operational Purpose:
    Pre-analysis verification of conversions.json. Ensures the conversion results
    file exists, satisfies minimum byte size constraints from workflow-config.json,
    is valid JSON, and contains successful conversions. Replaces inline bash in
    security-reports-pipeline.yml and refresh-old-conversions.yml.

Required Environment Variables:
    GITHUB_OUTPUT (optional): Path to write step outputs.

Outputs:
    has_successful (bool): 'true' if one or more conversions succeeded, 'false' otherwise.
    successful_count (int): Number of successful conversions.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json (workflow.validation.min_json_size_bytes)
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class ConversionVerificationConfigLoader:
    """Loads validation configuration from workflow-config.json with fail-fast validation."""

    def __init__(self, artifacts_dir: str = ".github/artifacts") -> None:
        self.config_path = Path(artifacts_dir) / "workflow-config.json"
        self.config = self._load()

    def _load(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Missing required artifact: '{self.config_path}'.")
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON artifact '{self.config_path}': {e}") from e

        workflow = data.get("workflow", {})
        val_cfg = workflow.get("validation")
        if not val_cfg or not isinstance(val_cfg, dict):
            raise KeyError(f"Missing 'workflow.validation' section in '{self.config_path}'.")
        return val_cfg

    @property
    def min_json_size_bytes(self) -> int:
        val = self.config.get("min_json_size_bytes")
        if val is None:
            raise KeyError(
                f"Missing required key 'min_json_size_bytes' in 'workflow.validation' of '{self.config_path}'."
            )
        return int(val)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify conversions.json before analysis.")
    parser.add_argument("--conversions-file", default="conversions.json", help="Path to conversions.json")
    parser.add_argument("--artifacts-dir", default=".github/artifacts", help="Path to artifacts directory")
    args = parser.parse_args()

    loader = ConversionVerificationConfigLoader(artifacts_dir=args.artifacts_dir)
    min_size = loader.min_json_size_bytes

    conv_path = Path(args.conversions_file)
    if not conv_path.exists():
        print(f"❌ '{conv_path}' not found.", file=sys.stderr)
        return 1

    file_size = conv_path.stat().st_size
    if file_size < min_size:
        print(f"❌ '{conv_path}' too small ({file_size} < {min_size} bytes).", file=sys.stderr)
        return 1

    try:
        with open(conv_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Invalid JSON in '{conv_path}': {e}", file=sys.stderr)
        return 1

    if not isinstance(data, list):
        print(f"❌ Expected list in '{conv_path}', got {type(data).__name__}.", file=sys.stderr)
        return 1

    successful = [item for item in data if isinstance(item, dict) and item.get("status") == "success"]
    success_count = len(successful)

    has_successful = "true" if success_count > 0 else "false"

    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write(f"has_successful={has_successful}\n")
            f.write(f"successful_count={success_count}\n")

    if success_count == 0:
        print("⊘ No successful conversions to analyze.")
        return 0

    print(f"✓ Verification passed — {success_count} conversion(s) ready for analysis.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
