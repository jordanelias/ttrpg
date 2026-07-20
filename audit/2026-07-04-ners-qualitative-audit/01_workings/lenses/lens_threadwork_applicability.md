# Lens — Threadwork Applicability (P-14 juncture map)

## Status: working notes, 2026-07-04, NERS qualitative audit, lane threadwork_applicability

## The bar (canon 02_canon_constraints.md §P-14)
Verbatim: "Board/VG modes must express inseparability: co-movement cannot be omitted in any play
mode… All modes produce three-dimensional co-movement per Thread operation." FAIL condition: "Does
any play mode allow thread operations without three-dimensional co-movement?"

Nuance that structures every verdict below: P-14 has TWO failure shapes.
- **(a) Co-movement omission** — a mode hosts a thread op but drops co-movement. (None found; where
  thread ops exist, co-movement fires — social §9.4, mass §A.10, settlement §4.4 all wire it.)
- **(b) Mode cannot host a thread op at all** — a whole play mode is thread-impossible, so P-14's
  "expressed in every play mode" is vacuously unmet. **This is the live corpus failure**, and
  personal combat is its sharpest instance.
Narrative sinks (articulation) are a THIRD, weaker concern: not a co-movement violation but a
render-path / collision-feed gap. I keep these tiers distinct rather than calling every silence a
P-14 breach.

## Verified this pass (working tree, not dossier-trusted)
- `articulation_layer_v30.md`: grep Thread|Coherence|Calamity|Gap|Rendering → **0 hits**. Confirmed.
- `combat_engine_v1/` (core.py, systems.py, wrapper.py, weapon_physics.py): 20 "thread" hits are ALL
  the verb "threads" (data threading through functions — `w['gap']` etc.), **zero** threadwork/Leap/
  Coherence. ED-911 confirmed by direct read.
- `faction_behavior_v30.md`: **1** incidental Thread mention, none in the α/β/γ/λ engine math.
- `settlement_layer_v30.md §4.9`: Thread Exploitation Sites present (Niflhel Dissolution origin).

## Juncture union (grounding 03 + all 12 dossiers) — verdict each

### PRESENT (thread touches; co-movement fires) — no P-14 concern
- Social contest §9.3/§9.4/§9.4b (Weaving, temporal-axis, adjudicator response) — mature.
- Mass battle §A.7/§A.10 (scale-tiered Ob/Coherence table) — the corpus's richest thread wiring.
- Faction Domain Echo + Priority-5 Thread slot; conviction_track PT drift (§1.3b, ED-676).
- Settlement §4.4 thread ops→stat deltas.
- NPC conviction Thread×Scar matrix (§3.4→conviction_track §3); NPC practitioner Coherence
  thresholds (§4.3, ED-665); Knot strain propagation (§5.0b).
- Investigation Case Board Thread Layer / Thread-Read; Chargen; Knots↔Coherence.
- Architecture scene.thread_operation Key (present but **[STUB] payload** — thin, not absent) +
  Thread Domain Echo §5.6.
- Victory Battle→MS cost; Community Weaving as thread op.
- NOTE degenerate-present: Settlement §4.9 Exploitation Sites are wired but an uncapped/uncontested
  faucet — present-but-degenerate, a collision-feed miss, not a P-14 gap (settlement dossier owns).

### WIRE IT (absent-plausible) — ranked by North-Star value
1. **combat_engine_v1 — no thread op possible in the personal-combat play mode.** ED-911 (open,P1),
   KNOWN-TRACKED. Natural interaction: a practitioner mid-fight Leaps to suspend rendering for one
   op, or spends Coherence as a commit-depth/legibility resource; combat_v30 §10 (superseded) HAD
   Leap-in-combat and it never migrated. Buys: closes the single (b)-shape P-14 hole; personal combat
   is a whole play mode currently thread-impossible. Cascades to #2/#7.
2. **articulation_layer_v30 — narrative sink renders zero thread.** KNOWN-UNTRACKED (grounding 03 §3;
   no dedicated ED — searched, only ED-911 is combat-resolver). Natural: a Rendering-Crisis / Gap /
   Dissolution-witnessing Key fires a Tier-2 cut scene. Buys: the corpus's densest collision feed
   (thread→faction/settlement/NPC per ED-673/675/676) currently computes but never surfaces; ED-681
   authored 4 thread narrative beats explicitly for the videogame with NO rendering path. Highest
   emergence-surfacing cost after combat.
3. **General Duel (mass battle scale_transitions §3.7) — thread-blind.** KNOWN-TRACKED (ED-911 child).
   Natural: practitioner-general gets a Leap option in the duel exchange. Buys: mass battle's own §A.10
   thread layer is mature yet the personal-scale hook it hands to is thread-dead — a pure inheritance
   of #1. Resolves automatically once #1 lands.
4. **faction_behavior engine math (α/β/γ/λ, cosine cascade) takes no Coherence/Calamity input.**
   KNOWN-UNTRACKED. Natural: a Calamity/Gap term in the env.* shock vector, or Thread events shifting
   Legitimacy/PS. Buys: P-14 (b)-smell at the STRATEGIC layer's core mechanism — the disposition
   engine that gates every faction's signature action is thread-inert.
5. **NPC faction Priority Trees — 7 of 9 thread-blind.** NEW scope. Only Varfell (§8.5) & Wardens
   (§8.10) have Thread-conditioned rows; Church/Crown/Hafenmark/Guilds/Löwenritter/RM have none.
   Natural: a Thread-state row per tree (institutional posture shifts when Gaps open in-territory).
   Buys: P-01/P-14 inseparability at the autonomous-world layer; asymmetry is arbitrary, not scaled.
6. **Settlement governance §3.2 verb menu — no Thread-response verb.** KNOWN-TRACKED extension (03 §3).
   Thread hits the settlement automatically (§4.4/§4.9) but the governor never gets a CHOICE about it.
   Natural: a Regulate/Exploit/Seal-a-Thread-Site governance verb. Buys: converts passive thread
   state into a player decision — directly widens choice at the thinnest governance loop.
7. **Scene→Mass §3.8 — no Thread-scene win channel.** NEW. §3.8 covers Social/Investigation/Combat
   wins only, despite thread being the densest personal-scale action (§A.10). Natural: a Thread-scene
   win feeds an up-transition modifier. Buys: cross-scale continuity for the one action that has none.
8. **NPC memory of thread witnessing (P-09) — no mechanical surface.** KNOWN-TRACKED (doc:null
   npc_memory). Natural: a messy/costly/detectable memory trace of a witnessed Leap. Buys: P-09
   compliance; lower value (schema exists, just unhomed).
9. **Insurgency formation → Gap/Knot substrate event.** NEW, plausible. Natural: territorial neglect
   that spawns an insurgency also seeds a Gap/Knot. Buys: thematic cross-scale tie; lowest value.
10. **propagation_spec_v1 / holonic_container_doctrine — zero thread mention.** KNOWN-TRACKED (ED-911
    orbit). The flagship cross-scale-consequence spine never names Coherence. Natural: the aggregate-
    up/distribute-down transform routes thread state. Buys: architecture-level P-14; meta, but the
    spine everything else rides.

### DELIBERATELY ABSENT (cited intent)
- **Church faction AI thread exclusion.** thread_horizontal_integration_spec ED-679: "Church does not
  use Thread operations… Thread-resistant by design." Legitimate design intent — do NOT wire. (Caveat:
  ED-679 itself never propagated and its Niflhel target dissolved — the *intent* stands even though the
  *doctrine* is stranded.)

### DEFER
- **sim/personal/contest kernel thread hooks** — design doc §9.3/9.4 present; kernel absent because the
  rebuild is staged (Stages 0-3 done, Stage 4 next). Staged gap, not a design hole. Defer to Stage 4.
- **territory_temperaments thread-state coupling** — KNOWN-TRACKED (03 §3); Calamity-adjacency FLAVOR
  only (T6/T13/T15 seeded near outcomes-only), doc is province-grain PROVISIONAL. No intent citation
  for deliberateness, but no live coupling and the layer is mechanically inert corpus-wide (settlement
  dossier). Defer until temperament has any mechanical consumer at all.

## MS/RS split, ED-911/1010/1011 — KNOWN, assessed not rediscovered
- MS (threadwork_v30 §5) vs RS (params/threadwork.md) = same world track, live naming fork; ED-428/731/
  772 flip-flop, sweep never reached params/threadwork.md. This is a LEGIBILITY defect that raises the
  cost of every wire-it above: a Godot Resource field can't bind the track under two names. Not my
  finding to re-report as novel; I flag it as the precondition on junctures #4/#6/#10.
- ED-1010 (per-op Coherence cap homeless) and ED-1011 (Coherence-0→NPC split) similarly gate #1: you
  cannot wire Leap-in-combat cleanly while the per-op Coherence cost is contradicted between
  threadwork §3.7 and mass_battle §A.10. So #1 has a hidden dependency on 1010/1011 resolving first.

## Bottom line
The corpus's thread wiring is deep where it exists (social, mass battle, faction Domain Echo, NPC
conviction) but has a **coherent hole shaped like "personal-scale + narrative-surfacing + strategic-
math"**: combat cannot host a thread op (#1), articulation cannot render one (#2), and the faction
disposition engine cannot feel one (#4). Those three are the P-14-load-bearing wire-its; everything
below #4 is choice-widening or cross-scale polish. Only Church exclusion is genuinely deliberate.
