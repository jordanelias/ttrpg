#!/usr/bin/env python3
"""review_core.py — the single repository-state review engine (Repository State Armature, ED-IN-0077).

One core, three faces (CLAUDE.md §8 "every rule lives once") — all read from HERE: the SessionStart
banner (tools/session_status.py, BUILT), a GitHub `review-state` job (Phase 4), and the published
artifact (Phase 2; write_state already emits the js bundle). Only the banner is wired today. This
module implements ZERO rules of its own — it is a VERDICT AGGREGATOR that runs each existing check
tool and normalizes the result into a Signal, then rolls the signals up into one per-lane + overall
repository grade.

The ratchet: report-only signals are graded against `registers/review_baseline.yaml` — a signal
is a REGRESSION (and fails `--check`) only when it exceeds its accepted baseline. Debt can only
shrink; each shrink is a one-line baseline edit in the PR that earns it. This makes report-only
signals blocking-on-regression from day one with no branch-protection edits and no job renames.

CLI:
  python3 tools/review_core.py --json       # compute + write review_state.json, print it
  python3 tools/review_core.py --summary     # banner lines (roll-up grade + worst signals)
  python3 tools/review_core.py --check        # exit 1 on any blocking failure OR regression-vs-baseline
  python3 tools/review_core.py --fast         # read the last committed review_state.json (no recompute)

Design: systems/_architecture/repo_state_armature_v1.md (PROPOSED, ED-IN-0077).
Status: PROVISIONAL — Phase-1 minimal core. Collectors are subprocess-based here; the Phase-2
inversion promotes the hottest ones to in-process imports. Adding a signal = one row in CHECKS.
"""
from __future__ import annotations
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "tools" / "observability" / "review_state.json"
BASELINE_PATH = ROOT / "registers" / "review_baseline.yaml"
SCHEMA_VERSION = 1
_TIMEOUT = 90  # per-check seconds; a hung check degrades to `error`, never blocks the engine

# ── the signal registry: (id, argv, tier, lane, count_re?) ────────────────────
#   tier: "blocking"  -> a nonzero exit fails --check outright
#         "report_only" -> graded against the baseline ratchet (regression fails --check)
#         "info"        -> surfaced, never fails
#   count_re (optional): a regex whose FIRST group captures the debt count the tool prints on
#         FAILURE. When present, the ratchet compares the parsed count to the baseline ceiling
#         (regression = count > ceiling) instead of the boolean exit code — so a report_only
#         signal detects a debt that GROWS while staying above its accepted floor. Without a
#         count_re, a failure falls back to the boolean rule (any fail on a baseline-0 signal
#         regresses). count is read only on failure; a passing check is always count 0.
# Adding a check to the armature is a single row here. All are existing CLIs (has_cli in
# references/apparatus_registry.yaml); review_core runs them, it does not reimplement them.
CHECKS = [
    {"id": "currency.stamps",   "argv": ["tools/currency_consistency_check.py"], "tier": "report_only", "lane": "IN",
     "count_re": r"\[CURRENCY DRIFT: (\d+)\]"},
    {"id": "vocab.a17",         "argv": ["tools/ci_quantity_vocabulary_check.py"], "tier": "report_only", "lane": "IN",
     "count_re": r"(\d+) unresolved"},
    {"id": "wiring.coverage",   "argv": ["tools/wiring_map_check.py", "--check"],  "tier": "report_only", "lane": "IN"},
    {"id": "definitions.parity", "argv": ["tools/definitions_store.py", "--check"], "tier": "report_only", "lane": "IN"},
    {"id": "vocab.parity",      "argv": ["tools/vocab_store.py", "--check"],       "tier": "report_only", "lane": "IN"},
    {"id": "sim_params.export", "argv": ["tools/export_sim_params.py", "--check"], "tier": "report_only", "lane": "IN"},
    {"id": "value_links.export", "argv": ["tools/link_values_pointers.py", "--check"], "tier": "report_only", "lane": "IN"},
    {"id": "audit.staleness",   "argv": ["tools/audit_staleness.py"],             "tier": "info",        "lane": "IN"},
    {"id": "workplan.state",    "argv": ["tools/workplan_status.py"],             "tier": "info",        "lane": "IN"},
]

_GRADE_ORDER = {"GREEN": 0, "AMBER": 1, "RED": 2}


def _load_baseline() -> dict:
    """Read the ratchet. Absent/unparseable baseline => empty (every report_only signal is then
    graded at ceiling 0, i.e. any failure is a regression) — fail-toward-visibility, never crash."""
    try:
        import yaml  # optional at runtime (SessionStart may lack pyyaml); guarded
    except Exception:
        return {}
    try:
        data = yaml.safe_load(BASELINE_PATH.read_text()) or {}
        if not isinstance(data, dict):
            return {}
        rows = data.get("signals", data)  # rows live under `signals:`; tolerate a flat map too
        return rows if isinstance(rows, dict) else {}
    except Exception:
        return {}


def _run_check(chk: dict) -> dict:
    """Run one check CLI; normalize to a Signal. Never raises."""
    argv = [sys.executable, str(ROOT / chk["argv"][0]), *chk["argv"][1:]]
    started = time.monotonic()
    try:
        proc = subprocess.run(argv, cwd=str(ROOT), capture_output=True, text=True, timeout=_TIMEOUT)
        rc = proc.returncode
        out = (proc.stdout or "") + (proc.stderr or "")
        verdict = "pass" if rc == 0 else "fail"
        detail = [ln for ln in out.strip().splitlines() if ln.strip()][-4:]
        count = _parse_count(chk.get("count_re"), out, verdict)
    except subprocess.TimeoutExpired:
        rc, verdict, detail, count = 124, "error", [f"timeout after {_TIMEOUT}s"], None
    except Exception as exc:  # unrunnable executable, OSError, etc. — degrade, don't crash the engine.
        # NOTE: a missing *.py tool does NOT land here — `python missing.py` exits 2, so it is
        # graded a "fail" (rc 2), which correctly alarms rather than passing silently.
        rc, verdict, detail, count = 127, "error", [f"{type(exc).__name__}: {exc}"], None
    return {
        "id": chk["id"], "source": "tools/" + chk["argv"][0].split("/")[-1],
        "tier": chk["tier"], "lane": chk["lane"], "verdict": verdict, "returncode": rc,
        "count": count,
        "elapsed_ms": int((time.monotonic() - started) * 1000), "detail": detail,
    }


def _parse_count(count_re: str | None, out: str, verdict: str) -> int | None:
    """The debt count a report_only tool prints on failure. A passing check is always 0 debt.
    On failure: parse count_re's first group if given; None (=> boolean fallback) if it can't."""
    if verdict == "pass":
        return 0
    if not count_re:
        return None
    m = re.search(count_re, out)
    return int(m.group(1)) if m else None


def _apply_ratchet(sig: dict, baseline: dict) -> dict:
    """Grade a report_only signal against its baseline row. A `fail` whose debt count is at or
    under the baseline ceiling is accepted debt (regressed=False); a count ABOVE the ceiling, or
    a fresh fail on a baseline-0 signal, regresses."""
    row = baseline.get(sig["id"], {}) if isinstance(baseline.get(sig["id"]), dict) else {}
    ceiling = row.get("baseline")
    sig["baseline"] = ceiling
    count = sig.get("count")
    if sig["tier"] != "report_only" or sig["verdict"] != "fail":
        sig["regressed"] = False
    elif isinstance(count, int):
        # count-aware ratchet: a growing debt regresses even while it stays above its floor.
        sig["regressed"] = count > (ceiling if isinstance(ceiling, int) else 0)
    else:
        # boolean fallback (tool prints no parseable count): any fail on a baseline-0 signal
        # regresses; a fail on a baseline>0 signal is presumed at-or-under its ceiling.
        sig["regressed"] = not (isinstance(ceiling, int) and ceiling > 0)
    return sig


def collect() -> dict:
    """Run every check, roll up. This is the exhaustive repository-state review."""
    baseline = _load_baseline()
    signals = [_apply_ratchet(_run_check(c), baseline) for c in CHECKS]
    blocking_failures = sum(1 for s in signals if s["tier"] == "blocking" and s["verdict"] != "pass")
    regressions = sum(1 for s in signals if s.get("regressed"))
    report_only_failures = sum(1 for s in signals if s["tier"] == "report_only" and s["verdict"] == "fail")
    errors = sum(1 for s in signals if s["verdict"] == "error")
    if blocking_failures or regressions:
        grade = "RED"
    elif report_only_failures or errors:
        grade = "AMBER"
    else:
        grade = "GREEN"
    # per-lane roll-up
    subsystems: dict[str, dict] = {}
    for s in signals:
        lane = s["lane"]
        sub = subsystems.setdefault(lane, {"grade": "GREEN", "signals": []})
        sub["signals"].append(s["id"])
        g = "RED" if (s["tier"] == "blocking" and s["verdict"] != "pass") or s.get("regressed") \
            else ("AMBER" if s["verdict"] in ("fail", "error") else "GREEN")
        if _GRADE_ORDER[g] > _GRADE_ORDER[sub["grade"]]:
            sub["grade"] = g
    head = _head_sha()
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_epoch": int(time.time()),
        "head_sha": head,
        "rollup": {
            "grade": grade, "blocking_failures": blocking_failures,
            "regressions_vs_baseline": regressions, "report_only_failures": report_only_failures,
            "errors": errors, "signal_count": len(signals),
        },
        "signals": signals,
        "subsystems": subsystems,
    }


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(ROOT),
                              capture_output=True, text=True, timeout=10).stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def write_state(state: dict) -> None:
    """Persist review_state.json + a window.VALORIA_REVIEW js bundle (for the artifact face).
    NOTE: not committed on every run — head_sha embedding would manufacture perpetual currency
    drift; the committed copy is refreshed by the refresh workflow, same as the decisions digest."""
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n")
    js = STATE_PATH.with_name("review_state_data.js")
    js.write_text("window.VALORIA_REVIEW = " + json.dumps(state, indent=2) + ";\n")


def summary_lines(fast: bool = False) -> list[str]:
    """Banner lines for the SessionStart face. fast=True reads the last LOCALLY-GENERATED state
    (review_state.json is git-ignored, so on a fresh clone it is absent and the banner shows one
    'not yet computed' line until `--json` runs — the Phase-4 refresh closes this gap). fast avoids
    the collection cost / subprocess-hang risk at session start."""
    state = None
    if fast:
        # SessionStart face: read the last locally-generated state ONLY (gitignored — see docstring);
        # never pay the collection cost or risk a subprocess hang at session start. Absent => info line.
        try:
            state = json.loads(STATE_PATH.read_text())
        except Exception:
            return ["repo-state: not yet computed — run `python tools/review_core.py --json`"]
    if state is None:
        state = collect()
    r = state["rollup"]
    lines = [f"repo-state: {r['grade']} · {r['blocking_failures']} blocking · "
             f"{r['regressions_vs_baseline']} regressions · {r['report_only_failures']} report-only · "
             f"{r.get('errors', 0)} errors ({r['signal_count']} signals)"]
    worst = [s for s in state["signals"] if s["verdict"] != "pass"]
    for s in worst[:3]:
        tag = "REGRESS" if s.get("regressed") else s["verdict"]
        cnt = s.get("count")
        gauge = f" {cnt}/{s.get('baseline')}" if isinstance(cnt, int) else ""
        lines.append(f"  [{tag}] {s['id']}{gauge} ({s['source']})")
    return lines


def main(argv: list[str]) -> int:
    mode = argv[1] if len(argv) > 1 else "--summary"
    fast = "--fast" in argv
    if mode == "--summary":
        print("\n".join(summary_lines(fast=fast)))
        return 0
    state = collect()
    if mode == "--json":
        write_state(state)
        print(json.dumps(state, indent=2))
        return 0
    if mode == "--check":
        # --check computes in memory only; it does NOT write review_state.json (writing embeds
        # head_sha and would dirty the tree on every CI/local check — the drift trap the armature
        # exists to prevent). Only --json (the refresh path) persists state.
        r = state["rollup"]
        if r["blocking_failures"] or r["regressions_vs_baseline"]:
            print(f"[REVIEW-STATE] {r['grade']}: {r['blocking_failures']} blocking, "
                  f"{r['regressions_vs_baseline']} regression(s) vs baseline", file=sys.stderr)
            for s in state["signals"]:
                if s.get("regressed") or (s["tier"] == "blocking" and s["verdict"] != "pass"):
                    print(f"  - {s['id']}: {s['verdict']} (baseline={s.get('baseline')})", file=sys.stderr)
            return 1
        print(f"[REVIEW-STATE] {r['grade']} — no blocking failures or regressions "
              f"({r['report_only_failures']} report-only at/under baseline)")
        return 0
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
