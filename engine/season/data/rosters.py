"""`season.data.rosters` -- the roster/table layer, extracted from `shape.py` (step 2 of the
decomposition, a PURE MOVE: no behaviour changed, only where the code lives).

A ROSTER, in this repo, is a closed set of allowed values that a loader validates against
(`rosters.yaml` is the file; the `roster()` reader below is the check).

Owns everything that loads or reads `rosters.yaml`: the closed-set/mapping readers (`roster`,
`roster_map`, `table`, `table_meta`), the roster constants bound at import (Jordan 2026-09-02 --
"I do not want definitions etc to be hardcoded"), and the two lookups that resolve canon's own
axes rather than the game's (`office_faction`, `title_domain`).

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
    rosters = doc.get("rosters") or {}
    # ⚠ BOTH KEYS IS A DECLARED-BUT-UNREAD `values:`, AND THE CHECK IS AT LOAD FOR A MEASURED
    # REASON. `04 §B.13` ID-12 puts the loader's cross-validation at load, "not at the first act
    # that would have hit it", and this rule proves why: it first shipped inside `roster()`, where
    # it only ever saw rows something CALLED `roster()` on. `pursuits` is not one of those --
    # its runtime route is the direct `PURSUITS` import below, so the row that MOTIVATED the
    # rule was the one row the rule could not reach. Driving the loop with both keys planted on it
    # ran clean and emitted a content hash; planted on `pursuit_axes`, which IS read through
    # `roster()`, it refused. Here it fires on every row whatever reads it, or nothing does.
    for _n, _r in rosters.items():
        if not isinstance(_r, dict):
            continue
        # ⚠ ONE RULE OVER EVERY POINTER, NOT ONE PER POINTER. `from_names:` joined
        # `from_descriptor:` on 2026-09-16 and `from_roster:` on 2026-09-19; spelling the refusal
        # once per pointer is how they would drift apart, which is the defect this refusal is about.
        # roster-exempt: these are THIS LOADER'S OWN YAML GRAMMAR -- the key names a row may carry
        # to name its owner -- not a definition the game resolves from. Moving them into
        # `rosters.yaml` is circular by construction: `roster()` would have to read the file to
        # learn how to read the file. It fails the data-file test in the direction that exempts:
        # changing this list changes how the LOADER works, never what the game is.
        _ptrs = [k for k in ("from_descriptor", "from_names", "from_roster") if k in _r]
        if len(_ptrs) > 1:
            raise Unspecified(
                f"roster {_n!r} carries {len(_ptrs)} owner pointers ({', '.join(_ptrs)})",
                "rosters.yaml",
                needs="keep the one that owns these members and delete the rest",
                law="ED-IN-0230 -- a pointed-at roster has ONE owner. Two pointers is two owners "
                    "with a read-order tiebreak, which is worse than a copy because it looks "
                    "single-owned")
        if _ptrs and "values" in _r:
            raise Unspecified(
                f"roster {_n!r} carries BOTH `{_ptrs[0]}:` and `values:`", "rosters.yaml",
                needs="delete one -- the pointer if this roster owns its members, the `values:` "
                      "if the owner is the registry it points at",
                law="ED-IN-0230 -- a pointed-at roster has ONE owner. The pointer wins at read "
                    "time, so a `values:` beside it is never read and never noticed, which is "
                    "exactly the second copy the pointer was introduced to prevent")
    return rosters, (doc.get("tables") or {})


_ROSTERS, _TABLES = _load_rosters()

OFFICES_YAML = files.OFFICES_YAML


def _load_offices() -> dict:
    """`engine/season/offices.yaml`, parsed once at import -- world-gen content: the governance
    ladder's titles (folded from `rosters.yaml: titles`, plan position `8a`, `13d-i` item 5) and
    the 29 authored seats. Not a `rosters.yaml` row, so it does not go through `_load_rosters`'s
    `from_descriptor`/`from_names`/`from_roster` pointer machinery -- it is a sibling content file
    with its own top-level shape (`meta:`, `titles:`, `seats:`), read the same way
    `harness/governance_spine.py::spec` reads `governance_spine.yaml`: through this module's own
    `load_yaml` (the duplicate-key refusal), never a bare `yaml.safe_load`.

    ⚠ SAME REFUSAL SHAPE AS THE ROSTER IT REPLACED. `TITLE_DOMAINS`'s own comment (below) records
    why `titles` was bound at import rather than read lazily: an absent or empty mapping fails OPEN
    into `_req_revoke`'s old purview-for-everything default, which `ED-IN-0256` superseded but a
    silently-empty `title_domain` would still misfire on today's title-in-a-body refusal
    (`state/carriers.py::refuse_a_title_in_a_body`). This file inherits that refusal rather than
    dropping it because the source moved."""
    if not OFFICES_YAML.exists():
        raise SystemExit(f"offices.yaml not found at {OFFICES_YAML}")
    doc = load_yaml(OFFICES_YAML.read_text()) or {}
    domains = (doc.get("titles") or {}).get("domains")
    if not isinstance(domains, dict) or not domains:
        raise Unspecified(
            "offices.yaml has no `titles: domains:` mapping, or it is empty", "offices.yaml",
            needs="give `titles:` a `domains:` mapping",
            law="carried from `rosters.yaml`'s former `TITLE_DOMAINS` refusal at the `8a` fold -- "
                "an absent or empty mapping fails OPEN into a behaviour Jordan ruled against")
    if not doc.get("seats"):
        raise Unspecified(
            "offices.yaml has no `seats:` list, or it is empty", "offices.yaml",
            needs="give `seats:` at least one row",
            law="`04_CODE_ARCHITECTURE.md` §B.13 ID-12 -- a declared-but-empty section is the "
                "defect this file's own loader refuses, applied to its own top level")
    # A ROW ID IS UNIQUE, CHECKED HERE AND NOWHERE ELSE. `populated.build_realm` keys the seats it
    # matched by row id (`authored[row["id"]]`) and skips a row already in that dict, so a second row
    # under one id was collapsed without a sound -- and the minted-id guard runs after that skip.
    ids = [row.get("id") for row in doc["seats"] if isinstance(row, dict)]
    repeated = sorted({i for i in ids if i is not None and ids.count(i) > 1}, key=str)
    if repeated:
        raise Unspecified(
            f"offices.yaml `seats:` carries more than one row under the id(s) {repeated}",
            "offices.yaml -- seats",
            needs="one row per `id`",
            law="`offices.yaml: meta: rule` -- one seat = one row; a repeated id is collapsed "
                "by the seat index without a sound")
    return doc


_OFFICES_DOC = _load_offices()
# Every authored seat, in file order. `harness/populated.py` is the one caller (the `8a` overlay);
# read directly rather than through a second index for anything that must see BOTH of NPC-020's
# two rows (`off_king`, `off_duke_valorsmark`) -- `OFFICES_BY_HOLDER` below deliberately is not
# that reader.
OFFICES_SEATS = tuple(_OFFICES_DOC.get("seats") or ())
# case id -> every seat row that names it as `holder`, so a caller matches on POST rather than
# guessing which of a multi-seat holder's rows applies (NPC-020 holds two). A list, not a single
# row, because `roster_map`'s single-mapping shape would silently keep the LAST of NPC-020's two
# and make the choice invisible at the call site -- the same defect `load_yaml`'s duplicate-key
# refusal exists to catch one layer up, avoided here by not building a lossy map at all.
OFFICES_BY_HOLDER: dict = {}
for _seat in OFFICES_SEATS:
    OFFICES_BY_HOLDER.setdefault(_seat["holder"], []).append(_seat)
del _seat


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
    # `from_descriptor:` — THE ROW POINTS AT THE SINGLE OWNER INSTEAD OF COPYING IT (ED-IN-0230).
    # A roster whose definition belongs to `references/descriptor_registry.yaml` names the block
    # and carries no `values:`, so there is exactly one place to edit and no second list to drift.
    # This is the `conviction_roster` shape made general: that row was handled by importing
    # `PURSUITS` directly, which works but SKIPS the `forbidden:` bar below — and that bar is
    # load-bearing on `pursuit_axes` (#353 `:1897`, the Exposure collision). Routing through
    # here keeps the data-side bar on a pointed-at roster, which a direct import could not.
    if "from_descriptor" in r:
        # ⚠ THE BOTH-KEYS REFUSAL IS AT LOAD, IN `_load_rosters`, NOT HERE. It lived here first and
        # could only see rows a caller reached -- see that function for what that missed.
        from engine.substrate import descriptors as _desc
        block = _desc.block(r["from_descriptor"])
        if not block or not block.get("names"):
            raise Unspecified(
                f"roster {name!r} points at descriptor block {r['from_descriptor']!r}, which is "
                f"absent or has no `names`", "references/descriptor_registry.yaml",
                needs=f"add {r['from_descriptor']}.names, then "
                      "`python tools/export_descriptors.py --build`",
                law="ED-IN-0230 -- a pointed-at roster REFUSES when its owner is missing. Falling "
                    "back to a local literal is how the two axis lists drifted in the first place")
        vals = list(block["names"])
    elif "from_names" in r:
        # `from_names:` — the same pointer aimed at `references/names_index.yaml`, whose rows carry
        # a `token_class:`. A roster of NAMES (factions, clocks, the npc cast) belongs to the naming
        # index, not the descriptor registry: `names_index.yaml` has called itself *"the one place a
        # definition's name lives"* since 2026-06-28, and its canonical/alias pair is what resolves
        # `Church` to `Church of Solmund`. Pointing here rather than copying is what lets a naming
        # ruling reach `systems/` — which, MEASURED on 2026-09-16, no register previously did.
        from engine.substrate import names as _names
        vals = list(_names.of_class(r["from_names"]))
        if not vals:
            raise Unspecified(
                f"roster {name!r} points at token_class {r['from_names']!r}, which no row in the "
                f"naming index carries", "references/names_index.yaml",
                needs=f"set `token_class: {r['from_names']}` on the rows that belong to it, then "
                      "`python tools/export_names.py`",
                law="ED-IN-0230 -- a pointed-at roster REFUSES when its owner is empty. Returning "
                    "an empty set would be the silent-false `rosters.yaml`'s own header forbids")
    elif "from_roster" in r:
        # `from_roster:` — the same pointer aimed at a SIBLING ROW IN THIS FILE, for the case where
        # one roster's members ARE another's. ⚠ IT EXISTS BECAUSE `remit_default` SPELLED
        # `remit_acts`' SIX VALUES A SECOND TIME, and a test pinned the two equal — so adding a
        # seventh remit act meant editing two rows, or reddening a test for a reason unrelated to
        # the edit (§0.05 cl.3, "never keep a second copy"). A row that later needs to NARROW the
        # set replaces this pointer with its own `values:`, which is an explicit edit rather than a
        # silent divergence.
        src = _ROSTERS.get(r["from_roster"])
        if not isinstance(src, dict) or not src.get("values"):
            raise Unspecified(
                f"roster {name!r} points at roster {r['from_roster']!r}, which is absent or "
                f"carries no `values:`", "rosters.yaml",
                needs=f"give {r['from_roster']} its members, or point somewhere that has them",
                law="ED-IN-0230 -- a pointed-at roster REFUSES when its owner is missing. Falling "
                    "back to a local literal is how the two lists drifted in the first place")
        if r["from_roster"] == name:
            raise Unspecified(
                f"roster {name!r} points at itself", "rosters.yaml",
                needs="point at the roster that owns these members",
                law="ED-IN-0230 -- a pointer names ANOTHER row's ownership, never its own")
        vals = list(src["values"])
    elif "values" not in r:
        raise Unspecified(
            f"{name!r} is not a roster -- it has no `values:`", "rosters.yaml",
            needs="read a MAPPING with table(), a SET with roster()",
            law="rosters.yaml -- a roster is a SET and a table is a MAPPING. Reading one with the "
                "other's function raises, so the two shapes cannot be confused at a call site")
    else:
        vals = r["values"]
        # ⚠ PRESENT BUT EMPTY IS THE SAME DEFECT AS ABSENT, AND THIS FILE'S HEADER ALREADY SAID
        # SO WITHOUT ENFORCING IT: *"an absent roster is a REFUSAL, never an empty set, because
        # an empty set silently makes every membership test false and every closed-set guard
        # vacuous"*. `contest_subsystems` carried `values: []` from its authoring until
        # 2026-09-16 and `roster()` handed back an empty frozenset for it -- the polarity stated
        # in prose and not in code. The header is the law; this is the line that applies it.
        if not vals:
            raise Unspecified(
                f"roster {name!r} carries an EMPTY `values:`", "rosters.yaml",
                needs="give the roster its members, or delete the `values:` key if the row's "
                      "content is a mapping read with roster_map()",
                law="rosters.yaml's header -- an empty set makes every membership test silently "
                    "false, so it REFUSES exactly as an absent roster does")
    # A roster may FORBID a member by name. `pursuit_axes` forbids `exposure` bare, because
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
    (That consequence is history since `13d-i`, 2026-09-26, which deleted `target_is_title`; the
    refusal still guards every mapping read here.)

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


def faction_prop_id(name: str) -> str:
    """`'Crown'` -> `'fac_crown'`. THE ONE OWNER OF THE FACTION-ID RELATION.

    ⚠ IT HAD NO OWNER UNTIL 2026-09-16, AND THAT COST A SILENTLY EMPTY QUERY. `populated.py`
    formed the id inline as `f"fac_{_slug(fac_name)}"`; `queries/world_q.py: leaders()` recovered
    the NAME from the other end by reading `Proposition.subject`. That worked while `subject` WAS
    the faction name -- and then the creed commit made `subject` the LEADER'S PERSON ID for every
    faction that has a creed, while leaving the name in `value`. One relation, two guesses, and the
    reader kept reading a field whose meaning had moved underneath it.

    MEASURED at `build_realm(0)` before the repair: `leaders()` returned `[]` for Crown, Church of
    Solmund, Hafenmark and Varfell -- all four factions that hold seats -- making 19 of 19 occupied
    offices invisible. It is the §0.1 pt 1 shape exactly: a getter's source changed while its
    readers went on reading the old one, and the wrong answer (`[]`) is a PLAUSIBLE answer, so
    nothing raised.
    """
    return "fac_" + "".join(c if c.isalnum() else "_" for c in str(name).lower()).strip("_")


# The prefix of a territory RUNG id, and nothing else. Named so the relation below has one spelling.
_TERRITORY_RUNG_PREFIX = "terr_"  # [JUSTIFIED: an id SPELLING, not a game value -- the territory-rung half of the faction-id relation's shape above]


def territory_rung_id(tid: str) -> str:
    """`'T9'` -> `'terr_T9'`. THE ONE OWNER OF THE TERRITORY-RUNG-ID RELATION, `faction_prop_id`'s
    shape one row down: `harness/populated.py` mints a `territory` Rung per geography row
    (`systems/settlements/valoria_geography_v30.yaml: provinces`, whose rows are territories) and
    the battle path (`seam/wrappers/mass_battle.py`, plan position `20-iv`) has to get from that
    Rung back to the geography row `terrain.py::terrain_row_for_territory` is keyed on. Before
    `20-iv` the builder spelled the id inline at four sites and nothing read it back, so the
    relation had no owner because it had no second reader; it has one now, and two spellings of
    one relation is how `leaders()` went silently empty (the docstring above)."""
    return _TERRITORY_RUNG_PREFIX + str(tid)


def territory_id_of(rung_id: "str | None") -> "str | None":
    """The inverse of `territory_rung_id`: `'terr_T9'` -> `'T9'`, and `None` for an id that does not
    carry the prefix. It reads the SPELLING, so it cannot tell a minted id from a hand-spelled one
    (`harness/scarce.py`'s `terr_march` is the case: `territory_id_of` answers `'march'`, a territory
    no geography row backs). Whether the answer is a real geography row is NOT asked here -- that is
    `terrain_row_for_territory`'s own question, and it answers an unknown territory with its
    no-modifier fallback rather than a refusal."""
    s = str(rung_id or "")
    if not s.startswith(_TERRITORY_RUNG_PREFIX):
        return None
    return s.removeprefix(_TERRITORY_RUNG_PREFIX) or None


def require_member(value, roster, what: str, where: str, law: str, needs: str = "") -> None:
    """THE ROSTER-MEMBERSHIP REFUSAL, IN ONE PLACE. Ten call sites had it check-for-check.

    The same shape recurred across `epistemic`, `decision/`, `loop/` and this file: test a runtime
    value against a bound roster, and on a miss raise `Unspecified` naming the hole, the accepted
    members and the law. `data/verbs._check_sparse_table` made this move already for the two
    sparse-table loaders and states the split it used -- centralise the mechanical check, leave
    the LAW STRINGS per-caller "because what a violation means differs by table". Same split here:
    `what`, `where` and `law` stay the caller's words; the test and the rendering come here.

    ⚠ THE RENDERING IS THE PART THAT WAS WORTH CENTRALISING, and it was not a style difference.
    An ORDERED roster is a tuple and its order is semantic, so it renders with `list()`; an
    unordered one is a frozenset and renders `sorted()` so the message is stable. Nine sites chose
    between those by hand and nine chose correctly -- measured, `QUESTION_AGGREGATION` and
    `ALIGNMENT_SWEEP` are the tuples and are exactly the two that used `list()`. Nine correct
    independent guesses is not a rule; this is. A caller needing prose instead passes `needs=`.
    """
    if value in roster:
        return
    raise Unspecified(
        what, where, law=law,
        needs=needs or f"one of {list(roster) if isinstance(roster, tuple) else sorted(roster)}")


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
# ⚠ TWO MEMBERS SINCE PLAN POSITION `19c`, FOR `contain`'s OWN REASON: `reside` (where a person
# lives) ends by a relocation too -- `_eff_migrate` closes the old edge as it opens the new -- and a
# releasable residence would let a person leave a home for nowhere. Still ONE derivation (this
# line): `verb_table.yaml`'s declared `release` domain is unchanged, because the six kinds it lists
# are exactly what remains, and loader invariant 6 compares the two.
RELEASABLE_KINDS = frozenset(TENURE_KINDS) - {"contain", "reside"}
# `holonic §15`'s DOMAIN and CODOMAIN for the `hold` row, read by `World._refuse_bad_hold`.
# Rostered rather than inlined at the guard (Jordan, 2026-09-02 -- *definitions are not
# hardcoded*), so widening `hold` to a new carrier is a data edit and an absent roster
# REFUSES instead of defaulting to a silent pass.
HOLD_OBJECT_KINDS = roster("hold_object_kinds")
HOLD_SUBJECT_KINDS = roster("hold_subject_kinds")
# Plan position `15` -- `ARCH §B.5`'s fold: `Petition` and `Dispensation` are KINDS of `Record`, and
# each kind declares the EXACT key set of its `subject_matter` (r2 `05`'s ⊕L35, refused in
# `Record.__post_init__`). `RECORD_KINDS` is the member set; `RECORD_KIND_KEYS` is the mapping,
# read through `roster_map` so an absent row refuses rather than answering `{}`; `RECORD_CONTENT`
# is how a mint reads the keys off an act and what the deposit rule names the claim.
RECORD_KINDS = roster("record_kinds")
RECORD_KIND_KEYS = {k: tuple(v or ()) for k, v in roster_map("record_kinds", "values").items()}
RECORD_CONTENT = roster_map("record_kinds", "content")
# ⚠ ONE STEM READS BOTH VOCABULARIES, SO THEY MAY NOT SHARE A WORD. `exists:<kind>`
# (`queries/world_q.py::WorldReader.read`) answers a `tenure_kinds` member as a live EDGE and a
# `record_kinds` member as a Record OF THAT KIND; a word in both rosters would be answered by
# whichever branch is tested first and the other reading would be silently unreachable. Refused
# at load, where the two rosters first meet, rather than at the first act that asks.
if RECORD_KINDS & TENURE_KINDS:
    raise Unspecified(
        f"`record_kinds` and `tenure_kinds` share {sorted(RECORD_KINDS & TENURE_KINDS)}",
        "rosters.yaml -- record_kinds",
        needs="rename one; each word the `exists:` stem reads must mean one thing",
        law="`queries/world_q.py::WorldReader.read`'s `exists` branch reads both rosters; a "
            "shared word is two questions spelled one way")
# `U1`: verb -> the capability key its contested roll draws dice from. A MAPPING inside a roster
# row, read through `roster_map` so an absent roster refuses rather than defaulting to `{}` -- the
# polarity that function exists to hold. A verb with no row falls through to `pool_default` inside
# the wrapper, which is the `assumption` grade's own reading (`08 §3`) and not a refusal.
VERB_CAPABILITY = roster_map("verb_capability", "values")
RUNG_KINDS = roster("rung_kinds", ordered=True)


def _check_scale_of_rung(mapping: dict, kinds) -> None:
    """`SCALE_OF_RUNG`'s domain must be EXACTLY `RUNG_KINDS` -- a function and not an inline `if`,
    so the test can plant a drifted mapping and watch it refuse (`CLAUDE.md` §0.1 pt 3: a load
    check with no falsifier cannot be told from one that never runs)."""
    if set(mapping) != set(kinds):
        raise Unspecified(
            f"`scale_of_rung` covers {sorted(mapping)}, and `rung_kinds` is {sorted(kinds)}",
            "rosters.yaml -- scale_of_rung",
            needs="give every rostered rung kind a scale, and give every scale a rostered rung "
                  "kind",
            law="`04 §B.13` ID-12 -- a declared row that reaches no code, or a key the domain "
                "does not have, is the defect the loader's cross-validation exists to catch")


# Plan position `20-ii` (U9/R-04). A rung_kind -> one of canon's five scales (`rosters.yaml:
# scale_of_rung`'s own note states, BEFORE this mapping, which of the two problems it solves and
# which it does not -- read that note before touching either roster row). Bound beside
# `RUNG_KINDS`, its domain, for the identical reason `SITE_KINDS` is bound beside it above.
SCALE_OF_RUNG = roster_map("scale_of_rung", "scale")
_check_scale_of_rung(SCALE_OF_RUNG, RUNG_KINDS)
# Plan position `24e`: the kinds `build` may make -- a works' `plan` is a Site only if it is one of
# these (`loop/effects.py::_eff_build`). Bound beside `RUNG_KINDS`, `found`'s twin roster, rather
# than read by a bare `roster(...)` at the one call site. `data/fixtures.py` reads the same row for
# its both-direction table checks, so a kind here always has a wear and a band-floor row.
SITE_KINDS = roster("site_kinds")
REMIT_ACTS = roster("remit_acts")
# `data/arrangements.py`'s four content rosters -- plan position `18` (PROC-A). Bound here beside
# their nearest kin (`RUNG_KINDS`/`REMIT_ACTS`, both read by the same loader) rather than left to a
# bare `roster(...)` call at the one call site, on this file's own established convention.
INTERPOSITION_KINDS = roster("interposition_kinds")
GENRES = roster("genres")
PROOFS = roster("proofs")
LADDER_RUNGS = roster("ladder_rungs", ordered=True)
# ED-IN-0256 rulings (2) and (3), plan position `13d-i`: HOW A SEAT IS FILLED and WHO MAY STRIP IT.
# Bound at import for `TITLE_DOMAINS`' reason below -- an unbound roster is the one whose absence
# goes unnoticed. `Office.__post_init__` refuses a declared basis off either; `state/gate.py`'s
# `has_conferral_basis`/`REVOCATION_RULES` read them (moved there by G3; CORRECTED, antagonist
# pass, 2026-09-27 -- this said `loop/predicates.py`).
CONFERRAL_BASES = roster("conferral_bases")
REVOCATION_BASES = roster("revocation_bases")
# Plan position `17a` (r2 `05` RULED (b), `ARCH F.17`): HOW A SEAT TAKES ON THOSE WHO SERVE IT, the
# third basis beside the two above and bound the same way. `Office.__post_init__` refuses a value
# off it; `loop/predicates.py::_req_oblige` admits an `oblige` only to a seat whose `binds` is on it.
BINDS_BASES = roster("binds_bases")
# ⚠ A TESTING FIXTURE, NOT CANON — see the roster's own note. Jordan, 2026-09-18: "for testing
# purposes for now, just build out a generic remit". It fills an EMPTY remit and never overwrites
# a grounded one.
REMIT_DEFAULT = roster("remit_default")


def remit_or_default(declared) -> list[str]:
    """A seat's remit, or the TESTING default when it declares none — the ONE owner of that rule.

    ⚠ IT FILLS AN EMPTY REMIT AND NEVER OVERWRITES A DECLARED ONE. The three grounded overlays
    (NPC-008/033/038) keep exactly what their case text supports; `remit_default` reaches only the
    seats that carry `[]`, which was 16 of the populated realm's 19 when this landed. ⚠ SINCE
    `13d-iii` (2026-10-01) IT REACHES ONE REALM SEAT: every seat with an `offices.yaml` row takes
    the row's remit through `authored_remit` (below), so only the seat no row authors
    (`off_npc_084`), the spine and the fixtures still fall through to this default.

    ⚠⚠ THE DEFAULT IS NOT CANON — see `rosters.yaml: remit_default`'s own note for why a
    transparently-wrong placeholder is the safe shape and what replaces it (per-POST remits, which
    need `Office.post` normalised first). Jordan, 2026-09-18: *"for testing purposes for now, just
    build out a generic remit"*.

    ⚠ NO FILTERING, DELIBERATELY. `corpus_run`'s own comment records why: a rev-1 filter
    `[a for a in ... if a in REMIT_ACTS]` dropped an unrecognised remit act on the floor, *"a quiet
    default sitting underneath `Office.__post_init__`'s loud one"*. A declared remit passes through
    untouched and `Office.__post_init__` refuses it loudly if it is off-roster.
    """
    declared = list(declared or [])
    # ⚠ `sorted`, NOT `list`. `REMIT_DEFAULT` is a frozenset, so `list()` gave a PER-PROCESS order
    # and `build_realm(0).content_hash()` returned a different digest on every run — measured 3/3
    # distinct under three `PYTHONHASHSEED`s, 3/3 identical without this. Gameplay was unaffected,
    # but R4 byte-identical replay is not, and a determinism break that only shows across processes
    # is exactly the kind a same-process self-comparison cannot see. Found by `/code-review`.
    return declared if declared else sorted(REMIT_DEFAULT)


# `offices.yaml: meta: remit_unruled` -- the remit acts whose standing as an act is an OPEN RULING
# (J-8: `dispatch`), so the overlay of an authored `remit_acts` leaves them exactly where they were.
# Read once at import and checked against `REMIT_ACTS` HERE, for the reason every roster above is
# bound at import: an unrecognised name would match no seat's remit and be dropped without a sound.
OFFICES_REMIT_UNRULED = frozenset(((_OFFICES_DOC.get("meta") or {}).get("remit_unruled")) or ())
if not OFFICES_REMIT_UNRULED <= REMIT_ACTS:
    raise Unspecified(
        f"offices.yaml `meta: remit_unruled` names {sorted(OFFICES_REMIT_UNRULED - REMIT_ACTS)}, "
        "which are not remit acts", "offices.yaml",
        needs="a member of `rosters.yaml: remit_acts`",
        law="a remit act off the closed roster matches no seat's remit -- the one that is named "
            "unruled would be silently granted to nobody, which is a ruling, not a typo")


def authored_remit(row: dict, held=()) -> list[str]:
    """A seat's remit from its authored `offices.yaml` row -- the ONE owner of the overlay rule
    (plan position `13d-iii`), beside `remit_or_default`, which it supersedes wherever a row exists.

    ⚠ THE ROW'S `remit_acts` IS THE REMIT, `[]` INCLUDED, EXCEPT FOR WHAT `held` BRINGS. A declared
    empty list is NOT passed to `remit_or_default` (which would fill it with every act): the row
    was authored from canon and the default is a testing fixture (`rosters.yaml: remit_default`).
    But it does NOT grant nothing on a loop-built seat -- see `held`.

    ⚠ `held` IS WHAT THE SEAT HAD BEFORE THE OVERLAY, and only the acts in `OFFICES_REMIT_UNRULED`
    survive from it -- `dispatch` today, an open ruling (J-8). THIS GRANTS IT, it does not stay
    neutral: a loop-built seat was seated with `remit_default` (every act) unless its case's own
    overlay declares a remit, so its `held` carries `dispatch` and it keeps it. MEASURED,
    `build_realm(0)`, 2026-10-02: 22 of the 29 authored seats hold it -- 22 of the 23 loop-built
    (seven whose row is `remit_acts: []`, where it is the whole remit, and fifteen that carry it
    beside the acts their row names; the one loop-built seat without it is `off_parliamentary_clerk`,
    whose overlay declares `remit: [issue]`) and 0 of the 6 minted -- and `march`, eligible on
    `remit:dispatch`, is eligible to every holder. A seat the loop did not build (a MINTED row)
    passes nothing and so does NOT gain it: two identical rows diverge by build route. Stripping
    `dispatch` (J-8) is a GRANT decision for Jordan, not a code fix. `sorted`, for
    `remit_or_default`'s reason: a set's order is per-process and the grant folds into
    `World.content_hash`."""
    return sorted(set(row["remit_acts"]) | (set(held) & OFFICES_REMIT_UNRULED))


WITNESS_CHANNELS = roster("witness_channels", ordered=True)
CLAIM_SOURCES = roster("claim_sources")
# Plan position `15d` (proceedings `19_PLAN.md` step 4 (b)): the source a deposit carries is set by
# the ONE channel `epistemic.observers_for` credits the witness to -- `WITNESS_CHANNELS`' order is
# that precedence. Cross-validated here, where both rosters it is keyed on are bound, and at import:
# a channel with no source would deposit under a source nothing declared (or `KeyError` mid-barrier,
# inside WITNESS's parallel map), and a source outside `claim_sources` is a fifth way of coming to
# hold a claim that the roster -- *"every value here is a way ONE person came to hold ONE claim"* --
# does not have.
CHANNEL_CLAIM_SOURCE = roster_map("witness_channels", "claim_source")
if (set(CHANNEL_CLAIM_SOURCE) != set(WITNESS_CHANNELS)
        or not set(CHANNEL_CLAIM_SOURCE.values()) <= set(CLAIM_SOURCES)):
    raise Unspecified(
        f"`witness_channels.claim_source` is {CHANNEL_CLAIM_SOURCE!r}; it must key exactly the "
        f"channels {list(WITNESS_CHANNELS)} and name only {sorted(CLAIM_SOURCES)}",
        "rosters.yaml",
        needs="give every channel exactly one source from `claim_sources`",
        law="19_PLAN.md step 4 (b) -- the claim's source is set FROM A CHANNEL->SOURCE MAP, so "
            "the map is total over the channels and closed over the sources")
STRATA = roster("strata", ordered=True)
# ⚠⚠ **READ FROM THE LEAF, NOT FROM `rosters.yaml`, AND THIS IS THE ONE ROSTER THAT WORKS THAT
# WAY.** Every other name here comes from `rosters.yaml` because Jordan ruled definitions must not
# be hardcoded and that file is the season package's definition surface. The thirteen Convictions
# already HAVE an owner one layer out — `references/descriptor_registry.yaml:conviction_roster`,
# exported by `tools/export_descriptors.py` behind a blocking `--check`, read by
# `engine.substrate.descriptors` — and `tests/valoria/test_conviction_roster_single_owner.py`
# records what a second copy costs: three incompatible rosters shipped simultaneously and silently
# disabled ED-912 §6.1's Conviction Scar for as long as both modules existed. Copying them into
# `rosters.yaml` would have been a fourth, in a file that guard does not scan.
# ⚠ THE ROW STILL EXISTS IN `rosters.yaml` and carries the source and the note; what it does not
# carry is `values:`. A reader looking for the definition is sent one hop, which is the correct
# number of hops when the definition is owned elsewhere.
# ⚠⚠ AND "THE ONE ROSTER THAT WORKS THAT WAY" IS STALE AS OF 2026-09-15, WHICH IS WHY THE CLAIM IS
# CORRECTED HERE RATHER THAN LEFT TO READ TRUE. The row was given `from_descriptor: conviction_roster`
# in that migration, so `roster("pursuits")` now resolves through the pointer branch above and
# returns the SAME thirteen -- measured, the two are set-equal. Two routes, one owner, no second
# copy: the direct import below is the leaf and the pointer is the data-side route that also gets
# the `forbidden:` bar. `pursuit_axes` on the line after this one has only ever had the pointer.
# What would be a defect is a THIRD route carrying its own literal, and that is what the guard in
# `roster()` above now refuses.
# ⚠ RENAMED 2026-09-24 (`ED-IN-0261` item 1, rename half only): the season-side binding is now
# `PURSUITS`/`PURSUIT_AXES`. The leaf itself (`CONVICTIONS`) and `descriptor_registry.yaml`'s
# `conviction_roster`/`axis_roster` keys are UNCHANGED -- they still carry the old 13/4 taxonomy,
# and this import merely gives the season package a vocabulary-neutral name for it.
from engine.substrate.descriptors import CONVICTIONS as PURSUITS  # noqa: E402
PURSUIT_AXES = roster("pursuit_axes")
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
# `H-33`. THE THREE ARMS OF THE FAN-OUT SWEEP, and the SIBLING of the line above -- two switches
# on one pipeline, and until 2026-09-16 only one of them was data. `observers_for` carried these
# three names as Python literals in an if/elif/else whose `else` refused correctly, so the closed
# set was ENFORCED and simply not DEFINED where a definition belongs (Jordan 2026-09-02, quoted
# at the head of this file). Bound at import for `TITLE_DOMAINS`' reason: an unbound roster is
# the one whose absence goes unnoticed.
FAN_OUT_MODES = roster("fan_out_modes")
# `R8.1`. THE `seen` CLAIM -- its four terms (ordered: they are the struct's fields), the one
# predicate it is deposited under, and which terms each witness channel shows. Bound at import for
# `TITLE_DOMAINS`' reason; the terms are cross-validated against `WITNESS_CHANNELS` and
# `epistemic.Seen` at import in `epistemic.py`, beside the channel predicates they are keyed on.
OBSERVATION_TERMS = roster("observation_terms", ordered=True)
OBSERVATION_DEPOSIT = roster_map("observation_terms", "deposit")
# THE ONE NAME THE `seen` CLAIM IS DEPOSITED UNDER. It lives here and not in `epistemic.py` (where
# it was bound) because `queries/person_q.py::said_of` must read it and `epistemic` imports
# `person_q`: a name two modules need, below both, so the import edge runs one way. `epistemic`
# imports it back, so `epistemic.SEEN_PREDICATE` still resolves for every existing importer.
SEEN_PREDICATE = OBSERVATION_DEPOSIT.get("predicate")
if not isinstance(SEEN_PREDICATE, str) or not SEEN_PREDICATE:
    raise Unspecified(
        "`observation_terms.deposit.predicate` is absent or not a name", "R8",
        needs="name the predicate the `seen` claim is deposited under",
        law="Jordan 2026-09-02 -- a definition is data. A deposit with no declared predicate "
            "would have to spell one in a body")
TERMS_SUPPLIED_BY = roster_map("observation_terms", "supplied_by")
# `W-E`. THE THREE BANDS PERSONAL COMBAT CAN DISTINGUISH, and HOW MUCH BODY A WOUND COSTS. Bound
# here with every other roster rather than beside their reader in the S39 block below, because
# that is where an absent roster's refusal is guaranteed to fire (`TITLE_DOMAINS`' lesson, above).
# ⚠ `ordered=True` AND UNPACKED POSITIONALLY: the order is SEVERITY, worst first, and the roster's
# own note says so. These are NOT the ladder's four bands -- combat is exempt from the ladder by
# Jordan's 2026-09-03 ruling, and `degree_of`'s margin branch calls the tree's owner for those.
COMBAT_BANDS = roster("combat_degree_bands", ordered=True)
FELLED, WOUNDED, UNTOUCHED = COMBAT_BANDS
# `H-98` (plan position `8`). THE QUANTITIES THE SEAM LIFTS OFF THE ENGINE'S `WoundTracker`, and the
# EDGES between the bands above, over those quantities. Both are rosters.yaml rows; the loader
# below refuses an edge that is not about a lifted quantity AT IMPORT, here, where every roster's
# absence is guaranteed to fire (`TITLE_DOMAINS`' lesson, above).
WOUND_QUANTITIES = roster("wound_quantities", ordered=True)


def check_edge_above(above, quantities, what: str, where: str) -> None:
    """THE ONE GRAMMAR OF AN EDGE'S THRESHOLD: a non-negative count, or the NAME of a quantity.

    Read by `load_combat_band_edges` for the authored edges and by `seam/ladder.py::combat_degree`
    for the swept `Fixtures.combat_wounded_above`, so the data and the injected value cannot come to
    disagree about what a threshold may be (§8). `bool` is an `int` in Python and `above: true` is
    a typo for a count, so it is refused by name rather than read as 1."""
    if isinstance(above, bool) or not (
            (isinstance(above, int) and above >= 0) or above in quantities):
        raise Unspecified(
            f"{what}: `above` is {above!r}", where,
            needs=f"a count >= 0, or one of the lifted quantities {list(quantities)}",
            law="H-98 -- an edge is a quantity compared with a count or with another quantity the "
                "tracker returns; anything else is a third kind of thing nobody ruled on")


def load_combat_band_edges(row, bands, quantities) -> tuple:
    """`combat_band_edges`, VALIDATED, as `((band, quantity, above), ...)` in the bands' own order.

    ⚠ ONE EDGE PER BAND EXCEPT THE LAST, AND THE LAST IS THE RESIDUAL -- what is left once every
    earlier edge failed (`combat_degree_bands`' order is SEVERITY, worst first, so the first edge
    that holds is the band). Every refusal is a way the old two literals could not drift and a
    data row can: an edge on a quantity the tracker does not return (the instruction's own
    falsifier), an edge on a band the roster does not carry, a band with no edge, an edge on the
    residual, a `keyed_on` that does not name the roster `bands` came from, an unreadable
    threshold. ID-12 -- at load, not at the first act that would have hit it. Pure over its
    arguments so a test can hand it a bad row and watch it refuse."""
    where = "rosters.yaml: combat_band_edges"
    if not isinstance(row, dict):
        raise Unspecified(
            "roster 'combat_band_edges' is not in rosters.yaml", "rosters.yaml",
            needs="add the row to the data file; do not inline the edge in a body",
            law="Jordan 2026-09-02 -- definitions are not hardcoded. An absent row REFUSES; "
                "falling back to the old literal would be the second copy this row replaced")
    keyed = row.get("keyed_on")
    if not isinstance(keyed, str) or tuple(roster(keyed, ordered=True)) != tuple(bands):
        raise Forbidden(
            f"combat_band_edges.keyed_on is {keyed!r}, which is not the roster the bands came from",
            where, needs="`keyed_on: combat_degree_bands`",
            law="H-98 -- the edges are keyed on the bands; keyed on anything else they would "
                "grade a scene into tokens `verb_table.yaml` does not write on")
    edges = row.get("edges")
    if not isinstance(edges, dict) or not edges:
        raise Unspecified(
            "combat_band_edges has no `edges:` mapping, or it is empty", where,
            needs="one `{quantity, above}` per band but the last",
            law="rosters.yaml's header -- an empty mapping makes every lookup silently answer "
                "the residual band, i.e. everyone Untouched")
    stray = [b for b in edges if b not in bands]
    if stray:
        raise Forbidden(
            f"combat_band_edges names band(s) combat_degree_bands does not carry: {stray}", where,
            needs=f"keys from {list(bands)}",
            law="H-98 -- an edge keyed past its own roster grades into a band nobody declared")
    if bands[-1] in edges:
        raise Forbidden(
            f"combat_band_edges carries an edge on {bands[-1]!r}, the residual band", where,
            needs="delete it -- the last band is what is left when every earlier edge failed",
            law="H-98 -- an edge on the residual would have to be tested after nothing")
    out = []
    for band in bands[:-1]:
        e = edges.get(band)
        if not isinstance(e, dict) or set(e) != {"quantity", "above"}:
            raise Unspecified(
                f"combat_band_edges has no well-formed edge for {band!r}: {e!r}", where,
                needs="`{quantity: <wound_quantities member>, above: <count or member>}`",
                law="H-98 -- a band with no edge is unreachable, and an unreachable band is a "
                    "definition that was never graded")
        if e["quantity"] not in quantities:
            raise Forbidden(
                f"combat_band_edges[{band}] is an edge on {e['quantity']!r}, which the tracker "
                f"does not return", where, needs=f"a quantity from {list(quantities)}",
                law="H-98 -- an edge reads the engine's own WoundTracker fields; one the seam "
                    "does not lift would be read off nothing")
        check_edge_above(e["above"], quantities, f"combat_band_edges[{band}]", where)
        out.append((band, e["quantity"], e["above"]))
    return tuple(out)


COMBAT_EDGES = load_combat_band_edges(
    _ROSTERS.get("combat_band_edges"), COMBAT_BANDS, WOUND_QUANTITIES)
WOUND_HARM_MODELS = roster("wound_harm_models")
# M4 (`ED-IN-0279` clause (a)). `field_degree_bands`' own note: ordered and unpacked the same way,
# `Declared` first because ENCOUNTER's declaration fold writes it at RESOLVE, before anything has
# fought. `FIELD_CASUALTY_MODELS`/`MARCH_TARGET_KINDS` bound here for `TITLE_DOMAINS`' reason: an
# unbound roster is the one whose absence goes unnoticed.
FIELD_BANDS = roster("field_degree_bands", ordered=True)
DECLARED, WON, LOST, UNOPPOSED = FIELD_BANDS
FIELD_CASUALTY_MODELS = roster("field_casualty_models")
MARCH_TARGET_KINDS = roster("march_target_kinds")
# ⚠ BOUND AT IMPORT LIKE THE OTHERS, AND THAT IS THE POINT. `titles` was the ONE roster read
# lazily through a bare `_ROSTERS.get(...) or {}`, so it alone got no existence refusal -- and
# because `_req_revoke` fails OPEN into purview-for-everything when the mapping is empty, the one
# unbound roster was the one whose absence silently restores a ruled-against behaviour.
# ⚠ (`13d-i`, 2026-09-26) `_req_revoke` NO LONGER READS IT -- revocation is `revocation_bases`
# (ED-IN-0256 ruling (3)), so the fail-open above is history. An empty mapping would now make
# every post a non-title: `Office` would stop refusing a title in a body and `build_realm` would
# seat no titled office. Still worth the import-time refusal.
# ⚠⚠ FOLDED FROM `rosters.yaml: titles` INTO `engine/season/offices.yaml` (plan position `8a`,
# `13d-i` item 5 -- Layer 1 `04_CODE_ARCHITECTURE.md` §B.7/§E.1 rules `titles.domains` world-gen
# DATA, and r2 `05_LEDGER_AND_BUILD.md` RULED (c) names the destination). Same mapping, same
# eleven entries, moved rather than copied -- read `_load_offices`'s docstring for the refusal
# shape. `rosters.yaml: titles` is physically deleted as of the Phase-1 methodology close
# (2026-09-29, `/simplify` ALTITUDE lens) -- it stood as orphaned residue for one session while a
# concurrent plan position owned that file, per `offices.yaml`'s own header, and the deletion
# HANDOFF_IN.md named as follow-up lands here.
TITLE_DOMAINS = dict(_OFFICES_DOC["titles"]["domains"])

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

#: `{proposition id: faction name}`. Derived from the roster, so it cannot disagree with it, and
#: it is the direction `leaders()` needs: a caller holds `fac_crown` and wants `Crown`.
FACTION_BY_PROP = {faction_prop_id(f): f for f in FACTIONS}
BODY_FACTION = roster_map("office_bodies", "faction")
BODY_FUNCTION = roster_map("office_bodies", "function")
ROLE_TEMPLATE_OF = roster_map("role_templates", "by_faction")

# ---------------------------------------------------------------------------
# THE `modules:` ROSTER (plan position `30`; A-25, `ED-IN-0284` revised by `ED-IN-0285`) -- THE ONE
# OWNER OF RETENTION. Terms, defined where the loader reads them (`CLAUDE.md` §4):
#   * a MODULE is running code reached by a composition row (`references/module_contracts.yaml`
#     `composition_roles:`); its one identity is its directory name, which is an entry's key here.
#   * an entry's `kind:` is a `module_kinds` member -- minigame, management space, world surface,
#     loop-resident, data register, host or stub (`rosters.yaml` defines each in one line).
#   * an entry's `home:` is the repo-relative path it lives at, a directory ending in `/`. It may
#     name a path that does not exist yet (`game/`); nothing here checks the disk, because a home is
#     a declaration about where an entry BELONGS, and moving code is `31a`-`31c`'s, not a loader's.
# Validated AT LOAD, `_load_rosters`' reason: a check that only runs when something reads the roster
# misses the rows nothing reads. The readers are `R04_PENDING_SUBSYSTEMS`
# (`tests/valoria/test_engine_does_not_import_systems.py`, computed from `home:`) and
# `tools/evacuation_plan.py`'s two `systems/` rules.
# ---------------------------------------------------------------------------
MODULE_KINDS = roster("module_kinds")
#: This loader's own row grammar -- the two keys an entry carries -- not a definition the game
#: resolves from (`_load_rosters`' pointer-key reason).
_MODULE_FIELDS = ("kind", "home")


def _load_modules(members: dict, kinds) -> dict:
    """`{identity: {"kind": str, "home": str}}`, every row refused by name if it is malformed."""
    out = {}
    for name, row in members.items():
        if not isinstance(row, dict):
            raise Unspecified(
                f"`modules` entry {name!r} is not a row", "rosters.yaml",
                needs="a mapping with `kind:` and `home:`",
                law="A-25 -- every retained entry says what it is and where it lives")
        extra = sorted(k for k in row if k not in _MODULE_FIELDS and not str(k).endswith("note"))
        if extra:
            raise Unspecified(
                f"`modules` entry {name!r} carries unknown key(s) {extra}", "rosters.yaml",
                needs=f"only {list(_MODULE_FIELDS)}, or an annotation spelled `*note`",
                law="04 §B.13 #10's rule for a data row -- a column nobody reads is a column that "
                    "silently does nothing")
        require_member(
            row.get("kind"), kinds, f"`modules` entry {name!r} has kind {row.get('kind')!r}",
            "rosters.yaml", law="A-25 -- an entry's kind is a `module_kinds` member")
        home = row.get("home")
        if not isinstance(home, str) or not home.strip() or home.startswith("/"):
            raise Unspecified(
                f"`modules` entry {name!r} has home {home!r}", "rosters.yaml",
                needs="a repo-relative path, a directory ending in `/`",
                law="A-25 -- the roster says where each retained entry lives; an absent home is an "
                    "entry nobody can find")
        out[str(name)] = {"kind": row["kind"], "home": home}
    return out


MODULES = _load_modules(roster_map("modules", "members"), MODULE_KINDS)


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
        require_member(
            body,
            BODY_FACTION,
            f"{body!r} is not a canonical body",
            "rosters.yaml -- office_bodies",
            law="Jordan 2026-09-02 -- systems/world is canon for organizations. Inventing a "
                "body here would be indistinguishable from canon to the next session",
            needs="name a body from `systems/world/`, or drop `body` and author `faction`")
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
    require_member(
        declared,
        FACTIONS,
        f"{declared!r} is not a canonical faction",
        "rosters.yaml -- factions",
        law="Jordan 2026-09-02 -- systems/world is canon for identity and names",
        needs="use a faction named in `systems/world/`")
    return declared


# `title_domain` -- RELOCATED FROM shape.py's governance slice (step 2). A pure content read
# (`TITLE_DOMAINS`), not a verb, so it belongs beside the roster/content layer rather than beside
# the governance verbs that once called it.
# ⚠ `title_rank` IS DELETED (`13d-i`, 2026-09-26). Its one decision was `_req_revoke`'s
# strictly-higher-rank conjunct, and ED-IN-0256 ruling (3) makes revocation *"rung above of same
# faction"* -- structural, not a rank comparison. `title_domain` SURVIVES THAT POSITION, and not by
# choice: `harness/populated.py`'s office seating calls it to decide who holds a titled seat and
# at which rung, and `Office.__post_init__`'s title-in-a-body refusal cannot be stated without it
# (see `state/carriers.py`).
# ⚠⚠ `TITLE_DOMAINS` NO LONGER READS `rosters.yaml: titles` (plan position `8a`, `13d-i` item 5).
# It is folded into `engine/season/offices.yaml: titles: domains:`, same eleven entries, moved
# rather than copied -- see `_load_offices` above and `offices.yaml`'s own header.
def title_domain(post: Optional[str]) -> Optional[str]:
    """The rung kind a title governs, from `offices.yaml: titles: domains:`. `None` for a post
    that is not a title -- a Dicastery is an office, not a rank."""
    return TITLE_DOMAINS.get(str(post or ""))


def refuse_a_titled_post_off_its_rung(who: str, post, kind: str, rung_id: str) -> None:
    """THE ONE RULE THAT A TITLED POST STANDS AT THE RUNG KIND ITS TITLE GOVERNS (r2 `03` §A.8,
    re-homed from `Office.__post_init__`), beside `title_domain`, its one input. Raises `Forbidden`
    for a post that IS a title and stands at a rung of any other `kind`; a post that is not a title
    (a Dicastery, an organ) stands anywhere. `who` names the seat in the refusal, `rung_id` the
    rung it was given. Two seaters call it so neither keeps a copy: `harness/populated.py::
    seat_anchor` (an `offices.yaml` row) and `harness/corpus_run.py::_seat_office` (a corpus
    overlay's `office:`) -- without it a cast entry `{post: Duke}` seated a Duke at a hearth, whose
    purview is then the hearth's, which is canon inverted by a data-entry slip."""
    dom = title_domain(post)
    if dom is not None and kind != dom:
        raise Forbidden(
            f"{who} names the TITLE {post!r} and stands at a {kind!r} rung ({rung_id!r}); the "
            f"title governs a {dom!r}", "offices.yaml -- titles vs rung",
            needs="a rung of the kind the title governs",
            law="r2 03 §A.8 -- a titled post sits at the rung its title governs, never a rung "
                "above or below it")
