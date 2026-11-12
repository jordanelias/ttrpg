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

### 0.6 Checked against the standing rule: "we do not do deterministic" (`AUDIT_BRIEF.md`, 2026-11-12)

Every consequential outcome resolves by a draw with a graded, recoverable result. State sets the odds,
and the draw sets the outcome. Each of the nine, as designed below:

| verb | the draw | finding in code or text, and its repair |
|---|---|---|
| `arrest` | `a standing` contest (`sigma_leverage`), four bands | conforms. Failure is a real branch (§1.3). |
| `capture` | the scene under `yield` terms. Whether anyone yields is drawn in the scene. | conforms. Custody opens on a drawn yield. |
| `fight` | the scene | **FINDING (code): a plain `fight` kills its loser in 200 of 200 (F-PC-04, H-263). Under `death` terms 99.8% end in a felling, and a felling is death with certainty.** Repaired in §3.3 items 6-7: the term follows the context, and a felled party's death is itself a draw (the mortal-wound draw in the seam). PC's Part B (`03_PC_exits_withdrawal_recovery.md`), filed as Jordan's choice, is answered by this rule (ladder step 1: superseded by a later ruling). |
| `accept` | the scene under `blood` or the challenge's stakes, plus the same mortal-wound draw | conforms after §3.3 item 7 (a `death`-stakes duel no longer kills with certainty). |
| `march` | the field | **FINDING (code, recorded at the row's own REM-27 note): "at `troops=weight` a realm force routs on contact whoever is stronger" (`modules/mass_battle/massbattle.py::_weighted_unit`), i.e. decided by the larger number.** MB's `04_MB_headcount_grade_and_scale.md` gate 2 requires "the verdict varies by seed". §5.3 item 9 makes that a precondition of P-B, and §5.7's gate asserts it on the season path. |
| `raze` | **was ungraded in this file's first writing (§6.3 item 6, "a town is razed or it is not"). That was deterministic, and it is corrected.** | §6.3 item 6 now grades it: a drawn razing whose Partial burns without ending the town and whose Failure ends nothing. |
| `examine` | the `graded_inquiries` roll | conforms. The trail shown is masked by the drawn band. |
| `surveil` | the `graded_inquiries` roll, and each sighting through the new channel admitted by its own draw at the band's rate | §8.3 item 2 corrected so that a success is not omniscience. |
| `thread_read` | **ungraded today (a flat `finding.made`: deterministic success for anyone past the gate)** | §9.3 item 2 grades it. Stage 2's Coherence cost is drawn with the working. |

What stays arithmetic, as the rule allows: eligibility and the formation stamps (who may attempt), the
custody edge once a drawn result opens it, the stores moved by a drawn sack (conservation), and the
seeded RNG.

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
6. **The terms follow the context (standing rule; PC Part B's finer form, taken).** `fight` is the one
   violent row fought under `death` terms, which end in a felling 99.8% of the time (F-PC-04). A new
   roster, `rosters.yaml: context_terms` (`violence_contexts`' names to `duel_terms` values), sets
   `war: death`, `crime: yield` and `defence: yield`. `seam/wrappers/combat.py::combat_input` reads the
   context the Candidate formed under (`violence_context_of`, recorded on the act's payload as
   `context`, `confer`'s `term` precedent) and falls back to `duel_terms`. A beaten man in a brawl or
   an arrest yields far more often than he dies (PC's table: `yield` fells 3.0%). His victor's next act
   is a choice (`capture`, `fight` again under a context, or nothing).
7. **A felling is not a death: the mortal-wound draw.** Even under `death` terms, whether a felled
   fighter dies goes by a draw. In `seam/wrappers/combat.py`, after the scene and before the result is
   typed, each felled party makes one roll through the one roller
   (`10_DICE_one_roller_one_fraction_rule.md`). The pool is his body band before the felling floor
   (`Person.body_ceiling`'s band, `band_floors`). The obstacle is the term's lethality plus named
   modifiers: a swept fixture `mortal_wound_ob` keyed by term (`death` high, `yield` and `blood` low),
   plus a tending modifier when a co-located ally holds the `tend` key `[named; SE's `_eff_tend`]`.
   Failure: he dies (the `Felled` band's writes, as today). Partial: he lives, left for dead, `Wounded`
   band writes with `wounds = max_wounds` (the lasting mark, CP-T03-07). Success and better: he lives,
   `Wounded`, the mark only if his wounds reach it. The draw lives in the seam, so `party_degree`
   still reads one typed per-party result and no band, cell or effect forks. The dead man's `Felled` is
   now a drawn outcome, not a function of the scene's last exchange.

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

**Standing-rule gate (the draw).** The audit's 200-fight season probe (H-263, F-PC-04 E3), re-run after
items 6-7: under `crime` and `defence` contexts, deaths fall well below 200 and yields appear. Under
`war` (`death` terms), felled fighters survive at a nonzero rate that varies with body band, and the
survival rate rises with a higher pool. The assertions are `0 < deaths < 200` and survival with
ceiling band high greater than with it low, over seeds 0-199. **Control:** with `mortal_wound_ob` at a
value no pool can meet, the pre-change 200 of 200 returns. That shows the draw is the only thing that
changed. **Planted failure:** bypass the mortal roll, and deaths return to equal fellings.

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

## 5. `march`

### 5.1 Premise

*A commander leads his faction's army against a place held by an enemy, to take it or to besiege it.* The
links: (a) a war, known to the commander, between his seat's faction and the place's holder; (b) an army:
persons and cohorts committed to his faction, mustered where he stands; (c) a target of a kind armies
take (a settlement or a territory); (d) a field (storm) or an investment (besiege), resolved at army
scale with the people in it; (e) casualties per side, a rout or a draw, an arrival or none, rations eaten;
(f) what follows: occupation (`seize`, `raze`), surrender, relief, another march, or peace.

### 5.2 State today

- **Row** `verb_table.yaml:1047-1084` (ruled). Eligibility `remit:dispatch`. `referent_class: Rung`
  (REM-27). `requires_typed`: `existence` of `subject` kind `Rung`. `contests: "a field"` (the
  mass-battle provider). Bands Declared, Won, Lost, Unopposed and Invested (`besiege`). Writes
  casualties, stance, the arrival (`move`'s three pairs), rations and siege wear. Emits `field.won`,
  `field.lost`, `field.unopposed`, `army.arrived`, `siege.pressed`, `person.died` and `tenure.closed`.
  Refusal `march.refused`.
- **Formation.** On any Rung the commander's ledger names (`places_named`) or a stocked larder in his
  seat's purview (`larders_in_purview`). No war, kind or holder test.
- **Fold.** `loop/sides.py::sides_of` musters the army at the actor's nearest settlement under `a.via`'s
  faction. It refuses a target outside `march_target_kinds` by mustering an empty army (H-149, an inline
  kind check its own comment discloses as misplaced, `sides.py:99-115`). A target held by nobody or by
  his own faction resolves `Unopposed` and arrives.
- **Reading** (`aperture 2 0`): eligible 26, formed 26, attempted 13. Of those, **3 unopposed arrivals,
  10 refused at ENCOUNTER on the target's kind, 0 fields fought**. Corpus: never attempted. MB audit
  F-MB-03 (`audits/04_MB_audit.md`): no field in natural play at seed 0, with or without preset armies.
  FA-P2 (`06_FA_remit_grant_by_row.md`): the 13 marches were made by the Guilds' representative, the
  Lord Treasurer, the Legal Advisor and the Skald-Chief, seats whose rows name no `dispatch`.
- **Verdict: executes only unopposed.** The resolver (field, siege, casualties, arrival, rations) is
  built. What fails is who may march, on what, and why.

### 5.3 The build-out, decided

1. **Who.** A seat whose row names `dispatch` (FA-P2; a dependency, not redone here).
2. **On what, and why: the `Field` occasion-only class.** A new reader,
   `world_q.march_defender(w, via, rung) -> Optional[str]`, is **the one owner of "is this a field for
   this seat, and against whom"**. It returns the defending faction id when `rung` is a
   `march_target_kinds` kind, its holder faction (`holder_faction_of`) is at war with `via`'s faction
   (`at_war`), and the war is one the commander knows of (`enemies_heard`'s knowledge rule, shared). It
   returns the ENEMY faction mustered there when the place is held by `via`'s own faction and an
   enemy faction occupies it (relief). Otherwise it returns `None`. A stamp term
   `fields_in_reach(w, p)` stamps every Rung his ledger names (`places_named`'s knowledge rule) for which
   some seat of his granting `dispatch` gets a non-`None` answer, under the new class `Field`.
   `march` declares `referent_class: Field`, replacing `Rung`. `sides_of` calls `march_defender` for
   `subject`, in place of its inline kind check and holder read. Its disclosed debt ("a target-kind
   constraint carried as data… left for a future session") closes by moving the rule to the one owner,
   which reads the roster.
   REM-27 measured a `fields_named` term *unearned* because `places_named` stamped the same Rungs under
   `Rung`. With an occasion-only class, `places_named` no longer reaches `march` at all, so the term earns
   its place by construction. The proposal's gate re-measures it.
3. **No war, no march.** ED-IN-0337 (RULED: fighting belongs to civil war, crime and duels) answers this
   (ladder step 3). Moving an army inside one's own lands is `order_unit` (MILITARY family), not `march`.
   The 3 unopposed arrivals of today's reading (into own-held or unheld places) stop. That is intended,
   and it is declared as a mover. An unheld place (H-166: who holds an unheld place is unruled) is not a
   field.
4. **War must exist.** A WAR Proposition arrives with CR-91 (`declare`, `remit:dispatch`), and FA-B1
   decides whose commitment keeps it live (`06_FA_war_lives_in_seats_B.md`). Until CR-91 lands,
   `fields_in_reach` returns `()` in every built world and `march` forms nowhere. That is an honest
   zero with a named owner, where today's number counts formations that cannot succeed.
5. **Posture is a choice.** `march_postures` (`storm`, `besiege`). The player chooses it as a payload.
   For an NPC, one Candidate is formed per posture, on `vocation_sourced`'s shape
   (`rosters.yaml: vocation_sourced`, `options.py:244-253`), so the chooser scores storm against siege
   and no branch picks for him. `besiege` is shipped withheld (MB). Un-withholding it is MB's
   (`04_MB_playable_field_scenario.md` A and C).
6. **Graded outcomes.** Won, Lost, Unopposed and Invested as built, plus `Drawn` from
   `04_MB_headcount_grade_and_scale.md` (an indecisive field leaves both armies standing, and the next
   act is the commander's). No band is a dead end: Lost leaves the army at its origin, Invested threatens
   (`siege.pressed`, which `surrender` answers), and Won arrives and licenses `seize` and `raze`.
7. **Title.** A won field writes presence, never title (#453 R-6 β, as ruled). The title passes by
   `seize` after occupation. Layer 1's roster contract (`10` §3, "`holdings` and `seats`, for what a
   defeat costs") reads the other way. FA-B1 carries that conflict (§10.4 D-2), and this family does not
   decide it.
8. **Refusals.** `march.refused` remains for: an empty army (no committed member mustered where the
   commander stands: a world fact the chooser cannot read, MB's army presets and MILITARY's
   `recruit`/`form_unit` are the remedy), and a band that moved nobody. A wrong kind, a friendly place or
   no war can no longer reach the fold. The `Field` class makes them unformable.
9. **The field is a draw (standing rule).** The row's own REM-27 note records that at `troops=weight`
   "a realm force routs on contact whoever is stronger". That is a field decided by the larger number,
   which the rule names as forbidden. P-B does not land until MB's `04_MB_headcount_grade_and_scale.md`
   holds its gate 2 ("the verdict varies by seed, and the larger side's `won` share exceeds the
   smaller's"). The size ratio sets the odds, and the engine's seeded draw sets the outcome. A
   `besiege` (Invested) wears the garrison by `sabotage`'s `_fall`. P-B adds a requirement there:
   `_fall` must be a draw, and if it is a fixed fraction it is a finding for SE/MB
   `[UNVERIFIED: `_fall`'s body was not opened]`.

### 5.4 Scales and play surface

Faction scale (the war), settlement and territory scale (the target), army scale (the field), and
person scale (the commander's body, a duel inside the field, SCN-14). A player chooses the target among
his `Field` referents, the posture, the standing orders (`marshal`, BINDING), and in the field the
per-phase orders of `04_MB_playable_field_scenario.md` B. The engine resolves the field. NPCs choose
through the one chooser with the per-posture Candidates.

### 5.5 Tuning hooks

| dimension | owner |
|---|---|
| which kinds are fields | `rosters.yaml: march_target_kinds` |
| postures | `rosters.yaml: march_postures` |
| war (de jure / de facto) | FA-B1 (`at_war`), CR-91 |
| army size and quality | MB presets, MILITARY verbs, SE training Sites (`07_SE_campaign_supply_and_muster.md`) |
| supply | `field_provisioning` fixture, `Rung.stores` (SE) |
| casualties | `field_casualty_model`, `field_winner_casualties` fixtures |
| personality | pursuits (`npcs.yaml`) via `choose.py` |

### 5.6 Exact edits

`proposals/14_VERBS_PHYSICAL_B_field_and_ruin.md` §B1.

### 5.7 Gate and falsifier

**Gate.** `test_v14_march_on_a_field.py`: `build_realm(0)` with one WAR Proposition planted through the
real fold (an `utter` and a `commit` by two seats granting `dispatch`, one per faction, each told of it),
one season through `SeasonDriver.season`. Pass: a seated holder of `dispatch` of one faction forms
`march` only on settlements and territories the other faction holds and that his ledger names; at least
one is attempted, and its Event is a field band (`field.won`, `field.lost`, `siege.pressed` or
`Drawn`), not `march.refused` on kind. **Draw assertion:** the same planted pair, seeds 0-29, produces
both `field.won` and `field.lost` (or `Drawn`) for the larger side. If one outcome holds in all 30, the
field is still deterministic and P-B is not done. **Control:** the same world without the war forms no `march`.
**Planted failure:** restore `referent_class: Rung`. Formations on hearths and own places return, and the
test fails on the formed set. Separately, `aperture 2 0` before and after: `march` formed falls from 26
to 0 in the war-less realm, and every remaining refusal reason is named.

### 5.8 Cases

NPC-089 (`NPC5.yaml:284`): a foreign power's posture toward a neighbouring territory, graduated from probe
to pressure to invasion. Pressure and invasion are `march` under `besiege` and `storm`, and the probe is
FA's. ARC2's invasion arc (`chain/ARC2.yaml:180`: "a failed invasion is more useful to her than a
successful defence") needs a field that can be lost. M-FIELD (10 cases, `12_ARCS_adjudication.md`) needs
fields fought at all.

### 5.9 NERS reading

- **N.** It is the only route by which force changes the map. Cut test: without it, `seize` and `raze`
  have no occupation to read, and war is words.
- **R.** Strategic choice among targets and postures, and wars that the world fights without a player.
  Complete at extremes (empty army, a draw, unopposed).
- **S.** One owner of "is this a field" for formation and fold. Removes `sides_of`'s inline verb rule.
- **E.** One reader, one stamp, one class. It replaces a check the code itself disclosed as misplaced.
  High.

---

## 6. `raze`

### 6.1 Premise

*An army that holds an enemy town destroys it.* The links: (a) a won field or an unopposed arrival has
put his faction's army in a town another faction holds (occupation); (b) the commander chooses ruin over
seizure; (c) the town ends: buildings, title and every tie to it; (d) its stores are carried off or
burned; (e) the people who lived there are homeless; (f) every witness and every former resident
remembers who did it.

### 6.2 State today

- **Row** `verb_table.yaml:1416-1438`. Eligibility `remit:dispatch`. `requires_typed`: `existence` of
  `subject` kind `Rung`. No `contests:`. Writes `Rung.exists`. Emits `rung.razed`. Refusal
  `raze.refused` (flat).
- **Formation.** No `referent_class`: it forms on every plain referent.
- **Effect.** `loop/effects_founding.py::_eff_raze` (`:247`): declines unless the Rung is a
  `raze_target_kinds` kind, `occupying_faction(w, a.via, rid)` names the seat's faction
  (`loop/effects_shared.py:149`, the licence `seize`'s Rung half shares), and that faction is mustered
  there. Otherwise the Rung is deleted and Layer 1's cascade closes every live edge naming it. Sites keep
  naming the gone id, and nothing is re-homed (H-228).
- **Reading** (`aperture 2 0`): eligible 26, formed 26, attempted 14, **refused 14 of 14, every one
  post-admission** (the effect: no occupation). H-228's own measurement, a hand-built march then raze on
  `build_realm(0)`, shows the effect works.
- **Verdict: forms but is refused.** It forms where occupation is impossible because `march` never takes
  a town (§5).

### 6.3 The build-out, decided

1. **The `Occupied` occasion-only class.** `occupying_faction` moves from `loop/effects_shared.py` to
   `queries/world_q.py`, because it is a pure world read and the stamp must call it. `effects_shared`
   re-exports it for `_seize_rung`. A stamp term `towns_occupied(w, p)` stamps every `raze_target_kinds`
   Rung for which some seat of `p` granting `dispatch` has `occupying_faction(...)` not `None` and
   `mustered` true, under `Occupied`. `raze` declares `referent_class: Occupied`. `_eff_raze` calls the
   same pair. One owner for both.
2. **Sack before ruin** (the share is set by the drawn band, item 6). Before the deletion, the town's `Rung.stores` move to the treasury of the
   exercised seat's rung (`requisition`'s two-sided `Rung.stores` shape, the same `_shift` primitive).
   This gives the act a gain to weigh against its costs. The row declares `Rung.stores` twice (both
   check-only beside the effect's first pair), as `march` does.
3. **The Sites end with the town** (on Success and better, item 6). Every Site whose `rung` field is the razed Rung is ended
   (`Site.exists`, a matrix row: `write_matrix.yaml:48`). This is #453 §9.2's Site half, and H-228 names
   it open. It is a write of the act, declared in the row, not a cascade, so Layer 1 §B.8's "nothing
   else" for the cascade is not touched. `site.razed` (#453's kind) is emitted once per ended Site.
4. **Re-homing stays out.** H-228's own ladder found that Layer 1 §B.8 decides it, and that re-homing is
   a Layer 1 amendment no batch may make. The displaced are therefore placeless. Their recovery is
   `migrate` (MATERIAL family): a person with no live `reside` should form `migrate` toward a place he
   knows `[UNVERIFIED: whether `migrate` forms for a placeless person was not read; the gate asserts
   it, and if it does not, the dependency goes to the MATERIAL lane, not into `raze`]`.
5. **Consequences by deed, not by meter.** The razing is witnessed (`rung.razed`, `site.razed`), every
   observer whose state moved takes a scar (`loop/resolve.py::_scar_witnesses`, as built), and a
   former resident's regard for the razer's faction moves through CHAR's reader of witnessed deeds
   (`02_CHAR_which_ground_moves_whom.md`). No social aggregate lands on a Rung (`04:237`).
6. **Graded, by a draw (standing rule; corrects this file's first writing, which left it ungraded).**
   #453 §9.2's `contests: none` stands: there is no second side and no prize. Whether a town is
   destroyed, however, goes by a draw. A town burns unevenly, its people fight the fire and hide their
   stores. The row joins the graded route (`rosters.yaml: graded_inquiries`, the route that is "not a
   prize", renamed `graded_routes` with its existing rows unchanged, since a razing is no inquiry: one
   key renamed, one loader). The pool is the occupying army (`mustered` headcount through
   `seam/wrappers/sigma.py::faculty`'s fallback). The obstacle is the town's size and fabric: the
   Rung's Site count and their `condition`, plus named modifiers (resident cohorts' resistance
   `[named; SE]`).
   - **Overwhelming:** the Rung ends, every Site in it ends, all stores are carried off.
   - **Success:** the Rung ends and its Sites end. Half the stores are carried off, and the rest burn
     (`raze_sack_share`, swept).
   - **Partial:** the town is burnt but stands. Each Site's `condition` falls by `sabotage`'s `_fall`
     (one formula), a share of the stores is carried off, and the Rung is not deleted. Recoverable by
     `restore`.
   - **Failure:** the townsfolk save it. Nothing is written. The act is witnessed as `raze.resisted`, a
     deed the town remembers.

   Partial and Failure are real outcomes for the people of the town. That is why a draw decides them.
7. **Recoverable.** The ground remains (the parent territory). `found` can found a settlement there
   again.
8. **Refusals.** `raze.refused` remains only for world changes between formation and the fold (the army
   left, the town changed hands). Both are named in the reason trail.

### 6.4 Scales and play surface

Settlement scale, decided at faction scale, felt at person scale (the displaced, the witnesses). The
player sees occupied towns on his question and chooses raze, `seize` or nothing. NPCs choose through
the one chooser. A commander whose pursuits weigh order against wealth scores the sack against the
loss.

### 6.5 Tuning hooks

`rosters.yaml: raze_target_kinds`; the sack fraction (all stores today; a swept fixture
`raze_sack_share` in `data/fixtures.py` if SE wants less than all `[named]`); the regard weight of a
razing (CHAR); offices granting `dispatch` (FA-P2).

### 6.6 Exact edits

`proposals/14_VERBS_PHYSICAL_B_field_and_ruin.md` §B2.

### 6.7 Gate and falsifier

**Gate.** `test_v14_raze_after_occupation.py`: §5.7's war world with the march forced to `Won` by a
fixture-planted army imbalance (MB presets). In the next season the victor's opening set holds `raze` on
the occupied town **only**. If attempted at Success (fixture pool): `w.rungs` shrinks by one, every
Site naming it is gone, and the seat's treasury `stores` rose by `raze_sack_share` of the town's prior
`stores`. At Partial: the Rung stands and every Site's `condition` fell. At Failure: nothing moved, and
`raze.resisted` is witnessed. **Draw assertion:** at the shipped pool, seeds 0-29 produce at least two
different bands for the same occupation. **Control:** with no occupation, the
opening set holds no `raze`. **Planted failure:** drop `referent_class: Occupied`. `raze` forms on
unoccupied places again, and the test fails on the formed set. H-228's existing pin
(`test_in12_raze.py`) reddens on the Site half, as it was written to, and is re-pinned.

### 6.8 Cases

`07_SE_arc_needs.md` (raze rows); ARC2 invasion; NPC-075 (`chain/NPC1.yaml`: the cumulative consequence
of every faction's warfare anywhere): a razed town is that consequence in its most visible form.
`[No case names razing directly; the corpus search for raze, sack and siege found none.]`

### 6.9 NERS reading

- **N.** The only act that shrinks the map (H-166's "grain tomb"). Cut test: merge into `seize` with an
  option, and title and ruin would share one licence while their consequences are opposites. Keep it,
  with one owner of the licence for both.
- **R.** A real strategic choice: loot and deny against regard and production. The world can burn
  without a player.
- **S.** One licence owner for `seize` and `raze`, and for formation and fold.
- **E.** One moved function, one class, two declared writes. High.

---

## 7. `examine`

### 7.1 Premise

*An investigator goes to a place and studies what is there (damage, objects, traces) and learns what
happened to it and, if he is good, whose hand did it.* The links: (a) he is at the site; (b) there is
something to find there; (c) a roll against how well it was hidden; (d) by degree: nothing, *that* it was
done, or *that and who*; (e) what he learns is his own firsthand knowledge, which he can tell, cite in a
hearing (FI-05-B), or act on.

### 7.2 State today

- **Row** `verb_table.yaml:1728-1756`. Eligibility `own`, `presence:<site>` (the second declined by the
  fold, H-33). `referent_class: Site` (REM-22). Cell: `existence` of `site` kind `Site`, `present_at`.
  Writes nothing. Graded through `graded_inquiries` (the social-contest module's roll, the obstacle
  `obstacle_default`). Emits `finding.made` on Partial and better and `finding.none` on Failure.
  Refusal `finding.none`.
- **The finding machinery exists.** `loop/resolve.py:1131-1143` sends every produced `finding.made`
  through `seam.find_trail` (`rosters.yaml: inquiry_modules`), and `loop/witness.py::_found_claims`
  deposits the trail Events masked by `rosters.yaml: finding_terms` (Partial: *that* it was done; Success
  and better: *and who*). The trail is `epistemic.trail_of` over `rosters.yaml: covert_kinds`, which has
  **one member, `record.forged`**. A Site is never the subject of a forgery, so an `examine` that
  executes can find nothing.
- **Reading** (`aperture 2 0`): eligible 83, **formed 1, attempted 0**. In the second world of the same
  run, 1 attempted and lost (graded Failure). Corpus: never attempted. REM-22's own measurement: no
  question the realm delivers carries a Site among its referents.
- **Verdict: unreachable**, and empty when reached.

### 7.3 The build-out, decided

1. **Sites where he stands reach his question.** A stamp term `sites_here(w, p)`: the Sites whose `rung`
   is `place_of(w, p)`, stamped under the existing `Site` class. `present_at` then holds for every
   formation. The term is a world read of his own place, `places_named`' shape. The Site class is
   shared, so `restore`, `sabotage` and any other Site-classed row also form on the Sites where he
   stands. That is correct for each (you mend or wreck what is in front of you). It is H-163's
   shared-class cost, declared and measured by the gate.
2. **There is something to find: deeds done to a Site are findable.** `rosters.yaml: covert_kinds` gains
   `site.damaged` (`sabotage`'s kind). `trail_of` already walks "the most recent Event of that kind that
   WROTE `subject`", so an `examine` of a sabotaged Site uncovers the sabotage and, at Success, the
   saboteur. This is one data line, and `_check_covert_kinds` refuses a kind the table does not emit.
   It is the detective precedent of `AUDIT_BRIEF.md` (evidence that names a hand;
   `08_FI_06_testimony-names-a-hand.md`).
3. **The non-gating product.** FI-03's `observes:` column (`08_FI_03_playable-inquiry.md` §2) for
   `examine`: the Site's `condition` and the `stores` of its rung, deposited firsthand on Partial and
   better. This family adopts FI-03's row and does not redesign it.
4. **The obstacle is the difficulty of the task plus named modifiers** (`AUDIT_BRIEF.md`; SC's
   `05_SC_obstacle_difficulty_and_modifiers_B.md`): the base is `obstacle_default`, and the modifier is
   the concealer's skill where the trail's actor holds the `conceal` capability key. Named, and carried
   by SC's modifier list. Not built here.
5. **Graded and recoverable.** Failure deposits nothing and costs a scene act. He may examine again next
   round (no foreclosure), and the trail stays until a newer deed of the same kind overwrites the index
   (`last_emission_of`'s bound).
6. **Refusals.** `finding.none` at admission remains only for a hand-built act (the stamp guarantees
   presence).

### 7.4 Scales and play surface

Person scale. Feeds settlement scale (a sabotaged granary's culprit), faction scale (an enemy's
saboteur exposed) and SC (evidence cited in a hearing). A player chooses which Site. NPC investigators
choose through the one chooser. Their pursuits carry `examine`'s alignment cells.

### 7.5 Tuning hooks

`covert_kinds` (what leaves a trail); `finding_terms` (what each band shows); `obstacle_default` and
SC's modifiers; `verb_capability` (`inquiry` key); `observation_deposit_mode` (who receives observations).

### 7.6 Exact edits

`proposals/14_VERBS_PHYSICAL_C_looking.md` §C1.

### 7.7 Gate and falsifier

**Gate.** `test_v14_examine_finds_the_saboteur.py`: `build_realm(0)`; a person sabotages a Site through
the real fold, unseen (`sabotage` executed with no co-present witness); an investigator stands at the
same place. One season. Pass: the investigator forms `examine` on that Site; an executed `examine` at
Success deposits a claim anchored on the saboteur with the `site.damaged` kind; at Partial it deposits
the kind without the hand. **Control:** with `covert_kinds` at its shipped value, the same Success
deposits no trail claim. **Planted failure:** remove `sites_here` from `_stamped`, and `examine`
formations return to 0.

### 7.8 Cases

ARC-54 (`chain/ARC4.yaml`: one investigative action resolved against a fixed difficulty that on success
reveals one hidden fact; a failed attempt that can expose the investigator, §8). ARC-07 (a military
condition invisible until someone investigates). NPC-004 (a plausible-but-wrong conclusion: FI-03 §3,
dependent on this product existing). NPC-086 (field data as a persistent evidence object). The
M-INFO rank of `12_ARCS_adjudication.md` (33 cases).

### 7.9 NERS reading

- **N.** The only inquiry into the physical world. Cut test: merging it with `surveil` loses the
  difference between studying a thing's past and watching a place's present. The trail and the witness
  channel are different reads.
- **R.** Covert acts become findable, so concealment becomes a strategy with a counter.
- **S.** The existing trail machinery and FI-03's column. Nothing new.
- **E.** One roster value and one stamp term. Very high.

---

## 8. `surveil`

### 8.1 Premise

*A person watches a place (who comes and goes, what is done there) over a stretch of time, and risks
being noticed.* The links: (a) he is at the place; (b) he spends the time; (c) a roll; (d) by degree he
sees some or all of what is done there afterwards this season; (e) on failure he is noticed, and the
people there know someone was watching.

### 8.2 State today

- **Row** `verb_table.yaml:1828-1852`. Eligibility `own`, `presence:<rung>`. No `referent_class`. Cell:
  `existence` of `subject` kind `Rung`, `present_at`. Graded, writes nothing, `finding.made` /
  `finding.none`. The row itself names two absences: the person case (a covert observation of a person)
  and canon's *+2 Exposure* (which has no carrier, since `04:237` forbids social aggregates on a Rung).
- **Reading** (`aperture 2 0`): formed 83, attempted 44, **executed 6** (`finding.made`). 38 refused
  or lost: graded loss 16, `present_at=False` 15, `exists:Rung=0` 7. Pools rolled `[2]` for every actor,
  so nobody differs. Corpus: 236 graded, Failure 173 of 236.
- **What a success yields.** `find_trail` walks `covert_kinds` for deeds that wrote the Rung. None do
  (`record.forged` writes a Record). The 6 findings taught nobody anything (the instrument's
  `finding.made` deposits "a finding was made").
- **Verdict: executes and finds nothing.**

### 8.3 The build-out, decided

1. **Form only where he stands.** `surveil` declares `referent_class: Rung`. A stamp term `place_here(w,
   p)` stamps `place_of(w, p)` under `Rung`. A person-side decline `own_presence_declines: [surveil]`
   (the `own_hold_declines` shape, `options.py:231-236`) keeps only a Rung that is the object of one of
   his own live `contain` tenures. That is his own state, no World. The `present_at` and `exists:Rung`
   refusals (22 of 44) stop.
2. **A success makes him a witness of the place for the rest of the season.** A new observer channel,
   `surveil`, in `loop/witness.py::observers_for`. For an Event whose place is, or lies under, the
   subject Rung of an executed `surveil` by `q` earlier in the same season (the act store's own
   `finding.made` Events of verb `surveil`, read through `causing_act`, so no new state), `q` is an
   observer. Each such Event is admitted by its own seeded draw at a rate the surveil's band sets
   (`witness_channels`' rate, a swept value per band), so a success is watchfulness and not omniscience:
   a deed may still go unseen. What an admitted sighting shows is also set by the band: Partial sees the deed and not the hand
   (`finding_terms`' Partial mask, the same masking), and Success and better see the hand. The channel
   is DATA: `rosters.yaml: witness_channels` gains `surveil` with its band-to-terms reference to
   `finding_terms`. This is canon's "observe… over extended time" without a meter, a watch edge or any
   held state.
3. **Failure exposes him.** The Failure band emits `finding.none` **and** a new kind `watcher.seen`,
   which is not in `undeposited_kinds`. It is witnessed by the persons present at the place through
   the ordinary co-location channel, as a deed anchored on the surveiller. This is the Exposure half of
   canon carried as claims, which `04:237` permits. A watched faction's officers can then act on it
   (`arrest` under a warrant, CHAR regard).
4. **Pool differences** are CHAR and DICE's (`02_CHAR_capability_uses_table.md`;
   `10_DICE_advantage_sources_for_the_arcs.md`). The row's capability key is `inquiry` (`verb_capability`).
5. **The person case stays absent.** `trail_of`'s anchor walk (deeds BY a person) is the shape a
   person-subject inquiry would use. A disjunction is not in the grammar, and inventing one for one row
   is refused (`G4`). An institutional track on a person (ARC-32, ARC-33) is composed from repeated place
   surveillance plus `tell` within an institution. Named, not built.

### 8.4 Scales and play surface

Person scale. Feeds faction intelligence (a spymaster's officers watching a town) and SC (what was
seen is evidence). A player chooses the place by standing in it. NPCs choose through the one chooser.

### 8.5 Tuning hooks

`witness_channels` (the channel's gain); `finding_terms` (what each band shows); `obstacle_default` and
SC's modifiers (a crowded market hides a watcher, a closed hall does not: `venues.yaml` `[named]`);
`verb_capability` (`inquiry`); alignment cells (`rosters.yaml` tables, existing).

### 8.6 Exact edits

`proposals/14_VERBS_PHYSICAL_C_looking.md` §C2.

### 8.7 Gate and falsifier

**Gate.** `test_v14_surveil_witnesses_the_place.py`: `build_realm(0)`; a watcher and a third person at
one settlement. The watcher's `surveil` is forced to Success (fixture pool) in round 1. The third person
performs `give` at the same place in round 2, with no co-location channel admitting the watcher
`[the test plants the watcher in a quarter under the settlement so the ordinary channel does not
admit him]`. Pass: the watcher holds a claim of the `give` anchored on the giver. At Partial, the claim
holds no hand. At Failure, the third person holds a `watcher.seen` claim anchored on the watcher.
**Control:** without the surveil, the watcher holds no claim of the `give`. **Planted failure:** remove
the `surveil` channel from `witness_channels`, and the Success case deposits nothing.

### 8.8 Cases

ARC-32 and ARC-33 (`chain/ARC2.yaml:584`, `:624`: an institutional surveillance track accumulating
toward a threshold; the accumulation is CHAR's goal stages reading the claims surveil deposits).
ARC-54's third need (a failed investigative action that exposes the investigator: `watcher.seen`).
NPC-033 (a spymaster surfacing a hidden actor through sustained effort against concealment). NPC-034's
unresolved purpose (surveillance of Crown policy).

### 8.9 NERS reading

- **N.** The only act that turns presence into knowledge of other people's acts. Cut test: without it,
  witnessing is accidental co-location only.
- **R.** A real risk and reward: knowledge against exposure. The world produces spies without a player.
- **S.** One masking table for findings and watching. One witness function, one more channel.
- **E.** One stamp, one decline line, one channel and one kind. High.

---

## 9. `thread_read`

### 9.1 Premise

*A person sensitive to the Thread looks into a person or a place with that sense and learns what the
Thread there shows: the knots and ties binding it, a practitioner's sensitivity and how frayed his
Coherence is. It costs him something of his own Coherence, and the Church condemns it.* The links:
(a) he has the sensitivity (a gate); (b) the subject is in front of him; (c) a working roll against the
difficulty of the read (depth, breadth, distance); (d) by degree: nothing, the surface, or the depth;
(e) a Coherence cost; (f) if anyone sees it, the deed is witnessed threadwork.

### 9.2 State today

- **Row** `verb_table.yaml:1853-1870`. Eligibility `own`, `presence:<site>`. Gate: `scalar_threshold`
  of `actor` over `thread_sensitivity` against the `thread_sensitivity.gate` fixture (K-3, H-85).
  Ungraded. Writes nothing. Emits `finding.made` (flat). The row says itself that what the act reads, the
  Depth and the Coherence cost are not expressed.
- **Reading** (`aperture 2 0`): eligible 83, formed 4 (the persons whose authored `ts:` passes the gate),
  attempted 3, executed 3, each depositing only "a finding was made" (ungraded: `find_trail` keys
  nothing for a finding with no degree; FI-03's evidence `thread_read` 2/1/0 in `build_realm(0..2)`).
  Corpus: never attempted. The corpus run lists it under *EMITS AND WRITES NOTHING… untagged*.
- **Verdict: executes and finds nothing.** The gate is the only built part.

### 9.3 The build-out, decided (two stages)

**Stage 1, now, on what exists.**

1. **Subject: a person present.** `referent_class: Person` and a cell conjunct `relation` of `subject`,
   `with` (world-only, `give`'s and `fight`'s carrier). The Site half waits on the Thread world substrate
   (`12_ARCS_substrate_as_ground.md`, M-SUB), which has no carrier.
2. **Graded.** `rosters.yaml: graded_inquiries` gains `thread_read` (the same route as the other
   inquiries). Its `emits:` becomes degree-keyed (`finding.made` on Partial and better, `finding.none`
   on Failure), as `examine`'s is.
3. **Product.** FI-03's `observes:` for `thread_read`: the subject's `thread_sensitivity` against the
   same gate, as a firsthand claim "sensitive / not" (NPC-004's latent sensitivity, NPC-005's secret
   one). Success and better add the band of the subject's sensitivity (the `band_floors` reading, no new
   number).
4. **It is witnessed threadwork.** The executed act's Event is already witnessed. The orthodoxy cell
   (`rosters.yaml:3767`, `thread_read: -1` on the Church's axis) already scores it for observers' regard.
   No edit.

**Stage 2, after the threadwork module and CP-T07-02 (WR).**

5. **The obstacle is the working's.** `09_WR_threadwork_module.md` makes `modules/threadwork/` a
   registered module with a `read` operation (`thread_operations`). The `graded_inquiries` row for
   `thread_read` re-points from the social-contest module to that module's entry, whose obstacle is the
   Three-Axis Ob. The edit is one data row, and the manifest check refuses an unregistered pair.
6. **The cost.** The working's outcome returns the practitioner's displacement, and the effect writes
   `Person.coherence` (matrix row exists, no writer: H-47) through CP-T07-02's carrier. The row
   declares `Person.coherence` on every band, including Failure (a failed read still frays).
7. **The depth.** `observes:` gains the subject's live `knot`/`tie` edges and Coherence band (T07,
   named in FI-03 §2 and not designed there or here).

### 9.4 Scales and play surface

Person scale. Feeds the Church's institutional hostility (NPC-034) and the threadwork arc lane
(M-PERC: 26 cases, 48 core needs). A player with sensitivity chooses whom to read. NPCs with
sensitivity choose through the one chooser. The orthodoxy cell makes a devout practitioner reluctant.

### 9.5 Tuning hooks

`thread_sensitivity_gate` fixture; `band_floors` (sensitivity bands); the threadwork module's
Three-Axis Ob tables (WR); `rosters.yaml` alignment cells (orthodoxy); `observation_deposit_mode`.

### 9.6 Exact edits

`proposals/14_VERBS_PHYSICAL_D_thread_read.md` (stage 1 as edits, stage 2 as the edits it waits on).

### 9.7 Gate and falsifier

**Stage 1 gate.** `test_v14_thread_read_diagnoses.py`: `build_realm(0)`; a practitioner with authored
`ts:` above the gate co-located with a person whose `ts:` is above it and with one whose `ts:` is below
it. Reads forced to Success. Pass: the practitioner holds firsthand claims "sensitive" of the first and
"not" of the second, through WITNESS's observation deposit. **Control:** at Failure, neither claim.
**Planted failure:** drop the `observes:` cell, and the Success deposits only `finding.made`.
**Stage 2 gate:** WR's own falsifier (`09_WR_threadwork_module.md`, "The gate that shows it worked"),
plus: an executed `thread_read` lowers the actor's `Person.coherence` resting point by the module's
returned displacement, and a Failure lowers it too.

### 9.8 Cases

NPC-004 (`chain/NPC2.yaml`: a second person with the capability runs a targeted check on Saemund and
learns his latent sensitivity: stage 1). NPC-005 (a secret sensitivity that must be true and
discoverable: stage 1). NPC-002 (a Thread operation in ordinary intelligence work costs the
practitioner: stage 2). NPC-075 (access gated by demonstrated Thread competence: CHAR goal stages
reading a `thread_read` deed claim). NPC-080 (`NPC5.yaml`: a person with a hard-zero capacity shown
evidence by someone who has it: stage 1's claim, told).

### 9.9 NERS reading

- **N.** The only verb of the threadwork arcs that exists in the loop. Cut test: without it, M-PERC's 26
  cases have no act at all.
- **R.** Stage 1 gives a hidden fact a discoverer. Stage 2 gives it a price.
- **S.** The same graded route and the same observation deposit as every inquiry. Stage 2 adds the
  threadwork module's obstacle through the same route row.
- **E.** Stage 1 is four data edits. Stage 2 is one route re-point and one write, on WR's module.

---

## 10. The family: order, dependencies, decisions

### 10.1 Dependency graph within the family

```
arrest (P-A1: warrants addressed and heard)
   └─> capture (P-A2: crime context reads the resisted warrant; custody to the warrant's court)
         └─> fight (P-A3: crime context reachable; duel context dropped)
accept (P-A4: challenges heard)  ──requires──> lane A's 03_PC_duel_chain_reach (challenges issue)
   └─> fight (P-A3's drop of `duel` must land WITH or AFTER P-A4, or no duel route exists between them)
march (P-B1: Field class)  ──requires──> CR-91 war + FA-B1
   └─> raze (P-B2: Occupied class; occupation only follows a won or unopposed march)
   └─> capture/fight (war context, already read by `enemies_heard`)
examine (P-C1)   surveil (P-C2)   — independent of each other and of P-A/P-B
thread_read (P-D1 now; P-D2 after WR's module and CP-T07-02)
```

`addressed_records` (P-A1) is the one new primitive shared by `arrest` and `accept`.
`march_defender` (P-B1) and `occupying_faction` moved to `world_q` (P-B2) are the shared primitives of
the field batch. `sites_here` and `place_here` (P-C) are the shared primitives of looking.

### 10.2 Cross-family dependencies

| this family needs | from | for |
|---|---|---|
| who holds `dispatch` by row | FA-P2 `06_FA_remit_grant_by_row.md` | `arrest`, `capture`, `march`, `raze` eligibility |
| a reason to issue a warrant (`determine`, `open_case`, `issue`) | BINDING (`14_VERBS_BINDING.md`), SC | `arrest` upstream |
| challenges issued on a dispute | lane A, `03_PC_duel_chain_reach.md` (CORE, PC) | `accept` |
| a WAR Proposition and its live reading | CR-91; FA-B1 `06_FA_war_lives_in_seats_B.md` | `march`, `raze`, `fight`/`capture` war context |
| armies that exist; `besiege` un-withheld; `Drawn` | MB `04_MB_playable_field_scenario.md`, `04_MB_headcount_grade_and_scale.md`; MILITARY (`recruit`, `form_unit`, `order_unit`) | `march` |
| standing orders, surrender | BINDING (`marshal`, `surrender`) | `march`'s aftermath |
| `migrate` for the placeless | MATERIAL | `raze`'s displaced |
| `observes:` column | FI `08_FI_03_playable-inquiry.md` §2 | `examine`, `surveil`, `thread_read` |
| obstacle modifiers | SC `05_SC_obstacle_difficulty_and_modifiers_B.md` | all graded rows |
| the threadwork module; Coherence carrier | WR `09_WR_threadwork_module.md`; CP-T07-02 | `thread_read` stage 2 |
| approach, loadout, withdrawal, duel round | PC `03_PC_duel_round_and_approach_B.md`, `03_PC_loadout_and_carry.md`, `03_PC_exits_withdrawal_recovery.md` | inside `fight`, `capture`, `accept` |
| regard moved by witnessed deeds | CHAR `02_CHAR_which_ground_moves_whom.md` | consequences of all nine |

### 10.3 Landing order, in batches

| batch | proposal | lands after | gate |
|---|---|---|---|
| P-C | `14_VERBS_PHYSICAL_C_looking.md` | nothing in this family (FI-03 §2's `observes:` for the product half; the stamp and trail halves stand alone) | §7.7, §8.7, plus `aperture 2 0` and `2 1`: `examine` and `surveil` refusals on `present_at`/`exists` = 0 |
| P-D1 | `14_VERBS_PHYSICAL_D_thread_read.md` stage 1 | FI-03 §2 (`observes:`) | §9.7 stage 1 |
| P-A | `14_VERBS_PHYSICAL_A_custody_and_force.md` | lane A; FA-P2 | §1.7, §2.7, §3.7, §4.7; `aperture 2 0` and `2 1` before/after |
| P-B | `14_VERBS_PHYSICAL_B_field_and_ruin.md` | CR-91, FA-B1, MB presets | §5.7, §6.7 |
| P-D2 | `14_VERBS_PHYSICAL_D_thread_read.md` stage 2 | WR module, CP-T07-02 | §9.7 stage 2 |

P-C goes first because it depends on nothing unbuilt and turns two executing-but-empty verbs into
products. P-B formation (the `Field` class) may land before CR-91: it takes `march` from 26 doomed
formations to an honest 0 with a named owner, and it is declared as such.

### 10.4 Decisions that survive to Jordan

Each was run through the five-step ladder (CLAUDE.md §0). Everything else in this file was decided at a
named step.

- **D-1. Does an arrest need the officer beside the prisoner?** (a) No: the seat's purview stands for
  its constables, and an officer arrests anywhere his court reaches (as built, and as this file
  proceeds). (b) Yes: `arrest` gains `with`, so arrests happen only where the officer stands, and a
  capital court's reach shrinks to the capital unless officers travel. These lead to materially
  different games (a realm-wide police against a local one), and no ruling, precedent or document
  decides it. `may_warrant`'s purview reads (a). `fight`'s IN-59 ruling reads (b) for violence, not
  for warrants.
- **D-2. Does a won field transfer title?** (a) No: presence only, and title passes by `seize`
  (#453 R-6 β, as built). (b) Yes: Layer 1's roster contract (`10` §3, "`holdings` and `seats`, for
  what a defeat costs"). The two documents contradict each other. FA-B1 already carries this to Jordan;
  it is restated here because `march` and `raze` both depend on it.

Not surviving, with the step that answered each: PC's Part B (`03_PC_exits_withdrawal_recovery.md`,
filed as Jordan's: is a plain fight to the death?), step 1, superseded by the standing rule of
2026-11-12 ("we do not do deterministic"), and taken in §3.3 items 6-7; arrest's contest of standing or of the body
(step 5: composition, §1.3); march without war (step 3: ED-IN-0337); the duel context on `fight`
(step 5, §3.3); raze re-homing (step 3: Layer 1 §B.8 and H-228's own ladder); surveil's Exposure
(step 5: claims, not a meter, §8.3).

### 10.5 Instrument note

Every figure in §0.3 and in each "State today" comes from the earlier lane's `aperture 2 0` and
`corpus_run` outputs (`scratchpad/runs/VERBS_PHYSICAL/`, timings in the `.time` files), read at the
line, or from the hole register and lane audits as cited. The completing lane ran no new instrument
(the brief forbids a long `aperture` run, and the two existing readings covered every verb). One seed
is a trajectory, not a rate.

