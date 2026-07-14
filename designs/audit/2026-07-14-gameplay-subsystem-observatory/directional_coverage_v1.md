# All-Directions Coverage — the Six (+Temporal) Delivery Directions in Detail (v1)

## Status: FILED — 2026-07-14 · ED-IN-0064 · companion to `subsystem_synthesis_v1.md` §8

> **Leads, not verdicts.** Directional cells derive from the machine wiring (`structure/data/g_l2.json`,
> `module_map_flat.md`, `module_contracts.yaml`) cross-checked against live `sim/` code (every `code:` claim below
> was grep-verified this run — file:line cited). The `scales:` vocabulary is itself unreconciled (WS2,
> ED-IN-0056), so a per-cell direction is a strong signal, not a gate. **All fixes HELD-BACK (ED-1094).**

## The premise — one substrate, all directions

Valoria has **no per-direction channel**. The Key substrate (`key_substrate §4.1/§4.2`) runs a single update rule:
emit a Key, resolve an observer set from three independent sources — `source_actor`, every `targets[].actor_id`,
and (for public Keys) `actors_in_scale(scale_signature)` — then apply `key.stat_deltas` to each observer.
**Direction is an *emergent property* of a Key's `targets[]`, `scale_signature`, and `causes[]`** — not a routing
table (`scale_transitions_v30 §12.1`, ruling J-1 / ED-1038). This is elegant, and it is exactly why "check all
directions" is subtle: a direction can be *mechanically supported by the substrate* yet **unreached in practice**
because no emit site ever populates the field that would make the substrate carry it that way. The audit's job is
to separate three very different states that all look like "cross-scale works":

- **LIVE** — a real emit site populates the field and a live caller fires it end-to-end.
- **ANNOTATION-DEBT** (the `!A6` / A6-exemption class, §12.2) — the mechanism exists and is *exercised elsewhere*;
  a specific emitter just hasn't populated its sub-scale `targets[]`. **Fixable by authoring discipline, no new apparatus.**
- **DOCTRINE-ONLY / UNCALLED / DEFERRED** — the function exists in code but **has zero callers**, or the field is
  **never populated anywhere**, or the term is an **explicit un-shipped deferral**. This is *not* annotation-debt —
  the direction is genuinely dead until someone wires or builds it.

The synthesis's first pass collapsed the second and third states into "annotation-debt." This document separates
them. **Bottom line up front: only two of the seven directions are live end-to-end.**

| # | Direction | Verdict | The issue |
|---|---|---|---|
| 1 | **lateral / horizontal** | 🟢 LIVE | Same-scale delivery works; the one exception is the zero-Key trio. |
| 2 | **bottom-up (aggregate)** | 🟡 SPLIT | Domain-Echo *core* is LIVE (ECHO_TRANSPORT default ON); the **Accord echo** leg is built-but-**uncalled**. |
| 3 | **vertical-up (8 handoffs)** | 🔴 DOCTRINE-ONLY | The dispatcher is an **import-orphan**; §3.3 is an **empty stub**. |
| 4 | **top-down (distribute)** | 🟡 ANNOTATION-DEBT | The 8 `!A6` seams (sparse `targets[]`); plus territory **transfer is uncalled**. |
| 5 | **down-diagonal** | 🟡 ANNOTATION-DEBT | Same class as top-down (`!A6`). |
| 6 | **diagonal (skip-scale, `causes[]`)** | 🔴 UNREACHED | **Zero executable instances** — `causes[]` is populated *nowhere* in `sim/`. |
| 7 | **temporal (cadence + decay)** | 🟡 SPLIT | Cadence partially wired; the general **`decay()` is an explicit deferral**. |

---

## Direction-by-direction, in detail

### 1 · Lateral / horizontal — 🟢 LIVE
**Mechanism.** Same-scale observers resolved via a shared `scale_signature` + scene presence (§12.1). No targeting
discipline needed — public Keys reach same-scale actors automatically.
**Status.** Live and dominant. The bulk of the 43-edge simple graph is lateral within a band: `faction_politics →
faction_state` (provincial↔provincial), `game_director → audit/scene_timer` (scene↔scene), `npc_behavior →
npc_memory/piety_track`, `threadwork/fieldwork → npc_behavior/piety_track` (all personal↔personal), `settlement_layer
→ settlement_economy`.
**The one issue.** The zero-Key trio — `ci_political`, `territorial_piety`, `victory` — emit and consume *nothing*
(`consumes:[] emits:[]`), so they are ABSENT even laterally. That is not a lateral-mechanism failure; it is a
wiring absence (GAP-E1/E2, and `victory` reads clocks directly). **Solution:** key their emitters/consumers (CTC).

### 2 · Bottom-up / aggregate — 🟡 SPLIT (core LIVE, Accord leg UNCALLED)
**Mechanism.** A scene/personal Key that meets *Sufficient Scope* (§7) echoes up to the faction scale via **Domain
Echo** (§5). This is how a duel won, a settlement governed, or a contest carried becomes a strategic-layer
consequence — the spine of the "personal actions matter strategically" promise.
**Live core — VERIFIED.** `ECHO_TRANSPORT` is **default ON** (`sim/mc_v18.py:47`, "default ON (Jordan
ratification)", ED-IN-0028/SC-0006/0007, 2026-07-08). `compute_domain_echo` fires through
`echo_transport.emit_scene_echo → scene_dispatch` and `parliamentary_bridge.run_parliamentary_scene ←
mc_v18._faction_actions_callback`. Every solid up-edge in the graph (`scene.gift`, `scene.contest_resolved`,
`state.scar_acquired`, `meta.miraculous_event`, `scene.battle_concluded` → `faction_state`) rides this. **This is
genuinely live end-to-end** and post-dates the 2026-07-13 governance docket, which reported it dead.
**The issue — the Accord leg is built-but-uncalled (GAP-DIR-2).** The *event-driven* Accord echo,
`domain_echo.compute_accord_echo` (`sim/cross_scale/domain_echo.py:128`), has **zero callers** (grep-verified: only
its def + docstring exist). A live *static* Accord recompute stands in, so settlements still aggregate — but the
**event-reactive** path (a specific scene outcome nudging provincial Accord in the moment) is dead. This reproduces
governance **GAP-A2** exactly.
**Also caveat.** The live firing path is the **faction-scale** parliamentary vote + a **synthetic** emergency
council (parties derived from aggregate faction stats). The **true personal-actor → faction** path still **defers**
on the context-derivation bridge (`scene_dispatch` — "combat, and any future contest… still defer"). So bottom-up
works at the faction-aggregate grain; it does not yet carry an *individual* actor's scene up to a faction decision.
**Solution.** (a) Wire `compute_accord_echo` into `echo_transport` beside `compute_domain_echo` (CTC — the function
is written). (b) Land the context-derivation bridge to move the personal-actor→faction path off "defer" (the
larger, partly-genuine piece — it needs the SC context-derivation design, ED-SC-0006/0007).

### 3 · Vertical-up — the eight named handoffs — 🔴 DOCTRINE-ONLY
**Mechanism.** §3.1–§3.8 are the *named, curated* cross-scale procedures (Personal→Thread, Personal→Faction via
Domain Echo, Thread→Mass, Mass→Personal duel, Scene→Mass, …) — "authored sugar over the substrate" (§3 preamble).
**Status — orphaned dispatcher (GAP-DIR-4).** `sim/cross_scale/handoff_rules.py` implements all eight as descriptor
rules but is an **import-orphan** — grep-verified: **nothing in `sim/` imports it** (`No matches`). The handoffs
that *do* fire (e.g. §3.4 Domain Echo) fire through `echo_transport`/`domain_echo` directly, not through the
dispatcher. So the curated handoff layer is present-but-bypassed.
**Plus an empty stub.** **§3.3 Personal→Scene (Contest)** is a canon stub — `scale_transitions_v30.md:51` is a
header with no body; `handoff_rules.py` fills it with a one-line "brief in canon" placeholder. This is the same
empty-handoff the governance docket flagged (ED-IN-0049).
**Solution.** Either (a) route the live cross-scale calls *through* `handoff_rules.py` so the dispatcher is the
single home (CTC — de-orphan it, then §8 "one rule, one home" holds), or (b) formally demote `handoff_rules.py` to
reference-only and delete the import expectation. Author §3.3's body (GENUINE-small — the Personal→Contest handoff
content genuinely doesn't exist).

### 4 · Top-down / distribute — 🟡 ANNOTATION-DEBT (+ one uncalled resolver)
**Mechanism.** A strategic/environmental Key names sub-scale `actor_id`(s) in `targets[]` and includes the sub-scale
in `scale_signature`, so `actors_in_scale` resolves the personal/settlement observers (§12.1/§12.3).
**Status — the eight `!A6` seams are the exemption class.** §12.2 grants the A6 exemption: these are a missing
*rule + populated targets*, **never a missing mechanism**. §12.4 enumerates them exactly:
`domain_actions → {npc_behavior, piety_track, settlement_economy}`, `faction_politics → npc_behavior`,
`peninsular_strain → {npc_behavior, settlement_economy, settlement_layer}`, `scenario_authoring → settlement_layer`.
The consumers are already registry-canonical; only the emitter-side sub-scale `targets[]` are sparse. **This is
genuine annotation-debt** — the synthesis's classification here is correct.
**The uncalled resolver (GAP-DIR-3).** Distinct from the seams: the **territory transfer** resolver,
`parliamentary_transfer.propose_transfer` (`sim/provincial/parliamentary_transfer.py:101`), has **zero callers**
(grep-verified). `parliamentary_bridge` wires the Mandate-penalty *vote*, not the transfer. So "a faction takes a
named settlement/territory top-down" is built and dead. Reproduces governance **GAP-A1**.
**Solution.** (a) Seams: populate sub-scale `targets[]` per §12.3 — a batch authoring pass, Lane B (CTC). (b)
Transfer: connect `parliamentary_bridge`'s vote outcome to `propose_transfer` (CTC — both ends exist).

### 5 · Down-diagonal — 🟡 ANNOTATION-DEBT
**Mechanism.** Top-down across a system-family boundary (e.g. a peninsula-scale environmental Key reaching a
settlement-scale economic actor). Same substrate path as top-down, same `targets[]` discipline (§12.1).
**Status.** Same exemption class as #4 — the `!A6` down-seams that cross a family boundary. No separate mechanism
gap. `faction_state → npc_behavior` and `miraculous_event → npc_behavior` are drawn *solid* (already populated),
proving the mechanism is exercised. **Solution:** the same §12.3 `targets[]` pass (CTC).

### 6 · Diagonal (skip-scale, `causes[]`) — 🔴 UNREACHED — the headline directional gap (GAP-DIR-1)
**Mechanism.** A cross-scale *consequence chain*: a Key's `causes[]` field links it to a downstream Key at another
scale, so a consequence "skips" intervening scales along a provenance chain (§12.1; the §5.6 Thread Echo exemplar).
This is the direction that lets a distant cause ripple to a distant effect without touching every rung.
**Status — ZERO executable instances (VERIFIED).** The substrate *supports* it (`sim/substrate/keys.py` has the
`causes[]` field + a DAG walk), but **no emit site in `sim/` ever populates `causes=`** (grep-verified: `causes=`
across `sim/**` returns only the def/serialize/validate in `keys.py` — no domain code sets it). The named exemplar,
§5.6 Thread Echo `domain_echo.compute_thread_echo` (`sim/cross_scale/domain_echo.py:178`), has **zero callers**. And
the armature concedes it *verbatim*: **"The diagonal direction has zero executable or exemplified instances"**
(`designs/architecture/key_echo_armature_v1.md:41`; "~15% … currently unauthored", L126).
**Why this is worse than annotation-debt.** Annotation-debt means "the mechanism runs; one emitter is sparse."
Diagonal is different: the mechanism has **never once run** — there is no exemplar to copy, no `causes[]`-populated
Key anywhere. A designer wanting a skip-scale consequence has no worked example. This is a genuine
authoring-and-exemplar gap, not a targets[] omission.
**Solution.** Author the **first** `causes[]`-populated exemplar end-to-end — the natural candidate is §5.6 Thread
Echo (a Thread operation causing a distant settlement/faction consequence), which already has a written (uncalled)
resolver. Wire `compute_thread_echo`, populate `causes[]` on its output Key, and add a substrate test that walks the
chain. Once one exemplar exists, further diagonals are CTC; today it is a genuine (small-surface) build.

### 7 · Temporal (the 7th direction) — 🟡 SPLIT (cadence partial, decay DEFERRED)
**Mechanism.** The armature lists a seventh **temporal** direction (`key_echo_armature_v1.md` §2.6: cadence and
ordering). Two halves: (a) *cadence/ordering* — when Keys apply relative to the Accounting boundary; (b) *decay* —
entropy that pulls quantities back over time.
**Status.** (a) Cadence is **partially wired** — `TickScheduler` deferred-apply, `accounting_boundary()`/`next_tick()`
(`mc_v18.py`), per-type `default_time_horizon` (registry), and the gated Year-End MS decay
(`sim/peninsular/accounting.py:61` calls `apply_ms_baseline_decay` under "PP-255 — Year-End cadence" — grep-verified;
this is exactly the mechanism that makes GAP-F1/MS a *wiring* gap, not a design gap). (b) The **general `decay()`
term is an explicit un-shipped deferral (GAP-DIR-5)** — the armature: "substrate ships WITHOUT decay … deferred to
Stratum B+." So event-builds accumulate without entropy. Reproduces governance **GAP-B4** (ΔLegitimacy has no decay
term) and **GAP-A4** (cross-tick convergence unproven; the D.6 double-count).
**Solution.** MS decay is already the worked cadence exemplar — generalize its pattern into the deferred `decay()`
term when Stratum B (cross-tick convergence) actually starts. Until then, `decay()` is a **ruled deferral**, not an
oversight — flag it, don't "fix" it. (Any faction/settlement quantity that "only goes up" — ΔLegitimacy, standing
event-builds — is a symptom to list against this deferral.)

---

## The 16 × 6 matrix (per-subsystem directional participation)

COVERED = wired/live · A-DEBT = declared-but-sparse/uncalled (exemption class) · ABSENT = no edge · the zero-Key
trio is ABSENT everywhere. Read a row as "which directions this subsystem's wiring actually participates in."

| Subsystem | bottom-up | lateral | vertical-up | diagonal | top-down | down-diag |
|---|---|---|---|---|---|---|
| personal_combat | A-DEBT¹ | COVERED | A-DEBT | ABSENT | COVERED² | ABSENT |
| social_contest | COVERED³ | COVERED | COVERED-decl | ABSENT | ABSENT | ABSENT |
| mass_battle | COVERED³ | COVERED | COVERED-decl | ABSENT | ABSENT | ABSENT |
| threadwork | A-DEBT⁴ | COVERED | A-DEBT | **A-DEBT⁵** | ABSENT | ABSENT |
| fieldwork_knots | COVERED³ | COVERED | COVERED-decl | ABSENT | ABSENT | ABSENT |
| domain_actions | ABSENT | COVERED | ABSENT | ABSENT | A-DEBT⁶ | A-DEBT⁶ |
| faction_state | ABSENT | COVERED | ABSENT | ABSENT | COVERED⁷ | COVERED⁷ |
| faction_politics | ABSENT | COVERED | ABSENT | ABSENT | A-DEBT⁶ | A-DEBT⁶ |
| ci_political | ABSENT | **ABSENT⁸** | ABSENT | ABSENT | ABSENT | ABSENT |
| territorial_piety | ABSENT | **ABSENT⁸** | ABSENT | ABSENT | ABSENT | ABSENT |
| settlement_layer | COVERED³ | COVERED | COVERED⁹ | ABSENT | A-DEBT⁶ | A-DEBT/COV⁹ |
| peninsular_strain | ABSENT | ABSENT | ABSENT | ABSENT | COVERED+A-DEBT⁶ | A-DEBT⁶ |
| npc_behavior | COVERED¹⁰ | COVERED | COVERED | ABSENT | COVERED¹⁰ | COVERED¹⁰ |
| piety_track | COVERED³ | COVERED | COVERED | ABSENT | A-DEBT⁶ | A-DEBT⁶ |
| miraculous_event | COVERED³ | COVERED | COVERED | ABSENT | COVERED⁷ | ABSENT |
| victory | ABSENT | **ABSENT⁸** | ABSENT | ABSENT | ABSENT | ABSENT |

¹ combat emits `scene.combat_resolved/felled` with registry consumers but the emits **dangle** (GAP-C2). ² consumes
`scene.combat_strike`. ³ Domain-Echo up-emit to `faction_state` (solid). ⁴ threadwork's up-path is §3.5/§5.6 only —
no faction-targeting Key in its emits (both land personal). ⁵ the diagonal exemplar — see #6. ⁶ `!A6` down-seam
(§12.4, annotation-debt). ⁷ `faction_state→npc_behavior`, `miraculous_event→npc_behavior` are **solid** (populated).
⁸ zero Key integration — unkeyed. ⁹ settlement aggregate-up (`Order→Accord`, `L/PS→Mandate`) + Mandate→L/PS down are
**live derivations** (§1.8), not Keys. ¹⁰ npc_behavior consume-edges for the down-seams are present (the `!A6` debt
is emitter-side).

**Reading the matrix:** three columns are healthy (lateral, and the up columns for the personal/scene producers via
Domain Echo). The two down columns are uniformly A-DEBT (the seams). The **diagonal column is empty for all 16** —
that is GAP-DIR-1 rendered as a stripe. The three ABSENT-everywhere rows are the zero-Key/reader trio.

---

## Seam reconciliation — why "20 / 19 / 15" are the same set

The three published seam counts are one set sliced three ways (verified):
- **20** = per-type `!A6` tags on the 9 mermaid module-pair edges (4+2+1+4+1+1+2+1+4).
- **19** = the module_map §5 "top-down" subset = 20 − the 1 lateral `scene.draft_da` folded into the
  `domain_actions→npc_behavior` bundle.
- **15** = §12.4's "15 type-edges / 8 seams" = 20 − the 4 `scene_slate→piety_track` edges − `scene.draft_da`.

**8 of the 9 machine seams == §12.4 exactly.** The **9th, `scene_slate → piety_track`, is a scale-signature
mislabel, not a genuine down-seam:** the four types (`scene.dialogue/insult/threat/witness`) carry
`default_scale_signature: [personal]` and `piety_track` is `[personal]` — no cross-band delivery occurs. The
identical bundle `scene_slate → npc_behavior` is drawn **solid** because `npc_behavior` declares
`scales:[personal,scene]` (shares `scene`) while `piety_track` omits `scene`. **Fix = scale-vocabulary
reconciliation (WS2) / add `scene` to piety_track's `scales:`** — not `targets[]` population. It belongs to the
exemption class by a *different* mechanism than the 8 strategic-down seams.

---

## Why each dead direction matters for the videogame (player-facing consequence)

- **Diagonal unreached** → no "a cause here ripples to a distant effect there" — the setting's calamity/insurgency
  chains can't propagate as skip-scale consequences; every consequence must be hand-chained rung by rung.
- **Accord echo uncalled** → a *specific* scene win doesn't nudge provincial Accord in the moment; only the slow
  static recompute does — strategic feedback feels laggy/indirect.
- **Territory transfer uncalled** → winning a parliamentary vote doesn't actually move a settlement/territory —
  the strategic map can't change hands through the political loop yet.
- **Handoff dispatcher orphaned / §3.3 empty** → the curated cross-scale procedures aren't the single home; a
  Personal→Contest zoom has no authored handoff.
- **Temporal decay deferred** → faction/settlement pressures only accumulate; without entropy, legitimacy and
  standing ratchet up and never relax, so long campaigns drift toward saturation (the D.6 double-count risk).
- **Personal-actor→faction path deferred** → an *individual's* deed reaches the faction only as aggregate stats,
  not as that character's act — the "my character mattered strategically" beat is muted.

---

## Solutions roadmap (ordered by leverage; all HELD-BACK)

1. **Wire the two built-but-uncalled resolvers** (CTC, highest ROI, code exists): `compute_accord_echo` into
   `echo_transport`; `propose_transfer` off the `parliamentary_bridge` vote outcome. → un-deadens bottom-up Accord +
   top-down transfer. *(New leads GAP-DIR-2, GAP-DIR-3 → FA/SC lanes.)*
2. **Author the first diagonal exemplar** (GENUINE-small): populate `causes[]` on §5.6 Thread Echo, wire
   `compute_thread_echo`, add a chain-walk test. → converts diagonal from "zero instances" to "one exemplar," after
   which further diagonals are CTC. *(GAP-DIR-1 → WR/cross_scale lane.)*
3. **Batch the §12.4 `targets[]` annotation pass** (CTC, Lane B): the 8 down-seams. → converts top-down/down-diag
   from A-DEBT to LIVE. *(GAP-D1/D2/D3, annotation-debt.)*
4. **De-orphan or demote `handoff_rules.py`** and author **§3.3**'s body (mixed CTC/GENUINE-small). *(GAP-DIR-4.)*
5. **Fix the `scene_slate→piety_track` scale mislabel** — add `scene` to piety_track's `scales:` (WS2 vocabulary).
6. **Land the personal-actor→faction context-derivation bridge** (the larger, partly-GENUINE piece; ED-SC-0006/0007).
7. **`decay()` stays a ruled deferral** until Stratum B — flag the "only-goes-up" quantities against it; do not
   "fix" it now (GAP-DIR-5).

**One-line verdict for the user's "check all directions":** of seven directions, **two are live end-to-end**
(lateral + bottom-up Domain-Echo core), **two are honest annotation-debt** (top-down + down-diagonal seams), and
**three hide a genuine uncalled/unreached/deferred gap** (diagonal = zero instances, the handoff dispatcher +
Accord/transfer resolvers = built-but-uncalled, temporal `decay()` = deferred). The substrate *can* carry all
seven; today it *does* carry two.
