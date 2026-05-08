# THREADWORK STRESS TEST — BATCH 3
## Session: d8b924fb834a398c | Date: 2026-04-16 | Effort: MAX
## No repeats from Batches 1 or 2.

---

# 1. HISTORY RESONANCE RISK DIE — CAMPAIGN-SCALE COHERENCE DRAIN

## 1.1 Probabilistic Coherence Cost Across Operations [EMERGENT — SYSTEMIC]

Params_threadwork Coherence table: "History Resonance risk die (shows 1): −1." One die among the History bonus dice is designated as the risk die per operation. P(1 on a d10) = 10%. This fires independently of scale-based Coherence costs — it is additional and not subject to the §3.2 cap.

**At 3 History points (cap 3, typical practitioner): 1 risk die.**
- P(Coherence hit from History Resonance per operation) = 10%.
- Expected additional Coherence loss over 50 operations: 50 × 0.10 = **5 Coherence**.

Combined with scale-based costs (Relational = −1/op; Structural = −2/op): a practitioner performing Relational operations across a 50-op campaign loses E[50 + 5] = 55 Coherence-units against a 10-point track. The History Resonance term adds ~10% to total expected Coherence drain per operation. This is not catastrophic in isolation — but it is an invisible pressure that the practitioner cannot mitigate through good play.

**The risk die is unmitigable.** Unlike Ob (which can be reduced by Overwhelming Leaps, TS advancement, collective operations), the History Resonance risk die cannot be modified. There is no mechanic that reduces the risk die P(1). A master practitioner (TS 100, Spirit 7, everything optimized) has the same 10% risk die exposure per operation as a novice. The only mitigation is performing fewer operations — but that is the same as not playing the Thread system.

**[GAP]** No rule specifies which die among the History dice is the risk die. Is it the first History die rolled? A designated die (different color in TTRPG)? Or does every History die that shows 1 trigger −1 Coherence? If it's every History die showing 1, the math changes dramatically:

- 3 History dice, each P(1) = 10%: P(at least one 1) = 1 − (0.9)³ = 1 − 0.729 = **27.1% per operation**.
- Expected additional Coherence loss over 50 operations: 50 × 0.271 = **13.6 Coherence** — more than the entire Coherence track. At this rate, History Resonance alone causes Rendering Crisis within ~37 operations at Relational scale.

**Required ruling:** Clarify whether "History Resonance risk die" means (a) one designated die per operation regardless of History pool size, or (b) every History die that shows 1. The difference is 10% vs 27% per-op Coherence risk. The answer dramatically changes campaign-scale Coherence depletion rates for History-heavy practitioners.

## 1.2 Practitioner Flashback Anchoring as Additional Coherence Source [EMERGENT+]

Coherence table: "Practitioner Flashback anchoring (Game Master discretion): −1." This fires at GM discretion during any scene where the practitioner's History is activated in a contextually significant way. Combined with History Resonance, a practitioner who relies heavily on History bonuses for Thread operations faces dual Coherence pressure: the risk die (probabilistic) and Flashback Anchoring (GM-discretion). In a campaign with an engaged GM, these combine to accelerate Coherence depletion beyond the scale-based cost alone.

**[GAP]** No guidance exists on how frequently Flashback Anchoring fires. If it's every time the History is used for a Thread op (same frequency as risk die), it would fire ~3× per session for an active practitioner. At −1 each: this adds 3 Coherence/session beyond scale-based costs. Over 10 sessions: −30 additional Coherence — catastrophic. Flashback Anchoring must be genuinely rare (once per session maximum) to be balanced. A cap needs to be stated.

---

# 2. DISSOLUTION RESIDUE POTENCY 5 — VOLATILE DICE EXPLOITATION

## 2.1 Potency 5 Pool Addition on Structural Operations [EXPLOIT — MAJOR]

Dissolution Residue: "Bonus dice equal to Potency rating (1–5). These dice explode on 9–10 (volatile)." Potency 5 adds 5 dice to the pool, each with P(9) = 10% chain or P(10) = 10% +2 — standard chain rule plus extra explosion.

**At Structural-scale Dissolution (Ob 8, TN 8), base pool 22D (TS 90+), adding Potency 5 residue:**
- Total pool: 27D (22 standard + 5 volatile).
- Standard E[net] at TN8 from 22D: 22×0.3 = 6.6.
- Volatile dice at TN8: P(7-9) = 30%, P(10) = 10% (+2 chaining). E per volatile die ≈ 0.3 + 0.1×(additional chain) ≈ 0.35 net.
- E[net from 5 volatile dice] ≈ 5×0.35 = 1.75.
- Total E[net]: 6.6 + 1.75 = **8.35**. At Ob 8: P(≥8) becomes approximately **52%** vs ~35% without residue.

**The residue transforms a coin-flip Structural operation into a majority-success attempt.** More critically: Structural Dissolution on Success = RS −5 (×3 in mass battle = −15). With Potency 5 residue pushing the practitioner above Ob 8 more reliably: Structural Dissolution becomes a tactically viable move instead of a desperate gamble.

**Cost:** Coherence −1 (residue use) + Coherence −3 (Structural FR surcharge, cap exempt) = **Coherence −4 per Structural Dissolution with residue**. From Coherence 10: two such operations = Coherence 2 (Fractured). The residue is a "spend everything" move. But at Potency 5, it may represent accumulated residue from 5 prior Dissolutions — meaning the practitioner has already caused 5 RS drain events to accumulate this resource.

**[EXPLOIT]** Dissolution residue at Potency 5 + Structural target + mass battle context = RS −15 at 52% success rate. This exceeds the PP-201 "three Dissolution attempts = Critical from RS 60" warning. Three Potency-5 residue-enhanced Dissolutions: ~52% each hitting. Expected RS drain: 3 × 0.52 × 15 = **−23.4 RS** — near Rupture from RS 60 in three actions.

**Required ruling:** Cap Potency rating available for single-contact use at 3 (not 5). Potency 4–5 requires two contact windows to expend (the residue is too volatile to discharge all at once). This limits the RS drain from residue-enhanced Dissolution to manageable levels while preserving residue as a meaningful resource.

## 2.2 Residue as Counter-Mending Weapon [EMERGENT+]

A practitioner defending a position can accumulate residue from fighting off attackers (each Dissolution they perform or resist generates residue). They then use Potency-rated residue to enhance Mending operations on their own positions.

Residue adds dice to ANY operation, including Mending. Mending is TN 7 (standard). Potency 5 on Mending: +5 dice at standard TN vs TN 8. E per volatile die at TN7 ≈ 0.4 (not 0.35). E[net from 5 volatile] ≈ 2.0. This makes Mending significantly more reliable. A defender who has accumulated residue through combat can use it to stabilize their settlement's Thread substrate while under siege — residue as defensive RS recovery tool.

This is elegant emergent design. A practitioner who fights defensively generates residue from each Dissolution, then uses that residue to enhance Mending operations. The combat-to-substrate-repair loop is thematically resonant (destruction feeds repair, at cost). Should be surfaced explicitly.

---

# 3. WARDEN COOPERATION (WC) — COMPLETELY UNMODELED IN OPEN ITEMS

## 3.1 WC 2 Halves RS Drain — Scale of Impact [CRITICAL OMISSION]

Warden Cooperation (WC 2): "All RS drain from Gaps and Locks halved." This applies to:
- Gap persistence: −4 RS/season → −2 RS/season per Gap.
- Lock chronic drift: −1/season (seasons 1-3) → −0.5/season; −2/season (season 4+) → −1/season.
- Object-scale Gaps: self-close in 1 season, 0 RS drain — unaffected.

**Impact on 30-year game RS budget:** In an aggressive Thread scenario, peak RS drain sources at Year 20–25:
- Without WC 2: 3 active Gaps + 2 active Locks = (3×4) + (2×1.5 avg) = 15 RS/season.
- With WC 2: same scenario = (3×2) + (2×0.75 avg) = 7.5 RS/season.
- WC 2 halves Gap/Lock RS drain at peak.

**This is a 50% reduction in the dominant RS drain source in the midgame.** The IP recalibration (Batch 1 and 2) calculated RS budgets without WC 2. Every RS endgame calculation in the open items is predicated on WC-0 conditions — the pessimistic baseline. With WC 2 maintained from Year 10 onward: RS budget extends dramatically. The 30-year game RS crisis (Year 20–25) may be avoidable if WC 2 is achieved early.

**[CRITICAL OMISSION]** All RS budget calculations in Batches 1 and 2 must be prefaced with WC state. WC 0 vs WC 2 produces fundamentally different campaign RS trajectories. The open items (IP recalibration, generational shift, settlement siege drain) all need WC as a variable.

## 3.2 WC Advancement Conditions + Thread Interaction [GAP]

WC advances via: "Forgetting Check Success +1; Overwhelming +1 additional." WC decreases via: "TE-13 Military in T15 −1 WR AND −1 WC; RM emergence −2; No expedition 3+ seasons −1."

**Thread interaction:** The WR/WC system is driven by Southernmost expeditions — Forgetting boundary crossings. Forgetting boundary Leap is itself a Thread operation. Success on the Forgetting Check gives WR/WC advancement. This creates a link between: practitioner Thread skill (Focus, Spirit, TPS) → Forgetting Check success rate → WC advancement rate → RS buffer growth.

**Specific calculation:** Forgetting Boundary Leap pool = (Spirit×2)+History+TPS. Spirit 4, History +5D, TPS 5: 18D, TN 7. Forgetting Check Ob is not explicitly stated in the available docs (the infill would specify), but Southernmost is described as high-Ob. Assume Ob 4 (standard difficult). P(≥4) at 18D TN7: ≈ 97%. Overwhelming (net ≥ 8): ~70%. At Overwhelming: WR+2, WC+2 potentially.

**A high-skill practitioner can advance WC rapidly through Forgetting successes.** If WC 2 can be reached within 5–8 seasons of Southernmost expeditions, the RS buffer is established early. The critical path: practitioner advancement (TS, Spirit, Focus) → Southernmost capability → WC 2 → RS stabilization. This is the intended cooperative system but it's never modeled in any open item.

## 3.3 WC 3 — Edeyja Active Mending [EMERGENT+]

WC 3: "Edeyja actively Mending. RS +2/season." Edeyja are canon-defined non-human Thread-sensitive entities (WR ≥ 3 required for deep trust). RS +2/season from WC 3 offsets:
- 2 seasons of Gap persistence (−4 RS/season per Gap) partially.
- Both Lock drift sources (combined −2.5 avg/season).
- Half of annual baseline drift (−1/year = −0.25/season).

**With WC 3 + WC 2 effects combined:** RS drain from Gaps halved AND +2/season restoration. In a campaign with 2 active Gaps and 1 active Lock at Year 25: net RS per season = −(2×2 + 0.75) + 2 = −4.75 + 2 = **−2.75 RS/season**. From RS 45 (likely position at Year 25 without WC), this is 16+ seasons to Rupture. The endgame is survivable with WC 3.

WC 3 is therefore the intended design solution to the RS endgame crisis. The "narrow, difficult path" described in the RS Critical design note is WC 3: trust the Edeyja enough that they actively Mend. This requires WR 3 (deep trust), which requires sustained cooperative Southernmost engagement over the campaign. The system rewards investment in the Warden relationship with RS survival capability.

**This must be made explicit in the endgame design note.** Currently, the RS Critical section doesn't mention WC at all.

---

# 4. DOCUMENT RS RESONANCE + PRIVATE COLLECTION — STRATEGIC RS RESOURCE

## 4.1 PP-258 as an Untapped RS Restoration Source [GAP — STRATEGIC]

PP-258: "A Thread Sensitivity 50+ practitioner reading a pre-Solmund first-person Thread-perception document gains: RS +2 (one-time per document per character). Requires: TS ≥ 50, full scene of contact, primary first-person account (not secondary analysis)."

S-026 Sigurdshelm Keep: "Private Collection housed here." The Private Collection is Vaynard's Einhir archive. If it contains pre-Solmund first-person Thread-perception documents: each such document, read by an eligible practitioner, generates RS +2.

**How many such documents might exist?** No count is specified. If 5 documents exist: 5 practitioners each reading all 5 = 5×5×2 = **RS +50** (one-time, but the total is significant). Even conservatively (3 documents, 2 eligible practitioners): **RS +12**. This is equivalent to 3 successful Mending operations — a meaningful restoration event.

**[GAP]** The Private Collection's contents are undefined. If the design intends the Private Collection to contain multiple PP-258-eligible documents, this is a major RS restoration mechanic hiding in a single sentence of the settlement spec. It needs to be inventoried: how many pre-Solmund first-person Thread-perception accounts does Vaynard possess? Each one is a one-time RS +2 per eligible practitioner.

## 4.2 Sigurdshelm Control as Thread Strategic Asset [EMERGENT+]

S-026 Sigurdshelm Keep: Vaynard's seat. Defense 2. Relatively undefended militarily (Defense 2 vs typical Fortress Defense 3–4). But the Private Collection here is the only known location of pre-Solmund Thread documents.

If an enemy faction captures Sigurdshalm: they control access to PP-258 RS restoration. They can deny eligible practitioners access to the documents (preventing RS +2 per document). They can also control access to the Einhir texts required for the Einhir framework (§4.3 below).

**Sigurdshalm at Defense 2 with Order 3 is the softest strategic Thread target on the map.** A militarily weak settlement that holds the peninsula's Thread archive. This is presumably intentional (Vaynard's scholarly weakness is his exposed position), but the Thread-strategic value of the Private Collection has never been articulated. It needs to be stated explicitly: "The Private Collection at S-026 is a Thread strategic asset. Control of Sigurdshalm grants or denies access to (a) PP-258 RS restoration documents and (b) Einhir framework technique sources."

---

# 5. EINHIR FRAMEWORK ACCESS — SIGURDSHALM AS CHOKEPOINT

## 5.1 Einhir Framework Prerequisites + Document Control [EXPLOIT — POLITICAL]

Einhir framework requirement 2: "The practitioner possesses at least one Einhir Text technique applicable to Mending or the relevant Restricted Operation."

Einhir Texts are physical documents. Their location: presumably the Private Collection at S-026, or equivalents. No other Einhir Text repository is named in the available documents.

**If Sigurdshalm is the only Einhir Text repository:** Control of Sigurdshalm = gate access to the Einhir framework. Without Einhir Text access:
- Locked Zone border Mending (Ob 8+) is unavailable.
- Permanent Lock dissolution is unavailable.
- T15 Askeheim cannot be addressed beyond piecemeal lower-scale Mending.

**A faction that conquers Sigurdshalm can hold the entire Einhir framework hostage.** They can negotiate Einhir Text access as a diplomatic leverage tool. They can deny access to all factions, accelerating Rupture to force a diplomatic resolution on their terms. They can reserve Einhir framework use exclusively for their own practitioners.

**This transforms Sigurdshalm from "Varfell's scholarly capital" into "the most strategically important settlement on the peninsula for Thread endgame purposes."** Its Defense 2 is a catastrophic under-protection of this asset.

**[EMERGENT+]** This is probably intended design (Vaynard's vulnerability is the mirror of the knowledge he holds) but the Thread-strategic implication has never been stated. Requires a design note: "Einhir Text access is required for the Einhir framework. If Sigurdshalm's Private Collection is the primary Einhir Text repository, its military vulnerability makes it the peninsula's most strategically underdefended Thread resource."

## 5.2 Einhir Framework Knowledge Requirement + Southernmost Siege [CONFLICT]

Einhir framework requirement 1: "Knowledge: The practitioner has Diagnosed the Locked Zone's structure via Southernmost expedition or equivalent scholarly research."

WC decrease condition: "TE-13 Military in T15 −1 WR AND −1 WC." Military action at T15 Askeheim resets Warden trust AND decrements Warden Cooperation. This means: any faction that sieges Askeheim (to control S-033) also loses WC progress — potentially destroying the WC 2/3 buffer they've built.

**The only military path to Askeheim (via T15 siege) destroys the Warden relationship needed for the Einhir framework.** Gaining physical control of T15 is mechanically antithetical to gaining Thread access to its secrets. This is either an elegant design constraint (you can't conquer your way to Thread knowledge) or an unintended conflict (military victory at Askeheim should have a different consequence than WC collapse).

**[EMERGENT+ — design depth]** This is likely intentional. The Einhir framework is not accessible by force. Military presence at T15 = WC loss = Einhir framework harder to reach. The only path to Einhir knowledge is cooperative, not coercive. Worth stating explicitly as a design note.

---

# 6. TS GROWTH RATE VS COHERENCE DEPLETION RATE

## 6.1 Can Thread Sensitivity Growth Outpace Coherence Depletion? [EMERGENT — DESIGN VALIDATION]

TS grows from: "Overwhelming on Leap: +1 TS. Overwhelming on Lock: +1 TS." TPS = TS ÷ 10 (round down). Each 10 TS growth = +1D to all Thread pools.

**Overwhelming rate on Leap:** At 18D TN7, Ob 1 (TS 50+): P(Overwhelming) = P(net ≥ 3 AND net ≥ 2) = P(net ≥ 3) ≈ 87%. Each Leap at TS 50+ is almost guaranteed to be Overwhelming. So: TS grows at roughly +1 per Leap (10% chance of the +1 TS trigger being the result of Overwhelming... wait. Overwhelming on Leap gives +1 TS as an explicit bonus, not a probabilistic one — it IS the Overwhelming outcome.

So: every Overwhelming Leap = +1 TS. At 87% Overwhelming rate: ~87% of Leaps produce +1 TS. Performing 10 Leaps (10 separate scenes/sessions): expected TS gain = 8.7 TS. TPS increases at TS 60 → 70 (+1D) after ~11.5 Overwhelming Leaps.

**Coherence depletion over 10 Leaps (with operations at Relational scale):** 10 Leaps → 10 Contact windows. Each Contact window: ~2 operations at Relational scale = Coherence −2 per window (not counting History Resonance). 10 windows = Coherence −20... but Coherence only runs from 10 to 0. So after 5 Contact windows (at Relational, 2 ops each), Coherence is depleted. Recovery: 1 non-practice season = +1 Coherence.

**TS growth does NOT outpace Coherence depletion.** TS grows at ~1 per Overwhelming Leap. Coherence depletes at −1 per Relational operation. A practitioner performing 2 operations per contact window and 2 contact windows per session depletes Coherence at 4/session. TS grows at ~2/session (2 Leaps, both likely Overwhelming). After 2.5 sessions: Coherence 0. TS has grown +5 (from 50 to 55, still TPS 5).

**Conclusion:** TS growth and Coherence depletion are on completely different scales. A practitioner can grow TS aggressively while simultaneously depleting Coherence. TS 100 is achievable theoretically, but the practitioner would experience multiple Rendering Crises along the way. Each crisis recovery costs −1 TS permanent. So maximum sustainable TS is bounded by how many Rendering Crises the practitioner can survive at −1 TS each.

**[EMERGENT+ — design depth]** Thread Sensitivity growth and Coherence depletion create a natural practitioner arc: rapid TS advancement (from Overwhelming Leaps) concurrent with Coherence burnout, recovery, and the permanent TS cost of each crisis. A practitioner who practices intensively grows fast and crashes often. The maximum sustainable TS depends on how carefully they manage Coherence recovery seasons. This arc should be explicit in the practitioner advancement documentation.

---

# 7. ENEMY PRACTITIONER DISSOLUTION FAILURE — SHARED RS CATASTROPHE

## 7.1 The Shared Track as Mutual Deterrent [EMERGENT+ — game theory]

RS is a shared track — it doesn't belong to any faction. An enemy practitioner's failed Dissolution drains the same RS pool that the players are trying to preserve.

**Specific scenario:** RS 35 (Fractured band). Enemy practitioner (TS 70, pool ~17D) attempts Structural Dissolution of a player-controlled fortification in mass battle. Ob 8+ TN 8: P(≥8) ≈ 22%. Failure: RS −8 ×3 (mass battle) = **RS −24**. At RS 35: RS drops to 11 → Critical band.

**The enemy's failed Dissolution benefits the player (tactically) by destroying the enemy practitioner (Incapacitated) and failing the operation — but it destroys both factions' RS buffer.** The shared track means every enemy Thread catastrophe is also a world-level catastrophe. A militarily winning faction that uses Thread aggressively to secure victory may Rupture the world in the process. This is mechanically accurate: "military victory via Thread = Rupture" is the Einhir Catastrophe replayed.

**[EMERGENT+]** This creates a genuine mutual deterrent: no faction can use destructive Thread operations recklessly without risking Rupture. The shared RS track is the gameworld's most elegant arms control mechanism. Factions with Thread practitioners are incentivized to negotiate rather than Dissolve — because Dissolution failure doesn't just hurt them, it ends the campaign for everyone. This insight should be articulated in the faction design documentation as a design note on Thread warfare.

## 7.2 Provocable Dissolution — Forcing Enemy Thread Failure [EXPLOIT — DARK]

A player faction could deliberately present targets that incentivize enemy Thread practitioners to attempt high-Ob Dissolution operations they're likely to fail, at moments when RS is near-critical — forcing the enemy to Rupture the world on their behalf.

Scenario: RS 26 (near-Fractured/Critical boundary). Player faction deploys an important fortification as "bait." Enemy Thread practitioner (TS 70) attempts Structural Dissolution: P(success) ≈ 22%. P(failure) ≈ 78%. On failure: RS −24 → RS 2 → Critical band. Spontaneous Gaps, global +1 Ob, faction Stability checks — the game destabilizes catastrophically.

**The player faction hasn't technically caused the RS collapse. The enemy did.** But the player engineered the conditions. This is within the realm of intentional play — Thread warfare as deterrence, brinksmanship, and provocation.

**[OK — but needs surfacing]** This is intended design (Thread war is mutual destruction) but players should understand the game-theoretic implications of provoking enemy Thread operations at near-critical RS. No design note currently articulates this dynamic.

---

# 8. BINDING OPS SCOPE GATE + COMPANION MASS COMBAT AI

## 8.1 PP-261: TS 70 Companion Should Not Attempt Binding Ops in Mass Battle [GAP]

PP-261: "Binding Ops at Relational scale in mass battle require Thread Sensitivity 90+ for >50% success. TS 70 practitioners: do not attempt Binding Ops in mass battle. RS cost without viable success probability."

A companion with TS 70 may attempt a Relational Lock in mass battle (ED-COMP-02/03 context). At TS 70, pool ~17D TN8, Ob ≥ 5 (Relational + breadth): P(≥5) ≈ 56% in isolation — but the mass battle ×3 RS multiplier makes the expected RS cost of Partial/Failure catastrophic regardless.

**The companion AI (videogame mode) must include PP-261 as a hard constraint:** Companions with TS < 90 should never declare Binding Ops in mass battle. This is not a tactical preference — it is a design-level prohibition based on expected RS cost. A companion AI that doesn't implement PP-261 will systematically cause RS drain through well-intentioned but probabilistically disastrous Binding Op declarations.

**[GAP — TTRPG vs Videogame split]** In TTRPG, the GM runs the companion and knows PP-261. In the videogame, the companion AI must encode PP-261 as a TS-gated behavior rule. ED-COMP-02 resolution must include: "Companion AI should not declare Binding Operations in mass combat contexts unless companion TS ≥ 90."

---

# 9. GENERAL DUEL + LEAP CONFLICT — PHASE 5 COLLISION

## 9.1 Simultaneous Phase 5 Actions in Mass Battle [GAP]

Mass battle Phase 5: "Personal Action available at Phase 5 (Priority 8). Limit: 1 exchange per battle turn. General's Command Rating suspended while in personal combat."

Leap (Thread op): "Priority 5 full-round action. Only reactive defence available during Leap round."

Both actions are Phase 5 (personal scale during mass battle). The Leap is Priority 5 within Phase 5. A General Duel exchange is Priority 8 within Phase 5.

**A practitioner-general can Leap (Priority 5) and then, within the same Phase 5 action, initiate a General Duel (Priority 8)?** The Leap is a full-round action — Priority 5 means the practitioner leaps before opponents at Priority 6-8. After the Leap, they are in Thread contact (not performing the exchange yet, just suspending rendering). The General Duel exchange happens at Priority 8. But during Thread contact, the practitioner can only take reactive defence — no offensive personal actions.

**Ruling check:** During Thread contact (post-Leap success, round 2+), the practitioner is suspended from rendering. Can they simultaneously engage in a General Duel? Answer: No. The Leap's consequence is that "only reactive defence is available during the Leap round" and during contact, Thread operations are their active action. A General Duel requires offensive action (initiative roll, attack exchange). A practitioner in Thread contact cannot initiate a General Duel in the same Phase 5 action.

**[GAP]** This is not explicitly stated but follows from the rules' logic. Required explicit ruling: "A practitioner in Thread contact cannot initiate or continue a General Duel. Thread contact must be dropped first (rendering reasserts, contact ends). Alternatively: the practitioner may decline Thread contact this battle turn and engage in a General Duel instead." This prevents the potentially powerful combo of Thread operations + personal combat simultaneously in mass battle.

---

# 10. FORGETTING COMPANION-CARRYING — COHERENCE CRISIS MID-CROSSING

## 10.1 −2 Coherence/Round Per Companion During Forgetting Crossing [EXPLOIT — STRUCTURAL]

PP-279 companion-carrying rule: "Each companion: −2 Coherence/round (cumulative). Maximum companions = practitioner's Focus − 1."

Focus 5 practitioner: maximum 4 companions carried. Each carried companion: −2 Coherence/round. With 4 companions: −8 Coherence/round total. At Coherence 10 start: after 1 round, Coherence 2 (Fractured). After 2 rounds: Coherence −6 (would be Coherence 0 — Rendering Crisis — in round 2). The practitioner reaches Rendering Crisis in round 2 of a 4-companion Forgetting crossing.

**At Fragmented (Coherence 4–3):** The threshold is hit after 1 round with 4 companions (Coherence 10 − 8 = 2). But: Fragmented fires +1 Ob to all Thread ops including the Leap. The Forgetting Leap is still in progress — the crossing hasn't completed. If the Forgetting crossing requires maintaining the Leap for multiple rounds (Focus contact duration governs): with Fragmented at round 1, the Leap continuation gets +1 Ob on any subsequent Thread operations in the contact window.

More critically: Fragmented produces "Roll Fragmented Fallout on entering this band." This fires mid-Southernmost crossing. The practitioner is simultaneously experiencing ontological instability (Fragmented effects) while trying to hold 4 companions through the Forgetting boundary. One fallout result: "A Knot's emotional valence briefly reverses." If the practitioner is Knotted to one of the companions they're carrying: that Knot's emotional valence reverses mid-crossing. The companion is experiencing the practitioner's relational signal as its inverse during the moment of maximum vulnerability.

**[EXPLOIT — STRUCTURAL]** Carrying 4 companions through a Forgetting crossing guarantees Rendering Crisis within 2 rounds. Focus 5 contact duration = 5 rounds. A 5-round Forgetting crossing with 4 companions = Rendering Crisis at round 2, then likely NPC conversion or permanent withdrawal from Thread practice. The maximum-companions scenario is mechanically suicidal.

**Required design note:** "Companion-carrying during Forgetting crossing is a high-cost sacrificial mechanic. Carrying 2+ companions at Focus 5 produces Rendering Crisis risk within the crossing window. This is intentional — the practitioner's willingness to risk their rendering for companions is the dramatic engine of the mechanic. Players should understand this before attempting it."

---

# 11. POP PARADOX WINDOW AS COUNTER-POP DEFENSE

## 11.1 The First POP Protects Itself [EMERGENT+ — TACTICAL]

PP-203: "If a practitioner attempts a Past-Oriented Pull targeting a thread that is currently in a paradox window (P-22 delayed manifestation active on that thread), the attempt automatically fails. No roll, no RS cost. The paradox window is unaffected."

Applied: Practitioner A POPs an obligation (Batch 2 §7.1). The POP succeeds. A paradox window opens on the obligation's Thread configuration. The window lasts 1d3 scenes. During this window: any practitioner attempting to counter-POP the same obligation-moment **automatically fails** (PP-203).

**The first POP creates a brief immunity window.** The practitioner who POPs first has a 1d3-scene window during which the temporal displacement is protected from counter-POP. After the window closes (physical facts update; thread snaps to displaced state), the temporal change is permanent — and a subsequent POP to "undo" the displacement would be a POP targeting the NEW past (the displaced state), not a counter of the original.

**[EMERGENT+]** This creates interesting first-mover advantage dynamics in Thread-political warfare. The faction that POPs first gets temporal immunity for 1d3 scenes. To counter: the opposing faction must wait until the paradox window closes, then POP the displaced state (which may have different actualization and different Ob). The temporal arms race favors the faction that acts first and acts decisively.

**Required tactical surfacing:** "A successful POP creates a paradox window on the targeted configuration. During this window (1d3 scenes), opposing practitioners cannot counter-POP the same target. After window closure, the displaced state is the new baseline — subsequent POPs must target the displaced state at appropriate recency Ob."

---

# 12. CHURCH CATHEDRAL THREAD FOOTPRINT SOVEREIGNTY

## 12.1 Church Practitioners in Crown Province — RS Attribution [GAP]

Settlement spec §3.3: Church governs S-003 Valorsplatz Cathedral (T1 Valorsplatz, Crown province) as a subnational faction. Church management includes Piety Influence generation.

If Church-affiliated practitioners operate at S-003 (Thread ops, Mending, or investigation), their Thread operations drain T1 Valorsplatz's province RS. But T1 is Crown province — Crown has Provincial Authority. 

**Question:** Does RS track at province level or global level? Answer (from params_threadwork): RS is a single global track (100→0). Thread ops anywhere on the peninsula drain the same RS pool. Province-level RS distinction doesn't exist — there's only one RS track.

**The sovereignty question becomes:** Who has authority to authorize Thread operations in T1 Valorsplatz? Crown (Provincial Authority) or Church (Cathedral management rights)? If a Church Inquisitor with TS 30+ performs a Thread operation at S-003 in Crown territory: the Crown cannot prevent this without revoking Church management (Domain Action: Influence, Ob = Church Influence ÷ 2 rounded up — probably Ob 4–5). The Church's management rights give them implicit Thread operational authority within their managed settlements.

**[GAP]** No rule addresses whether Provincial Authority extends to authorizing Thread operations within subnational-managed settlements. Proposed ruling: Thread operations in a settlement are governed by whoever manages that settlement, not the Provincial Authority. Church management of S-003 means Church practitioners have Thread operational rights there. The Province faction cannot prevent these operations without revoking management. This has downstream sovereignty implications: the Church has Thread-operational footholds in every province where they manage a Cathedral, regardless of provincial faction alignment.

## 12.2 Church Inquisitor TS + CI Investigation Loop [EXPLOIT — CASCADING]

S-003 Valorsplatz Cathedral: Church management (Order 4). A Church Inquisitor with TS 30+ stationed here can detect Thread operations anywhere in T1 Valorsplatz within perceptual range (TS 30–49: "senses an operation in the scene; general direction identifiable").

If Almud undergoes First Leap at S-001 (Batch 1 finding): the Inquisitor at S-003 may be within perceptual range (~50m from S-001 if the cathedral is near the palace district). They perceive the operation. They initiate formal Investigation (one Domain Action, Ob 2). Success: CI +1 at next Accounting.

**This creates a Church-Church feedback loop in the capital:** Church management rights at S-003 give them a Thread-detection asset in the Crown's political center. Any Thread operations by Crown-affiliated practitioners (including Almud's First Leap, any Warden Thread-Read of the capital) are potentially detectable by the S-003 Inquisitor. CI rises automatically from capital Thread activity — without any active Church policy decision. The Inquisitor is there, they have the TS, they detect; the Investigation is nearly automatic for a competent Church agent.

**[EXPLOIT — CASCADING]** CI ratchets upward from Crown Thread activity that the Church detects through its Cathedral management foothold. The player faction cannot prevent CI growth without either: (a) keeping all Thread operations in the capital away from the Cathedral's perceptual range, or (b) revoking Church management of S-003 (political cost: Order −1 at S-003, Disposition −2 with Church). This is a genuine political-Thread tension that should be explicit.

---

# 13. FACTION STABILITY TRIGGERS + THREAD OPERATIONS

## 13.1 Dissolution of Faction Institution — Does It Fire Stability Trigger? [GAP]

Faction layer §1.2 defines 5 canonical Stability triggers: Territorial Occupation/Loss, Unfavourable Treaty, Military Defeat, Officer Loss (ED-334/335), Suppress Action Failure.

A Thread practitioner Dissolves the Church's institutional grip on T9 (Structural-scale Dissolution of the Church's hierarchical configuration). RS −5, Structural Gap forms. The Church doesn't lose territorial control — the territory is still theirs. But their institutional structure is fractured.

**Does a Structural-scale Dissolution targeting a faction's institutional configuration trigger a Stability loss?** Under the 5-trigger list: none of the triggers explicitly covers "Thread-caused institutional disruption." Territorial Occupation requires military action. Dissolution is not military action.

**[GAP]** Thread operations at Structural scale targeting faction institutions are not among the canonical Stability triggers. A successful Structural Dissolution of a faction's core configuration produces: RS −5, Structural Gap, potentially NPC leader Dissonance checks — but no Stability trigger. This seems wrong. A Structural-scale Dissolution of the Church's institutional Thread should cause institutional shock at least equivalent to "Military Defeat" (which presumably causes Stability −1 or −2).

**Required addition to faction layer:** "Successful Structural-scale or higher Thread Dissolution targeting a faction's core institutional configuration: Stability −2 (equivalent to Major Military Defeat). Successful Structural Lock targeting a faction's core configuration: Stability −1/season (chronic, as the institution cannot adapt). Failed Structural Dissolution (Monstrous Incursion, Practitioner Incapacitated): no Stability change to factions — the catastrophe is indiscriminate."

---

# 14. AUDIENCE RESISTANCE DECAY IN FRACTURED RS — CHAIN CONTEST CONVERGENCE

## 14.1 Stability Decay → Audience Resistance Drop → Faster Contest Convergence [EMERGENT+]

Social contest §2 Step 4: "Audience resistance = average Stability of represented factions, round up, then −1 (minimum 0)."

Faction layer §1: Stability decreases from canonical triggers. In a late-game (Year 20–25) Fractured RS campaign, faction Stability is under sustained pressure:
- Lock chronic drift causes RS − which triggers Stability checks at RS ≤ 19 (Critical: "Seasonal Stability checks Ob 1; failure = Mandate −1").
- Military campaigns cause Stability losses.
- Occupation costs Stability.

If average faction Stability at Year 20 is 2 (plausible given sustained military activity): audience resistance = ceil(2) − 1 = **1**. At Year 25 with Stability averaging 1.5: resistance = ceil(1.5) − 1 = **1** still. At Stability averaging 1: resistance = ceil(1) − 1 = **0**.

**At audience resistance 0:** The Piety Track moves by full net successes per exchange, unreduced. A successful argument exchange (net 3 successes) moves the Piety Track 3 points. At starting position 5: three exchanges at net 3 = Piety Track 14 → Side A wins. Contests resolve in far fewer exchanges than designed.

**Chain contest convergence at late-game Stability 1 (resistance 0): Grand Contests (5 exchanges) resolve in 1–2 exchanges** for a competent orator. The contest system converges too fast in late-game conditions. This is neither intended nor good — political decisions at the endgame should be hard-fought, not trivially swift.

**[EMERGENT — DESIGN PROBLEM]** Audience resistance floor is 0. Late-game Stability decay makes resistance 0 likely. At resistance 0, social contests become trivial for orators with high Argue pools. The chain contest convergence simulation needs to account for this decay: what happens to political contest dynamics when factional institutions are degraded? Required: either a floor on audience resistance (minimum 1 regardless of faction Stability) or an explicit design note that late-game contest convergence is intentionally faster as institutions weaken.

---

# 15. DISSONANCE FACTOR 3 — POP ON SETTLEMENT NPC MEMORIES

## 15.1 POP Targeting Historical Events Witnessed by Settlement Residents [GAP]

Dissonance Factor table: "POP affecting character's own memories: 3." Spirit check TN7 Ob 3. Failure: Spirit −1D for rest of scene or season.

A practitioner POPs a historically significant event witnessed by many settlement residents (e.g., the founding of an institution, a public oath-taking, a major battle). The POP displaces the event. All residents who remember the event are now experiencing Temporal Disjunction — their memories are intact but physical facts have changed.

**Do these residents make Dissonance checks?** The Dissonance Factor 3 rule applies when "POP affects character's own memories." In Temporal Disjunction, the residents' memories persist but contradict current physical reality — their memories ARE effectively "affected" by the POP (the memories no longer correspond to facts). At Spirit 2–3 (typical settlement resident), Ob 3 Dissonance check: P(≥3) on 4D TN7 ≈ 25%. P(failure) ≈ 75%. 

**A POP targeting a publicly-witnessed event produces mass Dissonance failures in the settlement.** ~75% of affected residents suffer Spirit −1D for rest of scene (or season if the Dissonance is sustained). A settlement with 500 residents, 400 of whom witnessed the historical event: ~300 residents suffering Spirit −1D. This manifests as: mass disorientation, social contest degradation (Spirit is not the primary Argue attribute, but it governs Thread op pools for any resident practitioners), and Order instability.

**[GAP]** No rule addresses population-scale Dissonance from POP. At what breadth does a POP's Temporal Disjunction trigger resident Dissonance checks? Proposed: "A POP that displaces an event witnessed by a formation-scale or larger group (10+ people) triggers Dissonance Factor 3 checks for all witnesses with memories of the displaced event. These checks fire at the end of the scene in which the displacement manifests physically." This creates a mechanical cost for historically-significant POPs that scales with the event's witness count.

---

# 16. SPIRIT AS HIGHEST ATTRIBUTE + GENERATIONAL SHIFT PENALTY ON PC PRACTITIONER

## 16.1 Spirit −2 at Year 20 → Thread Pool Collapse [EMERGENT — SEVERE]

Generational Shift Threshold 4 (Year 20): −2 to highest attribute. ED-SETT-07 (proposed ruling: applies to PCs). If the PC practitioner's highest attribute is Spirit:

Spirit starts at 5 (creation max for a Thread-focused character): Spirit − 2 at Year 20 = Spirit 3.
Thread pool: (Spirit×2)+History+TPS. At Spirit 5: 13D + History + TPS. At Spirit 3: **9D** + History + TPS.

**Thread pool drops from ~21D (Spirit 5, History +5D, TPS 5) to ~17D at Year 20.** That's −4D across all Thread operations. At Ob 8 (Structural operations), this is significant: P(≥8) at 21D TN7 ≈ 62%. P(≥8) at 17D TN7 ≈ 48%. From majority-success to coin-flip.

At Year 30 (Threshold 6, −3 to highest attribute): Spirit 5 → Spirit 2. Thread pool: (2×2)+History+TPS = 4D+History+TPS. At 4D base: pool ≈ 12D. P(≥8 at TN7 on 12D) ≈ 22%. Structural operations become nearly impossible.

**By Year 30, a Spirit-focused practitioner who has survived has roughly the Thread capability of a Year-1 Spirit 3 practitioner.** The age penalty collapses Thread competency to novice level at the campaign's endgame. This interacts catastrophically with the RS Critical worldwide +1 Ob — the practitioner most needed for endgame Mending is the one most degraded by age.

**[EMERGENT — SEVERE]** The Generational Shift + Thread interaction is potentially campaign-breaking for Spirit-primary practitioners in 30-year games. Either: (a) the TS ≥ 50 exemption threshold is too high (should be TS ≥ 30 to include all practicing practitioners), or (b) the Generational Shift attribute penalty should cap at −1 for the Thread-primary attribute (Spirit) for active practitioners — the attribute governing Thread contact is sustained by practice, not merely biological capacity. Required design decision before Generational Shift clock is finalized.

---

# SUMMARY TABLE — BATCH 3

| Item | Finding | Severity | Action Required |
|------|---------|----------|----------------|
| History Resonance | "Risk die" undefined: one die or every History die? 10% vs 27% per-op Coherence risk | **[GAP — CRITICAL]** | Clarify: one designated risk die per op (10% additional Coherence) vs all History dice (27%+) |
| History Resonance | Flashback Anchoring fire frequency undefined; if every op, catastrophic | **[GAP]** | Cap: maximum 1 Flashback Anchoring per session |
| Dissolution Residue | Potency 5 + Structural + mass battle = RS −15 at 52% success; 3 ops ≈ Rupture | **[EXPLOIT — MAJOR]** | Cap single-use Potency at 3; Potency 4–5 requires two contact windows |
| Dissolution Residue | Residue-enhanced Mending as defensive RS recovery loop | **[EMERGENT+]** | Surface as design note |
| WC system | WC 2 halves Gap/Lock RS drain — all RS budget calculations in Batches 1–2 are WC-0 | **[CRITICAL OMISSION]** | All RS endgame calculations must include WC state as variable |
| WC system | WC 3 + Edeyja Mending (+2 RS/season) is the intended endgame RS solution | **[EMERGENT+]** | Add WC to RS Critical design note as the "narrow difficult path" |
| Private Collection | PP-258 document RS resonance (+2 per document per eligible practitioner) — untapped | **[GAP — STRATEGIC]** | Inventory Private Collection Einhir documents; count RS restoration capacity |
| Sigurdshalm | Defense 2 settlement controls all Einhir framework access — most vulnerable critical asset | **[EMERGENT+]** | State Thread-strategic value of Sigurdshalm explicitly |
| Einhir framework | Military action at T15 collapses WC (required for Einhir framework) — cannot conquer Einhir knowledge | **[EMERGENT+ — design depth]** | State explicitly: Einhir framework is inaccessible by force |
| TS growth | Overwhelming Leap ≈ +1 TS nearly every Leap at TS 50+; Coherence depletes far faster than TS grows | **[EMERGENT+ — design validation]** | Surface practitioner arc: rapid TS growth concurrent with Coherence burnout cycles |
| Enemy Dissolution | Shared RS track: enemy Dissolution Failure catastrophe affects all factions equally | **[EMERGENT+ — game theory]** | State mutual deterrence explicitly in faction design |
| Enemy Dissolution | Provoking enemy practitioners to attempt high-Ob Dissolutions near-critical RS is viable strategy | **[OK — surface]** | Note: Thread brinksmanship is intended strategic option |
| PP-261 + companion AI | TS 70 companion should not declare Binding Ops in mass battle; AI must encode this | **[GAP]** | Add PP-261 as hard constraint in companion AI spec (ED-COMP-02) |
| General Duel + Leap | Both Phase 5 actions; practitioner in Thread contact cannot initiate General Duel | **[GAP]** | Explicit ruling: Thread contact and General Duel are mutually exclusive per Phase 5 |
| Forgetting carrying | 4 companions = −8 Coherence/round; Rendering Crisis guaranteed in round 2 | **[EXPLOIT — STRUCTURAL]** | Add design note: companion-carrying is mechanically suicidal beyond 1–2 companions; intended sacrificial mechanic |
| POP paradox window | First POP creates 1d3-scene immunity to counter-POP on same target | **[EMERGENT+ — tactical]** | State explicitly as first-mover advantage in temporal Thread warfare |
| Church sovereignty | Cathedral management rights give Church Thread-operational footholds in every province | **[GAP]** | Ruling: Thread ops in settlement governed by settlement manager, not Provincial Authority |
| Church surveillance | Inquisitor at S-003 detects Almud's First Leap; CI ratchets from capital Thread activity | **[EXPLOIT — CASCADING]** | Surface: Church Cathedral management = automatic Thread detection asset in any province |
| Faction Stability | Structural Dissolution of faction institution not among 5 canonical Stability triggers | **[GAP]** | Add: Structural+ Thread Dissolution of faction core config = Stability −2 |
| Contest convergence | Fractured RS → Stability decay → audience resistance 0 → Grand Contests resolve in 1–2 exchanges | **[EMERGENT — DESIGN PROBLEM]** | Rule: audience resistance floor = 1 minimum, or explicit note that late-game contest convergence is intentionally faster |
| POP + settlement NPC | POP on publicly-witnessed event triggers mass Dissonance Factor 3 checks; ~75% failure rate | **[GAP]** | Add rule: formation-scale+ POP triggers Dissonance checks for all witnesses at scene end |
| Generational Shift | Spirit −2 at Year 20 collapses Thread pool by 4D; Spirit −3 at Year 30 → novice-tier capability | **[EMERGENT — SEVERE]** | Decision: lower TS ≥ 50 exemption to TS ≥ 30, OR cap Generational Shift at −1 for Spirit |

---

## ADDITIONAL CRITICAL ITEMS FROM BATCH 3

6. **History Resonance risk die scope** — if "every History die showing 1" rather than "one designated die," the Coherence depletion math for the entire campaign is approximately 3× worse than current calculations assume. This is foundational.

7. **Dissolution Residue Potency cap** — Potency 5 at Structural scale in mass battle approaches Rupture probability. Needs a cap before any Dissolution Residue design is finalized.

8. **WC as RS variable** — must be incorporated into all IP/RS calculations. WC 0 vs WC 2 changes the 30-year game RS trajectory enough to affect whether the endgame crisis is survivable.

9. **Generational Shift + Spirit** — a Spirit-primary practitioner PC at Year 30 with −3 Spirit is Thread-incapable at exactly the moment most needed. Must decide: lower exemption threshold or protect Thread-primary attribute.

10. **Faction Stability + Structural Thread** — no canonical Stability trigger covers Thread-caused institutional disruption. The 5-trigger system is incomplete with respect to the Thread layer.

---

*End of document. Session d8b924fb834a398c.*
