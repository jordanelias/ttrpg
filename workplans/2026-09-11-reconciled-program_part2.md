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
`HANDOFF.md`; strike `HANDOFF.md:463-469`'s *"THE STEP TO TAKE: S7"*; `CLAUDE.md:95-96`'s *"traces to
an open M1 juncture"* → an R-row of `requirements.yaml` or a position here. **Do not touch
`tools/m1_acceptance.py`** — §0.1 pt 5 forbids re-tooling a board reader.

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

**INSTRUCTION.** (a) **Relocate the one live rule before deleting anything**:
`systems/social_contest/sim/contest/degree_extension.py`'s demote-only rule becomes the `veto` on the
interim provider in `engine/season/seam/wrappers/sigma.py`. (b) `git rm -r systems/social_contest/` —
**46 files** today, not the 47 ED-SC-0033 states; recount at execution. (c) Write the `FORK:` row in
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
`loop/driver.py` only; `gate.write` takes it. **Rewrite the call sites, counted by `ast`, not text:
42** — `harness/probes.py` 20 · `state/world.py` 9 · `loop/matter.py` 6 · `loop/witness.py` 3 ·
`loop/calendar.py` 2 · `loop/resolve.py` 2. ✗ **The spine's "33 `.write(` call sites" does not
reproduce**; this unit's pre-flight owns the number. `loop/deliberate` and `seam/wrappers/*` receive
no token. Add the AST scan for `Token(` construction outside the driver, with an asserted floor on
what it inspected.
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
four declared bases and otherwise raise. Re-point `loop/resolve.py`'s `_eligible` `remit:` branch,
`under_purview`, `_req_revoke` and `_req_confer` from the actor's own `hold` tenures to `via.scope`.
**Expect three live violations** — `revoke`, `confer` and `kill / wound` all write another's edge;
declare each as `T-o`-with-`via` or under its own basis. **Do not weaken the check to keep them
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

### 8 · H-98 — the combat seam returns a `Margin`
**not earlier** order-free against Arc 2 (wrappers hold no token), placed after G4 so its Events land
once on the finished contract · **not later** U5's `_eff_kill` Wounded branch reads a degree with no
producer.

**INSTRUCTION.** Per the hole's own Jordan ruling of 2026-09-03 — *"kill/wound degrees should be
directly taken from scene combat"* — `seam/wrappers/combat.py` returns a `Margin` read off the
engine's WoundTracker instead of discarding it, and `seam/ladder.py` gains the producer its fourth
band waits on.
**LAYER 2.**
**COMPLIANCE.** `04:692` — *"| the degree | the subsystem returns a `Margin`; **a subsystem returning a
winner has not met the contract** — a type assertion |"*. The wrapper returns ±1/0 today, so it is in
breach of a ratified row.
**OBSERVABLE.** `corpus_run`'s degree histogram for `kill / wound` is non-empty for the first time;
H-98's grade moves `absent → measured` **in the landing commit**. Hash: no `kill` executes in the
corpus today, so expect stationary — and say so rather than leaving it implied.
**FALSIFIER.** A wrapper returning `+1` for a fight the tracker reports as *felled* is a winner, not a
margin. Assert the type.
**TIER.** `sonnet` producer against a ruled source, `opus` critic.

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
**OBSERVABLE.** Reconvergence **< 100 %** at `2x3`, with the cells committed. R-01/R-02 flip on the
printed number or not at all.
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
in the same commit as the first block** — `04:124` requires *"every roster, table, fixture, matrix and
verb row read at load by **one** loader that cross-validates and raises on any absence or any
declared-but-unread row"*, and a `cast:` nobody reads is exactly that. Schema: `who_acts`, `one_line`,
`knowledge`; entries naming a player get `WAITS-ON-PLAYER`. NPC lane (46) first.
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
Propositions; `build_at` consumes the cast.
**COMPLIANCE.** `04:152` — `queries/person_q` reads **nothing** and returns *"a `PersonInterior`
snapshot only"*; AX-2 splits the two Query families **by module**, not by first parameter.
**FALSIFIER.** The existing `sense`-is-the-only-World-taker test goes red if `ambitions` takes a `World`.
**TIER.** `sonnet`/`opus`.

**18 — INSTRUCTION.** (a) **The stress suite cannot run**: `stress_proceedings.py:7` targets
`proposals/2026-09-01-season-loop-tests/tracer/shape.py` and **that directory does not exist**.
Re-host its 28 tests against `engine.season` as `engine/season/tests` cases, each an execution or a
declared absence. (b) `world_q.judging_set(w, venue, matter)`. (c) `convene` corrected. (d)
`arrangements.yaml` plus its loader, through the ONE loader, unknown keys refused. Step 3 (`release`)
is already done.
**COMPLIANCE.** `04:325-327` deletes `judging_set_rule` from `Rung` and makes the judging set *a Query
over seats*; `04:131` puts every closed set and the ONE loader in `data/`; `04:468` — *"**unknown keys
rejected — a `scale:` key fails the load**"*.
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
**OBSERVABLE.** A bench member determines a heard matter; determining an unheard one emits
`determine.unheard`; an unseated actor emits `determine.unseated`. A `levy` executes with `Act.via` set.
**FALSIFIER.** Any of the five executing with `via=None`.
**TIER.** `opus`/`opus`.

**19b — CONDITIONAL ON ED-IN-0210.** Under arm (A) the three verbs key on the actor's ledger claim of
the terms and answer both channels; under (B) `dispatch` gets its own obey/disobey pair.
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
**COMPLIANCE.** `04:277-284` — a `Faction` is *"built at a barrier, handed on, dropped at the next"* and
**NEVER** a member of `World`, a field of its own, an `Act.actor`, a `contest` claimant or a `hold`
subject. And `Faction.holdings` is a Query that **reads** members' holds and cannot write one.
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
**M-7 fails at the 1D floor** and the σ-reach remedy is refuted, so take the other — an obstacle
ceiling or a pool floor above 1D, injected and swept. `speak` with four bands; `proceedings.run`
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
