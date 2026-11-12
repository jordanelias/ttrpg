# VERBS · SOCIAL1 — build-out of eleven `social` rows

## Status: REFERENCE (a verb build-out audit under `VERBS_BRIEF.md`; resolves nothing at runtime, CLAUDE.md §0.05)
Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12).

## Read at: 84d2a02 (working tree; implementation lane A's duel-chain and obstacle edits not merged)

Work order: `VERBS_BRIEF.md`, FAMILY = SOCIAL1. Verbs (rows of `engine/season/verb_table.yaml`, stratum
`social`): `carry`, `argue`, `commit`, `comply`, `conceal`, `covenant`, `evade / defy`, `lie`, `forgive`,
`give`, `challenge`. The exact edits are in the four proposals named in §0.4; this file holds the premise,
the state today with its reading, the decided build-out, and the family's order. Cited, not redone:
`proposals/03_PC_duel_chain_reach.md` and `IMPLEMENTATION_BRIEF_A.md` (lane A: formation of `challenge`
and `accept`, the Record-kind formation rule, persons holding scores), `proposals/05_SC_obstacle_difficulty_and_modifiers_B.md`
(the obstacle as task difficulty plus named modifiers; called **SC-OB** below),
`proposals/02_CHAR_offer_what_can_be_done.md` (one person-side decline read off the row; **CHAR-OFFER**),
`proposals/02_CHAR_relations_have_a_ground.md` and `02_CHAR_which_ground_moves_whom.md`. The
contest-interrogation lane's `audits/13_SC_contest_interrogation.md` **did not exist** when this was
written (its scratch `runs/SC_INT/` holds only a census); where the brief says to cite it, SC-OB is cited.

## 0. Verdict and reading

### 0.1 Verdict

**One of the eleven works as its premise promises (`commit`); two execute and carry a consequence a later
reader takes up (`conceal`, `carry`); three execute but a large share of what they form is refused for a
reason the actor could have known (`argue`, `lie`, `give`); four are formed and always refused (`comply`,
`evade / defy`, `covenant`, `challenge`); one is formed almost never (`forgive`).** None is a stub: every
row has a typed cell, a refusal channel and (but for `comply`, `evade / defy`, `lie`) an effect body.

Three causes account for nearly every failure, and each has one owner:

1. **Wrong-kind formation** (`challenge`, `covenant`, `comply`, `evade / defy`, part of `carry`): the row
   forms on a referent of the wrong collection or Record sub-kind and the fold refuses `exists:<K>=0`.
   Lane A's Record-kind rule and a `referent_class` on `covenant` remove it (proposal A).
2. **Co-location the actor cannot read** (`argue`, `lie`, `give`, part of `challenge`): `with` is
   WORLD-ONLY (`data/requires.py: WORLD_ONLY_STEMS`; `ED-IN-0282` for the hearer), the person forms on
   everyone he knows (`person_q.known_persons`), and the refusal is never deposited, so he forms the
   same refused act next round. A person-side belief of who is with him, read off his own dated
   sightings, removes most of it without touching the world-only fold (proposal A).
3. **The document never reaches its addressee** (`comply`, `evade / defy`, `covenant`'s acceptance,
   `accept` downstream of `challenge`): writs and challenges are minted into the maker's hand
   (`ED-IN-0292` (1), RULED NO "for now"), and reach the addressee only by `give`, which is 0 executed in
   season 1 and 1 of 19 in two seasons. The delivery link is `give`'s (proposal B), and whether to reopen
   `ED-IN-0292` survives to Jordan (§D).

### 0.2 What this is read against

- HEAD `84d2a02`. Lane A (`IMPLEMENTATION_BRIEF_A.md`) was landing `03_PC_duel_chain_reach.md` and the
  obstacle work in a worktree; every figure here is the **baseline** that lane moves.
- **This lane's reading:** `python -m engine.season.harness.aperture 1 0` (realm and spine, seed 0, one
  season, `PYTHONHASHSEED=0`, control `content_hash EQUAL`), written by the Fable lane before its cut-off
  to `scratchpad/runs/VERBS_SOCIAL1/aperture_1_0.txt`. **Second reading, not re-run:** the PHYSICAL lane's
  `aperture 2 0` (two seasons) at `scratchpad/runs/VERBS_PHYSICAL/aperture_2_0.txt`, and its
  `corpus_run` (143 cases, seed 0) at `scratchpad/runs/VERBS_PHYSICAL/corpus_run.txt`, read at the line.
  Marked `[2s]` and `[corpus]` below. One seed is a reading of a trajectory, not a rate (CLAUDE.md §0.1
  pt 4); nothing below is a balance claim.

### 0.3 State today, one line per verb

`elig` = persons eligible (seated / unseated); `att / ex / ref` = acts attempted / executed / refused.
Realm arm; `[2s]` the two-season reading.

| verb | elig | formed | att / ex / ref (1s) | `[2s]` att / ex / ref | deciding read of the refusals `[2s]` | verdict |
|---|---|---|---|---|---|---|
| `carry` | 33 / 50 | 46 | 4 / 2 / 2 | 17 / 4 / 13 | `exists:petition=0` 9 · post-admission 4 | **executes**; a third refused on a wrong-kind Record or a matter already docketed |
| `argue` | 33 / 50 | 33 | 10 / 3 / 7 | 41 / 10 / 31 | `with=False` 31 | **executes; three quarters refused** on an absent hearer |
| `commit` | 33 / 50 | 43 | 37 / 37 / 0 | 65 / 65 / 0 | — | **works** |
| `comply` | 33 / 50 | 45 | 16 / 0 / 16 | 33 / 0 / 33 | `exists:dispensation=0` 33 | **forms but is refused**; writes nothing even when admitted |
| `conceal` | 33 / 50 | 83 | 11 / 11 / 0 | 23 / 23 / 0 | — | **executes**; the cover is read by attribution; unranked (no celled axis) |
| `covenant` | 18 / 0 | 18 | 3 / 0 / 3 | 10 / 0 / 10 | `exists:Proposition=0` 10 | **forms but is refused** |
| `evade / defy` | 33 / 50 | 45 | 1 / 0 / 1 | 5 / 0 / 5 | `exists:dispensation=0` 5 | **forms but is refused** |
| `lie` | 33 / 50 | 42 | 6 / 2 / 4 | 22 / 6 / 16 | `clause:hearer` 16 | **executes; three quarters refused**; no band writes |
| `forgive` | 33 / 50 | 2 | 0 / 0 / 0 | 0 / 0 / 0 | — | **formed almost never** (no grievance it can read) |
| `give` | 33 / 50 | 21 | 0 / 0 / 0 | 19 / 1 / 18 | `with=False` 17 · post-admission 1 | **almost unreachable** |
| `challenge` | 33 / 50 | 83 | 48 / 0 / 48 | 84 / 0 / 84 | `exists:Person=0` 65 · `with=False` 13 · `dispute=False` 6 | **forms but is refused** (lane A's target) |

Of the family's declared kinds, never emitted in the one-season reading: `commitment.refused`,
`compliance.given`, `compliance.withheld`, `confidence.broken`, `covenant.offered`, `challenge.issued`,
`stance.moved`, `forgive.refused`, `give.refused`, `record.given`. Emitted: `commitment.made` 37,
`cover.assumed` 11, `petition.carried` 2, `argument.won` 2, `argument.lost` 1, `pursuit.moved` 1,
`news.told` 2 (of `lie`'s), `news.untold` 4. Pools rolled: `argue` and `lie` at pool 2 for every actor
("two actors at different pools: no"). `[corpus]`: `argue` 947 resolved (Failure 660), `lie` 138 (Failure
110); `comply`, `covenant`, `evade / defy` are among the 13 verbs only ever refused; `forgive` among the 30
never attempted; `lie`'s bands do not differ in writes; `comply`, `evade / defy`, `lie` are in "emits and
writes nothing, untagged".

### 0.4 The proposals that carry the edits

| file | verbs | batch |
|---|---|---|
| `proposals/14_VERBS_SOCIAL1_A_formation.md` | `covenant`, `comply`, `evade / defy`, `carry` (kind); `argue`, `lie`, `give`, `challenge` (believed co-location) | S1-A |
| `proposals/14_VERBS_SOCIAL1_B_documents_and_obedience.md` | `give` (delivery), `comply`, `evade / defy`, `covenant` (in force) | S1-B |
| `proposals/14_VERBS_SOCIAL1_C_persuasion_and_deceit.md` | `argue`, `lie`, `conceal` | S1-C |
| `proposals/14_VERBS_SOCIAL1_D_grievance_and_settlement.md` | `forgive`, `challenge` (beyond lane A), `carry` (venue), `commit` | S1-D |

The per-verb sections follow, in the order of the work order. Each has the nine parts the brief orders.

### 0.5 Two shared rules this family introduces (each with one owner)

- **R-WITH, believed co-location.** `queries/person_q.py::believed_with(claims, other, now, window)`:
  True when the holder's newest FIRSTHAND claim that names `other` (a `seen` claim's `Seen.who`, or a deed
  claim whose subject is `other`, or a telling `other` gave him) has `when >= now - window`, window the
  fixture `with_belief_window` (proposed: one season's ticks; control: unbounded, which is today's
  formation). A firsthand claim is deposited by WITNESS only to persons present, so a recent one is the
  person's own evidence that `other` is where he is. Read in formation by CHAR-OFFER's one decline for
  every row whose cell carries a WORLD-ONLY `with` conjunct, from the conjunct's own `of:` operand; never
  by verb name. The fold's `with` stays WORLD-ONLY and unchanged (`ED-IN-0282` is not reopened): a man can
  still be wrong, and then the fold refuses him. Proposal A.
- **R-KIND, the Record sub-kind at formation.** Lane A's rule (`03_PC_duel_chain_reach.md` edit 4): a
  `referent_class: Record` row whose cell has `existence … kind: K` forms only on a Record of kind K. This
  family does not redo it; it names the rows it repairs here (`comply`, `evade / defy`, `carry`).

### 0.6 Every verb resolves by a draw (Standing rule, `AUDIT_BRIEF.md`: *"we do not do deterministic"*)

Re-checked after Jordan's ruling of 2026-11-12. The first draft of this file gave seven of the eleven
(`carry`, `commit`, `comply`, `conceal`'s quality, `covenant`, `forgive`, `give`) and `challenge`'s issue a
fixed effect of state; each is corrected below and in its section. **State sets the odds; the draw sets
the outcome.** Every row below rolls through the one social roll (`modules/social_contest/roll.py`, via
`seam/wrappers/sigma.py`), composes its obstacle by SC-OB's one function (`difficulty` + the named
modifiers, bounded, favourable terms after the bound), records its `terms` on the Event, and resolves on
the four-band ladder (`dice_engine.degree_from_net`). What is NOT drawn, per the rule's own carve-out:
formation and requirement checks (R-WITH, R-KIND, `held_by`, `own_ledger`), the chooser's choice of an
act or a payload (`stakes`, `mode`), and bookkeeping (the hold moving once a hand-over succeeds, an id, a
tick). Every Failure below is recoverable: the act may be tried again, or another route taken, and the
Failure itself writes or deposits something (no band is a silent nothing).

| verb | pool (capability key, `verb_capability`) | obstacle: `difficulty` + modifiers (SC-OB terms; new ones marked †) | Overwhelming | Success | Partial | Failure |
|---|---|---|---|---|---|---|
| `carry` | `procedure` † row | `plain` + venue `standard` + `reception` (the bench's disposition to him) + `backlog` † (items already on that docket × `backlog_step`) | docketed at the next sitting, ahead of the queue | docketed | docketed, a sitting later (date pushed one sitting) | not docketed this season; the petition stays in hand; the refusal names the venue; may carry again next season or to another venue |
| `argue` | `argue` (exists) | `routine` + `opposition` + `regard` / `reception` + `evidence` + `commitment` † | pursuits × 2 | × 1 | × 0.5 (now written) | unmoved; hearer holds the arguer's position as a claim |
| `commit` | `resolve` † row (CHAR's `02_CHAR_resolve_and_temper.md` owns the key) | `plain` + `cross_pressure` † (live commits to contrary Propositions × `cross_pressure_step`) + `violated` † (the Proposition's lean against his own pursuits) | commit Tenure, `degree` Overwhelming (firm: doubles in `argue`'s `commitment` term; `release` of it reads as a grave breach) | `degree` Success | `degree` Partial (wavering: half weight in every reader) | no Tenure; `commitment.refused` with reason "could not bring himself"; may try again next season |
| `comply` | the capability the writ's terms call for (the terms' verb, when the Proposition names one), else `pool_default` | `routine` + `stakes` (the `oblige` kind's `stakes_ob`) + `violated` † (writ's terms against his pursuits) + `distance` † (writ's `at` not his place) | performed; `oblige` opened for the full term; issuer's deed claim leans strongly with | performed; `oblige` opened | performed late or in part; `oblige` opened with half the term; the issuer's claim is neutral | tried and failed: no `oblige`; he keeps the writ (may comply again or defy); the issuer receives `compliance.failed` † (an honest failure, not a defiance) |
| `evade / defy` (`mode: evade`) | `tradecraft` † | `routine` + `purview` † (the issuing seat's reach over his place) + `witnesses` † (persons present × `witness_step`) | never noticed: no `compliance.withheld` is ever emitted | noticed only at the due tick, unattributed | noticed at the due tick, attributed | noticed now, attributed, and a warrant ground for `arrest` |
| `evade / defy` (`mode: defy`) | `argue` (exists) | `routine` + `opposition` (the issuer's, if present, else his seat's holder's score) + `regard` (witnesses' mean regard of the issuer, sign reversed) | defiance stands and witnesses' regard of the defier rises; strife opens with him as its first actor | defiance stands; strife opens | defiance stands; his own stance toward the issuer falls by 2 not 1 (it cost him) | he backs down at the last: no `compliance.withheld`; his hold is kept; witnesses' regard of him falls |
| `conceal` | `tradecraft` † | `routine` + `notoriety` † (persons holding firsthand claims of him at his place × `notoriety_step`) | cover of quality 3 | quality 2 | quality 1 | no cover; `cover.failed` † deposited to those present (they saw him try) |
| `covenant` | `brokerage` † | `routine` + `divergence` † (the maker's own belief of how far the terms lean against the counterparty's pursuits, from his claims) + `regard` (his believed regard) | instrument `standing` 3 (the counterparty's `commit` to it ranks higher; a breach weighs triple) | `standing` 2 | `standing` 1 | not drawn up this season (`covenant.refused`, reason "terms would not hold"); may re-draft with other terms |
| `lie` | `deceit` † | `routine` + `opposition` (hearer's `perception`, via `opposed_by:`) + `regard` + `contradiction` † | believed at the liar's confidence | −1 | −2, floor 1 | not believed; `deceit.exposed` † deed to the hearer |
| `forgive` | `resolve` † | `routine` + `grievance` † (|`deeds_judged`| sum × `grievance_step`) + `scar` (CHAR's scar shift against the referent) | grievance ended (mark factor 0); `stance.moved` told to the forgiven | ended (factor 0) | eased: mark factor 0.5 (deeds before it weigh half) | cannot let it go: no mark; `forgive.refused` with reason; the next attempt's `grievance` term reads the same, so only time or a new kindness moves it |
| `give` | `pool_default` (no key: a hand-over is no skill) | `plain` + `regard` (the receiver's of the giver) + `unwelcome` † (an addressed writ or challenge whose terms the receiver's pursuits judge against him) | handed over and taken gladly (receiver's regard of giver +) | handed over | handed over, taken under protest (a deed claim of reluctance in witnesses' ledgers) | refused: the giver keeps it; the receiver still holds a firsthand claim of the tender, so an addressed document counts as **served** (its answer window starts) |
| `challenge` | `argue` (exists; a challenge is a public speech act) | `plain` + `rank_gap` † (the challenged's seat depth above the challenger's × `rank_step`) + `regard` (witnesses' mean regard of the challenger, favourable) | challenge Record `standing` 3 (a decline costs the challenged triple) | `standing` 2 | `standing` 1 | laughed off: no Record; witnesses' regard of the challenger falls; the dispute stands; he may challenge again later |

New obstacle terms (†) join SC-OB's closed `obstacle_terms` roster; each reads a fact that already exists
(tenures, ledgers, seats, presence at formation) and carries a fixture step with a control of 0. New
capability keys (†) join `rosters.yaml: verb_capability` through DICE's map; until a person holds one,
`pool_default` applies (`verb_capability`'s own note: a missing key is not an error). Proposed difficulty
levels are SC-OB's (`plain` 0, `routine` 1). Every band's write is in the verb's row as a Degree-keyed
`writes:` / `emits:` (the shape `argue` and `lie` already use), so `resolvable_verbs()` and the seam route
them as contested rows; the rows without a counterparty roll against `difficulty` + modifiers alone,
which is what SC-OB's form gives a non-person subject.

---

## 1. `carry` — put a held petition before the room

**1. Premise.** *A person who holds a petition carries it before the court that can hear it, so the matter
is docketed and will be decided.* Links: (a) a petition exists and he holds it; (b) a room exists whose
remit covers what the petition is about; (c) the matter is put on that room's docket; (d) a sitting hears
it and a determination binds; (e) the petitioner learns the outcome.

**2. State today.** Row `verb_table.yaml:108`: `own`; `referent_class: Record`; cell `existence kind:
petition` ∧ `held_by`; no roll; writes `Record.stages`, `DocketItem.*`; emits `petition.carried`; refusal
`carry.refused`. Effect `loop/effects_information.py::_eff_carry` (`:448`): rewinds the petition's stages
and appends `_docket_item(terms, None, pid)` — **no arrangement**, so link (b) is absent: the item names no
room's rule (`world_q.judging_set` gap, the docstring's own [ASSUMPTION]). Declines: not a petition; no
`terms`; already `docketed`; stages unchanged. Readers: `determine` (docket conjunct), `speak`
(`exists:DocketItem`), the strife roster (`petition.carried` joins a strand), `world_q.docketed_by`.
Reading: 1s 4 att / 2 ex / 2 ref (`exists:petition=0`); `[2s]` 17 / 4 / 13 (`exists:petition=0` 9,
post-admission 4: the matter was already docketed). `determine` in the same reading executes 0 (BINDING
§`determine`, refused on `docket`), so link (d) does not complete. **Verdict: executes; consequence reaches
the docket and stops there.**

**3. Build-out, decided.**
- *Formation:* R-KIND (petition only); and a person-side decline when his own ledger holds a claim that
  the matter is already docketed (`docket.formed` / `petition.carried` / `case.opened` claim whose
  docketed matter is the petition's `terms`, read by `world_q.docketed_by`'s person-side twin). The
  world-side `docketed` decline stays for a hand-built act.
- *Room:* the docket item names the arrangement row of the **venue whose purview contains the petition's
  matter at the actor's place** — the first `court`-kind venue up the actor's containment chain whose
  arrangement admits petitions (`arrangements.yaml`, an `admits_petition: true` key, default true on
  courts). One reader, `world_q.petition_venue(w, actor, matter)`. This closes the `None` arrangement
  [ASSUMPTION] in `_eff_carry`; `05_SC_arrangement_rows_that_bind.md` owns the arrangement row itself.
- *Roll (§0.6):* whether the room takes the matter could go either way, so it is drawn: pool `procedure`;
  obstacle `plain` + the venue's `standard` + `reception` + `backlog`. The merits are still contested
  later at `speak`/`determine`; this draw is admission to the docket.
- *Effects by degree:* Overwhelming docketed at the next sitting ahead of the queue; Success docketed;
  Partial docketed a sitting later; Failure not docketed this season, the petition stays in hand (it can be
  carried again, to another venue, or given to someone the bench receives better). Writes as today plus
  the arrangement on the item at the three admitting bands; emits `petition.carried` at those bands and
  `carry.refused` (reason: the room declined it) at Failure.
- *Appeal (the reopenable file, ARCS e5):* a petition whose matter has been determined may be carried to
  the **next venue up** (`petition_venue` walking past the venue that determined it). One rule: the
  reader skips venues whose docket already determined this matter.
- *Costs:* a scene. *Unlocks:* `speak` on the matter, `determine` by the bench. *Forecloses:* a second
  carry of the same matter to the same room.
- *Reason trail:* the docket item names petition, arrangement and venue; `petition.carried` is witnessed.

**4. Scales.** Person (the petitioner) → settlement or realm (the venue). An unseated person's only route
to a binding decision. NPC chooses through the one chooser on held petitions (`held_record_claims`).

**5. Tuning.** Venue (`arrangements.yaml`: `admits_petition`, the `standard:` of SC-OB); office (a seated
petitioner's standing enters at `speak`/`determine` as `reception`, not here); season (sittings,
`convene`'s dates).

**6. Exact edits.** Proposal D §1 (venue and appeal); proposal A §2 (R-KIND names `carry`).

**7. Gate and falsifier.** `aperture 2 s` (s = 0, 1): `carry` refusals `exists:petition=0` = 0; every
`petition.carried` docket item names a non-`None` arrangement; at least one carried matter reaches a
`determine` attempt (`matter.determined` or a `determine` refusal on any conjunct but `docket`). Planted
failure: delete the court venue's `admits_petition` and every carry declines, naming the venue reader.

**8. Cases.** M-SIT cases (ARCS §4 row 7: "a matter gets before a room on a date"); ARC-31 (Quaestio of
Baralta), ARC-21 (Excommunication) need a docketed matter heard; e5 cases (ARC-04, -06, -10) need appeal.

**9. NERS.** N: the only unseated route to a binding decision; removing it leaves petitioning inert. R: a
commoner's grievance can reach a court with nobody watching. S: one docket owner (`docketed`), one venue
reader. E, last: one reader and one row key against a docket that today names no room. **Cut test:**
merging into `petition` (file-and-carry in one act) loses the gap between holding and carrying in which a
petition can be given, seized or destroyed (M-REC); keep it.

---

## 2. `argue` — move a hearer toward one's position

**1. Premise.** *A person argues a position to someone present, and if he argues well the hearer comes
round, part way or wholly.* Links: (a) a position (Proposition) exists; (b) the hearer is present;
(c) a contest whose obstacle is the task plus the hearer's resistance; (d) the hearer's pursuits move by
degree; (e) the hearer's later choices differ.

**2. State today.** Row `:133`: `own`; `referent_class: Proposition`; cell `existence Proposition` ∧
`with` of `to`; `counterparty: to`; `contests: a proposition`; writes `Person.pursuits` at Overwhelming
and Success; emits `argument.won` at Partial too (with no write), `argument.lost` at Failure. Effect
`_eff_argue` (`:647`) through `person_q.argued_pursuits`. Reading: 1s 10 att / 3 ex / 7 ref (`with=False`
7); `[2s]` 41 / 10 / 31 (`with=False` 31); pool 2 for every actor; `[corpus]` 947 resolved, Failure 660,
Overwhelming 2. Obstacle today: `obstacle_default` 2 (nobody holds a score; F-SC-03). Reader of the
consequence: `choose`'s pursuit score (the hearer's later choices). **Verdict: executes; three in four
formed acts are dead ends on co-location; the roll does not differ by person; Partial claims a win and
changes nothing.**

**3. Build-out, decided.**
- *Formation:* R-WITH on `to`. The arguer forms on known persons he has firsthand seen this season.
- *Roll:* pool from `verb_capability: argue` (already a row). Obstacle per SC-OB: `difficulty: routine`,
  `opposition` = hearer's `argue` score × `opposition_rate`, `regard` = hearer's stance toward the arguer
  (no bench), `evidence` = the arguer's cited items for the Proposition, and in a sitting `reception`
  replaces `regard`. A **commitment term** (proposed new `obstacle_terms` member, `commitment`): a hearer
  holding a live `commit` to a Proposition contrary to the argued one adds `commitment_ob` (fixture,
  proposed 1.0, control 0) — affiliation tuning, read off his own tenures (`world_q`'s commit readers).
- *Effects by degree (graded, recoverable):* Overwhelming: pursuits shift × 2 `pursuit_shift`; Success: × 1;
  **Partial: × 0.5 and `Person.pursuits` is written** (today it writes nothing and still emits
  `argument.won` — a deed that did not happen; the row's Partial `writes:` gains `Person.pursuits`);
  Failure: nothing moves, and the hearer still gains the claim of the arguer's position (WITNESS's deposit
  of `argument.lost`, already firsthand to him) — a later `argue` may cite new evidence.
- *Costs:* a scene. *Forecloses:* nothing. *Reason trail:* SC-OB's `terms` on the Event.
- *Consequences:* `choose` (pursuit score), `covenant` (a moved hearer commits), `faction_q` (membership by
  commit), CHAR's `which_ground_moves_whom` (susceptibility — the hearer's cast row decides which grounds
  move him; this verb is its main caller).

**4. Scales.** Person to person; in a sitting, person to bench (the same verb with `reception`). A faction
argument is many person arguments; no faction-scale argue. NPC: one chooser, ranked by the Proposition's
alignment to the arguer's pursuits.

**5. Tuning.** Venue (`reception`, SC-OB), personality (`which_ground_moves_whom`: susceptibility on the
cast row), affiliation (`commitment` term), relationship (`regard`), evidence (`proof_step`), season (none).

**6. Exact edits.** Proposal A §1 (R-WITH); proposal C §1 (row, terms, Partial write).

**7. Gate and falsifier.** `aperture 2 s`: `argue` refusals `with=False` fall by at least half; pools
rolled differ across actors (after lane A's persons-hold-scores); a two-NPC hand-built fold with the
hearer committed to a contrary Proposition in one arm shows `commitment` in `terms` alone. Planted failure:
set `with_belief_window` unbounded and the refusal count returns.

**8. Cases.** ARC-31 (formal debate), ARC-21 (a formal challenge's argument), the e5 multi-tier verdict
cases; chooser demand c7 (ARCS §9).

**9. NERS.** N: the only verb that moves another's pursuits by persuasion. R: positions spread without a
player. S: one obstacle composition with `tell`, `lie`, `speak`. E, last: two data edits and one column
change against 31 of 41 wasted acts. **Cut test:** folding into `speak` loses the private, benchless
argument; keep.

---

## 3. `commit` — take a position as one's own

**1. Premise.** *A person commits himself to a cause or claim, and is thereafter counted as its adherent.*
Links: (a) the Proposition exists; (b) he binds himself; (c) others read him as committed; (d) he can
later release it.

**2. State today.** Row `:209`: `own`; `referent_class: Proposition`; cell `existence Proposition`; writes
`Tenure.since` (a `commit` Tenure, `_eff_commit` `:1252`); emits `commitment.made`; duplicate declined
person-side (`rosters.yaml: held_edge_declines`). Readers: `faction_q` (membership is a commit edge),
`world_q` (adherents, opinion), `predicates.py:176`, `release` (closes it). Reading: 1s 37 / 37 / 0;
`[2s]` 65 / 65 / 0. **Verdict: works.**

**3. Build-out, decided.** Formation unchanged. **Corrected under the Standing rule (§0.6):** today the
effect is a fixed function of state (every `commit` that reaches the effect opens the edge). Whether a man
can truly bind himself to a cause could go either way, so it is drawn: pool `resolve`; obstacle `plain` +
`cross_pressure` + `violated`. The band is written on the Tenure's existing `degree` field (as `_disposal`
writes it for `determine`): Overwhelming firm, Success held, Partial wavering (half weight in every
reader: `faction_q` membership weight, `argue`'s `commitment` term, `covenant_in_force`), Failure no edge
and `commitment.refused` (the row's existing, never-emitted refusal kind finally earned), recoverable next
season. Two consequences to wire, owned elsewhere and named here: `covenant` is in force when both parties hold a
`commit` to its terms (proposal B §3); `argue`'s `commitment` term reads it (proposal C). Costs: a scene;
forecloses nothing but is read by contrary arguments.

**4. Scales.** Person; aggregated to faction by `faction_q`. **5. Tuning.** Affiliation (which
Propositions are offered: those he utters or hears; `terms_sourced` for held documents); personality
(`resolve`), cross-pressure (his other commits). **6. Exact edits.** Proposal D §4 (the draw, the
Degree-keyed row). **7. Gate.** `aperture 2 s`: `commitment.made` and `commitment.refused` both > 0 and the
`commit` Tenures carry more than one `degree`; a hand-built two-arm fold (actor with and without a live
contrary commit) differs in `cross_pressure` alone. Falsifier: every commit Tenure at one degree. **8. Cases.** CHAR §7 "loyalty to a cause" (Kreutz, Ehrenwall,
Torberg). **9. NERS.** Works; E high. **Cut test:** removing it removes faction membership by choice.

---

## 4. `comply` — do what the writ orders

**1. Premise.** *A person who receives a lawful order obeys it, and is then bound to the service it
names; the issuer and the room know he obeyed.* Links: (a) a writ addressed to him exists; (b) it reaches
him; (c) he chooses to obey; (d) obedience binds him (a service, a duty); (e) the issuer, and those who
see it, read the obedience.

**2. State today.** Row `:227`: `own`; `referent_class: Record`, `referent_named`; cell `existence kind:
dispensation` ∧ `own_ledger`; **no effect body; writes `[]`**; emits `compliance.given` (read by no code);
refusal `compliance.impossible`. Formation: `world_q.writs_held` (a writ on his own `hold` naming him);
writs are minted into the issuer's hand (`ED-IN-0292` (1)), so link (b) is `give` alone. Reading: 1s
16 / 0 / 16; `[2s]` 33 / 0 / 33, every refusal `exists:dispensation=0` (a held Record of another kind,
`record_subkind`); `[corpus]` only refused. **Verdict: forms but is refused; would write nothing if
admitted.**

**3. Build-out, decided.**
- *Formation:* R-KIND (dispensation only, lane A). The occasion: `writs_held` (unchanged).
- *Roll (§0.6; the brief names "any obeyed effect with no resolution roll" as a known case):* choosing
  to obey is the person's; whether the obedience is carried off could go either way, so it is drawn: pool
  the capability the writ's terms call for, else `pool_default`; obstacle `routine` + `stakes` +
  `violated` + `distance`. Bands: Overwhelming full term, issuer's claim leans strongly with; Success
  the edge below; Partial half the term, issuer's claim neutral; Failure no edge, he keeps the writ
  (recoverable: comply again, or defy) and the issuer receives `compliance.failed` (new kind: an honest
  failure, judged far more lightly than a defiance).
- *Effects at Overwhelming / Success / Partial:* `comply` **opens an `oblige` Tenure** from the complier to
  the issuing seat (`world_q.issuing_seat(w, rid)`: the `via` of the act that minted the Record, read
  through `state/attribution.py::causing_act` on its minting Event; `None` for a seatless mint, and then
  the `oblige` is not opened and only the hold closes — `[UNVERIFIED]` that every minting Event resolves
  to its act after a load), with
  `term` = the writ's own stages' last due tick (the order lasts as long as it says), `payload =
  {"writ": rid}`. This composes on `oblige`'s existing Tenure (`_eff_oblige`, `rosters.yaml` tenure kind
  `oblige`), so a complier is read by every reader of sworn service: `purview_reaches`' oblige clause,
  `establishment_of`, legitimacy. It also **closes his `hold` on the writ** — he has answered it, which
  removes the occasion (`writs_held` no longer stamps it) and ends the scene tax `writs_held`'s docstring
  records ("NO 'ALREADY ANSWERED' DECLINE").
- *Emits:* `compliance.given` (now with a write behind it), witnessed: the issuer's ledger gains a deed
  claim his pursuits judge (obedience to his own writ leans with his pursuits), so his `regard` of the
  complier rises through the existing `deeds_judged`.
- *Refusals:* `compliance.impossible` keeps only the hand-built case (the writ is gone, or not his).
- *Costs:* the `oblige` binds him; forecloses `evade / defy` on the same writ (the hold is closed).

**4. Scales.** Person → seat (settlement/realm office). The realm's obedience is the sum of compliances;
the strife roster reads defiance, and now the `oblige` edges read compliance.

**5. Tuning.** Office (issuing seat's legitimacy in the complier's eyes drives the choice through
`choose`'s legitimacy term), affiliation (a writ whose terms violate a held affiliation scores low:
`violated_affiliations`), relationship (`regard` of the issuer), season (the term).

**6. Exact edits.** Proposal B §2.

**7. Gate and falsifier.** A seeded realm with the writ delivered (proposal B's delivery occasion, or a
planted `give`): `compliance.given` > 0, each with an `oblige` edge whose payload names the writ; the
issuer's `regard` of the complier rises versus the control arm with the comply effect removed. Planted
failure: drop the hold closure and the same complier forms `comply` on the same writ next round.

**8. Cases.** ARCS M-SIT ("ruling separate from enforcement"); strife moves `RU` (refusal or inaction) need
its opposite to exist.

**9. NERS.** N: without it an order binds nobody (BINDING's `issue` verdict: "binds nobody"). R: obedience
becomes a record others weigh. S: composes on `oblige`; no new Tenure kind. E, last: one effect body on
existing kinds. **Cut test:** merging `comply` into `oblige` (oblige to the writ's seat) loses the writ
link — the obedience would not answer a particular order; keep the verb, share the Tenure.

---

## 5. `conceal` — act under a cover

**1. Premise.** *A person assumes a cover, so that what he does next is attributed to the cover and not to
him, until someone sees through it.* Links: (a) he makes a cover; (b) his later deeds are witnessed as the
cover's; (c) an inquirer can penetrate it, harder the better it was made; (d) once penetrated, the deeds
return to him.

**2. State today.** Row `:251`: `own`; `requires: —`; writes `Record.exists` (a `cover` Record keyed to
the actor, `_eff_conceal` `:292`); emits `cover.assumed`; no refusal. Reader: `state/attribution.py::
live_cover` / `anchor_of` (tier 1): every Event the actor causes while the cover lives is anchored on the
cover's id, so WITNESS deposits deed claims on the alias. Reading: 1s 11 / 11 / 0; `[2s]` 23 / 23 / 0.
`[corpus]`: `conceal` is in RANKING EXCLUDES (no celled axis), so its choice is broken by the draw, not
by any reason. Link (c): no inquiry reads a cover's quality (SC-OB's `subject` term names "a cover's
quality when FI lands one"). **Verdict: executes, and the consequence is read; it is chosen at random and
cannot be seen through by degree.**

**3. Build-out, decided.**
- *Formation and ranking:* the chooser ranks `conceal` by **what it would hide**: the largest
  `violated_affiliations` / `violated_pursuits` weight among the other acts the person forms in the same
  deliberation (a deed he expects others to judge against him). A celled axis is not invented; the score
  term is `choose`'s, read off his own candidates (person-side). Zero when he forms nothing judgeable, so
  he does not mask idly.
- *Roll (§0.6; corrected — the first draft set quality equal to the capability score, a fixed function
  of state):* pool `tradecraft` (new `verb_capability` row `conceal: tradecraft`; ARCS §8 names tradecraft
  as an authored skill); obstacle `routine` + `notoriety`. Quality by band: 3 / 2 / 1; Failure mints no
  cover and deposits `cover.failed` to those present (recoverable: try elsewhere, where fewer know him).
- *Effects:* the cover Record gains a `quality` content key (`rosters.yaml: record_kinds.cover`), read by
  the inquiries as SC-OB's `subject` term (`surveil`, `examine`, `research` on a deed claim anchored on a
  cover). A Success by an inquirer **unmasks**: the cover's stages close (`Record.stages` matured now) and
  WITNESS re-deposits the inquirer's copy with the actor as doer — owned by FI's inquiry effect, named
  here as the consumer. The cover otherwise lapses at its stages (existing).
- *Costs:* a scene. *Forecloses:* nothing.

**4. Scales.** Person; a faction's spy network is many covers. **5. Tuning.** Personality (tradecraft
capability), season (cover lifetime = `record_stages_default`), evidence (quality as `subject` term).

**6. Exact edits.** Proposal C §3. **7. Gate and falsifier.** Hand-built two-arm fold: an actor with a
cover of quality 6 and one of quality 0; one `surveil` against each anchored deed; the two Events'
`terms` differ in `subject` alone. Realm: `conceal` attempts correlate with a same-deliberation
judgeable act (≥ 0.8 of attempts) against the control (draw-ranked). Planted failure: drop the score
term and the correlation returns to chance.

**8. Cases.** ARC-09 N2 and ARC-30 N1 (a concealed identity undetectable to non-specialists), NPC-004
N6 (concealment kept up scene by scene), ARCS e6 (suppressing evidence changes a case).

**9. NERS.** N: the only route by which a deed is misattributed. R: the hidden actor, a story with nobody
watching. S: quality enters inquiry as SC-OB's existing `subject` term. E, last: one capability row, one
content key, one score term. **Cut test:** without it, every witnessed deed names its doer; keep.

---

## 6. `covenant` — bind two parties to terms

**1. Premise.** *Two parties agree terms, each binds himself to them, and the agreement is then in force
and read by what it governs (tribute, alliance, marriage).* Links: (a) terms (a Proposition) exist; (b)
one party offers the instrument; (c) it reaches the other; (d) the other accepts (commits); (e) in force
when both are committed; (f) its readers act on it; (g) breaking it is visible.

**2. State today.** Row `:300`: `remit:issue`; `beneficiary: to`; cell `existence Person` of `to` ∧
`existence Proposition` of `subject`; **no `referent_class`**; writes a `dispensation` Record
(`_eff_covenant` = `_eff_issue`, `:275`); emits `covenant.offered`; refusal `covenant.refused`. Link (c)
is `give`; (d) is `commit` via `terms_sourced`; (e) "a reading nothing performs yet" (the effect's own
docstring); (f) deferred. Reading: 1s 3 / 0 / 3; `[2s]` 10 / 0 / 10, every refusal
`exists:Proposition=0` (`collection`: the subject is no Proposition). **Verdict: forms but is refused;
links (e)–(g) unbuilt.**

**3. Build-out, decided.**
- *Formation:* `referent_class: Proposition` (`argue`'s and `commit`'s class; the rung-4 repair of
  `03_PC_duel_chain_reach.md`), and R-WITH is **not** applied (an instrument can be drawn up in absence;
  it travels by `give`).
- *Roll (§0.6; corrected):* whether the maker can draw up terms that will hold could go either way, so it
  is drawn: pool `brokerage`; obstacle `routine` + `divergence` + `regard` (both the maker's beliefs, from
  his claims). The band is written as the instrument's `standing` content key (3 / 2 / 1); Failure drafts
  nothing this season (`covenant.refused`, recoverable with other terms). Acceptance stays the
  counterparty's `commit`, which is itself drawn (`commit`, §3) and whose `degree` the in-force reader takes.
- *Effects:* as today at the three drafting bands; plus the in-force reader `world_q.covenant_in_force(w, rid) -> bool`: the
  Record's maker and its `to` each hold a live `commit` to its `terms`; it returns the instrument's
  strength, `standing` × the weaker of the two commits' degree weights, `0` when not in force. A breach
  is judged by the other party in proportion to that strength. One owner; readers: tribute
  (`_renewals`) and allied sides (`mustered`), both named deferred in the effect docstring and both
  owned by FA/MB — this proposal builds the reader and names them as consumers, and adds one reader of its
  own that needs no other lane: **`legitimacy`'s deed judgement** — a party who `release`s his commit to
  in-force terms emits `commitment.ended` on a covenant's terms, which WITNESS deposits as a deed claim
  the other party's pursuits judge (a broken covenant is a grievance, read by `holds_dispute`, i.e.
  grounds for `challenge`).
- *Delivery:* proposal B's addressed-document occasion for `give` (the instrument's `to`).
- *Costs:* the maker binds his seat's word. *Forecloses:* nothing; a second covenant on the same terms
  to the same party is declined person-side (`held_document_declines`' shape: he holds one already).

**4. Scales.** Seat to person (a lord's charter), seat to seat (a treaty: the counterparty is the other
seat's holder). A person-to-person oath without office is two `commit`s to one uttered Proposition; no
covenant is needed for it (`remit:issue` stays).

**5. Tuning.** Office (only `issue`-remit seats), affiliation (terms aligned with the counterparty's
pursuits make his `commit` likelier, through `choose`), relationship (`regard`), season (the instrument's
stages = its duration).

**6. Exact edits.** Proposal A §3 (class); proposal B §3 (in force, breach, decline).

**7. Gate and falsifier.** `aperture 2 s`: `covenant` refusals `exists:Proposition=0` = 0 and
`covenant.offered` > 0. Planted-delivery run: maker and addressee both commit → `covenant_in_force`
True; addressee releases → a deed claim in the maker's ledger and `holds_dispute(maker, addressee)` True.
Control: reverted class reproduces the pre-change refusals.

**8. Cases.** ARC cases on marriage and alliance contracts (CHAR §7 "sworn bond"); FA tribute.

**9. NERS.** N: the only consensual binding between parties. R: alliances form and break with nobody
watching, and a breach feeds the duel chain. S: no new kind (a dispensation), in-force read off two
`commit`s. E, last: one class line, one reader. **Cut test:** folding into `issue` loses the two-sided
acceptance; keep.

---

## 7. `evade / defy` — refuse the order

**1. Premise.** *A person who receives an order refuses it, openly or by evasion; the issuer learns of it
and may enforce.* Links: (a)–(b) as `comply`; (c) he refuses; (d) the refusal is visible to the issuer;
(e) it is grounds for enforcement (arrest, revocation); (f) it opens strife.

**2. State today.** Row `:457`: as `comply` (`requires: as comply`); writes `[]`; emits
`compliance.withheld` — **read by the strife roster** (`rosters.yaml:3388`, `opens:`) and by
`harness/strife_moves.yaml` (`RF`, `RU`). Reading: 1s 1 / 0 / 1; `[2s]` 5 / 0 / 5, every refusal
`exists:dispensation=0`. **Verdict: forms but is refused; the one reader exists.**

**3. Build-out, decided.**
- *Formation:* R-KIND (lane A).
- *Two faces, one row (the slash is kept):* the payload's `mode` ∈ `rosters.yaml: defiance_modes`
  `[evade, defy]` (choice-sourced, `choice_sourced` roster; `marshal`'s `role` shape). **defy**: the
  refusal is announced. **evade**: a quiet non-performance. **Both are drawn (§0.6; corrected — the first
  draft made evasion's discovery a fixed function of the due tick):** `evade` rolls `tradecraft` against
  `routine` + `purview` + `witnesses` — Overwhelming never noticed; Success noticed at the writ's due tick
  (a `due` label `answer` on its stages, which MATTER matures) but unattributed; Partial noticed at the due
  tick and attributed; Failure noticed now, attributed, and a warrant ground. `defy` rolls `argue` against
  `routine` + `opposition` + the witnesses' regard of the issuer — Overwhelming the defiance stands and
  witnesses' regard of him rises (he leads the strife strand it opens); Success stands and opens strife;
  Partial stands at a higher personal cost; Failure he backs down at the last (no withheld Event, the
  writ kept, witnesses' regard of him falls) and may defy or comply later. Evasion buys time and risks
  discovery; defiance is immediate and honest.
- *Effects at the bands where the refusal stands:* his `hold` on the writ closes (the occasion is
  answered, as `comply`'s); `defy` writes his own `Person.stance` toward the issuing seat's holder (−1,
  weight 1; −2 at Partial), so `forgive` and `regard` see it. `[UNVERIFIED]` that MATTER's stage
  maturation can emit a row-declared kind for a stage label; if it cannot, the due-tick notice is a MATTER
  step owned by `loop/matter.py`, named in proposal B.
- *Consequences:* the issuer's ledger gains a deed claim (`compliance.withheld`) his pursuits score
  against the defier → `holds_dispute` (grounds for `challenge`), and is the occasion for `arrest` (PHYSICAL
  lane: a defiance claim is a warrant ground, `warrant_sourced`) and `revoke` (BINDING lane). Strife reads
  it unchanged.
- *Costs:* standing with the issuer. *Forecloses:* `comply` on that writ.

**4. Scales.** Person → seat; a settlement's mass defiance is many defy acts; the strife layer aggregates.

**5. Tuning.** Personality (pursuits violated by the writ's terms), affiliation (the issuer's faction vs
his own commit), office (issuer legitimacy), relationship (`regard`), season (the evasion's due tick).

**6. Exact edits.** Proposal B §2 (the shared obedience effect with `comply`).

**7. Gate and falsifier.** Planted-delivery run: one writ whose terms violate the addressee's pursuits;
he forms `evade / defy`; with `mode: defy` the issuer's ledger holds `compliance.withheld` in the same
season; with `mode: evade` only after the due tick; a strife strand opens in both. Planted failure: drop
the hold closure and the occasion repeats.

**8. Cases.** Strife moves RF (refusal or mutiny) and RU; ARCS "ruling separate from enforcement".

**9. NERS.** N: an order that cannot be refused is not an order; the strife opener depends on it.
R: rebellion with nobody watching. S: one obedience effect for both verbs. E, last: one payload roster,
one stance write. **Cut test:** merging `evade` and `defy` loses the time-versus-honesty choice; the
slash already merges them in one row, which is right — keep the row, give the payload two values.

---

## 8. `lie` — tell someone something false

**1. Premise.** *A person tells someone present a falsehood; if believed, the hearer holds it as true and
acts on it; if caught, the liar's standing with him falls.* Links: (a) the liar holds a fact he can falsify;
(b) the hearer is present; (c) a contest against the hearer's discernment and disposition; (d) believed:
the false claim lands at a confidence set by degree; (e) disbelieved: the hearer knows he was lied to;
(f) a later contradiction counts against the liar.

**2. State today.** Row `:534`: `own`; cell `own_ledger` of `subject` (`holds`) ∧ `with` of `to`
(`hearer`); `counterparty: to`; `contests: a standing`; writes `[]` at every band; emits `news.told` +
`confidence.broken` at Overwhelming/Success/Partial, `news.untold` at Failure; refusals `tell.refused` per
clause. Formation gated by `Fixtures.lie_offered` (shipped True) and `rosters.yaml: lie_verbs`; the
false value is `person_q.lie_said_of` (cells only; numbers moved one band step; booleans flipped), carried
on `payload["said"]` and deposited by WITNESS through the told channel; `decision/options.py::record`
counts a contradicted lie against the liar (H-183). Reading: 1s 6 / 2 / 4 (`clause:hearer` 4); `[2s]`
22 / 6 / 16 (`clause:hearer` 16); pool 2 everywhere; `[corpus]` 138 graded, Failure 110, "bands that
differ: False". **Verdict: executes; three in four formed acts are dead ends on co-location; every band
that is not Failure has the same consequence; Failure has none.**

**3. Build-out, decided.**
- *Formation:* R-WITH on `to` (the `hearer` conjunct).
- *Roll:* pool from `verb_capability` (new row `lie: deceit`; DICE's capability map is the owner).
  Obstacle per SC-OB: `difficulty: routine`; `opposition` = hearer's score on the **perceiving**
  capability (`verb_capability: lie` names the liar's key; the hearer's opposing key is the row's
  `opposed_by:` — a new column read by the one pool reader, `10_DICE_one_score_two_roles.md`'s `score()`,
  only where present); `regard` (hearer's stance to liar); a **contradiction term** (`contradiction_ob`,
  proposed 1.0, control 0) when the hearer holds the cell firsthand — read by the host, which may read the
  hearer's ledger because the host builds the counterparty's side (SC-OB "how an NPC-versus-NPC contest
  gets its obstacle").
- *Effects by degree (the told deposit already exists; the band now sets its confidence):*
  Overwhelming: deposited at the liar's own confidence; Success: −1; Partial: −2 (floor 1, believed but
  doubted); **Failure: nothing false is deposited, and the hearer gains a firsthand deed claim
  `deceit.exposed` naming the liar** (a new kind in the `lie` row's Failure `emits:`, in `EMITTED_KINDS`),
  judged by his pursuits (`deeds_judged`) → his regard of the liar falls, and it is grounds for a dispute.
  The confidence is a WITNESS-side read of the Event's band (`loop/witness.py`'s told deposit takes
  `confidence` from the Said; the band adjusts it, one owner: a `lie_confidence_by_band` fixture table).
- *Costs:* a scene; the risk of exposure (Failure is the most likely band today, 110 of 138).
- *Consequences:* the hearer's choices (a false cell drives `requires` reads in his formations); the
  liar's `record`; disputes (`holds_dispute`) and so `challenge`; FI (a told falsehood is evidence that
  can be contradicted).

**4. Scales.** Person to person; a faction's propaganda is many lies and tellings (the told channel
spreads a believed falsehood onward at the hearer's confidence — existing behaviour).

**5. Tuning.** Personality (deceit vs perception capabilities), relationship (`regard`), evidence
(`contradiction` term), venue (none: a lie in a sitting is `speak`'s), season (none).

**6. Exact edits.** Proposal A §1 (R-WITH); proposal C §2 (row, capability, terms, Failure deed,
confidence by band).

**7. Gate and falsifier.** Corpus run: "bands that differ" for `lie` becomes True; `aperture 2 s`:
`clause:hearer` refusals fall by at least half; a two-arm hand-built fold (hearer holds the cell
firsthand vs not) differs in `contradiction` alone; a Failure deposits `deceit.exposed` and
`stance_toward`-free `regard(hearer, liar)` falls versus a control with the Failure deposit removed.

**8. Cases.** M-INFO (ARCS §4 row 2: "reports that differ from what is held"); chooser demand c7 (29
cases); ARC-37 (a supply chain carrying a good under a false account).

**9. NERS.** N: the only route by which a person believes a falsehood on purpose. R: deceit spreads and
is caught without a player. S: one obstacle composition with `tell`/`argue`; one told channel. E, last:
a column, a fixture table and one deed kind against a verb whose four bands are three alike. **Cut
test:** folding into `tell` with a `false` flag would lose the separate formation gate (`lie_offered`)
and the distinct Failure consequence; keep.

---

## 9. `forgive` — let a grievance go

**1. Premise.** *A person forgives someone who wronged him; his grievance ends, he no longer seeks redress,
and the forgiven may learn of it.* Links: (a) he holds a grievance (a wrong he judges against the
other); (b) he chooses to forgive; (c) the grievance stops counting: no dispute, no challenge on it;
(d) his disposition toward the other recovers; (e) a new wrong can start a new grievance.

**2. State today.** Row `:573`: `own`; `requires: —`; writes `Person.stance` (removes rows `held_against`
— negative stance rows naming the referent; `_eff_forgive`, `loop/effects_combat.py:827`); emits
`stance.moved`; refusal `forgive.refused`; formation declined person-side unless `held_against` is non-empty
(`rosters.yaml: own_stance_declines`). **The grievance a person acts on is not a stance row**: `challenge`'s
`dispute` conjunct is `person_q.holds_dispute` over **deed claims** (`deeds_judged`), which `forgive` never
touches; stance rows are written only by `march` (a lost field) and seeded, and `march` fights 0 fields
(PHYSICAL §0.3). Reading: 1s formed 2, attempted 0; `[2s]` the same; `[corpus]` never attempted.
**Verdict: formed almost never; when executed it would not end the grievance that drives challenges.**

**3. Build-out, decided.**
- *What a grievance is:* one owner, `person_q.holds_dispute` (CR-88 re-points it to `grievance_against`;
  this build-out follows whichever is the owner at landing and adds nothing beside it).
- *Formation:* the person forms `forgive` on a referent when **either** `held_against` is non-empty **or**
  `holds_dispute` is True (the `own_stance_declines` reader widened to the one grievance owner; through
  CHAR-OFFER's one decline).
- *Roll (§0.6; corrected):* choosing to forgive is his; whether he can let it go could go either way, so
  it is drawn: pool `resolve`; obstacle `routine` + `grievance` (the size of what he holds) + `scar`.
  Overwhelming and Success end the grievance (mark factor 0; at Overwhelming `stance.moved` is told to the
  forgiven); Partial eases it (factor 0.5: earlier deeds weigh half); Failure writes nothing,
  `forgive.refused` ("could not let it go"), recoverable — the obstacle falls as the deeds age out of
  CR-88's window or a kindness offsets them.
- *Effects at Overwhelming / Success / Partial:* removes the `held_against` rows (Partial halves their
  valence instead) **and writes a forgiveness mark**: a stance row `(referent, 0, 0, since=tick,
  factor)` — zero valence and weight, so `stance_toward` and `held_against` are
  unchanged by it — which `attributed_deeds` reads to **weigh the holder's deed claims about the referent
  whose `when` is at or before `since` by `factor`** (0 skips them). One reader (`person_q.forgiven_since(p, referent)`), read by
  `attributed_deeds`, so `deeds_judged`, `holds_dispute`, `regard` and `world_q.reception` all see the
  same forgiveness. A new wrong (a deed after `since`) starts a new grievance. [ASSUMPTION: a fourth
  element on a stance row; K-49 says a row carries no KIND, and this carries a tick, not a kind; revert:
  a `Person.forgiven: dict[referent, tick]` field.]
- *Emits:* `stance.moved`; witnessed by those present, **told to the forgiven** when he is present (the
  Event names him as subject; WITNESS's firsthand deposit); his `deeds_judged` of the forgiver gains a
  deed that leans with mercy-weighted pursuits (`deed:stance.moved` cells, authored in `rosters.yaml`'s
  deed cells — an `assumption` row).
- *Ranking:* `choose` ranks it by the grievance's own magnitude against the forgiver's mercy/peace
  pursuit weights (existing alignment cells for `forgive`).
- *Costs:* gives up the grounds for `challenge`. *Forecloses:* `challenge` on that grievance (the dispute
  reads False), until a new deed.

**4. Scales.** Person; a lord's forgiveness of a rebel is the same act from a seated person, and composes
with BINDING's `pardon` (which releases a restraint) — two verbs, two objects: `pardon` ends a sentence,
`forgive` ends a grievance.

**5. Tuning.** Personality (mercy-leaning pursuits), relationship (`regard`, stance), season (deed age:
older grievances cost less to forgive, through `recent_claims`' window if CR-88 uses one).

**6. Exact edits.** Proposal D §2.

**7. Gate and falsifier.** Planted run: A holds a firsthand deed claim of B's judged against B
(`holds_dispute(A, B)` True); A forms and executes `forgive`; `holds_dispute(A, B)` is False after, and
A forms no `challenge` on B; a later planted deed by B makes it True again. Realm: `forgive` attempted > 0
over `aperture 2 s`. Planted failure: drop the `attributed_deeds` skip and the dispute survives the
forgiveness.

**8. Cases.** CHAR §7 (feud, rivalry); the duel chain's off-ramp (a dispute must be endable without a
duel, or every dispute ends in blood or never).

**9. NERS.** N: the only off-ramp from a grievance; without it disputes only end by a duel. R: reconciliation
with nobody watching. S: one grievance owner read by challenge and forgive alike. E, last: one widened
decline and one mark. **Cut test:** merging into `pardon` conflates a legal restraint with a private
wrong; keep.

---

## 10. `give` — hand something one holds to someone

**1. Premise.** *A person hands a thing he holds (a document, a title) to someone present, who then holds
it.* Links: (a) he holds it; (b) the receiver is present; (c) he chooses to hand it over (a reason: it is
addressed to the receiver, it pays a debt, it cedes a title); (d) the hold moves; (e) whatever reads the
receiver's holdings now sees it (a writ he must answer, a challenge he must accept, a petition he can
carry, a rung he rules).

**2. State today.** Row `:657`: `own`, `hold:<record>`; cell `held_by` of `subject` ∧ `with` of `to`;
`counterparty: to`; writes `Tenure.until`/`Tenure.since` (`_eff_give` `:887`, a two-hold `handover`);
emits `record.given` or `rung.ceded`; refusal `give.refused`; formation fans `to` over every known person
(`known_persons`), declined person-side where he holds nothing (`own_hold_declines`). **It is the only
link by which a writ, a challenge or a covenant reaches its addressee** (`world_q.writs_held`:
`ED-IN-0292` (1) "just say no for now"; H-229). Reading: 1s formed 21, attempted 0; `[2s]` 19 / 1 / 18
(`with=False` 17). **Verdict: almost unreachable; so `comply`, `evade / defy`, `accept` and a covenant's
acceptance are unreachable behind it.**

**3. Build-out, decided.**
- *Formation:* R-WITH on `to`. And **the addressed-document occasion**: for a held Record whose content
  names an addressee other than the holder (`person_q.addressed_to`'s keys, the one owner), the Candidate
  binds `to` = that addressee (`rosters.yaml: record_sourced_operands`, `to` from the addressee key, the
  existing route (1) of `decision/options.py`) — formed once per such document, not fanned over every
  known person. A document addressed to someone absent waits in hand (R-WITH declines it) until a sighting
  says the addressee is near; no refusal is spent meanwhile.
- *Ranking:* `choose` scores delivering an addressed document by the **maker's** purpose when the holder is
  the maker (he wrote it to be delivered: the issuing act's own score carries over through a
  `delivery_weight` fixture, proposed 1.0, control 0); a non-maker holder scores it by his pursuits as any
  give.
- *Roll (§0.6; corrected — the first draft made a hand-over certain):* whether the receiver takes it could
  go either way (a writ or a challenge is unwelcome), so it is drawn: pool `pool_default`; obstacle `plain`
  + `regard` + `unwelcome`. Overwhelming / Success / Partial the hold moves (Partial: taken under protest,
  a reluctance deed in witnesses' ledgers; Overwhelming: the receiver's regard of the giver rises); Failure
  the receiver refuses, the giver keeps it, and the receiver holds a firsthand claim of the tender, so an
  **addressed document counts as served** (its answer window starts) — the Failure is not a dead end.
- *Effects:* the existing two-hold write at the three taking bands. *Emits:* `record.given` / `rung.ceded`
  there; `give.refused` (reason: the receiver would not take it) at Failure.
- *Consequences (readers named):* `writs_held` (→ `comply`, `evade / defy`, `accept`), `held_record_claims`
  (→ `carry` of a given petition, `commit` via `terms_sourced`), `hold_force` (title), strife (`record.given`
  and `rung.ceded` join strands).

**4. Scales.** Person → person (documents); person → person with seat consequences (`rung.ceded`: title
moves, the settlement's ruler changes). A faction's cession is its head's give of the rung.

**5. Tuning.** Relationship (`regard` raises gift value), office (a seated maker's documents carry the
seat's purpose), season (none).

**6. Exact edits.** Proposal A §1 (R-WITH); proposal B §1 (delivery occasion, ranking weight).

**7. Gate and falsifier.** `aperture 2 s`: `give` refusals `with=False` fall by at least half; at least
one `record.given` of a `dispensation` or `challenge` to its addressee over seeds 0..2 (four seasons, not a
long run: `aperture 4 s` is not required, one planted run suffices if the realm has no co-located
addressee); in the planted run the addressee then forms `comply`/`evade / defy` (or `accept`). Planted
failure: drop the addressed-document occasion and the given count returns to baseline.

**8. Cases.** ARCS M-REC (ARCS §4 row 9: "possession that has consequences; a founding text in one man's
custody"); H-229 (the duel chain's second link); covenant cases.

**9. NERS.** N: the delivery link of three chains. R: documents move, titles cede, with nobody watching.
S: one hand-over basis for Records and Rungs. E, last: one occasion and one weight against three dead
chains. **Cut test:** none; removing it kills writs, challenges and covenants at delivery.

---

## 11. `challenge` — call someone out

**1. Premise.** *A person who holds a grievance against someone challenges him formally; the challenged
must answer (accept and fight, or decline and bear the shame); either way the dispute is settled in the
eyes of those who see it.* Links: (a) a grievance; (b) the challenged is present; (c) a challenge with
stated terms; (d) it reaches the challenged; (e) he accepts (→ duel, PHYSICAL's `accept`) or does not by a
time; (f) the outcome settles the dispute and is seen.

**2. State today.** Row `:923`: `own`; **no `referent_class`**; cell `existence Person` ∧ `with` ∧
`dispute` (all of `subject`); `counterparty: subject`; writes a `challenge` Record (`_eff_challenge`
`:307`: `terms`, `to`, `stakes` from payload else `None`, `challenger`); emits `challenge.issued`; refusal
`challenge.refused`. Reading: 1s 48 / 0 / 48 (`exists:Person=0` 43, `with=False` 4, `dispute=False` 1);
`[2s]` 84 / 0 / 84. Lane A owns formation (`challenge` classed Person, dispute declined person-side,
`accept` on challenge Records) and "the duel actually fires" (step 2). **Verdict: forms but is refused;
links (c)–(f) beyond lane A unbuilt: computed stakes always `None`, delivery by `give` only, no answer by
a time.**

**3. Build-out, decided (on lane A, not redesigning it).**
- *Formation:* lane A's; plus R-WITH on `subject` (the `with` conjunct) — the remainder of the 13
  `with=False`.
- *Roll (§0.6; corrected — the first draft minted the Record with certainty):* whether a challenge lands
  as a challenge could go either way, so it is drawn: pool `argue`; obstacle `plain` + `rank_gap` +
  witnesses' `regard` of the challenger (favourable). The band is the Record's `standing` (3 / 2 / 1),
  which scales what a decline costs the challenged; Failure mints nothing, the challenge is laughed off
  (witnesses' regard of the challenger falls; his dispute stands; he may try again).
- *Stakes:* `stakes` becomes choice-sourced (`rosters.yaml: choice_sourced`, ranged over
  `challenge_terms`, `marshal`'s shape) and ranked by the grievance's magnitude: the challenger's
  `deeds_judged` sum against the challenged, banded by a fixture table `stakes_by_grievance` (proposed: a
  small grievance → `yield`, a larger → `blood`, the largest → `death`, in `challenge_terms`' own order
  `[yield, blood, death]`; control: all `None`, today's, fought under `duel_terms`' `accept` line). The term the duel is fought under is then a person's choice with a reason.
- *Delivery:* the Record's `to` is the challenged; proposal B's addressed-document occasion carries it by
  `give` (the challenger holds it and the challenged is, by formation, present). **No new mint route**
  (`ED-IN-0292` stands; §D).
- *Answer by a time:* the challenge Record's stages carry a due label `answer` at `challenge_answer_ticks`
  (fixture, proposed one round-set within the season). At MATTER, an unanswered, unaccepted challenge
  whose due matures emits **`challenge.declined`** (new kind) naming the challenged as doer — a deed that
  every witness of the challenge judges by their pursuits (honour-leaning pursuits judge it against him),
  scaled by the Record's `standing`, so a refusal to fight costs regard without a fight. Whether the
  challenger then holds himself satisfied could go either way, so the MATTER step draws it (pool
  `resolve`, obstacle `routine` + `grievance` − `standing`): Overwhelming / Success settled (mark factor
  0), Partial eased (0.5), Failure unsatisfied (no mark; he may challenge again). The mark is the same
  `forgiven_since`-shaped mark, so one reader serves both `forgive` and a settled challenge.
- *After the duel:* PHYSICAL's `accept` resolves the fight (`duel.yielded`, wounds, death); the outcome
  likewise writes the settled mark on both parties (the dispute is settled by the duel, ED-IN-0337:
  "a duel settles a dispute"). Owner of the write: the `accept` effect (PHYSICAL lane); named here.
- *Costs:* a scene; a challenge is public (witnessed). *Forecloses:* a second challenge on the same
  dispute while one is live (person-side: he holds a live challenge naming the same `to`).

**4. Scales.** Person to person; a faction's champion is a seated person's challenge; the mass-battle
analogue is `march`. NPC: one chooser.

**5. Tuning.** Personality (honour/violence pursuits rank it; grievance magnitude sets stakes),
relationship (`regard`), office (a seated challenger's challenge is witnessed by his court), season (the
answer window).

**6. Exact edits.** Proposal A §1 (R-WITH, on lane A); proposal D §3 (stakes, answer window, decline,
settled mark).

**7. Gate and falsifier.** Lane A's planted-dispute run extended: the challenge carries a non-`None`
`stakes` chosen by grievance size; delivered by `give`; in one arm accepted (PHYSICAL), in the other left
unanswered → `challenge.declined` at the due tick, witnesses' `regard` of the challenged falls, and
over N seeds of the same planted world `holds_dispute(challenger, challenged)` is False after the
settling bands and True after Failure, at a rate that moves with `standing` (a distribution, not one
outcome: the Standing rule's gate). Planted failure: remove the answer stage and the unanswered challenge
never resolves (the pre-change dead end); fix the draw to one band and the rate goes to 0 or 1.

**8. Cases.** ARC-21 N3 ("a failed formal challenge"), CHAR §7 (feud, rivalry), the PC audit's duel
cases (`03_PC_audit.md` F-PC-01).

**9. NERS.** N: the head of the only route from grievance to personal combat. R: feuds escalate and settle
without a player; a refusal to fight has a price. S: stakes a choice like `marshal`'s role; the answer
window rides MATTER's existing stages. E, last: one choice-sourced key, one stage, one kind. **Cut test:**
none; removing it removes duels.

---

## 12. Dependency graph (within the family)

```
R-KIND (lane A) ──► comply, evade/defy, carry(kind)
R-WITH ──────────► argue, lie, give, challenge(with)          [and tell, fight, accept, capture: by conjunct]
covenant class ──► covenant.offered
give (delivery) ─► comply ──┐
                 ├► evade/defy ─► (issuer's deed claim) ─► holds_dispute ─► challenge
                 ├► covenant ─► commit (acceptance) ─► covenant_in_force ─► (breach) ─► holds_dispute
                 └► challenge's Record to the challenged ─► accept (PHYSICAL)
forgive mark (person_q.forgiven_since) ◄── shared by forgive and the challenge settlement
commit ──► argue's `commitment` term, covenant_in_force
lie Failure ─► deceit.exposed ─► holds_dispute
conceal ─► cover quality ─► FI inquiries (subject term)
carry ─► petition_venue ─► determine (BINDING)
```

`give`'s delivery occasion must land before `comply`, `evade / defy`, the covenant reader and the
challenge's answer window can be gated in the realm (each can be gated earlier on a planted `give`).
The forgiveness mark must land with or before the challenge settlement, which reuses it.

## 13. Cross-family dependencies

| this family needs | from | what |
|---|---|---|
| Record-kind formation; `challenge` Person class and person-side dispute; `accept` on a challenge | implementation lane A (`03_PC_duel_chain_reach.md`) | merged before S1-A's gate is read |
| persons hold scores; one score, two roles | lane A steps 3–4; `10_DICE_one_score_two_roles.md` | before S1-C's obstacle gate can show variation |
| the obstacle composition and its `terms` | SC-OB (`05_SC_obstacle_difficulty_and_modifiers_B.md`) | S1-C adds two members (`commitment`, `contradiction`) to its `obstacle_terms` roster and a `difficulty:` on `lie`/`argue` that SC-OB already lists |
| one person-side decline read off the row | CHAR-OFFER (`02_CHAR_offer_what_can_be_done.md`) | R-WITH and `forgive`'s widened decline are readings inside it, not a tenth roster; if CHAR-OFFER has not landed, they land as one roster each in `opening_set` and fold into it later |
| hearer susceptibility; seeded stance from relations | `02_CHAR_which_ground_moves_whom.md`, `02_CHAR_relations_have_a_ground.md` | `argue`'s pursuit move; `forgive` forming on seeded grudges |
| the duel's outcome writes the settled mark; a defiance is a warrant ground | PHYSICAL (`proposals/14_VERBS_PHYSICAL_A_custody_and_force.md`, `accept`, `arrest`) | S1-D names the write, PHYSICAL owns the effect |
| `issue` addresses executors; `revoke`; `pardon` stays distinct from `forgive`; `determine` consumes `carry`'s docket | BINDING (`audits/14_VERBS_BINDING.md`) | `issue`'s `to` fan should prefer persons R-WITH places with the issuer, so a writ is deliverable; BINDING's call |
| inquiries read a cover's quality and unmask | FI (`audits/08_FI_audit.md` lane; PHYSICAL's `examine`/`surveil`) | the `subject` term's second source |
| covenant readers (tribute `_renewals`, allied `mustered`) | FA, MB | consumers of `covenant_in_force` |
| `tell` gets R-WITH by its `hearer` conjunct | SOCIAL2 | SOCIAL2 must not author a second co-location rule |

## 14. Landing order, in batches, with the gate for each

| batch | proposal | content | needs | gate (execution artifact) |
|---|---|---|---|---|
| **S1-A** | `14_VERBS_SOCIAL1_A_formation.md` | R-WITH (`believed_with`, fixture, decline by conjunct); `covenant` `referent_class: Proposition`; naming `comply`/`evade / defy`/`carry` under R-KIND | lane A step 1 merged | `aperture 2 s`, s = 0, 1: `with=False`/`clause:hearer` refusals on `argue`, `lie`, `give`, `challenge` each down by ≥ half; `covenant` `exists:Proposition=0` = 0; `comply`/`evade / defy` `exists:dispensation=0` = 0; control: `with_belief_window` unbounded reproduces today's hash |
| **S1-B** | `14_VERBS_SOCIAL1_B_documents_and_obedience.md` | `give`'s addressed-document occasion and `delivery_weight`; the obedience effect for `comply` and `evade / defy` (`defiance_modes`); `covenant_in_force` and breach | S1-A | planted-delivery run: `record.given` of a writ → `compliance.given` with an `oblige` naming the writ (arm 1) / `compliance.withheld` and a strife strand (arm 2); a covenant in force then breached → `holds_dispute` True; realm `aperture 2 s`: `record.given` > 0 |
| **S1-C** | `14_VERBS_SOCIAL1_C_persuasion_and_deceit.md` | `argue` Partial writes and `commitment` term; `lie` capability, `opposed_by:`, `contradiction` term, confidence by band, `deceit.exposed`; `conceal` ranking, quality, capability | SC-OB, lane A steps 3–4 | corpus run: "bands that differ" True for `lie`; two-arm hand-built folds differ in one named term each; `conceal` attempts follow a judgeable act |
| **S1-D** | `14_VERBS_SOCIAL1_D_grievance_and_settlement.md` | `forgiven_since` mark and widened decline; `challenge` stakes, answer window, `challenge.declined`, settled mark; `carry`'s `petition_venue` and appeal | S1-B (delivery), lane A step 2, PHYSICAL `accept` | planted-dispute run: forgive ends the dispute; an unanswered challenge declines at its due tick and settles; a carried petition names a venue and reaches a `determine` attempt |

Each batch is a declared hash mover for the shipped realm; its re-record is named in its commit body
(CLAUDE.md §7). **Every gate also carries the Standing rule's check:** for each verb the batch makes drawn,
a planted world run over N ≥ 20 seeds shows at least three of the four bands, and the band distribution
moves when one named obstacle term moves (the state sets the odds). Where a per-verb gate above reads as a
single outcome ("False after", "forms `comply`"), it means at the bands that write it, at a rate.

## 15. Decisions that survive to Jordan

Each was put through the five-step order of CLAUDE.md §0 first; these are the two that survive.

**D1. Should an issued writ (and only a writ) be minted into its addressee's hand?** `ED-IN-0292` (1) is
RULED NO "for now". This audit's build-out works under it (delivery by `give` in person, proposal B), but
under it the realm's obedience depends on an issuer and an executor meeting.
- **(A) Keep the ruling.** Orders travel by hand. Obedience and defiance are rare and local; a distant
  executor never hears; the gap is a place for messengers (a later `dispatch` carrying a document).
- **(B) Reopen it for writs from a seat whose purview reaches the addressee.** Process is served by office:
  the writ is minted into the addressee's hand (the issuer keeps nothing), and `comply`/`evade / defy` form
  the next round. Obedience becomes a realm-wide mechanic. Challenges and covenants stay in-person.

**D2. Should a person learn, from his own refused act, that the one he sought was not there?**
`known_persons`' docstring records that he does not (the `with` read is never deposited). R-WITH removes
most dead ends, but within the window a man who is wrong repeats the act.
- **(A) No (today).** Belief is updated only by new sightings; R-WITH's window bounds the waste.
- **(B) Yes, to the actor alone.** His own refusal deposits a firsthand `absent` reading of the other, at
  the actor's place and tick, which `believed_with` treats as newer evidence; witnesses learn nothing. A
  person then stops seeking someone where he has already failed to find him.

Not escalated, decided here with the reason recorded at the site: the forgiveness mark's shape (§9; a
tick on a stance row, revert named); `comply`'s `oblige` skipped by `purview_reaches`' oath clause
(proposal B §2: an obedience is not an oath, `_disposal`'s `DETERMINED_BY` precedent); `lie`'s Failure
deed (§8: design intent, M-INFO); `challenge`'s stakes by grievance size (§11: the existing closed roster,
ranked).
