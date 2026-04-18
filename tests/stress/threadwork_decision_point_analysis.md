# Threadwork Decision Points vs Arc Register — Analysis

> **Date:** 2026-04-11
> **Sources:** threadwork_redesign_v25.md, params_threadwork.md, arc_register.md (v4)
> **Method:** For each key threadwork decision point, test whether the arc register captures the emergence conditions and cascade effects. Identify gaps and generate new arcs.

---

## Decision Point 1: Discovery Event Cascade (TK 4 + Originary Locks)

**Mechanic:** At TK 4, Vaynard offers his entire Private Collection including originary Locks. Each Lock is the same class of object that: (a) caused three Cardinals to request reassignment, (b) Klapp accumulated CE 4 from, (c) could trigger Discovery Events in any TS 10+ character who handles them. Spirit TN 7 Ob 1 per exposure.

**Test against register:** ARC-S01 (Vaynard Cascade) mentions TK 4 → Collection offered → "potential multi-character Discovery Events." But the register does not trace the cascade: if Vaynard distributes originary Locks to practitioners AND non-practitioners, every TS 10+ handler rolls Spirit TN 7 Ob 1. In a single season, this could fire Discovery Events for: Haelgrund (TS 12 — NPC-ARC-HAE accelerated), Torsvald (TS 35 — NPC-ARC-TOR compounded), Klapp (TS 31 — ARC-S21 accelerated), any Player Character with TS 10+, and potentially Strand, Almstedt, or other NPCs with unknown TS.

**Impact on existing arcs:**
- ARC-S01: correctly notes TK 4 consequences but understates cascade scope
- NPC-ARC-HAE: Haelgrund Defection can fire from Lock exposure, not just practitioner Diagnosis
- ARC-S21: Klapp Threshold can accelerate if Locks circulate outside Church
- ARC-S08: Faith that Destroys — Klapp's CE from archive Locks is the slow path; distributed Locks are the fast path
- Collision A: Church Double Fracture — if Locks fire Discovery Events in BOTH Klapp AND Haelgrund simultaneously, Church loses education + investigation + Olafsson exposure = triple fracture

**Gap:** The originary Lock distribution at TK 4 is a single decision point that can trigger 3–6 Discovery Events in one season. This is the highest-impact single decision in the campaign's threadwork system and it is underspecified in the register.

→ **NEW ARC: The Lock Distribution (see below)**

---

## Decision Point 2: Weaving at Relational+ Scale → Over-Actualisation → Brittleness

**Mechanic:** Successful Weaving at Relational+ drives configuration toward excess coherence. Over-actualisation: subsequent ops on same config +1 Ob. If non-Thread stress strikes (siege, betrayal, institutional collapse), the Woven configuration shatters into a Shifting Object at its scale. A Relational Shifting Object deteriorates to a Relational Gap within 1d3 seasons.

**Test against register:** ARC-S02 (Brittle Peace) captures the core mechanic but stops at "Consequence genre fires on fracture." It does not trace the full cascade: Woven treaty → political stress → shatters into Relational Shifting Object → deteriorates to Relational Gap (1d3 seasons) → RS −4/season from Gap persistence → requires Mending (TS 50+, Ob 5–6) to resolve. A single failed diplomatic Weaving that shatters can produce RS −8 to −12 over 2–3 seasons if the resulting Gap isn't Mended.

**Impact on existing arcs:**
- ARC-S02: needs cascade extension — brittleness is not just a failed agreement, it's an RS drain source
- ARC-P02: RS decay sources should include shattered Woven configurations as a category
- ARC-S15: Southernmost Spiral — if practitioners Weave the Southernmost boundary and it shatters under stress, the cracking timeline accelerates dramatically

**Gap:** The register treats over-actualisation as a single-event hazard. It is actually a delayed RS drain that compounds with existing decay sources.

→ **Affects ARC-S02 (extend description). No new arc needed — the cascade is part of Brittle Peace.**

---

## Decision Point 3: Mass Battle RS ×3 Multiplier (PP-192)

**Mechanic:** All RS costs from Thread operations in mass battle ×3. Coherence costs unaffected.

**Test against register:** ARC-S04 (Rendering Debt) mentions "×3 multiplier per PP-192" but does not quantify the cascade. At RS 60 (game start TTRPG):
- A single failed Weaving in mass battle: RS −2 × 3 = −6
- Two failures in one battle: RS −12 (capped at −10/season)
- One battle can push RS from 60 (Strained) to 50 (crossing into Fragile threshold zone)
- A failed Lock in mass battle: RS −3 × 3 = −9
- A failed Dissolution in mass battle: RS −8 × 3 = −24 (capped at −10, but the cap applies at Accounting — multiple operations within a single battle are mid-scene and may stack before the cap is checked)

**Impact on existing arcs:**
- ARC-S04: the "practitioner as battlefield Thread asset operating every turn" is mechanically suicidal for RS. A 3-round battle with one Weaving per round (base case): RS −0 × 3 = 0 (success), but with one Partial and one Failure across 3 rounds: RS −1 + −2 = −3, × 3 = −9. One bad battle = RS pushed 9 points toward Rupture.
- ARC-P02: mass battle is the single fastest RS drain in the system, faster than Lock drift or Gap persistence
- Collision C (Tutoring + Southernmost): if the Ceiral Ritual failure coincides with a mass battle where practitioners are operating, the RS cascade is multiplicative

**Gap:** The register notes the multiplier but does not identify mass battle as the system's primary RS acceleration mechanism. A single mass battle with Thread operations can advance the RS timeline by 2–4 seasons of passive decay in one Accounting period.

→ **Affects ARC-S04 (quantify cascade). No new arc — but the severity is underspecified.**

---

## Decision Point 4: Mending as Sole RS Recovery (Coherence −1 per attempt)

**Mechanic:** Mending is the only practitioner operation that restores RS (+1 Success, +2 Overwhelming). But every Mending attempt costs Coherence −1 regardless of outcome. Coherence 10→0. At Coherence 0: Rendering Crisis → Non-Player Character if unresolved by season end. Recovery from Rendering Crisis requires: full season no practice + 3 Anchoring Scenes + resolution roll (TN7 Ob3). Success restores Coherence 3 but costs TS −1 permanent. Failure = Non-Player Character.

**Test against register:** ARC-P02 (RS Decay) lists Mending as a recovery source. ARC-S16/S17/S18 (Coherence Zero) treat Coherence 0 as an endgame arc for specific NPCs. But the register does not capture the structural trap: the world needs Mending to survive, but Mending burns out the practitioners who perform it.

**Quantification:**
- Starting Coherence: 10
- Mending costs: −1 per attempt
- A practitioner can attempt ~7–8 Mendings before reaching Coherence 2 (Fractured — Belief Co-Authorship begins, +1 Ob all Thread ops)
- After ~10 Mendings total: Coherence 0 → Rendering Crisis
- Each successful Mending: RS +1 or +2
- Net RS recovery per practitioner lifetime: +10 to +20 RS before burnout
- RS decline rate (passive): Lock drift (−1 to −2/season per Lock) + Gap persistence (−4/season per Gap) + Winter (−1/year) + failed operations
- With 2 active Locks and 1 persistent Gap: RS decline = −6 to −9/season
- One practitioner's entire Coherence budget (10 Mendings ≈ +10 to +20 RS) covers ~2–3 seasons of passive decline

**Impact on existing arcs:**
- ARC-P02: RS recovery is structurally insufficient unless multiple practitioners Mend AND Locks/Gaps are resolved simultaneously
- ARC-S25 (Warden Cooperation): WC ≥ 2 = RS decay halved; WC ≥ 3 = RS +2/season. Warden cooperation is not just helpful — it is NECESSARY because practitioner Mending alone cannot sustain RS
- ARC-S15 (Southernmost Spiral): Ceiral Ritual success (RS −6 to −10) is the only source of RS recovery large enough to offset multiple decay sources simultaneously
- Community Weaving (PP-195): Revolution RS +1/+2 per success — the ONLY non-practitioner RS tool. Requires Mandate ≥ 1. This makes ARC-S10 (Revolution Eats Itself) an RS crisis arc, not just a political one

**Gap:** The structural trap — practitioners burn out saving the world — is the campaign's central mechanical tragedy and has no arc entry.

→ **NEW ARC: The Mending Trap (see below)**

---

## Decision Point 5: Cross-Faction Collective Operations (Belief Gating)

**Mechanic:** When practitioners from different factions cooperate, Belief compatibility determines contribution quality. Directly opposing Beliefs: pre-Leap check (Spirit TN 7 Ob 1) or helper drops. Tangential conflicts: helper dice don't chain on 10. This means cross-faction cooperation — essential for endgame RS recovery at RS Critical — is gated by whether practitioners share compatible Beliefs.

**Test against register:** No arc captures this. The endgame configuration requires "practitioner cooperation across faction lines" (threadwork v25 §5.3 design note) but the register's endgame table doesn't note the Belief-gating constraint.

**Impact on existing arcs:**
- Collision B (Practitioner King): Almud as practitioner-king cooperating with Edeyja requires Belief compatibility check. Almud's "ethical doubt" Belief and Edeyja's "duty to substrate" Belief are tangentially conflicting (governance pragmatism vs deontological duty) → Almud's dice don't chain. Almud is a weaker practitioner ally than his TS would suggest.
- ARC-S04 (Rendering Debt): battlefield collective operations between Crown and Varfell practitioners require Belief checks. Vaynard's revolutionary Beliefs directly oppose Crown institutional Beliefs → Spirit TN 7 Ob 1 to participate → ~40% chance of dropping out per battle
- ARC-S25 (Warden Cooperation): Edeyja's Beliefs (deontological duty to substrate) align well with Mending-focused practitioners. She is the best collective operation partner in the game — high TS, compatible Beliefs, no tangential conflicts with pure Mending intent.

**Gap:** The Belief-gating mechanic determines which practitioner alliances are mechanically viable for endgame RS recovery. The register treats practitioner cooperation as a binary (cooperate or don't) rather than a spectrum (full dice, non-chaining dice, Spirit check required, incompatible).

→ **NEW ARC: The Lattice of Enemies (see below)**

---

## Decision Point 6: Lock Chronic Drift (RS −1 to −2/season)

**Mechanic:** Every active Lock produces RS drift: 2–3 seasons = −1/season + ops +1 Ob. 4+ seasons = −2/season. Permanent Locks (Einhir Catastrophe Locked Zones): drift ceases but permanent +1 Ob adjacent. Removing a Lock (via Dissolution: RS −5 to −8 immediate) eliminates chronic drift.

**Test against register:** ARC-P02 mentions Lock drift as a decay source. ARC-T07 (Dissolution) captures the player choice to dissolve. But neither captures the structural calculus: maintaining Locks costs RS over time, removing them costs RS immediately. There is a crossover point where the cumulative drift exceeds the one-time Dissolution cost.

**Quantification:**
- Lock maintained 5 seasons: cumulative RS cost = −1−1−1−2−2 = −7
- Dissolution Success: RS −5 (one-time)
- Break-even: season 5 (cumulative drift = −7 exceeds Dissolution −5)
- Dissolution Failure: RS −8 + Gap + Monstrous Incursion + practitioner incapacitated
- The decision: do you pay RS −5 now to prevent RS −7+ over time? Risk of −8 + Gap on failure?

**Impact on existing arcs:**
- ARC-P02: Lock calculus is a repeating strategic decision, not a single event
- ARC-S15 (Southernmost): the Locked Zones from the Einhir Catastrophe are PERMANENT — they don't produce chronic drift (drift ceases at permanent) but produce +1 Ob adjacent permanently. Dissolving them is the only way to remove the Ob penalty. But Dissolving a Locked Zone border requires TS 70+, Einhir framework, and Ob 8+. Only Edeyja and late-campaign PCs can attempt it.

**Gap:** The Lock calculus is a structural decision point that repeats throughout the campaign. The register treats Locks as static decay sources rather than decision points.

→ **Affects ARC-T07 and ARC-P02 (extend descriptions). No separate arc — it's a decision framework embedded in existing arcs.**

---

## Decision Point 7: Thread Operation Visibility (Detection Economy)

**Mechanic:** TS 0–9: nothing. TS 10–29: vague unease. TS 30–49: senses operation, direction. TS 50–69: identifies type and target. TS 70+: full configuration. Concealment: Cognition only (no History), TN7, Ob = observer TS ÷ 30 (round up). Pre-Leap action.

**Test against register:** The register notes detection in NPC-ARC-HAE (Diagnosis on Haelgrund) and ARC-P04 (practitioner visibility). But the detection economy as a system-level arc driver is not captured.

**Key interactions:**
- Klapp (TS 31): senses operations, general direction. This is HOW his arc fires — he senses Thread activity in Church territory that shouldn't exist. The register's ARC-S08 doesn't specify the detection trigger.
- Haelgrund (TS 12): vague unease only. He calls it "investigative instinct." He cannot detect operations directly — but he NOTICES the consequences (people acting differently, unexplained physical changes). His PROCEDURALIST flaw means he documents everything, including the unease. Over time, his documentation accumulates into circumstantial evidence of Thread activity.
- Vossen (TS 25): vague unease. Near T13/T15, the Forgetting partially erases her cultural knowledge. She senses something wrong but cannot retain the specific perception.
- Concealment from Klapp: Cognition only, TN7, Ob = 31÷30 = Ob 2. Practitioners with Cognition 4+ have ~60%+ chance of concealing from Klapp. From Edeyja (TS 75): Ob = 75÷30 = Ob 3. Much harder.

**Gap:** The detection economy determines which NPCs can fire Thread-related arcs independently (without player action) and which require player intervention. Klapp's TS 31 makes him a passive Thread sensor — his arc can fire from NPC AI tendency alone. Haelgrund's TS 12 requires accumulated circumstantial evidence.

→ **Affects multiple existing arcs (ARC-S08, NPC-ARC-HAE, ARC-P04). No separate arc needed — but a note on detection as arc driver should be added.**

---

## Decision Point 8: Community Weaving Catch-22

**Mechanic:** Community Weaving (PP-195): Revolution Domain Action. Mandate ≥ 1 required. RS +1 on Success, +2 on Overwhelming. Once per season.

**Test against register:** ARC-S10 (Revolution Eats Itself) captures the Mandate ≥ 1 prerequisite contradiction. But it doesn't connect to the RS crisis: Community Weaving is the ONLY non-practitioner RS recovery tool. If RM cannot access it (no Mandate), the entire RS recovery burden falls on practitioners — who burn out (Decision Point 4). The Revolution's structural contradiction is not just a political problem. It is an existential one for the peninsula.

**Impact on existing arcs:**
- ARC-S10: needs reframing as RS-critical, not just political
- ARC-P02: RS recovery math depends on whether Community Weaving is available
- NPC-ARC-ULN (Maret Uln Succession): if Varfell aligns with RM, does this help RM gain Mandate faster? Maret's TS ~50 means Varfell-RM cooperation adds a practitioner to RS recovery without requiring RM to solve the Mandate problem first.

→ **Affects ARC-S10 (reframe as RS-critical). No separate arc.**

---

## New Emergent Arcs from Threadwork Analysis

### ARC-S31: The Lock Distribution
**Engine:** Vaynard TK 4 → offers originary Locks (Private Collection) → simultaneous Discovery Events
**Emergence:** At TK 4, Vaynard offers the entire Private Collection including originary Locks to practitioners in exchange for Thread education and Southernmost partnership. Each Lock triggers Spirit TN 7 Ob 1 Discovery Event in any TS 10+ character who handles it. If Locks are distributed: Haelgrund (TS 12), Klapp (TS 31), Torsvald (TS 35), and any Player Character with TS 10+ all roll simultaneously. Expected outcomes: ~60% success rate per character (Spirit pool varies). In a single season, 3–5 characters may experience Discovery Events. Consequences cascade: Haelgrund defection (NPC-ARC-HAE), Klapp acceleration (ARC-S21), Torsvald compound exposure (NPC-ARC-TOR), Church triple fracture if Klapp + Haelgrund + Olafsson crises fire simultaneously.
**Non-Player Characters:** Vaynard (TK 4 — distributes Locks), Haelgrund (TS 12 — Discovery Event shatters his worldview), Klapp (TS 31 — Discovery Event on top of existing CE development), Torsvald (TS 35 — Lock exposure compounds her Riskbreaker crisis), Himmensendt (Church loses multiple personnel simultaneously), Edeyja (if Locks reach Askeheim — she recognises their nature immediately)
**Key decision:** Who receives the Locks? Player choice determines which NPC arcs accelerate. Giving a Lock to Haelgrund fires his defection arc. Giving one to Klapp compounds Church fracture. Keeping them from Church figures denies the cascade but limits political leverage.
**Interaction:** ARC-S01 (Vaynard Cascade TK 4), Collision A (Church Double Fracture), NPC-ARC-HAE, ARC-S21, NPC-ARC-TOR

### ARC-S32: The Mending Trap
**Engine:** Mending = sole practitioner RS recovery (RS +1/+2) but costs Coherence −1 per attempt
**Emergence:** RS declines from Lock drift, Gap persistence, winter drift, and failed operations. Net passive decline: −6 to −9/season with 2 Locks and 1 Gap. Each Mending restores RS +1 or +2 but drains Coherence −1. A practitioner can perform ~8–10 Mendings before Coherence 0 (Rendering Crisis → Non-Player Character if unresolved). One practitioner's entire Coherence budget covers ~2–3 seasons of passive RS decline. The campaign cannot be saved by individual heroism — it requires: multiple practitioners Mending in rotation, Warden Cooperation (WC ≥ 2: RS decay halved; WC ≥ 3: RS +2/season), Community Weaving (Mandate ≥ 1 required), AND Lock/Gap resolution (Dissolution/Mending to eliminate persistent decay sources).
**Non-Player Characters:** Edeyja (TS 75–80, Coherence 9 — the most Mending-capable NPC, but each Mending costs her Coherence too; she is not inexhaustible), Maret Uln (TS ~50 — can Mend but at Ob 5–6 for serious Gaps), any practitioner Player Character, Vossen (RM leader — Community Weaving access depends on RM Mandate)
**Structural consequence:** The Mending Trap is the campaign's central mechanical tragedy. The people who can save the world burn out doing it. The Einhir practitioners reached this point 245 years ago. The game replicates their structural position mechanically.
**Interaction:** ARC-P02 (RS Decay — recovery budget), ARC-S16/S17/S18 (Coherence Zero — the burnout destination), ARC-S25 (Warden Cooperation — necessary multiplier), ARC-S10 (Revolution Eats Itself — Community Weaving access), ARC-S15 (Southernmost Spiral — Ceiral Ritual as bulk RS recovery)

### ARC-S33: The Lattice of Enemies
**Engine:** Cross-faction collective operations gated by Belief compatibility
**Emergence:** Endgame RS recovery at RS Critical (19–1) requires "practitioner cooperation across faction lines" (threadwork v25 §5.3). But collective operations require Belief compatibility checks: directly opposing Beliefs → Spirit TN 7 Ob 1 pre-Leap check (failure = helper drops); tangential conflicts → helper dice don't chain on 10. This means the practitioners who must cooperate to save the world may be mechanically unable to cooperate because their factions' Beliefs conflict.
**Key Belief interactions (provisional — depends on specific Belief wordings):**
- Vaynard (consequentialist — "control the Southernmost") vs Edeyja (deontological — "serve the substrate"): tangential conflict → Vaynard's dice don't chain. He is a weaker collective partner than his TS suggests.
- Almud (governance pragmatism) vs Edeyja (substrate duty): tangential → non-chaining.
- Crown practitioner (institutional loyalty) vs Varfell practitioner (revolutionary): directly opposing → Spirit check required. ~40% failure rate per collective operation.
- Maret Uln (RM sympathy) vs any Church-aligned practitioner: directly opposing → Spirit check.
- Multiple Player Character practitioners with harmonised Beliefs: full dice, full chaining. The campaign rewards Player Character-to-Player Character cooperation and penalises Player Character-Non-Player Character cooperation across faction lines.
**Non-Player Characters:** Edeyja (best collective partner — substrate-aligned Beliefs compatible with pure Mending intent), Vaynard (diminished partner despite high TS), Maret Uln (RM sympathy creates friction with non-RM practitioners), Almud (if practitioner — governance Beliefs tangentially conflict with substrate Beliefs)
**Structural consequence:** The endgame is not "can practitioners cooperate?" but "which practitioners can cooperate?" Belief compatibility determines viable practitioner alliances. The register's endgame table should note this constraint.
**Interaction:** All Coherence Zero arcs (S16/S17/S18), ARC-P02 (RS recovery requires collective Mending), Collision B (Practitioner King — Almud's Beliefs affect collective viability)

### ARC-T18: The Overweaving Cascade
**Engine:** Multiple practitioners Weaving same configuration → stacked over-actualisation → catastrophic brittleness
**Emergence:** If two practitioners independently Weave the same configuration in separate contact windows (PP-209): the configuration acquires two stacked over-actualisation modifiers (+2 Ob total). Brittleness compounded: shattering consequence escalates one severity tier (Shifting Object forms as if 1 season old). In politically volatile contexts (sieges, faction collapse), a doubly over-actualised configuration shatters into an accelerated Shifting Object → accelerated Gap formation → RS −4/season from an entity that didn't exist two sessions ago.
**Non-Player Characters:** Any two practitioners operating in the same theatre (most likely: two Player Character practitioners, or Player Character + Maret Uln during Varfell operations, or Player Character + Edeyja during Southernmost work)
**Key decision:** Practitioners must communicate about what they've Woven to avoid stacking over-actualisation. But during contact, they CANNOT communicate (communication requires rendering). Collective Diagnosis before the Leap is the only coordination mechanism. If practitioners Leap separately (non-collective), they cannot know what the other has already Woven.
**Classification:** Tertiary — requires two practitioners independently targeting the same configuration without coordination. But when it fires, RS consequences compound rapidly.
**Interaction:** ARC-S02 (Brittle Peace — over-actualisation at Relational+ scale), ARC-S04 (Rendering Debt — ×3 multiplier in mass battle makes stacked OA even more dangerous)
