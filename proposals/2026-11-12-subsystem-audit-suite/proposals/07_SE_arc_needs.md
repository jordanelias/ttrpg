# 07 · SE — what the provided arcs and characters need of the settlement layer: the three SE-owned changes

Reconciled: 2026-11-12, U5d closure — folded **A-12** and **A-56**. §3 b (amount as a choice) ships one share until a consequence path exists (`U5d_SE_owed_edits.md` §6); that path is now the cohort's own moves as well as `unrest`. NPC-083's and NPC-037's seats may carry a modifier on their rolls (A-12); no edit here authors one.

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §2 (A-81): §3(b) gains the write a refused or lesser `requisition` band leaves (the refuser's remembered deed); 7b-7 (named tests for (a) and (b)); C3-N22 over 7b-13 (the "two seasons" figure is left as measured and marked unverified against `07_SE_ground_and_granaries.md` §2's three-season reading, since U3 decided each file states its own horizon and U4 re-reads one instrument; 7b-13's change to "three seasons" is not applied); tier and batch (R3 7b-0; U3 B12).

## Status: PROPOSED

Lands in batch: B12 (world motion and ground), after `07_SE_ground_and_granaries.md` with `07_SE_treasury_granary_B.md` and before `16_PESSIMIST_SE_A` (U3 §1 item 13).
Depends on: nothing proposed for (a)–(c); the amount flip waits on `U5d_SE_owed_edits.md` §6 (B12, a consequence path).

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-27) — a `CHOICE_RANGES` range is a closed roster's members and needs a carrier the row writes; the share range is a three-member roster, not an integer list.

Carries §13 of `audits/07_SE_audit.md`. Most SE-mechanism needs in the case corpus are met by positions
the plan already holds (CP-T08-05, -06, -07; CR-49; CR-67; IN-52) or by this suite's other SE proposals;
the table in §13 names which. Three changes are owned here because no position carries them.

## 1. What changes in `engine/season/` at runtime

1. **A settlement-scale case world has a population.** `harness/corpus_run.py::build_at` seats a cohort
   and stocks a larder when the case's overlay declares one, so a case whose story is a settlement's
   demand has a settlement that can demand. Off for every case that declares none: the corpus hashes are
   unchanged.
2. **`requisition` and `transfer` carry an amount the actor chose from a closed set**, so a tithe or a
   relief is a decision with a size (NPC-013, NPC-037, NPC-083). Shipped at a one-member set (today's
   value), so nothing moves until a second member is authored.
3. **A foreign settlement can hold stores**, so a trade official has something to trade (NPC-090).
   World-gen content only.

## 2. The problem, with evidence

- `python -m engine.season.harness.corpus_run` (seed 0, 143 cases): 103 `RUNS-UNDECLARED`, 40
  `SPAN-UNAUTHORED`, the NPC bar and the ARC bar both `NOT-COMPUTABLE`. Of the settlement verbs,
  `transfer` and `move` executed somewhere in the corpus; `build`, `found`, `exchange` and `sabotage`
  were only refused; `migrate`, `requisition`, `restore`, `work` and `raze` were never attempted.
- No case world holds an eater: `build_at` seats no cohort (`cohorts.yaml:53-55`; H-171), and since
  `24f` only a cohort eats. So in every one of the 143 worlds the subsistence pass runs over nobody, no
  shortfall is recorded and no settlement generates a demand. NPC-083's third `core` need (*"the
  settlement itself must be able to generate demands … a shortfall"*) is unreachable in its own world
  whatever the engine can do elsewhere (`harness/scarce.py` shows it can).
- Every computed store move is `default_transfer_amount` (1) unless a shortfall claim supplies the gap
  (`decision/options.py::_from_shortfall_claim`). In the realm the two executed `transfer`s in two
  seasons at seed 0 each moved 1 grain against a settlement stock in the hundreds `[UNVERIFIED: C3-N22 —
  `07_SE_ground_and_granaries.md` §2 and `07_SE_valley_scenario.md` §2 read "2 units of 13,690 in three
  seasons" on `se_probe.py`; the horizons differ and U4 re-reads one instrument]`. NPC-013's
  *"aggressive wealth extraction"* and a cautious cardinal's are the same act.
- `harness/populated.py:1163-1170`: a foreign faction's settlement has *"no quarter, building, site or
  garrison"*, and no stores. `p_npc_090` lives at `set_alt_1` and his one executed act in two seasons at
  seed 0 is a `move` to where he already stands.

## 3. The exact edits

**(a) `harness/corpus_run.py` — a `world:` overlay block.** The overlay loader beside `CAST_KEYS` gains a
second closed set, `WORLD_KEYS = ("cohort", "stores", "sites")`, read from the case's
`cases/exercises/<id>.yaml`:

```yaml
case: NPC-083
world:
  cohort: {weight: 6}                 # seated at the case's settlement rung, as seat_cohorts seats one
  stores: {grain: 8, salt: 4}         # the settlement's larder at build
  sites:  [harbour]                   # producing Sites at the settlement; [] is a place that makes no food
```

`build_at` applies it after the cast: the cohort through `harness/populated.py::seat_cohorts` (one
owner of what a cohort is), the stores as a builder's write, the Sites as it already mints Sites
(`corpus_run.py:504`). A case with no `world:` block is built as today. The loader refuses a key outside
the set, a weight that is not an int above 1, a kind outside `site_kinds`, and a `world:` block on a case
whose `scale` is `person` (the corpus's person-scale worlds stay rooms).
[ASSUMPTION; medium; Jordan to correct; revert: delete the block and `WORLD_KEYS`.]

Authored in the same change for the three cases whose `core` needs turn on it: NPC-083 (above), NPC-013
(`cohort` at each of his two case territories' settlements, stocked, so a tithe has something to take and
someone to take it from) and NPC-037 (stores at the Crown seat's rung, so the treasury post has a
treasury).

**(b) `engine/season/rosters.yaml: choice_sourced` — `amount` as a choice.** The mechanism exists:
`decision/options.py::_fanned_choices` fans a bag over the closed sets a row's `choice_sourced` keys
range over (`marshal`'s `role × retreat_at`), and a one-member range is not fanned. Add:

```yaml
  amount_shares:
    source: "proposals/2026-11-12-subsystem-audit-suite/proposals/07_SE_arc_needs.md"
    open: false
    ordered: true
    note: "The share of the giving rung's stock a store move takes, per-mille. One member is the control: no fan."
    values: [1000]          # shipped: one member, so no act is renamed and no hash moves
  choice_sourced:
    requisition: [amount_share]
    transfer:    [amount_share]
```

`_operands` computes `amount` for these two rows as `max(1, stock_known × share // 1000)` where
`stock_known` is the actor's newest `stores:<kind>` claim about the giving rung (CR-23's stock report is
its source; `LedgerReader` reads it) and falls back to today's derivation when he holds none. Authoring
`[250, 500, 1000]` is the flip and a declared mover. The amount is a decision; the store move itself
resolves by the verb's own draw (`U5d_SE_owed_edits.md` §7, A-24), and every band leaves a write (A-81): a
`requisition` that is refused, or that lands a lesser band than the share asked, leaves the refusing
holder's deed as a claim in the requisitioner's ledger and his own (the `a_refusal_is_remembered` carrier,
`16_PESSIMIST_CORE_a_refusal_is_remembered.md`), so a refused larger share is a grievance someone holds, not
a null scene. Which share a person takes is then the chooser's
ordinary ranking: the candidate's pursuit cells differ by share only if `tables.pursuit_projection` is
given a cell for it, which is the CHAR lane's content (cross-listed in §14 of the audit).
[GROUNDED, 25 G-27: a range is the member tuple of a closed roster (`data/verbs.py:1698-1699`), and a
key also needs a `CHOICE_CARRIER` the row writes (`:1700`, `:1708`). The one number-valued range today is
spelt as strings: `ORDER_RETREAT_AT = ('none', '0.5', '0.25')`, `modules/mass_battle/massbattle.py:226`.
So the range is a roster of three members, by that precedent `'250'`, `'500'`, `'1000'` or the three
names; a bare integer list is not a shape the tree has.]

**(c) `harness/populated.py` — `FOREIGN_CAST` rows may carry `stores:`.** One optional key on the
settlement entry of a `FOREIGN_CAST` place, written as a builder's stores seed at the foreign settlement
rung. Shipped absent. With CR-49 (`exchange` names another rung) it gives NPC-090 a counterparty stock.

## 4. The gate, and the falsifier

- **(a)** `python -m engine.season.harness.headless --case NPC-083 --seasons 4 --seed 0`: a
  `stores.changed` Event at the case's settlement carries a `shortfall:<kind>` Observation, and the
  governor holds a claim of it the season after. **Falsifier:** the governor holds no such claim (the
  seat channel does not reach a settlement-rung seat). **Control:** the same run with the block deleted
  records no shortfall and reproduces the committed corpus hash for the case.
- **(b)** On `harness/scarce.governed` with `amount_shares: [250, 1000]`: the governor's candidate set
  holds two `requisition` candidates differing only in `amount`, and the executed one moves that amount.
  **Control:** `[1000]` reproduces the shipped `scarce` hashes.
- **(c)** `build_realm(0, foreign=True)` with the key absent hashes as today.
- **Named tests (7b-7).** New file `engine/season/tests/test_corpus_world_overlay.py`:
  `test_world_block_seats_a_cohort_stocks_a_larder_and_mints_sites`,
  `test_world_block_refuses_an_unknown_key_a_bad_weight_a_bad_site_kind_and_a_person_scale_case`,
  `test_case_without_world_block_hashes_as_before`. In the existing `engine/season/tests/test_demand_delivery.py`:
  `test_amount_shares_one_member_is_not_fanned`, `test_two_members_fan_two_candidates_differing_only_in_amount`,
  `test_a_refused_requisition_leaves_a_claim_of_the_refusal` (A-81).
- **For the arcs:** none of these makes an arc simulate end to end alone. The execution artifact for
  that is §13's ordered list; each entry names the seeded run in which the arc's beats must occur from
  persons' acts.

## 5. NERS reading

- **N.** Cut (a) and the corpus cannot observe any settlement need; cut (b) and extraction has no size,
  so NPC-013 and NPC-037 are indistinguishable from any seat holder.
- **R.** (b) is the smallest change that makes governing a choice of degree rather than of kind.
- **S.** (a) reuses `seat_cohorts`; (b) reuses the choice fan; (c) reuses the stores seed. No new shape.
- **E, last.** Three closed-set additions.

## 6. Cost class

Small build (a); edit plus content (b); edit (c). Hash EQUAL at every shipped arm. Tier: `sonnet`
(R3 7b-0).
