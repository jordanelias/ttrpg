"""`harness.arc` -- THE DRIVER-SIDE ARC READER AND ITS TWO ROSTERS (CL-THRUST B0.1, G-28).

It reads; it writes nothing, mints nothing and is read by nothing in the game, so it moves no hash.
It is an INSTRUMENT: like `harness/storybar.py` and `harness/aperture.py` it reports a reading and
grades nothing. What it computes is what the reading IS; the proposal that asked for it
(`proposals/2026-10-25-thrust-layer/00_THRUST_LAYER_DESIGN.md` §1.2, §8 B0.1) is reference
(`CLAUDE.md` §0.05) and fixes no behaviour.

THE QUESTION. For a person `p` and a thrust `a`, `ARC(p, a)` holds iff some act `A` by `p` and two
distinct Receipts `r_self`, `r_world` the gate minted satisfy:
  (1) `A` was ON THE THRUST (`on_thrust`, below), and was not refused (the refusal null);
  (2) `r_self` writes a `(kind, field)` of `ARC_SELF` on `p`, or on a Tenure whose `.subject` is `p`;
  (3) `r_world` writes a `(kind, field)` of `ARC_WORLD` on a record that is neither `p` nor a Tenure
      `p` owns;
  (4) `A` is in `causes*` of the Event carrying `r_self` and of the Event carrying `r_world`
      (`causes*` = the transitive closure of `Event.causes` through the log; an act id is a leaf);
  (5) `r_self` is not `r_world` (two Receipts, compared by identity).
A death is counted apart: `ArcReading.deaths` lists, per person, the acts that have a `person.died`
Event in their `causes*`, and no death Receipt is ever a self or a world write.

WHY THE ROSTERS EXIST (the failure the planted worlds observe). Every witnessed act deposits a claim
(`loop/witness.py`: `w.write("claim_ledger", ... emits="claim.deposited", subject=c.id, ...)`), so a
reading over ANY Receipt meets clause (3) after every seen act, and clause (2) by any self-write such
as `move`'s `Person.travel_leg`: "moved and was seen" would read as an arc, and a shuffled-`causes`
null could not catch it because the links are real. The rosters therefore name `(kind, field)` pairs
restricted to ACTS-class cells (rows of `write_matrix.yaml` whose `steps` include `RES`) and exclude by
name `claim_ledger`, every INTERIOR (`WIT`) cell and `Person.travel_leg`. `validate_roster` REFUSES a
pair that is not a `write_matrix.yaml` key, has no `RES` step, or is one of those exclusions, and it
runs at import and on every `read_arcs` call, so a roster handed in is refused the same way.

THE ROSTERS ARE HOMED HERE, NOT IN `rosters.yaml` (the B0.1 piece moves the roster to the instrument;
`rosters.yaml` is untouched). Their first reading is TL §1.2's table, `[ASSUMPTION; medium; Jordan to
correct]`:
  * `ARC_SELF`  -- `Tenure.since/until/term/degree`, `Person.capability/stance/pursuits`.
  * `ARC_WORLD` -- `Record.exists/stages`, `DocketItem.*`, `Site.condition`, `Rung.exists/stores`,
    `Office.exists/remit_acts`, and `Tenure.*`, `Person.stance/pursuits/body` on a record that is not
    `p`'s. Two wildcard readings, both [ASSUMPTION; medium; Jordan to correct]: `DocketItem.*` is its
    three RES cells (`matter`, `arrangement`, `petition`), listed rather than derived so a row added to
    the matrix does not join the roster unseen; `Tenure.*` is the SAME four cells `ARC_SELF` names
    (`since`, `until`, `term`, `degree`), leaving `Tenure.payload` out -- the narrower reading (the
    payload carries the remit grant and the determined-by mark, and `ARC_SELF` omits it).
Ownership, not the roster, tells self from world: the same pair is a self write on `p`'s record and a
world write on anyone else's. Clause (5) therefore holds by construction of the split (a Receipt is
owned by `p` or it is not); it is coded as the literal test anyway so a roster or an owner rule that
ever lets one Receipt serve both sides is caught here and not in a reading.

CLAUSE (1) IS AN INPUT, NOT A DEFAULT. No thrust is authored in the tree yet (`thrust_axes` is B10-05), so
"an act formed on the thrust" has nothing to be read from. `read_arcs` takes `on_thrust(act, occasion)
-> thrust id or None`, where `occasion` is the row `harness/soak.py::_occasion_row(d, act)` gives (the
question the act answered, read off the DRIVER's `Scene`; None for an act formed from no scene). The
default is `None`, which reads FALSE for every person: the empty-data control. `ambition_thrusts(w)`
is TL §1.2 clause (1) read literally over what the tree already has -- a thrust is a live `commit` to an
OUGHT (`world_q.ambitions`), and an act is on it when its question is `need` about that Proposition or its
referents meet `world_q.goal_referents` -- for reading a real log. [ASSUMPTION; medium; Jordan to correct:
a thrust is an ambition; the referents are read at the END of the run, not when the question formed,
so a succession between is followed; a dead person's ambitions are gone, so his acts read off-thrust.]

THE REFUSAL NULL (G-28). A refusal writes nothing, so the rosters already exclude it -- but clause (1) does
not: a refused act on the thrust can still sit in the `causes*` of a later person's writes. An act is
dropped from clause (1) when it is REFUSED, by `harness/storybar.py::refusal_sets` (which reads
`harness/corpus_run.py::attempts`, the one owner of the made/refused rule, over the act store), so a
graded loss counts as refused, as the driver counts it. Pass `refused=` to override (a planted test).

THE TWO NULLS (controls, not verdicts). `shuffled_causes(log, seed)` permutes the `causes` lists among the
Events; a reading over it keeps every roster and every Receipt and breaks only the links. `unrestricted=True`
is the BOOKKEEPING NULL: the same log with every Receipt counting as a write (self when its record is `p`'s,
world otherwise, claim deposits and `travel_leg` included, a death still counted apart); it must read
HIGHER than the restricted reading on a log with witnessed acts, and when it does not the roster is
leaking and is fixed before anything else.

WHICH RECORD A RECEIPT WROTE. A Receipt carries `subject` (an id) and `field` but no kind. `_Records.of`
reads the kind from the id and the field, in this order: a Tenure id (the Tenure's own `.subject` owns it);
a collection of `World` holding the id whose `(kind, field)` is a matrix key; the one kind in the matrix
that has the field at all; the one kind whose row's `emits` holds the Event's kind. The OWNER of every
non-Tenure record is its own id (so a person-rung, whose id is the person's, is that person's; a person
who has since died still owns his writes), and of a claim deposit the claim's holder, read off the
ledgers (a claim no ledger holds any more is nobody's and reads as a world write). [ASSUMPTION; medium;
Jordan to correct] A Receipt that resolves to no kind matches no pair and counts only under
`unrestricted=True`.

NOT DONE HERE, AND SAID: the roster is by CELL, so a MATTER-driven write of an ACTS cell (the wear that
chains `Site.condition` after an act's last emission, a term maturing) counts when it is in the act's
`causes*`. TL §1.2 states the roster by cell and this reader follows it; `Receipt.driver` would tell the
two apart. A death's CASCADE (the victim's tenures closing) is a `Tenure.until` Receipt like any other and
is not subtracted either: `deaths` names the acts that reach a death, so a reader can set them apart.
[ASSUMPTION; medium; Jordan to correct.] No stage, deadline, closing, successor or deal is read.
"""

from __future__ import annotations

import dataclasses
import random
from collections import defaultdict

from ..data.matrix import MATRIX, Step
from ..queries import world_q
from ..state.carriers import Receipt
from ..state.ids import ROOT
from .soak import _occasion_row
from .storybar import refusal_sets


class ArcRosterRefused(ValueError):
    """A roster named a pair the ARC rosters may not hold (`validate_roster`)."""


# ---------------------------------------------------------------------------------------------
# THE ROSTERS. `(kind, field)` pairs; every one is checked against `write_matrix.yaml` at import.
# ---------------------------------------------------------------------------------------------

#: A death is the Event kind `person.died`, whichever of `Person.body` or `Person.exists` carries its
#: Receipt (the realm's carries `body`). Read off the matrix: the one kind both rows emit.
DEATH_KIND = "person.died"
assert DEATH_KIND in MATRIX[("Person", "exists")].emits and DEATH_KIND in MATRIX[("Person", "body")].emits

#: What no roster may name, besides a non-RES cell: the walking self-write and the death cell.
#: `claim_ledger` is matched on the FIELD (TL §1.2 "names `claim_ledger`").
_EXCLUDED_CELLS = frozenset({("Person", "travel_leg"), ("Person", "exists")})
_EXCLUDED_FIELDS = frozenset({"claim_ledger"})

# roster-exempt: THIS INSTRUMENT'S OWN ROSTERS, homed here by the B0.1 piece (not in `rosters.yaml`)
# and checked against `write_matrix.yaml` below, which is the head of every cell they name.
ARC_SELF = frozenset({
    ("Tenure", "since"), ("Tenure", "until"), ("Tenure", "term"), ("Tenure", "degree"),
    ("Person", "capability"), ("Person", "stance"), ("Person", "pursuits"),
})
ARC_WORLD = frozenset({
    ("Record", "exists"), ("Record", "stages"),
    ("DocketItem", "matter"), ("DocketItem", "arrangement"), ("DocketItem", "petition"),
    ("Site", "condition"),
    ("Rung", "exists"), ("Rung", "stores"),
    ("Office", "exists"), ("Office", "remit_acts"),
    ("Tenure", "since"), ("Tenure", "until"), ("Tenure", "term"), ("Tenure", "degree"),
    ("Person", "stance"), ("Person", "pursuits"), ("Person", "body"),
})


def validate_roster(pairs) -> frozenset:
    """`pairs` as a frozenset, or `ArcRosterRefused`: every pair must be a key of the write matrix
    (`data/matrix.py::MATRIX`), carry a `RES` step (an ACTS-class cell), carry no `WIT` step (an
    INTERIOR cell), and be neither `claim_ledger` (any kind), `Person.travel_leg` nor `Person.exists`."""
    out = set()
    for pair in pairs:
        kind, field = pair
        row = MATRIX.get(pair)
        if row is None:
            raise ArcRosterRefused(f"{kind}.{field} is not a key of write_matrix.yaml")
        if field in _EXCLUDED_FIELDS:
            raise ArcRosterRefused(f"{kind}.{field}: claim_ledger is witness bookkeeping, never an arc effect")
        if pair in _EXCLUDED_CELLS:
            raise ArcRosterRefused(f"{kind}.{field} is excluded by name (travel_leg is the walking self-write; "
                                   "exists is a death, counted apart)")
        if Step.RESOLVE not in row.steps:
            raise ArcRosterRefused(f"{kind}.{field} has no RES step: not an ACTS-class cell")
        if Step.WITNESS in row.steps:
            raise ArcRosterRefused(f"{kind}.{field} has a WIT step: an INTERIOR cell")
        out.add(pair)
    return frozenset(out)


validate_roster(ARC_SELF)
validate_roster(ARC_WORLD)


# ---------------------------------------------------------------------------------------------
# CLAUSE (1): the thrust an act is on. Callers pass the predicate; the default reads nothing.
# ---------------------------------------------------------------------------------------------

def ambition_thrusts(w):
    """`on_thrust` for `read_arcs`: TL §1.2 clause (1), literally, over the ambitions of `w`. For an act
    by `p` with an `occasion` row, the first of `world_q.ambitions(w, p)` (in the order the edges opened)
    that the question is about -- `source == "need"` and `about` the Proposition's id -- or whose
    `world_q.goal_referents` the question's referents meet; else None. Reads only."""
    def on_thrust(act, occasion):
        p = w.persons.get(act.actor)
        if p is None or occasion is None:
            return None
        for prop_id in world_q.ambitions(w, p):
            if occasion["source"] == "need" and occasion["about"] == prop_id:
                return prop_id
            if set(occasion["referents"]) & set(world_q.goal_referents(w, p, w.propositions[prop_id])):
                return prop_id
        return None
    return on_thrust


# ---------------------------------------------------------------------------------------------
# THE READING.
# ---------------------------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class ArcReading:
    """`arcs`: `{person id: {thrust id: sorted act ids A with ARC(p, A)}}` -- only persons with one.
    `deaths`: `{person id: sorted act ids}` -- on-thrust, unrefused acts of that person with a
    `person.died` Event in their `causes*`, whether or not they are an arc. `persons`: every actor of
    an act in the store (the denominator of a rate)."""
    arcs: dict
    deaths: dict
    persons: tuple

    def holds(self, pid: str) -> bool:
        return bool(self.arcs.get(pid))

    def count(self) -> int:
        """Persons with an arc."""
        return sum(1 for pid in self.persons if self.holds(pid))


def shuffled_causes(log, seed: int) -> list:
    """THE SHUFFLED-`causes` NULL: a copy of `log` whose `causes` lists are permuted among its Events
    (`random.Random(seed)`), every Receipt, id and kind kept. The roster and the writes are as they were;
    only the links are broken."""
    events = list(log)
    lists = [list(e.causes) for e in events]
    random.Random(seed).shuffle(lists)
    return [dataclasses.replace(e, causes=c) for e, c in zip(events, lists)]


def _reach(log, cand: dict) -> dict:
    """`{event id: frozenset of the candidate act ids in causes*(event)}`, an iterative memoised walk
    (cycle-safe: an Event on the current path contributes nothing through itself, which only a
    `shuffled_causes` log can produce -- the real log's causes all point backward)."""
    by_id = {e.id: e for e in log}
    memo: dict = {}
    for root in by_id:
        if root in memo:
            continue
        stack, on = [root], {root}
        while stack:
            top = stack[-1]
            pending = [c for c in by_id[top].causes
                       if c in by_id and c not in memo and c not in on]
            if pending:
                stack.append(pending[0])
                on.add(pending[0])
                continue
            acc = set()
            for c in by_id[top].causes:
                if c == ROOT:
                    continue
                if c in cand:
                    acc.add(c)
                acc.update(memo.get(c, ()))
            memo[top] = frozenset(acc)
            stack.pop()
            on.discard(top)
    return memo


class _Records:
    """Which `(kind, field)` a Receipt wrote and whose it is, for one world (see the module docstring)."""

    def __init__(self, w):
        self.w = w
        self.tenure_subject = {t.id: t.subject for t in w.tenures}
        self._holder = None
        self._kinds_of_field: dict = defaultdict(set)
        for (kind, field) in MATRIX:
            self._kinds_of_field[field].add(kind)

    def _claim_holder(self) -> dict:
        if self._holder is None:
            self._holder = {c.id: p.id for p in self.w.persons.values() for c in p.ledger}
        return self._holder

    def of(self, r, ev) -> tuple:
        """`((kind or None, field), owner)` for Receipt `r` carried by Event `ev`."""
        sub, field = r.subject, r.field
        if sub in self.tenure_subject and ("Tenure", field) in MATRIX:
            return ("Tenure", field), self.tenure_subject[sub]
        cls = self.w.class_of(sub)
        if cls is not None and (cls, field) in MATRIX:
            return (cls, field), sub
        kinds = self._kinds_of_field.get(field, ())
        if len(kinds) > 1:
            kinds = {k for k in kinds if ev.kind in MATRIX[(k, field)].emits}
        if len(kinds) == 1:
            kind = next(iter(kinds))
            # a claim deposit's id is the claim's, not the holder's: the owner is whose ledger holds it
            owner = self._claim_holder().get(sub, sub) if field == "claim_ledger" else sub
            return (kind, field), owner
        return (None, field), sub


def read_arcs(w, d, on_thrust=None, *, n=None, refused=None, log=None, unrestricted=False,
              self_fields=ARC_SELF, world_fields=ARC_WORLD) -> ArcReading:
    """`ARC(p, A)` over the world `w` and its driver `d`. Reads only.

    `on_thrust(act, occasion) -> thrust id | None` is clause (1); `None` (default) reads every act
    off-thrust. `refused` is the set of act ids the refusal null drops; by default
    `storybar.refusal_sets(w, n)[0]` with `n` the seasons run (default `w.tick`, which
    `corpus_run.attempts` needs only as the upper bound of the ticks it looks Events up at). `log`
    defaults to `w.log` (a test plants its own). `unrestricted=True` is the bookkeeping null: the
    rosters are ignored. The rosters are `validate_roster`ed on every call."""
    self_fields, world_fields = validate_roster(self_fields), validate_roster(world_fields)
    log = list(w.log if log is None else log)
    acts = tuple(w.acts)
    persons = tuple(sorted({a.actor for a in acts}))
    cand: dict = {}
    thrust_of: dict = {}
    if on_thrust is not None:
        if refused is None:
            refused = refusal_sets(w, w.tick if n is None else n)[0]
        for a in acts:
            t = on_thrust(a, _occasion_row(d, a))
            if t is not None and a.id not in refused:
                cand[a.id], thrust_of[a.id] = a, t
    if not cand:
        return ArcReading({}, {}, persons)

    reach = _reach(log, cand)
    records = _Records(w)
    selfs, worlds, dead = defaultdict(list), defaultdict(list), defaultdict(set)
    for ev in log:
        hit = reach.get(ev.id)
        if not hit:
            continue
        if ev.kind == DEATH_KIND:
            for aid in hit:
                dead[aid].add(ev.id)
            continue
        for r in ev.changes:
            if not isinstance(r, Receipt):
                continue
            pair, owner = records.of(r, ev)
            for aid in hit:
                if owner == cand[aid].actor:
                    if unrestricted or pair in self_fields:
                        selfs[aid].append(r)
                elif unrestricted or pair in world_fields:
                    worlds[aid].append(r)

    arcs: dict = defaultdict(lambda: defaultdict(list))
    for aid, rs in selfs.items():
        rw = worlds.get(aid)
        # clause (5), the literal test: some self Receipt is not some world Receipt
        if rw and any(a is not b for a in rs for b in rw):
            arcs[cand[aid].actor][thrust_of[aid]].append(aid)
    deaths: dict = defaultdict(list)
    for aid in dead:
        deaths[cand[aid].actor].append(aid)
    return ArcReading({p: {t: tuple(sorted(a)) for t, a in ts.items()} for p, ts in arcs.items()},
                      {p: tuple(sorted(a)) for p, a in deaths.items()}, persons)
