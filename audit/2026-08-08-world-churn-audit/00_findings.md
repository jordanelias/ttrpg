# World Churn — seven-lens read-only audit

## Status: PROPOSED (read-only audit; no canonical head moved, no design text changed, nothing executed)
## Date: 2026-08-08 · Lane: IN (cross-cutting) · ED-IN-0149 · Method: 7 independent Fable-5 read-only lenses

**Question asked:** how does Key-substrate state dynamically change over a campaign as subsystems
interact with events, and do the primitives compose into emergent conditions that reach NPCs, arcs and
events?

---

## §0 · The finding, in one sentence

**The world does not churn because the churn machinery is DISCONNECTED — not because it is scripted.**

Three lenses reached this independently and in their own words. Lens C: *"nothing in this lens is
authored-scripted … the failure mode is not scripting but disconnection: emergent triggers whose input
state can never reach the threshold."* Lens A: trigger paths are **state**-conditioned, never
**entity**-conditioned. Lens B, on the decisive question: scenes are seeded from **live world state**,
not static templates — party faculties are derived at resolve time from current `L`/`Sta`
(`scene_dispatch.py:92-93,135-138`).

This is a good result about the architecture. The guardrail against scripting drift **held**: across
seven lenses, exactly one entity-hardcoding instance was found (`pr119_event_deck_engine.py:74-75,115`),
and it is contained in the zero-caller `sim_harness` prototype cluster. The work ahead is **wiring, not
redesign**.

---

## §1 · What actually churns today (the honest inventory)

The live campaign (`engine/mc_v18.py:260-267`, season as the only world tick) has **three** closed
feedback loops and a handful of autonomous drifts.

**Loop 1 — the political spine (LIVE, compounding, default-ON).**
World `L`/`Sta` → per-season parliamentary vote → writes `L` immediately (`parliamentary_vote.py:213`)
and `L`/`I` deferred at the accounting boundary (`echo_transport.py:430-438` → `mc_v18.py:158-161`) →
next season's vote re-reads the moved `L` (`parliamentary_bridge.py:90-91`). This is the one genuine,
uncontested `world→scene→world` loop.

**Loop 2 — territory ↔ CI ↔ seizure (LIVE).**
Territory ownership/PT → CI yield (`ci_track.py:130-140`) → CI gates Mass Seizure availability
(`mass_seizure.py:303-304`) → seizure rewrites owner/accord → next season's CI yield.
⚠ Qualified below: `resolve_mass_seizure` has **zero callers**, so the seizure leg is unreachable.

**Loop 3 — conquest ↔ signals (LIVE, damped).**
Conquest → adjacency/mil-advantage/undergoverned signals (`faction_action.py:125-212`) → conquest weight
→ conquest. Clamp-damped at `[0.5, 7.0]` (`game_state.py:124-129`).

**Autonomous drift that genuinely exists:** CI +1/season unconditional (`ci_track.py:51,116`), MS −1/year
(`accounting.py:116-117`), and per-season stochastic faction actions (`faction_action.py:220`,
seed-deterministic over state-conditioned weights).

> **CORRECTED after adversarial review (OVERTURN).** An earlier draft listed *"NPE stance drift every
> season (`accounting.py:138`)"* as live autonomous drift. **It is not.** `simulate_npc_actions` iterates
> `_npc_store(world)` = `world.npcs` (`npe.py:338-339`) — the very store D5 proves stays **empty** in
> every live campaign (strict xfail, `test_pipeline_reach.py:596-599`). The call happens every season;
> the drift never does. This was the document's one real internal contradiction — §1 crediting churn that
> D5 of the same document proves impossible — and it is exactly the failure mode this repo names:
> pattern-matching on the call site instead of the concept. Recorded rather than quietly deleted.

**Factions do act on their own** — the single biggest affirmative in the audit. `faction_take_action`
runs per parliamentary, territory-holding faction per season (`mc_v18.py:124-130`).

---

## §2 · What cannot churn — the disconnection register

Ordered by *leverage*: how much already-built machinery one missing edge would light up.

### D1 — The insurgency pipeline is emergent, implemented, invoked every season, and structurally unreachable
*(found independently by Lens C and Lens E — rediscovery-ranked)*

Formation requires ≥2 contiguous **uncontrolled** territories (`insurgency_pipeline.py:39,154`). Exactly
one territory starts unowned (T15, `game_state.py:48`) and **no code path anywhere ever sets
`Territory.owner = None`** — every owner-assign site writes a faction name
(`faction_action.py:468`, `parliamentary_transfer.py:293`, `mass_seizure.py:292`); both
`.territories.remove` sites immediately reassign. *(One qualification, from adversarial review:
`restore_world` (`game_state.py:357`) constructs `Territory(owner=td['owner'])` and **can** re-materialize
`None` from a serialized world. Not a live-campaign churn path — but "no code path anywhere ever" was one
site too absolute, and this is precisely where T1-2's guard test should also look.)* The Revolt step that would create uncontrolled
territory (`peninsular_strain_v30.md:60,483`) is unimplemented, and faction collapse
(`faction_canon_v30.md:300`) is documented-only.

`mc_v18.py:298`'s `insurgencies_formed` telemetry is **structurally always 0**.

Promotion is **doubly** dead: it needs `L ≥ 3` (`insurgency_pipeline.py:44,218`), records are created at
`L = 1.0` (`:41,73`), and **nothing anywhere mutates an InsurgencyRecord's L**. Promotion also sets a
status flag (`:247-248`) but never constructs a `Faction` — stage 4 "full faction status"
(`insurgency_pipeline_v30.md:30`) has no constructor.

### D2 — A victory condition that can never fail
`victory.py:73` reads Turmoil for its `PS ≤ 6` leg. **Nothing writes Turmoil** — no owner module, zero
writers. The condition is vacuously true forever. This is exactly the CLAUDE.md §0.1-point-2 defect
class: *an assertion that cannot observe the failure it excludes.*

### D3 — The Stability-Crisis council cannot clear its own trigger
`Sta ≤ 2` fires the trigger (`scene_dispatch.py:81-95`); the scene's echo writes **`L` only**
(`:334-343`). The scene can never write `Sta`, so a faction at `Sta ≤ 2` refires the **identical**
contest — pinned proceeding (`:117`), pinned policies/genre (`:311-321`) — every season until something
else moves `Sta`. It repeats rather than compounding.

### D4 — Battle casualties evaporate; `Faction.Mil` is a monotone ratchet
`resolve_mass_battle` computes surviving fractions (`massbattle.py:1834-1835,1850-1851`) and returns a
dict; the caller writes owner/garrison/accord/loser-`L` and **never touches either side's `Mil`**
(`faction_action.py:461-497`). A faction can lose ten battles with zero military attrition. Meanwhile
Muster is the **only** `Mil` writer and only ever raises it (`:524`; repo-wide: one `adjust('Mil')`
site). The sole brake is the 7.0 stat ceiling — biasing long campaigns toward conquest saturation.

### D5 — Zero person-scale state changes in a seeded campaign *(Lens D; the most consequential finding)*
Conviction scars, beliefs, coherence and knots are **real, correctly-wired mutable per-actor state**
(including the beliefs↔conviction cyclic pair). But every producer that would feed them is a stub
(`npc_ai.py:33-46`, `companion.py:28-33` — both stubwire no-ops), flag-off, or supplies stakes that never
engage them (`scene_dispatch.py:91`). `generate_npc` has **zero live callers**, pinned by a strict-xfail
asserting `world.npcs` stays empty (`test_pipeline_reach.py:596-599`); `world.knots` likewise
(`:602-606`).

**The `world event → Key → person` path terminates at the Key.** `Target.impact_vector` over the 4
Conviction axes exists (`keys.py:59,96`) and **no code anywhere applies a Key's `impact_vector` or
`stat_deltas` to any person store** — grep finds only validation (`keys.py:400`) and tests. Of the two live
`stat_deltas=` emission sites, **one is faction-facing (`echo_transport.py:421-422`) and one is
settlement-facing (`:319-320`, `actor_id=sid`, `scale_signature=["settlement"]`); neither is
person-facing.** *(Corrected by adversarial review — an earlier draft said both were faction-facing. The
headline is unchanged: no Key reaches a person.)*

⚠ **`generate_npc`'s zero-call state is a Jordan-held honest deferral**, not a defect to "fix" — do not
invent a population count.

### D6 — The conviction gate silently no-ops (a live correctness bug)
`apply_knot_loss` passes `conviction='Loyalty'` (`knots.py:348-353`), which is **not in `CONVICTIONS`**
(`conviction.py:46-49`), so `apply_conviction_scar` returns `magnitude=0` (`:191-193`) **while the caller
still reports `conviction_scar=1`** (`knots.py:345`). Inert today only because `apply_knot_loss` has no
production caller. Fix the **gate**, not the call site — otherwise every future scar writer no-ops
through the same hole.

> **Adversarial review found the defect worse-shaped than described.** The call is *also* wrapped in
> `try/except (ImportError, AttributeError): pass` (`knots.py:353-354`) — **a second silencing layer**. A
> fixed gate that raises would still be swallowed at this call site unless the fix raises a non-caught
> type or the wrapper is removed. "Fix the gate, not the call site" is therefore **incomplete as
> originally written**; plan item T0-1 is revised accordingly.

### D7 — The Key substrate is a telemetry spine, not the churn engine
3 of 55 registry types emit in a live campaign; exactly **one** (`scene.contest_resolved`) closes a
feedback loop through a Key; **zero** Key-to-Key cascades can ever occur because
`DEFAULT_CASCADE_DEPTH_MAX = 0` (`echo_transport.py:91`) makes any depth-1 scheduling raise
`TerminationBreach`. All 13 registered consumers are stubwire no-ops (`articulation.py:140-149`), and
**11 of 13 subscribe to types with no code producer at all — and at default-flag runtime, 13 of 13
receive nothing** (`scene.accord_echo` dormant, `scene.combat_resolved` unreachable). ~39 of 55 types
have zero traffic in either direction.

> **SHARPENED by adversarial review.** An earlier draft printed *10 of 13*. The critic recomputed and
> found no criterion yielding 10: only two of the thirteen types have any code emitter, and
> `scene.combat_felled` has **no Python emit site anywhere**. **The disconnect is worse than first
> claimed.** Operationally this matters: plan item T0-4's instrument must be required to reproduce
> **11/13**, not the erroneous 10/13, or the mistake gets baked into the baseline it pins.

The repo already knows: *"real inter-subsystem traffic ran over 16 direct Python imports. A substrate
with one call site is a prototype, not an architecture"* (`faction_action.py:326-327`).

`references/key_graph.json` declares 56 consumer entries with **no runtime behind any of them** — a paper
graph.

### D8 — Top-down Key delivery has no emitter at all
The armature specs four top-down emitter families (`key_echo_armature_v1.md:98-103`).

> **SOFTENED by adversarial review.** An earlier draft said *"zero have code"* — too absolute. The
> `domain_actions` family has one live emitter: `da.public_governance`
> (`parliamentary_transfer.py:162-176`), fired from the live campaign via `parliamentary_bridge.py:173`.
> It is log-only, names a territory rather than sub-scale actors, and meets none of the row's
> `targets[]`/`impact_vector` spec — so **"no genuinely top-down *delivery* ever fires" stands** — but
> remediation should **extend that existing emitter**, not design the first `da.*` emitter from scratch.
The substrate is direction-agnostic by design, so nothing prohibits it — but
`test_pipeline_reach.py:427-440` "proves" direction #4 by **reusing a bottom-up Key**. No genuinely
top-down Key ever fires in any campaign.

### D9 — The one implemented world→scene difficulty channel idles
`scene_ob_modifier` is computed (`zoom_in_out.py:87`) and stored (`scene_dispatch.py:222`), but **no
resolver consumes it** and no queue site ever populates `ctx['board_degree']` — so it is always 0.
Similarly `zoom_out`'s `pc_incapacitated`/`contested_figure_wounded` (`zoom_in_out.py:138-153`) are never
set and never read; the ED-167 +0.15 commander wound Ob is computed into a discarded dataclass.

### D10 — Treaties, mass seizure, settlement politics: whole mechanisms with no executor
- `process_treaty_expirations` (`treaty.py:121`) is **called by nothing**; `propose_treaty` is stub-wired
  (`:113-118`); and `treaty.py:11-15`'s claim that formation "lives in crown_initiative" is **false
  against disk**. There is **no time-driven expiration churn** anywhere.
- `resolve_mass_seizure` writes `t.owner='Church'` (`mass_seizure.py:292`) — **zero call sites**,
  including tests. This qualifies Loop 2 above.
- The **Mandate ↔ Settlement L/PS loop and its §1.8 damper are BOTH unimplemented**
  (`settlement_layer_v30.md:165-173`). No Python computes `7·T/(T+K)`; "Mandate" in sim code is just
  `Faction.L`; settlement `legitimacy`/`popular_support` are self-declared "NEVER READ OR WRITTEN"
  (`registry.py:69-72`). *Corrects the audit's own framing:* the loop neither explodes nor idles — it
  does not exist. Tracked as ED-FA-0004 / OI-37.
- Fieldwork and investigation are **total stubs** (`fieldwork.py:38-59`, `investigation.py:30-51`,
  honestly flagged ED-916); nothing ever queues those scene types.
- `parliamentary_stay` is inert (zero callers outside its module), so the tribunal-stay consequence can
  never land.

### D11 — Arcs are generated from documents, not from churn — and the generator reads evacuated paths
`skills/valoria-arc-generator/SKILL.md` is an LLM protocol reading **design docs/params**, not live world
state, not sim output, and not `is_arc_vector` (which is written at `npe.py:280`, serialized, and **never
read by anything**). Its read protocol requires `params/*.md` (`SKILL.md:46-57`) and its output target is
`arcs/simulated/` (`:22,66,122`) — **both trees were evacuated 2026-08-05 (ED-IN-0145)**, and `arcs/` is
marked "do not recreate". **Following this skill as written would recreate an evacuated tree.**

The relational graph is likewise DOC-ONLY: `npc_relational_graph_v30.md:501-528` marks the §7 defection
cascade "BUILT 2026-06-09", but `canon/relational_edges_v30.yaml` **does not exist** and grep for
`sworn|defection|fragility|relational_edge` in `*.py` finds zero implementations. "BUILT" there means
design-written.

### D12 — Fidelity asymmetry, measured
Combat: 15 engine modules with per-turn wounds/fatigue/measure/pursuit-sigma; **total external coupling
at default is zero** (`DISPATCH_COMBAT_BRIDGE` off *and* no `queue_scene("combat")` site exists). Even
flag-on it is one `int` in (`round(Mil)`) and one trit out onto a degenerate self-echo.
Contest: a multi-module kernel (8 proceedings) coupled by two derived ints in and one of three degrees
out. Combat state resets per fight (`wrapper.py:468`); the contest kernel is world-pure.

**Internal-state-to-boundary-state ratio: dozens of tracked variables to one scalar, per subsystem.**

---

## §3 · Latent traps (inert today, wrong tomorrow)

- **`temperaments.py` read/write asymmetry** — exactly the CLAUDE.md §0.1-point-1 class. The writer stores
  into `world.npc_drift_state` when `world` is passed (`:153,158`); the reader `temperament_modifiers`
  calls `_drift_store()` with **no world argument** (`:117`) and **cannot accept one** (`:105`). Any
  world-scoped drift write would be invisible to every read. Both sides are currently zero-caller — a
  wired-tomorrow trap.
- **Three divergent conviction vocabularies** — substrate 4 axes (`keys.py:59`), character sim 9 names
  (`conviction.py:46-49`), NPE 8 names (`npe.py:80`, the pre-taxonomy_v30 set). **Any Key→person edge
  built before reconciling these is shape divergence by construction.**
- **Four unreconciled scale vocabularies** — `keys.py:65` 4-enum vs `handoff_rules.py:35-40` 6 labels
  (zero overlap in spelling *or* membership) vs contracts' 7 vs mechanics_index's 9. Already held for
  Jordan (OI-40a / ED-IN-0103).
- **Two Accord unit dialects** — `Settlement.order` 0–5 index vs `Territory.accord` 0.5–7.0 continuous
  (`game_state.py:157`), monitored only by a report-only probe.
- **CI start-value drift** — code 30.0 (`game_state.py:244`) vs `CI_STARTING = 28` (`ci_track.py:71`) vs
  registry 28 (`clock_registry_v30.md:17`). Acknowledged in-code, unresolved.

---

## §4 · Stale claims the audit corrected (docstring vs disk)

The tree asserts, in several places, a property it no longer has:

- `scene_dispatch.py:417-418` and `mc_v18.py:138-140` still say scenes are *"side-effect-free on
  strategic stats by construction."* **False under defaults** since ECHO_TRANSPORT flipped ON — a fired
  Stability Crisis writes `Faction.L` at accounting. The text describes the pre-ED-SC-0007 world.
- `echo_transport.py:20-23` says the §5.2 path *"is INERT there"*; `mc_v18.py:104` says `keys_emitted` is
  *"0 while scenes defer"*. Both contradicted by the same tree — `test_battle_concluded_key.py:71`
  asserts `keys_emitted > 0`.
- `faction_action.py:324-325` misattributes the prior sole live emitter as `scene.accord_echo`;
  `test_battle_concluded_key.py:5` says `scene.contest_resolved`. The measurement is real; the type name
  is wrong.
- `echo_transport.py:22` cites `sim/tests/test_echo_transport.py` — a **retired-tree path**.
- `treaty.py:11-15` claims treaty formation "lives in crown_initiative"; `crown_initiative.py` contains
  no treaty code.

These are the *"comment asserting a property the tree lacks"* class CLAUDE.md §8 flags — the kind that
stops the next reader from looking.

---

## §5 · The ratified churn design, and what became of it

`audit/2026-07-05-emergent-narrative-engine/narrative_engine_design_v2_churn.md` is **RATIFIED**
(ED-IN-0011, 2026-07-05) and specifies exactly this subject: a stack L0 generator → L1 store+tick →
**L1.5 forecast** → L2 detect → **L3 Light Function** (subtract-only pruning-as-authorship) → L4
cast/impel → L5 render. `workplans/workplan_v6_progress.yaml` maps it to M2 stages S0–S5.

**Landing verdict: forecast objects, Light Function, arc-vector templates, the claim-grammar additions
and fixture F8 — NONE landed.** Only R-F2 (deterministic key-log hash, `keys.py:157,340-342`) and the F7
smoke oracle (`engine/tests/test_f7_smoke_oracle.py`) are real.

Two things rotted underneath it:

1. **The 138-arc validation corpus the L0 compile calibrates against was evacuated**, so the ratified
   compile *cannot run as specified on `main`* — while an **unratified** proposal
   (`settlement_generator_v1.md:127`, own Status: "PROPOSAL / working notes, Jordan-vetoable") has
   claimed the L0 slot. Forks 1 and 2 (ratified-at-default, "execution remains") are likewise **mooted by
   evacuation**: there is no `arc_register_events.md` to strike ARC-T04 from.
2. **`spec/churn_amendments.md`, a ratified normative companion, no longer resolves.** Its content now
   lives inside `_workings_joined.md`, under a banner reading *"Not independently ratifiable."*
   `CURRENT.md:165` still cites the dead path.

Leaving both L0 claimants true is **scripting-drift-by-neglect**: a ratified design and an unratified one
occupying the same slot.

**Highest-leverage single unblock:** ORD-3/ORD-4 + the `canonical_key_log` serialization spec. They
already block the substrate's own observer steps (`engine/substrate/__init__.py:17-19`,
`keys.py:10-11`), `propagation_spec_v1.md:393` names them as its own precondition, and everything
forecast-shaped is downstream.

One premise **dissolved**: v2 justified fixture F7 partly on *"the known degenerate ~87% win-share"* —
`test_f7_smoke_oracle.py:6-8` shows that figure was a small-N artifact of an unguarded `run_batch(8)`,
since eroded. The guard exists anyway; the justification is stale.

---

## §6 · Method note — corrections the lenses made to each other

Recorded because a synthesis that hides its disagreements is not evidence:

1. **Lens F corrected A and B** on mechanism: the live scene-phase world writes are **three**, not two,
   and **not all via `ctx['echo']`** — `parliamentary_vote.py:213` writes `L` directly, and the
   territory-transfer motion (`parliamentary_bridge.py:217`) is a third.
2. **Lens F softened the "side-effect-free" claim** — the text exists verbatim but describes pre-default-
   flip behaviour, so it is a stale comment, not a live property.
3. **Lens E corrected the brief itself** on the Mandate↔L/PS damper: "loop without damper" was the wrong
   dichotomy; both halves are unimplemented.
4. **Lens E softened ED-MB-0043**: `state: []` is *accurate* for the 5-module engine (it is a pure
   function); `consumes: []` is what is false-in-spirit, since it reads `Faction.Mil`.

**Independently rediscovered (highest confidence):** D1 insurgency-unreachable (C, E); D7
`battle_concluded` log-only with no consumer (A, E); D9 dead zoom channels (B, F); `Faction.intel` dead
(A, E); `Settlement.order` wired-dormant (A, B, C, E).

**Weakest claims, carried forward honestly.** Several rest on grep with a known blind spot for
dynamic/duck-typed access (§0.1 point 5): "39 types zero traffic", "nothing mutates insurgency L", "no
code sets `owner = None`", "no code computes Mandate". None has a guard test pinning it — which is
itself the recommendation in §D of the plan. Two claims are instrument-less by choice: no lens asserted
how often `Sta ≤ 2` is actually reached in a seeded campaign, because none could execute code, and
§0.1 point 4 forbids a number without a control.

## §7 · J2 consequence (verified, MB lane)

The campaign's only battle-resolver import is the **retired** 5-module engine (`faction_action.py:431`);
nothing in `engine/` or `systems/` imports the canon `tests/sim/mass_battle/`. So all strategic-layer
battle churn is produced by the retired engine, and the canon engine's richer state (per-cell morale,
facing, casualties) writes nothing into the world. *Observation:* `main`'s 16 MB golden failures live
entirely in the canon engine and cannot currently affect campaign churn **precisely because of this
disconnect**.
