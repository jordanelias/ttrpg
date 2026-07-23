# Combat Engine — Fiat / Broken-Logic Audit

**Author:** PC-lane audit node (CLAUDE.md §0/§10) · **Date:** 2026-07-23 · **ED:** ED-PC-0023
**Follow-on to:** ED-PC-0022 (U10 morphology-lever activation).
**Charter:** find WHERE top-down *fiat* occurs and fix broken LOGIC that suppresses emergence — radically
questioning ratified tenets, not just calibration. **Status: PROPOSED** (ratifies by merge, ED-1094).

## Method — four independent passes

Producing and checking are different jobs (§0). Three **read-only subagent hunters**, each blind to the others
and to the author's reasoning (structural independence), plus the author's own `[FIAT]`/`[ASSERTED]` inventory
(18 tagged sites). Lenses: (1) asymmetries & invariants; (2) hard clamps/floors/gates that erase gradients;
(3) contradictions/double-counts/mis-signs/dead-but-read terms. Findings reconciled below.

## The ratified tenet under the spotlight — grip-invariant thrust: GROUNDED

`weapon_physics.phi_grip('point') == 1.0` (`[ASSERTED — rigid-body first principles]`) was the flagged suspect.
Interrogated to first principles across two independent passes:

- Delivered axial-thrust **force** through a (rigid) shaft *is* grip-invariant — hand position along the column
  doesn't change the compression transmitted. Correct.
- The real costs of choking up are (a) **control/telegraph** — the point is beaten off-line more easily, the
  gathered posture reads — and (b) **reduced body-commitment** when close. Both already have live homes:
  (a) `choke_counterbalance → CHOKE_ACCURACY_K` legibility (charged for *every* head incl. point), (b) the
  reach / `lunge_depth` / `commit_depth` / `recoverability` systems. A `phi_grip` force term would **double-count**.

**Verdict: the invariant is the correct factoring; the ED-PC-0022 re-home (choke cost → control channel) was the
fix.** The "suspicious" feeling was pointing at the *wiring* (U5's mis-park), not the invariant. No change.

## Fixed in this pass (clean, contained — 9 accepted-red baseline unchanged)

| # | Site | Broken logic | Fix |
|---|---|---|---|
| 1 | `core.THRUST_LEVER_FLOOR` | 0.30 **bound** for the 7 longest polearms (head_len 1.85–2.03 m), flat-topping their real 0.271–0.297 spread to exactly **0.300** | → **0.24** (below the natural min); polearm class regains its head_len-driven spread |
| 2 | `core.GAP_EXPOSURE` | `{cloth:0.85, mail:0.90, plate:0.90}` **contradicts core.py's own grounding prose** ("mail exposes MORE than plate"; "cloth mostly accessible") — mail==plate, cloth lowest | → `{cloth:0.97, mail:0.95, plate:0.90}` (monotone none>cloth>mail>plate; **plate anchor unchanged**) |
| 3 | `Combatant.pool` | dead re-implementation of `core.resolution_pool` (`max(5,history+6)`), **zero readers** — §8 "every rule lives once" violation | removed; consumers call `core.resolution_pool` |
| 4 | `weapon_physics` WIRING-STATUS doc | described the **deleted** `authority()`/`reach()` as "not yet wired" and cited the **closed** `core.p_auth` single-source debt as open | struck the stale sentences |

## Flagged — evidenced, fix-spec'd, deliberately deferred (each needs its own verification; not bundled, per §2)

- **`MAX_TEMPO_PEN=0.8` hard-cap flat-tops 38/53 weapons** to one identical 0.80 (a rapier at raw pen 0.831 and a
  spear at 2.878 read the same tempo penalty). **This is the single largest emergence-suppressor found.** Fix =
  surgical over-cap-tail saturation `min(pen,MAXP) + K·tanh(max(0, pen−MAXP))` (arming 0.793 is sub-cap, so the
  mirror stays byte-identical; only the 38 over-cap weapons re-order within [0.80, ~0.86]). **Deferred because** it
  changes 38 weapons' `weapon_tempo`/`close_tempo` and so requires regenerating `tests/valoria/r3_identity_golden.json`
  per that fixture's re-baseline protocol — and **no generator exists** (it was built once, must be hand-reproduced).
  That is its own deliberate increment, not a bundle-in.
- **`PERC_EXP=0.30` low-mass compression.** The docstring self-admits the power law "cannot express structurally
  weak from input magnitude alone"; `REVERSED_GRIP_EFFICIENCY=0.25` patches only the Mordhau path, but
  `percussion_element_authority` applies the same undiscounted form to native secondary blunt elements
  (lucerne fluke, bec beak) — likely over-crediting them. Root recalibration touching every blunt weapon → Jordan-gated.
- **`PERC_TRANSMIT_FLOOR=0.35`** flat-tops 11 two-handed-sword Mordhau armour-transmission ratios (0.215–0.308) to 0.35.
- **`impose_node` (the whole imposition mechanism) — RETIRED as fiat (Jordan ruling 2026-07-23).** Flagged first as
  "fixed 0.5 rates, zero skill-gradient — candidate to couple to `eff_cw`". Jordan's ruling went deeper: the
  mechanism *itself* is fiat — it FORCES a tradition's preferred node (German impose-the-bind / Italian refuse-it)
  via a label-keyed coin-flip that OVERRIDES the emergent bind/counter resolution. Coupling it to skill would only
  dress the fiat as style. **A tradition's node-preference must EMERGE from the fighter's BUILD, not be imposed.**
  Executed: `IMPOSITION_GATE=False`, `impose_node` → no-op stub, `IMPOSE_BIND_BOOST`/`IMPOSE_REFUSE_P` deleted (this
  reverses the ratified WS-4 `IMPOSITION_GATE` default, per Jordan's live design authority). Verified the emergent
  channels carry the differentiation: a fighter who **invests** in a skill wins more, monotonically and with no fiat
  — `bind`-skill 1.0/2.0/3.0 → 61.3% / 71.1% / 74.7% win-share (through `bind_sigma`/`mode_sigma`); `parry` 1.0/2.0
  → 57.2% / 65.6%. Combat suite unchanged (9 accepted-red); the texture instrument still passes with imposition off.
- **`adef_cap` blunt branch doesn't thread `sel_head`/`sel_pc`** (unlike `core.strike`): `puncture_pressure`
  multiplies a pommel-strike by the whole-weapon *blade-tip* `strike_concentration`. Latent — currently inert
  (`ADEF_BLUNT` always wins the `max()`), structurally wrong.

## Confirmed sound (no defect)

- Core resolution signs all correct: `bind_sigma`, `legibility`, `reach_sigma`/`reach_threat`/`armor_defeat_sigma`;
  `gap_prec`/`thrust_auth` threaded exactly once each; `eff_cw` ratio denominators bounded ≥0.4.
- The `perc²`-vs-rigid-armour compounding is self-documented and intentional (FIX-1b).
- `SWING_FLOOR`/`PERC_ROOM_FLOOR`, the agility `min(1.0)` cap, `CUT/THRUST_AUTH_REF` clamps, `UPSET_FLOOR`,
  `ATTACKER_BIAS`, `ADEF_THRESHOLD` — verified as grounded/inert-guard/by-design, not emergence-suppressing.
- **CLAUDE.md §5's "Combat Pool defined three ways" is overstated:** the live engine + `engine/params/core.md` +
  `module_contracts.yaml` all agree on `max(5, History+6)`; only `values_master.yaml` carries the stale
  `(Agi×2)+History+3` (self-flagged rot) — one stale auto-extraction, not a live three-way conflict.

## Provenance

Fixes in `core.py` (THRUST_LEVER_FLOOR, GAP_EXPOSURE), `combatant.py` (pool removal), `weapon_physics.py`
(doc). Engine-params JSON re-exported (round-trip green). `pytest tests/valoria -k combat` → 9 accepted-red,
146 passed. No change to core damage/σ resolution.

---

## Design principle (Jordan ruling, 2026-07-23) — emergent expression over fiat

The imposition retirement crystallised a governing principle for the combat engine (and the wider design):

> **Each combatant should have their own feel, emergent from their full stack — tradition, abilities, attributes,
> weapon, armour, and preferences/biases/inclinations — and their fights should resolve in a way that feels real
> and correct to *their* style. It doesn't mean every build is good, but every build should be *available*. Hence
> all the surfaces.**

Consequences this pass acts on:

1. **No fiat.** A tradition (or any trait) must never *force* an outcome by label. It expresses through the
   fighter's build tilting the *emergent* resolution. `impose_node` violated this and is retired; the morphology
   levers + ability surface (U10) are the *right* shape — they modulate grounded primitives, they don't override.
2. **Expressive availability, not parity.** Balance-to-flat (the aggregate-winrate gate that drove U9's "keep at
   K=0" and the old 7-channel-weight removal) is the wrong target. The right target is that every build is
   *playable and distinct*; some are stronger than others, and that is fine. The correct instrument for a
   situational lever is therefore **per-fight texture with outcome-preservation** (§ u10 doc §8), not aggregate
   win-rate.
3. **Efficacy from investment/expertise.** "Feel" and strength come from *what the fighter invested in* — skill
   level in a technique, learned abilities — not from tradition membership. `skill('bind')` already demonstrates
   this emergently (investment scales outcome monotonically, above). The forward architecture is **levels of
   investment for techniques**: `ability_factor` graded by an invested level (the pattern `skill()` already sets),
   turning binary equipped-abilities into a continuum — the ability system's own stated target model
   ("learned ACCESS … effectiveness EMERGES from primitives"). Tradition gates *access* to a kit; investment +
   skill drive *efficacy*. (Scoped as the next increment, not built here.)
4. **The surfaces are the mechanism.** Every surface (`edge_read`/`spine_press`/`edge_grab`/`choke_control`/
   `facing_regime`, and the future graded-technique hooks) exists so a facet of the fighter's identity expresses
   in resolution. That is why they are worth having even at ~0 aggregate effect.
