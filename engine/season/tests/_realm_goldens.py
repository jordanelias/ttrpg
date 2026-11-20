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
"""

BUILD = {0: "d691552fcd4931573c465bbc341bdcad"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "88224913106d91e81ed815cd6114497c",      # (seed, seasons) at DEFAULT_FIXTURES; was 10934f0f516cad26f9c85625268d971e (merge)
           (1, 1): "a7b49d60bb22d53133e08ea6b112ebd0",      # was 6593d8b0c1cc0a7f7931d450df96b1e1 (merge)
           (2, 1): "7ed1fee3f535a08d87638dce09eb3edd",      # was ad10b3c876f3d9f19e27fe8e84e52dd6 (merge)
           (0, 2): "f39e02def78efc76fb679313804893ef",      # was ec41cc8d78ccbe9c5c7fe834e7ae9239 (merge)
           (1, 2): "33bf9f9b7c5f569c237328aa4e518390",      # was fded13c6f6ed2f42f0b2c57cc5dc67b4 (merge)
           (2, 2): "85c6ebfd6041d72348f787d61440c7c2"}      # was bbe99b7804e53b607bcc56f90605a48b (merge)

#: What the run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    # was (acts, log) at the B06/B14 merge: (0,1) 750/12583  (1,1) 780/11316  (2,1) 766/11751  (0,2) 1627/35771  (1,2) 1552/31803  (2,2) 1608/36974
    (0, 1): dict(acts=630, log=11927,
                 census="7effd68f0f12634cb7b8572bd5c0085bdbaf518e60577d482b2f4c18a989d427"),
    (1, 1): dict(acts=668, log=11367,
                 census="7f3a3a3f3a17fa376a9d2182218c03abc208ab01fcab14076ab18e9836d8bd3d"),
    (2, 1): dict(acts=652, log=10913,
                 census="722fb1d4ae772f822df4d7e01ed292ca334e367edcb5e529b013024737bd7c58"),
    (0, 2): dict(acts=1388, log=36230,
                 census="38f61da6acf6eb130285747ec502f72d1896220265a4cb1bc3c586f246b2be97"),
    (1, 2): dict(acts=1356, log=30039,
                 census="0c446eb752a214add70a00a172df59718fec83f0c5f53edf8552fad9922323e2"),
    (2, 2): dict(acts=1422, log=33919,
                 census="5eb6cb2efe740a503408c1cdf48af8128aec1aa7a894827624aaf7a784b8eec2"),
}
