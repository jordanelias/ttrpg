<!-- [PROVISIONAL: 2026-04-28 session — extended stress tests against doc 12] -->
<!-- STATUS: PROVISIONAL — new stress testing against 12_development_specification.md -->
<!-- POSITION: designs/audit/2026-04-28-political-dynamics-session/13_stress_tests_extended.md -->

# Extended Stress Testing: Political Dynamics System (Against doc 12)

**Scope:** New tests against `12_development_specification.md` (current source of truth). Doc 10 covered cascade depth, simultaneous crisis, long-run temporal, Knowledge propagation, adversarial Insinuate, simultaneous Scars, weight normalization, collapsed faction friction, affect_axis discrete events, deliberate fragmentation, dampened drift bounds. All those patches are integrated into doc 12. These tests probe vectors not addressed in doc 10.

**Method:** Each test defines a concrete game state, traces the system's behavior through spec-defined procedures, and identifies issues (or confirms clean behavior). No speculation flagged as fact; gaps clearly identified.

---

## ST-13: Memory Cap Overflow — No Clear Lowest-Salience Candidate

**Probe:** An NPC has 10 Memories all at salience 3. A high-salience event (salience 5) fires. The Memory cap is 10; the replacement rule is "drop the lowest-salience existing Memory."

**Trace:**
- New Memory (salience 5) would exceed cap.
- All existing Memories at salience 3. No unique lowest-salience candidate.
- Replacement rule as written: "lowest-salience existing Memory is dropped or merged."
- **Tie resolution is unspecified.** The spec provides the merge fallback ("collapses similar Memories") but neither the selection algorithm when all saliences are equal nor the merge trigger conditions.
- If the merge path fires: what is the merge algorithm? "Another disappointment from the Crown" implies collapsing semantically similar Memories. But semantic similarity is a content-matching problem, not a salience-matching problem. The spec provides one illustrative example but no general rule.

**Issue (ST-13-A):** Memory replacement has no tie-breaking rule for equal-salience candidates. Implementation will be forced to make an arbitrary choice (FIFO, random, domain-match) with behavioral consequences for long-run NPC characterization. An NPC with many equal-salience Memories will lose Memories in an implementation-defined order — which could mean foundational Memories that never got referenced are silently dropped while newer ones accumulate.

**Issue (ST-13-B):** Memory merge trigger conditions unspecified. The spec implies merge fires for "similar" Memories but does not define the similarity threshold (same event_type tag? same participant? same affect direction?). Without a rule, the merge path cannot be implemented deterministically.

**Patch ST-13:** 
- Tie-breaking: when multiple Memories share the lowest salience, apply secondary sort by `timestamp` (oldest first) — drop the oldest low-salience Memory. This is historically coherent (older, unreinforced memories fade) and deterministic.
- Merge rule: merge fires when the incoming Memory's `event_type` matches an existing Memory's `event_type` AND the same `participants` set overlaps by ≥50%. When merge fires instead of drop: the merged Memory retains the higher `salience`, increments `reference_count` by 1, and collapses `detail` text. Merge takes priority over drop when a valid merge candidate exists.

---

## ST-14: Concern Cap — All Three Slots Full, None Near Expiry

**Probe:** Active NPC has 3 Concerns, all at salience 4, TTL 3 seasons remaining each. A major event fires generating a new Concern at salience 5.

**Trace:**
- Spec (§6.2, Procedure B Generation): "if len(npc.concerns) > 3: drop_lowest_salience_concern(npc)"
- The condition triggers: drop_lowest_salience_concern evaluates the 3 existing Concerns (all salience 4).
- The new Concern (salience 5) would be added first, then the lowest of the 4 is dropped.
- With all 3 existing at salience 4 and new at 5: the new Concern is retained, and one of the three salience-4 Concerns is dropped.
- **Tie applies again** — which salience-4 Concern drops? Same unspecified tie-breaking as ST-13.

**Issue (ST-14-A):** Same tie-breaking gap as ST-13-A. The Concern dropping algorithm is identical to Memory dropping in structural terms. Without a defined tie-break, an arbitrary Concern is dropped — potentially the most plot-relevant one.

**Additional issue (ST-14-B):** The Concern cap enforcement happens AFTER appending the new Concern. This means momentarily there are 4 active Concerns before the drop. The spec says "if len(npc.concerns) > 3: drop..." which is correct — but if two events fire simultaneously in the same Accounting pass, two new Concerns could be appended before the cap check runs, briefly creating 5. The ordering within the for-each-event loop needs to enforce the cap check after each append, not after the full loop.

**Patch ST-14:**
- Tie-breaking for Concerns: when multiple Concerns share the lowest salience, drop the one with the lowest TTL remaining (most nearly expired anyway). Secondary: if TTL also ties, drop by oldest source_event timestamp.
- Cap enforcement: move the cap check inside the per-event loop (after each Concern is appended, immediately enforce). This prevents transient 4+ Concern states during simultaneous event processing.

---

## ST-15: Opinion Formation at Zero — First Contact With No Memory

**Probe:** Almud (Crown, Order/Virtue-Ethics) meets Baralta (Hafenmark, Precedent/Categorical-Imperative) for the first time. No prior relationship. No shared Memories. The interaction fires in Procedure E.

**Trace:**
- Procedure D runs Opinion Drift against existing Memories. But Almud has no Opinion of Baralta yet (first contact).
- **Opinion initialization:** The spec defines Opinion structure (§2.5) but does not define initial values when an Opinion is created.
- Procedure D's drift formula: `drift = base_drift × (1 - abs(opinion.affect_axis) / 3) × conviction_alignment_multiplier`. If opinion.affect_axis starts at 0, the dampening factor is (1 - 0/3) = 1.0 — maximum drift rate.
- Conviction alignment multiplier: Almud (Order) vs Baralta (Precedent) — the multiplier value for Order↔Precedent pairing is unspecified in the doc (only Procedure E specifies "shared primary Conviction: ±0.3" — they don't share primary Conviction).
- **The spec specifies drift values for three cases:** same faction/same Conviction (±0.3), same faction/no shared Conviction (±0.1), different Conviction (±0.05). Almud and Baralta are in different factions with different Convictions → drift ±0.05.
- After one interaction: Almud's opinion of Baralta shifts ±0.05. But the Opinion didn't exist before the interaction. **When does Opinion initialization happen?**

**Issue (ST-15-A):** Opinion initialization is unspecified. The spec states "~5-10 per Active NPC" starting Opinions (§10: "200 recommended, inner-circle pairs only; let others form dynamically"), implying some Opinions are authored and some form dynamically — but "form dynamically" has no mechanism specified. When Procedure E fires for a pair with no existing Opinion, does it create one at affect_axis=0? Or does the first interaction produce a Memory but no Opinion until some threshold?

**Issue (ST-15-B):** Procedure E iterates over `npc.opinions` for drift (Procedure D) and generates interactions (Procedure E). If no Opinion exists yet, Procedure D skips. But Procedure E's generated interaction still produces drift — applied where? If no Opinion object to write to, the drift is lost.

**Patch ST-15:**
- Opinion initialization on first interaction: when Procedure E generates an interaction between NPCs with no existing Opinion, the engine creates an Opinion entry at affect_axis=0, confidence=1 (weak, newly formed). Subsequent drift is applied normally.
- Specify initialization rule in §2.5: "Opinions not authored at game-start are initialized at affect_axis=0, confidence=1 on first Procedure E interaction or first Memory-generating encounter."

---

## ST-16: Memory Salience Floor Lock — Permanent Salience 5

**Probe:** An NPC has a founding-relationship Memory (the event where they met their Knot partner, salience 5, 20 seasons ago). The Memory has been referenced in Opinion drift, Concern resolution, and armature seeking-tag matching repeatedly. reference_count = 12. Salience floor = min(reference_count × 0.5, 5) = min(6, 5) = 5.

**Trace:**
- Normal salience decay: -1 per 4 seasons. After 20 seasons: -5 decay applied → salience would be 0.
- Salience floor at 5 → effective salience stays 5. Memory is permanently at max salience.
- This Memory now permanently contributes to: Concern resolution (always the highest-match candidate), Opinion drift evidence, armature seeking-tag matching.
- **The Memory is 20 seasons old.** Its `detail` describes events from early game. It is the highest-salience Memory the NPC has, permanently, regardless of what has happened since.

**Issue (ST-16-A):** The Memory salience floor mechanism as designed produces permanent salience-5 Memories for any founding relationship that is regularly referenced. This is intentional for that relationship — but it creates a systematic bias in Concern resolution. Whenever the NPC forms a Concern related to a domain also covered by a founding Memory, the founding Memory will be selected as the resolution candidate (highest salience). An NPC will persistently interpret new events through 20-season-old lenses if those lenses were frequently referenced.

This is arguably a feature (persistent interpretive path dependency). But it becomes an issue in one specific case: **wrong founding Memory interpretation.** If the founding Memory's `affect` was -2 (negative early relationship) and current reality is +3 (reconciled), the floor keeps the old negative Memory at max salience — potentially blocking Opinion drift from ever fully recovering the relationship, because the negative Memory keeps being referenced in Concern resolution and confidence dampening.

**Issue (ST-16-B):** The floor formula `reference_count × 0.5` has no ceiling on `reference_count`. An NPC who has lived for 30 seasons and referenced a Memory 20 times has floor = min(10, 5) = 5. Floor is already capped at 5, so this works. But the reference_count itself grows unboundedly — at reference_count 100, the display is "this Memory has been consulted 100 times" which is fine for data but the floor calculation still just returns 5. No issue with the formula, but the unbounded reference_count is wasteful storage. Minor.

**Patch ST-16:** No spec change required for the formula (it's capped correctly at 5). However, add a clarifying note in §2.6: "Salience floor caps at 5 regardless of reference_count. Referenced founding Memories may achieve permanent salience-5 status. This is intentional for relationship characterization — NPCs interpret new events partly through the lens of their most deeply reinforced experiences. Designers should author founding Memories carefully: a negative founding Memory that reaches permanent salience will persistently pull Opinion drift calculations in its direction even after relationship recovery."

Flag for authoring: the starting Memory set for Knot partners should be authored to match intended relationship arc entry points.

---

## ST-17: Path A + Path B Simultaneous on Same Belief

**Probe:** Season 12. Himlensendt holds a calcified Belief: "The Crown's secularism will be corrected by Faith's patient endurance" (unchallenged 10 seasons). This season:
- Player wins Total Victory Contest against Himlensendt targeting this Belief (Path A) → Scar.
- Procedure B at Accounting: Himlensendt has 3 accumulated contradicting Memories (salience ≥ 3) for this same Belief's domain. Strong contradiction condition met → Path B fires → Belief revision.

**Trace:**
- Path A fires in-scene (real-time), before Accounting.
- Scar is applied. Belief domain reset by Contest result.
- Procedure B at Accounting evaluates all active Concerns, resolves those whose TTL or salience have exhausted.
- Path B gating rule (§3.5): "If a Belief is revised via social Contest (Path A) this season, all accumulated contradicting Memories for that Belief reset."
- **The spec correctly prevents double-application.** Path A fires first (in-scene), resets Memory accumulation for that Belief domain, Path B Concern resolves as "no strong contradiction" (Memories reset to 0 accumulated weight) → no revision.

**Result: CLEAN.** The spec's Path A reset rule correctly prevents double-application. However:

**Issue (ST-17-A):** The reset rule says "accumulated contradicting Memories for that Belief reset" — but what does "reset" mean for a Memory? The Memory is not deleted (it still exists, its reference_count just decremented? Or its salience is unaffected and the reset is on the Belief's "evidence weight" tracking?). The spec doesn't define what the Memory accumulation counter is or how it's stored per-Belief.

The Concern resolution algorithm (§3.4) searches Memories for matching tags — it doesn't have a per-Belief accumulation counter. The contradiction-strength determination (§3.5) says "2+ contradicting Memories with salience ≥ 3" — this appears to be a real-time count during Procedure B, not a stored counter. If it's a real-time count, the Path A reset can't "reset" it without either modifying Memory content or adding a per-Belief "resolved this season via Contest" flag.

**Patch ST-17:** Clarify the Path A reset mechanism. Add to §3.5: "Path A reset is implemented as a per-Belief flag: `contested_this_season: bool`. When Path A fires on a Belief, set `contested_this_season = true`. Procedure B Concern resolution: before evaluating contradiction strength for a Belief, check `contested_this_season`. If true, skip Path B evaluation for this Belief this season; reset flag at end of Accounting." This is a per-Belief flag, not a Memory modification. Memories remain intact for next season's evaluation.

---

## ST-18: Concern-Generated Scar Generates New Concern in Same Accounting Pass

**Probe:** Procedure B processing. NPC Klapp has a Concern about Archbishop Himlensendt's authority. The Concern resolves: strong contradiction met → Belief revision → Scar. Klapp's Scar triggers Mood: Distracted. The Scar also triggers (by spec §6.2): "generate Concern('Is [Belief] accurate given Knowledge X?')" — wait, that's for Knowledge contradiction, not Scar.

**Revised probe:** Scar triggers Mood: Distracted (§6.1, Mood transition). Mood: Distracted does not itself generate a Concern in the spec. But a Scar changes Klapp's `conviction_secondary` weighting (Scar count increases → armature shifts). A new event fires this same season that Klapp is affected by. Concern generation for that event uses the post-Scar armature.

**Trace:**
- Procedure B processes events in `for each event in last_season.events`.
- If Klapp's Scar fires during Concern resolution mid-loop, subsequent Concern generation for other events in the same loop uses the updated armature (post-Scar).
- **Ordering within Procedure B:** Generation loop (for all events, all affected NPCs) happens before the Resolution loop (for all concerns, check salience/TTL). Or are they interleaved?
- The spec pseudocode (§6.2) shows: Generation block, then Resolution block, sequentially. They are not interleaved.
- This means: Scars acquired through Resolution (Path B) in Procedure B do NOT affect Concern Generation for the same Accounting pass — generation already completed. The Scar takes effect in the NEXT season's generation.

**Result: CLEAN** by sequential ordering. But:

**Issue (ST-18-A):** The spec's Procedure B pseudocode shows Generation then Resolution. However, Domain Action Proposal Phase sits between B and C: "Procedures run in fixed order at Accounting: B → (Domain Action proposals) → C → D → E." If a Scar fires during B-Resolution, the NPC's Mood is already Distracted when Domain Action proposals run. The spec correctly handles this: Procedure B Resolution → Distracted set → DA proposal phase checks mood (institutional_deference + Distracted = suppress proposal). **This is consistent.** But the spec doesn't explicitly state that Mood set during B-Resolution is active for the DA phase immediately following. Clarify ordering.

**Patch ST-18:** Add to §6.2 ordering note: "Mood states set during Procedure B Resolution (from Scar application) are active for the Domain Action Proposal Phase immediately following — the Phase does not use pre-Accounting Mood snapshots."

---

## ST-19: Grieving NPC Requires DA Proposal — Project Domain_Action_Required = True

**Probe:** Crown Marshal Ehrenwall has an active Project (progress 7, established) with `domain_action_required = true`. This season, Ehrenwall's Knot partner dies → Mood: Grieving (2-4 seasons). Procedure C runs.

**Trace:**
- Procedure C: "if npc.mood == Distracted: if project.progress < 3: continue [halt]; else: continue at +1 Ob"
- Grieving: spec §6.1 Mood table: "Major actions auto-fail without Spirit check Ob 1; minor actions standard."
- A Domain Action proposal is a major action. Without a Spirit check Ob 1, the proposal auto-fails.
- Project progress = 7 (established). Procedure C would normally advance the project. But the DA proposal auto-fails.
- **The DA Proposal Phase (between B and C) runs before Procedure C.** Ehrenwall's proposal goes into the DA phase. The DA phase checks `if npc.mood == Distracted and npc.personality.institutional_deference >= 1: continue`. Grieving is NOT Distracted — the DA phase's mood gating only explicitly handles Distracted. Grieving has no explicit gating in the DA phase pseudocode.

**Issue (ST-19-A):** The Domain Action Proposal Phase's mood gating (§6.2) explicitly handles only Distracted mood. Grieving mood has a major-action auto-fail rule (§6.1) but the DA proposal phase does not reference this rule. If a Grieving NPC's Project needs a DA, the proposal enters the phase without obstruction from the Distracted check — then presumably fires and auto-fails (requiring Spirit Ob 1). But the auto-fail rule is in §6.1's Mood table, not in the DA phase's procedure. The DA phase doesn't invoke Spirit checks. **The integration between Mood table effects and the DA phase is implicit and may be missed in implementation.**

**Issue (ST-19-B):** If Ehrenwall's DA auto-fails due to Grieving, his Project stalls. `project.seasons_stalled += 1`. If this continues for 8 seasons → failure. A 2-4 season Grieving period with DA-required Project could stall the Project to near-failure threshold. After Grieving resolves, the Project still needs to advance 3 more progress steps within the remaining stall budget. This is mechanically sound (grief has consequences) but the designer needs to know this is the intended behavior.

**Patch ST-19:** In the DA Proposal Phase pseudocode (§6.2), add Grieving handling explicitly: "If npc.mood == Grieving: proposal requires Spirit check Ob 1 to proceed (per §6.1 major-action auto-fail). If check fails: proposal does not enter DA phase this season; project.seasons_stalled += 1." This makes the Grieving interaction explicit in the DA phase rather than relying on implicit §6.1 application.

---

## ST-20: Settlement Signal With Zero Passive NPCs — Empty Aggregate

**Probe:** Remote outpost with no named Passive NPCs. Only governor + anonymous population. Event fires affecting this settlement. `compute_settlement_signal` runs (§5.2).

**Trace:**
```
function compute_settlement_signal(settlement, recent_memories):
    weighted_memories = []
    for npc in settlement.passive_npcs:        # empty — no Passive NPCs
        for memory in npc.recent_memories:
            ...
    # weighted_memories is empty []
    grouped = group_by_event_type([])          # empty dict
    dominant_tag = max({}, key=...)            # ERROR: max() on empty sequence
    net_affect = sum([]) / sum([])             # ZeroDivisionError
```

**Issue (ST-20-A):** `compute_settlement_signal` as written will crash (ZeroDivisionError / empty-sequence max()) when no Passive NPCs are present. The function assumes at least one Passive NPC Memory to aggregate.

**Issue (ST-20-B):** The Settlement Meta-Armature (§5.1) correctly handles the absent Passive NPC tier (weight normalization). But §5.2's Settlement Signal function is not aligned — it uses Passive NPC Memories as its sole input, without any fallback to the governor's interpretation or population baseline when the Passive NPC set is empty.

**Patch ST-20:** Add null guard to `compute_settlement_signal`: 
```
if not weighted_memories:
    # No Passive NPCs: generate minimal signal from population disposition only
    signal = SettlementSignal(
        affect_axis=settlement.population_disposition_average,
        primary_tag="population_mood",
        salience=max(1, abs(settlement.population_disposition_average) * 2)
    )
    signal.salience = signal.salience × 0.7
    return signal
```
Population disposition average is already tracked (per §5.1 component). This ensures the function is non-crashing and produces meaningful output even in sparse settlements.

---

## ST-21: Peninsula-Scale Event Originating at Peninsula Level

**Probe:** A peninsula-wide event fires (Calamity escalation, famine affecting all territories). This is NOT a personal event propagating upward — it originates at peninsula scale. What cascade attenuation applies?

**Trace:**
- §4.4: "Decay factor: 0.7 per boundary crossed. Example: Personal event with salience 5 → Settlement Signal: 5 × 0.7 = 3.5 → Faction Concern: 3.5 × 0.7 = 2.45 → Peninsula: 2.45 × 0.7 = 1.7."
- The example assumes bottom-up propagation. Peninsula-originating events propagate **downward** to faction, settlement, and personal scales.
- **The spec defines only upward cascade attenuation.** There is no downward cascade rule.
- A peninsula-scale famine should affect faction Concerns (food, resource Domain Actions), settlement Signals (hunger, unrest), and individual NPC Concerns (their Projects disrupted). The Event Impact Matrix (§4.1) includes `scale_signature[]` — which scales the consequences run at — but the propagation direction is not specified.

**Issue (ST-21-A):** Downward cascade from peninsula-scale events is undefined. The cascade attenuation section only illustrates upward propagation. A famine originating at peninsula scale would presumably hit factions directly (salience unattenuated at that scale) and then produce Settlement Signals at 0.7 decay and personal NPC Concerns at 0.7^2 decay. But this is an inference, not specified.

**Issue (ST-21-B):** The `scale_signature[]` field captures which scales are affected but doesn't define how the Event Impact Matrix is split across those scales for propagation purposes. The Matrix is computed once — but does it contain one row per affected scale, or one row per affected NPC/faction?

**Patch ST-21:** Add to §4.4: "Cascade attenuation is symmetric. Events originating at a higher scale propagate downward with ×0.7 decay per scale boundary crossed, same as upward propagation. Peninsula-originating event at salience 5: Faction Concern salience 5 (no boundary) → Settlement Signal salience 3.5 (×0.7) → NPC Concern from Settlement Signal salience 2.45 (×0.7 again). Threshold rule (Salience < 2 → inert) applies in both directions."

---

## ST-22: Anomaly Detection — "Major External Crisis" Threshold Undefined

**Probe:** §5.4 Anomaly detection trigger: "≥3 inner-circle NPCs simultaneously {Disposition-with-leader < baseline} AND ≥2 in negative Mood AND **no major external crisis event this season**."

**Trace:**
- The condition "no major external crisis event this season" is the suppressor. If a major external crisis exists, the anomaly detection doesn't fire (the Disposition drops are attributed to the crisis, not internal destabilization).
- **"Major external crisis" is undefined.** The spec lists no threshold for event magnitude, scope, or type that qualifies.
- Example: A minor skirmish at the border (1 territory, low casualties, faction resource loss 1) — does this qualify? A treaty breach? A Calamity event?
- Implementation will need to make this call. If the threshold is too low (any combat event = major crisis), anomaly detection is permanently suppressed during active campaigns. If too high (only full territorial loss), the detection system is too sensitive to non-crisis periods only.

**Issue (ST-22-A):** "Major external crisis" has no spec-defined threshold. This is an implementation-facing gap that could produce systematic false-negative suppression or false-positive fires depending on how implementers interpret it.

**Patch ST-22:** Define threshold in §5.4: "Major external crisis" for anomaly detection suppression purposes = any event this season with `scale_signature` containing {faction} or {peninsula} AND `material_effects` magnitude ≥ 2 for at least one inner-circle NPC. Personal-scale events do not qualify as major external crises for this purpose. Implementation note: if multiple simultaneous personal-scale events compound to faction-level disruption, they do NOT suppress anomaly detection individually — only events explicitly designated faction-scale or above in the Event Impact Matrix's scale_signature."

---

## ST-23: NPC With conviction_secondary = None at Scar 3+

**Probe:** Baralta has conviction_primary = Precedent, conviction_secondary = None (authored without a secondary Conviction). Baralta acquires 3 Scars across a campaign.

**Trace:**
- §3.2 weight derivation: "Scar 3+: secondary leads."
- conviction_secondary = None → no secondary weight table exists.
- The armature computation for `modify_by_scar_count` would attempt to load weights for `None` Conviction.

**Issue (ST-23-A):** No fallback specified for conviction_secondary = None at Scar 3+. The scar weight formula breaks for NPCs authored without a secondary Conviction — which is an explicitly allowed state (§2.1: "conviction_secondary: one of the above (or None)").

**Patch ST-23:** Add to §3.2: "If conviction_secondary = None and scar_count ≥ 1: scar modulation uses only conviction_primary weights, reduced by scar_count × 0.1 in specificity (spread weight mass more evenly across options) rather than shifting toward a secondary Conviction. Rationale: without a secondary anchor, scarred NPCs with no secondary become less certain in their primary — their interpretations spread across options — rather than shifting to an alternative framework." This produces a mechanically meaningful behavior (traumatized NPC becomes more interpretively uncertain) that works without a secondary Conviction.

---

## ST-24: Unknown Event Type Not in Conviction × Event Resonance Table

**Probe:** A unique event fires — "The Varfell Archivist presents evidence that the Calamity was man-made, not divine" — with event_type tag: `historical_revelation`. This event type is not among the 30 authored event types in the 210-entry conviction × event-type resonance table.

**Trace:**
- Event Impact Matrix construction requires `conviction_resonance` from the resonance table for symbolic_effects.
- Event type not in table → resonance lookup fails.
- `compute_settlement_signal` and `generate_concern` both require the Matrix, which depends on the resonance table.

**Issue (ST-24-A):** No fallback for unknown event types in the resonance table. Any authored event with a non-canonical type tag will break Matrix construction. The 30-type table was intended to cover "high-frequency event types initially" (§10, Gossip) — implying the table is incomplete by design. But there is no fallback behavior for events outside the table.

**Issue (ST-24-B):** Related: the spec says "~30 event types" — this is approximate. The authoring process will produce additional types. The system needs a graceful degradation path, not a hard failure.

**Patch ST-24:** Add to §4.1 Event Impact Matrix construction: "If event_type is not in the conviction × event-type resonance table: set all symbolic_effects conviction_resonance = neutral for this event. Log event_type as 'unmapped' for authoring follow-up. This ensures Matrix construction succeeds for novel event types while flagging them for table extension." A neutral resonance means the event produces material and relational effects but no conviction-alignment symbolic effects — conservative and safe as a fallback.

---

## ST-25: Player Systematic Opinion Poisoning — Full Negative Opinion Lock

**Probe:** Player engineers events so that all ~8 Opinion targets of Crown faction leader Almud shift to affect_axis = -3, confidence = 5 (maximum negative, fully entrenched). This is theoretically achievable through systematic betrayals, engineered failures, and insinuations over multiple seasons.

**Trace:**
- All of Almud's NPC opinions are at -3, confidence 5.
- Procedure D runs: new Memories are generated by events this season. All Memories involving Almud's opinion targets are negative-affect (because the player continues operating adversarially).
- Drift formula: `drift = base_drift × (1 - abs(opinion.affect_axis) / 3) × conviction_alignment_multiplier`
- At affect_axis = -3: dampening factor = (1 - 3/3) = 0. **Drift is zero.** The opinion is locked. No further movement in any direction.
- Almud has no positive Opinion of anyone in her inner-circle.

**Issue (ST-25-A):** Full-negative Opinion lock is mechanically stable — the dampening factor correctly prevents further movement. But the locked state means Almud's leadership function is impaired: all collaborative actions require Opinion above some threshold (implied by spec but not explicitly stated). If all Opinions are at -3, no collaborative Domain Actions fire (every proposal from any NPC is opposed by Almud's -3 affect opinions toward them). This is an extreme state but not a crash.

**Issue (ST-25-B):** Once locked at -3 confidence 5, Almud's Opinions are permanently frozen. The only path out of a locked Opinion is discrete events — but the drift formula prevents drift from escaping the clamp. The spec has no mechanism for deliberate "trust reset" or NPC-side Opinion recovery from entrenched negative states without memory-restructuring events. **This may be intentional** (deeply entrenched enmity is permanent unless a sufficiently dramatic event fires) — but the anomaly detection system (§5.4) should catch it:
- ≥3 inner-circle NPCs with Disposition-with-leader < baseline AND ≥2 in negative Mood AND no major external crisis → "Internal destabilization detected?" Concern.
- Almud's Opinions are NPC-NPC, not Disposition-with-player. Anomaly detection checks Disposition-with-leader (NPC-to-leader), not Almud's Opinion of them.
- If Almud has been generating hostile behavior toward her inner-circle (because their proposals always generate opposition from her armature), their Disposition-with-leader (Almud) would also drop — this eventually triggers anomaly detection independently.

**Result: CONDITIONALLY CLEAN.** The Opinion lock is mechanically stable. Anomaly detection fires through a separate channel (NPC Dispositions toward Almud dropping, not Almud's Opinions of them). However:

**Issue (ST-25-C):** The anomaly detection trigger references "Disposition-with-leader" — but it is not specified whether "leader" means the faction leader (Almud) or the player character. If it means the faction leader, then Almud's own opinion degradation of her inner-circle is not detected by the anomaly system (she doesn't self-report destabilization through her own Opinions). The anomaly fires only when inner-circle NPCs' Dispositions toward Almud drop. This is the correct behavior — but clarify the spec: "Disposition-with-leader = each inner-circle NPC's Disposition directed toward the faction leader NPC, not the player character."

**Patch ST-25:** Clarify §5.4 Anomaly Detection: "Disposition-with-leader refers to the Disposition value held by each inner-circle NPC directed toward the faction leader NPC. Not player Disposition. Not leader's Opinion of them." No other patch required; the system handles this correctly once the reference is unambiguous.

---

## ST-26: Standing 5+ Player in Faction Meta-Armature — Feedback Loop

**Probe:** Player reaches Standing 5 in Crown faction. Player's Conviction primary = Faith. Over 3 seasons, player engineers 5 major Faith-resonant events affecting Crown inner-circle.

**Trace:**
- §5.3: "At Standing 5+, the player's armature becomes part of the Faction Meta-Armature."
- Player's Faith Conviction → player's armature contributes Faith-weighted interpretations to Faction Meta-Armature aggregate.
- Meta-Armature biases Domain Action selection toward Faith-aligned proposals.
- Faith-aligned NPC proposals get -1 Ob modifier from the Faith-biased meta-armature.
- Successful Faith Domain Actions generate Memory events with positive affect for Faith-aligned NPCs.
- Those NPCs' Opinions of player (who is at +3 or higher Disposition already) produce further Outreach.
- Player uses Outreach scenes to further entrench Faith alignment in Crown.

**Issue (ST-26-A):** This is a functional positive feedback loop: player influences meta-armature → meta-armature favors player-aligned proposals → success generates memories → memories reinforce alignment → player influence grows. The loop has three dampeners built into the spec:
1. `institutional_stability` (§5.3): the faction's historical Conviction (Order/Virtue-Ethics for Crown) provides a fixed counterweight at `0.4 × (1 - inner_circle_scars/max_scars)`. Early-game: ~40% stability weight toward Order, not Faith. Player Faith influence competes against this.
2. Player is one of many inner-circle members. At Standing 5, weight = 0.5 (Standing-based). Leader (Almud, Standing 7) = 1.0 × 1.5 = 1.5. Player's 0.5 is significant but not dominant.
3. Memory-reference salience floor: Faith-resonant Memories accumulate high floor, but so do Order Memories from pre-player-arrival inner-circle members with longer tenure.

**Assessment:** The feedback loop exists but is bounded by institutional_stability and the leader's amplified weight. A player with Faith Conviction at Standing 5 can shift the Faction Meta-Armature's interpretive frame toward Faith, but cannot dominate it before the institutional stability weight decays naturally (requires many inner-circle Scars to substantially reduce). **This is correct behavior** — player political influence is meaningful but not world-breaking.

**Issue (ST-26-B):** If the player deliberately engineers inner-circle Scars (to reduce institutional_stability weight) AND advances to Standing 7 (weight = 1.0 × 1.5 = 1.5, equal to leader), the combination could produce genuine meta-armature dominance. This is a very long-term campaign strategy — but is it intended as a valid endgame? The spec doesn't define whether meta-armature dominance is a win condition or an exploitable degenerate state.

**Patch ST-26:** No structural patch required — the dampeners work correctly. Add a design note to §5.3: "Player meta-armature influence is intentionally bounded by institutional_stability and leader amplification. Coordinated play to reduce institutional_stability (via NPC Scar engineering) while advancing to Standing 7 is a valid but very long-term campaign strategy. Designers should ensure institutional_stability regeneration is possible (e.g., standing historical events reinforce institutional Conviction without requiring Scars) to prevent permanent Crown identity erasure."

---

## ST-27: Project Failure Into Overcrowded DA Slot

**Probe:** NPC Marshal's established Project fails (seasons_stalled ≥ 8). `generate_replacement_project(npc)` fires (§6.2 Procedure C). New Project has `domain_action_required = true` in the Military domain. This season's DA phase already has 2 Military domain proposals from other inner-circle NPCs.

**Trace:**
- New Project is generated during Procedure C (AFTER the DA Proposal Phase, which runs between B and C).
- The DA phase for this season has already run.
- The new Project's DA cannot be proposed this season (generation happened after DA phase closed).
- `project.seasons_stalled` resets to 0 on generation. But no DA advancement happens this season.
- Next season: DA phase runs normally. The new Project proposes. Competes with other Military proposals via inner-circle competition.

**Result: CLEAN.** The ordering (B → DA → C) means Procedure C failures produce new Projects that begin DA cycles next season. No collision this season. The project.seasons_stalled reset on generation prevents immediate re-failure.

**Issue (ST-27-A):** Minor but worth noting: a Project that fails in Procedure C and generates a replacement also runs `apply_project_legacy(project, npc)` — the completion effect is `failure_effect` in this case. The failure_effect may include Opinion shifts against NPCs who "failed to support" the Project. But which NPCs "failed to support"? The inner-circle competition winners from previous seasons (who won the slot over this NPC) are the appropriate targets. The spec doesn't specify that failure_effect legacy tracks opposition history — it only mentions "NPCs who supported/obstructed." Is the stalled opponent considered an obstructor for legacy purposes?

**Patch ST-27:** Clarify §6.2 Procedure C project legacy: "For failed Projects (seasons_stalled ≥ 8): apply_project_legacy with failure_effect. 'Obstructors' for legacy purposes = inner-circle competition winners who displaced this Project's DA proposals in any prior season. Tracked via a `blocked_by[]` list appended at each inner-circle competition loss." This requires adding `blocked_by: list[npc_id]` to the Project data structure (§2.4).

---

## ST-28: Gossip + Knowledge Contradiction at Same NPC

**Probe:** NPC Warden Solmund receives gossip from Baralta: "Hafenmark is funding the Calamity cult in Verdmuld." This becomes a Memory at salience 2 (gossip from Distant Contact). Solmund also holds direct Knowledge: "No Hafenmark financial activity in Verdmuld cult networks" (ongoing_state, salience 4, valid=true, contradicting the gossip content).

**Trace:**
- Solmund has a Memory (gossip-sourced, negative-affect, low salience) and a Knowledge entry (direct, high salience, contradicting).
- Procedure B generates a Concern if: Knowledge salience ≥ 4 AND contradicts an active Belief domain. Is this Knowledge triggering a Belief-domain Concern?
- The gossip Memory generates no automatic Concern (low salience doesn't trigger).
- If Solmund has a Belief about "Hafenmark's institutional ethics" — the contradicting Knowledge (high-salience, valid) triggers a Concern: "Is my understanding of Hafenmark's institutional behavior accurate given what I know?"
- Concern resolution: Solmund's Memories are searched. The gossip Memory is salience 2. Direct Knowledge is not a Memory — it's in a separate data structure. **Concern resolution searches Memories, not Knowledge.**

**Issue (ST-28-A):** Concern resolution uses Memories as evidence, not Knowledge entries. An NPC who holds contradicting Knowledge (high-salience, valid) generates a Concern via the Knowledge trigger, but then resolves that Concern by searching Memories — which may not include the Knowledge content at all (Knowledge and Memory are separate structures in §2.6 and §2.7). The Concern resolves on the gossip Memory (salience 2) as the closest match, producing a wrong resolution weighted toward the gossip rather than the direct Knowledge.

This is partly intentional (NPCs reason from experience, not information) — but it produces the paradox that high-quality direct Knowledge can trigger a Concern that then resolves to favor low-quality gossip Memory.

**Issue (ST-28-B):** Knowledge sharing (Procedure E) creates Memories from shared Knowledge: "new_memory = Memory('Heard from [npc] that [knowledge.fact]')" (§6.2 Procedure E). But Solmund's *own* Knowledge doesn't get auto-converted to a Memory. The NPC holds direct Knowledge but has no Memory of "I know this from direct investigation." This means Knowledge can never enter Concern resolution as direct evidence.

**Patch ST-28:** Add to §6.2 Procedure B Resolution: "When resolving a Knowledge-triggered Concern, search both Memories AND active Knowledge entries for matching seeking tags. Knowledge entries with valid=true receive a match_score bonus of +1 (direct knowledge outweighs Memory of gossip). Knowledge entries with valid=false receive a match_score penalty of -2 (known-invalid knowledge does not resolve Concerns)." This makes Knowledge a first-class participant in Concern resolution for Knowledge-generated Concerns specifically.

---

## ST-29: Loyalty Cover Decay — No Renewal for 4+ Seasons

**Probe:** Player performed major loyalty signal 4 seasons ago (Standing advancement). Has not performed a major loyalty signal since. Cover has been decaying.

**Trace:**
- §7.5: "Loyalty Cover bonus: +1 (max +2) for major loyalty signals this season. Decays each season not renewed."
- Decay rate is unspecified. "Decays each season" — by how much?
- If decay = -1 per season: after 2 seasons without renewal, bonus is 0. This is reasonable.
- But if the base Cover can go below 0 from lack of loyalty signals — the spec doesn't say Cover has a floor.

**Issue (ST-29-A):** Loyalty Cover bonus decay rate is unspecified. "Decays each season not renewed" does not define the step size. Implementation will choose arbitrarily — likely -1/season, which is reasonable, but should be specified.

**Issue (ST-29-B):** The relationship between the player's base Cover (without loyalty bonus) and the loyalty Cover bonus is undefined. Is the loyalty Cover bonus additive to a base Cover value? What is that base value? The §7.5 formula: `faction.intel_pool roll vs (player.cover + loyalty_cover_bonus)` — player.cover is referenced as an existing value, not defined in this spec.

**Patch ST-29:** In §7.5: "Loyalty Cover bonus decay rate: -1 per season not renewed. Minimum bonus: 0 (cannot reduce below zero). The base player.cover value is defined in existing systems (not in scope of this spec); the loyalty_cover_bonus is additive and decays independently."

---

## ST-30: Witness Mode — All 3 Capped Results Involve Same NPC

**Probe:** Season with 8 Witness Mode scenes. Five of them involve Confessor Himlensendt (high Disposition +3 with player). The priority rule (§7.3): "3 most scene-action-relevant results — those involving NPCs with highest Disposition with player." All top-3 selections resolve to Himlensendt.

**Trace:**
- Witness Mode cap: max 3 Read results.
- Selection: highest Disposition NPCs. Himlensendt at +3 dominates.
- Player receives 3 Read results, all for the same NPC (Himlensendt).
- The remaining 5 Witness scenes (including Almud's succession crisis, a Hafenmark territorial action) produce "narrative summary only."

**Issue (ST-30-A):** Witness Mode selection by "highest Disposition NPC" without a uniqueness constraint produces potentially all-same-NPC results. This deprives the player of any information about non-Himlensendt scenes while giving them 3 views of Himlensendt — which may be redundant (3 Read results about the same NPC, possibly duplicating information).

**Patch ST-30:** Add to §7.3: "Witness Mode Read result selection applies uniqueness constraint: no more than 1 Read result per NPC per Accounting. After applying Disposition priority ordering, select the top N (up to cap=3) with distinct NPCs." This ensures the 3 results represent 3 different NPCs, giving wider political coverage to the player.

---

## ST-31: Cross-Faction Knowledge Sharing — Sharer Generates No Concern

**Probe:** NPC Hafenmark Councilor Baralta (Procedure E Distant Contact, 10% chance) shares sensitive Knowledge (sensitivity=3) with Crown NPC Ehrenwall. The Knowledge is: "Hafenmark's military capacity is lower than publicly stated." The share fires (Concern seek-tag matched for Ehrenwall). Ehrenwall gains a Memory of this fact.

**Trace:**
- Procedure E: Knowledge is shared if "any other.concern.seeking matches knowledge.fact_tag." Sensitivity gate: only explicit sensitivity check in spec is in §7.1 (Read action gate) — the Distant Contact Knowledge sharing (§6.2 Procedure E) does not reference a sensitivity gate.
- Knowledge sensitivity = 3. The sharing in Procedure E has no sensitivity gate — any Knowledge is shared if the seek-tag matches.

**Issue (ST-31-A):** Procedure E Knowledge sharing has no sensitivity gate. A highly sensitive Knowledge entry (sensitivity=5 — faction military secrets) can be shared cross-faction in ambient Distant Contact interactions if the receiving NPC has a Concern seeking that fact_tag. This is a significant security leak that bypasses the Disposition-based sensitivity gate in §7.1 (which governs player-facing information access, not NPC-NPC sharing).

**Issue (ST-31-B):** After sharing, does Baralta generate any Concern about having shared? The spec has no NPC self-monitoring for information disclosure. A Precedent-Conviction NPC (institutional loyalty) would have strong armature signals toward "did I just violate institutional protocol?" — but no mechanism triggers this.

**Patch ST-31:** Add sensitivity gate to Procedure E Knowledge sharing: "Knowledge sharing in Distant Contact is gated by sensitivity: Knowledge with sensitivity ≥ 4 is NOT shared in ambient Distant Contact interactions regardless of seek-tag matching. Sensitivity 1-3 may be shared. Sensitivity gate for NPC-NPC sharing uses the sharer's Conviction alignment with institutional loyalty as a modifier: high institutional_deference NPCs effectively treat sensitivity ≥ 3 as non-shareable." This aligns Knowledge sharing with the NPC's character.

For concern generation: add "If NPC shares Knowledge with sensitivity ≥ 2 cross-faction: generate low-salience Concern (salience 1): 'Did I compromise institutional information?' Source event = sharing interaction." This produces optional self-reflection without over-burdening the system.

---

## ST-32: Procedure B-Resolution Looping — Concern Generates Opinion Drift Generates Concern

**Probe:** Klapp's Concern resolves → produces Opinion shift toward Himlensendt from +1 to +2 (strong new positive Memory). Procedure D hasn't run yet this season (runs after B and DA and C). But the Opinion is modified in B-Resolution.

**Trace:**
- Procedure B Resolution calls `apply_resolution(npc, resolution)` which "may produce Belief update, Opinion drift, or Scar."
- If apply_resolution produces an Opinion drift, this is a direct write to Opinion during Procedure B.
- When Procedure D runs later this Accounting, it processes this season's Memories to produce Opinion drift. But the B-Resolution-produced drift already modified the Opinion.
- Procedure D uses `new_memories = filter_memories(npc.memories, this_season=True)`. The Memory generated by Concern resolution IS a this-season Memory — it gets processed by Procedure D as well.
- This means a single Concern resolution can produce: (1) direct Opinion drift in B-Resolution, AND (2) Memory-driven Opinion drift for the same Memory in Procedure D. **Double-counting.**

**Issue (ST-32-A):** Concern resolution-produced Opinion drift may be double-counted: once directly applied in B-Resolution and once again from the resulting Memory in Procedure D. The Opinion moves twice from the same underlying event.

**Patch ST-32:** Two options:
- Option A: B-Resolution produces the Memory only, not direct Opinion drift. Procedure D then processes the Memory normally. No double-count.
- Option B: B-Resolution produces direct Opinion drift AND flags the resulting Memory as `resolution_sourced = true`. Procedure D skips flagged Memories.
- **Recommend Option A** — cleaner, Memory is the unit of record, Opinion drift is always Procedure D's domain. Modify §3.5 Belief Revision Paths to remove "may produce Opinion drift" from apply_resolution; instead: "produces Memory entries and Belief updates; Opinion drift from those Memories is processed by Procedure D normally."

---

## Summary Table

| ID | System Area | Issue Type | Severity | Patch Required? |
|---|---|---|---|---|
| ST-13-A | Memory replacement | Tie-break undefined | **Medium** | Yes |
| ST-13-B | Memory merge | Merge trigger undefined | **Medium** | Yes |
| ST-14-A | Concern dropping | Tie-break undefined | **Medium** | Yes |
| ST-14-B | Concern cap | Transient overflow under simultaneous events | **Low** | Yes (minor) |
| ST-15-A | Opinion initialization | First-contact mechanism undefined | **High** | Yes |
| ST-15-B | Procedure E + D | Drift applied to non-existent Opinion object | **High** | Yes |
| ST-16-A | Memory salience floor | Permanent max-salience lock (intentional but undocumented) | Design note | Clarify |
| ST-17-A | Path A reset | Reset mechanism not implementable without Belief flag | **High** | Yes |
| ST-18-A | Procedure B ordering | Mood state timing for DA phase implicit | **Low** | Clarify |
| ST-19-A | DA phase + Grieving Mood | Grieving major-action auto-fail not in DA pseudocode | **High** | Yes |
| ST-19-B | Project stall under Grieving | Expected behavior (design note) | Design note | Clarify |
| ST-20-A | Settlement Signal | ZeroDivisionError / max() crash on empty Passive NPC set | **Critical** | Yes |
| ST-20-B | Settlement Signal | Passive NPC-only input has no governor fallback | **Medium** | Yes |
| ST-21-A | Cascade attenuation | Downward propagation from peninsula-scale undefined | **Medium** | Yes |
| ST-21-B | Event Impact Matrix scale_signature | Split-by-scale not defined | **Low** | Clarify |
| ST-22-A | Anomaly detection | "Major external crisis" threshold undefined | **Medium** | Yes |
| ST-23-A | Armature | conviction_secondary = None at Scar 3+ crashes weight derivation | **High** | Yes |
| ST-24-A/B | Event Impact Matrix | Unknown event type crashes Matrix construction | **High** | Yes |
| ST-25-C | Anomaly detection | "Disposition-with-leader" referent ambiguous | **Low** | Clarify |
| ST-26-B | Faction Meta-Armature | Institutional_stability regeneration unspecified | Design note | Note |
| ST-27-A | Project legacy | "Obstructor" for failed Project legacy undefined | **Low** | Yes |
| ST-28-A/B | Concern resolution | Knowledge not searchable in Concern resolution | **Medium** | Yes |
| ST-29-A | Loyalty Cover | Decay rate unspecified | **Low** | Specify |
| ST-29-B | Loyalty Cover | Base player.cover relationship to bonus undefined | **Low** | Clarify |
| ST-30-A | Witness Mode | No uniqueness constraint on NPC per-Accounting | **Medium** | Yes |
| ST-31-A | Procedure E sharing | Knowledge sharing has no sensitivity gate | **High** | Yes |
| ST-31-B | NPC self-monitoring | No Concern generated on sensitive information disclosure | Design choice | Note |
| ST-32-A | Opinion drift | Double-counting from Concern-resolution + Procedure D | **High** | Yes |

---

## Issues Confirmed Clean (No Action Required)

- **ST-17 base:** Path A + Path B on same Belief — sequential ordering prevents double-application. Patch ST-17 only adds implementability clarity.
- **ST-18 base:** Concern-generated Scar doesn't retroactively affect Concern generation (sequential B structure).
- **ST-25 base:** Full-negative Opinion lock is mechanically stable and bounded; anomaly detection fires through independent channel.
- **ST-26 base:** Player meta-armature influence is bounded by institutional_stability and leader amplification. Feedback loop exists but is self-limiting.
- **ST-27 base:** Project failure → new Project generation ordering is clean (Procedure C runs after DA phase).

---

## Issue Count

- **Critical:** 1 (ST-20-A — crash)
- **High:** 7 (ST-15-A/B, ST-17-A, ST-19-A, ST-23-A, ST-24-A, ST-28-A, ST-31-A, ST-32-A) — 8 counting ST-24-B
- **Medium:** 6
- **Low:** 6
- **Design notes / clarifications:** 5

**Total issues requiring spec action: 20. Critical or High: 9. All are patchable within current architecture — no structural redesign required.**
