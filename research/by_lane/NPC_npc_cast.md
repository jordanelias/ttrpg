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
2. **A person's loyalty value is static**: a cosine of authored values against a role template, ruled "can be invented", computed once at build and written as a stance row toward the faction's leader; nothing writes that row's referent over a season — `engine/season/data/cast.py:256-332`, `harness/populated.py:787, 854-856` [CHECKED]. The stance channel does carry one in-season, Imperator-bleed-shaped term — a lost field battle appends −1.0 rows toward the loser's own faction and the winner, shipped on at weight 1 — but toward the faction proposition, not the leader, so it does not sum into the loyalty row — `loop/effects_combat.py:203-205, 256-261`, `data/fixtures.py:589-590` [CHECKED]. Every loyalty precedent the corpus collected (Imperator, JA2, EU4, X3) is a moving quantity (R4 C, T). [IN/FA]
3. **The only historical finding about persons that reached the season register (H-100, seat provenance sets revocation cost) is answered by a proposal keyed on a different variable** (the seat's `conferral` basis, not how the seat was won; the proposal's own R3 says so) — [CHECKED H-100; IN-31 proposal :25, :146, :606]; C4b F, H. [FA/IN]
4. **RTP, the bin's one research file, is weakly delivered**: pasted agent chatter (l.11), two statuses (FILED and PROPOSAL), fact-check outcomes shown for six entries, a §3 design built on the retired Key substrate, and a minor count slip ("~96" cases against 94 entries) — [CHECKED RTP l.3, l.11, l.25, l.312, l.761]; R7 K8, K12-K14. [IN]
5. **The authored cast is thinner than its loader claims**: `cast.py` says 29 rows carry `stats`, 32 `ts`, 30 `goals`; non-null counts are 1, 10 and 17; of the 10 `ts` values two are strings ("75–80", "~50") and no code reads `ts` at all [CHECKED]. [IN/WR]
6. **The leaders are mis-housed, not mis-seated**: five of six faction leaders in `npcs.yaml` have `institution: null` and homes in cottages, markets or an inn (the King at `b_s_002_cottage`, in S-002 Auerheim, not the Seat S-001); Hafenmark's leader is tagged `institution: Crown` at `b_s_001_court` — `npcs.yaml:183-237`, `cohorts.yaml:65-67` [CHECKED]. Office tenure is correct: a seat's faction comes from the cast, and `test_fa01_head_seats.py` asserts all six heads hold an own-faction seat and five of six act through it at the first fold — `engine/season/tests/test_fa01_head_seats.py:18-24, 114-123` [CHECKED]. What is wrong is residence and the `institution` tag, which the plan's regicide reading (IN-59) inherits — `_part5` IN-59 [CHECKED]. [IN/FA]
7. **The design corpus contradicts itself on every person-level fact**: TS values, names (Haelgrund Sæmund/Lennart; registry TS 15 vs 12), Standing 0-5/0-7/0-10, defection roll or no roll, relational graph BUILT and deferred, five succession designs — A5a H; A5b H; A7b H; U3 H; [CHECKED registry]. [WR/FA]
8. **Game-precedent sourcing degrades downstream**: dropped `[UNVERIFIED]` marks, a self-contradicting desertion null in PMM, inflated convergence counts (X1), a contradicted null (N-9), and one suite that anonymizes all its precedent — R4 K1, K6-K11; R8 K12; C5 G. [IN]
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
| `proposals/2026-10-03-verb-coverage-and-gap-fill.md` (VCD) App. B, family 63 and G15 | Grudge loop and damping (RimWorld, Guild 3, Bannerlord, Radiant AI); CK3 hooks, imprison, murder schemes | RATIFIED AS INTENT (ED-IN-0288); game claims partly [UNVERIFIED] (C8a G, H) | The only precedent that reached a scheduled person-verb (`forgive`, IN-12 step 13), and through a proposal, not research |

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
| Loyalty 0-100 | `cast.loyalty` cosine to role template; static (built, "can be invented") | RTP `power_base` liabilities; GOV "rank only as solid as its currency" | Imperator bleed; JA2 idleness; X3 "idleness punished 4/5"; EU4 loyalty vs influence | **UNGROUNDED (ruled invention) · precedent UNREACHED** — every cited precedent moves loyalty over time; this value is static and nothing writes its referent (the leader); the only in-season stance term of that shape is a defeat bleed toward the faction (`effects_combat.py:256-261`), uncited to Imperator | `cast.py:256-332`; `populated.py:787, 854-856` [CHECKED]; R4 C, T |
| Pursuits (15) × axes (7) as the decision's moral term | IN-08 cells (built); ED-IN-0261 ruled | philosophy traditions per pursuit (CPC §1a); 55 of 105 cells "reasoned" | Triangle Strategy hidden conviction axes (uncited); Prom Week's diffuse-causality caution | **PARTLY** | C7b F, G; R4 C (P5 §12.5); R8 C |
| Conviction = religious affiliation vector; confliction | STR-6 ruled; `conviction_of` built; **0 rows authored on `main`** | none | none | **UNGROUNDED and inert** — a known, scheduled gap (H-188's default; IN-64, batch B-X) | [CHECKED registry parse]; B2b H |
| Scar count, crisis at 3 | `_scar`, `conviction_after_crisis` (built); scar entries 61 → 508 with full vectors (session probe) | Catherine de' Medici, Charles V, Litz/Shay (PP-718 self-vetting) | none | **PARTLY** — history over-claimed for a d6 table that no longer exists; the live rule cites none | D1 G; `_part5` IN-65 |
| Grievance at read (IN-58) | stance-only half landed, sworn-to half BLK; EXIT "hash MOVED" not met, disclosed by the plan | RTP G-series (patron-lapse purges); vendetta edge type | CK council denial −40 Grudge; RimWorld; Nemesis encounter log; M&B execution starts feud | **UNREACHED** (research) · game shape present, uncited | [CHECKED `_part5` IN-58]; R4 C; C8a G |
| `forgive` (a grudge ends) | VCD G15, IN-12 step 13 (scheduled) | wergild (uploaded v3 P8, not in tree) | RimWorld, Guild 3, Bannerlord, Radiant AI (VCD family 63) | **PARTLY** (proposal-grade game evidence; R-9 "grudge ends only by `forgive`" vs MATTER decay is Jordan's) | C8a F, G; C8b H |
| `tie/knot`, relational edges, defection cascade | effect declined (H-182: 83 formed, 0 offered); graph PROVISIONAL, BUILT/deferred | Woodville affinity cascade (RTP C4), *fede giurata*, Medici *clientela* — not linked | KOEI RoTK officer bonds; CK3 | **UNREACHED** | B2b H; A5a G; R7 B§C4 |
| Changing sides (defection) | `release` + `commit` (commit executes since IN-11, H-156) | RTP F6 Wallenstein (subordinate flip), H8 favour-dependent counter-faction | Pax Pamir punished switching (cited by SFP and EN/04, refused there); JA2 staffing refusals | **UNREACHED** — two neutral acts with no cost or trigger; the design check (Spirit vs Disposition) has no carrier | B1b F; R7 B; C4a G; C7a G |
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
  verbs — known only as VCD carries them (`00_INDEX.md` §7).]
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
