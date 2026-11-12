# WR — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit; resolves nothing at runtime)

Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12).

## Read at: a3ee7e6 (working tree); completed at 7289ef2

`git diff --stat a3ee7e6 7289ef2 -- engine modules systems references architecture workplans registers
research CURRENT.md` is empty (§9 EB-09): the commits between the two readings touch this suite's own files
only, so every reading below is of one tree.

The first WR audit (`09_WR_audit.md`) was read at `601e715`. `git diff --stat 601e715 a3ee7e6 -- engine modules
systems references architecture workplans registers research CURRENT.md` is empty: no code, registry, plan or
research file moved between the two readings, so every run the first audit logs (its §12, E-01 to E-17) is a
reading of the tree this addendum was written against. Findings continue the first audit's numbering from
`F-WR-13`; resolutions continue from `R-21`; evidence ids are `EB-nn` so they cannot be confused with the
first audit's `E-nn`. Nothing in the first audit or its five proposals is edited; where this file disagrees
it says so, and where a proposal is replaced the replacement carries a `_B` suffix and names what it
supersedes.

Design documents under `.designs/` and audits under `.audit/` are cited as referents for intent, vocabulary
and history (CLAUDE.md §0.05); none is the reason a behaviour is correct, and no proposal here makes code,
a tool or a test read either tree.

## 1. What was read

Written as the reading proceeded; the list at the end of this section is the final one.

**Read in full, block 1 (research and the narrative-engine referents).**
`research/emergent_narrative_literature/00_README.md`, `01` to `07` and `08_not_read.md` (all 42 entries and
the 75-row apparatus); `.audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v1.md`,
`narrative_engine_design_v2_churn.md`, `integration_with_ners_audit.md`.

**Read, block 2 (the Fable lane, evidenced by what §3 to §7 cite; the lane was cut off before it wrote
this list, so it is reconstructed from its citations and claims no more than they show).**
Threadwork's design set: `.designs/systems/threadwork/reference/threadwork_v30.md` with `_infill` and
`_index`, `threadwork_applications.md` and `_part2`, `thread_horizontal_integration_spec.md`,
`threadwork_flow_skeleton_v1.md` (§4.1's table; the philosophical reference and the v25 history to their
heads only). The world's: `world/reference/calamity_radiation_v30.md` with its infill (whole);
`geography_v30.md`, `insurgency_pipeline_v30.md`, `miraculous_event_v30.md`, `ms_trajectory_v1.md`,
`southernmost_v30.md` (section structure and tables); `overview/reference/wc_survival_spine.md` (whole).
Live successors: `proposals/2026-10-23-subsystem-completion/` T07 and T10 (§0, CP-T07-xx, CP-T10-01 to -03),
`2026-10-07-unplugged-systems-replug.md` §3.3 (IN-06), the primitives-v2 proposal set (proposals 1 and 12),
narration-mechanisms §2 to §3.4. `.audit/2026-08-08-world-churn-audit/06_master_synthesis.md` Part VII.0.
Code: `systems/threadwork/sim/` (`operations.py`, `coherence.py`, `co_movement.py`, `threadcut.py`),
`harness/chronicle.py`, `harness/decision_spread.py`, `queries/world_q.py::season_factor_of`,
`decision/budget.py`, `modules/settlements/produce.py`, `references/module_contracts.yaml:43-50`,
`rosters.yaml: endings`, `data/fixtures.py` (the terms and the forcings). The 49 hole rows of §6, each to
470 to 640 characters of its cite. CORE's and CHAR's capability proposals (§7).

**Read, block 3 (the Opus completion).** `AUDIT_BRIEF.md` (whole); this file (whole); the first lane's
`09_WR_threadwork_module.md` and `09_WR_world_motion.md` (whole, because two `_B` proposals supersede parts
of them); `research/game_precedent_suite/tables/R7_magic_sanity_travel.md` and `R8_npc_life_economy.md`
(whole); `tutorials/T19_tactics_narrative.md` (head); `queries/world_q.py:3800-3836` (`wounded_with`'s
tail) and `:4356-4700` (`witnessed`, `PersonProjection`, `projection`, `WorldReader.read`) in full;
`loop/matter.py:845-885` (the wear write); `rosters.yaml:1905-1945`, `:3575-3590` (wear and floors);
`CURRENT.md:28`, `:36`; `requirements.yaml:170-176`; `module_contracts.yaml:300-304`; the H-209, H-225,
H-230 cites at their register lines, to the premise sentence. Re-verified at HEAD: EB-03, EB-05 to EB-08
(§9), which the Fable lane cited and had not logged.

**Not read, `[SKIPPED]`.** `research/cross_scale_action_catalogue_v1.md`,
`historical_concerns_action_catalogue_v1.md` and `valoria_systems_integration_master_v1*.md` (2,093 lines):
keyword passes only (weather, famine, travel, calamity, thread, plague, winter); one transfer is used in §2.
T19 past its head. `.audit/2026-07-29-scenario-visualization/` (not opened by either completing reader).
The world-churn audit beyond `06` Part VII.0. `.designs/systems/victory/**` and the scale-transition and
propagation specs beyond what the first audit read. Hole-row cites past the length stated in §6. Test
bodies. Why: the completion was sized to the sections the cut-off lane left empty (§1, §2, §8, §9 and the
five proposals its text names), not to a second reading of the design set.

## 2. Corrections to the first audit, and new findings

Findings F-WR-13 to F-WR-20 are stated where their subject is (§3 to §5); this section indexes them, states
the corrections to the first audit, and carries the three findings that have no section of their own.

### 2.1 Index of findings in this addendum

| id | severity | one clause | where |
|---|---|---|---|
| F-WR-13 | degrades narrative | the realm closes by clock, not by act: 23 lapsed against 3 determined, three seeds, six seasons | §3.2 |
| F-WR-14 | degrades narrative | the chronicle prints who and when, never what, from no viewpoint, picked by depth | §3.3 |
| F-WR-15 | degrades narrative | no reading of open situations, tension or idle persons exists | §3.4 |
| F-WR-16 | degrades narrative | flattening every person to the realm mean lowers no story reading at two seeds | §3.5 |
| F-WR-17 | degrades narrative | threadwork's designed session (push your luck inside one contact) has no code and no plan position | §4.2 |
| F-WR-18 | hygiene, design conflict | the first lane's scenario shows the practitioner his own Coherence band, which the design forbids | §4.3 |
| F-WR-19 | degrades narrative | the scheduled weather has no memory, no neighbours and a mean of 1.167 | §5.3 |
| F-WR-20 | degrades narrative | the second contest (the world's survival) has no reading and no ending | §5.4 |
| F-WR-21 | hygiene (measurement) | 248 of the 322 `condition.worn` Events a season are writes of zero | §2.3 |
| F-WR-22 | hygiene | three hole rows rest on deaths that no longer occur at their seed | §2.3 |
| F-WR-23 | hygiene, cross-listed | a believed wound is never cleared, so a mended body still draws `tend` each season | §2.3 |
| F-WR-24 | degrades narrative (R-09) | the world's wear, the Calamity's strain, the hungry body, a matter's lapse, the realm's endings and a strand's conclusion are fixed functions of state, not draws | §2.5 |

### 2.2 Corrections to the first audit (`09_WR_audit.md`)

1. **The 27 season-5 closures (its §3, "the 27 are matured `oblige` terms", `[UNVERIFIED]` there).**
   Corroborated by a natural control across seeds, not traced to causes: §3.2. The `[UNVERIFIED]` narrows to
   one extra closure per seed.
2. **The threadwork proposal (`09_WR_threadwork_module.md`).** Its edit 1 carries the operation and not the
   session (F-WR-17); its edit 2 names a `step_call` row with no host declaration, and one entry where the
   plan's own homes name three (R-21); its edit 4 shows the practitioner his band (F-WR-18). Edit 3 (the
   tables as typed data) stands. `09_WR_B_threadwork_session_and_practitioner.md` supersedes edits 1, 2, 4.
3. **Its §14 asked CHAR for a "banded scalar" row kind.** Not needed: R-24 (§7).
4. **Its RPG-axiom list named "corruption or sanity" as lacking.** The design refuses both the word and the
   visible meter; the axiom is strain and permanent set (§7, last paragraph).
5. **Its §9.3 "hold the valley" scenario had no instrument and no end.** §5.4 supplies both (the situations
   block of F-WR-15 and a `site_band` ending selector).
6. **Its F-WR-04 treats the weather draw as a forcing that is merely off.** Switching it on as scheduled
   does not give the incident the design names (F-WR-19).
7. **Its §6.1 disposition of H-168 (`migrate` executes only hand-built) is stale** at HEAD (16 of 116 and
   36 of 217 executed, its own E-07, E-08): §6 row.
8. **A correction to this addendum's own §3.3, made at completion.** The row for T11.Q2 / D6 says the
   per-person telling is unbuilt. The *render* is; the *focalized selection* is not. `queries/world_q.py`
   `:4374-4441` holds `witnessed(w, pid)` (the Events a person holds evidence of having witnessed, in log
   order, cumulative) and `projection(w, pid)` (`PersonProjection`: his own claims and those Events, as
   copies, with `observed` and `ending` emptied so a witness reads nothing WITNESS did not deposit). That is
   a viewpoint in the literature's sense, built and read-only (PC-06 S-2, L-1). Two consequences, both
   carried in `09_WR_B_chronicle_that_tells.md`: the journal NM-W5 owes is a selection over `projection`
   and never over `w.log` (R-32); and `witnessed` lists a trail Event a person *inferred* from a finding
   (FI-03's two-cause deposit) beside the ones he saw, which its docstring records as an open contract
   question. A focalized telling that presents an inference as a sight misreports the person's knowledge;
   the telling must mark which (`causes` of the deposit carries the difference).
9. **A trap for §4.3's resolution, found at completion.** A person's own quantity is read today through
   `data/requires.py:809`, `OWN_STATE_STEMS = {"thread_sensitivity", "thread_sensitivity.gate"}`, answered
   by `person_q.OwnStateReader` on the actor himself (`world_q.py:4686-4695`). That is the precedent the
   CP-T07-02 builder will reach for when `Person.coherence` lands, and following it would hand the
   practitioner his own Coherence, which R-25 refuses. R-25 therefore names the stem roster as the place
   the refusal is written: `coherence` is not added to `OWN_STATE_STEMS`; it is world-only for its owner
   and readable about *another* only through `thread_read`'s finding.
10. **A correction to this addendum's own §6, made at completion.** H-107 was dispositioned open; the field
    it names was deleted at G1b (`state/carriers.py:259-268`), so the row is closed and the chronicle's
    "about" has two owners by line kind (R-28). §6's row and counts are corrected in place.
11. **A correction to this addendum's own §5.1 and §5.2, made at completion.** "The year: unbuilt" is half
    right. The calendar exists: `queries/world_q.py:1169-1175`, `season_of_year(w) = w.tick %
    len(season_factor_draw)`, so a declared weather table *is* the year, and it is off only because the
    table ships `()`. What is unbuilt is everything a season of the year should change besides yield
    (CP-T10-03's `season_terms`: want, illness; EB-06). `09_WR_B_weather_with_memory_and_the_year.md` keys
    its spell on that same year.

### 2.3 New findings without a section of their own

**F-WR-21 · hygiene (measurement) · most of the wear signal is writes of zero (H-135).**
*Claim.* Three quarters of the Events every instrument would count as "the world wearing" change nothing.
*Evidence.* `loop/matter.py:852-870` writes one `condition.worn` per Site per season whatever the wear;
`rosters.yaml:1911-1912` ship `dwelling: 0` and `garrison: 0`, and `:3583-3584` give both `band_floors` of
`{}`. At seeds 0 and 1, `build_realm` holds 322 Sites: 211 dwellings, 37 garrisons, 37 harbours, 37 seams;
248 are wear-0 kinds (§9 EB-07). A dwelling's or garrison's condition therefore never moves in play, and
`WorldReader.read`'s `floor` stem raises `Unspecified` for both (`world_q.py:4519-4534`), so `work` cannot be
asked of them. *Falsifier.* A season in which a dwelling's `condition.worn` Event carries a non-zero change.
None can occur under the shipped table. *Consequence.* The incident count of F-WR-15 and any wear reading
over the log reads 322 where 74 Sites moved; first lane's F-WR-04 count ("322 `condition.worn` a season") is
the same number read as motion. *Fix.* The reading (this lane's): count a wear Event only when its change is
non-zero, and count crossings (`condition.band_crossed`) as the incident; carried as edit 2's rule in
`09_WR_B_readings_of_closure_and_tension.md` (R-30). The gate that declines a no-op write is H-135's and
CORE's; not proposed here. The wear-0 kinds are SE's and MB's (H-307, H-150).

**F-WR-22 · hygiene · three measured rows cannot be re-measured at their seed.** *Claim.* H-209, H-225
and H-230 are measured on deaths that seed 0 no longer produces. *Evidence.* H-230's cite: "SEED 0: the
King `p_npc_020` dies in season 1"; H-209 counts 11 `person.died` claims at seed 0 over six seasons;
H-225 counts death claims at seeds 0 to 2 over two seasons. At HEAD, seed 0 has no `person.died` in six
seasons, seed 1 one (season 3), seed 2 two (seasons 2 and 4) (first audit E-08; §9 EB-02; the ablation's
shipped arms, two seasons, none at either seed). *Falsifier.* A death at seed 0 within six seasons at HEAD.
None. *Consequence.* None of the three mechanism claims is falsified (a dead victim's claim still forms no
question; a killing still turns nobody; an heir is still not told), but their numbers cannot be reproduced
and nothing at seed 0 exercises them. *Fix* (R-31): each row's cite gains one sentence saying the
measurement is of an earlier tree and that the re-measurement is at seed 2 or under the illness arm (first
audit E-11, eight deaths in three seasons at seed 0), after PC's duel path executes. Text in
`09_WR_B_pointer_text_for_the_orchestrator.md`.

**F-WR-23 · hygiene, cross-listed to PC and CHAR · a believed wound is never cleared.** *Claim.* Once a
person holds a claim that another is wounded, nothing in the loop retracts it, so `tend` forms on a man who
has healed. *Evidence.* `queries/world_q.py:3806-3812`, `wounded_with`'s own stated limit: "NOTHING CLEARS A
BELIEVED WOUND. Only `_eff_kill` writes a `(pid, "body", v)` Observation; `_eff_tend` and MATTER write
none", with the `NoOpReceipt` refusal each season and "[GAP: a believed ceiling is not carried]".
*Falsifier.* Not run (the arm forms near zero today: 0, 3, 9 pairs at seeds 0 to 2, per the docstring's
CP-T03-08 measurement). *Why WR.* §5.2's "a body that mends when fed" (first audit R-13) and CP-T10-04's
recovery both make bodies *rise*; each rise this lane asks for leaves a stale belief behind it, and the
season tax grows with them. The fix is the docstring's own (carry the ceiling with the body Observation,
and have `_eff_tend` and the recovery write a body Observation), at PC's and CHAR's owner; this lane asks
only that R-13 and CP-T10-04 not land without it.

### 2.4 Research transfer added at completion (R7, R8)

- **The hidden meter is a null, not a precedent.** Every game in `R7` that prices power or exposure with a
  meter shows it to the player: Darkest Dungeon II's Stress 0 to 10, Sunless Sea's six Terror bands,
  Eternal Darkness's Sanity, Don't Starve's three meters, Bloodlines' Humanity and Masquerade. R-25 (§4.3)
  hides the practitioner's Coherence from its owner. The nearest shipped shape is DD2's banter: stress
  bands are *voiced by companions* (at 7 to 9, 90% negative banter), so the band reaches the player through
  others, which is §4.3's channel (2). The ruling stands on the design document and AX-7, not on precedent,
  and is marked as untested; the reader test (§3.8 step 6) is where it fails or holds.
- **A journey is one allocation decision** (Sunless Sea: three clocks share cargo space). It supports R-23:
  a price the chooser cannot read before choosing makes travel a toll, not a decision.
- **Pathologic 2's Bound infection** is a seeded daily draw, fixed at dawn, with player-side mitigation:
  the shape of `ids.draw_factory` plus a capability use, and the precedent for `body_hazard` in §7.
- **Wildermyth's repeat suppression** (an event that occurred becomes a quarter as likely next campaign)
  and its role-casting with fall-back are the shipped form of "prefer the rare" that
  `09_WR_B_chronicle_that_tells.md` uses for ties; Wildermyth's calamity cards are a director and do not
  transfer (strife R1).
- **Historical chains route incidents along roads** (`historical_concerns_action_catalogue_v1.md` chains 3
  and 5: a relief corridor or a muster route as the contagion vector). This is the historical form of
  F-WR-19's "neighbours"; the spell keyed on the parent rung is the minimum, and route-borne spread is the
  lattice coupling's job once it has a source (first lane's world-motion edit 1). Not proposed further.
- **Did not transfer:** Anno 1800's fixed prices and royal taxes (Valoria has no price); The Sims' needs
  ticking per person (named persons do not eat, ED-IN-0255).

### 2.5 Re-check against the standing rule "we do not do deterministic" (added at completion)

The brief's Standing rule (Jordan, 2026-11-12, emphatic): every consequential outcome resolves by a draw
with a graded, recoverable result; state sets the odds, the draw sets the outcome; seeded replay,
bookkeeping and eligibility checks are permitted. Re-checked: this lane's five `_B` proposals, the first
lane's five, and the code of WR's subject.

**F-WR-24 · degrades narrative (R-09) · the world's motions and its endings are thresholds.** Site wear is
exactly the kind's rate each season (`loop/matter.py:852-870`); the lattice strain is arithmetic; a hungry
cohort's body falls by exactly `body_step` (H-125); a matter lapses at exactly `docket_lapse` (H-356); an
ending is reached when a count crosses (`world_q.py:2675-2683`); a strand concludes on its move's kind
(`flows_in`, `:5212-5213`). *Falsifier:* an outcome among these that differs between two seeds at the same
state. None can, by construction (weather and illness, which do draw, are the exceptions and the
precedent). *Consequence:* the closures F-WR-13 counts by clock are the predictable kind for this reason.
*Fix:* `09_WR_B_draws_not_thresholds.md` (R-37 to R-39); SC's lapse, PC/CHAR's death by body, FA/MB's
`seize` and B10-15's breach are listed there for their owners.

| file | verdict under the rule | done |
|---|---|---|
| `09_WR_B_weather_with_memory_and_the_year.md` | weather drawn (complies); the leg's price is bookkeeping (complies); **the `site_band` ending was a threshold** | corrected in place: eligibility, then a keyed draw; exposure at a leg's end listed as a draw for B10-18 |
| `09_WR_B_threadwork_session_and_practitioner.md` | **fatigue closed the window at a threshold; cost was independent of the draw; the breach was a band edge** | corrected in place (R-40): Focus cap as eligibility only, a strain draw for contact, cost by degree, breach drawn (listed for B10-15); the Warden's ends restated as drawn |
| `09_WR_B_readings_of_closure_and_tension.md` | a reading, resolves nothing; complies | extended: `by_clock` split into `term` (bookkeeping) and `threshold` (what the rule forbids), so the instrument shows the repairs |
| `09_WR_B_chronicle_that_tells.md` | a reading; complies | none |
| `09_WR_B_pointer_text_for_the_orchestrator.md` | text; complies | none |
| first lane's `09_WR_world_motion.md` | e1's crossing and e3's reaching rule are thresholds; e2 rests on `seize`, not checked for a roll; e4 (illness) already draws | superseded in part by `09_WR_B_draws_not_thresholds.md` e1, e3; e2 listed for FA/MB |
| first lane's `09_WR_strand_conclusion.md` | "terminal" by kind is a threshold on a classification | superseded in part by draws `_B` e4: the kind is eligibility, the drawn degree concludes |
| first lane's `09_WR_story_instruments_that_can_fail.md`, `09_WR_provided_arcs.md` | readings and adjudication; comply (the `weather` arm should take the mean-one values) | noted in draws `_B` |
| this audit's §3 to §5 | §4.5's end conditions and §5.4's ending were stated as thresholds | corrected in place |

What is **not** changed, and why: a declared term maturing (`oblige_term`) is a clock counted from an act's
own declaration (bookkeeping); `ops_per_contact` and every `requires` cell are eligibility; the readings and
the chronicle resolve nothing in the fiction.

### 2.6 Resolutions decided in this addendum

| id | inconsistency, gap or unclear passage | decided resolution | ladder step | carried by |
|---|---|---|---|---|
| R-21 | the first lane's `threadwork.work` `step_call` row has no host declaration and omits two named entries | host tuple in `seam/wrappers/threadwork.py`, checked by `registrar.require_entries`; `threadwork.read` by an `inquiry_modules` row; `threadwork.coherence_band` lands with its consumer | 4 (MATTER's `STEP_CALLS`), 5 | `09_WR_B_threadwork_session_and_practitioner.md` e2 |
| R-22 | cost keyed on the verb with Mending a special case, against the design's "direction decides cost" | one cost rule over a `direction` column of the parameter file | 3, 5 | same, e2 |
| R-23 | CP-T10-01's "[GAP: unowned]" person-side price of a leg | a pure function of two settlement ids over loaded geography, handed to `decision/` beside `fx` | 4 (`budget(p, v, k, fx)`) | `09_WR_B_weather_with_memory_and_the_year.md` e3 |
| R-24 | "banded scalar" capability kind | none; one `aptitude` row and one `at_least` use per edge | 5 | §7 (no file; CHAR's and CORE's proposals) |
| R-25 | the design forbids a meter the owner reads; the first lane's scenario shows one; the own-state stem precedent would build one | `coherence` is world-only for its owner; not an `OWN_STATE_STEMS` member; `thread_read` does not form on the actor | 3, 4 (AX-7) | threadwork `_B` e3 |
| R-26 | the Rupture is an ending by every design document and has no expression in `endings` | a `site_band` selector as eligibility, reached by a keyed draw (§2.5); the row ships absent | 3, 4 (#457 END-VICTORY); the standing rule | weather `_B` e4 |
| R-27 | the scheduled weather is memoryless, placeless and biased upward | a spell (coarser keyed draw on parent rung and coarser tick); arm members with mean one | 5 | weather `_B` e1, e2 |
| R-28 | what a chronicle line is "about" has two owners by line kind (the deleted `Event.subject` carried both, H-107) | an act line: `carriers.subject_of(act)`; an Event line: `attribution.anchor_of(w, e)`; no third reading | 4 | `09_WR_B_chronicle_that_tells.md` |
| R-29 | strand and storybar readings count `closed` without saying by what | a close is *by act* when the closing Event's causes include an executed act, *by clock* when its driver is MATTER's term or lapse | 5 | `09_WR_B_readings_of_closure_and_tension.md` e1 |
| R-30 | wear Events counted as motion (F-WR-21) | a reading counts non-zero changes and crossings only | 5 | readings `_B` e2 |
| R-31 | three hole rows measured on deaths that no longer occur (F-WR-22) | re-pointed at seed 2 or the illness arm, after the duel path | 1 (the tree changed) | pointer `_B` |
| R-32 | the journal's source (correction 8) | a selection over `world_q.projection`, marking inferred Events | 4 (PC-06 S-2) | chronicle `_B` |
| R-33 | navigation as a capability | none until places can be unknown | 2 (discovery parked) | §7 |
| R-34 | the design's "engine sets scope" of a Partial working | the next-lower breadth, one row of the parameter file | 5 | threadwork `_B` e1 |
| R-35 | Approach Training: a second gate the plan dropped | absent; if wanted, a `trait` row and one `at_least` use | 2 | §7 |
| R-36 | the Rendering Crisis's four designed beats "resolved narratively" | the Event alone (CP-T07-08); the beats are the journal's to tell from the log, never a scripted sequence | 2, 5 | §4.5 |

| R-37 | wear and the Calamity's strain are exact per season (F-WR-24) | a keyed wear draw per Site, strain as obstacle; control is today's rate | standing rule; 4 (`season_factor_of`) | `09_WR_B_draws_not_thresholds.md` e1 |
| R-38 | endings reached by a count crossing (victory, Rupture) | selector as eligibility, then a keyed draw per season; `near` on Partial | standing rule | draws `_B` e3; weather `_B` e4 |
| R-39 | a strand concludes on its last move's kind | the first lane's rules as eligibility; concludes only on the move's drawn degree (Success, Overwhelming); an undrawn kind concludes nothing | standing rule | draws `_B` e4 |
| R-40 | threadwork fatigue closing a contact, cost independent of the draw, the breach at a band edge | Focus cap as eligibility only; a strain draw for contact; cost modulated by degree (the oracle's own rule kept); breach drawn | standing rule; 4 (`operations.py:312-334`) | threadwork `_B` e1, e2 |

Twenty resolutions (sixteen, then four under the standing rule); with §6's 49 rows dispositioned. None survives the ladder to §11's terms: the one
design conflict (a visible band for the player's own person, §4.3) is answered at step 3 and named, not
escalated.

## 3. The emergent-narrative engine, read against the full design set and the literature

**Verdict.** The engine has the one property the literature treats as the hardest to retrofit (a recorded,
walkable cause for every Event: gate B2, D5) and lacks the three that turn a causal record into a story
anyone can find: a **close that is an act**, a **telling with a viewpoint and a subject**, and a
**reading of tension** (what is open, between whom, and whether it is rising or releasing). The design set
knew all three in July (`narrative_engine_design_v2_churn.md` §4: connected, continuous, rooted, live); the
season loop kept the first two invariants as substrate and dropped the last two with the Key substrate
they were written on. The shortest faithful path does not rebuild that engine. It is four readings over
what the loop already records, one content change to how weather is drawn, and the closing verbs other
lanes own.

### 3.1 What a story is, for this engine

Each term is given a definition the engine can compute from what it stores today, in the vocabulary of the
tradition, and the place the definition comes from. None needs a carrier (ED-IN-0225, T-a); each is a
reading. Where the first audit already fixed a term, this section adopts it.

| term | definition over the engine's own records | source of the shape | computable today? |
|---|---|---|---|
| **beat** | one executed act whose own Event wrote a consequence cell (`harness/arc.py::consequence_acts`), together with the question it answered | Façade: "the smallest unit of dramatic action that moves a story forward" (T03a); the engine's unit is an act, not an authored bundle | yes: 446 at seed 0, two seasons (first audit E-01) |
| **incident** | a state with duration that a person did not choose and that more than one person can answer: a shortfall, a fabric below its floor, a vacancy, a term running, a detention | Sylvester as reported (G14.Q4): "the richness comes when several events interact"; incidents must last and overlap | partly: terms, dockets and legs have duration; weather does not (§5) |
| **situation** | two or more persons whose live edges cannot all be satisfied on one referent: two ambitions on one seat, a holder and an occupier of one rung, a creditor and a defaulting obligor, a party who is also the judge, a custodian and the kin of the held | Lessard & Paré-Chouinard (E04): "dramatic situations are not sequences but states", reachable by many histories; Kybartas et al. (E05): conflict potential is computable before a run | **no reading exists** (F-WR-15) |
| **strand** | the strife design's: a connected component of strife moves around shared referents, read at the lowest rung covering it | `00_MASTER.md` §4 (ratified) | yes; collapses to one by season six (first audit F-WR-02) |
| **reversal** | within one strand or one person's record, an edge that closes against its holder after having opened for him: a hold lost, a seat vacated, a field lost after a march declared, a commitment closed unmet | Kreminski et al. (E11): none reads as a steady rise, "a few (up to three) feel compelling, and more begin to feel incoherent" (anecdotal, n=2) | not read |
| **arc** (of a person) | he wrote on his own thrust and on the world, in that order, and a later Event changed what his thrust stands on | `harness/arc.py` (CL-THRUST B0.1), whose two nulls hold on real logs (first audit §4.5) | yes; its positives today are cohorts uttering (first audit R-10) |
| **ending**, three scales | *strand*: a terminal, non-opening move with no open referent; *person*: `exists` goes false, or his last live `commit` closes; *realm*: a row of `rosters.yaml: endings` reached | strife R6; `endings_reached` | strand: mis-read (F-WR-02); person: readable, unread; realm: never reached |
| **tension** | the number of open situations and open incidents at a season boundary, and its change: how many opened, how many closed by an act, how many closed by a clock | Booth (G10.Q1, Q2): a tension variable with named inputs and a designed fall after a peak; here it is read, never steered | **no reading exists** (F-WR-15) |
| **telling** | a selection with a stated criterion, an order, a subject for every line and a named viewpoint | Ryan as reported by Short (E12.Q1); Aylett (T11.Q2): "whose viewpoint it is told from"; Juul (T06.Q1): a retelling that only recounts moves loses the system | half: selection and order exist; subject and viewpoint do not (F-WR-14) |
| **retelling** | a second person's account of the same Events from his own ledger, which differs from the first | Eladhari's fourth layer (E01) moved inside the fiction: `tell`, `forge`, `lie`, the `chronicle` channel | the acts exist (`tell` 12 of 72 executed, seed 0, three seasons); no reading compares two accounts |

Two consequences of writing the terms down. First, **the engine's story unit is the situation, and it has
no word for it.** The strife registry names forty *moves* and sixteen *links*, which are sequences; the
study it reads found the categories "alike between opening and ending" (`00_MASTER.md` §2), which is the
finding that sequence does not discriminate. A situation is a state the engine can already evaluate from
`w.tenures` and the docket, and it is the level at which apparatus rows C2 ("name its target situations,
show each is reachable, report how often each occurs") and B4 ("the same target situation through
different causal histories and casts across seeds") can be answered at all. Second, **tension is defined
by what is open, so a world that never closes anything has monotone tension and no shape.** That is what
the runs show (§3.2).

### 3.2 What the runs say about closure: the realm closes by clock, not by act (F-WR-13)

Read from the first lane's six-season outputs (its E-08; seeds 0, 1, 2; `PYTHONHASHSEED=0`; shipped
fixtures), by Event kind per season. No new run.

| what opens, six seasons | seed 0 | seed 1 | seed 2 | what closes it | seed 0 | seed 1 | seed 2 |
|---|---|---|---|---|---|---|---|
| `petition.filed` | 51 | 59 | 68 | `matter.determined` (an act) | 1 | 2 | 0 |
| `docket.formed` | 31 | 30 | 17 | `matter.lapsed` (MATTER, at `docket_lapse` 4) | 8 | 8 | 7 |
| `duty.taken` | 67 | 42 | 152 | `tenure.closed` | 33 | 16 | 37 |
| `march.declared` | 78 | 22 | 56 | `field.lost` + `field.unopposed` | 7 | 7 | 15 |
| `case.opened` | 11 | 16 | 11 | (no closing kind in any run) | 0 | 0 | 0 |
| `challenge` attempted | 223 | 253 | 223 | executed | 0 | 0 | 0 |

`matter.lapsed` occurs in exactly one season of each run, the sixth (per-season `[0, 0, 0, 0, 0, 8]`,
`[0, 0, 0, 0, 0, 8]`, `[0, 0, 0, 0, 0, 7]`), and `tenure.closed` is `[0, 0, 2, 2, 2, 27]` at seed 0 and
`[1, 1, 2, 3, 3, 27]` at seed 2. The shipped terms are `oblige_term = 4` and `docket_lapse = 4`
(`data/fixtures.py:1104`, `:1168`), so both spikes fall where a term wound in season 1 runs out. The
first audit left "the 27 are matured `oblige` terms" unverified. It is still not traced to the closing
Event's causes, but the three seeds make a natural control: `duty.taken` in season 1 is 26 at seed 0, 26 at
seed 2 and **0** at seed 1 (its duties are taken in season 2), and the season-5 spike is 27, 27 and
**absent** (seed 1 reads `[1, 2, 3, 5, 1, 4]`). The inference is corroborated; `[UNVERIFIED]` narrows to
the one extra closure per seed.

**Claim.** In the shipped realm a matter is nine times likelier to end by expiry than by judgment (23
lapsed against 3 determined over the three runs), and the first closures of any size arrive at the season
the terms mature. The storyline the engine produces unaided has the shape *opened, unanswered, expired*.

**Falsifier.** A season in which `matter.determined` is at least `matter.lapsed`, after season 4. None in
the six season-readings past season 4 at three seeds.

**Why it matters here and not only in SC's audit.** Expiry is lawful (a declared term, T-n) and it is
the engine's own form of forgetting, which the design wants (primitives-v2 proposal 12: "he loses the town
by being forgotten"). But in the literature's terms an expiry has none of Schmid's eventfulness properties
that Lessard & Paré-Chouinard use (unpredictability, effect, irreversibility, non-iterativity, relevance):
it is predictable to the season, changes no one's options, and repeats. A world whose closures are mostly
expiries reads as "boring football matches" (Aylett, T11) however dense its causal graph is, and no
instrument in the tree distinguishes the two kinds of close. The first audit's strand-shape reading counts
`closed`; it should count *closed by an act* and *closed by a clock* separately (proposal
`09_WR_B_readings_of_closure_and_tension.md`, edit 1).

**Touches.** R-02, R-05; NERS-R's no-player half.

### 3.3 The telling: omniscient, without subjects, picked by forward depth (F-WR-14)

**Claim.** `harness/chronicle.py` is a selection stage and not yet a telling. Against gate D of the
apparatus it passes D5 (a stored, finite cause set) and E15.Q2 (every stated cause is a recorded fact,
labelled "had among its causes"), and fails four rows by construction:

| row | what it asks | what `chronicle.py` does | line |
|---|---|---|---|
| T06.Q1 | a retelling that keeps the existents, and does not only recount moves | a line is `season · actor · verb · emitted kinds · answers n`; **no line says what the act was about**. The rendered chain at seed 0 is `conceal → create_record → create_record → create_record`: three records about what, concealing what, is not printed | `:128-162` |
| T11.Q2, D6 | the viewpoint of each telling is nameable | it reads `w.log` and the driver's `act_of`: world truth, no focalizer. The per-person, label-free render that was ratified as intent (primitives-v2 proposal 1; narration-mechanisms §2.1's journal, NM-W5) is unbuilt | `:227-245`; `workplans/…part4.md:300` |
| E10.Q1 | when many matches exist, a rule better than first-found | the end of the chain is "the first-logged act of maximal depth"; the walk back takes "the smallest act id on a tie", a hash order | `:93-101` |
| E12 (Labov, as Short reports Ryan) | start at the most interesting final event and chain backwards to one that needs no explanation | the pick starts from depth, never from what closed. The Events a reader would call story (seed 1, six seasons: one `person.died`, one `rung.razed`, one `covenant.offered`, two `matter.determined`) are never the end of a rendered chain unless they happen to be deepest | `:86-104` |

**Evidence that the missing fields exist.** `state/carriers.py::subject_of` is "THE ONE READ" of an act's
subject (`:949`); `soak._occasion_row` returns the question an act answered; narration-mechanisms §3.2
already assigns each line field to its owner. Nothing needs inventing.

**Falsifier.** A rendered chain at any seed whose lines let a reader who did not build the engine say what
was concealed, recorded or contested. `runs/WR/chronicle_s0_k2.txt` is the counter-example.

**Consequence.** The project's first answer to "why did that happen?" (`04` §C.11) prints who and in what
order and omits what. Proposal 1 of the primitives set named this risk itself ("a wall of lines fails the
same way the almanac does") and asked for a cheap falsifier before any design: hand one reader another
run's record. That test (apparatus D7, a `rater` row) has not been run, and cannot pass on a render with no
subjects. This is recorded as `paper`, not as failed.

**Minimal fix.** Proposal `09_WR_B_chronicle_that_tells.md`: an `about` field from `subject_of`; a pick
that starts from closing Events, defined structurally (an Event whose Receipt writes a `Tenure.until` or an
`exists` cell); ties broken by rarity within the seed (StU's form, E10) and no longer by hash. The
focalized journal stays NM-W5's; this proposal only removes what would make it unreadable when it lands.

### 3.4 No reading of situations, tension or starvation (F-WR-15)

**Claim.** The engine cannot say what is at stake between whom at a season boundary, whether that set grew
or shrank, or which persons did nothing.

**Evidence.** (a) No function under `engine/season/` (tests aside) computes a set of open conflicts:
`grep -rn tension --include=*.py engine/season` returns docstring uses of the ordinary word and nothing
else (§9 EB-03). The pieces exist as separate stampers (`vacancies`, `detainees_held`, `matters_awaiting`,
`holdings_to_found`, `ambitions`, `at_war`, the docket), each read by `questions_for` for one person at a
time. (b) Narration-mechanisms §3.4 refused need-triggered injection and said starvation "is detected
outside the sim, as a group-by over `storybar.read` rows"; no such group-by is in `harness/`. (c)
`harness/soak.py::grade_mix` grades drift of the act mix and cost, not what is open.

**Against the apparatus.** F3 ("an explicit pacing target or tension variable with named inputs, a decay
rule and thresholds that a log can show") and F4 ("an alarm for the pacing mechanism running out of
suitable content") are the two rows a no-GM design is asked first. The design's ruled answer to pacing is
that nothing steers (strife R1; narration §3.4; the Light Function's "can never inject content"), and I
accept it. But refusing to *steer* tension is not a reason to refuse to *read* it: without the reading,
"the world generates drama when nobody is watching" has no observable at all, and F-WR-13's shape (opens
accumulate, closes are expiries) was found here by hand from Event-kind counts.

**Falsifier.** A harness command that prints, per season, the count of open situations by kind and how
many closed by an act. None exists.

**Minimal fix.** `09_WR_B_readings_of_closure_and_tension.md`, edits 2 and 3: `harness/storybar.py` gains
a `situations` block composed on the existing World-first stampers, and a per-season idle count.

### 3.5 Does character change the story? The ablation (apparatus E7)

Kreminski et al.'s one transferable experiment (E11.Q3): disable the system that is supposed to make
stories and see whether the stories get worse. Their Prom Week arm replaced social reasoning with random
choice. The tree already owns the equivalent control: `harness/decision_spread.py::apply_control` gives
every pursuit-holder the realm-mean pursuits and the realm-mean conviction, with `build_realm(goals=False)`
and `no_goals()` so no authored ambition is seated or read. `wrb_ablate.py` (§9 EB-01) runs the season loop
under that control and under the shipped build and reads both with the existing instruments. Control on the
probe itself: the shipped arm at seed 0 reproduces the first audit's season-1 hash `bacd687f…` and its
1,703 acts with 898 refused.

| reading, two seasons | seed 0 shipped | seed 0 flat | seed 1 shipped | seed 1 flat |
|---|---|---|---|---|
| acts · executed | 1,703 · 805 | 1,639 · 760 | 1,706 · 830 | 1,655 · 826 |
| executed cross-person share | 12.5% | 14.5% | 11.8% | 13.9% |
| executed acts at cross depth 3 or more | 36 | 15 | 27 | 37 |
| consequence chain ends, depth 2 or more · 3 or more | 29 · 1 | 52 · 1 | 27 · 0 | 35 · 7 |
| `utter` + `commit` executed | 194 | 31 | 186 | 72 |
| `oblige` executed | 26 | 168 | 0 | 27 |
| `march` executed · fields met (`lost` + `unopposed`) | 3 · 3 | 7 · 7 | 3 · 3 | 23 · 23 |
| deaths · `matter.determined` | 0 · 0 | 0 · 0 | 0 · 1 | 1 · 0 |
| distinct executed-verb sets over 83 actors (largest shared) | 80 (2) | 66 (11) | 79 (2) | 80 (3) |

**Reading (F-WR-16, degrades narrative).** Two seeds and two seasons are a direction and not a measure,
and the arm removes two things at once (authored goals and per-person spread), so nothing here is a balance
claim. The direction is plain at both seeds: **with every person flattened to the realm mean and no
authored ambition, no story reading falls, and the world-changing acts rise.** The executed cross share is
higher flat at both seeds; consequence chain ends are higher flat at both seeds; marches that reach a field
go 3 to 7 and 3 to 23; the only death in the four runs is in a flat arm. What character visibly buys in
the shipped arm is 186 to 194 executed `utter` and `commit` acts (23% of everything executed), the
declaration of ambitions: beats by the definition of §3.1, and beats that change no one else's options.
The one reading that moves the expected way is the spread of what persons did (66 distinct sets against
80, eleven persons sharing one set against two) and it moves at one seed only.

Two explanations fit and the runs cannot separate them: the instruments are blind to what character
contributes (the first audit's F-WR-03, again), or the authored goal layer spends the scene budget on
declaring and not on doing. Either is a defect; the second is CHAR's subject and is cross-listed to
`02_CHAR_goal_lean_on_its_own_question.md`. **Falsifier:** a reading on which the shipped arm exceeds the
flat arm at three seeds. None of the nine readings above does at two. Step 7 of §3.8 makes the arm
standing so every later instrument is asked this question first.

### 3.6 How the world should generate drama when nobody is watching

The literature converges on five conditions, and the design set agrees with all five; the table says which
the shipped realm meets. "Converges" means two or more independent sources of different kinds.

| condition | sources | Valoria's ruled form | shipped realm |
|---|---|---|---|
| **1. Conflicting drives and specified relationships** | Aylett (T01.Q2); Jenkins (T05.Q3); Kybartas (E05) | pursuits, convictions, `incompatible` affiliation pairs, seats with one holder | **met in data**: 46 of 83 hold a conviction; whether it changes what happens is §3.5 |
| **2. Events outside the characters' control, with duration, that overlap** | Aylett (T01); Sylvester as reported (G14.Q4); the churn audit's "wiring, not redesign" | AX-5's three motions; weather, bodies, the Calamity as matter (#457 §4.1) | **not met**: all three forcings ship at their controls (first audit F-WR-04), and the one that is scheduled to flip is drawn independently each season (§5, F-WR-19) |
| **3. Stakes that are rivalrous and irreversible** | Short on Ryan (E12.Q4: "things characters could want, lose or fight over"); Schmid via Lessard (irreversibility) | one seat, one hold, a body, a razed Site | **thin**: deaths 0, 1, 2 in six seasons; one `rung.razed` in two of three seeds |
| **4. A close that someone does** | Façade's beat needs an effect; strife R6 ("terminates or resolves with a concluding outcome, or it is not a flow") | `determine`, `covenant`, `fight`/`accept`, `seize`, `pardon` | **not met** (first audit F-WR-01; F-WR-13 here) |
| **5. A trace another agent can meet and act on** | Fernández-Vara (G04.Q2, Q4); Jenkins (T05.Q4); Aylett's off-stage reporting (T11.Q3) | WITNESS, `tell`, Records, fabric bands, `deeds_judged` | **met and the strongest part**: same-season cross-person answers 128, 160, 158 (first audit S2) |

Three things follow that the first audit did not say.

**(a) "Hurt but not kill" is an authored property, and the engine has its mirror image.** Sylvester's rule
(G14.Q3, secondary source) is that the generator damages a colony without ending it, so decline is a long
arc that can reverse. Valoria has no generator to damp, and rightly; but its hunger pass does the opposite
of the rule by accident: a body only falls (H-211), so a cohort that has been hungry once never recovers
without `tend`, and a first-season famine that is a build artefact (first audit F-WR-10) is permanent
damage. The lawful equivalent of the damping rule is not a director. It is that **every world motion has a
rising half**: fabric that can be restored (built), a body that mends when fed (R-13), a larder that
refills (built), a season after winter (unbuilt, CP-T10-03). Where a motion only falls, the world is a
ratchet and its drama is a countdown.

**(b) The off-stage problem is solved in the engine and unsolved for a player.** Aylett's Holodeck needs
"gossip or a recap voice-over" for what happened where the user was not. The season loop simulates
everything off-stage and delivers it by WITNESS and `tell`; what it lacks is the recap, which is the
focalized journal (NM-W5). This is the one place the July design's "re-light renders the catch-up
retroactively … always focalized" (`v2_churn.md` §4) survives intact as a requirement: a returning player
must read what his person learned, from whom, as of when (narration-mechanisms §3.3 rules 1 to 3).

**(c) The realm's cast is too large to follow and the strand reading makes it larger.** Sylvester's
remembered-cast argument (G13.Q1: about 12 named colonists against Dwarf Fortress's 200) is a secondary
report with no measurement, so it is a shape. The shape applies: 83 persons, strands of 17 to 55 doers,
one strand by season six. The strife design's capacity rule ("n+1" per rung, A1) is the engine's lawful
form of a remembered cast, a subtract-only ration of what a reading *presents*; it is the Light Function's
only surviving descendant, and it is the right one to keep. It has no reader (first audit §5.3). It should
get one before it is tuned: the journal.

### 3.7 What survives of the July design, and what must not be rebuilt

`narrative_engine_design_v1.md` and `v2_churn.md` are ratified (ED-IN-0011) and written on the Key
substrate that ED-IN-0232 retired; `CURRENT.md:36` still names v2 as the head (first audit F-WR-12). Read
whole, eleven of its objects have a fate at HEAD:

| July object | fate at HEAD | where |
|---|---|---|
| `causes[]` on everything, total accounting | **kept and stronger**: every Event carries causes; refusals are Events | `state/world.py::write` |
| invariant (i) proximate connectivity | kept as a reading | `storybar.read`'s `cross` edges; the edge null (first audit E-10) |
| invariant (iii) player-rooting / tie-graph casting | kept, re-expressed person-side | `questions_for`, `reach` |
| invariant (ii) light-inertia, anti-strobe | **dropped**; nothing rations attention across seasons | `question_aggregation_rule = "first"` |
| invariant (iv) liveness (no proximate climax forecloses unsurfaced) | **dropped**; expiry forecloses silently (F-WR-13) | `matter.lapsed` |
| the Light Function (subtract-only ration) | survives only as `flow_capacity`, `presented`, `slot_rank`, unread | `world_q.py:4747-5556` |
| forecast field, `stake_horizon`, never-a-meter | **not built, and should stay so**: a person-side estimate is CR-21/§C.11's; a world-side forecast is an actor-invisible apparatus with no consumer | — |
| R-AI (no actor reads a forecast) and F8 (anti-self-fulfilment control) | survives as the strife §6 guard: stamp on against off, terminal-code histogram | H-274 |
| arc-vector templates, COLLISION priors, the 138-arc corpus | **retired with the corpus**; the cases under `engine/season/cases/` are the successor as a *specification*, not a compile target | `corpus_run` |
| claim grammar (evidence, precedent, commitment, bluster) | alive as SC's and FI's proposals in this suite | `05_SC_evidence_and_rebuttal.md`, `08_FI_05_evidence-interface.md` |
| anti-slop theorem: binding, consequence, scarcity, memory, range | binding and consequence hold by construction; **scarcity, memory and range have no reading** | this section |
| F1 any-seed regression (five seeds, chronicles differing in actors, stakes, outcomes) | unbuilt; `storybar --draw-seeds` compares chain multisets, not tellings | first audit E-02 |

The row that matters is the fourth from the bottom. The July design's failure, on its own later audit
(`.audit/2026-08-08-world-churn-audit/06_master_synthesis.md` Part VII.0, "J-O"), was to assume a mesh of
declared consumers was the engine; the season loop is the answer J-O proposed ("keep [events] as an
append-only … causality log, drive churn through the boundary directly"). So nothing here proposes a
detector, a director, a salience field or a template compiler. What the July design had right and the loop
lost is narrower: **liveness** (a close should be surfaced to someone before a clock takes it) and
**focalization** (every telling has a viewpoint). Liveness has a lawful form in this architecture, and it
is a question, not a trigger: a matter within one season of lapsing is an occasion for the seat that could
hear it (`matters_awaiting` exists; whether it ranks is `attention_key`'s). That is SC's and CHAR's edit;
it is listed in §3.8 step 3 so the dependency is on file.

### 3.8 The shortest faithful path from the present substrate

Ordered. Each step names its owner, its gate as an execution artifact, and which apparatus rows it moves
from `paper` or `fail`. Steps 1 and 2 are this lane's and are hash EQUAL.

| # | step | owner · file | gate | moves |
|---|---|---|---|---|
| 1 | Read closure and tension: closes by act against by clock; open situations per season; idle persons | WR · `harness/strife.py`, `harness/storybar.py` (`09_WR_B_readings_of_closure_and_tension.md`) | the block prints at seeds 0 to 2 and a planted world with one determined and one lapsed matter reads 1 and 1 | F3, F4, C2, C3 |
| 2 | A chronicle that says what each act was about, starts from what closed, and breaks ties by rarity | WR · `harness/chronicle.py` (`09_WR_B_chronicle_that_tells.md`) | a planted `detain → determine → fight` reads back from the death with three subjects; the seed-0 render names what was concealed | T06.Q1, E10.Q1, E12; prepares D7 |
| 3 | The closing verbs execute; a matter about to lapse is an occasion | PC, SC, FA, CHAR (their proposals in this suite) | step 1's block: closes by act above closes by clock at some seed | condition 4 |
| 4 | Weather with memory, then the year, then the wound | WR · data (`09_WR_B_weather_with_memory_and_the_year.md`; first lane's `09_WR_world_motion.md`) | a two-season shortfall in one territory under the live arm; step 1's incident count above zero | condition 2; G14.Q4 |
| 5 | The focalized journal | NM-W5 (CHAR/GO), on step 2's fields | NM-W5's own three falsifiers | T11.Q2, D6, H3 |
| 6 | The reader test | Jordan or a rater, ten minutes, one seed's journal | a reader who did not build it writes an account containing one situation, from logged facts only | D7, E04.Q4 |
| 7 | Character ablation as a standing arm | WR · `harness/storybar.py`, composing on `decision_spread.apply_control` | §3.5's reading at three seeds | E7 |

What is deliberately absent: a pass bar for "a story happened". Compton's and Smith's point (P01, P02)
and the first audit's null (no game certifies generated content as good) stand: the instruments can show
that closure, tension, situations and tellings are *zero* or *indistinguishable from a control*, which is
the failure the project needs to be able to see; they cannot certify the opposite, and step 6 is the only
row that can.

## 4. Threadwork as a registered module: the design set in full, its playable form, its season integration

**Verdict.** The first lane's module proposal (`09_WR_threadwork_module.md`) is right about the shape
(pure typed entries under `modules/threadwork/`, state passed in and returned) and incomplete in three ways
the full design set makes visible: it gives the composition row an entry kind without the host declaration
that kind needs; its input record carries the *operation* and not the *session*, so the designed
moment-by-moment game (how many workings to risk inside one contact) cannot be the same code path as the
season's one fold; and its standalone scenario shows the player a Coherence band, which the design set
forbids in terms. `09_WR_B_threadwork_session_and_practitioner.md` supersedes its edits 1, 2 and 4 and
leaves edit 3 (the tables as typed data) standing.

### 4.1 What the design set says threadwork is (read for intent; five sources, one model)

| source | status line | what it contributes that the code or the plan does not already hold |
|---|---|---|
| `threadwork_v30.md` (1,028 lines, skeleton) with `_infill` and `_index` | CANONICAL as filed; its Part 3 superseded by ED-WR-0010 | the **session**: Approach Training (a binary prerequisite with three acquisition routes); the Leap roll; a contact window bounded by Thread Fatigue (threshold Spirit × 5; a cost per round by operation) and by Focus (operations per contact = Focus − 1); overweaving (+1 Ob per further operation in one window); visibility by the observer's sensitivity (five bands) and a pre-Leap concealment roll; opposing and collective workings; the four designed beats of a Rendering Crisis (ED-681) |
| `threadwork_applications.md` and `_part2` (ED-WR-0010) | PROPOSED, held back in full | the **pricing rules**: direction decides cost (restorative work moves the practitioner *toward* equilibrium; manipulative work costs "a step per season held"; destructive work damages beyond its target); reading is free and working is dear; operations are provable and their contents are not; the practitioner "cannot judge it themselves"; §10's never-build list |
| `thread_horizontal_integration_spec.md` (ED-673 to ED-681) | CANONICAL as filed | nine cross-system fire paths, of which two survive the later rulings in kind: witnessed workings move observers' convictions (ED-676), and starting sensitivity derives from lifepath (ED-678, a capability-authoring row: §7) |
| `threadwork_flow_skeleton_v1.md` | REFERENCE, traced structure | the entry points and seams as they stood on the retired driver; no design content |
| `threadwork_philosophical_reference_v30*`, `threadwork_v25_historical*` | reference; historical | not read beyond their heads (§1) |
| live successors, not quarantined: `proposals/2026-10-23-subsystem-completion/…-07-threadwork.md` (the home of the CP-T07 positions), `2026-10-07-unplugged-systems-replug.md` §3.3 (IN-06) | PROPOSED; homes of plan positions | the genre loop G1 to G10; IN-06's "store-shed" (each operation returns its cost, the host writes); the composition rows IN-06 named: `threadwork.<operation>` as `verb_call` and `threadwork.coherence_band` as `query` |

The oracle (`systems/threadwork/sim/`) implements the operations' arithmetic and the ED-WR-0010 Coherence
model (a distance; a resting point and an elastic displacement; recovery only where the surroundings stand
in equilibrium; no self-restoration past the crossing: `coherence.py:1-70`). It implements **none of the
session**: a grep of `systems/threadwork/sim/*.py` for Approach Training, concealment, visibility, Thread
Fatigue, overweaving, over-actualisation and seasonal Mending fatigue returns two card names in
`co_movement.py` and one perception label in `threadcut.py` (§9 EB-05). B10-15's card
(`workplans/…part3.md:127-151`) schedules five verb rows (`weave`, `lock`, `mend`, `ward`, `thread_read`)
and a host; it schedules no session either.

### 4.2 F-WR-17 · degrades narrative · the designed session has no code and no plan position, so threadwork can only ever be one roll

**Claim.** Every choice the design gives a practitioner *inside* a working (how deep, how many operations
before the window closes, whether to conceal, whether to stop) is absent from the oracle, from the first
lane's `WorkingInput` and from B10-15. What is planned is one graded fold per verb per scene.

**Evidence.** The grep above (EB-05). `operations.py`'s public entries are `attempt_leap`,
`attempt_weaving`, `attempt_pulling`, `attempt_past_pulling`, `attempt_locking`, `attempt_dissolution`,
`attempt_mending` (`:351-512`); each resolves one operation and none takes a count of prior operations or
a fatigue. The first lane's `WorkingInput` has `operation, actor, depth, breadth, distance, target_kind,
in_equilibrium, draw`.

**Why it matters under the standing requirement.** Jordan's intent for personal combat is two modes on one
path: moment by moment, and an automatic round inside a larger frame. The auto/manual doctrine
(`auto_manual_resolution_duality_v1.md`, ruled) makes that general. For threadwork the manual mode *is*
the session: the precedent the tree itself cites for costly magic (D_T07; Darkest Dungeon's stress,
Sunless Sea's terror, RimWorld's psyfocus) is a decision to press on or stop, repeated, with the price
rising. A module whose entry resolves one operation and holds no session state can still carry it, if the
session's state is in the input: the season's fold is a session of length one, and a played working is
the same entry folded again with the count and the fatigue it returned. Without those two fields a played
working needs a second resolver, which is the fork the standing requirement forbids.

**Falsifier.** A `WorkingInput` field or an oracle argument that changes the obstacle with the number of
operations already made in the contact. None exists.

**Touches.** R-05, R-09 (a chain of rolls inside one scene is what R-09's fourth band asks for); the
standing requirement.

**Minimal fix.** `09_WR_B_threadwork_session_and_practitioner.md` edit 1: two integers on the input, one
on the outcome, and the overweave step as one row of the typed parameter file. No new verb, no new state
on `Person`: fatigue lives for the length of a contact and is the host's to pass.

### 4.3 F-WR-18 · hygiene, with a design conflict · the practitioner's meter must not be shown to its owner, and the first lane's scenario shows it

**Evidence.** `threadwork_applications_part2.md` §10, first item: "A Coherence meter its owner can read —
the mechanic and its display contradict"; `threadwork_applications.md` §1.4: "They cannot judge it
themselves. The faculty that would register the degradation is the faculty degrading, so others see it
first." The first lane's edit 4 names "the practitioner's Coherence band" among the stakes and gives
"the witness's ledger" as the legibility surface. The second half is the design's own answer; the first is
the thing it forbids if it reaches the player's own person. The ratified ED-IN-0011 rule for anticipation
surfaces ("never a meter") points the same way, and so does the knowledge-model ruling (a person has a
reading of the world, never the world: AX-7).

**Resolution (ladder step 3, a design document; step 4, AX-7's precedent).** A practitioner's own
`Person.coherence` is **world-only** for him: no person-side Query returns it for the actor. He learns his
state the way the design says, from three channels that already exist: (1) what CP-T07-07 takes from him
(a season with fewer scenes: felt, not read); (2) what others who can perceive it tell him (`tell`, by a
person whose sensitivity meets the detection ladder, depositing a claim about him in his own ledger);
(3) how others act toward him (`deeds_judged`, regard). This is characterful by construction: the
practitioner with a trusted, sensitive companion knows where he stands, and the one who works alone does
not. It needs no new mechanism: CP-T07-10 already makes a person's band one of the two things
`thread_read` finds on *another* person, and `tell` carries a finding. It needs two refusals: the host
does not hand the band to the chooser or the player callback, and `thread_read` does not form on the
actor himself (CP-T07-04 lets him `mend` himself; reading himself is the faculty judging itself).
Proposal edit 3.

**Conflict named, not resolved.** The completion proposal's G3 ("feel the meter before it breaks": bands
change odds and refusals) is satisfied by channel (1) without display. If Jordan wants a visible band for
the player's own person, §10's line is the document to overrule; listed in §8 of the first audit's terms
as answered at step 3, so not escalated.

### 4.4 The registered module, corrected (R-21, R-22)

**R-21 · the entry kind needs its host declaration.** The first lane's row is `threadwork.work` with
`entry: step_call`. `references/module_contracts.yaml:43-50` defines three kinds: `verb_call` ("a verb's
adapter calls it; the row names the verb in `verb:`", one verb per row, and "the registrar refuses one
target under two roles"), `step_call` and `query`. IN-06's design named per-operation `verb_call` rows.
Five thread verbs sharing one entry cannot be five `verb_call` rows on one target, so the first lane's
`step_call` is the right kind **and** it is the fieldwork shape (`fieldwork.find`: several inquiry verbs,
one entry). What it omitted is what makes a `step_call` row refuse its own deletion: either a role roster
whose rows name `module_entry:` (`inquiry_modules`, checked by `manifest/registry.py::check_inquiry_modules`)
or a host tuple the registrar checks at driver construction (`loop/matter.py::STEP_CALLS` with
`registrar.require_entries`). *Decided:* the host tuple, in `seam/wrappers/threadwork.py`, because the
thread verbs have no per-verb module variation for a roster to carry (ladder step 4: MATTER's precedent;
step 5: no new roster). Two further entries are already named by the plan's own homes and the first lane's
proposal lists neither: `threadwork.read`, which CP-T07-10 reaches through an `inquiry_modules` row for a
new kind `thread.read` (so perception *does* use the roster route, and the module has two entries, not
one), and IN-06's `threadwork.coherence_band` `query` row, which still "lands only with a consumer"
(CP-T07-07). The move to `modules/threadwork/` must leave room for all three.

**R-22 · one entry, direction as an input.** The oracle's seven `attempt_*` functions differ in obstacle
table, cost row and one side effect each. The applications document's first rule is that *direction*
(restorative, manipulative, destructive), not the verb, decides whether there is a cost; the oracle keys
cost on the verb and carries Mending as a special case (`MENDING_COHERENCE_COST = 0`, `operations.py:451`).
*Decided:* `WorkingInput.operation` stays a `thread_operations` roster member, and the typed parameter
file (first lane's edit 3) carries a `direction` column per operation, read by the one cost rule. That
keeps ED-871's value (Mending costs nothing) as a row, removes the special case, and gives a designer one
place to say what a new operation costs. It does not adopt the applications document's "restorative work
moves the practitioner toward equilibrium" as a number: that is `recover`'s `mending=` term, already built
(`coherence.py`, `recover()`), and the value is Jordan's.

### 4.5 Playable alone: "the Warden's season"

The standing requirement, point by point. This replaces the first lane's edit 4.

| element | the design's answer | exists at HEAD | missing, and whose |
|---|---|---|---|
| **scenario seed** | one settlement at breadth-first distance 1 from a wound: three Sites (one below its floor, one above, one a dwelling), a practitioner at sensitivity 60, an apprentice at 35 (can read, can barely work), a steward who governs the larder the failing Site feeds, an orthodox witness whose affiliations are `incompatible` with the practitioner's | `tiny_world`-style builders; `data/cast.py::thread_sensitivity_of`; `band_floors`; affiliation pairs | the wound (first lane's `09_WR_world_motion.md` e1); an `exercises.py` overlay row (this proposal, edit 4) |
| **the situation shown** | the Site's band and what it has closed (`closed_uses`); who is present; what the practitioner holds about each | `world_q.verbs`, `closed_uses` (World reads) | a person-side reading of a Site's band (first audit §9.3: the same gap) |
| **choices, season scale** | `thread_read` (free of stretch, and it is how he learns direction: "nothing informs them beforehand except the read"); `mend` (restorative: no stretch, a raised obstacle each further cast in a season); `weave` (manipulative: holds the Site while held, and the holding is a load on him each season); `lock` (stops it changing for good; a locked Site yields nothing); `ward`; `restore` (the mundane repair, slow and visible to no one's orthodoxy); `conceal`; rest in a place at equilibrium | `thread_read`, `restore`, `conceal` | `weave`, `lock`, `mend`, `ward` (B10-15) |
| **choices, inside a working** (the manual mode) | how many operations to make before leaving contact, each further one a step harder; whether to conceal first; when to stop | none | F-WR-17 (this proposal, edit 1) |
| **stakes** | the Site's uses and the larder behind them; the practitioner's headroom (his resting point against the human band); exposure to the orthodox witness | Site bands; the oracle's two quantities; `deeds_judged`, `petition`, `arrest` | `Person.coherence` (CP-T07-02); the sign cells firing (CP-T07-09) |
| **outcome legibility** | each working returns a degree and what it wrote; the practitioner's own state reaches him only through others (§4.3); the witness's claim is a Record a hearing can cite | degrees; WITNESS | the typed `observed` tuple on the outcome; a claim about a practitioner's state that a sensitive can `tell` (CP-T07-10's second finding) |
| **end condition** | any of, each reached by a drawn outcome (§2.5): the Site restored by drawn workings and holding two seasons; the breach (CP-T07-08), drawn with odds from how far past his human band he has gone, a person ending; the Site's last use closed by drawn wear (ruin); his detention by a drawn `arrest` on the witness's petition | `endings_reached` has no person-scale row | a scenario's end is the overlay's to state; no new ending carrier is proposed |
| **instrument** | `aperture` on the fixture: a thread row offered and executed; the chronicle from the crossing backwards (§3.3) | `aperture` | — |

**One code path.** The scenario is `SeasonDriver.season` over a small world with
`play_surface.dispatching_chooser` binding the practitioner; the host is CP-T07-02's; the module entry is
the one the realm calls. A played working suspends where a played fight does (ENCOUNTER's `host`,
`loop/encounter.py`, the one step "a playable host may suspend at") and folds the same entry. There is no
standalone resolver.

**No GM.** The design set leans on a GM in four places, each of which the proposal resolves or names: the
"engine sets scope" of a Partial (decided: Partial is the next-lower breadth, a row of the parameter
file); "engine determines domain type when Lock is applied" (R-63: not carried; a locked Site yields
nothing, CP-T07-03's rule); the Rendering Crisis as "a campaign event … resolve the crisis narratively"
(named gap: CP-T07-08 builds "the Event alone"; the four beats of ED-681 have no carrier and are the
journal's to tell, not a scripted sequence); Approach Training's "narrative-driven" spontaneous
acquisition (decided in §7: a capability row with a growth rule, or absent).

### 4.6 Integrated with the season loop: the edges, real and designed

| edge | step | carrier | state at HEAD |
|---|---|---|---|
| a person forms a thread verb | DELIBERATE | `opening_set` over rows whose `scalar_threshold` cell reads `Person.thread_sensitivity` | real for `thread_read` (3 and 4 executed, first audit E-07, E-12) |
| the working resolves | RESOLVE, inside the fold | host → `MODULE_ENTRIES["threadwork.work"]` | designed (B10-15; module absent: F-WR-05) |
| the price lands on the practitioner | RESOLVE, `driver="Seam"` | `(Person, coherence)`, two quantities | `unproduced` in `write_matrix.yaml` |
| the working changes its target | RESOLVE | `Site.condition`, `Site.locked` | designed (CP-T07-03, -04) |
| a failed or held working strains the place | MATTER, the wear loop | the lattice coupling, from the target Site | designed and waiting on a source (H-236; first lane R-03). **This is the design's "co-movement", re-expressed**: v30 Part 4 says the practitioner "controls where they touch … not how the ground moves", and draws a card; the lawful form here is that strain enters at the target and the coupling carries it to the weakest neighbours, with no deck and no stored world scalar |
| others see it | WITNESS | a claim of the working's kind to those present whose sensitivity meets the ladder | designed (CP-T07-09); the ladder is `DEPTH_TS_MINIMUM`, hard-coded (§7) |
| the orthodox act on it | later rounds | `petition`, `arrest`, `determine` on the claim | real verbs; `determine` rarely executes (first audit F-WR-01) |
| he recovers | the next seam write (CP-T07-06) | `recover()` as a projection, gated by `in_equilibrium` (CP-T07-05) | designed |
| his season narrows | DELIBERATE | `decision/budget.py::bands_below` over `coherence_band_floors` | designed (CP-T07-07, shipped `()`) |
| the Calamity costs the traveller | MATTER, travel | CP-T10-02's bands by distance | designed (B10-18) |

**Pause and zoom.** A working is one fold in the season and suspends nothing; a played session suspends
at ENCOUNTER as a fight does and returns one outcome, so the other scales pause correctly by the rule
already tested for combat (`test_rem31_grid_suspension.py`). The one place the scales do not yet meet is
upward: nothing aggregates workings into a territory's reading. The applications document calls that
"the single highest-value piece of unbuilt threadwork … the one place the personal scale and the
strategic scale actually meet" and puts it in `rendering.py`, which was struck. The lattice is its
successor and needs no aggregate: a governor reads his Sites' bands.

**The NPC and chooser surface.** The archived doctrine for NPC practitioners (ED-679) gates their workings
on a stored world scalar ("If RS ≤ 25 … Mending only") and on a Coherence the practitioner reads off
himself ("If Coherence ≤ 5 … defer"). Both inputs are refused (#457 §5; §4.3 above). The lawful
equivalents exist: a practitioner's restraint is what he holds about the fabric where he stands (claims of
`condition.worn` and band crossings, witnessed) and what he has been told of his own state; his appetite
is his affiliation cells on the thread rows (CP-T07-09) and, when authored, pursuit cells (JQ-3). The
completion proposal's stated limit stands: until pursuit cells exist "NPCs tie among the four rows", so an
NPC practitioner is not yet characterful in *which* working he chooses, only in whether his convictions
let him work at all. Nothing in this lane hard-codes an NPC thread rule; the risk to watch is ED-679
returning as a predicate on a band.

## 5. World motion: travel, survival, weather and the Calamity, as playable and as ambient

**Verdict.** The first audit established that the world's motions ship at their controls (F-WR-04). Read
against the whole design set, two further things are true. The motions, once flipped as scheduled, still
do not have the property that makes weather and hardship into story (duration and neighbourhood); and the
design's organising idea for all of them, a second contest for the world's survival run against the first
for its rule, has in the season loop neither a reading nor an end.

### 5.1 What the design set asks of world motion

Read: `world/reference/calamity_radiation_v30.md` with its infill (the whole radiation matrix: five
Mending Stability bands by six distances from Askeheim, the settlement-type modifier, the Southernmost
Surge, the three classes of threadcut being); `geography_v30.md`, `insurgency_pipeline_v30.md`,
`miraculous_event_v30.md`, `ms_trajectory_v1.md`, `southernmost_v30.md` (section structure and tables);
`overview/reference/wc_survival_spine.md` (in full); the live successor
`proposals/2026-10-23-subsystem-completion/…-10-world-travel-survival-npc-life.md` (§0, CP-T10-01 to -03 in
full), which is the home of B10-18's positions.

| design idea | where | its ruled re-expression | state at HEAD |
|---|---|---|---|
| **Two contests at once**: who governs, and whether the world survives; they "compete for the same resources: player time, faction actions, military assets" and that "IS the game's strategic architecture" | `wc_survival_spine.md` | no stored stability, no cooperation track (#457 §5); the shared resource is the scene budget, the survival work is `restore`, `mend` and relief | **no reading says how the second contest stands** (F-WR-20) |
| **Radiation by distance**: the same world state means folklore at distance 3 and spontaneous Gaps at distance 1 | `calamity_radiation_v30.md` | the lattice coupling from a source at T15, read as Site bands (IN-35); CP-T10-02's exposure by `radiation_bands` | built dark; no source (first audit R-03) |
| **The year**: winter is prepared for | T10 §0 G3; CP-T10-03 (`season_terms`: winter yield 0.25, want 1.5, illness 2.0) | a fixture and a roster row | unbuilt: `year_length`, `season_terms` are in no file (§9 EB-06) |
| **A journey is priced and risky** | T10 §0 G1, G2 | `route`, leg points, exposure at the leg's end | unbuilt: `route_pricing`, `leg_unit`, `exposure_body` are in no file; every leg costs one point |
| **Hunger is a settlement's**, carried by cohorts; named persons do not eat (ED-IN-0255); hunger "never enters the score" | T10 standing constraints | the larder draw, the body fall, `hunger` bands | runs; binds in season 0 only (first audit F-WR-10) |
| **One event, three readings**: a miraculous event is a miracle to the Church, a working to Varfell, a threat to the Movement | `miraculous_event_v30.md` §23 | a hearer credits a told claim by whether he and the teller stand in one regime (`regime_gain` 0.5, shipped) | built (CR-79); its inputs are rare (first audit F-WR-07) |

### 5.2 Each motion, as ambient and as playable

"Ambient" is what the motion does with nobody acting. "Playable" is the decision it hands a person, the
standing requirement's test. The last column is what stands between the motion and a played scene.

| motion | ambient today (shipped) | ambient as scheduled (B10-18) | the decision it should hand someone | what is missing for play |
|---|---|---|---|---|
| **weather** | none: `season_factor_draw = ()` | one of three multipliers per territory per season, drawn independently (CL-EVENTS (2)) | relief before the lean season; whose larder is opened; whether to requisition | a shortage that lasts and that neighbours share (F-WR-19) |
| **the year** | none | winter: a quarter of the yield, half again the want | stock, travel in summer, relieve before winter | nothing beyond CP-T10-03 |
| **the larder and hunger** | cohorts draw; a short draw lowers a body; season 0 only | CR-22 chooses a per-head need at which it binds | `transfer`, `requisition`, `petition`, `migrate` at the shortfall rung | a body that mends when fed (first audit R-13); the reading of whether any of the four executes (CR-22's exit already asks it) |
| **bodies: age, illness** | none (deferred, ED-IN-0317) | illness by place and season (CP-T10-05), still at rate 0 | who succeeds; who is tended | Jordan's rates (first audit §11 item 2) |
| **wounds and recovery** | a wound persists until `tend` | recovery costs time and care (CP-T10-04) | tend or act; rest or travel | nothing beyond CP-T10-04 |
| **fabric wear** | 322 `condition.worn` a season; no crossing in any run | unchanged | `restore` or let a use close | a floor that is ever crossed: the wound and the weight (first lane e1) |
| **the Calamity** | none | none scheduled beyond CP-T10-02 | hold the edge or spend elsewhere; send whom into exposure | the source; then B10-15's workings |
| **travel** | a leg costs one scene point wherever it goes; `move` 21 of 78 executed, `travel.blocked` 77 (seed 0, three seasons) | priced by route, pricing **shipped off** with "[GAP: unowned]: no position gives a chooser a person-side reading of a leg's price" | go yourself or send; near business before far | the person-side price (R-23, below) |
| **migration** | `migrate` 16 of 116 executed | unchanged | leave want for plenty | SE's (first audit H-168 row) |

**The pattern.** Every row's third column is a number on a schedule and every row's fifth column is a
reason for someone to act. The plan builds the third and, with two exceptions, has the fifth; the
exceptions are this lane's to supply.

### 5.3 F-WR-19 · degrades narrative · the scheduled weather has no memory, no neighbours and a mean above one

**Claim.** The live weather arm B10-18 will ship cannot produce the incident the design and the strife
study both name ("a drought and then famine"), for three reasons that are arithmetic and can be read off
the code without a run.

**Evidence.** `queries/world_q.py::season_factor_of` (`:1178-1205`): the factor is the constant times one
outcome drawn uniformly from the current season's entry, keyed on `(world_seed, tick, territory rung id)`.
(a) *No memory.* The key includes `tick`, so successive seasons are independent draws: with the arm
`((0.5, 1.0, 2.0),) * 4` a territory has a low season one time in three, two in a row one time in nine,
three in a row one in twenty-seven. (b) *No neighbours.* The key includes the territory, "two territories
at one tick draw independently" (docstring; CL-EVENTS (2)'s own falsifier asserts it). With sixteen
territories in the realm, the chance that a territory and all of its neighbours draw low together falls
geometrically with their number, so relief by `transfer` from next door is always there and the question
"whose grain" never becomes "there is no grain". (c) *A mean above one.* The arm's arithmetic mean is
(0.5 + 1.0 + 2.0) / 3 = 1.167. Yield is scaled by the factor (`ProduceInput.factor`, "the multiplier on
this season's `yield`") and stores add, so the arm raises the long-run harvest by a sixth relative to its
own control, in a realm whose stores already grow without a sink (#457 §8: 4,810 to 9,268 in two seasons;
not re-measured here). The arm is symmetric in ratio and not in sum.

**Falsifier.** A run at the live arm in which one territory reads `shortfall` in two consecutive seasons
at three seeds; or, for (c), the realm's total stores at season 4 below the control's. CR-73's reading
("a low draw that bites") is the instrument for the first and is scheduled; neither is run here, so (a)
and (b) stand as arithmetic and their consequence for hunger is `[UNVERIFIED]` until CR-22.

**Against the literature.** This is apparatus row C9 and G14.Q4 exactly: "Do incidents have duration and
overlap?" (Sylvester, as reported: "the richness comes when several events interact"). An independent
draw per season is a one-shot event by construction.

**Touches.** R-01, R-06; NERS-R's no-player half; strife opening A (natural shock).

**Minimal fix.** `09_WR_B_weather_with_memory_and_the_year.md` edits 1 and 2: a *spell* is a second keyed
draw on a coarser clock and a coarser place (the key drops the low bits of `tick` and takes the territory's
parent rung), which selects which of the season's entries the fine draw uses; and the arm's members are
chosen with mean one. Both are fixture data; the control `()` is today's tree. No state is stored: the
spell a season is in is a function of `(world_seed, tick, rung)`, as the season of the year already is.

### 5.4 F-WR-20 · degrades narrative · the second contest has no reading and no ending

**Claim.** Nothing in the tree says how the world's survival stands, to an instrument or to a person, and
no ending is reached if it is lost.

**Evidence.** `rosters.yaml: endings` (`:3418-3464`) holds the victory row and says of itself that it is
"GD-1 minus its sustain, Accord and Stability clauses". Its selector grammar is `{post: …}` or
`{rung_kind: …}`: it selects *holds*, so no row can be written over the condition of Sites. The design's
survival terminal ("MS 0, the Rupture: … Campaign ends in catastrophe. No faction wins",
`threadwork_v30.md` §5.3; "RS 0 = Rupture = all factions lose", `wc_survival_spine.md`) therefore has no
expression. The readings that would show the contest's state exist and are unread: `closed_uses` and
`hunger` have one caller each, a report (first audit F-WR-04).

**Resolution (ladder step 3, then 4).** The Rupture is an ending by every design document that names it,
and #457's END-VICTORY handle already rules the form: "an ending and victory vocabulary … a Query over
holds and seats that the season reports, never an actor". The cut that removed the stored scalar (#457 §5)
does not remove the ending; it changes what the Query reads, from a number to the bands of Sites. *Decided:*
the `endings` grammar gains a third selector, `{site_band: <a band_floors band>, of: <site kind or all>}`,
*eligible* when at least one selected Site under the realm reads at or below that band and **reached by
a keyed draw** whose odds rise with how much of the fabric has fallen (corrected under the standing rule,
§2.5: as first written, "reached when every selected Site reads at or below", it was a threshold); a row
using it carries `victory: false`. The roster's act-credit clause ("an act opened at least one edge the condition stands
on") is stated for holds and is not applied to a Site selector: a ruin nobody caused is the case the
ending exists to report (T-b forbids a crossing *producing* an outcome; a reported ending "emits no Event,
halts nothing and writes nothing"). The **row** (which band, which kinds) is Jordan's content and ships
absent; the grammar is the proposal's edit 4. This is not escalated: both design documents and the
ratified handle point one way, and shipping the grammar with no row changes no behaviour.

**The survival contest as play.** Because named persons do not eat and hunger never enters the score,
survival is never a personal meter. Its playable form is a governor's: a settlement with a failing Site
and a short larder, a budget of scenes, and four answers (`restore`, `transfer`, `requisition`, `petition`)
against the same budget his rivals are spending on seats. That is the scenario the first audit sketched as
"hold the valley" (§9.3); what this section adds is its instrument and its end: the reading of §3.4
counts open incidents by settlement, and a `site_band` ending tells the player the valley was lost.

### 5.5 R-23 · the unowned gap in the journey's price has an answer

CP-T10-01 ships its pricing off because "no position gives a chooser a person-side reading of a leg's
price". The leg's price is `route(a, b)` over `settlement_adjacency` and `terrain_cost_matrix`, which are
geography *data*, loaded once by `data/geography.py`, identical for every person and changed by no act.
`decision/budget.py` already admits a non-World argument on exactly that ground: `budget(p, v, k, fx)`
(`:18`) takes `fx` because it is identical for every person and "not world state" (`:53`). Yield is linear
in the factor (`modules/settlements/produce.py:19`, `int(base * (max(0, condition) / scale) * factor)`),
which is what F-WR-19 (c) rests on. *Decided (ladder step 4, that precedent):* the price a chooser reads is a pure function of
the two settlement ids and the loaded geography, handed to `decision/` beside `fx`; whether the road is
open (the border, a `contain` path) stays a World read made at the fold, and a journey priced and then
blocked is `travel.blocked`, which is how a person learns the road is shut. No person-side World read is
introduced. Proposal edit 3; the flip of `route_pricing` then waits only on its own paired arm.

## 6. The 48 primary hole rows not read by the first lane, dispositioned

**How these were read.** Each row was opened at its register line in `engine/season/hole_register.yaml`
and its `grade`, `default` and `cite` fields read to the first 470 to 640 characters (the cite of a long
row runs to several thousand; its head carries the status sentence and the measurement). That is more
than the dossier's 300-character excerpt and less than the whole cite, and is stated so no row below is
taken as read to its last word. "Verified" means checked against code or a run named in §9 or in the
first audit's §12; "as the row says" means the row's own closing sentence was read and nothing here
contradicts it. The eight rows the first lane read in full (H-176, H-186, H-211, H-235, H-236, H-238,
H-257, H-274) are not repeated. The work order counts 48 unread rows; the dossier's 56 less the seven of
those eight that are dossier rows (H-236 is not one) is 49, and all 49 are below. H-118 carries no
register line in the dossier and is dispositioned last.

| row | register grade | disposition at HEAD | evidence | action |
|---|---|---|---|---|
| H-04 `q`'s producer | assumption | **closed** (the row: "DISCHARGED BY `W5`"; four sources, a roster) | `questions_for` forms every act | none |
| H-05 world-generation roster | assumption, **empty cite** | **closed in code, unrecorded at the row** | `build_realm(0)`: 83 persons (first audit E-13) | the row's cite names its closer; text in `09_WR_B_pointer_text_for_the_orchestrator.md` |
| H-27 travel-leg ownership | assumption | **closed, and the default is superseded in form**: the row says "as the Tenure's SUBJECT"; the code holds the leg as `Person.travel_leg` | `loop/matter.py:831-843`; `travel.ended` 24 | row text; CP-T10-01 changes the leg's element to a tuple and must update it |
| H-32 `judging_set_rule` | assumption | open, narrowed; **not WR's** (SC) | as the row says | none |
| H-34 establishment size | ruled | **closed as moot** (field deleted at `17a`) | as the row says | none |
| H-40 claim decay | assumption | **closed**; shipped 5 a season | `data/fixtures.py:328` | cost is first audit R-14 |
| H-51 what demands an individuation | ruled | **closed by a producer** (`person.demanded`) | as the row says | none |
| H-65 `requires:` is prose | assumption | open, narrowed; **not WR's** (CORE) | as the row says | none |
| H-125 body step | assumption | **open as a value**: ships 10, "Not a claim that 10 is the magnitude"; its own test is "IS STARVATION A SEASON OR A CAMPAIGN" | `body.changed` 37 to 41 in season 0 and at most 1 after, three seeds | CR-22 re-derives it; the test's answer depends on whether a fed body mends, so it should be read with first audit R-13's signed step on, not before (a sequencing note for B10-18: CR-22 precedes CP-T10-04 in the card) |
| H-95 two scale vocabularies | ruled | **closed in effect** (first audit E-15) | — | none |
| H-102 propagation loop | measured | **open as a sign, measured as an edge**; the row's own caveat stands ("under this instrument's own fixtures it cannot amplify at all") | cross edges 286 to 366 over four arms (§9 EB-01) | none; the ablation of §3.5 is a second reading of the same edge |
| H-103 claim decay as a bound | measured | **closed** | as the row says | none |
| H-107 `Event.subject` | measured | **closed (corrected at completion; the Fable lane had it open)**: the field is deleted (G1b, plan position 4, 2026-09-26; `state/carriers.py:259-268`), its two senses now read through `state/attribution.py::actor_of` (`:73`) and `anchor_of` (`:105`). It bears on §3.3: an act line's `about` is `subject_of(act)`; an Event line's is `anchor_of(w, e)`; nothing reads a subject off an Event | `state/carriers.py` docstring; `:1667` cites "`H-107`'s own closure" | `09_WR_B_chronicle_that_tells.md` |
| H-110 band crossing loses its Event | ruled | **closed, dissolved** | as the row says | none |
| H-129 `last_emission_of` | measured | **closed** (both halves fixed, per the row) | as the row says | none |
| H-130 a write can apply and still raise | measured | open; **not WR's** (CORE) | as the row says | none |
| H-135 a no-op closure write still emits | measured | **open, and it is most of this lane's wear signal**: 248 of the 322 `condition.worn` Events a season are writes of zero | §9 EB-07 | F-WR-21; CORE owns the gate, WR the reading |
| H-139 deleted Tenure invisible to the diff | measured | open; **not WR's** (CORE) | as the row says | none |
| H-150 garrison strength unreachable | assumption | open; **not WR's** (MB). Note: `garrison` wears at 0 and has no band floor, so the Site's `condition` never moves | §9 EB-07, EB-08 | MB |
| H-159 `oblige` term | assumption | **open as a value, and now observed**: ships 4; the season-5 closures are its first maturation | F-WR-13 (27, 27, absent by seed) | FA; the row's "NOT MEASURED" is out of date |
| H-164 how far one act raises a fabric | assumption | open as shipped; unreached, because no fabric is below its ceiling | §9 EB-07 | none until a Site falls |
| H-167 capacity floor | assumption | open; **not WR's** (SE) | as the row says | none |
| H-168 `migrate` executes only hand-built | measured | **stale**: `migrate` 16 of 116 and 36 of 217 executed | first audit E-07, E-08 | SE re-reads |
| H-172 `Claim.round` | measured | **closed in effect** (first audit S2) | — | re-grade at the row |
| H-185 authored ought's predicate | absent | held; **not WR's** (CHAR) | as the row says | none |
| H-208 bodies-clock values | assumption | **built dark, deferred by ruling** | fixtures 0.0 | first audit §11 item 2 |
| H-209 a dead victim's death claim never becomes a question | measured | open in mechanism; **its measurement no longer reproduces**: it counts 11 `person.died` claims at seed 0, six seasons, and seed 0 has no death in six seasons at HEAD | first audit E-08 | F-WR-22; re-measure after the duel path executes |
| H-215, H-216, H-223 | assumption | open as values; **not WR's** (SC) | as the rows say | none |
| H-225 a killing turns nobody toward the killer's faction | measured | open; same staleness as H-209 (its counts are of death claims at two seasons, seeds 0 to 2) | first audit E-05, E-12 | F-WR-22 |
| H-227 a witness does not form a `commit` from a petition | measured | open; **not WR's** (FI/SC) | as the row says | none |
| H-230 the heir is never told the throne is vacant | measured | open; **its premise no longer occurs**: "SEED 0: the King `p_npc_020` dies in season 1"; at HEAD nobody dies at seed 0 in six seasons | first audit E-08 | F-WR-22 |
| H-232 `pardon`, `raze` formed and refused | measured | open | `raze` 0 of 51, `pardon` 0 of 6 | CHAR/FA |
| H-242 hunger bands | assumption | **closed as an injected value** | as the row says | none |
| H-243 stock report | assumption | **closed as an injected value** | as the row says | none |
| H-245, H-246, H-247 practice | assumption | **closed as injected values, live** | `data/fixtures.py:475-479` | §7 |
| H-278 `convene` asks no purview | measured | open; **not WR's** (FA) | as the row says | none |
| H-283 ambition is a switch, not a weight | measured | open; **not WR's** (CHAR). §3.5 is a second reading in the same direction: removing authored ambition raises world-changing acts | §9 EB-01 | cross-listed |
| H-287 standing and backers do not reach the roll | measured | open; **not WR's** (SC) | as the row says | none |
| H-291 hand-built `establish` skips purview | measured | open; **not WR's** (FA) | as the row says | none |
| H-307 housing ignores dwelling condition | measured | open; **not WR's** (SE). Note: dwellings wear at 0 and have no floor, so their condition cannot change in play | §9 EB-07 | SE |
| H-311 a failed interrogation is spendable as proof | measured | open; **not WR's** (FI/SC) | as the row says | none |
| H-326 the fieldwork head's tracks have no carrier | measured | open; **not WR's** (FI) | as the row says | none |
| H-350 everyone fights with the same kit | measured | open by design (content); **not WR's** (PC) | as the row says | none |
| H-356 docket lapse | assumption | **closed as an injected value, and observed**: ships 4; "a matter docketed in season t … lapses as t + 5 opens", which is the season-5 spike of F-WR-13 | first audit E-08 | none |
| H-118 `content_hash` | measured | **closed** | hashes reproduce across this file's and the first lane's processes (§9 EB-01) | none |

**Counts** (corrected at completion for H-107). 49 rows: 19 closed (H-04, -05, -27, -34, -40, -51, -95,
-103, -107, -110, -118, -129, -172, -242, -243, -245, -246, -247, -356); 6 open in this lane or bearing on
it (H-102, -125, -135, -159, -164, -208); 4 whose measurement or premise is stale at HEAD (H-168, -209,
-225, -230); 20 another lane's, read and left. Whether H-107's register row itself still reads open was
not checked past its head; if it does, its re-grade is text for the orchestrator.

## 7. Capability-authoring consequences

**Not redone.** The capability authoring surface is CORE's
(`proposals/01_CORE_capability_authoring_surface.md`: one `capabilities:` block in
`references/descriptor_registry.yaml`, kinds `attribute | skill | aptitude | trait`, growth rules
`train | practice | use`, a `capability:` column on verb rows) and the table of where a capability enters a
person's own choice is CHAR's (`proposals/02_CHAR_capability_uses_table.md`: `rosters.yaml:
capability_uses`, forms `about_mid | at_least`, each with a named gain fixture; its third row is already
`{use: own_state_gate, key: prac.thread_sensitivity, form: at_least, gain: thread_sensitivity_gate}`). The
DICE audit's §14 maps what reaches a roll. This section states what the design set read for this addendum
changes in what WR asks of those two surfaces, in their schema, and corrects one request of the first
audit's §14.

**R-24 · the first audit's "banded scalar" row kind is not needed.** The first audit asked CHAR for "a row
kind for a scalar aptitude with bands" for thread sensitivity. Read against CHAR's actual proposal, a band
edge is an `at_least` use with its own gain fixture, and a ladder is several such rows over one key.
*Decided (ladder step 5):* no third form and no new kind. Thread sensitivity is one `capabilities` row of
`kind: aptitude`, and every place its value gates something is one `capability_uses` row. That keeps
CHAR's rule ("a third form is a code change and a design decision") intact.

| capability, as the design set has it | where it bites | today | as data, in the CORE and CHAR schema | what stays code or stays Jordan's |
|---|---|---|---|---|
| **thread sensitivity** (0 to 100; ED-678 derives a starting value from lifepath: origin, formation, vocation) | may form `thread_read` (30); may work at each depth (30, 50, 70); what a witness perceives of a working (five bands in v30 §2.3; four in the applications ladder); the Leap's obstacle (2 below 50, 1 from 50) | one field; one fixture gate; the rest are `operations.py` constants (`DEPTH_TS_MINIMUM`, `LEAP_OB_TS_LOW/HIGH`) and unbuilt | `capabilities.rows.thread_sensitivity: {kind: aptitude, scale: {floor: 0, ceiling: 100}, grows_by: []}`; one `capability_uses` row per edge: `thread_read` gate, `working_depth.<depth>` (three), `working_perceived.<band>`; the Leap's two obstacles as rows of the threadwork parameter file keyed on the same edges | the starting value by lifepath is CORE's edit 5 (the character's side) with ED-678's table as its content, Jordan's; **growth** is a rule the closed set does not hold: the design says "exposure teaches" (E-2) and that an Overwhelming working adds one. That is a fourth growth rule or `use` re-read, a design decision (ARC-51), not proposed |
| **the craft** (the pool a working rolls: Spirit doubled, a history term, sensitivity over ten) | every working | the oracle's `_actor_pool` on a duck-typed actor; CP-T07-01 routes `spirit` and `history` through `faculty` | a `capability:` on each thread verb row naming one `skill` row whose `base` is `attr.mind.will`; `grows_by: [practice]`, so `world_q.practice` reaches it by the route every other skill uses | not `train`: canon P-08 excludes advancement "by study alone" (T07 gap J). The history term's fate is CR-85's |
| **Approach Training** (v30 §2.1: a binary prerequisite to work at all, with three routes to acquire it) | a second gate beside sensitivity | absent from the oracle and from B10-15, where sensitivity is "the one class gate" | if wanted: a `kind: trait` row and one `at_least` use on the thread verbs; acquired by `train` under a mentor | whether the second gate exists is answered at ladder step 2 by the plan (it dropped it); recorded so the design's distinction between *perceiving* and *being able to work* is not lost by accident |
| **the practitioner's resilience** (R-14) | how much of a working's cost lands | `RESILIENCE_GAIN = 0` in the oracle | a `capability_uses` row `{use: working_cost, key: attr.mind.will, form: about_mid, gain: resilience_gain}`; the gain moves from an oracle constant to a fixture | the value (WR-01) |
| **wayfaring** (nothing in the tree) | the price of a leg; the exposure charged at its end | none: every person pays the same | a `skill` row and two uses, `leg_price` and `exposure_charge`, each `about_mid` with a gain shipped at 0 | two new use **sites** are code (one reader each, in `route`'s caller and the leg-end pass); the completion proposal already records the missing capability source for exposure ("J-13's remainder") |
| **hardiness** (Endurance) | illness and age (`body_hazard`); hunger's body step | the hazard reads age and two rates; no attribute | one use `body_hazard` over `attr.body.endurance`, `about_mid`, gain 0 | the rates (ED-IN-0317) |
| **navigation** | — | none | **none proposed** | a route is a shortest path over public geography; a skill at finding the way has nothing to act on until places can be unknown, and discovery is parked (`poi_catalog` holds counts, not places: T10 §0). A null, stated so nobody adds a skill with no reader |
| **tending** | how much one `tend` restores, and whether it works | one unpriced `tend` heals 1 to 1000 ("code-flagged [ASSUMPTION]", T10 G5) | CP-T10-04's, with a `capability:` on the `tend` row | CP-T10-04 |

**The interface this lane needs from the merged surface, restated after the full read** (it replaces
the four-function list in the first audit's §14 only where it differs): a use site may be declared for a
*module input* as well as for a person's own choice, because four of the rows above (`working_depth`,
`working_cost`, `leg_price`, `exposure_charge`) are read by a host when it builds a typed input record,
not by `decision/`. CHAR's table is scoped to "a person's own choice"; the same row shape serves, and the
closed roster of sites is where the difference is recorded. Nothing else is asked.

**RPG axioms, corrected against the design set.** The first audit listed "corruption or sanity as a
second track with recovery rules visible to the player" as lacking. The design refuses the visible half in
terms (§4.3) and refuses the word: "An alignment axis, a corruption track, or an arc from good to evil …
No sin, no corruption, no fall, and nothing being punished" (`threadwork_applications_part2.md` §10). The
axiom threadwork implements is nearer *strain and permanent injury* (an elastic reserve that recovers with
rest in the right place, and set that does not) than *sanity*, and a designer adding a capability to it
should reach for that vocabulary. The one tradition-standard axiom it still lacks is the one F-WR-17
names: *push your luck within a casting* (each further operation harder, the practitioner choosing when to
stop).

## 8. Proposals written by this addendum

All under `proposals/2026-11-12-subsystem-audit-suite/proposals/`, `## Status: PROPOSED`. None edits the
first lane's files; the `_B` infix marks a supersession or an addition.

| file | carries | supersedes | runtime change |
|---|---|---|---|
| `09_WR_B_readings_of_closure_and_tension.md` | F-WR-13, F-WR-15, F-WR-16, F-WR-21; R-29, R-30; §3.8 steps 1 and 7 | nothing (adds to the first lane's `09_WR_story_instruments_that_can_fail.md`) | none: harness readings, hash EQUAL |
| `09_WR_B_chronicle_that_tells.md` | F-WR-14; R-28, R-32; §3.8 step 2 | nothing | none: harness render, hash EQUAL |
| `09_WR_B_weather_with_memory_and_the_year.md` | F-WR-19, F-WR-20; R-23, R-26, R-27; §3.8 step 4 | nothing (sits beside the first lane's `09_WR_world_motion.md`) | e1, e2 only under a declared arm; e3 none until `route_pricing` flips; e4 none (grammar, no row) |
| `09_WR_B_threadwork_session_and_practitioner.md` | F-WR-17, F-WR-18; R-21, R-22, R-25, R-34; §4.5 | `09_WR_threadwork_module.md` edits 1, 2, 4 (edit 3 stands) | none by itself (as the first lane's) |
| `09_WR_B_draws_not_thresholds.md` | F-WR-24; R-37 to R-40; the standing rule applied to WR's subject | the *reaching rules* of the first lane's `09_WR_world_motion.md` e1, e3 and the *meaning of terminal* in `09_WR_strand_conclusion.md` e1, e2 (both kept as eligibility) | e1, e2 declared movers behind controls; e3, e4 change readings |
| `09_WR_B_pointer_text_for_the_orchestrator.md` | the first audit's R-11, R-12, R-20 as text; H-05, H-27, H-159, H-168, H-172 and F-WR-22's three rows | nothing | none: text for files only the orchestrator edits |

## 9. Evidence log

`PYTHONHASHSEED=0` for every run. Outputs under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/WR_B/` (this lane) and
`…/runs/WR/` (the first lane's, read and not re-run). No pytest; no `aperture` run.

| id | command or probe | seed · seasons | outcome |
|---|---|---|---|
| EB-01 | `python wrb_ablate.py <seed> 2 shipped|flat` (`runs/WR_B/wrb_ablate.py`; outputs `ablate_s{0,1}_k2_{shipped,flat}.txt`) | 0, 1 · 2 | shipped seed 0 hash `bacd687f…`, 1,703 acts, 898 refused (the first audit's E-05 reproduced); flat seed 0 `1e202aff…`, 1,639 / 879; shipped seed 1 `8aae8412…`, 1,706 / 876; flat seed 1 `e48c989e…`, 1,655 / 829; readings as §3.5's table; cross edges 363, 286, 366, 333 |
| EB-02 | read of the first lane's `runs/WR/probe_s{0,1,2}_k6.txt` by Event kind per season | 0, 1, 2 · 6 | §3.2's table; `person.died` absent at seed 0, `[0,0,1,0,0,0]` at seed 1, `[0,1,0,1,0,0]` at seed 2 |
| EB-03 | `grep -rn -i tension --include=*.py engine/season` (tests excluded) | — | 17 lines: comments on AX-7 tensions, `extension` substrings and one `spy` signature; no computation of a set of open conflicts. Re-run at completion, same result |
| EB-04 | read of `harness/chronicle.py` (whole, at completion) | — | as §3.3's table; the walk-back tie is "the smallest act id" (`:18`, `:90`), and the module is inside `tools/ci_sim_fabrication_check.py`'s blocking scope (`:65`), so a new flag takes no default seed or season count |
| EB-11 | read of `state/carriers.py:247-270` and `hole_register.yaml` H-107 | — | `Event.subject` deleted at G1b; H-107 closed (§6 corrected) |
| EB-05 | `grep -n -i -E "approach.?training|conceal|visib|fatigue|overweav|over.?actual|mending.?fatigue" systems/threadwork/sim/*.py` | — | two lines: `co_movement.py:50` (a card, "Scar Memory … visible to non-Sensitives") and `threadcut.py:41` (a perception label). Re-run at completion, same |
| EB-06 | `grep -rl` over `engine/`, `modules/`, `references/` (`*.py`, `*.yaml`) for `year_length`, `season_terms`, `route_pricing`, `leg_unit`, `exposure_body` | — | 0 files each (completion re-run) |
| EB-07 | `python -c` over `build_realm(seed)`: Sites by kind and `fixtures.wear(kind)` (`runs/WR_B/eb07_wear.txt`) | 0, 1 · build | 322 Sites: dwelling 211, garrison 37, harbour 37, seam 37; wear 0, 0, 10, 10; 248 wear-0 at both seeds |
| EB-08 | read of `rosters.yaml:1905-1945` and `:3575-3590` | — | `wear_per_season` `dwelling: 0`, `garrison: 0`; `band_floors` `dwelling: {}`, `garrison: {}` |
| EB-09 | `git diff --stat a3ee7e6 7289ef2 -- engine modules systems references architecture workplans registers research CURRENT.md` | — | empty; the ten commits between touch this suite's files only |
| EB-10 | `grep -o "SEED 0: the King[^.]*" engine/season/hole_register.yaml` and the H-209, H-225 cites at their lines | — | H-230's premise sentence as quoted in F-WR-22 |

