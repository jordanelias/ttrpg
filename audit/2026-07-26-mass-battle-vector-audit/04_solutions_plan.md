# Mass battle — solutions, gaps, and plan (ED-MB-0043)

**Date:** 2026-07-26 · **Lane:** MB · **Input:** `02_weakness_register.md` (this run) + the four open
MB ledger items + the 2026-07-22 stress-test corpus.

> **Framing (Jordan, this session): we are still trying to solve mass battle _the system, for
> itself_.** That is a load-bearing constraint on this plan, not a preamble. The vector audit's
> findings are mostly about *legibility* — contracts, registries, typed params, port readiness. Those
> matter, but they are **downstream of a system that is still moving**, and this plan is ordered
> accordingly: the mechanics first, the plumbing after. §3 states plainly which audit findings I am
> recommending you **defer on purpose**, and why acting on them now would be actively harmful.

---

## §0 — Two corrections to the audit, made before anything is built on it

**C1 — §3 of the register overclaimed novelty. `scene_outcome.battle_concluded` is ED-MB-0010,
filed 2026-07-13, still open.** That entry already contains the same diagnosis in the same terms
("`scene_outcome` is only the emit FAMILY name, not a type_id — the SS8.5-verbatim provenance claim
is false") and the same remediation ("remove the `scene_outcome.battle_concluded` emit"). I read the
`needs_jordan` id list and did not read the bodies, so I re-derived a 13-day-old finding and
presented the mechanism as newly identified.

What is genuinely new is narrower and worth keeping: the item has been open long enough that **five
downstream surfaces now report it as a live defect** (structure_audit dangling-emit, vector Mode E,
vector Mode H, workbench card `wb-00aeffeb7f`, `INCOMPLETENESS.md:146`). That changes the action from
"make a call" to "unblock a call already made" — see A5.

**C2 — the audit's own priority ordering was wrong for the stated goal.** The register leads with the
empty contract as "top port blocker". Against *solving the system*, freezing a contract now is
premature at best (§3.1).

---

## §1 — What "solving the system for itself" currently blocks on

Five open mechanical problems, from the ledger and the stress-test corpus. These are the plan.

| # | Problem | State |
|---|---|---|
| **A1** | **Over-decisiveness (DG-6).** Melee attrition sums N independent per-soldier dice → CV self-averages as O(1/√N) (measured 0.89→0.06 for N=4→1024) → outcomes collapse to 100%/0% where history shows bands. | ED-MB-0016 **open, needs_jordan**. Root cause mathematically confirmed. A fix is researched and costed. |
| **A2** | **Cell-as-primitive, phases 3–4.** Jordan's directive ("the cell needs to be the primitive for morale, discipline, quality, stamina, rout, health, armour, facing, damage, troop count"). Morale is built; stamina/discipline/quality and hp/armour are not. | ED-MB-0042. **Flag OFF**, default flip retracted — the measurement was confounded. |
| **A3** | **Envelopment has two regimes and nothing between.** Pure-infantry parity envelopment is deployment-chaotic (±54pp side swing); combined-arms is stable and ~100%. The moderate 55–72% historical bands sit in an engine gap. | ED-MB-0039 **needs_jordan**, fork A/B posed. |
| **A4** | **R3 ranged-vs-ranged never engages.** 100% draws at 0.0% casualties both sides. Spawn distance 18, `VOLLEY_MAX_RANGE` 8, and `stance == "hold"` early-returns from all steering, so neither archer body closes and `volley_phase` never fires. | Candidate, characterised, fix proposed (now **ED-MB-0044**). |
| **A5** | **Rules-level contradictions in the MB canon.** Two live, mutually contradictory ranged/volley DR tables (~2× apart for the same armour band); an orphaned rule fragment citing a `stage5_clocks.md` that has never existed. | ED-MB-0008 / ED-MB-0009, both **open, needs_jordan** since 2026-07-13. |

---

## §2 — Solutions

### A0 (prerequisite, mechanical) — the scalar-write sweep, finished

**Two harness writers were deliberately left unswept** (`tests/sim/mass_battle/lanchester_signature.py`
~L126, `test_persubunit_stress.py` ~L191). Under `PC_CELL_MORALE=OFF` they are inert; under ON they
become silent no-ops. They were reverted on purpose because touching either file dragged ~100
pre-existing uncited constants into the anti-fabrication gate.

**This is not hygiene — it gates everything below.** `lanchester_signature.py` pins morale high
*specifically to disable rout* so the Lanchester exponent is measured on un-truncated battles. A
silent no-op there lets bodies rout mid-signature and measures the exponent on truncated battles.
**The Lanchester exponent is the statistic A1's entire root-cause analysis rests on.** So any
DG-6 measurement taken under cell morale, before this sweep, is corrupt by construction.

**Solution:** sweep both sites onto `set_morale`; expect to cite or ledger the ~100 constants as part
of the work. `tests/valoria/test_morale_write_sweep.py`'s `_CELL_OWNED` registry is already
field-parameterized, so the guard extends by adding a key.

**Verify:** the sweep test passes with both files in `_CELL_OWNED`; `lanchester_signature` produces
an unchanged exponent under OFF (control) and a *defensible* one under ON.

---

### A1 — Over-decisiveness: **test the primitive before adopting the patch**

This is the plan's central recommendation and it changes the standing proposal.

**What is already established.** `dg6_friction_resolution.md` correctly identifies that CLT
self-averaging is broken only by **correlation across combatants**, citing Kress (2024) that
correlation is *the formal lever*. It then implements the **simplest possible** correlation: one
shared per-battle, per-side multiplicative shock `M ~ LogNormal(0, σ²)`, drawn once per battle.

**The cost is disclosed and it is real:** σ=1.1 fixes the force-ratio curve against Dupuy but moves
the tactical gauge **6/20 → 4/20**. It buys strategic realism by degrading tactical realism.

**The objection.** A per-battle scalar shock is a *top-level* injection of variance. It is
phenomenological: it does not say *why* men's fates correlate, it asserts that they do and multiplies
by a number. CLAUDE.md §0 asks for the opposite — find the single-owner primitive and compose on it.

**And the primitive already exists, unmeasured.** ED-MB-0042 gives cells morale, a du Picq
break-point, and **break contagion across the 8-neighbourhood lattice**. That is *spatial correlation
of fate, generated mechanistically*: when a cell breaks, its neighbours are likelier to break, so
casualties arrive in correlated clumps rather than N independent draws. That is precisely the
correlation Kress names as the lever — but produced by a mechanism, at the tactical scale, from a
primitive Jordan has already directed us to build.

**Nobody has measured whether it is sufficient.** `PC_CELL_MORALE` is OFF, and its one measurement
was confounded and retracted.

**Solution — ordered, and the order is the point:**
1. Finish A0.
2. Re-measure cell morale honestly (the ED-MB-0042 step-2 that A0 blocks).
3. **With cell morale ON, re-measure DG-6's decisiveness and the CV-vs-N curve.** The specific
   question: does lattice contagion floor the coefficient of variation at a force-independent level,
   the way a shared shock does?
4. Only then decide on `PC_FRICTION_SIGMA`. Three outcomes, all informative:
   - Cell correlation suffices → **the CEV shock is not needed**, and its 2/20 gauge cost is avoided.
     One mechanism instead of two competing ones.
   - It helps but under-delivers → σ can be set *much lower*, and the gauge cost shrinks with it.
   - It does nothing → adopt the shock as researched, now with a control behind it.

**Falsifier (named, per §0.1 #3):** if under `PC_CELL_MORALE=ON` the CV-vs-N curve still decays as
O(1/√N) — i.e. contagion does not survive aggregation to the body — then this recommendation is wrong
and the shared shock is the right instrument. That measurement is the artifact; it does not exist yet.

**Cost:** one probe reusing the existing CV-vs-N harness. Cheap relative to a ~200k-token research
pass already spent, and it does not discard that work — it supplies the control the work lacks.

---

### A2 — Cell-primitive phases 3–4

Sequenced after A0/A1 deliberately: phase 3 retires `col_grid`, the third granularity between cell and
subunit, and A1's measurement is cleaner before that structural change than during it.

- **Phase 3** — stamina + discipline + quality per cell; retire `col_grid`.
- **Phase 4** — hp + armour per cell.
- Each inherits the write-sweep guard by adding one `_CELL_OWNED` key — the guard was built
  field-parameterized precisely for this.

**Deferred decisions this unblocks:** `PC_STOCHASTIC_ROUT`'s fate (measured inert at 35.6% vs 36.1%,
but under the same confound — retire-or-keep is undecidable until A0/A1), and `ROUT_CASCADE_FRAC`
(inert at 1.0 until phase 3 defines what a "section" is).

---

### A3 — Envelopment: the gap is the finding

Jordan's fork stands, unchanged by this audit; recorded here so the plan is complete:
- **(A)** reframe H3/H4 as combined-arms — bands move to ~75–100, loses the infantry/cavalry
  distinction.
- **(B, recommended by ED-MB-0039)** gated seal-failure/breakout variance → envelopment becomes a
  gradient rather than two regimes. Blast radius: lowers currently-passing C4/C7.

**One observation this audit adds:** (B) is the same shape as A1's recommendation — restore a
*gradient* by letting a local mechanism fail probabilistically, rather than by selecting between two
top-level regimes. If A1's cell-correlation measurement lands, (B) may share machinery with it rather
than needing its own. **Do not decide A3 before A1's measurement** — that ordering could collapse two
mechanisms into one.

---

### A4 — R3: the smallest real fix, and it needs no new magnitude

Ranged bodies never close because `hold` is interpreted as "hold the spawn coordinate". For a missile
body, `hold` should mean *hold the firing position*.

**Solution:** a ranged subunit whose nearest enemy lies beyond `VOLLEY_MAX_RANGE` closes into the band
**by ROLE**, reusing `_kite_goal` verbatim (too close → flee, too far → close, in band → hold). That
primitive is already live on the node path; it is merely gated on `'kite' in instructions`, which only
`mounted_archers` carry.

No new mechanism, no new constant, no R3 special case — it removes a special case. **This is the one
item here I would ship without a ruling**, and it is the natural first commit after A0.

**Verify:** R3 produces non-zero casualties and a non-draw distribution; R1 unchanged (it resolves
only because the infantry walks into range, a path this does not touch); goldens re-recorded with the
delta disclosed.

---

### A5 — Unblock the three 2026-07-13 provenance items

These are not new decisions. All three were diagnosed, with remediations proposed, and have sat open
for 13 days.

- **ED-MB-0010** — delete the `scene_outcome.battle_concluded` emit row. **One line.** Closes five
  downstream surfaces at once (§0 C1). The only wrinkle: `module_contracts.yaml` is nominally
  "regenerate, never hand-edit", so confirm the regeneration path or edit-and-document.
- **ED-MB-0008** — **rules-level, and the most consequential of the three**: two live DR tables ~2×
  apart for the same armour band. *Volley resolution is currently undefined* — an implementer cannot
  determine which governs. Jordan rules which is canonical, or scopes each to a distinct phase.
- **ED-MB-0009** — orphaned rule fragment citing a `stage5_clocks.md` that has never existed.
  Reconstruct or remove.

---

## §3 — Audit findings I recommend **deferring**, and why

Stated explicitly because the audit itself implied the opposite priority, and acting on it now would
work against solving the system.

### 3.1 — Do **not** populate the `mass_battle` contract yet

The finding is correct: `consumes: []` / `state: []`, zero upstream in all four ripple layers, and the
inputs demonstrably exist (`resolve_mass_battle` reads `faction.Mil`, `world.rng`; `faction_action`
writes territory ownership, `adjust('L',-10)`, `t.garrison`). The contract's `status: "extracted"` is
a false claim — its `sources` cite only Key-flow docs, which never described the resolver's data
inputs.

**But a contract is a freeze, and the system is still moving.** A1–A3 will change what state a battle
owns — that is the entire content of "the cell is the primitive for morale, discipline, quality,
stamina, rout, health, armour, facing, damage, troop count". Extracting a `state:` block now would
document the *pre-cell* model and create exactly the doc↔engine divergence §5 of the register
complains about, with a CI gate attached.

**Do this instead, now, at near-zero cost:** replace `status: "extracted"` with an honest status and a
`gap_notes:` entry recording that the I/O surface is real but unextracted pending the cell-primitive
programme. That converts a silent falsehood into a visible, dated deferral — and it is the one change
here that *helps* rather than hinders solving the system.

**Revisit when:** A2 phase 4 lands and the cell-owned state set stops changing.

### 3.2 — Do **not** build the typed MB params export yet

`tools/export_engine_params.py` + a CI round-trip check is the right end-state and the primitive
already exists (it does exactly this for `combat_engine_v1`, auto-collecting every uppercase
constant so a new one cannot be silently unexported). Pointing it at the MB engine would close the
"222 of 262 constants have no prose surface" finding mechanically.

**But it exports a *canonical oracle*, and the MB engine is not one yet** — A1 may delete
`PC_FRICTION_SIGMA` before it is ever used, A2 phase 3 retires `col_grid` and its constants, and the
ED-MB-0041 adversarial audit found only ~17 of ~92 magnitudes survive scrutiny. Exporting now would
confer typed-artifact authority on numbers that are known not to have earned it.

**Revisit when:** A1–A2 settle and the ED-MB-0041 magnitude backlog is worked.

### 3.3 — The two-trees fork: real, but **not obviously "unify"**

The audit's framing implied the split is straightforwardly a defect. Adversarially, it is not.

The wired `resolve_mass_battle` serves the **strategic** layer, which needs only
`{attacker_wins, degree, size_pct}` to move territory. The live engine runs a tick-level tactical
simulation with per-cell morale lattices. **"Two scales, two models" is a defensible architecture** —
the strategic layer arguably *should not* pay tactical simulation cost per conquest.

What is **not** defensible, and is the real finding, is that the split is **undeclared**: nothing
records which tree is the oracle, `tests/sim/README.md` actively asserts the live tree is frozen
run-output, and every code-layer instrument is configured to skip it.

**Three options, for Jordan:**
- **(i) Declare the split** — wired = strategic abstraction, live = tactical oracle; document it,
  correct `tests/sim/README.md`, add a CI note. **Cheapest; recommended if the abstraction is
  intended.**
- **(ii) Adapter** — `resolve_mass_battle` becomes a thin adapter over `resolve_battle(kind=…)`. Ends
  divergence, but changes campaign outcomes → golden re-record + campaign A/B.
- **(iii) Promote** — move the live tree to `systems/mass_battle/sim/`, retire the old, repoint
  `faction_action`. Cleanest end-state, largest blast radius; only sensible *after* (ii) proves the
  interfaces line up.

**Why this matters to solving the system, which is the part the audit undersold:** under (i) the
strategic campaign's emergent behaviour is produced by the *stale* model, so campaign-scale
conclusions drawn from `mc_v18` runs do not reflect any of A1–A4. Whichever option is chosen, that
caveat should be recorded now.

---

## §4 — All other gaps, tracked

**MB lane, in scope, low priority (hygiene):**
- `Mass Battle` vs `Mass Combat` alias tokens: divergent Μ-degree (0 vs 23) and different scale class
  (mechanic vs province). One classification is wrong.
- `pp = 0` — the patch register contains no case-insensitive match for the subsystem. MB work records
  to the editorial ledger and bypasses the patch register entirely. Decide whether that is intended
  (if so, say so; the audit's Mode-A pp-degree signal is then permanently uninformative for MB).
- 3 of 6 MB docs carry no `## Status:` line (`mass_battle_v30_index`, `military_layer_v30`,
  `military_layer_v30_index`) → currency unresolvable by the §4 method.
- The `CURRENT.md` head `mass_battle_v30.md` is `WORKING DESIGN`, not `CANONICAL`, while the
  integration doc beside it *is* canonical.
- `engine/params/mass_combat.md` header cites `designs/mass_combat/mass_battle_v30.md` — a path that
  has never existed — and is stamped `last_updated: 2026-04-03`.
- `systems.mass_battle.sim.massbattle ↔ units` import cycle; both are code cut-vertices.

**Out of lane (IN) — the dead `sim/` root class, filed not fixed:**
- `tools/ci_quantity_vocabulary_check.py:145` — **a CI gate** whose `--sim-root` default is the
  deleted tree; its sim-side scan surface is silently empty.
- `registers/mechanics_index.yaml` — 11 distinct dead `sim_module:` paths across 19 entries.
- `tools/audit_staleness.py:69`, `tools/observability/build_decisions.py:57`,
  `tools/workplan_status.py:71`, `tools/build_apparatus_registry.py:169` — dead `sim` prefixes.
- `tests/sim/mass_battle/test_persubunit_stress.py:17` — inserts `<repo>/sim` on `sys.path`.

**Instrument gaps this run exposed but did not close:**
- `ripple_audit`'s node namespace has no Key nodes — a Key cannot be the subject of a ripple query.
- Contract↔code correspondence remains **UNVERIFIED** (`structure_audit`'s disclosed black-hole);
  the join is not name-based, and `mass_battle` ↔ `massbattle` is one of the misses. Nothing in this
  run verified that the contract describes the code.
- `EXTRA_CODE_ROOTS` allowlists exactly one path. Other live code under `tests/` remains outside
  G_code, unmeasured and un-enumerated.
- Mode-D's 612 MB cascade sinks are unverified leads; the impact query saturates at 268/275 tokens
  and cannot discriminate at this cite density.

---

## §5 — Sequence

```
A0  scalar-write sweep (2 harness files + ~100 constants)     ← gates everything
     │
     ├── A4  R3 ranged-closes-by-role        [ship without ruling]
     │
     └── A2-step2  honest cell-morale re-measure
              │
              └── A1  DG-6 CV-vs-N under cell correlation      ← the decision this plan turns on
                       │
                       ├── PC_FRICTION_SIGMA: adopt / lower / drop
                       ├── A3  envelopment fork (may share machinery)
                       └── A2  phases 3–4  →  then revisit §3.1 contract, §3.2 typed export

parallel, no dependency:  A5 (ED-MB-0008/0009/0010)  ·  §4 hygiene  ·  §3.3 fork declaration
```

**Critical path is A0 → A2-step2 → A1.** Everything expensive hangs off one measurement that cannot
be taken until two harness files are swept.

---

## §6 — Adversarial pass

Run against the plan above, after drafting it. Recorded per CLAUDE.md §0.1 #3 — what the attack
*changed*, not that it happened.

**Attack 1 — "the cell-correlation idea is novel."** *Refuted, and the plan was corrected.* The DG-6
research already names correlation as the formal lever and cites Kress (2024) for it. My contribution
is **not** the mechanism; it is the observation that a *second, mechanistic* source of correlation is
already being built and has never been measured against this problem, and that the shared-shock
implementation carries a disclosed 2/20 gauge cost that a primitive-generated one might not. A1 was
rewritten to credit the existing research and to frame the proposal as *supplying a missing control*
rather than replacing the work.

**Attack 2 — "cell contagion will obviously fix self-averaging."** *Not established; the plan must not
assert it.* Contagion is local (8-neighbourhood); whether that correlation **survives aggregation to
body scale** is an empirical question. It could floor the CV at a level far too low to matter. A1 now
carries an explicit named falsifier — if CV-vs-N still decays as O(1/√N) under `PC_CELL_MORALE=ON`,
the recommendation is wrong and the shared shock is right. **The plan's central claim is a hypothesis
with a stated test, not a finding.**

**Attack 3 — "the two-trees split is a defect."** *Substantially weakened; §3.3 was rewritten.* Two
scales legitimately warranting two models is a normal architecture, and the strategic layer needs only
a win/degree. The defensible finding is the *undeclared* split and the actively-wrong README, not the
split itself. The audit register overstated this; §3.3 now leads with the option that keeps both.

**Attack 4 — "populate the contract; it's a port blocker."** *Rejected, and this reversed the audit's
top recommendation.* Under "solve the system for itself", freezing a `state:` block before the
cell-primitive programme lands would document the pre-cell model and attach a CI gate to it. Deferral
with an honest status is strictly better than a premature freeze. The audit's own §5 complaint —
doc↔engine divergence — is what premature extraction would manufacture.

**Attack 5 — "A4 (R3) is a bug."** *Held, but narrowed.* `hold` early-returning from steering is
plausibly **correct** for an explicit holding order; the defect is that missile bodies *default* to it
at a spawn distance beyond weapon range. The fix must therefore be **role-conditioned**, not a change
to `hold` semantics — otherwise it would break deliberate holding orders for melee. A4's wording was
tightened accordingly.

**Attack 6 — "A0 is hygiene, do it later."** *Rejected, and A0 was promoted to gating.* The unswept
`lanchester_signature.py` pins morale high *to disable rout*; a silent no-op there measures the
Lanchester exponent on truncated battles — and that exponent is what A1's entire root-cause rests on.
Deferring A0 does not delay the measurement, it **corrupts** it. This is the same defect class that
retracted the ED-MB-0042 flip.

**Attack 7 — "this plan is too long to be actionable."** *Partially conceded.* The actionable core is
three lines: **sweep two files → measure cell morale honestly → re-measure DG-6 under it.** Everything
else is either parallel-and-cheap (A5, hygiene) or explicitly deferred (§3). §5 exists so the critical
path is readable without the prose.

**What I could not attack, and flag as the plan's weakest joint:** I have not run any of A1–A4. Every
magnitude here is quoted from the ledger and the stress-test corpus, not re-measured — and ED-MB-0041
found that only ~17 of ~92 MB magnitudes survive scrutiny. **The quoted numbers in §1 and §2 inherit
that unreliability.** The plan's *ordering* does not depend on their precision; its *cost estimates*
do.
