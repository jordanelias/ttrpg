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
B04.07). The shipped world, `DEFAULT_FIXTURES` as they stand, with no revert applied. A test support
module beside `_scar_helpers.py`, not a registry: nothing but tests reads it.
"""

BUILD = {0: "4b56a92cf2438d45bd080a7be0ab1d3c"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "ce765e35b9f59de3aa6f3485f0286772",                # (seed, seasons) at DEFAULT_FIXTURES
           (1, 1): "d35b4a0fd228d90c99c4e1622defc383",
           (2, 1): "2a1a02ead7fb913459c76a141d0307ed",
           (0, 2): "e3e950c8d295265c35b1b99d3bcd231a",                # two seasons: the batch gate's reading (B05.99)
           (1, 2): "27ee8b2e1998a169cbe40eb188ad37ea",
           (2, 2): "6b56a542ca50547d6fcea98377000769"}

#: What the run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    (0, 1): dict(acts=778, log=14168,
                 census="3557439b62969d31b40371a71cd913c2f81087443cee84039a2172db57216b6b"),
    (1, 1): dict(acts=768, log=12289,
                 census="0ee3acea6a611eb094722df8d3b687e67cf860271ac79c8d0b924bc6c6d91180"),
    (2, 1): dict(acts=748, log=12787,
                 census="e1093e96566f6d08e25f2673e67099cbd4b8ab1d49fc95a6740102b286d05e93"),
    (0, 2): dict(acts=1610, log=39397,
                 census="e940a0aacacb8be638c1c44b7a136ef25a7313220c788bb9151bc8b4a9d3fd83"),
    (1, 2): dict(acts=1601, log=35575,
                 census="f3d047f082a16b53efd710a2ff5fe8bb86f32c773061cd4e3dd99a62f5cabc6d"),
    (2, 2): dict(acts=1593, log=36061,
                 census="27d02877c57b82b50c43a099e025dd04aa5ec1dc7293ae48bf2a25ee0b0744e3"),
}
