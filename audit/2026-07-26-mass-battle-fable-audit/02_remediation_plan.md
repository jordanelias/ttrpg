# Mass battle — exhaustive remediation plan, all MB surfaces (ED-MB-0045)

**Date:** 2026-07-26 · **Lane:** MB · **Base:** `f4ab261` · **Scope:** every mass-battle surface (§1)
**Input:** `01_findings_register.md` (six-dimension Fable-5 audit) + ED-MB-0043 + the A17 scorecard.

---

## §0 — The frame

Jordan, on the first draft: *"it may not change the next battle, but it sure as heck should. make
identifying what's happening and preventing conflicts etc going forward."*

That correction is right and the first draft was wrong to file this as hygiene. Restated properly:

> **This plan changes the next battle, because three mechanisms are silently changing battles
> already — and the engine cannot currently tell you why any battle ended the way it did.**

**Silently distorting outcomes today (all verified, §1 of the register):**

| What | Effect on the battle, right now |
|---|---|
| Degree-boundary float compare, no epsilon guard | A 1-ulp error flips `Success`→`Partial`; at the universal `dr=1` default that is **3 damage → 0**. Exchanges are being zeroed. |
| `MAX_SUB_PHASES` bare `break` | Engagement groups past the 5th deal **zero damage that tick**. No log. Deep formations silently lose fights they should have had. |
| `check_drift` re-keys 1 of 10 cell maps | The moment cell morale is switched on: morale immortality plus phantom cell breaks that propagate to healthy neighbours. |
| Two engine trees | The campaign resolves battles on the **stale** model. None of the last month's work reaches the game. |
| `hp` vs cell-troops dual ledger | Two answers to "how many men are left", reconciled by convention. |
| Three stamina stores, two live drain laws | Fatigue means different things to the pool and to the sigma head. |

So the two goals, in Jordan's words:

> **G1 — Identify what's happening.** The engine must be able to explain a battle: who broke first,
> why, where the casualties came from, which mechanism decided it. Today it cannot. That is why two
> default flips were made on confounded measurements and retracted.
>
> **G2 — Prevent conflicts going forward.** Every fact gets **one owner**; every owner publishes an
> **invariant that fails loudly**. A declared rule with no enforcement is not a rule — it is the most
> common defect in this corpus.

---

## §1 — All mass-battle surfaces (the scope, exhaustively)

| # | Surface | Size | Audited? | Phase |
|---|---|---|---|---|
| 1 | `tests/sim/mass_battle/` — live engine | 28 files, 10,503 LOC | ✅ 6 dimensions | A,B,C,H |
| 2 | `systems/mass_battle/sim/` — stale twin, **wired to the campaign** | 5 files, 2,375 LOC | wiring only | G |
| 3 | `tests/valoria/test_*` — MB slice, CI-collected | 24 files | ✅ | A |
| 4 | `tests/sim/mass_battle/bat.py` + goldens | 4 digests | ✅ | A1 |
| 5 | `tests/sim/gauge_mb.py` — the 20-row gauge | 1 file | ✅ | E |
| 6 | `validators.py`, `provenance.py`, `lanchester_signature.py`, `test_persubunit_stress.py` | 4 harnesses | ✅ | A |
| 7 | `workbench/` — `server.py`, `trace.py`, `static/` | 3 | partial | **H** |
| 8 | `audit/2026-07-22-mass-battle-stress-test/` — 23 probes | 23 files | referenced | E |
| 9 | `systems/mass_battle/*.md` — 6 design docs | 6 | ✅ | F |
| 10 | `engine/params/mass_combat.md` | 1 | ✅ | F |
| 11 | `references/module_contracts.yaml` — `mass_battle` row | 1 row | ✅ | F |
| 12 | 12 registries carrying MB rows (`values_master`, `descriptor_registry`, `wiring_manifest`, `mechanics_index`, `numeric_bounds_report`, `silo_overlap_matrix`, …) | 12 | A17 only | F |
| 13 | `research/diagrams/mass_battle_formations/` | 2 scripts | no | F5 |

---

## §2 — PHASE A: make the instrument trustworthy (hard gate)

**Why absolutely first.** Phase B changes how cell state is stored. The only thing that can prove
such a refactor changed no behaviour is a byte-exact golden — and **the goldens for the configuration
the engine ships in are not checked by anything**. Refactoring the core data model without that is
how you get a third retracted flip.

| # | Item | Changes battles? | Size |
|---|---|---|---|
| **A1** | Wire `bat.py --check` at `FIELD_MOVEMENT=1` (both `PER_CELL` modes) into CI as its own ~4-min job. Today CI pins the field path OFF and the test says the field goldens are *"NOT checked here"*. | No — it *protects* them | M |
| **A2** | Epsilon-guard `compute_degree` — the **consumer** (`resolution.py:64-68`), not a fourth producer patch. | **YES — restores zeroed exchanges.** Goldens move; re-record deliberately with the delta published | S |
| **A3** | Make `MAX_SUB_PHASES` truncation loud (`orchestration.py:1431`): counter + trace event. Do not change the value. | No (reveals) — then **yes**, once we see how often it fires | S |
| **A4** | `assert checked >= N` in `test_front_takes_no_arc_penalty`; fix the `test_morale_write_sweep` fixture so it actually exercises the **own-morale** branch (`subunit.morale is None` in both params today, so the branch that flattens every cell to the mean has zero coverage). | No | S |
| **A5** | Finish the scalar-write sweep: `lanchester_signature.py:126`, `test_persubunit_stress.py:191`. Budget the ~100 pre-existing constants this drags into the anti-fabrication gate. | No | M |
| **A6** | Land `lanchester_signature` in CI **report-only** (it exits 1 today). Blocking flip waits on G2. | No | M |
| **A7** | Correct the record: retire ED-MB-0041's armour-inversion claim (refuted); re-scope ED-MB-0008 to docs-only; correct ED-MB-0038/0039's APEX diagnosis (dead code path). | No | S |

**Exit:** a byte-exact digest for the shipped configuration runs in CI, and no MB test can pass
vacuously.

---

## §3 — PHASE B: the CellTable — one owner, one invariant

**Not a per-cell object.** Array-of-structs is slower in a Monte-Carlo oracle and further from the
`PackedFloat32Array` layout the Godot port wants. Keep struct-of-arrays; add the missing owner.

```
CellTable                         # owns ALL per-cell state for one Subunit
  .ids                            # THE authoritative key set
  .troops .morale .facing .speed …# the ten maps, private
  .add(id) .remove(id) .rekey(m)  # the ONLY lifecycle operations
  .view(id)                       # per-cell accessor for ergonomics
  .check()                        # INVARIANT: every map's keys == .ids; Σtroops == troop_count
```

| # | Item | Fixes | Changes battles? | Size |
|---|---|---|---|---|
| **B1** | Introduce `CellTable`; move the ten maps behind it. Behaviour-preserving — preserve float operation order exactly, verified by A1's digests in both modes. | ownership #1 | No (by construction) | **L** |
| **B2** | `.check()` at phase boundaries under a debug flag + a mutation-verified guard (corrupt one map, assert `.check()` fails). | G2 | No | M |
| **B3** | Route `check_drift` through `.rekey()`. One call replaces ten forgotten ones. | S1.4 | **YES under cell morale** — removes morale immortality + phantom breaks | S |
| **B4** | Decide where fatigue lives, then retire `col_grid`. It is a **hybrid** — derived cache for density/depth, *authoritative* for stamina keyed to the **battlefield column**, so when men shift one file laterally their fatigue does not follow them. | ownership #4 | **YES** — fatigue stops teleporting | M |
| **B5** | Pre-register `_CELL_OWNED` keys for the phases-3/4 fields so they inherit the write guard by construction. | prevention | No | S |

**Why this supersedes ED-MB-0043's ordering.** Every new cell-owned field currently costs a new map,
a new bulk-write site, a new guard key, and a new forgotten re-key in `check_drift`. Ten fields have
paid that tax; Jordan's directive names six more. **Pay it once here instead of six more times.**

---

## §4 — PHASE C: collapse the remaining duplicate owners

| # | Duplicate | Action | Changes battles? |
|---|---|---|---|
| **C1** | Combat pool ×2 (`exchange.py:63-134`, `units.py:2339-2370`) — *"Mirrors EXACTLY"*, no test | Collapse to one; or add the mirror test the docstring implies | Only if they have already drifted — **which the test will tell us** |
| **C2** | Stamina ×3, two live drain laws | One owner (interacts with B4) | **YES** |
| **C3** | Facing/arc ×2 — both run every engagement, pin-perception gated differently | Retire legacy or unify gating; lift both out of the 652-line `resolve_engagements` so they are testable | **YES** |
| **C4** | Damage law ×2 — band model vs linear PP-233 in `pursuit_damage`; the band model cites a **nonexistent** `§A.4` while the nearest real canon is the linear form | Rule which is canon | **YES** — G6 |
| **C5** | Health ×2 (`hp` vs Σcells); `eff_size`/`cohesion` read a *different ledger depending on subunit count* | One ledger, other derived — fold into B1 | Removes a divergence class |
| **C6** | Dead/unwired: `provenance.py` (0 importers, all line numbers stale, yet cited as canon at `orchestration.py:1153,1166`), `merged_cells`/`resolve_internal_collisions` (0 call sites), `reform_check` (**canon-required**, permanently dark), `_find_contacts_field`, `PC_FACING_MODEL` family, `COMMAND_SIGMA_ENABLED` | ED-MB-0041's own rule: **wire or delete**, one line of disposition each | `reform_check`: **yes, if wired** |

---

## §5 — PHASE D: prevent conflicts going forward (G2 made mechanical)

Ownership fixes are point-in-time; these stop the class recurring.

| # | Item |
|---|---|
| **D1** | **Multi-owner scan.** A standing check that flags any quantity computed in >1 place in the MB tree. Seeded with the seven known duplicates so it starts green only once they are closed. |
| **D2** | **Configuration-liveness guard.** Reuse the one already shipped for `structure_audit` (ED-MB-0043) — assert every flag/root a harness pins actually exists, so a renamed flag fails loudly instead of silently pinning nothing. |
| **D3** | **Citation integrity for MB.** Three fabricated/unfindable citations found (`geometry.py:183` cites an octagon section with **zero** occurrences; `DAMAGE_BY_DEGREE` cites a nonexistent `§A.4`; `K_LINEAR` cites a doc that says values are sim-tuned). Extend the claim-provenance gate to resolve `[canonical: <doc> §<sec>]` tags and fail on a missing section. |
| **D4** | **Flag-pair coverage.** Coverage is diagonal-only (one flag flipped against default). Add pairwise coverage for the flags that interact — the `PC_CELL_*` family, `PER_CELL`×`FIELD_MOVEMENT`, octagon×cell-damage. |
| **D5** | **Golden-drift disclosure.** Any commit that re-records a digest must state which mechanism moved it. Enforced by requiring a `[goldens: <reason>]` line when `EXPECTED` changes. |

---

## §6 — PHASE E: gauge and probe integrity

| # | Item |
|---|---|
| **E1** | Resolve the two **incompatible 2:1 targets**: `lanchester_signature`'s own check demands ≥65% and measures 100%; `dg6` adopts ~70% as the historical target. One must be repudiated (G2). |
| **E2** | `triplex acies` is misapplied — a **depth** arrangement cited for a lateral tripartition — and it is load-bearing: `n_cmd` is the only free parameter that lands H3 in band, and it was chosen *after* measuring the 0/53/95 sweep. Re-ground or re-label the anchor. |
| **E3** | Re-verify the 23 probes against the corrections in §5 of the register — several were written against the APEX hypothesis that names a dead code path. |
| **E4** | Publish which gauge rows are **validation** and which are **calibration**. ~20 constants are self-tagged `CALIBRATED-DEBT`; the gauge cannot both set and check them. |

---

## §7 — PHASE F: docs, params, contract, registries

| # | Item |
|---|---|
| **F1** | 3 of 6 MB docs carry **no `## Status:` line**; the `CURRENT.md` head is `WORKING DESIGN`, not `CANONICAL`, while the integration doc beside it *is* canonical. |
| **F2** | `engine/params/mass_combat.md` describes a **7-phase d10 dice game**; the engine runs continuous ticks with a per-cell morale lattice and octagon damage multipliers. Its header cites a path that has never existed and it is stamped `2026-04-03`. Reconcile or mark superseded. |
| **F3** | The `mass_battle` contract declares `consumes: []`, `state: []` — **deliberately deferred** (ED-MB-0043 §3.1) until B/C settle what state a battle owns. Ship an honest `status`/`gap_notes` now; populate after Phase C. |
| **F4** | Delete the `scene_outcome.battle_concluded` emit row (= **ED-MB-0010**, open since 2026-07-13; a family name, not a Key). One line, closes five downstream surfaces. |
| **F5** | 12 registries carry MB rows; `values_master` is quarantined-stale and indexes a nonexistent file. Reconcile the MB slice only. |
| **F6** | Typed params: point `tools/export_engine_params.py` (already working, CI round-trip-checked) at MB's `config.py` — **gated** on C4/E1, since ED-MB-0041 found only ~17 of ~92 magnitudes survive scrutiny. |

---

## §8 — PHASE H: identify what's happening (G1) — the battle must explain itself

**This is the phase that most directly answers Jordan's steer, and it is the one with no prior
tracking item.** The seed exists: `workbench/trace.py` has `start_trace`/`get_trace`.

Today, asked *"why did this battle go this way?"*, the engine can answer only with a win flag and
casualty totals. Every diagnosis in this audit and the last required writing a bespoke probe — 23 of
them now live in the stress-test folder. **That cost is the finding.**

| # | Item | Answers |
|---|---|---|
| **H1** | **Per-phase casualty attribution.** Tag every casualty with its source (melee / volley / pursuit / freed-attacker / cellwise) and the tick. Directly settles the §4.2 finding — that the engine kills the loser *then* breaks him while history breaks *then* kills — which currently cannot be measured at all. | where losses come from |
| **H2** | **Decision log.** Record why each subunit broke: which threshold, what its casualty fraction was, what its morale was, whether contagion or its own break-point fired. | who broke first, and why |
| **H3** | **Mechanism attribution.** Per battle, report which mechanisms were live and how much each moved the result (octagon multiplier, Lanchester term, charge shock, rout cascade). Turns "the engine is subunit-emergent, not cell-emergent" from an inference into a measurement. | what decided it |
| **H4** | **Invariant reporting.** Surface `CellTable.check()` (B2), hp-vs-cells agreement, and the A3 truncation counter as first-class battle output, not debug prints. | conflicts, as they happen |
| **H5** | **Promote the workbench.** `trace.py`/`server.py` are unwired from CI and undocumented. Make the trace the standard diagnostic artifact so the next question does not need a 24th bespoke probe. | all of the above |

**H is what makes the design work cheaper forever.** Every future balance question — the DG-6
re-measure, the envelopment fork, phases 3–4 — currently starts by building an instrument. After H it
starts by reading one.

---

## §9 — PHASE G: decisions that are not engineering

No engineering below should assume an answer.

1. **The two engine trees** — declare / adapt / promote. Under "declare", campaign-scale conclusions
   come from the **stale** model.
2. **The two incompatible 2:1 validation targets** (E1/A6).
3. **CEV naming and σ** — Dupuy's CEV is a *persistent per-force fitted residual*, not an i.i.d.
   per-battle draw. Rename to Clausewitz/Beyerchen friction; expect σ to shrink as real mechanisms
   land or it double-counts them.
4. **`triplex acies`** (E2).
5. **The emergence verdict** — the cell is not yet load-bearing; envelopment is builder-authored, and
   the repo's own sweep found H4 passes with envelopment pathing **OFF**.
6. **Which damage law is canon** (C4).
7. **Where fatigue lives** (B4).
8. **The absent mechanisms** — terrain, pursuit in the measured mode, the general as an entity,
   surrender/prisoners, ammunition, weather. These are *design*, not remediation, and each would
   change battles far more than anything above.

---

## §10 — Sequencing

```
PHASE A  trustworthy instrument ───────────────────► HARD GATE
   A1 field goldens in CI   (B1 has no safety net without it)
   A2 degree guard [CHANGES BATTLES]   A3 loud truncation
   A4 vacuous tests   A5 write sweep   A6 law harness report-only   A7 record
        │
        ├──────────────► PHASE H  observability ── start in parallel, H1 early:
        │                  it is how we SEE whether A2/B3/B4 changed what we think
        ▼
PHASE B  CellTable ────────────────────────────────► unblocks the directive
   B1 owner → B2 invariant → B3 check_drift [CHANGES BATTLES] → B4 fatigue(G7) → B5
        │
        ├──► PHASE C  collapse duplicates (C1,C2,C5 need B; C3,C6 independent)
        │
        └──► ED-MB-0043's A1: re-measure DG-6 under cell correlation
                 — now on a trustworthy instrument, with H1 to attribute the result

PHASE D  conflict prevention ── after each ownership fix it guards
PHASE E  gauge integrity ────── needs G2
PHASE F  docs/params/contract ─ F3 after C; F4 now (1 line)
PHASE G  Jordan forks ───────── gates A6, B4, C4, E1, E2, F6
```

**Critical path: A1 → B1 → B3.** Everything expensive hangs off a safety net that does not exist yet.
**Cheapest real win: F4** — one line, closes five surfaces, already diagnosed 13 days ago.

---

## §11 — Guard catalogue (G2 applied to this plan itself)

Per CLAUDE.md §0.1 #5 — *if you cannot write the guard, you have not understood the pattern.* Each is
mutation-verified: revert the fix, watch the guard fail.

| Fix | Guard |
|---|---|
| A1 | The CI job itself |
| A2 | Test feeding `net = ob − 1e-16`, asserting `Success` |
| A3 | Test asserting the counter increments on truncation |
| A4 | `assert checked >= N`; fixture asserts `subunit.morale is not None` |
| B1–B3 | `CellTable.check()` + a test that corrupts one map and asserts failure |
| B5 | `_CELL_OWNED` parameterised registry (already built for this) |
| C1 | Mirror-equality test, single-subunit case |
| C6 | Zero-importer check via `build_apparatus_registry` |
| D1–D5 | Each *is* a guard |
| H4 | Invariant output asserted non-silent in a smoke test |

---

## §12 — Risks

1. **B1 is a core data-model refactor of a 10.5k-LOC engine.** Mitigated by A1. If the field goldens
   prove unstable *before* B1 starts, that is itself a finding and B1 stops.
2. **A2 and B3 move goldens deliberately.** Correct — the current goldens encode bugs — but each
   needs a published delta (D5), never a quiet update.
3. **A5 drags ~100 uncited constants into a blocking gate.** Known; budget the ledger work or the
   sweep stalls again as it did last time.
4. **H can sprawl.** Cap it: H1 and H4 are the load-bearing pair. H2/H3/H5 are valuable but optional
   until a specific question needs them.
5. **Phase C may reveal the duplicates have already drifted.** Then some current gauge results were
   produced by whichever copy happened to be called. That would be a finding, not a setback.

---

## §13 — What this plan does not do

- It does not touch the ~26,000 LOC of **other** subsystems. Their ownership state is unmeasured, and
  the parallel-dict counts I gathered are **not** evidence of the same defect (`autoload`'s 19 dicts
  are a registry doing its job). Auditing them is separate work.
- It does not resolve any §9 fork.
- It does not add terrain, pursuit, the general as an entity, surrender, ammunition or weather —
  §9.8. Those change battles more than everything above combined, and they are design, not repair.
- It does not change any historical band or magnitude. Where it changes outcomes (A2, B3, B4, C2,
  C3), it does so by **removing a defect**, and each such change is measured and published, never
  silent.
