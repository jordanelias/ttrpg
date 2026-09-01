# THE INSTRUMENT'S OWN ASSUMPTIONS — what it had to supply to run at all

**§42.2.1's inject-declare-name pattern, applied to SCHEMA ROWS rather than to
numbers.** Without these the loop cannot complete one season, so refusing them would
mean measuring nothing; asserting them silently would be the invention §42.3 names.

**3 of 3 declared assumptions were actually
exercised by this run.**

| row | social | why | exercised |
|---|---|---|---|
| `(Date, fired)` | False | ASSUMED: S24 has CALENDAR fire dates with no actor, so the writer is not an act. The matrix admits Date at CALENDAR and RESOLVE, which determines nothing. | yes |
| `(DocketItem, matter)` | False | ASSUMED: S24 says 'Dates come due. DOCKETS FORM.' with no actor, and S30's matrix marks DocketItem YES at CALENDAR -- so the design itself has an actorless writer. ⚠ REV 4 CORRECTION: rev 3 assumed True on the strength of S36.1's `carry` being an act, which made CALENDAR's own specified docket formation raise a FORBIDDEN CHARGED TO THE DESIGN. That was the instrument manufacturing a refusal and then reporting it as the shape's -- the worst available direction. The derivation rule two lines above (admitted at a step the world writes -> social:false) gives False, and this row now follows it. `carry`'s act-ness is a fact about WHO PUT THE MATTER THERE, not about whether the column admits an Event. | yes |
| `(Person, claim_ledger)` | False | ASSUMED: S28 puts the deposit at WITNESS, whose class is INTERIOR, and S20 makes `witness` the ONLY minter -- so the writer is an Event, not an act. The matrix determines nothing (WITNESS appears in no other row) and no S30 row states it. ⚠ THE CONSEQUENCE IS UNCOMFORTABLE AND IS NOT HIDDEN: under this assumption a person's own memory is a row THE WORLD MAY WRITE, which sits badly beside S22 giving the ledger to the Person and S9.3 making it the epistemic layer. | yes |

## Harness fixtures — every number this instrument used

| fixture | value | in chain? |
|---|---|---|
| `condition_scale` | `1000` | no — a harness fixture |
| `act_budget` | `5` | no — a harness fixture |
| `ledger_cap` | `200` | no — a harness fixture |
| `view_k` | `12` | no — a harness fixture |
| `wear_per_season` | `{'harbour': 10, 'seam': 10, 'body': 10}` | no — a harness fixture |
| `confidence_default` | `100` | no — a harness fixture |
| `entrenchment_seasons` | `60` | yes — §15.2 |
| `obstacle_refusal_multiple` | `2` | yes — §27.4 |
| `band_floors` | `{'harbour': {'bulk_shipping': 800, 'fishing': 100}, 'seam': {'deep_mining': 700, 'surface_gleaning': 50}, 'body': {'full_operations': 800, 'limited': 500, 'withdrawal_only': 100}}` | no — a harness fixture |