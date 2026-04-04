# VALORIA — SYSTEMATIC CRITIQUE
## Date: 2026-04-04
## Basis: Full 3-phase audit of all params, all canonical design docs, canon constraints, editorial ledger, coverage matrix, propagation map
## Scope: Entire game across all three modes (TTRPG ← Hybrid → Board Game)

---

## 1. WHAT THE GAME DOES WELL

### 1.1 Philosophical Integration Is Genuine
The Foundations are not flavour text bolted onto a generic system. P-01 (inseparability) mechanically enforces three-dimensional co-movement on every Thread operation — the player cannot touch a thread without the world changing in three directions simultaneously. This produces gameplay where every practitioner action has unintended consequences by design, not by GM fiat. No other TTRPG I can identify does this at a mechanical level. The closest comparator is Burning Wheel's Beliefs system, but BW's consequences are narrative; Valoria's are computational.

### 1.2 The Three-Mode Frame Is Architecturally Sound
TTRPG ← Hybrid → Board Game sharing a mechanical baseline (d10, TN 7, degree table, same faction stats) is a genuine achievement. The 8 handoff rules are mostly well-specified. The mode asymmetries (Domain Echo timing, Thread skipped in BG, Zoom In Phase-Lock) are intentional and documented. This is not three separate games — it is one game at three scales. The Hybrid mode acts as a real bridge, not a compromise.

### 1.3 The Dice Engine Is Mathematically Clean
d10 with TN 7 produces E[net] = 0.3 per die. The probability curves scale predictably. 4D gives ~80% to hit Ob 1; 10D gives ~73% to hit Ob 3. The degree table (Overwhelming at 2×Ob with floor 3) creates a meaningful distinction between "barely succeeded" and "dominated." No exploding dice, no re-roll mechanics, no fiddly modifiers to the die faces. The engine stays out of the way.

### 1.4 Faction Systems Have Real Asymmetry
Each faction has genuinely different mechanical identity: Church's Theocracy Counter trajectory, Crown's decree/loyalty tension, Varfell's intelligence-Thread trade-off, Hafenmark's economic leverage, Restoration's Community Weaving. These aren't cosmetic differences — they produce different strategic concerns and different optimal play patterns in BG mode.

---

## 2. STRUCTURAL CONCERNS

### 2.1 The Canonical Source Chain Was Broken (Now Fixed)
PP-232 — the single most important mechanical patch in the project — was applied to all params files but none of the canonical design documents. This was discovered during Phase 2 of this audit and has been resolved. But it reveals a process vulnerability: there is no automated check that a patch applied to params was also applied to the canonical doc. The `freshness_gate.py` tool checks SHAs but cannot detect partial propagation within a document. A patch can change a params value and the SHA check will see the params file changed, but it won't verify that the source doc also changed.

**Recommendation:** Add a "PP-applied" field to canonical_sources.yaml per system listing the highest PP number applied to both the params AND the canonical doc. If they diverge, the freshness gate fails.

### 2.2 The Game Has Too Many Provisional Decisions
The editorial ledger contains 30+ open items. The patch register contains dozens of [PROVISIONAL] markers. The coverage matrix has provisional patches applied during simulation that were never formally approved. Provisional decisions were the right call during rapid design iteration — they unblocked simulation. But the accumulated count means large sections of the ruleset are not final. Any future simulation built on provisional values inherits their uncertainty.

Specifically: Community Weaving has THREE conflicting specifications (ED-139). Discipline degradation has a trigger formula that contradicts its own design note (ED-140). The BG Overwhelming threshold has contradictory resolutions (ED-142). These aren't edge cases — they're core mechanics for their respective systems.

**Recommendation:** Dedicate a full session to resolving all P1 editorial items. No new design work until the provisional count is below 10.

### 2.3 Compilation Is Severely Behind
4 of 14 compilation stages are STALE. stage3 (Thread operations) is EMPTY. stage9 (social) is behind the v2 redesign. stage8 (combat) is behind the design doc. stage_bg is behind bg_v05. The compilation layer is supposed to be the player-facing document — the thing someone actually reads to learn the game. Currently, no one can learn the game from the compilation because it describes a different game than the one the params and design docs specify.

**Recommendation:** This is not urgent (design docs are canonical) but it means the game cannot be playtested by anyone who isn't the designer until compilation catches up.

---

## 3. PLAYABILITY RISKS

### 3.1 Thread in Mass Combat Is the Make-or-Break Moment
Even with PP-235 optimizations, Thread in Mass Combat is the most complex interaction in the game. It requires a player who has mastered both the Thread system and the mass combat system, then asks them to run both simultaneously (albeit sequentially per PP-235 TM-1). The PP-201 campaign-impact warning (Dissolution can end the campaign) adds decision weight on top of decision complexity.

This is the moment the game either feels brilliantly integrated or collapses under its own weight. Playtesting will determine which. The mechanical design is sound — the question is whether a human at a table can execute it without constant reference to 3+ documents.

The reference architecture (META-3) is not optional — it's load-bearing. Without physical cards, mats, and pre-printed tables, Thread in Mass Combat is not playable by most groups.

### 3.2 Social Contest Strain System May Feel Like Bookkeeping
The strain → Composure → Rattled chain, combined with Concentration depletion and Conviction Track movement, produces 3 separate resource tracks to monitor during a single scene type. Even with the strain reference card (SC-1), the player is tracking:
- Composure (am I Rattled?)
- Concentration (am I Spent?)
- Conviction Track (am I winning?)

These interact (Rattled + Spent stack penalties) but are tracked independently. The risk is that a social scene — which should feel like verbal combat — instead feels like accounting. The PP-235 argument styles (SC-3) help by giving the choices rhetorical identity, but the tracking burden remains.

The question: does the strain system produce meaningfully different outcomes from a simpler "margin-based track only" system? If the answer is "strain rarely causes Rattled before the Conviction Track resolves," then the Composure/Concentration subsystem is mechanical weight without proportional payoff. This needs simulation to confirm (but is separate from SIM-DEBT-03/04).

### 3.3 The Game Is Unpublishable in Current Form
Not because the design is bad — because the document architecture is a development workspace, not a product. 14 compilation stages, 40+ design docs, 8 params files, 200+ patches, 140+ editorial items. No player can navigate this. The game as experienced by a player must be a single document (or a small set of documents) that presents the rules in play order, not in patch order.

This is expected at this stage of development. But the gap between "design workspace" and "publishable game" is larger than it might appear, because the game's complexity means the rulebook needs to be exceptionally well-organized to be usable.

---

## 4. DESIGN DEBT

### 4.1 Stage 5 (Clocks) and Stage 15 (Spell Catalog) Are Empty
Two compilation stages have zero content. Clocks are mechanically critical (TC, RS, IP drive the entire BG game and half the TTRPG game). The clock mechanics are defined across multiple other files (factions, board game, threadwork) but there is no unified clock document. A player asking "how do clocks work?" has no single place to look.

Spell catalog is empty — Thread operations serve as the "magic system," but there's no consolidated reference for what a practitioner can actually DO. The operations are spread across threadwork_v25 (85k chars) with no quick-reference index.

### 4.2 Hybrid Integration Is Pending
17 resolved gap decisions in hybrid_gaps_resolved.md have not been integrated into stage11_scale_transitions.md. The Hybrid mode is the most architecturally ambitious part of the game (bridging TTRPG and BG in real-time), and its rules are split between a compilation stage and an unintegrated design doc.

### 4.3 NPC Stat Blocks Use Inconsistent Attribute Names
stage13_npcs.md contains "Coordination" and "Power" as attribute names, which don't correspond to any defined attribute. This suggests the NPC stat blocks predate one or more attribute naming passes and haven't been verified against the current attribute list.

### 4.4 Ranged Weapons Not Integrated Into PP-232 Weapon Matrix
ED-129 remains open. The PP-232 Short/Long × Light/Heavy × Blade/Blunt matrix does not cover ranged weapons (LP, HP, Sling). These retain the old per-weapon TN system. The two systems coexist in the same combat doc, which is inelegant and will confuse players.

### 4.5 Remaining Faction Tactic Cards Not Designed
Only Crown and Church have tactic cards. Varfell, Hafenmark, Löwenritter, and Restoration Movement are TBD. This is a content gap, not a structural one, but it means 4 of 6 playable factions lack a BG component.

---

## 5. WHAT'S MISSING

### 5.1 No Onboarding Pathway
The game's learning curve is steep: Personal Combat → Social Contest → Faction Domain Actions → Thread Operations → Mass Combat → Hybrid → Board Game. There is no designed onboarding sequence that introduces these systems progressively. The META-1 tiered complexity proposal addresses this but hasn't been formalised.

### 5.2 No Economy System
Characters have no money. Resources are referenced (Stamina = Endurance + History + 1, armour has STR minimums) but there's no acquisition, trade, or wealth system. Factions have Wealth as a stat but personal characters don't interact with it mechanically. This is a deliberate omission (the game is about political and metaphysical stakes, not shopping) but it means the GM has no mechanical support for mundane logistics.

### 5.3 No Exploration or Travel System
Movement between territories is mentioned (stage7) but there's no mechanical travel system. The Southernmost has an expedition structure (stage4) but general overland travel has no rules. Again, this may be intentional — the game focuses on social/political/metaphysical conflict, not dungeon crawling. But it means transitions between locations are purely narrative.

### 5.4 No Session Structure Guide
When does a TTRPG session of Valoria look like? How many scenes per session? When does the GM call for a Domain Action vs a personal roll? How does seasonal accounting integrate with session pacing? There's no procedural guide for running a session. Stage14 (GM tools) exists but focuses on mechanical tools, not session structure.

---

## 6. THE BIGGEST QUESTION THE DESIGN HASN'T ANSWERED

**Is the game fun to play slowly?**

Every system in Valoria produces consequences that ripple across multiple tracks and multiple sessions. Thread operations affect RS, which affects faction play, which affects NPC behaviour, which affects the political landscape, which affects which Thread operations are available. This interconnection is the game's thesis — inseparability made mechanical.

But interconnection means every action requires understanding the full system state. A player who wants to "just do a thing" — attack an enemy, persuade a noble, weave a thread — must first assess the downstream effects across 3-6 tracked variables. The game rewards strategic thinking and punishes impulsive action. This is philosophically consistent with the Foundations (rendering is constitutive work; carelessness has ontological consequences).

The risk: strategic thinkers will love this. Narrative-first players will find it oppressive. The game selects for a specific player type — one who enjoys the weight of consequence as a feature, not a bug.

The unanswered question is whether enough of those players exist, and whether they'll find each other at the same table. Valoria is not for everyone. That's a design choice, not a flaw. But it needs to be stated clearly in the game's own text so that prospective players can self-select.

---

## 7. OVERALL ASSESSMENT

The mechanical design is strong. The philosophical grounding is genuine and produces gameplay that no other system offers. The three-mode architecture is ambitious and architecturally sound. The audit found no unbounded crunch cascades, no broken feedback loops, and no canon constraint violations.

The game's primary risk is not mechanical — it's human. The complexity demands reference architecture, experienced players, and a GM willing to manage multiple subsystems simultaneously. The PP-235 cognitive load package brings every system into the Moderate range, but "Moderate" for Valoria means "heavier than most games' maximum." The game's floor is other games' ceiling.

The path forward: resolve the remaining editorial items, compile the ruleset into a single playable document, build the reference architecture (cards, mats, sheets), and playtest. Everything before that is theory. The design is ready for contact with players.
