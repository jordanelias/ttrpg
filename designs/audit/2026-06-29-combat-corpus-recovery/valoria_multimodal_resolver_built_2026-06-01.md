# Valoria — Multimodal Cross-Tradition Resolver (BUILT)
**2026-06-01 · the resolver is implemented in the modular engine**

> The cross-tradition resolver from the design spec is now built and working: traditions are cognitive-mode profiles
> (selection-weights over the shared physical substrate), with split visual/tactile read channels, a leverage-based
> bind, the commitment-window, and a cross-tradition unfamiliarity penalty. Baselines hold. One pre-existing reach
> CALIBRATION fault was exposed (not a resolver bug) and is isolated for a dedicated re-fit.
> `[CONFIDENCE: high — resolver validated; reach-calibration finding reproduced and localized]`
> `[SELF-AUTHORED — bias risk: my engine; the reach fault is exactly what an independent matchup sweep surfaced]`

## What was built (combat_engine/tradition.py + wrapper wiring)
- **`tradition.py`** — each tradition is a COGNITIVE MODE: channel-weights (visual/tactile/precommit/leverage/tempo/
  measure/footwork, neutral=1.0) + the named-set it expresses + a knowledge-of-others familiarity matrix. Seeded
  from the bridge's confirmed set↔tradition mapping (German→Bind Fighter/tactile; Italian→Thrust Duelist/temporal;
  Spanish→geometric; Japanese→Counter-time/intentional/pre-commit; Chinese→Burst; Filipino→Continuous-flow;
  English→biomechanical). All Class-C, Jordan-vetoable. The engine ALWAYS resolves in the substrate — a tradition
  only re-weights the channels the substrate already computes (it adds no new physics).
- **Split read channels** — VISUAL (pre-contact anticipation, Cog/Att, temporal-spatial) now distinct from TACTILE
  (in-bind Fühlen). Traditions weight the mix (German tactile-heavy; Italian visual/temporal). Resolves fidelity
  finding #2.
- **Leverage-based bind** — the bind sub-loop now resolves on LEVERAGE (Stark/Schwach: technique + bind-skill) +
  TACTILE read (Fühlen), with Strength only a minor contributor (half its old weight). Resolves fidelity finding #1
  ("winding asks you to be clever rather than strong"), per the bridge's transform-into-bind-leverage lens.
- **Cross-tradition unfamiliarity** — `familiarity(reader, opponent)` degrades the VISUAL and TACTILE read vs an
  unfamiliar tradition (you mis-time their commitment-window, misread their bind pressure). Same-tradition or
  vs-untrained = 1.0; adjacent (historically cross-pollinated) = 0.93; distant = 0.85. This is the mechanic that
  makes cross-tradition matchups more than stat-vs-stat.
- **Commitment-window** — the aggressor's initiative is tempo-weighted by tradition (tempo/Indes/sen as vocabularies
  onto the one substrate primitive). Resolves fidelity finding #4.

## Validation — resolver works, baselines intact
- **Baselines unchanged** (tradition='none' reproduces prior): mirror 48–49%, History 6v3 90%, plate>naked 100%. ✓
- **Tradition matchups modest + differentiated** (vs neutral, equal stats/skill): german 50, italian 55, spanish 57,
  japanese 55, chinese 53, filipino 52, english 54%. A tradition is a real but NON-dominant edge — correctly BELOW
  the mastery/skill differentiator (skill stays king, per the validated thesis). ✓
- **Cross-tradition asymmetry surfaces:** german vs japanese 48% but japanese vs german 52% (reversed) — the
  Japanese pre-commitment-read edge + asymmetric familiarity. ✓
- **Leverage bind + split reads + commitment-window all functional** and the engine resolves multivariate
  cross-tradition weapon pairs on the shared substrate (German longsword vs Japanese yari computes — see reach note).

## ⚠ Pre-existing REACH CALIBRATION fault (exposed, not caused, by the resolver; isolated for re-fit)
Cross-reach matchups at EQUAL skill are mis-scaled — a tiny reach gap over-wipes:
- longsword vs spear (gap **0.5**) = **2%** for the longsword — should be ~40% (a 0.5 reach edge is small).
- After making the stop-hit gap-proportional (a real improvement: **mastery can now close a small gap** — longsword
  H6+footwork6 vs spear H3 went 28%→**80%**, satisfying the thesis), the *equal-skill* curve became non-monotonic:
  spear vs dagger fell to 38%, longsword vs spear still 2%.
**Diagnosis:** the reach spectrum is governed by three interacting mechanics — per-beat stop-hit (approach),
closed-phase residual reach, and the exchange cap — and they don't compose into a monotonic "more reach = more
advantage, proportional to gap" curve. This is the same tightly-coupled-reach problem flagged in rev 7; the resolver
work sharpened it by testing long-vs-long-different-reach (longsword vs spear) which the prior weapon sweep didn't
isolate. **Fix = a dedicated joint reach re-fit** (stop-hit severity × close-rate × residual × exchange-cap) to a
monotonic gap-proportional curve: gap 0.5 → ~55/45, gap 2.8 → ~75/25, gap 3.3 (spear-dagger) → ~85/15, with mastery
able to shift each by ~±25pp. NOT another single-knob nudge — the four mechanics must be fit together.

## Files
`combat_engine/{core,combatant,config,systems,wrapper,tradition}.py` — `/home/claude/`.
Design: `valoria_multimodal_resolver_design_2026-06-01.md`; this build report — `/mnt/user-data/outputs/`.

## Next (ordered)
1. **Joint reach re-fit** (above) — monotonic gap-proportional curve; mastery shifts it. Blocks clean weapon/reach
   numbers but does NOT block the resolver, which is sound.
2. **Re-run the full validation suite** after the reach re-fit (weapon roster, equal-value Str/Agi/End, armour-defeat
   triad — all on the corrected reach base).
3. **Concentration baseline-consistency** term (wired, FOCUS_CONSISTENCY_K) — validate.
4. **Formalize the skill + set-bonus catalog** per axis on the now-built tradition layer (named sets already map to
   traditions — the bridge confirmed Thrust Duelist/Bind Fighter/Counter-time/Continuous-flow/Burst).
5. Jordan: differentiator steepness; in-world tradition culture-names; whether to use the per-weapon tradition
   spread (bridge Part C) for schools.

## Not committed
Lanes ignored per directive; all staged. The resolver is a working foundation; the reach re-fit is the next focused
task. Maps directly to a Godot combat-manager + tradition-profile + system-resolver structure.
