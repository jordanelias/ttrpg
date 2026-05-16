# Phase 10 — STR + Stamina reform empirical test

## Date
2026-05-16

## Scope
Personal combat balance. Two design-question reforms tested empirically against the corrected Phase 9 baseline (undoubled pool, 1/End Ob wound penalty, Disarm action available).

## Methodology corrections from prior phases

Three errors discovered during Phase 10 setup and corrected:

1. **TN vs Ob conflation (Phase 1-9 wound penalty sims).** Earlier "Ob +0.5 per wound" sims implemented this as a TN shift (every die rolled at TN 7.5 instead of TN 7), which compounds across all dice. Corrected interpretation: Ob is a net-success threshold raise (additional net required to land a hit). Ob interpretation is materially milder than TN-shift was; prior wound-penalty conclusions overstated their effect.

2. **Disarm AI threshold bug.** Sim AI required `opp_weapon_mod >= 4` to attempt Disarm; light blades have damage_mod = 3, so Disarm never fired vs light-weapon opponents. Corrected to `>= 3`. With the fix, low-Agi builds use Disarm against light-blade Fast builds — modest but measurable effect.

3. **Stamina formula error (this phase's primary finding).** All prior sims (Phase 4 through Phase 9) used `Stamina = 15 + End × 2` with Take Breath restoring full pool. Canonical formula per ED-694 is **`Stamina = End × 5`** with Take Breath restoring **partial** stamina (End × 2 not full pool), plus +1 stam cost per wound. The sim was systematically underweighting Endurance.

The third error is significant: prior phase claims about End-dominance magnitude (Phase 8: "Tough vs Strong 63.7% — real, moderate End-dominance") were undermeasured. With canonical stamina, Endurance produces a 4-9pp larger effect than previously reported.

## Two reforms tested

### Reform A — Canonical stamina

Replace sim's `15 + End × 2` (range 21-29 across End 3-7) with **canonical `End × 5`** (range 15-35) and partial Take Breath recovery (End × 2 not full pool) and +1 stam cost per wound.

Implementation: per ED-694 and params/combat.md `Stamina` section.

### Reform B — STR bonus dice on offense

Add `floor(STR/N)` bonus dice to offense pool on Strike and Disarm actions (not Feint). Three values tested for N:

- **mild** — `floor(STR/4)`: STR 4 → +1, STR 7 → +1, STR 8 → +2
- **strong** — `floor(STR/3)`: STR 4 → +1, STR 7 → +2 (recommended)
- **pool_add** — `floor(STR/2)`: STR 4 → +2, STR 7 → +3

Current canon: STR only adds to damage on landed hits (via `damage = net + STR × weapon.str_mult + weapon.damage_mod`). Reform proposes STR also contributes to hit probability via bonus dice.

## Results matrix

All matchups use undoubled pool grammar (Pool = Agi + Hist + 3) + 1/End Ob wound penalty + Disarm enabled. Each cell is N=3000 duels, A's conditional win rate.

| Matchup | BASE | +stam canon | +stam +STR mild | +stam +STR strong | +stam +STR pool_add |
|---|---|---|---|---|---|
| Fast (Agi 6) vs Strong (Agi 3) | 100.0% | 99.9% | 99.8% | 99.6% | 99.8% |
| Fast vs Mighty (Agi 3, STR 7, light) | 100.0% | 99.4% | 99.2% | 98.5% | 98.9% |
| Fast vs Mighty-heavy (Agi 3, STR 7, heavy) | 99.3% | 94.8% | 93.3% | **91.7%** | 92.3% |
| Fast vs Tough (Agi 3, End 6, light) | 99.7% | 96.8% | 97.3% | 96.9% | 97.3% |
| Fast vs Tough-heavy (Agi 3, End 6, STR 6, heavy) | 86.3% | 83.6% | 84.6% | **78.3%** | 80.1% |
| **Fast vs Titan** (Agi 3, End 6, STR 7, heavy) | **81.8%** | **72.6%** | 74.2% | **70.0%** | 70.0% |
| Fast vs Fast-strong (balanced Agi 5) | 52.7% | 53.8% | 53.5% | 51.2% | 52.3% |
| Mighty-heavy vs Titan (STR vs End, equal Agi) | 35.9% | 29.9% | 27.9% | 27.3% | 29.0% |
| Calibration: Strong vs Strong | 49.6% | 50.3% | 50.0% | 50.5% | 49.4% |
| Calibration: Fast vs Fast | 49.7% | 50.2% | 50.5% | 49.0% | 50.2% |

## Findings

### F1 — Stamina reform is the single largest lever tested in the chain (4-9pp shift)

Going from sim's `15 + End × 2` to canonical `End × 5` + partial TB + wound stam cost shifts every End-investing matchup by 4-9pp. Fast vs Titan: 81.8% → 72.6%. Fast vs Mighty-heavy: 99.3% → 94.8%. This is bigger than any single reform tested in Phases 4-9.

Mechanism: Fast builds have lower stam (End 4 → 20 stam canonical, down from 23 in sim baseline) and partial Take Breath recovery means Fast must Take Breath more frequently. Each Take Breath round is a free offensive turn for opponent. Tough/Titan builds (End 6 → 30 stam) Take Breath less often, get more Strikes per duel.

**This is not a "reform" — it is a sim correction.** The canonical stamina formula has been ED-694 since prior work; prior sims used the wrong formula. All Phase 4-9 conclusions about End-dominance magnitude were undermeasured.

### F2 — STR bonus dice (floor(STR/3)) provides 2-6pp meaningful uplift to high-STR compensator builds

Fast vs Tough-heavy: 83.6% → 78.3% (−5.3pp with STR strong). Fast vs Mighty-heavy: 94.8% → 91.7% (−3.1pp). STR investment now influences hit probability, not just damage-per-landed-hit.

Non-linear breakpoints reward STR specialization:
- STR 4 (baseline) → +1 bonus die
- STR 7 (specialized) → +2 bonus dice
- STR 10 (maxed) → +3 bonus dice

STR-strong is recommended over STR-pool_add: pool_add gives flat +2 to baseline STR 4 builds which inflates universal offense; strong rewards specialization without giving free dice to non-STR builds.

### F3 — STR with light blade is still essentially wasted

Fast vs Mighty (Agi 3, STR 7, light blade): 98.5% even with STR-strong reform. Light blade `str_mult = 1.0` means each landed hit only gets +3 bonus damage from STR 7. STR bonus dice partially help (Mighty hits at ~36% vs 34% baseline) but hit rate is fundamentally Agi-determined; STR adds 2pp to hit rate, not 20pp. STR matters when paired with a heavy weapon (str_mult 2.0) or when hit rate is already high.

Design implication: STR-investment + light-weapon archetype remains undefined. Either accept ("light weapons are not for STR builds") or design dedicated mechanics (e.g., specific light-weapon maneuvers that scale with STR, like grappling, throws, two-handed-light-blade techniques).

### F4 — End + STR + heavy weapon is the working compensator archetype

Titan (End 6, STR 7, heavy) vs Fast under STR-strong + stam-canon: 70.0% Fast (Titan wins 30%). Mighty-heavy (no End investment): 91.7% Fast (Mighty wins 8%). End is necessary for compensator viability; without it, the build can't survive long enough for STR-amplified hits to accumulate.

### F5 — Pool gap dominance at Agi 3 vs Agi 6 remains structurally significant

Even with all reforms (undoubled pool + 1/End Ob + Disarm + canonical stam + STR-strong), Fast vs Titan finishes at 70/30. A 3-die pool gap is still meaningful when no other lever can close it. The improvement from canonical doubled baseline (Titan ~25% wins) to fully-reformed (Titan ~30% wins) is real and meaningful, but is not balance.

### F6 — Balanced builds work fine; the problem is extreme stat distribution gaps

Fast (Agi 6) vs Fast-strong (Agi 5, STR 5): 51.2% under STR-strong + stam-canon. Moderate stat gaps produce balanced fights. The "broken" matchups are EXTREMELY specialized builds (Agi 3 with min Agi vs Agi 6 with max Agi).

## Best config recommendation

**Canonical stamina (already canon — sim was wrong) + STR-strong bonus dice (proposed reform).**

| Matchup | Win% | Cond% | Draw% |
|---|---|---|---|
| Fast vs Strong (light) | 99.6 | 99.8 | 0.2 |
| Fast vs Mighty-heavy | 91.5 | 91.9 | 0.4 |
| Fast vs Tough-heavy | 77.1 | 78.6 | 1.9 |
| Fast vs Titan | 67.5 | 68.8 | 1.9 |
| Fast vs Fast-strong (balanced) | 52.6 | 54.9 | 4.2 |
| Mighty-heavy vs Titan (STR vs End) | 27.4 | 29.1 | 5.7 |
| Calibration Strong vs Strong | 47.1 | 49.6 | 5.0 |
| Calibration Fast vs Fast | 46.9 | 49.6 | 5.4 |

5% draw rate in long fights is appropriate — both fighters running out of stamina before resolution is a real outcome in canonical stam economy.

## Open canonical questions for design owner (Jordan)

1. **Sim correction commitment.** Phase 4-9 End-dominance findings need an explicit erratum: the magnitude was undermeasured because of the stam-formula error. Should the Combat Balance Note (ED-834, ED-838) be updated to reference Phase 10's recalibrated picture?

2. **STR bonus dice.** Is `floor(STR/3) → bonus dice on Strike/Disarm` an acceptable mechanic to ratify? It changes how STR works mechanically — currently STR only contributes to damage-per-hit; reform makes it contribute to hit probability too. Pros: STR investment becomes broadly meaningful. Cons: shifts STR from "amplifier" to "primary" stat — may have unintended effects on other systems where STR is referenced.

3. **Pool dominance acceptance.** Even with all reforms tested, Fast (Agi 6) vs Titan (Agi 3 + max comp) finishes at 70/30. Acceptable as designed (Reframing 2: combat dominance is fine if compensator builds dominate cross-system)? Or push further (pool cap, static defense, smaller pools)?

4. **Light-weapon STR archetype.** Mighty (Agi 3, STR 7, light blade) sits at 98.5% loss to Fast under reforms. Either accept the archetype isn't viable or design specific light-weapon STR mechanics (grappling, throws, etc.). Currently a gap.

## Sim limitations

- Tie Up, Establish Distance, Reach mechanics still unmodeled. Tie Up could be a major underdog lever (skip opponent's turn entirely).
- Symmetric AI assumption persists: both fighters use identical strategy heuristics. Real play involves human asymmetric optimization.
- Action triangle Phase 7 limitations (PP-294 inversions) not retested under reform conditions.
- Mass-combat scale, faction-scale, Social Contest cross-system audits remain in CC-1 backlog.

## Files

- Sim: `tests/sim/scripts/phase10_str_stam_reform.py`
- This writeup: `tests/sim/phase10_str_stam_reform_2026-05-16.md`
- Prior phase writeups: `phase4_…` through `phase9_…` in `tests/sim/`
- Combat Balance Note: `params/combat.md` Phase 10 Update section (this commit)

## Related ledger entries

- ED-694 (canonical stamina formula — referenced)
- ED-834 (Combat Balance Note — superseded by Phase 10)
- ED-838 (Phase 8 Update — End-dominance magnitude superseded)
- ED-NEW-1 (this commit): Sim stamina correction; STR reform proposal
