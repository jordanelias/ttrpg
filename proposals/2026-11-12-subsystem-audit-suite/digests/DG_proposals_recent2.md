# Digest proposals_recent2

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: proposals dated 2026-09-20 or later, second half (100 assigned entries, 2026-10-21 through 2026-10-25 families: verb-key-rows, system-description, subsystem-completion, character layers, master-workplan-v10 build files, thrust-layer).
**Reading-depth note (honest):** the assignment is about 3.2 MB (~30,000 lines), more than one session can hold. Each entry begins with a depth tag: `[READ IN FULL]`, `[READ PARTLY: what was and was not opened]`, or `[HEADINGS+HEAD ONLY: ...]`. Nothing is summarised from memory; `:line` references were opened. Where a tag says partly, claims about the unread remainder are marked `[UNVERIFIED]` or omitted.
Ratification summary for this lane: nothing in these files is RATIFIED by its own Status line. Every proposal file is PROPOSED / HELD BACK; the master-workplan-v10 build files are "instructions under the adopted plan" (the plan itself was adopted, ED-IN-0299 / ED-IN-0301 cited inside the files); the system-description suite is PROPOSED (reference).

### proposals/2026-10-21-verb-key-rows.md
- **What it is:** [READ PARTLY: lines 1-60, 112-140 and the ## / ### heading index of 346 lines; the §2 disposition table (lines 167-346) not opened line by line] Part 1 of 3 of "Verb key rows": every folded name of Jordan's uploaded verb list (~120 names) given one disposition (KEY / DERIVED / PARKED) and the key rows needed; static reading, 2026-10-21.
- **Status:** "PROPOSED (2026-10-21). Not ratified ... Static reading. No season, probe or test ran ... No proposed row was loaded; every claim that a skeleton loads is unverified." (:2). Reading: PROPOSED, never built as written; the verb table has since grown (62 rows per B10-18b), so which keys landed is [UNVERIFIED].
- **Bears on:** CORE, SC, PC, MB, FI, FA, SE, WR, CHAR.
- **Content that matters:**
  - Terminology trap: here a "key" is "a verb's own row in `verb_table.yaml` that reaches the world through the host's code" (:42-45). It is NOT the retired Key substrate (ED-IN-0232; `keys.py`, echo transport) — same word, unrelated sense; the doc predates or ignores that retirement.
  - The requirements any new row meets at import: K-1 (row fields), K-2 (writes are `write_matrix.yaml` rows), K-3 (refusal kind for every failable clause), K-4 (effect or declared decline; `manifest/registry.py:599,:637`), K-5 (seven alignment cells or `uncelled:` line), K-6 (a `verb_capability` key only if a pool is rolled and differs; only two entries, `tell`/`speak` → `copying`), K-7 (optional creed cell) (:48-110).
  - Disposition test in order: PARKED (needs unbuilt mechanism) → KEY (a reader keyed by verb name must tell it apart, or precondition/write/Event kind differs) → DERIVED (recovery predicate) (:112-139). `appoint` is `confer` on a seat whose `conferral` is `appointed`; no row may add a basis (ED-IN-0256, `conferral_bases` closed).
  - Names folded into `tell` that the game can tell apart: `confide`, `praise`, `insult`, `threaten` (own rows); `confess`, `confront` (recoverable by predicate); `counsel`, `warn`, `testify`, `flatter` not with confidence (:34-39).
  - Recommends one host rename `examine` → `search` (:30).
- **Conflicts / stale:** the verb count (46 names in its import) differs from 56 (thrust-layer) and 62 (B10-18b). Uses "key" for what the repo's later rulings retired under the word Key (see above).
- **Open items:** §7 says "None survives CLAUDE.md §0's five answer-it-first tests" (part 3 :317).

### proposals/2026-10-21-verb-key-rows_part2.md
- **What it is:** [READ PARTLY: heading index of 540 lines and lines 1-9 only] Part 2: §3.0-§3.1.9, the key rows' skeletons.
- **Status:** same PROPOSED status as part 1 (:2).
- **Bears on:** PC, MB, SC, FI, WR.
- **Content that matters:**
  - Nine key skeletons: `accept` (KEY on `fight`, shipped, one amendment), `hire_troops` (on `levy`), `sack` (on `pillage`), `confide` (on `tell`: shared contest, no body), `praise` and `insult` (rows on `tell`'s prize), `audit` and `scout` (on `survey`), `teach` (on `train`) (:55-494).
  - §3.0 states "the rules every skeleton below follows" (:11).
  - [SKIPPED: /home/user/ttrpg/proposals/2026-10-21-verb-key-rows_part2.md body, lines 10-540 — not opened; per-skeleton cell values unread]
- **Conflicts / stale:** `levy` was renamed `requisition` (#482) per CL-TROOP in B10-19, so `hire_troops` on `levy` is stale-named.
- **Open items:** none read.

### proposals/2026-10-21-verb-key-rows_part3.md
- **What it is:** [READ PARTLY: lines 214-345 (§6 cost and ordering, §7) and heading index of 320 lines; §3.1.10-§5 not opened] Part 3: `propose`/`allege` (on `utter`), `threaten` (on `tell`), parked keys, why no per-row value fan, host-row edits, cost and ordering.
- **Status:** same PROPOSED status (:2).
- **Bears on:** SC, CORE, FA, FI.
- **Content that matters:**
  - Cost table (:216-226): 6 new rows with host built (`confide`, `praise`, `insult`, `threaten`, `propose`, `allege`), 5 once host exists, 1 amended (`accept`), 11 waiting (`assassinate`, `capture`, `champion`, `besiege`, `testify`, `flatter`, `track`, `coup`, `repay`, `bargain`, `navigate`).
  - Ordering (:260-277): buildable now: `accept`'s kind, `confide`, `threaten`, `propose`/`allege`, `commit` one-per-actor decline, `release`/`transfer` earned kinds, the rename; `praise`/`insult` only after H-194 ships `stance_polarity: declared` (under `legacy` the stance term cannot separate them).
  - Hash/emission moves (:295-315): `confide` makes `confidence.broken` emittable (never emitted at `telling_privacy: 0`); `threaten` deposits an intent claim not present at `intent_disclosure: 0.0`; the `examine` → `search` rename moves every `examine` act id.
  - Three fold lines in the upload are wrong against code: `designate`/`elect` as bases, `annex` under `seize`, peace as a covenant term (peace is release of a war commit) (:289-293).
  - Chooser growth is formula-only, unmeasured: `confide` adds |T|·|K| candidates (`tell`'s count again) (:243-257).
- **Conflicts / stale:** the thrust-layer register's wrong-kind formation tax (28.7% of acts) would rise with 6+ new rows that form on every referent; this file's chooser-growth note does not account for it.
- **Open items:** §7: none.

### proposals/2026-10-22-system-description/2026-10-22-system-description-00-overview.md
- **What it is:** [READ PARTLY: lines 1-93 and 260-282 and the heading index of 428 lines; §2-§5, §7-§9 not opened line by line] Suite index and overview of Valoria "as a game system": breakdown, reachability matrix, ranked defects, comparison handles; written at `a4ca9a5` (2026-10-21), revised in round 3 at `51d7b05`.
- **Status:** "PROPOSED (reference). Merging this PR ratifies nothing; ... reference, not a ruling" (:3). Reading: historical-but-useful snapshot of 2026-10-22; later superseded in specifics by thrust-layer probes (P1/P10 on 2026-10-25), the v10 plan, and B10 work.
- **Bears on:** CORE, DICE, CHAR, PC, MB, SC, FI, WR, SE, FA, PROCESS.
- **Content that matters:**
  - Grade rule (:34-48): RUNS-IN-LOOP / RUNS-IN-LOOP at control / TESTS-ONLY / DESIGN-ONLY; "a refusal gate firing is not the verb executing". "att" in the control = acts that reached the fold (`d.resolved`), not acts formed; 275 acts in seed 0 are formed and refused before the fold (the same G-02 gap the thrust register measures as 329) (:50-62, :279).
  - Verdict (:65-91): "a seeded, reproducible agent simulation without a player"; 53 verb rows (47 admitted; 46 choosable); 3 of 9 ruled requirements met, 5 partial, 1 not met, milestone NOT MET; seams vary one input to combat (`end`), troop count/morale/terrain to mass battle, a default pool plus bench terms to social contest; `Person.capability` empty on 83 of 83 realm persons; social roll is a 2-die pool vs Ob 2, fails 74%.
  - Ranked defects (:260-282): chooser sees verb identity not consequence (13 of 53 verbs without alignment cell; 37 of 83 actors cohorts with no pursuit vector); 19 verbs always refused; initiator of violence cannot die (33 of 59 realm calls felled the actor); no ending reached; seven of 32 built seats (King, Queen, Prince, Princess, Duchess of Hafenmark, Duke of Valorsmark, guild-leader seat `off_npc_084`) have no conferral basis, King dies at tick 0 in every seed; `sigma_leverage.p_success` is a Gaussian stand-in understating Partial-or-better by 10-15 points (pool 2 / Ob 2: 14.4% vs 26.0% exact; pool 2 / Ob 1: 43.0 vs 58.0) while Layer 1 AX-7 says no state is hidden from the player.
  - "Documents lag the code": `CLAUDE.md` §3/§5 named `engine/autoload/dice_engine.py` and a campaign driver that do not exist (:272).
  - Seven handles (20G axes) for comparison in §7, and the "two proposal directories" (verbs, remediation) in §8 (not opened).
- **Conflicts / stale:** probe scripts cited are "NOT committed; only `ctl/` is" (:5); counts differ across files (53 rows here, 56 thrust, 62 B10-18b). The `ctl/realm_seed*_2seasons.txt` output files exist beside `control.py` but are not in this lane's list.
- **Open items:** the three "answer-first" lists in §9 (not opened).

### proposals/2026-10-22-system-description/2026-10-22-system-description-01-shared-reference.md
- **What it is:** [READ PARTLY: heading index of 329 lines and lines 1-17 only] Shared glossary, process-id key, action economy, time scales, resources, comparison axes for the ten tutorials.
- **Status:** no top Status line found by grep; has "Round-3 corrections" and "Audit fixes" sections (:289-303). Reading: reference snapshot.
- **Bears on:** CORE, PROCESS, all subsystems.
- **Content that matters:**
  - Sections: §1 Glossary, §2 Process-id key, §3 Action economy, §4 Time scales, §5 Resources, §6 Comparison handles (the repo's own axes), Discrepancies found (:249), Checks (:269).
  - [SKIPPED: /home/user/ttrpg/proposals/2026-10-22-system-description/2026-10-22-system-description-01-shared-reference.md body, lines 18-328 — not opened]
- **Conflicts / stale:** glossary terms (RUNS-IN-LOOP etc.) are file-local, not in a code registry.
- **Open items:** none read.

### proposals/2026-10-22-system-description/2026-10-22-system-description-02-t01-resolution-and-dice.md
- **What it is:** [READ PARTLY: heading index of 694 lines and Status (:27-37)] Tutorial T01: resolution and dice — how a contested act becomes one of four degrees and what moves the odds.
- **Status:** "The grades follow the corrected rule, ERRATA G1." (:27). d10 roll and margin ladder RUNS-IN-LOOP (133 graded rolls in seeds 0-1 through `tell`, `speak`, `determine`, `research`, `surveil`); room terms and ceiling RUNS-IN-LOOP at control (ceiling clips the result back to the default); advantage term (`leverage` literal 0.0), S27.4 refusal (never fires), fractional obstacles TESTS-ONLY (:27-37).
- **Bears on:** DICE, SC, CORE.
- **Content that matters:**
  - Structure: §0a how it plays, §1 pieces, §2 how it works, §3 worked example, §4 what you can do, §5 pursuing goals, §6 connects, §7 as proposed, §8 traps, §9 checks (:9-648).
  - Overview-level facts (00 :65-93, :272): social roll is 2-die pool vs obstacle 2 and fails 74%; `p_success` stand-in understates by 10-15 points; ceiling = default.
  - [SKIPPED: tutorial bodies lines 38-693 — not opened]
- **Conflicts / stale:** the T01 proposal file (subsystem-completion-01) is derived from this.
- **Open items:** none read.

### proposals/2026-10-22-system-description/2026-10-22-system-description-03-t02-season-persons-choosing.md
- **What it is:** [READ PARTLY: heading index of 879 lines and Status (:24-31)] Tutorial T02: the season, the person and how an actor chooses (worked example Saemund Haelgrund, Senior Inquisitor, tick 0).
- **Status:** "Status: RUNS-IN-LOOP. ... the chooser is built only by harness code: `make_chooser` has no call site in `loop/`. Several of its terms are RUNS-IN-LOOP at control: scar weight shift, confliction damping, declared intent, and the urgency term. Conviction crisis RUNS-IN-LOOP per seed: 5 folds at seed 0 and 3 at seed 2, all at tick 1, none at seed 1" (:24-31).
- **Bears on:** CORE, CHAR, FA.
- **Content that matters:**
  - Season = seven steps, five rounds (§2.1); candidate formation, scoring (pursuit + stance + urgency), ordering at tau 0.1, budget and packing, release, events to beliefs (§2.2-§2.8, :186-339); predicting what a person will do (rules of thumb, :339).
  - Errata G12: "72% overridden" is a harness-slice reading with no season (`decision_spread.py:23-28`): 28% of strict-top cases (16% of all; 222 more are ties).
  - [SKIPPED: bodies lines 32-878 not opened]
- **Conflicts / stale:** `make_chooser` call-site claim: harness-only (matches thrust probes).
- **Open items:** none read.

### proposals/2026-10-22-system-description/2026-10-22-system-description-04-t03-personal-combat.md
- **What it is:** [READ PARTLY: Status (:29-35) and first lines of §0a] Tutorial T03: personal combat.
- **Status:** "The duel engine MC/ (5,643 lines) is RUNS-IN-LOOP in its default build only: seed 0 `fight` 7/4, `accept` 18/11, `challenge` 23/6. Weapons, armour, traditions, abilities and every attribute except endurance are TESTS-ONLY. Yield is TESTS-ONLY. Duel terms, capture, guards, ranged arms and played fights are DESIGN-ONLY" (:29-35).
- **Bears on:** PC, CORE, CHAR.
- **Content that matters:**
  - Every realm person has body 1000 at build (`FX:217` `condition_scale`); every fighter is the class-default Combatant (`arming`, `light`, tradition `none`) except `end` (derived from body bands) (:42-44).
  - Round-3 probe: 33 of 59 realm calls felled the actor, none written (00 :272).
  - [SKIPPED: bodies — not opened]
- **Conflicts / stale:** PC-10a landed since (inert); duel terms still unwired.
- **Open items:** none read.

### proposals/2026-10-22-system-description/2026-10-22-system-description-05-t04-mass-battle.md
- **What it is:** [READ PARTLY: Status block (:43-60) of 770 lines] Tutorial T04: mass battle.
- **Status:** "Status: TESTS-ONLY." (:43). In the control run `march` reaches the fold and is declared at seeds 0/1/2 with attempted/ok 21/21, 10/10, 4/4; every declared march is then refused, so `field.won`, `field.lost`, `field.unopposed` and `army.arrived` are 0 in all three. Engine runs only under tests, harnesses and direct calls (:43-55).
- **Bears on:** MB, CORE, FA.
- **Content that matters:**
  - Hand-built `march {subject: set_s_036}` by `p_npc_033` via `off_npc_033` gives `march.declared` then `field.lost` (2 attackers, Σ weight 2 vs 6; each attacker's body 1000 → 20) at seeds 0,1,2 (test `test_march.py:82-136`) (:51-55).
  - Mass-battle engine size: 10,154 + 3,089 LOC against a seam that varies troop count, morale start and one terrain row (00 :72-76).
  - [SKIPPED: bodies — not opened]
  - Sizes (opened by grep, not read in context): battlefield is a 51 x 51 cell grid, side A starts at row 34, B at row 15 (:163); a Subunit is one block with per-cell troop and morale grids (:166); troop-type presets (levy 1/1/2; light inf 3/3/4; heavy inf and pike 4/4/5; cavalry 5/5/5; knights_templar 5/6/6) (:168); the army rout line is `hp < 100`, so for a one-subunit army the binding rout line is 100 troops (:185, :219).
  - Seam fact: `resolve_field` (`MB.py:306`) builds per side ONE Unit with ONE Line subunit of `infantry` (:256) — the engine's cell grid, per-cell grids and formations are not reached from the season by natural play. This is the premise an MB audit against the cell-based design intent must test.
- **Conflicts / stale:** the cell-based approach and weapon-carry trade-off named in AUDIT_BRIEF are not examined at line level here [UNVERIFIED].
- **Open items:** none read.

### proposals/2026-10-22-system-description/2026-10-22-system-description-06-t05-social-contest.md
- **What it is:** [READ PARTLY: Status block (:34-46) of 651 lines] Tutorial T05: social contest including proceedings.
- **Status:** season roll RUNS-IN-LOOP (degenerate: pool 2, leverage 0); `tell` executes on all three seeds, `speak` seeds 0 and 2, `determine` seed 1 only (one Partial), `argue` none (TESTS-ONLY), `commit` seeds 1 and 2 (one each), `convene` seed 2 (1 of 5), `carry` none; arrangements and speech kinds loaded and almost unread; the Bout kernel TESTS-ONLY; lexicon's seven suites DESIGN-ONLY (:34-41).
- **Bears on:** SC, FA, FI, DICE.
- **Content that matters:**
  - "Two things share the name 'social contest'": (A) the season roll (one dice roll per act) is what runs; (B) the Bout kernel, a multi-exchange rhetorical duel, is a tested laboratory the season loop never calls; code says "KEEP THIS ROLL, DO NOT ADOPT THE KERNEL ... the timing of its retirement is Jordan's, SM-15" (:43-48).
  - Round-3: `agon_harness.py` is a stdin-played kernel contest that never seeds `random` (00/13 R-F4).
  - [SKIPPED: bodies — not opened]
- **Conflicts / stale:** B10-Z SC-05 would delete the kernel (`systems/social_contest/sim/contest/`).
- **Open items:** none read.

### proposals/2026-10-22-system-description/2026-10-22-system-description-07-t06-fieldwork-and-information.md
- **What it is:** [READ PARTLY: Status table (:55-68) of 943 lines] Tutorial T06: fieldwork and information (WITNESS, claims, inquiry, documents).
- **Status:** table of grades: WITNESS fan-out, refraction, decay, cap, eviction RUNS-IN-LOOP; `co_located`, `chronicle`, `document_key` channels RUNS-IN-LOOP; `witness_key` TESTS-ONLY (0 `firsthand_via_knot`); what an inquiry uncovers (found deposit) TESTS-ONLY (0 found deposits in seeds 0,1,2); `give` 0 of 16 at seed 0; `destroy_record` TESTS-ONLY (withheld); `systems/fieldwork/sim/knots.py` TESTS-ONLY (unplugged) (:55-68).
- **Bears on:** FI, WR, CORE.
- **Content that matters:**
  - Inquiry finds nothing in the realm run: `examine` never passes admission; FI-03's trail deposits nothing in seeds 0-2; a Partial finding closes that trail to its finder for good (`epistemic.py:356-366`) (00 :274).
  - `post_remit` slot: at tick 0 the King's obligee `p_npc_070` holds an `inferred` claim of a refused royal act (test `test_obligees.py:167`).
  - [SKIPPED: bodies — not opened]
- **Conflicts / stale:** AUDIT_BRIEF noir/detective intent (case-building) vs the system: "no case object" per T06 completion.
- **Open items:** none read.

### proposals/2026-10-22-system-description/2026-10-22-system-description-08-t07-threadwork.md
- **What it is:** [READ PARTLY: Status (:65-80) of 765 lines] Tutorial T07: threadwork.
- **Status:** "TESTS-ONLY for the seven operations, the Coherence store, collective and opposed workings ... Nothing here is RUNS-IN-LOOP at any seed." DESIGN-ONLY for rendering and for `thread_read` and every other threadwork verb in the loop (:65-72).
- **Bears on:** WR, PC, CHAR.
- **Content that matters:**
  - `Person` declares no TS or Coherence field; `(Person, coherence)` is "unproduced" in `write_matrix.yaml:185-192`; `ts:` values in `references/npc_registry.yaml` are read by no season code (:77-80). (Later: `thread_sensitivity` field added — see progression adjudication §2.1.)
  - Co-movement and threadcut implemented, executed only by oracle script `t07/cm_tc.py` (:68-70).
  - [SKIPPED: bodies — not opened]
- **Conflicts / stale:** `Person.thread_sensitivity` now exists (carriers.py:708-717 per the 2026-10-24 adjudication), so "declares no TS field" is stale.
- **Open items:** none read.

### proposals/2026-10-22-system-description/2026-10-22-system-description-09-t08-settlements-governance-economy.md
- **What it is:** [READ PARTLY: Status (:24-34) of 846 lines] Tutorial T08: settlements, governance, economy.
- **Status:** MATTER (draw, yield, wear, term lapse) RUNS-IN-LOOP (hunger→body at control: inert); `move`, `issue`, `dispatch`, `release` execute in all three seeds; `transfer` seeds 0 and 2; `oblige` (24/22) and `confer` (5/1) seed 1 only; upkeep renewal, shortfall→relief loop, CENSUS individuation, `requisition`, `revoke`, `establish`, `work`, `restore`, `sabotage`, `found`, `build`, `migrate` TESTS-ONLY (0 successes in seeds 0-2); tax, ration, proclaim, arrest, pardon, craft, exchange, hire, debt DESIGN-ONLY (:24-31).
- **Bears on:** SE, FA, CORE.
- **Content that matters:**
  - Scene budget `max(1, 5 + 1 per live hold − body bands fallen − 1 per travel leg)` (:33-34); errata G11: every live hold counts incl. held Records; budgets drift up (seed 0 mean 5.57 at build, 7.69 after tick 1).
  - [SKIPPED: bodies — not opened]
- **Conflicts / stale:** thrust-layer P1 at 4 seasons: restore 0/250, tend 0/302, build 0/230, found 1/208, work 3/726 — consistent with the TESTS-ONLY grades.
- **Open items:** none read.

### proposals/2026-10-22-system-description/2026-10-22-system-description-10-t09-factions-war-diplomacy.md
- **What it is:** [READ PARTLY: Status (:40-54) of 732 lines] Tutorial T09: factions, war, diplomacy.
- **Status:** mixed: membership, the faction view, faction-goal salience and `survey` RUNS-IN-LOOP; `oblige` RUNS-IN-LOOP at seed 1 only (22 of 24); `commit` once each at seeds 1,2 on uttered Propositions, never on a faction; `dispatch` executes (6,7,10 per seed) but writes nothing; `covenant`, `seize`, `sabotage`, `at_war`, the march arrival TESTS-ONLY; `declare`, `recruit`, `conspire`, `assign` DESIGN-ONLY. "No computed defection and no computed war: 0 faction `commitment.ended` and 0 WAR Propositions in seeds 0-2" (:40-50).
- **Bears on:** FA, SC, CORE.
- **Content that matters:**
  - Factions are Propositions plus `commit` edges and never act (A5 appendix); G6: no stored Faction/Settlement/Province entity; `faction_q.Faction` is a frozen per-barrier view dataclass.
  - [SKIPPED: bodies — not opened]
- **Conflicts / stale:** `faction_q.head` always `None` (T09 completion A1).
- **Open items:** none read.

### proposals/2026-10-22-system-description/2026-10-22-system-description-11-t10-world-travel-survival-npc-life.md
- **What it is:** [READ PARTLY: Status (:27-37) of 828 lines] Tutorial T10: world, travel, survival, NPC life.
- **Status:** WT containment ladder, presence, `move`, leg cost, MATTER's leg end RUNS-IN-LOOP; `migrate` TESTS-ONLY (0 successes in 81, 143, 143 acts that reached the fold); weather, hunger, ageing, illness RUNS-IN-LOOP at control (inert at shipped values); routes, terrain, exposure, POIs, foraging DESIGN-ONLY ("the data exists and no season code reads it"); NP cohorts, named persons, body bands, regard, `forgive` RUNS-IN-LOOP; `tend`, `train` TESTS-ONLY; kin, birth, marriage, household, inheritance DESIGN-ONLY or absent (:27-36).
- **Bears on:** WR, SE, CHAR.
- **Content that matters:**
  - 37 weight-2 cohorts that eat and 46 named individuals that act (A6 appendix).
  - [SKIPPED: bodies — not opened]
- **Conflicts / stale:** none checked.
- **Open items:** none read.

### proposals/2026-10-22-system-description/2026-10-22-system-description-12-reference-appendices.md
- **What it is:** [READ PARTLY: lines 1-12 and heading index of ~2,600 lines; 266 KB, bodies not opened] First-draft appendices A1-A8 (engine core; agents/verbs/data; PC and MB; threadwork; settlements/governance/factions; economy/world/NPC life; social contest; fieldwork/information), "verbatim Stage-2 syntheses".
- **Status:** "superseded where the tutorials (02–11) or the errata (13) differ" (:3). Reading: superseded as authority; useful as a map of sources.
- **Bears on:** all subsystems.
- **Content that matters:**
  - Index of subsections with line numbers (:13-2516): A1 resolution engine (:37), season loop (:133), harness (:257); A2 persons (:385), chooser (:474), verb system "53 rows; 47 admitted; RUNS-IN-LOOP for 41 verbs (22 with outcomes), the 92-verb roster DESIGN-ONLY" (:567), query layer (:718); A3 PC (:813), MB "cell-grid formation-warfare engine ... TESTS-ONLY in practice" (:969); A4 threadwork (:1129); A5 GV (:1471), FA (:1649); A6 EC (:1807), WT (:1924), NP (:2023); A7 SC (:2124); A8 FI (:2438) and information/epistemics (:2516).
  - States its own known errors: grade conventions differ, scene-budget "dispute", `write_matrix` has 40 rows, scar written at RESOLVE, FA roster (:3-6).
  - [SKIPPED: /home/user/ttrpg/proposals/2026-10-22-system-description/2026-10-22-system-description-12-reference-appendices.md lines 13-2603 — 266 KB, not opened beyond headings]
- **Conflicts / stale:** a 266 KB file that duplicates and is overruled by files 02-11 and 13; candidate for deletion by the repo's own retirement rule if the suite is not wanted.
- **Open items:** none.

### proposals/2026-10-22-system-description/2026-10-22-system-description-13-errata-and-audit-record.md
- **What it is:** [READ PARTLY: lines 1-62, 313-380 and heading index of 455 lines; audits D, E, F, G-L finding tables (lines 105-312) and Part 3 remainder (380-455) not opened] Errata G1-G20, per-subsystem corrections, cross-cutting rulings, every round-1/round-2 audit finding, control-run method, round-3 findings R-F1...
- **Status:** no Status line; "Authoritative over the draft appendices" (:10). Reading: authoritative within the suite; the suite itself is a snapshot.
- **Bears on:** CORE, all subsystems, PROCESS.
- **Content that matters:**
  - G1 grade rule (RUNS-IN-LOOP / at control / TESTS-ONLY / DESIGN-ONLY); G2 counts: ctl files win; G3 53 rows, 47 admitted, 46 on the chooser menu, 7 contested rows (argue, determine, speak, tell, fight, accept, march); G9 MATTER kills nobody at shipped values — every realm death is combat; G12 chooser: score = alignment + stance + inert urgency; 72% override figure is a harness-slice reading; G16 no player interface in code (D-2 RULED yes: RB-3 builds IN-46, IN-47); G17 designed-but-deleted layers (`victory`, MS/peninsular strain track, faction_state Mandate/Treasury, accounting_sequence, piety_track); no ending in the running loop; G18 even fully executed, the 40-item remediation plan cannot make THE NINE met; G19 verbs proposal override rule R-01..R-29; G20 attributes: nine ruled names (Strength, Endurance, Agility, Focus, Acuity, Will, Attunement, Charisma, Bonds), tenth unnamed (ED-IN-0301) (:13-62).
  - Round-3 R-F1: seven of 32 built seats have no conferral basis; King dies at tick 0 in every seed; seats vacated after two seasons 8/7/10 (:332-345). R-F2: a `revoke` can pass only through `off_duke_valorsmark`, vacant from tick 0 → no `revoke` can pass thereafter. R-F4: no player interface reaches the season loop; only `dispatching_chooser`, exercised only by tests. R-F5: hand-built acts run (march → `field.lost`); non-resolvable `exchange` raised `Unspecified` and aborted the season, a four-act scene raised `Ungraded`.
  - Round-3 method: thirteen read-only Opus disposition critics routed ~70 precedent games to the ten tutorials; "No LACKS row survived §0's five-step triage as a Jordan question" (:332-340).
- **Conflicts / stale:** "probes ... were session files and are not committed; their numbers cannot be reproduced from the tree" (:336-338).
- **Open items:** none stated.

### proposals/2026-10-22-system-description/ctl/control.py
- **What it is:** [READ IN FULL, 28 lines] Scratch control script from the system-description suite: runs `build_realm(seed)` for N seasons with the shipped chooser and prints per-verb attempted/ok counts and ~17 event-kind counts.
- **Status:** script, no Status line. Reading: historical instrument; hard-codes `sys.path.insert(0, "/home/user/ttrpg")`.
- **Bears on:** CORE, PROCESS.
- **Content that matters:**
  - Classifies a refusal by event-kind SUFFIX (`refused`, `unavailable`, `unauthorized`, `unheard`, `ineligible`, `untold`, `none`, `blocked`, `undecided`) on the FIRST cause only (:12-19) — the suffix rule the thrust-layer register's P1 replaced with the driver's `emits_on_refusal` rule (`01` §1; the narration proposal's rule "over-counts degree bands").
  - Imports `build_realm, SeasonDriver, make_chooser, resolvable_verbs, H, draw_factory` from `engine.season.harness.populated` (:4) — a re-export surface that may have moved; [UNVERIFIED by grep].
  - Reports `capability nonempty` and `pursuits empty` counts (:27), `live oblige`, cap-200 ledgers (:26) — the source of the "capability empty for 429 of 430" style figures.
- **Conflicts / stale:** suffix refusal definition; `d.resolved` omits graded/contested admission refusals (thrust-layer G-02), so `acts=` undercounts.
- **Open items:** none.

### proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-00-index.md
- **What it is:** [READ IN FULL, lines 1-106 of 108] Index for ten subsystem-completion proposal files (T01-T10), with cross-file rulings R1-R12, order of landing, the eight asks, hash movers and Layer-1 touches.
- **Status:** "PROPOSED ... every item, ruling and ask here is held back ... **Since adopted as v10 positions (ED-IN-0299); AQ-X1, Ask B and Ask C are answered in `workplans/valoria_master_workplan_v10_part6.md` M1, M3 and M4 (ED-IN-0301).**" (:2). Reading: live as the home of v10 positions; deleted with a FORK row when its last position lands (:4).
- **Bears on:** CORE, DICE, CHAR, PC, MB, SC, FI, WR, SE, FA, PROCESS.
- **Content that matters:**
  - Method: ten Opus authors, four read-only critics (BLOCKS 7/4/4/4), one fix pass, "not audited a second time" (:15-24). Several measurements come from probe scripts "not in the repository" (:20).
  - 83 live items of 89 headings across ten files; per-file item counts and asks table (:28-44, :71-82).
  - Rulings between files (:55-70): R1 one odds function — player's Act interface shows TRUE odds (AX-7), NPC choosing uses BELIEVED inputs only (AX-2), no chooser score term; R2 one owner of the H-213 obstacle ceiling (CP-T01-06; first-drafted `2·pool` cap produces 302 cells where more dice do worse); R3 `faculty(p, verb)` is the one function for person capacity; R6 CP-T03-00 (both parties of a fight take their band) "roughly doubles combat deaths in a closed cast"; R7 ED-IN-0279 resolved for loser only; R8 Layer-1 touches split into Asks.
  - Eight asks survived: AQ-X1 (does expected success enter NPC score), AQ-T02-1 (which ties carry a seated player's line), Ask A (what is a raised troop), Ask B (what a fought field writes), Ask C (field fought a round later; Layer 1 amendment), JA-1 (may a holder burn what he holds), A1 (what a person becomes on crossing), A1 (who may declare war) (:99-110).
  - Schema movers: `body_ceiling`, `Site.locked`, resting-band field on `Person`, place index, `w._estates`, `travel_leg` as `(dest, points, path)` (:122-126).
- **Conflicts / stale:** `tools/validate_ed_citations.py` reports `OPEN_AS_BASIS` for ED-IN-0202 and ED-WR-0011 (:27-29). §6 names CLAUDE.md §5's `engine/autoload/dice_engine.py` as nonexistent — "since fixed by #507" (:104-105).
- **Open items:** two unreconciled interface demands (T10 accepted T04's siege leg that T04 dropped; T03 parked `rescue`) (:98-101); 06's "asked 0" vs JA-1.

### proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-01-resolution-and-dice.md
- **What it is:** [READ PARTLY: lines 1-5, heading index, §6-§7 (lines 260-296) of 296] T01 completion proposal: dice and resolution. Items CP-T01-01..06.
- **Status:** "PROPOSED ... held back for Jordan's adoption" (:2); home of v10 positions (:3). Reading: live as positions' spec; AQ-X1 later answered.
- **Bears on:** DICE, SC, CHAR, CORE.
- **Content that matters:**
  - Items: CP-T01-01 one faculty owner for the social roll's pool; -02 practice arm (three numbers "nobody's", ships at cap 0, swept); -03 exact odds, one function, two input modes (mode (b) answers `None` for most person subjects since no claim carries capability); -04 fraction of a margin worth its fraction; -05 `effort`; -06 ceiling solved per pool so every admitted roll keeps a chance and more dice never do worse (:69-176).
  - CP-T01-06 changes an `assumption`-graded swept fixture (`hole_register.yaml:4592`, H-213); at pool 2 a hostile term costs up to 16 points of Partial+ (26% → 10%) (§7).
  - AQ-X1 laid out: (a) no, NPCs act from values; (b) yes, as a weighting of existing terms (:262-268). Recommendation: none. Later answered in v10 M1.
  - "Residual S defects": three methods for a fraction on whole dice; combat's 5% floor vs social 10% chance floor = two methods for one guarantee (§7).
  - Notes `CLAUDE.md` §5's nonexistent `engine/autoload/dice_engine.py` path (fixed in #507).
- **Conflicts / stale:** D-1/"live discrete path read .581 against .430 at 2D" in B10-18c is a related DICE discrepancy.
- **Open items:** the `effort` magnitude is "[OPEN — Jordan tuning]".

### proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-02-season-persons-choosing.md
- **What it is:** [READ PARTLY: lines 1-5, heading index, §6-§7 (lines 411-461) of 461] T02: season, persons, chooser. Items CP-T02-01..08.
- **Status:** "PROPOSED ... held back" (:2); home of v10 positions. Reading: live positions' spec.
- **Bears on:** CORE, CHAR, FA, WR.
- **Content that matters:**
  - Items: CP-T02-01 a death names the seats it empties (H-230 limit 1); -02 a built seat keeps its authored id (H-230 limit 2); -03 an ambition can be met or breached (`aim_state`, which the thrust design's M20 text builds on); -04 the superior hears an office's aim met/breached; -05 causes a person has heard of are ambitions on offer; -06 the seated person's line continues or ends; -07 the seated person sees every question; -08 Act interface shows true odds (:76-280).
  - AQ-T02-1: which ties carry a seated player's line past death (a) heir title only, (b) title then oath (recommended), (c) title, oath, followers (:411-424).
  - Risk: CP-T02-01 makes every vacated seat a claim in every ledger, so `confer`/`oblige` form on it and mostly refuse (H-203's scene tax) (:447-450). `aim_state` is a World read for `seat_holders` inheriting ED-IN-0292 (2).
  - Declines: no score term, no odds function, no pack_scenes effort slot, no births (ED-WR-0011).
- **Conflicts / stale:** CP-T02-05 "may be false": if REM-21's own-referent stamp already carries heard-of Propositions the item is cut (:450).
- **Open items:** AQ-T02-1.

### proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-03-personal-combat.md
- **What it is:** [READ PARTLY: lines 1-5, 17-60 (genre loop), 363-398 (§6-§7) and heading index of 398] T03: personal combat. Items CP-T03-00..11.
- **Status:** "PROPOSED ... held back" (:2). Reading: live positions' spec; many items now in B10-11.
- **Bears on:** PC, CHAR, SC, MB, CORE.
- **Content that matters:**
  - Genre-loop gap table G1-G12 (:17-48): kit/training absent in season (only `end` varies: `MC/fight.py:45`; plate 90.0%, spear 95.5%, history 5 87.8%); choosing a fight is no risk to the chooser (actor never written, 33 of 59 realm calls felled the actor, none written); NPC score reads verb identity and stance only; `challenge` writes nothing and 0 of 39 `accept`s answer a challenge; `tend` restores to 1000 in one act and 0 of 75 computed `tend`s executed.
  - CP-T03-00 "both parties of a fight take their band" is the repair; "roughly doubles combat deaths" in a closed cast (§7); Measurement: seeds 0-2, two seasons, deaths and acts per season, no number predicted.
  - CP-T03-07 `body_ceiling` (lasting mark; schema mover); CP-T03-09 `capture` (single combat-to-custody route, gate `warrant`/force basis); CP-T03-10 `rescue` PARKED; CP-T03-11 guards cut into IN-59.
  - `world_q.guard_weight` was said by docstrings to exist but "does not exist" at HEAD `2decf4a` (later landed: thrust-layer cites it at `world_q.py:1250-1277`); `may_warrant` does not read the warrant Record (`gate.py:822-826`).
  - No `engine/season` module reads `engine/engine_params/` today (grep) (:397-398).
- **Conflicts / stale:** the `world_q.guard_weight` absence was true at that HEAD, false at the thrust-layer's HEAD. PC-10a/PC-10b "not built" at that HEAD; PC-10a later landed (inert).
- **Open items:** JQ-2 gates CP-T03-03/-04; AQ-X1; ED-IN-0296; T04 Ask B (carried, no new ask).

### proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-04-mass-battle.md
- **What it is:** [READ PARTLY: lines 1-5, heading index, §6 asks (lines 466-545) of 566] T04: mass battle. Items CP-T04-01..10.
- **Status:** "PROPOSED ... held back" (:2). Reading: live positions' spec; B10-12 closed most.
- **Bears on:** MB, CHAR, FA, SE.
- **Content that matters:**
  - Items: CP-T04-01 a side is its persons (one subunit per commanding person, casualties by that subunit; a weight-1 subunit at or above 80 troops); -02 `marshal`; -03 retreat in good order; -04 field fought a round after declared (Ask C); -05 graded walls; -06 `besiege`; -07 `surrender`; -08 `field_estimate`; -09 CUT; -10 raise and keep a force (Ask A) (:90-336).
  - Ask A: (A) troop stock in `Rung.stores` (amends Layer 1 `04:793`,`:802`), (P/P') a company `Person` (breaks ED-WR-0011), (B) typed troop row, (A+M-1) field force that travels; recommendation A now, M-1 later. Under A "armies are counts that eat where they stand and fight for whoever holds their walls" (:468-482). Ask B: ED-IN-0279 resolved for the loser only (casualties, morale decrease, grudge token); options (a) as built, (b) winners take engine casualties, (c) survivors move a grade, (d) captives via T03's `capture`; recommendation (b)+(d) (:485-504). Ask C: amend `04:177`/`:541-545` so ENCOUNTER fights a declared field a round later; recommendation (b).
  - "Not raised": a march needs no war (no item reads `at_war`, FA owns); death in battle superseded by J-C-19; weight→troop value is JQ-4; `sack` declined; no separate `muster` row.
  - Gap ledger (:58-90): 30 rows addressed; 12 closed by items, 1 by remediation (REM-32 + JQ-4: "a field is too small to be fought"), 11 declined with five-step answers (no supply/attrition, no rally of routed units because every commander's Command is the constant 4 (`MB.py:182-186`) until JQ-2, no general falling in battle, one resolver because nobody plays, friction swings a battle, "the defender takes every tie": 44% between equal armies), 9 to Asks A/B. Rows split across outcomes are counted under each.
  - Only 4 occurrences of the word "cell" in the file: it treats the army as subunits-per-commander and a troop stock, not as the cell-grid formation design (the per-cell approach and weapon-carry trade-off in AUDIT_BRIEF are not engaged).
- **Conflicts / stale:** mass-battle design intent in AUDIT_BRIEF (cell-based approach; weapon-carry trade-off) is not discussed here: T04 centres on subunit-per-commander and troop stock, not cells. Whether Ask B/C answers (M3, M4) went (a) or (b): `CP-T04-04` and `-10` are HELD per B10-12, so Ask C (b) and Ask A are unanswered/held.
- **Open items:** Ask A (M3), Ask C (M4 (b)); both still HELD in B10-Z/B10-12.

### proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-05-social-contest.md
- **What it is:** [READ PARTLY: lines 1-5, heading index, §6-§7 (lines 408-461) of 461] T05: social contest and proceedings. Items CP-T05-01..05.
- **Status:** "PROPOSED ... held back" (:2). Reading: live positions' spec; B10-13/B10-18c build over it.
- **Bears on:** SC, FA, CHAR, DICE.
- **Content that matters:**
  - Items: -01 the verdict hears the bench; -02 the bench remembers the hearing and the accused may answer (new `subject_may_be_self` column); -03 a failed telling is realised; -04 formation for the proceedings verbs (two classes, one docket question); -05 questioning is part of the hearing (CP-T05-05 later CUT) (:85-257).
  - New asks: none. Candidates answered by ladder (§6): a verdict reads the party's whole record (no charge carrier exists, H-227); defence half under the shipped ceiling is T01 CP-T01-06's.
  - Risk: at HEAD the room bites only at net >= 1.0 (the net is an integer); under `obstacle_ceiling` 2 = `obstacle_default` a favourable bench cannot raise a verdict above Ob 2 — only the case against bites (§7). `opposed` reads every deed of the party's, not the charged one (H-216): "a man of ill repute is bound more easily for anything". Testimony of violence does not reach the verdict as evidence (a told killing names nobody).
  - CP-T05-03 lowers `news.told` volume, thinning the information loop (OV §5.2).
- **Conflicts / stale:** detective/noir design intent of AUDIT_BRIEF (fieldwork-SC bearing) is not engaged here; the file models proceedings (bench/verdict), not social interrogation as play.
- **Open items:** `reception` magnitudes unmeasured; J-C-6 (may a person lie) carried; `seen.who` on a told copy [ASSUMPTION].

### proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-06-fieldwork-and-information.md
- **What it is:** [READ PARTLY: lines 1-5, heading index, §6-§7 (lines 226-262) of 262] T06: fieldwork and information. Items CP-T06-01..09.
- **Status:** "PROPOSED ... held back" (:2). Reading: live positions' spec; B10-14 builds them.
- **Bears on:** FI, WR, SC, CORE.
- **Content that matters:**
  - Items: -01 a deed that writes a place or an alias leaves a trail; -02 `surveil` finds covert deeds at the place it watches; -03 a Partial closes the deed, not the hand; -04 a refused/failed inquiry teaches its actor his reads (reverses remediation DEC-12; H-111, RS-21); -05 the person questioned answers by his own act; -06 `inquiry` key (CUT later); -07 a cover can borrow another's name; -08 paper can be burned (PARKED on JA-1); -09 the room files a covered deed under the hand (:72-155).
  - JA-1 only ask: may a holder burn what he holds? `destroy_record` is WITHHELD (`data/fixtures.py:924-933`); H-156 registered "both defensible"; no recommendation (:228-238).
  - At shipped odds Failure F 0.74: "three of four inquiries on a real trail would deposit a false hand" so Failure-misleads declined until odds move (`T01 CP-T01-01, -06`); at pool 2 vs Ob 2 three of four inquiries fail (§7).
  - Risks: realm may reach no trail; the anchor claim leaks (an uncovered deed's hand reaches every admitted witness), so inquiry matters only where nobody was admitted or a cover stood.
  - Does not do: verifier, case object, plot carrier, Exposure meter, wrong-guess gauge, `disguise`, `infiltrate`, `bribe`, `eavesdrop`, `decipher`, `shadow`.
- **Conflicts / stale:** AUDIT_BRIEF's detective/noir intent (case-building, clues) vs this file's explicit "no case object": a tension an FI audit must weigh. SM-3 "investigation is not a contest seam".
- **Open items:** JA-1; the frame's reach unmeasured; ledger pressure from CP-T06-04.

### proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-07-threadwork.md
- **What it is:** [READ PARTLY: lines 1-5, heading index, §6-§7 (lines 447-493) of 493] T07: threadwork. Items CP-T07-01..11.
- **Status:** "PROPOSED ... held back" (:2). Reading: live positions' spec; B10-15 builds.
- **Bears on:** WR, PC, CHAR.
- **Content that matters:**
  - Items: -01 the practitioner on the Person (later CUT, folded into -02); -02 Leap stage and one working host; -03 `weave`/`lock` on Sites; -04 `mend` (reshaped so it never closes another's Tenure: a `locked` Site field); -05 equilibrium decided by place; -06 recovery as a projection; -07 permanent set; -08 crossing as witnessed breach; -09 every thread row celled; -10 what `thread_read` finds; -11 `ward` (:86-346).
  - Ask A1: what does a person become when he crosses the latch? (a) stays a person, rewritten, (b) leaves the cast and becomes a standing strain on his territory; nothing waits, the slot ships `none` (:447-458).
  - Risks: only four persons seed TS >= 30 in the registry; NPCs never stop (chooser has no state term reading displacement, `choose.py:130-151`); weave strong if IN-35's weight stays 0; lock as griefing (Locked Zone is canon).
  - Does not do: `dissolve` (PARKED), collective workings, `pull`, involuntary Leap knots, co-movement cards, threadcut beings.
- **Conflicts / stale:** thrust-layer P8 shows 0 threadwork modules loaded in a season: these are the items that would load them.
- **Open items:** A1; WR-01.

### proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-08-settlements-governance-economy.md
- **What it is:** [READ PARTLY: lines 1-5 and heading index of 151 lines] T08 part 1: settlements, governance, economy (CP-T08-01..05).
- **Status:** "PROPOSED ... held back" (:2). Reading: live positions' spec; B10-16 builds.
- **Bears on:** SE, FA, WR, CORE.
- **Content that matters:**
  - Items: -01 hands make the yield (`labour_mode`); -02 places are endowed by their ground; -03 stores spoil; -04 `craft`; -05 price read off the place, trade between places (:73-136).
  - Index says 88 rows addressed, 9/10 items live, knobs held at JQ-6 (hunger).
  - [SKIPPED: bodies of CP-T08-01..05, lines 6-151 — not opened]
- **Conflicts / stale:** none verified.
- **Open items:** none read.

### proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-08-settlements-governance-economy_part2.md
- **What it is:** [READ PARTLY: lines 1-5 and heading index of 188 lines] T08 part 2 (CP-T08-06..10).
- **Status:** "PROPOSED ... held back" (:2).
- **Bears on:** SE, FA, CORE.
- **Content that matters:**
  - Items: -06 the settlement's mood `unrest(w, S)`; -07 a standing levy via the `tax` edict; -08 the upkeep payment gets a question; -09 withdrawn (succession) in favour of CP-T02-01/02; -10 holding costs past a limit (:9-65).
  - [SKIPPED: bodies — not opened]
- **Conflicts / stale:** none verified.
- **Open items:** none read.

### proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-09-factions-war-diplomacy.md
- **What it is:** [READ PARTLY: lines 1-5, heading index and §6 (lines 615-660) of 689] T09: factions, war, diplomacy. Items CP-T09-01..09.
- **Status:** "PROPOSED ... held back" (:2). Reading: live positions' spec; B10-17 builds.
- **Bears on:** FA, SC, CORE, CHAR.
- **Content that matters:**
  - Items: -01 allegiance follows opinion (join/leave/switch); -02 `declare` (a war has a producer, occasion, target set); -03 alliance and peace as acts on the war Proposition; -04 land with no holder taken by plurality occupation; -05 fief for the sworn; -06 Crown's ducal seat refilled (data only; `appointed` basis [ASSUMPTION]); -07 `recruit` and seat's obligees in its army; -08 `dispatch` sends; -09 `conspire` (:113-431).
  - A1 ask: who may declare war — any `dispatch` seat (wars frequent, local) vs creed subject's faction head only (wars rare; King dies in season 0 in every seed so the faction cannot declare). `faction_q.head` is "always None" (`FQ:116-147`) so verbs-15's option two is unbuildable as written; default option one (:615-640).
  - Under `remit_default`, `dispatch` is 25 of 32 seats (T09 §1).
  - Not raised: whether a treaty binds the signer or the seat (the signer); territories seizable (GD-1 makes control of all 15 territories the victory, `RY:2584-2585`).
- **Conflicts / stale:** "King dies in season 0 in every seed" interacts with the thrust-layer deaths (16 of 20 seat-holders) and the succession (IN-61) stoppage.
- **Open items:** A1; FA-01 trade-demand clause held on ED-IN-0298.

### proposals/2026-10-23-subsystem-completion/2026-10-23-subsystem-completion-10-world-travel-survival-npc-life.md
- **What it is:** [READ PARTLY: lines 1-5 and heading index (items, §5-§7) of 564 lines] T10: world, travel, survival, NPC life. Items CP-T10-01..09.
- **Status:** "PROPOSED ... held back" (:2). Reading: live positions' spec; B10-18 builds.
- **Bears on:** WR, SE, CHAR, PC.
- **Content that matters:**
  - Items: -01 journey priced by route (`travel_leg` as `(dest, points, path)`); -02 Calamity costs the traveller; -03 the year turns (`year_length`); -04 recovery costs time and care; -05 bodies clock wounds before they kill; -06 kin; -07 an estate passes by its heir's claim (`w._estates`); -08 `marry`; -09 deeds done to me and mine (:111-353).
  - Index: 89 rows addressed; no asks; ED-WR-0011 cited as closed cast "for now" (provisional) and the validator does not accept `status=ruled` as resolved.
  - [SKIPPED: bodies and §6-§7 (lines 524-564) — not opened]
- **Conflicts / stale:** CP-T10-04's rising body arm and `tend_share` [ASSUMPTION 0.5] interact with CP-T03-07 `body_ceiling` (ruling R5).
- **Open items:** none read.

### proposals/2026-10-24-character-layers-capability-ambition-values-personality.md
- **What it is:** [READ IN FULL] v1 design (2026-10-24, lane IN) splitting a person into four layers (capability, ambition, values, personality) and deciding what the seven pursuit axes become; one producer + one critic + orchestrator.
- **Status:** "PROPOSED (2026-10-24). HELD BACK ... superseded in part by character-layers-v2.md ... v1 still carries the cuts Jordan withdrew on 2026-10-25" (:3). Reading: partly superseded; its §5 cuts (boldness, patience, vindictiveness) are overruled by Jordan's "don't cut anything because there isn't a code reader yet" (v2 :10) and ED-IN-0304 ruling noted at :129.
- **Bears on:** CHAR, CORE, PC, SC.
- **Content that matters:**
  - Four membership tests in order (:49-54): capability = more always helps; ambition = some state satisfies it; value = direction nothing finishes; personality = varies independently of values, leaves odds untouched, no pole always wins.
  - Split of the seven axes (:25-27, :95-103): four are value readouts at spread 0 (`selfish_selfless`, `partisan_equitable`, `hierarchical_equal`, `precedent_substantive`); three get a stored per-person offset (`rigid_flexible`, `grandiose_humble`, `deontological_instrumental`) at ±0.15, derived as one corpus sd (0.12/0.11/0.15 over 46 authored rows, measured at :107-111) rounded up to 0.05.
  - Carrier proposed `Person.personality: dict`, absent key = offset 0 = control; build-only like `thread_sensitivity` (:84-85). Likeness readers read the prior over all seven columns so spread 0 keeps `World.content_hash()` exact (:116, :206).
  - Worked example (:152-166): A/B/C with identical pursuits rank `comply`/`challenge`/`forge` differently only with offsets; the armed deontology gate "hardly discriminates" at these magnitudes (:168).
  - Cut rows: `forgiving_vindictive` "dead reader" (grudge row keyed by faction name, `effects_combat.py:311-313`; candidates' subjects are persons); `choice_temperature` fails test 4 (:126-137).
  - Every authored NPC holds all 15 pursuits (`data/cast.py:209-211`), minted persons (`loop/census.py:106`) hold none; cohorts hold none (SE-06 / ED-IN-0296) (:79, :194).
- **Conflicts / stale:** overrides the ED-IN-0261 R7 dissolution clause ("two people with identical pursuits ARE identically disposed") for three axes (:37) — held for Jordan (v2 :25). Line numbers are of HEAD `d59acc9`.
- **Open items:** [GAP] candour/discretion/credulity/dogmatism untested (:135); `Combatant.disp` unmapped (two ladders for one trait family, :136, :216); gate convention is H-146's (:195); whether example verbs share one real `opening_set` (:220-221).

### proposals/2026-10-24-character-layers-v2.md
- **What it is:** [READ IN FULL] Reconstruction (2026-10-30) of a lost v2 design (session 2026-10-24/25) from a digest of that session's closing summary: ten axes, fifteen personality traits, attribute readers.
- **Status:** "PROPOSED — HELD BACK IN FULL; reconstructed from a digest, not from the original file; where this file and a re-derivation from the tree disagree the tree wins" (:3). Original `layers_v2.md`: LOST (:5). The session's closing line asked "want the v2 design landed as a replacement" and Jordan's answer is not on record (:8). Reading: design exercise record; figures unverified.
- **Bears on:** CHAR, PC, SC, CORE.
- **Content that matters:**
  - Ten axes: the 4 value readouts (spread 0) + 3 prior-plus-offset (±0.15) + 3 new personality-only axes `cautious_bold` (derived from verb-table exposure, 12 of 56 verbs), `hasty_patient` (declared per verb, 13 delay cases), `conciliatory_coercive` (declared per verb) (:50-59).
  - Fifteen traits = six manner offsets + nine per-person copies of global gain settings (`forgiving_vindictive`, `trusting_sceptical`, `open_dogmatic`, `guarded_open`, `steadfast_malleable`, `callous_scrupulous`, `serene_torn`, `frugal_lavish`, `steady_capricious`) (:65-69). Sorting rule: effect varies by VERB → axis; by claim/stance/deposit/scar → per-person gain (:103).
  - Attribute readers: Body → budget base and combat strength; Hand → forgery and combat agility; Wit → Recall (`claim_decay_per_season`, `ledger_cap`, `view_k`); Nerve → wound-band penalty and combat spirit; Sense → Watchfulness and `record_gain`; Presence → none (:86-95).
  - Measured example (unreproduced): identical pursuits, `cautious_bold` -1/+1 → chance of landing a duel in top five 0.130 vs 0.324 vs control 0.208 (:121-122).
  - Session findings (:127-131): capability empty for 429 of 430 persons; only `tell`/`speak` read it; candidate gaps 0.01-0.06 at tau 0.1, top candidate reaches top five 41% of the time, stance term -8.0 on every candidate; `selfish_selfless` has no nonzero cell on any verb; growth loop has no start and no exit (`train` raises only if already held). Conclusion: wiring what exists comes before new layers.
- **Conflicts / stale:** v1's "no per-verb cell, no new reader" is contradicted by v2's per-verb columns (:39). Falsifiers are carried from v1, restated "at v2's numbers" nowhere (:148-155).
- **Open items:** four owner calls (`selfish_selfless` spread; `choice_temperature` swallows personality, tied to CR-17 and ED-IN-0304; `payoff`/`force` columns are unargued judgement cells; refusal gate convention) (:137-142); progression open gaps (Thread Sensitivity among the six; floors for unrostered persons; mapping `stats:`; decay period N; Nerve tension) (:97).

### proposals/2026-10-24-character-progression-adjudication.md
- **What it is:** [READ PARTLY: lines 1-260, 275-394, 547-754 opened; §4.7-§8 (lines 395-546) not opened] One first-principles adjudication of character progression by a read-only agent (HEAD `b7a1e1b`), with a §10 addendum by the orchestrating session on Nerve/Composure.
- **Status:** "PROPOSED (2026-10-24); partly superseded since by the ratified v10 plan (M2 / ED-IN-0301: nine stored attributes on 1-7 with practice live; CR-18 takes the practice arm of CP-T01-02; CR-20 keeps `max(held key, base)` floor)" (:3). Reading: partly superseded; the six-attribute roster and the cut of accrual are overtaken, the code premises in §2 remain a usable map.
- **Bears on:** CHAR, DICE, PC, SC, MB, CORE.
- **Content that matters:**
  - Architecture (:246-253): six immutable stored attributes (Body, Hand, Wit, Nerve, Presence, Sense) setting a ceiling and floor on capability, never a dice term; one capability ladder; decisive-event writer at RESOLVE (+1 at most once per key per season) and decay; no lifepath bundle; tradition as an input/label; attributes never move; no mechanical specialness for the player's seat.
  - Code facts (§2): `Person` has no attribute/tradition field (`carriers.py:655-729`); `pool_default = obstacle_default = 2` (`fixtures.py:414,416`, graded assumption H-126/H-127); `_eff_train` only raises a held key (`effects_combat.py:421-446`); `verb_capability` maps only `tell`/`speak` to `copying` (`rosters.yaml:1232-1233`); one of 430 persons holds any capability (NPC-088); 8 of 56 verbs contest (`argue`, `arrest`, `determine`, `fight`, `accept`, `march`, `speak`, `tell`).
  - Combat's pool: `resolution_pool = max(POOL_FLOOR=5, int(round(history)) + BASE_POOL=6)`, obstacle `defender.history / 2.0`; the season seam derives exactly one `Combatant` field (`end`) so every season fighter rolls max(5, 3+6) = 9 and familiarity is always 1.0 (:160-186). Two ladders for one quantity (C-4).
  - Corrections C-1..C-10 (:547-625): familiarity does not reach the obstacle; `march` reads no capability; the handoff is `dispatching_chooser` not `choose.py:433`; "no switch while a contest is open" is not held by the seam; name collisions Body/`Person.body`/`agg.body`, Presence alias of Charisma.
  - Addendum §10: chooser score = pursuit term + stance + urgency, no risk term, no timing term (`choose.py:130-151`); ED-IN-0304 (2026-10-29) rules risk appetite and short/medium/long horizon wanted; Nerve is decision-side (Jaccard overlap nerve/composure 0.09); verdict "not both as attributes" but the adjudication keeps Nerve (:750-753).
- **Conflicts / stale:** the six-attribute roster vs v10 M2 nine attributes; claims about `rosters.yaml` line numbers drift. Outside-literature grades: Juul, Hunicke & Chapman read; Ryan/Rigby/Przybylski abstract only; Lundblade abstract only; game precedents "community-grade or from memory" (:229-236).
- **Open items:** [GAP] J-T1/J-T2/J-T4 open decisions not read by the agent (:24); authoring source for persons outside the registry (C-9); the Nerve/chooser tension (:751-753).

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-00-sequence.md
- **What it is:** [READ PARTLY: lines 1-110 of ~210 opened (§0-§3 incl. the cut table); §4 question holds, §5 boundaries, §6 changes (rows 1-56) and §7 open risks NOT opened] Dependency-sequence document (T09, lane IN) for the master workplan v10: graph size, edge sources, critical path, the cut into batches B10-01..B10-20, the parallel plan.
- **Status:** "instructions under the adopted plan. The state index stays `-03` §1" (:2); grade `paper` (:4). Reading: live process instruction for the v10 plan (adopted, ED-IN-0299/ED-IN-0301); the plan's authored head is `workplans/valoria_master_workplan_v10*.md`, not this file.
- **Bears on:** PROCESS, CORE (and every subsystem via batch membership).
- **Content that matters:**
  - Graph: 211 nodes, 314 edges after the second decision round; the graph check script and transcription "are not on disk" (:8), so counts cannot be re-derived from this file; the script is cited as `ctl/graph_check.py` (:33) — not in this lane's files.
  - Spine: B10-01 → B10-02 → {B10-03 ∥ B10-04} → B10-03b → B10-05 → B10-06 → B10-07 → B10-07b → B10-08 → B10-09 → B10-10 → B10-10b → B10-11 (PC) → B10-12 (MB) → B10-13 (SC) → B10-14 (FI) → B10-15 (WR threadwork) → B10-16 (SE) → B10-17 (FA) → B10-18 (WR/NPC life) → B10-20 (port gate) (:55-56); B10-19 (design-first clusters) and B10-Z (held/leave) are off the spine (:96-97).
  - The cut table (:70-97) gives each batch's code/no-code class, entry gates and holds; B10-01 and B10-09, B10-10 are recorded CLOSED with closing commits; B10-12 through B10-18 are the build cards this lane holds.
  - Rules P13 (serial inside verb cluster), P14 (hash movers declared with old/new pins), P15 (re-pin once in batch's pin commit), P3 (rows leave `-03` at close) are cited by id and defined elsewhere (`-03`) [UNVERIFIED here].
  - CL-THRUST's row sits off the spine; its released pieces (B0.1, B2.x, B3.1, B3.2) land in B10-02/05/09; B5.1 is cut (M21) (:57-59).
- **Conflicts / stale:** counts inside (211 nodes, 184-node/218-edge earlier check) are explicitly layered across rounds. The file mixes dates: a closed batch (B10-12) later got narrowed (see B10-12 file). Later plan versions are `workplans/valoria_master_workplan_v11_part3.md` (cited by B10-12) so the "v10" label is no longer the newest [UNVERIFIED which is current: `CURRENT.md` names it].
- **Open items:** the §4 question holds M1, M3, M4 etc. (:109-129) were not opened.

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-11.md
- **What it is:** [READ PARTLY: lines 1-14 and ### headings of 116 lines opened; position bodies not opened] Build instructions for batch B10-11, PERSONAL COMBAT (T03, lane PC).
- **Status:** "instructions under the adopted plan" (:2). Reading: live process instruction, may be partly built; the batch card is `workplans/valoria_master_workplan_v10_part3.md`.
- **Bears on:** PC, CORE, CHAR.
- **Content that matters:**
  - Positions: CP-T03-01 (cohorts never a party to a personal fight, weight bound; two commits: the `individual` stem first, then the cohort-fought mover); CP-T03-05 (combat's odds sampled live for the player's Act interface, REPAIR per AM-C-02); CP-T03-06 (the survivor's grudge: MEASURE, then DESIGN-FIRST, then BUILD or CUT); CP-T03-10 parked, CP-T03-11 cut; plus CP-T03-02/09/03/04/07/08 and PC-10 listed in order (:12-14, :40-81).
  - Hash class mixed; `body_ceiling` is a schema mover changing every person's `repr` (CP-T03-07/08) (:11).
  - Entry gate: B10-10 and B10-10b (personal-combat module's own debt, six closes, edits `modules/combat/`) merged. `modules/combat/` is reached through the wrapper and not edited here (:10).
  - PC-10 route (1) decided (`-04` §3); PC-10b's `accept`-needs-a-held-challenge refusal is the thrust-layer register's G-15 owner.
- **Conflicts / stale:** the combat module calls in `Read before building` cite `-08` AM-C-02..08 amendments (not in this lane).
- **Open items:** CL-SLICE's build is a conditional landing first, if its design is approved and M31-M33 answered (:14).

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-12.md
- **What it is:** [READ IN FULL] Narrowed build record for batch B10-12, MASS BATTLE (T04, lane MB).
- **Status:** "CLOSED except CR-12, CP-T04-04 and CP-T04-10 (HELD in B10-Z); entries narrowed at the close" (:2). The batch's record moved to `workplans/valoria_master_workplan_v11_part3.md` (:3). Reading: partly historical, held entries live.
- **Bears on:** MB, CORE.
- **Content that matters:**
  - Landed: CP-T04-02 `marshal` (`a86be397`, standing order of battle; built on the user's ruling with `role_allowed` bypassed, H-361) and CP-T04-07 `surrender` (`1cdfcaf6`); both ship WITHHELD (`withheld_verbs`) with the flip a declared mover not yet made (:10-14). The `cession` basis is not in `architecture/meta/04_CODE_ARCHITECTURE.md` C.2's write-gate enumeration, held back for Jordan (:14).
  - CR-12 (melee attrition back to the locked linear law, ED-MB-0045): measured; design in `proposals/2026-11-08-cr12-melee-attrition-design.md`; "the only fix that moves the exponent removes troop numbers from the pool, against Jordan's 2026-07-08 directive"; builds nothing until he rules; acceptance when built: melee p at or below 1.4, volley p at or above 1.6, CI flip of `lanchester-signature` proposed not made (:16-19).
  - CP-T04-04 (field fought a round after declared) exists only under M4 Ask C (b): needs a Layer 1 amendment to `04:177/:541-545` (:21-32). CP-T04-10 (raise and keep a force) held on M3 Ask A, which needs amending Layer 1 `04:793/:802` to admit a counted troop stock in `Rung.stores`; only item that amends Layer 1 (:34-45).
  - CP-T04-09 CUT; reopen needs H-195's M0g trigger (:47-48).
  - File stays only because `verb_table.yaml` (`marshal`, `surrender` rows) and `hole_register.yaml` (H-361) cite it as `source:` (:6).
- **Conflicts / stale:** the shipped `marshal` bypassed `role_allowed`, a process deviation recorded in H-361 [UNVERIFIED: not opened]. Whether the CR-12 conflict with the 2026-07-08 directive has been ruled since is unknown.
- **Open items:** CR-12 ruling; M4 Ask C (b); M3 Ask A; flips of `marshal`/`surrender` out of WITHHELD.

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-13.md
- **What it is:** [READ PARTLY: lines 1-14 and ### headings of 220 lines] Build instructions for batch B10-13, SOCIAL CONTEST AND PROCEEDINGS (T05, lane SC).
- **Status:** "instructions under the adopted plan" (:2). Reading: live instruction.
- **Bears on:** SC, CHAR, FA.
- **Content that matters:**
  - Positions: SC-02 (F8 re-source of `reception`, DESIGN-FIRST; the build waits on approval; A1-08 answered option B, ED-SC-0040); CP-T05-01 (the verdict hears the bench, HELD on SC-02); CP-T05-02 (accused may answer now; (i) `hearing` held); CP-T05-03 (failed telling realised); SC-04 (`negotiation` arrangement row); CR-55 (a matter lapses visibly: dead party, venue with no bench, overdue stage); CR-56 (matter stamped where it waits); CR-34 (declared disposal read: a vote counts live commits; H-161); CR-27 (`lie`: spoken falsehood on a held cell claim; M9, `lie_offered` ships True); CR-31 (caste estimate: regard term over decider's creed and his belief about other's descent; `heritage_gain`) (:47-187).
  - Shared files serialised: `arrangements.yaml`, `queries/person_q.py` (`lie_said_of`, `heritage_regard`), `decision/options.py`, `data/fixtures.py` (`lie_offered`, `heritage_gain`), `hole_register.yaml` (:20).
  - Hash: CR-34 EQUAL in every seeded realm (realm reach 0); CR-31 EQUAL at `heritage_gain` 0 and a declared mover at shipped value (:10).
- **Conflicts / stale:** B10-18c (later) builds the "social-contest choice layer" over the same files.
- **Open items:** SC-02's design approval gates three builds (:15).

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-14.md
- **What it is:** [READ PARTLY: lines 1-12 and ### headings of 200 lines] Build instructions for batch B10-14, FIELDWORK AND INFORMATION (T06, lane FI).
- **Status:** "instructions under the adopted plan" (:2). Reading: live instruction.
- **Bears on:** FI, WR, CORE.
- **Content that matters:**
  - Positions: CP-T06-09 (room files a covered deed under the hand); CR-29 (REACH: event-kind reach channel then `chronicle`'s paired deletion); CP-T06-01 (a deed that writes a place or alias leaves a trail); CP-T06-03 (a Partial closes the deed, not the hand); CP-T06-04 (refused/failed inquiry teaches its actor his reads); CP-T06-02 (`surveil` finds covert deeds at the place); CP-T06-07 (a cover can borrow another man's name); CP-T06-05 (the person questioned answers by his own act, verb retype); CP-T06-08 PARKED on JA-1; CP-T06-06 CUT (:41-162).
  - CP-T06-01 is unobservable in the realm without B10-05's REM-21/22/2C; `test_fi03_trail.py` is re-recorded in the pin commit (:10-11).
  - M11 answered (a) by Jordan's "Confirm all" of 2026-10-26 (ED-IN-0300, ED-IN-0301) (:5).
- **Conflicts / stale:** none noted.
- **Open items:** CP-T06-08 parked; "a mover only wherever a trail/cover/interview is found; the realm may reach none, which the control reports as a finding" (:10).

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-15.md
- **What it is:** [READ PARTLY: lines 1-12 and ### headings of 269 lines] Build instructions for batch B10-15, THREADWORK (T07, lanes WR, PC).
- **Status:** "instructions under the adopted plan" (:2). Reading: live instruction.
- **Bears on:** WR, PC, CHAR, CORE.
- **Content that matters:**
  - Positions: CR-13 (the Leap not charged for failing); REM-45 (corrected history term, M18(b)); CP-T07-02 (Leap stage, one working host, actor adapter, `Person.coherence`: schema mover on every `repr`); CP-T07-03 (`weave`/`lock` on Sites: `Site.locked`); CP-T07-05; CP-T07-09 (every thread row a witnessable celled deed); CP-T07-04 (`mend`); CP-T07-06 (recovery as projection); CP-T07-07 (permanent set narrows the season); CP-T07-10 (what `thread_read` finds); CP-T07-08 (crossing as witnessed breach); CP-T07-11 (`ward`); IN-32 (`tie / knot` effect + reader); WR-01 (R-14 practitioner-resilience season reach, BLK on its own condition) (:43-226).
  - IN-06 "plugged nothing" (design re-review); IN-35 landed at B-S; CP-T07-01 CUT (adapter is CP-T07-02's first function) (:5).
  - Spirit is Will's alias (M2 narrowed); CP-T07-02 reads Will via CR-20's attribute carrier (:8-9).
- **Conflicts / stale:** relates to thrust-layer G-21 (threadwork absent from season run): this batch is the plan that would load it.
- **Open items:** none stated at head.

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-16.md
- **What it is:** [READ PARTLY: lines 1-12 and ### headings of 262 lines; assignment marked it 76% previously read] Build instructions for batch B10-16, SETTLEMENTS, GOVERNANCE AND ECONOMY (T08, lane SE).
- **Status:** "instructions under the adopted plan" (:2). Reading: live instruction.
- **Bears on:** SE, FA, CORE.
- **Content that matters:**
  - Positions: CR-40 (delete `starting_pros`, one grain for Prosperity); CP-T08-01 (hands make the yield, `labour_mode`); CP-T08-03 (stores spoil); CP-T08-02 (places endowed by ground); CP-T08-05 (price read from the REM-50 draw record; trade between places); CP-T08-06 (`unrest(w, S)`); CP-T08-07 (`tax` edict standing levy); CP-T08-08 (upkeep payment gets a question; `upkeep_lead`); IN-14 (`budget()` counts `granted_acts`, MORE ROUNDS shape); CP-T08-10 (holding costs past a limit); CP-T08-04 (`craft`); IN-52 (provisioning flip, retirement HELD on M3) (:42-214).
  - Off-arms EQUAL: `labour_mode: off`, rates 0, `uniform`, `()`; IN-14 is a declared MOVER (:10).
  - Requisition chain credit: CP-T08-06's compliance reader, CP-T08-07, CP-T08-08's refill and IN-52's flip are credited in computed play only where CR-23's exit recorded `requisition` executing, otherwise `harness/scarce.governed` only (:12).
- **Conflicts / stale:** none noted.
- **Open items:** the "Held and withdrawn members" section (:214) not opened.

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-17.md
- **What it is:** [READ PARTLY: lines 1-12 and ### headings of 310 lines] Build instructions for batch B10-17, FACTIONS, WAR AND DIPLOMACY (T09, lane FA; CR-32..37 also IN, SC).
- **Status:** "instructions under the adopted plan" (:2). Reading: live instruction.
- **Bears on:** FA, SC, CORE, SE.
- **Content that matters:**
  - Positions: IN-30 + CP-T09-04 (one owner of faction identity admitting emergence; land taken by plurality occupation, else by purview); CP-T09-01 (allegiance follows opinion, MEASURE first); CP-T09-05 (fief); CP-T09-02 (`declare`: war producer/occasion/target set; M10(b): no `at_war` gate on `march`); CP-T09-03 (alliance and peace as acts on the war Proposition); CP-T09-07 (`retain`); CR-09 (`own_purview` vs oblige clause, H-101); CP-T09-08 (`dispatch` sends); CP-T09-09 (`conspire`); CP-T09-06 (Crown's ducal seat passes with the line, data only); CR-32 (Standing ladders as posts on seats; `marks`); CR-35 (elected seat filled by faction bench; contested succession; H-217); CR-36 (nominate-then-confirm `nominated`); CR-37 (throne stripped by Holy See concurrence `joint_concurrence`; `depose` closed); IN-48 (H-108 delegation, DESIGN-FIRST); IN-36 (FORCE-FOREIGN remainder, HELD for `guards`); FA-01 (Schoenland trade-demand clause) (:41-269).
  - Every build is a declared MOVER; `guards` stays off (ED-IN-0310 keeps it off, ED-IN-0301 confirmed default) (:6-9). `foreign` ANSWERED by ED-IN-0310 (2026-11-04).
  - Two closes decided at batch open: close one T09 rows; close two CR-32/35/36/37 then IN-48 (:6 table in `-00`).
- **Conflicts / stale:** the thrust-layer G-19 (guards binds nobody) depends on IN-36's flip, which is HELD here.
- **Open items:** IN-36 on `guards`; CP-T09-01 and -09 measure-first then conditional.

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-18.md
- **What it is:** [READ PARTLY: lines 1-12 and ### headings of 277 lines] Build instructions for batch B10-18, WORLD, TRAVEL, SURVIVAL AND NPC LIFE (T10, lanes WR, IN).
- **Status:** "instructions under the adopted plan" (:2). Reading: live instruction.
- **Bears on:** WR, CHAR, SE, CORE.
- **Content that matters:**
  - Positions: CP-T10-06 (kin: releasable `kin` kind + authored edges); CP-T10-07 (estate passes by heir's claim; new hashed collection `World.estates`); CP-T10-09 (deeds done to me and mine); CP-T10-01 (journey priced by route); CP-T10-02 (Calamity costs the traveller); CP-T10-03 (`year_length` calendar, ships off) and its own flip commit 0 → 4; CL-EVENTS commit 2 (FORCE-WEATHER per territory live draw), commit 3 (Tensions receiver: `tensions.yaml`, `data/tensions.py`, switch off) and commit 4 (six Tensions cards as `[ASSUMPTION]` data); CR-08 (`(Person, weight)` one writer: CENSUS; H-49); CR-22 (hunger binds: per-head need by reading rule); CP-T10-04 (recovery costs time and care); CP-T10-05 (bodies clock wounds before they kill); CP-T10-08 (`marry`) (:37-239).
  - Entry gates include REM-52's `body_step = 10` (B10-05), the `individual` stem and `body_ceiling` (B10-11), `modules/mass_battle/terrain.py` (B10-12) (:12). Ends CR-38's approval window.
- **Conflicts / stale:** these positions would switch on the "dark" exogenous motion that the thrust-layer register (G-22, S4) says is dark: `body_step`, `illness_rate`, `age_step`.
- **Open items:** none stated at head.

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-18b.md
- **What it is:** [READ IN FULL] Build instructions for batch B10-18b, VERBS: THE R-05 CLOSE (lane IN with FA, MB, SE).
- **Status:** "instructions under the adopted plan" (:2). Reading: live instruction (batch after B10-18).
- **Bears on:** CORE, FA, MB, SE.
- **Content that matters:**
  - CR-46 (rewrites R-05's `measure:` text; does not set `status:`), CR-52 (army-preset run through `military_menu.callback`/`dispatching_chooser`/`SeasonDriver.season`), CR-50 (two data cells `raze`, `train`), CR-47 (ranking of every deliberating person), CR-48/49 (give; confer/oblige), CR-51, CR-53, CR-54 (design file only) (:7-19, :27-37).
  - Pre-flight: `len(VERB_TABLE)` is 62, `resolvable_verbs()` 60 at `eda39a6`, "the plan's earlier 56 is superseded" (:25); at `eda39a6`, pooled, 36 of 60 resolvable rows executed; 27 did not at seed 0 (:26); `aperture 3 --seeds 0 1 2` takes about a quarter-hour per seed at four seasons (:26).
  - CR-48: no mint into the addressee's hold (ED-IN-0292 (1), RULED NO); route is `give`; the operand vocabulary is closed (H-94) (:30-34).
  - Close prints the STORY READING (CR-69, ED-IN-0311) at the same seeds, "a reading, never a bar or a guard" (:42).
- **Conflicts / stale:** supersedes the 56-verb count used in thrust-layer docs (13 of 56 write nothing).
- **Open items:** any verb left at 0 is a named residue with an owner; no position invented.

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-18c.md
- **What it is:** [READ IN FULL] Build instructions for batch B10-18c, SOCIAL CONTEST: THE CHOICE LAYER (lane SC with IN); ED-IN-0308 ratifies the batch.
- **Status:** "instructions under the adopted plan" (:2). Reading: live instruction.
- **Bears on:** SC, FA, CHAR, DICE.
- **Content that matters:**
  - CR-57 (give consent), CR-58 (`warrant_sourced` discriminator; which acts need consent is Jordan's content), CR-59 (authority-staged hand-built route, basis beside `pardon`'s in `gate.py`), CR-60 (one `may_determine` with authority conjunct; `scope_rung`), CR-61 (a `case` Record kind lands with readers; delete H-80 default labels; re-pin `BASE_HASHES[1, 2]` and go07 `BASE` seeds), CR-62 (concession reward through the obstacle under D-1), CR-63 (five verb rows), CR-64 (forum plea as stage of same case), CR-65 (design file only; needs P4 Q2's answer) (:23-33).
  - Inputs: `proposals/2026-10-29-parliament-and-debate/` (P4 authority-staged proposal, matters-standpoints fold, build-all plan, probes `probe_event_kinds.py`, `probe_controls.py`, `probe_routes_hand_built.py`).
  - Pre-flight checks B10-08's closed form: `engine/dice_engine/sigma_leverage.py::p_success` against the live roll at pool 2 and 12, Ob 2.5; ".3899 closed against .3875 sampled at 5D; the live discrete path read .581 against .430 at 2D" — CR-62 starts only if they agree (:18).
  - Symbols that must be absent before the build (`authority`, `scope_rung`, `appeal_to`, `case` Record kind, `<verb>.unlicensed`); a present hit means the plan is stale (:20).
- **Conflicts / stale:** "the live discrete path read .581 against .430" is a DICE discrepancy (live vs closed form) an SC/DICE audit must check; `VERB_CAPABILITY` and the H-80 default labels are named for deletion.
- **Open items:** P4 Q2; port gate placement before B10-20.

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-19.md
- **What it is:** [READ PARTLY: lines 1-12, 27-35, 63-102 and ### headings of 140 lines] Instructions for batch B10-19, DESIGN-FIRST CLUSTERS (narration, tenth attribute, troop stock, thrust ladders, Court Parliament's bench).
- **Status:** "instructions under the adopted plan" (:2); "This batch changes no code. Every position is HELD ... or DESIGN-FIRST" (:8). Reading: live; the CL-THRUST section is the authoritative statement of what of the thrust layer is released.
- **Bears on:** CHAR, WR, MB, SC, PC, CORE.
- **Content that matters:**
  - CL-THRUST (:81-102): M20 "(b) yes in part": a sequence is an ordered list of stage conditions read from the person's own ledger that only adds referents to his own `need` question; `closing`, `successor`, `deal` are struck, R3' and stage `deadline` excluded; key named `goal_stages` not `ladders:`; M21(a): `Felled` is death, no `Slain` band, B5.1 cut. Released: B0.1 → B10-02 lane 2; B2.1/B2.2 → B10-05 after `layer-conformance` Lens B answers TL :462-467; B3.1 → B10-05; B3.2 R2 only → B10-09 close two.
  - Still held: B4.1 (docket crossing) gated on `determine` executing in computed play (3 of 43 at the register's base); B4.2 (bound-peace reader) gated on `covenant` executing (0 of 70); B5.2 on IN-36's `guards` flip; B6.n content is Jordan's, no builder. Arc rule (:98): a ladder names its source arc and its `ENDINGS_CLASSIFIED.yaml` class, drawn only from DECIDER/ROLL classes.
  - CL-ATTR: tenth attribute name held on J-T2 (TS or Recall with reader built first); carrier absorbed by CR-20 (`Person.attributes` keyed by nine registry keys; the tenth slot refuses a value) (:63-70).
  - CL-TROOP held on M3 (Layer 1 `04:793`/`:802` amendment for counted troop stock); NM-W1 PARTLY LANDED (chronicle render exists), NM-W4..W9 UNBUILT, DESIGN-FIRST; CR-38 Court Parliament's bench DESIGN-FIRST; CL-SLICE/OPEN/PERSON/MGMT design-first on `-10` questions (:27-120).
- **Conflicts / stale:** `ENDINGS_CLASSIFIED.yaml` counts "48 classified arcs" here (:98) vs "50" in thrust-layer docs [UNVERIFIED which is right].
- **Open items:** J-T2; M3; M1 residue; B4.x/B5.2/B6.n gates.

### proposals/2026-10-24-master-workplan-v10/2026-10-24-v10-09-build-B10-Z.md
- **What it is:** [READ IN FULL] Instructions for batch B10-Z, HELD AND LEAVE (all lanes): nine entries FA-03, FA-07, MB-08, PC-06, PC-08, IN-44, SC-05, SC-07, CR-39.
- **Status:** "instructions under the adopted plan" (:2); "This batch changes no code" (:8). Reading: live; entries are holds, not work.
- **Bears on:** PROCESS, FA, SC, MB, PC, CORE.
- **Content that matters:**
  - IN-44: 16 owed Layer 0/1 edits, row 1 released by M15(a); rows 2-16 unscheduled; each anchor re-derived by symbol and checked for a (RULED) mark (:24-27). Row 13 (`RemoteTrigger` vs CLAUDE.md §11 deny-list) listed for Jordan, no agent edit to settings.
  - SC-05 RET-SC: delete `systems/social_contest/sim/contest/` and `engine/tests/test_contest_kernel.py`, relocate degree veto as forwarded `extension=` at `engine/season/seam/ladder.py`, fold `sim-regression` job into `unit-tests` (a workflow edit: Jordan's file); `systems/social_contest/` stays (:31-35).
  - FA-07 faction-vs-faction mechanisms: every stored clock refused (T-a, T-c, A-29); each aggregate restated as a Query (Piety Track → share of residents whose live `commit` is to the Church's Proposition; Church Attention → each seat-holder's own attention) (:55-58).
  - CR-39 promotion of an emerged creed: "the retired oracle's `L` was initialized at 1.0 and never written, so promotion was unreachable by construction" (`git show 5c5d8ec6:systems/world/sim/insurgency_pipeline.py`) (:63-72).
  - PC-06: `Person.attributes` (K-2) builds only with its first reader; MB-08: commander-chosen orders are a named residue (`massbattle.py:170-178`) (:90-103).
- **Conflicts / stale:** the SC-05 deletion would orphan modules the SC audit may reference.
- **Open items:** IN-44 rows; SC-05 timing (scheduling call); CR-38/CR-39.

### proposals/2026-10-25-thrust-layer/00_THRUST_LAYER_DESIGN.md
- **What it is:** [READ IN FULL] Design (v2, 2026-10-25, one adversarial round) for a "thrust layer" in `engine/season/`: authored typed LADDERS of stage predicates under an ambition, plus closure engines, constraints on death and a standing gate. Producer + opus critic.
- **Status:** "PROPOSED — HELD BACK IN FULL (v2). PARTLY RULED since" (:3): the v10 plan folds it in as `CL-THRUST` (`workplans/valoria_master_workplan_v10_part12.md`); M20/M21 (ED-IN-0301, `v10_part6.md`) exclude R3' and the stage `deadline`, strike `closing`, `successor`, `deal`, and cut the `Slain` band and B5.1; B4.x, B5.2, B6.n held. Reading: partly superseded/live-in-plan; line numbers cited inside it have drifted (:5).
- **Bears on:** CHAR, CORE, WR, FA, PC, SC.
- **Content that matters:**
  - Thrust = an existing `commit` tenure to an OUGHT Proposition (`world_q.ambitions`); ladder = authored data; "current stage" is a query over the person's OWN ledger (person-side, AX-2), never a stored counter (:8-21, :40, :172, :194-197). Closed roster `thrust_axes` (ten axes plus opposite poles) in `rosters.yaml`, new `axis:` / `ladders:` keys on `goals.yaml` through the one loader `data/goals.py` (:107-142).
  - ARC predicate (:48-56): an act formed from a `need` question about the thrust, with a self-effect and a world-effect Receipt linked by `causes[]`. v1 was met by WITNESS bookkeeping (`witness.py:654-657` + `world.py:1306-1322`); v2 restricts to `arc_effect_fields` rosters, driver-side reading; the filter is itself flagged as insufficient because MATTER rewrites `Person.body`, `Rung.stores`, `Site.condition` every season (:65). Built reader `harness/arc.py` states the same limit.
  - R3' (promote a `need` question to tier 0 for one season per `deadline`, keyed-draw phase) replaces a standing promotion because unconditional tier-0 starved news (events 21,735 to 15,738; `news.told` 14 to 7, `world_q.py:2608-2612`) (:174-182, :213-230). Falsifier: `news.told` falls beyond seed spread.
  - Closure only by lawful forms: threshold-raised docket matter (a MATTER step on `_standing_crossings`' shape that writes nothing), bound peace via `covenant` + a NEW `(verb, referent)` decline reader, succession belongs to IN-61 (RULED RS-27: heir is a title, still has to claim), authored set piece via `arrangements.yaml` (:245-261).
  - Death is rare: `Felled` currently deletes (`verb_table.yaml:716,:802`); proposal splits `Felled`=down-alive from a new `Slain` band (:267-280; later CUT by M20/M21). Standing gate: `admits_audience` reaches only 3 of 31 seats (`cohorts.yaml:127-130`), so G1-G3 would seat guards for every seat that is a -1 `seat_holders` referent and add an `audience` conjunct to `fight/challenge/accept` (:282-307).
  - Per-axis ladder buildability (:332-418): axis J (heal Calamity) unbuildable (threadwork "built and inert"); caste has no store (D3: a Query over affiliation convictions); `construe` is `grade: absent` and not a weapon; 13 of 56 verbs write nothing (:89-90).
- **Conflicts / stale:** Cited line numbers in `queries/world_q.py` drifted (:5). The measured figures (51/803 need; 929/1,318 refused) are SUPERSEDED inside by `01_MISSING_IN_CODE.md` P1/P2/P10. Cites retired `valoria_master_workplan_v9*.md`. The toy-world results (:513) are post hoc with informed predictions.
- **Open items:** D1 (is a beaten fighter ever killed; where the `Slain` edge sits; later cut), D4 (line between licensed "sequence" and unlicensed "entire arc", Jordan 2026-08-18) (:496-497); `WoundTracker` separating down from dead is [ASSUMPTION]; G2's `audience` reader widening and R1's `subject := referent` binding are Layer-1 questions (:462-467).

### proposals/2026-10-25-thrust-layer/01_MISSING_IN_CODE.md
- **What it is:** [READ IN FULL] Gap register (29 rows G-01..G-29) beneath the thrust layer, built from probes P1-P12 run on `build_realm` seeds 0-4; v2 after one antagonist pass.
- **Status:** "PROPOSED — HELD BACK IN FULL; its gaps are folded into the v10 plan as `CL-THRUST`" (:5). Grades are as of 2026-10-25; B10-02 (#509) later landed instruments for G-02, G-08, G-11, G-12, G-20, G-27-G-29, so those rows need re-reading. Reading: reference; live as a measurement record.
- **Bears on:** CORE, CHAR, FA, PC, WR, SC, FI.
- **Content that matters:**
  - Headline measurement: 76.2% (2 seasons) / 76.8% (4 seasons) of 7,402 / 16,116 attempted acts are REFUSED on the driver's definition (`loop/driver.py:489-505`); 73.8-73.9% with graded losses excluded (:37, :76). 28.7-32.2% are refused at admission because the subject lives in another collection (wrong-kind formation) (:47, :74).
  - Closers barely execute at 4 seasons (exe/att): determine 3/43, confer 10/111, covenant 0/70, revoke 0/32, commit 8/564, restore 0/250, tend 0/302, build 0/230, found 1/208, work 3/726; `arrest` never forms; `succeed` not in `resolvable_verbs()` (:37, :77-80). `build/found/work` cannot execute in computed play at all (ED-IN-0297: a computed act "always mints `text`") (:78).
  - Deaths: 20 in 5 seeds x 4 seasons, 16 seat-holders, 11 by `accept`, 9 by `fight`; 0 of 11 `accept` deaths had a challenge from the other party (P4, P11b); no `person.died`/`tenure.closed` claim ever names the dead holder's seat (H-206, H-209) (:41, :48, :103-106).
  - H-156 (decline wrong-kind formation vs accept the tax) is the register's largest OPEN ruling and "survives all five steps"; only H-156's options (a) `withheld_verbs`, (b) more classed sources, (c) person-side known-false test survive; the v1 rule is withdrawn for six reasons (:74, :177, :182).
  - Of 38 `goals.yaml` rows only 12 mint a Proposition in the shipped realm; no seat-attached goal binds anyone; `need` scenes 24-28% of scenes, about a goal only 7.1-8.5% (:38, :87-89).
  - Executable terminus exists and TL misses it: `world_q.endings_reached` over `rosters.yaml: endings`, reported once per season (:97, :153); suggested key name `goal_stages` because `ladders` names two other things (:96).
- **Conflicts / stale:** G-02: a contested act refused at admission never enters `SeasonDriver.resolved`, so aperture's attempted count (1,182) differs from the driver's (1,511) (:75). Four readers classify "refused" differently (G-03, :76). `age_at_build` is not sweepable on a built world (G-22, :120). `storybar`/`chronicle` count refused acts as story: 30.4% cross-person as read vs 17.9% executed-on-executed (G-27, :135). Row grades older than B10-02.
- **Open items:** H-156 ruling; H-240 route for PC-10b (`accept` with no challenge); ED-IN-0297 (where a works comes from); share of delivered questions fed by a refusal-kind claim not measured (:186, :210); player seat bypasses `opening_set` (O1, :186).

### proposals/2026-10-25-thrust-layer/02_MAJOR_TAKEAWAYS.md
- **What it is:** [READ PARTLY: lines 1-120, 149-400 opened; §4 second half (lines 120-148) not opened] Expansion of eight session takeaways (T1-T8) with evidence tags [engine]/[toy]/[critic], corrections table and a "needs Jordan" list.
- **Status:** "PROPOSED — HELD BACK IN FULL" (:3). Currency note (:5-8): folded into v10 as `CL-THRUST`; M19/M20/M21 and ED-IN-0301 decided H-156, D4, D1 since (:386). Reading: reference; derivative of 00 and 01.
- **Bears on:** CORE, CHAR, PC, WR, FA.
- **Content that matters:**
  - The decided-since list (:386): H-156 = M19(a) (`v10_part11.md:13`); D1 = M21(a), no `Slain` band (`v10_part6.md:181`); D4 = M20 narrowed (`v10_part6.md:172`); PC-10b/H-240 = route (1) (`v10_part3.md:192`); ED-IN-0297 closed by a superseding row (`editorial_ledger_in.jsonl:81`). An audit must read those rows, not the open-looking text above them.
  - Toy table (:154-167): arc-minus-null for ladder + decisive-form set piece + bound peace = +0.244 [+0.188, +0.303] (0.24 deaths/run); same set piece without ladder +0.016; ladder + tribunal under constraints +0.010; bottom-up -0.056. Unconstrained ladder+tribunal was +0.09; "does not transfer under the constraints".
  - T5 "do not build" (:249-283): lookahead-biased choice costs ~270x run time and cuts explained motive 0.58 to 0.29; a blind script violated world constraints 96% of runs; a forcing director dictates a death in 99% of arc-passing runs. Any sigma-leverage correlate would live at the choice stage in tau units of `choice_temperature`, soft-capped (:271-274).
  - T6/T7 (:287-330): 0 threadwork modules load in a season; 29 of 46 registry rows have `age: null` (H-208); all 46 NPC `ends_when` are prose; every axis has a non-lethal closing act in existing verbs.
  - Corrections table (:357-369): 929/1,318 refused → 76.2%; 33% wrong-kind → 28.7-32.2%; "51 of 803 need" not reproduced; the claim H-156 "sits in no workplan" was wrong.
  - Excludes: human legibility testing; player character (bypasses `opening_set`); share of questions fed by refusal-kind claims (:371-382).
- **Conflicts / stale:** the exile-vs-settlement toy comparison was run inline and not saved [UNVERIFIED] (:172-173, :368). Primary literature (Compton, Ryan, Façade, Riedl) read via repo research files only (:377).
- **Open items:** human-reader test of narrative quality; refusal-kind-claim share; exile arm.

### proposals/2026-10-25-thrust-layer/probes/p10_clean_remeasure.py
- **What it is:** [READ PARTLY: docstring and imports, lines 1-22 of 192] Scratch probe (P10) re-taking wrong-kind refusal per act, graded-loss share and `_admits` double calls; orchestrator, v2, 2026-10-25.
- **Status:** no Status line (script). Reading: historical measurement instrument, not wired into CI; hard-codes `sys.path.insert(0, "/home/user/ttrpg")` and wraps driver-instance methods.
- **Bears on:** CORE, CHAR.
- **Content that matters:**
  - Classifies refusals into collection_mismatch / subkind_mismatch / subkind_wrong_coll / world_read_docket / absent_subject (:3-12); graded loss = every refusal-kind Event degree Failure AND kind also in the row's `emits` (:13-15).
  - Output saved as `p10_out.json` and `p10_s4.txt`; reads `engine/season` owners (`SeasonDriver`, `build_realm`, `loop.resolve._admits`) by import, so it breaks if those are renamed.
- **Conflicts / stale:** Reproduces P1 totals exactly per `01` §2; Line refs it uses into `loop/resolve.py` have drifted since (the design says so for `world_q.py`).
- **Open items:** none stated.

### proposals/2026-10-25-thrust-layer/probes/p10_out.json
- **What it is:** [READ IN FULL] Saved output of P10: counters at 2 and 4 seasons, seeds 0-4 pooled.
- **Status:** data file. Reading: historical record of one run.
- **Bears on:** CORE.
- **Content that matters:**
  - s2: attempted 7,402; refused 5,639; executed 1,763; wrongkind_collection 2,385; graded_loss 175; refused_kind_also_in_emits 1,299 (:1-17).
  - s4: attempted 16,116; refused 12,372; executed 3,744; wrongkind_collection 4,620; graded_loss 469; subkind_mismatch 174; world_read_docket 216 (:18-34).
  - Internal check: 4,063 + 557 = 4,620 (collection_mismatch + subkind_wrong_coll), matching `01` G-01.
- **Conflicts / stale:** `wrongkind_any` (2,442 / 4,794) is a third figure the prose never quotes.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p11b_accept_challenge.py
- **What it is:** [READ PARTLY: docstring, lines 1-22 of 82] Probe P11b: for each death whose cause is an `accept`, whether a `challenge.issued` Event or ledger claim stood behind it.
- **Status:** script. Reading: historical.
- **Bears on:** PC, CORE.
- **Content that matters:**
  - Measures `issued_by_subject`, `issued_either`, `ledger_claim` per accept-death, plus supply of `challenge.issued` per seed (:1-10).
  - Result per `01` G-15: 0 of 11 accept-deaths had a challenge from the other party; 4 of 11 ledgers hold some challenge claim.
- **Conflicts / stale:** its usage line names `p11_accept_challenge.py` (the superseded name), not the file's own name (:11).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p12_fallback_kinds.py
- **What it is:** [READ PARTLY: lines 1-22 of 42] Probe P12: acts whose only Events are the fallback kinds `act.ineligible`/`act.refused`.
- **Status:** script. Reading: historical.
- **Bears on:** CORE.
- **Content that matters:**
  - Checks `FALL & set(REFUSAL_KINDS)` (empty per `01`): fallback kinds sit in no row's `emits_on_refusal`, so such acts count as EXECUTED (:3-4, :14-16); 6 of 681 executed acts (0.9%) at seeds 0-1.
- **Conflicts / stale:** none noted.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p1_out_s2.json
- **What it is:** [READ PARTLY: head 1.2 KB of 5.4 KB for the sibling seed0 file; this file's per-verb table opened only via `01` §3] Saved P1 output, 2 seasons x seeds 0-4, pooled per verb.
- **Status:** data file. Reading: historical.
- **Bears on:** CORE.
- **Content that matters:**
  - Per-verb attempted/executed/refused with refusal-kind keys (`rk:accept.refused` etc.); pooled totals reproduce `01` §3 (7,402 / 1,763 / 5,639).
- **Conflicts / stale:** `[UNVERIFIED]` against the file itself beyond the head; figures taken from `01`.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p1_out_s2_seed0.json
- **What it is:** [READ PARTLY: first ~1.2 KB of 4.2 KB] Saved P1 output, seed 0, 2 seasons.
- **Status:** data file. Reading: historical; a hash-stamped control.
- **Bears on:** CORE.
- **Content that matters:**
  - seed 0: log_len 21,710; hash `5301d6b62af614f4`; persons 80; attempted 1,511; executed 335; refused 1,176; null 0 (head). The 1,511 vs aperture's 1,182 is the G-02 gap.
  - accept 48 attempted / 44 refused / 4 executed; commit 64 / 63 refused; covenant 14 / 14 refused; determine 6 / 6 refused (head).
- **Conflicts / stale:** none. Note: this hash is the content hash of a 2026-10-25 tree; the engine has moved (B10-xx), so it will not reproduce today [UNVERIFIED].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p1_out_s4.json
- **What it is:** [NOT OPENED beyond `01`'s account: SKIPPED body] Saved P1 output, 4 seasons x seeds 0-4.
- **Status:** data file. Reading: historical.
- **Bears on:** CORE.
- **Content that matters:**
  - [SKIPPED: /home/user/ttrpg/proposals/2026-10-25-thrust-layer/probes/p1_out_s4.json body — a 5.6 KB data table duplicating `01` §3; the pooled 4-season totals (16,116 / 3,744 / 12,372) are cited from `p10_out.json` instead]
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p1_refusal_census.py
- **What it is:** [READ PARTLY: docstring and imports, lines 1-22 of 115] Probe P1: per-verb attempted/executed/refused/null census copying `loop/driver.py:489-505`.
- **Status:** script. Reading: historical, but it IS the pattern later landed as `harness/aperture.py`'s pooled block (B10-02).
- **Bears on:** CORE.
- **Content that matters:**
  - Wraps `SeasonDriver.resolve` and `.encounter` on the instance, composition copied from `harness/storybar.py::drive` (:3-5); usage via `PYTHONHASHSEED=0 python3 probes/p1_refusal_census.py SEASONS SEED...` (:10-11).
  - Imports `make_chooser`, `SeasonDriver`, `resolvable_verbs` (:20-22) — three engine seams.
- **Conflicts / stale:** docstring says "run as ... python3 probes/..." but file hard-codes the absolute repo path.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p2_goals_and_need.py
- **What it is:** [READ PARTLY: lines 1-22 of 66] Probe P2: goals.yaml by object/org kind; what `seed_goals` minted; scene occasion source over a run.
- **Status:** script. Reading: historical.
- **Bears on:** CHAR, CORE, FA.
- **Content that matters:**
  - Reads `engine.season.data.goals` (`G.goals()`), `harness.populated.build_realm`, `queries.world_q` (:10-16); reports occasion source of every Scene via the Scene's `occasion` (:2-4).
  - Result per `01`: 38 rows (24 orientation / 6 seat_holders / 4 rung / 4 deed_doers); only 12 mint a Proposition in the shipped realm.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p3_refusal_reasons.py
- **What it is:** [READ PARTLY: lines 1-22 of 68] Probe P3: wraps `loop/resolve.py::_admits` to record why closer verbs refuse.
- **Status:** script. Reading: historical.
- **Bears on:** CORE, FA, SC.
- **Content that matters:**
  - CLOSERS list of 23 verbs (:20-22) including determine, confer, covenant, open_case, commit, release, oblige, revoke, arrest, issue, petition, found, build, work, give, restore, tend, migrate, research, examine, fight, accept, challenge.
  - Finding: no closer refusal is an eligibility refusal; refusals are precondition refusals on wrong-kind subjects (`01` §2 P3).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p3b_kind_mismatch.py
- **What it is:** [READ PARTLY: lines 1-22 of 83] Probe P3b: kind mismatch across all verbs; refusals after admission.
- **Status:** script. Reading: SUPERSEDED by P10 (own v2 account, `01` §2 P3b): its 7,737 counted `_admits` CALLS, not acts, and mis-classed Record sub-kinds and DocketItem.
- **Bears on:** CORE.
- **Content that matters:**
  - Still-valid output: 0 ineligible refusals; admitted-then-refused leaders migrate 705, transfer 136, move 112, forge 90, surveil 89, raze 84, survey 70, tell 65 (`01` P3b).
- **Conflicts / stale:** the 33.1% headline is withdrawn.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p4_killing_consequence.py
- **What it is:** [READ PARTLY: docstring, lines 1-22 of 83] Probe P4: what a death does in computed play (seats held, killer act, claims, later occasions).
- **Status:** script. Reading: historical.
- **Bears on:** PC, CORE, WR.
- **Content that matters:**
  - For each removed person: seats at start of season, claims naming him by predicate, claims naming his seats at/after death (H-206), later occasions naming killer AND about a claim on the dead (H-209) (:3-10).
  - Result: 20 deaths, 16 seat-holders, `accept` 11, `fight` 9; 0 `person.died`/`tenure.closed` seat claims; 0 later killer-about-dead occasions.
- **Conflicts / stale:** matches claims against end-of-run ledgers, so an evicted claim would be missed (R14 "could not verify").
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p5_exogenous_switches.py
- **What it is:** [READ PARTLY: lines 1-22 of 52] Probe P5: each dark exogenous switch set to its own fixture comment's sweep value, seed 0, 2 seasons.
- **Status:** script. Reading: historical.
- **Bears on:** WR, CORE, CHAR.
- **Content that matters:**
  - Arms: control, `body_step=10`, `age_step=0.01`, `illness_rate=0.05` and others (:19-22). Results per `01`: `body_step`/`illness_rate`/`season_factor_draw`/`lattice_coupling` move the hash; `age_step=0.01` and `age_at_build=160` do NOT (ages 0-1; `Person.born` fixed at construction).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p6_case_termini.py
- **What it is:** [READ PARTLY: lines 1-22 of 58] Probe P6: classifies the 46 NPC cases' `ends_when` strings by lexical markers via `harness/run_cases.load_cases("NPC")`.
- **Status:** script. Reading: historical; `01` itself says its strict-regex 28 "is a fit to the strings, not a measurement".
- **Bears on:** CHAR, ARCS.
- **Content that matters:**
  - NEVER and PRESUMED regexes (:18-21); cross-reads `engine/season/ENDINGS_CLASSIFIED.yaml` (an agent's prose classification).
  - Count: 40 of 46 by the extractor's own marker; 28 by the strict regex.
- **Conflicts / stale:** uses `python3 -I` in usage (:9) yet imports via `sys.path.insert`; fine.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p7_chain_refusals.py
- **What it is:** [READ PARTLY: lines 1-22 of 51] Probe P7: do `storybar`/`chronicle` count refused acts as story.
- **Status:** script. Reading: historical.
- **Bears on:** CORE, WR.
- **Content that matters:**
  - Runs `storybar.drive`, reads `storybar.read` + `chronicle.deepest_chain`, classifies by the driver's rule; recomputes cross-person share with refused antecedents removed (:1-9). Result: 55 of 66 deepest-chain acts refused; cross-person 30.4% as read vs 17.9% executed-on-executed.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/probes/p8_thread_import.py
- **What it is:** [READ IN FULL, 17 lines] Probe P8: lists `sys.modules` with "thread" after one season and verb rows/event kinds naming thread/lattice/Calamity.
- **Status:** script. Reading: historical; the strongest single execution-evidence that threadwork is not in the season loop.
- **Bears on:** WR, CORE.
- **Content that matters:**
  - Result per `01`: 0 threadwork modules loaded; one verb row (`thread_read`); 0 thread/lattice/Calamity event kinds; log 7,018 events (:6-17).
- **Conflicts / stale:** it is a snapshot (2026-10-25); a later B10 position could have wired threadwork [UNVERIFIED].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/reports/R01_partial_top_down.md
- **What it is:** [READ IN FULL] Chat report: is pure bottom-up emergence a problem; can partial top-down guides help (with the oatmeal-problem literature).
- **Status:** "REFERENCE — HELD BACK IN FULL"; figures predate the register's probes (:5).
- **Bears on:** WR, CHAR, CORE.
- **Content that matters:**
  - Verdict: partial top-down in three places only: standing motives held by actors, selection of what the player is shown, a narrow declinable occasion channel; every state change stays bottom-up.
  - `goals.yaml` already has referents/attention-only shape (`goals.yaml:9-12`) but no lifecycle field; offices: `remit_acts` is a licence not an obligation, 2 of 38 goal rows attach to a seat; cohorts carry no wants (`cohorts.yaml:18-23`).
  - Keeps refusal of need-triggered outcome injection even with Jordan's permission to overrule: a threshold that acts is an actor; an injected beat cannot be contested; storybar would measure its own injections.
- **Conflicts / stale:** 929/1,318, 51/803, 33% figures superseded (`02` §9).
- **Open items:** [GAP] primary literature not re-fetched; human-reader ablation of the recognition layer not run.

### proposals/2026-10-25-thrust-layer/reports/R02_arcs_deconstruction_and_logic_tests.md
- **What it is:** [READ IN FULL] Chat report: seven ways the corpus achieves arcs; toy logic tests of BU/TD/TDR/HY.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** ARCS, WR, CHAR.
- **Content that matters:**
  - Seven arc engines: accrual, exposure, succession, decision point, contest, conjunction, held control state; closes by decider 20/50, crossing-forced 19/50, never 10/50, roll 9/50, threshold 8/50.
  - Hand classification of the 46 NPC cases by `ends_when`: forks 11, exit-only 7, presumed 12, nothing authored 16 (names ids) — one reader, since superseded in count by P6.
  - "~13 shapes" figure comes from 24 of 138 arcs; the calibration set was evacuated.
- **Conflicts / stale:** "the corpus is top-down by origin" — every arc is an authored predicate (Jordan 2026-08-18).
- **Open items:** spirals (ARC-05) not visible to the three-act test.

### proposals/2026-10-25-thrust-layer/reports/R03_sigma_leverage_correlate.md
- **What it is:** [READ IN FULL] Chat report: is there a sigma-leverage correlate for the likelihood of subsequent events.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** DICE, CHAR, WR.
- **Content that matters:**
  - Yes in form: `decision/choose.py::_sample_order` orders by `softmax(score/tau)`, `choice_temperature = 0.1`; a narrative term would be expressed in tau units, soft-capped like `sigma_leverage.py`'s `soft_cap`, on the choice stage, never the dice resolution, never removing an option.
  - Toy table: ladder+tribunal arc-minus-null +0.09 [+0.04, +0.15]; lookahead strength 4 = -0.08 [-0.14, -0.01], ~270x run time; explained motive 0.58 → 0.29.
  - It would override v2 narrative-engine rules R-AI and F8 (F8 would become a dosimeter).
- **Conflicts / stale:** toy only.
- **Open items:** two-level lookahead, human judgement of "construable".

### proposals/2026-10-25-thrust-layer/reports/R04_ladder_tribunal_best.md
- **What it is:** [READ IN FULL] Chat report: is ladder + threshold-raised tribunal the best.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** WR, CHAR.
- **Content that matters:**
  - "No": leads only on arc rate without outcome-writing; ordering signal depends on threshold (holds at 4.5-10, weak at 3, gone at 16); closure is one template (192 of 293 runs close on a tribunal ruling); thread continuity lowest of six arms (0.58).
  - Ladder alone: multiplies cross-person chain depth ~2.7x (62.5 vs 23.0) and keeps legibility 0.72.
- **Conflicts / stale:** the threshold-sensitivity table was printed, not saved.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/reports/R05_scripted_director_set_pieces.md
- **What it is:** [READ IN FULL] Chat report: a director that injects set pieces rather than outcomes.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** WR, SC, PC.
- **Content that matters:**
  - Situation-only set piece fizzles (ordering -0.04); decisive-form set piece (best-of contest, lethal climax) +0.14; ladder + decisive form +0.20; at 80% refusal the decisive-form arm holds 0.81 but "likely an artifact" because the toy contest bypasses the act layer.
  - Trade: "dictated outcome for dictated form and stakes" — an authored occasion that is not declinable.
- **Conflicts / stale:** cites `regimes7.py`, which is in `toy/` but not in this lane's assignment.
- **Open items:** declinable set pieces, mid-run stake adjustment untested.

### proposals/2026-10-25-thrust-layer/reports/R06_npc_deaths_clarification.md
- **What it is:** [READ IN FULL] Chat report: "94% end with both principals alive" does mean toy NPC deaths.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** WR, PC.
- **Content that matters:**
  - Decisive-form lethal arms kill one principal per run (principals dead 1.00); the ordering signal depends on that death (exile +0.01, pact +0.03, lethal +0.14) partly because the test requires a post-peak fall. Tribunal kills no one and keeps +0.09.
  - Corrects R05's headline: holds only for the lethal climax.
- **Conflicts / stale:** the non-lethal run was printed not saved; code `regimes8.py` (not in assignment).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/reports/R07_arcs_without_deaths.md
- **What it is:** [READ IN FULL] Chat report: arcs without NPC death; death rare, fighting authority hard, killing consequential.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** PC, WR, FA.
- **Content that matters:**
  - Prior arc-passing runs closed on a death in 99% (forcing director), 94% (lethal set piece), 98% (ladder + lethal), 3% (ladder + tribunal); 19-36% of harm events hit a prize holder.
  - Constrained-world table (:20-30); killing consequence package: kin grievance, witnesses turn, forfeiture, infamy, vacated holdings → ~9.5 acts by ~4.9 actors, ~1.3 tribunals, no runaway feud.
  - Real engine: `fight` needs only existence and co-location; `Felled` deletes the person; the "deontological gate" the row mentions does not exist.
- **Conflicts / stale:** `regimes10.py` + `exp_con_out.txt` saved; review table and killing-at-season-10 printed only.
- **Open items:** trial, succession politics, longer feud unbuilt.

### proposals/2026-10-25-thrust-layer/reports/R08_ten_axes.md
- **What it is:** [READ IN FULL] Chat report: the user's ten goal axes mapped to `goals.yaml` rows, existing verbs and gaps; the arc criterion as a test.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** CHAR, FA, WR, ARCS.
- **Content that matters:**
  - Ten axes list and per-axis table (:25-36): rows today, verb ladders, gap. Tension already authored for four (1 vs 10, 5 vs Kommerkiarios, 2 vs Varfell thread-truth, 3 vs Church orthodoxy); missing poles block caste (4) and healing (9).
  - Arc criterion: one actor's goal-driven chain with a self effect and a world effect, linked by `causes[]` — the form later made the `ARC(p, a)` predicate.
  - Says at least nine verbs write nothing (later corrected to thirteen by R12).
- **Conflicts / stale:** "nine verbs" superseded by thirteen (R12).
- **Open items:** the 46 character cases not mapped onto the axes.

### proposals/2026-10-25-thrust-layer/reports/R09_design_verdict.md
- **What it is:** [READ IN FULL] Chat verdict after the design relay (thrust layer designable, not buildable yet).
- **Status:** "REFERENCE — HELD BACK IN FULL"; carries a recorded correction that "sits in no workplan" is wrong (H-156).
- **Bears on:** CHAR, CORE, WR.
- **Content that matters:** one-page summary of design v2; four critic breaks (vacuous arc test, succession duplicate of IN-61, gate protecting 3 of 31 seats, R3 synchrony); asks Jordan D1 and D4.
- **Conflicts / stale:** cites `toy/thrust_layer_design_v2.md` (the design now lives one directory up).
- **Open items:** D1, D4 (since decided M21, M20).

### proposals/2026-10-25-thrust-layer/reports/R10_major_takeaways_as_first_delivered.md
- **What it is:** [READ IN FULL] The eight takeaways as first delivered in chat.
- **Status:** "REFERENCE — HELD BACK IN FULL"; superseded by `02_MAJOR_TAKEAWAYS.md` (:7).
- **Bears on:** CORE, CHAR, WR.
- **Content that matters:** same eight takeaways with first-delivery figures (929/1,318; 51/803; 28 of 46); says design item 1 "is the gate on all of them".
- **Conflicts / stale:** first-delivery figures wrong, see `02` §9.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/reports/R11_register_verdict.md
- **What it is:** [READ IN FULL] Chat verdict on the gap register after the relay.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** CORE, PC.
- **Content that matters:** G-01 design withdrawn (passed over open ruling H-156); P3b's 33.1% was calls not acts; G-16 re-owned to PC-10b; `endings_reached` added; stopped after one round per CLAUDE.md §0.
- **Conflicts / stale:** none beyond what 01 §7 records.
- **Open items:** share of questions fed by refusal-kind claims; player seat.

### proposals/2026-10-25-thrust-layer/reports/R12_design_producer_receipt.md
- **What it is:** [READ PARTLY: lines 1-66 of 113; the verbatim brief (:67-113) not opened] Design producer's hand-back for v1.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** CORE, CHAR, PC.
- **Content that matters:**
  - Corrections to the brief: thirteen verbs write nothing (adds `dispatch`, `challenge`, `evade / defy`, `speak`); `construe` is `grade: absent`; `offices.yaml` has 31 seats (16 null revoker / 13 same-faction / 2 in-holdings; header "14 of 29" stale); orientation rows mint no Proposition (:15-26).
  - `succeed`, `tie`, `knot` have no opener (`rosters.yaml:141-143`); ED-IN-0225 is cited in four `.py` files, not three.
  - Cheapest sinking test: count executed determine/confer/covenant/open_case over several seeds (:63).
- **Conflicts / stale:** v1 file not committed.
- **Open items:** the unverified list (:56-62).

### proposals/2026-10-25-thrust-layer/reports/R13_design_critic_report.md
- **What it is:** [READ PARTLY: lines 7-74 of 100; the verbatim brief (:75-100) not opened] Critic's report on design v1: findings F1-F16 with evidence.
- **Status:** "REFERENCE — HELD BACK IN FULL"; dispositions are in `00` final section.
- **Bears on:** CORE, CHAR, FA.
- **Content that matters:**
  - F1 BLOCKER: ARC clause (3) vacuous via `witness.py:654-657` + `world.py:1306-1322`; F2 BLOCKER: §4.3 chose the rejected succession carrier; F3 BLOCKER: gate reaches 3 of 31 seats; F6: `of: referent` unspellable, builder exits `SystemExit` (`data/requires.py:973-978`).
  - Confirmed true: 22 of 29 loop-built seats keep `dispatch`; 31 seats, 16/13/2 revocation split; conferral 6 null / 8 elected / 17 appointed (:62-64).
- **Conflicts / stale:** critic could not run code.
- **Open items:** none left (all accepted).

### proposals/2026-10-25-thrust-layer/reports/R14_register_producer_receipt.md
- **What it is:** [READ PARTLY: lines 44-70 of 106; head 1-43 and the verbatim brief not opened] Register producer's hand-back for v1.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** CORE, PC.
- **Content that matters:** findings outside the brief: G-02, G-03, G-27, G-16 (non-lethal duel already exists, unwired), G-15; `REFUSAL_KINDS` is at `data/verbs.py:1403` not `:1073`; could not verify why `arrest` never forms, whether `survey` mints a works record.
- **Conflicts / stale:** its S12 answer (IN-53 precedent) was overturned by the critic.
- **Open items:** its two escalations (fight_terms default, H-240) — the first withdrawn.

### proposals/2026-10-25-thrust-layer/reports/R15_register_critic_report.md
- **What it is:** [READ PARTLY: lines 7-64 of 89; the verbatim brief not opened] Register critic's report, findings A1-A14, O1.
- **Status:** "REFERENCE — HELD BACK IN FULL".
- **Bears on:** CORE, PC, FA.
- **Content that matters:** A1 BLOCKER G-01 passes over H-156; A2 BLOCKER rule unsound; A10 `world_q.endings_reached` missed (`world_q.py:1990-2024` at the time); lists six NEEDS-RUN probes (graded-loss share, clean P3b, refusal-fed questions, clause-4 decay, accept deaths, G-03 hash move) and what holds (P1 capture, hashes, P4 counts).
- **Conflicts / stale:** 12 of 46 citations failed in v1.
- **Open items:** refusal-fed-question share still unrun.

### proposals/2026-10-25-thrust-layer/reports/README.md
- **What it is:** [READ IN FULL] Index of R01-R15 with reproduction rules and a known-errors pointer.
- **Status:** "REFERENCE — PROPOSED, HELD BACK IN FULL"; R12-R15 kept under CLAUDE.md §0's terminal-verdict exception, "delete them if the exception becomes the general case" (:5-10).
- **Bears on:** PROCESS.
- **Content that matters:** R09 and R10 error (H-156 "unruled") and superseded refusal figures (:50-56); path rewrites only (:41-47).
- **Conflicts / stale:** R01-R11 are chat transcripts under `proposals/` — a candidate for deletion by the repo's own rule if the exception widens.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/README.md
- **What it is:** [READ IN FULL] Module table for the toy world (24 actors, 6 places, 6 prizes, 24 seasons) with pre-registration status.
- **Status:** "Grade: model-internal, low confidence. Reference ... Not game code, not read by any tool" (:3-4).
- **Bears on:** WR, PROCESS.
- **Content that matters:**
  - Only v1's predictions were blind; every later set is informed; HYc, HYd, bootstrap CIs, ladder, set-piece, constrained arms are post hoc (:30-38).
  - Checked 2026-10-28: prediction/experiment scripts match recorded hashes (13 of 17); `regimes.py`, `regimes2.py`, `regimes5.py`, `regimes10.py` do NOT match their freezes (:25-30) — the freezes cover predictions, not the world.
  - Several runs (`regimes8.py`, `regimes9.py`, review table, killing-at-season-10 cascade) printed not saved (:40-44). `real_engine_chronicles/` holds seeds 0,1,2,4,5 chronicles (:46-50).
- **Conflicts / stale:** README says `regimes.py` = `regimes_v1.py` byte-identical — verified by `cmp` (identical); `predictions.py` = `predictions_v1.py` also identical.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_closure.py
- **What it is:** [READ PARTLY: lines 1-16 of 25] Post-hoc experiment: threshold-forced, decider-closed moment (BU/TDR/HY/HYd) at base and 80% refusal, 300 seeds, bootstrap CIs. Imports `regimes3`.
- **Status:** script; labelled "POST-HOC, exploratory" (:1). Reading: historical; reference-only.
- **Bears on:** WR, PROCESS.
- **Content that matters:** the HYd arm (tribunal) experiment behind R02's 0.26 arc rate; output `exp_closure_out.txt`.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_con.py
- **What it is:** [READ PARTLY: lines 1-16 of 69] Constrained-world experiment: death_p=0.01, gate_p=0.9, accusation, truce, consequences; CON1 non-lethal and CON2 lethal. Imports `regimes10`.
- **Status:** script; "Predictions registered BEFORE the first run" (:2); see README on hash mismatch for `regimes10.py`.
- **Bears on:** PC, WR.
- **Content that matters:** constants `CON1`, `CON2` (:5-6) define the constrained-world parameters whose results the design quotes (+0.244 etc.).
- **Conflicts / stale:** world file's freeze hash does not match (README :25-30).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_contest.py
- **What it is:** [READ PARTLY: lines 1-16 of 66] Conclusive-form set piece experiment (best-of contest at a venue, lethal at climax); imports `regimes7` (not in this lane's list).
- **Status:** script; predictions frozen (`setpiece2_pred.sha`).
- **Bears on:** WR, PC, SC.
- **Content that matters:** arms BU, TDR, TDSc, TDScf, HYg3c, HYg3d at N=300 (:15).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_ladder.py
- **What it is:** [READ PARTLY: lines 1-16 of 52] Ladder experiment with pre-registered predictions H1-H7 (`ladder_pred.sha`); imports `regimes5`.
- **Status:** script; "Exploratory, post hoc to v2" (:2).
- **Bears on:** CHAR, WR.
- **Content that matters:** H1 ladder adds closure (>= +0.10); H2 depth dose; H4 ordering signal >= +0.05 (FALSIFIED per design); H5 motive preserved >= 0.70 (:5-14).
- **Conflicts / stale:** H1, H4, H7 falsified (4 of 7 held).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/exp_setpiece.py
- **What it is:** [READ PARTLY: lines 1-16 of 79] Set-piece director writing a situation (relocation + engagement window + optional stake multiplier); imports `regimes6` (not in lane).
- **Status:** script; frozen (`setpiece_pred.sha`); post hoc to v2.
- **Bears on:** WR.
- **Content that matters:** arms BU, TDR, TDS, TDSm, HYg3d, HYg3s (:16).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/lb_more.py
- **What it is:** [READ PARTLY: lines 1-16 of 26] Lookahead leverage comparison, lam 0 vs 4, 120 seeds, multiprocessing Pool(4).
- **Status:** script. Reading: historical.
- **Bears on:** DICE, CHAR.
- **Content that matters:** produces `lb_more_out.txt` (the lookahead -0.08 result); uses `lookahead.simulate_lb`.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/lb_sweep.py
- **What it is:** [READ PARTLY: lines 1-16 of 23] Lookahead leverage sweep lam in (0,1,2,4), 40 seeds, Pool(3).
- **Status:** script. Reading: historical.
- **Bears on:** DICE, CHAR.
- **Content that matters:** the lam sweep behind `lb_sweep_out.txt`.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/lookahead.py
- **What it is:** [READ PARTLY: docstring, lines 1-16 of 155] Toy implementation of choice-level "narrative leverage" with rollouts.
- **Status:** script. Reading: historical.
- **Bears on:** DICE, CHAR.
- **Content that matters:**
  - Models the engine's `choose.py::_sample_order` (Plackett-Luce/Gumbel over candidates with keyed noise) and adds `lam * tau * soft_cap(z_c)` with z_c standardised over THAT actor's candidates — "the mu-shift-in-sigma-units idea of sigma_leverage.py" (:3-9). Only "relevant" actors (participants of the top-3 threads) are leveraged — the casting rule (:13).
- **Conflicts / stale:** a rejected design (T5): reference only.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/metrics2.py
- **What it is:** [READ PARTLY: lines 1-16 of 235] Metric library for the toy (event selection `select(ev, B=12, top=3)`, etc.). No docstring.
- **Status:** script. Reading: historical.
- **Bears on:** WR, PROCESS.
- **Content that matters:** defines `executed(ev)` as events with delta > 0, a thread and an int actor (:1-3).
- **Conflicts / stale:** not imported by files read in this lane (regimes* define their own `run_metrics`) [UNVERIFIED by grep].
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/posthoc.py
- **What it is:** [READ PARTLY: lines 1-16 of 43] Post-hoc analysis after v2: HYc arm, bootstrap CIs, director templating, sifting availability; imports `regimes2`.
- **Status:** script; "POST-HOC (exploratory, run after v2)" (:1).
- **Bears on:** WR.
- **Content that matters:** output `posthoc_out.txt`; the HYc ("fired ambitions simply end") change-nothing result.
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/predictions.py
- **What it is:** [READ PARTLY: docstring, lines 1-16 of 160] Pre-registered v1 predictions (blind): conditions base/noent/engine(80% refusal)/small/null/pert.
- **Status:** script; byte-identical to `predictions_v1.py` (`cmp`).
- **Bears on:** PROCESS, WR.
- **Content that matters:** "the real engine refuses ~70-80% of acts" is embedded as a model parameter `refuse=0.8` (:5-6).
- **Conflicts / stale:** DOUBLED file: `predictions.py` and `predictions_v1.py` are the same bytes.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/predictions_v1.py
- **What it is:** [READ PARTLY: lines 1-16 of 160] Identical copy of `predictions.py` (verified `cmp`).
- **Status:** script. Reading: duplicate.
- **Bears on:** PROCESS.
- **Content that matters:** see `predictions.py`.
- **Conflicts / stale:** pure duplicate (README :8 names `predictions.py` = `predictions_v1.py`).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/predictions_v2.py
- **What it is:** [READ PARTLY: lines 1-16 of 112] v2 predictions registered after v1 results (L1 etc.).
- **Status:** script; "informed, not blind" (:1-3).
- **Bears on:** PROCESS, WR.
- **Content that matters:** L1 "apparent legibility does not discriminate: spread < 0.05".
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes.py
- **What it is:** [READ PARTLY: docstring, lines 1-16 of 599] v1 toy world: BU, TD, TDR, HY regimes; separate RNG streams (world / acts / ambition / director) so HY(w_amb=0, occasions off) hashes identical to BU as control.
- **Status:** script; byte-identical to `regimes_v1.py` (`cmp`). Reading: historical.
- **Bears on:** WR, PROCESS.
- **Content that matters:** the control idea (identical log hash when the feature is off) mirrors the repo's hash controls; the regime definitions (TD = blind script forcing a five-beat schedule; TDR = replan; HY = standing referent-bound ambitions + declinable occasion channel) (:3-14).
- **Conflicts / stale:** world-file freeze hash does not match (README).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes10.py
- **What it is:** [READ PARTLY: docstring, constants and function index; lines 1-60 and a `def` index of 1025] Final toy world: constrained world with rare death (`death_p`), standing gate (`gate_p`), accusation, bound peace (truce), killing consequences, `simulate(..., con=, killing_t=)` (:739).
- **Status:** script. Reading: historical; freeze hash mismatch (README).
- **Bears on:** PC, WR.
- **Content that matters:** W init defaults (:32-60): `death_p=0.25`, `gate_p=0.0`, `ladder_depth=3`, `deadline=6`, `cap=2`; metrics `arc_test` with `peak_hi=0.92` (:836); THETA=6.0 (:21).
- **Conflicts / stale:** none.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes2.py
- **What it is:** [READ PARTLY: docstring, lines 1-16 of 649] v2 instrument: pair-thread identity, plateau peak, burn-in, director thread.
- **Status:** script. Reading: historical; freeze mismatch.
- **Bears on:** WR.
- **Content that matters:** same regime docstring as v1.
- **Conflicts / stale:** four near-identical copies of the same ~600-line world (regimes, 2, 3, 5, 10 differ by added features).
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes3.py
- **What it is:** [READ PARTLY: lines 1-16 of 686] Adds terminal-lifecycle and threshold-raised tribunal arms.
- **Status:** script. Reading: historical.
- **Bears on:** WR.
- **Content that matters:** base for `exp_closure.py` and `lookahead.py`.
- **Conflicts / stale:** as above.
- **Open items:** none.

### proposals/2026-10-25-thrust-layer/toy/regimes5.py
- **What it is:** [READ PARTLY: lines 1-16 of 793] Adds goal ladders (HYg1-3) and ladder + tribunal.
- **Status:** script. Reading: historical; freeze mismatch.
- **Bears on:** CHAR, WR.
- **Content that matters:** base for `exp_ladder.py`.
- **Conflicts / stale:** as above.
- **Open items:** none.

## Reading-depth tally (for the holistic stage)

Of 100 assigned entries: 25 read in full; 74 read partly (statuses, headings, the sections named in each entry, and where the entry says so only the head or the grade block); 1 not opened beyond its siblings' account (`probes/p1_out_s4.json`). 18 entries carry an explicit `[SKIPPED: ...]` line naming the unread body. The most weakly read: `system-description-12-reference-appendices.md` (266 KB, headings only), tutorials 02-11 (Status blocks only), `subsystem-completion-08`/`08_part2`/`10` (headings only), `verb-key-rows_part2` (headings only), the toy `regimes*.py` worlds (docstring and function index only), and the B10-14..B10-18 cards (head and position headings). A later lane that needs line-level detail from those must open them.

## Cross-subsystem leads

- **CORE, all subsystems:** the refusal floor. Thrust-layer probes (5 seeds): 76.2% of 7,402 attempted acts refused at 2 seasons, 76.8% of 16,116 at 4; 28.7-32.2% refused at admission on a wrong-kind subject (`01_MISSING_IN_CODE.md` :37, :74; `probes/p10_out.json`). Any subsystem audit claim that a verb "executes in play" must be read through the driver's refusal rule (`loop/driver.py:489-505`), not `SeasonDriver.resolved`, which omits contested/graded acts refused at admission (G-02: 1,182 vs 1,511 at seed 0; the 2026-10-22 suite measured the same gap as 275 acts, `system-description-00` :50-62). Closer execution at 4 seasons (exe/att): determine 3/43, confer 10/111, covenant 0/70, revoke 0/32, commit 8/564, restore 0/250, tend 0/302, build 0/230, found 1/208, work 3/726. Tags: CORE, FA, SC, SE, PC, FI.
- **PC, CORE:** deaths come mostly through `accept` (11 of 20 in 5 seeds x 4 seasons; 16 of 20 seat-holders), and 0 of 11 had a challenge from the other party (`probes/p11b_accept_challenge.py`; `01` G-15). PC-10b's "an `accept` with no held challenge is refused" is the cut, gated on H-240's route (decided "route (1)", `v10_part3.md:192`). Also `Felled` = death (M21(a): no `Slain` band). PC-10a duel terms (`modules/combat/wrapper.py`) exist, inert; the season passes no `terms`. System-description 04: the season seam derives only `end` from a person; every fighter rolls `max(5, 3+6) = 9` (adjudication :160-186). Tags: PC, MB, CHAR.
- **DICE, SC, CORE:** two exact-odds disagreements. `sigma_leverage.p_success` is a Gaussian stand-in understating Partial-or-better by 10-15 points (pool 2/Ob 2: 14.4% vs 26.0% exact) while AX-7 says no state is hidden from the player (`system-description-00` :272); B10-18c's pre-flight requires "closed form vs live roll" agreement before CR-62 starts, quoting ".3899 closed against .3875 sampled at 5D; the live discrete path read .581 against .430 at 2D" (B10-18c :18). H-213's obstacle ceiling (default 2 = ceiling 2) clips every room/bench term: only the case against bites, a favourable bench cannot (completion-05 §7; CP-T01-06). Related audit ids: F-DICE-04, F-DICE-14, F-TEST-08. Tags: DICE, SC, FI.
- **CHAR, DICE, PC, MB:** the person has almost no capacities that reach outcomes. `Person.capability` is empty for 429 of 430 persons, `verb_capability` maps only `tell`/`speak`, 2 of 8 contested rows (`progression-adjudication` :115-160); the chooser's candidate gaps are 0.01-0.06 at tau 0.1 so any personality or attribute term needs tau or spread to move (`character-layers-v2` :137-142). Attribute roster is contested between three documents: six (adjudication), nine stored on 1-7 with practice (v10 M2 / ED-IN-0301), ten with an unnamed tenth (J-T2; CL-ATTR). ED-IN-0304 (2026-10-29) rules risk appetite and short/medium/long horizon wanted. Related audit ids: F-CHAR-01, F-CORE-15, F-MB-14. Tags: CHAR, DICE, MB, PC.
- **FI, SC (noir/detective intent):** T06 completion explicitly builds no case object, verifier, exposure meter or `disguise`/`infiltrate`/`eavesdrop` (completion-06 §7), SM-3 says "investigation is not a contest seam", and `reconstruct` stays dominated; T05 completion models proceedings (bench, verdict, docket) and states testimony of violence cannot reach a verdict as evidence (completion-05 §7). An FI/SC audit against the AUDIT_BRIEF detective-and-noir intent should start here. Tags: FI, SC.
- **MB:** natural season play never fights a field (`march` reaches the fold 21/21, 10/10, 4/4 and is then always refused; no natural `march` names a settlement) and `resolve_field` builds one Unit with one `infantry` Line subunit per side (system-description-05 :43-60, :256). The T04 completion proposes subunit-per-commander (CP-T04-01), `marshal`, `surrender` (both landed, WITHHELD), and asks A/B/C; CP-T04-04 and CP-T04-10 remain HELD (B10-12). Neither the cell grid nor the weapon-carry trade-off is engaged by any of these. Related ids: F-MB-14, F-MB-17, F-MB-18. Tags: MB, CHAR.
- **FA, CORE:** succession and standing. Seven of 32 built seats have no conferral basis; the King dies at tick 0 in every seed; seats vacated after two seasons 8/7/10 (`system-description-13` R-F1); `revoke` can pass only through the vacant `off_duke_valorsmark` (R-F2); `faction_q.head` is always `None` (completion-09 §6). IN-61 (succession) stopped; CR-35..37 (B10-17) are the later routes. The King-dead-at-tick-0 fact explains why thrust-layer deaths are 16/20 seat-holders. The military verbs are open to 25 of 32 seats under `remit_default` (F-FA-03). Tags: FA, CORE, CHAR.
- **WR, CORE:** exogenous motion is dark: `body_step=0`, `age_step=0.0`, `illness_rate=0.0`, `season_factor_draw=()`, `lattice_coupling=0`; `age_at_build` is not sweepable on a built world (`Person.born` set at construction); 29 of 46 registry rows have `age: null` (H-208); 0 threadwork modules load in a season (P8); the Calamity has no source in the realm (H-236). B10-18 builds the switches (`year_length`, Tensions receiver, CP-T10-04/05, `body_step=10` via REM-52 in B10-05). Related id: F-WR-05. Tags: WR, SE, CHAR.
- **CORE/PROCESS:** the thrust-layer instruments (`aperture` pooled census, `arms` generalised, `storybar --executed-only`, `harness/arc.py`) landed in B10-02 (#509) after these documents; the probe scripts here hard-code `sys.path.insert(0, "/home/user/ttrpg")` and wrap driver-instance methods, so they are scaffolds, not tests. Tags: CORE, PROCESS.

## Likely stale or superseded

- `proposals/2026-10-25-thrust-layer/reports/R09_design_verdict.md`, `R10_major_takeaways_as_first_delivered.md` and the first-delivery figures in R01-R08 (929/1,318 refused; 33% wrong-kind; "51 of 803" need; "28 of 46" case termini; "nine verbs write nothing" → thirteen; "H-156 sits in no workplan"): superseded by `02_MAJOR_TAKEAWAYS.md` §9 and the register's probes (`reports/README.md` :50-56).
- `00_THRUST_LAYER_DESIGN.md`: R3', stage `deadline`, `closing`, `successor`, `deal`, the `Slain` band and B5.1 are excluded or struck by M20/M21; the line numbers into `queries/world_q.py` have drifted; the cited `valoria_master_workplan_v9*.md` are retired.
- `proposals/2026-10-24-character-layers-capability-ambition-values-personality.md` (v1): its §5 cuts (boldness, patience, vindictiveness) overruled by Jordan 2026-10-25 / ED-IN-0304; `character-layers-v2.md` is a reconstruction of a LOST file.
- `proposals/2026-10-24-character-progression-adjudication.md`: the six-attribute roster and the accrual cut are overtaken by M2 / ED-IN-0301 (nine attributes with practice live), CR-18, CR-20.
- `proposals/2026-10-22-system-description/2026-10-22-system-description-12-reference-appendices.md` (266 KB): self-declared superseded; the tutorial grade blocks (TESTS-ONLY etc.) reflect `51d7b05`, pre-B10; `Person` thread-sensitivity field, `guard_weight`, `endings_reached` and PC-10a all landed later.
- `proposals/2026-10-21-verb-key-rows*.md` (three parts): static reading of a 46-row table; uses "key" for a verb-table row, a word the repo later retired for the Key substrate (ED-IN-0232); which of its eleven new rows exist is not established here.
- `proposals/2026-10-23-subsystem-completion/*`: "Home of v10 positions", to be deleted with a FORK row as positions land; many items are built (B10-12 CP-T04-02/-07 landed) so per-file item lists are partly historical; measurements cited from probes "not in the repository".
- `master-workplan-v10/*-build-*.md`: B10-12 is CLOSED and narrowed; B10-10 and others were deleted at close per the sequence; B10-20 exists in the directory but is not in this lane's assignment; the plan has a v11 successor (`valoria_master_workplan_v11_part3.md` cited from B10-12) [UNVERIFIED which `CURRENT.md` names].
- Toy and probe scripts: `predictions.py` = `predictions_v1.py` and `regimes.py` = `regimes_v1.py` byte-identical (`cmp`); world files for four freezes do not match their recorded hashes (`toy/README.md` :25-30); `regimes6/7/8/9.py`, `suite*.py`, `save_figs.py`, `*_out.txt` live in the directory but were not in this lane.

## Items that could change an audit finding

- **Any "X executes / X is absent" claim in a subsystem audit:** check it against the thrust-layer census (`01_MISSING_IN_CODE.md` §3 and `probes/p10_out.json`) and say which refusal rule it used. A finding built on `SeasonDriver.resolved` (aperture's older reading) undercounts by about 20%. Relevant ids: F-CHAR-05 ("four in ten resolved acts are refusals the actor could have foreseen" — the register says 76% are refused on the driver's definition, 28.7-32.2% at admission), F-CORE-17.
- **H-156 / wrong-kind formation:** the register withdrew its own design and left four live options; v10 took it as M19 (a) (`v10_part11.md:13`) [UNVERIFIED which option]. A CORE/CHAR finding recommending formation typing must say which option and must read the motion control (questions delivered, claims deposited), which no one has measured (`01` §6).
- **F-CHAR-01 (ranking does not read what an act would do) and F-DICE-14 (chooser's odds):** AQ-X1 (does expected success enter the NPC score) was "taken" in v10 M1/M3/M4 per the index (:2) [UNVERIFIED answer]; the shape of the score is a ruled Layer-1 item (`ARCHITECTURE_V2.md:508-528`), so a finding that adds a score term contradicts ruling R1 unless it rides AQ-X1.
- **F-MB-14 (individuals' attributes do not reach the battle):** corroborated at the seam (one Unit, one infantry Line subunit per side; the seam reads weights and mean stance only, `progression-adjudication` C-5), but the T04 completion's CP-T04-01 (subunit per commanding person) is the planned answer and CP-T04-10/-04 are HELD on Layer-1 asks A and C.
- **F-WR-05 (threadwork is not in the game):** P8 confirms by execution (0 modules loaded in a season); B10-15 would load it; the system-description grades say TESTS-ONLY at `51d7b05`.
- **F-FA-03 (military verbs open to clerks):** consistent with `remit_default` giving `dispatch` to 25 of 32 seats (completion-09 §6, T09 §1); A1 asks whether to restrict `declare` to the creed subject's faction head; default option one built.
- **Succession/King-dead findings:** the system-description R-F1 gives the mechanism (null-conferral seats, `off_duke_valorsmark` vacant → no `revoke`) any FA/CORE audit of IN-61 or CR-35..37 should check against current `offices.yaml` before repeating.
- **Arc/ENDINGS counts:** thrust-layer docs count 50 classified endings (DECIDER 20, crossing-forced 19, NEVER 10, ROLL 9, THRESHOLD 8) while B10-19 says 48 classified arcs; reconcile before any audit cites the class shares (relates to F-CORE-02, F-CORE-23).
