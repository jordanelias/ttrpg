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
   IN-61); `FASE` T1–T3 and X4 for the levy feed (IN-49, IN-52 — both built on a `levy` row that moves stores, a name Jordan
   ruled wrong on 2026-10-16, §8 M-IN-13); `PW`/`PA` for `march` arrival and occupation (IN-13); `HCC` for forcing
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
| `VCD` App. B game sets | Seven detective games (107 acts), CK3 + RoTK (107 acts) mapped to 63 act families | RATIFIED AS INTENT (ED-IN-0288); "Web facts about the games rest partly on search snippets"; many review sites 403; Paradox wiki pages would not load [CHECKED `VCD`:156-158] | Name-level evidence; several rows [UNVERIFIED] (Disco Elysium arrest, CK3 torture, Espiocracy) [READER C8_1 §G]; the two surveys behind P1–P58 and F01–F84 are not committed and are in no upload [CHECKED `VCD`:99-133; UPLOAD_CHECKS "STILL ABSENT"]. **Upload test of `VCD`'s [SESSION] rows** (the churn survey's game claims, carried "at its word", `VCD`:127): *Guild 2* fabricated evidence with strength, believability and ~6-year decay, and slander spreading a fabricated crime (`VCD`:1120-1121, :1266, :3455) CONFIRMED by the teardown [CHECKED TD:191]; *Dwarf Fortress* values/facets, *RimWorld* moodlets and storyteller, *The Sims* argmax (`VCD`:1063-1072, :1125) CONFIRMED by the mechanical specifications [CHECKED N2:199, :245, :273, :369]; *Manor Lords* approval-gated immigration and *Tropico* die-hard diffusion (`VCD`:1074, :1124) CONFIRMED [CHECKED TD:148, :231]; *Prom Week*/*Versu* norm gating (`VCD`:1213) PARTLY (the compendium names both, nothing on norm gating) [READER UPLOAD_CHECKS]; *Shadows of Doubt* case submission (`VCD`:1093) is in no upload; *Guild 3* F77 (below, §2.2) NOT IN THE SOURCE. `VCD`'s [ASSUMPTION] that "the survey never expands the labels" (`VCD`:125-127) is superseded: *The Third Strand* expands them — D1 the nine-title settlement teardown, D2 the thirteen-title analysis, D3 the twenty-game consolidation, N1 the compendium, N2 the mechanical specifications (not a second compendium) [CHECKED 3S:5] |
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
| RimWorld, Guild 3, Bannerlord, Skyrim radiant (grudge loop/damping) | Feud spiral; need for a damper | failure | churn survey [SESSION] via `VCD`, except *Guild 3*: the teardown and the twenty-game consolidation give the publisher's own account (T1): with the citizen layer enabled, townsfolk "burned the **player's** residence down at roughly every second launch", and the publisher asked the studio to switch the inhabitants' AI off [CHECKED TD:195; 20G:241]. `VCD`:985 says "the producer's residence" (wrong owner) and `VCD`:183-184 a "producer's forum post that predates Early Access" (neither upload says forum post or dates it); `VCD`:1122's F77, "a mob burning a residence at a popularity threshold", comes from the absent churn survey: no threshold, popularity or mob is in either upload [CHECKED TD:195; 20G:241]. "Switched off rather than damped" (`VCD`:985, :995) is CONFIRMED (20G:241) | Informs `forgive` (IN-12 step 13, unbuilt) and K-45's recommended signed LOOP row, "not written" [READER C8_2 §H]. The grudge append per lost field has no bound today (`VCD`:985 cites `effects_combat.py:353-358`). The *Guild 3* case is a failure of an agent layer with no damping and no half-strength setting, which the uploads themselves draw as a directive (TD:543 per UPLOAD_CHECKS; 3S T6 [READER UP01 §T 6]) |

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
| `proposals/2026-09-17-governance-and-behaviour/` (RULINGS.yaml, 00, 01) | SPENT / ABSORBED; ratified AS INTENT (ED-IN-0243) [READER C4_1, C4_2] | beneficiary column; teller on Claim; stance stored; τ = 0.1; AX-7; RR-A FOLD of comply/evade-defy/refract/dispatch | rulings; one ED-SE-0051 citation of the "nine-game teardown" [READER C4_2 §G], untracked but now in hand in its audited revision (upload 3cb2a6c8): it supports capacity as a growth gate only partly (Banished vacancy gates births, Manor Lords plot capacity gates immigration; "strongest entries" is not in it) [READER UPLOAD_CHECKS SFP 05:202-207] | **RR-A (fold the four response verbs, ruled 2026-09-17) is contradicted by the live table**, which keeps `comply`, `evade / defy`, `construe`, `dispatch` [CHECKED VT]; J-2 (2026-09-18) re-ruled ONE `evade/defy`, `comply`, `construe` [READER W2 §V A(v9) J-2]. The later ruling governs; RULINGS.yaml still reads "SPENT … 0 escalated" [READER C4_2 §H] |
| `proposals/2026-09-12-emergent-narrative-primitives-v2/` | 00 RATIFIED AS INTENT for P1 (IN-37), P5 (IN-34); 01–04 HELD BACK [READER C7_1 §H] | chronicle render, patron pressures, declared terms, bodies clock, complication modal, counterparty, sheet-as-document | DF legends, Tropico, Banished; PbtA/Blades; seven outside documents pinned by SHA (`04_PROVENANCE.md`:130-138) [READER C7_1 §G], of which five are now in hand as uploads and hash-match (compendium, mechanical specifications, thirteen games, nine titles, twenty games); the two earlier drafts are not, and the uploaded *Third Strand* differs from its pin [READER UPLOAD_CHECKS §Identity] | Partly live (IN-34 built with rates shipped 0; IN-37 BLK) |
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
| G8 Matter | `exchange`, `levy`, `transfer` | E: `transfer`; R: `levy`; N: `exchange` (reverted, IN-33) | `FASE` T1–T3 (fiscal sociology, tax farming, moral economy); `PW` §3 mustering | X4 levy ≠ professional (CK, Shogun 2, JA2; "4/4"); Pax Pamir pricing (the companion cites its own dossiers and the rulebook; content CONFIRMED against the teardown's T0 rulebook reading [CHECKED TD:33, :49]) | **UNREACHED**: IN-49/IN-52's levy feed (LF-1..3) cites the computation note, not the levy/professional convergence or `FASE`. **And the `levy` row is misnamed** (Jordan, 2026-10-16: "levy typically doesn't refer to goods/stores. that verb is wrong as currently used"): it moves `Rung.stores` [CHECKED VT:629-652; `effects_governance.py`:374], so X4's levy ≠ professional, which is about raised troops, has no verb to reach (§8 M-IN-12, M-IN-13) | W1 p4 IN-52; R4 §C X4; R6 |
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
| `confer` | G7 | ruled · — · N | IN-10, IN-48, IN-61 | `RTP` A, `GOV` | Kremlin/X1 | UNREACHED | IN-10's enabler reverted; a computed `confer` executes `via` its seat since IN-53 (`5652e846`) in the realm, not the corpus [CHECKED `_part2`:178, `_part7`:123; corpus 0, `requirements.yaml`:895-898]; the realm assertion was deleted under the relaxed exit (v9:128-129) |
| `establish` | G7 | assumption · — · N | IN-10, IN-48 | `GOV` offices | — | UNREACHED | operands outside closed 8 |
| `oblige` | G7 | ruled · — · N | IN-10, IN-40, IN-58, FA-04 | homage [H1]; `GOV` | CK contracts | PARTLY | vassalage derived (H-101) |
| `release` | G7 | ruled · — · E | IN-11 | resign, abjure [H1] | — | PARTLY | one generic `release` (A-16) |
| `revoke` | G7 | ruled · — · N | IN-10, IN-31 | `GOV` via H-100 | — | PARTLY | the only research reach; computed revoke executes 0 (C4_2 §H) |
| `succeed` | G7 | assumption · — · N | IN-61 | `RTP` G, `FASE` T9; tanistry [H1] | CK3 succession law | UNREACHED | effect declined; heir unbound |
| `tie / knot` | G7 | ruled · — · N | IN-32 | marriage [H1] | — | UNGROUNDED | `_eff_tie` unbuilt (H-182) |
| `exchange` | G8 | assumption · — · N | IN-33, FA-01 | `FASE` | Pax Pamir pricing (CONFIRMED, TD:49) | UNREACHED | reverted at B-I |
| `levy` | G8 | assumption · — · R | IN-49, IN-52 | `FASE` T1–T3, `PW` §3 | X4 levy ≠ professional | UNREACHED | eligibility is a substitution (H-52). **MISNAMED** (Jordan, 2026-10-16): the row moves `Rung.stores` ×2 into the seat's treasury [CHECKED VT:629-652, `_eff_levy` `effects_governance.py`:374], a store extraction; the troop-raising act the name denotes does not exist (§8 M-IN-12, M-IN-13). The store act's new name is Jordan's |
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
| a troop-raising `levy` (Jordan 2026-10-16: troops "levied from settlements as their own resource") | none: IN-49 gives the stores row a referent, IN-52 "`levy` moves stores, not troops" (`_part4`:137 [CHECKED]); MB-08 LEAVE carries #445 U-1 "musters with inputs beyond headcount" (`_part7`:26 [CHECKED]) | X4 levy ≠ professional (CK, Shogun 2, JA2) [READER R4 §C]; `PW` §3 mustering | UNREACHED (no position; §8 M-IN-12) |
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
- [GAP: the two surveys behind `VCD`'s P1–P58 and F01–F84 and the "A Tells B About C" dossier are not committed and are in no upload; their points survive only as `VCD` restates them. Of the seven outside documents ENP v2 pins, five are in hand since this pass as uploads (not tracked files) and hash-match; the two earlier drafts are not (UPLOAD_CHECKS §Identity)]
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

## 7. THROUGHLINES

Sections 7–10 were read at HEAD `5445e34`. Code lines marked [CHECKED] were re-opened this pass; the uploaded NERS audit is a near-copy of the
tracked file `references/ners_audit_2026-10-14.md` (Status REFERENCE, added by `4112b0e`; `diff` shows only its four-line header and two ED-id
rewordings), written at `092fc45`. Between `092fc45` and `5445e34` the non-test code that moved is `witness.py`, `world_q.py`, `person_q.py`,
`cache.py`, `carriers.py`, `log.py`, `world.py`, `epistemic.py`, `options.py`, `verbs.py` (`git diff --stat 092fc45 HEAD`); the dice, seam,
chooser and `deliberate.py` lines the audit cites did not move. [AUDIT] marks a claim taken from it and not re-opened.

**Verdict.** Fourteen throughlines hold in this lane, by primary kind: eight repository patterns (T-IN-1, -2, -3, -4, -8, -9, -11, -14),
one failure shape (T-IN-6; T-IN-3 also carries failure shape A), three convergences (T-IN-5, -10, -13) and two nulls (T-IN-7, -12). The
strongest is T-IN-1 (persons differ in what they want, not in what they can do), which reaches every resolver in the season loop and which no
v9 position closes; T-IN-14 (the season force is sized from stores and weight, never from a troop stock) is its field-scale twin and the one
Jordan's 2026-10-16 statements contradict directly. Two document-stated throughlines are wrong or over-stated as filed (PREC-NULLS N-9,
narrowed: fog by channel loss exists, deceit does not; COMP "six of eight, Valoria owns the primitive"). T-IN-13 is SOUND only as narrowed.

### 7.1 Register

| ID | pattern | kind | cases / sources (independent count) | counter-evidence or limits | REACH IN CODE | REACH IN PLAN | verdict |
|---|---|---|---|---|---|---|---|
| T-IN-1 | **Persons differ in wants, not capacities.** Every resolver the season reaches is fed a default, not the person | REPOSITORY PATTERN | contest `_pool_of` → `pool_default` 2, `_obstacle_of` → `obstacle_default` 2 [CHECKED `seam/wrappers/sigma.py`:95-129]; capability empty on 429/430 [CHECKED `requirements.yaml`:1244-1247]; combat derives `end` only [CHECKED `seam/wrappers/combat.py`:130-138; `modules/combat/combatant.py`:93-94; `fight.py`:45]; mass battle `_SEASON_FORCE_POWER = 4`, `command=4`, raw weight sum as troops [CHECKED `modules/mass_battle/massbattle.py`:180-207]; audit T1 [AUDIT :324-335]; THR thesis "one absent object (persistent named person)" [READER R8 §T 7]; XSC/INT "missing person is the highest fan-out blocker" [READER R5 §T 3]. Independent: 3 code subsystems; 3 documentary sources, of which THR and XSC share descent (R4 §K 11) → 2 | pursuits and stance do vary per person and move choice (`choose.py`:402-406 [CHECKED]); body band moves `end`. The August "missing person" was the absence of persons; that is fixed (430 built). What remains is the absence of per-person **magnitudes** | executes in the season loop (the defaults are what runs) | J-13 remainder = J.2 rank 1, Jordan's (`_part5`:514 [CHECKED]); `train` (IN-12 step 9, B-Q) writes capability only where a case names a vocation, key `copying` only (`_part5`:73 [CHECKED]); K-1/K-5 "NOT scheduled", K-2 "not ratified" (`_part7`:44 [CHECKED]) | **SOUND** |
| T-IN-2 | **One ladder, many roads to it and beside it** | REPOSITORY PATTERN | per-die literals owned four times [CHECKED `dice_engine.py`:174-175; `sigma_leverage.py`:77-79, :105, :112-113]; combat main roll continuous Normal [CHECKED `modules/combat/core.py`:60] with a logistic side channel [CHECKED :36-41], season/contest discrete [CHECKED `modules/social_contest/roll.py`:35], mass battle discrete [CHECKED `orchestration.py`:1288-1292]; result vocabularies: four-band margin, Felled/Wounded/Untouched, Won/Lost/Unopposed, plus mass battle's own four labels read by nothing [CHECKED `seam/ladder.py`:195-206; `massbattle.py`:285-296]; pool formulas: `c` or 2 (season), `max(5, history+6)` (combat, `core.py`:54-56 [CHECKED]), `spirit×2 + min(3, history+3) + TS//10` (threadwork, `operations.py`:244-247 [CHECKED]); audit T3 [AUDIT]; pre-season-loop degree census "11 sites → 8 ladders → 7 classes" [READER E4_5 §F]; XSC "rival formulas persist because rulings are unexecuted" [READER R5 §T 6]. Independent: code (1) + the two audits (same lineage? no: E4_5 is July, the NERS audit October) → 3 | `degree_from_net` is single-owned and guarded; combat grades through it (`core.py`:61-74 [CHECKED]). The margin ladder is one; the multiplicity is in inputs, substrates and vocabularies | executes | no position unifies substrates or literals: `grep -n "roll_net_continuous\|discrete\|one substrate" workplans/valoria_master_workplan_v9*.md` → 0 relevant hits [CHECKED]; mass-battle margin "open MB-lane work" (`ladder.py`:198-203 [CHECKED]) | **SOUND** |
| T-IN-3 | **Built ahead of its readers; armed controls shipped at off.** A carrier is kept as the record that a measurement happened | REPOSITORY PATTERN + FAILURE SHAPE A | 18 shipped-dark knobs (BASELINE B5, `fixtures.py`:405-849); `urgency` "INERT BY CONSTRUCTION … kept … because deleting it would hide the finding" [CHECKED `choose.py`:172-193]; `benefits_me` no production caller [CHECKED grep: only `choose.py`:150 and docstrings]; σ-leverage `leverage=0.0` [CHECKED `sigma.py`:147]; OUGHT predicate read by nothing (H-185 [CHECKED]); `scale:` reaches no resolver (H-89 [CHECKED]); audit T4 [AUDIT]; EU4/Imperator "a mechanism engineered not to fire is indistinguishable from one that does not exist" [READER R4 §T shape A; R8 §T 4]; XSC "characteristic failure = finished code with no caller" (August tree) [READER R5 §T 2]; twenty-game asymmetry A5: "an emergent agent layer built as a single switch will be switched off … the data behind it becomes decoration" [CHECKED 20G:245]. Independent: code + audit + COMP/THR (shared descent, 1) + 20G (different research line) → 4 | Valoria's knobs are swept **dials** (each has arms, e.g. `scar_weight_shift` 0/0.5/1), not 20G's single switch; the defect is the shipped value, which is Jordan's [OPEN — Jordan tuning]. The tree does delete dead carriers when a ruling or zero-caller sweep kills them (`DECISIVE_OB`, TN 6/8 rows [CHECKED `dice_engine.py`:164-173; `core.py`:47-49]) | built and inert | relaxed exit closes positions on DONE-test (m:121-135); no position flips `age_step`, `illness_rate`, `scar_excludes_actor`, `intent_disclosure`, `said_slant`, `telling_privacy` (BASELINE B5 "none") | **SOUND** |
| T-IN-4 | **Acts record that something happened, not what** | REPOSITORY PATTERN + NULL (expression) | 52/52 act-minted Propositions predicate `''`; 112/120 Records `subject_matter` None; ~48/1,318 acts with an effect beyond an existence flag [CHECKED `proposals/2026-10-13-narration-mechanisms.md`:38-53; one seed, scratch instrument, outputs uncommitted]; five investigation rows `writes: []` [CHECKED via BASELINE B3]; H-185 [CHECKED]; audit T5 [AUDIT]; "tracking is not expressing" (D6 / N-2) [READER R4 §T; R8 §T 2]; "legibility caps state: record only what can be surfaced" [READER UP05 §T 6]; "corpus builds substrates and clocks, not attribution/discourse" [READER UP01 §T 1]; Tale-Spin and "10,000 bowls of oatmeal" [READER UP02 §T 8]. Independent: code datum + COMP/THR (1) + the uploaded research line (N1/N2/3S share an author line → 1) → 3 | tellings carry a `Said` with a predicate; 8 Records carry content (`narration-mechanisms.md`:50-53) | executes (the empty fields are what runs) | IN-26 sink (B-Q, BLK SC-01), IN-37 render (B-U, BLK SC-01 step 16), FI-01 degree producer (B-O); H-185: zero plan mentions (BASELINE B4) | **SOUND** in shape; magnitude [CONFIDENCE: low] (one seed) |
| T-IN-5 | **One resolver, several fidelities** (FM/XCOM vs Total War's second resolver) | CONVERGENCE | COMP K7, D4, refuse #14 [READER R4 §T]; THR TL06 §5.3 and PRE (same descent) [READER R8 §T 5]; Jordan SM-5 ("fire emblem style", independent); the August suites applied it [READER C6_1 §G]. Independent: 2 (precedent line, owner) | the PLAYABLE fidelity is designed, not built; the bout's AUTOMATED path is the one that runs | executes for the duel (`fight` → one engine); grid absent ("Grid-based unit combat does not exist anywhere in the tree", `_part2`:181 [CHECKED]) | IN-46 "no build batch" (m:272; `_part4`:32-36 [CHECKED]) | **SOUND**, half UNREACHED |
| T-IN-6 | **Hostility with no damper is switched off, not tuned** | FAILURE SHAPE | *Guild 3* publisher account, T1 [CHECKED TD:195; 20G:241]; RimWorld insult spiral, Skyrim kin revenge [SESSION, via `VCD`:985]; COMP T-04 "accrual beats bounded restoration", 11 instances, 7 verified [READER R8 §T 6]; uploads' "half-strength setting" directive [CHECKED 20G:245; READER UP03 §T 8, UP04 §T 9]. Repository: `_eff_march` appends a −1.0 grudge row toward the winner for every loser, no cap, decay or closer [CHECKED `loop/effects_combat.py`:246-261]; H-25 "a termination bound per self-feeding loop" absent; H-106 loop enumeration incomplete [CHECKED HR]. Independent: Guild 3 (T1) + COMP + repo → 3 | Valoria's root forbids appraisal-without-registration: a threshold never acts (T-b), scoring reads own state; "damped today only because the realm fights no field" (`VCD`:985 [CHECKED]) | built and inert (no field is fought in the realm, HR:3264-3265) | `forgive` IN-12 step 13 (B-Q); H-25 named by IN-10; K-45's signed LOOP row "not written" [READER C8_2 §H] | **SOUND** as a hazard; UNREACHED in play |
| T-IN-7 | **No precedent solves the scale handoff above the bout** | NULL | COMP D3 (personal leverage N=1…1000+), D4 (auto-resolve calibration) [READER R4 §T]; PRE N-3, N-4 [READER R8 §T 1] (same descent → 1); "high scale loses attribution; fixes: personification, avatar, pops, scale-shift" [READER UP02 §T 3]; repository: battle is one 18-tick call with no yield [CHECKED `massbattle.py`:281-283], thread→mass hook "Empty hook — threadwork lands in a future cycle" [CHECKED `orchestration.py`:333-335]; audit S-coverage [AUDIT :61]. Independent: 2 | Valoria's one carried vertical seam (contest at RESOLVE/ENCOUNTER) is a real answer for the bout | absent above the bout | M-6 LEAVE (`_part7`:44 [CHECKED]); no position for thread→mass | **SOUND** |
| T-IN-8 | **Research enters as vocabulary; magnitudes enter from nowhere** | REPOSITORY PATTERN | 0 of 45 VT rows cite research or a game; 2 of 198 HR rows cite `research/`; plan cites none; Layer 1 excludes by rule (§3.1, §4 [CHECKED]); `VCD` maps by name (§1.3 item 5); the two tier-3 rosters built and deleted unread (`rosters.yaml`:84-89 [CHECKED]). Independent: 1 (one tree), many sites | the refusal to invent a magnitude is a stated discipline (`massbattle.py`:198-207 "not the place to invent one" [CHECKED]); it is the discipline, not neglect, that leaves defaults standing | executes (defaults) | J-13 asks for a source (J.2 rank 1) | **SOUND** |
| T-IN-9 | **The plan's accounting moved execution from the position to the requirement, and no position owns the requirement** | REPOSITORY PATTERN | relaxed exit: BUILT on DONE-test, realm count "not required" (m:121-128 via BASELINE B2.1); IN-12's exit "a row that reads 0 there is a named residue … R-05 stays unmet; no position is invented to fix it" [CHECKED `_part5`:65]; R-05 earliest `met` "conditional … only if every owner's EXIT above recorded ≥ 1 execution" [CHECKED `_part2`:262-266]; H-207: four causes stand between a seat question and an executed `revoke`/`confer` on `build_realm(0)`, zero plan mentions [CHECKED HR; BASELINE B4]; failure shape A (EU4) [READER R4 §T]. Independent: 1 tree + 1 precedent family → 2 | the executed-set pin fails when the set moves (`test_season_shape.py`:7738-7742) and 21 → 17 is recorded as a regression, so movement is observed; the requirement-level reading is itself [ASSUMPTION; medium] (m:134) | built (instrument) | no owner of computed-play execution for R-04 conjunct (1) (`confer`, `establish`, `revoke`) or R-05 | **SOUND** |
| T-IN-10 | **Show the inputs and the band, not the trigger; randomness must read as fate** — and the player surface shows neither | CONVERGENCE (precedent) + REPOSITORY PATTERN | COMP S6 "Publish every input. Publish a band, not a number. Never publish the trigger point" and D2 legibility-vs-depth null [READER R4 §T]; "randomness must read as fate" [READER UP02 §T 4]; "randomness shaping inert without surfacing" [READER UP05 §T 8]; Layer 1 §C.11 `explain(p : PersonInterior, v : Value) -> Derivation` [CHECKED `04_CODE_ARCHITECTURE.md`:847-863]. Repository: `explain` has no definition (`grep -rn "def explain" engine modules` → 0 [CHECKED]); `p_success` has no game-path caller [AUDIT A3]; "odds" occurs 0 times in v9 [CHECKED grep]. Independent: COMP line + uploaded line + Layer 1 → 3 | the odds are non-monotone (§9 B-instrument run), so "show the band" would show a sawtooth | absent | IN-47 (character sheet) "no build batch"; nothing names `explain` (`grep -n "explain(" workplans/…v9*` → 0 [CHECKED]) | **SOUND**, UNREACHED |
| T-IN-11 | **Apparatus grows where the game cannot read it, and moves when banned** | REPOSITORY PATTERN (process) | tracked run output 88,377 lines in 10 files under `engine/season/runs/` [CHECKED `git ls-files … \| xargs wc -l`]; `ci_checks_registry.yaml` `subject:` is `compliance` on 32 rows [CHECKED grep]; dated correction narrative in game-code docstrings (`sigma.py`:101-102 still says capability is "EMPTY ON EVERY CORPUS PERSON TODAY", which `requirements.yaml`:1284-1287 records as contradicted [CHECKED]); audit T6, §7 [AUDIT :265-306, :394-406]; "BUILT meant design finalized" (August) [READER R5 §T 5]. Independent: audit + my recount (same object) → 1 source, re-measured | the quarantine (`.designs/`), retirement of `balance_oracle`, deprecation of `mc_v18` show removal happens | n/a (process) | IN-44 Layer 0/1 edits (J); no position for `runs/` | **SOUND** |
| T-IN-12 | **Allegiance is recomputed on the current tick; nothing in either corpus delays it** | NULL (precedent) + REPOSITORY PATTERN | "Lagged allegiance absent in all 13" [READER UP04 §T 2]; nine titles "allegiance never arrives late" (but self-contradicted by Bannerlord at L128) [READER UP03 §T 7, §K 4]; 20G A1 "Give allegiance a delay" [CHECKED 20G:227]; Pax Pamir punished switching [CHECKED TD:19]; repository: cast loyalty a cosine of authored values against a role template at world-gen [AUDIT A4 ii, `cast.py`:318-331]; regard at read moves by judged deeds and told valence (A-12) [READER W2 §V]. Independent: one research line (D1/D2/D3/3S, same author line) → 1 | Valoria's regard-at-read does lag (deeds must be witnessed or told, `told_by` chains), so allegiance-as-regard is delayed by carriage; the static part is the initial loyalty | executes (cosine at genesis; regard at read) | IN-69 salience by alignment, IN-70 opinion of a faction at read (B-X, B-R) | **SOUND** narrowed: static at seeding, lagged by carriage after |
| T-IN-13 | **Belief with provenance is where Valoria is ahead of the genre** — provenance and channel loss, not deceit | CONVERGENCE | 20G A9 "Nothing in twenty titles models where a belief came from except The Guild 2 and Tropico" [CHECKED 20G:235]; Talk of the Town fallibility (DOCUMENTED) [READER R8 §K 12]; *Guild 2* evidence with strength, believability, decay [CHECKED TD:191]; repository: `told_by` chains, a cell value that a Partial-band telling loses in the channel (`_told_value`, `witness.py`:134; "what a copy may LOSE in its value is already owned", `options.py`:1217-1219), confidence refraction `refraction_gain` 0.5 [CHECKED `witness.py`:231-239, :495; `fixtures.py`:800]. Independent: 2 research lines + code | **no person lies**: H-198 (absent) "A TELLER NEVER LIES … a deed claim is `(x, <kind>, True)` and no deposit ever holds it False, so a lie about a deed can never be caught" [CHECKED HR:4331-4336; `person_q.py`:74-76 deed-claim shape; marker `person_q.py`:681]; deception is "G7 recorded, H-198" (`_part4`:76 [CHECKED]), recorded, not scheduled. Carriage is thin: 4 of 1,270 `told_by` claims arrived by a telling (one seed) [AUDIT S-DOWN]; H-200 competence and H-191 intent reconciliation absent; actor's own deposit unrefracted | executes (provenance, channel loss); absent (deceit) | IN-18 G5/G8 (BLK); G7 none | **SOUND, narrowed** to provenance and channel drift on cell values; deception is a MISSING area (M-IN-14) |
| T-IN-14 | **The season force is sized from stores and weight, never from a troop stock; the verb that should raise troops moves grain** | REPOSITORY PATTERN | (1) the season seam passes each side's `Person.weight` tuple and nothing else that sizes a force [CHECKED `seam/wrappers/mass_battle.py`:191-193]; (2) the module builds one `Unit` of one `Line` infantry `Subunit`, `troops` = raw weight sum, `command=4`, `_SEASON_FORCE_POWER = 4`, labelled "minimum-viable defaults … no canonical spec exists for army -> Unit construction of ANY kind" [CHECKED `modules/mass_battle/massbattle.py`:158-196, :226-230]; (3) `levy` writes `Rung.stores` ×2 [CHECKED VT:629-652]; (4) IN-52: "`levy` moves stores, not troops … a season field is one troops-sized subunit (J-18)", LF-1 "the feed bounds troops by the treasury" [CHECKED `_part4`:137]; its design rejects "Converting stores into troops. That mints persons" [CHECKED `proposals/2026-10-07-settlements-computation-modules.md`:401]; (5) H-49: `Person.weight` "is set only when a Person is constructed", no runtime writer, grade absent [CHECKED HR, row H-49]. Independent: one tree, five sites in four owners (seam, module, verb table, plan) → 1 source, 5 sites | a composite-army builder exists on the harness side: `build_army` builds a multi-subunit `Unit` with per-subunit shape/role, `troop_type` quality via `Subunit.of_type` (`TROOP_TYPE_STATS` "levy": power 1, discipline 1, morale 2) and an `officers=` span of control [CHECKED `systems/mass_battle/sim/engine.py`:213-244; `units.py`:713; `troop_types/registry.py`:41]; several Units per side run through `run_multi_unit_battle` [CHECKED `orchestration.py`:2683], "not reachable from here" (`massbattle.py`:247 [CHECKED]); equipment "NOT YET WIRED" (`equipment/__init__.py`:10 [CHECKED]); experience has no carrier (`grep -rni "experience\|veteran" modules/mass_battle` → 2 comment lines, `core/state.py`:230, `orchestration.py`:357 [CHECKED]) | executes in the season loop (the stub is what runs); built and inert on the season path (`build_army`, `run_multi_unit_battle`) | IN-49 (B-K: `levy` over a full larder, `_part5`:211-216), IN-52 (B-T: stores bound troops); MB-08 LEAVE: #445 U-1 "musters with inputs beyond headcount", U-2 "one equipment model", DEPS "IN (the season-side reader of any of them)" (`_part7`:26-29 [CHECKED]) | **SOUND**; CONTRADICTED by Jordan's statements 1, 3, 4, 5 (2026-10-16) as a design |

**Document-stated nulls and throughlines, disposition** (COMP-2 §3.4, PREC-NULLS N-1…N-9, PMM/XSC, FASE/HCC, `#445` 02 [READER R4 §T, R8 §T, R5 §T, R6]):
N-1 argument content → SC lane (stands). N-2 expression → T-IN-4. N-3 leverage across N → T-IN-7. N-4 auto-resolve calibration → does not
arise (one resolver; T-IN-5). N-5 certifying generated content → the story bar (IN-19, M2) is the tree's attempt; a cause-graph property, not a
quality certificate [READER W1 §V]; stands. N-6 legibility vs depth → T-IN-10. N-7 appointed governor → SE/FA. N-8 unit quality cap → MB.
**N-9 social-state fog of war: NARROWED, not refuted outright.** Talk of the Town (S05 §1.3) contradicts it as a genre null; Valoria
contradicts it only for channel drift on cell values (`_told_value`, T-IN-13). For deceit N-9 stands inside Valoria too: no teller lies and no
deed claim is ever held False (H-198 [CHECKED HR:4331-4336]); M-IN-14.
COMP "six of eight, Valoria owns the primitive" is **CONTRADICTED** by its own table (X1 "Absent entirely") [READER R4 §K 8].
XSC "opposition is almost never a true opposed roll; score/2 is the single highest-leverage unexecuted decision" [READER R5 §T 1]: **superseded
in shape** — `_obstacle_of` executes score/2 for a person subject [CHECKED `sigma.py`:112-129]; the values feeding it are T-IN-1's defaults.
PMM "people exist, zero loaders" [READER R4 §T]: **superseded** (430 built persons). FASE T10 legitimacy-derived: converges with IN-23's
Query (§1.2), uncited. HCC ripple chains: rest on tier-4 stats and retired Keys (§1.3 item 3); not a throughline the season can carry.
`#445` 02's "finishing the plan consolidates the engine; it does not change this verdict" [CHECKED `02_against_precedent.md`:73]: a
verdict, not a throughline; the uploaded audit reaches the same verdict independently ("not yet a game of distinct persons") → SOUND, 2
independent.

### 7.2 Conflicts inside the lane, and where code or plan contradicts a throughline

1. **Layer 1 contradicts itself over the dedup filter the loop runs.** `03_VERBS_AND_LOOPS.md` §C.3:138-140 [CHECKED]: "No cap, no dedup,
   no per-venue limit, no *already-before-this-body* rule — each of those would be the engine deciding a person's options"; §C.2:131-134
   [CHECKED]: "at one scene … nobody ever chooses what to leave undone … Triage is the mechanism the budget exists to create".
   `_drop_what_was_already_done` [CHECKED `loop/deliberate.py`:305] is called on every queue [CHECKED :225]. Its own justification is §C.2
   (S26.3) plus a **measured monoculture** before it existed — "`create_record` x10, `reconstruct` x9, `research` x7, `move` x2 — **all by
   `p_carin`**", with seven verbs "gone from the world entirely" (`deliberate.py`:314-318 [CHECKED]); it cites `player_agency_v30.md` §6.3
   only for its unit. Its key is `(verb, subject)`, or `(verb, subject, counterparty)` where the row names one (`:346-352` [CHECKED]), and
   it bars only what was REALISED, not attempted. So the conflict is inside ratified Layer 1 (§C.2 against §C.3), not Layer 1 against a
   reference document, and deleting the filter re-opens a measured failure. Audit A5a [AUDIT] (which read it as Layer 1 vs reference): the
   contradiction survives at `5445e34`, its framing does not.
2. **AX-7's falsifier names three sites that no longer exist and one gloss Layer 1 contradicts.** `01_AXIOMS.md`:314-317 names `witness.py`:191,
   :271, :361 [CHECKED]; the Claim constructions are now at :532, :648, :671, :700, :850 [CHECKED grep]. The gloss "No state is hidden from the
   player" (`01`:301-302) sits beside §C.11's "engine owes the ARITHMETIC of what the character already holds, and nothing else"
   (`04`:849-850); `04` never names AX-7 (`grep -c "AX-7"` → 0) [CHECKED]. Audit A2b, A9 [AUDIT]: survive.
3. **`requirements.yaml` calls a path that no longer exists "CANONICAL"** (`:34-35` → `systems/_architecture/reference/scale_transitions_v30.md`;
   the file is under `.designs/`) [CHECKED `ls`; `git ls-files`]. Audit A2c survives.
4. **GD-2 (mutable canon) has no carrier and contradicts Layer 1.** "Deterministic threat response precedes stochastic action selection",
   a faction mandatory-actions pass [CHECKED `canon/04_game_design_constraints.md`:28]; the season loop has no faction actor (AX-1) and "a
   threshold never acts" (T-b); ED-IN-0202 recorded that GD-2's violation test failed against the retired `mc_v18` [CHECKED
   `registers/editorial_ledger_in*.jsonl`]; v9 never names GD-2 [CHECKED grep: only GD-1, GD-3 occur].
5. **T-IN-1 against J-13's interim**: Jordan's constraints quoted in the plan — "pool only it is", "a derived score … not a character
   attribute" [CHECKED `_part2`:416] — rule out a stored attribute for the contest, while K-1/K-2 for combat would add `Person.attributes`
   (`_part7`:44). The two scales are heading for different per-person sources.
6. **Plan internal drift** already recorded in §3.3 (contested verbs 3 vs 4; `len(VERB_TABLE)` 46 vs 45; IN-14 batch three ways; `march`
   readings). Not re-listed. IN-14 adds one more: its entry reads STATE B, the repair's shape "RULED 2026-10-12 … MORE ROUNDS … §26.3:
   the budget varies by office", BATCH B-J (`_part4`:26 [CHECKED]); the index row reads ask-then, B-Z (v9:256 [CHECKED]); the code carries
   neither (`grep -n "granted_acts" engine/season/decision/budget.py` → 0 [CHECKED]).
7. **v9 rules out Jordan's mass-battle model on purpose (T-IN-14).** IN-52 "`levy` moves stores, not troops" and its design's rejection of
   "Converting stores into troops. That mints persons" (design :401 [CHECKED]) stand against Jordan's 2026-10-16 statements that troops are
   "levied from settlements as their own resource" and that "levy typically doesn't refer to goods/stores". R-04 conjunct (1) names `levy`
   as its verb (`_part3`:85 [CHECKED]) and U9's acceptance reads "a `levy` executes with `Act.via` set" (`_part5`:213 [CHECKED]), so a
   Jordan requirement is written on a verb whose meaning he has now ruled wrong.
8. **IN-31's exit against Jordan's H-207 ruling.** IN-31 (B-Q) exits on "a seeded corpus run where `revoke` has more than one outcome
   across seat provenances" (`_part5`:127 [CHECKED]); H-207's ruling (A), Jordan 2026-10-12: "a computed `revoke` is NOT driven: no motive
   in the chooser's scoring offers it, and none is to be special-cased in" [CHECKED HR, row H-207 `cite`]. Hand-forced, the chain
   `revoke` → `confer` works on `build_realm(0)` (same row). The exit needs an execution the ruling says nothing will produce until a
   motive is designed; no position designs one (H-207: 0 plan hits).

### 7.3 Shared with other lanes

T-IN-1: PC, MB, SC, NPC. T-IN-2: PC, MB, SC, WR. T-IN-3: NPC, MB, SC, WR. T-IN-4: WR, FI, FA. T-IN-5: PC, GO. T-IN-6: NPC, FA. T-IN-7: MB,
WR. T-IN-10: GO, SC. T-IN-12: NPC, FA. T-IN-13: NPC, FI. T-IN-14: MB, SE, FA, NPC, PC. T-IN-8, T-IN-9, T-IN-11: IN only.

### 7.4 What the throughlines do not establish

- That any default is the **wrong value**: values are Jordan's [OPEN — Jordan tuning]; T-IN-1 establishes that no per-person source exists,
  not that `pool_default` 2 is miscalibrated.
- That T-IN-4's emptiness persists after IN-26, IN-37 and SC-01 land: the datum is one seed of a scratch run.
- That the world fails R-WORLD over a campaign: nothing in this lane or the audit ran beyond four seasons (`m1_acceptance.py`'s invariant row is
  24 seeds × 4 seasons, BASELINE B7).
- That the research converges independently where it says so: the uploaded line (N1, N2, D1–D3, 3S) is one author line by its own statement
  (3S:5 "All five appear to be prior output in this same research line"), so it counts once wherever it appears.

## 8. MISSING AREAS

**Verdict.** What the game lacks in this lane is mostly not verbs: every one of the 45 rows and the 12 IN-12 additions has a position —
but one row is **misnamed** and the verb its name denotes is missing: `levy` moves grain, and **nothing raises troops** (M-IN-12, M-IN-13;
Jordan's statements 1, 3, 4 and 5, 2026-10-16). The season's mass-battle input is a one-unit stub sized by raw weight, and v9 schedules a
stores-bounded feed (IN-52) that rules Jordan's model out by design. Beside it the lane lacks **per-person magnitudes below the seams**
(M-IN-1), **a player surface** — the grid fidelity, the character spaces and the derivation the architecture owes the player (M-IN-2,
M-IN-3), **a motive that makes a person revoke or establish an office in computed play** (M-IN-4; `confer` executes since IN-53, and
Jordan ruled that no motive for `revoke` be special-cased), **deception** (M-IN-14) and **the scale handoff above the bout** (M-IN-6). Each
is either unscheduled in v9, scheduled only as LEAVE, or scheduled with an exit that does not deliver its demand.

### 8.1 Counts

`examined 75 candidates; 24 entered (14 MISSING, 10 HOLLOW or BLOCKED); 30 rows PLANNED-UNBUILT or BUILT-DARK (8.4); 21 dropped (8.5)`.
The walks raised 116 items before merging: 38 verbs whose class or owner raised a question (table 8.0, every row but the first; the 7 in
"E, no question" are covered by one position each); 18 clauses of THE NINE (the first walk's 14, plus four it missed: R-01's positive-plant
caveat, R-04 conjunct (2), R-04 conjunct (3)'s owned rows, R-08's inclination clause); 29 hole-register rows (the first walk's 24 plus
H-44, H-92, H-111, H-198 and H-203, which BASELINE B4 lists and the first walk skipped); 13 audit findings (A2a–c, A3, A4 i–v, A5a–b,
A9, T6); 14 throughlines; 4 Jordan statements of 2026-10-16 (troops levied from settlements; the 4/4 Line is a stub; faction-assembled
composite armies; `levy` misnamed). Where two walks met one area it is counted once. The first draft's line read "examined 63 … 19 verbs
… 12 audit findings … 82 items"; its verb and audit counts were wrong (19 for 38; 12 for 13), corrected here.

### 8.0 The verb walk (BASELINE B3: 45 rows; E 17 · R 10 · N 18)

| class | verbs | owner (batch) | disposition |
|---|---|---|---|
| E, no question | `create_record`, `give`, `issue`, `move`, `release`, `transfer`, `utter` | — / IN-12 give+Rung (B-R) | covered |
| E, writes nothing | `speak`; `interview`, `research`, `surveil`, `reconstruct` | SC-01 step 12 (B-N); FI-01 grades three (B-O), `interview`/`reconstruct` named residue (`_part2`:184 [CHECKED]) | 8.4; `reconstruct`'s value space → FI lane |
| E, by-person default | `tell`, `fight`, `accept`, `challenge`, `petition` | IN-12 step 9 (B-Q); PC-10 (B-Y); K-1/K-5 unscheduled | M-IN-1, H-IN-2; `petition`'s addressee 8.4 |
| R | `build`, `found` (IN-28, B-K); `levy` (IN-49, B-K; **misnamed**: a store extraction, M-IN-13); `migrate`, `work` (IN-45, B-K); `survey` (IN-12, B-K); `examine` (FI-01, B-O); `restore` (SE-03 B-K; IN-35 B-S); `commit` (IN-68, B-X); `dispatch` (FA-01, B-V; posts J-8 ask-then) | as listed | 8.4; computed execution → H-IN-1 |
| N, never attempted | `convene`, `determine`, `open_case` (SC-01, B-N); `destroy_record` (IN-26, B-Q); `march` (IN-13, B-M); `oblige` (IN-10/FA-04); `comply` (IN-09, slotted by `_part3` §B.0 R1 [CHECKED `_part5`:47-48]); **`confer`, `revoke`, `establish`** | `confer`: executes `via` its seat in the realm since IN-53 (`5652e846`, `_part7`:123 [CHECKED]), 0 in the corpus; `revoke`: IN-31 (B-Q), whose exit needs a computed `revoke` that Jordan's H-207 ruling (A) says no special-cased motive will drive; `establish`: IN-10's enabler unbatched (`_part3`:109 [CHECKED]), IN-48 in B-JR "unscheduled" | **M-IN-4** (the motive), H-IN-11 |
| N, no predicate/effect | `carry`, `forge` (IN-45); `evade / defy`, `construe` (IN-09); `exchange` (IN-33, restorable); `succeed` (IN-61, B-R); `thread_read` (PC-06 K-3, B-S); `tie / knot` (IN-32, B-S) | as listed | 8.4; `carry` may stop at a Layer 1 amendment (`_part2`:265-266 [CHECKED]) → H-IN-6 |

### 8.2 MISSING

| ID | the area | demand source(s) · strength | code state [CHECKED] | plan state | absence test (command → result) | what its absence does | NERS axis |
|---|---|---|---|---|---|---|---|
| M-IN-1 | **A per-person source of capacity for the body, the contest and the commander**: a `Combatant` built from the person, a contest pool from the person, and a commander's command from the person who commands. (The force itself is M-IN-12: Jordan's statement 1 sizes and grades troops by a levied stock, equipment, experience and commander, not by the persons' own capacities) | D1 R-09 ("two persons with different `capability` resolving the same contested verb at different pools", `_part2`:423 via BASELINE B2; `fight`/`accept`/`march` are 3 of the 4 contested rows); D1 R-06; D5 A1/G1/T1 · **STRONG** | `party_end` is the one derived field (`seam/wrappers/combat.py`:130-138); `Combatant` defaults (`combatant.py`:93-94); `_SEASON_FORCE_POWER = 4`, `command=4`, raw weight as troops (`massbattle.py`:180-207) | K-1/K-5 "NOT scheduled", K-2 "not ratified" (`_part7`:44); M-2…M-6 LEAVE; PC-08 LEAVE | `grep -n "attributes" engine/season/state/carriers.py` → 2 hits, both comments on Python class attributes (:405, :439); no `Person.attributes` field [CHECKED]; `grep -n "K-1\|K-2" workplans/…v9_part3.md` → no batch member [CHECKED via BASELINE B1.1 member lists] | a duke and a copyist fight alike, and every field is commanded at 4 whoever commands it; 5,643 + 10,154 lines of module depth are reached through `end` and a weight sum | R-VARIETY (bottom-up), S (vertical: the seam drops what the person is) |
| M-IN-2 | **The PLAYABLE fidelity and the character spaces**: grid suspension at ENCOUNTER (IN-46) and creation/development/chronicling (IN-47) as built mechanisms | D1 R-04 conjunct (3): "every `scales:` row reads `in_loop`" (`_part2`:214 [CHECKED]); D5 A2a · **STRONG** | `play_surface.py`:40-51: a callback per person id over `auto` and the same `View` [CHECKED]; "Grid-based unit combat does not exist anywhere in the tree" (`_part2`:181 [CHECKED]) | designs landed at B-C; "no build batch" (m:272-273; `_part4`:32-41 [CHECKED]); "R-04, hence M1, cannot read `met` under v9 until a build batch exists for both" (`_part2`:209 [CHECKED]) | BASELINE B1.1 batch member lists: neither IN-46 nor IN-47 in any batch [CHECKED by reading B-K…B-Z rows] | the player can only override a choice among the engine's candidates; M1 cannot be met under v9 by the plan's own reading | R-PLAYER (all seats), S-pause |
| M-IN-3 | **The derivation the architecture owes the player**: `explain(p : PersonInterior, v : Value) -> Derivation`; **a shown band of odds is a separate, unruled question** | `explain`: D3 Layer 1 §C.11 ("The engine owes the ARITHMETIC of what the character already holds, and nothing else"; "the derivation of a value the character already has", `04_CODE_ARCHITECTURE.md`:849-855, :860 [CHECKED]) · **STRONG**. An odds band: D5 A3 legibility; D6 T-IN-10 (3 sources) · **MEDIUM**, and not D3: odds for an act not yet taken are not a value the character holds, so §C.11 does not owe them; AX-7's gloss "No state is hidden from the player" (`01_AXIOMS.md`:301-302 [CHECKED]) points the other way (§7.2 item 2) | absent | absent | `grep -rn "def explain" engine modules` → 0 [CHECKED]; `grep -n "explain(\|odds" workplans/valoria_master_workplan_v9*.md` → 0 [CHECKED] | the player cannot intuit outcomes from choices, and the odds the kernel produces are non-monotone (§9, B-instrument) | E-LEGIBILITY, R-PLAYER |
| M-IN-4 | **A motive that makes a person `revoke` or `establish` in computed play** (the seat verbs' remaining half: `confer` already executes) | D1 R-04 `met` (1) names the three (`_part2`:211-213 [CHECKED]); D1 R-05; D4 H-207 absent, zero plan mentions; D4 H-203 absent (offices named by no record; its standing-form producer landed as IN-53, its writ half is IN-09's) · **MEDIUM-STRONG** (narrowed: Jordan's ruling bounds it) | `confer`: executes `via` its seat in the realm since IN-53 (`5652e846`; `_part2`:178, `_part7`:123 [CHECKED]), 0 in the 143-case corpus (`requirements.yaml`:895-898 [CHECKED]); the realm assertion was deleted 2026-10-13 under the relaxed exit (v9:128-129 [CHECKED]), so today's realm count is unasserted [UNVERIFIED: `aperture` not run]. `revoke`: hand-forced, `revoke` → `confer` works end to end on `build_realm(0)`; computed, 0, because the chooser offers no motive (H-207 causes 5, 6) and Jordan ruled 2026-10-12 that "a computed `revoke` is NOT driven: no motive in the chooser's scoring offers it, and none is to be special-cased in" (H-207 ruling (A) [CHECKED HR, row H-207 `cite`]); cause 3 LANDED, cause 1 partly ruled. `establish`: on IN-10's enabler, reverted | `revoke`: IN-31 (B-Q) owns its cost and outcome, exit "a seeded corpus run where `revoke` has more than one outcome across seat provenances" (`_part5`:127 [CHECKED]) — it presumes the execution H-207 (A) withholds (H-IN-11). `establish`: "on IN-10's enabler, unbatched" (`_part3`:109 [CHECKED]); IN-48 B-JR "unscheduled". IN-48's EXIT is delegation, not seat exercise generally (`_part5`:208 [CHECKED]). The motive: none | `grep -c "H-207" workplans/valoria_master_workplan_v9*.md` → 0 per file [CHECKED]; `grep -n "H-203" workplans/valoria_master_workplan_v9*.md` → 0 [CHECKED]; `grep -c "IN-53"` over the eight files → 13 lines, 8 citing `5652e846`, none an open entry [CHECKED] | offices are filled by persons but never stripped or created by them; a seated rival can be removed only by killing him (§9.4 R-CHOICE) | R-WORLD (no patronage or purge drama unwatched), R-CHOICE |
| M-IN-5 | **Delegation and regency**: a seat exercised by a non-holder | D3 Jordan 2026-09-03 "Regency and puppet rulers must be possible" [READER W2 §V IN-48]; D4 H-108 absent · **STRONG** | built `40926a95`, reverted for contradicting Layer 1 (01 §E.2.4) [READER C4_2] | B-JR "unscheduled; left B-J" (p3:213, :276 via BASELINE B1.3) | BASELINE B1.1 B-JR row: "unscheduled" [CHECKED] | a weak heir cannot be ruled through, so the holder ≠ controller drama (COMP X1) has no carrier | R-WORLD, R-CHOICE |
| M-IN-6 | **The scale handoff above the bout**: a battle that yields to a general's duel; threadwork into the field; a pause the season loop honours | D1 Jordan in `requirements.yaml`:30-34: "the repository outlines all of this pretty explicitly at the different scales … needs to accommodate it all" [CHECKED]; D1 R-04; D5 A2 S-coverage · **MEDIUM-STRONG** | one 18-tick call (`massbattle.py`:281-283); "Empty hook — threadwork lands in a future cycle" (`orchestration.py`:333-335) | M-6 LEAVE (`_part7`:44); no position names `threadwork_check` | `grep -n "threadwork_check\|M-6" workplans/valoria_master_workplan_v9*.md` → `threadwork_check` 0; `M-6` only as LEAVE: `_part7`:44, :51 and the main file's "M-2..M-6 → PC-08" at v9:309, :364 (PC-08 LEAVE) [CHECKED] | scales compose by summary, not by handoff: no person's act inside a battle changes it | S-vertical, S-pause |
| M-IN-7 | **AX-7's two missing inputs**: a reader's competence (H-200) and the performer's own fallible reading of their act (layer 2) | D3 AX-7 names "the reader's competence" as an input to divergence and gives layer (2) "its OWN mechanism" (`01_AXIOMS.md`:278-281 [CHECKED]); D4 H-200 absent, zero plan mentions; D5 A9 · **MEDIUM** (layer 2: permitted or owed is unruled) | `refracted_confidence`'s competence factor is 1 (H-200 [CHECKED]); the actor's own deposit skips refraction (`witness.py`:495 [CHECKED]); AX-7's falsifier names stale sites (`01`:314-317) | none | `grep -c "H-200\|own understanding\|self-reading" workplans/…v9*.md` → 0 [CHECKED] | a practised observer and a careless one hold the same act at the same confidence; a person never misreads their own deed | R-COMPLETE, R-WORLD |
| M-IN-8 | **A hearer's credibility inputs**: whether a declared intent was kept (H-191), the teller's stake (H-180), rank ordering of tellers (H-181) | D4 three absent rows; H-180/H-181 "stays absent" (m:369); D1 R-07 "imperfect knowledge" · **MEDIUM** | `options.py::record` pairs cell claims only; intents are never reconciled (H-191 [CHECKED]) | H-191: 0 mentions; H-180/181: re-checked IN-17, "stays absent" | `grep -c "H-191" workplans/…v9*.md` → 0 [CHECKED] | a liar by deeds is credited like an honest teller, so reputation for keeping one's word cannot form | R-WORLD (hooks), R-COMPLETE |
| M-IN-9 | **Content in acts**: a reader for an authored OUGHT's predicate (H-185), or the field's deletion | D4 H-185 absent, zero plan mentions; D5 T5; D1 R-06 ("goals, ambitions") · **MEDIUM** | Q4 reads only `subject`; `Proposition.predicate` read by nothing for an OUGHT (H-185 [CHECKED]) | none; IN-66 `goals.yaml` may supersede the `ought:` cast field [CONFIDENCE: medium — IN-66's entry not opened in full] | `grep -c "H-185" workplans/…v9*.md` → 0 [CHECKED] | an ambition is a subject with no content, so what a person wants of it cannot steer what they do | N (false N-line candidate), R-WORLD |
| M-IN-10 | **A controlled, multi-season reading over any mechanic, and a control that separates propagation from lost variety** (process; IN only). Not "no instrument": two exist, each with half the shape | Layer 0: `balance_oracle.py` retired, "the campaign-level instrument has **no live successor** — an open gap" (CLAUDE.md §7); D5 audit GAP "nothing runs beyond four seasons"; D1 R-01's own caveats: the wd_collect positive-plant line reads "`detected OVER THE BASELINE on ALL 4 plants: False`" (`requirements.yaml`:406 [CHECKED]) and "no control separates 'flips absorbed' from 'less variety'" (:421 [CHECKED]) · **MEDIUM** (process) | `harness/arms.py` is two-arm, n-seed and already multi-season (`run_arm(model, n, base_seed, seasons)`, `--seasons`, default 2), but its arm is hard-coded to `field_casualty_model` (`arms.py`:153-170 [CHECKED]) and it keeps a retired comparison, `_pool_arm`/`_ARMS_POOL`, "kept because `_pool_arm` is the record" (`:213-230` [CHECKED]); `harness/soak.py` runs many seasons on one driver but single-arm, grading only cost and act mix (`soak.py`:1-9 [CHECKED]); invariants row 24 seeds × 4 seasons (BASELINE B7). The first draft missed `soak.py` and `arms --seasons` | TEST HORIZON confines `aperture 4 0` to propagation readings (m:141-151); IN-20 landed `soak.py`'s grades (v9:354 [CHECKED]) | `grep -n "balance_oracle\|play-length\|campaign-level" workplans/…v9*.md` → one hit, `_part8`:420, "keep the gap statement" [CHECKED]; `grep -n "def run_arm\|sweep(" engine/season/harness/arms.py` → one knob, `field_casualty_model` [CHECKED] | every R-WORLD and R-CHOICE verdict in every lane is an upper bound on four seasons, and R-01's `met` cannot tell absorbed flips from fewer behaviours | R (all verdicts' denominator) |
| M-IN-11 | **A damping bound on self-feeding loops** beyond `forgive` | D4 H-25 absent ("a termination bound per self-feeding loop"); H-106 loop enumeration incomplete; D3 ID-16 "sign every loop" (`VCD`:985 citing `01_AXIOMS.md`:664-681); D6 T-IN-6 · **MEDIUM** | grudge rows appended per lost field, no cap/decay/closer (`effects_combat.py`:246-261 [CHECKED]) | `forgive` (IN-12 step 13, B-Q) is one person-side closer; H-25 is named by IN-10 only; K-45's signed LOOP row "not written" | `grep -n "H-25\b" workplans/…v9*.md` → IN-10 entry only (BASELINE B4) | the first season that fights fields compounds grudges with no brake but persons' choice to forgive | R-COMPLETE (extremes) |
| M-IN-12 | **Troops as a settlement's own resource, raised by a levy, fielded as a composite army a faction assembles**: (a) a troop stock at a rung, distinct from `Person.weight`; (b) a verb that raises it; (c) quantity and quality differing by equipment, experience and commander; (d) a season force built from several subunits, each with its own subformation, chosen by the faction. IN's share is the verb (b) and the season seam's reader (d); the stock and the army are MB/SE's | **D1** Jordan 2026-10-16, statements 1 ("army units that are troops levied from settlements as their own resource … differ in quantity and quality based upon equipment and experience and their commanders"), 3 ("this 4/4 one line formation … as coded is a stub"), 4 ("factions are supposed to be able to assemble armies with different subunits with subformations"); D4 H-49 absent, zero plan mentions; D4 MB-08 LEAVE naming #445 U-1, U-2 with DEPS "IN (the season-side reader of any of them)" · **STRONG** | (a) absent: `levy` writes `Rung.stores` only (VT:629-652); no stores kind is troops; `Person.weight` has no runtime writer (H-49) [CHECKED]. (b) absent (M-IN-13). (c) equipment "NOT YET WIRED" (`equipment/__init__.py`:10); experience: no carrier (2 comment lines); commander: the season passes `command=4` (`massbattle.py`:183) [CHECKED]. (d) the seam passes weights only (`seam/wrappers/mass_battle.py`:191-193); one `Unit`, one `Line` infantry `Subunit`, `troops` = raw weight sum (`massbattle.py`:170-178, :226-230) [CHECKED]. Built on the harness side and unreachable from the season: `build_army` (multi-subunit, per-subunit role/shape/`troop_type`, `officers=`; `systems/mass_battle/sim/engine.py`:213-244), `Subunit.of_type` (`units.py`:713) with `TROOP_TYPE_STATS` "levy" P1/D1/M2 (`registry.py`:41), `run_multi_unit_battle` (`orchestration.py`:2683; "not reachable from here", `massbattle.py`:247) [CHECKED] | IN-49 (B-K) makes the stores `levy` execute (`_part5`:211-216); IN-52 (B-T) "`levy` moves stores, not troops … a season field is one troops-sized subunit (J-18)"; LF-1 "the feed bounds troops by the treasury" (`_part4`:137) [CHECKED]; its design rejects "Converting stores into troops. That mints persons" (design :401 [CHECKED]); MB-08 LEAVE "(musters with inputs beyond headcount), U-2 (one equipment model for both scales)", DEPS "IN (the season-side reader of any of them)" (`_part7`:26-29 [CHECKED]) | `grep -c "troop" engine/season/verb_table.yaml` → 0 [CHECKED]; `grep -rn "build_army\|run_multi_unit_battle" engine/season modules/mass_battle/massbattle.py` → only the `:247` docstring [CHECKED]; `grep -rn "^from systems\|^import systems" modules/mass_battle` → 0 [CHECKED] | a realm cannot raise, spend or lose an army; every field is two one-Line blocks whose only difference is headcount, so no faction can out-recruit, out-equip or out-general another | R-CUSTOMIZATION and R-CHOICE (factions; bottom-up), S-vertical (settlement → army → field), N (the stub is not an N-line: Jordan calls it a placeholder) |
| M-IN-13 | **The store-extraction act has the wrong name, and the name it has belongs to M-IN-12's verb.** The VT row `levy` moves `Rung.stores` from a levied rung to the seat's treasury | **D1** Jordan 2026-10-16, statement 5: "levy typically doesn't refer to goods/stores. that verb is wrong as currently used"; CLAUDE.md §4 ED-IN-0179 (a word must be used "that way *outside* this repo") · **STRONG** (the naming); the new name is Jordan's | the row and its effect are live: `scale_note` "a levy moves a Rung's stores"; `writes: ["Rung.stores", "Rung.stores"]` (VT:629-652); `_eff_levy` "A LEVY MOVES A RUNG'S STORES INTO THE LEVYING SEAT'S TREASURY" (`effects_governance.py`:374-379) [CHECKED] | every plan reference reads `levy` as a stores transfer: IN-49 (`_part5`:211-216), IN-52 (`_part4`:137), R-04 conjunct (1)'s named verb (`_part3`:85; U9's acceptance, `_part5`:213) [CHECKED] | `grep -c "\blevy\b"`: v9 39 lines over 7 files; `hole_register.yaml` 19; `requirements.yaml` 23; `verb_table.yaml` 15; the editorial ledgers 14; tests: 11 files, 96 lines under `engine/season/tests` [CHECKED, this pass] | the player reads "levy" and expects troops; the one act that should raise an army is the one that empties a granary, so the name blocks the verb Jordan's model needs | E-LEGIBILITY (the name misleads), S (the verb vocabulary and the field disagree) |
| M-IN-14 | **Deception**: when a person lies and what the lie says; a deed claim that can be held False, so a lie can be caught | D4 H-198 absent, owner `person_q.py::said_of` at the `ABSENT: H-198 deception` marker (`person_q.py`:681) [CHECKED HR:4331-4336]; telling G7 "recorded, H-198" (`_part4`:76 [CHECKED]); D1 R-07 "imperfect knowledge" (lying is the deliberate half); D6 T-IN-13's precedent (*Guild 2* believability) · **MEDIUM**, and a RULING by the row's own ladder: "two defensible lie rules (alter a held cell value vs. assert an unheld deed) lead to different games" (H-198 `cite`) | `said_of` passes a held claim unaltered; a deed claim is `(x, <kind>, True)` and "no deposit ever holds it False" (H-198; `person_q.py`:74-76) [CHECKED]; `record` (H-183) prices caught contradictions on cells only (`options.py`:1258-1300 [CHECKED]); G7's named falsifier passes with no lie mechanism and so "cannot observe a lie rule's failure" (H-198 `unblocks`) | G7 recorded, not scheduled; no position | `grep -n "H-198" workplans/valoria_master_workplan_v9*.md` → `_part4`:60 and :76, both IN-18's note that G7 is recorded [CHECKED] | a liar by deeds cannot exist, so reputation for honesty and the intrigue of false report have no carrier; N-9 holds inside Valoria for deceit | R-WORLD (hooks), R-COMPLETE |

### 8.3 HOLLOW and BLOCKED

| ID | position | its EXIT (quoted) | the demand (quoted) | gap |
|---|---|---|---|---|
| H-IN-1 HOLLOW | every verb position under the relaxed exit (m:121-135) | "a verb position is BUILT when it is wired and proven by a falsifier on a hand-built world"; "A row that reads 0 there is a named residue … R-05 stays unmet; no position is invented to fix it" (`_part5`:65 [CHECKED]) | R-05 `met`: "`corpus_run`'s `WHERE THE <n> GO` line reads 0 … or every verb … executing ≥ 1 in `aperture 4 0`" (`_part2`:274-276 [CHECKED]) | the plan's exits cannot deliver R-05; the requirement has observers but no owner |
| H-IN-2 HOLLOW | IN-12 step 9 `train` (B-Q) | "`train` forms and writes `Person.capability` only where a case names a vocation, and `pool_default` holds everywhere else" (`_part5`:73 [CHECKED]) | R-09: "two persons with different `capability` resolving the same contested verb at different pools" | delivers by-person pools for the copyist's vocation only (`verb_capability` key `copying`) |
| H-IN-3 HOLLOW | IN-47 creation space (when batched) | "**creation** — no act; a cast entry the world-gen builder seats" (`_part4`:41 [CHECKED]) | R-04 (3) "character creation … `in_loop`" | flips the field by selecting a pre-authored person; no creation act exists to customize (NERS R, §9) |
| H-IN-4 BLOCKED | R-09 by-person conjunct | "none under v9 … waits on J-13's remainder" (p2:32 via BASELINE B2) | R-09 | J-13 remainder, J.2 rank 1 (`_part5`:514) |
| H-IN-5 BLOCKED | IN-61 succession (B-R) | — | R-05 (`succeed`), R-04 | ED-IN-0292 (2) `vacancies` vs AX-7, needs_jordan [READER W2 §H] |
| H-IN-6 BLOCKED | IN-45 `carry` | — | R-05 | `carry`'s fourth gate `Subject` shape "would amend ratified Layer 1 (then it is Jordan's)" (`_part2`:265-266 [CHECKED]) |
| H-IN-7 BLOCKED | `revoke` eligibility | — | H-91: Part E's `remit:revoke` and Jordan's purview "cannot both be the eligibility rule" [CHECKED HR] | unruled; zero plan mentions (BASELINE B4) |
| H-IN-8 BLOCKED (HELD) | `scale:` reader (H-89); nested DELIBERATE in RESOLVE (H-56); common-fact store (RS-24/29) | — | R-04 (H-89); S-pause (H-56) | HELD (J.2 rows 5-7; `_part5`:518-520; `_part8`:337-342 via BASELINE B1.3) |
| H-IN-10 HOLLOW | IN-49 (B-K) and IN-52 (B-T), the levy-to-field feed | IN-49: "`python -m engine.season.harness.aperture 4 0`'s `levy` row executes ≥ 1 with `Act.via` … `levy.taken` in `w.log` from a computed act" (`_part5`:215); IN-52: "with it on … a side's fielded troops are bounded by its levied treasury" (`_part4`:139) [CHECKED] | Jordan, statement 1: troops "levied from settlements as their own resource … differ in quantity and quality based upon equipment and experience and their commanders"; statement 5: `levy` "doesn't refer to goods/stores" | both exits deliver a stores levy and a stores-bounded headcount of the same one-Line force; neither raises, grades or composes troops (M-IN-12, M-IN-13) |
| H-IN-11 BLOCKED | IN-31 `revoke`'s cost and seat provenance (B-Q) | "a seeded corpus run where `revoke` has more than one outcome across seat provenances" (`_part5`:127 [CHECKED]) | R-04 (1), R-05 (`revoke` executing) | Jordan's H-207 ruling (A), 2026-10-12: a computed `revoke` "is NOT driven … none is to be special-cased in"; the exit needs a motive no position designs (§7.2 item 8; M-IN-4) |

### 8.4 PLANNED-UNBUILT and BUILT-DARK

| area | state | what arms or builds it | locator |
|---|---|---|---|
| 12 IN-12 verbs (`seize`, `covenant`, `sabotage`, `tend`, `argue`, `train`, `conceal`, `forgive`, `arrest`, `pardon`, `interrogate`, `raze`) | planned | B-K, B-M, B-Q, B-R | `_part5`:61-80 |
| `march` arrival, occupation | planned | IN-13, B-M | `_part5`:81 |
| legitimacy/stability Queries | planned | IN-23, B-U | `_part5`:88 |
| endings vocabulary (GD-1; H-176) | planned, BLK IN-37 | IN-27, B-U | `_part5`:102 |
| insurgency, emerged faction (GD-3; H-186) | planned | IN-30, B-U | `_part5`:116 |
| paper sink; chronicle render | planned | IN-26 (B-Q), IN-37 (B-U) | `_part5`:95, :176 |
| forcing: Calamity coupling, foreign faction | planned | IN-35 (B-S), IN-36 (B-V) | `_part5`:144, :158 |
| goals, salience, opinion, scar re-read, doctrine pull | planned, next batch | IN-62…IN-72, FA-04…FA-06 (B-X) | `_part3`:277 |
| `found`/`build` cost, holder, closer; `work`, `migrate`, `forge`, `carry`; `levy` referent | planned | IN-28, IN-45, IN-49 (B-K) | `_part5`:109, :190, :211 |
| levied stores → field (not troops; H-IN-10) | planned, to ship OFF; the `field_provisioning` fixture it ships behind does not exist yet (`git ls-files engine/season \| xargs grep -l field_provisioning` → 0 [CHECKED]) | IN-52 (B-T); flip "delegated-ruled" | `_part4`:134-141 |
| `confer` `via` its seat | landed in the realm (IN-53, `5652e846`); 0 in the corpus; realm assertion deleted 2026-10-13 | nothing further scheduled | `_part7`:123; v9:128-129 [CHECKED] |
| IN-14 BOUND-ATTENTION (H-92: a landholding buys scene actions; H-10) | planned-unbuilt, and its plan rows disagree: entry STATE B, shape "RULED 2026-10-12 … MORE ROUNDS … §26.3: the budget varies by office", BATCH B-J; index ask-then, B-Z; code has neither (`grep granted_acts budget.py` → 0) | IN-14 (the first draft's H-IN-9 quoted its FALSIFIER as its EXIT and called it BLOCKED; the ruled shape answers the demand) | `_part4`:25-29; v9:256 [CHECKED] |
| H-44 the nine Dispensation term types | re-scoped: `comply`, `evade / defy`, `construe` execute without term rows | IN-09 (restorable) | HR row H-44 `cite`; `_part2`:236 [CHECKED] |
| H-111 refusal as news | ANSWERED as SKIP at WITNESS except declared keyed kinds [medium; Jordan to correct] | FI-01's deposit half (B-O) | `_part3`:160; `_part8`:234 [CHECKED]; FI lane |
| R-04 conjunct (3), the three other `in_loop: false` rows | owned: grand strategy → FA-01 mechanism (landed `42c5588c`; content B-V); settlement management → IN-07 (B-T, read after `levy` and its siblings execute); investigations → FI-01 (B-O). Only creation and grid have no owner (M-IN-2) | as named | `_part2`:172-186; `_part7`:120 [CHECKED] |
| R-04 conjunct (2), "no Domain-Action mechanism exists in `engine/season/`" | by design: a faction never acts (AX-1); its acts are persons' acts `via` seats; FA-01 mechanism landed | FA-01 content (B-V) | `requirements.yaml`:705-712 [CHECKED] |
| R-08 "Inclination breaks a tie: STILL NOT BUILT" | the requirement text says unbuilt (`requirements.yaml`:1166); the plan says "nothing but IN-08 moves it" and IN-08 has landed (`_part2`:376, :386) — a requirement-vs-plan reading conflict, not re-measured here | IN-08 (landed); IN-57 contributor (landed) | [CHECKED both; CONFIDENCE: medium] |
| `field_morale_loyalty_gain` (H-148) | built-dark at 0 (control, shipped); swept 0.4 / 1 | none | `data/fixtures.py`:608 [CHECKED] |
| `evade / defy`, `construe`; `exchange` | restorable from checkpoints | IN-09 (R1-slotted); IN-33 (before B-V) | `_part5`:47, :137 |
| petition's addressee (S-UP) | docket path planned; `petition`/`issue` "always have `to` == `subject`" [CHECKED `deliberate.py`:355] | SC-03a (landed) → SC-01 (B-N); IN-12 step 5a reads the petition the docket names | `_part5`:77 [CHECKED] |
| `age_step`, `illness_rate`, `age_at_build` | built-dark, 0 | no flip position; "JORDAN'S TO SET" | `fixtures.py`:537-544 |
| `scar_weight_shift`, `confliction_weight`, `scar_excludes_actor` | built-dark | IN-65 (conditional); none | `fixtures.py`:631-651 |
| `refusal_axis` | built-dark, None | "stays unarmed until a ruling" | `_part5`:466 |
| `intent_disclosure`, `said_slant`, `telling_privacy`, `stance_polarity` | built-dark at control | none; `stance_polarity` ask-then (ED-IN-0296) | `fixtures.py`:736-789 |
| `season_factor_draw`, `body_step` | built-dark | none; J-6 "control 0 kept for the corpus" | `fixtures.py`:405, :530 |
| `bench_quorum` | loosest (1) | SC-01 step 11 builds a different term | `fixtures.py`:849 |
| σ-leverage | built, contributes 0 | "this plan schedules none"; open input to SC-01 step 15 | `_part2`:418-421 [CHECKED]; `sigma.py`:147 |
| `urgency`; `benefits_me` | built, inert / no caller | IN-62's `score_terms -> (pursuit, stance, urgency)` keeps `urgency` as a term in a "refactor, hash EQUAL" (`_part5`:255 [CHECKED]) — it preserves the term, it does not invest in it | `choose.py`:150-193 [CHECKED] |
| speech-kind ladder knobs (D-6, D-7a, D-7b) | built-dark, "nothing reads it" | none | `fixtures.py`:672-683 |
| `MB_SUPPORT_RANK_CAP` | OFF | MB-07r (J) | `modules/mass_battle/config.py`:150 |

### 8.5 Dropped

| candidate | reason |
|---|---|
| GD-2 faction mandatory-actions pass | superseded (ladder 1): its subject, faction action selection, was retired with `mc_v18`; Layer 1 (ED-IN-0204, later) makes only persons act and no threshold act. The canon text still stands unstruck: a canon edit, Jordan's (GD is "mutable canon — updates require explicit Jordan ratification", `canon/04_game_design_constraints.md`:23 [CHECKED]); entered as a process item in §10 |
| an outcome or odds term in NPC choice (A4 v) | no demand source: R-08 asks for non-optimal choice, which sampling delivers; the audit itself declines it as a fix that adds a system |
| a producer for σ-leverage | answered by Jordan's constraint as the plan reads it ("pool only it is", `_part2`:416) and named as an open input to SC-01 step 15 (`:420`); moved to 8.4 |
| births and growth | closed by ruling (ED-WR-0011, the cast only shrinks; `cohorts.yaml`:25-32 [AUDIT]); SE/NPC lanes |
| lagged allegiance (T-IN-12) | WEAK DEMAND (one research line); regard at read already lags by carriage |
| H-203 as its own row | folded into M-IN-4: its office-referent producer landed in standing form as IN-53 (H-203 `cite`: "PLANNED 2026-10-10 AS v9 `IN-53` … IN THE STANDING FORM"); its writ half (`comply`, `evade / defy`, `construe` need a writ in hand) is IN-09's, restorable [CHECKED HR row H-203]. BASELINE B4's "unscheduled" reads the row's grade, not this sentence |
| H-105 the world only decays | IN-45 `work` (B-K), `restore` arm built |
| H-195 the `holder` operand | IN-70 reads `regard` of F's head (B-R) [CHECKED `_part5`:325] |
| H-205 vow-break priced at `release` cells | retired-handle note only (m:375); NPC/FA |
| H-206 dead holder's office named by no claim | holder half landed with IN-34 (p3:213); remainder not traced [CONFIDENCE: low] |
| Domain Echo, Sufficient Scope, zoom triggers | irrelevant (ladder 2): Key-based reference rows, replaced by claim landing (RR-3) [READER C4_2 §F] |
| Scene Slate, Standing ladder | reference only (`CURRENT.md`:13; `fixtures.py`:423 per AUDIT A2) |
| mass battle weight→troop conversion | superseded as a design by Jordan's statement 1 (troops come from a levied stock, not converted weight); the IN half is entered as M-IN-12; the conversion itself is the MB lane's (A7, G3). H-49 (`Person.weight` has no runtime writer) moved from this table into M-IN-12 |
| `kill`, `wound`, `execute`, `proclaim`, `steal`, `repudiate` | closed by rulings (direction 3, R-1, R-3, R-8; IN-11) |
| the dedup filter, `_drop_what_was_already_done` | not a missing area but a contradiction inside Layer 1 (03 §C.2 against §C.3, §7.2 item 1); Jordan's, in §10 (K-IN-3) |
| non-monotone odds lattice | a methodology finding (§9 S), and its parameters are Jordan's |
| tracked run output, `params_tables.yaml`, ledgers, process checks, `evacuation_plan.py` | apparatus deletions, not missing areas; §10 |
| a faction readable by the player (AX-1 residual) | folded into M-IN-3 (the player's derivation surface) |
| R-02 bar "passes anything not on rails" (audit §7.2) | an instrument critique, not a game area; §10 process |
| H-128 actor scarred by own act | built-dark knob (`scar_excludes_actor`), 8.4 |
| the two `march` readings (16/16 vs 11 refused) | a reading conflict between trees (§3.3 item 5), not an area |

## 9. NERS PASS

`[SELF-AUTHORED — bias risk]`: this pass extends this lane file's own sections 0–8 and re-tests an audit the same repository committed. Target:
IN's mechanisms — the resolution kernel as the season reaches it, the season loop's barriers and budget, the verb table and its one `resolve`,
the chooser, the witness/refraction path, the seams between scales, and the plan's instruments — with every v9 position ASSUMED BUILT, the
shipped-today state stated where it differs. Head: `engine/season/` (`CURRENT.md`:17 per the audit; Layer 2), `architecture/` (Layer 1),
v9 (the one plan). Instruments: **A + B** (B = the exact band arithmetic below, executed). On the uploaded audit: its attacks on A1, A3, A5a,
A9 and the S-UP petition were **re-opened at `5445e34`** (lines in §7–8); its refusal-emits attack was **re-run** (a YAML count, narrowed
below); its R-CHOICE `levy` table, the S-DOWN 4-of-1,270 figure and the pause finding at `deliberate.py`:116 are **relied on** [AUDIT].

### 9.1 B-instrument: the season roll's band odds, executed

Script `scratchpad/in_lane/odds.py`, importing `_die_result` and `degree_from_net` from `engine/dice_engine/dice_engine.py`, exact convolution,
leverage 0 (as `sigma.py`:147 ships), Ob = c/2 (the score/2 ruling for a person subject, `sigma.py`:112-129):

| pool c | Ob | P(≥ Partial) | P(≥ Success) | Overwhelming |
|---|---|---|---|---|
| 1 | 0.5 | 0.400 | 0.100 | 0 |
| 2 | 1.0 | 0.580 | 0.260 | 0.010 |
| 3 | 1.5 | 0.400 | 0.172 | 0.010 |
| 4 | 2.0 | 0.512 | 0.279 | 0.038 |
| 5 | 2.5 | 0.380 | 0.198 | 0.028 |
| 6 | 3.0 | 0.470 | 0.281 | 0.059 |
| 2 (default) | 2.0 (default) | 0.260 | 0.070 | 0 |

The audit's c = 1…4 figures reproduce exactly; extended to c = 6 the series is a **sawtooth**: every odd pool against a half-integer Ob does
worse than the even pool below it, because a net in integers meets an Ob of k + ½ as k + 1. The shipped default pair (2 vs 2) gives Failure
0.74, no Overwhelming. Parameters are [OPEN — Jordan tuning]; the **form** (equal skill, higher capability, worse odds at every odd step) is a
structural finding — but a **latent** one: capability is empty on 429 of 430 corpus persons (`requirements.yaml`:1246-1250), so shipped play
is the 2-vs-2 row and the sawtooth describes no contest that runs today. It becomes live the day K-IN-1's per-person source lands.

### 9.2 N-line ledger (six directions; attack and result)

| object | N-line (narrowed where needed) | attack run | result | direction |
|---|---|---|---|---|
| frozen world in DELIBERATE | cut it and deliberation order becomes an outcome | looked for a write path during DELIBERATE: `deliberate.py`:72-74 raises `Forbidden` on an unfrozen world [CHECKED] | HOLDS | horizontal |
| scene budget | cut it and a king's scarcity equals a copyist's; nobody chooses what to leave undone | not attacked this pass; the audit walked it (no other object prices attention by office) [AUDIT, `03`:131-134] | HOLDS on the audit's walk only, **unscored here** | vertical |
| one `resolve` over one verb table, refusal as an Event | cut it and verbs need private resolvers (the second-resolver failure, T-IN-5) and scarcity stops being witnessable | re-ran: 40 of 45 rows carry a non-empty `emits_on_refusal`; the five with `[]` (`create_record`, `forge`, `speak`, `tie / knot`, `utter`) have eligibility `own` and no `requires:`, so no refusal path [CHECKED YAML load] | HOLDS, **narrowed** to "every refusable row emits" | lateral, bottom-up |
| `degree_from_net`, one ladder | cut it and each scale re-bands one quantity (the July census's 8 ladders) | combat routes through it under a guard (`core.py`:61-74 [CHECKED]); mass battle's own four labels and march's Won/Lost sit beside it | HOLDS for the margin; **narrowed**: three vocabularies remain beside it | lateral |
| ENCOUNTER barrier | cut it and the grid's suspension and deferred contests lose their barrier | the audit's fold-into-RESOLVE attack [AUDIT], not re-run | HOLDS on the audit's attack only, MEDIUM, **unscored here**; its first consumer (IN-46) is unbatched, so today it is held for a future reader | vertical |
| contest seam at RESOLVE/ENCOUNTER | cut it and no person's act can be resolved by a subsystem | **no attack run**: the row states a role (the only carried vertical seam, `seam/contest.py`), not a cut walked | **unscored** (a PASS needs a named failed attack) | vertical, diagonal |
| witness `_refract` (confidence only) | cut it and every witness holds an act at the actor's own confidence; R-07's imperfect knowledge loses its graded half | re-opened `witness.py`:231-239, :495 [CHECKED]: value, source and chain are never refracted; the actor is never refracted | HOLDS, **narrowed** to confidence; value-level fallibility is a limit | bottom-up |
| attention tiers (IN-57) | claimed: tractable choice at scale | its own measurement is a regression (21 → 17 executed, `requirements.yaml`:901-905) | **not an N-line as filed** ("makes X tractable" argues for a representation); unscored | — |
| σ-leverage at the season seam | claimed: circumstance shifts μ | the possibility survives the cut because nothing produces leverage (`sigma.py`:139-147; "this plan schedules none", `_part2`:418-421) | **FALSE N-LINE** (disqualifier 2, no producer) at the season seam only; combat and mass battle keep their σ terms | — |
| `urgency` | claimed: need reorders choice | constant across candidates, "INERT BY CONSTRUCTION" (`choose.py`:172-193) | **FALSE N-LINE** (disqualifier 5) — the audit's, confirmed | — |
| `benefits_me` (the function) | claimed: self-interest weights choice | no production caller (grep [CHECKED]); the ruled weighting (ED-IN-0261) is consumed at world generation, not here [AUDIT] | **FALSE N-LINE for the function**; the ruling it was written for is not cut | — |
| verb table `scale:` column | claimed: verbs are scoped by scale | H-89: read by nothing but the loader [CHECKED HR] | **FALSE N-LINE** (disqualifier 2) | — |
| `_drop_what_was_already_done` | cut it and one person spends every scene on their top three acts, and seven verbs leave the world (the monoculture measured before it existed, `deliberate.py`:314-318 [CHECKED]) | the cut was walked by its author, not by this pass: the measurement is in its docstring; §C.3 (`03`:138-140) forbids it, §C.2 (`03`:131-134) supplies its reason [CHECKED] | **contested inside Layer 1**: the N-line rests on §C.2 and a measurement, and is forbidden by §C.3; unscored until the cut is re-measured with a control | top-down |
| relaxed exit (plan instrument) | cut it and positions stall on realm counts the chooser's data, not wiring, decides (m:126-128) | an argument, not an attack: no cut walked | **unscored**; recorded as a finding instead — it leaves R-05's computed execution with no owner (H-IN-1), the EU4 detector moved up a level | bottom-up |

| the season force as one `Line` at power 4, command 4 | claimed by nobody as a design: the module labels it "minimum-viable defaults … no canonical spec" (`massbattle.py`:158-166 [CHECKED]) | Jordan 2026-10-16: "this 4/4 one line formation … as coded is a stub" | **not an N-line: a placeholder by ruling** (M-IN-12) | — |

**Tally (attacked this pass).** Of eight rows the first draft scored HOLDS, four survive an attack run in this pass (frozen world, one
`resolve`, `degree_from_net`, witness `_refract`; three narrowed); two hold only on the audit's attack and are unscored here (scene
budget, ENCOUNTER); two were never attacked and are unscored (contest seam, relaxed exit). The dedup filter is contested inside Layer 1.

**False N-lines, null check:** four found (σ-leverage at the season seam, `urgency`, `benefits_me`, `scale:`), each with a disqualifier;
mass battle's four-label degree is the MB lane's (audit G2b). Each was attacked for a hidden reader; none found.

### 9.3 The five cross-cutting checks

- **C1 claim → mechanism.** "Personal-scale resolution varies by person": no carrier in combat or mass battle; contest only where a vocation
  is named (M-IN-1, H-IN-2). "No state is hidden from the player" (`01`:301-302): no carrier — `explain` is unimplemented (M-IN-3). "R-05 is
  owned by the verb positions": no carrier (H-IN-1). "History improves a thread roll": no carrier (`operations.py`:246 [CHECKED]; WR).
  "A faction levies troops and fields an army" (Jordan, statements 1, 4): no carrier — `levy` moves stores, the seam passes weights, the
  force is one Line (M-IN-12). "A person may deceive": no carrier (H-198; M-IN-14).
- **C2 type signature.** `explain(p : PersonInterior, v : Value)` takes no `World` (`04`:860 [CHECKED]), but a contested act's odds depend on
  the subject's capability (`_obstacle_of` reads `w.persons[subject]`, `sigma.py`:125-128 [CHECKED]). **So if the player is ever shown odds,
  they cannot be the true odds: only the actor's estimate from claims they hold about the subject.** Whether §C.11 owes odds at all is a
  separate question: it owes "the derivation of a value the character already has" (`04`:855), and an act not yet taken has no held value.
  The signature constrains the shape of any band; it does not decide that a band is owed (M-IN-3; K-IN-9 is Jordan's).
- **C3 epistemic feasibility.** The resolver's read of the subject's capability is resolver-side and lawful. A shown band must be computed from
  held claims (C2). H-207's second cause, question priority, is evaluated from the person's own questions, so it is feasible; its first cause
  ("one actor, one season") is cast content, which R-05's rule forbids inventing.
- **C4 contradiction sweep.** Seven, in §7.2 items 1–8 (item 6 is drift): 03 §C.2 vs 03 §C.3 over the dedup filter; v9's stores `levy`
  vs Jordan's troop levy (item 7); IN-31's exit vs H-207 (A) (item 8); AX-7's gloss vs §C.11; the dead CANONICAL path; GD-2 vs AX-1/T-b; Jordan's "pool
  only" for the contest vs K-2's `Person.attributes` for combat. One introduced here and resolved: §8.4 lists σ-leverage as built-dark while
  §9.2 calls it a false N-line — both hold, because the kernel's σ term is live in combat and mass battle and dead only at the season seam.
- **C5 path construction.** Showcase *a seated person is killed and the seat passes* (IN-61's regicide probe [READER W2 §H]): `fight`
  executes (E) → Felled writes `Tenure.until` (VT `fight` writes, BASELINE B3) → the office is vacant → `succeed` has no predicate/effect →
  `confer` never attempted → **asserted** after the death. Under planned-built, IN-61 supplies `succeed` (B-R), blocked on ED-IN-0292 (2)
  (H-IN-5). Showcase *a faction levies troops from its settlements and fields them* (Jordan, statement 1): `levy` is refused today and
  moves grain when it executes (VT:629-652) → under planned-built, IN-49 makes the grain levy execute and IN-52 (OFF, then flipped) lets the
  treasury **bound** a headcount that is still the persons' weight sum, fielded as one Line (`_part4`:137; `massbattle.py`:226-230)
  → **not expressible even planned-built**: no step raises a troop, grades it by equipment, experience or commander, or lets the faction
  compose subunits (M-IN-12, H-IN-10). The first draft read this showcase as "expressible, not implementable, until the flip"; that
  reading assumed the levy produced troops.

### 9.4 R — both halves, and completeness

- **Seat question.** Answered by the design's laws: the player is an ordinary person, overridden per person id (`play_surface.py`:40-51
  [CHECKED]); every person seat is occupiable. R-CHOICE and R-VARIETY therefore bind at every person seat.
- **R-COMPLETE: FINDINGS.** Extremes: S27.4 refuses when Ob exceeds `obstacle_refusal_multiple × pool` (`sigma.py`:190 [CHECKED]);
  pool 2 at Ob 2 can never be Overwhelming (executed, 9.1); the σ-boost floors below one die (`orchestration.py`:1284-1289 [CHECKED]).
  Unwritten branches: `succeed`, `carry`, `forge` effects declined; H-207's unruled remainder (the motive; causes 5, 6); H-91's eligibility
  conflict; a deed claim that is never False (H-198). The odds sawtooth (9.1) is a completeness defect at every odd step **of a lattice no
  shipped contest reaches** (every contest is 2 vs 2 today): latent, live once capability varies.
- **R-VARIETY: FINDINGS.** One build fights and argues like every other (T-IN-1); every field is one Line at 4/4 whose sides differ by
  headcount only (T-IN-14); variety lives in pursuits, stance and seat only.
- **R-CUSTOMIZATION (factions): FINDINGS.** A faction cannot raise, equip or compose an army: no troop stock, no troop-raising verb, the
  `march` operand gives it nothing to choose, and `build_army`'s per-subunit composition is unreachable from the season (M-IN-12).
  Jordan's statement 4 names this exact customization.
- **R-WORLD: FINDINGS** [CONFIDENCE: medium]. Unwatched seats emit acts (R-01/R-02 met), but the act content is thin (T-IN-4), no field is
  fought in the realm (HR:3264-3265), hunger, age and illness ship at control (8.4), and `at_war` has no world-gen utterance [AUDIT]. Under
  planned-built, forcing (IN-35, IN-36), endings (IN-27) and the cast (IN-38) are scheduled; whether they emit hooks is unmeasured beyond four
  seasons (M-IN-10).
- **R-CHOICE: FINDINGS, upper bound.** One table added to the audit's `levy` table [AUDIT A5] (that table prices the stores `levy`, the
  misnamed act of M-IN-13):

  SEAT: any person · INTENT: remove a rival from an office

  | act | gain | cost |
  |---|---|---|
  | `fight` | executes today; Felled ends the rival's `Tenure` (VT `fight` writes) | body risk at identical pools (pool 9 vs Ob 1.5 for every season duel [AUDIT A1]); a grudge only if witnessed (**decaying cost**) |
  | `revoke` | ends the Tenure without a death | never chosen in computed play: no motive offers it and Jordan ruled none be special-cased (H-207 (A)); hand-forced it works; under IN-31 an appointed holder is permanently banned [READER C4_2]; eligibility now `rung_above_in_holdings` for the two duchy heads, and no duchy is a holding as built (H-207 (B)) [CHECKED HR] |
  | the charge (`petition` → `determine`) | a lawful disposal (`detain`/`ban`) | planned (IN-12 step 5a, SC-03b); multi-season through a docket |

  Shipped today the killing row is **strictly dominant** (the only one that executes). Planned-built it is a **decaying-cost** dominance: its
  price falls to the witnesses, and §6's "silence beats refusal" warning applies to an unwitnessed killing. Dependency: the act economy (IN-14,
  shape ruled, unbuilt — §8.4) and the witness set; no equilibrium run. The `fight` row's "pool 9 vs Ob 1.5" is the audit's [AUDIT A1], not
  re-derived here.

### 9.5 S — six directions, pause, methodology

| direction | carried by | verdict |
|---|---|---|
| S-UP (a demand filtered by a person at a rung) | petition: `to` == `subject` (`deliberate.py`:355 [CHECKED]) — FAIL; docket: a lapse emits `date.fired` [AUDIT] — PARTIAL, completed by SC-01 (B-N) | FAIL (petition), PASS planned-built (docket) |
| S-DOWN (published, distorting, picked up by the recipient's own perception) | telling through `refraction_gain` [CHECKED `fixtures.py`:800] | PASS in shape; the tree delivers thinly [AUDIT] |
| vertical | the contest seam; ENCOUNTER; settlement → army → field: the seam passes weights only (`seam/wrappers/mass_battle.py`:191-193 [CHECKED]), and no rung resource reaches a field as troops | PASS for the bout; FAIL above it (M-IN-6); FAIL settlement → field (M-IN-12) |
| diagonal (cross-scale and cross-family) | thread → mass: an empty hook (`orchestration.py`:333-335 [CHECKED]) | FAIL |
| lateral | one `resolve`, one verb table, one ladder | PASS, narrowed by three vocabularies |
| horizontal | the frozen world, the draw key per `(world_seed, tick, pid, purpose)` [AUDIT] | PASS |
| **pauses correctly** | a battle is one 18-tick call with no yield (`massbattle.py`:281-283 [CHECKED]); a human callback runs inside a per-person map marked parallel [AUDIT `deliberate.py`:116]; H-56 (nested DELIBERATE) HELD | **FINDINGS** |
| **calculations consistent in methodology** | T-IN-2: four owners of one per-die pair, a continuous and a discrete substrate, three result vocabularies, at least three pool formulas; the sawtooth (9.1) exists only on the discrete side | **FINDINGS** |

Shape and tree scored separately: the **shape** passes lateral and horizontal; the **tree** fails vertical above the bout because no
person's act reaches inside a battle.

### 9.6 The design's own falsifier (§8 of the skill)

Two disciplines, walked by reading (not executed; `test_ax7_refraction.py` exists and its tests assert the refraction rule, including
`test_in15_the_actor_is_never_refracted` [CHECKED test names], which pins the very exemption the falsifier's letter flags):

1. **AX-7's falsifier** — "any deposit … whose value is the engine's own resolution, unmediated" (`01`:314-317). Hits: five Claim
   constructions (`witness.py`:532, :648, :671, :700, :850 [CHECKED]); all pass through `_refract`, which mediates confidence only. Cluster:
   **one family — value unmediated, confidence mediated**; plus one exemption, the actor's own deposit (:495). Whether confidence-only
   mediation satisfies "mediated" is unruled: the design's exception list is missing this family. Not a free one-liner.
2. **"The person triages; the engine never truncates."** Hits: the dedup filter (a hit by §C.3's letter; §C.2 and its own measured
   monoculture argue it is the triage, not a truncation — it bars only what the person already realised; contested, not clean);
   packing by rank or subject, never by place
   (`choose.py`:613-621 [CHECKED]) against `03`:116 "one place" (clean); fixtures standing where an opener's declaration should be
   (`bench_quorum`, `oblige_term`, `record_stages_default`, `fixtures.py`:460, :818, :849 [CHECKED]) — one family; `budget_office_bonus`
   passes by tracing to S26.3 [AUDIT]. **HITS**, clustering as the audit found.

### 9.7 E — scored last, as a ratio against N and R

- **E-OVERHEAD: FINDINGS.** Counts: 45 verb rows now, 57 planned-built (45 + 12 IN-12, `repudiate` already cut); 66 fixture knobs, 18 shipped
  dark (BASELINE B5); 64 rosters + 7 tables; 198 hole-register rows read by no game code; 4 owners of the per-die pair; 3 result
  vocabularies + 1 unread. The plan's largest moves are **additions** (12 verbs, a goals carrier, two rosters, a successions registry); its
  deletions are `repudiate`, the TN 6/8 rows and `DECISIVE_OB`. The vocabulary grows. Four false N-lines (9.2) are free cuts not yet made.
- **E-LEGIBILITY: FINDINGS.** The player cannot predict an outcome's shape: odds are shown nowhere (M-IN-3), and would be a sawtooth in
  capability once capability varies (9.1, latent today); a pursuit reaches an act through 15 pursuits × 7 axes × 45 verbs (`choose.py`:402-406
  [CHECKED]); and a verb's name says the opposite of its act (`levy` moves grain, M-IN-13).
- **Ratio.** Against what N and R found — a resolver that varies by seed rather than by person, and a player surface that does not exist —
  the overhead is not buying robust choosing yet. E cannot improve by addition (meta-rule); its repairs are the four false-N cuts and one
  owner for the per-die pair.

**Over-distillation watchlist**

| watched | the N it protects | verdict |
|---|---|---|
| a cohort as one Person at weight | one code path for crowds | kept for crowds, MEDIUM (cannot dissent or die in part) [AUDIT]; **overruled as the source of troops** by Jordan's statement 1 — an army is a levied stock, and weight has no runtime writer (H-49) |
| one subunit per side at the season seam | one season-force construction | **overruled** by Jordan's statement 3 ("a stub") and the module's own "minimum-viable defaults" label; `build_army` already builds composite armies on the harness side (M-IN-12) |
| a faction as a view, never an actor | AX-1 | kept, MEDIUM; costs player readability (M-IN-3) |
| `scale:` retired in favour of `Act.via` scope | one carrier of scope | cut — nothing reads `scale:` (H-89); kept HELD by Jordan, so the cut waits |
| σ-leverage removed at the season seam only | circumstance as μ-shift | kept in the kernel, MEDIUM: combat and mass battle use it; the season's zero is Jordan's "pool only" as the plan reads it |
| the relaxed exit | plan velocity | kept, LOW: it buys velocity at the price of R-05's ownership (H-IN-1) |

### 9.8 Self-audit

- **9a backward propagation.** Two residues found and fixed in this pass: §8.1's first count line used an invented subtraction ("minus 19
  duplicates") and was rewritten to the counts the tables carry; §8.5's σ-leverage row was moved to 8.4 when §9.2 found the kernel term live in
  combat. One residue reported, not fixed: §0 item 3 still says leverage "contributes 0 in the game loop" without the season-seam qualifier;
  it is correct as written for the season loop.
- **9b §3 turned on this pass's additions.** M-IN-3 proposes one function the architecture already declares (`explain`, `04`:860) — not a new
  object (disqualifier 3 checked: it was never cut). M-IN-10 proposes an instrument: disqualifier 1 checked — `arms.py` exists but is
  season-loop-only and one-mechanic (CLAUDE.md §7), so it is not the carrier; the recommendation in §10 is written to extend `aperture`/`arms`
  rather than add a tool. M-IN-11 asks for a bound on loops: `forgive` is the existing carrier for the one loop that runs; the recommendation
  is narrowed to that.
- **9c the critic's pass (applied 2026-10-16).** An independent critic found the levy/troop demand missing, N-9/T-IN-13 resting on
  held-false deed claims that do not exist (H-198), M-IN-4/K-IN-4, K-IN-3, K-IN-9, G5 and H-IN-9 over-stated, §8.1's verb and audit counts
  wrong, four of six N "holds" unattacked in this pass, and four recommendations with no real cut. Each was re-opened at source; the
  corrections are in place and listed in §11. This pass found two more on its own: `confer` executes since IN-53 (M-IN-4 had it "never
  attempted"), and `arms --seasons` plus `soak.py` already run multiple seasons (M-IN-10 had "no instrument").
- **An independent reviewer would add:** a seeded run beyond four seasons; the act-economy equilibrium; whether IN-66's goals carrier makes
  H-185 moot; the IN-12 step 5a docket routing traced end to end.

### 9.9 Verdict

```
NERS PASS: IN — kernel, season loop, verb table, chooser, witness, seams, plan instruments (v9 assumed built)   INSTRUMENTS: A+B

MUST BE STATED AS A LIMIT
  - Personal-scale resolution varies by person — no carrier in combat or mass battle; contest by vocation only   [C1; M-IN-1]
  - The player can read why an outcome came out as it did — `explain` unbuilt, no odds anywhere   [C1, C2; M-IN-3]
  - R-05 is owned by the verb positions — exits are DONE-test; computed execution has no owner   [C1; H-IN-1]
  - Scales hand off and pause — above the bout they summarize, they do not pause   [S; M-IN-6]
  - A demand travels up a rung — the petition is addressed to its own subject   [S-UP]
  - Witnessing is mediated by channel, competence and prior belief — confidence only; competence has no carrier   [§8; M-IN-7]
  - A faction raises troops from its settlements and fields an army it composed — `levy` moves grain; one 4/4 Line per side   [C1, C5; M-IN-12]
  - A person can deceive — no teller lies; no deed claim is ever held False   [C1; M-IN-14]
  - Offices are made and emptied by persons — `confer` executes; `revoke` and `establish` have no motive (H-207 (A))   [M-IN-4]
MAY BE CLAIMED, HAVING SURVIVED
  - The world is frozen during deliberation — attacked for a write path; DELIBERATE raises on an unfrozen world
  - Every refusable act emits on refusal — 40/45 rows emit; the 5 that do not cannot be refused (eligibility `own`, no `requires:`)
  - One margin ladder — attacked for a second banding; combat routes through the owner under a guard
  - One resolver, several fidelities — attacked for a second resolver; `fight` routes to one engine

| axis / test | verdict | what would overturn it |
|---|---|---|
| N (six directions) | FINDINGS: 4 hold under an attack run this pass (3 narrowed); 2 hold on the audit's attack only and 2 were never attacked (all 4 unscored); 4 false N-lines; 1 contested inside Layer 1 (the dedup filter); 1 placeholder by ruling (the 4/4 Line) | a reader found for σ-leverage, `urgency`, `benefits_me` or `scale:`; an attack that removes the scene budget, ENCOUNTER or the contest seam without loss |
| E-OVERHEAD | FINDINGS | the 18 dark knobs each guarding a behaviour Jordan has ruled in |
| E-LEGIBILITY | FINDINGS | a shown estimate band and a monotone pool/Ob rule |
| R-COMPLETE | FINDINGS (the sawtooth latent) | a ruled per-odd-step Ob rule; written `succeed`/`carry` effects |
| R-VARIETY | FINDINGS | two persons with different authored capacities producing different Felled rates at fixed seeds |
| R-CUSTOMIZATION (factions) | FINDINGS | two factions fielding different composite armies from different levied stocks at fixed seeds |
| R-WORLD | FINDINGS [medium] | a seeded multi-season run in which an unwatched seat emits a war, succession or dearth that changes a later decision |
| R-CHOICE | FINDINGS, upper bound | an equilibrium run over `fight` vs `revoke` vs the charge at a seated rival |
| S-UP | FAIL (petition); PASS planned-built (docket) | a computed petition addressed to the holder of the rung above its subject |
| S-DOWN | PASS (shape) | a telling routed to a named recipient by the engine |
| S — coverage · pause · methodology | FINDINGS | a carrier for battle→duel and thread→mass; one substrate or a ruled reason for two |
| the design's own falsifier | HITS: value-unmediated family (AX-7); fixtures-for-declarations family (triage) | a ruling that confidence-only refraction is AX-7's mediation |
| self-audit | both sweeps run; 2 residues fixed, 1 reported; a critic's 12 findings applied (§9.8 9c) | a play-length run; the act-economy equilibrium |

REPAIRS (worst first; each a deletion or one object)
  per-person capacity has no source → Jordan rules one source (K-2 with its first reader, or "identical fighters are intended")
  troops are not a resource and `levy` moves grain → a troop stock raised by `levy`, a composite army on `build_army`; the stores act renamed (Jordan's name); cut the 4/4 stub and IN-52's stores bound
  the player is owed a derivation → Jordan rules AX-7's gloss against §C.11, then `explain` is built to the survivor
  `revoke`/`establish` have no motive → Jordan rules a general motive or a DONE-test reading of R-04 (1)/R-05 (H-207 (A) stands)
  four false N-lines → delete `urgency`, `benefits_me`, the season-seam leverage plumbing, `scale:` (the last when H-89's hold lifts)
  03 §C.2 vs §C.3 → Jordan amends one sentence; the filter stays or goes with a control on the measured monoculture (falsifier: R-03)

GRADE: paper for the planned-built object; one execution artifact for the shipped kernel (9.1, the band arithmetic) and one for the loop
(`python -m engine.season.harness.register --requirements`, run 2026-10-16 at `5445e34`: "met 3 · not_met 1 · partial 5", EXIT 0). Not run:
`corpus_run`, `aperture 4 0`, `arms`, `soak`, any test file, any multi-season run. The §9.6 disciplines were walked by reading, not executed.
```

## 10. KEY RECOMMENDATIONS

This is an audit-design pass over six months of repository work. Jordan, 2026-10-16: it "gets permission to be whatever it is". The
recommendations below are this pass's output; none is entered in the plan or a ledger until Jordan so rules.

### 10.0 Top five, worst problem first

1. **K-IN-1** — rule one source for per-person capacities that every resolver reads (T-IN-1; M-IN-1).
2. **K-IN-13** — make `levy` raise troops into a settlement's own stock and build the season's army from those stocks as composite
   subunits; rename the stores act (M-IN-12, M-IN-13; T-IN-14; Jordan's statements 1, 3, 4, 5).
3. **K-IN-10** — put IN-46 and IN-47's builds in a batch (M-IN-2; without it M1 cannot be met under v9).
4. **K-IN-6** — let a battle pause for a person's act inside it (M-IN-6; T-IN-7).
5. **K-IN-9** — rule what the player is shown (AX-7's gloss against §C.11), then build `explain` to the ruling (M-IN-3; T-IN-10).

K-IN-4 left the five: `confer` already executes (IN-53), and what remains — a motive for `revoke` — sits under Jordan's own H-207 ruling.

### 10.1 PRIMITIVES

| ID | recommendation | grounded in | §0 ladder | adds / cuts | falsifier |
|---|---|---|---|---|---|
| K-IN-1 | Rule one source for per-person capacities that the contest pool, the `Combatant`, a commander's command and a witness's competence all read, or rule that identical capacities are intended and withdraw the claim that personal-scale resolution varies by person. | M-IN-1, M-IN-7 (competence, H-200), H-IN-2, H-IN-4, T-IN-1 (code [CHECKED], 3 subsystems); NERS R-VARIETY. (The force's size and quality are K-IN-13's: Jordan's statement 1 grades troops by equipment, experience and commander, not by the persons' own capacities) | **Jordan**: survives all five — (1) nothing supersedes it; (2) combat and mass battle are retained scales (`requirements.yaml` `scales:`); (3) K-2 "not ratified", J-13's remainder is J.2 rank 1; (4) precedent conflicts — Jordan's "pool only … a derived score … not a character attribute" for the contest (`_part2`:416) against K-2's `Person.attributes` for combat; (5) both options are lawful and give materially different games | adds one per-person source (one field or one derivation from authored data); cuts `pool_default`/`obstacle_default` as person stand-ins, `party_end`'s single-field mapping, the season's constant `command=4` (`massbattle.py`:183), refraction's constant `competence = 1` (`options.py`:1198-1210), and the K-1/K-5/M-2…M-6 LEAVE rows it answers | two persons with different authored capacities give different `tell` degrees and Felled rates over the same seeds; identical capacities reproduce today's `content_hash` |
| K-IN-2 | Delete what the season carries and nothing reads — the chooser's `urgency` and `benefits_me`, and an authored OUGHT's `predicate` — unless a reader is ruled for it. (Absorbs the first draft's K-IN-8.) | §9.2 false N-lines (disqualifiers 5 and 2) [CHECKED `choose.py`:150-193]; M-IN-9, T-IN-4 [CHECKED HR H-185; `narration-mechanisms.md`:38-53]; audit G5, T5 | `urgency`, `benefits_me`: takeable, step 3 (`urgency`'s own docstring calls it a §F2 defect; `benefits_me` has no caller); IN-62's `score_terms` keeps `urgency` only as a hash-EQUAL refactor (`_part5`:255), so dropping the slot costs it nothing. The OUGHT `predicate`: takeable, step 5, if IN-66's `goals.yaml` supersedes the `ought:` cast field [CONFIDENCE: medium — IN-66 not read in full]; a reader for it is Jordan's (H-185 `unblocks:`). **Whether ED-IN-0261's self/other weighting is ever built stays Jordan's** | adds nothing; cuts ~50 lines, one test (`test_w5_…`), one slot in IN-62's triple, and H-185's dead field | `World.content_hash()` equal at seed 0 before and after the two chooser deletions (inert by construction); the predicate deletion moves the hash by schema alone (`content_hash` folds every dataclass's `repr`, `_part3`:33), so its falsifier is an unchanged sequence of chosen acts over the same seeds |

### 10.2 VERBS

| ID | recommendation | grounded in | §0 ladder | adds / cuts | falsifier |
|---|---|---|---|---|---|
| K-IN-3 | Delete `_drop_what_was_already_done`, so a person may spend a season repeating an act as Layer 1 says they may. | §7.2 item 1; §9.6 clean hit [CHECKED `deliberate.py`:225, :305; `03`:138-140]; audit A5a/G4 | takeable, step 3 (Layer 1 forbids it verbatim; its basis is a reference document). If R-03 goes red, the filter is load-bearing on a Jordan requirement and amending 03 §C.3 becomes his | adds nothing; cuts one function and its call | `pytest engine/season/tests -k test_u2_` (R-03's `measure:`) stays green |
| K-IN-4 | Give one position the job of making `confer`, `establish` and `revoke` execute in computed play with `Act.via` set, owning H-207's four causes, instead of leaving R-04 (1) and R-05 to "no position is invented to fix it". | M-IN-4, H-IN-1, T-IN-9 [CHECKED `_part5`:65; `_part2`:211-213, :270-276; HR H-207] | takeable, step 4: the plan itself answered "built out" as computed play on U7's precedent (`_part2`:270-273 [CHECKED]); a requirement read in computed play needs an owner in computed play. The named revert (m:134, `met` read DONE-test) is the other option and is Jordan's | adds one position (no code object); cuts the "named residue" path for these three verbs and B-JR's orphaning of `establish` | `aperture 4 0` shows each of the three executing ≥ 1 with `Act.via`; R-04's `measure:` reads it |

### 10.3 MECHANICS

| ID | recommendation | grounded in | §0 ladder | adds / cuts | falsifier |
|---|---|---|---|---|---|
| K-IN-5 | Grade every scale's roll on one die substrate whose per-die figures live in one place, with an obstacle rule under which a more capable equal pair never has worse odds. | T-IN-2 [CHECKED 4 owners; `core.py`:60 vs `roll.py`:35]; §9.1 sawtooth (executed); audit G2a, G2d | split: **one owner of the per-die pair is takeable, step 4** (CLAUDE.md §8; `degree_from_net`'s guarded single owner). **The substrate and the half-integer rule are Jordan's**: they re-read his score/2 ruling and move combat balance (two lawful readings, different odds shapes) | adds nothing; cuts three literal owners and either the continuous main roll or the season's ceiling lattice | a grep finds 0.40/0.80 defined once; the export `--check` round-trips stay green; the 9.1 table is monotone in c |
| K-IN-6 | Let a battle stop at its phase boundaries for a present person's act — a general's duel, a thread act — and resume with the result, using ENCOUNTER's barrier as the grid design already does. | M-IN-6, T-IN-7 [CHECKED `massbattle.py`:281-283; `orchestration.py`:333-335]; §9.5 pause FINDINGS; audit A2 | takeable, step 4 for the form: IN-46's suspension at ENCOUNTER (`proposals/2026-10-07-grid-mode-suspension.md`, re-read at B-L) is the tree's precedent for pausing inside ENCOUNTER; which acts may interrupt is MB/WR lane design | adds one yield point in the 18-tick call (3 phases × 6); cuts the empty `threadwork_check` hook and M-6's LEAVE row | a seeded field in which a duel between the two commanders, resolved through `fight`, changes the field's result against a control where it is forbidden |

### 10.4 TEXTURE

| ID | recommendation | grounded in | §0 ladder | adds / cuts | falsifier |
|---|---|---|---|---|---|
| K-IN-7 | Let what a person is believed to have done depend on who saw it and whether their word has held: give refraction its competence input from K-IN-1's source, and reconcile declared intents against later deeds. | M-IN-7, M-IN-8, T-IN-13 [CHECKED HR H-200, H-191; `witness.py`:495]; audit A9 | competence: takeable, step 3 (AX-7 names it as an input, `01`:278-281) once K-IN-1 is ruled; intent reconciliation: takeable, step 5 (the pairing step and its `ABSENT: H-191` marker exist in `options.py::record`); **the performer's own fallible reading (AX-7 layer 2) is Jordan's**: "may be wrong" read as permitted or owed gives different games | adds no store (competence reads K-IN-1's source; reconciliation reads intent claims and deed claims the ledger already holds); cuts H-200's constant 1 and two absent rows | two observers of one act with different competence hold it at different confidence; a teller whose declared intent went unkept is credited less than one who kept it |
| K-IN-8 | Make every act-minted Proposition and Record say what it is about, or delete the fields that are always empty. | M-IN-9, T-IN-4 [CHECKED `narration-mechanisms.md`:38-53; HR H-185] | takeable, step 5 for deletion of the OUGHT `predicate` read by nothing if IN-66's goals carrier supersedes the `ought:` cast field; a reader for it is Jordan's (a verb × predicate magnitude nobody has ruled, H-185 `unblocks:`) | adds nothing, or one reader; cuts H-185's dead field | the narration measure, re-run on its committed form: act-minted Propositions with an empty predicate fall to 0, or the field no longer exists |

### 10.5 SURFACE

| ID | recommendation | grounded in | §0 ladder | adds / cuts | falsifier |
|---|---|---|---|---|---|
| K-IN-9 | Build `explain(p, v)` as Layer 1 declares it and use it to show the player an estimated band of odds computed from the claims the actor holds about the subject, never from the subject's true capability. | M-IN-3, T-IN-10, §9.3 C2 [CHECKED `04_CODE_ARCHITECTURE.md`:847-863; `grep "def explain"` → 0]; audit A3 legibility | takeable, step 3: Layer 1 §C.11 declares the signature and its no-`World` rule; the band-not-trigger shape is COMP S6 (research, tier 3, vocabulary only) | adds one declared function (no new store: it reads `PersonInterior`); cuts the need for any separate odds display state | `explain`'s signature has no `World` parameter (a type test); two actors holding different claims about one subject are shown different bands for the same act |
| K-IN-10 | Put IN-46's grid suspension and IN-47's character spaces into a build batch. | M-IN-2 [CHECKED `_part2`:209; `_part4`:32-41]; audit A2a | takeable, step 3: the plan states M1 cannot be met without it, both designs landed and were re-read. **Whether creation is an act (a person shaped by the player) or a selection ("no act; a cast entry", `_part4`:41) is Jordan's**: pick-a-person and make-a-person are different games (H-IN-3) | adds one batch; cuts two "named residue" rows in the R-04 scale table | R-04's two `scales:` rows read `in_loop` with an execution artifact named; `register --requirements` reports it |

### 10.6 APPARATUS AND PROCESS (IN only)

| ID | recommendation | grounded in | §0 ladder | adds / cuts | falsifier |
|---|---|---|---|---|---|
| K-IN-11 | Extend the existing `arms`/`aperture` harness to a seeded multi-season two-arm run of the shipped loop, rather than add a tool, so R-WORLD and R-CHOICE verdicts stop being four-season upper bounds. | M-IN-10 [CHECKED `_part8`:420 "keep the gap statement"]; CLAUDE.md §7 "no live successor — an open gap"; audit §10 GAP | takeable, step 5 (the gap is stated in Layer 0; extending an existing instrument adds no tool); loads on the game because every R verdict's denominator is it (§0.1 pt 5) | adds arguments to an existing harness; cuts nothing | a planted mechanic difference is detected over N seasons against a control arm that is identical by construction |
| K-IN-12 | Delete what the game cannot read and re-point what lies: untrack `engine/season/runs/` output except `results.json`, fork-delete `params_tables.yaml`, re-point `requirements.yaml`:34-35's dead CANONICAL path, AX-7's stale falsifier sites, and mark GD-2's faction mandatory pass as superseded. | T-IN-11 [CHECKED 88,377 tracked lines; `ls` of `params_tables.yaml`; `requirements.yaml`:34-35; `01`:314-317 vs `witness.py`:532-850]; §7.2 items 2–4; audit X1, X3, G6(i), G8 | `runs/` and `params_tables.yaml`: takeable, steps 4 and 2 (ED-IN-0125 "generated artifacts evacuate"; no game reader). The two path fixes: takeable, step 1 (the files moved). AX-7's text lands by PR review (Layer 1). **GD-2: Jordan** — GD is mutable canon whose updates "require explicit Jordan ratification" (`canon/04`:23) | adds nothing; cuts ~87,000 tracked lines of output and 10,821 lines of a frozen capture | `report && delta` on a clean checkout gives the same deltas; `freshness_gate.py` and `currency_consistency_check.py` pass; a grep finds no runtime load of `params_tables.yaml` |

### 10.7 The uploaded audit at `5445e34`: which findings and recommendations survive

| item | at `5445e34` | how tested |
|---|---|---|
| A2 (a) callback player; (b) §C.11 vs AX-7 gloss; (c) dead CANONICAL path | survive | (a) `play_surface.py`:40-51, `_part4`:41; (b) `04`:845-863, `grep -c AX-7 04` → 0; (c) `ls`, `requirements.yaml`:34-35 [all CHECKED] |
| A3 one ladder, several roads; non-monotone odds | survives, extended to c = 6 (sawtooth) | literals, substrates, vocabularies re-opened; §9.1 executed |
| A4 (i) `urgency` inert; (ii) `benefits_me` no caller; (iii) OUGHT predicate; (iv) dark knobs; (v) no outcome term | (i)–(iv) survive; (v) not a missing area (§8.5) | `choose.py`:150-193; HR H-185; BASELINE B5 |
| A5 (a) dedup contradicts 03 §C.3; S-UP petition; R-CHOICE `levy` | (a) and S-UP survive; `levy` table relied on | `deliberate.py`:225, :305, :355; `03`:136-140 |
| A9 AX-7 falsifier fires by its letter | survives; sites moved again: :532, :648, :671, :700, :850; actor skip :495 | `witness.py` grep, `_refract` :231-239 |
| T3, T4, T5, T6 | SOUND (T-IN-2, T-IN-3, T-IN-4, T-IN-11); T6's run-output count is now 88,377 (was 87,678) | §7.1 |
| G1 per-person source | survives (K-IN-1) | `_part7`:44; `_part5`:514 |
| G2a one owner of literals | survives (K-IN-5) | 4 owners re-opened |
| G2b delete mass battle's four-label degree | survives (MB lane) | `ladder.py`:195-203 "stays there for introspection" |
| G2c mass battle returns a margin | survives, Jordan's (MB) | as audit |
| G2d one substrate | survives (PC; K-IN-5) | `core.py`:60 |
| G3 weight→troop conversion | survives (MB) | `massbattle.py`:198-207 |
| G4 delete the dedup filter | survives (K-IN-3) | as above |
| G5 delete `urgency`, `benefits_me` | survives, **and v9 now plans the opposite for `urgency`**: IN-62's `score_terms -> (pursuit, stance, urgency)` (`_part5`:255 [CHECKED]) — K-IN-2 | |
| G6 AX-7 falsifier re-point; narrow the gloss | survives; its line targets have moved since `092fc45` | K-IN-12 |
| G7 `operations.py`:246 `min(3, history+3)` | survives (WR lane) | `operations.py`:244-247 [CHECKED] |
| G8 re-point quarantined head rows; dead path | survives | BASELINE B6 (15 of 24 head rows name quarantined documents); `requirements.yaml`:34-35 |
| G9 re-read candidate formation over several seeds | survives; not run here | — |
| X1 untrack `runs/` | survives (K-IN-12) | 10 tracked files, 88,377 lines |
| X2 move R-01/R-02 narrative out of `requirements.yaml` | survives [AUDIT]; the file grew 17 lines since `092fc45` | `git diff --stat` |
| X3 delete `params_tables.yaml` | survives (K-IN-12) | `ls` |
| X4 park module depth | survives | — |
| X5 move `build_realm` into game code | survives | `harness/populated.py` still under `harness/` [CHECKED `git ls-files`] |
| X6 archive resolved ED rows | survives [AUDIT] | not re-counted |
| X7 apply §0.1 pt 5 to the process checks | survives | `ci_checks_registry.yaml`: `subject: compliance` on 32 rows [CHECKED] |
| X8 delete `tools/evacuation_plan.py` | precondition still [UNVERIFIED] | file exists [CHECKED `ls`] |

## 11. METHOD NOTE (sections 7–10)

**Opened myself at `5445e34`.** The dice engine, `sigma_leverage.py`, the season σ wrapper, the contest roll, the combat core and wrapper and
config, the combat seam, `combatant.py`, `massbattle.py` and `orchestration.py` at the cited lines, `seam/ladder.py`, `play_surface.py`,
`choose.py` (inert terms, score, packing), `deliberate.py` (frozen world, dedup filter, petition note), `witness.py` (refraction, Claim
sites), `effects_combat.py` (grudge rows), `fixtures.py` lines, `faction_q.at_war`'s docstring, `operations.py`:244-247, H-rows by YAML load,
`verb_table.yaml` by YAML load (refusal emission), `01_AXIOMS.md`, `03_VERBS_AND_LOOPS.md` and `04_CODE_ARCHITECTURE.md` at the cited lines,
`canon/04_game_design_constraints.md`, plan lines in v9 main, `_part2`, `_part4`, `_part5`, `_part7`, the narration-mechanisms table, the
uploads at TD:19, :33, :49, :148, :191, :195, :231; 20G:221-245; N2:199, :245, :273, :369; 3S:1-8; and `git diff --stat 092fc45 HEAD`. Ran
`python -m engine.season.harness.register --requirements` (EXIT 0) and the band-arithmetic script `scratchpad/in_lane/odds.py` (python -I,
importing the repo's own die rule and ladder).

**Taken from elsewhere.** Sections 0–6 of this file; BASELINE B1–B7 (plan index, verb classes, hole-register selection, dark knobs, heads);
the uploaded audit (marked [AUDIT] where not re-opened: the `levy` R-CHOICE table, S-DOWN 4/1,270, the pause at `deliberate.py`:116, the draw
key, cohort costs, `cast.py` loyalty, X2/X6 counts); reader extractions R4, R5, R8, W1–W3, C4_2, C8_2, E4_5, UP01–UP05 (T, K, G sections),
marked [READER]; UPLOAD_CHECKS for the SFP and VCD attribution verdicts I did not re-open myself.

**Upload corrections applied to sections 0–6 (Step 0).**
1. §2.1 `VCD` App. B row: the [SESSION] rows tested against the uploads — Guild 2, DF/RimWorld/Sims, Manor Lords/Tropico CONFIRMED; Prom
   Week/Versu PARTLY; Shadows of Doubt in no upload; Guild 3 F77 NOT IN THE SOURCE.
2. §2.1 same row: `VCD`:125-127's [ASSUMPTION] that the labels are never expanded is superseded by 3S:5; N2 is the mechanical
   specifications, not a compendium.
3. §2.2 Guild 3 row: the case is the publisher's T1 account — townsfolk burned the **player's** residence at roughly every second launch, the
   AI was switched off (TD:195; 20G:241); `VCD`:985's "producer's residence", `VCD`:183-184's "forum post that predates Early Access" and
   F77's "popularity threshold" are not in either upload.
4. §2.2 / §4.1 / §4.2 Pax Pamir pricing: content CONFIRMED against the teardown's T0 rulebook reading (TD:33, :49).
5. §3.2 ENP v2 row and §5 GAP line: five of the seven pinned documents are now in hand (uploads, not tracked files) and hash-match; the two
   earlier drafts are not; the surveys behind P1–P58/F01–F84 and *A Tells B About C* remain absent.
6. §3.2 RULINGS row: the "nine-game teardown" ED-SE-0051 cites is in hand in its audited revision and supports capacity-as-gate only partly.
No correction changed a §0 ranking.

**Could not check.** IN-66's full entry (whether `goals.yaml` supersedes the `ought:` predicate, M-IN-9); the IN-12 step 5a docket routing end to
end (petition addressee, 8.4); `results.json`'s two test readers (X1); the act-economy equilibrium; anything beyond four seasons; the
committed audit's own claims about squad-engagement Parts A–D and UI Parts 4–10, which it did not read either.

**Confidence.** [CONFIDENCE: medium] on T-IN-4's magnitude and R-WORLD (one uncommitted seed); on M-IN-7's layer-2 half (permitted vs owed is
unruled); on M-IN-9 (IN-66 unread). [CONFIDENCE: low] on H-206's remainder. Counts in 8.1 are the tables' own; the five walks' raw count (82)
is reported, not a de-duplicated derivation. Spawned no sub-agents: the reading was one lane and the critic stage is the orchestrator's.
