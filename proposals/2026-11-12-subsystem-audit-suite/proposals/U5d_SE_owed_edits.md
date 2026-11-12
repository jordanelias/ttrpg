# U5d-SE — owed edits: the settlement resolutions decided with no proposal file

## Status: PROPOSED (a plan for a later implementation lane; nothing here was executed)

Author: U5d closure lane (Fable), 2026-11-12. Carries `audits/07_SE_audit.md` R-SE-16 to -20, -22;
`audits/07_SE_audit_addendum_B.md` F-SE-23, F-SE-24, R-SE-31, -37, -38; `audits/16_PESSIMIST_SE.md`
F-PES-SE-09, -10, -12, -13, R-PES-SE-05, -07, -08, -09, -13 and §6.3's item for the determinism sweep.
Each section: owner, edit, gate, falsifier, movers, dependencies. Land order: §1, §8 (text), §3, §9 d,
§2, §7, §4, §10, §9 a–c, §5, §6.

## What it changes in `engine/season/` at runtime

§2: `transfer` and `migrate` form on a place that is not the actor's own and not a person-rung. §7: a
trade is formed on the kind the actor has to spare and the kind he lacks. §9 d: a debit leaves no zero
key. §4, §9 a: data that moves only when its arm is flipped. §1, §3, §5, §6, §8, §9 b–c, §10: register
text, a deletion of a field nothing reads, notes, a gate arm.

## §1 — register edits (R-SE-16, -17, -18; H-105, H-171, H-309, H-168)

`engine/season/hole_register.yaml`: H-105 and H-171 cites gain "`restore`: 0 attempts, seed 0, three
seasons, tree `601e715`; cause not isolated"; H-309 closed (a seat is a `hold` exercised `via`; absence
is not an act; ladder step 4); H-168's cite re-read (false since IN-45: 16 executed migrations from
computed acts, `aperture 3 0`). Gate: `python -m engine.season.harness.register --requirements` loads.
No code. Not done here: a fix for `restore` not reaching; it waits on the cause.

## §2 — CR-49's class on `transfer` and `migrate` (R-SE-19; F-SE-07, F-SE-09; F-PES-SE-13's third item)

- **Owner.** `engine/season/verb_table.yaml` rows `transfer`, `migrate` (the plan position CR-49 gives
  `exchange` the same); the decline in each effect.
- **Edit.** `referent_class: Rung` restricted to a settlement rung (a cohort may not `migrate` into a
  territory, a duchy or the realm: 485, 76 and 1 such open pairs read by the pessimist) and a `to != from`
  decline. A plan edit to CR-49's entry, so the three rows land as one.
- **Gate.** `python -m engine.season.harness.aperture 3 0` before and after: `transfer.made` to self
  goes to 0 (2 today, both to self); no `migrate` candidate names a non-settlement rung.
- **Falsifier.** A `transfer` whose `to` is the giver's own rung executes.
- **Movers.** Every seeded run with a `transfer` or `migrate` candidate. Declared.

## §3 — `Rung.envelope` (R-SE-20, SE-04 (b))

Delete the field through plan position IN-44 (its Layer 1 row), in IN-44's commit. Gate: `grep -rn
"envelope" engine/season --include=*.py` returns no reader or writer before the deletion (the audit's
claim; `[not re-opened]` by this lane). Movers: none if the field is unhashed; if `Rung` hashes it, one
declared re-pin.

## §4 — the ration's kinds at the supply flip (R-SE-22)

`engine/season/data/fixtures.py`: `field_ration_kinds`, shipped `["grain"]`; `modules/…/provision`
bounds a field by a kind only if the fixture lists it and `subsistence_weight` weights it. Lands inside
plan IN-52's flip entry, after `07_SE_treasury_granary_B.md` and with
`16_PESSIMIST_SE_B_harvest_walls_and_the_supply_gate.md` edit 4 (the load-time refusal). Gate: a
grain-only treasury fields troops in the flipped arm. Falsifier: it fields nobody.

## §5 — the top of the relief ladder (F-SE-23)

No edit: the ruled ladder stands (the realm rung feeds every town beneath it; the Church's and
Schoenland's ladders differ by the containment the world builds). Recorded so the consequence is read
when `07_SE_treasury_granary_B.md` lands: its gate adds one reading, the stock drawn from `r_valoria` by
settlements of each duchy per season, so a king's withholding (moving stock off the realm rung) is
visible as an act with a trail.

## §6 — notes for the builders of GROUND and ARCN (R-SE-31, -37, -38; F-SE-24)

The endowment rows are built with the addendum's annotations P-2 to P-4. `ration` is not a verb
(withhold and release are both `transfer`). `amount_shares` ships one member; `[250, 500, 1000]` is
flipped only after plan CP-T08-06 (`unrest`) or `U5d_SE_cohort_heavy_moves_and_caste.md` gives the
largest share a consequence path.

## §7 — the kinds a trade is formed on (R-PES-SE-09; F-PES-SE-10; owed to CHAR's formation)

- **Owner.** `engine/season/decision/options.py` (operand bags) for `exchange` and `transfer`.
- **Edit.** `kind` is the kind the actor's rung holds most of beyond its own draw; `return_kind` is a
  kind its ladder was short of at the last MATTER (`World._subsistence_shortfall`), else the fixture
  default. Both are read from the actor's own ledger and rung (AX-2).
- **Gate.** In `harness/scarce.py`'s short town, the formed `exchange` asks for the kind it lacks.
- **Falsifier.** A hungry town offering grain for the default return kind.
- **Movers.** Runs with an `exchange` or `transfer` candidate. Declared. Depends on §2.

## §8 — one line of the determinism sweep (PES-SE §6.3)

`audits/18_DETERMINISM_SWEEP.md:110` lists `world_q.subsistence_draw` among "checked, drawn". The SE
pessimist read it as arithmetic (F-PES-SE-02). The two readings are recorded side by side in the closure
(`unified/U5_FINDINGS_CLOSURE_U5d.md` Part 9); the sweep's line is not deleted. What settles it is the
draw `09_WR_B_draws_not_thresholds.md` edit 2 adds for the hungry body, on the one ladder (A-54).

## §9 — readers or deletions (R-PES-SE-05, -07, -08, -13; F-PES-SE-13)

a. `rosters.yaml: works_cost` rows `garrison`, `barracks`, `archery_range`, `stable`,
   `siege_workshop` gain `ore: 10` beside timber `[ASSUMPTION; medium; Jordan to correct]`, so `ore` has
   a reader. A data edit; a mover only where such a works is built.
b. The hunger bands keep their census reader only until `unrest` (CP-T08-06) or the cohort's moves read
   them; not deleted.
c. `coin` stays a registered kind; nothing may read it until something yields or mints it.
d. `loop/effects_shared.py::_debit` drops a key it has brought to 0 (the rule `provision.py` already
   states). Gate: a `build` leaves no `timber: 0` in the payer's stores. A hash mover wherever a debit
   empties a kind; declared.
e. Site-kind names `field` and `woodland` are roster rows when GROUND's endowment table lands.

## §10 — stocking and migration (F-PES-SE-12)

`07_SE_ground_and_granaries.md` §4 (c)'s gate gains one arm: `migrate`'s executed count and refusal
clauses in the stocked arm against the unstocked control (10 of 84 executed against 0 of 239, cause not
isolated). With A-50 the starting stock is drawn within bounds, so some larders start low; the arm
shows whether migration returns with them. Falsifier of the stocking edit: migration at 0 in every
stocked seed with low-larder towns present.

## NERS (E last)

N: each item is a decided resolution with no other carrier. R: trade and migration become responses to
want. S: `transfer`, `migrate` and `exchange` take one class rule. E: ten short items; two code edits.

## Cost class

Edits (§1 to §4, §8, §9, §10), a note (§5, §6), a small build (§7).
