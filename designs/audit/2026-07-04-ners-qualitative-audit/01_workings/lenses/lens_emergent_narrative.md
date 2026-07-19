# Lens: Emergent Narrative — full working notes

## Status: audit working notes (2026-07-04, IN lane, NERS qualitative audit)
Charter: `designs/audit/2026-07-04-ners-qualitative-audit/00_grounding/00_audit_charter.md`.
Working-tree only; every claim cites `file §section` I read myself.

---

## BRIEF 1 — Is the collision engine REAL? (3 canonical collision claims traced)

The corpus names its **emergent narrative engine** explicitly:
`references/throughlines_complete.md` §T-24 (L197-200): *"The game's biggest narrative
moments are not designed — they are structural. COLLISION C (Tutoring + Southernmost)
produces RS +8, IP +2, TC +2 in a single season — none of the component vectors predict
this combined effect... These convergences are the game's emergent narrative engine."*

The collisions themselves live in **one reference doc**:
`references/arcs/arc_register_events.md` §VI — Convergence Markers (L23-60), 8 defined
(A–G, J). Traced three:

- **COLLISION C — Tutoring + Southernmost** (L37-39): Trigger = Torben Loyalty ≤3 (ARC-S07)
  coincides with Southernmost Ritual **[UNNAMED — ED-416]** failure (ARC-T04). Combined =
  hand-written `RS +8, IP +2, TC +2` + cascade clauses.
- **COLLISION J — Church Siege of Southern Gates** (L58-60): Trigger = Church holds T9+T2 +
  TC ≥60 + RS ≤39. Combined = the winning-destabilises-substrate paradox, narrated in prose.
- **COLLISION B — Practitioner King** (L33-35): Trigger = Almud Discovery + Elske installed +
  Torben in Altonia. Combined = `TC +3 but RS improves`, "not predictable from any arc."

### The tell (header, L25)
Section VI's own header: *"Not named for dramatic effect — named because the combined
pressure is **not predictable from the constituent vectors** without the marker."*

That is the opposite of what T-24 claims. A marker exists **because** the engine cannot
derive the effect from the vectors — so a human authored both the trigger-coincidence rule
**and** the combined payload (`RS +8` etc.). The vectors (Torben Loyalty, RS/TC/IP thresholds,
Southernmost Ritual) ARE independently modelled, so the **WHEN** could emerge; but the
**WHAT** (the payload) is scripted, and — decisively — **nothing watches for the coincidence
or applies the payload.**

### No mechanical home (verified)
- `references/module_contracts.yaml`: grep `convergence|COLLISION` → only a name-collision
  note (L231) and a 2-cycle *numerical* convergence damper (L442). No convergence-marker module.
- `sim/` grep `convergence|COLLISION` → 7 files, all *mathematical/statistical* convergence
  (contest dictionaries, massbattle, treaty, units) — none is a collision-marker firer.
- No Key type: `key_type_registry_v30` has no convergence/collision Key (registry file is
  `references/key_type_registry_v30.md`-shaped; grep of the corpus finds no `scene.convergence`
  or marker Key).

**Verdict on collision engine:** Structurally it is **emergent-trigger, authored-payload,
with no runtime detector.** The independent vectors are real; the "engine" that composes them
into qualitatively-new pressure is a **hand-authored 8-item list in one reference doc**, and
`throughlines_complete.md` §T-24 **misrepresents** this as undesigned/structural. COLLISION C —
the charter's own worked example of emergence — is anchored on an **unnamed, unresolved ritual
(ED-416)**. This is the single sharpest gap in the North Star: the "collision engine that
produces emergent narrative" (charter) has no engine.

---

## BRIEF 2 — Does ANY surface render emergence to the player? (articulation coverage)

Articulation is the **sole** narrative-surfacing layer (`02_interdependency_map.md` (a)11;
`articulation_layer_v30.md` §5 universal `*` subscriber, emits nothing back).

Coverage from the articulation dossier (verified against grounding 03):
- **Dense/sim-verified:** faction coup/succession/covert_betrayal/strain_shock/cascade_cluster/
  belief_revised (§3.1 10-trigger table; Stage-10 sim 6/6).
- **SILENT — the decisive gap:** zero Thread/Coherence/Calamity/Gap/Rendering-Crisis hooks
  (grounding 03 §3; articulation dossier). This means the **#1 clock throughline** —
  `throughlines_complete.md` §T-04 "RS Decay → Radiation Cascade" ("**The world is dying**",
  L41), the game's core survival contest — has **no rendering path.**
- **Blind to endgame:** victory-era transitions (Post-Calamity/Occupation/Anarchy) UNKEYED
  (ED-1006; articulation dossier).
- **Self-contradictory:** §6.4 claims `scene.battle_concluded` triggers Tier-2, but §3.1 table
  omits it (articulation dossier, NEW).
- **Starvation mechanism unwired:** §3.3 anti-starvation promise not backed by §5 pseudocode —
  non-trigger-matching Bonded NPCs never render (articulation dossier, NEW).

**Verdict:** A surface *does* render emergence — but only political/faction/succession
emergence. The autonomous driver the setting is built around (Calamity/Thread decay) and the
game's own endgame transitions are invisible to it. The renderer of emergence is blind to the
world's central story.

---

## BRIEF 3 — Autonomous-world thought experiment (0 input, 4 seasons)

What actually ticks, walked qualitatively:
- **Clocks advance (real):** `throughlines_complete.md` §T-04/T-05/T-06/T-07 — RS baseline
  decay −1/yr + Gap/Lock/battle costs; TC +1/season → Church expansion thresholds (40/60/75/100);
  IP accumulation → Altonian intervention; Turmoil → Accord erosion. These are structural, not
  player-gated.
- **Factions act (real but deterministic):** faction behavior engine computes disposition each
  season via named-coefficient formulas (`faction_behavior_v30.md` §3.2-§3.5, faction dossier);
  BG Priority Trees are fixed if-then ladders (`npc_behavior_v30.md` §8.1-§8.10, npc dossier).
- **Insurgency forms from neglect (real, autonomous):** `insurgency_pipeline_v30.md` L111 —
  2+ contiguous Uncontrolled territories, 2 seasons → GD-3 Insurgency, GD-2 mandatory response
  (L284). Genuine autonomous-world generator; can invade the neglecting parent (L150).
- **NPC arcs advance (real):** §T-23 state machines driven by Scar/Certainty/threshold.

**Holes in autonomy:**
1. **Literal no-GM violation:** `faction_layer_v30.md` L490 "**GM controls NPC faction votes**
   (Guilds, Niflhel...)" and L362 "Partial | ... (**GM adjudicates**)". In an explicitly no-GM
   engine (CLAUDE.md header). Over 4 seasons of Parliament, NPC-only-faction votes have no
   autonomous resolver.
2. **Autonomous → predictable → solvable:** all 9 priority trees deterministic (npc dossier);
   sim converges to a degenerate ~87%/0%/0% win-share (CLAUDE.md §7). "Autonomous" collapses
   toward a solved end-state — direct tension with the non-dominance clause.

**A player returning after 4 seasons:** finds a **materially changed world** — territories
flipped, RS dropped, maybe an insurgency, NPC arcs advanced — a real strength. But (a) the
change trends toward a predictable single-winner, and (b) the parts of the change with the
richest story (Thread/Calamity) won't be *told* (Brief 2). Changed world: yes. Legible
emergent stories: only the political ones.

---

## BRIEF 4 — Verdict on the four Omega clauses, corpus-wide

1. **Cross-scale consequence — PARTIAL.** Bottom-up Domain Echo is the best-specified channel
   in the spine (`scale_transitions_v30.md` §5-§7; architecture dossier). But consequence
   propagates **one hop up**; it does not **compound** — the collision engine that would
   compose multiple echoes into qualitatively-new pressure doesn't exist (Brief 1), and
   cross-tick convergence is explicitly unproven (`propagation_spec_v1.md` §4.3; architecture
   dossier P1). Top-down: 8 §12.4 down-seams emitter-unpopulated.
2. **Personal transformation — BEST-SERVED (positive).** Conviction Scars, arc state machines
   (§T-23), Rendering Crisis perma −1 TS, Belief-revision endgame (§T-22). Genuinely rich in
   the slow political/thread layer. BUT its highest-frequency vector — combat — has **zero**
   transformation hook (ED-911), and arc *destinations* are authored menus, not emergent
   trajectories (npc dossier). Rich where play is slow; absent where play is fast.
3. **Autonomous world — REAL but holed.** Clocks + priority trees + insurgency genuinely tick
   (Brief 3). Holed by the `faction_layer §490` GM-vote delegation and the degenerate solved
   win-share.
4. **Non-dominance — MULTIPLE LIVE VIOLATIONS under repair.** Spear/polearm 84-96% (calibration,
   R2/R3); Command-dominance axiom (`mass_battle_v30.md` §A.1); deterministic-therefore-solvable
   priority trees; single victory shape (GD-1 collapsed ~9 endings→1); pre-ED-1060 Obscuring
   dominance. Actively worked, not closed.

**Cross-clause synthesis:** The corpus is strongest exactly where play is slow (faction/thread
transformation) and weakest where the North Star's "emergent narrative engine" is supposed to
live (the collision layer has no engine; the render layer is blind to the central clock). The
autonomous world runs, but its stories mostly don't reach the player and mostly trend to a
solved end.

---

## Threadwork junctures (this lens)
- **Collision engine → Thread:** ABSENT-plausible. COLLISION C/J both hinge on RS/Calamity
  (Thread state) but no marker is Thread-keyed into any resolver (Brief 1). §T-04 is the Thread
  survival clock and has no render path (Brief 2).
- **Articulation → Thread:** ABSENT (grounding 03 §3; articulation dossier). The load-bearing one.
- **Insurgency → Thread:** ABSENT-plausible — `insurgency_pipeline_v30.md` formation cites only
  adjacency/Uncontrolled, no Gap/Knot/calamity_radiation despite the natural fit (victory dossier).
