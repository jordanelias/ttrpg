"""The realm goldens: one literal per (seed, seasons, arm). Every hash test imports from here.
A re-record is one edit to this file, in the commit that moves the world, with the mover named in
that commit's message (CLAUDE.md §7).

An item that moves the realm proves in its own commit that its revert reads the previous pin, and
records that in the commit message; the proof is not kept as a test.

Read with `build_realm(s)` and `populated.run(k, s, w=w)` at `PYTHONHASHSEED=0`, seeds 0, 1, 2, one and
two seasons, on the tree of B05.64 (`e075e511b`), RE-PINNED ONCE at B05.99. The movers since B04.99,
each a declared B05 item, each segment between two of them read equal at seeds 0, 1, 2: the one sampler
(B05.02), the skill score without the attribute (B05.09), the averaged governing score (B05.25), the
opposition is the opponent's score (B05.11), the one obstacle form (B05.14), `Event.ending` carries the
margin tuple (B05.18), `Office.modifier` (B05.20, by encoding: the build hash too), the calibrated arm
(B05.23, the bench seats' `modifier: minor`: the build hash too), the `wounds` row in every roll's
`levels` (B05.60), the believed prior (B05.62), one spacing of remove (B05.64). Earlier: B03 by
encoding (`Office.body_function`, B03.28), B04 by encoding (`Claim.lap`, B04.01; `Person.traits`,
B04.07). RE-PINNED ONCE MORE AT B06.99 (every value below): the uniform's source changes from CPython's
generator to the keyed mix (B06.04, A-30), a stream change and not a balance change (seed 0, one season,
read equal at B06.04, B06.05 and B06.06: `7ccf4abe89d508d4221e0a0c7cbcbfaf`). The shipped world, `DEFAULT_FIXTURES` as they stand, with no revert applied. A test support
module beside `_scar_helpers.py`, not a registry: nothing but tests reads it.
"""

BUILD = {0: "d691552fcd4931573c465bbc341bdcad"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "7ccf4abe89d508d4221e0a0c7cbcbfaf",                # (seed, seasons) at DEFAULT_FIXTURES
           (1, 1): "8c038011362cc69a17e964f0bfd3735f",
           (2, 1): "61af70f40c67f8972a416b8c59612789",
           (0, 2): "d20ef860170ebe0d96001935bdd5e1d3",                # two seasons: the batch gate's reading (B05.99)
           (1, 2): "709e1f8a879ace385ee79200aae7d65b",
           (2, 2): "b6d80014c71394b100192f629aeb8cbb"}

#: What the run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    (0, 1): dict(acts=749, log=12603,
                 census="6e538abddb9081e0bd01afc7ac8b173b14a772fa8be199bcc9e558d048c926da"),
    (1, 1): dict(acts=780, log=11299,
                 census="3c5cd6408e05fe987dce1f97f7be6e5d7d87101c860fc4bf7c400ccdbd0daa84"),
    (2, 1): dict(acts=766, log=11715,
                 census="4077a96cb9e8c41bab637281dfd2943e443f30cadf88c8a9429db666c013f31d"),
    (0, 2): dict(acts=1621, log=35807,
                 census="f5057483dcfda198b382585a678732be7f06342bcdd5ddd321d37bd0d88c6572"),
    (1, 2): dict(acts=1548, log=31651,
                 census="6305e2362c868cf9c9a6b8bfb152a6ba3725ffade2e4d1931982e2846ca81e78"),
    (2, 2): dict(acts=1617, log=35704,
                 census="4600e8ccd416bf35bdd3283ab7d5f5e9199a974ca6630e1e9a084a573a062c51"),
}
