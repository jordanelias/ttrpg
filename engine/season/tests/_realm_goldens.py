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
"""

BUILD = {0: "f8f4cb234a523f56d6a912625cb3046f"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "4aab36db1767d39e1074cc7996678350",   # B15.99 re-record: e279b27a.. -> 4aab36db..
           (1, 1): "20fe61b8784c62f9f3146edef2b35ec8",   # B15.99 re-record: eae45bee.. -> 20fe61b8..
           (2, 1): "cc07d47191ad6f9aa997fbdb6d24dd98",   # B15.99 re-record: 40f92a88.. -> cc07d471..
           (0, 2): "e6466cf763c438ba8699db9e8ec659d0",   # B15.99 re-record: aea26494.. -> e6466cf7..
           (1, 2): "ab117da3abaaf3efd54519fffdf3de16",   # B15.99 re-record: 5d165eb4.. -> ab117da3..
           (2, 2): "810c688f94ea052a7d899d176c5ef5e8"}    # B15.99 re-record: 63065b27.. -> 810c688f.. (last row); the earlier values are in `git log`

#: What the run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    (0, 1): dict(acts=583, log=13525,   # B15.99 re-record: acts 570 -> 583, log 13315 -> 13525, census 8a58cd34.. -> 1f2426e6..
                 census="1f2426e61d00a5e6c625cddd0d262a47f48a7e1792872da54a9f143d9cb5df55"),
    (1, 1): dict(acts=593, log=11304,   # B15.99 re-record: acts 593 (equal), log 11681 -> 11304, census 76f43359.. -> 0439b04c..
                 census="0439b04cd5e6ccf849b51e4de1cddae34a19cb207b42b9e4c8c73e78879509ff"),
    (2, 1): dict(acts=561, log=12097,   # B15.99 re-record: acts 567 -> 561, log 12208 -> 12097, census 8dd936c6.. -> 800444a0..
                 census="800444a09fae60b6fc1705c6deddffb4a07e01c71941fcb5d41cf06a35b247f6"),
    (0, 2): dict(acts=1192, log=32794,   # B15.99 re-record: acts 1235 -> 1192, log 26996 -> 32794, census caa693b0.. -> d55dac81..
                 census="d55dac8175f7314c5a84aa53ffad4b63964767b11eb9f86a88a2a6a7b57834da"),
    (1, 2): dict(acts=1230, log=38677,   # B15.99 re-record: acts 1230 (equal), log 27998 -> 38677, census 44dc9ad3.. -> b6f4878c..
                 census="b6f4878ce70c224997a1a205cad8e9439c35d6969e96bb004df7fc588d29fcbb"),
    (2, 2): dict(acts=1230, log=33701,   # B15.99 re-record: acts 1245 -> 1230, log 29699 -> 33701, census 268e6c19.. -> 425e91e7..
                 census="425e91e7f0722374592458001928315c81c13b8baa704c283b21218c9a95e61a"),
}
