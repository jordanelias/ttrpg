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

# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

ROOT = ci_common.REPO

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

    # ── THE ARCHIVES, added 2026-08-12 (ED-IN-0165) ──────────────────────────
    # ARCHIVING AN ENTRY USED TO REMOVE ITS CLAIMS FROM THIS GATE FOREVER, and
    # nothing said so. `LEDGERS` named only the two LIVE lane files, so the moment
    # a settled id moved to its archive sibling — which is now ROUTINE, four times
    # in three commits, because the 50,000-token cap forces it — every measured
    # number in that entry stopped being checked. The gate reported OK on a
    # shrinking population, which is this repo's signature defect class (§1.6,
    # ED-IN-0149) sitting inside the gate built to stop claims going unverified.
    #
    # Found by an adversarial pass on the branch that CAUSED it: archiving
    # ED-IN-0160/0161 to make room under the cap moved this branch's own headline
    # measurements out of scope, and the gate's entry count dropped 23 -> 22
    # between origin/main and HEAD while still reporting green.
    #
    # MEASURED, NOT PREDICTED: scope goes 22 -> 47 entries across 4 ledgers, and
    # the gate STAYS GREEN — every one of the 25 recovered entries already names
    # an instrument. The coverage was free and had simply never been claimed.
    #
    # Same cutover ids as the live files: an archived entry is the same entry, and
    # its id decides whether the rule binds. Guard: tests/valoria/test_claim_provenance_archives.py.
    "registers/editorial_ledger_in_archive.jsonl": "ED-IN-0087",
    "registers/editorial_ledger_pc_archive.jsonl": "ED-PC-0040",

    # ── THE DEEP ARCHIVE, added 2026-09-17 (ED-IN-0245) ──────────────────────
    # Same rule, one store further down. Jordan ruled the live lane ledger is an
    # INDEX OF OPEN WORK, not a history: pre-current-month and terminal-status rows
    # leave it even when their bodies read as current. They land in
    # `registers/archive/` as frozen YAML fragments, and without this entry every
    # one of them would leave this gate's scope the moment it was archived --
    # which is precisely what ED-IN-0165 was written to prevent one store up.
    # Cutover ids are the live files': an archived entry is the same entry.
    "registers/archive/editorial_ledger_in_archive_pre-2026-09.yaml": "ED-IN-0087",
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



# Hidden quarantine trees, as (old_prefix, new_prefix) pairs. THE TWO HAVE DIFFERENT SHAPES and
# conflating them is a real bug, not a tidiness point: `.designs/` PREPENDS to the original path
# (`systems/x.md` -> `.designs/systems/x.md`, because the documents were gathered from several
# trees), while `.audit/` REPLACES a prefix (`audit/x.py` -> `.audit/x.py`, because that tree was
# renamed whole). A single "prepend the prefix" rule silently produces `.audit/audit/x.py`, which
# never exists, so every affected claim reads as a violation while looking like it was handled.
QUARANTINE_MIRRORS = (('', '.designs/'), ('audit/', '.audit/'))


def _quarantined_paths(target):
    """Where `target` would live if it had been moved into a quarantine tree."""
    for old, new in QUARANTINE_MIRRORS:
        if target.startswith(old):
            yield new + target[len(old):]


def _resolves_through_restructure_ledger(target):
    """True if `references/restructure_ledger.md` has an EXACT row retiring `target`.

    EXACT ROWS ONLY, AND THAT IS THE WHOLE CORRECTNESS ARGUMENT. The first version of this
    helper (2026-08-21, same day) called `pathres.resolve()` and accepted any status other than
    DEAD. `pathres` matches DIRECTORY PREFIXES (`pathres.py:187-194`), and the ledger carries 162
    directory-prefix `FORK:` rows — `tools/observability/`, `tools/sim_harness/`, `dashboard/`,
    `deprecated/`, `arcs/`, ~70 `audit/<unit>/` and more. A `FORK:` target has no existence check
    and cannot have one, because the content is at a ref. So that version made
    `MEASURED-BY: tools/observability/never_existed.py` resolve FORKED and PASS.

    That is fabrication passing an anti-fabrication gate, across 162 whole namespaces, and it
    looked exactly like a fix. Caught by an adversarial read-only pass the same day; reproduced
    before fixing:

        tools/observability/never_existed.py  -> FORKED   (should have been a violation)
        tools/sim_harness/totally_made_up.py  -> FORKED   (should have been a violation)

    Requiring an exact row restores the property: a retired instrument is recorded BY NAME, so a
    made-up filename under a retired directory has no row and still violates. Retiring a tool
    therefore costs one ledger line — which is the correct price, and the reason the ledger's own
    header says rows are exact.

    Deliberately does NOT delegate to `pathres.resolve()`: that function answers "does this point
    anywhere", and this gate is asking a narrower question — "is THIS FILE recorded as retired".
    It uses `pathres.load_alias_map()`, so the ledger is still parsed by its single owner and this
    is not a fifth parser. Degrades to False (still a violation) if pathres is unavailable, so an
    import failure can never silently green the gate.
    """
    try:
        import sys as _sys
        _sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import pathres
        exact, _prefix_rows_deliberately_ignored = pathres.load_alias_map()
        return target in exact
    except Exception:
        return False

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
    """JSONL lane ledger, or a frozen YAML fragment under `registers/archive/`.

    ⚠ THE YAML ARM WAS ADDED 2026-09-17 (ED-IN-0245) AND IT CLOSES THE SAME HOLE
    `ED-IN-0165` CLOSED FOR THE `_archive.jsonl` SIBLINGS. Jordan ruled that anything
    pre-dating the current month, and anything carrying a terminal status, leaves the
    live lane ledger. The deep store for that is `registers/archive/` -- uncapped
    (`atomization_rules`: `on_exceed: skip`) and globbed by `validate_ed_citations.py`,
    so ids keep resolving. But this gate's `LEDGERS` is a JSONL path map, so the first
    pass of that archival took 29 entries OUT OF SCOPE and the gate's coverage fell
    47 -> 18 WHILE STILL REPORTING GREEN -- the exact defect `ED-IN-0165` names, and
    `tests/valoria/test_claim_provenance_archives.py` caught it within the hour.
    Reading the fragments here means archiving can no longer shrink this gate's
    population, whichever store it moves to."""
    out = []
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        return out
    if path.endswith((".yaml", ".yml")):
        try:                                              # `ci_common.load_yaml` is the intended
            doc = ci_common.load_yaml(full, default={}) or {}  # owner of YAML register load (§8);
        except Exception as e:                            # loading it bare here would raise the
                                                          # shrink-only residual that
                                                          # test_ci_common_primitives ratchets.
            print(f"  [ERROR] {path} is not valid YAML ({e})")   # A malformed fragment is
            return out                               # REPORTED, never silently skipped:
                                                     # silence is how scope shrinks unseen.
        entries = doc.get("entries") if isinstance(doc, dict) else doc
        for i, entry in enumerate(entries or [], 1):
            if isinstance(entry, dict):
                out.append((i, entry))
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
            # `measured_by` added 2026-08-02 (ED-IN-0122). The gate that demands an instrument
            # could not see the field literally named for the instrument — it failed ED-IN-0122's
            # own entry, whose MEASURED-BY marker sat in `measured_by`, and the "fix" was to move
            # the marker into `description`. That treated the symptom: a provenance field the
            # provenance gate cannot read is a silent-pass trap in the other direction too, since
            # an entry whose numbers live in `measured_by` was never even scanned for claims.
            # MEASURED before widening (the expected-delta test this needed): scope 23 -> 25
            # entries, violations 0 -> 0, NEW violations 0. No backlog imported.
            blob = " ".join(str(entry.get(k, ""))
                            for k in ("description", "provenance", "measured_by"))
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
                if os.path.exists(os.path.join(ROOT, target)):
                    continue
                # QUARANTINE MIRRORS ARE AN EXISTENCE CHECK, NOT AN ALIAS RULE (2026-09-16,
                # ED-IN-0231). `.designs/` and `.audit/` mirror the tree exactly — an archived path
                # is the original with one prefix — so an instrument that moved into one is still
                # ON DISK and the claim is still re-runnable, which is the only question this gate
                # asks. This is deliberately NOT the ledger branch below: it proves the file is
                # there rather than that a row says it went somewhere, so a fabricated path fails
                # here exactly as it did before. That distinction is the whole correctness argument
                # of `_resolves_through_restructure_ledger`, and widening THAT to prefixes is what
                # `test_a_fabricated_path_under_a_forked_directory_still_violates` exists to stop.
                if any(os.path.exists(os.path.join(ROOT, c)) for c in _quarantined_paths(target)):
                    continue
                # RETIRED INSTRUMENTS RESOLVE, THEY DO NOT VIOLATE (2026-08-21, ED-IN-0194).
                #
                # Culling waves 1-3 retired 42 apparatus files, and 24 historical MEASURED-BY
                # markers cite one of them. Those claims were TRUE and their instrument still
                # exists — at the ref `references/restructure_ledger.md` records — so "the claim
                # cannot be re-run" is false for them: it can, from that ref. Failing here would
                # have forced a choice between rewriting 24 settled ledger rows and narrowing this
                # gate, and both destroy evidence to satisfy a checker.
                #
                # The resolver is the SANCTIONED one and is not re-implemented here:
                # `tools/pathres.py` is the declared sole parser of the restructure ledger, and
                # `broken_dependency_checker.py` already treats a `FORK:<ref>` target as resolved.
                # A marker naming a path with NO ledger row still violates, exactly as before —
                # this widens the gate to the retirement mechanism, not to absence.
                if _resolves_through_restructure_ledger(target):
                    continue
                violations.append(
                    (ledger, lineno, entry.get("id", "?"),
                     f"cites `MEASURED-BY: {ref}` but {target} does not exist in the tree and no "
                     f"references/restructure_ledger.md row retires it — the claim cannot be "
                     f"re-run, which is the whole point of the marker."))

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
