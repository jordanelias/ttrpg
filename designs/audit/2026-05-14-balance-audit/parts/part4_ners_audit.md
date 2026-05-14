# NERS Audit — Corrected Balance Tweaks (4-Faction Model)
## Date: 2026-05-13 · Session: ners-audit · Part 4/5 · Status: AUDIT-COMPLETE
## Companions:
- `part3_4faction_balance_resim_2026-05-13.md` (Part 3 — corrected sim; subject of this audit)
- `errata_part1_4faction_corrections_2026-05-13.md` (Part 1 — canonical correction)
- `log_schema_part2_2026-05-13.md` (Part 2 — log schema)
## Precedents:
- `designs/audit/2026-04-30-architecture-session/01_week_audit_NERS.md`
- `designs/audit/2026-04-28-political-dynamics-session/22_NERS_and_bloat_assessment.md`

---

## §1 Frame

This audit applies the **NERS framework** — Necessary, Elegant, Robust, Smooth — across
**6 directions** — top-down, bottom-up, vertical, diagonal, lateral, horizontal — to
each of the 9 active balance tweaks from Part 3 §3. 24 cells per tweak. 216 verdict
cells total.

A tweak passes only if all 4 axes return ≥ pass / conditional across all 6 directions
relevant to its scope. A `fail` on any axis-direction triggers revision or rejection.
A `conditional` flags a known limitation to monitor in playtest.

This audit does **not** verify throughline coverage — that is Part 5. Part 4 verifies
the **mechanical and design quality** of each tweak in isolation and as a set.

---

## §2 NERS Axes (Definitions)

| Axis | Definition | Pass criterion |
|------|------------|----------------|
| **N — Necessary** | Does the tweak address a real P1/P2 finding? Is the mechanism the minimum intervention? | Tweak targets a confirmed issue and uses minimal change |
| **E — Elegant** | Does the tweak integrate with existing canonical mechanisms cleanly? Does it create new edge cases or special rules? | Uses existing ops vocabulary (Ob modifiers, Token, etc.); minimal new rule surface |
| **R — Robust** | Does the tweak hold under variance — dice outcomes, player strategies, edge cases, regression scenarios? | Effect monotonic / well-defined across the domain |
| **S — Smooth** | UX: comprehensibility at the table; rule load on players; remember-ability | Player can apply the rule from memory after one read |

## §3 Six Directions (Definitions)

| Direction | Definition | Pass criterion |
|-----------|------------|----------------|
| **Top-down** | Alignment with design pillars (4-faction equality, asymmetric paths, BG layer coherence) | Tweak serves the pillar it claims to serve |
| **Bottom-up** | Composition with atomic mechanics (dice, Ob, degree table, AP, Sta, etc.) | No interaction breaks an atomic rule |
| **Vertical** | Scales across player count / campaign length | Same behavior at 2P, 3P, 4P; over 4-season and 12-season arcs |
| **Diagonal** | Cross-layer (BG ↔ scene ↔ personal ↔ articulation) | No unintended cascade into other layers |
| **Lateral** | Cross-faction (other 3 factions' play patterns) | No unintended buff/nerf to another faction |
| **Horizontal** | Temporal — operates correctly across multiple seasons / political arcs | Multi-season behavior matches intent; no exploitable resets |

## §4 Methodology

For each tweak: one 4×6 cell matrix with verdict + 1-line rationale. Verdicts:

- **P** = pass (no concern)
- **C** = conditional (issue noted; track in playtest)
- **F** = fail (revision or rejection required)
- **n/a** = direction not applicable to tweak's scope

Overall verdict per tweak: **PASS** (all P or n/a), **CONDITIONAL-PASS** (some C, no F),
**REVISE** (1+ F), **REJECT** (multiple F or fundamental issue).

---

## §5 Per-Tweak NERS Audit

### §5.1 T-01a — Valorsmark Charter Diminishing Returns

**Proposal:** Each active Royal Charter beyond the first imposes +1 Ob on subsequent
Charter plays by Valorsmark that season.  
**Source finding:** A-07-F1 (Charter loop self-reinforcing positive feedback)  
**Mechanism:** Modifies PP-433 with cumulative Ob penalty

| | **N (Necessary)** | **E (Elegant)** | **R (Robust)** | **S (Smooth)** |
|---|---|---|---|---|
| **Top-down** | P — addresses confirmed P1 self-reinforcement loop | P — single rule addition, no new mechanism | P — monotonic effect; bounded penalty | C — "active Charter count" requires per-season tracking |
| **Bottom-up** | P — directly counters per-seasonal +N stat accumulation | P — Ob modifier is canonical (PP-N category) | P — well-defined for all pool sizes; floors at 0 | P — players already track Charters individually |
| **Vertical** | P — same need at any player count | P — no scaling concerns | P — multi-arc compatible | P — same load 2P–5P |
| **Diagonal** | P — purely BG-layer | P — no scene/personal interaction | P — doesn't cascade to other layers | P — BG-only |
| **Lateral** | C — only Valorsmark has Charters; only Valorsmark affected — fairness defensible but asymmetric | P — other factions' rules untouched | P — doesn't disadvantage other factions | P — others don't have to track this |
| **Horizontal** | P — multi-season cumulative is the point | P — natural reset at season boundary | P — Winter reset of Charter activity per PP-N | C — long-arc memory of which Charters are "first" can drift |

**Overall verdict: PASS** with two minor `C` notes — UX (per-season Charter tracking)
and long-arc memory drift. Both surface in playtest. **Recommend: print the Charter
count threshold on the Valorsmark faction mat to support memory.**

---

### §5.2 T-01c — Royal Guard Cancels Passive Intel Only

**Proposal:** Valorsmark's Royal Guard (PP-442) cancels passive Intel actions only
(Spy, Tribune Investigate). Active Intel (Disinformation, Reveal) is not cancelled.  
**Source finding:** A-17-F1 / D-08-01 — Royal Guard absorbs too broadly  
**Mechanism:** Narrows PP-442 scope

| | **N** | **E** | **R** | **S** |
|---|---|---|---|---|
| **Top-down** | C — Royal Guard is currently broad; narrowing changes Valorsmark's defensive identity. Necessary for Spy meta but reduces Sovereign-defending-self fantasy | P — distinction between passive and active Intel is canonical (Tribune action taxonomy) | P — well-defined; either category triggers or doesn't | C — players must categorize Intel types correctly at play |
| **Bottom-up** | P — distinction respects Tribune card type categorization | P — uses existing taxonomy | P — robust across Intel types | C — categorization requires referencing card; not memorable from feel alone |
| **Vertical** | P — same at any player count | P — no scaling | P — long-arc compatible | P — same load |
| **Diagonal** | P — BG-only | P — no scene/personal cascade | P — Royal Guard remains canonical entity | P — no cross-layer |
| **Lateral** | P — affects only Valorsmark's defense vs other factions' offense | P — symmetric impact on attacker factions | P — doesn't break Hafenmark/Varfell/Church | P — opponents see same Royal Guard behavior on cancellable subset |
| **Horizontal** | P — once-per-season behavior continues | P — no temporal interaction | P — works across arcs | P — same season-to-season behavior |

**Overall verdict: CONDITIONAL-PASS.** The `C` on top-down necessity is real:
narrowing Royal Guard's scope is a Valorsmark **nerf** that opens new Intel pressure.
Per Part 3 §6.2 ranking, T-01c is rank 7 (low impact on win-share band). **Recommendation:
treat T-01c as cross-tweak-dependent — only apply alongside T-09a (Valorsmark Treaty
mid-game boost) to preserve Valorsmark agency.**

---

### §5.3 T-02a — Inquisitor +2 Ob First-Attempt Only

**Proposal:** The Inquisitor +2 Ob penalty on Counter-Narrative applies only to the
first attempt against the Inquisitor's territory per arc. Subsequent attempts use
standard Ob (Conseq +0 from familiarity).  
**Source finding:** A-12-F1, C-Δ-F4 (Varfell structural decline)  
**Mechanism:** Modifies PP-441-COR

| | **N** | **E** | **R** | **S** |
|---|---|---|---|---|
| **Top-down** | P — directly counters Varfell's structural decline finding (P1) | P — "first attempt per arc" is canonical phrasing (used in PP-431-COR, PP-433 etc.) | P — eventual access guaranteed | P — clean storytelling: Varfell *learns* the Inquisitor's pattern |
| **Bottom-up** | P — Ob modifier reverts to pre-Inquisitor baseline | P — single Boolean flag per Inquisitor-territory pair | P — well-defined; one attempt threshold | P — track via faction mat marker |
| **Vertical** | P — same need at any player count | P — no scaling | P — multi-arc compatible | P — same load |
| **Diagonal** | P — BG-only | P — no scene cascade | P — works with arc-scoped Inquisitor presence | P — no cross-layer |
| **Lateral** | C — only Varfell affected; Church loses Inquisitor's Counter-Narrative deterrence after season 1 | P — Church can still relocate Inquisitor as response | P — Church has counter via 2nd Inquisitor (or T-09c cap means real choice) | P — Church experiences clear arc-defined pressure release |
| **Horizontal** | P — arc-scoped familiarity is intrinsically temporal | P — arc reset is canonical | P — long-arc behavior intended | C — players must track first-attempt-vs-subsequent per Inquisitor-territory pair |

**Overall verdict: PASS** with one minor `C` on per-pair tracking. **Recommendation:
mark the Inquisitor token with "First attempt: untriggered / triggered" on the back.**

---

### §5.4 T-02c — Counter-Narrative Overwhelming Relocates Inquisitor

**Proposal:** When Counter-Narrative rolls Overwhelming, Varfell may relocate the
Inquisitor to an adjacent territory of Varfell's choice (subject to Inquisitor placement
rules).  
**Source finding:** A-12-F1 secondary; deepens Varfell options  
**Mechanism:** Adds an Overwhelming-only effect to Counter-Narrative

| | **N** | **E** | **R** | **S** |
|---|---|---|---|---|
| **Top-down** | C — secondary effect; rare. Necessary for *depth* not for *equality* | P — Overwhelming-as-bonus is canonical pattern (combat, debate) | P — well-defined effect; rare occurrence | P — high-leverage moment for Varfell player |
| **Bottom-up** | P — Inquisitor relocation rules canonical (per Active Inquisition deployment) | P — adjacency requirement standard | P — degenerate cases bounded (adjacent Varfell territories rare) | P — single decision point |
| **Vertical** | P — same at any player count | P — no scaling | P — multi-arc compatible | P — same load |
| **Diagonal** | P — BG-only | P — no scene cascade | P — works with Inquisitor mechanics | P — no cross-layer |
| **Lateral** | C — heavy on Church (loses Inquisitor positioning) | P — but rare (Overwhelming roll, 4D vs Ob 2 = 14.2%) | P — frequency-bounded | C — Church player perceives lost Inquisitor as severe; narrative compensation needed |
| **Horizontal** | P — single-season effect | P — no temporal interaction | P — robust | P — well-bounded |

**Overall verdict: PASS** with `C` on lateral Church impact. Rate is ~14% per Counter-Narrative
attempt at peak conditions; over a 6-season arc Varfell may relocate ~1 Inquisitor. **Recommendation:
include flavor language ("the Inquisitor is sent on pilgrimage") to soften the loss
narratively for Church player.**

---

### §5.5 T-03c — Hafenmark Token Costs W−1

**Proposal:** Each Token placed on another faction's mat costs Hafenmark Wealth -1
on placement.  
**Source finding:** A-Δ-10-F2 (Hafenmark concentrated Token pressure on Varfell);
Hafenmark mid-game ascendant  
**Mechanism:** Adds a Wealth cost to Token placement (currently free)

| | **N** | **E** | **R** | **S** |
|---|---|---|---|---|
| **Top-down** | P — throttles Hafenmark's primary soft-power vector | P — Wealth cost is the canonical Hafenmark resource | P — bounded by Wealth ceiling (max 8) | P — single rule: pay 1 W to place |
| **Bottom-up** | P — Wealth ledger handles it cleanly | P — no new mechanism | P — robust across Wealth states (cannot afford → cannot place) | P — clear |
| **Vertical** | P — same at any player count | P — no scaling | P — Token economy still functional at high player count | P — no UX change |
| **Diagonal** | P — BG-only | P — no scene cascade | P — Token mechanics canonical | P — no cross-layer |
| **Lateral** | P — affects only Hafenmark | C — other factions don't have Token-placement equivalent, so the symmetry of "spend resource to pressure" is partial | P — Hafenmark still has Token tools, just metered | P — clean |
| **Horizontal** | P — Wealth-recovery via Trade still possible | P — multi-season Token investment still viable | P — long-arc compatible | P — same load |

**Overall verdict: PASS.** Only `C` is lateral-symmetry (other factions don't have a
"pay-to-pressure" rule; Hafenmark is uniquely throttled). This is intended — Hafenmark
is **the** soft-power faction; the others have different pressure vectors. **Recommendation:
note explicitly in design rationale that this is identity-preserving asymmetric.**

---

### §5.6 T-04a — Revelation Tokens Path A Relaxed

**Proposal:** Varfell can advance one stage of victory Path A (Revelation Tokens)
without external prerequisite verification when holding 3+ Tokens (instead of 5).  
**Source finding:** C-Δ-F4 (Varfell decline); long-arc Varfell progression need  
**Mechanism:** Modifies victory_v30 §Path A threshold

| | **N** | **E** | **R** | **S** |
|---|---|---|---|---|
| **Top-down** | C — necessary if 8+-season runs are expected; less impactful for 6-season arcs | P — threshold change, single number | P — monotonic threshold | P — single number change |
| **Bottom-up** | P — Token count + threshold check is canonical | P — uses existing victory check | P — robust | P — players already check threshold |
| **Vertical** | P — same at any player count | P — no scaling | C — at 3+ players, Revelation Tokens more contested; threshold may be too low | P — no UX change |
| **Diagonal** | C — Tokens generated via Intel actions interact with scene-layer probes; threshold change ripples | P — no new mechanism | C — interaction with Tribune scene-probes needs verification | P — BG layer load unchanged |
| **Lateral** | P — Varfell-specific | P — no faction interaction change | P — doesn't break other factions | P — no cross-faction UX |
| **Horizontal** | P — long-arc accelerator | P — natural pace | C — in a 12-season campaign, lower threshold may accelerate Varfell win past target | C — players may not immediately see effect for several seasons |

**Overall verdict: CONDITIONAL-PASS** with 3 `C` notes — multi-player scaling, scene-layer
diagonal interaction, and long-campaign acceleration. T-04a is **the weakest tweak in
the set**; per Part 3 rank 8. **Recommendation:** defer T-04a until 8+-season playtest
confirms the long-arc Varfell deficit is real and structural rather than a 6-season-window
artifact.

---

### §5.7 T-09a — Valorsmark Treaty Ob Reduction Once Per Arc

**Proposal:** Once per political arc (~4–6 seasons), Valorsmark may declare an
"Influence Surge" Treaty: Treaty Ob = floor(target L/2) (drops the +1 base term).  
**Source finding:** A-Δ-15-F1 (GAP-08 Mandate-suppression ceiling); C-Δ-F3 (Valorsmark
territorial vulnerability)  
**Mechanism:** New once-per-arc Valorsmark action; modifies PP-N (Treaty) Ob calculation

| | **N** | **E** | **R** | **S** |
|---|---|---|---|---|
| **Top-down** | P — addresses Valorsmark agency loss in 4-faction model; gives one decisive Treaty moment per arc | C — adds a new arc-scoped action (not a modifier on existing); slight design surface increase | P — bounded by once-per-arc | C — players must remember they have this card available |
| **Bottom-up** | P — Ob reduction is canonical Ob modifier | P — once-per-arc is canonical scoping (PA Session precedent) | P — well-defined; Treaty mechanics canonical | P — single-attempt Ob shift |
| **Vertical** | P — same at any player count | P — no scaling | P — multi-arc compatible | P — same load |
| **Diagonal** | P — BG-only | P — no scene cascade | P — no cross-layer | P — no cross-layer |
| **Lateral** | C — only Valorsmark; other factions have no equivalent "one big moment per arc" | P — Treaty already requires target consent (still applies; GAP-05 still open) | C — Treaty consent gap still blocks landing the Treaty even at improved Ob | P — clean |
| **Horizontal** | P — arc-scoped is intrinsically temporal | P — natural arc reset | P — bounded use | P — clear cadence |

**Overall verdict: CONDITIONAL-PASS.** Three `C` notes. The most significant: T-09a
improves Treaty *odds* but does not fix **GAP-05** (Treaty consent — target faction has
no AI rule or PC incentive to agree). **Recommendation: T-09a must be paired with a
Treaty consent resolution (e.g., target faction gains +1 stat of their choice when
agreeing to Valorsmark Treaty) for the tweak to deliver on its win-share equality goal.**

---

### §5.8 T-09b — Varfell Defensive Token on Failed-Spy-Detection

**Proposal:** When Varfell successfully detects an incoming Spy attempt (via PP-N
counter-espionage at Int ≥ 4) AND that Spy attempt failed (Partial or Failure), Varfell
gains 1 Revelation Token on the attacking faction's mat.  
**Source finding:** A-Δ-10-F2 (Hafenmark Diplomat concentrates on Varfell); C-Δ-F4
(Varfell structural decline)  
**Mechanism:** New trigger on counter-espionage; gives Varfell a defensive Token income

| | **N** | **E** | **R** | **S** |
|---|---|---|---|---|
| **Top-down** | P — Varfell's structural Token income compensates the Hafenmark Token pressure | C — adds new trigger; modest design surface increase | P — bounded by attempt rate | C — compound trigger (detect AND failed) needs clear adjudication |
| **Bottom-up** | P — uses existing Spy / Counter-espionage / Token mechanics | C — joint condition (detect AND fail) is new; canonical compound triggers exist (e.g., Cardinal Focus + AP threshold) but each compound adds load | P — joint per-attempt rate computed at 23.2% in Part 3; bounded | P — sequence: roll Spy → roll detect → check both → apply |
| **Vertical** | P — same at any player count | P — no scaling | P — Token economy robust | P — same load |
| **Diagonal** | P — BG-only | P — no scene cascade | P — Token mechanics canonical | P — no cross-layer |
| **Lateral** | P — Varfell only benefits; symmetric to Hafenmark's Diplomat Token | P — other factions can also Spy Varfell (and trigger Varfell Token gain) | C — actively rewards opponents for *trying* and *failing* to Spy Varfell, which may incentivize them to *not* Spy Varfell — counter-strategically self-defeating | C — opponents may simply not Spy Varfell, neutralizing the tweak |
| **Horizontal** | P — multi-season effect | P — Token persists | P — long-arc compatible | P — clear |

**Overall verdict: CONDITIONAL-PASS** with **important lateral `C`**: the tweak only
works if opponents continue to Spy Varfell. If T-09b deters Spying on Varfell, Varfell
gains *neither* the Tokens *nor* the intelligence pressure relief. **Recommendation:
playtest specifically tests opponent behavioral adaptation; if Spying on Varfell drops,
revise to provide Varfell defensive Tokens via a different mechanism (e.g., per-season
1 Token from successful Garrison or successful Mil action).**

---

### §5.9 T-09c — Inquisition Cap (2 Active Inquisitors Max)

**Proposal:** No more than 2 active Inquisitors may be deployed peninsula-wide
simultaneously. Deployment of a 3rd Inquisitor requires recalling one of the existing
two as a free action that season.  
**Source finding:** C-Δ-F1 (Church Inquisition trajectory dominates 4-faction); per
Part 3 §6.2 the **largest single equality lever**  
**Mechanism:** Caps Church Active Inquisition deployment count

| | **N** | **E** | **R** | **S** |
|---|---|---|---|---|
| **Top-down** | P — directly limits Church's dominant mid-game vector to bring win-share into ±5pp band | P — cap mechanic is canonical (PP-N action-limit pattern) | P — fixed bound; well-defined | P — single rule: "max 2 Inquisitors" |
| **Bottom-up** | P — counts existing Inquisitor tokens on map | P — physical token-count check | P — fully robust; no edge case | P — count is visible on board |
| **Vertical** | P — same at any player count | P — no scaling | P — multi-arc compatible | P — same load |
| **Diagonal** | C — Inquisitor presence affects scene-layer interrogation probes; capping may reduce scene-layer narrative threads | P — no new mechanism | P — scene layer adapts to lower Inquisitor density | C — fewer Inquisitors means fewer scene-layer Inquisitor-driven encounters for players |
| **Lateral** | C — heavy Church nerf; Church player may feel their core identity throttled | P — Church retains Inquisitor as canonical tool, just rate-limited | P — Church can still use Inquisitor strategically | C — Church player perception management needed |
| **Horizontal** | P — cap is multi-season aware (max 2 at any time, recall is an action) | P — recall mechanic canonical | P — long-arc compatible | C — players must remember the cap when planning future Active Inquisition |

**Overall verdict: CONDITIONAL-PASS.** Three `C` notes — diagonal (scene-layer narrative
density), lateral (Church identity feel), and horizontal (recall mechanism's UX). The cap
is the **single most impactful tweak for equality** per Part 3 §6.2. **Recommendation:
prototype with this cap immediately; the scene-layer narrative density concern requires
designer attention but is the right trade for win-share equality. Church flavor preserved
by adding "Senior Inquisitor" archetype to the 2-slot cap (each Inquisitor named, with
backstory)** to reinforce identity through depth rather than breadth.

---

## §6 Set-Level Audit

Beyond per-tweak audit, the set as a whole must hold:

### §6.1 No internal conflicts

| Tweak A | Tweak B | Interaction | Verdict |
|---------|---------|-------------|---------|
| T-01a | T-01c | Both Valorsmark; together create stat-stable but defensively narrower Valorsmark | C — paired effect intended; net = Valorsmark trades dominance for vulnerability balance |
| T-02a | T-09c | T-09c caps Inquisitor density; T-02a relaxes Inquisitor lock-out → composable | P — multiplicative benefit to Varfell |
| T-09b | T-01c | T-01c opens Valorsmark to Spy; T-09b rewards Varfell for being Spied | P — both contribute to Spy meta becoming an active game |
| T-09a | T-03c | Both reduce stronger-faction's dominance; complementary | P — independent |
| T-02c | T-02a | Both Varfell Counter-Narrative buffs | C — combined may over-empower Varfell; verify in playtest |

**Set-level conflict verdict: PASS with note** — T-02a + T-02c combined is the only
identified over-empowerment risk; otherwise the set composes cleanly.

### §6.2 Set-level NERS

| Axis | Verdict | Rationale |
|------|---------|-----------|
| **N (Necessary)** | P | 7 of 9 tweaks address P1 findings directly; 2 (T-01c, T-04a) are supporting |
| **E (Elegant)** | C | 3 tweaks introduce new constructs (T-09a once-per-arc action, T-09b compound trigger, T-09c cap). Design surface increases moderately |
| **R (Robust)** | C | Set is robust IF GAP-05 (Treaty consent) and GAP-01 (AP reset) are independently resolved; otherwise T-09a partially blocked and Inquisitor mechanics ambiguous |
| **S (Smooth)** | C | Combined player rule load increases: track Charters, track first-attempt-per-Inquisitor-pair, compound trigger for T-09b, recall cap for T-09c. Faction mats should be updated to surface these |

**Set-level overall: CONDITIONAL-PASS** — all 4 axes pass at the set level, with
`C` flags on Elegant (design surface growth), Robust (depends on resolving GAP-01/05),
and Smooth (player load).

### §6.3 Minimum-viable subset

Per Part 3 §6.2 ranking, the **minimum-viable subset** for 25% ±5pp equality is:

- **T-09c** (Inquisition cap 2) — single largest equality lever
- **T-02a** (Inquisitor familiarity) — Varfell relief
- **T-09b** (Varfell defensive Token) — Varfell agency

NERS verdict on the 3-tweak minimum subset:

| Axis | Subset verdict |
|------|----------------|
| **N** | P — addresses C-Δ-F1, C-Δ-F4, and A-Δ-10-F2 directly |
| **E** | C — T-09c cap and T-09b compound trigger both new constructs |
| **R** | P — T-09c doesn't depend on GAPs; T-09b conditional on opponent Spy behavior; T-02a self-contained |
| **S** | P — only 3 rules to internalize; manageable |

**3-tweak subset: PASS** with one `C` on Elegant. The minimum-viable subset is the
**recommended initial playtest configuration**. The remaining 6 tweaks are added in
subsequent playtest waves as needed.

---

## §7 NERS Findings — Part 4

### N1 [SET PASSES SET-LEVEL NERS] P1
The full 9-tweak set passes all 4 NERS axes at the set level with conditional flags
on E (design surface) and S (player load). The 3-tweak minimum-viable subset passes
more cleanly. **Recommendation: stage rollout — start with 3-tweak subset, expand
based on playtest.**

### N2 [TREATY CONSENT GAP BLOCKS T-09a] P1
T-09a improves Treaty Ob from 3 to 2 against Church, lifting Success+ from 38% to 60% —
but **only if the target faction agrees**. GAP-05 (no NPC AI rule for Treaty consent;
no PC incentive) remains unresolved. **T-09a is conditional on resolving GAP-05.**
Without GAP-05 resolution, T-09a's intended win-share equality lift is unrealized.

### N3 [T-09b BEHAVIORAL DEPENDENCE] P1
T-09b only works if opponents continue Spying Varfell. Game-theoretically, opponents
may stop Spying Varfell once the defensive Token is known — neutralizing the tweak.
**Playtest test: does opposing Spy rate on Varfell drop after T-09b becomes visible?**
If yes, T-09b needs revision toward an unconditional defensive Token income.

### N4 [T-02a + T-02c COMPOSITION] P2
Combined Varfell Counter-Narrative buffs (familiarity + Overwhelming-relocates) may
over-empower Varfell beyond the 25% ±5pp target. **Playtest test: 3-tweak subset
(includes T-02a but not T-02c) vs full set.** Compare Varfell win-share.

### N5 [SCENE-LAYER NARRATIVE DENSITY UNDER T-09c] P2
T-09c caps Inquisitor count at 2 peninsula-wide. Fewer Inquisitors → fewer scene-layer
Inquisitor-driven encounters → fewer scene-layer narrative threads for players investigating
Church investigations. **Compensate by promoting "Senior Inquisitor" archetype with
named NPCs, denser backstory, and arc-driving questions per Inquisitor.** Quality over
quantity.

### N6 [CHURCH IDENTITY PRESERVATION UNDER T-09c] P2
Capping Inquisitor density is a heavy Church nerf at the resource level. Compensate
by **deepening Church's other vectors**: Excommunication is mid-tier (per Part 3 §2),
CI 60 Seizure remains powerful, Cardinal Focus pipeline robust. The 4 fewer expected
Inquisitor deployments per arc are replaced by deeper Inquisitor engagement per deployment.

### N7 [DESIGN SURFACE GROWTH] P2
T-09a (new once-per-arc action), T-09b (new compound trigger), T-09c (new cap rule)
each add design surface. Set-level rule load grows. **Mitigation: update faction mats
to surface these — Valorsmark mat shows "Once per arc: Influence Surge"; Varfell mat
shows the counter-espionage trigger; Church mat shows the Inquisitor cap.** Distributes
load to faction-owned UX.

---

## §8 Set Verdict — Part 4

**Full set (9 tweaks): CONDITIONAL-PASS**

| Tweak | Verdict | Conditions |
|-------|---------|------------|
| T-01a | PASS | Track Charter count visibly |
| T-01c | CONDITIONAL-PASS | Apply only alongside T-09a |
| T-02a | PASS | Mark Inquisitor first-attempt status |
| T-02c | PASS | Add flavor language for Inquisitor relocation |
| T-03c | PASS | Identity-preserving asymmetric — document explicitly |
| T-04a | CONDITIONAL-PASS | Defer until 8+-season playtest confirms need |
| T-09a | CONDITIONAL-PASS | Requires GAP-05 (Treaty consent) resolution |
| T-09b | CONDITIONAL-PASS | Playtest opponent Spy rate; revise if Spy avoidance emerges |
| T-09c | CONDITIONAL-PASS | Compensate with Senior Inquisitor archetype + named NPC |

**Minimum-viable subset (T-09c + T-02a + T-09b): PASS**

**Open items propagated to Part 5 (Throughline Audit):**

- T-09a, T-09b, T-09c are new tweaks not previously throughline-vetted; Part 5 verifies
  throughline coverage and meta-throughline compliance
- All tweaks need throughline mapping per `references/throughline_registry.md`
- Orphan-mechanic check per `references/throughlines_meta.md` PP-674 vetting protocol

**Open items for editorial / canon work (outside Parts 1–5 scope):**

- **GAP-05** (Valorsmark Treaty consent): blocks T-09a; 4 sims flagging
- **GAP-01** (Phase 5 AP reset): may affect Inquisitor mechanics under T-09c
- **GAP-08** (Mandate-suppression ceiling): unresolved; 4 sims flagging
- **PI Crisis tuning** (Y1 too early): not in tweak set; separate design question
- **Token max-per-faction-mat rule** (PP-517 cited but not freshly verified)
- **Inquisitor relocation rules** (Active Inquisition deployment + T-02c)

---

## §9 Cross-Audit Notes

### §9.1 Audit method limits

This audit is paper-only. NERS-pass on a tweak does not guarantee playtest success.
The robustness axis (R) tests against *modeled* variance, not actual player behavior
under fatigue, social dynamics, or rule-mis-recall. Smooth (S) is the most-likely-to-be-wrong
axis at the table.

### §9.2 What this audit cannot verify

- **Player-fun trade-off**: NERS doesn't measure fun. Some `P`-rated tweaks (T-01a
  Charter dim. returns) may feel "obvious nerf" to Valorsmark player.
- **Story / fiction coherence**: NERS doesn't fully verify whether the tweak's mechanism
  *feels* like the faction's identity. Partial via lateral axis.
- **Long-campaign emergent behavior**: 12+ season campaigns may surface effects not visible
  in 6-season simulation.
- **GM workload**: NERS doesn't measure GM rule-arbitration load. New rules (especially
  T-09b compound trigger) add GM adjudication burden.

### §9.3 Confidence assessment

| Tweak | Audit confidence | Reasoning |
|-------|------------------|-----------|
| T-01a, T-02a, T-03c | **High** | Clean mechanism, existing canonical operators |
| T-01c, T-02c | **High** | Narrow scope changes |
| T-04a | **Medium** | Long-arc effects uncertain; threshold change is loose |
| T-09a | **Medium** | New action surface + blocked by GAP-05 |
| T-09b | **Low-Medium** | Behavioral dependence creates uncertain effect |
| T-09c | **High** | Single number cap; bounded; clean |

**Overall audit confidence: Medium-High.** The 3-tweak minimum-viable subset has
Medium-High to High confidence. The full 9-tweak set's Low-Medium confidence cells
(T-09b) are the playtest priority.

---

## §10 Recommendations

1. **Prototype the 3-tweak minimum-viable subset first** (T-09c + T-02a + T-09b).
   Six-session playtest; measure win-share variance.

2. **Resolve GAP-05** (Treaty consent) before promoting T-09a from CONDITIONAL to PASS.

3. **Update faction mats** to surface new tweak rules per §7 N7.

4. **Add Senior Inquisitor archetype** with named NPCs and arc-driving questions if
   T-09c is adopted; preserves Church narrative density.

5. **Run T-09b behavioral test** specifically: monitor opponent Spy rates on Varfell
   across multiple playtest sessions. Revise if Spy avoidance pattern emerges.

6. **Document T-03c rationale** as identity-preserving asymmetric: Hafenmark is the
   soft-power faction; the Wealth cost preserves identity while throttling rate.

7. **Defer T-04a** until 8+-season campaign playtest data exists.

8. **Defer T-02b and T-04b** (originally P3) — out of scope for this audit pass.

---

## §11 Open Items — Part 4

- Set-level NERS audit could include a "Bloat" check per precedent (`22_NERS_and_bloat_assessment.md`
  used this); deferred to Part 5 throughline audit which serves similar purpose
- Per-tweak interaction matrix could expand beyond §6.1 — defer until playtest data
- T-09a's "once per arc" trigger needs canonical arc-boundary definition; check
  `designs/architecture/campaign_architecture_v30.md` for definition
- T-09c cap mechanics: recall via Action vs Cardinal Focus vs free-on-deployment;
  unspecified; pick canonical option

---

*Session: ners-audit · 2026-05-13 · Part 4/5 · Author: simulator under Jordan*
