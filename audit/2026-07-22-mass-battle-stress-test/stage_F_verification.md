# Spatial-model v2 — Stage F verification, digest re-record, historical revalidation

**Status: DONE 2026-07-22 (ED-MB-0015).** Full verification pass over Stages D+E (the balance-moving
core of the v2 field-engine upgrade), per `spatial_model_v2_plan.md` §3 Stage F + §9 P-DEC-4. No new
mechanics — this stage re-runs every invariant gate, re-records the field goldens, and re-validates the
history-grounded gauge under the OBB geometry.

## 1. Invariants (I1–I7) — all hold

| # | invariant | result | evidence |
|---|---|---|---|
| **I1** | conservation (Σ cell_troops == hp) | **hold** | 300-battle randomized field fuzz (varied shape/type/speed), **0 violations**; + `test_frontage_conservation.py` / `test_reach_weapon_class.py` seeded |
| **I2** | determinism (same seed ⇒ identical) | **hold** | stress harness S5 `determinism: PASS`; per-stage determinism tests |
| **I3** | no integer on the live position/contact path | **hold** | the last frontage integer removed (Stage D); the only residual `int(round)` on the live `_find_contacts_standoff` path is the **formation-lattice cell-identity** recording (a discrete troop-block label feeding the casualty/density substrate — I3's defensible-quantization carve-out, not position math). The `int(round)` at `core/contact.py:337-353` is in `_find_contacts_field`, a **non-live** path (FIELD_CONTACT on + FIELD_MOVEMENT off), not the default field path. |
| **I4** | grid oracle byte-exact | **hold** | `test_mass_battle_byte_exact.py` green (grid `unit`/`cell` modes); both D and E are `FIELD_MOVEMENT`-gated |
| **I5** | no silent balance tuning | **hold** | every shift A/B'd + disclosed in ED-MB-0013/0014; field goldens re-recorded here (§2); **no balance constant tuned** |
| **I6** | mirror symmetry (order-cancelled) | **hold** | stress harness S5 `mirror symmetry: PASS  A-favoured 1  B-favoured 1  draw 46  |skew|=0/48` (exact) |
| **I7** | reach ⇒ facing (facing-away → no reach) | **hold** | `_effective_reach` FOV gate; `test_reach_weapon_class.py::test_facing_away_gets_no_reach` |

## 2. Field-golden re-record (grid unchanged = I4)

The field digests moved (D's continuous frontage + E's per-type reach both shift field behaviour);
re-recorded in `tests/sim/mass_battle/bat.py`:

| mode | new digest | verified |
|---|---|---|
| `unit_field` | `2da5183aeeedfadaf3acba1d72c2868b7b7d3a83a832df6e66d4f9d964f1bc38` | `bat.py --check` → `[BYTE-EXACT OK]` |
| `cell_field` | `5f5db965f2712ae1b2b4fc614c827b6cb74a98fab4b4e9dfb410e5010ee5c273` | recorded from a clean run |

Grid modes (`unit`/`cell`) **unchanged** — the CI byte-exact gate stays green.

## 3. Stress harness S0–S5 (`audit/…/run.py 40`) — all green

- **S0 wiring census:** all 30 mechanics WIRED; *"WIRED mechanics whose gate is OFF under field defaults: none."*
- **S1 aggregate fuzz (n=40):** ENGINE FAILURES: **0**.
- **S2 isolation validators:** V-REFORM PASS.
- **S3 per-flag A/B:** every expected gate WIRED — including `PC_BRACE_ENABLED`, `PC_CHARGE_RECOIL`,
  `PC_RECOIL_FRONTAL` on `charge_vs_brace` (the gates Stage E's reach-advantage rides on); the
  documented inert-by-scenario gates (`MORALE_FIX`/mirror, `PC_BRACE_SETUP_DELAY`, `PC_WHEEL`) inert as
  before.
- **S4 off-by-default activation:** all SAFE (`PC_FACING_MODEL`, `FIELD_CONTACT`, `REFORM_CHECK_ENABLED`,
  all-three-on) — viol=0.
- **S5 controls:** determinism PASS; mirror symmetry PASS (|skew|=0/48).

## 4. Standing gates re-confirmed

- **Lanchester melee exponent:** p=2.50 (A/B: **unchanged** before/after the geometry work — the
  pre-existing DG-6 pool-variance artifact is frontage/reach-independent).
- **depth-2 experiment (Column vs Line, n=20):** **byte-identical** before/after D+E (deep_wins=0,
  deep_hp=0.8953, wide_hp=0.9123) — a close non-degenerate loss (89.5% retained), NOT a collapse. The
  "must preserve" gate holds exactly; the 0-wins is a pre-existing DG-6 width-vs-depth baseline.
- **full `tests/valoria`:** 447 passed / 60 skipped / 1 xpassed (byte-exact confirmed separately).

## 5. Historical revalidation (P-DEC-4) — gauge under the OBB geometry

`tests/sim/gauge_mb.py` (history-grounded bands, `references/historical/mass_battle_gauge_grounding.md`)
run against the live v2 engine, A/B'd against the pre-D baseline (isolated git worktree at `076f239`,
which already carries Stages A–C):

- **pre-D baseline (A–C): multi = 10/20**
- **v2 (A–E, OBB): multi = 6/20** (single = 2/20 for both, a tick-cap artifact per the harness docstring)

**Reading (honest, material):** Stages D+E **moved the gauge down 4 rows** (10→6/20). This is an
*authorized* re-baseline (P-DEC-4 explicitly expected the frontage/reach change to move the gauge and
authorised re-recording), but it is a directional shift, not a wash — the more physically honest OBB
geometry produces outcomes that fall outside **more** of the current history bands. Two readings are
possible and P-DEC-4 asks us to distinguish them: (a) the honest geometry exposes engine divergences the
coarser circle model masked, or (b) the bands themselves need re-grounding under the honest geometry.
The dominant failure class in BOTH baseline and v2 is the **DG-6 over-decisiveness** — envelopment /
force-ratio rows resolve to 100%/0% (`H2–H8`, `C1`, `C4` WIN-OUT) where history shows bands. Confirmed
mechanism: the melee pool sums `N` independent per-soldier dice, so its coefficient of variation
collapses as ~1/√N (measured: 0.89→0.49→0.25→0.12→0.06 for N=4→1024) and the pool scales linearly with
troop count → `compute_degree` returns a near-deterministic tier from the force ratio → certain, not
banded, outcomes. Note the Stage E win: **C2 and C6 (Cav vs BRACED Line) both REPEL** (attacker ≈5%,
band 0–30) — the anti-cavalry brace/reach mechanic is consistent with the historical repel bands.

**This is being RESOLVED, not deferred** (Jordan directive 2026-07-22: "validate emergent results
top-down from historical precedent; extend code as required to resolve standing issues using academic
research, military theory, mathematics, historical precedent"). The DG-6 grounded resolution — restoring
scale-invariant outcome variance so a large advantage produces a *decisive-but-uncertain* (banded)
result rather than a certain one — is a follow-on work item (its own ED-MB) built on research grounding
(stochastic Lanchester / breakpoint models; Clausewitzian friction / du Picq morale; Sabin's quantified
*Lost Battles* decisiveness bands). The field goldens re-recorded in §2 are correct for the A–E state
and will re-record again when the DG-6 resolution lands (goldens move with every disclosed balance
change).

## 6. Final adversarial backwards-analysis

Independent re-trace (outcome → inputs), per `backwards_analysis.md` methodology:
- **Position/contact math on the live field path is float end-to-end** — Euclidean motion (`_node_advance`,
  Stage C analytic TOI), OBB contact (`obb_front_reach_overlap`), continuous frontage
  (`engaged_frontage`), per-type float reach. The only integers on that path are the **formation-lattice
  cell identities** (discrete troop blocks) feeding the casualty/density substrate — the defensible
  quantization I3 explicitly scopes out, not position/contact arithmetic.
- I1–I7 all re-established above. No balance constant tuned across D/E/F.

**Deferred (flagged, not silently dropped):**
- **PP-290 reach-scale reconciliation** — the P-DEC-1 0.1/0.2/0.3 scale is finer than PP-290's 0.5/1.5
  meter-grounding; a Jordan/canon reconciliation is owed (Stage E note).
- **P-DEC-3 cavalry density cap** (< infantry) — deferred to keep the reach A/B clean.
- **DG-6** (over-decisiveness / super-linear resolution) — the dominant remaining gauge gap, **now IN
  PROGRESS as a research-grounded resolution** (Jordan directive 2026-07-22), tracked as its own ED-MB
  follow-on. Root cause confirmed (§5): 1/√N variance collapse of the pooled-dice melee resolution.
