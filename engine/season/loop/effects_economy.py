"""`season.loop.effects_economy` -- labour, repair, material transfer: work, restore, transfer.

EXTRACTED from `effects.py` at the per-subsystem split (Phase 4). Holds the fabric-raising pair
(`work`/`restore`, both routed through the shared `_rise` formula, which stays local -- nothing
outside this pair calls it) and `transfer`, the two-sided store move, whose own private tail helper
`_renewals` (which winds `oblige` terms a payment covers) also stays local here rather than in
`effects_shared.py`: only `transfer` calls it. See `effects_shared.py` for `effect_for`, `_operand`
and the cross-file helpers this file's effects call (`_exercised_office`, `_oblige_term`, `_shift`).
"""

from __future__ import annotations

from ..queries.world_q import ceiling, home_of, share, upkeep_of, works_for
from ..state.carriers import Term
from ..state.gate import NO_CHANGE, Change, Subject, may_renew
from ..trace_log import TRACE

from .effects_shared import _exercised_office, _oblige_term, _operand, _shift, effect_for


@effect_for("work")
def _eff_work(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """`work` alters `(Site, condition)` by the act's declared delta. The DELTA IS NOT APPLIED
    HERE -- §27.3 sums every delta across the fold and clamps ONCE, so applying it per act would
    make the clamp arrival-order dependent, which §32 forbids. The write goes through the gate so
    the class and Partition are checked; the value lands in the accumulator.

    ⚠⚠ G4 -- THE ONE EFFECT WHOSE WRITE IS NOT WHERE ITS CHANGE IS, AND WHERE F9 IS JUDGED FOR IT.
    The plan's pre-flight named the trap: a gate that compares the SITE either side of this act's
    write sees no change BY CONSTRUCTION -- the site moves later, in `resolve()`'s one write per
    cell -- so `work` would be refused forever. So the change is judged TWICE, at the two writes
    that exist, each by the same before-and-after and neither by a rule of its own:

      1. HERE, PER ACT: the act STAGES its delta on the accumulator (`World.stage`), and the
         subject is that staged cell (`Subject.staged`). It moves iff the delta is non-zero -- an
         alter by zero stages nothing -- so a `work` declaring no delta, or a delta of 0, is
         `NoOpReceipt` -> `work.unavailable` at its own write. That is `H-94`'s worked case:
         `site.worked` over a repair nobody declared. The receipt still names the SITE, which is
         what the success Event has always carried (hash-identical where a real delta is staged).
      2. AT THE ACCUMULATOR, PER SITE: `resolve()` writes the clamped sum once, naming the Site, and
         the gate compares the site's condition either side. A clamp that eats the whole sum -- a
         site already at `condition_scale` being worked up, or two deltas cancelling -- moves
         nothing, and EVERY act that staged on that site is refused with it: their provisional
         `site.worked` is replaced in place by `work.unavailable` (`_refuse_after_the_fact`).

    WHY NOT JUDGE ONLY AT (2), the plan's candidate: an act with no delta stages nothing, so the
    accumulator would never learn of it and its `site.worked` would stand beside a site another
    act moved. WHY NOT ONLY AT (1): a per-act delta cannot see the clamp. The staged cell is not a
    parallel mechanism -- it is a store the gate reads like any other, which is why the gate needed
    no branch for `work`.

    ⚠ THE DELTA IS READ FROM THE ACT'S OWN DECLARED CHANGES, ON ITS OWN SITE, AND NOWHERE ELSE.
    Before G4 the accumulator summed every integer delta on ANY success Event's `changes[]` for ANY
    site -- so an act of a verb whose row writes no `Site.condition` could move a site by riding a
    delta on its Event, a write the matrix never saw declared. Now only an act whose row writes
    `Site.condition` stages -- `work`, and since plan position `24e` `restore` -- and only on the site
    it names. The DECLARED delta is unreachable from a computed act (none carries one: `H-94`).

    ⚠⚠ PLAN POSITION `24e` -- *"`work` advances `stage` (and inherits G4's accumulator answer)"* --
    AND WHAT THAT MEANS HERE, READ AGAINST THE CONTENT OWNER. A computed `work` carries no declared
    delta, so before `24e` it staged nothing and every one was `work.unavailable` (`H-105`: *"a loop
    with one arm cut is a RATCHET wearing a loop's clothes"*). It now has a SECOND source, used only
    when the act declares none: THE WORKS NAMING THE SITE. When a live works plans this site's kind
    at this site's rung (`queries/world_q.py::works_for`), the act stages `_rise` -- the headroom to
    the works' `ceiling`, shared among those standing at the fabric -- through the SAME accumulator,
    judged at the same two writes. So the works ADVANCES: each ripened term lifts the ceiling, and
    labour raises the fabric toward it. ⚠ NOT A `stage` KEY ADVANCED ON THE RECORD, which r2 `04`
    §A.6.1 RULED out on three grounds, the third decisive (*"progress is the condition and permission
    to progress is the ceiling, so nothing needs counting"*): `subject_matter` has no matrix row, so
    moving a stage there is an ungated write, and it would be a second progress ladder beside
    `Site.condition`. The stage a works has reached IS its fabric's condition against its ceiling.
    ⚠ AND NOT A THIRD FORMULA: `_rise` is `restore`'s own (`_eff_restore`), one owner for one
    quantity (§0.06 S: *"calculations consistent in methodology"*). What separates the two verbs is
    their preconditions, not their arithmetic -- `work` asks that the site clear its floor, `restore`
    that the actor stand at it -- and that `work` advances ONLY a works: a site no works names
    stages nothing from here, which is the position's control (*"a `text` Record is NOT advanced
    by `work`"*: a text Record has no `plan`, so it can never be the works a site is named by).
    REJECTED: summing the declared delta AND the works' rise -- one act would then move a fabric by
    two magnitudes from two owners, and the hand-built channel (`H-94`) would stop meaning what the
    act declared."""
    # ⚠ NO FALLBACK. This read `or next((x for x in sorted(w.sites)), None)` -- the alphabetically
    # FIRST site in the world -- so a `work` with no site named one nobody chose. `_eff_move`
    # refused the identical situation and this did not; found by the W-A adversarial pass, which
    # noted the two are the same defect one verb along. `W-C` gave that answer ONE owner
    # (`_operand`) rather than two copies of it.
    site = _operand(a, "site")
    site_deltas = tuple(c.delta for c in (a.changes or ())
                        if c.subject == site and c.field == "condition" and isinstance(c.delta, int))
    delta = sum(site_deltas)
    fabric = w.sites.get(site)
    # `not site_deltas`, NOT `not delta`: the fallback is for an act that declares NO delta on this
    # site, not for one that declares an explicit `0` -- the two read alike through `sum(())`,
    # `sum((0,))`, so testing the summed value would also replace a hand-built act's declared `0`
    # with the works' rise, which is not what "the act declares none" (above) says.
    if not site_deltas and fabric is not None and works_for(w, fabric.rung, fabric.kind):
        delta = _rise(w, fabric)
    cell = Subject.staged("Site", site, "condition")
    return Change((cell,), lambda: w.stage(cell.ref[1], a.id, delta))


def _rise(w: "World", site) -> int:
    """HOW FAR ONE ACT RAISES A FABRIC -- the ONE owner of `restore`'s formula, which `work` also
    reads when it advances a works (plan position `24e`). `verb_table.yaml`'s `restore` row:
    `Δ = +(1 − condition) × f(degree) × share` (§54 item 7's mirror), in fixed point:

      * `(1 − condition)` IS THE HEADROOM TO THE CEILING, `ceiling(w, site) − condition` -- r2 `04`
        §A.6.5's units decision (`condition` is an int on `condition_scale`, S48), bounded by the
        works (`queries/world_q.py::ceiling`, the full scale where no works names the site). Floored
        at 0: a fabric above its ceiling is not raised, and is not lowered here either.
      * `× share` IS `queries/world_q.py::share`, `(1, n)` for `n` persons standing at the fabric --
        r2 §A.6.4's commons: at a harbour forty stand at, one act moves a fortieth of the headroom.
        Multiply first, divide last, so the fraction is exact to the int.
      * ⚠ `× f(degree)` IS NOT BUILT, AND THE REASON IS THE FOLD'S, NOT THE FORMULA'S. r2 §A.6.5 reads
        it off `res.degree` (*"the existing degree ladder, not a new one"*), but `restore` and `work`
        are UNCONTESTED -- no `contests:` -- and `_fold` hands every such act `resolution=None`
        (*"`None` on every uncontested act, which is honest: no contest graded it"*), so r2's own
        body would raise on `None.degree`. The term is therefore the IDENTITY: an act no contest
        graded is taken whole. REJECTED: a fixture factor (an invented number standing where the
        design says a degree goes) and routing `restore` through a contest (a prize no subsystem
        claims, `rosters.yaml: contest_subsystems`). `H-164` carries the term, and the sweep r2
        declares for `share`.

    So the pace of a works is its TERMS (the ceiling) and its COMMONS (the share), never a rate:
    one hand alone at a fabric raises it to its ceiling in one act, and then nobody can raise it
    further until another term ripens -- r2 §A.6.6's TERM-STALL, arithmetic and not a cooldown."""
    headroom = max(0, ceiling(w, site) - site.condition)
    if not headroom:
        return 0
    num, den = share(w, site)
    return (headroom * num) // den


@effect_for("restore")
def _eff_restore(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `24e` -- `restore` RAISES A FABRIC. The row was TYPED (`verb_table.yaml`, W3's
    cell: *the site exists and the actor is present at it*) and had NO EFFECT, so
    `resolvable_verbs()` excluded it: `★` measured it formed 46 times in a populated season and
    offered never. r2 `04` §A.6.2's moment 4, *"BUILD IT UP"*, and §A.6.5's body, built as
    specified but for the degree term (`_rise` says why that is the identity).

    `work`'s ACCUMULATOR SHAPE, EXACTLY (G4, `_eff_work`'s docstring): the act STAGES its delta on
    `(Site, condition)` through `World.stage`, named as a `staged` subject, and `resolve()` sums every
    act's delta on the site and clamps ONCE, under the works' ceiling -- so two hands at one fabric
    commute and neither's delta is applied alone. It is judged twice, as `work` is: a delta of 0 (a
    fabric already at its ceiling -- *"you cannot hurry mortar"*) stages nothing and is
    `NoOpReceipt` -> `restore.refused` at its own write; a sum the clamp eats is refused after the
    fact (`loop/resolve.py::_refuse_after_the_fact`), which reads the row's refusal and so needed
    no line for `restore`.

    BUILDING AND REPAIRING ARE ONE ACT AT DIFFERENT BANDS (r2 §A.6.3's table, and its RULED
    heading): at a fabric no works names the ceiling is the full scale, so this repairs wear; at a
    works' fabric it raises the first courses as far as the ripened terms allow. No works is needed
    to restore, and no office: `own` admits and presence binds in the precondition, so *"a rival may
    finish what somebody else began"* (r2 §A.6.7) with no special case anywhere.

    DECLINES: a site that does not exist (a hand-built act that skipped the precondition) is
    `NO_CHANGE` -> `restore.refused`."""
    sid = _operand(a, "site")
    site = w.sites.get(sid)
    if site is None:
        return NO_CHANGE
    delta = _rise(w, site)
    cell = Subject.staged("Site", sid, "condition")
    return Change((cell,), lambda: w.stage(cell.ref[1], a.id, delta))


@effect_for("transfer")
def _eff_transfer(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§54 item 7's mirror: the giver's store goes DOWN and the receiver's goes UP.

    ⚠ THE FIRST VERSION ONLY DECREMENTED, and §E3 says `transfer` writes `(Rung, stores)` **×2**,
    one per side. A one-sided transfer ANNIHILATES MATTER -- six grain left the world and arrived
    nowhere, in an economy where `yield` is the only source (#353 `:856`). The scarcity proof still
    passed, because it only watched the giver: a run can be right about the thing it looks at and
    wrong about the world.

    G4 -- WHAT IT NAMES: BOTH RUNGS, giver first, each whole -- the two `(Rung, stores)` writes and
    the two ids it always reported. Two no-ops become visible that the old contract reported as
    successes: a transfer of `amount` 0, and a transfer from a rung TO ITSELF (the decrement and
    the increment land on one store and cancel). Each moved nothing and is now `transfer.refused`.
    Neither is a transfer; both published `transfer.made` with two receipts. MEASURED BEFORE THIS
    POSITION on `build_realm(0)`, four seasons: no `transfer` reached this effect at all (every one
    refused at its precondition), so no run moves."""
    # ⚠ FOUR SILENT DEFAULTS STOOD HERE AND `W-C` DELETED ALL FOUR: `from`/`to` defaulted to
    # `""`, `kind` to `"grain"` and `amount` to `1`. Each was §0.05's literal-in-a-body, and
    # together they made an operand-less `transfer` a WELL-FORMED act about a granary nobody
    # named. They are `_operand` reads now, and their two open values are fixtures with a register
    # row and a sweep (`H-94`).
    src = w.rungs.get(_operand(a, "from"))
    dst = w.rungs.get(_operand(a, "to"))
    kind, amount = _operand(a, "kind"), _operand(a, "amount")
    # ⚠ A SIDE THAT IS NOT A RUNG MEANS THE TRANSFER DID NOT HAPPEN, and returning nothing is what
    # makes the fold emit the refusal. This branch became reachable FROM A COMPUTED ACT the moment
    # operands became real: a person names a receiver from their question's referents and may name
    # something that is no rung at all. The old shape moved the giver's side anyway, which is the
    # matter ANNIHILATION this effect's own docstring records -- grain leaving the world and
    # arriving nowhere. §42.2's polarity: an unperformable transfer refuses; it does not
    # half-happen.
    # ⚠ *"IT SURVIVED ONLY BECAUSE NO COMPUTED ACT EVER BOUND `from` TO BEGIN WITH"* STOOD HERE
    # AND IS FALSE; STRUCK BY THE `W-C` ADVERSARIAL PASS. No COMPUTED act bound `from` -- but
    # probe `F10` did, in its payload, and omitted `to`, so the old effect decremented `Hh` and
    # delivered nowhere: `F10` DESTROYED 6 GRAIN ON EVERY PROBE RUN, in an economy where `yield`
    # is the only source. Measured by weighing every rung across the probe's own season: total
    # store mass ends at 107 on the pre-`W-C` tree (`45a537c`) and at 113 here, and the difference
    # is exactly the 6. The path was reachable AND REACHED; only the computed path was closed, and
    # `F10`'s payload edit is a BUG FIX in a live probe rather than a signature accommodation.
    # `F10` now asserts conservation, because its old assertion set could not observe the failure
    # it was sitting on (§0.1 point 2).
    if src is None or dst is None:
        TRACE.decision(f"transfer names a side that is no rung -> from "
                       f"{_operand(a, 'from')!r} to {_operand(a, 'to')!r}", "E3/S27.1",
                       chose="change nothing, so the fold emits the refusal",
                       alternatives=["move the giver's side anyway (matter leaves the world)"])
        return NO_CHANGE

    renewed = _renewals(w, a, src.id, dst.id, amount)

    def perform() -> None:
        _shift(src, dst, kind, amount)
        for t, term in renewed:
            t.term = term
    # BOTH SIDES, because §E3 says `transfer` writes `(Rung, stores)` twice -- one per side -- and
    # a one-sided report would make the Event name half of what it did. The `if r is not None`
    # filter that stood here is gone with the branch above that made it necessary.
    # ⚠ PLAN POSITION `17b`: EACH SUBJECT NOW NAMES THE KIND IT EARNS. The row declares
    # `term.renewed` beside `transfer.made`, and a subject earning `None` earns EVERY declared kind
    # (`loop/resolve.py::_fold`) -- so left as they were, the two rungs would publish a renewal on
    # every transfer that renewed nothing, and one renewed edge would earn `term.renewed` ALONE and
    # silently drop `transfer.made`. Named per kind, an ordinary transfer emits exactly what it
    # always did. The renewed edges ride as `edge` subjects, judged by G3's diff (`renewal`).
    # ⚠ THEIR RECEIPTS CARRY THE FIRST PAIR'S FIELD, `stores`, not `term` -- the fold mints every
    # subject's receipt against the write pair the effect ran on (`_eff_confer`'s docstring has the
    # history; `establish`'s re-stamped holds carry `exists` the same way). A known limit of the
    # one-effect-per-act fold, not a claim that a Tenure's stores moved.
    return Change((Subject.entity("rungs", src.id, "transfer.made"),
                   Subject.entity("rungs", dst.id, "transfer.made"))
                  + tuple(Subject.edge(t, "term.renewed") for t, _ in renewed), perform)


def _renewals(w: "World", a: "Act", src: str, dst: str, amount) -> list:
    """PLAN POSITION `17b` -- WHICH `oblige` TERMS A `transfer` RENEWS, as `[(edge, its new Term)]`.
    The whole of *"payment by `transfer` renewing `oblige` terms"* (the plan's Contradiction-1 box;
    the retirement plan's G2: *"treasury = `Rung.stores` at the office's own rung; payment = the
    existing `transfer` verb; `oblige` Tenures carry a term (T-n) the paying act renews"*), and
    `04 F.18`'s repair: *"A MATTER payment would be a fourth clock, so the repair is a verb."*

    A TRANSFER IS A PAYMENT OF UPKEEP WHEN, AND ONLY WHEN, all of these hold:
      1. it is exercised THROUGH A SEAT (`Act.via`) whose seated holder is the actor -- `may_renew`,
         the gate's own `renewal` test, asked here first so the effect never names an edge the gate
         would refuse (a `NotYours` would escape the fold and end the season);
      2. it is paid OUT OF THAT SEAT'S OWN RUNG -- *"what the post pays its establishment out of the
         office's stake"* (`holonic_ARCHITECTURE.md:428`). A holder paying from his own hearth is
         giving a gift, not keeping a seat; a seat with no rung has no treasury and cannot pay;
      3. matter actually MOVED: another rung, a positive amount. A transfer from a rung to itself
         cancels to nothing (G4 already refuses it as a no-op), and without this clause a seat whose
         obligee lives at the seat's own rung could renew a term by paying itself;
      4. the receiving rung is where an obligee IS PRESENT (`home_of`, the one owner of *where a
         person is* -- NOT `residence_of`; ⚠ found by the terminal Phase-2-close critique,
         2026-09-30: this clause was written and reasoned about as "home" meaning residence, before
         `19c` split presence from residence, and was never revisited. Its own stated reason ("the
         larder upkeep fills") is ALSO stale since `24f`: individuals no longer draw from a larder
         at all (`ED-IN-0255`), so upkeep paid to wherever an obligee stands fills nothing today --
         unruled whether this clause should read `home_of` or `residence_of` (`hole_register.yaml`
         H-174), and whether it should still cite the larder as its reason once it does).
    Then it renews, of that seat's live `oblige` edges carrying a term whose subject is present at
    the receiving rung, as many as the amount covers at `upkeep_of(seat)` apiece (`0`: all of them),
    SOONEST-MATURING FIRST, ties by edge id -- the man about to lapse is paid first, and the order
    is a rule, not an accident of the store. Each new term runs `oblige_term` seasons ON FROM WHERE
    THE OLD ONE STOOD (so paying early buys the next term; it is not lost), and is `declared_by`
    this act, so the next lapse -- if nobody pays again -- cites this payment as the last hand to
    wind the clock (AX-5).

    ⚠ NO ENTITY IS NAMED AND NO OUTCOME IS SCRIPTED. Embezzlement -- narrative #3, *"already runs"*
    (`proposals/2026-09-12-emergent-narrative-primitives-v2/01_THE_TEN.md` §3) -- is not a branch
    here: a steward who moves the treasury to his own hearth simply meets clause 4 for nobody, the
    terms he did not pay mature at MATTER, and the seat's `establishment_of` shrinks. That is the
    observable this position gives #3, and it falls out of the rule rather than being written.

    ⚠ ONE TERM PER OBLIGEE PER PAYMENT, and any excess is simply transferred. Buying several terms
    for one man with one large payment is a reading the fixture does not rule on, and taking it
    would make "how far ahead may a seat prepay" a second quantity with no row.

    ⚠ WHAT NO COMPUTED ACT CAN REACH TODAY, STATED RATHER THAN IMPLIED. Clause 1 needs `Act.via` on a
    `transfer`, and `decision/options.py::exercised_seat` sets `via` only for a `remit:` alternative
    -- `transfer` is `own | hold:<store>`, so every computed transfer carries `via=None` and renews
    nothing. And no computed act forms an `oblige` (its row is untyped, `17a`). So the mechanism is
    EXECUTED by hand-built acts (`tests/test_term_upkeep.py`) and by MATTER's maturation, which needs
    no act at all; a person CHOOSING to pay upkeep is `H-158`'s `unblocks:`, not this body's.

    The cheap refusals come first, so an ordinary transfer (no `via`) reaches no Query and moves no
    trace line."""
    seat = _exercised_office(w, a)
    if seat is None or seat.rung != src or src == dst or amount <= 0:
        return []
    if not may_renew(w, a.actor, a.via, seat):
        return []
    n = _oblige_term(w)
    if n is None:
        return []                         # `H-159`'s control: no term exists to renew
    homes = home_of(w)
    due = sorted((t for t in w.tenures
                  if t.kind == "oblige" and t.object == seat.id and t.live
                  and t.term is not None and homes.get(t.subject) == dst),
                 key=lambda t: (t.term.matures_at, t.id))
    each = upkeep_of(w, seat.id)
    covered = len(due) if each == 0 else min(len(due), amount // each)
    return [(t, Term(t.term.matures_at + n, a.id)) for t in due[:covered]]
