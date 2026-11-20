# CHAR — a choice the chooser can judge: alignment cells on `choice_sourced` values

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.2 row (CONFORMS; "Per phase" overtaken), §2 row A-9/A-72, §7, §7b-17, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` ledger P-03, S-08; `unified/U3_DEPENDENCY_ORDER.md` node B10). Changed: the "Per phase" paragraph follows A-9 (a scene is a short sequence; the chooser orders its steps and a step may hang on the band of the one before) and A-72 (a battle may call one duel round; a duel round calls nothing), keeping ED-IN-0304's appetite as the open carrier for an in-module NPC policy; the `approach` key is the PC lane's (`modules/combat/vocabulary.py: APPROACHES`), and LACUNA's `calm`/`press` is the separate key `questioning` (U1 ledger P-03, S-08); the `marshal` mark is settled at the tree (`marshal` ships in `withheld_verbs`, `data/fixtures.py:1157`, CP-T04-02, H-361); named tests; lands-it and tier.

**Lands in batch:** B10. **Depends on:** B09; `16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` (B08, A-9's scene order, which the per-round choice reads).

## Status: PROPOSED

Written by the CHAR audit lane (`audits/02_CHAR_audit.md`, §0A, §10, §14). Ratifies nothing. Reference
under `CLAUDE.md` §0.05. It serves three stated intents with one mechanism: a commander's orders (mass
battle), an attack approach (personal combat), and any later closed-set option on an act.

## What this changes in `engine/season/` at runtime

`decision/choose.py::score_terms`' pursuit term adds, for a candidate that carries a `choice_sourced`
key, the alignment of the VALUE it carries, read from a new block of the existing alignment table.
With no cell authored (the shipped state) the addition is 0.0 for every candidate and the hash is
EQUAL. A declared mover once a cell is authored.

## The problem, with evidence

One interface already lets a chooser, player or NPC, set an option on an act: `rosters.yaml:
choice_sourced` (`marshal: [role, retreat_at]`; `march`'s `posture`), fanned by
`decision/options.py::_fanned_choices` into one candidate per value. The player picks among them on
`decision/sheet.py::DevelopmentSheet`; the NPC's ranker orders the same list. The roster's own note
states the limit (`rosters.yaml`, `choice_sourced`): *"THE CHOOSER IS CONTENT-BLIND: Candidates score on
`(verb, subject)`, so the fan is a draw among equally scored orders, not a judgement of which role
suits the field."* H-361 (register line 6541) measured the fan's cost (45 bags per settlement) and that
a standing order's role can move the field against its orderer.

So an NPC commander's order, and an NPC duellist's approach if one is added by the same route, is
chosen by the draw. Two commanders of opposite temperament order alike. That fails the mass-battle
intent (a manager whose settings decide the match), the personal-combat intent (an approach chosen per
phase), and R-06.

## The resolution, decided

A choice value is scored the way a verb is scored: by alignment cells on the seven pursuit axes.
Ladder step 4: `tables.alignment` (verb × axis, sparse, default 0.0, refused if unrostered) is the
precedent and the owner; a value of a closed set is one more row of it.

```yaml
# engine/season/rosters.yaml, inside tables.alignment
choices:                       # optional block; absent or empty is the shipped state
  retreat_at:                  # a `choice_sourced` key
    never:   {rigid_flexible: -0.4, grandiose_humble: -0.3}     # illustrative; the cells are Jordan's
    early:   {rigid_flexible: +0.3, selfish_selfless: -0.2}
  approach:                    # the PC lane's key (`modules/combat/vocabulary.py: APPROACHES`); LACUNA's calm/press is `questioning`
    aggressive: {grandiose_humble: -0.4}
    defensive:  {grandiose_humble: +0.3}
```

- `data/verbs.py::align_choice(key, value, axis)` beside `align` and `align_kind`, reading the one
  binding the `H-66` sweep rebinds.
- `score_terms`: `pursuit += damp · Σ_axis axis_w[axis] · Σ_(key,value in c.operands, key choice-sourced)
  align_choice(key, value, axis)`, inside the same `odds_weight` factor.
- The loader refuses a key that is not `choice_sourced`, a value outside that key's `CHOICE_RANGES`,
  and an axis off the roster. No value is required to carry a cell.

**What it deliberately is not.** It is not a judgement of which order suits the field: that is the
believed chance of the act, which `odds_weight` already multiplies in and which reads the candidate's
payload. Today the believed-odds query answers `None` for another module's prize, so a field or a duel
is not priced by its order. Serving a module's own estimate through `View.odds` (the combat seam has
`fight_estimate`, marked for the player's display only) is the MB and PC lanes' edge and is named in
the audit's §10. With both in place an NPC chooses an order by temperament times believed chance,
which is the same sentence as for any other act.

**Per round (A-9, A-72).** A scene is a short sequence (A-9): the chooser orders its steps and a step may
hang on the band of the one before. So a duel's approach is chosen per **duel round** as a step the chooser
forms in the scene, each step's value scored by these cells, and the next step may read the band the last
round came out at; a field's standing order is set the same way at the step that marches. Inside one duel
round the module resolves at RESOLVE (a registered module holds no token and takes a typed input), and a
duel round called from a battle calls nothing further (A-72). `[ASSUMPTION: the duel round stays inside the
module at RESOLVE; only the choice between rounds is the chooser's — basis: A-72 and R2 §1.2]`. A played
person's choice within the round stays the suspension at ENCOUNTER's barrier (REM-31, ratified), whose
`decide(view)` callback is the per-turn choice; an NPC's choice within the round is a policy inside the
module parameterised by data on the typed input, which needs a person-side quantity the input does not carry
today (`Combatant.disp` has `registry_key: None`): its carrier is ED-IN-0304's risk appetite (open ask M40),
not resolved here.

## Edits, by owner

1. `engine/season/rosters.yaml` — the optional `choices:` block under `tables.alignment`.
2. `engine/season/data/verbs.py` — `_load_alignment` reads the block; `align_choice`; the refusals.
3. `engine/season/decision/choose.py::score_terms` — the added sum.
4. `engine/season/rosters.yaml: choice_sourced` note — the *"CONTENT-BLIND"* sentence amended to say
   where content enters.

## Gate, falsifier

- No cell authored: `build_realm(0)` one-season hash EQUAL.
- Two hand-built persons with opposite weights on one axis, one `marshal` question: with one cell
  authored on that axis they rank two `retreat_at` values in opposite orders at temperature 0; with
  the cell removed they rank them alike. `aperture 1 0` with `marshal` released from `withheld_verbs`
  (it ships withheld, `data/fixtures.py:1157`; whether the realm forms it once released is read by that run,
  and is a declared mover of its own).
- Named tests (new, `engine/season/tests/test_choice_alignment.py`):
  `test_opposite_temperaments_rank_two_retreat_at_values_in_opposite_order`,
  `test_no_cell_authored_is_hash_equal`, `test_a_cell_on_a_non_choice_sourced_key_is_refused`.
- Falsifier for the whole idea: if, with cells authored, the distribution of chosen values over seeds
  0–4 does not differ between two persons of opposite temperament, the term is swamped by the fan and
  the fan must be scored before it is formed.

## NERS reading (§0.06)

- **N.** From the commander's direction: without it the manager's instruction is a coin. From the
  character's: the one place a person's manner would show in a fight or a battle is decided by nothing
  about him.
- **R.** Strategy (a player learns an opponent's habits), customization (temperament shows in orders),
  the no-player half (NPC commanders differ unwatched).
- **S.** The same dot, the same table, the same sweep and null control as verbs. It zooms: one rule
  for an order on a field and an approach in a duel.
- **E (last, as a ratio).** One optional block and one sum, against a second personality system.

## Cost class

Small build. Content (the cells) is Jordan's, on the cell-value and cosine pass that already owns
`tables.alignment`.

**Lands it and tier.** The B10 batch, an IN `valoria-author` session on `sonnet` (`high`), closed by B10's
`methodology-close` once. **Hash movers.** None with no cell (control); each authored cell a declared mover.
**INCOMPLETE, content:** the cells are Jordan's.
