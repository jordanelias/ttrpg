# Digest auditB5

## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Scope: 36 files of the hidden `.audit/` corpus (social-contest three-lens audit 2026-08-06, vector-audit metrics, world-churn audit 2026-08-08, code-leanness 2026-08-11, world-schema-gap audit 2026-08-11, degree census and reband scripts). All are ARCHIVED-NOT-CANON; leads, not facts. Working-tree checks are single greps, marked where not done.

Working-tree facts checked while reading (used below): `systems/social_contest/sim/contest/` still holds `resolver.py primitives.py modes.py wrapper.py faction.py agon_harness.py policy.py` etc.; `VALID_KINDS` is at `resolver.py:34` and still contains `"hard"`; `Stasis`-style `COST = {"advance":3,"hard":5,...,"support":2}` still at `primitives.py:51`; `ECHO_TRANSPORT` no longer appears in any `.py` (key/echo substrate retired, ED-IN-0232); no `parliamentary_stay.py` or `scene_dispatch.py` remains in the tree (only `engine/substrate/composition.py` mentions the name `scene_dispatch`); `modules/social_contest/` now exists as the registered module.

---

### .audit/2026-08-06-social-contest-three-lens-audit/02_system_vs_proposals_overview.md
- **What it is:** orientation/comparison document, 2026-08-06, lane SC (ED-SC-0017..0022 reads); compares the live social-contest system with three uploaded political-mechanics proposals (P1-P45, state graphs S1-S8, consolidation M1-M14).
- **Status:** "PROPOSED — orientation companion to `00_synthesis.md`; no design text changed". Reading: historical; its method/inventory is useful, its adoption ranking was partly retracted by file 03 (warrant x attack matrix).
- **Bears on:** SC, FA, WR, CORE, DICE.
- **Content that matters:**
  - Names the "three resolution models under one name": Model A canonical prose exchange algebra (`social_contest_v30.md` 1-12), Model B the promoted kernel (`systems/social_contest/sim/contest/`, move-from-budget, adv scalar, banded at close), Model C the legacy stub; "overlap nowhere except the Persuasion Track's band thresholds" (:51-63).
  - Kernel inventory (:68-78): dsigma kernel with tanh cap (M_MAX=1.5 sigma, TN7), stasis ladder of six, appeal x tense 3x3 `RhetoricalWeights`, resonance/leak, `Readiness`/`Room`, `Reserve`, hidden-weight Dossier, Nyaya fault/clinch catalogue, `Pressure`, five-six win-condition families.
  - Measured overlap of proposals with live system (:285-291): 0 of 45 primitives fully present, 13 partial, 21 absent in-lane, 8 other lanes, 3 contradicted (P4 Immunity, P10 Forum Challenge, P41 Scaled Compromise).
  - Tier 1/2/3 cut list (:345-380), ~800 lines: strain/Charisma/Rattled sub-economy, superseded `social_contest_system_v2.md`, 9 non-canonical venue presets, Appraise channel (a), Contest Fatigue, `CONCENTRATION_MULTIPLIER`; consolidate four bonus dice onto Dossier, faction boost onto `Pressure`, Casual Dispute onto Personal Appeal; retire three-mode TTRPG/BG/Hybrid tripartition.
  - Part VI (:389-408) runs the expressibility test: what M1-M14 cannot express (dsigma cap, appeal x tense resonance, leak, fault/clinch, Pressure, Readiness/Room, Persuasion Track compromise band) - "adopting wholesale would be an amputation"; adopt the discipline (separation rule, single-owner composition, `gate(burden)`), Record spine, M2 Scope, opposition model.
  - One-sentence verdict (:493): "Valoria built a better engine than the proposals describe and a worse memory than the proposals require."
- **Conflicts / stale:** (a) Treats warrant x attack matrix (:235, :444) as a strongest contribution - retracted by file 03 as fabricated. (b) References `ECHO_TRANSPORT` default ON, Domain Echo, `LedgerTag` at `systems/settlements/sim/ledger.py` (:91, :428); the echo transport is retired and I found no `class LedgerTag` by grep [UNVERIFIED that the ledger itself is gone]. (c) Says no player-visible interface thinking in any of the three uploads; unchanged claim. (d) "Casual Dispute = Personal Appeal" and 8 proceedings: [UNVERIFIED] at present modes.
- **Open items:** the two forks ED-SC-0020 and ED-SC-0021 left to Jordan (:530); "prototype the contest loop on paper with twenty claims and four bodies" (:500) - nothing seems to have answered.

### .audit/2026-08-06-social-contest-three-lens-audit/03_persuasion_documents_adjudication.md
- **What it is:** adjudication/retraction document, 2026-08-06, lane SC, ED-SC-0025; three Fable lenses + Opus synthesis, on two later source documents (doc 4 retraction, doc 5 N1-N20 primitives).
- **Status:** "PROPOSED — findings filed; amends CIP-2 and ED-SC-0021". Reading: historical; the fabrication-split and `hard`-dominance findings are the load-bearing parts.
- **Bears on:** SC, DICE, FA, FI, CHAR.
- **Content that matters:**
  - The warrant x attack vulnerability matrix is FABRICATED (unsourced assignments); the three-attack taxonomy (Undermine/Rebut/Undercut, Prakken) is sourced and survives (:36-44). The "40% authoring invariant" survives only relabelled as an own `[SEED]` threshold (:45-51).
  - Story model (coverage/coherence/uniqueness) does not satisfy principle C-1 (no fixed scalarizer); invention just moved into function bodies (:53-78).
  - Klei/Griftlands refutation lands on the kernel: stationary always-full 7-verb menu resolving through a roll into one scalar `adv`; `logos_spammer` (same move forever) is a viable default sparring partner (:84-98).
  - Bug F9: `hard` costs 5 vs `advance` 3, executes byte-identical code after `SelfGating.licit`, and the harness sells it as "a bigger swing" (:103-111). **Still live at tree:** `VALID_KINDS` retains "hard", `COST["hard"]=5` (primitives.py:51).
  - N10 Deliberation is an extension of `VoteAtClose` ("today's VoteAtClose is formally a degenerate zero-round N10") and is blocked because `ContestView` shows audience as two booleans and `Panel` averages member discipline/character at ballot time (:167-186). N16 Attribution = second currency, post-close only (:188-206). Reject list N2/N14/N15/N18/N11/N4/N12 (:247-255).
  - Gap: deception unrepresentable - `EvidenceItem` is (ground, weight, appeal) with weight the hidden true value, no apparent-vs-true split, so forgery cannot be exposed (:262-268). Canon-vs-design bar: Guiguzi/Han Feizi material is T2 paraphrase, must not be cited as historical in ratified docs (:224-243).
- **Conflicts / stale:** CIP-2/CIP-11/CIP-12 and ED-SC-0021/0022 are proposals that may no longer exist as live objects [UNVERIFIED]. `agon_harness.py:327` "bigger swing" copy [UNVERIFIED now].
- **Open items:** CIP-11 Deliberation needs per-member exposure in `ContestView`/`Panel` first; Fork B annotation; whether any pick-entropy sweep for the three-attack taxonomy was ever run (file 05 says it was not).

### .audit/2026-08-06-social-contest-three-lens-audit/04_reductive_audit_primitives_and_foundations.md
- **What it is:** reductive (prune/cut/consolidate) audit, 2026-08-06, lane SC, ED-SC-0026; two Fable lenses (kill-list, foundations).
- **Status:** "PROPOSED — findings filed; several cuts collide with ratified items and need Jordan". Reading: historical lead list; the strongest foundational argument (§2) is still of interest.
- **Bears on:** SC, CORE, CHAR, DICE, FA.
- **Content that matters:**
  - §2 (:53-78): given the ratified Auto/Manual Duality (`E[auto] ~ E[played]`, "free of strategic advantage", `auto_manual_resolution_duality_v1.md:65`) and every contest output being a scalar stat delta, "auto-resolving every contest is strictly correct play"; played mode is wasted attention unless it shapes WHICH consequences occur (the Record spine, CIP-1).
  - §3 (:82-96): no foundational player choice: Style bet API-unreachable, appeal-vs-judge read illegible (`ContestView` shows two booleans), forum choice foreclosed by `social_contest_v30.md:39`. In the shipped campaign both sides are `logos_spammer` (`scene_dispatch.py:311`) (:38-40).
  - Irreducible set of 11 primitives (:100-117) and a K1-K15 kill list (:130-146) with "breaks:" column; ~1500-1700 lines identified; K2, K3, K9 and the genre kill touch Jordan-ratified items (ED-1060, ED-1062, ED-1056) so are escalated (:353-355).
  - Collinearity (:168-191): genre vs tense vs stasis ground; Orientation/Style die with the Doubt Marker; CONSEQUENCE and FEASIBILITY merge (stasis 6 -> 4-5). Domain Echo channel selection (Memory->Mandate, Projection->Influence) would re-key on ground tense.
  - Character layer (:197-212): of six attributes only `faculty` feeds `Pool.size` and `Leverage.net`; Cognition/Charisma/Attunement/Focus/Spirit/Recall have no SC consumer. Either ship the one line (`_as_contestant` maps proceeding primary attribute to `faculty`) or delete the table.
  - 24 configurations -> 4 types T1-T4 (:218-226). New incoherences (:256-278): DEFINITION tagged "past" (`primitives.py:16`) contradicts CR4; JURISDICTION sits 4th on an upward-only ladder but is ruled pre-merits; `support` spends 2 regains 4 (net +2) so Reserve cannot bind (:309-311).
  - Scores (:373-384): dramatic-legibility 0/3 at personal scale; Omega-Intent 4/4 FAIL (cross-scale consequence, personal transformation, autonomous world, non-dominance).
- **Conflicts / stale:** `scene_dispatch.py:311` and `wrapper.py:165-167` cites: `scene_dispatch.py` is not in the tree now [UNVERIFIED how the campaign now dispatches contests]. `COST["support"]=2` still at primitives.py:51 (regain value not checked). `HANDOFF_SC.md:164` / `CURRENT.md:151` "Stage 4 - four games - next" claim (:341-348) - [UNVERIFIED].
- **Open items:** reconciliation of the "Stage 4 four games" roadmap with the CIP programme; the duality doctrine's "chief build implication" (event-parameterising the auto-resolver to resolve specific slate motions) covered by no CIP (:346-349); CIP-11/12 have no wave; Nyaya-vs-scholastic grounding of the fault catalogue.

### .audit/2026-08-06-social-contest-three-lens-audit/05_track_architecture_and_state_graph.md
- **What it is:** requirements/track-architecture proposal (revised after adversarial audit), 2026-08-07, lane SC, ED-SC-0027/0028; Fable lenses + Opus authorship.
- **Status:** "PROPOSED (2026-08-07, ED-SC-0027; REVISED same day after adversarial audit, ED-SC-0028)". Reading: historical design proposal; superseded for headline claims by file 06's corrections which this text already incorporates.
- **Bears on:** SC, WR, FI, FA, SE, CHAR.
- **Content that matters:**
  - Corrected test for "one state written twice": A and B are one state iff at every reachable moment A is recoverable from B by a fixed rule AND carries no state anything reads; two riders (state which system the verdict is graded against; every withdrawal names its consumer) (:40-47).
  - Requirements C1-C4 (character: how/what/why/how effectively), P1-P4 (type: venue/adjudicator/verdict/audience), world interface W1-W7 (:60-122). Kernel status: C3 (why one argues) ABSENT; claim record ABSENT; the Bout kernel's whole world interface is `build_contest(parts[0], parts[1], venue=proceeding)` - two integers (:106-110); the parliamentary path (`parliamentary_bridge._derive_vote`, `mc_v18.py:148-151`) is a Mandate-pool roll, not the agon (:94-108).
  - Architecture: 8 in-bout tracks T1-T8, 8 interaction edges E1-E8 (Decorum, Leak, Readiness, Emotion precondition, Burden, Clinch, Clash, Gallery-vs-bench), config rows for Venue/hearer (:131-182). Lose the case, win the room: verdict and reputation route through different profiles (:506).
  - State graph (mermaid): Constitution -> Exordium -> TranslatioWindow -> Narratio -> Partitio -> StasisLoop -> Peroratio -> Verdict -> Settlement/Record (:276-296); phases as a venue mask.
  - Warrant schemes carry their own critical questions (Toulmin/Walton), replacing the retracted matrix, conditional on an unrun pick-entropy sweep (:231-246). Decorum f(proof-type x appeal x temporal, question, judge): "parameter count explodes" liability (:267-269).
  - Ledger finding (:459-464): `ledger_add` treats Reputation as SINGLE_VALUED by kind ignoring key, tags live on one settlement - no holder dimension; "one primitive, extended cross-lane, needs SE". 18 forks listed (:438-453); cross-lane commitments: W3 evidence producer -> FI (`investigation.py` all stubs), W5/W7 ledger -> SE, C3 -> characters, W2(d) -> FA (:455-458).
- **Conflicts / stale:** cites `ledger.py:31-32, 50-53`, `mc_v18.py:148-151`, `parliamentary_stay.py` "zero campaign callers" - no `parliamentary_stay.py` file now and `ECHO_TRANSPORT` is gone (retired substrate); `LedgerTag` grep returned nothing [UNVERIFIED]. `social_contest_v30.md:39` terminate-and-reinstantiate is quarantined in `.designs/`.
- **Open items:** the "lose the case, win the room" guard is "Not yet written" (:486-489); 18 forks unresolved; three independently derived "second currencies" (attribution CIP-12, disposition CIP-6, room impression) not reconciled as one axis or three (:522-524).

### .audit/2026-08-06-social-contest-three-lens-audit/06_adversarial_audit_of_05.md
- **What it is:** record of a three-critic adversarial pass (correctness, logic, elegance; `valoria-critic` read-only) against file 05, 2026-08-07, lane SC, ED-SC-0028.
- **Status:** "RECORD (2026-08-07, ED-SC-0028)". Reading: historical; useful as a method exhibit (an author-written falsifier that was never run).
- **Bears on:** SC, PROCESS, CORE.
- **Content that matters:**
  - Method result: ~25 checkmarked citations hand-verified across two critics, zero misquotes (:19-32); 22 ranked errors (:46-71).
  - Headline error: "sealed off from the world" false - `mc_v18.py:148-151` ran `parliamentary_bridge` every season, `_derive_vote` generates a topic from world pressure, `parliamentary_vote.py:206-216` writes `world.factions` (:50). Claim narrowed to "the Bout kernel is sealed".
  - "No new primitive" false: `ledger_add` makes Reputation `SINGLE_VALUED` by kind ignoring `key`; no holder dimension, factions have no ledgers (:53).
  - Duality trilemma: if auto = headless kernel (Fork A RULED) then either playing shapes nothing in expectation or the player mode-shops in consequence space; escape is unratified CIP-9b (:52).
  - `FactionBoost` has NO resolution consumer in code - the +1D is prose-level (:35); `Reserve` net-positive (:36); the warrant-vs-appeal reversal and FactionBoost-to-disposition rescue were motivated reasoning / category error (:57-58).
  - Methodological lesson (:81-91): a duplicate-vs-distinct test is decidable only against a FIXED system; grading kills against what exists and rescues against what is proposed converts a pruning instrument into a licence; naming a falsifier is not running it (§0.1 pt 3).
- **Conflicts / stale:** `ECHO_TRANSPORT` default-ON premise gone with the retired echo/key substrate; ledger cites unverified at tree [UNVERIFIED]. Citations to `resolver.py` lines have drifted (VALID_KINDS now `resolver.py:34`, was `:32`).
- **Open items:** the unwritten guard (no site converts a track into `adv` at a fixed rate); reconciling CIP-12/CIP-6/CIP-14 "second currencies"; 5 parliamentary-path questions (what Mandate-pool roll carries) left to FA/CORE.

### .audit/2026-08-06-social-contest-three-lens-audit/07_keys_knots_npcs_and_the_combat_model.md
- **What it is:** extension proposal, 2026-08-08, lane SC, ED-SC-0030; six Fable lenses on four Jordan axes (Keys I/O with scatter-gather, Knots, world churn as anti-repetition, the contest as multimodal combat).
- **Status:** "PROPOSED (2026-08-08, ED-SC-0030)". Reading: partly superseded - Section 2 (Keys as I/O substrate, `scene.contest_convened`, OF-CAP cascade_depth_max=3, emissions 64, `drain_tick`) is dead because the Key substrate is RETIRED (ED-IN-0232); sections 1, 3, 4, 5 retain design value.
- **Bears on:** SC, PC (combat comparison), WR, CHAR (NPCs, Knots), FA, MB (rout), CORE.
- **Content that matters:**
  - Coverage finding (:15-21): audits 00-06 never opened `systems/combat/combat_engine_v1/`; track map of combat's eight tracks vs social (:43-55): Initiative, Tempo and Commitment/legibility/read are NULL on the social side; Stamina maps to Reserve (two yields clinch as silence).
  - Standing dead zone (:85-106): `Standing.frac()=(v-START)/(HI-START)` clamped, START=5 (`primitives.py:32` still `LO,HI,START = 0,10,5`) so Standing 0 and 5 are indistinguishable in reception; ruling: add `discredit_bar` to `DefeatCatalogue` (fatal iff venue says so, `[SEED]` ~2), shipped only with a face-attack channel.
  - Non-fungibility guard (:182-188): "tracks enter resolution as multipliers on process, never as addends on the score; no site converts Standing/Room/Reserve/faults/claim state into `adv` at a fixed rate"; fix is more terminals and record kinds, not addends.
  - Jordan's correction (:108-141): a feint in speech is a deliberately chosen act (unlike combat), with two independent detections (opponent; bench/room) - being caught being clever costs Face; explicit trick/feint class warranted. Leak term `res=(1-leak)*venue_w+leak*judge_character` already is the "suckered" mechanism (:154-157); judge default vector 0.34/0.33/0.33 makes judge identity inert until skew is authored (:271-274).
  - NPC adjudicator: derivation adapter not replacement; `faction.py:39` already derives an Adjudicator from faction stats; aggregate benches by ballot not mean; `ArmatureConfig` keys by `id(adjudicator)` - ephemeral (:290-293). Five disjoint id spaces.
  - Knots (:299-336): `check_knot_rupture` has zero callers outside module+test; `EvidenceItem` lacks provenance so rupture can never fire - add `provenance` incl. `knot_counsel(knot_id)`; `conviction.py` `CONVICTIONS` tuple was wrong and silently no-op'd 'Loyalty'. Churn (:342-371): same emergency council replays the same contest every season at Sta<=2; `_derive_vote` derives who, not what; shippable repeat-detector tuple (xfail now, blocking when the minimum set lands).
- **Conflicts / stale:** Section 2 all retired (Key substrate). `id(adjudicator)` still used at `agon_harness.py:211` and `_kernel_tests.py:1366` (still live as pattern). `CONVICTIONS` now `= descriptors.PURSUITS` at `systems/characters/sim/conviction.py:60` (the gate was re-founded; fixed or changed [UNVERIFIED which]). `check_knot_rupture` now referenced only in `engine/tests/test_knots_ed912.py` (still no production caller). `PP-724` status [UNVERIFIED].
- **Open items:** no NPC lane in the ED roster at the time; 5-way id space; the Vor (initiative scalar) fork; outcome enum extension (clinch, remitted); Rivalry+Patronage edge minimum subset; Room collapse terminal default off.

### .audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md
- **What it is:** verbatim upload 1 ("Political Mechanics for a Renaissance-Inflected Videogame"), research to 45 primitives P1-P45 in seven families, four assembled scene types, self-audit A1-A11; preserved 2026-08-06; external author, not Valoria.
- **Status:** README header "SOURCE MATERIAL — verbatim, NOT canon, NOT ratified, NOT Valoria design text". Reading: research input (tier-3 material); reference for vocabulary only.
- **Bears on:** SC, FA, SE, WR, FI (inquisition, inspection circuit), CORE (Record spine).
- **Content that matters:**
  - Source-tier tagging `[T0]..[T2]`, `[UNVERIFIED]`, `[TIER-FLOOR: T2]`; Inquisition material rests on Hill 2019 and Lea (partisan), Hermagoras only via Cicero (:8, :100-106, :753-755).
  - Constraint C1 from Burning Wheel Duel of Wits collapse (players converge on Point/Dismiss): manoeuvres must differ in what they change about the state of the argument, not damage (:186-190); C2 (contradiction-matching is a puzzle not a debate, :198); C3 (cap affection so structural conflicts stay unbuyable, :224).
  - P5 Stasis Gate (Conjecture -> Definition -> Quality -> Jurisdiction, ordered/gating, :309-315) and P7 three attacks Undermine/Rebut/Undercut (Prakken, :322-329); P9 Burden of Proof as a single token "sits differently in each forum" (:337-341); P11 Evidence Array hidden from the defence (:349-354).
  - P16 Recorded Defeat (senatus auctoritas, :385-389), P33 Decree with Compliance (:491-494), P34 Detection+Graduated Sanction (:496-500), P37 Split Command (:513-516), P41 Scaled Compromise (:537-540), P42 Cheap Talk default with P43 Costly Signal as exception (:542-549), P45 Shared Loss (:556-559).
  - Composition rules (:563-569): one vocabulary; forums differ by parameter not minigame; every power primitive has a cost or term; records outlive scenes; information layer not optional. Content graph: author Claims and Frames, generate Records, never generate the framing of a question or charter terms (:677-698). Four hearing types as one machine with four parameter sets (:595-602); negotiation = same scene with burden token removed (:604).
  - Own audit A1-A11 (:716-755): A1 stasis fix lives at content layer (remedy: ~40% invariant, 20-claim paper prototype); A5 no resource economy; A9 P45 is a multiplayer fix and in single-player becomes an AI opposition problem; blind spots: assumes turn-based scene-bounded play, no interface thinking, no player-fantasy check (:767-773).
- **Conflicts / stale:** Uses Victoria 3 enactment-clock figures (100-day stages, 2x/1.5x multipliers) it itself flags as not transferable (A4). Nothing in it is canon; any Valoria doc citing "40%" or P-numbers as authority has an orphaned provenance (see file 03).
- **Open items:** the three closing questions (player's position, resource economy, multiplayer) - the later documents answer them for a single-player no-GM game.

### .audit/2026-08-06-social-contest-three-lens-audit/sources/02_political_state_graphs.md
- **What it is:** verbatim upload 2 ("State Graphs — Eight Systems"): eight mermaid state machines S1-S8 in the P-vocabulary plus a computed interrogation (incidence matrix, tiers, Jaccard, role stability, call graph, throughlines T1-T5).
- **Status:** SOURCE MATERIAL per README (not canon). Reading: research input; the computed findings are reproducible via `02a_interrogate.py`.
- **Bears on:** SC, FA, SE, WR, FI, CORE.
- **Content that matters:**
  - Eight graphs: S1 Court, S2 Tribunal, S3 Inquisition (abjuration negotiated by calling S4), S4 Negotiation (burden removed), S5 Parliament (with nested Enactment machine), S6 Settlement, S7 Territory (fans out to one S6 per locality), S8 Diplomacy (:27-487).
  - Tiers (:550-556): only P1 Standing and P16 Record are in 7-8 systems; P4 Immunity and P24 Alternating Narrow/Widen used nowhere; "S9 Selection and Investiture" is the missing ninth system and "largest gap" (:564-566).
  - Clusters (:585-591): Adjudication S1-S3 (J 0.52-0.76), Administration S6-S7 (0.67), Exchange S4-S8 (0.52); S4 vs S6 J=0.07 "honest boundary"; S2 Tribunal is the hinge and S5<->S2 the only call cycle, "do not break" (:595, :626).
  - S4 is a subroutine (3 inbound calls, 0 outbound) (:624). Role shifts: P1 is M everywhere but G in S2 (accuser standing gates opening); P35 Bond produced in S8, consumed as guard in S6/S7 (:605-608).
  - T1 record spine: every terminal emits a Record that guards a later transition (e.g. RelapseWatch -> Condemnation guarded by an earlier hearing's P16) (:633). T4: P30 Sealed Channel is the sole bridge from information to adjudication (:642).
  - Self-audit: encoding written after the graphs by same author; M cells weakest; P1 and P31 counts are upper bounds (:662).
- **Conflicts / stale:** Cites Valoria-unrelated sources only. Overlap analysis depends on the encoding, not independently derived. Has no consumer in code (SC kernel does not implement Record spine).
- **Open items:** S9 Selection never built; all S5 enactment parameters untuned.

### .audit/2026-08-06-social-contest-three-lens-audit/sources/02a_interrogate.py
- **What it is:** the Python script behind upload 2's interrogation (SYS dict of primitive->role per system, CALLS list), 105 lines.
- **Status:** SOURCE MATERIAL (script, not run by anything). Reading: historical instrument.
- **Bears on:** SC, PROCESS.
- **Content that matters:**
  - Defines `SYS` (8 systems x primitive->role in {S,T,G,O,M}) and `CALLS` (7 edges); computes frequency, tiers (CORE>=7, BROAD 4-6, BRIDGE 2-3, LOCAL 1, UNUSED), role-shifts for primitives in >=3 systems, pairwise Jaccard, matrix, call graph (:17-104).
  - Hard-coded input: it reads `political-mechanics-primitives.md` by bare filename at :9 (the file is now `01_political_mechanics_primitives.md`), so it does not run as filed from this directory.
  - Encoding is a hand-authored table identical to the markdown matrix; computing from it only re-derives it (circular: the "computed" claim rests on the hand encoding).
  - Nothing in the repo reads it (one-off).
- **Conflicts / stale:** the name mismatch above; otherwise dead artefact.
- **Open items:** none.

### .audit/2026-08-06-social-contest-three-lens-audit/sources/README.md
- **What it is:** index to the five-document source series, 2026-08-06, lane SC, ED-SC-0025.
- **Status:** "SOURCE MATERIAL — verbatim, NOT canon, NOT ratified, NOT Valoria design text". Reading: live as provenance note, historical otherwise.
- **Bears on:** SC, PROCESS.
- **Content that matters:**
  - Why the sources were copied: ED-SC-0017 flagged that `params/contest.md` is cited 97 times across the kernel and no longer exists on disk; ED-SC-0021/0023/0024 cited documents with no on-disk provenance (:12-17).
  - Series table (:20-27): doc 1 primitives P1-P45; doc 2 state graphs; doc 3 consolidation 45 -> 14 mechanisms + 31 configurations; doc 4 persuasion pivot (story model, ELM, Cialdini, N1-N11); doc 5 era sources (Guiguzi, Han Feizi, N12-N20).
  - Three warnings (:29-44): doc 4 retracts doc 3's warrant x attack matrix as fabricated; doc 5 carries `[TIER-FLOOR: T2]` on Chinese material (adopt as design on merit, never cite as historical in ratified docs; only Gentz's comparative thesis is T1); the series inflated 14 -> 25 primitives and the re-distillation gives 20 N-primitives -> 5 mechanisms.
- **Conflicts / stale:** cross-refs say "adjudication §4" for the re-distillation, which is §3 in file 03 (minor).
- **Open items:** none.

### .audit/2026-08-06-social-contest-three-lens-audit/sources/03_consolidation.md
- **What it is:** verbatim upload 3 ("Consolidation — From Research to Encodable Systems"): self-audit of docs 1-2, distillation 45 primitives -> 14 mechanisms M1-M14 + 31 configurations, four-resource economy, M2 Scope, data schemas, resolution pseudocode, three loops, opposition model.
- **Status:** SOURCE MATERIAL per README (not canon). Reading: research input; its §6.2 warrant x attack table is the retracted fabrication.
- **Bears on:** SC, FA, CORE, SE, WR, CHAR (Actor/aims).
- **Content that matters:**
  - Separation rule: "A mechanism is code: it takes inputs and branches. A configuration is data... If it can be written as a row in a table, it is not a mechanism" (:62-63); M1 Standing, M2 Scope, M3 Concealed Value, M4 Probe, M5 Claim, M6 Attack, M7 Gate, M8 Floor, M9 Block, M10 Record, M11 Clock, M12 Compliance, M13 Settlement, M14 Selection (:67-82).
  - Four resources (:117-124): Time (universal cost, segments), Standing (indexed per body, non-fungible, 0-100), Coin, Obligation (directional, destroyed by use, cannot be bought); rule that Standing and Coin do not convert directly (:129).
  - M2 Scope: `Scope = SELF|SETTLEMENT|HOUSE|FACTION`; `bind()` returns BOUND within mandate limits else PROVISIONAL(risk) that is live and may be repudiated; "the only thing in this design that gets more interesting without a human across the table" (:147-172).
  - `gate(burden)` with ACCUSER / RESPONDENT / LOWER_STANDING / NONE gives accusatorial / inquisitorial / political tribunal / negotiation (:378-385); S1 and S3 differ in exactly two fields (burden, evidence visibility) (:547); S8 Diplomacy is Loop A with burden NONE wrapped in Loop B (:548).
  - §6.2 anti-collapse table of warrant (WITNESS, DOCUMENT, EXPERT, SIGN, PRECEDENT, CONSEQUENCE) vs attack (strong/moderate/weak) and the "no attack kind optimal for >40% of claims" invariant (:314-337) - RETRACTED by doc 4 as fabricated.
  - Opposition model (:556-579): faction aims (2-3, visible), unbuyable red lines, private `threatModel`, `concessionCurve`, `patience`; aims expire with their holder; replaces P45; Selection chain encoded `[N30,N9,W40,N12,W25,N9,W45,N11,W41]` (:492).
- **Conflicts / stale:** all numerics `[UNTUNED]`; self-flagged gaps: interface never specified (third doc running), 40% invariant stated not enforced, inquisitorial array authored-to-be-inferable has no guidance (:596-600). The "requested model handoff" note at :4 is an artefact of the upload's chat session.
- **Open items:** paper prototype of Loop A (twenty claims, four bodies) - never done; build order (:602-609: Record+Standing first, then Concealed Value+Probe, then Loop A with burden, Scope, Selection).

### .audit/2026-08-06-social-contest-three-lens-audit/sources/04_negotiation_and_persuasion.md
- **What it is:** verbatim upload 4 ("Negotiation and Persuasion"): classical rhetoric + behavioural science + game survey (Griftlands, Dogs in the Vineyard, Reacting to the Past), primitives N1-N11, three systems (Table, Floor, Verdict), encoding, adversarial audit A1-A11.
- **Status:** SOURCE MATERIAL per README (not canon). Reading: research input; its opening retracts doc 3's warrant/attack matrix; its A1 is the Klei refutation used by the SC audits.
- **Bears on:** SC, CHAR (minds, aims), FA, DICE (resolution shape).
- **Content that matters:**
  - Pivot: persuasion operates on minds (counterpart, audience, jury), not propositions; table of targets and governing research (:4-16).
  - Atechnic (inventory: laws, witnesses, contracts, tortures, oaths) vs entechnic (ethos/pathos/logos actions) proofs (:24-30); ELM central vs peripheral route with durability asymmetry (:62-71); Cialdini levers with unity as multiplier (:75-79).
  - Story model (Pennington and Hastie): coverage, coherence (consistency, plausibility, completeness), uniqueness; `acceptance=h(coverage,coherence)`, `confidence=k(uniqueness)`; terms "not formally defined" so the numbers are ours (:85-104).
  - N6 counter-anchoring (Galinsky and Mussweiler: focusing on opponent's alternatives/reservation/own target eliminates the anchor), N7 logroll (better joint outcome, rated less attractive), N10 Deliberation (first ballot, informational vs normative influence, acceleration, momentum, first-crossing reversal) (:255-283); N8 Arena+Escalation (Talk -> Status -> Coercion -> Force, concession priced) (:266-269); N9 factions and indeterminates (RTTP) (:271-274).
  - A1 (:466-467): Klei's playtest evidence - conversation challenges built as spending resources to influence rolls were "a lot less fun than fighting"; cards fixed it - and docs 1-3 are exactly that shape. A6: N3 route-forcing creates a dominant strategy ("make them stupid, then charm them"). A10: no deception/truth field. A3: per-mind plausibility content cost uncosted.
  - Recommended build order (:529-532): paper-prototype the Verdict (six minds, two stories, twelve evidence items), then the Table; decide interaction model from prototypes; do not write the Floor until A6 answered.
- **Conflicts / stale:** `[CLOSED: fabricated matrix]` claim is qualified by A2 (function bodies g,h,k are invented). Laboratory-derived findings (A5); leniency asymmetry carried as tunable parameter.
- **Open items:** interaction model (cards vs scripted vs spend-and-roll), deception, escalation pricing, "nothing played - four documents running".

### .audit/2026-08-06-social-contest-three-lens-audit/sources/05_persuasion_in_the_era_sources.md
- **What it is:** verbatim upload 5 ("Persuasion in the Era Sources"): corrects doc 4's A4 with the Chinese counterpart-facing tradition (Guiguzi, Han Feizi), Roman jury composition, Koziol supplication, Sengoku kishomon oaths; primitives N12-N20.
- **Status:** SOURCE MATERIAL per README (not canon). Reading: research input with explicit `[TIER-FLOOR: T2]`; adopt as design on merit only.
- **Bears on:** SC, FI (assessment-before-speaking), FA, WR, CHAR.
- **Content that matters:**
  - Gentz thesis (T1): European rhetoric is forum-facing, Guiguzi counterpart-facing (:18); the other technique lists rest on a publisher's table of contents and encyclopedia summaries (B1, :237).
  - N12 Read Before Speaking (Weigh/Gauge/Assess, assessment is the majority of the activity, :126-133), N13 Open-Shut, N14 Reverse Scale (per-mind lethal topic; B3: save-scum trigger unless inferable/survivable, :140-143, :245), N15 Concealed Comprehension (legibility value; inverts "knowledge always good", :145-149), N16 Attribution (scored outcome: did the target believe the decision was his own, :151-154).
  - N17 Supplication binds the powerful at public cost (Koziol; B6: no failure state, :156-160, :255); N18 Self-cursing bond with trust inflation (plain paper -> talisman -> seal -> blood) resting on Ogino's contested reading (B9, :162-167, :261); N19 Composition Contest (lex Aurelia changed only who sat after 50 years of contest, :169-172); N20 Advocate as Evidence (:174-177).
  - Own audit: Renaissance Italian practice search failed (B5, :250); the series corrects itself each document and the primitive count is rising again (:273-274).
- **Conflicts / stale:** nothing here is citable as historical in ratified docs (file 03 §3.5).
- **Open items:** primary-text reads (Hui Wu translation, Gentz 2014, Watson Han Feizi, Koziol chapters, Cotrugli 1458); re-run separation rule on N12-N20 (done in file 03: 20 -> 5).

### .audit/2026-08-06-vector-audit/structure_audit/data/structure_metrics.json
- **What it is:** machine-generated JSON snapshot (2026-08-06) of import-graph and module-contract structure: 271 nodes / 408 edges for code (`cli_entries`, `cut_vertices`, `cycles`, `orphans`, `stub_wired`) and a 27-node contract graph (`l2`: joined/none/undeclared contracts, locality, cycles); plus `findings` (dangling_emit, doc_null, phantom_producer).
- **Status:** none (data file). Reading: historical snapshot; the tree it measured (engine/cross_scale, engine/substrate/keys, engine/mc_v18, systems/factions) no longer exists.
- **Bears on:** CORE, PROCESS, SC, FA, MB.
- **Content that matters:**
  - Import cycles (`code.cycles`): `mass_battle.sim.massbattle <-> units`; the whole `social_contest.sim.contest` package (appraise, armature, dictionaries, faction, modes, resolver, rhetoric, wrapper) in one cycle; a mass_battle test-package cycle (:117-139).
  - Cut vertices include `engine.cross_scale.echo_transport`, `engine.cross_scale.scene_dispatch`, `engine.mc_v18`, `engine.substrate.keys`, `systems.social_contest.sim.parliamentary_vote` (:94-116) - all of the engine ones now gone (checked: `engine/mc_v18.py`, `engine/cross_scale`, `engine/substrate/keys.py`, `systems/factions` absent; `systems/overview`, `systems/mass_battle/sim`, `systems/threadwork/sim` still present).
  - `stub_wired` list (:209-234): tribunal, treaty, charter_liberties, fieldwork investigation etc. were wired to stubs; `l2.contract_code_join` says 13 of 27 contract modules join code and 13 have none (`audit, domain_actions, npc_behavior, npc_memory, settlement_economy, game_director...`) and `mass_battle` "undeclared" (:271-306).
  - Contract-graph cycle `faction_state, npc_behavior, piety_track, social_contest` and cross-locality fraction 0.511 (:335-352).
  - `findings.dangling_emit`: `peninsular_strain -> env.crisis` (non-notional) plus two notional (:236-253).
- **Conflicts / stale:** wholly Key-substrate-era (the `module_contracts` "emits/consumes" model); `tools.build_key_graph`, `tools.export_key_types`, `tools.dead_primitive_census`, `tools.trace_execution_phases`, `tools.sim_harness` all absent now (checked). Not reproducible from the current tree.
- **Open items:** none.

### .audit/2026-08-08-world-churn-audit/01_plan.md
- **What it is:** v2 interdependency plan (rewritten after adversarial review) from the world-churn audit, 2026-08-08, lane IN, ED-IN-0149; tiers T0 repairs/instruments, T1 high-leverage edges, T2 substrate maturation, T3 Jordan decisions J-A..J-I.
- **Status:** "PROPOSED — nothing here is ratified by merging this audit PR. Tier 3 is HELD for Jordan." Reading: superseded/historical - its subject (Key substrate, `scene_dispatch`, `mc_v18`) is retired (ED-IN-0232) and the plan is not an active workplan.
- **Bears on:** CORE, WR, FA, SE, MB, CHAR, SC.
- **Content that matters:**
  - Strategy (:11-25): "the machinery is built and disconnected, not missing and not scripted"; repair, connect highest-leverage single edges, instrument connectivity, force Jordan-owned decisions; behaviour changes flag-gated OFF with byte-exact goldens; no uncited constants.
  - T1-2 Revolt -> `Territory.owner=None` (:133-152): `Territory.accord` continuous 0.5-7.0 with a mutator flooring at 0.5, so a naive `== 0` is inert forever; use `canon_buckets.canonical_accord` (<1.75); Step 4c.1 and garrison contest must be in scope. T1-1 battle -> Mil attrition BLOCKED (no canon maps size_pct -> Mil; J-I) (:154-171). T1-4 Council -> `Sta`: one echo block carries one stat, so shape not magnitude is the blocker (:178-186).
  - T0-1 conviction gate: `apply_conviction_scar` returns magnitude 0 for unknown names while caller reports `conviction_scar=1`; fix breaks `engine/tests/test_knots_ed912.py:103-109` and forces a name choice (J-C) (:92-109). T0-3 `temperaments.py` reader cannot see `world.npc_drift_state`; `_CELL_OWNED` is MB-scoped so extending it would be a guard that passes because it cannot look (:77-90).
  - Tier 3 list J-A (L0 identity fork), J-B insurgency L growth rule, J-C conviction vocabulary (4 axes vs 9 vs 8 vs claimed 13), J-D ED-1051 engine_clock open, J-E Strain/Turmoil/PI collapse, J-F council echo shape, J-G dead `spec/churn_amendments.md` cite, J-H arc-generator skill reads evacuated trees, J-I battle -> Mil (:206-218).
  - Review changed 6 of 11 items (:244-250): wrong sequencing, vacuous guard, second parser (`build_execution_map`), unblocked-by-assertion item.
- **Conflicts / stale:** `conviction.py` `CONVICTIONS` is now `= descriptors.PURSUITS` (grep) - J-C looks superseded in code; `apply_conviction_scar` still present in `systems/characters/sim/conviction.py` and `knots.py` and `engine/tests/test_knots_ed912.py` [UNVERIFIED whether still no-op on unknown]. `canonical_accord`, `process_treaty_expirations`, `npc_drift_state` greps: only `tests/valoria/test_import_cycle_game_state_npe.py` and `tools/export_game_constants.py` match the group - the Accord/treaty code appears gone. J-D/J-A/J-G refer to doc objects not rechecked [UNVERIFIED].
- **Open items:** all of J-A..J-I as of 2026-08-08; most dissolved with the Key retirement and `engine/season/` rebuild (superseded by 5-way test in CLAUDE.md §0 rather than answered).

### .audit/2026-08-08-world-churn-audit/02_adversarial_review.md
- **What it is:** verdict record of two read-only critics against the churn findings and plan (2026-08-08, lane IN, ED-IN-0149).
- **Status:** "RECORD". Reading: historical method exhibit.
- **Bears on:** PROCESS, CORE, WR, FA.
- **Content that matters:**
  - Overturned: the findings credited NPE stance drift as live churn while its own D5 proved `world.npcs` stays empty (:18-24, call site vs concept pattern-match); "both live stat_deltas sites faction-facing" false (one settlement-facing); T1-1 blocked; T1-2 unimplementable; T0-3 guard vacuous (:16-51).
  - Sharpened: "10 of 13 subscriptions have no producer" is 11/13, and 13/13 at default-flag runtime; `scene.combat_felled` has no Python emit site (:57-62).
  - Softened: `da.public_governance` is a live log-only emitter; `restore_world` can create `owner=None` (:70-79).
  - Method: independence structural (read-only tools, producer output only); the biggest value was a self-contradiction between two sections the producer itself wrote (:128-131); critics' weakest verdicts carried forward (:104-118).
- **Conflicts / stale:** subject surfaces gone (see 01). **Open items:** the unaudited producer-only claims (§5 landing verdicts, §6 lens attribution, §7 canon-engine import, D12 contest-kernel purity).

### .audit/2026-08-08-world-churn-audit/03_causal_model.md
- **What it is:** causal-model and build-order document from seven Fable lenses + two critics, 2026-08-08, lane IN, ED-IN-0149.
- **Status:** "PROPOSED (read-only audit; nothing executed, no head moved, no flag flipped)". Reading: historical; premise (Key graph with 46 nodes/139 edges, notional edges) retired with the Key substrate; economic/stability reasoning still useful as leads.
- **Bears on:** WR, SE, FA, MB, CHAR, CORE.
- **Content that matters:**
  - Core finding: the causal model is "declared and unemitted" - of 94 module-to-module `emits_consumes` edges 43 are `notional`, only 7 carry a Key type with a live emitter; `wiring_map_check` reported `live: 2` of 27 modules; a 40-season traced run showed no npcs/characters/fieldwork/threadwork/combat calls at all (:12-28).
  - Adjudicated build order (:32-83): fiscal edge first (`realized_income = Prosperity x stance x compliance`; without income every Wealth-denominated cost ends in a clamp no-op since `Faction.adjust` floors at 0.5), then conquest fork at settlement grain with Accord-write reconciliation (4 control/accord writers incl. Crown Initiative), declare `scene_outcome` at one producer, battle consumers after a roster reconciliation (registry vs key_graph.json disagree), derivation-crossing rule (edge-triggered with hysteresis).
  - Stability (:85-107): casualty writeback before fiscal edge degenerates to first-mover extermination; conserved population tier flips the sign of misgovernance punishment (emigration to a better-run city raises T); loyalty-retarded migration over-damped unless loyalty decays.
  - Double-counting (D.6) (:109-122): Mandate counted twice (mass_battle_v30:688 direct write vs derived aggregate in settlement_layer_v30:165); one conquest at three grains; casualties charged to two settlements; migrants twice.
  - Keys verdict (:128-151): `stat_deltas` has no applier; derived values invisible to `causes[]` (derive-never-write vs causal legibility conflict); six of 55 key types carry registry defaults their own validator rejects; proposed ruling: store conviction on the canonical 13, derive the 4 axes (13->4 non-invertible).
  - Recurring failure mode (:155-169): declaring a mechanic missing without checking where the corpus keeps it (e.g. `mc_v18` refusing NPC generation although `settlement_layer_v30.md:857` is the Local Actors rule; captive pool already owned by `faction_layer_v30.md` 6.3). Also: no Scar decay anywhere (needs a vindication mirror) (:193-196).
- **Conflicts / stale:** all Key/`mc_v18`/`scene_dispatch` references retired; the "two battle engines" finding (canon 28-module engine never imported at runtime) pre-dates `modules/mass_battle/` and `engine/season/` [UNVERIFIED current state]. Stability claims are reasoned, not simulated (:202-207).
- **Open items:** whether Accord can reach 0, whether `Sta<=2` is reached, conquest frequency - hypotheses never measured. Several leads (no Scar decay; fiscal edge; double-counted Mandate) are architecture-neutral and may still be live for SE/FA/CHAR.

### .audit/2026-08-08-world-churn-audit/04_throughline_permutations.md
- **What it is:** analysis of branch structure across throughline compositions, four read-only hub traces + adversarial pass applied inline, 2026-08-08, lane IN, ED-IN-0149.
- **Status:** "PROPOSED (read-only; nothing executed). Adversarial pass COMPLETE — corrections applied inline." Reading: mostly historical (hubs sat on retired engine code) but the register/design-contradiction findings are design-level.
- **Bears on:** WR, FA, SE, CORE (victory), MB, PROCESS.
- **Content that matters:**
  - Live bug (held): victory Accord gate mis-scaled by a canonical band - `ACCORD_MAP={0:1.0,1:2.5,2:4.0,3:5.5,4:7.0}` yet `victory.py` `ACCORD_MIN=2.0` against the continuous field (canonical 1 passes "Accord >= 2"); the PS leg reads `Turmoil`, initialised 0.0 and written nowhere (vacuous); `mass_seizure.py` states "11+ territories" vs 15 (:10-43). **Tree check:** `ACCORD_MAP`/`ACCORD_MIN` now only in `tools/export_game_constants.py` (engine victory code gone) - [UNVERIFIED] whether the export reproduces the defect or the successor reads a canonical value.
  - The throughline register (`references/throughlines_complete.md`, not at `references/` now; only `throughlines_meta.md` family remains) has 43 headers/42 live but states "30" and "41"; 861 pairs vs hand matrix of 20 (2.3%); six types of "throughline" (axioms, clocks, postures, personal state machines, geographic projections, second-order) compose by different rules; T-24 is a type error (the composition operator mis-filed as an entry) (:47-105).
  - July instrument measured and REJECTED the pair matrix ("20/21 pairs interact") - correct object is the bipartite throughlines x state-variables graph (:96-99); proposed derived sidecar `references/throughlines_index.yaml` with `{id,type,reads,writes,status}` (:208-215), defect: vocabulary source `descriptor_registry.yaml` clocks list lacks Strain/Turmoil/Accord/Order (:217-222).
  - Hub collapses: MS/rendering branch space is one-dimensional (net delta clamped +-10), restore arm unreachable (`mending_stability_delta` applied nowhere), MS 0 has three incompatible rulings (:109-134); Faith/CI: CI>=60 in 20/20 seeds and forced declaration (CI=100) in 8/20 while `mass_seizure` unreachable and `Territory.adjust_pt` has no callers so Piety is frozen (:136-157); Accord: persistent anarchy invisible because Strain/IP counts scope to playable-faction territories (:169-176); four dialects of "Accord" (0-3 doc, 4 derived, canonical 0-4, continuous 0.5-7.0) (:187-188).
  - Order-sensitivity questions: province-Accord recompute has no step in §7 list; whether immediate writes count against the MS +-10 cap; no +-5/season CI clamp implemented (:192-204).
- **Conflicts / stale:** engine files named (`game_state.py`, `victory.py`, `mc_v18.py`, `mass_seizure.py`) are gone from `engine/`; `references/throughlines_complete.md` moved (`ls references` shows only `throughlines_meta*.md`). Register metadata rot: 186 distinct Systems tokens, 4 canonical; "Fully implemented" labels measure design completeness; 9 of 20 ARC vector cites dangling (:238-242).
- **Open items:** MS 0 ruling; which Accord scale wins (superseded if `engine/season/` has one owner - [UNVERIFIED]); throughlines sidecar never built (greps: no `throughlines_index.yaml`).

### .audit/2026-08-08-world-churn-audit/05_key_catalogue.md
- **What it is:** generated + hand-verified reference catalogue of 55 Key types across 67 declared edges (164 incidences), from `references/key_graph.json` (produced by `tools/build_key_graph.py`), 2026-08-08, lane IN.
- **Status:** "REFERENCE (generated + hand-verified)". Reading: superseded/dead - the Key substrate, `key_graph.json` generator (`tools/build_key_graph.py` absent) and the emit sites are retired (ED-IN-0232).
- **Bears on:** CORE, PROCESS (history), SC, FA, MB, WR, CHAR.
- **Content that matters:**
  - Edge table (:21-89) of producer -> consumer module pairs and the "live on edge" column: only `da.public_governance`, `scene.accord_echo`, `scene.battle_concluded`, `scene.contest_resolved` ever had literal emit sites (four of 55). Consumer table (:93-105): `articulation_layer` consumes 43 types (4 live), `npc_behavior` 31 (3), `faction_state` 25 (3), `piety_track` 9 (1).
  - Per-key detail (:109-706): required/optional payload, scale, permanence, time_horizon, reconciliation verdict between registry and contracts (`agreed`, `registry_superset`, `contracts_superset`, `registry_only`, `absent_both`), and a runtime flag. Types with NO declared consumers: `env.crisis`, `mechanical.era_transition`, `mechanical.season_change`, `mechanical.second_calamity`, `mechanical.settlement_captured`, `mechanical.theocracy_unification_declared`, `meta.legacy_event` (no producer either), `state.settlement_revolt`.
  - Useful as a design vocabulary trace: the payload field lists (e.g. `scene.contest_resolved` required `scene_id, outcome, participants`; optional `persuasion_track_final, rhetorical_style_used`; `state.opinion_revised` payload with affect_axis before/after and confidence before/after; `state.scar_acquired`) show what the earlier architecture thought cross-subsystem events carried.
  - `scene.contest_resolved` consumers declared as `faction_state` and `npc_behavior`, never `social_contest`'s own feedback; `state.opinion_revised` is the only declared edge into `social_contest` (:57) and has no producer emit site (relevant to file 07's "compose; extend nothing").
- **Conflicts / stale:** entire document is a snapshot of a retired substrate; `references/key_graph.json` and `tools/build_key_graph.py` are not in the tree (checked absent). Not a basis for any current finding.
- **Open items:** none that survive retirement; the "what should cross-scale events carry" question maps to `engine/season/` write matrix instead.

### .audit/2026-08-08-world-churn-audit/06_master_synthesis.md
- **What it is:** reconciling master synthesis of the 2026-08-08/09 world-churn audit (22 read-only lenses, four adversarial passes), lane IN, ED-IN-0149, tree `690f4c3`; Parts I reconciliation, II consolidation, III architecture ruling, IV orchestration P0-P5, V rulings J-A..J-O, VI do-not-build, VII weak claims, VIII adversarial record.
- **Status:** "PROPOSED. Read-only audit... HELD, LOUDLY (ED-1094): Parts III, V and VI are all held". Reading: historical; the programme assumed promoting the Key mesh (J-O), which CLAUDE.md §0 has since answered by retiring the Key substrate (ED-IN-0232). Individual findings (Accord units, one-way Wealth ratchet, Turmoil vacuity) are leads about code that was in `engine/`/`systems/` at 690f4c3.
- **Bears on:** CORE, SE, FA, WR, CHAR, MB, SC.
- **Content that matters:**
  - Accord is three units on one field (canonical int 0-3 per `victory_v30.md:80`, continuous 0.5-7.0 via `ACCORD_MAP`, granular delta /10 via `MULTS['accord']`) plus a canonical 0-4 bucketing; `victory.py` compared continuous to `ACCORD_MIN=2.0` where canon needs 4.0 (gate at half height, burden "halved not bypassed"; `SUSTAIN_SEASONS=2`); `settlement.py:120` `math.floor(t.accord)` is a fourth dialect (floor(2.5)=2 vs canonical_accord(2.5)=1) (:92-175). Proposed guard P0-6 (no `.accord` compare to a numeric literal outside `canon_buckets`, with allowlist for deliberate sites).
  - D13 fiscal finding (:177-238): Wealth has no income path (reachable stat set from the dynamic `echo_transport` write is {L, I, Mil}); four cost sites, three levy full-size via `_MULTS_W=100` pre-multiplication; so a one-way ratchet; Wealth gates Great Work (`crown.W>=3.0`) and muster pool (`Mil+floor(W/2)`); the closing constant is specified twice, x10 (`derived_stats_v30.md:308`) vs x50 (`settlement_layer_v30.md:47`).
  - Architecture criterion (narrowed): "Aggregate-crossing detection belongs to the aggregator; effect magnitude belongs to the effect's owner" (:394-395); a distributor wrapper or world director is a do-not-build (:550); cascade-depth "clocked relay" claim withdrawn: `drain_tick` has zero production callers and `next_tick` raises if the queue is non-empty (:422-440).
  - Topology (probe output): 27 modules, 16 pure sources, 4 pure sinks, 7 bidirectional; 125 consume-declarations, top four modules hold 108/125; 55 key types: 8 orphan, 4 seam, 36 channel, 7 nexus (:316-324); wildcard `"*"` entry caused a retraction-then-retraction-withdrawn episode (:35-88).
  - Jordan ruled in session 2026-08-09 (J-M): "local actors should be NPCs" - seed Local Actors via the NPC path into `world.npcs` (settlement_layer §4.5 per-type table: Seat 2, City 2, Town 1, Fortress 1, Port 2, Cathedral 1, Mine 1, Outpost 0) (:500, :539).
  - Appendix A.1: same-lane concurrent ED allocation collision (ED-IN-0148 renumbered to 0149); nameable guard (no id appears twice across ledger files) not written (:696-714).
- **Conflicts / stale:** Keys/herald/`econ.*`/`gov.*`/`state.treaty_changed` programme is moot after Key retirement; `references/key_graph.json` absent. Whether `engine/season/` (effects_economy.py etc.) closed the Wealth income and Turmoil gaps is [UNVERIFIED] - `engine/season/loop/effects_economy.py` exists.
- **Open items:** J-A (Accord unit direction), J-B (x10 vs x50), J-F (D.6 Mandate double-count owner), J-G (population conservation sign-flip), J-L (battle -> Mil coefficient): these are design-level and may have been re-decided in `engine/season/` or still be open for SE/FA/MB.

### .audit/2026-08-08-world-churn-audit/topology_probe.py
- **What it is:** 127-line Python probe computing module degree, consume/produce concentration, key fan-out buckets and producerless keys from `references/key_graph.json` (wildcard `"*"` excluded by default).
- **Status:** none (script). Reading: dead instrument.
- **Bears on:** CORE, PROCESS.
- **Content that matters:**
  - Defines thresholds orphan 0 / seam 1 / channel 2-3 / nexus >=4 and prints module classes (pure source/sink/bidirectional) (:61-104).
  - Reads `references/key_graph.json` via `ROOT / "references" / "key_graph.json"` (:31) with `ROOT=parents[2]` (assumes the old `audit/` path, now `.audit/<dir>/`).
  - Nothing runs it; `references/key_graph.json` is absent (checked), so it fails with FileNotFoundError.
- **Conflicts / stale:** docstring path `audit/2026-08-08-world-churn-audit/...` is the pre-rename path; the data file and the generator tool are retired.
- **Open items:** none.

### .audit/2026-08-11-code-leanness/00_code_leanness.md
- **What it is:** findings document of the code-leanness audit, 2026-08-11, lane IN, ED-IN-0159, baseline `ff9e3e3`; three passes (Opus census, read-only critic, PR #304 systems divergence audit); §7 connectivity matrix; §8-§9 Jordan's centralization directive.
- **Status:** "REFERENCE — observation with evidence; nothing ruled, nothing executed". Reading: mostly historical; the engine/systems-side findings (degree producers, rng fallback, definition collisions, uncited constants) and the directive are design-relevant leads; tools-side ones are process.
- **Bears on:** CORE, DICE, PC, MB, SC, FA, CHAR, SE, PROCESS.
- **Content that matters:**
  - Directive (Jordan 2026-08-11, :615-625): "Callables should be defined ONCE in centralized locations if appearing across multiple subsystems, or as a dictionary within the subsystem..."; target measured 200 definitions -> 20, 140 mechanical (copies agree) + 40 needing a ruling (:632-655). Disagreement blocks only *implicit* merging (:657-686); the one stated exception is #304's B11 (rebasing `standing` onto `contest.primitives.Standing` adds +5 to two dice pools).
  - Degree ladder: 16 producers, 6 vocabularies, 5 Overwhelming formulas, four incompatible meanings of `net` all typed `(int,int)->str` (:389-396, :570-574); held ruling #0 (which `net`/`ob` convention is canonical) gates it. **Tree check:** `def degree` still in `modules/combat/core.py:67`, `systems/social_contest/sim/contest/degree_extension.py:121`, `engine/reference/contest-groundup/engine.py:70`, `engine/dice_engine/dice_engine.py:236 degree_from_net`, plus `engine/season/seam/ladder.py:111 degree_ladder` - still multiple owners (live for DICE/CORE).
  - rng fallback: `dice_engine` uses `random.Random()` (unseeded, not reproducible under `random.seed`) while `massbattle` uses global `random.random()` (:441-445). **Tree check:** `engine/dice_engine/dice_engine.py:210,227` still `random.Random()`; `engine/season/seam/wrappers/sigma.py:488,533` also fresh unseeded `random.Random()` (documented). Still live as a determinism question [DICE/CORE].
  - Provenance: 354 citations of 12 evacuated `params/...` paths in 74 files; 498 module-level constants, 83% carry no provenance comment, 16% cite an absent path; the typed masters (`params_tables.yaml` 669 KB, `sim_params.json`, `value_pointer_links.json`) have 0 readers in `engine/`+`systems/` (:129-155, :726-757). "A provenance comment is not a pointer; it is a promise nobody checks." **Tree check:** 38 `.py` files still cite `params/core.md` or `params/contest.md`.
  - Dead scope in blocking gates (compliance_check dead functions, `ci_co_file_checker` Rule 4 on evacuated `engine/params/`, `designs/` policy row, `ci_supersession_check`/`ci_audit_registry_check` always-exit-0 in the blocking tier) (:157-236); two dead-code censuses wrong in opposite directions (`build_apparatus_registry` counts py_compile as invoked; `dead_primitive_census` has no stub concept) (:303-328).
  - Connectivity matrix over 127 modules/33,021 LOC (:524-609): 27 definition collisions (8 with disagreeing values: `CI_CEILING`, `CONVICTIONS` (characters vs world), `WEAPONS`/`TRADITIONS` literals in `workbench/balance.py`, `GOLDEN_*`); `TN_STANDARD=7` defined in `sigma_leverage.py:79` and `threadwork/sim/operations.py:46`; 144 of 292 cross-subsystem vocabulary edges have no import path; strongest design edge `combat <-> social_contest` 40 (shared resolution substrate).
  - Evidence hierarchy for deadness: behavioural (`harness.py` DEAD verdict) > hand-filtered referential > raw instrument output (:326-328); four "uncalled" factions modules are reached by `engine/tests/test_pipeline_reach.py` via string module path (:284-301); an instrument that lives inside its own population counts itself (:345-352).
- **Conflicts / stale:** `tools/dead_primitive_census.py`, `tools/index_gen.py`, `tools/doc_index_gen.py`, `tools/atomizer.py`, `deprecated/`, `tools/sim_harness` all absent now; `obs_core`/`tools/observability/` absent from `tools/` (`ls tools` shows no `observability/`). The `params/` provenance defect is **still live (38 files)**. ED-IN-0175 later retired generators to `deprecated/` which also no longer exists (CLAUDE.md §1 says no `deprecated/` tree).
- **Open items:** held #0 (net/ob convention), #1 faction_action band shift and `s==ob` dead zone, #1b strategic layer resolving on d6>=4 rather than d10 engine, #2 one owner for degree bands, #7 `standing` bounds, #8 ten dead `infrastructure.py` constants; unrun `harness.py`/`flag_ablation.py` mechanism census; `stress_battery` mirror-match FAIL (worst dev 0.500 @ arming/heavy p=0.000) undiagnosed.

### .audit/2026-08-11-code-leanness/01_plan.md
- **What it is:** the merged consolidation plan companion (Tracks G gates/tooling, S engine/systems correctness, T instruments; held-for-Jordan list), 2026-08-11, lane IN, ED-IN-0159.
- **Status:** "REFERENCE — plan of record; PARTIALLY EXECUTED 2026-08-12 (ED-IN-0160..0168)"; G1, G2, G3, G7, G8, G9 DONE; G4, G5, G6, G10, G11, Track S, Track T (T1 early) not started at write. Reading: historical (a lane plan, not the current one-active-plan under `workplans/`, CLAUDE.md §2).
- **Bears on:** PROCESS, CORE, DICE, PC, MB.
- **Content that matters:**
  - Track G (:82-94): G7 mechanical one-owner migrations (REPO, YAML load, LANES, tokens, ID_RE, ledger read) with expected-delta-none tests; G8 one `STATUS_RE` (two-sided test over 7 disputed docs); G10 repoint all 354 citations at `params_tables.yaml` plus a test that no live `.py` cites an evacuated path (not done: 38 files still cite).
  - Track S order (:96-109): A1 pin the unpinned canon ladder, B1-B3, B7-B8, B9, B10, A2, A3-A4, A6, A8, A9, B5-B6, B11; `altonian_reinforcements` item struck (accepted cross-session handoff guarded by a passing test); two additions: bind/guard the 4x faction-roster literal, disposition forked degree ladder in `skills/valoria-dice-model/valoria_dice.py:45`.
  - Track T (:111-122): promote Class-A batteries as `xfail(strict)`, build `tools/mechanism_census.py` from `flag_ablation`+`harness`+`interaction`+`reachability_sweep` and RUN it before ruling #1, #1b, #2, #8.
  - Held list (:126-139): ruling #7 `standing` mutator kept (reusing `Standing` adds +5 to two dice pools).
- **Conflicts / stale:** G2 note states the earlier "blocked by test_evacuation_plan" claim was wrong (:15-21); "There is no G12 or G13" (:23-26) contradicts findings §8.4 which names NEW G12/G13 (the findings doc was not updated). `deprecated/tools/` destination no longer exists.
- **Open items:** G4/G5/G6/G10/G11, Track S/T unstarted at the time; the HELD rulings.

### .audit/2026-08-11-code-leanness/connectivity_matrix.py
- **What it is:** 218-line read-only instrument deriving definition collisions, cross-subsystem vocabulary throughlines and hidden (import-free) coupling over `engine/**/*.py` + `systems/**/*.py` (git-tracked).
- **Status:** none (script). Reading: dead instrument as filed; the method is reusable.
- **Bears on:** CORE, PROCESS.
- **Content that matters:**
  - Regex harvest of module-level `CONSTANTS`, def/class names, quoted tokens and bare calls (`(?<![.\w])([a-z_]{4,})\s*\(`), STOP list of stdlib verbs; imports via regex; `subsystem_of()` maps `systems/<sub>` and `engine.<x>` (:70-77, :80-124).
  - Hard-codes `REPO = ../..` from `audit/<dir>/` and `SELF='audit/2026-08-11-code-leanness/connectivity_matrix.py'` (:46-47); under `.audit/<dir>/` the `..\..` resolves to `.audit`, not the repo root, so `git ls-files` runs in the wrong cwd [UNVERIFIED by running]. Corpus globs `engine/*.py`, `systems/**/*.py` omit `modules/` (new layer 2).
  - Nothing reads it.
- **Conflicts / stale:** path anchor and corpus scope outdated (`modules/` and `engine/season/` are the game code now). **Open items:** none.

### .audit/2026-08-11-code-leanness/duplication_census.py
- **What it is:** 250-line census script reproducing every number in file 00 (shared-library adoption, primitive re-implementation, five `## Status:` regexes vs tracked `.md`, evacuated `params/` citations, syntax-gate coverage, audit probe runnability, forked `MU_PER_DIE`, ledger ID uniqueness); self-invalidating (exit 1) when a claim stops reproducing.
- **Status:** none (script). Reading: dead instrument (REPO anchored to `audit/`, reads `tools/`, `skills/`, `.github/...` shapes that have changed).
- **Bears on:** PROCESS.
- **Content that matters:**
  - Section 6 (:199-236): ledger ID uniqueness check and `next_free` ahead-of-ledger check for lane IN - the guard shape the churn audit also named (no id twice across ledgers); never turned into a tracked guard.
  - Section 2 (:140-165) counts `params/...md` citations in all tracked `.py`; still would report a large non-zero count (38 files per one grep).
  - Self-exclusion by path `SELF` (:27, :41): any move of the file breaks the self-exclusion (the instrument counted itself once, 00 §2.4).
- **Conflicts / stale:** `.audit/` path vs `audit/` constants; the `deprecated/` filter and `git ls-files audit/**/*.py` look in the wrong tree. **Open items:** none.

### .audit/2026-08-11-world-schema-gap-audit/00_orchestration_plan.md
- **What it is:** method record of the world-schema gap audit run (ED-IN-0153), 2026-08-11, lane IN; three passes (A strata 4 lanes, B lenses 5 lanes, C config 3 lanes) + 4 critics + 1 synthesis, over `.claude/wf_world_schema_gaps.js`.
- **Status:** "REFERENCE — method record for the ED-IN-0153 run. Ratifies nothing." Reading: historical (schema = key_type_registry + module_contracts, now partly retired).
- **Bears on:** CORE, WR, CHAR, SE, FA, PROCESS.
- **Content that matters:**
  - The question: "What does the world model logically require that the schema cannot express?" where schema = `systems/_architecture/key_type_registry_v30.md` (55 key types) + `references/module_contracts.yaml` (27 modules); a blank cell in a generated view means "not declared", not "none" (:14-27).
  - Entity ladder character -> settlement -> settlement faction/governance -> territory -> provincial faction -> national faction; 18 lenses (corrected from "19": the list enumerates eighteen, :51); Pass C names three individuation failure shapes: flavour with no hook, hook with no variation, hardcoded singleton (scripting drift) (:55-64).
  - Scope stops (:105-125): no key type may be appended because `rendering_dispositions.yaml` does not exist; no scale-vocabulary unification (ED-IN-0103 fork); merge does not ratify.
  - Section 7 correction (Jordan in-session): "Valoria has no PC/NPC distinction" - the character entity is the `NPC` dataclass in `systems/world/sim/npe.py`; identity recorded twice with no bridge (`NPC.territory_id` province grain; `Settlement.npc_ids` settlement grain; no `settlement_id` on any character; bare `actor_id` strings a third representation) (:144-175).
- **Conflicts / stale:** `systems/world/sim/npe.py` and `systems/factions` are gone; character identity now lives in `engine/season/` (npcs.yaml, state). `.claude/wf_world_schema_gaps.js` harness presence [UNVERIFIED]. Critics' model tiering (fable not on synthesis) matches CLAUDE.md §10.
- **Open items:** character-identity owner (whether `engine/season/state` now owns it - CHAR lane).

### .audit/2026-08-11-world-schema-gap-audit/01_gap_register.md
- **What it is:** part 1 of 4 of the world-schema gap register (rows G-01..G-14) plus the index of all 50 rows; ED-IN-0153, 2026-08-11, lane IN; 75 raw findings from 12 producer lanes -> 50 rows after critic verdicts.
- **Status:** "REFERENCE — observations against the tree. Ratifies nothing." Reading: historical (schema = Key registry + module_contracts, since retired); but the underlying design gaps (what state has no owner) are lead material for CHAR/FA/SE/WR/CORE.
- **Bears on:** FA, CHAR, SE, WR, CORE, MB.
- **Content that matters:**
  - Index/dispositions (:18-86): 20 `propose_contract`, 13 `needs_jordan_ruling`, 8 `propose_key`, 4 `already_tracked`, 3 `propose_authoring_field`, 1 each `propose_descriptor` and `not_a_gap`; kinds: 16 missing_owned_state, 6 missing_key_type, 6 missing_edge, 5 missing_individuation_descriptor, 4 each missing_payload_field/missing_authoring_schema/vocabulary_conflict, 3 missing_contract_module, 2 scale/transition.
  - G-01 (:94-106): no key announces a faction coming into/going out of existence (Stage-4 declaration, collapse, split, promotion); `check_insurgency_promotion` sets two fields and returns; "which factions exist is a 4-entry Python literal, not schema". G-02: `faction_state` owns 3 state rows against a canon schema of ~9-12 fields (mission, role, culture, hierarchy, cascade fidelity, Public Expectation, strictness); cascade resolution has zero implementation.
  - G-03: territory temperament (5-typology alpha/beta) has no contract row and its only implementation `temperaments.py` is a zero-importer orphan. G-04: `Settlement.governor_id`, no key expresses a governor change, `succeed_governor` has zero production callers. G-05: Renown (0-10, 8 triggers, gates the Stature Ladder) has no key, no state row, no module (player_agency has no row); needs ruling because folding into npc_behavior is shape divergence and promoting it out of `not_descriptors.tracks` special-cases one of seven.
  - G-06 Casus Belli (granted by treaty breach/Outlawry/Excommunication; `getattr(world,'casus_belli',None)` with zero writers => every CB branch unreachable); G-07 `World.treaties` real but no module owns it, `process_treaty_expirations` zero production callers; G-08 `state.standing_change` lacks faction_id/ladder_id (4 main ladders + 7 sub-office ladders; Niflhel four independent arms); G-09 caste (load-bearing per canon) absent from every schema and from `references/npc_registry.yaml`; G-10 fractional province ownership (ED-711) has no owner; G-11 Franchise (DRAFT doc) not allocatable; G-12 geography/march layer (49 adjacency edges, terrain_cost_matrix, march_budget) implemented by zero gameplay code; G-13 the 13-Conviction weighted vector is unowned at runtime and four incompatible conviction shapes coexist; G-14 never-playable NPC factions (Altonia, Schoenland, ...) have no instances.
  - Method notes inside rows: proposals corrected for wrong enum ('ledger' is not a bucket; buckets are exactly {clock 14, derived_value 7, pool 2, track 17}); `'provincial'` is not in `keys.py` SCALES (personal/settlement/territory/peninsula) and would raise; modifying a key's required payload is a Class A supersession (more expensive than a new type).
- **Conflicts / stale:** all state/key/contract targets (`module_contracts.yaml` rows, `key_type_registry_v30.md`, `engine/autoload/game_state.py`, `systems/factions/sim/*`, `systems/world/sim/npe.py`) are the pre-`engine/season/` architecture; those paths are gone (checked `systems/factions`, `systems/world/sim`, `engine/autoload`). Several design facts persist in `engine/season/*.yaml` [UNVERIFIED which].
- **Open items:** the 13 `needs_jordan_ruling` rows (G-05, G-11, G-17, G-19, G-21, G-22, G-24, G-32, G-33, G-35, G-38, G-42, G-47) - see 02_verdict.

### .audit/2026-08-11-world-schema-gap-audit/01_gap_register_part2.md
- **What it is:** part 2 of 4 (G-15..G-29): scripting-drift singletons, the blocking `rendering_dispositions.yaml` precondition, parser defect, character-roster orphan, scale-vocabulary seams.
- **Status:** "REFERENCE — observations against the tree. Ratifies nothing." Reading: historical; design-level claims retain lead value.
- **Bears on:** CORE, FA, SE, CHAR, WR.
- **Content that matters:**
  - G-15 scripting drift: `Territory.templar=(tid=='T9')`, prosperity from an inline set literal, fort_level from `STARTING_GARRISON` in `create_world()` while the geography YAML authors per-province `fort_level`/`starting_pros`; a proposed spiritual_weight threshold was rejected (T15 Askeheim = 5 > T9 = 4). G-16: faction-unique mechanics dispatched by `faction.name == 'Crown'/'Church'` string compare; `mechanics_index.yaml:939-966 faction_unique_actions` already is the faction -> capability map; three Church/Crown booleans sit on every Faction.
  - G-17 BLOCKER: `key_type_registry_v30.md` section 10 (RATIFIED 2026-07-07, ED-IN-0026) requires a row in `references/rendering_dispositions.yaml` (does not exist) before any new Key type; plus generated `key_types.json` export and Godot mirror.
  - G-18 executable defect: registry parser at `keys.py:294` treats a flow list with a trailing `#` comment as a raw string, so `apply_defaults` makes a list of characters and invariant 7 raises; at least 2-3 registry entries affected; no guard.
  - G-19: `meta.knot_formed` tier enum 'Loose|Medium|Close' is the STRUCK PP-632 model (Distant/Close strain model is canon, ED-912) and propagated into generated `key_types.json`; `supersession_register.yaml` `files_to_recheck` omitted the registry. G-20: `references/npc_registry.yaml` is the enforced canonical roster of named characters yet referenced by zero contracts or key types. G-21/G-22/G-43: scale hierarchy B12 (Settlement<Territory<Province<Duchy<Country) has no schema representation; four-five parallel scale vocabularies held at ED-IN-0103 fork 1; faction tiers (local/provincial/national) have no field.
  - G-23: NPC-NPC relational graph (PP-724, six edge types) is design-only, `canon/relational_edges_v30.yaml` never created. G-24: the state bucket taxonomy has no shape for per-counterparty relations or continuously updated meters (Field/Gauge sketch in `governance_type_registry_v1.md`). G-25: Church Attention Pool, Guild Favour and legacy Prosperity are unowned per-territory tracks. G-26/G-27/G-28/G-29: no key for territory revolt (Accord 0), province coherence form/dissolve, conviction resolution (Fulfilled/Failed/Transformed/Unresolved; canon cites ED-686 which is unrelated Co-Movement calibration), or project formation.
- **Conflicts / stale:** corrections appended inline (ED-IN-0157): G-19 "none found" overturned by `supersession_register.yaml:227-230`; G-25 softened by `tools/observability/INCOMPLETENESS.md:336`. Substrate-specific rows (G-17, G-18, G-26..G-29) moot after Key retirement; whether the same design gaps exist in `engine/season/` is for CORE/CHAR.
- **Open items:** G-17 (who authors `rendering_dispositions.yaml` and backlog order), G-21 (B12 tier), G-22 (faction tier field), G-24 (Field/Gauge primitive).

### .audit/2026-08-11-world-schema-gap-audit/01_gap_register_part3.md
- **What it is:** part 3 of 4 (G-30..G-45): population, governance, economy, military unit, sanctions, deniability, subnational factions, starting-world configurability, memory references, affiliation, mortality.
- **Status:** "REFERENCE — observations against the tree. Ratifies nothing." Reading: historical; lead material.
- **Bears on:** SE, FA, MB, CHAR, WR, CORE.
- **Content that matters:**
  - G-30: `env.population_change` has no Population field to land on; `settlement_economy` is a phantom stub recommended for retirement; compose on Settlement Weight. G-32: settlement-to-settlement grain/economic flow (Requisition displaces Dearth) has no edge; BALANCE-005 contradiction (archive resolved 2026-04-13 "narrative pressure, not mechanical" vs ED-SE-0009 reopening as mechanical rule).
  - G-33: persistent individuated military-unit entity (`units.py:325 Unit` battle-scoped, unregistered; garrison is a bool) crosses the MB single-writer boundary (`module_contracts.yaml:566-572`); needs ruling. G-34: five Parliamentary Sanction statuses and Recognition/Succession Endorsement outcomes have no state field. G-35: Shadow Renown/Deniability Debt (ED-632/633 CANON) are marked DEPRECATED in three registries (currency conflict).
  - G-36 and G-37: six of seven subnational-faction archetypes exist only in `Settlement.subnational` (dead dict with three occurrences) and `controller_subordinate` (S-014 Ehrenfeld Loewenritter under Crown) is dropped by the loader whose docstring claims one controller entry only while all 37 settlements carry one.
  - G-38: nothing expresses which starting world a campaign uses; `create_world()` takes only a seed; hardcoded `STARTING_OWNER/STATS/ACCORD/PT/GARRISON` dicts but `valoria_geography_v30.yaml` is an authored world-data locus loaded by `populate_from_geography`. G-39: npc_memory `MemoryReference` (salience 0-7, 10-per-NPC cap) has nowhere to be stored. G-40: `NPC.affiliation_faction` has no mutator. G-41: no typed NPC lifecycle status; ED-898 rules named characters are incapacitated/captured not killed in mass battle.
  - G-42: `env.crisis` and `mechanical.season_change` declare wildcard consumers; G-44: settlement->province membership has no contract locus (`province_id` free string); G-45: parliamentary_transfer / mass_seizure have no contract row (mass_seizure UNREACHABLE, zero production callers).
- **Conflicts / stale:** inline corrections: G-36 "none found" overturned by `.audit/2026-08-10-subsystem-atlas-verification/code_strategic.md`; G-44 OI-37 anchor false (HANDOFF_SE has zero OI-37). Code targets (`registry.py`, `game_state.py`, `npe.py`) predate `modules/settlements` and `engine/season`.
- **Open items:** BALANCE-005 reconciliation; Deniability Debt currency; MB unit entity ownership; population owner.

### .audit/2026-08-11-world-schema-gap-audit/01_gap_register_part4.md
- **What it is:** part 4 of 4 (G-46..G-50): succession scale signature, A6 piety_track edge, per-territory authored inputs unread, institutional_culture unread, NPC residence two grains (not a gap).
- **Status:** "REFERENCE — observations against the tree. Ratifies nothing." Reading: historical; lead material.
- **Bears on:** SE, FA, CHAR, WR, CORE.
- **Content that matters:**
  - G-46: settlement_layer 1.8b (PROPOSED, ED-SE-0012) needs `state.succession` to carry settlement scale; file against ED-SE-0012 at ratification. G-47: the 9th A6-violating pair (`piety_track` receiving `scene.*` from `scene_slate`) likely dissolves under ED-IN-0103.
  - G-48: authored provinces block (spiritual_weight, proximity_calamity, starting_pros, fort_level) is read by no production code; `settlement_generator_v1.md:45` declares spiritual_weight 0-2 and Cathedral gate >=2 while data authors 4 and 5 (range defect). G-49: `institutional_culture` is read by zero Python lines; six factions collapse to four values (-0.1 thrice); the whole cascade subsystem is unimplemented.
  - G-50 not a gap: both NPC residence fields are unpopulated (`generate_npc` has no production call site; acceptance test xfail(strict) keeps npc_counter 0).
- **Conflicts / stale:** G-49 inline correction: citation of `_workings_joined.md:978` reversed ("consumed, not orphaned" at design level vs zero Python readers).
- **Open items:** none new.

### .audit/2026-08-11-world-schema-gap-audit/02_verdict_and_residuals.md
- **What it is:** verdict, held decisions (17), residual coverage statement and critic-added items for the ED-IN-0153 gap audit, 2026-08-11, lane IN.
- **Status:** "REFERENCE — observations against the tree. Ratifies nothing." Reading: historical; the "what was not covered" list is the useful part for the current suite.
- **Bears on:** CORE, FA, SE, CHAR, WR, PC, SC, FI, MB, PROCESS.
- **Content that matters:**
  - Ladder verdict (:13-21): the schema cannot express the ratified entity ladder (Country > Duchy > Province > Territory > Settlement vs a 4-value runtime SCALES); at the faction rung no key announces faction birth/death; "a second campaign would differ from the first essentially by RNG seed" (individuation: zero code readers for spiritual_weight, proximity_calamity, starting_pros, institutional_culture; faction dispatch by name string).
  - Instrument defect (:25-62): `tools/wf_harness.js` `hSameFinding` gates on `hFirstFile(a)===hFirstFile(b)` so every `rediscovery` value was 1 across 75 findings; the corroboration signal was absent; the `x` column in the register is a hand reconstruction. Guard to ship with any fix: two paraphrases citing different files must group to 2 (ED-IN-0154).
  - Not covered (:107-130): no findings from combat (PC), social_contest (SC), fieldwork/investigation (FI), threadwork, articulation/UI, npcs beyond the relational graph, victory beyond Altonia; world history and threadwork lenses empty; no PP citation verified (CLAUDE.md §0: 433 of 452 distinct PP numbers resolve to no register); no finding verified by execution; "existing tracking: none found" unreliable (about a dozen wrong, because only `editorial_ledger*.jsonl` was grepped).
  - Three overturned producer claims and two damaging proposals (templar-by-threshold would site the station in Askeheim T15; Franchise wiring into consuming_systems reverses ED-IN-0096) (:126-128).
  - 17 held decisions (:66-103) incl. G-17 rendering_dispositions, G-21/G-43 scale vocab, G-22 faction tier field vs module, G-38 singleton start world, G-24 Field/Gauge, G-35 Deniability Debt currency, G-32 BALANCE-005, G-33 MB single-writer, header contradictions (fractional_province_ownership PROVISIONAL/CANONICAL/PROVISIONAL; march_layer CANONICAL/PROVISIONAL), ED-686 citation passes the ED gate while resolving to unrelated content, CLAUDE.md §§4-7 deleted (ED-IN-0147) yet contracts cite "CLAUDE.md §6".
- **Conflicts / stale:** the held list's substrate-bound items die with the Key retirement; design-bound items (G-22 faction tier, G-38 starting world, G-05 Renown owner, G-35 Deniability Debt) may persist. `tools/wf_harness.js` presence [UNVERIFIED].
- **Open items:** all 17; the unread subsystems (PC, SC, FI, threadwork, UI) are exactly the audit-suite subsystems now.

### .audit/2026-08-11-world-schema-gap-audit/03_discussion.md
- **What it is:** analysis of the 50 rows into five patterns, what the schema gets right, adversarial corrections to the discussion itself, decision surface; ED-IN-0153/0154, 2026-08-11.
- **Status:** "REFERENCE — analysis of observations already filed. Ratifies nothing." Reading: historical; the five patterns and the individuation result are design-level.
- **Bears on:** CORE, CHAR, FA, SE, WR, PROCESS.
- **Content that matters:**
  - Five patterns (:134-): P1 built and unowned (`World.treaties`, `governor_id`, temperament, Church Attention, `env.population_change`), P2 nothing announces existence ("an emergent-narrative engine whose entities cannot be created at runtime has a fixed cast by construction"), P3 arity too narrow (`standing_change`, bilateral `da.diplomatic_alliance`), P4 missing scale rung and five vocabularies, P5 individuation. Ratio: `missing_owned_state` (16) + `missing_edge` (6) vs `missing_key_type` (6): "The engine can mostly announce; it largely cannot hold."
  - Individuation measured by hand (:236-278): `spiritual_weight`, `proximity_calamity`, `starting_pros` zero Python readers; `institutional_culture` zero readers and values `0.0,-0.1,-0.2,-0.1,+0.1,-0.1`; `templar=(tid=='T9')`; `faction_unique_actions` in `mechanics_index.yaml` has zero Python readers.
  - Controls: 75 findings and 59 clean entries; `KEY_INDEX.md` contradictions list "None"; threadwork and `faction_politics` are contract templates but NOT audited code (:91-105); three of the author's own pre-run leads were refuted (Domain Echo `scene_outcome`, 20 A6 violations, 8 consumerless keys) (:303-316). "NPE's 5-axis genome ... narrower than the five axes suggest" - stance base 3 keyed on territory, loyalty deterministic by faction, deviation die flips one axis (:122-130).
  - Compression-drops-qualifier as a third error class (:346-349); decision surface ordered G-17, G-24, G-21/G-43, G-22, G-38 (:394-421); G-18 parser defect is a correction not a ruling; G-19 is a Class A supersession (:423-434).
- **Conflicts / stale:** relies on `systems/world/sim/npe.py`, `engine/autoload/game_state.py` (gone). **Open items:** G-38 (is a singleton start world intended?), the 25+ other held rows.

### .audit/2026-08-11-world-schema-gap-audit/04_key_io_and_propagation_map.md
- **What it is:** traced map of the declared and built Key bus (55 types, 7 families, 27 modules), emit ledger, subscriber wall, throughlines T1-T5, broken throughlines B1-B12, proposed keys placed on the bus; ED-IN-0153/0155, 2026-08-11.
- **Status:** "REFERENCE — a traced map over existing artifacts. Ratifies nothing." Reading: superseded as an architecture description (Keys retired, ED-IN-0232); useful as a record of which cross-subsystem links were dead.
- **Bears on:** CORE, SC, FA, MB, PC, WR, SE, CHAR.
- **Content that matters:**
  - Transport (:17-44): deferred-apply `sched.emit(key, apply=fn)` (2 live sites), log-only (2), subscribe (13 type_ids, all stub callbacks); `schedule_emission` has zero production callers and `DEFAULT_CASCADE_DEPTH_MAX=0`; "the cascade half of the substrate is switched off by default and has never run in production".
  - Live emit ledger (:190-213): 4 call sites, 5 type_ids: `scene.accord_echo` (writes `Settlement.order`), `scene.contest_resolved` and `scene.combat_resolved` (write a faction stat delta), `da.public_governance` and `scene.battle_concluded` (log-only inside swallowing `try/except`); "5 of 55 type_ids emitted (9%), 3 write state". `KEY_TYPE_BY_SCENE` maps only the two personal-scale resolvers.
  - T1 is the one fully closed loop (scene -> accord echo -> `Settlement.order`); T2 Domain Echo personal -> faction skips settlement/territory/province (:235-257). Broken throughlines B1-B12 (:272-292): eleven of twelve break at the consumer or state end ("The engine can say what happened. It cannot record it, and it cannot hear it").
  - `test_key_graph.py` docstring figure "1 of 55 emitted" was unguarded and wrong (ED-IN-0155) (:159-188); `keys.py:294` flow-list parser defect (:417-439); `SCALES` four values, 'provincial' 0 of 55 (:384-415).
  - Subscribed (13) vs emitted: 11 of 13 subscribed types are never emitted; 3 of 5 emitted never subscribed (:225-229, :453-457). Modules `campaign_architecture` and `clock_registry` on the bus roster with zero edges (:81-90).
- **Conflicts / stale:** entire substrate retired; `echo_transport`, `parliamentary_bridge`, `scene_dispatch` gone (checked `engine/cross_scale` absent). Confirms the retirement rationale (transport sound, endpoints not). **Open items:** none that survive retirement except the architectural lesson - declared consumers with no rule content and no joint test of emitted vs subscribed.

