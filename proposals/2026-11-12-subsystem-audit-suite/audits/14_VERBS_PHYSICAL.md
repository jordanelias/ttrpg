# VERBS · PHYSICAL — build-out of the nine `contested_physical` rows

## Status: REFERENCE (a verb build-out audit; resolves nothing at runtime, CLAUDE.md §0.05)

Authored in part by Fable; completed by Opus after the Fable usage limit (2026-11-12).

## Read at: 84d2a02 (working tree; implementation lane A's duel-chain edits not yet merged, see §0.2)

Work order: `VERBS_BRIEF.md`, FAMILY = PHYSICAL. Verbs: `arrest`, `fight`, `capture`, `accept`, `march`,
`raze`, `examine`, `surveil`, `thread_read` (the nine rows of `engine/season/verb_table.yaml` whose
`stratum:` is `contested_physical`). The exact edits are in the four proposals named in §0.4; this file
holds the premise, the state today with its reading, the decided build-out, and the family's order.

## 0. Verdict and reading

### 0.1 Verdict

**None of the nine works as its plain meaning promises, and none is a stub.** Every one has a row, an
effect or a route, and a test that passes on a hand-built world; what fails is reach and consequence. At
`aperture 2 0` (realm, seed 0, two seasons, `PYTHONHASHSEED=0`, control hash EQUAL) the family made 113
attempts and produced, in total, three unopposed arrivals and six `surveil` findings that taught nobody
anything. The single largest obstacle is the same for seven of the nine: **the act forms on a referent,
or in a state, that the fold must refuse for a reason the actor could have read** (a Record that is no
challenge, a place his army does not stand in, a person who is not where he is, a hearth that is no
field). The other two (`surveil`, `thread_read`) execute and carry no product.

### 0.2 What this is read against

- HEAD `84d2a02`. Implementation lane A (`IMPLEMENTATION_BRIEF_A.md`) is landing
  `proposals/03_PC_duel_chain_reach.md` in a worktree; at the time of this reading its branch carried no
  commit, so every figure here is the **baseline** that lane moves. Where a build-out below depends on
  lane A's result it says so and does not restate that proposal's edits.
- One seeded instrument reading per verb, as the brief asks: `aperture 2 0`
  (`scratchpad/runs/VERBS_PHYSICAL/aperture_2_0.txt`) and `corpus_run`
  (`scratchpad/runs/VERBS_PHYSICAL/corpus_run.txt`). A second seed is quoted from the lane audits where
  they ran one (`audits/03_PC_audit.md` E7b; `audits/04_MB_audit.md` F-MB-03). One seed is a reading of a
  trajectory, not a rate (CLAUDE.md §0.1 pt 4); nothing below is a balance claim.

### 0.3 State today, one line per verb

`elig` = persons eligible at build (seated / unseated); `formed` = persons who formed it; `att / ex / ref`
= acts attempted, acts that emitted a declared `emits:` kind, acts that emitted a refusal kind (`ex`
counts a `finding.none` and a `march.declared`, so read `ex − both`). Realm arm.

| verb | elig | formed | att | ex − both | ref | deciding read of the refusals | verdict |
|---|---|---|---|---|---|---|---|
| `arrest` | 26 / 0 | 1 | 0 | 0 | 0 | — | **forms almost never; never attempted** (`arrest.made` is in the never-emitted list) |
| `fight` | 33 / 50 | 0 | 0 | 0 | 0 | — | **unreachable** (no `violence_contexts` reader names anybody) |
| `capture` | 26 / 0 | 26 | 12 | 0 | 12 | `with=False` 7 · `exists:Person=0` 3 · `individual=False` 2 | **forms but is refused** |
| `accept` | 33 / 50 | 37 | 27 | 0 | 27 | `exists:challenge=0` 27 | **forms but is refused** (lane A's target) |
| `march` | 26 / 0 | 26 | 13 | 3 | 10 | `no-read` 10 (ENCOUNTER: the target is no field) | **executes only unopposed**; 0 fields fought |
| `raze` | 26 / 0 | 26 | 14 | 0 | 14 | post-admission 14 of 14 (the effect: no occupation) | **forms but is refused** |
| `examine` | 33 / 50 | 1 | 0 | 0 | 0 | — | **unreachable** (its `site` operand is never a Site) |
| `surveil` | 33 / 50 | 83 | 44 | 6 | 38 | graded loss 16 · `present_at=False` 15 · `exists:Rung=0` 7 | **executes and finds nothing** |
| `thread_read` | 33 / 50 | 4 | 3 | 3 | 0 | — | **executes and finds nothing** (ungraded; no finding terms) |

Never emitted in this run, of the family's declared kinds: `arrest.made`, `arrest.resisted`,
`arrest.refused`, `arrest.unauthorized`, `fight.declared`, `kill.refused`, `contest.undecided`,
`capture.declared`, `person.captured`, `accept.declared`, `duel.yielded`, `field.won`, `field.lost`,
`siege.pressed`, `rung.razed`, `person.died`, `tenure.closed`, `capability.raised`. Death census: 0.

### 0.4 The proposals that carry the edits

| file | verbs | batch |
|---|---|---|
| `proposals/14_VERBS_PHYSICAL_A_custody_and_force.md` | `arrest`, `capture`, `fight`, `accept` | P-A |
| `proposals/14_VERBS_PHYSICAL_B_field_and_ruin.md` | `march`, `raze` | P-B |
| `proposals/14_VERBS_PHYSICAL_C_looking.md` | `examine`, `surveil` | P-C |
| `proposals/14_VERBS_PHYSICAL_D_thread_read.md` | `thread_read` | P-D |

