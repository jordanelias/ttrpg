# THE RECONCILED PROGRAM — part 2: the instruction and the compliance clause per position

## Status: PROPOSED (ED-IN-0215)
## Reads after `2026-09-11-reconciled-program.md`. That file owns the ORDER and the supersession
## verdict; this one owns the per-position detail. Unit CONTENT still belongs to its own owner.

**How to read a position.** `INSTRUCTION` is what a session does from cold. `LAYER` is decided by
**who the output constrains**, not by the directory it lands in (`skills/layer-conformance` Lens A1).
`COMPLIANCE` quotes the Layer-1 row the position must satisfy, **verbatim, with its line** — every
quotation below was re-read at its cited line by the author. `OBSERVABLE` is the execution artifact
that makes it done (`CLAUDE.md` §0.2 — never a `## Status:` line) and `FALSIFIER` is the test that
would have shown it wrong (§0.1 pt 3). `TIER` is per `CLAUDE.md` §10.

⚠ **Lens B does not run on every position.** It runs only on Layer-2 code against a Layer-1 row, and
`04_CODE_ARCHITECTURE.md`'s own Status line scopes it to `engine/season/`. For `systems/combat/`,
`systems/mass_battle/` and `systems/threadwork/` the governing surface is that subsystem's head plus
`holonic_container_doctrine_v1.md` — **which is CANONICAL but is not Layer 1.** Grading against it is
fine; reporting the result as a Layer-1 verdict is not.

---

## 8. THE POSITIONS

### 1 · CLOSE-PASS
**not earlier** nothing precedes it · **not later** every subsequent session otherwise opens 108 rows,
and §5's ruling batch is unreadable until the queue visibly holds ~12.

**INSTRUCTION.** Edit the eight `registers/editorial_ledger*.jsonl` files holding the ids in §2.1.
Per row: `status` → `superseded`/`closed` (both already in the live enum), `needs_jordan` → `false`,
and append the closing citation **in the row's own text** — ED-IN-0204 Decision 1 for the retained-lane
closures, ED-SC-0033 for the 17 SC rows and docket D5, `CLAUDE.md` §0/§0.05 for ED-IN-0113/D1. The 10
authorial rows get `needs_jordan: false` and an authorial note, **not** closure. Ride-alongs, one line
each, same commit: `return_to_game_queue.yaml`'s stale *"WHAT TO READ INSTEAD"* → `CLAUDE.md` §1 +
`HANDOFF.md`; strike `HANDOFF.md:463-469`'s *"THE STEP TO TAKE: S7"*. **Do not touch
`tools/m1_acceptance.py`** — §0.1 pt 5 forbids re-tooling a board reader.

⚠ **THE `CLAUDE.md:95-96` EDIT IS REMOVED FROM THIS POSITION — the antagonist pass was right and the
finding is worth keeping in full.** The first draft rode along an edit repointing *"traces to an open
M1 juncture"* at *"an R-row of `requirements.yaml` **or a position here**"*. Three things wrong with
it. (1) It is a **Layer-0 governance change** to RULED text whose rationale is attached at
`CLAUDE.md:100-101` (*"without the first the literal reading tells a session to refuse Jordan"*),
bundled as "one line" inside a 97-row closure commit — exactly what §2 forbids. (2) The moment
`CLAUDE.md` points at *a position here*, **this workplan constrains what a session may work on** and
becomes Layer-0 content living in `workplans/` — under Lens A1 the layer follows who the output
constrains, and part 1 §0's *"delete it and the game behaves identically"* becomes the wrong test:
delete it and a session can no longer tell what its work is. (3) That is a working instance of the
T3 channel §0.3 names — findings → a surface → the surface defines the next session's work — with
`workplans/` as the surface. **If the M1-juncture binding needs repointing, it points at
`requirements.yaml`'s R-rows, which code reads, and it is Jordan's edit to make, not a ride-along.**

**LAYER 0** — it binds the agent's queue. Lens B does not run.
**COMPLIANCE.** `CLAUDE.md` §0: *"**Escalate only what survives all five.**"* and *"clearing the
standing queue is session work — find a stale `needs_jordan` on a settled question and CLOSE it with
its citation."* ED-1094 requires the flip land in the same merge, *"not as a later step nobody
triggers."*
**OBSERVABLE.** The count of `needs_jordan: true ∧ status: open` across all ledgers goes **108 → ≤ 12**,
printed in the commit message with the command that produced it; `validate_ed_citations.py` 0
violations. **FALSIFIER.** An independent read-only critic samples 10 closures; any row whose cited
successor does not itself name that row's subject is a wrong closure, and **any row closed under test
1 whose lane ED-IN-0204 Decision 1 *retained* (SC/PC/MB) is wrong by construction.**
**TIER.** producer `sonnet` (yes/no against a named test, per row); critic `opus` on a 10-row sample —
the surface is Jordan's queue, so §0.1 pt 5 makes it load-bearing on a Jordan decision and a wrong
closure is silent. `haiku` rejected: 97 JSONL edits each needing the row's own text read is not
deterministic extraction, and its 4,096-token cache floor makes the fan-out no cheaper.

### 2 · RET-SC — the ruled `systems/social_contest/` retirement
**not earlier** than 1, which closes the 17 SC rows whose subject this retires · **not later** it is the
repo's standing "ruled and unexecuted" instance and touches no engine-spine file.

⚠⚠ **STEP (a) AS FIRST WRITTEN IS WRONG. PRE-FLIGHT RUN 2026-09-11, AGAINST THE CODE RATHER THAN THE
PLAN, AND IT OVERTURNS THE PREMISE.** Four measurements:

1. **`seam/ladder.py` HAS NO `veto` PARAMETER.** `degree_of(result, subject)` at `:138` is the whole
   signature. The `degree(margin, veto?) -> Degree` on `ladder.py:2` is a **docstring quoting `04`'s
   spec**, not a built thing — so `04:681-682`'s `veto=provider.veto` shape is specified and unbuilt.
   Relocating the rule "as a veto" would first require building a Layer-1 parameter, which is a unit,
   not a step.
2. **THE SEASON LOOP NEVER REACHES THE RULE.** `rg 'PoolDesaturation|degree_extension|BandExtension'
   engine/season/` returns **zero**. So moving it onto the game path does not PRESERVE a behaviour —
   it **ADDS** one, and would move the content hash. That is a behaviour change wearing a
   relocation's clothes, which is the `U3a` failure this tree already reverted once.
3. **`engine/autoload/sigma_leverage.py` DOES NOT IMPORT IT** — comment-only, at `:114` and `:339`,
   both recording that `ED-SC-0032` moved the rule OUT of the engine deliberately, on Jordan's
   2026-08-15 ruling that a subsystem's band modification belongs to the subsystem. A grep that
   counts those comments as consumers is term-matching, not reachability.
4. **THE REAL BLAST RADIUS IS SIX IMPORTING FILES, AND NONE OF THEM IS THE GAME:**
   `engine/tests/test_sigma_leverage_parity.py:52` · `tests/valoria/test_band_extension_seam.py:133` ·
   `tests/valoria/test_balance_oracle_arms.py:65-66` · `tests/valoria/test_degree_ladder_single_owner.py:138` ·
   **`tools/balance_oracle.py:153-154`** · `proposals/2026-09-04-degree-sweep/arm5_social.py:55`.

**SO THE RULE IS NOT LIVE ON THE GAME PATH; IT IS LIVE ON THE MEASUREMENT PATH, AND THAT CHANGES WHAT
THIS POSITION RISKS.** Deleting `systems/social_contest/` does not orphan a game rule. It orphans an
arm of **`tools/balance_oracle.py`** — the campaign-level balance instrument `CLAUDE.md` §7 designates
for balance questions — plus the σ-leverage parity test. Losing an instrument quietly is worse than
losing a rule loudly, because the next balance claim is then made with no control (§0.1 pt 4).

**INSTRUCTION — step (a), corrected.** Decide the rule's HOME before deleting, and the choice is not
between "engine" and "subsystem" but between three: (i) it belongs to **proceedings**, the ruled owner
of all social contests, and therefore waits for position 22 — in which case this position must NOT
delete `degree_extension.py` and the retirement is partial; (ii) it is a **general de-saturation** and
returns to `dice_engine` as a `BandExtension` the ladder already types, which contradicts Jordan's
2026-08-15 ruling and needs his word; (iii) it dies with the kernel and `balance_oracle`'s social arm
dies with it, which must be **stated in the commit**, not discovered later by a balance question that
returns nothing. ⚠ **(i) is the reading this document takes**, because ED-SC-0033 named proceedings
the owner and nothing has transferred the rule yet. Under (i), step (b)'s `git rm` is scoped to
everything EXCEPT `degree_extension.py`, and the file moves at position 22.
(b) `git rm -r systems/social_contest/` — under reading (i), **less `degree_extension.py`** —
**28 tracked files** (`git ls-files`): 21 `.py` and 7 `.md`. ⚠ **Do not use a `find` count.** The
directory reads 46 or 47 depending on `__pycache__` churn, which is why ED-SC-0033's "47" and an
earlier draft of this document's "46" disagree while nothing was edited. A number that moves when
nobody changes anything was never a measurement (§0.1 pt 4); `git ls-files` is what the command acts
on. (c) Write the `FORK:` row in
`references/restructure_ledger.md`. (d) Repoint every inbound site: `module_contracts.yaml`,
`canonical_sources.yaml`, `descriptor_registry.yaml`, `lane_assignments.yaml`,
`ci_checks_registry.yaml`, three `skills/` files. **Keep the logical name** — `rosters.yaml`'s prize
rows key on it and ED-SC-0033 clause (2) makes the repoint a row change when proceedings lands.
(e) Re-run every exporter's `--check`; fix the `engine/tests/` cases that import the retired package.
(f) `tests/valoria/test_engine_does_not_import_systems.py` uses a `systems.social_contest` symbol as a
*fixture* — re-point it to a surviving one.

**LAYER.** The deletion and repoints constrain the repo (Layer 0 / Layer-1 scripts); **the relocated
`veto` constrains the game → Layer 2**, and Lens B runs on that part only.
**COMPLIANCE.** `04:164` — *"| `seam/wrappers/*` | **nothing, ever** | the projection | a `Margin` |
**none** |"*. The relocated rule must therefore be a veto that can only demote, never a re-banding.
**OBSERVABLE.** `rg -n social_contest engine/ tools/ tests/ references/ skills/` returns only the
logical-name rows; content hash **stationary** and `PROBE FLIPS 0` — the interim provider's bands must
not move. **FALSIFIER.** Plant a `tell` contest that the old extension demoted, at a pool where it
would otherwise read `Overwhelming`; confirm red before the move and green after.
**TIER.** producer `sonnet` (bounded path surgery); critic `opus` on the `veto` relocation only — the
one behaviour-carrying edit. `haiku` for the inbound-site census: deterministic `rg`, and the tier drop
pays against a one-command handoff.

### 3 · G1a — the act store, `Receipt`, `state/gate`, the `log.append` assertion
**not earlier** U1/U3 are pinned so the first Arc-2 hash move is Arc 2's alone · **not later** G1b–G4
mint into it, and every effect written after it is written to the right contract once.

**INSTRUCTION.** Start from the held G1 record in `registers/handoffs/HANDOFF_IN.md`. **The
measurement first**: re-land the ruled `Record.matured` write and decide the H-80 control — either the
pin is stale because a gate-emitted maturation legitimately joins the chain, or `causes=[prior]` must
differ for one. Record which, with the three-arm numbers. Then `state/acts.py` (append-only);
`state/gate.py` owning `write(...) -> Receipt`, moved off `World.write`; `Receipt` replacing
`StateChange` in `Event.changes[]` (five construction sites, two outside the gate); `state/log.py`
whose `append` asserts causes ∈ `log ∪ acts ∪ {ROOT}` and receipts ∈ the minted set. Ride-along: amend
the spine's spent §0 table and `HANDOFF_META_ARCHITECTURE.md:3`.

**LAYER 2.**
**COMPLIANCE.** `04:1024` step 3 owns this position: *"the stores with private setters · the gate ·
the four tokens · the receipt mint · the log · the ledgers · the act store · `World`"*. And `04:1036`
— *"**Critical path: 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8.** Step 8 is the bar; nothing after it is on
the path."* — which is why this is the pivot: the tree built 4–8 and 10 before 3.
**OBSERVABLE.** A hand-built receipt in an Event fails `append`; the same Event with a gate-minted
receipt passes. One declared hash move (`Record.matured`), with `PROBE FLIPS` named per probe.
**FALSIFIER.** An act-caused Event appended while the act store is **empty** must fail; if it passes,
the assertion is not reading the store.
**TIER.** `opus` producer, `opus` critic — an unminted receipt that passes is a silent error. The
`StateChange → Receipt` rename is a `sonnet` sub-stage once the type is fixed.

### 4 · G1b — delete `Event.subject`
**not earlier** needs the act store · **not later** its hash move should ride G1a's rather than open a third.

**INSTRUCTION.** Delete the field; rewrite its readers — `loop/witness.py`'s whole `actor` observation
mode, four sites in `epistemic.py`, the MATTER clock chain and the content hash in `state/world.py`.
Attribution now comes from `state/acts` via `causes[]`.
**LAYER 2.**
**COMPLIANCE.** `04:402` — *"**No `actor`, no `target`, no `subject` on `Event` — STRUCTURAL:** the
fields do not exist, and"* … `changes[]` carries the changed things individually. The field is live
today, so this is `04`'s own STRUCTURAL claim not yet being true of the tree.
**OBSERVABLE.** The witness still deposits a `did` claim on a co-located act; the document holder's
ledger still does not. **FALSIFIER.** Plant a belief write and watch the **negative** assertion go red
before trusting the channel — silently vacating the actor channel is the failure mode here, and a
passing suite does not see it.
**TIER.** `opus`/`opus`. Not delegable: the failure is a channel that goes quiet.

### 5 · G2 — one `Token`, minted in `loop/driver` only
**not earlier** one signature, rewritten only after G1a returns receipts · **not later** G3 reads the
token's class.

**INSTRUCTION.** `WriteClass` is today an enum passed as a parameter. Add `Token`, constructed in
`loop/driver.py` only; `gate.write` takes it. **Rewrite the 33 gate call sites** —
`harness/probes.py` 20 · `loop/matter.py` 6 · `loop/witness.py` 3 · `loop/calendar.py` 2 ·
`loop/resolve.py` 2. Reproduce with: `ast` walk over `engine/season/**/*.py` minus `tests/`, keeping
`Call` nodes whose `func` is an `Attribute` with `attr == "write"`, **grouped by receiver** — 33 have
receiver `w`, 9 have receiver `TRACE`. ⚠ **Those 9 are `trace_log.py`'s tracer, a different object,
and are NOT gate sites.** The spine's 33 was right; an earlier draft of this document reported 42 as
an overturn and was wrong (part 1 §7). Whether the tracer calls ride along is this unit's pre-flight
call, not a rewrite it inherits.

⚠ **AND THE SCAN CANNOT SEE THE ONE CALL THAT MATTERS MOST.** `loop/deliberate.py:67` calls
`w._rehome()`, which **mutates the tenure store during DELIBERATE — a barrier that owns nothing and
holds no token.** It is not a `.write(` site, so a `Token(`-construction scan lands green with the
violation intact, which is the property G2 exists to make impossible. `deliberate.py:20-29` records it
and rules it out of scope for the unit that found it: *"either it moves to the MATTER barrier or the
row is amended. That is a Layer-1 question, not this unit's. Found by the Fable gate on Arc 1 and
filed under `ED-IN-0206`."* **It is this unit's.** Disposition it in the pre-flight: move the call to
MATTER, or amend the `04` row and say which.

Add the AST scan for `Token(` construction outside the driver, with an asserted floor on what it
inspected — and a second assertion that DELIBERATE mutates no store **by any route**, not only through
`gate.write`.
**LAYER 2** (the scan is a Layer-1 script and is licensed: its subject is Layer-2 code against `04:206`).
**COMPLIANCE.** `04:199` — *"`Token      := (write_class, tick)                 -- constructed by
loop/driver and NOWHERE ELSE`"*. `04:206` — *"| only the driver mints a Token | MECHANICAL — a test
asserts `Token(` appears in `loop/driver` only | MECHANICAL, same scan; **GDScript has no private
constructors** |"* — note the two grades, and that only the Python one is in scope before position 26.
**OBSERVABLE.** Content hash **stationary**, `runs/` byte-identical — this is a pure signature move.
**FALSIFIER.** Two plants: a `Token(` in `loop/deliberate.py` must redden the scan; and a wrapper
calling `gate.write` must fail **for want of a token**, not for want of a matrix row — assert on which
error is raised.
**TIER.** `opus` for the type and scan; **`sonnet` for the 42-site rewrite** — mechanical against a
fixed signature, and the tier drop pays because the handoff is the `ast`-derived site list itself.

### 6 · G3 — `NotYours` at the gate, `Act.via`, purview through `via.scope`
**not earlier** token + receipts · **not later** U7-remit and U9 consume `via`, and the purview readers
are rewritten exactly once here.

**INSTRUCTION.** `Act` gains `via: Optional[SeatId]`. In `state/gate.py`, for a Tenure write, admit the
declared bases and otherwise raise. Re-point `loop/resolve.py`'s `_eligible` `remit:` branch,
`under_purview`, `_req_revoke` and `_req_confer` from the actor's own `hold` tenures to `via.scope`.
**Expect three live violations** — `revoke`, `confer` and `kill / wound` all write another's edge;
declare each as `T-o`-with-`via` or under its own basis.
⚠ **AND A FOURTH CASE THE FIRST DRAFT MISSED, added by the antagonist pass:** a **conferral-basis
opener** matches none of `§C.2`'s four admitted bases. `04_VERBS.md:352-357` files this as *"an `IN`-lane
defect this design reveals rather than causes"*, and position 19's `determine` needs it. Write it here
or it is written twice — this position is the only place the F3 branch is authored. **Do not weaken the check to keep them
green**: every hand-built `Act` in probes and tests that writes another's tenure without a seat goes
red and is fixed by giving it a seat.
**LAYER 2.**
**COMPLIANCE.** `04:529-534` — *"kind is Tenure => one of: / actor == subject(id) -- T-m, the owner's
discretion / cause is this Tenure's declared `term` maturation -- T-n / via is a Seat whose
`revocation` basis reaches it -- T-o, and `via` MUST be present / cause is an existence change this
same act caused -- destroy's cascade / otherwise raise NotYours"*. And `04:330` — *"| **purview is
asked of the seat exercised, not the actor** | MECHANICAL | `Act.via : SeatId?`; every purview walk
uses `via.scope`. **A regent has the seat's purview** |"*.
**OBSERVABLE.** A `revoke` with `via=None` is refused at the gate. The hash may move **only** where a
previously-lawful non-owner write is now refused — name each one.
**FALSIFIER.** A `T-o` write whose `via` names a seat whose `revocation` basis does **not** reach the
edge must raise. If it passes, the basis walk is still reading the actor.
**TIER.** `opus`/`opus`. The wrong answer is a quietly permissive gate.

### 7 · G4 — `NoOpReceipt` and the final effect contract
**not earlier** needs `before`/`after` from the receipt · **not later** U5 and every U7 effect are then
written to a finished contract.

**INSTRUCTION.** In the gate: compute `before`, apply, compute `after`; equal ⇒ raise `NoOpReceipt`,
converted at the fold boundary into the row's refusal kind. This **changes the contract all 11 effects
in `loop/effects.py` are written to**: today an effect mutates inside an opaque `apply()` closure and
returns touched ids; under §C.2 the gate takes the change and computes before/after itself. Rewrite
the eleven once — which is the whole argument for paying Arc 2 before U7 adds up to fifteen more.
**LAYER 2.**
**COMPLIANCE.** `04:536` — *"`  before = get(); store._set(); after = get()                             --
THE GATE APPLIES THE WRITE`"*, with the `NoOpReceipt` raise on the following line.
**OBSERVABLE.** `work` — refused in every world today — emits `site.worked` only when the delta is
non-zero. **This is the one Arc-2 clause licensed to move the hash**: each flipped probe must be named
and attributed to the no-op refusal, and a move anywhere else is a break.
**FALSIFIER.** Plant an effect that returns touched ids without mutating; it must produce a refusal
Event, not a success.
**TIER.** `opus`/`opus`. The 11 rewrites are judgment, not transcription — each decides what its
`change` is.

### 8 · H-98 — the general ladder branch's producer, and the wound-count band edges
⚠ **RESCOPED BY THE ANTAGONIST PASS. The first draft of this position was wrong on every branch, and
the way it was wrong is worth keeping:** it read *"the wrapper returns ±1/0 and throws away what it
computed"* out of `seam/wrappers/combat.py:43-47` — a docstring recording a claim that had **already
been struck** — and attributed it to the seam wrapper. That sentence is about `wrapper.fight` **inside
`combat_engine_v1`**, a different object. Term-matching the word *wrapper* across two objects is the
same failure as counting `TRACE.write` and `w.write` as one API (part 1 §7).

**not earlier** order-free against Arc 2 (wrappers hold no token), placed after G4 so its Events land
once on the finished contract · **not later** the non-combat contested verbs need a graded producer.

**WHAT IS ALREADY BUILT, and must not be rebuilt.** `seam/wrappers/combat.py:203-208` already returns
`wound_state` per party (`felled`, `wounds`, `max_wounds`, `health_remaining`, `health_full`), and its
own comment names it *"THE DEGREE SOURCE. A caller reads severity from here; it does not map it from
`winner`, which carries none."* `seam/ladder.py:151-152` already grades it: `if "wound_state" in
result: return combat_degree(result, subject)`.

**AND THE "FOURTH BAND" IS FORBIDDEN, not missing.** `ladder.py:81-82`: *"⚠ A FOURTH BAND (decisive vs
narrow) HAS NO SOURCE IN THE DATA and is NOT invented — that is the whole of what survives in `H-98`
after the 2026-09-03 ruling."* The first draft cited that ruling as its warrant while proposing the
thing the ruling removed.

**INSTRUCTION — the two things actually absent.** (a) **The general ladder branch has no producer.**
`HANDOFF.md:239-240`: *"there is no roll anywhere in the instrument, so the general ladder branch has
no producer. `H-98` stays `absent` on purpose."* `ladder.py:153` takes that branch on `"net" in result
and "ob" in result` — which U1's σ-leverage provider now supplies for `tell`. Extend it to the other
contested non-combat verbs as they gain `contests:` rows, so the branch has a producer for each.
(b) **The wound-count band edges**, which `combat.py:56-61` names as all that is left of `H-98`: which
wound counts sit in which band — an edge over a real quantity, not an invented correspondence.
**LAYER 2.**
**COMPLIANCE.** `04:164` — *"| `seam/wrappers/*` | **nothing, ever** | the projection | a `Margin` |
**none** |"*. ⚠ The `04:692` "a subsystem returning a winner has not met the contract" clause the first
draft cited **does not bind here**: the combat wrapper already returns the quantity, so quoting it
against this position asserted a breach that does not exist.
**OBSERVABLE.** `corpus_run`'s degree histogram is non-empty for a **non-combat** contested verb whose
`contests:` row this position wires. For combat, the histogram is already reachable — do not claim it
as new. H-98's grade moves only for the half actually closed, and the commit says which half.
**FALSIFIER.** A band edge that discriminates on a quantity the tracker does not return; or a fourth
band re-introduced under another name, which `ladder.py:131-132` calls *"the mapping that ruling
removed."*
**TIER.** `sonnet` producer against a ruled source, `opus` critic — the first draft of this position
is the evidence that the critic is doing the work here.

### 9 · PC-SURRENDER
**not earlier** same lane and files as 8 · **not later** it is the only PC item with a live spec and no
implementation, and it sits beside 8 so the `Margin` accounts for a yield.

**INSTRUCTION.** `combat_reference_v1.md` §11.4 specifies Yield (declared in Phase 1; accepted ends the
combat, refused leaves the yielder unresisting) and Disengage (Agility pool, opposed pursuit, penalty
at 0 Stamina). Disengage already has symbols; **Yield has none**. Add the state, the accept/refuse
branch and the wrapper mapping — a yield is a `Margin` with the loser's outcome, never a fourth resolver.
**LAYER 2**, but the governing surface is the `combat_engine_v1/` head plus holonic doctrine, **not
`04`**. Lens B against `04` runs on the wrapper edge only, under `04:164` as at position 2.
**COMPLIANCE.** `CLAUDE.md` §0.05 — *"A value the engine uses must live where code reads it."* The TN,
Ob and dice-penalty figures go into `config.py` as justified constants, never into prose.
**OBSERVABLE.** A planted yield ends the exchange with no further rolls, in the `engine/tests/` combat
goldens; `ci_sim_fabrication_check.py` green with every new constant cited.
**FALSIFIER.** A yield accepted while the yielder's faction objective is still contested in the zone
must be refused — that is §11.4's own clause.
**TIER.** `sonnet`/`opus`.

### 10 · U5 / R-07 — `Person.stance` written
**not earlier** degree (U1, landed) + contract (G4) · **not later** U6 needs it.

**INSTRUCTION.** Content owner is the r-execution-plan. `verb_table.yaml`: the degree-keyed `writes:`
for `tell`/`speak` gain `Person.stance` and `emits:` gains `stance.moved`; `loop/effects.py` gains the
writers; `rosters.yaml` **derives** its band key from the degree labels rather than retyping the
combat bands. The write matrix row already exists. Ride-along: set H-46's grade, still `absent` after
U3 landed.
**LAYER 2.**
**COMPLIANCE.** `04` AX-3: ledger and conviction state live in different sub-stores with different
write tokens — **INTERIOR at WITNESS, ACTS at RESOLVE**. And the interior writer's signature takes a
`PersonInterior` and **no ledger reference**, exactly as `choose` takes no `World`.
**OBSERVABLE.** R-07 moves `partial → met` **only** on the output of its own `measure:` command.
**FALSIFIER.** Two people told the same thing at different degrees must end with different stance
rows; and a `Failure` band that writes a stance move must fail at load.
**TIER.** `sonnet`/`opus` — **no byte-identity control exists here**, so the critic carries the weight.

### 11 · U6 — the first R-01/R-02 measurement
**not earlier** U1, U2, U4, U5 in, and Arc 2's hash moves behind it · **not later** the verb set must be
stable when the number is taken.

**INSTRUCTION.** Run the sweep verbatim from the r-execution-plan; acceptance point is the `2x3` cell.
**No code changes.** ED-IN-0210 adds a precondition: every opener in the executing set has its closer
built, or the measurement says which do not.
**LAYER 2 measurement.** Lens B does not run.
**COMPLIANCE.** `CLAUDE.md` §0.1 pt 4 — *"**A number without a control is not a measurement — in
either direction.**"* The only control this instrument yields is the `none ≥ default` arm; say so.
**OBSERVABLE.** Reconvergence **< 96 %** at `2x3`, with the cells committed. R-01/R-02 flip on the
printed number or not at all. ⚠ **The first draft wrote `< 100 %` here against a falsifier of `≥ 96 %`
— an overlap of four points in which the same result both passed and failed**, which is §0.1 pt 2's
assertion that cannot observe the failure it excludes. The content owner's threshold is unambiguous
(`r-execution-plan_part2.md:1367-1368`: *"If reconvergence is still ≥96% at U6, U6's own falsifier
governs"*) and the draft had silently loosened it.
⚠ **Declare the prior before running.** `HANDOFF.md:241-243` records this cell at **100.00 %, zero
divergences** — *"the acceptance is CELL-DEPENDENT and the cheaper cell fails it. 95.77% at `2 x 1`;
100.00%, zero divergences, at `2 x 3` … Do not quote 95.77% without the cell."* So `2x3` is the cell
that has never read below the bar. The number that lands is read against that prior, not against
nothing.
**FALSIFIER.** Reconvergence ≥ 96 % ⇒ report which channel is closed and leave both `not_met`. Do not
re-pin.
**TIER.** `sonnet` runs it; **`opus` reads the number** — the judgment is attributing the result to the
engine rather than to the roster.

### 12 · H-62-rest · 13 · W28-cast · 14 · U7-own
**12 — INSTRUCTION.** Degree-keyed `writes:` rows for `(Person, scar)`, `(Person, axis_count)`,
`(Person, convictions)` on the contested verbs, with `_delta` tables on U5's shape and magnitudes
declared-and-swept. `beliefs` is not a field — a belief is a `commit` to an OUGHT — so it lands at 14.
**COMPLIANCE.** `04:1023` names these four `Person` interior cells and records that **no verb in the
table writes any of them**, which is tier-0 H-62 in the executable chain. `04:227`: **WITNESS never
touches a conviction** — convictions are ACTS rows and the gate refuses an INTERIOR token on one.
**FALSIFIER.** A conviction write reachable from a `Failure` band, or from WITNESS's token.
**TIER.** `opus`/`opus` — which verb moves which interior, and by how much, is design under a ratified
shape.

**13 — INSTRUCTION.** `rg '^\s*cast:' engine/season/cases/` returns **0**. The reader does not exist
either: `harness/corpus_run.py::build_at` seats three people and reads no `cast:`. **The reader lands
in the same commit as the first block.** The principle is `04:124`'s — *"every roster, table, fixture,
matrix and verb row read at load by **one** loader that cross-validates and raises on any absence or
any declared-but-unread row"* — ⚠ **cited as an ANALOGY, not as the row this position must satisfy**,
which the antagonist pass was right to insist on: `04:124`'s own "where it lives" column is `data/`,
and a `cast:` block under `cases/` read by `harness/` is neither a `data/` closed set nor one of `04`'s
nine modules. `skills/layer-conformance` B0: *"Do not grade code against a spec that does not claim
it."* What actually binds is `01_AXIOMS.md` ID-13 — *"a mechanism that does not exist, wearing a
schema's clothes"* — the rule that reverted `U3a` for putting a table in `rosters.yaml` that nothing
read. Schema: `who_acts`, `one_line`, `knowledge`; entries naming a player get `WAITS-ON-PLAYER`. NPC
lane (46) first. **This position owns `build_at`'s `cast:` consumption**; position 17 does not.
**LAYER.** The blocks are Layer-2 **content**; the reader is Layer-2 apparatus in `harness/`, which is
none of `04`'s nine modules. Lens B runs on the reader only.
**CONTROL.** With `cast:` absent, `build_at` still seats three and the tallies are unchanged.
**FALSIFIER.** A `one_line` token-matched from the case prose rather than authored.
**TIER.** `sonnet` authors against the schema; `opus` critic checks the `WAITS-ON-PLAYER` split.
`haiku` rejected — each block needs the case's prose read for who actually acts.

**14 — INSTRUCTION.** Land the verbs in antonym pairs, per ED-IN-0210 ruling 1 (*verbs invoke
mechanisms or interactions between a character and another entity; they are not fiats*): `commit`+
`repudiate`, `oblige`+`waive`, `succeed`+`deposed`, `tie / knot`+`fray / loosen`, then `forge`,
`restore`, `exchange`, `destroy_record`. **Precondition inside the unit:** `decision/options.py`
returns the same `subject` for every operand slot, so no corpus-formed act can name two distinct
parties — fix that and put the counterparty check **in the fold**, not per effect. Ride-along
CANDIDATE-WHY: `Candidate.why` is written once and read nowhere; give it a reader or remove it in this
commit — `04` licenses a reader *or* removal, never a hole row. Default: remove.
**COMPLIANCE.** `04`'s loader invariant 4, widened by F7: **every failable clause has a refusal kind —
not only a verb with a `requires`, but each conjunct of it.**
**OBSERVABLE.** State the prediction before the commit: landing a reversible pair moves W-D divergence
**up**, the opposite of group 1's fall.
**FALSIFIER.** A `Tenure(X, X)` self-loop accepted, or an `oblige` whose object is a bare string naming
no entity — both are the F7/F8 recurrence that reverted this work once already.
**TIER.** `sonnet` producer, **`opus` critic** — a green 190-test suite already missed two findings in
this exact family.

### 15 · Record-kind fold · 16 · H-84
**15 — INSTRUCTION.** `state/world.py` carries `petitions` and `dispensations` as separate dicts. Fold
both into `Record` kinds; re-key the verb table's `writes:` from `Petition.exists`/`Dispensation.exists`
to `Record.exists`; two existence matrix rows collapse to one. Then `petition` and `carry` as verbs,
`petition` two-sided per ED-IN-0210 ruling 2. Settlements P7 *is* this fold and needs no separate
acceptance.
**COMPLIANCE.** `04:180` — *"| 11 | `Petition`, `Dispensation` as separate non-carriers | **kinds of
`Record`** *(synthesis call)* | ID-7; §D.4's admission test |"*. ✗ Note for anyone re-deriving this:
`04:178` is row 9 (`tie`/`knot`) — an intermediate agent "corrected" `:180` to `:178` and was wrong.
`04:255-258` carries the reasoning: folding them in means *"`forge`, `destroy_record`, `hold` and
`carry` reach them with no new rows, and two existence rows collapse into one."*
**FALSIFIER.** A `hold` on a dispensation refused because the store still has a second home.
**TIER.** `opus`/`opus` — schema.

**16 — INSTRUCTION.** One two-party verb (name it against `VOCABULARY.md` before adding the row):
`own` + `hold:<record>` eligibility, writing the holder's `hold` closed and the receiver's open. This
is the first verb in the vocabulary that moves a Record to another person — **without it no second
person ever holds one**, which bounds propagation depth everywhere downstream.
**COMPLIANCE.** `04:529-530`'s T-m at the gate (the transfer closes the holder's own tenure), and
`04`'s row on two homes for one relation: one store keyed by subject, the object side a cache.
**OBSERVABLE.** `holder_of(record)` changes and the previous holder's channel stops minting for it;
H-84's grade set by the commit.
**FALSIFIER.** The receiver's claim about the Record predates the transfer — that means the witness
read the old holder.
**TIER.** `sonnet`/`opus`.

### 17 · U8 · 18 · PROC-A · 19 · U7-remit · 19b · U7-disp
**17 — INSTRUCTION.** `queries/person_q.py::ambitions(p)` over live `commit` edges to OUGHT
Propositions. ⚠ **`build_at`'s consumption of `cast:` belongs to position 13, not here** — one symbol
was assigned to two positions four apart in the first draft, which is §8's *every rule lives once*
failing on the plan itself. Part 1 §7 item 6 holds the move back, because U8's content belongs to the
r-execution plan.
**COMPLIANCE.** `04:152` — the row's columns are `owns (writes) | may read`: `queries/person_q`
**writes** nothing and **may read** *"a `PersonInterior` snapshot only"*. (The first draft inverted
the two and said it "returns" the snapshot; the table says neither.) AX-2 splits the two Query
families **by module**, not by first parameter.
**FALSIFIER.** The existing `sense`-is-the-only-World-taker test goes red if `ambitions` takes a `World`.
**TIER.** `sonnet`/`opus`.

**18 — INSTRUCTION.** (a) **The stress suite cannot run**: `stress_proceedings.py:7` targets
`proposals/2026-09-01-season-loop-tests/tracer/shape.py` and **that directory does not exist**.
Re-host its 28 tests against `engine.season` as `engine/season/tests` cases, each an execution or a
declared absence. (b) `world_q.judging_set(w, venue, matter)`. (c) `convene` corrected. (d)
`arrangements.yaml` plus its loader, through the ONE loader, unknown keys refused. Step 3 (`release`)
is already done.
**COMPLIANCE.** `04:176` — *"| 7 | `Rung.judging_set_rule` | **deleted**; the judging set is a Query
over seats | §D.2's NEVER — *decision-shaped state on a container* |"* (the first draft cited
`:325-327`, which is a table header); `04:131` puts every closed set and the ONE loader in `data/`;
`04:468` — *"**unknown keys rejected — a `scale:` key fails the load**"*.
**OBSERVABLE.** Removing a seat's remit empties the judging set; a purview walk one rung up still finds
it. A thirteenth arrangement loads with no code change; a fifteenth key fails naming the row.
**FALSIFIER.** A stress test passing against a tracer-era fixture rather than a real `World`.
**TIER.** `sonnet`/`opus`; the stress re-host is `sonnet` — bounded translation of declared cases.

**19 — INSTRUCTION.** The five remit verbs; each gains a predicate reading `via.scope` and an effect on
the G4 contract. `establish`'s third write is removed — establishment is a Query over `oblige`.
`open_case` gains `writes: DocketItem.matter` and the world reader a `docket` branch: **a proceeding
with zero authored acts needs somebody to have put the matter before the room, and no step did that.**
**COMPLIANCE.** `04:120` AX-1 — `Act.actor : PersonId` and nothing else has that type; `resolve` has no
institution parameter; **a seat enters through `Act.via`.** Plus `04:330` as at position 6.
**OBSERVABLE.** ⚠ **Corrected by the antagonist pass.** The first draft copied `12_BUILD_ORDER.md:19`'s
step-7 artifact verbatim — *"determining an unheard one emits `determine.unheard`"* — and **that event
no longer exists**: `04_VERBS.md:379` struck the `heard` conjunct because *"no act in this design
writes a `heard` relation, so the conjunct had no producer"*, `:381-384` registered the loss as
`P-23`, and the corrected row's `emits_on_refusal` is `["determine.refused", "determine.unseated"]`.
A position whose observable waits on a deleted event cannot be closed by execution (§0.2).
The live artifact is `21_RECONCILIATION.md:575`: **a determination opens the disposal Tenure on its
subject via the seat; below quorum, `determine.refused`.** Plus: a `levy` executes with `Act.via` set.
**FALSIFIER.** Any of the five executing with `via=None`.
⚠ **AND THIS POSITION NEEDS A GATE CLAUSE IT CANNOT ADD ITSELF.** `04_VERBS.md:352-357` records that a
**conferral-basis opener matches none of `§C.2`'s four admitted bases** — *"So does `confer`, today,
which is an `IN`-lane defect this design reveals rather than causes."* A determination that opens a
Tenure on another's subject needs that fourth case, and position 6 is the only place the gate's F3
branch is written (*"the purview readers are rewritten exactly once here"*). It lands at position 6
or it is written twice.
**TIER.** `opus`/`opus`.

**19b — CONDITIONAL ON ED-IN-0210.** ⚠ **This position is a declared departure from the spine**, which
put `U7-disp` off-spine with *"**Do not schedule it until ruled**"* and made the reversion slot
*"between positions 10 and 11"*. It is given a position because Jordan asked for everything
sequenced; part 1 §7 item 5 records the departure and what reverts it. Under arm (A) the three verbs
key on the actor's ledger claim of the terms and answer both channels; under (B) `dispatch` gets its
own obey/disobey pair.
**COMPLIANCE.** `04:230`'s carve-out, which is exact and is not a widening: **the fold may ask the
actor's own ledger, through the `PersonInterior` snapshot the act carries, and no other.** A Query
taking a ledger and an asker who is not its holder still does not exist.
**FALSIFIER.** `comply` evaluable for a person whose ledger holds no claim of the terms.
**TIER.** `sonnet`/`opus`.

### 20 · U9 / R-04 · 21 · U10 · 22 · PROC-B · 23 · PART-E-0/2
**20 — INSTRUCTION.** `faction_q` as **queries, never fields**: `resolve`, `holdings`, `purview`,
`superiors`, `subordinates`, `at_war`. `scale_of_rung` in `rosters.yaml`, stating **before writing it**
which of the two problems it solves — the eight `rung_kinds` admit neither `faction` nor `world`.
Re-scale the 44 faction cases with a `why:` each; rule the 10 world cases as ≥ 2 realm rungs under §0
test 5. H-101 is expressed as `superiors`/`subordinates` over `contain` + seats, **not as a field**.
Settlements P5 is `faction_q.resolve` and rides here.
**COMPLIANCE.** `04:285` — *"`faction_q.resolve(w, prop) -> Faction      -- built at a barrier, handed
on, dropped at the next`"*, with `:286`'s `NEVER:` list — never a member of `World`, a field of its
own, an `Act.actor`, a `contest` claimant or a `hold` subject. And `Faction.holdings` is a Query that
**reads** members' holds and cannot write one. (The first draft cited `:277-284`, which is the prose
and the type body and contains neither quoted string.)
**OBSERVABLE.** `corpus_run` reports no unrepresentable scales; ≥ 1 faction-scale ARC ends.
**CONTROL.** Person, settlement and realm case hashes do not move.
**FALSIFIER.** The permuted-`rung_kinds` run `04` specifies — a real one. A `rg` for `superior|liege|rank`
is term-matching and is named here as weak.
**TIER.** `opus`/`opus`.

**21 — INSTRUCTION.** Repeat 11's instrument; flip R-rows only on printed numbers; reconcile the
progress board against what ran **without greening a row by editing the board**.
**COMPLIANCE.** `CLAUDE.md` §0.2 — the board row *"counts `state:` strings in
`workplans/workplan_v6_progress.yaml`, a hand-edited board"* and is **bookkeeping, not evidence**.
**FALSIFIER.** Any `measured:` line not reproducible from its row's `measure:` command. The register
refuses an empty one; it cannot refuse a wrong one, so the critic must.
**TIER.** `sonnet` runs, `opus` reads.

**22 — INSTRUCTION.** The proceedings provider, with the amendment its own reconciliation records:
**M-7 fails at the 1D floor** (`p_success` 0.0006 at Ob 3, 0.0000 above) and the σ-reach remedy is
refuted. ⚠ **The content owner leaves two remedies open — *"the obstacle needs a ceiling — remedy (b),
or a pool floor above 1D"* — and the first draft passed that fork through as "take the other", which
names two things.** Dispositioned here under §0 test 5, because this document was asked to
orchestrate: **take the obstacle ceiling.** It is the remedy the design's own `06_RESOLUTION.md`
§B.3a already names as (b), and the two are not interchangeable games — a ceiling caps how hard a
matter can get, while a pool floor raises every participant's competence, which is a statement about
people rather than about matters. The **value** is injected and swept, not chosen here. If Jordan
prefers the floor, that is a §5 item and it displaces this clause only. `speak` with four bands; `proceedings.run`
registered as a provider; the prize rows repoint from `sigma_leverage` and drop `interim: true` —
**a row change, not a code change**, which is what ED-SC-0033 clause (2) bought. The seam's own
obstacle site is deleted: clause (3)'s single owner.
**COMPLIANCE.** `04:679-684` — the provider is resolved *by string, at boot*, and returns **a MARGIN.
Never a winner.** `04:1031` step 10: a misspelled manifest row fails at boot naming the row.
**OBSERVABLE.** One seeded proceeding runs end to end with zero authored acts, twice, byte-identical
including the hash — and `causes[]` walks from the determination back to the date that raised it.
**FALSIFIER.** A planted `if arrangement.id == "tribunal"` must redden the closure test; and M-7
re-run at the floor must clear Ob ≥ 4 after the ceiling.
**TIER.** `opus`/`opus`; the arrangements transcription `sonnet`.

**23 — INSTRUCTION.** Typed id wrappers over the same `H` output, so `content_hash` folds identical
strings — that is the byte-identity control. Then consolidate the `data/` loaders behind one entry and
land whichever of the twelve invariants remain unenforced, **each with a planted violation naming its
row**. ⚠ This position is a **departure from the spine**, which held PART E steps 0 and 2
*"unscheduled by design"*; §7 item 4 of part 1 records the departure and what would revert it.
**COMPLIANCE.** `04:1021` step 0 — 1,000 ids minted twice under one seed are bit-identical, a golden
hash pinned, and **`H` is not a language `hash()`**. `04:204`: `Act.actor` cannot hold a `SeatId` —
*"STRUCTURAL under a checker; MECHANICAL at runtime"*, and **the build runs no such checker in CI, so
the runtime grade is the real one and this unit must say so.**
**FALSIFIER.** A `SeatId` passed as `Act.actor` and not refused in the fold.
**TIER.** `sonnet` producer once the shape is fixed, `opus` critic.

### 24–27 · the ruling-gated positions
Each waits on its §5 ruling and none blocks another.

**24 SE-BUILD.** After ED-SE-0051 and acceptance: P3 (individuation is a refusal — CENSUS reads the
demand kind and individuates with `causes[]` naming it), P4 (the founding verbs — `found` does not load
today because a `writes:` pair has no matrix row), P1 (dearth reaches the body), P2 under whichever arm
is ruled. `band_floors` also does not load; fix or drop at pre-flight.
**COMPLIANCE.** `04:1030` step 9 — a `dispatch` to a non-existent clerk emits `person.demanded`, and
next season a Person exists whose `person.individuated` cites it. `04`'s F.20 row: **the founding rows
are dropped until a verb is ruled.** **FALSIFIER.** `Person.weight` or the envelope written by anything
but CENSUS/MATTER; or a stored aggregate where a Query is required. **TIER.** `opus`/`opus`.

**25 MB-GOLDEN.** Under arm (A): re-record the goldens **once**; make the three flags whose env
defaults contradict their own comments say what they do; apply the CEV friction. Ride-along: ED-MB-0016's
file cites point at paths the 08-24 port deleted, and `mass_battle_v30.md`'s "Effective Combat Pool" is
a different quantity from the PC Combat Pool — a §4 idempotence collision worth renaming.
**LAYER 2**, governed by the MB head and holonic doctrine, **not `04`**; Lens B does not run.
**COMPLIANCE.** `CLAUDE.md` §0.1 — *"**`pytest tests/valoria` is a SHIPPING gate, not a belief gate**,
and behaviour changes include default flips and golden re-records."*
**FALSIFIER.** A second re-record within the same arm. **TIER.** `sonnet`/`opus`.

**26 GO-VERSION.** Record the ruled version where the conversion strategy and the stale architecture
spec disagree; then ED-1050's deferred module re-export; then held H6. `port/` stays absent until
PART E step 13.
**COMPLIANCE.** `04:1034` step 13 — both licensed guards red on a planted violation then green, and a
headless run prints the Python oracle's hash in the integer domain. `CLAUDE.md` §6 — *"a port never
corrects its oracle in place (ED-1050)."*
**FALSIFIER.** Any `.gd` value differing from its `.py` oracle. **TIER.** `sonnet` port, `opus` parity critic.

**27 WR-SCOPE.** If in scope: reshape `systems/threadwork/sim/coherence.py` from the depleting track
the rulings replaced to the two-quantity distance, and re-price the application bands. If not: retire
the tree by position 2's pattern. **Not `04`-governed**; Lens B does not run.
**COMPLIANCE.** `CLAUDE.md` §0.05's test — *"if this document were deleted, would the game behave
differently?"* The applications corpus is reference either way; only `coherence.py` is mechanism.
**OBSERVABLE.** A coherence distance with two remedies executes in a threadwork sim, or the directory
is at a `FORK:` ref. **TIER.** `opus`/`opus` if built.
