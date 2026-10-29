# The thrust layer — a design for `engine/season/` (v2, after one adversarial round)

## Status: PROPOSED — HELD BACK IN FULL (v2). PARTLY RULED since: the v10 plan folds this design in as `CL-THRUST` (`workplans/valoria_master_workplan_v10_part12.md`) and rules (M20, M21, ED-IN-0301; `workplans/valoria_master_workplan_v10_part6.md`) that R3′ and the stage `deadline` are excluded, `closing`, `successor` and `deal` are struck, and the `Slain` band and B5.1 are cut, with B4.x, B5.2 and B6.n held — read those rows before this file. Merging the PR that carries this file ratifies NOTHING in it (ED-1094's default is not applied; no ledger row, CURRENT.md row or Status line elsewhere is flipped). Reference under CLAUDE.md §0.05 — not a mechanism, binds no code, creates no plan position. v2 = the producer's v1 plus one adversarial round (critic: read-only, opus, saw only the file and the tree); every finding was checked against the tree before it was applied; the record is the last section. Citations marked [c] were opened by the critic and not re-opened by the orchestrator.

Citations are `path:line` as opened by the producer on 2026-10-25 (tree at `b7a1e1b2`; **checked 2026-10-28:** `queries/world_q.py` has since gained ~93 lines above `:2168`, so its line numbers have drifted by +93 — `ambitions` is now at `:2261`, `goal_referents` at `:2300` — and the `workplans/valoria_master_workplan_v9*.md` files cited at the plan rows are retired: read `workplans/valoria_master_workplan_v10*.md`); a citation I could not open is
marked so. `[ASSUMPTION]` marks a reading of mine with no tree support.

**What the thrust layer IS.** A person's *thrust* is a standing OUGHT he is committed to (an
ambition — already a live `commit` tenure to an OUGHT Proposition, `engine/season/queries/world_q.py:2168-2204`),
plus an authored, typed LADDER of short/medium-term stages beneath it whose completion is a
*query over world state*, never a stored progress counter. The layer's whole job is to change
WHICH QUESTION a person answers and WHICH REFERENT he answers it about, season by season, so that
the existing chooser and the existing verbs produce causally linked acts that change both the
person and his world. Closure comes from lawful, actor-decided forms (a docket matter a judge
determines, a bound peace, a succession, an authored contest form whose winner the dice pick).

**What it IS NOT.** It is not an arc object, not a script, not a director in the sense of writing outcomes (it does steer attention: a stage's referents join a person's own `need` question, which the drama-manager literature also calls management): no row of it writes an
outcome, picks a winner, schedules a beat because a person *needs* one, or shows an actor a
forecast. It adds no verb and no question source. It does not raise lethality; it lowers it
(§5). A goal still "only changes what a person attends to; it never acts" (`engine/season/goals.yaml:12`) —
the layer keeps that sentence true and adds an ORDER to the attending.

---

## 1. The contract

### 1.1 Objects

| Object | What it is | Reads | Writes | Exists? |
|---|---|---|---|---|
| **Thrust** (ambition) | a live `commit` tenure to an OUGHT Proposition | `p.tenures`, `w.propositions` | nothing (a READ) | **EXISTS**: `world_q.ambitions` `world_q.py:2168-2204`; org-goal Propositions minted per `goals.yaml` row at world-gen (`goals.yaml:3-4`, reader `harness/populated.py`) |
| **Referent** of a thrust | who/what the thrust is about | goal `object:` kind; live `hold` tenures; own ledger | nothing | **EXISTS**: `goal_referents` `world_q.py:2207-2267` (kinds `person`, `rung`, `seat_holders`, `deed_doers`, `orientation`→`()`) |
| **Axis** | one of the user's ten thrust directions, with a pole and its opposing pole | — (roster) | — | **NEW**: a closed roster in `engine/season/goals.yaml` (§2.1) |
| **Ladder** / **Stage** | an ordered list of typed stage predicates under an axis; the *current stage* of a person on a thrust is the first stage whose predicate is false | the world (through existing queries) and `p`'s own ledger | nothing | **NEW** data (§2.2); **NEW** one reader `current_stage(w, p, ambition)` in `queries/world_q.py`, beside `goal_referents` (§3) |
| **Duty** | what a held seat obliges its holder to attend to | `offices.yaml` seat rows; live `hold` | nothing | **PARTIAL**: seat-attached goal rows exist for 2 seats only (`goals.yaml:449-472`, `off_katepano`, `off_kommerkiarios`) — both foreign seats, seated only by `build_realm(foreign=True)`, so none binds anyone in the shipped realm (`01` G-09); seats' purview is already a tier-1 referent (`attention_key`, `world_q.py:2570-2571`, `own_purview`) |
| **Challenge** | a settlement condition that raises a question (larder low, site damaged, band crossed) | `Rung.stores`, `Site.condition`, MATTER's crossings | nothing | **EXISTS as occasions**: `larders_in_purview`, `places_named` stamped onto `out[0]` (`world_q.py:2889-2897`); band crossings deposit claims (`world_q.py:2748-2751`). No new object. |
| **Identity** | the cohort/settlement/faction a person is — the stance he takes toward a pole | `cast.stance_from_loyalty`, `goals.yaml` `stance:` | nothing | **EXISTS**: `goals.yaml:25-27` (stance × loyalty sign), `engaged_poles` `world_q.py:2278` |
| **Closure form** | a lawful way a stage or thrust ends (§4) | docket, tenures, the seam | through existing verbs only | **EXISTS** as verbs (`open_case`, `determine`, `oblige`, `covenant`, `challenge`/`accept`; succession is IN-61's, §4.3); the threshold that RAISES a docket matter is **NEW** (§4.1) |

Nothing in the table stores "this person is on stage 3". The ladder is authored; the current
stage is derived every time it is asked (§3.2).

### 1.2 The user's arc criterion as a predicate

The user: *"an arc for a character needs to be something narrative that affects themselves and
their world in some manner."* For person `p` and thrust `a`:

```
ARC(p, a) holds iff there exist an act A by p and Receipts r_self, r_world minted by the gate with
  (1) A was formed from a question q with  q.source == "need" and q.about == a,
      OR q's referents intersect goal_referents(w, p, a)               -- the act is ON the thrust
  (2) r_self  writes a (kind, field) in ARC_SELF  on p, or on a Tenure whose .subject is p
  (3) r_world writes a (kind, field) in ARC_WORLD on a record that is neither p nor a Tenure owned by p
  (4) A ∈ causes*(r_self.event) and A ∈ causes*(r_world.event)          -- linked by causes[]
  (5) r_self ≠ r_world
```

**ARC_SELF and ARC_WORLD are rosters, not "any Receipt".** v1 said any Receipt would do and was
wrong: every witnessed act deposits a claim through `w.write("claim_ledger", … emits="claim.deposited",
subject=c.id, causes=[e.id])` (`engine/season/loop/witness.py:654-657`), and the gate puts that
`subject=` on the minted Receipt (`engine/season/state/world.py:1306-1322`). So clause (3) was met by
WITNESS bookkeeping after every seen act, and clause (2) by any self-write such as `move`'s
`Person.travel_leg`: "moved toward a referent and was seen" would have read as an arc, and the
shuffled-`causes` null could not catch it because the links are real. The rosters therefore name
`(kind, field)` pairs, restricted to ACTS-class cells — **reviewed 2026-10-28: this filter is not enough.** `Person.body`, `Rung.stores` and `Site.condition` have steps `[MAT, RES, …]` and class `MATTER/ACTS` (`write_matrix.yaml:166-172`, `:357-363`, `:375-381`); MATTER rewrites them every season with `causes` chained to the subject's previous emission (`loop/matter.py:608-616`, `:660-698`, `:765-770`), so clauses (3) and (4) can be met by MATTER bookkeeping — the hole v1 had, one barrier over. Key the roster on the WRITE's class (`token.write_class`, `state/world.py:1106`) or on the Receipt's `driver` (`state/carriers.py:187`) `[ASSUMPTION: one of the two is readable at the instrument]`, not on the field name. The built reader `harness/arc.py` (B10-02, #509) states the same limit and defers it ("NOT DONE HERE, AND SAID"); its tests (`engine/season/tests/test_cl_thrust_b01_arc_reader.py`) plant cases (i)–(vi) and both nulls but no MATTER-chained case. As first drafted (rows of `write_matrix.yaml` whose `steps`
include `RES`), and exclude by name `claim_ledger`, every INTERIOR (`WIT`) cell and `Person.travel_leg`:

| Roster | First reading `[ASSUMPTION; Jordan to correct]` |
|---|---|
| `ARC_SELF` | `Tenure.since/until/term/degree` (own holdings and obligations), `Person.capability`, `Person.stance`, `Person.pursuits` (own) |
| `ARC_WORLD` | `Record.exists/stages`, `DocketItem.*`, `Site.condition`, `Rung.exists/stores`, `Office.exists/remit_acts`, and `Tenure.*`, `Person.stance`, `Person.pursuits`, `Person.body` on a record that is not `p`'s |

Home: a new roster `arc_effect_fields` in `rosters.yaml` beside `goal_object_kinds`; the loader refuses a
pair that is not a key of `write_matrix.yaml`, a pair with no `RES` step, and `claim_ledger`.
`Person.exists` (a death) is counted separately in every B6 reading (§8), never as the arc's world effect.

**Read at the driver, not from a finished log.** The question an act answered lives on the driver's
`Scene`, not on the World (`state/carriers.py:574-584` [c]; the reader is `harness/soak.py`'s
`_occasion_row`, `:139-144`, `:262` [c]), and an act formed from a `need` question cites no occasion
(`world_q.py:2947-2948` [c]). Clause (1) is therefore read by a driver-side instrument like `soak`,
not by a pure read over the log. (v1's "pure read over a finished world" was false.)

**What the predicate refuses.** Talk alone is not an arc: `tell`, `examine`, `interview`, `research`,
`surveil`, `thread_read`, `reconstruct` write nothing but WITNESS deposits, which the rosters exclude.
Talk that leads someone ELSE to write (a judge's `determine`, a conferrer's `confer`) is an arc through
clause (4). **The static check is deleted.** v1 proposed a loader refusal on a stage's `advanced_by`
verbs. Nothing in the game reads that field (§3.2 step 3), so the refusal guarded a process-only
artifact, which CLAUDE.md §0.1 pt 5 forbids, and it contradicted v1's own axis C (whose short stage is
write-less). Thirteen of the 56 verbs write nothing in any band (`verb_table.yaml` lines 238, 418, 447,
772, 1043, 1189, 1296, 1446, 1467, 1483, 1508, 1531, 1546, counted by two readers).

**The user's other guides, mapped (no new object for any of them):** *character ambitions* = Thrust;
*office duties* = seat-attached goal rows (`org: {seat: …}`, schema `goals.yaml:16`; 2 authored) plus
tier-1 purview attention; *faction goals* = faction/body rows (36 of 38); *settlement challenges* =
the existing occasions; *settlement/cohort identities* = stance, plus one schema gap (§2.3: cohorts
hold no `commit`, `harness/populated.py:394-398`); *arc decks* = a WORLD-GEN assignment of ladders to
persons (§2.2 `deal:`), never a per-season deal.

---

## 2. Data — where the head of every fact lives

Every fact below is YAML under `engine/season/` read by code (CLAUDE.md §0.05 cl. 1). No `.md` is the
head of anything. **One parser:** `data/goals.py` (the goals carrier's "ONE LOADER", `data/goals.py:1`)
gains the new keys; no second reader of `goals.yaml` is written (§8).

### 2.1 The axes roster — `engine/season/rosters.yaml`

A closed set belongs in `rosters.yaml`, where `goal_object_kinds` (`rosters.yaml:1811`) and
`goal_derivations` (`:1836`) already live and are read through `roster()`/`require_member`
(`data/goals.py:122`, `:273`). New roster `thrust_axes`:

```yaml
thrust_axes:
  values: [suppress_einhir_revival, hide_thread_truth, overthrow_church, overthrow_caste,
           purge_altonia, political_authority, faction_standing, community_benevolence,
           heal_calamity, revive_einhir]
  opposes: {suppress_einhir_revival: revive_einhir, revive_einhir: suppress_einhir_revival,
            hide_thread_truth: reveal_thread_truth, overthrow_church: uphold_church,
            overthrow_caste: uphold_caste, purge_altonia: altonian_ascendancy}
```

`[ASSUMPTION]` that the opposite poles that are not among the user's ten (`reveal_thread_truth`,
`uphold_church`, `uphold_caste`, `altonian_ascendancy`) are roster members too, so a row on either
side can be tagged. The user said the list is "not exhaustive"; the roster is closed but editable.

### 2.2 Extensions to `goals.yaml` (one file, one loader)

| Key | Where | Shape | Loader REFUSES (by name, `_refuse`, `data/goals.py:66`) |
|---|---|---|---|
| `axis:` | optional, on a goal row | a `thrust_axes` member | a non-member; an `orientation` row carrying `axis:` (it mints no Proposition, `goals.yaml:24`, so no one can be committed to it: a thrust about nobody) |
| `ladders:` | new top-level list | rows below | a missing `ladders:` key is read as `[]` — a NEW choice: the precedent REFUSES a missing `goals:` list (`data/goals.py:247-250`, `Unspecified`), so `ladders: []` would have to ship in the file as `goals: []` does |
| `ladders[].id` | | unique string | a repeat (`Forbidden`, `data/goals.py:257-260` precedent) |
| `ladders[].for` | | non-empty list of goal ids | a non-goal; an `orientation` goal; two ladders claiming one goal (one ladder per thrust) |
| `ladders[].stages[]` | ordered, ≥ 2 | `{id, term, predicate, pursuits, deadline}` | see rows below |
| `stage.term` | | `short` \| `medium` \| `long` | a non-member; a ladder whose terms DEcrease |
| `stage.predicate` | | a cell in the `requires_typed` grammar with `of: subject`; **R1 binds `subject := each referent` of the thrust** (the closed operand set `requires_operands` has no `referent`, and `build_typed_requires` exits on any other operand: `data/requires.py:973-978`, `rosters.yaml:1847-1854` [c]) | a cell the builder refuses (it raises `SystemExit`, not `Unspecified`/`Forbidden`, so the loader wraps it into its own refusal and the test asserts the wrapper); a stem in `WORLD_ONLY_STEMS` (`data/requires.py:817`), because the stage is read person-side (§3.1) and `with`/`audience` always read UNKNOWN there |
| `stage.pursuits` | | `{<pursuit>: w>0}` | through `data/pursuits.py::pursuit` (`data/goals.py:167-179`'s check, reused) |
| `stage.deadline` | | seasons ≥ 1, or `null` | `0`, a negative, a non-integer |
| `ladders[].closing` | | `{form: docket \| covenant \| arrangement \| none, arrangement: <id>?}` (succession is IN-61's, §4.3) | a non-member; `form: arrangement` naming no row of `arrangements.yaml` (`data/arrangements.py`, the ONE loader, `arrangements.yaml:4`) |
| `ladders[].successor` | | `{on_met: <goal id>\|null, on_failed: <goal id>\|null, failed_when: <predicate>\|null}` | a non-goal; an `orientation` successor; a successor cycle of length 1 |
| `ladders[].deal` | | `{weight: >0}` | the world-gen "arc deck": weight with which a person committed to a `for:` goal is dealt THIS ladder when a goal has more than one candidate ladder. ⚠ Only if two ladders per goal is wanted; v1 refuses it (one ladder per goal) and keeps the key reserved |

Why the stage predicate reuses the verb grammar: a second predicate language for stages would be
*shape divergence* (CLAUDE.md §10). Its limits are therefore the ladder's limits and are named as GAPS
in §6: `REQUIRES_STEMS` is closed (`data/requires.py:794-797`); the grammar has `all` and no `any`/`not`
(`release`'s note in `verb_table.yaml`); and binding `subject := referent` is a **Layer 1 question**
(§8), not a settled reuse.

### 2.3 One schema gap outside `goals.yaml`

Cohorts (37 of 80 persons in the measured run, `proposals/2026-10-13-narration-mechanisms.md:51`)
hold no `commit` and no pursuits by design (`harness/populated.py:394-398`: *"inventing convictions
for a population would be authoring a creed nobody wrote"*). A settlement/cohort identity thrust
therefore needs an authored org kind `org: {rung: <populated rung>}` (the cohort's synecdoche rung,
`cohorts.yaml`) that `seed_goals` commits the cohort to. That is AUTHORED CONTENT, not invention; until
a row is written, axis 8 has no cohort climber. Loader refusal: a rung not in `cohorts.yaml`.

---

## 3. Runtime

### 3.1 No new source, no new verb, no stored progress

Today: Q4 forms one `need` question per ambition whose `goal_referents` is non-empty
(`world_q.py:2833-2841`); `attention_key` puts it in tier 3 (`world_q.py:2582`, `:2659-2660`); the
aggregation rule `first` (`data/fixtures.py:481`; `decision/questions.py:62-63`) delivers only `out[0]`.
The layer changes three things, all inside `queries/world_q.py`, beside the owners they extend:

| Change | Owner it extends | Stored? |
|---|---|---|
| **R1** `current_stage(w, p, amb)` → the first stage of the ambition's ladder whose `predicate` is not TRUE for each referent, read through `p`'s own `LedgerReader` (person-side, AX-2); `None` when the ladder is complete or the ambition has none | new function beside `goal_referents` (`world_q.py:2207`) | **no** — computed when asked, `ambitions`' discipline (`world_q.py:2172-2173`) |
| **R2** the `need` question's referents = `goal_referents` ∪ the stage's referents, **passed through `_stamped`'s classes** (`world_q.py:2889-2897`) so that a seat reaches `confer` (which forms only on Office-classed referents, `verb_table.yaml:266-267` [c]) and an unclassed verb does not form on an office id (that would add to S1); the stage's `pursuits` join the salience target as a goal's do (`world_q.py:2643-2647`) | Q4 loop (`:2837-2841`) and `salience` | **no** |
| **R3′** a `need` question is promoted to **tier 0 for one season in every `deadline`**, never as a standing promotion: when `(w.tick + phase(p)) % d == 0`, `phase(p)` a keyed draw `draw(p.id, "stage_phase")` in `[0, d)` (the per-candidate keyed-draw idiom of `decision/choose.py:350-388`). Promoted only if (i) the person's salience for that ambition is ≥ 0 — a head whose pursuits point against his org answers his own want first, A-33 / IN-69 (`workplans/valoria_master_workplan_v9_part5.md:178`) — and (ii) at least one candidate forms on the stage's referents (a detained holder's due stage forms only acts the custody decline refuses, `verb_table.yaml:913` [c]) | `attention_key.key` (`world_q.py:2659-2660`) | **no** |

**Why R3′ is a pulse and not "due = since + Σ deadline".** v1's rule was met by every committed person on
the same tick: goal commits are minted at `since` 0 (`harness/populated.py:709`,
`Tenure(f"t_{g.id}_{pid}_commit", pid, g.id, "commit", 0)`), and a due stage stayed due until its
person-side predicate turned true. With `commit`, `determine` and `confer` refused on every attempt in
the measured run (`narration-mechanisms.md:47` [c]) stages stay unmet, so v1's R3 converged on the
unconditional tier-0 arm that starved news (`world_q.py:2608-2612`). The pulse expires; the stagger
removes the world-gen synchrony (the pulse hazard the narration proposal names, `:315` [c]).
`[ASSUMPTION]` a keyed phase is architecture-right; the alternative (date a stage from a term an act
declared, as `oblige`'s `matures_at` is) waits on `oblige` executing.

**Why progress is a query, and how that squares with ED-IN-0225.** ED-IN-0225 (archive row,
`registers/archive/editorial_ledger_in_archive_pre-2026-09.yaml:3209-3237`) closed the question *"what
is an arc, as a thing the engine holds"*, with the absence of a carrier **and a type**. This design
builds no runtime carrier: no arc store, stage counter or per-person ladder field. It does add a TYPE
(authored `ladders:` data, like a goal row) and it names that as a narrowing (§9). The current stage is
a read over the person's own ledger, recomputed each time; the arc is a predicate read by a driver-side
instrument. If every `ladders:` row were deleted the world would run as today.

**Why person-side.** A person acts on what he believes his progress is. Reading the world would hand him
facts no channel delivered — the hazard `goal_referents` records for `seat_holders`
(`world_q.py:2224-2230`, ED-IN-0292 (2) on the queue). A false belief about one's own stage is a story,
not a defect.

### 3.2 How a stage advances, using existing machinery only

1. The person's `need` question names the stage's referents (R2).
2. `opening_set` (`decision/options.py:56`) forms candidates over every verb × referent, as now.
3. The stage's `pursuits` tilt salience and, through the alignment cells, the chooser's score — the
   canonical fifteen, not a verb whitelist (a whitelist is a script).
4. `choose` samples by Plackett-Luce over `softmax(score/τ)`, τ = `choice_temperature` 0.1
   (`decision/choose.py:264-266`, `:350`; `data/fixtures.py:286`). Unchanged.
5. The act resolves through the fold; WITNESS deposits claims; the stage predicate reads them next
   season. Advancement is never written.

### 3.3 The starved `need` question — the fix, its instrument and its controls

Measured (one seed, two seasons, uncommitted scratch instruments): of 803 deliberations 686 took a
`claim_landed`, 51 a `need`, 66 none (`narration-mechanisms.md:55`; **superseded as the baseline** by `01_MISSING_IN_CODE.md` P2: five seeds, counted per scene, `need` 149–174 of 606–642, about a goal 43–53). Putting `need` in tier 0
unconditionally starved news (`world_q.py:2608-2612`: events 21,735 → 15,738, `news.told` 14 → 7).
**Take R3′, not a global re-tier and not `one_per_source`** (which delivers one question's `about`, so an
act's occasion attribution breaks: the narration proposal's D-J, `:314` [c]).

**The instrument did not exist when this was written (B0.2); B10-02 (#509, `be24c71e`, 2026-10-27) has since landed `harness/aperture.py`'s pooled, answered-by-source block and a generalised `harness/arms.py` arm (the register's G-08, G-11, G-12).** `harness/arms.py` is wired to one mechanic,
`field_casualty_model`, and returns act-subject tallies only (`arms.py:135-170` [c]); its default run is
two seasons (`:236` [c]); the 51/803 baseline is from a scratch run and is superseded (`01` P2). B0.2 commits a harness that reports,
per arm and seed: the `need` share of deliberations, `news.told`, and the **stage-referent hit rate** — the
share of promoted `need` questions that formed a candidate AND whose act executed (not refused). Run
length is at least twice the largest authored `Σ deadline`.

**Controls.** (a) `ladders: []` → R1/R2 inert → `World.content_hash()` byte-identical. (b) **Ladders
authored, R3′ off vs on** is the R3′ control. (v1's "`deadline: null` reproduces today's hash" was wrong:
R1/R2 move the hash once any ladder is authored.) **Falsifier:** with R3′ on, `news.told` falls by more
than the arms' own seed-to-seed spread, or the stage-referent hit rate is at the refusal floor → R3′ is
the `:2608-2612` failure again and is reverted. "The `need` share rises" is NOT a falsifier: once R3′
promotes it cannot fail.

### 3.4 Stored vs derived

| Stored (already) | Derived (new reads) | Authored (new data) |
|---|---|---|
| `commit` tenures and their `since`; Propositions; ledgers; the log; dockets; tenures | current stage; due-ness; stage referents; ARC(p, a) | axes roster; `axis:`; ladders |

Thrust succession is by the person's own acts: when `current_stage` is `None` (met) or the ladder's
`failed_when` holds, the `need` question carries the `successor` goal's Proposition as a referent, so
`commit` (writes `Tenure.since`) and `release` (writes `Tenure.until`, `commitment.ended`) can form. No
row releases or commits for him.

---

## 4. Closure engines — lawful forms only (no outcome written by a non-person)

The corpus says most authored endings are a choice forced by a crossing: DECIDER 20, ROLL 9, THRESHOLD
8, NEVER 10, UNCLEAR 3, with *"a crossing FORCES the moment even where a person makes the final call"*
in 19 of 50 (`engine/season/ENDINGS_CLASSIFIED.yaml:13-23`; an agent's blind classification of prose,
its own weakest-evidence label, `:6`). The engines below give that shape lawfully.

| Engine | Existing verbs / stores | New piece | Forbids |
|---|---|---|---|
| **4.1 Threshold-raised docket matter** | `open_case` (remit:determine; writes `Record.exists/stages`, `DocketItem.*`), `convene` (`Date.due_at`), `determine` (contested; Success/Overwhelming write `Tenure.since`, `DocketItem.matter`, `Tenure.degree`, `Person.pursuits`; opens the `disposes:` kind — `oblige`, `detain` or `ban`), `speak`, `argue`; the bench question `sittings_before` (`world_q.py:2843-2860`) | a MATTER step `_docket_crossings` on `_standing_crossings`' exact shape (`loop/matter.py:187-240`): for a seated person with `open_case` in his grant, when the deed claims in HIS OWN ledger, against one doer, of kinds named by the `deed_doers` goals **of his seat's body or faction** (only two seat rows exist, `goals.yaml:449-472`, so seat-keyed would fire for nobody) cross a band (fixture floors; `()` = control, the `standing_band_floors` precedent, `data/fixtures.py:445-446`), log one Event with no Receipt minted, causes = those claims' deposits; `questions_for` raises a `claim_landed` question to him about the doer. Per the critic `determine` decides only in hand-built worlds (H-163 [c]) and was refused 7 of 7 (`narration-mechanisms.md:47` [c]): this engine inherits that floor (§7 S2) | the crossing writing anything (L5, `loop/matter.py:79`, *"MAY NEVER PRODUCE AN OUTCOME"*); opening the case for him; a judge chosen by the engine; a verdict not rolled |
| **4.2 Bound peace** | `covenant` (remit:issue; `Record.exists/stages`), `commit` by the counterparty, `oblige` with a declared term (`Tenure.term`), `release`, `evade / defy` (`compliance.withheld`) | **a NEW person-side reader** keyed on `(verb, referent)`: a person does not form `fight`/`challenge`/`accept` on a referent a covenant he is committed to names; breaking the peace takes a prior witnessed `release`. v1 said to compose on `held_document_declines`; that roster maps a verb to a record kind and declines the verb outright while the person holds such a document ABOUT HIMSELF (`rosters.yaml:2020-2033`; `decision/options.py:857-874` [c]), so it cannot name a referent — composing on it declines `fight` against everyone, or needs the new shape this row now names. Layer 1 question (shape divergence) | a peace imposed by the engine; a peace that cannot be renounced; reading Record content at the FOLD (K-52, `arrest`'s note) |
| **4.3 Succession** | **IN-61 owns it** (`workplans/valoria_master_workplan_v10_part4.md:575-579`, RULED RS-27: *"designated heir is not a verb but a status or title. the heir still has to claim their throne"*; designation is `confer` of the heir seat; the claimant is the title-holder; FALSIFIER: a `confer` of the vacant throne by the Widow Regent admitted → fail). `succeed` is `Person → Person`, owned by the holder, and the death cascade closes it (`architecture/meta/04_CODE_ARCHITECTURE.md:195`), so it is never live at the vacancy | **nothing in this design.** v1 proposed a `succession` gate basis on `confer` keyed on a live `succeed` tenure to the vacant seat; that is the carrier Jordan rejected and duplicates IN-61. A ladder whose closing needs a succession depends on IN-61 | any succession path other than IN-61's |
| **4.4 Authored set piece** | `arrangements.yaml` — the FORM (`legal_trial` `:177`, `tribunal` `:200`, `inquisition_hearing` `:234`, `excommunication_deliberation` `:265`, `council_of_state` `:145`…), `convene`, `speak` (contests "a matter"), `determine` (contests "a proposition") | `closing: {form: arrangement, arrangement: <id>}` on a ladder: the ladder's last stage is read as met when the stage predicate reads a determination under that arrangement (a *stem for "determined under arrangement X" does not exist* — GAP, §6) | a dated pin (T-c; #457 cuts *"a scripted invasion or other dated pin"*, cited at `research/by_lane/WR_world.md:270`); an authored winner; a set piece convened by no person |

A `challenge` → `accept` duel is NOT offered as a closure engine yet: `accept` cannot read that a
challenge was made (`verb_table.yaml:796`, measured 0 of 12 executed accepts had the challenge in the
acceptor's ledger). It is a substrate repair (§7 S9).

---

## 5. The three constraints as mechanisms

### 5.1 Death is rare

**Today death is not rare.** The corpus run behind `attention_key`'s note shows *"combat high (felled
82, wounded 116 against base 47/66)"* (`world_q.py:2616-2618`). Every `Felled` band of `fight` and
`accept` writes `Person.exists` and the cascade deletes the person (`verb_table.yaml:716`, `:802`;
`loop/effects_combat.py:160-178`, through `World.remove_person`, the one owner of death).

| Route to death | Today | Proposed |
|---|---|---|
| `fight` / `accept`, `Felled` band | deletes the subject | **`Felled` = down, alive**: writes `Person.body` only, emits `body.changed`. A NEW band `Slain`, worst-first in `rosters.yaml: combat_band_edges` (`:823`; bands are data, `seam/ladder.py:147-154`), on a quantity the scene's `WoundTracker` returns, keeps today's three writes and `person.died`. The edge value is Jordan's (§10 D1). `[ASSUMPTION]` the tracker exposes a quantity that separates "down" from "dead" (`health_remaining` is read for magnitude, `verb_table.yaml:720`); if it does not, `Slain` has no source and must not be invented — then `Felled` stays lethal and §5.2 carries the whole constraint |
| a yield (`result["surrender"]`, `seam/ladder.py:142-145`) | the yielder reads `Untouched`/`Wounded`; nothing reads the surrender | unchanged here; a later position may let a yield open an `oblige` to the victor (bound peace, §4.2) — not v1 |
| field battle (`march`) | kills only under `field_casualty_model: total`; shipped `scaled_by_degree` floors body at 1 (`data/fixtures.py:654`; `loop/effects_combat.py:317-326`) | unchanged |
| MATTER hunger / bodies pass (`loop/matter.py:243` `_die`) | named persons exempt from the larder draw (ED-IN-0255, per `research/by_lane/WR_world.md:276`); `body_step=0` (`data/fixtures.py:594`) | unchanged |
| ageing / illness | `age_step=0.0`, `illness_rate=0.0`, `age_at_build=0` (`data/fixtures.py:606-608`) | unchanged; ageing is a succession source once ages are authored (§7 S5) |

### 5.2 The standing gate — composed on the access gate that already exists, and honest about its reach

The tree already has RS-26's access gate: `admits_audience(w, actor, rung)` (`world_q.py:1295-1344`),
four limbs (unguarded / own seat / an oath / a writ), over `guard_weight` (`world_q.py:1250-1277`:
the sworn weight present with a principal; *"a duke is easier to reach than a king only because less
sworn weight stands at his home -- data, not a table"*). It gates `move`/`migrate`
(`verb_table.yaml:903-913`); `fight`'s own cell gates only co-location (`verb_table.yaml:653-660`).

**Its reach is three principals.** Guards are seated only by `build_realm(guards=True)`, and
`cohorts.yaml:127-130` authors three guard rows (`off_king`, `off_duchess_hafenmark`, `off_duke_varfell`)
of 31 seats. Limbs 2 and 3 admit ANY seat-holder whose purview reaches the rung, and anyone sworn to such
a seat (`world_q.py:1305-1315`). The seats the user means by "authority" include the Cardinal of
Justice, the Senior Inquisitor, the Confessor and the Restoration leader, which are the referents of the
−1 `seat_holders` goals whose own comment declares the risk: *"`fight` forms on them, so violent attempts
can rise"* (`goals.yaml:159-163`). Those seats are UNGUARDED, and R3′ promotes exactly those `need`
questions. The gate as built binds nobody who matters to the user's rule.

| Piece | Where it lives | Existing or new |
|---|---|---|
| **G1** seat the guard cohorts by default (`guards=True`) AND **author guard rows for every seat that is the referent of a −1 `seat_holders` goal, and for each faction head** (weights `[ASSUMPTION; Jordan to correct]`, the `cohorts.yaml:123-126` precedent) | `harness/populated.py` flag; content `cohorts.yaml` | existing flag; NEW content; a content-hash move to declare |
| **G2** a third conjunct on `fight`, `challenge`, `accept`: `relation of: subject, relation: audience`, re-asked at the act (a guard posted after the attacker arrived bars him) — refusal keyed `audience` | `verb_table.yaml` rows; the `audience` branch of `WorldReader.read` (`world_q.py:3203-3210`) accepting a PERSON subject read through `place_of` (today a non-rung subject reads UNKNOWN) | new conjunct on an existing stem; a reader widening — **Layer 1 question** |
| **G3** the residence limit — a household member cannot return home past his own lord's guard (`world_q.py:1323-1327`) | a fifth limb in `admits_audience` | named limit, fixed before G1 or G1 strands households |
| **Measure** harm aimed at seat-holders per run, `guards` off vs on, same seeds | instrument B0.2 | the control is `guards=False` (today's behaviour) |

The gate stops an outsider at the door; once co-located with an official, `fight` forms. It is a
deterministic refusal, not a hidden die: a roll no person made is an outcome no person wrote.

**The non-violent weapons** (all existing rows; writes from `verb_table.yaml`):

| Verb | Eligibility | Writes / effect | Role |
|---|---|---|---|
| `tell` | own | writes nothing; deposits at WITNESS; contests "a standing" | spreads the accusation |
| `petition` | own | `Record.exists` (to a named person) | puts it before a judge |
| `argue` | own | hearer's `Person.pursuits` on Success/Overwhelming | turns a bench |
| `open_case` | remit:determine, purview | `Record.*`, `DocketItem.*` | the tribunal (§4.1) |
| `issue` → `arrest` | remit:issue → remit:dispatch, warrant-sourced (`rosters.yaml:1913`) | `Record.exists` → `Tenure.since` (`detain`) | the only lawful hands on authority; `arrest` contests "a standing" |
| `construe` | own | **none, and `grade: absent`, `requires_typed: none`** (D18) | ⚠ NOT a weapon today, despite the brief listing it; repair or drop |

### 5.3 A killing has significant consequences — on existing carriers, two of them mute today

| Consequence | Carrier | State |
|---|---|---|
| witnesses condemn the killer | WITNESS deposits `person.died`; `paired_deed_term` scores it by `\|lean·bond\|` (`world_q.py:2572-2581`; `_bond`, `queries/person_q.py:350-361`: full allegiance doubles a condemnation) | ⚠ **MUTE**: *"a dead victim's `person.died` never reaches the question set ... a dead man has no place: H-209"* (`world_q.py:2579-2581`; `hole_register.yaml:4539`). §7 S6 |
| the protectors act | `goal_riskbreakers_prevent_threats` (`deed_doers against goal_riskbreakers_royal_safety`, `goals.yaml:97-100`) makes the killer a referent | works for the four royal seats only |
| the seat falls vacant | the cascade closes the `hold`; `vacancies` gives conferrers the seat (`world_q.py:2386-2408`) | ⚠ the office half is **absent**: the vacancy is named by no claim (H-206, `hole_register.yaml:4500`; `WR_world.md:276`). §7 S7. Hereditary succession is IN-61's (§4.3) |
| kin take up a thrust against the killer | a kin's `utter` + `commit` to an OUGHT about the killer | ⚠ act-minted Propositions carry predicate `''` (52 of 52, `narration-mechanisms.md:49`): a vengeance thrust has no content. GAP |
| a tribunal | §4.1's docket crossing counts the paired-kind claims against the killer in a judge's own ledger | NEW (§4.1) |

---

## 6. Per-axis ladders, ordered by buildability

Stage predicates use stems of `REQUIRES_STEMS` (`data/requires.py:794-797`); a stem not there is a
GAP. "Self" and "world" name the writes that would satisfy §1.2 (2) and (3). Opposing rows are
`goals.yaml` ids. ⚠ An `orientation` row mints no Proposition and so produces **no thrust at all**
(`goals.yaml:24`; `goal_referents` → `()`, `world_q.py:2222`): every axis whose only row is an
orientation needs a referent-bearing row before a ladder can attach.

**A · 6 political authority** — rows: `goal_crown_peninsular_sovereignty` (seat_holders `off_king`,
+1), `goal_varfell_southernmost_dominion`/`_oastad_gate` (rung), `goal_katepano_press_the_capital`
(rung). Opposing: `goal_altonia_conquer_valoria` (rung `r_valoria`, −1), Hafenmark's dynastic rows.
Short: `confer` a vacant seat to an ally (predicate `held_by` on the seat). Medium: `covenant` with a
rival (`Record.exists`) or `oblige` a subordinate (`Tenure.since/term`). Long: `establish` an office
(`Office.exists`) or `march` to hold a rung (Won: `Tenure.until/since`, `Rung.stores`). Closing:
covenant (§4.2) or succession (IN-61, §4.3). Self: the actor's seat gains obliges, a treasury (`Rung.stores`).
World: others' tenures. Gaps: `confer` and `revoke` refused on every attempt in the measured run
(`narration-mechanisms.md:47`); `at_war` False for every pair (`WR_world.md:276`).

**B · 8 community benevolence** — rows: `goal_knights_of_the_peace_patrol`,
`goal_guilds_commerce_sustained`, `goal_cardinal_prudence_tithes` (all orientation). Opposing: none.
Needs a `rung`-kind row (`object: {kind: rung, rung: <settlement>}`, stance +1; kind exists,
`goals.yaml:21`). Short: `tend` (`Person.body`), `restore` (`Site.condition`). Medium: `transfer`/
`give` stores (`Rung.stores`, `Tenure.until/since`). Long: `build`/`found` (`Site.exists`,
`Rung.exists`). Closing: none needed — a THRESHOLD on the rung's `stores`/`condition` stems. Self: the
giver's own stores fall; world: the rung's rise. Gaps: hunger dark (`body_step=0`), so no challenge
presses; `work`, `build`, `found`, `give` refused on every attempt (`narration-mechanisms.md:47`).

**C · 1 suppress Einhir revival** — rows: `goal_church_root_out_heresy`, `goal_inquisitors_find_heresy`
(deed_doers engaging `einhir_restoration`), `goal_church_suppress_restoration` (seat_holders
`off_restoration_leader`, −1). Opposing: axis 10. Short: `interview`/`surveil`/`examine` — write
nothing; predicate `claim.held` on the referent (findings are claims). Medium: `issue` a warrant →
`arrest` (`Tenure.since`, `detain`). Long: `open_case` + `determine` under `inquisition_hearing`
(`arrangements.yaml:234`). Closing: docket (§4.1). Self: promotion by a superior's `confer`
(cross-person; satisfies (2) through (4)). World: the accused's `detain`/`ban`/`oblige`. Gaps: no
`detain` relation stem (a `tenure:<kind>` stem is a grammar change); `determine` refused on every
attempt (`:47`).

**D · 7 faction standing** — rows: the 2 seat rows only (`goals.yaml:449-472`). Short: `oblige` to a
seat (`Tenure.since/term`, `duty.taken`). Medium: `petition` the conferrer (`Record.exists`) so he
is a referent. Long: be `confer`red a higher seat (predicate `held_by` + `rank`). Closing: succession
(IN-61, §4.3). Self: his own `hold`. World: the seat's purview. Gaps: ⚠ "standing" collides with
`standing_of` (D-4 pressure, `loop/matter.py:190`): name the axis `faction_rank` in code (CLAUDE.md
§4 word choice); a conferrer's `confer` subject is drawn from referents, so a petitioner who never
reached his ledger is never chosen.

**E · 10 revive Einhir heritage** — rows: `goal_restoration_einhir_revival`,
`goal_restoration_practitioners_protected` (orientation); `goal_restoration_evade_capture`
(seat_holders, −1) is the only thrust-bearing row. Opposing: axis 1. Short: `utter`/`argue`
(hearers' `Person.pursuits`). Medium: `found` a commune (`Rung.exists`). Long: a covenant of
protection from Hafenmark or the Crown (§4.2), or survive an `excommunication_deliberation`
(`arrangements.yaml:265`). Gaps: the referent-bearing row; `thread_read` needs a TS carrier
(H-85, `WR_world.md:275`); `tie / knot` has no opener (`rosters.yaml:141-143`).

**F · 5 purge Altonian influence** — rows: `goal_crown_resist_altonia` (orientation). Opposing:
`goal_altonia_conquer_valoria`, `goal_katepano_press_the_capital`, `goal_kommerkiarios_treaty_order`.
Needs a seat_holders row on `off_katepano`/`off_kommerkiarios`, −1. Short: `surveil`/`interview`.
Medium: `seize` records (`Tenure.until/since`) / `arrest` Altonian agents. Long: `march`. Closing:
covenant or field. Gaps: Altonia exists only in a `foreign=True` world (`world_q.py:2188-2189`);
exogenous motion is dark (T-WR-8), so Altonia never presses.

**G · 3 overthrow the Church** — row: `goal_hafenmark_church_influence_suppressed` (seat_holders
`off_confessor`, −1). Opposing: `goal_church_solmundan_orthodoxy`, `goal_holy_see_orthodoxy`.
Short: `argue` churchmen. Medium: `forge`/`destroy_record` (`Record.*`), `petition` the Crown.
Long: `open_case` against the Confessor; `determine` disposes `oblige`/`detain`/`ban`, never `revoke`.
Gap: Church seats are strippable by nobody — 16 of 31 seats carry `revocation: null`
(`offices.yaml` `seats:`, counted by the producer), seven of them by Jordan's ruling
(`offices.yaml:66-75`). "Overthrow" therefore has no terminus but a ban or a march. ⚠ The header's
*"14 of 29"* (`offices.yaml:64`) is stale against the file's own 31 rows; the data rows are the owner.

**H · 2 hide threadwork truth** — no row; `goal_varfell_thread_knowledge` is the opposite pole
(orientation, `goals.yaml:340-348`). Short: `conceal` (`Record.exists`); medium: `seize`/
`destroy_record`; long: hold every copy (predicate `held_by` on each Record). Gaps: the holder — answered from canon (§10 D2): the Church; the row is still to be authored; 112 of 120 Records are `text` with no `subject_matter`
(`narration-mechanisms.md:50`), so "a record of the thread truth" is not yet a thing.

**I · 4 overthrow the caste system** — row: `goal_restoration_caste_ended` (orientation); no defender
row. Canon: the caste is *"informal ... not a formal legal act"*, a geographic gradient of stigma
(`canon/03_canonical_timeline.md:94-100`). No engine code holds caste (`grep -rniw caste engine/season --include=*.py` (0 hits; a bare `-rni caste` also matches `Dicastery`: 81 hits in 24 files)
finds only `goals.yaml` and case files). Only `argue`/`utter` can move it, and nothing can observe the
end. Gap: no end can be observed until caste is a read (§10 D3: a Query over the affiliation convictions, no store).

**PC entry.** A player character is a Person like any other. His thrust is a `commit` the player makes
(or the lifepath assigns); the ladder only ORDERS the questions offered to him (attention), never his
choice; his stage is read from his own ledger. `[ASSUMPTION]` — `player_agency_v30.md` was not read.

**J · 9 heal the Calamity** — no row, no act: threadwork is *"built and inert"* and the Calamity *"run
zero times"* (`WR_world.md:275`, `:279`); `restore` cannot be told from mending a wall
(`WR_world.md:286`). Unbuildable in this layer; blocked on a thread-operation act (IN-35/IN-06).

---

## 7. Substrate repairs that gate the layer

| # | Repair | Evidence | Blocks |
|---|---|---|---|
| S1 | candidate typing: `opening_set` loops every verb over every referent with no kind filter | 28.7% of attempted acts at 4 seasons (32.2% at 2) are refused at admission on a subject that lives in another collection, per act, five seeds (`01_MISSING_IN_CODE.md` P10); the scratch figure 439 of 1,318 (33.3%) (`narration-mechanisms.md:45`) is SUPERSEDED | every stage: a `need` question whose referents feed the wrong kind wastes the scene |
| S2 | refusal rate | 76.2% (2 seasons) and 76.8% (4 seasons) of attempted acts refused on the driver's definition, five seeds (`01` P1); closers at 4 seasons, executed/attempted: `determine` 3/43, `confer` 10/111, `covenant` 0/70, `revoke` 0/32 (`01` P1). The scratch figures 929 of 1,318 (70.5%) and `determine` 7/7, `confer` 4/4 (`narration-mechanisms.md:41`, `:47`) are SUPERSEDED | every closure engine in §4 |
| S3 | need starvation | `need` scenes 149–174 of 606–642 (24–28%) per seed, about a goal Proposition 43–53 (7.1–8.5%) (`01` P2); the scratch figure 51 of 803 (`narration-mechanisms.md:55`) uses a different denominator (deliberations) and is SUPERSEDED | the thrust is never attended (§3.3) |
| S4 | exogenous motion dark | `season_factor_draw=()`, `body_step=0`, `age_step=0.0`, `illness_rate=0.0` (`data/fixtures.py:469`, `:594`, `:606-607`) | challenges, vacancies, Altonian pressure |
| S5 | ageing has no input | `age_at_build=0`; ages unauthored (`data/fixtures.py:603-608`; `WR_world.md:276`) | natural succession; switching ageing on now ages everyone from 0 |
| S6 | H-209: a death never reaches the question set | `world_q.py:2579-2581` | §5.3 consequence |
| S7 | H-206: a dead holder's seat is named by no claim | `hole_register.yaml:4500`; `WR_world.md:276` | succession as consequence |
| S8 | `succeed`, `tie`, `knot` have no opener; succession is **IN-61** (RULED RS-27), which this design depends on and does not duplicate | `rosters.yaml:141-143`; `workplans/valoria_master_workplan_v10_part4.md:575-579` | hereditary succession; kin |
| S9 | `accept` cannot read a challenge | `verb_table.yaml:796` (0 of 12) | the duel as decisive form |
| S11 | closure verbs refuse: `determine` 7/7, `confer` 4/4, `revoke` 4/4, `commit` 74/74 refused in the measured run; `determine` decides only in hand-built worlds (H-163 [c]) | `narration-mechanisms.md:47` [c] | every closure engine, and successor thrusts |
| S12 | S1's disposition is an UNRULED decision of the narration proposal (refusals as learning, or declined at formation) and S1 sits in no workplan position | `narration-mechanisms.md` §7 item 1 [c]; `valoria_master_workplan_v9.md` | B1.1 cannot start until it is ruled or taken |
| S10 | act-minted Propositions are empty | 52 of 52 predicate `''` (`narration-mechanisms.md:49`) | successor and vengeance thrusts |

---

## 8. Build order — positions, each with falsifier, control and instrument

Every executed test asserts it asserted (`assert checked >= N`, CLAUDE.md §0.1 pt 2). "Hash control" =
same-seed `World.content_hash()` byte-identity with the feature's data empty.

| Batch · position | Falsifier (would show it wrong) | Control | Instrument |
|---|---|---|---|
| **B0.1** ARC reader, **driver-side**, over the `arc_effect_fields` rosters (§1.2); writes nothing | planted worlds: (i) a linked self+world chain through ARC_SELF/ARC_WORLD writes reads TRUE; (ii) both effects, no `causes` link → FALSE; (iii) only write-less acts → FALSE; (iv) **a witnessed `move` → FALSE**; (v) **a witnessed `tell` → FALSE**; (vi) a `petition` answered by the conferrer's `confer` of the petitioner → TRUE through clause (4); (vii) **an act whose `causes[]` chain reaches a MATTER-written `body`, `stores` or `condition` Event → FALSE** | the shuffled-`causes` null AND a **bookkeeping null**: the same log read with unrestricted Receipts must read higher; assert that it does | new test in `engine/season/tests/` |
| **B0.2** the need/news instrument (§3.3), committed | the harness reproduces the scratch baseline's order of magnitude (need ≈ 6% of deliberations; `01` P2 reads 7.1–8.5% of scenes for a goal-about `need` and 24–28% for all `need`) on the shipped realm or reports why not | the shipped realm, ladders empty | `harness/` |
| **B1.1** S1 candidate typing — **blocked on the open S12 decision** | kind-mismatched share does not fall | same seeds, typing off | the narration proposal's measure, committed |
| **B1.2** S6, S7 — **already IN-12 step 5** (`valoria_master_workplan_v9.md:255` row; H-226, H-227, H-209); not a new position | a planted killing of a seated person reaches ≥1 witness's question set; the vacancy is named by ≥1 claim | the pre-fix log reads 0 for both | IN-12's tests |
| **B2.1** `thrust_axes` and `arc_effect_fields` rosters + `axis:` + loader refusals | each refusal row has a test that plants the bad row and asserts the loader's own refusal (the stage-predicate builder's `SystemExit` is wrapped, `data/requires.py:973-978`) | `ladders: []`, no `axis:` → hash control | `engine/season/tests/test_fa05_user_goals.py`, `test_fa06_org_goals.py`, or a new `test_thrust_ladders.py` |
| **B2.2** `ladders:` schema | a predicate using a `WORLD_ONLY_STEMS` stem is refused; a ladder on an `orientation` goal is refused; a repeated `for:` goal is refused | the shipped files pass | same file |
| **B3.1** R1 `current_stage` (person-side) | a person whose ledger holds the stage-1 claim reads stage 2; one whose ledger lacks it reads stage 1 although the WORLD satisfies it (belief, not truth) | no ladder → `None` for every ambition | targeted test |
| **B3.2** R2 + R3′ | with one authored ladder: R3′ on vs off — `news.told` stays within the seed spread; the stage-referent hit rate is reported and asserted non-vacuous | ladders authored, R3′ off (§3.3); `ladders: []` hash control | B0.2 |
| **B4.1** §4.1 docket crossing | **no Receipt is minted during the step** (assert on the gate's mint count, not a literal); an `open_case` follows only by the judge's choice | floors `()` → no crossing Event, hash control | targeted test + B0.2 |
| **B4.2** §4.2 peace reader | a committed party forms no `fight` on the named referent; after a witnessed `release` he can | no covenant held → candidate set unchanged | targeted test |
| **B5.1** §5.1 `Slain` band | Felled persons survive; a `Slain` reading deletes; deaths per run fall | edge at today's reading → today's outcomes | `test_we_a_contested_acts_consequence_differs_by_degree`'s file, re-pinned |
| **B5.2** §5.2 G1–G3 | an actor with no seat, oath or writ, co-located with a guarded principal, gets `kill.refused` keyed `audience`; a sworn man does not; **harm aimed at seat-holders falls with guards on across ALL −1-referent seats, not three** | `guards=False` → today's behaviour | targeted test; B0.2; corpus felled/wounded vs 82/116 |
| **B6.n** author ladders in §6's order, one axis per position | ARC rate for committed persons minus the shuffled-`causes` null AND minus the bookkeeping null has a CI excluding 0, AND is not carried by `person.died` (arcs whose world effect is a death are counted separately) | same seeds, that axis's ladder removed | B0.1 + B0.2 |

**Layer 1 conformance questions** (route to `layer-conformance` Lens B before building): B2.2 and R1 —
binding `subject := referent` in a typed-requires cell read person-side, and `build_typed_requires`
called outside `verb_table.yaml`; B3.1 — `current_stage` in `world_q` reading a person-side reader
(AX-2's line between `person_q` and `world_q`, `world_q.py:2175-2181`); R2 — stage referents through
`_stamped`; B4.1 — a new MATTER step writing nothing; B4.2 — a new `(verb, referent)` decline reader;
B5.2 — the `audience` reader accepting a Person subject; B0.1 — an instrument reading the driver's Scene.

---

## 9. Refusals and contraventions

**Refused by this design:** an arc carrier or stage store; any outcome written by a non-person (a
crossing writes nothing, L5); a per-season deal of arcs (the deck is world-gen only); a verb whitelist per
stage in the chooser; actor-visible forecasts; lookahead-biased choice (toy result (e), §11: it cut
explained motive, flipped ~32% of leveraged decisions and cost ~3,200 rollouts/run, and it is an actor
reading an engine forecast); a succession carrier other than IN-61's; a hidden die in the standing gate.

| Ruling | Effect | Named |
|---|---|---|
| ED-IN-0225 (*"ignore the arcs"*), as since cited as a prohibition in four `.py` files (`harness/storybar.py`, `soak.py`, `populated.py`, `chronicle.py`) | **NARROWED, in two respects.** No runtime carrier is built. But the ruling's absence was of a carrier **and a type** (archive `:3219-3221` [c]); a typed `ladders:` schema running to a `closing` form with successors is a type, authored as data. The ruling dropped an obligation; this design takes up the question | yes |
| `narration-mechanisms.md` §3.4: *"A storyline object that steers the sim — kept out"* (`:181` [c]); #457 `:190` (cut: *"an arc, story or thread carrier inside the simulation"*) [c] | **NARROWED**: a ladder steers ATTENTION (which question a person answers), writes nothing, and is not a runtime object. Its authority is Jordan 2026-08-18, *"We can script narrative hooks and sequences so long as we don't script entire arcs"* (`proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md:618`) — a ladder is a sequence of conditions; it is NOT licensed to script an entire arc, and the line between "sequence" and "arc" is Jordan's | yes |
| same §3.4: the ban on need-triggered injection and scripted beats (`:186`, `:195-196`) | **KEPT for injection** (R3′ emits nothing; it reorders a person's own questions). **NARROWED for scripted beats** (nothing in a ladder "will occur") | yes |
| `oblige`'s declared term (`term.declared_by`): a duration an ACT declared | **CONTRAVENED by R3′'s `deadline`**: the stage deadline is a term the AUTHOR declared, not an act; the pulse does not read it as a forecast of the world | yes |
| v2 R-AI — no actor resolver takes a forecast object (`narrative_engine_design_v2_churn.md:448`; not re-opened by the critic) | **KEPT** | — |
| 2026-09-03 ruling (degrees read off the scene) and `fight`'s comment *"felled -> ... This is the kill"* (`verb_table.yaml:693-694`); **and Jordan's 2026-09-04 ruling to accept the combat result, with the `Felled` edge never swept** (`rosters.yaml:837-841`; the earlier cite `04_CODE_ARCHITECTURE.md:366` does not hold it) | **CONTRAVENED in reading**: the degree is still read off the scene; `Felled` stops meaning death and a `Slain` band carries it; the `Felled` edge becomes a swept value | yes |
| `fight`'s cell note: *"A WIDER precondition — a hostility test ... — would be an invention"* (`verb_table.yaml:662`, G4) | **CONTRAVENED** by G2, on the user's instruction; composed on an existing stem | yes |
| IN-61 (RS-27), L5, ED-IN-0256, ED-WR-0011, A-31, A-33 | KEPT. R3′ respects A-33: a misaligned head answers his own want first (salience ≥ 0 gate) | — |

---

## 10. Open decisions (survivors of CLAUDE.md §0's five steps)

| # | Decision | Why it survives |
|---|---|---|
| **D1** | Is a person who is beaten in a fight ever killed outright, and if so where the `Slain` edge sits | the user gave a disjunction (*"extremely rare, or at least its consequences significant"*); the two lead to materially different games, and the edge is a value |
| **D4** | Where the line falls between a "sequence" of ladder stages (licensed) and an "entire arc" (not), 2026-08-18 | the licence is Jordan's wording; the design cannot rule on its own scope |

**Taken, with reasoning (not escalated):**
- **D2 (answered by canon, step 3).** `canon/03_canonical_timeline.md:98`: the post-war settlement *"elevates the institution that suppresses Thread awareness (Church)"*. Axis 2 is held by the Church (and the Crown's circle where Church-consecrated); the caste order is defended by the settlement's beneficiaries, the Crown and the Church. `[ASSUMPTION; medium; Jordan to correct]`. Content to author: a referent-bearing row for each, and the opposing-pole roster members of §2.1.
- **D3 (answered by precedent, step 4).** No caste store. Stability is already *"a Query over stance and claims, no stored value"* (CARRY-STABILITY, cited at `research/by_lane/WR_world.md:179` [c]), and the affiliation spine already holds the poles (`einhir_restoration`, `thread_truth`, `inner_tradition`, `rosters.yaml:2714-2718`). Caste is a Query over persons' convictions on those poles. `[ASSUMPTION]`.
- The axes roster lives in `rosters.yaml` (precedent: `goal_object_kinds`); one ladder per goal (`deal:` reserved); stage predicates reuse the `requires_typed` grammar with `of: subject`; progress is read person-side (AX-2); R3′ over a global re-tier or `one_per_source` (measured failures, §3.3); the standing gate is a deterministic refusal on `admits_audience`, not a die; succession is IN-61's; axis 9 is out of scope until a thread-operation act exists; `construe` (`grade: absent`, `requires_typed: none`) is not a weapon and is dropped until its own repair; a player character is a Person (§6).

---

## 11. Evidence grades

| Grade | Claims |
|---|---|
| **[repo reading]** | §1 objects and owners; the thirteen write-less verbs; `fight`/`accept` writes; the access gate and its four limbs; 31 seats (16 null / 13 same-faction / 2 in-holdings; the header's "14 of 29" at `offices.yaml:64` is stale); orientation rows mint nothing; L5; `_standing_crossings`; arrangements as authored forms; caste absent from engine code; claim deposits mint Receipts (`witness.py:654-657`, `world.py:1144-1160`); goal commits minted at `since` 0 (`populated.py:709`); IN-61 (`part5:129-133`) |
| **[measured in the repo]** (one seed, two seasons, uncommitted scratch instruments, per the proposal) | 51/803 need; 929/1,318 refused; 439/1,318 kind-mismatched (all three SUPERSEDED by `01_MISSING_IN_CODE.md` P2, P1, P10: `need` 24–28% of scenes, 76.2–76.8% refused, 28.7–32.2% wrong-kind at admission, five seeds); 37/80 pursuit-less; closure verbs all refused; 52/52 empty Propositions. Committed: R3-history in `world_q.py:2608-2618`; 0/12 accepts with a challenge (`verb_table.yaml:796`) |
| **[agent classification of prose]** | ENDINGS DECIDER 20 / ROLL 9 / THRESHOLD 8 / NEVER 10 / UNCLEAR 3, forced 19/50 |
| **[toy-world result, low confidence]** (`proposals/2026-10-25-thrust-layer/toy/`) | **Confirmed/observed (the ladder, set-piece and constrained arms are POST HOC with informed predictions; only v1's predictions were blind — `toy/README.md`):** ladder adds cross-person chain depth — 85.6 vs 25.8 in the constrained world, 62.5 vs 23.0 unconstrained (`save_figs_out.txt`); a killing at season 10 drew 9.54 acts by 4.86 actors against the killer and 1.31 tribunals, no runaway feud (`save_figs_out.txt`); ladder + decisive-form set piece + bound peace: arc-minus-null +0.244 [+0.188, +0.303], deaths 0.24/run (`exp_con_out.txt`). **Falsified or null, to be read beside them:** the same set piece WITHOUT the ladder under the same constraints: +0.016 [−0.019, +0.051]; ladder + tribunal: +0.010 [−0.046, +0.067] under the constraints; bottom-up fell BELOW its null (−0.056 [−0.083, −0.027]); pre-registered predictions falsified: ladder H1, H4, H7 (4/7 held); constrained K1, K2, K3, K5 (3/7 held); set-piece S1, S2, S6, S8 (5/9 held); contest C10 (9/10 held, `toy/exp_contest_out.txt`); lookahead leverage raised closure but not ordering and cut explained motive (`lb_more_out.txt`). The toy's arc test credits a lone closing event and ends arcs by silence; treat every figure as logic of the regimes, not of Valoria |
| **[ASSUMPTION]** | the `arc_effect_fields` first reading; opposite poles as roster members; a Receipt for a tenure write names the tenure; the `WoundTracker` separates down from dead; G2's reader widening and R1's `subject := referent` binding are Layer-1-conformant; cohort goals via `org: {rung}`; a keyed phase for R3′; D2 and D3 as taken; the PC reading |

Not opened by anyone: the 143-case count (from ED-IN-0225's text); `combat_seam`'s tracker fields beyond
`seam/ladder.py`; `World.write`'s Receipt subject on tenure writes beyond `:1125-1164`; whether
`covenant` executes in the realm; `choose.py:388`; `person_q.py:350-361`; `narrative_engine_design_v2_churn.md:448`.

---

## What would make this design wrong

1. **Already observed against v1, fixed in v2:** reading `loop/witness.py:654-657` beside
   `state/world.py:1306-1322` showed v1's arc predicate was met by witness bookkeeping. It needed no run.
   v2's predicate is only as good as the `arc_effect_fields` roster; the bookkeeping null (B0.1) is the
   standing check that it stays so.
2. **Cheapest remaining:** count executed (not refused) `determine`, `confer`, `covenant` and `open_case`
   acts over n seeds of `build_realm`, two seasons. The measured run refused all 7 `determine`s and all
   4 `confer`s (`narration-mechanisms.md:47` [c]); every closure engine in §4 ends through one of them.
   If they stay near zero after S1 and S11, ladders can be climbed but not closed, and the arc predicate
   can only be met through `person.died` — the lethal-climax dependence the toy found.
3. **Next:** B3.2's arm. If the stage-referent hit rate sits at the refusal floor, the attention order is
   not where the thrust is lost and §3 is aimed at the wrong owner.

---

## Adversarial pass — record (one round; its fixes are not themselves audited)

Critic: read-only, opus; saw only this file and the tree. About 125 citations opened, 114 held, 9 failed,
2 unverifiable. The orchestrator re-opened the load-bearing findings (F1, F2, F4, F6, F10, F13) before applying them.

| ID | Sev | Finding | Disposition |
|---|---|---|---|
| F1 | BLOCKER | arc clause (3) met by WITNESS bookkeeping | **Accepted, verified.** §1.2 rewritten: field rosters, driver-side, planted `move`/`tell` cases, bookkeeping null |
| F2 | BLOCKER | §4.3 chose the carrier Jordan rejected; duplicates IN-61 | **Accepted, verified.** §4.3 and B4.3 deleted; IN-61 named; S8 re-pointed |
| F3 | BLOCKER | gate reaches 3 of 31 seats | **Accepted.** §5.2 states the reach; G1 authors guards for every −1-referent seat; B5.2 measures harm on seat-holders |
| F4 | MAJOR | R3 converges on tier-0 (commits at `since` 0) | **Accepted, verified.** R3′: pulse, keyed phase, salience ≥ 0, formable-candidate gate |
| F5 | MAJOR | instrument and hash control wrong | **Accepted.** B0.2 added; control is R3′ off vs on |
| F6 | MAJOR | `of: referent` unspellable; wrong exception | **Accepted, verified.** `of: subject` with binding; Layer 1 question; wrapper |
| F7 | MAJOR | R2 `confer` example fails | **Accepted.** referents pass through `_stamped` |
| F8 | MAJOR | `advanced_by` static check is a §0.1-pt-5 guard and contradicts axis C | **Accepted.** deleted |
| F9 | MAJOR | "pure read over a finished world" false | **Accepted.** driver-side reader |
| F10 | MAJOR | `held_document_declines` cannot name a referent | **Accepted, verified.** new reader named; Layer 1 question |
| F11 | MAJOR | contraventions understated | **Accepted.** four rows added or sharpened in §9 |
| F12 | MAJOR | closers refused; S1 unscheduled; seat goals only 2; B1.2 duplicates IN-12 | **Accepted.** S11, S12; §4.1 keyed on body/faction goals; B1.2 = IN-12 |
| F13 | MAJOR | D2 answered by canon; D3 ignores the affiliation spine | **Accepted, verified.** D2, D3 taken |
| F14 | MINOR | toy figures uncited; falsified predictions omitted | **Accepted.** figures re-run and saved; §11 lists the falsified |
| F15 | MINOR | R3 inverts A-33 | **Accepted.** salience gate |
| F16 | MINOR | line slip; non-failing assertion | **Accepted.** `offices.yaml:64`; B4.1 asserts no Receipt minted |
| obs. | — | player character; detained holder | **Accepted.** PC entry (§6); formable-candidate gate in R3′ |

Not rejected: nothing. Where I diverged from the critic's wording: F6's "use `of: subject`" is kept as
a Layer 1 QUESTION, not a settled reuse; F8's deletion also removes the producer's static self/world split,
which the field rosters now carry at runtime.
