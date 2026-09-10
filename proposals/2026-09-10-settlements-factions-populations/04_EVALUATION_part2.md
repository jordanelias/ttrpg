# Part C (2 of 2) — evaluation: the political proposals, the seam, and the overturn table

## Status: **PROPOSED (2026-09-10). HELD BACK IN FULL** — see `00_INDEX.md`. Continues `04_EVALUATION.md`.

Loci are the tree at `ccc3f2a`; the relocation map is `04_EVALUATION.md` §0.

---

## §7 · The theorem that governs all three political proposals

All three claim, in different words, that **somebody notices**. A superior notices a defection; an
issuer notices defiance; bystanders notice a commitment. On this tree none of them can, and the reason
is one mechanism rather than three.

A claim reaches a person's question set through **Q2**, which admits it only if
`c.subject == p.id or c.subject in mine`, where `mine = {t.object for t in p.tenures if t.live}`
(`world_q.py:178, 196-199`). So a claim **about a person** is invisible unless that person is already
the *object* of one of the reader's live tenures — a `tie`, `knot`, `oblige` or `succeed`.

**None of those verbs has an effect.** `EFFECTS` registers ten: `confer`, `revoke`, `convene`, `move`,
`work`, `create_record`, `destroy_record`, `kill / wound`, `utter`, `transfer` (`effects.py:91-406`).
A verb with a `writes:` row and no effect raises `Unspecified` at `resolve.py:233-242`.

> **No computed act can place a person's id where another person's questions would find it.**

`references/design_rulings_2026-09-06.md:298` states the same line as a design instruction — *any new
deposit whose subject is not a person id or a live Tenure object is inert on arrival; design against
this line first.* **P5 designed against it and says so. P6 and P7 did not, and do not.**

Compounding it: `revoke` — the act both P6 and P7 rely on as the consequence — **cannot be formed by
anyone.** It is `remit:revoke`-eligible, and `remit:` is declined person-side by construction
(`options.py:163-165`; `H-71`, tier 0, `hole_register.yaml:795-799`: *"§F1 clause 2 says eligibility is
evaluated PERSON-SIDE, and `remit:<act>` CANNOT BE"*). Its predicate and effect also read
`payload["office"]` (`predicates.py:201-203`; `effects.py:132-133`), and `office` is not on the closed
operand roster, so it could not be carried even if the eligibility resolved.

---

## §8 · P5 · Risk of revolt is a Query

### N — six directions

**NARROWED to authored commitments, and one direction is carried by a reader P5 does not name.**

The proposal's own admission is correct and I could not break it. I attacked it with the shipped
`claim_subject_rule = "both"` (`fixtures.py:334`): a witnessed `utter` deposits a claim whose subject is
the Proposition id (`epistemic.py:133-137`), and Q2 admits it only if that id is already in `mine` —
that is, only if the witness has already committed to it. A `tell` about the Proposition lands the same
way. **The attack failed; an uncommitted bystander can never form a `commit` candidate.**

**But the top-down direction *is* carried, by Q2 rather than by Q3.** P5 describes the crossing as
reaching people through presence, in Q3's shape. Q3 keys on `w.sites.get(who)` (`world_q.py:219-223`)
and a rung id is not a site, so Q3 can never fire on a `subject = rung` crossing. What does carry it:
the crossing is a witnessed Event with `subject = rung`, it deposits a claim with that subject, and
**every person whose live `contain` object is that rung has it in `mine`** — so Q2 fires next season
with the rung as referent. That is a real S-DOWN path, better than the one P5 claims, and P5 does not
describe it.

**Restated N-line:** *cut `commit_share` and an authored revolt cannot, by itself, raise a question for
the people standing in the town.*

### False N-lines — two

| object | disqualifier | evidence |
|---|---|---|
| `faction_value(w, prop)` | **no reader** — §2's *"it would be needed if Z were built"* row | Nothing in P1–P7 consults it. The claimed loss is *"§5.1 executable"*; step one of that walk is *a resolver reads the value*, and no object carries step one |
| `faction_q.resolve(w, prop)` | **no reader** | Its only consumer inside the set is `faction_value`. Layer 1 naming a resolver is a reference count, not an N-line |

Marking the gap honestly is not a §3.1 evasion — but an admitted consumer-less object still loses its
hearing. §5.1's arithmetic belongs in the set as **one sentence of vocabulary**, not as two objects.

`commit_share`, `incompatible` and the crossing survive, narrowed to authored commitments.

### The `band_floors` row does not load

P5 puts `commit_share` in `band_floors`. That table is `keys: [site_kinds]`, and its own note states
*"The outer key IS validated against `site_kinds`"* (`rosters.yaml:957, 962`). `site_kinds` is
`[harbour, seam, body]` (`:673`). **`commit_share` is not a site kind, so the row refuses at load.**
P5 cites `:956`, the `sweep:` line, and not `:957`. The repair is one object for one object: a
`commit_share_floors` fixture with its own register row and three-point sweep, which also leaves a
site-kind table keyed on site kinds.

### E

**E-OVERHEAD.** In: one effect, one view resolver, one predicate, two Queries, one table row plus the
key widening it needs, one Event kind and its emission site, one hole row, one LOOP row. Out: nothing.
Vocabulary +5.

**The denominator is the whole of P5's cost and the proposal states its opposite.** Every `commit`
edge the Query counts must be **authored** by a test or a case, because no computed act can mint one.
*"New primitive? None"* is true; the boast of a revolt that forms itself is **false as filed**.

**E-LEGIBILITY — findings.** The band crossing depends on a denominator — the weight of *named* persons
at and under the rung — that the player cannot estimate and that moves without any commitment changing:
a committed person walks in, an uncommitted one dies, P3 mints one. *"Recruit, and the town turns"* is
intuitable only if the player knows the town is three named people, and nothing tells them.

### R

**R-COMPLETE — findings.** P5 rules the crossing's `causes` to be *the commitment Events since the last
barrier — never `[ROOT]`*. But the share is a ratio and **both terms move by other acts**: `move`
(which executes), `person.died`, P3's mints. The falsifier's clause *every rise coincides with a
`commitment.made`* **fails on a world where a committed person moves in**, which is reachable today.
The `person.died` clause shows the proposal half-knows this. Separately, *"crossed a floor since the
last barrier"* needs the previous barrier's share, and caches are discarded at WITNESS
(`witness.py:36`) — so it must be reconstructed by undoing the commitment Events, which is unspecified.

**R-VARIETY — one line of play.** The recruiter's acts all execute; no follower can follow.

**R-WORLD — fail as declared.** The seat throws no hook unless a test commits for it.

**R-CHOICE — provisional.** Once a crossing lands, the mayor's table is real: Q2 with the rung as
referent offers `petition`, `transfer`, `speak`. That is genuine, and it is downstream of an authored
act.

### S

Top-down carried by Q2. Bottom-up: shape holds, tree authored-only. Vertical and diagonal hold.
**Lateral and horizontal deliver blind.** S-UP: P5 adds nothing — a crossing is not a demand, and
`petition` already exists. **S-DOWN: pass for the shape** — a postless person present at the rung gets
the question through their own witness set, and nobody routes it to them. Pauses correctly: pass.

**Methodology — findings.** Two, both in §9 below: the denominator divergence, and the claim that
`faction_value` *"replaces legacy `W_s × q_s` with the same shape"*. It does not: `W_s` counted the
settlement's whole population; `faction_value` counts committed members. That is a different quantity
asserted to be the same one.

### Repairs

1. Delete `faction_value` and `faction_q.resolve`; keep §5.1's formula as one sentence, marked as having
   no consumer until `W28`.
2. Replace the `band_floors` row with a `commit_share_floors` fixture.
3. Widen the `causes` rule to the commitment, `travel.moved`, `person.died` and `person.individuated`
   Events, and bring the falsifier's rise/fall clause with it.
4. State the reader correctly: the crossing raises **Q2** for persons contained in the rung.
5. Strike *"a cohort at weight 200 that commits after one `tell` **is** 200 minds moved by one scene"* —
   the proposal's own loop section, four paragraphs earlier, proves no uncommitted cohort can form that
   candidate.

---

## §9 · P6 · Forswearing costs

### N — six directions

**NARROWED to the authored act.** The attack the proposal names — *`revoke` alone models expulsion* —
genuinely fails: `T-m`'s owner-closure needs the subject's own act, and `revoke` is someone else's.
That much is real.

Everything else P6 claims runs through *"the superior's Q2 fires"*, and §7's theorem says it cannot.
`repudiate` emits `commitment.ended` with `subject = actor`; the deposit's subjects are the defector's
id and the tenure id; the superior's `mine` holds rungs, offices, records and propositions — **never a
person**, because no verb that would put one there has an effect.

**Restated N-line:** *cut P6 and a person cannot end their own commitment by their own act. Nothing
else in P6's claim survives on the executing tree.*

### False N-line — `entrenchment`

**Disqualifier 1: the carrier already exists.** `person_q.entrenchment(p, seasons_held, scale, span)`
is at `engine/season/queries/person_q.py:44-46`. P6 proposes `entrenchment(w, person, obj)` as new,
under a World-first signature, and **does not name the existing one**. The claimed loss — *a fresh
commit after a repudiation starts at 0* — survives the cut: the caller reads `since` off the current
live edge and passes `seasons_held`, exactly as `probes.py:1254-1261` already does.

P6's *"one Query on fields that exist"* is a **second owner of one rule**, which is also §7.3's
two-ladders defect. Delete it and cite the existing function.

### R-CHOICE — fail under Rule 3, and worse than the method's own worked example

Seat: a person holding a live commitment to X. Intent: *stop being bound by X.*

| act | gain | cost |
|---|---|---|
| `repudiate X` | the edge ends; X's share falls, resolver-side, where nobody reads it | 1 scene; `commitment.ended` witnessed; **"exposure" unreachable by any computed act** |
| commit Y and keep X | counted in both shares — a live contradiction | 1 scene; and nothing ever makes them betray one, because `choose` scores a constant |
| **do nothing** | **the same in practice** — the commitment binds only a Q4 standing question they may leave unanswered (`world_q.py:228-233`) | **0 scenes, no Event** |

Decaying-cost dominance at a playable seat. **This is worse than `SKILL.md` §13's worked example.**
There, the silent option reaches the same end more cheaply. Here the *explicit act has no gain the
actor can feel*, because a commitment on this tree constrains its holder through nothing but a question
they can ignore.

**It is not repairable inside P6.** The repair is whatever makes a bond felt — `H-62`, or a termed
`oblige` — and both are outside the set. **The claim that must be stated as a limit:** *"never free"*
is unsupported. *"Always possible"* holds, authored.

**The channel attack fails, and instructively.** I attacked the cost as a coin flip on `fan_out_mode`.
Under `all_five` the superior witnesses a social act only when co-located; under `total` he receives
the claim. **In both arms the break is downstream**, at Q2's `mine` and at `H-71`. The channel is
irrelevant; the cost is structurally zero for computed play.

**R-WORLD — fail.** *An NPC whose scoring now ranks the rival's OUGHT higher repudiates in a quiet
season* is false twice: scoring never changes (`H-62`), and the Q4 route forms `repudiate` with
`subject = prop.subject`, not the Proposition id, so the typed cell reads zero live commitments whose
object is a settlement and **refuses every time**. The one computed route to an executable `repudiate`
is a `tell` whose subject is the Proposition id landing in an already-committed listener's ledger —
narrow, and P6 does not name it.

**R-COMPLETE.** The effect is complete. The falsifier is not: it asserts that a witness holding
`remit:revoke` is offered `revoke` by `opening_set`, which contradicts `H-71` by name. As written it
cannot pass.

### S

Bottom-up holds in shape. Top-down — the revocation — is dead at `H-71`, at the `office` operand, and
at `mine`. S-UP: *a defector's history travels by telling* — `tell` executes, and the listener's Q2
does not fire on a person subject, so it **delivers blind**. Methodology: consistent with `revoke`,
both writing `until`. Pauses correctly: pass.

### Repairs

1. Delete `entrenchment(w, person, obj)`; cite `person_q.entrenchment`.
2. Restate the claim to what holds: *switching is always possible by the holder's own act and costs a
   scene; whether it is noticed by a question, or answered by a revocation, is blocked on `H-71` and on
   Q2's subject rule, and this proposal closes neither.*
3. Fix the falsifier: assert the claim lands; assert an **authored** `revoke` folds. Do not assert
   `opening_set` offers it.

---

## §10 · P7 · A dispensation is a document

### The overturn holds — and the warrant is better than the one P7 gives

P7 types `comply`'s operand as `{form: existence, of: subject, kind: Record}`, against a written
refusal at `verb_table.yaml:117` which says that reading *"would assert that an act's subject IS the
dispensation whose terms are sought, which no in-chain document says"*.

I attacked this as coining an operand by another route. **The attack failed.** `subject` is on the
closed roster; `existence` is already read as *an object of a named class*; and the exact precedent is
**`carry`** (`verb_table.yaml:86-93`), which ships the identical cell —
`{form: existence, of: subject, kind: Petition}` — with a note declaring the identical move: *"THE
SCOPING IS A CHOICE AND IS DECLARED: the prose is INDEFINITE (a Petition) and this reads it as the
petition being carried, which is the act's `subject`."*

So the tree has already made P7's move once, declared it, and given its reason — and `carry`'s prose is
*indefinite* where `comply`'s is *definite*, which is the easier case. **P7's move is not an overturn
at all: it is the application of a precedent the refusal failed to cite.** That is `CLAUDE.md` §0
test 4, and it is a stronger footing than P7's own §0.05 argument.

One point of care: `rosters.yaml:873-876` reserves the coinage to *"the ruling `H-94` is waiting for"*.
`H-94`'s structural half **closed 2026-09-04** (`hole_register.yaml:1094-1118`) and other rows still
cite it as blocking the Dispensation operand. The question is moot rather than resolved: **P7 coins no
operand**, so it does not need `H-94` either way. What is genuinely held back is the Layer 1
verb-table edit itself.

### False N-lines — two, and the second is a signature contradiction

**`suspicion` — no reader.** P7 says `compliance.given` claims *"are read by the same
`stance_toward`"*. `stance_toward(p, referent)` reads `p.stance` rows and never the ledger
(`choose.py:40-49`), and `stance` is an interior field no verb writes. The ledger reaches `choose` only
through Q2 formation and clause 4's `LedgerReader`, whose vocabulary is the typed `requires` stems —
which `compliance.withheld` is not. **C1 fails.** This is the set's third consumer-less Query and the
only one not marked as such; Jordan's E11 symmetry *"falls out"* of a number nothing reads.

**The comply/defy dispatch — C2, and it cannot run.** P7 makes `comply`'s `writes: []` with
`writes_note: "per the term's own row"` into *a dispatch to an effect that already exists*. An effect is
invoked only inside `_apply_write`, on the first `writes:` pair, and the whole block is guarded:
`_pairs = row.writes_at(_degree) if row.writes else ()`, then `if _pairs:` (`resolve.py:231-255`).
**`comply` declares `writes: []`, so `_pairs` is empty and an effect registered under that name can
never execute.** To run one, `comply` needs a `writes:` cell — and the writes depend on the term, so
the cell would have to be per-term: a new column.

The tree already refuses this shape and says why, for `dispatch`: *"Part E gives it `writes: []`, so an
order is an EMISSION and nothing else… whether they go is their own act next season"*
(`effects.py:87-89`). Under §8 this is also the set's **one clean hit** on its own declared discipline
*no engine decides a person's options*: an executor's act whose writes are fixed by another person's
document. The possibility survives the cut — compliance moving grain is the executor's own `transfer`,
which executes today.

### Where the delivery routes diverge, and P7 does not say so

- **Told route.** A `tell` deposits a claim whose subject is the Record id; the executor's Q2 admits it
  only if the Record id is in his `mine` — a live `hold` on it. Under the told route he holds nothing,
  so **the claim is inert on arrival.** P7's correction diagnosed the *absence* case correctly and then
  asserted the *presence* case, which clause 3 refuses for the same reason.
- **Carried route.** He holds it, so his Q2 fires — but carrying is `H-84`, tier 0, `absent`.
- **And the two routes have opposite recall consequences.** A `compliance.withheld` Event deposits with
  the Record id as a subject, so the **issuer's** Q2 fires only if *he* still holds the Record: true
  when he told it, false when he gave it away.

P7 names `W24(a)` as needed *for carrying*. It is needed for any computed compliance at all.

### The roster, and the terms that name no verb

`dispensation_terms` ships six of nine, and the claim is that *each term names the verb its compliance
is*. Three do: `extract → transfer`, `install → confer`, `cede → revoke + confer`. Of the rest, `tax`
is a clock unless it is `extract` repeated; `host` names no verb that moves another person; and
**`suppress` of "a proposition named" is unspellable by construction** — Propositions are frozen and
nothing destroys them (`carriers.py:409-419`; `effects.py:397-398`).

The `conviction_axes` precedent has three legs — the source says N and enumerates none, a `blocked_by`
row, and a ruling that it stays open (`rosters.yaml:145-159`). P7 has the first only. The precedent
licenses the *marker*; it does not license *"Gap filled: `F.15`"*. Under §0.2 the honest reading is
**partially filled: three of nine carry a compliance verb.**

### One unstated edit

`issue` writes `Dispensation.exists` (`verb_table.yaml:244`) and the fold gates that pair
(`write_matrix.yaml:112-118`), while the proposed effect mutates `w.records`. **As specified the gate
validates one row and the effect writes another carrier.** One edit makes the collapse P7 claims real —
`writes: [Record.exists, Record.stages]`, and retire the `(Dispensation, exists)` row. Today it is
narration.

### R-CHOICE — fail under Rule 3, in §13's exact shape

Seat: an executor named in a writ. Intent: *the writ is not executed.*

| act | gain | cost |
|---|---|---|
| `defy` | not executed | 1 scene; a claim in co-located witnesses; the issuer's Q2 only if he still holds the Record; `revoke` unformable regardless |
| never receive it | not executed | **0 — and this is the design** |
| receive it and ignore it | not executed | **0 scenes, no act.** The `ttl` expires at MATTER emitting `record.expired`, witnessed by its holder |

Identical gain; `defy`'s cost depends on someone choosing to tell; ignoring emits nothing the defier
did. **A player at the executor seat never defies.** The precedent §6 asks for already exists here —
the expiry emits — so the omission *is* visible; but the issuer's Q2 admits that expiry only along the
route where he kept the Record.

**Residual, stated:** an ignored writ is attributable on one delivery route and invisible on the other.
**"Attributable" is all P7 may claim; "punished" is a limit.**

**And the issuer's seat is bookkeeping.** `issue` is unformable person-side (`H-71`); `levy`'s effect is
unbuilt; `transfer`'s `from` binds his own containing rung, so he cannot reach the target's larder.
There is no dominance among formable acts because **none is formable.** The seat becomes a game after
`H-71`, `H-62` and a suspicion reader — three holes, of which P7 names one.

**R-VARIETY.** The terms roster customises the *vocabulary*. With `H-62`, each executor's answer to
every writ is the same forever — a portrait, and a dead seat once the issuer can neither notice nor act.

### Repairs

1. Delete the comply/defy dispatch effects; leave both emission-only on `dispatch`'s precedent. The
   compliance is the executor's own `transfer`, which the issuer can witness through the store route.
   The *"comply in word, transfer in deed"* gap this opens is the diegetic truth, and is the residual.
2. Delete `suspicion`, or name its reader. There is none in `decision/`.
3. Edit `issue`'s `writes:` and retire `(Dispensation, exists)`.
4. State which delivery route makes the issuer's Q2 reachable.
5. Cite `carry` at `verb_table.yaml:86-93` as the warrant.
6. Roster: `have: 3 with a verb / 6 named / 9 in Layer 1`; add a `blocked_by`; strike `suppress` of a
   proposition.

---

## §11 · The substrate/politics seam

P5–P7 claim to *run on P1–P4's substrate but not require it*. Tested:

1. **The envelope eats but cannot revolt, and nobody says so.** `mouths(r)` counts it, `population()`
   counts it, `commit_share` does not. P5's exclusion is right under Layer 1 and undeclared.
2. **P3 and P1 move P5's denominator without appearing in its loop register.** A loyal cohort of 200
   individuated by P3 **collapses** the share it was counted in; P1's deaths of the uncommitted raise
   it. P3 is a `−` on P5 and P1 is a `±` on P5, and no LOOP row names either. This is §7.2's diagonal
   direction — carried, and undeclared.
3. **The cohort-at-200 story is impossible twice** on the set's own findings: a cohort cannot form
   `commit`, and a minted cohort's first possible question is two seasons out. Where it *would* be
   possible it is a lever rather than a game — the whole town's weight rides on one `tell`.

---

## §12 · What survived, with the attacks that failed

A pass is licensed by a named failed attack, not by an absent finding. These attacks were run and
failed, and they are why the corresponding verdicts are passes.

- **P1's overturn of the starvation refusal holds.** Attacked three ways: through L4 — the gate fires
  only on `social and driver != "Act"` and `body` is `social: false`; through `T-b` — an outcome is what
  a decision produces and a body is *the case*; and through precedent — `Site.condition` crosses floors
  and emits without producing an outcome (`matter.py:233-258`). **Not an escalation.**
- **P1's body write passes the gate**, and P1's death cascade is licensed by the §15.3 seam.
- **P2 is not a container clock** — one driver pass over `sorted(w.rungs)`, exactly as wear.
- **P2's Malthusian bound is real:** at steady state `fed_ratio → yield/draw` and births fall toward
  zero.
- **P3's mint *shape* is right** — `tiny_world` seats every person with a same-id person-rung and a
  `contain` edge. Only the gate steps fail.
- **P4's warrant is `R4` verbatim**, and its `AX-1` and `T-b` arguments hold.
- **P5's "no producer" admission could not be broken** — every route to a Proposition id in a
  referent set passes through `c.subject in mine`, which requires a prior commitment. It is the set's
  most accurate claim.
- **`commit_share` is not a stored aggregate** — barrier-cached, discarded at WITNESS, and
  `Rung.__setattr__` refuses the field.
- **The crossing is not a threshold producing an outcome** — it emits and changes the question set, on
  the `matter.py:248-257` precedent.
- **`commit_count_guard` is not a no-op** — it inspects the edge list and raises on an ended edge, so
  P5's `L3 cl. 3` grade is correct.
- **P7's suspicion is neither an omniscient oracle nor a stored world condition** — it is a sum over the
  issuer's own ledger, and it decays, so it cannot ratchet. What fails is that nothing reads it.
- **P7's typed cell holds**, on the `carry` precedent.
- **§8 against the set's declared disciplines** — *no stored aggregate*, *no threshold produces an
  outcome*, *every effect traces to a self-interested act*: **zero clean hits on each.** The disciplines
  are real. The single clean hit is on *no engine decides a person's options*, it is a family of one,
  and it is repaired by a deletion.

---

## §13 · What would overturn each verdict

| verdict | what would overturn it |
|---|---|
| The set is `paper` | any execution artifact — a green test naming a proposal's falsifier, run against `engine/season/` |
| P4 refuses at load | a `requires_forms` entry for `amount`, or a cell of an existing form that carries the stake |
| P3's mint is refused | a matrix edit admitting CENSUS on `(Rung, exists)` and `(Tenure, since)` |
| P5's band row refuses | `band_floors` ceasing to validate its outer key against `site_kinds` |
| The Q2 theorem | an effect for `tie`, `knot`, `oblige` or `succeed` — after which a person id can reach another's questions and P6's and P7's noticing claims become reachable |
| `revoke` unformable | `H-71` closed, **and** `office` derivable person-side |
| Five objects have no reader | a resolver that consults `population()`, `faction_value`, `faction_q.resolve` or `suspicion` |
| P7's typed cell holds | an in-chain document ruling that `carry`'s indefinite-to-subject reading was itself wrong |
| P1's collapse is undeclared | a declared per-kind `k`, or a ruled summing rule for `short` |
| The political half is a substrate, not politics | `H-62` closed — a verb that writes a `Person` interior field |

---

## §14 · The one question this evaluation does not answer

**`E-1`** — whether the demographic loop is bounded by matter alone or by matter plus hearth capacity —
is filed as `ED-SE-0051`, `needs_jordan: true`. Nothing here bears on it: both arms ship with P1 as the
damping term, and every finding above applies identically under either.

What this evaluation *adds* to it is a cost that was not visible when it was filed. The capacity arm
requires a `hearth_capacity` fixture per `site_kind`, and `site_kinds` is closed at three with a
required row in three tables — so the capacity arm's real price is **one fixture table plus three table
rows per buildable kind**, and it composes with P4, which does not load as written. The matter-only arm
still costs nothing new.
