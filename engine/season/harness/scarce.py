"""THE SCARCE WORLD: two settlements, one larder short, and a steward who can see it and feed it. Plan
position `19d` (DEMAND · DELIVERY), the retirement plan's G3: *"Includes the deliberately-scarce test
world needed to actually exercise it"*.

⚠⚠ A TEST FIXTURE, NOT CANON. Every id and number below is chosen to make one chain observable. None
of it is a claim about Valoria's economy.

WHY THE SHIPPED WORLDS CANNOT SHOW THE CHAIN, MEASURED rather than taken from the plan's sentence. G3
says *"today's default world runs a 35x surplus, so `transfer` is refused every time"*. Re-measured on
`populated.build_realm(0)` at `19d`, three seasons:
  * THE SURPLUS FIGURE STILL HOLDS: 4,810 units produced a season against 138 demanded by the 46
    eaters at build (135 by the 45 still housed after season 1), at `subsistence_weight` grain 2 /
    salt 1. That is about 35x. Counting only the two eaten kinds (2,590 grain and salt) it is about
    19x.
  * THE CAUSATION DOES NOT HOLD. 27 of 27 computed `transfer`s were refused, and EVERY ONE named a
    `from` that is a HEARTH HOLDING NOTHING. `from` is the actor's own containing rung
    (`decision/options.py::containing_rung_of`, r2 §A.13), all 46 persons live in hearths, and
    yield lands only at settlements. So no computed transfer can ever pass `stores(from, kind) >=
    amount` there, however scarce or rich the realm is. Scarcity is not why transfer refuses, and
    a scarce copy of that realm would refuse the same way. Registered as `H-160`.
  * AND NOTHING IN IT EVER RUNS SHORT MID-DRAW. Season 1's eaters find no stock at all (the draw
    precedes the first yield: `source None`), and every later season is in surplus. So MATTER's
    shortfall observation (`loop/matter.py`, `19d`) has nothing to report on the shipped worlds.
    That is also why it moves none of their artifacts.

SO THIS WORLD NEEDS TWO THINGS THE REALM LACKS, AND BOTH ARE STATED RATHER THAN SMUGGLED:
  1. A LARDER THAT RUNS DRY WITH MOUTHS UNFED. `set_hungry` starts with a little grain and salt and
     no producing site. Its people are ONE COHORT, a `Person` at `weight > 1`: the population
     synecdoche `24f` mints for the realm from `cohorts.yaml` (`ED-IN-0255`: *"NPC synecdoches that
     just represent the overall population affected ... it's a territorial issue"*). It uses
     `harness/probes.py`'s crowd precedent, not a new carrier. ⚠ SINCE `24f` IT IS THE ONLY EATER
     HERE: the steward, at weight 1, is exempt from the larder draw (`world_q.subsistence_draw`), so
     `set_granary` is drawn by nobody and its stock is what the steward can GIVE, not what he eats.
  2. A GIVER WHO STANDS IN A STOCKED LARDER AND CAN SEE THE HUNGRY ONE. `p_steward` lives AT
     `set_granary`, the rung itself, as `probes.tiny_world` seats its duke in the settlement. So
     `from` is a store with stock. The steward HOLDS `set_hungry` (a `hold` on a Rung, lawful by
     `rosters.yaml: hold_object_kinds`), so the drained larder's `stores.changed` reaches him
     through `document_key`, the bureaucratic channel (`told_by`). ⚠ SINCE v9 IN-22 PURVIEW ALSO
     REACHES IT, as a report and not a witnessing: MATTER's recorded shortfall (the read, never the
     write) is deposited into every holder of a seat whose purview contains the drained rung
     (`loop/witness.py`, the seat channel's `inferred`). The steward holds no seat, so in THIS world
     his `hold` is still the only route; `governed` below adds the governors (`H-160` limit 2).

WHAT IT PROVES THAT THE DEFAULT WORLD COULD NOT: the whole G3 chain executes on COMPUTED acts. A
larder runs dry, `demanded > delivered` is recorded on its own write, a person who was not there
holds it as a claim, a `claim_landed` question forms a `transfer` whose `kind` and `amount` come
from that claim, the fold EXECUTES it (`transfer.made`, matter conserved), and the next season's
`delivered` at the hungry settlement rises against a control world whose steward holds nothing.
`tests/test_demand_delivery.py` asserts each link and each control.

⚠ NOT A SEPARATE FLAG ON ANOTHER BUILDER, on `governance_spine.py`'s stated reason: a flag would
make one world answer two questions, and a later reader could not tell which census a measurement
came from.
"""

from __future__ import annotations

from collections import Counter

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.requires import SHORTFALL_PREDICATE
from ..decision import make_chooser
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..state.carriers import Office, Person, Rung, Site, Tenure
from ..state.ids import H, draw_factory
from ..state.world import World
from . import probes as P

# THE TWO SETTLEMENTS AND THE TWO PEOPLE. Test-fixture ids, not definitions the game resolves from.
GRANARY, HUNGRY = "set_granary", "set_hungry"
STEWARD, POPULACE = "p_steward", "p_populace"
# How many people the cohort stands for. It is a fixture, and `ED-WR-0011` grants that latitude for
# a synecdoche's weight (*"the initial count N ... is a fixture, not an axiom"*). At the shipped
# `subsistence_weight` (grain 2, salt 1) ten mouths want 20 grain and 10 salt a season. That is
# four times the hungry larder's opening stock and well under the granary's.
COHORT_WEIGHT = 10
# The two opening larders. `set_hungry` holds a quarter of the cohort's season want, so its first
# draw runs it dry with the cohort unfed. `set_granary` holds several seasons of what one person
# eats, plus its harbour's yield, so it can give (since `24f` nobody draws on it: its steward is
# exempt).
# [JUSTIFIED: a test-fixture stock, not a game value -- sized only so the first draw drains one larder and not the other]
GRANARY_STOCK = {"grain": 60, "salt": 30}
# [JUSTIFIED: a test-fixture stock, not a game value -- a quarter of the cohort's season want at the shipped subsistence_weight]
HUNGRY_STOCK = {"grain": 5, "salt": 2}


def build(seed: int = 0, fixtures=DEFAULT_FIXTURES, steward_holds: bool = True) -> World:
    """The scarce world. `steward_holds=False` is the CONTROL: the same world with the one edge that
    lets the steward witness the hungry larder removed. It holds the same stores, the same people
    and the same sites, so any difference in what reaches `set_hungry` is that edge's."""
    w = World(seed, fixtures)
    scale = w.fixtures.get("condition_scale")
    # realm > territory > two settlements. The granary produces (a harbour at full condition, the
    # shipped `site_yield`); the hungry settlement produces nothing and opens with a quarter of a
    # season's want, so its first draw runs it dry with the cohort unfed.
    for rid, kind, stores in (("r_realm", "realm", None), ("terr_march", "territory", None),
                              (GRANARY, "settlement", dict(GRANARY_STOCK)),
                              (HUNGRY, "settlement", dict(HUNGRY_STOCK))):
        w.rungs[rid] = Rung(rid, kind, stores=stores)
    for i, (sub, obj) in enumerate((("terr_march", "r_realm"), (GRANARY, "terr_march"),
                                    (HUNGRY, "terr_march"))):
        w.add_tenure(Tenure(f"t_in_{i}", sub, obj, "contain", 0))
    w.sites["s_granary_harbour"] = Site("s_granary_harbour", GRANARY, "harbour", condition=scale)
    for pid, name, weight, home in ((STEWARD, "the steward", 1, GRANARY),
                                    (POPULACE, "the people of the hungry town", COHORT_WEIGHT,
                                     HUNGRY)):
        w.persons[pid] = Person(pid, name, weight=weight)
        w.rungs[pid] = Rung(pid, "person")
        w.add_tenure(Tenure(f"t_{pid}_in", pid, home, "contain", 0))
        # Plan position `19c`: and they live there (`populated.build_realm`'s rule).
        w.add_tenure(Tenure(f"t_{pid}_home", pid, home, world_q.RESIDE_KIND, 0))
    if steward_holds:
        w.add_tenure(Tenure("t_steward_holds_hungry", STEWARD, HUNGRY, "hold", 0))
    return w


# v9 IN-22: THE TWO GOVERNORS AND WHAT THEY SIT OVER. Test-fixture ids, not definitions.
REEVE, FAR_REEVE = "p_reeve", "p_far_reeve"
REEVE_SEAT, FAR_SEAT = "off_march_reeve", "off_far_reeve"
FAR_TERRITORY = "terr_far"
# Every office names its faction (`H-99`); `probes.tiny_world`'s generic Duke is the Crown's, and a
# generic reeve is too. Test data, not a claim about who governs a march.
GOVERNING_FACTION = "Crown"


def governed(seed: int = 0, fixtures=DEFAULT_FIXTURES, steward_holds: bool = True) -> World:
    """v9 IN-22 (#457 `CARRY-SHORTFALL`, `H-160` limit 2): `build`'s world plus TWO GOVERNORS, each
    seated on a territory and living there -- so neither stands at `set_hungry` nor holds it, and
    the only thing that differs between them is whether his seat's purview contains it.
      * `p_reeve` holds `off_march_reeve`, whose rung is `terr_march`: `set_hungry` lies inside it.
      * `p_far_reeve` holds `off_far_reeve`, whose rung is `terr_far`, a SIBLING territory under the
        same realm: `set_hungry` does not. He is the CONTROL -- same channel, same mode, same kind of
        seat, a different ground.
    Both weigh 1, so neither eats from a larder (`world_q.subsistence_draw`) and neither changes the
    draw `build` sets up. A SEPARATE BUILDER, NOT A FLAG ON `build`, on this module's own reason: the
    shipped `build` answers `19d`'s question and its measurements stay its own."""
    w = build(seed, fixtures, steward_holds)
    w.rungs[FAR_TERRITORY] = Rung(FAR_TERRITORY, "territory")
    w.add_tenure(Tenure("t_in_far", FAR_TERRITORY, "r_realm", "contain", 0))
    for seat, post, rung in ((REEVE_SEAT, "Reeve of the March", "terr_march"),
                             (FAR_SEAT, "Reeve of the Far Territory", FAR_TERRITORY)):
        w.offices[seat] = Office(seat, post, rung, [], faction=GOVERNING_FACTION)
    for pid, name, home, seat in ((REEVE, "the reeve of the march", "terr_march", REEVE_SEAT),
                                  (FAR_REEVE, "the far reeve", FAR_TERRITORY, FAR_SEAT)):
        w.persons[pid] = Person(pid, name)
        w.rungs[pid] = Rung(pid, "person")
        w.add_tenure(Tenure(f"t_{pid}_in", pid, home, "contain", 0))
        w.add_tenure(Tenure(f"t_{pid}_home", pid, home, world_q.RESIDE_KIND, 0))
        w.add_tenure(Tenure(f"t_{pid}_seat", pid, seat, "hold", 0))
    return w


def shortfall_question(w: World, pid: str):
    """The `claim_landed` question that `pid`'s newest shortfall claim raises, or `None`. It is the
    FIRST such question in `questions_for`'s own order, so which of two kinds is asked first is that
    function's rule and not this one's."""
    p = w.persons[pid]
    ids = {c.id for c in p.ledger
           if str(c.predicate).partition(":")[0] == SHORTFALL_PREDICATE}
    return next((q for q in world_q.questions_for(w, p) if q.about in ids), None)


# [JUSTIFIED: a run length, not a game value -- three seasons show the dearth, the delivery, and the draw after it]
def run(seasons: int = 3, seed: int = 0, w: World | None = None,
        name_the_question: bool = True) -> dict:
    """Tick the world with the REAL chooser and report the chain, season by season.

    ⚠ `name_the_question` IS THE ONE THING THIS INSTRUMENT DECIDES, AND IT IS `H-54`'s. Before each
    season it names the steward's shortfall question as the season's `question` (the driver's
    probe override: *"An explicit `question` still overrides, so a probe can name the q it is
    testing"*). Everything after that is the shipped loop: the chooser's score and packing, the
    fold, WITNESS. The override exists because WHICH of a person's questions they answer is
    `H-54`'s open rule, not this position's. At the shipped `question_aggregation_rule: first`, a
    person answers `qs[0]`, which is the lowest HASH among their landed questions. MEASURED at
    `19d` in this world, four seasons, override off, at each of `first`/`all`/`one_per_source`:
    the steward holds both shortfall claims and deliberates 15/19/15 times, and none of those
    deliberations is about a shortfall claim, because claims about his own granary sort first.
    Under `all` and `one_per_source`
    the folded question still carries `qs[0].about` alone (`decision/questions.py`), so a
    claim-sourced operand is unreachable unless its question is `qs[0]`, and that is `15c`'s writ
    operands' limit too. `False` runs the shipped rule unassisted; that is what `main` prints
    second.

    Each season's `demanded`/`delivered` at `set_hungry` is read BEFORE the season. Nothing between
    that read and MATTER's draw touches a store (CALENDAR writes dates), so it is the draw MATTER
    then performs. `transfers` lists every `transfer` the fold resolved, with its operands and
    outcome, and `claim_sourced` marks one whose `kind` and `amount` equal a shortfall claim its
    actor held about its `to`. Nothing here chooses an act."""
    w = build(seed) if w is None else w
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    out = []
    for _ in range(seasons):
        need, got = world_q.demanded(w, HUNGRY), world_q.delivered(w, HUNGRY)
        n_log, n_acts = len(w.log), len(d.resolved)
        asked = shortfall_question(w, STEWARD) if name_the_question else None
        d.season(ch, question=asked, subsistence=P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
        new = w.log[n_log:]
        outcome = {e.causes[0]: e.kind for e in new
                   if e.kind in ("transfer.made", "transfer.refused") and e.causes}
        transfers = []
        for a in d.resolved[n_acts:]:
            if a.verb != "transfer":
                continue
            op = dict(a.payload or {})
            held = {(c.predicate, c.value) for c in w.persons[a.actor].ledger
                    if c.subject == op.get("to")}
            transfers.append(dict(actor=a.actor, **{k: op.get(k) for k in sorted(op)},
                                  outcome=outcome.get(a.id),
                                  claim_sourced=(f"shortfall:{op.get('kind')}",
                                                 op.get("amount")) in held))
        out.append(dict(tick=w.tick - 1, demanded=need, delivered=got,
                        asked=asked.about if asked is not None else None,
                        shortfalls=[(o.subject, o.predicate, o.value)
                                    for e in new for o in e.observed
                                    if str(o.predicate).startswith("shortfall:")],
                        transfers=transfers,
                        stores={r: dict(w.rungs[r].stores or {}) for r in (GRANARY, HUNGRY)}))
    return dict(seasons=out, hash=w.content_hash(), world=w,
                kinds=dict(sorted(Counter(e.kind for e in w.log).items())))


def main() -> int:  # pragma: no cover -- a printer over `run`
    for named in (True, False):
        print(f"== the steward's shortfall question {'NAMED' if named else 'NOT named (H-54 as shipped)'}")
        r = run(4, name_the_question=named)
        for s in r["seasons"]:
            print(f"tick {s['tick']}: demanded {s['demanded']} delivered {s['delivered']} at "
                  f"{HUNGRY}; asked about {s['asked']}")
            for sf in s["shortfalls"]:
                print(f"    shortfall recorded {sf}")
            for t in s["transfers"]:
                if t["actor"] == STEWARD:
                    print(f"    steward's transfer {t}")
            print(f"    stores after: {s['stores']}")
        print(f"hash {r['hash']}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
