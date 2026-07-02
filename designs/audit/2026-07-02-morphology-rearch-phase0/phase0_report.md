# Phase-0 Morphology Harmonization Report

**Scope:** 9 source files (1 canonical roster + 8 cluster batches), 53 weapons total.
**Output:** `phase0_morphology_combined.json` — `{"weapons": {...53 keys...}, "flags": [...], "harmonization_notes": "..."}`

---

## 1. Per-cluster confidence summary

| Cluster | Weapons | Grade mix | Notes |
|---|---|---|---|
| `existing_roster` | 12 (rapier, arming, longsword, greatsword, sabre, dagger, paired_short, spear, staff, mace, poleaxe, longsword_halfsword) | mostly S1/S2, `paired_short` S3 | Canonical-12, already well-formed; schema used as the harmonization target for all others. |
| `polearm_spears_A` | 5 (yari, kama_yari, dangpa, bear_spear, ranseur) | S1 (bear_spear) → S2 (rest) | Tightest mass-budget closures in the whole roster (all ≤0.04% residual). `bear_spear` strongest (Royal Armouries specimen + 3 treatises). `ranseur` weakest whole-weapon (no S1 treatise names it directly). |
| `polearm_multi_and_blade_A` | 5 (spetum, partisan, naginata, glaive, guandao) | S1 (partisan, guandao) → S3 (glaive) | `glaive` is the single weakest-evidenced weapon of this cluster — no period treatise or named specimen, pure typological analogy to naginata. |
| `polearm_choppers_A` | 5 (podao, fauchard, bardiche, sparr_axe, voulge) | S1 (bardiche) → S3 (sparr_axe, voulge) | `bardiche` strongest (3 independent museum specimens). `voulge` had zero handling/treatise sources in prior research — weakest in this cluster alongside `sparr_axe`. |
| `polearm_hooks_hammers_A` | 5 (guisarme, ji, bec_de_corbin, lucerne_hammer, goedendag) | S1 (bec_de_corbin, lucerne_hammer) → S2/S3 (goedendag, guisarme) | `bec_de_corbin`/`lucerne_hammer` are excellent poleaxe-family siblings (near-identical haft geometry, both Met-specimen-anchored). `goedendag` has no comparable museum specimen at all. |
| `sword_japanese_chinese_long_A` | 5 (katana, tachi, odachi, tsurugi, changdao) | S1 (tsurugi mass anchor) → S3 (odachi combat-class size) | All 5 have a **residual_pct sign-labeling bug** in the source (see §2). `odachi`'s combat-representative 120cm/2.2kg class is interpolated, not specimen-pinned (only oversized votive outliers exist as S1 anchors). |
| `sword_curved_world_sabres_A` | 5 (nandao, jian, scimitar, pulwar, shamshir) | S1 (scimitar) → S2/S3 (nandao) | `pulwar` and `shamshir` sit closest to the ±10% mass-budget ceiling (−9.47%, −9.41%) of any weapons in the roster, though both remain in tolerance. `nandao` is a 20th-c. sport invention with no organic historical specimen corpus. |
| `sword_straight_thrust_and_broad_A` | 6 (szabla, cinquedea, flamberge, estoc, estoc_halfsword, falchion) | mixed S1–S3, no top-level grade field | `cinquedea` has 2 accession-numbered Met specimens (strongest). `flamberge`'s wave amplitude/period (15mm/90mm) is a bracketed S3 estimate, weakest single numeric fact in this cluster. |
| `dagger_and_hook_A` | 5 (rondel, main_gauche, stiletto, misericorde, hook_sword) | S2 (most) → S3 (hook_sword) | `main_gauche` and `rondel` best-attested (named Royal Armouries/Wallace Collection specimens). `hook_sword` is the **single weakest-grounded weapon in the entire 53-weapon roster** — no period treatise exists for it at all. |

---

## 2. Flags (7 total)

1. **`sabre` (existing_roster)** — geom_notes cites `curvature=0.42` as context from weapons.py's own dimensionless shape descriptor. Not a smuggled scalar in this record's physical fields (mass/x_m/extent_m are all clean); flagged for visibility only, not altered.

2. **`goedendag` (polearm_hooks_hammers_A)** — its `head_elements` list includes a "tapering club body" entry with `mass_kg_est=0.0` on a nonzero-`extent_m` element. This is an intentional zero-mass geometry placeholder (real mass is folded into `haft_or_grip.mass_kg_est` to avoid double-counting, per the source cluster's own explicit convention), not a defect — but flagged because a bare `0.0` mass on a real geometric element could be misread as an omission by a downstream consumer.

3. **`pulwar` (sword_curved_world_sabres_A)** — mass-budget residual −9.47%, the tightest margin against the ±10% tolerance ceiling in the roster. Still within tolerance; no adjustment made since the source cluster's own componentry (guard/pommel/grip) is already the least-grounded part (S2/S3, no gram-level specimen breakdown located) and further squeezing it would not improve grounding, only cosmetically shrink the residual.

4. **`shamshir` (sword_curved_world_sabres_A)** — same situation as pulwar: −9.41% residual, tightest-margin runner-up. Left as-is for the same reason.

5. **FORMS check (compliance confirmation, not a defect)** — `estoc_halfsword` correctly mirrors `longsword_halfsword`'s pattern: identical total mass (2.0kg) and identical guard/pommel masses to its base `estoc`, with only the blade split repositioned around a shifted working-hand origin (`origin_shift_m=0.75`). No independent physics introduced. Confirmed compliant with instruction (5).

6. **`hook_sword` (dagger_and_hook_A)** — its crescent hand-guard is deliberately double-listed under both `head_elements` and `guards[]` with shared (explicitly non-duplicated) mass. This is a genuine open modeling question the source cluster itself flags for Phase B (does the physics engine consume one part-record or sum two independent ones) — carried forward unresolved, not a Phase-0 defect, but the single item most likely to bite a downstream consumer that naively sums both lists.

7. **SIGN-ERROR in source reporting (katana, tachi, odachi, tsurugi, changdao — sword_japanese_chinese_long_A)** — all five report `mass_budget.residual_pct` as a positive magnitude (e.g. `6.8`) while their part-sums are actually *less than* `total_mass_kg` in every case, meaning the mathematically correct signed residual is negative (e.g. `-6.8%`). Recomputed residuals run −5.7% to −7.9%, still comfortably within the ±10% band — this is a cosmetic sign bug in the source cluster's own `mass_budget` field, not an actual mass-budget failure. **Corrected** (sign fixed) in the combined output.

No AXIS violations, no UNIT inconsistencies, and no 0–1 behavioral scalars smuggled into mass/position/extent fields were found anywhere in the 53-weapon roster.

---

## 3. Weakest-grounded weapons needing follow-up

Ranked by combined confidence-tier + evidentiary thinness (worst first):

1. **`hook_sword`** (dagger_and_hook_A) — S3, no period treatise at all; total mass/length scaled down from a single antique-dealer specimen (Mandarin Mansion, Qing-era, 979g/103.7cm) by a length ratio; crescent guard/head dual-role mass-sharing is an unresolved structural question (see Flag 6).
2. **`voulge`** (polearm_choppers_A) — S3; the prior research pass returned **zero** handling/treatise sources; all geometry and mass split rest on typology/replica sources only.
3. **`goedendag`** (polearm_hooks_hammers_A) — S2/S3; no surviving museum specimen with directly measured mass; only a single primary-source combat-use quote (Guiart) with no numbers.
4. **`glaive`** (polearm_multi_and_blade_A) — S3; no period treatise or named accessioned specimen; dimensions rest entirely on generic European-typology convention and family analogy to naginata.
5. **`sparr_axe`** (polearm_choppers_A) — S3; no single accessioned specimen mass located for the "sparth axe" identity (a modern typological label); total mass is typology-interpolated.
6. **`odachi`** (sword_japanese_chinese_long_A) — S3 for its specific combat-representative 120cm/2.2kg size class; the only S1-specimen-attested odachi masses (Atsuta Shrine 4.5kg, Norimitsu ~14.5kg) are both oversized votive outliers explicitly excluded as non-representative.
7. **`nandao`** (sword_curved_world_sabres_A) — S2/S3; a 20th-century sport-invented weapon with no organic historical specimen corpus, grounded only via the niuweidao ancestor lineage by analogy.
8. **`ranseur`** (polearm_spears_A) — S2; no S1 period treatise names the type directly (handling reasoned by analogy to Fiore's lanza and Marozzo's partisan); secondary sources show real total-mass variance (~4kg vs. 1.4–2.3kg band).
9. **`guisarme`** (polearm_hooks_hammers_A) — S2, handling-research stream in its cluster prior was entirely placeholder; per-element hook/spike mass split rests on engineering apportionment only.
10. **`flamberge`**'s wave-profile numerics (amplitude 15mm / period 90mm) — S3 bracketed estimate, no laser/caliper-measured specimen located.

---

## 4. Mass-budget table (all 53 weapons, sorted by |residual|)

| Weapon | total_mass_kg | sum_est_kg | residual_pct | grade | source cluster |
|---|---:|---:|---:|---|---|
| pulwar | 0.95 | 0.86 | −9.47 | S2 | sword_curved_world_sabres_A |
| shamshir | 0.85 | 0.77 | −9.41 | S2 | sword_curved_world_sabres_A |
| dagger | 0.30 | 0.274 | −8.67 | S2 | existing_roster |
| tachi | 1.20 | 1.105 | −7.92 | S2 | sword_japanese_chinese_long_A |
| changdao | 1.60 | 1.475 | −7.81 | S2 | sword_japanese_chinese_long_A |
| fauchard | 2.20 | 2.03 | −7.73 | S2 | polearm_choppers_A |
| jian | 0.90 | 0.835 | −7.22 | S2 | sword_curved_world_sabres_A |
| tsurugi | 0.65 | 0.605 | −6.92 | S1 | sword_japanese_chinese_long_A |
| katana | 1.10 | 1.025 | −6.82 | S2 | sword_japanese_chinese_long_A |
| odachi | 2.20 | 2.075 | −5.68 | S2 | sword_japanese_chinese_long_A |
| spetum | 1.90 | 1.80 | −5.26 | S2 | polearm_multi_and_blade_A |
| rapier | 1.30 | 1.368 | +5.23 | S2 | existing_roster |
| scimitar | 1.00 | 0.95 | −5.00 | S1 | sword_curved_world_sabres_A |
| podao | 2.60 | 2.48 | −4.62 | S2 | polearm_choppers_A |
| nandao | 1.30 | 1.24 | −4.62 | S2 | sword_curved_world_sabres_A |
| lucerne_hammer | 2.60 | 2.483 | −4.48 | S1 | polearm_hooks_hammers_A |
| naginata | 1.40 | 1.35 | −3.57 | S2 | polearm_multi_and_blade_A |
| poleaxe | 2.50 | 2.583 | +3.32 | S1 | existing_roster |
| glaive | 1.90 | 1.84 | −3.16 | S2 | polearm_multi_and_blade_A |
| bec_de_corbin | 2.40 | 2.453 | +2.22 | S1 | polearm_hooks_hammers_A |
| sparr_axe | 2.30 | 2.25 | −2.17 | S2 | polearm_choppers_A |
| greatsword | 2.70 | 2.751 | +1.89 | S2 | existing_roster |
| guisarme | 1.90 | 1.866 | −1.77 | S2 | polearm_hooks_hammers_A |
| staff | 1.50 | 1.478 | −1.47 | S2 | existing_roster |
| partisan | 2.60 | 2.57 | −1.15 | S1 | polearm_multi_and_blade_A |
| voulge | 2.20 | 2.18 | −0.91 | S2 | polearm_choppers_A |
| longsword / longsword_halfsword | 1.40 | 1.408 | +0.57 | S1 | existing_roster |
| bardiche | 2.60 | 2.61 | +0.38 | S1 | polearm_choppers_A |
| paired_short | 0.70 | 0.698 | −0.29 | S3 | existing_roster |
| goedendag | 1.80 | 1.796 | −0.22 | S2 | polearm_hooks_hammers_A |
| spear | 2.00 | 2.004 | +0.20 | S1 | existing_roster |
| dangpa | 1.84 | 1.839 | −0.04 | S2 | polearm_spears_A |
| kama_yari | 1.44 | 1.440 | −0.02 | S2 | polearm_spears_A |
| bear_spear / ranseur | 2.35 / 2.15 | 2.350 / 2.150 | +0.01 | S1 / S2 | polearm_spears_A |
| arming, sabre, mace, yari, guandao, ji, szabla, cinquedea, flamberge, estoc, estoc_halfsword, falchion, rondel, main_gauche, stiletto, misericorde, hook_sword | — | — | 0.00 | mixed | (all closed exactly to source total) |

All 53 residuals fall within the ±10% tolerance; none required a compensating adjustment to the least-grounded part per instruction (3) — the tightest cases (pulwar, shamshir) were left as-is since squeezing them further would not improve evidentiary grounding.

---

## 5. Cross-cluster comparability

- **Sabre family** (sabre, scimitar, pulwar, shamshir, szabla, nandao): masses 0.85–1.3kg, blade lengths 0.78–0.87m, uniform 4-part decomposition (blade/guard/grip/pommel). Coherent; nandao's higher mass is a deliberately sourced heavier chopper cross-section, not an error.
- **Hammer/pick composites** (mace, poleaxe, bec_de_corbin, lucerne_hammer): poleaxe/bec_de_corbin/lucerne_hammer share an essentially identical 3-element compound-head pattern and haft geometry (1.8m, 50/50 centre-grip, ~0.038–0.040m diameter) — excellent comparability. mace is correctly simpler (single flanged block, no beak/spike) at a shorter implied length.
- **Japanese/Chinese long-sword family** (katana, tachi, odachi, changdao): scale coherently from 1.1kg/0.70m blade to 2.2kg/1.20m blade, same shinogi-zukuri construction family.
- **Two-handed thrust-spear family** (spear, yari, kama_yari, dangpa, bear_spear, ranseur): shared grip fraction 0.12–0.19 and cylinder-volume shaft-mass methodology; mass scale 1.23–2.35kg tracks documented use-case (duelling vs. charge-reception) coherently.

---

## 6. FORMS and ADORNMENTS compliance

- **FORMS (instruction 5):** both `longsword_halfsword` and `estoc_halfsword` correctly reference their base weapon's exact part-set with only a shifted working-hand origin — no independent physics. Compliant.
- **ADORNMENTS (instruction 6):** only 3 adornments survive roster-wide, all attested with explicit sourcing and flagged as non-combat/ceremonial: `ranseur` tassel (S3, period art), `guandao` tassel (S2, period illustration + Qing ceremonial specimens), `jian` pommel tassel (S2, civilian/taijijian tradition). No speculative adornments were found anywhere else in the roster to strip — every other weapon already carries an empty `adornments: []`.
