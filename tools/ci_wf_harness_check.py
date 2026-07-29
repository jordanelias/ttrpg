#!/usr/bin/env python3
"""Workflow run-discipline gate — the .claude/wf_*.js harness must be present, current, and USED (ED-IN-0087).

WHY THIS EXISTS. ED-IN-0085 measured the .claude/ orchestration scripts against nine external
practice sources and found the same four holes in all three: no loop-termination discipline of any
kind, critic independence asserted only as a sentence inside a prompt, no alarm when a critic
returned nothing, and no record of a disagreement the run then failed to resolve. The fix is a
shared prelude (`tools/wf_harness.js`) — but workflow scripts run in a sandbox with no filesystem
and no Node API, so they cannot import it. It is copied in verbatim between sentinels instead.

A copied rule rots. That is precisely the §0.1 point-5 signature this repo keeps hitting: code that
was correct when written and stopped being correct because something else moved. So the rule has one
owner (tools/wf_harness.js) and this is the guard that fails on recurrence.

WHAT IT CHECKS
  1. PRESENCE + BYTE-IDENTITY. Every .claude/wf_*.js carries the sentinel block, and its contents
     match the owner exactly. `--fix` re-syncs.
  2. STRUCTURAL USE, not just presence. A prelude nobody calls is dead data — the exact defect
     class these workflows exist to hunt, and shipping it here would be indefensible. Each script
     must actually build a run, report per-lens results, rank by rediscovery, and return a summary.
  3. READ-ONLY CRITICS ARE STRUCTURAL. Every agent() whose label or phase marks it a critic must
     route through hCritic() — which sets the agentType whose definition has no write tools. The
     old mechanism was the string "You are READ-ONLY" inside a prompt, which restricts nothing.
     VERIFIED 2026-07-28, not assumed: the restriction and a `schema` COMPOSE. A controlled 3-agent
     probe had the restricted critic report its own tools as [Read, Grep, Glob, StructuredOutput]
     against an unrestricted control reporting 20+ including Write and Bash — so the schema tool is
     injected ON TOP of the frontmatter list, and no critic stage returns null for this reason. The
     write attempt created nothing on disk (checked independently of the agent's own claim).
  4. THE FABLE RULING. Jordan ruled 2026-07-28 that fable is a read-only audit / planner /
     orchestrator / guardrail tier and NOT a synthesis or artifact-authorship tier (CLAUDE.md §10).
     A script that puts model:'fable' on a stage that writes files contradicts ratified canon.

WHAT IT DOES NOT DO. It cannot check that a workflow's *reasoning* is disciplined, only that the
mechanism is wired in and callable. Same limit as every other gate in tools/: it narrows the
surface, it does not close it. The behavioural half — that the breaker actually fires, that
signal() never throws — is tests/valoria/test_wf_harness.py, which executes the harness.

Usage:  python tools/ci_wf_harness_check.py [--fix] [--staged]
Exit 1 on violation.
"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWNER = os.path.join(ROOT, "tools", "wf_harness.js")
WF_GLOB = os.path.join(ROOT, ".claude", "wf_*.js")
CRITIC_AGENT = os.path.join(ROOT, ".claude", "agents", "valoria-critic.md")

BEGIN = "// ==== VALORIA WF HARNESS v1 — GENERATED FROM tools/wf_harness.js — DO NOT EDIT HERE ===="
END = "// ==== END VALORIA WF HARNESS v1 ===="

# Required call sites, each tied to the proposal it executes. The message is the point: a bare
# "missing hRediscover" tells a future reader nothing about why the call has to be there.
REQUIRED_CALLS = [
    ("hRun(", "P3", "build a run recorder — `const run = hRun('<workflow-name>')`"),
    ("run.lens(", "P7a", "report each lens/stage's findings through run.lens() so a zero-finding "
                         "stage raises the null_result alarm instead of passing silently"),
    ("hRediscover(", "P7b", "rank findings by how many independent lenses surfaced them — this "
                            "signal is already produced by the fan-out and was being discarded"),
    ("run.summary()", "P3", "return the run summary, so stop_reason and every signal reach the reader"),
    ("hCritic(", "P4", "route critic stages through hCritic() for a structurally read-only agentType"),
]

# An agent() call is a critic stage if its label or phase says so. These are the words the three
# scripts actually use; a new critic phase under a new name needs adding here, deliberately.
CRITIC_MARKERS = ("critic", "verify", "adversarial", "refut", "skeptic")

# The subset of hRun's API a script may call. Guards against a copy inventing a method the owner
# does not define — which would fail silently in the sandbox (TypeError inside one agent's stage).
RUN_METHODS = {"signal", "round", "lens", "critiqued", "dispute", "adjudicate", "summary", "trace_",
               "attempt", "attempted", "lost",
               "signals", "disagreements", "trace", "rounds", "cap", "name"}


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _owner_block():
    text = _read(OWNER)
    i, j = text.find(BEGIN), text.find(END)
    if i < 0 or j < 0:
        raise SystemExit(f"[wf-harness ✗] {OWNER} has lost its sentinels — it is the owner; repair it first.")
    return text[i:j + len(END)]


def _staged_paths():
    try:
        r = subprocess.run(["git", "diff", "--cached", "--name-only"],
                           cwd=ROOT, capture_output=True, text=True, check=True)
        return set(r.stdout.split())
    except Exception:
        return set()


def _insert_at(text):
    """Byte offset just after the `export const meta = { ... }` block.

    Placement is not cosmetic. These scripts are top-level-await modules that execute in source
    order, and the harness declares `const`s — appending it to the end would put every call site
    in the temporal dead zone and throw `ReferenceError` on the first stage. So: immediately after
    meta, before any script code. If meta is missing (it is mandatory for a workflow), fall back to
    the top of the file rather than guessing.
    """
    m = re.search(r"^export const meta\s*=\s*\{", text, re.M)
    if not m:
        return 0
    depth, i = 0, m.end() - 1
    while i < len(text):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return 0


def _agent_calls(text):
    """Yield (line_no, call_text) for each agent(...) options object.

    Deliberately crude: it scans for the options object that follows the prompt, which in these
    scripts is always a single-line `{ ... }` literal on the agent() call. A multi-line options
    object would be missed — recorded as a known limit rather than pretended away, and the reason
    the behavioural test exists alongside this one.
    """
    for i, line in enumerate(text.splitlines(), 1):
        for m in re.finditer(r"\{[^{}]*\b(?:label|phase)\s*:[^{}]*\}", line):
            yield i, m.group(0)


def check(fix=False, staged_only=False):
    if not os.path.exists(OWNER):
        print(f"[wf-harness ✗] owner missing: {os.path.relpath(OWNER, ROOT)}")
        return 1
    block = _owner_block()
    scripts = sorted(glob.glob(WF_GLOB))
    if not scripts:
        print("[wf-harness ✗] no .claude/wf_*.js found — this gate would pass vacuously")
        return 1

    staged = _staged_paths() if staged_only else None
    violations, fixed = [], []

    if not os.path.exists(CRITIC_AGENT):
        violations.append((".claude/agents/valoria-critic.md", 0,
                           "the read-only critic agent definition is missing — hCritic() would name "
                           "an agentType that does not resolve, and critic independence silently "
                           "reverts to a prompt string (P4)"))
    else:
        fm = _read(CRITIC_AGENT)
        tools_line = re.search(r"^tools:\s*(.+)$", fm, re.M)
        if not tools_line:
            violations.append((".claude/agents/valoria-critic.md", 0,
                               "no `tools:` frontmatter — an agent with no tools list inherits "
                               "everything, including Write. That is the defect P4 fixes."))
        else:
            granted = {t.strip() for t in tools_line.group(1).split(",") if t.strip()}
            writers = granted & {"Write", "Edit", "NotebookEdit", "Bash", "Artifact"}
            if writers:
                violations.append((".claude/agents/valoria-critic.md", 0,
                                   f"grants write-capable tool(s) {sorted(writers)} — the critic's "
                                   f"independence is supposed to be structural, not declared"))

    for path in scripts:
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
        if staged is not None and rel not in staged:
            continue
        text = _read(path)
        i, j = text.find(BEGIN), text.find(END)

        # 1. presence + byte-identity
        if i < 0 or j < 0:
            if fix:
                at = _insert_at(text)
                text = text[:at] + "\n\n" + block + "\n" + text[at:].lstrip("\n")
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(text)
                fixed.append(f"{rel}: harness inserted after meta")
            else:
                violations.append((rel, 1, "carries no harness block. Every workflow needs the run "
                                           "discipline; run `python tools/ci_wf_harness_check.py --fix`."))
                continue
            i, j = text.find(BEGIN), text.find(END)
        else:
            have = text[i:j + len(END)]
            if have != block:
                if fix:
                    text = text[:i] + block + text[j + len(END):]
                    with open(path, "w", encoding="utf-8") as fh:
                        fh.write(text)
                    fixed.append(f"{rel}: harness re-synced from owner")
                else:
                    violations.append((rel, text[:i].count("\n") + 1,
                                       "harness block has DRIFTED from tools/wf_harness.js. The owner is "
                                       "the only editable copy (CLAUDE.md §8: every rule lives once); "
                                       "re-sync with --fix, or move your change into the owner first."))

        # The script's own code, harness blanked OUT rather than cut out: the block is replaced by
        # the same number of newlines so every offset below still maps to the real file line. Cutting
        # it made every reported line number wrong by ~220 — a checker that mis-cites its own findings
        # is worse than no checker, since the first thing a reader does is open the cited line.
        harness = text[i:j + len(END)]
        body = text[:i] + ("\n" * harness.count("\n")) + text[j + len(END):]

        # 1b. PLACEMENT. `const` does not hoist: a harness below its first call site throws
        # ReferenceError on the first stage, which in the sandbox surfaces as one agent dying
        # rather than as a syntax error anyone would notice.
        first_use = min([m.start() for m in re.finditer(r"\bh(?:Run|Critic|Rediscover|FindingKey)\(", text)
                         if m.start() > j + len(END) or m.start() < i] or [len(text)])
        if first_use < i:
            violations.append((rel, text[:first_use].count("\n") + 1,
                               "calls the harness BEFORE the harness block is declared. `const` does not "
                               "hoist — this throws ReferenceError inside the first stage at run time. "
                               "The block belongs immediately after `export const meta`."))

        # 2. structural use
        for token, prop, why in REQUIRED_CALLS:
            if token not in body:
                violations.append((rel, 0, f"[{prop}] never calls `{token}` — {why}. A prelude nobody "
                                           f"calls is dead data, which is the defect these workflows audit for."))

        # a method the owner does not define fails only at runtime, inside one agent's stage
        for m in re.finditer(r"\brun\.([A-Za-z_][A-Za-z0-9_]*)", body):
            if m.group(1) not in RUN_METHODS:
                violations.append((rel, body[:m.start()].count("\n") + 1,
                                   f"calls run.{m.group(1)}(), which tools/wf_harness.js does not define — "
                                   f"it would throw inside a stage at run time"))

        # 3. critic stages must be structurally read-only
        for lineno, opts in _agent_calls(body):
            lowered = opts.lower()
            if not any(w in lowered for w in CRITIC_MARKERS):
                continue
            if "hcritic(" not in body.splitlines()[lineno - 1].lower():
                violations.append((rel, lineno, "critic/verify stage does not pass its options through "
                                                "hCritic() — it can write. Wrap the options object: "
                                                "`hCritic({ label: ..., phase: ... })`."))

        # 4. the fable ruling. A `//` line is prose ABOUT the ruling (these scripts carry a comment
        # explaining why the fable node was removed) and is inert code — flagging it would make the
        # gate un-satisfiable for anyone documenting their own compliance.
        lines = body.splitlines()
        for m in re.finditer(r"model:\s*'fable'", body):
            lineno = body[:m.start()].count("\n") + 1
            if lines[lineno - 1].lstrip().startswith("//"):
                continue
            violations.append((rel, lineno, "puts model:'fable' on a stage. Jordan ruled 2026-07-28 that "
                                            "fable is a READ-ONLY audit / planner / orchestrator / guardrail "
                                            "tier, not synthesis or artifact authorship (CLAUDE.md §10). "
                                            "Use opus for synthesis; use fable only where the stage writes "
                                            "nothing and rules on the run."))

    for f in fixed:
        print(f"  [FIXED] {f}")
    print(f"[wf-harness] {len(scripts)} workflow script(s) checked against tools/wf_harness.js")
    if violations:
        print(f"[wf-harness ✗] {len(violations)} violation(s):")
        for rel, lineno, msg in violations:
            print(f"  {rel}:{lineno}  {msg}")
        return 1
    print("[wf-harness ✓] harness present, current, and wired in every workflow")
    return 0


if __name__ == "__main__":
    sys.exit(check(fix="--fix" in sys.argv, staged_only="--staged" in sys.argv))
