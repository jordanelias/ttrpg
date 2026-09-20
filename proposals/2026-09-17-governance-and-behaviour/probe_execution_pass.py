#!/usr/bin/env python3
"""The instrument behind `01_THE_BUILD_ORDER.md` §7. Re-runnable, gates nothing, dies with this suite.

    python proposals/2026-09-17-governance-and-behaviour/probe_execution_pass.py

Precedent and shape: `../2026-09-17-governance-and-holdings-r2/probe_reach_questions.py`, which is
the instrument behind that suite's `561 -> 1632`. This one reproduces every number `§7` states, so
`ED-IN-0246`'s `MEASURED-BY:` names a script rather than a claim.

⚠ TWO OF §7's NUMBERS ARE NOT REPRODUCIBLE FROM THIS BRANCH AND THE SCRIPT SAYS SO RATHER THAN
QUIETLY OMITTING THEM. Item 1 (`@effect_for("commit")`) and item 4 (`delete budget_office_bonus`)
were written, measured and then WITHDRAWN -- so `commitment.made 0 / refused 42` and the telling
collapse `26 -> 12` are readings of trees that are not this one. Each is printed as UNREPRODUCIBLE
with the exact edit that restores it, which is what lets a later session re-take them rather than
take this file's word. `CLAUDE.md` §0.1 pt 3: a citation you have not opened is not a citation, and
a number nobody can re-run is the same thing wearing a measurement's clothes.

⚠ THE BEFORE/AFTER PAIRS ARE TAKEN BY CONSTRUCTING BOTH ARMS, not by remembering one. The "before"
arm rebuilds the pre-item-16 shape (faction-subject province holds) in a throwaway world with the
guard bypassed, so the comparison is two states of one builder rather than a number against a memory.
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from engine.season.data import cast                                    # noqa: E402
from engine.season.data.rosters import FACTIONS                        # noqa: E402
from engine.season.decision import budget                              # noqa: E402
from engine.season.harness.populated import build_realm                # noqa: E402
from engine.season.loop.driver import resolvable_verbs                 # noqa: E402
from engine.season.loop.predicates import in_holdings                  # noqa: E402
from engine.season.queries import world_q                              # noqa: E402
from engine.season.queries.world_q import provinces_of, sovereign_fraction  # noqa: E402
from engine.season.state.carriers import Tenure, View                  # noqa: E402


def _sweep_in_holdings(w) -> tuple[int, list]:
    """Returns (pairs examined, pairs true). IT ASSERTS THAT IT ASSERTED (`CLAUDE.md` §0.1 pt 2):
    a sweep that finds nothing is indistinguishable from a sweep whose body never ran, so the
    examined count is returned beside the hits and printed."""
    checked, hits = 0, []
    for pid in w.persons:
        for rid in w.rungs:
            checked += 1
            if in_holdings(w, pid, rid):
                hits.append((pid, rid))
    return checked, hits


def _before_arm(w):
    """The pre-item-16 shape, rebuilt: every province `hold` put back onto its FACTION Proposition.

    `World._refuse_bad_hold` now raises on that construction, which is the point of the item -- so
    the arm is built by appending to the store directly, exactly as the old `add_tenure` did before
    the conjunct existed. This is a THROWAWAY world; nothing else reads it."""
    for t in list(w.tenures):
        if t.kind == "hold" and t.object in w.rungs and w.rungs[t.object].kind == "territory":
            holder = w.persons.get(t.subject)
            if holder is not None:
                holder.tenures.remove(t)
            facs = [x.object for x in (holder.tenures if holder else [])
                    if x.kind == "commit" and x.live and x.object.startswith("fac_")]
            if facs:
                w._unowned.append(Tenure(t.id, facs[0], t.object, "hold", t.since))
    return w


def main() -> int:
    print("=" * 78)
    print("§7 · THE EXECUTION PASS — every number, re-taken")
    print("=" * 78)

    w = build_realm(0)
    fx, k = w.fixtures, w.fixtures.get("scene_budget")

    print("\n--- §7.3 · ITEM 16, LANDED ---")
    holds = [t for t in w.tenures if t.kind == "hold"]
    by_class = Counter((w.class_of(t.subject), w.class_of(t.object)) for t in holds)
    print(f"  hold Tenures by (subject class, object class) : {dict(by_class)}")
    print(f"  faction-subject holds                         : "
          f"{sum(1 for t in holds if w.class_of(t.subject) != 'Person')}   (§7.3 says 0)")
    checked, hits = _sweep_in_holdings(w)
    print(f"  in_holdings sweep                             : {checked} pairs examined, "
          f"{len(hits)} TRUE over {len({p for p, _ in hits})} holders   (§7.3 says 15 over 4)")
    print(f"  unheld for want of an authored head           : {w._unheld_for_want_of_a_head}")

    print("\n--- §7.3a · THE RATIFIED-RULING COLLISION AND ITS REPAIR ---")
    pv = provinces_of(w, "r_valoria")
    print(f"  provinces_of(r_valoria), repaired             : "
          f"{ {f: len(ts) for f, ts in pv.items()} }   (§7.3a says 4 factions)")
    print(f"  every key is a faction Proposition            : {all(f in w.propositions for f in pv)}")
    print(f"  sovereign_fraction(r_valoria)                 : {sovereign_fraction(w, 'r_valoria')}"
          f"   (the CONTROL — unchanged, and its own docstring says (0.4, 304))")
    before = _before_arm(build_realm(0))
    print(f"  provinces_of on the BEFORE arm                : {provinces_of(before, 'r_valoria')}")
    print("    ^ the repair's subject: read off the edge, this is `{}` after the re-home. "
          "`faction_holding` derives it through the holder's membership `commit` instead.")

    print("\n--- §7.3b · H-92 IS LIVE ON THIS BRANCH (item 4 reverted) ---")
    moved = sorted(((pid, budget(p, View(pid, [], fx.get("view_k")), k, fx))
                    for pid, p in w.persons.items()), key=lambda r: -r[1])
    print(f"  base scene_budget                             : {k}")
    print(f"  persons budgeting above the base              : "
          f"{sum(1 for _, b in moved if b != k)}   (§7.3b says 20)")
    print(f"  the highest                                   : {moved[0]}   (§7.3b says 12)")
    print(f"  releasable scenes = scene_budget x scenes_per_round : "
          f"{k * fx.get('scenes_per_round')}   — so the excess is unspendable")

    print("\n--- §7.3c · ITEM 3a, THE LARDER LADDER ---")
    # ⚠ THE DRAW BITES IN SEASON 2, NOT SEASON 1. `#353 §25` puts larders before yield, so season
    # one draws against a world that has produced nothing yet and EVERY eater is short. A
    # one-season probe reads this item as dead, which is why this runs two and prints both.
    from engine.season.data.matrix import Step                           # noqa: E402
    from engine.season.loop.driver import SeasonDriver                   # noqa: E402
    from engine.season.decision import make_chooser                      # noqa: E402
    from engine.season.state.ids import H, draw_factory                  # noqa: E402
    from engine.season.harness import probes as HP                       # noqa: E402
    ww = build_realm(0)
    dd = SeasonDriver(ww)
    mint = lambda pid, verb, subj: H(ww.world_seed, ww.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(ww.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(ww.world_seed, lambda: ww.tick))
    dd.season(ch, question=None, subsistence=HP.SUBSIST,
              contest_max_depth=ww.fixtures.get("contest_max_depth"))
    short = ww._subsistence_shortfall
    print(f"  after season 1: eaters short {len(short):>2} · units unmet "
          f"{sum(sum(v.values()) for v in short.values()):>3}   (§7.3c: 46 and 138 — nothing has "
          f"been produced yet)")

    # `MW-1`'s four falsifiers, re-taken AT THE TICK THE SUITE TOOK THEM — one season of stock on
    # the ground. The DRAW is isolated from the yield by clearing the sites, because MATTER draws
    # and then produces in one barrier and a bare run measures the NET.
    #
    # ⚠ THE ABSOLUTE FIGURES ARE SEASON-DEPENDENT AND THE INVARIANT IS NOT. Taken one season later
    # this probe read control B as 6,144 rather than 3,120 — two seasons of yield on the same
    # untouched settlements — which is a fact about WHEN it was measured, not about the item. The
    # load-bearing half of control B is `0 changed`, and that holds at every tick.
    before = {rid: dict(r.stores or {}) for rid, r in ww.rungs.items()}
    ww.sites.clear()
    ww.step = Step.MATTER
    evs = dd.matter([])
    drew_at = [e.subject for e in evs if e.kind == "stores.changed"]
    after_short = ww._subsistence_shortfall
    print(f"  season 2's draw, isolated: eaters short {len(after_short)} · units unmet "
          f"{sum(sum(v.values()) for v in after_short.values())}   (§7.3c: 0 and 0)")
    print(f"  MW-1 · rungs the larder pass WRITES  : {len(drew_at)}   (predicted 13; was 0)")
    hearth = sum(sum((r.stores or {}).values()) for r in ww.rungs.values() if r.kind == "hearth")
    print(f"  MW-1 · hearth stores, which must stay 0 (nothing is DELIVERED) : {hearth}")
    homes = world_q.home_of(ww)
    anc: set = set()
    for h in set(homes.values()):
        cur = h
        while cur:
            anc.add(cur)
            cur = world_q.parent_of(ww, cur)
    untouched = [r for r, rr in ww.rungs.items() if rr.kind == "settlement" and r not in anc]
    kept = sum(sum(before[r].values()) for r in untouched)
    moved = [r for r in untouched if before[r] != (ww.rungs[r].stores or {})]
    print(f"  MW-1 · control B — settlements with nobody beneath: {len(untouched)} holding {kept} "
          f"units, {len(moved)} changed   (predicted 3,120 and 0 changed)")

    print("\n--- §7.3d · ITEM 3b, THE BODY WRITE (shipped at its control arm) ---")
    from engine.season.data.fixtures import DEFAULT_FIXTURES                 # noqa: E402
    print(f"  shipped `body_step`                          : "
          f"{DEFAULT_FIXTURES.get('body_step')}   (§7.3d: 0, the control arm — `H-125`)")
    # WHY it is parked there: the corpus cannot answer for the number.
    from engine.season.harness.run_cases import load_cases                   # noqa: E402
    from engine.season.harness.corpus_run import build_at                    # noqa: E402
    built = stocked = people = 0
    cases: list = []
    for kind in ("NPC", "ARC"):
        try:
            cases += list(load_cases(kind))
        except Exception:
            pass
    for c in cases:
        try:
            cw = build_at(c)
        except Exception:
            continue
        built += 1
        if sum(sum((r.stores or {}).values()) for r in cw.rungs.values()):
            stocked += 1
        people += len(world_q.home_of(cw))
    print(f"  corpus worlds built {built} · holding ANY stores {stocked} · persons in them "
          f"{people}   (§7.3d: 86 · 0 · 258)")
    # AND the mechanism at a live arm: an empty-root world, bodies falling and the budget moving.
    tw = HP.tiny_world()
    for rid in ("R", "D", "S", "Hh"):
        tw.rungs[rid].stores = {}
    tw.sites.clear()
    tw.fixtures = tw.fixtures.sweep("body_step", 10)
    td = SeasonDriver(tw)
    who, start = "p_low", tw.persons["p_low"].body
    bud = lambda: budget(tw.persons[who], View(who, [], tw.fixtures.get("view_k")),
                         tw.fixtures.get("scene_budget"), tw.fixtures)
    b0, crossed = bud(), None
    for season in range(1, 40):
        tw.step = Step.MATTER
        evs = td.matter([])
        tw.tick += 1
        if [e for e in evs if e.kind == "condition.band_crossed" and e.subject == who]:
            crossed = season
            break
    print(f"  at body_step=10: {who} body {start} -> {tw.persons[who].body}, crossed a band at "
          f"season {crossed}, budget {b0} -> {bud()}   (§7.3d: 1000 -> 790, season 7, 5 -> 4)")

    print("\n--- §7.3e · ITEM 6d, THE BENEFICIARY COLUMN (ED-IN-0248) ---")
    from engine.season.data.verbs import VERB_TABLE as _VT
    from engine.season.decision import choose as _choose
    from engine.season.harness import populated as _populated

    # The carriage census CAT-2 killed option 1 on, re-taken in-process. A static column is only
    # safe while it declares carriers a row can hold, so this is the number the loader's third
    # invariant exists to keep honest.
    _typed = [r for r in _VT.values() if r.requires_typed is not None]
    _admits_to = [v for v, r in _VT.items() if r.requires_typed is not None
                  and "to" in (set(r.requires_typed.operands()) | set(r.requires_typed.needs()))]
    print(f"  carriage census: {len(_VT)} verbs · {len(_VT) - len(_typed)} UNTYPED · "
          f"{len(_typed)} typed · `to` carriable by {len(_admits_to)}"
          f"   (CAT-2: 38 / 24 / 14 / 12)")
    print(f"  declared        : {Counter(r.beneficiary for r in _VT.values())}"
          f"   (§7.3e: actor 18 · none 15 · subject 4 · to 1)")

    # THE MEASUREMENT THAT IS NOT SATISFIABLE BY DECLARING ANYTHING: resolve every beneficiary on
    # the candidates a real season forms. `opening_set` is read as a BARE NAME inside `choose`, so
    # rebinding it HERE reaches that reader -- the same namespace rule `decision/choose.py`'s own
    # docstring states for the degree sweep.
    seen: list = []
    _inner = _choose.opening_set

    def _spy(person, view, question, fx):
        cands = _inner(person, view, question, fx)
        seen.extend((person, c) for c in cands)
        return cands

    _choose.opening_set = _spy
    try:
        _populated.run(seasons=1, seed=0)
    finally:
        _choose.opening_set = _inner

    by_kind = Counter(_VT[c.verb].beneficiary for _, c in seen)
    holes = [(p.id, c.verb) for p, c in seen
             if _VT[c.verb].beneficiary != "none" and _choose.beneficiary_of(p, c) is None]
    resolved = sum(1 for p, c in seen if _choose.beneficiary_of(p, c) is not None)
    mine = sum(1 for p, c in seen if _choose.benefits_me(p, c) == 1.0)
    self_subject = sum(1 for p, c in seen if c.subject == p.id)
    print(f"  candidates formed        : {len(seen)}   (§7.3e: 5345)")
    print(f"    by declared kind       : {dict(by_kind)}")
    print(f"    RESOLVED               : {resolved}"
          f" ({resolved / len(seen):.1%})   (§7.3e: 3796, 71.0%)")
    print(f"    declared-but-UNRESOLVED: {len(holes)}   "
          f"(§7.3e: 0 -- STRUCTURAL, not a result; test_governance_build.py:707-717)")
    print(f"    benefits_me == 1.0     : {mine}   (§7.3e: 3420)")
    print(f"  ⚠ CONTROL on that last figure: {self_subject} candidates"
          f" ({self_subject / len(seen):.1%}) carry THE ACTOR AS THEIR OWN SUBJECT"
          f"   (§7.3e: 2650, 49.6%) -- the aperture's shape, not a fact about Valorians")

    print("\n--- §7.1(b) · THE HOLONIC SURFACE ---")
    import ast
    root = Path(__file__).resolve().parents[2]
    for rel in ("engine/season/loop/driver.py", "engine/season/loop/deliberate.py"):
        tree = ast.parse((root / rel).read_text())
        names = [a.name for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)
                 and ((n.module or "").endswith("decision") or (n.module or "").startswith("decision"))
                 for a in n.names]
        names += ["decision (module)" for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)
                  and n.module is None and n.level and any(a.name == "decision" for a in n.names)]
        print(f"  {rel:36} : {len(names)} names from decision/   (§7.1(b) says 18 and 3)")

    print("\n--- NOT REPRODUCIBLE FROM THIS BRANCH, and how to re-take each ---")
    print(f"  resolvable_verbs()                            : {len(resolvable_verbs())}"
          f"   (§7.2: 19 WITH item 1, which is held; 18 without)")
    print("  §7.2  commitment.made 0 / refused 42          : UNREPRODUCIBLE — add "
          "`@effect_for(\"commit\")` to engine/season/loop/effects.py, then run one populated "
          "season at seed 0 and count `commitment.*` event kinds.")
    print("  §7.3b telling collapse 26 -> 12 of 27         : UNREPRODUCIBLE — delete the "
          "`offices * budget_office_bonus` term from engine/season/decision/budget.py, then run "
          "`pytest engine/season/tests -k test_r7_m6_ -q`.")
    print("\nNothing here gates anything. This file dies with "
          "proposals/2026-09-17-governance-and-behaviour/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
