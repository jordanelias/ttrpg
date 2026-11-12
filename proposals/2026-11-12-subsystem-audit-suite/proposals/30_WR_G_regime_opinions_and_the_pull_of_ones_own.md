# WR-30-G — what a regime shares, and what it asks: opinion axes as data, a core and a fringe, and the unsaid pressure of one's own circle

Folded: 2026-11-12 by `audits/31_HOUSE_STANCES_AND_CAST_VALUES.md` (Jordan's A-87 to A-90). Nothing here is deleted. (1) **Commit 2 is completed** by `31_WR_A_house_cores_and_the_cast_on_the_opinion_axes.md` §4: the 46 rows' values (57 cells grounded, 106 assumption, 67 no key), derived from the houses' cores Jordan gave; the INCOMPLETE mark is removed here and nowhere else. The owner file is `references/npc_registry.yaml` (`affiliations:`), not `engine/season/npcs.yaml` as commit 2 below says. (2) **Commit 1 is amended, read `31_WR_A` §1 in its place**: five rows, not three (`parliamentary_rule` beside `militarism`, A-87's one line as two poles; `einhir_folk`, A-90); 35 cells, of which `parliamentary_rule × militarism` is `true` and `caste_order × royal_order` and `einhir_folk × einhir_restoration` are `false`; and **no `concerns:` key**, because the three keys of §2 below make `data/cast.py::conviction_of` (`:253-262`) refuse every cast row (audit 31 F-31-01, probe P-31-5: 46 of 46). A `vowed:` list keeps the shared vow column off the new members. (3) **Core and fringe**: with ten axes this file's core (the exact creed set) is 25 sets among 46 persons (F-31-04); `31_WR_A` commit 3 adds the six authored **regime cores** as data and `world_q.core_standing`, which reads each person's distance from a core row (`person_q.closeness`); `accord` (commit 3 here) stays the credit form of commit 4. (4) **The link** A-87 names ("unhappy royal order due to caste") is `rosters.yaml: tables.opinion_links`. (5) **Commit 5's `circle_of`** is reused by `31_WR_B_the_revival_gathers.md`, where the pull of one's own also bears on a stand (one die in a drawn step), not only on approach.

## Status: PROPOSED (the roster rows are amended and the cast's values authored by `31_WR_A`; every cell there marked `a` is `[ASSUMPTION; Jordan to correct]`)

Source: Jordan, 2026-11-12, as `unified/DECISIONS_ANSWERED.md` records them. **A-82**: *"regimes also share to some extent common opinions on caste, religion, politics, Altonia, militarism, etc"*. **A-83**: *"regime not only who believes whom but also some commonality in thoughts opinions approaches (still individuals, but it's like having unsaid pressure from around you to behave in a particular way)"*. `audits/30_ERAS_REGIMES_STRIFE_AND_MOMENTUM.md` F-30-05, F-30-12. Reference only (`CLAUDE.md` §0.05). Lane WR with CHAR; owner files `references/descriptor_registry.yaml`, `engine/season/rosters.yaml`, `engine/season/queries/`.

Extends `30_WR_B_regimes_who_believes_whom.md` (whose "body" is this file's **core**) and `20_NARRATIVE_A_stands_for.md` (the one reading of "stood for"). Composes on `20_NARRATIVE_D` (a faction's `creed:`), `16_PESSIMIST_CHAR_A` (the drawn crisis, A-24), A-34 (self-knowledge), `11_GO_player_surface_contract_B.md` (the offer).

## What it changes in `engine/season/` at runtime

| commit | change | hash |
|---|---|---|
| 1 | three affiliations join the roster; eighteen `incompatible` cells keyed `null` | EQUAL (nobody holds the new ones); `engine/engine_params/descriptors.json` re-derived (the port's file moves, declared) |
| 2 | the cast's intensities on the new poles | authored in `31_WR_A` §4 (was INCOMPLETE); a declared build-hash mover |
| 3 | `world_q.accord`; `regimes` reads a core and a fringe | EQUAL (readings) |
| 4 | the credit factor may read the graded accord in place of the sign, behind `Fixtures credit_form` | EQUAL at `sign` (control); `accord` a **declared mover** at every telling between two persons with a shared axis |
| 5 | the pull of one's own: a person's axis weights lean toward the custom he believes his circle keeps, behind `Fixtures custom_shift` | EQUAL at 0 (control); above it a **declared mover** for every person who holds a claim of a deed by one of his circle |

## 1. Which opinion axes exist (verified at `2600cb0`)

| Jordan's question | a conviction pole today? | where the tree has it |
|---|---|---|
| **religion** | **yes** | `solmund_orthodoxy`, `inner_tradition`, `thread_truth` (`references/descriptor_registry.yaml:220-222`); `einhir_restoration` as the counter-theology (`:223`) |
| **Altonia** | **yes** (the suspicion that it is missing is wrong) | `altonian_civics`, "the Altonian imperial order as the political structure one wants" (`:224`); concern `altonia` (`:228`) |
| **politics** | **in part** | `altonian_civics` is a political pole; there is none for the kingdom's own order. `political_authority` exists as a goal axis (`rosters.yaml: thrust_axes`, `:2358-2361`), which is what a faction pursues, not what a person holds |
| **caste** | **no** | descent is a fact about a person (`heritage_roster`, `descriptor_registry.yaml:236-247`), read as regard by believed descent (`person_q.heritage_regard`, CR-31); `uphold_caste` and `overthrow_caste` are goal axes (`rosters.yaml:2361`); A-41 gives caste three expressions (regard, vote blocks, tiered rights). No affiliation says what a person thinks of the order of descent |
| **militarism** | **no** | `military-order` is a faction role template (`rosters.yaml:2086-2107`), a profile of pursuits. No affiliation says what a person thinks of rule by arms |
| *approaches* (A-83) | **yes, and not as affiliations** | the seven bipolar axes (`descriptor_registry.yaml:178-189`: rank or equality, precedent or the new, one's own or the impartial, self or others, rigid or flexible, forward or humble, rule or outcome), onto which pursuits project and against which every verb and every deed kind is aligned (`data/verbs.py::align_kind`) |

So an opinion in A-82's sense is a position on the affiliation roster (`Person.conviction`, 0 to 5, read signed by `person_q.conviction_stand`, `:456`), and an approach in A-83's sense is a lean on the seven axes. Both are data the engine reads. Three rows are missing.

## 2. The rows (commit 1), `[ASSUMPTION; medium; Jordan to correct; revert: delete the row and its cells]`

```yaml
# references/descriptor_registry.yaml: affiliation_roster   (count: 5 -> 8)
    - caste_order      # the order of descent as right: who may hold, earn and command by birth (A-41's informal tiers, held as a position)
    - militarism       # that arms, and those who bear them, should decide the realm's affairs
    - royal_order      # the kingdom's own order of crown, duchies and bench as the political structure one wants (the native counterpart of altonian_civics)
  concerns:
    caste: [caste_order]
    arms: [militarism]
    crown: [royal_order]
```

Names are plain words; none is a canon name, and none is taken from research (`rosters.yaml`'s source-precedence ruling). `rosters.yaml: tables.incompatible` gains the eighteen new pairs, **every one `null`** with the comment "no source either way": this file invents no strain. In particular `altonian_civics × royal_order` and `caste_order × einhir_restoration` are left `null`; whether either strains is Jordan's content. `affiliation_engagement` gains no cell (its default is `null`). `heritage_roster.engages` is untouched.

## 3. Sharing "to some extent": accord, a core and a fringe

- **Accord** of two persons is graded: the mean, over the affiliations both have considered (a key present in both `conviction` maps), of the product of their signed stands (`conviction_stand`: for at +1, against at −1, lukewarm near 0). Two who are both firmly for, or both firmly against, agree; one for and one against disagree; an axis only one has considered says nothing. 0 when they share none.
- A regime keeps `30_WR_B`'s definition (a creed set with seats). Its **core** is the persons who stand for exactly that creed set. Its **fringe** is every other person who stands against no member of the creed and whose mean accord with the core's members is above 0. A person is in the core of at most one regime and may be on the fringe of several: that is "to some extent".
- **Edges move as opinions move**: a crisis of faith drawn (A-24) moves a man from a core to a fringe or across; what he comes to believe of his own motives (A-34) can move him; a persuasion (`argue`) moves him one step. None is a membership flag; each is a change in `Person.conviction` by a drawn act, and the reading follows.
- **Who believes whom**, graded: at `credit_form: accord` the credit factor is `1 + regime_gain × accord` in place of `1 + regime_gain × c` with `c` in {−1, 0, +1}. A fringe teller is believed more than a stranger and less than one of the core. This is inside the ratified assumption A12, whose listed revert is "any other monotone form" (`strife-00` §10). The ruled sign form stays the control.

## 4. The pull of one's own (A-83)

**The constraint, kept.** A modifier is read from the acting person's own interior or edges, never from a flow or a count of the world (`audits/20_NARRATIVE_CHURN.md` §7.3; `ED-IN-0352`), and no one is omniscient. So the pressure is read from **what he himself holds about those around him**: his claims of the deeds of his circle.

- His **circle** is the doers his own ledger names who are live members of his faction or are housed where he is housed. Which of the names in his ledger those are is the World half, computed resolver-side and handed down as a tuple, as `world_q.opinion_of` hands down `regarded` (`:3055-3062`). He himself is never in it.
- The **custom** he believes his circle keeps is an axis vector: over his claims (inside the estimate window) of deeds done by the circle, the sum of each deed kind's alignment on each axis (`align_kind`, the table `person_q._lean` reads, `:418-421`), weighted by the claim's confidence, scaled to unit length. It is what he has seen and been told they do, so it can be wrong, stale or partial, and a man new to a place holds none.
- **Where it enters: his own axis weights.** `projected_axes(p, shift)` (`person_q.py:895`) already shifts a person's weights by his scars (`scar_weight_shift`, H-187). The custom is a second shift of the same kind: `axis_w' = (1 − k)·axis_w + k·‖axis_w‖·custom`, where `‖axis_w‖` is the length of his own vector (so the lean never makes him care more in total, only differently) and `k = custom_shift`. One vector then serves both readers that exist: how he **judges others' deeds** (`deeds_judged` → `regard` → the stance term) and what he is **inclined to do, and in what manner** (the pursuit term: the same act aligned with the custom ranks a little higher, one against it a little lower). No new term is added to the score, nothing under `decision/` reads the World, and the choice stays a sampled order.
- **He remains himself.** At `k` below 1 his own pursuits dominate; a strong conviction or pursuit outweighs the lean; the sample still takes unlikely rows.
- **Resisting costs, by what is already built.** An act against the custom, seen by one of the circle, is a deed that circle member judges by his own weights (which lean the same way): his regard for the actor falls (`deeds_judged`), it is told along the regime's own lines and believed there, and where the act violates an affiliation the observers hold it scars them (`affiliation_engagement`). That is the cost, and it is a story: the man who would not do as his house does. Bending is the sample falling with the custom; breaking is leaving (A-46) or moving, after which his circle, and so the custom he feels, is a different one.
- **A regime's commonality of approach** is then emergent and readable: persons of one core see each other's deeds, lean toward the same custom, and act alike; the harness prints, per regime, the mean custom of its core.

**Entrenchment and stillness (A-80, A-81).** A custom is a held position. What it produces: the deviant's cost above, a circle that argues with him or shuts him out, and a second custom wherever a few deviants see each other (a faction of opinion forming inside a house). The pull adds no outcome that writes nothing: it changes ranks only.

## Instructions to code

Tier: commits 1, 3 second tier (sonnet); commits 4 and 5 third tier (opus) for the placement, with a second-tier critic; commit 2 is authoring.

**Commit 1 (EQUAL).** (a) `references/descriptor_registry.yaml: affiliation_roster`: `count: 8`, the three names and three `concerns:` keys of §2. (b) Re-derive: `python tools/export_descriptors.py` then `python tools/export_descriptors.py --check` (never hand-edit `engine/engine_params/descriptors.json`). (c) `engine/season/rosters.yaml: tables.incompatible.cells`: the eighteen pairs, `null`, keyed once each (the half-matrix loader refuses a pair keyed twice, `data/affiliations.py`). (d) Tests: the covering files are `engine/season/tests/test_h10_affiliations.py`, `test_h11_affiliation_scar.py`, `test_in64_cast_integration.py`, `test_rem30_character_sheet.py` (found by `grep -rl AFFILIATIONS engine/season/tests`); any count of five or ten pairs they pin is re-pinned to eight and twenty-eight, said in the commit. Add `test_h10_affiliations.py::test_a_new_affiliation_nobody_holds_moves_no_hash` (`build_realm(0).content_hash()` before and after).

**Commit 2 (completed by `31_WR_A` commit 2, whose instructions replace this paragraph; kept as lane 30 wrote it).** The 46 cast rows' intensities on `caste_order`, `militarism`, `royal_order` (`engine/season/npcs.yaml` rows, read by `data/cast.py::conviction_of`, `:234`). **What is missing:** the values. They are Jordan's content; this lane derives none (a value read off a faction template or a heritage would be a guess, and `conviction_of` "reads and validates, it does not guess"). Two ways to complete it, either sufficient: (i) Jordan authors them; (ii) `21_PROCEDURAL_B_cast_and_seats.md`'s generation tables gain a rule that draws them (A-44, A-50), with its own sweep. Until then the three poles are held by nobody and every reading of them prints `n/a (unheld)`.

**Commit 3 (EQUAL).** `engine/season/queries/world_q.py`, beside `commensurate` (`:5317`).

```python
def accord(w: World, a: str, b: str) -> float:
    """[-1, +1]: the mean over affiliations BOTH have considered (a key in both `conviction` maps) of
    `conviction_stand(pa, x) * conviction_stand(pb, x)`; 0.0 when they share none or either is gone.
    Graded and symmetric. `commensurate` stays the sign form (A12); this is its listed other form."""
```

`Regime` (`30_WR_B` commit 1) gains `fringe: tuple = ()`, filled by `regimes`: persons not in the core who stand against no member of `creed` (`conviction_stand < 0` on none) and whose mean `accord` with the core is above 0. `harness/storybar.py --regimes` prints `core=<n> fringe=<n>` and, per person on more than one fringe, the regimes. Tests, `engine/season/tests/test_strife_credit.py`: `test_accord_is_symmetric_and_bounded`, `test_two_who_reject_the_same_creed_agree`, `test_a_person_is_in_one_core_at_most`, `test_the_fringe_stands_against_nothing_the_core_stands_for`.

**Commit 4 (control EQUAL; `accord` a declared mover).** `rosters.yaml`: `credit_forms`, `values: [sign, accord]`; `data/fixtures.py`: `credit_form="sign"`. `engine/season/loop/witness.py::_credit` (`:240-256`): `k = regime_gain * (commensurate(...) if form == "sign" else accord(...))`; the clamp and the untouched-at-zero rule are unchanged. Flip only on the strife guard passing and not blind, as CR-79 shipped `regime_gain` (H-275's method). Test, `tests/test_strife_credit.py::test_a_fringe_teller_is_credited_between_a_stranger_and_the_core`; `test_credit_form_sign_is_byte_identical`.

**Commit 5 (control EQUAL; above 0 a declared mover).**
1. `data/fixtures.py`: `custom_shift=0.0`, swept `0` (control, SHIPPED) / `0.25` / `0.5`, refused outside `[0, 1)`; a NUMBER row in `hole_register.yaml`, `[ASSUMPTION; medium; Jordan to correct; revert: 0.0]`.
2. `engine/season/queries/person_q.py`: `def custom_of(p: Person, circle: tuple, window) -> dict` returning `{axis: float}` (unit length, or `{}`), from `attributed_deeds(recent_claims(p.ledger, window), m)` for each `m` in `circle` (the readers `legitimacy` uses, `:556-557`), each deed's `align_kind(kind, axis)` times `Claim.confidence`. Person-side, no World.
3. `projected_axes(p, shift, custom=None, k=0.0)` (`:895`): with `custom` empty or `k` 0 it returns today's vector exactly; else the blend of §4.
4. `engine/season/queries/world_q.py`: `def circle_of(w, p) -> tuple`: the doers `deed_doers(p.ledger, {"kinds": DEED_KINDS}, p.id)` names who are in `members(w, faction_of(w, p.id))` or whose `home_map` rung is his; sorted; never `p`. It rides the `View` the resolver builds for him (the route `View.odds` rides, `decision/sheet.py:40-41`), so `decision/` holds no World.
5. `decision/choose.py::deliberation_memo` (`:130-141`): `_AXIS_W` is `project(p, shift, custom_of(p, view.circle, window), k)`; the `make_chooser` path and `harness/decision_spread.py` both take it from here (the memo's own reason for existing). `person_q.deeds_judged(p, referent, scar_shift, axis_w=None)` (`:97`) takes the weights when they are passed and computes `projected_axes(p, scar_shift)` as today when they are not; `regard` (`:424`) forwards an optional `axis_w`; `decision/choose.py`'s stance term, which already caches `regard` per subject in the memo, passes `memo[_AXIS_W]`. Every other caller of `regard` (the harness estimates, `teller_weight`) passes nothing and reads today's value.
6. `hole_register.yaml`: LOOP row **L16 custom**: "custom believed, acts aligned, seen by the circle, custom believed"; sign `+`; bounds: `custom_shift` below 1, the estimate window, `_sample_order`, `scene_budget`, turnover of the circle (death, `migrate`, `release`); switch `custom_shift` 0.
7. Tests, `engine/season/tests/test_custom.py` (new): `test_custom_shift_zero_is_byte_identical`; `test_a_man_with_no_claims_of_his_circle_feels_nothing`; `test_the_same_candidate_ranks_higher_when_his_circle_is_seen_to_do_its_like` (planted ledger, fixed sample); `test_he_judges_a_deed_more_as_his_circle_would`; `test_a_stranger_s_deeds_do_not_move_him`; `test_the_pull_reads_no_world` (the AX-2 path scan of `tests/test_season_shape.py` covers `decision/`; this asserts `custom_of` takes no `World`). `assert checked >= 6`.

## The gate (execution artifacts)

```sh
python tools/export_descriptors.py --check
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 4 --arms off off --regimes
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 5 --seasons 6 --arms custom_off custom_on --stories --crossings
python -m pytest engine/season/tests/test_h10_affiliations.py engine/season/tests/test_strife_credit.py engine/season/tests/test_custom.py -q
```

Expected. Commit 1: `--check` passes; `build_realm(0)` hash EQUAL. Commit 3: each regime line prints a core and a fringe; with `held_reading: stands` the cores are `20_NARRATIVE_A`'s six sets and at least one person is on a fringe. Commit 5, the on arm against `custom_off` (the pressure-off control `30_WR_E` carries as arm `custom_off`): (1) the share of executed acts whose verb aligns with the actor's believed custom (dot above 0) is higher in the on arm by more than the off arm's seed spread; (2) shape E-10 of `30_WR_E` (a man acts against his circle's custom, is seen, and is answered) occurs at two seeds or more in the on arm; it is not required to be absent in the off arm (deviance exists without pressure), and what is required is that its rate differs between the arms by more than the off arm's seed spread; (3) the no-null-scene reading is unchanged between arms and executed acts per person-season in the on arm are not below half the off arm's (a conforming world still moves, A-80); (4) on one built world, four draw seeds do not give four equal vectors (the pull is not a script).

## The falsifier, and its control

- Two persons choosing identically at every question once they share a circle: the pull has become a determinant; lower `custom_shift` or the form is wrong.
- The aligned share equal between arms within the seed spread: the pull is inert at that gain; the row is recorded `inert`, and the gain is not raised to pass.
- Any hash moving at `custom_shift` 0, `credit_form` `sign`, or after commit 1.
- A person's custom moving with no claim landing in or fading from his ledger: it read the World.
- Control arms: `custom_off`; `credit_form: sign`; and for commit 1, the roster of five.

## Dependencies

`20_NARRATIVE_A` (stood for), `30_WR_B` (commit 1, 2). Commit 5 after `01_CORE_claim_fade_as_read.md` if the window is to fade smoothly; it lands without it on the hard window. Feeds `30_GO_F` (the circle's expectation on the offer), `30_WR_E` (shape E-10, arm `custom_off`), `30_WR_D` (L16).

## Layer 1

AX-2 (`decision/` reads no World): kept, **STRUCTURAL**; the circle rides the View, the custom is read from his ledger. AX-7 (a reading of the world, never the world): kept, **STRUCTURAL**; the custom is what he believes they do. `ED-IN-0352`'s FORBIDDEN list (a weight inside `decision/`; a term keyed on identity; a flow read into choice): no term is added to the score, no id is tested, no flow is read; the shift is the `scar_weight_shift` precedent. Named at the site because two careful readers could differ on whether a shift of the axis weights is "a weight inside `decision/`": it is computed in `person_q` and enters by the memo, as the scar shift does. **MECHANICAL** (the path scan and the fixture control check it). ID-16: L16 declared, **MECHANICAL**. A12 (the credit form): commit 4 is within its revert, **CONVENTION**.

## NERS reading

- **N.** Without the rows a regime cannot share an opinion on caste or arms, which Jordan names; without the pull a regime changes what is believed and not what is done. Holds bottom-up (one man, his house), top-down (a regime acts alike), laterally (the same weights judge and choose), diagonally (what he believes they do against what they do). Narrowed: the new poles do nothing until the cast holds them.
- **R.** Customisation: a designer adds an opinion as a roster row. The deviant, the convert and the newcomer are each a story with no player in it. Complete: no circle, no pull; no claims, no pull.
- **S.** One vector for judging and for choosing; one window; the scar shift's own channel. Nothing pauses.
- **E, last.** One blend and one tuple on the View, against a whole second way a regime acts. High, and it would be low if it added a score term.

## Cost class

Edit (1). Authoring, carried by `31_WR_A` (2). Small build (3). Edit, a declared mover (4). Small build, a declared mover (5).
