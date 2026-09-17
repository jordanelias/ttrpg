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
from ..queries.world_q import home_of as home_of_q
from ..gaps import Unspecified
from ..data.fixtures import DEFAULT_FIXTURES, SITE_YIELD
from ..data.rosters import (BODY_FACTION, FACTIONS, ROLE_TEMPLATE_OF, faction_prop_id,
                            load_yaml, title_domain)
from ..decision import make_chooser
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..state.carriers import Office, Person, Proposition, Rung, Site, Tenure
from ..state.ids import H, draw_factory
from ..state.world import World
from . import probes as P
from .run_cases import load_cases, seed_convictions, wants_of

GEOGRAPHY = "systems/settlements/valoria_geography_v30.yaml"
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


def build_realm(seed: int = 0, cap: int | None = None, from_roster: bool = True) -> World:
    """The whole map, its buildings, and one person per season loop.

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
    # ALONG. `references/world_initial_state.yaml` calls the same rows *"the 16 territory ids"*, so
    # the two canon files disagreed on the noun and the ruling settles it. §6 of that document lists
    # the propagation as *"tracked, not yet executed … nothing below needs further Jordan input, it
    # needs authoring"*, which is why the stale label survived to here.
    #
    # ⚠⚠ **AND A PROVINCE IS NOT A CONTAINER AT ALL.** §2: *"Provinces are only formed if the same
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

    for tid, terr in geo["provinces"].items():          # geography's stale key; the rows are territories
        rid = f"terr_{tid}"
        w.rungs[rid] = Rung(rid, "territory")
        holder = str(terr.get("faction") or "")
        # ⚠ A FOREIGN TERRITORY GETS NO PARENT, AND THAT IS THE POINT RATHER THAN A GAP. Schoenland
        # is on the faction roster and is FOREIGN — `rosters.yaml` records it as not
        # player-eligible, holding its territory and granting or refusing Altonian naval passage —
        # so a `contain` edge into `r_valoria` would assert it is part of the realm. It is a root
        # rung instead, which keeps it out of `descendants(realm)` and therefore out of the
        # realm's `sovereign_fraction`, where counting it would be a canon error wearing a number.
        # `references/world_initial_state.yaml` makes the same cut from the other side: it carries
        # 16 territories and deliberately omits T16, Schoenland's.
        if holder == "Schoenland":
            continue
        # The Church holds one territory and is not a duchy; an unheld territory has no duchy
        # either. Both hang off the realm, which the ladder permits.
        w.add_tenure(Tenure(f"t_{rid}_in", rid, duchy_of.get(holder, realm), "contain", 0))
    for sid, s in geo["settlements"].items():
        rid = f"set_{_slug(sid)}"
        w.rungs[rid] = Rung(rid, "settlement")
        w.add_tenure(Tenure(f"t_{rid}_in", rid, f"terr_{s['territory']}", "contain", 0))

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
        w.persons[pid] = Person(pid, str(case.get("name") or cid))
        w.rungs[pid] = Rung(pid, "person")
        w.add_tenure(Tenure(f"t_{pid}_in", pid, home, "contain", 0))
        # ⚠⚠ AUTHORED, NOT DRAWN — AND THE DRAW REMAINS AS THE NAMED FALLBACK IT ALWAYS WAS.
        # `references/npc_registry.yaml` carries a weighted conviction vector for all 46 of these
        # people, cited to canon, using only the canonical thirteen. Nothing that executes had ever
        # opened it, so `seed_convictions` — a `blake2b(seed, case_id, pid)` draw — was supplying
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
        # ⚠ `seed_convictions` IS STILL THE SINGLE OWNER OF THE DRAW (§8) and is still called
        # rather than copied. What changed is which source is consulted first.
        authored = cast.convictions_of(cast.row(cid) or {})
        w.persons[pid].convictions = authored or seed_convictions(seed, cid, pid)

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
    # it generates. Subject the creed on a faction NAME and all eight factions' members deliberate
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
        if fac_name is None:
            # ⭐ **UNPLACED IS A CORRECT OUTCOME, NOT A PENDING ONE — RULED by Jordan,
            # 2026-09-14: *"Not everyone has to belong to a faction."*** This was carried as an
            # open question for two days; it is closed, and it is closed in the direction that
            # makes the branch below RIGHT rather than tolerated. Six of the 46 name an
            # affiliation on no roster — `Altonia` (3), `Independent (Southernmost Wardens)` (2),
            # the dissolved Virke syndicate (1) — and they stay unaffiliated.
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
        # STANCE ROW weighted by `cast.loyalty`, and `decision/choose.py::stance_toward` is what
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
        # stubbed to `None`, so all eight factions fall back to `HOLDS` and no stance row is
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
            unheld_for_want_of_a_head.append((f"terr_{tid}", held_by))
            continue
        w.add_tenure(Tenure(f"t_hold_terr_{tid}", lead_pid, f"terr_{tid}", "hold", 0))
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
    # `Ministries` is one row where canon names six ministries, the four Cardinals are there and
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
    from .corpus_run import rescales          # deferred — `data/__init__` records what eager costs
    overlays = rescales()
    seated, no_post, occupations, proposed = 0, [], [], []
    for case in cases:
        cid = str(case.get("id"))
        pid = f"p_{_slug(cid)}"
        r = cast.row(cid)
        if r is None:
            continue
        fac_name, _sub, _raw = cast.faction_of(r)
        if fac_name is None:
            continue                          # unplaced above; an office needs a faction (§11)
        over = (overlays.get(cid) or {}).get("office") or {}
        title = cast.title_of(r)
        governs = title_domain(title) if title else None
        # ⚠⚠ **AN OFFICE IS A SEAT, NOT AN OCCUPATION, AND THE FIRST CUT OF THIS BLOCK CONFLATED
        # THEM.** It gave every placed person an Office named after their registry `role`, which
        # made `leaders(w, faction) == members(w, faction)` for all eight factions — everybody a
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
        rung = realm if governs == "realm" else duchy_of.get(fac_name) if governs == "duchy" else None
        # ⚠ THE SUB-ORGANIZATION BECOMES THE `body` WHERE IT NAMES ONE, AND THE GAIN IS THE
        # CONSTRUCTOR'S CROSS-CHECK, NOT THE FIELD. With a body, `office_faction` DERIVES the
        # faction and refuses a body/faction mismatch; with `body=None` the faction is taken on the
        # caller's word. So a Crown person whose row said `Hafenmark (Inner Council)` now raises
        # instead of seating quietly. EXACT MATCH, not substring: `Inner Circle / Löwenritter
        # Liaison` (NPC-035) and `dual-loyalty: Crown Inner Circle agent…` (NPC-034) resolve to
        # nothing and keep `body=None`, which is honest — each names two allegiances and canon has
        # no organ for either shape.
        body = over.get("body") if over else (_sub if _sub in BODY_FACTION else None)
        oid = f"off_{_slug(cid)}"
        w.offices[oid] = Office(
            oid, post, rung, list(over.get("remit") or []),
            body=body,
            faction=(over.get("faction") if over else None) or (None if body else fac_name),
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
    w._office_census = {"seated": seated, "no_post": no_post,
                        "occupations": occupations, "proposed_seats": proposed}

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
    return w


def census(w: World) -> dict:
    """What was built, counted from the world rather than from the inputs."""
    kinds = Counter(r.kind for r in w.rungs.values())
    # §8: `world_q.home_of` owns "where is everyone"; this used to roll its own copy, and so did
    # three other sites (see that query's docstring).
    where = home_of_q(w)
    return {"rungs": dict(kinds), "persons": len(w.persons), "sites": len(w.sites),
            "ties": getattr(w, "_tie_census", {}), "propositions": len(w.propositions),
            "distinct_buildings_inhabited": len(set(where.values())),
            "largest_building": max(Counter(where.values()).values()) if where else 0}


def run(seasons: int = 1, seed: int = 0, cap: int | None = None, w: World | None = None) -> dict:
    """Build it and tick it. Returns the census plus what the season did.

    `w` takes a world ALREADY BUILT, for a caller that wants to report on the build before the
    season runs -- `main` below is the one, and without this it built the whole realm twice
    (~10s each) to print a census it then discarded."""
    w = build_realm(seed, cap) if w is None else w
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(seasons):
        d.season(ch, question=None, subsistence=P.SUBSIST,
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
    print(f"  persons              {c['persons']}   (one per season loop)")
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
