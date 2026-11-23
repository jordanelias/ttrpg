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

RE-PINNED AT BA1.99 (every value below, BUILD too), ONCE for the batch BA1-cast-content: the cast's content, each mover declared at its item and
read once here, each tree on its own commit (`PYTHONHASHSEED=0`); seed 0, one season, each mover in order, the build hash beside it:
`c8e57653..` (BUILD `4c6a3a99..`, the B10.99 tree `c21e451f1`) -> `f5ed8eba..` (BA1.01, the cast's `stats:` and `capabilities:`, BUILD
`a621787d..`; acts 563, log 13238) -> `ca5372e7..` (BA1.02, the `manner:` offsets, BUILD `c1929e93..`; acts 563, log 12840); BA1.03, BA1.04 and
BA1.06 read equal to it (hash, acts, log, census, BUILD) -> `d5026773..` (BA1.08, the six `relations:` rows, BUILD `c87a1888..`; acts 570, log
12917); BA1.09 read equal to it -> `6b35fd7d..` (BA1.12, the two `unaware:` marks, which remove seeded `self:` claims, BUILD `e7085d8c..`; acts and
log unmoved, the census digest moved) = the closing tree. The B10.99 values these replace are in `git log`. One re-pin, for the batch; seeds 1 and 2
and the two-season spans were read on the closing tree only.
"""

BUILD = {0: "e7085d8c8a9f1258fea926f4f92fa0a6"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "6b35fd7dc0d3fe320a383c99926988b1",
           (1, 1): "eeb4bc2e4f9e44c494daa21510205f50",
           (2, 1): "4a21cda39ab60a48c537488c78e58933",
           (0, 2): "e66b5058933a1f20e0269f1c5857a856",
           (1, 2): "b1eb3b80e18da91e6d6195c74591b5f1",
           (2, 2): "85d07a55cc6bd8e88eb0659a6053c5b4"}    # BA1.99 re-pin (the docstring); the B10.99 values are in `git log`

#: What the run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    (0, 1): dict(acts=570, log=12917,
                 census="5114ed0b882b987d5dfefd6d7890644139288617618abd37948c6db72f260454"),
    (1, 1): dict(acts=588, log=11651,
                 census="9101f2bd6778cde98897b14a21867c905f8d14002d933b01c14c390bb1c7a594"),
    (2, 1): dict(acts=565, log=12290,
                 census="4fa23ebe6415e2847784fa33d04c58fbdb8ee4ee8aa9c54a9567f3a6c332aad8"),
    (0, 2): dict(acts=1223, log=26980,
                 census="4829a74292988ad88e4ed1dac71ffae578ab87600c5e5f16373b583989128363"),
    (1, 2): dict(acts=1218, log=26296,
                 census="afc64140a4a429a5224a51e72f39c53facb918841e9b8fb588730a1c7e104fc4"),
    (2, 2): dict(acts=1214, log=29706,
                 census="4844ae524815d556506e80659a4a3e917ed2bfdf2a8c84be5ebc1962904642fa"),
}
