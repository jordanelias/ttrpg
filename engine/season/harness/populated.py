"""`harness.populated` — ONE WORLD, THE WHOLE CAST, AND MORE THAN ONE PLACE TO STAND.

WHAT THIS IS FOR, in Jordan's words (2026-09-13): *"I want to see as many persons as there are NPC
season loops for each world. If there are 87 loops, then I want 87 persons for each test run. I want
there to be multiple locations to inhabit."* And: *"each settlement has places/buildings. we need to
build these out for testing."*

WHAT IT REPLACES, AND WHY THE OLD SHAPE COULD NOT SHOW ANYTHING. `corpus_run.build_at` builds ONE
WORLD PER CASE and seats exactly three persons in it -- `p_a`, `p_b`, `p_c`, unnamed, all three in
the SAME rung, in all 89 runnable worlds. Measured 2026-09-13, and each of these is a fact about the
instrument rather than about the design:

  * all three persons act in every world (p_b 2182 acts · p_a 1935 · p_c 1911), so it is not that
    one NPC does everything -- the loops ARE concurrent within a world;
  * they are co-located at tick 0 and at the end of every run, and NOBODY'S containing rung ever
    changes, in any of the 89 worlds;
  * 0 of 4,870 acts name another person as their subject;
  * and the told channel (`ED-IN-0222`) deposits 8 second-hand claims in the whole corpus, because
    a witness who saw everything the teller saw cannot be told anything.

Three anonymous people standing in one room, 89 times over, is not a population, and every
measurement taken on it inherits that. `engine/season/requirements.yaml` names the gap `W27`
("a real cast") and it is the stated blocker on `R2` and `A3`.

WHERE THE PLACES COME FROM, AND WHICH HALF IS CANON.

  * `systems/settlements/valoria_geography_v30.yaml` -- CANON. 17 provinces, 37 settlements, each
    with a territory, a controller and a type. Read, never edited, never overridden here.
  * `engine/season/venues.yaml` -- AUTHORED FOR PLAY. The buildings inside a settlement, which
    canon does not name at all. Its header says so at length.

⚠ THE LADDER NEEDED NO NEW KIND AND THAT IS THE POINT. `rosters.yaml: rung_kinds` is
`person < hearth < community < settlement < territory < province < duchy < realm`. `community` and
`hearth` sat unused in every world this repo has ever built, which is precisely why everyone was in
one room: `build_at` seats a person directly in the settlement. A BUILDING is a `hearth`; a QUARTER
is a `community`. `contain_ascends` requires strict ascent and not adjacency (`state/world.py:220`),
so `realm -> province -> settlement -> community -> hearth -> person` is legal with `territory` and
`duchy` unused.

⚠ THE CAST IS THE CORPUS'S OWN, NOT A GENERATED ONE. Every case carries a `name:` -- "Carin Vedel",
not `p_a` -- and one person is seated per case. That is `W27`'s *"the cast comes from the case"*
read literally, and it is why this module authors no NPC: inventing a roster here would be the
fabrication `OI-05` is filed as a ruling to avoid (`ED-WR-0011`).

⚠ WHAT THIS DOES **NOT** DO. It does not grade the 143 cases -- `corpus_run` still owns that, and
its per-case worlds are what the `R1`/`R3`/`R4`/`R5` checks are computed over. This is a second
instrument beside it, not a replacement, and nothing here is wired into a gate yet. Read its output
as a measurement of what a populated world does, not as a claim that a case passes.

⚠ **ARCS ARE OUT OF SCOPE BY DECISION, NOT BY OVERSIGHT (Jordan, 2026-09-13: *"Maybe we just
ignore the arcs now"*, `ED-IN-0225`).** The 97 ARC cases name SITUATIONS -- "The Unworked Clause",
"Vaynard's Wager" -- and what an arc IS in this world has no carrier. An earlier draft of this
module listed that as an open design question; it is closed, and the next session should not
reopen it.

THE DECISION COSTS NOTHING MEASURABLE, which is why it is cheap to take and is recorded with its
evidence rather than as a preference. `corpus_run`'s own bar reports the ARC lane as
*"ENDS = NOT-COMPUTABLE -- closed by W23 (contest results) + W26 (binding decisions) + W30 (the
predicates)"*. An arc CARRIER is on none of those three. So the ARC half of the bar was never
waiting on this and does not start moving if someone builds it -- the ARC cases keep being graded
by `corpus_run` exactly as before, and only the *design question* is dropped.
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict

from ..data import cast, files
from ..data import goals as goals_data
from ..queries.world_q import (HUNGER_KIND, RESIDE_KIND, WORKS_KIND, ancestry, capacity, closed_uses,
                                enclosing_territory, home_of as home_of_q, hunger, members, subsistence_draw, uncontrolled)
from ..gaps import Forbidden, Unspecified
from ..data.fixtures import DEFAULT_FIXTURES, SITE_YIELD
from ..data.rosters import (BODY_FACTION, FACTIONS, FOREIGN_CAST, FOREIGN_SEATS, OFFICES_BY_HOLDER,
                            OFFICES_SEATS, ROLE_TEMPLATE_OF, authored_remit,
                            faction_prop_id, load_yaml, refuse_a_titled_post_off_its_rung,
                            remit_or_default, territory_id_of, territory_rung_id, title_domain)
from ..data.geography import geography
from ..data.pursuits import temperament_pursuits
from ..decision import make_chooser
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..loop.effects import EFFECTS
from ..state.carriers import Act, Office, Person, Proposition, Rung, Site, Tenure
from ..state.gate import NO_CHANGE
from ..state.ids import H, ROOT, draw_factory
from ..state.world import World
from . import probes as P
from .run_cases import load_cases, seed_pursuits, wants_of

GEOGRAPHY = files.GEOGRAPHY_YAML.relative_to(files.REPO_ROOT).as_posix()  # the path's one owner is `data/files.py`
VENUES = "engine/season/venues.yaml"
ROSTER = "engine/season/npcs.yaml"


def _load(rel):
    """A repo-relative YAML file, through the package's OWN anchor and its OWN reader.

    ⚠ NEITHER HALF IS A STYLE CHOICE AND THE FIRST CUT GOT BOTH WRONG. It carried a private
    `_repo_root()` climbing three `.parent`s -- a thirtieth anchor in a package whose
    `data/files.py` exists to hold the only one, and whose docstring makes that a CHECKABLE
    property (*"`grep -rln <the dunder> season/` must print this file and nothing else"*), with
    `combat_seam.py` as the worked case for why a wrong anchor fails SILENTLY. And it called
    `yaml.safe_load` directly, which keeps the LAST of two identical keys without a word --
    the defect `data/rosters.load_yaml` was written to refuse, and `venues.yaml` is exactly the
    shape that hides one (a settlement type listed twice would lose its first building set).
    """
    return load_yaml((files.REPO_ROOT / rel).read_text(encoding="utf-8"))


def _slug(text: str) -> str:
    """An id fragment. Lowercase, alphanumerics and underscores only."""
    return "".join(c if c.isalnum() else "_" for c in str(text).lower()).strip("_")


# ---------------------------------------------------------------------------
# THE RUNG ANCHOR (plan position `13d-iii`; r2 `03` §A.14, A-5 answered at ladder step 3).
# `offices.yaml` never spells a rung id, so a `build_realm` rename cannot rot the file (`CLAUDE.md`
# §5's hand-transcription hazard, one layer earlier). A seat's `rung:` is a FORM -- a one-entry
# mapping `{<rung kind>: <key>}` -- and there is ONE resolver over all of them. The forms in use are
#     {realm: true} · {duchy: "<faction>"} · {territory: "<code>"} · {settlement: "<code>"}
#     · {hearth: "<geography code>:<building slug>"} (v10 IN-45: `venues.yaml: planned_works`' `at:`)
# and the resolver does not know that: it asks the INDEX `build_realm` fills as it mints each rung
# (`_index_anchor`, at the mint sites, where the key is already in hand) for exactly one rung of
# exactly that kind. It names no rung kind and no seat, so another form is a line at one more mint
# site and a row, never a branch here -- and it is why a rung kind with no minted rung (`province`,
# which `build_realm` deliberately never builds: a province is a QUERY) refuses instead of
# resolving to something near it.
# ---------------------------------------------------------------------------

def _index_anchor(w: World, anchors: dict, key, rid: str) -> None:
    """Record that `rid` is the rung the anchor `{<its kind>: key}` names. A second rung under one
    anchor is REFUSED, not shadowed: the anchor would then resolve to whichever was minted last,
    which is `r2 03` §A.14's "resolves to more than one" failure arriving without a sound."""
    kind = w.rungs[rid].kind
    if (kind, key) in anchors:
        raise Forbidden(
            f"the anchor {{{kind}: {key!r}}} names two rungs: {anchors[(kind, key)]!r} and {rid!r}",
            "harness/populated.py -- rung anchors",
            needs="one rung per anchor; a form's key must tell its rungs apart",
            law="r2 03 §A.14 -- an anchor that resolves to more than one rung is refused")
    anchors[(kind, key)] = rid


def resolve_anchor(w: World, anchors: dict, form, whose: str = "") -> str:
    """The rung id an `offices.yaml` `rung:` FORM names -- ONE resolver over every form.

    `form` is `{<kind>: <key>}`: exactly one entry, `kind` a rung kind that `build_realm` minted
    and `key` what tells that kind's rungs apart. Refuses (`Unspecified`) a form that is not a
    one-entry mapping, and one that resolves to NO rung -- the unknown key, the kind the realm has
    none of, or a key of the wrong type (`{realm: "x"}` is not `{realm: true}`). It never guesses
    and never falls back to a nearby rung: a seat with the wrong ground reaches the wrong rungs
    quietly, which is worse than a seat that does not build."""
    if not isinstance(form, dict) or len(form) != 1:
        raise Unspecified(
            f"{whose or 'a seat'} declares the rung anchor {form!r}", "offices.yaml -- rung",
            needs="a one-entry mapping `{<rung kind>: <key>}`",
            law="r2 03 §A.14 -- four anchor forms, never a rung id")
    (kind, key), = form.items()
    # THE KEY'S TYPE IS PART OF THE ANCHOR. `True == 1` and the two hash alike, so `{realm: 1}` would
    # find `{realm: true}`'s rung through the dict below; and an unhashable key (`{duchy: [..]}`)
    # would raise `TypeError` out of `anchors.get` instead of the refusal this function owes. Every
    # form is `{<text kind>: <text key>}`, or `true` for the one realm: refuse the rest, by name.
    if not isinstance(kind, str) or not isinstance(key, (str, bool)):
        raise Unspecified(
            f"{whose or 'a seat'} declares the rung anchor {form!r}, whose "
            f"{'kind' if not isinstance(kind, str) else 'key'} has the wrong type",
            "offices.yaml -- rung",
            needs="a text kind and a text key (`true` for the realm)",
            law="r2 03 §A.14 -- `True == 1` and an unhashable key would otherwise resolve to the "
                "wrong rung or raise `TypeError`, not refuse")
    rid = anchors.get((kind, key))
    if rid is None or rid not in w.rungs or w.rungs[rid].kind != kind:
        raise Unspecified(
            f"{whose or 'a seat'} declares the rung anchor {{{kind}: {key!r}}}, which names no "
            f"{kind} rung in this realm", "offices.yaml -- rung",
            needs="an anchor `build_realm` indexed as it minted the rung",
            law="r2 03 §A.14 -- the anchor resolves to exactly one rung or the seat is refused")
    return rid


def seat_anchor(w: World, anchors: dict, row: dict) -> str:
    """The rung an authored seat ROW stands at: its anchor, resolved, plus the one content rule
    r2 `03` §A.8 re-homed from the constructor -- a TITLED post stands at the rung kind its title
    governs, or a Duke seated at the realm has realm-wide purview (`Office.__post_init__`'s own
    comment; `title_domain` is the ladder's one owner). The rule itself is
    `rosters.refuse_a_titled_post_off_its_rung`, which `corpus_run._seat_office` calls too."""
    rid = resolve_anchor(w, anchors, row["rung"], f"{row['id']} ({row['post']!r})")
    refuse_a_titled_post_off_its_rung(row["id"], row["post"], w.rungs[rid].kind, rid)
    return rid


# ---------------------------------------------------------------------------
# WHICH INSTITUTION A SEASON LOOP BELONGS TO.
#
# ⚠ THE CASES DO NOT NAME PLACES AND THIS IS THE MEASURED REASON FOR THE INDIRECTION. Scanned
# 2026-09-13 over all 143 cases against every canonical province and settlement name: EXACTLY TWO
# name one (NPC-083 names Ehrenfeld, ARC-25 names Schoenland). They are requirement specifications
# -- *"a person holding no office must be able to perform a repeated, multi-week task"* -- and carry
# no setting whatsoever. So a place cannot be read off a case directly.
#
# What 62 of them DO name is an institution, and institutions have canonical seats. That is the
# overlap this seats people on: the Church's 25 loops share Himmelenger, the Crown's 26 share
# Valorsplatz. A place that serves many loops is the shared SEAT, not a coincidence of wording.
#
# ⚠ ORDER IS SIGNIFICANT AND IS NOT ALPHABETICAL. A case naming both the Church and the Crown is
# seated by the FIRST match, so the more specific institution is listed first -- `Löwenritter`
# before `Crown`, because a knightly order is a Crown body and the barracks is the better answer
# than the court. Re-ordering this list moves people, which is a game change, which is why it is
# stated rather than sorted.
_INST_CACHE = None


def _mentions(candidate: str, text: str) -> bool:
    """Does `text` name `candidate` as a whole word? The one owner of this file's match rule.

    Written out three times before 2026-09-15 (`institution_of`, and both loops in `concerns_of`).
    A change to the boundary rule — a hyphenated title like `Warden-Chief` is already on the
    `TITLES` roster and does not word-match cleanly — had to be found and made three times, with a
    reviewer re-verifying each copy rather than reading one function."""
    return re.search(r"\b" + re.escape(candidate) + r"\b", text) is not None


def _institutions() -> list:
    """The institution match order, from `venues.yaml: seat_precedence`. ONE owner.

    ⚠⚠ THIS WAS A SECOND LITERAL AND NOTHING COMPARED THE TWO. It re-typed the eleven `seats:`
    keys of `venues.yaml` in a different order, inside this file, four days after ED-IN-0230 fixed
    exactly that shape for the ethical axes. A seat added to `venues.yaml` was never matched; a
    seat removed sent its people to `commons` with no signal — failing silently in both
    directions.
    ⚠ THE REFUSAL IS THE POINT, not the de-duplication: a precedence list that has drifted from
    the seats it orders is a world built on a matcher that cannot see part of its own map."""
    global _INST_CACHE
    if _INST_CACHE is not None:
        return _INST_CACHE
    ven = _load(VENUES)
    order = list(ven.get("seat_precedence") or [])
    seats = set(ven.get("seats") or {})
    if set(order) != seats:
        raise Unspecified(
            f"venues.yaml: seat_precedence and seats disagree — "
            f"only in precedence: {sorted(set(order) - seats)}; "
            f"only in seats: {sorted(seats - set(order))}",
            "engine/season/venues.yaml",
            needs="every `seats:` key ordered exactly once in `seat_precedence`",
            law="ED-IN-0230 — two literals of one set with no refusal between them is how the "
                "ethical axes drifted; a seat nobody ordered is a seat nobody is ever matched to")
    _INST_CACHE = order
    return order


def institution_of(case: dict) -> str | None:
    """The institution this loop answers to, or `None` for an unaffiliated life."""
    import json
    blob = " ".join([str(case.get("name", "")), str(case.get("one_line", "")),
                     json.dumps(case.get("season_requires", ""), ensure_ascii=False),
                     json.dumps(case.get("who_acts", ""), ensure_ascii=False),
                     json.dumps(case.get("knowledge", ""), ensure_ascii=False),
                     json.dumps(case.get("ends_when", ""), ensure_ascii=False)])
    for inst in _institutions():
        if _mentions(inst, blob):
            return inst
    return None




# ⚠ TITLES ARE NOT NAMES (Jordan, 2026-09-13: *"inge baralta is Duchess baralta etc. so don't
# confuse titles with names"*). The corpus refers to a person by title and surname -- "Duchess
# Baralta", "the Warden-Chief" -- and almost never by the full name its own `name:` field carries.
# MEASURED: matching the full name finds **11 ties across 9 cases**; matching the surname with
# titles stripped finds **104 across 66 of 143**. The first number is not a sparse graph, it is a
# broken matcher, and reporting it as a finding about the corpus would have been wrong.
TITLES = ("Duchess", "Duke", "Baron", "Baroness", "Count", "Countess", "Bishop", "Archbishop",
          "Abbot", "Abbess", "Prior", "Prioress", "Sir", "Dame", "Lord", "Lady", "King", "Queen",
          "Prince", "Princess", "Captain", "Commander", "Warden", "Warden-Chief", "Inquisitor",
          "Master", "Mistress", "Father", "Mother", "Brother", "Sister", "Chancellor", "Marshal",
          "Steward", "Reeve", "Provost", "The", "the")


def surname_index(cases: list) -> dict:
    """`surname -> [case_id, ...]`, titles removed. A surname may be SHARED -- `Almqvist` is four
    NPC cases, which is a family and not a collision to resolve away."""
    out: dict = defaultdict(list)
    for c in cases:
        toks = [t for t in re.split(r"\s+", str(c.get("name", "")).strip())
                if t and t not in TITLES]
        # A one-token name ("Orm") is its own surname. Short tokens are skipped: a three-letter
        # match against free prose is a coincidence generator, not a tie.
        if toks and len(toks[-1]) >= 4:
            out[toks[-1]].append(str(c.get("id")))
    return dict(out)


def concerns_of(case: dict, by_name: dict) -> tuple:
    """WHO THIS LOOP'S WANT CONCERNS: `(case_id | None, institution | None)`.

    Read off `who_acts`, which is a list of the parties a case says are involved. Two kinds of
    entry, and both are used:

      * A NAMED PERSON who is another case's own person. Measured: **11 such ties across 9 cases**
        -- sparse, and real, so they are used first and never overridden by a heuristic.
      * A ROLE: *"any Church Inquisitor investigating the region"*, *"Guild leadership"*,
        *"the Warden-Chief (his senior)"*. 583 `who_acts` entries exist and most are this. A role
        resolves to an INSTITUTION, and an institution has a canonical seat, so the tie lands on
        somebody seated there.

    ⚠ `who_acts[0]` IS NOT RELIABLY THE CASE'S OWN PERSON -- it matches the case `name` in only 38
    of 143. So self-exclusion is done by id afterwards rather than by skipping the first entry,
    which is what a reader would assume and what would silently mis-tie 105 cases.
    """
    acts = [str(x) for x in (case.get("who_acts") or [])]
    for entry in acts:
        for nm, cids in by_name.items():
            if _mentions(nm, entry):
                # A shared surname is a FAMILY (`Almqvist` is four cases). The tie lands on the
                # first by id and the ambiguity is real rather than resolved -- which of four
                # siblings *"his family"* means is not answerable from the corpus.
                for cid in sorted(cids):
                    if cid != case.get("id"):
                        return cid, None
    for entry in acts:
        for inst in _institutions():
            if _mentions(inst, entry):
                return None, inst
    return None, None


# -- THE POPULATION SYNECDOCHES (plan position `24f`, `ED-IN-0255`) -----------------------------
#
# The row's own field names -- the schema `cohorts.yaml` is checked against, `Rung._DECLARED`'s
# shape -- not the game's vocabulary.
COHORT_FIELDS = frozenset({"rung", "weight"})
# The id a cohort's `Person` (and its `person` rung) is minted under: this prefix and the rung it
# lives in. One cohort per rung, so the rung id is the whole of what distinguishes two of them.
COHORT_PREFIX = "cohort_"


def cohort_rows(text: str | None = None) -> list:
    """THE AUTHORED ROWS OF `cohorts.yaml`, schema-checked: `[{rung, weight}, ...]` in file order.
    Plan position `24f`. `text` is the file's contents, for a caller that plants rows; `None`
    reads the file through `data/files.py`'s one anchor and `load_yaml`'s duplicate-key refusal.

    Everything a row can get wrong WITHOUT a world is refused here; what needs the built world
    (the rung exists, the weight fits its capacity) is `seat_cohorts`'s. Each refusal names the row.
      * NO ROWS AT ALL. The larder draw feeds only cohorts (`world_q.subsistence_draw`), so a realm
        seeded from an empty file would run its whole subsistence pass over nobody and report a
        quiet world. That silent emptying is the failure the plan's attack on `24f` names, so the
        loader refuses it rather than a test catching it later.
      * A FIELD THE FILE DOES NOT DECLARE (`COHORT_FIELDS`). A `case:`, `want:` or `concerns:` would
        be `npcs.yaml`'s schema arriving here, the invented character this file exists not to be.
      * A WEIGHT THAT IS NOT AN INT `> 1`. S9: a person at weight 1 is an individual, and this file
        mints no individuals. `bool` is refused too, because YAML's `yes` would otherwise pass as 1.
      * THE SAME RUNG TWICE. One cohort per populated rung is the design (item 10's *"one authored
        `weight > 1` `Person` row per populated rung"*); a second row would quietly double the
        mouths under one roof, and the minted ids would collide."""
    if text is None:
        text = files.COHORTS_YAML.read_text(encoding="utf-8")
    rows = (load_yaml(text) or {}).get("cohorts") or []
    if not rows:
        raise Unspecified(
            "`cohorts.yaml` declares no cohort", "engine/season/cohorts.yaml",
            needs="one `{rung, weight}` row per populated rung",
            law="plan position `24f` -- only a cohort eats (`ED-IN-0255`), so a world with none "
                "has no eater and its subsistence pass runs over nobody")
    seen: set = set()
    for n, row in enumerate(rows):
        extra = set(row) - COHORT_FIELDS if isinstance(row, dict) else None
        if extra is None or extra or not COHORT_FIELDS <= set(row):
            raise Unspecified(
                f"`cohorts.yaml` row {n} is {row!r}", "engine/season/cohorts.yaml",
                needs=f"exactly the fields {sorted(COHORT_FIELDS)}",
                law="plan position `24f` -- a cohort traces to no case, so it carries none of "
                    "`npcs.yaml`'s fields and nothing undeclared")
        wt = row["weight"]
        if isinstance(wt, bool) or not isinstance(wt, int) or wt <= 1:
            raise Forbidden(
                f"`cohorts.yaml` row {n} ({row['rung']!r}) has weight {wt!r}", "S9",
                law="S9 -- A COHORT IS A PERSON AT weight > 1; a weight-1 row would mint a named "
                    "individual, which this file never does")
        if row["rung"] in seen:
            raise Unspecified(
                f"`cohorts.yaml` names {row['rung']!r} twice", "engine/season/cohorts.yaml",
                needs="one row per populated rung",
                law="plan position `24f` -- one synecdoche per rung; a second row doubles its "
                    "mouths and collides on the minted id")
        seen.add(row["rung"])
    return rows


TEMPERAMENT_FIELDS = frozenset({"territory", "alpha", "beta"})


def temperament_rows(text: str | None = None) -> list | None:
    """THE `temperaments:` BLOCK OF `cohorts.yaml`, schema-checked: `[{territory, alpha, beta}, ...]` in file
    order, or `None` when the file carries no such block (cohorts then stay uniform, as before SE-06: the block's
    absence IS the revert and the control). `text` is the file's contents, for a caller that plants a block.

    Refused here, without a world: a block with no row, a field the file does not declare
    (`TEMPERAMENT_FIELDS`), an `alpha` or `beta` that is not a number in `[0, 1]` (`bool` refused: YAML's
    `yes` is not 1), a territory that is no row of the geography file's `provinces:`, and the same territory
    twice. What needs the built world (every cohort's territory has a row) is `seat_cohorts`'s."""
    if text is None:
        text = files.COHORTS_YAML.read_text(encoding="utf-8")
    block = (load_yaml(text) or {}).get("temperaments")
    if block is None:
        return None
    if not isinstance(block, list) or not block:
        raise Unspecified(
            "`cohorts.yaml: temperaments` declares no list of rows", "engine/season/cohorts.yaml",
            needs="one `{territory, alpha, beta}` row per territory holding a cohort, or no block at all",
            law="SE-06 -- an empty block would read as a configured realm and configure nothing")
    provinces = set(geography()["provinces"])
    seen: set = set()
    for n, row in enumerate(block):
        if not isinstance(row, dict) or set(row) != TEMPERAMENT_FIELDS:
            raise Unspecified(
                f"`cohorts.yaml: temperaments` row {n} is {row!r}", "engine/season/cohorts.yaml",
                needs=f"exactly the fields {sorted(TEMPERAMENT_FIELDS)}",
                law="SE-06 -- a temperament row is a territory and its two weights, and nothing undeclared")
        for f in ("alpha", "beta"):
            v = row[f]
            if isinstance(v, bool) or not isinstance(v, (int, float)) or not 0 <= v <= 1:
                raise Forbidden(
                    f"`cohorts.yaml: temperaments` row {n} ({row['territory']!r}) has {f} {v!r}", "SE-06",
                    law="SE-06 -- alpha and beta are weights, numbers in [0, 1]")
        if not isinstance(row["territory"], str) or row["territory"] not in provinces or row["territory"] in seen:
            raise Unspecified(
                f"`cohorts.yaml: temperaments` row {n} names the territory {row['territory']!r}, "
                f"{'twice' if isinstance(row['territory'], str) and row['territory'] in seen else 'which the geography file does not carry'}",
                "engine/season/cohorts.yaml",
                needs="one row per geography `provinces:` territory",
                law="SE-06 -- one temperament per territory; a second would be two answers to one question")
        seen.add(row["territory"])
    return block


def seat_cohorts(w: World, rows: list, names: dict | None = None, temperaments: list | None = None) -> list:
    """SEAT THE AUTHORED COHORTS IN A BUILT WORLD, and return their person ids in row order. Plan
    position `24f`: the producer the design step named (`workplans/2026-09-28-the-plan-one-order-
    mc-v18-retired.md` §3.1 item 10), read at world-gen beside the case-derived cast.

    Each row becomes what every builder mints for a person, and nothing else: a `Person` at the
    row's weight, its `person` rung, a `contain` edge (where it IS) and a `reside` edge (where it
    LIVES, `19c`'s rule) to the row's rung. No `commit`, so it is no faction's member; no `hold`,
    so it holds nothing; no convictions -- inventing convictions for a population would be authoring a
    creed nobody wrote, and the conviction half is HELD (`cohorts.yaml: temperaments:` names the residue;
    `Person.conviction` stays `{}`). Its PURSUITS are its
    territory's temperament when `temperaments` is given (SE-06, ED-IN-0293 row 1 reading (b), taken by M1 of
    the v10 decision round: `cohorts.yaml: temperaments:`, translated by `data/pursuits.py::temperament_pursuits`),
    and none when it is `None`, so it ranks by the uniform arm a person with no authored pursuits gets. Two
    cohorts of one territory hold the same vector (declared); no spread between them, and no goals.
    It is a Person in full, though (S9.1, ONE CLASS; probe `P21`: *"a crowd must be able to
    act"*), so it witnesses, holds claims and deliberates like anyone. Nothing here stops that, and
    doing so would be special-casing an entity (`CLAUDE.md` §10's scripting drift).

    ⚠ THE CEILING, CHECKED AND NEVER USED AS A SOURCE (`ED-SE-0051`, `ED-WR-0011`). A row whose
    weight passes `capacity(w, rung)` REFUSES: the synecdoche would stand for more people than the
    place's dwellings house. It is the COHORT's weight that is checked, not the rung's `population`
    with it. The case-derived cast already overfills two settlements on the realm as built
    (measured at `24f`: `set_s_001` houses 10 named residents against 9 dwellings, `set_s_036` 8
    against 6), and that is `npcs.yaml`'s placement, not this file's; refusing a cohort for it
    would leave the court's own town with no people. The check reads the Query at build, once, so
    it sees exactly the dwellings `build_realm` minted.
      * AN UNKNOWN RUNG REFUSES. A row naming a place the builder did not build would otherwise
        seat nobody and look like a quiet town.
      * A CLASH WITH AN EXISTING PERSON ID REFUSES, rather than overwriting a cast member.

    `temperaments` is `temperament_rows()`'s output, or `None` for a uniform cohort. When given, EVERY
    cohort's territory (the rung that CONTAINS its settlement, `territory_id_of`) must have a row, else
    `Unspecified` names the territory and the cohort: a block that covered some cohorts would leave the rest
    uniform and read as complete.

    `names` maps a rung to the place's canon name, so the cohort reads *"the people of
    Valorsplatz"*; a rung it does not name is named by its id. Display only: nothing resolves on a
    `Person.name`."""
    names = names or {}
    vector_of = ({r["territory"]: temperament_pursuits(r["alpha"], r["beta"]) for r in temperaments}
                 if temperaments is not None else None)      # territory -> its vector, once; a cohort takes a COPY
    out: list = []
    for row in rows:
        rung, wt = row["rung"], row["weight"]
        if rung not in w.rungs:
            raise Unspecified(
                f"`cohorts.yaml` seats a cohort at {rung!r}, which this world did not build",
                "engine/season/cohorts.yaml",
                needs="a rung id `build_realm` builds (a settlement is `set_` + its geography id)",
                law="plan position `24f` -- a cohort at a missing place seats nobody silently")
        room = capacity(w, rung)
        if wt > room:
            raise Forbidden(
                f"`cohorts.yaml` gives {rung!r} a cohort of weight {wt}; its capacity is {room}",
                "ED-SE-0051",
                law="RR-2 -- capacity bounds POPULATION; an authored cohort may not stand for more "
                    "people than the rung's dwellings house (checked, never derived)")
        pid = f"{COHORT_PREFIX}{rung}"
        if pid in w.persons or pid in w.rungs:
            raise Unspecified(
                f"cohort id {pid!r} is already taken in this world", "engine/season/cohorts.yaml",
                needs="a rung whose cohort id no cast member or rung already uses",
                law="plan position `24f` -- a cohort is seated beside the cast, never over it")
        pursuits: dict = {}
        if vector_of is not None:
            terr = territory_id_of(enclosing_territory(w, rung))
            if terr not in vector_of:
                raise Unspecified(
                    f"cohort {pid!r} lives in the territory {terr!r}, which `cohorts.yaml: temperaments` has no row for",
                    "engine/season/cohorts.yaml",
                    needs=f"a `{{territory: {terr}, alpha, beta}}` row, or no `temperaments:` block",
                    law="SE-06 -- a cohort's pursuits are its territory's temperament; a territory with no row is refused, not left uniform")
            pursuits = dict(vector_of[terr])
        w.persons[pid] = Person(pid, f"the people of {names.get(rung, rung)}", weight=wt, pursuits=pursuits)
        w.rungs[pid] = Rung(pid, "person")
        w.add_tenure(Tenure(f"t_{pid}_in", pid, rung, "contain", 0))
        w.add_tenure(Tenure(f"t_{pid}_home", pid, rung, RESIDE_KIND, 0))
        out.append(pid)
    return out


# -- THE GUARD COHORTS (v9 IN-36 carrying IN-60's guard content, RS-26) ------------------------------
GUARD_FIELDS = frozenset({"seat", "weight"})


def guard_rows(text: str | None = None) -> list:
    """THE AUTHORED GUARD ROWS OF `cohorts.yaml: guards`, schema-checked: `[{seat, weight}, ...]` in file
    order. `text` is the file's contents for a caller that plants rows. Refused here, without a world: a row
    with a field the file does not declare (`GUARD_FIELDS`), a weight that is not an int `> 1` (S9: a guard
    is a cohort, and a weight-1 row would mint a named individual), a seat that is no `offices.yaml: seats`
    id, a seat twice, and NO ROWS AT ALL (`guards=True` over an empty section would seat nobody and read as
    a guarded realm)."""
    if text is None:
        text = files.COHORTS_YAML.read_text(encoding="utf-8")
    rows = (load_yaml(text) or {}).get("guards") or []
    if not rows:
        raise Unspecified(
            "`cohorts.yaml` declares no `guards:` row", "engine/season/cohorts.yaml",
            needs="one `{seat, weight}` row per guarded principal's seat",
            law="v9 IN-36 (IN-60's content, RS-26) -- `build_realm(guards=True)` over no row guards nobody")
    seats = {s["id"] for s in OFFICES_SEATS}
    seen: set = set()
    for n, row in enumerate(rows):
        if not isinstance(row, dict) or set(row) != GUARD_FIELDS:
            raise Unspecified(
                f"`cohorts.yaml` guards row {n} is {row!r}", "engine/season/cohorts.yaml",
                needs=f"exactly the fields {sorted(GUARD_FIELDS)}",
                law="v9 IN-36 -- a guard row names a seat and a weight, and nothing undeclared")
        wt = row["weight"]
        if isinstance(wt, bool) or not isinstance(wt, int) or wt <= 1:
            raise Forbidden(f"`cohorts.yaml` guards row {n} ({row['seat']!r}) has weight {wt!r}", "S9",
                            law="S9 -- A COHORT IS A PERSON AT weight > 1; a guard is one")
        if row["seat"] not in seats or row["seat"] in seen:
            raise Unspecified(
                f"`cohorts.yaml` guards row {n} names the seat {row['seat']!r}, "
                f"{'twice' if row['seat'] in seen else 'which offices.yaml does not carry'}",
                "engine/season/cohorts.yaml",
                needs="one row per `offices.yaml: seats` id",
                law="v9 IN-36 -- one guard per principal's seat; a second doubles the sworn weight under one id")
        seen.add(row["seat"])
    return rows


def _first_holder(w: World, oid) -> "str | None":
    """THE PERSON WHO HOLDS THE OFFICE `oid` (a seat held by two persons reads as the FIRST, `w.tenures` order), or
    `None` when `oid` is `None` or nobody holds it: `seat_guards`' read of a guard's holder and
    `mint_planned_works`' of a works' master (`world_q.hold_force` raises on two live holders; these post at the first)."""
    return next((t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == oid
                 and t.subject in w.persons), None) if oid else None


def _seat_id(row, cid: str) -> str:
    """The Office id a loop-built seat is minted under: its `offices.yaml` row's id where a row stands for
    it (the throne is `off_king`), else the registry slug (`off_<case>`; NPC-084's `guild leader` has no
    row). One owner of the choice, so a test can read the pre-CP-T02-02 ids by replacing it."""
    return row["id"] if row is not None else f"off_{_slug(cid)}"


def seat_guards(w: World, rows: list, authored: dict, partial: bool = False) -> None:
    """SEAT THE GUARD COHORTS IN A BUILT WORLD. Each row becomes a
    Person at the row's weight, its `person` rung, a `contain` edge (where it IS) at the exact rung its seat's
    HOLDER is present at, a `reside` edge at the nearest settlement above that rung (a guard is posted at a
    door and lives in the town, so the capacity ceiling is checked against the town's, as for any cohort),
    and a live `oblige` to the seat -- the edge `world_q.guard_weight` (IN-60) counts. No `commit`, no `hold`,
    no pursuits (SE-06's `temperaments:` covers the population rows only; a guard stands for no place): a guard is a cohort, not a character.

    `authored` is `_office_census["authored"]` (an `offices.yaml` seat id -> the Office id standing for it).
    A seat this world did not seat, or one nobody holds, REFUSES -- unless `partial` (a `cap` dropped the
    cast), where the row is skipped as the per-case loops skip their absent. The holder of a seat held by two
    persons posts the guard at the FIRST (`w.tenures` order)."""
    where = home_of_q(w)
    for row in rows:
        oid = authored.get(row["seat"])
        holder = _first_holder(w, oid)
        if holder is None or holder not in where:
            if partial:
                continue
            raise Unspecified(
                f"`cohorts.yaml` guards the seat {row['seat']!r}, which this realm "
                f"{'did not seat' if oid is None else 'seated and nobody holds, or whose holder stands nowhere'}",
                "engine/season/cohorts.yaml",
                needs="a seat `build_realm` seated, held by a person who is present at a rung",
                law="v9 IN-36 (IN-60's content) -- a guard stands where the principal is; none is guessed")
        post = where[holder]
        town = next((r for r in ancestry(w, post) if w.rungs[r].kind == "settlement"), post)
        wt = row["weight"]
        room = capacity(w, town)
        if wt > room:
            raise Forbidden(
                f"`cohorts.yaml` gives the guard of {row['seat']!r} a weight of {wt}; its town {town!r} "
                f"has capacity {room}", "ED-SE-0051",
                law="RR-2 -- capacity bounds POPULATION; a guard lives in the town and may not stand for "
                    "more people than its dwellings house (checked, never derived)")
        pid = f"{COHORT_PREFIX}guard_{row['seat']}"
        if pid in w.persons or pid in w.rungs:
            raise Unspecified(
                f"guard id {pid!r} is already taken in this world", "engine/season/cohorts.yaml",
                needs="a seat whose guard id no cast member or rung already uses",
                law="v9 IN-36 -- a guard is seated beside the cast, never over it")
        w.persons[pid] = Person(pid, f"the guard of {w.offices[oid].post}", weight=wt)
        w.rungs[pid] = Rung(pid, "person")
        w.add_tenure(Tenure(f"t_{pid}_in", pid, post, "contain", 0))
        w.add_tenure(Tenure(f"t_{pid}_home", pid, town, RESIDE_KIND, 0))
        w.add_tenure(Tenure(f"t_{pid}_oblige", pid, oid, "oblige", 0))


# THE KEYS OF ONE `venues.yaml: planned_works` ROW -- a closed set, so a misspelt key REFUSES rather than
# reading as an absent one (the loader-refuses-per-data-family rule `cohort_rows` and `guard_rows` keep).
PLANNED_WORKS_FIELDS = frozenset({"id", "kind", "plan", "at", "rung", "master", "terms"})


def mint_planned_works(w: World, rows: list, anchors: dict, authored: dict, partial: bool = False) -> list:
    """MINT THE WORKS THE SETTING PLANNED, IN A BUILT WORLD (v10 IN-45, M5 option (B)). Returns the minted ids.

    Each row is ONE `create_record` EFFECT RUN AT TICK 0: `EFFECTS["create_record"]` is handed the act the row's
    master would have declared -- `{record, kind, subject_matter: {plan, at}, rung: <the paying rung>, stages}`
    -- and the `Change` it returns is applied, so the Record, its stages, the master's `hold` and the
    one-live-works-per-target decline are the ones a master's declaring `create_record` writes, with no second mint here (a COMPUTED `create_record`
    carries no payload and mints `text`: `loop/effects_information.py`).
    It is NOT folded: no `Event` is logged, no token is minted, and no driver runs (`build_realm` writes the
    world straight, as every other section of it does); the effect's own `Change` is the writer, which is what
    makes a planned works the same Record a master's act would leave. WHY NOT THROUGH THE GATE (`04` §C.2, *"the seam
    every mutation crosses"*; §A.2, *"The driver is the ONLY constructor of write tokens"*): world generation is none
    of §A.2's nine modules, a builder holds no token and can lawfully hold none, and `build_realm` writes the world
    straight in some two dozen places; the gated route a probe takes (`harness/probes.py`: `w.write(..., mint_token(...),
    change=EFFECTS[...](w, act))`) mints a token outside the driver and logs an Event, so it is not followed here.
    No scan sees a `.apply()` under `harness/`, and none is licensed (`layer-conformance` A3). [ASSUMPTION; medium; Jordan to correct;
    revert: one `create_record` act per row, folded before season 0 -- it moves the log by a `record.created`
    per row and needs a driver in the builder.]

    `anchors` is `build_realm`'s anchor index and `authored` is `_office_census["authored"]` (an `offices.yaml`
    seat id -> the Office id standing for it). `at` and `rung` are anchors, resolved by `resolve_anchor` (a
    building is `{hearth: "<code>:<slug>"}`); `master` is a seat row id and the works' maker is that seat's
    holder -- the first live `hold` on it (`seat_guards`' read). A row whose `kind` is not a record kind that
    carries `{plan, at}` mints a Record WITHOUT that content (`create_record`'s own reading of an act that
    declares none), which `found`, `build` and `work` never name: that is the planted failure
    (`test_in45_planned_works.py`), and why no shipped row is `kind: text`.

    REFUSES (`Unspecified`), each one change from a row that mints: a row that is not a mapping of exactly
    `PLANNED_WORKS_FIELDS`; an `id` already a Record's; a `plan` that `works_cost` does not price (every
    priced key is a `rung_kinds` or `site_kinds` member, `fixtures.py::_check_works_cost`; a place nobody can pay for is dead data, `_cost`'s own
    decline arriving a season late); `terms` that is not a positive integer; an `at` or `rung` that resolves
    to no rung (`resolve_anchor`'s refusal, never a guess); a `master` seat this realm did not seat or nobody
    holds; and a second live works on one `(plan, at)` target (`create_record`'s decline). `partial` (a `cap`
    dropped the cast) skips, without a sound, a row whose master's seat was not seated, as the per-case loops
    skip their absent. No operand is coined: the act carries only what `create_record` already reads."""
    term = w.fixtures.get("record_stage_term")
    priced = w.fixtures.get("works_cost") or {}
    made: list = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != PLANNED_WORKS_FIELDS:
            raise Unspecified(
                f"a `planned_works` row is {row!r}", "engine/season/venues.yaml -- planned_works",
                needs=f"a mapping of exactly {sorted(PLANNED_WORKS_FIELDS)}",
                law="v10 IN-45 -- a misspelt key must refuse, not read as a missing one")
        rid, plan, terms = row["id"], row["plan"], row["terms"]
        whose = f"planned work {rid!r}"
        if not isinstance(rid, str) or rid in w.records:
            raise Unspecified(
                f"{whose} names an id that is not text, or that a Record already carries",
                "engine/season/venues.yaml -- planned_works",
                needs="a unique text id", law="v10 IN-45 -- one Record per id; a mint would replace it")
        if plan not in priced:           # every priced key is a rung or site kind (`fixtures.py::_check_works_cost`, at import, default fixtures)
            raise Unspecified(
                f"{whose} plans {plan!r}, which is no priced `rung_kinds` or `site_kinds` member",
                "engine/season/venues.yaml -- planned_works",
                needs="a plan `found` or `build` can make and `rosters.yaml: works_cost` prices",
                law="v9 IN-28 (H-166 limit 1) -- a plan with no price has nobody to pay for it")
        if isinstance(terms, bool) or not isinstance(terms, int) or terms < 1:
            raise Unspecified(
                f"{whose} declares terms {terms!r}", "engine/season/venues.yaml -- planned_works",
                needs="a positive integer", law="r2 04 §A.6.3 -- a works with no terms bounds nothing")
        oid = authored.get(row["master"])
        master = _first_holder(w, oid)
        if master is None:
            if partial:
                continue
            raise Unspecified(
                f"{whose} names the master seat {row['master']!r}, which this realm "
                f"{'did not seat' if oid is None else 'seated and nobody holds'}",
                "engine/season/venues.yaml -- planned_works",
                needs="an `offices.yaml` seat row `build_realm` seated, held by a person",
                law="v10 IN-45 -- the maker's `hold` is what makes a person a works' master; none is guessed")
        at = resolve_anchor(w, anchors, row["at"], whose)
        payer = resolve_anchor(w, anchors, row["rung"], whose)
        kind = row["kind"]
        act = Act(id=rid, actor=master, verb="create_record", payload={
            "record": rid, "kind": kind,
            "subject_matter": {"plan": plan, "at": at} if kind == WORKS_KIND else None,
            "rung": payer,
            # THE WINDER OF EACH TERM IS `ROOT`: MATTER's `term.matured` names `causes[]` the Event that created
            # the Record, else the stage's third element, and a Record minted without a fold has no Event and no
            # act in the act store to name. The setting planned it -- authored world data, caused by the world.
            # A DELIBERATE DEPARTURE from `04` §A.1's AX-5 row (*"a matured term cites the act that wound it"*): no act
            # wound these terms, `ROOT` is PART D row 6's typed origin, and the card's other route (a folded
            # `create_record` per row, above) would satisfy the row at the price of moving the log and every pin.
            "stages": [(w.tick + (i + 1) * term, f"term{i + 1}", ROOT) for i in range(terms)]})
        change = EFFECTS["create_record"](w, act)
        if change is NO_CHANGE:
            raise Unspecified(
                f"{whose} plans a {plan!r} at {at!r}, where a live works already does",
                "engine/season/venues.yaml -- planned_works",
                needs="one live works per (plan, at)", law="r2 04 §A.6.3 -- `create_record` declines the second")
        change.apply()
        made.append(rid)
    return made


def goals_missing(w: World, rows: tuple) -> list:
    """THE ORGANIZATIONS THIS BUILT WORLD SEATS THAT NO GOAL ROW IS ABOUT (v9 FA-06): `["faction X", "body Y",
    ...]`, in roster order. A faction is seated by an AUTHORED HEAD that stands in the cast (`cast.
    faction_leader`, the same read `seed_goals` binds a faction goal's head by); a body by a live `hold` of
    a seat whose `Office.body` it is. Either needs a row whose `org:` is that faction or body -- a goal of
    any kind, an `orientation` included. A faction with no head and a body with no seated holder
    (`Lions' Helm`, an unfilled seat) is asked for nothing: a goal there binds no one."""
    have = {(g.org_kind, g.org) for g in rows}
    held = {t.object for t in w.tenures if t.kind == "hold" and t.live and t.subject in w.persons}
    seated = {o.body for oid, o in w.offices.items() if o.body and oid in held}
    out = []
    for fac in sorted(FACTIONS):
        if fac in FOREIGN_CAST and faction_prop_id(fac) not in w.propositions:
            continue                      # v9 IN-36: a foreign faction this world did not seat is asked for nothing
        lead = cast.faction_leader(fac)
        if lead and f"p_{_slug(lead)}" in w.persons and ("faction", fac) not in have:
            out.append(f"faction {fac!r}")
    out += [f"body {b!r}" for b in BODY_FACTION if b in seated and ("body", b) not in have]
    return out


def seed_goals(w: World, rows: tuple, authored: dict, cid_of: dict, partial: bool = False,
               complete: bool = True) -> dict:
    """SEED THE ORGANIZATIONS' GOALS IN A BUILT WORLD (v9 IN-68, A-32; ED-IN-0293 (8), (10)). `rows` are
    `data/goals.py` `Goal`s, `authored` is `_office_census["authored"]` (an `offices.yaml` seat id -> the
    Office id that stands for it: since v10 CP-T02-02 the SAME string wherever a row stands for the seat,
    `_seat_id`), `cid_of` the built cast's
    person id -> case id, `partial` true when `cap` dropped part of the cast. Returns the counts
    `census` reports (never read by the loop).

    Per row, `orientation` mints NOTHING -- an OUGHT about nobody is not a motive (the rule at the tie
    write above); it is counted, and its `pursuits:` are IN-69's. Every other kind mints
    `Proposition(goal id, "OUGHT", subject, text, org, 0)` and its org's persons `commit` to it:

      * a faction goal -> the faction's members (the creed's `commit` holders) and its authored head;
      * a body goal    -> the live holders of the seats whose `Office.body` is the body;
      * a seat goal    -> the live holder of the seat.

    `derives` combines levels: `establishes` takes the PARENT goal off every person of the child's org
    (they do not commit to it); `influences` keeps both -- the child's persons ALSO commit to the parent
    goal (v9 FA-05: before, nothing read `influences` and the parent never reached a child org of another
    faction), and its stance rows are written as the parent's own members get theirs, the loyalty being to
    the faction of the org that reached them. [ASSUMPTION; medium; Jordan to correct -- revert: head and
    seat-holders only.] THE CLIMB IS BY ORG, TRANSITIVE WHILE THE CHAIN STAYS `influences`
    [ASSUMPTION; medium; Jordan to correct -- revert: the immediate parent only], and `establishes` takes
    off the one parent only: a person taken off a parent still reaches that parent's `influences`
    ancestors through any org he belongs to (the Riskbreakers' holders `establish` over
    `goal_lowenritter_throne_security` yet commit to the Crown goal as Löwenritter members, which
    `goal_lowenritter_military_security` gives them anyway).

    The subject, per kind: `person` -> that person; `rung` -> the rung (REFUSED if this world built no such
    rung -- a rung exists only once built, so the loader could not check it); `seat_holders` -> the first
    listed seat's Office (`world_q.goal_referents` follows the throne and never reads it); `deed_doers` ->
    the org's own name (read from the ledger at the question, never from the subject).

    A row with `stance` takes a stance row toward each PERSON its referent resolves to at seeding
    (`person`; `seat_holders`' holders now -- a succession moves the referent, never the row), for each
    committed person: `(referent, stance * valence, weight)` from `cast.stance_from_loyalty` of that
    person's loyalty to the org's faction -- the creed's own call, so a `stance: +1` goal reads exactly as
    the creed does, and an opposed member's regard inverts with the sign. [ASSUMPTION; medium; Jordan to
    correct -- revert: the row's sign is the goal's `stance` for every member and only the weight is the
    loyalty's.]

    `partial` drops, without a sound, a goal whose person or seats the cap removed (the per-case loops'
    own rule); a complete cast refuses it. A goal id already a Proposition's refuses (a mint would
    replace it).

    `complete` (v9 FA-06, the SHIPPED DEFAULT) refuses a world that seats an organization no row is about:
    a faction with an authored head, or a body with a seated member, and no goal -- `goals_missing` names
    each. It is the law of the shipped file, so a test that plants a PARTIAL goals file passes `False`
    (`build_realm(..., goals_complete=False)`); `build_realm(goals=False)`, the control arm, mints nothing and
    asks for nothing. [ASSUMPTION; medium; Jordan to correct -- revert: no completeness refusal.]"""
    if complete:
        missing = goals_missing(w, rows)
        if missing:
            raise Unspecified(
                "goals.yaml holds no goal for " + ", ".join(missing),
                "goals.yaml -- completeness",
                needs="a row whose `org:` is each named faction or body (an `orientation` row counts)",
                law="v9 FA-06 -- every faction with an authored head and every body with a seated member holds "
                    "at least one goal; none is guessed")

    def refuse(cls, g, what: str, needs: str):
        raise cls(f"goal {g.id!r}: {what}", f"goals.yaml -- {g.id}", needs=needs,
                  law="v9 IN-68 (A-32) -- a goal is seeded onto what the built realm holds; none is guessed")

    def holders(oids) -> list:
        oids = set(oids)
        return list(dict.fromkeys(t.subject for t in w.tenures
                                  if t.kind == "hold" and t.live and t.object in oids
                                  and t.subject in w.persons))

    def org_persons(g) -> tuple:
        """`(the org's faction name, its persons)` -- the persons a goal of this org binds."""
        if g.org_kind == "faction":
            lead = cast.faction_leader(g.org)
            head = f"p_{_slug(lead)}" if lead else None
            mem = members(w, faction_prop_id(g.org))
            return g.org, mem + ([head] if head in w.persons and head not in mem else [])
        if g.org_kind == "body":
            return BODY_FACTION[g.org], holders(oid for oid, o in w.offices.items() if o.body == g.org)
        oid = authored.get(g.org)
        office = w.offices.get(oid)
        return (office.faction if office else None), (holders([oid]) if office else [])

    out = {"goals": 0, "orientation": 0, "commits": 0, "stance_rows": 0, "dropped": 0}
    bound: dict = {}          # goal id -> (faction name, the org's persons)
    minted: list = []         # (goal, referent persons)
    for g in rows:
        bound[g.id] = org_persons(g)
        kind, obj = g.object["kind"], g.object
        if kind == "orientation":
            out["orientation"] += 1
            continue
        if g.id in w.propositions:
            refuse(Forbidden, g, "its id is already a Proposition of this world",
                   "an id no creed, tie or other goal mints")
        referents = ()
        if kind == "person":
            subject = f"p_{_slug(obj['case'])}"
            if subject not in w.persons:
                if partial:
                    out["dropped"] += 1
                    continue
                refuse(Unspecified, g, f"names {obj['case']!r}, who is not in the cast this realm built",
                       "a case id of the built cast")
            referents = (subject,)
        elif kind == "rung":
            subject = obj["rung"]
            if subject not in w.rungs:
                refuse(Unspecified, g, f"names the rung {subject!r}, which this realm did not build",
                       "a rung id `build_realm` builds")
        elif kind == "seat_holders":
            built = [authored[s] for s in obj["seats"] if s in authored]
            if not built:
                if partial:
                    out["dropped"] += 1
                    continue
                refuse(Unspecified, g, f"names the seats {obj['seats']!r}, none of which this realm seated",
                       "a seat id of offices.yaml")
            subject, referents = built[0], tuple(holders(built))
        else:                                   # deed_doers: read from the holder's ledger at the question
            subject = g.org
        # A `seat_holders` goal carries the Office ids its listed seats BUILT as (`scope`), read through
        # `authored`; a seat that stands for a row keeps the row's id (`_seat_id`), so the map is the identity.
        w.propositions[g.id] = Proposition(g.id, "OUGHT", subject, g.text, g.org, 0,
                                           tuple(built) if kind == "seat_holders" else None)
        minted.append((g, referents))
        out["goals"] += 1
    # `establishes`: the parent goal is off every person of the child's org (an orientation child too)
    taken_off: dict = defaultdict(set)
    for g in rows:
        if g.derives_kind == "establishes":
            taken_off[g.derives_from].update(bound[g.id][1])
    # `influences`: the child's persons ALSO hold the parent goal, and the parent of a parent while the
    # chain stays `influences` (an `establishes` link stops it: that link replaces). Each carries the FACTION
    # OF THE ORG THAT REACHED HIM, so a stance row's loyalty is to his own organization, the parent's own
    # members keeping theirs. [ASSUMPTION; medium; Jordan to correct -- revert: the parent org's faction.]
    by_id = {g.id: g for g in rows}
    reach: dict = {g.id: {pid: bound[g.id][0] for pid in bound[g.id][1]} for g in rows}
    for g in rows:
        cur = g
        while cur.derives_kind == "influences":
            for pid in bound[g.id][1]:
                reach[cur.derives_from].setdefault(pid, bound[g.id][0])
            cur = by_id[cur.derives_from]
    for g, referents in minted:
        for pid, fac in reach[g.id].items():
            if pid in taken_off[g.id]:
                continue
            w.add_tenure(Tenure(f"t_{g.id}_{pid}_commit", pid, g.id, "commit", 0))
            out["commits"] += 1
            if g.stance is None or not referents:
                continue
            r = cast.row(cid_of[pid]) if pid in cid_of else None
            st = cast.stance_from_loyalty(cast.loyalty(r, fac)) if r else None
            if st is None:
                continue                        # no template to be loyal to: no row (the creed's rule)
            for ref in referents:
                w.persons[pid].stance.append((ref, g.stance * st[0], st[1]))
                out["stance_rows"] += 1
    return out


def build_realm(seed: int = 0, cap: int | None = None, from_roster: bool = True,
                goals: bool = True, goals_complete: bool = True, foreign: bool = False,
                guards: bool = False) -> World:
    """The whole map, its buildings, and one person per season loop.

    `foreign` (v9 IN-36) seats the EXTERNAL EMPIRE: the factions `rosters.yaml: foreign_cast` names get their
    root rung, their settlement (no parent, so outside the realm), a Proposition, their cast rows' persons
    homed there, their `offices.yaml: foreign_seats` and their goal rows. `False` (the shipped default) is the
    CONTROL ARM: none of it exists, and the world is byte-identical to the realm before the empire was authored
    (the `foreign_cast` roster says why a faction is a `factions` member in both arms and a world's member in
    one). [ASSUMPTION; medium; Jordan to correct -- the default stays `False` so every golden pinned on the
    default realm stands; flipping it is this one default, plus those goldens' re-record.]

    `guards` (v9 IN-36, carrying IN-60's guard content) seats `cohorts.yaml: guards` -- a cohort of `weight > 1`
    sworn (`oblige`) to a principal's seat, posted at the exact rung the seat's holder is present at. `False`
    (the default) is its control arm, for the same reason. The two switches are independent.
    [ASSUMPTION; medium; Jordan to correct] `guards` ships OFF (as `foreign` does): the on arm moves the realm hash
    and switches on an unmeasured side effect (the guards enter the obligee witness channel and the larder draw),
    so IN-60's EXIT reads on `build_realm(0, guards=True)` until a position flips the default as its own declared
    mover. Revert: the default is `True` and the realm hashes and 1-/2-season pins are re-recorded.

    `goals` seeds `goals.yaml`'s organization goals (`seed_goals`, v9 IN-68). `False` is the CONTROL
    ARM (`harness/decision_spread.py --control`): the same realm with no goal minted, committed to or
    stanced. The shipped file carries rows (FA-05, FA-06), so the arms differ.

    `goals_complete` (v9 FA-06) is the COMPLETENESS REFUSAL's switch, `True` by default: the world that
    seats a faction head or a body member with no goal row refuses, naming it (`goals_missing`). A test
    that plants a deliberately partial goals file passes `False`; nothing else does. Ignored when
    `goals` is `False` (the control arm seeds nothing and asks for nothing).

    `cap` limits the cast for a fast run; `None` seats every case. The cap is a PARAMETER and never
    a hidden default -- a run that quietly seated twenty people while reporting on a hundred and
    forty-three would be the confounded arm `CLAUDE.md` §0.1 pt 1 exists to refuse.

    `from_roster` reads `engine/season/npcs.yaml` for each person's institution, home, want and
    the SUBJECT of their tie. That file is the AUTHORITY on those four fields once it exists.
    `False` forces the derivation and is what `tools/export_npc_roster.py` calls to regenerate --
    the one caller that must not read the file it is about to write.

    ⚠ "THE MATCHERS ARE NOT CONSULTED AT RUNTIME" IS WHAT THE FIRST CUT OF THIS DOCSTRING SAID
    AND IT WAS NOT TRUE. `institution_of` runs over EVERY case on every build, roster or not,
    because the institution index the `institution` tie-rule pools over is built from the cases;
    and `concerns_of` runs for any row whose `concerns` cell is blank. What the roster actually
    buys is that a row it HAS FILLED is never re-derived -- which is the guarantee that matters
    (a hand correction survives) and is narrower than the sentence it replaces.

    ⚠ THE ROSTER IS READ, NOT MERELY SHIPPED. `04 §A.2:124` binds `data/` to RAISE on a
    declared-but-unread row and `01_AXIOMS.md` ID-13 calls such a thing *"a mechanism that does not
    exist, wearing a schema's clothes"*. A roster the loop did not open would be exactly that, and
    the tree has deleted two rosters on that criterion already (`rosters.yaml:69-73`).
    """
    geo, ven = _load(GEOGRAPHY), _load(VENUES)
    w = World(seed, DEFAULT_FIXTURES)

    # -- the canonical layers -------------------------------------------------
    realm = "r_valoria"
    w.rungs[realm] = Rung(realm, "realm")
    # THE ANCHOR INDEX (`resolve_anchor`'s one input), filled at each mint site below -- the only
    # places the key that tells a kind's rungs apart is in hand: the realm is the one (`true`), a
    # duchy is its faction's, a territory and a settlement are their geography codes.
    anchors: dict = {}
    _index_anchor(w, anchors, True, realm)

    # ⚠⚠ **THE TIER THESE 17 ROWS BELONG TO IS `territory`, NOT `province`, AND THAT IS A RATIFIED
    # RULING THIS MODULE WAS ON THE WRONG SIDE OF.** `systems/settlements/reference/scale_hierarchy_v1.md`
    # — **Status: RATIFIED, direct Jordan ruling 2026-07-13** — states the ladder verbatim:
    #
    #     "People in one place comprise settlements comprise territories comprise provinces
    #      comprise duchies comprise country."
    #
    # A TERRITORY IS THE FIXED UNIT HOLDING MULTIPLE SETTLEMENTS, which is exactly what each of
    # geography's 17 rows is (`settlements: [S-001, ...]`). Its `provinces:` key and `# PROVINCES
    # (17)` banner are the label the ruling superseded — and the `T` PREFIX ON EVERY ID WAS RIGHT ALL
    # ALONG. `references/world_initial_state.yaml` (retired at plan position `29d-ii`; open it with
    # `git show fd321c81:references/world_initial_state.yaml`, `:41`) calls the same rows *"the 16
    # territory ids"*, so the two canon files disagreed on the noun and the ruling settles it. §6 of
    # that document lists the propagation as *"tracked, not yet executed … nothing below needs
    # further Jordan input, it needs authoring"*, which is why the stale label survived to here.
    #
    # ⚠⚠ **AND A PROVINCE IS NOT A RUNG AT ALL.** §2: *"Provinces are only formed if the same
    # faction holds the constituent territories … a province is an emergent aggregation that exists
    # only while its constituent territories share a common faction holder."* So it is a QUERY, never
    # a rung this builds — `queries/world_q.provinces_of`. That is the §22 shape arrived at from the
    # other direction: an aggregate that cannot go stale because there is nothing to initialise.
    # `contain_ascends` permits `territory -> duchy` directly (checked: the parent need only be
    # strictly above), so the ladder skipping a conditional tier is legal by construction.
    #
    # **THREE DUCHIES, NOT TWO.** The ruling carries PP-726's duchy tier unchanged: *"3 duchies,
    # unchanged ownership: Almud/Valorsmark, Baralta/Hafenmark, Vaynard/Varfell."* A first writing of
    # this block built two and reasoned that *"the Crown has no duchy — the King governs the realm
    # directly"*, which canon contradicts outright: the Crown's duchy is **Valorsmark**, and Almud
    # holds the realm seat AS WELL, which §5.3 makes the point of him — *"the rulers of a nation are
    # an exception in that they are able to influence duchies/provinces/territories/settlements
    # outside their direct chain of control."*
    #
    # ⚠ THE TENSION OVER VARFELL IS RECORDED RATHER THAN SMOOTHED. `faction_politics_v30.md:246`
    # frames Vaynard as *"first among the Jarls, not a monarch"*; tier-1 `worldbuilding_v30.md:25`
    # says *"Duke of Varfell"*. The rung is a place on a containment ladder and asserts nothing about
    # how the Jarls choose him.
    duchy_of: dict = {}
    for fac_name, duchy_name in (("Crown", "Valorsmark"), ("Hafenmark", "Hafenmark"),
                                 ("Varfell", "Varfell")):
        did = f"duchy_{_slug(duchy_name)}"
        w.rungs[did] = Rung(did, "duchy")
        w.add_tenure(Tenure(f"t_{did}_in", did, realm, "contain", 0))
        duchy_of[fac_name] = did
        _index_anchor(w, anchors, fac_name, did)

    for tid, terr in geo["provinces"].items():          # geography's stale key; the rows are territories
        rid = territory_rung_id(tid)                    # one owner: data/rosters.py
        w.rungs[rid] = Rung(rid, "territory")
        _index_anchor(w, anchors, tid, rid)
        holder = str(terr.get("faction") or "")
        # ⚠ A FOREIGN TERRITORY GETS NO PARENT, AND THAT IS THE POINT RATHER THAN A GAP. Schoenland
        # is on the faction roster and is FOREIGN — `rosters.yaml` records it as not
        # player-eligible, holding its territory and granting or refusing Altonian naval passage —
        # so a `contain` edge into `r_valoria` would assert it is part of the realm. It is a root
        # rung instead, which keeps it out of `descendants(realm)` and therefore out of the
        # realm's `sovereign_fraction`, where counting it would be a canon error wearing a number.
        # `references/world_initial_state.yaml` (retired at `29d-ii`; `git show
        # fd321c81:references/world_initial_state.yaml`, `:44`) made the same cut from the other side:
        # it carried 16 territories and deliberately omitted T16, Schoenland's.
        if holder == "Schoenland":
            continue
        # The Church holds one territory and is not a duchy; an unheld territory has no duchy
        # either. Both hang off the realm, which the ladder permits.
        w.add_tenure(Tenure(f"t_{rid}_in", rid, duchy_of.get(holder, realm), "contain", 0))
    for sid, s in geo["settlements"].items():
        rid = f"set_{_slug(sid)}"
        w.rungs[rid] = Rung(rid, "settlement")
        _index_anchor(w, anchors, sid, rid)
        w.add_tenure(Tenure(f"t_{rid}_in", rid, territory_rung_id(s["territory"]), "contain", 0))

    # -- THE FOREIGN FACTIONS' PLACES (v9 IN-36; `foreign=True` only) ----------------------------------
    # A ROOT territory with no `contain` edge into `r_valoria` -- T16's own shape (above), so it is outside
    # `descendants(realm)`, outside `endings_reached`'s victory selector (every territory under a `realm` rung)
    # and outside `census`'s `uncontrolled_in_realm`. It is a `territory`, NEVER a `realm`: a foreign realm rung
    # would join both of those silently. THAT ABSENCE IS THE BORDER; crossing it is a `march`'s arrival leg
    # (`loop/effects_migration.py::_relocate`), not a path authored here. One settlement under the root is where
    # the faction's persons live. No quarter, building, site or garrison: nothing here is marched on, and the
    # persons are named individuals who do not eat from a larder (`ED-IN-0255`).
    foreign_home: dict = {}
    for fac_name, place in sorted((FOREIGN_CAST if foreign else {}).items()):
        trid, srid = territory_rung_id(place["territory"]["code"]), f"set_{_slug(place['settlement']['code'])}"
        w.rungs[trid] = Rung(trid, "territory")
        _index_anchor(w, anchors, place["territory"]["code"], trid)
        w.rungs[srid] = Rung(srid, "settlement")
        _index_anchor(w, anchors, place["settlement"]["code"], srid)
        w.add_tenure(Tenure(f"t_{srid}_in", srid, trid, "contain", 0))
        foreign_home[fac_name] = (trid, srid)
    # A faction named in `foreign_cast` that this world did not build does not exist in it: no Proposition, no
    # member, no seat, no goal. `absent` is that set, and every site below that reads `FACTIONS` filters by it.
    absent = frozenset(FOREIGN_CAST) - frozenset(foreign_home)

    # -- the authored layers: quarters, then buildings -------------------------
    # ⚠ A SETTLEMENT WITH NO VENUE ROW WOULD SILENTLY HOLD NOBODY, so an unknown type RAISES
    # rather than defaulting. `venues.yaml` covers all seven types the geography uses and a
    # validator asserts that; this is the second reading of the same rule, at the call site.
    buildings_at: dict = defaultdict(list)
    for sid, s in geo["settlements"].items():
        kind = s["type"]
        if kind not in ven["buildings"]:
            raise KeyError(
                f"settlement {sid} is type {kind!r} and `venues.yaml` has no buildings for it. "
                f"A settlement with no building holds nobody and would vanish from the world "
                f"silently. Known: {sorted(ven['buildings'])}")
        srid = f"set_{_slug(sid)}"
        for q in ven["quarters"][kind]:
            qid = f"q_{_slug(sid)}_{q}"
            w.rungs[qid] = Rung(qid, "community")
            w.add_tenure(Tenure(f"t_{qid}_in", qid, srid, "contain", 0))
        for b in ven["buildings"][kind]:
            bid = f"b_{_slug(sid)}_{b['slug']}"
            w.rungs[bid] = Rung(bid, "hearth")
            # THE FIFTH ANCHOR FORM (v10 IN-45): a building is `{hearth: "<geography code>:<slug>"}`, so a
            # `venues.yaml: planned_works` row names a building the way a seat names a settlement — by what
            # tells it apart, never by a built rung id. One more line at a mint site, no branch in the resolver.
            _index_anchor(w, anchors, f"{sid}:{b['slug']}", bid)
            w.add_tenure(Tenure(f"t_{bid}_in", bid, f"q_{_slug(sid)}_{b['quarter']}",
                                "contain", 0))
            buildings_at[sid].append((bid, b))

    # -- a site per producing kind, at the settlement ---------------------------
    # Same rule `build_at` uses, one layer up: `work` needs somewhere to be done, and a world whose
    # sites are all in one place is the co-location defect again by another route.
    for sid in geo["settlements"]:
        for k in sorted(SITE_YIELD):
            if SITE_YIELD[k]:
                s_id = f"s_{_slug(sid)}_{k}"
                w.sites[s_id] = Site(s_id, f"set_{_slug(sid)}", k,
                                     condition=w.fixtures.get("condition_scale"))

    # -- a dwelling per hearth, at the hearth (`ED-SE-0055`, plan position `24d-i`) -----------
    # `ED-SE-0051`'s `capacity(w, rung)` counts *"the rung's dwelling Sites"*, and the
    # buildings above are `hearth` RUNGS, not Sites. Jordan chose the literal reading on
    # 2026-09-25: a `dwelling` site kind, one per hearth rung. The id and starting condition are
    # built the way the producing Sites' are, one layer down: `s_` + the place's key + `_` + kind,
    # at full `condition_scale`. Iterating `buildings_at` covers every hearth this function builds,
    # because the building loop above is its only `hearth` constructor.
    # ⚠ NOTHING READS A DWELLING YET. `capacity` (`24d-ii`) lands with `19c`'s `migrate`. It ships
    # at the control arm, `wear_per_season.dwelling: 0` and an empty `band_floors.dwelling`
    # (`rosters.yaml`, which says why), so it wears nothing and crosses no band. It still emits
    # one `condition.worn` per dwelling per season, because MATTER writes every Site.
    # ⚠ `governance_spine.build` mints dwellings by the same rule. `corpus_run.build_at`,
    # `probes.tiny_world` and `headless.build_world` do not.
    # `engine/season/tests/test_governance_build.py`, section `24d-i`, records why.
    for sid in geo["settlements"]:
        for bid, b in buildings_at[sid]:
            s_id = f"s_{_slug(sid)}_{b['slug']}_dwelling"
            w.sites[s_id] = Site(s_id, bid, "dwelling",
                                 condition=w.fixtures.get("condition_scale"))

    # -- a garrison per settlement, at the settlement (M4, `ED-IN-0279` clause (a)) --------------
    # Jordan ruled WHAT garrison strength is (2026-09-28, M4 planning round 2): a Site's own
    # `condition` field, `world_q.fortification_of`'s reader. One per settlement is the ruling's
    # own scope -- there is no second garrison-bearing rung kind to seed against, and `condition
    # scale` matches every other Site's starting value, so a fresh realm starts every settlement
    # equally fortified: since `20-iv` every settlement march target here is a `WALLS` field.
    # ⚠ READ ON THE BATTLE PATH SINCE PLAN POSITION `20-iv` (`H-150`, `hole_register.yaml`).
    # `seam/wrappers/mass_battle.py` reads `world_q.fortification_of` at the march target and hands
    # it, with the target's territory, to `terrain.py::terrain_row_for_territory`: a garrison at
    # any positive condition makes the field `WALLS`, A.9's defender DR bonus. A garrison worn to
    # condition 0 is no wall. (This comment said "nothing consults this yet" until then.)
    # ⚠ `governance_spine.build`, `corpus_run.build_at`, `probes.tiny_world` and
    # `headless.build_world` do NOT seed a garrison -- the dwelling precedent immediately above is
    # `build_realm`-and-`governance_spine` together; H-150's own docstring and `fortification_of`'s
    # both name only `harness/populated.py`'s build step 11, and widening past that is a separate
    # decision, not this one.
    for sid in geo["settlements"]:
        s_id = f"s_{_slug(sid)}_garrison"
        w.sites[s_id] = Site(s_id, f"set_{_slug(sid)}", "garrison",
                             condition=w.fixtures.get("condition_scale"))

    # -- the cast ---------------------------------------------------------------
    # ⚠ **NPC CASES ARE PEOPLE; ARC CASES ARE NOT, AND THE FIRST CUT SEATED ALL 143.** The NPC
    # lane names persons -- "Carin Vedel", "Inge Baralta", "Orm". The ARC lane names SITUATIONS --
    # "The Unworked Clause", "Vaynard's Wager", "The Penitent Duke". Seating 143 put 97 events in
    # buildings as though they were people, and their "surnames" (`Know`, `War`, `Economy`,
    # `Threshold`) then polluted every name match. Jordan asked for *"as many persons as there are
    # NPC season loops"*, and that count is **46**.
    #
    # ⚠ THE ARC CASES ARE NOT DISCARDED, THEY ARE NOT PEOPLE. What an arc is in this world -- a
    # situation a cast is subject to -- has no carrier yet, and inventing one here would be
    # authoring a mechanism inside a harness. Named as absent rather than faked.
    cases = list(load_cases("NPC"))
    if cap is not None:
        cases = cases[:cap]
    roster = None
    if from_roster:
        try:
            roster = {r["case"]: r for r in (_load(ROSTER).get("npcs") or [])}
        except FileNotFoundError:
            roster = None
    seats = ven["seats"]
    # The unaffiliated are spread over every `serves: []` building on the map, in settlement order,
    # so an unaffiliated life is somewhere ordinary and NOT all in one place.
    commons = [(sid, bid) for sid in geo["settlements"]
               for bid, b in buildings_at[sid] if not b["serves"]]
    n_common = 0
    for case in cases:
        cid = str(case.get("id"))
        pid = f"p_{_slug(cid)}"
        row = (roster or {}).get(cid)
        inst = row.get("institution") if row else institution_of(case)
        home = None
        if row and row.get("home") in w.rungs:
            home = row["home"]
        if home is None and inst is not None:
            sid = seats.get(inst)
            if sid is not None:
                for bid, b in buildings_at[sid]:
                    if inst in b["serves"]:
                        home = bid
                        break
        if home is None:
            home = commons[n_common % len(commons)][1]
            n_common += 1
        # v9 IN-36: a person of a faction this world seated FOREIGN lives at that faction's settlement, over
        # `npcs.yaml`'s home (the roster's home is the realm's derivation, which seats NPC-011 at Lowenskyst's
        # barracks and the two others in Feldmark's commons -- the empire's persons are not in the realm).
        # `foreign_home` is empty unless `foreign=True`, so the control arm reads no faction here.
        if foreign_home:
            fac_here = cast.faction_of(cast.row(cid) or {})[0]
            if fac_here in foreign_home:
                home = foreign_home[fac_here][1]
        w.persons[pid] = Person(pid, str(case.get("name") or cid))
        w.rungs[pid] = Rung(pid, "person")
        w.add_tenure(Tenure(f"t_{pid}_in", pid, home, "contain", 0))
        # Plan position `19c`: and they LIVE there -- the `reside` edge a `move` leaves behind and
        # only a `migrate` re-homes (`loop/effects.py::_eff_migrate`). Every builder mints it beside
        # the first `contain`, so `world_q.residence_of` reads one edge and never falls back.
        w.add_tenure(Tenure(f"t_{pid}_home", pid, home, RESIDE_KIND, 0))
        # ⚠⚠ AUTHORED, NOT DRAWN — AND THE DRAW REMAINS AS THE NAMED FALLBACK IT ALWAYS WAS.
        # `references/npc_registry.yaml` carries a weighted conviction vector for all 46 of these
        # people, cited to canon, using only canonical names (the fifteen pursuits since IN-08's
        # cells commit; the figures below are the thirteen-name roster's, as measured then -- the
        # names they quote are retired, the contrast stands). Nothing that executes had ever
        # opened it, so `seed_pursuits` — a `blake2b(seed, case_id, pid)` draw — was supplying
        # the one quantity that orders every candidate in these worlds. The contrast is not
        # cosmetic: Carin Vedel (NPC-088), whose case is hand-copying SUPPRESSED texts, is authored
        # `Liberty 0.60 / Equity 0.20` and was drawn `Authority 0.90` — the precise opposite of her
        # own case. Almud Almqvist, the King, is authored `Virtue 0.45 / Authority 0.30` and was
        # drawn `Faith 0.90`.
        #
        # ⚠ THE FALLBACK IS NOT DEAD CODE, AND `ID-13` IS WHY THE DISTINCTION MATTERS. It is
        # unreachable on TODAY'S data (46 of 46 rows carry convictions, measured) and it is reached
        # the moment a case is added to the corpus ahead of its registry row — which is the normal
        # authoring order. A `None` here would seed a person with no convictions at all, and a
        # person with no convictions scores every candidate identically, which is `uniform`, the
        # sweep's CONTROL arm, shipped silently as a default.
        #
        # ⚠ `seed_pursuits` IS STILL THE SINGLE OWNER OF THE DRAW (§8) and is still called
        # rather than copied. What changed is which source is consulted first.
        authored = cast.pursuits_of(cast.row(cid) or {})
        w.persons[pid].pursuits = authored or seed_pursuits(seed, cid, pid)
        # IN-08 H10: the religious affiliations, from the same row and NEVER drawn -- a drawn creed
        # is an invented one. No fallback: a row without `affiliations:` holds none (`{}`).
        w.persons[pid].conviction = cast.conviction_of(cast.row(cid) or {})
        # v9 PC-06 K-3 (`H-85`): Thread Sensitivity, from the same row's `ts:`, set here and NEVER
        # written in play. No fallback and no draw: a row with no authored value leaves `None`, and a
        # `None` cannot pass `thread_read`'s gate (`Person.thread_sensitivity`'s comment).
        w.persons[pid].thread_sensitivity = cast.thread_sensitivity_of(cast.row(cid) or {})

    # -- WHO BELONGS TO WHAT ----------------------------------------------------
    #
    # §14.2, verbatim: **"A faction IS a Proposition plus its `commit` edges."** §15's cardinality
    # table annotates `commit : Person -> Proposition, many` as **"this is faction membership"**.
    # The edge was ruled, typed and built; nothing had ever used it for membership, so in every
    # world this repo has constructed the only way to belong to a faction was to hold an office in
    # one — no laity, no rank and file, and `role_templates` keyed on a population that could not
    # exist. `members`, `leaders`, `footprint` and `density` (`queries/world_q.py`) read these
    # edges and return nothing without them.
    #
    # ⚠⚠ **MOOD IS `OUGHT` AND THE SUBJECT IS A PERSON — RULED by Jordan, 2026-09-13: *"Faction
    # creed as an ought: sure. Weight it by their loyalty tho."*** This block previously wrote
    # `HOLDS` and registered the OUGHT as a live design choice it declined to take. The choice was
    # put to Jordan and taken; what follows is the reason the narrowing existed and how the ruling
    # clears it, because the hazard it named is real and is what constrains the SHAPE of the creed.
    #
    # Q4 (`world_q.questions_for`) raises a standing question from every live `commit` to an OUGHT,
    # with `referents = (prop.subject,)`, and `decision/options.py`'s clause 3 is
    # `subject in referents(q)` — so a Proposition's subject becomes the SUBJECT OF EVERY CANDIDATE
    # it generates. Subject the creed on a faction NAME and every faction's members deliberate
    # each season about a string naming no entity in the world. That is the defect `build_at`
    # demonstrated from the other side: its one Proposition pointed at a RUNG and produced **0 of
    # 4,870 acts naming another person** (ED-IN-0210 Ruling 1 — *"verbs invoke mechanisms or
    # interactions between a character and another entity/character. they are not fiats."*).
    #
    # So the creed is subjected on **the faction's authored leader**, a person id, and its
    # CONTENT is the `role_template` — `scope` carries the template name and `value` the faction's.
    # Neither is invented: the leader comes from `rosters.yaml: faction_leaders.by_faction` and the
    # template from `role_templates.by_faction`, both transcribed from `faction_canon_v30.md` §4.
    # This is what the earlier note meant by refusing to invent a creed *"in the one carrier §14.1
    # makes IMMUTABLE"*: the Proposition names canon's own two handles and no authored sentence.
    #
    # ⚠ **A FACTION WITH NO LEADER AND NO TEMPLATE KEEPS `HOLDS`, AND THAT IS THE SILENCE SHOWING
    # THROUGH RATHER THAN A FALLBACK.** `Guilds` and `Schoenland` have neither in canon, so there
    # is no creed to utter and nothing to be loyal to — `cast.loyalty` returns `None` for both for
    # the same reason. `members()` reads a `commit` edge's KIND and OBJECT, never the Proposition's
    # mood, so membership in those two is unaffected; what they lack is a standing question.
    for fac_name in sorted(FACTIONS):
        if fac_name in absent:            # v9 IN-36: a foreign faction this world did not seat has no creed to utter
            continue
        fid = faction_prop_id(fac_name)   # one owner: data/rosters.py
        lead_cid = cast.faction_leader(fac_name)
        lead_pid = f"p_{_slug(lead_cid)}" if lead_cid else None
        template = ROLE_TEMPLATE_OF.get(fac_name)
        if template is None or lead_pid not in w.persons:
            w.propositions[fid] = Proposition(fid, "HOLDS", fac_name,
                                              "is a faction of this world", True, 0)
            continue
        w.propositions[fid] = Proposition(fid, "OUGHT", lead_pid, "carries the creed of",
                                          fac_name, 0, scope=template)
    unplaced: list = []
    for case in cases:
        cid = str(case.get("id"))
        pid = f"p_{_slug(cid)}"
        r = cast.row(cid)
        fac_name, sub, raw = cast.faction_of(r) if r else (None, None, "")
        if fac_name in absent:
            # v9 IN-36: a person of a foreign faction this world did not seat is UNPLACED, exactly as the
            # cell read before the faction was on the roster (`Altonia`, raw) -- counted, not dropped.
            fac_name = None
        if fac_name is None:
            # ⭐ **UNPLACED IS A CORRECT OUTCOME, NOT A PENDING ONE — RULED by Jordan,
            # 2026-09-14: *"Not everyone has to belong to a faction."*** This was carried as an
            # open question for two days; it is closed, and it is closed in the direction that
            # makes the branch below RIGHT rather than tolerated. Six of the 46 name an
            # affiliation on no roster — `Altonia` (3), `Independent (Southernmost Wardens)` (2),
            # the dissolved Virke syndicate (1) — and they stay unaffiliated.
            # (v9 IN-36: `Altonia` has since joined the roster as a FOREIGN faction, so in a
            # `foreign=True` world its three are placed; in the shipped control arm they are
            # unplaced exactly as above, via `absent`. The other three stay off the roster.)
            #
            # ⚠ SO DO NOT "FIX" THIS BY GROWING THE ROSTER. The earlier reading pointed the other
            # way, on Jordan's precedent at `state/carriers.py`'s Office check (*"Wouldn't it just
            # imply that we don't have enough factions?"*), and a later session could reasonably
            # re-derive that and add three faction names. It would be wrong: that precedent is
            # about an OFFICE, which is a seat inside a faction and cannot exist without one. A
            # PERSON is not a seat. An unaffiliated person is a person, and a world where everyone
            # carries a banner has no room for someone who does not.
            #
            # They are still COUNTED rather than dropped — `census` reports `_unplaced_cast`, and
            # `test_the_populated_world_is_not_everybody_in_one_room` asserts
            # `placed + unplaced == persons`, so a person lost to a resolution bug is still
            # distinguishable from a person who belongs to nobody.
            unplaced.append((cid, raw))
            continue
        fid = faction_prop_id(fac_name)   # one owner: data/rosters.py
        w.add_tenure(Tenure(f"t_{pid}_member", pid, fid, "commit", 0))
        # -- AND WHAT THAT MEMBERSHIP IS WORTH TO THEM --------------------------
        #
        # ⭐ Jordan, 2026-09-13: *"The faction one is factored by loyalty."* The `commit` edge says
        # a person belongs; it cannot say how much they mean it, and a faction whose members all
        # pull equally hard is not a political game. So the creed's referent — the leader — gets a
        # STANCE ROW weighted by `cast.loyalty`, and `queries/person_q.py::stance_toward` is what
        # reads it: `valence * weight` summed over the rows naming a candidate's subject, added to
        # every candidate the creed's own Q4 question generates.
        #
        # ⚠⚠ **THE LOYALTY DOES NOT GO ON `Tenure.degree`, WHICH IS WHERE IT OBVIOUSLY BELONGS AND
        # WHERE IT WOULD HAVE DIED.** `degree` is declared on `Tenure` (`state/carriers.py:58`) and
        # MEASURED 2026-09-14 by grep across `engine/season/`: **nothing reads it.** Every `.degree`
        # in the tree is an `Event`'s or a contest's. Writing loyalty there would reproduce exactly
        # the defect the field two lines above it was DELETED for — `carriers.py:48` on `conferrer`:
        # *"It occurred EXACTLY ONCE in the whole tracer — this line — and reached no reader, which
        # by `ID-13` is not a weak field but one that does not exist, wearing a schema's clothes."*
        # A stance row has a reader, so the loyalty changes what people do; on `degree` it would
        # have changed a repr.
        #
        # ⚠ **NO ROW WHERE THERE IS NO CREED, AND NO ROW AT ZERO WEIGHT EITHER.** `stance_from_loyalty`
        # returns `None` for the two template-less factions and `(+1, 0)` at exact indifference,
        # which `stance_toward` sums to the same nothing as an absent row — so an indifferent member
        # is not quietly given a push. The row is appended for it anyway, because `census` counting
        # rows is how a zero-weight member stays visible.
        # ⚠⚠ **THIS TABLE IS THE BASELINE, NOT A REGRESSION CHECK — RULED by Jordan, 2026-09-14:
        # *"whatever you run for the first time IS the baseline since this is new stuff."*** No
        # suite in this tree encodes what a populated world SHOULD do, so none of them could have
        # validated the creed; what validates it is the control arm, and what a first honest run
        # buys is a recorded starting point for the next change to move against. It is deliberately
        # NOT pinned as a golden — a number nobody has argued is correct would be a guard that has
        # not earned its existence (`CLAUDE.md` §0.1 pt 5). The PINNED claims are structural and
        # live in `test_the_populated_world_is_not_everybody_in_one_room`.
        #
        # ⚠ **AND THE ANSWER DEPENDS ON A FIXTURE NOBODY HAS RULED ON.** Control arm = the same
        # build with `cast.faction_leader`
        # stubbed to `None`, so every faction falls back to `HOLDS` and no stance row is
        # written; two seasons each.
        #
        #     creed  rule    seed   acts   other   self   not-a-person   told_by
        #     ----------------------------------------------------------------------
        #     no     first      0    831     175    300            356         7
        #     yes    first      0    814     157    345            312         8
        #     no     first      1    804     183    337            284         8
        #     yes    first      1    800     176    327            297         7
        #     no     all        0    747     272    161            314        10
        #     yes    all        0    665     400    116            149         0
        #     no     all        1    737     270    148            319         8
        #     yes    all        1    653     385    128            140        14
        #
        # Under `all` the creed does what it was ruled for: acts naming ANOTHER PERSON rise 47%
        # (seed 0) and 43% (seed 1). Under `first`, the incumbent default, they move the WRONG WAY
        # on both seeds, -10% and -4%. BOTH signs replicate, so each is the creed and not the seed
        # — which is what makes the inversion a finding rather than a wobble.
        #
        # THE CAUSE IS A STRING PREFIX, AND IT IS `H-54`'s ROW, NOT A NEW ONE. `question_sources`
        # puts `need` LAST, so a creed never displaces a date or a landed claim — but the person's
        # OWN want is also a `need`, and `questions_for` breaks a within-source tie on `q.id`.
        # `q:need:fac_…` sorts before `q:need:prop_…`, so under `first` **every member's faction
        # creed silently outranks their personal ambition, decided by the spelling of an id.**
        # That is exactly the undeclared tiebreak `W-D` measured (*"WHICH QUESTION A PERSON ANSWERS
        # IS SETTLED BY LEXICOGRAPHIC ORDER OVER HASHES"*) and `H-54` owns. Disposition follows
        # `W-D`'s, which is precedent on the identical shape (`CLAUDE.md` §0 step 4): DECLARED and
        # LEFT ALONE — renaming these ids to win the sort would be gaming an undeclared tiebreak,
        # and flipping `question_aggregation_rule` is a design edit to a hole whose own roster note
        # says `first` is kept *"as the sweep's control — not because it is argued for"*.
        # `needs_jordan` is FALSE for the same reason it is on `W-D`.
        #
        # ⚠ AND ONE NUMBER THE CONTROL KILLED: at seed 0 alone, `told_by` fell 10 -> 0 under the
        # creed, which reads as the second-hand channel collapsing. At seed 1 it ROSE, 8 -> 14. It
        # is noise at this corpus size and is NOT reported as an effect (§0.1 pt 4).
        prop = w.propositions[fid]
        st = cast.stance_from_loyalty(cast.loyalty(r, fac_name))
        if st is not None and str(prop.mood).upper() == "OUGHT":
            w.persons[pid].stance.append((prop.subject, st[0], st[1]))
    # Reported by `census`, never read by the loop — the same treatment `_tie_census` gets.
    w._unplaced_cast = unplaced

    # -- WHAT EACH FACTION HOLDS ------------------------------------------------
    #
    # §14.2's closing note is both the licence and the warning: *"A Proposition may be a `hold`
    # subject and is never destroyed, so a memberless faction leaves territory held by a banner
    # nobody carries."* That is how canon's holdings attach at all — `geography_v30.md`'s
    # starting-control table names an owner per PROVINCE and never a person, so the holder has to
    # be the faction, and a faction IS a Proposition. The declared defect is §54's, not repaired
    # here.
    #
    # ⚠ `Uncontrolled` WRITES NO EDGE, AND THAT IS THE MECHANISM WORKING. It is the geography's own
    # value for a province nobody holds; `cast.resolve_faction` returns `None` for it, so the
    # province lands in `sovereign_fraction`'s `undetermined_count` instead of being quietly
    # assigned to somebody. An unheld province is a fact about the world and a thing to play for.
    #
    # ⚠⚠ **ITEM 16, 2026-09-17: THE HOLDER IS THE FACTION'S HEAD, A PERSON, AND THE SENTENCE ABOVE
    # IS SUPERSEDED RATHER THAN DELETED.** §14.2's note is still true about the CARRIER (a
    # Proposition may be a `hold` subject); it was read as a licence and it is a description of a
    # defect. MEASURED on `build_realm(0)` before the change: `hold` Tenures were
    # `{('person', 'Office'): 19, ('faction', 'Rung'): 16}` and `in_holdings` -- *a `hold` whose
    # object is a RUNG* -- was **false for every person over every rung in the world**, so a seat
    # declaring `revocation: "holdings"` refused every revocation forever while looking exactly
    # like a working precondition. `World._refuse_bad_hold` now raises on the old shape
    # (`rosters.yaml: hold_subject_kinds`), so this is not a preference: the old line no longer
    # loads.
    #
    # ⚠ **THE LEADER IS `cast.faction_leader`, THE EXISTING OWNER, AND NO SECOND MAPPING IS MINTED
    # HERE.** The same handle the creed above is subjected on (`rosters.yaml:
    # faction_leaders.by_faction`, transcribed from `faction_canon_v30.md` §4) decides who holds
    # the faction's provinces, so "who heads this faction" has one answer in this file rather than
    # two.
    #
    # ⚠ **AND A FACTION WITH NO AUTHORED HEAD HOLDS NOTHING — THE SILENCE SHOWS THROUGH, AS IT
    # ALREADY DOES FOR THE CREED.** `Guilds` and `Schoenland` have no `leader:` in canon, which is
    # why `members()` gives them no standing question either. MEASURED: of the 16 provinces held,
    # **15 re-home to a person and 1 (Schoenland's) does not**, so one province becomes unheld.
    # That is the same reading `Uncontrolled` already gets one comment up — an unheld province is a
    # fact about the world and a thing to play for — and inventing a holder for it would put a
    # person canon does not name in charge of a territory. Counted, not swallowed: the census
    # reports it below.
    unheld_for_want_of_a_head: list = []
    for tid, terr in geo["provinces"].items():
        held_by = cast.resolve_faction(terr.get("faction"))
        if held_by is None:
            continue
        lead_cid = cast.faction_leader(held_by)
        lead_pid = f"p_{_slug(lead_cid)}" if lead_cid else None
        if lead_pid is None or lead_pid not in w.persons:
            unheld_for_want_of_a_head.append((territory_rung_id(tid), held_by))
            continue
        w.add_tenure(Tenure(f"t_hold_{territory_rung_id(tid)}", lead_pid, territory_rung_id(tid), "hold", 0))
    # v9 IN-36: and a foreign faction holds its own root territory, by its head -- the same `hold` a realm
    # territory's holder has, so `holder_faction_of` reads the empire's settlement as the empire's (a `march`
    # INTO it is opposed, and a seat there can `seize` what it holds). No head, no hold: the silence shows.
    for fac_name, (trid, _srid) in sorted(foreign_home.items()):
        lead_cid = cast.faction_leader(fac_name)
        if lead_cid and f"p_{_slug(lead_cid)}" in w.persons:
            w.add_tenure(Tenure(f"t_hold_{trid}", f"p_{_slug(lead_cid)}", trid, "hold", 0))
    # Reported by `census`, never read by the loop — the same treatment `_tie_census` gets.
    w._unheld_for_want_of_a_head = unheld_for_want_of_a_head

    # -- WHO GOVERNS: OFFICES AND TITLES ----------------------------------------
    #
    # ⭐ RULED by Jordan, 2026-09-13: *"a faction is not just comprised of people but also offices
    # and titles."* Membership above is the people; this is the other two. Until now a populated
    # world held **zero offices** — `leaders()` returned nothing for every faction, `remit:`
    # eligibility matched nobody, and the whole governance surface was reachable in principle and
    # empty in fact.
    #
    # ⚠ **BUILT FROM `references/npc_registry.yaml`'s `role`, NOT FROM THE PROSE TABLES, AND THAT
    # CHOICE IS WHAT MAKES IT SAFE.** An adversarial pass found `faction_politics_v30.md` §1.2c/
    # §1.3c and `npc_behavior_v30.md` §2.16/§2.17 disagreeing about Inner Circle membership BY
    # HALF — four against two for Hafenmark, five against two for Varfell, with two survivors given
    # different Conviction and Resonant-Style values. ⭐ Jordan ruled it the same day: *"NPC
    # behaviour supersedes faction politics"* (recorded at `rosters.yaml`'s precedence block as
    # tier 2a). MEASURED: the registry already matches the superseding document on every contested
    # cell, so reading `role` per person builds to the ruling and never touches the contested
    # prose.
    #
    # ⚠ `body` IS `None` FOR ALL BUT THE THREE AUTHORED OVERLAYS, AND THAT IS HONEST RATHER THAN
    # LAZY. §11 makes `rung?` optional and `office_bodies` carries a faction's TOP organs only —
    # `Ministries` is one row by the ruling at `rosters.yaml`'s `office_bodies` note, the four Cardinals are there and
    # the four Dicasteries under them are not, and Hafenmark's Committees and Varfell's Councils
    # are absent entirely. MEASURED: only 10 of 25 canon-named seats can construct with a body.
    # An office with a declared FACTION and no body is lawful (`office_faction(None, declared)`)
    # and says exactly what is known: who they answer to, not which organ they sit in. Expanding
    # `office_bodies` is a data edit and is the next unit, not this one.
    #
    # ⚠ THE THREE OVERLAYS WIN WHERE THEY EXIST. `cases/exercises/{NPC-008,NPC-033,NPC-038}.yaml`
    # carry an authored `office:` block — post, body-or-faction, and a `remit:` read from the
    # case's own nouns with the reasoning attached. They are the tree's own worked examples of how
    # an office is authored, so they are read rather than overridden, and their `body`/`faction` is
    # taken as-is so a derived faction cannot be forced to disagree with the constructor.
    #
    # ⚠ EVERY OTHER OFFICE CARRIES `remit_acts: []`, WHICH IS A DECLARED ABSENCE. Canon states no
    # per-post remit, and the five remit acts are a CLOSED set whose members gate verbs — inventing
    # one would silently hand somebody an authority nobody granted. An empty remit is lawful and
    # grants nothing.
    # ⚠⚠ **AMENDED 2026-09-18: THE SEATING BELOW NOW FILLS AN EMPTY REMIT FROM
    # `rosters.yaml: remit_default`, WHICH IS THE THING THIS PARAGRAPH REFUSES TO DO.** The refusal
    # is correct AS CANON and is not overturned — Jordan asked for a generic remit explicitly and
    # only *"for testing purposes for now"*, so the tree hands out an authority nobody granted, ON
    # PURPOSE, and says so in three places rather than letting it look canonical. The default is
    # transparently wrong (every office gets every act), which is what stops it reading as design.
    # This paragraph stays because it states the standard the default is an exception to, and the
    # per-POST remits that replace it must meet it.
    from .corpus_run import RESCALES as overlays   # deferred — `data/__init__` records what eager costs
    seated, no_post, occupations, proposed = 0, [], [], []
    # `offices.yaml` row id -> the Office id that stands for it (matched below, or minted after the
    # loop), and the loop-built offices no row matches. Both reported by `_office_census`.
    authored: dict = {}
    unauthored: list = []
    for case in cases:
        cid = str(case.get("id"))
        pid = f"p_{_slug(cid)}"
        r = cast.row(cid)
        if r is None:
            continue
        fac_name, _sub, _raw = cast.faction_of(r)
        if fac_name is None or fac_name in absent:
            continue                          # unplaced above; an office needs a faction (§11)
        over = (overlays.get(cid) or {}).get("office") or {}
        title = cast.title_of(r)
        governs = title_domain(title) if title else None
        # ⚠⚠ **AN OFFICE IS A SEAT, NOT AN OCCUPATION, AND THE FIRST CUT OF THIS BLOCK CONFLATED
        # THEM.** It gave every placed person an Office named after their registry `role`, which
        # made `leaders(w, faction) == members(w, faction)` for every faction — everybody a
        # leader, the word meaning nothing, and no seat scarce enough to be worth competing for.
        # §11 is the corrective: an Office carries `conferral`, `revocation`, `establishment[]` and
        # `upkeep`. A copyist and a hedge-school teacher have none of those; they have work.
        #
        # THE DISCRIMINATOR IS AUTHORED, NOT INFERRED. `references/npc_registry.yaml` packs a
        # SUB-ORGANIZATION into its `faction` cell — `Crown (Inner Circle)`, `Hafenmark (Inner
        # Council)`, `Varfell (Jarl Council)`, `Crown (Ministry)`, `Crown (Royal Family)` — and an
        # occupation carries none. So: a sub-organization, a title on the governance ladder, or an
        # authored `office:` overlay. Anything else is a life, and the registry still records what
        # they do.
        #
        # ⚠ `Royal Family` SEATS ONE, AND THAT IS THE MARGINAL CALL SAID OUT LOUD. A lineage is not
        # an organ, but the three rows it covers are the Heir Apparent, the Widow Regent and a
        # Princess married into Altonia — succession seats, which is the one thing a `hold` on a
        # realm-scale office is for. Recorded rather than silently included.
        if not (over or governs or _sub):
            occupations.append(cid)
            continue
        # A TITLED POST IS THE BARE TITLE, so `title_domain` resolves and `Office.__post_init__`
        # sets `scope_rung` to the rung it governs. `role` carries the same fact as prose
        # ("Duke (Varfell Leader)"), which that lookup cannot match.
        post = str(over.get("post") or (title if governs else r.get("role") or "")).strip()
        if not post:
            no_post.append(cid)
            continue
        # ⚠ THE SUB-ORGANIZATION BECOMES THE `body` WHERE IT NAMES ONE, AND THE GAIN IS THE
        # CONSTRUCTOR'S CROSS-CHECK, NOT THE FIELD. With a body, `office_faction` DERIVES the
        # faction and refuses a body/faction mismatch; with `body=None` the faction is taken on the
        # caller's word. So a Crown person whose row said `Hafenmark (Inner Council)` now raises
        # instead of seating quietly. EXACT MATCH, not substring: `Inner Circle / Löwenritter
        # Liaison` (NPC-035) and `dual-loyalty: Crown Inner Circle agent…` (NPC-034) resolve to
        # nothing and keep `body=None`, which is honest — each names two allegiances and canon has
        # no organ for either shape.
        body = over.get("body") if over else (_sub if _sub in BODY_FACTION else None)
        # ⚠ `offices.yaml`'S OVERLAY (plan position `8a`, `13d-i` item 5, then `13d-iii`). The seat
        # this loop builds is MATCHED to its authored row by `holder` case id, and the row's
        # `rung` (resolved -- `resolve_anchor`), `remit_acts`, `conferral` and `revocation` are laid
        # on it; the loop's own `post`, `body` and `faction` stand (a post normalisation is a
        # separate unit -- `rosters.yaml: remit_default`'s note). Before `13d-iii` this overlaid
        # the two bases only: 21 of the 24 seats it builds carried NO rung (`H-163` limit 1, a
        # titled holder's `governs` was the one rule that gave one), so a holder's purview was
        # empty and `requisition`/`issue`/`open_case` refused on `authority`.
        # A case may name MORE than one row (NPC-020 holds two): match on `post` first, the one
        # field both this loop and `offices.yaml` author independently. `offices.yaml`'s `post` is
        # a NORMALISED spelling for three rows (`03` §A.15 rows 5, 14, 17 -- a live registry post
        # carrying a parenthetical condition or a co-title, e.g. "Queen (Widow Regent if Almud
        # eliminated)" against the authored `Queen`), so a holder with exactly ONE row is matched
        # on the case id alone rather than left unmatched by a spelling this fold does not correct.
        _off_candidates = OFFICES_BY_HOLDER.get(cid, ())
        if len(_off_candidates) == 1:
            _off_row = _off_candidates[0]
        else:
            _off_row = next((cand for cand in _off_candidates if cand.get("post") == post), None)
        oid = _seat_id(_off_row, cid)
        if _off_row is not None:
            rung = seat_anchor(w, anchors, _off_row)
            # `held` is what this seat would have had without the overlay: the acts `offices.yaml:
            # meta: remit_unruled` names survive it (`authored_remit`), the rest is the row's.
            remit = authored_remit(_off_row, remit_or_default(over.get("remit")))
            authored[_off_row["id"]] = oid
        elif governs is not None:
            # A TITLED holder with no authored row would be seated rungless, silently -- the one
            # derivation that used to give it a rung is gone with the second mechanism it was.
            raise Unspecified(
                f"{cid} holds the title {title!r} and `offices.yaml` has no row for the seat",
                "offices.yaml -- seats",
                needs="a row naming this holder, so the seat has an anchor",
                law="a titled seat sits at the rung its title governs (r2 03 §A.8); no row, no rung")
        else:
            # THE DECLARED EXCEPTION: a seat the registry derives and no row authors (NPC-084's
            # `guild leader`, measured). It has no anchor to resolve and invents none.
            rung, remit = None, remit_or_default(over.get("remit"))
            unauthored.append(oid)
        w.offices[oid] = Office(
            oid, post, rung, remit,
            scope_rung=rung,
            body=body,
            faction=(over.get("faction") if over else None) or (None if body else fac_name),
            conferral=(_off_row or {}).get("conferral"),
            revocation=(_off_row or {}).get("revocation"),
        )
        w.add_tenure(Tenure(f"t_{oid}_hold", pid, oid, "hold", 0))
        seated += 1
        # ⚠ A PROPOSED SEAT IS SEATED AND COUNTED AS PROPOSED. The registry marks 35 rows
        # `canonical` and 11 `proposed`, and the two council members that EXCEED
        # `npc_behavior_v30.md` §2.16/§2.17's two-per-council — the ruling's superseding
        # document — are exactly two of the proposed ones (NPC-081, NPC-082, whose `#4` /
        # `#5` seat numbers YAML ate as comments). Dropping them would discard authored
        # work; hiding the distinction would let a proposal read as canon a session later.
        if str(r.get("status")) != "canonical":
            proposed.append(cid)
    # -- THE AUTHORED SEATS NO LOOP-BUILT SEAT STANDS FOR: MINTED FROM THE ROW ALONE ---------------
    # (`13d-iii`.) The loop seats a person from the registry; it never saw these holders as seated
    # (measured: six of `offices.yaml`'s 29 rows -- the King's second seat and five people the
    # registry gives no seat). The row IS the seat -- id, post, body/faction, rung, remit, bases --
    # and its holder takes it with a `hold`. A row's holder must be a person the cast built (a seat
    # nobody can sit in would be a ghost in `leaders`), and a minted seat grants exactly its
    # authored remit: it held nothing before, so nothing is "kept" (`authored_remit`).
    minted: list = []
    # v9 IN-36: and the foreign seats of the factions this world seated (`offices.yaml: foreign_seats`).
    seat_rows = tuple(OFFICES_SEATS) + tuple(r for r in FOREIGN_SEATS if r["faction"] in foreign_home)
    for row in seat_rows:
        if row["id"] in authored:
            continue
        pid = f"p_{_slug(row['holder'])}"
        if pid not in w.persons and cap is not None:
            continue                  # a deliberately partial cast: the per-case loop skips its absent too
        if pid not in w.persons:
            raise Unspecified(
                f"{row['id']} names the holder {row['holder']!r}, who is not in the cast this "
                f"realm built", "offices.yaml -- seats",
                needs="a holder from the built cast (a `cap` that drops the cast drops the seat)",
                law="r2 03 §A.14 -- the holder is a case id in the cast")
        # a person the cast built may still have no registry row (the per-case loop above skips
        # `r is None` for the same reason), and the seat's `proposed` status is read off that row
        holder_row = cast.row(row["holder"])
        if holder_row is None:
            raise Unspecified(
                f"{row['id']} names the holder {row['holder']!r}, who is in the cast this realm "
                f"built but has no `npc_registry.yaml` row", "offices.yaml -- seats",
                needs="a holder with a registry row, so the seat's canonical/proposed status is known",
                law="r2 03 §A.14 -- the holder is a case id in the cast; the registry row is what "
                    "says whether the seat is canon or proposed")
        rung = seat_anchor(w, anchors, row)
        if row["id"] in w.offices:
            # a MINTED seat is one no loop-built seat stands for, so its id must be fresh: the
            # assignment below would otherwise REPLACE the seat already standing under it, and its
            # holder's `hold` would then name a different office than the one he sat in
            raise Forbidden(
                f"the minted seat {row['id']!r} names an id a seat already stands under "
                f"({w.offices[row['id']].post!r})", "offices.yaml -- seats",
                needs="a seat id no other seat in the realm carries",
                law="one seat per id -- a minted row that reuses an id overwrites the seat it "
                    "names without a sound")
        w.offices[row["id"]] = Office(
            row["id"], row["post"], rung, authored_remit(row), scope_rung=rung,
            body=row.get("body"), faction=row.get("faction"),
            conferral=row.get("conferral"), revocation=row.get("revocation"))
        w.add_tenure(Tenure(f"t_{row['id']}_hold", pid, row["id"], "hold", 0))
        authored[row["id"]] = row["id"]
        minted.append(row["id"])
        seated += 1
        if str(holder_row.get("status")) != "canonical":
            proposed.append(row["holder"])
    # -- A SEAT'S OBLIGEES SERVE IT (`obligees:`; `04 §B.7` call 2: a council is one seat and many
    # holders, through `oblige`). Opened with no term: `term?` is lawful null, and a seat seeded at
    # world-gen has no opening act to declare one (`_eff_oblige` is the act that does).
    for row in seat_rows:
        seat = authored.get(row["id"])
        if seat is None:
            continue                  # a `cap` dropped this seat's holder, so the seat does not exist
        holder_pid = f"p_{_slug(row['holder'])}"
        for ob in row.get("obligees") or ():
            opid = f"p_{_slug(ob)}"
            if opid == holder_pid:
                # checked BEFORE the `cap` skip below: a seat's holder does not serve his own seat,
                # whether or not a partial cast kept him (`_req_oblige` clause 3's rule)
                raise Forbidden(
                    f"{row['id']} lists its own holder {row['holder']!r} among its obligees",
                    "offices.yaml -- seats",
                    needs="obligees other than the seat's holder",
                    law="`_req_oblige` clause 3 -- the occupant is not his own seat's obligee")
            if opid not in w.persons and cap is not None:
                continue
            if opid not in w.persons:
                raise Unspecified(
                    f"{row['id']} names the obligee {ob!r}, who is not in the cast this realm "
                    f"built", "offices.yaml -- seats",
                    needs="an obligee from the built cast", law="r2 03 §A.14 -- `obligees` are case ids")
            w.add_tenure(Tenure(f"t_{seat}_oblige_{_slug(ob)}", opid, seat, "oblige", 0))
    # The index `resolve_anchor` read, kept on the world so a test can resolve a form no row uses
    # (`{settlement: ...}`) and so a mutated resolver is observable. The loop never reads it.
    w._anchors = anchors
    w._office_census = {"seated": seated, "no_post": no_post,
                        "occupations": occupations, "proposed_seats": proposed,
                        "authored": authored, "minted": minted, "unauthored": unauthored}

    # -- WHAT EACH PERSON WANTS, AND WHO IT CONCERNS ----------------------------
    #
    # ⚠ WITHOUT THIS THE WORLD BUILDS AND NOBODY ACTS -- measured: 143 persons, 77 buildings,
    # **0 acts by 0 actors** over a full season. `questions_for` raises a question from a Date
    # coming due (Q1), a claim the person holds (Q2), a band (Q3), or a Proposition they have a
    # live `commit` to (Q4). A world seeded with none of those gives every person an empty option
    # set, and an empty option set is not a quiet world -- it is no world at all.
    #
    # ⚠ THE WANT IS THE CASE'S OWN, NOT A CONSTANT. `wants_of` reads the first `core` row of
    # `season_requires`; the corpus declares 427 of them. The first cut of this module gave all
    # 143 people the string "a standing ambition", which is `build_at`'s identical-people defect
    # rebuilt at scale.
    #
    # ⚠ THE SUBJECT IS A PERSON, WHICH IS RULED RATHER THAN CHOSEN. `ED-IN-0210` Ruling 1
    # (Jordan, 2026-09-10): *"verbs invoke mechanisms or interactions between a character and
    # another entity/character. they are not fiats."* `world_q`'s Q4 emits `(prop.subject,)` as
    # the referent, so a person-subject Proposition is the whole difference between an act about a
    # granary and an act about somebody. `corpus_run.build_at` points its one Proposition at a
    # RUNG, and 0 of its 4,870 acts name another person.
    #
    # THE TIE, IN PRIORITY ORDER, EACH WEAKER THAN THE LAST AND EACH SAID OUT LOUD:
    #   1. a person another case NAMES in `who_acts` -- 11 real ties, used first;
    #   2. somebody at the seat of an INSTITUTION the case names -- the 583 role entries;
    #   3. a person under the same roof;
    #   4. a person in the next inhabited building.
    # Nobody is tied to a stranger by a draw. A draw here would read as a relationship and be one
    # only by accident, which is the scripting drift `CLAUDE.md` §10 names.
    by_home: dict = defaultdict(list)
    for t in w.tenures:
        if t.kind == "contain" and t.live and t.subject in w.persons:
            by_home[t.object].append(t.subject)
    homes = sorted(by_home)
    home_of = {pid: home for home, mates in by_home.items() for pid in mates}
    by_name = surname_index(cases)
    at_institution: dict = defaultdict(list)
    for case in cases:
        # ROSTER WINS HERE TOO, as at seating -- and SPELLED THE SAME WAY, which the first cut was
        # not: `or institution_of(case)` re-derives on a FALSY roster value, and `npcs.yaml` ships
        # `institution: null` and documents it as *"null for an unaffiliated life"*. That spelling
        # honoured a hand-set null at seating and silently overrode it here.
        _row = (roster or {}).get(str(case.get("id")))
        inst = _row.get("institution") if _row else institution_of(case)
        if inst:
            at_institution[inst].append(f"p_{_slug(str(case.get('id')))}")

    ties = Counter()
    tie_of: dict = {}
    for n, case in enumerate(cases):
        cid = str(case.get("id"))
        pid = f"p_{_slug(cid)}"
        row = (roster or {}).get(cid)
        # ⚠ THE ROSTER'S `want` APPLIES ON EVERY BRANCH, AND THE FIRST CUT APPLIED IT ON ONE.
        # It read `row["want"]` inside the roster-tie branch alone, so a hand-corrected want was
        # DISCARDED for any row whose `concerns` was blank -- the file being the authority on one
        # field and not on the next, which is exactly the silent-drift the roster exists to end.
        # (It is a no-op on today's data, because every roster `want` was exported from
        # `wants_of`. It stops being one the first time somebody edits a row, which is the point.)
        want = str(row["want"]) if row and row.get("want") else wants_of(case)
        about = why = None
        if row and row.get("concerns"):
            cand = f"p_{_slug(str(row['concerns']))}"
            if cand in w.persons and cand != pid:
                about, why = cand, "roster"
        if about is None:
            named, inst = concerns_of(case, by_name)
            if named is not None:
                cand = f"p_{_slug(named)}"
                if cand in w.persons and cand != pid:
                    about, why = cand, "named"
            # ⚠ ONE LOOP, NOT THREE NEAR-COPIES — and they HAD drifted before this was folded
            # (2026-09-15): the institution branch carried an extra `q in w.persons` guard the
            # other two lacked, which is the copies starting to disagree. The guard is now applied
            # to every tier, which is what each branch meant; a change to the pick rule (the
            # modulo, or a fifth tier) is one edit.
            nxt = homes[(homes.index(home_of[pid]) + 1) % len(homes)] if homes else None
            tiers = ((at_institution.get(inst, []) if inst is not None else [], "institution"),
                     (by_home.get(home_of.get(pid, ""), []), "roof"),
                     (by_home.get(nxt, []), "neighbour"))
            for candidates, tag in tiers:
                if about is not None:
                    break
                pool = [q for q in candidates if q != pid and q in w.persons]
                if pool:
                    about, why = pool[n % len(pool)], tag
        # ⚠ ONE WRITE, AFTER THE WHOLE CHAIN. The roster branch used to carry its own copy of the
        # Proposition and the `commit` Tenure and then `continue`, so the two paths were free to
        # disagree about what a tie WRITES -- and they did, on `want`, above. A person with no tie
        # at all is the one case that writes nothing: an OUGHT about nobody is not a motive.
        if about is None:
            continue
        ties[why] += 1
        tie_of[cid] = why
        prop_id = f"prop_{_slug(cid)}"
        w.propositions[prop_id] = Proposition(prop_id, "OUGHT", about, want, True, 0)
        w.add_tenure(Tenure(f"t_{prop_id}_commit", pid, prop_id, "commit", 0))
    w._tie_census = dict(ties)   # reported by `census`, never read by the loop
    # WHICH RULE CHOSE EACH TIE, per case. Read by `tools/export_npc_roster.py` to fill the
    # roster's `tie` column -- provenance a human needs to tell a real tie (`named`) from a
    # filler one (`neighbour`) before correcting a row -- and by its `--check` round-trip. The
    # loop never reads it; the exporter is why it is not a field nothing reads.
    w._tie_of = tie_of

    # -- WHAT EACH ORGANIZATION IS FOR: THE GOALS (v9 IN-68, A-32) ---------------------------------
    # AFTER the creed (its members are the faction goal's), the offices (a body's and a seat's holders)
    # and the ties (so a goal Proposition cannot enter a tie's pools), and before the cohorts, which
    # commit to nothing. World-gen only: a person committed here stays committed through a succession
    # unless a `release` ends it, while a `seat_holders` referent follows the seat (IN-67). `goals=False`
    # builds the control arm; the shipped `goals.yaml` carries rows (FA-05, FA-06), so the arms differ.
    # v9 FA-06: the world that seats an organization no row is about REFUSES (`goals_complete`).
    w._goal_census = seed_goals(
        w, tuple(g for g in goals_data.goals() if goals_data.org_faction(g.org_kind, g.org) not in absent)
        if goals else (), w._office_census["authored"],
        {f"p_{_slug(str(c.get('id')))}": str(c.get("id")) for c in cases}, partial=cap is not None,
        complete=goals and goals_complete)

    # -- THE POPULATION: ONE AUTHORED COHORT PER POPULATED RUNG (plan position `24f`) ------------
    #
    # ⭐ `ED-IN-0255` (Jordan, 2026-09-18): subsistence is *"a territorial issue"*, carried by *"NPC
    # synecdoches that just represent the overall population affected"*, and *"lords and guild
    # members"* do not worry about it. So the larder draw feeds only cohorts
    # (`world_q.subsistence_draw`), and THIS is where the realm gets its cohorts: `cohorts.yaml`,
    # authored rows read once here (`ED-WR-0011` option A -- no clock and no formula mints one).
    #
    # ⚠ LAST, AFTER THE WHOLE CASE-DERIVED CAST, AND THAT ORDER IS WHAT KEEPS IT A SECOND SEED
    # RATHER THAN AN EDIT TO THE FIRST. The module docstring's *"the cast comes from the case"*
    # governs everything above unchanged: every tie, membership, holding and office has been
    # decided before a cohort exists, so none of them can land on one (the `roof`/`neighbour`
    # tiers pool over `contain` edges, and would otherwise tie an NPC's want to a crowd), and
    # `tools/export_npc_roster.py`'s derivation is untouched.
    # ⚠ AND AFTER THE DWELLINGS, because the ceiling reads `capacity`, which counts them.
    names = {f"set_{_slug(sid)}": str(s.get("name") or sid)
             for sid, s in geo["settlements"].items()}
    seat_cohorts(w, cohort_rows(), names, temperament_rows())
    # v9 IN-36 (IN-60's content): AFTER the population cohorts, so a guard never lands on a population row's
    # id or capacity read, and AFTER the seats, whose holders it is posted beside. `guards=False` seats none.
    if guards:
        seat_guards(w, guard_rows(), w._office_census["authored"], partial=cap is not None)
    # v10 IN-45 (M5, option (B)): THE WORKS THE SETTING PLANNED, minted LAST so no tie, creed, seat, goal or
    # cohort above can have read them -- the build up to here is byte-identical to the realm without this
    # block, which is the control (an empty `planned_works:` reads the old hash). `venues.yaml: planned_works`.
    mint_planned_works(w, ven.get("planned_works") or [], anchors, w._office_census["authored"],
                       partial=cap is not None)
    return w


def census(w: World) -> dict:
    """What was built, counted from the world rather than from the inputs."""
    kinds = Counter(r.kind for r in w.rungs.values())
    # §8: `world_q.home_of` owns "where is everyone"; this used to roll its own copy, and so did
    # three other sites (see that query's docstring).
    where = home_of_q(w)
    # ⚠ THE SUBSISTENCE ROWS ARE ITEM 3a's EXECUTION ARTIFACT, and they exist because the number
    # that mattered was invisible. Before the larder ladder, `build_realm(0)` after one season
    # held 4,810 units at the 37 settlements and 0 at the 211 hearths, while every person lived
    # in a hearth — so the draw ran at 0 rungs and the census reported a thriving economy nobody
    # could eat from. `stores_by_rung_kind` is where the food IS; `eaters_short` is who could not
    # reach it. Both are read from the world, never from the inputs.
    stores_by_kind: Counter = Counter()
    for r in w.rungs.values():
        for k, v in (r.stores or {}).items():
            stores_by_kind[r.kind] += v
    short = getattr(w, "_subsistence_shortfall", {})
    # REM-50: one walk of the larder ladder for every settlement's `hunger`, never one per call.
    next_draw = subsistence_draw(w)
    hunger_bands = Counter(hunger(w, r.id, next_draw)[0] for r in w.rungs.values() if r.kind == HUNGER_KIND)
    # `24f`: the cohorts are persons (S9.1), so `persons` counts them; these two rows separate them
    # from the cast, read off the world (`Person.is_cohort`) rather than off `cohorts.yaml`.
    cohorts = [p for p in w.persons.values() if p.is_cohort]
    return {"rungs": dict(kinds), "persons": len(w.persons), "sites": len(w.sites),
            "cohorts": len(cohorts), "cohort_weight": sum(p.weight for p in cohorts),
            "ties": getattr(w, "_tie_census", {}), "propositions": len(w.propositions),
            # v9 IN-68: what `seed_goals` minted, a report and never read by the loop. `orientation`
            # rows are loaded and counted and mint nothing; `dropped` is the cap's.
            **{(k if k == "goals" else f"goal_{k}"): getattr(w, "_goal_census", {}).get(k, 0)
               for k in ("goals", "orientation", "commits", "stance_rows", "dropped")},
            "distinct_buildings_inhabited": len(set(where.values())),
            "largest_building": max(Counter(where.values()).values()) if where else 0,
            "stores_by_rung_kind": dict(sorted(stores_by_kind.items())),
            "eaters_short": len(short),
            "unheld_for_want_of_a_head": len(getattr(w, "_unheld_for_want_of_a_head", [])),
            # `24h` P5: the revolt Query's only caller (r2 `05` §A.1.5 RULED (d),
            # `establishment_of`'s precedent). A report, not a rule: it feeds no decision and moves no hash.
            # Summed over REALM rungs: `terr_T16` is a root rung outside the realm (see `build_realm`), so
            # it is not counted.
            "uncontrolled_in_realm": sum(len(uncontrolled(w, r.id))
                                            for r in w.rungs.values() if r.kind == "realm"),
            # v9 IN-35: the Calamity's effect per territory (`world_q.closed_uses`, a Query over band
            # floors), its one reader -- `uncontrolled`'s precedent above: a report, not a rule. Each
            # territory with a Site below a floor, and how many such Sites it holds.
            "sites_below_a_floor_by_territory": {
                r: n for r in sorted(w.rungs) if w.rungs[r].kind == "territory"
                if (n := len(closed_uses(w, r)))},
            # REM-50: `world_q.hunger`'s only caller until CP-T10-05 -- `uncontrolled`'s precedent above: a
            # report, not a rule. Each settlement's band, from the NEXT draw; D = 0 counts as `fed`.
            "hunger_by_settlement": dict(sorted(hunger_bands.items()))}


def run(seasons: int = 1, seed: int = 0, cap: int | None = None, w: World | None = None) -> dict:
    """Build it and tick it. Returns the census plus what the season did.

    `w` takes a world ALREADY BUILT, for a caller that wants to report on the build before the
    season runs -- `main` below is the one, and without this it built the whole realm twice
    (~10s each) to print a census it then discarded.

    ⚠ `out["acts"]`, `out["actors"]` AND `out["act_subjects"]` READ `d.resolved`, THE FOLD SET, ON
    PURPOSE (REM-10 / HR-8): `harness/aperture.py`'s CONTROL line compares this `acts` with the
    measured arm's `len(d.resolved)`, and `harness/arms.py` reads `act_subjects` as its outcome
    metric. The ATTEMPT census (`corpus_run.attempts`, the act store) is a different, larger
    quantity; it does not replace this one."""
    w = build_realm(seed, cap) if w is None else w
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(seasons):
        d.season(ch, question=None,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    out = census(w)
    out["acts"] = len(d.resolved)
    out["actors"] = len({a.actor for a in d.resolved})
    subj_rel = Counter()
    for a in d.resolved:
        s = (a.payload or {}).get("subject") if isinstance(a.payload, dict) else None
        subj_rel["another person" if (s in w.persons and s != a.actor)
                 else "self" if s in w.persons else "not a person"] += 1
    out["act_subjects"] = dict(subj_rel)
    out["claim_sources"] = dict(Counter(c.source for p in w.persons.values() for c in p.ledger))
    return out


def creed_sweep(seasons: int = 2, seeds: tuple = (0, 1)) -> list:
    """`ED-IN-0229`'s instrument: does the faction creed change what people do, against a control?

    ⚠ **THE CONTROL ARM IS THE POINT AND IT IS BUILT BY REMOVING THE CAUSE, NOT BY EDITING THE
    RESULT.** `cast.faction_leader` is stubbed to `None` for the build, so every faction falls
    through `build_realm`'s own `template is None or lead_pid not in w.persons` branch to `HOLDS`,
    no creed is uttered and no stance row is written — the world this repository had before the
    ruling, produced by the same code path rather than by a second builder that could drift from
    it. Everything else (seed, cast, map, offices, holdings, wants) is identical between arms.

    ⚠ **AND IT SWEEPS `question_aggregation_rule`, WHICH IS WHY IT HAS TWO AXES INSTEAD OF ONE.**
    The creed's effect INVERTS across that fixture, and a single-arm run would have reported
    whichever sign the incumbent default happened to give. `H-54` owns the fixture; the reason the
    sign flips is the `q.id` tiebreak written out in `build_realm`'s membership block.

    Returns one row per (creed, rule, seed); `main --creed-sweep` prints them."""
    from ..data import cast as _cast
    rows = []
    for creed in (False, True):
        for rule in ("first", "all"):
            for seed in seeds:
                real = _cast.faction_leader
                if not creed:
                    _cast.faction_leader = lambda _f: None
                try:
                    w = build_realm(seed)
                finally:
                    _cast.faction_leader = real
                # ⚠ `.sweep()` RETURNS A NEW `Fixtures`; `_v[...] = rule` MUTATED THE SHARED ONE.
                # `World.__init__` stores `fixtures` BY REFERENCE and `build_realm` always passes
                # the module-level `DEFAULT_FIXTURES`, so writing through `_v` left the singleton
                # carrying the last arm's rule for the rest of the interpreter -- every later
                # `corpus_run`, `m1_acceptance` row and pytest test in that process silently
                # grading under `all` instead of the shipped `first`. A sweep that contaminates
                # the control is §0.1 pt 1's failure inside the instrument built to provide one.
                w.fixtures = w.fixtures.sweep("question_aggregation_rule", rule)
                out = run(seasons, seed, None, w=w)
                subj = out["act_subjects"]
                rows.append({
                    "creed": creed, "rule": rule, "seed": seed, "acts": out["acts"],
                    "other": subj.get("another person", 0), "self": subj.get("self", 0),
                    "not_a_person": subj.get("not a person", 0),
                    "told_by": out["claim_sources"].get("told_by", 0),
                    "stance_rows": sum(len(p.stance) for p in w.persons.values()),
                    "creeds": sum(1 for p in w.propositions.values()
                                  if p.id.startswith("fac_") and str(p.mood).upper() == "OUGHT"),
                })
    return rows


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--creed-sweep" in argv:
        argv.remove("--creed-sweep")
        n = int(argv[0]) if argv and argv[0].isdigit() else 2
        hdr = (f"{'creed':<6} {'rule':<6} {'seed':>4} {'acts':>6} {'other':>6} {'self':>6} "
               f"{'thing':>6} {'told':>5} {'stance':>7} {'creeds':>7}")
        print(f"THE CREED, AGAINST A CONTROL — {n} season(s) per arm (ED-IN-0229)")
        print(hdr); print("-" * len(hdr))
        for r in creed_sweep(n):
            print(f"{('yes' if r['creed'] else 'no'):<6} {r['rule']:<6} {r['seed']:>4} "
                  f"{r['acts']:>6} {r['other']:>6} {r['self']:>6} {r['not_a_person']:>6} "
                  f"{r['told_by']:>5} {r['stance_rows']:>7} {r['creeds']:>7}")
        return 0
    seasons = int(argv[0]) if argv and argv[0].isdigit() else 1
    cap = int(argv[1]) if len(argv) > 1 and argv[1].isdigit() else None
    w = build_realm(0, cap)
    c = census(w)
    print("THE POPULATED WORLD — one world, the canonical map, the corpus's own cast")
    print(f"  rungs by kind        {c['rungs']}")
    print(f"  persons              {c['persons']}   ({c['persons'] - c['cohorts']} one per season "
          f"loop; {c['cohorts']} cohort(s) of total weight {c['cohort_weight']}, `cohorts.yaml`)")
    print(f"  buildings inhabited  {c['distinct_buildings_inhabited']}"
          f"   (largest holds {c['largest_building']})")
    print(f"  sites                {c['sites']}")
    out = run(seasons, 0, cap, w=w)
    print(f"\n  after {seasons} season(s): {out['acts']} acts by {out['actors']} actors")
    print(f"  act subjects         {out['act_subjects']}")
    print(f"  claims by source     {out['claim_sources']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
