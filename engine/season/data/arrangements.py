"""`season.data.arrangements` -- THE ONE LOADER for `arrangements.yaml` and its `speech_kinds:`
section. Plan position `18` (PROC-A), `21_RECONCILIATION.md` PHASE 2 step 6 / `19_PLAN.md` step 11 /
`03_PARAMETERS.md` PART D.

Modelled on `data/verbs.py::_load_verb_table` and `data/rosters.py::_load_offices` -- the two
existing "a sibling registry gets a loader that refuses unknown keys at import" precedents in this
package (`04_CODE_ARCHITECTURE.md:131` puts every closed set and the ONE loader in `data/`). Load-time
schema violations raise `SystemExit`, never `Unspecified` -- `H-115`'s ruling, carried from
`data/verbs.py`: a broken TABLE is not a per-act gap `corpus_run.run_case`'s `except ShapeGap` should
catch and misattribute to one case.

⚠ THIRTEEN KEYS, NOT FIFTEEN. See `arrangements.yaml`'s own header for the `19_PLAN.md` step 11
derivation (15 - `registers`/`verdict_reasons`/`stakes_grade` + `quorum` = 13).

⚠ C-1 IS REPORTED, NOT REFUSED, AND THE REASON IS STATED RATHER THAN QUIETLY DECIDED.
`21_RECONCILIATION.md` PHASE 2 step 6 names a load check: *"every row's `disposes` kind must name
`determine` in `ID-14`'s opener map (or the parties' `oblige` for `disposal: mutual`)."* `ID-14`'s
opener map is `data/verbs.py::_derive_openers_from_effects()`, an AST walk over `loop/effects.py`'s
`Tenure(...)` constructions -- and `determine` HAS NO EFFECT FUNCTION AT ALL YET (`grep -rn
'"determine"' loop/effects.py` returns nothing; that is `21_RECONCILIATION.md` PHASE 2 step 11's job,
explicitly out of this position's five parts). So the check, read as a hard load-time refusal, would
refuse EVERY row this loader could ever carry -- `determine` opens nothing today, for any Tenure kind,
and neither does any verb yet open an `oblige` on a mutual disposal's behalf. Enforcing it would make
the loader vacuous, contradicting this position's own stated artifact ("twelve rows load"). Built
instead as a REPORT (`arrangements_without_a_disposal_opener()`), on the exact precedent
`tenure_kinds_without_an_opener()` already sets one file over for the identical kind of fact: a kind
with a declared `writes:` cell and no opener is *"a real, disclosed hole, not an absent declaration."*
A row failing C-1 today is disclosed by that function, not silently admitted and not blocked.

⚠ SUPERSEDED IN ITS PREMISE AT PLAN POSITION `19` (U7-remit), 2026-09-29, AND LEFT A REPORT: the
paragraph above is true of `18`'s commit and no longer of the tree -- `loop/effects.py::_eff_determine`
EXISTS and opens an `oblige` (the disposal), the derived opener map reads `determine` beside
`oblige`'s own opener, and the report is EMPTY over the seeded rows (`test_arrangements.py`,
`test_u7_remit.py`). So the reason given for reporting rather than refusing -- *"`determine` opens
nothing today"* -- is gone. `19` did not turn it into a load refusal: the refusal would have to read
`data/verbs.py`'s derived map at `_load()` time, an import-order question for this module's owner,
and nothing seeded fails it. A row disposing a Tenure kind `determine` does not open (`hold`,
`commit`, ...) would still only be REPORTED.
"""

from __future__ import annotations

from typing import Any, Optional

from . import files
from .rosters import (
    GENRES, INTERPOSITION_KINDS, LADDER_RUNGS, PROOFS, REMIT_ACTS, RUNG_KINDS, TENURE_KINDS,
    load_yaml,
)

ARRANGEMENTS_YAML = files.ARRANGEMENTS_YAML

# THE DEGREE LADDER, NOT RE-DERIVED. `engine/autoload/dice_engine.py::DEGREE_LABEL` is the single
# owner (Jordan ruling, 2026-08-14: "THE degree ladder... for every scale of the game"), imported
# rather than copied into a `rosters.yaml` roster of its own -- a fresh `degree_bands` roster with
# these same four values collided with a PRE-EXISTING, unrelated literal in
# `tests/test_mass_battle_provider.py` (same four names, same reason: it is the same ladder), which
# `test_jordan_no_definition_is_hardcoded_in_a_body` correctly read as two owners of one fact the
# moment a second one was written down. Importing the enum's own labels is the one-owner fix rather
# than a second declaration this loader would then have to keep in step with dice_engine.py by hand.
from engine.autoload.dice_engine import DEGREE_LABEL as _DEGREE_LABEL   # noqa: E402
DEGREE_BANDS = frozenset(_DEGREE_LABEL.values())

# ---------------------------------------------------------------------------
# roster-exempt: MECHANISM. These are THIS LOADER'S OWN GRAMMAR -- which values a key on THE ROW
# ITSELF may take -- not the game's vocabulary the way `interposition_kinds`/`proofs`/`genres` are.
# `data/requires.py::REQUIRES_STEMS`/`COMPARATORS` are the direct precedent for a closed set that
# stays a Python frozenset rather than a `rosters.yaml` entry: a grammar's own shape, checked once,
# never a content roster a designer edits to add a game.
# ---------------------------------------------------------------------------
_DISPOSAL_VALUES = frozenset({"bench", "mutual", "none", "declared"})
_FLOOR_FORMS = frozenset({"open", "closed", "admitted"})
_ORDER_VALUES = frozenset({"free", "rank", "alternating", "scripted", "written_only"})
_DISPOSAL_REACH_FORMS = frozenset({"room", "body"})     # or a `RUNG_KINDS` member, checked separately
_DISPOSES_LITERALS = frozenset({"Record", "none"})      # or a `TENURE_KINDS` member, checked separately

# roster-exempt: MECHANISM, same reason as the block above -- THE ROW'S OWN FIELD NAMES, the
# identical shape `state/carriers.py::Rung._DECLARED` is exempted for. Not the game's vocabulary.
_ARRANGEMENT_KEYS = frozenset({
    "id", "disposal", "bench_basis", "floor", "records_dissent", "venue_min_rank",
    "term_required", "appeal_basis", "interposed", "order", "proofs", "disposes",
    "disposal_reach", "quorum",
})
_SPEECH_KIND_KEYS = frozenset({"id", "genres", "min_rank", "reachable_bands"})


def _refuse_unknown(row: dict, declared: frozenset, name: str, kind: str) -> None:
    unknown = sorted(k for k in row if k not in declared)
    if unknown:
        raise SystemExit(
            f"arrangements.yaml: {kind} {name!r} carries unknown key(s) {unknown}. "
            f"`04_CODE_ARCHITECTURE.md:468` -- unknown keys are rejected; a row's keys are the "
            f"ones this loader reads ({sorted(declared)}).")


def _refuse_not_in(name: str, field: str, value, roster, roster_label: str = "", *,
                    repr_fn=sorted) -> None:
    """A single value must be a roster member. `repr_fn` formats the roster for the message --
    `sorted` by default, or `list` where order is semantic (`RUNG_KINDS`'s rank order), passed
    rather than re-derived so a rank-ordered roster keeps displaying in rank order.
    `roster_label` describes the roster (e.g. "a `rung_kinds` member"); omitted, the message
    reads "not one of {repr}" with no parenthesised citation, for a roster with no name worth
    citing (a literal value set declared right here, not read from another file)."""
    if value not in roster:
        if roster_label:
            raise SystemExit(
                f"arrangements.yaml: {name!r} has `{field}: {value!r}`, not {roster_label} "
                f"({repr_fn(roster)}).")
        raise SystemExit(
            f"arrangements.yaml: {name!r} has `{field}: {value!r}`, not one of "
            f"{repr_fn(roster)}.")


def _refuse_any_not_in(name: str, kind: str, field_label: str, values, roster, roster_label: str,
                        *, repr_fn=sorted) -> None:
    """Every value in a list must be a roster member."""
    bad = [v for v in values if v not in roster]
    if bad:
        raise SystemExit(
            f"arrangements.yaml: {kind} {name!r} names {field_label} {bad} outside "
            f"{roster_label} ({repr_fn(roster)}).")


def _parse_floor(name: str, raw: Any) -> tuple:
    """`open | closed | admitted:<remit act>` -- the one key with an embedded parameter. Returns
    `(form, basis_or_None)`. `admitted` alone (no `:<basis>`) is admitted too: `03_PARAMETERS.md`'s
    own worked rows write bare `admitted` on three of the twelve games with no basis spelled out."""
    text = str(raw)
    form, _, basis = text.partition(":")
    if form not in _FLOOR_FORMS:
        raise SystemExit(
            f"arrangements.yaml: {name!r} has `floor: {raw!r}`, whose form {form!r} is not one of "
            f"{sorted(_FLOOR_FORMS)} (`open | admitted:<basis> | closed`, PART D's schema).")
    if basis and basis not in REMIT_ACTS:
        raise SystemExit(
            f"arrangements.yaml: {name!r} has `floor: {raw!r}`, whose basis {basis!r} is not a "
            f"`remit_acts` member ({sorted(REMIT_ACTS)}).")
    return form, (basis or None)


def _load_speech_kind(row: dict) -> dict:
    if not isinstance(row, dict) or not row.get("id"):
        raise SystemExit(f"arrangements.yaml: a `speech_kinds:` row has no `id`: {row!r}")
    name = str(row["id"])
    _refuse_unknown(row, _SPEECH_KIND_KEYS, name, "speech_kinds row")
    genres = list(row.get("genres") or ())
    _refuse_any_not_in(name, "speech_kinds row", "genre(s)", genres, GENRES, "`rosters.yaml: genres`")
    min_rank = row.get("min_rank")
    if min_rank is not None:
        _refuse_not_in(name, "min_rank", min_rank, RUNG_KINDS, "a `rung_kinds` member",
                       repr_fn=list)
    bands = list(row.get("reachable_bands") or ())
    _refuse_any_not_in(name, "speech_kinds row", "reachable band(s)", bands, DEGREE_BANDS,
                       "`dice_engine.py: DEGREE_LABEL`")
    # ⚠ Loader invariant per `19_PLAN.md` step 7: "the loader refuses a kind whose reachable
    # bands name a band outside the ladder" -- carried as a code comment, not repeated per row,
    # since `_refuse_any_not_in`'s message above already names the exact defect and the roster.
    # roster-exempt: MECHANISM -- the return shape's own field names, not a second roster.
    return {"id": name, "genres": tuple(genres), "min_rank": min_rank,
            "reachable_bands": tuple(bands)}


def _load_arrangement(row: dict) -> dict:
    if not isinstance(row, dict) or not row.get("id"):
        raise SystemExit(f"arrangements.yaml: an `arrangements:` row has no `id`: {row!r}")
    name = str(row["id"])
    _refuse_unknown(row, _ARRANGEMENT_KEYS, name, "arrangement")

    def need(key: str):
        if key not in row:
            raise SystemExit(f"arrangements.yaml: {name!r} has no `{key}:`. PART D's thirteen keys "
                             f"are all required (a row states its shape in full, or not at all).")
        return row[key]

    disposal = need("disposal")
    _refuse_not_in(name, "disposal", disposal, _DISPOSAL_VALUES)
    bench_basis = need("bench_basis")
    if bench_basis != "none":
        _refuse_not_in(name, "bench_basis", bench_basis, REMIT_ACTS, "`none` or a `remit_acts` member")
    floor_form, floor_basis = _parse_floor(name, need("floor"))
    records_dissent = need("records_dissent")
    if not isinstance(records_dissent, bool):
        raise SystemExit(f"arrangements.yaml: {name!r} has `records_dissent: {records_dissent!r}`, "
                         "not `true`/`false`.")
    venue_min_rank = need("venue_min_rank")
    _refuse_not_in(name, "venue_min_rank", venue_min_rank, RUNG_KINDS, "a `rung_kinds` member",
                   repr_fn=list)
    term_required = need("term_required")
    if not isinstance(term_required, bool):
        raise SystemExit(f"arrangements.yaml: {name!r} has `term_required: {term_required!r}`, "
                         "not `true`/`false`.")
    appeal_basis = need("appeal_basis")
    if appeal_basis != "none":
        _refuse_not_in(name, "appeal_basis", appeal_basis, REMIT_ACTS, "`none` or a `remit_acts` member")
    interposed = list(need("interposed") or ())
    _refuse_any_not_in(name, "arrangement", "interposed kind(s)", interposed, INTERPOSITION_KINDS,
                       "`rosters.yaml: interposition_kinds`")
    order = need("order")
    _refuse_not_in(name, "order", order, _ORDER_VALUES)
    proofs = list(need("proofs") or ())
    _refuse_any_not_in(name, "arrangement", "proof(s)", proofs, PROOFS, "`rosters.yaml: proofs`")
    disposes = need("disposes")
    if disposes not in _DISPOSES_LITERALS and disposes not in TENURE_KINDS:
        raise SystemExit(
            f"arrangements.yaml: {name!r} has `disposes: {disposes!r}`, not `Record`, `none` or a "
            f"`tenure_kinds` member ({sorted(TENURE_KINDS)}).")
    disposal_reach = need("disposal_reach")
    if disposal_reach not in _DISPOSAL_REACH_FORMS and disposal_reach not in RUNG_KINDS:
        raise SystemExit(
            f"arrangements.yaml: {name!r} has `disposal_reach: {disposal_reach!r}`, not `room`, "
            f"`body` or a `rung_kinds` member ({list(RUNG_KINDS)}).")
    # THE ONE KEY `19_PLAN.md` step 11 ADDS: required exactly when `disposal: declared`, and
    # refused otherwise -- both directions checked, on the same discipline `verb_table.yaml`'s
    # `requires_typed_note:` cross-check uses (a key present for no reason is as much a defect as
    # one absent for a reason). `19_PLAN.md` step 11's own falsifier: "a declared-disposal row
    # with no quorum fails the load."
    quorum = row.get("quorum")
    if disposal == "declared" and quorum is None:
        raise SystemExit(
            f"arrangements.yaml: {name!r} has `disposal: declared` and no `quorum:`. A declared "
            "disposal's tally IS the finding (`19_PLAN.md` step 11: \"the dissent key ... under a "
            "declared disposal it is the tally made visible\"), and a tally with no quorum is not "
            "a rule.")
    if disposal != "declared" and quorum is not None:
        raise SystemExit(
            f"arrangements.yaml: {name!r} has `quorum: {quorum!r}` and `disposal: {disposal!r}` -- "
            "`quorum` is `declared`'s own key; a row with a different disposal carrying one is a "
            "stray value nothing reads.")
    # roster-exempt: MECHANISM -- the return shape's own field names, not a second roster.
    return {
        "id": name, "disposal": disposal, "bench_basis": bench_basis,
        "floor": floor_form, "floor_basis": floor_basis, "records_dissent": records_dissent,
        "venue_min_rank": venue_min_rank, "term_required": term_required,
        "appeal_basis": appeal_basis, "interposed": tuple(interposed), "order": order,
        "proofs": tuple(proofs), "disposes": disposes, "disposal_reach": disposal_reach,
        "quorum": quorum,
    }


def _load() -> tuple[dict, dict]:
    if not ARRANGEMENTS_YAML.exists():
        raise SystemExit(f"arrangements.yaml not found at {ARRANGEMENTS_YAML}")
    doc = load_yaml(ARRANGEMENTS_YAML.read_text(encoding="utf-8")) or {}
    kinds: dict = {}
    for r in doc.get("speech_kinds") or ():
        row = _load_speech_kind(r)
        if row["id"] in kinds:
            raise SystemExit(f"arrangements.yaml: speech_kinds id {row['id']!r} appears more than once")
        kinds[row["id"]] = row
    arrangements: dict = {}
    for r in doc.get("arrangements") or ():
        row = _load_arrangement(r)
        if row["id"] in arrangements:
            raise SystemExit(f"arrangements.yaml: arrangement id {row['id']!r} appears more than once")
        arrangements[row["id"]] = row
    return arrangements, kinds


ARRANGEMENTS, SPEECH_KINDS = _load()


def arrangements_without_a_disposal_opener() -> list[str]:
    """C-1, AS A REPORT (see module docstring for why refusing is wrong today). Every arrangement
    id whose `disposes` kind has no opener naming `determine` -- or, for `disposal: mutual`, whose
    `oblige` has no opener at all -- in `data/verbs.py::_derive_openers_from_effects()`'s map.

    ⚠ MEASURED, NOT ASSUMED, AND CORRECTED (methodology close, terminal critique, 2026-09-29):
    at this position's own commit, `determine` opens nothing (no `_eff_determine` exists) and
    `oblige` had no opener either (`rosters.yaml: tenure_kinds`'s own note: "the other five
    empty") -- it has one since plan position `17a` (`_eff_oblige`, the joiner's own act), so a
    `disposal: mutual` row now passes this check -- but that reports only the seeded rows this check actually ASKS: a row disposing
    `Record` or `none` is excluded below (`continue`, "C-1 is about a TENURE kind's opener; neither
    is one"), so it is the seeded rows disposing a real Tenure kind or `mutual` that report today,
    not every seeded row -- `test_arrangements.py` pins this exactly (`["arbitration"]`, the one
    seeded row disposing a Tenure kind, against two `Record`-disposing rows that are correctly
    absent). That is the disclosed gap this function exists to make checkable rather than silent --
    the same shape `tenure_kinds_without_an_opener()` already reports one file over.

    ⚠ AND THE GAP CLOSED AT PLAN POSITION `19`: `_eff_determine` opens the disposal `oblige`, so
    `arbitration` is no longer reported and the pinned report is `[]` (see the module docstring's
    `19` paragraph for why it stays a report)."""
    from .verbs import _OPENERS_FROM_EFFECTS as openers
    out = []
    for name, row in ARRANGEMENTS.items():
        if row["disposal"] == "mutual":
            if not openers.get("oblige"):
                out.append(name)
            continue
        kind = row["disposes"]
        if kind in ("Record", "none"):
            continue                      # C-1 is about a TENURE kind's opener; neither is one
        if "determine" not in (openers.get(kind) or ()):
            out.append(name)
    return out
