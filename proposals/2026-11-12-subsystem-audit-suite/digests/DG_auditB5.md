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

