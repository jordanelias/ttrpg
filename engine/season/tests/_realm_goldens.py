"""The realm goldens: one literal per (seed, seasons, arm). Every hash test imports from here.
A re-record is one edit to this file, in the commit that moves the world, with the mover named in
that commit's message (CLAUDE.md §7).

An item that moves the realm proves in its own commit that its revert reads the previous pin, and
records that in the commit message; the proof is not kept as a test.

Read with `build_realm(s)` and `populated.run(k, s, w=w)` at `PYTHONHASHSEED=0`, seeds 0, 1, 2, one and
two seasons, on the tree of B05.64 (`e075e511b`), RE-PINNED ONCE at B05.99 and ONCE at B14.99 (the B14
movers: `prevailed` B14.02, `fell_to` B14.03, the scene's shape B14.15, the hand B14.16; the believed price
B14.24 and the drawn mark B14.23 read equal at one season; the build hash did not move). The movers since B04.99,
each a declared B05 item, each segment between two of them read equal at seeds 0, 1, 2: the one sampler
(B05.02), the skill score without the attribute (B05.09), the averaged governing score (B05.25), the
opposition is the opponent's score (B05.11), the one obstacle form (B05.14), `Event.ending` carries the
margin tuple (B05.18), `Office.modifier` (B05.20, by encoding: the build hash too), the calibrated arm
(B05.23, the bench seats' `modifier: minor`: the build hash too), the `wounds` row in every roll's
`levels` (B05.60), the believed prior (B05.62), one spacing of remove (B05.64). Earlier: B03 by
encoding (`Office.body_function`, B03.28), B04 by encoding (`Claim.lap`, B04.01; `Person.traits`,
B04.07). RE-PINNED ONCE MORE AT B06.99 (every value below): the uniform's source changes from CPython's
generator to the keyed mix (B06.04, A-30), a stream change and not a balance change (seed 0, one season,
read equal at B06.04, B06.05 and B06.06: `7ccf4abe89d508d4221e0a0c7cbcbfaf`). RE-PINNED A SECOND TIME AT THE
B06/B14 MERGE (every value below except BUILD): B14's combat record (the scene's shape, the hand, `prevailed`,
`fell_to`) had been pinned against the old stream, so the merged tree reads a third value (seed 0, one season:
`7ccf4abe89d508d4221e0a0c7cbcbfaf` -> `10934f0f516cad26f9c85625268d971e`; the build hash did not move; each
reading equal under `PYTHONHASHSEED` 0 and 1). RE-PINNED A THIRD TIME AT B07.99 (every value below except BUILD): the task draw ships on (B07.05), a refused task act carries no band (B07.10) and `reconstruct` reads the inquiries' `routine` level (B07.11); seed 0, one season: `10934f0f516cad26f9c85625268d971e` -> `88224913106d91e81ed815cd6114497c` (arm on; with `task_draw_arm` swept off the world reads the previous pins, gate 2), read at `PYTHONHASHSEED=0` and equal under `1` at seed 0. The shipped world, `DEFAULT_FIXTURES` as they stand, with no revert applied. A test support
module beside `_scar_helpers.py`, not a registry: nothing but tests reads it.

THE B07 CLOSE'S ONE FURTHER MOVER (B07.02's `_reached`, found by the close's CORRECTNESS pass): a `move` or `migrate` drawn Partial seated its
mover at the rung one leg short of `dest`, and every settlement sits directly in a territory, which is arrival-only; `_reached` now reads
`_arrival_only` at that rung too. Seeds 0 and 1 moved (one season `88224913..` -> `c5cbd61a..`, `a7b49d60..` -> `ef37fc05..`; two seasons
`f39e02de..` -> `5b2b3c93..`, `33bf9f9b..` -> `94a4896b..`), seed 2 read equal at both spans, the arm `off` is unmoved (`ARM_OFF_PINS`).

RE-PINNED AT B09.99 and read again after the `scar.taken` id was minted as the fold mints it (`f0821359c`; it moves the hash, not the census) (every value below except BUILD, which read `d691552f..` unmoved): the batch's movers, each declared at its item and
read once here on the closing tree (`PYTHONHASHSEED=0`; seed 0 one season also equal under `1`): fewer Events (B09.01), a filled
`Receipt.delta` and `scar.taken` Events (B09.10, B09.11), the opening Event in `causes` (B09.12), the shipped `refusal_memory` and
`weigh_confidence` (B09.05, B09.08), the re-pointed belief readers (B09.07), no zero-wear `condition.worn` (B09.21: seed 0, two seasons,
644 -> 148 of that kind, log 27040 -> 26228), a seat's closing names its holder (B09.22). The B07.99 values these replace are in `git log`.

RE-PINNED AT B10.99 (every value below, BUILD too): encoding (`Person.manner_offset`, B10.58: the build hash moves, the acts and
Events read identical) and behaviour (B10.60 cohorts take no individual acts, B10.65 the seeded `self:` claims, B10.72 a want can be laid
down, with its `release` no longer forming on a faction membership: `4aac919e3`; B10.73 ARC-47's stage row); B10.59, B10.66, B10.70 and B10.71
measured equal at the shipped data and the first half moved nothing.
Read once on the closing tree (`PYTHONHASHSEED=0`); seed 0, one season, each mover in order: `6e3a066a..` -> `5f2b9826..` (B10.58) ->
`576272fd..` (B10.60) -> `39d7c1bc..` (B10.65) -> `3ed14dad..` (B10.72, before the release fix) -> `faf327b7..` (B10.73, before the release
fix) -> `c8e57653..` (B10.72's release fix, on the closing tree). The B09.99 values these replace are in `git log`.

RE-PINNED AT BA1.99 (every value below, BUILD too), ONCE for the batch BA1-cast-content, a SECOND time after BA1.02's ten `manner:` rows were held back (`8d32955b1`: they moved R-06.d's strict-top share to exactly one half). The movers are BA1.01 (the cast's `stats:` and `capabilities:`), BA1.08 (the six `relations:` rows) and BA1.12 (the two `unaware:` marks, which remove seeded `self:` claims); BA1.03, BA1.04, BA1.06 and BA1.09 read equal to their predecessors. Seed 0, one season, each on its own tree (`PYTHONHASHSEED=0`), hash (BUILD) acts/log: `c21e451f1` (the B10.99 tree) `c8e57653..` (`4c6a3a99..`) 563/12966 -> BA1.01 `f5ed8eba..` (`a621787d..`) 563/13238 -> BA1.08 `08466028..` (`17094d3d..`) 570/13315 -> BA1.12 `e279b27a..` (`f8f4cb23..`) 570/13315, the census digest moved = the closing tree. BA1.02's ten `manner:` rows are held back (the IS-A-11 draft's table (a) `manner:` column keeps them) and these pins exclude them; the BA1.08 and BA1.12 readings are the closing tree with the later mover's rows taken out, since the item commits carry the manner rows. Seeds 1 and 2 and the two-season spans were read on the closing tree only. The previous pins (recorded with the manner rows in) are in `git log`.

RE-PINNED AT B15.99 (main, after BA1.99; every `SHIPPED` and `CENSUS` value; BUILD unmoved): the fight's calibration (B15). Its readings are in `git log`.

RE-PINNED AT B24p.99 (every `SHIPPED` and `CENSUS` value; BUILD read `4c6a3a99..` unmoved at seed 0, on the B24p tree before the merge): the batch's movers, each declared at its item: the five influence
verbs `argue`, `lie`, `speak`, `tell` and `interrogate` rest on the proceeding entry (B24p.19), each hearer is moved for himself (B24p.20), what the beats
show is deposited with those who saw it (B24p.22), the six roles (B24p.23); the docket item's `arranger` and `rig` (B24p.24) move the realm's hash by their encoding, the item's two keys. Read once on the
closing tree (`PYTHONHASHSEED=0`, twice equal, the six readings); seed 0, one season, each mover in order: `c8e57653..` (batch open) -> `ae2019b6..` (B24p.19) ->
`4b7d0ca5..` (B24p.24) -> `aae24e2a..` (B24p.20) -> `ce07cfb4..` (B24p.22) -> `a0000b5e..` (B24p.23, the closing tree). The B10.99 values these replace are in `git log`.

RE-PINNED AT THE B24p.99 CLOSE (the six `SHIPPED` hashes; `BUILD` and every `CENSUS` value, acts, log and digest, read unmoved on the B24p tree): the close's fixes to the proceeding. `heard` is
read against the man opposite again (`lead(inp, other side)`, as `esteem` is), not against the one addressed in an abridged act: that is the one that moves the realm (seed 0, one
season, reverted alone it reads `a0000b5e..`; each of the others reverted alone, one at a time, leaves the new hash, so they are inert at that reading). The rest: an abridged
close reads the addressed man's own `Margin`, not the last hearer's; `believes` and `false_items` read claims at the world's tick and only truth-valued ones; the chooser's
believed path filters claimants to persons and raises the fold's data defects; `View.odds` signs the mood toward `for`; `odds_of` is `None` for a verb that proceeds. Read
once on the closing tree (`PYTHONHASHSEED=0`, twice equal); seed 0, one season: `a0000b5e..` -> `acdee97d..`.

RE-PINNED AT THE B24p MERGE WITH MAIN (BA1.99 and B15.99 landed on main while B24p was open; every `SHIPPED` and `CENSUS` value, BUILD unmoved: `f8f4cb23..`, main's, at seed 0): the merged realm is a third state. Seed 0, one season,
read twice equal at `PYTHONHASHSEED=0`: main `4aab36db..` (B15.99) and the B24p tree `acdee97d..` -> `1e3cd6db..`.

RE-PINNED AT B21.99 (every value below, BUILD too), ONCE for the batch B21-fa-governance (57 commits since `c21e451`, 144 files; `git diff --stat c21e451..a390628` reaches `engine/season/loop`, `queries`, `state`, `data`, `decision`, `boot/realm.py`, `offices.yaml`, `rosters.yaml` and `verb_table.yaml`, which every pin below reads). The movers are the batch's declared behaviour movers (B21.51 to B21.57, B21.63, B21.65, B21.66, B21.69, B21.73, B21.79, B21.80 to B21.83) and the first half's (B21.02 to B21.23). Seed 0, one season, hash (BUILD) acts/log: `c8e57653..` (`4c6a3a99..`) 563/12966 at `c21e451` (the B10.99 tree, before the batch) -> `e279b27a..` (`f8f4cb23..`) 570/13315 at the BA1.99 pin (`ce61cbf`) -> `fbc82e79..` (`7eb6293a..`) 425/9290 at `a390628` (the closing tree). Seeds 1 and 2 and the two-season spans were read on the closing tree. The BA1.99 values these replace are in `git log`.

RE-PINNED AT THE B24p MERGE WITH B21 (B21-fa-governance landed on main while B24p was open; every `SHIPPED` and `CENSUS` value, BUILD unmoved: `7eb6293a..` at seed 0): the merged realm is a fourth state. Seed 0, one
season, read twice equal at `PYTHONHASHSEED=0`: main `fbc82e79..` (B21.99) and the B24p tree `1e3cd6db..` -> `38044624..`. The B24p tree's shipped values are in `git log`.

RE-PINNED AT THE B11 MERGE WITH MAIN (B24p and B21 landed on main while B11-fi-readers was open; every value below, BUILD too: B11's encoding movers B11.08, B11.17 and B11.74 move the build hash, `7eb6293a..` -> `08a3ac1534672c8c4f1f0576a11dc1e7` at seed 0): the merged realm is a fifth state, read twice equal at `PYTHONHASHSEED=0` on the merged tree: main `380446248fd513..` (B24p merge with B21, seed 0, one season), the B11 tree `793f29fd..` (this branch before the merge) and the merged tree `94dc5293c35bb143d905e35098a0319d` (acts 392, log 9320). The merge also needed `rosters.yaml: seat_founding_kinds`: B11.08's ledger-sourced vacancy left a seat nobody has held unnamed, so B21's founded office was never offered to the man who founded it; it now reads as vacant from its founding. The B11.99 values are in `git log`.

RE-PINNED AT B08.99 (every `SHIPPED` and `CENSUS` value; BUILD read `08a3ac15..` unmoved, as at the S13 base `8142371`), ONCE for the batch B08-scene-order. The movers are B08.03 (a scene is folded in its own order) and B08.04 (the chooser sets `after` from the row, so a skipped second interaction logs a refusal at clause `sequence`); B08.05 (the precedence draw) reads equal here, since no rivalry group forms at seeds 0, 1, 2 in two seasons; B08.01, B08.02 and B08.06 are EQUAL. Seed 0, one season (`PYTHONHASHSEED=0`), hash acts/log: `94dc5293..` 392/9320 (`reading @8142371`, the S13 base) -> `0f7f42a3..` (B08.03, that item's reading) -> `6a394d86..` 377/7804 (B08.04, which B08.05 and B08.06 leave; `reading @ce09a54`). Seeds 1 and 2 and the two-season spans were read on `ce09a54` and on `8142371`. The B11 merge values these replace are in `git log`.

RE-PINNED A SECOND TIME AT B08.99 (every `SHIPPED` and `CENSUS` value; BUILD unmoved), after the batch's close applied an antagonist's ruling (`44cdf60`): `decision/choose.py::hangs_on` also requires the same counterparty, so an `argue` to one hearer no longer hangs on an `argue` to another. That removes every hang in the realm over two seasons at seed 0 (acts with `after` set 238 -> 0, skipped at clause `sequence` 230 -> 0): the realm reads B08.03's value again at seed 0, one season (`0f7f42a3..`, which c32da4e's body records for B08.03), and no longer carries the B08.04 values above. Seed 0, one season (`PYTHONHASHSEED=0`): `6a394d86..` 377/7804 (`reading @c32da4e`) -> `0f7f42a3..` 392/9319 (`reading @000d177` plus this edit). The values above are in `git log`.

RE-PINNED AT B12a.99 (every value below, BUILD too), ONCE for the batch B12a-world-motion-and-ground (37 commits since the open commit `8142371d0`, the B11-fi-readers close: B08-scene-order merged to main while this batch was open, so the values below are read on the MERGED tree (`ce20d65e0`: this batch on B08's main) and the pre-B08 chain here is the batch's alone). The movers that moved the shipped realm are three, each read on its own tree at `PYTHONHASHSEED=0`: B12a.15 (a `move` to where the mover stands is refused, H-140), B12a.54 (`endowment_mode` `uniform` -> `ground`: the Site set and the starting stores) and B12a.55 (`granary_seasons` 0 -> 4: the treasuries' starting stores). Seed 0, hash build / one season / two seasons: `08a3ac15..` / `94dc5293..` / `ba502b30..` (open) -> `08a3ac15..` / `6671e3c6..` / `a5182a4e..` (B12a.15) -> `a241435e..` / `3c86e3a6..` / `09f8202f..` (B12a.54) -> `ba0ecd0e..` / `6a39e62c..` / `404a6137..` (B12a.55, and the closing tree: B12a.56 to B12a.99 read equal at the shipped realm). Seed 1 one season `f2b715d1..` -> `3557c4c7..` (.15) -> `24b33bce..` (.54) -> `b0473a33..` (.55, the closing tree), two seasons `6703a00f..` -> `9f6cb705..` -> `e8c0be9b..` -> `adc54867..`; seed 2 one season `c30707ca..` -> `df0e620a..` -> `8d6dba9a..` -> `1dc0d1c7..`, two seasons `2b121693..` -> `6492bbf1..` -> `d905acea..` -> `65fd9e7e..`; the build hash reads `ba0ecd0e..` / `a8ebd0f1..` / `c9a8221e..` at seeds 0 to 2 (it moves at .54 and .55 only). Declared movers that read INERT at the shipped realm (hash equal, seeds 0 to 2 or 0 to 3, their commit bodies say why): B12a.05, .06, .08, .14, .56, .62, .66, .69; B12a.03 built nothing. The values these replace are in `git log`. The merged-tree values (B08 and this batch together), read once at `PYTHONHASHSEED=0`, seed 0: build `ba0ecd0e..` (B08 does not move it), one season `56d183c1..` (the batch-only tree read `6a39e62c..`), two seasons `a2e6baef..`; the six `SHIPPED` and `CENSUS` values are those.
"""

BUILD = {0: "ba0ecd0e8b11b259792818a689583771"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "56d183c1a015d47da9a6690e254f7008",
           (0, 2): "a2e6baef1a017bddcefd9d06d0bd8196",
           (1, 1): "dd2d323ef9349821f6d60bbb39c6b7a0",
           (1, 2): "bae6f6db5493a9e4634d2c180d875f7f",
           (2, 1): "c65ea69b28c0792c96e2e1eed0f219a8",
           (2, 2): "61066f356ac3142d43d7e87066f06680"}    # B12a.99 re-record (the docstring); the earlier values are in `git log`

#: What the run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    (0, 1): dict(acts=408, log=8660,
                 census="c0afbe6f8ff255cd1c8f76c025e8d1b34c9393140d0226ea62f4302e8f5a7b61"),
    (0, 2): dict(acts=867, log=19248,
                 census="8aa31eb17351276299b21e63ce7960d06414ec9529ef977ffd5a8486a4107b22"),
    (1, 1): dict(acts=435, log=8647,
                 census="8fdd4526b3328b8a240885db672a98ad00e95ffbd272aac4c951aeb1f3ca5421"),
    (1, 2): dict(acts=931, log=21820,
                 census="ffb4242f934d92e055c0fc54b477d18252e69e01bae25aeab63323d002f809e4"),
    (2, 1): dict(acts=418, log=9297,
                 census="4e06cdcd855f996dde49659c1c60efb10ddfaf11ab30c1f46bce28a9c6e343e2"),
    (2, 2): dict(acts=912, log=20919,
                 census="9fd50c6f1022560797a15bfa149fd1edd2eeeda2e3fdbd7c73f89cd3779b6275"),
}
