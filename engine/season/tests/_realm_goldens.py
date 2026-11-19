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
B04.07). The shipped world, `DEFAULT_FIXTURES` as they stand, with no revert applied. A test support
module beside `_scar_helpers.py`, not a registry: nothing but tests reads it.
"""

BUILD = {0: "4b56a92cf2438d45bd080a7be0ab1d3c"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "01b25620671b774f0fe3a93f40b82c9f",                # (seed, seasons) at DEFAULT_FIXTURES; B14.99 re-pin, was ce765e35...
           (1, 1): "2d813f1dcb529318681fcdd2ab7f2f09",                # was d35b4a0f...
           (2, 1): "f5dad72e776496746807815fcfb17a82",                # was 2a1a02ea...
           (0, 2): "faba3b35e6dfd677f12c11bd797d8843",                # two seasons: the batch gate's reading (B05.99); was e3e950c8...
           (1, 2): "33a7af20eed995e5ff7e92ebad0e21fd",                # was 27ee8b2e...
           (2, 2): "ca30d5d44b869278da5387932d01b747"}                # was 6b56a542...

#: What the run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    # B14.99 re-pin (the old literal in the trailing comment of each row; (2, 1) and (2, 2) census digests did not move).
    (0, 1): dict(acts=778, log=14178,           # was log 14168, census 3557439b...
                 census="ba2bf038f06594c4ba0d99bcfdf6dd95d3601175c1550ff4d06bce9992f4d7e4"),
    (1, 1): dict(acts=768, log=12299,           # was log 12289, census 0ee3acea...
                 census="ae3ca459f53d689d01eb0134074d745c446826b423e3accc9e61f7070898850a"),
    (2, 1): dict(acts=748, log=12787,
                 census="e1093e96566f6d08e25f2673e67099cbd4b8ab1d49fc95a6740102b286d05e93"),
    (0, 2): dict(acts=1611, log=38977,          # was acts 1610, log 39397, census e940a0aa...
                 census="4e51703ea60164c3755b23b8e6381e4f4c6479cdbbc9ed72263d381d85a3a970"),
    (1, 2): dict(acts=1594, log=35585,          # was acts 1601, log 35575, census f3d047f0...
                 census="d9420f9480e175f8c9e8517ae5d07ac9862d52da00e08d5ca9af288cd0bdf718"),
    (2, 2): dict(acts=1593, log=36061,
                 census="27d02877c57b82b50c43a099e025dd04aa5ec1dc7293ae48bf2a25ee0b0744e3"),
}
