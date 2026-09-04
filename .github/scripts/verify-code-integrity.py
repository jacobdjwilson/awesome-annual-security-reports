"""
Operational Purpose:
    Fast CI release gating validator for GitHub Actions. Validates Python compilation across
    all repository scripts, AGENTS.md 4-part docstring compliance, JSON artifact schema integrity,
    and AI prompt structure formatting without requiring heavy local execution dependencies.

Required Environment Variables:
    GITHUB_OUTPUT (optional): Path to write step outputs in GitHub Actions.

Outputs:
    checks_passed: 'true' or 'false'
    error_count: Number of failed validation checks.
    script_count: Total Python scripts inspected.
    artifact_count: Total JSON artifacts validated.
    prompt_count: Total AI prompt documents validated.

JSON Artifact Dependencies:
    .github/artifacts/workflow-config.json
    .github/artifacts/ai-models.json
    .github/artifacts/report-categories.json
    .github/artifacts/discovery-feedback.json
    .github/artifacts/readme-updater-config.json
    .github/artifacts/google-search-config.json
"""

import os
import sys
import glob
import json
import py_compile
from pathlib import Path
from typing import List, Dict, Tuple, Any

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def write_github_output(key: str, value: Any) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        try:
            with open(output_path, "a", encoding="utf-8") as f:
                f.write(f"{key}={value}\n")
        except Exception as e:
            print(f"Warning: Failed to write to GITHUB_OUTPUT: {e}", file=sys.stderr)


def check_python_compilation(scripts_dir: str = ".github/scripts") -> Tuple[int, List[str]]:
    """Validates that all Python scripts compile with zero syntax errors."""
    errors: List[str] = []
    scripts = sorted(glob.glob(f"{scripts_dir}/*.py"))
    print(f"\n[1/4] Compiling {len(scripts)} Python scripts...")

    for script_path in scripts:
        try:
            py_compile.compile(script_path, doraise=True)
        except Exception as e:
            msg = f"Syntax error in {script_path}: {e}"
            errors.append(msg)
            print(f"::error file={script_path}::{msg}")

    if not errors:
        print(f"  ✓ All {len(scripts)} scripts compiled cleanly.")
    return len(scripts), errors


def check_docstrings(scripts_dir: str = ".github/scripts") -> Tuple[int, List[str]]:
    """Validates that all Python scripts adhere to the 4-part AGENTS.md docstring standard."""
    required_sections = [
        "Operational Purpose:",
        "Required Environment Variables:",
        "Outputs:",
        "JSON Artifact Dependencies:",
    ]
    errors: List[str] = []
    scripts = sorted(glob.glob(f"{scripts_dir}/*.py"))
    print(f"\n[2/4] Verifying AGENTS.md docstring standard across {len(scripts)} scripts...")

    for script_path in scripts:
        with open(script_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        missing = [sec for sec in required_sections if sec not in content]
        if missing:
            msg = f"Missing mandatory docstring section(s) in {script_path}: {', '.join(missing)}"
            errors.append(msg)
            print(f"::error file={script_path}::{msg}")

    if not errors:
        print(f"  ✓ All {len(scripts)} scripts strictly satisfy AGENTS.md docstring requirements.")
    return len(scripts), errors


def check_json_artifacts(artifacts_dir: str = ".github/artifacts") -> Tuple[int, List[str]]:
    """Validates JSON syntax and required top-level keys for all repository artifacts."""
    errors: List[str] = []
    artifacts = sorted(glob.glob(f"{artifacts_dir}/*.json"))
    print(f"\n[3/4] Validating {len(artifacts)} JSON configuration artifacts...")

    for artifact_path in artifacts:
        try:
            with open(artifact_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, dict):
                errors.append(f"{artifact_path}: Root must be a JSON object")
        except Exception as e:
            msg = f"JSON parse failure in {artifact_path}: {e}"
            errors.append(msg)
            print(f"::error file={artifact_path}::{msg}")

    # Specific required schema checks
    wf_cfg_path = Path(artifacts_dir) / "workflow-config.json"
    if wf_cfg_path.exists():
        try:
            with open(wf_cfg_path, "r", encoding="utf-8") as f:
                wf_cfg = json.load(f)
            wf = wf_cfg.get("workflow", {})
            for key in ["discovery", "conversion", "validation", "pull_request"]:
                if key not in wf:
                    errors.append(f"workflow-config.json missing 'workflow.{key}' section")
        except Exception:
            pass

    if not errors:
        print(f"  ✓ All {len(artifacts)} JSON configuration artifacts validated cleanly.")
    return len(artifacts), errors


def check_ai_prompts(prompts_dir: str = ".github/ai-prompts") -> Tuple[int, List[str]]:
    """Validates that all AI prompt markdown files satisfy the standardized prompt structure."""
    errors: List[str] = []
    prompts = sorted(glob.glob(f"{prompts_dir}/*.md"))
    print(f"\n[4/4] Validating {len(prompts)} AI prompt templates...")

    for prompt_path in prompts:
        with open(prompt_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        if not content.startswith("# AI Instruction Set for"):
            errors.append(f"{prompt_path}: Must begin with H1 title '# AI Instruction Set for ...'")
        if "## Purpose" not in content:
            errors.append(f"{prompt_path}: Missing mandatory '## Purpose' section")
        if "## Goals" not in content:
            errors.append(f"{prompt_path}: Missing mandatory '## Goals' section")
        if "---" not in content:
            errors.append(f"{prompt_path}: Missing runtime sentinel horizontal rule '---'")

    if not errors:
        print(f"  ✓ All {len(prompts)} AI prompt markdown files satisfy repository standards.")
    return len(prompts), errors


def main() -> int:
    print("=" * 70)
    print("CI Code & Configuration Integrity Gate")
    print("=" * 70)

    num_scripts, compile_errs = check_python_compilation()
    _, doc_errs = check_docstrings()
    num_artifacts, json_errs = check_json_artifacts()
    num_prompts, prompt_errs = check_ai_prompts()

    all_errors = compile_errs + doc_errs + json_errs + prompt_errs
    total_errors = len(all_errors)
    passed = total_errors == 0

    write_github_output("checks_passed", "true" if passed else "false")
    write_github_output("error_count", total_errors)
    write_github_output("script_count", num_scripts)
    write_github_output("artifact_count", num_artifacts)
    write_github_output("prompt_count", num_prompts)

    print("\n" + "=" * 70)
    if passed:
        print("✅ ALL CI GATING CHECKS PASSED — Code and configurations are compliant.")
        print("=" * 70 + "\n")
        return 0
    else:
        print(f"❌ CI GATING FAILED with {total_errors} violation(s):")
        for err in all_errors:
            print(f"   • {err}")
        print("=" * 70 + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
