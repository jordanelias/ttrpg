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
"""

BUILD = {0: "d691552fcd4931573c465bbc341bdcad"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "c5cbd61a8c0aba51b0e1585b9fbbc0b1",      # (seed, seasons) at DEFAULT_FIXTURES; was 10934f0f516cad26f9c85625268d971e (merge)
           (1, 1): "ef37fc05d82dc1696ff4ebb4bce0e3df",      # was 6593d8b0c1cc0a7f7931d450df96b1e1 (merge)
           (2, 1): "7ed1fee3f535a08d87638dce09eb3edd",      # was ad10b3c876f3d9f19e27fe8e84e52dd6 (merge)
           (0, 2): "5b2b3c93b16e791f1adae0efb1c83e64",      # was ec41cc8d78ccbe9c5c7fe834e7ae9239 (merge)
           (1, 2): "94a4896be8fdef059f640d163d0ce026",      # was fded13c6f6ed2f42f0b2c57cc5dc67b4 (merge)
           (2, 2): "85c6ebfd6041d72348f787d61440c7c2"}      # was bbe99b7804e53b607bcc56f90605a48b (merge)

#: What the run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    # was (acts, log) at the B06/B14 merge: (0,1) 750/12583  (1,1) 780/11316  (2,1) 766/11751  (0,2) 1627/35771  (1,2) 1552/31803  (2,2) 1608/36974
    (0, 1): dict(acts=630, log=11936,
                 census="4a961c0491c1a1b1b13ab870b683570dcb0aba35ebec3f969b50f827625fd6e8"),
    (1, 1): dict(acts=669, log=11404,
                 census="81b7911ca7cfee146add067d4dc61ac0552fcb39a177cd4a13a2470de381c486"),
    (2, 1): dict(acts=652, log=10913,
                 census="722fb1d4ae772f822df4d7e01ed292ca334e367edcb5e529b013024737bd7c58"),
    (0, 2): dict(acts=1385, log=36560,
                 census="bb65c68c03f628fde736badc616ba2ed5c009b2dd050d5f76132974418f73e56"),
    (1, 2): dict(acts=1368, log=30736,
                 census="d04c8f1715482286243c274576f9f0789aa5c024fccca0a8ac3525533fc38e92"),
    (2, 2): dict(acts=1422, log=33919,
                 census="5eb6cb2efe740a503408c1cdf48af8128aec1aa7a894827624aaf7a784b8eec2"),
}
