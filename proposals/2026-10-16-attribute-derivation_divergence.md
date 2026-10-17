# Attribute derivation: the divergence test, executed on the equivalent pairs

## Status: PROPOSED (2026-10-16). Not ratified. Merging it ratifies nothing unless Jordan so rules. An executed test of the one grouping (`_part3` §8.1) and the relations inside each group (`_equivalences` §2); it edits no code, registry or ledger, and the choice of primaries stays Jordan's.
## Lane: IN (cross-cutting). IDs: none allocated. Read and run at the working tree of 2026-10-16.
## Parts: [head](2026-10-16-attribute-derivation.md) · [`_part2`](2026-10-16-attribute-derivation_part2.md) · [`_part3`](2026-10-16-attribute-derivation_part3.md) · [`_aptitudes`](2026-10-16-attribute-derivation_aptitudes.md) · [`_equivalences`](2026-10-16-attribute-derivation_equivalences.md) · **this file**.

**What this answers.** Jordan, 2026-10-16: *"run the divergence test on the equivalent pairs"*, after
the Opus critique and its correction. The frame is the derivation's: any item may be an attribute; no
prior ruling (J-13, the ten attributes, V-2/V-3, the 2026-09-05 ruling, *"Balance is not a stat"*)
constrains a verdict; nothing is *derived* except relative to a chosen set, and the registry's nine are
not assumed to be the primaries; learned skills and computed quantities are folded in.

**The test.** Two candidate primaries X and Y (or a primary and a demand grouped under it) are

- **SEPARABLE** if some resolver gives different outcomes when only X's ingredient varies than when
  only Y's varies, beyond the control band, in a different *mix* of outcome metrics;
- **IDENTICAL-BY-CODE** if every resolver reads them only through one shared input or one shared
  expression, so no resolver can hold one fixed and vary the other (shown by a grep of every reader,
  and where possible by a run whose arms are byte-identical on every seed);
- **SEPARABLE-ONLY-BY-MAGNITUDE** if they move the same metrics in the same direction by different
  amounts, so that one rescaling of Y reproduces X;
- **NOT TESTABLE** if either has no code reader, or (stated where it applies) has a reader that moves
  no outcome; the design that reads it is named.

**Everything below was executed.** The scripts and their saved outputs are in the session scratchpad,
`/tmp/claude-0/-home-user-ttrpg/3f6de207-94f6-530b-a5b4-52aac53c2712/scratchpad/div/`, script first and
output beside it; the numbers that carry a verdict are quoted here, because that directory is not part
of the tree.

| probe | script | saved output | resolver run |
|---|---|---|---|
| 1 | `combat_div.py` | `combat_div.txt`, `.json`, `.log` | personal combat, `modules/combat` `wrapper.fight` |
| 1b | `combat_channels.py` | `combat_channels.txt`, `.json` | the same, one ingredient split into its channels |
| 1c | `combat_wil_identity.py` | `combat_wil_identity.txt` | the same, Spirit against its derived figures |
| 1d | `profile_test.py` | `profile_test.txt` | analysis of 1 and 1b: is one arm a rescaling of another |
| 2a | `massbattle_command_reach.py` | `massbattle_command_reach.txt` | mass battle, the ten-row `bat.py` battery at Command 1 / 4 / 7 |
| 2b | `massbattle_div.py` | `massbattle_div.txt`, `.json`, `.log` | mass battle, a general's Charisma and Cognition, `bat.py`'s `oblique` row |
| 3 | `contest_div.py` | `contest_div.txt`, `.json` | the contest kernel, `resolver.py` `Bout`; the season loop's sigma roll |
| 4 | `threadknot_div.py` | `threadknot_div.txt`, `.json`, `.log` | threadwork Weaving, Leap, collective; knot formation |
| 5 | `grep_proofs.sh` | `grep_proofs.txt` | every non-test Python reader of each ingredient |

**Fan-out.** None. This lane holds no agent-spawning tool, and the four resolvers share one baseline
person, one statistic and one verdict rule, so a helper per resolver would have bought parallel
reading, not independent judgment. Independence on the verdicts is the orchestrator's critic stage.

---

## 1. Step 1: the code ingredient each demand maps to

[CHECKED] means the line was opened in this pass; [grep] means it was seen only as a grep hit
(`grep_proofs.txt`). Paths: `cs` = `modules/combat/combat_systems.py`, `cb` = `modules/combat/combatant.py`,
`wr` = `modules/combat/wrapper.py`, `ops` = `systems/threadwork/sim/operations.py`, `kn` =
`systems/fieldwork/sim/knots.py`, `res` = `systems/social_contest/sim/contest/resolver.py`.

| group | demand | code ingredient(s) | reader | tag |
|---|---|---|---|---|
| STR | strength | `Combatant.strength` | handling `cs:178-180`; half of Balance `cs:188`; wind `cs:349`; Health term `cb:40-42` | [CHECKED] |
| | | | bind `cs:1062`; percussion `cs:1239`; impact `core.py:663`; grab `contact.py:46` | [grep] |
| AGI | quickness | `agi` | tempo `cs:113`; initiative `cs:1416-1421` | [CHECKED] |
| | reflexes | `agi` (2), `att` (1) | `cs:172`; parry and dodge `cs:332-347`; counter `cs:1438-1443` | [CHECKED] |
| | balance | `agi` (½), `strength` (½), skill | `cs:184-189` | [CHECKED] |
| | dexterity | none | no Python reader names it; registry alias only | grep |
| END | stamina | `end` (3), `spirit` (2) | `cb:45-47`, `:126`; reset `wr:21-24`; recovery `wr:522` | [CHECKED] |
| | toughness | `end`, `spirit` (0.4), `strength` (0.25·S·E) | `cb:30-42`, `:59-63`, `:122`; re-derived at fight start `wr:498` | [CHECKED] |
| | hardiness | none | FW:239 (design) | grep |
| (state) | BODY | `Person.body` → `end` | `engine/season/seam/wrappers/combat.py:130-138`; `modules/combat/fight.py:45` builds `Combatant(a_id, end=a_end)` and nothing else; `engine/season/decision/budget.py:64-76` | [CHECKED] |
| FOC | concentration | `focus` (3), `spirit` (2) | `cb:147`; consistency and mental fatigue `cs:1423-1431`; drain `wr:523` | [CHECKED] |
| | (Focus's other readers) | `focus` | poise regathering `cs:1433-1436`; disruption `cs:1449-1452` | [CHECKED] |
| ACU | anticipation | `cog` (2), `att` (1), `history` | Reading `cs:171`; read at `cs:331`, `:1420` | [CHECKED] |
| | | | `cs:958-998`, `:1057-1059`, `:1130-1131`, `:1342` | [grep] |
| | reasoning (collective) | `cognition`, else `spirit` | helper dice `floor(Cognition/2)`, `collective.py:62-68` | [CHECKED] |
| | reasoning, observation, spatial-sense, land-sense | none | FW:90, :93, :304; settlement and governance designs | grep |
| CHA | leadership, situational-awareness, tactical-read | `charisma` (2), `cognition` (1) → `command` | `derive_command`, `modules/mass_battle/core/exchange.py:57-65`; called only at `units.py:2716-2717`, `:2810-2811` | [CHECKED] |
| | | `command` | `orchestration.py:322-327`, `:2224`, `:2251`, `:2589`, `:2598`, `:2834`; `core/state.py:95-105`; `units.py:2815`, `:2893`, `:2969-2971` | [grep] |
| | presence, persuasiveness | `charisma` (contest) | Face only: `res:185-195`, `:213`, `:230-236` | [CHECKED] |
| | judgment | none | governance_play_redesign_v1:64 (design) | grep |
| WIL | will | `spirit` | thread pool `ops:235-247`; knot roll `kn:214-216` | [CHECKED] |
| | steadfastness, sincerity, devotion, contact-endurance | none | Spirit checks and formulas in designs only (head U27-U33, F29-F30); no Thread Fatigue, Inspiration or Sincerity code (`git grep`) | grep |
| ATT | reading-people, empathy, discernment | none | FW:94, :97, :101; investigation_systems_v30:255 (design). `att`'s only Python readers are Reading and Reflex, `cs:171-172` | [CHECKED] |
| BON | relational-depth | `bonds` | gate `kn:185-187`; cap `kn:201-202`; the disposition gate beside it `kn:189-193` | [CHECKED] |
| REC | memory, inference, learning, breadth, practice-ceiling | none | no Python field: the `recall` hits are Command's recall roll (`orchestration.py:2546-2590`) and docstrings | grep |
| TS | thread-sensitivity | `ts` | pool `ops:244`; Leap gate and Ob band `ops:358-369`; knot gate `kn:195-198`; opposing Ob `opposing.py:139-142`; anchor rank `collective.py:102` | [CHECKED] |
| uncovered | self-coherence | `resilience` | `ops:250-275`, gain 0 at `ops:156-157` | [CHECKED] |
| temperament | boldness | `disp` | `cs:181-183` | [CHECKED] |
| | | | initiative `wr:127-128`; attack and counter `cs:1115`, `:1149` | [grep] |
| practice | combat History | `history` | pool `core.py:54-56`; the opponent's Ob `core.py:100-115` | [CHECKED] |
| | thread History | `history` | `min(3, history + 3)`, `ops:243-246` | [CHECKED] |
| | relationship History | `history_relationships` | `kn:215-216` | [CHECKED] |
| | contest `faculty` | `faculty` | pool and leverage `res:300-301`; `Pool.size`, `Leverage.net` in `primitives.py:208-230` | [CHECKED] |
| | season `capability` | `Person.capability[key]` | `engine/season/seam/wrappers/sigma.py:82-129` | [CHECKED] |

**What the season loop reads per person** ([CHECKED]): in a fight, `end` from BODY and nothing else
(`fight.py:45`); in a field battle, `Person.weight`, stance and loyalty, with the general fixed at
`command=4` and no Charisma or Cognition (`modules/mass_battle/massbattle.py:182-186`, `:226-230`); in a
contested act, `capability` (`sigma.py:97-129`). Every other arm below runs a module directly, on fields
the season loop never sets (T2).

---

## 2. Protocol

- **Baseline person** (combat): the class default, `strength 4, agi 4, end 4, cog 3, att 3, spirit 3,
  focus 3, history 3, disp 4`, arming sword, light armour (`cb:93-94`); the opponent is the same person.
  Other resolvers: stated with each.
- **Arms.** V_X: one ingredient up one step, and two for linearity (down where the down step is the
  question: END−1 is one BODY band). Control C: the baseline on a disjoint seed set of the same size.
- **Seeds.** Every non-control arm runs the same seeds (paired); each resolver takes its RNG as a
  parameter or from a seeded module stream, as its own tests seed it.
- **N and the band.** Combat, contest, threadwork and knots: N = 20,000 per arm. The control band is the
  95% band of the difference between two independent seed sets of size N, `1.96·√2·sd/√N`: for a win
  rate near 50%, **±0.98 percentage points**. Mass battle (`oblique`): N = 300 per arm, band ±7.7 points
  on win rate; its verdicts rest on per-seed identity, which does not depend on N.
- **The control held.** C stayed inside its band on 14 of 15 combat metrics (A's ending Concentration
  exceeded it by 0.03 points), on every contest, Weaving, Leap, knot and mass-battle metric, and on 4 of
  5 collective metrics (success, by 0.14 points). One
  exceedance in fifteen is what a 95% band predicts, so **no verdict here rests on a single metric
  barely past the band**.
- **The profile test** (`profile_test.py`): fit the one scalar k that best maps Y's effect vector onto
  X's over 14 metrics (each normalized by its band); if every residual is within `band·(1+|k|)` the pair
  is MAGNITUDE-ONLY, else SEPARABLE. **Its falsifier ran first:** pairs that are one ingredient at two
  step sizes must read MAGNITUDE-ONLY, and FOC+1/FOC+2, TMP+1/TMP+2, TMP−1/TMP+1 and ACU+1/ACU+2 do
  (worst residuals 0.27, 0.36, 0.56, 0.73). END−1/END+1 does not (9.1), because Max Wounds is
  `min(⌊End/2⌋+1, 3)` and steps down at End 3 but not up at End 5 (`cb:30-32`): the test reads a
  nonlinearity as a profile difference, so END's within-group verdict rests on the channel split (§3.2),
  not on the profile test.

---

## 3. Results by resolver

### 3.1 Personal combat (probe 1; A's effect against the baseline; * outside the control band)

| arm | Δ win (pts) | Δ opponent felled (pts) | Δ A's damage / Health (pts) | Δ A's ending fatigue (pts) | Δ A's ending Concentration (pts) | Δ turns |
|---|---|---|---|---|---|---|
| STR+1 | +9.90* | +10.94* | −13.38* | −0.68* | +1.89* | −0.03 |
| STR+2 | +19.08* | +21.11* | −26.69* | −1.60* | +4.44* | −0.17* |
| AGI+1 | +8.78* | +9.71* | −11.76* | −0.56* | +0.52* | +0.11* |
| AGI+2 | +17.41* | +19.59* | −23.81* | −1.18* | +1.32* | +0.20* |
| END+1 | +4.50* | +5.05* | −7.26* | −5.10* | −0.81* | +0.12* |
| END+2 | +8.28* | +9.32* | −12.58* | −8.89* | −1.65* | +0.23* |
| END−1 (one BODY band) | −9.06* | −10.11* | +15.67* | +3.04* | +5.77* | −0.45* |
| ACU+1 | +17.89* | +19.98* | −24.04* | −0.68* | +3.89* | −0.08* |
| ACU+2 | +31.29* | +35.01* | −44.05* | −1.46* | +7.48* | −0.19* |
| ATT+1 | +10.18* | +11.24* | −13.18* | −0.26* | +2.00* | −0.03 |
| ATT+2 | +18.93* | +21.20* | −25.62* | −0.78* | +3.81* | −0.05* |
| WIL+1 | +5.19* | +5.82* | −7.57* | −3.60* | +5.46* | +0.05* |
| WIL+2 | +6.75* | +7.64* | −9.28* | −6.67* | +10.32* | −0.02 |
| WIL+3 | +8.33* | +9.29* | −11.03* | −9.15* | +14.29* | −0.09* |
| FOC+1 | +1.87* | +2.15* | −2.25* | −0.08 | +8.48* | −0.08* |
| FOC+2 | +3.85* | +4.21* | −4.18* | −0.12 | +14.58* | −0.17* |
| FOC+2, tracker only | +3.73* | +4.04* | −4.03* | −0.13 | +14.58* | −0.17* |
| FOC=WIL +1 (merged) | +6.97* | +7.80* | −9.48* | −3.64* | +12.31* | −0.05* |
| FOC=WIL +2 (merged) | +11.03* | +12.26* | −13.74* | −6.69* | +20.15* | −0.20* |
| History+1 | +20.31* | +22.87* | −28.07* | −1.35* | +3.41* | −0.02 |
| History+2 | +33.86* | +37.89* | −49.14* | −2.51* | +6.74* | −0.18* |
| TMP+1 | +2.18* | +2.53* | −2.75* | +0.50* | +0.77* | −0.04 |
| TMP+2 | +5.49* | +5.87* | −6.17* | +0.94* | +1.74* | −0.08* |
| TMP−1 | −2.16* | −2.51* | +3.13* | −0.34* | −0.64* | +0.01 |
| TMP−2 | −5.05* | −5.66* | +6.26* | −0.80* | −1.39* | +0.07* |
| C (control) | +0.52 | +0.92 | −0.76 | +0.10 | +0.36* | −0.04 |

*"FOC+2, tracker only"* switches off Focus's poise and disruption gains (`POISE_FOCUS_K`, `DISRUPT_K`,
`cs:1436`, `:1452`) for both fighters; the default opponent sits at Focus 3, where both terms are zero.
**Every ingredient moves win rate past the band at one step; none is inert in combat.** Two are much
larger than their neighbours: ACU (+17.9 at one step) and the learned skill History (+20.3).

### 3.2 Combat channels (probe 1b, 1c)

| arm | what moves | Δ win (pts) | Δ fatigue (pts) | Δ Concentration (pts) | Δ turns |
|---|---|---|---|---|---|
| END+1, stamina reserve only | `stamina_max` 18 → 21 | +0.76 | −5.43* | +0.09 | +0.01 |
| END+1, Durability only | WI 9 → 10, Health 40 → 45 | +3.69* | +0.53* | −0.93* | +0.11* |
| WIL+1, stamina reserve only | `stamina_max` 18 → 20 | +0.55 | −3.83* | +0.05 | +0.00 |
| WIL+1, Concentration only | `conc_max` 15 → 17 | +1.29* | −0.06 | +5.99* | −0.05* |
| WIL+1, Durability only | WI 9 → 10, Health 40 → 44 | +3.29* | +0.41* | −0.74* | +0.09* |
| AGI+1 without tempo and initiative | reflex, Balance, footwork | +5.29* | −0.44* | −0.13 | +0.14* |
| ATT+1, Reflex only (Reading held) | reflex +⅓ | +0.56 | −0.04 | −0.08 | +0.02 |
| ATT+1, Reading only (Reflex held) | Reading +⅓ | +9.60* | −0.23* | +2.04* | −0.05* |

- **The stamina reserve barely moves who wins.** One END step's reserve alone is +0.76 points, inside the
  band; END's win effect is its Durability channel. The two channels have opposite fatigue signs and a
  residual of 21 on the profile test: stamina and toughness are separable channels of one ingredient.
- **Spirit has no combat channel of its own (probe 1c).** A Spirit 4 fighter and a Spirit 3 fighter
  with End 4.4, Focus 3⅔ and a stamina reserve of 20 have the same derived figures (stamina 20, WI 10,
  Max Wounds 3, Health 44, Concentration 17). Their fights are identical on **4,951 of 5,000** seeds,
  with equal win rates (54.42%); with Focus's two side gains off for both, on **5,000 of 5,000**. Each of
  WIL's three channels is a rescaling of END's or FOC's (profile residuals 0.04, 0.21, 0.09).
- **Focus acts through the tracker alone.** FOC+2 with and without its poise and disruption terms differs
  by +0.12 points of win rate (inside the band; k = 1.003, residual 0.10).
- **Attunement's Reflex term is at the edge of noise.** At one step it is +0.56 points (inside the band);
  ACU+1 against ATT+2, whose Readings are equal, differs by −1.04 ± 0.23 points paired, just past the
  ±0.98 band. ATT's Reading channel is a rescaled ACU (k = 0.525, residual 0.59).
- **Quickness is a real channel of AGI.** Tempo and initiative carry 3.50 ± 0.40 points of AGI+1's
  8.78; what remains (reflex, Balance, footwork) differs from the whole only on fight length, and only
  just (profile residual 1.02).
- **Temperament is monotone here.** Against a neutral opponent, more aggression wins more at every step
  (−5.05, −2.16, +2.18, +5.49 points from TMP−2 to TMP+2), and TMP−1 is the mirror of TMP+1 (k = −1.00,
  residual 0.56). In this matchup the lean behaves as a capacity.

### 3.3 Mass battle: Command, the only channel Charisma and Cognition have (probes 2a, 2b)

- **Command 1, 4 and 7 give byte-identical end states on every seed in 9 of the 10 `bat.py` rows**
  (24 seeds each: mirror, wedge, envelop, cannae, manipular, three cavalry rows, ranged). In `oblique`
  it changes 17 of 24 end states and no winner (6 / 6 / 6 wins for A).
- **In `oblique`, the arms collapse onto their Command value, seed for seed** (N = 300): CHA+1 ≡ CHA+2 ≡
  ACU+2 ≡ ACU+3 (all Command 5), ACU+1 ≡ baseline (Command 4: `round((8+5)/3)` = 4), CHA+3 is Command 6.
- **Effects:** the given Command 1 lowers A's ending morale by 2.47 (band 0.21) and wins 4.0 points less
  (band 7.7, inside it); Command 7 raises morale by 0.47*; Command 5 (CHA+1) moves morale +0.20 and win
  rate −0.33, both inside the band; Command 6 (CHA+3) moves morale +0.35*.
- **The season loop's field battle reads neither:** its general is `command=4`, fixed
  (`massbattle.py:182-186`).

### 3.4 The contest kernel and the season's sigma roll (probe 3)

| arm (faculty, Charisma) | A wins | A's advantage | Face_current / Face_max |
|---|---|---|---|
| baseline (4, 4) | 50.24% | 4.318 | 8 / 12 |
| CHA+1, +2, +3 | 50.24% | 4.318 | 10/15, 12/18, 14/21 |
| faculty+1 | 63.64%* | 4.670* | 8 / 12 |
| faculty+2 | 70.20%* | 4.819* | 8 / 12 |
| control | 50.02% | 4.316 | 8 / 12 |

Charisma +1, +2 and +3 are **byte-identical to the baseline on all 20,000 bouts** (winner, how, both
advantages, reserve, standing); only the Face view changes. The season's sigma roll reads
`capability` alone: mean degree ordinal 0.340 at the default pool of 2, 0.589 at 3, 0.833 at 4 (control
0.320).

### 3.5 Threadwork (probe 4)

| arm | Weaving, Field (Ob 5): Δ degree | Leap: Δ degree | note |
|---|---|---|---|
| WIL+1 (Spirit 4) | +0.310* | +0.187* | +2 dice |
| WIL+2 | +0.588* | +0.328* | |
| TS+10 (40) | +0.159* | +0.101* | +1 die |
| TS+20 (50) | +0.310* | +0.409* | +2 dice, and the Leap Ob falls 2 → 1 at TS 50 (`ops:369`) |
| TS−10 (20) | −0.164* | −2.223* | the Leap's TS ≥ 30 gate fails |
| thread History +1, +2 | 0 | 0 | `min(3, history+3)` is already 3 at History 0 |
| thread History −1 | −0.164* | −0.115* | −1 die |
| resilience +1, +2 (gain 0, shipped) | 0 | 0 | |
| resilience +1 at gain 1 (swept arm) | degree 0; Coherence cost +1.00* | cost +0.20* | |

Per-seed identities (20,000 seeds): **WIL+1 ≡ TS+20 in Weaving** (one pool); TS−10 ≡ History−1 in
Weaving; History+1 ≡ History+2 ≡ resilience+1 ≡ resilience+2 ≡ baseline. In the Leap, TS+20 and WIL+1
come apart (+0.409 against +0.187).

**Collective Weaving** (Structural, Ob 8; anchor Spirit 3, TS 50; one helper Spirit 3, TS 30,
Cognition 4): helper Cognition+1 is identical to the baseline (`⌊5/2⌋ = ⌊4/2⌋`); Cognition+2 adds 0.85
dice and +3.9 points of success; helper Spirit+1 raises the helper's own Leap success by 3.0 points and
moves the pool +0.06 (inside the band). A helper **with no Cognition field** contributes `⌊Spirit/2⌋`
(`collective.py:64-68`): 0.85 dice fewer at Spirit 3, and at Spirit 4 byte-identical to a helper with
Cognition 4.

### 3.6 Knots (probe 4; actor Bonds 5, disposition 5, TS 30, Spirit 3; partner TS 0)

| arm | one attempt: formed | six partners: knots formed | six partners: Close knots |
|---|---|---|---|
| baseline | 47.31% | 2.431 | 0.729 |
| BON+1, BON+2 | 0 change | +0.291* (cap 3 → 4) | +0.088* |
| BON−1 (4) | −47.31* (gate) | −2.431* | −0.729* |
| WIL+1 | +14.13* | +0.371* | +0.540* |
| WIL+2 | +24.64* | +0.503* | +0.965* |
| relationship History +1 | +7.62* | +0.229* | +0.281* |
| relationship History +2 | +14.13* | +0.371* | +0.540* |
| TS+10 | 0 | 0 | 0 |
| TS−10 (20) | −47.31* (gate) | −2.431* | −0.729* |

Per-seed identities: **WIL+1 ≡ relationship History+2**; BON+1 ≡ BON+2 (`6//2+1 = 7//2+1`); BON−1 ≡
TS−10 (a failed gate is a failed gate); TS+10 ≡ baseline.

---

## 4. Verdicts by pair

### 4.1 Within each group (`_equivalences` §2)

- **D01 stamina vs toughness (END).** Both are formulas over END and WIL, toughness also over STR; the
  END/WIL mix can hold one and move the other, and their channels differ (§3.2). **SEPARABLE.**
- **D02 hardiness vs stamina and toughness.** Hardiness has no code reader (FW:239; head U05).
  **NOT TESTABLE.**
- **D03 BODY vs END (season).** `end = max(1, 4 − bands)` is the only field the loop sets
  (`combat.py:130-138`, `fight.py:45`). One band is −9.06 points of win rate. **IDENTICAL-BY-CODE.**
- **D04 quickness vs reflexes (AGI).** One ingredient; ATT can move Reflex alone, worth +0.56 points at
  one step (inside the band) and 1.04 at two (at its edge); the quickness channel is 3.50 points.
  **SEPARABLE, marginally** (only through ATT's minor term).
- **D05 balance vs quickness and reflexes.** STR moves Balance without tempo, but no field moves Balance
  without STR's other channels. **SEPARABLE** (not isolable).
- **D06 dexterity vs the AGI members.** No reader. **NOT TESTABLE.**
- **D07 FOC vs concentration.** In code Focus is the tracker term: its two side readers move +0.12
  points at FOC+2 (inside the band). **IDENTICAL-BY-CODE** (measured).
- **D08 ACU vs anticipation.** Cognition's only combat reader is Reading (`cs:171`; grep). **IDENTICAL-BY-CODE
  in combat** (ACU's other readers are Command and the collective helper).
- **D09 reasoning vs observation vs spatial sense vs land sense** (and inference, judgment, planning).
  No code reads any of them; they would all read `cog` if built. **NOT TESTABLE.**
- **D10 reading people vs empathy vs discernment.** No code reader (designs FW:94, :97, :101;
  investigation_systems_v30:255). **NOT TESTABLE.**
- **D11 anticipation vs tactical read.** Reading (Cognition, Attunement, History) against Command
  (Charisma, Cognition): ATT moves the first with Command fixed, CHA the second with Reading fixed, in
  different resolvers and metrics (combat win rate; field-battle morale). **SEPARABLE**, with tactical
  read's channel moving morale in one battery row and nothing in nine.
- **D12 leadership vs situational awareness vs tactical read.** Three uses of one field, `command`.
  **IDENTICAL-BY-CODE.**
- **D13 presence vs persuasiveness vs leadership.** Charisma's contest reader is the outcome-inert Face
  (§3.4); it reaches outcome only as two-thirds of Command. **NOT TESTABLE** (no outcome-moving reader for
  presence or persuasiveness).
- **D14 will vs steadfastness, sincerity, devotion, contact endurance.** Only `will` has a reader (thread
  pool, knot roll); the other four are Spirit rolls and formulas in designs only. **NOT TESTABLE.**
- **D15 contact endurance vs self-coherence (WIL vs resilience).** Resilience is inert as shipped
  (byte-identical, 20,000 seeds); at the module's own swept gain 1 it moves the Coherence cost and not
  the degree, where WIL moves both. **NOT TESTABLE as shipped; SEPARABLE at the swept arm.**
- **D16 relational depth vs sincerity and devotion.** Sincerity and devotion have no reader. **NOT
  TESTABLE.** (BON against Spirit's knot roll is X7.)
- **D17 the Recall group** (memory, inference, learning, breadth, practice ceiling). No Python field.
  **NOT TESTABLE.**

### 4.2 Across the recommended primaries

- **X01 FOC vs WIL.** FOC moves Concentration only; WIL moves the reserve, Durability and Concentration
  (profile residuals 16 to 21). **SEPARABLE.** WIL keeps its standing through threadwork and knots: in
  combat it has no channel of its own (§3.2).
- **X02 STR vs END.** STR moves damage dealt and taken; END moves damage absorbed, fatigue and length
  (residual 9.3). **SEPARABLE.**
- **X03 AGI vs ACU** (the Reading blend). Residual 2.8 on fatigue, Concentration and fight length.
  **SEPARABLE.**
- **X04 CHA vs ACU** (Command). In the one resolver both reach, both are read only through
  `derive_command`, and arms with equal Command are byte-identical on every seed (§3.3). ACU has readers
  CHA lacks (Reading, the collective helper). **IDENTICAL-BY-CODE in mass battle**: one shared
  expression, rescaling exact at 2 : 1 up to rounding.
- **X05 ATT vs ACU** (`(2·Cog + Att)/3`). ATT's only readers are Reading and Reflex. ACU+1 against ATT+2:
  k = 0.945, residual 0.46; ACU+1 against ATT+1: k = 1.79, residual 0.51. The Reflex residue is about one
  point at ATT+2. **SEPARABLE-ONLY-BY-MAGNITUDE; one rescaling (ATT ≈ ½ ACU) absorbs it.**
- **X06 WIL vs END.** Close in win rate (+5.19 against +4.50 at one step); WIL raises Concentration,
  END lengthens fights and absorbs more (residual 10.8). **SEPARABLE.**
- **X07 BON vs WIL** (knots). BON is eligibility: the gate, then the cap; past the gate one attempt is
  unchanged. WIL is the odds of each attempt and the tier. **SEPARABLE.**
- **X08 REC vs every primary**, and the smaller set's REC → ACU merge. No code reads Recall; it is rolled in
  FW:95, :306, SCV:155 and threadwork_v30:688, and gates learning in HIST:34-43 and :517-522. **NOT
  TESTABLE.**
- **X09 TS vs WIL.** One pool in Weaving (WIL+1 ≡ TS+20 seed for seed, 1 Spirit = 20 TS); apart in the
  Leap (TS-band Ob), the knot gate, the opposing Ob and the anchor rank. **SEPARABLE.**
- **X10 STR vs AGI.** k = 1.12, residual 1.9 (damage dealt, fight length). **SEPARABLE.**
- **X11 AGI vs ATT.** Residual 2.5 (Concentration, fight length). **SEPARABLE.**
- **X12 TMP vs the others** (larger set). Residual 5.3 to 5.7 against FOC+2 and STR+1. **SEPARABLE**, and
  monotone in this matchup (§3.2).

### 4.3 The smaller and larger alternatives

- **A01 the smaller set's FOC → WIL merge.** On a merged primary (Focus = Spirit = M), M = 4 gives +6.97
  points and −3.64 fatigue; FOC+2 alone gives +3.85 and −0.12. No M reproduces a person with high Focus
  and low Spirit, who moves Concentration without moving fatigue (FOC+2 against the merged +1: residual
  10.3). **SEPARABLE: the merge loses a measured outcome dimension.**
- **A02 the smaller set's BON → CHA or ATT merge.** Knots read neither Charisma nor Attunement; the merge
  is a rewrite of `kn:185-202`, not a pair any resolver can compare. **NOT TESTABLE.**
- The larger set's **RES** is D15, its **TMP** X12, the **Command-as-primary** variant X04 (carrying
  Command lets it take values off the 2 : 1 lattice; everything Charisma and Cognition do in a field
  battle is Command), and the smaller set's **REC → ACU** X08. They are not counted twice.

### 4.4 Learned skills against their ingredients

- **L01 combat History vs ACU, ATT, AGI, STR.** The pool is `max(5, History + 6)` and reads no attribute
  (`core.py:54-56`); History also sets the opponent's Ob (`core.py:115`) and enters Reading, initiative
  and the counter. It is the largest single lever (+20.3 points) and its profile differs from each
  attribute's (residuals 1.7 to 2.4). **SEPARABLE: not additive with any attribute in one pool.**
- **L02 thread History vs WIL and TS.** One pool, and capped: History 0, +1 and +2 all give the same 3
  dice, byte-identical on 20,000 seeds; History −1 ≡ TS−10. **IDENTICAL-BY-CODE** (additive in one pool;
  inert above 0).
- **L03 relationship History vs WIL.** `spirit × 2 + history_relationships` (`kn:214-216`); History+2 ≡ WIL+1 on every
  seed. **IDENTICAL-BY-CODE** (additive in one pool, 2 : 1).
- **L04 contest faculty vs Charisma.** Faculty is the kernel's only live person input (+13.4 points at
  +1); Charisma moves nothing. **NOT TESTABLE** (one side inert).
- **L05 season capability vs any primary.** The sigma roll reads no attribute (`sigma.py:97-129`).
  **NOT TESTABLE.**
- **L06 collective helper: Cognition vs Spirit.** Cognition sets the helper's dice, Spirit the helper's
  own Leap; Spirit stands in for Cognition when the actor has no Cognition field. **SEPARABLE.**

---

## 5. SUMMARY TABLE

S = SEPARABLE · I = IDENTICAL-BY-CODE · M = SEPARABLE-ONLY-BY-MAGNITUDE · NT = NOT TESTABLE. Effects are
percentage points of win rate (or of success, or of knots formed, as stated) against a control band of
±0.98 unless stated; * is outside it.

| # | pair | ingredients each maps to | resolver | effect of each arm vs control band | verdict |
|---|---|---|---|---|---|
| D01 | stamina vs toughness | `3·end + 2·spirit` / WI, MW, Health on `end`, `0.4·spirit`, `0.25·str·end` | combat | reserve-only +0.76 (in), fatigue −5.43*; Durability-only +3.69* | S |
| D02 | hardiness vs stamina, toughness | none / as D01 | (FW:239, design) | — | NT |
| D03 | BODY vs END | `body` → `end` | season combat | one band = END−1: −9.06* | I |
| D04 | quickness vs reflexes | `agi` / `agi`, `att` | combat | tempo and initiative 3.50*; Reflex-only +0.56 (in); 1.04 at +⅔ Reflex (edge) | S (marginal) |
| D05 | balance vs quickness, reflexes | `agi`, `str` / `agi` (`att`) | combat | STR+1 +9.90* moves Balance and not tempo; not isolable | S |
| D06 | dexterity vs AGI members | none / `agi` | (registry alias) | — | NT |
| D07 | FOC vs concentration | `focus` / `3·focus + 2·spirit` | combat | FOC+2 +3.85*; tracker-only +3.73*; side readers +0.12 (in) | I |
| D08 | ACU vs anticipation | `cog` / `(2·cog + att)/3 + history` | combat | Reading is `cog`'s only combat reader (grep) | I |
| D09 | reasoning, observation, spatial sense, land sense, inference, judgment, planning | none | (FW, settlement, governance designs) | — | NT |
| D10 | reading people, empathy, discernment | none | (FW, investigation designs) | — | NT |
| D11 | anticipation vs tactical read | Reading / `command` | combat / mass battle | ATT+1 +10.18*; Command 1: morale −2.47*, win −4.0 (in ±7.7) | S |
| D12 | leadership, situational awareness, tactical read | `command` (all three) | mass battle | equal Command is byte-identical | I |
| D13 | presence, persuasiveness vs leadership | `charisma` (Face) / `command` | contest / mass battle | CHA +1..+3 byte-identical to baseline, 20,000 bouts | NT |
| D14 | will vs steadfastness, sincerity, devotion, contact endurance | `spirit` / none | threadwork, knots | — | NT |
| D15 | contact endurance vs self-coherence | none / `resilience` | threadwork | RES byte-identical at gain 0; at gain 1: cost +1.00*, degree 0 | NT (shipped); S at gain 1 |
| D16 | relational depth vs sincerity, devotion | `bonds` / none | knots | — | NT |
| D17 | the Recall group | none | (HIST, FW, SCV designs) | — | NT |
| X01 | FOC vs WIL | `3·focus` in the tracker / reserve, Durability, tracker | combat | FOC+2 +3.85*, fatigue −0.12 (in); WIL+1 +5.19*, fatigue −3.60* | S |
| X02 | STR vs END | handling, bind, impact, Balance / Durability, reserve | combat | +9.90* vs +4.50*; residual 9.3 | S |
| X03 | AGI vs ACU | tempo, reflex, Balance / Reading | combat | +8.78* vs +17.89*; residual 2.8 | S |
| X04 | CHA vs ACU | `derive_command` (2 : 1) | mass battle | CHA+1 ≡ CHA+2 ≡ ACU+2 ≡ ACU+3, seed for seed | I |
| X05 | ATT vs ACU | Reading (1 : 2), Reflex | combat | ATT+2 +18.93* vs ACU+1 +17.89*; k 0.945, residual 0.46 | M (rescale absorbs) |
| X06 | WIL vs END | reserve 2 : 3, WI 0.4 : 1, tracker / — | combat; thread, knots | +5.19* vs +4.50*; residual 10.8 | S |
| X07 | BON vs WIL | gate and cap / roll | knots | BON+1: one attempt 0, six partners +0.29*; WIL+1: +14.13* | S |
| X08 | REC vs every primary (and REC → ACU) | none | (HIST, FW, SCV, threadwork designs) | — | NT |
| X09 | TS vs WIL | `ts // 10` and gates / `spirit × 2` | threadwork, knots | Weaving: WIL+1 ≡ TS+20; Leap: +0.187* vs +0.409* | S |
| X10 | STR vs AGI | as X02 / as X03 | combat | +9.90* vs +8.78*; residual 1.9 | S |
| X11 | AGI vs ATT | tempo, reflex, Balance / Reading, Reflex | combat | +8.78* vs ATT+2 +18.93*; residual 2.5 | S |
| X12 | TMP vs STR, FOC | `(disp − 4)/3` | combat | TMP+2 +5.49*; residual 5.3 to 5.7; monotone | S |
| A01 | merged FOC = WIL vs FOC | `3F + 2S` with F = S | combat | merged +1: +6.97*, fatigue −3.64*; FOC+2: +3.85*, fatigue −0.12 | S |
| A02 | BON merged into CHA or ATT | `bonds` / not read by knots | knots | — | NT |
| L01 | combat History vs ACU, ATT, AGI, STR | pool, opponent's Ob, Reading, initiative, counter | combat | History+1 +20.31*; residuals 1.7 to 2.4 | S |
| L02 | thread History vs WIL, TS | `min(3, history + 3)` in one pool | threadwork | +1, +2 byte-identical to baseline; −1 ≡ TS−10 | I |
| L03 | relationship History vs WIL | `spirit × 2 + history_relationships` | knots | History+2 ≡ WIL+1 on every seed | I |
| L04 | contest faculty vs Charisma | `faculty` / Face | contest kernel | faculty+1 +13.40*; CHA byte-identical | NT |
| L05 | season capability vs any primary | `capability[key]` | season sigma roll | cap 3: degree +0.25; reads no attribute | NT |
| L06 | collective helper: Cognition vs Spirit | `⌊cog/2⌋` (else `⌊spirit/2⌋`) / the helper's Leap | threadwork collective | Cog+2 +3.94* success; Spirit+1 helper Leap +2.99* | S |

**Counts (37 pairs):** SEPARABLE **16** (D01, D04, D05, D11, X01, X02, X03, X06, X07, X09, X10, X11,
X12, A01, L01, L06) · IDENTICAL-BY-CODE **7** (D03, D07, D08, D12, X04, L02, L03) ·
SEPARABLE-ONLY-BY-MAGNITUDE **1** (X05) · NOT TESTABLE **13** (D02, D06, D09, D10, D13, D14, D15, D16,
D17, X08, A02, L04, L05). D15 is counted NOT TESTABLE as shipped; at the module's swept gain it would be
SEPARABLE.

---

## 6. One line per group (relative to the recommended set)

| group | reading |
|---|---|
| STR | **keep**: one member, separable from END and AGI |
| AGI | **keep as a group under AGI**: quickness, reflexes and balance are channels of one ingredient; ATT and STR separate them only marginally or not in isolation; dexterity is untested |
| END | **keep as a group under END**: stamina and toughness are separable channels of the same ingredients, and the reserve channel barely moves who wins; BODY is END on the season path |
| FOC | **keep as a group under FOC**, separable from WIL; in code FOC is exactly the tracker term, so carrying *Concentration* instead would lose nothing in combat |
| ACU | **keep**: anticipation is its only combat channel; reasoning, observation and spatial sense are untested |
| WIL | **keep as a group**, on threadwork and knots: only `will` has readers, and in combat WIL has no channel END, FOC and the reserve do not carry |
| ATT | **merge into ACU on code evidence alone** (a rescaled ACU wherever code reads it); keep only on its design uses, which no code tests |
| CHA | **no code evidence either way**: identical to ACU in the one resolver both reach, outcome-inert in the contest; its three Command uses are one field; keep only on design uses |
| BON | **keep**: separable from WIL; past the gate only the cap moves an outcome |
| REC | **untested**: no code reader |
| TS | **keep**: separable from WIL everywhere except inside the Weaving pool |
| uncovered (RES) | **inert as shipped**; separable from WIL at the swept gain |
| temperament (TMP) | **separable**, and monotone in the matchup tested |
| practice | **History splits from every attribute in combat** (its own pool, the largest lever) and **is additive with Spirit in the thread and knot pools** |

---

## 7. Does any result change the recommended eleven?

**Not by itself.** No pair inside the eleven came out IDENTICAL-BY-CODE across every resolver. The one
IDENTICAL pair between primaries, CHA and ACU, is identical only in the resolver both reach, and ACU
has readers CHA lacks. **Three results bear on the set, and each is Jordan's to weigh:**

1. **ATT has no code evidence as a separate primary.** Wherever code reads Attunement it is about half a
   Cognition (X05). Its case rests on design uses (reading people, the Lattice gate, Appraise, the
   fifteen Histories skills of head §1.6) that no code runs.
2. **CHA has no outcome-moving reader of its own at T2.** The contest's Charisma is byte-identical inert
   (§3.4); in a field battle Charisma is two-thirds of a Command that moves nothing in 9 of 10 battery
   rows and only morale in the tenth (§3.3); the season's field battle fixes Command at 4. `_part3`
   §7.4 calls CHA *"narrowed at T2"*; measured, it is inert at T2.
3. **The smaller set's FOC → WIL merge loses something the code measures** (A01). That supports keeping
   FOC. Two other results cut against reasons `_part3` gives: WIL has no combat channel of its own, and
   TMP, rejected as a lean (P5), is monotone in the matchup tested.

---

## 8. LIMITS

- **One matchup per resolver.** Combat: arming sword, light armour, a default opponent. Mass battle: the
  `bat.py` battery for reach, and `oblique` alone for the Charisma arms. Contest: default venue, neutral
  adjudicator, advocate against advocate. A pair separable here may collapse elsewhere and the reverse;
  TMP's monotone result especially may not survive an aggressive opponent.
- **Nonlinear responses read as profile differences** (END−1 against END+1, §2); verdicts at a step
  boundary rest on the channel split, not the profile test.
- **The channel arms use values the game does not allow** (End 4.4, Focus 3⅔, Cognition 2.5). The code
  accepts them and they isolate a channel exactly; they show what the code does, not what a sheet can
  hold.
- **Many resolvers exist in design only.** Recall and all its formulas (F25, F37-F40), the Spirit checks
  of belief under shock (U28-U33), Sincerity, Inspiration (F29), Thread Fatigue (F30), the operations
  cap (F31), the Focus defence (F20), Composure (F24), every fieldwork and settlement roll, hardiness,
  dexterity: no code reads them, so **this test cannot show any design intent no code reads**, and it
  says nothing for or against the demands they carry.
- **Stubs and inert readers count as absent outcomes, not absent readers:** `RESILIENCE_GAIN = 0`
  (`ops:157`); Charisma into Face (`res:230-236`); Command in 9 of 10 battery rows. A default flag can
  change that (`POOL_QUALITY_MODEL` keeps Command out of the mass-battle pool,
  `modules/mass_battle/config.py:556`, a grep hit; not varied here).
- **T1 is almost empty.** The season loop sets one combat field (`end`, from BODY), one practice key
  (`capability`), and the field battle's weights; every other arm runs a module on fields the loop never
  writes.
- **Mass battle is underpowered for win rates** (N = 300, band ±7.7 points); its verdicts rest on
  per-seed identity, which does not depend on N.
- **Not opened in this pass:** `orchestration.py` beyond `:1815-1854` (the Command readers are grep
  hits), `core/state.py`, `contact.py`, `config.py`'s mass-battle flags beyond the grep lines, and the
  design documents (cited from the head, not reread).
- **Single producer.** No independent agent re-ran a probe; the scripts are written to be re-run as
  they stand.
