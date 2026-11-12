# INST-BYZ-B — the yearly stipend and the fisc: what a seat owes its sworn, the bill as a shortfall, and a collection that is drawn

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_BYZANTINE.md` §2.2, §2.5, §4, §6.3 item 4, §7.0, §10. Batch B. Depends
on proposal A (`dignity:`), on `07_SE_treasury_granary_B.md` (stores that exist at seat rungs) and on
the MATERIAL verb lane for `requisition`'s row text. Ratifies nothing.

## What it changes in `engine/season/` at runtime

1. Seat rows may declare `upkeep:`. Nothing moves at build: no built oath is termed, and none is
   made so here. The three oaths the founding houses and the Grand Master hold to `off_king` stay
   without a clock (a house that won its seat by deed is not kept by a wage); the oath a person
   swears in play to receive a dignity (proposal A, edit 7) opens with `oblige_term`'s term as every
   computed oath does (`loop/effects_governance.py`, `_new_oblige_term`), and that is the oath a
   stipend renews.
2. What a sworn person is owed is read per person (`world_q.upkeep_owed`), by the highest `upkeep` of
   the seats he holds that sit in the paying seat's purview, else the paying seat's own.
3. At MATTER, a seat whose terms falling due within a season exceed its rung's stores deposits a
   shortfall claim on its holder. The existing shortfall-sourced operands then form his `requisition`
   and `transfer` candidates. Arithmetic, no draw: it is a bill.
4. `requisition` is a draw with four bands. With `procedure_draws: off` (control) it moves the whole
   amount, as today.

## The problem (evidence)

- `build_realm(0)` (audit E-1): four live `oblige` edges, none with a term; no office declares
  `upkeep`; `r_valoria`, `terr_T1`, `duchy_valorsmark` hold `{}`. `_renewals`' own docstring
  (`loop/effects_economy.py:321`) says "no computed act forms an `oblige`", which is stale (`oblige`
  executed 26 of 26 at `aperture 2 0`, FA audit E-3), and "a person CHOOSING to pay upkeep is
  `H-158`'s `unblocks:`", which is not: nothing tells a seat-holder that terms sworn to his seat are
  falling due, so the mechanism Layer 1 names for upkeep (`04` §B.7, F.18) has subjects and no payer.
- `world_q.upkeep_of` (`:2748`) is one amount per paying seat. A court pays by rank.
- `requisition` moves `amount` whenever `stores >= amount` and the purview reaches (the row's typed
  cell): a tax is collected in full or refused at eligibility. `requisition.taken` is a
  `standing_routes: dominance` kind, so every collection reads as coercion in `person_q.stability`;
  nothing distinguishes a tax rendered from a tax taken.
- FA audit E-5: `requisition.taken` 0, 1 and 6 at realm seeds 0, 1, 2 over three seasons, and
  "nothing to take until `requisition` executes" (§7).

## The resolution, decided

The stipend is `upkeep`, the bond is a termed `oblige`, the payment is `transfer` through the seat:
all built. This file gives them subjects, makes the amount follow the grade, lets the bill reach its
payer as the claim form the engine already acts on, and makes collection a draw whose bands decide
how much arrives and how it is remembered. Paying is conservation and a clock; it buys a renewed term
and the payee's judgment of a `transfer.made`. It does not buy obedience: every later answer of his is
his own choice and its own draw.

## Exact edits

**1. `offices.yaml: seats[].upkeep`** — optional int ≥ 0, loaded onto `Office.upkeep`
(`state/carriers.py:1052`, the field exists and `__post_init__` already validates it). Authored:

| rows | `upkeep` | basis |
|---|---|---|
| dignity rows, by `dignity` 5, 4, 3, 2, 1 | 5, 3, 2, 1, 1 | `[ASSUMPTION; medium]`; sweep: flat 1 (H-158's shipped default) / linear 5..1 / the proposed |
| `off_king` (what the seat pays a sworn person who holds no graded seat) | 1 | `default_upkeep`'s shipped value, now stated on the row |
| every other row | absent | falls to `default_upkeep` as today |

Unit: units of the matter the paying `transfer` carries, per sworn person, per term (`upkeep_of`'s
own stated limit, H-158). The bill of edit 3 names `coin` (`rosters.yaml: matter_kinds`).

**2. No edit to the built oaths.** `offices.yaml:132-133` seeds `obligees:` with "no term (a seat
seeded at world-gen has no opening act to declare one)", and that stands: the dukes' and the Grand
Master's oaths are not stipendiary. (Considered and refused: a `meta.sworn_term` that would put all
four on a yearly clock. It would end the dukes' vassalage in season 4 of every run in which the King
did not pay them, and it would give the Grand Master's `release`, which ED-IN-0293 (7) makes the
Split, a second cause nobody chose.)

**3. `queries/world_q.py::upkeep_owed(w, seat_id, person_id) -> int`** — new, beside `upkeep_of`:
the maximum `Office.upkeep` over the seats `person_id` holds whose rung the paying seat's purview
reaches and that declare one; else `upkeep_of(w, seat_id)`. `_renewals` (`effects_economy.py:321`)
replaces its `upkeep_of(seat)` apiece with `upkeep_owed(seat, obligee)`; its order (soonest-maturing
first, ties by edge id) and its four clauses are unchanged.

**4. `loop/matter.py` — the bill.** In the step that already deposits `(rung, "shortfall:<kind>",
units)` from the larder write: for each office with at least one live termed `oblige` whose term
matures within `season` ticks, `bill = Σ upkeep_owed`; if `stores(seat rung, coin) < bill`, deposit
on the seat's live holder the claim `(seat rung, "shortfall:coin", bill − stores)`, firsthand.
`[UNVERIFIED]` the exact site and name of the larder shortfall deposit (`person_q.stability`'s
docstring places it in WITNESS from MATTER's write; read `loop/matter.py` and `loop/witness.py`
before landing). No new claim predicate: `SHORTFALL_PREDICATE` is reused, and
`rosters.yaml: shortfall_sourced_operands` (`kind`, `amount`) already forms a `requisition` and a
`transfer` from a held shortfall claim (`verb_table.yaml: requisition.requires_typed_note`).

**5. `requisition` — the draw** (the row is the MATERIAL lane's; this is what the institution needs):

```yaml
    counterparty: subject            # the place; its people are the opposition
    contests: a standing
    writes:
      Overwhelming: [Rung.stores, Rung.stores]
      Success:      [Rung.stores, Rung.stores]
      Partial:      [Rung.stores, Rung.stores]
      Failure:      []
    emits:
      Overwhelming: [requisition.rendered]
      Success:      [requisition.taken]
      Partial:      [requisition.taken]
      Failure:      [requisition.resisted]
```

| term | reads |
|---|---|
| pool | `faculty(w, p, "requisition")`; `rosters.yaml: verb_capability.requisition` → the vocation `copying` `[ASSUMPTION; medium]` (the clerical competence the roster already names) |
| `difficulty` | the band of `amount / stores(place, kind)`: under a quarter, under a half, under the whole, the whole |
| `opposition` | the place's regard against the collector: minus the mean `regard` for him among the persons (cohorts included, by weight) residing under the place |
| `stakes` | the place's `hunger_bands` band: `lean` one step, `hungry` two, `starving` three |
| `favourable` | one step each: the collector holds a `faction_sheet` Record of the place's faction (an assessment exists, `survey`); a person sworn to the exercised seat resides under the place; the collector's `conviction_stand(altonian_civics)` above zero |

By degree: Overwhelming moves `amount` and emits `requisition.rendered`, a new kind that is **not**
added to `standing_routes.kinds.dominance` (a tax paid willingly is no sign of unrest); Success moves
`amount` and emits `requisition.taken`; Partial moves `amount // 2` (at least 1) and deposits on the
collector a shortfall claim for the rest; Failure moves nothing and emits `requisition.resisted`,
which the place's people hold as a deed of the collector's. Every band is recoverable: he may collect
again, send force, or remit.

## Gate (execution artifacts)

1. *Nothing moves at build.* `build_realm(0)`'s `content_hash` is proposal A's (this file adds no
   Tenure, Record or claim at build); the four built oaths still read `term None`.
2. *The draw.* 400 seeds, a hand-placed `requisition` of half a place's stores by a collector the
   place regards at zero: all four bands occur; conservation holds in every seed (the two rungs' sum is
   unchanged); with `procedure_draws: off` the full amount moves in every seed.
3. *The court.* The `roga` scenario of proposal F under the auto chooser, seeds 0 to 19, eight
   seasons: `term.renewed` and `term.matured` on sworn oaths both non-zero across the seeds, and the
   per-seed pair reported; `requisition` by band reported. Control: the same seeds with
   `oblige_term: None` (H-159's control arm), in which no oath carries a term and no shortfall claim
   of kind `coin` is deposited.

## Falsifier

Empty the paying rung and withhold every `requisition`: every sworn term matures in season 4 and
`world_q.establishment_of(off_king)` is empty in season 5. If the terms do not mature, MATTER is not
reading them. Plant `upkeep: 0` on the dignity rows: one unit pays everyone, and `upkeep_owed` is not
read if the count renewed does not rise.

## NERS

N: without termed oaths the upkeep machinery has no subject (its own docstring); without the bill a
holder has no occasion to pay; without the bands a tax cannot be borne well or badly. All directions:
the payer (top-down), the paid (bottom-up: his term), the place (lateral: its stores and its memory).
R: whom to pay first when short is a choice; the no-player half is the unpaid court and the tax
revolt. Completeness: an empty fisc lapses terms and raises no error. S: the shortfall claim, the
`transfer`, the `Rung.stores` conservation and the obstacle form are each the existing owner's. E,
against that: two keys, one Query, one MATTER clause and one row's bands.

## Cost class

Small build. Movers: any run in which a `requisition` resolves, a bill is deposited, or a sworn
dignity-holder is paid. The build hash does not move.
