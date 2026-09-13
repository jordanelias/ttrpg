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
"""

from __future__ import annotations

import sys
from collections import Counter, defaultdict

import yaml

from ..data.fixtures import DEFAULT_FIXTURES, SITE_YIELD
from ..data.rosters import CONVICTIONS, RUNG_KINDS
from ..decision import make_chooser
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..state.carriers import Person, Proposition, Rung, Site, Tenure
from ..state.ids import H, draw_factory
from ..state.world import World
from . import probes as P
from .run_cases import load_cases

GEOGRAPHY = "systems/settlements/valoria_geography_v30.yaml"
VENUES = "engine/season/venues.yaml"
ROSTER = "engine/season/npcs.yaml"


def _repo_root():
    from pathlib import Path
    return Path(__file__).resolve().parents[3]


def _load(rel):
    with open(_repo_root() / rel, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


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
INSTITUTIONS = ["Löwenritter", "Einhir", "Altonian", "Schoenland", "Parliament",
                "Hafenmark", "Varfell", "Guild", "Church", "court", "Crown"]


def institution_of(case: dict) -> str | None:
    """The institution this loop answers to, or `None` for an unaffiliated life."""
    import json
    import re
    blob = " ".join([str(case.get("name", "")), str(case.get("one_line", "")),
                     json.dumps(case.get("season_requires", ""), ensure_ascii=False),
                     json.dumps(case.get("who_acts", ""), ensure_ascii=False),
                     json.dumps(case.get("knowledge", ""), ensure_ascii=False),
                     json.dumps(case.get("ends_when", ""), ensure_ascii=False)])
    for inst in INSTITUTIONS:
        if re.search(r"\b" + re.escape(inst) + r"\b", blob):
            return inst
    return None


def wants_of(case: dict) -> str:
    """WHAT THIS LOOP WANTS, in the case's own words.

    ⚠ THE CASES CARRY THIS AND THE FIRST CUT OF THIS MODULE IGNORED IT, giving all 143 people the
    string *"a standing ambition"* -- 143 identical wants, which is `build_at`'s three-identical-
    people defect re-created at scale. `season_requires` is a list of `{need, why, hardness}` and
    the corpus declares **427 `core` needs across the 143 cases** (median 7 needs each). The first
    `core` need is what the case says it cannot do without.

    Falls back through `important` and then to the one-line summary, because a case with no `core`
    row is a corpus gap and a person with no want does not act at all -- and an ambition invented
    here would be the fabrication this module refuses everywhere else.
    """
    rows = [r for r in (case.get("season_requires") or []) if isinstance(r, dict)]
    for hardness in ("core", "important", "flavour"):
        for r in rows:
            if r.get("hardness") == hardness and r.get("need"):
                return str(r["need"])
    return str(case.get("one_line") or case.get("name") or case.get("id"))


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
    import re
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
    import re
    acts = [str(x) for x in (case.get("who_acts") or [])]
    for entry in acts:
        for nm, cids in by_name.items():
            if re.search(r"\b" + re.escape(nm) + r"\b", entry):
                # A shared surname is a FAMILY (`Almqvist` is four cases). The tie lands on the
                # first by id and the ambiguity is real rather than resolved -- which of four
                # siblings *"his family"* means is not answerable from the corpus.
                for cid in sorted(cids):
                    if cid != case.get("id"):
                        return cid, None
    for entry in acts:
        for inst in INSTITUTIONS:
            if re.search(r"\b" + re.escape(inst) + r"\b", entry):
                return None, inst
    return None, None


def build_realm(seed: int = 0, cap: int | None = None, from_roster: bool = True) -> World:
    """The whole map, its buildings, and one person per season loop.

    `cap` limits the cast for a fast run; `None` seats every case. The cap is a PARAMETER and never
    a hidden default -- a run that quietly seated twenty people while reporting on a hundred and
    forty-three would be the confounded arm `CLAUDE.md` §0.1 pt 1 exists to refuse.

    `from_roster` reads `engine/season/npcs.yaml` for each person's home, want and tie. That file is
    the AUTHORITY once it exists; the matchers below are how it was first derived and are not
    consulted at runtime while it is present. `False` forces the derivation and is what
    `tools/export_npc_roster.py` calls to regenerate -- the one caller that must not read the file
    it is about to write.

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
    for tid, prov in geo["provinces"].items():
        rid = f"prov_{tid}"
        w.rungs[rid] = Rung(rid, "province")
        w.add_tenure(Tenure(f"t_{rid}_in", rid, realm, "contain", 0))
    for sid, s in geo["settlements"].items():
        rid = f"set_{_slug(sid)}"
        w.rungs[rid] = Rung(rid, "settlement")
        w.add_tenure(Tenure(f"t_{rid}_in", rid, f"prov_{s['territory']}", "contain", 0))

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
    convictions = sorted(CONVICTIONS)
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
        # Convictions seeded from the case id, exactly as `build_at` does it and for its stated
        # reason: identical convictions would force identical rankings for everybody.
        # [JUSTIFIED: `16` is `int()`'s RADIX for H()'s blake2b hexdigest -- same as corpus_run.py:242 and combat_seam.py:153. The `3` is #353 §14's own upper bound: "1-3 primary + distributed"]
        n_conv = 1 + int(H(seed, 0, cid, f"axis:{pid}:n"), 16) % 3
        # [JUSTIFIED: a DESCENDING ladder, not three chosen magnitudes -- #353 §14 distinguishes the "primary" conviction from the "distributed" remainder and supplies no numbers. Carried verbatim from corpus_run.py:245, its single owner; a second ladder here would be two answers to one question]
        chosen, weights = {}, (0.9, 0.5, 0.3)
        for k in range(n_conv):
            purpose = f"axis:{pid}" if k == 0 else f"axis:{pid}:{k}"
            # [JUSTIFIED: `16` is `int()`'s RADIX for H()'s hex digest -- same as corpus_run.py:248]
            pick = int(H(seed, 0, cid, purpose), 16) % len(convictions)
            chosen.setdefault(convictions[pick], weights[k])
        w.persons[pid].convictions = chosen

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
        inst = institution_of(case)
        if inst:
            at_institution[inst].append(f"p_{_slug(str(case.get('id')))}")

    ties = Counter()
    for n, case in enumerate(cases):
        cid = str(case.get("id"))
        pid = f"p_{_slug(cid)}"
        about = None
        row = (roster or {}).get(cid)
        if row and row.get("concerns"):
            cand = f"p_{_slug(str(row['concerns']))}"
            if cand in w.persons and cand != pid:
                about, why = cand, "roster"
        if about is not None:
            ties[why] += 1
            prop_id = f"prop_{_slug(cid)}"
            w.propositions[prop_id] = Proposition(
                prop_id, "OUGHT", about, str(row.get("want") or wants_of(case)), True, 0)
            w.add_tenure(Tenure(f"t_{prop_id}_commit", pid, prop_id, "commit", 0))
            continue
        named, inst = concerns_of(case, by_name)
        if named is not None:
            cand = f"p_{_slug(named)}"
            if cand in w.persons and cand != pid:
                about, why = cand, "named"
        if about is None and inst is not None:
            pool = [q for q in at_institution.get(inst, []) if q != pid and q in w.persons]
            if pool:
                about, why = pool[n % len(pool)], "institution"
        if about is None:
            mates = [q for q in by_home.get(home_of.get(pid, ""), []) if q != pid]
            if mates:
                about, why = mates[n % len(mates)], "roof"
        if about is None:
            nxt = homes[(homes.index(home_of[pid]) + 1) % len(homes)] if homes else None
            pool = [q for q in by_home.get(nxt, []) if q != pid]
            if not pool:
                continue
            about, why = pool[n % len(pool)], "neighbour"
        ties[why] += 1
        prop_id = f"prop_{_slug(cid)}"
        w.propositions[prop_id] = Proposition(prop_id, "OUGHT", about, wants_of(case), True, 0)
        w.add_tenure(Tenure(f"t_{prop_id}_commit", pid, prop_id, "commit", 0))
    w._tie_census = dict(ties)   # reported by `census`, never read by the loop
    return w


def census(w: World) -> dict:
    """What was built, counted from the world rather than from the inputs."""
    kinds = Counter(r.kind for r in w.rungs.values())
    where = {}
    for t in w.tenures:
        if t.kind == "contain" and t.live and t.subject in w.persons:
            where[t.subject] = t.object
    return {"rungs": dict(kinds), "persons": len(w.persons), "sites": len(w.sites),
            "ties": getattr(w, "_tie_census", {}), "propositions": len(w.propositions),
            "distinct_buildings_inhabited": len(set(where.values())),
            "largest_building": max(Counter(where.values()).values()) if where else 0}


def run(seasons: int = 1, seed: int = 0, cap: int | None = None) -> dict:
    """Build it and tick it. Returns the census plus what the season did."""
    w = build_realm(seed, cap)
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


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
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
    out = run(seasons, 0, cap)
    print(f"\n  after {seasons} season(s): {out['acts']} acts by {out['actors']} actors")
    print(f"  act subjects         {out['act_subjects']}")
    print(f"  claims by source     {out['claim_sources']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
