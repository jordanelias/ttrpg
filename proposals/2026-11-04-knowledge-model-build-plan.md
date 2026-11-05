# Build plan: the knowledge model, the ten attributes, histories (ED-IN-0319 to ED-IN-0331)

## Status: PROPOSED (a plan, not a mechanism: CLAUDE.md §0.05; nothing here is built). Lane: IN

**What this is.** Jordan's rulings of 2026-11-04 (`registers/editorial_ledger_in.jsonl` ED-IN-0319 to ED-IN-0331) were
vetted against the tree and the v11 plan by three read-only passes (claim-model integration, attributes/risk/`lie`/histories,
derived-value duplicates) and a derived-value name census. This file says, per ruling, what the code already does, what to
build, in what order, with what control, and which v11 rows change. Jordan's instruction: vet against existing code and v11,
plan the build first. **Nothing below has been built.** Every citation was opened by a reader; the orchestrator re-opened the
ones marked (checked).

## 1. The result in one paragraph

Most of the claim model Jordan describes **already exists**; what is missing is narrow, and two of CR-82's four commits as
written would break the write gate and double count. "Histories" cannot be dropped as a rename: combat's `history` is the
roll's backbone. The ten attributes are a registry rewrite that no engine reader depends on yet, but CR-20 and CL-ATTR
assume nine. Risk tolerance already has an owner. `lie` needs nothing beyond CR-27.

## 2. The claim and knowledge model (ED-IN-0319 to 0327)

| ruling | what the code does (file:line) | action |
|---|---|---|
| R1 knowledge is kept for years (0319) | `ledger_cap` 200 fills in season 1; `state/ledgers.py::eviction_key` forgets lowest `confidence × (when+1)`; CR-81's claims: 0, 11, 0 of 236 at season 4. At decay 5 a claim reaches 0 at 20 seasons and eviction then falls to insertion order (`fixtures.py:247`; H-40) | **BUILD, one lever** (§2.1) |
| R2 stale claim, opinion stays (0320) | `deeds_judged` never reads confidence (`person_q.py:94-142`): **staleness already leaves the judgment alone**; the opinion is lost only when the claim is evicted | R1 covers it. Replace the "write to `stance`" commit with a measurement (§2.2) |
| R3 same origin adds nothing, distinct origins corroborate (0320, 0322) | Built for told claims: the guard deposits a second claim on a different origin (`witness.py:921-937`, checked) and `LedgerReader._support` is a noisy-OR over distinct origins (`person_q.py:938-974`) | **Build nothing.** No refresh |
| R4 once heard is less certain; trust or judgment settles competing claims (0321) | `teller_weight ** hops`, noisy-OR; but only `belief_contradicts` passes a `weigh`; chained told claims are about 0 in the realm (H-237; 0, 0, 4, 0), so the arm is dormant | Record dormant; `said_of` weighing (G3) goes to CR-83's design |
| R5 trust + count + fit (0323) | Trust, count, situation fit (`dissents`, `options.py:1435-1477`) and teller fit (`record`, `:1540-1580`) exist. **Missing: fit with what the holder holds of the claim's SUBJECT person** | CR-83's design file, nothing else |
| R6 attunement / reason sharpen judgment (0326, 0327) | No engine reader takes an attribute value (`engine/substrate/descriptors.py` is read only by a test) | CR-83's design; needs CR-20 |

**Why the commits 2 and 3 of CR-82 are dropped (checked in the tree).**
(a) `write_matrix.yaml:93-96` allows `(Claim, confidence)` only at MATTER; `:256-262` allows `(Person, stance)` only at
RESOLVE and ENCOUNTER; `:180-185` gives WITNESS `claim_ledger` only. A refresh or a `stance` write at the witnessing is
`Forbidden` at `state/world.py:1263-1286`, and `Claim.when` has no row at all. (b) The refresh "in place of the
suppression" has no suppression to replace for a different origin; keeping the second claim and raising the first counts
corroboration twice under two owners. (c) A deed judgment written to `stance` is read again by `legitimacy`
(`person_q.py:456-482`), `_bond` (`:354-365`), `teller_weight` (through `regard`, `options.py:1630-1633`), `choose`
(`choose.py:60,101`), `held_against`/forgive, and it forks `regard` from `reception`, which CP-T05-02 AM-D-01 refused
(`part13.md:418`). `verb_table.yaml:1394-1405` records the same `stance` write attempted for `tell` and reverted.

### 2.1 Position CR-82, cut down (B10-09 close two, after CR-25, before CR-17; unchanged place)

1. **Commit 1, measurement** (a producer is running it; first report 2026-11-04). Findings so far: (a) the control at the
   tip reads **0, 6, 0** of 236 acquaintance claims at season 4 and cap 200 (CR-81's 0, 11, 0 reproduces at `c35f6599`; the
   seed-1 move is CR-25's and B3.2's re-pinned hashes), so the exit's control line is re-based to the tip; (b) the code
   carries **no year** (`year_length` and `season_terms` exist only in CP-T10-03's prose, shipped as `year_length` 0), and
   **Jordan has ruled a year is four seasons (ED-IN-0332)**, which confirms CP-T10-03's planned flip to 4 and moves nothing:
   the horizon is stated in seasons at four to the year (eight seasons is two years, twelve three);
   (c) the told arm is **near empty** at cap 200 (1 and 0 told claims held at seed 0, 8 and 4 at seed 1), which confirms
   the integration read: a told column cannot separate caps; (d) season cost grows with the season at cap 200 (4.1, 7.8,
   11.2, 20.4 s at seed 0, two processes) and peak memory was 522 MB at four seasons, so the first limit at large caps is
   time, not memory; the grid is narrowed to caps 400-3200, seeds 0-1, snapshots at seasons 2, 4 and 8. Adds three readings the integration read asked for: the told-claim
   count at cap 200 **first** (if near 0 the told arm cannot separate caps and is a fake control: report and do not cite);
   the event-log size (a bigger cap multiplies `claim.decayed` emissions, `matter.py:437-466`); and season time at the
   shipped `declared` arm (scan cost is O(ledger), and `said_of` runs once per known entity: O(L·E), `options.py:371`).
2. **Commit 2, the retention lever, ONE of two** (decided by commit 1's table, by the ladder, not asked): (i) `ledger_cap`
   raised (H-09's value is injected and unruled, so this overturns no doctrine), or (ii) `known_persons` also reads the
   holder's own person-to-person `p.tenures`, which eviction never reaches (CR-83 already names "his own tenures with the
   other"). Faction co-membership cannot be read person-side (`person_q.py:528`: membership is world truth), so (ii) alone
   does not keep CR-81's faction acquaintances. Falsifier: the tip's 0/6/0 of 236 at cap 200 against the lever; planted
   failure: the cap back to 200 reddens the retention test. Declared mover of every hash that reaches the cap.
3. **Commit 3, readers list** (the old commit 4's measurement half): every reader of `Claim.confidence` and age (the
   integration read's section B is most of it). Hash EQUAL.
4. The old commit 3 (opinion into `stance`) and commit 4's build half **leave CR-82** and are folded into CR-83's design
   (§2.2). The revert notes in ED-IN-0320 to 0323 that say "drop commits 3 and 4" re-point to CR-83.

### 2.2 CR-83 (design-first, drafted beside B10-13, before CR-27 and CR-31) absorbs

The opinion-outlives-the-claim question **as a measurement first**: deed claims evicted before N seasons at the shipped
lever. If zero, R2 is met and nothing is built. If non-zero, a DESIGN decision with a **matrix change**
(`write_matrix.yaml` row steps), a single owner for the judgment (not `stance` and `regard` both), and a control that every
reader of `stance_toward` (legitimacy, `_bond`, `teller_weight`, `choose`, forgive, `reception`) is unchanged. Also the
subject-fit term (R5) in `person_q`, passed to `queries/` as a closure so `decision/` is never imported (`world_q.py:2672`),
and `regard`'s recursion constraint (`deeds_judged` must stay unweighted, `person_q.py:102-104`). **The event-identity gap**
(a "similar claim" is the exact `(subject, predicate, value)` triple, so news of a second killing by the same person from an
origin already behind a copy is dropped) is recorded here and not fixed: no field is coined.

**Position order is preserved so τ is not stale:** only commits 1 to 3 run in B10-09, ahead of CR-17.

## 3. The ten attributes (ED-IN-0328), a registry rewrite, new position CR-84

**Mapping** (`references/descriptor_registry.yaml:36-48`): Strength unchanged; Agility → **Coordination**; Endurance
unchanged; Acuity → **Reason**; Focus unchanged; Will → **Spirit** (Willpower); Attunement loses the Perception alias;
Charisma → **Presence** (Charisma); **Perception** added; **Grace/Composure** added; **Bonds dropped**. 9 − 1 + 2 = 10.

**Decisions taken by the ladder (each `[ASSUMPTION; medium; Jordan to correct]`, none asked):**
- **Bonds is dropped**: the count of ten is ruled (ED-IN-0185, quoted `part15.md:65`) and Jordan enumerated ten without it;
  keeping it makes eleven. Revert: keep Bonds as an eleventh and the count is re-ruled. Cost: `test_knot_pool_formula.py:52-57`
  pins Bonds' gate and cap against a `.designs` doc and reddens; the oracle `knots.py:185-216` reads `bonds` (an oracle, not
  game code).
- **Keys stay stable; names and aliases change.** `attr.body.agility` is named Coordination (aliases Agility, Dexterity);
  `attr.mind.acuity` named Reason (aliases Acuity, Faculty, Forecasting, Predicting, Reasoning, Cognition); `attr.mind.will`
  named Spirit (aliases Will, Willpower); `attr.social.charisma` named Presence (aliases Charisma). New keys
  `attr.mind.perception` and `attr.social.grace`. A key rename after CR-20 lands is a schema re-pin (`part15.md:66`), so
  keeping keys is the cheap path; the cast's `stats:` spellings (`cognition`, `social`; `npc_registry.yaml:57-61`) must keep
  resolving through aliases.
- **Grace is the primary name, Composure an alias**, because Jordan's gloss (composure, calm, etiquette, manners) is Grace's
  breadth. **The collision is narrower than ED-IN-0328 says:** social contest retired Composure at CR3
  (`engine/tests/test_contest_kernel.py:27-31`; `_kernel_tests.py:799-804`), so no social-contest reader exists; the only
  live "Composure" in code is the knot damage track (`systems/threadwork/sim/opposing.py:56-59`;
  `systems/fieldwork/sim/knots.py:84`; `engine/engine_params/sim_params.json:1996,3607-3641`), and the registry lists it as
  a derived value (`descriptor_registry.yaml:244`). Alias `Composure` must not make `resolve('Composure')` return the
  attribute where the knot track is meant: the build checks and, if it does, omits the alias. `Grace` also soft-collides with
  the petition "grace threshold" (oracle: `modes.py:79`).
- **Other collisions** to handle in the rewrite: "Reason" is conviction `conv.reason` (`names_index.yaml:96`); "Faculty" is
  `sigma.py::faculty`; "Presence" is `world_q.presence`; "Poise" is `pc.poise`; Nerve, none.
- **Resolve is not an attribute** (Jordan confirmed): it is Spirit's derived value. Left out.
- **The Godot bar stays**: `descriptor_registry.yaml:31` ("until the tenth is named") is literally lifted, but the ruling is
  hedged ("I think") and CLAUDE.md §5 binds Godot fields only to confirmed keys. IN FLUX stays until Jordan confirms.

**Where it lands: before CR-20 in B10-10** (CR-20 asserts nine keys and a pending tenth slot that refuses a
value; at ten the exporter clears the sentinel itself, `tools/export_descriptors.py:217-221`, and that exit cannot run).
Hash: EQUAL for the game (no `engine/season` or `modules` file reads `ATTRIBUTES`). Files: `descriptor_registry.yaml`;
`names_index.yaml` (checked by `tools/ci_names_consistency.py:12`); `engine/engine_params/names.json` and `descriptors.json`
(re-export); the stale second roster `alias_registry.yaml:21-56` (nothing reads it; fix or leave, say which); tests
`test_descriptor_registry.py:19,21,24-28,33,43`, `test_registry.py:90-94`, `test_names_chain.py:139-140`,
`test_tag_normalizer.py:36-37`, re-pinned to the new expectation. Control: every alias that resolved before still resolves
to the same key except the dropped Bonds, which resolves with a deprecation flag.

**v11 rows that change when CR-84 lands:** CR-20 ("nine keys", the pending-tenth exit, `vocation_attribute` rows keyed by
`verb_capability` values); CL-ATTR, M23, J-T2 and `part15.md` E-1 (answered: none of their three options matches, the
nearest is the suite's split); PC-14's `registry_key` map (`agi`→agility, `cog`/`spirit` through aliases, `att` null: Jordan's
Perception is now a candidate for combat's `att`, "attention", `combat_systems.py:1327`); CR-83's key wording.

**Combat's "nine attributes" at `hole_register.yaml:1352` are not the registry's:** they are `Combatant(strength, agi, end,
cog, att, spirit, focus, history, disp)` (`modules/combat/combatant.py:93-99`), with no Charisma or Bonds. The registry
rewrite does not touch them.

## 4. Risk tolerance (ED-IN-0328's tail): a duplicate, no position

ED-IN-0304 (2026-10-29, Jordan: "persons differ in risk appetite" and in decision horizon) already owns it: CR-17's follow-on
(`part4.md:129`) and CL-PERSON M40 (`part4.md:474-482`), a B10-19 design-first row whose build follows CR-17's last commit
and is HELD on M34-M37, M40 and E-4. The places it can act with no new apparatus: `score_terms` (`choose.py:129-148`), τ
(`choose.py:301`), `odds_of` mode (b) band odds (`sigma.py:367-404`), `crisis_weights` (`person_q.py:748`). **Action:** add
ED-IN-0304 to ED-IN-0328's citations by a correcting row; build nothing.

## 5. `lie` beside `forge` (ED-IN-0329): CR-27 as written, plus proximity

`forge` is an `uncontested_material` verb whose effect mints a document (`_eff_forge`, `effects_information.py:777`); a
forgery is caught by `ob += forgery_quality` (`modules/social_contest/roll.py:135-144`) and covert research of
`record.forged`. `lie` shares `tell`'s cell (stratum `social`), emits only `tell`'s kinds and has no effect function, so it
has no kind to be researched: its only route is `record(H, T)` pairing (`options.py:1540-1580`). The two detection routes
**cannot be made symmetrical** without giving `lie` its own kind, which CR-27 forbids by design. **Action:** CR-27 builds as
written; "alongside" is satisfied by adjacency in `verb_table.yaml` and a ledger citation. A forged `faction_sheet` sits by
ED-IN-0326 with Reason, not Attunement: an observation, unruled. ED-IN-0327 enters a lie at CR-19's competence (its sign
problem is already a RE-BASE note, `part4.md:144`) and a forgery through the examiner's `faculty` dice once CR-20's
`vocation_attribute` exists for `inquiry`.

## 6. Histories (ED-IN-0330, 0331): a design, not a rename

**What is eliminated, exactly:** the integer `history` fields that are summed into rolls: combat `Combatant.history`
(`combatant.py:93`), threadwork's term (`systems/threadwork/sim/operations.py:246`), knots (`knots.py:215-216`). **The
skill-shaped half already runs and is not eliminated**: `Person.capability` keyed by `verb_capability`, `faculty`
(`sigma.py:145-159`), `train`, the `practice` addend (`world_q.py:4093-4113`), `tradition`, and CR-33's `lifepath_templates`
(a lifepath expands into capability keys: literally "bundles of skills"). ED-IN-0330's "PRA" wording conflates the two.
Jordan had already written the intent at `proposals/2026-10-24-character-progression-adjudication.md:64`.

**Why it is a design.** Combat history is the roll's backbone, not a term among several: pool `max(5, history + 6)`
(`modules/combat/core.py:54-56`, checked), obstacle `defender.history / 2.0` (`core.py:115`, checked), read again at
`combat_systems.py:171,332,1053,1421,1441`, exported to the port as `READ_HISTORY_K`, `INIT_HISTORY_K`, `BASE_POOL`
(`combat_engine_v1.json:113,194,238`). In the season loop **history is never authored**: `seam/wrappers/combat.py:36-39`
leaves the class default 3, so every season fight rolls pool 9 against Ob 1.5. Removing or replacing it moves the hash of
**every season fight**: a declared mover for the PC lane, not for B10-09.

**Plan positions pushing the other way (conflicts):** REM-45 builds `min(3, history) + 3` (`part3.md:230`), switching a dead
term back on (today `min(3, history + 3)` is always 3, `operations.py:246`): **drop REM-45** (hash EQUAL, so free);
CP-T07-02 re-depends on it (`part14.md:42-43`): re-base; PC-14 makes `history` an editable attribute with
`set_attr('history', 7)` giving "pool 13, Ob 3.5" (`part4.md:922-924`): re-base items 1 and 7 and its exit.

**Hooks (ED-0331).** CR-33 stores the lifepath nowhere (`part4.md:314,318`), so a hook has no writer at build. Hook-shaped
machinery that exists: `goals.yaml`/`seed_goals` (`populated.py:818`), CL-OPEN's role-bound goal rows (`part4.md:460-472`),
CR-30 `heritage` (feeding `_term_marks`, `epistemic.py:918-924`). `Person.marks` is deleted. No `hook`/`life_path` code.

**New position CR-85, DESIGN-FIRST, in B10-10 before CR-33 and CL-CHAR** (they are one lane): one design file, no code, naming
(1) what replaces combat's `history` in `pool`/`Ob` (the `faculty`/capability route that other scales use, or a
combat-specific bundle) and the season-loop hash cost; (2) what a hook is, where a lifepath writes it, how it reaches play,
from the carriers above with none coined; (3) the oracles' fate (`systems/*/sim`), which are Python oracles the port
validates against, so a change is made at the owner and re-exported (CLAUDE.md §6). Its build lands in B10-11 (§11), not here.

## 7. The derived values, traced (the census and the duplicate survey)

21 registry derived values: **2 duplicates, 12 correlates, 4 single-owner, 3 absent.** The game code (`engine/season`) reads
none under its own name. Single owner (all `modules/combat/combatant.py`): Stamina `:45-47`, Max Wounds `:30-32`, Wound
Interval `:35-37`, Concentration as `conc_max` `:127,147`. Absent: Composure, Thread Fatigue, Resolve (`faculty` is a pool
size, not a cap). The derived scores with attribute formulas in game code are only those four plus TroopCount.

**Routed to the owning batch's re-base (V1), not new positions** (a finding needing no ruling is fixed in its own batch or
dropped, CLAUDE.md §0):
1. **TroopCount** has two weight-to-troop ratios: 1:1 at `massbattle.py:228`, and `under_arms_cap` = weight × 300 × 0.10 =
   30 per unit at `:255` (`troop_types/recruitment.py:78-80`); `settlements.provision` sizes it 1:1 again
   (`provision.py:16-17,38`); comments disagree (`massbattle.py:248` vs `recruitment.py:48`). One owner should be
   `Subunit.troop_count` (`units.py:646`). → B10-12 (mass battle). The compounded mixed-field arithmetic is the reader's
   inference, unrun.
2. **Health** is carried twice: season `Person.body` and module `WoundTracker`; into the fight `party_end` turns body bands
   into Endurance (`seam/wrappers/combat.py:130-138`), out of it `effects_combat.py:224` writes `body × left // full`. The
   tracker's own contract says it persists between encounters (`combatant.py:56-57`) and the seam rebuilds it. → B10-11
   with PC-14 and CR-85 (one design).
3. **Garrison Strength** is authored (`fort_level`), ignored, and the live reading collapses to `> 0` → WALLS
   (`terrain.py:133,143-144`). → B10-12.
4. Instrument-only readers: `person_q.legitimacy`/`stability` stand in for four derived values and nothing in the loop
   reads them (`harness/storybar.py` only). Record only.

## 8. Order, files, hashes

| step | where | files | hash | control |
|---|---|---|---|---|
| CR-82 commit 1 measure | B10-09 close two, after CR-25 | none | EQUAL | cap 200 reproduces 0/6/0 of 236 at the tip; told count first |
| CR-82 commit 2 lever | same | `fixtures.py` or `person_q.py::known_persons` | MOVER | retention test, planted failure |
| CR-82 commit 3 readers list | same | none | EQUAL | — |
| CR-17 | B10-09, last | `options.py`, `choose.py`, `fixtures.py` | MOVER | τ re-derived last |
| CR-84 attribute roster | B10-10, before CR-20 (the card puts CR-68 and CR-69 first) | registry, mirrors, 9 test files | EQUAL (game) | aliases resolve as before |
| CR-85 design (histories, hooks, combat input) | B10-10, before CR-33; build in B10-11 (§11) | one `proposals/` file | none | its own falsifier |
| REM-45 dropped; CP-T07-02, PC-14 re-based | at their batches | plan rows | — | — |
| CR-83 design (knowledge, fit, truth, `said_of`, opinion measurement) | drafted beside B10-13; v11's needs cell (CR-31, CR-17) stands | one `proposals/` file | none | its own falsifier |

File edges: `witness.py` (CR-79, maybe CR-29), `person_q.py` (CR-27, CR-31, CR-83), `options.py` (CR-17, CR-19, CR-27, CR-31,
CR-79), `fixtures.py` (nearly all). No two of the building steps are in flight together (P13).

## 9. Open for Jordan: only what survives the ladder

1. **Is `write_matrix.yaml` Layer-1-bound?** If an opinion-persistence mechanism is ever built (CR-83, only if its
   measurement is non-zero), it needs a row to gain a step; whether that is an agent edit or Jordan's is unread in the tree.
   Blocks nothing now.
2. Everything else above is taken by the ladder and tagged as an assumption with its revert. The ones that most change the
   game, so worth a glance: **Bonds dropped**; **Grace as the primary name**; **the readers' choice of lever** (cap or
   tenure read) after the measurement; **combat history's replacement** (CR-85).

## 10. Corrections owed to the ledger rows already written

ED-IN-0328 cites no ED-IN-0304 and says Composure is "also a derived debate damage track" (the debate track was retired at
CR3; the live clash is the knot damage track); ED-IN-0328, 0330 and 0331 cite this file, which now exists. ED-IN-0330's
"PRA" wording conflates the history fields with the capability carrier that already replaces them. A correcting row
(ED-IN-0333) records these when the plan is accepted.

**Could not verify** (from the readers): the current chained-told-claim
count (H-237 is a session probe); REM-30's creation sheet (not opened); the cast's 29 `stats:` blocks; run time and memory
(the measurement is running).

## 11. Corrections applied after the sequencing check (2026-11-04; one round, then folded into v11)

A read-only check of this plan's order, gates and counts found the plan sound on facts and defective in these places; each
is taken by the ladder and tagged `[ASSUMPTION; medium; Jordan to correct]`.

1. **CR-82 commit 2 is the cap alone.** Lever (ii) (`known_persons` reads own tenures) is dropped: it cannot keep CR-81's
   faction acquaintances (its own test would fail by construction), it makes later tenure writers (CP-T10-06 `kin`, CP-T10-08
   `marry`, CP-T03-09 `capture`) undeclared hash movers, it falsifies IN-32's "`known_persons` keeps its three sources"
   (`part3.md:241`), and `said_of` runs per known entity so it costs time too. Commit 2 therefore also states: (a) a **run-time
   ceiling**: the chosen cap is the smallest value at which the acquaintance claims survive the horizon (eight seasons, two
   years, ED-IN-0332), and the commit records the measured wall time of `engine/season/tests` and of `corpus_run` against the
   `season-tests` CI job's 30-minute timeout (`.github/workflows/valoria-ci.yml:368,390`); if no cap keeps both the horizon
   and the ceiling the commit **stops and reports**, because the ruling and the run cost then conflict and that is Jordan's;
   (b) the **HR-9 controls (2) and (4)** on seeds 0-4 at two seasons, new against base, as CR-28 read them (v11's CR-82 exit
   already carries them): a larger ledger feeds the CR-28 stamper more Propositions and can undo the pass B11-S4 assumes
   (`v11.md:111`); (c) the retention reading on seeds 0-2 (v11's seeds), not 0-1; (d) the control line is 0/6/0 at the tip.
   Readings already taken at cap 200 (CR-28's, CR-81's) stay valid as their own bases.
2. **CR-85's build lands in B10-11, not B10-10b** (B10-10b is declared EQUAL throughout and its identity control would read a
   season-fight move as a defect): design approved (ED-1094's merge default, like CR-83 and CR-38) before B10-11 opens;
   build after CP-T03-02 and before CP-T03-05. **More conflicts than §6 listed:** CP-T03-04 feeds an `arms` skill into the pool
   term `round(history) + 6` and its falsifier reproduces "the history-5 row" (a candidate host or a conflict: re-based as
   CR-85's consumer); CP-T03-05 exports `pc_matchup.json` with history at its default (it would stale); PC-14 item (5) adds a
   typed `attributes` export to `combat_engine_v1.json`, `history` included; PC-17 calibrates its tempo constant against
   `INIT_HISTORY_K`. Each gets a re-base line naming CR-85.
3. **CR-83 keeps v11's needs cell (CR-31, CR-17)**; it is *drafted beside B10-13*. The words "before CR-27 and CR-31" are
   struck: CR-27 builds as written (§5) and needs nothing from CR-83.
4. **CR-19 ships its factor at gain 0** until CR-83's design gives a separator between a lie and a truth; the flip to a live
   gain is a declared mover scheduled by that design. CR-19 is then EQUAL (the function in place, which is all B11-S5 needs,
   `part3.md:411`). CR-27's exit gains the falsifier: a lie told to receivers at Attunement 2 and 6, where the 6 does not
   hold it higher. In the realm CR-19 is latent today (the cast's `stats:` carry no Attunement key).
5. **CR-33 is gated on CR-85's design** (the lifepath id is stored nowhere, `part4.md:314,316`, which is where a hook writer
   goes); if CR-85 is unapproved at CR-33's turn, CR-33 builds as written and records the re-pin it owes. CL-CHAR's piece
   check also reads CR-85.
6. **CR-84:** "before CR-20", not "first commit". The mirror list adds `engine/engine_params/value_pointer_links.json` (links
   `PERCEPTION_BANDS` to Attunement and `KNOT_BONDS_MIN` to Bonds) and `tests/valoria/test_link_values_pointers.py`; the
   test-file count is as named in §3, not "9". **CL-ATTR narrows to M24 (the training composition); it is not closed.**
   Whether `tools/ci_names_consistency.py` refuses the new aliases (for example Reason, also a conviction) is **not verified**
   and is read first in the build.
7. **REM-45 dropped:** CP-T07-02's needs cell, B10-15's order, exit and hash lines and M18 "TAKEN (b)" (`part6.md:152,299,351`)
   change; CP-T07-02's re-base revives HR-7's superseded override without its "waits on M18" clause: the actor adapter reads
   `_actor_pool`'s `min(3, history + 3)` as the code has it, and the term's fate goes to CR-85.
8. **The fold lands before B10-10 opens**, because B11-S2 runs in a parallel worktree on the premise that it edits no file
   B10-10 edits (`part3.md:88`).
9. **ED-IN-0333 (the correcting row)** also re-points ED-IN-0320 to 0323's "drop commits 3 and 4" reverts to CR-83.
