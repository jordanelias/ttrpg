"""The realm goldens: one literal per (seed, seasons, arm). Every hash test imports from here.
A re-record is one edit to this file, in the commit that moves the world, with the mover named in
that commit's message (CLAUDE.md §7).

An item that moves the realm proves in its own commit that its revert reads the previous pin, and
records that in the commit message; the proof is not kept as a test.

Read with `build_realm(s)` and `populated.run(1, s, w=w)` at `PYTHONHASHSEED=0`, seeds 0, 1, 2, on
the tree of B04.99 (the hashes moved in B03, by encoding: `Office.body_function` was deleted from a
class `World.content_hash()` encodes, B03.28; and in B04, by encoding: `Claim.round` became `Claim.lap`,
B04.01, and `Person` gained `traits`, B04.07; acts, log length and the census below did not move): the shipped world, `DEFAULT_FIXTURES` as they stand, with no revert applied. A test support
module beside `_scar_helpers.py`, not a registry: nothing but tests reads it.
"""

BUILD = {0: "bf3064be8fe5830b8cb5e06ef93ee883"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "c7b1543008d3a7dac8255b6f3873dcea",                # (seed, seasons) at DEFAULT_FIXTURES
           (1, 1): "1aa84707bd034b9e88fc456270cfe6a2",
           (2, 1): "8f44e683e2b0fe281944614935f2c783"}

#: What the one-season run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    (0, 1): dict(acts=793, log=14292,
                 census="ab6693fb73c7acd2753859403115b772f9bd732bbc21cadb354f3fddd0ddb121"),
    (1, 1): dict(acts=777, log=12583,
                 census="0e226fe03fc00b707e754dd14e6e3661ff1bb9b507d847777e5fb5709c2977e7"),
    (2, 1): dict(acts=744, log=12250,
                 census="022765489c92a537183e1b5786b6bb61d4551d192d45cfaec65fd191f7be3866"),
}
