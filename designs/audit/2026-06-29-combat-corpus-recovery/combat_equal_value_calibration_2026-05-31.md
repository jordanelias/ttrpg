# Combat Equal-Value Calibration — Str/Agi/End, full mechanics
**2026-05-31 · personal combat (duel context) · σ-leverage engine + unified damage**
[SELF-AUTHORED — bias risk: this calibrates a model this session built; an independent reviewer's caveats are surfaced in §7.]

---

## VERDICT

**Str = Agi = End equal-value: ACHIEVED.** On identical optimal duel gear, the win-value of a point in each of the three physical stats is equal — group means **Str-lead 50% / Agi-lead 50% / End-lead 50%** across all no-1 allocations summing to 12. Any combination (no stat at 1, optimized gear) is ~50% against any other.

**Differentiator = martial-tradition mastery + assigned skills: CONFIRMED.** Holding the body identical, the skill axis (History pool, coherence/named-set, Reading) is what moves the win rate — monotonically and decisively.

**All components wired: DONE.** The integration sim now includes the three ratified components R8 omitted — W2/W3 weapon-tempo, A1 armour-tempo, m5 stance/reaction/coherence — plus the unified damage model.

**Open for Jordan: 5 items** (§7), the load-bearing two being the **fight-model decision** (single vs multi-phrase duel) and **how steep the skill differentiator should be**. Seeds are **staged, not committed** — this session holds no write lane.

---

## 1. SCOPE & WHAT WAS WIRED

The balance target (your spec): *any Str/Agi/End allocation with no stat at 1, each with optimized equipment, has ~the same chance against any other; the differentiator is the extent of martial-tradition mastery and the skills assigned in the build.* The test is a 1v1 duel.

The verified R8 parity harness was the integration oracle, but it **omits three ratified armature components**. They had to be wired in for an "all components" test:

| Component | Source | What it does | Why it mattered here |
|---|---|---|---|
| **W2/W3** weapon-tempo | `r9_weapon_engagement` | reach governs the approach, speed governs the bind; a slow weapon is disadvantaged every duel phase | gives fast/finesse weapons their duel edge; war hammer correctly weak in a duel |
| **A1** armour σ-tempo | armature addendum (seed 0.5·minor/drain) | armour costs initiative/tempo, scaled by weight | **the key fix** — without it heavy armour is free and universal |
| **m5** stance/reaction/coherence | `m5_stance_reaction_coherence` | RPS stance counter (reading-driven), reaction vs commit-depth, named-set coherence bonus | the skill differentiator channels |
| unified damage | this session's ratification candidate | force-cap + quality-outside-cap; no one-shot | replaces the multiplicative one-shot tail |

Harness: `eqval_harness.py` (all channels, parameterized by a seed dict).

---

## 2. DIAGNOSIS — why the uncalibrated full model was imbalanced

Running all components at seed 1.0 produced a 61–66-point win-rate spread. The cause was **not** a Str/Agi/End leading-stat bias (group means were already close). Two structural defects:

1. **Universal-heavy-armour degeneracy (missing A1).** With armour free, every build wore heavy plate; against universal plate the war hammer's anti-plate coupling dominates — the C1 *battlefield* dynamic leaking into a duel. The spread was bimodal **by weapon** (war-hammer wielders 66–75%, everyone else 9–49%), not by stat.
2. **End negatively valued.** Builds that *dumped* End to 2 outperformed; builds that maxed End lost. The unified-damage force-cap was scaled to the **defender's** WI, so tougher targets took proportionally bigger hits — eroding the very Health advantage End buys.

---

## 3. THE CALIBRATION

Three structural corrections, then channel tuning:

- **Wire A1** (armour costs tempo) → heavy armour becomes a real sacrifice → armour meta diversifies → war hammer stops auto-winning. (spread 61→25)
- **Baseline-scale the force-cap** (`cap = 1.2·WI(baseline)`, not the defender's WI) → End's Health advantage is no longer eroded; the sign on End's value flips positive. Still no one-shot for any non-dump build.
- **Lower the cap baseline to End 3** → fights run slightly longer, so durability (End) pays off → End reaches parity.
- **Trim the over-stacked Str channels** — Str alone carried bind-σ + stagger + armour-defeat + pressure + heft + weapon access. Scaled `strength_leverage ×0.6`, `stagger ×0.45`, `pressure ×0.55`.

### Locked seeds (Class-C, sim-tunable)

| Seed | Value | Channel |
|---|---|---|
| `str_lev` | **0.60** | strength_leverage_dsig (bind + stagger-setup + armour-defeat) scale |
| `str_press` | **0.55** | STR_PRESSURE_PER_POINT scale (→ 0.0172/pt) |
| `stagger` | **0.45** | STR_STAGGER_WINDOW scale (→ 0.1125) |
| `armor_tempo` | **2.00** | A1 armour σ-tempo scale (→ heavy 0.50δσ, medium 0.25δσ per attack) |
| `CAP_END` | **3** | unified force-cap baseline (→ flat cap 10.8) |
| `agi`, `wtempo`, `stance`, `react`, `coh` | **1.00** | unchanged from their module seeds |
| `read_k` | **1.5** | Reading→stance/reaction policy-quality scale |

Note `armor_tempo = 2.0` makes heavy armour a **0.50δσ per-attack** tempo cost — high, and correct *for the duel* (where tempo is the currency). In battlefield context (C1) armour's value rises / tempo matters less, so this scale is context-specific, not global.

---

## 4. RESULT — equal-value confirmed

### (a) Fixed-gear (identical optimal duel kit, no optimizer noise) — the clean physical-channel test
`N=4000/pair`. **Group means: Str-lead 50% / Agi-lead 50% / End-lead 50%. Spread 13 (43–56%), unbiased by stat.**

```
S3A5E4 56  S3A4E5 54  S2A5E5 53  S5A3E4 53  S5A5E2 50
S5A2E5 50  S5A4E3 49  S4A4E4 47  S4A3E5 46  S4A5E3 43
```

### (b) Best-loadout (each build optimizes its own gear — your literal spec), 3-seed average
**Group means: Str-lead 47% / Agi-lead 49% / End-lead 51%. Spread 21.** The meta collapses to a fencing loadout (fast thrust + light/no armour) — the correct duel meta per C1 (heavy gear is battlefield kit). The lone outlier, S4A4E4 at 39% (±6), is the one-step loadout optimizer occasionally mis-picking its weapon — a harness artifact (the same build is 47% on fixed gear), not a real imbalance (§7.3).

**Reading the two together:** the physical channels are balanced (fixed-gear is dead-level); the wider best-loadout spread is optimizer noise, not stat bias.

---

## 5. DIFFERENTIATOR — martial tradition + skills

Identical 4/4/4 body and gear; opponent fixed at baseline (History 2, Reading 3, no tradition). Only the skill axis varies:

| Skill axis | Win rate vs baseline |
|---|---|
| **History (mastery → pool)** | 0→**22%** · 2→51% · 4→**72%** · 6→**85%** · 8→**91%** |
| **Coherence (assigned tradition)** | none→49% · moderate set→**94%** · strong set→**98%** |
| **Reading (Cog/Att)** | 2→**9%** · 3→49% · 4→**91%** · 5→**99%** |
| **Combined trained vs untrained** | moderate→**100%** · strong→**100%** |

Skill is unambiguously the differentiator: with physical stats held equal, mastery + assigned skills decide the fight, monotonically.

**FINDING (P2) — the skill channels are steep.** A single Reading point (4 vs 3) → 91%; one moderate tradition → 94%. Two contributors: (i) real — σ edges compound over the decisive phrase (L1 leverage→degree); (ii) artifact — coherence is wired as a **flat per-strike** bonus, whereas m5's named sets are **state-gated** (`applies_to` specific states/actions), so the live game would apply it less often. *How steep the differentiator should be is a design decision (§7.2).*

---

## 6. SAFETY (re-verified under the locked seeds)

| Property | Result |
|---|---|
| No one-shot | max single blow **16** (OW heavy-blunt, Str5 vs unarmoured End2) < End-2 Health **24**; ~2 blows worst case, ~4 typical (armoured End4). PASS |
| Decisive (R2) | mean **9.8 strikes**; 77% produce a decisive winner |
| Small-pool robust (L3) | floor-pool mirror (History 0, 6D) = **51%** (fair at the floor) |
| Skill gap bounded | 14D vs 6D = 98% (steep but not unbounded) |
| Death-spiral (L5) | damped — fights resolve within the phrase, no runaway |

Wrinkle: at CAP_END=3, ~**23% of equal-build duels end in an equal-wound draw** (excluded from win rates). In a real duel these would continue — which is the argument for §7.1.

---

## 7. OPEN ITEMS FOR JORDAN (severity-ranked)

**7.1 [P1 — design decision] Single-phrase vs multi-phrase duel.** Equal-value was reached partly by lowering the cap (CAP_END=3) so the single decisive phrase runs long enough for End's durability to pay off — at the cost of a 23% draw rate. The cleaner model is likely a **multi-phrase duel** (Health/stamina persist, exchanges continue until someone falls): it would resolve the draws *and* value End naturally, possibly allowing a less-aggressive cap (CAP_END=4) with more decisive single phrases. This touches R2 ("one decisive phrase") — your call. I can test it on request and report whether it gives equal-value with fewer draws.

**7.2 [P2 — design decision] Skill-differentiator steepness + coherence state-gating.** The differentiator works but is steep (§5). Two sub-items: (a) decide the intended steepness (should +1 Reading be ~90% or ~60%?); (b) the coherence bonus should be **state-gated per m5** (`applies_to`) rather than flat-per-strike — that's a wiring-fidelity fix that also lowers steepness. Both are seed/wiring tunes, not structural.

**7.3 [P3 — harness] Best-loadout optimizer noise.** The one-step best-response optimizer (vs default-gear opponents, MC-estimated) occasionally mis-picks near-equal loadouts (S4A4E4). Cosmetic for the verdict (fixed-gear is clean); fix is a fixed-point loadout solve or higher trials if a publication-grade best-loadout table is wanted.

**7.4 [confirm] Unified-cap change.** This calibration changes the unified model's force-cap from defender-scaled to **baseline-scaled (CAP_END=3)** — a Stage-4-style re-test correction (defender-scaling eroded End). Confirm before it folds into the unified-damage ratification candidate.

**7.5 [carried] W4 supersession.** The KEEP-Heavy-Blunt-×3 directive (W4) is superseded by the no-one-shot unified model; the war hammer's identity now lives in its battlefield (C1) dominance, not a ×3 one-shot. Confirm.

---

## 8. STAGING NOTE

All of the above is **staged, not committed.** This session declared no write lane; the locked seeds are Class-C values that belong in the combat params / armature ledger (Lane A) and the sim modules (Lane C). On your go, the seed table (§3) and the cap change (§7.4) route through the owning lane's commit path with a `Citations:` block. No canon, params, or sim files were written.

**Evidence trail:** all numbers from the verified v32 modules (r1/r2/r5/r8/r9/m1/m3/m5/m7) run locally + the unified damage model; MC up to N=4000/pair, differentiator/safety at N=4000. `[CONFIDENCE: high]`
