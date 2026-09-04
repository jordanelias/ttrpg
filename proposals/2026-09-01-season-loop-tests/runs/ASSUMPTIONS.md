# THE INSTRUMENT'S OWN ASSUMPTIONS — what it had to supply to run at all

**§42.2.1's inject-declare-name pattern, applied to SCHEMA ROWS rather than to
numbers.** Without these the loop cannot complete one season, so refusing them would
mean measuring nothing; asserting them silently would be the invention §42.3 names.

**0 of 0 declared assumptions were actually
exercised by this run.**

> **ZERO IS A MEASUREMENT HERE, NOT AN ABSENCE.** The instrument assumed three
> schema rows until `W2` made Part D data: §D2's `DR-3` states all three, so
> nothing is left to assume. The channel that would record one
> (`shape.assume_partition_row`) is deliberately **kept live** — an empty dict
> that no code path can populate would make this count satisfiable by deletion,
> which is `CLAUDE.md` §0.1 point 2. If any future run has to assume a row, it
> appears in the table below.

| row | social | why | exercised |
|---|---|---|---|

## Harness fixtures — every number this instrument used

| fixture | value | in chain? |
|---|---|---|
| `condition_scale` | `1000` | no — a harness fixture |
| `scene_budget` | `5` | no — a harness fixture |
| `ledger_cap` | `200` | no — a harness fixture |
| `view_k` | `12` | no — a harness fixture |
| `wear_per_season` | `{'harbour': 10, 'seam': 10, 'body': 10}` | no — a harness fixture |
| `confidence_default` | `100` | no — a harness fixture |
| `claim_decay_per_season` | `5` | no — a harness fixture |
| `fan_out_mode` | `total` | no — a harness fixture |
| `contest_max_depth` | `2` | no — a harness fixture |
| `entrenchment_seasons` | `60` | yes — §15.2 |
| `obstacle_refusal_multiple` | `2` | yes — §27.4 |
| `band_floors` | `{'harbour': {'bulk_shipping': 800, 'fishing': 100}, 'seam': {'deep_mining': 700, 'surface_gleaning': 50}, 'body': {'full_operations': 800, 'limited': 500, 'withdrawal_only': 100}}` | no — a harness fixture |
| `season_factor` | `1.0` | no — a harness fixture |
| `subsistence_weight` | `{'grain': 2, 'salt': 1}` | no — a harness fixture |
| `question_aggregation_rule` | `first` | no — a harness fixture |
| `interactions_per_scene` | `3` | no — a harness fixture |
| `extended_scene_cost` | `2` | no — a harness fixture |
| `scene_packing_rule` | `greedy` | no — a harness fixture |
| `claim_subject_rule` | `both` | no — a harness fixture |
| `record_stages_default` | `3` | no — a harness fixture |
| `record_stage_term` | `1` | no — a harness fixture |
| `budget_office_bonus` | `1` | no — a harness fixture |
| `budget_leg_penalty` | `1` | no — a harness fixture |
| `default_store_kind` | `grain` | no — a harness fixture |
| `default_transfer_amount` | `1` | no — a harness fixture |