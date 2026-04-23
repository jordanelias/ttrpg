# SOLMUND CULTURAL GUIDE — N Check + Resolution Check

## Status: AUDIT — companion to designs/world/solmund_cultural_guide_consolidated.md
## Method: Every numerical/mechanical reference verified against canon sources. Resolution tested at personal, settlement, territory, and peninsula scales.

---

# N CHECK — Numerical Fidelity

## Values Verified ✓

| Value | Document Ref | Canon Source | Match |
|---|---|---|---|
| SA starting: Church 0, Crown 0, Hafenmark 1, Varfell 2, RM 3 | §19, §20.3 | southernmost_v30 §6.2 | ✓ |
| SA scale 0-7 (0-10 with research infrastructure) | §24 | southernmost_v30 §6.2 | ✓ |
| Mending Ob: 6 Entrenched, 7 Catastrophic, 8+ Locked Zone | §20.1, §20.2 | threadwork_v30 Mending table | ✓ |
| Mending TS min: 50+ base, 70+ at Ob 6+ | Implicit | threadwork_v30 Mending table | ✓ |
| Visibility: TS 0-9 nothing, 10-29 unease, 30-49 senses operation, 50-69 type+target, 70+ full | §12, §20.1 | threadwork_v30 §2.3 | ✓ |
| Certainty range 1-6+ | §18 | character_histories_v30 | ✓ |
| RWCE Proximity radius: Ob 6 local, Ob 7 +Prox 1, Ob 8+ +Prox 2 | §20.2 | geography_v30 node distances | ✓ |
| TD 3 effect: Church loses PI → Hafenmark PI +1 | §22.2 | params/bg/tracks.md | ✓ |
| Ob 7-8 "near-impossible solo (~40-58%)" | §20.1 | threadwork_v30 Mending design note | ✓ |
| Physical effects visible to all | §20.1 | threadwork_v30 §2.3 | ✓ |
| Mending Coherence cost: 0 | Not stated | threadwork_v30 Mending table | ✓ (not contradicted) |
| Einhir framework requirement at Ob 7+ | §20.1 | threadwork_v30 Mending table | ✓ |

## Failures

### N-1: Seam Text Mechanism — Wrong Canon Reference

**Document says (§12):** Seam Text second reading "gated by TS via the existing visibility tables (threadwork_v30 §2.3)."

**Problem:** The visibility table governs perception of ACTIVE thread operations in progress. TS 30-49 = "Senses an operation in the scene; general direction identifiable." A Seam Text is not an active operation. It is a written description of a historical event. No operation is occurring when someone reads scripture. The visibility table does not apply.

**Correct reference:** P-08 (epistemological barrier, §10.1-10.2). "Non-sensitive practitioners who learn the same facts intellectually do not continually forget them. Rather, they cannot access the facticity of the facts. The knowledge is propositionally available — they can recite what they have been told — but they cannot epistemologically reconcile it."

**What this means:** A non-sensitive reader can read the Seam Text passage in full. The words are not hidden. The reader cannot recognise that the description is describing threadwork because they have no experiential referent. They read "the water returned from below... as if the ground remembered holding water" and parse it as vivid devotional language — a miracle account. A TS 30+ reader has seen threads. The same words suddenly cohere with experience. "The ground remembered" — they have perceived configurations reasserting prior states. "Returned from below" — they have felt the direction of Mending operations. The second reading is not revealed content. It is the same content, comprehended differently.

**Mechanical consequence for Godot:** The Seam Text is NOT hidden text revealed at a TS threshold. It is the same text with an added annotation layer — a character-internal recognition response. Implementation: when TS ≥ 30, the player character's reaction is displayed alongside the text ("Wait — I've seen this. This isn't describing a miracle. This is describing what I felt when I touched the thread."). The scripture object itself does not change. The player's relationship to it changes. This is P-08 operating in reverse: instead of knowledge being epistemically inert, previously-inert knowledge suddenly becomes active when the reader gains the experiential framework.

### N-2: Miracle Investigation Ob — Unscaled

**Document says (§22.1):** Miracle Investigation: Mandate vs Ob 2 (flat).

**Problem:** Other Church Consul actions scale:
- Piety Spread: Mandate vs Ob = floor(controlling faction Mandate / 2) + 1 + Fort Level
- Active Inquisition: Mandate vs Ob = floor(territory Stability / 2) + 1

Flat Ob 2 is inconsistent. A Miracle Investigation in a territory controlled by a faction with high SA should be harder — the controlling faction already knows more about the Southernmost than the Church does, making the Church's investigation less likely to produce coherent results.

**Proposed fix:** Mandate vs Ob = floor(target territory controller's SA / 2) + 1. At SA 0 (neutral territory / uncontrolled): Ob 1. At SA 2 (Varfell): Ob 2. At SA 4: Ob 3. The more the controlling faction already knows, the harder it is for the Church to impose its miracle framing — because the local population has access to competing explanations.

### N-3: RDT Prerequisites Omitted

**Document says (§22.2):** "If Hafenmark controls a territory where RWCE fired AND Church has presence: Baralta can argue the Church's passive theology was proven inadequate."

**Problem:** This implies RWCE alone triggers RDT advancement. Canon (params/bg/tracks.md) requires ALL of:
- Hafenmark controls territory where Church has Parish/Cathedral
- Hafenmark M ≥ 3
- PI ≥ 4

RWCE provides political ammunition — it makes the argument for Reformed Settlement more compelling. It does not bypass the M ≥ 3 and PI ≥ 4 prerequisites. A Hafenmark without sufficient Military or Parliamentary Influence cannot advance RDT regardless of what happens in the Southernmost.

**Fix:** Add: "RWCE strengthens the political case for Reformed Settlement but does not bypass existing RDT advancement prerequisites (Hafenmark M ≥ 3, PI ≥ 4, Church presence in controlled territory). All conditions must be met."

---

# RESOLUTION CHECK — By Scale

## Personal Scale

| Element | How It Resolves | Status |
|---|---|---|
| **Voice register selection** | Certainty × TS → determines which register governs NPC dialogue and discoverable text. Certainty 4 + TS 0 = Di Cicco inhabitation. Certainty 5 + TS 30 = Hopkins with John of the Cross undertones. | ✓ Clean — but only governs text generation/NPC dialogue, not player mechanical interaction |
| **Seam Text recognition** | Player character's TS crosses 30 → previously-discovered scripture triggers recognition response | ✓ once N-1 is fixed |
| **Conviction pressure from RWCE** | §25 mentions "witnessing RWCE may trigger Conviction pressure for individual characters" | **GAP — no mechanic.** Proposal: character witnesses RWCE effects → Certainty check. Roll Cognition vs Ob = current Certainty. Success: Certainty unchanged (framework holds). Partial: Certainty −1 (framework strained). Failure: Certainty −2 (framework shaken). This fires once per character per RWCE. Characters with TS perceive more and face higher Conviction pressure. |
| **Character formation hooks** | Origins 1D (Einhir descendant), 1E (Himmelenger), Formation 2A (Church School), 2G (Monastic Seclusion) all correctly referenced as producing characters with specific voice register defaults | ✓ |
| **Baralta prophylaxis cracking** | §21.4: "weakened prophylaxis... over generations" | **GAP — timescale mismatch.** Game spans ~5 years. "Over generations" is outside the game timeframe. In-game effect: Baralta's territories do NOT produce higher TS during the game. The effect is narrative/thematic — it explains WHY Baralta's theology is historically progressive, positioning the player to understand the long-term consequence of who holds power. If a mechanical effect is desired: territories under Baralta's direct governance (Hafenmark-controlled) could get −1 to the base Certainty floor for newborn NPCs, reflecting a *beginning* of the shift. But this is speculative and not grounded in existing mechanics. |

## Settlement Scale

| Element | How It Resolves | Status |
|---|---|---|
| **POI Seam Texts** | Remnant-type POI in Church territories. Discovered via Survey action (fieldwork_v30 §8.1). Placed in T2 Kronmark, T9 Himmelenger, T14 Ehrenfeld. | ✓ |
| **Settlement flavour text** | §27: "calibrated to territory Certainty" | **GAP — no settlement-level Certainty defined.** Canon tracks Certainty per character, not per settlement or territory. Proposal: settlement flavour text keyed to the territory's controlling faction's starting Certainty baseline (Church territories default 5, Varfell territories default 3-4, Crown heartland 4, Hafenmark 4, Askeheim N/A). This is a content-authoring guideline, not a tracked variable. |
| **Settlement Accord interaction** | Not addressed | **GAP.** If RWCE improves local conditions — blight recedes, water returns, structures stabilise — population sentiment should improve. Proposal: territories within RWCE radius gain +1 Accord at next Accounting (one-time). Represents population response to tangible improvement in living conditions, regardless of cause attribution. |
| **Settlement adjacency (PP-666)** | Not referenced | ⚠ Settlement adjacency governs how effects propagate between settlements within a territory. If RWCE affects a territory, does it affect all settlements within that territory, or only settlements adjacent to the Mending site? Recommend: RWCE affects the entire territory (the effects are rendered-world, not settlement-specific). Settlement adjacency matters only if future design requires sub-territory RWCE granularity. |

## Territory Scale

| Element | How It Resolves | Status |
|---|---|---|
| **RWCE by territory and Proximity** | Ob 6: mended territory. Ob 7: +Prox 1 (T6 Stillhelm, T13 Oastad from T15). Ob 8+: +Prox 2 (also T5 Feldmark, T12 Sigurdshelm). | ✓ Maps cleanly to geography_v30 node distances |
| **SA increment by faction presence** | Controls territory (Crown/Hafenmark), PT ≥ 1 (Church), Trade Route token (Hafenmark), automatic (Varfell) | ✓ |
| **PT change from Miracle Investigation** | §22.1: PT +1 in investigated territory on Success/Overwhelming | ✓ |
| **Territory Stability interaction** | Not addressed | **GAP.** RWCE improves physical conditions — Shifting Objects cease, Gaps close, anomalous phenomena end. The RS radiation table (params/bg/clocks.md) governs these effects by RS band × Proximity. When RS improves locally, affected territories should experience fewer negative modifiers. But RS is a GLOBAL track, not per-territory. The RWCE improves conditions locally while the global RS may not have changed. This creates a discrepancy: local conditions improve, but the RS-band lookup still applies the old band's penalties. Proposal: territories within RWCE radius receive a −1 modifier to their Proximity Rating for RS-band lookup purposes, effective until next Accounting. This represents the local Mending creating a pocket of stability within the broader RS gradient. One-time per Mending event. Resets if RS band transitions globally. |
| **Fractional province ownership (PP-666)** | Not referenced | ⚠ If Church establishes governance via Ecclesiastical Appointment in a territory where RWCE fired, the settlement controller differs from the territory Seat holder, triggering province fractionalisation. The Southernmost engagement could create multi-faction provinces. Note, do not design for — this is an emergent consequence of existing systems interacting with the new trigger. |

## Peninsula Scale

| Element | How It Resolves | Status |
|---|---|---|
| **RS track → RWCE** | Mending improves RS locally. The RWCE is a consequence of RS improvement, not a separate system. | ✓ But note: Mending at Ob 6-8 affects RS per the Mending degree table. Overwhelming: RS +2. Success: RS +1. This is the existing mechanic. RWCE fires on top of this, adding faction awareness to the existing RS change. |
| **CI track → Assert/Accommodate** | Church Assert: CI +1. Church Accommodate: CI −1. Both are Decision Event outcomes. | ✓ |
| **RDT/TD → Baralta challenge** | Routes through existing advancement conditions. RWCE provides ammunition, not bypass. | ✓ once N-3 is fixed |
| **IP tradeoff** | §25: "every season south = a season unavailable against Altonia" | **GAP — not mechanised.** Garrison absence in northern territories does not automatically increment IP. IP advances on its own schedule (params/bg/clocks.md). The tradeoff is strategic, not mechanical: if Crown/Hafenmark sends military escorts for Southernmost expeditions, those units are not available for border defence. If Altonian Vanguard is deployed (IP 75+), those units are needed north. The tradeoff is real but operates through player resource allocation, not an automatic trigger. No mechanical change needed — the tradeoff is emergent from existing unit positioning rules. |
| **AER interaction** | Not addressed | **GAP.** AER advancement requires Temperance Cardinal focus (1 declaration/year per params/bg/tracks.md). AER decays −1 at year-end if Temperance focus was not maintained. If Church commits to Miracle Investigation, does this compete with AER maintenance? Structurally yes: Miracle Investigation is a Consul Outward action, and the Church has limited action slots per season. If the Church uses its Consul action for Miracle Investigation, it cannot use it for other Consul actions that season. But AER advancement is a Phase 1 declaration by Cardinal of Temperance, not a Consul action. There is NO mechanical conflict between Miracle Investigation and AER maintenance. They use different action slots. The tradeoff is narrative (Church attention divided) and potentially affects which Cardinal the Church focuses, but not mechanically exclusive. **Resolution: no AER-specific mechanic needed.** The tension is real but operates through Cardinal Focus choices (focusing Temperance vs. other Cardinals), not through action-slot competition. |
| **Peninsular Strain** | Not addressed | ⚠ Strain increments from battles and territorial disruption. RWCE is stabilisation — the opposite. Should RWCE decrement Strain? Recommend: no. Strain measures the cumulative damage of inter-faction conflict. RWCE measures the cumulative repair of Calamity damage. These are tracking different things. Conflating them would dilute both. Strain should track what it tracks. RS tracks what RWCE affects. |

---

# SUMMARY

## Must Fix (3)

| # | Issue | Fix |
|---|---|---|
| N-1 | Seam Text cites visibility table; should cite P-08 | Replace visibility-gate with comprehension-gate. Same text, annotation layer at TS 30+. Implement as character-internal recognition, not hidden content. |
| N-2 | Miracle Investigation Ob 2 flat; should scale | Mandate vs Ob = floor(target controller SA / 2) + 1. Higher SA = harder to impose miracle framing. |
| N-3 | RDT prerequisites omitted | Add: "RWCE does not bypass existing RDT prerequisites (M ≥ 3, PI ≥ 4, Church presence)." |

## Gaps to Address (5)

| # | Gap | Proposal |
|---|---|---|
| G-1 | Conviction pressure from RWCE unspecified | Certainty check: Cognition vs Ob = current Certainty. Once per character per RWCE. |
| G-2 | Settlement flavour text — no settlement Certainty | Content-authoring guideline keyed to controlling faction's Certainty baseline, not a tracked variable. |
| G-3 | Settlement Accord interaction with RWCE | +1 Accord at next Accounting for territories in RWCE radius. One-time. |
| G-4 | Territory Stability / RS-band local improvement | −1 Proximity Rating modifier for RS-band lookup in RWCE-affected territories until next Accounting. |
| G-5 | Mending TS minimums never explicitly stated | Add to §20.1: "Mending requires TS 50+. Ob 6+ requires TS 70+ (threadwork_v30 Mending table)." |

## Resolved Without Change (3)

| # | Concern | Resolution |
|---|---|---|
| R-1 | IP tradeoff not mechanised | Emergent from unit positioning. No automatic trigger needed. |
| R-2 | AER interaction | Miracle Investigation and AER maintenance use different action slots. No mechanical conflict. Tension is narrative. |
| R-3 | Peninsular Strain interaction | Strain and RS track different things. Do not conflate. |

## Warnings — Note Only (3)

| # | Concern | Note |
|---|---|---|
| W-1 | Baralta prophylaxis cracking outside game timeframe | Narrative/thematic positioning, not in-game mechanical effect. |
| W-2 | Settlement adjacency (PP-666) not referenced | RWCE affects entire territory. Sub-territory granularity not needed unless future design requires it. |
| W-3 | Fractional province ownership | Emergent consequence if Church governs settlements in multi-faction territories. Do not design for — let existing systems interact. |
