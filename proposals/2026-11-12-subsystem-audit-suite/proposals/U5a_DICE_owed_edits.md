# U5a · DOE — the DICE owed edits: the one sampler Jordan chose, and the resolutions no proposal carried

## Status: PROPOSED (a plan for future execution; nothing here is executed by the closing lane)

Authored by the U5a unification-closure lane, 2026-11-12, from `audits/10_DICE_audit.md` (§6.2 resolutions
9, 11–16, 20; F-DICE-11, -12, -13), `audits/10_DICE_audit_addendum_B.md` (§3 H-152; §5.1; F-DICE-19, -22)
and `audits/16_PESSIMIST_DICE.md` (F-PES-DICE-05; §7's notes on two DICE proposals), as Jordan's answers
A-5 (the bell curve everywhere) and A-8 (a wound is a level against the roll) decide them. The DICE audit
wrote its export and roller proposals for whole dice and listed the other sampler as Option B; Jordan
answered B. §1 is therefore the plan those proposals did not have. It decides nothing new except where
marked **(U5a)**.

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `U3_CONFLICT_LEDGER.md` C3-L1 and `R1_READ.md` §1.3 / 7b-18 (row 1: the margin is quantised once at the ladder to integer milli-units; row 6: `_MARGIN_EPS` deleted; `04:903` and D-29 bind as written, no Layer 1 text owed), C3-D2 (the Order: row 4, the field's sampler, lands here in B05; the field calibration batch lands after the keyed draw), `U5b_MB_rulings_in_the_field.md` §1 row 2 (row 4: the melee pair is not an opposed roll; no `obstacle:` contract key), `10_DICE_advantage_sources_for_the_arcs.md` as reconciled (§2: Edit B is bilateral, `29_DICE` item 29-4 step 5), U1 §4 R-27 (§2: the in-fight σ and the season's `wound_step` are sized by one calibration); test 9 (row 2's call sites listed from the tree, including the off-loop social-contest oracles, which are re-pointed in the same commit; tests per row; tier; `Depends on:` / `Lands in batch:`; U3 §4.1 rows 23–24 put §4 in B09).

**Depends on:** `10_DICE_one_roller_one_fraction_rule.md` (B05, the MB composition) and `U5a_capability_home_and_two_inputs.md` Part B (B05, the same batch); §4 on `16_PESSIMIST_CORE_a_refusal_is_remembered.md` and `01_CORE_claim_fade_as_read.md` (B09).
**Lands in batch:** §1–§3 in B05 (`B05-one-roll`, IN), before `11_GO_one_draw_owner.md` (B06); §4 in B09 (`B09-memory`).

## What it changes in `engine/season/` at runtime

§1 changes every graded draw outside combat: the social roll, the graded inquiries, the task draw and the
field's exchanges are sampled from the bell curve personal combat already uses; the exact enumeration, the
settled integer margin and the fractional die are deleted. Every seeded result moves once. §2 is the
wound's level. §3 moves nothing. §4 is a declared mover for an actor who has failed a search.

## §1 · One sampler (A-5; lands in one batch with `U5a_capability_home_and_two_inputs.md` Part B)

| # | owner | exact edit |
|---|---|---|
| 1 | `modules/social_contest/roll.py::roll` | `roll_net(pool, rng)` → `roll_net_continuous(pool, rng)`; the margin is `net + net_boost(leverage, pool) − obstacle`, converted once at the ladder to integer milli-units (`round(MARGIN_SCALE × margin)`, `MARGIN_SCALE = 1000`) and graded by `degree_from_net` against `BAND_FLOORS` in the same units (`04:903`, D-29; C3-L1, W3-1); `settle_record` is not called |
| 2 | `engine/dice_engine/sigma_leverage.py` | `band_odds(pool, ob, …)` keeps its name and signature and returns the four band shares from the Normal closed form of the same sampler (the bands' edges read from `BAND_FLOORS`); `record_odds` follows; `_net_counts`, `_dice_dealt`, `roll_net`, `settle_margin`, `settle_record` are deleted. `p_success` is the same closed form and is kept as its one-band case. `eff_ob`, `effective_ob`, `sigma_space_ob_shift` have no caller and leave with the kernel (SC-P2). *Call sites (W3-1, grepped at the tree):* `roll_net` at `modules/social_contest/roll.py:165` (row 1) and in the off-loop oracles `systems/social_contest/sim/contest/faction.py:144-145`, `agon_harness.py:259`, `resolver.py:32`, which are re-pointed to `roll_net_continuous` in the same commit (one sampler, A-5); `settle_record` at `engine/season/seam/wrappers/sigma.py:552`; `_dice_dealt`, `_net_counts`, `settle_margin` only inside `sigma_leverage.py` (`:364`, `:368`, `:397`, `:412`). `modules/combat/core.py:62`'s `roll_net` is already `roll_net_continuous` and is untouched |
| 3 | `modules/social_contest/roll.py::_chance_floor_cap` | solved on the closed form (the pool's cap is the obstacle at which Partial-or-better equals the one-pool chance at the fixed ceiling); `16_PESSIMIST_DICE_soft_ceiling.md`'s `saturate` reads that cap unchanged. With a signed channel the floor is solved at the largest lawful disadvantage (the soft cap's `−M_MAX`), not "at no advantage" **(U5a; closes the pessimist's P-iii (c))** |
| 4 | `modules/mass_battle/resolution.py` (MB's lane, U5b) | `roll_pool`, `roll_pool_fractional`, `compute_degree`, `_sigma_softcap`, `_sigma_net_boost` become calls to the owner: `roll_net_continuous`, `degree_label`, `soft_cap`, `net_boost` (`10_DICE_one_roller_one_fraction_rule.md` Edit C, with the sampler changed). *(W3-1:)* the melee pair is not an opposed roll (`U5b_MB_rulings_in_the_field.md` §1 row 2: each side paid by its own net), so no `obstacle: opposed_roll` key is created on the contract row; a check that keeps a stated obstacle reads `sigma_leverage.OB_MIN` for its floor |
| 5 | `engine/dice_engine/dice_engine.py`, `sigma_leverage.py` | below one die there is one rule: `continuous_engine_sample` and `net_boost` take the pool as it is for `pool > 0` (spread and boost both scale with `√pool`); the floor at one die is removed from the sampler and the boost. A person never reaches it (`pool_floor` is five); an aggregate may (F-DICE-19) |
| 6 | `engine/dice_engine/dice_engine.py` | *(W3-1, C3-L1: no `_MARGIN_EPS`; `…one_fraction_rule.md` Edit A is withdrawn)*; `MARGIN_SCALE`, `BAND_FLOORS` in milli-units, the per-die pair asserted against `FACE_NET`, `LEVEL_SIGMA` unannotated (`10_DICE_exported_face_rule_and_band_edges.md` Edits A, D). `FACE_NET` is kept as the derivation of `MU_PER_DIE` and `SIGMA_PER_DIE`; no game path deals a face. `roll_pool` loses its last season and module caller; whether it stays for the retained off-loop oracles (`systems/threadwork/sim`, `systems/fieldwork/sim`) is those subsystems' question and is not decided here |
| 7 | `references/module_contracts.yaml`; the three wrappers' `resolver` strings | one name for all three providers, `d_sigma` (combat's existing string); the three tests that pin the strings re-pin in the same commit. The three-name vocabulary of the export proposal's Edit C is not created |
| 8 | tests | `engine/tests/test_band_odds.py` and `test_settle_margin.py` (enumeration against the face table) are replaced by the closed form against a sampled check at a stated n and tolerance (an *approximation* claim, so a tolerance is honest); `tests/valoria/test_fractional_pool.py` is deleted with its subject; `engine/tests/goldens/sigma_leverage_parity.json` is regenerated for the functions that remain |
| 9 | the two docstrings (`continuous_engine_sample`, `roll_net_continuous`) | *"The sampler every provider draws from (ED-833; Jordan, 2026-11-12). Same mean and variance as the d10 face rule it is derived from."* The export proposal's Edit B wording (combat only) is not used |

**Order.** After `10_DICE_one_roller_one_fraction_rule.md`'s mass-battle composition is designed with MB
(U5b) and before `11_GO_one_draw_owner.md` / the keyed draw (A-30), so the goldens move once for the sampler
and once for the draw key, each said plainly. *(W3-1, C3-D2:)* row 4 (the field's sampler,
`U5b_MB_rulings_in_the_field.md` §1) lands here in B05; the field calibration batch lands after the keyed draw.

**Gate.** (1) One sampler: `grep -rn "randint(1, 10)" modules/ engine/season/` prints nothing; under
`engine/dice_engine/` the one call is in `roll_pool`. (2) Shown odds are dealt odds: for pools 5 to 12 and
obstacles 1 to 6 in halves, 200,000 seeded social rolls per cell sit within three standard errors of
`band_odds`. (3) Monotone and bounded: P(Partial or better) strictly falls in the obstacle and rises in the
pool on a 0.25 grid below the cap; no chance under the floor at `−M_MAX`. (4) The realm, seeds 0–2, two
seasons: `DEGREES RESOLVED` by verb, both arms, reported in the landing commit (a reading with its control,
not a balance claim). (5) The port: `tools/export_sim_params.py --check` passes with `BAND_FLOORS` and
`LEVEL_SIGMA` present.
**Falsifier.** A graded act outside combat that draws a d10 face; `band_odds` differing from the dealt
frequency beyond the stated tolerance; two obstacles a quarter apart composing one chance.
**Hash movers.** Every world in which a graded act resolves; all goldens, re-pinned once.
**Tests (W3-1).** Row 8's replacements: `engine/tests/test_band_odds.py` (closed form against a sampled check),
`tests/valoria/test_degree_ladder_single_owner.py::test_quantised_margins_sum_in_either_order` (C3-L1's
falsifier), gate (1) as `engine/season/tests/test_mass_battle_module.py::test_no_d10_face_in_mass_battle` plus a
sibling for `modules/social_contest`; gate (2)'s 200,000-roll check is a one-time reading in the commit body.
**Lands:** an IN-lane implementation session under `/methodology-execute` with SC, MB and GO review; edits
`sonnet`, the re-pin's reading `opus`.

## §2 · The wound (A-8)

A wound is a named level against the wounded roller, through the signed advantage channel:
`10_DICE_advantage_sources_for_the_arcs.md` Edits A–D stand, with Edit B bilateral (the bearer's wound is
also a level for the roller when the bearer defends; `29_DICE` item 29-4 step 5, absorbed there by W3-1). The obstacle-term form of
`audits/10_DICE_audit_addendum_B.md` §5.4 (from ED-PC-0005/0006, which A-8 replaces) is not built, and
`obstacle_terms` ships with the one generic member `capability` and no `wounds`. Combat already spends a
wound as sigma (`combat_systems.wound_impairment`), so the season and the fight agree on the channel; the
level's size at each scale is the calibration's: the in-fight σ (`CFG`) and the season's `wound_step` are two
sites of one rule, sized together in PC's calibration batch (B15; U1 §4 R-27).

## §3 · Edits decided by the audits and carried by no file (hash EQUAL)

| row | owner | exact edit | source |
|---|---|---|---|
| 1 | `engine/season/hole_register.yaml` H-215 | `cite:` gains: *"the room moves the obstacle by a flat amount, so its leverage falls with the pool (1.25 z at one die to 0.44 at eight for one point of reception) where a named level's does not (0.48 z at every pool); accepted as an instance modifier under the 2026-08-14 ruling; the favourable half moves to leverage by Jordan's answer A-25"* | DICE res. 9; F-DICE-10 |
| 2 | `engine/dice_engine/dice_engine.py::degree_from_net` | context is validated on entry, before the band is decided; context with `extension=None` raises `TypeError` | res. 11; F-DICE-11 |
| 3 | `engine/season/seam/contest.py:184` | the unread `extension` parameter and its word in the docstring are deleted | res. 12 |
| 4 | `engine/dice_engine/sigma_leverage.py:114` | `OB_MIN`'s tag: *"the floor a favourable modifier may not push an obstacle below"*, not "Ob minimum" | res. 20 |
| 5 | F-DICE-13's lines: `dice_engine.py:6-8`; `engine/dice_engine/__init__.py:8`; `sigma_leverage.py:5-9`; `loop/resolve.py:887-888`; `requirements.yaml`'s social-contest scale note; `modules/mass_battle/resolution.py:43-46` | each corrected at its line to the present state (the package is the ruled owner, not a provisional stub; `verb_capability` names three inquiries; the provider is built and the kernel is not reached; the volley path delegates) | res. 14 |
| 6 | `hole_register.yaml` H-152 | head CLOSED, citing CP-T02-01 and the three-arm probe (`total`: 8 removed, 8 named by `person.died`; control 0 and 0; mutation 8 and 0); `owner:` `state/gate.py::death_subjects` | addendum §3 |
| 7 | `hole_register.yaml` H-31 | `grade: ruled`, citing the 2026-08-14 and 2026-08-15 rulings | res. 16 |
| 8 | `hole_register.yaml` H-88 | closed: `seam/contest.py:245-283` dispatches by manifest row | §6.1 |
| 9 | `hole_register.yaml` H-98, H-114, H-115; `requirements.yaml` R-09 `blocks:` | H-98 closed (combat's three bands are data and ruled off the scene; nothing keys a fourth) and removed from R-09's `blocks:`; H-114 and H-115 heads say CLOSED | res. 15; §6.1 |
| 10 | `engine/dice_engine/sigma_leverage.py::band_odds` docstring | the sentence that combat reads `p_success` is removed (under §1 the closed form is every provider's odds) | res. 13 |
| 11 | the gates of two DICE proposals | `10_DICE_one_score_two_roles.md`'s gate gains a row at an obstacle below `OB_MIN` (an opponent of rank 0); `10_DICE_advantage_sources_for_the_arcs.md`'s gate gains: at the largest stack of levels against, the chance is not under the per-pool floor (§1 row 3) | `16_PESSIMIST_DICE.md` §1.2, §7 |

**Gate.** `register --check` shape passes for the edited rows; the lower-band probe of the DICE audit's
E-04 (`degree_from_net(2, 0, extension=E(), poool=8)`) raises; headless hash EQUAL for rows 2–4.

## §4 · A failed search is remembered by the one who searched (F-PES-DICE-05)

The pessimist's control showed that depositing `finding.none` changes nothing by itself (failed inquiry
aims tried again 19 of 42 against 20 of 47): the missing piece is a reader. The reader exists in this
suite: `16_PESSIMIST_CORE_a_refusal_is_remembered.md`'s `person_q.refused_before`, which weighs a held
claim whose predicate is in the row's `emits_on_refusal`. `finding.none` is such a kind and is never held,
because `rosters.yaml: undeposited_kinds` skips it for everyone.

**Edit, owner `engine/season/rosters.yaml: undeposited_kinds` and `loop/witness.py`.** The roster's row for
`finding.none` becomes actor-only: the Event deposits to its own doer (the `witness_key` channel's rule,
*change claims about self*) and to nobody else. This is the narrower skip the roster's own note names
(H-111, *Jordan to correct*). Behind a fixture arm (`finding_none_deposit: none | actor`; control `none`).
No other reader is added: `admission_weight` then discounts a search he remembers failing, until the claim
fades or news of the subject lands.

**Gate.** Seeds 0–2, two seasons, both arms: failed inquiry aims tried again fall at the `actor` arm with
`refusal_memory` above 0, and do not fall at `refusal_memory` 0 (the pessimist's control, reproduced);
deposits to non-actors equal across arms. **Falsifier.** The retry share is unchanged with both edits in.
**Hash movers.** The `actor` arm. **Dependency.** `16_PESSIMIST_CORE_a_refusal_is_remembered.md`;
`01_CORE_claim_fade_as_read.md` (the claim's present confidence). The neighbouring case of a missing
person is D-46 (taken B by the ladder) and is the verbs lane's.

## NERS reading (E last)

**N.** §1 is Jordan's answer made executable; without it two samplers stand and the port carries both.
§4 gives the search the memory its own row said it lacked. **R.** Fractional pools and obstacles are native,
leverage is uniform at every pool, and no pool under five dice exists to starve a band. **S.** One sampler,
one closed form for shown and believed odds, one channel for a wound in a fight and in a debate.
**E (last).** Five functions and two test files leave; one closed form and one fixture arm enter.

## Cost class

§1: small build plus one calibrated re-pin. §2: as its proposal. §3: edit. §4: edit behind an arm.
