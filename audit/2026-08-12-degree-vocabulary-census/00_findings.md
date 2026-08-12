# Degree-of-success vocabulary — behavioural equivalence census

## Status: REPORT — RATIFIES NOTHING. No head moved, no ladder changed, no `## Status:` flipped.
## Date: 2026-08-12 · Lane: IN (cross-cutting) · ED-IN-0170
## Instrument: `degree_census.py` (this folder) — re-runnable, imports the live functions

> **Why this exists.** `audit/2026-08-11-divergence-audit` §3.1 reports **16 producers, 6
> vocabularies, 5 incompatible Overwhelming formulas**, and the merged plan holds ruling **#0**
> (which `net`/`ob` convention is canonical) as the gate on the entire degree family. That framing
> makes the decision look like sixteen decisions. **It is seven, and four of the seven are not
> really in dispute.** Nothing had measured the difference, so the ruling had been priced by
> counting code sites rather than by counting behaviours.

---

## 1. The headline

**11 code sites → 8 distinct ladders → 7 behavioural equivalence classes.**

A class is a set of ladders whose **band surface is identical** over the evaluated domain once
spelling is normalised to an ordinal (Failure < Partial < Success < Overwhelming). Ladders in one
class are a **rename**. Ladders in different classes are a **design disagreement**.

| # | class | sites | disposition |
|---|---|---|---|
| 1 | `dice_engine:94` — canon | 1 | the reference |
| 2 | additive `ob+3` | **4** (`threadwork/operations:134` + 3 inline copies) | one decision, four sites |
| 3 | `threadwork/opposing:87` — 3 bands, `'Meets'` | 1 | no Overwhelming band at all |
| 4 | `faction_action:97` — ob pre-subtracted | 1 | **the sharpest divergence** |
| 5 | mass battle — `resolution:89` + `massbattle:640` | 2 | **behaviourally identical to each other** |
| 6 | `combat/core:57` — continuous, −0.5 | 1 | deliberate continuity correction |
| 7 | `valoria_dice:45` — skill-local fork | 1 | `Ob==10` special case, no `>=3` floor |

**Four of the audit's 16 are not ladders at all.** `echo_transport:187`,
`parliamentary_bridge:100` and `scene_dispatch:260`/`:334` are **translators** — they map an
already-decided outcome into a display vocabulary. They carry no band boundaries, so they are pure
spelling and need no ruling.

---

## 2. What is mechanically mergeable today (no ruling required)

- **Class 2's four sites collapse to one.** `mass_seizure:264`, `collective:166` and `knots:226`
  are inline re-typings of `threadwork/operations:134`. Identical surfaces. Delta = none.
- **Class 5's two ladders collapse to one.** `tests/sim/mass_battle/resolution.py:89` (with
  `_DEGREE_EPS = 1e-9`) and `systems/mass_battle/sim/massbattle.py:640` (without) produce
  **identical bands on every one of the 1,490 cells**. ⚠ **This does NOT refute the epsilon.**
  ED-MB-0051 justifies it as ulp-recovery from *accumulated* float error; a quarter-step grid does
  not produce accumulated error, so this census is structurally unable to observe the case it was
  written for. The correct reading is "the epsilon does not change the band surface", not "the
  epsilon is unnecessary".
- **Class 5 vs canon differ in 9 of 1,490 cells (0.6%)**, all at **ob ≥ 20** — the canon Ob-20
  exception, which the mass-battle ladders do not implement. Everywhere else they are identical.
  Whether mass battle should carry the Ob-20 exception is a small, well-bounded question, not a
  convention war.
- **The four cross-scale translators** are renames.

**That is 8 of the 11 sites reachable without a design ruling.**

---

## 3. What genuinely needs your ruling — and how much each costs

Ranked by how much of the band surface actually moves:

| divergence | cells differing | first divergence |
|---|---|---|
| canon vs `faction_action:97` | **670/1490 (45.0%)** | net=0.25 ob=1 → Partial vs Failure |
| canon vs `threadwork/opposing:87` | 560/1490 (37.6%) | net=0.25 ob=1 → Partial vs Failure |
| canon vs additive `ob+3` | 228/1490 (15.3%) | net=3 ob=1 → Overwhelming vs Success |
| canon vs `combat/core:57` | 50/890 frac (5.6%) | net=0.25 ob=1 → Failure vs Partial |
| canon vs `valoria_dice:45` | 20/600 int (3.3%) | net=2 ob=1 → Success vs Overwhelming |
| canon vs mass battle | **9/1490 (0.6%)** | net=1 ob=20 (Ob-20 exception only) |

**`faction_action` is the one to rule first.** It disagrees with canon on nearly half the surface,
and the reason is structural rather than a threshold choice: its `_degree` takes **only `net`**,
with `ob` already subtracted at the call site (`:520`, `net = _successes(pool, rng) - ob`). Its
`net == 0 → Partial` branch is the `s == ob` dead zone that #304 flagged as item #1 — this census
prices it at 45% of the band surface, not an edge case.

**`combat/core:57` should probably NOT be merged.** Its −0.5 offsets are a documented continuity
correction (ER-2) that exists precisely because a continuous net approximates a sum of integer
effects. Merging it into the discrete canon would re-introduce the 5–9pp low read the correction
was written to fix.

---

## 4. A methodological finding, recorded because it changed the answer

**The first run of this instrument reported 6 classes, and it was wrong.** On the integer domain
alone, `combat/core:57` groups with the two mass-battle ladders — because a **−0.5 continuity
correction is invisible at integer nets**, which is the one domain the continuous resolver is never
actually evaluated on. Adding quarter-step nets split the class: 5.6% divergence, first at
net=0.25.

A class computed on the wrong domain is a merge recommendation that silently changes behaviour —
the exact defect this census exists to prevent, reproduced by the census on its own first run. The
instrument now evaluates both domains and **prints a warning when they disagree**.

The functions are **imported, not transcribed**. Re-typing each ladder would have measured the copy
and agreed with itself (the ED-IN-0132 F1 defect). Three ladders initially failed to import and
were reported as EXCLUDED rather than reconstructed; all three were then fixed properly (a path
entry, a package import to resolve a cycle, and a wrong function name) so the census covers 8 of 8.

---

## 5. What this does NOT measure

- **Reachability.** Every cell is weighted equally. A divergence at ob=20 may never occur in a
  seeded campaign while one at ob=1 occurs constantly. Ranking by *fired frequency* needs the
  behavioural instruments (plan T4: `flag_ablation`, `harness`, `reachability_sweep`), which remain
  unrun.
- **`sigma_leverage:284`** is excluded by design — it is pool-aware, so it is not a function of
  `(net, ob)` and shares no domain with the others. It is also the most-pinned ladder in the repo
  (a 1,758-row golden table), which makes it the most expensive to change and the least likely
  merge target.
- **The `net`/`ob` naming question itself.** This census measures *band surfaces*. Whether the
  parameter should be called `net` or something else is a nomenclature question, and
  `proposals/canonical_nomenclature_v1.md` already owns it.

---

## 6. Recommended sequence

1. **Rule `faction_action` (#0/#1).** Largest surface, structural cause, and it gates #2.
2. **Merge the free ones** — Class 2's four sites → one; Class 5's two → one; the four translators
   → the owner's vocabulary. All delta-none, each with an expected-delta test.
3. **Decide the Ob-20 exception for mass battle** — 9 cells, well bounded.
4. **Leave `combat/core:57` alone** unless ER-2 is being revisited.
5. **Run T4** before ruling anything that depends on how often a band actually fires.
