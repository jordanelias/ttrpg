# IN — infrastructure and cross-cutting: historical research, game precedent and repository work, critically evaluated

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · a critical evaluation; resolves nothing at runtime
## Date: 2026-10-16 · HEAD as stated in the opening note · Lane: IN

Read at HEAD `021fd96` (2026-10-16). Key: [CHECKED] = opened in the tree by this lane; [READER] = taken from the named
extraction in `scratchpad/out/`. Short names as in `research/00_INDEX.md` §1 key (`VCD` = `proposals/2026-10-03-verb-coverage-and-gap-fill.md`,
`#457` = `proposals/2026-10-04-forcing-churn-and-the-story-bar.md`, `COMP-n`, `SIM-n`, `PMM`, `XSC`, `GOV`, `RTP`, `FASE`, `HCC`, `PGS`, `RHET`,
`PA`, `PW`, `MBG`, `THR`, `PREC-NULLS`, `EMG`). `v9` = `workplans/valoria_master_workplan_v9.md`; `p2`…`p8` its parts. "VT" = the live verb
table `engine/season/verb_table.yaml`; "HR" = `engine/season/hole_register.yaml`. "<LANE> synth §n" = a sibling synthesis file
in `scratchpad/synth/`, cited only for a check that lane marked [CHECKED]; not re-verified here unless also marked [CHECKED].

## 0. VERDICT

**IN's repository work is grounded in Layer 1, Jordan's rulings and its own measurements, not in research: Layer 1's derivation excluded
`research/` by stated rule while the season loop's data owners admit it only as tier-3 reference, the plan cites no research document, and of
the 45 live verb rows none takes its shape from evidence that code carries (0 GROUNDED, 18 PARTLY through `VCD`'s name-level mapping or an
uncited convergence, 18 UNGROUNDED, 9 UNREACHED, 0 CONTRADICTED; §4.2).**

Problems, worst first:

1. **Layer 1's architecture documents exclude research by stated rule** ("Nothing under `canon/`, `systems/` or `research/` is authority here …
   prior work is not a constraint") [CHECKED `01_AXIOMS.md`:1173-1176, a rule scoped to Part E, "the Part that broke it"; `04_CODE_ARCHITECTURE.md`:6;
   `holonic_ARCHITECTURE.md`:12-15]. The season loop's data owners do not: `rosters.yaml`:75-78 and HR:1942-1944 admit `research/` as tier 3
   on Jordan's direction ("research/ contains useful information to make everything more robust") [CHECKED]. Precedent entered Layer 1 only by
   inheritance: the admissible chain (#337→#357 in `01_AXIOMS.md`:1174; #337→#352 in `holonic_ARCHITECTURE.md`:13) includes the from-scratch and
   ideal suites, which applied the companion's refusals (no second resolver, on-demand population, unreachable bands) [READER C6_1 §G; C6_2 §G],
   uncited in Layer 1 itself.
2. **The research that bears on IN's scheduled work is unread where it matters**: `RTP`/`GOV` for cast, goals and succession (IN-58…IN-72,
   IN-61); `FASE` T1–T3 and X4 for the levy feed (IN-49, IN-52); `PW`/`PA` for `march` arrival and occupation (IN-13); `HCC` for forcing
   (IN-35, IN-36); `RHET` for `tell`/`argue`/`speak` (§4.5).
3. **The kernel's season-loop inputs are defaults with no stated source**: `leverage=0.0` [CHECKED `sigma.py`:147]; `Person.capability` is empty on
   429 of 430 corpus persons (NPC-088's `{copying: 3}` the exception), so `_pool_of` returns `pool_default` (2) for those 429 [CHECKED
   `requirements.yaml`:1246-1250, :1284-1287, which records `sigma.py`:101-102's "EMPTY ON EVERY CORPUS PERSON TODAY" as contradicted by the
   tree]. Pool 2 vs Ob 2 gives Failure 74 / Partial 19 / Success 7 / Overwhelming 0 as a computed band split, not a measurement [CHECKED
   `proposals/2026-09-12-emergent-narrative-primitives-v2/04_PROVENANCE.md`:114-115]; the measured tellings are 24 told (Success 6, Partial 18)
   against 29 untold [CHECKED `requirements.yaml`:1240]. No research or precedent sets either input.
4. **Cast loyalty is a static cosine** where every loyalty precedent in the corpus is a moving quantity (NPC synth §0 item 1).
5. **The one research-to-design path (H-100 → IN-31) rests on a reverted carrier and keys cost on a different variable** than the research's
   (conferral basis vs how the seat was won) [CHECKED HR:1942-1960; `in31…md`:176-177; READER C4_2].
6. **Which verbs fire depends on which world is read, and `march`'s realm record conflicts with itself.** 17 of 45 execute in the 143-case
   corpus [CHECKED `test_season_shape.py`:7738-7740]; the realm reading at tree `23bea9da` adds `convene` 12/2, `determine` 20/1, `dispatch`
   86/16, `open_case` 28/7, `survey` 165/10 and `march` 16/16 att/ex [CHECKED `requirements.yaml`:731-734], while :1124 (2026-09-30) records all 11
   `march` attempts refused and HR:3264-3265 "the realm fights no field at all yet" [CHECKED]; :116-131 records `march` executing in `aperture 1 0`
   (H-175) [CHECKED].
7. **The relaxed exit (RULED 2026-10-13) decouples a position's BUILT from realm execution**; computed play is still read at the requirement
   level ("It relaxes a POSITION's exit, not a requirement's `met`: R-04's and R-05's `met` still read computed play") [CHECKED v9:132-135], but
   that sentence is itself marked [ASSUMPTION; medium] (:134). `#445` P-2 (scarcity with a reachability bar and control arm) maps to IN-22 [CHECKED
   v9:363, :368], whose reach, paying half and live arm landed [CHECKED `_part5`:191; `_part3`:213]; whether IN-22 carries P-2's control arm was
   not checked.
8. **The game-precedent corpus is weaker than its verdicts**: dropped [UNVERIFIED] marks, inflated convergence counts, a self-contradicting
   null, an unsourced null file contradicted by documented precedent, verdicts judged on the retired driver [READER R4 §K, R8 §K].
9. **Internal count and state drift in the plan and data**: contested verbs 3 vs 4, VERB_TABLE pinned 46 vs 45, IN-14 and IN-06 batch gates
   stated three ways, RR-A vs J-2 on the response verbs, P-1 mapped to IN-08 (v9:363) and to IN-18 G1 / IN-13 (`_part8`:207), `restore` read as
   Mending pending a carrier that does not exist (§3.3).
10. **`CURRENT.md`'s IN-adjacent rows name quarantined documents in a column labelled "Head"** (scale transitions, player agency, articulation,
   NPC behaviour, holonic doctrine, propagation, narrative engine, decision policy; `CURRENT.md`:29-35, :40), several built on the retired Key
   substrate [READER A7_1, A7_2, C4_2]. The index declares such rows "reference, not a head" [CHECKED `CURRENT.md`:13], as CLAUDE.md §1 sanctions;
   the defect is the column label, not misdirection.

Solid: the measurement discipline in `engine/season/` (regressions pinned and recorded, invented numbers swept, 2 of 198 HR rows honestly
tier-3) and the one convergence the plan honours — one resolver at several fidelities (FM/XCOM vs Total War; SM-5, IN-46) — is grounded.
`VCD` is a real verb-keyed interrogation with an independent read-only audit; its weakness is tertiary sourcing, not method.

## 1. HISTORICAL RESEARCH

IN owns no historical corpus of its own. What bears on its functions (the kernel, the verb table, the roster and cast, forcing and
endings, scale transitions, the plan) is borrowed from corpora filed for other lanes, or carried inside `VCD` as an extraction.

### 1.1 Sources table

| path | what it is | status and method as stated | reliability finding |
|---|---|---|---|
| `VCD` §4–§6, App. B, governance-history extraction (189 acts, cited `[H1-nn]`) | Procedure step by step: parliaments, royal writ/edict/homage/*diffidatio*/pardon/regency, Venetian councils, church justice and inquisition, secular warrant/arrest/bail/*habeas corpus*, intelligence. The only historical material the plan reaches, and only through `VCD` | RATIFIED AS INTENT (ED-IN-0288); "History rows rest on secondary summaries (mostly Wikipedia) read by an extraction pass" [CHECKED `VCD`:157-160]; extraction "built partly from headings and greps, not full reads" [CHECKED :148] | Tertiary sourcing, read by a model, no per-row verifier; the extraction table itself is not committed (the `[H1-nn]` ids occur in no other tracked file) [CHECKED `git grep 'H1-160'`; `VCD`:4457-4486]. Adequate for *naming* procedures; not evidence for any parameter. [UNVERIFIED] marks kept on State Inquisitors, Venetian details, tanistry [READER C8_2 §H] |
| `research/governance/political_hierarchy_standing.md` (`GOV`) | Rank, standing, demotion across 8 civilizations; one `=> design hook` per pattern | RESEARCH 2026-07-14, ED-IN-0064; per-civ brief "adversarially verified", verifier note quoted per civ; Byzantium omitted from the pass [READER A9_2 §FILES; A9_1 line 16] | The only `research/` file that reached `engine/season/`: HR `H-100` cites it [CHECKED HR via YAML load: `H-99`, `H-100` are the only 2 of 198 rows naming `research/`]. Verifier notes in the sibling GOV files are cut mid-sentence in the source [READER A9_1 line 106] |
| `RTP` `research/rise_to_power_roster_system_research_v1.md` | How people rose: patronage, merit, kinship, favourites, capture, retinue, purges, factions, venality, religion; §3 roster proposal | FILED 2026-07-11 Lane IN; 31-agent workflow find → adversarial fact-check → distillation (Sonnet), Opus synthesis; "fact-check results not shown per entry" [READER R7 §FILES] | Unreached by the cast and goals positions (IN-62…IN-72) that implement the function it studies: no plan part names it [CHECKED `git grep -n 'research/' -- workplans` → one hit, `_part8`:170, a rewrite caveat] |
| `FASE` T1–T10 | Fiscal sociology, tax farming, charters, governor control, conquest terms, church–state, frontier, **interregna (T9), legitimacy theory (T10)** | FILED 2026-07-08; read-only pass; "no verifier stated; no sources fetched stated" [READER R6 §FILES] | Weakest-method corpus bearing on IN (no retrieval, no verifier) [READER R6 §K item 14]. T9/T10 bear on IN-23 (legitimacy Query) and IN-61 (succession); neither position cites it |
| `HCC` `research/historical_concerns_action_catalogue_v1.md` | Ten crisis categories, §3 ripple chains, an event-deck source | FILED 2026-07-10 Lane IN; 31-agent find → adversarial fact-check → distillation; Opus synthesis [READER R6 §FILES] | Ripple chains stack on proposal-only stats of `governance_play_redesign_v1` (tier 4 "IDEAS") unmarked; chain links over-reach (Chain 1 step 2) [READER R6 §K 2-3]. Bears on forcing (IN-35, IN-36, #457); unreached |
| `PGS` `research/proactive_governance_scale_research_v1.md` | Proactive levers at four scales; §4 reuse-vs-new-lever ledger | FILED 2026-07-11 Lane IN; same 31-agent method [READER R6 §FILES] | Six dangling cross-references; uses Key emission (retired, ED-IN-0232) [READER R6 §K 7-8]. Bears on R-04 management acts; unreached |
| `RHET` | Rhetoric, assemblies, trials, negotiation; stasis, Nyāya | RESEARCH 2026-06-02; web + primary-language scholarship; self-audit tiers; no independent verifier; §9 [SELF-AUTHORED] [READER R7 §FILES] | Strongest-sourced corpus touching an IN verb (`argue`, IN-12 step 9); reaches the old contest kernel (CR4/CR5 per `RHET` §0, index §5), not the season verb table |
| `PA`, `PW` | Theocracy, invasion in civil instability, occupation; Crécy, Agincourt, Cannae, Hastings, Austerlitz | ANALYSIS 2026-04-17; single author with self-audit [READER R3 §FILES] | Bear on `march`, `seize`, occupation (IN-12 step 6, IN-13); unreached by the plan; predate the season loop by five months |
| `MBG` §1 | Combat-modelling literature (Lanchester; Hillestad–Owen–Blumenthal 1995; Taylor; Armstrong–Sodergren 2015): draws expected near parity; decisive split metric | v2.4 2026-06-17; [SELF-AUTHORED — bias risk] [READER R3 line 8, 39] | The nearest thing to historical grounding for the resolution kernel. Bands were raised after engine output (C5 90→98, C7 90→100); C7 saturates by construction [READER R3 §K 1-2]. It grounds the mass-battle gauge, not d10/TN 7/σ-leverage |
| `XSC`, `SIM-1…4`, `PMM` | Repository catalogues filed under `research/` (every action at every scale; 1,079 harvest records; personnel/muster) | XSC FILED 2026-08-27 "read from the working tree at f567c13"; SIM PROPOSED 2026-08-28 [READER R5 §FILES] | **Not historical research.** They describe the pre-season-loop tree (Key substrate, `mc_v18`, factions sim) and are stale against `engine/season/` (§3.3). Historical names they carry (Levy 1983, Tilly 1990, iltizam, publicani) are "cited by name, not a source examined" [READER R5 §T 8] |

### 1.2 Cases and patterns that bear on this lane

| case | period | what is claimed | the hook proposed | evidence marks and corrections | assessment | locator |
|---|---|---|---|---|---|---|
| Venetian lot-and-ballot, quorum (Senate 70), Council of Ten term limits | 13th–18th c. | Election, quorum and term-limit procedure | `confer` basis `elected` + members' `commit`s; quorum as `bench.size >= quorum` | secondary summaries; State Inquisitors [UNVERIFIED] | Sound as vocabulary; the quorum hook is a Query over holds that the code ships at `bench_quorum 1` (a fixture, not a sourced number) [READER B1_2 §P] | `VCD` App. B 14-15 [CHECKED :4470]; C8_2 §G |
| Church justice: denunciation, edict of grace (30–40 days), *Ad extirpanda* torture limits, relaxation to the secular arm (Lateran IV c.18), confiscation in thirds | 1215–16th c. | The step-by-step inquisitorial chain | "Active Inquisition" chain `utter`→`petition`→`give`→`open_case`→`issue`→`arrest`→`interrogate`→`determine`→`pardon` (§10.2) | secondary summaries | Over-claimed as grounding for verbs that do not exist: `arrest`, `interrogate`, `pardon` are absent from VT [CHECKED: 45 keys, none of the 12 IN-12 verbs]. The chain is a composition proposal, not a mechanism | C8_2 §V; `VCD`:1654, :2302 [CHECKED] |
| English constable, bail, *habeas corpus*, Act of Settlement pardon | medieval–1701 | Secular arrest and release | `arrest` (warrant-bound, contested), `pardon` (closes `detain`/`ban` only) | secondary | Unbuilt (IN-12 step 5, B-R); the `detain`/`ban` Tenure kinds exist in `rosters.yaml` tenure_kinds [READER B1_1 §P line 90] but nothing outside a `determine` disposal opens them | C8_1 §G; `VCD`:1736-1737 |
| Homage / *diffidatio* | feudal | Vassalage as a sworn bond, defiance as its breach | `oblige` read as vassalage by `purview_reaches` (H-101); `evade / defy` | etymology [UNVERIFIED] | `evade / defy` is in VT but its rows were reverted after 0 realm executions (IN-09) [READER W2 §V IN-09]; H-101 vassalage is "DERIVED, no stored parent [medium]" [READER W3 §F] | C8_1 L437; W2 §V |
| Seat provenance: "rank is only as solid as the currency backing it"; favour-derived seats face total ruin, kinship-derived get containment | 8 civs | Demotion severity keyed to how the seat was won | Six bases (bureaucratic, kinship, military, ideological, patronage, purchased) → two tier-3 rosters (`governance_modes`, `power_bases`), **built then deleted unread** | `GOV` verifier SOUND_WITH_FIXES; read at tier 3 | Sound research, correctly demoted. It reaches IN-31's design as vocabulary only: "It is tier 3: vocabulary, not authority" [CHECKED `proposals/2026-10-14-in31-revocation-cost-provenance.md`:176-177]. The one research-to-plan path in the tree runs through a hole row, not a citation | HR `H-100` [CHECKED :1942-1960]; `rosters.yaml`:84-89 [CHECKED] |
| Interregna and legitimacy theory (Weber, Ibn Khaldun) | — | Succession gaps and legitimacy as derived | ED-SE-0007 Weberian legitimacy table | FASE: no retrieval, no verifier | Superseded in the plan by IN-23's "legitimacy/stability Queries … no stored value" [READER W3 §G; W2 §F]. The Query keeps FASE's shape (derived, not stored) without citing it | W3 §G; R6 §FILES |
| Lanchester / combat-model draw rate near parity | 1914; 1979–2015 | Draws expected near parity; decisiveness metric | decisive split `decA = A/(A+B)`, separate `draw_exp` | [SELF-AUTHORED]; bands adjusted after emergent output | Sound literature, over-claimed calibration (bands moved toward engine output) [READER R3 §K 1]. Not a test of d10/TN 7; the kernel has no historical calibration target | R3 line 39 |
| Ming *piaoni*, Roman *relatio*/*senatus auctoritas* (recorded defeat), Byzantine Office-vs-Dignity | — | Drafting right; a vetoed motion persists as a citable record; holder ≠ controller | `COMP-2` steal #3, #12; convergence X1 | "survived the survey's own adversarial attack", no source cited [READER R4 §C, R8 §C line 55] | X1's "five independent systems" joins opposite splits (control vs holder, drafter vs signer); three of five are historical [READER R4 §K 10]. Recorded defeat reaches SC-07 (#445 P-4) as an attached item that "builds nothing" [READER W3 §V SC-07] | R4 §C; W3 SC-07 |

### 1.3 Critical evaluation of the historical research for this lane

1. **Method gradient.** The IN-touching corpora sort by method: `RHET` (primary-language, web, self-audit) > `GOV`, `RTP`, `HCC`, `PGS`
   (researcher → independent fact-checker, per entry) > `PA`, `PW`, `MBG` (single author, self-audit, [SELF-AUTHORED]) > `FASE` (no retrieval, no
   verifier) > `VCD`'s `[H1-nn]` rows (secondary summaries, "mostly Wikipedia", extraction table uncommitted). **The plan reaches only the
   bottom rung** (`VCD`), and reaches it as intent ("ratified AS INTENT … nothing they describe exists until built") [READER W2 banner line 6].
2. **No corpus is dedicated to the kernel, the season loop, the verb table or scale transitions.** The resolution kernel's only
   literature contact is `MBG` §1, which calibrates the mass-battle gauge, not d10/TN 7 [READER R3 line 39]. Index §3's "Resolution kernel H"
   cell is `MBG` §1 alone [CHECKED `research/00_INDEX.md`:172].
3. **Hooks ride retired or tier-4 apparatus.** `HCC` chains and `PGS` menus stack on `governance_play_redesign_v1` stats (tier 4,
   "IDEAS" [CHECKED `rosters.yaml`:79-80]) and on Key emission (retired) [READER R6 §K 2, 8]. Their hook columns describe a board-game layer that
   `engine/season/` does not have: no Pi, AP, Capital-Posture, Ledger tags, Fiscal Stance exists in `rosters.yaml` [READER B1_1 §P lists the 64 roster keys; none of these].
4. **The research that is sound did not need to be wrong to be dropped.** Two rosters (`governance_modes`, `power_bases`) were built from
   tier 3 and deleted because nothing read them ("They were not wrong; they were UNREAD") [CHECKED `rosters.yaml`:86-88]. That is the correct
   application of CLAUDE.md §0.1 pt 5, and these two rosters are the recorded instances of research being *tried* against the season loop.
5. **Anachronism and surface analogy.** The `VCD` history set is a vocabulary harvest: each procedure is mapped to an existing or
   proposed verb by name-likeness (denunciation → `utter` + `petition`; homage → `oblige`; outlawry → `determine` disposing `ban`). No row
   carries a parameter, a rate, or a failure from the source; none is used to reject a design. It is analogy, labelled as coverage
   ("COVERED"/"GAP"), not grounding.

## 2. GAME PRECEDENT

### 2.1 Sources table

| path | what it is | status and method as stated | reliability finding |
|---|---|---|---|
| `COMP-1`…`COMP-8` `research/valoria_game_precedent_companion_v1*.md` | Collation of three programs (political mechanics; personnel/muster; failure dossiers P1–P5): convergences X1–X8, nulls D1–D7, failure shapes A–E, complements K1–K9, synergies S1–S6, steal/refuse | PROPOSED 2026-08-28; "no precedent claim re-verified against source" (`COMP-2` §7) [READER R4 §FILES] | Marks dropped downstream (Duel of Wits 21-v-11, Dominions, V3 counter-mobilization, Blades corpus [UNVERIFIED] at source, unmarked in `COMP-2`…`COMP-5`) [READER R4 §K 7]; "independent programs" asserted while declared precedents descend from one un-audited source [R4 §K 11]; "six of eight, Valoria owns the primitive" contradicted by its own table [R4 §K 8]; `COMP-3` §7 verdicts judged the retired campaign driver [CHECKED index §1 rule 5]; Key substrate treated as live (retired, ED-IN-0232) [R4 §K 20] |
| `PMM` | Nine game passes, five personnel + four muster lanes | FILED 2026-08-27; first-person single author, no external verifier, six self-corrections [READER R4 §FILES] | Self-contradicts on the non-payment null (`PMM`:397-402 vs :511) [READER R4 §K 1; CHECKED index §7]; numbers cluster on two KOEI manuals |
| `THR` (`proposals/2026-08-25-throughlines-and-precedent/`), `S05` suite-05 | Failure dossiers: every recommended mechanism must arrive with a shipped precedent that failed while holding it; five failure shapes | PROPOSED 2026-08-25; Fable read lanes, Sonnet+web dossiers, Opus chapters, `valoria-critic`; 11 corrections, "none caught by producer re-reading" [READER R8 §FILES, §T 11] | The best-attacked precedent work in the tree; still internally inconsistent on the correction count (4 vs 11) and on whether the n≥100 oracle exists [READER R8 §K 1, 3]. URLs not re-verified (TL08 §10) |
| `PREC-NULLS` `proposals/_session_provenance/2026-08-29-to-31/PRECEDENT.md` | Nine nulls N-1…N-9 | No header, status, author, date or method [READER R8 §FILES] | Its "survived the survey's own adversarial pass" cites none; N-9 (no game ships an NPC acting on false information) is contradicted by `S05` §1.3's Talk of the Town (DOCUMENTED) and by `02_against_precedent` §3 [READER R8 §K 12, 18] |
| `EMG` `…/relay/G_EMERGENCE_PRECEDENT.md` | What stores story in CK, DF, RimWorld, Nemesis, Qud/URR, KoDP, Pentiment | REFERENCE 2026-09-06; Sonnet, web; Burning Wheel and Ars Magica "not freshly verified"; no verifier [READER R8 §FILES] | Its memory finding (memory works only when read at a decision point) is the one precedent claim that reached the season loop's design, but by convergence, not citation (regard-at-read, A-12) [READER W2 §V A-12]; not cited by any plan part [CHECKED index §6 item 2] |
| `proposals/2026-09-30-character-and-play-surface/02_against_precedent.md` (`#445` 02) | Re-score of `COMP-3` §7 against `engine/season/` at `c8cc408`; recommendations P-1…P-5 [CHECKED `02_against_precedent.md`:80-84] | PROPOSED 2026-09-30; no verifier; README RATIFIED AS INTENT for P-1, P-2, P-3 mechanism (ED-IN-0290) [READER C7_2 §FILES; R8 §FILES] | **The plan's only channel to the companion.** Its own verdict: "Finishing the plan consolidates the engine; it does not change this verdict" (below the floor on factions that act, procedure, relationships, scarcity) [CHECKED `02_against_precedent.md`:73] |
| `VCD` App. B game sets | Seven detective games (107 acts), CK3 + RoTK (107 acts) mapped to 63 act families | RATIFIED AS INTENT (ED-IN-0288); "Web facts about the games rest partly on search snippets"; many review sites 403; Paradox wiki pages would not load [CHECKED `VCD`:156-158] | Name-level evidence; several rows [UNVERIFIED] (Disco Elysium arrest, CK3 torture, Espiocracy) [READER C8_1 §G]; the two surveys behind P1–P58 and F01–F84 are not committed [CHECKED `VCD`:99-133 region via index §7] |
| `.designs/systems/_architecture/reference/auto_manual_resolution_duality_v1.md`, `player_agency_v30.md` | FM/Total War/CK/XCOM three fidelities; RoTK Officer Mode, CK3 Vassal Play as declared stance precedents | Quarantined ARCHIVED-NOT-CANON; duality "RULED 2026-07-08", fork C calibration open [READER A7_1 §FILES, §G] | Declared precedents never bound to a module (`COMP-7` §14.2) [READER R4 §C row "declared precedents"] |

### 2.2 Games and systems that bear on this lane

| game | what is borrowed or warned against | shape | evidence grade and sourcing | assessment | locator |
|---|---|---|---|---|---|
| Football Manager (three fidelities of one match engine) vs Total War auto-resolve (a second resolver, no calibration target) | "One engine, several entry points; the fast path must be the same engine run headless"; refuse #14 "a second resolver of any kind" | convergence (FM, XCOM) + failure shape C (TW) | manual quote / dossier; numbers unsourced [READER R4 §C, §T] | **Applied correctly and grounded in code.** SM-5 (Jordan: grid/Fire-Emblem bout and duel are two modes of one engine) and IN-46's "AUTOMATED and PLAYABLE replay-equal under 6 conditions" are the FM shape; `fight` routes to one duel engine via `seam/contest.py` [READER W1 §V p4 IN-46; C8_2 §V `fight`]. The calibration null (D4) does not arise because there is no second resolver | R4 §C; W1 p4 4.2 |
| Fire Emblem ("fire emblem style", Jordan's words) | Grid attack resolved by the personal combat engine for a round | precedent named by the owner | Jordan quote, not surveyed; `COMP` never surveyed it [READER S/05 §1.3 [UNVERIFIED] in C7_2 §G] | Owner intent, not evidence. Correctly marked as a ruling (SM-5 CONFIRMED) | W1 §G; W3 §G |
| EU4 estates ("a mechanism engineered not to fire is indistinguishable from one that does not exist"); Imperator loyalty | Failure shape A: detector = run maximum mitigation against maximum accrual; reachability bar + control arm | failure | dossier P1; links not re-verified [READER R8 §C] | **Detected at the requirement level, not at the position.** v9 §0.5 relaxed exit (RULED 2026-10-13): a verb is BUILT on a hand-built-world falsifier, "realm count recorded, not required" [READER W1 §F; W2 banner], so a position can close on a verb that never executes in computed play. The same bullet keeps the detector one level up: "It relaxes a POSITION's exit, not a requirement's `met`: R-04's and R-05's `met` still read computed play" [CHECKED v9:132-135], marked [ASSUMPTION; medium] (:134); R-05 cannot read `met` while any of IN-45's four verbs does not execute in computed play [CHECKED `_part5` IN-45 WHAT]; the executed set is pinned exactly and fails when it moves [CHECKED `test_season_shape.py`:7738-7742], and 21 → 17 is recorded as a regression with R-05 `not_met` [CHECKED `requirements.yaml`:901-905]. Positions reverted at B-I for 0 realm executions are "restorable from their checkpoints under this rule" [CHECKED v9:130-132]. `#445` P-2 is scarcity-specific (shortfalls > 0 at default fixtures, a control arm at today's yields) [CHECKED `02_against_precedent.md`:81], not a verb-execution bar; it maps to IN-22 [CHECKED v9:363], whose reach, paying half and live arm landed [CHECKED `_part5`:191; `_part3`:213]. Whether IN-22 carries P-2's control arm was not checked | R4 §C; W1 §F; CHECKED |
| Old World (goals = person × houses, expire on death); Kremlin (holder ≠ controller; politicians age) | Goals emitted by a person, not a faction; complement K6 | convergence (2 games) | no mark [READER R4 §C] | Reached the plan as `#445` P-3 → FA-01 (head acts via seat, landed B-J) [CHECKED v9:320]. IN-66…IN-68 (goals carrier, referents, seeding) implement "goals by person" but cite ED-IN-0293 and Jordan's words, not P-3 [READER W2 §V]. Expiry-on-death is not in IN-66…IN-68's text [READER W2 §F IN-66–68] | R4 §C; W2 |
| Kremlin, CK contracts, Ming *piaoni*, Byzantine Office/Dignity (X1 holder ≠ controller) | Who holds an office is separate from who controls the holder | convergence claimed "5 systems"; 3 of 5 historical; opposite splits joined [READER R4 §K 10] | Over-claimed convergence. Bears on IN-48 (regency, delegation without a hold), which was built and **reverted** for contradicting ratified Layer 1 (01_AXIOMS §E.2.4) [READER W2 §V IN-48]; no plan text cites X1 |
| Talk of the Town, Dwarf Fortress rumour, CK hooks | Fallible beliefs with provenance; rumour carriage | convergence vs null N-9 | S05 DOCUMENTED vs PRE unsourced [READER R8 §K 12] | The season loop already ships held-not-true claims, `told_by` chains, Partial-band lossy `tell` [READER B2_2 §F H-155, H-157; C3_1 §F 02 §A.10]. PREC-NULLS N-9 is wrong about the genre or about Valoria; either way it is not a null to cite |
| Nemesis, Dwarf Fortress, Wildermyth (tracking ≠ expressing; Tale-Spin effect) | Interior-state expression null (D6/N-2); "budget expression in the same milestone as the substrate" | null + failure shape D | literature + patent [READER R4 §C; R8 §C] | Unaddressed: IN-37 (chronicle render) is BLK on SC-01 step 16 [READER W1 §V]. M2 bar is a cause-graph property, not an expression channel. Shape D (substrate mistaken for game) is the live risk; `#445` 02 says so | R4 §T D6 |
| Blades in the Dark (P(fail) 50%→1.6% for N=1..6); PbtA middle band | Band-probability floor test (I-7); a complication band of ~41–45 % | failure shape B; arithmetic | figure is arithmetic, corpus unverified [READER R4 §K 7] | Bears on the kernel as wired in the season loop: σ-leverage passes `leverage=0.0` [CHECKED `engine/season/seam/wrappers/sigma.py`:147] and 429 of 430 corpus persons fall to `pool_default` (2) [CHECKED `requirements.yaml`:1246-1250]; pool 2 vs Ob 2 computes to FAILURE 74 / PARTIAL 19 / SUCCESS 7 / OVERWHELMING 0, labelled "[computed, exact]" [CHECKED ENP v2 `04_PROVENANCE.md`:114-115], while the measured tellings are 24 told (Success 6, Partial 18) against 29 untold [CHECKED `requirements.yaml`:1240]. The kernel's band shape is not at issue; its season-loop inputs are defaults. No precedent was used to set `pool_default` | C7_1; CHECKED |
| CK3 population ("generate on demand, not on a clock") | Refuse #13 | refusal | community-derived [READER R4 §C] | Consistent with the tree: "the cast is the 46, no season-tick generation, cast only shrinks" (ED-WR-0011) [READER C3_2 §H]; IN-34 ageing/illness ships `age_step 0`, `illness_rate 0.0` [READER B2_2 §P H-208] |
| Seven detective games (*Pentiment, Disco Elysium, Esoteric Ebb, Lacuna, L.A. Noire, Tails Noir, Shadows of Doubt*) | Act families 1–5, 26–27: question, inspect, read, watch, board, arrest, interrogate | coverage map | snippets; Pentiment Acts II–III trial not fetched [CHECKED `VCD`:156-160] | Name-level. Supports the six investigation verbs that exist in VT but write `[]` and emit `finding.made` with no degree [READER B1_2 §F "Six investigation acts"]. The games' defining mechanic (graded inquiry, contradiction of testimony) is the part not built (FI-01 BLK) |
| CK3, RoTK (107 acts) | War/truce, imprison/ransom/execute, schemes, sabotage, alliances | coverage map | Paradox wiki pages "would not load"; RoTK = Koei series [ASSUMPTION] [READER C8_1 §H] | Name-level; supports proposed verbs `arrest`, `seize`, `covenant`, `sabotage`, none in VT [CHECKED] |
| Republic of Rome (agenda control) | `carry`, `convene` as procedural power | precedent | board game, named [READER C8_1 §G] | `carry` is in VT with effect DECLINED (always NoOpReceipt, H-63) [READER B1_2 §F]; the precedent names a power the row cannot exercise |
| RimWorld, Guild 3, Bannerlord, Skyrim radiant (grudge loop/damping) | Feud spiral; need for a damper | failure | search snippets [READER C8_1 §G] | Informs `forgive` (IN-12 step 13, unbuilt) and K-45's recommended signed LOOP row, "not written" [READER C8_2 §H]. The grudge append per lost field has no bound today |

### 2.3 Critical evaluation of the game precedent for this lane

1. **The sourcing floor is honoured at source and lost downstream.** `COMP-1` states that fan wikis were bot-walled and figures are leads;
   by `COMP-2`…`COMP-5` four [UNVERIFIED] marks are gone [READER R4 §K 7]. `VCD` repeats the pattern: game facts from search snippets, 403s
   [CHECKED `VCD`:156-158]. No IN-lane decision rests on a game *number*, so the damage is confined to the precedent documents'
   own verdicts.
2. **Convergence counts are inflated.** "4/4 franchises" is three franchises (RoTK ×2) [R4 §K 6]; X1's "five independent systems" joins
   opposite splits [R4 §K 10]; independence of the three programs is asserted and undercut in the same volume [R4 §K 11].
3. **What the plan took, it took through one re-score.** `#445` 02 re-scored `COMP-3` on the season loop and produced P-1…P-5 [CHECKED
   `02_against_precedent.md`:80-84]. P-1 maps to IN-08 [CHECKED v9:363] and, in `_part8`:207, to IN-18 G1 / IN-13 as regard-at-read [CHECKED];
   P-2 → IN-22, P-3 → FA-01, P-4 → SC-07 (builds nothing) [CHECKED v9:363]. P-2 carries shape A's reachability bar and control arm, but for
   scarcity only (`SITE_YIELD`, subsistence fixtures; "shortfall events per season on the populated realm > 0") [CHECKED :81]; it is not a bar on
   verb execution. P-5 is a one-line pointer edit in `COMP-3` §7.11 [CHECKED :84]. The same document says finishing the plan does not change
   the below-floor verdict [CHECKED :73]; nothing in v9 contests that sentence.
4. **The strongest precedent finding the plan honours is "one resolver"** (FM/XCOM vs TW). It is honoured because Jordan ruled it (SM-5),
   not because the companion argued it; the two arrive at one shape independently, which is the evidence class the index ranks highest
   [CHECKED `research/00_INDEX.md`:30-32].
5. **Failure shape A is moved up a level, not ignored.** Under the relaxed exit (§2.2 EU4 row), "BUILT" and "fires in play" are separate
   claims at the position; the requirement level still reads computed play (R-04, R-05 `met`) and the executed-set pin fails when the set
   moves [CHECKED v9:132-135; `test_season_shape.py`:7738-7742]. The requirement-level reading is itself [ASSUMPTION; medium] in v9:134.
6. **Precedent did its real work a month before the plan, and lost its citations on the way.** The August from-scratch suite (PR #342,
   inside Layer 1's admissible chain, #337→#352 in `holonic_ARCHITECTURE.md`:13 and #337→#357 in `01_AXIOMS.md`:1174 [READER C6_3 abbrev line;
   CHECKED both]) applied the companion's
   refusals by name: Total War's second resolver, CK3's population tap, Dominions' commander anchor, EU4's unreachable bands, Duel of Wits
   [READER C6_1 §G; C6_2 §G]. Layer 1 kept the shapes and dropped the sources. The ED-874 d+σ faction regime cited "CK3/EU/KoDP" as its
   basis [READER G2 §G]; it is not the season loop's kernel.

## 3. REPOSITORY WORK

### 3.1 Heads and code: what runs, what the plan schedules, what the heads say

| object | what it is | status as stated | what was verified |
|---|---|---|---|
| Resolution kernel `engine/dice_engine/dice_engine.py`, `sigma_leverage.py` | d10, TN 7, μ 0.40 σ 0.80 per die, continuous Normal; `degree_from_net` four bands; σ-leverage μ-shift | `CURRENT.md` row "Dice / resolution: in code" [CHECKED `CURRENT.md`] | Exists [CHECKED `ls engine/dice_engine/`]. **In the season loop the leverage half is inert**: `seam/wrappers/sigma.py` passes `leverage=0.0` "until something supplies leverage" [CHECKED :139-147]. `_pool_of`'s docstring says capability is "EMPTY ON EVERY CORPUS PERSON TODAY" [CHECKED :101-102]; that is stale: `requirements.yaml`:1246-1250 measures it empty on 429 of 430 corpus persons (NPC-088's `{copying: 3}` the exception) and :1284-1287 records the older sentence as "CONTRADICTED BY THE TREE" [CHECKED]. Only `tell` reaches it [CHECKED `requirements.yaml`:109-112]. `CLAUDE.md` §5 names `engine/autoload/dice_engine.py`, which does not exist [CHECKED `ls engine/`] |
| Season loop `engine/season/` | CALENDAR → MATTER → rounds (DELIBERATE → RESOLVE → ENCOUNTER → WITNESS) → CENSUS; one `resolve` over the verb table | RATIFIED ED-IN-0204, Layer 2 [CHECKED `CURRENT.md`] | Runs; "IT RUNS AND IT IS NOT YET A GAME" (CLAUDE.md §3). THE NINE: R-01…R-03 met, R-04, R-06…R-09 partial, R-05 not_met [CHECKED YAML load of `requirements.yaml`] |
| Verb table `engine/season/verb_table.yaml` | 45 rows (VCD's 44 + `challenge`, `accept` − `repudiate`) | per-row `grade:` ruled / assumption / absent; grade "NOT validated at load" [READER B1_2 §H] | **45** [CHECKED `VERB_TABLE`]. Contested rows: 4 — `fight`, `accept` (the body), `march` (a field), `tell` (a standing) [CHECKED]; plan p8 C item 6 still says 3 [READER W3 §F]. Every row's `source:` is internal (ARCHITECTURE_V2 §E3 transcribed, ED rulings, workplans, quarantined `fieldwork_v30.md`); 5 rows name `#453`; **0 rows cite `research/` or any game** [CHECKED YAML scan + grep] |
| Executed set (corpus_run, 143 cases, seed 0, after IN-57) | 17 executed: `accept challenge create_record fight give interview issue move petition reconstruct release research speak surveil tell transfer utter`; 10 always refused: `build commit dispatch examine found levy migrate restore survey work`; 18 never attempted or no predicate | pinned in a test as a regression record (21 → 17 at IN-57) | [CHECKED `engine/season/tests/test_season_shape.py`:7738-7740 (the `ever` set; :7725-7731 is the IN-11/IN-57 note), :7834-7835 (always refused), :8668-8670 (never attempted); `requirements.yaml`:895-905]. Of the four contested verbs only `march` is outside the corpus executed set. **The realm is a different world**: at tree `23bea9da` it records att/ex `convene` 12/2, `determine` 20/1, `dispatch` 86/16, `open_case` 28/7, `survey` 165/10, `march` 16/16 [CHECKED `requirements.yaml`:731-734]; "17 of 45" is a corpus figure |
| Rosters, write matrix, hole register | `rosters.yaml` 64 rosters + 7 tables; `write_matrix.yaml` (kind, field) rows; HR **198 rows** | data code reads; HR read only by `register.py` [READER B2_1] | HR grades over all 198 rows: assumption 83, measured 48, absent 36, ruled 31; tier 0: 45, tier 1: 153 [CHECKED YAML load]. **2 of 198 rows cite `research/` (H-99, H-100); 0 name a game or historical case** (the single regex hit, "ck2" in H-172, is the substring of `w9_check2`) [CHECKED]. The extraction's half counts (131 + 67) reconcile to 198 [READER B2_1, B2_2; CHECKED] |
| Layer 1 `architecture/` | `holonic_ARCHITECTURE.md` (#353), `ARCHITECTURE_V2.md`, `meta/01`–`10` | RATIFIED 2026-09-05, ED-IN-0204 [CHECKED head] | **Research-excluding by stated rule, in its derivation**: "Nothing under `canon/`, `systems/` or `research/` is authority here. We are designing an idealized system; prior work is not a constraint" [CHECKED `01_AXIOMS.md`:1173-1176; scoped to Part E, "the rule this document broke once and now states at the top of the Part that broke it", with the chain #337→#357]; "Nothing under `canon/`, `systems/`, `research/` or `engine/` was read" [CHECKED `04_CODE_ARCHITECTURE.md`:6]; "no decision ratified before #337 is authority — not as support, not as precedent", with the chain #337→#352 [CHECKED `holonic_ARCHITECTURE.md`:12-15]. The season loop's data owners admit `research/` as tier-3 reference on Jordan's direction [CHECKED `rosters.yaml`:75-78; HR:1942-1944]. Where Layer 1 says "precedent" it means the CLAUDE.md §0 ladder's internal precedent [CHECKED `ARCHITECTURE_V2.md`:535-541] |
| The plan `workplans/valoria_master_workplan_v9*.md` | 77 state-index rows: IN 42, SC 8, FA 7, SE 5, FI 4, PC 4, GO 3, MB 2, WR 2 | RATIFIED ED-IN-0286, grade `paper`; held back §K and the common-fact store [READER W1 §FILES] | Row counts match index §6 [CHECKED awk over §3]. `git grep 'research/' -- workplans` → one line, `_part8`:170, a caveat about path strings in provenance files, not a citation [CHECKED]. Games named in the plan: the six detective games of A-25's world surface (`_part5`:388) and "fire emblem style" as Jordan's quoted words [CHECKED grep; READER W1 §G]; no historical case [READER W3 §G] |
| `CURRENT.md` IN-lane rows | Scale transitions → `scale_transitions_v30.md`; Player agency → `player_agency_v30.md`; Holonic doctrine → `holonic_container_doctrine_v1.md` (ED-1083); Propagation spec → `propagation_spec_v1.md` (ED-1093); Narrative engine → `narrative_engine_design_v2_churn.md` (ED-IN-0011); Articulation; Decision policy (DRAFT) | pointer index [CHECKED `CURRENT.md`:14-45] | Every one of these rows names a quarantined `.designs/` or `.audit/` document by bare filename, which the index declares "reference, not a head" [CHECKED `CURRENT.md`:13], as CLAUDE.md §1 sanctions; the column is still labelled "Head". NPC behaviour (:32) follows the same pattern. Scale transitions (one substrate carries all six directions, J-1), the holonic container doctrine, the propagation spec ("one Key per echo", `targets[]`) and the narrative engine (Key-native I/O) build on the retired Key substrate [READER A7_1 §H, A7_2 §F, E4_4 §F]; player agency's Scene Slate and Standing ladder have no season-loop counterpart [READER A7_2 §F]. The live code that replaced them (`engine/season/`, `architecture/`) has its own rows; the old rows stand as reference rows, not retired. `engine/substrate/` holds no `keys.py` [CHECKED `ls`] |

### 3.2 Design documents and proposals

| path | status as stated | what it defines (functions, verbs, primitives) | grounding cited | assessment |
|---|---|---|---|---|
| `VCD` `proposals/2026-10-03-verb-coverage-and-gap-fill.md` | RATIFIED AS INTENT (v9, ED-IN-0288); "Nothing exists until built with its test" [READER C8_1 §FILES] | 44-verb REACH/NOT; G1–G15; 12 new verbs (IN-12 steps); `record_sourced_operands`; `detain`/`ban`; gate bases warrant/seizure/muster; 63 act families; K-01…K-56; R-1…R-9 | 707 acts from `research/` (80), proposals, loop demand, 7 detective games, CK3+RoTK, governance history (189); secondary sources, snippets [CHECKED `VCD`:70-80, :148-160] | **Live as intent; the only verb-keyed bridge between evidence and plan.** Self-contradicts on K-23 (challenge as petition+fight: "struck" at the head, used in the body) [READER C8_1 §H; C8_2 §H]; its realm att/ex figures are copied from an older tree and "not re-run" [CHECKED :161-164] |
| `#457` `proposals/2026-10-04-forcing-churn-and-the-story-bar.md` | RATIFIED AS INTENT (v9, ED-IN-0287) for handles whose class is not held; CAST-POPULACE not ratified [READER C7_2 §FILES] | FORCE-WEATHER/-BODIES/-HAZARD/-FOREIGN; CARRY-*; BOUND-*; STORY-BAR/-READ/-SOAK; END-VICTORY; each with N-line and control | Jordan's nine drivers; ID-16; internal measurements [READER C7_2 §G]; **cites no `research/` file and no game** [CHECKED grep] | Live (IN-23, IN-27, IN-30, IN-35…IN-37). Grounded in owner intent and controls, not in HCC (the event-deck research) or `EMG` |
| `#445` `proposals/2026-09-30-character-and-play-surface/` | README RATIFIED AS INTENT (ED-IN-0290) for named items; each file PROPOSED [READER C7_2 §H] | season-loop description, the bout's three fidelities, troop registry, Person carrier, faculty(domain), P-1…P-5 | `COMP-1`…`COMP-3` by section [READER C7_2 §G] | The plan's one channel to the companion (§2.3). P-1…P-4 are placed (P-5, a one-line pointer edit, is not in v9:363): P-1 → IN-08, P-2 → IN-22, P-3 → FA-01, P-4 → SC-07 [CHECKED v9:363]; P-2 is scarcity-only [CHECKED `02_against_precedent.md`:81] |
| `proposals/2026-10-07-unplugged-systems-replug.md`, `…-settlements-computation-modules.md`, `…-grid-mode-suspension.md`, `…-character-sheet-spaces.md` | PROPOSED, designs owed by IN-06, IN-07, IN-46, IN-47 [READER W1 §V p4] | module contract (A-25): stateless calls, composition rows `verb_call`/`step_call`/`query`; six settlement extractions; grid suspension at ENCOUNTER | internal only; "no games or history cited" (UNP) [READER C7_2 §G]; 0 `research/` strings [CHECKED grep] | Live designs; ungrounded in research, grounded in Layer 1 |
| `proposals/2026-10-14-in31-revocation-cost-provenance.md` | PROPOSED, design only; conditional on IN-48's reverted carrier [READER C4_2 §FILES] | `REVOCATION_DISPOSAL {appointed: ban, …}`; appointed ⇒ permanent `ban` | H-100's `GOV` vocabulary, "tier 3: vocabulary, not authority" [CHECKED :176-177] | **The one plan design that reads research, through a hole row.** Keys cost on `conferral` basis, not on how the seat was won (H-100's variable) [READER NPC synth §0 item 8 → C4_2 §F]; FA lane finds it harsher than the research's graded demotion [FA synth §0 item 3] |
| `proposals/2026-10-14-in48-delegation-carrier.md` | PROPOSED; built `40926a95`, REVERTED for contradicting ratified Layer 1 [READER C4_2] | `delegate : Person → Office` kind; `delegation` gate basis | Jordan 2026-09-03 "Regency and puppet rulers must be possible" [READER W2 §V IN-48] | Contradicted by Layer 1 (01_AXIOMS §E.2.4; 04:351); the holder ≠ controller precedent (X1) that bears on it is not cited |
| `proposals/2026-09-17-governance-and-holdings-r2/` (01–05), `…-governance-and-holdings/03_THE_SURFACE.md` | RATIFIED AS INTENT (v9), "absorbed where built", and in the same files PROPOSED/HELD BACK [READER C3_1–C3_3 §H] | `reach`, `place_of`, record kinds, `give`, deposit rule, lossy `tell`, conferral/revocation as values, MATTER blocks, `found`, works, surface law | Layer 1 and Jordan rulings; **no game or historical case; refuses to cite unsurveyed Manor Lords/Banished/HoMM** [READER C3_2 §G] | Live where absorbed (`give`, record kinds, lossy `tell`, offices.yaml). The refusal to invent precedent is correct discipline |
| `proposals/2026-09-17-governance-and-behaviour/` (RULINGS.yaml, 00, 01) | SPENT / ABSORBED; ratified AS INTENT (ED-IN-0243) [READER C4_1, C4_2] | beneficiary column; teller on Claim; stance stored; τ = 0.1; AX-7; RR-A FOLD of comply/evade-defy/refract/dispatch | rulings; one ED-SE-0051 citation of an uncommitted "nine-game teardown" [READER C4_2 §G] | **RR-A (fold the four response verbs, ruled 2026-09-17) is contradicted by the live table**, which keeps `comply`, `evade / defy`, `construe`, `dispatch` [CHECKED VT]; J-2 (2026-09-18) re-ruled ONE `evade/defy`, `comply`, `construe` [READER W2 §V A(v9) J-2]. The later ruling governs; RULINGS.yaml still reads "SPENT … 0 escalated" [READER C4_2 §H] |
| `proposals/2026-09-12-emergent-narrative-primitives-v2/` | 00 RATIFIED AS INTENT for P1 (IN-37), P5 (IN-34); 01–04 HELD BACK [READER C7_1 §H] | chronicle render, patron pressures, declared terms, bodies clock, complication modal, counterparty, sheet-as-document | DF legends, Tropico, Banished; PbtA/Blades; seven outside documents pinned by SHA only [READER C7_1 §G] | Partly live (IN-34 built with rates shipped 0; IN-37 BLK) |
| `proposals/2026-08-31-authoritative-architecture/`, `…-09-01-holonic-architecture/` | PROPOSED, HELD BACK IN FULL; holonic README says successor is `ARCHITECTURE_V2.md` [READER C7_1 §FILES] | `choose`/`resolve`/`witness` signatures; six-step loop; Tenure; id(x) by hash; fixed point | `research/` SIM, COMP, XSC (AA/05 §2) [READER C7_1 §G] | Superseded by Layer 1; **AA's central ruling builds Event on `keys.py`** (retired) [READER C7_1 §H] |
| `proposals/2026-08-29-valoria-from-scratch/`, `2026-08-31-ideal*/`, `2026-08-28/29-greenfield-systems-suite*/` | PROPOSED, nothing executed; greenfield v1 ARCHIVED, v2 "content quarry" [READER C5_1, C6_1–C6_4] | the August lineage: `choose(person,view)`, Tenure, mint/efface, gauges, posts, Slate, derive_ob, herald | greenfield anonymizes every precedent ("surveyed franchise") [READER C5_1 §G]; cites SIM/COMP/PMM/XSC by path | **Ancestors, not live.** Their shapes survive in `engine/season/` (signatures, Tenure, Proposition, eight operands) by way of the admissible chain (#337→#357 per `01_AXIOMS.md`:1174; #337→#352 per `holonic_ARCHITECTURE.md`:13), but Layer 1 forbids citing pre-#337 work as authority [CHECKED `holonic_ARCHITECTURE.md`:12-15]. Both greenfield versions build on Keys (J-O) and cite the retired `balance_oracle.py` [READER C5_1 §H, C5_3 §H] |
| `proposals/2026-09-03-governance-corpus-rebuild/` | PROPOSAL; held in `_part8` §K; "no repository file was read as a source" (a 33-doc upload) [READER C2_1] | margin resolver (ED-874), 12-phase tick, Title/Claim/Scheme/InterestGroup | CK3, Victoria 3, EU4, Democracy 4, Into the Breach, Shadow Empire, Frostpunk [READER C2_1 §G]; [SELF-AUTHORED] | **Dead on arrival for IN**: a second kernel (probability-margin for bare-stat checks) and a second tick, both against the one-resolver season loop. Its precedent reading is the richest in any IN-adjacent design and reaches nothing |
| `.designs/systems/_architecture/reference/` (24 + 17 + 3 files) | ARCHIVED-NOT-CANON; several carry CANONICAL inside [READER A7_1–A7_3] | Domain Echo, Sufficient Scope, zoom triggers, Key universal record, aggregate-up/distribute-down, propagation theorems, Scene Slate, three modes | FM/TW/CK/XCOM (duality); RoTK/CK3/Disco/M&B/Pathologic/Pentiment (agency) [READER A7_1 §G, A7_2 §G] | Retired apparatus still named as heads (§3.1). `scale_transitions_v30.md` carries two Status lines (CANONICAL and DESIGN) [READER A7_2 §H] |
| `.audit/` IN audits (NERS 2026-07-04; narrative engine; world-churn; code-leanness; world-schema gap; degree census) | RATIFIED (NERS, narrative engine) or REFERENCE [READER E4_1, E4_4, E4_5] | degree census: 11 sites → 8 ladders → 7 classes; faction_action diverges from canon on 45 % of cells [READER E4_5 §F] | internal; no game or history in E4_5 [READER E4_5 §G] | Historical record of the pre-season-loop tree; the degree-ladder unification it asked for is what the season loop's one `resolve` now does for the 45 verbs, while mass battle keeps a second ladder (MB synth §0 item 9) |
| `proposals/2026-08-19…22` loose August set (wiring map, roll inventory, obstacle census, stats census, event deck, fieldwork architecture) | FINDINGS / MEASURED / PROPOSED [READER G1 §FILES] | 36 roll sites, 6 private kernels, 213 obstacle sites, 30 probability gates; Π-weighted deck | FW cites 20+ games; EV cites one historical case per card [READER G1 §G] | Measurements of a retired tree; EV file holds 8 of its 58 claimed cards [READER G1 §FILES] |

### 3.3 Internal contradictions that matter, and work built on retired apparatus

1. **The relaxed exit and the plan's earlier reversions are reconciled in the same bullet, not contradicted.** v9 §0.5 (RULED 2026-10-13):
   BUILT on a hand-built-world falsifier, realm count recorded, not required [READER W1 §F]. IN-09 (`evade/defy`, `construe`), IN-10's enabler
   and IN-33 (`exchange`) were reverted at B-I *for* 0 realm executions [READER W2 §V IN-09, IN-10, IN-33], and IN-12, IN-26, IN-28, IN-49 still
   state "executes ≥1 in aperture 4 0" [READER W2 §H item 5]; v9:130-132 answers both: those positions "are restorable from their checkpoints
   under this rule", and an exit "still written as 'executes ≥ 1 in `aperture 4 0`' … reads under this bullet" [CHECKED]. What remains is
   drift in the entries' wording, not a rule conflict.
2. **Contested verbs: 3 or 4.** `_part8` §C item 6 "contested verbs = 3 (fight, march, tell)" [READER W3 §F] vs VT and `requirements.yaml`:109
   "4 of 45 … `fight` and `accept`, `march`, `tell`" [CHECKED].
3. **Verb counts.** The plan pins `len(VERB_TABLE)==46` [READER W2 §P] while the table holds 45 [CHECKED]; R-05's measure comment says "44 today"
   [CHECKED `requirements.yaml`:906]; HR rows cite 32- and 38-row tables [READER B2_1 §H, B2_2 §H].
4. **IN-14's batch reads three ways** (B-J / B-Z / absent from B-J) [READER W1 §H; W3 §H item 3]; **IN-06's B-S entry gate three ways**, "not
   reconciled" [READER W1 §H].
5. **`march` attempts/executions**: `requirements.yaml`:732 "`march` 16/16" (realm, tree `23bea9da`, 2026-10-02) vs :1124-1125 "all 11 `march`
   attempts refused at ENCOUNTER (`aperture 4 0`'s `march` line, Declared 11 / no field fought)" (2026-09-30) vs :116-131 `march` "forming,
   being offered, being attempted and executing" in `aperture 1 0` (H-175) [CHECKED all three]; HR:3264-3265 "the realm fights no field at all
   yet: every march it declares targets a non-settlement and is refused at `H-149`'s check" [CHECKED]. The readings come from different trees and
   apertures; the tree does not reconcile them, and none is a flat zero.
6. **RR-A vs J-2** on the response verbs (§3.2 row RULINGS).
7. **`restore` as Mending: a tension conditional on an unbuilt carrier, not a contradiction.** IN-35 quotes `#457`: "Mending as persons' acts
   (the `restore` arm)", and lists under *Needs* "thread operations as a carrier" [CHECKED `_part5`:147-151]. The roster declines to carry the
   Mending cell because `restore` today is "a repair of fabric, not a thread operation", and names its own revert condition: "a thread-operation
   verb or a restore kind exists" [CHECKED `rosters.yaml`:2150-2155]. Both sides wait on the same missing carrier.
8. **Key-substrate builds still standing as reference rows or citations.** `CURRENT.md`'s scale transitions, propagation spec, holonic container
   doctrine, narrative engine rows (§3.1; reference by `CURRENT.md`:13); the authoritative-architecture suite's Event-on-`keys.py` [READER C7_1 §H]; greenfield v1/v2,
   `PGS`/`HCC` hooks, `COMP-1` §2.9 and `PMM` [READER C5_1 §H, R6 §K 8, R4 §K 20]; the Godot strategy's KeyStore, now struck [GO synth §0 item 1].
   The verb table and rosters carry no Key dependence [CHECKED: no `keys.py`; VT sources internal].
9. **`CLAUDE.md` itself is stale on the kernel's path** (`engine/autoload/dice_engine.py`, §5) [CHECKED: no `engine/autoload/`]. Layer 0 text
   is Jordan's file (IN-44 holds the owed edits [READER W3 §V IN-44]).

### 3.4 Critical evaluation

1. **The repository work in this lane is grounded in Layer 1, Jordan's rulings and its own measurements — and Layer 1's derivation excluded
   research by stated rule.** That is a design choice, stated three times in ratified architecture text (§3.1 row Layer 1), one of them scoped
   to `01_AXIOMS.md` Part E. It does not bind the season loop's data owners: `rosters.yaml` records research as tier-3 reference on Jordan's
   direction ("research/ contains useful information to make everything more robust") [CHECKED `rosters.yaml`:75-78; HR:1942-1944]. In practice
   no IN verb row and only two HR rows (H-99, H-100) name research [CHECKED, §3.1]. The exclusion is not total in substance: the chain
   Layer 1 admits (#337→#357 in `01_AXIOMS.md`:1174; #337→#352 in `holonic_ARCHITECTURE.md`:13) contains PR #342 (from-scratch) and the ideal suite, which cite Total War's second resolver, CK3's
   population tap, EU4's unreachable bands, Dominions' commander anchor, Duel of Wits, stasis and Nyāya [READER C6_1 §G; C6_2 §G;
   C6_4 §G]. So the precedent that shaped the loop (one resolver; cast generated on demand, not on a clock) arrived through ancestors
   whose sources the ratified text no longer names. A reader of Layer 1 cannot trace any of its shapes to evidence.
2. **The measurement discipline is real where it is applied.** The executed-set regression is pinned in a test and recorded (21 → 17)
   [CHECKED]; HR grades are mostly `assumption`/`measured`; every invented number is swept. This is the opposite failure from the August
   corpus, whose "BUILT" headers meant "design finalized" [READER R5 §T 5].
3. **What runs is narrow in the corpus and wider in the realm.** 17 of 45 verbs execute in the 143-case corpus [CHECKED
   `test_season_shape.py`:7738-7740]; the realm reading adds `convene`, `determine`, `dispatch`, `open_case`, `survey` and `march`
   [CHECKED `requirements.yaml`:731-734], and `march`'s realm record conflicts with itself (§3.3 item 5). `tell` rolls `pool_default` for 429
   of 430 corpus persons (§3.1). The kernel's σ-leverage, the one IN mechanism with a stated mathematical design, contributes 0 in the game loop
   (`leverage=0.0`, `sigma.py`:147).
4. **The heads index labels reference rows "Head".** Eight IN-adjacent `CURRENT.md` rows (:29-35, :40) name quarantined documents, several
   Key-based; the index states that such rows are "reference, not a head" [CHECKED `CURRENT.md`:13], the convention CLAUDE.md §1 sets. A reader
   who takes the column label over that sentence lands on retired architecture for scale transitions and propagation.
5. **The relaxed exit moves the execution check from the position to the requirement.** A position may close on a verb that executes 0 times
   in computed play, but R-04's and R-05's `met` still read computed play [CHECKED v9:132-135], R-05 cannot be met while IN-45's four verbs do
   not execute [CHECKED `_part5` IN-45 WHAT], the executed set is pinned exactly [CHECKED `test_season_shape.py`:7738-7742], and 21 → 17 is
   recorded as a regression [CHECKED `requirements.yaml`:901-905]. The requirement-level reading is marked [ASSUMPTION; medium] (v9:134). P-2
   maps to IN-22 [CHECKED v9:363]; whether IN-22 carries P-2's control arm was not checked.

## 4. JOIN: FUNCTION, VERB AND PRIMITIVE AGAINST EVIDENCE

**Verdict key.** GROUNDED = evidence of adequate quality bears on the shape, the repository took it, and code realizes it.
PARTLY = evidence was used by the design that specified the row, but it is name-level or tertiary, or code realizes only part of it.
UNGROUNDED = the row and its design cite no research or precedent; it rests on rulings, Layer 1 or measurement only (which can still be
correct). CONTRADICTED = cited or bearing evidence says otherwise, or the code contradicts the design. UNREACHED = research or precedent
bearing on it exists and no owner, design or plan position reads it. Corpus status (E executed / R attempted, always refused / N never
attempted or no predicate/effect) is the IN-57 pin [CHECKED `test_season_shape.py`:7738-7740 executed, :7834-7835 always refused,
:8668-8670 never attempted]. It is the corpus only: the realm reading at tree `23bea9da` records executions for `convene` 12/2, `determine`
20/1, `dispatch` 86/16, `open_case` 28/7, `survey` 165/10 and `march` 16/16 (att/ex) [CHECKED `requirements.yaml`:731-734]. No VT row cites
`research/` or a game [CHECKED], so every verdict below concerns the design layer above the code.

### 4.1 Verb groups G1–G15 (`VCD` §3.2; index §4)

| group | verbs (live / proposed) | repository claim (status) | historical evidence | game evidence | joined verdict | locator |
|---|---|---|---|---|---|---|
| G1 Personal combat | `fight`, `challenge`, `accept` (live); duel terms `yield/blood/death` (PC-10, B) | `fight` contests "the body" through one duel engine; E. `challenge`→`accept` graded `assumption`; `accept` "cannot check a standing challenge", 0 of 12 acceptors held one | HEMA fact files in `.audit/`, unreached (combatants default-built); "ordeal/judicial duel" a list item in `VCD` | FM/TW one-resolver convergence; Fire Emblem (Jordan's words, unsurveyed); bout lineage [UNVERIFIED] | **PARTLY**: one-resolver shape grounded; duel pair and terms UNGROUNDED (rulings only); HEMA UNREACHED | B1_2 §F, §H; PC synth §0 items 1, 6; W1 p4 IN-46 |
| G2 Mass battle | `march` (live, widened arrival IN-13 planned) | contests "a field"; corpus N; realm 16/16 att/ex at tree `23bea9da` (`requirements.yaml`:732) vs all 11 refused on 2026-09-30 (:1124) vs executing in `aperture 1 0` (:116-131) vs HR:3264-3265 "fights no field" [CHECKED]: not a flat zero; one Line subunit per side routs on contact | `PW`, `PA` (occupation), `PFF`, `MBG`; Cannae/Leuctra builders in `modules/mass_battle/` | `COMP-6` §13.3 CK levies; TW auto-resolve (refused); Dominions/M&B leverage null | **UNREACHED**: the most-cited history in the tree feeds module constants the season path does not reach; IN-13's arrival rests on `VCD` §9.6 only | MB synth §0 items 1-2; C8_2 §F 14; index §6 item 3 |
| G3 Social contest | `tell` (live), `argue` (IN-12 step 9) | `tell` contested "a standing" via σ wrapper at `pool_default` (429 of 430 corpus persons) vs hearer capability/2; E; Partial lossy copy; `told_by` chain | `RHET` (stasis, Nyāya, ethos); none cited | Talk of the Town / DF rumour carriage (S05 DOCUMENTED) converge with the built carriage; Duel of Wits; Disco Elysium | **PARTLY**: carriage converges with precedent and is built; the contest half rolls default inputs with no grounding; `RHET` UNREACHED; `argue` plan-only | CHECKED sigma.py; C3_1 §F 02 §A.10; SC synth §0 item 1 |
| G4 Proceedings | `carry`, `convene`, `determine`, `open_case` | all N in the corpus; realm att/ex `convene` 12/2, `determine` 20/1, `open_case` 28/7 [CHECKED `requirements.yaml`:731-732]; `carry` effect DECLINED (H-63); `determine` uncontested, contested form planned (SC-03b) | Venetian councils, impeachment, *ordo iudiciarius*, consistory [H1-nn] (secondary) | Republic of Rome agenda control; Pentiment hearing; L.A. Noire charging | **PARTLY / UNREACHED**: `VCD` maps names; agenda-control precedent names a power `carry` cannot exercise; `RHET` §7 (assemblies, trials) unread by SC-01 | CHECKED `VCD`:4462-4464; B1_2 §F |
| G5 Writ answers | `comply`, `construe`, `dispatch`, `evade / defy` | `comply` landed then N; `construe` grade `absent`; `evade/defy`, `construe` rows reverted at B-I (IN-09); `dispatch` R in the corpus (since IN-57), 86/16 in the realm (`requirements.yaml`:731) | *diffidatio* etymology [UNVERIFIED]; writs, citation/contumacy [H1] | none specific | **UNGROUNDED**, and internally **CONTRADICTED** (RR-A fold vs J-2 retain; §3.3 item 6) | B1_2 §F; W2 §V IN-09; C4_2 §F |
| G6 Documents | `create_record`, `destroy_record`, `forge`, `give`, `issue`, `petition`, `survey` (live); `conceal` (step 10) | E: `create_record`, `give`, `issue`, `petition`; R: `survey` (realm 165/10, `requirements.yaml`:734); N: `destroy_record` (H-75), `forge` (no effect body, H-169) | writ, charter, safe-conduct, warrant [H1]; Zhao Gao forged edict, petition-as-object (PRE, unsourced) | CK3 hooks/secrets (refused by D-5); Shadows of Doubt documents | **PARTLY**: document-as-carrier is the architecture's own design (r2/02) converging with petition-as-object; forgery has no producer; `GOV`/`CGR` UNREACHED | CHECKED `VCD`:4463; R8 §C; C3_1 §F |
| G7 Seats and bonds | `commit`, `confer`, `establish`, `oblige`, `release`, `revoke`, `succeed`, `tie / knot` (live); `repudiate` cut | E: `release`; R: `commit`; N: `confer`, `establish`, `oblige`, `revoke` (IN-10 reverted), `succeed`, `tie/knot` (effects declined) | `RTP` (patronage, kinship, purges), `GOV` hierarchy/standing (H-100), `FASE` T9 interregna; homage, elect/lot, depose [H1] | Kremlin/CK contracts (X1); Old World goals; CK3 succession law | **UNREACHED** for `RTP`/`FASE`; **PARTLY** for `revoke` (H-100 → IN-31 vocabulary); succession (IN-61) rests on Jordan's "the heir still has to claim" | CHECKED HR H-100; W2 §V IN-61; CHECKED `VCD`:4470, :4472 |
| G8 Matter | `exchange`, `levy`, `transfer` | E: `transfer`; R: `levy`; N: `exchange` (reverted, IN-33) | `FASE` T1–T3 (fiscal sociology, tax farming, moral economy); `PW` §3 mustering | X4 levy ≠ professional (CK, Shogun 2, JA2; "4/4"); Pax Pamir pricing | **UNREACHED**: IN-49/IN-52's levy feed (LF-1..3) cites the computation note, not the levy/professional convergence or `FASE` | W1 p4 IN-52; R4 §C X4; R6 |
| G9 Ground and fabric | `build`, `found`, `restore`, `work` (live); `raze`, `sabotage` (steps 9, 11) | all four R; `work` 0/183; `body_step` shipped 0 | `PGS` §2A, `HCC` §2.3–2.5; Malthus, tragedy of the commons (quoted in 04_MATTER) | Manor Lords, Banished, HoMM named and **refused as unsurveyed** | **UNGROUNDED** by choice (04_MATTER refuses to invent precedent); `PGS`/`HCC` UNREACHED | C3_2 §G; SE synth §0 item 2 |
| G10 Movement | `migrate`, `move` | E: `move`; R: `migrate`; capacity throttle (RR-2) | `FASE` T8 frontier colonization; `PGS` | none | **UNREACHED** | C4_2 §F RR-2 |
| G11 Findings | `examine`, `interview`, `reconstruct`, `research`, `surveil`, `thread_read` | E: `interview`, `reconstruct`, `research`, `surveil`; R: `examine`; N: `thread_read` (H-85); all write `[]`, no degree | coroner's view, Walsingham's cipher secretary [H1]; no `research/` corpus | seven detective games (snippets; one survey from memory per FI synth) | **PARTLY**: names covered; the graded inquiry the games define is unbuilt (FI-01 BLK) and FI-01 would route it through the contest roller Jordan ruled out | CHECKED `VCD`:4457-4458; FI synth §0 items 1-3 |
| G12 Free speech acts | `speak`, `utter` | E both; `speak` writes nothing, contests nothing; `utter` mints Propositions (OUGHT only from computed play) | `RHET` | Disco Elysium voices; Suzerain | **UNREACHED** (`RHET`); `speak` is a placeholder row | B1_2 §F; C8_1 §H |
| G13 Law and custody | `arrest`, `pardon`, `interrogate`, `seize` (IN-12 steps 5, 5a, 6; none in VT) | proposed; `detain`/`ban` tenure kinds exist, opened only by `determine` disposals | inquisitorial chain, *Ad extirpanda*, Lateran IV c.18, bail, *habeas corpus*, confiscation in thirds [H1] (secondary, "mostly Wikipedia") | L.A. Noire, Shadows of Doubt arrest; Disco Elysium arrest [UNVERIFIED]; CK3 imprison/ransom | **PARTLY** at the design layer (`VCD` §9 specs cite the procedures); **not built** | CHECKED `VCD`:1654, :4481-4485; CHECKED VT keys |
| G14 Polity instruments | `covenant` (step 7); `proclaim` deferred | proposed; war = `utter` WAR + `commit`s, `at_war` returns False in every buildable world | Kautilya/Callières, Lodi/Cambrai (FA lane); edict of grace | CK3 war/truce; Diplomacy (binding instruments as exception) | **UNREACHED** (FA synth §0 item 9: "Treaty, war and victory have no grounded live owner") | C8_1 §F; FA synth §0 items 1, 9 |
| G15 The person | `tend`, `train`, `forgive` (steps 9, 13) | proposed; `train` writes `Person.capability` only where a case names a vocation (one NPC) | none | RimWorld/Guild 3/Bannerlord grudge loops (damper); Nemesis | **PARTLY**: `forgive` answers the grudge-loop warning by design; K-45's signed LOOP row "not written"; capability writer otherwise UNGROUNDED | C8_2 §H; W2 §V IN-12 step 9 |

### 4.2 The live verb table, row by row (45)

| verb | grp | VT grade · contests · corpus | plan position | H evidence | G evidence | verdict | note / locator |
|---|---|---|---|---|---|---|---|
| `fight` | G1 | ruled · the body · E | PC-10a/b, IN-59, IN-46 | HEMA (`.audit`), unreached | FM/TW one engine | PARTLY | default-built combatants (PC synth §0 item 1) |
| `challenge` | G1 | assumption · — · E | PC-10b, IN-59 | none | none | UNGROUNDED | Jordan "3 accept"; B1_2 §H |
| `accept` | G1 | assumption · the body · E | PC-10b, IN-59 | none | none | UNGROUNDED | 0/12 held the challenge (VT:600-628 via B1_2) |
| `march` | G2 | ruled · a field · N | IN-13, IN-36, IN-52, MB-07r | `PW`, `PA`, `PFF`, `MBG` | CK levies; TW refused | UNREACHED | realm record conflicts: 16/16 (`requirements.yaml`:732) vs 11 of 11 refused (:1124) vs "fights no field" (HR:3264) [CHECKED]; §3.3 item 5 |
| `tell` | G3 | ruled · a standing · E | IN-18 G5/G8, step 2a | `RHET` unread | ToT/DF carriage (converges) | PARTLY | `pool_default` for 429/430 corpus persons, `leverage=0.0`; CHECKED `requirements.yaml`:1246-1250, sigma.py:147 |
| `carry` | G4 | ruled · — · N | IN-45 | Venetian agenda [H1] | Republic of Rome | UNREACHED | effect declined H-63 |
| `convene` | G4 | ruled · — · N | SC-01 fired slot | prorogation, councils [H1] | — | PARTLY | name-level; realm 12/2 (`requirements.yaml`:731) |
| `determine` | G4 | assumption · — (contested planned) · N | SC-01, SC-03b | trials, consistory [H1]; `RHET` §7 unread | Pentiment, L.A. Noire | PARTLY | Tenure.degree unproduced (H-162); realm 20/1 (`requirements.yaml`:731) |
| `open_case` | G4 | assumption · — · N | SC-01 | inquest, impeachment [H1] | Pentiment inquiry | PARTLY | CHECKED `VCD`:4462; realm 28/7 (`requirements.yaml`:732) |
| `comply` | G5 | ruled · — · N | IN-09 (landed) | writs [H1] | — | UNGROUNDED | RR-A vs J-2 |
| `construe` | G5 | absent · — · N | IN-09 (reverted) | — | — | UNGROUNDED | receiver-side reading, ruling only |
| `dispatch` | G5 | ruled · — · R | J-8 (posts deferred) | pursuivants [H1] | — | UNGROUNDED | `remit_unruled` (B1_1 §F); realm 86/16 (`requirements.yaml`:731) |
| `evade / defy` | G5 | ruled · — · N | IN-09 (reverted) | *diffidatio* [UNVERIFIED] | — | UNGROUNDED | untyped (IN-41) |
| `create_record` | G6 | ruled · — · E | IN-18 G8 | — | — | UNGROUNDED | the one mint |
| `destroy_record` | G6 | ruled · — · N | IN-26 | — | — | UNGROUNDED | eligibility declines both sides (H-75) |
| `forge` | G6 | assumption · — · N | IN-45 | Zhao Gao (PRE, unsourced) | — | UNGROUNDED | no effect body (H-169) |
| `give` | G6 | ruled · — · E | IN-12 give+Rung | homage gifts, hostages [H1] | — | PARTLY | widening to Rung is `VCD` §10.4 |
| `issue` | G6 | ruled · — · E | IN-10 enabler | royal writ [H1] | — | PARTLY | CHECKED `VCD`:4463 |
| `petition` | G6 | ruled · — · E | IN-12 steps 5, 5a | supplique, English SC 8 (PRE, unsourced) | — | PARTLY | RS-23 charge route |
| `survey` | G6 | assumption · — · R | IN-12 survey+Rung | Domesday, visitation [H1] | — | PARTLY | means a faction sheet, not an assessment (SE synth §0 item 5); realm 165/10 (`requirements.yaml`:734) |
| `commit` | G7 | ruled · — · R | IN-11, IN-68 | — | — | UNGROUNDED | left executed set at IN-57 |
| `confer` | G7 | ruled · — · N | IN-10, IN-48, IN-61 | `RTP` A, `GOV` | Kremlin/X1 | UNREACHED | IN-10 reverted |
| `establish` | G7 | assumption · — · N | IN-10, IN-48 | `GOV` offices | — | UNREACHED | operands outside closed 8 |
| `oblige` | G7 | ruled · — · N | IN-10, IN-40, IN-58, FA-04 | homage [H1]; `GOV` | CK contracts | PARTLY | vassalage derived (H-101) |
| `release` | G7 | ruled · — · E | IN-11 | resign, abjure [H1] | — | PARTLY | one generic `release` (A-16) |
| `revoke` | G7 | ruled · — · N | IN-10, IN-31 | `GOV` via H-100 | — | PARTLY | the only research reach; computed revoke executes 0 (C4_2 §H) |
| `succeed` | G7 | assumption · — · N | IN-61 | `RTP` G, `FASE` T9; tanistry [H1] | CK3 succession law | UNREACHED | effect declined; heir unbound |
| `tie / knot` | G7 | ruled · — · N | IN-32 | marriage [H1] | — | UNGROUNDED | `_eff_tie` unbuilt (H-182) |
| `exchange` | G8 | assumption · — · N | IN-33, FA-01 | `FASE` | Pax Pamir pricing | UNREACHED | reverted at B-I |
| `levy` | G8 | assumption · — · R | IN-49, IN-52 | `FASE` T1–T3, `PW` §3 | X4 levy ≠ professional | UNREACHED | eligibility is a substitution (H-52) |
| `transfer` | G8 | ruled · — · E | — | — | — | UNGROUNDED | — |
| `build` | G9 | assumption · — · R | IN-28, SE-03 | `PGS` §2A | Manor Lords (refused) | UNGROUNDED | no works declared |
| `found` | G9 | assumption · — · R | IN-28, SE-03 | `PGS` | Manor Lords (refused) | UNGROUNDED | — |
| `restore` | G9 | ruled · — · R | IN-35 | — | — | UNGROUNDED | as its G9 siblings; Mending reading waits on a thread-operation carrier, as does the roster's revert (§3.3 item 7) |
| `work` | G9 | ruled · — · R | IN-45 | `HCC` | — | UNGROUNDED | 0/183 |
| `migrate` | G10 | assumption · — · R | IN-45 | `FASE` T8 | — | UNREACHED | capacity throttle |
| `move` | G10 | assumption · — · E | IN-59 audience | — | — | UNGROUNDED | — |
| `examine` | G11 | assumption · — · R | FI-01 | coroner's view [H1] | Pentiment, L.A. Noire | PARTLY | refused since IN-57 |
| `interview` | G11 | assumption · — · E | FI-01 (prompt) | — | Disco Elysium, Lacuna | PARTLY | plan vs Jordan's "Lattice first" (FI synth §0 item 6) |
| `reconstruct` | G11 | ruled · — · E | FI-01 (waits K-37) | — | L.A. Noire notebook | PARTLY | no degree |
| `research` | G11 | assumption · — · E | FI-01 | Walsingham cipher [H1] | Shadows of Doubt records | PARTLY | — |
| `surveil` | G11 | assumption · — · E | FI-01 | State Inquisitors [UNVERIFIED] | Shadows of Doubt tailing | PARTLY | watch/tail family DEFERRED |
| `thread_read` | G11 | assumption · — · N | IN-06, PC-06 | none (threadwork null) | none | UNGROUNDED | Thread Sensitivity has no carrier (H-85) |
| `speak` | G12 | assumption · — · E | SC-01 step 12 | `RHET` | — | UNREACHED | writes nothing |
| `utter` | G12 | assumption · — · E | SC-01 step 5a | denunciation [H1] | — | PARTLY | computed `utter` cannot set mood (C8_1 §H) |

Tally (45, recounted from the table after `restore` moved from CONTRADICTED to UNGROUNDED): GROUNDED 0 · PARTLY 18 · UNGROUNDED 18 ·
UNREACHED 9 · CONTRADICTED 0. Every PARTLY rests on `VCD`'s name-level mapping or a
convergence the design reached without citing it; no row reaches GROUNDED because no row's shape was set by evidence that code then carries.

### 4.3 Verbs and re-specifications the plan schedules that are not in the table

| verb / re-spec | plan | evidence the design cites | verdict |
|---|---|---|---|
| `arrest`, `pardon`, `interrogate` + the charge (steps 5, 5a) | IN-12, B-R | inquisition and secular law [H1]; L.A. Noire, Shadows of Doubt, CK3 [G]; RS-23 (Jordan) | PARTLY (procedures named; [H1] tertiary) |
| `seize` (step 6), `raze` (step 11), occupation as a Query | IN-12, IN-13 | confiscation, search on warrant [H1]; chevauchée [R1-58] | PARTLY |
| `covenant` (step 7) | IN-12, B-Q | hostages as treaty surety [H1]; CK3, Diplomacy | UNREACHED (FA's treaty research not read) |
| `sabotage`, `tend`, `argue`, `train` (step 9) | IN-12, B-Q | RoTK schemes (sabotage); `RHET` not cited for `argue` | PARTLY (`sabotage`); UNREACHED (`argue`); UNGROUNDED (`tend`, `train`) |
| `conceal` (step 10), `forgive` (step 13) | IN-12, B-Q | spy cover [H1]; RimWorld/Guild grudge damping [G] | PARTLY |
| `march` arrival (step 8) | IN-13, B-M | `VCD` §9.6 derivation only | UNGROUNDED (`PW`, `PA` UNREACHED) |
| `succeed` as the heir's claim; `inheritance` basis | IN-61, B-R | Jordan 2026-10-14; RS-27 | UNGROUNDED (`RTP` G, `FASE` T9 UNREACHED) |
| `kill`, `wound`, `execute`, `proclaim`, `steal`, `repudiate` | refused or deferred | Jordan's rulings (direction 3, R-1, R-3, R-8) | ruling-based; consistent with the evidence (execution as detain + fight is how Pentiment and CK3 present it) |

### 4.4 Functions and primitives

| function / primitive | repository claim (status) | historical evidence | game evidence | joined verdict | locator |
|---|---|---|---|---|---|
| d10 / TN 7 / four bands (`degree_from_net`) | CURRENT "in code"; one owner | none (`MBG` §1 calibrates the MB gauge, not the kernel) | `COMP-3` §7.9 "ahead on ownership, behind on calibration"; Blades band-floor test (arithmetic) | UNGROUNDED (no calibration target), ownership sound | CHECKED CURRENT; R4 §T P3 |
| σ-leverage μ-shift | `sigma_leverage.py`; in the season loop `leverage=0.0`, `pool_default` on 429/430 corpus persons | none | none surveyed | **UNREACHED by the game**: the mechanism exists and contributes 0 | CHECKED sigma.py:139-147; `requirements.yaml`:1246-1250 |
| Season loop and barriers (CALENDAR…CENSUS) | RATIFIED, runs | none (Layer 1 excluded it) | FM "one engine headless"; inherited via the #342/#343 suites | PARTLY (inherited, uncited) | CHECKED 01_AXIOMS:1173-1176; C6_1 §G |
| `resolve` from one table, refusal as an Event | runs | none | "never build a second resolver" (TL06, PRE; FS 09 §2.1) | PARTLY (inherited, uncited) | B1_2 §F; R8 §T 5; C6_1 §G |
| `choose`: score = Σ axis·alignment + stance + urgency; softmax τ 0.1 | runs; τ "not tuned" | 28 of 105 pursuit cells cite outside literature (Sidanius, Schwartz, Weber…) in `candidate_pursuit_cells.md`; **0 literature names travel into `rosters.yaml`** (cells tagged carried/derived/reasoned) | Plackett-Luce via Gumbel (decision theory) | PARTLY | C7_2 §F CPC; CHECKED rosters grep |
| Regard at read (stance + judged deeds + told valence) | landed (A-12) | none | `EMG` memory question (read at a decision point) | PARTLY (convergent, uncited) | W2 §V A-12; R8 §T 3 |
| Attention tiers T0–T4 (IN-57) | landed; cost felled 47→82, executed 21→17 | none | none | UNGROUNDED; its own measurement shows regression | W2 §V IN-57 |
| Cast loyalty | static cosine of authored values against a role template | `RTP` G (downfall), `GOV` | Imperator, JA2, EU4 loyalty all moving quantities | **CONTRADICTED** by every precedent the corpus holds | NPC synth §0 item 1 |
| Goals carrier (IN-66…IN-69), goal referents at read | B (B-X) | `RTP` | Old World goals × houses, expiring on death; Kremlin mortality (K6) | UNREACHED (expiry-on-death absent from the entries) | W2 §F; R4 §C |
| Grievance at read (IN-58) | stance half landed, EXIT unmet | — | CK opinion stack; RimWorld | UNGROUNDED | W2 §V IN-58 |
| Legitimacy / stability as Queries (IN-23) | B | `FASE` T10 (Weber), derived not stored | Victoria 3 derived numbers | UNREACHED (shape converges, uncited) | W3 §G ED-SE-0007 superseded |
| Endings vocabulary (IN-27, END-VICTORY) | BLK; H-176 `absent` | none | none surveyed | UNGROUNDED | FA synth §0 item 9 |
| Forcing handles (#457: weather, bodies, hazard, foreign) | partly built, rates shipped 0 | `HCC` (crises), `PW` (invasion during instability) | CK population refusal (#13) honoured | UNREACHED (`HCC` 0 readers) | WR synth §0 item 2 |
| Chronicle / story bar (IN-19, IN-37, M2) | instrument built; render BLK | — | DF legends, Tropico almanac, sifting literature (EN P1); expression null D6 | PARTLY (via ENP v2, not via plan) | C7_1 §G |
| Scale transitions / fidelities (IN-46 grid suspension; SM-5) | design landed; replay-equal under 6 conditions | — | FM three fidelities; TW auto-resolve failure; XCOM | **GROUNDED** (owner ruling and independent precedent converge; one engine in code) | W1 p4 4.2; R4 §C |
| Old scale transitions document (Domain Echo, Sufficient Scope, 13 zoom triggers) | CURRENT reference row (`CURRENT.md`:13, :29); RR-3 replaced triggers by claim-landing | — | — | CONTRADICTED by RR-3 and by Key retirement | C4_2 §F RR-3; A7_2 §F |
| Holonic aggregation (aggregate on demand, never stored; no reach-through) | Layer 1, runs | none (excluded) | CK3/EU4 aggregates; Victoria 3 "number derived from agents" | PARTLY (convergent, uncited) | C7_1 §F HO |
| Propagation (aggregate-up, distribute-down via Keys; theorems A/B) | CURRENT reference row `propagation_spec_v1.md` (`CURRENT.md`:34) | — | — | CONTRADICTED (Key-based; retired) | A7_2 §F |
| Key substrate | RETIRED (ED-IN-0232); `keys.py` absent | — | `COMP-2` §6 #19 warned against treating it as emergence | retired; still load-bearing in several `CURRENT.md` reference rows and most August proposals | CHECKED `ls engine/substrate/`; R4 §C |
| Write matrix, `unproduced:` holes | data code reads | — | — | UNGROUNDED (architecture), measured | B1_2 §F |
| Hole register (198 rows) | read by `register.py` | 2 rows cite `research/` | 0 rows | UNGROUNDED except H-99/H-100 | CHECKED |
| Rosters (`conferral_bases`, `tenure_kinds`, `record_kinds`, operands) | closed sets, code reads | two tier-3 rosters (`governance_modes`, `power_bases`, from `GOV`) built then **deleted unread** | — | UNREACHED by design (tier 3 ruling) | CHECKED rosters.yaml:84-89 |
| Plan instruments (STATE classes, stopping rule, relaxed exit, test horizon) | RULED 2026-10-13 | — | EU4/Imperator failure shape A | **PARTLY**: the relaxed exit lets a position close on a never-firing verb, but R-04/R-05 `met` still read computed play (an [ASSUMPTION; medium] reading) and the executed-set pin fails when the set moves | CHECKED v9:132-135; `test_season_shape.py`:7738-7742; `requirements.yaml`:901-905; R8 §C |

### 4.5 Plan positions against the research that bears on them (each lane)

| lane (rows) | positions | research and precedent that bear | what the position cites | verdict |
|---|---|---|---|---|
| IN (42) | verbs IN-09…IN-13, IN-26, IN-28, IN-32, IN-33, IN-45, IN-49 | `VCD`; [H1] procedures; `GOV`, `RTP`, `FASE`, `PW`; X4 | `#453` lines, H-rows, Jordan | PARTLY via `VCD` only |
| | cast and goals IN-38, IN-58, IN-62…IN-72, IN-61 | `RTP`, `GOV` hierarchy; Old World/Kremlin (K6); loyalty precedents | ED-IN-0293, RS-22…RS-27, Jordan's words | UNREACHED (and loyalty CONTRADICTED) |
| | forcing and endings IN-23, IN-27, IN-30, IN-35, IN-36, IN-37 | `HCC`, `PW` §2, `FASE` T10; `EMG`, `THR` ch. 1/4/5 | `#457`, ED-IN-0225, GD-1 | UNREACHED |
| | IN-31 | `GOV` via H-100 | the hole row; its design reads the vocabulary | PARTLY (the one reach; keyed on a different variable) |
| | IN-46, IN-47 | FM/TW/XCOM; JA2 publish-bands (via `#445` 07) | SM-5, `#445` | GROUNDED (IN-46); PARTLY (IN-47) |
| | IN-48 | X1 holder ≠ controller | Jordan 2026-09-03 | UNREACHED; reverted against Layer 1 |
| | IN-06, IN-14, IN-18, IN-23, IN-44, IN-52, IN-59, IN-60 | threadwork: none; telling dossier "A Tells B About C" uncommitted; levy X4 | internal | UNGROUNDED / UNREACHED (IN-52) |
| SC (8) | SC-01…SC-08 | `RHET`, `SC-SRC`, `COMP-6` §13.1–13.2, Duel of Wits | proceedings suite (T2 study), `04_VERBS`, `#445` P-4 | UNREACHED (SC synth §0 item 2); SC-07 attaches P-4 and builds nothing |
| SE (5) | SE-03, SE-04, SE-06 (+ aliases IN-07, IN-30) | `FASE`, `PGS`, `HCC`, `GOV`; null N-7 (appointed governor) | ED-SE-0053, H-170/171, ED-IN-0293 | UNREACHED (SE synth §0 items 1, 5) |
| FA (7) | FA-01, FA-04…FA-07 | `GOV`, `CGR`, `RTP`; Old World, EU4, Imperator | `#445` P-3 (FA-01); ED-IN-0293; quarantined v30 docs (FA-06) | PARTLY (FA-01 via P-3); rest UNREACHED |
| PC (4) | PC-05, PC-06, PC-08, PC-10 | HEMA fact files, weapon physics (`.audit`) | `#445` K-items, RS-25 | UNREACHED (PC synth §0 item 1); PC-10 terms UNGROUNDED |
| MB (2) | MB-07r, MB-08 | `PFF`, `PW`, `MBG` | J-18, ED-MB-0041; cites module paths that no longer exist (MB synth §0 item 8) | UNREACHED by the plan; consumed by module constants |
| FI (4) | FI-01…FI-03 (+ FI-05 = IN-32) | `VCD` App. B 1–5; detective games | ED-FI-0009, J-22, SM-3 | PARTLY (names); contradicts Jordan's "not a contest seam" in routing (FI synth §0 item 2) |
| WR (2) | WR-01 (+ WR-05 = IN-35) | `HCC`; threadwork has none | `06_operations.md`, H-94 | UNREACHED (`HCC`); UNGROUNDED (threadwork null) |
| GO (3) | GO-01, GO-05, GO-06 | none exists | J-9, SM-13 | UNGROUNDED (null corpus) |

**The plan cites no `research/` document** [CHECKED: one grep hit, `_part8`:170, not a citation]. It reaches game precedent through three
proposals (`VCD`, `#445` 02, the proceedings suite) and historical precedent through `VCD`'s `[H1-nn]` rows and one hole row (H-100). Of 77
state-index rows, the ones whose cited evidence includes any external case are the IN-12 steps (via `VCD`), FA-01 (P-3), SC-07 (P-4),
IN-46 (Fire Emblem as Jordan's words) and IN-31 (H-100). IN-22, to which P-2 (citing EU4's estates) maps, has landed and left the state
index [CHECKED v9:363; `_part5`:191].

## 5. WHAT THIS LANE'S CORPUS DOES NOT COVER, AND WHAT YOU DID NOT READ

- [GAP: resolution-kernel calibration — no historical, statistical or game source sets TN 7, the four band edges, `pool_default` 2 or `obstacle_default` 2; `MBG` §1 calibrates the mass-battle gauge only; the 2026-05-28 engine-replacement audit exists only at tag `v30-snapshot-2026-06-28` (index §2.E), not read]
- [GAP: season-loop structure — no research on turn structure, simultaneous resolution or barrier order; Layer 1 excluded it by rule]
- [GAP: scale transitions beyond the bout — FM/TW/XCOM cover fidelity of one contest; nothing in the corpus covers personal ↔ faction ↔ settlement handoff in the season loop (null N-3/D3 stands)]
- [GAP: endings and victory — no research for IN-27/IN-30 (FA synth §0 item 9)]
- [GAP: threadwork and the Calamity coupling (IN-06, IN-35) — no game or historical source exists (index §7)]
- [GAP: the two surveys behind `VCD`'s P1–P58 and F01–F84, the "A Tells B About C" dossier and the seven pinned outside documents are not committed; their points survive only as `VCD`/ENP v2 restate them]
- [GAP: the `[H1-nn]` governance-history extraction table is not committed; only its ids survive in `VCD` App. B]
- [SKIPPED: the other lanes' reader extractions (D1–D4, E1–E3, A1, A2, A5, R1–R3, R6, R7, R9) — read only through targeted greps (R3, R6, R7, A9 FILES and checks) and through the sibling synthesis files' verdict sections, cited as "<LANE> synth"; their findings used here are those lanes' [CHECKED] items]
- [SKIPPED: `C5_greenfield_2`, `C5_greenfield_3`, `C6_from_scratch_ideal_2`…`_4`, `G2_godot` — read FILES, F–G and H sections; V and P sections skimmed, since this lane needed only their status and grounding]
- [SKIPPED: re-running `corpus_run`, `register --requirements`, `m1_acceptance.py` — the brief forbids test runs; executed-set figures are the IN-57 pin in `test_season_shape.py` and the `requirements.yaml` measured blocks]
- [CONFIDENCE: medium — per-verb H and G evidence in §4.2 compresses `VCD` App. B families to one or two examples each; App. B lines 4457–4486 were opened, the rest taken from C8_2 §V]
- [CONFIDENCE: medium — §4.2's PARTLY/UNGROUNDED boundary is a judgment about whether `VCD`'s name-level mapping counts as "used"; moving it would shift up to 18 rows between the two classes, not into GROUNDED]
- [CONFIDENCE: low — whether IN-22 (to which `#445` P-2 maps, v9:363; H-160 → IN-22, :368; landed per `_part5`:191 and `_part3`:213) carries P-2's control arm "at today's yields" was not checked: `test_in22_shortfall_reach.py` was not opened]

## 6. METHOD NOTE

Written from reader extractions, then attacked by an independent read-only critic who checked 14 load-bearing claims, recounted the 45
verb rows and their grades (confirmed), and re-ran three absence searches (held). Two claims failed outright and five more were overstated
or mis-located. Each correction below was checked against its source before it was applied.

1. "`#445` P-2 has no plan position" was false: v9:363 maps P-2 → IN-22 (and H-160 → IN-22, :368), which landed (`_part5`:191); the draft's
   grep missed it across a line break. Whether IN-22 carries P-2's control arm is left unchecked.
2. P-2 is scarcity-only (`02_against_precedent.md`:81), not a verb-execution bar, and the table runs P-1…P-5 (:84); the shape-A argument no
   longer rests on it.
3. "No instrument would fail if a built verb never fires" was false: v9:132-135 keeps R-04/R-05 `met` on computed play (marked [ASSUMPTION;
   medium]); the executed set is pinned exactly (`test_season_shape.py`:7738-7742) and 21 → 17 is recorded as a regression
   (`requirements.yaml`:901-905). §0 item 2 fell to item 7; §4.4's plan-instruments row moved CONTRADICTED → PARTLY.
4. The relaxed exit vs the reversions is reconciled at v9:130-132 (reverted positions restorable; "executes ≥ 1" exits read under the rule);
   §3.3 item 1 restated as wording drift.
5. `march` is not a flat zero in the realm (`requirements.yaml`:116-131, :732 16/16 vs :1124 11 refused; HR:3264-3265); the realm also executes
   `convene`, `determine`, `dispatch`, `open_case`, `survey` (:731-734); "17 of 45" is now labelled a corpus figure (§0 item 6, §3.1, §4).
6. `march` locators corrected from `requirements.yaml`:675/:1022 to :732/:1124.
7. "Every pool `pool_default`" and "measured 74/19/7" corrected: 429 of 430 defaulted (`requirements.yaml`:1246-1250, :1284-1287, which
   records `sigma.py`:101-102 as stale); 74/19/7 is a computed split (ENP v2 `04_PROVENANCE.md`:114-115); measured tellings 24 told
   (Success 6, Partial 18) vs 29 untold (:1240).
8. The `CURRENT.md` rows are declared reference, not heads (`CURRENT.md`:13); the count is eight IN-adjacent rows, not five; the defect is the
   "Head" column label. §0 item 4 fell to item 10.
9. Layer 1's exclusion is scoped (01_AXIOMS Part E), its chain is #337→#357 there and #337→#352 in `holonic_ARCHITECTURE.md`:13, and the
   season loop's data owners admit research as tier 3 on Jordan's direction (`rosters.yaml`:75-78; HR:1942-1944); "every IN function inherits
   that" withdrawn.
10. `restore` reclassified CONTRADICTED → UNGROUNDED: IN-35's Mending reading needs "thread operations as a carrier" (`_part5`:147-151) and the
    roster's revert condition is that carrier (`rosters.yaml`:2155); tally now 0 / 18 / 18 / 9 / 0.
11. Executed-set locators corrected to `test_season_shape.py`:7738-7740 (executed), :7834-7835 (refused), :8668-8670 (never attempted).
12. Research tried against the season loop: two rosters (`governance_modes`, `power_bases`), not one instance (`rosters.yaml`:86-88).
13. Spelling: anonymizes, finalized, realizes (×2), colonization, mobilization (not a quoted name).
