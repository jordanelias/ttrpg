# MB · the commander as a chooser: what he decides, what he is shown, and what each order costs him

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §1.2 (`officer_pool` showing the true pool VIOLATES `04` D-42) with 7b-16 [DECISION] (the host builds each officer's pool as the commander believes it, from his own claims, `None` when he holds none, shown "unknown"; the "true value until the belief model supplies one" paragraph and INCOMPLETE item 2 removed), §1.2 watch row (`obey_odds` is one draw's band odds from the dice owner, not a field closed form; the manager proposal's §8 refusal is of a field's: stated once), `U1_GLOSSARY.md` *band* (`reach_bands` → `reach_steps`, distance steps), D-U1-11f (`standing_order_cap`); test 9 (INCOMPLETE item 3 closed by order: the manager's §4 lands earlier in B20; `Depends on:` / `Lands in batch:`).

**Depends on:** `27_MB_A_command_and_the_obedience_draw.md` 27A-3, 27A-4 (B19); `04_MB_manager_battle_one_resolver.md` §2, §4, §5 (B20, earlier in the batch); `10_DICE_believed_odds_have_a_prior.md` (B05) and the believed-estimate route of `U5b_MB_residue.md` §5 for the believed officer pool; `26_MASS_BATTLE_cell_scale_and_time.md` §3 (B19); CHAR's cells for 27D-4.
**Lands in batch:** B20 (`B20-mb-orders`, MB), after `04_MB_playable_field_scenario.md` A, C, D; 27D-4 returned to CHAR.

## Status: PROPOSED

Lane MB for the read surface and the costs; **CHAR owns the scoring** (the cells, the temperament and the
reason trail's wording) and this file states the interface it needs and no ranking rule. Serves ruling
**A-59** (`unified/DECISIONS_ANSWERED.md:73`): placement and instructions relative to the opponent are what
decide, so somebody has to choose them, and the same somebody whether played or not (`AUDIT_BRIEF.md`, the
NPC and AI-chooser charge). Builds on `04_MB_manager_battle_one_resolver.md` §2, §4, §5 (standing orders, the
window, the interventions list), `26_MASS_BATTLE_maneuver_orders.md` §2, §3 (lull actions, doctrine rows),
`27_MB_A_command_and_the_obedience_draw.md` (the draw) and `audits/04_MB_audit.md` §16. Audit:
`audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md`. Reference, not mechanism (`CLAUDE.md` §0.05). No code is
edited by this file.

## What it changes in `engine/season/` at runtime

Nothing by itself: it adds three fields to a view, one pure odds function, one column to the army Record and
a tuple of reasons to an action. With a decider supplied (a player's, or the chooser's for an unplayed
commander) it changes what that commander does at a window. No natural season fights an army field today.

## The problem

- During a field nobody decides anything, and the defender has no turn (`audits/04_MB_audit.md` §16 (a), last
  two rows). The unplayed commander's army is a preset doctrine and a role table
  (`modules/mass_battle/troop_types/presets.py:37-50`), "one policy standing where a person's choice should be"
  (same audit §16 (c)).
- The estimate is the player's alone (`engine/season/seam/wrappers/mass_battle.py:463-466`), so player and NPC
  are not the same kind of agent at the moment of decision (§16 (b)).
- Once orders are drawn (`27_MB_A`), an order has odds. A chooser that cannot see them cannot weigh "signal
  the wings now" against "ride to the left and steady it", and a player who cannot see them is guessing.
- Nothing an order costs is stated anywhere, so every order is free and the best plan is the longest.

## The resolution, decided

### 1. What a commander decides, and when (every set closed, every set data)

| when | decision | closed set (owner) | act |
|---|---|---|---|
| in the season, before any field | composition | troop rows; the Record's ops (`armyrecord.OPS`) | `recruit`, `form_unit`, `assign_troops`, `disband_unit` (`14_VERBS_MILITARY_C`, `_D`) |
| | the formation | `troops.yaml: formations` | `order_unit`, army-level payload |
| | each unit's post, ranks, files, second weapon, role, stance | the unit row's columns | `order_unit` |
| | each unit's standing orders (at most `standing_order_cap`, D-U1-11f) and the signals they wait on | `battle_orders.json: triggers`, `behaviours` | `order_unit` |
| | **who commands each unit** | persons of his faction; the row's `officer` | `order_unit` |
| | **where he rides** | the unit names of his own Record; `commander_post` | `order_unit` |
| | a doctrine, which writes most of the above at once | `troops.yaml: doctrines` | the doctrine choice (`04_MB_playable_field_scenario.md` step 5a) |
| to march, and to meet it | fight, decline, storm, invest, yield | the march's payload and postures | `march`, `surrender`, `besiege` (same file, A to D) |
| at each window of a bout | **one** action | `GeneralAction.kind`: `signal`, `order`, `rally`, `withdraw`, `none` | inside the one call (`decide`) |
| in a lull between bouts | **one** action | `relieve`, `reform`, `commit`, `withdraw`, `none` | inside the one call |
| when the field ends | nothing new: recall and pursuit follow his standing orders; rally is his draw | | |

Two rows are new with A-59 (bold): the officer on a unit and the commander's own post now change odds, so
they are choices.

### 2. What he is shown (person-side; no `World`)

`FieldWindowView` (`04_MB_manager_battle_one_resolver.md` §4) gains, per own unit, three fields the module
already computes for the draw:

```python
units: tuple   # ((name, share, routed, in_contact, in_hand, orders_pending,
               #   reach_steps, steady, officer_pool), ...)
               # reach_steps: whole distance steps from his post to the unit (27_MB_A §4; "band" is kept for a degree)
               # steady: 'disciplined' | 'ordinary' | 'unsteady'
               # officer_pool: the dice of the unit's officer AS THE COMMANDER BELIEVES THEM, or None ("unknown")
```

and one pure function, beside `obey`, that a player's surface and an NPC's decider both call:

```python
obey_odds(view, action, me: CommandRecord) -> (p_at_once, p_late, p_not)
```

- It is `engine/dice_engine/sigma_leverage.py::band_odds` on the same pool, levels and obstacle `obey` would
  compose, for each link, composed. It is the closed form of the same sampler for **one draw** (U1 §4, last
  row), not a second rule, and it draws nothing. It is not the field closed form that
  `04_MB_manager_battle_one_resolver.md` §8 refuses: that refusal is of an odds function for a whole field
  (the auto-resolve formula Layer 1 names); a single order's band odds from the dice owner is the same shape
  the social roll already shows.
- A commander's own pool is known to him (`seam/wrappers/pool.py:78-82`). *(Reconciled, W3-1, 7b-16; `04`
  D-42, ladder step 3.)* His officers' pools are shown **only as he believes them**: the host builds each from
  the commander's own claims about that officer (`person_q` over his ledger, the same believed route as
  `U5b_MB_residue.md` §5) and hands it in on the input beside the officer's `CommandRecord`; `None` when he
  holds no claim, shown as "unknown". The module copies the handed value into the view and never reads the
  officer's true record for it.
- He is shown nothing of the enemy but what is in contact with his own units, as that proposal's §4 already
  rules; the enemy's orders, posts and officers are never in the view.
- Before the field, the estimate is the resolver sampled on what he believes of the enemy
  (`04_MB_playable_field_scenario.md` step 5b), for a player and for an NPC alike. After `27_MB_C` it is no
  longer blind to the thing that decides.

### 3. What an order costs him

Nothing below is a new meter. Each cost is a consequence of a rule in the proposals cited.

| cost | how it is paid | from |
|---|---|---|
| **the window** | one action a window, one a lull. An action spent on one unit is not spent on another | manager proposal §4; command as a scarce thing, WG D2, L3 |
| **a missed order is still spent** | on `late` it takes effect when the moment may have passed; on `not carried out` the window is gone and the order waits for its trigger | `27_MB_A` §4 |
| **improvising costs more than preparing** | an improvised order to an officered unit is two draws and carries the distance term; a standing order is one draw with none; a signal carries the field but is one draw for each unit and harder past three | `27_MB_A` §3, §4 |
| **a plan's size** | each further signal on a unit is something it can misread; each further unit on a signal is a step harder; each standing order past the first waits behind it | `27_MB_A` §4; manager proposal §2 |
| **his post** | forward: fewer distance steps, and `rally` reaches a unit he is beside. But his unit can be struck, and then every unit draws to stand; and his unit in contact with an enemy officer's is a duel he fights | `26_…_rout_pursuit_and_giving_ground.md` §1; `U5b_MB_rulings_in_the_field.md` §3 (A-4) |
| **his officers** | a good officer on one unit is not on another; the span check limits how many units he may leave without one | `armies.py:176-193` |
| **restraint** | an order to hold a victorious unit is a step harder than an order to act, and its failure is a unit gone from the field | `26_MASS_BATTLE_maneuver_orders.md` §1, restrain row; MV P5 |
| **what the season remembers** | each draw that changed the end state is an Observation on the band Event; whoever witnessed the field holds a claim that his order was not carried out, or that his wing went early | `27_MB_C` §3; `04_MB_manager_battle_one_resolver.md` §6 |

### 4. One interface for the player and the chooser

- The decider is the `decide` parameter of `resolve_field` (manager proposal §4), which A-4's record classes
  as a declared adapter input. A player's surface and the chooser fill the same parameter with a function
  from `FieldWindowView` to `GeneralAction` over the same closed set. With none, standing orders decide.
- `GeneralAction` gains `reasons: tuple = ()`, opaque to the module, returned in `FieldOutcome.interventions`
  and so on the report. The chooser fills it with the terms that ranked the action (CHAR's reason trail);
  a player's surface leaves it empty.
- The decider draws nothing from the module's RNG (manager proposal §5). A tie among the chooser's options
  is broken host-side by the chooser's own keyed draw, as everywhere else it ranks.
- **No rule for an unplayed commander lives in the module.** The default decider is absence. A doctrine row
  writes standing orders, a formation, posts and a default `commander_post`; it writes no window policy. A
  commander's behaviour at a window, when CHAR supplies it, comes from his sheet through the chooser.

### 5. What makes two commanders differ (the values CHAR's cells must be able to see)

A bold man and a cautious one, a schemer and a plain soldier, differ on exactly these, all of which are
payload values on acts or fields of an action: `commander_post` (a forward post or the reserve); the number
of signals in his plan; `pursue: true` or `false` on `enemy_broken`; each unit's fall-back fraction; whether
his best officer goes to the unit with the hardest orders or to the one he trusts least; at a window,
`rally` in person against `signal`; when he takes `withdraw`. The chooser keys on `(verb, subject)` today and
scores these alike (`audits/04_MB_audit.md` §16 (d)); cells on the value are CHAR's dependency and are named
there, not built here.

## Exact edits

| file (owner) | edit |
|---|---|
| `modules/mass_battle/massbattle.py` (MB) | `FieldWindowView.units` gains the three fields; `GeneralAction.reasons` |
| `modules/mass_battle/core/contact.py` (MB) | `obey_odds`, sharing `obey`'s composition of pool, levels and obstacle through one helper |
| `modules/mass_battle/armyrecord.py` (MB) | `order` accepts `commander_post` and `officer`, validated; `options()` reports units with no officer and a post that names no unit |
| `references/troops.yaml: doctrines` (MB) | each doctrine row gains a default `commander_post` (a post name, resolved to the unit holding it) |
| `engine/season/harness/military_menu.py` (IN) | offers the officer and the post from their closed sets, and shows `obey_odds` beside each window action |
| `engine/season/seam/wrappers/mass_battle.py` (IN) | forwards `host.decide` for either side's commander, played or chooser-served, by the one parameter |

## Gate (execution artifacts)

1. `obey_odds` agrees with `obey`: for 20 hand-built situations, the three shares it returns lie within the
   sampling band of 2,000 draws of `obey` on the same inputs; the two share one helper
   (`git grep -c "def _obey_terms" modules/mass_battle` is 1).
2. A decider that maximises `p_at_once` and one that returns `none`, same seeds, n 200: the first has more
   orders obeyed at once; both have the same count of draws per order issued.
3. The same commander posted forward against in reserve, n 400: forward, improvised orders are obeyed at once
   more often; forward, the share of fields in which his unit was struck is higher. Both differences beyond
   two standard errors.
4. A plan with three signals against the same plan with one: misreadings occur in the first and never in the
   second; the first's share of fields in which every wing closed is lower.
5. The view handed to a decider contains no enemy unit that is not in contact with one of his
   (asserted on the view's fields over 200 fields).
6. With no decider and no standing orders, the field equals the field without this proposal, at 200 seeds.

## Falsifier

A decider that changes the draw sequence for an identical action. An odds function that needs a second
obstacle rule. A window policy inside `modules/mass_battle/`. A forward post that costs nothing in 400
fields. An NPC commander whose window action is the same in every field whatever his sheet says, once CHAR's
cells land.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** From the player: an order with odds he cannot see is not a decision. From the world: an unplayed
  commander who never acts in a field makes every unwatched battle the same battle. From the architecture:
  one parameter, one closed set, the chooser's own interface. From history: where the commander stood and
  what he kept in hand was his art (MV E6).
- **R.** Where to ride, whom to trust with a wing, how elaborate a plan to risk; distinguishable commanders;
  with no player, a field's story is its commander's choices and what became of them.
- **S.** Player and NPC through one function; the odds shown are the odds drawn; the window pauses the bout
  and nothing else.
- **E, against that.** Three view fields, one function, one Record column, one tuple.

## Cost class

Small build, after `27_MB_A` and the manager proposal's §4. The scoring is CHAR's and is not costed here.

## Instructions to code it (standing charge, `AUDIT_BRIEF.md:545-547`; for workplan v12)

Checked against the charge on 2026-11-12. **The module half (27D-1 to 27D-3) is specified to the symbol and
is INCOMPLETE only on `27_MB_A` and the manager proposal landing. The chooser half (27D-4) is a design only
and is marked INCOMPLETE and returned to CHAR.**

**Batch items, in edit order.**

| item | file :: symbol (single owner) | edit | hash |
|---|---|---|---|
| 27D-1 | `modules/mass_battle/core/contact.py` :: new `obey_odds(view, action, me)` | calls `_obey_terms` (27A-4's helper, the one composition of pool, levels and obstacle) for each link and `engine.dice_engine.sigma_leverage.band_odds(pool, ob, boost)` on the result; composes two links by multiplying the at-once shares and summing the rest; draws nothing | none |
| 27D-2 | `modules/mass_battle/massbattle.py` :: `FieldWindowView.units`, `GeneralAction` (both created by `04_MB_manager_battle_one_resolver.md` §4) | the three view fields, computed where the view is built: `reach_steps` by the same function `obey` uses, `steady` from the unit's Discipline and `raw`, `officer_pool` copied from the believed value the host handed in (7b-16; never from `Subunit.officer_record`'s true score); `GeneralAction.reasons: tuple = ()`, copied untouched into `FieldOutcome.interventions`. Host side: `seam/wrappers/mass_battle.py::field_input` builds the believed pools from the commander's claims | none with no decider |
| 27D-3 | `modules/mass_battle/armyrecord.py` :: `order`, `options`; `references/troops.yaml: doctrines.<name>.commander_post`; `engine/season/harness/military_menu.py` | `order` accepts `commander_post` and `officer` (27A-3 adds the keys; this adds the menu's closed sets: unit names; persons of the faction, handed in as facts); `options()` gains `unofficered` and `post_names_no_unit`; the menu lists both and prints `obey_odds` beside each window action | none (withheld verbs) |
| 27D-4 | `engine/season/seam/wrappers/mass_battle.py::resolve` (`:355`); `engine/season/decision/` | forward `host.decide` for either side's commander by the one parameter; the chooser's decider over `GeneralAction`'s closed set | INCOMPLETE |

**Data rows.** `doctrines.<name>.commander_post`: a post name of the formation (`front`, `rear`, `left`,
`right`, `reserve`), resolved to the unit holding that post; seed `reserve` for every doctrine, which is the
control (the rear centre, today's implied position).

**Call sites.** The window hook is the `phase_boundary` call at `modules/mass_battle/battle_loop.py:461`
(where the manager proposal puts `on_window`); the view is built there. `resolve` already forwards a
decider for combat (`seam/wrappers/combat.py`, REM-31); the field's forward is its sibling.

**Tests** (named).

- `tests/valoria/test_conditional_orders.py`: `test_obey_odds_agrees_with_two_thousand_draws_of_obey`
  (gate 1); `test_obey_odds_and_obey_share_one_terms_helper`.
- `tests/valoria/test_mass_battle_officers.py`: `test_a_forward_post_buys_obedience_and_costs_exposure`
  (gate 3, both differences beyond two standard errors, n 400);
  `test_three_signals_can_be_misread_and_one_cannot` (gate 4).
- `tests/valoria/test_army_battle.py`: `test_the_window_view_shows_no_enemy_unit_out_of_contact` (gate 5);
  `test_no_decider_and_no_orders_is_todays_field` (gate 6, the control).
- `tests/valoria/test_army_menu_presets.py`: `test_the_menu_offers_officer_and_post_from_their_closed_sets`.

**Gate, with the reading expected.** As "Gate" above. Control: gate 6, hash-equal with no decider and no
standing orders.

**Falsifier and its control.** As "Falsifier" above. Planted: `obey_odds` given its own obstacle arithmetic
(the helper-count test and gate 1 fail); the view built from `World` (gate 5 fails on an enemy unit out of
contact).

**Hash movers.** None with no decider. With one: fields in which the decider acts.

**Dependencies.** `27_MB_A` items 27A-3 and 27A-4; `04_MB_manager_battle_one_resolver.md` §2, §4, §5;
`26_MASS_BATTLE_cell_scale_and_time.md` §3 for lull actions; `04_MB_cell_hierarchy_as_data.md` §3 for posts;
`04_MB_playable_field_scenario.md` step 5a for doctrines as rows.

**What lands it; cost class; tier.** An IN-lane session under `/methodology-execute`, in
`U5b_MB_rulings_in_the_field.md` §6 row 5. 27D-1 to 27D-3: small build, `sonnet`. 27D-4: design-first,
`opus` (competing considerations in a chooser), CHAR's.

**INCOMPLETE, with what is missing.**

1. *27D-4, the unplayed commander's decider, is a design only.* This file gives the interface (the closed
   action set, the view, `obey_odds`, the costs) and no ranking. Missing, all CHAR's: the cells on payload
   values (`audits/04_MB_audit.md` §16 (d): the chooser keys on `(verb, subject)`); the question a commander
   answers at a window; how temperament and conviction weigh `rally` against `signal`; the wording of
   `reasons`. Returned to CHAR. Until it lands an unplayed commander has no decider and his standing orders
   decide, which is a complete behaviour and not a stub.
2. *(Closed, W3-1, 7b-16.)* The view shows a believed pool or "unknown", never the true value.
3. *(Closed by order, W3-1.)* `FieldWindowView` and `GeneralAction` land earlier in B20 with the manager
   proposal's §4.

**Added test (W3-1):** `tests/valoria/test_army_battle.py::test_officer_pool_is_believed_or_unknown` (a commander
holding no claim about an officer sees `None`; one holding a false claim sees the false value).
