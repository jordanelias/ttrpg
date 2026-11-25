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

RE-PINNED AT BA1.99 (every value below, BUILD too), ONCE for the batch BA1-cast-content, a SECOND time after BA1.02's ten `manner:` rows were held back (`8d32955b1`: they moved R-06.d's strict-top share to exactly one half). The movers are BA1.01 (the cast's `stats:` and `capabilities:`), BA1.08 (the six `relations:` rows) and BA1.12 (the two `unaware:` marks, which remove seeded `self:` claims); BA1.03, BA1.04, BA1.06 and BA1.09 read equal to their predecessors. Seed 0, one season, each on its own tree (`PYTHONHASHSEED=0`), hash (BUILD) acts/log: `c21e451f1` (the B10.99 tree) `c8e57653..` (`4c6a3a99..`) 563/12966 -> BA1.01 `f5ed8eba..` (`a621787d..`) 563/13238 -> BA1.08 `08466028..` (`17094d3d..`) 570/13315 -> BA1.12 `e279b27a..` (`f8f4cb23..`) 570/13315, the census digest moved = the closing tree. BA1.02's ten `manner:` rows are held back (`git show 27ab0bb3b`) and these pins exclude them; the BA1.08 and BA1.12 readings are the closing tree with the later mover's rows taken out, since the item commits carry the manner rows. Seeds 1 and 2 and the two-season spans were read on the closing tree only. The previous pins (recorded with the manner rows in) are in `git log`.

RE-PINNED AT B11.99 (every value below, BUILD too), ONCE for the batch B11-fi-readers: re-pin: B11's declared movers. Read once on the closing tree
(`PYTHONHASHSEED=0`; seeds 0 to 2, one and two seasons; the same values twice at seed 0, one season). Seed 0, one season, each mover in order on its
own commit, build hash (BUILD) -> hash: `ce61cbf30` (BA1.99) `f8f4cb23..` -> `e279b27a..`; B11.04 `reach` channel `c8e57653..` -> `88b15722..` (read on the
pre-BA1 tree `c21e451f1`, where the batch opened: BUILD `4c6a3a99..`); B11.08 ledger referents BUILD -> `bbaac534..`, hash `70a0b41c..`; B11.10 `d15b772c..`;
B11.12 `aa274da4..`; B11.13 `31f2c719..`; the BA1 merge `eeb62941e` BUILD `30731bfd..`, hash `94c5f786..`; B11.14 `6ea8bbbd..`; B11.17 (`Record.ttl` deleted,
by encoding: BUILD) BUILD `d0003259..`, hash `879408ac..`; B11.51 `42e52d5e..`; B11.58 `403f07b2..`; B11.59 `14531379..`; B11.61 `43fcd2a5..`; B11.83 `05f0d9fc..`;
B11.64 `62d9ba9d..`; B11.69 `4326c35d..`; B11.71 `546eb23c..`; B11.72 `80301489..`; B11.73 `1fdef279..`; B11.74 (`Proposition.support`, by encoding: BUILD)
BUILD `f2e82ab5..`, hash `793f29fd..` = the closing tree. B11.15, B11.22, B11.53 to B11.55, B11.60, B11.63, B11.75 to B11.79 read equal to their
predecessors at seed 0, one season (every per-item reading above is seed 0, one season only; seeds 1 and 2 and the two-season spans were read on the closing tree only). B11.67 flipped nothing (`notice_arm` ships `off`), B11.16 and B11.85 were not built.
The BA1.99 values these replace are in `git log`.
"""

BUILD = {0: "f2e82ab5efd35714a15064eaeab81872"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "793f29fd22710b5257a00589c34021d9",
           (1, 1): "fa87fb815a6ecd6dd6639dd82e7437ae",
           (2, 1): "e3bf99b86b2314a4b5fb90cc8f2fa86e",
           (0, 2): "22923ad396032a8c208498002b6cd9fa",
           (1, 2): "1246e1562ed2bd8c7c0b667e64bd0e59",
           (2, 2): "792f4f1de28653657c1f6e53909134bb"}    # B11.99 re-pin (the docstring); the BA1.99 values are in `git log`

#: What the run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    (0, 1): dict(acts=536, log=9542,
                 census="e563cb712db7dc03c151379bdf94effa730d0a4b5e6784ee06991f4faae2a5b8"),
    (1, 1): dict(acts=584, log=10066,
                 census="10bf5068720526958960dff112b4bee0f90c89ae79b1c3a4e429dd2c46edec38"),
    (2, 1): dict(acts=542, log=9126,
                 census="737bb17341471dc3c9094716eec47b22bbbbc1cab66fb9d4b680a8cc5e6ed7b5"),
    (0, 2): dict(acts=1112, log=19202,
                 census="3375123274289ed8e2fbe0b226936e5e582d5085f2cafca8d367b9526df6fe72"),
    (1, 2): dict(acts=1193, log=20536,
                 census="274d77ec0599c8165837a9ed1ce1ad9c4bf0dba5e530d4b650e3866ed06d6a2a"),
    (2, 2): dict(acts=1095, log=19046,
                 census="2830500e0294e5089a97ff35c0f30135ddcd4cedf21736556a793a7aaffd36a7"),
}
