# NPC — people and cast: historical research, game precedent and repository work, critically evaluated

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · a critical evaluation; resolves nothing at runtime
## Date: 2026-10-16 · HEAD as stated in the opening note · Lane: NPC

Bin: people and cast (roster, behaviour and priority trees, relational graph, convictions and the decision layer,
succession, roster and advancement, loyalty and defection, `engine/season/npcs.yaml`, `references/npc_registry.yaml`,
character progression). No ED lane of its own; each finding below names the lane it belongs to (FA, WR, IN, SE, PC).
Marks: **[CHECKED]** = opened in the repository by this lane at HEAD `021fd96` (shallow clone); **[READER]** = taken
from an extraction in `scratchpad/out/`. Extraction short names: A5a/A5b = `A5_npcs_1/2`, D1 = `D1_pc_combat_characters`,
A4a/A4b = `A4_canon_1/2`, B1a/B1b = `B1_engine_data_1/2`, C7a/C7b = `C7_architecture_decision_play_1/2`, C4a/C4b =
`C4_behaviour_sfp_gather_1/2`, R7 = `R7_rtp_rhet`, R4 = `R4_companion_pmm`, R8 = `R8_precedent_in_proposals`,
U1/U2/U3, A7a/A7b/A7c, A8a, B2a/B2b, C8a/C8b. Research short names follow `research/00_INDEX.md` §1 (RTP, GOV, PMM,
COMP-n, PRE = `PREC-NULLS`).

## 0. VERDICT

The person that runs in the season loop is grounded in Jordan's rulings and its own measurements, not in the bin's
research or precedent: no code reads that research and no plan entry for this bin cites it; one GOV sentence survives
as a hole row (H-100), and one game precedent reaches the plan through VCD (`forgive`); the quarantined NPC design
corpus shares the cast's names and none of its mechanisms.

Problems, worst first (lane in brackets):

1. **Succession, defection, standing, recruitment and bonds have no carrier**; `succeed` and `tie/knot` are declined effects, revoke executes 0, heredity is `null` — B1b F, H; B2b H (H-182, H-207); [CHECKED grep]. IN-61 cites none of RTP's succession cases. [IN/FA]
2. **A person's loyalty value is static**: a cosine of authored values against a role template, ruled "can be invented", computed once at build and written as a stance row toward the faction's leader; nothing writes that row's referent over a season — `engine/season/data/cast.py:256-332`, `harness/populated.py:787, 854-856` [CHECKED]. The stance channel does carry one in-season, Imperator-bleed-shaped term — a lost field battle appends −1.0 rows toward the loser's own faction and the winner, shipped on at weight 1 — but toward the faction proposition, not the leader, so it does not sum into the loyalty row — `loop/effects_combat.py:203-205, 256-261`, `data/fixtures.py:589-590` [CHECKED]; that writer is also unreached, since every `march` is refused at ENCOUNTER (`requirements.yaml:1124-1125`). What does move live is **regard, computed at read**: `judged_gain` and `told_valence_gain` ship at 0.5 (`data/fixtures.py:741-750`) and 3,270 of 11,449 realm pairs differ beyond stored stance against 0 at control (`requirements.yaml:1132-1139`) [CHECKED]; it reaches the head only through deeds of his that the reader judges. Every loyalty precedent the corpus collected (Imperator, JA2, EU4, X3) is a moving quantity (R4 C, T). [IN/FA]
3. **The only historical finding about persons that reached the season register (H-100, seat provenance sets revocation cost) is answered by a proposal keyed on a different variable** (the seat's `conferral` basis, not how the seat was won; the proposal's own R3 says so) — [CHECKED H-100; IN-31 proposal :25, :146, :606]; C4b F, H. [FA/IN]
4. **RTP, the bin's one research file, is weakly delivered**: pasted agent chatter (l.11), two statuses (FILED and PROPOSAL), fact-check outcomes shown for six entries, a §3 design built on the retired Key substrate, and a minor count slip ("~96" cases against 94 entries) — [CHECKED RTP l.3, l.11, l.25, l.312, l.761]; R7 K8, K12-K14. [IN]
5. **The authored cast is thinner than its loader claims**: `cast.py` says 29 rows carry `stats`, 32 `ts`, 30 `goals`; non-null counts are 1, 10 and 17; of the 10 `ts` values two are strings ("75–80", "~50") and no code reads `ts` at all [CHECKED]. [IN/WR]
6. **The leaders are mis-housed, not mis-seated**: five of six faction leaders in `npcs.yaml` have `institution: null` and homes in cottages, markets or an inn (the King at `b_s_002_cottage`, in S-002 Auerheim, not the Seat S-001); Hafenmark's leader is tagged `institution: Crown` at `b_s_001_court` — `npcs.yaml:183-237`, `cohorts.yaml:65-67` [CHECKED]. Office tenure is correct: a seat's faction comes from the cast, and `test_fa01_head_seats.py` asserts all six heads hold an own-faction seat and five of six act through it at the first fold — `engine/season/tests/test_fa01_head_seats.py:18-24, 114-123` [CHECKED]. What is wrong is residence and the `institution` tag, which the plan's regicide reading (IN-59) inherits — `_part5` IN-59 [CHECKED]. [IN/FA]
7. **The design corpus contradicts itself on every person-level fact**: TS values, names (Haelgrund Sæmund/Lennart; registry TS 15 vs 12), Standing 0-5/0-7/0-10, defection roll or no roll, relational graph BUILT and deferred, five succession designs — A5a H; A5b H; A7b H; U3 H; [CHECKED registry]. [WR/FA]
8. **Game-precedent sourcing degrades downstream**: dropped `[UNVERIFIED]` marks, a self-contradicting desertion null in PMM, inflated convergence counts (X1), a contradicted null (N-9), one suite that anonymizes all its precedent, and VCD's Guild 3 grudge rows, which misstate the now-uploaded teardown (§2.1 VCD row) — R4 K1, K6-K11; R8 K12; C5 G; [CHECKED `3cb2a6c8` L195]. [IN]
9. **The conviction half of the decision layer is inert on `main`, a known and scheduled gap**: 0 of 46 registry rows carry `affiliations:`, so confliction and H-188 read nothing; this is stated at `cast.py:222-225`, H-188's default ("INERT IN THE SHIPPED REALM BY CONSTRUCTION", `hole_register.yaml:4207`) and IN-64 (state B, batch B-X, data at worktree checkpoint `4e942bac`) — [CHECKED registry parse; `_part5` IN-64]. [IN]
10. **"Conviction" means pursuits in one field and religious affiliation in the next** inside `npc_registry.yaml`, against four older rosters of 7, 8, 9 and 13 — [CHECKED header]; D1 H; G1 ML §8. [IN]
11. **Grievance (IN-58) carries a disclosed residue**: the stance-only half landed (`3bf936ee`) at hash EQUAL under the shipped polarity, the sworn-to half is BLK, and the plan says outright that the EXIT "hash MOVED" is NOT MET and names the residue (IN-70, IN-12 step 5) — `workplans/valoria_master_workplan_v9.md:277`, `_part5:225`, `_part2:343` [CHECKED]. [IN/FA]

What is solid: the claim ledger with source, chain and `seen.who`, the 15×7 pursuit cells that code reads, the refusal
to spawn people on a clock, the FA-01 test that each authored head holds and acts through an own-faction seat, and the
plan's B-X batch, which states falsifiers and controls for every position. THR
(the throughlines and precedent chapters) is the best-method precedent work in the bin and names the missing object
precisely: a persistent named person.

## 1. HISTORICAL RESEARCH

### 1.1 Sources

| path | what it is | status and method as stated | reliability finding |
|---|---|---|---|
| `research/rise_to_power_roster_system_research_v1.md` (RTP) | The only research document written *for* this bin: how people rose to influence, ten categories A–J, and §3 a roster/advancement proposal | Two statuses: "FILED — 2026-07-11 · Lane: IN (cross-cutting; touches FA, SE, NPC)" (l.3) and "This deliverable is PROPOSAL-status" (l.761) [CHECKED]. 31-agent workflow, Sonnet find → "independent adversarial fact-check" → distillation, one Opus synthesis [CHECKED l.3-7] | **Weak as delivered.** (a) Line 11 is pasted agent chatter: "I have everything I need in the brief … I'll return the polished deliverable directly as my response rather than writing a report file" [CHECKED]. (b) It claims "~96 historical cases" (l.25, l.50); the catalogue holds 94 entries plus a stub "E9" whose text says category E has 8 [CHECKED: 95 bold entry markers at line start, l.312] — a difference of 2 against a stated approximation, minor beside (a). (c) Fact-check outcomes are shown for only six entries (R7 K12); many entries cite encyclopedia or Wikipedia level sources while §5 says "every surviving entry carries a real citation" (R7 K13) [READER]. (d) §3.4 routes everything through the Key substrate and proposes ~60 new Key types (R7 K14) [READER]; the Key substrate is retired (CLAUDE.md §0, ED-IN-0232) |
| `research/governance/political_hierarchy_standing.md` (GOV, hierarchy theme) | Governance history, Sonnet researcher → Opus verifier per civilization (`00_INDEX.md` §2.B) | RESEARCH, ED-IN-0064 | Not read by this lane (its extraction, A9, is outside this bin). Its one finding that bears on people — demotion severity keyed to how a seat was won, "favor-derived seats … face total ruin, while kinship-derived seats get containment" — is quoted verbatim at `engine/season/hole_register.yaml` H-100 [CHECKED l.1941-1947]. This is the only historical finding about persons that the season loop's own register carries |
| `.designs/systems/npcs/reference/npc_roster_v30_infill.md` | Per-NPC "Historical echo" lines (Edeyja–Hypatia, Maret–Sorge, Vossen–Luxemburg, Haelgrund–Bellarmine, Torsvald–Granville, Brandt–Aetius, Feldhaus–Cœur, Almstedt–logothetes, Strand–William Marshal, Virke–Medici branch managers, Laskaris–Demetrios Palaiologos, Solberg–Xenophon, Tormann–Suger) | ARCHIVED-NOT-CANON; header "CANONICAL" with "[EDITORIAL: Full roster flagged for user review … provisional]" (A5b FILES, H) | Character inspiration, not research: one analogue per person, no citation, no method (A5b G) [READER]. Nothing in it is falsifiable and nothing reads it |
| `.designs/systems/npcs/reference/npc_relational_graph_v30.md` §0, §2 | Edge types grounded in *fede giurata*, *fidelitas/commendatio*, Medici *clientela*, Medici–Pazzi, Capulet/Montague, vendetta | PROVISIONAL, Class A canonical (PP-724) (A5a FILES) | Named analogues with no citation (A5a G); one is literary (Capulet/Montague). Shape-level only |
| `.designs/systems/npcs/reference/npc_behavior_v30.md` §3.5 | Advisor confidentiality grounded in the Privy Counsellor's oath, *curia regis*, Hoccleve, Joel Rosenthal | CANONICAL 2026-04-17 (editorial batch acceptance) (A5a FILES) | The only NPC-design passage that names a scholar (Rosenthal); no page or work given (A5a G) [READER] |
| `.designs/systems/characters/reference/conviction_taxonomy_v30.md` §2.1; `conviction_axis_matrix_v30.md` §3 | Thirteen Convictions mapped one-to-one to Renaissance values (*fides, auctoritas, ordo, studium, utilitas, aequitas, libertas, consuetudo, communitas, gens, cura, virtù, honor*); Aquinas, Bracton, Machiavelli, Florentine and Venetian republicanism | heading CANONICAL, body PROVISIONAL, footer "PROVISIONAL pending ratification" (D1 H) | A vocabulary-mapping exercise, not historical research; the roster it grounds has since been replaced (§3.3) |
| `.designs/systems/characters/reference/conviction_track_v1_pp718_vetting.md` | Per-Conviction Scar grounded in Catherine de' Medici, Charles V, and Litz/Shay moral injury | no Status line; "Class B vetting passes" (D1 FILES) | Self-vetting of a proposal by its own program; the clinical literature is cited as an inversion of the design's intent (D1 G, "clinical inversion") [READER] |
| `proposals/2026-09-26-decision-layer-execution-plan/candidate_pursuit_cells.md` §1a | Pursuit and axis definitions grounded in named philosophy and social science (Aristotle/MacIntyre, Pitt-Rivers/Bourdieu, Berlin/Pettit, Rawls/Sen, Weber/Veblen, Sidanius SDO, Schwartz circumplex, Weber *Gesinnungs-/Verantwortungsethik*) | FOLDED INTO THE BUILD (Jordan 2026-10-06, RS-1, ED-IN-0291) (C7b FILES) | Traditions named, no page-level citation; of 105 pursuit×axis cells 28 cited, 22 derived/analogy, **55 "reasoned" with no corpus citation** (C7b F CPC) [READER]. The only grounding in this bin that reached a table code reads (§2.D) |
| `proposals/_session_provenance/2026-08-29-to-31/PRECEDENT.md` (PRE), "Steals" | Historical steals on persons: Claudius's freedmen ("influence is measured in volume of things filtered, not rank"), Zhao Gao's forged edict, Day of the Dupes, Woodville, Yoritomo, Yuan Shikai, Wang Mang, malikane, Fujiwara | no header, status, author, date or method (R8 FILES) | **Unsourced.** Restates RTP cases as slogans; "survived the survey's own adversarial pass" with no pass cited (R8 K18) [READER] |
| `proposals/2026-08-25-throughlines-and-precedent/05_ch2_the_ladder_runs_both_ways.md` §7 | Officer and recognition history: Kamakura *honryō-ando* vs *shin'on* (ED-FA-0019), *sankin-kōtai* (ED-FA-0020), Zhang Juzheng *kaochengfa* (ED-FA-0021), Arte della Lana and Book of the Eparch (ED-FA-0022/0023), Florentine scrutiny and Medici *accoppiatori* (ED-FA-0018) | none (chapter); verification notes attached (R8 FILES) | FA-lane rulings; two RATIFIED "prose only"; the Florentine row carries "[UNVERIFIED — L5 quotation, archive unread]" (R8 C) [READER]. TL05 §10 admits ten officer surfaces have no historical grounding (R8 G) |
| `canon/03_canonical_timeline.md` l.84, l.92 | Deed-monarchy (Carolingian, Pepin's papal legitimation); "Coup Counter and Motion of No Confidence are the enforcement mechanisms" | Canonical reference document, 2026-04-11 (A4a) | **World truth, not research** (`00_INDEX.md` §2.B last row). The succession rule it states has no carrier in code (§3.1) |

Not located for this bin: any historical source on **personal loyalty as a quantity**, on **defection cascades** (the
relational graph's §7 mechanism), or on **character progression** (skill gain, ageing, retirement). RTP covers rise and
fall of standing; nothing covers how a person changes in capacity over a life.

### 1.2 Cases and patterns that bear on this bin

| case | period | what is claimed | hook proposed | marks and corrections | assessment | locator |
|---|---|---|---|---|---|---|
| Seat provenance sets demotion cost | GOV, cross-civilization | a rank is "only ever as solid as the currency backing it"; favour-derived seats total ruin, kinship-derived containment | H-100 row: purview says who may revoke, provenance says what revocation costs; `power_bases` roster built and deleted unread | tier 3 (`rosters.yaml:75-88`) | **Sound as a shape; unreached.** H-100 is `grade: absent`; IN-31 proposes `REVOCATION_DISPOSAL {appointed: ban, …}` but nothing named so is in `state/gate.py` [CHECKED]; IN-31's own residue R3 says provenance is "the seat's basis, not its route" (C4b H) — i.e. the proposal keys cost on `conferral` basis, which is not what GOV says (how the seat was *won*) | hole_register.yaml:1925-1960 [CHECKED]; C4b F IN-31 |
| Patronage both ways (Roman *clientela*, *cursus*, Cicero 58 BCE) | Rome | climb gated on patron; patron's fall decays clients | `upward_patron` edge, `clientele_breadth` | none | Sound history; hook unbuilt; the one patron mechanism the season loop has is a Tenure kind with no opener for `tie/knot` (B1a P tenure_kinds) | R7 B§A1 |
| Cosimo de' Medici, "robust action" (Padgett & Ansell 1993); Albizzi 1433 | Florence | capture the gate (slate generator), not the seat | "Gate Capture", `selection_bias` | the one entry with a peer-reviewed network study behind it | **Sound**; the hook (`selection_bias`) "fits neither ambition payoff nor ladder" by RTP's own admission | R7 B§A3, B§H6 |
| Sejanus; Claudius's freedmen; Kızlar Ağası | Rome; Ottoman | access monopoly; fall by single bypass | `isolated_residence`, `access_monopoly`, correspondence filter | Sejanus D2+G1 are the same case counted twice | Sound shape; double-counted (R7 T convergences); unreached | R7 B§D2, G1, E1, H2, E5 |
| Woodville affinity cascade 1464–83 | England | one patron's cluster voided together | `patronage_cascade_voided` Key | Key retired | Nearest historical case to the relational graph's defection cascade (A5a F "Defection cascade"), but neither document cites the other | R7 B§C4; A5a F |
| Wei Zhongxian / Ming eunuch faction | Ming | succession-triggered total reversal | `succession_purge_cascade` | the case recurs in five categories (D3, E6, G4, H4, J10) | Real convergence *within one figure*, not across sources; RTP presents five entries as five cases | R7 T |
| Carolingian Mayors of the Palace | Frankish | office made hereditary; needs papal legitimation | mutable `succession_rule` | none | Sound; it is also the grounding of canon's deed-monarchy (A4a G). The season loop leaves heredity `null`, "JUDGMENT CALL flagged for attack" (B1a H, offices.yaml:43) | R7 B§F2; A4a G |
| Zeng Guofan → Li Hongzhang → Yuan Shikai | Qing | patron's asset pool transfers to designated successor | `successor_designate`, Succession Contest | Key retired | Sound shape; `succeed` exists as a verb but its effect is declined: "no heir operand, no reader" (B1b F succeed) | R7 B§A5; B1b |
| Verdun 843 | Carolingian | two-claimant succession inside a faction | grounding cited for `contest/faction.py::succession` | "cited only" | **Unverifiable here**: the cited module path is pre-restructure; nothing in the season loop resolves a succession contest | R4 C (P7 §14.5, P8 §18.1) |
| Cross-ladder gate (Investiture; Calvin's Consistory; Massachusetts Bay franchise) | 1075; Geneva; colonial US | eligibility in one ladder gated by standing in another | Cross-Ladder Gate primitive | none | Sound; the season loop has `person_predicates` incl. `church_standing` and `eligibility_kinds` closed at four — the shape is expressible, unused | R7 B§J1/J8/J9; B1a P |
| Venality (Paulette, papal venal offices, British commissions, Qing *juanna*) | 16th–19th c. | price schedules for office | Chokepoint Seat purchasable; `state.rank_sale` | "LOUDEST FLAG IN THE CORPUS" = a naming collision with mass-battle "officer" | Sound history; the season loop's `conferral_bases` are closed at appointed/elected/annex (`open: false`) — purchase is not a basis | R7 B§I1-I10; B1a F conferral |
| Catherine de' Medici; Charles V; Litz/Shay moral injury | 16th c.; clinical | Convictions scar independently; resilience | per-Conviction Scar (PP-718) | self-vetted | **Over-claimed**: two biographies and a clinical construct justify a d6 crisis table; the clinical source is used inverted (D1 G) | D1 G |
| Sorge, Luxemburg, Bellarmine, Granville, Aetius, Cœur, William Marshal, Palaiologos, Xenophon, Suger, Hypatia | various | each NPC's compromise has a historical echo | the NPC's "Behavioral AI flaw" | none | Literary analogue, sound as inspiration. All thirteen names are rows of `engine/season/npcs.yaml` [CHECKED], but none of the thirteen "Behavioral AI flaws" (CONFLICTED, IDEALIST, PROCEDURALIST …) exists in code; each person's `want` there is a capability requirement, not a motive (§3.1) | A5b G |
| Florentine scrutiny-and-lot; Medici *accoppiatori* | 1328– | impartial lot turned weighted | "the subversion is the intra-faction game" (ED-FA-0018) | [UNVERIFIED — L5 quotation, archive unread] | Unverified; ED-FA-0018 open, needs_jordan (R8 G) | R8 C, G |

### 1.3 Critical evaluation

1. **One research document serves this bin, and it is the weakest-delivered file in the research tree I have seen.**
   RTP carries agent chatter in its body, two statuses, and a synthesis (§3) that is a design for a retired
   substrate; its "~96" case count is 2 above its catalogue's 94, a minor slip against an approximation. Its *catalogue* is ordinary, mostly encyclopedic history
   and is sound at the level RTP uses it (shapes of rise and fall). Its *hooks* are not research: nearly every entry
   mints a new field, tag or Key, so 94 cases produce on the order of a hundred proposed primitives with no reuse
   analysis except §4's cross-reference to the 44 governance proposals (R7 T, B§4).
2. **Convergence is overstated.** RTP's "rise and fall are the same structure" rests on cases counted in several
   categories (Wei Zhongxian ×5, Cromwell ×3, Sejanus ×2, Cosimo ×2, Basil Lekapenos ×2) (R7 T). Several entries are the
   same historical event under different headings; they corroborate nothing.
3. **Internal inconsistency in the one primitive RTP is best remembered for.** `power_base` is a seven-value enum in §3.3
   and a two-value `{independent | favor-dependent}` field in H8 (R7 K10). The six-value `power_bases` roster the
   season loop built and deleted unread (bureaucratic, kinship, military, ideological, patronage, purchased) was
   built from GOV, not RTP: H-100 says it "was built from this research" under a GOV quotation
   [CHECKED `hole_register.yaml:1941-1956`], and `rosters.yaml:86-90` says only "TIER 3" [CHECKED]. Whether RTP's
   `power_base` influenced it is unproven.
4. **What survived the research is one sentence**, and it came from GOV, not RTP: H-100's provenance-sets-cost finding
   [CHECKED]. `git grep -l rise_to_power` returns 15 files [CHECKED]: ten inside `research/` (`00_INDEX.md`, PMM,
   the systems-integration master `_part2` and `_part4`, `cross_scale_action_catalogue_v1.md`, and five files under
   `research/provenance/2026-08-28-systems-integration-harvest/`); outside `research/`, only the quarantined
   governance compendium (two files), TL05 and two session-provenance logs. No workplan part, no engine file.
5. **The design documents' own history is decoration.** The NPC roster's echoes, the relational graph's edge-type
   analogues, the conviction taxonomy's Renaissance values and the pursuit cells' philosophy citations all name a source
   and argue no mechanism from it. The pursuit cells are the honest case: they grade themselves, and the grade is that
   more than half the cells are reasoned, not cited (C7b F).
6. **Anachronism and register.** RTP is unrestricted in era (Tammany Hall 1905, Night of the Long Knives 1934, NKVD
   succession) against a setting whose canon draws on medieval and Renaissance Europe (A4a G). The shapes may transfer;
   the document does not argue that they do.
7. **No historical source covers loyalty, defection or progression as such.** The relational graph's cascade, the
   companion's Disposition ladder and the recruitment roll (A5a F) have no historical grounding located in any
   extraction read here. [GAP: confirmed only across the extractions this lane read.]

## 2. GAME PRECEDENT

### 2.1 Sources

| path | what it is | status and method as stated | reliability finding |
|---|---|---|---|
| `research/personnel_muster_integration_master_v1.md` (PMM) | Nine game passes on personnel and muster (KOEI RoTK and Nobunaga, CK2/3, Total War, Jagged Alliance, Brigandine, Unicorn Overlord, Tactics Ogre, Triangle Strategy, Radiata Stories), plus a code audit | FILED 2026-08-27; first-person single author; no external verifier; six self-corrections in §14 (R4 FILES) | **Self-contradicting on its headline null**: lists Shogun 2 culling, Medieval II manual disbanding and CK refusing to field (l.397-402), then states "every franchise resolves non-payment as permanent desertion" (l.511) (R4 K1; `00_INDEX.md` §7 checked both). Its "4/4" counts mix lanes and games (R4 K6). Its people finding — 46 people, zero loaders (§1.1) — was true when written and is now superseded: `engine/season/data/cast.py` reads `references/npc_registry.yaml` [CHECKED] |
| `research/valoria_game_precedent_companion_v1.md` + `_part2`…`_part8` (COMP-1…8) | The collation of three programs; COMP-7 §14 "the person across systems", COMP-8 §15-22 the personnel precondition and ED-IN-0201 | PROPOSED 2026-08-28; "no precedent claim re-verified against source" (COMP-2 §7) (R4 FILES) | Marks are dropped downstream (Duel of Wits, Dominions, Blades) (R4 K7); "in six of eight, Valoria already owns the primitive" contradicted by its own table (R4 K8); COMP-7 admits Parts 1-4 never read `player_agency_v30`'s own precedent takes (R4 K4). Verdicts predate the season loop (`00_INDEX.md` §1 rule 5) |
| `proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md` (EMG / REL-G) | What stores story in CK2/3, DF, RimWorld, Nemesis, Qud/URR, KoDP/Six Ages, Pentiment; the "memory question" | REFERENCE 2026-09-06; Sonnet, web searches, no verifier; Burning Wheel and Ars Magica "not freshly verified" (R8 FILES) | The most useful precedent document for persons: it locates the null (interior state is tracked but not expressed) and the one working shape (memory read at a decision point). Its RimWorld row disagrees with itself ("only partially" vs "never" gates eligibility) (R8 K18) |
| `proposals/_session_provenance/2026-08-29-to-31/PRECEDENT.md` (PRE) | Nine nulls N-1…N-9 and slogan-form steals | no header, status, author, date or method (R8 FILES) | Unsourced. N-9 ("no surveyed game ships an NPC acting on knowingly false political information") is contradicted by S05's documented Talk of the Town fallibility model (R8 K12) |
| `proposals/2026-08-25-throughlines-and-precedent/` (THR, ch. 1-5) | Failure dossiers; ch. 2 "the ladder runs both ways" (officer and demotion); ch. 5 five failure shapes | PROPOSED; Fable/Sonnet/Opus programme, valoria-critic attack, 11 corrections all found by independent readers (R8 FILES, T11) | The best-method precedent work in the bin; its own thesis — "one absent object (a persistent named person) explains the largest connected group" (TL04 §9) — is the strongest statement in the corpus of why this bin matters (R8 T7). Counts of corrections disagree (four / eleven) (R8 K1) |
| `proposals/2026-09-30-character-and-play-surface/02_against_precedent.md` (AP) | Re-score of COMP-3 §7.11 against the season loop at `c8cc408` | PROPOSED; no verifier (R8 FILES) | Places Valoria "below the floor on factions that act, procedure, accumulating relationships" (R8 T10); the settlement ledger/`ledger_sweep` primitive that THR builds on has "no counterpart in the season loop" (R8 K17) |
| `.designs/systems/_architecture/reference/player_agency_v30.md` §1 | Declared precedents for the player's stance: RoTK officer mode, CK3 vassal play, Disco Elysium, M&B/Manor Lords, Pathologic 2, Pentiment | CANONICAL 2026-04-17, title "Design Proposal — PP-TBD" (A7b FILES) | Named takes, no sourcing; COMP-7 says "take was never bound to a module" (R4 C) |
| `.designs/systems/characters/reference/character_generation_questionnaire_v30.md` §1 | Ogre Battle (1993) questionnaire, Disco Elysium inner voices, Darklands career time | two Status lines, CANONICAL and "DESIGN DIRECTION (not yet authored)" (D1 FILES) | Three named games, no mechanics quoted; the questionnaire is unauthored |
| Uploaded `REG` (faction politics patch register, PP-660) | Skyrim guild ladders → Standing 0-7, "Skyrim Eight" per rank | header CANONICAL vs l.946 "this is a proposal document … No canon mutations performed" (U3 FILES, H) | One game, one designer's reading; not in the repository |
| `proposals/2026-10-03-verb-coverage-and-gap-fill.md` (VCD) App. B, family 63 and G15 | Grudge loop and damping (RimWorld, Guild 3, Bannerlord, Radiant AI); CK3 hooks, imprison, murder schemes | RATIFIED AS INTENT (ED-IN-0288); game claims partly [UNVERIFIED] (C8a G, H). Against the uploaded teardown: its Guild 2 evidence and slander rows hold (`3cb2a6c8` L191); its Guild 3 rows misstate the source — the AI burned the player's (not the producer's) residence, no "popularity threshold" or mob appears, and the shutdown rests on the publisher's account, not a forum post (`3cb2a6c8` L193-195 [CHECKED]; UPLOAD_CHECKS VCD table) | The only precedent that reached a scheduled person-verb (`forgive`, IN-12 step 13), and through a proposal, not research |

### 2.2 Games and systems that bear on this bin

| game | borrowed or warned against | shape | evidence grade | assessment | locator |
|---|---|---|---|---|---|
| Old World (ambitions from attitudes × families; expire on death) | goals emitted by a person crossed with the houses around him | convergence (with Kremlin mortality, K6) | unsourced in COMP-1; re-used by AP P-3 | **Applied, and reached a plan**: IN-66…IN-69 and FA-05/06 build org goals plus the person's own want, ordered by alignment (salience) — the same shape, though the plan cites ED-IN-0293 and RS-22, not Old World [CHECKED `_part5` IN-66, IN-69]. Expiry on death is not in the plan | R4 C; C7b G; `_part5` |
| Kremlin / John Company (holder ≠ controller of office) | X1 "who holds the office is separate from who controls the officeholder" | claimed 5-system convergence | three of five rows are historical; the pairings run "opposite directions" (R4 K10) | **Over-claimed convergence.** The season loop separates `hold` from `oblige` (IN-40) but has no controller relation; the regent path is IN-48, built and reverted (C4b H) | R4 C, K10 |
| CK council-seat denial (−40 opinion) | a passed-over NPC accrues a Grudge tag (steal #1) | single game | none | Unreached: the season loop has no grudge store; `forgive` is specified to remove negative stance rows, and "grudge rows never end" is an open cost (C8a H) | R4 C |
| CK3 landless + DF demotion + Shogun 2 bands | demotion must be its own game: seated / displaced / dishonoured | complement K1 | community-derived | **Contradicted by code state, not by design**: revoke executes 0 in the realm (H-207 "IN-53 built and falsified"), and IN-31's proposed `REVOCATION_DISPOSAL` gives two outcomes keyed on the seat's basis — `appointed` → permanent `ban`, `elected`/`annex`/none → no disposal — not the three bands (B2b H; C4b F; [CHECKED `proposals/2026-10-14-in31-revocation-cost-provenance.md:146`]). Appointed → ban lines up with GOV's "favour-derived → total ruin", but on the seat's basis, not the route (R3, :25, :606) | R4 C; R8 C |
| Imperator: Rome loyalty bleed | failure shape A: run maximum mitigation against maximum accrual | failure dossier | links not re-verified | Applicable to the relational graph's strain accrual (A5a F "Strain accrual/decay") and to the scar writer (scar ≥ 3 entries 61 → 508 after two seasons with fifteen weights, IN-65 [READER of plan, MEASURED as a session probe]); no document applies it to either | R4 C; R8 C |
| Shadow of War War Chests | failure shape E: provenance field on every durable tag | failure dossier | patent and press | Sound warning; the season loop's claim ledger does carry `source` and `chain` (B1a P `claim_sources`; B2b F H-157), which is the shape asked for | R4 C; R8 C |
| CK3 population (6-7 parentless 16-year-olds/month; 24,000-character saves) | refuse #13: "generate on demand, not on a clock" | refusal | community-derived numbers (leads only) | **Honoured**: the cast is 46 authored rows; `generate_npc` has no production call site (A5b H S§7); `CENSUS generates nobody` (C8b H) | R4 C; R8 C |
| Radiata Stories (175 NPCs on static schedules) | "cheap row, theatre not simulation" | single game | none | Matches `npcs.yaml`'s 46 rows with home and tie (B1a P) | R4 C |
| Jagged Alliance 2 / 3 | publish every input, a band not a number, never the trigger point; JA3 compressed morale to ±1 AP | convergence X2 "5/5"; complement K8 | v1.13 docs fetched | Sound and widely quoted; nothing in the bin's code publishes or hides a band — the cast has no player-facing surface yet | R4 C |
| Triangle Strategy hidden conviction axes (fixed roster) | three hidden conviction axes per character | single game | none | The closest commercial analogue to the 13-Conviction / 15-pursuit vector; COMP-5 records it and nobody cites it in the conviction work | R4 C (P5 §12.5) |
| RoTK officer mode; CK3 vassal play | on-behalf vs within stance; dual agenda | declared precedent | manual quote (RoTK) | Declared at `player_agency_v30` §1 and never bound (R4 C P7 §14.2). The Standing ladder it grounds is not a carrier in the season loop (no `Standing` in `rosters.yaml` rosters, B1a P) | A7b G; R4 C |
| Skyrim guild ladders | Initiation Duty, Hall Tier, Livery, Mentor, Dismissal → Standing 0-7 per faction | single game | designer reading | Unreached; the uploaded register is not in the repository and its ladders do not exist in code (U3 F, H) | U3 G |
| Dwarf Fortress, Nemesis, Wildermyth (Tale-Spin effect) | state grows combinatorially, expression linearly; a dead officer must leave a queryable trace | convergence X8 | Nemesis patent; DF wiki | **Honoured in part**: the claim ledger keeps deeds (`person.died` with `seen.who`, IN-58 M-who 18/18 realm) [READER `_part5` IN-58]; expression has no carrier (N-2 null stands) | R4 C; R8 C, T2 |
| RimWorld (mood = sum of decaying thoughts) | memory feeds mood only | divergence | wiki | EMG's "memory question": memory works only when read at a decision point; IN-72 exists because a death claim fell to attention tier 4 and was never read (`_part5` IN-72) — the precedent's lesson re-learned in code, uncited | R8 C, T3; `_part5` |
| KOEI RoTK officer bonds (Liu/Guan/Zhang oath; Lü Bu) | relational edges, defection cascades | named analogue | no citation | Grounds the relational graph's six edge types (A5a G); the season loop's `tie/knot` effect is declined: "tie formed 83 offered 0" (H-182) (B2b H) | A5a G |
| Disco Elysium; Ogre Battle; Darklands | questionnaire character generation; inner voices | named | none | Unreached; no character generation exists in the season loop (`requirements.yaml` scale "character creation/development" UNRULED, B1a H) | D1 G |
| Pendragon Glory; CK trait acquisition; Darklands ageing | Renown as threshold currency; rank grants attributes; fixed chargen stats that age | named | none | Proposed only in the uploaded progression horizon model, PROPOSED and `[SELF-AUTHORED — bias risk]` (U2 FILES, G) | U2 G |

### 2.3 Critical evaluation

1. **The sourcing floor is mostly honoured in the research files and dropped downstream.** COMP-1 marks Duel of Wits,
   Dominions and Blades as unverified; later parts reprint the figures unmarked (R4 K7). For this bin the dropped marks
   matter less than the absent ones: Old World, Kremlin, CK council denial and Triangle Strategy carry no mark at all
   and no sourcing (R4 C).
2. **Convergence counts are inflated.** X1 counts five "independent systems", three historical and two running in
   opposite directions (R4 K10). The three programs' independence is asserted while two of COMP's own parts say the
   declared precedents descend from one un-audited source (R4 K11).
3. **The nulls are the most valuable precedent for this bin, and one is contradicted.** N-2 (no expression channel
   for interior state) and N-7 (no convergent answer on the appointed governor) stand. N-9 (no NPC acting on
   knowingly false information) is contradicted by Talk of the Town in S05 and by the season loop itself, where "a
   belief can be false and its holder cannot tell" is built (R8 K12). The repository's NPC case NPC-004 asks for
   exactly that capability [CHECKED `npcs.yaml` Haelgrund row].
4. **The precedent that reached code arrived through rulings, not research.** ED-IN-0201 (no leader, no faction act;
   the leader changes the option set, not a modifier) is recorded in COMP-8 and is Jordan's ruling; the archived ledger
   row stands `status: open` [CHECKED `registers/archive/editorial_ledger_in_archive_pre-2026-09.yaml:1765`]. The code
   that executes the gate cites H-99 and the 2026-09-13 rulings, not the companion [CHECKED: no `ED-IN-0201`,
   `companion` or game name in `engine/`]. That is correct under §0.05; it also means the companion's other people
   findings (U-3 "person as relationship ledger with roster", K1 demotion bands, X1) have no reader.
5. **Applied correctly where applied.** "Generate on demand, not on a clock" is honoured (no spawner, 46 authored rows).
   Old World's goal shape is the plan's B-X batch. Both are design convergences, not citations.
6. **One precedent document anonymizes its precedent.** The greenfield suite (v1 and v2) states its evidence as
   "surveyed franchise", "four of four surveyed franchises", and names no game or historical case (C5 G). A claim
   with no named source cannot be checked against the sourcing floor at all; it is weaker than an `[UNVERIFIED]` row.

## 3. REPOSITORY WORK

### 3.1 Heads and code: what runs

| object | what it is in code | status as stated | finding |
|---|---|---|---|
| `engine/season/npcs.yaml` | 46 rows (case, name, institution, home, want, concerns, tie), generated by `tools/export_npc_roster.py` from `engine/season/cases/NPC*.yaml`, hand-editable; read by `harness/populated.py` and two test files [CHECKED `git grep npcs.yaml`] | no status line; "THE NAMES AND THE WANTS ARE THE CORPUS'S" (header) | **A person's `want` is a capability requirement on the engine, not a motive** — e.g. Maret Uln: "Performing a Thread operation … must cost the practitioner a persistent personal resource"; Almud: "A single leader must be able to face several independent, ongoing pressure sources" [CHECKED l.94-112, 184-212]. **Five of the six faction leaders carry `institution: null` and have homes in cottages, markets or an inn in S-002…S-004** (Almud `b_s_002_cottage` — S-002 Auerheim, not the Seat S-001 Valorsplatz, `cohorts.yaml:65-67`; Himlensendt `b_s_003_market`, Vaynard `b_s_003_inn`, Vossen `b_s_004_market`, Ehrenwall `b_s_003_cottage`); the sixth, Baralta, Hafenmark's leader, is tagged `institution: Crown` at `b_s_001_court` [CHECKED `npcs.yaml:183-237`]. 18 of 46 rows have `institution: null` [CHECKED]. **This is residence and the `institution` tag, not office tenure**: a loop-built seat takes its faction from the cast (`populated.py`), and `test_fa01_head_seats.py` asserts every authored head holds an own-faction seat at build and five of six execute an act through it at the first fold [CHECKED `engine/season/tests/test_fa01_head_seats.py:18-24, 114-123`]. The plan's regicide reading inherits the residence: "the King lives at `b_s_002_cottage`; his killers at …" (`_part5` IN-59 measured basis) [CHECKED] |
| `references/npc_registry.yaml` | 46 rows; read by `engine/season/data/cast.py` (`pursuits_of`, `conviction_of`, `loyalty`, `faction_leader`) and seven other modules [CHECKED `git grep npc_registry`] | 35 `canonical`, 11 `proposed` [CHECKED] | The authored cast is thin: of 46 rows, `stats` non-null 1, `ts` non-null 10, `goals` non-null 17, `territory` non-null 7, `affiliations` 0 [CHECKED by parse]. **`cast.py`'s docstring overstates it** — "every row carries … 31 a `territory`, 30 `goals`, 29 `stats`, 32 `ts`" counts keys present, most of them null [CHECKED `cast.py:1-15` against the parse]. of the 10 non-null `ts` values eight are integers and two are strings ("75–80", "~50"), and no Python file reads the key [CHECKED parse; `git grep` for `["ts"]`/`get("ts")`], consistent with H-85: no carrier for Thread Sensitivity ≥ 30 (B1b H) |
| `faction_leaders` roster (`rosters.yaml:1467`, row H-99) | six leaders by case id, read by `cast.faction_leader`; the ED-IN-0201 gate's referent | TIER 2 source | Its cited source, `systems/factions/reference/faction_state_authoring_v30.md`, does not exist at that path; the file is under `.designs/` [CHECKED]. Guilds and Schoenland have no leader and no template, and `loyalty` returns `None` for them by design (`cast.py:287-320`) [CHECKED] |
| `cast.loyalty` (0-100) and `stance_from_loyalty` | cosine of the person's projected pursuits against the faction's role template, mapped to 0-100; turned into a stance row toward the creed | "RULED by Jordan, 2026-09-13: *Loyalty can be invented. Just do it on a scale of 0-100.*" (`cast.py:256`) [CHECKED] | **The loyalty value is a static function of authored values**, computed once at build (`cast.py:256-332`) and appended as a stance row whose referent is the leader (`harness/populated.py:787, 854-856`) [CHECKED]; nothing writes a row on that referent over a season. The same stance channel has one in-season writer: a lost field battle appends `(loser_faction, -1.0, morale_w)` and `(winner_faction, -1.0, grudge_w)` to each loser, a docstring says these "FOLLOW THE SEEDED-LOYALTY SHAPE", and both weights ship at 1 (`loop/effects_combat.py:203-205, 256-261`; `data/fixtures.py:589-590`) [CHECKED] — an Imperator-bleed-shaped, defeat-driven term, but toward the faction proposition, so it does not sum into the loyalty row. Every precedent the corpus collected on loyalty (Imperator bleed, JA2 idleness, X3 "idleness punished", EU4 loyalty vs influence) describes a moving quantity (R4 C, T) |
| `offices.yaml` (29 seats) | seats, remits, conferral/revocation bases | WORLD-GEN CONTENT | `off_king` and `off_heir` declare `conferral: null`; heredity is `null`, "JUDGMENT CALL flagged for attack" (B1a H). 14 of 29 seats revocable by nobody; computed revoke executes 0 in the realm (H-207; C4b H). `succeed` has no opener and its effect is declined: "no heir operand, no reader" (B1b F) |
| Decision layer (`decision/choose.py`, `queries/person_q.py`) | score = pursuit dot (15 pursuits × 7 axes) + stance term + urgency; crisis at scar 3; confliction from incompatible affiliations | pursuits ruled ED-IN-0261; cells FOLDED (IN-08); conviction = religious affiliation vector (STR-6, ruled) | **The conviction half is inert on `main`, a known and scheduled gap**: no registry row carries `affiliations:` [CHECKED], so `confliction` is 0 and H-188's doctrine coupling reads nothing. The repository states this itself in three places: `cast.py:222-225` ("[ASSUMPTION] No row … carries `affiliations:` yet"), H-188's default ("INERT IN THE SHIPPED REALM BY CONSTRUCTION", `hole_register.yaml:4207`) and IN-64 (state B, batch B-X; the cast's full vectors and convictions are built at worktree checkpoint `4e942bac`, `_part5` IN-64) [CHECKED]. With fifteen weights, scar entries ≥ 3 after two seasons rose 61 → 508 in that checkpoint [READER `_part5` IN-65, a session probe] |
| Grievance at read (IN-58; stance-only half landed `3bf936ee`) | `deeds_judged` judges a death or wound once, for its doer, scaled by the judge's stored stance to the victim | state index: BLK for the sworn-to half, the stance-only half landed (`valoria_master_workplan_v9.md:277`) [CHECKED] | **A disclosed residue, not a mis-recording**: hash EQUAL at the shipped `legacy` stance polarity; stance reaches candidate formation only under the non-shipped `declared` arm (7 of 12 realm pairs); the plan says the EXIT "hash MOVED" is NOT MET and names the residue (IN-70, IN-12 step 5) [CHECKED `_part5:225`; `_part2:343`] |
| `tie/knot`, `succeed` | Tenure kinds with no opener | — | "tie formed 83 offered 0" (H-182); `_eff_tie` unbuilt, no plan owner (B2b H) |
| Defection, recruitment, companions, Disposition, Standing, Renown | — | — | **No carrier in `engine/season/`** [CHECKED: no `defect`, `recruit`, `companion` outside instrument-defect names; no `standing`/`renown` roster in `rosters.yaml`]. Membership is a `commit` to a faction's creed and ending it is `release` (B1b F); changing sides is two ordinary acts |
| Character progression | `Person.capability` (retired row), `train` proposed (VCD step 9) | — | Nothing advances a person. Ageing and illness fixtures ship 0 (H-208), "age rates GAP on 29 of 46 `npc_registry` rows" (H-206) (B2b H). The older tree's census found zero writers for any attribute, skill, Disposition or Renown (G1 ST §16.0) |
| Cohorts (`cohorts.yaml`) | 37 persons at weight 2, one per settlement; only cohorts eat | WORLD-GEN CONTENT | weight 2 is "a number nobody chose" (H-170, B1a H). All 37 act with no pursuits: "their choices are urgency, a constant stance term and the draw" (`_part6` SE-06) [CHECKED] |
| `requirements.yaml` R-06 | "characters must be robustly built with goals, ambitions, convictions" | `partial` (B1a P) | the honest status; B-X is the plan's answer |
| Plan (`workplans/valoria_master_workplan_v9.md` §3 and parts 5-7) | IN-58 (BLK, sworn-to half), IN-61 succession (BLK), IN-62…IN-69, IN-71, IN-72 (B, batch B-X), IN-70 opinion of a faction (BLK), SE-04 (BLK), FA-04…FA-06 (B, B-X) [CHECKED state index l.277-325] | RATIFIED (ED-IN-0286) | **B-X is unbuilt on `main`**: `goals.yaml`, `data/goals.py`, `harness/decision_spread.py` do not exist [CHECKED]. None of the bin's plan entries cites a `research/` document [CHECKED `git grep` over parts 5-7: hits are verb names and `02_against_precedent.md` only] |

### 3.2 Design documents and proposals

| path | status as stated | what it defines | grounding cited | assessment |
|---|---|---|---|---|
| `.designs/systems/npcs/reference/npc_behavior_v30.md` (+ `_infill`) | CANONICAL 2026-04-17; ARCHIVED-NOT-CANON | Stance Triangle, Resonant Style, Decision Fork, priority trees, arcs, Leadership Deviation Ob, recruitment, Outreach/Demand caps, tracking tiers | privy counsellor's oath, Rosenthal; per-NPC analogues | **Superseded in substance by the season loop's decision layer, never retired by name.** None of its mechanisms has a carrier; FA-07 lists Leadership Deviation as a LEAVE row (`_part7`) [CHECKED] |
| `npc_behavior_system_v1.md` | SUPERSEDED | the 7-Conviction predecessor | — | dead; still referenced by later documents (A5a H) |
| `character_canon_v30.md` | PROVISIONAL; Part B never written | 13-Conviction vector, Self-Other drift (κ = 0.03 "calibrate at Stage 10"), Scar table, belief revision | Cesare Borgia | replaced by 15 pursuits (ED-IN-0261); Self-Other has no successor in code (`selfish_selfless` is an axis, not a drift) |
| `npc_relational_graph_v30.md` | PROVISIONAL, Class A (PP-724) | six edge types, strain, defection cascade, Fragility | KOEI RoTK, CK3, Medici clientela | **contradicts itself**: §7-§8 "BUILT 2026-06-09, ED-1000" and §12 "deferred" (A5a H; G1 DL §4.4, WM F3). Unreached by the season loop |
| `companion_specification_v30.md` | CANONICAL 2026-04-17 | companions at Disposition ≥ +3, max 2, departure conditions | none | unreached; "GM discretion" in a GM-less game (A5a H) |
| `npc_roster_v30.md` (+ `_infill`) | header CANONICAL, body "[EDITORIAL: … provisional]" | 13 named NPCs with flaws, Character Event cards, mode presence | historical echoes | names survive in `npcs.yaml`; flaws and cards do not. Stat blocks "Deferred to next session" and never written (A5b H) |
| `npcs_flow_skeleton_v1.md`; `characters_flow_skeleton_v1.md` | REFERENCE | traced code of the retired tree | — | record of the retired `npe.py`/`npc_ai` stubs; `generate_npc` had no production call site (A5b H); historical only |
| `conviction_taxonomy_v30.md`, `_axis_matrix`, `_migration_roster`; `conviction_track_v1.md` / `_v30.md` | CANONICAL heading / PROVISIONAL body; v1 SUPERSEDED-and-CANONICAL | 13 Convictions, 13×4 matrix, per-Conviction Scar, territory Piety Track | Renaissance values; Catherine de' Medici; Litz/Shay | the 13 → 15 pursuits migration is executed (`candidate_pursuit_cells.md` §4); the per-Conviction Scar survives as "scar is a COUNT per element" (ED-IN-0261) |
| `character_histories_v30.md`; `character_generation_questionnaire_v30.md` | CANONICAL with open EDs; questionnaire "not yet authored" | lifepath, sparking, Recall slots; questionnaire | SaGa; Ogre Battle, Disco Elysium | unreached; character creation is an UNRULED scale in `requirements.yaml` (B1a H) |
| `.designs/systems/_architecture/reference/player_agency_v30.md`, `generational_transition_v30.md` | CANONICAL / "proposed §11" | Standing 0-7 (and 0-5 in the same file), Duty, Renown, leadership acquisition, Lineage Acts | RoTK officer mode, CK3 vassal play | unreached; Standing range contradicts itself (A7b H) |
| `research/rise_to_power_roster_system_research_v1.md` §3; `.audit/2026-07-12-governance-compendium/40_roster_officer_system.md` | FILED + PROPOSAL; PROPOSED | Ascendancy engine, `power_base`, consolidation_progress, shared Standing ladder | RTP | **built on the retired Key substrate** (A8a H; R7 K14); quarantined; unreached |
| `governance_ripple_substrate_v1.md`, `governance_type_registry_v1.md` | PROPOSED | `power_base`-shaped response vectors | compendium M1 | Key-built; unreached |
| `proposals/2026-09-16-conviction-decision-layer/`, `2026-09-18-character-decision-layer/PROPOSAL.md`, `2026-09-26-decision-layer-execution-plan/` | REFERENCE (absorbed into ED-IN-0251/0261); PROPOSED, retired by FORK; FOLDED INTO THE BUILD (IN-08) | score terms, precedence bands, affiliation roster, crisis selector, 15×7 pursuit cells | CPC §1a philosophy | **the grounded line of the bin**: rulings plus cells that code reads. CD and CV disagree on whether `cost(c)` exists (C7a H); CPC's 55 of 105 cells are "reasoned" |
| `proposals/2026-10-14-in31-revocation-cost-provenance.md` | PROPOSED; partly CONDITIONAL on IN-48 (reverted) | appointed → permanent `ban` on revocation | H-100 (GOV) as "vocabulary not authority" | keys cost on `conferral` basis; GOV keys it on how the seat was won; its own residue R3 says so (C4b H) |
| `proposals/2026-10-14-in48-delegation-carrier.md` | HELD: built and REVERTED, contradicts Layer 1 | `delegate` Tenure kind | — | dead by its own record |
| `proposals/2026-10-03-verb-coverage-and-gap-fill.md` (VCD) G15 | RATIFIED AS INTENT (ED-IN-0288) | `forgive`, `tend`, `train` | game acts (RimWorld, Bannerlord, Radiant AI), Venetian and English procedure | scheduled (IN-12 steps 9, 13); proposal-grade; the 707 acts behind it come partly from two surveys not in the repository (C8a G) |
| `proposals/2026-10-04-forcing-churn-and-the-story-bar.md` | RATIFIED AS INTENT except CAST-POPULACE | CAST-DISPOSITION, CAST-POPULACE | — | CAST-POPULACE is SE-04 (c), held for Jordan's construal [CHECKED `_part6`] |
| `proposals/2026-08-29-valoria-from-scratch/02_the_person.md`, `07_alignment.md`; `2026-08-31-ideal*` | PROPOSED; superseded by ideal-v2 then ARCHITECTURE_V2 | Person with marks, practice, stance, knots; commitment degrees 0-5; 7 `power_base` shapes; succession pointer {cognatic-senior, marriage, deed, grant, forged} | "Research files cited by path: NONE" (C6a G) | ancestors of the season loop's Person; `power_base` re-enters uncited from RTP. Person names inconsistent across its own files (Aldwin ×4, Gerik ×4) (C6a H) |
| `proposals/2026-08-28-greenfield-systems-suite/` (v1), `-v2/` | v1 SUPERSEDED; v2 PROPOSED | personnel management, character generation, succession claim contest, Grudge on passed-over candidates | anonymized precedent; COMP, PMM, SIM by path | v1 "six claims known false"; unreached |
| `proposals/2026-08-15-character-and-faction-stats-and-progression.md` | PROPOSED, HELD FOR JORDAN | faculties, Practice accrual (+0.02D decided, +0.05D contested-and-lost), three progression ladders | DCSS, EVE, SaGa, Pendragon, Burning Wheel (Appendix "not present in this file") | the only progression design with numbers; its cited precedent appendix is missing from the file (G1 H, "missing referents"); draft 1 held two fabricated quotes, removed (G1 H) |
| Uploaded documents (REG PP-660 standing ladders; 3M three modes; PH1/PH2 progression horizon; V8 arc vectors) | not in the repository | Standing 0-7 per faction, Generational Trigger, NPC longevity %, Torben Loyalty clock | Skyrim; Pendragon | historical context only; none reached the tree (U2, U3) |

### 3.3 Internal contradictions that matter, and retired apparatus

1. **Two rosters of the same 46 people disagree on where they live and which institution tags them.** `npc_registry.yaml`
   NPC-020 Almud is `faction: Crown`, `role: King`; `npcs.yaml` NPC-020 is `institution: null`, home `b_s_002_cottage`
   [CHECKED both]. The same holds for four more faction leaders. `npcs.yaml` derives institution and home from the case
   prose by first-hit matching ("reordering MOVES PEOPLE", B1a F `seat_precedence`); the registry is authored. The
   disagreement does not reach office tenure: a seat's faction comes from the cast, and FA-01's test asserts every
   authored head holds an own-faction seat [CHECKED `engine/season/tests/test_fa01_head_seats.py:18-24, 114-123`]. The
   leaders are mis-housed, not mis-seated. Lane: **IN** (world-gen) and **FA**.
2. **"Conviction" names two things inside one file.** `npc_registry.yaml`'s `convictions:` holds pursuits; its
   `affiliations:` is read into `Person.conviction` (header l.6-24) [CHECKED]. STR-6 ruled conviction = religious
   affiliation (C4b F). The design corpus uses Conviction for a 13-value moral roster, a 9-value legacy roster, an
   8-value `npe.py` roster and a per-territory 0-5 track (D1 H; G1 ML §8 #1). Lane: **IN**.
3. **Per-person facts disagree across every surface.** Haelgrund: TS 12 hidden (roster, analyses), TS 15 (registry)
   [CHECKED], and two first names, Sæmund and Registrar Lennart (A5a H; G1 H). Maret TS 0 / 35 / ~50; Almud 28 / 0;
   Edeyja's Conviction Continuity vs Warden (A5a H). No code reads them: no Python file reads the registry's `ts` key [CHECKED `git grep`]. Lane: **WR**.
4. **Standing is 0-5, 0-7 and 0-10** across `player_agency_v30` (both ranges in one file), the clock registry, the
   uploaded PP-660 and the contest kernel (A7b H; G1 ST §7 #3; U2 H). No carrier in the season loop. Lane: **FA**.
5. **Defection is "NOT a roll" and a Spirit TN 7 roll against Disposition** in one document (A5a H); the season loop
   has neither — defection is `release` + `commit`. Lane: **FA**.
6. **Succession has five designs**: Standing 7 offered / 5-6 contest (`player_agency_v30` §5.2), Generational Trigger
   (PP-660), PC-death options (`hybrid_gaps` G-086), Ascension Arc (uploaded LW), and IN-61's heir title plus `succeed`
   claim (RS-27). Canon's deed-monarchy names "Coup Counter and Motion of No Confidence" as enforcement (A4a F), and the
   Coup Counter itself both "never decrements" and "resets" (U3 H). Only IN-61 is scheduled. Lane: **IN/FA**.
7. **Retired Key substrate as the foundation**: RTP §3.4 (~60 Key types), compendium Part 40, the ripple substrate,
   the axis matrix §5 (`key_substrate_v30` §2.5), the NPC flow skeleton's Key edges, and the armature interpretation of
   NPCs (`interpretation(npc,key)`) (R7 K14; A8a H; A7b F; D1 H; A5b H). All of it is unreachable by construction.
8. **GM language in a GM-less design**: companion spec, behaviour Hooks ("GM decision"), roster ("GM tracks"),
   histories ("GM provides") (A5a H; A5b H; D1 H). Every such rule is unimplementable as written.
9. **IN-58's EXIT** ("hash MOVED") is not met, and the plan says so: the state index lists IN-58 as BLK for its
   sworn-to half with the stance-only half landed (`valoria_master_workplan_v9.md:277`), and `_part5:225` and
   `_part2:343` state the unmet EXIT and name the residue (IN-70, IN-12 step 5) [CHECKED]. A disclosed residue, not a
   contradiction. Lane: **IN**.

### 3.4 Critical evaluation

The bin holds two different objects under one name. The **design corpus's NPC** (Stance Triangle, Resonant Style,
Scars, priority trees, arcs, flaws, Disposition, companions, relational graph, recruitment) is almost entirely
quarantined and has no carrier. The **season loop's person** (15 pursuits, stance rows, a claim ledger, a scar count,
an affiliation vector, tenures, a loyalty cosine) was built from Jordan's rulings and the decision-layer proposals, and
it runs. They share 46 names and nothing else: the names come from the old roster, the wants are engine requirements,
and the mechanics are new.

What runs is grounded in rulings and in its own measurements, which is the correct grounding under §0.05. What it
lacks is most of what the research and precedent describe as the substance of people in a political game — standing
that moves, a loyalty value that accrues and bleeds toward its own referent (the one in-season stance term, a defeat
bleed, points at the faction, not the leader: `loop/effects_combat.py:256-261` [CHECKED]), grievance that persists
and ends, succession that is contested, bonds that form. Each of those has a hole row, a reverted build, a declined
effect or a plan position, and none cites the research that exists for it. The authored cast is also thinner than
the loader's docstring says, and `npcs.yaml` houses five of six faction leaders in cottages, markets or an inn with no
institution tag; their office tenure is correct and tested (FA-01), but the plan's regicide reading (IN-59) inherits
the residence.

## 4. JOIN: FUNCTION, VERB AND PRIMITIVE AGAINST EVIDENCE

Verdict key: GROUNDED · PARTLY · UNGROUNDED (nothing cited) · CONTRADICTED · UNREACHED (research exists, no owner reads it).
"Ruled" grounding (a Jordan ruling) is recorded as such; it is the legitimate source under §0.05 but it is not research.

| function / verb / primitive | repository claim (status) | historical evidence | game evidence | joined verdict | locator |
|---|---|---|---|---|---|
| Named cast as authored rows, no spawner | 46 rows loaded by `cast.py`; `npcs.yaml` (built) | per-NPC echoes (inspiration only) | CK3 population refusal "generate on demand"; Radiata "cheap row" | **PARTLY** — the game refusal is honoured by design convergence; the history is decoration | §3.1; R4 C; A5b G |
| Faction leader is a person; no leader, no faction act | `faction_leaders` (H-99), `test_fa01_head_seats` (built); ED-IN-0201 ruled, archived row `status: open` | RTP F/G series (retinues, purges) not cited | COMP-8 records the ruling; TW Three Kingdoms "changes the option set, not a modifier" | **PARTLY** (ruled; precedent recorded beside it, not read) | [CHECKED] ledger archive :1765; R4 C (P7 §14.3, P8 §19) |
| Loyalty 0-100 | `cast.loyalty` cosine to role template; static (built, "can be invented") | RTP `power_base` liabilities; GOV "rank only as solid as its currency" | Imperator bleed; JA2 idleness; X3 "idleness punished 4/5"; EU4 loyalty vs influence | **UNGROUNDED (ruled invention) · precedent UNREACHED** — every cited precedent moves loyalty over time; this value is static and nothing writes its referent (the leader); the only in-season stance term of that shape is a defeat bleed toward the faction (`effects_combat.py:256-261`), uncited to Imperator and unreached (no field is fought); regard computed at read does move live (`fixtures.py:741-750`) | `cast.py:256-332`; `populated.py:787, 854-856` [CHECKED]; R4 C, T |
| Pursuits (15) × axes (7) as the decision's moral term | IN-08 cells (built); ED-IN-0261 ruled | philosophy traditions per pursuit (CPC §1a); 55 of 105 cells "reasoned" | Triangle Strategy hidden conviction axes (uncited); Prom Week's diffuse-causality caution | **PARTLY** | C7b F, G; R4 C (P5 §12.5); R8 C |
| Conviction = religious affiliation vector; confliction | STR-6 ruled; `conviction_of` built; **0 rows authored on `main`** | none | none | **UNGROUNDED and inert** — a known, scheduled gap (H-188's default; IN-64, batch B-X) | [CHECKED registry parse]; B2b H |
| Scar count, crisis at 3 | `_scar`, `conviction_after_crisis` (built); scar entries 61 → 508 with full vectors (session probe) | Catherine de' Medici, Charles V, Litz/Shay (PP-718 self-vetting) | none | **PARTLY** — history over-claimed for a d6 table that no longer exists; the live rule cites none | D1 G; `_part5` IN-65 |
| Grievance at read (IN-58) | stance-only half landed, sworn-to half BLK; EXIT "hash MOVED" not met, disclosed by the plan | RTP G-series (patron-lapse purges); vendetta edge type | CK council denial −40 Grudge; RimWorld; Nemesis encounter log; M&B execution starts feud | **UNREACHED** (research) · game shape present, uncited | [CHECKED `_part5` IN-58]; R4 C; C8a G |
| `forgive` (a grudge ends) | VCD G15, IN-12 step 13 (scheduled) | wergild (uploaded v3 P8, not in tree) | RimWorld, Guild 3, Bannerlord, Radiant AI (VCD family 63); Guild 3 is a negative case, not a damping precedent: its citizen layer burned the **player's** residence "at roughly every second launch" and was switched off at the publisher's request (`3cb2a6c8` L193-195, T1; `6039edcc` L241) [CHECKED] — VCD:985 says "producer's", and F77's "popularity threshold" (VCD:1122) is in neither upload | **PARTLY** (proposal-grade game evidence; R-9 "grudge ends only by `forgive`" vs MATTER decay is Jordan's) | C8a F, G; C8b H |
| `tie/knot`, relational edges, defection cascade | effect declined (H-182: 83 formed, 0 offered); graph PROVISIONAL, BUILT/deferred | Woodville affinity cascade (RTP C4), *fede giurata*, Medici *clientela* — not linked | KOEI RoTK officer bonds; CK3 | **UNREACHED** | B2b H; A5a G; R7 B§C4 |
| Changing sides (defection) | `release` + `commit` (commit executes since IN-11, H-156) | RTP F6 Wallenstein (subordinate flip), H8 favour-dependent counter-faction | Pax Pamir punished switching — T0 rulebook rule confirmed in the uploaded teardown (`3cb2a6c8` L70-72, L487-491) and thirteen-game survey (`b42377f7` L110, B2) [CHECKED]; SFP **borrows** it "in its exact shape" (forfeit what came through the loyalty: seats, entrenchment) and refuses only the discard (`03_PROPOSALS_POLITICS.md:249-252`), ENP v2 carries it as M7 perishable allegiance (`04_PROVENANCE.md:164`) [CHECKED]; its carrier was `repudiate`, cut at IN-11; JA2 staffing refusals | **UNREACHED** — two ordinary acts with no trigger; a witnessed vow-break is priced only at `release`'s alignment cells (H-205, `absent`; its `cite:` attaches it to Jordan's CELL-VALUE AND COSINE PASS, whose ask-then row omits it: `hole_register.yaml:4415-4426`, `_part5:531` [CHECKED]); the design check (Spirit vs Disposition) has no carrier | B1b F; R7 B; C4a G; C7a G |
| Recruitment, companions | none built (PP-642; companion spec CANONICAL, quarantined) | none | none cited | **UNGROUNDED** | A5a F; §3.1 |
| Succession (heir title + `succeed` claim) | IN-61 BLK; `off_king`/`off_heir` `conferral: null`; `succeed` declined | RTP F2 Carolingian mayors, A5 successor designate, C1 banked claim, J7 institutional search; Verdun 843; canon deed-monarchy | CK3 succession laws (VCD P47); Old World ambitions expiring on death | **UNREACHED** — IN-61 cites only RS-27 and the code; none of RTP's succession cases is read | [CHECKED `_part5` IN-61]; R7 B; R4 C |
| Revocation cost by seat provenance | H-100 `absent`; IN-31 PROPOSED (keys on `conferral`) | GOV: cost keyed to how the seat was won (favour → ruin, kinship → containment) | CK3 landless + DF demotion bands (K1) | **PARTLY** — the only research finding about persons in the season register; the proposal that answers it measures a different variable | [CHECKED H-100]; C4b F, H |
| Rise to power / Standing / advancement | no carrier | RTP A–J (94 entries), `power_base` | RoTK officer mode; Skyrim guild ladders; CK3 vassal play | **UNREACHED** — RTP has no reader; the `power_bases` roster built and deleted unread came from GOV (H-100), not RTP | [CHECKED `hole_register.yaml:1952-1956`; `rosters.yaml:86-90`]; R7; U3 G |
| Organization goals and the person's own want (B-X: IN-66…IN-69, FA-05/06) | plan B, unbuilt on `main` | none | Old World (ambitions from attitudes × families) — uncited | **UNGROUNDED in cited evidence; convergent with Old World** | [CHECKED `_part5`, `_part7`]; R4 C |
| Opinion of a faction (IN-70) | BLK, design first | none | EU4 estates (loyalty vs influence) uncited | **UNGROUNDED** | [CHECKED `_part5` IN-70] |
| Access gate and guard weight (IN-59/60) | BLK; measured 0 of 10 season-0 kills co-located | none | none | **UNGROUNDED** — measured, not researched; its premise rests on leaders' homes that §3.3 item 1 shows are mis-derived (residence only; their seats are correct, FA-01) | [CHECKED `_part5` IN-59/60] |
| Cohort as a weighted person; CAST-POPULACE | 37 cohorts at weight 2 (built); spread held (SE-04 c) | Sen entitlement failure (FASE, for dearth, not cohorts) | Banished/Knights of Honor II named tier; URR/Qud individuation on demand | **PARTLY** (game shape cited in EN/SFP; the weight is "a number nobody chose") | C7a G; C4a G; B1a H |
| Witnessed deeds and memory (`seen.who`, claim ledger with source and chain) | built; M-who 18/18 realm | none | Nemesis, DF, Talk of the Town (provenance); EMG "memory read at a decision point" | **PARTLY** — EMG's lesson re-learned at IN-72 (death claims fell to attention tier 4) without citation | [CHECKED `_part5` IN-58, IN-72]; R8 T3 |
| Interior-state expression (an NPC's mood or grudge shown) | none | none | null N-2 (no shipped solution) | **null stands; correctly unclaimed** | R8 T1 |
| Character progression (practice, `train`, attributes, ageing) | none built; `train` proposed; ageing fixtures 0 | none | SaGa sparking, Pendragon, DCSS/EVE, Burning Wheel (stats proposal; appendix missing) | **UNREACHED** (game) · **UNGROUNDED** (history) | G1 F, G, H; B2b H |
| Character generation (lifepath, questionnaire) | none; scale UNRULED | none | Ogre Battle, Disco Elysium, Darklands | **UNREACHED** | D1 G; B1a H |
| Priority trees, Leadership Deviation, Resonant Style | none (FA-07 LEAVE row for Deviation) | none | none | **UNGROUNDED and unreached** | A5a F; `_part7` FA-07 [CHECKED] |

## 5. WHAT THIS BIN'S CORPUS DOES NOT COVER, AND WHAT I DID NOT READ

- [GAP: historical loyalty, defection and progression — no research file or extraction treats personal loyalty as a
  quantity, defection as a process, or a person's capacity changing over a life; RTP covers standing only.]
- [GAP: `research/governance/political_hierarchy_standing.md` — its extraction (A9) is outside this bin; I relied on the
  verbatim quotation at `hole_register.yaml` H-100 and did not evaluate the file's method.]
- [GAP: `institutional_persistence_pre1600.md` — cited by the uploaded v3 design document for H1' Magnate Crisis, H2
  Inner Circle Removal Cascade and H3 Continuity Check (U1 G); it is not in the repository [CHECKED `git ls-files`].]
- [GAP: the two uncommitted surveys (*Mechanics of Inquiry, Speech and Rule*; *Narrative Churn*) behind VCD's person
  verbs — known only as VCD carries them (`00_INDEX.md` §7); absent from the uploads too (UPLOAD_CHECKS, "STILL ABSENT").]
- [SUPERSEDED GAP: the uploaded precedent documents pinned by ENP v2 (`04_PROVENANCE.md:130-138`) — the nine-title
  teardown (`3cb2a6c8`), *Thirteen Strategy Games* (`b42377f7`), the mechanical specifications (`773bbfde`) and *Twenty
  Games* (`6039edcc`) — are now in hand (not in the repository); they are evaluated as NPC-lane game precedent in §7-§8.]
- [GAP: FASE T5 (governor control) and T9 (interregna), which `00_INDEX.md` §3 lists for "People: roster, loyalty,
  succession" — their extraction (R6) is outside this bin.]
- [SKIPPED: the bodies of RTP and PMM — I relied on R7 and R4, opening RTP only to check its head, its count and its
  agent chatter.]
- [SKIPPED: `engine/season/hole_register.yaml` rows beyond those the B2 extractions and my own reads of H-100 cover.]
- [SKIPPED: `workplans/valoria_master_workplan_v9.md` §3 prose beyond the state-index rows for this bin's handles.]
- [CONFIDENCE: medium — the scar 61 → 508 figure, the 0-of-10 co-location figure and the regicide reading are
  session probes quoted in the plan, not repository artifacts; I did not re-run them.]
- [CONFIDENCE: medium — C6_2…C6_4 and C5_1 were read by targeted search for person-related lines, not in full; all
  optional files carried their final `## X` section.]

## 6. METHOD NOTE

This file was written from the reader extractions in `scratchpad/out/`, then attacked by an independent read-only
critic who checked 16 claims: 9 held and 7 failed or were overstated, two of them on headline problems (loyalty,
leaders' residence). Each correction below was verified against its source before it was applied.

1. Leaders are mis-housed, not mis-seated: FA-01's test (`test_fa01_head_seats.py:18-24, 114-123`) added; §0 #6, §3.1, §3.3 item 1, §3.4 and the §4 access-gate row reworded.
2. Loyalty: the value is static, but a defeat-driven stance term (`effects_combat.py:203-205, 256-261`, on at weight 1) exists toward the faction, not the leader; §0 #2, §3.1, §3.4 and §4 corrected; ruling cited at `cast.py:256`.
3. The deleted `power_bases` roster came from GOV, not RTP (H-100 l.1952-1956); §1.3 item 3 and the §4 rise-to-power row corrected.
4. `rise_to_power` is cited by 15 files, ten inside `research/`; §1.3 item 4 restated as "outside `research/`, only …".
5. §0 verdict: H-100 carries one GOV sentence and VCD carries one precedent to the plan; "no code, data owner or plan entry" narrowed to "no code reads it, no plan entry cites it".
6. IN-58 is BLK in the state index and the plan discloses the unmet EXIT; §0 #11, §3.1, §3.3 item 9 and §4 reframed as a disclosed residue.
7. The inert conviction half is stated in `cast.py:222-225`, H-188 and IN-64; §0 #9, §3.1 and §4 call it a known, scheduled gap.
8. IN-31's disposal gives two outcomes keyed on the seat's basis (proposal :146), not "a single band"; §2.2 CK3/DF row corrected.
9. No Python file reads the registry's `ts` key; eight of ten values are integers; §0 #5, §3.1 registry row and §3.3 item 3 corrected.
10. RTP's "~96" against 94 entries softened to a minor slip; §0 #4, §1.1 RTP row and §1.3 item 1 reworded.

§0 was re-ranked: the old #1 (loyalty) moved to #2, the old #2 (leaders) to #6, the old #3 (conviction) to #9 and the
old #5 (IN-58) to #11; the old #6 (no carrier for succession, defection, standing, recruitment and bonds) now leads.

## 7. THROUGHLINES

**Verdict.** Sixteen throughlines: six convergences (T-NPC-14 only as claimed; T-NPC-10 and T-NPC-16 from one
producer), three nulls, two failure shapes and five repository patterns (T-NPC-8 is filed as a null and carries a
failure shape too). Twelve are SOUND (T-NPC-3 partly unreached, T-NPC-13 partly unverified), two OVER-CLAIMED (T-NPC-10,
T-NPC-14), one UNVERIFIED (T-NPC-16) and one CONTRADICTED (T-NPC-15). The precedent converges, on independent sources,
on a person whose loyalty moves and whose kin, heir and bonds tie him to the polity; that his usefulness breeds his own
threat rests on one producer. The code holds a person whose wants differ, whose regard and beliefs move at read in
shipped play, and whose values, capacity, unwounded body, ties and stored loyalty do not move. The one null Valoria
fills, belief in transit, is the one the uploaded teardown warns fails unless it is displayed. Independence is weak throughout: the nine-title teardown (TD, `3cb2a6c8`) and *Thirteen
Strategy Games* (13G, `b42377f7`) survey disjoint titles but come from one undisclosed producer, and *Twenty Games*
(20G, `6039edcc`) reconciles the two, so it is derivative and adds no independent case. Upload line numbers are `L`n.

### 7.1 Register

| ID | pattern | kind | cases / sources (independent count) | counter-evidence, limits | REACH IN CODE | REACH IN PLAN | verdict |
|---|---|---|---|---|---|---|---|
| T-NPC-1 | Loyalty moves over time | CONVERGENCE | 13G B4 Imperator power base, −0.55 loyalty per unit (L194, L134-135); A2 currency supplied by loyalty (L176) [CHECKED]. COMP/PMM X3 "idleness punished 4/5" and failure shape A, Imperator bleed (R4 T) [READER]. **Two independent** (13G; COMP), sharing Imperator and RTK. RTP is not a third: its "each rise carries its own characteristic fall" (R7 T) [READER] is about a person's standing, not his loyalty | 13G B3 kinship lock is a loyalty that deliberately stops moving; B7 hidden loyalty is a negative result (L198-200) [CHECKED]. Jordan's ruling fixes the scale ("0-100"), not the motion (`data/cast.py:256`) [CHECKED] | **stored row static; regard moves at read.** A static cosine at build (`data/cast.py:256-332`) becomes one stance row toward the leader (`harness/populated.py:787, 854-856`) [CHECKED §3.1]; no writer changes it. The in-season stance writer, a lost field's −1.0 rows toward the faction proposition, **ships at weight 1, unreached**: "all 11 `march` attempts refused at ENCOUNTER … no field fought" (`requirements.yaml:1124-1125`; `loop/effects_combat.py:241-260`; `data/fixtures.py:589-590`) [CHECKED], and this pass's probe appended no stance row (§9). Regard toward the head does move in shipped play, through `judged_gain`/`told_valence_gain` 0.5 (`data/fixtures.py:741-750`; `requirements.yaml:1132-1139`) [CHECKED], but only on the deeds `deeds_judged` admits (death, wound, undecided contest; §9.2 C2) | IN-69 (B, B-X) moves the cosine to `data/pursuits.py::alignment` and **reads** it to order own want against faction goal (`_part5:311-313`) [CHECKED]: a new reader, still no writer. IN-70 opinion of a faction (BLK, B-R) | SOUND · UNREACHED (the stored row); the motion precedent describes is carried only by regard at read |
| T-NPC-2 | Allegiance never arrives late: every opinion is recomputed on the tick; nothing models a grievance that matures or a belief in transit, except The Guild 2's evidence | NULL | 13G R1 (L274, L345) [CHECKED]; TD §4.6 "Allegiance never arrives late" (L472) and unoccupied combination 2 (L354) [CHECKED]; 20G empty cell 3 and asymmetries A1, A9 (L142, L227, L235) [CHECKED]. **One producer**, two disjoint title sets (22 titles); 20G derivative | TD contradicts itself: Bannerlord loyalty as a "genuine lagged-consequence loop" (TD L128) and Tropico's delayed arrest cost (L447) (UP03 K4) [READER]. 13G concedes Victoria unexamined (L345) [CHECKED] | **Valoria occupies the null.** Regard is computed at read from claims that arrive by `tell` (an executed verb, BASELINE B3) with source and chain; witnesses' deposits refract in confidence (`loop/witness.py:494-495`) [CHECKED]; grievance at read is landed for its stance-only half (IN-58). Thin in the tree: 4 of 1,270 `told_by` claims arrived by a telling, one seed [AUDIT S-DOWN row] | IN-18 G5/G8 BLK; H-198 (a teller never lies) absent, no position (BASELINE B4) | SOUND (as a null); Valoria's shape is ahead of the corpus, its delivery thin |
| T-NPC-3 | An agent layer that cannot run at half strength is switched off, and per-person data that conduct does not consume becomes decoration | FAILURE SHAPE | The Guild 3: citizen AI burned the player's residence "at roughly every second launch" and the publisher asked for it to be switched off (TD L195, T1; 20G L241) [CHECKED]. Bannerlord: trait axes exist per hero and the campaign barely consumes them (13G G3 L256; TD L543) [CHECKED]. Manor Lords AI settlements cheat (TD L158, L543) [READER UP03]. 13G gate: "specify half-strength behaviour or it is a switch that gets switched off" (L361) [READER]. **Three cases, one producer** | Valoria's knobs are graded arms (0 / 0.5 / 1, `data/fixtures.py:643, 651, 736`) [CHECKED], so a half-strength setting exists by construction and the gate's letter is met; what fails is the ship state, not the shape | **Bannerlord's shape recurs**: pursuits move the score (`decision/choose.py:403-406`) [CHECKED], but convictions are authored on 0 of 46 rows [CHECKED parse], the OUGHT predicate is read by nothing (H-185, `hole_register.yaml:4162-4168`) [CHECKED] and `benefits_me` has no production caller (`git grep benefits_me` outside tests: the definition and two comments) [CHECKED]: built and inert | IN-64 (B-X) authors vectors and convictions; H-185 is in no plan position (BASELINE B4) | SOUND · partly UNREACHED |
| T-NPC-4 | Persons differ in what they want and whom they know, not in what they can do | REPOSITORY PATTERN | `Person.capability` empty on 429 of 430 corpus persons (`requirements.yaml:74-82`) [CHECKED]; `stats` non-null on 1 of 46 registry rows [CHECKED parse]; the registry's `ts` read by no Python file (§3.1) [CHECKED]; cohorts carry no pursuits (`harness/populated.py:392-395`) [CHECKED]; combat reads only `end`, mass battle `power`/`command` 4 for every side [AUDIT A1, report l.67-78]. **Two independent** (this pass's reads; the audit's) | Body band, seat and stance do differ (the audit's own counter-example). Precedent has no such corpus: every surveyed title with advancement differentiates capacity (13G G1 L252, C7 L216; TD Medieval Dynasty six skills L205) [CHECKED] | absent beyond `{copying: 3}` on one corpus person | IN-12 step 9 `train` writes capability only where a case names a vocation, and `copying` is the only key (`_part5:73`) [CHECKED]; J-13's remainder is J.2 rank 1 (`_part5:514`) [CHECKED]; K-2 not ratified [AUDIT] | SOUND |
| T-NPC-5 | Every mechanism by which a person's **values, capacity or body** change unwatched is built and shipped at its control arm; regard and beliefs are the exception and move live | REPOSITORY PATTERN | Values: `data/fixtures.py:631` scar_excludes_actor False, `:643` scar_weight_shift 0, `:651` confliction_weight 0, `:661` refusal_axis None. Body: `:530` body_step 0, `:542-544` age_step, illness_rate, age_at_build 0. Capacity: no writer of `capability` outside tests but `corpus_run.py:539` and `probes.py:580` (critic's re-run, quoted) and `train` unbuilt (IN-12 step 9) [CHECKED fixture lines]; NERS A4 (iv), T4 [AUDIT]. **Two** | **Regard and beliefs ship live**: `judged_gain` and `told_valence_gain` 0.5, "SHIPPED LIVE … per Jordan's ruling of 2026-10-09" (`fixtures.py:741-750`), `stance_gain` 1.0 (`:773`), `told_drift_band` 0.5 (`:697`); `requirements.yaml:1132-1139` records 3,270 of 11,449 realm pairs differing beyond stance against 0 at control [CHECKED]. Body moves by wound in a contest (2 persons, seed 0, one season, this pass's probe). Two telling knobs remain dark (`:736` intent_disclosure, `:789` telling_privacy), but they govern what is told, not what a person is. Values are `[OPEN — Jordan tuning]` ("JORDAN'S TO SET", fx:537); the defect is that nothing schedules arming them | built and inert (executes as a no-op) | IN-65 conditional on H-187 > 0 (B-X); refusal_axis "stays unarmed until a ruling" (`_part5:466`, BASELINE B5); age, illness, confliction, actor-scar: no position | SOUND (restricted to values, capacity and body) |
| T-NPC-6 | The person-to-polity couplings the genre runs on (heir, kin, bond, recruitment, switching cost, delegation) are the ones Valoria declines | CONVERGENCE (precedent) on a REPOSITORY PATTERN | THR: "one absent object (a persistent named person) explains the largest connected group" (TL04 §9; R8 T7) [READER]. 13G: A1, B1 and C2-C3 dominate by reach, "any design … that omits all three is doing something unusual" (L272) [CHECKED]. TD's three unoccupied combinations (L351-355) [CHECKED]. **Two independent** (THR, a repository programme; 13G) | B1 (opinion) is carried by regard at read; A1 (currency) is FA's. Several declines are rulings: AX-1 forbids stored modifiers; RS-27 makes the heir a title | `succeed` and `tie / knot` effect-declined (`verb_table.yaml:886-905, 1186-1197`) [CHECKED]; no `heir` or `succession` token in `loop/ decision/ queries/ state/ data/` [CHECKED grep, 0 hits]; no recruitment or defection token in `engine/season/` outside instrument names [CHECKED grep]; delegation IN-48 built and reverted | IN-61 (BLK, B-R); IN-32 (BLK, B-S); B-JR unscheduled (p3:276); recruitment, switching cost: none | SOUND |
| T-NPC-7 | Kinship and heredity couple a person's life to the polity's capacity: the heir sets the action budget, kin locks loyalty, children inherit | CONVERGENCE | Genghis Khan II: the ruler's Politics sets commands per season and decays with age; kin as a hard loyalty lock; child stats random at birth (13G L96-99, B3 L198, P6 L462-479) [CHECKED]. CK2 succession law, gavelkind, sixteen-year education (13G L35-37) [CHECKED]. The Guild 2: losing every controllable heir ends the game (TD L185); Medieval Dynasty: children average their parents (TD L221) [CHECKED]. RTP F2 Carolingian mayors, A5 successor designate (R7 B) [READER]. **Two independent** (the TD/13G producer; RTP) | 13G's own unfair-heir warning: a random heir costs "thirty years of reduced agency … uncaused, untraceable, unpreventable" (L553) [CHECKED]. Jordan: "designated heir is not a verb but a status or title" (RS-27, `_part5:244-246`) [CHECKED]. AX-5: "the world may never individuate a person nobody's act demanded" (`architecture/meta/01_AXIOMS.md:164-198`) [CHECKED] | absent: `Person` carries id, name, weight, capability, stance, pursuits, ledger, body, born, scar, conviction, travel_leg and no kin or parent (`state/carriers.py:645-676`) [CHECKED]; heredity is no conferral basis (`offices.yaml:43-45`) [CHECKED] | IN-61 heir title (BLK); a birth-side consumer: "no position builds one" (`_part8:134`, BASELINE B1.3) | SOUND as precedent; kin-as-mechanism is a live design option under RS-27, not a demand |
| T-NPC-8 | Tracking is not expressing: interior state a player cannot read makes no story; legibility caps state | NULL (+ failure shape) | N-2 null and "tracking is not expressing" (PRE, COMP-2 D6, S05; R8 T1-T2) [READER]. N2: Nemesis cut its faction bars because the hierarchy "looked somewhat like a Christmas tree" (`773bbfde` L321) [CHECKED]; "record only what can be surfaced" (L527, UP05 T6) [READER]. TD: belief-with-provenance "named and not recommended" unless the belief structure is displayed (L529) [CHECKED]. 13G B7 hidden loyalty (L200) [CHECKED]. **At most two independent** (N2; TD/13G). The repository leg does not count: PRE, which carries N-2, is "Unsourced" (§2.1), and COMP-2 D6 and S05 reach this pass only through R8 [READER] | AX-7 forbids an omniscient display but admits `explain` [AUDIT G6]. EMG names games that do express interior state (R8 C) [READER] | absent: no player surface shows a person's pursuits, stance or grievance | IN-37 chronicle render (BLK, B-U); IN-47 character sheet, "no build batch" (`_part4:39-41`) [CHECKED] | SOUND |
| T-NPC-9 | Accrual without a closer runs away, and the genre switched hostility off rather than damping it | FAILURE SHAPE | THR T-04: "accrual beats bounded restoration", 11 instances, 7 verified (R8 T6) [READER]; Imperator failure shape A (R4 T) [READER]; VCD finding 2 (`proposals/2026-10-03-verb-coverage-and-gap-fill.md:985`) [CHECKED; its Guild 3 detail corrected in §2.1]; scar entries ≥ 3 rose 61 → 508 after two seasons at fifteen weights (IN-65, session probe) [READER]. **Two independent** (THR; VCD over TD's games) | Grievance is computed at read, so no stored grudge can spiral (IN-58). The scar's consequence ships at 0 | the accrual executes: one scar count per observer per violated pursuit (`loop/resolve.py::_scar_witnesses`; H-128, `hole_register.yaml:952-958`) [CHECKED row]; no decay; `forgive` is not a verb (BASELINE B3), H-59 absent | IN-12 step 13 `forgive` (B-Q); scar decay: none | SOUND · the closer is planned, the scar's decay is not |
| T-NPC-10 | Scarcity of named agents, not their count, makes a decision weigh | CONVERGENCE | KoH II nine-slot court, "the highest decision-density-per-rule primitive" (13G C1 L204) [CHECKED]; 20G empty cell 1 and A8 (L138, L234) [CHECKED]. The audit's N-line: the scene budget makes office cost attention [AUDIT, report §5]. **One producer**: 20G is derivative of TD/13G (§7 opening); CK3's "generate on demand, not on a clock" (R4 C) [READER] is about not spawning people on a timer, not about scarcity making a decision weigh, so it is not a second source; the audit's line is a repository reading, not precedent | A cap bites through assignment, and Valoria assigns nobody: no delegation | cast fixed at 46 authored rows with no spawner (§2.2); the per-person scene budget executes [AUDIT] | none for assignment | OVER-CLAIMED (one producer) · reached only as the scarcity of a person's own scenes |
| T-NPC-11 | Research and precedent reach the person only through Jordan's rulings, uncited, and their failure shapes stay behind | REPOSITORY PATTERN | ED-IN-0201 vs COMP-8 (§2.3 item 4); Old World ≈ B-X, uncited (§2.2); Imperator bleed ≈ field grudge rows, uncited (§3.1); EMG's memory-at-decision ≈ IN-72, uncited (§2.2); RTP read by no plan part (§1.3 item 4) [CHECKED in §1-§3]. One tree, five instances | Correct under §0.05: a ruling licenses code, a citation does not | n/a | none of parts 5-7 cites `research/` (§3.1) [CHECKED] | SOUND; its cost is T-NPC-3's and T-NPC-9's lost warnings |
| T-NPC-12 | Two NPCs under one name: the quarantined corpus and the season loop share 46 names and no mechanism, and the person-level facts disagree on every surface | REPOSITORY PATTERN | §3.3 items 1-6; A5a H, A5b H [READER]; `cast.py:1-15` counts keys present, not values (§3.1) [CHECKED] | No code reads the contradicted facts (TS, Standing, flaws), so they are inert at runtime | the data code reads is thin: stats 1, goals 17, affiliations 0 of 46 [CHECKED parse] | IN-64 (B-X) authors vectors; IN-38 overlays (B-V) | SOUND |
| T-NPC-13 | A person's acts record that something happened, not what he meant: an OUGHT's predicate is unread, a declared intent is never reconciled, act-minted propositions are empty | REPOSITORY PATTERN | H-185 (`hole_register.yaml:4162-4168`), H-191 (`:4240-4246`) [CHECKED]; 52 of 52 act-minted Propositions with an empty predicate, one uncommitted seed (`proposals/2026-10-13-narration-mechanisms.md:38-52`) [AUDIT T5]. **Two** | Tellings carry a `Said` with a predicate (the audit's counter-example) | built and inert (the predicate field exists, nothing reads it) | H-185 and H-191 in no plan position (BASELINE B4) | SOUND for the rows · UNVERIFIED for the datum |
| T-NPC-14 | Who holds an office is separate from who controls the holder (X1) | CONVERGENCE (as claimed) | Kremlin, CK contracts, Ming *piaoni*, Byzantine Office vs Dignity, Venetian rectors (COMP-2 X1; R4 T) [READER] | three of the five rows are historical and two run in opposite directions (R4 K10) [READER] | `hold` and `oblige` separate since IN-40; no controller relation | IN-48 delegation (B-JR, unscheduled) | OVER-CLAIMED |
| T-NPC-15 | No game ships an NPC acting on knowingly false political information (N-9) | NULL (as claimed) | PRE N-9 (R8 T1) [READER] | Talk of the Town's fallibility model contradicts it (R8 K12) [READER]. In Valoria a held claim can go stale, and the default read is stale (ENP v2 `04_PROVENANCE.md:166`) [CHECKED], but every deposit's value is the engine's resolution [AUDIT A9] and a teller never lies (H-198) | stale beliefs execute; lies absent | IN-18 G7 (H-198) BLK | CONTRADICTED (as a null); in code only half-occupied |
| T-NPC-16 | A person's usefulness feeds his disloyalty: the agent who produces for you accumulates the means to leave (split from T-NPC-1) | CONVERGENCE (one producer) | 13G B4: Imperator's power base is "usefulness and threat as one number", `[U]` in that fused form (L194); C3 delegate as defection vector, Rome II, Imperator, RTK, `[R]` (L208) [CHECKED]. **One producer**, three titles. COMP's X3 "idleness punished" (R4 T) [READER] runs the other way (an unused man drifts); RTP's "each rise carries its own characteristic fall" (R7 T) [READER] matches the term, not the concept | 13G itself marks B4 `[U]`, unique in its fused form | absent: nothing reads a seat-holder's holdings against his loyalty (`data/cast.py:256-332`) [CHECKED] | none | UNVERIFIED (one producer; M-NPC-11 grades the demand WEAK accordingly) |

### 7.2 Conflicts inside the lane, and where code or plan contradicts a throughline

1. **Two referents for one quantity (T-NPC-1).** Loyalty is a row toward the leader at build; the defeat bleed, whose own
   docstring says it "FOLLOW[S] THE SEEDED-LOYALTY SHAPE" (`loop/effects_combat.py:203`) [CHECKED], writes toward the
   faction proposition, and is unreached because no field is fought (`requirements.yaml:1124-1125`). The code disagrees
   with itself on the referent; the motion precedent describes reaches shipped play only as regard at read
   (`fixtures.py:741-750`), which needs no stored row to move.
2. **The plan's newest loyalty reader inherits the static value (T-NPC-1).** IN-69's EXIT names persons by measured loyalty
   ("NPC-033 25, NPC-052 43 …", `_part5:313`) [CHECKED]; those numbers are fixed at world generation, so salience by
   alignment orders the same person the same way in every season unless a pursuit or stance writer moves the vector.
3. **The strongest shape is the most legibility-exposed (T-NPC-2 against T-NPC-8).** Valoria fills the corpus's null with
   belief in transit; TD names that primitive "the one most likely to fail in practice" unless displayed (L529) [CHECKED],
   and the plan schedules no display (IN-47 has no build batch).
4. **A borrowed precedent lost its carrier (T-NPC-6).** SFP's P6 borrowed Pax Pamir's punished switching "in its exact
   shape" (`03_PROPOSALS_POLITICS.md:249`; P6 "absorbed or superseded", `00_INDEX.md:3`) [CHECKED]; IN-11 cut `repudiate`, so a vow-break is now priced at `release`'s
   alignment cells. H-205 (`absent`) is attached by its own `cite:` to Jordan's CELL-VALUE AND COSINE PASS (§J.2,
   `hole_register.yaml:4425`), and that ask-then row lists the doctrine row, NPC-089, `intelligence-diplomatic` and
   `restore`'s cells but not H-205 (`_part5:531`); the plan mentions H-205 once more, as a retired-handle note (m:375)
   [CHECKED].
5. **Kinship against the heir ruling (T-NPC-7).** Precedent couples heir and kin; RS-27 makes the heir a title conferred
   by the King's remit. Both are lawful; they give different games (§10).
6. **Precedent against AX-5 (T-NPC-7, T-NPC-10).** Medieval Dynasty and Banished generate people by pairing; AX-5 admits
   individuation only on a demand an act produced. Births are lawful only as a CENSUS answer to such a demand.

### 7.3 Shared with other lanes

T-NPC-1: FA, MB · T-NPC-2: SC, WR, FI · T-NPC-3: IN, WR · T-NPC-4: PC, MB, SC, IN · T-NPC-5: IN, WR · T-NPC-6: FA, IN, SE ·
T-NPC-7: FA, IN, SE · T-NPC-8: IN, GO · T-NPC-9: WR, FA · T-NPC-10: SE, FA · T-NPC-11: IN · T-NPC-13: IN, WR, FI ·
T-NPC-14: FA, SE · T-NPC-15: SC, FI · T-NPC-16: FA, MB.

### 7.4 What the throughlines do not establish

- **Nothing here measures play.** Every game claim is a folk model: TD calls its non-Pax-Pamir sections "player-facing
  folk models" (L575-577) and 13G "the wrong thing to trust for any specific constant" (L582) (UP03 K10; UP04 K) [READER].
- **Independence is thin.** TD, 13G and 20G are one programme; COMP's three programmes are asserted independent while two
  of its own parts trace the declared precedents to one source (R4 K11). No throughline above has three independent
  game sources.
- **No throughline settles a rate, a referent or a value.** Whether loyalty moves toward the leader, the faction or both,
  and how fast, is design (§10).
- **A precedent convergence is not a demand.** T-NPC-7 rests on D6 alone unless a D1-D4 hook joins it (§8); T-NPC-10 and
  T-NPC-16 do not reach D6's own floor of two independent verified cases.
- **Unread here:** FASE T5 (governor control) and T9 (interregna), RTP's body beyond its head, and the earlier drafts of
  TD and 13G pinned at `04_PROVENANCE.md:130-138`.

## 8. MISSING AREAS

**Verdict.** The game lacks a person who **differs in what he can do**, including as the commander or the troops of a
field army, and a person whose **values and body change unwatched**: the carriers exist or are declared, and no v9
position arms or sources them. Regard and beliefs are not in this gap; they move live (§7.1 T-NPC-5). Next, it lacks the
**acts that bind a person to others across time**: a priced change of sides, recruitment, and a vacancy delivered by
claim to anyone who is not a conferrer; delegation is planned and blocked behind its Layer-1 design. Third, it lacks
**any surface on which a person can be read or made**. Succession, bonds, goals and convictions are planned, not
missing; succession is blocked on an open Jordan item.

### 8.1 Counts

`examined 49 candidates; 36 entered (12 missing, 5 hollow, 5 blocked, 14 planned-unbuilt or built-dark); 13 dropped (one-line reasons in 8.5)`

Walk: (a) the 23 rows of §4; (b) R-04 conjunct 3, R-06, R-07, R-08 and R-09; (c) the lane's hole rows H-49, H-59, H-85,
H-100, H-108, H-128, H-146, H-170, H-180, H-181, H-182, H-185, H-187, H-188, H-190, H-191, H-195, H-198, H-200, H-205,
H-206, H-207 and H-208; (d) NERS A1/T1, A4 (i)-(v) and its datum, A7, A9, T4, T5; (e) T-NPC-1 to T-NPC-16; (f) Jordan's
2026-10-16 statements 1 and 3 (troop quality by equipment, experience and commanders; the 4/4 Line a stub) as they bear on
persons. The first draft walked A4 (ii) and H-170 without placing either; both are now entered (M-NPC-12, M-NPC-13), and
M-NPC-8 moved from MISSING to BLOCKED (B-NPC-5).

### 8.2 MISSING

| ID | area | demand (strength) | code state [CHECKED] | plan state | absence test (run, result) | what its absence does | NERS axis |
|---|---|---|---|---|---|---|---|
| M-NPC-1 | **Per-person capacity magnitudes**: a source for what a person can do (skill, attribute, Thread Sensitivity) beyond one vocation key | D1: R-09's `met` needs "two persons with different `capability` resolving the same contested verb at different pools" (p2:423, BASELINE B2); D1: R-04 conjunct 3's character scale; D5: A1/T1; D6: T-NPC-4. **Strong** | `Person.capability` empty on 429 of 430 corpus persons (`requirements.yaml:74-82`); the registry's `stats` non-null on 1 of 46; `ts` read by no Python file (§3.1) | `train` (IN-12 step 9, B-Q) writes capability only where a case names a vocation, and `copying` is the only key (`_part5:73`); the source is J-13's remainder, J.2 rank 1 (`_part5:504, 514`); K-2 "not ratified" [AUDIT] | `python3 -c` registry parse: `stats` non-null 1, `affiliations` 0 of 46; `grep -n copying engine/season/rosters.yaml` → the only `verb_capability` value (`:1106-1107`) | A duke and a copyist argue, fight and march alike; outcomes vary by seed, not by person | R-VARIETY, R-COMPLETE; S-vertical (nothing about a person crosses into the physics) |
| M-NPC-2 | **A reader's competence**: AX-7's second input to how far a witness's reading diverges | D3: AX-7 names channel, competence and prior belief as the inputs (`loop/witness.py:488`); D4: H-200 `absent` (`hole_register.yaml:4355-4361`). **Strong** | `competence` is the constant 1, "unbuilt (`H-200`)" (`decision/options.py:1205-1209, 1230`) | none: H-200 occurs 0 times in the eight plan files | `grep -o 'H-200\b' workplans/valoria_master_workplan_v9*.md` → 0; `grep -n competence engine/season/decision/options.py` → `:1209` "1, unbuilt" | Every witness of equal stance and channel reads an act equally well; the scholar and the drunk misread alike | R-VARIETY; S-methodology (one input of a three-input rule hard-coded) |
| M-NPC-3 | **A person whose values, capacity and body change in shipped play**: values bending under scars and religious strain, refusals from conscience, age and illness. Regard and beliefs are excluded: they move live (T-NPC-5) | D1: R-06 "convictions, moral values" (`requirements.yaml` R-06 statement); D4: H-188 default "INERT … BY CONSTRUCTION" (`hole_register.yaml:4207`), H-146 "stays unarmed until a ruling" (`_part5:466`), H-208 rates unchosen; D5: A4 (iv), T4. **Strong** | carriers built and shipped at control: `data/fixtures.py:542-544` (age, illness), `:643` scar weight shift 0, `:651` confliction 0, `:661` refusal None; regard and belief gains ship live (`:697`, `:741-750`, `:773`) | no position arms age, illness, confliction or refusal (BASELINE B5); H-208 occurs 0 times in the plan. `scar_weight_shift` is the exception (IN-65, conditional; §8.4) | `grep -o 'H-208\b' workplans/valoria_master_workplan_v9*.md` → 0; `grep -n "age_step=\|confliction_weight=\|refusal_axis=" engine/season/data/fixtures.py` → 0.0, 0, None | Over a campaign nobody grows old, breaks under strain or refuses on principle: a person's values, capacity and unwounded body in season 20 are those of season 0, though his regard for others and his beliefs have moved | R-WORLD (no unwatched change), R-COMPLETE; N bottom-up |
| M-NPC-4 | **What an ambition demands**: the predicate of an authored OUGHT, so a person can see his ambition met or thwarted | D1: R-06 "goals, ambitions"; D4: H-185 `absent`, "nothing planned needs it" (`hole_register.yaml:4162-4168`); D5: A4 (iii), T5. **Strong** | Q4 reads the OUGHT's `subject` and nothing else (H-185 text); IN-66/IN-68 will mint goal OUGHTs of the same shape (`_part5:304`) | none: H-185 occurs 0 times in the plan | `grep -o 'H-185\b' workplans/…v9*.md` → 0 | Ambitions start questions and never end them; nobody achieves anything, so nobody can be satisfied, disappointed or envied for it | R-COMPLETE; C1 (the ambition claim has no carrier for its content) |
| M-NPC-5 | **A change of sides priced as its own deed** | D4: H-205 `absent` (`hole_register.yaml:4415-4426`); D6: Pax Pamir punished switching, T0 rulebook (TD L70-72, L487-491; 13G L110) joined to SFP P6's borrowing (`03_PROPOSALS_POLITICS.md:249`; the file is PROPOSED and held back, and its index records P6 "absorbed or superseded", `00_INDEX.md:3`) [CHECKED]. **Strong** (on D4; the D6 half is one game) | a vow-break is judged at `release`'s alignment cells, since IN-11 cut `repudiate`; `grep -n "deed:commitment" engine/season/rosters.yaml` → 0 | attached by its hole row's `cite:` to an ask-then that omits it: H-205 names Jordan's CELL-VALUE AND COSINE PASS, §J.2 (`hole_register.yaml:4425`), whose row does not list it (`_part5:531`); otherwise H-205 appears once, as a retired-handle note (m:375) | the grep above → 0 lines; `grep -n H-205 workplans/valoria_master_workplan_v9*.md` → m:375 only | Betrayal is an ordinary resignation: no witness can tell a turncoat from a man who retired | R-CHOICE (silence beats refusal: the cheap exit dominates); R-WORLD |
| M-NPC-6 | **A vacancy delivered by claim**: the dead seat-holder's office and closed `hold` named in claims, so persons who are not conferrers learn the seat is empty | D4: H-206 `absent`, office half (`hole_register.yaml:4428-4434`); D1: R-07 "imperfect knowledge" (persons must learn the seat is empty). **Medium** | **Delivery to conferrers is built**: `vacancies()` (IN-53, landed `5652e846`) puts every office with no live `hold` into the questions of each person whose `confer`-granting seat passes `may_fill` (`queries/world_q.py:1617-1639`); `remove_person` closes the dead man's holds (`state/world.py:746-751`); H-207 records four seats vacant after season 1, `p_npc_032` passing `may_fill` into two (`hole_register.yaml:4443`), though `confer` there still fails at its conferee (H-207 cause 4). **Delivery by claim is not**: the holder half landed with IN-34 (`person.died` placed where he stood); no claim names the office or the closed hold, so `seats_named` (`world_q.py:1642-1654`), which reads only the person's own ledger, has nothing to return. The fix "needs `claim_subjects` to expand a departed person's holds and would also move RESOLVE deaths" (H-206) [CHECKED] | H-206 appears once, at p3:213 (the holder half's landing). IN-61's heir learns of the vacant throne "through `seats_named` (a claim naming it), not through `vacancies`" (`_part3:56`), and its FALSIFIER requires that question (`_part5:248`), so IN-61 rests on the same missing claim [CONFIDENCE: medium: IN-61 is design-first and may build it] | `grep -o 'H-206\b' workplans/…v9*.md` → 1 (p3) | A death's seat reaches only those who could confer it; a rival, an heir outside the throne or the faction's members learn of it from no claim, so the scramble for a dead man's office is confined to conferrers whose `confer` does not yet execute (H-207). Deaths are frequent, on three figures from three builds that this pass cannot reduce to one rate: H-206, `build_realm(0)` at the B-F close (2026-10-10), "4 deaths in 2 seasons … RESOLVE-written"; IN-59, a session probe of 2026-10-14, "10 season-0 kills" (`_part5` IN-59); this pass's probe at HEAD `021fd96` (engine and modules unchanged to `f590d00`, `git diff --stat`), shipped fixtures, `populated.run`: 8 of 83 removed in one season at seed 0, 12 in two seasons at seed 0 and 11 at seed 1, all caused by acts (no MATTER death), with four of the six heads gone after one season and five after two at both seeds [MEASURED this pass; scratch, uncommitted, two seeds, no control arm on deaths]. The plan index lists B-I, B-J and B-W as closed after B-F (`valoria_master_workplan_v9.md:235`; B-W's close `3bf936ee` is dated 2026-10-14, the others are outside this shallow clone), so the builds differ in output-moving code; the rise is plausible, not explained | S-DOWN (published to conferrers only); R-WORLD |
| M-NPC-7 | **The character surface**: creation, development and chronicle a player can read and act on | D1: R-04 conjunct 3, the `scales:` row "character creation / development / chronicling", `in_loop: false` (`requirements.yaml:71-82`); D5: A2; D6: T-NPC-8 (N-2, Nemesis, TD L529). **Strong** | creation: "no act; a cast entry the world-gen builder seats"; chronicle: no field (`_part4:41`) | IN-47 design landed, "no build batch" (`_part4:39-40`); IN-37 BLK (B-U); "R-04, hence M1, cannot read `met` … until a build batch exists for both IN-46 and IN-47" (p2:209) | `grep -n "no build batch" workplans/valoria_master_workplan_v9_part4.md` → IN-46, IN-47 | The richest person model in the bin cannot be seen or chosen; belief in transit (T-NPC-2) is invisible, which TD names as its failure condition | E-LEGIBILITY; S-vertical (no seam from person to player) |
| M-NPC-9 | **Whether a declared intent was kept** | D4: H-191 `absent` (`hole_register.yaml:4240-4246`); D1: R-07 "attitudes … imperfect knowledge" (trust from promises kept). **Medium** | "ABSENT: H-191 intent reconciliation" marker (`decision/options.py:1295`); intents are told at rate 0 (`fixtures.py:736`) | none: H-191 occurs 0 times in the plan | `grep -o 'H-191\b' workplans/…v9*.md` → 0 | A promise costs nothing to break and earns nothing kept; reputation for keeping one's word cannot form | R-WORLD; C3 (nobody can evaluate the promise) |
| M-NPC-10 | **Recruitment**: an act by which a head or household brings a person in, with rivals competing for the same people | D6 only: 13G C6 recruitment as negotiation [R] (L212), TD "Nobody is a rival for the same people" (L474). **WEAK DEMAND** | membership is the person's own `commit` (always refused in the corpus at B-W, BASELINE B3); no recruiter's act | IN-68 seeds commits at world-gen; FA-05 "user goals; commit"; no recruiting act | `grep -rn -i recruit engine/season --include=*.py` (outside tests) → 0 | Factions cannot grow by persuasion; their membership is fixed at world generation plus each person's own drift | R-CHOICE at a head's seat |
| M-NPC-11 | **Usefulness breeds threat**: a seat-holder's power raising his danger to the one who seated him | D6 only: 13G B4, C3 (L194, L208); RTP B§1 (R7 T) [READER]. **WEAK DEMAND** | loyalty is computed once from authored vectors (`data/cast.py:256-332`); nothing reads a seat-holder's holdings against his loyalty | none | `grep -n "power_base" engine/season/rosters.yaml` → 0 (the roster was deleted unread, H-100) | Elevating a subordinate is free; the principal-agent tension the genre runs on is absent | R-CHOICE (no cost to a dominant act) |

### 8.3 HOLLOW and BLOCKED

| ID | position | stated EXIT (quoted) | the demand it does not deliver |
|---|---|---|---|
| H-NPC-1 HOLLOW | IN-12 step 9 `train` (B-Q) | "`train` forms and writes `Person.capability` only where a case names a vocation, and `pool_default` holds everywhere else, so R-09's by-person pool stays PARTIAL" (`_part5:73`) | R-09's by-person conjunct (M-NPC-1); the plan says so itself |
| H-NPC-2 HOLLOW | IN-31 revocation cost (B, B-Q) | appointed → permanent `ban`, keyed on the seat's `conferral` (`proposals/2026-10-14-in31-revocation-cost-provenance.md:146`; §2.2) | H-100's demand that cost follow how the seat was won; the proposal's residue R3 concedes it |
| H-NPC-3 HOLLOW | IN-58 grievance (stance-only half landed) | "HASH EQUAL at the shipped `legacy` … so the entry's EXIT 'hash MOVED' is NOT MET" (`_part5:225`) | R-07 attitudes reaching choice: stance turns a witness hostile only under the non-shipped `declared` arm (0 of 12 realm pairs at `legacy`) |
| H-NPC-4 HOLLOW (weak demand) | IN-69 salience by alignment; IN-70 opinion of a faction | IN-69: persons below indifference "answer their own want first" (`_part5:313`); IN-70: Opinion(p, F) = alignment + affiliation + regard of F's head (`_part5:325`) | T-NPC-1's moving loyalty: the alignment term is fixed at world generation, so only the regard term can move |
| H-NPC-5 HOLLOW [CONFIDENCE: medium] | IN-59 access gate (B-Y) | measured 0 of 10 season-0 kills co-located; the regicide reading places "the King … at `b_s_002_cottage`" (`_part5` IN-59) | an access gate whose premise is where leaders live: `npcs.yaml` houses five of six heads off-seat (§3.3 item 1) |
| B-NPC-1 BLOCKED | IN-61 succession (B-R) | "a death followed by the title-holder's `succeed` claim opening the throne's hold" (`_part5:248`) | behind ED-IN-0292 (2) (J, pending `needs_jordan`) and SC-04 (B-P) (`_part5:245`). Until it lands, a headless faction stays headless: the probe above kills five of six heads in two seasons, and `faction_leaders` is a static roster (`rosters.yaml:1467`) |
| B-NPC-2 BLOCKED | SE-06 cohort pursuits and convictions; SE-04 (c) spread | SE-06 J, ask-then at B-X's close (ED-IN-0296); SE-04 (c) HELD (BASELINE B1.2) | R-06 for 37 of 83 persons: cohorts choose by "urgency, a constant stance term and the draw" (`_part6` SE-06); cohorts cannot `commit`, so cannot be mustered, and die whole [AUDIT A7, E watchlist] |
| B-NPC-3 BLOCKED | H-146 `refusal_axis` | "stays unarmed until a ruling" (`_part5:466`) | ED-IN-0261's ruled deontological refusal (M-NPC-3) |
| B-NPC-4 BLOCKED | J-13's remainder | J.2 rank 1, "Where do per-person `capability` magnitudes come from once the interim runs out?" (`_part5:514`) | M-NPC-1 |

### 8.4 PLANNED-UNBUILT and BUILT-DARK

| area | state | what arms or builds it | locator |
|---|---|---|---|
| 15 pursuits + 3 convictions on every cast Person | planned (B) | IN-64, B-X | `_part5:267` |
| goals carrier, referents, seeding; user and organization goals | planned (B) | IN-66, IN-67, IN-68, FA-05, FA-06, B-X | `_part5:288-302`; `_part7:143-150` |
| inclination breaks a tie (R-08) | planned (B) | IN-62 … IN-65, IN-71, B-X | p2:382; `_part5:253-281` |
| a death or wound claim reaching attention | planned (B) | IN-72, B-X | `_part5:316` |
| bonds: `tie / knot` (P-12's knots, H-182) | planned (BLK) | IN-32, B-S | m:264 |
| a grudge ends: `forgive` (H-59) | planned (BLK) | IN-12 step 13, B-Q | `_part5:61-80` |
| deception: a teller lies (H-198) | planned (BLK) | IN-18 G7 | m:257 |
| NPC overlays at scale | planned (B, answered [medium]) | IN-38, B-V | `_part5:183-188` |
| foreign faction as persons; guard cohorts | planned (BLK) | IN-36, B-V | m:267 |
| scar weight shift (H-187) | built dark | IN-65 builds a floor "ONLY IF H-187's shipped shift is above 0" | `fixtures.py:643`; `_part5:283-286` |
| stance reaching candidates (`stance_polarity`, H-194) | built dark | ask-then at B-X close (ED-IN-0296) | `fixtures.py:759`; `_part5:540` |
| actor scarred by own act (H-128) | built dark | none | `fixtures.py:631` |
| a telling made in confidence (H-197) | built dark | none; G6 break path unreached (H-204) | `fixtures.py:789` |
| a field's loyalty moving morale (MB-03) | built dark | none | `fixtures.py:608` |

### 8.5 Dropped

1. **Standing / rank ladder** (RTP, Skyrim, RoTK): covered by seats and `confer`; SFP records "there is no Standing to reset" (`03_PROPOSALS_POLITICS.md:252`) [CHECKED]; D6 alone.
2. **Companions and Disposition**: quarantined design with GM rulings; no D1-D4 source.
3. **Priority trees, Leadership Deviation, Resonant Style, per-NPC flaws and Event cards**: superseded in substance by the decision layer (§3.2); FA-07's LEAVE row records Deviation.
4. **A defection roll** (Spirit vs Disposition): the design contradicts itself (§3.3 item 5); M-NPC-5 covers the act.
5. **`urgency`**: a false N-line (the audit, report §5); no demand for the term.
6. **An outcome evaluator reading odds, cost or capability** (A4 (v)): the audit itself declines it as a fix that adds a system; no demand source.
7. **The candidate-formation datum** (33% wrong-kind subjects): one uncommitted seed; UNVERIFIED until re-read with `harness/aperture` (audit G9).
8. **The actor's own fallible self-reading** (A9): AX-7 (2) says self-understanding *may* be wrong, which permits and does not require a mechanism (audit G6).
9. **Kinship as a relation distinct from ties**: R-07's relationships are carried by IN-32's `tie / knot`; whether kin is a tie kind is a design option (K-NPC-6), not a missing area.
10. **Births and new persons**: CENSUS individuates on a demand an act raised (`loop/census.py:14-17`) [CHECKED]; demographic birth is SE's (p8:134).
11. **H-180, H-181, H-195** (a teller's stake, rank ordering, the `holder` operand): telling-lane rows, SC/SE.
12. **Key-substrate designs** (RTP §3.4, compendium Part 40, ripple substrate): retired (ED-IN-0232).
13. **A spawner on a clock**: refused by AX-5 and honoured (`generate_npc` has no production caller, A5b H).

## 9. NERS PASS

`[SELF-AUTHORED — bias risk: this pass audits a lane file written earlier in this session.]` Target: the person as code
plus v9 with every position assumed built (the uploaded audit's assumption); the shipped state is recorded where it
differs. **Instruments: A.** The chooser's Gumbel draw is the lane's only draw; `resolution-diagnostic` was not run.
**Executed:** `python -m engine.season.harness.register --requirements` (met 3 · not_met 1 · partial 5; R-06, R-07,
R-08, R-09 partial) and a scratch probe, `scratchpad/work/npc_change_probe.py` (shipped fixtures, `populated.run`, seeds
0 and 1, two seasons), which observes change, since scar counts moved on 34 persons, and found: 0 persons with
`capability`, no change to any `pursuits` or `conviction`, the 32 stance rows toward faction heads unchanged, **no
stance row appended at all**, 11-12 deaths including five of six heads, and nobody individuated. Not run: `corpus_run`,
`aperture 4 0`, any pytest file, the audit's own probes.

### 9.1 N-line ledger

| object | N-line (restated narrowly where narrowed) | attack run | result · direction |
|---|---|---|---|
| Claim ledger with `seen.who`, source and chain | Cut it and a person can neither be wrong about a deed nor learn it second-hand, so grievance by witness and belief in transit die (R-07) | Could stance rows carry it? A stance row `('p_npc_003', 1, 4)` [probe] has no date, source or truth value; it cannot be told, refuted or stale | **HOLDS** · bottom-up, lateral, horizontal. Vertical narrowed: a death reaches seat questions only for the holder half (H-206) |
| Pursuit term of the score (`choose.py:403-406`) | Cut it and two persons in one seat choose alike, since stance is constant over candidates on plain referents at `legacy` [AUDIT A4] and capacities are equal (T-NPC-4) | Does stance or seat differentiate without it? Only through classed referents and remit | **HOLDS** · bottom-up; top-down once IN-69 orders goals by alignment |
| `cast.loyalty` seed row | Narrowed: cut it and a witness of a head's death judges the killer with no allegiance to the dead man, because `deeds_judged`'s `_bond` reads the stored stance (`_part5:226`) | Is the cosine carried elsewhere? IN-69 moves it to `alignment`, so the **ordering** survives the cut (false in that direction); the stored row's grievance role does not | **HOLDS, NARROWED** · bottom-up only; in shipped play it reaches no choice (hash EQUAL at `legacy`, `_part5:225`) |
| Scar count | Armed: cut it and a person who keeps seeing his values violated never bends | Shipped: the probe moved scar on 34 persons and nothing else; `scar_weight_shift` is 0 | **NOT SCORABLE** until H-187's value: a store with a producer and no live consumer is paper |
| Convictions and doctrine pull (IN-64, IN-71) | Cut them and faith stops pulling persons, so a schism cannot run through a household | `confliction_weight` (damping) is dark with no arming position; IN-71's pull is a different term | **HOLDS** for IN-71 (assumed built) · lateral; confliction NOT SCORABLE |
| `faction_leaders` + ED-IN-0201 gate | Cut it and a faction acts as a gauge, against AX-1 | Probe: five of six heads die in two seasons; the creed OUGHT is subject-ed on the head (`harness/populated.py:751-752`) and immutable | **HOLDS**, and breaks at its extreme (R-COMPLETE): a dead head leaves the creed naming a dead man until IN-61 |
| `succeed` / heir title (IN-61, assumed built) | Cut it and the throne cannot be filled after the King dies: its own FALSIFIER refuses a regent's `confer` (`_part5:248`) | Can `confer` fill it? Not under IN-61's own falsifier | **HOLDS, NARROWED** · vertical; throne only (M-NPC-6) |
| `tie / knot` (IN-32, assumed built) | Cut it and P-12's knot-borne drift has no path between persons | Stance rows are one-way and carry no partner operand (H-182) | **HOLDS** · lateral, diagonal (person → threadwork) |
| Goals (IN-66…IN-69) | Cut them and every faction's members answer one shared OUGHT ("one shared OUGHT per world", `requirements.yaml` R-06 `measured:`, BASELINE B2) | Pursuits differ, but questions come from OUGHT commits | **HOLDS** · top-down |
| `forgive` (IN-12 step 13) | Narrowed: cut it and a grudge ends only by **eviction** (`ledger_cap`, confidence × recency), which "nobody can witness" (`loop/witness.py:868-878`; `queries/world_q.py:1988-1990`) [CHECKED] | The possibility "a grudge ends" survives the cut via eviction; what dies is a **witnessed, chosen** ending | **HOLDS, NARROWED** · lateral (R-CHOICE: see 9.4) |
| `urgency`; `benefits_me` | — | the audit's attack (report §5): `urgency` constant over candidates; `benefits_me` no caller [AUDIT, `choose.py:150-193` CHECKED] | **FALSE N-LINE** (`urgency`, disqualifier 5); `benefits_me` unscheduled, not free |

### 9.2 False N-lines and the five checks

- **False:** `urgency` (re-opened, `choose.py:185`); `cast.loyalty` as an **ordering** input once IN-69's `alignment`
  exists (disqualifier 1: the carrier exists). Not false: the stored seed row (grievance).
- **C1 (claim → mechanism).** "Characters … with goals, ambitions" (R-06): an ambition's content has no carrier (H-185,
  M-NPC-4). "Loyalty 0-100": carried at build only. **C2.** `deeds_judged` judges only `PAIRED_KINDS` (death, wound,
  undecided contest; `_part5:226`), so being revoked or passed over cannot be judged as a wrong done to oneself; the
  type does not admit the input T-NPC-1 needs. **C3.** Opinion of a faction is evaluated at read from the reader's own
  claims (IN-70, "nothing stored") — PASS. **C4.** `effects_combat.py:203` says the defeat rows follow the loyalty
  shape while writing a different referent (§7.2 item 1). **C5.** Showcase "the King dies and the heir claims": shipped
  objects exist for the death (fight), the holder half of the vacancy (H-206) and `off_heir`; the claim (`succeed`),
  the throne's `inheritance` basis and the heir's question are planned (IN-61) → **expressible, not implementable**
  until B-R.

### 9.3 E (scored last, against N and R)

- **E-OVERHEAD: FINDINGS.** `Person` has 12 fields (`state/carriers.py:645-676`); in shipped play 2 differ between
  persons beyond identity and place (`pursuits`, `stance`), `capability` is empty, and `scar` accrues without a reader.
  Nine person-level knobs ship dark (§8.4, M-NPC-3); four person carriers are inert (`benefits_me`, `urgency`, the OUGHT
  predicate, `competence = 1`). v9 adds goals.yaml with two rosters, a `successions` registry and an opinion query, and
  deletes nothing in this lane. The vocabulary is larger than the behaviour (T4). The shape is small because capacity
  and change were amputated, not because it was distilled.
- **E-LEGIBILITY: FINDINGS.** The pursuit → act path runs through 15 pursuits × 7 axes onto 45 verbs [AUDIT]; no surface
  shows any of it (M-NPC-7). A player cannot predict who will betray whom.
- **Watchlist.** Cohort as one Person at weight: kept, MEDIUM (it cannot dissent, be mustered or die in part [AUDIT]).
  Loyalty as a cosine of authored vectors: kept, LOW (the only allegiance seed; its cost is that it cannot move).
  Conviction as religious affiliation only (STR-6): kept, MEDIUM (the thirteen-value moral roster's depth is folded into
  pursuits, ED-IN-0261).

### 9.4 R

- **Seats.** The player is an ordinary Person (IN-47: development is "the player's own `View`/`Question`/`Candidate`,
  acting into the chooser slot", `_part4:41`); which seats a campaign offers at start is not ruled. Favourable R-CHOICE
  findings are PROVISIONAL.
- **R-CHOICE.** `SEAT: a faction head` · `INTENT: be rid of a subordinate`:

  | act | gain | cost |
  |---|---|---|
  | `revoke` | the seat | never executes in the realm (H-207); IN-31 assumed built: `ban` for an appointed seat |
  | `fight` | the man and his seat | a deed judged at read by witnesses, reaching choice only under `declared` (hash EQUAL at `legacy`) |

  Shipped: **`fight` dominates strictly** (the probe's deaths are its trace). Assumed built: IN-59 adds an access gate
  and IN-70 turns grievance into faction-level referents; dominance is then an act-economy question (IN-14 ask-then).
  `SEAT: any member` · `INTENT: end a grudge`: let it be evicted (silent, no event) vs `forgive` (witnessed). **Silence
  beats refusal**: eviction dominates unless `forgive` buys something eviction does not. Upper bounds only.
- **R-VARIETY: FINDINGS** — one capacity profile for all (T-NPC-4). **R-WORLD: FINDINGS** — the world emits deaths
  unwatched (probe), but nothing follows them except the throne's planned claim: no vacancy (M-NPC-6), no birth, no
  promotion. **R-COMPLETE: FINDINGS** — the leader object breaks at its extreme (dead heads, immutable creed);
  ambitions have no completion (M-NPC-4).

### 9.5 S

- **S-UP: FAIL** — a member's want reaches his head through no accountable carrier; the petition path is addressed to
  its own subject [AUDIT A5]. **S-DOWN: FAIL for vacancies** (unpublished, H-206); PASS in shape for tellings [AUDIT].
- **Coverage.** Vertical: person → office (holder half only), person → combat and mass battle (no capacity crosses,
  T-NPC-4; cohorts cannot muster [AUDIT A7]). Diagonal: person → threadwork (TS has no carrier, H-85; PC-06 K-3 planned).
  Lateral: telling (built), ties (planned). Horizontal: frozen deliberation (the audit's N-line holds).
- **Pauses correctly: FINDINGS** — a headless faction does not yield: its creed keeps a dead referent and the season
  ticks on. **Methodology: FINDINGS (shipped) → planned PASS** — allegiance has three scales: loyalty 0-100, a stance
  row of ±25 (`STANCE_MAX`), opinion in [−1, 1]; IN-70 normalises "one ladder per quantity" (`_part5:325`).

### 9.6 The design's own falsifier

Discipline: *a person-level value nobody authored is not invented* (`harness/populated.py:394-395`; `massbattle.py`
"not the place to invent one" [AUDIT]). Hits: loyalty against a role template — **settled, licensed by ruling**
(`cast.py:256`); cohort weight 2, "a number nobody chose" (H-170) — clean, fixture family; `age_at_build = 0` for all
(`fixtures.py:544`) — clean, fixture; `pool_default` / `obstacle_default` 2 — clean, fixture; residence derived by
first-hit parse, "reordering MOVES PEOPLE" (B1a F) [READER] — clean, a second family; full `body` at build —
borderline. **HITS, two families:** fixture constants standing where an authored person value should be (the audit's
family), and **person facts derived by parsing prose** (residence), which the exception list does not name.

### 9.7 Self-audit and verdict

9a: the Pax Pamir correction reached §0 #8, §2.1, §4, §5 and §7.2; the probe's deaths were carried into M-NPC-6,
B-NPC-1 and 9.4. §0 #6 (leaders mis-housed) stands, but the probe shows the housing matters less than the deaths.
9b: this pass adds no object; the probe is scratch. An independent reviewer would add a corpus-level death count, a
check of whether ED-IN-0201's gate silences a headless faction, and squad-engagement Parts A-D.

| axis / test | verdict | what would overturn it |
|---|---|---|
| N (six directions) | FINDINGS: narrowed (loyalty, scar, forgive, succession); false: `urgency`, loyalty-as-ordering | a cut whose loss survives, e.g. eviction carrying a chosen, witnessed ending |
| E-OVERHEAD | FINDINGS | nine dark knobs each guarding a ruled-in behaviour |
| E-LEGIBILITY | FINDINGS | a surface showing a person's pursuits and allegiances |
| R-COMPLETE | FINDINGS | a successor for every dead head; an ambition's predicate read |
| R-VARIETY | FINDINGS | two persons in one seat with different capacity resolving one verb differently |
| R-WORLD | FINDINGS | an unwatched death followed by a vacancy contest |
| R-CHOICE | FINDINGS (shipped, upper bound); NOT SCORABLE assumed built (act economy, IN-14) | `revoke` executing with a cost below `fight`'s |
| S-UP / S-DOWN | FAIL / FAIL (vacancy) | a member's demand carried to his head; a vacancy published |
| S — coverage · pause · methodology | FINDINGS | a capacity crossing the combat seam; a headless faction yielding |
| own falsifier | HITS (fixtures; parsed facts) | an authored source for each fixture value |
| self-audit | both sweeps run | — |

REPAIRS (worst first, each a deletion or one object): rule a source for capacities (one field, one reader) → M-NPC-1;
publish a vacancy as a claim at the seat (one emission) → M-NPC-6; arm or delete each dark person knob → M-NPC-3; give
a vow-break its own deed cell (one cell) → M-NPC-5; re-subject the creed when its head dies (IN-61's claim, or the
seat rather than the man) → 9.1.

**GRADE: paper** for the v9-built shape. One execution artifact covers the shipped state: the scratch probe, two seeds,
uncommitted.

## 10. KEY RECOMMENDATIONS

This is an audit-design pass over six months of repository work. Jordan, 2026-10-16: it "gets permission to be whatever
it is". The recommendations below are this pass's output; none is entered in the plan or a ledger until Jordan so rules.
Every K row's lane is IN unless it says otherwise; NPC has no ED lane.

### 10.0 The top five, worst problem first

1. **K-NPC-3** — deaths are the world's most frequent unwatched event (five of six heads in two seasons, probe), and
   outside the throne nothing follows one.
2. **K-NPC-4** — a faction's creed names its head as a man, so a regicide leaves every member answering to a corpse.
3. **K-NPC-1** — persons differ in wants only, so every seat resolves by seed.
4. **K-NPC-2** — nobody changes over a campaign; the mechanisms exist and ship off.
5. **K-NPC-11** — none of this can be seen or chosen by a player.

### 10.1 PRIMITIVES

| ID | recommendation | grounded in | §0 ladder | adds / cuts | falsifier |
|---|---|---|---|---|---|
| K-NPC-1 | Give every person a capacity profile from one ruled source, read by the contest pool, the combat `Combatant` and the witness's competence. | M-NPC-1, M-NPC-2, T-NPC-4 (code, CHECKED); NERS A1/T1 [AUDIT] | **Jordan**: survives all five, since persons who differ in capacity and persons who differ only in wants are different games, and K-2 is "not ratified" (audit G1, the same item) | adds one field with three readers; cuts `pool_default`/`obstacle_default` as stand-ins, `competence = 1`, and the registry's unread `stats`/`ts` keys (sourced or deleted) | two persons differing only in authored capacity resolve one contested verb at different degree distributions over the same seeds; equal capacities reproduce `content_hash` |
| K-NPC-6 | Rule whether kin is a kind of tie that a conferral basis can read, or whether the heir stays a title only. | T-NPC-7 (D6, two programmes); R-07 "relationships" (D1); RS-27 | **Jordan**: a dynastic game (kin locks loyalty, heirs by blood, GK2/CK2) and a title game (RS-27) are both lawful under AX-5 and materially different | adds at most one tie kind under IN-32; cuts nothing; the "title only" answer adds nothing | under a kin kind, a seeded heir's claim reads the kin tie and a non-kin claimant is refused; under "title only", no kin field exists anywhere |

### 10.2 VERBS

| ID | recommendation | grounded in | §0 ladder | adds / cuts | falsifier |
|---|---|---|---|---|---|
| K-NPC-5 | Give breaking a vow its own deed, so a witnessed change of sides reads as betrayal, not as a resignation. | M-NPC-5, H-205 (D4); Pax Pamir T0 via TD/13G (CHECKED) | **takeable**, step 3/4: the IN-11 entry said the pricing "becomes a `deed:commitment.ended` cell" (H-205 `cite:`), on the precedent of the two authored `deed:` cell pairs (RS-29). Values `[OPEN — Jordan tuning]` | adds one cell pair; cuts the mapping of `commitment.ended` onto `release` | a witness of a vow-break and a witness of a plain `release` judge different valences; with the cell set to `release`'s values the hash is unchanged |
| K-NPC-8 | Let a seat-holder confer a deputy's seat over his domain, so a lord's reach exceeds his own scenes and a steward can betray a trust. | M-NPC-8, H-108 (D4); 13G C2-C3 (CHECKED) | **takeable**, step 3: B-JR names the route ("`establish` a second seat … `confer` it … a new `tenure_kinds` member is NOT licensed", p3:276) and needs only a batch. Lane FA/IN | adds no kind (uses `establish` + `confer`); cuts nothing | a deputy's act executes with `Act.via` set to the second seat; revoking the deputy ends his acts that season |

### 10.3 MECHANICS

| ID | recommendation | grounded in | §0 ladder | adds / cuts | falsifier |
|---|---|---|---|---|---|
| K-NPC-2 | Arm or delete each person-change mechanism (scar weight shift, religious strain, conscience refusal, age, illness): none ships dark without a position that will arm it. | M-NPC-3, T-NPC-5 (CHECKED); A4 (iv) [AUDIT] | **takeable for the form**, step 3: ED-IN-0261 rules the scar thresholds and the refusal, so arming is the answer and deletion would overwrite it; age and illness rates are H-208's. Values `[OPEN — Jordan tuning]` | adds nothing; cuts each knob that is not armed, with its hole row | a four-season realm run in which some person's pursuit weights differ from season 0, with the hash moved and declared |
| K-NPC-3 | Make a seat-holder's death publish his vacancy at the seat, so every person who could claim or confer it receives a question naming it. | M-NPC-6, H-206 (D4); probe (MEASURED this pass); T-NPC-6 | **takeable**, step 4: IN-34 already places `person.died` where the man stood, and IN-61's FALSIFIER already demands the throne's version (`_part5:248`) | adds one emission at death; cuts IN-61's throne-only special case (scripting drift) by generalizing it | after a seeded kill of a seat-holder, at least one person at that seat's rung holds a claim naming the vacant office; no such claim exists while the holder lives |
| K-NPC-4 | Decide whether a faction's creed binds to its head as a man or to the head's seat, so that a regicide is either a schism or a vacancy. | 9.1 faction_leaders row; `harness/populated.py:751-752` (CHECKED); probe | **Jordan**: Jordan ruled the creed an OUGHT (2026-09-13); the code subjects it on the leader because a faction name is no entity (`rosters.yaml` faction_leaders note, :1475-1483). Binding it to the seat turns personal loyalty into institutional loyalty, and the two give different games | adds nothing (one subject re-pointed); cuts the dead-referent state | after a head's death, no member's Q4 question names a dead id |
| K-NPC-7 | Judge being revoked, passed over or bound as a deed done to oneself, at the same `deeds_judged` owner, so allegiance to a head moves with what he does to you. | T-NPC-1 (three sources); C2 finding in 9.2; H-NPC-4 | **takeable**, step 5: one owner, computed at read, nothing stored (IN-70's own T-a falsifier); the magnitudes are `[OPEN — Jordan tuning]` | adds kinds to `PAIRED_KINDS`; cuts the static seed row's role as the only allegiance input (the row stays as a seed) | a person whose seat his head revokes reads lower regard toward that head next season than a matched control; equal otherwise |
| K-NPC-12 | Require co-location for `fight`, so killing a head costs access and removing a subordinate through his office can compete with killing him. | 9.4 R-CHOICE (shipped dominance); probe; H-207 | **takeable**, step 3: IN-59 and RS-26 rule the access gate; only its batch (B-Y) is pending | adds nothing beyond IN-59; cuts the free remote kill | the probe's two-season death count falls, and no kill occurs between persons in different places |

### 10.4 TEXTURE

| ID | recommendation | grounded in | §0 ladder | adds / cuts | falsifier |
|---|---|---|---|---|---|
| K-NPC-9 | Read an ambition's predicate, so ambitions are achieved, thwarted and envied rather than raised forever. | M-NPC-4, H-185 (D4); T-NPC-13 | **takeable**, step 5: a reader for a field that exists, and IN-66's goals mint OUGHTs of the same shape (`_part5:304`) | adds one reader at Q4; cuts the dead predicate if not read | a person whose OUGHT's predicate holds in his own claims stops receiving its `need` question; a control whose predicate fails keeps it |
| K-NPC-10 | Let a hearer learn whether a told intent was kept, so persons earn a reputation for their word. | M-NPC-9, H-191 (D4); `intent_disclosure` dark | **takeable**, step 5, for the reader; the disclosure rate is H-190's, `[OPEN — Jordan tuning]` | adds one reconciliation at read; cuts the "ABSENT: H-191" marker (`options.py:1295`) | at a nonzero disclosure rate, two hearers of one intent, one of whom witnesses it broken, read different regard toward the teller |

### 10.5 SURFACE

| ID | recommendation | grounded in | §0 ladder | adds / cuts | falsifier |
|---|---|---|---|---|---|
| K-NPC-11 | Build the character sheet as a view of a person's pursuits, allegiances, ties, scars and witnessed deeds, read only from what he holds, with creation choosing a cast seat. | M-NPC-7; T-NPC-8 (three sources); R-04 conjunct 3 (D1) | **takeable**, step 3: IN-47's design landed and "PASSES WITH CORRECTIONS" (`_part4:41`); only a build batch is missing (p2:209) | adds a view, not state; cuts nothing | R-04's `scales:` row reads `in_loop: true` with an artifact; the view changes when the ledger changes and never shows a claim the person does not hold (AX-2) |

## 11. METHOD NOTE (sections 7-10)

**Opened myself.** `skills/ners/SKILL.md`; the three uploads 13G (`b42377f7`: L15-37, L80-150, L174-216, L252-278,
L300-352, L462-479, L545-556), TD (`3cb2a6c8`: L59-72, L164-223, L351-356, L467-491, L529-547) and 20G (`6039edcc`:
L134-146, L164-236, L241), N2 (`773bbfde`: L262-271, L311-321, L498-504, L613-625) and the NERS audit (report
l.40-162, 205-262, 324-444). In the tree: `decision/choose.py:150-193, 400-412`, `loop/witness.py:488-495, 868-878`,
`loop/effects_combat.py:203, 241-260`, `data/fixtures.py` knob lines, `data/cast.py:217-344`, `state/carriers.py:640-676`,
`state/world.py:735-751`, `harness/populated.py:328-395, 732-760, 1313-1330`, `queries/world_q.py:1984-1992`,
`decision/options.py:1205-1230, 1295`, `verb_table.yaml:886-916, 1186-1198`, `rosters.yaml:1100-1107, 1460-1475`,
`requirements.yaml:60-82`, hole rows H-85, H-108, H-128, H-146, H-170, H-185, H-187, H-190, H-191, H-195, H-200,
H-205-H-208, `01_AXIOMS.md:164-198`, `canon/02_canon_constraints.md` P-04, P-12, P-15, GD-1..3, plan entries IN-47,
IN-58, IN-61, IN-69, IN-70, IN-12 step 9, J-13, B-JR, SFP `03:240-262` and `00_INDEX.md:3`, ENP v2 `04_PROVENANCE.md:155-175`,
VCD Guild lines. Ran: the register (above); the scratch probe at seeds 0 and 1 (two seasons, and one season at seed
0); greps and counts quoted in §8.

**Taken, not re-opened.** Sections 1-6 of this file; extractions R4, R7, R8, A5a/A5b, UP03, UP04, UP05 for their T, G
and H sections; the audit's A1, A5, A7 and T5 code claims, marked [AUDIT]; BASELINE B1-B5 for plan states and the
dark-knob table.

**Upload corrections applied (step 0).** (1) §4 changing-sides row: SFP *borrowed* Pax Pamir's switching and refused only
the discard; the rule is T0-confirmed in TD and 13G; its carrier `repudiate` was cut, and H-205 prices a vow-break at
`release`'s cells. (2) §2.1 VCD row: The Guild 3 burned the *player's* residence, was switched off on the publisher's
account, and F77's "popularity threshold" is in neither upload. (3) §4 `forgive` row: The Guild 3 marked as a negative
case. (4) §0 #8 extended to the VCD misstatement. (5) §5: the surveys still absent are named; the four pinned uploads are
recorded as in hand. No §0 ranking changed.

**Could not check.** Whether ED-IN-0201's gate silences a faction after its head dies; the corpus-level death rate
(`corpus_run` not run); FASE T5/T9; the RTP and PMM bodies; the earlier drafts of TD and 13G; IN-65's 61 → 508 figure.
**[CONFIDENCE: medium]** on T-NPC-10 and M-NPC-10/11 (D6-led), on H-NPC-5 (residence premise), and on the probe, which
is scratch and uncommitted, with two seeds and no control arm beyond the scar field showing the instrument sees change.
