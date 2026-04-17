# THREADWORK STRESS TEST — BATCH 5
## Session: d8b924fb834a398c | Date: 2026-04-16 | Effort: MAX
## No repeats from Batches 1–4.

---

# 1. PP-603 SEASONAL RS CAP — STRUCK VS STILL PRESENT IN SKELETON

## 1.1 Canon Conflict: Cap Struck but Referenced in Three Locations [CONFLICT — CRITICAL]

params_threadwork canonical state: "RS Track (PP-603 — canonical): Seasonal cap: STRUCK (PP-603). Reality takes full consequence."

But three locations still reference ±10:
- threadwork_v30.md §5.5 (Hybrid): "seasonal cap on RS change is ±10 net"
- threadwork_v30.md §5.5: "the cap applies to the net RS change after all sources"
- params_threadwork (superseded section): "Seasonal cap: ±10 net RS change per season (applies at Accounting)"

**Canonical ruling is clear: PP-603 struck the cap.** RS changes apply in full at Accounting — no ceiling, no floor, no smoothing. But the skeleton and hybrid rules still contain the struck text. Any GM reading the threadwork_v30 skeleton (the document they'll actually consult during play) will find the cap still present and apply it.

**Impact on all four prior batches:** Every RS budget calculation assumed uncapped RS — but they were written knowing the cap was struck. What they didn't calculate is what no-cap means for the upside: in a campaign season where three Mendings Overwhelming succeed in mass battle (RS +6 each, ×3 multiplier per PP-225 = +18 each, three total = **+54 RS in one Accounting**). With no cap, a good Mending season can fully restore RS from Critical to Fragile in a single Accounting. This swings the endgame recovery possibility from "narrow and difficult" to "potentially rapid if mass battle Mending concentrates."

**Required:** Purge ±10 cap language from threadwork_v30 skeleton and Hybrid section. Add explicit note at each struck location: "RS cap struck per PP-603. All RS changes apply at full value at Accounting with no seasonal ceiling."

## 1.2 No-Cap RS + Mass Battle PP-225 = RS Restoration Swing [EMERGENT+]

PP-225 (provisional): RS ×3 multiplier applies to gains. Mending Overwhelming in mass battle: normally RS +2 → with ×3 = **RS +6 per operation**. Without a cap, five successful Mending Overwelming results in one mass battle season: RS +30. From RS 20 (Critical band): RS 50 → Fragile. The world recovers from near-Rupture in a single good battle.

This is symmetrical with the catastrophic downside (Dissolution Failure × 3 = RS −24). The no-cap world is high-variance: a single season of concentrated Thread effort in either direction produces dramatic RS swings. This is apparently intentional ("Reality takes full consequence") but creates a very different campaign feel than the smooth-decay model the skeleton language implies.

**[EMERGENT+]** The no-cap RS is the hidden design — high volatility, high stakes, both directions. Needs to be stated explicitly in the RS design notes: "RS is a high-variance track without seasonal smoothing. A concentrated Mending effort in a single mass battle can restore 20–30 RS; a single Dissolution failure can drop RS 24. This is intended. Players and GMs should plan for RS volatility, not gradual decline."

---

# 2. TS 90+ AT COHERENCE 0 — REALITY STRAIN AS CONTINUOUS RS DRAIN

## 2.1 A Resonant Practitioner at Coherence 0 Drains RS Per Scene [EXPLOIT — CATASTROPHIC]

PP-197: "A practitioner who reaches Coherence 0 with Thread Sensitivity 90+ undergoes Structural-scale self-maintenance threadwork at every moment... RS cost: −1 RS per scene in which the practitioner is actively maintaining their existence (any scene in which they are conscious and present)."

**Calibration against campaign pacing:** 3 scenes/session × 10 sessions/year (conservative) = 30 scenes/year. At −1 RS/scene: **−30 RS/year** from one TS 90+ practitioner at Coherence 0. From RS 60 start: 2 years to Rupture from this source alone.

This is the fastest single-entity RS drain in the entire system. It exceeds: Gap persistence (−4/season, −16/year for one Gap), Lock drift (−2/season max, −8/year), siege (−1/season, −4/year), winter (−1/year). A single unresolved Resonant practitioner at Coherence 0 outpaces ALL other combined RS drain sources.

**The only counter:** Rendering Crisis resolution arc. Minimum conditions: full season no Thread practice + three Anchoring Scenes + resolution roll. During the arc, is the RS drain suspended? The rule says "any scene in which they are conscious and present." The crisis arc doesn't require unconsciousness — the practitioner is withdrawing from practice, not catatonic. The RS drain presumably continues during the arc. If so: the arc takes minimum one full season (4 scenes minimum for the Anchoring checks + non-practice season) = 4+ scenes of −1 RS = −4 RS minimum during recovery, plus the crisis arc's narrative uncertainty.

**[EXPLOIT — CATASTROPHIC]** An enemy faction that includes a TS 90+ practitioner who is driven to Coherence 0 (through repeated Thread combat, through forcing many Thread operations) creates a persistent RS drain engine. The player factions cannot simply kill the practitioner — killing a TS 90+ practitioner may cause De-Actualisation effects (if it's a threadcut being) or simply remove one of the most valuable potential allies in the game. The least destructive solution is to help the practitioner through the Rendering Crisis arc — which requires player action specifically to benefit a dangerous NPC.

**Required design note:** "TS 90+ practitioners at Coherence 0 are the highest-priority RS drain event in the game, exceeding all passive drain sources combined. Helping them through the Rendering Crisis arc is not altruistic — it is RS self-preservation. Player factions should treat Resonant practitioner Rendering Crisis as a campaign-level emergency."

---

# 3. PERMANENT LOCK — THE 4-SEASON UNGOVERNABLE PROVINCE

## 3.1 Deliberate Permanent Lock Before Military Defeat [EXPLOIT — STRATEGIC]

A Lock becomes Permanent after 4+ seasons with substrate adapted. Consequences:
- Dissolution of a Permanent Lock auto-fails (no discrete target).
- Pulling a Permanent Lock: the configuration no longer exists as a discrete target → also fails by implication.
- Only the Einhir framework can address it (requires: Knowledge from Southernmost expedition + Einhir Technique + TS 70+).

**Extended Lock-and-cede (Batch 4, §7):** A defending faction's practitioner, anticipating military defeat in Season 6, placed a Relational Lock on provincial institutional loyalty in Season 1. By Season 5 (4 seasons elapsed): the Lock becomes Permanent. The attacking faction arrives in Season 6. They inherit:
1. A Permanent Lock on provincial loyalty (population is frozen in loyalty to the defeated faction).
2. No Pull or Dissolution solution available.
3. Einhir framework required — which requires Sigurdshalm access + Southernmost expedition + TS 70+.
4. Province Accord cannot be raised while the Lock persists (institutional loyalty frozen ≠ transferable).
5. Province is militarily captured but **politically ungovernable for TCV purposes** (Accord cannot reach 2 while loyalty is Locked to the previous faction). TCV does not count at Accord < 2.

**Result:** The attacker has won the province militarily but cannot count its TCV toward universal victory until the Permanent Lock is addressed via Einhir framework. If Sigurdshalm is controlled by a third faction (or hostile Varfell): the Einhir framework is unavailable. The attacker holds a province that costs RS (Permanent Lock RS consequences → none once substrate adapts, per the rules: "substrate adapts. RS drift ceases." So drift actually stops at Permanent!) but provides no TCV.

Wait — I need to re-read: "Permanent (never reversed): Substrate adapts. RS drift ceases. Permanent +1 Ob to adjacent operations." So a Permanent Lock STOPS draining RS once it becomes Permanent (because substrate adapts). This means the Permanent Lock is actually better for the attacker RS-wise than an active Lock (which drains −1 to −2/season). But the Permanent Lock is worse politically (ungovernable province, −Ob adjacent, Einhir framework only solution).

**Revised analysis:** The Permanent Lock is a political landmine, not an RS landmine. It grants a province that looks controlled but yields no TCV, and extraction from it requires Sigurdshalm + Southernmost access. It's a geopolitical poison pill specifically targeted at the TCV-counting victory condition.

**[EXPLOIT — STRATEGIC]** This needs explicit design acknowledgment. A faction with 4+ seasons of forewarning (which IS realistic — military campaigns develop over years) can Permanent Lock their most strategically important provinces before defeat, denying TCV to the victors indefinitely unless Einhir framework resources are available.

---

# 4. VAYNARD THREAD MASTERY (VTM) TRACK — NEVER TOUCHED

## 4.1 VTM as Varfell's Thread Development Path [GAP — SYSTEMIC]

Clock registry: "Vaynard Thread Mastery (VTM) | Varfell | 0–5 | 0." Source: params_board_game.md §VTM.

VTM is a faction-specific BG/Hybrid track for Varfell. It measures Vaynard's Thread knowledge development. The name "Vaynard Thread Mastery" implies Vaynard himself develops Thread capability over the campaign. Starting at 0 with a 0–5 range.

**Threadwork interactions:**
- VTM advances presumably through: Southernmost expeditions (WR/WC overlap?), Private Collection research (PP-258 document RS resonance?), Thread-adjacent events in Varfell-controlled territories.
- VTM at higher values presumably unlocks Varfell Thread capabilities — BG Thread orders, access to Einhir framework resources at Sigurdshalm, potentially Vaynard's own TS growth via archive research (PP-289: "archive research (Spirit + Einhir Scholar, TN 7, Ob 2). Maximum potential TS 40-50").
- Vaynard at TS 30+ (achievable via archive research if VTM gates progression) becomes a practitioner with full Thread op access.

**[GAP — SYSTEMIC]** VTM is listed in the clock registry but its mechanics are entirely in params_board_game.md (not fetched). The threadwork interactions are substantial: VTM = Vaynard's Thread development path = potential TS 40-50 practitioner in Varfell faction = major Thread-political actor. The entire Varfell Thread faction strategy depends on VTM progression mechanics that are undefined in available documents.

**Critical question:** Does VTM advancement produce Vaynard as a TS 30+ practitioner? If yes: Varfell gains BG Thread order capability (Mend, Weave, Investigate) contingent on VTM reaching the threshold where Vaynard can Leap. This transforms Varfell from "weak Thread capability" to "full Thread capability" at a campaign milestone. The TCV impact (Sigurdshalm at TCV 3, Private Collection controlling Einhir access, Vaynard potentially TS 40-50) makes Varfell the most Thread-strategically positioned faction if VTM succeeds.

---

# 5. TORBEN LOYALTY TRACK + THREAD INTERACTIONS

## 5.1 Torben Loyalty as Thread-Manipulable BG Track [EMERGENT+]

Clock registry: "Torben Loyalty | Crown → Löwenritter | 0–7 | 3." Source: params_board_game.md §Torben (PP-498).

Torben is Almud's heir. His Loyalty track (starting at 3, range 0-7) determines his factional allegiance — Crown retains heir if Loyalty > threshold; Löwenritter Coup relies on Torben Loyalty reaching their threshold.

**Almud's Belief #3:** "Torben must be kept from Altonian influence — he is Valoria's future." Almud's Belief ties his personal agenda to the Torben Loyalty track. A Thread practitioner who targets Torben's relational configuration (his loyalty bonds, his belief orientation) can manipulate the Torben Loyalty BG track via personal-scale Thread operations that then echo through Domain Echo into the BG layer.

Specifically:
- **Weaving Torben's loyalty configuration** (Personal scale: Ob 2 + Breadth 0 + Distance 0 = Ob 2, TN 7): coheres his loyalty to Crown. Could this produce a Torben Loyalty +1 via Domain Echo (personal action → faction consequence)?
- **Pulling Torben's loyalty configuration** (Personal scale: Ob 2, normally actualized): opens his loyalty, making him susceptible to other influences. Could produce Torben Loyalty −1 (toward Löwenritter) via Domain Echo.

**The Torben Loyalty track is a BG mechanic with a personal-scale Thread manipulation vector.** A TS 30+ practitioner with access to Torben (S-001 Valorsplatz Palace) can treat the Crown succession as a Thread target. The operation is low-Ob (Personal scale, Ob 2) and highly consequential (Löwenritter Coup depends on this track).

**[EMERGENT+]** Thread manipulation of the heir's loyalty configuration is the most consequential low-Ob operation available. At Ob 2 TN7 with 17D pool: P(Overwhelming) ≈ 99%. The Torben Loyalty track is almost trivially manipulable via Thread if the practitioner has access to Torben's person. The limiting factor is access (Almud protects Torben) and co-movement (Weaving a royal heir's loyalty in the palace is a massive event if detected — Batch 1 finding: Church Inquisitor at S-003 may detect it). The political detection risk is the primary constraint, not the Thread Ob.

---

# 6. PARLIAMENT INTEGRITY (PI) TRACK + THREAD

## 6.1 PI Auto-Resolves at 20 — Thread Operations Can Force This [EMERGENT+]

Clock registry: "Parliament Integrity (PI) | 0–20 | 7 | ↑ (cumulative pressure) | Auto-resolves at PI ≥ 20."

Parliament Integrity tracks the parliamentary institution's structural health. It starts at 7 and advances (under pressure). At PI ≥ 20: auto-resolves (presumably Parliament collapses, restructures, or produces a decisive constitutional event).

**Thread interactions:** The N-way Parliamentary Thread catastrophe (Batch 2) would produce a Relational Gap in Parliament. A Relational Gap in Parliament's deliberative chamber should advance PI significantly — it's an extreme institutional disruption. How much? Undefined in available docs.

More specifically: **Deliberate PI manipulation via Thread.** A faction that wants Parliament to auto-resolve (e.g., Hafenmark, whose Parliamentary Manoeuvre power depends on Parliament functioning vs Crown or Church who might prefer Parliament disabled) could:
1. Deliberately create conditions for N-way opposing Thread operations in Parliament.
2. Each N-way collapse produces a Gap + RS drain — and presumably PI advance.
3. With 4 N-way collapses (achievable across 4 Parliamentary sessions): PI could advance from 7 to 20 (if each collapse produces ~3 PI advance).

**[EMERGENT+]** Parliament Integrity auto-resolve is a designed endpoint. Thread-forcing it via deliberate Parliamentary Thread chaos is an extreme but mechanically reachable strategy. Requires knowledge of which factions have practitioners, coordination to ensure at least 3 opposing intentionalities target the same configuration simultaneously, and political cover for the resulting chaos. This is the Thread equivalent of a constitutional coup — destabilizing the institution itself.

---

# 7. CHURCH ATTENTION POOL (AP) AS SYSTEMIC THREAD DETECTION MECHANISM

## 7.1 Thread Detection → AP → Inquisitor Deployment → TC [EMERGENT+ — SYSTEMIC]

Clock registry: "Church Attention Pool (AP) | 0–10 per territory | 0 | params_board_game.md §Church Inquisitor. First Inquisitor at AP ≥ 3; second at AP ≥ 6."

AP is a per-territory counter. The Church deploys Inquisitors at AP thresholds. TC advances from Inquisitor Investigation successes (PP-182: Church Inquisitor with TS 30+ witnesses Thread op → formal Investigation → TC +1 at next Accounting if Investigation succeeds at Ob 2).

**The full causal chain:**
1. Thread operation performed in territory.
2. Church agent with TS 30+ present → perceives operation (TS 30–49: general direction).
3. Church initiates formal Investigation (Domain Action, Ob 2) → TC +1.
4. Repeated TC advances eventually reach 75 (freeze ceiling, ED-303).
5. **But AP is the PRIOR step:** AP advances from Thread-related events in the territory. AP ≥ 3 → Inquisitor deployed. Inquisitor has TS 30+ (presumably — otherwise they can't fulfill their detection function). Inquisitor deployed to territory → Thread ops in that territory are now automatically observed.

**AP as amplifier:** Before AP ≥ 3, Thread ops in a territory are unobserved (no Inquisitor present, civilian population TS 0). After AP ≥ 3, all Thread ops in that territory are observed by the Inquisitor. AP turns a "safe" Thread territory into a permanently-observed one.

**What advances AP?** Unknown from available docs (params_board_game.md §Church Inquisitor not fetched). But inferred: Thread-adjacent events (open Thread ops, Certainty-declining populations, Dissolution residue formation) advance AP. The Batch 2 finding (Almud's First Leap at S-001 → Church observer at S-003 → TC +1) generates AP at T1 Valorsplatz.

**[EMERGENT+ — SYSTEMIC]** AP is the systemic bridge between Thread activity and Church political power. Every Thread operation in a territory contributes (indirectly) to AP → Inquisitor deployment → more Thread ops observed → TC escalation. The Thread-active faction accelerates its own Church persecution by being Thread-active. This is the core political tension of playing a practitioner faction and it needs to be explicitly stated in the design documentation.

---

# 8. VICTORY CONDITION + THREAD AGGRESSION → PENINSULAR STRAIN LOCK

## 8.1 Faction Elimination Via Thread Advances Peninsular Strain [EMERGENT+]

Peninsular Strain §0.3: "Global track (0–10). Advances from inter-faction battles, faction eliminations, revolts." Universal victory requires Peninsular Strain ≤ 6.

A faction that uses Structural Dissolution to collapse an enemy faction (Stability −2 from Structural Dissolution per Batch 4 ruling — pending), then military conquest to capture their remaining territories, eliminates the faction. Faction elimination advances Peninsular Strain. If Thread-assisted military conquest eliminates 2 factions: Peninsular Strain may exceed 6, blocking universal victory.

**More specifically:** The faction using Thread to win cannot achieve the very victory condition their Thread was meant to enable. Universal victory requires Accord ≥ 2 (which requires governing well = non-Thread-coercive governance) AND Peninsular Strain ≤ 6 (which requires NOT eliminating factions = militarily restrained approach). The most powerful Thread operations (Structural Dissolution, Permanent Lock, RS brinkmanship to force enemy retreat) all advance Peninsular Strain.

**[EMERGENT+]** The game's victory conditions structurally reward cooperative governance over Thread-aggressive conquest. The player who Thread-fights their way to dominance creates Peninsular Strain that may block their victory. The only way to win universally via Thread is: use Thread exclusively for RS maintenance, settlement Order stability, and targeted political influence — never for faction elimination. Thread as political tool enables victory; Thread as weapon prevents it.

**This should be an explicit design note in the victory architecture:** "Thread-aggressive strategies (faction elimination via Structural operations, RS brinkmanship, widespread Dissolution) are self-defeating toward universal victory. The universal victory condition structurally rewards Thread-cooperative play."

---

# 9. FREE AGENT PRACTITIONERS AFTER FACTION ELIMINATION

## 9.1 Enemy Practitioners as Dangerous Loose Ends [EMERGENT+]

Settlement spec §6.3 (Faction Collapse): "Its officers become free agents eligible for recruitment by other factions." Practitioners in the eliminated faction are free agents.

A free agent practitioner carries:
- Their Thread Sensitivity (TS) — cannot be removed.
- Their Dissolution Residue (Potency rating — accumulated from operations they performed while in the faction).
- Knowledge of all Locks they personally placed (they know the Ob to Pull their own Locks = TS ÷ 10 − 2). They can reverse their own Locks for much lower Ob than anyone else.
- Their Coherence state — if they're in Fragmented or Fractured, they're already degraded.
- Potential active co-movement relationships with their former Knots (the Knot ruptures from faction collapse may create strain events).

**Strategic implications:**
- A free agent TS 70+ practitioner who Locked several of the conqueror's now-occupied provinces can unilaterally REVERSE those Locks (Pull at trivially low Ob for their own Locks) if they're recruited by a rival faction. The conqueror's ungovernable provinces become governable again — for the recruiter.
- A free agent practitioner with Dissolution Residue Potency 5 is the most dangerous asymmetric Thread weapon available. A single session with residue-enhanced Structural Dissolution could threaten Rupture.
- A TS 90+ free agent at Coherence 0 (Reality Strain drain) is an immediate RS emergency that affects all factions equally.

**[EMERGENT+]** Free agent practitioners after faction elimination should be treated as campaign-level crisis events. The conquering faction has an urgent incentive to either: (a) recruit the free agent practitioners before rivals do, or (b) assist them through Rendering Crisis (removing the Reality Strain RS drain). Battlefield elimination of practitioner opponents is almost never optimal — converting them is.

---

# 10. PLAYER BELIEFS VS THREAD OPERATIONS — P-12 SELF-CONSTRAINT

## 10.1 Belief Directly Opposing Thread Practice — Pre-Leap Belief Check [GAP]

Threadwork §2.5 (Collective Operations): "If a helper's Belief directly opposes the operation's declared goal, the helper must pass a pre-Leap Belief check (Spirit TN 7 Ob 1)."

P-12 (§2.5): "Directly opposing Beliefs require a pre-Leap Belief check. Tangential conflicts: non-chaining dice."

This rule is stated for Helpers in collective operations. But the philosophical foundation establishes that Beliefs govern all Thread engagement — not just collective operations. A practitioner's own Beliefs could oppose their own Thread operation.

**Scenario:** A player character early in the campaign writes Belief: "Thread practice is spiritual corruption — it tears the world apart." The character then develops Thread Sensitivity (through play exposure, not deliberate study) and reaches TS 30. Their Belief directly opposes performing a Leap.

**Does the pre-Leap Belief check apply to solo operations where the practitioner's OWN Beliefs oppose the operation?** The text is written for Helpers in collectives, but the philosophical principle (P-12) is universal. A practitioner who genuinely believes Thread practice is wrong and then attempts a Leap would face: their own intentionality opposing their own operation. The Leap requires suspending rendering — but the practitioner's Belief "rendering should not be suspended; Thread is corruption" actively resists the surrender.

**[GAP]** Solo practitioner Belief opposition to their own Thread operations is undefined. Proposed: "A practitioner whose own active Belief directly opposes a Thread operation they are attempting must pass a pre-Leap Belief check (Spirit TN 7 Ob 1) before rolling the Leap. Success: the practitioner suppresses the Belief enough to attempt the Leap (with non-chaining History dice if the Belief governs this domain). Failure: the Leap cannot be attempted this round. The Belief was not suppressed — rendering held."

**[EMERGENT+]** This creates a natural character arc where a practitioner who began as a Thread skeptic (Belief opposing Thread) must either change that Belief (through play, through experiencing Thread's necessity) or face mechanical resistance to their own operations. The Belief system becomes a practitioner growth constraint, not just an NPC interaction tool.

---

# 11. DOMAIN ACTION LOCKING — FACTION OPERATION INTERRUPTION

## 11.1 Thread-Interrupting a Faction's Domain Action [EMERGENT+]

A faction's Domain Action is in progress (e.g., Crown is executing a Fortify action — building fortifications at S-006 Lowenskyst, declared at Phase 1, resolving at Phase 5). The Domain Action's in-progress state is a relational/territorial configuration: the faction's invested resources, labor, and intent all constitute an actualization in progress.

A hostile practitioner could target this configuration:
- **Relational Pull** (disrupting the organizational coherence of the fortification effort): Depth 3 + Breadth 2 (Formation: workers, soldiers, administrators) + Distance 0-1 = Ob 4-5, TN 7. On Success: the Domain Action's configuration opens. Does this force a Domain Action roll penalty? Or does it produce a flat Domain Action failure?
- **Object-scale Pull** (targeting a specific component — the supply chain, the lead architect's plans, the mason guild's cooperation agreement): Depth 1 + Breadth 0 + Distance 0 = Ob 1, TN 7. On Success: one component of the Domain Action is disrupted.

**The Domain Action system has no Thread interface.** Domain Actions are faction-layer mechanics that operate on faction stats and roll outcomes. Thread operations are personal-scale that echo through Domain Echo into faction consequences. But direct Thread targeting of an in-progress Domain Action is undefined.

**[EMERGENT+]** Proposed: "A practitioner may target an in-progress Domain Action's underlying relational/territorial configuration via Thread operations. The Domain Action's actualization level for Pull purposes = Standard (Ob 2, base) + Depth by scale (Relational for organizational actions, Territorial for geographic actions) + Distance. A successful Pull reduces the Domain Action's roll by a number equal to net surplus successes on the Pull (minimum 1). A Failure snap-back causes the Domain Action to succeed with an additional +1 net (the Pull disrupted the disruption)."

---

# 12. COMPOUND OB WORST-CASE IN LATE GAME

## 12.1 Late-Game Thread Operation at Compound Ob 14 [EMERGENT — DESIGN VALIDATION]

Constructing the worst-case compound Ob scenario for a Thread operation in the final act:

Base operation: Relational Weave at a settlement in a contested province.
- Depth 3 + Breadth 2 + Distance 1 = **Ob 6** (three-axis base).

Modifiers stacking:
- RS Critical (19–1): +1 Ob worldwide = **7**.
- Practitioner Coherence Fragmented (4–3): +1 Ob = **8**.
- 2 Wounds: +2 Ob (per wound penalty on all Thread ops) = **10**.
- Hostile faction controls territory (fieldwork Ob modifier, applicable to Thread-Read at least — does it apply to all Thread ops in hostile territory? Unresolved. If yes:) +1 Ob = **11**.
- Opposing practitioner in same scene (TPS 5, floor(5/2) = +2 Ob) = **13**.
- Overweaving (second op in same contact window) = **14**.

Pool: Spirit 4, History +5D, TPS 5 = 18D. At Ob 14, TN 7: E[net] = 5.4. P(≥14) ≈ 1.8%. Essentially impossible.

At Ob 10 (removing Opposing and Overweaving): P(≥10) ≈ 17%.
At Ob 8 (removing additionally the 2 Wounds): P(≥8) ≈ 45%.

**The compound Ob stack tells the story of late-game Thread practice:** Each additional crisis condition (Coherence degradation, wounds, RS Critical, opposition) multiplies the difficulty. A practitioner trying to help in the endgame while wounded, Fragmented, and opposed is statistically ineffective. Only fresh practitioners (high Coherence, unhurt, unopposed) can reliably operate at late-game RS Critical conditions. This validates the "reserve practitioners for the endgame" design note from Batch 3.

**[EMERGENT — DESIGN VALIDATION]** The compound Ob calculation confirms the endgame design: Thread operations require healthy, non-depleted practitioners. A campaign that burns out all practitioner Coherence in the midgame has no Thread capability for the endgame crisis. This is correct design, explicitly validated. No change needed — surface as explicit design validation in the endgame documentation.

---

# 13. CALAMITY RADIATION + THREAD OPERATIONS AT PROXIMITY 0 (ASKEHEIM)

## 13.1 Multi-Source Ob Stacking at T15 Askeheim [EMERGENT+ — COMPOUNDING]

Fieldwork_v30: Calamity radiation = "+1 Ob per RS band below 60 at current Proximity Rating." The Proximity Rating for T15 Askeheim (Catastrophe epicenter) is Proximity 0 — maximum radiation.

**RS band below 60 at Proximity 0:**
- RS 59-40 (Fragile): +1 Ob at Proximity 0.
- RS 39-20 (Fractured): +2 Ob at Proximity 0.
- RS 19-1 (Critical): +3 Ob at Proximity 0.

**Does Calamity radiation apply to Thread operations at T15?** The fieldwork doc says "+1 Ob per RS band" applies to fieldwork rolls. Thread operations at T15 are not fieldwork rolls (except Thread-Read). But the philosophical basis — the substrate is damaged near Askeheim, making all perceptual and intentional work harder — should apply to Thread operations as well. Thread is the deepest form of substrate engagement; a damaged substrate (near-Askeheim) logically increases Thread op difficulty.

**At RS Critical and Proximity 0, applying Calamity radiation to Thread ops:** +3 Ob (Critical band, Proximity 0). A Field-scale Mending at Askeheim: Depth 5 + Breadth 2 + Distance 0 + RS Critical +1 + Fragmented +1 + Calamity +3 = **Ob 12**. With the Einhir framework: Mending Ob = Depth Ob − 1 = 11 + modifiers = still ~Ob 12-14.

**[GAP]** Calamity radiation's applicability to Thread operations (not just fieldwork) is undefined. Required ruling: "Calamity radiation Ob modifier applies to all actions requiring intentional engagement with the substrate at Askeheim-adjacent territories (T15, and at reduced rate T6, T13, T11 at Proximity 1-3), including Thread operations. Thread operations at Proximity 0 receive the full Calamity radiation Ob modifier." This makes Askeheim Thread operations progressively harder as RS degrades — the location where Mending is most needed is also the location where it becomes least possible.

---

# 14. CHURCH TRIBUNAL — THREAD SELF-INCRIMINATION TRAP

## 14.1 Thread Operations During Heresy Trial Are Self-Defeating [EMERGENT+]

Social contest §2: "Church Tribunal: 1–5 (Inquisitor sets) | Inquisitor proposes throughout | Halved for accused."

A practitioner accused of Heresy (Thread practice) is in a Church Tribunal where the Inquisitor proposes throughout. The accused responds. The Tribunal is investigating Thread use.

**If the accused practitioner uses Thread operations to influence the Tribunal:**
1. The Church Inquisitor (likely TS 30+ — they're deployed specifically to detect Thread) perceives the operation (TS 30–49: senses an operation, general direction).
2. They can cite this as direct evidence during the Tribunal's own proceeding.
3. The practitioner has literally performed a Thread operation during a Heresy Trial for Thread operations. This is the strongest possible Conviction evidence.
4. Co-movement fires: epistemic auto-effect (+1 Ob social rolls if Partial/Failure). This degrades the accused's own Argue pool for the current and next exchange.

**Thread use during a Heresy Tribunal is self-defeating under almost all conditions.** The only scenario where it might not be: if the practitioner uses Thread operations to Mend — which is philosophically positive, produces settling co-movement rather than destabilizing co-movement, and could be interpreted as evidence that Thread practice is restorative, not destructive. A Mending during the Tribunal produces epistemic auto-effect (Success: "Settling. Thread Sensitivity 10+ observers perceive calming. Non-sensitives may notice subtle easing."). The Inquisitor perceives the operation — but perceives it as calming.

**[EMERGENT+]** The Church Tribunal is the one context where the practitioner's best Thread strategy is Mending (if they do Thread at all) — not any other operation. A practitioner who Mends during their own Heresy Trial is making an argument through action: "Thread practice repairs the substrate. This is what I do." Whether the Inquisitor accepts this argument is a social contest question. But the co-movement is on the practitioner's side.

---

# 15. KNOT AS THREAD TARGET — WEAVING OR PULLING THE KNOT ITSELF

## 15.1 The Knot Is a Relational Thread Configuration [GAP — CRITICAL]

PP-632: "Knots are being-with (Mitsein), not Thread operations. Any character. TS not required." Knots are ontological — they constitute the relational being-with of bonded characters.

But: Thread operations target relational configurations. A Knot IS a relational configuration — arguably the most fundamental one (Mitsein = being-with at the most basic level). Can a Thread practitioner target a Knot with:

**Weaving a Knot:** Cohering the relational bond. The Knot becomes over-actualized — more firmly bonded. Social actions between the Knotted pair are easier (the bond is Thread-cohered, not merely relational). OA applies: subsequent Thread operations targeting the same Knot config +1 Ob.
- Ob: Personal (Depth 2, one person's configuration... or Relational, Depth 3, the connection between two specific entities?) + Breadth 0 + Distance 0. Probably Relational (Depth 3): the Knot IS a relational configuration.
- Weaving a Knot (Relational): Ob 3, TN 7. Very achievable.

**Pulling a Knot:** Opening the relational bond — making it more porous, susceptible to outside influence, easier to break. A pulled Knot would make Solidarity attacks on the bonded NPC easier (the relational obligation is less firmly actualized). Duration: if surplus successes ≥ 3 → until next seasonal Accounting.

**[GAP — CRITICAL]** No rule addresses whether Knots are Thread-targetable configurations. This is fundamental: Knots are described as "Mitsein, not Thread operations" — but this describes their NATURE, not whether they can be targeted. Mitsein is still a configuration in the substrate. The question is whether Thread practitioners can engage with Mitsein-layer configurations.

**Required ruling:** "Knots, as constitutive relational configurations (Mitsein), occupy the Relational scale of Thread operation. They can be targeted by practitioners with TS ≥ 50 (Relational scale minimum). Weaving a Knot: OA applies; on Success, the Knot's social bonuses extend to +2D (vs standard +1D) for one season. Pulling a Knot: opens the bond; Solidarity attacks on the targeted partner are at −1 Ob for the Pull's duration. Locking a Knot: prevents the Knot from changing tier or breaking; the bond is frozen in its current state — cannot be Ruptured or Lost while the Lock holds. Dissolving a Knot: tears the Mitsein. Both bonded characters lose the Knot (as Loss consequences) immediately. RS −5 (Dissolution Success). The practitioner has torn a fundamental ontological bond — the RS cost reflects this."

---

# 16. COMMUNITY WEAVING AS REVOLUTION PROXY BG MEND — CHURCH ALLIANCE IMPLICATIONS

## 16.1 Revolution (RM) Can Issue BG Mend Orders Without High-TS Affiliated Character [EMERGENT+]

Threadwork §7.1 BG Mend order: "Available to any faction with an affiliated Thread Sensitivity 50+ character, OR Revolution (via Community Mending)."

The OR creates an asymmetric exception: Revolution can issue Mend BG orders through the Community Mending mechanism, bypassing the TS 50+ requirement. Revolution's Mend orders come from distributed community Thread practice (Community Weaving), not from a single high-TS practitioner.

**Incompatible co-victory pairings (peninsular_strain §0.1):** "Incompatible: Crown + Church, Crown + Löwenritter, Church + Varfell, **Church + RM**." Church and Revolution CANNOT co-victory. They are factionally incompatible.

But: can the Church **commission** RM Community Mending in a territory the Church controls? Not as a co-victory — as a contractual arrangement. The Church cannot issue Mend orders (Batch 3 finding: TS 0 leadership). Revolution CAN issue Mend orders. If Church territory is experiencing RS degradation and the Church needs Mending, could they invite RM practitioners to perform Community Weaving in their territories?

**Politically: almost certainly not** (Church views Thread practice as heresy). But mechanically: Community Weaving is a Thread operation that any faction can permit in their territory if they don't revoke the permission. The Church's theological position is hostile to Thread, but the game mechanic doesn't prevent Community Weaving from occurring in Church territories unless the Church actively suppresses it (via Inquisitors, AP threshold, TC actions).

**[EMERGENT+]** The RS crisis creates a scenario where the Church faction (unable to Mend themselves, aware the world is degrading) must choose between theological principle (suppress Thread practice = advance TC = accelerate their own victory path) and existential pragmatism (permit Community Weaving in Church territories to offset RS drain = compromise theological position). This is one of the most interesting faction-level dilemmas in the game and it emerges entirely from the intersection of the Mend BG order restriction, the Church's TS 0 constraint, and Revolution's community Mending exception.

---

# 17. THE CEIRAL RITUAL — FAILURE = RS +8 (COUNTERINTUITIVE)

## 17.1 Southernmost Failure as Substrate Release [GAP — DESIGN VERIFICATION NEEDED]

ED-034 resolution: "Ceiral Ritual RS changes: Success RS −6, Overwhelming RS −10, Partial RS −3, **Failure RS +8**."

The Ceiral Ritual on Failure produces the largest single RS restoration in the game (+8). No other single operation or event produces RS +8 from Failure. This is counterintuitive — failure usually costs RS (Thread Partial/Failure = RS −1 to −8).

**Possible interpretations:**
1. **Typo/error:** Failure and Overwhelming are swapped. RS −10 on Overwhelming and RS +8 on Failure is a copy error; intent was RS +8 on Overwhelming and RS −10 on Failure. This interpretation makes the Ceiral Ritual a high-risk/high-reward operation (Success = RS −6, Overwhelming = RS +8 restoration, Partial = RS −3, Failure = RS −10 catastrophe). This matches the general pattern.
2. **Intentional design:** The Ceiral Ritual's Failure means the ritual collapses back into the substrate — the intended disruption fails and the substrate reasserts itself, releasing the tension that was being worked. Failure = the substrate rejecting the operation = RS restoration as the unintelligible ground floods back into the space being worked. This is philosophically coherent with the Southernmost setting (the substrate there is overwhelmingly present; failure means the substrate wins).
3. **Intentional design (dark):** The Ceiral Ritual is an RM ritual for interfering with Church power. Its Failure in the Southernmost context means something catastrophically unexpected happened — the substrate's response is not RS drain but RS surge, as if the ritual accidentally completed some aspect of substrate repair while failing its intended purpose.

**[GAP — DESIGN VERIFICATION]** This cannot be resolved without designer input. The Ceiral Ritual's Failure = RS +8 is either the most interesting mechanic in the game (failure has a positive world effect because you're working near the substrate's raw self-repair tendency) or a documentation error. Required: explicit designer confirmation of intent.

---

# 18. BG HARVEST ORDER — UNDEFINED MECHANIC

## 18.1 Harvest Is Listed but Never Defined in Available Documents [GAP]

Threadwork §7.3 cross-mode table: "Board Game: Weave, Mend, Investigate, **Harvest** — faction-scale." Harvest is listed as a BG Thread order alongside Weave, Mend, Investigate.

Threadwork §7.1 (BG): "New Order: Mend" — only Mend is given a full definition. Weave is referenced but not fully defined for BG. Harvest has no definition anywhere in the available documents.

**What might Harvest do?** Inferred from context:
- Harvest likely involves collecting Dissolution Residue from Gap sites (Residue "remains" after Dissolution, per §6.4 De-Actualisation). A BG Harvest order might collect Residue as a faction resource.
- Clock registry §7.1 BG: "Cards 16–18 added: 18. Residue Condensation — dissolution residue forms at Mending site. Niflhel may harvest." The Co-Movement card specifically connects Niflhel with Harvest. Niflhel is a covert faction.

**Niflhel Harvest:** Niflhel harvests Dissolution Residue. This is a Thread-adjacent faction power for Niflhel that creates a faction incentive to encourage (or cause) Dissolution events — so they can Harvest the Residue. Niflhel benefits from Thread catastrophes. This is a fundamental game-theoretic insight: Niflhel's faction interest is aligned with RS destabilization (more Dissolutions = more Residue to Harvest = stronger Niflhel Thread capabilities).

**[GAP — NIFLHEL DESIGN]** If Niflhel Harvests Dissolution Residue as their primary Thread resource mechanic, they are the one faction whose strategic interest directly opposes RS preservation. Every other faction benefits from preventing Rupture (shared loss at RS 0). Niflhel benefits from maintaining high Dissolution activity (for Residue) while stopping just short of Rupture. This is a profoundly interesting faction design — the faction that plays the long game of controlled Thread catastrophe.

---

# SUMMARY TABLE — BATCH 5

| Item | Finding | Severity | Action Required |
|------|---------|----------|----------------|
| PP-603 RS cap struck | Seasonal ±10 cap struck canonically (PP-603) but still present in skeleton + Hybrid docs | **[CONFLICT — CRITICAL]** | Purge cap language from all skeleton references; update Hybrid section |
| No-cap RS + PP-225 mass battle | Mending Overwhelming ×3 in mass battle = RS +6/op; five ops = RS +30/season; no cap = full swing | **[EMERGENT+]** | State explicitly: RS is high-variance, no smoothing, both directions |
| TS 90+ Coherence 0 | −1 RS/scene = −30 RS/year; fastest single-entity RS drain in the game | **[EXPLOIT — CATASTROPHIC]** | Design note: Resonant practitioner Rendering Crisis is a campaign-level RS emergency |
| Permanent Lock | 4-season Lock becomes Permanent; invader inherits ungovernable province; only Einhir framework solution | **[EXPLOIT — STRATEGIC]** | Surface "poison pill" Lock-and-cede as named strategic option |
| VTM track | Vaynard Thread Mastery track unexplored; if gates Vaynard TS growth, Varfell becomes most Thread-capable faction at mid-campaign | **[GAP — SYSTEMIC]** | Fetch params_board_game.md §VTM; define Thread mechanic interactions |
| Torben Loyalty + Thread | Personal-scale Weave/Pull on Torben (Ob 2) manipulates the BG Torben Loyalty track via Domain Echo | **[EMERGENT+]** | Note: lowest-Ob, highest-consequence Thread operation available; constrained only by detection risk |
| Parliament Integrity (PI) | N-way Thread collapse in Parliament likely advances PI; deliberate PI-rushing via Thread chaos is reachable | **[EMERGENT+]** | Define PI advance per Thread-caused Parliamentary event |
| Church AP system | AP per territory → Inquisitor deployment → perpetual Thread observation → TC escalation; AP is the systemic Thread detection bridge | **[EMERGENT+ — SYSTEMIC]** | State explicitly: Thread-active factions accelerate their own Church persecution via AP |
| Victory + Thread aggression | Faction elimination via Thread advances Peninsular Strain → Strain > 6 blocks universal victory | **[EMERGENT+]** | Design note: Thread-aggressive conquest is self-defeating for universal victory |
| Free agent practitioners | Eliminated faction's practitioners carry Residue, Lock knowledge, Coherence state; dangerous loose ends | **[EMERGENT+]** | Note: converting practitioners > killing practitioners; Reality Strain NPC = immediate campaign emergency |
| Player Beliefs vs Thread (P-12) | Solo practitioner's own Beliefs can oppose their Leap; pre-Leap Belief check for self-opposition undefined | **[GAP]** | Rule: solo pre-Leap Belief check on directly opposing Beliefs; creates natural practitioner arc |
| Domain Action Locking | Thread targeting of in-progress Domain Actions is undefined; Pull on organizational Domain Action should reduce roll | **[EMERGENT+]** | Define Thread-to-Domain-Action interference; proposed: net surplus successes = Domain Action roll penalty |
| Compound Ob worst case | RS Critical + Fragmented + 2 Wounds + Opposing + Overweaving = Ob 14; P(≥14) ≈ 1.8% at 18D | **[EMERGENT — DESIGN VALIDATION]** | Reserve fresh practitioners for endgame; confirm intentional |
| Calamity radiation + Thread at Askeheim | Calamity radiation applicability to Thread ops undefined; at Proximity 0 + RS Critical = +4 Ob additional | **[GAP]** | Ruling: Calamity radiation applies to Thread ops; Askeheim Thread work hardest when most needed |
| Church Tribunal Thread trap | Thread use during Heresy Tribunal is self-incriminating; only Mending has positive co-movement exception | **[EMERGENT+]** | Surface: Mending during own Tribunal is the only viable Thread strategy |
| Knot as Thread target | Knots are Relational configurations and can be Woven/Pulled/Locked/Dissolved; no rule currently addresses this | **[GAP — CRITICAL]** | Full ruling proposed in text; Dissolution of a Knot = RS −5 + immediate Loss consequences for both |
| RM Community Mending as Church proxy | Church cannot Mend; Revolution can; RS crisis may force Church to permit RM Thread practice in Church territories | **[EMERGENT+]** | Surface as faction dilemma: theological principle vs RS pragmatism |
| Ceiral Ritual Failure = RS +8 | Most likely a typo (Success/Overwhelming swap) or a deep Southernmost design (substrate reasserts on failure) | **[GAP — DESIGN VERIFICATION]** | Require designer confirmation of intent before Ceiral Ritual can be used in any RS calculation |
| BG Harvest order undefined | Harvest listed but undefined; inferred: Niflhel collects Dissolution Residue; Niflhel's faction interest = controlled Thread catastrophe | **[GAP — NIFLHEL DESIGN]** | Define Harvest mechanics; confirm Niflhel's strategic alignment with controlled RS destabilization |

---

## NEW CRITICAL ITEMS FROM BATCH 5

16. **PP-603 RS cap language** — three locations in the skeleton still reference a cap that was struck. Any GM using the skeleton will apply a cap that doesn't exist. Must purge before any document is player-facing.

17. **TS 90+ Coherence 0 RS drain rate** — −1 RS/scene is the fastest single-source RS drain in the game, faster than all passive sources combined. Any campaign with a Resonant practitioner who reaches Coherence 0 and isn't resolved is in immediate RS emergency. No design documentation warns of this.

18. **Knot as Thread target** — the most fundamental relational unit in the game has no Thread-targeting rules. Given that Thread operates on all relational configurations, this is an unavoidable gap that will arise in play the first time a practitioner antagonist tries to damage a player's Knot through Thread means.

19. **Ceiral Ritual Failure = RS +8** — cannot be used in any RS calculation until designer intent is confirmed. If it's a typo, all Southernmost RS modeling is wrong; if it's intentional, Southernmost has a mechanic where deliberate ritual failure is the fastest RS restoration available.

20. **Niflhel as RS-destabilizing faction** — if Harvest = Dissolution Residue collection, Niflhel is the only faction whose strategic interest aligns with controlled Thread catastrophe. This is either a brilliant asymmetric design or an unexamined implication. Either way it must be stated.

---

*End of document. Session d8b924fb834a398c.*
