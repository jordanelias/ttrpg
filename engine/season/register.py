"""THE HOLE REGISTER, AS AN OBJECT -- `W0` of `architecture/PLAN.md`.

`ARCHITECTURE_V2.md` §0.3 row 13 claims Part VII is *"rows, not prose"*. IT WAS A MARKDOWN TABLE
THAT NOTHING READ. Not one of its 32 rows carried the `site:`, `sweep:` or `cite:` fields its own
§G4 defines; its self-reported counts (39 holes · 8 ruled · 13 assumption · 12 absent · 1 mixed)
do not reproduce from its own rows; and it could not report that TWENTY-TWO holes had no row at
all. By `CLAUDE.md` §0.05's test -- *would the game behave differently if this document were
deleted?* -- it was reference. `hole_register.yaml` is the object; this module is the only thing
that reads it.

WHAT THIS MODULE IS FOR, STATED SO IT IS NOT MISTAKEN FOR A REPOSITORY GUARD. It lives inside the
instrument directory and nowhere else (`PLAN.md` §7, guardrail `G9`). It grades no repository
signal, aggregates no verdict, and has no CI job. It exists because an instrument that fills a
hole must be able to ASK whether that hole is fillable, and a markdown table cannot be asked.

    python register.py --counts                 # the tallies, computed, never typed
    python register.py --check                  # every rule; exit 1 on any violation
    python register.py --check --rule R0,R1,R2,R3

THE RULES, each with the failure that earned it:

  R0  SHAPE          a row carries exactly the twelve declared keys, ids are unique, tier is 0|1.
                     Earned by: §G4 defines ten fields and V2's rows carried seven. A shape that
                     is not checked is a shape that grows.
  R1  GRADED         every row's grade is one of ruled|measured|assumption|absent.
                     Earned by: §42.2's polarity rule -- *a row with no grade FAILS THE EXPORT*.
                     [`W0`]
  R2  INJECTABLE     an `assumption` row carries a `site:` and at least three `sweep:` points.
                     Earned by: §G's inject-declare-sweep doctrine is worthless if a default can
                     be declared without saying WHERE it enters or WHAT ELSE was tried. [`W0`]
  R3  REFUSAL        an `absent` row carries no `default:`.
                     Earned by: §42.2.1 in one line -- *the honest behaviour is to REFUSE, not to
                     pick a plausible number.* This is that sentence made mechanical. [`W0`]
  G6  LADDER RUN     an `absent` row carries a non-empty `cite:`.
                     Earned by: `PLAN.md` §2.6 -- NOBODY EVER RAN `CLAUDE.md` §0's five tests over
                     the twelve refusals, and run in chain eleven of twelve close or downgrade.
                     A refusal nobody argued for is not a refusal, it is an omission wearing one.
  G8  DISCHARGED     every Part B defect id appears in a row or in the discharge map, never both.
                     Earned by: `D16` was the ONLY one of 26 defects with no Part VII row and no
                     Part D-G discharge, and was claimed discharged anyway.
  G12 CITE AGREES    a row's `cite:` may not argue for a grade the row does not carry.
                     Earned by: `H-46`'s cite was written from neighbouring `H-20`'s and kept its
                     conclusion -- *"THIS ROW THEREFORE STAYS `assumption`"* -- on a row graded
                     `absent`. So it satisfied `G6` on an argument for a DIFFERENT refusal, and a
                     `tier: 0` row's grade feeds both artifact 0's verdict and, through
                     `resolve()`, the case verdicts. [`W10` adversarial pass]

⚠ `--check` EXITS 1 TODAY, ON G6, AND THAT IS THE MEASUREMENT RATHER THAN A BUG. `W0`'s stated
proof in `PLAN.md` is *"exits 0"*, and it cannot: the plan's own §1.5 finds that no row carries
`cite:` or `sweep:`, so a register that transcribes those rows faithfully MUST fail the rules that
read those fields. Writing 0 would have required backfilling citations nobody derived, which is
the exact laundering this register exists to stop. `W1` is the item that runs the ladder; the
honest reading of `W0` is that `R0`-`R3` and `G8` pass and `G6` reports its floor.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
ARCH_DIR = REPO_ROOT / "architecture"   # LAYER 1 doctrine; the YAML below is mechanism (§0.05)
REGISTER = HERE / "hole_register.yaml"
ARCHITECTURE_V2 = ARCH_DIR / "ARCHITECTURE_V2.md"

GRADES = ("ruled", "measured", "assumption", "absent")
# Strictest first. A row V2 grades in parts (H-02, H-20) takes the strictest grade present,
# because §42.2's polarity rule sends zero evidence to the verdict AGAINST the thing measured:
# a hole that is absent in part must refuse in part, and refusing is what a grade decides.
GRADE_STRICTNESS = ("absent", "assumption", "measured", "ruled")
FIELDS = ("id", "tier", "hole", "kind", "owner", "grade",
          "default", "site", "sweep", "unblocks", "cite", "source")
# ⚠ `sign` IS DECLARED OPTIONAL AND IS REQUIRED ON EXACTLY ONE KIND. `ID-16` — *a design
# enumerates its loops and signs each one* — and the register is where the enumeration lives,
# because every one of its nine existing kinds names an ABSENCE and a feedback path is not an
# absence. Optional rather than universal: `FIELDS` holds twelve names, so a mandatory `sign` would
# be the THIRTEENTH column, and it would force a meaningless cell onto the 98 rows that are not
# loops — a column that is meaningless on 98 rows is not read on any of them. ⚠ This comment read
# "a twelfth mandatory column … onto 91 rows" until 2026-09-04: off by one on the column (there are
# twelve already) and stale by eleven on the rows (the file held 91 when the column was proposed and
# holds 102 now). `:122` below had the arithmetic right and this line disagreed with it. ⚠ `G13` VALIDATES ITS SHAPE; NO RESOLVER READS IT. The first writing of this comment
# called G13 "the reader … which keeps this from being a column nobody consults (`ID-13`)", and
# that overstated it: `ID-13` speaks of a column no RESOLVER consults, and `§0.05`'s test decides
# it -- delete `sign` and the season loop is byte-identical. The column is SHAPE-VALIDATED
# REFERENCE. What would give it a reader in `ID-13`'s sense is the derived check (`H-106`).
OPTIONAL_FIELDS = ("sign",)
LOOP_KIND = "LOOP"
# `+` AMPLIFYING · `-` DAMPING. Two values and no third: a loop whose sign nobody can name is the
# finding `ID-16` exists to surface, and it is recorded as an `absent` row rather than as a
# question mark in this column.
LOOP_SIGNS = ("+", "-")
SWEEP_POINTS = 3
# Part B of ARCHITECTURE_V2.md carries D1..D26. The bound is re-derived from the document by
# `part_b_defects()` rather than pinned here; this is only the pattern.
# `§D4` is Part D SECTION 4 (travel is a Tenure alter); `D4` is Part B DEFECT 4 (budget's
# signature). Part D has only §D1-§D5, so the two namespaces collide exactly there, and V2
# spelled EIGHTEEN Part B ids with a leading `§` -- `W0` corrected those. The lookbehind is what
# keeps the surviving legitimate `§D1`-`§D5` section references out of the defect scan.
DEFECT_RE = re.compile(r"(?<!§)\bD([1-9]\d?)\b")
# A section reference in a discharge-map value: `§D4`, `§G4`, `§VII.2`, `Part E`.
SECTION_RE = re.compile(r"§[A-Z]*[0-9IVX]+(?:\.[0-9]+)?|Part [A-Z]+")
# The marker a row carries when it claims to have come from V2's tables; read by `counts()`.
TRANSCRIBED = "transcribed verbatim"
# THE HOLE-ID SHAPE, WITH ONE OWNER. `exercises.py` re-derived it as `H-\\d+` and the two
# disagreed at `H-100`: one classified it as a hole, the other refused it as malformed. CLAUDE.md
# §8 -- never re-implement a rule. Widened to 2-3 digits here because the register passed 99 rows
# during `W10` and the old shape would have started refusing ids the moment it did.
REG_ID_RE = r"H-\d{2,3}"


def normalised_default(cell: str) -> str:
    """⚠ `default:` MEANS TWO THINGS AND BOTH ARE DECLARED HERE. On an ordinary row it is *the
    value an instrument may inject*. On a `LOOP` row it is **what bounds the loop**, which is what
    `G13` clause 3 reads. A column with two meanings is `CLAUDE.md` §4's hazard, carried
    deliberately rather than by accident: a bound is a loop's analogue of a default, and a
    thirteenth column for four rows would put an empty cell on ninety-eight. **Say it here, or the
    next reader derives one meaning and misses the other.**

    ⚠ AND `G13` CLAUSE 3 IS A PRESENCE CHECK, NOT A BOUND CHECK: any non-`none` string passes, so
    `default: "TBD"` would satisfy it — one notch from the term-grep `ID-16`'s own first draft was
    indicted for. Left as a presence check on purpose; see the `G13` docstring.

    V2 writes an `absent` row's default as "none" FOLLOWED BY COMMENTARY -- "none. ⚠ every
    contest is blocked", "none — §63.1 may accept it instead". The field means *the value an
    instrument may inject*, and a warning is not a value, so it normalises to `none`. THIS IS THE
    ONE NORMALISATION APPLIED TO `default`, and it is declared here rather than in prose.

    ⚠ It is load-bearing on a published number: transcribed literally, H-23/H-25/H-31/H-32/H-33
    would each fire R3, and R3 would read 7 rather than 2."""
    cell = cell.strip()
    return "none" if re.match(r"^none\b", cell, re.I) else cell


def section_exists(sec: str) -> bool:
    """Does `ARCHITECTURE_V2.md` actually carry this section? A discharge naming a section that
    does not exist is the D16 failure with a new spelling."""
    src = ARCHITECTURE_V2.read_text()
    if sec.startswith("Part "):
        # V2 writes them `# PART E ...`; the map may say `Part E`.
        return bool(re.search(r"^# " + re.escape(sec) + r"\b", src, re.M | re.I))
    return bool(re.search(r"^#+ " + re.escape(sec) + r"\b", src, re.M))


def load(path: Path = REGISTER) -> dict:
    if not path.exists():
        raise SystemExit(f"register not found: {path}")
    return yaml.safe_load(path.read_text())


def grade_of(cell: str) -> str:
    """The strictest grade NAMED in a cell. Word-bounded, because a substring scan is a router
    and this module's own G8 docstring indicts one: `unmeasured` contains `measured`, `not ruled`
    contains `ruled`. No V2 cell trips it today, which makes it latent rather than safe."""
    for g in GRADE_STRICTNESS:
        if re.search(r"\b" + g + r"\b", cell, re.I):
            return g
    return ""


def part_b_defects() -> set:
    """Every `D<n>` id defined by Part B's own table -- read out of the document, not pinned as a
    range here. A defect added to Part B and to nothing else must fail `G8`, and it cannot if
    this function does not know it exists."""
    src = ARCHITECTURE_V2.read_text().splitlines()
    out, on = set(), False
    for ln in src:
        if ln.startswith("# PART B"):
            on = True
            continue
        if on and ln.startswith("# PART "):
            break
        if on and ln.startswith("| **D"):
            m = DEFECT_RE.search(ln.split("|")[1])
            if m:
                out.add("D" + m.group(1))
    return out


# ---------------------------------------------------------------------------
# THE RULES
# ---------------------------------------------------------------------------

def rule_R0(reg: dict) -> list:
    bad, seen = [], set()
    for r in reg["rows"]:
        extra = sorted(set(r) - set(FIELDS) - set(OPTIONAL_FIELDS))
        missing = sorted(set(FIELDS) - set(r))
        if extra:
            bad.append(f"{r.get('id','?')}: keys outside the declared shape: {extra}")
        if missing:
            bad.append(f"{r.get('id','?')}: missing declared keys: {missing}")
        if r.get("tier") not in (0, 1):
            bad.append(f"{r.get('id','?')}: tier is {r.get('tier')!r}, not 0 or 1")
        if r.get("id") in seen:
            bad.append(f"{r['id']}: duplicate id")
        seen.add(r.get("id"))
    return bad


def rule_R1(reg: dict) -> list:
    return [f"{r['id']}: grade is {r.get('grade')!r}, not one of {GRADES}"
            for r in reg["rows"] if r.get("grade") not in GRADES]


def rule_R2(reg: dict) -> list:
    bad = []
    for r in reg["rows"]:
        if r.get("grade") != "assumption":
            continue
        if not str(r.get("site") or "").strip():
            bad.append(f"{r['id']}: assumption with no `site:` -- where does the default enter?")
        sweep = r.get("sweep")
        if not isinstance(sweep, list):
            # `sweep: "TBD"` is three characters and passed a bare length test.
            bad.append(f"{r['id']}: sweep is {type(sweep).__name__}, not a list")
        elif len(sweep) < SWEEP_POINTS:
            bad.append(f"{r['id']}: assumption swept at {len(sweep)} points, "
                       f"needs {SWEEP_POINTS}")
        elif len({str(x) for x in sweep}) < SWEEP_POINTS:
            # A sweep is three points a verdict can differ ACROSS. [2, 2, 2] is one point,
            # written three times, and it would report "no verdict flipped" truthfully and
            # meaninglessly -- the dead-carrier shape §W5's guardrail names for `alignment`.
            bad.append(f"{r['id']}: sweep {sweep} has fewer than {SWEEP_POINTS} DISTINCT points")
    return bad


def rule_R3(reg: dict) -> list:
    return [f"{r['id']}: `absent` row carries a default ({r['default']!r}) -- §42.2.1 says REFUSE"
            for r in reg["rows"]
            if r.get("grade") == "absent"
            and str(r.get("default") or "").strip().lower() not in ("", "none")]


def rule_G6(reg: dict) -> list:
    return [f"{r['id']}: `absent` with an empty `cite:` -- §0's five tests were never run on it"
            for r in reg["rows"]
            if r.get("grade") == "absent" and not str(r.get("cite") or "").strip()]


def rule_G12(reg: dict) -> list:
    """A row's `cite:` may not argue for a grade the row does not carry.

    ⚠ THIS IS A REAL DEFECT CLASS AND IT SHIPPED. `H-46`'s cite was written from `H-20`'s -- they
    are neighbouring questions about the same roster -- and carried `H-20`'s conclusion verbatim:
    *"THIS ROW THEREFORE STAYS `assumption`"*, on a row graded `absent`. So `H-46` satisfied `G6`
    (*"a refusal nobody argued for is not a refusal"*) on an argument for a DIFFERENT REFUSAL, and
    `G6`'s whole purpose leaked. It matters beyond bookkeeping: `H-46` is `tier: 0`, so it sits
    inside `tier0_absent` and artifact 0's verdict, and `resolve()` turns a row's grade into a case
    verdict -- a wrong grade with a plausible-looking cite is exactly how a wrong verdict survives
    review. `CLAUDE.md` §0.1 pt 5: the defective artifact is load-bearing on the game-facing
    verdict, so the pattern earns a guard. Found by `W10`'s adversarial pass."""
    import re as _re
    bad = []
    for r in reg["rows"]:
        cite = str(r.get("cite") or "")
        for g in ("ruled", "assumption", "absent", "measured"):
            if r.get("grade") == g:
                continue
            # ⚠ SCOPED TO A CLAIM ABOUT **THIS** ROW. The pattern was any occurrence of
            # `STAYS <grade>`, and it fired on `H-55`, whose cite legitimately says *"`H-33` stays
            # `assumption`"* -- a CROSS-REFERENCE to a different row, on a row graded `measured`.
            # A guard that reddens correct prose pushes the fix toward mangling the prose, and
            # `PLAN.md` `G4` weighs that equally with an invention. `THIS ROW` is the shape the
            # real defect had (`H-46` carried `H-20`'s *"THIS ROW THEREFORE STAYS `assumption`"*
            # verbatim), so requiring it keeps the catch and drops the false positive.
            if _re.search(r"THIS ROW[^.]{0,80}?STAYS\s+`?%s`?" % g, cite, _re.I):
                bad.append(f"{r['id']}: graded `{r.get('grade')}` and its `cite:` argues it "
                           f"STAYS `{g}` -- one of the two is wrong")
    return bad


def rule_G8(reg: dict) -> list:
    """Every Part B defect binds to a register row or to a named section, EXPLICITLY. The first
    draft inferred the binding by scanning row text for a defect id, which is a keyword search --
    a router, and §7.4 is the sixth recurrence of what routers do. It also could not tell Part D
    SECTION `§D4` from Part B DEFECT `D4`, the two namespaces V2 had collided."""
    defects = part_b_defects()
    if not defects:
        return ["Part B parsed to ZERO defect ids -- the check cannot run, which is a FAILURE and "
                "not a pass (§42.2's polarity rule, applied to this module)"]
    mapped = reg.get("discharges") or {}
    ids = {r["id"] for r in reg["rows"]}
    bad = []
    for d in sorted(defects, key=lambda x: int(x[1:])):
        target = mapped.get(d)
        if not target:
            bad.append(f"{d}: Part B defines it and the discharge map has no entry")
            continue
        target = str(target)
        if target.startswith("row:"):
            row = target[4:]
            if row not in ids:
                bad.append(f"{d}: discharged to {row}, which is not a row in this register")
        else:
            # THE SECTION BRANCH MUST RESOLVE, or G8 reproduces the exact failure it was built to
            # stop. `D16: "§D9"` -- a section Part D does not have -- passed the first draft, and
            # D16 was once again "claimed discharged anyway".
            unresolved = [sec for sec in SECTION_RE.findall(target)
                          if not section_exists(sec)]
            if not SECTION_RE.search(target):
                bad.append(f"{d}: discharged to {target!r}, which names no section and no row")
            elif unresolved:
                bad.append(f"{d}: discharged to section(s) {unresolved} that do not exist in "
                           "ARCHITECTURE_V2.md -- the D16 failure, exactly")
    for d in sorted(set(mapped) - defects, key=lambda x: int(x[1:]) if x[1:].isdigit() else 0):
        bad.append(f"{d}: in the discharge map and Part B does not define it")
    return bad


def rule_G13(reg: dict) -> list:
    """`ID-16`: a design enumerates its loops and SIGNS each one — and the sign is read here.

    ⚠ **THIS GATE VALIDATES THE COLUMN'S SHAPE. IT DOES NOT MAKE IT A MECHANISM, AND THE FIRST
    WRITING OF THIS DOCSTRING SAID IT DID.** No resolver consults `sign`: delete the column and the
    season loop is byte-identical, which is `§0.05`'s own test. What this gate buys is that a
    declared loop cannot be declared badly — worth having, and a smaller claim than the one it
    replaced. **The reader that would satisfy `ID-13` is the derived check (`H-106`), unbuilt.**
    Three clauses, and the third is the one with teeth:

      1. a `LOOP` row carries a `sign`, and it is `+` or `-`. A feedback path whose direction
         nobody will state is not enumerated, it is merely mentioned.
      2. a row of any OTHER kind carries no `sign`. The column means one thing.
      3. **an amplifying loop must name what bounds it**, in `default:` — ⚠ **a PRESENCE check:
         any non-`none` string passes.** Hardening it into a real bound check would need this
         module to import the fixtures, and the column is reference either way (`§0.1` pt 5: a
         stronger checker over a non-load-bearing artifact guards nothing). Saying so was the
         fix; building it was not. A `+` loop with no bound
         is a spiral, which is `F.28` — *nothing bounds a spiral across seasons* — and the whole
         reason `ID-16` says a design of nothing but damping converges is that the two failures
         are opposite and a design can have both. A `-` loop needs no such cell; convergence is
         not a crash.

    ⚠ **AND IT DOES NOT CHECK THAT THE ENUMERATION IS COMPLETE, WHICH IS THE HALF THAT IS STILL
    ABSENT.** Completeness needs the cycle set computed from **what is written** × **every typed
    reader** — the question sources and the channel predicates as much as a verb's `requires`,
    since the write edge on every declared loop belongs to a STEP rather than to a verb. **`H-106`
    is that row** (not `H-102`, which is the propagation loop; the first writing of this docstring
    named the wrong one). This gate checks every loop somebody declared; it cannot see one nobody
    did — which is how `H-112` went unrecorded until an audit read `World.write`."""
    bad = []
    for r in reg["rows"]:
        sign, kind = r.get("sign"), str(r.get("kind") or "")
        if kind == LOOP_KIND:
            if sign not in LOOP_SIGNS:
                bad.append(f"{r.get('id','?')}: kind is LOOP and sign is {sign!r}, "
                           f"not one of {list(LOOP_SIGNS)}")
            elif sign == "+" and normalised_default(str(r.get("default") or "")) == "none":
                bad.append(f"{r.get('id','?')}: an amplifying loop with no bound in `default:` "
                           "-- that is a spiral, and F.28 is the row that says nothing catches one")
        elif sign is not None:
            bad.append(f"{r.get('id','?')}: carries `sign` on a {kind or 'kind-less'} row; "
                       "the column belongs to LOOP rows only")
    return bad


RULES = {"R0": rule_R0, "R1": rule_R1, "R2": rule_R2,
         "R3": rule_R3, "G6": rule_G6, "G8": rule_G8, "G12": rule_G12,
         "G13": rule_G13}


def check(reg: dict, only: list | None = None) -> dict:
    return {k: fn(reg) for k, fn in RULES.items() if not only or k in only}


# ---------------------------------------------------------------------------
# THE COUNTS -- computed, never typed. `G11`.
# ---------------------------------------------------------------------------

def _source_bucket(source: str) -> str:
    """A row's attribution: the text before the first em-dash, normalised. `source:` is prose
    after that point and must not decide which bucket a row falls in."""
    head = source.split("\u2014")[0].split("|")[0].strip()
    if TRANSCRIBED in source and head.startswith("ARCHITECTURE_V2.md"):
        return TRANSCRIBED
    if head.startswith("PLAN.md"):
        return "PLAN.md §1.4"
    return head or "unattributed"


def counts(reg: dict) -> dict:
    rows = reg["rows"]
    by_grade = Counter(r.get("grade") for r in rows)
    return {
        "rows": len(rows),
        "by_grade": dict(sorted(by_grade.items())),
        "tier0": sum(1 for r in rows if r.get("tier") == 0),
        "tier1": sum(1 for r in rows if r.get("tier") == 1),
        "tier0_absent": sorted(r["id"] for r in rows
                               if r.get("tier") == 0 and r.get("grade") == "absent"),
        "transcribed": sum(1 for r in rows if TRANSCRIBED in str(r.get("source"))),
        "added_by_plan": sum(1 for r in rows if "PLAN.md" in str(r.get("source"))),
        # ⚠ THE TWO BUCKETS ABOVE STOPPED PARTITIONING THE REGISTER THE MOMENT `W5` ADDED ROWS
        # FROM A THIRD SOURCE, and the header line went on printing "32 + 27" over 64 rows --
        # an arithmetic claim nobody would have re-added. `by_source` is derived from the data
        # rather than from two hardcoded predicates, and `--check` asserts it sums to `rows`, so
        # a fourth source cannot silently fall out of the total again.
        # Bucketed on the ATTRIBUTION PREFIX -- the text before the first em-dash -- not on a
        # substring of the whole cell. The first version matched "PLAN.md" anywhere and put
        # `H-66` (source: "W5 - ... a hole PLAN.md §1.4 named") in the PLAN bucket, so a row's
        # own prose could change its attribution.
        "by_source": dict(sorted(Counter(
            _source_bucket(str(r.get("source", ""))) for r in rows).items())),
        # The register's own header states how many rows carry an empty `cite:`. A number a
        # document states and its named command cannot produce is G11's defect in miniature, and
        # it was in the file that forbids it nine lines above.
        "absent_uncited": sum(1 for r in rows if r.get("grade") == "absent"
                              and not str(r.get("cite") or "").strip()),
    }


SOURCE_353 = ARCH_DIR / "holonic_ARCHITECTURE.md"
REPO = REPO_ROOT
# A `cite:` may quote MORE THAN #353. The first version of this gate checked every quote against
# #353 alone and reported ten legitimate quotations of V2, PLAN.md, CLAUDE.md and a live engine
# module as FABRICATED -- the same false-positive class as comparing typography instead of prose,
# one level up. A quote must now be found in AT LEAST ONE source the cite NAMES, and a cite that
# names no resolvable source verifies nothing.
CITE_SOURCES = {
    "#353": SOURCE_353,
    "ARCHITECTURE_V2": ARCHITECTURE_V2,
    "V2": ARCHITECTURE_V2,
    "PLAN.md": ARCH_DIR / "PLAN.md",
    "PLAN §": ARCH_DIR / "PLAN.md",
    "CLAUDE.md": REPO / "CLAUDE.md",
}
# Any repo-relative path the cite mentions, e.g. `engine/autoload/dice_engine.py`.
PATH_RE = re.compile(r"\b((?:[\w.-]+/)+[\w.-]+\.(?:py|md|ya?ml|json))\b")
LINEREF_RE = re.compile(r":(\d{2,4})(?:-(\d{2,4}))?\b")
# A quoted span long enough to be a claim rather than a term. `cite:` is free text, so this
# finds the quotes an author actually wrote rather than requiring a format.
QUOTE_RE = re.compile(r'"([^"]{25,})"')


def _cite_norm(text: str) -> str:
    """Compare PROSE, not typography. #353 is markdown: the sentence a row quotes arrives wrapped
    across lines, inside a blockquote, with `**emphasis**` mid-clause and an em-dash where a cite
    typed two hyphens. None of that is part of the claim, and a matcher that fails on it reports a
    verified citation as FABRICATED -- which is exactly what the first version of this function
    did to all eight of them."""
    text = re.sub(r"[*`]", "", text)                    # markdown emphasis and code spans
    text = re.sub(r"^\s*>+\s*", "", text)               # blockquote markers
    text = re.sub(r"^\s*[-*+]\s+", "", text)            # list markers
    text = text.replace("\u2014", "-").replace("\u2013", "-")   # em / en dash
    text = re.sub(r"[\u201c\u201d\u2018\u2019'\"]", "'", text)     # every quote mark, one form
    text = re.sub(r"-{2,}", "-", text)                  # `--` typed for an em dash
    # CASE-FOLDED. A citer who SHOUTS the clause that matters has not changed the claim, and the
    # first version of this gate reported five hand-verified quotes as FABRICATED for exactly
    # that -- the same class of false positive as comparing typography instead of prose.
    return re.sub(r"\s+", " ", text).strip().lower()


def _contains(hay: str, needle: str) -> bool:
    """An elided quote (`... `) matches when every fragment is present, in order. Eliding the
    middle of a long sentence is normal citation practice; treating it as a mismatch would push
    an author toward quoting less precisely, not more."""
    pos = 0
    for frag in [f.strip() for f in needle.split("...") if f.strip()]:
        i = hay.find(frag, pos)
        if i < 0:
            return False
        pos = i + len(frag)
    return True


def _rows_text_excluding(reg: dict, row: dict) -> str:
    """Every string field of every row EXCEPT `row`, normalised and joined — the haystack for a
    `cite:` that names this register as a source. See `verify_citations`: a row may not be its own
    evidence, and excluding it at the data level is the only way that cannot silently no-op."""
    parts: list = []
    for other in reg["rows"]:
        if other is row:
            continue
        for v in other.values():
            if isinstance(v, str):
                parts.append(v)
            elif isinstance(v, list):
                parts.extend(x for x in v if isinstance(x, str))
    return re.sub(r"\s+", " ", " ".join(_cite_norm(p) for p in parts))


def verify_citations(reg: dict) -> list:
    """EVERY `:NNN` A `cite:` NAMES MUST EXIST, AND EVERY VERBATIM QUOTE MUST BE THERE.

    `PLAN.md` PART 9 gives this as the falsifier for `W1`: *"a cited line that does not say what
    §3.1-§3.4 claims it says. Every citation is a file and a line; check them."* A closure resting
    on a line that does not say what the row claims is worse than an open hole, because the hole
    is visible and the false closure is not -- and `CLAUDE.md` §0 calls the anti-fabrication gate
    leaky and says to verify provenance BY HAND. This is that check, mechanised, so it does not
    depend on anyone remembering.

    A quote is matched with whitespace collapsed, because the source wraps mid-sentence and a
    citation should not fail on a line break. The window is +/-6 lines: a row citing `:929-930`
    for a sentence that begins at `:927` is imprecise, not fabricated, and this reports the
    difference rather than conflating them."""
    if not SOURCE_353.exists():
        return [f"#353 not found at {SOURCE_353} -- citations cannot be verified, which is a "
                "FAILURE and not a pass (§42.2's polarity rule)"]
    src = SOURCE_353.read_text().splitlines()
    flat = [_cite_norm(ln) for ln in src]
    bad, checked = [], 0

    def sources_named(cite: str) -> dict:
        """Every source this cite names and this checker can open. `#353` is implied by a bare
        `:NNN`, because that is the convention every row in this register uses."""
        found = {}
        for token, path in CITE_SOURCES.items():
            if token in cite and path.exists():
                found[token] = path
        for rel in PATH_RE.findall(cite):
            f = REPO / rel
            if f.exists():
                found[rel] = f
        if LINEREF_RE.search(cite) and SOURCE_353.exists():
            found.setdefault("#353", SOURCE_353)
        return found
    for r in reg["rows"]:
        cite = str(r.get("cite") or "")
        if not cite.strip():
            continue
        refs = [(int(a), int(b or a)) for a, b in LINEREF_RE.findall(cite)]
        for a, b in refs:
            checked += 1
            if b > len(src):
                bad.append(f"{r['id']}: cites :{a}-{b} and #353 has {len(src)} lines")
        named = sources_named(cite)
        # A quote INSIDE a backticked span is part of a COMMAND, not a quotation of a source.
        # G11 asks for a reproduction command on every number, so a cite that obeys G11 contains
        # one, and a command carrying a double-quoted string would otherwise be checked against
        # #353 and reported FABRICATED. Positional rather than a strip, because a legitimate
        # quotation may itself contain backticks — H-33's does.
        code = [(m.start(), m.end()) for m in re.finditer(r"`[^`]*`", cite)]
        # ⚠ MASK CODE SPANS BEFORE PAIRING, NOT AFTER. `QUOTE_RE` pairs `"` characters
        # left-to-right and non-overlapping, so a `"` INSIDE a backticked span -- `f"q:claim:{c.id}"`,
        # `f"claim:{e.id}:{n}"` -- is consumed as an opening or closing mark and shifts every pair
        # after it, manufacturing spans that begin and end mid-sentence. Discarding those matches
        # afterwards (what this did) removes the code-span match but leaves the SHIFT, so real
        # prose downstream is reported FABRICATED for a reason that has nothing to do with it.
        # Blanking the spans first, offsets preserved, makes the pairing correct. Found 2026-09-04
        # when the self-citation fix below turned the misalignment from invisible into 7 spurious
        # violations.
        # ⚠ PAIR ON THE MASKED TEXT, EXTRACT FROM THE ORIGINAL. A legitimate quotation OFTEN
        # CONTAINS a code span -- `H-33` quotes "the `total` default at this milestone is TOTAL
        # FAN-OUT" -- so reading the quote off the masked string would hand the matcher a sentence
        # with holes in it and report eight true citations as fabricated. Offsets are preserved by
        # the blanking, so `cite[m.start(1):m.end(1)]` is the real text.
        masked = list(cite)
        for a, b in code:
            for i in range(a, b):
                masked[i] = " "
        masked = "".join(masked)
        quotes = [cite[m.start(1):m.end(1)] for m in QUOTE_RE.finditer(masked)]
        if quotes and not named:
            bad.append(f"{r['id']}: quotes something and names no source this checker can open")
        for quote in quotes:
            if not named:
                continue
            checked += 1
            needle = _cite_norm(quote).rstrip(".")
            # In #353, a quote with a line ref must be AT the lines cited -- that is the whole
            # point of a line reference. In any other named source, presence is what is checked;
            # those cites carry section names rather than line numbers.
            hit_where, hit_any = False, False
            for token, path in named.items():
                body = [_cite_norm(l) for l in path.read_text().splitlines()]
                # ⚠ COLLAPSE AGAIN AFTER THE JOIN. `_cite_norm` collapses whitespace WITHIN a
                # line, and a BLANK line normalises to "", so joining with " " puts a DOUBLE space
                # where the source had a paragraph break -- while the YAML-folded `cite` has a
                # single one. Without this the self-citation removal below silently missed any row
                # whose `cite:` contains a blank line (`H-117` did), which is a no-op guard that
                # reports green. Collapsing can only make more text match, never less, so no
                # previously-resolving citation is affected.
                whole = re.sub(r"\s+", " ", " ".join(body))
                # ⚠ A ROW MAY NOT BE ITS OWN SOURCE. Naming this register in your own `cite:`
                # otherwise makes every quotation verify AGAINST ITSELF -- a one-token way past
                # the anti-fabrication gate, and WORSE than the defect it was added to fix: the
                # `W-D` pass first "fixed" a flagged self-quote by DELETING ITS QUOTE MARKS
                # (invisible to `QUOTE_RE`), then restored them and named the register instead,
                # and MUTATION-CHECKED that remedy -- planting a `71 GENUINE forks, all DIVERGED`
                # sentence no source says, and watching `CITATIONS: all resolve` come back green.
                # ⚠ THE HAYSTACK IS REBUILT FROM THE OTHER ROWS' PARSED FIELDS, NOT BY DELETING
                # THIS ROW'S TEXT FROM THE FILE. A string subtraction was tried first and SILENTLY
                # DID NOTHING on `H-117`, because `_cite_norm` strips a leading `+` as a list
                # marker per line while the YAML-folded `cite` keeps it mid-string, so the two
                # never matched -- a guard that reports green without checking anything, which is
                # the failure class this whole pass is about. Excluding at the data level cannot
                # miss. Quoting another row still verifies; quoting yourself no longer does.
                # 2026-09-04.
                if path == REGISTER:
                    whole = _rows_text_excluding(reg, r)
                if _contains(whole, needle):
                    hit_any = True
                    if token != "#353" or not refs:
                        hit_where = True
                    else:
                        window = set()
                        for a, b in refs:
                            window |= set(range(max(1, a - 6), min(len(body), b + 6) + 1))
                        if _contains(" ".join(body[i - 1] for i in sorted(window)), needle):
                            hit_where = True
            if not hit_where:
                where = ("in NONE of the sources it names (%s) -- FABRICATED"
                         % ", ".join(sorted(named))) if not hit_any else \
                        "present but NOT at the lines cited -- the LINE NUMBER is wrong"
                bad.append(f"{r['id']}: quoted text is {where}: {quote[:70]!r}")
    if not checked:
        return ["no citation carried a line reference or a quote -- nothing was verified, which "
                "is a FAILURE and not a pass"]
    return bad


# ── THE NINE (ED-IN-0202, Jordan 2026-09-05) ──────────────────────────────────────────────────
REQUIREMENTS = HERE / "requirements.yaml"


def check_requirements() -> int:
    """`requirements.yaml` IS THE ACCEPTANCE SURFACE FOR THE ADOPTED LOOP, and this is what makes
    it mechanism rather than prose (CLAUDE.md §0.05). It fails on the one move that would let the
    nine rot into a wish-list: a row claiming progress it cannot show.

    Two rules, both of them §0.2 ("done means it runs") in a form a checker can apply:
      1. A row at `met` or `partial` MUST carry a non-empty `measured:` AND a `measure:` command.
         A status is a reading, never a judgement, so a status with no reading behind it is a
         claim about the game that nothing produced.
      2. A row at `not_met` must still name a `measure:` -- what WOULD show it, if it held. A
         requirement nothing could ever measure is not a requirement, it is a mood.
    """
    doc = yaml.safe_load(REQUIREMENTS.read_text())
    rows = doc.get("rows") or []
    bad: list[str] = []
    for r in rows:
        rid, st = r.get("id"), r.get("status")
        if st not in ("not_met", "partial", "met"):
            bad.append(f"{rid}: status {st!r} is not one of not_met/partial/met")
        cmd = str(r.get("measure") or "").strip()
        if not cmd:
            bad.append(f"{rid}: no `measure:` -- nothing could ever show this, at any status")
        else:
            # ⚠ THE FIRST VERSION OF THIS CHECK ONLY ASSERTED `measure:` WAS NON-EMPTY, which is
            # §0.1 pt 2 exactly: an assertion that cannot observe the failure it excludes. It
            # shipped with TWO dead commands -- R-09's `-k 'no_roll or ladder_has_no_producer'`
            # selected ZERO tests, and R-02 named a module with no `__main__` that printed
            # nothing on a clean exit 0. Both were found by an adversarial pass, not by this
            # gate. A command is now resolved statically: a `-k` must select at least one test,
            # and a `python <path>` must name a file that exists and can be run.
            head = cmd.split("#", 1)[0].strip()
            if " -k " in head:
                expr = head.split(" -k ", 1)[1].strip().strip("'\"")
                names = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", expr)
                names = [n for n in names if n not in ("or", "and", "not")]
                src = ""
                for t in (HERE / "tests").glob("test_*.py"):
                    src += t.read_text(encoding="utf-8")
                if names and not any(("def test_" in src) and (n in src) for n in names):
                    bad.append(f"{rid}: `-k {expr}` selects NO test -- the measure is dead")
            else:
                m = re.search(r"python3?\s+([\w./-]+\.py)", head)
                if m:
                    f = REPO_ROOT / m.group(1)
                    if not f.exists():
                        bad.append(f"{rid}: `measure:` names {m.group(1)}, which does not exist")
                    elif "__main__" not in f.read_text(encoding="utf-8"):
                        bad.append(f"{rid}: {m.group(1)} has no `__main__` -- running it prints "
                                   f"nothing and exits 0, so the measure shows nothing")
        if st in ("met", "partial") and not str(r.get("measured") or "").strip():
            bad.append(f"{rid}: claims {st} with an empty `measured:` -- a status is a reading")
        if not str(r.get("statement") or "").strip():
            bad.append(f"{rid}: no `statement:` -- the requirement's own words are the record")
    counts: dict = {}
    for r in rows:
        counts[r.get("status")] = counts.get(r.get("status"), 0) + 1
    print(f"THE NINE ({len(rows)} rows, ruled {doc.get('ruled_by')}, {doc.get('ed')})")
    print("  " + " · ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    for r in rows:
        flag = "  ⚠ needs_jordan" if r.get("needs_jordan") else ""
        print(f"    {r['id']}  {r['status']:<8} {str(r['statement'])[:64]}{flag}")
    if bad:
        print("REQUIREMENTS: " + str(len(bad)) + " violation(s)")
        for b in bad:
            print("    " + b)
        return 1
    print("REQUIREMENTS: every row carries a measurement or names one")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--counts", action="store_true")
    ap.add_argument("--verify-citations", action="store_true",
                    help="every `:NNN` a cite names exists, and every verbatim quote is there")
    ap.add_argument("--rule", default="", help="comma-separated subset, e.g. R0,R1,R2,R3")
    ap.add_argument("--requirements", action="store_true",
                    help="THE NINE (ED-IN-0202) -- every row carries a measurement or names one")
    a = ap.parse_args(argv)
    if a.requirements:
        return check_requirements()
    if not (a.check or a.counts or a.verify_citations):
        ap.print_help()
        return 0
    reg = load()
    rc = 0

    if a.counts or a.check:
        c = counts(reg)
        parts = " · ".join(f"{n} {k}" for k, n in c["by_source"].items())
        print(f"REGISTER: {c['rows']} rows ({parts})")
        assert sum(c["by_source"].values()) == c["rows"], (
            f"the source buckets sum to {sum(c['by_source'].values())} over {c['rows']} rows")
        print("  by grade: " + " · ".join(f"{k} {v}" for k, v in c["by_grade"].items()))
        print(f"  tier 0: {c['tier0']}   tier 1: {c['tier1']}")
        print(f"  `absent` rows with no `cite:` (G6's floor): {c['absent_uncited']}")
        print(f"  ARTIFACT 0 -- 'Part VII has no `absent` row in Tier 0': "
              + ("MET" if not c["tier0_absent"]
                 else "UNMET, on " + ", ".join(c["tier0_absent"])))

    if a.check and not a.rule:
        # Skipped when `--rule` selects a subset, so a rule can still be run in isolation.
        cbad = verify_citations(reg)
        print("CITATIONS: " + ("all resolve" if not cbad else f"{len(cbad)} unresolved"))
        for b in cbad:
            print("    " + b)
        rc |= 1 if cbad else 0

    if a.verify_citations:
        cbad = verify_citations(reg)
        for b in cbad:
            print("    " + b)
        print(f"CITATIONS: {'all resolve' if not cbad else str(len(cbad)) + ' unresolved'}")
        rc |= 1 if cbad else 0

    if a.check:
        only = [s.strip() for s in a.rule.split(",") if s.strip()] or None
        res = check(reg, only)
        print()
        for name, bad in res.items():
            print(f"{name}: {'ok' if not bad else str(len(bad)) + ' violation(s)'}")
            for b in bad:
                print("    " + b)
        rc |= 1 if any(res.values()) else 0
    return rc


if __name__ == "__main__":
    sys.exit(main())
