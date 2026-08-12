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

# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

ROOT = ci_common.REPO
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


def _balanced(text, start):
    """Return (inner, end) for the {...} / [...] / (...) beginning at `start`, string-aware.

    Hand-rolled rather than regex because these are nested object literals containing strings that
    contain braces. A regex that "works" on the current tree and breaks on the next nested literal
    is the drift this whole file exists to prevent.
    """
    pairs = {"{": "}", "[": "]", "(": ")"}
    if start >= len(text) or text[start] not in pairs:
        return None, start
    stack, i, quote, esc = [], start, None, False
    while i < len(text):
        c = text[i]
        if quote:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == quote:
                quote = None
        elif c in "'\"`":
            quote = c
        elif c in pairs:
            stack.append(pairs[c])
        elif stack and c == stack[-1]:
            stack.pop()
            if not stack:
                return text[start + 1:i], i + 1
        i += 1
    return None, start


def _object_keys(inner):
    """Top-level keys of a JS object-literal body — nested objects/arrays/strings skipped.

    ONE DEPTH-AWARE PASS. Quoted keys were first collected by a separate regex sweep over the whole
    body, which had no notion of depth and therefore leaked nested keys: `positions: [{ 'layer': 1 }]`
    reported `layer` as a top-level key and failed a legal call. Depth is the whole job of this
    function, so the quoted-key case has to live inside the same scan, not beside it.

    Three forms are recorded as deliberately-unrepresentable keys rather than skipped, because each
    was a FALSE PASS found by adversarial review:
      `<spread>`         — `{ ...rec, finding_id: x }`: what `rec` carries is undecidable statically.
      `<non-ascii-key>`  — a unicode identifier, which used to raise AttributeError and kill the run.
      a quoted key body  — collected verbatim (`[^'"]+`, not an identifier pattern) so that
                           `'layer-disputed':` and `'$layer':` are seen and rejected, instead of
                           matching no branch at all and vanishing.
    """
    keys, i, depth, at_key = [], 0, 0, True

    def _skip_string(j):
        q, j, esc = inner[j], j + 1, False
        while j < len(inner):
            c = inner[j]
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == q:
                return j + 1
            j += 1
        return j

    while i < len(inner):
        c = inner[i]
        if c in "'\"`":
            if depth == 0 and at_key:
                j = _skip_string(i)
                body = inner[i + 1:j - 1]
                after = inner[j:].lstrip()
                if after.startswith(":"):
                    keys.append(body)
                at_key = False
                i = j
                continue
            i = _skip_string(i)
            continue
        if c in "{[(":
            depth += 1
        elif c in "}])":
            depth -= 1
        elif depth == 0 and c == ",":
            at_key = True
        elif depth == 0 and inner.startswith("...", i):
            keys.append("<spread>")
            at_key = False
            i += 3
            continue
        elif depth == 0 and at_key and (c.isalpha() or c == "_"):
            m = re.match(r"[A-Za-z_][A-Za-z0-9_]*", inner[i:])
            if m is None:
                keys.append("<non-ascii-key>")
                at_key = False
                i += 1
                continue
            after = inner[i + m.end():].lstrip()
            if after.startswith(":"):
                keys.append(m.group(0))
            at_key = False
            i += m.end()
            continue
        i += 1
    return keys


def _dispute_contract():
    """The keys run.dispute() actually reads, derived from the OWNER — never hardcoded here.

    Hardcoding them would re-create the very failure this guard closes: two copies of one rule,
    drifting apart silently. Returns (legal_keys, required_keys).
    """
    text = _read(OWNER)
    m = re.search(r"run\.dispute\s*=\s*function\s*\([^)]*\)\s*\{", text)
    if not m:
        raise SystemExit("[wf-harness ✗] tools/wf_harness.js no longer defines run.dispute — "
                         "the dispute-shape guard cannot derive its contract and would pass "
                         "vacuously. Repair the owner, or retire this check deliberately.")
    body, _ = _balanced(text, m.end() - 1)
    # Comments stripped FIRST. Otherwise a comment inside run.dispute's body mentioning a retired
    # key (`// rec.layer was retired`) would make that key legal repo-wide — silently widening the
    # contract, with no test failing. Prose about a field is not a read of it; the same rule the
    # call-site scanner applies. Latent today, one line to close.
    legal = set(re.findall(r"\brec\s*(?:&&\s*rec\s*)?\.\s*([A-Za-z_][A-Za-z0-9_]*)",
                           _blank_line_comments(body)))
    if not legal:
        raise SystemExit("[wf-harness ✗] derived an EMPTY dispute key set from the owner — this "
                         "gate would accept anything. Fix the derivation before trusting it.")
    # finding_id is the one field whose absence is unrecoverable: run.adjudicate() binds on it, so a
    # record without it can never receive a ruling and is guaranteed to reach the return unresolved.
    return legal, {"finding_id"} & legal


def _run_arities():
    """{method: required_positional_count} for `run.X = function (...)`, DERIVED from the owner.

    THE DISPUTE LESSON, GENERALISED. That defect was "the gate checks method NAMES, never argument
    shapes". Fixing it for `run.dispute` alone left the identical defect live eight lines away:
    `run.critiqued(stage, produced, reviewed)` was called with a single ARRAY in all five wave
    scripts, so `produced` was undefined, `undefined > 0` was false, and the critic-starvation
    signal could not fire. A fix that closes one instance of a pattern and not the pattern is the
    §0.1 point-5 failure in miniature, so arity is now checked for every run.* method the owner
    defines — parsed from the owner, never listed here.

    Parameters with defaults or a trailing rest are not counted as required; the owner uses neither
    today, and the parse records what it sees rather than assuming.
    """
    text = _read(OWNER)
    out = {}
    for m in re.finditer(r"run\.([A-Za-z_][A-Za-z0-9_]*)\s*=\s*function\s*\(([^)]*)\)", text):
        params = [p.strip() for p in m.group(2).split(",") if p.strip()]
        if any(p.startswith("...") or "=" in p for p in params):
            continue
        out[m.group(1)] = len(params)
    return out


def _run_calls(text, method):
    """Yield (line_no, arg_count) for each `run.<method>(...)` literal call."""
    for m in re.finditer(r"\brun\." + re.escape(method) + r"\s*\(", text):
        inner, _ = _balanced(text, m.end() - 1)
        if inner is None:
            continue
        depth, n, seen, quote = 0, 1, False, None
        i = 0
        while i < len(inner):
            c = inner[i]
            if quote:
                if c == "\\":
                    i += 2
                    continue
                if c == quote:
                    quote = None
            elif c in "'\"`":
                quote = c
            elif c in "{[(":
                depth += 1
            elif c in "}])":
                depth -= 1
            elif c == "," and depth == 0:
                n += 1
            if not c.isspace():
                seen = True
            i += 1
        yield text[:m.start()].count("\n") + 1, (n if seen else 0)


def _blank_line_comments(text):
    """Replace `//` comment bodies with spaces, preserving every byte offset and line break.

    Prose ABOUT a call is not a call. The harness's own commentary quotes `run.dispute({...})` to
    explain the rule, and scanning it as code made this gate flag the documentation of the defect
    it was written to catch. Same reasoning as the fable check's `//` skip, done positionally so
    reported line numbers stay true. Block comments are not stripped — these scripts do not use
    them, and pretending to handle a case untested against the tree is how gates rot.
    """
    out, i, quote, esc = list(text), 0, None, False
    while i < len(text):
        c = text[i]
        if quote:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == quote:
                quote = None
        elif c in "'\"`":
            quote = c
        elif c == "/" and i + 1 < len(text) and text[i + 1] == "/":
            while i < len(text) and text[i] != "\n":
                out[i] = " "
                i += 1
            continue
        i += 1
    return "".join(out)


def _dispute_calls(text):
    """Yield (line_no, keys) for each run.dispute({...}) written as a literal.

    A call whose argument is NOT a literal — run.dispute(hVerdictDispute(v, ...)) — is skipped on
    purpose: the owner built that record, so there is nothing here to drift.

    KNOWN LIMIT, measured rather than assumed. A COMPUTED key (`{ [k]: v }`) is invisible to
    _object_keys and therefore passes: its name is not decidable until run time, so no static check
    can classify it. Probed 2026-08-01 against ten adversarial literals; computed keys are the only
    form that yields a false PASS. Shorthand (`{finding_id}`), spread (`{...rec}`) and a regex
    literal containing a brace all yield an EMPTY key list, which fails the required-finding_id
    check — over-strict, and the message will misattribute the cause, but the safe direction. No
    call site in .claude/wf_*.js uses any of these forms; verified by reading all eight.
    """
    for m in re.finditer(r"\brun\.dispute\s*\(", text):
        i = m.end()
        while i < len(text) and text[i] in " \t\r\n":
            i += 1
        if i >= len(text) or text[i] != "{":
            continue
        inner, _ = _balanced(text, i)
        if inner is None:
            continue
        yield text[:m.start()].count("\n") + 1, _object_keys(inner)


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
        # ZERO SCRIPTS IS NOW A LEGITIMATE STATE (2026-08-05, the evacuation). All eight wf_*.js
        # were completed one-shot session workflows whose INPUTS were evacuated audit units and
        # engine/params docs; they were retired with their subject rather than kept pointing at
        # the fork. The vacuity this guard exists to catch is "scripts exist and the scan missed
        # them", which is still caught: the owner block must be present and parseable, and the
        # moment a wf_*.js reappears every per-script rule applies to it again.
        if not block:
            print("[wf-harness ✗] tools/wf_harness.js is missing or unparseable — the harness "
                  "owner must survive even with no consumers, or a new workflow has nothing to "
                  "copy from")
            return 1
        print("[wf-harness —] no .claude/wf_*.js in the tree. The owner (tools/wf_harness.js) is "
              "present and parseable, so a new workflow can be created correctly. Not vacuous: "
              "there is genuinely nothing to check.")
        return 0

    staged = _staged_paths() if staged_only else None
    dispute_legal, dispute_required = _dispute_contract()
    run_arities = _run_arities()
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
                    # RECOMPUTE. The insert branch above does this; this one did not, and a re-synced
                    # block of a DIFFERENT length leaves `j` pointing into the middle of the new
                    # block. Every check below then reads a half-blanked harness as if it were the
                    # script's own code — phantom violations at wrong line numbers, on the one run
                    # (`--fix`) a caller is least likely to re-verify. Caught by growing the owner.
                    i, j = text.find(BEGIN), text.find(END)
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
        # COMMENTS BLANKED ONCE, HERE, FOR EVERY SCANNER BELOW. This bug has now appeared three
        # times: the dispute scanner read the harness's own prose about run.dispute() as a call;
        # ci_gate_coverage computed compiles_only from un-stripped text; and the new arity scanner
        # read a comment explaining the dispute fix as a zero-argument run.dispute(). Each was
        # fixed locally, which is why it kept coming back. Prose about a call is not a call, and
        # the place to establish that is once, before any scanner runs — not inside each one.
        # Offsets and line numbers are preserved (spaces, not deletion), so citations stay true.
        body_nc = _blank_line_comments(body)

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

        # 2b. DISPUTE RECORD SHAPE. Method names were guarded; argument KEYS were not, which is
        # exactly how five scripts shipped run.dispute({layer,target,detail,severity}) — four keys
        # the owner never reads, so every field took its default and finding_id became '?'. It ran
        # live before anyone noticed, because a wrong key is not a syntax error and the record still
        # serialises. tests/valoria/test_wf_harness.py could not have caught it: it exercises the
        # harness with correct keys, so it verifies the contract while every caller violated it.
        for lineno, keys in _dispute_calls(body_nc):
            unknown = [k for k in keys if k not in dispute_legal]
            if unknown:
                violations.append((rel, lineno,
                                   f"run.dispute() is passed key(s) {sorted(unknown)}, which "
                                   f"tools/wf_harness.js does not read. Legal keys: "
                                   f"{sorted(dispute_legal)}. An unread key is not an error at run "
                                   f"time — the field silently takes its default and the dispute "
                                   f"records nothing. Use hVerdictDispute(v, '<critic-label>', ...)."))
            for missing in sorted(dispute_required - set(keys)):
                violations.append((rel, lineno,
                                   f"run.dispute() omits `{missing}`. run.adjudicate() binds on it, "
                                   f"so this record can never receive a ruling and is guaranteed to "
                                   f"reach the return unadjudicated."))

        # 2c. ARITY, for every run.* method the owner defines. See _run_arities: fixing the dispute
        # shape without generalising left the same defect live on run.critiqued in all five wave
        # scripts. A JS call with too few arguments is not an error — the missing parameter is
        # `undefined`, the guard's comparison quietly goes false, and the signal never fires.
        for meth, want in sorted(run_arities.items()):
            for lineno, got in _run_calls(body_nc, meth):
                if got < want:
                    violations.append((rel, lineno,
                                       f"run.{meth}() called with {got} argument(s); "
                                       f"tools/wf_harness.js declares {want}. The missing "
                                       f"parameter(s) are `undefined` at run time, which does not "
                                       f"throw — it silently disables whatever they control."))

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
