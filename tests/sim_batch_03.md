# VALORIA SIMULATION BATCH 03
## 30 Stress Tests — Track Terminals, NPCs, Remaining Mechanics
**Executed:** 2026-03-27 | **Model:** Sonnet 4.6 | **Skill:** valoria-simulator

---

## Corrections from Batch 02
- **F29 RETRACTED:** Coherence is a live canonical track (§5.10). §5.11 "−1 Coherence per use" is correct.
- **F31 RETRACTED as P1:** Dissolution Residue draining Coherence is correct. Coherence ≠ Intelligibility — separate tracks.
- **M-021 matrix label corrected:** "Taint Track" → "Coherence Track." Taint was renamed to Coherence in CP14 Stage 17 patch (Appendix A, Stage 17-P2). No live Taint track exists.
- **Remaining P1 findings from Batch 02:** F25 only (Personal-scale Pulling bypasses social counter-mechanics).

---

## TEST B3-001 — Certainty Track: Full Depletion Arc
**Coverage:** M-009 | TTRPG | CROSS | CERT, TS, INT | — | — | — | Practitioner

**Mode A + D — Isolation + Terminal Value**

### Track Parameters
Starting = Spirit score; Max = Spirit score; Range 0–(Spirit max 7).

**Loss triggers per event type:**
| Trigger | Loss | Resist? |
|---------|------|---------|
| Successful Leap | −1 | No |
| Non-consensual Thread work on sentient | −1 | No |
| Witness monstrous entity | −1 | Spirit TN7 Ob1 (Devout +2D) |
| Intelligibility ≤ 4 | −1 to **maximum** per level below 5 | No |

### Depletion Simulation — Spirit 5 Practitioner

| Event | Raw | Max | State |
|-------|-----|-----|-------|
| Start | 5/5 | 5 | Normal |
| Leap 1 (success) | 4/5 | 5 | −1 |
| Monstrous entity, resist fails | 3/5 | 5 | −1 |
| Non-consensual Pull | 2/5 | 5 | −1 |
| Intelligibility drops to 4 | 2/4 | 4 | Max reduced |
| Intelligibility drops to 3 | 2/3 | 3 | Max −2 from base |
| Leap 2 (success) | 1/3 | 3 | −1 |
| Witness second entity, resist fails | 0/3 | 3 | **Rendering Crisis** |

**Rendering Crisis at 0:** Scene event. Character must: revise a Belief, withdraw from Thread-active situations, or find new framework. Not passive incapacitation — active narrative requirement.

**Maximum suppression:** Intelligibility at 1 → Max = Spirit − 3 = 2 (for Spirit 5). Even fully recovered (Certainty 2/2), a single failed resist on a monstrous entity triggers Rendering Crisis. **Intelligibility degradation creates a permanent structural vulnerability to Certainty crisis.**

### Recovery Rate vs Loss Rate
- Recovery: +1 per season of non-practice + stable relationships; +1 from Belief achievement.
- Loss rate (active practitioner): 1–3 per session minimum. At Spirit 5, 5 losses before crisis.
- Season = ~4 sessions → practitioner can gain ~2 Certainty/season from rest. But active practitioners don't rest.

**Net:** Active practitioners are in a permanent Certainty draw-down. The only sustainable path is either: (a) non-practice seasons (foregoing all Thread work), or (b) high Spirit score (Spirit 7 gives 7 starting, recovers 2/season if possible — barely sustainable).

### Findings
**F52 — Certainty as countdown timer, not track:** With Spirit 5, a practitioner has ~5 events before crisis. At 1–2 events per session, Rendering Crisis arrives within 3–5 sessions. The "recovery" path (non-practice season) requires 4 sessions of inactivity — the same duration as depletion. This is structurally a use-it-lose-it mechanic with no sustainable mid-game equilibrium. Intentional? Works as designed if practitioners are meant to face existential crisis regularly.

**F53 — Max reduction from Intelligibility is severe:** Intelligibility 3 reduces Certainty maximum to Spirit − 2. A Spirit 5 practitioner can only ever have 3 Certainty while Intelligibility is at 3. Even if they recover Certainty to max (via non-practice season), the ceiling compresses. Double-track degradation: Intelligibility drops → Certainty ceiling drops → crisis arrives faster. No recovery path for Intelligibility max suppression of Certainty except recovering Intelligibility itself.

**Severity:** F52 = P3 (intended existential pressure). F53 = P2 (double-track compression may be unintentionally terminal — confirm ceiling interaction is designed).

---

## TEST B3-002 — Past-Oriented Pulling: Temporal Disjunction Cascade
**Coverage:** M-019 | TTRPG | PAST | TD, TT, TS, CERT | Varfell | — | Vaynard | Practitioner

**Mode C — Full Scenario**

### Setup
Maret Uln (TS confirmed practitioner, Spirit 5, Attunement 5) attempts Past-Oriented Pulling to erase a signed treaty between Varfell and the Crown from the same session.

**Requirements check:**
- TS 70+? ❌ — Maret's TS is practitioner-level but unspecified. If TS < 70: **cannot perform Past-Oriented Pulling.** This is the primary gate. Assuming TS = 72 for this test (Attuned → Sensitive tier).
- TT ≥ 40? Assumed TT 48. ✓
- Diagnosis mandatory. ✓ (performed prior round)

### State: Pre-Operation
```
Maret — TS 72, Spirit 5, Certainty 3/5, Intelligibility 7, ThS 14
TT 48 | TC 33 | IP 30
Target: Signed treaty (Relational-scale configuration, same session = Ob 4)
```

### Roll
**Pool:** Spirit 5 + "Thread Practices" History (4 pts + 3) = 5 + 7 = **12D**
**TN:** 7. **Ob:** Same session = **Ob 4**.
Expected net: 12 × 0.33 ≈ 4.0. P(≥4) ≈ 62%. P(≥8 Overwhelming) ≈ 22%.

### Outcome: Success (most likely)

**Immediate mechanical consequences:**
- TT: +3 minimum. TT 48 → **51**. Crosses TT 50 threshold (cross-clock: TC +1/season now locks in).
- ThS automatic (Pulling auto-effect −1) + Past-Oriented additional (−3 total): ThS 14 → **10**. Enters **Fractured band**. Fractured Fallout fires immediately (d6 roll).
- TD: +1 from temporal operation. TD 0 → 1 (first operation).

**Temporal Disjunction outcome:**
Physical facts: treaty document becomes incoherent text. Both parties' signatures fade. The negotiators' hands feel wrong — they have a memory of signing something that no longer exists in material form.

**Epistemic co-movement (automatic):**
All witnesses retain both memories: the treaty as it was, and the present where it doesn't exist. The paradox is unresolvable without Thread-level understanding. Each witness: Inert Knowledge of paradox forms.

**Temporal co-movement (automatic):**
ThS −3 additional (Past-Oriented Pull). Crown negotiator who cited the treaty as historical precedent: +1 Ob on any social roll citing it (the precedent's temporal weight is frayed — R40).

**Fraying Bane check:**
First Past-Oriented Pull this season — no Fraying yet. Two more in same season would trigger Fraying Bane (+1 Ob all Thread ops, −1 contact duration, micro-Gaps on partials).

### State: Post-Operation
```
Maret — ThS 10 (FRACTURED — d6 Fractured Fallout fires), TD 1
Certainty 2/5 (−1 from Leap cost earlier)
TT 51 — TC now gains +1/season passive
TC 33 — no immediate threshold change
```

**Fractured Fallout (d6, most likely result 1–6 equally likely):**
E.g. result 4: "You perform an action you do not remember. GM describes the gap." On a first Fractured Fallout, this is a single memory gap — narratively jarring, mechanically minor (+1 Ob on Memory-based rolls now active).

### Findings
**F54 — Single Past-Oriented Pull can push ThS into Fractured:** At ThS 14 (start of Fractured band = 15), one Past-Oriented Pull (−3 ThS) pushes into Fractured immediately. A practitioner beginning a session at ThS 15–17 and performing a Past-Oriented Pull enters Fractured mid-session. Given the operation's high narrative value, this is a realistic scenario. **No warning mechanism** — ThS crosses the threshold mid-operation with no opportunity to abort.

**F55 — TT threshold crossing from Past-Oriented Pull:** The +3 minimum TT gain from Past-Oriented Pulling frequently crosses TT 50 if starting anywhere between 48–50 (common mid-campaign range). TT 50+ triggers TC +1/season passive — a permanent faction-clock consequence from a single character's Thread operation. This is correct (inseparability), but players may not know that erasing a treaty just locked in permanent TC acceleration.

**F56 — Past-Oriented Pulling costs are front-loaded, not graduated:** ThS, TD, and TT all hit at operation completion. No ability to abort mid-operation after seeing the cost. Players commit to the full cost before knowing outcomes beyond success/fail.

**Severity:** F54 = P2 (surprise Fractured entry — consider whether ThS should be visible). F55 = P2 (consequence opacity — TT→TC linkage may not be player-visible at decision point). F56 = P3 (intentional irreversibility).

---

## TEST B3-003 — Coherence Track: Terminal Cascade (M-021 corrected)
**Coverage:** M-021 (Coherence Track) | TTRPG | CROSS | Coherence, CERT, TS | Niflhel | — | — | Practitioner

**Mode D — Terminal Value**

### Coherence Track (10→0, dissolution residue use)
Per §5.10:
- Starts at 10 (fully coherent)
- −1 per use of dissolution residue (max 1 use per contact window)
- Recovery: Corrective Weaving (Ob 3) by another practitioner, +1 per season at Coherence 4–6; below 4 requires active cooperation (which epistemic seduction makes unlikely)

### Terminal State Simulation

| Coherence | Effect | Key Change |
|-----------|--------|-----------|
| 10 | Normal | — |
| 9–7 | +1D Thread ops | Other TS 50+ sense instability; Knot strain +1/3 sessions |
| 6–4 | +2D Thread ops | −1D social; rendering contingency perceptible; Knot strain +1/2 sessions; GM recontextualises one Knot |
| 3–2 | +3D Thread ops | −2D social; NPCs react with unease; minor monstrous presence; all Knots +1 strain/session; Certainty max −1 per level below 4 |
| 1 | Perceived "human/monstrous" as rendering artifact | Player chooses: correction (Coherence → 5, 2 Wounds) or continue |
| 0 | Monstrous configuration | Character → NPC |

### Certainty Maximum Compression at Coherence 2–3
Per §5.10: "Maximum Certainty −1 per Coherence level below 4."
- Coherence 3: Certainty max = Spirit − 1.
- Coherence 2: Certainty max = Spirit − 2.
- Coherence 1: Certainty max = Spirit − 3.

**Combined with Intelligibility max compression (Intelligibility ≤ 4: −1 Certainty max per level below 5):**
A practitioner with Coherence 2 AND Intelligibility 3 has Certainty max = Spirit − 2 (Coherence) − 2 (Intelligibility) = Spirit − 4. At Spirit 5 → max Certainty = 1. **Rendering Crisis is now one event away permanently.**

### Recovery Deadlock at Coherence < 4
"Below Coherence 4: requires the transforming character's active cooperation — which epistemic seduction makes increasingly unlikely."

At Coherence 3: the character perceives the transformation as perceptual clarity, not corruption. They have no mechanical incentive to seek Corrective Weaving and increasingly don't perceive it as desirable. **Mechanically, below Coherence 4 is a near-irreversible path to Coherence 0.**

The only exit before 0: player choosing correction at Coherence 1 (2 Wounds, Coherence → 5). After this: +2D Thread ops lost, but social function restored.

### Findings
**F57 — Coherence below 4 is mechanically terminal without player agency:** The recovery deadlock (cooperation required, cooperation undermined by seduction) means that once a character passes Coherence 3 without intervention, the only mechanical stops are: player chooses correction at 1 (if they still exercise player agency over the character) or the character becomes an NPC at 0. No NPC or external intervention can force recovery. This is intentional (epistemic seduction is P-10), but players should know this is a one-way door below 4.

**F58 — +3D Thread bonus at Coherence 2–3 creates perverse incentive:** At Coherence 2–3, the character gains +3D to all Thread operations — a massive mechanical benefit. This is the seduction working: transformation produces genuine capability increase. Players who discover this may deliberately push Coherence down for the bonus. The recovery cost (NPC at 0, 2 Wounds + reset at 1) is severe but the bonus is real mid-campaign.

**Severity:** F57 = P2 (one-way door should be clearly signposted). F58 = P2 (perverse incentive — deliberate Coherence farming is a dominant strategy risk).

---

## TEST B3-004 — Thread Stability Terminal: ThS 0 Campaign Event
**Coverage:** M-020 (ThS component of TD) | TTRPG | CROSS | TD, ThS, TS | — | — | — | Practitioner

**Mode D — Terminal Value**

### ThS 0 — Crisis
"The character must resolve the disjunction narratively — sustained engagement with the world's rendered state — or withdraw from practice until ThS rises above 5."

**Recovery:** +2 ThS per season of no Thread operations (end of season).
**At ThS 0:** Character cannot practice. To reach ThS > 5 from 0 requires **3 clean seasons** (+2/season: 0→2→4→6). Three seasons = ~12 sessions of no Thread operations.

### Degradation Rate to ThS 0
Starting at ThS 20. Per batch 02 test B2-012, typical operation sequence:
- Each Object/Personal operation: −1 ThS (temporal auto-effect)
- Each Relational+: −1 ThS (auto) + degree-table losses
- FR or Past-Oriented: −2 or −3 additional

**Active practitioner (1 Relational operation/session, 4 sessions/season):**
- Each Relational operation: ThS −1 (auto) + Partial degree −1 = ~−1.5 average per operation.
- Per season: 4 operations × 1.5 = −6 ThS. Recovery at season end (no-practice): +2.
- Net per active season: −4 ThS.
- Sessions to ThS 0 from 20 at this rate: 20 ÷ 4 = **5 seasons = ~20 sessions.**

**Heavy practitioner (FR/Past-Oriented use):**
- FR operation: −2 auto + degree-table −2 (partial) = −4 per FR.
- 2 FRs per season: −8 from FR alone. Net: −6/season.
- Sessions to ThS 0: ~13 sessions.

### Findings
**F59 — ThS 0 recovery is campaign-disrupting:** Three seasons of no Thread work to exit Crisis. In a 30-session campaign, this is 12 sessions of mandatory inactivity — 40% of campaign length. A practitioner who hits ThS 0 mid-campaign is effectively retired unless the GM compresses recovery timing. No accelerated recovery option exists (cannot purchase with CP; no Einhir technique listed).

**F60 — No ThS degradation warning system:** ThS is a campaign-arc resource that tracks across sessions. Like Coherence, there is no moment-to-moment warning before threshold crossings. A practitioner can enter Fragmented (15), Fractured (10), or Severed (5) bands mid-operation with no opportunity to abort. Each band entry fires a Fallout roll — surprise narrative disruptions from what felt like a routine operation.

**Severity:** F59 = P2 (campaign-disrupting recovery; consider whether an Einhir technique for accelerated ThS recovery should exist). F60 = P2 (threshold opacity — recommend ThS be tracked as player-visible at session open).

---

## TEST B3-005 — TT Terminal: Clock at 80 and 100
**Coverage:** M-030 | TTRPG/BG | FUT | TT, TC, IP | All | — | — | Multiple

**Mode D — Terminal Value**

### TT Thresholds (§7.1, not yet scanned — reconstructing from cross-references)

From cross-references found in Batch 02 and 03 scans:
- TT > 45: TC +1/season; IP +1/season (§7.4)
- TT > 60: TC +2/season total; IP +2/season total (§7.4)
- TT ≥ 60: Weaving failure creates Shifting Objects (§5.4)
- TT ≥ 80: Weaving failure creates Gaps (§5.4); Gaps open upon monstrous entity defeat (§5.13)
- TT = 100: Campaign event (presumed — not directly confirmed from scan)

**[FLAG: TT full threshold table at §7.1 not scanned. Proceeding from cross-references only. Recommend §7.1 read for complete threshold list.]**

### TT 80 State Analysis

At TT 80, **every failed Weaving** creates a Gap. Probability of failed Weaving:
- Practitioner with 12D pool, Ob 3 (Relational scale), TN7: P(failure, net ≤ 0) ≈ 3%.
- At TN8 (Desperate): P(failure) ≈ 15%.
- Under Fractured conditions (+1 Ob all Thread ops): Ob 4. P(failure, 12D TN7 Ob 4) ≈ 12%.

**At TT 80, every Fractured practitioner's Weaving has ~12% chance of opening a new Gap.**

Each Gap: TT +4/season passive. At TT 80 with 2 Gaps open: +8 TT/season passive. TT reaches 100 in < 3 seasons from passive drift alone.

### Clock Acceleration Cascade at TT 80+
```
TT 80 → Gap formation risk from every failed Thread op
       → Each new Gap: +4 TT/season passive
       → TC +2/season (TT > 60 condition)
       → IP +2/season (TT > 60 condition)
       → TC 60+: IP +2/season additional
       → All three clocks above midpoints: ENDGAME phase
```

This is a cascade with no mechanical brake. Once TT reaches 80, the only stabilisation paths are:
1. Close all Gaps (FR Dissolution at appropriate scale — but FR failures at TT 80 create new Gaps)
2. Stop all Thread operations entirely
3. Overwhelming Weavings at TT −1 per Overwhelming (Relational+)

**F61 — TT 80+ creates a self-reinforcing failure state:** At TT 80, the tools that could lower TT (Weaving at Relational+) carry increasing risk of creating the thing that raises TT fastest (Gaps). A practitioner attempting to stabilise at TT 80 under Fractured conditions has ~12% chance per Weaving attempt of making things worse. This is not runaway by accident — it is the Calamity mechanic operating as designed (P-07: Calamity = rendered-side failure). But players may not have a viable stabilisation path at TT 80+ without TS 70+ practitioners in good ThS condition.

**Severity:** F61 = P2 (escalation may be unwinnable without specific high-TS characters — confirm design intent).

---

## TEST B3-006 — TC Terminal: Theocracy Clock at 80 and 100
**Coverage:** M-031 | TTRPG/BG | FUT | TC, TT, IP | Church, Crown, Hafenmark | — | Himlensendt, Baralta | Faction Leader

**Mode D — Terminal Value**

### TC 80 — Church Territorial Seizure
Per §7.2: "At TC 80, the Church may attempt to seize territories through institutional claim rather than military force. Per-territory roll vs variable Ob."

**Seizure roll:** Church Mandate (5→7 by mid-campaign) + Influence dice. Against Ob = territory Fortification + controlling faction Mandate ÷ 2.

Example: Church seizes Himmelstift (T3, which Church already controls — trivial). Contested: Hafenstadt (T6, Hafenmark controls, Fort 1, Mandate 4 → Ob 2 + 1 = Ob 3).

Church pool: Mandate 7 + Influence 6 = institutional pool. NPC roll: 7D (Mandate) TN7 Ob 3. Expected net ≈ 2.3. P(≥3) ≈ 57%. **Church has moderate success rate on Territorial Seizure even against defended regions.**

Baralta's Sovereign Authority Doctrine (§13.3): usable once per campaign arc. On Overwhelming: TC −3, Church Mandate −1. This is the primary structural brake.

### TC 100 — Holy State
"Confessor Himlensendt declares Valoria a Holy State under Church governance."

This is a campaign event — narrative resolution, not a mechanical continuation. No "TC 101" state exists. TC 100 is a loss condition (or a unique victory condition for Church-aligned campaigns).

**Rate to TC 100 from start (TC 22):**
Passive drift: +1/season (Church Mandate ≥7). 
TT > 45: +1/season. TT > 60: +2/season (total).
TC 40+: The Ultimatum threshold — formal demand placed. This is TC's major narrative escalation.

From TC 22 to 100 = 78 points. At 2/season average: **39 seasons = ~156 sessions.** This is unreachable in a normal campaign without Church player actively accelerating. At aggressive acceleration (TC 80 Territorial Seizure + multiple heresy convictions): possible in ~20–25 seasons.

**Baralta as structural brake:** While Baralta's Mandate > 5: TC suppressed −1/season. This is significant — effectively negates one source of passive TC rise. Baralta excommunicated (TC +4 immediately) removes the brake permanently.

### Findings
**F62 — TC 100 is effectively unreachable without player mistakes:** At 2/season drift, TC takes 39 seasons. Even at aggressive Church play, TC 100 requires approximately 25 seasons. This means TC is a pressure mechanic, not a countdown — the threat is real but the clock rarely fires unless players actively ignore it. The TC 40 threshold (The Ultimatum) is the realistic pressure point, achievable in ~9 seasons.

**F63 — Baralta excommunication is TC's catastrophic accelerator:** Excommunication removes −1/season brake AND adds +4 immediately = net +5 TC swing. If Church excommunicates Baralta (TC + heresy investigation +2 → +4 total), TC jumps and loses its primary suppressor permanently. This is the highest-leverage single event on the TC track.

**Severity:** F62 = P3 (intended — TC is pressure, not countdown). F63 = P2 (excommunication event has asymmetric TC impact — confirm this is intentional and documented for GMs).

---

## TEST B3-007 — NPC: Ehrenwall Coup Threshold Mechanics
**Coverage:** M-034, M-035 | TTRPG | FUT | FSTAT, TLK | Crown, Löwenritter | Ehrenwall, Almud, Torben | Faction Leader, Löwenritter Knight

**Mode C — Scenario**

### Coup Trigger Conditions (from §13.5)
Ehrenwall has not yet concluded the Crown has failed. Two explicit triggers referenced:
- Coup trigger #2: Almud surrenders the heir (Torben) to Altonia.
- Coup trigger #2 (second reference): Torben's loyalty reaches 3–2 (Altonia-aligned).

**[FLAG: Only "coup trigger #2" is referenced in both Ehrenwall and Torben sections. Coup trigger #1 not specified in scanned NPC text. Requires §13.5 full scan or GM Tools reference.]**

### Scenario: IP Reaches 30, Tutoring Demand Active

**State:**
```
IP 32 | TC 28 | TT 45
Torben Loyalty: 8 (homesick, resistant)
Crown Mandate 5 | Löwenritter Military 5
Ehrenwall: monitoring — coup threshold not yet met
```

**Crown response options:**
1. Comply with tutoring demand → Torben goes to Altonia. Loyalty clock starts ticking.
2. Refuse → IP escalation (+2 per season of refusal?). Covert contact required for extraction instead.

**Option 1 — Torben sent:**
Torben Loyalty: 8 → decays per season in Altonia. Rate not specified in scanned text. Assume −1 per season.

At Loyalty 5–4 (Adapting): Crown Mandate −1. Retrieval requires Altonian consent or covert extraction.
At Loyalty 3–2 (Altonia-aligned): Crown Mandate −1 again (cumulative −2). Coup trigger #2 arguably met.

**Coup resolution (if Ehrenwall acts):**
Löwenritter Military 5 vs Crown Military 4. BG mode: single roll. P(Löwenritter wins in open field) ≈ 58%. In Ehrenfeld (Fort 3 garrison): Crown at 4+0 = 4D, Löwenritter at home base. Ehrenwall's Löwenritter control Ehrenfeld (T5) — they don't need to assault Crown territory, they need to occupy Valorsplatz.

Path to Valorsplatz from Ehrenfeld: T5 → T1 (adjacent). One march action. Crown Mandate 5 → if Mandate has dropped to 3 (−2 from Torben loyalty): P(Parliamentary resistance to coup) reduced significantly.

### Findings
**F64 — Coup trigger #1 is undocumented in NPC text:** Ehrenwall NPC entry references "coup trigger #2" twice but trigger #1 is never stated in scanned text. Players and GMs need to know what Ehrenwall is counting. If trigger #1 is implied from Belief 2 ("Almud is surrendering sovereignty incrementally. I am keeping count"), a quantified threshold is needed.

**F65 — Torben loyalty decay rate not specified:** §13.1 lists Loyalty thresholds and their effects but not the rate of decay per season in Altonian custody. GM must improvise. Given the Loyalty clock is a key campaign pressure mechanic, its tick rate should be defined.

**Severity:** F64 = P2 (missing trigger definition). F65 = P2 (missing clock rate).

---

## TEST B3-008 — NPC: Lenneth Scholarly TS Path
**Coverage:** M-008 | TTRPG | PAST | TS, TC | Crown, Revolution | Lenneth | Non-TS Scholar

**Mode C — Scenario**

### Setup
Lenneth (TS 0, Inert; "simply never confronted") has access to a pre-Altonian coastal survey that a TS 50+ practitioner would recognise as a first-person thread-perception account (~180 years old).

**Scholarly TS Path (§4.4):** A character with access to Einhir scholarship and no essentialist theological Belief may pursue TS growth through intellectual engagement. Qualifying events are scholarly — deep study, temporal anomaly analysis, Originary inscription decoding. Spirit check TN7 Ob1 required.

**Lenneth's Spirit score:** Not specified in §13.1. Assume Spirit 4 (typical non-practitioner noble).

### Sequence
1. Lenneth studies the pre-Altonian coastal survey (qualifies as scholarly Thread-related text under Scholarly TS Path).
2. Spirit check TN7 Ob1: Spirit 4 pool. P(≥1 net) ≈ 88%.
3. Success: +5 TS. Lenneth: TS 0 → **5**. Still Inert (range 0–9); no mechanical change yet.
4. Continued engagement: next qualifying event → Spirit check → if Lenneth reaches TS 10: Dormant. Passive awareness begins.

**[FLAG: Scholarly TS path says qualifying events are "scholarly rather than experiential." But §4.4 specifies "The Spirit check is still required — intellectual understanding alone does not produce sensitivity." Does the Spirit check threshold (Ob1) apply equally to scholarly path? Yes — same rules, different trigger events.]**

### TS Growth to Dormant: How Long?
- Each qualifying scholarly event: +5 TS on success (88% chance).
- TS 0 → 5 → 10 (Dormant): 2 qualifying events.
- TS 0 → 10 in 2 events. If one event per session: **2 sessions to Dormant.**
- Dormant → Stirring (TS 30): 4 more events = 4 more sessions.
- Total: ~6 sessions for Lenneth to reach TS 30 (Stirring) via scholarly path, assuming she pursues it actively.

**TC implications:** Lenneth at Stirring TS 30 is the Queen of Valoria. Her Thread sensitivity would be the most politically explosive secret in the kingdom. Church discovers Queen is a practitioner → TC +1 per public Thread event, heresy investigation risk.

### Findings
**F66 — Lenneth scholarly path is extremely fast:** 6 sessions to TS 30 with 88% success rate per qualifying event. This is faster than most confrontation-based TS paths (which require rare qualifying events). Lenneth has regular access to scholarly material through her foundation network. She could become a full practitioner within 2–3 campaign seasons while maintaining plausible deniability.

**F67 — No Devout Constraint blocks Lenneth's TS growth:** Lenneth's Belief is Liberty (political, not theological). No essentialist theological Belief. The Scholarly TS path is fully available to her. She is the only Crown character without a theological barrier to Thread sensitivity.

**Severity:** F66 = P3 (intended — scholarly path is designed as a viable route). F67 = P3 (intentional — Lenneth's political beliefs enable what Baralta's theology forecloses).

---

## TEST B3-009 — NPC: Baralta Sovereign Authority Doctrine
**Coverage:** M-036, M-037 | TTRPG | PRES | TC, FSTAT | Hafenmark, Church | Baralta, Himlensendt | Faction Leader

**Mode C — Scenario**

### Setup: TC 44 (The Ultimatum — formal Church demand before Parliament)

Baralta invokes Sovereign Authority Doctrine (§13.3) to contest Church supremacy claim.

**Roll:** Mandate 7 + Reach 5 dice (pool = 12D) vs Ob 4 (Church Reach).
TN7. Expected net ≈ 4.0. P(≥4) ≈ 62%. P(Overwhelming ≥8) ≈ 22%.

| Degree | P | Consequence |
|--------|---|-------------|
| Overwhelming (≥8) | 22% | TC −3, Church Mandate −1, Heresy Investigation Ob 4 to pursue, Baralta +1D vs Church for arc |
| Success (≥4) | 40% | TC −2, Church Mandate −1, Heresy Investigation opens (Ob 4) |
| Partial (1–3) | 25% | TC −1, Heresy Investigation opens immediately, Church Reach +1 |
| Failure (≤0) | 13% | TC +1, Heresy Investigation opens immediately, Baralta Mandate −1 |

**Expected TC change:** 0.22 × (−3) + 0.40 × (−2) + 0.25 × (−1) + 0.13 × (+1) = −0.66 − 0.80 − 0.25 + 0.13 = **−1.58 expected TC.**

**Expected Heresy Investigation launch:**
- Partial or Failure: guaranteed launch. P(Partial + Failure) = 38%. 
- Success: Heresy Investigation opens at Ob 4 (hard to advance). P(Success) = 40%.
- Overwhelming: Heresy Investigation cannot advance this season (explicitly blocked).

**Expected outcome:** Baralta invokes → TC decreases by ~1.6 expected. But Heresy Investigation launches ~78% of the time (all non-Overwhelming results). A Heresy Investigation against a sitting noble is TC +2 (§7.2 TC Rise Sources). **Using Sovereign Authority has ~78% chance of triggering the very mechanism that raises TC.**

### Findings
**F68 — Sovereign Authority is a net-zero or worse TC action in expectation:**
- Expected TC from invoking: −1.58 (from the action itself)
- Expected TC from Heresy Investigation trigger: +2 × P(investigation opens) = +2 × 0.78 = +1.56
- **Net expected TC from invoking Sovereign Authority: −1.58 + 1.56 ≈ −0.02**

Baralta's ultimate anti-Church tool is roughly TC-neutral in expectation. It is only clearly beneficial on Overwhelming (22% chance, −3 TC with investigation blocked). On all other results, the TC reduction is partially or fully offset by the Heresy Investigation.

**F69 — Sovereign Authority is limited to once per campaign arc:** Given the near-neutral expected value, the once-per-arc limit means players are unlikely to use it early and may hold it for a critical moment — but the math suggests they should only invoke it when the Heresy Investigation opening is manageable (i.e., Crown can defeat the Inquisition procedure before it advances).

**Severity:** F68 = P2 (dominant Baralta tool is near-TC-neutral — confirm this tradeoff is intentional and that players are expected to understand the Heresy Investigation linkage).

---

## TEST B3-010 — NPC: Vaynard Thread Investigation Track
**Coverage:** M-035 | TTRPG | FUT | TC, TS, FSTAT | Varfell, Church | Vaynard | Non-TS Scholar

**Mode C — Scenario**

### Vaynard TK Track (0–5)
TK 3: succession leverage formally linked to Southernmost access. TC +1.
TK 5: knows what Galbados was structurally. TC +3 cumulative.

**TK Advancement:** Governed by what Vaynard discovers. No explicit roll specified — GM-driven based on information players provide or withhold.

### Scenario: Players Share Thread Information with Vaynard

Players (practitioners, TS 50+) demonstrate a Thread operation to Vaynard in private. This constitutes a Discovery Event for Vaynard (TS 14 Dormant).

**Discovery Event → Spirit check TN7 Ob1:** Spirit score not listed for Vaynard in §13.4. Assuming Spirit 4.
P(success) ≈ 88%. Success: TS advances to **30** (Stirring). "The world reorganises itself for him."

**Immediate consequences:**
- Vaynard TS 30: Dormant → Stirring. He now perceives active Thread operations in his vicinity.
- Vaynard still lacks Approach Training — cannot Leap.
- TC +1 (TK advancement from direct Thread witness pushes TK toward 3–4).
- Vaynard's Belief #2 accelerates: "I will know what they are hiding." He now knows Thread operations are real from direct experience.

**TK advances to 3–4 from this event:** Succession leverage formally linked to Southernmost access terms. Varfell's position hardens.

### Findings
**F70 — Sharing Thread knowledge with Vaynard immediately escalates TC:** Players who try to recruit Vaynard as an ally by demonstrating Thread operations trigger: TK advancement → TC +1 immediately, TC +2 eventually (TK 5). There is no "inform Vaynard without TC cost" path. Recruiting Valoria's most intellectually capable ally accelerates the Church's structural conquest.

**F71 — Vaynard's Discovery Event is player-triggerable:** Players can choose when to trigger Vaynard's Discovery Event by demonstrating operations in his presence. This gives players control over when his TS jumps to 30 — and thus when the TC consequences land. Strategic timing is available.

**Severity:** F70 = P2 (ally recruitment has TC cost — should be clearly communicated as a faction tradeoff). F71 = P3 (intentional player agency).

---

## TEST B3-011 — NPC: Klapp — Church Scholar with Developing TS
**Coverage:** M-008, M-049 | TTRPG | PAST | TS, CE, TC | Church | Klapp, Olafsson | Non-TS Scholar

**Mode C — Scenario**

### Klapp's Current State (§13.2)
- TS 31 (Stirring, unknown to anyone)
- CE 4 (from archive work with Originary Locks)
- "One more sustained encounter with a Thread-significant object will trigger a TS growth check."
- "If it succeeds: the head of the Church's entire educational apparatus develops Thread sensitivity."

### Scenario: Klapp handles a submitted Einhir text

Discovery Event triggers automatically. Spirit check TN7 Ob1. Spirit score not listed; assuming 4.
P(success) ≈ 88%. Success: TS +5 → TS 36.

**Consequences:**
- Klapp TS 36: still Stirring, but now perceives active Thread operations in the same scene.
- Klapp has access to Einhir texts (his archive). If he reads a primary Einhir text: +5 TS per text (§5.16). At TS 50+ he would perceive Thread operations in the same building.
- CE 4 + this event: CE 5 (handling Originary Lock-adjacent material). **CE 5 threshold?** Inquisitor CE thresholds go to 3; Riskbreaker CE to 3. No CE 5 defined in scanned text.

**[FLAG: CE track for Church scholars not fully defined. §13.2 mentions Trajectory B (Fracture) and C (Conversion) at CE 4 for Klapp, but CE thresholds above 3 for non-Inquisitor roles are not specified in §13.6 Inquisitor section.]**

**Theological Dissonance Event (Devout Constraint):**
Klapp is a Church Cardinal. Is he Devout (essentialist theological Belief)? §13.2 doesn't explicitly state. If Devout: Discovery Event → Theological Dissonance Event immediately → Spirit check TN7 Ob1. Failure: Dissonance Mark. At 3 Marks: Devout Constraint collapses.

**If not Devout:** Klapp develops TS freely. Within 3–4 scholarly encounters, could reach TS 50 — full practitioner. The head of the Church's educational apparatus would perceive Thread operations in the same building as him. Every Inquisitor operation, every interrogation, every heresy conviction — Klapp would sense it all.

### Findings
**F72 — Klapp's TS development is a structural Church crisis:** Klapp controls Church universities and the archive of Einhir texts. His TS development means the Church's gatekeeper of Thread-related materials becomes Thread-sensitive. He would recognise what he has been suppressing. The Conversion trajectory (CE → TC crisis) is the most destabilising Church-internal event in the campaign.

**F73 — CE track above 3 undefined for non-Inquisitor roles:** Klapp's CE 4 puts him above the defined Inquisitor CE threshold (3). No CE 4–5 effects defined for Church scholars. The Trajectory B/C descriptions in §13.2 are narrative but lack mechanical anchors.

**Severity:** F72 = P3 (intentional campaign event). F73 = P2 (CE track incomplete for non-Inquisitor characters).

---

## TEST B3-012 — NPC: Elske Recruitment Across Factions
**Coverage:** M-011, M-037 | TTRPG | PRES | FSTAT, IP | Crown, Varfell, Revolution | Elske | Faction Leader

**Mode C — Scenario**

### Setup
Elske: married to Altonian Duke, in Altonian territory, not working for any faction. Recruitable via Circles Ob 3 + Appeal/Debate (3 exchanges) targeting Family or Self-Determination conviction. Resonant Style: Evidence.

### Scenario A: Crown Recruits Elske to Extract Torben

**Circles to reach Elske in Altonian territory:**
Pool: Presence + History. Assumed Crown diplomat Presence 5, "Altonian Court Connections" History 3 pts → 5 + 6 = 11D. Ob 3 (secretive; in hostile territory). TN7. P(≥3) ≈ 87%.

**Social Scene (3-exchange Debate):**
Target: Family conviction. Evidence Style required (her Resonant Style).
GM must present concrete proof about Torben's situation.

Crown diplomat pool: Cognition 4 + "Diplomatic Service" History 3 pts = 4 + 6 = **10D**. Ob calibrated from Elske's Disposition. Elske is neutral-to-cautious (Neutral, Ob 2 baseline). Evidence Style match: no mismatch penalty.

Elske NPC pool: Not specified. Assuming Cognition 5 (Noble, educated), no relevant History → 5D.

**Exchange 1:**
Crown: 10D TN7 vs Ob 2. P(Success) ≈ 93%.
Elske NPC: 5D TN7 vs Ob 2. P(Success) ≈ 67%.
Crown likely wins exchange 1. Elske Composure strain +1.

**After 3 exchanges (most likely: Crown wins 2–1 or 3–0):**
2–1 Crown win: Elske partially persuaded. Player must offer something concrete (information about Torben's actual loyalty erosion, or a promise of genuine independence post-return).
3–0: Elske persuaded; Disposition → Warm. Will act.

### Scenario B: Revolution Recruits Elske for Intelligence Access

Revolution appeals to Self-Determination: "You could matter as an agent of genuine change, not a dynastic piece."
Evidence Style required — Revolution needs concrete proof of what they can offer her agency-wise.

Revolution pool: Influence 3 + Cognition of NPC operator. Much weaker than Crown (pool ~7D). Ob 2. P(Success per exchange) ≈ 83%. Still likely to win a 3-exchange Debate but needs more successes.

**Faction conflict:** If Crown AND Revolution both approach Elske in the same season, she must adjudicate competing offers. No mechanic for "NPC receives simultaneous faction recruitment" is specified.

### Findings
**F74 — Elske is highly recruitable by multiple factions simultaneously:** High Circles success rate + moderate Debate Ob means most competent factions can reach and persuade Elske. No mechanic prevents multiple factions from successfully recruiting her in the same season.

**F75 — Simultaneous recruitment → undefined NPC response:** If Crown and Revolution both succeed on their recruitment Debates in the same season, who does Elske work for? No NPC adjudication procedure for contested recruitment exists. GM must resolve narratively.

**Severity:** F74 = P3 (intentional — Elske is a contested resource). F75 = P2 (contested recruitment procedure absent).

---

## TEST B3-013 — NPC: Himlensendt Originary Lock Encounter
**Coverage:** M-014, M-051 | TTRPG | CROSS | TS, TC, CERT | Church | Himlensendt | Devout Character

**Mode C — Scenario**

### Setup
Players arrange for Himlensendt to handle one of the Church's own Originary Locks during a restricted ceremony. (The Locks are Church property — §13.2 states Cardinals who handled them subsequently requested to be relieved.)

**Originary Lock handling (§5.12 Category Two):**
- Requires TS 50+ to "work" — Himlensendt (TS 0) cannot perform operations on it.
- But handling for one full scene: "+10 TS gain immediately" — this is not gated on TS 50+. The experience is available to any character who handles it for a scene.
- Spirit check TN8 Ob = current Wounds + 1 (= Ob 1 for undamaged Himlensendt). Failure: 2 Wounds, armour does not apply.

**Himlensendt handling Originary Lock:**
- Spirit score: not listed. Assuming Spirit 3 (theology-focused, lower resilience).
- Spirit check TN8 Ob1: 3D at TN8. P(die ≥8) = 0.3. P(≥1 net, 3D TN8): 1 − (0.7)³ = 1 − 0.343 = **66%.**
- Success: +10 TS. Himlensendt: TS 0 → **10** (Dormant). No Wounds.
- Failure (34%): 2 Wounds. TS still +10.

**Devout Constraint activation:**
Himlensendt TS now 10 (Dormant). His Belief is: "The Church must complete Galbados's mandate." Essentialist theological Belief → Devout Constraint active.

Dormant TS (10–29) provides: passive awareness of wrongness near Gaps, Shifting Objects, low-Intelligibility practitioners. Himlensendt now **passively detects Thread activity** in his vicinity, against his theology.

**Theological Dissonance Event fires immediately** (Discovery Event triggered):
Spirit check TN7 Ob1: 3D. P(success) ≈ 73%.
- Success (73%): Framework holds. Certainty −1. He attributes the experience to divine revelation.
- Failure (27%): Framework cracks. **Dissonance Mark 1.** Certainty −2.

### The Cardinals Who Left (§13.2)
"Three Cardinals who handled these objects during restricted ceremonies subsequently requested to be relieved of their duties."

This suggests the standard Originary Lock handling outcome for TS-0 individuals is: +10 TS → Dormant awareness → Dissonance Mark cascade → framework collapse → too destabilised to continue. The Dissonance Mark trajectory (3 Marks → Devout Constraint collapses) would unfold over subsequent Discovery Events.

### Findings
**F76 — Originary Lock as targeted Devout disruption tool:** Players can use the Church's own sacred objects as weapons against Devout characters. Arranging for Himlensendt to handle a Lock triggers his TS development, Dissonance Marks, and eventually Devout Constraint collapse — all without direct Thread operations on him (which would trigger F25/F43 concerns). This is a canonical, non-coercive path.

**F77 — +10 TS from Originary Lock is not gated on existing TS:** Any character, including TS 0 characters, gains +10 TS from handling. A Crown diplomat who "accidentally" handles a Lock in the archive becomes Dormant. This is a powerful uncontrolled vector for TS spread.

**Severity:** F76 = P3 (intentional — the Church's own objects are its vulnerability). F77 = P2 (TS spread vector from Locks is uncontrolled — confirm any characters with archive access are at risk).

---

## TEST B3-014 — NPC: Olafsson-Niflhel Evidence Chain
**Coverage:** M-049, M-050 | TTRPG | PAST | TC, FSTAT, DD | Church, Niflhel, Crown | Olafsson, Baralta | Inquisitor, Riskbreaker

**Mode C — Scenario**

### Setup
Baralta holds circumstantial evidence of Olafsson-Niflhel connection. Players supply Solvind Brak's testimony.

**Baralta's Domain Action (§13.2):**
Pool: Mandate 7 + Reach 5 + player evidence bonus (assume +2D for strong testimony) = **14D**.
Ob 3 vs Church Stability.
TN7. Expected net ≈ 4.6. P(≥3) ≈ 93%. P(Overwhelming ≥6) ≈ 75%.

**Most likely outcome (Success or Overwhelming):**
- Church Stability −2 (immediately, before seasonal cap — this is an event-driven change, not seasonal drift).
- TC −3 (explicitly stated). TC: 33 → **30**.
- Olafsson's Inquisitor operations suspended.

**Church Stability at 5 − 2 = 3:** Below the anti-death-spiral floor trigger (Stability 2). Still above floor. But Stability 3 at next Stability check (Ob 2, active threat): 3D TN7 Ob2. P(failure) ≈ 33%. Failure: Stability → 2. At Stability 2: floor activates (treated as Ob 4 regardless of actual pressure).

### Riskbreaker Deniability Debt
If players used Riskbreakers to obtain the testimony: each exposed covert operation → Debt +1.
Obtaining Brak's testimony covertly: likely 1–2 Riskbreaker operations. Debt: 0 → 1 or 2.

At Debt 3: Crown Domain Actions vs non-Crown factions +1 Ob (Parliament trust erodes).
At Debt 5: Parliamentary inquiry → Grand Debate (5 exchanges), Crown Mandate and Reach at stake.

### Findings
**F78 — Baralta action is high-value but one-shot:** Once Olafsson is exposed, this path is exhausted. The TC −3 and Stability −2 are among the largest single-action clock effects available to players. But Baralta is the only actor who can execute it (pool requires her specific stats), and it requires player-supplied evidence.

**F79 — Riskbreaker Debt accumulates toward Parliamentary crisis:** Using Riskbreakers to obtain evidence creates Debt that can trigger a parliamentary crisis. Players who use covert methods to achieve the most effective Church-weakening action simultaneously jeopardise Crown legitimacy. A clean win here is not available.

**Severity:** F78 = P3 (intended — high-value one-shot). F79 = P2 (Debt-building tradeoff should be player-visible before committing operations).

---

## TEST B3-015 — Grand Debate: 5-Exchange Probability Distribution
**Coverage:** M-037 | TTRPG | PRES | TC, FSTAT | Church, Crown, Hafenmark | Himlensendt, Almud, Baralta | Faction Leader

**Mode A — Isolation**

### Grand Debate Structure
5 exchanges. Both orators roll Cognition + History bonus simultaneously each exchange. Loser takes Composure strain (+1 normal loss, +2 Overwhelming loss).

### Matched Opponents: Baralta (Cognition 4, History 3 = 10D) vs Himlensendt (Cognition 5, History "Political Negotiation" 2 pts = 5 + 5 = 10D)

Each exchange: both roll 10D TN7. Net = 10 × 0.33 ≈ 3.3 expected.

**Per exchange:**
P(Baralta net > Himlensendt net) ≈ 50% (matched pools — symmetric).
P(Overwhelming win: winner net ≥ 2× loser net) ≈ 15% per exchange (rough estimate).

### 5-Exchange Distribution
With equal pools, expected outcome: 2.5–2.5 split (roughly symmetric). P(5-0 sweep by either side): extremely low (~3%).

**Composure consequences:**
- Each normal loss: +1 strain. 5 exchanges: possible +5 strain per character if they lose all.
- Himlensendt Composure 12. Losing all 5 exchanges: worst case +10 strain (5 Overwhelming losses). Still 2 below Rattled threshold.
- Baralta Composure 11. Same calculation: remains above Rattled at 5 normal losses.

**Grand Debate total loss (5–0):**
"Losing faction takes +1 Ob to social actions with opposing faction for one season."

P(5-0 loss for Baralta with equal pools): ≈ (0.5)⁵ = 3%. P(5-0 for Himlensendt): same 3%. Very rare — this is a catastrophe condition.

### Unmatched: Baralta at TC 60 (Church Mandate 7+, Himlensendt gets resonant style bonus)
Himlensendt's Resonant Style: Consequence. If debate is framed as future outcomes for the Church's mandate, his opponent addressing him in Consequence Style earns +1D. Himlensendt's effective pool in ideal framing: 11D vs Baralta's 10D.

P(Himlensendt wins exchange with 11D vs 10D): ~54%. Over 5 exchanges: P(Himlensendt wins 3+) ≈ 68%. Player should avoid framing debate as "what does this mean for the future" when facing Himlensendt.

### Findings
**F80 — Grand Debate between matched leaders is a coin flip:** Equal pools produce near-50/50 exchanges. The Grand Debate mechanic's outcome is dominated by variance at similar pool sizes. Strategic differentiation (Resonant Style exploitation, Inspiration attacks, Composure management) matters more than raw pool size.

**F81 — Composure rarely reaches Rattled in Grand Debate:** Composure thresholds (11–12 for named leaders) are too high for a 5-exchange debate to trigger Rattled on normal losses. Only Overwhelming-spam could deplete Composure. This makes Rattled a rare condition in formal Grand Debates — narrative pressure, but mechanical Rattled is an edge case.

**Severity:** F80 = P3 (variance is the point — Grand Debates are political gambles). F81 = P3 (intended — Rattled requires sustained domination).

---

## TEST B3-016 — Parliamentary Vote: Faction Pool Substitution
**Coverage:** M-036 | TTRPG/BG | PRES | FSTAT, TC | Crown, Church, Hafenmark, Varfell | Almud, Himlensendt, Baralta, Vaynard | Faction Leader

**Mode C — Scenario**

### Parliamentary Vote Structure (§9.6)
Parliamentary Votes use Debate exchange structure (best of 3 exchanges). Faction pools substitute for personal pools. Players may use higher of personal pool or faction pool.

### Motion: Church Supremacy Claim (Ultimatum, TC 40+)

**Church faction pool (Mandate/Reach):** Church Mandate 5, Influence 6. NPC institutional roll: 5D or 6D.
Himlensendt personal pool: Cognition 5 + Theology History 3 pts = 5 + 6 = **11D**. Higher of personal vs faction → Himlensendt uses 11D.

**Crown faction pool:** Crown Mandate 5. Almud personal: Cognition 5 + "Royal Policy" History → 11D. Equal — Crown uses 11D.

**Hafenmark:** Baralta personal 10D (Cognition 4 + Court Law History 3 pts). Higher than faction pool (Mandate 4D). Baralta uses 10D — sides with Crown.

**Varfell:** Vaynard's position depends on succession leverage. If Southernmost access not yet granted: Vaynard abstains or sides with Church conditionally.

**Vote alignment: Crown + Hafenmark (22D combined) vs Church (11D + allies).**

**[FLAG: Multi-faction Parliamentary Vote doesn't specify whether it's a simple coalition head-to-head or multi-party simultaneous roll. "Best of 3 exchanges" implies head-to-head. Who represents each coalition?]**

### Findings
**F82 — Multi-faction Parliamentary Vote has no multi-party resolution rule:** The Parliamentary Vote uses "best of 3 exchange" Debate structure. This works for two-party contests. For multi-faction votes (Crown + Hafenmark vs Church + NPC minor factions), the structure is undefined. Does the largest coalition member roll? Does the coalition pool combine? No rule specified.

**F83 — Named NPC personal pools dominate faction pools:** Every named NPC has personal pool (attribute + History) ≥ faction pool. Parliamentary Votes are decided by NPC personal capacity, not faction institutional strength, except for factions without named NPC leaders. This means having named NPCs present in Parliament is always better than relying on institutional capacity — NPCs with good social stats are the Parliament's decisive variable.

**Severity:** F82 = P2 (multi-party vote structure undefined). F83 = P3 (intended — individual leaders matter more than institutional weight).

---

## TEST B3-017 — Concealment: Hiding Operations from TS 30+ Observers
**Coverage:** M-052 | TTRPG | PRES | TS, CE | Church, Crown | — | Klapp | Practitioner, Inquisitor

**Mode A — Isolation**

### Concealment Roll (§5.2)
Roll: Cognition only (no History), TN7, Ob = observer's TS ÷ 30 (round up).

| Observer TS | Concealment Ob |
|-------------|---------------|
| 30–59 | Ob 1 |
| 60–89 | Ob 2 |
| 90–100 | Ob 3 |

**Success:** Reads as ambient Thread background.
**Failure:** Observer identifies practitioner as source and operation type.

### Case: Practitioner (Cognition 4) concealing from Klapp (TS 31)
Pool: Cognition 4 (no History). Ob = 31 ÷ 30 = Ob 2 (round up from 1.03).

Wait — "Ob = observer's TS ÷ 30 (round up)." TS 31: 31/30 = 1.03 → round up = Ob 2.
TS 30: 30/30 = 1.0 → round up = Ob 1.

4D TN7 Ob2. P(≥2 net): Expected net 1.3. P(≥2) ≈ 50%.

**Against Klapp (TS 31, just Dormant threshold):** 50% success rate on concealment. Klapp detects ~50% of operations performed in his presence.

### Case: Concealing from high-TS observer (TS 72)
Ob = 72 ÷ 30 = 2.4 → Ob 3. Pool 4D TN7. P(≥3 net) ≈ 25%. Only 1 in 4 concealment attempts succeed against a Sensitive practitioner.

### Findings
**F84 — Concealment Ob rounds up at TS 31:** The round-up formula means TS 31 is treated identically to TS 59 for concealment purposes (both Ob 2). There is no incentive for an observer's TS to be between 31–59 vs exactly 30 from the practitioner's perspective — the Ob is identical. Granularity is lost in the 30–59 band. This is a simplification that works at table but means Klapp (TS 31) is as hard to conceal from as a full Attuned practitioner (TS 59).

**F85 — No History applies to Concealment:** Concealment is Cognition only. This creates a flat cap on concealment quality. A practitioner with high Cognition (7) is moderately good at concealment (7D, P(Ob2) ≈ 83%) but cannot improve this through advancement beyond Cognition itself. Concealment cannot be a character specialty in the same way other operations can. Intentional (Thread operations cannot be hidden behind skill — only cognition matters)?

**Severity:** F84 = P3 (simplification works, minor loss of granularity). F85 = P2 (concealment non-advanceable beyond Cognition — confirm design intent).

---

## TEST B3-018 — Inquisitor Investigation: Full 3-Stage Procedure
**Coverage:** M-049 | TTRPG | PRES | CE, TC, FSTAT | Church, Crown | Olafsson, Klapp | Inquisitor, Practitioner

**Mode C — Full Scenario**

### State: Inquisitor investigating Maret Uln (practitioner, TS confirmed)

**Stage 1 — File Building**
Roll: Church Reach, Ob 3. Player obstruction at Ob 2.

If player obstructs (Riskbreaker operation to suppress evidence): Riskbreaker makes counter-roll. Church Reach 7D TN7 Ob3 vs Riskbreaker pool (assume 8D TN7 Ob2 for counter).

Church: P(≥3) using 7D ≈ 67%.
Riskbreaker obstruct: P(≥2) using 8D ≈ 86%.
Combined: Inquisitor succeeds and Riskbreaker fails to fully obstruct: P ≈ 67% × 14% = 9%. Obstruction mostly works (86% rate). Successful obstruction does not advance File but does add Deniability Debt +1.

**Stage 2 — Formal Accusation (requires completed File)**
Church Reach Ob 4. Accused may call Grand Debate (5 exchanges, Cognition + History pool).

Maret Uln (Cognition assumed 5, "Thread Research" History 4 pts = 5 + 7 = 12D) vs Church institutional pool (Reach 7D).
Maret wins with ~90% probability. Accusation collapses.

**BUT:** Calling Grand Debate at Stage 2 is public — it confirms Maret is under investigation. CE effects on Inquisitor: Stage 2 requires confronting Maret. Inquisitor encounters a practitioner at Stage 2 → CE +2 (direct witness to Thread operation if Maret uses contact during interrogation).

**Stage 3 — Conviction Hearing (Grand Debate finale)**
Identical to Stage 2 but framed as final verdict. Conviction: TC +2, imprisonment or exile.

### CE Accumulation on Inquisitor during this investigation:
| Event | CE |
|-------|-----|
| Reviewing physical evidence from Thread operation site | +1 |
| Interrogating Maret (who perceives the Inquisitor's threads) | +1 |
| Stage 2 confrontation with practitioner | +2 |
| Total | **CE 4** |

At CE 3: Inquisitor Cognition TN7 Ob2 for TS growth check (Ob 2, not Ob 1 — essentialist formation raises Ob). P(success, 5D TN7 Ob2): ≈ 67%. **Successful investigation of Maret likely produces an Inquisitor with developing Thread sensitivity.**

### Findings
**F86 — Investigation procedure produces CE accumulation as designed:** The three-stage procedure ensures any Inquisitor who successfully investigates a practitioner will hit CE 3 by Stage 2. TS growth check at CE 3 with 67% success rate. This is the Inquisitor Confrontation Arc operating correctly — the investigation produces the crisis of faith.

**F87 — Maret's Grand Debate pool trivially defeats institutional Church pool:** At Stage 2, Maret (12D) vs Church Reach 7D. P(Maret wins 3 of 5 exchanges) > 90%. The formal Accusation stage is essentially not a threat to a practitioner with high Cognition and relevant History. The investigation is dangerous not because of formal conviction risk but because of the CE/TS effects on the Inquisitor and the public exposure of being investigated.

**Severity:** F86 = P3 (intentional design). F87 = P2 (Accusation stage lacks mechanical bite vs high-Cognition practitioners — persecution is more about social/political exposure than conviction risk).

---

## TEST B3-019 — Riskbreaker Operations: Deniability Debt Escalation
**Coverage:** M-050 | TTRPG | PRES | DD, FSTAT | Crown, Church | — | Riskbreaker

**Mode A + D — Isolation + Terminal**

### Deniability Debt Track (0–5)

| Debt | Effect |
|------|--------|
| 3 | All Crown Domain Actions vs non-Crown factions: +1 Ob |
| 5 | Parliamentary inquiry: Grand Debate (5 exchanges), Crown Mandate and Reach at stake |

**Debt accumulation:** Each exposed covert operation: +1 Debt.

"Exposed": presumably when an operation fails and the opposition can identify the Crown's involvement, or when evidence is presented to Parliament.

**[FLAG: "Exposed operation" definition not specified. Is exposure automatic on Failure? Or does it require an opposing faction intelligence action to reveal? Debt accumulation trigger ambiguous.]**

### Debt 5 — Parliamentary Inquiry Grand Debate
Crown Mandate and Reach "at stake." This is the terminal event. 
Best-case for Crown: Almud (11D) wins all 5 exchanges. Mandate and Reach preserved.
Worst case: Church/Niflhel coalition presents evidence publicly. Grand Debate at +1 Ob if already at Debt 3 (Crown Domain Actions penalised → includes the defensive Grand Debate roll itself?).

**[FLAG: Does the +1 Ob from Debt 3 apply to the Crown's parliamentary debate at Debt 5? If yes, Crown defends a formal inquiry at −1D or +1 Ob — doubly penalised.]**

### Findings
**F88 — "Exposed operation" definition absent:** Deniability Debt's core mechanic requires knowing when an operation is "exposed." If exposure requires an opposing intelligence success, players can mitigate exposure through counter-intelligence. If exposure is automatic on Failure, every failed covert operation is a debt accumulator regardless of whether anyone discovers it. Mechanical difference is significant.

**F89 — Debt 3 Ob penalty may compound at Debt 5 inquiry:** If the +1 Ob from Debt 3 applies to all Crown Domain Actions including the defensive parliamentary debate, Crown is penalised during the very proceeding meant to resolve the Debt. Circular penalty — confirm whether the inquiry debate is subject to the Debt 3 modifier.

**Severity:** F88 = P2 (exposure trigger undefined). F89 = P2 (potential circular penalty at terminal state).

---

## TEST B3-020 — Combat Manoeuvres: Disarm and Trip Interaction Chain
**Coverage:** M-044 | TTRPG | PRES | — | Löwenritter | — | Ehrenwall | Löwenritter Knight

**Mode B — Interaction Chain**

### Scenario: Ehrenwall (12D combat pool) vs practitioner attempting a Leap

Practitioner declares: Thread Operation (Leap, Priority 5). Full-round action.
Ehrenwall declares: Manoeuvre → **Trip** (Priority 3A, resolves before attacks).

**Trip resolution (Priority 3A):**
Both roll Combat History pool (Agility vs Agility).
Ehrenwall: 12D. Practitioner: 6D (lower combat skill).
Expected net Ehrenwall ≈ 4.0 vs Expected net Practitioner ≈ 2.0. P(Ehrenwall trips) ≈ 78%.

**Trip effect:** Target prone: −2D attack, attacks vs prone +2D, double cost to stand.

**Leap eligibility while prone:**
"Not currently engaged in melee with an opponent who has declared an attack this round." Ehrenwall declared a Manoeuvre, not an attack — does the Leap eligibility condition apply? The Leap restriction is about attacks, not manoeuvres. A strict reading: Trip doesn't prevent the Leap.

However, prone condition (−2D to attacks) — does this apply to Thread operation pools? Thread pools (Attunement + History) are not attack pools. **Prone condition specifies "−2D attack" — Thread operation pools are not attack pools. Prone does not directly penalise the Leap roll.**

**BUT:** +1 Ob per Wound. If Ehrenwall follows Trip with an attack next round, the prone practitioner is at −2D defence, and attacks vs prone are +2D offence. A wound from the follow-up attack would add +1 Ob to the Leap.

### Priority conflict resolution:
- Round 1: Ehrenwall Trips (Priority 3A). Practitioner prone. Leap not yet executed (Priority 5 — later in round).
- Practitioner can still attempt Leap at Priority 5 while prone (no explicit restriction).
- Leap succeeds (say, 80% likely with reduced pool of 9D after −0D adjustment — prone doesn't penalise non-attack rolls).
- Round 2: Practitioner in Contact. Ehrenwall attacks prone practitioner (+2D bonus): 14D vs practitioner's prone defence (−2D, so 4D). Hit likely. Wound taken. Wound disruption check: Focus pool (Focus 4 = 4D TN7 Ob1). P(focus check passes) ≈ 88%. Contact maintained.

### Findings
**F90 — Prone condition does not penalise Thread operations:** "−2D attack" does not apply to Thread operation pools (which use Attunement + History, not Combat History). A tripped practitioner can still perform the Leap and Thread operations normally from prone. This is technically correct (Thread operations are not attacks) but feels incongruous — prone on the ground shouldn't be the optimal position for Thread operations.

**F91 — Manoeuvre-before-attack sequence allows disruption without Leap prevention:** Ehrenwall can Trip → then attack next round while practitioner is in Contact. Trip creates a wound-vulnerability that indirectly threatens contact via the Wound disruption check. Clever sequence, but requires 2 rounds. In Round 1, the Trip succeeds but doesn't stop the Leap.

**Severity:** F90 = P2 (prone not penalising Thread operations — consider whether prone should add +1 Ob to Thread ops). F91 = P3 (indirect disruption via wound setup — works as designed).

---

## TEST B3-021 — Faction Generic: Revolution (BG Mode)
**Coverage:** M-034, M-035, M-038 | BG | PRES | FSTAT, TT | Revolution | — | — | Faction Leader

**Mode C — BG Faction Turn**

### Revolution Faction Sheet (BG Mode)
Stats available: Influence 3, Stability 3, Intel (not listed as available — §8.1 "Revolution: Influence, Stability, Intel only").

**Intel stat not in starting values table.** Starting values show Revolution as "—" for Intel. But §8.1 says Revolution has "Influence, Stability, Intel only." Starting Intel = unstated.

**[FLAG: Revolution Intel starting value not in the faction table (§8.1 starting values). Either Intel starts at a value not listed or Revolution's Intel is defined elsewhere.]**

### BG Domain Actions Available to Revolution
Revolution has no Mandate (cannot issue royal decrees), no Wealth (cannot muster or bribe), no Military (cannot fight conventional battles). Limited to:
- Influence actions: political pressure, coalition building
- Stability actions: internal cohesion maintenance
- Intel actions: intelligence gathering, covert operations

**Revolution Unique Action:** Not confirmed in scanned text for Revolution specifically (§8.8 at line 2064 not yet read).

### Seasonal Accounting
Revolution Stability check (Ob 1 quiet season): 3D TN7 Ob1. P(success) ≈ 73%. P(failure → Stability −1) ≈ 27%. P(Overwhelming → Stability +1) ≈ 28%.

**Anti-death-spiral floor:** Stability 2 or lower → Ob 4 regardless. Revolution starting Stability 3 is only 1 step from the floor. Any Stability failure pushes them to the floor immediately.

### Findings
**F92 — Revolution is one failed Stability check from the anti-death-spiral floor:** Starting Stability 3. One quiet-season Stability failure (27% per season) reduces to Stability 2 → floor activates. The floor (Ob 4 regardless of threat level) means a weakened Revolution faces disproportionate Stability check difficulty. The anti-death-spiral floor was designed to prevent cascading collapse but for a faction starting at Stability 3, it's the first threshold they'll hit.

**F93 — Revolution Intel starting value absent from table:** Cannot run Intel actions for Revolution without this value. Gap in faction sheet.

**Severity:** F92 = P2 (Revolution structural fragility — likely intentional but confirm that Revolution's floor activation is an intended design feature). F93 = P2 (missing stat value).

---

## TEST B3-022 — Faction Generic: Niflhel (BG Mode)
**Coverage:** M-034, M-035 | BG | PRES | FSTAT | Niflhel | — | — | Riskbreaker

**Mode C — BG Faction Turn**

### Niflhel Faction Sheet
Stats: Influence 5, Wealth 4, Stability 4. No Mandate, no Military (§8.1).

**Niflhel Unique Action:** "Quiet Network" (−1 Ob in Schwarzmarkt T10 per territory map). Full Niflhel action mechanics at §8.7, not scanned. Proceeding from references.

### BG Niflhel Operations
Without Military: cannot contest territory through combat. Must use Influence (political pressure) and Wealth (economic) + Intel (not listed for Niflhel in §8.1 either — Niflhel has "no Mandate, no Military" but Intel status unspecified).

**Starting values table shows Niflhel Intel as "—"** — same gap as Revolution.

**[FLAG: Niflhel Intel value absent from starting values table. §8.1 states partial sheets for Niflhel ("no Mandate, no Military") but does not explicitly confirm Intel is available. §8.7 full text needed for confirmation.]**

### Niflhel as Spoiler Actor
Niflhel's campaign function: intelligence operations, economic disruption, operating through proxies (Olafsson connection). In BG mode, Niflhel's leverage comes from:
- Influence 5 (strong) → coalition disruption, factional information sales
- Wealth 4 → funding proxies, bribing, economic pressure
- Operating from Schwarzmarkt (T10): −1 Ob on Quiet Network operations

### Findings
**F94 — Niflhel Intel gap:** Same as Revolution. Intel starting value absent.

**F95 — Niflhel has no formal victory condition:** §8.7 text not scanned, but from context: Niflhel's faction goal is survival and influence maintenance, not conquest or institutional completion. In BG mode, victory conditions for non-territorial factions (Niflhel, Revolution) may be absent or purely GM-defined.

**Severity:** F94 = P2 (missing stat). F95 = P2 (BG victory condition for shadow factions undefined — may be in §8.7 or §12.2).

---

## TEST B3-023 — Faction Generic: Guilds Domain Actions
**Coverage:** M-035 | TTRPG/BG | PRES | FSTAT | Guilds | — | — | Faction Leader

**Mode A — Isolation**

### Guilds Faction Sheet
Mandate 3, Influence 4, Wealth 6, Military 2, Stability 5. No Intel listed.

**Guilds Unique Action:** "Trade" (inferred from territory bonuses — Sternhaven T7 "Trade orders +1D", Feldmark T11 "Muster Ob −1 willing recruits"). Full unique action at §8.6 not scanned.

### Wealth-Dominant Strategy
Guilds Wealth 6 is the highest in the game. Domain Actions using Wealth:
- Domain Ob: target faction's relevant stat ÷ 2, round up.
- Guilds Wealth 6D pool vs Hafenmark Wealth Ob 3 (Hafenmark Wealth 5 ÷ 2): P(≥3 net, 6D TN7) ≈ 45%.

**Trade action (inferred):** Wealth roll to gain economic control of territory or faction. Ethical Framework for Guilds not specified in scanned text — unknown modifier.

**Military 2 gap:** Guilds cannot defend territory conventionally. Military 2D pool TN5 (mass combat) vs any faction with Military 3+: P(Guilds wins) < 40%. Guilds must rely on alliance or proxy defense.

### Findings
**F96 — Guilds Wealth 6 dominates economic Domain Actions but cannot defend:** The highest Wealth faction cannot win military engagements. This creates a structural dependency: Guilds must politically neutralise military threats (through Influence, bribery, or coalition) or accept territorial vulnerability. The asymmetry is intentional but means Guilds victory requires sustained diplomatic management that can be disrupted by any military faction.

**Severity:** F96 = P3 (intended asymmetric faction design).

---

## TEST B3-024 — Faction Generic: Löwenritter Martial Law
**Coverage:** M-034, M-035 | TTRPG/BG | PRES | FSTAT, TC | Löwenritter, Crown, Church | Ehrenwall | Löwenritter Knight

**Mode C — Scenario**

### Löwenritter Stats
Military 5, Intel 3, Influence 3, Stability 5. No Mandate, no Wealth.

**Unique position:** Löwenritter garrison at Ehrenfeld (T5, Fort 3+, unique Fort 4 cap). This is the strongest single fortified position in the game.

**Martial Law Unique Action (from territory map: "Löwenritter Martial Law −1 Ob here"):**
Declared at Ehrenfeld. Effect: full territory military control, suppresses civilian unrest, can prevent faction entry.

### Scenario: Ehrenwall declares Martial Law at Ehrenfeld (T5)

**Roll (inferred):** Military 5D + Ehrenwall personal Cognition pool.
Ehrenwall Cognition not specified. Assuming Cognition 4 (military commander background). Pool: Military 5 + Commander Cognition 4 = 9D (or however Martial Law pool is constructed — unspecified).

**−1 Ob in Ehrenfeld:** Standard Ob −1. If Ob 2 normally: Ob 1.

**TC effect:** Löwenritter deploying without Crown authorisation = TC +2 (§7.2). Martial Law at Ehrenfeld without Crown authorisation would trigger this.
But: Löwenritter predates the Church in Valoria (§13.5). Ehrenwall may have grounds to argue Ehrenfeld is Löwenritter jurisdiction, not requiring Crown authorisation.

**[FLAG: Whether Löwenritter Martial Law at Ehrenfeld requires Crown authorisation for TC purposes is ambiguous. The Löwenritter's institutional independence claim and the TC trigger "without ducal or Crown authorisation" are in tension.]**

### Findings
**F97 — Löwenritter Martial Law TC ambiguity:** Declaring Martial Law in the Löwenritter's own garrison may or may not require Crown authorisation for TC purposes. Resolution depends on whether the GM rules Ehrenfeld as Löwenritter independent jurisdiction or Crown-delegated garrison territory.

**Severity:** F97 = P2 (authorisation ambiguity creates GM-dependent TC outcomes — recommend clarification in §8.9 Löwenritter).

---

## TEST B3-025 — IP Terminal: Invasion at 100
**Coverage:** M-032 | TTRPG/BG | FUT | IP, TT, TC, FSTAT | Crown, All | — | Almud, Ehrenwall, Torben | Multiple

**Mode D — Terminal Value**

### IP 100 — Invasion Campaign Event

"Altonian forces enter Valoria." (§7.3)

**Invasion force capability (inferred):** Altonia is a colonial power that previously occupied Valoria. Their military capacity exceeds any single Valorian faction. Likely Military stat ≥ 7 for invasion force.

**Cross-clock state at IP 100:**
- IP 100 requires IP drift from 20 (+80 points). Passive drift: +1/season. Cross-clock: TT > 45 adds +1/season; TC > 60 adds +2/season. At maximum acceleration: +4 IP/season.
- Minimum time to IP 100: 80/4 = **20 seasons** at maximum acceleration.
- Realistic: 40–60 sessions minimum.

**Invasion response options:**
1. United Valorian resistance: all factions align (TC < 40 required for Church cooperation; Crown Mandate ≥ 5 required; IP freeze possible via Grand Diplomatic Scene).
2. Surrender: Crown becomes Altonian vassal. Campaign ends.
3. Löwenritter lead resistance: Ehrenwall command + Martial Law + coalition.

**Schoenland (T15) at IP 75+:** "Altonian vanguard deploys here." Schoenland becomes a military staging point before IP 100. Sea route severed. Players lose −2 IP/year from Schoenland trade — permanently gone at IP 75.

### Findings
**F98 — IP 100 is effectively a background threat, not a realistic terminal:** Like TC 100, IP 100 requires 40–60 sessions at realistic drift rates. The real IP pressure is at IP 75 (vanguard deployment, sea route closure) and IP 60 (warlike: invasion preparations begin). These are the crisis points, not IP 100 itself. The terminal state is a loss condition that frames urgency but shouldn't fire in a typical campaign.

**F99 — No Altonian stats provided:** At IP 100, Altonian forces enter Valoria. Their Military, Martial, and Endurance stats for mass combat are not specified in scanned text. GM must improvise the invasion force.

**Severity:** F98 = P3 (intended background threat). F99 = P2 (invasion force stats absent — needed for when the terminal fires).

---

## TEST B3-026 — Intelligibility Terminal: 0 State
**Coverage:** M-020 | TTRPG | CROSS | INT, TS, CERT | — | — | — | Practitioner

**Mode D — Terminal Value**

### Intelligibility 0
"Reality as commonly rendered is no longer accessible to the character. Permanent condition unless reversed through specific Thread intervention. Character becomes an NPC unless reversed."

**Path to Intelligibility 0:**
- Each Relational+ operation: −1 Intelligibility.
- Forced Resolution (any scale): −1 Intelligibility.
- Past-Oriented Pulling: −1 additional.
- Extended proximity to Structural Gap: −1/season.

**From 10 to 0:** 10 reduction events. At 1 Relational operation/session: **10 sessions to Intelligibility 0.**

### Intelligibility 0 Recovery
"Reversed through specific Thread intervention." Three paths:
- Full season of non-practice: +1 Intelligibility (passive recovery from 0 → 1 is possible).
- Anchoring Scene with Close Knot (Bonds check TN7 Ob2): +1 Intelligibility (at Knot +1 strain cost).
- "Certain Einhir techniques (GM discretion, late-campaign): +1–2."

Wait — does passive recovery (+1 per non-practice season) work at Intelligibility 0? Text says "Intelligibility does not recover passively. Recovery requires: Full season of non-practice (no Thread operations): +1." This IS passive recovery — it just requires the condition of non-practice. So Intelligibility 0 recovery is possible at +1/season of non-practice.

**BUT:** At Intelligibility 0 the character "becomes an NPC unless reversed." If the character is already an NPC when passive recovery starts, who decides to keep them in a non-practice season? This is a GM problem, not a player problem.

**Findings**
**F100 — Intelligibility 0 → NPC transition creates recovery paradox:** The character becomes an NPC at Intelligibility 0. Recovery requires non-practice seasons (+1/season). But if the character is an NPC, the player has no agency to choose non-practice. Recovery requires GM agency on behalf of a character the GM now controls. This is the designed tragic arc, but it means player-driven recovery from Intelligibility 0 is mechanically unavailable — only GM mercy can restore them.

**F101 — Rate to Intelligibility 0 is fast:** 10 operations at Relational+. An active practitioner performing 2–3 operations per session would reach Intelligibility 0 in 4–5 sessions of heavy Thread use. **This is within a single campaign arc.** Intelligibility is the fastest terminal track to reach 0.

**Severity:** F100 = P2 (recovery paradox — player agency lost before recovery is possible; confirm this is intended). F101 = P2 (terminal reachable within a single campaign arc — confirm rate was designed for this pace).

---

## TEST B3-027 — Weaving Overweaving Edge Case
**Coverage:** M-015 | TTRPG | PRES | TT, ThS | — | — | — | Practitioner

**Mode D — Edge Case**

### Overweaving Rule
"Each Weaving after the first in the same scene: +1 Ob (cumulative)."

Third Weaving in same scene: +2 Ob. At Relational scale (base Ob 3): Ob 5.
Fourth Weaving: Ob 6. Etc.

**Collapse on failed Overweaving:** TT +3 + local Shifting Object may form.

**Scene definition:** "Same scene" = from establishment to conclusion. Register Shift does not reset counter.

### Edge Case: Collective Thread Operation counted as one Weaving
Four practitioners perform a collective Weaving (§5.14). Does this count as one Weaving for the Anchor (and therefore one Overweaving instance) or as four?

Text says "each Weaving after the first in the same scene." A collective operation is one Weaving with multiple participants. The Anchor performs one Weaving; helpers contribute dice. **One Weaving event = one Overweaving count for the Anchor.**

**But:** Do the helpers each use their own Overweaving counter? If a helper performed an independent Weaving earlier in the same scene, is their contribution in the collective +1 Ob for them? Text is silent on helper Overweaving interaction.

**F102 — Collective Weaving helper Overweaving status undefined:** If a helper already has +1 Ob from their own prior Weaving this scene, does their contribution to a collective operation degrade? Rules specify the Anchor's roll but don't address whether helper prior Weavings penalise the collective.

**F103 — Overweaving counter resets unclear between scene and session:** "Same scene" reset. Does transitioning from a combat scene to a social scene (same physical location) constitute a new scene? "From establishment to conclusion" — GM defines scene establishment. Disputed edge case.

**Severity:** F102 = P2 (collective Weaving + Overweaving interaction undefined). F103 = P3 (GM judgment, manageable).

---

## TEST B3-028 — TD Track: Co-Movement Accumulation (M-020 full test)
**Coverage:** M-020 | TTRPG | CROSS | TD, ThS, TS | — | — | — | Practitioner

**Mode A — Isolation**

### TD Track (Temporal Disjunction / Coherence Degradation)
Range: 0–20. The coverage matrix labels this "Temporal Disjunction Track." From §12.7 "The TD Track as Campaign Arc" (line 3285, not fully scanned). Known from state tracking format: "TD [N/20]."

**[FLAG: TD track mechanics text at §12.7 not scanned. The track is referenced in state tracking but its threshold effects and accumulation rules are from §12.7 and §5.6 (Past-Oriented Pulling). Proceeding from what's confirmed:]**

From Past-Oriented Pulling (§5.6): operation produces "Temporal Disjunction — physical facts removed, memories remain intact." TD accumulates from this.
From state tracking: TD 0–20 range.

**Co-Movement ThS effects** (§5.8):
- Past-Oriented Pull: ThS −3 additional (already tested in B3-002).
- ThS and TD may be related but are confirmed as separate tracks (ThS = practitioner's own configuration stability; TD = world's temporal coherence state).

**TD Rate of Accumulation:**
From B3-002 test: 1 Past-Oriented Pull added TD +1. Rate depends on how many Past-Oriented Pulls are performed. At 1/session: TD 0 → 20 in 20 sessions.

**TD Threshold Effects:** Not confirmed from available scans. §12.7 required.

**F104 — TD full threshold table not confirmed:** The TD track exists, has a 0–20 range, and is fed by Past-Oriented Pulling. Threshold effects at TD 5, 10, 15, 20 are not confirmed from available scans. Coverage of M-020 is partial until §12.7 is read.

**Severity:** F104 = P2 (coverage gap — §12.7 unread).

---

## TEST B3-029 — Faction Generic: Schoenland (Spoiler Actor)
**Coverage:** M-034 | BG/HYB | FUT | IP, FSTAT | Crown, All | — | — | Faction Leader

**Mode A — Isolation**

### Schoenland: Not a Faction, Spoiler Actor (§8.10)

"Schoenland is not a faction — it is a spoiler actor."

**T15 Schoenland special property:**
- +1 Wealth/season to any faction with Trade order while route open.
- Altonian spies: Intelligence orders here reveal results to Altonia.
- IP 75+: Altonian vanguard deploys here.

**Spoiler actor mechanics:** No faction stats listed. No Domain Actions for Schoenland. It is a territory with passive effects and event triggers, not a playable faction.

**Trade route status:** Route open while Schoenland neutral (not at IP 75+). Any faction placing a Trade order at T15 gets +1 Wealth. But all Intelligence orders reveal to Altonia.

### Board Game Implication
In BG mode, players choosing to Trade at T15 for the +1 Wealth benefit are automatically feeding Altonian intelligence. This is a cost-benefit decision built into the territory's design.

### Findings
**F105 — Schoenland intelligence leak is automatic, not opposed:** All Intelligence orders at T15 "reveal results to Altonia" — no roll required. This is a passive ability that cannot be countered. Players cannot use Intel to block this leak. Accepting the trade bonus = accepting Altonian awareness of your intelligence operations.

**Severity:** F105 = P3 (intended — Schoenland is a trap/tradeoff mechanic).

---

## TEST B3-030 — Cross-Mode: Full Hybrid Campaign Turn at TC 40
**Coverage:** M-030, M-031, M-032, M-033, M-038, M-048 | HYB | CROSS | TT, TC, IP, FSTAT | All | Himlensendt, Almud, Baralta, Ehrenwall | Multiple

**Mode C — Full Hybrid Turn Simulation**

### State: Season 8, TC just crossed 40 (The Ultimatum)

```
TT 52 | TC 40 → The Ultimatum threshold fires | IP 35 (Aggressive)
Factions: Crown M5/I5/W4/Mi4/Sta4, Church M5/I6/W5/Mi4/Sta5
Hafenmark M7/I5/W5/Mi3/Sta4 (Baralta's Mandate buffed by player success)
Revolution I3/Sta3 | Löwenritter Mi5/I3/In3/Sta5
Torben Loyalty: 6 (Homesick, no mechanical effect yet)
Ehrenwall: monitoring, threshold not met
```

**TC 40 Threshold — The Ultimatum fires:**
Confessor Himlensendt formally demands Church supremacy over spiritual governance from Parliament. Specific demand placed.

**Strategic Phase (BG):**
- Crown: Grand Debate order (respond to Ultimatum). Roll: Crown Mandate 5D vs Church Influence 6D (institutional pools). 
  - Crown 5D TN7 expected net ≈ 1.65. Church 6D TN7 ≈ 2.0. Church slightly favoured.
  - Almud personally present: Almud 11D dominates — Crown wins ~85%.
- Church: Inquisitor File Building order (targeting Maret Uln, begins investigation).
- Löwenritter: Fortify order at Ehrenfeld (T5, Fort 3 → 4 — their cap).
- Revolution: Influence order in Korntal (T14, −1 Ob from Einhir Heartland). 3D TN7 Ob 1: P(success) ≈ 73%. Revolution Influence +1 if succeeds → Influence 3 → 4.
- Niflhel: Quiet Network at Schwarzmarkt (T10, −1 Ob).

**Cross-clock interactions active:**
TT 52 (> 45): TC +1/season, IP +1/season. (Already in effect.)
TC 40: The Ultimatum is a narrative event, not an additional clock modifier.
IP 35 (30–44): Economic sanctions active. Proxy disruption of Valorian factions.

**Personal Phase (TTRPG):**
IP 35 > 30: Torben tutoring demand remains active. Players must decide.

**Seasonal Accounting:**
1. TT passive drift: +1 per 4 seasons (every campaign year). Season 8 = year 2. TT +1: 52 → 53.
2. TC cross-clock from TT > 45: TC +1. TC: 40 → 41.
3. IP cross-clock from TT > 45: IP +1. IP: 35 → 36.
4. Stability checks:
   - Crown: 1 active threat (Ultimatum). Ob 2. Crown Stability 4D. P(failure) ≈ 17%. P(Overwhelming) ≈ 32%.
   - Church: no threats (it's issuing the threat). Ob 1. Stability 5D. P(Overwhelming, Stability +1) ≈ 42%.
   - Revolution: 1 threat (IP proxy disruption). Ob 2. Stability 3D. P(failure) ≈ 33%. **One-third chance Revolution Stability drops to 2 → floor activates.**

**Post-season state:**
```
TT 53 | TC 41 | IP 36
Crown Sta 4 (likely stable) | Church Sta 5→6 (possible) | Revolution Sta 3→2 (33% chance)
Ehrenfeld Fort 4 (Löwenritter maximum)
Maret Uln: Inquisitor File Building begun
```

### Findings
**F106 — TC 40 Ultimatum is a cascade trigger, not a discrete event:** The Ultimatum is the threshold narrative event but mechanically TC continues to increase through the established cross-clock linkages. There is no pause or reset at TC 40 — the threshold fires its event and TC keeps climbing. Players must respond to the Ultimatum while also managing ongoing clock drift.

**F107 — Revolution Stability floor risk is a regular pressure:** In any season with one active threat (routine for Revolution), there's a 33% chance of Stability floor activation. Over 10 seasons: P(at least one floor activation) = 1 − (0.67)^10 ≈ 98%. **Revolution will almost certainly hit the Stability floor at least once in a campaign.** This is likely intentional (Revolution is structurally fragile) but its recovery path from the floor is not specified.

**Severity:** F106 = P3 (intended — threshold is narrative trigger not mechanical pause). F107 = P2 (Revolution floor activation near-certain — recovery procedure needed).

---

## FINDINGS SUMMARY — BATCH 03

| Finding | Severity | Mechanic(s) | Description |
|---------|----------|-------------|-------------|
| F52 | P3 | M-009 | Certainty is a countdown timer — intended existential pressure |
| F53 | P2 | M-009 | Intelligibility + Coherence double-compress Certainty max |
| F54 | P2 | M-019 | Single Past-Oriented Pull can push ThS into Fractured mid-operation |
| F55 | P2 | M-019 | Past-Oriented Pull TT→TC consequence chain not player-visible at decision point |
| F56 | P3 | M-019 | Operation costs front-loaded, no abort — intentional |
| F57 | P2 | M-021 | Coherence below 4 is mechanically terminal without player agency |
| **F58** | P2 | M-021 | +3D bonus at Coherence 2–3 creates perverse farming incentive |
| F59 | P2 | M-020 | ThS 0 recovery requires 3 seasons non-practice — campaign-disrupting |
| F60 | P2 | M-020 | ThS threshold crossings are opaque — no player-visible warning |
| F61 | P2 | M-030 | TT 80+ self-reinforcing failure state — confirm design intent re: viable stabilisation path |
| F62 | P3 | M-031 | TC 100 effectively unreachable without player mistakes — intended pressure clock |
| F63 | P2 | M-031 | Baralta excommunication has asymmetric TC impact — confirm GM documentation |
| F64 | P2 | M-034/M-035 | Ehrenwall coup trigger #1 undefined in NPC text |
| F65 | P2 | M-034 | Torben loyalty decay rate not specified |
| F66 | P3 | M-008 | Lenneth scholarly TS path is fast — intended |
| F67 | P3 | M-008 | No Devout Constraint on Lenneth — intentional |
| F68 | **P2** | M-036/M-037 | Baralta Sovereign Authority is near-TC-neutral in expectation due to Heresy Investigation trigger |
| F69 | P3 | M-036 | Players should hold Sovereign Authority until investigation is manageable |
| F70 | P2 | M-035 | Recruiting Vaynard as ally triggers TC consequences |
| F71 | P3 | M-035 | Vaynard Discovery Event is player-controllable — intentional |
| F72 | P3 | M-008/M-049 | Klapp TS development is structural Church crisis — intended |
| F73 | P2 | M-049 | CE track above 3 undefined for non-Inquisitor Church characters |
| F74 | P3 | M-011/M-037 | Elske recruitable by multiple factions — intended contested resource |
| F75 | P2 | M-011 | Simultaneous multi-faction recruitment procedure absent |
| F76 | P3 | M-014/M-051 | Originary Lock as Devout disruption tool — intentional |
| F77 | P2 | M-014 | TS spread from Originary Lock handling is uncontrolled |
| F78 | P3 | M-049/M-050 | Baralta-Olafsson chain is high-value one-shot — intended |
| F79 | P2 | M-050 | Riskbreaker Debt from evidence gathering should be player-visible tradeoff |
| F80 | P3 | M-037 | Grand Debate between matched leaders is high-variance — intended |
| F81 | P3 | M-037 | Rattled rare in Grand Debate — intended |
| F82 | P2 | M-036 | Multi-party Parliamentary Vote resolution undefined |
| F83 | P3 | M-036 | Named NPC personal pools dominate institutional in Parliament — intended |
| F84 | P3 | M-052 | Concealment Ob round-up loses granularity in 31–59 band |
| F85 | P2 | M-052 | Concealment non-advanceable beyond Cognition — confirm design intent |
| F86 | P3 | M-049 | Investigation produces CE accumulation as designed — intentional |
| F87 | P2 | M-049 | Formal Accusation lacks mechanical bite vs high-Cognition practitioners |
| F88 | P2 | M-050 | "Exposed operation" definition absent — Debt trigger ambiguous |
| F89 | P2 | M-050 | Debt 3 Ob penalty may compound at Debt 5 parliamentary inquiry |
| F90 | P2 | M-044 | Prone condition does not penalise Thread operations |
| F91 | P3 | M-044 | Indirect disruption via Wound setup works as designed |
| F92 | P2 | M-034/M-038 | Revolution one failed check from Stability floor — confirm intent |
| F93 | P2 | M-034 | Revolution Intel starting value absent |
| F94 | P2 | M-034 | Niflhel Intel starting value absent |
| F95 | P2 | M-034 | Niflhel BG victory condition undefined |
| F96 | P3 | M-034/M-035 | Guilds Wealth dominance vs Military weakness — intended asymmetry |
| F97 | P2 | M-034/M-035 | Löwenritter Martial Law TC authorisation ambiguous |
| F98 | P3 | M-032 | IP 100 is background threat not realistic terminal — intended |
| F99 | P2 | M-032 | Altonian invasion force stats absent |
| F100 | P2 | M-020 | Intelligibility 0 → NPC transition creates recovery paradox |
| F101 | P2 | M-020 | Intelligibility 0 reachable within single campaign arc |
| F102 | P2 | M-015 | Collective Weaving + Overweaving helper interaction undefined |
| F103 | P3 | M-015 | Overweaving reset between scenes — GM judgment |
| F104 | P2 | M-020 | TD track threshold effects unconfirmed (§12.7 unread) |
| F105 | P3 | M-034 | Schoenland intel leak automatic — intended trap/tradeoff |
| F106 | P3 | M-030/M-031/M-033 | TC 40 Ultimatum is narrative trigger, not mechanical pause — intended |
| F107 | P2 | M-038 | Revolution Stability floor near-certain over campaign; recovery procedure needed |

### P1 Findings This Batch
None.

### P1 Findings Remaining from All Batches
| Finding | Mechanic | Issue |
|---------|----------|-------|
| **F25** | M-016 Pulling | Personal-scale Pulling bypasses all social counter-mechanics — no non-practitioner resistance or detection |

### P2 Count This Batch: 27
### P2 Running Total (Batches 01–03): ~50

---

## Coverage Dimension Log

| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes |
|---------|-----------|------|----------|--------|----------|------|------------|
| B3-001 | M-009 | TTRPG | CROSS | CERT, TS, INT | — | — | Practitioner |
| B3-002 | M-019 | TTRPG | PAST | TD, TT, TS, CERT | Varfell | Vaynard | Practitioner |
| B3-003 | M-021 (Coherence) | TTRPG | CROSS | Coherence, CERT, TS | Niflhel | — | Practitioner |
| B3-004 | M-020 (ThS) | TTRPG | CROSS | TD, ThS, TS | — | — | Practitioner |
| B3-005 | M-030 | TTRPG/BG | FUT | TT, TC, IP | All | — | Multiple |
| B3-006 | M-031 | TTRPG/BG | FUT | TC, TT, IP | Church, Crown, Hafenmark | Himlensendt, Baralta | Faction Leader |
| B3-007 | M-034, M-035 | TTRPG | FUT | FSTAT, TLK | Crown, Löwenritter | Ehrenwall, Almud, Torben | Faction Leader, Löwenritter Knight |
| B3-008 | M-008 | TTRPG | PAST | TS, TC | Crown, Revolution | Lenneth | Non-TS Scholar |
| B3-009 | M-036, M-037 | TTRPG | PRES | TC, FSTAT | Hafenmark, Church | Baralta, Himlensendt | Faction Leader |
| B3-010 | M-035 | TTRPG | FUT | TC, TS, FSTAT | Varfell, Church | Vaynard | Non-TS Scholar |
| B3-011 | M-008, M-049 | TTRPG | PAST | TS, CE, TC | Church | Klapp, Olafsson | Non-TS Scholar |
| B3-012 | M-011, M-037 | TTRPG | PRES | FSTAT, IP | Crown, Varfell, Revolution | Elske | Faction Leader |
| B3-013 | M-014, M-051 | TTRPG | CROSS | TS, TC, CERT | Church | Himlensendt | Devout Character |
| B3-014 | M-049, M-050 | TTRPG | PAST | TC, FSTAT, DD | Church, Niflhel, Crown | Olafsson, Baralta | Inquisitor, Riskbreaker |
| B3-015 | M-037 | TTRPG | PRES | TC, FSTAT | Church, Crown, Hafenmark | Himlensendt, Almud, Baralta | Faction Leader |
| B3-016 | M-036 | TTRPG/BG | PRES | FSTAT, TC | Crown, Church, Hafenmark, Varfell | Almud, Himlensendt, Baralta, Vaynard | Faction Leader |
| B3-017 | M-052 | TTRPG | PRES | TS, CE | Church, Crown | Klapp | Practitioner, Inquisitor |
| B3-018 | M-049 | TTRPG | PRES | CE, TC, FSTAT | Church, Crown | Olafsson, Klapp | Inquisitor, Practitioner |
| B3-019 | M-050 | TTRPG | PRES | DD, FSTAT | Crown, Church | — | Riskbreaker |
| B3-020 | M-044 | TTRPG | PRES | — | Löwenritter | Ehrenwall | Löwenritter Knight |
| B3-021 | M-034, M-035, M-038 | BG | PRES | FSTAT, TT | Revolution | — | Faction Leader |
| B3-022 | M-034, M-035 | BG | PRES | FSTAT | Niflhel | — | Riskbreaker |
| B3-023 | M-035 | TTRPG/BG | PRES | FSTAT | Guilds | — | Faction Leader |
| B3-024 | M-034, M-035 | TTRPG/BG | PRES | FSTAT, TC | Löwenritter, Crown, Church | Ehrenwall | Löwenritter Knight |
| B3-025 | M-032 | TTRPG/BG | FUT | IP, TT, TC, FSTAT | Crown, All | Almud, Ehrenwall, Torben | Multiple |
| B3-026 | M-020 (INT) | TTRPG | CROSS | INT, TS, CERT | — | — | Practitioner |
| B3-027 | M-015 | TTRPG | PRES | TT, ThS | — | — | Practitioner |
| B3-028 | M-020 (TD) | TTRPG | CROSS | TD, ThS, TS | — | — | Practitioner |
| B3-029 | M-034 | BG/HYB | FUT | IP, FSTAT | Crown, All | — | Faction Leader |
| B3-030 | M-030/M-031/M-032/M-033/M-038/M-048 | HYB | CROSS | TT, TC, IP, FSTAT | All | Multiple | Multiple |

---

*End sim_batch_03.md*
