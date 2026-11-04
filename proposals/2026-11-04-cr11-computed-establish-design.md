# CR-11: where the office a computed `establish` founds is described

## Status: PROPOSED (design reference for CR-25's builder; the code is the mechanism, CLAUDE.md §0.05)
## Lane: IN

**What this is.** The design that `workplans/valoria_master_workplan_v11_part4.md` `### CR-11` asks for. It
records the derivation CR-25 (same file, `### CR-25`) builds, and nothing else. It describes intent. Whether a
computed `establish` executes is shown by CR-25's tests and realm reading, not by this file. Every symbol
below was opened at the cited line on the tree at `6732c952`.

**Why a computed act refuses today.** `loop/predicates.py:218` `office_described_by(a)` returns `None` unless
the payload carries `office`, `post`, `rung` (non-empty strings) and `remit` (a list of strings). It takes no
World. A computed payload is `_payload_of` (`decision/choose.py:494`): the chooser's operands plus `subject`.
The closed operand roster (`rosters.yaml:2078`, `requires_operands`) names none of `office`, `post` or
`remit`, and the doctrine that forbids a ninth operand is written at `rosters.yaml:2119` and
`decision/options.py:1008-1009` (`_derive_operand`). The held-Record route (`record_sourced_operands`,
`rosters.yaml:2106`) cannot carry them either, because no record kind has those keys (`record_kinds.values`,
`rosters.yaml:225-230`). `_req_establish` (`loop/predicates.py:251`) therefore refuses at clause 1.

## 1. The derivation: one reader, World-taking, from `subject` and `Act.via`

A sibling of `office_described_by` takes `w` and works out the whole office from two things the act already
carries: `subject`, a rung, and `Act.via`, the seat exercised (`state/carriers.py:692`). It adds no operand
and invents no office. Both `_req_establish` (`loop/predicates.py:302`) and `_eff_establish`
(`loop/effects_governance.py:229`) call `office_described_by` today, so both must call the sibling.
Otherwise the precondition admits an office the effect never writes. A hand-built act that carries the
overlay keys keeps its current reading.

| field | source |
|---|---|
| `rung` | `subject`. It must pass four conjuncts, each a refusal: (i) `state/gate.py:507` `in_holdings(w, actor, rung)`; (ii) `state/gate.py:370` `purview_reaches(w, via_seat, rung)`; (iii) the rung's kind sits strictly below the seat's rung kind on `rung_kinds` (`rosters.yaml:267-270`, read as `RUNG_KINDS`, `data/rosters.py:647`, by the ordinal comparison `state/world.py:196` `rung_kind_ascends` already owns); (iv) `state/gate.py:495` `seated_on_the_rung_above_structure(w, via_seat, founded)`, so the seat exercised sits on the rung's parent and `rung_above_in_holdings` (`state/gate.py:564`) can be satisfied by the founder through the same seat (H-90 message 2) |
| `post` | `offices.yaml:168-179` `titles.domains` (read as `TITLE_DOMAINS`, `data/rosters.py:1044`), the post whose value is the rung's kind. The pairing is read as data, never as a branch on a kind `[ASSUMPTION; medium; Jordan to correct; revert: the post is chosen another way]`. Where a kind has two posts (King/Queen, Duke/Duchess, Count/Countess), the first in authored order is used `[ASSUMPTION; medium; Jordan to correct; revert: the second, or the eventual holder's]` |
| `faction`, `body` | the exercised seat's. A seat with a `body` founding a titled post is refused by the constructor (`refuse_a_title_in_a_body`, `state/carriers.py:926`), and clause 1 turns that refusal into `False` |
| `remit` | the seat's `remit_acts` less `confer` and `revoke` `[ASSUMPTION; medium; Jordan to correct; revert: the full remit]` |
| `conferral` | `appointed` (`rosters.yaml:2630`). It passes `has_conferral_basis` and `has_filler` (`state/gate.py:780`, `:705`) |
| `revocation` | `rung_above_in_holdings` (`rosters.yaml:2670`; rule at `state/gate.py:585` `REVOCATION_RULES`) |
| `office` (id) | deterministic from (rung, post), so the same founding forms the same id. A repeat founding meets clause 4's existing-id arm, and a different seat's faction or body refuses there as a re-founding |

The `Rung` referent that offers the subject is CR-25's `holdings_to_found(w, p)` stamper term, placed after
`queries/world_q.py:3073` `larders_in_purview`. This file does not design it further.

## 2. The two checks inside `_req_establish` clause 5 (M8, taken: H-132 (b), H-144 (b))

- **H-144 (b), purview on a re-remit** (`hole_register.yaml:1840`). Today clause 5
  (`loop/predicates.py:337-338`) asks `may_fill` only when a live `hold` exists, so a vacant existing office
  can be re-remitted from anywhere. Under (b) the test becomes "the id is an existing Office", which clause 4
  has already computed as `held_as == "Office"`. On any existing office, vacant or held, clause 5 then asks
  `may_fill` (`state/gate.py:813`), which carries `purview_reaches` on the exercised seat. A founding is not
  an existing office. Its purview check is conjunct (ii) above.
- **H-132 (b), a reduction is a partial revocation** (`hole_register.yaml:1684`). A re-stamp whose new remit
  drops any act from the current one must pass `may_revoke(w, actor, via, current)` (`state/gate.py:798`).
  That predicate is the one owner that wraps `REVOCATION_RULES` together with `seat_hold` and the basis-roster
  test. Reading `REVOCATION_RULES` directly would make a second copy of it (§8). The check is asked where a
  live hold exists, because H-132 concerns a sitting holder's grant `[ASSUMPTION; medium; Jordan to correct;
  revert: ask it on every existing office]`. M8 (a) follows from this: a seat with `revocation: None` is in
  no basis, so `may_revoke` is False and its grant cannot be reduced. No seat with no revocation basis is
  stripped. `depose` is CLOSED, as the card states, and answered by CR-37 `[ASSUMPTION; medium; Jordan to
  correct; revert: restore the two clauses]`.

## 3. The falsifier CR-25's build carries (as the card states it)

**Hand-built set.**
1. A King holding a territory inside his purview founds `Lord` there, and `w.offices` gains the derived row.
2. A founding on a territory he does not hold refuses.
3. A founding at equal rank refuses: the Confessor at `terr_T9` (`offices.yaml:369-371`).
4. A re-remit of a vacant office outside his purview refuses.
5. A reduction of a `revocation: None` seat's grant refuses.
6. The founder revokes the founded Lord through the same seat, and the revocation executes.

**Planted failure.** Dropping conjunct (i) turns test 2 red.

**Control.** With `holdings_to_found` off, the hash matches the pre-item hash.

**Realm reading.** `python -m engine.season.harness.aperture 4 s`, s = 0-2: `establish` executes at least
once, with `Act.via` a seat that grants `confer`. This is the R-04 line, so it runs on Jordan's call.

## Where the card and the tree differ

- **Line citations.** `rosters.yaml:1864-1890` (`record_sourced_operands`) is now `:2106-2140`.
  `rosters.yaml:1877` (the ninth operand) is now `:2119`. `decision/options.py:976-977` is now `:1008-1009`.
  `rosters.yaml:225-230` still holds `record_kinds.values`.
- **Conjunct (iv) in prose versus the named function.** The card's prose, "a rung whose parent holds a seat
  of the same holder", accepts any of the holder's seats on the parent. `seated_on_the_rung_above_structure`
  asks about the exercised seat alone. This file takes the function, which is what lets test 6 revoke
  "through that seat". Under it, (ii) and (iii) both follow from (iv): the parent is the seat's own ground
  (`_ground_reaches`), and `contain` ascends strictly (`rung_kind_ascends`). They stay named refusals, as the
  card lists them. Test 3 therefore refuses at (iii) and at (iv) alike and cannot tell the two apart.
- **Test 1's "King".** In `build_realm`, territories hang under duchies, or directly under the realm only
  when Church-held or unheld (`harness/populated.py:1039`). So no realm seat meets (iv) on a territory it
  holds. The realm route goes through the duke seats instead (`off_duke_valorsmark`, `offices.yaml:200-207`,
  held by the King's NPC-020). Test 1's King needs a hand-built territory directly under the realm, which
  canon's unassembled territory allows. A read-only probe on `build_realm(0)` at this tip returned 16 live
  holds on a rung and 14 holdings that meet (i) and (iv) through a seat that grants `confer`. The card's
  "15 live holds" is therefore not the reading here. CR-25 still re-runs and attaches the probe.
- **"The purview check on a founding (H-144 (b))".** H-144 (b) covers re-remitting an existing office
  (`hole_register.yaml:1843`: founding "IS the intended, unblocked case"). The purview check on a founding is
  conjunct (ii), which comes from CR-25.
- **`titles.domains` maps post to kind,** and the mapping is many-to-one for three kinds. Reading it in
  reverse needs the pick recorded in §1.
- **M8's corrected throne basis is not yet in the tree.** `revocation_bases` holds two values
  (`rosters.yaml:2670`) and `off_king` has `revocation: null` (`offices.yaml:194`). Adding the third value is
  CR-37's work and does not affect this derivation.
