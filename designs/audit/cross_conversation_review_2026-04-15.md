# VALORIA — Cross-Conversation Review
## What the canonical registry and complete systems reference missed or got wrong
## Based on exhaustive review of 20 conversations (April 10–15, 2026)
## Date: 2026-04-15

---

## 1. STALE DATA IN MY DOCUMENTS

### 1.1 Disposition Range — Using Pre-PP-632 Values

**My documents say:** Disposition −3 to +5.

**PP-632 (committed April 14, confirmed in fieldwork/Knot session) changed this to:** Disposition range −4 to floor(Bonds/2)+1. Maximum +4 at Bonds 6–7. Decay threshold changed from above +3 to above +2. Ob calculation: max(1, base Ob − Disposition) — replaces the old stepped lookup table.

**This is one of the most important recent changes.** The April 14 audit chat called PP-632 "the single best piece of design work in the sprint." My documents throughout use the old range. Every reference to Disposition −3 to +5 must be corrected to the PP-632 formulation.

### 1.2 Knot Mechanics — Partially Captured

**My documents included:** Pool = (Bonds × 2) + 3. Max count = floor(Bonds/2)+1. Tiers (Close/Medium/Loose). Formation, breaking (rupture vs loss).

**What I missed:** PP-632 also established that Bonds governs depth in BOTH directions simultaneously — Disposition ceiling AND Knot capacity both derive from the same formula. The design elegance is that one attribute (Bonds) determines both how deep a relationship can go AND how many deep relationships you can maintain. This structural insight should be highlighted, not just listed.

### 1.3 Godot Implementation — Severely Understated

**My audit said:** "Phase 0 complete, Phase 1+ not started."

**The most recent Godot session (April 15, "echoes" chat) delivered:** Phases 1–12 fully implemented. BoardContainer with territory map. BattleContainer with general Command from Cha+Cog. check_victory covering ALL canonical victory conditions (Crown, Church Graduated Seizure, Hafenmark Parliamentary + Dynastic Assertion, Varfell 3 paths, RM Cultural Revolution, Partition, Dominion). Nested zoom (Phase 10.1). Season loop mechanically complete and runnable end-to-end.

**The game is much further along than I described.** The conversion ledger showed Phase 0; that was stale. Multiple subsequent sessions implemented everything through Phase 12.

### 1.4 Simulation Results — Not Referenced

**The headless simulation session (April 14) produced validated results:**
- TC_THEOCRACY victory: 53% (BG), 45% (Hybrid)
- CROWN_TREATY victory: 14% (BG), 16% (Hybrid)
- TIMEOUT (no victory): 32% (BG), 39% (Hybrid)
- Average game length: 13.3 years (BG), 14.5 years (Hybrid)
- Crown collapse rate: 3.4%
- Hafenmark collapse rate: 27.8%

**These results indicate a Church-dominant meta** that the tc_political_redesign_v30 (the document Jordan uploaded this session) was designed to address. The simulation also identified: territory Prosperity not seeded, Löwenritter post-coup AI not implemented, Varfell VTM path incomplete, Hafenmark RDT/TD tracks unresolved.

---

## 2. SYSTEMS I FAILED TO INCLUDE

### 2.1 Löwenritter Internal Structure (Five Arms)

From the April 4 governance session, the Löwenritter have a detailed internal arm structure:

| Arm | Function | Primary Stat | Domain |
|---|---|---|---|
| Lions' Table | Military command, garrison, battle coordination | Military | Standard military |
| Lions' Helm | Naval affairs, sea route security, blockade | Military (naval) | Naval operations |
| Knights of the Peace | Patrol, law enforcement, dispute resolution | Influence | Civil order |
| Royal Investigators | Investigation, counter-espionage, evidence gathering | Intel → Investigation | Covert |
| Riskbreakers | Infiltration, cult disruption, deniable operations | Intel → Investigation | Extralegal |

**Mechanical effects:**
- Royal Guard: +2 Ob to assassination attempts on Court members.
- Knights of the Peace patrol: +1 Ob to covert actions by hostile factions in patrolled territory.
- Lions' Helm: secure sea routes (+1D trade for Crown/allies), naval blockade, coastal defense vs Altonian approach.
- Riskbreakers: loyal to Valoria the concept, not the institutions — structural fault line that the Coup arc exploits.

**My documents mentioned none of this.** It's important for the videogame because the Löwenritter aren't just "Military 6" — they have differentiated capabilities through their arm structure.

### 2.2 Community Projects System

From earlier conversations, a multi-season project system exists:

| Project | Duration (seasons) | Effect |
|---|---|---|
| Community Weave | 3 | Metaphysical Stability +2; permanent +1 Thread node in territory |
| Einhir Memory Recovery | 4 | Reveals narrative hook; Thread Knowledge +1; Metaphysical Stability +1 |
| Restoration Network | 5 | RM gains permanent Presence in 2 adjacent territories; Invasion Pressure −1 |
| Fortification | 3 | Fort +1 at no Wealth cost |
| Diplomatic Mission | 2 | +1 Standing cleared; Diplomacy −1 Ob next season |

Projects advance +1/season with faction presence. Disrupted by battle (−2), control change (−1), or Heresy Investigation (−1/season).

**Status:** This system may be from an earlier iteration (pre-peninsular_strain). It should be cross-checked against current design docs to confirm whether it's still canonical or was superseded.

### 2.3 NPC Comprehensive Audit Results (April 10)

A detailed NPC audit was committed to the design repo (designs/npcs/npc_comprehensive_audit.md). Key findings I should have referenced:

- **Haelgrund** scored 39/40 (highest). His hidden TS and buried Reason conviction make him the most mechanically complex NPC — not "incomplete" as I suggested, but exceptionally well-designed.
- **Lenneth** scored 28/40 with "zero mechanical expression despite high narrative importance" — the widest gap between characterization quality and mechanical presence.
- **Almud** has "no BG mode expression" — the peninsula's most important political figure is invisible in board game mode.
- **Elske** has "mechanical impact but zero characterization" — she is a mechanism, not a person.
- **Haelgrund ↔ Torsvald** parallel is flagged as "the most valuable unwritten NPC interaction" — both have hidden TS in institutions that would reject them.

### 2.4 NPC Conviction-to-AI Integration (Committed April 14)

The full NPC ethical stance and resonance behavior system (npc_behavior_v30.md) was designed, audited, simulated, and committed in a dedicated session. My documents captured the content but missed the simulation patches:

- **PP-NPC-01:** Crown Decree gated on Mandate ≥ 3 (prevents death spiral where Almud keeps issuing Decrees at low Mandate, failing, losing more Mandate).
- **PP-NPC-02:** Deterministic coup requires active Church Assert, not just passive CI advancement (prevents the coup from firing based on a clock no player actively controls).
- **PP-NPC-03:** Church Influence drift conditioned on Stability + Church Influence + yearly cycle (prevents runaway drift).
- **PP-NPC-04:** Varfell Private Collection cooldown enforced (prevents unbounded VTM advancement).

These simulation patches are critical for the videogame AI and my documents didn't mention them.

### 2.5 Opposing Threadwork — PP-632 §2.6

From the concurrent threadwork session (April 14), a full opposing operations system was designed and committed. My "simplified" version in the complete systems reference captures the core but misses:

- **Mending is categorically immune to direct opposition** (different target category — substrate absence vs thread presence). This is a philosophical derivation, not an arbitrary rule.
- **Opposing engagement modifier = +floor(opponent's TPS / 2), minimum +1.** This is philosophically necessary: the opponent's configuration IS part of the thread's resistance.
- **N-way opposing operations (3+ practitioners):** Automatic lattice collapse. All operations fail. Gap forms at target's scale. Metaphysical Stability −(2 × number of practitioners). This is the definitive answer to "what happens when too many people try to change the same thing."
- **FR vs FR Both-Fail scaling table** by scale (Object through Structural), with increasing Metaphysical Stability cost and Shifting Object risk.

### 2.6 Emergent Arc Trigger Distribution

From the April 14 arc evaluation session, the trigger distribution across the game was analyzed:

- **Overtriggered:** Church faction (too many arcs fire from CI thresholds alone).
- **Undertriggered:** Crown (too few territory-based triggers), Hafenmark (almost no arcs below Season 8), Varfell (VTM path arcs too linear).
- **Missing:** Territory-based triggers (arcs that fire when specific territories change hands, reach specific Piety/Accord values, or develop specific POI chains). These are essential for the videogame where the player explores territories.

---

## 3. THINGS I GOT RIGHT

For completeness, confirming what holds up against the five-day review:

- **PP-403 repeal** (Failed DA no longer costs Stability) — confirmed in faction_layer_v30.
- **Five canonical Stability triggers** — confirmed.
- **Thread pool formula** (Spirit × 2 + History + TPS) — confirmed canonical post-PP-619.
- **Three-axis Ob system** (Depth + Breadth + Distance) — confirmed canonical post-PP-622/623.
- **Accord system** (peninsular_strain_v1) — confirmed, propagated to 12 files in the victory conditions session.
- **Battle consequences** (Metaphysical Stability −1, Invasion Pressure +2, Political Stability +1) — confirmed and propagated.
- **Church Influence milestones** (40/55/65/80/100) from tc_political_redesign_v30 — confirmed and sim-validated.
- **Faction acquisition toolkits** (Crown Treaty, Graduated Seizure, Dynastic Proclamation, Cultural Reformation, Martial Governance) — confirmed.
- **Unit stat renames** (Size/Power/Discipline/Command per PP-232) — confirmed, though propagation to all documents is still incomplete.

---

## 4. PENDING FROM CROSS-CONVERSATION REVIEW

| Item | Source | Status |
|---|---|---|
| PP-632 Disposition range change | fieldwork/Knot session April 14 | Must update all references in my documents from −3/+5 to PP-632 formula |
| Löwenritter five-arm structure | governance session April 4 | Must add to complete systems reference |
| Community Projects system | older iterations | Must verify whether still canonical or superseded |
| NPC simulation patches (PP-NPC-01 through PP-NPC-04) | NPC behavior session April 14 | Must add to NPC AI sections |
| Godot Phase 1–12 implementation | echoes session April 15 | Must correct implementation status throughout |
| Hafenmark 27.8% collapse rate | headless sim April 14 | Must note as game balance concern |
| Territory-based arc triggers missing | arc evaluation April 14 | Must flag for videogame design |
| Mending immune to opposition | opposing threadwork session April 14 | Must add to Thread operations section |
| N-way opposing operations | opposing threadwork session April 14 | Must add to Thread operations section |
