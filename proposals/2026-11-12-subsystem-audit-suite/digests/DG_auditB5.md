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

