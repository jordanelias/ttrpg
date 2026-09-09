# VALORIA — UI/UX v4.1 Max-Effort Granular Audit

**Date:** 2026-04-16
**Subject:** `designs/ui/valoria_ui_ux_v4_1.md` (1421 lines; uploaded version)
**Scope of review:** v4.1 against all read v30 design files and both working player-world bridge proposals, measured against "how do we play the game" for each playable moment, tested for **robustness · elegance · smoothness**.
**Method:** Linear pass by UI/UX Part × playable mechanic-set, then integrated whole.
**Evaluation axes (per Jordan's definitions):**
- **Robust** — strategic depth, customization, creativity, player impact, emergent/compelling play without player input.
- **Elegant** — logically simple, clear approach, no overhead.
- **Smooth** — no friction, clean mechanical integration, transitions, cross-system flow.

**Documents read in full:** UI/UX v4.1 (uploaded); player_agency_v30; companion_specification_v30; scale_transitions_v30; integration_proposal_2026-04-15; investigation_systems_proposal_2026-04-15; combat_v30; social_contest_v30; npc_behavior_v30; settlement_layer_v30; threadwork_v30; fieldwork_v30; mass_battle_v30; board_game_v30; clock_registry_v30; peninsular_strain_v1; faction_layer_v30 (structural scan); victory_v30 (structural scan).
**Documents read lightly (secondary reference):** calamity_radiation, geography, southernmost, tc_political_redesign, military_layer, hybrid_gaps, factions_ttrpg.

---

## PART 0 — PLAYABLE-MOMENT INVENTORY

The universe of playable moments the UI must support, derived from the integrated reading of v30 + bridge proposals. Each is a test target in Part 2.

**Personal-scale moments (state Personal, driver player_agency):**
1. Phase 0 Briefing (auto)
2. Phase 1a Duty Assignment — receipt, and at Standing 3+ negotiation
3. Phase 1b Slate Reveal (auto, 4–9 opportunities, with tags)
4. Phase 1c Personal Phase — scene action selection
5. Travel within settlement / within province / between provinces
6. Enter a location / scene
7. Fieldwork — Examine · Interview · Research · Surveil · Thread-Read · Reconstruct
8. Socializing — Read · Converse · Connect · Impress · Rumour · Negotiate · Gift/Bribe
9. Sincerity Gate firing
10. Exposure accumulation + crossing Noticed / Watched / Compromised
11. Dialogue Lattice exploration (bridge proposal)
12. Dialogue escalation → Contest
13. Social Contest — Expert / Crowd / No-adjudicator / Panel / Parliament / Tribunal / Royal Audience / Grand Debate / Chain-contest / Private Negotiation / Personal Appeal
14. Corroboration
15. Obligation binding / tracking / violation
16. Evidence Track progress (Simple 3 / Complex 5 / Structural 8) → Finding
17. Reconstruct synthesis
18. Personal combat — all 12 actions + Leap (for TS 30+)
19. Wound accumulation (ED-548), Stamina depletion, Composure, Momentum
20. Feint / Rescue / Tie Up / Disarm — contested-pool UI
21. Incapacitation Stage 1 / Stage 2 / Death Cascade
22. Thread First-Acquisition scene (v4.1-new)
23. Thread sight toggle (TS 1+)
24. Leap (TS 30+) with 1.5 s transition
25. Diagnosis (before operation)
26. Weaving / Pulling / Past-Oriented Pulling / Locking / Dissolution / Mending / Memory Pull
27. Three-axis Ob builder (Scale × Depth × Distance)
28. Co-movement panel (3 s minimum)
29. Coherence degradation states (10 → 0), Fragmented and Fractured Fallout rolls
30. Dissolution residue use
31. Rendering Crisis arc (Coherence 0 → resolution)
32. Knot formation / Knot strain propagation (P-12) / Knot rupture
33. Taint state (v4.1 claims this — see Finding F-9)
34. Threadcut being encounter (P-06)
35. Monster encounter (P-04)
36. Southernmost entity encounter (P-13)
37. Memory Pull detection by observers (P-09)
38. RS band transitions (100–80 / 79–60 / 59–40 / 39–20 / 19–1 / 0 Rupture)
39. Rupture endgame

**Settlement-scale moments (driver settlement_layer):**
40. Governance action (Develop / Fortify / Pacify / Administer)
41. Subnational faction visibility / management grant / management revocation / contested management contest
42. Settlement event (famine / raid / revolt / flourishing / festival / sermon)
43. Assault / Siege / Bypass on settlement
44. Settlement capture mid-mass-battle
45. Companion-governor delegation (social OR governance, choose one)

**Faction-scale moments (driver board_game / faction_layer):**
46. Strategic Phase — Domain Action selection (Uphold / Appease, targeting)
47. Hand panel view (cards, cooldowns, Casus Belli)
48. Framework Drift pulse (Agent+ only)
49. Cascade Phase — 6-step accounting with animated propagation
50. Domain Echo firing (and the co-reading from Reference Table in integration proposal)
51. Parliament / Lobbying at Standing 3+
52. Treaty Positioning → Concession → Ratification (faction_layer §3.3)
53. Counselor negotiation win (integration proposal Gap 1)
54. Faction leader succession / Leadership challenge (Standing 5)
55. Faction emergence Stage 1–5 (independent path)
56. Faction collapse to city-state

**Mass-scale moments (driver mass_battle):**
57. Mass battle 7-phase resolution
58. Volley / Manoeuvre / Offensive Thread / Engagement / Cascade / Reform
59. General Duel Zoom In (Phase 5)
60. Multi-engagement (3v2 / 4v3)
61. Settlement Defense contribution to Assault pre-battle

**Cross-scale moments (driver scale_transitions + hybrid_gaps):**
62. Zoom In — Priority 0 mandatory trigger
63. Retrospective Zoom In (player not present)
64. Zoom Out
65. Fieldwork → Combat; Combat → Fieldwork; Contest → Fieldwork; Fieldwork → Thread; Fieldwork → Mass; Mass → Personal (General Duel); Scene → Mass (win-modifier carry)
66. BG Survey degree → TTRPG Fieldwork Offset
67. Sufficient Scope threshold crossing (companion +1)
68. Hybrid Coherence binary declaration
69. Contested Figure wound in personal combat → commander +1 Ob

**World-state moments (driver clocks + peninsular_strain + calamity):**
70. RS shader modulation (§9.6 five bands + Rupture)
71. CI appearance / threshold crossings (40 / 75)
72. IP appearance / thresholds / Altonian Preparation / Invasion firing
73. PI (Parliament Integrity) 0–20 (v4.1 does not surface this — see F-11)
74. Calamity radiation proximity 0–5 (v4.1 partially surfaces)
75. GEN (year counter)
76. CD (v4.1 surfaces it — canon absence, see F-9)
77. Generational Shift clock (settlement_layer §7.2 — v4.1 does not surface; see F-12)
78. Church Influence effect display (v4.1 surfaces as CI bar)
79. Convergence Marker firing (COLLISION A/B/C/D)

**Content integrity moments (driver canon principles):**
80. P-03 depth-access gating (render what character can render)
81. P-08 Inert Knowledge for non-sensitives
82. P-12 Knot contagion propagation
83. P-13 Southernmost forgetting (v4.1 §4.5.1)
84. P-15 three-layer being-persistence in Coherence 0 outcomes

---

## PART 1 — WHAT V4.1 GETS RIGHT (concise, so the rest is visible)

Listed briefly because the document is substantially correct and the test below is about where it breaks. All of these pass robust × elegant × smooth:

- **Capability-gated chrome (§2.1).** The mount/unmount-on-signal design is correct. Screen readers, player onboarding, and Jordan's C-3 correction all align. **R / E / S = ✓ / ✓ / ✓.**
- **Scene Slate docked left, priority-sorted entries with tag (§2.5).** Direct rendering of player_agency §4.2. Overflow rule at 12 is a clean invention. **R / E / S = ✓ / ✓ / ✓.**
- **Depth Axis as perception UI (§4.2) — "This is not a menu. It is the character's perceptual horizon rendered as UI."** Correct operational reading of fieldwork §1 and P-03. **R / E / S = ✓ / ✓ / ✓.**
- **Progressive Thread unlock table (§9.1).** Maps cleanly to threadwork §2.1-§2.3 TS gates and Approach Training requirement. **R / E / S = ✓ / ✓ / ✓.**
- **Wound Interval system (§7.1) post-ED-548.** Matches combat_v30 §7 exactly.
- **Coherence only during contact (§7.2, §9.4).** Correct per threadwork Part 3 — Coherence is a practitioner track, irrelevant to non-practitioners.
- **RS environmental rendering (§9.6).** Bands align with threadwork §5.3.
- **Monster encounter UI (§10.1).** Correctly reads P-04 as "rendering failure, not villains" and produces a hex ambiguity that honors it.
- **Southernmost forgetting (§4.5.1 + §10.4).** Strong P-13 translation; the seasonal decay in Journal is elegant.
- **Corrected palette / typography / music (§3.2.1, Appendix C, Appendix D).** Period-faithful, non-anachronistic, setting-grounded.
- **The Integrated Loop walkthrough (§12.2).** The scene-action accounting against ED-548 is correct.

---

## PART 2 — GRANULAR MOMENT-BY-MOMENT TEST

Each test block: **Moment · v4.1 treatment · Robust? Elegant? Smooth? · Finding** (F-##). Findings numbered and severity-tagged (P1/P2/P3) — P1 = blocker for Godot development reference; P2 = needed before next version; P3 = enrichment.

### 2.A — Phase loop (moments 1–4)

**M1 Phase 0 Briefing · **v4.1 §1.1 names it; §1.2 gives 30–60s target, save-on-enter, partial cutscene skip. · **R / E / S = ✓ / ✓ / ✓.** **Pass.**

**M2 Phase 1a Duty Assignment — Counselor+ negotiation · **v4.1 §1.2 notes "Counselor+ may negotiate." §5.3 mentions Duty-aligned row type. §1.3 has "Lobby (pre-Parliament) 1 per target" but no Duty-negotiation cost. **integration_proposal Gap 1 explicitly calls out: "When a Standing 3 player wins a social contest against the faction leader about Duty assignment or faction priorities, what changes?"** The resolution proposes a **Faction Priority Adjustment** — a one-season modification to the faction AI's Priority Stack, with Overwhelming amplifying to two seasons plus a Conviction Wound on the leader.

**Finding F-1 [P1] — Duty negotiation has no UI surface.** v4.1 does not specify: (a) the UI flow for Duty negotiation at Phase 1a, (b) the Priority Stack Adjustment visualization, (c) the leader's Conviction Wound feedback when the player wins Overwhelming. This is a core Counselor-stature loop, specifically the pivot that turns Stature 3 into something mechanically different from Stature 2. Robust: ✗ (blunts Counselor stature's distinguishing feature). Elegant: n/a (absent). Smooth: ✗ (dangling mechanic).
**Repair:** §1.2 Phase 1a should fork — *Operative/Agent flow* = receive Duty card and dismiss; *Counselor+ flow* = receive Duty card with "Negotiate" button that opens an asymmetric Private Negotiation contest (social_contest §2 Step 5 "Private Negotiation" variant; NPC = faction leader; adjudicator = none; primary attribute = Attunement per §3) with faction Priority Stack shown partially (top 3 visible at Counselor; full at Lieutenant+). On Overwhelming: Priority Stack Adjustment card animates onto the faction sheet for two seasons with a visible countdown; leader portrait shows a Scar flicker per §6.2 (the v4.1-specified portrait crack). This is a Hand Panel overlay fired at the faction sheet, not at the chrome right rail.

**M3 Phase 1b Slate Reveal · **v4.1 §1.2 10–15 s target, skippable. §2.5 entry format shown. Priorities 0–4 correct per player_agency §4.2. Companion tag correct.

**Finding F-2 [P2] — Companion commentary on Slate is specified in companion_spec §4.4 but not surfaced in v4.1.** companion_specification §4.4 says "When the Scene Slate is presented each season, each companion states their opinion on 1–2 entries." v4.1 §2.5's example entry format includes `[ Eira : Equity ]` per entry but does not show companion *opinion text* attached to entries, nor does §2.6 Companion strip enumerate Slate commentary as a state. Robust: partial (companion voice diluted to a tag). Elegant: ✗ (tag is a label, not a view). Smooth: ✗ (players will wonder what the tag gives them beyond decoration).
**Repair:** §2.5 should add one-line companion opinion text under the tag, e.g.:
```
●1 Heresy investigation opens  [ Tamm : Order ]
   "This is precisely what we feared. Attend."
●1 Treasury crisis at Gransol  [ Eira : Equity ] ✦ Conviction B
   "The common folk will feel this first."
```
Maximum one companion comment per entry per season; companion chooses one or two entries (not all) per companion_spec §4.4 bound.

**M4 Personal Phase scene selection · **v4.1 §2.5 shows Slate dock with entries; §1.3 gives Scene Action Cost Table with chain rule. **Smooth:** chain rule "highest single cost, not the sum" is a concise resolution of player_agency §6's ambiguity. **Elegant:** single table. **Pass.** **R / E / S = ✓ / ✓ / ✓.**

### 2.B — Travel and layers (moments 5, 6)

**M5 Travel · **v4.1 §3.6 gives explicit transition durations and audio cues per scale. §1.3 costs are correct per player_agency §4.2 (0 within settlement/province; 1 per province traversed; Altonian-adjacent +1 surveillance). **Pass.**

**M6 Enter location (settlement interior → vignette) · **v4.1 §3.4 gives Darklands/Pentiment precedent, depth pips per location, NPCs with Disposition. **Finding F-3 [P2] — Settlement location lists do not indicate NPC schedule (investigation_proposal Drift nodes / npc_behavior Ministry officials with time-of-day routines).** npc_behavior §8.11 + investigation_proposal §2 (Scene-as-Graph §Temporal Dimension) both indicate NPCs move on time cycles — "Archivist at Archives in morning, Court in afternoon." v4.1 §13.7.1 correctly says "NPC availability varies with time. Archivist at Archives in morning, Court in afternoon" but does not show how the location list card expresses this. A player visiting a location in the wrong time slot should see that the target NPC is *not here now*, not merely absent from the NPC list without explanation — otherwise investigation becomes guess-where-they-are.
**Repair:** Location card adds a small time-cue line under each named NPC: "Archivist (here: morning, prayer)" with the current time-of-day highlighted. If the target is not present in the current slot, the card grays them with a "returns at: morning" hint. Preserves spatial-attention gameplay (Lacuna precedent cited in investigation_proposal) without hiding the information.

### 2.C — Fieldwork (moments 7, 10, 16, 17)

**M7 Fieldwork action execution · **v4.1 §4.3 defers to v4. §4.4 Cover & Exposure present. **Robust:** Depth axis present; Thread-Read at Depth 3–5 gated by TS 30+. **Elegant:** one action panel.

**Finding F-4 [P2] — The six fieldwork actions' Exposure projections differ (Examine +0 on Success, Surveil +2 always, Thread-Read +1 always, etc. — fieldwork §4.2 / §6.3) and v4.1 §4.3 claims "Exposure projection on each button" exists but defers the projection's *content* to v4 §4.3.** This is a spec-autonomy failure rather than a missing UI element: v4.1 asserts the affordance's existence ("Exposure projection on each button, confirm-before-commit flow") but an engineer implementing from v4.1 alone has no content to place in that projection. Since Thread-Read fires co-movement *and* Exposure *and* Coherence cost, the pre-commit panel must be uniform — the player is choosing from six actions with radically different downstream cost profiles.
**Repair:** §4.3 should be fully restated in v4.1 (not defer to v4) with a per-action cost matrix:

| Action | Scene-action | Exposure (Success) | Exposure (Failure) | Coherence | RS | Depth cap (at TS 0) |
|---|---|---|---|---|---|---|
| Examine | 0 (within scene) | 0 | +1 | — | — | 2 |
| Interview | 0 (within scene) | 0 | +1 | — | — | 2 |
| Research | 0 (within scene) | 0 | +1 | — | — | 2 |
| Surveil | 0 (within scene) | +2 | +3 | — | — | 2 |
| Thread-Read | 0 (within scene) | +1 | +1 | Per scale table | Per op degree | *blocked* (3+) |
| Reconstruct | 0 | 0 | +0 | — | — | Already-reached |

Displayed as a micro-panel on the button hover, before commit. Resolves Oath II (transparency is not over-explanation) — the numbers are there when hovered, bands by default.

**M10 Exposure thresholds (Noticed / Watched / Compromised) · **v4.1 §4.4 refers to v4. Cover / Exposure are in fieldwork §6.2. Cover = Cognition + concealment History; thresholds are Cover-scaled per fieldwork §6.1.

**Finding F-5 [P1] — Exposure is territory-scoped per fieldwork §6.2, but v4.1 does not surface a per-territory Exposure view.** The Left context panel is said to "display during fieldwork — unchanged from v4" but the rule "per territory, per season" means the player may have Exposure 6 in T8 (Watched threshold for Cover 4–5) and Exposure 0 in T9 simultaneously. A single Exposure bar is misleading.
**Repair:** §4.4 should specify a multi-territory Exposure strip — one per territory the character has acted in this season, collapsed by default to current territory with expand-on-click showing all non-zero territories. Season reset should visibly empty the strip at Phase 0 Briefing as a small animation (fieldwork §6.4 "Reset to 0 in all territories").

**M16 / M17 Evidence Track + Reconstruct · **v4.1 §4.6 specifies 3 / 5 / 8 node templates, which matches fieldwork §4.1. **Elegant.** The Case Board from investigation_proposal §Scene-as-Graph is absent as a concept — v4.1 uses "Reconstruct templates" instead. These are not the same.

**Finding F-6 [P2] — The Case Board spatial visualization from investigation_proposal §"The Case Board" is collapsed into v4.1's "Reconstruct templates" without preserving the spatial accumulation affordance.** investigation_proposal §Case Board specifies evidence discovered in nodes appears on "a visual Case Board — a map of connected facts" where connections are drawn via Reconstruct, and the board is persistent across seasons. v4.1 §4.6 says "3 / 5 / 8 evidence slots + synthesis branches" but makes the Reconstruct a discrete action that fires only at threshold — not a persistent spatial artifact that the player reads between scenes. **Robust:** ✗ (loses the pinboard affordance that connects evidence emerging in different territories — fieldwork §4.1 says "One track per investigation, regardless of territory").
**Repair:** §4.6 should specify Case Board as a persistent view accessed via `J` (Journal) or a tabbed subview: nodes for each Evidence added (showing territory of origin, reliability tag, and Thread-verified status); Reconstruct draws visible connections between nodes; the board auto-arranges but is player-draggable; the "synthesis branches" of the template are rendered as target regions where connected-node clusters accumulate. Simple/Complex/Structural templates drive the target slot count (3/5/8), but the board itself is free-form beneath. **This also resolves UI-12 more thoroughly than v4.1's claim.**

### 2.D — Dialogue (moments 11, 12)

**M11 Dialogue Lattice · **v4.1 Part 5 renders "Disco-Elysium Conviction interface" with 8 row types. This is the ***most important structural gap* in v4.1.*** investigation_proposal §System 3 specifies a Dialogue Lattice with *seven gate types* (Attribute, Evidence, Belief, Truth, History, Disposition, Thread Sensitivity), *visibility rules* (visible-locked vs hidden), *six outcome types*, plus a *five-filter Response Matrix*. v4.1's 8 row types overlap with this only partially — v4.1 has Conviction-driven / Framework-aligned / Belief-targeted / Negotiate / Walk away / Locked (Conviction) / Locked (prereq) / Mechanical social action.

**Finding F-7 [P1] — v4.1 Part 5 conflates player_agency Convictions (author-stated) with the Dialogue Lattice's differentiated gate system.** v4.1 has only two "lock" categories (Conviction vs prereq), whereas investigation_proposal §Gate Types demands seven distinct gate types with different visibility rules (Attribute/Evidence/History gates always visible-locked; Truth/TS gates hidden at extreme distance, visible-locked when close). **Robust:** ✗ (the seven-gate richness produces character-state-dependent conversation options — "orthodox utterances available at Truth ≥ 4" is a structural feature, not a Conviction lock). **Elegant:** partially — v4.1's 8-row taxonomy is simpler but *at the cost of the gate structure*. **Smooth:** ✗ (player cannot tell why an option is locked — investigation_proposal's visibility rules give the "Requires: Evidence [name]" / "Requires: Cognition 4+" hints that v4.1 compresses into just "prereq").
**Repair:** §5.3 should be rewritten to align with investigation_proposal §Gate Types, either by adopting the 7-gate taxonomy directly or by adding a **gate sub-type column** to v4.1's 8-row table that specifies which gate(s) apply. The visible-locked hint text is the single most important affordance in the Dialogue Lattice — it is what turns exploration into a legible pursuit (investigate to unlock Evidence-gated utterances; build Disposition to unlock Disposition-gated utterances). Without it, Part 5 is a Disco-Elysium skin on a system that behaves like a standard dialogue tree.

**Finding F-8 [P2] — The Sincerity Gate (fieldwork §5.3 + investigation_proposal §Sincerity Gate Integration) has no v4.1 UI surface.** This is the most-cited mechanic in the entire game (integration_proposal Part 11 names it "The finest single mechanic in the design"). v4.1 Part 5 does not explicitly render the [SINCERE] / [INSTRUMENTAL] tagging on options, nor does it specify what the player sees when Spirit TN 7 Ob 1 fires. **Robust:** ✗ (the mechanic fires invisibly; the player feels a Disposition drop without understanding the cause). **Elegant:** n/a. **Smooth:** ✗.
**Repair:** §5.3 should add a row type and a firing animation. Row: "Instrumental [gold-dice icon, Spirit roll preview]" — visibly marks the option as Spirit-gated before selection. On click: brief inline roll animation showing the Spirit check result. On Failure: NPC portrait subtly recoils; on Success: normal proceed; on Overwhelming: a "Genuine interest" pip appears offering a Belief revision opportunity per fieldwork §5.3 Overwhelming outcome. Belief-gated utterances auto-tag [SINCERE] and bypass the gate; this should be visible as an ✦ adjacent to the row (same mark as the Conviction mark in v4.1 §5.3).

**M12 Dialogue → Contest escalation · **v4.1 §5.7 notes escalation as one of four scene-end modes. integration_proposal §"The Dialogue Lattice Escalation Moment" specifies this should be *environmental* — "camera angle shifts slightly, NPC idle animation changes, ambient sound drops, dialogue options update to show Contest framing." v4.1 §12.1 has `Contest → Combat ... Initiative rolls; hex grid fades in ... 0.8s` and `Investigation → Contest ... ESCALATE TO CONTEST button ... 0.5s fade`. The **ESCALATE TO CONTEST button is wrong.** It announces the state change via text — violating Oath III.

**Finding F-9 [P1 per Jordan's C-1 / Oath III] — The ESCALATE TO CONTEST button violates Oath III.** Oath III: "The game is felt, not narrated. State changes are shown before they are labeled." A button labeled "ESCALATE TO CONTEST" does exactly what Oath III forbids. integration_proposal has this right.
**Repair:** §12.1 transition should be environmental — when the player selects a dialogue option whose content triggers §5.7 escalation (exceeds informal negotiation threshold *as assessed by the contest's Piety Track starting conditions*), there is no button; the response options silently update to Contest framing (now showing Appraise result, style options) and the environment shifts (palette desaturates slightly, audio bed drops, NPC portrait reframes). Scene transition audio fires *after* the shift as confirmation. The **Walk away** row type in §5.3 serves as the ejection hatch before commit. If the player wants to explicitly escalate rather than have the system detect escalation, a low-profile "Press the point" row type (Negotiate-style) may appear when Piety Track offset ≥ +1 — this is their commit, not a modal button.

### 2.E — Social Contest (moment 13)

**M13 Contest (all 9 variants) · **v4.1 Part 6 consolidates Parliament / Tribunal / Royal Audience / Treaty / Casual / Private Negotiation / Personal Appeal / Grand Debate / Guild Arbitration into one generic interface. social_contest §2 Step 5 lists nine proceeding types. This is correct in direction.

**Finding F-10 [P2] — The generic contest interface collapses per-variant asymmetries that matter mechanically.** social_contest §6.3 (Inquisition Hearing) says "Accused has no corroboration. Exchange count set by Inquisitor (1–5). Piety Track starts biased at 6." v4.1 §6.3 mentions "no Corroboration, no Findings, Church Obscuring boost, halved audience resistance." But it does not show *what the accused sees* — specifically that their Corroborate button is absent, their Finding citation ribbon is absent, their starting Piety Track is biased, and the Inquisitor's genre/style selection is predetermined (Inquisitor proposes throughout per social_contest §2 Step 5 table). v4.1's generic §6.1 exchange surface will wrongly suggest the accused has the same options as in a Formal Contest. **Robust:** ✗. **Elegant:** partially. **Smooth:** ✗ (asymmetry surface mismatched with asymmetry mechanics).
**Repair:** §6.3 should give a per-variant variation spec table — for each of the 9 proceeding types, which generic-surface elements are hidden/modified/added. Minimum viable: (1) Tribunal (accused): Corroborate button absent, Finding ribbon absent, Track visual starts at 6 with gold bias mark, Inquisitor portrait outsized with exchange-count dial set by Inquisitor. (2) Royal Audience (petitioner): Resistance halved (rendered as fainter audience bar), petitioner *may* Corroborate (may-not default to cannot). (3) Private Negotiation: no adjudicator panel, no Track (unless opted in), Attunement-primary indicator. (4) Grand Debate: Parliament-as-Crowd adjudicator overlay.

**Finding F-11 [P1] — The Style Decision UI from integration_proposal §Part 9 is wholly absent.** This is integration_proposal's H-6 "High Value" recommendation: reduce the 30-second genre × orientation decision to a 5-second plain-language choice:
- "Cite the record" (Memory + Revealing)
- "Show the future" (Projection + Revealing)
- "Raise the doubt" (Memory + Obscuring)
- "Anchor the fear" (Projection + Obscuring)

v4.1 §6.1 specifies "Style selection (Memory/Projection × Revealing/Obscuring)" in 10-step exchange — the raw mechanical naming. This is exactly what integration_proposal §Part 9 calls out as "the central cognitive load of the contest system." At the TTRPG layer it's fine; at the videogame layer it is a documented friction point. **Robust:** preserved (the mechanic still works). **Elegant:** ✗ (four-cell matrix with jargon). **Smooth:** ✗ (30-second cognitive load per exchange; Contest is 3–5 exchanges).
**Repair:** §6.1 Step 2 should add the four plain-language buttons above, each labeled with the underlying style in smaller secondary text for mechanical transparency. Appraise result (§6.1 Step 1) surfaces as advice below the choice: "The crowd is responding to demonstrations of past precedent [Cite the record advantaged]." Maps directly to integration_proposal §Part 9 resolution.

### 2.F — Personal Combat (moments 18–21)

**M18 Combat actions list · **v4.1 §7.5 says 12 actions, dimmed actions show unlock condition on hover, Leap appears at TS 30+ with Approach Training. Correct. **Pass.**

**M19 Wound/Stamina/Composure/Momentum · **v4.1 §7.2 HUD matches combat §7 derived values. ED-548 formula present. **Pass.**

**M20 Feint / Rescue / Tie Up contested-pool UI · **v4.1 does not specify how these appear. combat §4 is complex: Feint requires dice commit + contested roll producing opponent pool reduction; Rescue requires eligibility check (outnumbered at Phase 1), dice commit, contested roll, and chain-block rules; Tie Up requires Strength contest to escape.

**Finding F-12 [P2] — Contested-pool manoeuvres (Feint, Rescue, Disarm, Tie Up) have no v4.1 UI surface.** These are the tactical-depth actions of combat. A player selecting Feint needs to see (a) the dice-commit slider (N minimum 3 to Offence), (b) the opponent's Defence pool estimate (hidden until roll), (c) the projected pool-reduction magnitude. For Rescue, eligibility must be checked on hover (outnumbered / chain-block). **Robust:** ✗ without this the tactical layer collapses to Strike / Full Guard / Take a Breath. **Elegant:** n/a (absent). **Smooth:** ✗.
**Repair:** §7.5 should specify a manoeuvre sub-panel: selecting Feint opens an inline dice-commit slider (min 3, max = current pool − 1 so at least 1D Defence remains); hovering opponent-targeted manoeuvres shows the eligibility check result ("Eligible: outnumbered 2:1"), or the reason for ineligibility. Disarm / Tie Up / Retrieve / Establish Distance / Escape each have their own contested-pool preview. The confirm-commit flow matches §4.3 fieldwork but with the dice-commit widget.

**M21 Incapacitation & Death Cascade · **v4.1 §7.6 points to v4 for Death Cascade; §13.2 notes Death Cascade triggers cutscene only when the dead NPC was central to an active Conviction. combat §13.3 gives a full 5-step cascade (immediate Knot rupture / Priority 1 Scene Slate entries / faction Stability trigger / +2 Exposure in NPC's relational network / player Conviction test).

**Finding F-13 [P1] — The 5-step Death Cascade per combat §13.3 is not explicitly rendered in v4.1.** v4.1 says "For non-Conviction-related deaths, the 5-step Death Cascade panel plays without cutscene" but does not say what those 5 steps look like. The steps are: (1) Knot rupture visual, (2) Slate entry animation showing new Priority 1 entries added, (3) faction sheet Stability tick, (4) Exposure strip ticking across multiple territories, (5) player Conviction strain/revision prompt. Each needs to be visible for players to understand why their action had faction-scale consequence. **Robust:** ✗ (invisibility of consequences destroys learning). **Elegant:** partial (the 5-step exists). **Smooth:** ✗ (animation sequence absent).
**Repair:** §7.6 should specify the 5-panel Cascade sequence explicitly; not defer to v4. Each step 0.8–1.2 s, total ≤ 6 s; the Cascade is not a cutscene but a deterministic animated-state-change accounting — the same idiom as Phase 3 Cascade Accounting (v4.1 §1.2 "animated 5-step accounting") but scoped to a death. Step 5 (Conviction test) opens the Restate/Transform/Abandon modal per §11.3 — same prompt normally seen at Phase 4 Aftermath, fired immediately when the death was Conviction-relevant.

### 2.G — Thread (moments 22–39)

**M22 First Thread acquisition scene · **v4.1 §9.1 adds this. Correct, new, good.

**M23 Thread sight toggle · **v4.1 §9.2 correctly notes I-02 "always-payoff" — every location has a Thread signature. **Pass.**

**M24 Leap · **v4.1 §9.3 1.5 s transition spec is good. Leap commit modal shows pool, TN, Ob, vulnerability window — per Oath II. **Pass.**

**M25 Diagnosis · **threadwork §2.2 "Diagnosis precedes Leap" — struck / reordered. v4.1 does not surface a Diagnosis action, but the "Diagnosis occurs here (public declaration = rendering the configuration)" rule exists in mass_battle §A.7 Phase 1. In personal Thread operations Diagnosis is implicit.

**Finding F-14 [P3] — Pre-Leap Diagnosis is not surfaced as a separate UI act.** threadwork §2.2 marks Diagnosis as preceding the Leap ("Revised standard sequence (Diagnosis precedes Leap)"). v4.1 §9.3 surfaces only the Leap commit modal. For UI-visible Diagnosis: before commit, show the target configuration with its current Depth / Scale / Distance estimate and the three-axis Ob projection. This is partially present in §9.4 "Pre-commit co-movement preview" but Diagnosis is specifically the act of reading-the-configuration that produces the estimate. **Robust:** modest gain. **Repair:** §9.3 should include a brief Diagnosis preview panel — essentially a pre-Leap inspection showing target configuration properties. Non-blocking; addresses P-01 compliance more fully by making the intent-formation transparent.

**M26 Operations (Weave, Pull, POP, Lock, Dissolution, Mending, Memory Pull) · **v4.1 §9.4 covers panel + three-axis Ob. §9.8 covers CD display. §10.3 covers Memory Pull detection.

**Finding F-15 [P1 — CANON COMPLIANCE BREACH] — v4.1 §9.8 surfaces a "CD (Calamity Drift)" track that is not in the canonical clock registry.** clock_registry_v30 §Shared Clocks lists exactly: RS, CI, IP, PI. There is no CD. threadwork mentions "Calamity Drift" historically but it was replaced — see threadwork §8.1 "ThS / CD (§5.9, 20→0) ... → Coherence (10→0) ... Campaign tracking eliminated as separate system." **CD as a distinct track does not exist in current canon.** v4.1 §9.8's "CD this session: 3 / — (no threshold yet)" is a confabulation. (The History Resonance mechanic from threadwork §4.4 still exists, but it is not "CD.")

**Repair:** Delete §9.8 entirely. The Thread-contact HUD should show Coherence (10 → 0) during contact per §9.7, and History Resonance risk die results as they fire. The "CD contribution to next RS tick" is not a mechanic — RS degradation sources are enumerated in threadwork §5.2 (per-op degree, chronic drift from Locks, winter annual drift, Gap persistence, etc.), none of which are a "CD clock."

**Finding F-16 [P1 — CANON COMPLIANCE BREACH] — v4.1 §9.7 surfaces a "Taint (0–6 per threadwork §16)" as a practitioner track distinct from Coherence.** threadwork §3.4 explicitly replaces Taint with Coherence: "*Replaces §5.10 (Taint track) and §5.11 (Dissolution Residue). No separate Taint track.*" threadwork §8.1 Systems Replaced: "Taint (§5.10, 0→10) → Coherence (low-end effects) ... No separate track. Dissolution residue = accelerated Coherence loss." There is no "threadwork §16" in the current document; what exists is §3.4 Dissolution Residue, which is not a 0–6 track but a potency rating (1–5) attached to residues acquired from Gaps. **v4.1 is reintroducing a dead system.**

**Repair:** Delete the Taint references in §9.7 and §11.3. The "Belief shows transformation-candidates ghosted above current Beliefs" effect that v4.1 attributes to "Taint 4+" should be relocated to Coherence ≤ 3 / ≤ 2 per threadwork §3.3 (where Belief Co-Authorship begins at Coherence 2 / Fractured). The character sheet's practitioner block correctly shows Coherence, Thread Sensitivity, Approach Training — Taint is removed. P-10 is about *Coherence vs persona* per canon, not Coherence vs Taint — this was a misread of P-10.

**Finding F-17 [P2] — v4.1 §13.7.3 entry threshold is Coherence ≤ 5, which excludes the upper half of the canonical Dissonant band (7–5) per threadwork §3.3.** threadwork §3.3 Dissonant 7–5: "Narrative flickers: wrongness, déjà vu, events slightly out of sequence. Close Knots sense wrongness (+1 strain per 3 sessions)." Knot-strain propagation begins at Coherence 7, not 5. v4.1 §13.7.3 line 1138 triggers Layer 3 at "Coherence ≤ 5 OR in Thread contact OR in RS ≤ 40 territories" — missing Coherence 6 and 7. **Robust:** ✗ (narrative-flicker band silent). **Elegant:** partial. **Smooth:** ✗ (Knotted companions begin suffering strain at Coherence 7 with no visible cue).
**Repair:** §13.7.3 threshold changes from "Coherence ≤ 5" to "Coherence ≤ 7." The 5 ambient bullets (animation slow, drone, tensile lines, NPC desaturation, hermetic typography) apply uniformly across the Dissonant band. Per-state changes at Coherence 4 / 2 / 1 / 0 remain as specified. Additionally, §9.9 Knot strain pips should tick visibly at Dissonant entry (Coherence 7) — not wait for Fragmented.

**M27 Three-axis Ob builder · **v4.1 §9.4 correct. **Pass** (modulo F-15/F-16 which affect HUD, not the builder itself).

**M28 Co-movement panel · **v4.1 §9.5 3-s minimum cannot-dismiss-early. Matches co-movement Version C per threadwork §4. **Pass.**

**M29 Coherence degradation UI · **v4.1 §9.7 table + §13.7.3. See F-17 above.

**M30 Dissolution residue · **Canonical per threadwork §3.4 (potency 1–5, bonus dice to pool, volatile 9-10 explode, -1 Coherence per use cap-exempt). v4.1 does not surface residue acquisition or use.

**Finding F-18 [P2] — Dissolution residue acquisition and use has no v4.1 UI surface.** A practitioner who has performed Dissolution operations may have residue tokens to bank — these are a meaningful strategic resource (Niflhel arm specifically harvests them per board_game §co-movement card 18). Using residue is a decision with cost (−1 Coherence, +1 Ob per prior use of same source, volatile dice).
**Repair:** §9.4 Thread panel should add a Residue inventory at low-prominence: icon row of residue tokens with potency rating; clicking adds to pool with animated warning-glyph for volatility. If none held: row is hidden (capability-gating).

**M31 Rendering Crisis arc · **PP-194 specifies Coherence 0 arc = full season of non-practice + 3 Anchoring Scenes + resolution roll. v4.1 §9.7 says only "Cutscene fires — TS-branched outcome."

**Finding F-19 [P2] — The Rendering Crisis arc (threadwork §3.7) is collapsed into a single Coherence 0 cutscene in v4.1 §9.7.** This is a multi-scene, multi-season arc with player agency (withdraw from practice, seek Anchoring Scenes with Close Knots, roll Bonds pool vs Ob 3 at Accounting). The outcome is not purely TS-branched — it is based on roll degree (Failure = NPC, Overwhelming = Coherence 4 + permanent −1 TS, etc.). v4.1 is at once overspecifying (TS branching) and underspecifying (no arc UI).
**Repair:** §9.7 Coherence 0 row should not be a cutscene terminus but an arc entry: fires a mandatory Priority 0 Slate entry "Rendering crisis" that persists until arc resolution; the character sheet's practitioner block gains a visible "In crisis (season N of 1, Anchoring Scenes 0/3)" indicator; Close Knots gain an "Anchor" action available once per session (costs the Knot +1 strain per Anchoring Scene per §3.7). At Accounting after conditions: roll panel fires with Bonds-based pool vs Ob 3. *Then* cutscene per degree result. PP-206 guidance (TS 30–31 risk warning at arc start) must appear as a confirmation modal before the arc begins. **This is the most consequential missing arc in v4.1.**

**M32 Knot formation / strain / rupture · **v4.1 §9.9 silver-thread visualization, strain pips (silver → gold → red), rupture cutscene. §11.5 Knot graph for P-12 contagion. **Robust:** ✓ graph is a good affordance. **Smooth:** ✓. 

**Finding F-20 [P2] — Knot formation procedure (fieldwork §5.6 + npc_behavior §6.3 / ED-391) is not surfaced.** v4.1 §11.5 says "Companion cap 2. Connection action during social scene: requires Disp +3, not faction leader, not under active Heresy Investigation, 2+ prior scenes." But fieldwork §5.6 says Knots require **Thread contact** (both parties TS ≥ 30; non-sensitives at Disp +5 get +1D but no Knot). This is a different gate from Companion eligibility. A companion at Disp +5 with TS 0 and a player with TS 0 cannot form a Knot. v4.1's current §11.5 makes it look like Connection action → Knot path, which is wrong.
**Repair:** §11.5 should separate Companion Connection (Disp +5 relational depth) from Knot formation (TS ≥ 30 both parties + thread contact ritual). Add a "Knot candidate" chip in the companion strip when Disp +5 is reached, which opens into a Knot Formation action only if TS gate is met. Non-sensitive companions cap at Disp +5 without Knot and with +1D only (fieldwork §5.6). Thread-aware players can Knot with an npc who has TS ≥ 30 following the fieldwork §5.6 procedure.

**M33 Taint — superseded per F-16 above.**

**M34 Threadcut being · **v4.1 §10.2. "Wound Interval bar replaced with Thread cost accumulating — 0 / ? operations to sever." Correct direction per threadwork Part 6, which specifies that threadcut beings do not accrue Wounds normally and require sustained Thread work to de-actualize.

**Finding F-21 [P3] — Rendering Strain (threadwork §6.2 + §6.4) for threadcut beings is not surfaced.** threadwork §6.4 gives explicit De-Actualization sequence (Round 1–3 phasing) and Rendering Strain accumulation (each scene of beyond-ceiling rendering +1). For TS 30+ observers watching a threadcut being render beyond the observer's ceiling, there is additional scene-by-scene accrual of the being's self-cost. v4.1 §10.2 names "Thread cost accumulating" generically; the actual mechanic is Rendering Strain with a specific formula.
**Repair:** §10.2 should name the stat as Rendering Strain, show it with a specific cap = Health of the being (per threadwork §6.2), and indicate De-Actualization cascade when Strain = Health. The observer-dependency (rendering-ceiling per observer TS per §6.2 table) must be shown — TS 50+ sees one thing, TS 70+ sees more. Partial rendering to non-sensitives *is the UI state* — a red-outlined hex for a TS 0 observer, a partial figure for TS 10–29, full figure for TS 30+. v4.1 §10.2 does not capture the observer-dependency.

**M35 Monster encounter · **v4.1 §10.1. Correct reading of P-04. **Pass.**

**M36 Southernmost entity · **v4.1 §10.4. Forgetting handled via §4.5.1. **Pass.**

**M37 Memory Pull detection · **v4.1 §10.3. Correct per P-09. **Pass.**

**M38 RS band transitions · **v4.1 §9.6 five-band shader table matches threadwork §5.3. **Pass.** Environmental rendering modulation is a **core robust element** — the Peninsula breathes with the substrate.

**M39 Rupture · **v4.1 §9.6 RS 0 row "Cutscene fires — see §13." §13.2 implies 22 mandatory triggers + Convergence Markers; Rupture is among them but not explicitly bulleted.

**Finding F-22 [P2] — Rupture endgame cutscene is named but not specified.** threadwork §5.3 RS 0 row describes Rupture as the campaign-ending catastrophe, and §5.3 has the critical "design note" that this is a designed 2–4 season endgame trap once RS enters Critical. The cutscene should respect this — Rupture is not a single climactic moment but the closing act of a multi-season decline the player has felt for 4–8 seasons. v4.1 does not specify anything beyond "cutscene fires."
**Repair:** §13 should list Rupture as one of the 22 mandatory cutscenes with bespoke treatment — 3-minute duration (matching Convergence Marker tier per §13.3). Additionally, the RS Critical band (19–1) needs a sustained UI signal — not merely the §9.6 "Map aberration" but a per-season "Crisis Accounting" banner showing RS progression with projected Rupture season (based on current trajectory of Locks-drift + spontaneous Gaps + Winter). This transforms the endgame trap into a legible crisis.

### 2.H — Settlement scale (moments 40–45)

**M40 Governance action (Develop / Fortify / Pacify / Administer) · **v4.1 §11.2 docks Governor Panel to left in settlement view. Says "Governance action this season (free, mandatory): Develop / Fortify / Pacify / Administer. Each resolves via roll." settlement_layer §3.2 gives the full Ob formulas and degree-specific effects.

**Finding F-23 [P2] — Governance action pre-commit preview is absent.** settlement_layer §3.2 gives explicit Obs: Develop Ob = floor(Prosperity/2) + 1; Pacify Ob = floor((3 − Order) + 1), min 1; Administer Ob = 2 (+ reveals one local NPC's Conviction on success); Fortify Ob = floor(Defense/2) + 1. Each uses different attributes (Cognition / Military-stat / Charisma / Attunement). The player selecting needs to see: current settlement stats (Prosperity/Defense/Order), pool, Ob, degree projection. Currently §11.2 says "Each resolves via roll" — no preview. **Robust:** ✗. **Elegant:** partial. **Smooth:** ✗.
**Repair:** §11.2 Governor Panel spec: stat block for the governed settlement at top (P/D/O values with caps-by-type); four action buttons with Ob + pool preview; confirm-commit modal with degree bands. Matches the fieldwork §4.3 confirm-commit idiom for consistency.

**M41 Subnational faction management · **v4.1 §3.3 covers the `?` Niflhel ambient cue (UI-15). §11.2 says "Subnational delegation" is one of the governor actions. settlement_layer §3.3 gives the grant / revoke / contested management structure (Domain Actions, Ob = subnational Influence ÷ 2, Order −1 + Disposition −2 on revoke). The contested case resolves through social contest.

**Finding F-24 [P2] — Subnational management grant / revoke / contest is not a first-class UI flow.** This is the mechanism by which Church holds Cathedrals in non-Church provinces, Guilds manage Markets, RM covertly holds Outposts. The Govern panel at province level needs a settlement-subnational action; the province-faction-leader needs a visibility on which of their settlements are subnational-managed and how. **Repair:** Province panel (§3.3) adds a "Subnational management" strip listing each settlement's governor (faction or subnational actor), with a `Grant/Revoke` affordance for the province-controlling faction (Counselor+ only). Revoke action opens a confirmation modal showing the Order and Disposition costs. Contested management fires a social contest per §6 with the institutional asymmetry pre-configured (province faction as advantaged / subnational as petitioner).

**M42 Settlement event · **settlement_layer §4.3 gives 7 event types firing from settlement stat conditions (Prosperity 0 famine, Defense 0 + hostile adjacent raid, Order 0 revolt, Order 5 + Prosperity 4+ flourishing, Cathedral + CV change religious event, Mine + Prosperity 3+ surplus, Fortress + hostile mobilization).

**Finding F-25 [P2] — Settlement events should fire as Priority 4 Slate entries with settlement-specific framing.** v4.1 §3.4 settlement interior cards name "Active Slate anchor" at location level — but this is settlement-level, and the Slate entry should carry the settlement's event as its Priority 4 framing (settlement_layer §4.3 says "These feed into the Scene Slate at Priority 4 (Territorial)"). v4.1 §2.5 Slate dock Entry format does not show settlement anchoring. integration_proposal §Mechanism 2 explicitly calls out settlement-anchored Slate generation as foundational.
**Repair:** §2.5 Entry format should add a settlement-prefix option and an event-type icon:
```
●4 [S-017 Gransol Market] Trade fair  ●FLOURISHING
●4 [S-010 Stillhelm] Granary rot      ●FAMINE
```
Settlement anchor is clickable — opens the settlement view directly. Event icon is standardized across the 7 settlement event types. This matches investigation_proposal §Scene-as-Graph's Anchor node concept: the scene has a spatial anchor point, named and locatable.

**M43 Assault / Siege / Bypass · **v4.1 §8.4 names the three options; says Bypass locked unless Military > Defense + 3. settlement_layer §5.1 confirms: Military vs Defense + garrison, siege reduces Order −1/season to 0 → surrender, Bypass requires Military > Defense + 2. (v4.1 says +3; settlement_layer §5.1 says +2+ for bypass. Inconsistency.)

**Finding F-26 [P2 — NUMERIC UNDER-DISTINCTION] — v4.1 §8.4 states a single "Bypass locked unless Military > Defense + 3" but settlement_layer §5.1 gives two thresholds.** settlement_layer line 237 (general rule): "Bypass | Military > Defense by 2+." settlement_layer line 241 (Fortress-specific): "A Fortress settlement in the invader's path forces engagement — it cannot be bypassed unless the invader's Military exceeds the Fortress Defense by 3+." v4.1's single `+3` rule is canonically correct for Fortress bypass but over-restrictive for non-Fortress settlements (which should be `+2`). A Town with Defense 2 should be bypassable at Military 5 (canon: +2+), but v4.1 locks bypass until Military 6.
**Repair:** §8.4 should split the rule: "Bypass (non-Fortress): Military > Defense + 2. Bypass (Fortress): Military > Defense + 3." The example "Lowenskyst Fortress (S-006, Defense 4) requires Military 7+" is correctly derived from the Fortress +3 rule and should be retained.

**M44 Settlement capture mid-mass-battle · **v4.1 §8.4 specifies "Settlement capture mid-battle fires side-panel notification, does NOT interrupt current Phase (resolves UI-09)." ✓ per settlement_layer §5.

**M45 Companion-governor delegation · **v4.1 §11.2 "Companion governance animation (resolves UI-14)." Mentions Phase 3 Cascade 2-s overlay. companion_specification §4.1 specifies "1 free action per season that can be used as EITHER a social fieldwork action (companion role) OR a governance action (governor role)" — meaningful trade-off.

**Finding F-27 [P2] — Companion-governor trade-off (social vs governance) is not surfaced at selection time.** companion_specification §4.1 gives the player a per-season choice. v4.1 §11.2 only describes Phase 3 result overlay, not the selection. **Repair:** At Phase 1c Slate reveal, the companion strip shows an "Assignment" radio for any governor-companion: Social (default) / Governance (at S-nnn). Mousing over shows the opportunity cost. Selected Assignment propagates to Phase 3.

### 2.I — Faction scale (moments 46–56)

**M46 Strategic Phase Domain Action selection · **v4.1 §11.1 Counselor Stature+ only. Faction Hand Panel with card arts, illuminated manuscript aesthetic + faction-specific typography per Appendix C. Domain Action flow: target → confirm with Domain Echo projection → Uphold/Appease prompt (if Mandate ≥ 4 on target) → dice roll → degree → Domain Echo animation if Sufficient Scope fires.

**Finding F-28 [P1] — Uphold/Appease trigger condition in v4.1 §11.1 is imprecise.** board_game_v30 §PART ONE states: "**Trigger:** Domain Action directly challenges a faction's core institutional authority AND targeted faction Mandate ≥ 4." v4.1 §11.1 says "challenging Mandate ≥ 4 faction" — elides the "directly challenges core institutional authority" half, making it sound like any DA targeting a Mandate ≥ 4 faction triggers the choice. This would be a game-breaking misread — Uphold/Appease is specifically the institutional-challenge mechanic, not a general targeting check. **Robust:** n/a (the mechanic is right in the source). **Elegant:** ✗ (UI would over-fire). **Smooth:** ✗.
**Repair:** §11.1 Domain Action flow should be: target selection → *Sufficient Scope projection* (scale_transitions §7 — whether this action will produce Domain Echo) → *Institutional challenge check* (does this DA challenge target's core authority AND target Mandate ≥ 4?) → if yes, Uphold/Appease modal for target faction's NPC (AI decides per board_game §NPC rule) → dice roll → Domain Echo animation. The NPC-side Appease decision ("Mandate ≥ 4 AND Stability ≤ 3" per board_game §NPC rule) should be transparently shown in the modal so the player understands why Appease fired.

**M47 Hand panel view · **v4.1 §11.1 iconic card art, illuminated manuscript aesthetic, faction-specific typography, card readiness + cooldowns + Casus Belli indicators. 

**Finding F-29 [P2] — Card cooldown timing is vague; Casus Belli indicator content is not specified.** board_game §Casus Belli, §Treaty Betrayal, and various patches specify cooldown rules. The Hand Panel should show per-card: cooldown seasons remaining, trigger conditions for ready (some cards require faction stat thresholds), Casus Belli targets if any. Currently v4.1 is illustrative not specific.
**Repair:** Hand Panel card face format: card name (faction-typographed), pool attribute icon + current-stat value (auto-updates on stat change), Ob hint if previewable from game state, cooldown/unlock condition in footer, Casus Belli target token (if the card would consume one). Hover reveals full mechanical text. The v4.1 §11.1 spec should enumerate the card fields rather than describe in prose.

**M48 Framework Drift pulse · **v4.1 §2.1 Agent+ Stature only. §2.3 shows the strip with four factions pulsing. Matches npc_behavior §7.1 Drift mechanics.

**Finding F-30 [P3] — Framework Drift pulse shows directional arrows (↑·↓) per faction in §2.3 example but does not distinguish *why* each faction is drifting.** npc_behavior §7.1 has 9 framework-drift triggers, each with specific per-season cumulation rules. A Counselor character seeing "Crown ↑ / Church ↑ / Hafen · / Varfell ↓" has no idea whether Crown's up-arrow is from "Crown NPCs at Truth ≥ 3: +1 Truth per year of unchallenged governance" vs some other condition. Tooltip on hover should surface: "Crown: Unchallenged governance (2 seasons) → Truth +1 projected." Non-blocking; enrichment.

**M49 Cascade Phase 6-step accounting · **v4.1 §1.2 60–120s, per-step dismiss after first. §1.1 points to "Phase 3 Cascade (G) — animated 5-step accounting." board_game §Cascade Phase has specific depth cap = 3 per resolution window (so some effects queue to Accounting rather than resolving mid-phase). 

**Finding F-31 [P2] — Cascade Depth Cap (3 immediate effects per card play) is not in v4.1 Cascade spec.** board_game §PART TWO p.348 + p.390: "Within the Cascade Depth Cap of 3 immediate effects" — this is why massive card plays like Church Seizure at CI 80 have some effects queue to next Accounting rather than resolving all at once. Player needs visibility on which effects queued vs resolved.
**Repair:** §1.2 Phase 3 Cascade spec should add: per-step dismissal shows "Resolved immediately" vs "Queued to next Accounting" state. The Cap of 3 acts as a natural pacing mechanism — the animated accounting shows 3 effects landing with weight, with the rest appearing in the next-season Briefing.

**M50 Domain Echo firing · **v4.1 §11.1 mentions "Domain Echo projection" and "Domain Echo animation if Sufficient Scope fires." integration_proposal Part 8 proposes the **Domain Echo Reference Table** as a formal canonical specification — this is integration_proposal's B-1 blocker.

**Finding F-32 [P1] — Domain Echo Reference Table from integration_proposal Part 8 is not a UI-readable artifact in v4.1.** The table specifies, per action type (Investigation Complex / Structural; Contest Grand; Thread Mending / Dissolution; Combat named-NPC; Belief Fulfillment NPC / systemic; Duty Investigate / Governance; Governance sustained; NPE Coalition), the OW/Success/Partial/Failure consequences plus Stature Modifier (Standing 3 lets Partial produce stat changes; Standing 4 amplifies Success to ±2; Standing 5 OW to ±3) and Seasonal Cap (±2 per faction stat per season). Without UI surfaces of this table, the player cannot plan around Echo.
**Repair:** Pre-commit Domain Action (§11.1) and pre-commit Thread operation (§9.4) should display the Domain Echo Reference Table row for the action being committed, with the player's current Stature amplifier shown: "Investigation Complex on Church institutional matter: Success = +1 Faction Intelligence. At your Standing 3: Partial = +1 narrative → stat (amplified)." This is the single most important robustness-increasing addition available — it makes the bridge mechanism legible.

**M51 Parliament / Lobbying · **v4.1 §6.2 Parliament variant with chamber view + lobbying at 1 scene action per target. board_game and faction_layer §5 define Parliamentary Motions and Parliamentary Intent.

**Finding F-33 [P1] — Parliamentary Intent from integration_proposal Gap 3 (Standing 3+) is absent.** integration_proposal Gap 3 specifies: "Standing 3+ players can declare **Parliamentary Intent** as a scene action during the Personal Phase... evidence adds +1D to the Ratification roll (Corroboration in Parliament, mirroring the Contest Corroboration mechanic). Diplomacy scene with a neutral faction's representative produces a Positioning Roll bonus (+1D to the faction's Diplomacy pool in any Treaty initiated this season)." v4.1 §6.2 only describes Lobbying as "personal persuasion of individual faction representatives via brief private contests" — this is the NPC-targeted version. Parliamentary Intent is the Evidence-Track-targeted version and is more fundamental: it converts investigation into diplomatic capital.
**Repair:** §6.2 should add Parliamentary Intent as a declarable scene action for Standing 3+ characters: choosing this action consumes 1 scene action, binds one completed Finding to an upcoming Parliamentary vote, and causes that Finding's +1D bonus to appear on the faction's Senate action pool next season. Visible on the Hand Panel as a pre-bound corroborator chip on the next Senator card. Counselor affordance surfaces in Phase 1c.

**M52 Treaty / Grand Debate · **v4.1 §6.5 three phases per faction_layer §3.3: Positioning → Concession → Ratification. Grand Debate escalation to Parliament adjudicator.

**Finding F-34 [P2] — Treaty and Grand Debate do not render the binding Obligation output.** social_contest §6.1 specifies that Decisive wins in Formal and Grand Contests produce **Obligations** — binding clocks tracked by clock_registry per Obligation (source contest / parties / commitment / duration / violation trigger). v4.1 §2.1 lists "Obligations block" as visible only when character has at least one active Obligation; ok. But Treaty/Grand Debate's output → Obligation generation is not specifically surfaced at the moment of contest resolution. The player wins a Grand Debate and gets... what? The Obligation naming step is the dramatic payoff.
**Repair:** §6.5 Ratification Step 3 should add a post-win "Obligation naming" modal — the winner types or selects one specific commitment the losing side must honor (must be verifiable, not abstract, per social_contest §6.1). Settlement-targeted Obligations per peninsular_strain C-08 should appear as selectable targets. The bound Obligation appears as a pinned entry on both the winner's Obligations block and the losing faction's faction sheet (with duration clock).

**M53 Counselor negotiation win · **See F-1 — this is the other face of the Duty negotiation moment.

**M54 Faction leader succession / Leadership challenge · **v4.1 §11.1 Victory progress panel (V key). Says "Faction-aligned see universal condition + faction-specific path + co-victory pairings + shared-loss risk." player_agency §5.2 gives succession & leadership-challenge mechanics.

**Finding F-35 [P2] — Leadership challenge action has no surfaced trigger.** player_agency §5.2: "A Standing 4+ character can call a leadership challenge at any time via social contest against the current leader, with the faction council as expert adjudicator." Also succession offer when leader is eliminated and player is Standing 5. Neither has a visible call-to-action. **Repair:** §11.1 or a new §11.1b "Leadership" subsection specifies: at Standing 4+, a "Challenge Leadership" action button appears in the Hand Panel's footer (not a card — a faction action); at Standing 5 at the moment a leader is removed, a Priority 0 Slate entry fires offering leadership.

**M55 Faction emergence Stage 1–5 · **v4.1 §11.3 §5.3 says "Independent path ... No faction stat pool until Renown 7+. At Renown 9+, may call Grand Contest any time." settlement_layer §6.2 gives the full 5-stage faction emergence pathway with explicit thresholds: Stage 2→3 (2+ settlements, Renown 5+, 2 NPC officers at +3), Stage 3→4 (4+ settlements across 2+ provinces, Renown 7+, Influence-pool formal declaration Ob 3, 1 province Seat), Stage 4→5 (2+ province Seats, Renown 9+, full faction sheet).

**Finding F-36 [P1] — Faction emergence pathway is not surfaced as a tracked progression.** An independent player working toward founding a faction has no visibility into "you are at Stage 2, need X to reach Stage 3." This is the design's most rewarding long-form arc (Mount & Blade / Manor Lords analog, explicitly cited in player_agency §1.4). **Robust:** ✗ (invisible progression). **Elegant:** n/a. **Smooth:** ✗.
**Repair:** New §11.1c "Independent Actor progression" panel visible only to Independent characters: shows current Stage (1 / 2 / 3 / 4 / 5) with checkbox list of requirements for next Stage. At each Stage-up, cutscene per §13 (atmospheric mini-cutscene tier at Stage 2→3 and 3→4; arc-critical tier at Stage 4→5 "Faction Declared"). This maps to player_agency §5.4 Renown thresholds and settlement_layer §6 simultaneously — the two systems point at the same progression; v4.1 must render it as one.

**M56 Faction collapse to city-state · **settlement_layer §6.3: collapse sequence produces city-state with partial stat sheet. v4.1 does not address collapse UI.

**Finding F-37 [P3] — Faction collapse animation / city-state transition UI is absent.** When a controlled faction loses its last province but leader remains, the Hand Panel transforms (loses Mandate / Military cards, retains Influence / Wealth / Stability cards); Parliament access may persist depending on political context. Non-blocking; UI-level polish; note for future version.

### 2.J — Mass scale (moments 57–61)

**M57 Mass battle 7-phase · **v4.1 Part 8 says "7 phases per mass_battle §A.7. Each phase has its own UI affordances: Strategy grid, Volley animation, Manoeuvre drag-drop, Offensive Thread panels (only if practitioner commanders), Engagement splits, Cascade simultaneous damage, Reform." Generally correct direction.

**Finding F-38 [P1 — TWO ERRORS IN ONE PARAGRAPH] — v4.1 §8.2 line 717 contains two canon mis-reads.**

**Error (a) — Phase 4 silent-skip:** v4.1 says "For non-practitioner commanders, Phase 4 is skipped silently (auto-advanced to Phase 5)." mass_battle §A.7 Phase 4 + threadwork §2.3 Thread Operation Visibility require the phase to *run and be observable* at degraded perception: commanders with TS 0–9 see "nothing perceived," 10–29 see vague unease, 30–49 see direction, 50+ see full operation. Skipping Phase 4 silently hides *enemy* practitioner operations from a non-practitioner commander, which breaks the observable-enemy principle.

**Error (b) — General Duel wrongly restricted:** v4.1 continues "A practitioner General-Duel option appears in Phase 5 only when both combatants have the capability to engage." scale_transitions §3.7 defines General Duel as a **generic Personal Action at Phase 5 Priority 8** — any general may enter personal combat against an opposing general. This is not a practitioner-only option. v4.1 conflates the canonical General Duel (two generals, personal combat) with a hypothetical Thread-vs-Thread duel (both practitioners). Only the first is canonical.

**Robust:** ✗ (tactical depth removed for non-practitioner players). **Elegant:** ✗ (two mis-reads in one paragraph). **Smooth:** ✗ (player with TS 0 general cannot duel opposing TS 0 general in v4.1's reading).
**Repair:** §8.2 Phase 4 specification should run the phase always; render observer's-perception view per threadwork §2.3 Observation table. §8.2 General Duel line should be rewritten: "General Duel action available at Phase 5 Priority 8 (per scale_transitions §3.7). Any general with Personal Actions available may enter personal combat against an opposing general. Thread-vs-Thread practitioner duels are a separate case handled by Thread operations in Phase 4."

**M58 Phase mechanics (Volley / Manoeuvre / Engagement / Cascade / Reform) · **See F-38. mass_battle Phases 2, 3, 5, 6, 7 each have specific rules (sight-line for Artillery, deterministic Discipline check at Phase 6 Step 2, Morale triggers, etc.). v4.1 §8.2 is too terse — it names "their own UI affordances" without specifying them.

**Finding F-39 [P2] — Mass battle per-phase UI not specified.** The sim-depth of mass_battle is high; v4.1 Part 8 is under-specified relative to Part 7 (personal combat). Repair: Each phase gets a sub-section (8.2.1 through 8.2.7) specifying: what's visible on-screen, what's declarable by player, what's hidden (secret declarations), what animates on resolution. The Reform phase (§8.2.7) in particular — Discipline restoration with Command ≥ Discipline+1 AND Command ≥ 2 gate, formation changes, Reserve commitment for next turn — is a compressed strategic moment that warrants a UI specification. **Non-blocker for v4.1 *if* the game is not ready to ship Mass battle to Godot; blocker if it is.** Flag to Jordan: does the Godot milestone include Mass battle in the near term?

**M59 General Duel Zoom In · **v4.1 §8.3. Personal combat embedded, 1 exchange = 1 mass combat turn, mass battle freezes behind. Correct per mass_battle §A.5 / PP-232 / PP-111.

**Finding F-40 [P2] — General Duel exit conditions not specified.** mass_battle §A.5 cites "Maximum 5 exchanges before forced disengage or incapacitation." v4.1 §8.3 just says "mass battle freezes behind" without saying when/how the duel ends. Should specify: the exchange counter is visible (1/5, 2/5, ...), on 5 exchanges without resolution both parties forced disengage, either party's incapacitation ends the duel. Mass battle resumes at the next turn's Phase 1 (not the current turn's next phase). **Minor.**

**M60 Multi-engagement · **combat §8 Multi-Engagement covers personal; mass_battle handles unit-level. v4.1 §8.1 mentions 16×10 hex, unit tokens. Multi-engagement (3v2, 4v3) flanking rules not surfaced specifically.

**Finding F-41 [P3] — Flanking visualization not specified.** Flanking is a major tactical lever (Morale −1 per flanked-and-lost-exchange). v4.1 §8.1 doesn't describe how flanking is shown on the 16×10 hex grid. Non-critical; standard wargame convention (hex-side arrows) will suffice; but flag for v4.2 spec.

**M61 Settlement Defense pre-battle contribution · **settlement_layer §5.2 "effective Defense = settlement Defense + garrison Discipline." v4.1 §8.4 mentions the three-option resolution. Not clear how the combined value renders on the battle setup screen.

**Finding F-42 [P2] — Effective Defense formula not exposed in pre-battle UI.** Before committing to Assault, the attacker should see the effective Defense value (base Defense + garrison Discipline) so they can assess their Military advantage. Similarly, Bypass eligibility (Military > Defense + 2 per F-26 correction) should pre-commit-check against effective Defense. **Repair:** §8.4 adds a pre-battle setup screen for invasions showing: settlement name, base Defense, garrison presence (unit info), effective Defense, attacker's Military vs thresholds for Assault roll / Siege qualification / Bypass.

### 2.K — Cross-scale transitions (moments 62–69)

**M62 Mandatory Zoom In (Priority 0) · **v4.1 §1.4 cutscene queue rules correctly prioritize Priority 0 events. scale_transitions §4.3.2 table matches v4.1's coverage: Settlement Revolt, Heresy target, Faction Leader Removal.

**Finding F-43 [P2] — scale_transitions §4.3.2 also includes arc-specific triggers (§4.3.1: Haelgrund Defection, Consecration Crisis, per-arc triggers) that v4.1 §1.4 does not enumerate.** These are arc-register-driven (arcs/registers/arc_register.md) — the 120+ arc vectors from emergent_arcs. v4.1 cannot enumerate all, but should specify the mechanism: any arc vector whose trigger condition is met during a season generates a Priority 0 entry at the arc's designated location. Non-blocking; spec-completeness.

**M63 Retrospective Zoom In (player not present) · **scale_transitions §4.3 Retrospective table: companion delivers / Knot resonance / messenger / ambient rumor. v4.1 does not address this.

**Finding F-44 [P2] — Retrospective Zoom In has no v4.1 UI surface.** This is the mechanism for events that happened while the player was elsewhere (Löwenritter Coup, Graduated Seizure, battle the player missed). The scene is not about the event — it's about the player's relationship to it. scale_transitions §4.3 Retrospective gives a beautiful framing: "The player hears about it from ambient sources — tavern conversation, broadsheet, market rumor. The information is Unverified (reliability tag per fieldwork §4.3)." **Robust:** ✗ without this, offscreen events become stat changes rather than felt events. **Repair:** §13 atmospheric mini-cutscene list should add "Retrospective event mini-cutscene" triggered by: player arrives in or communicates with a territory where a major event occurred while they were elsewhere. The mini-cutscene routes through the player's closest connection per scale_transitions §4.3 table: companion → Knot → messenger/letter → ambient rumor. Each has a different reliability tag applied to the resulting Journal entry.

**M65 Transition inventory · **v4.1 §12.1 gives Fieldwork↔Investigation, Investigation→Contest (see F-9 ESCALATE button issue), Contest→Combat, Combat→Fieldwork, Fieldwork→Combat (Exposure ambush), Fieldwork→Thread, Contest→Fieldwork, Any→Cutscene. Missing transitions from scale_transitions §3.9:

**Finding F-45 [P2] — Transition inventory incomplete.** Missing: Fieldwork → Contest Findings-as-preparation (F-TRANS-11: Findings cited in Contest opening grant +1D per Finding, max +2D); Fieldwork → Mass Battle suspension (F-TRANS-06); BG Survey → TTRPG Discovery Fieldwork Offset (Survey degree produces Ob modifier on next Fieldwork scene per fieldwork_hybrid §9.1); Combat → Fieldwork Exposure codification (+1 quiet / +2 conspicuous / +3 public per F-TRANS-09); Contest → Fieldwork Appraise → Evidence Track +1 Testimonial (F-TRANS-10). These are all canonical cross-system bridges; they should appear in §12.1 table with their triggers, UI handoffs, animations. **Repair:** Add these 5 rows to §12.1.

**M66 BG Survey degree → TTRPG Fieldwork Offset · **fieldwork_hybrid §9.1 specifies Failure = −1 Ob / Partial = +0 / Success = +1 Ob reduction / Overwhelming = +2 Ob reduction on the next Fieldwork scene. Non-trivial cross-phase bridge. v4.1 does not render.

**Finding F-46 [P3] — Survey Offset pill on next-scene scene card absent.** Minor UI refinement: if the player's faction used BG Survey targeting a territory this season, the next fieldwork scene in that territory shows an "Survey Offset: −1 Ob" pill in the scene-opening HUD, visible to the player. Non-blocker; enrichment.

**M67 Sufficient Scope threshold crossing with companion modifier · **scale_transitions §7 lists 7 Sufficient Scope conditions. Companion present: +1 net successes. v4.1 §11.1 says "Domain Action flow ... confirmation with Domain Echo projection" — OK direction, but Sufficient Scope conditions are not enumerated in the UI projection.

**Finding F-47 [P1] — Sufficient Scope check must be pre-commit-visible.** This is the threshold that separates a Personal-only action from one that will generate Domain Echo. A player considering whether to push a negotiation to Contest should know: "Target NPC is a faction officer — Sufficient Scope criterion 5 met." Companion-present modifier adds explicitly visible "+1 net" pip. **Repair:** Any pre-commit UI (Thread panel §9.4, Domain Action panel §11.1, Contest setup §6, Combat Sufficient Scope banner §7.7) should render the Sufficient Scope check: which of the 7 conditions apply, whether the action will trigger Domain Echo, and what the companion modifier contributes. v4.1 §7.7 names "Sufficient Scope indicator" for personal combat only; needs to extend to all four gateways.

**M68 Hybrid Coherence binary declaration · **scale_transitions §6.4–§6.5 PP-198: the PC who declares leadership at Phase 1 of the Cascade Phase pays Coherence cost. No co-declaration — one PC bears the Thread bridge cost.

**Finding F-48 [P2] — Hybrid declaration UI for multi-player scenarios is not v4.1-specified.** v4.1 is Godot-facing, which is a single-player context — multi-player declaration may not apply. However, Hybrid mode mixing human-leader and NPC-led factions may still have this declaration for the human player when their faction's Thread operations apply at the strategic layer. **Repair:** Flag for Jordan: is Godot single-character-single-faction, or does Hybrid mode apply? If yes, §1.5 or Phase 2 Strategic needs a Coherence cost declaration dialog. If no, scoped out.

**M69 Contested Figure wound → BG tactic Ob penalty · **scale_transitions §11 ED-167: CF wound during personal combat → +1 Ob to commander's BG tactic rolls for remainder of current battle. v4.1 §8.3 doesn't surface this.

**Finding F-49 [P3] — Contested Figure wound penalty carry-over is invisible.** Mass battle resume after General Duel should show the commander's current Ob penalty from wounds taken in the Duel. Minor but material — if the Duel wounds the general, the commander's next mass-battle tactic roll is harder.

### 2.L — World-state (moments 70–79)

**M70 RS shader · **v4.1 §9.6 five-band shader table. ✓ canonical per threadwork §5.3. **Pass.**

**M71 CI appearance / threshold crossings · **v4.1 §2.1 "CI visible once character has interacted with Church content." OK. clock_registry CI ranges 0–75 (freeze at 75 per board_game P-23). Thresholds at 40 (Altonian Preparation trigger per victory §AEA), 55 (Church Policy escalation), 65 (Seizure eligible), 80+ (seizure triggers per next Accounting).

**Finding F-50 [P2] — CI threshold markers not shown in v4.1 §2.1 clock display.** Showing CI as a value ("Strained" band) without the upcoming-threshold context fails Oath II (transparency is not over-explanation). A player with CI 58 should see "CI 58/75 · Seizure eligible at 65." **Repair:** The three-clock summary panel (§2.1) expanded view shows per-clock: current value, next threshold name, seasons-to-threshold if trajectory is predictable (e.g., CI +1/season passive, so seasons-to-65 = 7). CI specific: freeze at 75, then seizure firing at 80 per board_game P-23.

**M72 IP appearance / thresholds · **v4.1 §2.1 "Visible once IP has reached ≥ 20, OR character is in a border territory, OR Altonian-related investigation is active." IP range 0–100 per clock_registry. settlement_layer §7.1 recalibrated IP to +1 per 2 seasons (halved) for extended-timeline games. Altonian Preparation fires at IP 60, Diplomatic Pressure at IP 40, Invasion Vanguard at IP 75.

**Finding F-51 [P2] — IP threshold markers not shown.** Same as F-50 but for IP. Add threshold markers for 40 / 60 / 75 / 100. IP is especially important for Crown/Hafenmark defensive planning.

**M73 PI (Parliament Integrity) · **clock_registry lists PI 0–20, auto-resolves at PI ≥ 20. v4.1 does not surface PI at all.

**Finding F-52 [P1] — PI (Parliament Integrity) is completely absent from v4.1 chrome.** This is a canonical shared clock (clock_registry §Shared Clocks), starts at 7, accumulates as pressure, fires at 20. Hafenmark-specific but affects any Hafenmark-aligned or Parliament-participating character. At Counselor+ stature in a Parliament-participating faction, PI should be visible. **Repair:** §2.1 visibility rule: PI visible at Counselor+ Stature in Crown, Hafenmark, Church, Guilds, Löwenritter, or Restoration (any Parliament-participating faction). Adds to the three-clock summary if relevant. Tooltip: "Parliament Integrity — 7/20. Pressure auto-resolves at 20."

**M74 Calamity radiation proximity 0–5 · **calamity_radiation_v30 defines proximity bands from T15 Askeheim. v4.1 §3.2 "Calamity gradient: Static radial darkening from T15 Askeheim, per calamity_radiation_v30." Shader present. Fieldwork Ob modifier +1 per RS band below 60 at current Proximity per fieldwork §1 is not surfaced in Fieldwork action panel.

**Finding F-53 [P2] — Calamity proximity Ob modifier invisible in fieldwork panel.** fieldwork §1 specifies "Calamity radiation: +1 Ob per RS band below 60 at current Proximity Rating." A fieldwork action in T13 Oastad at RS 50 faces +1 Ob from Calamity-RS-cumulation. v4.1 §4.3 should surface this in the Ob preview. **Repair:** Per-action Ob breakdown on hover: base Ob + Depth + territorial modifiers + Calamity modifier. Already a natural extension of F-4's per-action panel.

**M75 GEN (year counter) · **v4.1 §2.1 always visible. ✓ clock_registry confirms.

**M76 CD · **see F-15. **Remove.**

**M77 Generational Shift clock · **settlement_layer §7.2 defines Generational Shift 0–10 at +1 per 5 years. Threshold 2 (Year 10) = first-gen leaders −1 to highest attribute; 4 = −2; 6 = −3. TS ≥ 50 exempts. Exception: PCs also affected per ED-SETT-07 (P2, pending Jordan confirmation but proposed = yes).

**Finding F-54 [P2] — Generational Shift clock absent from v4.1.** For 10–30 year campaigns this is a meaningful clock. Affects player character at Threshold 2. **Repair:** Add to §2.1 visibility table: GEN-Shift visible from Year 8 onwards (2 years before first threshold). Character sheet (§11.3) shows age penalty if applicable. NPC sheets show succession-candidate arrow at Threshold 4+.

**M78 CI bar · **v4.1 §2.1 covered. ✓

**M79 Convergence Marker firing · **v4.1 §13.3 confirms 4 cutscenes (Church Double Fracture, Practitioner King, Tutoring + Southernmost, Niflhel Weaponises). Arc-critical tier. **Pass.**

### 2.M — Content integrity / canon-specific (moments 80–84)

**M80 P-03 Depth-access gating · **v4.1 §4.2 operationalizes; ED-544 resolution notes "depth gate + Thread sight + environmental shader" IS the P-03 implementation. ✓ Canonically correct.

**M81 P-08 Inert Knowledge for non-sensitives · **v4.1 §4.5 + §11.4 Codex. ✓

**M82 P-12 Knot contagion · **v4.1 §9.9 Knot graph + P-12 Patch O (+1 strain/season on Close Knots at Taint 4–6).

**Finding F-55 [P1 — KNOCK-ON FROM F-16] — "+1 strain/season on Close Knots at Taint 4–6" cites a non-existent Taint track.** npc_behavior §5.0b (AUD-NPC-02 fix, P-12 compliance) specifies the correct propagation: it's based on *TS state* (30–49 / 50–69 / 70+) AND on "in epistemic seduction," not on a Taint number. The Taint track was removed in threadwork §8.1. Correct propagation per npc_behavior §5.0b:
| NPC TS state | Close Knot strain | Distant Knot strain |
| TS 30–49 Active | +1/season | None |
| TS 50–69 Deep | +2/season | +1/season |
| TS 70+ or in epistemic seduction | +3/season | +2/season |
**Repair:** §9.9 P-12 Patch O should be rewritten per npc_behavior §5.0b table. The Knot graph visualization should color-code edges by TS state of the Knotted NPC (not by Taint). This resolves a canon-compliance breach.

**M83 P-13 Southernmost forgetting · **v4.1 §4.5.1 gives detailed 5-season decay. ✓ Strongest P-13 translation in the document. **Pass.**

**M84 P-15 Three-layer being-persistence · **v4.1 §9.7 Coherence 0 TS-branched outcomes: "TS 30–49 dissolution-of-self narrative resolution (character becomes NPC); TS 50–69 ontological freefall (−3 RS/session); TS 70+ forces layer-3 self-maintenance (−1 RS/session)." Cross-check threadwork PP-197: **"TS 70–89: −1 RS per session"** and **"TS 90+ Resonant: −1 RS per scene."** v4.1's "TS 70+ forces layer-3 self-maintenance (−1 RS/session)" is correct for TS 70–89 but does not distinguish TS 90+ Resonant.

**Finding F-56 [P2] — P-15 TS 90+ Resonant band not distinguished in Coherence 0 outcome.** threadwork §PP-197 specifies: TS 70–89 = −1 RS/session; TS 90+ Resonant = −1 RS/scene (much higher). v4.1 §9.7 TS 70+ row misses the 90+ distinction. **Repair:** Split the TS 70+ row into TS 70–89 and TS 90+ with the correct RS costs.

---

## PART 3 — INTEGRATED ASSESSMENT

### 3.A — Performance by axis (robust / elegant / smooth), individually then as set

**3.A.1 Robust:**
Individual moments: 60/79 score strong, 19/79 score weak-or-absent (F-1, F-5, F-6, F-7, F-8, F-12, F-13, F-17, F-19, F-20, F-21, F-23, F-24, F-25, F-28, F-32, F-33, F-36, F-47). Most robustness gaps are **in the Personal-scale bridge to Faction-scale** — the Duty negotiation / Parliamentary Intent / Counselor negotiation / Domain Echo Reference Table pathway that integration_proposal specifically calls out as integration_proposal's central B-1 through B-5 blockers. v4.1 has the *chrome surface* right (capability-gating, visibility rules) but not the *vertical mechanics* that turn player stature into faction-layer consequence. The player's accumulation of stature is mechanically absorbed but not expressed.

As a set: the robustness failure clusters around **Part 5 Dialogue Lattice** (F-7, F-8), **Part 9 Thread** (F-15, F-16, F-17, F-19), and **Part 11 Faction management** (F-28, F-32, F-33, F-36). These are the three systems where player agency most needs legibility, and they are where v4.1 is weakest.

**3.A.2 Elegant:**
Individual moments: strong in chrome design (§2.1 visibility rules, §2.5 Slate dock, §4.2 depth-axis, §9.1 progressive unlock). Weak when v4.1 defers to the v4 document without respecification (F-4 fieldwork panel, F-13 Death Cascade). Particularly inelegant: two false Thread tracks (F-15 CD, F-16 Taint) are *additions* of complexity on top of a canonically simpler system — this is the most inelegant kind of mistake because it imports burden that canon already removed.

As a set: the 14-part structure is cleaner than v4's 25-part structure — this is a real gain. The Appendices A–E split reference material from linear reading effectively. The single Scene Action Cost Table (§1.3) is a strong unification. But the document's elegance is undermined by three classes of problem: (a) deferral to v4 in critical sections (§4.3 fieldwork panel, §7.5 actions list detail, §11.2 governance panel), (b) introduction of invented mechanics (F-15, F-16), (c) flattening of per-variant asymmetries (F-10 generic contest).

**3.A.3 Smooth:**
Individual moments: strong cross-system chrome persistence (chrome survives all transitions except cutscenes — correct per Oath I), zoom transitions with audio cues (§3.6 ✓), atomic scene rule (no saves mid-resolution ✓), cutscene queue priority system (§1.4 ✓). Weak where the *mechanical integration* is specified in source docs but not surfaced in UI: the five missing transition-inventory rows (F-45), the Dissolution escalation button (F-9), the ambient-retrospective scenes absent (F-44).

As a set: **the Peninsula-level "always-on-world" presence** is the document's strongest integration achievement. Clocks pulse (§13.7.4), shaders modulate per RS (§9.6), factions pulse in their own rhythms, map-as-document rendering. This produces the "world breathes" feeling integration_proposal cites as the target experience. But the smoothness fails at *moment-of-transition* — where one system hands off to another, the player needs to feel continuity. The ESCALATE TO CONTEST button (F-9) is the clearest failure; scale_transitions' 5 missing fieldwork transitions (F-45) are the next; Rendering Crisis arc reduction to single cutscene (F-19) is the deepest.

### 3.B — "How do we play the game?" — the integrated loop

Measure the v4.1 document against the 7-scene walkthrough in §12.2. That walkthrough is v4.1's test-case for its own claim to support play. The walkthrough:
1. Enter Gransol Court (fieldwork Examine at Depth 1): 1 action, ✓
2. Continue fieldwork — Read + dialogue with Conviction option: 0 (chain), ✓
3. Reconstruct: 0, ✓
4. Domain Echo fires (on Structural Finding): requires F-32 Reference Table to be UI-legible for the player to understand what happened
5. Travel + dialogue → Contest escalation: 1, but per F-9 the escalation must be environmental, not button
6. Contest → Combat when Niflhel plant draws weapon: ✓
7. Post-combat fieldwork: 1
8. Phase 4 Aftermath companion scene + Conviction revision: ✓

The walkthrough is internally consistent *if* the findings above are repaired. Without F-9, the player feels the scene broken by a modal button; without F-32, the Domain Echo in step 4 is invisible. The integrated loop walks correctly on paper; the playable legibility of that walk depends on the repairs.

### 3.C — The three design oaths test

**Oath I (World always present):** ✓ passes fully. Chrome persistence, clock persistence, slate persistence across all four layers is the document's strongest commitment. No violation found.

**Oath II (Transparency is not over-explanation):** ✓ passes in principle but ✗ fails in several specific places:
- F-4 per-action Exposure projection absent → player acts blind
- F-23 governance action Ob projection absent → governor acts blind
- F-47 Sufficient Scope pre-commit absent → Domain Action player acts blind
- F-50/F-51 CI/IP threshold markers absent → clock-band display is incomplete bands
- F-32 Domain Echo Reference Table absent → personal-to-faction mapping is a black box

These are all Oath II violations in specific mechanical moments. The *principle* of Oath II is in the document; the *implementation* in these moments is missing.

**Oath III (Felt, not narrated):** ✗ fails in two specific places:
- F-9 ESCALATE TO CONTEST button — announces state change via text
- F-13 5-step Death Cascade not specified as animated-state-change → player may experience death as a notification

Oath III's violation test in §P0: "Does the UI announce a state change via text before the state change is shown visually or audibly?" — the ESCALATE button fails this explicitly.

### 3.D — Whole-document coherence

The v4.1 document is **65–70% of a publishable Godot-development-reference.** The 14-part structure works. The three Oaths produce a genuine design discipline. The capability-gating approach (C-3) is the correct solution to the "earn your HUD" philosophy. Setting-faithfulness (palette, typography, music) is achieved. The Scene Slate operationalizes player_agency. The depth axis operationalizes P-03. The progressive Thread unlock operationalizes C-2.

The document becomes incomplete precisely at the **bridge mechanisms between Personal and Faction scales** — the same gap that integration_proposal Part 2 identifies as the project's "central unresolved design problem." v4.1 has absorbed most of integration_proposal's findings but has not adopted: (a) Domain Echo Reference Table as a pre-commit UI artifact, (b) Parliamentary Intent as a Personal-scale action, (c) Counselor negotiation → Priority Stack Adjustment output, (d) Dialogue Lattice's 7 gate types with visible-locked hint text, (e) Style Decision UI for Contest. These five absences are integration_proposal's H-1 through H-6. Each is mapped to specific findings above.

The document also has two canon-compliance breaches (F-15 CD, F-16 Taint) that must be repaired regardless of playability. A Godot dev reference that cites non-existent tracks would generate canon-drift downstream.

---

## PART 4 — PRIORITIZED REPAIR LIST

### P1 (blocking for Godot development reference)
1. **F-1 Duty negotiation** — add §1.2 Phase 1a Counselor+ fork + social contest UI + Priority Stack Adjustment visualization
2. **F-5 Exposure per-territory** — surface multi-territory Exposure strip in §4.4 left panel
3. **F-7 Dialogue Lattice gate taxonomy** — replace §5.3 row types with investigation_proposal's 7-gate + visibility-rules system
4. **F-9 ESCALATE button** — make dialogue→Contest escalation environmental, not modal
5. **F-11 Style Decision UI** — add 4-button plain-language Contest style choice in §6.1 Step 2
6. **F-13 Death Cascade 5-step animation** — specify the 5-panel sequence in §7.6
7. **F-15 CD track** — delete §9.8; remove all CD references
8. **F-16 Taint track** — delete from §9.7 and §11.3; relocate effects to Coherence ≤ 3 / ≤ 2
9. **F-28 Uphold/Appease trigger precision** — rewrite §11.1 Domain Action flow with institutional-challenge gate
10. **F-32 Domain Echo Reference Table** — surface as pre-commit UI in §9.4 and §11.1
11. **F-33 Parliamentary Intent** — add scene action for Standing 3+ in §6.2
12. **F-36 Faction emergence progression** — add §11.1c Independent-Actor progression panel
13. **F-38 Mass battle Phase 4 visibility** — correct §8.2 to render opposing-side Phase 4 per observer TS
14. **F-47 Sufficient Scope pre-commit** — extend §7.7 Sufficient Scope indicator to all four gateways
15. **F-52 PI clock** — add to §2.1 visibility rules at Counselor+ in Parliament factions
16. **F-55 Taint → TS-state Knot propagation correction** — rewrite §9.9 P-12 Patch O per npc_behavior §5.0b

### P2 (needed before next version)
17. **F-2 Companion Slate commentary** — add one-line opinion to §2.5 Slate entries
18. **F-3 NPC time-of-day cue** — add time-of-day strip to location cards in §3.4
19. **F-4 Fieldwork action cost matrix** — fully restate §4.3 panel
20. **F-6 Case Board** — specify persistent Case Board in §4.6 per investigation_proposal
21. **F-8 Sincerity Gate UI** — add [SINCERE]/[INSTRUMENTAL] tagging + firing animation in §5.3
22. **F-10 Contest variant spec** — enumerate per-variant UI differences in §6.3
23. **F-12 Contested-pool manoeuvres** — specify Feint/Rescue/Disarm/Tie Up sub-panels in §7.5
24. **F-17 Dissonant Coherence band UI** — specify §13.7.3 Coherence 7–5 ambient layer
25. **F-18 Dissolution residue inventory** — add residue row to §9.4 Thread panel
26. **F-19 Rendering Crisis arc** — specify full arc UI in §9.7 Coherence 0 row
27. **F-20 Knot vs Companion separation** — clarify §11.5 Knot formation vs Disp +5 relational depth
28. **F-22 Rupture cutscene specification** — add RS Critical band crisis banner + Rupture cutscene spec in §13
29. **F-23 Governance action preview** — add pre-commit Ob/pool preview in §11.2
30. **F-24 Subnational management flow** — add Grant/Revoke affordance in province panel
31. **F-25 Settlement-anchored Slate entries** — add settlement prefix + event icon in §2.5
32. **F-26 Bypass threshold per-type split** — distinguish non-Fortress (+2) from Fortress (+3) in §8.4
33. **F-27 Companion-governor assignment radio** — add Social/Governance selector in companion strip
34. **F-29 Hand panel card field spec** — enumerate card face fields in §11.1
35. **F-31 Cascade Depth Cap** — specify immediate-vs-queued state in §1.2 Phase 3
36. **F-34 Obligation naming modal** — add post-win Obligation flow in §6.5
37. **F-35 Leadership Challenge action** — add Standing 4+ call-to-action affordance
38. **F-39 Mass battle per-phase UI** — sub-sections for each of the 7 phases in Part 8
39. **F-40 General Duel exit conditions** — specify in §8.3
40. **F-42 Effective Defense pre-battle** — add pre-battle setup screen in §8.4
41. **F-43/F-44 Retrospective Zoom In + arc-specific triggers** — add to §13 + §1.4
42. **F-45 Missing transition-inventory rows** — add 5 rows to §12.1
43. **F-48 Hybrid Coherence declaration** — scope question for Jordan
44. **F-50/F-51 CI/IP threshold markers** — add next-threshold displays in §2.1
45. **F-53 Calamity Ob modifier in fieldwork** — surface in §4.3 per-action preview
46. **F-54 Generational Shift clock** — add to §2.1 visibility + §11.3 character sheet
47. **F-56 P-15 TS 90+ Resonant split** — correct §9.7 TS 70+ row

### P3 (enrichment; future version)
48. **F-14 Pre-Leap Diagnosis** — add Diagnosis preview in §9.3
49. **F-21 Threadcut Rendering Strain naming** — specify in §10.2
50. **F-30 Framework Drift tooltips** — add hover detail in §2.1 Framework Drift strip
51. **F-37 Faction collapse to city-state** — add Hand Panel transformation animation
52. **F-41 Flanking visualization** — add hex-side arrows in §8.1
53. **F-46 BG Survey Offset pill** — add on next-scene HUD
54. **F-49 CF wound penalty carry-over** — show on mass-battle resume

---

## PART 4b — SECOND-ORDER FINDINGS (re-test sweep of Parts 0, 13, 14 + Appendices A, E)

The first-pass audit spent less attention on Part 0 (oaths), Part 13 (feel layers), Part 14 (resolved items index), and Appendices A / E. A targeted sweep of these produced 13 additional findings, numbered F-57 through F-69.

### 4b.A — Part 14 Resolved Items Index

**Finding F-58 [P1 — KNOCK-ON FROM F-15, F-16] — Part 14 rows for P-10 and P-11 are falsely resolved.** Row 1204: "P-10 | Taint distinguished from Coherence (§9.7)" cites the invented Taint track per F-16. Row 1205: "P-11 | CD accumulation track in Thread HUD (§9.8)" cites the invented CD track per F-15. These must be revised when F-15 and F-16 repair. Canonically: P-10 is about Coherence vs persona-integrity (addressable via §9.7 Coherence band effects + threadwork §3.3 Fragmented/Fractured Fallout). P-11 is about temporal co-movement costs fire visibly — *actually* resolved by §9.5 co-movement panel (temporal axis shown), not §9.8 CD.
**Repair:** Delete row 1204. Rewrite row 1205 to cite §9.5 co-movement panel. Add P-10 resolution row citing §9.7 Coherence band effects and threadwork §3.3 Fallout tables.

**Finding F-59 [P2 — KNOCK-ON FROM F-17] — UI-03 "Involuntary Thread perception via Coherence ≤5" threshold conflicts with canonical Dissonant band 7–5.** threadwork §3.3 Dissonant narrative flickers begin at Coherence 7, not 5. Either UI-03's framing needs correction or §13.7.3's Layer 3 trigger stays at ≤5 — but both cannot be canonical against threadwork §3.3.
**Repair:** Reconcile UI-03 description with F-17 repair. If §13.7.3 threshold changes to ≤7, UI-03 description updates correspondingly.

**Finding F-60 [P3] — UI-09 compound row.** "UI-09 | Settlement capture side-panel, General Duel full Zoom In" bundles two unrelated resolutions (settlement capture mid-battle + General Duel Zoom In). Related to F-38's second error. Split into two rows for index searchability.

### 4b.B — Oath violation tests

**Finding F-57 [P3] — Oath II Violation Test 3 is canonically correct but narrow.** "e.g., Liminal-depth content to a non-sensitive character" covers Depth 4 (TS 30+). Depth 3 (Buried) is accessible via alternative gates per fieldwork §5.4 (Disposition +3 for social; TS 10+ for investigation). A more precise test: "Does the UI reveal content at a Depth the character's perception cannot reach via *any* of the gates specified in fieldwork §1?" Not blocking; precision refinement.

### 4b.C — Appendices A and E

**Finding F-61 [P2] — Appendix E Core resources list is incomplete.** Listed 10 resource types; missing at minimum: Belief, Knot, Obligation, Duty, Disposition, Evidence (distinct from Investigation), Clock. For a Godot resource-tree engineer, this is insufficient.
**Repair:** Expand to: Attribute, Character, Belief, Conviction, StanceTriangle, Knot, Obligation, Duty, Disposition, Faction, Territory, Settlement, Investigation, Evidence, SlateEntry, Clock, CutsceneRef.

**Finding F-62 [P2] — Appendix E Signal bus enumeration is sparse.** 3 signals listed, 50+ claimed. §2.1 Implementation Note names 4 (Stature / TS / faction alignment / Obligation count). For implementation, at minimum 30 enumerated signals needed.
**Repair:** Expand signal list. Candidates include: `obligation_added/removed`, `knot_formed/strained/ruptured`, `coherence_band_crossed`, `rs_band_crossed`, `tc/ip/pi_threshold_crossed`, `belief_scar_added`, `conviction_strain_added/revised`, `disposition_changed`, `exposure_threshold_crossed`, `season_boundary`, `phase_transition`, `scene_action_spent`, `sufficient_scope_triggered`, `domain_echo_fired`, `cutscene_queued`.

**Finding F-63 [P3] — Appendix E asset manifest "72+ card arts" potentially under-counts.** 8 factions × ~8 card types ≈ 64 baseline + subnational/special cards. Flag for verification against the authoritative card registry in the game repo (which v4.1 line 1400 correctly defers to).

**Finding F-64 [P2] — Appendix E save system spec is thin.** "Phase-boundary only; version-headered binary; backward-migratable" is asserted but no migration strategy, no file structure, no specification of resource-ref vs deep-copy serialization. For 30-year campaigns (~500+ save points), engineers need more.
**Repair:** Specify save-file structure (resource refs with IDs vs embedded copies, version header format, migration fallback, size expectations).

**Finding F-65 [P1] — Appendix A does not address capability-gated shortcut remapping.** Line 1247 lists `T (Thread sight — if TS 1+)` as a conditional shortcut. Line 1245 asserts "full remapping." Interaction between capability-gating and remapping is unspecified: does a remapped-before-TS-acquisition binding persist? Does the key go live on capability acquisition?
**Repair:** Appendix A should specify: capability-gated shortcuts remain mapped even when the element is unmounted (keystroke is no-op until capability acquired); remapping is persistent per character; on capability acquisition, the mapped key becomes live without re-mapping prompt.

**Finding F-66 [P3] — Appendix A shortcut list is sparse.** 9 keys listed for a game with 4 layers × ~10 panels. Non-blocker; Godot engineers will iterate input maps regardless.

### 4b.D — Part 13 cutscene inventory

**Finding F-68 [P1 — SPEC-AUTONOMY] — §13.2 says "From v4 Part 19 — 22 mandatory triggers. Unchanged." and does not enumerate them in v4.1.** The 22 mandatory cutscene triggers are the single most important content-production input for cutscene authors. Deferring them to v4 while claiming "CANONICAL — approved for Godot development reference" is a structural inconsistency.
**Repair:** §13.2 must enumerate the 22 triggers. If v4's list is correct, copy it. If it needs updates (e.g., incorporation of Generational Shift per F-54, Rupture per F-22, Rendering Crisis arc opening per F-19), revise while enumerating.

### 4b.E — Spec autonomy pattern (systemic)

**Finding F-69 [P1 — SYSTEMIC] — v4.1 contains multiple "See v4 §X for details — unchanged" deferrals that undermine the document's "CANONICAL — approved for development reference" status line.** Collected instances:
- §4.3 — Action panel (F-4 already flagged)
- §5.2 — Dialogue layout "See v4 §5.2"
- §6.2 — Parliament "See v4 §15 for details — unchanged structurally in v4.1"
- §7.5 — combat action list
- §7.6 — "See v4 §7.6–7.9. Unchanged"
- §7.7 — Sufficient Scope indicator "Unchanged from v4"
- §8.1 — Battle map "See v4 Part 8 for detail"
- §13.2 — 22 mandatory triggers (F-68)

Each instance points an engineer to a 168K-char superseded document. **The document self-identifies as canonical development reference but behaves as a structural supplement to v4.** This is misleading to downstream engineers.
**Repair option A (long-term):** Restate all deferred sections inline. Increases v4.1 length substantially.
**Repair option B (short-term):** Change status line from "CANONICAL — approved for development reference" to "CANONICAL — structural supplement to v4; v4 remains authoritative for content-level UI specification until incremental restatement completes." Makes dependency explicit without forcing immediate rewrite. Allows v4.2 / v4.3 to restate priority sections.

### 4b.F — Thread axis terminology

**Finding F-67 [P2 — STALE TERMINOLOGY] — v4.1 §9.4 Three-axis Ob builder labels the first axis "Scale" but canonical (post-PP-622) is "Breadth."** Verified via threadwork §2.4 Mending design note line 375: "Mending Ob = Depth Ob − 1 + age modifier + **Breadth + Distance**." integration_proposal line 362: "The Three-Axis Thread Ob (**Depth + Breadth + Distance**)." v4.1's 5 values (Object/Personal/Relational/Territorial/Structural) are correct; only the axis label is stale. "Scale" is ambiguous across the design (also means game-mode abstraction per three-mode framing); Breadth is the post-PP-622 canonical term.
**Repair:** Rename §9.4 first axis from "Scale" to "Breadth." Values unchanged.

### 4b.G — Second-order additions to repair list

Add to **P1 blockers:**
- F-58 (P-10 / P-11 index rows falsely resolved) — delete row 1204, rewrite row 1205
- F-65 (capability-gated shortcut remapping spec)
- F-68 (§13.2 22 trigger enumeration)
- F-69 (spec-autonomy pattern — at minimum adopt Repair Option B status-line change)

Add to **P2:**
- F-59 (UI-03 threshold reconcile with F-17)
- F-61 (Appendix E resources expansion)
- F-62 (Appendix E signal enumeration)
- F-64 (save system spec depth)
- F-67 (Scale → Breadth rename)

Add to **P3:**
- F-57 (Oath II Violation Test 3 precision)
- F-60 (UI-09 row split)
- F-63 (card count verification)
- F-66 (shortcut list expansion)

**Updated totals: 69 findings (20 P1, 37 P2, 12 P3).**

---



The **v4.1 document achieves its core design claim** — that the interface should match the character's capability — through capability-gated chrome, progressive Thread unlock, depth-axis as perception UI, period-faithful aesthetics, and persistent world presence. These are genuine design achievements and should be preserved.

The document **fails at the bridge between Personal and Faction scales** — the same gap integration_proposal identifies as the project's central unresolved design problem. The five H-class recommendations in integration_proposal Part 12 (Named NPC as Ecology Anchor, Counselor Negotiation Output, Occupation → Resistance Scene, Progressive Revelation, Parliament + Personal Layer, Style Decision UI) are almost entirely absent from v4.1. Repairing them via findings F-1, F-7, F-11, F-32, F-33, F-36 would close that gap.

The document has **two canon-compliance breaches** (F-15 CD track; F-16 Taint track) that reintroduce dead mechanics. These must be deleted regardless of gameplay implications.

**As a Godot-development-reference**, v4.1 is approximately 65–70% complete. With the 16 P1 repairs, it reaches ~90%. With P1+P2, it reaches ~95% and becomes a usable engineering spec. P3 items are refinement, not structure.

**As a design coherence statement**, v4.1 is ~75% coherent. The three Oaths are correct. The 14-part structure is clean. The chrome philosophy is right. But Parts 5, 9, and 11 — Dialogue, Thread, and Faction Management — contain the highest density of findings. These three Parts warrant focused revision in v4.2.

**Total findings:** 69 (20 P1, 37 P2, 12 P3). **Canon-compliance breaches:** 3 (F-15, F-16, F-55). **Absent integration_proposal high-value items:** 5 (F-7, F-11, F-32, F-33, F-36). **Absent player_agency / companion_specification / settlement_layer flows:** 11 (F-1, F-2, F-20, F-23, F-24, F-25, F-27, F-36, F-44, F-52, F-54). **Structural spec-autonomy breaches:** 1 systemic (F-69, affecting ~8 deferred sections).

**The document is not wrong in direction. It is incomplete in specific mechanical surfaces where the interface must carry mechanical weight, and it is structurally dependent on v4 in a way that its status line does not acknowledge.** The repairs above are additive; none require restructuring the 14-part architecture. F-69 Option B (status-line change) is the lowest-cost highest-value immediate action — it aligns the document's self-description with its actual dependency state and unblocks incremental restatement in future versions.

— End of audit.

