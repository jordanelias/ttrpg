# Scenario visualisation + dead-primitive census — findings

**Date:** 2026-07-29 · **Lane:** MB · **IDs:** ED-MB-0055 (field geometry), ED-MB-0056 (co-location),
ED-MB-0057 (dead-primitive census)

Built to four Jordan directives given in sequence: visualise the 20 scenarios against real
historical diagrams with machine vision; use *appropriate* troops and subunits; match the precedent
battles' **ratio, formation and subunit count**; and identify **all** built-but-unwired primitives,
because "if we have built a model that hasn't been superseded, it likely has a purpose that must be
evaluated."

---

## §1 — The tier-3 gauge cannot be compared to history at all

The honest gauge scores all 20 rows with **tier-3 single-subunit** bodies: 25 cells, 400 troops,
5 wide × 5 deep. Rendered (`png_gauge/`), an "envelopment wing" is **about two visible cells**.

**There is no geometry to compare.** H3 and H4 show two small blobs walking into each other and
merging; no wrap develops because there is no frontage to wrap with. This is not a rendering
artefact — it is the scale the bands were fitted at. It also supplies a mechanism for ED-MB-0039's
standing finding that "the engine has two envelopment regimes and nothing between, and the moderate
bands sit in an engine gap": **at 2 cells per wing, the moderate regime has nowhere to exist.**

## §2 — Rebuilt from the historical orders of battle

`scaled_orders_of_battle.py` takes the real combatant numbers, preserves the **ratio**, the
**formation** and the **subunit count**, and scales absolute size only as far as the engine's own
ceilings force (`MAX_TROOPS_PER_UNIT` 10,000 · `SUBUNIT_CAP` 11 · field 51×51).

| row | battle | historical | engine ratio | subunits |
|---|---|---|---|---|
| H3/H4/H10/H11 | **Cannae 216 BC** | Rome 86,000 : Carthage 50,000 | **1.72 : 1** ✓ | Rome 8 · Carthage 7 (3 centre + 2 African + 2 cavalry) |
| H5/H6 | **Leuctra 371 BC** | Thebes 7,000 : Sparta 10,500 | **0.67 : 1** ✓ | Thebes 5 (3 massed + 2 refused) · Sparta 6 |
| H7/H8 | **Zama 202 BC** | Rome 34,000 : Carthage 40,000 | **0.85 : 1** ✓ | 6 per side |
| R1 | **Agincourt 1415** | English 6,000 : French 18,000 | **0.33 : 1** ✓ | English 5 · French 6 |

**Deployment geometry (Jordan directive):** field **51×51** — odd, so a mirror matchup has a true
centre column instead of a half-cell bias — and the row budget divides exactly:

```
rows  0.. 4   free ground behind B     (5 — tactical pull-back room)
rows  5..17   side B, depth 13
rows 18..32   no-man's land            (15 — the approach)
rows 33..45   side A, depth 13
rows 46..50   free ground behind A     (5)                    5+13+15+13+5 = 51
```

⚠ **A measured correction to the engine's own spawn constants.** A formation extends *downward in
row index* from `starting_position` for **both** sides. The shipped rows (A=34, B=15) look 19 apart,
but B's own depth eats 14 of that — the true **front-face gap was 5**, so bodies were in contact
within a couple of ticks and no approach phase was ever visible. Front faces are now aligned per
side, so bodies of different depth (a thin crescent centre, a 4-deep cavalry wing) form **one**
battle line rather than a ragged one.

## §3 — Machine-vision read of the historical-scale renders

**H3 (Cannae) — the mechanism appears, and that is a real positive.** By t=12–24 the Roman mass has
deformed into a downward V while the Carthaginian wings close on **both** outer flanks. That is the
Cannae dynamic in outline, and the tier-3 battery could not produce it at all.

**Two defects visible in every multi-subunit row:**

1. **Formations shear and rotate pathologically.** Blocks pivot to 30–45° and interpenetrate
   (clearest in H6, where the Spartan line disintegrates into diagonal streaks by t=16). Infantry
   blocks do not pivot like that; a battle line degrades by breaking, not by shearing.
2. **Attrition at historical scale is far too low.** Cannae at t=24: **A 84.8% hp, B 93.0% hp** —
   7–15% losses. Leuctra: **A 91.7%, B 97.2%** — 3–8%. Cannae destroyed ~85% of a Roman army;
   Leuctra broke the Spartan right and killed a king. This is the D5 casualty-realism finding seen
   from the geometry side, and it is *worse* at scale, not better.

## §4 — Cell co-location, measured (ED-MB-0056) — and two retracted numbers

Jordan: *"cells are co-locating … the surface of battle between units is the boundary between their
cells — if we accept co-location, everything becomes a disaster codewise."*

Standing probe: `measure_colocation.py` (added 2026-07-29 — it was run ad-hoc first, which is how
the first two numbers below went out unchecked).

### §4.0 — ⚠ RETRACTIONS. Both earlier figures for this section were wrong, in opposite directions.

**Retracted #1 — "17.31% overlap rate".** That was *rounded-square co-location*: cell positions
`int(round(...))`-ed onto a lattice and counted as collisions when they shared a square. The field
path is CONTINUOUS; two bodies 0.6 apart round into a collision that never happened. It over-counts.

**Retracted #2 — "17.31% → 0.35% with exclusion ON".** This is the worse one. That measurement was
taken on an arm where the exclusion pass had **deadlocked the engine** (§4.2): cells were not
overlapping because they were not *moving*. It is the §0.1 confound — an uncontrolled measurement
banked because it was favourable — and it is exactly the failure mode §0.1 was written after. The
adversarial pass performed on it attacked the number and never the setup.

The honest metric is **body-box interpenetration** via `geometry.obb_overlap` (the engine's existing
single owner of "these two bodies overlap"), **thresholded by penetration depth**. Depth matters
because the lattice pitch is 1.0 and the bodies are 1.0 × 1.0, so neighbours sit *exactly on* the
touch boundary by construction and any sub-millimetre jitter flips the predicate. Measured at t=4:
of 16,847 overlapping same-subunit pairs the **median depth is 0.0029** lattice units and 88.5% are
under 0.1. A raw overlap boolean over-states the defect by roughly an order of magnitude.

### §4.1 — What the exclusion pass actually buys (deep overlap, depth ≥ 0.1)

140 snapshots (20 scenarios × 7 ticks), **79,226 cell placements**:

| class | EXCL=0 | EXCL=1 | change |
|---|---|---|---|
| same subunit | 43,068 | 44,531 | +3.4% |
| **different subunit, same side** | **13,477** | **6,932** | **−48.6%** |
| **opposing sides** | **875** | **224** | **−74.4%** |

On the class Jordan named — *cells between subunits mixing* — the pass halves it, and it cuts
cross-side interpenetration by three-quarters. It does **not** reach zero, for two identified
reasons: (a) the rule deliberately skips pairs already overlapping at tick start, because capping
them at s=0 freezes without separating, so an overlap once formed is never undone — nothing in the
engine separates overlapped bodies (`resolve_internal_collisions`, §5.1, is the only thing ever
built for it and is intra-subunit + grid-era); and (b) the whole solve is gated on
`toi_deferred = FIELD_MOVEMENT and enemy_cells_float`, so **formations with no enemy supplied
interpenetrate freely** — same-side exclusion inherits a cross-side precondition it has no reason to.

Spawn geometry is clean: at t=0, same-subunit 0, cross-side 0, inter-subunit 40. The overlap is
created in the first ~4 ticks, not inherited from deployment.

### §4.2 — The defect the pass shipped with, and its cost

The first form accepted a time-of-impact of `s == 0.0`, copying the cross-side loop. Safe there —
armies start apart, pre-existing contact is caught by `halted_cells`. Inverted for same-side pairs:
the formation lattice is *permanently tangent*, and no cell is ever halted against its own
neighbour. Measured (cell_field, 2 seeds): **568,785 of 1,213,199 same-side solves — 46.9% —
returned exactly 0.0**, against 9.84% cross-side. Halted cells fell 20,356 → 3,300; resolve calls
rose 1,482 → 11,934. Frozen formations never close, never contact, never halt, so every battle ran
to the turn cap.

That **8.05× tick inflation was the entire "8.2× slowdown"** (47s → 386s on unit_field) the pass was
blamed for — and it is why a swept-AABB broad phase written to fix the *cost* bought nothing
(386s → 370s): it culled pairs correctly inside a loop whose iteration count was the real defect.
The broad phase was removed with the fix. Runtime is now **1.41× baseline**. Guard:
`tests/valoria/test_cell_exclusion_no_deadlock.py`, mutation-verified (dropping the `s <= 0.0` skip
freezes the fixture dead — 0 cells moved between tick 1 and tick 6).

### §4.3 — The cost, measured with a control

The pass suppresses contact, and therefore casualties. Mean end-state HP across all 20 rows at t=24:
**0.8684 (OFF) → 0.8939 (ON)** — total attrition falls **19%**, on a casualty model §3 already flags
as far too low. H3 moved 84.8%/93.0% → 93.7%/97.9% hp; H5 91.7%/97.2% → 98.7%/96.1%. This is a real
trade-off, not a free win: geometric integrity is bought with engagement. It is shipped ON per the
standing "gate models ON" directive, with the cost recorded here rather than discovered later.

**Machine-vision read of the re-render (H5, Leuctra, the clearest case):** the massed blocks now
hold as **distinct parallel rectangles with visible gaps between them through t=24**, tilting
obliquely — which is the correct Leuctra behaviour. §3's "the Spartan line disintegrates into
diagonal streaks by t=16" is substantially fixed. H3 (Cannae) still shows the Roman mass fragmenting
into ribbons by t=8, so the shearing defect is reduced, not eliminated.

## §5 — Dead-primitive census (ED-MB-0057)

New tool: `tools/dead_primitive_census.py`. The existing instruments (`structure_audit`,
`build_apparatus_registry`, the vector audit) work at **module** granularity, and every dead thing
found here lives *inside a live, heavily-imported module* — which is why the same findings kept
being re-flagged by hand from 2026-05-29 onward without becoming a standing signal.

⚠ **The tool's own first result was wrong and was caught before quoting.** The first draft
subtracted the whole definition *file* when checking for external references, which reported every
method called as `self._foo(...)` from inside its own module as dead: **96 false positives**,
including `_node_advance`, `_kite_goal` and `_rekey_node_state` — all of which this same session had
just read live call sites for. Repaired (a `def` contributes no reference node, so no subtraction is
needed at all) before any number was reported.

**Repo-wide: 118 dead primitives** (73 functions + 45 constants) of 2,164 definitions, spanning
threadwork, factions, fieldwork, characters, settlements, world, social contest and the engine core.
Full data in `dead_primitive_census.json`.

### §5.1 — Mass battle, analysed for relevancy

| primitive | what it is | verdict |
|---|---|---|
| **`resolve_internal_collisions`** (`units.py:2061`) | discipline-gated formation hold: detects same-position cells, rolls d10 vs discipline — PASS reverts the trailing cell to its previous position, FAIL merges them with **averaged facing** (a broken formation then reads YELLOW/RED on the octagon more often) | **HIGHEST RELEVANCE — wire it.** This is the primitive built for exactly the defect §4 measures. Flagged "IMPLEMENTED BUT NOT INVOKED" since 2026-05-29 ("over-tuned battery, left available"). Its FAIL branch also writes `merged_cells`, itself dead. ⚠ It covers **intra**-subunit only — the 3,705 **inter**-subunit overlaps need a sibling that does not exist. |
| **`_reach_throttle`** (`units.py:129`) | reach-asymmetric closing budget: the longer-reach side is capped to a smaller share of this tick's closing motion, so it **plants its formation first** and the shorter-reach side must cover the rest | **HIGH RELEVANCE — evaluate.** ED-MB-0014 built the per-type reach data and then disclosed that "reach differentiation does NOT change symmetric standing melee — reach is a charge/brace lever, not a standing-melee one". This primitive is the missing piece that would make reach matter *in the approach*, which is where a pike advantage historically is. |
| `DAMAGE_TYPES`, `REACHES`, `WEIGHT_CLASSES` (`equipment/weapons.py`) | weapon taxonomy vocabularies | **RELEVANT — belongs to the ED-MB-0008 fork.** E3 records that the armour catalogue is "explicitly unwired; the live engine uses a free scalar `dr` defaulting to 1". These are the vocabulary that DR model would need. Do not delete while that fork is open. |
| `_cell_radius` (`core/contact.py:265`) | per-atom contact radius for the `FIELD_CONTACT` centroid bound | **Flag-dark, not dead.** Same disposition as `_find_contacts_field` (plan B3): `FIELD_CONTACT` is pinned 0 in every golden mode. |
| `_octagon_dmg_mod` (`orchestration.py:1023`) | subunit-scalar arc = the **mean** of the per-cell arcs | **SUPERSEDED — delete.** ED-MB-0040 made `_octagon_cell_mods` the single owner precisely because averaging smeared flank/rear damage across a body. This is the smear that fix removed. |
| `_SHAPE_BUILD` (`geometry.py:78`) | shape → builder dispatch table | **SUPERSEDED — delete.** A parallel owner to the live `CELL_PATTERN_FN`; a second dispatch table for one fact. |
| `debt_rows`, `TERMINAL_OK_FOR_VALUE` (`provenance.py`) | provenance reporting | **Delete with the module.** `provenance.py` has 0 importers and stale line numbers (plan B3 already files it). |
| `agg_power`, `agg_dr` (`units.py:2343-46`) | unit aggregates | **Low.** Their siblings `agg_discipline`/`agg_morale`/`agg_stamina` are live; these two are unused accessors with no behaviour attached. |
| `do_GET`, `do_POST`, `log_message` (`workbench/server.py`) | HTTP handlers | **FALSE POSITIVES.** `BaseHTTPRequestHandler` protocol overrides, dispatched by the stdlib. The census cannot see framework dispatch — recorded here so the next reader does not chase them. |

**The through-line:** the two highest-relevance dead primitives (`resolve_internal_collisions`,
`_reach_throttle`) are both **spatial-integrity** mechanics, and both were switched off for the same
stated reason — they perturbed a battery that was being tuned. §4's 17.31% overlap rate is what was
bought with that decision.

---

## §6 — Reproducing

```bash
export PER_CELL=1 FIELD_MOVEMENT=1 PC_NODE_COHESION=1
VIZ_SCALE=historical python3 audit/2026-07-29-scenario-visualization/render_scenarios.py --ticks 0,4,8,12,16,20,24
VIZ_SCALE=historical python3 audit/2026-07-29-scenario-visualization/render_png.py
python3 tools/dead_primitive_census.py --json census.json
```

`manifest_<scale>.json` carries a SHA-256 per scenario's geometry, so a re-run after an engine
change shows exactly which scenarios moved. The images are a regression surface, not decoration.
