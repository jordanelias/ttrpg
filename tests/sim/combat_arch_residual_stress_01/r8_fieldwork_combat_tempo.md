# R8 — Fieldwork ↔ Combat Tempo Shift
## Module 8 of combat_arch_residual_stress_01

**Date:** 2026-05-10
**Mode:** B (interaction chains)
**Source question:** *"When combat erupts in the middle of fieldwork (investigation, exploration, social engagement), how does the tempo shift work? Does fieldwork state freeze entirely, partial-freeze with selective continuation, or continuous (timers tick during combat)?"*

**Decision shape:** full freeze / partial / continuous

---

## 1. Verification ledger entries

| ID | sim_variable | value | canonical_source | section | quoted_text |
|---|---|---|---|---|---|
| R8-L01 | fieldwork_to_combat_exposure | Combat Exposure: quiet +1, conspicuous +2, public +3 | designs/scene/combat_v30.md | §11.5 F-TRANS-01/09 | "Combat Exposure codified: quiet engagement +1, conspicuous +2, public +3 Exposure to the fieldwork-active character. Applied before the combat scene opens, not during it." |
| R8-L02 | combat_does_not_consume_fieldwork_time | Battle does not consume fieldwork time; only post-combat investigation does | designs/scene/combat_v30.md | §11.5 F-TRANS-12 | "The battle itself does not consume fieldwork time; only the post-combat investigation does." |
| R8-L03 | flight_no_state_reset | Fleeing combat does NOT reset fieldwork state | designs/scene/combat_v30.md | §11.5 ED-576 | "Fleeing combat does NOT reset the player's fieldwork state — any active investigation or social engagement in the territory continues from where it was when combat interrupted." |
| R8-L04 | fled_combat_exposure_persists | Exposure from fled combat still applies | designs/scene/combat_v30.md | §11.5 ED-576 | "Exposure from the fled combat still applies per F-TRANS-01/09 (quiet +1, conspicuous +2, public +3). Flight does not reduce Exposure — witnesses saw the player arrive, even if they left." |
| R8-L05 | post_combat_investigation_one_scene | Post-combat investigation = 1 fieldwork scene | designs/scene/combat_v30.md | §11.5 F-TRANS-12 | "Post-combat investigation of battle site = 1 fieldwork scene." |
| R8-L06 | evidence_degrades_over_seasons | Evidence at fled-combat site degrades +1 Ob/season | designs/scene/combat_v30.md | §11.5 ED-576 | "Evidence degrades: +1 Ob to investigation per season elapsed since the battle." |
| R8-L07 | fieldwork_exposure_section_canonical | Fieldwork §6 Exposure section canonical | designs/scene/fieldwork_v30.md | §6 | "## §6 EXPOSURE" |

---

## 2. Re-asking the question against actual canon

The synthesis R8 question presupposed a spec gap. **Canon already specifies the tempo model.** Per R8-L02 + R8-L03 + R8-L04:

| Element | Behavior on combat ↔ fieldwork transition |
|---|---|
| Fieldwork scene state (active investigation, social engagement) | **Persists** through combat (R8-L03). Resumes from interruption point. |
| Fieldwork time / scene-budget | **Does not tick** during combat (R8-L02). Combat is its own time-scope. |
| Exposure | **Applies on entry** to combat (R8-L01). Persists post-combat — flight doesn't reduce (R8-L04). |
| Evidence at battle site | **Time-degrades** post-combat at +1 Ob/season if fled (R8-L06). |
| Post-combat investigation | **One additional fieldwork scene** at battle site (R8-L05). |

**This is canonical "partial freeze with one-way state coupling":** fieldwork state freezes; some derived effects (Exposure, Evidence) propagate forward into post-combat fieldwork; nothing flows backward (combat doesn't retroactively change fieldwork results).

---

## 3. Candidates

| ID | Name | Description |
|---|---|---|
| **C8.1** | Full freeze | Fieldwork state freezes; Exposure applies but no other propagation. Combat is fully isolated; post-combat returns to exact pre-combat fieldwork state. |
| **C8.2** | Partial freeze (current canon) | Fieldwork state freezes; one-way couplings: Exposure propagates forward into combat (R8-L01); battle-site investigation adds 1 fieldwork scene post-combat (R8-L05); Evidence degrades over seasons if fled (R8-L06). |
| **C8.3** | Continuous tempo | Fieldwork clocks continue ticking during combat (Exposure decay, Evidence freshness, NPC schedules, Heresy Investigation pool ticks). Combat occurs in fieldwork-time. |

---

## 4. NERS at full grain

### C8.1 — Full freeze

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✗ | **S ✗:** contradicts canonical Exposure propagation R8-L01 (Exposure crosses the boundary). Full-freeze means combat is invisible to fieldwork — but witnesses to combat affect Exposure. |
| Bottom-up | ✓ | ✓ | ⚠ | ✗ | **S ✗:** evidence at battle site (R8-L05) is canonical post-combat fieldwork content; full-freeze removes this. |
| Vertical | ✓ | ✓ | ✓ | ⚠ | Mass-scale combat (battle vs. fieldwork-active character) loses the witness-based propagation. |
| Diagonal | ✓ | ✓ | ⚠ | ⚠ | Conviction Scar from witness events in combat (npc_behavior §3.4) cross-couples to social fieldwork — full-freeze breaks this. |
| Lateral | ✓ | ✓ | ✓ | ⚠ | Wound state (PP-716) carries across combat ↔ fieldwork already; full-freeze of fieldwork state is consistent for player-state but breaks for derived effects. |
| Horizontal | ⚠ | ✓ | ⚠ | ⚠ | Cleanest UX (combat is a "diversion") but loses narrative coupling. |

**Verdict C8.1:** N=✓, E=✓, R=⚠ (some), S=✗ on 2 directions + ⚠ on 4. **REJECT — contradicts canonical propagation.**

### C8.2 — Partial freeze (current canon)

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ✓ | ✓ | ✓ | ✓ | Canonical model per §11.5 (R8-L01..L06). One-way coupling spec is complete. |
| Bottom-up | ✓ | ✓ | ✓ | ✓ | Mechanical entries all specified. |
| Vertical | ✓ | ✓ | ✓ | ✓ | Combat → fieldwork transition handles mass-scale via Battle Aftermath / scale_transitions §4.4 (R4-L02 Where Were You retrospective also). |
| Diagonal | ✓ | ✓ | ✓ | ✓ | Wound (R7-L05 carry, PP-716 universal), Threadwork operations during combat all integrate with post-combat fieldwork resumption. |
| Lateral | ✓ | ✓ | ✓ | ✓ | Conviction Scar, Disposition shifts from combat propagate to fieldwork-Socializing as expected. |
| Horizontal | ✓ | ✓ | ✓ | ✓ | Narrative coupling preserved; combat has consequences in fieldwork without making fieldwork tick during combat. |

**Verdict C8.2:** 24/24 ✓. Canonical, mature, coherent.

### C8.3 — Continuous tempo

| Direction | N | E | R | S | Notes |
|---|---|---|---|---|---|
| Top-down | ⚠ | ✗ | ⚠ | ✗ | **E ✗:** dual-clock tracking (combat round-by-round + fieldwork scene-by-scene) imposes substantial bookkeeping. **S ✗:** contradicts R8-L02 ("battle does not consume fieldwork time"). |
| Bottom-up | ⚠ | ✗ | ⚠ | ✗ | Fieldwork timer ticks (Exposure decay, Heresy Investigation pool, NPC schedules) operate at scene-granularity; combat at round-granularity (3-second rounds). Cross-scale rate matching undefined. |
| Vertical | ⚠ | ✗ | ⚠ | ✗ | Mass-scale battle (3-5 BG minutes per R3-L04, or full TTRPG resolution per Part A) doesn't have a meaningful fieldwork-time mapping. |
| Diagonal | ⚠ | ⚠ | ⚠ | ⚠ | Cross-system cascade: a Threadwork operation during combat would tick Coherence + Exposure + fieldwork pool simultaneously. Spec gap. |
| Lateral | ⚠ | ✗ | ⚠ | ⚠ | Stamina, Wounds tick on combat clock; fieldwork-active effects tick on fieldwork clock; rate-matching needed. |
| Horizontal | ⚠ | ✗ | ⚠ | ⚠ | "Realistic" passage of time during combat is satisfying but pays bookkeeping cost on every interaction. |

**Verdict C8.3:** N=⚠ on 6, E=✗ on 5 + ⚠ on 1, R=⚠ on 6, S=✗ on 4 + ⚠ on 2. **REJECT — contradicts canonical R8-L02 + categorical E-fail.**

### Cross-candidate summary

| Candidate | N | E | R | S | Verdict |
|---|---|---|---|---|---|
| C8.1 Full freeze | 6/6 (1⚠) | 6/6 | 4/6 (2⚠) | 0/6 (2✗+4⚠) | **REJECT — contradicts Exposure / Evidence propagation** |
| C8.2 Partial freeze (canon) | 6/6 | 6/6 | 6/6 | 6/6 | **PASS — canonical, mature** |
| C8.3 Continuous tempo | 0/6 (6⚠) | 0/6 (5✗+1⚠) | 0/6 (6⚠) | 0/6 (4✗+2⚠) | **REJECT — categorical multi-axis fail** |

---

## 5. Mode B — Interaction chain analysis

### Chain 1: Fieldwork-active character → combat erupts → Exposure applies

Per R8-L01, on combat entry from fieldwork: Exposure +1/+2/+3 by visibility class. Applied BEFORE combat opens, not during. This means combat resolution happens in its own time-scope; the Exposure tag is the boundary marker.

Under C8.1: only Exposure (and explicit witnesses) propagate; cleaner but doesn't match canon's broader Evidence/Investigation propagation.

Under C8.2 (canon): Exposure propagates forward; battle-site evidence is preserved as a discoverable fieldwork scene (R8-L05); time-decay applies if not investigated immediately (R8-L06).

Under C8.3: Exposure ticks during combat; this contradicts R8-L01 ("Applied before the combat scene opens, not during it").

### Chain 2: Combat ends → return to fieldwork → state resumption

Per R8-L03: fieldwork state persists across combat. Active investigation, social engagement continue from interrupt point.

Under C8.2: clean resumption; one scene of post-combat investigation available at battle site (R8-L05).

Under C8.3: fieldwork has been ticking; resumption is at advanced state (some Exposure may have decayed; some NPC schedules may have shifted). Spec gap on synchronization.

### Chain 3: Player flees combat → no state reset → Exposure persists

Per R8-L03 + R8-L04: fleeing doesn't reset state; Exposure still applies.

Under C8.1: this works — flight is just leaving the combat scene; fieldwork state was frozen, Exposure was already applied at entry.

Under C8.2: same as C8.1 plus the +1 Ob/season Evidence decay clock at battle site (R8-L06). Canonical.

Under C8.3: complications around how much fieldwork-time elapsed during the combat that was fled.

### Chain 4: Combat with multi-character allies → witness Scar propagation

NPC witnesses to combat events generate Scar shifts (npc_behavior §3.4). Under C8.2 these propagate to post-combat social fieldwork as Disposition / Scar shifts. Under C8.1, would NPCs be aware of the combat at all if fieldwork is fully frozen? Spec gap.

### Chain 5: Threadwork operation in combat → Coherence + Exposure + fieldwork pool

Threadwork operations in combat (R1v2-L13 FR Dissolution, witness Scar) generate cross-system effects. Under C8.2 (canon), these resolve at combat scope, then propagate to fieldwork as appropriate state changes (Coherence updates carry; Exposure already applied on entry). Under C8.3, fieldwork pools (Exposure, Heresy Investigation) are concurrently ticking, leading to cross-clock spec needs.

---

## 6. Mode D — Edge cases (compressed)

### Boundary
**EC-D8.B-01 [P3] (any):** Combat that lasts multiple in-game minutes (sustained engagement, multi-zone) — does the time-scope still hold? Per R8-L02, yes; the entire battle is a single scope.

### Cascade
**EC-D8.C-01 [P3] (C8.3):** Concurrent fieldwork-Exposure-decay during combat would mean a long combat reduces Exposure even as combat is generating new Exposure (R8-L01). Self-cancelling pattern.

### Regression
**EC-D8.R-01 [P3] (C8.3):** Players optimize: prolong combat to bleed off Exposure decay. Combat becomes time-laundering tool — opposite of intended.

### Crunch cascade
**EC-D8.CR-01 [P2] (C8.3):** Dual-clock tracking on every combat. Tabletop bookkeeping infeasible.

### Ambiguity
**EC-D8.A-01 [P2] (C8.3):** Rate matching combat-rounds to fieldwork-scenes undefined.

### Incoherence
**EC-D8.I-01 [P1] (C8.1, C8.3):** Both contradict canonical R8-L01 (Exposure timing) and R8-L02 (battle doesn't consume fieldwork time).

### Optimal play
**EC-D8.O-01 [P2] (C8.2):** Player optimal: exploit "battle-site as discoverable POI" by orchestrating battles in target territories then returning seasons later to investigate — Evidence decays (R8-L06) but the discoverable trail persists. Acceptable use of canonical mechanic.

---

## 7. Decision-shape findings

**Recommendation: C8.2 (partial freeze — current canon per §11.5).**

**Rationale:**

1. **C8.2 passes 24/24 NERS** because it IS the canonical model. §11.5 specifies all relevant transitions (R8-L01..L06). The "partial freeze with one-way state coupling" model is mature.

2. **C8.1 (full freeze) fails on S** by removing canonical Exposure / Evidence propagation. It would be a regression from current canon.

3. **C8.3 (continuous tempo) fails categorically**: contradicts R8-L02 (battle doesn't consume fieldwork time), introduces dual-clock bookkeeping, creates time-laundering optimization (EC-D8.R-01), and has unspecified rate-matching between combat-rounds and fieldwork-scenes.

4. **The synthesis R8 question presupposed a spec gap that doesn't exist in canon.** §11.5 specifies the tempo model explicitly. R8 is answered by re-pointing to canonical text.

**Implementation under C8.2 (no mechanical change; documentation):**

- No new spec needed.
- Optional: add a `§11.5 → R8 verified canonical-confirmation` note pointing to the §11.5 ruleset as the answer to "tempo shift" questions in design discussion.

**Decision-shape statement for Jordan ratification:**

> Fieldwork ↔ combat tempo follows partial-freeze model per `combat_v30 §11.5`. Fieldwork state persists through combat (R8-L03); combat does not consume fieldwork time (R8-L02). One-way couplings: Exposure propagates forward into combat at entry (R8-L01); battle-site evidence becomes a post-combat discoverable scene (R8-L05); Evidence degrades +1 Ob/season at fled-combat sites (R8-L06). The synthesis R8 question is answered by re-affirming canonical §11.5 rather than introducing new spec.

---

## 8. Module status

| Item | Status |
|---|---|
| Canonical sources fetched | ✓ |
| Verification ledger (7 entries) | ✓ |
| Re-asked question against actual canon | ✓ |
| NERS full-grain analysis | ✓ |
| Mode B chains (5) | ✓ |
| Mode D edge cases | ✓ |
| Decision-shape finding (C8.2 — preserve canonical §11.5) | ✓ |

**Module 8 status: verified.**
