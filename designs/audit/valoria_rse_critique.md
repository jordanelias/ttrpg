# VALORIA — Robustness / Smoothness / Elegance Critique
## Date: 2026-04-15
## Criteria:
##   Robust = allows strategizing, rewards player creativity, impacts game world meaningfully
##   Smooth = works alongside other systems, handles transitions/zooming, no friction at boundaries
##   Elegant = logically simple, clear approach, minimal special cases

---

## Grading Scale: ● Strong | ◐ Mixed | ○ Weak

---

## S02 CORE ENGINE

| Criterion | Grade | Assessment |
|-----------|-------|------------|
| Robust | ● | Universal pool formula means every action in the game uses the same math. Players who understand one system understand all systems. The d10 with TN 7 produces a clean 0.4 expected net per die — probability space is intuitive. |
| Smooth | ● | Every system plugs into this engine. No system has a different dice resolution. Transitions between systems never require learning new math. |
| Elegant | ● | One pool formula: (Attr×2)+H+3. One Ob formula: floor(stat/2)+1. Two formulas govern the entire game. The only structural exception (Thread TPS replacing +3) is justified and minor. |

**Verdict:** The foundation is excellent. This is the project's strongest system.

---

## S11 COMBAT (Personal)

| Criterion | Grade | Assessment |
|-----------|-------|------------|
| Robust | ● | Pool split (Offense/Defense) creates genuine tactical decisions every exchange. 14 actions (Strike, Feint, Rescue, Escape, etc.) give creative options. Wound accumulation with threshold creates tension — you're tracking toward a wound, not losing abstract HP. Momentum rewards bold play. |
| Smooth | ● | Combat Pool uses the universal formula. Wounds carry into other systems (−1D all pools). Stamina depletion carries into fieldwork (can't investigate while exhausted). Rescue creates emergent narrative (no Defense = genuine sacrifice). |
| Elegant | ● | Three-axis weapon system (Reach × Weight × Type) compresses an entire equipment system into three binary choices producing TN 5-8. No weapon tables, no special abilities, no feat lists. The system is the weapon system. |

**Verdict:** The most polished system. No changes needed.

---

## S12 SOCIAL CONTESTS

| Criterion | Grade | Assessment |
|-----------|-------|------------|
| Robust | ◐ | The 2×2×4 structure (genre × orientation × style) gives 16 tactical combinations — genuine strategic depth. Appraise lets you read opponents. Corroborate rewards preparation. Institutional Mandate (Appease at Mandate −1) creates meaningful political cost. BUT: the decision space is steep. A player needs to internalize genre/orientation/style interactions before they can strategize meaningfully. In the first 3-4 contests, players will be executing mechanically without understanding why their choices matter. |
| Smooth | ◐ | Composure/Concentration parallel Health/Stamina — structurally clean. Contest outcomes feed into faction Mandate/Influence via Domain Echo. NPC conviction modifiers integrate cleanly. BUT: transitioning from combat to contest mid-scene requires switching mental models entirely — different pool, different resource, different action vocabulary. No shared action between combat and contest (you can't "Feint" in a debate). |
| Elegant | ◐ | The exchange structure (Appraise → Declare → Corroborate → Argue → Resolve → Forfeit) is clean. But: four styles (Citation, Suppression, Vision, Insinuation) each with different genre/orientation bonuses create a 16-cell lookup that players must internalize. Compare to combat: you split your dice between Offense and Defense. That's it. The contest system asks for significantly more cognitive overhead per decision. |

**Key problem:** The system is intellectually elegant but experientially complex. A combat round takes 5 seconds to decide (how many dice offense vs defense?). A contest exchange takes 30+ seconds (which genre? which orientation? which style? do I corroborate? what's my opponent's likely style? what's the adjudicator bonus?). The system rewards mastery but punishes newcomers.

**Recommendation:** For the videogame, implement a "suggested style" UI hint that highlights the mechanically strongest option given the current contest state. This preserves strategic depth for experienced players while giving newcomers a viable default. The TTRPG needs a one-page quick reference card with the 16-cell matrix and decision flowchart.

---

## S13 THREAD OPERATIONS

| Criterion | Grade | Assessment |
|-----------|-------|------------|
| Robust | ● | Seven distinct operations (Weaving, Pulling, POP, Locking, Dissolution, Mending, Community Weaving) each with different TN and mechanical consequences. Three-axis Ob (Depth + Breadth + Distance) means the player explicitly states what they're attempting: how primordial, how much, how far. Coherence as a depleting resource creates genuine risk/reward calculations. Opposing operations and N-way collapse create emergent tactical situations. |
| Smooth | ● | Thread ops modify the peninsula's most important clock (MS). Thread-Read advances fieldwork Evidence Track. Knot-mediated remote operations integrate with the socializing system. War-scale Thread ops occur during mass combat Phase 4. Co-movement (temporal, epistemic, actualized) automatically produces cross-system consequences without additional rules. |
| Elegant | ● | Single pool: (Spi×2)+H+TPS. TN encodes operation type (7/8/9). Three-axis Ob encodes scope. Mending immunity derived from philosophy, not patched in. The entire system follows from one metaphysical premise: threads are simultaneously constitutive ground and condition of possibility for rendering. Every rule can be traced to that premise. |

**Verdict:** The system most faithful to the "derive mechanics from metaphysics" methodology. The three-axis Ob is the standout design element — it turns an abstract difficulty number into a meaningful statement.

---

## S14 FIELDWORK

| Criterion | Grade | Assessment |
|-----------|-------|------------|
| Robust | ● | Six investigation actions (Examine, Interview, Research, Surveil, Thread-Read, Reconstruct) each with different attribute pools and risk profiles. Surveil gives +2 Exposure — high reward, high detection risk. Evidence Track with three thresholds (Simple 3, Complex 5, Structural 8) paces investigation naturally. Sincerity Gate (37% failure on instrumental Connect) forces genuine choices about relationship investment. Cover/Exposure creates cat-and-mouse tension. |
| Smooth | ◐ | Fieldwork → Contest: social evidence feeds into contest Corroborate. Fieldwork → Combat: detection triggers ambush (no Defense first exchange). Fieldwork → Thread: Thread-Read advances Evidence Track. These transitions are clean. BUT: Fieldwork → Faction Layer has a gap. Extended investigation has no resource cost — no stamina drain, no health parallel, no opportunity cost except Exposure. A player can investigate indefinitely within a season. Every other system has a depletion mechanic (Wounds/Stamina in combat, Composure/Concentration in contest, Coherence in Thread). Fieldwork is the only system where sustained action has no personal cost. |
| Elegant | ● | PP-632 unification: Bonds governs both Disposition ceiling and Knot capacity via floor(Bonds/2)+1. One attribute, two applications, philosophically grounded. Ob = max(1, base − Disposition) replaces a lookup table with one formula. Sincerity Gate (Spirit TN 7 Ob 1) adds meaningful friction to instrumental relationships with a single roll. |

**Key problem (ED-547):** No resource depletion. The system needs a "Fatigue" or "Attention" track that depletes with extended investigation, forcing players to choose between thoroughness and efficiency. This should be lightweight — perhaps scenes-per-season cap (already proposed at 3-5 in the videogame spec) rather than a new tracked resource. The scene cap IS the fieldwork resource — it just needs to be explicit as a design choice rather than implied.

---

## S15 MASS COMBAT

| Criterion | Grade | Assessment |
|-----------|-------|------------|
| Robust | ◐ | Seven phases give commanders genuine tactical decisions. Formations (6) and tactics (6) create a 36-cell decision matrix. Splitting doctrine (+9-45% advantage) produces a clear dominant strategy that has specified counters (Narrow Pass, Feigned Retreat). Battle consequences (MS −1, IP +2, Political Stability +1) make every battle geopolitically consequential. BUT: the dominant strategy problem is real — splitting is always better unless terrain prevents it. Players will learn this quickly and the tactical variety of formations becomes largely irrelevant once splitting is identified as optimal. |
| Smooth | ◐ | Thread Phase (Phase 4) integrates threadwork into battles. Battle consequences feed directly into peninsula clocks. Unit stats derive from faction Military. These are clean. BUT: the seven-phase structure is the heaviest per-round cognitive load in the entire game. Each phase has its own resolution procedure. At a table, running one round of mass combat takes 10-15 minutes. In the videogame, phases can be automated, but the player still needs to understand what's happening. |
| Elegant | ○ | Seven phases × six formations × six tactics is a large decision space with a known dominant strategy. The unit pool formula (min(Size,Command)+Command) is elegant — it naturally caps effectiveness when depleted. But the overall structure lacks the simplicity of personal combat (split dice, resolve) or Thread operations (three-axis Ob, resolve). Mass combat asks the player to track: unit Size, Power, Discipline, Command, formation, tactic, phase, sub-unit split, general combat pool, Thread phase, cascade, and reform — per unit, per side. |

**Key problem:** Cognitive load. The system is mechanically sound but experientially heavy. Consider collapsing the seven phases to three for BG/videogame: Strategy (formation + tactic selection), Engagement (simultaneous resolution with Thread integrated), and Aftermath (cascade + reform + consequences). The full seven phases can remain in the TTRPG for groups who want granular tactical control.

**Recommendation:** Three-phase compression for videogame. The automation handles the sub-phases internally, but the player's decision points reduce from seven to three.

---

## S06 FACTION LAYER

| Criterion | Grade | Assessment |
|-----------|-------|------------|
| Robust | ● | Five stats (Mandate, Influence, Wealth, Military, Stability) capture a faction's institutional health with no redundancy. The card system (6 cards per faction with cooldowns) creates genuine action economy — you can't do everything, so you must prioritize. Domain expertise (+1D for faction-specific card types) rewards playing to your faction's strengths. Institutional Mandate (Appease at Mandate −1) creates a meaningful "concede the battle to win the war" decision. |
| Smooth | ◐ | Domain Echo connects personal actions to faction stats — clean upward transition. Card cooldowns create temporal pacing. BUT: the Accounting phase (6 sequential steps) is complex. And the faction layer's interaction with peninsular_strain (Accord, Political Stability) adds 4+ new tracks per territory. The total tracked-value count for a 4-faction game with 15+ territories is: 5 stats × 4 factions + 4 tracks × 15 territories + 4 peninsula clocks + faction-specific tracks (VTM, Loyalty, Coup Counter, etc.) = **100+ values**. This is manageable in a videogame (the computer tracks it all) but unwieldy at a table. |
| Elegant | ◐ | Individual mechanics are clean (card cooldown, Institutional Mandate, Stability triggers). But the total system complexity (faction stats + territory tracks + peninsula clocks + faction-specific tracks + card economy + Accounting sequence) is high. Compare to Crusader Kings, which has a similar complexity level but distributes it across a persistent UI with tooltips. The BG version asks a human to track all of it on paper. |

**Key problem:** Value proliferation. The system is robust and well-designed but asks players to track too many values simultaneously. For the videogame, this is fine — the UI handles it. For the BG, consider which territory tracks can be represented on territory cards (Accord, Piety as printed dials) vs. which need separate tracking.

---

## S07 VICTORY & PENINSULAR STRAIN

| Criterion | Grade | Assessment |
|-----------|-------|------------|
| Robust | ● | Universal victory condition (all 15 territories, Accord ≥ 2, Political Stability ≤ 6, 2 consecutive seasons) is elegant — every faction pursues the same goal with different tools. Five acquisition toolkits (Crown Treaty, Graduated Seizure, Dynastic Proclamation, Cultural Reformation, Martial Governance) create genuine asymmetry. Shared loss conditions (Rupture, Altonian Conquest, Anarchy) create cooperative pressure. |
| Smooth | ● | The Accord ≥ 2 gate is the best smoothness feature — it means military conquest (which sets Accord to 1) is self-defeating. Players must govern after conquering, creating a natural pacing brake. Political Stability gates the universal victory condition, meaning violence has a cumulative cost that can prevent anyone from winning. These interlocking gates create organic game rhythm. |
| Elegant | ● | One universal condition. Five tools. Three shared losses. The entire victory architecture fits on one page. Peninsular_strain's contribution is making military conquest structurally expensive rather than arbitrarily prohibited — Accord naturally degrades under occupation, creating a governance challenge that isn't a special rule but a consequence of the system. |

**Verdict:** Possibly the most elegant system at its scale. The Accord gate is the single best balance mechanic in the game — it makes conquest require governance without any "you can't attack" rules.

---

## S10 NPC BEHAVIOR

| Criterion | Grade | Assessment |
|-----------|-------|------------|
| Robust | ● | Seven convictions × four pressure points × eight ethical frameworks create a rich NPC decision space. The three-step decision procedure (Institutional Filter → Conviction Filter → Decision Fork by wound count) is deterministic enough for AI, expressive enough for narrative. PP-NPC-01 through NPC-04 fix real simulation failures. Each NPC's AI priority stack creates distinct behavior patterns — Almud consolidates, Himlensendt asserts, Baralta legislates, Vaynard espionages. |
| Smooth | ● | NPCs read faction stats, territory state, and peninsula clocks for their priority decisions. Contest integration (conviction-modified Ob) means NPC encounters in debate have faction-specific mechanical texture. Disposition/Knot integration means NPC relationships evolve based on player actions, not scripts. |
| Elegant | ◐ | Individual NPC specifications are elegant (conviction + pressure point + ethical framework + beliefs + priority stack). But the total system (13 named NPCs × 7-step priority stacks + 4 Cardinals + Guilds + Niflhel) is large. The Decision Procedure (3 steps) is clean. The Priority Stacks (7 levels each) are necessarily complex because each NPC is a distinct political actor. This is intrinsic complexity, not accidental complexity — but it means running NPC factions at a table requires significant GM overhead. |

**Key problem (reiterated from three_day_audit):** At a physical table with 3 NPC factions, the GM must execute CK3-level AI every season. The videogame handles this natively. The BG needs a simplified NPC decision card (top 3 priorities only, resolve in order, skip if impossible).

---

## S16 EMERGENT ARCS

| Criterion | Grade | Assessment |
|-----------|-------|------------|
| Robust | ● | Vector-based architecture (sustained pressures, not discrete triggers) produces emergent narrative rather than scripted events. 120+ arcs across all scales. The GM doesn't execute arcs — they run pressures and observe what they produce. This is the correct architecture for a game with 100+ tracked values and 18 interacting systems. |
| Smooth | ◐ | Arcs read from every system (the matrix confirms S16 reads all 17 others). This is structurally correct — arcs ARE the cross-system integration layer. BUT: trigger distribution is uneven (Church overtriggered, Crown/Hafenmark/Varfell undertriggered). And Zoom In triggers (5 defined) are grossly insufficient for 120+ arcs. The arc system is smooth at the design level but rough at the implementation level. |
| Elegant | ● | The vector format is elegant: source, direction, modulators, 2-5 sentences. No flowcharts, no state machines, no trigger trees. The simplicity of the format scales to 120+ entries without the format itself becoming unwieldy. Compare to a traditional "event table" approach — those break down at 30+ entries. The vector approach works at 120+ because each vector is self-contained. |

**Key problem:** Implementation gap between arc design and arc experience. The arcs exist as design documents. The videogame needs: trigger evaluation code (partially in ArcEvaluatorRegistry.gd), UI presentation of arc moments, and Zoom In triggers that create personal scenes from arc pressures.

---

## S17 SCALE TRANSITIONS

| Criterion | Grade | Assessment |
|-----------|-------|------------|
| Robust | ○ | Domain Echo (personal → faction) is well-specified: Sufficient Scope → OW ±2, Success ±1. But the reverse direction (faction → personal via Zoom In) has only 5 triggers for 120+ arcs. The scale transition system is half-built: the upward path works, the downward path is skeletal. A player at the strategic layer has no clear signal for when to zoom into a personal scene — the system doesn't tell them "this board state is interesting enough to play out." |
| Smooth | ○ | Domain Echo is smooth upward. Zoom Out is automatic. But Zoom In friction is the project's biggest smoothness failure. When should a territory reaching Accord 0 produce a personal revolt scene? When should CI hitting 55 produce a personal confrontation with Himlensendt? These moments are the videogame's narrative climaxes, and the system doesn't specify when they happen. The three_day_audit called this "the hybrid mode's unkept promise" — that remains accurate. |
| Elegant | ◐ | Domain Echo itself is elegant: one table, four outcome tiers, clear faction stat modifications. But the overall transition system is two elegant half-systems that don't meet in the middle. |

**Key problem (ED-545, P1):** This is the #1 videogame design priority after clock_registry update. The system needs: threshold-based Zoom In triggers (territory Accord 0, CI milestone, MS band transition), NPC-based Zoom In triggers (arc moment, conviction wound, loyalty threshold), and discovery-based Zoom In triggers (Thread Wound formation, Warden contact, POI revelation). Minimum 20-30 triggers to cover the game's narrative surface.

---

## OVERALL ASSESSMENT

| System | R | S | E | Priority Issue |
|--------|---|---|---|----------------|
| Core Engine | ● | ● | ● | None |
| Combat | ● | ● | ● | None |
| Social Contests | ◐ | ◐ | ◐ | Learning curve; needs quick-ref card and UI hints |
| Thread Operations | ● | ● | ● | None |
| Fieldwork | ● | ◐ | ● | No resource depletion (ED-547) |
| Mass Combat | ◐ | ◐ | ○ | Cognitive load; consider 3-phase compression |
| Faction Layer | ● | ◐ | ◐ | Value proliferation; needs UI design |
| Victory/Strain | ● | ● | ● | None |
| CI Political | ● | ● | ◐ | Still PROPOSAL; needs acceptance + merge |
| NPC Behavior | ● | ● | ◐ | GM overhead at table; needs simplified card |
| Emergent Arcs | ● | ◐ | ● | Trigger distribution; implementation gap |
| Scale Transitions | ○ | ○ | ◐ | Only 5 Zoom In triggers (ED-545, P1) |
| Geography | ● | ● | ● | J-7 pending |
| Clocks | ● | ● | ● | Stale file (ED-543, P1) |
| Calamity | ● | ● | ● | POI content needed |
| Military Layer | ◐ | ● | ◐ | Largely a bridge doc |
| Character/Histories | ● | ● | ● | Certainty propagation check |
| Metaphysics | ● | ● | ● | P-03 videogame model (ED-544) |

**Systems that are complete and require no further design work:** Core Engine, Combat, Thread Operations, Victory/Strain, Geography (pending J-7), Calamity, Character/Histories.

**Systems that need targeted fixes (1-2 sessions):** Social Contests (quick-ref card), Fieldwork (resource depletion decision), Clocks (file update), NPC Behavior (simplified table card).

**Systems that need significant design work (3+ sessions):** Scale Transitions (20-30 Zoom In triggers), Mass Combat (phase compression for videogame), Faction Layer (UI information architecture).

**The two critical paths:** (1) Scale Transitions — the videogame cannot ship without Zoom In triggers. (2) Faction Layer UI — 100+ tracked values need an information hierarchy before the game is playable.
