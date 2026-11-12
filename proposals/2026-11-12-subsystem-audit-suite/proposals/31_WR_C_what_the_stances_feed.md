# WR-31-C — what the stances feed: the founding deeds and the race for the crown, the vote, the strands, the chronicle and the player's view of regimes

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §1 found it CONFORMS and R3 §2 found no ruling it contradicts. Added: batch and dependencies (U3 B38; commit 1 rides the institutions batches); `U5d_FA_owed_edits.md` §4's weight is now authored as `rosters.yaml: tables.territory_weight` (U1 ledger F-12), which `block_lean` reads through `faction_q.weight`; U3 §6.3 (no goal row carries `axis:`; commit 2 ships at its control until rows are authored); commit 3's storybar edit is placed in C3-K7's serial order after `31_WR_B` commit 3 `[ASSUMPTION: C3-K7 does not list this file; it edits `harness/storybar.py`, so it is placed last — basis: C3-K7's rule that no two proposals edit the file concurrently]`. Tier already named.

## Status: PROPOSED (four small edits, each a request to the file that owns its site; the ten phrase pairs are `[ASSUMPTION; Jordan to correct]`)

Lands in batch: B38 (narrative and regimes), after `31_WR_B` and before `30_WR_A` (U3 §1 item 38); commit 1's step rows land with `15_INSTITUTIONS_BYZANTINE_E` and `15_INSTITUTIONS_VENICE_C` in their batches (B32/B40).
Depends on: `31_WR_A` (B38); `20_NARRATIVE_D` (B38); `U5d_FA_owed_edits.md` §4 (B21); `15_INSTITUTIONS_SYNTHESIS_B` (B32); `30_GO_F` (B38).

Source: A-17 to A-19 (the founding order and the deed race), A-41, A-42 (vote blocks), A-45 (strands), A-82 ("visible to the player as factions of opinion, not as numbers"), A-87 to A-90. `audits/31_HOUSE_STANCES_AND_CAST_VALUES.md` §5, §10. Reference only (`CLAUDE.md` §0.05). Lane WR with FA and GO.

Composes on `31_WR_A` (rows, cores, `creed:` signs, links, `closeness`, `core_standing`), `31_WR_B` (sway), `20_NARRATIVE_D` (`engaged_poles`, `opinion_of`), `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md`, `22_HAPPENINGS_B_the_throne_is_never_stranded.md`, `15_INSTITUTIONS_BYZANTINE_E_accession_recall_and_the_crowd.md`, `15_INSTITUTIONS_VENICE_C_roll_lot_ballot.md`, `U5d_FA_owed_edits.md` §4, `30_WR_C_strands_open_grow_join_conclude.md`, `09_WR_B_chronicle_that_tells.md`, `30_GO_F_the_plot_as_the_player_is_shown_it.md`.

## What it changes in `engine/season/` at runtime

| commit | change | hash |
|---|---|---|
| 1 | one term in the voter's draw (an acclamation, a ballot): his opinion of the claimant's or proposer's side | EQUAL until a ballot or accession exists (none is built); then inside those proposals' declared movers |
| 2 | `thrust_axes.bears` (data): which poles a matter's thrust speaks to; the ballot reads it | EQUAL (no reader in the loop until the ballot) |
| 3 | `world_q.strand_fault` and `world_q.block_lean` (readings); `storybar` prints them | EQUAL |
| 4 | `affiliation_roster.phrases` (ten pairs); the chronicle and the player surface read them | EQUAL (text; `descriptors.json` re-derived, declared) |

## 1. The founding deeds and the race for the crown (A-17 to A-19)

**What already carries it, once `31_WR_A` lands.** The deed ledger seeds the three founders' deeds at three confidences by the founding order (A-18), and the crown, when the line fails, goes by a race among the heir, the consort, the Princess and the heads of Hafenmark and Varfell, with odds from what others believe of each claimant's deeds (A-19). Two existing channels then read the stances with no new code: (a) every retelling of a deed is credited by `loop/witness.py::_credit`, which is +1 inside a regime and −1 across a `true` pair, and on the built realm that sign now separates the houses (Hafenmark against Varfell −1.0, Hafenmark with the Church +0.71, Varfell with the Movement +0.5; audit §5, P-31-2), so Varfell's deed is held firmly where the Revival runs and discounted among the devout; (b) `world_q.opinion_of` (`:3029`) gives each person an opinion of each side from how his own stands sit with that side's public creed (`20_NARRATIVE_D` edit 2 with `31_WR_A` commit 4).

**The one edit (commit 1).** The voter's draw in an accession or a ballot has no term for what he thinks of the side asking. Added, as one row in each owner's table of steps: *"his opinion of the claimant's side (`world_q.opinion_of(w, voter, faction_of(claimant))`, handed down resolver-side as one value) is above indifference: one step for; below it: one step against; a claimant of no side: none."* It is a step in a drawn roll, never a count of supporters. Owners: `15_INSTITUTIONS_BYZANTINE_E` edit 1's `favourable` table (the acclamation), `15_INSTITUTIONS_VENICE_C` edit 5 (each ballot's roll).

**What the data then says about the race** (a reading of `31_WR_A`'s table, audit P-31-6; it predicts odds, not an outcome):

| claimant | nearest cores (`closeness`) | so his road runs |
|---|---|---|
| Torben, the heir | every new cell at the middle (canon leaves him to emerge) | through the wide Valorsmark tent (18 near it), on title and his father's deeds; he offends nobody and moves nobody |
| Lenneth, the consort | Revival 0.87, Movement 0.73, her own house 0.23, the Church −0.60 | through the Revival's ten and against the Church's twelve; pulled apart on caste and Crown (link fit −1.0) |
| Baralta | the Church 0.80, Hafenmark 0.77 | through the devout, who are the Church's own, while her house's goal row is to suppress the Church's influence (`goals.yaml: goal_hafenmark_church_influence_suppressed`) |
| Vaynard | Revival 0.87, Movement 0.73, Varfell 0.69 | through the same ten as the Queen: two claimants for one regime, and the third founding deed as his head start |
| Elske | Valorsmark, with an Altonian lean | on title, from abroad |

The founding order stays a head start (the seeded confidences); the stances decide who will hear a deed told and credit it.

## 2. The vote (A-41, A-42)

`U5d_FA_owed_edits.md` §4 gives a faction and a territory a political weight that a ballot's draw reads (authored as `rosters.yaml: tables.territory_weight`, keyed by territory id; U1 ledger F-12). Two additions:

- **`thrust_axes.bears`** (commit 2, `engine/season/rosters.yaml: thrust_axes`): which poles a matter on that line speaks to, sign included. `revive_einhir: {einhir_restoration: 1, einhir_folk: 1}`, `suppress_einhir_revival: {einhir_restoration: -1, einhir_folk: -1}`, `overthrow_caste: {caste_order: -1}`, `uphold_caste: {caste_order: 1}`, `uphold_church: {solmund_orthodoxy: 1}`, `overthrow_church: {solmund_orthodoxy: -1}`, `altonian_ascendancy: {altonian_civics: 1}`, `purge_altonia: {altonian_civics: -1}`. The other six axes bear on none. Each a plain reading of the axis's own name; `[ASSUMPTION; medium; Jordan to correct]`.
- **The ballot's roll** (`15_INSTITUTIONS_VENICE_C` edit 5) gains one more step row: *"the matter's goal row names an `axis:` that bears on a pole: the voter's own `conviction_stand` on that pole, times the sign, above 0: one step for; below 0: one step against."* A voter with no key on the pole takes no step, so the Church's men are unmoved by a caste measure (A-88) and decide it on other terms.
- **`world_q.block_lean(w, voters, pole) -> float`** (commit 3): the mean `conviction_stand` of a body's voters on a pole, each weighted by `faction_q.weight`'s per-person weight. A reading, for the harness and the player: "the Jarl Council leans hard against the order of birth". It predicts a ballot and decides none.

So caste is expressed as A-41 asks, in three places that now differ: regard by believed descent (the Einhir concern, two poles), the weight of a block (U5d-FA), and the tiers (U5d-SE), with `caste_order` the opinion each voter brings to a measure about them.

## 3. The strands (A-45)

`world_q.strand_fault(w, strand) -> tuple` (commit 3): the poles on which the strand's two sides (`side_against`) have mean stands of opposite sign, largest gap first; `()` when none or when a side has no living party. A reading beside `incompatible_span`: that one says whether a fault runs through the strand, this one says which. `storybar --strands` prints `over <pole>[, <pole>]`. On the built realm the standing quarrel of the Church with the Movement (`goal_church_suppress_restoration` against `goal_restoration_evade_capture`) reads over both Einhir poles, and one between Hafenmark's and Varfell's people over the caste and the form of rule `[expected from the house means, audit P-31-1; not run on a strand, since the strand readings need a played season]`. Each move of such a strand is a deed taken in by onlookers, which is `31_WR_B`'s occasion: strife feeds the drift, and the drift changes who is on which side of the next strand.

## 4. The chronicle and the player's view

- **`affiliation_roster.phrases`** (commit 4, `references/descriptor_registry.yaml`): per pole, the words for standing for it and against it, read by `harness/chronicle.py` (the line for `conviction.moved`: "<name> came to hold with the old ways", with `on_account_of` rendered through the claim it names) and by the surface. Proposed: `caste_order: ["holds with the order of birth", "would see the order of birth ended"]`; `royal_order: ["holds with the Crown's order", "is no friend of the Crown's order"]`; `parliamentary_rule: ["would have the realm ruled in assembly", "has no use for assemblies"]`; `militarism: ["would have the sword decide", "would keep the sword out of rule"]`; `einhir_folk: ["stands with the Einhir", "stands against the Einhir"]`; `einhir_restoration: ["holds with the old ways", "holds the old ways a heresy"]`; `solmund_orthodoxy: ["is of the faith", "is no son of the Church"]`; `inner_tradition: ["keeps the inner tradition", "rejects the inner tradition"]`; `thread_truth: ["holds the Thread to be true", "holds the Thread a fable"]`; `altonian_civics: ["would have the empire's order", "wants none of the empire"]`. A link prints as "on account of": "is no friend of the Crown's order, on account of the order of birth".
- **The player sees regimes as factions of opinion** (`30_GO_F`), under the rule that no one reads another's convictions: (1) his own stands, as bands (`player_sees: bands`), and where a link pulls him apart, both phrases together (A-34); (2) the realm's cores by name with their public creed in phrases (the `creed:` rows are what a side is known for; the six names are `regime_cores`' keys); (3) of another person, only what his ledger holds: that person's side's creed, any `conviction.moved` he saw or was told, and the deeds from which he may judge; never a number, never the other's sheet; (4) which cores he himself is near, in words ("you stand close to the Revival, and apart from your house"), from `closeness` on his own stands; (5) the expectation of his circle (`30_WR_G` commit 5).

## Instructions to code

Tier: second (sonnet) throughout; no judgment node.

**Commit 1.** No code in this tree until an accession or ballot is built. The step row of §1 is added to `15_INSTITUTIONS_BYZANTINE_E` edit 1 and `15_INSTITUTIONS_VENICE_C` edit 5 by their implementing batch; its test, in the file that batch creates for the draw: `test_a_voter_s_opinion_of_the_claimant_s_side_is_one_step_and_no_more`, `test_a_claimant_of_no_side_gains_no_step`.

**Commit 2.** `engine/season/rosters.yaml: thrust_axes`: the `bears:` mapping of §2 beside `opposes:`; `engine/season/data/goals.py` (the one loader of the axes) refuses a `bears` key that is no `values:` member, a pole that is not rostered and a sign outside −1 and 1, and exposes `THRUST_BEARS`. `[UNVERIFIED: no goal row carries an `axis:` today (all 38 printed `None` in this lane's read); the commit's first step is `grep -rn "\.axis\b\|\"axis\"" engine/season --include=*.py` to list what reads one before any row gains it.]` No goal row gains an `axis:` here. Test, in the file covering `data/goals.py`: `test_bears_refuses_an_unrostered_pole`.

**Commit 3.** `engine/season/queries/world_q.py`, after `incompatible_span` (`:5350`): `strand_fault(w, strand)` and `block_lean(w, voters, pole)` as §2 and §3 give them; `harness/storybar.py --strands` and `--regimes` print them. Tests, `engine/season/tests/test_strife_credit.py`: `test_strand_fault_names_the_pole_two_planted_sides_differ_on`, `test_strand_fault_is_empty_when_a_side_has_no_living_party`, `test_block_lean_of_voters_with_no_key_is_zero`, `test_the_two_readings_move_no_hash`.

**Commit 4.** `references/descriptor_registry.yaml: affiliation_roster.phrases` (refused by `tools/export_descriptors.py` unless every `names:` member has exactly two non-empty strings); re-export and `--check`; `engine/substrate/descriptors.py` exposes `AFFILIATION_PHRASES`; `harness/chronicle.py` renders `conviction.moved` through it. The surface's rows are `30_GO_F`'s. Test, `engine/season/tests/test_storybar.py::test_a_conviction_moved_reads_as_words_and_never_a_number`.

## The gate (execution artifacts)

```sh
python tools/export_descriptors.py --check
PYTHONHASHSEED=0 python -m engine.season.harness.storybar --base-seed 0 --n 3 --seasons 2 --arms off off --regimes --strands
python -m pytest engine/season/tests/test_strife_credit.py engine/season/tests/test_storybar.py -q   # at the close, once
```

Expected: every hash EQUAL; at least one strand at two seeds of three prints a non-empty `over`; `block_lean` on `caste_order` orders the Jarl Council's members below the Inner Council's of Hafenmark; no printed line of the chronicle or the regimes block shows a conviction as a number where `phrases` covers it. Control: the realm before `31_WR_A` commit 2, where `strand_fault` can name only the five shipped poles and `block_lean` on `caste_order` is 0 for every body.

## The falsifier, and its control

- A ballot or acclamation decided by the opinion term alone at every seed (the same side winning ten of ten with the term on and a split with it off): the step is too large; it is one step.
- `strand_fault` non-empty for a strand whose parties all hold the same stands: it is reading the wrong sides.
- A surface row showing another person's stand that the player's character holds no claim for: AX-7 broken.
- Any hash moving.

## Dependencies

`31_WR_A`. `20_NARRATIVE_D` edit 2. The institutions kit for commit 1 (A-13, A-14). `U5d_FA_owed_edits.md` §4 for the weights. `30_WR_C` commit 1 and `09_WR_strand_conclusion.md` for strands; `30_GO_F` for the surface.

## Layer 1

AX-7: the voter's term is his own opinion of a side's public creed; the surface shows what his ledger holds. `04` §A.2: two readings in `queries/`, data in `rosters.yaml` and the descriptor registry. The standing rule: a vote is a draw on the voter (A-14); this adds steps to it. **STRUCTURAL**.

## NERS reading

- **N.** Without these the stances are held and never asked: no vote hears them, no strand is named by them, no player sees them. Holds across scales (one voter's step, a block's lean, a realm's race).
- **R.** Two claimants for one regime; a duchess courting the Church's own; a council whose lean can be read before it sits. Complete: a man with no key takes no step.
- **S.** `opinion_of`, `conviction_stand` and the one roll, reused; no second vote arithmetic.
- **E, last.** Two step rows, two readings and twenty phrases. High.

## Cost class

Edit (1, in its owner's batch). Edit (2). Small build (3). Edit (4).
