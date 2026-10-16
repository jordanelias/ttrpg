# Research and Precedent Index — game precedent and historical research, keyed for interrogating the subsystems and the plan

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · a pointer index; resolves nothing at runtime
## Date: 2026-10-15 · read at HEAD `462c68a` · Lane: IN (cross-cutting)
## Reads: every tracked document that surveys other games or draws on history, found by the commands in §9

**What this is.** One map of everything the repository holds as game precedent and historical research,
indexed three ways so a verb, a primitive or a function can be put to the evidence: by **function** (§3), by
**verb** (§4) and by **primitive** (§5). §6 sets the live plan against it. It does not argue a design, rank
a proposal or schedule work. If it were deleted the game would behave identically.

**Every count here is a dated reading** of the command in §9, not a standing figure. A mention count measures
where a game is *named*, not how deeply it was studied.

---

## 1. Rules for reading the evidence

1. **Research is tier 3 and cannot settle a design question.** The source-precedence ruling (Jordan,
   2026-09-02) is written at `engine/season/rosters.yaml:75`: *"`research/` contains useful information to
   make everything more robust"* — it *"informs DESIGN; it is not a source of canon names."* Two rosters
   built from it (`governance_modes`, `power_bases`) were deleted because nothing read them
   (`engine/season/rosters.yaml:86-88`); the insight survives as hole-register row `H-100`
   (`engine/season/hole_register.yaml`, `source: research/ -- Jordan-directed 2026-09-02`). A finding that
   reaches the game must reach it through an owner that code reads (CLAUDE.md §0.05).
2. **The sourcing floor binds every number.** Fan wikis were bot-walled (Paradox, KOEI, Brigandine, Unicorn
   Overlord returned 402/403), so specific figures about games are leads; the durable findings are *shapes*
   (`COMP-1` §1.2). Strongest game rows: Victoria 3 law enactment, Pax Pamir pricing, Burning Wheel's
   *Duel of Wits*. Marks such as `[UNVERIFIED]` and `[SELF-AUTHORED — bias risk]` are carried at source.
3. **Convergence is the evidence class that earns weight.** The three game programs never read each other
   (`COMP-1` §1.1), and the historical corpora were run per civilization with an independent verifier. Where
   a game and an institution arrive at one shape, that coincidence is the strongest form of evidence here.
4. **Nulls are findings.** Where no shipped game solves a problem, citing precedent is false comfort
   (`COMP-2` §3.4; `PREC-NULLS`). Check §7 before asserting "the genre does X".
5. **Verdicts about Valoria in the precedent documents are dated.** `COMP-3` §7 judged the 2026-08-28 tree
   against the retired campaign driver; `proposals/2026-09-30-character-and-play-surface/02_against_precedent.md`
   §2 re-scores each verdict against `engine/season/` at `c8cc408`. Read the re-score, not `COMP-3` §7.11,
   for the season loop.
6. **Citations inside these files use pre-restructure paths.** Resolve with §8.

### Key to the short names used below

| short | path |
|---|---|
| `COMP-n` | `research/valoria_game_precedent_companion_v1.md` (n=1) and `…_part2.md` … `…_part8.md` (n=2…8) |
| `SIM-n` | `research/valoria_systems_integration_master_v1.md` (n=1), `…_part2.md` … `…_part4.md` |
| `PMM` | `research/personnel_muster_integration_master_v1.md` |
| `XSC` | `research/cross_scale_action_catalogue_v1.md` |
| `GOV` | `research/governance/` (`governance_modes.md`, `political_hierarchy_standing.md`, `conflicts_power_struggles.md`, `00_MANIFEST.md`) |
| `FASE` | `research/fa_se_historical_precedent_research_v1.md` |
| `HCC` | `research/historical_concerns_action_catalogue_v1.md` |
| `PGS` | `research/proactive_governance_scale_research_v1.md` |
| `RTP` | `research/rise_to_power_roster_system_research_v1.md` |
| `RHET` | `research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md` |
| `PFF` | `research/pre_firearms_formations/` (`00_MANIFEST.md`, `01`–`16`) |
| `PA`, `PW` | `research/historical/precedents_analysis.md`, `research/historical/precedents_warfare.md` |
| `MBG` | `research/historical/mass_battle_gauge_grounding.md` |
| `THR` | `proposals/2026-08-25-throughlines-and-precedent/` (`00_index.md`, `04`–`09`) |
| `PREC-NULLS` | `proposals/_session_provenance/2026-08-29-to-31/PRECEDENT.md` |
| `EMG` | `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md` |
| `VCD` | `proposals/2026-10-03-verb-coverage-and-gap-fill.md` |
| `CGR` | `.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md` |
| `SC-SRC` | `.audit/2026-08-06-social-contest-three-lens-audit/sources/` (`01`–`05`) |
| `SNAP:<path>` | `<path>` at git tag `v30-snapshot-2026-06-28` (read with `git show v30-snapshot-2026-06-28:<path>` after `git fetch --depth=1 origin tag v30-snapshot-2026-06-28`) |
| `ARCH:<path>` | `<path>` at git tag `archive-2026-08-05` (same method) |

---

## 2. The source registry

### 2.A Game precedent

| source | what it holds | status as stated · limits |
|---|---|---|
| `COMP-1`…`COMP-8` | **The collation.** Three independent programs (political mechanics; personnel and muster; failure dossiers P1–P5) surveyed against ten-plus systems. `COMP-1` §2.1–2.13 survey by system · `COMP-2` §3 convergences, divergences, five failure shapes, seven nulls; §4 complements; §5 synergies S1–S6; §6 steal/refuse · `COMP-3` §7 Valoria judged · `COMP-4` §8 reconciliation R1–R7, §9 unification U-1…U-4, §11 import register · `COMP-5` §12 comparative matrix · `COMP-6` §13 six precedents decomposed in Valoria's slices · `COMP-7` §14 the person across systems · `COMP-8` §15–22 the personnel precondition, ED-IN-0201 | PROPOSED 2026-08-28. Tactics Ogre surveyed with no surviving finding (`COMP-1` §1.1). `COMP-3` verdicts predate the season loop (§1 rule 5) |
| `PMM` | Nine passes (KOEI Romance of the Three Kingdoms and Nobunaga, CK2/3, Total War, Jagged Alliance, Brigandine, Unicorn Overlord, Tactics Ogre, Triangle Strategy, Radiata Stories) as five personnel and four muster lanes, with a convergence count per finding | FILED 2026-08-27. Numbers cluster on the two KOEI manuals that fetched |
| `THR` | Failure dossiers: every mechanism recommended in ch. 1–4 must arrive with a shipped precedent that **failed while holding it**; `08_ch5_what_we_should_not_do.md` names five failure shapes | PROPOSED 2026-08-25. Claims carried at the dossiers' own confidence |
| `PREC-NULLS` | Nine nulls (N-1…N-9) where the design is inventing, not adapting: argument content, interior-state expression, personal leverage across N, auto-resolve calibration, certifying generated content, legibility against depth, the appointed governor, unit-quality caps, social fog of war | session provenance; unheaded |
| `EMG` | What stores story in CK2/3, Dwarf Fortress, RimWorld, the Nemesis system, Caves of Qud / Ultima Ratio Regum, King of Dragon Pass / Six Ages, Pentiment; its "memory question" finding | REFERENCE 2026-09-06; run at `sonnet`; the two tabletop entries not freshly sourced |
| `proposals/2026-09-05-proceedings-subsystem/relay/A_FABLE_INTERROGATION.md` | Precedent survey, option surface and refusals for the proceedings subsystem (Ace Attorney, Pax Pamir, PbtA, Burning Wheel among 17 games named) | PROPOSED 2026-09-06; `fable`, read-only, informing only |
| `proposals/2026-08-23-suite-05-precedent-and-proposals.md` | Published systems graded DOCUMENTED / REPORTED / INFERRED, against Valoria analogue grades ANALOGUE / PARTIAL / NOTHING | unratified |
| `proposals/2026-09-30-character-and-play-surface/02_against_precedent.md` | The re-score of the August survey against `engine/season/` (scope, concept, emergence) | PROPOSED 2026-09-30 |
| `proposals/2026-09-03-governance-corpus-rebuild/02-critique-and-precedents.md` | A governance design critiqued against precedent | `[SELF-AUTHORED — bias risk]` |
| `proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md` | Acclaimed games on exploration, investigation and non-adversarial play (10 games named) | design calls ruled 2026-08-18; architecture unbuilt |
| `proposals/2026-09-25-squad-engagement-concept-v5.md` | Football Manager and Total War as the formation model; Unicorn Overlord | CONCEPT, non-canonical |
| `VCD` | **Seven detective games** (*Pentiment*, *Disco Elysium*, *Esoteric Ebb*, *Lacuna*, *L.A. Noire*, *Tails Noir*, *Shadows of Doubt*), CK3 and Romance of the Three Kingdoms, and governance history, as 707 candidate acts → 63 act families (App. B). It also interrogates two surveys **not committed to the repository** — *Mechanics of Inquiry, Speech and Rule* (P1–P58, families A–K) and *Narrative Churn* (F01–F84, sets A–K); VCD carries their points in its own words (§6.1–6.8) | RATIFIED AS INTENT (v9, ED-IN-0288); each verdict held until built |
| `SC-SRC` | Jordan's five uploaded persuasion and political-mechanics documents, verbatim: TTRPG debate systems, courtroom adventure games, grand strategy, seven negotiation board games → 45 primitives (P1–P45) → 14 mechanisms + 31 configurations | SOURCE MATERIAL, not canon; quarantined |
| `valoria_ui_ux_v4.md`, `valoria_ui_ux_v4_1.md`, `valoria_ui_ux_v4_1_max_audit.md` (in `.designs/`, named by bare filename) | UI precedents (Disco Elysium, Pentiment, Tactics Ogre and others) | quarantined, not read for this index beyond mention counts |

### 2.B Historical research

| source | subject · method | coverage | status |
|---|---|---|---|
| `GOV` | Governance, three themes (modes · hierarchy and standing · conflicts and power struggles), each with a `=> Valoria design hook` per pattern and a consolidated hooks table. Sonnet researcher → Opus verifier per civilization | Ottoman · Roman (Republic–Dominate) · Carolingian · Holy Roman · Renaissance Italy and Papal States · Venice · Han and Three Kingdoms · Shogunate Japan. **Byzantium omitted** (agent interrupted) | RESEARCH, ED-IN-0064, 2026-07-14 |
| `CGR` | Round 2 of the FA/SE program: economic development, guilds, bureaucracy, courts, civic and provincial governance | Byzantium · China · feudal Japan · HRE · Venice · Renaissance Italy · Habsburg Spain | FILED 2026-07-09; quarantined |
| `FASE` | Round 1, ten themes T1–T10: fiscal sociology, tax farming, moral economy of subsistence, urban charters, governor control, conquest terms, church–state jurisdiction, frontier colonization, interregna, legitimacy theory | Tilly/Levi/Brewer, Thompson/Scott/Sen, Weber/Olson/Hirschman/Ibn Khaldun | FILED 2026-07-08 |
| `RTP` | How people rose to influence — categories A patronage · B merit · C marriage and kinship · D favourites · E bureaucratic capture · F military retinues · G downfall and purges · H court factions · I venality · J religious authority; §3 roster/advancement proposal | unrestricted era | FILED 2026-07-11 |
| `HCC` | Crises that damage settlements and economies, 10 categories: succession, embargo, siege and sack, earthquake and eruption, flood and drought, famine, plague, climate and storm, debasement, trade monopoly; §3 ripple chains; §4 cross-reference to the 44 proposals | event-deck source | FILED 2026-07-10 |
| `PGS` | What leaders did proactively, at settlement, organization, territory and faction scale; §4 reuse-versus-new-lever ledger | four scales | FILED 2026-07-11 |
| `PA`, `PW` | Theocracy establishment, invasion during civil instability, movements to governance, post-occupation governance; warfare, sieges, mustering, territory seizure, legitimacy | Papal States, Geneva, Iran 1979, Tibet; Crécy, Agincourt, Cannae, Hastings, Austerlitz | ANALYSIS 2026-04-17 |
| `PFF` | Pre-firearms formations, ~3000 BC–1525, weighted to 1450–1525: `01_ancient`, `02_classical`, `03_early_medieval`, `04_high_medieval`, `05_late_med_renaissance_europe`, `06_renaissance_islamic_steppe`, `07_renaissance_east_asia`, `08_pre_columbian`; then (by filename) `09` throughlines and matchups · `10` battle-phase choreography · `11` throughlines NERS audit · `12` moment-by-moment dynamic spacing · `13` verification corrections · `14` methodology audit · `15` methodology resolutions · `16` historical-versus-game-design audit | grand formation / unit formation / unit / strategy / tactic vocabulary (`00_MANIFEST.md`) | research |
| `MBG` | Bottom-up grounding for the mass-battle gauge bands from historical precedent and the combat-modelling literature (Lanchester, Hillestad–Owen–Blumenthal, Taylor, Armstrong–Sodergren) | v2.4; `[SELF-AUTHORED — bias risk]` | drives `tests/sim/gauge_mb.py` |
| `research/diagrams/mass_battle_formations/` | Cannae and other formation schematics against engine output; `SOURCES.md` links originals (binary downloads were denied by the proxy) | | working |
| `RHET` | Rhetoric, oratory, debate, appeals, assemblies, trials and negotiation: Greece and Rome · Byzantine progymnasmata · Arabic-Islamic · Chinese · Indian (Nyāya) · medieval *artes* · assemblies and trials · royal appeals; §9 throughlines; §11 verification register | multilingual primary treatises | RESEARCH 2026-06-02 |
| `.audit/2026-07-02-scene-combat-closing-distance-redesign/r0_research_{commitment_depth,facing_stance,grappling,measure_gap}.json` | HEMA and biomechanical **facts**: commitment depth, facing and stance, grappling in armed combat, the measure gap (12 + 16 + 10 + 4 findings) | European and Asian sword and polearm traditions | quarantined |
| `.audit/2026-07-02-morphology-rearch-phase0/`, `.audit/2026-07-04-weapon-morphology-granularity/`, `proposals/weapon_physics_and_concentration_model.md` | 53 weapons graded by evidence (S1–S3), point-of-balance and composite-mass model | | quarantined / partly superseded (model built) |
| `.audit/2026-07-22-mass-battle-stress-test/historical_fidelity_readiness.md`, `cannae_historical.py`; `.audit/2026-07-04-mass-battle-cannae-gauge-audit/` | Whether the engine can stage and reproduce Cannae, Leuctra, Gaugamela, Zama | | the Cannae audit RATIFIED ED-MB-0002 |
| `canon/philosophy/08_history.md` | The *in-world* history (the Calamity, Solmund, the Church). **Not research** — world truth; listed so it is not mistaken for it | PROPOSED | canon |

### 2.C Syntheses that bridge both

| source | role |
|---|---|
| `SIM-1`…`SIM-4` | Every faction, personnel, settlement, governance, territory, NPC and political mechanic in the repository, sorted into ten systems and five slices (§2), flattened, analysed within and across systems, resolved to four rival integration proposals (`SIM-4` §6). PROPOSED 2026-08-28 |
| `research/provenance/2026-08-28-systems-integration-harvest/` | The 1,079 structured harvest records behind `SIM`. **Append-only; do not reason from them directly** — they predate the gate's corrections (`README.md`) |
| `XSC` | Every action at every scale with its formula and whether it resolves opposed or unopposed: §1 faction · §2 settlement · §3 mass battle · §4 personal combat · §5 social contest · §6 fieldwork · §7 threadwork · §8 cross-scale plumbing · §9 faction management |
| `.audit/2026-07-12-governance-compendium/` | Ten files including `42_action_verb_catalogue.md`, `40_roster_officer_system.md`, `41_proactive_scale_menus.md` |

### 2.D Where research reaches executable code (the only reach that counts under §0.05)

| consumer | what it takes from research |
|---|---|
| `modules/mass_battle/config.py` | Rout-onset and rout-cap fractions tagged `[canonical: Jordan historical research 2026-07-23]` (`:186-187`); Cannae-derived shock and rear-charge constants (`:230`, `:372`) |
| `tests/sim/gauge_mb.py` | Gauge bands H1–H5… each tagged `[canonical: mass_battle_gauge_grounding.md §3 …]` (`:324-332`). ⚠ It cites `references/historical/mass_battle_gauge_grounding.md`, a path that does not exist; the file is `MBG` (§8) |
| `engine/season/rosters.yaml:75`, `engine/season/hole_register.yaml` (`H-99`, `H-100`) | The tier-3 ruling and the one hole row that draws on `GOV` |
| `engine/season/verb_table.yaml` | The 44 verbs — the executable roster §4 is keyed to. Its evidence is `VCD`, not `research/` |

### 2.E Pre-restructure refs (tags `v30-snapshot-2026-06-28` and `archive-2026-08-05`)

Compared against the current tree by path, blob and basename. The tags are not named in `CLAUDE.md`, `CURRENT.md` or `references/*.md`.

| tree at the ref | files | against the current tree | precedent or history in it |
|---|---|---|---|
| `ARCH:research/` | 38 | **Every path and every blob is identical to current `research/`; nothing is archive-only.** The current tree adds 40 files besides this index (the companion, the two masters, `XSC`, `PMM`, the harvest provenance) | none beyond §2.A–2.C |
| `SNAP:references/historical/` | 3 | The three files are `PA`, `PW`, `MBG` under `research/historical/`; `PA` is identical, the other two differ by one line each | those three; the ref holds the original of the path `tests/sim/gauge_mb.py` still cites (§2.D) |
| `SNAP:designs/provincial/` (42), `SNAP:designs/territory/` (15) | 57 | **Design documents for subsystems, not research.** All but three share a basename with a file in the current tree (the documents moved under `.designs/`). The three absent are `strategic_layer_v30` (+ index, infill): the board-game layer, retired to `deprecated/archives/audit/` (`references/restructure_ledger.md:1010-1011`) | Light: `mass_battle_v30.md` names Cannae, Hastings, Leuctra, du Picq, Lanchester and Mount & Blade; `faction_politics_v30.md` names Skyrim (16×, the guild ladder) and Byzantium; `settlement_layer_v30.md` names Crusader Kings, CK3 and EU4 |
| `SNAP:archives/audit/` | 114 | **107 have no basename in the current tree**; the current `.audit/` holds a later, different set. These are the April–June 2026 audits | see below |
| `SNAP:tests/sim/` | 481 | **395 have no basename in the current tree.** Mass-battle and weapon-system sim code, specs and audit reports predating `modules/` and `.audit/` | see below |

Precedent- or history-bearing files at the snapshot, with no current counterpart located (heads read; bodies counted, not read):

| file | what it holds |
|---|---|
| `SNAP:archives/audit/2026-05-28-engine-replacement/engine_replacement_audit.md` (+ `_reconciled`, `_reconciled_AUDIT`) | Whether the d10/TN/Ob engine should be replaced, **each system compared with acclaimed precedent games** researched per system: Crusader Kings, CK3, Total War, Mount & Blade and others (57 mentions across 13 of the games counted). Jordan specifies; the audit informs. The nearest committed counterpart is `COMP-3` §7.9 and `THR` ch. 3 |
| `SNAP:archives/audit/2026-06-04-attributes-derived-ners/02_COMPARATIVE.md` (+ `04_RECONCILED_MASTER.md`, `03_ADVERSARIAL.md`) | Attributes and derived stats against acclaimed games (CK3, Burning Wheel, Mount & Blade, Disco Elysium, Battle Brothers, SaGa); records the games Valoria's canon names as its own referents |
| `SNAP:archives/audit/2026-06-22-massbattle-wiring-historical/wiring_historical_validation.md`; `…/2026-06-20-massbattle-loose-ends/massbattle_loose_ends_resolution.md` | Wiring stress test plus top-down comparison with cited historical analyses (Cannae, Napoleon, du Picq, Lanchester) |
| `SNAP:tests/sim/sim_mb_06_v9_historical_spec.md`; `SNAP:tests/sim/audit_sim_mb_06_v14.md` | Historical accuracy specification for formation-matchup bands (Cannae, Crécy, Agincourt, Hastings); a tick-by-tick audit against pre-firearms precedent **and** strategy-game precedent (Total War, Mount & Blade, Battle Brothers) |
| `SNAP:tests/sim/weapon_system_v2/weapon_v2_audit_2026-05-14.md`, `weapon_v2_complete_audit.md` | Weapon-system audit against historical precedent (HEMA, Liechtenauer, Fiore) — the earlier layer of the `.audit` weapon-morphology files in §2.B |
| `SNAP:tests/sim/mass_battle/{orchestration,config,validators}.py` | The mass-battle simulator with its historical constants and validators (48, 9 and 17 historical-term mentions); current counterparts under `modules/mass_battle/` |
| `SNAP:archives/audit/2026-04-29-topographic-analysis/`, `…/2026-04-30-terminology-vector-audit/`, `…/2026-06-22-faction-action-audit/`, `…/2026-06-09-*-comprehensive/` | Corpus-structure audits and per-subsystem analyses. Not precedent research; listed so they are not mistaken for it |

---

## 3. By function — what each function has, and where

`G` = game precedent · `H` = historical · `Plan` = state-index handles (`workplans/valoria_master_workplan_v9.md` §3) whose subject is evident from their row. A blank cell means none located by the commands in §9.

| function (lane) | G | H | Plan |
|---|---|---|---|
| **Faction strategy** (FA) | `COMP-1` §2.1, `COMP-5` §12.1, `COMP-3` §7.1: Victoria 3 clout, CK3 crown authority, Old World, John Company, Kremlin; `02_against_precedent` §2 re-score | `GOV` (all three themes), `CGR`, `FASE` T1/T5/T9/T10, `PGS` §2D, `RTP` | FA-01, FA-04…FA-07, IN-27, IN-30 |
| **Deliberation and law** (SC) | `COMP-1` §2.2, `COMP-5` §12.2, `COMP-6` §13.1 (Victoria 3 law enactment) and §13.2 (*Duel of Wits*), `COMP-3` §7.2; `VCD` App. B families 6–15 | `RHET` §7–§8; `GOV` (HRE Diet, Venice, Roman Republic); `PA` | SC-01 (the contest-resolution core of the proceedings subsystem), SC-03b (`determine` contested, `VCD` §10.4 step 4); the SC lane is SC-01…SC-08 |
| **Settlement governance** (SE) | `COMP-1` §2.3, `COMP-5` §12.3, `COMP-3` §7.3 (the appointed governor, null N-7) | `FASE` T4/T5/T8, `PGS` §2A–2B, `HCC` §2, `GOV` | SE-03…SE-06, IN-07, IN-28, IN-31, IN-49 |
| **Territory and conquest** (SE/FA/MB) | `COMP-1` §2.4, `COMP-5` §12.4, `COMP-3` §7.4 | `PW` §4–§5, `PA` §2/§4, `FASE` T6, `PGS` §2C | IN-13 (`VCD` §10.4 step 8, the `march` arrival); IN-12 (steps 6, 7, 11: `seize`, `covenant`, `raze`) |
| **People: roster, loyalty, succession** (FA/IN) | `SNAP:…/2026-06-04-attributes-derived-ners/02_COMPARATIVE.md` (attributes); `COMP-1` §2.5, `COMP-5` §12.5, `COMP-7`, `COMP-8`, `PMM`, `COMP-3` §7.5 | `RTP` A–J, `GOV` hierarchy and standing, `FASE` T5/T9 | IN-58, IN-61, IN-62…IN-72, SE-04 |
| **Economy, levy, muster** (SE/MB) | `COMP-1` §2.6, `COMP-5` §12.6, `COMP-6` §13.3 (CK3 levies), `PMM`, `COMP-3` §7.6 | `PW` §3, `FASE` T1–T3, `HCC` §2.9–2.10 | IN-33, IN-45, IN-52 |
| **Mass battle** (MB) | `COMP-1` §2.7, `COMP-5` §12.7, `COMP-3` §7.7; squad-engagement concept v5 (Football Manager, Total War) | `PFF` (all), `PW` §1–§2, `MBG`, `research/diagrams/…`, the `.audit` fidelity and Cannae audits; `SNAP:tests/sim/sim_mb_06_v9_historical_spec.md`, `audit_sim_mb_06_v14.md`, `SNAP:…/2026-06-22-massbattle-wiring-historical/` | MB-07r, MB-08, IN-13, IN-36, IN-52 |
| **Personal combat** (PC) | `COMP-1` §2.7 (the seam only); `proposals/2026-09-30-character-and-play-surface/04_the_bout.md`, `05_two_modes_of_one_bout.md` | **Not under `research/`.** `.audit` HEMA fact files, morphology and weapon-physics (§2.B); `SNAP:tests/sim/weapon_system_v2/` audits | PC-05, PC-06, PC-08, PC-10, GO-05 |
| **Cross-scale and auto-resolve** | `COMP-1` §2.8, `COMP-2` S3, `COMP-6` §13.6 (Total War autoresolve), `COMP-3` §7.8; `THR` ch. 3; `auto_manual_resolution_duality_v1.md` (`.designs/`) | `XSC` §8 (internal) | |
| **Social contest, persuasion, negotiation** (SC) | `COMP-1` §2.10–2.11, `COMP-6` §13.2, `COMP-3` §7.10; `SC-SRC` 01/04/05 | `RHET` (whole) | IN-12 (step 9, `argue`), SC-01 |
| **Investigation and fieldwork** (FI) | `VCD` App. B families 1–5 and 11 (seven detective games); the fieldwork architecture proposal | Incidental only: the coroner's view, Walsingham's cipher secretary, the State Inquisitors, the *ordo iudiciarius* appear as `VCD` evidence rows (`[H1-…]`). **No file under `research/` is dedicated to it** | FI-01…FI-05 |
| **Emergence, events, narration** (WR/IN) | `COMP-1` §2.9, `COMP-5` §12.10, `COMP-2` §3.3 failure shapes; `EMG`; `THR` ch. 1/4/5; `PREC-NULLS` N-2, N-5; `proposals/2026-09-12-emergent-narrative-primitives-v2/`; `proposals/2026-10-04-forcing-churn-and-the-story-bar.md`; `proposals/2026-10-13-narration-mechanisms.md` | `HCC` (event-deck source, §3 ripple chains) | IN-35, IN-37, WR-01 |
| **Resolution kernel** | `SNAP:…/2026-05-28-engine-replacement/engine_replacement_audit.md` (the d10 engine against acclaimed games, per system); `COMP-3` §7.9, `THR` ch. 3, `COMP-6` §13.2/§13.6 | `MBG` §1 (decisiveness and draw rate near parity, from the combat-modelling literature) | |
| **Threadwork** (WR/FI) | None. Named in `PA` and `PFF/16` as a system tested against history, not surveyed | | IN-06, WR-01 |
| **Godot port** (GO) | None located | | GO-01, GO-05, GO-06 |
| **Presentation / UI** | the three `valoria_ui_ux_v4*` documents (`.designs/`); `COMP-5` §12.10 | | no lane |

---

## 4. By verb — the 44, in the groups of `VCD` §3.2

`VCD` is the verb-keyed interrogation that already exists: §3.4 gives each verb its REACH and NOT; §4 its hook; §6.3 and §6.7 each verb against the two surveys; App. A the full row; **App. B the 63 act families with their evidence**, citing game acts, repo documents and historical procedures by extraction id (`[G1-…]` detective games, `[G2-…]` CK3 and RoTK, `[H1-…]` governance history, `[R1-…]` `research/`, `[P1-…]`/`[P2-…]` proposals, `[C-…]` code demand). Its class tally at HEAD: COVERED 31 · WIDENED 6 · GAP 10 · DEFERRED 7 · OUTCOME 4 · SYSTEM 5 (of 63).

| group | verbs | `VCD` App. B families (class) | research that stands behind them | plan handle (`VCD` §10.4 step) |
|---|---|---|---|---|
| G1 Personal combat | `fight` | 55 challenge/accept · 58 combat moves · 48 murder | HEMA fact files (`.audit`, §2.B); `COMP-1` §2.7 | PC-10 (duel terms and the yield) |
| G2 Mass battle | `march` | 23 muster · 24 siege · 25 conquer | `PFF`, `PW`, `MBG`; `COMP-6` §13.3 | IN-13 (step 8, the arrival) |
| G3 Social contest | `tell`, `argue` (suite) | 37 slander (deferred) · 38 persuade (GAP) · 59 negotiation moves (SYSTEM) | `RHET`; `COMP-6` §13.2; `SC-SRC` | IN-12 (step 9, `argue`); IN-18 (step 2a, the `tell` widening) |
| G4 Proceedings | `carry`, `convene`, `determine`, `open_case` | 6–9 accuse, inquiry, summons, trial · 50 mediate/appeal | `RHET` §7; `GOV` (Venetian councils, church justice); `COMP-6` §13.1 | SC-03b (step 4, `determine` contested); SC-01; IN-45 (`carry`) |
| G5 Writ answers | `comply`, `construe`, `dispatch`, `evade / defy` | 8 summons and writs | `GOV`; `PA` | IN-09 (`evade / defy`, `construe`) |
| G6 Documents | `create_record`, `destroy_record`, `forge`, `give`, `issue`, `petition`, `survey`, `conceal` (suite) | 8 · 33 expose · 34 blackmail · 42 survey/census · 32 cover identity (GAP) | `GOV`; `FASE` T4 | IN-12 (step 10, `conceal`); IN-45 (`forge`) |
| G7 Seats and bonds | `commit`, `confer`, `establish`, `oblige`, `release`, `repudiate`, `revoke`, `succeed`, `tie / knot` | 14 motion/vote · 15 elect · 16 appoint · 17 depose · 18 resign · 19 heir/regency · 20 homage · 36 marry · 51 recognize · 53 admit/expel · 57 regency | `RTP`; `GOV` hierarchy; `FASE` T9; `COMP-1` §2.5, §2.2 | IN-61 (`succeed`); IN-12 |
| G8 Matter | `exchange`, `levy`, `transfer` | 35 bribe · 39 trade · 40 borrow (deferred) | `FASE` T1–T3; `PW` §3; `COMP-6` §13.3 | IN-33 (`exchange`) |
| G9 Ground and fabric | `build`, `found`, `restore`, `work`; `raze`, `sabotage` (suite) | 41 build · 52 damage/raze (GAP) | `PGS` §2A; `HCC` §2.3–2.5 | IN-12 (steps 9, 11: `sabotage`, `raze`); IN-45 (`work`) |
| G10 Movement | `migrate`, `move` | — | `FASE` T8; `PGS` | IN-45 (`migrate`) |
| G11 Findings | `examine`, `interview`, `reconstruct`, `research`, `surveil`, `thread_read` | 1–5 question, inspect, decipher, watch/tail (deferred), evidence board | the seven detective games; no corpus under `research/` | IN-06 (`thread_read`); FI-01…FI-05 |
| G12 Free speech acts | `speak`, `utter` | 14 · 21 declare war | `RHET`; `COMP-6` §13.1 | no open row (`utter` is step 2); IN-10 is the step-1 enabler it reads |
| G13 Law and custody | `arrest`, `interrogate`, `pardon`, `seize` (suite) | 26 arrest, bail, ransom · 27 interrogate (GAP) · 28 execute (OUTCOME) · 29 outlaw · 30 seize · 62 steal (deferred) | `RHET` §7; `GOV` conflicts | IN-12 (steps 5, 5a, 6) |
| G14 Polity instruments | `covenant` (suite; `proclaim` deferred) | 13 edict (deferred) · 21–22 war, truce, treaty · 43 envoy | `GOV`; `CGR`; `COMP-1` §2.11 | IN-12 (step 7, `covenant`) |
| G15 The person | `tend`, `train`, `forgive` (suite) | 45 heal · 46 train · 63 feud and grudge (GAP) | `COMP-7` §14; `PMM` | IN-12 (steps 9, 13: `tend`, `train`, `forgive`) |

Families with no verb by design: 60 events and 61 inner mechanics (SYSTEM), 47 thread operations (deferred to plan positions 27/29f per `VCD`), 56 privileged counsel (SYSTEM).

---

## 5. By primitive — the vocabularies already in the corpus

| vocabulary | where | what it classifies |
|---|---|---|
| **Slices** — primitive (stores state) · derivative (computed) · formula · mechanic (one resolution event) · process (several mechanics on a clock) | `COMP-6` head; `SIM-1` §2 | any mechanic, in Valoria's own terms so a precedent row and a Valoria row sit in one schema |
| **Resolution shapes** — U unopposed · SO statically opposed · DO dynamically opposed · BI bilateral (both outcomes bind) · GATE (deterministic, no roll) | `COMP-6` head; `XSC` | how an act resolves. `GATE` was added by `COMP-6`; it is itself a finding (`COMP-6` §13.7) |
| **Political primitives** P1–P45 in seven families → 14 mechanisms + 31 configurations | `SC-SRC` 01, 03 | political and persuasion mechanics, each required to appear in two independent systems |
| **Survey primitives** P1–P58 (families A–K) and F01–F84 (sets A–K, one fact's journey from event to new event) | **not committed**; mapped to the verbs in `VCD` §6.2 and §6.6 | investigative, narrative and strategy-game acts. `VCD` §6.1–6.8 writes out each point it relies on |
| **Act families** 1–63 | `VCD` App. B | acts, by evidence |
| **Failure shapes** A–E | `COMP-2` §3.3, `THR` `08_ch5` | five shapes in which shipped mechanisms failed; the detector for each is named there |
| **Formation vocabulary** — grand formation, unit formation, unit, strategy, tactic; per-formation entry (composition, geometry, equipment, role, context, vulnerabilities, engagements, throughline flags) | `PFF` `00_MANIFEST.md` | mass-battle primitives |
| **Design hooks** — one `=> Valoria design hook` per historical pattern, plus consolidated tables | `GOV` (each theme file), `RTP` §3, `PGS` §3–4, `HCC` §4–5, `FASE` STEP 3 | historical pattern → proposed mechanic |
| **Rhetorical primitives** — stasis × genre; Nyāya self-gating obstruction; ethos as a tracker | `RHET` §9 | persuasion, as ratified into the contest redesign (CR4, CR5, per `RHET` §0) |
| **Executable roster** — 44 verbs, write matrix, rosters | `engine/season/verb_table.yaml`, `rosters.yaml` | what the code does; the only primitive list that is a mechanism |

---

## 6. The plan set against the research

The workplan is `workplans/valoria_master_workplan_v9.md` and `_part2`…`_part8` (RATIFIED, ED-IN-0286). State-index rows by lane, as the file stands at `462c68a` (`STATE`: B buildable · BLK blocked · J decision owed · LEAVE unscheduled):

| lane | rows | state mix | function(s) | research reach (§3) |
|---|---|---|---|---|
| IN | 42 | B 21 · BLK 19 · ask-then 1 · J 1 | cross-cutting: verbs, cast and goals, forcing, threadwork | deepest: `VCD` |
| SC | 8 | BLK 6 · ask-then 2 | deliberation, social contest | `COMP`, `RHET`, `SC-SRC` |
| SE | 5 | B 2 · BLK 2 · J 1 | settlement governance, populace | `COMP`, `FASE`, `PGS`, `GOV` |
| FA | 7 | B 4 · LEAVE 2 · — 1 | faction strategy, goals | `COMP`, `GOV`, `CGR`, `RTP` |
| PC | 4 | B 1 · BLK 2 · LEAVE 1 | personal combat | `.audit` HEMA files only |
| MB | 2 | BLK 1 · LEAVE 1 | mass battle | `PFF`, `PW`, `MBG` |
| FI | 4 | BLK 3 · — 1 | investigation | `VCD` App. B 1–5 only |
| WR | 2 | BLK 1 · — 1 | world events, threadwork | `HCC` |
| GO | 3 | BLK 2 · J 1 | port | none |

**What the measurements say about how the plan reaches the research** (commands in §9):

1. **No workplan part cites any `research/` document.** Twelve distinct research-document name patterns (`GOV`, `FASE`, `HCC`, `PGS`, `RTP`, `RHET`, `COMP`, `PMM`, `XSC`, …) return zero across all eight parts. The single `research/` string (`_part8`, a rewrite caveat) is not a citation.
2. **The plan reaches precedent through three proposals only:** `VCD` (parts 1, 2, 5, 6, 7, 8), `02_against_precedent.md` (parts 5, 6) and the proceedings subsystem (parts 5, 6, 8). `EMG` and the `THR` chapters are cited by no plan part by name.
3. **The mass-battle and historical research is consumed by code, not by the plan.** `PFF`, `PW` and `MBG` carry the most historical material in the tree; no plan part mentions Cannae, the formations corpus or the gauge grounding, yet `modules/mass_battle/config.py` and `tests/sim/gauge_mb.py` read it (§2.D). MB's two open rows (`MB-07r`, `MB-08`) name a recalibration and a leave-unscheduled item, not a research source.
4. **Personal combat's evidence is entirely in `.audit/`**, the tree with a rule that nothing outside it loads anything inside it. The plan's PC rows cite `#445` and ED ids, not the fact files.
5. **The governance research reached the season loop once**: hole-register row `H-100`, after Jordan pointed at `GOV` (2026-09-02). Its roster was deleted unread (§1 rule 1).
6. **Investigation is the one function whose precedent is detective *games* only**, held in `VCD`, a proposal. FI's four rows rest on it.

---

## 7. What the corpus does not cover

Stated so an "absence" in an interrogation is not mistaken for a finding about the game. Each was checked by the command in §9, not assumed.

- **No game or historical source for threadwork or the Godot port.** Threadwork appears in `PA` and `PFF/16` as a system tested against history.
- **Byzantium** is absent from `GOV` (agent interrupted) and present in `CGR` and `RHET` §2.
- **Tactics Ogre** was surveyed and produced no finding that survived (`COMP-1` §1.1).
- **The two surveys behind the 58 and 84 primitives are not in the repository** (`VCD` §1). Their points survive only as `VCD` carries them, and the "session documents" they cite (N1, N2, D1–D3, *The Third Strand*, *A Tells B About C*) are pinned by hash at `proposals/2026-09-12-emergent-narrative-primitives-v2/04_PROVENANCE.md`, not stored.
- **The seven nulls** (`COMP-2` §3.4): no game models argument content; none solves personal leverage across mass sizes; none has a general expression channel for interior state; none certifies generated content is good rather than varied; none defends a cross-scale bridge whose default state equals its absence; none caps unit *quality* by a faction scalar (4/4 franchises cap quantity); every franchise resolves non-payment as permanent desertion, where both Valoria options are recoverable. `PREC-NULLS` adds the legibility-against-depth null, fog of war for social state, and the appointed governor.
- **Numbers about games are leads** (§1 rule 2). `[UNVERIFIED]` marks persist at source: Dominions assassination meta, the *Duel of Wits* 21-versus-11 account, the Blades failure corpus, the State Inquisitors' watching of envoys.
- **The two older refs add little research.** `ARCH:research/` is wholly contained in the current tree, and `SNAP:references/historical/` is the same three files. What exists only at `SNAP:` is the earlier precedent comparison of the engine and of attributes (§2.E), whose conclusions the companion and `THR` re-derived from different programs.
- **Mention counts overstate games named in passing.** *Old World* is also a phrase in the pre-Columbian files; *Diplomacy* and *Civilization* are not counted because the word is ordinary.

---

## 8. Path translation — what the citations inside these files resolve to

Research files cite the tree as it stood before the restructure. Where the target exists today:

| cited as | is now |
|---|---|
| `designs/audit/<x>` and `audit/<x>` | `.audit/<x>` (a prefix **replace**; `QUARANTINE_MIRRORS` in `tools/ci_claim_provenance_check.py`) |
| `designs/audit/2026-07-08-fa-se-historical-precedent-research/` | `FASE` |
| `designs/audit/2026-07-09-comparative-governance-research/` | `CGR` |
| `designs/audit/2026-07-10-historical-concerns-action-catalogue/` | `HCC` |
| `references/historical/…` and `research/historical_precedents_analysis.md` | `research/historical/…` (`PA`, `PW`, `MBG`) |
| `systems/<sub>/reference/<x>.md` | `.designs/systems/<sub>/reference/<x>.md` (a prefix **prepend**) — read as reference, never authority |
| `sim/…`, `designs/…` | dissolved; `python tools/pathres.py` and `references/restructure_ledger.md` say where each went |

---

## 9. How to re-read this index

```sh
git ls-files research | wc -l                                              # the research tree
git grep -lE 'Crusader Kings|Victoria 3|Dwarf Fortress|Burning Wheel|Pentiment|Total War' -- . ':!registers/archive'   # where games are named
git grep -cE 'Cannae|Crécy|Byzantin|Venice|Ottoman|Carolingian|Mamluk' -- . ':!registers/archive' ':!.audit' ':!.designs'  # where history is drawn on
git grep -nE 'research/' -- workplans                                      # the plan's citations of research (§6, items 1–2)
git grep -nE 'mass_battle_gauge_grounding' -- tests modules                # code that consumes it (§2.D)
python tools/pathres.py                                                    # old path -> current
python -m engine.season.harness.register --requirements                    # whether any of it runs
```

A function absent from §3's `G` or `H` column was not found by these commands; run the matching search over a
new name before treating the absence as real (CLAUDE.md §0.1 pt 3).
