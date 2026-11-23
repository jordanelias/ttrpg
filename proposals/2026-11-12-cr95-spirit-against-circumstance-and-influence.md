# CR-95: Spirit against circumstance and influence

## Status: PROPOSED (2026-11-23). Workplan v12 position B10.52 (Batch B10-character, lane IN), the design half of CR-95; its build is `B10.81` (HELD). A design: reference under `CLAUDE.md` §0.05, binding nothing and resolving nothing. No file under `engine/` changes with it. Every take is marked `[ASSUMPTION; Jordan to correct]` and reverts alone.
## Lane: IN
## Reads: `references/descriptor_registry.yaml` (`attributes`, `capabilities`) · `engine/season/verb_table.yaml` (`opposed_attribute:`) · `engine/season/seam/wrappers/pool.py` (`register_pool_addend`, `opposing_attribute`) · `engine/season/seam/wrappers/sigma.py` (`_opposing`, `OBSTACLE_TERMS`) · `modules/social_contest/roll.py::obstacle` · `modules/combat/combatant.py` (Spirit as strain) · `proposals/2026-11-05-attribute-rulings-adjudication.md` §2.2 (ii), (iv) ("adj §2.2") · `proposals/2026-11-08-sc02-reception-proofs-own-commit-design.md` (PROPOSED; read, not built)
## Base read: the working tree at `43da21c37`. Every number below is the output of a command quoted beside it, or is marked `[ASSUMPTION; Jordan to correct]`.

**The four questions** (v11's REMAINING UNBUILT, copied by v12 B10.52): (1) which verbs are opposed by Spirit, written as opposition on the owner the registry now names; (2) which ADVERSE instance modifiers Spirit discounts, never `base_Ob`, never TN, never below `base_Ob` or `OB_MIN`; (3) whether a pool addend is used anywhere instead; (4) the Grace and Spirit boundary. Each answer below carries its falsifier. The `resolution-diagnostic` run on the resolving form is §6, quoted as evidence, not as a verdict.

**The ruling this composes on.** AR-44 (ED-IN-0347, RULED), verbatim from `proposals/2026-11-05-attribute-rulings-by-subject.md:100`: *"spirit/willpower concerns the ability to stay true to yourself and be free of external influence or compulsion, the capacity to tolerate harm and strain and stress, the likelihood to perform threadwork without losing coherence, the ability to get good results despite poor circumstances, to overcome an obstacle. in different contexts you can see it as ignoring obstacle modifiers or adding modifiers to dice pool"*. ED-IN-0348 folded the adjudication that turns it into CR-95. ED-IN-0251 (convictions) is not displaced: Spirit resists a change to what a person holds (adj §2.1). ED-1041 is the combat wound channel read in §2.2.

**Sources the entry cites by short path.** `proposals/2026-11-12-subsystem-audit-suite/` exists in the tree. This design read the adjudication ("adj §2.2", at `proposals/2026-11-05-attribute-rulings-adjudication.md`, not under the suite), the governing-attributes proposal (`proposals/2026-11-12-subsystem-audit-suite/proposals/2026-11-13-verb-governing-attributes.md`) and the entry's own copied INSTRUCTION. The intake, `master/eval/E1.md` and `E4.md` were not opened: the entry copies v11's text, and the tree, not the intake, says what is built.

---

## 0. What Spirit already does, read off the code

| where | what Spirit does today | opened at |
|---|---|---|
| the social roll's obstacle | the person OPPOSITE resists with his skill score PLUS his score in the verb row's `opposed_attribute:`; that sum is the `opposition` member, `opposed_ob(sum, opposition_rate)` | `engine/season/seam/wrappers/pool.py:100-112` (`opposing_attribute`), `engine/season/seam/wrappers/sigma.py:126-135` (`_opposing`), `modules/social_contest/roll.py:121-123` |
| the pool | Spirit is a `governing:` attribute of one verb, `thread_read`, through `governing_score` (the attribute route, not an addend) | `engine/season/verb_table.yaml:2036` (row), `pool.py:76-91` |
| combat | strain: the wound interval (`+0.4·Spirit`), the stamina reserve (`+2·Spirit`), the concentration reserve (`+2·Spirit`) | `modules/combat/combatant.py:17, 24, 32-34, 42-44, 172`; `modules/combat/config.py:113` (`CONC_SPIRIT=2.0`) |
| combat's obstacle | nothing: `ob_from_defender` adds no instance modifier, by its own docstring | `modules/combat/core.py:86-105` |

The opposition half of CR-95 is therefore already built (B05.14, B05.16, B05.25). What is unbuilt is the circumstance half: the actor's own Spirit against the adverse modifiers on his own roll.

**One correction to the entry's premise.** The entry reads `opposed_by` as "a column of its definition row (`descriptor_registry.yaml: capabilities`, `B04.02`)". That column is gone: B05.25 moved which attributes a verb reads onto the verb row (`references/descriptor_registry.yaml:69-71`; `engine/season/data/verbs.py:1394-1396`, *"The skill row's `base:` and `opposed_by:` columns, and `VOCATION_ATTRIBUTE` and `VOCATION_OPPOSED_BY` read off them, are deleted"*). The owner of "who resists with what" is the verb row's `opposed_attribute:` cell, validated at import by `data/verbs.py::_check_governing_attributes` (`:692-736`: a row contested against a person on a `pool` prize must name one).

---

## 1. Which verbs Spirit opposes, and which owner holds it

**Measured.** Command:

```
python3 -c "import yaml; d=yaml.safe_load(open('engine/season/verb_table.yaml'))
for v in d['verbs']:
    if v.get('opposed_attribute') or v.get('counterparty'): print(v['verb'], v.get('capability'), v.get('opposed_attribute'), v.get('counterparty'), v.get('contests'))"
```

Output, the rows that name an opposition (rows with a counterparty and no opposition — `confer`, `covenant`, `give`, `issue`, `challenge`, `oblige`, `petition`, and combat's `capture` and `accept` on `the body`, `person_inputs: own` — omitted):

```
argue       |cap argue   |opp attr.spirit.will        |cp to      |contests a proposition
arrest      |cap arms    |opp attr.body.strength      |cp subject |contests a standing
determine   |cap argue   |opp attr.spirit.will        |cp subject |contests a proposition
lie         |cap none    |opp attr.social.attunement  |cp to      |contests a standing
seize       |cap None    |opp attr.spirit.will        |cp None    |contests None
speak       |cap copying |opp attr.spirit.will        |cp None    |contests a matter
tell        |cap copying |opp attr.spirit.will        |cp to      |contests a standing
interrogate |cap inquiry |opp attr.spirit.will        |cp subject |contests a proposition
```

**The answer.**

| verb | Spirit? | level | owner today | owner after B24p.19 |
|---|---|---|---|---|
| `argue`, `tell`, `speak`, `interrogate` | **yes** (influence; interrogation is compulsion) | verb-level, never a skill's | `verb_table.yaml` `opposed_attribute: attr.spirit.will` (`:100`, `:1778`, `:1641`, `:1949`), read by `pool.py::opposing_attribute` | the proceeding's opposition, "the listener's Will plus rank" (`workplans/valoria_master_workplan_v12_part22_b24p_cont.md:104-114`: B24p.19 step 3 deletes the cell on these rows; its control names "the listener's Will plus rank" at `:114`) |
| `determine` | **yes** (a ruling compels the party) | verb-level | `opposed_attribute:` (`:371`) | unchanged by B24p.19 (B24.08 owns `determine`) |
| `lie` | **no**: a lie is detected, not resisted | verb-level | `opposed_attribute: attr.social.attunement` (`:569`) | the proceeding |
| `arrest` | **no, pending BA1.13** | verb-level | `opposed_attribute: attr.body.strength` (`:145`) | unchanged |
| `seize` | cell names Spirit, **inert** | verb-level | `opposed_attribute:` (`:1611`) on a row with no prize, no counterparty and no `difficulty:` cell, so nothing reads it | unchanged |

- **No skill row carries an opposition, and none is to be added.** One skill serves verbs that rely on different attributes (`inquiry` serves `examine`, `surveil`, `research`; `descriptor_registry.yaml:69-71`). A skill-level `opposed_by` would be a second owner of what the verb row already says.
- **(1)'s data edit is none.** Every influence row Spirit should oppose already names it. v11's "(1)'s data edit a MOVER wherever a resisting person has authored Spirit" was written before B05.14 and B05.25 landed the cells; that edit has happened, and `B10.81` inherits no data edit for (1).
- **`arrest` is not CR-95's to change.** Adj §2.2 (iv) names arrest among the acts Spirit opposes; the later B05.25 cell reads Strength, marked `[ASSUMPTION; medium; Jordan to correct at BA1.13]`, and the governing-attributes proposal's §6 Q1 (`:346-353`) asks whether resisting arrest is a contest of standing or of the body. The two readings line up with that question: a standing contest (submission to authority) is AR-44's "compulsion" and would be Spirit's; a bodily one is Strength's. CR-95 records the link and takes no edit `[ASSUMPTION; Jordan to correct; revert: Spirit on arrest, with adj §2.2 (iv)]`.
- **`seize`'s Spirit cell is a declared field with no reader** today (the loader leaves an unrolled kind-(b) row alone, `data/verbs.py:698-699`, its docstring: *"its draw is B07's"*). Kept: deleting it is B07's call when a draw is routed to the row, not this design's.

**Falsifier (1).** Wrong if a row contested against a person on a social-roll prize (`a standing`, `a proposition`, `a matter`) that is not `lie` or `arrest` names an opposition other than `attr.spirit.will`, or if any `capabilities` row in `references/descriptor_registry.yaml` carries an `opposed_by` key. Both are read by the command above (zero offending rows at `43da21c37`) and by `grep -n opposed_by references/descriptor_registry.yaml` (no output at `43da21c37`: the capability rows `:77-83` carry no such key). After B24p.19 the same falsifier is asked of the proceeding: the listener's opposing attribute is Spirit for the five influence rows.

---

## 2. Which ADVERSE instance modifiers Spirit discounts

### 2.1 The social roll: what each obstacle member is, and whether Spirit discounts it

The obstacle has one form and one owner (`modules/social_contest/roll.py:82-161`): `hard = even + difficulty + opposition + Σ raw_i·step_i (+ forgery)`, then the ceiling (H-213), then `max(OB_MIN, ·)`. The members are the closed roster `rosters.yaml: obstacle_terms` (`engine/season/rosters.yaml:1632`): `[even, difficulty, opposition, standard, stakes, regard, reception, capability]`. Every member is non-negative and the module refuses a negative one (`roll.py:125-127`).

| member | what it is (`sigma.py` host function) | Spirit discounts it? | why |
|---|---|---|---|
| `even` | the pool's even line (`:590`) | **no** | `base_Ob`: the scale of the roll itself |
| `difficulty` | the act's own level (`:596`) | **no** | `base_Ob`: the task |
| `opposition` | the person opposite: skill + his own opposing attribute (`:607`) | **no** | `base_Ob`: that is the OTHER man's Spirit (§1); the actor's Spirit does not lower another's resolve |
| `standard` | what the room demands of conduct (`:662`) | **no** | Grace's lane (§4): resolve does not supply manners |
| `stakes` | the weight of what the act takes or imposes (`:683`) | **no** | a property of the act, not pressure on the actor |
| `regard` | the one counterparty's HOSTILITY to the actor (`:691`) | **yes** | another person's ill will bearing on him: "free of external influence" |
| `reception` | the hearing room's HOSTILITY to the actor (`:613`) | **yes** | the same, from a bench: "good results despite poor circumstances" |
| `capability` | a circumstance that punishes a WANT (`:621`) | **no** | a want of a thing (a seal, a letter) is not overcome by resolve `[ASSUMPTION; Jordan to correct; revert: discounted with the two above]` |
| `forgery` (lane A) | an examined document's quality (`roll.py:131-135`) | **no** | a property of the object |

**The set Spirit discounts is `{regard, reception}`: the two members that are other persons' hostility toward the actor.** Both are already the hostile halves only (their favourable halves are leverage, `advantage_sources: favour`), so the discount never touches anything the actor brings.

### 2.2 The form

For the ACTOR's Spirit `S` (his `attr.spirit.will`, on the registry's scale `FLOOR..CEIL` = 1..7, `engine.substrate.descriptors.ATTRIBUTE_FLOOR`/`ATTRIBUTE_CEILING`) and a fixture `k = spirit_discount` in `[0, 1]`:

```
f(S, k) = 1 − k · (S − FLOOR) / (CEIL − FLOOR)          ∈ [1 − k, 1]
value_i = raw_i · step_i · f(S, k)        for i in {regard, reception}
value_i = raw_i · step_i                  for every other member (unchanged)
ob      = max(OB_MIN, bound(even + difficulty + opposition + Σ value_i + forgery))   # the module's form, unchanged
```

- **It lives inside `roll.py::obstacle`**, the obstacle's single owner (ED-SC-0033 clause (3)); the host carries the operands and composes nothing (`sigma.py:35-37`). The record (`queries/inputs.py::SocialContestInput`) gains the actor's held Spirit (`None` where unheld) and the fixture `k`; the discounted set is a closed roster beside `obstacle_terms` (a subset of it, loader-checked), carried in the record as `opposition_rate` is. `[ASSUMPTION; Jordan to correct; revert: the host scales the two raw operands before they enter the record]`
- **Linear from the floor, never an amplifier.** Spirit 1 discounts nothing; each point discounts `k/6` more; Spirit 7 at `k = 1` ignores the two members entirely (AR-44's "ignoring obstacle modifiers"). The form has no dead range on the scale and never raises an obstacle `[ASSUMPTION; Jordan to correct; revert: centred at the scale's mid-point (B05.16's reading), so Spirit below 4 amplifies hostility]`.
- **Unheld Spirit is `None` and discounts nothing** (`f = 1`): a read, not a default, so a hand-built world with no attributes is unchanged at any `k`. Every realm person holds all ten after B01a (`pool.py:101-104`), so this case is the hand-built world's only `[ASSUMPTION; Jordan to correct; revert: read at the mid-point, as the opposition reads an unheld attribute]`.
- **The terms stay non-negative and still sum to `ob`**: the two members are recorded at their discounted values. No negative "spirit" term is written, because a negative member is the Ob-reduction form the module refuses.
- **Advantage is untouched.** The discount is not leverage: it never enters `advantage_sigma`, `levels_to_net_sigma` or `net_boost`, and `base_Ob` and TN are never modified (the TN is fixed at 7: `engine/dice_engine/sigma_leverage.py:77-79`, `PER_DIE` holds the one key `7`).
- **The believed odds follow for free.** `contest_input` and `believed_input` both fill the record through `sigma.py::_frame` (`:721-741`), and the believer is the actor, who knows his own Spirit, so the odds he weighs are the odds dealt.

**What `base_Ob` means here.** `base_Ob` is the obstacle the module composes for the SAME record with both discountable members at 0, ceiling and floor included. The discount cannot take `ob` below it, because `bound` and `max(OB_MIN, ·)` are non-decreasing and every member stays `≥ 0` (§6 measures it). ⚠ Against the RAW sum `even + difficulty + opposition`, the composed obstacle can already sit below the sum: the H-213 ceiling clips it, at any Spirit and at `k = 0`. That is the ceiling's property, not Spirit's (§6, finding F3).

### 2.3 Combat

**No combat discount.** Combat's obstacle carries no instance modifier (`modules/combat/core.py:98-104`), and ED-1041's wound differential is a σ term summed into the net (`modules/combat/combat_systems.py:919-923`, added at `:977`), not an obstacle term. Adj §2.2 (ii)(b) named "the fighter's own wound term" as the combat modifier Spirit could act on; in today's code that term is not an obstacle modifier, and Spirit already acts on it through the wound interval (`combatant.py:32-34`: more Spirit, more damage per wound, fewer wounds). A second route by which Spirit lowers the same wound penalty would be two ladders for one quantity (§0.06 S) `[ASSUMPTION; Jordan to correct; revert: Spirit scales the bearer's own share of `wound_impairment` by f(S, k)]`. Spirit as strain stays as it is; it reaches the season's fights through PC-06 K-1 (`modules/combat/attributes.py:49`, `spirit` ↔ `attr.spirit.will`).

The social roll's `wounds` advantage source (`sigma.py:376-401`) is leverage against the actor, not an obstacle member, so it is outside (2). Not discounted `[ASSUMPTION; Jordan to correct; revert: one fewer `wound_level` against the actor per (CEIL − FLOOR)/k points of Spirit]`.

**Falsifier (2).** Wrong if, for any record, any Spirit and any `k` in `[0, 1]`: `ob(S, k) < obstacle(record with regard = reception = 0)`, or `ob < OB_MIN`, or `ob(S, k) > ob(undiscounted)`, or `ob` rises as `S` rises, or a member outside `{regard, reception}` moves. §6's grid asks all five over 2,772,000 cells on the live module function.

---

## 3. Is a pool addend used anywhere instead?

**No.** AR-44 allows Spirit "adding modifiers to dice pool" in some contexts. The one context where Spirit is the doing itself, threadwork ("perform threadwork without losing coherence"), already has it: `thread_read` names `governing: [attr.spirit.will]`, so Spirit enters that pool through `governing_score`, the attribute route. The door `register_pool_addend` (`pool.py:46-50`) is not used for Spirit:

- An addend is `(w, person, verb) -> whole dice`, summed into every pool `faculty` builds (`pool.py:38-43`, `:161-164`). A Spirit addend would raise the pool of every act he rolls, whatever the circumstance, which makes Spirit a competence attribute; AR-44 makes it resistance. Adj §3.1 (11) already took that no verb needs a second pool attribute.
- On `thread_read` it would count Spirit twice in one pool, through `governing:` and through the addend.
- An addend returns whole dice, so a 1..7 attribute would enter in steps, while the obstacle discount is continuous.

**Measured.** `grep -rn "register_pool_addend(" --include=*.py engine modules`: one production caller, `engine/season/seam/wrappers/pool.py:56: register_pool_addend(practice)`; the other four hits are in `engine/season/tests/` (`test_odds_of.py:352`, `test_u1_two_inputs.py:112, 117`, `test_in12_step9.py:361`). `python3 -c "from engine.season.seam.wrappers import pool; print([f.__module__+'.'+f.__name__ for f in pool.POOL_ADDENDS])"` → `['engine.season.queries.world_q.practice']`.

**Falsifier (3).** Wrong if, after `B10.81`, `pool.POOL_ADDENDS` holds anything but `practice` at import, or if `thread_read`'s pool reads Spirit by any route but its `governing:` cell.

---

## 4. The Grace and Spirit boundary

**Spirit is inner, Grace is outer** (adj §2.2 (iv), on AR-33 and AR-44). Spirit is not being moved: it resists influence and compulsion (the `opposition` member, §1), discounts other persons' hostility on the actor's own roll (§2), and tolerates strain (combat, §2.3). Grace is being seen as composed and correct: it never opposes a roll and never discounts one; it supplies dice where the act is itself conduct, and it is what a formal venue's `standard` asks.

| | Spirit | Grace |
|---|---|---|
| opposes a roll (`opposed_attribute:`) | `argue`, `determine`, `speak`, `tell`, `interrogate` (`seize` inert) | **never** |
| in a pool (`governing:`) | `thread_read` | `carry`, `conceal`, `lie`, `speak`, `recruit` |
| discounts an obstacle member | `regard`, `reception` | **never** |
| the venue's `standard` member | **never** discounts it | the single roll's flat term today (`sigma.py:662-669`); inside a proceeding, Grace's `esteem` on the leverage (B24p.13, B24p.19) |
| regard others hold of the person | — | CR-92's design (Grace reaches regard through what is deposited) |

Measured: `python3 -c "import yaml; d=yaml.safe_load(open('engine/season/verb_table.yaml')); print([v['verb'] for v in d['verbs'] if v.get('opposed_attribute')=='attr.social.grace'])"` → `[]`; the `governing:` lists above are the same command's output for each attribute (`spirit governing: ['thread_read']`, `grace governing: ['carry', 'conceal', 'lie', 'speak', 'recruit']`). The registry's glosses hold the same line: Spirit *"The resolve that resists being swayed or influenced"*, Grace *"Composure, calm, etiquette and manners"* (`descriptor_registry.yaml:54, 59`); "nerve" is Spirit's, narrowed by AR-44 (adj §2.1).

**Where the boundary bites in one act.** A graceless but resolute speaker before a hostile formal bench: the bench's hostility (`reception`) is discounted by his Spirit; the venue's `standard` is not, and his want of Grace still costs him there. A graceful but weak-willed speaker meets the full hostility and passes the standard.

**Falsifier (4).** Wrong if any verb row names `opposed_attribute: attr.social.grace`; if the discounted roster gains `standard`; or if the discount reads any attribute but `attr.spirit.will`.

---

## 5. What the build (`B10.81`) changes, its control and its hash

- **Where.** `modules/social_contest/roll.py::obstacle` (the form, §2.2); `engine/season/queries/inputs.py::SocialContestInput` (the actor's Spirit and `k`, plus the discounted set); `engine/season/seam/wrappers/sigma.py::_frame` (carries them); `engine/season/rosters.yaml` (the discounted set, a closed subset of `obstacle_terms`); `engine/season/data/fixtures.py` (`spirit_discount`, with its NUMBER row). No combat file. No data edit for (1).
- **Control.** `spirit_discount = 0` → `f = 1.0` exactly, so every record composes the same `(ob, terms)`, bit for bit (§6: 0 differences in 2,772,000 cells), and the realm hash is equal. Unheld Spirit → `f = 1.0` at any `k`.
- **Shipped value.** Adj §2.3's rule (a gain ships at its sweep's midpoint where the sweep is monotone and the control reproduces the base, else at its control). Sweep `0 / 0.5 / 1.0` `[ASSUMPTION; Jordan to correct]`.
- **Hash.** EQUAL at the control. At `k > 0`, a MOVER wherever a dealt social record carries a hostile `regard` or `reception` member for an actor with Spirit above the floor and the ceiling does not clip it; §6's realm reading finds 1 such record in 630 over three seasons at seed 0. Declared by the build.
- **Sequence.** After SC-02's re-source (B24.02) `reception` is expected to read 0 in computed play at seed 0 (SC-02 §3c), and after B24p.19 the five influence verbs resolve through the proceeding entry, not `roll.py::obstacle`. The rule (Spirit discounts other persons' hostility on the actor's own roll, never `base_Ob`) carries to whichever obstacle owner those verbs reach when `B10.81` is built; if the proceeding composes no hostility member, the discount reaches the single roll alone (`arrest`, `determine`, the task draws).

---

## 6. The `resolution-diagnostic` report (Phase 0 to 6), quoted as evidence

**Run.** `skills/resolution-diagnostic/SKILL.md` §6, on §2.2's resolving form. Phase 3c was run on the live module function: a scratch script (not kept in the tree; this paragraph is its record) handed `modules/social_contest/roll.py::obstacle` real `SocialContestInput` records with the two discountable members' raw operands scaled by `f(S, k)`. No engine file was edited. Grid: `S ∈ {None, 1, 1.5, 2, 2.5, 3, 4, 5, 5.5, 6, 7}` × `k ∈ {0, .25, .5, .75, 1}` × pool `{0.25, 0.5, 1, 2, 5, 9, 15}` × opposition `{None, 0, 2, 6, 14}` × difficulty `{0, .8, 1.6, 2.4}` (the shipped `difficulty_ob` ladder) × reception raw `{0, .5, 1, 2, 5, 20}` × regard raw `{0, .5, 1}` × ceiling arm `{uncapped; 2 fixed hard; 2 per-pool hard (SHIPPED); 2 per-pool soft; 3 per-pool soft}` × `standard {0, 1.6}` × forgery `{0, 0.7}`, with `pool_add 6`, `pool_default 2`, `opposition_rate 0.4` (the shipped fixtures, read by `python3 -c "from engine.season.data.fixtures import DEFAULT_FIXTURES as F; ..."`). Command: `PYTHONPATH=. python3 cr95_diag.py` (21.9 s). Output, verbatim:

```
GRID cells=2772000
below base_Ob (same record, adverse members at 0, bounds applied): 0
below OB_MIN: 0
discounted obstacle ABOVE undiscounted: 0
CONTROL k=0 != undiscounted (ob, terms): 0
CONTROL S=None != undiscounted (ob, terms): 0
non-monotone in S (ob rose as S rose): 0
non-monotone in m (ob fell as hostility rose): 0
below the RAW sum even+difficulty+opposition at S=7: k=0 -> 28868, k=1 -> 30978
S=7,k=1 with hostility>0: discount moved ob in 23375, inert (ceiling-clipped) in 24225
largest share of the composed obstacle Spirit removed: 0.8974
P-ii  dz of removing 1.0 of hostile reception, by pool (SIGMA_PER_DIE*sqrt(N)):
  pool  1: dz = 1.2500
  pool  4: dz = 0.6250
  pool  9: dz = 0.4167
  pool 16: dz = 0.3125
  pool 25: dz = 0.2500
WORKED  pool 9, routine, opposition 2+4, hostile reception 1.0, shipped arms (ceiling 2, per-pool, hard):
  k=0.0: S=None: ob=6.600 P(>=Partial)=0.1057 | S=1: ob=6.600 P(>=Partial)=0.1057 | S=4: ob=6.600 P(>=Partial)=0.1057 | S=7: ob=6.600 P(>=Partial)=0.1057
  k=0.5: S=None: ob=6.600 P(>=Partial)=0.1057 | S=1: ob=6.600 P(>=Partial)=0.1057 | S=4: ob=6.350 P(>=Partial)=0.1260 | S=7: ob=6.100 P(>=Partial)=0.1488
  k=1.0: S=None: ob=6.600 P(>=Partial)=0.1057 | S=1: ob=6.600 P(>=Partial)=0.1057 | S=4: ob=6.100 P(>=Partial)=0.1488 | S=7: ob=5.600 P(>=Partial)=0.2024
  base_Ob (reception 0): 5.600
CLIPPED  pool 5, hard, opposition 14, reception 2, regard 1: undiscounted ob=5.577, S=7 k=1 ob=5.577, base_Ob=5.577, raw sum=10.400
```

The raw-sum line differs between `k = 0` and `k = 1`, so it was decomposed by a second run over the same grid: *"cells below raw sum at S=7,k=1 whose base_Ob is NOT itself below the raw sum: 0"*; *"of them on the uncapped arm (ceiling None): 0"*; *"cells below raw sum at k=1 but not at k=0, by arm: {(3, True, 'soft'): 1117, (2, True, 'soft'): 993}"*. Every underrun of the raw sum is a record whose `base_Ob` already sits under it, all of them under a ceiling, and the extra cells at `k = 1` are all soft-ceiling cells where the hostile member had been lifting a bent obstacle back over the raw sum.

**Phase 1b, how often it is reached.** A second scratch script wrapped `sigma._read_social_roll` (read-only) and ran `engine.season.harness.populated.run`. Commands and output:

```
PYTHONHASHSEED=0 PYTHONPATH=. python3 cr95_realm.py 0      # seed 0, one season (10.2 s)
seed 0: social records built 217
with a hostile reception/regard member > 0: {}
actor Spirit held (value: count): {1: 36, 2: 34, 3: 30, 4: 28, 5: 37, 6: 52}
PYTHONHASHSEED=0 PYTHONPATH=. python3 cr95_realm.py 2      # seed 2, one season
seed 2: social records built 227
with a hostile reception/regard member > 0: {}
PYTHONHASHSEED=0 PYTHONPATH=. python3 cr95_realm.py 0 3    # seed 0, three seasons
seed 0: social records built 630
with a hostile reception/regard member > 0: {'speak': 1}
of those, where removing both members moves the shipped obstacle: {'speak': 1}
actor Spirit held (value: count): {1: 100, 2: 80, 3: 118, 4: 75, 5: 117, 6: 140}
```

### The phases

| phase | finding |
|---|---|
| **0** draw present? | Yes. The roll is `roll_net_continuous(pool) + net_boost(leverage, pool)` against `roll.py::obstacle` (`roll.py:164-173`): the one engine. The design adds no draw and routes nothing outside `dice_engine` + `sigma_leverage`; it changes two members of the obstacle the module already composes. No bare-pool-against-flat-Ob leftover is introduced. |
| **1** stress points | (a) the ceiling region, where the discount is clipped to nothing: 24,225 of the 47,600 grid cells with hostility at `S = 7, k = 1`; (b) sub-1D pools (0.25, 0.5), where the fixed ceiling applies, held with the rest; (c) Spirit at the floor (no discount) and at the ceiling with `k = 1` (the members ignored). **1b:** rarely reached in computed play: 0 of 217 (seed 0) and 0 of 227 (seed 2) dealt records carry hostility in one season; 1 of 630 over three seasons (seed 0). The shipped `pool_floor` is 5, so sub-1D pools are unreachable at the shipped arms. |
| **2** what it decides | How hard other persons' hostility makes the actor's own social act: whether a hostile hearer or bench sways the outcome. Reversible in the main (a lost argument or telling re-forms next season), but it feeds `determine`'s verdicts and `interrogate`'s confessions, which open Tenures. A wrong answer makes a resolute person as cowed by a hostile room as a weak one, or makes resolve erase a room it should only blunt. Carried to `ners` unscored. |
| **3a** advantage enters via `levels_to_net_sigma` → `net_boost` | The discount is not advantage and enters no σ path; leverage is unchanged. None of §2's three bypasses is introduced (no flat bonus on the net, no `capped=False`, no inline `soft_cap·sigma_n`). |
| **3b** nothing resolves on `eff_ob` | Holds: the module's `ob` is the resolution value; `eff_ob` is not read. |
| **3c** the paths agree; `base_Ob` and `OB_MIN` hold | **No composed obstacle below `base_Ob` at any Spirit and modifier: 0 of 2,772,000 cells; 0 below `OB_MIN`; 0 raised by the discount; 0 non-monotone in Spirit or in hostility; the control (`k = 0`, and unheld Spirit) equal in `(ob, terms)` in every cell.** See F3 for the raw sum. Fractional Spirit (1.5, 2.5, 5.5) is monotone with the integers. |
| **3d** role conflation | None: the ACTOR's Spirit discounts; the OPPONENT's Spirit is in `opposition`; the two never share a variable. |
| **3e** a named level reaches the player | Not applicable to leverage (untouched). On the obstacle side see F4. |
| **3f** an irreversible outcome gets four bands | Unchanged: the margin is graded by `degree_from_net` as before. |
| **4** loops | Hostility (`reception`, `regard`) is read from stance and ledger, which the act's outcome can move next season; Spirit is an attribute nothing in the season writes. The discount scales the loop's gain by `f ≤ 1` (a damper) and adds no accumulator; the cap is the existing ceiling. Not a defect. |
| **5** intent | Deliberate: AR-44 ("ignoring obstacle modifiers"; "good results despite poor circumstances") with safeguards: the discount acts only on adverse members, `f ≥ 0`, and `bound`/`max(OB_MIN, ·)` are applied after it. Pass. |

### Findings, worst first (for `ners`)

| # | property | finding | reproduced by | lands on |
|---|---|---|---|---|
| F1 | P-iii (completeness at one end) | **Inert under the shipped hard ceiling wherever the record's own `base_Ob` reaches the cap.** At `S = 7, k = 1` the discount moves nothing in 24,225 of 47,600 hostile grid cells (the `CLIPPED` line: undiscounted 5.577 = discounted = `base_Ob`). This is the hostile member's own property: under `hard`, a hostile room already moves nothing past the cap, and the discount inherits it. `[INTENT UNDETERMINED]`: H-213's `soft` arm keeps both live; its flip is held (H-430). | the grid's `inert` count; the `CLIPPED` line | R-COMPLETE |
| F2 | P-ii (uniform leverage), inherited | **The discount's z-impact falls as `1/√pool`**, as every flat obstacle member's does: removing 1.0 of hostility is Δz 1.25 at pool 1 and 0.42 at pool 9. Spirit introduces no new scaling; it shrinks a member whose scaling is the existing obstacle's (members are raw × step, not σ_N-scaled, `roll.py:124`). Not Spirit's defect; recorded so `ners` does not score it as Spirit's. | the `P-ii` lines (`1/(SIGMA_PER_DIE·√N)`) | S (methodology), against the obstacle form, not CR-95 |
| F3 | P-iii, not a defect of this design | **The composed obstacle sits below the RAW sum `even + difficulty + opposition` in 28,868 cells at `k = 0` and 30,978 at `k = 1`.** Every such cell's `base_Ob` is already below the raw sum (0 exceptions), none is on the uncapped arm (0), and the 2,110 extra cells at `k = 1` are all soft-ceiling cells. The ceiling (H-213), not Spirit, puts the obstacle under the raw sum. Measured against `base_Ob` as §2.2 defines it, nothing falls below. | the raw-sum line and its decomposition | R-COMPLETE, against H-213 |
| F4 | P-i (legible odds) | **The discount is a scaled member, not a named level.** The terms record `reception` and `regard` at their discounted values, so a reader of the terms sees a smaller hostile member and not why. Legible only if the record's Spirit and `k` reach the surface beside the terms (the build carries both in the record). | by construction | E-LEGIBILITY |
| F5 | reach, not a property | **Rarely reached today.** 0 of 444 dealt records over two seeds' first seasons carry hostility; 1 of 630 over three seasons at seed 0. After SC-02's re-source `reception` is expected to read 0 at seed 0 (SC-02 §3c), leaving `regard`. The design is complete and runs on the records it reaches; its weight in play depends on hostility forming. | the Phase 1b output | R (narrative reach) |

**Named attacks that failed:** P-ii as a NEW bypass (none: no σ path touched); P-iii at the floor (0 below `OB_MIN`); P-iii monotonicity (0 non-monotone cells in Spirit or in hostility); P-iv (the four bands unchanged); P-v (no bespoke draw, no second ladder, no fractional pool sent to `roll_pool`); the control (0 differences in `(ob, terms)`).

**The headline, for the gate:** the diagnostic's report shows **no composed obstacle below `base_Ob`** at any Spirit and modifier (0 of 2,772,000 cells), where `base_Ob` is the module's composition of the same record without the two discounted members. Against the raw unbounded sum, the H-213 ceiling already puts the obstacle below it at every Spirit, `k = 0` included (F3).

---

## 7. Takes, each reverting alone

All `[ASSUMPTION; Jordan to correct]`, answered by the `CLAUDE.md` §0 ladder (precedent or architecture); none is escalated:

1. Spirit discounts `{regard, reception}` and nothing else (§2.1). Revert: add `capability`.
2. `f` is linear from the floor and never amplifies (§2.2). Revert: centred at the mid-point.
3. Unheld Spirit discounts nothing (§2.2). Revert: read at the mid-point.
4. No combat discount; Spirit stays strain there (§2.3). Revert: Spirit scales the bearer's own `wound_impairment` share.
5. The social `wounds` source is not discounted (§2.3). Revert: fewer wound levels against the actor.
6. The form lives in the module, with the discounted set a roster carried in the record (§2.2). Revert: the host scales the two raw operands.
7. `arrest` keeps Strength, pending BA1.13's Q1 (§1). Revert: Spirit, with adj §2.2 (iv).
8. The shipped `k` follows adj §2.3's sweep rule over `0 / 0.5 / 1.0` (§5).
