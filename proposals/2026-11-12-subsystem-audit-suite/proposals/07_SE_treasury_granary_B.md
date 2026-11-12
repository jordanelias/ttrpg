# 07 · SE — the relief stock sits where someone holds it: the treasury is the granary (supersedes one clause of `07_SE_ground_and_granaries.md`)

Reconciled: 2026-11-12, U5d closure — folded **A-23** and **A-57 / A-58**. The addendum's P-16 (an absentee duke's treasury still feeds his duchy) gains: a duke in custody forms no act through his seat (A-23), so he cannot withhold or release; the rule of relief still runs (it is no act). A treasury sits at a seat's rung: when that rung is seized by a victor its seats pass with it (A-58, A-66), and the stores on the rung go with the rung's `hold` (stores are `Rung.stores`; no separate transfer is written).

## Status: PROPOSED

Carries findings F-SE-17, F-SE-22 and F-SE-23 and resolutions R-SE-28, R-SE-29 and R-SE-30 of
`audits/07_SE_audit_addendum_B.md`. It supersedes **only** resolution R3 and the territory-rung clause
of edit (c) in `proposals/07_SE_ground_and_granaries.md`. That proposal's endowment table, its
one-season stock, its remainder walk (`larder_walk`) and its fixtures stand; nothing here edits it.
Nothing is ratified by being written.

## 1. What changes in `engine/season/` at runtime

With `endowment_mode: uniform` (shipped): nothing. Every hash is the base hash.
With `ground`: `harness/populated.py::build_realm` seeds the relief stock at **the nearest rung above
each settlement at which an Office sits**, instead of at every territory rung. No verb, carrier, barrier
or module changes. The larder ladder reads it as it reads any rung above a home.

## 2. The problem, with evidence

- **Fourteen of the sixteen settled territories have no seat at the territory rung.** `build_realm(0)`
  seats 34 offices: `terr_T1` 10, `terr_T9` 6, `terr_T15` 1 (no settlement there), `duchy_hafenmark` 5,
  `duchy_valorsmark` 1, `duchy_varfell` 4, `r_valoria` 4, the foreign `set_alt_1` 2, one with no rung
  (addendum §8, E-2 and E-7; seed 0, no season run).
- **A requisition can only fill a seat's own rung.** `loop/effects_governance.py:538-549`: *"THE TREASURY
  IS THE SEAT'S RUNG AND NOTHING ELSE"*. So the superseded R3's *"what fills it is `requisition` into a
  territory seat's rung (built)"* names a path that exists at two territories.
- **Every other reader of a treasury reads a seat's or a holder's rung.** The attacker's field ration:
  `seam/wrappers/mass_battle.py::_seat_treasury` (the rung of the office the march is exercised through).
  Upkeep of sworn men: `loop/effects_economy.py::_renewals` (a payment out of a seat's rung). The
  governor's relief act: `engine/season/tests/test_in22_shortfall_reach.py`
  (`test_in22_the_governor_pays_the_shortfall_out_of_his_seats_rung_through_his_seat`, by name; the body
  was not read).
- **So a territory-rung granary is stock with no keeper**: nothing governing can refill it, it pays
  nobody, it provisions no field. It runs down and is gone.
- **The dependency the endowment creates has a recorded resolution about its channel.**
  `registers/editorial_ledger_archive.jsonl:477` (BALANCE-005, resolved 2026-04-13): *"Hafenmark operates
  through trade and diplomacy, not territorial control of food supply."* The ladder of a Hafenmark
  settlement is its territory, `duchy_hafenmark`, `r_valoria` (probe): no rung of another duchy is on it.
  The superseded proposal's reading for ARC-20 (*"Hafenmark's settlements drawing at a rung another duchy
  fills"*, first audit §13) can therefore be met only at the realm rung.

## 3. The resolution, decided

**R-SE-28. The granary is the treasury.** World-gen puts each settlement's relief stock at the first rung
in `ancestry(settlement)[1:]` that some Office names as its `rung`. On the built realm that is `terr_T1`
for the capital's three settlements, `terr_T9` for the Church's, the duchy rung for every other kingdom
settlement, and nothing for Schoenland (no seat on its ladder: it starts with its own larder only, which
is what a foreign island is). Ladder step 4: this is the rung `requisition`, `_renewals`, `_seat_treasury`
and IN-22's relief already treat as the treasury; one stock, not a second kind of store.

**R-SE-29. Relief is the rule; withholding is the act.** Subsistence is ruled territorial (ED-IN-0255) and
the draw up the ladder is built. Stock at a seat's rung is therefore open to every town beneath it with
no act. A holder who means to deny it moves it off the ladder (a `transfer` to a store beneath a
settlement or to another place) and that act is an Event with a witness. No `ration`, `open_granary` or
`hoard` verb is added (ladder step 1: the ruling decided the default).

**R-SE-30. The dependency bites through a person's store move, not through the ladder.** Whether hunger is
mechanical was settled after BALANCE-005 by ED-IN-0255. What BALANCE-005 still says is the channel, and
the ladder's shape agrees with it. ARC-20's execution artifact is re-worded (below).

**Named, not resolved (F-SE-23).** The realm rung tops three duchies' ladders. Once it holds stock, the
Crown's treasury feeds both other dukes' hungry towns by rule. This follows from the ruled ladder and is
not re-raised. It is stated here so that whoever flips `ground` reads it before the flip: the only way a
king starves a rebel duchy is to move grain off the realm rung, which the rebel's people can witness.

## 4. The exact edits, by owner

**(a) `engine/season/queries/world_q.py` — one reader, beside `governing_hold`.**

```python
def treasury_above(w: World, rung_id: str) -> Optional[str]:
    """The nearest rung strictly above `rung_id` at which some Office sits, or None. The one owner of
    *whose treasury relieves this place*; read-only; traces as a resolver."""
    seated = {o.rung for o in w.offices.values() if o.rung is not None}
    return next((r for r in ancestry(w, rung_id)[1:] if r in seated), None)
```

**(b) `engine/season/harness/populated.py::build_realm` — the stores seed, moved and re-keyed.** The seed
the superseded edit (c) placed *"after the garrison loop"* runs instead **after the offices are seated**
(it reads them), beside `mint_planned_works`. Under `endowment_mode == "ground"`:

- each settlement's `stores`: one season of its Sites' base yield (unchanged from the superseded text);
- for each settlement `S` with `t = treasury_above(w, S)` not `None`: `w.rungs[t].stores[k] +=
  granary_seasons × max(0, want_k(S) − yield_k(S))` for each eaten kind `k`, where `want_k` is the
  subsistence weight times the cohort weight seated at `S` and `yield_k` its Sites' base yield.

`granary_seasons` keeps its sweep (`0 / 4 / 8`; 0 is the control). The id scheme and the `uniform` arm are
untouched, so `build_realm(0)` hashes as the base under `uniform`.

**(c) Plan text, replacing the superseded R3's gate (AM-E-13).** *In a seeded realm run under `ground`,
every draw cell whose `source` is above a settlement names a rung at which an Office sits, and at least
one such cell exists.*

**(d) First audit §13, ARC-20's gate, re-worded** (an audit table, not code): *a `transfer.made` or
`exchange.made` by a person, whose giving rung lies under one duchy and whose receiving rung under
another, in a seeded run under `ground`.* It depends on CR-49's destination class (first audit R-SE-19).

**(e) `proposals/07_SE_valley_scenario.md`** needs no edit to its world (its granary is at `terr_valley`,
where its steward's seat sits). Its `hoard` policy is re-read by this proposal's R-SE-29: to hoard is to
take a candidate that moves stock off the ladder, not to refuse relief candidates.

## 5. The gate, and the falsifier

- **Execution artifact.** `ground`, `granary_seasons 4`, seed 0, eight seasons, no acts: every settlement
  whose own Sites do not cover an eaten kind holds body at scale while its treasury holds stock of that
  kind and falls when it empties, and every `source` above a settlement is one of `terr_T1`, `terr_T9`,
  `duchy_hafenmark`, `duchy_valorsmark`, `duchy_varfell`, `r_valoria`. By arithmetic on the first
  proposal's table at the shipped weights and need (not a run): 12 settlements make neither eaten kind
  (the seam territories T3, T4, T7, T9, T10, T17), 10 make grain and no salt (the field territories T2,
  T5, T6, T14) and 15 cover both (the harbour territories). The counts are re-read at the build; the
  first lane's hand-made reading stocked territory rungs and is not this one.
- **With play** (seed 2, where the FA audit read six `requisition.taken`): at least one requisitioned
  unit is later named in a draw cell's source. Stock an act put into a treasury is eaten by rule.
- **Falsifier.** A draw sourced at a rung with no Office; or a seat rung holding relief stock that no
  ladder reaches (the planted failure: seed at `terr_T15`). If under `ground` no duchy's treasury is ever
  drawn, the endowment left nobody short and the proposal moved nothing.
- **Control.** `uniform` reproduces the base hash; `granary_seasons 0` under `ground` shows the
  dependants short from the first season.

## 6. What this does not cross

ED-SE-0053's standing order (no hearth larder, no delivery across `contain`): no matter is delivered;
the draw reads up the ladder as ED-IN-0246 built it. H-160 limit 3 (the silent dearth is a balance
number): untouched. ED-WR-0011: no person is minted. H-309 (a holder who migrates keeps his seat): his
treasury keeps feeding his duchy; named in the addendum's §5 (P-16).

## 7. NERS reading (definitions: `CLAUDE.md` §0.06; E last)

- **N.** Cut it and the buffer above the household is a world-gen number that runs out; keep it and the
  buffer is a person's office. Bottom-up: one reader, no new store. Top-down: the duke's treasury is what
  a duke's treasury means. Lateral: the field's ration and the sworn men's pay now compete with the
  hungry for one stock, which is the campaign layer's first real decision
  (`07_SE_campaign_supply_and_muster.md`). Across scales: the realm rung is the reserve of last resort.
- **R.** Strategic: a holder chooses between leaving stock on the ladder, paying his men, provisioning a
  march and hiding it. With no player: treasuries run down, towns go short duchy by duchy, and the acts
  that follow have authors. Completeness: a polity with no seat on its ladder (Schoenland) has no reserve,
  stated; a seat rung with no settlement under it (`terr_T15`) is never seeded.
- **S.** The same stock is read by subsistence, upkeep and provision with one arithmetic each and no
  second ledger. It pauses nothing.
- **E, last, against N and R.** One six-line reader and a re-keyed seed. A player can say "the duke's
  granary feeds the duchy" without being told a rule.

## 8. Cost class

Edit, inside the first proposal's small build. Hash EQUAL at the shipped arms; under `ground` it is part
of that flip's declared mover.
