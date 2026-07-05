# Verify — Contract Coherence across the five drafted spec sections

## Status: capstone-verify working notes, 2026-07-05 · Lane IN
Verifier role: contract coherence across `01_workings/spec_sections/{s1_q1_q2, s2_q3_arcs,
s3_q4_render, s4_substrate, s5_season_trace}.md`. Checked against working-tree canon:
`designs/architecture/key_type_registry_v30.md`, `references/module_contracts.yaml`,
`designs/architecture/key_substrate_v30.md`, `references/arcs/arc_register_events.md`,
`references/arcs/arc_register_territory.md`. C1/C2 treated absolute.

---

## 1. Every consumed/emitted Key in the binding sections is grounded — PASS

The authoritative module-contract binding is **s4 §S4.4** (module entries) + **§S4.5** (new
Key-type registry entries). Every Key named in a `consumes:`/`emits:` there is either registered
in `key_type_registry_v30` or is one of the two new Class B types declared in §S4.5 with a
consumer:

| Key | Status | Registry line |
|---|---|---|
| mechanical.scene_entered/exited/skipped | EXISTING (re-owned) | 365 / 393 / 418 |
| scene.combat_strike | EXISTING | 743 |
| scene.dialogue / .witness / .gift / .insult / .threat | EXISTING | 38 / 60 / 76 / 94 / 111 |
| scene.investigation_resolved | EXISTING, emitting_systems [scene_slate, faction_politics] | 705/720 |
| scene.combat_resolved | EXISTING, emitting_systems [personal_combat] | 724/738 |
| env.crisis / env.disaster | EXISTING | 608 / 625 |
| state.belief_revised | EXISTING | 879 |
| meta.convergence_detected | NEW Class B (§S4.5), consumers declared | — |
| meta.arc_state_changed | NEW Class B (§S4.5), consumers declared | — |

Consumer closure holds: `articulation` (universal `*` + explicit) and `game_director` (universal
`*`) both back the two new types; `scene_slate` also consumes both (§S4.4 lines 283-284) and edge
E8. The two new types correctly slot into the `system_meta` (§8) family; `state.belief_revised`
is precedent for a non-`meta.`-prefixed name in that family (registry L1019).

s5's worked-trace Keys are illustrative (see finding 5) and not part of the binding.

## 2. Module entries do not collide with module_contracts.yaml — PASS

The current file has doc:null `extracted` stubs the s4 candidates **replace**, not duplicate:
- `scene_slate` (mc:342) — currently emits `mechanical.scene_entered` (mc:349, "substrate §8.5
  verbatim — registry attributes … to game_director instead: cross-doc attribution conflict
  [OPEN — Jordan]"). s4 candidate removes that emit → resolves the flagged conflict.
- `game_director` (mc:368) — currently `scales:[scene]`, emits scene lifecycle. s4 candidate
  widens scales and adds the two meta types + arc-state store. Supersedes cleanly.
- `scene_timer` (mc:387) — s4 leaves UNCHANGED; already `consumes: mechanical.scene_entered
  from:[game_director]` (mc:392-395). Correct.
- `npc_behavior "arc state"` bucket (mc:150, `bucket: clock`, npc-scoped) — s4/s2 correctly treat
  it as the specialization the new `game_director` store READS, not owns.

No new module name collides; the four candidates flip `doc:null` for existing registry_systems.

## 3. scene_entered resolution is consistent everywhere — PASS

All five sections carry the SAME resolution and the SAME held-back caveat:
- **s1 §Q2.2**, **s2 §Q3.11 held-back**, **s3 Q4.11 + Deliverable 3**, **s4 §S4.8 + O-1**,
  **s5 O-1**: default = `game_director` single-sources `mechanical.scene_entered/exited/skipped`;
  `scene_slate` demoted to content-Key generator; **ratifiable only if the same PR edits
  `key_substrate_v30 §8.5 L510`**; flagged as a held-back hard call in the PR body per CLAUDE.md
  §2 ED-1094. No section relabels it "RESOLVED."
- Grounding all verified accurate: §8.5 L510 = "scene_slate: scene activation emits
  mechanical.scene_entered" (verbatim); mc:349 scene_slate emits it; mc:392-395 scene_timer
  consumes `from:[game_director]`; registry L383 `emitting_systems:[game_director]`. The registry
  already sides with game_director; §8.5 is the lone contradicting source, exactly as the sections
  state.

## 4. No section contradicts another on ownership / Key names / lifecycle — PASS (with fixes)

- **Lifecycle FSM states** identical in all sections: `seeded → active → escalating → converging
  → resolved | dormant | abandoned` (s2 §Q3.3 diagram + §Q3.8 enum; s4 registry desc; s5 §S5.1).
- **activity_mode** enum identical: `level_triggered, edge_triggered_once, edge_triggered_retryable,
  clock_escalation, convergence`.
- **Module ownership** identical: game_director owns arc-vector store (L1/L2/L3/L4); scenario_authoring
  L0 offline compile; scene_slate L4 candidate/manifest; articulation L5 render.
- **Fork DEFAULTS** agree across sections: Coup Counter 1:1 remap; ARC-T04 strike; temporal_window
  (4-season cosine + same-Accounting); add the two Class B types; Certainty in the frozen pool →
  low-thousands headline; GM-judgment ~15% declare non-firing; lifecycle.state → game_director store.
- **COLLISION-C / ARC-T04** claims verified against `arc_register_events.md:38-39` and
  `arc_register_territory.md:33`: ARC-T04 is genuinely dangling ([UNNAMED — ED-416], never defined);
  COLLISION-C combined deltas are "RS +8, IP +2, TC +2" (register-raw).

Fixed two mechanical inconsistencies inside s4 (see §Fixes). Remaining divergences are ID-numbering
and trace-hygiene, not contract breaks (see §Findings).

## 5. C1–C7 hold in the drafted text — PASS

- **C1** (no runtime LLM): realizer is offline `select→substitute→splice` over a frozen bake, zero
  inference (s3 Q4.6; s4 articulation `resolver: deterministic_accounting`). ✓
- **C2** (no narratological surfacing): C2 literal-string lint on ALL lifecycle/salience state +
  baked fragments (s2 CR-7, s3 Q4.6.7, s4 R4); the two meta labels are C2-internal, never in `text`.
  ✓
- **C3** (books venues, never resolves): `game_director resolver: manifest`; "participation-is-
  ordinary-resolution" rule; every played beat routes to a subsystem engine. ✓
- **C4** (closes ED-IN-0003 + ED-IN-0004): lifecycle.state generalization (s2 §Q3.3) + render-trigger
  completion E9–E11 (s4 §S4.6). ✓
- **C5** (holonic; no new currency): one owned store; "one ledger"/no new progression currency; the
  two new **Key types** are a flagged fork (total-accounting > type-count), not a new currency. ✓
- **C6** (thread beats render): s3 Deliverable 1 + s4 E11 add the four ED-681 Rendering-Crisis beats
  to the §3.1 trigger table. ✓
- **C7** (never railroads; pricing preferred; foreclosure via arc events): offer-not-outcome
  invariant, engagement-window-divergence, demotion-exemption, director-subtract-only,
  foreclosure-via-edge + mandatory-render, pricing-preferred audit — consistent across s1/s2/s3/s4/s5.
  ✓

---

## Fixes applied (mechanical, in-file)

1. **s4 §S4.5 heading** — the second new type was headed
   `### state.arc_state_changed  (registered as meta.arc_state_changed — …)`. Every other reference
   (game_director emit mc-candidate L235, s2, s3, s5, edge table E3/E4) uses `meta.arc_state_changed`;
   the `state.`-prefixed label was the sole outlier and contradicts its declared `system_meta` family.
   Normalized to `### meta.arc_state_changed  (add to §8 Family: system_meta)`.
2. **s4 §S4.5 consuming_systems** — both new-type entries listed
   `[game_director, articulation, chronicle]`, but `scene_slate`'s own candidate entry (§S4.4
   L283-284) and edge E8 declare it consuming both types. Registry consumer list omitted it →
   consumer-closure gap. Added `scene_slate`: now `[game_director, articulation, scene_slate,
   chronicle]` on both.

---

## Findings — flagged, NOT applied (larger than mechanical)

1. **Conformance-rule numbering collides across sections (active contradiction).** Five schemes for
   overlapping rules: s1 "rules 6–11", s2 "CR-1..CR-12", s3 named rules, s4 "R1–R10 (+ tools/ homes)",
   s5 "R1–R10 + R-ORD/R-FP/R-RND". The s4↔s5 maps **conflict**: s4 R5=scene_entered-single-emitter,
   R8=foreclosure-render, R9=convergence-provenance; s5 R5=convergence-provenance,
   R8=scene_entered-single-emitter, R9=foreclosure. Same rule *content*, contradictory IDs — violates
   the spec's own "each rule lives once in tools/". Recommend adopting **s4 R1–R10** (only scheme that
   names `tools/` homes) as canonical and having the other sections cite those IDs. Too broad/error-prone
   for a mechanical edit.
2. **Fork numbering diverges** (s2 fork 4 = lifecycle-ownership / fork 6 = bake; s4 fork 2 = lifecycle /
   fork 6 = bake; s5 O-1..O-8). Defaults all agree; only labels differ. Fold into the same harmonization
   pass as finding 1.
3. **`chronicle` listed as a consuming_system but is not a module.** Both new Key-type entries name
   `chronicle` as a consumer, but there is no `chronicle` module in `module_contracts.yaml` and no
   `chronicle` emitting/consuming system in the registry (chronicle is a Tier-3 *function of*
   articulation). Closure is still satisfied by `articulation`+`game_director`, so non-fatal, but
   `chronicle` should resolve to `articulation` (or get a real module entry) before R2/CR-12 runs.
4. **COLLISION-C clock-name convention diverges.** s2 §Q3.2 writes alias-resolved "MS +8, IP +2, CI +2";
   s3 Q4.6.7 and s5 write register-raw "RS +8, IP +2, TC +2". Both correct via the RS→MS / TC→CI aliases
   (clock_registry_v30, ED-731/782, which s2 cites). Reconcile to one convention (recommend
   alias-resolved with the raw form noted).
5. **s5 trace uses unregistered illustrative Key names, some over-claiming provenance.**
   `state.tutoring_demand`, `state.autonomy_increment`, `da.covert_contact`,
   `state.obligation_incurred/discharged`, `state.altonian_oath_sworn`, `env.trade_tariff_fluctuation`
   are not in the registry nor s4 new-entries, and are not tagged `[UNGROUNDED]`. Acceptable as trace
   illustration, but **`state.tutoring_demand` specifically claims to be "a new … entry the Stage-0 §3.1
   completion adds"** — yet s3 Deliverable 1 lists NO such Key (it adds scene.combat_resolved,
   scene.investigation_resolved, the 4 thread beats, and the 2 meta triggers). Either add it to the
   Stage-0 deliverable or relabel it trace-illustrative.

Minor: s4 §S4.8 cites `key_type_registry_v30.md:388` for `emitting_systems:[game_director]`; the actual
line is 383 (388 is a note). Substantive claim correct; citation line drift only.

---

## Verdict

**PASS-WITH-FIXES.** The module/Key/lifecycle contract binding is coherent: all binding-section Keys
are grounded, module candidates replace (not collide with) the existing stubs, the scene_entered fork
is handled identically and accurately in all five sections, and C1–C7 hold. Two internal s4
inconsistencies fixed in place. The residual items are ID-numbering harmonization (findings 1–2, the
one genuine cross-section contradiction, but cosmetic — content agrees), a consumer-name cleanup
(finding 3), a clock-alias convention pick (finding 4), and trace-Key hygiene (finding 5) — none break
the contract.
