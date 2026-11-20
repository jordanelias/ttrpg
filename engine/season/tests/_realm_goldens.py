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
reading equal under `PYTHONHASHSEED` 0 and 1). The shipped world, `DEFAULT_FIXTURES` as they stand, with no revert applied. A test support
module beside `_scar_helpers.py`, not a registry: nothing but tests reads it.
"""

BUILD = {0: "d691552fcd4931573c465bbc341bdcad"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "10934f0f516cad26f9c85625268d971e",                # (seed, seasons) at DEFAULT_FIXTURES; was 7ccf4abe89d508d4221e0a0c7cbcbfaf (B06.99)
           (1, 1): "6593d8b0c1cc0a7f7931d450df96b1e1",                # was 8c038011362cc69a17e964f0bfd3735f
           (2, 1): "ad10b3c876f3d9f19e27fe8e84e52dd6",                # was 61af70f40c67f8972a416b8c59612789
           (0, 2): "ec41cc8d78ccbe9c5c7fe834e7ae9239",                # two seasons; was d20ef860170ebe0d96001935bdd5e1d3
           (1, 2): "fded13c6f6ed2f42f0b2c57cc5dc67b4",                # was 709e1f8a879ace385ee79200aae7d65b
           (2, 2): "bbe99b7804e53b607bcc56f90605a48b"}               # was b6d80014c71394b100192f629aeb8cbb

#: What the run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    # was (acts, log) at B06.99: (0,1) 749/12603  (1,1) 780/11299  (2,1) 766/11715  (0,2) 1621/35807  (1,2) 1548/31651  (2,2) 1617/35704
    (0, 1): dict(acts=750, log=12583,
                 census="c587f66cb2336d983f6661a7aa39d1a225f0766206af22edde2e0be8af7bc6b0"),
    (1, 1): dict(acts=780, log=11316,
                 census="58490fceaa4c103557cb6d6a0369a7da904ff65ccbb0b732ca753c00924ec1f0"),
    (2, 1): dict(acts=766, log=11751,
                 census="2fe65ec52faac082eb4210bcfd16f39e5490602e0440191377ce4f202cfc5c7f"),
    (0, 2): dict(acts=1627, log=35771,
                 census="ee0c956493156cc6c98796fbf6384fd8c49f5c745dbe026bbe16b0515d193af7"),
    (1, 2): dict(acts=1552, log=31803,
                 census="204f74accad83acd305a24bae8bcf43c378d540168aa6904d1a9c05a323292f8"),
    (2, 2): dict(acts=1608, log=36974,
                 census="9c48547ee19014e6a007a45b81b48cf90da2b491ce1165774b1050a2c430bd5c"),
}
