# Capstone-Verifier Working Notes — S5 Season Trace (ARC-S07)

## Status: VERIFICATION (emergent-narrative-engine effort · Lane IN · 2026-07-05)
Role: capstone verifier. Target: `01_workings/spec_sections/s5_season_trace.md`.
Type-check reference: `designs/architecture/scale_transitions_v30.md` §5/§12.
Verdict: **PASS-WITH-FIXES** (1 fix applied, 4 precision notes, no blockers).

---

## 1. All 12 capstones present AND substantively satisfied

| # | Requirement | Where | Verdict |
|---|---|---|---|
| 1 | Major arc seed→scene→convergence→resolution→chronicle, ≥3 rungs | Beats 1.1→2.1→3.2→4.2→4.3; **4 rungs** (indiv→family→faction→world, S5.2 close) | PASS |
| 2 | Casting why-you via tie-graph | Beat 1.2 `Bond(Halden,Torben)`∧`Duty(Halden,Crown)` matched, surfaced diegetically | PASS |
| 3 | Player-shaped branch changes next stage | Beat 2.1 + S5.3 divergence table (2 outcome classes → 2 distinct `lifecycle.state`s) | PASS |
| 4 | Followed-only arc (spectator, no played scene) | Beat 3.3 ARC-T02 (Almud), spectator channel only, no casting hook consumed | PASS |
| 5 | Leader beat (subordinate-originated) + member beat (duty-assigned) | Beat 1.1 (Almud, politics Key hunts leader as target) + Beat 1.2 (Halden duty) | PASS |
| 6 | gated / priced / foreclosed, each citing ledger cause | Beat 2.1 gated (diplomacy<4, ARC-T17) + priced (Standing) ; Beat 4.2 foreclosed (Loyalty≤2 ∧ Mandate−2) | PASS |
| 7 | Every beat's venue labeled | court/Bond-scene/case-board/cut-scene/extraction/chronicle | PASS (3.2/3.3 note below) |
| 8 | Meaningfulness pass one beat + fail one context event | PASS: 3.3 belief_revised{Almud}; FAIL: 1.1 tariff | PASS (correctly applied) |
| 9 | Total accounting: zero unaccounted Keys | S5.4 table | PASS (spine complete; see §3) |
| 10 | ARC-S07 compiled end-to-end (typed vector + slots + trace) | S5.1 arc_vector + template slot table + S5.2 | PASS |
| 11 | Two-seed chronicle comparison (actors/stakes/outcomes) | S5.6 seeds 42 vs 77; honestly scoped to data layer | PASS |
| 12 | Type-checks against scale_transitions §5/§12 | S5.2 close | PASS (see §2) |

All 12 present and substantive, not merely claimed.

---

## 2. Cross-scale hop type-check vs scale_transitions §5/§12

**Echo caps (§5.1 one Echo/faction/scene PP-329; §5.2 ±2/stat/Echo):**
- Crown_Mandate −2 (Beat 4.2) = exactly at ±2 cap → LEGAL. Register grounds it: `arc_register_factions.md:11` "Loyalty ≤ 2 → Crown Mandate −2 cumulative"; cumulative = per-application ≤2, each within cap.
- Löwenritter Autonomy +1 (Beat 3.1) < cap → LEGAL.
- No two Echoes stack on the same faction in one scene (Crown Echo at 4.2, Löwenritter at 3.1 — distinct factions). No PP-329 violation.

**Sufficient Scope (§7):** invoked at Beat 2.1 / §5.2-close ("Loyalty check meets Sufficient Scope"). Best-fit clause is §7.1 (Torben = heir / designated representative). Defensible; the trace does NOT name the specific sub-condition (Note N3).

**targets[] discipline (§12.3):** Beat 1.1 strategic Key names Torben/Almud/Laskaris in `targets[]` — correct application of §12.3 populate-sub-scale-targets. arc_vector `participating_actors` set is consistent.

**Direction coverage:** §5.2-close cites §5 (bottom-up), §12.3 (down-target), §12.4 (down-seam `scenario_authoring→settlement_layer`), §12.1 (all-directions), §12.2 (no private channel A6), §12.5 (NERS note). All cites resolve to real sections; §12.4 seam names settlement_layer while the trace targets personal actors — the general §12.1 top-down row covers personal observers, so the §12.4 cite is illustrative, not load-bearing. No new mechanism introduced (§12.5). **Type-check PASSES.**

**Loose use of "Domain Echo":** the trace repeatedly calls bottom-up clock/arc feeds "Domain Echo aggregate-up." Strictly, Domain Echo (§5.1) = personal scene meeting Sufficient Scope → faction stat. A clock crossing (IP-30) and an arc→arc pressure feed (Autonomy+1 → ARC-S20) are NOT §5 Domain Echoes. This is imprecision, not a structural error — the ±2 caps are respected and the directions are correct. Fixed the clearest instance (Beat 1.1); flagged the rest (Note N2).

---

## 3. Total accounting — zero unaccounted Keys (spine)

Walked every Key emitted in Beats 1.1–4.3 against the S5.4 table. Every spine Key is present with exactly one class:
- S1·1.1: clock.IP, env.crisis, state.tutoring_demand, meta.arc_state_changed, env.trade_tariff_fluctuation (DISCARDED) — all 5 tabled. ✓
- S1·1.2: mechanical.scene_entered, scene.dialogue, state.obligation_incurred — tabled. ✓
- S2·2.1: scene.investigation_resolved, da.covert_contact, Altonian_Intel+1 — tabled. ✓
- S3·3.1: meta.arc_state_changed, state.autonomy_increment, cut-scene — tabled. ✓
- S3·3.2: COLLISION-C (DISCARDED, `predicate_unresolvable(ARC-T04)`), meta.convergence_detected — tabled. ✓
- S3·3.3: state.belief_revised{Almud}, cut-scene — tabled. ✓
- S4·4.1: mechanical.scene_entered, scene.combat_strike/witness, obligation — tabled. ✓
- S4·4.2: state.altonian_oath_sworn (RENDERED+CONSUMED), Crown_Mandate−2, meta.arc_state_changed — tabled. ✓
- S4·4.3: meta.arc_state_changed(→resolved), chronicle paragraph — tabled. ✓

Two conditional Keys NOT in the table, both consistent (Note N4): Beat 2.1's `meta.arc_state_changed (if outcome flips a lifecycle edge)` does not fire on the spine (Loyalty still >3 at S2; flip is at Beat 3.1); Beat 4.2's Laskaris IP+3 is NPC-ARC-LAK's own trigger (reads Elske Loyalty≤2), not an ARC-S07 emission. Neither is an unaccounted spine Key. **Capstone #9 PASS.**

New Class B types (`meta.convergence_detected`, `meta.arc_state_changed`) are consumer-closed per S5.4 closing note (synthesis §8). Existing-type registration is asserted, not shown — acceptable for a spec draft.

---

## 4. Gated / priced / foreclosed — ledger causes

- GATED (2.1 opt 3, Formal Crown Treaty): "Altonian diplomacy < 4" — grounded `arc_register_factions.md:46` ARC-T17 (diplomacy 4+ threshold). ✓
- PRICED (2.1 opt 2, direct negotiation): Standing / foreign-operative exposure — grounded `tests/sim/sim_arc_01:60-62,82` (IP-B). ✓
- PRICED (4.1 opt 1, extraction): Obligation (Beat 1.2 accrual) + Standing — grounded `sim_arc_01:67`. ✓
- FORECLOSED (4.2): `payload.ledger_cause = Torben_Loyalty ≤ 2 AND Crown_Mandate −2 cumulative` — grounded `arc_register_factions.md:11`. ✓

All four cite ledger causes. C7 pricing-preference honored (arc carries `[pricing, foreclosure]`, no bare gating on its own transitions; the one gate is an external ARC-T17 option, S5.4 R10 note). **PASS.**

---

## 5. Venues labeled

1.1 Crown court T1 (settlement governance) · 1.2 private audience/Bond scene T1 · 2.1 fieldwork case-board T16 · 3.1 cut scene AT T16 + chronicle · 3.2 Tier-2 + chronicle · 3.3 cut scene + chronicle · 4.1 covert extraction (combat/infiltration) T16 · 4.2 Tier-3 chronicle + cut scene T16 · 4.3 year-end chronicle.
Charter rule = "AT a location, THROUGH a venue, or IN the chronicle." Beats 3.2/3.3 name surface (cut scene) + chronicle but no physical T-location; satisfied via the "IN the chronicle" clause (Note N5, weakest). **PASS.**

---

## 6. Meaningfulness test correctly applied

Test = durability × tie-proximity × identity-touch (charter :83-88; synthesis §3).
- FAIL (1.1 tariff): moves no slow variable, touches no `participating_actor` Belief/Conviction/Scar/Obligation, closes no possibility → all three factors ≈0 → texture. DISCARDED-with-reason, not silent. ✓
- PASS (3.3 belief_revised{Almud}): durability (Belief slow var) × tie-proximity (Almud one edge from PC's Bond, Torben's father) × identity-touch (Belief/Conviction). ✓

Clean pass/fail contrast, both accounted. **Capstone #8 PASS.**

---

## 7. Constraint compliance spot-checks

- **C1 (no runtime LLM):** realizer is template/slot, offline bake, deterministic splice. ✓
- **C2 (no narratological surfacing):** Beat 3.2 explicit — "convergence" label never surfaces, player sees "two crises that rhyme"; R4 C2 lint on all lifecycle/salience state. Register bands are internal bake keys. ✓
- **O-1 honesty:** the trace's `game_director` single-source default for `mechanical.scene_entered` genuinely CONTRADICTS `key_substrate_v30 §8.5 L510` ("scene_slate: scene activation emits mechanical.scene_entered"), verified. The trace flags this as an OPEN fork requiring an explicit §8.5 edit in the same PR — correct, not hidden. `module_contracts.yaml:392-395` (scene_timer consumes from game_director) confirmed. ✓

---

## 8. Source-citation audit (sampled, all confirmed on working tree)

- `arc_register_factions.md:10-11` ARC-S07 (IP30→Tutoring; Loyalty≤3→Coup Counter+1; Loyalty≤2→Mandate−2 cumulative; floor 6; Laskaris PROTECTIVE delay/flip). ✓
- `:19` ARC-S20 Ehrenwall's Count (the coup chain, convergence partner). ✓ `:31` ARC-S35. ✓ `:40-41` ARC-T02 (parallel Belief crisis). ✓ `:46` ARC-T17 (diplomacy 4+). ✓ `:312-313` NPC-ARC-LAK. ✓
- `arc_register_events.md:37-39` COLLISION-C (Tutoring+Southernmost; combined RS+8/IP+2/TC+2). ✓ ARC-T04 confirmed dangling ([UNNAMED — ED-416]; defined in no register). ✓
- Coup Counter STRUCK ED-781 confirmed `params/factions_personal.md:103` → replaced by 4-stage Löwenritter Autonomy (Loyal→Restless→Autonomous→Split). Fork-1 remap grounded. ✓
- `sim_arc_01:37` three endings (retrieved/Altonian/dead) ✓; `:64` Loyalty 8 ✓; `:66` minor Crown cost ✓; `:67` covert extraction Military/Intel ✓; `:68` ≤3→Elske viable heir ✓; `:78` 3–4 seasons ✓; `:60-62,82` IP-B ✓.
- `articulation_layer_v30`: cosine ±0.40 + corr +0.937 Crown/Hafenmark 30-season pair ✓; trigger-10 belief sig=7 ✓; §7 pacing D11 deferred "cut scenes fire whenever triggers match" ✓.

No fabricated citations found.

---

## 9. Fixes + notes

**FIX APPLIED (F1):** Beat 1.1 mislabeled the `clock.IP`→30 crossing as "an aggregate-up Domain Echo." A global-clock threshold crossing is not a §5.1 Domain Echo (which requires a personal scene meeting Sufficient Scope). Rewrote to: global clock (`§4.3.3`) aggregating bottom-up via the §12.1 bottom-up / §5 path, IP clock itself READ; the crossing fires the Tutoring Demand strategic Key. Preserves the §12.3 down-target claim intact.

**NEEDED, not applied (precision notes, non-blocking):**
- N2: Beat 3.1 + §5.2-close use "Domain Echo aggregate-up (§5.2/§5.3)" for an arc→arc feed (Autonomy+1 → ARC-S20) that is lateral/diagonal, not a §5 scene→faction Echo. §5.2 correctly bounds the ±2 cap, so no violation; recommend relabeling "bottom-up substrate delivery (§12.1)" and reserving "Domain Echo" for §5 scene→faction cases.
- N3: §5.2-close asserts the Loyalty check "meets Sufficient Scope" without citing the §7 sub-condition; name §7.1 (Torben as heir / designated representative) explicitly.
- N4: Beat 2.1's conditional `meta.arc_state_changed` and Beat 4.2's Laskaris IP+3 are absent from S5.4 — consistent (former doesn't fire on the spine; latter is NPC-ARC-LAK's own trigger). Optionally add a one-line "conditional, off-spine" footnote so a reader doesn't read them as dropped.
- N5: Beats 3.2/3.3 label surface + chronicle but no physical T-location; satisfied via "IN the chronicle" but the weakest venue labels — consider naming the ambient location (T1 court for Almud) for parity with other beats.
