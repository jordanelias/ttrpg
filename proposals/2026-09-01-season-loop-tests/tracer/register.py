"""THE HOLE REGISTER, AS AN OBJECT -- `W0` of `proposals/2026-09-02-executable-architecture/PLAN.md`.

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
    python register.py --verify-transcription   # the 32 rows still match V2's tables

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
PROPOSALS = HERE.parent.parent
ARCH_DIR = PROPOSALS / "2026-09-02-executable-architecture"
REGISTER = ARCH_DIR / "hole_register.yaml"
ARCHITECTURE_V2 = ARCH_DIR / "ARCHITECTURE_V2.md"

GRADES = ("ruled", "measured", "assumption", "absent")
# Strictest first. A row V2 grades in parts (H-02, H-20) takes the strictest grade present,
# because §42.2's polarity rule sends zero evidence to the verdict AGAINST the thing measured:
# a hole that is absent in part must refuse in part, and refusing is what a grade decides.
GRADE_STRICTNESS = ("absent", "assumption", "measured", "ruled")
FIELDS = ("id", "tier", "hole", "kind", "owner", "grade",
          "default", "site", "sweep", "unblocks", "cite", "source")
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
# The marker a row carries when it claims to have come from V2's tables. `verify_transcription`
# walks BOTH directions on it, so a fabricated row cannot wear this string and go unnoticed.
TRANSCRIBED = "transcribed verbatim"


def normalised_default(cell: str) -> str:
    """V2 writes an `absent` row's default as "none" FOLLOWED BY COMMENTARY -- "none. ⚠ every
    contest is blocked", "none — §63.1 may accept it instead". The field means *the value an
    instrument may inject*, and a warning is not a value, so it normalises to `none`. THIS IS THE
    ONE NORMALISATION APPLIED TO `default`, it is declared here rather than in prose, and
    `verify_transcription` pins the field THROUGH it -- so any other edit to a default is drift.

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


# ---------------------------------------------------------------------------
# THE SOURCE OF THE 32 TRANSCRIBED ROWS
# ---------------------------------------------------------------------------

def v2_rows() -> dict:
    """Re-extract V2's Part VII tables. This is the SAME extraction that produced the register,
    so `--verify-transcription` is a genuine round trip rather than a comparison of a file with
    itself: it re-reads the markdown and fails if either side has drifted."""
    src = ARCHITECTURE_V2.read_text().splitlines()
    out, tier, on = {}, None, False
    for ln in src:
        if "## §VII.1" in ln:
            tier, on = 0, True
            continue
        if "## §VII.2" in ln:
            tier, on = 1, True
            continue
        if "## §VII.3" in ln:
            on = False
            continue
        if on and ln.startswith("| **H-"):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            rid = c[0].replace("*", "").strip()
            if not re.fullmatch(r"H-\d{2}", rid):
                # The id CELL must carry the id and nothing else. A marker put there -- an
                # arrow, a footnote -- silently becomes part of the id, and both directions of
                # the round trip then fire with a confusing "fabricated row" verdict rather
                # than naming the real cause. Say the real cause.
                raise SystemExit(
                    f"ARCHITECTURE_V2.md Part VII: id cell reads {rid!r}, which is not `H-NN`. "
                    "The id cell carries the id and nothing else -- put any marker in prose "
                    "beside the table, not in the cell.")
            out[rid] = dict(
                tier=tier, hole=c[1], kind=c[2], owner=c[3],
                grade_cell=c[4], default=c[5], unblocks=c[6])
    return out


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
        extra = sorted(set(r) - set(FIELDS))
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


RULES = {"R0": rule_R0, "R1": rule_R1, "R2": rule_R2,
         "R3": rule_R3, "G6": rule_G6, "G8": rule_G8}


def check(reg: dict, only: list | None = None) -> dict:
    return {k: fn(reg) for k, fn in RULES.items() if not only or k in only}


# ---------------------------------------------------------------------------
# THE COUNTS -- computed, never typed. `G11`.
# ---------------------------------------------------------------------------

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
        # The register's own header states how many rows carry an empty `cite:`. A number a
        # document states and its named command cannot produce is G11's defect in miniature, and
        # it was in the file that forbids it nine lines above.
        "absent_uncited": sum(1 for r in rows if r.get("grade") == "absent"
                              and not str(r.get("cite") or "").strip()),
    }


SOURCE_353 = PROPOSALS / "2026-09-01-holonic-architecture" / "ARCHITECTURE.md"
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
    text = re.sub(r"-{2,}", "-", text)                  # `--` typed for an em dash
    return re.sub(r"\s+", " ", text).strip()


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
    for r in reg["rows"]:
        cite = str(r.get("cite") or "")
        if not cite.strip():
            continue
        refs = [(int(a), int(b or a)) for a, b in LINEREF_RE.findall(cite)]
        for a, b in refs:
            checked += 1
            if b > len(src):
                bad.append(f"{r['id']}: cites :{a}-{b} and #353 has {len(src)} lines")
        for quote in QUOTE_RE.findall(cite):
            if not refs:
                continue
            checked += 1
            needle = _cite_norm(quote).rstrip(".")
            window = set()
            for a, b in refs:
                window |= set(range(max(1, a - 6), min(len(src), b + 6) + 1))
            hay = " ".join(flat[i - 1] for i in sorted(window))
            if not _contains(hay, needle):
                # Not found where cited. Is it anywhere at all? The two are different defects:
                # a wrong line number, versus a quote the source does not contain.
                whole = " ".join(flat)
                where = "NOWHERE IN #353 -- FABRICATED" if not _contains(whole, needle) else \
                        "elsewhere in #353 -- the LINE NUMBER is wrong"
                bad.append(f"{r['id']}: quoted text is {where}: {quote[:70]!r}")
    if not checked:
        return ["no citation carried a line reference or a quote -- nothing was verified, which "
                "is a FAILURE and not a pass"]
    return bad


def verify_transcription(reg: dict) -> list:
    """The 32 rows must still say what V2's tables say. Pins `hole`, `kind`, `owner` and
    `unblocks` -- NOT `grade`, which `W1` deliberately changes as it runs the ladder. Drift in
    EITHER direction fails: a row edited here silently, or a table edited there silently."""
    v2, bad = v2_rows(), []
    if not v2:
        # ZERO EXTRACTED IS A FAILURE, NOT A PASS. Part VII's headings or row format changing --
        # which PLAN.md §0.3 row 14 says is the plan -- would otherwise make this print "clean"
        # having compared nothing, and every later register edit would be unpinned. `rule_G8`
        # already applies this polarity to Part B; omitting it here was the asymmetry.
        return ["ARCHITECTURE_V2.md Part VII parsed to ZERO rows -- the transcription cannot be "
                "verified, which is a FAILURE and not a pass (§42.2's polarity rule)"]
    reg_by_id = {r["id"]: r for r in reg["rows"]}
    # REGISTER -> V2, the direction the first draft did not walk. Without it a fabricated row
    # carrying `source: "...transcribed verbatim"` is undetectable: it would wear V2's provenance
    # and every instrument built on this file would inject from it.
    for r in reg["rows"]:
        if TRANSCRIBED in str(r.get("source")) and r["id"] not in v2:
            bad.append(f"{r['id']}: claims `{TRANSCRIBED}` and ARCHITECTURE_V2.md Part VII has "
                       "no such row -- a fabricated row wearing V2's provenance")
    for rid, src in sorted(v2.items()):
        r = reg_by_id.get(rid)
        if r is None:
            bad.append(f"{rid}: in ARCHITECTURE_V2.md Part VII and NOT in the register")
            continue
        for f in ("hole", "kind", "owner", "unblocks"):
            if str(r.get(f)) != src[f]:
                bad.append(f"{rid}.{f}: register has {r.get(f)!r}, V2 has {src[f]!r}")
        # `default` IS PINNED -- through its one declared normalisation, and ONLY WHILE THE ROW
        # STILL CARRIES V2'S GRADE. It is the field an instrument injects FROM and the field R3
        # reads, so an unpinned `default` is the most consequential silent edit this file could
        # carry. But a re-grade is REQUIRED to move it: `absent` forbids a default (R3) and
        # `assumption` requires one (§G4), so W1 cannot re-grade a row without rewriting its
        # default, and pinning it unconditionally would make the guard fire on the work the plan
        # exists to do. So a moved default is drift while the grade is unchanged, and a reported
        # NOTE once the grade has moved -- the same treatment `grade` itself gets, for the same
        # reason.
        v2_grade = grade_of(src["grade_cell"])
        if r.get("grade") == v2_grade:
            if str(r.get("default")) != normalised_default(src["default"]):
                bad.append(f"{rid}.default: register has {r.get('default')!r}, V2 has "
                           f"{src['default']!r} (normalises to "
                           f"{normalised_default(src['default'])!r})")
        elif str(r.get("default")) != normalised_default(src["default"]):
            bad.append(f"NOTE {rid}.default: rewritten with the re-grade "
                       f"{v2_grade!r} -> {r.get('grade')!r}")
        if r.get("tier") != src["tier"]:
            bad.append(f"{rid}.tier: register has {r.get('tier')}, V2 has {src['tier']}")
        if r.get("grade") and grade_of(src["grade_cell"]) != r["grade"]:
            # Not an error by itself -- W1 re-grades. Reported so a re-grade is visible.
            bad.append(f"NOTE {rid}.grade: register {r['grade']!r}, V2 cell grades "
                       f"{grade_of(src['grade_cell'])!r} (a deliberate re-grade, or a drift)")
    return bad


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--counts", action="store_true")
    ap.add_argument("--verify-transcription", action="store_true")
    ap.add_argument("--verify-citations", action="store_true",
                    help="every `:NNN` a cite names exists, and every verbatim quote is there")
    ap.add_argument("--rule", default="", help="comma-separated subset, e.g. R0,R1,R2,R3")
    a = ap.parse_args(argv)
    if not (a.check or a.counts or a.verify_transcription or a.verify_citations):
        ap.print_help()
        return 0
    reg = load()
    rc = 0

    if a.counts or a.check:
        c = counts(reg)
        print(f"REGISTER: {c['rows']} rows "
              f"({c['transcribed']} transcribed from ARCHITECTURE_V2.md Part VII, "
              f"{c['added_by_plan']} added by PLAN.md §1.4)")
        print("  by grade: " + " · ".join(f"{k} {v}" for k, v in c["by_grade"].items()))
        print(f"  tier 0: {c['tier0']}   tier 1: {c['tier1']}")
        print(f"  `absent` rows with no `cite:` (G6's floor): {c['absent_uncited']}")
        print(f"  ARTIFACT 0 -- 'Part VII has no `absent` row in Tier 0': "
              + ("MET" if not c["tier0_absent"]
                 else "UNMET, on " + ", ".join(c["tier0_absent"])))

    if a.verify_transcription:
        bad = verify_transcription(reg)
        hard = [b for b in bad if not b.startswith("NOTE ")]
        for b in bad:
            print(("  note: " if b.startswith("NOTE ") else "  DRIFT: ") + b.removeprefix("NOTE "))
        print(f"TRANSCRIPTION: {'clean' if not hard else str(len(hard)) + ' drifted'}")
        rc |= 1 if hard else 0

    if a.check and not a.rule:
        # THE TRANSCRIPTION IS PART OF THE CHECK. It was a separate branch, so the plan's proof
        # command (`--check`) never validated that the register still says what V2 says --
        # leaving the one guard on fidelity reachable only by a flag nobody was told to pass.
        # Skipped when `--rule` selects a subset, so a rule can still be run in isolation.
        drift = [b for b in verify_transcription(reg) if not b.startswith("NOTE ")]
        print("TRANSCRIPTION: " + ("clean" if not drift else f"{len(drift)} drifted"))
        for b in drift:
            print("    " + b)
        rc |= 1 if drift else 0

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
