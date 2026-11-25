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

RE-PINNED AT B15.99 (main, after BA1.99; every `SHIPPED` and `CENSUS` value; BUILD unmoved): the fight's calibration (B15). Its readings are in `git log`.

RE-PINNED AT B24p.99 (every `SHIPPED` and `CENSUS` value; BUILD read `4c6a3a99..` unmoved at seed 0, on the B24p tree before the merge): the batch's movers, each declared at its item: the five influence
verbs `argue`, `lie`, `speak`, `tell` and `interrogate` rest on the proceeding entry (B24p.19), each hearer is moved for himself (B24p.20), what the beats
show is deposited with those who saw it (B24p.22), the six roles (B24p.23); the docket item's `arranger` and `rig` (B24p.24) move the realm's hash by their encoding, the item's two keys. Read once on the
closing tree (`PYTHONHASHSEED=0`, twice equal, the six readings); seed 0, one season, each mover in order: `c8e57653..` (batch open) -> `ae2019b6..` (B24p.19) ->
`4b7d0ca5..` (B24p.24) -> `aae24e2a..` (B24p.20) -> `ce07cfb4..` (B24p.22) -> `a0000b5e..` (B24p.23, the closing tree). The B10.99 values these replace are in `git log`.

RE-PINNED AT THE B24p.99 CLOSE (the six `SHIPPED` hashes; `BUILD` and every `CENSUS` value, acts, log and digest, read unmoved on the B24p tree): the close's fixes to the proceeding. `heard` is
read against the man opposite again (`lead(inp, other side)`, as `esteem` is), not against the one addressed in an abridged act: that is the one that moves the realm (seed 0, one
season, reverted alone it reads `a0000b5e..`; each of the others reverted alone, one at a time, leaves the new hash, so they are inert at that reading). The rest: an abridged
close reads the addressed man's own `Margin`, not the last hearer's; `believes` and `false_items` read claims at the world's tick and only truth-valued ones; the chooser's
believed path filters claimants to persons and raises the fold's data defects; `View.odds` signs the mood toward `for`; `odds_of` is `None` for a verb that proceeds. Read
once on the closing tree (`PYTHONHASHSEED=0`, twice equal); seed 0, one season: `a0000b5e..` -> `acdee97d..`.

RE-PINNED AT THE B24p MERGE WITH MAIN (BA1.99 and B15.99 landed on main while B24p was open; every `SHIPPED` and `CENSUS` value, BUILD unmoved: `f8f4cb23..`, main's, at seed 0): the merged realm is a third state. Seed 0, one season,
read twice equal at `PYTHONHASHSEED=0`: main `4aab36db..` (B15.99) and the B24p tree `acdee97d..` -> `1e3cd6db..`.
"""

BUILD = {0: "f8f4cb234a523f56d6a912625cb3046f"}                      # build_realm(seed), unplayed

SHIPPED = {(0, 1): "1e3cd6db48ed7c5518aa3e36606d38e4",   # B24p merge re-record: 4aab36db.. -> 1e3cd6db.. (the B24p tree alone: acdee97d..)
           (1, 1): "c59f3f3f1f2b710059f27216e7da24d5",   # B24p merge re-record: 20fe61b8.. -> c59f3f3f.. (the B24p tree alone: 48c76e3f..)
           (2, 1): "2400da0b04fa90d99965ee8838116431",   # B24p merge re-record: cc07d471.. -> 2400da0b.. (the B24p tree alone: eb92a171..)
           (0, 2): "c9bba3fafb2262524af9eb30179977fe",   # B24p merge re-record: e6466cf7.. -> c9bba3fa.. (the B24p tree alone: ba059cf7..)
           (1, 2): "c27bb192d458d1e2981d7de4cf1f5c27",   # B24p merge re-record: ab117da3.. -> c27bb192.. (the B24p tree alone: e22aedb8..)
           (2, 2): "66216a487ee49ee85befca9c6dab50fc"}    # B24p merge re-record: 810c688f.. -> 66216a48.. (the B24p tree alone: 0d941347..); the earlier values are in `git log`

#: What the run leaves, beside its hash: `acts` is `populated.run`'s act count, `log` the
#: length of the world's Event log, `census` the sha256 of `populated.run`'s return value as sorted
#: JSON (the census plus `acts`, `actors`, `act_subjects` and `claim_sources`).
CENSUS = {
    (0, 1): dict(acts=584, log=14310,   # B24p merge re-record: acts 583 -> 584, log 13525 -> 14310, census 1f2426e6.. -> 51923d09..
                 census="51923d09e9b1bec9725c5834c72a14dbb21d657b43f68b789fdccede145c1698"),
    (1, 1): dict(acts=595, log=11347,   # B24p merge re-record: acts 593 -> 595, log 11304 -> 11347, census 0439b04c.. -> c9f31a69..
                 census="c9f31a691cbc408a9a81d7afb305c3e480a296d13b7a1cfc72afed5588a2a729"),
    (2, 1): dict(acts=557, log=11538,   # B24p merge re-record: acts 561 -> 557, log 12097 -> 11538, census 800444a0.. -> 6bca6431..
                 census="6bca6431e395f402463232f6a7075cbed6c8ce45981a1e47beffe159329cbdd2"),
    (0, 2): dict(acts=1204, log=33920,   # B24p merge re-record: acts 1192 -> 1204, log 32794 -> 33920, census d55dac81.. -> 06a39a58..
                 census="06a39a58a006504713a0e55a21156d96c6de0e5b55514ba05daa2b325fcfcf15"),
    (1, 2): dict(acts=1227, log=39789,   # B24p merge re-record: acts 1230 -> 1227, log 38677 -> 39789, census b6f4878c.. -> 9de042f8..
                 census="9de042f87a9d2517ca335854b78fd50ebfdbe2167e3707a3638dbb7c7345d3bf"),
    (2, 2): dict(acts=1239, log=31374,   # B24p merge re-record: acts 1230 -> 1239, log 33701 -> 31374, census 425e91e7.. -> 9de7afed..
                 census="9de7afedb9b39b57fd20de532e2f0b8518d052ec53315a6e35b36e89daca44d6"),
}
