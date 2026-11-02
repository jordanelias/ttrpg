# Social contest: how to build everything the companion document marks missing

## Status: PROPOSED (reference; resolves nothing, schedules nothing)

> **Asked:** *"plan how to build all"*. `[ASSUMPTION: "all" is every item that `2026-11-01-social-contest-matters-standpoints-and-fold.md` (the companion, **C**) marks ABSENT or NEVER, ordered into batches; basis: it is the one document that lists them across intake, disposals, standpoints and the fold]`

**This file is not a plan and adds none.** `CURRENT.md` names one active plan, `workplans/valoria_master_workplan_v10.md`
(+ `_part2` to `_part15`), and `CLAUDE.md` §2 allows one per lane, with a carve-out only by name. This file proposes which
of that plan's social-contest rows to re-cut. Adopting any of it is an edit to B10-13 and B10-19 in one commit that retires
what it supersedes, and that commit is Jordan's. Rulings `R-n`, `S-n` and ids `P1` to `P4`, `K1` to `K8` are as in C.

**Evidence.** Plan rows were read in `workplans/valoria_master_workplan_v10.md` (the batch table, `:79-103`) and
`_part12.md` (the position index). A coverage cell marked **[UNVERIFIED]** means I looked for the item in `_part12`'s index
and did not find it; it may live in a position I did not open. The "today" figures are C's probe outputs (seeds 0 and 1, four
seasons). Nothing here was built or run.

---

## 1. The result

1. **Twenty-eight items**, in seven groups (§2). Nine are on the active plan already (B10-13, B10-09, B10-17, B10-19, B10-08,
   B10-Z; W1, W2, W5, W7, W8, W17, W25, W26, W28); nineteen are marked **[UNVERIFIED]**, meaning I did not find them in
   `_part12`'s index.
2. **One item blocks more than any other: a computed `give` that completes** (W6). It carries the citation, a petition to a
   grantor, a writ, a bargain, a grant, and the forged-sheet example. It was refused 7 of 7 at seed 0, and the reason is a
   ruling Jordan worded *"just say no for now"* (ED-IN-0292 (1)). It is the plan's most valuable single question.
3. **Eight batches, one spine** (§3). The shared dead core goes first because every proposal needs it. The deletion of the
   kernel goes last, not first, because P4's critic showed batch A1 cannot be green as ordered (it deletes
   `VERB_CAPABILITY` before its replacement lands).
4. **Done is not "the document exists"** (`CLAUDE.md` §0.2). Each batch is closed by an observable that is zero today and
   must be above zero after, with a control arm that reproduces today (§4).
5. **Two decisions are Jordan's after the answer-first ladder** (§5): reopening ED-IN-0292 (1), and the Layer-1 §A.3 wording
   for office weight (ARM G2). A third (P4 Q2) waits until batch 6.

---

## 2. The build ledger

"Covered by" names a position in the active plan. "Flips" is the observable (a probe in this folder, or a named test).

### Group A: the shared dead core (every proposal needs it)

| id | build | lands in | covered by | flips (today at seeds 0 / 1) | needs |
|---|---|---|---|---|---|
| W1 | a computed `open_case` names its arrangement row | `_eff_open_case`, `world_q.judging_set`, `arrangements.yaml` | SC-04 residue (B10-13) | docket items naming a row: 0 of 10 / 0 of 5 | none |
| W2 | a speech reaches a judgment: the judge's regard enters his own `determine` | `decision/`, `_eff_determine`, `sigma.py` | CP-T05-01 (B10-13) | `matter.determined`: 0 / 0 | W1 |
| W3 | a petition may be addressed to someone other than its subject (H-94) | `decision/options.py` binding | reasons-to-convene RL4 **[UNVERIFIED]** | a petition with `to` ≠ `terms` | none |
| W4 | a decline is an Event: unanswered citation, unserved warrant, lapsed matter (`matter.lapsed`) | `loop/matter.py`, `rosters.yaml` emits | **[UNVERIFIED]** | `matter.lapsed`: no code emits it | W1 |
| W5 | capability authored: the faculty default at R-40's reference, sheets for the cast | `data/cast.py`, `rosters.yaml: faculties` | J-13 and JQ-2; `_part6.md:33` (M2) | persons with capability: 0 of 78 | G2 if office weight is included |

### Group B: delivery (the hop six families wait on)

| id | build | lands in | covered by | flips | needs |
|---|---|---|---|---|---|
| W6 | a computed `give` completes for a Record, a petition and a writ | formation of `give`, `_eff_give`, `writs_held` | H-229 **[UNVERIFIED]** | `give` executed 0 of 7; `record.given` 0; `compliance.given` 0; forged sheets with two holders 0 of 45 | **ED-IN-0292 (1)** |

### Group C: disposals that do not exist

| id | build | lands in | covered by | flips | needs |
|---|---|---|---|---|---|
| W7 | a `hold` site in `_disposal`, and the `succession` row | `loop/effects_information.py`, `arrangements.yaml` | SC-04 residue; IN-61 (B10-09); CR-35 (B10-17) | a determination that transfers a hold; family 4 | W1 |
| W8 | the `resolution` Record kind and the licence conjunct on the owner's act, with a data owner for "this cession needs consent" | `record_kinds`, `verb_table.yaml`, `gate.py` | CR-36, CR-37 (B10-17) | an owner's act refused without a held resolution | W2, W7 |
| W9 | consent rows, and a distinct refusal kind (`<verb>.unlicensed`) that stamps the council's tier | `verb_table.yaml`, `rosters.yaml` | reasons-to-convene RL3 **[UNVERIFIED]** | a refusal that leads to a convening: 0 | W8 |
| W10 | the appeal closure basis (a seat other than the exercised one may void) | `state/gate.py` | **[UNVERIFIED]** | a crown seat voids a church custody | W7 |
| W11 | the warrant branch: a custody disposal becomes a warrant to a `dispatch` holder, who serves or declines | `_disposal`, `_eff_arrest` | IN-12 residue **[UNVERIFIED]** | `arrest.made`: 0 / 0 | W1, W4, W6 |

### Group D: intake producers (reasons to convene)

| id | build | lands in | covered by | flips | needs |
|---|---|---|---|---|---|
| W12 | stamp the tier where a matter waits (RL1); stop offering places-to-settle as venues (RL2); a re-slot step for matters already waiting | `queries/world_q.py` | **[UNVERIFIED]** | docket items holding both a date and a matter: 0 at every season end | W1 |
| W13 | a matter-sensitive term in the convene score (RL5) | `decision/choose.py` | **[UNVERIFIED]** | the share of offered convene Candidates chosen | W12 |
| W14 | strain producers: vacancy, shortage, war, restraint, each a motion kind bound to an existing query (RL6) | `queries/`, motion roster | **[UNVERIFIED]** | motions per run: 0 | W12, W8 |
| W15 | the docket lifecycle: a dead party and a venue with no bench lapse visibly; a non-person matter is refused or typed at `open_case` | `loop/matter.py`, `effects_information.py` | **[UNVERIFIED]** | no item holds a slot beyond a stated number of seasons | W4 |
| W16 | terms as a periodic reason (RL7) | council join | **[UNVERIFIED]** | renewals heard at a sitting | W14 (optional) |

### Group E: the choice layer (P4, cut back as its critic directed)

| id | build | lands in | covered by | flips | needs |
|---|---|---|---|---|---|
| W17 | verify, before building: B10-08 is CLOSED and names one faculty, one odds function and one ceiling. Check it is P4's continuous closed form (`p_success`), with the ceiling bounding the score and not the modifiers (D-1) | `modules/social_contest/roll.py`, `sigma.py` | B10-08 (CLOSED) | the live discrete roll equals the closed form at 2D and 12D | none |
| W18 | `authority.by_faction`, a `scope:` key on offices, case-opening reading `scope_rung`, and a two-valued rite default (accusatorial, inquisitorial) | `rosters.yaml`, `offices.yaml`, `data/arrangements.py` | **[UNVERIFIED]**; CR-38 for the bench | a church seat opens a case outside T9 | W1, Q1 of P4 |
| W19 | the case file as a Record of kind `case`; `determine` requires a held file; `_mint_document` declines an existing id; `forge` accepts kind `case`; MATTER matures on `<=` | `effects_information.py`, `matter.py:340`, `verb_table.yaml` | **[UNVERIFIED]** | burning the file stalls `determine`; an overdue stage matures | W1, W4 |
| W20 | a plea with a concession reward routed through the obstacle, tested **before** any grade cap is adopted | `roll.obstacle`, `_eff_determine` | **[UNVERIFIED]** | the plea's control: deny not best alone | W17, W19 |
| W21 | the robust five decisions as verb rows with their write-matrix cells: proofs, self or advocate, naming mortal enemies, the warrant duty, appear / evade / defy (P4 critic findings 11 and 12) | `verb_table.yaml`, `write_matrix.yaml`, `decision/options.py` | **[UNVERIFIED]** | each decision taken above zero over three seeds | W5, W6, W11, W19 |
| W22 | the forum stage on the same case | docket item's row | **[UNVERIFIED]** | a forum plea moves a row with no second case | W18, W19 |
| W23 | the legitimacy index (`cache.standing_index`), defined at the territory, zero cases refused | `queries/cache.py` | **[UNVERIFIED]** | an L ≡ 1 arm shows no draw difference | P4 Q2 and S-7 (see §5) |

### Group F: content and the remaining families

| id | build | lands in | covered by | flips | needs |
|---|---|---|---|---|---|
| W24 | expectations and poles for Schoenland and "faction x"; a Church goal engaging `solmund_orthodoxy` | `goals.yaml`, `rosters.yaml` | **[UNVERIFIED]** | a faction no longer reads zero for all 78 | none |
| W25 | membership contests (admission, expulsion, precedence) | design first | B10-19 (design-first) | family 16 above zero | W7 |
| W26 | trade and levy (a market, a toll, a tax) | design first; needs a verb | B10-19 | family 17 above zero | W8 |
| W27 | a reader for a yielded duel (`surrender_of`) | `loop/effects_combat.py` | **[UNVERIFIED]** | a yield changes a body or a stance | none |

### Group G: retirement

| id | build | lands in | covered by | flips | needs |
|---|---|---|---|---|---|
| W28 | delete the kernel `systems/social_contest/sim/contest/` last, with its six or seven repointed tests; keep the `social_contest` contract row | repository | SC-05 (B10-Z) | `sys.modules` after a season holds no `systems.social_contest` | W17, W5, W19 landed |

---

## 3. The order

```
 0  answer-first ladder (§5)
 1  CORE        W1 → W2, W15, W4        (one file cluster: effects_information.py, matter.py)   ∥   W5 (cast, rosters)
 2  DELIVERY    W6                       (gate: ED-IN-0292 (1))
 3  SITES       W7 → W8 → W9, W10, W11  (gate.py and _disposal: one batch by shared file)
 4  INTAKE      W12 → W13, W14, W16     (queries, choose)
 5  CASE        W18, W19, W17 (verify) → W20, W22
 6  CHOICE      W21, W23
 7  CONTENT     W24, W25, W26, W27     (W25 and W26 are design-first and may move to B10-19)
 8  RETIRE      W28
```

- **Batches 1 and 2 are independent of each other** except that W11 (batch 3) needs both. Batch 1's W5 is a separate lane and
  may run in its own worktree.
- **Group by shared file, not by topic** (the plan's own rule for batch sizing): batch 3 is one batch because W7 to W11 all
  edit `gate.py` and `_disposal`.
- **Where this meets the active plan:** batch 1 is B10-13's head (CP-T05-01 to 03, SC-04); batch 3 reaches into B10-17
  (CR-35 to CR-37) and B10-09 (IN-61); batches 4 to 6 are new positions; batch 7's design-first items are B10-19; batch 8 is
  SC-05. A re-cut means moving CR-35 to CR-37 ahead of B10-13's tail, or building W7 and W8 inside B10-13.

### How each batch is built (`CLAUDE.md` §0.4, §10)

1. A `valoria-author` producer per disjoint file cluster, in a worktree, writing its head before it finishes reading;
   **no tier above Sonnet** except the two judgment nodes, W6's ruling text and W21's verb-row design (Opus).
2. The batch's observable is measured by `valoria-measure` (Haiku) re-running this folder's probes at seeds 0 to 2, once per
   batch, as a batch table, not per item.
3. `methodology-close` once per batch; the full suite once per batch, never per item. A red close re-runs the failing file only.

---

## 4. Acceptance: what must move, and its control

Read with C §5.3 and §2.3. Each row is zero today at seed 0 unless stated.

| observable | today (seed 0 / 1) | after | control arm (reproduces today) |
|---|---|---|---|
| `matter.determined` | 0 / 0 | above 0 over three seeds | the dial for W2 at 0 |
| `pursuit.moved` | 0 / 0 | above 0 | `pursuit_shift` 0 |
| docket items naming a row | 0 of 10 / 0 of 5 | above 0 | W1 off: arrangement `None` |
| docket items holding a date and a matter | 0 | above 0 | no RL1 stamp |
| `give` executed, `record.given` | 0 of 7, 0 | above 0 | `give` unformed |
| `compliance.given` | 0 / 0 | above 0 | no `give` |
| forged sheets with a second holder | 0 of 45 | above 0 | no `give` |
| `arrest.made` | 0 / 0 | above 0 | W11 off |
| persons with capability | 0 of 78 | 78 | faculty table absent |
| `matter.lapsed` | not emitted | emitted | W4 off |
| opinion of Schoenland and "faction x" | all 0.0 | a spread | W24 off |
| hand-built route 4 (C §5.5): legitimacy estimate of a judge | +0.02 to +0.066 | unchanged or larger | `judged_gain` 0 |

**Hash churn is declared, not hidden.** W1, W5 and W17 move every computed roll or every docket item and are declared movers;
W2 to W4, W7 and W12 should be EQUAL at their control arm. A re-recorded golden is said plainly (`CLAUDE.md` §7). Any batch
that re-pins depends on the pin and interpreter mismatch already on `main` (the pins pass under Python 3.13 and fail under
CI's 3.11); that is parked, as instructed, and is named here only because a re-pin recorded on the wrong interpreter would
be wrong.

---

## 5. What reaches Jordan, after the answer-first ladder

`CLAUDE.md` §0 says answer a pending decision as superseded, irrelevant, answered by a document, answered by precedent, or
by what suits the architecture, before escalating. Applied to the owed questions:

| question | ladder result |
|---|---|
| ED-IN-0292 (1): may a computed `give` complete, or a writ be minted to its addressee? | **survives.** It says "for now", so it is open by its own words; two defensible options lead to different games (a world where writs can be delivered, and one where they cannot) |
| ARM G2: the Layer-1 §A.3 wording for office weight | **survives**: it would overwrite ratified Layer 1 (R-31 contradicts §A.3), and it blocks every office weight |
| P4 Q1, church judging reach (a `scope:` key) | answered by what suits the architecture: take it (the church cannot judge outside T9 otherwise, and R-36's own example is a heresy case in weak-piety land). Record the reasoning |
| P4 Q2, may the draw read a barrier index built from residents' ledgers (F8) | **survives only if W23 is built**; W23 is last, so defer the question to batch 6 |
| P4 Q3, attributes into the roll | answered by a design document: `_part6.md:33` (M2) rules faculty derived at read; P4's critic finding 17 says drop it |
| P4 Q4, the ceiling's value | probably answered by B10-08 (CLOSED, "one ceiling"); verify its value against R-37's 3 before asking |
| P4 Q5, "a royal person is involved" | answered by P4's own default (a party), with the revert named |

So two questions reach Jordan before batch 3, one before batch 6.

---

## 6. Risks and stop conditions

- **A batch that closes with its observable still zero stops the run** (`CLAUDE.md` §0.2); it does not proceed to the next.
- **The built-direction trap.** C's hand-built control shows routes 1 and 2 close when `determine` fires, so a batch that makes
  `determine` fire in a hand-built world has proved nothing about computed play. The observable is always the computed probe.
- **W17 may already be done.** B10-08 is CLOSED; if its continuous path equals P4's closed form, W17 is a test and W20 starts
  earlier. If not, W20 to W23 wait.
- **Apparatus.** P4 is the most apparatus of the four proposals and its critic held its narrow options (judge challenge, forgery,
  impugn, cite-licence, the term of grace) until the explanation contract can show a player why they matter. They are not in
  this ledger.
- **Not covered by this plan:** the played-contest pause (where the season waits for a player, C §5.6); the Godot port; the
  campaign-level balance instrument (`CLAUDE.md` §7 names it an open gap).

`[CONFIDENCE: medium]` on the grouping and order, which are mine; `[CONFIDENCE: low]` on every **[UNVERIFIED]** coverage
cell, which is a search of an index and not a reading of the positions.
