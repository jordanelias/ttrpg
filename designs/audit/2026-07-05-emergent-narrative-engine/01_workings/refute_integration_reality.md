# Refutation lane — INTEGRATION REALITY

## Status: PROPOSED (adversarial-skeptic lane, 2026-07-05)
Adversary brief: try to BREAK the synthesized Arc-Vector Engine on integration reality —
consumed-Key existence, module-boundary collisions with `module_contracts.yaml`, the
`scene_entered` conflict resolution's consistency with BOTH citing docs, Gate-0/ED-1051 staging
reality (`strategic_judgments` J-2), phantom dependencies. Working tree only.

---

## What SURVIVED my attack (the synthesis got these right)

- **`scene.combat_resolved` / `scene.investigation_resolved` EXIST.** Registry
  `key_type_registry_v30.md` L724 (`scene.combat_resolved`, added by ED-935) and L705
  (`scene.investigation_resolved`). The synthesis's claim these are "EXISTING Keys given render
  triggers, not new types" is CORRECT — not phantom.
- **The two new `meta.*` types are genuinely new and correctly declared.**
  `meta.convergence_detected` / `meta.arc_state_changed` are NOT in the registry (only
  `meta.knot_formed/ruptured/thread_woven/miraculous_event/legacy_event` exist, L800-901). The
  synthesis flags them as NEW Class B with consumers — honest, consumer-closed. Fork 4 is real.
- **Every `module_contracts.yaml` line citation checks out.** game_director L368 ✓, scene_slate
  L342 ✓, scenario_authoring L744 ✓, articulation_layer `consumes:*` L762+ ✓, npc_behavior
  arc-state bucket L150 ✓, scene_timer consuming `scene_entered` `from:[game_director]` L392 ✓.
  No fabricated line refs.
- **`scene_timer` alignment is real.** `scene_timer` already consumes
  `mechanical.scene_entered/exited/skipped` `from:[game_director]` (module_contracts L392-395),
  so single-sourcing to game_director is consistent with the registry side of the conflict.
- **articulation `consumes:*` trivially closes the two new meta keys** (wildcard, L768) — no
  consumer-closure break there.
- **ORD-4 hazard is real and correctly located.** `propagation_spec_v1` O.7/ORD-4 (L116-118):
  `scene_slate.py._queue` is module-global; relocate to World. Synthesis's mandatory-fix framing
  is grounded.

---

## Where it BREAKS (findings)

### F1 [MAJOR] — `scene_entered` resolution contradicts `key_substrate_v30 §8.5`; NOT consistent with both citing docs
The synthesis §5 declares the ownership conflict **"RESOLVED — this lane's job, not a fork"** and
single-sources `mechanical.scene_entered` to `game_director`, citing ONLY the `scene_timer`
consumer alignment. But the conflict has TWO citing docs:
- `key_type_registry_v30` (registry-derived) → attributes emission to **game_director**.
- `key_substrate_v30 §8.5` L510 verbatim: *"scene_slate: scene activation emits
  `mechanical.scene_entered`; events within emit `scene.*` Keys."* → attributes emission to
  **scene_slate**. This is the EXACT source `scene_slate`'s registry emit cites
  ("substrate §8.5 verbatim", module_contracts L349).
Resolving to game_director **directly contradicts a CANONICAL architecture doc** (`key_substrate`
is `## CANONICAL`), and the synthesis lists NO edit to §8.5 anywhere in its deliverable set. So
the "resolution" leaves a live canon contradiction: the substrate doc still says scene_slate
emits it. My lane's exact test — "consistent with both citing docs" — FAILS.
**REQUIRED FIX:** add an explicit edit to `key_substrate_v30 §8.5` L510 to the scene_entered
resolution deliverable (re-attribute emission to game_director, or split: scene_slate builds the
manifest / game_director emits the lifecycle Key). Ship it in the same PR (CLAUDE.md §2 ED-1094:
merge ratifies; a canon-contradicting resolution cannot be left implicit). Until §8.5 is edited,
this is a fork, not a resolution.

### F2 [MAJOR] — Stages 2–3 phantom-depend on `engine_clock`/ED-1051 (Gate-0); contradicts J-2's "existing home" claim
Synthesis §7 asserts "each stage independently mergeable and rides an existing home." But:
- **Stage 2 (store+tick)** "steps lifecycle FSMs on Key stream **+ clocks each season**" and
  reads clocks.
- **Stage 3 (detect)** edge-triggers the 8 COLLISION conjunctions **"at the ACCOUNTING_BOUNDARY"**.
Both ride the temporal spine. `strategic_judgments` **J-2** (L22-30) is explicit: `engine_clock`
— the temporal spine — is **doc:null pending ED-1051**, and it is the FROZEN critical path
("stop deepening combat until Gate-0 (Key v2 migration, three-doc reconciliation, engine_clock
authoring) is executed"). The Accounting-boundary machinery Stage 3 edge-triggers on is part of
that un-authored spine. So Stages 2-3 do NOT "ride an existing home" — they ride
`engine_clock`/Gate-0 infrastructure that ED-1051 has not delivered. The synthesis surfaces the
ORD-3/ORD-4 determinism precondition (§9) but is SILENT on the engine_clock/ED-1051/Gate-0
precondition for its own clock-stepping and Accounting-boundary detector — a phantom dependency
on the single most load-bearing doc:null module in the corpus.
**REQUIRED FIX:** in §7, gate Stage 2 (clock-stepping) and Stage 3 (Accounting-boundary
detection) behind Gate-0 / ED-1051 (`engine_clock` authoring) as an explicit precondition, and
note that `propagation_spec_v1` (ED-1093) is engine_clock's candidate home per J-2. Stage 0
(render) and Stage 1 (offline compile) genuinely have no clock dependency and can precede it — so
the ships-first ordering survives, but the dependency must be stated, not elided.

### F3 [MINOR] — Stage-0 lists `scene.combat_resolved` as an "add," but it ALREADY renders; and mislocates §6.4 as "§3.1"
Synthesis §6 item 1: "articulation §3.1 trigger-table completion (the literal F-4 / ED-IN-0004
root at `articulation_layer_v30 L294-298`) ... add `scene.combat_resolved` + ...". Two errors:
- L294-298 is **§6.4**, not §3.1. §3.1 (L77) is the 10-trigger ruleset; §6.4 (L294) is the
  per-key note. The citation conflates them.
- `scene.combat_resolved` is **ALREADY** given a Tier-2 render trigger in §6.4 ("emits Tier 2 cut
  scene by default", ED-935/936). Per grounding 03(b) and J-3, the F-4 root is that this §6.4
  trigger is an unverified **[ASSUMPTION]** (ED-936 delegated authority) — the fix is to RATIFY
  it, not re-add it. The genuinely-missing triggers are `scene.investigation_resolved` and the
  four ED-681 thread beats (J-3: "add articulation triggers for battle_concluded/
  investigation_resolved" — combat_resolved NOT listed, because it's already there).
**REQUIRED FIX:** reword Stage 0: (a) correct the citation to §6.4; (b) reframe combat_resolved as
"ratify the §6.4 [ASSUMPTION] trigger (ED-936)", not "add"; (c) keep investigation_resolved +
thread beats as the genuine additions — otherwise a drafter authors a duplicate §3.1 trigger.

### F4 [MINOR] — "chronicle" named as a declared consumer of the two new meta keys, but it is not a registered module/system (phantom consumer)
Synthesis §8 lists consumers of `meta.convergence_detected` as "game_director / articulation /
**chronicle** (causes[] walk)" and of `meta.arc_state_changed` as "game_director / **chronicle** /
articulation". But there is NO `chronicle` module in `module_contracts.yaml` and no `chronicle`
system in `key_type_registry_v30`'s consuming_systems — chronicle is **Tier-3 of
`articulation_layer`** (registry L390 "Articulation may consume for Tier 3 chronicle"). The
synthesis's own conformance rule #2 (consumer-closure) requires a *declaring consumer whose
`consumes:` names it* — "chronicle" cannot declare anything, it is not a module. Not fatal
(articulation + game_director already close both keys), but it is a phantom consumer reference
that would fail a literal consumer-closure lint.
**REQUIRED FIX:** attribute the chronicle-walk consumption to `articulation_layer` (which owns
Tier-3 chronicle), OR actually register a `chronicle` module in `module_contracts.yaml` before
citing it as the declaring consumer. Drop "chronicle" as a standalone consumer name.

---

## Caveats (noted, NOT findings — no break)
- Stage-0 adds render triggers for `meta.convergence_detected` (emitted only at Stage 2/3), so
  Stage-0's "closes ED-IN-0004 + C6" is true for thread-beats/investigation_resolved but the
  meta-key render path is inert until L1/L2 ship. Honesty caveat, not a break — a trigger for an
  unemitted key is harmless.
- "Sidesteps ORD-3 mid-cascade nondeterminism" (§3) is only half-true: detection READ over
  settled state is order-free, but the detector's OWN `meta.convergence_detected` emission
  re-enters the cascade and inherits ORD-3 order. The synthesis's §9 determinism claim already
  states "CONDITIONAL on ORD-3/ORD-4," so it is internally consistent — noted, not scored.
- ORD-4 ownership (game_director-on-World vs scene_slate) is itself Open Flag O-5 in
  `propagation_spec_v1`; the synthesis asserts game_director owns it. Defensible design call that
  closes the hazard; not a break, but it is a fork the synthesis presents as settled.
- scene.dialogue remains a multi-emitter (scene_slate + npc_behavior Procedure E + social_contest,
  ED-1009 open). The demotion of scene_slate to "emits scene.* content keys" doesn't resolve or
  collide with ED-1009 — out of scope, glossed but not broken.

## Verdict: SOUND-WITH-FIXES
No outright integration BLOCKER — the spine's consumed Keys exist, line citations are accurate,
and the two new types are honestly declared. But two MAJORs must be applied before the scene_entered
resolution and the staging can be called integration-clean: F1 (edit §8.5 or it's still a fork) and
F2 (gate Stages 2-3 behind ED-1051/Gate-0). F3/F4 are precision fixes a drafter needs to avoid a
duplicate trigger and a phantom consumer.
