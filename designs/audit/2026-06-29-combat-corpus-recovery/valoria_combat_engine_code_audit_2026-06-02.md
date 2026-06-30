# Combat Engine v1 — Code Architecture & Pattern-Matching Audit

**Scope:** the committed `combat_engine_v1/` source (804 lines across 7 modules) — `core.py`, `combatant.py`,
`config.py`, `systems.py`, `tradition.py`, `wrapper.py`, `geometry.py`. **Lens:** software architecture (module
boundaries, purity, single-source-of-truth, coupling, dead code, robustness) and pattern-matching defects — both
*code* pattern-matching (brittle name/attribute dispatch) and *epistemic* pattern-matching (values set by "what the
answer should look like" vs grounded bottom-up). **Method:** full read of every line from the committed source.

`[READ: audit_src/{core,combatant,config,systems,tradition,wrapper,geometry}.py — all 804 lines, committed HEAD]`
`[SELF-AUTHORED — bias risk]` I wrote all of this. I've audited it harder than external code, and the headline
findings (P1/P2) are against my own recent additions (the dead armour-defeat hook, the duplicated damage call, the
attribute-conjunction weapon IDs, the matrix-calibrated constants). No finding is softened.

---

## VERDICT (worst-first, no false balance)

**The core architecture is sound and the role-object discipline genuinely holds** — every subsystem takes Combatant
objects by role, the wrapper owns A/B identity and (almost) all state mutation, and resolution is centralised in
`core`. The frame-inversion bug class the design was built to kill *is* killed at the structural level.

**But there are real defects, and they cluster in two places:** (1) a **duplicated 11-arg positional `core.damage(...)`
call repeated 10×** — the single largest maintainability/▸correctness risk, and ironically the exact positional-call
surface where transposition bugs live; and (2) **two "identify-a-specific-weapon-by-a-conjunction-of-attributes"
pattern-matches** (`is_long_pole`, `is_slow_heavy`) — the brittle anti-pattern, one of which feeds **dead code**. On
the epistemic side, the config is honestly self-labelled "calibrated against the harness, not canon," which — after
the method steer away from matrix-fitting — is the right flag to act on: a band of σ-weights are matrix-tuned magic.

**Nothing here is a live gameplay bug** (the dead paths are inert, the duplicated call is currently consistent), but
the duplication and the attribute-conjunction IDs are latent-bug factories and should be fixed before the engine
grows further (initiative/contratempo will add more `core.damage` sites and more weapon classes).

---

## P1 — DUPLICATED 11-ARG POSITIONAL `core.damage(...)` CALL (×10). Maintainability + latent correctness.
`core.damage(deg, weight, head, strength, armor, close, DAMAGE_SCALE, CAP_END, gap, perc)` is spelled out **ten
times** — wrapper.py lines 63, 134, 135, 140, 143, 155, 180, 189 (+ the approach stop-hit and displace-graze). Every
call passes the same 8 trailing args; only the degree string and the actor differ. This is the highest-severity
*structural* finding:
- **Latent correctness:** 11 positional args (incl. two booleans `close` and an int/float pair `scale,cap_end`) is
  precisely the transposition surface the role-object refactor was meant to eliminate — it survived inside `core.damage`.
- **Maintainability:** the percussion arg (`aggressor.w.get('percussion',8)`) had to be threaded into **8 sites by
  hand** this session (the geometry/percussion work); the next damage-relevant attribute will need the same 10-site
  edit. That is how a site gets missed.
- **Fix:** a single wrapper method `self._strike(actor, target, deg)` (or a free `strike(attacker, defender, deg, cfg)`)
  that reads weight/head/strength/gap/perc off the attacker object and `armor/close` off the context, returning the
  int. Collapses 10 call-sites to one definition; removes the positional surface entirely. (Mirrors the role-object
  fix already applied everywhere *except* the damage call.)

## P1 — ATTRIBUTE-CONJUNCTION WEAPON IDENTIFICATION (×2). Brittle pattern-match; one feeds dead code.
Two sites reverse-engineer "is this a specific weapon" from a conjunction of attributes — the comments literally name
the weapons they're trying to match:
- `systems.py:37` `is_long_pole = (w['hands']==2 and w['reach']=='long' and w['spd']<=0.0 and w['wt']=='light')  # spear, staff`
- `systems.py:103` `is_slow_heavy = (w['wt']=='heavy' and w['head']=='blunt' and w['spd']<=0.0)  # mace, poleaxe`
This is the brittle anti-pattern: add a new long light pole (a glaive, a longer spear variant) or a heavy blunt
non-slow weapon and the conjunction silently mis-classifies it. It also *encodes weapon identity in logic* instead of
in data. **Fix:** make the property explicit — a `closes_poorly` (or `pole_recovery_penalty`) flag and a
`plate_breaker` flag (or better, let the existing `percussion`/`reach`/`grip_len` values drive the behaviour
continuously, which `armor_defeat_sigma` now already does via `percussion`). The `is_slow_heavy` case is **moot** —
see P2 (it feeds dead code) — so fixing P2 deletes that one outright.

## P2 — DEAD CODE: `armor_defeat_bonus` + `SLOW_WEAPON_IMPACT_K=0.0`. Necessary/Elegance.
`systems.py:98-106` `armor_defeat_bonus()` returns `cfg['SLOW_WEAPON_IMPACT_K'] * armor_factor`, and
`config.py:48` sets `SLOW_WEAPON_IMPACT_K=0.0` ("tuning hook for the poleaxe-vs-plate fix"). So the function **always
returns 0.0**; `wrapper.py:127` `astr = aggressor.strength + armor_defeat_bonus(...)` adds zero. The poleaxe-vs-plate
role is now carried by the `percussion`-scaled `armor_defeat_sigma` instead, so this whole path is **superseded dead
code** — the function, the constant, the `astr` addition, and the `is_slow_heavy` conjunction inside it. **Fix:**
delete all four. (Keeping a zeroed "tuning hook" is the keep-bias the project's retirement discipline warns against.)

## P2 — `reading()` DEFINED TWICE. Single-source-of-truth violation.
`(c.cog+c.att)/2` is defined in **both** `systems.py:52` and `wrapper.py:222`. They agree today, so no live bug — but
two definitions of the same primitive is exactly how they later diverge. **Fix:** delete `wrapper.py:222`; import
`from systems import reading` (the wrapper already imports `systems as S`, so use `S.reading`).

## P2 — EPISTEMIC PATTERN-MATCHING: a band of σ-weights are matrix-calibrated magic, now off-method.
`config.py:1` is honest: *"Class-C — calibrated against the harness, not canon."* After the method steer (validate
top-down vs history, **not** matrix mean-|Δ|), the constants split into two epistemic classes that the file does not
distinguish:
- **Grounded (keep):** `RESIST`/`DELIVERY` (armour physics), `percussion` per weapon (§4), `reach_adj` (validated
  reach ordering), the geometry params (calibrated to *reproduce* validated tiers), `UPSET_FLOOR` (design rule),
  `ADEF_THRESHOLD` (mail-defeats-cuts physics). These trace to a source.
- **Pattern-matched (flag):** the bare inline coefficients in `bind_sigma` (`systems.py:227-234`: `0.06`, `0.04`,
  `0.0156`), the `mode_sigma` mix weights (`0.45/0.45`, `0.30/0.70`), `INIT_K=0.045`, `COMMIT_SIGMA=0.18`, the
  `neutralize`/`riposte` probabilities (`0.55/0.62/0.50`, `0.20`, `0.40` in the bind loop). These were set to make the
  aggregate behave; none cites a source. They are not *wrong*, but they are unaudited magic and several were tuned
  against the matrix the method now demotes. **Fix:** (a) move the inline `bind_sigma` literals into `config.py` (they
  are the only σ-weights hiding *inside* a function — every other tunable is centralised); (b) tag each config block
  `# grounded:<source>` or `# calibrated:<harness>` so the epistemic status is visible; (c) re-validate the
  calibrated band against the emergent/historical anchor, not the matrix.

## P3 — `legibility()` BRANCH GAP. `cut_thrust` swings read as "neutral."
`systems.py:180-184`: `point→LEGIB_THRUST`, `straight_cut/curved_cut/blunt→LEGIB_SWING`, **else→1.0**. A `cut_thrust`
weapon (arming, longsword, dagger) making a *cut* therefore gets legibility `1.0` (neutral), not `LEGIB_SWING` —
i.e. a longsword cut is treated as no-more-readable-than-baseline, while a sabre cut is. Likely an oversight (a
cut-and-thrust sword's cut is a lateral swing and should read as one when it cuts). **Fix:** decide legibility by the
*mode being thrown this beat* (the engine already computes cut-vs-thrust mode in `head_mode`), not by the static head
category — which also removes another string-category branch.

## P3 — DUPLICATED MODE-DISPATCH: `head_mode()` vs `coupling()`. Possible dead function.
`core.py:25-32` `head_mode()` computes the cut-vs-point mode-shift; `core.py:45-53` `coupling()` re-implements the
same blunt/point/cut_thrust/else dispatch independently (via `max(_mode_transmit('cut'), _mode_transmit('point'))`).
`head_mode` may be **unreferenced** (grep: not called inside the engine). If so it is dead; if used elsewhere, the two
implementations of "what mode does this head fight in vs this armour" can diverge. **Fix:** confirm callers; either
delete `head_mode` or route `coupling` through it so the mode logic has one definition.

## P3 — PURITY LEAK: `halfsword_switch` mutates a "pure" module's input.
`systems.py:149-159` is in the file whose docstring says "NO subsystem … mutates combatants," yet `halfsword_switch`
sets `c.weapon=…` (`wrapper.py:78-79` calls it on both actors). It is documented as reversible and the wrapper owns
the call, but it violates the stated module contract (mutator living among pure functions). **Fix:** either move the
form-switch into the wrapper (where mutation is owned) and keep `systems` deciding *whether* to switch (pure
predicate `want_halfsword(c, closed, armor)→bool`, wrapper applies), or relabel the systems contract to carve out the
documented exception. The predicate-vs-apply split is cleaner and matches the feint pattern already used (pure
`feint_eval` returns a dict; wrapper applies).

## P3 — BARE MAGIC NUMBERS in the wrapper's outcome mapping. Centralisation gap.
Inline probabilities not in `config.py`: `wrapper.py:59` `+0.4` (stop-hit base nsig), `:134` `0.4`/`:135` `0.30`
(graze chances), `:138` `0.55`, `:139` `0.20`, `:179` `0.4` (bind hit), `:107/:113` `0.4`/`0.3` mental-fatigue
weights, `:196/:219` `0.03`. Everywhere *else* tunables are centralised; these escaped. **Fix:** lift to `config.py`
with names (the file already has the discipline; these are the leaks).

---

## ROBUSTNESS / MINOR
- **Parallel-dict key-sync risk (P3):** `WEAPONS`, `GEOMETRY` (combatant.py), and `GATE` (systems.py:67) are three
  hand-maintained dicts keyed by weapon name. A weapon in `WEAPONS` but missing from `GATE` → `KeyError` at
  `mode_sigma`; missing from `GEOMETRY` → silently keeps its hand-set `gap` (inconsistent derivation, no error). Add a
  one-line import-time assertion that the three key-sets match (fail fast), and decide the GEOMETRY-miss policy.
- **`sys.path` hard-coding (P3):** every module does `sys.path.insert(0,'/home/claude/...')` and `…/v32`. Fine for the
  harness, but it hard-codes the container layout into the engine source — a packaging defect if this ever ships as a
  module. Acceptable for now; flag for the Godot port (`[ASSUMPTION: harness-only — basis: current sim surface]`).
- **`MAX_EXCHANGES_PER_BOUT=3` + `rng()<0.03` separation (P3):** both are reasonable bout-length bounds but are
  magic; the `0.03` random-separation per beat is undocumented. Name + comment.
- **`reflex`/`reading`/`reach_base` recomputed per-beat (negligible):** pure recompute each beat; fine at sim scale,
  and correct (they depend on live fatigue). Not a defect — noting it was checked.

## WHAT IS GENUINELY GOOD (verified, not flattery)
- Role-object discipline holds end-to-end: no subsystem indexes raw A/B; the wrapper assigns aggressor/defender once
  per beat and flips by object swap (`wrapper.py:193`), frame-safe. This is the cure for the documented bug class and
  it is real.
- Resolution is centralised in `core` and delegates to the ratified engine — no re-implementation, no parallel odds.
- `config.py` is, the inline-leak exceptions aside, a disciplined single source with per-block provenance comments.
- The geometry layer is calibrated to *reproduce* validated behaviour (not to fit), baked once at import — the right
  pattern, honestly documented.
- Pure-evaluator/wrapper-applies split (feint) is a clean seam; extend it to halfsword.

## REMEDIATION ORDER (worst-first)
1. **P1** Collapse the 10 `core.damage` calls into one `strike()` helper (kills the positional surface).
2. **P1** Replace the two attribute-conjunction weapon IDs with explicit data flags (and delete `is_slow_heavy` via #3).
3. **P2** Delete the dead armour-defeat-bonus path (`armor_defeat_bonus`, `SLOW_WEAPON_IMPACT_K`, the `astr` add).
4. **P2** De-duplicate `reading()`.
5. **P2** Split config constants into grounded vs calibrated, move the `bind_sigma` inline literals in, re-validate
   the calibrated band against the historical/emergent anchor (not the matrix).
6. **P3** legibility-by-mode; head_mode/coupling de-dup; halfsword purity (predicate+apply); lift remaining magic
   numbers; add the parallel-dict key assertion.

`[CONFIDENCE: high — every finding cites a specific committed line read this session; severities reflect latent-bug
risk and method-alignment, not style preference. The two P1s and the dead-code P2 are unambiguous; the epistemic-
pattern-matching P2 is a judgment call flagged as such.]`

---
# REMEDIATION APPLIED (2026-06-02) — committed a5a0a06 (Stage A) + ec185bb (Stage B)

Two stages, deliberately separated so the behavior-changing fix is isolated and measurable.

## STAGE A — behavior-PRESERVING (a5a0a06). Verified identical to baseline (same seed): mirror 49, spear>dagger 95,
ls>spear 16, poleaxe>arming-A3 92, mace-A0 19, monotonicity [53,57,71,92], H6v3 79 — all unchanged.
- **P1 FIXED** — the 10 duplicated 11-arg `core.damage(...)` calls collapsed into one `core.strike(attacker,
  defender, deg, close, cfg)` (reads weight/head/strength/gap/percussion off the attacker, armour off the defender).
  8 call-sites now route through it; the positional-transposition surface exists in exactly one place.
- **P1 FIXED** — `is_long_pole` attribute-conjunction replaced by an explicit `closes_poorly=True` data flag on
  spear+staff. `is_slow_heavy` deleted outright (it lived only in the dead bonus path).
- **P2 FIXED** — dead `armor_defeat_bonus` + `SLOW_WEAPON_IMPACT_K` + the `astr` addition all deleted (returned 0;
  superseded by percussion-scaled `armor_defeat_sigma`).
- **P2 FIXED** — `reading()` de-duplicated (wrapper-local def removed; routed to `S.reading`).
- **P2 FIXED** — `bind_sigma` inline literals (0.06/0.04/0.0156) lifted to named config (`BIND_TECH_K`/`BIND_TACTILE_K`/
  `BIND_STR_K`); outcome-mapping magic numbers (stop-hit base, partial-graze chances, wind-bind, riposte-on-
  neutralize, bind-hit, separation, mental-fatigue weights) lifted to named config. Config now tags blocks
  grounded-vs-calibrated.
- **P3 FIXED** — dead `head_mode()` deleted (coupling owns the mode logic).
- **P3 FIXED** — `halfsword_switch` (mutator-in-pure-module) split into pure predicate `halfsword_target(...)`; the
  wrapper now applies the `c.weapon=` mutation (matches the feint pure-evaluator/wrapper-applies seam).
- **P3 FIXED** — import-time assertion that `WEAPONS`/`GEOMETRY`/`GATE` key-sets stay synchronised (fail-fast on drift).

## STAGE B — behavior-CHANGING correctness fix (ec185bb), isolated + measured.
- **P3 FIXED** — `legibility()` branch gap: a `cut_thrust` weapon's cut previously read as neutral (1.0). Legibility
  now follows the MODE the head fights in vs armour (swings unarmoured = easy-read; shifts to gap-thrust vs plate =
  hard-read), matching `coupling`'s mode-shift. **Measured delta (small, historically correct):** ls>spear-A0 16→13
  (a longsword cut now reads as the swing it is); emergent A0 tier stable (longsword 42, rapier 82, spear 82, mace/
  dagger bottom); monotonicity [51,58,73,91], invariants hold. Did not worsen the pre-existing longsword-low /
  rapier-high flags (separate findings).

## STILL OPEN (deferred, lower-value or separate work)
- Epistemic re-validation of the *calibrated* config band against the historical/emergent anchor (not the matrix) —
  the constants are now NAMED and tagged, but the re-validation against the demoted matrix is its own pass.
- A few low-value bare constants remain inline (the `min(0.95,...)` riposte caps, the `0.4` disrupt/sim graze) — left
  as guardrails; lift if the config block is touched again.
- `sys.path` container hard-coding — flagged for the Godot port, not fixed here (harness-only concern).

`[CONFIDENCE: high — Stage A behavior-identity verified against baseline at n=1500 same-seed; Stage B delta measured
and bounded; both committed clean through the gates.]`
