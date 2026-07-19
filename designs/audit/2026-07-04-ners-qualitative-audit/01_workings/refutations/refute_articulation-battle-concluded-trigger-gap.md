# Refutation review — articulation-battle-concluded-trigger-gap

## Verdict: CONFIRMED (could not refute). Intent: NOT-INTENDED. Severity: P2. Novelty: NEW.

## Claim vs. text
1. **§3.1 omits scene.battle_concluded & scene.investigation_resolved** — TRUE. Triggers 1–10
   (articulation_layer_v30.md §3.1 L83-92) are: scar_acquired, coup_attempted, succession,
   mission_shift, covert_betrayal, knot_formed, knot_ruptured, peninsular_strain_shock,
   cascade_cluster_event, belief_revised. Neither battle_concluded nor investigation_resolved
   (nor combat_resolved) appears.
2. **Both are registry-declared articulation consumers** — TRUE. key_type_registry_v30.md §7:
   scene.battle_concluded `consuming_systems: [... articulation ...]` (L699);
   scene.investigation_resolved likewise (L721).
3. **§6.4 asserts battle_concluded "already triggers Tier 2"** — TRUE. L296 verbatim:
   "`scene.battle_concluded` (existing) already triggers Tier 2." No §3.1 trigger backs it →
   genuine internal contradiction (Q-smooth).

## Refutation attempts (all failed)
- *"Fires via significance/§3.2"* — REFUTED. §5 callback (L254-262): significance is computed
  **only after** `matches_trigger_ruleset(key)`; a non-matching Key merely
  `accumulate_unarticulated_weight`. No trigger match ⇒ no cut scene.
- *"§3.3 accumulated weight eventually fires it"* — REFUTED. Accumulated weight is a significance
  BOOST applied when some other trigger fires; it is not itself a trigger.
- *"§6 'by default' is the mechanism"* — REFUTED by the doc's own precedent. belief_revised had the
  identical §6.3 "emits Tier 2 by default" language; Stage 10 §4.1 (quoted at §3.1 L114-123) found
  "a belief-revision Key on its own — without a co-firing trigger — has sig=7 (mid-tier) but does
  **not** produce a cut scene," which is why trigger #10 was **added to §3.1**. This proves §6
  defaults are NOT self-executing and that §3.1 is meant to be the exhaustive ruleset. The exact
  same unbacked assertion survives for battle_concluded / combat_resolved.

## Intent evidence (grep canon/editorial_ledger.jsonl, decision queue, handoffs)
- **ED-935/936/937 (2026-06-14)** concern registration/naming/consumer-wiring of the F2/F3 types,
  NOT the §3.1 trigger. **ED-936** *authored* the §6.4 line ("scene.combat_resolved → articulation
  Tier-2 default — articulation_layer §6.4") under **delegated authority, ASSUMPTION-flagged,
  Jordan-vetoable**; §6.4 carries an explicit `[ASSUMPTION …Jordan-vetoable]` comment (L298).
  So §6.4 is a delegated assertion that contradicts §3.1 — not a safeguarded deliberate omission.
- No decision-queue item (2026-07-01 overview) or HANDOFF lane tracks the trigger gap.
- The file's own carry-forward P2 (header L1) is about belief_revised — **closed** by trigger #10.
  The battle/investigation trigger gap is untracked ⇒ **NEW**, not KNOWN.

## Not a duplicate
Corroborated only inside THIS audit session (dossier_articulation.md L23-26; lens_emergent §L73;
lens_cohesion §L50-51) — the audit's own emerging consensus, not a pre-existing tracking artifact.
No `duplicate_of`.

## Severity vs North Star
Articulation is the renderer of emergence into player-experienced story. A decisive mass battle /
trial verdict is a flagship emergent beat; absent a Tier-2 trigger it gets no in-the-moment cut
scene (only the annual Tier-3 chronicle, §4.4). Direct dramatic-legibility / cohesion hit. Tier-3
still captures it annually ⇒ degradation not total loss ⇒ **P2** (not escalating to P1).
Direction **lateral** (sibling §3.1 ↔ §6.4 within one subsystem) is apt. Minor scope note: the
same gap also covers scene.combat_resolved, which §6.4 likewise claims by default.
