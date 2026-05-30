# R3 Parity Sweep — Result (armature reset, Build-3)

**Date:** 2026-05-29 · **Module:** `tests/sim/v32-combat-balance/r3_parity_sweep.py` · **Status:** Class-C proposal result — no canon edited. Flagged for Jordan.

`[SELF-AUTHORED — bias risk: R1/R2/R3 are this session's build. The sweep was run with nothing tuned to pass; it reports the model as NOT-yet-balanced rather than massaging the Class-C seeds to green.]`

## Headline

Run honestly (symmetric, equal physical-triad budget, N=4000/matchup, Wilson 95% CI, one decisive exchange — not attrition):

| Build (equal 9-pt physical triad) | vs field | CI | verdict |
|---|---|---|---|
| Agi-heavy (Agi5/Str2/End2) | **40.1%** | [39.1, 41.2] | ok (now the *weakest*) |
| Str-heavy (Str5/Agi2/End2) | 46.5% | [45.4, 47.6] | ok |
| End-heavy (End5/Agi2/Str2) | **63.4%** | [62.4, 64.5] | **DOMINANT** |

## What this means

1. **The original C-04 is CLOSED.** Agility no longer dominates — the demoted, Agility-independent pool (R1) removed the base-rate channel the M8b re-sweep pinned. Agi is now the *weakest* equal-budget build (40%). The σ-leverage tempo channel (AGI_TEMPO_PER_POINT) is currently under-tuned, but the dominance defect Jordan named is gone.

2. **Dominance MOVED to Endurance, not eliminated.** End-heavy wins the field at 63.4% (CI excludes the band). Cause: on a one-exchange *decisive* model, End's wound-gate depth (Health 44 vs 24 — nearly double the trades survived) outweighs Str's damage multiplier and Agi's tempo. **This reproduces an independent prior finding** — PP-717's sim note recorded "Endurance the dominant stat investment at all armour tiers (69–82% win rate for End-6 builds)"; the MW≤3 cap reduced it but, under this decisive single-exchange resolution, End still wins.

3. **The correctly-framed C-04 (Ω-d / М-6 "no dominant strategy") does NOT yet pass.** It is closed on the Agi axis but failed on the End axis. The parity target is all-three-in-band; we are one knob away.

## The localized knob (for Jordan — Class-C, sim-tunable)

The sweep is the tuning oracle. To equalize, the End wound-gate channel must be down-weighted relative to Str/Agi, OR Str/Agi up-weighted. Concretely, in rank of leverage:

- **End channel (the dominant one):** the Health-depth advantage (44 vs 24) is doing the work. Options: (a) make the decisive threshold less End-favoring (a clean strike crosses gates faster, compressing the Health advantage); (b) widen Str's multiplier payoff so the extra Health is offset by harder hits; (c) reduce the per-wound survivability edge.
- **Agi channel (under-tuned):** raise `AGI_TEMPO_PER_POINT` (currently ½·Minor) so tempo/initiative buys more — Agi at 40% has room.
- **Str channel (near-band):** Str-heavy at 46.5% is close; small multiplier or armour-defeat uplift.

**These are the equal-budget tuning levers the parity sweep exists to turn. I am not turning them** — the magnitudes are a balance decision (Class-C → Jordan calibration), and the project-owner contract bars me from retconning balance. The harness will re-verify after each turn.

## Boundaries / honesty flags

- `[ASSUMPTION]` one exchange = up to 6 alternating sub-actions, decisive at first wound. Equal-budget = equal *physical-triad* point sum (Agi+Str+End held at 9); mental/social/metaphysical points untouched (not contested by combat).
- `[ASSUMPTION]` base sub-action Ob = 3 (canonical degree band centre); medium armour, equal weapon (long_cut_and_thrust), History 2 across all builds.
- `[GAP]` the full Agi σ-leverage stack (Reading window, Reaction matchup, Facing — M5/M7) is not yet wired into the sweep; only the R1 tempo δσ is. Agi's real ceiling is higher than 40% once those compose. Build-4 should wire them before the final parity call.
- `[GAP]` weapon/armour *variety* not swept here (single loadout); the M8b axis (weapon category) is held constant to isolate the attribute axis. A full sweep crosses both.

## Next

Build-4: wire the full Agi σ-leverage stack (M5 stance/reaction + M7 facing) + sweep weapon/armour variety, then re-run parity. The End-dominance knob is **Jordan's calibration call** (decision B-adjacent: the Str/End/Agi channel magnitudes) before the omega Class-A vetting block can claim Ω-d passes.
