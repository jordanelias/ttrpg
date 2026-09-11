"""`season.data.rosters` -- the roster/table layer, extracted from `shape.py` (step 2 of the
decomposition, a PURE MOVE: no behaviour changed, only where the code lives).

Owns everything that loads or reads `rosters.yaml`: the closed-set/mapping readers (`roster`,
`roster_map`, `table`, `table_meta`), the roster constants bound at import (Jordan 2026-09-02 --
"I do not want definitions etc to be hardcoded"), and the two lookups that resolve canon's own
axes rather than the game's (`office_faction`, `title_domain`/`title_rank`).

Also owns `load_yaml` -- the one YAML reader every loader in this package shares, so a duplicate
mapping key raises instead of `safe_load`'s silent last-one-wins. It lives here rather than
beside `write_matrix.yaml`'s loader because `season.data.matrix` needs it and
`season/data/__init__.py` loads this module first for exactly that reason.
"""

from __future__ import annotations

from typing import Optional

from . import files
from ..gaps import Forbidden, Unspecified


# ---------------------------------------------------------------------------
# ONE YAML READER FOR EVERY DATA FILE THIS INSTRUMENT OWNS, AND IT REFUSES A DUPLICATE KEY.
#
# ⚠ `yaml.safe_load` SILENTLY KEEPS THE LAST OF TWO IDENTICAL KEYS. `verb_table.yaml` declared
# `writes_note` TWICE on `issue` and twice on `petition` -- once with Part E's transcribed cell
# (*"a Dispensation is not a state write -- §37.3"*, *"a Petition is created, not written"*) and
# once with the `W3` audit's correction of it. The transcription was discarded at load, in the one
# file whose whole purpose is to be a faithful capture of Part E, and nothing said so. Both cells
# are merged in the data now; this is the guard that fails on recurrence.
#
# ⚠ SEVERITY, STATED ACCURATELY: `writes_note` is not a field of `VerbRow`, so nothing in the fold
# read either cell -- THAT instance lost transcribed text in a capture whose purpose is fidelity to
# Part E, and changed no behaviour. What earns the guard under `CLAUDE.md` §0.1 pt 5 is the same
# class at the ROW level, which DID change behaviour: two `(Office, exists)` rows where the loader
# took the last, so gate behaviour depended on file order. That fix guarded rows only; this guards
# every mapping in every file.
# ---------------------------------------------------------------------------

def load_yaml(text: str):
    """The instrument's only YAML entry point. Raises on a duplicate mapping key.

    Built per call rather than at module scope because this file imports `yaml` inside the
    functions that need it, and a class body cannot wait for that."""
    import yaml as _y

    class _NoDuplicateKeys(_y.SafeLoader):
        pass

    def _no_dup(loader, node, deep=False):
        seen, out = set(), {}
        for k, v in node.value:
            key = loader.construct_object(k, deep=deep)
            if key in seen:
                raise ValueError(
                    f"duplicate key {key!r} at line {k.start_mark.line + 1} -- `safe_load` would "
                    f"silently keep the last, which is how two `writes_note` cells became one")
            seen.add(key)
            out[key] = loader.construct_object(v, deep=deep)
        return out

    _NoDuplicateKeys.add_constructor(
        _y.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dup)
    return _y.load(text, _NoDuplicateKeys)


# ===========================================================================
# THE ROSTERS, LOADED FROM DATA.
#
# ⚠ RULED BY JORDAN, 2026-09-02: *"I do not want definitions etc to be hardcoded"* … *"these must
# be easy to modify"* … *"that goes for all"*. Six rosters — 35 definitions — were literals in
# this file. They are `rosters.yaml` now, and changing one is a data edit.
#
# `roster()` RAISES on a name the file does not carry. That is §42.2's polarity rule applied to
# definitions: an absent roster is a REFUSAL, never an empty set, because an empty set silently
# makes every membership test false and every closed-set guard vacuous.
# ===========================================================================

ROSTERS_YAML = files.ROSTERS_YAML


def _load_rosters() -> tuple:
    import yaml as _y
    if not ROSTERS_YAML.exists():
        raise SystemExit(f"rosters.yaml not found at {ROSTERS_YAML}")
    doc = load_yaml(ROSTERS_YAML.read_text()) or {}
    return (doc.get("rosters") or {}), (doc.get("tables") or {})


_ROSTERS, _TABLES = _load_rosters()


def roster(name: str, ordered: bool = False):
    """A closed set, from `rosters.yaml`. `ordered=True` returns a tuple because the order is
    semantic (the strata resolve in sequence); otherwise a frozenset, so a caller cannot depend
    on an order the data does not promise."""
    r = _ROSTERS.get(name)
    if r is None:
        raise Unspecified(
            f"roster {name!r} is not in rosters.yaml", "rosters.yaml",
            needs="add the roster to the data file; do not inline it here",
            law="Jordan 2026-09-02 -- definitions are not hardcoded. An absent roster REFUSES; "
                "returning an empty set would make every membership test silently false")
    if "values" not in r:
        raise Unspecified(
            f"{name!r} is not a roster -- it has no `values:`", "rosters.yaml",
            needs="read a MAPPING with table(), a SET with roster()",
            law="rosters.yaml -- a roster is a SET and a table is a MAPPING. Reading one with the "
                "other's function raises, so the two shapes cannot be confused at a call site")
    vals = r["values"]
    # A roster may FORBID a member by name. `conviction_axes` forbids `exposure` bare, because
    # #353 `:1897` names it as three senses of one word; a data edit that added it would
    # otherwise reintroduce the collision silently, which is the whole failure mode this file
    # exists to prevent. The check is on the DATA, so it survives every route into the roster.
    for bad in (r.get("forbidden") or []):
        if bad in vals:
            raise Forbidden(
                f"roster {name!r} carries the forbidden member {bad!r}", "rosters.yaml",
                needs=f"spell the sense meant; {bad!r} is named as a collision, not a value",
                law=f"rosters.yaml -- {name}'s `forbidden:` list. A roster may bar a member by "
                    "name, and the bar is DATA so no code path can route around it")
    return tuple(vals) if (ordered or r.get("ordered")) else frozenset(vals)


def roster_map(name: str, key: str) -> dict:
    """A MAPPING that lives inside a roster row -- `titles.domains`, `contest_subsystems.prizes`.

    ⚠ THIS EXISTS BECAUSE TWO CALL SITES HAD ALREADY WRITTEN IT AS `_ROSTERS.get(x) or {}`, WHICH
    SILENTLY DEFAULTS. `rosters.yaml`'s own header states the polarity: *"a name the code asks for
    that is not here RAISES rather than defaulting, which is §42.2's polarity rule applied to
    definitions -- an absent roster is a refusal, never an empty set."* The bare-dict reads broke
    exactly that rule, and the consequence was not cosmetic: delete the `titles` key and
    `title_domain` returns `None` for every post, `target_is_title` becomes universally false, and
    `_req_revoke` SILENTLY REVERTS TO PURVIEW-FOR-EVERYTHING -- the reading Jordan's fourth
    message exists to forbid. A guard that fails open into the ruled-against behaviour.

    One owner, so a third mapping inherits the refusal by existing (§8). Found by the
    governance-canon adversarial pass."""
    r = _ROSTERS.get(name)
    if r is None:
        raise Unspecified(
            f"roster {name!r} is not in rosters.yaml", "rosters.yaml",
            needs="add the roster to the data file; do not inline it here",
            law="Jordan 2026-09-02 -- definitions are not hardcoded. An absent roster REFUSES; "
                "returning an empty mapping would make every lookup silently answer `None`")
    m = r.get(key)
    if not isinstance(m, dict):
        raise Unspecified(
            f"roster {name!r} has no mapping `{key}:`", "rosters.yaml",
            needs=f"give {name!r} a `{key}:` mapping, or read it with roster()/table()",
            law="rosters.yaml -- the mapping is the DEFINITION. An absent one cannot be "
                "substituted by an empty dict without inverting the answer it gives")
    return dict(m)


def table(name: str) -> dict:
    """A MAPPING from `rosters.yaml`'s `tables:`, returned as `{outer: {inner: float}}`.

    Sparse: a pair the data does not list reads as `default_cell`, which is NOT the same claim as
    an all-zero table -- `alignment` may be sparse and may not be uniformly zero, and the two are
    checked separately below."""
    t = _TABLES.get(name)
    if t is None:
        if name in _ROSTERS:
            raise Unspecified(
                f"{name!r} is a roster, not a table", "rosters.yaml",
                needs="read a SET with roster(), a MAPPING with table()",
                law="rosters.yaml -- a roster is a SET and a table is a MAPPING")
        raise Unspecified(
            f"table {name!r} is not in rosters.yaml", "rosters.yaml",
            needs="add the table to the data file; do not inline it here",
            law="Jordan 2026-09-02 -- definitions are not hardcoded. An absent table REFUSES")
    return {outer: dict(inner) for outer, inner in (t.get("cells") or {}).items()}


def table_meta(name: str) -> dict:
    """The table's own declarations -- `default_cell`, `row`, `keys`. Read rather than assumed, so
    a data edit that changes the sparse default cannot leave a stale constant in a body."""
    return {k: v for k, v in (_TABLES.get(name) or {}).items() if k != "cells"}


TENURE_KINDS = roster("tenure_kinds")
# `release`'s domain, DERIVED ONCE. `04_CODE_ARCHITECTURE.md` PART D row 15 states it as
# `tenure_kinds \ {contain}`, and `verb_table.yaml` DECLARES the same set as a column so the
# loader has something to disagree with -- declaration there, derivation here, and loader
# invariant 6 compares them. `contain` is the one kind whose end is a MOVE rather than a release:
# `_eff_move` closes the old leg and opens the new one, so a releasable `contain` would let a
# person leave a place for nowhere.
# ⚠ IT LIVES BESIDE `TENURE_KINDS` BECAUSE THE DERIVATION MUST LIVE ONCE (§8). It was written
# twice -- once in `data/verbs.py`'s loader and once in `loop/predicates.py` -- and the
# declared-there/derived-here argument is satisfied by ONE derivation, not two. Today the
# exclusion is a single member so drift would be cheap; the moment it is not, two code sites would
# have to move together and only one of them is guarded. Found by the `release` adversarial pass.
RELEASABLE_KINDS = frozenset(TENURE_KINDS) - {"contain"}
# `U1`: verb -> the capability key its contested roll draws dice from. A MAPPING inside a roster
# row, read through `roster_map` so an absent roster refuses rather than defaulting to `{}` -- the
# polarity that function exists to hold. A verb with no row falls through to `pool_default` inside
# the wrapper, which is the `assumption` grade's own reading (`08 §3`) and not a refusal.
VERB_CAPABILITY = roster_map("verb_capability", "values")
RUNG_KINDS = roster("rung_kinds", ordered=True)
REMIT_ACTS = roster("remit_acts")
WITNESS_CHANNELS = roster("witness_channels", ordered=True)
CLAIM_SOURCES = roster("claim_sources")
STRATA = roster("strata", ordered=True)
CONVICTION_AXES = roster("conviction_axes")
QUESTION_SOURCES = roster("question_sources", ordered=True)
PERSON_PREDICATES = roster("person_predicates")
VIEW_BUILDER_RULES = roster("view_builder_rules")
QUESTION_AGGREGATION = roster("question_aggregation", ordered=True)
SCENE_PACKING_RULES = roster("scene_packing_rules")
CLAIM_SUBJECT_RULES = roster("claim_subject_rules")
# `W-B` / `H-122`. WHO RECEIVES A CLAIM MINTED FROM WHAT THE FOLD READ. Bound at import
# like every other roster, and for the reason `TITLE_DOMAINS` records below: an unbound
# roster is the one whose absence goes unnoticed.
OBSERVATION_DEPOSIT_MODES = roster("observation_deposit_modes")
# `W-E`. THE THREE BANDS PERSONAL COMBAT CAN DISTINGUISH, and HOW MUCH BODY A WOUND COSTS. Bound
# here with every other roster rather than beside their reader in the S39 block below, because
# that is where an absent roster's refusal is guaranteed to fire (`TITLE_DOMAINS`' lesson, above).
# ⚠ `ordered=True` AND UNPACKED POSITIONALLY: the order is SEVERITY, worst first, and the roster's
# own note says so. These are NOT the ladder's four bands -- combat is exempt from the ladder by
# Jordan's 2026-09-03 ruling, and `degree_of`'s margin branch calls the tree's owner for those.
COMBAT_BANDS = roster("combat_degree_bands", ordered=True)
FELLED, WOUNDED, UNTOUCHED = COMBAT_BANDS
WOUND_HARM_MODELS = roster("wound_harm_models")
# ⚠ BOUND AT IMPORT LIKE THE OTHERS, AND THAT IS THE POINT. `titles` was the ONE roster read
# lazily through a bare `_ROSTERS.get(...) or {}`, so it alone got no existence refusal -- and
# because `_req_revoke` fails OPEN into purview-for-everything when the mapping is empty, the one
# unbound roster was the one whose absence silently restores a ruled-against behaviour.
TITLE_DOMAINS = roster_map("titles", "domains")

# ⚠ THE OFFICE'S THREE CANON AXES -- `H-99`, and they are BOUND AT IMPORT for the reason the
# comment above gives: an unbound roster is the one whose absence goes unnoticed. Jordan asked
# *"does the office schema include faction belonging, scale of office, type of office, etc?"* and
# it did not. `FACTIONS` is the belonging, `BODY_FACTION`/`BODY_FUNCTION` the type. SCALE is
# deliberately not here -- an office's scale is the RUNG it is seated at, which `Office.seat`
# already carries; a body does not fix a rung.
#
# ⚠ SOURCED UNDER THE 2026-09-02 PRECEDENCE RULING, WHICH `rosters.yaml`'s header states in full:
# `systems/world/` is CANON for identity/names/organizations, `systems/factions/` near-canon only
# where it concerns a faction's identity AND world is silent, `research/` reference. The first
# version of these rosters was sourced from the near-canon tier and carried a name that tier
# itself calls *"institutional infrastructure, not a faction"*.
FACTIONS = roster("factions")
BODY_FACTION = roster_map("office_bodies", "faction")
BODY_FUNCTION = roster_map("office_bodies", "function")
ROLE_TEMPLATE_OF = roster_map("role_templates", "by_faction")


def office_faction(body: str | None, declared: str | None) -> str:
    """The faction an office belongs to: DERIVED from its canonical body where it has one,
    authored where canon gives its faction no organ.

    ⚠ ONE AUTHORED FIELD, TWO DERIVED, AND A DISAGREEMENT REFUSES. `office_bodies` already binds
    every body to its faction, so an overlay that names a `body` need not -- and may not -- name a
    different faction. A `Cardinal of Justice` seated in the Crown is a mis-seating, and it is
    exactly the kind of error a re-scaling pass makes at volume; without this it would be silent
    and would then read as canon.

    ⚠ AN ABSENT BODY IS NOT AN ERROR. The Restoration Movement's authority is *"informal"*
    (`worldbuilding_v30.md` §8) and canon gives it no organ, so such a case authors `faction`
    directly. That is a real gap in canon, carried as one rather than filled."""
    if body is not None:
        if body not in BODY_FACTION:
            raise Unspecified(
                f"{body!r} is not a canonical body", "rosters.yaml -- office_bodies",
                needs="name a body from `systems/world/`, or drop `body` and author `faction`",
                law="Jordan 2026-09-02 -- systems/world is canon for organizations. Inventing a "
                    "body here would be indistinguishable from canon to the next session")
        derived = BODY_FACTION[body]
        if declared is not None and declared != derived:
            raise Forbidden(
                f"office body {body!r} belongs to {derived!r}, not {declared!r}",
                "rosters.yaml -- office_bodies",
                needs="drop the `faction:` field; it derives from `body:`",
                law="H-99 -- one authored field, two derived. A body's faction is canon's, and a "
                    "disagreement is a mis-seating rather than a second opinion")
        return derived
    if declared is None:
        raise Unspecified(
            "an office names neither a `body` nor a `faction`", "the case overlay",
            needs="name a canonical body, or the faction directly where canon gives it no organ",
            law="H-99 -- an office belongs to something. §42.2's polarity rule: no evidence of "
                "belonging is a refusal, never a default faction")
    if declared not in FACTIONS:
        raise Unspecified(
            f"{declared!r} is not a canonical faction", "rosters.yaml -- factions",
            needs="use a faction named in `systems/world/`",
            law="Jordan 2026-09-02 -- systems/world is canon for identity and names")
    return declared


# `title_domain`/`title_rank` -- RELOCATED FROM shape.py's governance slice (step 2). Both
# are pure roster reads (`TITLE_DOMAINS`, `RUNG_KINDS`), not verbs, so they belong beside
# the rosters they read rather than beside the governance verbs that call them.
def title_domain(post: Optional[str]) -> Optional[str]:
    """The rung kind a title governs, from `rosters.yaml: titles`. `None` for a post that is not
    a title — a Dicastery is an office, not a rank."""
    return TITLE_DOMAINS.get(str(post or ""))


def title_rank(post: Optional[str]) -> int:
    """A title's rank as its domain's ordinal in `rung_kinds`. Higher governs wider.

    ⚠ RANK IS NOT A SECOND LADDER. `rung_kinds` is already ordered person → realm, and each title
    names the rung kind it governs, so the ordering falls out of a roster that exists rather than
    from a number somebody assigns. `-1` for a non-title."""
    dom = title_domain(post)
    return -1 if dom is None else (list(RUNG_KINDS).index(dom)
                                              if dom in RUNG_KINDS else -1)
