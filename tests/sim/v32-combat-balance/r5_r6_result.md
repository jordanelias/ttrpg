# R5 + R6 — Strength Leverage & Stamina Recomposition (armature reset, Build-5/6)

**Date:** 2026-05-29 · **Modules:** `r5_strength_stamina.py` (clean, self-test 6/6), `r6_equal_value_resweep.py` (in-progress harness — **not** a verdict) · **Status:** Class-C proposal; no canon file edited.

`[SELF-AUTHORED — bias risk: R5/R6 are this session's build. R6's field aggregate is reported as confounded/inconclusive rather than tuned to a passing number.]`

## What R5 implements (your two decisions)

**1 — Strength now has landing/control channels** (was dead at 23% in R4 with +0.00 σ-leverage). Five channels, two already canonical, three new:

| Channel | Type | Effect |
|---|---|---|
| Bind win | new (Class-C) | In-bind state: stronger fighter (+¼ Agi finesse) wins the bind → δσ. **Str's primary landing channel.** |
| Stagger | new (Class-C) | Heavy-weapon Overwhelming hit opens a σ-window on the victim's next defence — converts magnitude → tempo. |
| Stamina efficiency | new (Class-C) | Str above weapon STR-min lowers per-action stamina cost; below raises it. |
| Armour-defeat window | canon-derived | Heavy/blunt at STR-min vs armour opens a leverage window (half-sword/poleaxe logic), not just damage. |
| Wield penalty | **canonical** | 1 below STR-min → −1D pool; 2+ below → cannot wield. |

Self-test confirms the fix: **Str leverage now +0.88 in-bind / +0.38 closing** where R4 measured **+0.00**. In single-loadout matchups Str now *beats* Agi decisively (2072–927) and dominates its heavy-blunt-vs-plate niche (2666–331). The dead-stat finding is structurally resolved — Str has a landing game.

**2 — Stamina = f(Endurance, Spirit)** replacing canonical `Stamina = Endurance × 5`:
- `Stamina = 3·End + 2·Spirit` (End3/Spi3 = 15, matching the old End3 value; End keeps a per-point premium).
- **Spirit gains its first combat role** (energy reserves / sustain), per your clarification that Spirit is base tenacity/fortitude, not thread-only.
- **Endurance loses its action-economy monopoly** — it kept *both* Health-depth and Stamina, which was the R3/R4 End-dominance source. Splitting Stamina to (End + Spirit) directly attacks that.
- Stamina depletion drives the **canonical** Out-of-Breath −2D inside the phrase, so the action economy is now a real in-fight factor.

## What R6 does NOT yet show (honest limitation)

R6 re-runs the six-attribute parity sweep with R5 wired in. **Its field-rate aggregate is confounded and is not a verdict:**
- Single-loadout traces show Str's channels working (above).
- But the field sweep averages over shared weapon/armour loadouts; when both fighters carry the same loadout, the armour-defeat/weapon-class terms **cancel**, erasing Str's niche and producing a misleading field rate (Str 6.6%).
- The harness needs **per-loadout isolation + asymmetric-loadout matchups** (a Str-heavy build *choosing* a mace vs an Agi build *choosing* a rapier) before its field numbers mean anything. As-is it answers the wrong question (mirror-loadout duels) for several attributes.

So: **R5's mechanics are validated; R6's equal-value verdict is pending a harness fix.** I did not tune R6 to a passing number — that would be fabricating parity from a broken measurement.

## Canon-level items for your ratification (flagged, not edited)

1. **Stamina formula change** — `Stamina = Endurance × 5` → `3·End + 2·Spirit`. This edits a canonical derived score (derived_stats §4.2). Committed as a Class-C **proposal**; needs your ratification to become canon (and an editorial-ledger entry).
2. **Spirit's definition expansion** — from metaphysical/thread to "base tenacity/determination/fortitude/energy reserves with combat-relevant reserves." This widens a canonical attribute's role; worth a canon note (editorial ledger).
3. **Bind-as-Str-contest + Stagger** — new combat mechanics. The In-bind state and Overwhelming degree are canonical; the Str-contest weighting and stagger window are new. Full N/Ω/Μ vetting territory before canon.

## Next

Fix R6's harness (per-loadout isolation + asymmetric loadouts + weight Str's channels against the corrected baseline), then re-run the six-attribute parity. That's the path to a trustworthy equal-value verdict and the omega Class-A vetting block. The R5 channels are the substrate; the harness is the remaining work.

`[CONFIDENCE: high — R5 channel mechanics + Stamina recomposition are self-test-verified and canon-grounded. low — R6 field aggregate (confounded; flagged inconclusive).]`
`[ASSUMPTION: Stamina coefficients 3·End/2·Spirit seeded to match the old End3 value; sim-tunable, your calibration.]`
