# What a move costs the person who makes it: the NPC decider's terms inside a hearing

## Status: PROPOSED — the design pass HEAR_B edit 8 left open (`05_SC_playable_hearing_B.md` "Not decidable here"); master workplan v12 item B24.12. Design only: no code lands with this file. B24.13 ships the hearing's decider with every term below ABSENT (E-14) and lists them under `DIALS AT CONTROL`; the build of this file is not scheduled in v12.

Source: `05_SC_playable_hearing_B.md` "Who decides" (*"less the move's cost in his own terms (an item
exposed, an enemy made, a concession witnessed, effort)"*) and "Exact edits" 8; `IS-B2-SC-04` (the cost
terms stay this file's pass); `IS-B2-CHAR-02` "What stays open" and its bar, *no term is added that the
chooser does not have*; `IS-B2-SC-03` (the default rite's `bears:` is read once by this pass); D-18.
Code read (the mechanism; this file is reference, CLAUDE.md §0.05): `engine/season/decision/decider.py`,
`engine/season/decision/choose.py`.

## 0. The constraint this design is built under

`make_decider` (`decision/decider.py`, B10.57) scores a legal value `v` of a view by exactly two terms,
`TERM_NAMES = ("pursuit", "bias")`:

- `pursuit = damp × Σ_axis axis_w[axis] × align_choice(key, v, axis)`, times
  `weigh_by_chance(fx, odds(view, v))` — the chooser's own pursuit term over a choice value, priced by the
  believed chance of the module's pure estimate (for a hearing, `closing_odds`/`p_carried`);
- `bias` — an optional `(view, value) -> float` the caller hands, added after pricing.

Its docstring states the bar this pass is held to: *"it adds no term the chooser does not have: no stance,
no fit, no aim, no risk, no refusal memory."* A cost term is therefore admissible only if (a) the
quantity is one the chooser (`choose.score_terms`) ALREADY scores for a verb candidate, (b) it enters
through the slot that quantity already occupies in the chooser, on the chooser's ladder, and (c) its
operand is read off the person (`View.own`, his interior) and the hearing's own view — never `World`, never
another person's ledger. Anything that fails (a) is a new term and fails `IS-B2-CHAR-02`.

**What the tree holds that this reads** (B24p and B24.05–B24.10, in the tree at the batch's branch head;
`Item.cell`, `View.board` and `View.hand` are there, `queries/inputs.py:178-182`, `:443-444`): the hearing is `modules/social_contest/proceeding.py` (V2). A chooser is shown
`queries/inputs.py::View`: `own` (his `Cond`: `rattles`, `strain`, `heat`, `spoken`, `spent`, all TRUE),
`esteem`, `weary`, `awe`, `options` (each an `Option(move, ground, item, relation, ev, p, frame)`, `ev`
his PERCEIVED worth in track units and `p` his perceived chance), and since B24.05 `board` and `hand` (the
`Item`s standing and his own unshown ones; an `Item` carries `about`, `source`, `origin`, `cell`, `side`).
The module's `menu` prices every option in track units BEFORE the decider sees it: a failed press costs
the presser `rebound`; a press that lands is worth the target's continuing loss (`_lasting`: his esteem
shortfall, his staying power, his pull); a concession costs `concede_step × (1 + max |stake|)`; a point
left standing or a burden unmet costs `silence_cost`; a raised point is discounted by the reply it
invites (`invite`); an exhibit is worth `_worth(weight)`. RD §B.5–§B.6's "mark" is V2's rattle
(`Cond.rattles`), and V2's `esteem(inp, st, v)` is computed from rattles, Grace and the venue's standard
against the man opposite: there is no separate stock of esteem.

## 1. The cost terms, as quantities his interior already scores

Six costs are named (HEAR_B's four; part 5's B24.12 row adds two). They fall into two classes by WHERE
the cost lands, and the class decides the owner.

**Class R — what the move does to a person he holds a regard for.** The cost lands outside the verdict,
on a relation. The chooser scores this quantity with one term, `stance` (`choose.stance_term`, arm
`declared`: `regard(p, x, fx)` times the sign of the act toward `x`, at weight `1 + stance_gain`). Each cost
in this class is that term, read toward the person the move acts upon:

| cost | the person the move acts upon (`x`) | sign toward `x` | interior read | owner |
|---|---|---|---|---|
| **an enemy made** | the man a `press` strikes; the source of an item an `answer` strikes (`answer` is in the `inquisition` rite's moves, not `default`'s, `arrangements.yaml:214`); the origin an `impugn` halves | −1 (an act against him: `options.subject_is_opponent`'s default, B10.11) | `regard(p, x, fx)` = `stance_toward` + judged + told + heritage | `person_q.regard`; `choose.stance_term` (the arm, the scale) and `_stance_arm` (the clamp) |
| **a concession to `x`** (HEAR_B's "concession witnessed": only the beneficiary is read; the witnessing, i.e. face, is scored nowhere, below) | the other side's lead, for whom the concession is made | +1 (an act for him: the `beneficiary` reading, B10.69) | `regard(p, x, fx)` | the same |
| **an item exposed** | the item's `about` (the man the shown deed names) | the sign of `deed_valence(axis_w, cell)`: a deed his own weights judge ill exposes `x` (−1), one they judge well credits him (+1), a cell that is no valenced deed acts on nobody (0) | `regard(p, x, fx)`, and `person_q.deed_valence` over his own projected weights | `person_q.regard`, `person_q.deed_valence` (the told channel's one scoring of a deed, `G1`/`G3`) |

The item-exposed row is the told channel's consequence: a shown item is a deed told to the room, and
what a told deed does is move its doer in the hearers' `told` half of regard by the deed's valence. He
cannot read the hearers' ledgers (F8; AX-2), so he judges the deed by his own weights — the one
scoring of a deed (`deed_valence`, which `deeds_judged`, `said_of` and `attention_key` already read) —
and weighs the consequence by his own regard for the man it lands on. Only the SIGN of the valence is
taken, so the term stays in stance units (`regard`'s), not stance × valence.
`[ASSUMPTION: the sign rule — basis: ladder step 5; the sign of a deed told is the deed's, as regard's told
half reads it; a row sign would score every exposure the same way whatever the deed. Revert: a fixed −1 on
`present`, which scores crediting a friend as betraying him.]` A damning item about HIMSELF reads
`−regard(p, p.id)`: the chooser's rule that self-regard is unsigned (`_stance_arm`, *a person is not his
own adversary*) governs a ROW's sign, and no row sign is read here.

**Reachability in computed play.** Two Class R readings have no input in computed play today. The host builds
items with `source` and `about` only (`sigma.py::_items_of`, `:1456`, `:1458`, `:1460`, `:1466`;
`person_q.py:3163`), so `Item.cell` is `()` and `Item.origin` is `None`. The module gates on both:
`_clash` needs `len(cell) >= 2` (`proceeding.py:238`) and `_answerable` needs `tg.origin` (`:262`). So "an item
exposed" reads 0 for every computed item until `_items_of` writes `cell` (§6). `impugn`'s `x`, the origin,
has no writer, so it stays `None` and reads 0. Until then, only a hand-built item reaches these two readings.

**One owner of relation in the room — RULED (ladder step 5).** The module has its own relation reading:
`person_q.tie(p, q)`, `clip(stance_toward / STANCE_MAX + debt + shared faction)` on `−1..1`
(`person_q.py:3069-3077`). The host carries it as `Present.bonds` (`sigma.py:1497-1498`); it is read as `_bond`
at `proceeding.py:728` and `:927` (how a hearer weighs the man a press strikes) and in the automatic policy's
`D["grudge"] * (-_bond(me, foe))` (`:1073`). Class R reads `regard`. Two readings of how p bears on q in
one room is an S defect, and it has to be decided. **The mover's own choice reads `regard`. `tie` stays the
module's reading of how a HEARER is moved** (resolution, not choice). The reason is that the decider is
`decision/`'s, and the one relation the chooser scores anywhere is `regard`. A term reading `tie` (or
`Present.bonds`, which `View` does not carry) would be a term the chooser does not have, and that fails
`IS-B2-CHAR-02`. It would also make one man's grudge weigh differently in the room than in the season.
The consequence, which B24.13 records when it lands: for an NPC that `make_decider` decides, the automatic
policy's `grudge` term is superseded by Class R. It survives only for an attendee that the automatic policy still
moves. Between the two readings, `tie`'s debt and faction addends and `regard`'s judged, told and heritage
addends still differ. That is recorded as a limit of the split by role, not fixed here.
⚠ `regard` is unbounded at the shipped `stance_clamp=False` (`fixtures.py:1345`), and `tie` is clipped. §3's
dominance warning is the worse for it.

**Class S — what the move does to his standing in the room.** The cost lands inside the sitting, on the
chances of his later speeches and so on the verdict. The decider already scores that quantity once,
through the believed chance (`weigh_by_chance(fx, odds)`, CR-17's ladder). The module prices a mark and
lost esteem into the option's worth from his TRUE own values, and effort only in part (row 3). So none
is an added decider term:

| cost | where the tree already prices it | read off |
|---|---|---|
| **a mark taken** | every later speech's leverage reads `esteem_step × esteem`, and `esteem` reads `Cond.rattles` (`_short`); a raised point's worth is discounted by the reply it invites (`invite`) | `View.own.rattles` (the module computes the menu on his true `Cond`) |
| **esteem lost** | the same quantity as a mark in V2 (no separate stock), plus a failed press's `rebound`, charged in that option's `ev` | `View.esteem`, `View.own` |
| **effort** | the turns he spends are priced ONCE, at the act's formation: `settle_efforts` prices an effort variant by the acts its slots displace (CP-T01-05). **Inside the sitting a drawing move's own spend is UNSCORED today.** The exchange adds `spent + (1.0 if draws else 0.0)` (`proceeding.py:1010`), and spent staying power reaches his later obstacles as `weary`. But `menu` charges the mover no own-spend (`:705-717`, `:730`; `_lasting` charges only the TARGET's spend, `:655`), and `make_decider` never reads `View.weary`. The cost differs by move (the `draw` column, `rosters.yaml:3841-3849`) | `View.own.spent`, `View.weary` (by the module, once the edit below lands) |

A decider term for a mark or lost esteem would score a second time what the believed chance already scores:
two ladders for one quantity (CLAUDE.md §0.06 S). **Effort's in-sitting cost belongs to the same owner, the
module's `menu`.** The edit is named in §6: a drawing option's `ev` is charged the mover's own spend, by the same
`weary_step × (1 if spent + 1 > stay else 0)` form `_lasting` already charges the target. That edit moves the
automatic policy too, which picks by `ev`, so it carries its own control. Until it lands, the in-sitting spend is
unscored. NERS accepts that for now: the cost bites only once he passes `stay`, a long sitting's edge rather than
its body. It does not license a decider term. The out-of-room half of a mark, of lost esteem and of
a witnessed concession — what the room thinks of him afterwards, carried on the Event's `ending` and
deposited by WITNESS — is no term either: the chooser holds no face term (face is never stored: RD part 5,
row 21), so adding one fails `IS-B2-CHAR-02`. B24.41 and B27 decide what regard makes of that deposit;
once regard reads it, Class R reads it on the next choice through `regard` with no edit here.

**None reads `World` or another's ledger.** Class R reads `regard(p, x, fx)` and `deed_valence` over `p`'s
own weights (`person_q`, person-side, AX-2) and three ids and one cell off the view; the decider is never
handed `x`'s `Person`. Class S is read by the module from the `Input` the host built (V2's rule: own
values true, everything else perceived).

**Falsifier (1).** For each Class R row, two hand-built deciders differ ONLY in `regard(p, x)` (a stance
row `+R` against none): the move acting on `x` is picked less often (enemy made, item exposed) or more
often (concession to a friend; less to a man held at `−R`) over 200 keyed draws. The AX-2 path scan over
`decision/` (`test_decision_package_never_names_world_anywhere_under_it`) stays green; a planted claim
in `x`'s ledger is not a falsifier, because the decider is never handed `x` (structural, not tested).
For Class S: author one positive `hearing_move` cell on `press` and raise `rebound` from 0. The `press` share
must fall through `odds` alone. Run it once with a `for` mover and once with an `against` mover; a sign
error in §2.4 shows on exactly one of the two. **Control:** `move_cost_gain` 0 (§3): every Class R reading is exactly `0.0` and
`regard` is not read.

## 2. How each enters `make_decider`'s choice score

```
score(v) = pursuit(v) × weigh_by_chance(fx, odds(view, v))     # B10.57, unchanged: the move's cells, the believed verdict
         + bias(view, v)                                       # B10.57, unchanged (IS-MB-03's caller only)
         + stance(v)                                           # NEW TO THE DECIDER, the chooser's own term:
stance(v) = move_cost_gain × (1 + stance_gain) × sign(v) × scaled_regard(p, x(v))
```

1. **Class R enters as the chooser's `stance`, unpriced.** In `score_terms` the stance term is added after
   the pursuit term and is not multiplied by the believed chance; so here: a betrayal costs whether or not
   the verdict is carried. `sign × scaled_regard` is the chooser's own arithmetic, factored out as
   `(p, subject, sign, fx, memo)`. The factored part KEEPS the `stance_polarity` arm dispatch
   (`choose.py:137-162`; `declared` is shipped, `fixtures.py:906`): `legacy` reads `stance_toward` unsigned,
   `regard` reads regard unsigned, and `declared` reads regard times `sign`. It also keeps the `regard` memo,
   the `stance_clamp` bound (`_stance_arm`), and the `stance_scale / STANCE_MAX` factor, applied once
   (it lives in `stance_term`, `choose.py:111`, not `_stance_arm`). `stance_term` passes the row's sign
   and the decider passes the move's, so one owner serves both. A term that bypassed the arm would be a
   second ladder. `hostile_stance_gain` does not apply: it is the weight for a VIOLENT prize, and a
   verdict is not one.
2. **`x(v)` and `sign(v)` come from cells, never a move id** (the chooser reads a row's cells, never a verb
   name; the module "compares no row, move or person id"). `rosters.yaml: proceeding_moves` gains two
   columns mirroring `verb_table.yaml`'s: `regard_sign` (a `regard_signs` member: `press`, `answer`,
   `impugn` −1; `concede` +1; `argue`, `rest`, `rule`, `adjourn` 0) and `acts_on` (`target` | `told` |
   `none`; `present` is `told`: its sign is the deed's, as §1). ⚠ `verb_table.yaml:53` reserves
   `regard_sign` values to content. The values here equal the default the loader derives (−1 against an
   opponent, +1 otherwise), so the build may derive them as `verb_table` does and author none. The module, which alone knows whom a move
   strikes, fills one field it already computes: `Option.target` (the press's `T`, the answered item's
   `source`, the impugned `origin`, the other side's lead for a concession, the item's `about` for an
   exhibit; `None` otherwise) — `Beat.target` is its precedent.
3. **`make_decider` gains `acts_on: Optional[Callable[[view, value], Optional[tuple]]]`** (default `None`:
   adds nothing), the caller's statement of `(x, sign)` per value, as `odds` and `bias` are the caller's.
   `TERM_NAMES` becomes `("pursuit", "bias", "stance")`: appended third, the `fit`/`aim`/`risk` precedent
   in `score_terms` (*every reader of it by index keeps it*); `watch` reports it, so the reason trail says
   "stance", not "bias". `bias` is not used to carry it, because that would hide the term's name from the
   trail. ⚠ **This reverses a sentence of the decider, and the reversal is named here.**
   `decider.py:5-6` says *"it adds no term the chooser does not have: no stance, no fit, no aim, no risk"*.
   `IS-B2-CHAR-02` (`IS_B2_SC_FI_CORE_CHAR_part2.md:135`, `:141`) bars only a term the chooser does NOT
   have, and leaves the hearing's cost terms to this pass. So `stance`, which the chooser has, is
   admissible, and the build amends `decider.py:5-6`, `:26-27` (`TERM_NAMES`) and `:52` (`watch`'s
   tuple) to say so.
4. **Class S enters through `odds` only, and that binds B24.13.** `p_carried(inp, track)` is P(carried)
   toward `for` (`proceeding.py:1116-1128`; the side note at `:1126`). `Option.ev` is the option's worth
   to the MOVER, in track units, and carries `rebound`, `_lasting`, the concession's cost, `silence_cost`
   and `invite`. So the believed chance of an option is
   `p_carried(inp, t + _sg(side) × ev)` for a `for` mover and `1 − p_carried(inp, t + _sg(side) × ev)` for an
   `against` mover, `t` being his believed track. A `p_carried` read on the move's immediate effect alone
   would drop Class S from the score, and one read without the side would invert it for `against`.
5. **The pick is over `Option`s, not over move ids, and that also binds B24.13.** The item exposed and the
   person struck are properties of the option (which item, which target), so a two-stage pick (a move id
   first, blind; then its item) cannot avoid a damning item once `present` is drawn, and §4's falsifier
   fails under it. Each option is one value whose choice operands are its `hearing_move` and its
   `argument_ground`, their cells summed into `pursuit` as `score_terms` sums a candidate's choice operands
   (B10.56, `chosen_values`).

**What reaches the pick today.** `pursuit` is `0.0` until a `hearing_move` cell is authored (Jordan's content,
`02_CHAR_choice_alignment.md`), and `make_decider` does not ask `odds` of a zero pursuit, so with no cell
the believed verdict and all of Class S are silent, and `stance` would be the only term that speaks. That
is the chooser's own arithmetic, not a defect of this design, but it fixes the order of switching on (§3).

**Falsifier (2).** For the term: §4, and §1's Class S run with a `for` and an `against` mover (§2.4's sign).
For the effort edit in `menu` (§6): a mover at `spent = stay − 1` sees every drawing option's `ev` fall
against the same mover at `spent` 0, and his non-drawing options (`rest`, `present`, `concede`) unchanged.
**Control:** `acts_on=None`, at which the decider is B24.13's to the byte. For the `menu` edit, its own
dial at 0, at which `ev` is today's.

## 3. Its setting at control, and its sweep

One dial, `Fixtures move_cost_gain` (a NUMBER row; `H` slot allocated by the build): **control `0.0`**, at
which `stance(v)` is exactly `0.0` for every value, `regard` is not read and the score is B24.13's, so
B24.13's realm hash is reproduced (and, at `sitting_exchanges` 0, no move is asked anyway). Refused below
0 and NaN (`stance_gain`'s rule: a negative weight inverts the sign). At `1.0` the term carries exactly the
weight the chooser gives `stance` outside the room — the S-consistent point, and the target. **Sweep:
`0` / `0.1` / `0.5` / `1.0`.** The low points matter. `regard` is not held to `STANCE_MAX` (25) at the shipped
`stance_clamp=False`, so it can run past 25, and `choice_temperature` is 0.05. At `1.0` one stance step
dwarfs a choice cell's pull, and the pick is all but fixed by regard. The reading at each point, over B24.15's `build_hearing` three hands: the share of each
move by sign of regard toward its `x`, and HEAR_B gate 5 (no constant decider best on all three hands).
**Do not ship it above 0 before `hearing_move` cells exist**: with pursuit 0, a positive gain makes an NPC
move by his relations alone, blind to his case (§2) — a NERS R failure (strategy absent), not a tuning.
v12 schedules no build (E-14); B24.13 lists the dial under `DIALS AT CONTROL`, target: §4's falsifier.

**Falsifier (3):** the realm hash at `move_cost_gain` 0 equals B24.13's (seeds 0–2), and at 0.5 on
`build_hearing` with `sitting_exchanges` above 0 it differs wherever an attendee holds a nonzero regard
toward a man one of his legal moves acts on (the dial is not inert; the fixture's regard is read first,
and a fixture where all such regard is 0 is no reading). **Reachability reading**, taken with it: count
the offered `present` options, over realm seeds 0–2 with `sitting_exchanges` above 0, whose item carries
a valenced deed cell. If the count is 0, "an item exposed" is reported UNREACHABLE in computed play (§1),
not passing. **Control:** the same
hash pair with `acts_on=None` at any gain.

## 4. The falsifier

`engine/season/tests/test_contest_decider.py::test_a_damaging_item_is_presented_less_and_equally_at_control`
This is a **game-state** test: it reads which move a person makes from his ledger and weights. Its lane is
`season_loop`, which `conftest.py:53` assigns B10.57's file. It is written red before the build. The
item's `cell` is hand-built as a `Claim`, because no computed item has one yet (§1).

- **Setup.** One person `p` with projected weights under which a deed kind `K` has `deed_valence < 0`, and
  a stance row `+R` (`R` > 0) toward `x`. Two hand-built views, identical but for ONE field: the cell of
  the single item in his hand, same item id `e`. View A: `cell = (x, K, True)` — a damaging item. View B:
  a cell that is no valenced deed. Each offers three options: `present e`, an `argue`, `rest`; no
  `hearing_move` cell authored; `odds` flat.
- **Assert, terms on** (`move_cost_gain` 0.5): over 200 keyed draws per view (the same 200 scopes), the count
  of `present e` under A is strictly below B's, and B's equals the count of each other option within the
  sampler's spread (B's present scores 0, as `argue` and `rest`). `assert checked == 200` per view.
- **Assert, terms at 0:** the two pick sequences are EQUAL, element by element (`==`, not a rate): the
  streams are keyed by the value's spelling, which is the same in A and B.
- **Mutations it must turn red:** the sign rule inverted (A presents more); `x` read off the item's
  `source` instead of `about` with `source` ≠ `x` (no difference); the term added at gain 0 (sequences
  differ); the term read toward `p` instead of `x` (no stance row toward himself: no difference).
- **Control:** the second assertion is the control; the first is the claim.

## 5. The default rite's `bears:` map — RULED (ladder step 5)

B24.09 landed `default` with `bears: {procedure: against, fact: against, definition: against,
justification: for}`, taking `IS-B2-SC-03`'s reading of the sides as HEAR_B's `Exhibit.side` (*"for" |
"against" the party*, the party being the man charged). **The code reads the sides the other way.** In
the tree a side is the bearer's, not the accused's: `sigma.py::proceeding_input` puts `claimants[0]`, the
man who brings the matter, at `for` (*"`claimants[0]` is the bearer (`for`)"*); `Rite.bears` is *"which side
bears it: he opens"*; and every other rite with a charge (`trial`, `inquisition`) says `bears: for`.
`Item.side` (B24.05, where HEAR_B's `Exhibit` landed) is the side that showed it — the mover's
(`proceeding.py`, effect `exhibit`). So the `against` the map names is the ACCUSED. Read by the code:
`Rite.bears` resolves to `against`, so in the six re-pointed rows the accused opens (`_speakers`), the
burden of putting the charge falls on him (`burden`: *"the bearer of a matter the other side must answer
has to put it"*), and the accuser becomes the side a press may lie on for want of a point (`pressable`).
`bears_by_rung` itself is carried to `Rite` and read by no code yet.

**Ruling:** the map keeps `IS-B2-SC-03`'s assignment of the questions (the accuser bears procedure, fact and
definition; the accused bears justification, his plea) and writes it in the code's side words:
**`{procedure: for, fact: for, definition: for, justification: against}`**, whose first-issue bearer, `for`,
is what `trial` already says. This is clearly right for the code. It agrees with the one builder that
assigns sides and with every sibling rite (`arrangements.yaml:122-188`), and it changes no ruling: it
corrects a translation. What it restores is the OPENER the six rows had before B24.09, `bears: for`. It
does not restore every row's burden. `burden` also needs the other side's reply to be `must`, and the three
rows that were on `debate` (`parliamentary_debate`, `council_of_state`, `excommunication_deliberation`)
replied `may`/`may` (`:171`) where `default` replies `must`/`must`. Their burden is new with B24.09, either way.
**A reader the current `against` also breaks: `abridged()`.** `data/arrangements.py:476-477` gives the one
`argue` to `rite["bears"]`. An abridged row's turns are not zeroed (`sigma.py:1394` zeroes only `bench`
and `declared` rows), and `card_odds` reads `r.bears` (`proceeding.py:1140-1142`). So today a `speak` filed
on a docket item naming one of the six arrangements gets an abridged row (`verb_table.yaml:1796`) that gives
the move to `against`. The actor at `for` then has no move, or the input refuses `nobody_speaks`
(`inputs.py:489-490`). It is not true that nothing reads the rite at `sitting_exchanges` 0. Realm-hash
equality across the fix must be MEASURED. It is plausibly equal only because computed docket items name no
arrangement (`world_q.py:533`). The edit is outside this file: `engine/season/arrangements.yaml` (`default.bears` and its comment's
⚠ sentence) and `engine/season/tests/test_sc_hearing_sitting.py:136`, `:185` (the pinned map and
`rite.bears == "against"`), with `season_registries.json` re-derived. When a reader of `bears_by_rung`
lands (the ladder's descent), it replaces `rite.bears` per rung in `burden`, `pressable` and `_speakers`;
that is the descent's build, not this.

## 6. What the build edits, when one is scheduled

- `decision/choose.py`: the shared `(p, subject, sign, fx, memo)` part, with the arm dispatch, the clamp,
  and the scale applied once. `stance_term` calls it with the row's sign.
- `decision/decider.py`: `acts_on`, `stance`, `TERM_NAMES`, and its docstring at `:5-6`, `:26-27`, `:52` (§2.3).
- `queries/inputs.py::Option`: `target`, defaulted `None`.
- `modules/social_contest/proceeding.py::menu`: fills `target`, and charges a drawing option the mover's own
  spend (§1, effort) behind its own dial at control 0.
- `rosters.yaml: proceeding_moves`: `acts_on`, and `regard_sign` derived as `verb_table` derives it (§2.2).
- `data/fixtures.py`: `move_cost_gain`, control 0.
- `seam/wrappers/sigma.py::_items_of`: sets `cell = (c.subject, c.predicate, c.value)` on every item built
  from a ledger claim (`:1466`). It has no writer for `origin`, so `impugn`'s `x` stays `None`.
- `seam/wrappers/sigma.py`: the hearing's `acts_on`, reading `Option.target`, `regard_sign` and the hand item.
  It passes the ledger `Claim` the item was built from (`Item.id` is the claim's id), never the `cell`
  tuple, to `deed_valence`, which reads `c.value` and `c.predicate` (`person_q.py:639`, `:650`) and would
  raise on a tuple. The `[ASSUMPTION]` on `proceeding.py::_worth` (*"the NPC decider's cost
terms are B24.12's, which replaces it"*) is answered: nothing replaces `_worth` — it is the exhibit's
in-room worth (Class S's channel), the item exposed is a relation (Class R), and both stand.

## 7. NERS

- **N.** Without Class R an NPC presses his brother as readily as his enemy and shows the deed that ruins
  his patron for a few points of weight; the room's choices would be free of the person who makes them.
  From the other directions: bottom-up it is one term the chooser already has. Laterally it reads the
  same `regard` the season's choices read, so a decided man's betrayal in a sitting and his grudge in a
  season are one quantity. That holds for the MOVER only. The room still weighs a hearer's bonds by
  `tie` (§1's ruling, by role), and the automatic policy's `grudge` survives for those it moves.
  Reachable in computed play only for `press` and `concede` until `_items_of` writes `cell` (§1, §6).
- **R.** Strategic: a player who knows who regards whom can predict what a witness will not show and whom
  an advocate will not press. Emergent without the player: an NPC holding a damning item about a friend
  withholds it, and the case turns on what was not shown. Complete at the extremes: regard is clamped where
  `stance_clamp` holds; a self-damning item reads self-regard; a value acting on nobody reads `0.0`.
- **S.** One methodology holds only where the arm is shared: the stance term goes through the one
  `stance_polarity` dispatch at the chooser's weight, unpriced as in `score_terms`. A copy that bypassed
  the arm would be a second ladder. Class S is priced once, in the module, and reaches the score through
  the one believed chance, signed by the mover's side. Effort's in-sitting spend is unscored until the
  `menu` edit lands. Zooms: the term the season loop uses is the term the room uses, for the mover.
- **E** (scored last, against N and R): one added term, three readings off one field and two cells; the
  player intuits it from relationships he can see. The cost is the shared-arithmetic refactor and one
  `Option` field.

## 8. What the ladder settled, and what it did not

Settled at step 5 (architecture), each recorded above:
- Class S gets no decider term (two ladders).
- Effort is `settle_efforts`' outside the sitting; inside it, a named `menu` edit.
- Face is not scored (no chooser term).
- The told item's sign is the deed's.
- The mover's relation reads `regard`; `tie` is the hearers'.
- The pick is over options.
- The `bears:` map is written in the code's side words.

Nothing here needs a ruling. **Owed by B24.13, in parallel** (re-read at its close, per the batch's PARALLEL
ITEMS line):
- its `odds` must read `Option.ev`, signed by side (§2.4);
- its pick must be over options (§2.5);
- it records the policy `grudge` as superseded for the NPCs it decides (§1).

If it lands otherwise, if it lands otherwise, Class S is absent
from the score and §4 cannot pass, and this design is re-read against what landed.
