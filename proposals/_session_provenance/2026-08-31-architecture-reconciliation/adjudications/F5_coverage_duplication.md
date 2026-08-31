# F5 — ADJUDICATION: coverage, duplication, gaps, supersession

Adjudicator: Fable 5, read-only pass over `/home/user/ttrpg` at `3871043` (2026-08-31).
Evidence base: fourteen trace logs (R1–R6, PR337–PR344) + direct verification of every
high-stakes claim named below. Every `path:line` cited was either read directly this session
or is attributed to the lane that read it. `[unclear]` marks the rulings I could not ground.

---

## 0. METHOD, and what I verified myself

Read all fourteen logs in full. Then, directly against the working tree (read-only):

1. **Re-ran R5's corpus enumeration from scratch.** `find proposals -name '*.md' | xargs wc -l`,
   filter `>200`. Current tree: 205 files / 88,899 lines; 147 files >200 lines / 82,911 lines.
   **14 of those 147 are this very exercise's own trace logs**, committed at `3871043` as
   `proposals/_session_provenance/2026-08-31-architecture-reconciliation/` — excluding them
   reproduces R5's figures **byte-exact: 133 files, 75,453 lines.** R5's method is verified.
2. **Verified all named documents at their claimed line counts** (`wc -l`): `11_world_events.md` 715 ·
   `09_ambitions_and_arcs.md`+`_part2` 695+370=1,065 · `10_the_slate_and_salience.md`+`_part2`
   676+476=1,152 · `02_the_act_economy.md` 426 · `03_knowledge_telling_investigation.md` 980 ·
   `governance_ripple_substrate_v1.md` 559 · `governance_play_redesign_v1.md` 337. All exact.
3. **Quoted ED-IN-0200 and ED-IN-0201 in full** from `registers/editorial_ledger_in.jsonl` (§6 below).
   Both carry `status: open`, **`needs_jordan: false`** — a fact that changes the ruling.
4. **Grepped the citation channels myself**: `NN:LLL` key confirmed at `01_ARCHITECTURE.md:37`;
   the `108 of 123` confession confirmed verbatim, still standing, at
   `proposals/2026-08-31-ideal-v2/00_INDEX.md:10`; the ambition self-correction at
   `01_ARCHITECTURE.md:1688`; **zero** hits for `ED-IN-0200|0201` or
   `integration_master|precedent_companion` anywhere in `2026-08-31-ideal{,-v2}/`,
   `2026-08-29-valoria-from-scratch/`, `2026-08-30-fixes/`, `2026-08-30-play-space-coverage/`,
   `2026-08-31-integration/` — versus **20 files** citing them across the two greenfield suites.
5. **Resolved a live lane conflict by direct read** (R3 vs the PR344 log, on FATAL F-4): the
   fixed-point ruling exists at `01_ARCHITECTURE.md:454-466`; `02_THE_SEASON_LOOP.md:570-573`
   still carries the uncorrected claim. Both lanes were half right (§9, overturn 3).
6. **Verified supersession headers directly**: `10_SUPERSEDING.md:1-8` (supersedes #342's 17 docs +
   `00_THE_SHAPE.md`, "Read this one file"); greenfield-v2 `00_INDEX.md:2-9` (supersedes v1 only;
   itself superseded by nothing); `10_SUPERSEDING.md:27` names
   `2026-08-31-integration/09_citation_ledger.md` as its verified fact base.
7. **Verified G-26's subject resolved in the merged tree**: `07_alignment.md:706-711` — "the
   licence table is now gone" (PR #343's own edit). And G-30's subject ruled (F6, `01_ARCHITECTURE.md`
   §7). Verified `Recall` at `2026-08-18-breaking-the-recursion.md:335-347`.
8. **Read the full G-01..G-30 register** at `03_COMPENDIUM.md:707-742` and the collision register
   header at §7 (22 data rows, not the 18 two lanes reported — counted by awk).

What I did **not** do: execute anything (M1 state taken from R6's live `m1_acceptance.py --summary`
run: 0/7, NOT MET); re-read the ~20 H-priority uncited documents in full (R5's §4 mechanism
reproductions accepted after spot-verification of their five documents' existence, line counts,
and the quoted correction passages in the head).

---

## 1. ⭐ THE COVERAGE NUMBERS, RULED

**Authoritative figures, true of the working tree at `3871043`, 2026-08-31, excluding the
14 reconciliation logs this exercise itself committed:**

| metric | ruled figure | basis |
|---|---|---|
| Proposal documents >200 lines | **133** (75,453 lines) | re-measured this session, byte-exact match with R5 |
| Documents the six-file citing suite touches | **30** (24 external + 6 self) | R5's three-pass method, verified: the `NN:LLL` channel is real (`01_ARCHITECTURE.md:37`) and invisible to a filename grep |
| Uncited documents >200 lines | **103** — 77.4% by count | set difference, R5, method verified |
| Uncited by line weight | **51,111 / 75,453 = 67.7%** | R5, corpus total re-verified |
| PR #344's "108 of 123, 15 touched" | **TRUE OF ITS MOMENT, STALE NOW** | 123 ≈ 133 − ~12 `integration/` files counted before they existed (arithmetic reconciles); "15 touched" predates the self-correction section (`01_ARCHITECTURE.md` ~:1440-2180) that added the `NN:LLL` reading of 14 more #342 docs |

**Why PR #344's numbers differ:** the PR body describes the suite *before* its own correction pass
finished; the working tree has since partially closed the gap the body describes. Both numbers are
honest measurements of different states. **The defect that survives into the present:**
`proposals/2026-08-31-ideal-v2/00_INDEX.md:10` still carries "108 of 123" as if current — the head's
own confession is now a stale number in a live document, exactly the failure class this repo keeps
filing (`CLAUDE.md` §1's dated-stamp lesson).

**The number that matters most — how much architectural content the head has actually accounted
for.** By line weight the head touches **32.3% of the >200-line proposals corpus**. But `proposals/`
is the *narrowest* denominator. Add what the sweeps measured outside it and the honest statement is:

- `research/`: **0 of 2 master documents cited** (~1,830 + multi-part companion lines; grep verified,
  zero hits) — including P4 and U-3/U-4, the direct ancestors of the head's own Person model (§7).
- `registers/`: **0 of the 2 governing Jordan rulings cited** (ED-IN-0200, ED-IN-0201) — despite the
  same design line having filed one of them (§6).
- `systems/`: the head cites `engine/substrate/keys.py` for **id/uniqueness/cycle precedents only**
  (`03_COMPENDIUM.md` §12, 8 rows; `01_ARCHITECTURE.md` §2.2); it never reconciles its
  Event/witness/Claim/Query cluster against `key_substrate_v30.md` §4's CANONICAL
  `compute_observers`/`memory_query`/`compute_salience`, which R2 found to be near-exact,
  **already-executable** overlaps.

**Ruling: the current head is built on roughly one third of the proposals corpus and on essentially
none of the architecture-bearing content outside `proposals/` — call it under 25% of the corpus's
architectural content overall, and the unread remainder includes the only part that executes.**
That last clause is the load-bearing one: the single largest unaccounted-for artifact is CANONICAL
and runs (`engine/substrate/keys.py`, 601 LOC, 8 invariants, replay-deterministic), while everything
the head *did* read is PROPOSED prose.

---

## 2. ⭐ THE SUPERSESSION MAP

Governing facts first, because they order everything below. (1) **Nothing under `proposals/` is
canon.** Every design PR #337–#344 was explicitly HELD BACK from ratification-on-merge; the live
canonical surface is still `CURRENT.md`'s v40 roster — `systems/` heads + `engine/` code. The
proposal line supersedes only *within itself*. (2) Under §0.05, **the only mechanisms in this table
are the code rows.** Status below is my ruling on *what a reader should treat as the current
statement of its subject*, not on ratification.

### Tier 0 — canon and code (LIVE; no proposal supersedes any of these)

| document | lines | subject | status | what survives |
|---|---|---|---|---|
| `engine/substrate/keys.py` + `systems/_architecture/key_substrate_v30.md` | 601 py / (CANONICAL PP-687) | Key/Event substrate, observers, memory, salience | **LIVE — the only executing analogue of the head's Event cluster** | everything; the head must build on it or explicitly replace it (§3 row 1) |
| `systems/_architecture/holonic_container_doctrine_v1.md` | — | code-module scale ladder | LIVE (CANONICAL, ED-1083/1094) | module-shape uniformity; **not** an entity-containment claim — do not read it against `Rung` (R2 §4) |
| `systems/settlements/scale_hierarchy_v1.md` | — | geographic/faction containment | LIVE (RATIFIED 2026-07-13) | Province-existence-conditional + faction-holds-people = the ratified precedent `Rung`-as-edge generalizes |
| `systems/factions/faction_politics_v30.md` (PP-660) + 4 co-docs | — | rank ladders, offices per faction | LIVE (CANONICAL) | the office/Standing content `Office`/`Tenure(hold)` must reconcile against |
| `systems/fieldwork/investigation_systems_v30.md`, `fieldwork_v30.md` | — | investigation | LIVE (CANONICAL/DESIGN) | six-act investigation agrees with catalogue and doc 03 (three-way convergence) |
| `engine/autoload/dice_engine.py` (`degree_from_net`, TN7 ED-IN-0196), `engine_clock.py`, `game_state.py` | — | resolver, tick, world | LIVE (code) | TN7-immutable; 3-phase tick the six-step loop must map onto; `World` composition |
| `references/module_contracts.yaml` (27 modules) · `key_types.json` (55) · `descriptor_registry.yaml` | — | the three flat registries | LIVE, and the subject of ED-IN-0200 | 9 `doc: null`, 11 [ASSUMPTION] resolvers — the port's real contract surface |
| `systems/overview/clock_registry_v30.md`, `player_agency_v30.md`, `narrative_engine_design_v2_churn.md` | — | clocks; Scene Slate; Light Function | LIVE (CANONICAL/RATIFIED) | the ratified salience/attention ancestors `10_the_slate_and_salience.md` extends and the head never read |

### Tier 1 — the #337–#344 proposal chain (all PROPOSED; internal supersessions explicit)

| document | lines | subject | status | what survives |
|---|---|---|---|---|
| `proposals/2026-08-31-ideal-v2/01_ARCHITECTURE.md` | 2,186 | primitives + refusals (4 carriers, Tenure, StateChange, Query, partition) | **LIVE HEAD** | the whole document; supersedes only the v2 synthesis brief |
| `…-v2/02_THE_SEASON_LOOP.md` | 1,205 | 6 steps / 4 barriers / 4 write classes | **LIVE HEAD** — and per its own §0 it *is* the missing `engine_clock` contract | all; ⚠ carries F-4's uncorrected order-independence claim at :570-573 (§9.3) |
| `…-v2/03_COMPENDIUM.md` | 949 | the register (identity, types, queries, collisions, gaps) | **LIVE HEAD** | all; ⚠ two register rows stale against its own suite/tree (G-26, G-30 — §4) |
| `…-v2/04_GODOT_IMPLEMENTABILITY.md` | 941 | port audit (4 FATAL / 16 MAJOR) | **LIVE HEAD** | all; three of four FATALs already folded into 01/03 |
| `proposals/2026-08-31-ideal/10_SUPERSEDING.md` | 2,017 | the enlarged from-scratch design | **LIVE** — source of truth for everything `01_ARCHITECTURE.md` §10's 28 departures do not override | its own header supersedes #342 + THE_SHAPE |
| `proposals/2026-08-31-ideal/00_THE_SHAPE.md` | 995 | earlier draft | **SUPERSEDED BY `10_SUPERSEDING.md`** (its own §0.1) | history only |
| `proposals/2026-08-31-ideal/20_FABLE5_ADVERSARIAL_REVIEW.md` | 1,823 | corrected review of SUP | REFERENCE (findings absorbed) | the correction provenance; `REV:772-778`'s leaders-comparator proposal (G-04) |
| `proposals/2026-08-29-valoria-from-scratch/` (17 docs) | ~9,600 | the from-scratch suite | **SUPERSEDED BY `10_SUPERSEDING.md` in name — with one load-bearing exception**: `03_knowledge_telling_investigation.md` (980) is in practice the LIVE owner of the knowledge layer — the head cites it at line level ~60+ times post-correction (`NN:LLL`, doc 03 dominant in my grep) | doc 03 §§1-6 fully; §§7-9, §12 (correspondence filtering, setting's-own-epistemics, worked trace) still unabsorbed; `15_adjudications.md`/`16_ners_audit.md` as ruling records |
| `proposals/2026-08-31-integration/` (12+ docs) | ~4,800 | the parallel Part-2/3 synthesis (#343) | **PARTIALLY ABSORBED**: `09_citation_ledger.md` is SUP's declared fact base (`10_SUPERSEDING.md:27`); the synthesis products `04/05/11_INTEGRATED.md` are cited by nothing downstream | harvest pass owed (§8 item 8); after it, ARCHIVE |
| `proposals/2026-08-30-fixes/01…05` | 445–573 | the five D-fixes | **02 = absorbed by convergence** (D-2, disclosed); **01 = partially struck** (Part-3 reconciliation; EDIT 2 marks→all-referents survives); **03/04/05 = LIVE-UNABSORBED** — formulas and dispositions the head does not contain | need(commitment)/need(exposure); Relational-at-Settlement + councillor venues; 19 blocked-core dispositions |
| `proposals/2026-08-30-play-space-coverage/` (9 docs) | ~5,700 | 56-probe evidence + `09_GAP_REPORT.md` D-1..D-10 | LIVE EVIDENCE — the design's only measured instrument; only D-2 absorbed | D-3..D-5, D-7, D-9, D-10 diagnoses |
| `proposals/2026-08-30-arc-reachability/` (5 docs) | ~3,400 | 83-arc sweep | LIVE EVIDENCE | the world-substrate hole (3-route convergence) — the largest gap the head never filed (§4 ADD-1) |
| `proposals/2026-08-29-greenfield-systems-suite-v2/` (20 docs) | ~11,900 | Entity/Tag/Post/Gauge substrate + 8 systems | **LIVE-PARALLEL — superseded by NOTHING** (own header: supersedes v1 only). The head reads its 09/10/11 post-correction and ignores its substrate | 01 (four primitives + write rule), 03 (world population), 04 (personnel), 05/06 (faction actions/mgmt), 07/08 (places/settlements), 11 (world events), 13 (build order) |
| `proposals/2026-08-28-greenfield-systems-suite/` (11 docs) | ~3,800 | v1 | **SUPERSEDED BY v2** (`ARCHIVED.md` + banners) | ARCHIVED.md's list of what survived the critique |
| `proposals/2026-08-29-fable5-throughline-critique/` (6 docs) | 1,334 | T1–T9 critique of v2 | REFERENCE — consumed by #342's throughlines | the X-1..X-8 cross-register; "no personal-scale actor layer" finding |
| `research/valoria_systems_integration_master_v1{,_part2-4}.md` | ~1,830 | 338-thing census; P1–P4 | **LIVE REFERENCE (FILED), UNCITED ANCESTOR** | F1–F10; P4 (`_part4.md:619`); the synergy matrix; F10's attribution discipline |
| `research/valoria_game_precedent_companion_v1*` (8 parts) | large | precedent; U-1..U-4; 24 imports | **LIVE REFERENCE, UNCITED ANCESTOR** | U-1 disclosure contract (free, first move); U-3; **U-4's M&B warning — the sharpest uncited fact** |
| `research/cross_scale_action_catalogue_v1.md` | ~900 | the closed action census | LIVE REFERENCE | the build-status table; six investigation acts (:610-619) confirming doc 03 row-for-row |

### Tier 2 — older proposals: live, uncontradicted, unread by the head

| document | lines | subject | status | what survives |
|---|---|---|---|---|
| `2026-08-18-fieldwork-architecture-and-nonadversarial-play.md` | 1,032 | FI architecture, §13 ratified Jordan rulings | **LIVE — carries RATIFIED rulings** ("scripting hooks allowed; scripting arcs is not") the head inherits only secondhand through doc 09 | all of §13; GAP-A/GAP-B (`Key.visibility` written-never-read) |
| `2026-08-18-epistemic-propositions-and-provenance.md` | 265 | P1–P5, five RULED Jordan calls | **LIVE — RULED** | all five; the head's O-A5 dependency is secondhand |
| `2026-08-18-breaking-the-recursion.md` | 852 | recursion diagnosis; **§4.5: the tenth attribute is `Recall`** | LIVE (§4.5 verified this session at :335-347; 10 named attributes shipped in `CharacterCreationManager.gd:146-151`) | §4.5 closes a CLAUDE.md-flagged open item (§10, item closed-by-precedent) |
| `2026-08-15-character-and-faction-stats-and-progression.md` | 1,676 | stat census from running code | LIVE REFERENCE | the measured stat surface any Person.capability must bind to |
| `canonical_nomenclature_v1.md` | 342 | dotted-ID naming plan, Phase 0 unruled | LIVE, unexecuted | Axis C for quantities/entities; **complementary to, not subsumed by, the head's §7 register** (R5 §6: different collision classes) |
| `grounded_event_card_deck_v1.md` | 335 | 58 event cards bound to the ripple substrate | LIVE CONTENT — the authored deck the head's MATTER events could ingest | all 58 cards |
| `systems/_architecture/governance_ripple_substrate_v1.md` | 559 | the event→standing loop, 5 primitives | **REFERENCE/ANCESTOR** — PROPOSED since 2026-07-11, never ratified, direction superseded by three later event-design generations; content uncontradicted | the primitive discipline ("a read/write dependency, never a thematic resemblance") — the same rule the head's Query/StateChange doctrine re-derives; the self-graded AT-RISK SC hook (6.2) survives as a real gap |
| `systems/settlements/governance_play_redesign_v1.md` | 337 | governor verbs, Pi deck, NPC ambition engine, Ledger tags | **REFERENCE/ANCESTOR** — same disposition; its own build-gate (settlement registry) is met and its status line never followed (R2 §11.3) | Part 3's NPC dossier schema (richer than the head's bare `choose`); the 5 Ledger tag families (built, INERT, zero writers — F3); the verb table as `choose` prior art |
| `2026-08-25-throughlines-and-precedent/` (8 docs) | ~4,300 | prior throughline corpus | REFERENCE — ancestors of the root-cause diagnosis | 04_ch1 "the world has no people" (root cause E's earliest statement) |
| `2026-08-23-*` vocabulary suites + MASTER rulings | ~1,800 | earlier vocab collisions | **SUPERSEDED in content** by `canonical_nomenclature_v1.md` + the head's §7 register | history |
| `2026-08-18/20/21/24` process plans (culling, execution-order, error-regions, return-to-game) | ~2,900 | repo process | PROCESS — live pointer is execution-order §3 per `HANDOFF.md` (S7 next) | not design |
| `valoria_fork_plan_of_record_v1.md` | 522 | repo fork plan | REFERENCE, partly superseded by later tree state | direction only |

### Tier 3 — godot/

| document | status | note |
|---|---|---|
| `godot/godot_conversion_strategy_v1.md` | LIVE-BUT-STALE (PROPOSED 2026-06-10, never updated) | still the governing port spec; its Part VIII register (8 open, incl. #5 autoload) is live; its `STRAT:75-77` resolver table **contradicts the live registry** (`personal_combat` = `d_sigma` now, R3 §9) and `STRAT:41`'s "4.6 pin" cites a file that no longer exists on disk (R3 §5.2) |
| `godot/skeleton/` (8 .gd + .tres) | NON-COMPILING ILLUSTRATION | extends `BaseEngine`/`EngineModule` defined nowhere; carries the anti-patterns the head's port audit indicts (`strike_module.gd:67` shared re-seeded RNG; `wound_module.gd:55` writes its own declared-non-writable field — R3's new finding) |
| `godot_architecture_specification.md` + 4 2026-04-18 docs | STALE REFERENCE / ⚠ STALE banners | do not implement from |

**How to use this table:** to write the single authoritative suite, read the LIVE HEAD (ideal-v2
four documents + SUP for non-departed content + doc 03 for the knowledge layer), pull the
LIVE-UNABSORBED rows (fixes 03/04/05, GAP_REPORT, arc synthesis, greenfield-v2's substrate and
population/personnel docs, the two research masters, the two 2026-08-18 ruling docs), and treat
everything marked SUPERSEDED/REFERENCE as history. Tier 0 is what the suite must reconcile against,
not what it replaces.

---

## 3. ⭐ THE DUPLICATION REGISTER, AUTHORITATIVE

Merged from R2 §7, R5 §5, R6 §9, R4 §11, PR340/342/343/344 logs; de-duplicated; ranked by
architectural weight. **Independent convergence** = same answer reached from different routes
without reading each other (the strongest evidence in the corpus, per §10's
rank-by-independent-rediscovery). **Re-invention** = the earlier design was simply not read.

| # | mechanism | every place it is designed | best version + why | verdict | what to do |
|---|---|---|---|---|---|
| 1 | **Typed event/state-change channel with provenance** | `key_substrate_v30.md` §1-5 + `engine/substrate/keys.py:126-601` (CANONICAL, EXECUTABLE, 8 invariants, replay hash) · ripple substrate's 5-primitive loop (`governance_ripple_substrate_v1.md:379-398`) · head's `StateChange`/`Event` (`01_ARCHITECTURE.md` §2.4) | **keys.py for the spine** — it runs, is hash-verified, and the head's own §12 cites it as precedent; **the head for the semantics** the substrate lacks (mint/alter/efface modes, Act/Event driver partition — genuinely new, R2 §8) | partial re-invention + genuine refinement: the head cites keys.py for id discipline only, never reconciles its Event against the Key | the suite declares: Event = a Key-shaped row; `changes[]`/driver/mode are new columns on the substrate's contract, not a second log |
| 2 | **Per-observer witnessing** | `key_substrate_v30.md` 4.1-4.2 (`compute_observers` → per-observer interpretation/memory, CANONICAL) · doc 03 §2 (two-stage registration/construal) · head's `witness:(Person,Event)->Claim[]` | **doc 03 + the head's signature** — construal divergence and root-token minting are richer than the substrate's fan-out; but the substrate already owns reach/visibility | re-invention of the fan-out; refinement of the semantics | fan-out (WITNESS step 1) = `compute_observers`; step 2's claim minting is the new layer |
| 3 | **Query / never-stored recomputation** | `key_substrate_v30.md` 4.4 `memory_query()`+`MemoryIndex` (CANONICAL, with perf targets) · `canon_buckets.py`/`descriptors.py` (practiced, unnamed) · head's 23-row Query catalogue | **the head's catalogue** — the World-first-parameter enforcement (M-2) is the best single idea in the port audit; `memory_query` is its executable precedent | re-invention of the category; the `Derived`→`Query` rename is **necessary and repo-verified** (R4 §3 — three live registries use `Derived` for the opposite) | keep `Query`; cite `memory_query()` as precedent row 9 |
| 4 | **Person-first iteration ("a faction acts because someone in it acts")** | integration master **P4** (`research/…_part4.md:619-745`, 2026-08-27, with NERS math) · precedent companion **U-3** (person as relationship ledger) · head's Person/choose/D-2 | **the head** — more complete; but P4's NERS repair ("the roster buys action-count, not pool size") *is* D-2's establishment reading, reached independently 4 days earlier | **independent convergence at the mechanism level** (unread ancestor, identical repair) — the bankable kind | cite P4/U-3; import U-4's warning (row 15) |
| 5 | **The act economy** | `governance_play_redesign_v1.md` 1.1 (`AP = 2+FacilityTier`, zero readers) · greenfield "budget buys actions, never modifiers" · #342's one-act rule (`09:33`) vs `14:562`'s ten-act season (the contradiction) · **`02_the_act_economy.md` Reading C (56-probe discriminator)** · head's D-2 | **Reading C** — the only one with a measurement; head's D-2 states the identical rule | **exact independent convergence** (fixes/02 ↔ ideal-v2 D-2; disclosed by the head itself) — the cleanest in the corpus | adopt; cite fixes/02 as the evidence base; the three rival faction economies (integration master F6) close to this one |
| 6 | **Actorless/exogenous world events** | redesign Part 2 (Pi-gated deck, 2026-06-22) · `grounded_event_card_deck_v1.md` (58 cards, 07-11) · **`11_world_events.md`** (registry rows, rate-bounded, `we.altonian_pressure`, 08-29) · head's F5 reversal + MATTER events | **`11_world_events.md`** for mechanism (zero new modules, three rate bounds, Tag-not-scheduled-Key persistence); head for the partition that licenses it | re-invention, self-corrected in the tree (`01_ARCHITECTURE.md:1632-1637`); residue unabsorbed: rate-bound proofs, `institutional_pressure`, the `informational` contract | fold 11's registry schema into MATTER step 6; check its rate bounds against G-07 |
| 7 | **Ambition's carrier** | redesign Part 3 (NPC dossier `ambition{goal,method,timeline,progress}` + trajectory, 06-22) · **`09_ambitions_and_arcs.md`** (Ambition Tag, derived progress, §6.4 mass actor, 08-29) · head's F6 discussion | **09** — derived-at-read progress + obstruction-needs-no-verb is the sharpest design; redesign's trajectory re-planning is richer on the "what if blocked" side | re-invention, self-corrected (`01_ARCHITECTURE.md:1688`); §6.4's auto-declaring `rising` (the suite's only mass actor) + tag-age grammar still unabsorbed | absorb §6.4 and tag-age; reconcile with redesign's trajectory |
| 8 | **Slate / salience / what reaches a decider** | `key_substrate_v30.md` 4.5 `compute_salience()` (CANONICAL) · `player_agency_v30.md` Scene Slate (CANONICAL) · Light Function (`narrative_engine_design_v2_churn.md` §4, RATIFIED) · **`10_the_slate_and_salience.md`+part2** (candidate contract C-1..C-6, bounded+monotone truncation proof, cast/depth severance) · doc 03 salience · head's §4.1 view assembly | **10** — it supplies the definition the RATIFIED Light Function presupposes and never states; the head's view assembly covers the person side only | acknowledged-unread and *left* unread (the head says so at `01_ARCHITECTURE.md:1805`) — the least-closed of the five confessions | read 10 before writing the suite's surfacing layer; its candidate contract likely answers G-01's `q` producer |
| 9 | **Field investigation** | `investigation_systems_v30.md` (CANONICAL) · catalogue `:610-619` (six acts) · **doc 03 §6** (six acts + obstacle owner + counter-investigation) · head's invented `investigate` → corrected to the six | **doc 03**, which agrees row-for-row with the catalogue (independent convergence between those two) | re-invention (the invented verb), fully corrected (`03_COMPENDIUM.md:353`, `02:912`) | done; keep `investigate` in the twelve-act table explicitly labelled a header over six acts |
| 10 | **Epistemics/belief/memory** | `beliefs.py:50` `Belief` (durable, mutable) · `key_substrate_v30.md` 4.3-4.4 NPC Memory (indexed) · doc 03 Claim ledger · head §2.4 | **doc 03/head** — but the corpus now holds THREE unreconciled per-actor knowledge stores, and the pre-existing Belief-vs-Memory duplication (R2 §7) is inherited, not addressed | re-invention + inherited internal duplication | one ruling in the suite: Claim ledger subsumes Belief; Memory's index is its implementation precedent |
| 11 | **Tenure / who-holds-what** | five scattered live mechanisms: `governor_id` FK · faction-holds-people prose (`scale_hierarchy_v1.md` 5.1) · `Compact` Ledger tag · `TreatyRecord` (`treaty.py:62`) · Standing ladders (`faction_politics_v30.md`) — vs the head's one edge, 7 kinds, cardinality | **the head** — R2's verdict stands: "the proposal's real contribution is the unification, not the primitive" | **genuine refinement** (the closest thing to genuinely new in the whole exercise, with row 12) | keep; map the five old mechanisms to kinds explicitly in the suite |
| 12 | **Containment as edge (Rung)** | `scale_hierarchy_v1.md` §2 (Province existence-conditional) + §5.1 (factions hold people) — case-by-case, RATIFIED · head's `Rung`+`contain`/`hold` | **the head** — a generalization of ratified precedent, not novelty (R2 §4) | genuine refinement of ratified case law | cite scale_hierarchy as the precedent; resolves R2's escalation 1 (the doctrine/hierarchy "tension" is two different axes — module shape vs entity relation) |
| 13 | **The season loop** | `engine_clock.py` 3-phase (LIVE code, ED-IN-0199) · greenfield accounting phases · head's 6-step/4-barrier | **the head as the contract, the code as the floor** — `02_THE_SEASON_LOOP.md` §0 *is* the missing `engine_clock` canon (O-2, `module_contracts.yaml:1128-1136` `doc: null`) | refinement — highest-leverage connection in the corpus, and **neither surface points at the other** | the one-line editorial action: re-point `engine_clock`'s gap_notes at 02 (ED-1051's candidate) |
| 14 | **Collision/naming registers** | `canonical_nomenclature_v1.md` (Axis C, quantities/entities, validated with counts) · head's §7 register (carrier/field words, 22 rows) · greenfield O-2 (edge enum ceded to PP-724) | both — **different collision classes; neither subsumes the other** (R5 §6: grep-noise vs class-name/field-reuse) | complementary, not duplicated | apply both; nomenclature Phase 0 rulings still owed |
| 15 | **Cross-scale coupling as the differentiator** | precedent companion **U-4** (Valoria sits exactly where M&B sits — one reachable crossing, default-off bridge) · head's seam-at-`resolve` §8 | U-4 is the *warning*; the head's nested-loop seam is the *answer* — but the head never confronts whether new object names actually close the isolation (R6 §9) | uncited ancestor carrying the head's own hardest test | write U-4's test into the suite's acceptance criteria |
| 16 | **Whole-effort duplication: two syntheses of the same evidence** | `2026-08-31-integration/04,05,11_INTEGRATED.md` vs ideal/ideal-v2 | ideal-v2 (two more adversarial rounds, more corrections) | **qualified**, not the clean fork R5 called it: SUP's fact base *is* integration's citation ledger (`10_SUPERSEDING.md:27`); what is genuinely uncross-cited is the synthesis products | one harvest pass over 04/05/11, then archive them (§8 item 8) |
| 17 | **Coverage measurement itself** | PR #344 body (108/123) vs R5 (103/133) vs `00_INDEX.md:10` (stale) | R5's three-channel method | measurement duplication with a stale survivor in the live head | fix `00_INDEX.md:10`'s figure when the suite is written |

---

## 4. ⭐ THE GAP REGISTER, AUTHORITATIVE

Re-ruling of `03_COMPENDIUM.md:713-742` (G-01..G-30), then the additions the sweeps found.
Statuses: **open** · **closed-by-uncited-doc** (the answer exists on disk, unread) ·
**closed-by-merged-edit** · **closed-by-ruling** · **not-a-gap** · **RESERVED**.

| id | what is missing | who it blocks | closed by | ruled status |
|---|---|---|---|---|
| G-01 | `q`'s producer for view assembly | every retrieval | likely `10_the_slate_and_salience.md`'s candidate contract (unread); LOOP §4.1's default (highest unmet need) is defensible | **open — read 10 first**; the default stands meanwhile |
| G-02 | ~~`relevance(c,q)` undefined~~ | — | `03:342-344` | **CLOSED** (confirmed) |
| G-03 | `Profile`'s field list | faction reads | arithmetic at `07_alignment.md:217-231`; only the record shape open | **open, narrowed** (confirmed) |
| G-04 | `leaders`' comparator | deposition | `REV:772-778` proposes commitment-degree × backing-raisable | **close by architecture (§0 test 5)**: faction = Proposition + commit edges, so the comparator must be commitment-derived; adopt REV's proposal, record the reasoning. Not Jordan's |
| G-05 | channel-store location | minted persons' plausible past | nothing — three refusals block every candidate | **open** (genuinely; engineering, not Jordan) |
| G-06 | construal-spread rule (row 4) | cohort witnessing | same cluster as G-05 | **open** |
| G-07 | `season_factor(territory)` distribution | yield, every season | candidate: `11_world_events.md`'s rate/hazard machinery (flagged by R5, unverified); otherwise one authored line in the `(3+d10)/8.5` form | **open — check 11, then author**. Not Jordan |
| G-08 | ~~predicate vocabulary~~ | — | `03:66-79`, 14 forms | **CLOSED** (confirmed) |
| G-09 | Venue's 8 once-occurring params | the sitting | authoring | **open** |
| G-10 | `standard` in advancement/demotion gates | both gates | nothing found anywhere (KEYS_AUDIT D.3) | **open** |
| G-11 | `Act.payload` type | verbs | engineering | **open** |
| G-12 | `Event`'s record | witness | fields; substrate `Key` is the precedent shape | **open — cheap**: derive from `keys.py:126-158` |
| G-13 | `World`'s record | resolve; all 14 refusals | O-6: first thing a typed port declares | **open — first port task** |
| G-14 | `Rung.matter` structure | carrier layer (M-14) | typed sub-records | **open** |
| G-15 | envelope age-band boundaries | births/deaths/draws | candidate: greenfield-v2 `03_world_population.md` (638 lines, uncited — "who exists, how many") | **open — likely closed-by-uncited-doc; verify** |
| G-16 | channel latency values | every telling | candidate: greenfield-v2 `01_substrate_primitives_part2.md` (edges, disclosure, the herald) | **open — check before authoring** |
| G-17 | ~~dead person declares an act~~ | — | MATTER precedes DELIBERATE | **CLOSED** (ordering argument verified sound) |
| G-18 | upkeep magnitude; establishment size; first author | office economy | candidate: greenfield-v2 `04_personnel_management.md` (747 lines, uncited) | **open — likely closed-by-uncited-doc; verify** |
| G-19 | the empty judging set | F3's falsifier | a floor | **open** (engineering) |
| G-20 | Coherence-0 officeholder | frozen seat | vacancy-by-absence reaching them | **open** (engineering) |
| G-21 | row-11 `exclude` limb widened by `efface` | razing | inherited, no bound invented | **open, inherited** |
| G-22 | the `R≤1→0` branch | every trivial attempt | a ruling + a balance instrument that does not exist for this design | **open** — do not delete without a control (§0.1 pt 4) |
| G-23 | `Office.conferral` cycles silently exclude | office clusters | the substrate's append-only pattern (`keys.py:389-392`) named as the fix | **open — cheap, precedent named** |
| G-24 | root-uniqueness | `sovereign_fraction` | `SUP:475-478` rules root-plurality political | **ruled, not closed** (confirmed) |
| G-25 | two incompatible Coherence band tables | K penalty ladder | pick the table canon's derived-stats doc backs (`ABS:222` vs `:223`) | **close by precedent** — a table choice, not a fork; record which |
| G-26 | commitment ladder's licence column "in two contradictory states" | degree entitlements | **PR #343 already deleted the licence column** — `07_alignment.md:706-711`, verified: "the licence table is now gone" | **CLOSED-BY-MERGED-EDIT** — the register missed its own tree |
| G-27 | the exchange form | rescue-by-market | an object; gift constructs, market asserted | **open** |
| G-28 | coercion coin arithmetic → typed stores | wages, arrears | unwritten work | **open** |
| G-29 | L-4, the playable-seat list | every R-line | the architecture itself: every person can act; the postless season is tested and right; play = choosing a person | **close by architecture** — no privileged seat list is required; scenario authoring comes later. Not Jordan's |
| G-30 | is the world dying or misunderstood? | campaign feel | **Jordan RULED F6 this same suite** — "the world is in flux"; `wear` is the mechanism (`01_ARCHITECTURE.md` §7) | **CLOSED-BY-RULING; the RESERVED tag is stale against its own sibling document.** The live residue is the wear:restoration *ratio* — a measurement item, not a fork |

**Net on the design's own register: 30 filed → 5 CLOSED (G-02, G-08, G-17 already; G-26, G-30 by
this ruling), 2 close-by-architecture (G-04, G-29), 1 close-by-precedent (G-25), 3 likely
closed-by-uncited-doc pending verification (G-15, G-16, G-18), 19 genuinely open — none of the 19
needing Jordan.**

**Gaps the sweeps found that the design never filed (ADD rows):**

| id | what is missing | who it blocks | closed by | status |
|---|---|---|---|---|
| ADD-1 | **the world-substrate object** (Thread/Mending-Stability state a person's act can degrade) | arcs 5, 22, 27, 48; the design "PRICES an operation it does not define" (Coherence cost with no operation); "the world is not dying, only misunderstood" — now contradicting Jordan's F6 flux ruling, which needs matter that can decay *metaphysically* too | nothing — confirmed an OMISSION by 3 independent arc lanes (`04_SYNTHESIS.md` §2); named their #1 next item; the head's G-register has **no row for it** | **open — the largest unfiled gap in the corpus** |
| ADD-2 | `hold` collision, 5th sense: mass-battle stance (`config.py:269` `STANCE_SPEED_MOD['hold']: -99`, live code) | Tenure(hold) ↔ MB interop | one disambiguation row | **open — add to §7 register** (R4's highest-value find) |
| ADD-3 | `Presence` (legacy attribute alias, `descriptor_registry.yaml:58`) and `View` (engine-atlas lens sense) missing from §7 | formula-cited legacy name; doc vocabulary | two rows | **open — cheap** |
| ADD-4 | **F-4 not propagated**: `02_THE_SEASON_LOOP.md:570-573` + §10 still claim order-independence-under-batching; the fixed-point ruling lives only at `01_ARCHITECTURE.md:454-466` | any implementer working from 02 alone | copying five lines from 01 | **open — my own finding, verified both files this session** |
| ADD-5 | whether the twelve-act table (`03:781-783`) is exhaustive or faction/settlement-scoped — PC, SC, threadwork, MB absent | any implementer of the act layer | one scope sentence | **open** (R6 §10) |
| ADD-6 | save-model conflict: `STRAT:19` (initial-conditions+log replay) vs head (snapshot; log never the load path) — filed as M-12 in 04, absent from the G-register | whichever side builds first | one ruling; recommendation exists (snapshot; log for provenance) | **open — escalates, bundled (§10.2)** |
| ADD-7 | the autoload/state-owner ruling (`STRAT:213`, open since 06-10) — now load-bearing on F-1 | the whole port's purity guarantee; live `valoria-game` `Meta` does the opposite | one ruling | **open — escalates, bundled (§10.2)** |
| ADD-8 | ED-IN-0200/0201 uncited by the head | ledger hygiene; the suite's charter | two citation lines + §6's reconciliation | **open — session work** |
| ADD-9 | the four structural tests have no harness (no code, no board row — R6 §4) | "done means it runs" for the whole design | new objects first; `test_engine_does_not_import_systems.py` / `test_key_substrate.py` / `test_morale_write_sweep.py` are the named templates | **open** |
| ADD-10 | the tenth attribute unnamed in the head's vocabulary | Person.capability binding; Godot fields stay unbound per the registry's own banner | `2026-08-18-breaking-the-recursion.md:335-347`: **`Recall`**, shipped in `CharacterCreationManager.gd:146-151` | **closed-by-uncited-doc + precedent (shipped code)** — record it; Jordan can veto on merge (§10.3) |
| ADD-11 | contest-nesting depth bound (M-7 — GDScript overflow is a crash; the Python substrate's caps are required constructor args) | the deferred-subsystem seam | an explicit depth parameter | **open — cheap** |
| ADD-12 | D-3/D-4/D-5/D-7/D-9/D-10 content unabsorbed (formulas exist in fixes/03, fixes/04; diagnoses in `09_GAP_REPORT.md`) | needs, settlement membership, councillor venues, petition pricing, vacancy, material economy | the fixes documents themselves | **closed-by-uncited-doc — absorb** |
| ADD-13 | `engine_clock` contract not re-pointed at 02 (ED-1051 residue; O-2) | the port's first module | one gap_notes edit | **open — one-line session work** |
| ADD-14 | `resolve`-table three-way disagreement: `STRAT:75-77` vs live `module_contracts.yaml` (`personal_combat: d_sigma`) vs head's "adds no resolver" (O-5) | porting any deferred subsystem | a reconciliation note | **open** |

---

## 5. THE SEVEN FORKS AND D-2

The head claims all seven answered (`01_ARCHITECTURE.md` §7). Re-ruled against the corpus:

| fork | design's answer | already answered elsewhere? | my ruling |
|---|---|---|---|
| **D-2** act economy | RULED (Jordan, this session): one act per person or cohort, universally; office throughput = the establishment's acts | **YES — `2026-08-30-fixes/02_the_act_economy.md` (426 lines), Reading C, chosen on a 56-probe discriminator** ("the design prices remit and forgets establishment"); identical conclusion, identical formula shape (`acts = 1 + \|establishment members whose choose served the office\|`) | **STANDS — exact independent convergence, correctly disclosed by the head itself** (`01_ARCHITECTURE.md` §7 D-2 names the file unread-but-matching). The suite should cite fixes/02 as the evidence and keep Jordan's ruling as the licence. Residue D-16 (cohort self-individuation exploit) **dissolves**: CENSUS's individuation triggers are RULED exhaustive and demand-driven ("may not create a person for whom nothing asked", `02:1199`-region §7.5) — a person cannot vote themselves a split |
| **F1** conferral basis | DISSOLVES: per-office | partially — the arc synthesis §3 adjudicated office-rooted from 4 independent fiction-side demands, then **withdrew it** as "not an audit's call" (SUP §4.5/§16) | **DISSOLUTION STANDS for the *basis* field** (nothing requires uniformity). The *Church rooting* question underneath is D-6/D-7 and stays live — §10.1 |
| **F2** `stores` denominator | DISSOLVES into `MatterKind` type parameter | SUP §16 reserved it; no other corpus answer | **STANDS** — a real dissolution (both branches true of different kinds); G-27/G-28 are its residue |
| **F3** S19 rootless vacancy | DISSOLVES: conferral rule may name the office's own judging set | S19 flagged unrepaired by SUP §15.16 | **STANDS**, with G-19 (empty judging set) as honest residue — engineering |
| **F4** Coherence-0 ontology | NOT A FORK — de-individuation by another cause | SUP §16 carried it as two incompatible readings | **STANDS** — the de-individuation predicate genuinely absorbs it; residue G-20/G-25 are engineering |
| **F5** off-board polities | REVERSED — event source, not simulated realm | **YES — `11_world_events.md` ships the entire mechanism including `we.altonian_pressure` by name**, rate-bounded, registry-ready (verified 715 lines) | **REVERSAL STANDS, credit corrected**: the head's own tree text says it — "a re-derivation, not an invention … a pointer to `11_world_events.md`" (`01_ARCHITECTURE.md:1632-1637`). The suite adopts 11's row schema, not a re-derivation |
| **F6** dying or misunderstood | RULED BY JORDAN: neither — "the world is in flux"; direction is an output; one constant `wear` | No prior answer; the fork's two poles are both in the corpus (arc synthesis: "misunderstood"; Jordan's spec: flux) | **STANDS — a genuine fresh Jordan ruling.** Two consequences this adjudication adds: (a) `03_COMPENDIUM.md` G-30's RESERVED tag is stale against it (§4); (b) the ruling makes ADD-1 (the world-substrate object) *more* urgent — a flux world needs metaphysical matter that can wear, and the arc sweep proved that object absent |

**Count check:** the design's "five dissolve, two ruled, one reversed" tally is loose — the true
disposition is 1 RULED-with-convergence (D-2), 3 DISSOLVE (F1, F2, F3), 1 NOT-A-FORK (F4),
1 REVERSED-already-designed (F5), 1 RULED-fresh (F6). All seven survive scrutiny; two of the seven
(D-2, F5) were already answered in uncited documents, and the head's own corrections say so.

---

## 6. ⭐ ED-IN-0200 AND ED-IN-0201

**ED-IN-0200** (2026-08-27, `registers/editorial_ledger_in.jsonl`, `status: open`,
**`needs_jordan: false`**, confidence high), quoted in full from the ledger:

> "'KEY CONTRACTS AND MODULE CONTRACTS ETC NEED TO BE EXPLICITLY DEFINED IN A CENTRALIZED
> HIERARCHICAL MANNER' (Jordan, this session) — RULED, NOT EXECUTED, AND LOGGED LATE. Like
> ED-FA-0038 this ruling went unrecorded: a post-merge audit grepped the tree for its own words and
> found ZERO files. It is filed `status: open` and NOT `needs_jordan` — Jordan has ruled; what is
> missing is execution, and flagging it for him would be the parking-space misuse CLAUDE.md §0
> forbids. THE MEASURED CURRENT STATE, so the next session starts from a fact rather than an
> impression. Three registries exist and none of them is hierarchically related to the others:
> references/module_contracts.yaml (27 modules + 27 composition_roles, with each module's Key IN ->
> resolver -> OUT and owned state), engine/engine_params/key_types.json (55 key types, cooked from
> key_type_registry_v30.md behind a blocking exporter), and references/descriptor_registry.yaml
> (attributes, aggregates, faction/settlement stats and their bounds). They are three FLAT
> namespaces that reference each other by string. There is no single surface from which a reader —
> or the Godot port — can descend from 'the game' to a subsystem to a module to its Keys to the
> fields those Keys carry. WHY IT IS NOT DONE HERE, stated rather than left as an unexplained gap:
> it is a genuine architecture job, not a re-siting. It needs a decision about what the hierarchy's
> LEVELS are (scale? subsystem? module? Key?), whether the existing three registries become views of
> one artifact or stay separate with a declared parent, and what the exporter/round-trip story is
> for the composite. Faking it by nesting the current three files under a new top-level key would
> produce a hierarchy in shape and not in meaning, which is worse than the honest flat state because
> it would look done. WHAT IS ALREADY POINTING THIS WAY, and should be read before starting:
> systems/_architecture/propagation_spec_v1.md §1's O.2 engine_clock contract is the worked example
> of a module contract stated properly; ED-1051 is the open question of whether that form is
> ratified; 9 of 27 modules still carry `doc: null` and 11 of 27 resolvers are [ASSUMPTION]-grade,
> so a third of the contract surface is not yet an implementable spec at all. A hierarchy over a
> surface that incomplete would centralise the holes as much as the content. Authoring the missing
> contracts is plausibly the first half of this work. RELATED AND DELIBERATELY SEPARATE: the
> wrapper/orchestrator architecture Jordan described in the same conversation (each subsystem has a
> wrapper handling all Key I/O; inputs trickle down with increasing granularity, outputs aggregate
> up) is the RUNTIME half of the same idea. ED-SC-0032 executed one instance of it — the
> degree-ladder extension seam — and that is one seam, not the architecture. MEASURED-BY:
> references/module_contracts.yaml … MEASURED-BY: engine/engine_params/key_types.json …"

**ED-IN-0201** (2026-08-28, same file, `status: open`, **`needs_jordan: false`**), quoted in full:

> "PERSONNEL PRECONDITION — RULED BY JORDAN, THIS SESSION, NOT EXECUTED. Verbatim: 'all faction
> actions, settlement governance, mass battles, etc are predicated upon people existing. we do not
> allow the game to perform faction actions if there is no leader of that faction, and that leader
> themselves is going to influence what choices are made for available faction actions in the same
> way that the person(s) who are governing a settlement or conducting a battle may make different
> choices with the same information and options.' Filed status:open and NOT needs_jordan — Jordan
> has ruled; what is missing is execution. TWO CLAUSES, and they are separable. (1) THE GATE: no
> leader, no faction action; no governor, no settlement governance; no commander, no battle (the
> third is the one genuine ambiguity — see below). (2) THE DECIDER: the person shapes WHICH action
> is chosen from the same option set with the same information. Clause 2 is presence-as-identity,
> not presence-as-a-stat: the person must change the choice, not scale a modifier. MEASURED STATE AT
> HEAD. engine/autoload/game_state.py Faction has NO leader/ruler/head field (verified by read,
> :109-140). engine/mc_v18.py's faction pass gates on exactly two conditions, `faction.parliamentary`
> and `faction.territories`, then calls faction_action unconditionally.
> systems/factions/sim/faction_action.py selects with one rng.random() against a prior re-weighted
> by three RNG-free FACTION-level signals; no person is consulted anywhere. Settlement.governor_id
> is None on all 37 after world-gen and its only writer succeed_governor has zero callers.
> massbattle.py's _faction_to_unit sets neither charisma nor cognition, so derive_command falls back
> to a hardcoded command=4 despite COMMAND_SIGMA_ENABLED defaulting ON. world.npcs is empty in every
> seeded campaign. THE BOOTSTRAP CONSEQUENCE, which is the load-bearing one: under clause 1, with
> world.npcs empty, a campaign performs ZERO faction actions. The ruling therefore promotes the
> person loader from an enhancement to a PRECONDITION OF THE ENGINE RUNNING, and requires leaders to
> exist at world-gen before season 1 rather than being generated during play. SECOND CONSEQUENCE: it
> makes systems/social_contest/sim/contest/faction.py::succession load-bearing. … THIRD CONSEQUENCE:
> the deciding logic belongs to a person-AI, not a faction-AI. engine/autoload/npc_ai.py is the
> module named for it; both its entry points are typed no-ops … NERS NOTE: clause 2 must not be
> implemented as a flat trait bonus … the leader changes the OPTION SET and the POOL SOURCE, not a
> modifier … ONE GENUINE AMBIGUITY, flagged rather than decided: 'no commander, no battle' has two
> readings … (a) a faction with no available commander CANNOT declare a conquest, or (b) it can, and
> an unled army fights at a penalty (the Dominions shape). … Recorded as open. IMPACT CLASS: MOVES,
> at the largest scale in the tree — it changes which actions occur, so every seeded golden moves
> and a balance_oracle control is mandatory."

**The reconciliation, ruled.** Three facts the sweeps did not put together:

1. **Neither ruling is an open question.** Both are RULED-NOT-EXECUTED, filed `needs_jordan: false`
   by their own authors precisely to avoid the parking-space misuse. They do not escalate.
2. **The design line did not lack access — it filed them.** ED-IN-0201 was created and recorded by
   PR #338's own session; PR #339's index *executes both by name*, and 20 files across the two
   greenfield suites cite them (grep, this session). The citations vanish exactly at PR #342, whose
   method line reads "designed and coded from scratch. All existing work was reference, never
   ruling" (`00_INDEX.md:6`). The zero-citation state of the head is a **consequence of the
   from-scratch method reset, not ignorance** — R4's "may not have had access" is overturned (§9.7).
3. **The design line is the answers, unattributed.** The head's Person carrier + `choose(Person,
   View, Sensation)` + person-generation triggers + "if no person acts, no social thing occurs" is
   the most complete design for **ED-IN-0201** on disk — clause 1 is its no-fallback rule, clause 2
   is its whole choose-signature thesis, and the NERS note's "option set and pool source, never a
   modifier" is the head's own opening_set/pool design. The head's `03_COMPENDIUM.md` is a working
   demonstration of the hierarchical registration surface **ED-IN-0200** demands — for the *new*
   design only; it does nothing for the three live registries the ruling is actually about.

**Ruling:** ED-IN-0201 — *the ideal-v2 design is its unwitting execution vehicle on the design
side*; the ledger row stays open until the code side lands (world-gen leaders, the gate in
`mc_v18`, a person-AI). Session work: add a cross-citation both ways. The commander ambiguity
inside it closes by the design's own partition — "no social thing occurs without a person acting"
selects reading (a), the gate; record it, don't escalate. ED-IN-0200 — stays open; the suite should
declare itself the *template* for the hierarchy (levels: game → subsystem → module → Key → field,
which the compendium already exhibits) and 0200's execution then becomes migrating the three live
registries under it — separate, later work. **Neither ruling is superseded; the design line is an
unwitting answer to both; the reconciliation is two citation edits and one recorded reading, all
session-grade.**

---

## 7. THE ANCESTRY

"Earliest statement" = earliest on-disk statement found by any lane, verified where marked.

| idea | earliest statement | how it reached the current head | cited? |
|---|---|---|---|
| **Person-not-faction iteration** | diagnosis: `2026-08-25-throughlines-and-precedent/04_ch1_the_world_has_no_people.md` (630 lines); architecture: integration master **P4** `research/…_part4.md:619` ("THE SEASON IS A PERSON'S SEASON", 2026-08-27, verified) + companion **U-3** | P4/U-3 (08-27/28) → greenfield Post/person entities (08-28) → #342's one-actor substrate (08-29, from-scratch reset) → head | **NO** — zero grep hits for either research master in the six-file suite (verified). The NERS repair P4 carries ("roster buys action-count, not pool size") was re-derived as D-2 |
| **The containment ladder as derived, not parent-pointer** | `systems/settlements/scale_hierarchy_v1.md` §2 + §5.1 (RATIFIED 2026-07-13): Province existence-conditional; factions hold people | generalized by #342's containment/alignment split → `Rung` + `contain`/`hold` Tenure kinds | **NO** — the ratified precedent is uncited; the head presents the generalization without its case law |
| **Offices and tenure** | per-faction rank ladders `faction_politics_v30.md` (CANONICAL 2026-04-17); custodian≠holder: precedent companion I-13 (Kremlin, 08-28); Post primitive: greenfield `01_substrate_primitives.md` (08-28) | `Holding := (person, office, since, conferrer)` in #342's `SUP:367` → widened to `Tenure` (7 kinds) by the keys audit + review A-10/A-12 | **NO** for all three ancestors |
| **The Key substrate** | `key_substrate_v30.md` (PP-687, CANONICAL 2026-05-01); executable `engine/substrate/keys.py` (2026-07-07) | cited by the head **narrowly** — §12 precedent appendix (8 rows: ids, invariants, cycles) and §2.2 | **PARTIAL** — id discipline yes; the witness/memory/salience machinery (§4 of the substrate) never reconciled |
| **Witness / claim / belief** | `key_substrate_v30.md` 4.1-4.2 `compute_observers` (05-01); `beliefs.py` Belief; **five RULED Jordan calls** `2026-08-18-epistemic-propositions-and-provenance.md` P1-P5; `2026-08-18-fieldwork-architecture…` §13 rulings | P1-P5 → doc 09's O-A5 (secondhand) → head; doc 03's claim machinery → head (directly, post-correction) | doc 03 **YES** (post-correction, heavily); the two 2026-08-18 RULING documents **NO** — the head inherits ratified rulings secondhand |
| **The act economy** | `governance_play_redesign_v1.md` 1.1 AP economy (2026-06-22, zero code readers) | greenfield "budget buys actions" → #342's one-act rule (`09:33`) vs `14:562` contradiction → fixes/02 Reading C (measured) ∥ head's D-2 (ruled) — convergent endpoints | redesign **NO**; fixes/02 **YES** (named unread-but-matching) |
| **Salience / the slate** | `key_substrate_v30.md` 4.5 `compute_salience()` + `player_agency_v30.md` Scene Slate (CANONICAL) + Light Function (RATIFIED, ED-IN-0011) | greenfield-v2 `10_the_slate_and_salience.md` supplies the candidate definition the Light Function presupposes → head acknowledges it unread; head's own §4.1 salience formula descends from doc 03 | CANONICAL ancestors **NO**; 10 acknowledged-unread |
| **Exogenous events** | redesign Part 2 Pi-deck (06-22) → `grounded_event_card_deck_v1.md` 58 cards (07-11) → ripple substrate (07-11) → `11_world_events.md` (08-29) → head's partition + MATTER events | four generations, each unaware of most predecessors | only 11, post-correction |

**The practical cost of unread ancestry, stated as the section header demands:** the corrections
the ancestors contain were not applied. Concretely: U-4's isolation test never made it into the
head's acceptance criteria; F10's attribution discipline (land cheap writers one at a time or the
measurement is confounded) is absent from the head's build guidance; the 2026-08-18 ratified
rulings reach the head only through one derivative document's paraphrase; and the head re-derived
P4's NERS repair from scratch, spending two adversarial rounds to reach a result the corpus had
held, with math, for four days.

---

## 8. WHAT TO READ NEXT — ranked by expected change to the architecture

1. **`systems/_architecture/key_substrate_v30.md` §4 + `engine/substrate/keys.py`** — would change
   the suite's Event/witness layer from a parallel design into a specialization of the one
   CANONICAL executable substrate (fan-out = `compute_observers`; Event = Key row; claims deposit
   per-observer as Memory already does). The single highest-stakes reconciliation.
2. **`…-v2/10_the_slate_and_salience.md` + `_part2` (1,152)** — candidate contract (C-1..C-6),
   bounded+monotone truncation proof, cast/depth severance, per-candidate RNG substreams. Likely
   closes G-01's producer and rewrites 02's "what surfaces this season."
3. **`research/valoria_systems_integration_master_v1_part4.md` + `…precedent_companion_v1_part4.md`**
   — P1–P4 ordering, F10 attribution discipline, U-1 (free first move), U-4 (the acceptance test
   the design must pass to claim its own differentiator).
4. **greenfield-v2 `01_substrate_primitives.md`(+part2), `03_world_population.md`,
   `04_personnel_management.md`** — the storage discipline (four write leaves) under the head's
   carriers; likely closes G-15, G-16, G-18; supplies the world-gen population the head never
   states.
5. **`2026-08-30-fixes/03,04,05` + `09_GAP_REPORT.md`** — need formulas, settlement membership,
   councillor venues, the 19 blocked-core dispositions: content the suite must absorb or refute
   row by row.
6. **doc 03 §§7-9, §12** (`03_knowledge_telling_investigation.md`) — correspondence filtering /
   channel-holder power, the P-08 ledger-referent barrier, the worked trace — still undiscussed in
   the head beyond one `filter_share` pickup.
7. **`2026-08-18-fieldwork-architecture…` §13 + `2026-08-18-epistemic-propositions…` P1-P5** — the
   ratified rulings, firsthand; removes the secondhand dependency.
8. **`2026-08-31-integration/04, 05, 11_INTEGRATED.md`** — harvest anything SUP dropped, then
   archive; ends the parallel-synthesis ambiguity.
9. **`11_world_events.md` §2-3** rate bounds (G-07 candidate) + **`grounded_event_card_deck_v1.md`**
   (58 authored cards for MATTER step 6) + ripple substrate's AT-RISK SC hook (the one cross-system
   edge every event design inherits).
10. **`canonical_nomenclature_v1.md`** — the other half of the collision problem (grep-noise class);
    its Phase-0 items fold into §10.3's batch.

---

## 9. WHAT I OVERTURN

1. **PR #344's "108 of 123, 15 touched" as a current-state claim** — stale; current truth 103/133,
   30 touched (§1). Worse: the stale figure still stands in the live head at
   `…-ideal-v2/00_INDEX.md:10` (verified). Both R5 and I independently re-measured — bankable.
2. **PR #344's "an invented `investigate` verb"** as a description of the merged state — R6
   verified the post-correction table entry is a header over the six shipped acts
   (`03_COMPENDIUM.md:353` = `cross_scale_action_catalogue_v1.md:610-619`, row-for-row). True of
   the draft, false of the tree.
3. **R3's "F-4 is the one FATAL not remediated anywhere"** — half-overturned by direct read: the
   fixed-point ruling exists at `01_ARCHITECTURE.md:454-466` ("`condition` AND `stores` ARE
   FIXED-POINT INTEGERS"); R3's quoted range stopped at :449, five lines short. What survives of
   R3's finding: `02_THE_SEASON_LOOP.md:570-573`/§10 were never updated (ADD-4). The PR344 log's
   implication that F-4 was fully folded is equally half-wrong.
4. **`03_COMPENDIUM.md` G-26** — its subject was already resolved in the same merged tree:
   PR #343 deleted the licence column, `07_alignment.md:706-711` says so in prose ("the licence
   table is now gone"; verified). Closed-by-merged-edit; the register audited a stale snapshot.
5. **`03_COMPENDIUM.md` G-30's RESERVED tag** — stale against its own sibling: `01_ARCHITECTURE.md`
   §7/§11 records F6 RULED by Jordan ("the world is in flux," `wear`). The live residue is a
   ratio measurement, not the fork.
6. **R5's "two independent same-day syntheses … neither cites the other"** — overstated:
   `10_SUPERSEDING.md:27` declares `2026-08-31-integration/09_citation_ledger.md` its verified
   fact base (verified), so the integration line is upstream of SUP. What survives: the integration
   *synthesis products* (04/05/11) are cited by nothing downstream. The escalation R5 filed on this
   demotes to a harvest task (§8.8).
7. **R4's "the design may not have had access to [ED-IN-0200/0201]"** — overturned: PR #338's own
   session filed ED-IN-0201; PR #339 executes both by name; 20 greenfield files cite them
   (verified). The from-scratch reset dropped them deliberately-by-method, not by unavailability.
8. **R2's "the single largest miss is that `key_substrate_v30.md` … is not cited"** — qualified:
   the head cites `keys.py` in eight precedent rows (`03_COMPENDIUM.md` §12) and §2.2. The true
   miss is narrower and worse-shaped: the *witness/memory/salience* machinery specifically is
   never reconciled, while the id machinery is happily borrowed.
9. **The task brief's framing that ED-IN-0200/0201 "look like independent answers to the same
   problem"** awaiting reconciliation-by-Jordan — both rows are `needs_jordan: false`,
   ruled-not-executed; the reconciliation is citation work, not a ruling (§6).
10. **`STRAT:75-77` (`personal_combat: dice_pool`)** — contradicted by the live registry
    (`module_contracts.yaml`: `d_sigma`; R3 §4/§9 verified by parse). The strategy doc is stale on
    its own terms; O-5's two-way framing is really three-way (ADD-14).
11. **CLAUDE.md §0.05's "248 uncited"** — off by one against the live artifact:
    `sim_params.json.citation_coverage` reads `{cited:166, total:415, uncited:249}` (R1, live
    read). One-line doc fix, flagged not made (read-only).
12. **R5's `hold`/`kind`/`View` collision-register sufficiency verdicts** stand, but its §6 claim
    that the head's register has "18 rows" (repeated by PR344's log) — the table holds 22 data
    rows (counted). Trivial, recorded for hygiene.

---

## 10. ⭐ WHAT ESCALATES TO JORDAN

Applying §0's five tests in order to every candidate the fourteen logs raised. The register the
tests **close** (with the closing test):

- G-04 leaders' comparator → **test 5** (faction=Proposition+commits forces a commitment-derived
  comparator; adopt `REV:772-778`, record).
- G-25 Coherence tables, G-29 playable seats, D-16 cohort exploit, the ED-IN-0201 commander
  ambiguity → **tests 3/4/5** (§4, §5, §6 above — each closed with its citation).
- `piety_track` owner (nomenclature §3.3's "three docs disagree") → **test 4**: the live registry
  already ships BOTH scopes as separate modules (`piety_track` personal + `territorial_piety`
  territorial, `module_contracts.yaml`; R3 §4 rows 4-5). The "one owner" question dissolved when
  the contract layer split it; close citing the two rows.
- ripple substrate R-1..R-4 + redesign ratification → **tests 1/2**: three later design
  generations superseded the direction; the documents move to REFERENCE/ANCESTOR (§2); the one
  live residue (the AT-RISK SC hook) is a gap row, not a ruling.
- "Which of the two live architectures is the head?" → **test 5**: write the suite on ideal-v2's
  spine (newest, most-corrected, absorbs the most) with greenfield-v2's substrate mapped under it
  as the storage discipline (Entity↔carrier, Tag↔mark/Tenure-adjacent, Gauge↔condition/stores,
  Post↔Office+hold). Ratification of the *resulting* suite is Jordan's ordinary ED-1094 merge
  review — the held-back banners mean nothing is ratified until then; that is process, not an
  escalation.
- Recall as the tenth attribute → **test 4** (precedent: shipped code,
  `CharacterCreationManager.gd:146-151`, 19 references; §0.05 code-is-mechanism). Record it in the
  suite; the registry's "naming is the open workshop" note means Jordan sees it at merge review —
  the loud-callout path, not a standing question.
- The wear:restoration ratio, `season_factor`'s distribution, the `R≤1` branch → **measurements**,
  not rulings; they need instruments, and §0.1 pt 4 forbids settling them by assertion.

**What survives all five tests — three genuine escalations:**

1. **D-6 / conferral rooting in the Church (person-rooted vs office-rooted vs off-map Holy See).**
   Not superseded, not irrelevant; the design documents *explicitly refuse to answer it* — the arc
   synthesis's office-rooted adjudication was formally **withdrawn** as "not an audit's call"
   (SUP §4.5/§16), and `09_GAP_REPORT.md` D-6 independently converged on the same question with a
   third option (canon's off-map Holy See). Two-plus defensible options, materially different
   Church games (a self-consecrating hierarchy vs an externally-rooted one vs an off-board
   authority as event source under F5's own pattern). Evidence pack for the ruling: arc synthesis
   §3's four office-rooted demands; D-6's Holy-See reading; F5's off-board precedent.
2. **The port's two reserved rulings, bundled — (a) `STRAT:213` autoload/state-owner, (b) M-12
   save model.** Both sit in the governing spec's own `[OPEN — Jordan]` register (Part VIII) —
   already his by that document's charter, surfaced as now-due rather than newly escalated. (a) is
   forced: the head's F-1 purity fix requires *no live state behind any global name*, while the
   stale plan and the live `valoria-game` tree both do the opposite (`Meta`/`GameState` autoloads,
   `STRAT:97`, `scene_tree_architecture.md:16`); recommendation: rule the head's way. (b):
   `STRAT:19`'s log-replay save vs the head's snapshot-save are incompatible load paths;
   recommendation on file (snapshot; log retained for provenance/UI; re-run-from-seed stays a test
   device). Each is one sentence to rule and a rewrite to leave.
3. **Godot version Q3 — not a new escalation; a briefing addendum to the one already queued**
   (CLAUDE.md §3 forbids picking). New facts for the ruling: the only artifact asserting 4.6
   (`ecosystem_versions.yaml`) is gone from `main` and unreachable in this shallow clone; 4.3 has
   two executed, reproducible compile runs and a `git`-verifiable `project.godot:11`; only three
   design recommendations are version-gated, each with a fallback (R3 §5, verified).

Everything else in the fourteen logs' "claims to escalate" sections is closed above with its
citation. That is 20+ candidate escalations reduced to three — which is what §0's amendment says
a session is for.

---

## 11. CONFIDENCE, and the independently-rediscovered findings

**Confidence per major ruling:**

| ruling | confidence | ground |
|---|---|---|
| §1 coverage figures (133/103/30, 67.7%) | **high** | reproduced byte-exact from scratch |
| §2 supersession spine (canon untouched; SUP+ideal-v2 head; greenfield-v2 parallel-live) | **high** | status headers read directly |
| §3 rows 1-9 | high | mechanisms verified by ≥2 lanes or direct read |
| §3 rows 10-17 | medium-high | single-lane reproductions, spot-verified |
| §4 G-register re-rulings (G-26, G-30 overturns) | **high** | tree read directly this session |
| §4 ADD-1 world-substrate | high | 3-route independent convergence |
| §4 "likely closed-by-uncited-doc" rows (G-15/16/18) | **low — flagged, unverified**; candidates named, not read | [unclear] until those three greenfield docs are read |
| §5 fork rulings | high (D-2, F5, F6), medium (F1-F4 residues) | both sides quoted from tree |
| §6 ED reconciliation | **high** | ledger rows quoted in full; citation greps run both directions |
| §7 ancestry earliest-statements | medium | earliest-on-disk per lane evidence; an earlier statement may exist in unread files |
| §10 escalation set | high | each closure carries its citation |

**Independently rediscovered by two or more lanes (§10's bankable signature):**

1. **The uncited-corpus problem itself** — PR #344's self-audit, R5's re-measure, R6's research/
   extension: three routes, one finding.
2. **`world.npcs` empty / the absent person as the binding constraint** — R1, R4, R6, PR #337
   (F2), PR #338 (measured), PR #341 (the named gap): five-plus independent statements. The most
   corroborated fact in the whole exercise.
3. **The world-substrate hole** — three arc lanes, independently (arcs 5/22/27/48), explicitly
   ruled a non-seeded convergence by `04_SYNTHESIS.md` §2. → ADD-1.
4. **D-2's establishment reading** — fixes/02 (measured) ∥ ideal-v2 (ruled) ∥ P4's NERS repair
   (derived): **three** independent routes to one mechanism. The strongest design result in the
   corpus.
5. **WITNESS is a global barrier** — two of PR #344's five isolated runners, separately.
6. **The six investigation acts** — doc 03 ∥ `cross_scale_action_catalogue_v1.md:610-619`,
   row-for-row, plus the head's correction: convergence, not copying.
7. **`engine_clock`'s missing contract = the season loop document** — R3 (O-2), R6, PR #344's own
   §8.5: three lanes, same one-line fix (ADD-13).
8. **ED-IN-0200/0201 as unacknowledged antecedents** — R4 found them; my greps confirmed the
   citation cliff at PR #342. Two routes.
9. **F-1's autoload reach is real, not hypothetical** — R3's direct read of
   `strike_module.gd:38-67` ∥ PR #344's §3.2 citing the same lines independently.
10. **The Godot version conflict** — two separate 2026-08 sessions executed 4.3 headless
    (interrogation log, return-to-game baseline), plus R3's documentary sweep.
11. **The Key substrate as the design's executable twin** — R2 (systems side) ∥ R1 (engine side)
    ∥ R6 (test side, `test_key_substrate.py`): three lanes each independently named it the
    reconciliation target.

The four adjudication rulings I would stake least on, stated per §0.1 pt 3: the three
closed-by-uncited-doc candidates (G-15/16/18 — falsifier: read the named greenfield docs and find
nothing) and the §7 "earliest statement" column (falsifier: a full-corpus grep for each idea's
vocabulary predating the cited dates).
