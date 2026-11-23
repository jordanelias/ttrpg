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
derivation (15 - `registers`/`verdict_reasons`/`stakes_grade` + `quorum` = 13). B05.21 (T13 edit 2) adds a fourteenth, `standard:`, a
`difficulty_levels` member required of every row. ⚠ B24p.03 (V2 p1 §D, p2 §B, §I, §J) makes it SEVENTEEN: `rite`, `turns`, `authority`,
`reason_lean` are added, `order` is deleted (the bearer opens, the rest by precedence), `proofs` is renamed `admits` (a `MATTERS` member each) and
`disposal` is renamed `close` (`bench`, `declared`, `hearers`, `consent`; `exchange` is `abridged(row)`'s alone). The file also carries the
`rites:`, `context:` and `disposal:` blocks, loaded before the rows and exposed as `RITES`, `CONTEXT`, `DISPOSAL`.

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
paragraph above is true of `18`'s commit and no longer of the tree -- `loop/effects_information.py::_eff_determine`
EXISTS and opens an `oblige` (the disposal), the derived opener map reads `determine` beside
`oblige`'s own opener, and the report is EMPTY over the seeded rows (`test_arrangements.py`,
`test_u7_remit.py`). So the reason given for reporting rather than refusing -- *"`determine` opens
nothing today"* -- is gone. `19` did not turn it into a load refusal: the refusal would have to read
`data/verbs.py`'s derived map at `_load()` time, an import-order question for this module's owner,
and nothing seeded fails it. A row disposing a Tenure kind `determine` does not open (`hold`,
`commit`, ...) would still only be REPORTED.
"""

from __future__ import annotations

from typing import Any

from . import files
from .rosters import (
    AUTHORITIES, DEGREE_BANDS, DIFFICULTY_LEVELS, DISPOSAL_WRITES, GENRES, GROUNDS, INTERPOSITION_KINDS, ISSUE_RUNGS, MATTERS,
    PROCEEDING_MOVES, REMIT_ACTS, RUNG_KINDS, TENURE_KINDS, load_yaml, roster,
)


ARRANGEMENTS_YAML = files.ARRANGEMENTS_YAML

# THE DEGREE LADDER, NOT RE-DERIVED: `DEGREE_BANDS` is bound ONCE, in `data/rosters.py` beside its first
# consumer (`FINDING_TERMS`), from `engine/dice_engine/dice_engine.py::DEGREE_LABEL` -- the single owner
# (Jordan ruling, 2026-08-14). A second spelling of the four labels is a second owner of one fact.

# ---------------------------------------------------------------------------
# roster-exempt: MECHANISM. These are THIS LOADER'S OWN GRAMMAR -- which values a key on THE ROW
# ITSELF may take -- not the game's vocabulary the way `interposition_kinds`/`matters`/`genres` are.
# `data/requires.py::REQUIRES_STEMS`/`COMPARATORS` are the direct precedent for a closed set that
# stays a Python frozenset rather than a `rosters.yaml` entry: a grammar's own shape, checked once,
# never a content roster a designer edits to add a game.
# ---------------------------------------------------------------------------
_CLOSE_VALUES = frozenset({"bench", "declared", "hearers", "consent"})     # `exchange` is `abridged`'s, never a row's (B24p.03)
_FLOOR_FORMS = frozenset({"open", "closed", "admitted"})
_DISPOSAL_REACH_FORMS = frozenset({"room", "body"})     # or a `RUNG_KINDS` member, checked separately
# or a `TENURE_KINDS` member, checked separately (`yield` is a questioning's: what the questioned man gave up)
_DISPOSES_LITERALS = frozenset({"Record", "none", "yield"})
# B24p.03: THE RITE'S OWN GRAMMAR (V2 p2 §B) -- the sides a rite names and the values of its cells; the moves and the issues are rosters.
_RITE_SIDES = ("for", "against")
_REPLY_VALUES = frozenset({"must", "may", "raise"})
_SILENCE_VALUES = frozenset({"admits", "refusal", "free"})
_CONCEDE_VALUES = frozenset({"descends", "accepts"})
_IMPASSE = "impasse"          # the disposal table's band for a sitting that reached no verdict (V2 p2 §J)

# roster-exempt: MECHANISM, same reason as the block above -- THE ROW'S OWN FIELD NAMES, the
# identical shape `state/carriers.py::Rung._DECLARED` is exempted for. Not the game's vocabulary.
_ARRANGEMENT_KEYS = frozenset({
    "id", "rite", "turns", "authority", "reason_lean", "admits", "close", "bench_basis", "floor", "records_dissent",
    "venue_min_rank", "term_required", "appeal_basis", "interposed", "disposes", "disposal_reach", "quorum", "standard",
})
_RITE_KEYS = frozenset({"id", "genre", "live", "bears", "reply", "silence", "issues", "concede", "moves"})
# the context tables' own field names (V2 p2 §I); an era's fields are the `GROUNDS`, a regime's `power` the `AUTHORITIES`
_REGIME_KEYS = frozenset({"unlawful", "gravity", "standard", "reason_lean", "admits_add", "admits_drop", "power", "silence", "floor"})
_STRIFE_KEYS = frozenset({"turns", "unrest", "gravity", "care_want"})
_CONTEXT_TABLES = ("eras", "regimes", "strife")
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


def _is_number(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _in_tenths(x, lo: float, hi: float) -> bool:
    """A number in `[lo, hi]` that is a whole number of tenths (R11's dials are set in tenths)."""
    return _is_number(x) and lo <= x <= hi and abs(x * 10 - round(x * 10)) < 1e-9


def _word(name: str, kind: str, key: str, value) -> str:
    if not isinstance(value, str) or not value:
        raise SystemExit(f"arrangements.yaml: {kind} {name!r} has `{key}: {value!r}`, not a non-empty word.")
    return value


def _load_rite(row: dict) -> dict:
    """One `rites:` row (V2 p2 §B): the type's structure, which no module compares by id. The sides are `_RITE_SIDES`; `moves` and `reply`
    are per side; a side with no move has no reply (the crowd of a `rally`); `bears` (who opens) is a side that has a move; `issues` is a
    list of `ISSUE_RUNGS` members, empty for the one undivided issue, the matter itself."""
    if not isinstance(row, dict) or not row.get("id"):
        raise SystemExit(f"arrangements.yaml: a `rites:` row has no `id`: {row!r}")
    name = str(row["id"])
    _refuse_unknown(row, _RITE_KEYS, name, "rite")
    missing = sorted(_RITE_KEYS - set(row))
    if missing:
        raise SystemExit(f"arrangements.yaml: rite {name!r} has no {missing}; a rite states every cell (V2 p2 §B).")
    genre, live, bears = (_word(name, "rite", k, row[k]) for k in ("genre", "live", "bears"))
    moves_in, reply_in = row["moves"], row["reply"]
    if not isinstance(moves_in, dict) or not isinstance(reply_in, dict) or set(moves_in) != set(_RITE_SIDES):
        raise SystemExit(f"arrangements.yaml: rite {name!r} must give `moves:` for each of {list(_RITE_SIDES)} (an empty list for a side "
                         f"with none) and `reply:` as a mapping from a side.")
    moves = {}
    for side in _RITE_SIDES:
        ms = list(moves_in[side] or ())
        _refuse_any_not_in(name, "rite", f"move(s) of the `{side}` side", ms, PROCEEDING_MOVES, "`rosters.yaml: proceeding_moves`",
                           repr_fn=list)
        moves[side] = tuple(ms)
    if bears not in _RITE_SIDES or not moves[bears]:
        raise SystemExit(f"arrangements.yaml: rite {name!r} has `bears: {bears!r}`, not a side with a move ({list(_RITE_SIDES)}).")
    reply = {}
    for side, r in reply_in.items():
        _refuse_not_in(name, f"reply.{side}", side, _RITE_SIDES)
        _refuse_not_in(name, f"reply.{side}", r, _REPLY_VALUES)
        reply[side] = r
    unanswering = [side for side in _RITE_SIDES if moves[side] and side not in reply]
    if unanswering:
        raise SystemExit(f"arrangements.yaml: rite {name!r} gives {unanswering} moves and no `reply:` (must, may or raise).")
    issues = list(row["issues"] or ())
    _refuse_any_not_in(name, "rite", "issue(s)", issues, ISSUE_RUNGS, "`rosters.yaml: issue_rungs`", repr_fn=list)
    silence, concede = row["silence"], row["concede"]
    _refuse_not_in(name, "silence", silence, _SILENCE_VALUES)
    _refuse_not_in(name, "concede", concede, _CONCEDE_VALUES)
    # roster-exempt: MECHANISM -- the return shape's own field names, not a second roster.
    return {"id": name, "genre": genre, "live": live, "bears": bears, "reply": reply, "silence": silence, "issues": tuple(issues),
            "concede": concede, "moves": moves}


def _load_rites(rows) -> dict:
    out: dict = {}
    for r in rows or ():
        rite = _load_rite(r)
        if rite["id"] in out:
            raise SystemExit(f"arrangements.yaml: rite id {rite['id']!r} appears more than once")
        out[rite["id"]] = rite
    if not out:
        raise SystemExit("arrangements.yaml: no `rites:` -- every row names one (V2 p1 §D).")
    return out


def _load_context(ctx) -> dict:
    """The `context:` block (V2 p2 §I): `eras` (a weight for each ground), `regimes` and `strife` (the cell deltas), each row stating every
    key of its table. A key outside a table's set, a ground, authority or matter that does not exist, is refused naming the row. A rite or row
    named `unlawful` is checked in `_load`, once the rows are read."""
    if not isinstance(ctx, dict) or set(ctx) != set(_CONTEXT_TABLES):
        raise SystemExit(f"arrangements.yaml: `context:` must carry exactly {list(_CONTEXT_TABLES)}, not {sorted(ctx) if isinstance(ctx, dict) else ctx!r}.")
    out: dict = {}
    for table, keys in (("eras", GROUNDS), ("regimes", _REGIME_KEYS), ("strife", _STRIFE_KEYS)):
        rows = ctx[table]
        if not isinstance(rows, dict) or not rows:
            raise SystemExit(f"arrangements.yaml: `context.{table}` carries no rows.")
        out[table] = {}
        for rid, row in rows.items():
            name = f"{table}.{rid}"
            if not isinstance(row, dict):
                raise SystemExit(f"arrangements.yaml: `context` row {name!r} is not a mapping: {row!r}")
            _refuse_unknown(row, frozenset(keys), name, "context row")
            absent = sorted(set(keys) - set(row))
            if absent:
                raise SystemExit(f"arrangements.yaml: `context` row {name!r} has no {absent}; a context row states every key of its table.")
            out[table][rid] = dict(row)
    for rid, row in out["eras"].items():
        for g, w in row.items():
            if not _is_number(w) or w <= 0:
                raise SystemExit(f"arrangements.yaml: `context` row 'eras.{rid}' weighs {g!r} at {w!r}, not a positive number.")
    for rid, row in out["strife"].items():
        for k, v in row.items():
            if not _is_number(v) or (k == "turns" and v != int(v)):
                raise SystemExit(f"arrangements.yaml: `context` row 'strife.{rid}' has `{k}: {v!r}`, not a number"
                                 f"{' (a whole number of turns)' if k == 'turns' else ''}.")
    for rid, row in out["regimes"].items():
        name = f"regimes.{rid}"
        for k in ("gravity", "standard", "reason_lean"):
            if not _is_number(row[k]):
                raise SystemExit(f"arrangements.yaml: `context` row {name!r} has `{k}: {row[k]!r}`, not a number.")
        for k in ("admits_add", "admits_drop"):
            row[k] = tuple(row[k] or ())
            _refuse_any_not_in(name, "context row", f"`{k}` kind(s)", row[k], MATTERS, "`rosters.yaml: matters`")
        row["unlawful"] = tuple(row["unlawful"] or ())
        power = row["power"]
        if not isinstance(power, dict) or set(power) != set(AUTHORITIES) or not all(_is_number(w) and w > 0 for w in power.values()):
            raise SystemExit(f"arrangements.yaml: `context` row {name!r} has `power: {power!r}`, not a positive weight for each of "
                             f"{sorted(AUTHORITIES)}.")
        if row["silence"] is not None:
            _refuse_not_in(name, "silence", row["silence"], _SILENCE_VALUES)
        if row["floor"] is not None:
            _refuse_not_in(name, "floor", row["floor"], _FLOOR_FORMS)
    return out


def _load_disposal(table) -> dict:
    """The `disposal:` block (V2 p2 §J): `disposes -> band -> typed writes`. A key is a `disposes` value (`_DISPOSES_LITERALS` or a
    `TENURE_KINDS` member); each states every band of the ladder and `impasse`; each write is a `rosters.yaml: disposal_writes` member."""
    if not isinstance(table, dict) or not table:
        raise SystemExit("arrangements.yaml: no `disposal:` -- every row's `disposes` names a row of it (V2 p2 §J).")
    bands = frozenset(DEGREE_BANDS) | {_IMPASSE}
    out: dict = {}
    for kind, by_band in table.items():
        if kind not in _DISPOSES_LITERALS and kind not in TENURE_KINDS:
            raise SystemExit(f"arrangements.yaml: `disposal:` row {kind!r} is not a `disposes` value (`Record`, `none`, `yield` or a "
                             f"`tenure_kinds` member).")
        if not isinstance(by_band, dict) or set(by_band) != bands:
            raise SystemExit(f"arrangements.yaml: `disposal:` row {kind!r} must state exactly the bands {sorted(bands)}.")
        out[kind] = {}
        for band, writes in by_band.items():
            writes = list(writes or ())
            _refuse_any_not_in(f"{kind}/{band}", "disposal row", "write(s)", writes, DISPOSAL_WRITES, "`rosters.yaml: disposal_writes`")
            out[kind][band] = tuple(writes)
    return out


def _load_arrangement(row: dict, rites: dict | None = None, disposal: dict | None = None) -> dict:
    """One `arrangements:` row. `rites` and `disposal` default to the loaded `RITES` and `DISPOSAL` (a caller outside `_load`, which passes
    them, reads the shipped blocks)."""
    rites = RITES if rites is None else rites
    disposal_table = DISPOSAL if disposal is None else disposal
    if not isinstance(row, dict) or not row.get("id"):
        raise SystemExit(f"arrangements.yaml: an `arrangements:` row has no `id`: {row!r}")
    name = str(row["id"])
    _refuse_unknown(row, _ARRANGEMENT_KEYS, name, "arrangement")

    def need(key: str):
        if key not in row:
            raise SystemExit(f"arrangements.yaml: {name!r} has no `{key}:`. PART D's keys, `standard:` "
                             f"(B05.21) and the proceeding's (B24p.03) are all required (a row states its shape in full, or not at all).")
        return row[key]

    rite = need("rite")
    _refuse_not_in(name, "rite", rite, rites, "a `rites:` id")
    turns = need("turns")
    if (not isinstance(turns, (list, tuple)) or len(turns) != 2
            or not all(isinstance(t, int) and not isinstance(t, bool) for t in turns) or not 1 <= turns[0] <= turns[1]):
        raise SystemExit(f"arrangements.yaml: {name!r} has `turns: {turns!r}`, not `(least, most)`, whole numbers with 1 <= least <= most.")
    authority = need("authority")
    _refuse_not_in(name, "authority", authority, AUTHORITIES, "an `authorities` member", repr_fn=list)
    reason_lean = need("reason_lean")
    if not _in_tenths(reason_lean, -1, 1):
        raise SystemExit(f"arrangements.yaml: {name!r} has `reason_lean: {reason_lean!r}`, not a number in [-1, 1] that is a whole number "
                         f"of tenths (the venue's lean of the dice toward Reason or Presence, R11).")
    admits = list(need("admits") or ())
    _refuse_any_not_in(name, "arrangement", "kind(s) admitted", admits, MATTERS, "`rosters.yaml: matters`")
    close = need("close")
    if close == "exchange":
        raise SystemExit(f"arrangements.yaml: {name!r} has `close: exchange`, which only `abridged(row)` sets (the one speech's own "
                         f"margin with the one addressed); a row's close is one of {sorted(_CLOSE_VALUES)}.")
    _refuse_not_in(name, "close", close, _CLOSE_VALUES)
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
    disposes = need("disposes")
    if disposes not in _DISPOSES_LITERALS and disposes not in TENURE_KINDS:
        raise SystemExit(
            f"arrangements.yaml: {name!r} has `disposes: {disposes!r}`, not `Record`, `none`, `yield` or a "
            f"`tenure_kinds` member ({sorted(TENURE_KINDS)}).")
    if disposes not in disposal_table:
        raise SystemExit(f"arrangements.yaml: {name!r} has `disposes: {disposes!r}` and the `disposal:` block has no row for it "
                         f"({sorted(disposal_table)}); the fold would have no writes to perform (V2 p2 §J).")
    # A-139 AS CORRECTED: a party may also adjudicate, so the loader refuses only the row that can seat ONE character in every role -- a rite that
    # gives moves to one side alone, closed by the parties' consent: the one party would consent with himself. Every other combination loads
    # (`acclamation`, a consent on the `rally` structure under `authority: none`, among them); the sitting-level invariant is `Input`'s.
    # [ASSUMPTION; Jordan to correct: the data form of A-139's one refusal.]
    sides_with_moves = [side for side, ms in rites[rite]["moves"].items() if ms]
    if close == "consent" and authority == "parties" and len(sides_with_moves) < 2:
        raise SystemExit(f"arrangements.yaml: {name!r} has `close: consent` under `authority: parties` on the rite {rite!r}, which gives moves "
                         f"to {sides_with_moves} alone -- the one party would consent with himself (A-139: one character may not fill every role).")
    disposal_reach = need("disposal_reach")
    if disposal_reach not in _DISPOSAL_REACH_FORMS and disposal_reach not in RUNG_KINDS:
        raise SystemExit(
            f"arrangements.yaml: {name!r} has `disposal_reach: {disposal_reach!r}`, not `room`, "
            f"`body` or a `rung_kinds` member ({list(RUNG_KINDS)}).")
    # B05.21 (T13 edit 2): WHAT THE ROOM DEMANDS -- a `difficulty_levels` member (`Fixtures.difficulty_ob` sizes it; no second ladder), required
    # of every row and refused outside the roster, as `verb_table.yaml`'s `difficulty:` is.
    standard = need("standard")
    _refuse_not_in(name, "standard", standard, DIFFICULTY_LEVELS, "a `rosters.yaml: difficulty_levels` member", repr_fn=list)
    # THE ONE KEY `19_PLAN.md` step 11 ADDS: required exactly when `disposal: declared`, and
    # refused otherwise -- both directions checked, on the same discipline `verb_table.yaml`'s
    # `requires_typed_note:` cross-check uses (a key present for no reason is as much a defect as
    # one absent for a reason). `19_PLAN.md` step 11's own falsifier: "a declared-disposal row
    # with no quorum fails the load."
    quorum = row.get("quorum")
    if close == "declared" and quorum is None:
        raise SystemExit(
            f"arrangements.yaml: {name!r} has `close: declared` and no `quorum:`. A declared "
            "disposal's tally IS the finding (`19_PLAN.md` step 11: \"the dissent key ... under a "
            "declared disposal it is the tally made visible\"), and a tally with no quorum is not "
            "a rule.")
    if close != "declared" and quorum is not None:
        raise SystemExit(
            f"arrangements.yaml: {name!r} has `quorum: {quorum!r}` and `close: {close!r}` -- "
            "`quorum` is `declared`'s own key; a row with a different close carrying one is a "
            "stray value nothing reads.")
    # roster-exempt: MECHANISM -- the return shape's own field names, not a second roster.
    return {
        "id": name, "rite": rite, "turns": tuple(turns), "authority": authority, "reason_lean": reason_lean,
        "admits": tuple(admits), "close": close, "bench_basis": bench_basis,
        "floor": floor_form, "floor_basis": floor_basis, "records_dissent": records_dissent,
        "venue_min_rank": venue_min_rank, "term_required": term_required,
        "appeal_basis": appeal_basis, "interposed": tuple(interposed),
        "disposes": disposes, "disposal_reach": disposal_reach,
        "quorum": quorum, "standard": standard,
    }


def _load() -> tuple[dict, dict, dict, dict, dict]:
    if not ARRANGEMENTS_YAML.exists():
        raise SystemExit(f"arrangements.yaml not found at {ARRANGEMENTS_YAML}")
    doc = load_yaml(ARRANGEMENTS_YAML.read_text(encoding="utf-8")) or {}
    kinds: dict = {}
    for r in doc.get("speech_kinds") or ():
        row = _load_speech_kind(r)
        if row["id"] in kinds:
            raise SystemExit(f"arrangements.yaml: speech_kinds id {row['id']!r} appears more than once")
        kinds[row["id"]] = row
    rites = _load_rites(doc.get("rites"))
    context = _load_context(doc.get("context"))
    disposal = _load_disposal(doc.get("disposal"))
    arrangements: dict = {}
    for r in doc.get("arrangements") or ():
        row = _load_arrangement(r, rites, disposal)
        if row["id"] in arrangements:
            raise SystemExit(f"arrangements.yaml: arrangement id {row['id']!r} appears more than once")
        arrangements[row["id"]] = row
    for rid, regime in context["regimes"].items():
        outlawed = [u for u in regime["unlawful"] if u not in rites and u not in arrangements]
        if outlawed:
            raise SystemExit(f"arrangements.yaml: `context` row 'regimes.{rid}' outlaws {outlawed}, which are neither a rite nor an "
                             f"arrangement id ({sorted(rites)}; {sorted(arrangements)}).")
    return rites, context, disposal, arrangements, kinds


RITES, CONTEXT, DISPOSAL, ARRANGEMENTS, SPEECH_KINDS = _load()


def abridged(row: dict) -> dict:
    """THE ABRIDGED FORM OF A ROW (V2 p2 §B; pure): a copy with one turn, the one move `argue` for the bearer (the side its rite says opens) and
    none for the other side, and `close: exchange` -- the one speech's own margin with the one addressed, who is seated by the builder as a
    hearer who decides (B24p.13), so no bench is needed (V2 p4 §K B3). The venue stays: `standard`, `reason_lean`, `admits`, `authority`,
    `floor` and `disposes` are the row's (an abridged speech keeps its room). It is the only place `exchange` is set."""
    rite = RITES[row["rite"]]
    moves = {side: (("argue",) if side == rite["bears"] else ()) for side in _RITE_SIDES}
    return {**row, "turns": (1, 1), "moves": moves, "close": "exchange"}


def arrangements_without_a_disposal_opener() -> list[str]:
    """C-1, AS A REPORT (see module docstring for why refusing is wrong today). Every arrangement
    id whose `disposes` kind has no opener naming `determine` -- or, for `close: consent` (was `disposal: mutual`), whose
    `oblige` has no opener at all -- in `data/verbs.py::_derive_openers_from_effects()`'s map.

    ⚠ A `disposal: mutual` row passes this check, because `oblige` has an opener (`_eff_oblige`, the
    joiner's own act). It reports only the seeded rows this check actually ASKS: a row disposing
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
        if row["close"] == "consent":
            if not openers.get("oblige"):
                out.append(name)
            continue
        kind = row["disposes"]
        if kind in _DISPOSES_LITERALS:
            continue                      # C-1 is about a TENURE kind's opener; `Record`, `none` and `yield` are none
        if "determine" not in (openers.get(kind) or ()):
            out.append(name)
    return out
