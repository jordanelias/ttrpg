# VERBS · PHYSICAL — build-out of the nine `contested_physical` rows

## Status: REFERENCE (a verb build-out audit; resolves nothing at runtime, CLAUDE.md §0.05)

Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12).

## Read at: 84d2a02 (working tree; implementation lane A's duel-chain edits not yet merged, see §0.2)

Work order: `VERBS_BRIEF.md`, FAMILY = PHYSICAL. Verbs: `arrest`, `fight`, `capture`, `accept`, `march`,
`raze`, `examine`, `surveil`, `thread_read` (the nine rows of `engine/season/verb_table.yaml` whose
`stratum:` is `contested_physical`). The exact edits are in the four proposals named in §0.4; this file
holds the premise, the state today with its reading, the decided build-out, and the family's order.

## 0. Verdict and reading

### 0.1 Verdict

**None of the nine works as its plain meaning promises, and none is a stub.** Every one has a row, an
effect or a route, and a test that passes on a hand-built world; what fails is reach and consequence. At
`aperture 2 0` (realm, seed 0, two seasons, `PYTHONHASHSEED=0`, control hash EQUAL) the family made 113
attempts and produced, in total, three unopposed arrivals and six `surveil` findings that taught nobody
anything. The single largest obstacle is the same for seven of the nine: **the act forms on a referent,
or in a state, that the fold must refuse for a reason the actor could have read** (a Record that is no
challenge, a place his army does not stand in, a person who is not where he is, a hearth that is no
field). The other two (`surveil`, `thread_read`) execute and carry no product.

### 0.2 What this is read against

- HEAD `84d2a02`. Implementation lane A (`IMPLEMENTATION_BRIEF_A.md`) is landing
  `proposals/03_PC_duel_chain_reach.md` in a worktree; at the time of this reading its branch carried no
  commit, so every figure here is the **baseline** that lane moves. Where a build-out below depends on
  lane A's result it says so and does not restate that proposal's edits.
- One seeded instrument reading per verb, as the brief asks: `aperture 2 0`
  (`scratchpad/runs/VERBS_PHYSICAL/aperture_2_0.txt`) and `corpus_run`
  (`scratchpad/runs/VERBS_PHYSICAL/corpus_run.txt`). A second seed is quoted from the lane audits where
  they ran one (`audits/03_PC_audit.md` E7b; `audits/04_MB_audit.md` F-MB-03). One seed is a reading of a
  trajectory, not a rate (CLAUDE.md §0.1 pt 4); nothing below is a balance claim.

### 0.3 State today, one line per verb

`elig` = persons eligible at build (seated / unseated); `formed` = persons who formed it; `att / ex / ref`
= acts attempted, acts that emitted a declared `emits:` kind, acts that emitted a refusal kind (`ex`
counts a `finding.none` and a `march.declared`, so read `ex − both`). Realm arm.

| verb | elig | formed | att | ex − both | ref | deciding read of the refusals | verdict |
|---|---|---|---|---|---|---|---|
| `arrest` | 26 / 0 | 1 | 0 | 0 | 0 | — | **forms almost never; never attempted** (`arrest.made` is in the never-emitted list) |
| `fight` | 33 / 50 | 0 | 0 | 0 | 0 | — | **unreachable** (no `violence_contexts` reader names anybody) |
| `capture` | 26 / 0 | 26 | 12 | 0 | 12 | `with=False` 7 · `exists:Person=0` 3 · `individual=False` 2 | **forms but is refused** |
| `accept` | 33 / 50 | 37 | 27 | 0 | 27 | `exists:challenge=0` 27 | **forms but is refused** (lane A's target) |
| `march` | 26 / 0 | 26 | 13 | 3 | 10 | `no-read` 10 (ENCOUNTER: the target is no field) | **executes only unopposed**; 0 fields fought |
| `raze` | 26 / 0 | 26 | 14 | 0 | 14 | post-admission 14 of 14 (the effect: no occupation) | **forms but is refused** |
| `examine` | 33 / 50 | 1 | 0 | 0 | 0 | — | **unreachable** (its `site` operand is never a Site) |
| `surveil` | 33 / 50 | 83 | 44 | 6 | 38 | graded loss 16 · `present_at=False` 15 · `exists:Rung=0` 7 | **executes and finds nothing** |
| `thread_read` | 33 / 50 | 4 | 3 | 3 | 0 | — | **executes and finds nothing** (ungraded; no finding terms) |

Never emitted in this run, of the family's declared kinds: `arrest.made`, `arrest.resisted`,
`arrest.refused`, `arrest.unauthorized`, `fight.declared`, `kill.refused`, `contest.undecided`,
`capture.declared`, `person.captured`, `accept.declared`, `duel.yielded`, `field.won`, `field.lost`,
`siege.pressed`, `rung.razed`, `person.died`, `tenure.closed`, `capability.raised`. Death census: 0.

### 0.4 The proposals that carry the edits

| file | verbs | batch |
|---|---|---|
| `proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` | `arrest`, `capture`, `fight`, `accept` | P-A |
| `proposals/14_VERBS_PHYSICAL_B_field_and_ruin.md` | `march`, `raze` | P-B |
| `proposals/14_VERBS_PHYSICAL_C_looking.md` | `examine`, `surveil` | P-C |
| `proposals/14_VERBS_PHYSICAL_D_thread_read.md` | `thread_read` | P-D |

### 0.5 The family's one repair, stated once

Seven of the nine fail the same way: **the licence the effect asks lives in the effect, and formation
cannot see it**, so a person forms the act on a referent the fold must refuse (`raze` on a town nobody
occupies, `march` on a hearth, `capture` on a man he has no quarrel with, `accept` on a Record that is no
challenge, `examine` on nothing at all). The tree already has the shape that closes this, twice: an
**occasion-only referent class** stamped onto the question by a resolver-side `queries/world_q.py`
reader (`Detainee` by `detainees_held`, `Enemy` by `enemies_heard`; `rosters.yaml: referent_classes`,
`occasion_only_classes`), which no collection answers and only the declaring row forms on. The repair
for each verb is that shape, with one discipline added: **the stamp and the effect call the same reader**.
The licence moves out of the effect body into one `world_q` function; the effect declines on that
function's `False`, and the stamp offers exactly the ids for which it is `True`. There is one owner of
each licence, called from two places. No new form, operand or column of the requirement grammar is
needed for any of the seven. The fold's conjuncts stay as they are, for a hand-built act.

What this does not fix: a refusal on a WORLD-ONLY fact the chooser is barred from reading (`with`, the
co-location conjunct ruled world-only at IN-59 (a) / RS-26). Those refusals stay. A man may go looking
for someone and not find him there. That is a miss, and it is witnessed. It is not a dead end.

---

## 1. `arrest`

### 1.1 Premise

*An officer of a seat with the power to make arrests takes a person named in a warrant into the custody of
the court that issued it.* The links: (a) a court (a seat that can try him) issues a warrant naming the
person; (b) the warrant reaches an officer whose seat may enforce it; (c) the officer forms `arrest` on
the person it names; (d) the person submits or resists; (e) on submission he is held to the issuing court
(a `detain` edge); on resistance the officer knows he must take him by force; (f) the court, and anyone who
knows, acts on the custody: questions him, tries him, pardons or releases him, or his friends free him.

### 1.2 State today

- **Row** `verb_table.yaml:171-208` (`stratum: contested_physical`). Eligibility `remit:dispatch`.
  `requires_typed`: `existence` of `subject` kind `Person` (conjunct `party`). `counterparty: subject`.
  `contests: "a standing"` (`sigma_leverage`, interim; the row's own open assumption: standing or body).
  Writes `Tenure.since` on Overwhelming, Success and Partial; nothing on Failure. Emits `arrest.made` on the
  three bands and `arrest.resisted` on Failure; refusals `arrest.unauthorized` (eligibility) and
  `arrest.refused` (party, write, counterparty).
- **Formation.** `rosters.yaml: warrant_sourced` (`arrest: dispensation`): `decision/options.py::opening_set`
  (`:255-266`, `:286-287`) keeps only a subject a HELD dispensation's `terms` names
  (`held_record_claims(p)`).
- **Effect.** `loop/effects_information.py::_eff_arrest` (`:1142-1179`): declines unless the prisoner is a
  person not already restrained, the ACTOR HOLDS a warrant naming him (`_held_warrants`, `:948`), the
  warrant's issuing seat could close the custody (`_may_close_custody`), and the gate's `warrant` basis
  admits it (`state/gate.py::may_warrant`, `:980`). It opens one `detain` edge, prisoner -> issuing seat.
- **Readers of its result.** `world_q.detainees_held` (`:3602`) stamps the prisoner as `Detainee` for the
  holder of the custodial seat, so `interrogate` forms on him; the `crime` context of
  `rosters.yaml: violence_contexts` reads the same stamp, so `fight` may form on him; `pardon`, `release`
  and `determine` close custody under the gate's `determination` basis.
- **Reading** (`aperture 2 0`, realm, §0.3): eligible 26 seated; **formed 1, attempted 0**; `arrest.made`
  in the never-emitted list; the corpus run lists `arrest` among the 30 verbs "foldable but never even
  attempted". `detainees_held`'s own docstring records the knock-on: no `detain` is ever open, so the
  `Detainee` class names nobody and `interrogate` is unreachable too.
- **Why.** A warrant is a dispensation minted into its ISSUER's hand (`issue`; IN-12 step 6). The formation
  filter and the effect both require the ARRESTING OFFICER to hold it. Only a person who is both the issuer
  and an enforcing seat could arrest. Delivery to an officer exists only through `give`, which does not reach
  the realm (H-229), and ED-IN-0292 (1) is ruled NO on minting into an addressee's hand. The one formation in
  the reading is such a self-issued warrant, and it was not chosen.
- **Verdict: forms almost never; never attempted.** The mechanism (custody, its gate basis, its readers) is
  sound and tested on hand-built worlds. Link (b) is missing, and link (a) has no reason behind it.

### 1.3 The build-out, decided

1. **A warrant is the officer's licence when it is ADDRESSED to him and he knows of it, not only when he
   holds the paper.** A writ is an order to its addressee. `rosters.yaml: record_kinds` already gives a
   dispensation a `to` key, and `person_q.addressed_to` (`:1365`) is the one reader of it. The licence
   becomes: *a live dispensation whose `terms` names the prisoner, and which the actor holds or which is
   addressed to the actor and named in his own ledger*. Ladder step 4: `fight`'s `crime` context
   (`options.py::_crime_context`) already reads a warrant this way ("the man a warrant charges is its
   addressee, not its maker"). The addressee half needs no mint into his hand, so ED-IN-0292 (1) stands.
2. **One owner of that licence, `queries/world_q.py::warrants_for(w, actor, prisoner) -> tuple[str, ...]`**,
   built from `_held_warrants` (moved out of the effects module) plus the addressee half. `_eff_arrest`
   calls it in place of `_held_warrants`. A new stamp term `warrants_heard(w, p)` stamps every person a
   warrant addressed to `p` names onto his question, under the existing `Person` class, and
   `warrant_sourced` reads the stamp in place of `held_record_claims`. `seize` shares `_held_warrants` and
   is moved onto `warrants_for` in the same commit (one owner; the widening for `seize` is the same
   sentence, and it is named in the proposal as a declared mover).
3. **The contest stays `a standing`.** The row's open assumption is answered by composition rather than by
   choosing (ladder step 5): the warrant's force is a matter of standing (a man submits to the court or
   defies it), and the bodily case already has its verb. On **Failure** (`arrest.resisted`, deposited with
   both parties and every witness) the officer holds a warrant addressed to him naming a man who defied it,
   which is exactly the `crime` context. `capture` forms on him next (§2), fought under `yield` terms. The
   resisting man's own option is `evade / defy` (SOCIAL family) and flight (`move`). The Failure branch
   therefore ends in a choice for both parties.
4. **Graded outcomes.** Overwhelming, Success and Partial open the same edge, as ruled (#453: no degraded
   magnitude for an edge). What grades them is what the WITNESSES learn. The band rides `Event.degree` into
   every deposited `arrest.made` claim, so a Partial arrest (a scuffle, a crowd) is read as one. No new
   write is invented.
5. **Who forms it, when.** A person with a seat granting `dispatch` (who holds `dispatch` is FA-P2's,
   `06_FA_remit_grant_by_row.md`), on a person named by a warrant he holds or that is addressed to him and
   that he has heard of. All person-side: his tenures, his ledger and the stamp.
6. **Refusals, each necessary.** `arrest.unauthorized` (eligibility: he holds no seat granting `dispatch`;
   readable, so formation already declines it). `arrest.refused` at `party` (a hand-built act on a
   non-person), at `counterparty` (self), and at `write`. The `write` refusal remains for two world facts
   the officer cannot read: the man is already in another court's custody (`restrained`), or the issuing
   court could not close the custody (`_may_close_custody`). Both are reported with the clause in the
   reason trail (`01_CORE_reason_trail_in_the_act_store.md`).
7. **Costs and what it forecloses.** One scene act of the officer. A made arrest forecloses a second
   custody of the same man (one live `detain`) and opens `interrogate`, `determine`, `pardon` and `release`
   to the custodial bench.
8. **Reason trail.** The `arrest.*` Event carries the warrant id as its `via` Record. Proposal A adds the id
   to the act's payload as `warrant`, an existing payload key on `confer`'s `term` precedent, so a later
   reader can ask *by whose warrant*.
9. **Consequences for other subsystems.** SC: the custody is a docket item for the issuing bench
   (`05_SC_playable_hearing_B.md`); FI: the prisoner is a witness who can be interrogated; CHAR: the
   prisoner's and his allies' stance toward the officer and the court (`02_CHAR_which_ground_moves_whom.md`);
   FA: an arrest of a seat-holder is a seat neutralised for the season, read by `detainees_held` and by
   every seat-reading predicate that asks `restrained`.

**Upstream, not this family's.** Why a court issues a warrant at all is BINDING's (`issue`, `determine`,
`open_case`; `14_VERBS_BINDING.md`). The minimal chain this family needs from it is one: a `determine` that
finds against a person who is not in custody issues a warrant addressed to an enforcing seat-holder of the
same bench. Until that lands, warrants come from computed `issue` alone, and the gate below plants one.

### 1.4 Scales and play surface

Person scale: one officer, one prisoner. Settlement and faction scale: the seat's purview (the gate's
`warrant` basis, `may_warrant`) bounds where an arrest reaches. The officer need not stand beside the
prisoner. The seat's purview stands for its constables. **This is the one live choice that survives to
Jordan (§10.4, D-1).** A player chooses whom, from the warrants addressed to him, and whether to act on
them this season. The engine resolves the contest. An NPC chooses it through the one chooser
(`decision/choose.py`) on the same candidates, scored by his pursuits like any other act. No branch names
`arrest`.

### 1.5 Tuning hooks

| dimension | modulates | owner |
|---|---|---|
| office | who may arrest (`dispatch` grant) | `offices.yaml` (FA-P2) |
| venue / purview | where (the `warrant` basis's purview) | `state/gate.py::may_warrant` reading `offices.yaml` rung |
| relationship / affiliation | the obstacle: the prisoner's standing and his protectors | `modules/social_contest/roll.py::obstacle` via `05_SC_obstacle_difficulty_and_modifiers_B.md`'s named modifiers |
| capability | the officer's pool | `rosters.yaml: verb_capability` (`arrest` key; CHAR `02_CHAR_capability_uses_table.md`) |
| personality | whether he chooses it | `npcs.yaml` pursuits, `decision/choose.py::score_terms` |
| evidence | whether a warrant is issued | BINDING (`determine`), FI (`08_FI_05_evidence-interface_B.md`) |

### 1.6 Exact edits

In `proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` §A1.

### 1.7 Gate and falsifier

**Gate.** `engine/season/tests/test_v14_arrest_by_addressed_warrant.py`: `build_realm(0)`; a court seat
(a holder of `determine`) issues, through the real fold, a dispensation whose `terms` is a person and whose
`to` is a seated holder of `dispatch` co-located with the issuer. One season through `SeasonDriver.season`
with the shipped chooser and no hand-built act. Pass: the officer's opening set contains `arrest` on the
named person; if attempted, its Event is `arrest.made` or `arrest.resisted`; on `arrest.made` the
custodial holder's next opening set contains `interrogate` on the prisoner (`Detainee` read downstream).
**Control:** the same world with `to` set to a third person forms no `arrest` for the officer.
**Planted failure:** revert `_eff_arrest` to `_held_warrants`. The act forms and is refused at `write`. The
test must fail on the refusal kind.

### 1.8 Cases

NPC-088 (`cases/exercises/NPC-088.yaml:115-117`, `chain/NPC1.yaml:69-71`): a single scene must be able to
change a persistent fact about her, including *arrested*, which needs a made arrest whose custody lasts
into later seasons (the `detain` edge does). Her other need (`:97-98`: an end that is *not* an arrest)
is `fight`'s (§3). NPC-004 and NPC-038 (an investigator's authority varying by territory; a superior's
authorization): the `warrant` basis's purview and the warrant's issuing seat are those two facts. ARC-21
(a target who repels the accusation): `arrest.resisted` followed by `evade / defy`.

### 1.9 NERS reading

- **N.** From below: custody, its gate basis and four reader verbs exist and are unreachable without it.
  From above: every case about a court that bites needs a custody. Laterally: `interrogate`'s whole reach
  is downstream of it. Cut test: remove `arrest` and the only custody left is `capture`, which needs a
  fight, so the law has no way to hold a man except by violence. It cannot be folded into `capture`.
  The two differ in prize (standing against body), and the difference is what a court is.
- **R.** Resistance is a real branch with a follow-up for each party. The no-player half gains courts
  that hold people. Complete at the extremes: self-arrest, double custody and a court that cannot try its
  prisoner each refuse with a named clause.
- **S.** One licence owner for `arrest`, `seize` and the `crime` context, and one occasion-class shape for
  the stamp.
- **E (last, as a ratio).** One reader moved and widened, one stamp, one roster line, against a verb
  family (custody, interrogation, pardon) brought into play. High.

---

## 2. `capture`

### 2.1 Premise

*A man with the authority and the means overpowers a person who is present and takes him prisoner rather
than killing him.* The links: (a) a reason to use force on this person (war, a defied warrant, a crime);
(b) the person is there; (c) a fight under terms that stop at a yield; (d) a yielding loser is held by the
captor's seat; (e) the captive is now leverage: questioned, ransomed, exchanged, tried or freed, and the
people who care about him know.

### 2.2 State today

- **Row** `verb_table.yaml:280-328`. Eligibility `remit:dispatch`. `requires_typed`: `fight`'s four
  conjuncts (`existence` Person, `with`, `individual` of both). `contests: "the body"`, fought under
  `rosters.yaml: duel_terms` `capture: yield`. Bands Declared, Felled, Wounded and Untouched, read off the
  scene per party. `Tenure.since` on Wounded and Untouched (the `detain` on a yield). Emits
  `person.captured` on a yield. Flat refusal `capture.refused`.
- **Formation.** No `referent_class`, so it forms on the question's plain referents of any kind. It is
  **not** in `rosters.yaml: violence_contexts`, so unlike `fight` it forms on anyone the seat-holder knows.
- **Effect.** `loop/effects_combat.py::_eff_capture` (`:334`): `_eff_kill`'s wounds per party plus one
  `detain` edge, captive -> `Act.via`, when the scene's `surrender` names the subject, under the same
  `may_warrant` and `_may_close_custody` pair as `arrest`.
- **Reading** (`aperture 2 0`, §0.3): eligible 26, formed 26, attempted 12, **executed 0, refused 12**
  (`with=False` 7, `exists:Person=0` 3, `individual=False` 2). The corpus run resolved 2 (`Declared` 1,
  `Wounded` 1) across 143 worlds. The hole register's three-seed reading (`hole_register.yaml:5321`)
  counts `capture` 7 resolved over 3 realm seeds x 4 seasons.
- **Verdict: forms but is refused.** It forms on the wrong kinds (5 of 12) and on people who are not there
  (7 of 12). Where it does form correctly it forms with no reason: a seat-holder takes any man he knows of,
  which contradicts ED-IN-0337 (RULED: fighting is exceptional and belongs to war, crime and duels). That
  ruling was applied to `fight` and not to the other violent row.

### 2.3 The build-out, decided

1. **`referent_class: Person`** (the `challenge` repair of `03_PC_duel_chain_reach.md`, rung 4, REM-28's
   precedent). The `exists:Person=0` refusals stop. Cohort persons (`individual=False`, 2 of 12) remain
   `Person` referents, because `individual` is a WORLD-ONLY stem (`data/requires.py: WORLD_ONLY_STEMS`).
   The war and crime contexts below should remove most of them: a cohort is never named by a warrant
   `[UNVERIFIED: whether `enemies_heard` stamps cohort persons as `Enemy` was not read past `:3707`; the
   gate counts the residue]`. Any residue is reported, not hidden. Making cohort-ness person-side is CORE's question, not this row's.
2. **`violence_contexts: capture: [war, crime]`.** The ruled exceptionality applied to the second violent
   row, with the readers that exist (`options.py::VIOLENCE_CONTEXT_READERS`). No `duel` (a duel is
   `accept`'s) and no `defence` (a man defending himself fights; he does not take prisoners under yield
   terms). The import-time check at `options.py:506-511` already accepts the line, since `capture`'s
   subject is its opponent.
3. **Co-location stays world-only** (IN-59 (a), RS-26). The `with` refusals that remain are misses, and
   each is witnessed as a `capture.refused` with clause `with` in the reason trail.
4. **The arrest hand-off is the crime context, unchanged.** A warrant addressed to the actor that names
   the man (§1.3) is read by `_crime_context`. After an `arrest.resisted` the officer forms `capture` on
   him, and the yield-terms fight opens custody to the WARRANT's seat. **One edit to `_eff_capture`:** when
   the captor holds a warrant naming the captive (`warrants_for`, §1.3), the `detain` object is the
   warrant's issuing seat, as `arrest` does. Otherwise it is `Act.via`. One rule ("custody goes to the
   court whose warrant it is"), one owner.
5. **Graded outcomes, recoverable.** Felled (the scene killed someone despite the terms: recorded, not
   prevented), Wounded with a yield (captured and hurt), Untouched with a yield (taken cleanly), and no
   yield (the write clause refuses; the captive is free and both know it). Every branch leaves the captive
   alive except Felled, and every custody is closable (`_may_close_custody` is a precondition of opening it).
6. **What it unlocks.** Every reader of `arrest`'s custody (`interrogate`, `determine`, `pardon`,
   `release`), plus the hostage use: a captive held by a seat of a faction at war is a person whose
   release can be a term of `surrender` or `covenant` (BINDING's). Named, not built here.
7. **Refusals.** `capture.refused` (flat) remains for: a hand-built act on a non-person or a cohort (the
   cell), absence (`with`, world-only), and the write clause (no yield, or a custody nothing could close).

### 2.4 Scales and play surface

Person scale inside every other scale. In a field, a captured commander is SCN-14's "a personal action
inside a mass battle changes the NPC's mass-scale status": the captive's `detain` edge is read by
`world_q.mustered` through `restrained` (a detained person musters nowhere) `[UNVERIFIED: mustered's body
was not opened; the proposal's gate asserts it]`. A player chooses the target and, through the PC duel
round (`03_PC_duel_round_and_approach_B.md` §3), the approach per phase. The engine resolves the scene.
NPCs choose through the one chooser.

### 2.5 Tuning hooks

`rosters.yaml: duel_terms` (`capture: yield`: where the yield falls); `rosters.yaml: violence_contexts`
(which contexts license it); the PC approach and loadout (`03_PC_loadout_and_carry.md`,
`03_PC_weapon_form_at_round_start.md`); `rosters.yaml: verb_capability` (`arms`); `offices.yaml` (who
holds `dispatch`, FA-P2); personality via pursuits (`npcs.yaml`).

### 2.6 Exact edits

`proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` §A2.

### 2.7 Gate and falsifier

**Gate.** `aperture 2 s`, s = 0, 1, before and after: `capture` refusals on `exists:Person` and
`individual` equal 0, and `capture` formed only on persons for whom `violence_context_of` returns `war` or
`crime` (the instrument's `formed` column against a wrapped `violence_context_of` count). Planted scenario
in `test_v14_capture_after_resisted_arrest.py`: §1.7's world with the arrest forced to Failure by a
fixture pool of 0 dice. The same officer's next opening set holds `capture` on the man. A scene fought to
a yield opens `detain` to the warrant's issuing seat, not to `Act.via`. **Control:** with no warrant, the
officer forms no `capture` on him. **Planted failure:** delete the `capture` line from
`violence_contexts`. Formation on a stranger returns, and the test asserts it does not.

### 2.8 Cases

ARC-23 (`chain/ARC2.yaml:292`): *an opposing force defeating a leader in combat must be able to choose
capture over death, creating a distinct ongoing hostage state*. That is the yield terms plus the custody
edge, and the war context makes it formable. ARC-16 (`chain/ARC1.yaml:640`): capturing a movement's
leader with consequences that scale with what survives. The band and the witnesses' claims carry the
scale. NPC-003, NPC-020 (a leader's or an heir's capture as a crisis): the `person.captured` claim
deposited with his faction is the trigger (CHAR's goal stages, `12_ARCS_arcs_as_staged_goals.md`).

### 2.9 NERS reading

- **N.** It is the only route to custody by force and the only hostage-maker. Cut test: fold it into
  `fight` with a terms operand, and the seat-gated custody (`remit:dispatch`) would gate an ordinary
  man's self-defence. Keep it separate.
- **R.** War and law both gain prisoners. The world produces hostages unaided.
- **S.** One violence decline for both violent rows. One custody rule for both custody rows.
- **E.** Two data lines and one branch in the effect. High.

---

## 3. `fight`

### 3.1 Premise

*A person attacks another who is there, and they fight until one falls, yields or the fight breaks off.*
The links: (a) a reason that makes violence thinkable (war, crime, self-defence; ED-IN-0337); (b) the
target is present; (c) a scene resolved at personal scale, approach by approach, with the weapons each
carries; (d) wounds, a death, or nothing, per party; (e) the world learns: witnesses hold the deed, the
dead man's seats empty, the wounded carry the mark, and the feud or the law follows.

### 3.2 State today

- **Row** `verb_table.yaml:733-865` (ruled). Eligibility `own`. Four conjuncts (`existence` Person,
  `with`, `individual` of both). `contests: "the body"`, `step: ENCOUNTER` (Declared at RESOLVE, fought
  at ENCOUNTER, suspendable for a played party). Bands Felled, Wounded and Untouched, read per party off
  `combat_seam` (`seam/ladder.py::party_degree`), the act's band the worst over both. Writes body,
  existence, tenure closure, capability growth (`_grown`) and the lasting mark. Emits `person.died`,
  `tenure.closed`, `body.changed`, `capability.raised` and `contest.undecided`. Refusal `kill.refused`.
- **Formation.** `rosters.yaml: violence_contexts` `fight: [war, crime, duel, defence]`, read in
  `opening_set` (`options.py:216-224`).
- **Reading.** Realm (`aperture 2 0`): eligible 83, **formed 0**. Hole register H-row at
  `hole_register.yaml:5321`: 0 formations in about 3,500 opening sets over seeds 0-2; every
  `violence_context_of` reading was `None`; with `VIOLENCE_CONTEXTS` emptied, `fight` is offered. Corpus
  run: 13 resolved (Declared 5, Felled 8), so the act executes and kills where a case world supplies a
  context.
- **Why no context arises.** `war`: no WAR Proposition exists in any world the tree builds before CR-91
  (`enemies_heard`'s docstring, `world_q.py:3688-3690`). `crime`: no warrant is ever addressed to anyone
  and no `detain` is ever open (§1.2). `duel`: no challenge is ever issued (`03_PC_duel_chain_reach.md`).
  `defence`: needs a violent deed seen in the newest season, and none occurs.
- **Verdict: unreachable in the realm.** The resolver is the most complete in the family. Every missing
  link is upstream.

### 3.3 The build-out, decided

1. **No change to the row's writes, bands or cell.** They are ruled and they execute (corpus).
2. **Reach arrives through the contexts, which other batches feed.** Crime through P-A (§1, warrants
   addressed and heard; §2, custody). War through CR-91 (the war Proposition) under FA-B1's de-jure
   reading (`06_FA_war_lives_in_seats_B.md`). Defence follows from any of them.
3. **Drop `duel` from `fight`'s contexts.** `_duel_context` (`options.py`) is true when the actor holds a
   challenge Record naming him and `r` *either way round*. The challenger holds every challenge he issues
   (it is minted into his hand), so once `03_PC_duel_chain_reach.md` makes challenges issue, **every
   challenger may attack his man under lethal terms without the challenge being accepted**. That is the
   opposite of a duel, which is a fight both sides agreed to, fought under the challenge's stakes. A duel
   is `accept` (§4), under `duel_terms` `accept: blood`. The context line was a CR-87 assumption
   ("Jordan to correct"). This narrows it, by ladder step 5. `test_cr87_violence_contexts.py`'s duel
   positive control is re-pointed to `accept`. A declined challenge is not a dead end. The challenger's
   standing remains (the `challenge.issued` claim every witness holds, read by CHAR's `deeds_judged`),
   and the challenged's refusal to answer is a deed judged by the same reader `[named, not built]`.
4. **Inside a field.** SCN-14 (`ARC6.yaml:1177-1205`) needs a personal act inside a mass battle, one
   per mass time unit, which suspends the actor's command. That is
   `03_PC_duel_round_and_approach_B.md` step 5 (a caller in the field's adapter), and this family does
   not redo it. What `fight` contributes is that the act is the same row (one resolver).
5. **Approach, equipment and withdrawal** are PC's (`03_PC_duel_round_and_approach_B.md` §3-§5,
   `03_PC_loadout_and_carry.md`, `03_PC_exits_withdrawal_recovery.md` Part A). They land inside the scene
   and change no column of this row.

### 3.4 Scales and play surface

Person scale. It is the zoom target of every larger scale (a field's personal act, a riot's ringleader,
an arrest resisted). The player chooses the target among his contexts and, in PLAYABLE mode (REM-31,
the ENCOUNTER suspension), the approach per phase. The engine resolves every unplayed party through
`decide=None` or the PC chooser. NPCs form it through the one chooser, gated by the same contexts.

### 3.5 Tuning hooks

`rosters.yaml: violence_contexts` (which contexts license it); `duel_terms` (lethal by default);
`verb_capability` `arms`; PC loadout records (`03_PC_weapon_records_in_the_export.md`); temperament
and lean (`02_CHAR_choice_alignment.md`); venue (a hall where weapons are surrendered: PC loadout,
`venues.yaml` rows `[named, not designed]`).

### 3.6 Exact edits

`proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` §A3 (one roster line, one test re-point).

### 3.7 Gate and falsifier

**Gate.** After P-A: §1.7's world, the arrest forced to Failure. The officer's opening set holds `fight`
on the man under the `crime` context (`violence_context_of` returns `"crime"`), as well as `capture`.
After `03_PC_duel_chain_reach.md` and §4: a world with one issued challenge. The challenger's opening set
holds **no** `fight` on the challenged, and the challenged's holds `accept`. **Control:** the
pre-change roster forms `fight` for the challenger. **Planted failure:** restore `duel` to the line, and
the test fails on the challenger's opening set.

### 3.8 Cases

NPC-088 (`:97-98`): her season must be able to end by being found and killed. That needs `fight` formed
on her under some context, which for an unaffiliated person is `crime` (a warrant names her) or `war`.
SCN-14 (ARC6): the personal act inside a field. The M-FIELD rank of `12_ARCS_adjudication.md` (10 cases,
17 core needs: a commander's fall, a wound that follows a leader) is this row's per-party bands plus the
lasting mark, which already exist.

### 3.9 NERS reading

- **N.** The only lethal personal act. Its absence is the 0-death realm (§0.3: death census 0).
- **R.** Complete at its extremes (undecided, double felling, a felled attacker). The no-player half
  depends entirely on contexts arising. That dependency is correct under ED-IN-0337 and is the family's
  largest residue.
- **S.** One scene and one ladder for `fight`, `capture` and `accept`. Dropping the duel context removes
  two routes to one outcome under different terms, which is a methodology inconsistency.
- **E.** One deleted roster word. High.

---

## 4. `accept`

### 4.1 Premise

*A person who has been challenged agrees to fight the challenger, and they fight on the challenge's
terms.* The links: (a) a challenge exists, naming him; (b) he knows of it; (c) he chooses to answer it;
(d) the challenger is there; (e) the duel is fought under the challenge's stakes (first blood, yield,
death); (f) the result is a deed every witness judges. Honour is satisfied, a man is wounded or dead,
and the dispute is settled or worse.

### 4.2 State today

- **Row** `verb_table.yaml:951-1009`. `referent_class: Record`, `referent_named: true`. Six conjuncts:
  `existence` of `subject` kind `challenge`, `names:to`, `names:actor`, `with` of `to`, `individual` of
  both. `counterparty: to`. `fight`'s bands, plus `duel.yielded` on Wounded. Fought under the
  challenge's `stakes`, or `duel_terms` `accept: blood` for a computed challenge.
- **Formation.** A `challenge` Record is minted into the CHALLENGER's hand (`_eff_challenge`,
  `effects_information.py:309-336`). `writs_held` stamps Records on the live hold of their ADDRESSEE.
  The challenged never holds his challenge (ED-IN-0292 (1) RULED NO on minting into an addressee's hand;
  `give` does not reach the realm, H-229). So `accept` forms only on OTHER Record-classed referents, and
  the fold refuses each.
- **Reading** (`aperture 2 0`): eligible 83, formed 37, attempted 27, **refused 27, every one on
  `exists:challenge=0`**. Corpus: `accept` among the 13 only ever refused.
- **Lane A** (`03_PC_duel_chain_reach.md`, landing now) removes the wrong-kind formations (a
  Record-classed row forms only on the kind its cell names) and makes `challenge` issue on a dispute. It
  does **not** deliver the challenge to the challenged: its falsifier expects *an `accept` by the
  challenged*, which needs a delivery route it does not build. With lane A alone, `accept` formations
  fall to 0 and stay there. That is the gap this section closes.
- **Verdict: forms but is refused** today. After lane A: **unreachable**.

### 4.3 The build-out, decided

1. **The challenged answers a challenge he has heard of. He need not hold the paper.** The fold's cell
   asks nothing about holding: `names:to`, `names:actor` and `existence` are world reads of the Record.
   Only formation asks for the hold, through `writs_held`. A new stamp reader,
   `world_q.addressed_records(w, p, kind) -> tuple[str, ...]`, returns live Records of `kind` whose
   addressee key (`RECORD_CONTENT["addressee"]`) is `p` and whose id `p`'s own ledger names
   (`person_q.ledger_names`). `questions_for` stamps them as `Record` for `kind = challenge`. One reader
   serves §1's warrants as well (`kind = dispensation`, then mapped to the persons they name). A
   challenge is issued with the challenged present (`challenge` requires `with`), so he witnesses
   `challenge.issued`. Whether that witness claim names the Record id is `[UNVERIFIED: _eff_challenge's
   Event subject was not opened; the gate asserts it, and if it names the challenger instead, the reader
   asks the claim's `content:challenge` value through `ABOUT_KEYS`]`.
2. **No change to the cell, bands, writes or terms.** They execute (the PC-10b tests on a hand-built
   world).
3. **Stakes.** A computed challenge carries no payload, so its duel is fought at `blood` (CR-87). The
   PC lane's approach work (`03_PC_duel_round_and_approach_B.md`) gives the challenger a `stakes` choice
   among `duel_terms` values when the chooser forms `challenge` `[named; the payload key exists]`.
4. **Declining** is the absence of the act, and it costs: §3.3 item 3.
5. **Refusals.** `accept.refused` remains for: the challenger is not here (`with`, world-only), the
   challenger is dead or the Record was destroyed between formation and the fold (`existence`), and a
   hand-built act on a Record that does not name the pair.

### 4.4 Scales and play surface

Person scale, with standing consequences at settlement scale (witnesses). A played challenged person
sees the challenge on his question (the stamp) and chooses to accept or not. The PLAYABLE suspension
gives him the approach. An NPC chooses through the one chooser. His pursuits score `accept` as they do
any act, and the `beneficiary: actor` column credits him the win.

### 4.5 Tuning hooks

`duel_terms` (`accept: blood`); the challenge's `stakes` (PC-B); `venues.yaml` (where a duel may be
fought `[named]`); temperament and pursuits (`npcs.yaml`, `02_CHAR_choice_alignment.md`); regard
consequences (`02_CHAR_scar_cap_and_regard_unit.md`).

### 4.6 Exact edits

`proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` §A4.

### 4.7 Gate and falsifier

Lane A's own falsifier, completed. A seeded realm with one planted dispute between two co-located
persons, run through the real chooser with no hand-built act, produces `challenge.issued`, then an
`accept` attempted by the challenged, then a scene fought under `blood` terms with `duel.yielded` or
`body.changed`. **Control:** without the new stamp, the challenged's opening set has no `accept` (the
pre-change shape after lane A). **Planted failure:** the stamp reader returning `()` reproduces 0
`accept` formations.

### 4.8 Cases

SCN-14 (ARC6: the personal duel within a field) when the duel is agreed. The ARC1/ARC2 honour and
dispute arcs ride on `challenge`'s dispute conjunct (CHAR's `deeds_judged`, CR-88). `12_ARCS` M-REGARD
(a regard earned or lost by a witnessed deed) is the duel's consequence.

### 4.9 NERS reading

- **N.** It is the only consensual violence. Cut test: fold it into `fight` and the duel becomes an
  attack (§3.3), losing the terms and the agreement. Keep it.
- **R.** Adds the honour economy: disputes settled by agreed risk.
- **S.** One delivery rule (heard and addressed) for writs and challenges.
- **E.** One reader, one stamp line. High.

---

