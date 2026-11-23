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
down, B10.73 ARC-47's stage row); B10.59, B10.66, B10.70 and B10.71 measured equal at the shipped data and the first half moved nothing.
Read once on the closing tree (`PYTHONHASHSEED=0`); seed 0, one season, each mover in order: `6e3a066a..` -> `5f2b9826..` (B10.58) ->
`576272fd..` (B10.60) -> `39d7c1bc..` (B10.65) -> `3ed14dad..` (B10.72) -> `faf327b7..` (B10.73). The B09.99 values these replace are in `git log`.
"""

BUILD = {0: "4c6a3a994777d975976bd3874ce74c9b"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "faf327b78ebf3132a50ba1319fcad0c3",
           (1, 1): "9e763785af9c648cd4bacb4890b80af7",
           (2, 1): "b1489dab34908506b98f4534d5e96e43",
           (0, 2): "e6eddc5dc4cbcac1d4484cba448b742a",
           (1, 2): "04586bc49efada683d4095599ff552a1",
           (2, 2): "34be2cb25f84e72855011ba10282e332"}      # B10.99 re-pin (the docstring); the B09.99 values are in `git log`

#: What the run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    (0, 1): dict(acts=581, log=24384,
                 census="cea0d00896fffc38865f9f99759404f5796ed51e9e70aec9049a78fd250b592d"),
    (1, 1): dict(acts=586, log=24009,
                 census="eb17b81cdc02db9f773f3ece25308bd65c86ad557dfaf318d6d88a303bd79a5f"),
    (2, 1): dict(acts=575, log=23231,
                 census="43b44ab6447678ebbef4097877c8eae15650a5d74483dc12a7f1a87ccb545f66"),
    (0, 2): dict(acts=1213, log=47771,
                 census="47ad784c57ae5c0ad56ff3d9c25599c23407219bb4d0d940a16abb2a75e69cf0"),
    (1, 2): dict(acts=1226, log=41237,
                 census="0bfad3ef249e086440a52f2040df8c6bc13b73f2784e3e076da2e91dfc53ae46"),
    (2, 2): dict(acts=1171, log=36741,
                 census="afd6b54691cdbe5c33435b85188932d6cb2b06081ac6b3c5ca4dc4fff3cc6786"),
}
