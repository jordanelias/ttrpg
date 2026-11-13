# E_REPAIR — repair of the Stage E antagonist's findings 1 and 2

## Status: WORK FILE (log of one repair lane; resolves nothing at runtime; deleted when v12 is adopted)

**Finding 1 — two definitions of a null scene under one flag.** One owner chosen: `B02.20` (`30_WR_D` §3's
durable write, copied into `null_scenes`'s docstring). Ladder: design document (`IS-A-07` names B02.20 the one
owner); architecture (28A's "no gate write and no `claim.deposited` citing them" counts a bystander's sighting,
the defect `30_WR_E`'s falsifier names; two wordings are two ladders for one quantity, CLAUDE.md §0.06 S).
B28's and B38.12's narrower scene classes are now a `scope` argument of `null_scenes` (which acts are counted),
not a definition of the write.

| file | handle | change |
|---|---|---|
| `workplan_v12_part3.md` | B02.20 step 2 | one-owner sentence, ladder reason, `scope=None` argument |
| `workplan_v12_part3.md` | B02.20 GATE | baseline = this item's first reading, command stated; 59 of 821 labelled a one-season comparison |
| `workplan_v12_part3.md` | B02 BATCH GATE (two lines) | `NULL SCENES` close reading must equal B02.20's |
| `workplan_v12_part3_cont.md` | B02.99 ADVANCES | `NULL SCENES` re-read against B02.20's |
| `workplan_v12_part35.md` | B28 BATCH GATE | `access --null-scenes` cites B02.20, its class stated as a scope |
| `workplan_v12_part35_cont.md` | B28.22 INSTRUCTION, DEPENDS ON | the flag calls `null_scenes` with a scope; depends on B02.20 |
| `workplan_v12_part40.md` | B38.12 step 3, GATE | the same, the scope widened to `carry` or an engaging act |
| `workplan_v12_part40.md` | B38 BATCH GATE | access count above 0 STOPS; C9 and C8 asserted, either failing STOPS |
| `workplan_v12_part41.md` | B38.71 step 6, C9 | the carriers listed by item handle, by `30_WR_D` §3 row |
| `workplan_v12_part39.md` | B36 "Not in this batch" | `--null-scenes` is B02.20's, not B38's |

**Finding 2 — C8 could not fail its gate.** B38.71's GATE now asserts C8's failure condition (three of ten
at two of five seeds; acts per person-season at least half the free arm's), runs five seeds (`--n 5`, was
`--n 3`, which could not read "of five"), names the controls (S-43 and E-02 at 0, the free arm, `S-28d` at 0
from B38.13 GATE 3), and the batch STOPS on it (B38 BATCH GATE; B38.99 step 2 and FALSIFIER). The thresholds
stay flagged; `V12_FOR_JORDAN.md` J-08 added.

**Not resolved here.** Whether every listed C9 carrier makes a reading of 0 reachable at B38.99 is unmeasured;
the list is an `[ASSUMPTION]` at C9. Other items that mention a durable write in their own words (B17.01,
B22.11, B34.01 and others) were not touched: they describe their own write, not the instrument.
