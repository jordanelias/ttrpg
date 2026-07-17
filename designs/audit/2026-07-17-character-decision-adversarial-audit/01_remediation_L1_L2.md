<!-- STATUS: PROPOSED — remediation design for audit findings L1, L2. Magnitudes [SEED]. -->
<!-- AUTHORITY: ED-IN-0073 umbrella; per-lane candidates C-1 (SC), C-2 (SC+IN). File on ruling. -->

# Remediation Design — L1 (armature degeneracy) & L2 (conviction↔contest disconnection)

## Status: PROPOSED
## Date: 2026-07-17
## Parent: `00_findings.md`

These two fixes compose. L2 makes the contest armature a *function of the NPC's Convictions* (so
Convictions actually reach the social contest); L1 makes that armature *discriminate between styles*
(so the resulting vector does more than a single-axis lookup). Applied together, an NPC's Conviction
vector produces a judge whose style-susceptibility is both grounded and genuinely multi-dimensional.
All new magnitudes are `[SEED]` pending the calibration harness in `02_`; the **structure** is
grounded and cited per row.

---

## §1 The two defects, precisely

**L1.** `armature.py:228-235` `_row(primary)` → `{ax: 1.0 if ax==primary else 0.15}`. Every row is
`0.15·𝟙 + 0.85·e_primary`. Hence `alignment(style,pos) = 0.85·pos[primary(style)] + 0.15·S`, and
`alignment(s1)−alignment(s2) = 0.85·(pos[p1]−pos[p2])` — the `0.15·S` cancels, so style comparison
sees **one axis only**. (Re-derived; a balanced judge ties all styles at 0.725.)

**L2.** `armature.py`'s `ArmaturePosition{evidence,consequence,authority,insinuation}` is authored by
hand (`agon_harness.py:132`) and never computed from `personal_convictions`. The substrate's
`armature_position{hierarchical,sacred,instrumental,traditional}` (`keys.py:56`) is a *different*
space. Nothing bridges them, so Convictions never influence a contest verdict.

---

## §2 Fix L1 — a genre-grounded, non-degenerate `STYLE_AXIS`

**Grounding.** The four Contest Styles are not four independent atoms; `npc_behavior_v30.md §1.3` +
`complete_systems_reference.md §1.2` define each as a point in a **2-D genre plane** — the product of
`{Memory, Projection}` × `{Revealing, Obscuring}`:

| Style / axis | Genre coordinates |
|---|---|
| Evidence (Precedent) | Memory + Revealing |
| Consequence (Vision) | Projection + Revealing |
| Authority (Suppression) | Memory + Obscuring |
| Insinuation | Projection + Obscuring |

Two styles are *kin* to the degree they share genre coordinates. Replace the uniform `0.15` off-axis
weight with a **shared-genre-dimension** weight: primary `1.0`; shares exactly one genre dimension
`0.5` (`OFFAXIS_ADJ`, `[SEED]`); shares none (the diagonal pair) `0.0`. The resulting matrix:

```
                E     C     A     I          (columns = judge's per-axis susceptibility)
  evidence    [1.0,  0.5,  0.5,  0.0]        # kin to Consequence (Revealing) & Authority (Memory)
  consequence [0.5,  1.0,  0.0,  0.5]        # kin to Evidence (Revealing) & Insinuation (Projection)
  authority   [0.5,  0.0,  1.0,  0.5]        # kin to Evidence (Memory) & Insinuation (Obscuring)
  insinuation [0.0,  0.5,  0.5,  1.0]        # kin to Consequence (Projection) & Authority (Obscuring)
```

**Why this fixes L1 (re-derived).** Rows are no longer permutations of one multiset, so the constant
offset no longer cancels. `gap(Evidence,Consequence)` now has coefficients `[+0.5,−0.5,+0.5,−0.5]`
over `[E,C,A,I]` — it depends on **all four axes**, not two. A Memory-leaning judge `{E:.7,A:.7}`
correctly ranks Evidence & Authority (both Memory) above Consequence & Insinuation; a truly balanced
judge still ties (correct — a balanced judge *has* no style preference).

**Honest limit — rank 3, not 4.** The matrix satisfies `row_E + row_I = row_C + row_A = 𝟙`, so
`alignment(E)+alignment(I) = alignment(C)+alignment(A)` for every judge — one linear constraint. This
is *semantically correct*: four styles occupying a 2-D genre plane have exactly 2 genre DoF + 1
magnitude = 3 independent directions. It is a strict improvement over the current effective single-axis
discrimination. If Jordan wants full rank-4 independence (all four style scores freely settable), break
the symmetry with distinct diagonal floors per style (e.g. small, unequal `DIAG_s ∈ {0.0,0.05,0.10}`
grounded in an asymmetry argument) — flagged as a fork, not assumed.

**Code change (minimal).** Replace `_row()` with a genre-overlap builder; `STYLE_AXIS` keys and the
`style_axis_alignment`/`style_axis_dsigma` call sites are unchanged. The δσ channel, `ARMATURE_MAX_DSIGMA`,
the asymmetric-proceeding gate, and the zero-vector degenerate case all keep their current semantics.
`OFFAXIS_ADJ = 0.5` is `[SEED]`; the `1.0`/`0.0` structure is grounded in §1.3.

```python
# proposed replacement for _row() in armature.py
_GENRE = {  # npc_behavior_v30 §1.3 head:32-42; complete_systems_reference §1.2
    "evidence":   ("memory",     "revealing"),
    "consequence":("projection", "revealing"),
    "authority":  ("memory",     "obscuring"),
    "insinuation":("projection", "obscuring"),
}
OFFAXIS_ADJ = 0.5   # [SEED] shared-one-genre-dimension weight; primary=1.0, shares-none=0.0

def _row(style):
    return {ax: (1.0 if ax == style
                 else OFFAXIS_ADJ if len(set(_GENRE[style]) & set(_GENRE[ax])) == 1
                 else 0.0)
            for ax in ArmatureAxis.ALL}
```

Acceptance test (add to `_kernel_tests.py`): for a Memory-leaning judge, `dsigma(Evidence) ==
dsigma(Authority) > dsigma(Consequence) == dsigma(Insinuation)`; and there exists a judge for which two
*different* styles produce different δσ while sharing the same primary-axis weight (the property the
current matrix provably cannot satisfy).

---

## §3 Fix L2 — derive the contest armature from the Conviction vector

**Goal.** `position_of(adjudicator)` should return an `ArmaturePosition` **computed from the
adjudicator's `personal_convictions`**, not read from a hand-authored dict. This requires a mapping
`CONV_TO_RESONANCE : 13 Convictions → 4 contest axes {evidence, consequence, authority, insinuation}`.

**Why not reuse the existing 13×4 axis matrix?** That matrix targets the *substrate* axes
(hierarchical/sacred/instrumental/traditional) — a different question ("where does this Conviction sit
in value-space") than the contest question ("which rhetorical register moves a holder of this
Conviction"). Compose-through-substrate would launder a second interpretation on top of the first. A
direct Conviction→resonance map is cleaner and independently gradeable.

**Grounding.** Map each Conviction to the rhetorical register that, per its own §2/§3 rationale,
*binds* a holder — mirroring how `npc_behavior_v30 §2` already assigns each named NPC a Primary
Resonant Style by hand. The proposed `13×4` (rows sum-free; each is a susceptibility profile in
`[0,1]`, `[SEED]` magnitudes, structure cited):

| Conviction | evidence | consequence | authority | insinuation | rationale (cited) |
|---|---:|---:|---:|---:|---|
| Faith | 0.7 | 0.2 | 0.5 | 0.1 | reality-responsive theology → Evidence strains it (§2.2 Himlensendt) |
| Authority | 0.2 | 0.2 | 0.9 | 0.3 | defers to binding authority (§1.3 Authority row) |
| Order | 0.5 | 0.4 | 0.6 | 0.2 | procedural; moved by precedent-evidence + rank |
| Scholastic | 0.9 | 0.4 | 0.2 | 0.2 | inquiry-mode → named verifiable fact (§3.4) |
| Utility | 0.4 | 0.9 | 0.1 | 0.3 | consequentialist → Consequence (§2.4 Vaynard) |
| Equity | 0.4 | 0.7 | 0.2 | 0.3 | outcomes for the populace → Consequence (§2.6 Vossen 2°) |
| Liberty | 0.3 | 0.5 | 0.1 | 0.5 | anti-authority; moved by implication, not command |
| Precedent | 0.9 | 0.2 | 0.4 | 0.2 | documents/records are its language (§2.3 Baralta) |
| Community | 0.3 | 0.4 | 0.3 | 0.6 | relational; moved by the unstated/among-us register |
| Identity | 0.3 | 0.3 | 0.5 | 0.6 | categorical belonging; authority-of-the-group + insinuation |
| Warden | 0.6 | 0.6 | 0.3 | 0.2 | stewardship; evidence of harm + projected consequence |
| Virtue | 0.4 | 0.5 | 0.3 | 0.3 | intrinsic character; mild across |
| Honor | 0.3 | 0.3 | 0.7 | 0.4 | oath/reputation → recognized binding authority |

**Composition.** `ArmaturePosition = Σ_c personal_convictions[c] · CONV_TO_RESONANCE[c]`, clamped to
`[0,1]` per axis (linear, same shape as the substrate composition rule). Because `personal_convictions`
is structured-concentration normalized to 1.0, the result is a convex-ish blend already in range;
clamp guards the hand-set edge cases.

**Interaction with L4.** This derivation needs a `CONV_TO_RESONANCE` row for every Conviction the cast
actually uses — which is why **L4 must be resolved first or jointly** (the legacy labels Reason /
Autonomy / Continuity have no row here, by design; migrate them via the taxonomy). Ship C-2 and C-4
together.

**Code change.**
- Add `CONV_TO_RESONANCE` (13×4, `[SEED]`) beside `STYLE_AXIS`.
- Add `armature_from_convictions(personal_convictions) -> ArmaturePosition`.
- `position_of(adjudicator, ...)`: if the adjudicator carries `personal_convictions`, compute via
  `armature_from_convictions`; else fall back to the supplied `armature_positions` dict; else zero.
  The asymmetric-proceeding gate and Panel-mean logic are unchanged.
- Deprecate `DEMO_JUDGE_POSITION` hand-authoring to test-only.

Acceptance test: a Faith-primary adjudicator yields `evidence > consequence` susceptibility (so
Evidence-style appeals earn more δσ against him), matching `§2.2` Himlensendt's authored Primary
Resonant Style = Evidence — **derived, not hand-set**. Regression: with no `personal_convictions`
supplied, behavior is byte-identical to today (zero vector → flat scalar).

---

## §4 Sequencing & risk

1. **C-1 (L1) first** — self-contained, changes only `_row()`, no data-model change, immediately
   testable. Low risk.
2. **C-4 (L4) next** — migrate legacy Conviction labels so every cast member has a taxonomy Conviction
   (prerequisite for C-2's rows). Content reconciliation; coordinate with C-3 (L3 roster contradiction)
   so the migration picks one canonical Conviction per NPC.
3. **C-2 (L2) last** — add `CONV_TO_RESONANCE` + `armature_from_convictions`, rewire `position_of`.
   Gated on C-4 so no NPC hits a missing row.
4. **Calibrate** all `[SEED]` magnitudes (`OFFAXIS_ADJ`, the 13×4 cells) under the `02_` harness before
   flipping any `[SEED]` to canonical; index them into `values_master.yaml` (closes L7 for this slice).

Risk: the 13×4 magnitudes are judgment calls; keep them `[SEED]` and let the parity/calibration harness
move them. The **structure** (which register binds which Conviction) is grounded in `npc_behavior §2`'s
existing hand assignments — this fix's job is to make those assignments *emerge from the vector* instead
of being re-authored per NPC, which is also the anti-drift win (one source, not two).
