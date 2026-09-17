# Mass-battle historical-fidelity readiness — consolidated audit + roadmap (2026-07-23)

Synthesis of a multi-axis audit of the spatial-model-v2 field engine (`tests/sim/mass_battle/`) against the
question: **can it faithfully reproduce the historical battles we use to validate it top-down (Cannae,
Leuctra, Gaugamela, Zama)?** Five independent adversarial critics, an architectural cell-up audit, a
granularity audit, a capability-vocabulary audit, a ratified-but-unbuilt sweep, and a full-campaign gauge
A/B were run. This is the integrated verdict and a prioritized roadmap.

## Verdict in one line

The **primitives and the aggregation spine are sound and genuinely cell-up**; **granularity is adequate**;
the fidelity ceiling is **not numeric resolution but (a) three missing capability layers needed to *stage*
these battles and (b) the DG-6 variance-structure problem that governs whether a correct *staging*
reproduces the *result*.** The geometry model was just made rigorous (octagon damage + perimeter target
points); the maneuver layer is the main remaining architectural debt.

## Axis 1 — Architecture: is it built cell-up? (mostly YES)

| Link | Verdict | Note |
|---|---|---|
| cell → subunit | **EMERGENT** | pool/troops/frontage aggregate from `cell_troops`; column is an emergent view |
| subunit → unit → army | **EMERGENT** | envelopment/refused-flank are emergent compositions (ED-909), not templates |
| engagement → casualty magnitude | **EMERGENT** | per-cell contact → per-pair damage; attribution is proportional-by-density (aggregate-equivalent today, latent drift when per-cell power exists) |
| octagon damage **arc** | **EMERGENT** | per-cell facing vs local attacker centroid |
| movement **maneuver-goal** | **SCRIPTING-DRIFT** | `_envelop_goal`/`_sweep_goal` are hardcoded 2-waypoint state machines (steering substrate under them is emergent) |
| octagon **multi-side shock** | **FIXED** (was drift) | ED-MB-0019 moved it from a subunit-pair count to a bearing/face aggregation |

**The one real architectural debt:** the wrap trajectory is choreographed, not discovered. The
`perimeter_targeting_geometry_v1` spec retires it — "approach the rear face along its normal" makes the
wrap *emerge*. Also flagged: casualty attribution and per-cell power/type are uniform today (aggregate-
equivalent), a latent drift to close when heterogeneous cells (veteran-front/levy-rear) land.

## Axis 2 — Granularity: fractional dice / fractional Ob where needed? (ADEQUATE)

- **Pool** = integer (double-floored). **Roll** = hybrid (discrete d10s + a *continuous* σ-head μ-shift).
  **Degree** = float comparison collapsed to 4 buckets (mitigated: damage stays continuous within a tier).
  **σ head** = continuous.
- The octagon damage multiplier (ED-MB-0018) is the template done right: a continuous facing exposure on a
  continuous casualty multiplier, not a `round()`ed integer-pool penalty.
- **DG-6 is a variance-STRUCTURE problem, not a granularity one** — the discrete and continuous engines are
  provably distribution-equivalent, so fractional dice/Ob are orthogonal to it. The fix is the once-per-
  battle CEV friction (ED-MB-0016), not finer numbers.
- One real fixable leak: **puncture is `int()`-floored inside the continuous σ-channel** — specificity
  discarded where it should be kept (a one-line fix, logged for a follow-up).

## Axis 3 — Capability: enough vocabulary to *stage* these battles? (RICH, 3 gaps)

**Present & strong:** Line/Arrowhead/GappedLine/Column shapes + continuous depth; ~11 troop types incl.
ranged (archers/crossbow/sling/horse-archer/artillery) and cavalry/knights/pike; per-type weapon reach;
WIRED instructions (brace/envelop/sweep/kite/yield/shoot-move); a conditional timed `Order` queue
(`immediate|tick|enemy_range|ally_at`) + conditional targeting; deployment presets (Cannae/Leuctra shapes);
and — as of ED-MB-0018/0019 — a rear-2× / multi-side encirclement **damage** model.

**Fidelity-critical gaps** (per-battle mapping in `capability` audit):

1. **Concurrent multi-body engagement + cavalry rear-transit** — *ratified-but-unbuilt* (`proposals/
   multiunit_envelopment_plan.md`, Path B, Phase-1 never started). Blocks Cannae ring-closure, Cannae/Zama
   cavalry-return-to-rear, all true N-on-1 fix-and-flank. `run_multi_unit_battle` silos each pairing 1v1.
2. **Multi-line depth / triplex-acies reserve lines + reserve commitment** — single-line only today.
   Required for the Roman grid at Cannae and generic reserve doctrine.
3. **Elephants + chariots + triggered lane-channeling** — *not-yet-designed*. Required for Zama/Gaugamela.

**Secondary:** battle-state conditional triggers (`ally_routed`/`casualty_frac`/`enemy_cleared`) + a thin
army-plan object; wire the INERT instructions (`lure`/feigned-retreat, `pin`, `screen`, `reserve`,
`refuse`); emergent (auto) fighting-withdrawal entry + rally/pocket exits; Square + cavalry rhomboid shapes.

## Axis 4 — Geometry: made rigorous this session

- **Octagon = damage-received multiplier** (front 1× / flank 1.5× / rear 2×), reaction delay (a rear strike
  is blind → the 2× persists), multi-side shock (graded by distinct faces). Shipped + adversarially
  hardened (ED-MB-0018/0019).
- **Perimeter target-points + face normals** (Jordan 2026-07-23) — the approach/targeting backbone: major
  (face-mid) + minor (corner) target points, each with an outward normal = required approach angle; the
  attacker aligns its body on the normal before contact; pointed tips (≲60°) are a vertex exception. Spec'd
  in `perimeter_targeting_geometry_v1.md`; **this is the lever that makes the wrap emergent and retires the
  maneuver-goal scripting-drift.**

## Axis 5 — Outcome fidelity (DG-6) — the cross-cutting gate

Even a perfectly-staged battle currently mis-bands its *result*: the melee pool self-averages (CV ~ 1/√N)
→ `compute_degree` becomes near-deterministic from the force ratio → 100%/0% vs historical ~65–83% bands.
The gauge A/B for the octagon flip: mirror byte-identical; rows it moves shift **toward** bands (H2/H5/H6),
**none** more over-decisive; but H3/H4 envelopment is *already* 100%-decisive under both flags — so the
octagon buff deepens the **casualty exchange ratio** (toward Cannae ~11%-inflicting-~85%) without fixing
decisiveness there. Complete DG-6 = CEV friction (ED-MB-0016, built, gated OFF) + a **conjunctive
envelopment gate** + **brace-repel preservation** (both ratified-necessary, unbuilt).

## Prioritized roadmap

**P0 — outcome fidelity (unblocks trusting any staged result):**
- Ratify + default-on the CEV friction (ED-MB-0016) with the brace-repel exemption; build the conjunctive
  envelopment gate (center-holds × cavalry-sufficiency × terrain). *Ratified-necessary, unbuilt.*
- Add an **exchange-ratio band** to the gauge (the decisiveness gauge can't see the casualty-ratio change
  the octagon model introduces).

**P1 — the geometry backbone (fixes fidelity + the one architecture debt together):**
- Build `perimeter_targeting_geometry_v1`: perimeter extraction → target points + normals → approach-along-
  normal maneuver goal (retires `_envelop_goal` scripting-drift) → interception. Makes the wrap emergent.

**P2 — the three staging capabilities:**
- Concurrent multi-body engagement / cavalry rear-transit (Path B) → full-ring Cannae/Zama.
- Multi-line depth / reserve lines + line-relief (triplex acies) → Roman grid, reserve doctrine.
- Elephants/chariots + triggered lane-opening → Zama/Gaugamela.

**P3 — expressiveness + the live-path bridge:**
- Battle-state conditional triggers + army-plan object; wire the inert instructions (`lure` etc.); emergent
  fighting-withdrawal entry.
- **Stage G** (P-DEC-2, ratified): route `resolve_mass_battle` + `faction_action` onto the field engine and
  retire the integer engine — until this lands, *none* of the above is live in the game path.

**Nits:** puncture `int()`-floor (granularity leak); the reach 0.1/0.2/0.3 vs PP-290 meter-grounding
reconciliation; command-clamp(1–7) vs subunit-cap(11).

## What shipped this session
ED-MB-0017 (deployment/pathing + fast envelopment), ED-MB-0018 (octagon damage model), ED-MB-0019
(adversarial-review fixes: reaction-clock lifecycle, face-based multi-side shock, double-count kill, test
hardening, correct-env goldens). Geometry spec `perimeter_targeting_geometry_v1`. All gated `needs_jordan`
for the default-ON flip + the target-point model ratification.
