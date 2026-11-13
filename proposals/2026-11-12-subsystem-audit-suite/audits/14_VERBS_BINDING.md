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

### 0.2 The standing rule: no governance outcome is a fixed function of state

`AUDIT_BRIEF.md`'s "Standing rule" (Jordan, 2026-11-12: *"we do not do deterministic!!!!!"*): every
consequential outcome resolves by a draw with a graded, recoverable result; state sets the odds, the
draw sets the outcome. **Today eleven of the twelve rows are deterministic** in the sense the rule
forbids: once admitted, `confer` seats, `revoke` unseats, `succeed` crowns, `pardon` frees, `establish`
founds, `surrender` cedes, `dispatch` (rebuilt by CP-T09-08) moves a man and `issue` binds, each with
certainty. Only `determine` is contested. That is a finding against the code (severity: degrades
narrative; touches R-09), and the first draft of this file repeated it (its `confer` and `issue`
sections said "uncontested by design"); those sentences are corrected below.

**Decided: every binding act whose effect could go either way for the people in the fiction is a
contested row**, rolled through the one roll owner (`social_contest.roll`, the σ-leverage d10, the
composition role `contests:` already routes `determine` to), with the obstacle composed by its one owner
(`modules/social_contest/roll.py::obstacle`, as `05_SC_obstacle_difficulty_and_modifiers_B.md` defines it:
the task's `difficulty` plus named modifiers). Admission (eligibility, the typed `requires`) stays a
check: a man cannot exercise a seat he does not hold. The pool is the actor's, through the one pool
reader (capability via the governance vocations of FA-P6 `06_FA_office_capabilities.md`, practice,
office weight). **One shape across the family**: a seat-opening act's `Partial` opens a **provisional**
hold (a `Tenure.term` of `provisional_term` seasons, matured at MATTER under `T-n`, so it lapses unless
confirmed by a later act), and every `Failure` writes nothing on the target and emits a kind of its own,
leaving the act re-attemptable (recoverable, never a dead end).

| verb | prize (new rows marked +) | counterparty (opposition) | obstacle terms beyond `difficulty` | O / S | P | F |
|---|---|---|---|---|---|---|
| `confer` | + `a seat` | the incumbent, when displacing | `reception` (the seat's body toward the conferee), `standing` +, `stakes` (`hold`) | seated (row's term) | seated, provisional term | not seated; `appointment.resisted` |
| `revoke` | `a seat` | the holder | `regard`, `standing`, `stakes` (`hold`), `reception` (the seat's body) | unseated + disposal | unseated, no disposal | holds; `revocation.resisted` |
| `succeed` | `a seat` | none (rival claims fight by other verbs) | `reception` (the seat's body/realm toward the claimant), `standing` | seats taken, title laid down | seats taken provisionally, title kept | claim fails this season; `succession.contested` |
| `pardon` | `a matter` | none | `stakes` (the restraint kind), `standard` (the disposing arrangement), `reception` (the bench) | every restraint on the seat ends | `detain` ends, `ban` stands (commutation) | stands; `pardon.denied` |
| `establish` | `a seat` | none | `reception` (the holding's seated persons), `standing` | founded, full derived remit | founded, remit = first half of the derived acts in authored order | nothing; `office.unrecognised` |
| `surrender` | + `a holding` | none | `reception` (the place's residents toward the receiver's faction) | ceded | ceded provisionally (receiver's hold termed) | the place will not yield; `surrender.rejected` |
| `issue` | + `an order` | `to` | `regard`, `standing` | writ minted, `force` = band | writ minted, `force` Partial | writ minted, `force` Failure (a dead letter: no answer forms) |
| `dispatch` | `an order` | `to` | `regard`, `standing` | relocated | relocated, `order.grudged` | stays; `order.refused` |
| `determine` | `a proposition` (today) | the party | SC's | unchanged | unchanged | SC-P6's acquittal |

`standing` is the one term this family adds to SC's closed roster `obstacle_terms`: the counterparty's
(or, for an act on the actor's own behalf, the audience's) rank against the exercised seat, read off
`rosters.yaml: rung_kinds`' order through the gate's rank reader, times a fixture `standing_step`
(control 0). It is listed in `14_VERBS_BINDING_C_turnover.md` as a cross-lane request to the SC
obstacle's owner, not edited there. `reception` gains an *audience* operand (the bench today; the seat's
body, a holding's seated persons or a place's residents here), the same reader with a different set of
persons. **The answers to a writ** (`comply`, `evade / defy`, `construe`) are the addressee's choices
and their rows are FA's; this family only writes the writ's `force` band onto the Record so that their
odds can read it (a cross-lane item, named in `14_VERBS_BINDING_D_orders.md`).

**Three rows stay uncontested, each for a reason the rule itself admits**: `convene` writes a date (a
clock; whether the room then decides is `determine`'s draw and SC's hearing); `release` closes the
actor's own edge (a man's renunciation of his own tie cannot fail in the fiction; what others make of it
is the witnesses' regard); `marshal` writes a standing order on paper (whether the troops follow it is
the field's draw, MB's). If the orchestrator judges any of the three to be an outcome that could go
either way, it takes the same shape as the table above.

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
- *Roll and effects by degree* (§0.2): `confer` becomes contested (prize `a seat`), so an appointment
  can fail to take. Pool: the conferrer's (office weight, the governance vocation). Obstacle:
  `difficulty` `routine`, `reception` of the seat's body toward the conferee, `standing` (a low man
  raised high is harder), `stakes` `hold`, and `opposition` the incumbent when the act displaces him.
  Overwhelming/Success seat him (with the row's term, FA-P3); Partial seats him provisionally
  (`provisional_term`); Failure seats nobody and emits `appointment.resisted`, re-attemptable. The
  elected seat's bench (CR-35) is a different act and stays so.
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
- *Roll* (§0.2): an order obeyed is a draw, not an effect. Contested, prize `an order`, opponent `to`
  (his score, `regard` toward the lord, `standing`). Overwhelming/Success: relocated; Partial: relocated
  and `order.grudged` (witnesses read a grudging obedience); Failure: he stays, `order.refused`, his
  `oblige` intact, the lord's next act his to choose (revoke, case, release him).
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
- *Roll* (§0.2): contested, prize `a seat`, no person opponent; obstacle `difficulty` `demanding`,
  `reception` of the holding's seated persons, `standing`. Overwhelming/Success: founded with the full
  derived remit; Partial: founded with the first half of the derived remit acts in authored order (a
  later `establish` on the existing id re-remits it, clause 4's arm) `[ASSUMPTION; medium; revert: Partial
  founds in full]`; Failure: `office.unrecognised`, nothing written.
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

---

## 6. `issue`

**1. Premise.** *A seat issues a written order to men under it, who must obey, evade or answer for it.*
Links: the issuer holds a seat → he names what is ordered (a proposition: "X ought to be done") and whom
it binds (executors under him) → the writ exists and is proclaimed → each addressee learns its terms →
each answers by his own act (`comply`, `evade / defy`, `construe`) → the issuer learns the answers →
defiance is his occasion (recall, case, arrest).

**2. State today.** Row `remit:issue`, typed three conjuncts (`executors`: `to` a Person; `authority`:
the seat's purview reaches `to`; `terms`: `own_ledger` of `subject`), `counterparty: to` fanned over
known persons, writes `Record.exists` (a `dispensation` minted into the maker's hand), emits
`dispensation.issued`. Seed 0: attempted 26, executed 19, refused 7 on `authority` `[FA]`; seed 1:
15/14/1. 29, 21, 41 writs over three seasons at seeds 0–2; 0 held by an addressee; 0 answers (FA F-FA-01).
The probe adds: `terms` is a **person id** in most writs (the King's five name the King), and a
subordinate can address the King. **Verdict: executes; binds nobody; orders nothing.**

**3. Build-out, decided.**
- *Reach and answer*: FA-P1 (`06_FA_decree_binds.md`) is adopted whole: the terms of a proclaimed writ
  reach its addressees as a content claim; `comply`/`evade / defy`/`construe` form on a writ the
  addressee's own ledger names him addressee of; the issuer's folded suspicion carries a defiant
  subordinate's seats as the recall referent. The proclaimed-or-delivered choice stays the FA audit's §11
  item 1 for Jordan.
- *What a writ orders*: `issue` declares `referent_class: Proposition`, so `subject` (the terms) is
  always a Proposition; the `terms` conjunct stays `own_ledger`. The stamp today (`propositions_heard`)
  carries only Propositions he heard from *another* (`Claim.doer != p.id`), which would leave out the
  most natural writ: the OUGHT he himself committed to. So the Proposition stamp gains his ambitions
  (`world_q.ambitions`, the one owner of the live-`commit`-to-an-OUGHT rule), a declared widening for
  every row declaring the class (`argue` gains them; `commit` does not, `held_edge_declines`). This is the
  smallest edit that stops a writ ordering a person. Which Propositions are orders (a stores demand, an
  installation, a cession) is F-FA-18 / R-27's design-first item and stays there: a writ's terms are what
  the issuer holds ought to be, and the answer verbs read them.
- *Whom it binds*: `authority` reads purview over the executor's place today, which admits an order up
  the chain. Decided, as `dispatch`'s: **an executor is a person sworn to, or seated beneath, the issuing
  seat** — a new basis value `command` in `state/gate.py` (one predicate: `to` holds a live `oblige` to
  `via`, or holds a seat whose revocation `may_revoke` grants to `via`, or lives within `via`'s purview
  and holds no seat). `[ASSUMPTION; medium; Jordan to correct; revert: basis `purview`]`. It is §13
  decision 1.
- *Formation*: the fan over `to` filters by the same predicate person-side where it can (his own seats'
  obligees and the persons his ledger seats beneath him); what he cannot read stays the
  `issue.unauthorized` refusal.
- *Degree* (§0.2): `issue` becomes contested (prize `an order`, opponent `to`), because whether a
  decree takes hold could go either way. The paper is minted at every band (bookkeeping); the band is
  written onto it as its `force`. Failure is a dead letter (the addressee hears of it, no answer forms);
  Partial binds loosely; Success and Overwhelming bind. The answers' odds read `force` (FA's rows; a
  cross-lane item). The issuer's response to defiance (`revoke`, `open_case` → `determine`) is itself
  drawn.
- *Consequences*: answers (FA-P1), recall (`revoke`), cases (`open_case`), `comply`'s performing acts
  (`terms_sourced`), chronicle.

**4. Scales.** The issuing seat's rung (province by the retired key). Player: chooses terms (a
Proposition he holds) and addressees among his men; is offered answers when addressed. NPC: chooser.

**5. Tuning hooks.** FA-P1's suspicion threshold (its home); the `command` basis (`state/gate.py`,
reading `offices.yaml` revocation bases); `terms_sourced` (rosters).

**6. Exact edits.** `proposals/14_VERBS_BINDING_D_orders.md` §1.

**7. Gate and falsifier.** FA-P1's gate (an addressee's answer executes; the issuer's later act cites
it), plus: seeds 0 and 1, realm, two seasons, **0 writs whose `terms` is not a Proposition** and **0
writs addressed to a person the issuing seat does not command**. Control: class and basis reverted (the
probe's figures: 5+ person-terms, 1 writ to the King). Planted failure: revert the class; person-terms
return.

**8. Cases.** NPC-083 (a governor's limited orders), NPC-038, ARC-17 (FA-P1's citations); NPC-008 N1
(a bureaucrat acting through his post); M-ABROAD (ARC-38 N2, NPC-089 N6: a superior who recalls).

**9. NERS.** N: the act of authority over men; without it there is no command loop (FA-B4's first link).
R: obedience, evasion, construal and recall are four games, and the realm runs them unwatched. S:
answers read the same Record; one mint. E: one act (what, to whom); the answers carry the drama. Cut:
merge `covenant` into `issue`? No: the covenant row keeps its terms private by design.

---

## 7. `marshal`

**1. Premise.** *A commander sets his army's order of battle for the field at a place: what role it
takes and when it falls back.* Links: a seat that may muster → a place where his side will fight → he
issues a standing order → the field reads the newest order when it is fought.

**2. State today.** Row `remit:dispatch`, `referent_class: Rung`, typed `authority` (purview), writes
`Record.exists` (`order_of_battle`), emits `order.marshaled`; `role`/`retreat_at` ranged by
`choice_sourced`. **Withheld** (`data/fixtures.py:1157`, `withheld_verbs`), so eligible 26, formed 0.
`field_input` reads the order; fields fought: 0 at seed 0 (PHYSICAL §0.3: `march` executes only
unopposed). **Verdict: unreachable (withheld), and its reader has no field to read it at.**

**3. Build-out, decided.**
- *Precondition of use*: a field is fought. That is PHYSICAL batch P-B
  (`14_VERBS_PHYSICAL_B_field_and_ruin.md`, `march` meeting a defender) and MB's field scenario;
  `marshal` cannot be judged before it.
- *Who may*: FA-P2 (remit by row: only seats whose row names `dispatch`) and FA-B2 (levy through the
  seat) bound eligibility to commanding seats. Cited.
- *Formation*: the shared Rung class offers every known place. Decided: **`marshal` forms only on a
  place where his side may fight** — a named class `Front`, stamped by `questions_for` from his own
  ledger: a place his faction holds that a `march.declared` claim names as a target, or a place a
  `march.declared` claim names as his faction's target (person-side, AX-2). An order for a place no field
  will be fought at is a Record nobody reads.
- *Effect*: unchanged (one Record per order; the newest wins at `field_input`).
- *Unwithhold*: a separate declared mover, after P-B, with the gate below.
- *Consequences*: `field_input` (MB), the field's degree, `field.won`/`field.lost`, casualties.

**4. Scales.** Settlement where the field is; the seat's faction. Player: picks role and retreat
threshold (closed sets). NPC: chooser over `choice_sourced`.

**5. Tuning hooks.** `order_roles`, `order_retreat_at` (rosters), MB's `ROLE_SPEC` (module).

**6. Exact edits.** `proposals/14_VERBS_BINDING_E_war_seats.md` §1.

**7. Gate and falsifier.** After P-B and the unwithhold: a seeded realm run where a field is fought and
`field_input` reads an `order_of_battle` for at least one side; the same seed with that order's `role`
flipped (planted) changes the field's degree or casualties. Control: `marshal` withheld (today).

**8. Cases.** NPC-036 N4, NPC-072 N3 (named command posts); MB's field scenario
(`04_MB_playable_field_scenario.md`).

**9. NERS.** N: without it a commander has no decision at the field scale beyond whether to march. R:
role and retreat give a field tactics a person chose. S: the order is a Record the field reads; no second
parameter channel. E: two closed choices. Cut: fold into `march` as payload? Defensible, at the cost that
the defender (who does not march) could set no order; kept separate.

---

## 8. `surrender`

**1. Premise.** *A lord whose town is besieged yields it to the besieger rather than fight.* Links: an
enemy presses a siege on a place his faction holds → he learns of it → he chooses to yield → the place
passes without a field → the realm hears it.

**2. State today.** Row `remit:dispatch`, `referent_class: Rung`, typed `authority`, effect
`_eff_surrender` (a held settlement, `siege.pressed` this season, a receiver of another faction,
`may_cede`), writes `Tenure.since`/`until`, emits `place.surrendered`. **Withheld**. `siege.pressed` is
never emitted (PHYSICAL §0.3; `raze` refused 14 of 14 after admission). **Verdict: unreachable twice
over: withheld, and its occasion is never produced.**

**3. Build-out, decided.**
- *Occasion*: `siege.pressed` is PHYSICAL P-B's. Cited.
- *Formation*: decided, **a named class `Besieged`**, stamped from his own ledger: a `siege.pressed`
  claim of this season naming a place within his seat's purview (person-side). The faction-match test
  stays the effect's `may_cede`, the cost the row's note already states. The no-siege refusal leaves
  formation.
- *Terms*: the row cedes the place outright. A surrender on terms (garrison leaves, stores kept) is the
  covenant route (`covenant` + `give`), not this row; recorded, not built.
- *Roll* (§0.2): contested, prize `a holding` (new), no person opponent; obstacle `difficulty`,
  `reception` of the place's residents toward the receiver's faction. Overwhelming/Success: ceded;
  Partial: ceded provisionally (the receiver's hold termed); Failure: `surrender.rejected`, the town
  will not yield and the field goes ahead.
- *Unwithhold*: a declared mover after P-B.
- *Consequences*: `holder_faction_of`; pending marches resolve `Unopposed`; chronicle; FA-B1 (a yielded
  town is a war cost the waging seats read).

**4. Scales.** Settlement; faction. Player: yield or not, when a siege presses his town. NPC: chooser
(alignment cells; no special term).

**5. Tuning hooks.** The chooser's alignment cells for `surrender` (`rosters.yaml: alignment`); nothing
new.

**6. Exact edits.** `proposals/14_VERBS_BINDING_E_war_seats.md` §2.

**7. Gate and falsifier.** After P-B: a seeded run in which a `siege.pressed` is followed in the same or
the next season by a `place.surrendered` or a fought field at that place, and `holder_faction_of` reads
the receiver after a surrender. Planted failure: stamp every known Rung as `Besieged`; refusals return.

**8. Cases.** ARC-13 N1 (a faction's default defensive behaviour), ARC-24 N2; EMG-X5 (a brittle peace).

**9. NERS.** N: the only bloodless transfer under arms; without it every siege is a battle or a ruin. R:
a lord weighs honour against lives. S: `may_cede` on the one gate. E: one yes/no. Cut: fold into `give`
+ Rung? No: `give` is unthreatened and consensual; a surrender reads a threat.

---

## 9. `pardon`

**1. Premise.** *A bench frees a man it holds in custody, or lifts a ban it laid.* Links: a man is
restrained on a seat → a judge of that seat's bench is moved to mercy → the restraint ends → the man and
the realm learn it.

**2. State today.** Row `remit:determine`, typed (`existence` Person, `basis` bench), effect closes every
live `detain`/`ban` the subject owns on `Act.via`, emits `detention.ended`/`ban.ended`. Seed 0: formed
8, attempted 0 `[FA]`; seed 1 realm: 1 attempted, refused after admission (the probe: a man restrained
nowhere); spine seed 1: 5 refused. **Verdict: formed on no restraint.** It forms on every person a
question names.

**3. Build-out, decided.**
- *Formation*: `pardon` declares `referent_class: Restrained`, a named class stamped by a sibling of
  `detainees_held`, `restrained_on_seats(w, p)`: every living person with a live `detain` **or** `ban`
  whose object is a seat `p` holds granting `determine`. `Detainee` stays `detain`-only for
  `interrogate`. `world_q.restrained` stays the one owner of what a restraint is; the new term composes it.
- *Occasion and choice*: mercy is the bench's; the chooser weighs it by regard and pursuits (the
  alignment cells for `pardon`). Nothing is written for the pardoner; the chronicled act's regard is its
  cost and its gain.
- *Roll* (§0.2): contested, prize `a matter`; obstacle `difficulty`, `stakes` (the restraint's kind),
  `standard` (the disposing arrangement), `reception` (the bench). Overwhelming/Success: every restraint
  on the seat ends; Partial: commutation (the `detain` ends, a `ban` stands); Failure: `pardon.denied`,
  the restraint stands, re-attemptable.
- *Consequences*: a lifted ban re-opens `confer` and `oblige` to the man; `interrogate` loses its
  referent; `capture`/`arrest` may recur.

**4. Scales.** Settlement up (the seat's rung). Player: offered "pardon X" for each prisoner or exile of
his bench. NPC: chooser.

**5. Tuning hooks.** Alignment cells (`rosters.yaml`); regard (`person_q`).

**6. Exact edits.** `proposals/14_VERBS_BINDING_B_sittings.md` §3.

**7. Gate and falsifier.** Seeds 0 and 1 realm: `pardon` formed → 0 persons and `pardon.refused` → 0
while the stamp is empty; with a hand-planted `detain` (the `interrogate` tests' fixture) a computed
`pardon` forms and, chosen, emits `detention.ended`. Planted failure: widen the stamp to every person;
refusals return.

**8. Cases.** ARC-10 (fully reversing a punishment, SC-P4's citation); NPC-041 N2.

**9. NERS.** N: the only end of a restraint short of death. R: mercy is a political act. S: the gate's
`determination` basis, shared with `determine`. E: one act. Cut: fold into `release`? No: a prisoner may
not end his own custody (`RELEASABLE_KINDS`); a pardon is another's closure.

---

## 10. `release`

**1. Premise.** *A man lets go of what binds him: resigns his seat, renounces a vow, ends a service,
lays down a thing he holds.* Links: he holds a live tie → news about it makes it a burden → he ends it →
those who watch learn it; a broken vow costs regard.

**2. State today.** Row `own`, untyped (`_req_release`: a live releasable edge he owns toward the
subject), `domain: [hold, commit, oblige, succeed, tie, knot]`, writes `Tenure.until`, emits
`tenure.closed`/`commitment.ended`. Seed 0: formed 83, attempted 15, executed 0 `[FA]`; seed 1: 18/3/15.
The probe: every refusal is a referent he holds no releasable edge toward (the King; his own
settlement). **Verdict: forms on referents it could have read; executes only by accident.**

**3. Build-out, decided.**
- *Formation*: a new person-side decline, `own_edge_declines` (`own_hold_declines`' shape, one carrier
  over): a listed verb forms only on a referent that is the object of one of his own live Tenures whose
  kind is in **the row's own `domain:`**. Reading the row's column keeps one owner of what `release`
  closes; the loader refuses a member with no `domain:` or not `own`-eligible.
- *No widening*: it narrows the plain referents. The occasion of a release is a question about the thing
  he is tied to (news about his cause, his seat, his lord): he reconsiders a tie when something about it
  reaches him, which is the plain meaning.
- *Effects*: unchanged; the vow-break's price is `release`'s alignment cells (the hole register's own
  record of it).
- *Consequences*: resignation vacates a seat (`vacancies` → `confer`, `succeed`); a broken `commit`
  changes the de facto share of a war (FA-B1); an ended `oblige` shrinks `establishment_of`.

**4. Scales.** Person; the tie's object may sit at any scale. Player: offered "renounce / resign /
leave X" for each tie the question touches. NPC: chooser.

**5. Tuning hooks.** Alignment cells (rosters); `oblige_term` (fixtures).

**6. Exact edits.** `proposals/14_VERBS_BINDING_A_formation.md` §1.

**7. Gate and falsifier.** Seeds 0 and 1 realm, two seasons: `release.refused` 15/15 → 0 (every refusal
today is a formation miss); executions not below today's (0/3). Planted failure: add `reside` to the
domain the decline reads; the cohorts' refusals on their home return.

**8. Cases.** NPC-031 N3 (an heir's alignment locks in or breaks), EMG-X5 N2 (an agreement's hidden
fragility), FA-B1's peace by release of the war commitment.

**9. NERS.** N: the one closer of a person's own ties; without it no resignation, apostasy or
desertion of a cause. R: the realm's commitments decay by choice. S: one closer for six kinds. E: one
act. Cut: none.

---

## 11. `revoke`

**1. Premise.** *A superior strips a man of his seat.* Links: a seat above holds revocation authority →
the holder has failed, defied or become a threat → the superior revokes → the seat falls vacant (an
appointee is barred from the revoking seat) → the realm hears it → the seat is refilled.

**2. State today.** Row `remit:revoke`, `referent_class: Office`, untyped (`_req_revoke`: payload
`office` names a seat with a disposal, `may_revoke`, a live hold), effect closes the hold and, for an
`appointed` seat, opens `ban : him → via`. Seed 0: formed 5, attempted 0 `[FA]`; seed 1: formed 0.
**Predicate and effect read `payload["office"]`, which a computed act never carries** (it binds
`subject`; `loop/effects_governance.py:333-334`, `loop/predicates.py`'s `_req_revoke`), so a computed
`revoke` is refused at clause 1 by construction (FA-P1 change 4). **Verdict: formed, unexecutable.**

**3. Build-out, decided.**
- *Read the seat from `subject`*: `_req_revoke` and `_eff_revoke` read it through `office_named_by(a)`,
  `confer`'s reader. FA-P1 change 4, adopted.
- *Occasion*: FA-P1 change 3 (the recall referent from folded defiance) and CR-35/CR-36's removal for
  elected seats. The seven seats nobody can strip (`revocation: null`) are the FA audit's §11 item 3.
- *Formation*: the Office stamp today offers vacant seats too (`vacancies`); a revoke of a vacant seat
  is a refusal the actor could read from the same stamp. Decided: **`revoke` forms only on a seat his own
  ledger says is held** (the newest claim naming the seat is a `tenure.opened` or `succession.claimed`),
  a person-side filter on the stamp, `own_title_declines`' route.
- *Roll and effects by degree* (§0.2): contested, prize `a seat`, opponent the holder (his score,
  `regard`, `standing`, `stakes` `hold`, `reception` of the seat's body). Overwhelming/Success: the hold
  closes and IN-31's disposal applies; Partial: the hold closes with no disposal; Failure: he keeps the
  seat, `revocation.resisted`, and the revoker may try again or go to a bench.
- *Consequences*: vacancy → `confer`/`succeed`; ban → `confer`'s decline, `pardon`; chronicle; the
  revoked man's grudge (stance rows).

**4. Scales.** Settlement up. Player: offered "strip X of Y" for subordinate seats he knows are held.
NPC: chooser, with FA-P1's recall referent as the occasion.

**5. Tuning hooks.** `REVOCATION_DISPOSAL` (`state/gate.py`, Jordan-ruled); revocation bases
(`offices.yaml`); FA-P1's suspicion threshold.

**6. Exact edits.** `proposals/14_VERBS_BINDING_C_turnover.md` §2.

**7. Gate and falsifier.** FA-B4's `recall` scenario: the Count withholds; the Duke's computed `revoke`
executes; `tenure.closed` on the Count's seat; the Count's later options are an unseated man's. Planted
failure: revert the `subject` read; `revoke` is refused at clause 1 again.

**8. Cases.** NPC-038 N1 (removal on exposure), ARC-29 N1–N2 (a head of state removed), NPC-070,
NPC-004 (FA §11 item 3's).

**9. NERS.** N: the only removal short of death; the defiance loop needs it. R: purges and disgrace. S:
`confer`'s mirror on one gate. E: one act. Cut: none.

---

## 12. `succeed`

**1. Premise.** *When the throne falls vacant, the heir claims it by his title.* Links: a seat with a
succession falls vacant (death, abdication, revocation) → the holder of its title learns of it → he
claims → he holds the seat(s) and lays down the title → the realm hears it.

**2. State today.** Row `own`, `referent_class: Office` narrowed by `own_title_declines`, untyped
(`_req_succeed` → `may_claim`), effect opens every seat the title claims and closes the title, emits
`succession.claimed`/`tenure.closed`. `successions` has **one row** (`off_king → off_heir`). Seeds 0 and
1: formed 0 (the King lives); 0 in 9 heir-seasons (CHAR F-CHAR-01, H-289; `12_ARCS` M-SEAT row).
`engine/season/tests/test_in61_heir_hears_vacancy.py` executes the chain on a hand-built death.
**Verdict: works when its occasion exists; unreachable at the realm horizon; the law has one row.**

**3. Build-out, decided.**
- *Occasion*: vacancies of succession seats come from death, `release` (abdication, §10) and `revoke`
  (§11). No new producer.
- *Law*: `successions` is content. Decided: **every seat whose `conferral` is `inheritance` must have a
  `successions` row, checked at load** (the roster's own check gains a totality clause), so a hereditary
  seat without an heir title cannot ship. Authoring further rows (the ducal heirs; CP-T09-06's
  Valorsmark) is content.
- *Contest*: SCN-12 and NPC-081 need a contested succession. For elected seats that is CR-35; for
  hereditary seats a rival claim is fought by the verbs around it (`argue` before a bench, `march`).
  No second claim rule; but no claim wins by order either (§0.2): the claim is contested (prize `a
  seat`, no person opponent; `reception` of the seat's body or the realm's seated persons toward the
  claimant, `standing`). Overwhelming/Success: the seats open and the title is laid down; Partial: the
  seats open provisionally (`provisional_term`) and the title is kept, so a failed confirmation leaves
  him heir; Failure: `succession.contested`, nothing written, and a rival's act may come first.
- *Formation*: the title narrowing re-forms the claim while the King sits (the row's own note). Decided:
  **the claim forms only while his newest claim about the seat is a `tenure.closed`** (he believes it
  vacant), the same ledger read as `revoke`'s filter, inverted.
- *Consequences*: the new holder's grant; `endings_reached`; FA-B1 (the war passes to his decision).

**4. Scales.** A person taking a realm or duchy seat. Player: as heir, offered "claim the throne" when
he believes it vacant. NPC: chooser.

**5. Tuning hooks.** `successions` (rosters); conferral bases (offices).

**6. Exact edits.** `proposals/14_VERBS_BINDING_C_turnover.md` §3.

**7. Gate and falsifier.** FA-P4's `succession` situation on the spine (the Sovereign dies at tick 0):
`succession.claimed` within two seasons; control: the heir title unheld (no claim). The load clause:
plant an `inheritance` seat with no row; the load fails.

**8. Cases.** SCN-12 N1, NPC-081 N1–N2, NPC-031, ARC-29.

**9. NERS.** N: the only hereditary transfer. R: a death becomes a story. S: the claim basis on the one
gate. E: one act. Cut: fold into `confer` (self-conferral)? No, and measured (the row's note: a second
emitter of `tenure.opened` re-weighs every such claim).

---

## 13. The family's order

### 13.1 Dependency graph (within the family)

```
release ─────────────► succeed (abdication is a vacancy)      [A]
establish ───────────► confer (a founded seat is vacant)      [A → C]
convene ─► determine ─► pardon (a bench's restraint)          [B]
issue (FA-P1 answers) ─► revoke (recall) ─► confer / succeed   [D → C]
dispatch (CP-T09-08)                                           [D]
marshal, surrender (after PHYSICAL P-B)                        [E]
```

### 13.2 Cross-family and cross-lane dependencies

- **CORE**: H-54 (the question slot) and CR-88 (duty in the chooser) decide whether `confer`,
  `convene`, `revoke` are *chosen*; this family makes them *formable and executable*.
- **SC**: SC-P4 (band-keyed disposal), SC-P6 (acquittal), hearing B (the room) for `determine`;
  `05_SC_obstacle_difficulty_and_modifiers_B.md` for its obstacle.
- **FA**: FA-P1 (decree), FA-P2 (remit by row), FA-P3/FA-B3 (terms), FA-B1 (war in seats), FA-B2
  (levy), FA-B4 (the recall scenario, the gate for C and D), FA-P4 (the scenarios), FA-P6 (founding
  content as data), CP-T09-06, -07 (b), -08, CR-35, CR-36.
- **PHYSICAL**: P-B (fields fought, `siege.pressed`) before batch E.
- **MB**: `field_input` reads `marshal`'s Record.

### 13.3 Landing order, in batches

| batch | verbs | proposal | depends on | gate |
|---|---|---|---|---|
| A | `release`, `establish` | `14_VERBS_BINDING_A_formation.md` | nothing | seeds 0, 1, realm, two seasons: both rows' refusals → ≤1, executions not lower; hash a declared mover |
| B | `convene`, `determine`, `pardon` | `14_VERBS_BINDING_B_sittings.md` | SC-P6, SC-P4 (for `determine`'s bands; the formation edits do not wait) | `convene.refused` collision gone; `determine` refusals at `party`/`docket` → 0; `pardon` formed only on a restraint |
| D | `issue`, `dispatch` | `14_VERBS_BINDING_D_orders.md` | FA-P1; CP-T09-07 (b), CP-T09-08 for `dispatch`'s relocation | 0 person-terms, 0 orders up the chain; FA-P1's answer gate |
| C | `confer`, `revoke`, `succeed` | `14_VERBS_BINDING_C_turnover.md` | D (the recall), FA-P3, CR-88 for selection | FA-B4 `recall` and FA-P4 `succession` scenarios close their links |
| E | `marshal`, `surrender` | `14_VERBS_BINDING_E_war_seats.md` | PHYSICAL P-B, FA-P2, FA-B2 | a fought field reads an order; a siege is followed by a surrender or a field |

### 13.4 Decisions that survive to Jordan

Each was put through `CLAUDE.md` §0's five steps; the ones answered there are decided in the sections
above and listed in the proposals with their reverts.

1. **Does an order run up the chain?** `issue`'s and `dispatch`'s authority is purview over the
   addressee's *place* (ruled, ED-IN-0256 (4)); read literally, any seat whose rung contains the King's
   residence may order the King.
   - *(A) Territorial authority (today).* A seat orders whoever stands in its land. Officers of the
     realm seat can order the King; an order's force comes from where it is given. Cheap, legible, and
     the King's officers command him in his own city.
   - *(B) Command authority (proposed).* A seat orders its sworn men (`oblige`) and the holders of the
     seats it may revoke, and the unseated within its purview. Orders run down the chain; a writ to a
     superior is a petition, not a command.
   The proposals take (B) behind its revert; it narrows a ruled basis for these two verbs only, so it is
   Jordan's.
2. Carried, not re-decided: the FA audit's §11 items 1 (proclaimed or delivered decree), 3 (seats nobody
   can strip) and addendum §B6.2 item 1 (whose word ends a war); each binds batch D, C or E.

### 13.5 Fan-out

This completion was written by one agent; no subagent was spawned. The judgment nodes (decision 1, the
named classes) are listed for the orchestrator's critic.
