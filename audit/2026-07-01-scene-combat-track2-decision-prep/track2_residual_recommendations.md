# Scene-Combat Track-2 Residuals — Decision Memo

**Status: RECOMMENDATION, not a decision.** This memo compiles two Track-2 single-source
residuals for the scene-combat engine (`designs/scene/combat_engine_v1/`) through an
agonist/antagonist debate, synthesis, adversarial (skeptic) review, and reconciliation. Nothing
in this document has been implemented — no code, config, or docstring has been touched. Both
recommendations below are queued for Jordan's ratification. Supporting measurement artifacts live
alongside this file: `wt_spd_deleak_report.md`, `wt_spd_deleak_measurement.py`,
`wp_reach_authority_comparison.md`, `wp_reach_authority_measurement.py`.

---

## Residual 1 — wt/spd cost-path single-source de-leak

**Scope:** two independent candidate substitutions in the weapon cost-path math —
`core.py:heft_resp` (damage-impact path) and `systems.py:weapon_tempo` (tempo path) — both
proposed as ways to close a single-source leak where weight/hands penalties are computed from
one primitive chain (`wield_heft`) instead of being derived consistently.

### Agonist case (for approving both substitutions as proposed)

- The current `heft_resp` and `weapon_tempo` implementations pull weight/hands penalties from a
  single ad hoc primitive (`wield_heft`) rather than a principled, physically-grounded derivation —
  that's the single-source leak Track-2 exists to close.
- Substituting `wield_heft`-reuse in `heft_resp` produces small, defensible deltas across seven of
  eight weapons (+0 to +6 flat damage per `wt_spd_deleak_report.md:57-63`) — evidence the fix is
  basically sound for the damage path.
- For the tempo path, `recoverability_factor` is grounded in real physics: it correlates with the
  current `spd` term at r=+0.878 (vs. +0.359 for thrust-vs-swing alone), which is strong evidence
  the underlying physical model is *more* correct than what ships today.
- Both substitutions anchor on the same reference weapon (arming/longsword ≈ 1.0), which is
  internally consistent and doesn't require re-deriving the whole cost path from scratch.

### Antagonist case (against approving both substitutions as proposed)

- The spear result under Path A is not a small correction — it's +10 to +14 flat damage, "roughly
  doubles to 2.5×" (`wt_spd_deleak_report.md` lines 64, 69-70) — on a weapon `forward_roadmap.md`'s
  separate spear-fix finding already measures at 94-96% win rate. Shipping a damage-side buff on an
  already-dominant weapon before its dominance is independently fixed compounds a known-live
  problem instead of correcting it in isolation.
- Path B's full substitution is confirmed structural double-counting, not a stylistic concern:
  `weapon_tempo`'s `pen` term (`systems.py:42`,
  `pen=cfg['WEIGHT_PEN']*_heft+cfg['HANDS_COMMIT']*(w['hands']==2)*_heft`, with live nonzero
  `WEIGHT_PEN=0.8`/`HANDS_COMMIT=0.5` at `config.py:43`) already penalizes weight and hands via
  `wield_heft`. `recoverability_factor` independently re-derives from the same `I_g`/`S_g`/hands
  primitives (via the shared `at_grip` call) for the same `spd` slot — substituting it whole
  double-counts weight/hands once through `pen`, once through the replacement.
- The report itself concedes the naive Path B substitution is "not the numbers that would actually
  ship" (lines 151-158) — i.e., even its own author doesn't stand behind the literal proposed
  change.
- Both candidates inherit the arming/longsword ≈ 1.0 anchor silently and independently; if that
  anchor convention is ever revisited, every number downstream rescales by a constant — a hidden
  dependency neither candidate surfaces on its own.

### Synthesis

Split the residual by path, because the two candidates have unrelated failure modes and unrelated
readiness. Path A (damage) is structurally clean — `heft_resp` has no sibling term reading the same
primitives, so there's no double-counting risk — and its only problem is a dominance-compounding
risk isolated to one weapon (the spear). Path B (tempo) is structurally unclean regardless of which
weapon it's applied to — the double-counting exists for every weapon, not just an outlier — so no
per-weapon carve-out can fix it; it needs a different-shaped candidate (a decomposition) before it's
even measurable.

### Skeptic refutation attempt

The skeptic pass tried to find holes in the "split the residual" synthesis on three fronts: (1)
whether the non-spear Path A deltas might hide their own double-counting — checked directly against
`core.py`/`systems.py` and confirmed `heft_resp` has no sibling term sharing its primitives, so this
holds; (2) whether the "88% attributed to approach phase, not damage" figure is actually sourced in
`forward_roadmap.md` — confirmed it is not; it appears only in the de-leak report's own text, which
is disclosed accurately above rather than misattributed; (3) whether the r=+0.878 correlation for
Path B is strong enough to justify shipping the naive substitution anyway on the theory that "close
enough physics beats acknowledged double-counting" — rejected, because correlation of the underlying
physical quantity doesn't answer whether the *mechanical wiring* double-counts, and the report's own
concession (lines 151-158) that the naive numbers wouldn't ship confirms the wiring problem is real
independent of the physics being right. All three challenges left the synthesis intact.

### Final reconciled recommendation

**Split the residual. Approve Path A (damage) everywhere except the spear. Do not approve Path B
(tempo) in its current naive form. Neither ships without joint calibration.**

**Path A — `core.py:heft_resp` (damage path):** Approve the `wield_heft`-reuse substitution for
every weapon **except** the spear (`point` head on the 2m hafted weapon). Verified deltas for the
seven non-spear weapons are +0 to +6 flat damage (`wt_spd_deleak_report.md:57-63`) — unremarkable
corrections, and `heft_resp` has no sibling term reading the same primitives, so there's no
double-counting risk here (confirmed clean at `core.py`/`systems.py`). The spear is the outlier: +10
to +14 flat, "roughly doubles to 2.5×" (report line 64, 69-70), landing on a weapon
`forward_roadmap.md`'s spear-fix finding already measures at 94-96% win rate (~88% attributed to
approach phase, not damage — report lines 78-82, confirmed directly in the report text since it
doesn't appear in `forward_roadmap.md` itself by grep). Shipping a damage doubling on an
already-dominant weapon before its separate dominance fix lands would compound a known-live problem,
not just add an independent correction. Concrete action if approved: gate the continuous `heft_resp`
swap on everything except `point`-class-on-the-spear record (or equivalent explicit carve-out), and
re-measure the spear once the approach-phase fix lands.

**Path B — `systems.py:weapon_tempo` (tempo path):** Do not approve the naive full substitution of
`spd` with `recoverability_factor`. This is confirmed structural double-counting, not a hand-wave:
`weapon_tempo`'s `pen` term (`systems.py:42`,
`pen=cfg['WEIGHT_PEN']*_heft+cfg['HANDS_COMMIT']*(w['hands']==2)*_heft`, with live nonzero
`WEIGHT_PEN=0.8`/`HANDS_COMMIT=0.5` at `config.py:43`) already penalizes weight and hands via
`wield_heft`. `recoverability_factor` independently re-derives from the same `I_g`/`S_g`/hands
primitives (via the shared `at_grip` call) for the `spd` slot — so substituting it whole
double-counts weight/hands once through `pen`, once through the replacement itself. The report
itself concedes this is "not the numbers that would actually ship" (lines 151-158). The grounding
validation underneath (current `spd` correlates with `1/recoverability_factor` at r=+0.878 vs
+0.359 for thrust-vs-swing alone) is solid evidence the *physics* is right, but the mechanical
wiring isn't. Direct next step: build and re-measure a decomposed candidate that isolates
`recoverability_factor`'s thrust-vs-swing shape independent of its weight/hands magnitude — that
candidate does not yet exist in the report and needs its own measurement pass before any sign-off.

**Both paths, if/when approved:** no merge without `combat_balancing_methodology.md` §4 joint
calibration (report lines 162-165; `forward_roadmap.md` Lesson 1, "no change without a regression
guard").

**Needs Jordan design input on (taste, not fact):**
1. Whether "hold the spear only" is fine-grained enough, or whether all of Path A should wait as a
   single gate until the approach-phase dominance fix lands.
2. Whether the anchor-weapon convention (arming/longsword ≈ 1.0, both formulas independently
   anchored there) is acceptable permanently, or needs revisiting — both candidates inherit it
   silently and re-anchoring would rescale every number by a constant.
3. How much of `recoverability_factor`'s magnitude to retain vs. fully normalize out in the Path B
   decomposition (tuning judgment the record can't settle by itself).

**Readiness verdict:** Ready for Jordan ratification on Path A (with the spear carve-out as the
concrete change to make if approved). Path B needs Jordan design input on question 3 above before a
decomposed candidate can even be built for measurement — it is not ready for a yes/no ratification
this round, only for a decision on which decomposition approach to build next.

---

## Residual 2 — WP.reach()/authority() canonical-home decision

**Scope:** `weapon_physics.py:193-202` (`authority()`) and `:205-217` (`reach()`) are two orphaned
diagnostic functions with "pending decision" docstrings. Neither is currently wired into a live
resolver path. The question is whether either has a canonical home to be wired into, or whether both
should be formally retired as diagnostics.

### Agonist case (for wiring one or both in)

- `reach()` is arguably the more HEMA-principled derivation of reach than the live `reach_base` path
  — it's a geometrically distinct model (`REACH_GEOM_SCALE=0.635` vs. the live path's
  `K_GRIP_REACH=0.4`), and retiring it outright would throw away a re-derivation seed that took real
  effort to build.
- `authority()` has zero input overlap with either live impact term today (`percussion_authority`
  for blunt, `heft_resp` for edged), so wiring it wouldn't immediately conflict with anything already
  on the resolver bus.
- Both functions represent completed diagnostic work; leaving them permanently orphaned risks the
  effort being forgotten or re-derived from scratch later.

### Antagonist case (against wiring either in now)

- `reach()` lacks `reach_base`'s `L0=4.0` offset entirely and carries an independently-tuned 2H
  gain, producing a per-weapon ratio to the live path that ranges 0.16 (dagger) to 0.77 (spear) with
  no affine fit — and the divergence isn't even monotonic in an obvious covariate (rapier 0.54 vs.
  arming 0.42 despite similar `head_len`), meaning the per-weapon `reach_adj` fudge compounds the gap
  beyond `L0` alone.
- The concrete failure mode for `reach()`: spear's `reach()`=5.98 sits below `CLOSE_REACH_REF`=6.5,
  so wiring it unscaled would zero exactly the close-combat penalty that gives spear its "dominant at
  range, vulnerable in close" identity — a core archetype, not an edge case.
- `authority()`'s only plausible wiring target is `heft_resp` — which is Residual #1's open question,
  not this residual's. Wiring it here would resolve Residual #1 through the back door, under this
  residual's label, without going through Residual #1's own approval gate.
- `authority()`'s `0.30` constant (line 202) is the only bare, uncommented literal in the entire
  module — every other constant carries `[SIM-CALIBRATE]`, `[FIAT]`, or a citation (e.g.,
  `percussion_authority`'s Oh et al. 2022). Under this repo's grounding discipline, an ungrounded
  formula shouldn't displace a live term regardless of the wiring question.

### Synthesis

Neither function should be wired in now, but for different reasons: `reach()` fails on its own
measured evidence (the non-affine, non-monotonic ratio to the live path, and the spear
close-combat-penalty failure mode are concrete, not speculative). `authority()` fails on process
grounds — it isn't this residual's decision to make, since its only viable target belongs to
Residual #1, and it also fails the repo's grounding-citation bar independent of that. The
correct action for both is the same regardless of the different reasoning: retire the "pending
decision" framing without deleting the code, and make clear that `authority()` remains open only
insofar as Residual #1 might eventually call on it.

### Skeptic refutation attempt

The skeptic pass tried three challenges: (1) whether the 0.16-0.77 ratio range could be explained by
a simple missing scalar (i.e., a one-constant fix) rather than being genuinely non-affine — checked
against the ratio table in `wp_reach_authority_comparison.md` directly, including the rapier-vs-arming
non-monotonicity, which rules out a single missing scalar since a scalar fix can't un-invert a
non-monotonic relationship; the non-affine finding holds. (2) whether `authority()` could be judged
independently of Residual #1 by treating "no live target today" as sufficient grounds to just delete
it — rejected, because "no target today" is different from "can never have one," and the record
shows `heft_resp` is exactly the kind of term it could target once Residual #1 resolves; deleting it
now would foreclose that option prematurely. (3) whether leaving both orphaned indefinitely is itself
a decision being smuggled in as a non-decision — acknowledged as a fair asymmetry, and surfaced below
rather than resolved by fiat, since it's a hygiene/visibility preference, not a factual question.

### Final reconciled recommendation

**Verified against source directly:** `weapon_physics.py:193-202` (`authority()`) and `:205-217`
(`reach()`), `config.py:4` (`L0=4.0`), `config.py:11`/`weapon_physics.py:88`
(`REACH_GEOM_SCALE=0.635` vs `K_GRIP_REACH=0.4`), `core.py:49-60` (`heft_resp` reads only
`w.get('wt')` + linear mass delta, never `WP.derive()`/`PoB_frac`/`MoI`), and
`wp_reach_authority_comparison.md`'s ratio table (0.16 dagger → 0.77 spear, non-affine). All prior
claims hold; no correction needed.

**`reach()` — retire the label, do not wire, do not delete.** It lacks `reach_base`'s `L0=4.0`
offset entirely and carries an independently-tuned 2H gain, producing a per-weapon ratio to the live
path that ranges 0.16–0.77 with no affine fit — and the divergence isn't even monotonic in an
obvious covariate (rapier 0.54 vs arming 0.42 despite similar `head_len`), meaning the per-weapon
`reach_adj` fudge compounds the gap beyond `L0` alone. The concrete failure mode: spear's
`reach()`=5.98 sits below `CLOSE_REACH_REF`=6.5, so wiring it unscaled would zero exactly the
close-combat penalty that gives spear its "dominant at range, vulnerable in close" identity — a core
archetype, not an edge case. Action: change the docstring from "pending decision" to "retired
diagnostic, not a live candidate"; leave `reach_base`/`CLOSE_REACH_REF`/`reach_adj` untouched. Full
re-derivation (all four terms together) is a separate future task, not this decision.

**`authority()` — leave orphaned; this decision is owned by Residual #1, not this one.** It has zero
input overlap with either live impact term today (`percussion_authority` for blunt, `heft_resp` for
edged — confirmed `heft_resp` never touches `PoB_frac`/`MoI`). But "no overlap today" isn't "safe to
wire" — its only plausible target is `heft_resp`, which is the *other* open residual (`wt`/`spd`
de-leak). Wiring it here would resolve Residual #1 through the back door under Residual #2's label.
Independently confirmed: `authority()`'s `0.30` constant (line 202) is the only bare, uncommented
literal in the entire module — every other constant carries `[SIM-CALIBRATE]`, `[FIAT]`, or a
citation (e.g., `percussion_authority`'s Oh et al. 2022). Under this repo's grounding discipline, an
ungrounded formula shouldn't displace anything regardless of the wiring question. Action: leave
labeled and orphaned; re-evaluate `sqrt(mass)*(0.30+pob)` as one candidate input only when Residual
#1 is decided.

**Asymmetry flagged for Jordan (taste call, not a fact):** deleting `authority()` outright is
lower-risk than deleting `reach()` — it has no live target and structurally can't get one until
Residual #1 resolves, whereas `reach()` is the more HEMA-principled derivation and arguably worth
keeping visible as a re-derivation seed. Whether to also physically relocate both functions to a
marked deprecated section vs. leaving them in place with updated docstrings is pure repo-hygiene
preference.

**Readiness verdict: (a) ready for Jordan ratification.** If he approves, the exact concrete change
is: retitle both docstrings' status line from "kept pending decision" to "retired diagnostic — not a
live candidate" (functions and all constants stay exactly where they are; no other line changes;
`authority()` stays flagged as pending re-evaluation under Residual #1, not resolved by this change).
