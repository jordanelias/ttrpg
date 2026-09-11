# ONE SPINE FOR EVERYTHING THAT REMAINS — Arc 1 / Arc 2 / Arc 3 resequenced

## Status: PROPOSED (ED-IN-0212)
## Owner: infrastructure / cross-cutting (IN lane)
## Supersedes: nothing. AMENDS the ORDER in `workplans/2026-09-09-layer1-conformance-plan.md`
## (Arc 2's unit cut) and `workplans/2026-09-09-r-execution-plan.md` (Arc 3's sequence). Both
## remain the single owners of their units' CONTENT; this document owns only the order across them.

**Why this exists, in Jordan's words:** *"adjudicate across Arc 1/2/3 to determine the best dependency
order so that we can just build sequentially rather than hopping around … plan how to do this work
holistically from a top-down perspective that obeys code architecture."*

**How it was produced.** The adjudication was run read-only by Fable 5.1 against the working tree
(`CLAUDE.md` §10: `fable` on the audit/planner node, never on synthesis or artifact authorship); this
write-up is Opus's, per the same ruling. Every load-bearing claim below was re-verified against the
tree by the author before being written down — three were checked by hand and are marked ✓ where they
corrected something this session had already said out loud.

---

## 0. WHAT IS ACTUALLY BUILT — verified 2026-09-11, not quoted from a plan

| | state |
|---|---|
| **Arc 1** (L0–L5, Layer-1 structure) | **LANDED on `main`.** `decision/`, `loop/` (driver + six steps), `manifest/`, `seam/` (+`wrappers/`), `queries/`, `state/` are all directories on `origin/main` @ `5a35084`. |
| **Arc 2** (the gate contract) | **NOTHING IS IN THE TREE.** No `Receipt`, no `NoOpReceipt`, no `NotYours`, no `Token`, no `Act.via`; `state/` is `carriers.py ids.py world.py`; the gate is still `World.write(thing, wclass, apply, …)` at `state/world.py:295`. No PR for any of G1–G4 has ever been opened. |
| **Arc 2, in the RECORD** | ✓ **but "not started" is wrong, and this document corrects a statement made earlier this session.** `registers/handoffs/HANDOFF_IN.md:86` carries *"⏸ ARC 2 / G1 — HELD 2026-09-10"*: a G1 pre-flight that found a **live game defect** (`loop/matter.py` emitted `term.matured` carrying a `StateChange` to `(Record, stages)` and applied no write at all — `ID-9`'s worked example, live, and against the one field `write_matrix.yaml` forbids MATTER to touch), obtained **a Jordan ruling** (*add `Record.matured`, write it at MATTER*), implemented it, measured it (hash `ee0383bf…` → `b20dad27…`, `PROBE FLIPS 0`) and **backed it out** on one unexplained control. G1 has a ruled, unlanded first step and an open *measurement* question — not a ruling question. |
| **Arc 3** (U1–U10) | Three units landed on `claude/repo-workplans-state-xk44q2` (unmerged, PR #395): `11ec43c` U4/R-08, `d0165b5` `release`, `2ebab0c` U2/R-03. **U1/R-09 is uncommitted in the working tree.** U3, U5, U6, U7's remainder, U8, U9, U10 untouched. |
| **THE NINE** | `python -m engine.season.harness.register --requirements`: **1 met (R-03) · 5 not_met · 3 partial.** R-03 was flipped by U2 on an execution, which is the only kind of flip `CLAUDE.md` §0.2 accepts. |
| **W28 `cast:` blocks** | ✓ **0 of 143 cases carry one.** No plan schedules the authoring, and U8 and U9 are both hard on it. |

---

## 1. THE SPINE

Sixteen positions. Each says what makes it not-earlier and not-later. **Positions 2–6 are Arc 2,
re-cut into five units rather than four** — see §3 for why the original cut is short.

| # | unit | not earlier because | not later because |
|---|---|---|---|
| **0** | **U1 — finish, re-pin, commit, land** | it is in the tree uncommitted and the suite is red on it; nothing measures cleanly on top of a red tree | every degree consumer is downstream, and R-09 `not_met → partial` is the arc's first row move |
| **1** | **U3 / R-06a** — 13 convictions × 4 axes, the projection into `make_chooser`, the axis swap, 27 alignment cells | free now; nothing blocks it | U4 already landed **on the sparse table U3 fixes**, so R-08 and R-06 sit `partial` on exactly this. It touches no write path, so it is immune to Arc 2, and its hash move is attributable before Arc 2 starts moving the hash for other reasons |
| **2** | **G1a** — `state/acts` · `Receipt` · `state/gate` minting it · `log.append` asserting causes ∈ `log ∪ acts ∪ {ROOT}` and receipts ∈ the minted set · the ruled `Record.matured` fix, with the H-80 control re-derived first · the two body-literal Event kinds declared | U1 and U3 should be pinned before the first Arc-2 hash move so that move is Arc 2's alone | G2/G3/G4 mint into it, and **every effect written after it is written to the right contract once** |
| **3** | **G1b** — delete `Event.subject`; witness and epistemic read the actor through `causes[] → state/acts` | needs the act store | it moves the content hash and should ride G1a's move rather than open a third |
| **4** | **G2** — one `Token := (write_class, tick)`, minted in `loop/driver` only; the AST scan; **33 `.write(` call sites** rewritten | one signature, rewritten only after G1a returns receipts | G3's check reads the token's class |
| **5** | **G3** — AX-4 clause 2 at the gate (`NotYours`), **`Act.via`**, and `_eligible` / `under_purview` / `_req_revoke` / `_req_confer` re-pointed from actor-purview to `via.scope` | token + receipts | U7-remit and U9 consume `via`; the purview readers are rewritten exactly once here |
| **6** | **G4** — `NoOpReceipt` at the gate, converted to the row's refusal at the fold boundary; the effect contract finalised | needs `before`/`after` from the receipt | U5 and every U7 effect are then written to a finished contract |
| **7** | **U5 / R-07** — `stance_delta`, `_eff_tell` writes `Person.stance`, `stance.moved` | degree (U1) + contract (G4) | U6 needs it |
| **8** | **U6 / R-01+R-02** — the first measurement | U1, U2, U4, U5 all in; Arc 2's hash moves behind it, so the number is Arc-2-clean | before U7, so the verb set is stable when it is taken |
| **9** | **W28-cast** — author the `cast:` blocks, NPC lane first (46), `WAITS-ON-PLAYER` for player entries | order-free (pure authoring); placed here so its effect on R3 is measured against a stable loop | U8 and U9 are hard on it, and nothing has started it |
| **10** | **U7-own** — the `own`-eligibility verbs, in pairs: `commit`+`repudiate`, `forge`, `oblige`, `tie / knot`, `succeed`, `restore`, `exchange`, `destroy_record` | after G4, so each effect is written once | U9's "an arc ends" wants them; U8's ambitions read `commit` edges |
| **11** | **Record-kind fold** (Petition/Dispensation become kinds of `Record`, `04:180`), then **U7 `petition` + `carry`** | schema before verb | precondition for `rescind`/`withdraw` |
| **12** | **U8 / R-06b** — `ambitions(p)` and `build_at` from the cast | the cast (9) | U9 |
| **13** | **U7-remit** — `levy`, `establish`, `open_case`, `determine`, `issue` | G3, for `via.scope` | `levy` executing **with `Act.via` set** is U9's own observable |
| **14** | **U9 / R-04** — `faction_q`-shaped queries, `scale_of_rung`, the 44 re-scales, the 10 world cases | G3 + U8 + U7-remit | the last structural unit |
| **15** | **U10** — second measurement; `measured:` lines from instrument output only | everything above | — |
| **off-spine** | **U7-disp** — `comply`, `evade / defy`, `refract` | — | **genuinely Jordan's.** ED-IN-0210's fork (*does an order carry terms?*) is the one remaining node that survives all five of §0's tests. Do not schedule it until ruled |

**Where two units were order-free, that is said and a choice is still made** — the ask was a spine, not
a lattice. U3 is order-free against Arc 2 (picked first so game yield lands even if G1a stalls on the
H-80 control); G1b is order-free against G2–G4; W28-cast could sit anywhere before position 12.

---

## 2. THE EDGES — hard, soft, and the ones no plan names

### Hard (the later cannot be built, or cannot be correct, without the earlier)

- **G1a → G2 → G3.** `04 §C.2:523` has clause 2 read the token's class *and* the caller's `actor`/`via`;
  `04:583` spells `gate.write(…, actor=a.actor, via=a.via)`. There is nothing to mint into today —
  `world.py:441` constructs the Event and `resolve.py:353` builds `StateChange`s *after* the write.
- **G3 → U9.** `Act` has no `via` (`state/carriers.py:323`); `04:930` row 1: *"a seat enters **only**
  through `Act.via`"*; `04:330`: *"every purview walk uses `via.scope`"*. H-108 is the row.
- **W28-cast → U8 → U9.** 0 of 143 cases carry a `cast:` block.
- **Record-kind fold → U7 `petition`/`carry`.** `04:180` rules them *kinds of `Record`*; the store
  carries them as separate dicts (`world.py:164`) and `carry`'s typed cell is `kind: Petition`.
- **U1 → U5 → U6.** U5's write is degree-keyed; U6 measuring R-01/R-02 before a degree producer exists
  measures the theorem, not the game.

### Two hard edges **no plan names**, found by reading the tree

- **G1a needs an ACT STORE.** `04:799` has the append assert *every cause in `log ∪ acts ∪ {ROOT}`*, and
  `04:1044` puts the act store in step 3. Today `causes=[a.id]` names ids that are **never in `w.log`**
  — `resolve.py:283` says so in as many words — and the only record of an act is the driver's
  `act_of`/`resolved` dicts. **A G1 that lands the append assertion without the act store rejects every
  act-caused Event in the corpus.**
- **`Event.subject` is the actor field `04:402` forbids, and it is live.** `epistemic.py:262`: *"Every
  fold-emitted Event sets `subject = a.actor`."* It is read by `witness.py:190` (the whole `actor`
  observation mode), four sites in `epistemic.py`, `world.py:487` (the MATTER clock chain) and
  `world.py:559` (the content hash). Removing it is not a field deletion — it is the attribution
  mechanism of `04 §C.6` being built. That is **G1b**, and the conformance plan lists it as a gap
  (`:109`) and then assigns it to no unit.

### Soft (tidier, or avoids editing the same lines twice)

- **G3 → U7-remit.** `_eligible`'s `remit:` branch reads authority off the *actor's own* `hold` tenures
  (`resolve.py:52`), as do `under_purview` and `_req_revoke`. Predicates written before G3 are written
  against actor-purview and rewritten after. Execution works either way, so soft for the corpus and
  hard for *write it once*.
- **G1a/G4 → every unit that writes an effect.** Effects mutate **inside the gate's `apply()` closure**
  and return touched ids (`effects.py:96`). `04 §C.2:536` has the gate take the `change`, apply it, and
  compute `before`/`after` itself. A value-level `NoOpReceipt` cannot be computed on an opaque closure
  whose targets are known only afterwards — so G1a/G4 change **the contract all 11 existing effects are
  written to.** Eleven are already on the wrong contract; U7 would add up to fifteen more.

### Plan claims the tree does not support

- **"U7 groups 1–2 are startable on `main` today"** is true only of the `own`-eligibility rows with no
  Petition operand. It is false for `levy`/`establish`/`open_case`/`determine` (remit → G3) and for
  `petition`/`carry` (the Record-kind fold). U7 splits by **eligibility kind**, not by W31 group.
- ✓ **"G3 merged" and "`Act.via` is LANDED BY G3"** in `r-execution-plan.md:1586`/`:1592` are
  **preconditions written in the past tense**, and they were read as status this session. Corrected in
  that file in the same commit as this one.
- **"Arc 2 is zero game yield, declared"** is false in one respect — see §3.

---

## 3. WHERE ARC 2 BELONGS — the position taken

**After U1 lands and after U3; before any unit that writes an effect. Not payable late. Its scope is
under-cut, not wrong.**

- **Not late.** Every remaining Arc-3 unit except U3 and U8 writes effects, Events, or purview
  predicates — U5 (one effect, one emit kind), U7 (5–15 effects), U9 (`levy` through a seat). Those are
  exactly the surfaces Arc 2 rewrites. Paying Arc 2 after them is the second payment of the defect the
  conformance plan already diagnosed for Arc 1: the same lines edited twice, plus the guard-blinding
  recurrence it measured four separate times.
- **Not before U1/U3.** Both are already substantially landed on the pre-Arc-2 contract and neither
  writes an effect; their hash moves deserve their own attribution.
- **It is not zero game yield.** G1's pre-flight found a live `ID-9` defect in MATTER — an Event
  reporting a change that did not happen — and Jordan ruled the fix. Arc 2 carries a ruled game repair
  on its first step, and its subject is Layer-2 game code against a ratified axiom, so it passes
  `CLAUDE.md` §0.1 pt 5's predicate. It is not the apparatus loop §0.3 warns about.
- **Its scope is short by three items and one blocker:** the act store, the derived kind roster (or a
  declared kind-unchecked append), `Event.subject`, and the H-80 chain-length control that stopped G1 —
  **a measurement question, not a ruling.** G1–G4 becomes G1a / G1b / G2 / G3 / G4.

**Alternative considered and refused:** U5 + U6 before Arc 2, for the earliest R-07 flip and the first
R-01/R-02 number. It costs one effect written twice (small) — but U6's number is then invalidated by
Arc 2's three declared hash moves and needs a *third* measurement before U10. That is precisely the
hopping this document was asked to end.

---

## 4. WHAT THE ARCHITECTURE FORCES THAT A UNIT LIST CANNOT SEE

1. **`04` PART E's critical path is `0→1→2→3→4→5→6→7→8` (`:1036`), and the tree built 4–8 and 10 before
   3.** Arc 2 *is* step 3 (`04:1024` — stores with private setters, the gate, the four tokens, the
   receipt mint, the log, the ledgers, **the act store**, `World`). Every Arc-3 unit is step 6–8 work
   stacked on an unbuilt step 3. **The spine above is PART E's own order, applied to what is left.**
2. **The gate's signature IS the effect contract.** This is the single architectural fact the
   U-numbering cannot see, and it makes *how many effects exist when Arc 2 lands* the multiplier on
   Arc 2's cost.
3. **`04 §B.7:330` — purview is asked of the seat exercised, never of the actor.** The verb table's
   eligibility axis (`own` vs `remit:*`) is what predicts whether a verb depends on G3. The R-plan
   groups U7 by an axis that predicts nothing here.
4. **Lines edited twice under the current order and once under the spine:** the eleven effects in
   `loop/effects.py`; `under_purview` and the `_req_*` predicates; every `Event.changes` reader.
   Unavoidable either way: `loop/resolve.py` and `loop/witness.py`, at different lines.

---

## 5. MODEL TIER PER NODE (`CLAUDE.md` §10)

Arc gates (end of Arc 2, end of Arc 3) go to `fable` with a read-only `valoria-critic` — the audit and
guardrail node, never the producer. Escalate at unit boundaries only (caching fact 3). `haiku` is for
citation and line-number extraction inside a unit, never as a producer here.

| node | producer | critic | note |
|---|---|---|---|
| U1 finish | `opus` | `opus` | the third-gate amendment and the re-pins are judgment, and being wrong here is silent |
| U3 | `sonnet` | **`opus`** | the 52 cells are transcription; the projection, the `Precedent` two-sense collision and a corpus-wide hash move are not |
| G1a · G1b · G2 · G3 · G4 | `opus` | `opus` | contract migration; an unminted receipt that passes is a silent error. G2's 33-site rewrite is a `sonnet` sub-stage |
| U5 | `sonnet` | `opus` | no byte-identity control exists, so the critic carries the weight |
| U6 · U10 | `sonnet` | `opus` | running is mechanical; **reading the number is the judgment** |
| W28-cast | `sonnet` | `opus` | authoring against a schema; the critic checks the `WAITS-ON-PLAYER` split |
| U7-own | `sonnet` | **`opus`** | a green 190-test suite already missed two findings in this family |
| Record-kind fold · U7-remit · U9 | `opus` | `opus` | schema, purview-through-seat, and the scale vocabulary |
| U8 | `sonnet` | `opus` | as planned |

---

## 6. THE HONEST COST

**What the spine pays that the current order does not.** Five Arc-2 units before R-07 and before the
first R-01/R-02 number — game yield is deferred by roughly the length of Arc 2. Three declared content
hash moves inside Arc 2 (`Record.matured`, `Event.subject`, the no-op refusals); **the hash stops being
the control at G1a**, and each unit must declare its own before/after. Every Arc-3 golden already
pinned is re-pinned once more. And the plans' only parallel lanes (U3 ∥ U7-own ∥ W28 authoring) are
serialised deliberately, because a spine is what was asked for.

**What it gives back.** Every effect, every purview predicate and `Act.via` written exactly once. No
fourth guard-blinding recurrence from moving write sites after they have multiplied. U6's number
measured on a write path that will not change again before U10. And U9 stops being *"the only
structural blocker"* and becomes the last unit on a path whose every predecessor is named.

**Risks, named rather than filed.** G1b can silently vacate the witness's actor channel — plant a
belief write and watch the negative assertion go red before trusting it. G3 must not be weakened to
keep `confer` / `revoke` / `kill / wound` green; declaring a `T-o` basis with `via` present is the fix,
and it will red every hand-built `Act` in the probes and tests that writes another's tenure without a
seat. W28-cast is the long pole for U8/U9 and is content authoring, not engineering.

---

## 7. HELD BACK FROM RATIFICATION-ON-MERGE (`CLAUDE.md` §2, ED-1094)

Merging this PR ratifies **the order in §1 and the position taken in §3**. Three things are
**explicitly held back** and must not be read as ratified by the merge:

1. **The Arc-2 re-cut into five units (G1a/G1b/G2/G3/G4)** changes the unit boundaries in
   `workplans/2026-09-09-layer1-conformance-plan.md`, which is that document's to own. This proposes it;
   that plan should absorb it.
2. **`U7-disp` staying off-spine** rests on ED-IN-0210's fork being genuinely Jordan's. If it is not,
   the node returns to the spine between positions 10 and 11.
3. **Nothing here reschedules PART E steps 0 and 2** (typed ids with an owned `H`; one loader with
   twelve invariants). ED-IN-0206 records them; neither arc carries them; no R-row's `measure:` moves on
   them. `[GAP: PART E steps 0 and 2 — unscheduled by design, not by oversight]`
