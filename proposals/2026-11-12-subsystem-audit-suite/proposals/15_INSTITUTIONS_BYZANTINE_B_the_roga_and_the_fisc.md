# INST-BYZ-B — the yearly stipend and the treasury: what a seat owes its sworn, the bill as a shortfall, and a collection that is drawn

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-19, X-22, X-26, X-27, X-30) — `requisition`'s row is `14_VERBS_MATERIAL_B_stores.md` §4's (graded, no capability row, `stakes` by the share asked, the cohort's `regard`); edit 5 survives as terms on that row (`remove`; `evidence` for a held assessment; `obligation` where the levied are sworn to the seat) and as two requests to that lane (Overwhelming emits `requisition.rendered`, outside the dominance kinds; Partial deposits a shortfall claim for the rest); the hunger band as `stakes`, the `copying` capability row and the `altonian_civics` step are withdrawn; the payment of a stipend is that lane's drawn `transfer`, not arithmetic; the bill's shortfall claim names `default_store_kind`, not `coin`, until `coin` has a producer; `procedure_draws` is not added (the task row's control is `task_draw_arm`). Edits 1 to 4 otherwise stand. Every finding below stands.

Re-grounded: 2026-11-12 (audit §18) — one addition: the treasurer's seat declares the kit's `audit_at_exit` (`15_INSTITUTIONS_BYZANTINE_grounding_mechanisms.md` item 1; sources `research/governance/governance_modes.md:329`, `research/fa_se_historical_precedent_research_v1.md:127`). The stipend's payment ceremony stays memory-grade (the tree's Liudprand is the receptions of 949 and 968 only); "an unpaid court is an unbound court" has sourced cousins (`research/governance/political_hierarchy_standing.md:20`, `:457`) and one shipped precedent (`research/game_precedent_suite/tutorials/T13_koei.md:78`); tax farming and its term are `research/fa_se_historical_precedent_research_v1.md:99-103`, `:204-208`. The fiscal vocabulary (assessor against collector, joint liability, reversion) stays memory-grade.

Reconciled: 2026-11-12, U5d closure — folded **A-13**: the exit audit on seats that hold money is one of the three ruled seat facts (the key is `audit_at_exit`, X-12). No step changes.

Reconciled: 2026-11-12, wave 3 lane W3-4b — applied `R4_READ.md` §1.7 (BYZ_B: e4's MATTER deposit AMBIGUOUS, F-R4-02; e5 `requisition.rendered` CONFLICT with MATERIAL-B), §2 (A-25 row: the favourable list becomes levels), §6 (C3-N24: `oblige` 26 of 26), §7 (INCOMPLETE: the bill's claim site; `rendered`), 7b.0, 7b.7 ("the bill is not a MATTER claim: `world_q.upkeep_owed` and a stamp `bills_due(w, p)` … as `vacancies`"); `U3_CONFLICT_LEDGER.md` C3-C7 (MATTER emits `term.matured` only), C3-C10, C3-N24 (name the route), C3-Y7 (MATERIAL-B, B12, lands before this file; the kind's name is U1's). Changed: edit 4's bill is computed when read (a stamp beside `vacancies`), not a claim MATTER deposits; edit 5's body now follows this file's first `Reconciled:` line (the row is MATERIAL-B's; this file supplies terms as levels and two requests; the hunger band, `copying` and `altonian_civics` are removed from the body); the bill names `default_store_kind`, not `coin`; the controls are the task row's (`task_draw_arm`) and the pinned roll; the `oblige` 26 of 26 figure names its route. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "fisc" → "treasury" (glossary loan words). A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "capability" in prose → skill (1); "trained score/rank" → skill score (1).

## Status: PROPOSED

**Implementation block (W3-4b; `R4_READ.md` 7b.0).** Lands in batch: **B33**, first (`U3_DEPENDENCY_ORDER.md` §1 item 33). Depends on: `15_INSTITUTIONS_BYZANTINE_A` (B32), `07_SE_treasury_granary_B.md` (B12, stores at seat rungs), `14_VERBS_MATERIAL_B_stores.md` (B12, `requisition`'s and `transfer`'s rows; C3-Y7). Lane tag: FA (edit 5 is a cross-lane request to MATERIAL-B's owner). Tier: `sonnet` producer, effort `high`; one `opus` read of gate 3's renew/mature table. Named test: `engine/season/tests/test_inst_byz_b.py`. Standing sentences: *Pool* — `requisition`'s pool is MATERIAL-B's, the one pool rule on the collector's skill score (A-6, A-7, A-8). *Failure writes* — a `requisition` Failure emits `requisition.resisted`, a deed of the collector's the place's people hold (A-81). *Draw keys* — the draw is MATERIAL-B's, keyed `H(w.world_seed, w.tick, <place id>, "requisition.draw")` (A-30); this file adds none.

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
3. A seat whose terms falling due within a season exceed its rung's stores **reads** as owing a bill:
   `world_q.bills_due(w, p)` stamps the shortfall on its holder's question when read (the `vacancies`
   shape, L-4), and his `requisition` and `transfer` candidates form from it. Arithmetic, no draw, no
   write at MATTER: it is a bill.
4. `requisition` is a draw with four bands (MATERIAL-B's row). Its control is the task row's
   `task_draw_arm: off`, under which it moves the whole amount, as today.

## The problem (evidence)

- `build_realm(0)` (audit E-1): four live `oblige` edges, none with a term; no office declares
  `upkeep`; `r_valoria`, `terr_T1`, `duchy_valorsmark` hold `{}`. `_renewals`' own docstring
  (`loop/effects_economy.py:321`) says "no computed act forms an `oblige`", which is stale (`oblige`
  executed 26 of 26 at `aperture 2 0`, FA audit E-3: realm, seed 0, two seasons, chooser-formed
  `own`-row acts in computed play, not the four build-seeded edges; `audits/06_FA_audit.md:76-81`.
  `14_VERBS_SOCIAL2_B`'s "0 persons with `seats_named`" counts a different thing, who holds a named
  seat-holder claim, and the two are not reconciled here; C3-N24), and "a person CHOOSING to pay upkeep is
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
own stated limit, H-158). The bill of edit 4 names `default_store_kind` (this file's first `Reconciled:`
line: `coin` has no producer at build).

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

**4. `queries/world_q.py::bills_due(w, p)` — the bill, computed when read.** Beside `vacancies` (L-4)
and `upkeep_owed`: for each office `p` holds with at least one live termed `oblige` whose term matures
within `season` ticks, `bill = Σ upkeep_owed`; if `stores(seat rung, default_store_kind) < bill`, the
stamp is the referent `(seat rung, "shortfall:<default_store_kind>", bill − stores)` on `p`'s question,
read when read and stored nowhere. MATTER writes nothing for it (C3-C7; `write_matrix.yaml` gives MATTER
no claim). `rosters.yaml: shortfall_sourced_operands` (`kind`, `amount`) then forms a `requisition` and a
`transfer` from the stamped referent exactly as from a held shortfall claim
(`verb_table.yaml: requisition.requires_typed_note`). `[UNVERIFIED: that `shortfall_sourced_operands`
reads a stamped referent as it reads a held claim; if it reads only claims, the stamp's referent class is
added to its reader, one line, in the same commit.]` `loop/matter.py` is not edited.

**5. `requisition` — what the institution asks of MATERIAL-B's row** (`14_VERBS_MATERIAL_B_stores.md`
§4 owns the row, its `contests:` shape, pool and bands; X-27; it lands first, B12).

- **Terms, in the SC form** (C3-C10: what helps the collector is levels, nothing lowers the obstacle):
  obstacle `distance` (OBS member 20, hops from the exercised seat's rung to the place; D-U1-11k);
  `stakes` by the share asked (MATERIAL-B's); the place's `reception` toward the collector (the cohort's
  `regard`, hostile half). The collector's levels: `proofs` for a held assessment (a `faction_sheet`
  Record of the place's faction, from `survey`), and `obligation` where persons residing under the place
  are sworn to the exercised seat.
- **Request 1 (open; the name is U1's, U3 §11):** Overwhelming emits `requisition.rendered`, a kind
  **not** in `standing_routes.kinds.dominance` (a tax paid willingly is no sign of unrest), where
  MATERIAL-B's row emits `requisition.taken` at every carrying band. Recommended: adopt (a distinct
  witnessed kind is the distinction the audit asks; `R4_READ.md` 7b.4).
- **Request 2:** Partial moves half (at least 1); the rest is still owed and is read when read by
  `bills_due` (edit 4), not deposited by the effect (`loop/witness` is the one writer of claims, `04`
  §A.2).
- Failure moves nothing and emits `requisition.resisted`, which the place's people hold as a deed of the
  collector's. Every band is recoverable: he may collect again, send force, or remit.
- Withdrawn from this edit's earlier text (this file's first `Reconciled:` line): the hunger band as
  `stakes`, the `copying` skill row, the `altonian_civics` step, and `procedure_draws`.

## Gate (execution artifacts)

1. *Nothing moves at build.* `build_realm(0)`'s `content_hash` is proposal A's (this file adds no
   Tenure, Record or claim at build); the four built oaths still read `term None`.
2. *The draw.* 400 seeds, a hand-placed `requisition` of half a place's stores by a collector the
   place regards at zero: all four bands occur; conservation holds in every seed (the two rungs' sum is
   unchanged); with `task_draw_arm: off` the full amount moves in every seed.
3. *The court.* The `roga` scenario of proposal F under the auto chooser, seeds 0 to 19, eight
   seasons: `term.renewed` and `term.matured` on sworn oaths both non-zero across the seeds, and the
   per-seed pair reported; `requisition` by band reported. Control: the same seeds with
   `oblige_term: None` (H-159's control arm), in which no oath carries a term and `bills_due` stamps
   nothing.
4. *The bill is read, not written.* After a season in which a bill fell due, no claim of predicate
   `shortfall:*` names the paying seat's rung as written by MATTER; `bills_due` returns the stamp.

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
revolt. Completeness: an empty treasury lapses terms and raises no error. S: the shortfall claim, the
`transfer`, the `Rung.stores` conservation and the obstacle form are each the existing owner's. E,
against that: one key, two Queries (one a stamp) and one row's terms and two requests.

## Cost class

Small build. Movers: any run in which a `requisition` resolves, a bill is deposited, or a sworn
dignity-holder is paid. The build hash does not move.
