# Grappling System — Validation (bottom-up build, top-down precedent check)

**Date:** 2026-05-30 · **Module:** `grappling.py` (self-test 6/6) · **Status:** Class-C proposal; **no canon retconned** (reuses the canonical close-combat actions; fills the canon-acknowledged unarmed gap ED-129). `[CONFIDENCE: high]` `[SELF-AUTHORED — bias risk: see §4.]`

Built grappling bottom-up from canonical primitives (Disarm/Tie Up/Escape/Retrieve + ST1 Strength + the armour matrix + the hands axis) and validated top-down against Fiore's *abrazare* / *ringen* / the rondel-dagger record.

## §1 — Build validated (self-test 6/6)

Strength-dominant grapple contest (extends ST1); the **hands axis** (a 2H weapon hampers the clinch); **asymmetric fatigue** (a heavier-drained fighter grapples worse — fatigue's *correct* role); the **closing tempo cost** (grappling surrenders reach/tempo); and the load-bearing check — **the dagger-finish bypasses mitigation** (a controlled foe = gap access; dagger-to-gaps reaches a full-harness foe at mod 2 where a cut is deflected to mod 0).

## §2 — Top-down precedent check (combat-sim runs)

**A) The third plate-counter — strikes to fell a full-harness foe:**

| approach | strikes | mechanism |
|---|---|---|
| blunt (poleaxe) | 3.0 | transmits percussion through plate |
| **grappler (throw + dagger to gaps)** | **4.2** | **bypasses mitigation — throw him down, dagger the gaps** |
| cut (longsword) | 4.3 | (its STR×2 mass, *not* its cut mod — the cut mod is 0, deflected) |

→ All three counters now fell plate where a pure cut cannot. The triad — **blunt / point-to-gaps / grapple** — is complete. ✓

**B) Grappling is a context-gated choice, not a win-button:**

| matchup | grappler win-rate | reading |
|---|---|---|
| vs a spacing rapier, **unarmoured** | **0%** | the spacer's reach + tempo end it before the clinch — closing is risky |
| vs that same rapier fighter, **in full plate** | **98%** | armour slows the spacer's tempo *and* the grapple bypasses the plate they rely on |

→ Exactly the historical logic: **you don't grapple a nimble unarmoured duellist — you grapple the armoured man.** Against him, the thrust that beats a duellist is the worst tool and wrestling-him-down is the best. ✓

## §3 — Historical precedent (the project's research + the record)

- **Fiore's *abrazare*** — "wrestling/grappling, the foundation under all weapon work" (the seven-axes doc). Grappling underlies the weapon game; closing to it is always available. ✓
- **German *ringen*** + **half-swording** — armoured combat resolved by closing, controlling, and thrusting the gaps. ✓
- **The rondel dagger** — the specialist gap-finisher for a downed/controlled armoured man (the §2A finish). It existed for exactly this. ✓
- **Judicial armoured combat** routinely ended in a grapple + dagger, not a clean weapon blow. ✓

## §4 — Honest limits (self-review)

- **Robust:** the dagger-finish bypassing mitigation (the third counter), Strength-dominance, the hands penalty, and the context split (lose to a spacer / beat armour). These follow from the structure and the canonical actions.
- **Exaggerated magnitude:** the **0%** unarmoured-vs-spacer result is too absolute — my model lets the spacer *always* win at range; real fights let a grappler sometimes close. The **direction** (grappling loses to a distance-keeper, beats armour) is validated; the exact percentage is not. A reviewer would soften the closing model so a grappler closes some fraction of the time.
- **Scope:** this is the **anti-armour grapple** (clinch / throw / disarm / dagger-finish), grounded in *abrazare* — **not** a full striking art (punches/kicks). Flagged as a deliberate scope bound, not an omission.
- The σ-magnitudes (grapple-per-STR, hands penalty, closing cost) are grounded seeds, not canon.

## §5 — Canon status

- **No canonical value changed** — Disarm/Tie Up/Escape/Retrieve are reused; this unifies them into the close-combat phase and fills the ED-129 unarmed gap.
- **New, flagged for ratification:** the **dagger-finish** (a controlled/prone foe takes a point strike on the gap profile, bypassing mitigation) — the one genuinely new mechanic.
- **Resolves** the third plate-counter, so plate's intended 1v1 dominance now has its full, historical set of answers (blunt / point / grapple).

`[GAP: a full unarmed striking system (not grappling) remains unbuilt — out of scope here; abrazare is grappling-centric. Flag if you want striking.]`
`[ASSUMPTION: the dagger-finish triggers off a won grapple (throw/control); flag if you want it gated behind a separate Tie Up + finish roll.]`
