# Digest canon_arch1

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: `canon/` (foundations P-01..P-15), `architecture/` (Layer 1), `godot/`. Entries are in assignment order.
Line references are to the file in the entry. `[UNVERIFIED]` marks anything not checked against the tree.

### architecture/00_ADOPTION_README.md
- **What it is:** Layer 1 adoption cover note for the season-loop architecture (successor to PR #353), ratified 2026-09-05, amended 2026-10-03 and 2026-10-28; reads as a lane-IN document.
- **Status:** "RATIFIED 2026-09-05 (ED-IN-0204) ... LAYER 1 ... binding as AGENT INSTRUCTION ... AMENDED 2026-10-03 (ED-IN-0284/0285) ... AMENDED 2026-10-28 (ED-IN-0302/0303)". Reading: live as agent instruction; its measured numbers are historical.
- **Bears on:** CORE, PROCESS, GO (the scene/rung/`game/` amendment).
- **Content that matters:**
  - Layer 1 governs "the game code" = `engine/season/` plus `modules/<name>/` reached by composition row (:3). The 2026-10-28 amendment: a registered module's playable form is a *scene*, `rung` is the world side, the scene tree lives in `game/` not `port/` (:3).
  - Measured result of the tested #353 version: 46 NPCs, 97 arcs, 972 requirement rows, 121 probe executions, ZERO cases end to end (:44); "Artifact 2 is the bar: one NPC season, end to end" (:93).
  - Conditioned by "#358 rev.2": `scale:` on ten verb rows fails invariant 10 (retired when `Act.via` carries scope); `kill/wound` writes become `Degree`-keyed (invariant 12), bands `assumption` at H-98 (:11-17).
  - Open at :14: eligibility can decline and no row declares a refusal for it; the fold emits `act.ineligible` / `act.refused` / `contest.resolved` as body literals that invariant 7 refuses.
  - "Six steps" is explicitly left unedited; M4 (ED-IN-0279 (a)) added a seventh step ENCOUNTER sharing barrier 3; current count lives in `04_CODE_ARCHITECTURE.md` §A.2/§C.1 and `03_VERBS_AND_LOOPS.md` §D.1 (:56-59).
  - Critical path stated as W0 -> W1 -> W2 -> W3 -> W5 -> W9 ending at one NPC season (:107).
- **Conflicts / stale:** the file table (:27) lists `hole_register.yaml` as a sibling; it lives at `engine/season/hole_register.yaml`. The command `python engine/season/register.py --counts` (:27, :104) is stale: `engine/season/register.py` does not exist; CLAUDE.md names `python -m engine.season.harness.register`. Counts "113 rows as of 2026-09-05" are dated, not current.
- **Open items:** the "one question for Jordan" in PLAN.md is referenced (:25) but not stated here.

### architecture/01_NPC_VS_ARC.md
- **What it is:** companion measurement to ARCHITECTURE_V2: refusal-vs-hole census of NPC vs arc case sets, computed from the 2026-09-01 probe ledger.
- **Status:** same RATIFIED/Layer-1 banner as the README; the body carries its own banner "EVERY NUMBER IN THIS DOCUMENT IS ROUTER-ERA AND IS NOT CURRENTLY REPRODUCIBLE" (:10). Reading: historical measurement; the qualitative hypothesis is live.
- **Bears on:** CORE, ARCS, CHAR, FA.
- **Content that matters:**
  - Headline: "0% of NPC core blocks are refusals, 33% of arc's" (:7) is then corrected: P33 (act cost) is a ruling not a hole (#353 `:927-930`), F19 is an L1/T5 refusal; 21 of 23 blocked NPC cases contain no refusal (:70-91, :104).
  - Five refusals the design makes on purpose: L1 institutional actor, L3 stored social aggregate, L5 threshold outcome, no fourth clock, no GM/referee (§2.2, :122-130). 22 arc core blocks "re-authored against the primitives, or they do not run" (:132-134).
  - NPC set throughline: "THE PERSON HAS NO DURABLE INTERIOR THE ENGINE READS" — P10 work in progress, P17 quiet counter, P26 accumulated harm, P32 condition band (:153-158). ARC throughline: arcs want a narrator the design deleted (:160-165).
  - P17 (a per-(Person, axis) counter) is the one blocker large in both sets (4 NPC, 16 ARC); H-20 named "the single highest-value row in the register" (:179-181).
  - Scale mix: NPC cases person 21 / faction 18; arc cases realm 43 (:136-147) — the refusals all bite at aggregate scale.
  - Arc lane has 0 of 611 rows declared; NPC 35 of 292 (:25-28) — the arc column is "unmeasured".
- **Conflicts / stale:** its own three totals do not agree (26/71 vs 25/66 vs 22/63, :85-91). `proposals/2026-09-01-season-loop-tests/tracer` command at :25 [UNVERIFIED]. Pre-dates the CHAR decision layer and REM-44.
- **Open items:** the arc re-authoring pass for ~22 arcs against §36.3 petition chain and §37 dispensation (:169-175) is named and not shown done here.

### architecture/ARCHITECTURE_V2.md
- **What it is:** the proposal that closes #353's execution gaps: write matrix keyed on (kind, field), verb table, NPC decision policy, delegation doctrine, hole register (Part VII); 923 lines.
- **Status:** same RATIFIED Layer-1 banner (:3) plus "REFERENCE, never mechanism ... nothing in it runs" (:4). Reading: live as intent and as the Layer-1 source; several sections carry in-text amendments that supersede the body (W5, REM-44).
- **Bears on:** CORE, CHAR, SC, FA, SE, FI, DICE.
- **Content that matters:**
  - Part D (:279-352): write matrix, one row per (kind, field) with `social:` and `emits:` columns; derivation DR-1 (world-written step -> `social:false`), DR-2 (RESOLVE only -> `social:true`), DR-3 (silent, state the row). "ANY (kind, field) NOT ON THIS TABLE IS AN UNMARKED CELL AND THE WRITE RAISES" (:351).
  - Part E verb table (:408-439): ~28 verbs with stratum (0 movement .. 4 social), eligibility (`own|remit:|hold:|presence:`, "NEVER capability" §9.2), `requires`, `writes`, `emits`, `emits_on_refusal` (scarcity channel, §27.1). Invariants: capability gates no verb, office adds no verb, no second resolver (:441-448).
  - Open verb holes: `determine` needs `judging_set_rule` (D11, `absent`) so "nothing is decided at a sitting" (:418, :451-453); `refract` side `absent` (D18); `create_record`/`forge` have no cost (:459).
  - §F1 question sources Q1..Q4 (Date due, claim landing, Sensation band change, standing commit to an OUGHT Proposition); Q4 added by W5, closed sets belong in `rosters.yaml` as `question_sources` (:470-491). Candidate filter is on the person's OWN claims, not world truth (:503-506).
  - §F2 `choose` scoring: conviction x alignment + stance + urgency (:513-520). Pointer at :522: REM-44 (ED-IN-0300) deleted the urgency term and `Sensation.subsistence`; live terms are `decision/choose.py::score_terms`, shape `04_CODE_ARCHITECTURE.md` §B.10/§C.3.
  - §F3 `budget : (Person, View) -> int` person-side, reading own hold Tenures, body band, travel legs (:548-575); H-35 ruled by Jordan 2026-09-02: the SCENE is the budgeted unit, 5 per season (:758).
  - Part G grade-decides-behaviour doctrine (:638-646): `absent` -> REFUSE; `assumption` -> inject default, declare, site, sweep; a flipping verdict is itself a finding. Register row shape at :686-696.
  - Part VII Tier-0 holes H-01..H-12, H-26 and Tier-1 H-20..H-39 with grade/default (:724-762). Still `absent`: H-31 degree-ladder margin model ("every contest is blocked"), H-32 judging set, H-33 five witness channel predicates ("nothing said in private is private"), H-36, H-37, H-38, H-39 (:754-762).
- **Conflicts / stale:** `standing` (§F4, D3/H-29) depends on `Sensation`'s two scalars; REM-44 removed one (:522 only partly reconciled; the file says the other mentions are "not individually re-walked"). H-31 (degree ladder margin model) marked `absent` at :754 while `engine/season/seam.py::degree_of` exists (see VOCABULARY.md). The command `python engine/season/register.py --counts` (:714, :899) is stale (module moved to `engine/season/harness/register`). Counts at :766-793 are struck through by the file itself.
- **Open items:** H-23 (act cost beyond budget), H-25 (termination bound per spiral), H-33 witness predicates, H-37 fault roster, H-39 construal spread are `absent` here; whether the code has since filled them is for the CORE/CHAR/SC lanes [UNVERIFIED].

### architecture/PLAN.md
- **What it is:** the improvement plan for building the season loop to execution, adjudicating ARCHITECTURE_V2 and listing work items W0-W32, guardrails G1-G11, the bar (Part 6); 2097 lines, heavily annotated with "LANDED" notes dated 2026-09-02..09-05.
- **Status:** same RATIFIED/Layer-1 banner (:3); §8.5 (:2024-2027) says "PROPOSED, held back in full" and "Nothing in it runs" (:7). Reading: historical work-plan with some live constraints (guardrails, "what not to do"); most numbers are router-era or dated.
- **Bears on:** CORE, CHAR, SC, FA, FI, ARCS, PROCESS.
- **Content that matters:**
  - §3 closes 11 of 12 `absent` holes by CLAUDE.md §0's five tests: H-23 act cost is a RULED REFUSAL ("No cost clause is required. A petition consumes budget like any act", #353 `:927-930`, :364); H-38 a person DOES carry a banded scalar (:366); H-36 refraction is RECEIVER-side (:402-417); H-31/H-32/H-33 regraded `assumption` with defaults (four-band margin ladder; judging set = holders of a `determine` remit whose scope contains the venue; five witness-channel predicates) (:375-383).
  - H-35 ruled by Jordan 2026-09-02: "5 scenes for a character to play per season" — the SCENE is the budgeted unit, every character has it; interactions per scene (1-3) and extended-scene cost (2) are `assumption` rows citing `player_agency_v30.md` §6.3 (:419-460, W17 :1199-1236).
  - Guardrails G1-G11 (:1926-1940): a fill off the register is a red test; test the property not the string; over-refusal equals invention in weight (G4); an adversarial pass EDITS the thing, no findings doc (G5); no guard under `tools/` for this (G9); never average NPC and ARC lane counts (G10); every number ships with its command (G11).
  - Part 4B (:1297-1384): the first critical path W0-W5-W17-W9 completed and ran 0 of 143 cases; defects found by running: N1 `Q1` dead (calendar sets `fired` before `questions_for` requires not-fired, :1341), N2 the loop hands the seam ONE claimant so contests raise PARTY-GAP (:1345), N3 deliberation absent from the causal graph (closed 2026-09-03, :1346), N4 every corpus world has the same cast (:1347), N5 register `site:` never checked to exist (:1348).
  - Part 6 bar (:1751-1870): NPC `RUNS` needs R1-R5 including R3 "an Act by ANOTHER person whose causes[] walks back" (Event-level wording was satisfiable 711/711, :1781-1789); ARC `ENDS` by DECIDER/ROLL/THRESHOLD/NEVER labels; about 44 of 97 arcs name a player/party so `WAITS-ON-PLAYER` is a valid terminal status (:1862).
  - §4B.2 bucket A (:1358-1367): 47 corpus cases declare `scale: faction`, a ruled refusal (L1); "the brief was written in a vocabulary the architecture had already closed"; W28 re-scales them. Open `world` scale reading: a world = set of realms, >=2 realm Rungs (:1613-1617).
  - W16 (:1260-1293): two degree-ladder owners each claim to be "the one" (#353 `:1397` and `engine/autoload/dice_engine.py::degree_from_net`).
- **Conflicts / stale:** commands name `engine/season/register.py` (:560-580, :850) which does not exist (now `engine/season/harness/register`; checked by `ls`). Test counts "181 passed", "63 passed" are dated, the file itself says run the command (:145, :1315). `engine/autoload/dice_engine.py` path at :1273 vs VOCABULARY.md's `engine/autoload/dice_engine.py` and CLAUDE.md §5's `engine/dice_engine/dice_engine.py` [UNVERIFIED which is current]. W6 note: third proof clause ("a tell reaches only the told") declared structurally unreachable (:988-1001) because the Event has no target (§19.3).
- **Open items:** per-kind witness-channel policy (so `news.told` can be narrower than `condition.worn`) (:998-1001); H-86 split of `emits:` into `emits_per_write`/`emits_when` (:869-878, W32 :1655-1660); H-94 structural half, H-98 (winner vs degree), H-95 `world` half are live escalations (:2044); W14 Godot port artifacts "not before W30" (:1670). Whether W18-W32 all landed is not stated here [UNVERIFIED]; CORE lane should check against `python -m engine.season.harness.corpus_run`.

### architecture/VOCABULARY.md
- **What it is:** a ballot of Layer-1 terms in four tiers (repository, world, boundary, subsystems), 2026-09-05; 157 lines.
- **Status:** "PROPOSED — a ballot, not a ruling", with a top banner "DO NOT RULE ON THIS FILE YET (2026-09-05). An adversarial pass overturned four dispositions" (:3-14). Reading: unclear/unresolved; probably never ruled [UNVERIFIED whether CLAUDE.md §4's word-choice rule or `references/names_index.yaml` superseded it].
- **Bears on:** PROCESS, CORE, SC (the `social_contest` naming row), GO.
- **Content that matters:**
  - Tier model ranks vocabulary by blast radius: repository / world / boundary / subsystems (:38-61); stability not containment (:63-69).
  - `layer` collides with epistemic/argument/narrative layers in `engine/season/` (:82); `loop` collides ("the apparatus loop" vs "season loop", :83); `module` has two ranks, a contract row in `module_contracts.yaml` vs a `.py` file (:79).
  - Seam/bridge/adapter are three words for one thing; proposed: seam = the contract, adapter = the implementer, bridge retired (:86). `seam`'s Tier-1 definition ("the ONE place ... RESOLVE via contest") is falsified by Jordan's 2026-09-05 "each mode of play is separately called from season loop" (:106).
  - `mode of play` vs `scale of play` used as synonyms but are not: "personal combat and mass battle are one MODE at two SCALES" (:119-120).
  - `resolver` has two senses (ladder vs callable); proposal: resolver = the ladder, `target` = the callable (:126). `social_contest` is "the genus inside a species name": 30 tracked files carry it in their path, 299 mention it, ED lane `SC` has 32 ids (:138).
- **Conflicts / stale:** mentions `keys` as a substrate leaf (:84) and "the Key" substrate is RETIRED (ED-IN-0232). `degree` marked RATIFY at :125 but the banner at :4 says `seam.py::degree_of` branches two band vocabularies and the RATIFY is false. The ballot references `engine/mc_v18.py` as old driver [UNVERIFIED present].
- **Open items:** all `CHOOSE` rows (seam, mode/scale, social_contest rename, layer, loop) unanswered in this file; the banner itself says rebuild before ruling.

### architecture/holonic_ARCHITECTURE.md
- **What it is:** the "holonic" season-loop architecture and Godot build guide (the #353 spec this chain rests on): laws L1-L5, primitives, the loop, scale, contract descent, Godot port, fold-in set; 2078 lines.
- **Status:** same RATIFIED/Layer-1 banner (:3) plus "REFERENCE, never mechanism ... nothing in it runs" (:4). Reading: live as Layer-1 source for `engine/season/` and `modules/`; CLAUDE.md §3 names §43, §45-§47 as the rows `layer-conformance` Lens B checks `modules/` against.
- **Bears on:** CORE, CHAR, SC, FA, SE, FI, MB, PC, GO, WR.
- **Content that matters:**
  - Throughlines T1-T9 and laws L1-L5 (:114-195): L1 person is the only actor ("obstruction falls out, no `obstruct` verb"); L2 `choose` has no World "by type"; L3 every aggregate is a function, never a field (clause 2: no resolver-side Query sums per-person tallies; §22.4 adds clause 3, aggregates compose over LIVE edges only); L4 `social: bool` partition on (record-kind, field); L5 Edge Law: a crossing may change WHAT MAY BE CHOSEN, never write a social row or produce an outcome; every clock beyond matter/bodies/memory-confidence "was set by a nameable act".
  - R-1/R-2 rung contract and the barrier-cache concession (:202-216); two topologies, containment tree vs lateral graph (tie/knot/commit/distant hold), R-1 governs only the tree (:240-276); code hierarchy vs world hierarchy are different trees (:278-294).
  - Primitives: five carriers (Person, Rung, Office, Site, Record), immutable Proposition, one edge `Tenure` of seven kinds (:304-345, :529-545); a cohort IS a Person at weight>1, "refuse the subclass" (:339-343); capability supplies dice and gates no verb (:345-350); WITNESS never touches a Belief (:352-362). `reside` was added as an eighth Tenure kind 2026-09-30, separating where one lives from where one is (:539).
  - Loop: six steps/four barriers (:786-817; pointer: ENCOUNTER added by M4, seven steps now); RESOLVE is an ordered fold (not grouping), "No second resolver. No auto-resolve formula. No fast path" is called the highest-value refusal enforced only "by a person noticing" (:984-990); sum-then-clamp-once and fixed-point arithmetic (:992-994, :1116-1146, :1819-1828).
  - Seam: `contest(World, Rung, prize, claimant[], depth, max_depth)`, claimants are persons always, no default depth cap, ONE degree ladder of four bands read off the margin, demote-only `bool` veto injected by the wrapper (:1356-1423). A five-band ladder exists in the corpus; owner implements four (:1422).
  - Act budget ~5 scenes ruled; petition spray allowable ("no cap, no dedup, no required cost gate"); thin act vocabulary is an "accepted state" (:902-954, :2006-2014). Wrapper layer retired; routing is a registry row not a computation (:1638-1696). Modules register by composition row resolved AT BOOT, not import (:1623-1636).
  - Godot port: `core/` holds no Node, autoload table empty, World never an autoload; two licensed guards (autoload check, token scan) (:1699-1817); version floor >=4.4 stated (:1860-1872) — but CLAUDE.md says the Godot version is ruled by ED-GO-0002 and nothing in this tree asserts one.
- **Conflicts / stale:** §18.2 Sensation "exactly two scalars" superseded by REM-44 (one scalar, `standing`), pointer at :635; §23 "six steps" superseded by seven (:813-817). §8 says an `address` is a `contain` Tenure, partly overtaken by `reside` (:539). §52's >=4.4 floor vs ED-GO-0002 (CLAUDE.md) [UNVERIFIED which now governs]. Document restricts evidence to PR chain #337-#352 (:13) and rejects `engine/` as authority, opposite to CLAUDE.md §0.05 (code is mechanism) — scoping artefact of the proposal, not a live rule. `ARCHITECTURE_V2` said the register has 12 `absent` holes; `PLAN.md` closes 11.
- **Open items:** §62 live choices (:1996-2004): scene=act (since ruled in PLAN.md), refraction side (since closed receiver-side in PLAN.md), whether "no reaction inside a season" survives the seam, whether a social quantity may sink by neglect (three arcs), dispensation distortion magnitude. §61 debts: judging_set_rule, `q` producer, WITNESS total fan-out, no spiral termination argument, season_factor owner, cohort construal spread, travel-leg ownership. Ten execution artifacts at §66 (:2056-2072); artifact 10 (twelve trajectory transitions) never run per the file.

### architecture/meta/00_THE_METHOD.md
- **What it is:** one-page front door to the meta-architecture: the three generators, three questions, six moves, four rules of emergence, the one hazard; 175 lines.
- **Status:** same RATIFIED/Layer-1 banner; "the page to read first ... If this page and a stage disagree, the stage is right and this page is stale" (:4-5). Reading: live reference.
- **Bears on:** PROCESS, CORE, CHAR.
- **Content that matters:**
  - Three questions for any design: WHO OWNS THIS (field / edge owned by its subject / Query owned by Nobody / barrier cache; "two owners = a defect") (:26-45); WHAT CAN CHECK THIS (loader-validated data or a code falsifier; prose "does not exist yet") (:61-71); WHOSE ACT MAKES THIS HAPPEN (a named person, or matter/bodies/memory-fading; "nobody's = a narrator, remove it") (:73-82).
  - D.0 admission: a field asserts what is DECLARED, THE CASE, or READ OFF; one that cannot be sorted is on the wrong carrier (:47-53). "First-class for consumers is not first-class for state" (a view has lifetime, not absence, as its defence) (:55-59).
  - Four rules of emergence: emergence is what is left when you refuse; a primitive earns its place by what it makes unnecessary; interaction must be uniform ("rule count must not grow with pair count"); no primitive may know another's purpose (:121-136).
  - The test: a rule whose subject is a specific PAIR belongs to one of the two or is a Query (:154-161); Jordan's later rulings (a faction is a deployable view; factions can be at war) added no primitive but exposed representation gaps F.32/F.33 (:163-172).
  - Stage output is "a loader invariant, a type or a falsifier"; the doc is not the artifact (:110-117).
- **Conflicts / stale:** none found; its "twelve loader invariants" (:116) are Stage 4 (`04_CODE_ARCHITECTURE.md`, not in this lane).
- **Open items:** the claim that a SCOPE (not an instruction) defeats the "defer to what exists" hazard is flagged as the least-evidenced claim, "no stage has ever actually run under one" (:147-150).

### architecture/meta/01_AXIOMS.md
- **What it is:** Stage 1 of the meta-architecture: seven axioms, theorems T-a..T-o, idioms ID-1..ID-18, carrier schema (Person, Rung, Site, Record, Proposition, Office, Tenure, Event/Act/Claim, Faction view), derived open questions (subordination, delegation, ladder); 1709 lines, dated 2026-09-03 onward.
- **Status:** same RATIFIED/Layer-1 banner. Own text: "Scope: Jordan-directed ... top-down ... Nothing here is built and nothing here is meant to run" and `CLAUDE.md` §0.2 "DOES NOT GOVERN THIS DOCUMENT" (:4-25); "Not ratified. Merging it ratifies nothing" (:1702). Reading: live as reference; later amended through 2026-11-07.
- **Bears on:** CORE, CHAR, FA, SE, FI, SC, WR, PROCESS.
- **Content that matters:**
  - Axioms (:75-319): AX-1 only a person acts; AX-2 no privileged access to the world; AX-3 true vs right are different kinds; AX-4 every value has exactly one owner who is its only writer; AX-5 the world moves by itself in exactly three ways (matter, bodies, memory fading) — fading changes a claim's confidence, never its value; AX-6 nothing becomes permanent without an author (state, not schema); AX-7 (RULED 2026-09-17, ED-IN-0244) no character touches the world directly, three layers (objective performance / performer's own understanding / others' understanding), divergence governed by channel, competence, prior belief and (2026-11-07, H-L0-11) teller affiliation, binds the character never the player, does NOT reach permissions/remits (Jordan: "too noisy ... for assailable/uncertain remits").
  - AX-7 falsifier names live violations: `loop/witness.py:191`, `:271`, `:361` construct `Claim` with the engine's own event kind asserted TRUE, unmediated (:306-317) [UNVERIFIED whether still true; WR/FI/CHAR should grep].
  - T-d honoured in field name, violated in mechanism: `Event.subject` is set to the actor so every ledger holds "I hold that <actor> did <kind>" certainly and identically (:396-402); `W24` is the proposed fix. T-g obstruction needs no verb (`confer`'s 1-per-object precondition refuses, `emits_on_refusal` carries it) (:425-441); obstacle (rolled against) vs obstruction (a refusal) are different things (:443-455).
  - Idioms (:508-742): ID-9 the gate applies the write (measured instances: `move` published `travel.moved` changing nothing; `work` accumulates no delta so site condition is a one-way ratchet; `term.matured` marks nothing); ID-13 a declared field that no resolver reads does not exist (`scale:`, `stratum`, `contests:`); ID-14 what an act can open an act can close, with opener and closer sets per tenure kind (four of seven relations are open-only); ID-15 view vs carrier; ID-16 enumerate loops and sign them (cycle enumeration over write/read graph is BLOCKED on typing verb `requires`, F.24); ID-17 a suspension is a band on a Query; ID-18 enumerate schema permanences.
  - Schema decisions: `beliefs` is NOT a field — a belief is a `commit` to an OUGHT Proposition; `convictions` stays a field (:866-890). Office `establishment` is a Query over `oblige`, not a field (:980-992). Title is not an entity: a rank whose domain is a rung kind, with governing authority / holdings / sovereign power as three separate things (:998-1045).
  - Subordination = an `oblige` edge owned by the swearer (not a Query); T-m an owner may always end what they own; T-o a seat may end what its remit reaches, declared on the seat; `tie`/`knot` should be two directed edges not one stored on the lower id; `succeed` should be the holder's disposition (:1186-1312). War = an uttered Proposition plus owned edge, peace is `until` (:1366-1389). What is owed = an OUGHT Proposition (:1391-1417).
  - RULED 2026-09-03 (Jordan): "Regency and puppet rulers must be possible" and "Same with delegation" -> AUTHORITY IS A PROPERTY OF THE SEAT BEING EXERCISED, never of the person; three seat-filling shapes: governor (establish+confer), council (one seat, membership a Query over `oblige`), election (a Date fires, judging set `determine`s) (:1426-1590). Falsifier named: sovereign power may be the authority that cannot be conferred (:1584-1590).
  - Ladder membership is content, ordering and walkability are architecture; `if kind == "duchy"` is scripting drift; falsifier "fires three times today" (a resolver precondition `here.kind == "person"`, verb table `scale:` column names four rung kinds, titles table total over `rung_kinds`) (:1590-1621).
- **Conflicts / stale:** Part E scope says "Nothing under canon/, systems/ or research/ is authority" (:1173-1176) — opposite to CLAUDE.md §0.05's ranking, a stage-local rule. Reference to `W24`, `F.24`, `H-90`, `H-101`, `G13` rows live in `engine/season/hole_register.yaml` / `registers/` [UNVERIFIED]. AX count moved 5 -> 6 -> 7. The `22` arc-blocks figure is router-era (:96-100). Says T-g "Obstruction needs no verb" yet the code's `confer` refusal path depends on H-71 (remit-verb formation) per PLAN.md. Mentions 3 production sites of `Claim` at `witness.py:191/:271/:361` — check path `engine/season/loop/witness.py` [UNVERIFIED].
- **Open items:** `Office.conferral` vocabulary (named / elected / inherited ...) is content, still open (:1681); per-ending standing cost "Stage 3" (:1682); ID-16 derived-cycle check blocked on F.24; whether sovereign power is conferrable (:1584-1590); whether `Faction` view survives a 40-season legitimacy test (:1697); `tie`/`knot` two-directed-edge reshaping and `succeed` re-subjecting are proposals in :1286-1323 with no sign they were landed [UNVERIFIED].

### architecture/meta/02_HIERARCHIES.md
- **What it is:** Stage 2: hierarchies, dependencies, nests and scales; 267 lines.
- **Status:** same RATIFIED/Layer-1 banner; "Nothing here runs and nothing here is meant to" (:5). Reading: live reference.
- **Bears on:** CORE, FA, SE, MB, PROCESS.
- **Content that matters:**
  - Three shapes the chain calls "hierarchy": containment (tree, single parent, walkable), subordination (cyclic graph, no root and "must never be given one"), rank (a total order of domain width, "rank is not headcount") (:20-56).
  - "Only places nest; everything else relates"; faction under faction does not nest, but `holdings(faction)` and `members(faction)` are named Queries (:64-95); a contest nests TIME not SPACE and needs a caller-supplied depth cap with no default, exceeding it returns a typed refusal (:97-113).
  - Branching rule: "BRANCH ON THE ORDINAL OR ON THE RELATION. NEVER ON THE MEMBER" — `if rung.kind == "duchy"` is scripting drift; falsifier: change the roster membership and see what breaks (:146-157).
  - Module contract = rung contract: write only what you own, read own plus aggregate over descendants; "acyclic import graph is not an acyclic dependency graph. The engine depends on subsystems exactly as much as it ever did" (:202-221) — matches CLAUDE.md §3's "acyclic is not independence".
  - Reference graph is cyclic on purpose; every traversal iterative with a visited set (:223-231).
  - Graded ABSENT rather than asserted: "only places nest" and "the subordination graph has no root" have no check (:247-260).
- **Conflicts / stale:** §B.1.1's 2026-10-28 note: "container" now means a *view*, a registered module's playable form is a *scene* (:82-83).
- **Open items:** contest depth cap value per venue (Stage 3); whether the containment roster carries a sub-settlement tier — content (:262-267).

### architecture/meta/03_VERBS_AND_LOOPS.md
- **What it is:** Stage 3: what a verb is, consequence, a slice of play, the seven-step loop, where a contest re-enters; 314 lines. (Lines 1-3, the title and Status banner, were not re-read; the banner is the same RATIFIED text per `head -3`.)
- **Status:** same RATIFIED/Layer-1 banner; "Nothing here runs" (:5). Reading: live reference; the loop count is the current one (seven steps).
- **Bears on:** CORE, SC, MB, PC, FI, FA.
- **Content that matters:**
  - A verb declares five things: who may attempt, what must hold, what it writes, what it emits on success, what it emits on REFUSAL; "a per-verb body IS a second resolver" (:13-20). Eligibility is never capability; four kinds (own standing, seat's warrant, custody, presence); "an incompetent attempt is a story; an unavailable option is a menu" (:22-32). A seat adds no verb and no modifier (:34-42).
  - A refusal must emit: scarcity lives in the ordered fold; a verb that emits success while writing nothing is "a consequence with no effect" (:76-90). `causes[]` is the narrative layer (:92-100).
  - A slice of play = a SCENE: one person's attention, at one occasion, in one place; ladder interaction < scene < season < campaign; the budget counts scenes (~5) (:104-134). Fidelity (summarised / narrated / expanded into a contest) does not fork the slice — "they agree exactly, because they are the same slice" (:146-153); this is the auto-resolve-equals-played-scene principle MB/PC lanes should hold code to.
  - Seven steps: CALENDAR, MATTER, DELIBERATE, RESOLVE, ENCOUNTER, WITNESS, CENSUS; ENCOUNTER (M4, ED-IN-0279 (a), 2026-09-28) shares barrier 3 and RESOLVE's write class; a verb whose prize row names a `step:` it defers to writes nothing at RESOLVE (the roster's `Declared` band) (:159-188).
  - Contest roster contract: sides are two resolved `Faction` views frozen at seam entry; units are persons at weight, "there is no unit class"; one scale down a squad is the faction members present at a rung (:247-270). A subsystem that returns a winner rather than a margin "has not met the contract"; nothing may mint missing bands; an undecided outcome is legitimate (:286-289).
- **Conflicts / stale:** §F says "Six axioms" (:295) while 01_AXIOMS now has seven; "Fourteen idioms" (:303) vs ID-1..ID-18 in Stage 1. "units are persons, at weight. One type; there is no unit class" (:261) is relevant to the MB lane: it conflicts with a hierarchical army -> unit -> subformation -> troops design if MB code introduces a unit class [UNVERIFIED against `modules/mass_battle/`].
- **Open items:** none new; refers to Stage 4 for per-verb pricing.

### architecture/meta/05_ONTOLOGY.md
- **What it is:** a reading of Stages 1-4 indexed by the question "how do objects, relations, edges and fields work"; 136 lines.
- **Status:** same banner; "If this and a stage disagree, the stage is right and this is stale" (:5). Reading: live reference, partly stale where noted.
- **Bears on:** CORE, CHAR, FA.
- **Content that matters:**
  - Four kinds of value sorted by "who writes this": FIELD (one writer, one thing), EDGE (one writer, two things, owned by its subject), QUERY (spans many owners, owned by Nobody), BARRIER CACHE; "two writers = a defect" (:12-20).
  - Ids typed, minted `H(world_seed, tick, subject, purpose)`, no allocator (:29-31).
  - Field admission: what a thing HOLDS needs a decision-reader; what the world READS OFF it needs a resolver-reader; D.0's third clause declared/the case/read-off (:43-66).
  - Three routes end a Tenure: owner's discretion, declared term, seat-declared revocation (T-o) (:81-95). Edge whose subject cannot act is a field in disguise (`succeed`, seat membership list); `contain` is the honest exception (:101-113).
  - `destroy` sets `until` on tenures naming the id and cascades nothing; `hold`'s subject is `Person` only (:121-136).
- **Conflicts / stale:** §2 lists carrier `Seat` where holonic uses `Office` (:26) — vocabulary drift between Stage 4's `Seat` and the earlier `Office` [UNVERIFIED which the code uses].
- **Open items:** none.

### architecture/meta/06_STRUCTURE.md
- **What it is:** reading answering "how do we structure design going forward": hierarchies, nestings, dependencies, state changes; 104 lines.
- **Status:** same banner; "If this and a stage disagree, the stage is right" (:4). Reading: live reference.
- **Bears on:** CORE, PROCESS.
- **Content that matters:**
  - Code hierarchy `GAME -> MODULE -> DECLARED EDGE -> FIELD`; role, subsystem, key type, phase, scale are axes (:29-31).
  - Process nesting needs a caller-supplied cap with no default; exceeding returns a typed refusal (:43-51).
  - One write shape `(subject, mode create|alter|destroy, driver Act|Event, field?, delta?)`; matrix keyed on `(kind, field)` with `writer: act_only | world_or_act`; "every write goes through one gate, and the gate applies it" returning a receipt; the log refuses an Event carrying a receipt the gate never minted (:77-92).
  - Single test: "Name the writer" (:99-105).
- **Conflicts / stale:** the "log refuses an Event carrying a receipt the gate never minted" is a Stage-4 design statement; whether `shape.World.write` / `Event.__post_init__` implements receipts is for CORE [UNVERIFIED].
- **Open items:** none.

### architecture/meta/07_DYNAMICS.md
- **What it is:** reading on slices, graphs, chains, loops, echo and propagation; 194 lines.
- **Status:** same banner; stage governs on disagreement (:4). Reading: live reference; contains dated supersession notes.
- **Bears on:** CORE, WR, FI, SC, FA.
- **Content that matters:**
  - Graph table: containment (decision-reachable), subordination (no root), lateral web, causation `causes[]`, claim citation (cyclic); the "touch graph" is REJECTED — contests are declared, never inferred from write collisions (:31-41).
  - `tell` chain is the only news transport: "no news service, no rumour tick, no ambient diffusion" (:57-58). Three claim carriers: presence (what changed and who), a document (only that it changed), a telling (what said, at their confidence) (:133-146).
  - The loop that is "actually the game": claim lands -> question -> candidate -> act -> Event -> witnessed -> claim in SOMEONE ELSE's ledger -> their question; originally measured ZERO instances, superseded 2026-09-04 (30 of 30 NPC, 54 of 59 ARC; row `H-102`), but "nothing moves a Record to a second person (`H-84`)" (:80-91).
  - Spirals remain an open debt: nothing bounds season-to-season feedback; ID-16 declared `LOOP` rows with a `sign` column are buildable but no resolver reads them (:95-123).
  - Flood lesson: per-write MATTER emission took events 207 -> 896 -> 3,389; fix was channel predicates (deposits 678 -> 68); "bound echo by who could have perceived it, never by how important it is" (:171-188). PLAN.md later restates 678->68 as stale (711 -> 66 measured).
  - No within-season reaction at person scale: "you anticipated, or you are late" (:194).
- **Conflicts / stale:** numbers 678 -> 68 flagged stale in PLAN.md §6.3 (:1838-1840 of that file). "Zero instances" struck by the file itself.
- **Open items:** spirals; `H-84` Record movement; declared loop list has no reader.

### architecture/meta/08_DATA_AND_KEYS.md
- **What it is:** reading on dictionaries, definitions, registers, keys and buses; 111 lines.
- **Status:** same banner; stage governs (:4). Reading: live reference. Its title says "KEYS" but the Key substrate is RETIRED (ED-IN-0232); the Event is the only "key-like record" it discusses.
- **Bears on:** CORE, PROCESS, GO.
- **Content that matters:**
  - Four data shapes: Roster (closed set), Table (mapping keyed on roster), Fixture (free scalar injected at a named site), Register (holes as rows). Separating test: "would changing this change the GAME or how the CODE works?" (:9-27). A number that is a property of a roster member travels with the roster (`alignment[axis][verb]`); a free-standing one is a fixture (`view_k`) (:24-27).
  - Polarity rule: an absent roster RAISES; a `default_cell` may cover only an unlisted PAIR of registered keys (:37-42).
  - Registered Event kind roster is DERIVED as the union of every emission column in the write matrix and verb table; "a subsystem cannot invent a kind" (:73-76).
  - No bus: a bus routes to a recipient, which needs a `target`, which is forbidden; WITNESS computes observers from presence and five channels (co-located, document, witness-key, post-remit, chronicle) (:84-104). Modules are the one thing that route by name, via role -> manifest row, failing at startup naming the row (:109-111).
- **Conflicts / stale:** "keys" in the title/§4 predates the retirement of the Key substrate; "Event kinds are `family.type`" is the live use.
- **Open items:** none.

### architecture/meta/09_WORKED_EXAMPLES.md
- **What it is:** three worked cases (political strife, a settlement at risk of revolting, excommunicating a mayor) derived from the primitives, each ending in what is blocked today; 178 lines.
- **Status:** same banner; stage governs (:5). Reading: live reference with dated blocker notes.
- **Bears on:** FA, SE, SC, FI, WR, CHAR.
- **Content that matters:**
  - Seven sources of contention that fall out free: scarcity, one seat many claimants, overlapping purview, de jure vs de facto, incompatible honest claims, revocation asymmetry, custody (:23-33).
  - Four-season trace: Count dies -> "nobody convenes, the seat stays empty" (if no person acts, the thing does not occur) -> convene by remit holder -> date fires -> loser's stance moves -> `tell` distorts -> third person acts (:49-67). "A CIVIL WAR IS: ENOUGH NAMED PEOPLE, EACH CHOOSING, IN A SEASON" (:69-75).
  - Revolt: no unrest value; risk of revolt = share of persons at and under a rung whose LIVE `commit` edges are to a proposition incompatible with the holder's (a Query over live edges, reversible); the Query is resolver-side so no person can read it (:79-114). §C.11 explanation contract: owed is the arithmetic of the claims the character holds, not the aggregate (:116-125).
  - Excommunication is an `issue` (a dispensation to EXECUTORS) landing as a compliance contest per person, not a flag; "a mayor excommunicated and ignored is a mayor who is fine" (:147-158).
  - Blocked today: `oblige` cannot be closed, judging set absent, no Record movement (`H-84`), commitment-share Query not computed anywhere, six investigation acts `assumption` with no writes, nine dispensation terms unspecified (:169-178).
- **Conflicts / stale:** blockers dated 2026-09; some may have closed (W26 sitting decides, W21 H-71) [UNVERIFIED]. The revolt design contradicts any `settlement.unrest`/`discontent` stored field SE/WR code may carry [UNVERIFIED: grep `unrest` in `engine/season`].
- **Open items:** the commitment-share Query; the nine dispensation term types.

### architecture/meta/10_FACTIONS_AND_DEPLOYMENT.md
- **What it is:** rationale for Jordan's 2026-09-03 rulings: a faction is a deployable resolved view, and war is an uttered declaration; 148 lines (lines 1-3 not re-read).
- **Status:** "AMENDS the stages ... FOLDED IN 2026-09-03 — this is the RATIONALE, and the stages are now the text" (:4-6). Reading: live reference; superseded in text by Stage 1 §D.11/§E.1.6.
- **Bears on:** FA, MB, PC, CORE, GO.
- **Content that matters:**
  - Jordan verbatim: "factions can't act by themselves, but they should be available as an abstraction for all the people who belong to that faction such that the game code can actually deploy it" and "factions can be flagged at war ... a container for people and holdings ... way easier to define mass battles and grid based squad combat" (:8-12).
  - `Faction := (proposition, members, holdings, seats, head?)`, built at a barrier, owns nothing, never `Act.actor`, a contest claimant, a `hold` subject, or a `resolve` parameter (:24-49).
  - War = a Proposition somebody UTTERED plus an owned edge, peace is `until`; `at_war(A,B)` is a real predicate the combat seam may ask (:55-77); open gaps F.32 (whose edge a war is, so who may make peace if the declarer is dead) and F.33 (whether `at_war` may appear in a verb's `requires`) (:134-137).
  - The seam receives two RESOLVED factions frozen at entry; a squad is the faction members present at a rung (:83-98). A guard was LOST: "a faction cannot gain a field" was structural by absence of a type, now only lifetime (:130-133).
- **Conflicts / stale:** none beyond Stage-1 supersession.
- **Open items:** F.32, F.33 (not shown closed here).

### architecture/meta/README.md
- **What it is:** index and change-log of the meta-architecture (Stages 1-4 plus readings 05-10), revisions 2 and 3; 176 lines.
- **Status:** same RATIFIED banner; own text: "Not ratified ... does not run ... changes no code, register row, roster or plan" (:174-177). Reading: live index; the "not ratified" line sits oddly beside the RATIFIED banner (the banner is later, ED-IN-0204).
- **Bears on:** PROCESS, CORE.
- **Content that matters:**
  - Rev. 2 findings: AX-3 vs AX-5 contradiction (fading removes, never revises), AX-6 scope clause, the write gate never checked `subject == actor` (AX-4 clause 2 was CONVENTION; two live verbs write another person's `Tenure.until`) -> T-o; a lost contest still wrote -> `writes:` `Degree`-keyed for `contests:` verbs (:42-60).
  - Rev. 3 applied seven of thirteen edits left by `proposals/2026-09-03-v2-against-the-meta-architecture.md`; deleted `Tenure.conferrer` (ID-13); `establishment` is a Query at both Stage 1 sites (:5-40).
  - Stage 4 (`04_CODE_ARCHITECTURE.md`, not in this lane) has PART F with 33 gaps; two block the build outright: `F.20` nothing founds a hearth or builds a site ("the world only decays"), `F.24` every verb's `requires` is a prose string ("the resolver has thirty") (:107-113). PART G is called the most durable thing.
  - Scope rule of the exercise: admissible sources are the axioms and PR chain #337-#357; nothing under `canon/`, `systems/`, `research/` or `engine/` is authority (:114-124).
  - Method: derive with the tree closed; decompose by who writes what; write in a form a loader/falsifier can evaluate; close only on representations (:97-99).
- **Conflicts / stale:** scope line contradicts CLAUDE.md §0.05 for code authority (stage-local); "There are SIX axioms" (:155) vs seven now. `F.20`/`F.24` status unknown [UNVERIFIED; CORE/SE lanes should check whether hearth founding and typed `requires` exist].
- **Open items:** F.20 and F.24 as above.

### canon/00_philosophical_foundations.md
- **What it is:** the original "Philosophical Foundations" compendium (Parts 1-8, 18 sections, appendices A-B); prose theory of threads, Ein Sof, rendering, monstrosity, Calamity, Church, Coherence/drift; 472 lines, text dated through 2026-04-25.
- **Status:** "SUPERSEDED — 2026-09-07 ... by canon/philosophy/" (:1-25), retained unedited for ~70 citing files. Reading: superseded (historical; use `canon/philosophy/`).
- **Bears on:** WR, CHAR, FI, PC (monstrosity), DICE (Coherence/TS).
- **Content that matters:**
  - Inseparability: every thread operation moves temporal, epistemic and actualized dimensions together; operations differ only by intended target (:87-93); every operation produces some Temporal Disjunction (:105-107).
  - Rendering is consciousness-performed; thread operations change both facticity and rendering, so "changing the world" and "changing how it is experienced" collapse (:127-137).
  - Monstrosity = the Lacanian Real, ontological not moral; three emergence modes (ordinary incursion, Providence, threadcut) (:141-195). Confrontation produces a trauma-like signature that is the rendering's correct response to finitude (§4.3, :159-175).
  - Calamity: over-drawing the substrate tears it at anchor points; ground has no agency; "forensic not explanatory" knowledge (:199-213). Collapse is ontological devastation through the knot lattice (:215-233).
  - Coherence = integrity of layer-two self-rendering (reflexive and outward facings), tridimensional, orthogonal to Thread Sensitivity; Coherence 0 is not threadcut (:341-364); reality-strain for high-reach Coherence-0 beings (:385-391).
  - Perceptual prophylaxis (Church theology forecloses sensitivity) is emergent, not designed (:245-267).
- **Conflicts / stale:** its §4.2 "rendering's preference for stable actualisation" and the Calamity-as-tearing account were ruled against/revised by `canon/philosophy/RULINGS.md` per the sibling banners (stabilizing tendency, Calamity mechanism, what the Church worships) [UNVERIFIED until RULINGS read below]. "Coherence 0 outcomes by TS" are in the amendment files.
- **Open items:** none; superseded.

### canon/00_philosophical_foundations_rules.md
- **What it is:** condensed loadable rule set (A1-A15, vocabulary, C1-C5 universal principles) derived from the foundations compendium; 137 lines.
- **Status:** "SUPERSEDED — 2026-09-07 ... recommended for retirement rather than migration" (:1-31). Reading: superseded; banner calls it a third restatement that introduced two drifts (a second referent for Providence, "what came through the tear were threadcut beings").
- **Bears on:** WR, CHAR, PROCESS.
- **Content that matters:**
  - A8 redefines Providence as "the rendering's tendency toward stable configuration", while the compendium's §5.2 (and P-05) use Providence as an emergence mode — the banner names this as one of the suite's worst drifts (:64-65 vs compendium :183).
  - A14: "What came through the resulting fracture were threadcut beings" — contradicts the compendium §6.2 (surfeit flooded; why Solmund unknowable) (:82-84).
  - C1-C5 are game-facing mechanic rules: every thread op must fire all three dimensional effects; track cumulative Temporal Disjunction; character growth through confrontation not XP; drift mechanics tridimensional; social bonds are mechanical bonds (:113-128).
  - D: "Any mechanic that violates A2, A11 or A14 is a canon violation regardless of other considerations" (:137).
- **Conflicts / stale:** C3 "Character growth through confrontation, not XP accumulation" conflicts with any XP/skill-advancement mechanic in CHAR [UNVERIFIED].
- **Open items:** none.

### canon/01_foundations_amendment_self_rendering.md
- **What it is:** 2026-03-31 amendment: three layers of being-persistence, the Leap as suspension of layer 2, Coherence redefined, Coherence-0 outcomes gated by Thread Sensitivity bands; 167 lines.
- **Status:** "SUPERSEDED — 2026-09-07 ... chiefly canon/philosophy/04_being_persistence.md and 07_drift.md" (:1-29); inner "Status: Canonical". Banner says "central derivation sound, citation not" (:24-26). Reading: superseded.
- **Bears on:** CHAR, PC, WR, DICE.
- **Content that matters:**
  - Three layers: (1) Ein Sof spooling, (2) unconscious self-rendering, (3) deliberate threadwork; organic humans have 1+2, threadcut have 3 only (:48-56, :152-159).
  - Coherence degradation bands 10-8 Stable, 7-5 Dissonant, 4-3 Fragmented, 2-1 Fractured, 0 Failure (:82-92).
  - TS-gated Coherence-0 outcomes: TS 30-49 Stirring = ontological freefall; 50-69 Attuned = relational persistence (Knots load-bearing); 70-89 Sensitive = structural reconstitution; 90-100 Resonant = full reconstitution plus reality-strain (:96-138). These band numbers are a numeric table a CHAR/DICE lane may find hard-coded elsewhere [UNVERIFIED].
  - The campaign arcs for Vaynard, Almud, Lenneth at Coherence 0 must specify TS and acknowledge reality-strain (:161-163).
- **Conflicts / stale:** this file's Amendment 5 says threadcut beings = layer 3 only; `02_canon_constraints.md` P-06 says "Threadcut beings have no layer 2" and "Coherence does not apply" while the foundations rules A9 say threadcut "lack layer 1" (:68 of the rules file) — three superseded sources disagree on which layer threadcut lacks [UNVERIFIED what canon/philosophy/04 states].
- **Open items:** none; superseded.

### canon/02_canon_constraints.md
- **What it is:** P-01..P-15 canon constraint table (§A) plus GD-1..GD-3 game design constraints (§B); 95 lines.
- **Status:** "SUPERSEDED — 2026-09-07 ... §A by canon/philosophy/ (10_constraints.md); §B by canon/04_game_design_constraints.md" (:1-31). Reading: superseded; the live P-01..P-15 text is `canon/philosophy/10_constraints.md`.
- **Bears on:** all subsystems (every design is checked against P-01..P-15), CORE, FA, WR, DICE, PROCESS.
- **Content that matters:**
  - P-01 Inseparability (all three dimensions co-move, no GM discretion to skip) :42; P-02 Monstrosity grounded in the Lacanian Real :43; P-03 Rendering = consciousness-performed, "GM is the rendering engine" :44; P-04 Monstrosity ontological not moral, no alignment system :45; P-05 three emergence modes mechanically distinct, Mode 2 is an event not an entity :46; P-06 threadcut beings :47; P-07 Calamity rendered-side, ground never "responds" :48; P-08 barrier = inaccessibility not suppression :49; P-09 memory pulling messy and detectable :50; P-10 Coherence indexes commensurability with human-mode being :51; P-11 Temporal Disjunction universal :52; P-12 drift propagation tridimensional :53; P-13 Forgetting = rendering failure :54; P-14 board/VG modes must express inseparability :55; P-15 three-layer being-persistence, Leap needs a vulnerability window :56.
  - Violation Tests are phrased as yes/no questions per constraint (e.g. P-15: "Does any mechanic allow Coherence 0 with no consequence, or a Leap without a vulnerability window? -> FAIL").
  - GD-1: Peninsular Sovereignty is the sole victory condition (all 15 territories, Accord >= 2, Political Stability <= 6, sustained 2 seasons); code must route through a single `peninsular_sovereignty()`; `victory_paths` in `registers/mechanics_index.yaml` holds exactly one entry (:70).
  - GD-2: deterministic threat response precedes stochastic action selection (mandatory Muster at Accord <= 3 ungarrisoned, Govern at Accord <= 2 garrisoned; up to 3 per season) (:71). GD-3: Revolt -> Insurgency -> Faction pipeline (:72).
- **Conflicts / stale:** P-03's "GM is the rendering engine" contradicts the current "no GM, engine resolves everything" framing (CLAUDE.md); P-14 cites Foundations §21.1/§22.2 which do not exist in `00_philosophical_foundations.md` (that file ends at §18). GD-1..GD-3 reference `designs/`, `sim/world/insurgency_pipeline.py`, "Accord", "Political Stability", `valoria_hooks.py`, board-game vocabulary for dissolved trees; the Level-4 hooks are "[PROVISIONAL — pending]" (:80-82). FA/CORE should check whether the season loop honours GD-2/GD-3 at all [UNVERIFIED].
- **Open items:** the three hooks never landed per this file.

### canon/02_foundations_amendment_leap_mechanism.md
- **What it is:** 2026-04-20 amendment: the Leap as suspension of the reflexive facing, involuntary directional knots, restorative/manipulative/destructive operation taxonomy, the Catastrophe as inversion of a manipulative operation, the Church's conflation, knot-profile tag; 120 lines.
- **Status:** "SUPERSEDED — 2026-09-07 ... chiefly 06_operations.md and 08_history.md"; banner: "Two of its claims were ruled against. The Calamity is tensile on a holding-against reading, not an inversion event; and the stabilizing tendency belongs to the futural-potential-legible rather than to substrate spooling" (:1-29). Reading: superseded.
- **Bears on:** WR, CHAR, PC, DICE.
- **Content that matters:**
  - Operation-type risk: restorative (Mending; Coherence cost zero), manipulative (Weaving/Locking/Pulling imposing non-prior states), destructive (dissolution); "scale makes destructive worse, alignment makes restorative non-corrosive" (:62-76).
  - Knot-profile tag per Leap-formed knot (operation type, target, formation context) with four mechanical consequences: Coherence-event propagation, passive seismographic awareness of Mending Stability (MS), vulnerability triggers (Coherence checks Ob 1-2), relational propagation (Coherence-band drop -> MS -1 per knotted territory; practitioner death -> MS -2) (:98-112).
  - Church persecutes Wardens (Edeyja) though Mending is non-corrosive (:88-94).
- **Conflicts / stale:** the "Catastrophe as inversion" account (:78-84) is the claim ruled against; `canon/03_canonical_timeline.md` still carries the inversion wording (:22), so the live timeline conflicts with the ruling unless RULINGS says otherwise [UNVERIFIED]. MS/Mending Stability clock and `designs/threadwork/` references point to dissolved trees.
- **Open items:** none; superseded.

### canon/03_canonical_timeline.md
- **What it is:** canonical setting chronology (pre-history through 245 AG game start), starting clocks, key figures, faction starting values, conflicts-resolved table; 198 lines, updated through 2026-11-08 (Schoenland neutral, ED-IN-0356).
- **Status:** "Canonical reference document ... canonical for setting chronology" (:1-4). Reading: live (listed as live in `canon/README.md`).
- **Bears on:** WR, ARCS, FA, CHAR, SE.
- **Content that matters:**
  - Calendar AG = After Solmund; Einhir Catastrophe ~12 years before 0 AG; Solmund emergence ~12 years (5 coalescing + 7 ministry); dissolution 0 AG; Church forms 0-200 AG; Altonian colonial period and Church containment ~50-200 AG (Himmelenger cathedral city); Secession Wars ~195-200 AG; deed-monarchy; informal caste of southern Einhir; GAME START 245 AG (:16-122).
  - Game-era table: first Almqvist reigns ~200-218; hunting accident ~218 (perpetrator TBD, E-01); Almud ascends ~218; Almud marries Lenneth ~220 (children Elske, Torben); direct Altonia trade 238 via Elske's marriage to Doux Alexios Laskaris (:114-122).
  - Starting clocks: MS 72 (Strained), CI 22, IP 20 (Dormant) (:129-133). Key figures with parallels (Almud TS 0; Lenneth institutional Einhir revivalist; Himlensendt keystone; Baralta Hafenmark Henry-VIII; Vaynard Varfell Von Lohengramm; Ehrenwall Löwenritter) (:136-145).
  - Faction starting values on a 1-7 scale are "board-game-era ... kept as history"; Niflhel dissolved, "Revolution" = Restoration Movement; "Faction-wide stats are not engine quantities (architecture/meta/01_AXIOMS.md T-a)"; live roster of polities is `references/names_index.yaml` `token_class: faction` rows (:146-153).
  - Schoenland is a neutral offshore trade nation, not a faction; persons act from their own seats, no GM (:166-167).
- **Conflicts / stale:** internal: "five years of Solmund's presence" (:48, :70) vs "five years coalescing, seven years ministry (twelve)" (:32, :190). Catastrophe described as "configuration inverts" (:22) vs the Calamity ruling (see above). The "Standing Editorial Items" E-01 (assassin) and E-03 (calendar name) remain TBD. Starting clocks MS/CI/IP are board-game clocks; whether the season loop carries them [UNVERIFIED]; per L3/T-a "stored aggregate" such clocks are disallowed as fields. Header says "Last updated 2026-04-11" but contains a 2026-11-08 edit.
- **Open items:** E-01, E-03.

### canon/04_game_design_constraints.md
- **What it is:** GD-1..GD-3 extracted verbatim from `02_canon_constraints.md` §B on 2026-09-07; 52 lines.
- **Status:** "CANONICAL (mutable canon — updates require explicit ratification logged in the editorial ledger)" (:3). Reading: live in status, but content is board-game-era and its hooks are provisional.
- **Bears on:** FA, CORE, SE, MB.
- **Content that matters:**
  - GD-1 sole victory = Peninsular Sovereignty (15 territories, Accord >= 2, Political Stability <= 6, 2 seasons); 8 faction-specific alternates STRUCK; single `peninsular_sovereignty()` (:27).
  - GD-2 mandatory-actions pass precedes stochastic action selection; mandatory pool Muster/Govern (:28).
  - GD-3 insurgency emerges from 2+ contiguous Uncontrolled territories for 2 seasons; promotes to Faction at L>=3, 2+ territories, Accord>=4 sustained 2 seasons; PT<3 -> Restoration Movement variant (extra-parliamentary) (:29).
  - Level-4 hooks `h.victory_singularity_check`, `h.mandatory_action_precedence`, `h.insurgency_invariant_check` are "[PROVISIONAL — pending]" (:35-39).
- **Conflicts / stale:** all three are framed in a faction-as-actor, territory/Accord/Political-Stability vocabulary which L1/AX-1 (only persons act; no stored faction aggregates) and the architecture's refusal of faction-wide stats contradict: GD-2's "faction action-selection" runs a faction chooser; "a faction acts" is a ruled refusal in `holonic_ARCHITECTURE.md` L1. FA lane should name this conflict and not resolve it. Cross-references (`designs/`, `sim/world/`, `params/factions.md`) are dissolved paths. "Victory" as a game-end condition: whether the season loop evaluates `peninsular_sovereignty` anywhere [UNVERIFIED; grep `peninsular` in `engine/`].
- **Open items:** the three hooks; GD-3 pipeline "pending Pass 2l" never built per this file.

### canon/README.md
- **What it is:** index of `canon/`; 39 lines.
- **Status:** none stated. Reading: live index.
- **Bears on:** PROCESS, WR.
- **Content that matters:**
  - `philosophy/` is Rank 1 and "the live statement of the framework's metaphysics, ontology and phenomenology"; `RULINGS.md` governs where any document disagrees (:7-9).
  - Five superseded files retained for ~70 citations: 00_philosophical_foundations, 00_..._rules, 01_amendment, 02_canon_constraints, 02_amendment_leap; concordance at `philosophy/00_standing.md` §0.4 (:17-32).
  - "A note on immutable": the old claim of immutability was wrong; what is durable is the record of decisions (`RULINGS.md`) (:34-39).
- **Conflicts / stale:** CLAUDE.md §3 says canon/ holds "foundations P-01..P-15, timeline, constraints, amendments; world truth only"; the README itself says the amendments are superseded.
- **Open items:** none.

### canon/philosophy/00_standing.md
- **What it is:** §0 of the philosophy suite: standing/precedence rules, lineage table of borrowed traditions, and the old-section -> new-section concordance; 197 lines.
- **Status:** "PROPOSED" (:3); text itself says it is a reference document, "not a mechanism" (:10-15). Reading: live reference (the `canon/README.md` calls the suite Rank 1), though the `Status: PROPOSED` line was never flipped.
- **Bears on:** PROCESS, WR.
- **Content that matters:**
  - Self-limiting standing: "If it were deleted, nothing in the world would resolve differently"; authoritative only for intent, history, vocabulary (:10-18). "Numeric bands are not foundations": TS thresholds, Coherence tracks, obstacle numbers are mechanism and are marked for relocation, not reproduced (:25-29).
  - Precedence rule: this suite is sole owner of claims it states; sources own unabsorbed content; absorbing documents must mark absorbed sections superseded in the same change; "Restatements are forbidden" - every drift entered through a hand-written restatement (:42-60).
  - Lineage: Husserl, Kant (apperception, previously misattributed to Husserl), Heidegger (ontical/ontological claim "withdrawn"; Welt weltet; coprimordial), Derrida (always-already, trace, supplement; Ruled 2026-09-07 to name Derrida, Kant, Freud/Jentsch), Kierkegaard, Lurianic Kabbalah (agency stripped), Lacan (Real redefined as plenitude), Whitehead/Bergson, apophatic theology (:74-85). Four pivots and whether their debts are paid (Real paid by §5.3 finitude; epoché paid; Ein Sof partially; ontological difference NOT paid) (:87-115).
  - Concordance table old F/A/L/R/C section -> new section; L Am. 6 (knot-profile tag), R A1-A15 and GD-1..GD-3 are "Not migrated" (:147-195).
- **Conflicts / stale:** Status line "PROPOSED / Supersedes: nothing yet" (:3-4) while `canon/README.md` and the sibling banners treat the suite as superseding the five files. Outstanding scholarship correction: the as-structure (Auslegung) appears in no lineage row (:78).
- **Open items:** the Heidegger as-structure row owed (:78).

### canon/philosophy/01_limit_and_ground.md
- **What it is:** §1 The Limit and the Ground: epistemic opacity charter, regress, Ein Sof, contraction, no agency; 129 lines.
- **Status:** "PROPOSED" (:3). Reading: live reference.
- **Bears on:** WR (cosmology constraints), PROCESS.
- **Content that matters:**
  - Charter: no causal claim about the ground's constitution/response is supportable; ruled R-19 2026-09-09 that the grounding is "always withdrawing", a receding limit (:13-28). "That the ground gives" is allowed (evidenced by becoming); "how or why" is forbidden (:30-41).
  - Ein Sof reading restated as a regulative inference from the rendered side ("what comes through presents as surfeit"), not a description (:74-84). The contraction is "originary and uncaused" (Ruled 2026-09-07) (:93-105).
  - §1.5 the ground does not act, intend, respond, prefer or tend; three forbidden formulations incl. a spooling "tendency" (:107-126) - the P-07 root.
- **Conflicts / stale:** none within lane; the forfeit of an origin story is stated openly (:58-62).
- **Open items:** none.

### canon/philosophy/02_threads.md
- **What it is:** §2 Threads: dual role, configuration defined, coprimordiality, intelligibility, temporality, actualized dimension, Inseparability, Temporal Disjunction; 253 lines.
- **Status:** "PROPOSED" (:3). Reading: live reference (rulings 2026-09-07 and 2026-09-09 inline).
- **Bears on:** WR, DICE (P-01/P-11 grounding), CHAR.
- **Content that matters:**
  - Threads "are not literal threads"; imagery gestures at essence (Ruled 2026-09-09) (:11-16). A configuration = "an organization or cohering of threads such that they come to constitute a being or entity" - its boundary is the being (:25-32).
  - Substrate and conditions are coprimordial (Heidegger gleichursprünglich); chain "Threads comprise beings. Beings have consciousness. Rendering occurs due to conscious beings" (:34-64). Inseparability is the acknowledgement that the constituting/constituted distinction was never stable (:87-95).
  - Temporality is one dimension; splitting it is "a metaphysical violation" (Ruled 2026-09-07); a temporal operation does not rewind time, it pulls a configuration out of its own becoming in equilibrium (:132-153). The three dimensions are closed: that (actuality), when (temporality), as-what (intelligibility); "where" is imbrication (:174-183).
  - Inseparability governs WHICH dimensions move (all); operation type governs DIRECTION relative to the tendency; "restorative" must not be defined by return to a prior actualized state (:208-217).
  - Temporal Disjunction is a relation between configurations (witnessed, local); scoped 2026-09-09 so restorative operations produce none, and ordinary experience carries none; distinct from Coherence's temporal facet (:219-253). This narrows P-11 ("universal").
- **Conflicts / stale:** §2.2 defers "what a thread is when nobody renders it" to §3.5 (:102-111).
- **Open items:** none.

### canon/philosophy/03_rendering.md
- **What it is:** §3 Rendering: constitutive process, dual consequence, passive stratum, stabilizing tendency (futural-potential-legible), positional constitution through imbrication; 239 lines.
- **Status:** "PROPOSED" (:3). Reading: live reference.
- **Bears on:** WR, DICE, FI (epistemics), CHAR.
- **Content that matters:**
  - Rendering = "the ability for consciousness to interpret phenomena as meaningful"; nothing is prior to it; one cannot decline it; rendering does not configure, spooling does (Ruled 2026-09-09) (:11-42). Constitution/experience, not appearance/reality (:44-48).
  - Passive stratum (pre-predicative) explains the residue of a confrontation, seismographic awareness, the primitive system; "not actively constituted; passively registered as trace" (:84-111).
  - Stabilizing tendency belongs to the threads ("what threads are like", not an action); equilibrium target is the futural-potential-legible; Locked Zones = becoming precluded, threads no longer moving toward equilibrium; Mending = restoration of becoming (:113-188).
  - §3.5 rendering is positional: a person is a position within the weave constituted by imbrication; shared reality = overlap of imbrication; disagreement is not error (:190-239).
- **Conflicts / stale:** retires "Providence" as a name for the tendency (kept for emergence Mode 2, per 04 §4.6).
- **Open items:** none.

### canon/philosophy/04_being_persistence.md
- **What it is:** §4 Being-Persistence: three layers, derivation of layer 2, Coherence defined, Coherence-0 not threadcut, threadcut beings, three emergence modes, orphaned configurations; 295 lines.
- **Status:** "PROPOSED" (:3). Reading: live reference; settles which layer threadcut lacks.
- **Bears on:** CHAR, PC, WR, DICE.
- **Content that matters:**
  - Layers: 1 spooling (configures), 2 self-rendering (gives human shape, "continuous, unconscious, default" - not "always-already"), 3 deliberate threadwork (:13-35). Derivation of layer 2 (:37-79).
  - Coherence is "a distance, not a quantity" and everyone has it; practitioners differ by spending it; communal life protects by holding and mending; the isolated drift faster (:81-147); orthogonal to TS but contingently correlated through confrontation (:142-147).
  - Layer-profile table: organic 1+2; Coherence-0 shallow 1; Coherence-0 deep 1+3; threadcut 3; Locked Zone 1+2 with becoming precluded (:160-166). Settles the superseded files' disagreement: "Threadcut beings lack layer 1" (:154).
  - Threadcut beings are singular and alien (not "a human minus one layer"); their cost never eases - "immortality is unremitting labour" (:173-230). A struck derivation (persistence partly supplied by others' rendering) was never ruled (:222-230).
  - Mode 1 ordinary incursion, Mode 2 Providence (an event, not an entity), Mode 3 threadcut; Mode-3 organization is radically opaque (:232-281).
  - Orphaned configurations decay because removing causal history removes accumulated spooling depth (:283-295).
- **Conflicts / stale:** none found; this is the resolution file.
- **Open items:** none.

### canon/philosophy/05_confrontation_and_sensitivity.md
- **What it is:** §5: monstrosity, rendering's limit, finitude pivot, development of sensitivity, what sensitivity is (a band of sensing across three axes), epistemic barrier, transmission as religious poetry, deepening vs destabilization; 369 lines.
- **Status:** "PROPOSED" (:3). Reading: live reference.
- **Bears on:** CHAR, WR, FI, PC (monster encounters), DICE.
- **Content that matters:**
  - Monstrosity is ontological; "being moral requires being human" so calling a monster evil is a category error (:9-31). Sensitivity captures more of the surfeit without commensurability ("two dimensions can represent three") (:33-50).
  - Confrontation trauma-signature is a theorem of the two-stratum rendering; "A larger cup is still a cup" - growth changes how much, not what kind (:74-137, :261-298).
  - Sensitivity cuts both ways: greater reach holds more of an encounter and is reconfigured more ("sensitivity is not armour"; "the exposed are not the ignorant; they are the ones who can see") (:154-179).
  - Thread sensitivity = how far outside the human band one can sense (Ruled 2026-09-09: window analogy; 40-60% -> 10-90% range); practitioners are not tied to more threads; perceptual reach and self-holding are one variable; imbrication is the engagement side (:181-259). §6.8 cost account answered "under a misunderstanding"; whether reach bears on cost is OPEN (:291-297).
  - Epistemic barrier = inertness not amnesia; non-sensitives retain thread knowledge and cannot render it (Ruled 2026-09-07) - the rewritten P-08/P-13 basis (:299-329).
- **Conflicts / stale:** `02_canon_constraints.md` P-13 ("Forgetting = rendering failure") framed as forgetting, now contradicted; `canon/03_canonical_timeline.md` still uses "the Forgetting" as a named event (:22, :66) - CHAR/FI lanes should treat the Forgetting as inertness, not memory loss.
- **Open items:** the retracted cost consequence; "does reach bear on what a working costs" (:291-297, deferred to §6.8).

### canon/philosophy/06_operations.md
- **What it is:** §6 Operations: what an operation is, the Leap, knot formation, knotting/wrapping, collective work, operation-type taxonomy, memory operations, and the unified Coherence-cost account; 402 lines.
- **Status:** "PROPOSED" (:3). Reading: live reference; carries the richest mechanism-adjacent intent for threadwork cost.
- **Bears on:** CHAR, PC, WR, DICE (cost model), FI (investigation of Gaps).
- **Content that matters:**
  - Operation = "threadwork that requires going beyond oneself as a finite ordinary human"; layer-2 self-maintenance is threadwork but not an operation; every operation requires a Leap; ordinary experience carries no Temporal Disjunction (:14-57).
  - The Leap suspends the reflexive facing only; layer 1 and the outward facing continue; "an entire suspension of all grounding" struck; not a veil-lifting filter, a change in the *as* (:61-127). Epoché analogy owned: the Leap forfeits the reduction's safety (:119-125).
  - Knots form involuntarily along the operation channel, are directional, bidirectional in effect, permanent, below the reach of re-engaged self-rendering; permanence is a posit, wrapping would have been compatible (:129-152).
  - Taxonomy by direction relative to the futural-potential-legible: restorative (needs no holding), manipulative (held by the practitioner), destructive (unmakes harmony; target's dependents orphaned); "scale makes destructive worse, direction makes restorative non-corrosive at any scale" (:179-214). Mending restarts becoming in a Locked Zone; a whole Locked Zone can be Mended without self-defeat if it is restoring equilibrium, not "restoring a remembered state" (which is the Calamity's mechanism) (Ruled 2026-09-07) (:216-247).
  - Coherence cost has two channels: operational (type x scale, held shape borne by the practitioner) and confrontation (environmental, non-accumulating); restorative work moves the practitioner toward their own equilibrium and self-mending can reach the resting point ("extremely difficult but possible", Ruled 2026-09-08) (:270-330). Practitioner-side resilience = strength of configuration, not sensitivity or imbrication (Ruled 2026-09-09) (:333-350).
  - Retention roll reconciled: Leap risk = environment x duration plus type x scale; "A Mending in a quiet place is genuinely free. The same Mending at a Gap margin is not" (:373-402).
  - The target of a manipulative operation also bears Coherence cost (:266-268).
- **Conflicts / stale:** the word "retention" is used for both the phenomenological term and a dice check (`09_terminology.md` §9.2 says the check should be renamed; this file still says "retention roll", :373). `canon/02_foundations_amendment_leap_mechanism.md` said destructive/manipulative cost are catastrophic and Mending zero; this file adds "understated" (restorative is positive).
- **Open items:** whether the load is split between Coherence and substrate strain (flagged in 07 §7.5); the knot permanence posit (:143-146); the "retention roll" rename.

### canon/philosophy/07_drift.md
- **What it is:** §7 Drift: elastic/plastic Coherence model, point of no return, amorality, what produces drift, phenomenology, propagation, observable bands, reality-strain, Coherence-0 reach-gated trajectories; 497 lines.
- **Status:** "PROPOSED" (:3). Reading: live reference; the most mechanism-shaped foundations file.
- **Bears on:** CHAR (practitioner state), DICE (any Coherence/TS track), WR, FA (drift through community), ARCS (Vaynard, Almud, Lenneth arcs at Coherence 0).
- **Content that matters:**
  - Coherence is DISTANCE from the human equilibrium, not a depleting store; stress displaces the configuration elastically below a threshold and plastically above it, moving the RESTING POINT; the elastic range is a constant of the being; only events deform (no creep); recovery is return over time conditioned on environmental equilibrium, accelerable by mending; sensitivity accrues from exposure independent of stress (:9-74).
  - Purpose: "Coherence loss exists to make repeated threadwork expensive"; it must bite and must be answerable (rest and mending) (Ruled 2026-09-08) (:83-99).
  - Two quantities: resting point (moves by permanent set; returns only by deliberate restorative threadwork aimed at the configuration) vs present displacement (returns with rest); eventual crossing out of the human band: "they became other"; past it, working them back to human is restoring a remembered state, i.e. manipulation (:101-170). A veteran presents further gone under the same load without being more fragile (:143-148).
  - Drift is amoral not neutral ("being moral requires being human"); drifted beings retain preferences and attachments as post-human sensibilities not boundable by human language; no alignment, corruption track or good-to-evil arc (:172-236).
  - Propagation through two channels: rendering (presence-based) and knots (relationship-based, distance-independent; exile does not protect kin); exposure is bivalent: sensitivity accrues cumulatively, drift only by event (:288-330).
  - Observable bands: Stable, Dissonant, Fragmented, Fractured, Coherence failure; "numbers are mechanism and not owned by this document"; bands read present displacement except the last; written from the observer's side (:332-380).
  - Reality-strain: Coherence-0 deep-reach beings, also every manipulative operation (posit, unresolved) and threadcut beings like Solmund, strain the substrate; Coherence 0 outcomes gated by perceptual reach AT THE MOMENT OF PERMANENT LOSS (freefall / relational persistence / reconstitution / reconstitution-and-strain); it gates self-comprehension as well (Ruled 2026-09-07) (:382-497).
- **Conflicts / stale:** §7.5's split-load posit vs its rival (all load on practitioner while Coherence remains) flagged unresolved (:409-412). Superseded canon files give numeric TS bands 30/50/70/90 that this file refuses to own; whether any code carries them [UNVERIFIED]. P-11 vs §2.7 scope: restorative ops produce none.
- **Open items:** "what is owed to a being outside the moral register" deliberately unanswered (:231-232); how much strain remains per operation with Coherence remaining.

### canon/philosophy/08_history.md
- **What it is:** §8 History as a worked case: the Calamity, what came through, relational lattice, cascading collapse, Gaps, Locked Zones, Solmund, the Church, the prophylaxis, the Church's category error, the betrayal; 410 lines.
- **Status:** "PROPOSED" (:3). Reading: live reference; resolves the Calamity-mechanism and Church-worship questions.
- **Bears on:** WR, ARCS, FA (Church, Löwenritter, Einhir politics), CHAR.
- **Content that matters:**
  - Ruled 2026-09-07: the Calamity is TENSILE on a holding-against reading; "Catastrophe" usage retired; the "directional inversion mid-execution" account is NOT canon (:13-57). The Einhir held a refined arrangement the configurations did not tend toward; it broke "as a balance" taking every associated configuration with it (:42-57).
  - Surfeit flooded the opening; forms are explained at §4.6; the claim that threadcut beings came through is struck (:59-83). Cascade is physical, epistemic, temporal, relational (:102-120).
  - A Gap is an absence where something should be (a standing breach in the boundary or the hole where a configuration was removed); not the same as a Locked Zone (Ruled 2026-09-07) (:122-145). Locked Zone = becoming precluded; persists "in a thousand years"; people inside do not accumulate; substrate-side fact (:147-191).
  - Ruled 2026-09-07: THE CHURCH'S GOD IS SOLMUND (not the Ein Sof); a category error, not a deception; Solmund ceased the work (no external cause), strained reality throughout, misread as miracle (:229-285). Prophylaxis derivable from what Solmund was (unchanging, all-knowing, determining) (:307-320). The moral question about Solmund is "malformed" (non-human, outside the register) (:352-366).
  - Church persecutes Wardens (Mending) on the same grounds as manipulative practitioners; sincere but structurally incorrect (:369-392). Northern Einhir betrayal is epistemological as much as political (:394-410).
- **Conflicts / stale:** `canon/03_canonical_timeline.md` (:22) still says the configuration "inverts"; and `canon/philosophy/08` itself retired the "Catastrophe" name while the timeline's heading is "The Einhir Catastrophe" (:21). Timeline also says Solmund "ministry ~7 years / 12 total" while §8.7 says "active for a generation or less" and the Church takes "two to three centuries" vs the timeline's ~200 years [UNVERIFIED which timing the setting wants]. §8.3 retracted paragraph on "larger vessel".
- **Open items:** whether Solmund understood what was made of him; whether his presence also catalysed flourishing (:359-364).

### canon/philosophy/09_terminology.md
- **What it is:** §9: the ontical/substrate/ontological scoping, process-vocabulary discipline, the vocabulary reference table; 127 lines.
- **Status:** "PROPOSED" (:3). Reading: live reference (vocabulary owner for the suite).
- **Bears on:** PROCESS, WR, CHAR.
- **Content that matters:**
  - Ruled 2026-09-07: re-scope the word; "ontological" reserved for the disclosure register (rendering, layer 2); thread-constitution is called "substrate" (normally inapparent, ontic, not a deeper layer); thread sensitivity has two aspects of one capacity (:27-47).
  - Process vocabulary: idempotent in meaning, idiomatic in choosing (mirrors CLAUDE.md §4); recorded collisions: Calamity/Catastrophe (standardized: Calamity), retention vs "retention roll" (rename owed), Providence (kept for the mode, retired from the tendency) (:64-86).
  - Vocabulary reference table: Threads, Rendering, Ein Sof, Configuration, Spooling, Layer 1/2/3, Threadwork, Operation, Threadcut, Coherence (present displacement vs resting point), Drift, Thread Sensitivity, Confrontation, Leap, Knotting, Wrapping, Operation type, Orphaned configuration, Temporal Disjunction, Reality-strain, Equilibrium, futural-potential-legible, Imbrication, Providence, Gap, Locked Zone, Harmony, Apperception, The Real (:90-121).
- **Conflicts / stale:** the vocabulary re-states other sections (the suite's own rule 4 against restatements, `00_standing.md` §0.2); apperception gloss corrected as Kant's (:123-127).
- **Open items:** the "retention roll" rename (:79-82).

### canon/philosophy/10_constraints.md
- **What it is:** the live P-01..P-15 canon-constraint table (regenerated against the suite's numbering) with violation tests; 53 lines.
- **Status:** "PROPOSED" (:3). Reading: live; this is THE statement of P-01..P-15 that lanes check against (CLAUDE.md names `valoria-canon-guard`).
- **Bears on:** all subsystems (every design is checked against P-01..P-15), WR, CHAR, DICE, PROCESS.
- **Content that matters:**
  - Rules, each with a Ref and a yes/no violation test: P-01 inseparability (:25); P-02 monstrosity is surfeit not evil (:26); P-03 rendering constitutive, corrected to remove "GM is the rendering engine - there is no GM; the engine resolves" (:27); P-04 monstrosity ontological, ground: being moral requires being human (:28); P-05 three modes distinct by layer profile (:29); P-06 threadcut lack layer 1, Coherence does not apply (:30); P-07 the ground has no agency AND spooling has no direction (new clause) (:31); P-08 barrier is inertness not amnesia - "Does any mechanic make non-sensitives forget? -> FAIL" (:32); P-09 memory operations messy, costly, detectable (:33); P-10 Coherence indexes commensurability (:34); P-11 Temporal Disjunction universal across operations, scoped so restorative ops produce none (:35); P-12 drift propagation tridimensional through two channels, knots distance-independent (:36); P-13 ontological knowledge not transmissible as propositional content (:37); P-14 every play mode expresses inseparability (:38); P-15 three-layer persistence, deep vs shallow reach not identical, Leap not uniformly risky (:39).
  - "Numbers are out": no constraint may name a threshold (:13-15). GD-1..GD-3 and the Level-4 hook table not reproduced (:43-53).
- **Conflicts / stale:** P-11 text reads "universal across operations. Every operation produces some" and the note scopes it so restorative operations produce none: the headline and its scope disagree within one cell (:35). The older `canon/02_canon_constraints.md` P-08/P-13 "Forgetting" (retention instability) is contradicted. Whether the canon-guard skill (`valoria-canon-guard`) cites the superseded `02_canon_constraints.md` rather than this file [UNVERIFIED; one grep would show].
- **Open items:** none.

