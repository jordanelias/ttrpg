#!/usr/bin/env python3
"""Claim-provenance gate — a MEASURED claim in a ledger entry must name a re-runnable source (ED-PC-0040).

WHY THIS EXISTS. The PC-lane four-dimension audit's remediation arc returned HALF-STANDS from adversarial review
three batches running. The meta-review found one recurring cause, and it was not subtle physics: quantitative claims
were written into ledger entries faster than they were measured, and the scripts that would have falsified them were
ad-hoc and discarded. Three that shipped:

  · ED-PC-0038: "spear/yari/estoc -> 0" damage at plate. The estoc is the MOST decisive plate weapon in the roster
    (99% of its plate fights settled, mean 12.84 per strike). Nobody had measured the estoc.
  · ED-PC-0039: "capability clears the tier BY CONSTRUCTION" about a weapon whose realized in-fight capability is
    0.60 against a 0.72 threshold — contradicted by a sweep in the same commit.
  · ED-PC-0038: mail was "a tier the fix was never meant to touch". It moved the odachi 23 points.

Each was caught by an expensive `fable`-tier adversarial review, batches after it shipped, and each was trivially
falsifiable by a two-minute script. THE RULE THIS GATE ENFORCES: if a ledger entry makes a measured claim, it must
name the instrument that produced it, and that instrument must exist in the tree so the claim can be re-run.

WHAT IT DOES NOT DO. It cannot check that a number is CORRECT — only that a source is named and present. That is a
real limit, and the same limit CLAUDE.md §7 records for the anti-fabrication gate: it narrows the surface, it does
not close it. A reviewer still has to run the thing. What it removes is the specific failure of a confident
quantitative claim with no way to check it at all.

FORWARD-LOOKING BY DESIGN, AND THE CUTOVER IS AN ID NOT A DATE. Only entries from CUTOVER_ID onward are checked. A
date cutover was tried first and was wrong: every entry in the failing arc (ED-PC-0034..0039) carries the SAME date
as the entry that establishes this rule, so a date either exempts the new rule from itself or demands mass-editing an
append-only ledger. An ID cutover starts the discipline at exactly the entry that creates it — ED-PC-0040 is the
first entry the gate holds to its own standard.

The five grandfathered entries are NOT quietly excused: ED-PC-0040 retracts their false claims in the ledger, and the
audit infill records what measurement actually says. Grandfathering here means "not re-litigated by a linter", not
"not corrected".

Usage:  python tools/ci_claim_provenance_check.py [--staged]
Exit 1 on violation.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ledgers under the rule, each with the FIRST entry id the rule binds on (see FORWARD-LOOKING above). Scoped to the
# lane that generated the failure; widen deliberately, lane by lane, once each lane has a measurement instrument to
# point at — a rule nobody can satisfy is a rule that gets bypassed.
LEDGERS = {
    "registers/editorial_ledger_pc.jsonl": "ED-PC-0040",
    # IN lane added 2026-07-28 (ED-IN-0087), taking this file's own widening instruction at its word:
    # "widen deliberately, lane by lane, once each lane has a measurement instrument to point at."
    # The IN lane now has one — tools/ci_claude_workflow_paths.py, written for ED-IN-0085 precisely
    # because that entry's headline was hand-counted and wrong by an order of magnitude. Same failure
    # this gate was built for, different lane, so the same rule applies.
    #
    # Cutover follows the PC precedent exactly: an ID, not a date, starting at the entry that adopts
    # the rule. ED-IN-0087 is the first IN entry held to it. ED-IN-0085 is grandfathered in the
    # linter's sense only — it names its instrument in prose, and its wrong numbers were retracted in
    # its own successor rather than left standing.
    "registers/editorial_ledger_in.jsonl": "ED-IN-0087",
}

# The marker an entry uses to name its instrument.
#
# The trailing-punctuation strip is not cosmetic. `[^\s;,)]+` already excludes `;` `,` `)`, but a
# marker at the END OF A SENTENCE — "…re-run. MEASURED-BY: tools/x.py." — captured the period into
# the path and failed with "tools/x.py. does not exist", which reads as a missing instrument when
# the instrument is right there. Caught by this gate firing on ED-IN-0087's own entry. No filename
# in this tree ends in `.` or `:`, so stripping them can only ever remove prose punctuation.
MARKER = re.compile(r"MEASURED-BY:\s*([^\s;,)]+)")
_TRAILING_PROSE = ".:"

# Claim shapes that make an entry "quantitative". Deliberately narrow — these are the shapes the three historical
# misses actually took (a transition, a per-sample rate, a delta in points, a sample size), not "contains a digit".
CLAIM_PATTERNS = [
    (re.compile(r"\b\d+(?:\.\d+)?\s*(?:->|→)\s*\d+(?:\.\d+)?"), "a measured transition (x -> y)"),
    (re.compile(r"\bn\s*=\s*\d{2,}"), "a sample size (n=...)"),
    (re.compile(r"[-+]?\d+(?:\.\d+)?\s*pp\b"), "a delta in percentage points"),
    (re.compile(r"\bmean\s+\d+(?:\.\d+)?"), "a reported mean"),
    (re.compile(r"\bdecide[sd]?\s+~?\d+(?:\.\d+)?%"), "a reported decided-rate"),
]


_ED_ID = re.compile(r"^(ED-[A-Z]+)-(\d+)$")


def _is_pre_cutover(entry_id, cutover_id):
    """True when `entry_id` predates `cutover_id` and is therefore grandfathered.

    This used to be a plain string `<`, with the comment "zero-padded ED-<LANE>-NNNN ids compare
    correctly as strings within a lane". That holds for the PC lane, whose ids are uniformly
    ED-PC-NNNN — but it silently breaks on any lane carrying a second id shape. The IN lane does:
    alongside ED-IN-NNNN it holds ED-IN-REMEDIATION-NNNN, and since 'R' (82) > '0' (48), every one
    of those sorted AFTER the cutover and got dragged into the gate (ED-IN-0087 exposed this while
    widening the rule to the IN lane).

    The fix compares the lane prefix and the sequence number, not the raw string:
      · different lane, or an id that isn't ED-<LANE>-<digits> at all → not in the cutover's
        sequence, so grandfathered. A gate should not hold an entry to a rule keyed on a
        numbering scheme that entry never used.
      · same lane → numeric comparison, which is what "from this entry onward" actually means.
    """
    m_entry, m_cut = _ED_ID.match(entry_id), _ED_ID.match(cutover_id)
    if not m_cut:                      # malformed cutover: fall back to the old behaviour
        return entry_id < cutover_id
    if not m_entry:                    # e.g. ED-IN-REMEDIATION-0064 — a different scheme
        return True
    if m_entry.group(1) != m_cut.group(1):   # different lane in a shared file
        return True
    return int(m_entry.group(2)) < int(m_cut.group(2))


def _load(path):
    out = []
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        return out
    with open(full, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                out.append((i, json.loads(line)))
            except json.JSONDecodeError as e:
                print(f"  [ERROR] {path}:{i} is not valid JSON ({e})")
    return out


def _staged_paths():
    try:
        r = subprocess.run(["git", "diff", "--cached", "--name-only"],
                           cwd=ROOT, capture_output=True, text=True, check=True)
        return set(r.stdout.split())
    except Exception:
        return set()


def check(staged_only=False):
    staged = _staged_paths() if staged_only else None
    violations = []
    checked = 0

    for ledger, cutover_id in LEDGERS.items():
        if staged is not None and ledger not in staged:
            continue
        for lineno, entry in _load(ledger):
            if _is_pre_cutover(str(entry.get("id", "")), cutover_id):
                continue
            blob = " ".join(str(entry.get(k, "")) for k in ("description", "provenance"))
            claims = [why for pat, why in CLAIM_PATTERNS if pat.search(blob)]
            if not claims:
                continue
            checked += 1
            found = MARKER.findall(blob)
            if not found:
                violations.append(
                    (ledger, lineno, entry.get("id", "?"),
                     f"makes quantitative claims ({'; '.join(claims)}) but names no instrument. "
                     f"Add `MEASURED-BY: <path>` naming a re-runnable script that reproduces the numbers."))
                continue
            for ref in found:
                target = ref.rstrip(_TRAILING_PROSE).split("::")[0]
                if not os.path.exists(os.path.join(ROOT, target)):
                    violations.append(
                        (ledger, lineno, entry.get("id", "?"),
                         f"cites `MEASURED-BY: {ref}` but {target} does not exist in the tree — the claim cannot "
                         f"be re-run, which is the whole point of the marker."))

    print(f"[claim-provenance] {checked} quantitative entr(y/ies) in scope across {len(LEDGERS)} ledger(s) "
          f"(cutovers: {', '.join(sorted(LEDGERS.values()))})")
    if violations:
        print(f"[claim-provenance ✗] {len(violations)} violation(s):")
        for ledger, lineno, eid, msg in violations:
            print(f"  {ledger}:{lineno}  {eid}: {msg}")
        print("\n  Rule (ED-PC-0040): a ledger entry that states measured numbers must name the instrument that")
        print("  produced them, and that instrument must be in the tree. This gate exists because three consecutive")
        print("  batches shipped confident numbers that measurement later contradicted.")
        return 1
    print("[claim-provenance ✓] every quantitative entry names an instrument that exists")
    return 0


if __name__ == "__main__":
    sys.exit(check(staged_only="--staged" in sys.argv))
