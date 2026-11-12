# VERBS — BINDING family: build-out of the twelve `binding_decision` verbs

## Status: REFERENCE (a verb build-out audit under `VERBS_BRIEF.md`; resolves nothing at runtime)

Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12).

## Read at: 84d2a02 (working tree)

Family: the twelve rows of `engine/season/verb_table.yaml` whose `stratum:` is `binding_decision`:
`confer`, `convene`, `determine`, `dispatch`, `establish`, `issue`, `marshal`, `surrender`, `pardon`,
`release`, `revoke`, `succeed`. They are the governance verbs: who sits where, who is ordered, what a room
decides, who is let go. The FA lane's audit, addendum and proposals and the SC lane's proposals bind this
file; they are cited by path and not redone. The exact edits are in
`proposals/14_VERBS_BINDING_*.md`, one per batch of the landing order (§ "Landing order" at the end).

Every reading names its command, seed and season count. `[UNVERIFIED]` marks what was not checked.
`[FA]` marks a figure taken from the FA lane's run of the same instrument on the same tree
(`scratchpad/runs/FA/aperture_2_0.txt`), which this lane read at the line and did not re-run at that seed;
this lane's own reading is `aperture 2 1` (seed 1, two seasons), in
`scratchpad/runs/VERBS_BINDING/aperture_2_1.txt`.

## 0. Verdict for the family

**Two of the twelve work in computed play in the sense the premise requires; three execute and write
nothing a later decision reads; four form and are never chosen or are always refused; three are never
formed at all.** The mechanisms are sound almost everywhere (each effect returns a `Change` through the
write gate, each precondition asks the gate's own predicate, no entity is special-cased). What fails is
reach: the acts that redistribute power are not chosen, and the acts that are chosen bind nobody.

| verb | state (seed 0, 2 seasons, realm; `[FA]`) | verdict |
|---|---|---|
| `convene` | formed 12, attempted 12, executed 12 | **executes; consequence thin** (a date; summons nobody) |
| `dispatch` | formed 26, attempted 12, executed 12 | **executes but writes nothing** |
| `issue` | formed 18, attempted 26, executed 19, refused 7 on `authority` | **executes; binds nobody** |
| `establish` | formed 6, attempted 8, executed 1, refused 7 (no reason recorded) | **forms, mostly refused** |
| `determine` | formed 8, attempted 2, executed 0, refused 2 on `docket` | **forms but is refused** |
| `release` | formed 83, attempted 15, executed 0, refused 15 (no reason recorded) | **forms but is refused** |
| `confer` | formed 5, attempted 0 | **formed, never chosen** |
| `revoke` | formed 5, attempted 0; a computed act is refused at clause 1 by construction | **formed, unexecutable** |
| `pardon` | formed 8, attempted 0 (spine: 3 attempted, 3 refused) | **formed on no restraint** |
| `marshal` | eligible 26, formed 0 | **unreachable** |
| `surrender` | eligible 26, formed 0 | **unreachable** |
| `succeed` | eligible 83, formed 0 | **unreachable at this horizon** |

The per-verb sections follow in table order of the verb table. Each has the nine parts the brief orders.

### 0.1 This lane's own reading (seed 1), and what it adds to the table above

`aperture 2 1` (realm, seed 1, two seasons, `PYTHONHASHSEED=0`, control hash EQUAL;
`scratchpad/runs/VERBS_BINDING/aperture_2_1.txt`) moves three rows of the seed-0 table: `confer` and
`revoke` form for **0** persons (5 at seed 0), `determine` executes **1** (`matter.determined` 1), `release`
executes **3** (`tenure.closed` 3). Everything else holds in kind.

A per-act probe on the same world and seed (`scratchpad/runs/VERBS_BINDING/binding_probe.py`, output
`binding_probe_2_1.txt`; read-only, prints every attempted act of the family with its subject's collection
and the kinds it caused) shows *what* was attempted, which the funnel cannot:

- **`release`**: 15 refusals, every one a referent the actor owns no releasable edge toward. Persons
  release the King (`p_npc_033 → p_npc_020`, owning 4 live releasable edges, none to him); cohorts release
  the settlement they live in (`cohort_set_s_036 → set_s_036`, 7 times; `reside` and `contain` are not
  releasable). The 3 executions are cohorts laying down a held Record.
- **`establish`**: all 5 refusals are one act repeated, the Confessor founding over `b_s_014_barracks`,
  which is not among the holdings he may found over (`holdings_to_found`: False each time). An untyped
  refusal does not decay, so he re-forms it every scene.
- **`dispatch`**: 6 orders; 4 are addressed **to the King** (`p_npc_020`) by the Guard Captain, the Lord
  Treasurer, the covert Riskbreaker and the Heir; one is a duchess dispatching **herself**. Nothing the King
  then does reads any of them.
- **`issue`**: 14 writs; the King's five all have `terms` = **the King himself** (a person id, not a
  Proposition), and the Lord Steward addresses one **to the King**, admitted because the realm seat's
  purview reaches the King's residence. One writ's `terms` and `to` are the same person (`p_npc_040 →
  p_npc_004` about `p_npc_004`).
- **`determine`**: refused on a party not yet docketed (s1), on a `Rung` as party (s2, the Confessor on
  `b_s_003_market`), and on the Confessor by the Widow Regent; executed once (the Confessor on
  `p_npc_004`).
- **`pardon`**: the Cardinal of Justice pardons a man who holds no restraint on his seat (refused after
  admission).
- **`convene`**: 12 dates; one refusal is the King convening `set_s_015` through `off_king` after doing so
  through `off_duke_valorsmark` in the same tick: the date id salts actor and venue, not the seat, so the
  second seat's sitting collides with the first (a defect in `_eff_convene`, not a design choice).

The common shape: **the verbs form on referents the actor could have known were wrong**, and the acts that
execute bind nobody. Both are the brief's dead ends: a refusal the chooser could have read belongs in
formation.

---

## 1. `confer`

**1. Premise.** *A lord fills a vacant seat beneath him with a man of his choosing.* Links: a seat falls
vacant → a seat-holder whose seat reaches it learns of the vacancy → he picks a candidate he knows (or
himself) → the candidate holds the seat, with its grant → the realm hears who was seated → the new holder
acts from it.

**2. State today.** Row `remit:confer`, `referent_class: Office` (vacancies and seats he was told of),
`counterparty: to` fanned over the persons he knows plus himself, untyped (`_req_confer`: conferral basis,
conferee alive, `may_fill`, 1-per-object or displacement under T-o). Effect `_eff_confer` opens the hold,
closes any prior one, declines a banned conferee; writes `Tenure.since/until/term`; emits `tenure.opened`
(+ `tenure.closed`). Readers: WITNESS (Tenure expansion), `vacancies`, `endings_reached`, every seat-gated
verb (the grant). Reading: seed 0 formed 5, attempted 0 `[FA]`; seed 1 formed 0 (no vacancy existed).
`tenure.opened` 0 at seeds 0–2, three seasons (FA audit E-5). **Verdict: formed, never chosen.** The
mechanism is complete and correct by test; the realm makes almost no vacancies (FA F-FA-02 (a)), the
question slot rarely carries one (F-FA-02 (b), CORE's H-54), and `confer` scores below the conferrer's
other candidates because nothing in `decision/` reads a vacancy beneath his seat (F-FA-02 (c)).

**3. Build-out, decided.**
- *Occasions* (the reach problem, three producers, all already owned): seat terms on the office row
  (FA-P3 `06_FA_seat_terms_and_turnover.md`, with FA-B3's per-body terms), the recall that vacates a
  defiant seat (FA-P1 `06_FA_decree_binds.md` change 3 + `revoke`, §11 below), and the heir's claim and
  deaths (`succeed`, §12). This lane adds no fourth producer.
- *Selection*: a vacancy in the conferrer's purview is a duty of his office, which is CR-88's (B10-17b,
  duty's build). The build-out requires of CR-88 one thing, stated as its acceptance: **a vacant seat in
  the purview of a seat granting `confer` raises the conferrer's score for `confer` on it above his
  median candidate**, read through the one chooser (`decision/choose.py`), never a per-verb branch. Until
  CR-88 lands, the vacancy stays a classed referent only, as today.
- *Requirements, roll, effects*: unchanged. `confer` is uncontested by design: a conferral is an act of
  authority, not a contest; contest belongs to the elected seat's bench (CR-35) and to the displaced
  holder's later acts. No degree.
- *Refusals*: `confer.refused` on a banned conferee is a refusal the conferrer could read only if he knew
  the ban; bans are `binding_decision`-chronicled (`revoke`'s disposal, `determine`'s), so a conferrer who
  heard it can decline it person-side. Decided: **a person-side decline on a conferee his own ledger holds
  a ban claim about** (`held_against`-shaped, reading his claims, AX-2), so the refusal leaves formation
  for the informed and stays a refusal for the uninformed. FA-P3's scoping of the ban to the banning
  seat's purview applies to the same read.
- *Reason trail*: the `tenure.opened` Event cites the act; the act cites the question (the vacancy
  claim); unchanged.
- *Consequences*: the conferee's grant reaches every seat-gated verb; `establishment_of` (if he obliges
  others); `faction_q` seats; `endings_reached`.

**4. Scales and play surface.** Settlement to realm (the seat's rung, not a column: the `scale:` key is
retired when `Act.via.scope` carries it, verb table header item 1). Player: offered `confer` on each
vacancy in his purview, choosing the conferee among those he knows (and himself). NPC: the one chooser,
with CR-88's duty term.

**5. Tuning hooks.** Office row `term:` (`offices.yaml`, FA-P3); conferral basis (`offices.yaml`);
`counterparty_may_be_self` (the row); duty weight (CR-88's `score_terms` home); regard of the conferee
(`person_q.regard`, read by the chooser's alignment). No constant here.

**6. Exact edits.** `proposals/14_VERBS_BINDING_C_turnover.md` §1.

**7. Gate and falsifier.** Spine, FA-P4's `vacancy` situation (`06_FA_playable_scenario.md`): a seat is
vacated at tick 0; within two seasons a computed `confer` on it executes and a later act of the conferee
exercises the seat (`Act.via` = that seat). Control: the same run with the vacancy not stamped (revert of
IN-53's term) shows no conferral. Planted failure: delete CR-88's term; the conferral must disappear at
the realm (it would show the duty term is what moves selection).

**8. Cases.** NPC-006, NPC-009, NPC-070 (FA audit §13: seats that end and are refilled); CP-T09-06's
Widow Regent refilling Valorsmark; ARC-02 N1 (an institution's routine placement decisions must be able
to compound, `12_ARCS_adjudication.md` M-SEAT); NPC-008 N3 (a person seeking a post).

**9. NERS.** N: without it power never changes hands except by claim; the turnover loop (FA-B4) loses
its last link. R: a player shapes his court; the realm generates rises without him once terms and deaths
open seats. S: one writer of a seat-hold for appointment, `succeed` for title, CR-35 for election, each a
basis on the same gate. E (last): one act, one choice (who), outcome legible. Cut test: merge into
`succeed`? No: `succeed` is the claimant's own act on a title; `confer` is another's grant. Both stay.

---

## 2. `convene`

**1. Premise.** *A seat calls its court or council to sit at a place on a day.* Links: a matter awaits →
a seat with the remit names a venue and a date → the bench and the parties learn of it → the date
comes → the matters before it are heard (`determine`).

**2. State today.** Row `remit:convene`, `referent_class: Rung`, `requires: rank(subject.kind) >
rank(person)`; `_eff_convene` writes a Date (`due_at`, `convening_attached`, `holder` = `Act.via`);
emits `date.scheduled`; CALENDAR fires it, forms a docket slot, re-slots a waiting matter (CR-56). Seed 0:
12 formed, 12 executed `[FA]`; seed 1: 13 attempted, 12 executed, 1 refused (`binding_probe`: the seat
collision above). 17 `date.scheduled`, 12 `date.fired`, 0 `matter.determined` at seed 0, three seasons
(FA E-5). **Verdict: executes; consequence thin.** The date summons nobody directly; a judge is asked
only if he witnessed the firing first-hand (`sittings_before`), and a convening is chosen with no regard
to whether a matter awaits (CR-56's RL2 measured: the score reads the verb, never the matter).

**3. Build-out, decided.**
- *Fix the collision*: the Date id salts the exercised seat: `H(seed, tick, actor, f"convene:{via}:{venue}")`.
  Two seats of one man convening one venue are two sittings. A hash mover only where the collision
  occurs (the probe's one act at seed 1).
- *What a sitting is*: the room is SC's (`05_SC_playable_hearing_B.md`, the module's hearing entry,
  supersedes SC-P3); `convene` stays the act that puts it on the calendar. Not redone here.
- *The summons*: decided **no new carrier**. The parties docketed into the slot and the bench already
  receive the `date.scheduled`/`date.fired` claims by WITNESS (`binding_decision` → chronicle). What is
  missing is that a **party** can act on the summons: the `appear`/`defend` side is SC's hearing B moves;
  this lane requires only that `date.scheduled` carry the venue (it does) and that the docketed party's
  question carry the date (SC-P3's fixture). Cited, not rebuilt.
- *Selection*: RL5 (a matter-sensitive score term) is a Layer-1 question (`ARCHITECTURE_V2` §F2) and
  stays where CR-56 left it; CR-88's duty term is the vehicle (a matter awaiting in his purview is a duty
  of the convening seat), with the same acceptance shape as `confer`'s.
- *Refusals*: `convene.refused` now fires only on a true repeat (same seat, venue, tick, date).
- *Consequences*: CALENDAR, `open_slots`, `sittings_before` → `determine`, `interrogate`, `speak`.

**4. Scales.** Any rung above `person` (Jordan, 2026-09-05). Player: picks a venue among the tiers his
seats reach and (later, SC-P3) a date. NPC: chooser.

**5. Tuning hooks.** `docket_lapse` and the date offset (`when`, default next tick) in fixtures; the
arrangement row's `quorum`/`venue_min_rank` (`arrangements.yaml`, SC-P4 deletes the unread keys).

**6. Exact edits.** `proposals/14_VERBS_BINDING_B_sittings.md` §1.

**7. Gate and falsifier.** Seed 1 realm, two seasons: `convene.refused` 1 → 0 and `date.scheduled` 12 →
13, the extra Date holding `off_king`. Planted failure: revert the salt; the collision returns. Downstream
gate is SC's (a convened date whose slot holds a matter produces a `matter.*` Event).

**8. Cases.** M-SIT's cases (`12_ARCS_adjudication.md` mechanism row 7: ARC-04, -06, -10, -21, EMG-C4,
NSC-04, NPC-085): each needs a matter to reach a room on a date, which only `convene` makes; NPC-050 N2
(an overreaching attempt brought before a room).

**9. NERS.** N: the only producer of a sitting; without it `determine` has no room. R: a lord chooses
when and where justice is done. S: one calendar, one firing rule. E: one act, a date. Cut test: fold into
`open_case`? No: `open_case` dockets a matter; `convene` makes a room; one room hears many matters.

---

## 3. `determine`

**1. Premise.** *A bench hears a party's matter and binds him by its finding.* Links: a sitting fires
with the party on its docket → a judge on the bench is asked → the judge and the party contest → the
band decides the binding (obligation, custody, ban) or the matter is dismissed → the realm learns the
finding → the party lives under it, may discharge it, may be pardoned.

**2. State today.** Row `remit:determine`, no `referent_class` (forms on plain referents), typed five
conjuncts (`party`, `docket`, `bench`, `quorum`, `vote`), contested through `social_contest.roll`,
degree-keyed writes (`Tenure.since`, `DocketItem.matter`, `Tenure.degree`, `Person.pursuits`), emits
`matter.determined`/`pursuit.moved`/`matter.undetermined`. Seed 0: formed 8, attempted 2, refused 2 on
`docket` `[FA]`; seed 1: attempted 4, executed 1, refused 3 (`docket` 2, `party` 1). The probe: the party
refusal is a **Rung** taken as the party; one docket refusal is a man not yet docketed. **Verdict: forms
but is mostly refused; when it executes it binds.** Two structural defects beside the reach one: a
`Failure` is not an acquittal (SC-P6), and the bands share one consequence (SC-P4).

**3. Build-out, decided.**
- *Formation from the docket*: `determine` declares `referent_class: Party`, a named non-collection
  class on `Detainee`'s precedent (H-232's shape for a world fact the chooser cannot see), stamped by
  `questions_for` from `sittings_before(w, p)` — the persons on a fired sitting's docket before his
  bench. The `party` and `docket` refusals then leave formation; `bench`, `quorum` and `vote` stay
  refusals (they depend on the room's state at the fold, which the judge cannot read beforehand).
  RL2's lesson applies (narrowing on a verb-blind score can lower executions): the gate below measures
  executions, not refusals.
- *Bands*: SC-P4 (band-keyed `disposes:`) and SC-P6 (acquittal at `Failure`, `matter.dismissed`). Cited.
- *The room*: SC's hearing B (exchanges before the closing draw). Cited.
- *Requirements, roll*: unchanged, with SC's obstacle rule (task difficulty plus modifiers,
  `05_SC_obstacle_difficulty_and_modifiers_B.md`).
- *Consequences*: `oblige`/`detain`/`ban` edges (read by `confer`'s ban decline, `pardon`,
  `interrogate`, `release` for the party's own `oblige`), `pursuit.moved`, chronicle.

**4. Scales.** Settlement to realm (the venue's rung). Player: as judge, asked at a sitting; as party,
hearing B's moves. NPC: chooser for the judge's act; the party's moves are the module's.

**5. Tuning hooks.** `arrangements.yaml` (disposes, quorum), `pursuit_shift` (fixtures), SC obstacle
terms (SC-B), bench rule (`judging_set`).

**6. Exact edits.** `proposals/14_VERBS_BINDING_B_sittings.md` §2.

**7. Gate and falsifier.** Seeds 0 and 1, realm, two seasons: `determine.refused` keyed `party` and
`docket` → 0; executions ≥ today's (0 and 1). Control: the class reverted. Planted failure: stamp the
plain question referents as `Party`; refusals at `party` return.

**8. Cases.** ARC-04, ARC-10, ARC-21, ARC-31 (SC-P4/P6's citations); NPC-004, NPC-038.

**9. NERS.** N: the only act that binds a person by judgment. R: graded consequences once SC-P4 lands;
the world tries its own accused. S: one roll owner; one bench rule. E: one act; the band is legible.
Cut: none possible.

---

## 4. `dispatch`

**1. Premise.** *A lord sends one of his men somewhere on his business.* Links: the lord holds a seat →
the man is his (sworn to the seat) → the lord names a place within his purview → the man goes (or
refuses, or deserts) → what he does there is his own act.

**2. State today.** Row `remit:dispatch`, `referent_class: Person`, `requires: the named person exists`,
`writes: []`, emits `order.given`. Seed 0: formed 26, attempted 12, executed 12 `[FA]`; seed 1: 6
executed. The probe: 4 of 6 orders are addressed to the King by his own officers; one is a self-order.
91 later acts by others cite an `order.given` at seed 0, none constrained by it (FA F-FA-06). **Verdict:
executes but writes nothing; addresses anyone.**

**3. Build-out, decided.** CP-T09-08 (`proposals/2026-10-23-subsystem-completion/...-09-factions-war-diplomacy.md`
`:398-420`) is the rebuild and is adopted whole: `subject` a destination Rung inside the seat's purview,
`to` a person holding a live `oblige` to `Act.via`; the effect relocates `to` through `_relocate` under
the MUSTER basis; `order.given` stays; depends on CP-T09-07 (b) (the `oblige` clause of `may_muster`).
This lane adds two things CP-T09-08 leaves open:
- *Formation on the man's side*: `to` is fanned over `establishment_of(via)` (the seat's obligees,
  `world_q`), not over every person he knows; a man not sworn to the seat is not offered. That moves
  CP-T09-08's `dispatch.refused` for a non-obligee into formation. Self-dispatch is refused by the
  counterparty clause as for `issue`.
- *What it costs and unlocks*: the journey's leg is charged to the man (`_relocate`); his own next
  season's options are those of the place (presence is the whole binding, L1). Desertion is his `move`
  back; defiance is `evade / defy` once REM-2B's form reaches orders (FA-P1's answer formation reads
  `dispensation`; an order is not a writ, so the answer is the act, not a document).
- *Until CP-T09-08 lands*: the row keeps `writes: []` and the interim `referent_class: Person` is
  narrowed to the seat's obligees by the same fan, so no order goes up the chain. Decided (see §13,
  decision 1): **an order is addressed to the seat's own men**, by the `oblige` edge, not by purview over
  the man's place.

**4. Scales.** Person (the man) moved at territory scale (the destination within the seat's rung).
Player: chooses which sworn man and which place. NPC: chooser; the man's response is his own chooser.

**5. Tuning hooks.** `oblige` term (`oblige_term` fixture) bounds how long a man is sworn; journey legs
(world travel); the seat's purview (offices).

**6. Exact edits.** `proposals/14_VERBS_BINDING_D_orders.md` §2.

**7. Gate and falsifier.** After CP-T09-07 (b) + CP-T09-08 + this fan: a seeded realm run in which a
dispatched obligee's `contain` moves to the destination and his next act there cites the order's place
(`occasioned_by`); control: the same seed with `dispatch` withheld. Planted failure: fan `to` over known
persons again; orders to the King return.

**8. Cases.** FA §13 NPC-032 (the consort must not command), NPC-034, NPC-036; CP-T09-03's envoys.

**9. NERS.** N: the one act that moves another man by authority. R: delegation, desertion, envoys. S:
MUSTER basis shared with `march`; no second relocation body. E: one choice (who, where). Cut: merge
into `issue` (a writ ordering a journey)? No: a writ mints a document and binds by answer; `dispatch`
moves a body now. Kept.

---

## 5. `establish`

**1. Premise.** *A lord founds a new office over land he holds, or changes what an office may do.*
Links: he holds land and a seat that may found → he founds a post at that land with a remit drawn from
his own → the office exists, vacant → he or another fills it (`confer`).

**2. State today.** Row `remit:confer`, `referent_class: Rung` (shared with `migrate`, `requisition`,
`march`, `convene`), untyped (`_req_establish`, four clauses), `office_founded_by` derives the office
from `subject` and `Act.via` (CR-25). Writes `Office.exists/remit_acts`, `Tenure.payload`; emits
`office.established`/`remit.changed`/`tenure.payload_set`. Seed 0: attempted 8, executed 1, refused 7
`[FA]`; seed 1: attempted 5, refused 5, each the same act on a non-holding (probe). `office.established`
is in seed 1's never-emitted list. **Verdict: forms, mostly refused, on referents it could have read.**
Two causes: the class is shared, so places named and larders form it; a holding already founded is
still offered (the derived id lives in `loop/`, which `queries/` does not import).

**3. Build-out, decided.**
- *Formation*: `holdings_to_found` stamps each holding **also** as a named class `Holding` (in
  `questions_for`'s classed tuple, `Detainee`'s route; the `Rung` stamp stays, so the other four verbs
  do not move); `establish` declares `referent_class: Holding`.
- *Already founded*: `founded_office_id` and the post reverse lookup (`TITLE_DOMAINS` read by kind) move
  from `loop/predicates.py` to one owner `queries/` can read (`state/gate.py`, beside `founds_over`'s
  inputs, or a `data/offices.py` helper; the choice is by import graph: `state/` is imported by both).
  `holdings_to_found` then omits a holding whose derived office exists. One owner, two readers; no
  second copy of the id rule (the reason the docstring gave for not filtering is answered by moving it).
- *What follows*: the founded seat is vacant; it enters `vacancies` for the founder (who keeps `confer`,
  `FOUNDER_KEEPS`), so `establish` → `confer` is the chain. A founding is the lord's investment in
  structure; its cost is the grant he delegates (the new seat's remit is drawn from his).
- *Refusals left*: `establish.refused` on a constructor refusal (title in a body) — a fact of the seat's
  body the founder holds, so it too moves into the stamp's filter (`founds_over` already reads the seat).
- *Consequences*: new seat in `offices`, `vacancies`, `faction_q` seats, `endings_reached` if filled.

**4. Scales.** Settlement up (the holding's rung). Player: offered "found a post at X" per holding.
NPC: chooser.

**5. Tuning hooks.** `FOUNDER_KEEPS`, `FOUNDED_CONFERRAL`, `FOUNDED_REVOCATION` (today constants in
`loop/predicates.py`; moved with the id rule into the same owner and read as data from
`offices.yaml: founding` — FA-P6's "founding content as data" `06_FA_office_capabilities.md` is the
owner of that move and is cited).

**6. Exact edits.** `proposals/14_VERBS_BINDING_A_formation.md` §2.

**7. Gate and falsifier.** Seeds 0 and 1, realm, two seasons: `establish.refused` 7/5 → ≤1 each; `office.established`
≥ 1 at seed 1 or the stamp is empty for every person (then the reading is "nobody holds land he may
found over", which is content, reported, not a pass). Planted failure: drop the already-founded filter;
repeat refusals return.

**8. Cases.** SE lane's founding (`07_SE_capability_and_chooser_surface.md`); NPC-084's unauthored seat
(FA-P2).

**9. NERS.** N: the only producer of new structure. R: a lord shapes his administration. S: one office
derivation, one owner. E: one act. Cut: fold into `found` (a settlement)? No: different carrier (Office
vs Rung).
