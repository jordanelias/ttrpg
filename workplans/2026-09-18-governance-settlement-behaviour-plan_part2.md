# THE PLAN — part 2: the instruction and the compliance clause per position

> **RENAMED 2026-09-18 (`ED-IN-0254`)** from `workplans/2026-09-11-reconciled-program_part2.md`; the
> old path resolves via `tools/pathres.py`. Reads after
> `workplans/2026-09-18-governance-settlement-behaviour-plan.md`.

## Status: RATIFIED 2026-09-12 (ED-IN-0215), same as the file this reads after — a stale `PROPOSED`
## left over from before that ratification is corrected here (found 2026-09-25 during the ED-IN-0270
## amendment). AMENDED 2026-09-25 (`ED-IN-0270`): lettered sub-position entries added or corrected
## throughout (see that file's `§3.1`/`§3.9` for what changed and why).
## Reads after `2026-09-18-governance-settlement-behaviour-plan.md`. That file owns the ORDER and the supersession
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

⚠ **`04` MOVED UNDER THESE QUOTATIONS (found 2026-09-25).** `534a2bc` (`ED-IN-0267`/`ED-IN-0268`)
added two lines to `architecture/meta/04_CODE_ARCHITECTURE.md` at `:213`, so **every `04:NNN` cited
below with NNN above 213 now reads at NNN + 2** — `04:227` is `:229`, `:330` is `:332`, `:402` is
`:404`, `:529-534` is `:531-536`, `:536` is `:538`, and so on through `:1036` → `:1038`. The quoted
TEXT is unchanged; citations at or below `:213` (`:120`, `:124`, `:131`, `:152`, `:164`, `:176`, `:180`,
`:199`, `:206`) did not move. The entries added 2026-09-25 cite the current lines. The claim above —
*"every quotation below was re-read at its cited line"* — held when it was written and does not hold
for the moved range.

**THE LETTERED SUB-POSITIONS (added 2026-09-25, `ED-IN-0270`).** Until this date every numbered position had an
entry here and no lettered one did; they existed only as `§3.2` row text. Each now has an entry beside
the position it hangs off, in `§3.2`'s order, with the same fields — plus `WHERE` (the files it
edits) and `GATE`, because a lettered row's dependencies are what `§3.1`'s phases are built from.
`13b` is the exception: `H-71`'s row in `engine/season/hole_register.yaml` is its record, and it is not
copied here.

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

⚠⚠ **THIS POSITION HAS NOW BEEN GOT WRONG TWICE, IN THE SAME SHAPE, AND THE SECOND TIME IS RECORDED
HERE BECAUSE IT IS THE MORE INSTRUCTIVE ONE.** A pre-flight censused **imports** of
`degree_extension.py`, found six, none under `engine/season/`, and concluded the rule was "live on the
measurement path, not the game path". **A read-only antagonist broke that in one move: THE ENGINE DOES
NOT IMPORT THIS PACKAGE, IT BINDS IT BY STRING** — which is the mechanism `CLAUDE.md` §3 states
outright (*"the engine still depends on subsystems, resolved by string at first call, so one is swapped
by editing a registry row"*). An import census cannot see a registry row. Verified on disk:

| the chain | evidence |
|---|---|
| **seven** roles target `systems.social_contest` | `engine/engine_params/composition.json` — `contest_side.a/.b`, `scene_builder.contest`, `scene_resolver.contest`, `parliamentary_motion`, `parliamentary_vote`, `parliamentary_vote_declaration` |
| resolved dynamically | `engine/substrate/composition.py:67` — `getattr(importlib.import_module(mod_name), attr)` |
| called by the cross-scale dispatcher | `engine/cross_scale/scene_dispatch.py:288-289` (`composition.require('scene_builder.contest')`), `:337,:339` (`contest_side.a/b`) |
| run by the campaign driver | `engine/mc_v18.py` → `scene_dispatch.run_scene_phase` |
| and the rule rides it | `contest/__init__.py` → `resolver.py:26` imports `CONTEST_DEGREE_EXTENSION`, applied at `resolver.py:307-308` — `degree_from_net(net, base_ob, extension=self.degree_extension, pool=pool)` |

**So the rule IS reached from the campaign driver.** Three further corrections follow from that:

1. **The veto is NOT unbuilt.** `engine/autoload/dice_engine.py:227-228` is
   `degree_from_net(net, ob, extension: "BandExtension | None" = None, **context)`, with the
   demote-only constraint structural in its body. `seam/ladder.py:164` simply calls it with **two
   positional arguments** and does not forward the extension. That is a pass-through on an existing
   primitive — a step, not a unit. The pre-flight's own option (ii) called it *"a `BandExtension` the
   ladder already types"* twelve lines later, contradicting itself.
2. **But it is unreachable AT THIS SEAM regardless**, and this is the real structural blocker:
   `04:684`'s shape takes the veto **from the provider**, and the season's provider for both contest
   prizes is `sigma_leverage` — engine-side, `interim: true`. `seam/wrappers/sigma.py:55-58` states
   *"THIS MODULE IMPORTS NOTHING FROM `systems/` AND INSERTS NO `sys.path`"*, and `PATH_SEAM_ALLOWED`
   is shrink-only. An engine-side provider cannot carry a subsystem's veto. The shape opens when the
   **proceedings** provider lands (position 22), not when a parameter is added.
3. **The sharper statement of what the season loop does today:** `sigma.py:28` reproduces
   `resolver.py:302`'s `net = roll_net(pool) + net_boost(lev, pool)` — the line immediately **above**
   `:307`, where the extension is applied. The loop reaches the rule's site and stops one line short.
   That is not "never reaches the rule".

⚠ **AND ED-SC-0033 DOES NOT NAME THIS RULE.** Its three clauses are the seam dispatching by manifest
row, the two contest prizes repointing, and *the obstacle* having a single owner — a different
quantity from the band extension. Reading proceedings as the rule's owner substitutes *"owns the
activity"* for *"owns this rule"*. Jordan's order is also scoped to **orphaned** code, and per the
chain above this file is not orphaned. The home question is therefore open under §0 test 5, **not
settled by the ruling**, and this document does not settle it either.

⚠ **"Losing the instrument quietly" was wrong too.** `tools/balance_oracle.py:152-154` are bare
unguarded function-local imports, so a `git rm` breaks its default invocation outright — but
`tests/valoria/test_balance_oracle_arms.py:65-66` and `:88-89` import the same modules **inside the
blocking pytest gate**, so the loss reddens the shipping gate. Loud, not silent.

**INSTRUCTION — step (b) is what is mis-scoped, not step (a).** `git rm -r systems/social_contest/`
deletes `parliamentary_vote.py` and `parliamentary_stay.py` too, and three composition roles bind
those to `engine/cross_scale/parliamentary_bridge.py` and two `systems/factions/` modules. Carving out
`degree_extension.py` would protect the one file least at risk while deleting six live bindings.
**ED-SC-0033's own row says this in advance** — *"more than twenty inbound reference sites OUTSIDE it
… several machine-read by blocking gates. So a bare `git rm` turns validators red. RULED HERE,
EXECUTED ELSEWHERE."* Re-derive the deletion set **from the composition roles**: retire what is
genuinely orphaned (`contest_legacy_stub.py`, anything no role and no caller reaches) and leave every
role-bound module until the proceedings provider exists to take its row over — which is exactly what
ED-SC-0033 clause (2) already describes as a ROW change rather than a code change.

**Two consumers the import census also missed, of different kinds:**
`engine/engine_params/sim_params.json:3851` carries a row whose `file` is `degree_extension.py`,
generated by `tools/export_sim_params.py` — the typed layer that crosses into the port, and the one
consumer that is **mechanism** under §0.05 rather than test or tool. And
`tests/valoria/test_degree_ladder_single_owner.py:162` hardcodes the **path string** as a registry key,
which repointing an import does not fix.
(b) ~~`git rm -r systems/social_contest/`~~ — **re-derive from the composition roles, per above** —
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
**STATE (2026-09-25). DONE** — `ED-IN-0258`, 2026-09-19: `state/acts.py`, `state/gate.py`,
`state/log.py`, `state/attribution.py`; `engine/season/tests/test_g1a_act_store_and_receipts.py`.

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

**STATE (2026-09-25). PARTIAL — COMMITTED** (`952dc21`, PR #429, `ED-IN-0269`, ledger `status:
partial`). Every production READER except the content hash is off the field: G1a (`ED-IN-0258`) built
`state/attribution.py` (`actor_of`, `anchor_of`) and moved `epistemic.py`'s three readers
(`claim_subjects`, `_event_place`, `_ch_witness_key`); `ED-IN-0269` moved `world.py::last_emission_of`
(the MATTER clock chain) and `witness.py`'s `observation_deposit_mode == "actor"` branch — the shipped
default. Its control: `engine/season/tests` 267 passed before and after, `World.content_hash()`
byte-identical — equality is the right control for a reader migration, because the hash still folds
`e.subject`.

**WHAT REMAINS, AND WHY IT NEEDS NO DESIGN DECISION.** Every production `Event(` constructor already
attributes without the field: the fold's four sites in `loop/resolve.py` carry `causes=[a.id]` (tier
1), MATTER's `condition.band_crossed` at `loop/matter.py:53` always carries the prior MATTER emission
as its cause (tier 3), and the gate's own emission in `state/world.py` carries a minted change (tier
2). **The only `causes=[ROOT]`-and-no-`changes` emitters are APPARATUS** — `harness/probes.py`'s
`Ev()` (`:270`, the one owner every probe construction goes through; `plague.struck` at `:1593` is the
class `state/attribution.py:42` names as the blocker) and `harness/corpus_run.py`'s `planted_control`
(`:545`). They are the population the corpus measurement runs on, so they are migrated, not ignored.

**REMAINING INSTRUCTION, in order.** (1) Give each such construction a bare `StateChange` carrying its
subject (tier 2) — `test_a_bare_statechange_is_still_admitted_and_this_is_the_transitional_seam`
(`tests/test_g1a_act_store_and_receipts.py:108`) confirms the log still admits one — or a real
antecedent (tier 3). Change `Ev()` once, and `planted_control`. (2) Delete `Event.subject`
(`state/carriers.py:168`) and `World.write`'s `subject=` parameter; shift every positional `Event(...)`
constructor. (3) Remove `e.subject` from the content-hash fold (`state/world.py:751`). **That moves
every content hash: DECLARE the re-record** (part 1 `§3.0` sweep check 5). (4) Rewrite
`test_the_accessors_reproduce_the_field_exactly` (`tests/test_g1b_attribution.py:121`), whose control
IS the field, and delete `test_tier_4_is_the_field_and_it_is_the_blocker` (`:93`) on purpose, as its
own docstring asks. (5) Update `attribution.py`'s header, and append to `H-107`'s `source:` — never a
new key (R0, `test_w0_the_row_shape_cannot_grow_quietly`). The raw readers left today:
`state/world.py:751`, `harness/headless.py:189` (a print), `harness/probes.py:698`.
**WHERE.** `state/carriers.py`, `state/world.py`, `state/attribution.py`, `harness/probes.py`,
`harness/corpus_run.py`, `harness/headless.py`, `loop/resolve.py`, `loop/matter.py`.
**FALSIFIER, added.** After deletion, plant a probe Event with no changes and `[ROOT]`: `anchor_of`
returns `None` AND the witness deposits nothing for it — asserted as an anchored-event count `>= N`
over the probe corpus, so an empty population cannot pass. And
`test_events_with_no_actor_are_a_real_population_not_an_empty_one` (`:147`) keeps its floor.
**CONFLICT.** `11a` moves `epistemic._event_place` to `world_q.place_of`. Finish this deletion first,
or `11a` moves the `anchor_of`-based version — never both in flight (part 1 `§3.9` edge 1).

### 5 · G2 — one `Token`, minted in `loop/driver` only
**not earlier** one signature, rewritten only after G1a returns receipts · **not later** G3 reads the
token's class.

**INSTRUCTION.** `WriteClass` is today an enum passed as a parameter. Add `Token`, constructed in
`loop/driver.py` only; `gate.write` takes it. **Rewrite the ~~33~~ 36 gate call sites** —
`harness/probes.py` 20 · `loop/matter.py` ~~6~~ **8** · `loop/witness.py` ~~3~~ **4** ·
`loop/calendar.py` 2 · `loop/resolve.py` 2 (**re-measured 2026-09-25 at `952dc21`** by the method
below; MATTER gained item 3b's `body`/`exists` writes at `matter.py:309,322`. Re-run it at build
time rather than trusting either number). Reproduce with: `ast` walk over `engine/season/**/*.py` minus `tests/`, keeping
`Call` nodes whose `func` is an `Attribute` with `attr == "write"`, **grouped by receiver** — ~~33~~
**36** have receiver `w` (33 on the spine's day), and 9 have receiver `TRACE` (re-run 2026-09-25). ⚠ **Those 9 are `trace_log.py`'s tracer, a different object,
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
**TIER.** `opus` for the type and scan; **`sonnet` for the ~~42~~ 36-site rewrite** — mechanical against a
fixed signature, and the tier drop pays because the handoff is the `ast`-derived site list itself.
**STATE (2026-09-25). NOT STARTED** — no `Token` type exists anywhere in `engine/season/`
(`state/gate.py:36`: *"Not a token in `04:199`'s sense — that is G2"*). `World.write`'s signature is
at `state/world.py:467-472`, the one line G1b and G2 both touch.
**CONFLICT.** Beyond `4 → 5`: `loop/matter.py` is also edited by `11a`, `24f` and `24` (P1), and
`loop/witness.py` by `15` and `15b` (part 1 `§3.9`).

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
**STATE (2026-09-25). NOT STARTED.** `Act` has no `via` (`state/carriers.py:406`); `under_purview`
(`loop/predicates.py:105`) and the title helpers read the ACTOR's own titles; `_req_revoke` carries
the `is_title` branch at `predicates.py:347-349` (moved from `:252` by `13f`'s additions to this file —
re-check citations below `13f`'s edits before building). **The three live violations, located:** `_eff_revoke`
(`loop/effects.py:191`) and `_eff_confer` (`:108`) close another person's `hold`; `_eff_kill` (`:410`)
closes others' edges through `World.remove_person` (`state/world.py:384`). `_eff_release` (`:161`) is
T-m by construction. **The `Act(...)` mint** is in `decision/choose.py` — `via` is set there, from the
holder's seat, person-side.
**ABSORBS `13d-ii`** — purview as ruled by `ED-IN-0256` (4): *"owner of highest rung in chain of
ownership, eg territory is owned by Duke if it's within boundaries of duchy"*, asked of `via.scope`
(`04:332` at current lines). And build-order item 15.
**FALSIFIER, sharpened.** Count the refusals: `>= 3`, one per live violation, so a gate that refuses
one and admits two cannot pass.
**CONFLICT.** `13d-i` rewrites `_req_confer` and `_req_revoke` onto rostered basis values; this
position re-points the same two predicates at `via.scope`. `13d-i` first, or this position does both
— never in parallel (part 1 `§3.9` edge 3). And `16` (≡ `15a`, `give`) opens a Tenure for the
RECEIVER, which none of the four bases admits unless `give` is the receiver's own act or a fifth
basis: settle it in this pre-flight, beside the conferral opener.

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
**STATE (2026-09-25). NOT STARTED.** `_apply_write` (`loop/resolve.py:352`) computes no before/after;
the effect runs inside `apply()` and the receipts are minted after `w.write` returns (`:400`). Eleven
effects are registered today; every effect landed before this position adds one to the rewrite (`13f`
first, in part 1 `§3.1`'s order — so twelve).

⚠ **PRE-FLIGHT — A HARD PROBLEM NO CONTENT OWNER NAMES.** `work`'s delta is not written by its
effect. `_eff_work` (`loop/effects.py:277`) returns the site and defers the delta to an accumulator
(`loop/resolve.py:641-653`), which sums deltas per `(subject, field)` and applies them ONCE in a
second `w.write("condition", WriteClass.ACTS, ...)` at `:653`. A gate that computes before/after at
the effect's own write therefore sees NO change for `work`, by construction, and the change lands in
the accumulator's write. **Decide where `NoOpReceipt` is judged for accumulated writes before
`_eff_work` is rewritten** — the candidate is at the accumulator's write, per subject, carrying the
act ids that contributed — **or `work` is refused forever.** Architecture's answer (§0 test 5), not
Jordan's. `test_w8_work_emits_a_success_while_repairing_nothing`
(`engine/season/tests/test_season_shape.py:5211`) pins today's defect — `work` emits `site.worked`
while `site.condition` is unchanged, as its own docstring records — and it flips here and is
rewritten.
**FALSIFIER, sharpened.** The planted no-mutation effect must produce the refusal Event and NO
`mode="set"` receipt for its subject: refusal count `>= 1`, success count `== 0`.

### 7a · COMMIT-EFFECT (added 2026-09-25)
**not earlier** than `15`, `15c` and `15b` — its aperture is shut until they land · **not later** than
`17a`, which waits on it.

**STATE.** Built once and HELD, not in the tree: `EFFECTS` has no `commit`, and `commit` is not
resolvable (`writes: ["Tenure.since"]` with no effect; `loop/driver.py:99`). `HANDOFF_IN.md` carries
it HELD.
**INSTRUCTION.** `@effect_for("commit")` minting the `commit` Tenure the row already declares (kind in
`tenure_kinds`), through `add_tenure`, returning the Tenure it opened — an effect that returns nothing
makes the fold emit the refusal (`loop/resolve.py:306-311`). Content owner:
`proposals/2026-09-17-governance-and-behaviour/01_THE_BUILD_ORDER.md` §7.2 (`:460`), which records the
first build: *"`commitment.made : 0` / `commitment.refused : 42`"* on one populated season, because
**no question source offers a Proposition referent** (BO-9). BO-10: build-order items 5, 7 and 8 — here
`15`, `15c`, `15b` — are what open it. Built before them, its first run re-measures 0 / 42.
**WHERE.** `loop/effects.py`; `verb_table.yaml`'s `commit` row only if its `writes:` needs re-keying.
**OBSERVABLE.** BO-9's own command after `15`/`15c`/`15b`: one populated season, seed 0,
`commitment.made > 0`. `resolvable_verbs()` gains `commit`.
**FALSIFIER.** BO-10's: if `commitment.made` is still 0 after `15`/`15c`/`15b`, the producer is
somewhere else and §7.2's diagnosis is wrong — report that, do not widen Q4 (§7.2 refused that repair,
with its measurement). And the effect with its body removed, same seed: no Tenure.
**GATE.** `15`, `15c`, `15b`; lands after G4 in part 1 `§3.1` or accepts G4's rewrite.
**TIER.** as position `16`: `sonnet`/`opus` — a small effect on a declared row.

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
**STATE (2026-09-25). (a) HAS NO FURTHER SUBJECT TODAY; (b) IS THE LIVE HALF.** (a): the general
branch at `seam/ladder.py:153` already has its producer — `tell`, through the σ-leverage provider
(`seam/wrappers/sigma.py`) — and only 2 of 38 verbs carry `contests:` at all (`kill / wound` → the
body, `tell` → a standing; `ED-IN-0261` measured it). The one contested verb `ED-IN-0261` adds,
`accept`, is combat. *"Extend it to the other contested non-combat verbs as they gain rows"* is
therefore contingent on rows nothing has ruled. (b): the band edge is a literal —
`seam/ladder.py:133-135`, `if st["felled"]: return FELLED` / `return WOUNDED if st["wounds"] > 0
else UNTOUCHED`. `combat_degree_bands` is data (`rosters.yaml:507`), and the `> 0` edge is not.
**INSTRUCTION for (b).** Move the edge to data — a `combat_band_edges` row keyed on
`combat_degree_bands`, with a declared sweep (Jordan, 2026-09-02: *"definitions are not
hardcoded"*), read by `combat_degree`. No fourth band. Grade `H-98` by the half closed.
**FALSIFIER for (b).** An edge on a quantity the tracker does not return refuses at load; an edge set
to `wounds > max_wounds` yields `UNTOUCHED` for every fought subject, and the test asserts it checked
`>= 1` fought subject.
**CONFLICT.** The `kill / wound` row and the combat wrapper are re-cut by `ED-IN-0261`'s verb split,
which rides the cells commit, and touched by position 9. Either order, never interleaved (part 1
`§3.9` edge 10).

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
**STATE (2026-09-25). NOT STARTED — AND THE PC LANE FRAMES IT AS A DECISION, WHICH THIS ENTRY DID
NOT.** `registers/handoffs/HANDOFF_PC.md`: *"ED-PC-0056 — §11.4 is live spec with no implementation —
Decide: a resolver in `combat_engine_v1/`, or strike the spec"*. `ED-PC-0056` itself is `closed`
(2026-08-08) and carried §11.4 forward verbatim as load-bearing. Part 1's row reads *promote*, which
is an ORDER placement, not that decision — part 1 `§5` item 12. And a second, administrative gate:
the PC `ED-` id block is exhausted (`references/id_reservations.yaml:124`, `HANDOFF_PC.md`), so a
release comes before anything is filed. **The symbols, located:** Disengage already exists as an
EMERGENT behaviour — `combat_engine_v1/wrapper.py:167-183`, gated by `disengage_attempt_p` /
`disengage_clean_p` (`combat_systems.py:972,993`), constants in `config.py`. Yield has none. The
source is quarantined reference, named here by bare filename as `CLAUDE.md` §1 asks:
`combat_reference_v1.md` §11.4.
**IF BUILT — ONE DATA DECISION TO STATE, NOT INVENT.** A yield maps onto the seam as a `Margin` /
`wound_state` with the loser's outcome (`seam/wrappers/combat.py`'s `resolve`), never a fourth
resolver. `combat_degree_bands` is `[Felled, Wounded, Untouched]`, and position 8 forbids a fourth
band: either a yield maps onto `Untouched`/`Wounded` with the surrender carried on the result, or the
band roster gains a value — say which, and why.
**FALSIFIER, added.** A planted yield ends the exchange with zero further rolls — assert the bout
count, not only the outcome.
**GATE.** 8; the build-or-strike decision; a PC id-block release; and never interleaved with the
cells commit's verb split (part 1 `§3.9` edge 10).

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
**CORRECTIONS (2026-09-25).**
- **The field is written today — at CONSTRUCTION, not by any act.** `harness/populated.py:596`
  appends `(prop.subject, …)` rows from `cast.stance_from_loyalty`, and `decision/choose.py`'s
  `stance_toward` (`:140`) is read by `score`. `requirements.yaml` R-07's *"nothing writes it"* is true
  of ACTS and false of construction. **FALSIFIER, added:** after two seasons at least one `stance.moved`
  Event whose `causes` names an act exists (`>= 1` asserted) — otherwise the populated world passes
  with nothing built.
- **`speak` cannot carry it.** `speak` is untyped with no `contests:`, so there is no degree to key a
  delta on; `tell` is the only own-ledger-typed verb resolving through the four-band ladder. The
  INSTRUCTION above over-reaches by one verb: `tell` only.
- **The band key.** `ladder_bands` is DERIVED at import from `engine.autoload.dice_engine`'s degree
  labels, never retyped; `combat_degree_bands` (`rosters.yaml:507`) is the wrong set and its own note
  says so. `tables.stance_delta` is keyed `[ladder_bands, verb_table]`, `default_cell: 0.0`, sweep
  `[declared, none, doubled]`. Rows are per referent — `(referent=actor, valence, weight)` on the
  SUBJECT — never a summed field. Content owner: `workplans/2026-09-09-r-execution-plan.md:1324-1428`.
- **The name.** `ED-IN-0261` records that `Person.stance` has FOUR live senses and no
  `references/names_index.yaml` entry. Add the entry in this commit (`CLAUDE.md` §4: define it where it
  is invoked).
- **The hash moves on BOTH arms**, declared: on the `none` arm a successful `tell` whose effect writes
  nothing is refused (`loop/resolve.py:306-311`), so the event stream changes either way.
**GATE.** 7 (G4) — part 1's row read `—` until 2026-09-25, against this entry's own *not earlier*.
**WHERE.** `rosters.yaml`, `data/rosters.py`, `verb_table.yaml` (`tell`), `loop/effects.py`,
`references/names_index.yaml`.

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
**NOTE (2026-09-25).** Part 1 `§5` item 1's *"a later yes invalidates U6's number"* no longer applies:
`ED-IN-0214` is superseded by `ED-IN-0261`, and the cells commit (`12b`/`12c`) IS the re-centre. If the
cells land before this measurement, it is taken on the new basis; if after, it is re-taken — declare
which. The instrument's runner is `proposals/2026-09-04-degree-sweep/` (`wd_acceptance.py`, with
`wd_chunk.py` / `wd_collect.py` splitting the same sweep into chunks); it was verified PRESENT and
tracked on 2026-09-25, not run.

### 11a · REACH (added 2026-09-25)
**not earlier** G1b's deletion, which rewrote the function this moves · **not later** `11b`, which
waits on it, and `15`, whose r2 item depends on it.

**INSTRUCTION.** Content owner: `proposals/2026-09-17-governance-and-holdings-r2/05_LEDGER_AND_BUILD.md`
§A.4.1 item 2 (`:1091-1136`) and `01_ATTENTION_AND_REACH.md` §A.3–§A.4. (1) `reach(w, p)` beside
`descendants` in `queries/world_q.py` — four limbs, and **a FILTER that never widens the fan**
(`01` §A.4.4); the seat limb is the seat's rung and its descendants (LB-2e). `descendants` excludes
its own rung, so the inclusive walk is written, not assumed. (2) `place_of(w, x)` moved in from
`epistemic._event_place` (`epistemic.py:273`), with a new Record limb (`05:496-503`). ⚠
`state/carriers.py:390`'s comment already says *"`place_of(w, event)` already answers that
question"* — it does not exist yet; this position makes the comment true. (3) `questions_for` with
TWO sources and a three-clause Q2; delete `date_due` and `band_crossed` from `question_sources`
(`rosters.yaml:341`; they contribute 0 questions — the control is an identity). (4) Delete
`w.crossings` (`state/world.py:188`, written `loop/matter.py:58`); the Event at `matter.py:53`
carries the same fact. (5) `occasioned_by` (`world_q.py:672`) to one route, its dead guard and id
search deleted (`05:775-782`). (6) Rename `test_w5_q_has_a_producer_across_all_four_sources` (LB-2d).
**WHERE.** `queries/world_q.py`, `rosters.yaml`, `data/rosters.py` (`QUESTION_SOURCES`),
`state/world.py`, `loop/matter.py`, `epistemic.py` (`_ch_co_located` calls `_event_place`),
`harness/probes.py` (the `w.crossings` readers), `decision/options.py` (a docstring).
**COMPLIANCE.** LB-2b, the r2 flood test, and `01` §A.4.4's filter rule — design documents, cited
for intent. The `04` row that binds is `04:124` (`ID-13`): a question source that contributes nothing
is a declared-but-unread row, which is why two are deleted rather than kept.
**OBSERVABLE.** Question histogram, same seed, against `{'claim_landed': 561, 'need': 81}` (measured
2026-09-17, `05:1105` — re-take it before comparing); a seatless person's count unchanged. Golden
re-record DECLARED.
**FALSIFIER.** LB-2b — **a duke is NOT reached by a crossing in his purview that nobody witnessed**:
`observers_for`'s count before == after. And LB-2e's inclusive walk.
**CONFLICT.** G1b on `_event_place` (part 1 `§3.9` edge 1); `loop/matter.py` with G2 and `24f`.
**GATE.** `S4` (STR-4's fold-rule constraint — closed; the `reach` source declares how it folds under
`aggregate_questions`), 4.

### 11b · CALENDAR-EMIT (added 2026-09-25)
**not earlier** `11a` · **not later** anything that reads `date.fired`.

**INSTRUCTION.** `loop/calendar.py:37` writes `Date.fired` through the gate with no `emits=` and no
subject. Add `emits="date.fired"` with the venue as subject (r2 `05:795-797`), and `causes=` chained
through `last_emission_of` as the other clocks do. Nothing else. ⚠ `holder` is written nowhere in
production, so `calendar.py:33`'s `vacant` is always true and the DocketItem write at `:40-42` never
runs (`05:812-816`) — **say so, do not fix it here.**
**WHERE.** `loop/calendar.py`.
**COMPLIANCE.** `04:156` — *"| `loop/calendar` | `Date.fired`, `DocketItem`, `ConveningCondition` | own
state, an R-1 subtree aggregate, the calendar | `date.fired` · `docket.formed` | CALENDAR |"*.
`write_matrix.yaml` already declares `Date.fired [CAL] emits date.fired`; the gap is the call site.
**OBSERVABLE — CORRECTED.** Unobservable on the populated world (`build_realm(0)`: 0 dates), and part 1
used to say *"plant a date or it proves nothing"*. **The corpus already plants one:**
`corpus_run.build_at` adds `d_forced` (`due_at: 1`, no holder) to every case whose
`ENDINGS_CLASSIFIED` ending is `forced_by_threshold` (`harness/corpus_run.py:320-325`). LB-2c — *a
fired date deposits a claim in the convener's ledger* — runs on those worlds. Count them from
`ENDINGS_CLASSIFIED.yaml` and assert `>= 1`.
**FALSIFIER.** No date planted → no `date.fired` Event and no claim (the control); a date with `due_at`
≠ the tick → nothing fires.
**GATE.** 11a. The hash moves on every world that fires a date — declare it.

### 12 · H-62-rest
(`13` and `14` shared this heading until 2026-09-25; the lettered `12b`–`13d` entries now sit
between them, so each has its own.)

**12 — INSTRUCTION.** Degree-keyed `writes:` rows for `(Person, scar)`, `(Person, axis_count)`,
`(Person, convictions)` on the contested verbs, with `_delta` tables on U5's shape and magnitudes
declared-and-swept. `beliefs` is not a field — a belief is a `commit` to an OUGHT — so it lands at 14.
**COMPLIANCE.** `04:1023` names these four `Person` interior cells and records that **no verb in the
table writes any of them**, which is tier-0 H-62 in the executable chain. `04:227`: **WITNESS never
touches a conviction** — convictions are ACTS rows and the gate refuses an INTERIOR token on one.
**FALSIFIER.** A conviction write reachable from a `Failure` band, or from WITNESS's token.
**TIER.** `opus`/`opus` — which verb moves which interior, and by how much, is design under a ratified
shape.
**RE-SCOPED BY `ED-IN-0261` (2026-09-20), recorded 2026-09-25.** Three things changed under this entry:
- **`convictions` is `pursuits`** (`ED-IN-0268` landed the rename): FIFTEEN pursuits over SEVEN bipolar
  axes, and `(Person, pursuits)` is `[RES] ACTS social:true emits pursuit.moved`, *"moved by argument
  and consequence, never by evidence"* (`write_matrix.yaml:183-190`). **No trigger for that movement
  is specified anywhere** (`H-62`: *"none of the remaining five has a specified trigger"*). It is a
  design gap; describe it, do not build around it.
- **The scar is REBUILT, not "DONE".** What ships (`loop/effects.py:340`, `_scar`, reached from
  `_eff_kill`) is a float per axis on the wounded party, at its control arm (`scar_step=0`, `H-128`).
  `ED-IN-0261` rules a COUNT per element, thresholds 1 / 2 / 3 on BOTH tracks, written at RESOLVE by
  the act over `observers_for(w, e, mode, everyone)` (`epistemic.py:491`, perception's one owner — the
  ruling declares where the RESOLVE and WITNESS calls of it diverge on `co_located`). **R6-atomic
  with the cells** (`12b`/`12c`) — `HANDOFF_IN.md` carries it Open.
- **`(Person, axis_count)` has a matrix row and NO FIELD** (`write_matrix.yaml:148-152`;
  `matrix_rows_without_a_field()` lists it). Once scars ARE counts per element, the count-scar is the
  counter: retire the `axis_count` row or give it the field — **never build both.** A §0 test-4/5
  answer, not Jordan's (part 1 `§5`). And `Person.beliefs` is a field the matrix header says to
  delete — `18a`'s and `14`'s, not this entry's.
**COMPLIANCE, current line.** `04:229` — *"**WITNESS never touches a conviction**"*.
**FALSIFIER, added.** A scar written on a person who did NOT observe the violating act, per
`observers_for`.
**GATE.** `12b`/`12c` (the cells) for the scar; 7 (G4) for any effect; a design answer for the
`pursuits` trigger. Part 1's `OPEN · —` was stale until 2026-09-25.
**WHERE.** `loop/effects.py`, `state/carriers.py`, `write_matrix.yaml`, `verb_table.yaml`,
`epistemic.py` (read only).

### 12b · 12c · 12d — THE PURSUIT CELLS (added 2026-09-25; JORDAN-gated)
**not earlier** than Jordan's cells · **not later** than `12`'s scar rebuild and any `score` term that
dots against the basis (build-order 6f).

**STATE.** The authoring surface is `proposals/2026-09-20-pursuit-basis-worksheet.yaml` — 15 pursuits ×
7 axes = 105 projection cells, plus the alignment re-cell over the verbs. **`12d` is PARTIAL:** the
season-side identifier rename landed by hand (`ED-IN-0268`: `data/pursuits.py`, `Person.pursuits`,
`rosters.yaml`'s `pursuits` / `pursuit_axes` / `pursuit_projection`); the SUBSTRATE owner is
unchanged — `references/descriptor_registry.yaml:236` `conviction_roster`, `count: 13`, which
`rosters.yaml`'s `pursuits` (`:251`) still reads through `from_descriptor:`, and `pursuit_axes`
(`:290`) still carries the four old axis rows. `tools/valoria_rename.py` is still retired (part 1
`§3.5`). **`12b`** — the affiliation roster and the incompatibility relation, with `conviction` a
VECTOR and confliction DERIVED — has no field: `Person` carries no `conviction`, and no roster exists.
**INSTRUCTION — ONCE JORDAN HAS FILLED THE `set:` CELLS, AND NOT BEFORE.** ONE R6-atomic commit:
`descriptor_registry.yaml` (the roster and the axes, behind `tools/export_descriptors.py --check`);
`rosters.yaml`'s `tables.pursuit_projection` (15 × 7) and `tables.alignment` (the verbs × 7, including
the split rows `kill`, `wound`, `fight`, `challenge`, `accept`). **Atomic because `_load_projection`
and `_load_alignment` bind at module scope (`data/verbs.py`) and refuse an unrostered key or an
all-zero matrix, so a partial landing is an `ImportError`.** Then `ED-IN-0261`'s verb split
(`HANDOFF_IN.md`), then `12`'s scar rebuild.
~~**PREPARABLE BEFORE THE CELLS (`12b`'s schema half).**~~ **`12b`'s SCHEMA HALF — IN THE CELLS
COMMIT, NOT BEFORE IT (corrected 2026-09-25).** A `(Person, conviction)` carrier, its matrix row, and
a `person_q` Query for confliction, derived and never stored. No cell values. This is `.py` work, so
part 1's *"no `engine/season/*.py` change"* holds for `12c`'s tables and not for `12b`. Preparing it
ahead of the cells would ship a carrier with nothing in it and nothing reading it. That is `ID-13`'s
*"a mechanism that does not exist, wearing a schema's clothes"*, the rule `24d-ii` is held to below.
⚠ **The Query also needs a caller.** If nothing reads confliction when the cells land (the score
function, build-order 6f, is unscheduled), the Query waits for 6f, just as `capacity` waits for
`19c`.
**WHERE.** `references/descriptor_registry.yaml`, `engine/engine_params/descriptors.json` (via the
exporter, never by hand), `rosters.yaml`, `verb_table.yaml`, `state/carriers.py`, `write_matrix.yaml`,
`queries/person_q.py`.
**OBSERVABLE / FALSIFIER — Jordan's own.** The devout-Solmund / anti-Solmund `faith` pair must score
far apart; `conviction_spread.py`'s `within_60deg` is the aggregate form. And the export `--check`
round-trips.
**GATE.** Jordan's cells (part 1 `§5` item 11). Never interleaved with positions 8 and 9 (part 1
`§3.9` edge 10).
**DO NOT** author a cell. This entry describes the shape and the atomicity only.
**TIER.** as position 12: `opus`/`opus` for the landing; the cells are Jordan's.

### 13 · W28-cast

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

### 13b · 13f · 13e · 13d — the offices and the remit (added 2026-09-25)

**13b — H-71. DONE IN BOTH HALVES; its record is not here.** `engine/season/hole_register.yaml`'s
`H-71` row (`grade: measured`) carries both closures — the holder's own (`ED-IN-0255`) and others'
(`ED-IN-0267`, appended to `source:`). Its cost, a seated holder's new verbs displacing subsistence
work, is `24f`'s origin.

**13f — `establish` HAS NO EFFECT.**
**not earlier** nothing — part 1 `§3.1` phase α, first · **not later** `13e`, which cannot land until
the semantics this decides is decided.
**STATE.** `verb_table.yaml:222-233`: `eligibility: ["remit:confer"]`, `writes: ["Office.exists",
"Office.remit", "Office.establishment"]`, `grade: assumption`; no `@effect_for("establish")`; not
resolvable. ⚠ **THE ROW/FIELD KEY IS BROKEN BEFORE ANY EFFECT RUNS:** `write_matrix.yaml` carries an
`(Office, remit)` row, and `Office` has no `remit` field — `matrix_rows_without_a_field()['absent']`
lists it; the field is `Office.remit_acts` (`state/carriers.py:581`). ⚠ **AND AN EFFECT ALONE WILL
NOT MAKE IT RUN:** `requires:` is prose (*"the establishing office's conferral basis, and a rung to
establish it at"*) with no typed cell and no predicate, so the fold raises `Unspecified` on a
hand-built `establish` (`loop/resolve.py:164-176`), and `resolvable_verbs()` excludes it on that gate
as well as on the effect gate (`loop/driver.py:96-99`).
**INSTRUCTION.** (1) Reconcile the key at its OWNER (`CLAUDE.md` §0.05 cl.3): rename the matrix row or
the field, and say which; the loader keys writes by `(kind, field)`. (2) Make the precondition
evaluable — a `_req_establish` in `REQUIRES_PREDICATES` or a typed cell. **Compose it on the basis test
`_req_confer` already uses** (`loop/predicates.py:167`, *"no conferral basis: the office cannot be
conferred"*), factored once if it is not, so `13d-i` rewrites ONE function and both predicates
inherit the rostered values. Which office's basis the prose means — the new office's declared
conferral, or the establishing actor's — is a reading the build states. (3) `_eff_establish` constructs
an `Office(...)` and returns its id. ~~`Office.__post_init__` REQUIRES a `body` or a `faction` (it refuses
an office belonging to nothing) and validates `remit_acts` against `REMIT_ACTS` (`carriers.py:603`):
let those refusals stand, never pre-empt them with a default.~~ ⚠ **CORRECTED 2026-09-25: THOSE ARE
RAISES, NOT REFUSALS, and a raise inside RESOLVE crashes the fold.** `Office.__post_init__` raises
`Unowned` on a remit act off `REMIT_ACTS` (`carriers.py:603-607`). `office_faction` raises on an
unknown body or faction, a body/faction mismatch, or an office belonging to nothing
(`data/rosters.py:491-521`).
It raises `Forbidden` when a titled post names a body (`carriers.py:626-637`). Raised from inside the
effect's `apply()`, any of these escapes the fold, and `establish.refused` is never emitted. **So an
`establish` whose operands are empty, or name a body, faction or rung that does not resolve, REFUSES
before any `Office` is constructed.** It uses the fold's existing refusal paths. First choice: the
precondition returns `False`, and the fold emits `emits_on_refusal`. Otherwise the effect returns
`[]` and the fold emits the refusal (`loop/resolve.py:306-311`), as `_eff_kill` does for a payload
naming no subject. The precondition asks the SAME owners the constructor asks: `office_faction`,
with its refusal translated to `False` so the rule still lives once, and `REMIT_ACTS` membership. The
constructor's raises remain as the backstop for a malformed `Office` that got past it, and there
loud is correct. Never pre-empt the check with a default, and never catch the raise and report
success. (4) `Office.establishment` stays in `writes:` until `17a` deletes the field, its matrix row
and this entry together (r2 ~~`05_LEDGER_AND_BUILD.md:238-246`~~ `05_LEDGER_AND_BUILD.md:214-221`:
*three edits, not one*). The effect leaves the field at its default.
(5) **Decide snapshot vs mirror with the effect in front of you.** The evidence: `_grant_remit`'s
docstring states SNAPSHOT (`state/world.py:295`), and `test_h71_the_grant_is_a_snapshot_not_a_mirror`
(`engine/season/tests/test_season_shape.py:5368`) pins the behaviour and records that it is not ruled.
The concrete case is a `hold` opened on an office id before the office exists — `_grant_remit` traces
`class_of(t.object) is None` and stamps nothing — and then `establish` creates it.
**CANDIDATE ANSWER — §0 test 5, NOT Jordan's (part 1 `§5`); for the antagonist to attack.** The
effect writes the office AND re-stamps the grant on every live `hold` on that office, in the same
act. `(Tenure, payload)` is a licensed `[RES] ACTS` row (`write_matrix.yaml`) and so is
`(Office, remit)`. The grant still changes only by an act (snapshot's property); sitting holders are
reached (mirror's observable); `choose` still receives no `World`. ⚠ **Route the re-stamp through
`_grant_remit`, the one writer** — `Tenure.granted_acts` (`carriers.py:66`) makes the payload's shape
a rule that lives once — **given an explicit overwrite**, because today it calls
`payload.setdefault("remit_acts", …)` (`world.py:343`), which leaves an existing grant untouched. A
second writer that knows the key is `CLAUDE.md` §8 broken.
**REQUIRES — WITHOUT THIS THE CANDIDATE'S LICENCE NEVER FIRES (added 2026-09-25).** `establish`'s
`writes:` (`verb_table.yaml:229`) is `["Office.exists", "Office.remit", "Office.establishment"]`, and
it names no `Tenure.payload`. The fold gates exactly the pairs a verb declares. It runs the effect
once, inside the FIRST pair's `w.write` (`loop/resolve.py:293-298`, `:369-393`). So a re-stamp
written from `_eff_establish` today writes `Tenure.payload` inside the `Office` write's `apply()`,
under the Office pair's gate and not its own. The fold consults the `(Tenure, payload)` matrix row
(`write_matrix.yaml:339-345`) only for a verb that declares that pair. **So `writes:` gains
`Tenure.payload`, and `emits:` gains `tenure.payload_set`**, that row's declared emission. It is
earned only when a holder was actually re-stamped, through the effect's `{kind: [ids]}` return
(`loop/resolve.py:377-390`), so an establish with no sitting holder does not publish it.
**AN `establish` ON AN OFFICE ID THAT ALREADY EXISTS IS A REMIT CHANGE, NOT A REFUSAL.** This is a
candidate answer at the same ladder step (§0 test 5), NOT a fresh escalation. This position's own
framing is that *the grant changes only by an act*. `establish` is the only act whose `writes:` name
`Office.remit`, so refusing it on an existing id would leave NO act able to change a remit, and the
re-stamp would be dead code. On an existing id the effect rewrites `remit_acts` in place and
re-stamps every live `hold`. It earns `remit.changed` (`(Office, remit)`'s declared emission, which
`emits:` also gains) and not `office.established`. Any other difference refuses. An act naming a
different `body`/`faction` for an existing id is re-founding, which `writes:` does not declare. The
FALSIFIER below is this case.
**WHERE.** `loop/effects.py`, `loop/predicates.py`, `state/world.py` (`_grant_remit`),
`write_matrix.yaml` or `state/carriers.py` (the key), `verb_table.yaml` (the `Tenure.payload` write
and the two emissions above, and a typed cell if that is the precondition route).
**OBSERVABLE.** A planted `Act(verb="establish", payload={…})` naming a body or faction executes and
`office.established` is emitted; a sitting holder's `granted_acts` changes by that act. ⚠ **A computed
`establish` forms with NO operands** — its `requires_typed` is absent, so `operands_for` returns `{}`
(`decision/options.py:439-441`) — **and must REFUSE** until `15c` widens the operand vocabulary; no
corpus world executes it. Once it is resolvable the corpus chooser offers it, so the executed/refused
sets move: name the move, and re-read
`test_the_corpus_runs_and_the_ranking_cannot_discriminate`'s pinned never-attempted set
(`test_season_shape.py:6996`).
**FALSIFIER.** Change an office's remit by a planted `establish` on its EXISTING id: a sitting
holder's `granted_acts` DID change (the mirror observable), and a `tenure.payload_set` naming that
holder's Tenure is emitted. A hand-mutation of `w.offices[x].remit_acts` still does NOT change it
(the snapshot half of the existing test). And an `establish` naming no `body`/`faction`, or an
unknown one, emits `establish.refused`, constructs nothing, and **lets no exception escape the fold**.
Assert on the Event, not on the absence of a traceback.
**GATE.** — (phase α). It is one of the nine `H-71` unblocked; `§3.9` edge 2 puts it before `13e`.
**BUILT 2026-09-25.** `office_described_by`/`_req_establish`/`_eff_establish` landed as specified;
21 new tests in `test_governance_build.py`. Confirmed by an antagonist pass (independent re-run):
`engine/season/tests -q -n auto` 209 passed clean (not the 207-with-2-pre-existing-failures the
builder's own receipt reported — that was the pre-fix baseline; the corpus never-attempted pin gaining
`establish` and one probe count moving 19→20 of 38 resolvable are RE-PINS this diff causes, not
failures it fixes, and `runs/results.json`'s diff is confirmed to move exactly those two things, no
probe verdict flipped). **KNOWN LIMITATIONS, NOT BLOCKING, RECORDED SO A LATER SESSION DOES NOT
RE-FIND THEM:** an office with `rung=None` (an office cluster — `tiny_world`'s `off_dicastery`, and
every populated office governing neither a realm nor a duchy) can never be re-remitted by this effect,
correctly refused rather than silently admitted; the remit-change arm cannot fire in ANY built world
today because no world builder sets an office's `conferral`, so it is reachable only through a
hand-built fixture, the same dependence `confer` already has; and there is no authority clause on who
may found or re-remit what — any holder with the `confer` remit can found an office for any
faction at any rung and re-remit any office with a conferral basis, including granting themselves a
new remit act in one act, which is unreachable until `13d-i` (conferral values) and `15c` (operands)
land and should be checked again then, possibly against the purview model `revoke` already uses
(`loop/predicates.py:110-114`).

**13e — ONE READING OF THE REMIT.**
**not earlier** `13f` · **not later** `17a`, which replaces one of the two functions this edits.
**STATE.** Three readings over two stores: `loop/resolve.py:55-56` (`off = w.offices.get(t.object);
if off and arg in off.remit_acts`), `epistemic.py:446` inside `_ch_post_remit` (`:413`,
`remits & set(off.remit_acts)`), and `decision/options.py:199-211` (`arg in t.granted_acts`, the
Tenure). `epistemic.py:420-436` records the finding and names `13f` as its gate.
**INSTRUCTION.** `resolve.py:55-56` → admit on `arg in t.granted_acts`; `epistemic.py:446` → `remits &
set(t.granted_acts)`. Both loops already bind `t`. Delete the `w.offices.get` reads. One commit.
**NO CONTENT OWNER** beyond part 1's row and the docstring above — this entry is the specification
(part 1 `§6`).
**WHERE.** `loop/resolve.py`, `epistemic.py`.
**COMPLIANCE.** `CLAUDE.md` §8, *"every rule lives once"*; the paragraph at `epistemic.py:420-436`
records the tree paying for this exact mistake once.
**FALSIFIER.** Hand-open a `hold` on an office that does NOT yet exist (snapshot `()`), then create the
office **BY HAND** (`w.offices[x] = Office(...)`, no act). The resolver must now REFUSE the holder's
remit verb, which it admitted before this position. Assert the refusal, and assert the test observed
`>= 1` such holder. ⚠ **Not by `establish` (clarified 2026-09-25).** After `13f`, an `establish`
re-stamps the sitting holder's grant, so the resolver ADMITS. That is `13f`'s falsifier and the
complement of this one: by hand → refuse, by act → admit. Assert both arms, or the two positions'
falsifiers read as contradicting each other. **And an AST scan:** no
`remit_acts` read outside `_grant_remit`, `Office.__post_init__` **and `_eff_establish`** (allow-listed
2026-09-25 — `13f` landed first and `loop/effects.py:194,196` compares and rewrites `remit_acts`
directly, on the office being re-remitted, which is what the effect's whole job is). A fourth reader is
planned — `budget()` counting `t.granted_acts` (`HANDOFF_IN.md`, blocked on `test_n3`'s floor) — and the
scan is what stops it regressing to the office.
**GATE.** `13f` (`§3.9` edge 2). **TIER.** `sonnet` producer — two one-line edits; `opus` critic,
because three independent lanes found this and a fourth reading is already queued.

**13d — OFFICES. SPLIT 2026-09-25: `13d-i` is buildable now; `13d-ii` is G3's.**
**STATE.** *Holders seated* is DONE as the 13-seat generic spine (`engine/season/governance_spine.yaml`,
`harness/governance_spine.py`; every empty remit filled from `rosters.yaml`'s `remit_default`, `:152`, a
declared TEST FIXTURE). NOT done: `engine/season/data/offices.yaml` does not exist; there is no
conferral or revocation roster; the `titles` roster is live (`rosters.yaml:783`); the `is_title` branch
is live (`loop/predicates.py:347-349`, moved from `:252` by `13f`); the title helpers are live (`predicates.py:144-165`, `titles_held`,
`highest_title_rank`, plus `title_domain` and `title_rank`); purview reads the actor
(`predicates.py:105`).

**13d-i — OFFICES AS DATA.**
**not earlier** nothing — phase α · **not later** G3, which re-points the predicates this rewrites.
~~and `18a`, whose `conferral_path` deletion replaces a field with this position's roster~~
(corrected 2026-09-25: `conferral_path` is a Query superseded by `13d-ii`'s purview walk, not a field
replaced by these rosters. See `18a`.)
**INSTRUCTION.** Content owner: r2 `03_SEATS_AND_CONTENT.md` and r2 item 10, **for STRUCTURE only**.
⚠ **r2's roster VALUES ARE SUPERSEDED (found 2026-09-25).** r2 `03:1043-1056` specifies two closed
rosters (`open: false`) with a basis assigned per seat. The values are `conferral_bases: [confer,
determine, succeed]` and `revocation_bases: [purview, holdings, none]`, and r2's 29 seats are
authored on them. Both value lists predate `ED-IN-0256` (2026-09-18), whose rulings (2) and (3)
replace them. **r2 supplies the structure. The ED supplies the values.** Mapping r2's seats onto the
new values is this position's build work, stated seat by seat and never inherited from r2's
columns. The two conferral vocabularies do not correspond by name: r2's is keyed on the act that
opens the hold, the ruling's on how a seat is filled. (1) Rosters for conferral —
**`appointed · elected · annex`**, `ED-IN-0256` ruling (2) — and for revocation —
*"rung above of same faction"*, ruling (3): structural, the holder of the rung ABOVE within the SAME
faction. It is not a rank comparison, and not r2's `purview`/`holdings` conjuncts. That is what
unblocks the `is_title` deletion (`H-109`). (2)
`_req_confer` (`predicates.py:167`, whose whole basis test today is a non-empty `conferral` string) and
`_req_revoke` (`:222`) rewritten on those values. (3) Delete `titles`, `title_domain`, `titles_held`,
`highest_title_rank`, `title_rank`. (4) **RE-HOME, DO NOT DELETE** the title-in-a-body refusal in
`Office.__post_init__` (~~`carriers.py:611-620`~~ `carriers.py:626-637`; `:611-620` is the faction
comment): r2 `03:661` re-expresses it as a CONTENT rule in
`offices.yaml`'s loader, same refusal and law string. (5) `offices.yaml` as the world-gen content
file `build_realm` reads — r2 `03:81` declares 29 seats, informed by 44 of `offices_draft.yaml`'s rows
(`03` §A.13).
**WHERE.** `rosters.yaml`, `loop/predicates.py`, `data/rosters.py`, `state/carriers.py` (`Office`),
`harness/populated.py`, new `engine/season/data/offices.yaml`.
**COMPLIANCE.** `AX` ID-4, *no `is_title` branch* (r2 `03:67`); and `04:124`, the one loader.
**FALSIFIER.** `LB-10c` (r2 `05:1278`), **re-pointed by ruling (3)**: r2 names it
`test_a_titled_seat_is_revocable_only_by_a_holder_of_its_domain` and prices item 10 on a
three-conjunct `holdings` rule, both written before `ED-IN-0256` ruled *"rung above of same
faction"* — so the test asserts the ruling, and is named for it. A titled seat is revocable only by
the holder of the rung above in the same faction: iterate the candidate revokers and `assert checked
>= N`. Plus: a revocation by a higher-ranked holder of a DIFFERENT faction refuses.
**CONFLICT.** G3 on the same two predicates (`§3.9` edge 3). If `13f` has landed, its
`_req_establish` composes on the same basis test and inherits this rewrite.
**GATE.** — .

**13d-ii — PURVIEW.** Absorbed into position 6 (G3), which rewrites every purview reader exactly once.
The ruling is `ED-IN-0256` (4): *"owner of highest rung in chain of ownership, eg territory is owned by
Duke if it's within boundaries of duchy"*, asked of `via.scope` (`04:332` at current lines). See
position 6. **GATE.** 6. **TIER.** position 6's, `opus`/`opus`.

### 14 · U7-own

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
**STATE AND DETAIL (2026-09-25).** NOT STARTED. `World.petitions` / `World.dispensations` are plain
dicts (`state/world.py:176-177`), hashed through `_STATE_COLLECTIONS` (`:714`), swept by
`harness/invariants.py:72`, and planted by `harness/probes.py` (`:1166`, `:1190`, `:1457`, `:1459`);
no production code reads them. In `verb_table.yaml`, `issue` writes `Dispensation.exists`, `petition`
writes `Petition.exists`, and `carry` is typed on the existence of a Petition and writes
`DocketItem.matter`; none has an effect and none is resolvable. There is no `record_kinds` roster:
`Record.kind` is free text (`state/carriers.py:522`), and `_eff_create_record` defaults it to `"text"`
(`loop/effects.py:316`). `Record` already has `subject_matter`, which r2 `02_THE_WRIT_AND_THE_WORD.md`
§A.4 specifies the `dispensation` schema for.
**REQUIRES, beyond the INSTRUCTION above.** A `record_kinds` roster with per-kind `subject_matter`
key-lists and the ⊕L35 refusal (r2 `05:671`) — copy `Rung.__setattr__`'s refusal shape
(`carriers.py:684-692`), do not invent a second. `_eff_issue` / `_eff_petition` mint a `Record` of kind
`dispensation` / `petition` plus the maker's `hold`, as `_eff_create_record` does. Delete the two
matrix rows and the two `World` dicts, and edit `harness/invariants.py:72` in the SAME commit — its
pinning test, `test_the_entity_set_covers_every_world_collection_a_tenure_can_name`
(`tests/valoria/test_season_invariant_sweep.py:103`), is the falsifier that you did. The deposit rule:
a `content:dispensation` claim in the issuer's ledger (r2 `05:1245`'s artifact). `Record.rung` is
required (`carriers.py:521`), so a writ's rung is decided — the issuer's seat rung is the answer r2
`02` gives. ⚠ **And `issue` still needs an evaluable precondition** — its `requires:` is prose — or it
stays out of `resolvable_verbs()` with an effect (part 1 `§3.2` row 19). That is position 19's, but a
session landing this position must not report `issue` as newly reachable.
**FALSIFIER, sharpened.** `hasattr(w, "petitions")` and `hasattr(w, "dispensations")` are FALSE — not
merely empty.
**WHERE.** `state/world.py`, `state/carriers.py`, `rosters.yaml`, `verb_table.yaml`, `write_matrix.yaml`,
`loop/effects.py`, `loop/witness.py` (the deposit rule), `harness/invariants.py`, `harness/probes.py`.
**GATE.** `11a` (r2 item 5 depends on 2a). ⚠ **Its Arc-2 exposure is `7a`'s**: it adds effect bodies
G4 rewrites, so part 1 `§3.1` lands it after G4.

**15a — GIVE. ≡ POSITION 16, merged 2026-09-25.** r2 `05_LEDGER_AND_BUILD.md`'s row 6 (`give` + body
+ `_req_give` + release-before-mint) names *ratified position: **16***, and position 16 is *"one
two-party verb … moves a Record to another person"*. One piece of work under two numbers — part 1
`§3.4`'s collision again. **The detail is at 16, below.**

**15b — LOSSY TELL.**
**not earlier** `15` — there must be content to lose · **not later** `7a`, whose aperture BO-10 ties
to it.
**INSTRUCTION.** `tell`'s degree-keyed `writes:` are `[]` at every band (`verb_table.yaml`, lawful
per `04 §C.4`), so the lossy copy is NOT a `writes:` change: it is a WITNESS-side deposit change in
`loop/witness.py`'s told channel (`ED-IN-0222`), keyed on `Partial`, carrying the teller's identity
(S3). Content owner: r2 item 8.
**WHERE.** `loop/witness.py`.
**OBSERVABLE / FALSIFIER** (r2 `05:1248`). `Full` → an identical value; `Partial` → exactly one omitted
`to` key or one drifted operand; **the teller's own ledger byte-identical** — RR-P's test, as an
assertion.
**GATE.** 15.

**15c — CONTENT OPERANDS.**
**not earlier** `15` and `16` (r2 dependency 5, 6 → 7) · **not later** `7a`, `19`, `19b`, and `24e`'s
`found` — every one of them needs an operand the closed vocabulary cannot name.
**INSTRUCTION.** Content owner: r2 item 7. `decision/options.py`'s `_derive_operand` reads `to` /
`amount` / `kind` / `at` from a held writ; Q2 gains its third clause in `world_q.questions_for`
(today two); the invariant statement (S5). **This is what widens `requires_operands`** — `rosters.yaml`,
closed on eight names (`actor, subject, from, to, site, kind, amount, floor`) — for `13f`, `19`, `19b`
and `found`.
**WHERE.** `decision/options.py`, `queries/world_q.py`, `rosters.yaml`.
**OBSERVABLE.** `probes` on the corpus: Candidates with writ-derived operands > 0 (r2 `05:1247`).
**FALSIFIER.** A person NOT named in the writ, in the same world, is not asked.
**GATE.** 15, 16.

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
**≡ `15a` / build-order item 6 (merged 2026-09-25).** r2 `05`'s row 6 is this work — `give` + body +
`_req_give` + release-before-mint (⊕ R14) — and names this position. `H-84` (`hole_register.yaml`,
tier 0, `absent`) is the row; `epistemic.py:376-382` says in terms that `H-84` forbids inventing a
`give_record` there to make a case pass.
**DETAIL.** `hold` cardinality is one per object, enforced by `world_q.hold_force` (`:138`) and
`_refuse_bad_hold`; `RELEASABLE_KINDS` includes `hold`, so `_eff_release` already closes the giver's
side. `give` must close-then-open in ONE effect, so the fold never sees two live holders.
**FALSIFIER, added** (r2 `05:1246`'s control). A `give` without the release leaves two holders and
`hold_force` raises; a non-co-located `give` is refused.
**CONFLICT — for G3's pre-flight.** Under G3 the giver's close is T-m, but the RECEIVER's open matches
none of the four admitted bases unless `give` is admitted as the receiver's own act or as a fifth
basis. Position 6 settles it, beside the conferral opener.
**GATE.** 15; lands after G4 in part 1 `§3.1`.

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

**17a — OBLIGEES (added 2026-09-25).**
**not earlier** `7a`, and `13e` (the same function) · **not later** `18a`, which deletes
`Office.establishment` only once this has replaced its reader.
**STATE.** `oblige` writes `Tenure.since`, has no effect, and is not resolvable (`verb_table.yaml`).
`world_q.establishment_of` (`:487`) reads `Office.establishment` and has **zero callers**;
`Office.establishment` is a live field (`state/carriers.py:586`) with a live matrix row and a live
`writes:` entry on `establish` — r2 ~~`05:238-246`~~ `05:214-221`, *three edits, not one*. `_ch_post_remit`
(`epistemic.py:413`) is the channel r2 item 9 rewrites to *"obligees co-located, minting
`inferred`"*; claims by source read `{firsthand: 2174, told_by: 1}`, `inferred: 0` (a 2026-09-17
figure — part 1's ★ row).
**INSTRUCTION.** Content owner: r2 item 9 and `03` §A.9. `_eff_oblige` opens an `oblige` Tenure (a
`tenure_kinds` member, `rosters.yaml:101`); `_req_oblige` reads `Office.binds`; `establishment_of` is
rewritten as a Query over live `oblige` Tenures **WITH this channel as its caller** (r2 `05`
§A.1.5(d): *"with a caller or not at all"*); `_ch_post_remit` is replaced by the obligee channel,
minting `source: inferred`; delete `Office.establishment`, its matrix row, and `establish`'s third
`writes:` entry — coordinate with `13f`, which edits the same row.
**WHERE.** `loop/effects.py`, `loop/predicates.py`, `queries/world_q.py`, `epistemic.py`,
`state/carriers.py`, `write_matrix.yaml`, `verb_table.yaml`.
**OBSERVABLE / FALSIFIER.** The claim-source histogram moves `inferred` 0 → N with `N >= 1` asserted;
and a person NOT obliged to the seat and NOT co-located does NOT receive the `inferred` claim — the
flood control.
**GATE.** `7a` (so, transitively, `15`/`15c`) and `13e` — `13e` first: it is one line in
`_ch_post_remit`, and this position replaces the function (part 1 `§3.9` edge 4).

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

**18a — FIELD DELETIONS (added 2026-09-25).**
**not earlier** `17a` (the `Office.establishment` half), ~~`13d-i` (the `conferral_path` half)~~
`13d-i` + `13d-ii` (r2 item 14 depends on item 10 whole, `05:1254`; the `conferral_path` half is
`13d-ii`'s, i.e. G3 — corrected 2026-09-25) and `18` (the `judging_set` half) · **not later** the ★
gate, which re-measures after it.
**STATE.** All thirteen fields in r2 `05:223-256` still exist: `Tenure.payload`
(`state/carriers.py:59`), `Person.beliefs` (`:457`), `Office.establishment` / `upkeep` / `dates` /
`scope_rung`, `Rung.sites` / `records` / `dates` / `stake` / `transmission` / `judging_set_rule` (in
`_DECLARED`, `:663`), `Site.drawers` (`:513`). `world_q.judging_set` (`:146`) raises `Unspecified` and has
two probe callers (`harness/probes.py:1221`, `:2480`). `world_q.conferral_path` (`:539`) ~~has
none~~ **has one caller, a test** (corrected 2026-09-25):
`test_the_populated_world_has_a_governance_ladder_and_scarce_seats`
(`engine/season/tests/test_season_shape.py:11674`), asserting at `:11753-11756`. That assertion is
the executed check of Jordan's 2026-09-13 subordination ruling (*"the duchy is underneath the
Crown"*, quoted at `:11745-11746`).
**INSTRUCTION.** Content owner: r2 item 14 and `05` §A.1.1(c)–(e). Delete **twelve** fields — ⚠ **NOT
`Tenure.payload`**. r2 `05:229` says *"NOTHING reads it"*; since `13b` it carries the remit grant
(`world.py::_grant_remit`, `carriers.py::Tenure.granted_acts`). `RULINGS.yaml` CAT-6 already priced
this (*"ARM 2's CARRIER IS ON r2's DELETION LIST … un-deleting a field RATIFIED ARCH §B.8 prescribes
deleting"*), so if ARCH §B.8's `term?` replacement is ever built, it carries the grant. Delete
`conferral_path`. ~~— `13d-i`'s rosters are what replaces it.~~ ⚠ **CORRECTED 2026-09-25: the rosters
matched on the TERM "conferral", not the concept.** `conferral_path` is an ancestry walk
(`world_q.py:539-555`, returning `ancestry(w, off.rung)`). r2 `05:450-451` names what supersedes it:
*"superseded by `descendants(w, seat.rung)`, which `03`'s purview rule uses"*, i.e. `13d-ii`'s purview
walk, built by G3. **And it is not caller-free.** Re-point the subordination test's two assertions
onto `ancestry(w, o.rung)`, the primitive `conferral_path` wraps, in the same commit. Deleting the
test with the Query would delete the only executed check of a Jordan ruling. **`judging_set`: position 18 BUILDS
`world_q.judging_set(w, venue, matter)` for `19`'s `determine` (`H-32`), and r2 item 14 deletes the STUB
of the same name.** `18` lands first (the order's own sequence), so this position deletes only the
stub `18` has replaced — never the name.
**WHERE.** `state/carriers.py`, `queries/world_q.py`, `write_matrix.yaml`, `harness/probes.py`,
`tests/test_season_shape.py` (the `conferral_path` re-point).
**COMPLIANCE.** `04:176` — `Rung.judging_set_rule` *"**deleted**; the judging set is a Query over
seats"*.
**OBSERVABLE.** `matrix_rows_without_a_field()`'s report, before and after, as the artifact (r2
`05:1254`).
**FALSIFIER.** `Tenure.granted_acts` still returns the grant for a seated holder after the deletions —
the test that you did not delete the live field.
**GATE.** `17a`, `13d-i`, `13d-ii` (≡ G3, position 6; added 2026-09-25), `18` (part 1 `§3.9` edges 5
and 11).

**★ — APERTURE RE-MEASUREMENT (added 2026-09-25).** A measurement, not a build. Fires once, after
`18a`.
**INSTRUMENTS.** `resolvable_verbs()` (19 of 38 at `952dc21`) · `person_side_eligible` over the roster,
**per HOLDER** — the spine gives 13 holders at 7 depths (part 1 `§3.8b`) · claims by source over one
populated season (`harness.populated 1`) · questions by source (`questions_for`). Content owner:
`01_THE_BUILD_ORDER.md:190-205`.
⚠ **TWO GAPS, STATED NOT FILLED.** (1) **Nothing runs the populated realm for formability or
execution** — `corpus_run` and `register --requirements` score the corpus, and
`test_the_generic_remit_seats_every_office_and_unblocks_the_nine` says so in its docstring
(`test_season_shape.py:5310-5316`). Until an instrument exists, a per-holder re-take re-takes on the
corpus only; say so in the result. (2) The *was* figures are **2026-09-17 values** — re-run, never
re-cite.
**WHAT IS ALREADY ESTABLISHED, so it is not re-diagnosed at the gate:** why `issue` never executes
(part 1 row 19 — two of `resolvable_verbs()`'s gates). The never-attempted set is pinned at `{confer,
convene, revoke, destroy_record}` (`test_season_shape.py:6996`).
**THEN** re-take `CAT-6`'s evidence block and `STR-4`'s conclusion against the new numbers.
**FALSIFIER.** A single flat *"N of 38 unformable"* reported — that is the category error `13b`
exposed.

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
**STATE (2026-09-25). All five are formable by a holder and none is resolvable** — each fails TWO of
`resolvable_verbs()`'s gates: no effect behind a non-empty `writes:` (`loop/driver.py:99`), and a
prose `requires:` with no typed cell and no predicate (`:96-98`). So **each needs an evaluable
precondition as well as an effect**; a precondition left in prose raises `Unspecified` in the fold
(`loop/resolve.py:164-176`). Per verb:
- **`levy`** — `eligibility: ["remit:issue", "presence:<rung>"]`. The source cell named `remit:levy`, and
  `levy` is not a `remit_acts` member; the substitution is DECLARED at the row's
  `eligibility_substitution` and stays an open eligibility question this position inherits (a
  neighbour of `H-52`). `requires: stores(...) >= amount` is untyped: author it as `transfer`'s
  form-2 `stores >= amount` cell.
- **`open_case`** — `remit:determine`, graded `assumption` (`H-52`). Gains `writes: DocketItem.matter`
  and a `docket` branch in the world reader; its typed cell declares stages, as `create_record`'s does.
- **`determine`** — writes `Tenure.degree`; `requires:` names `judging_set` (`H-32`), which exists only
  once position 18 builds it — SC lane, outside this scope, a hard dependency.
- **`issue`** — the effect is `15`'s; the precondition is this position's.
- **`establish`** — `13f`.
**FALSIFIER, added.** Two `levy`s on one larder in one fold: the second refuses (§27.1 scarcity, as
`test_lb3a_two_eaters_cannot_spend_the_same_unit` does for eaters).
**GATE.** ★; 6 (`via`); `15`/`15c` (`issue`'s Record, and every operand); `18` (`determine`).

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
**STATE (2026-09-25).** The rows exist and are named (`comply`, `evade / defy`, `construe` — renamed
2026-09-18 with `construal.impossible`). All three are `eligibility: ["own"]` with no typed cell and
no predicate; `construe` is also `grade: absent` (D18: whose ledger is read). **None is in
`resolvable_verbs()`.**
**IT DEPENDS ON `15` (+`15c`), WHICH PART 1'S ROW DID NOT SAY.** `comply`'s own note in `verb_table.yaml`
says the operand is a Dispensation, and `requires_operands` has no name for one. After `15`, a
dispensation is a `Record`, and the cell can be `form: own_ledger, of: subject` over a
`content:dispensation` claim — the form `tell` already uses. `15c` binds the operand.
**THE EFFECT SHAPE.** Compliance is `writes: []` *"per the term's own row"* — under arm (A) the
compliance itself is the executor's LATER act — so `_eff_comply` may be emission-only. A `writes: []`
verb takes no effect path at all, so the fold's write-nothing refusal (`loop/resolve.py:306-311`) does
not reach it, as long as the row keeps `writes: []`.
**JORDAN — DESCRIBE BOTH ARMS, DO NOT PICK.** `ED-IN-0210`'s fork, `needs_jordan: true` on the live row:
**(A)** one `comply` keyed on the ledger claim answers both an `issue`d dispensation and a
`dispatch`ed order — the falsifier adds *a `dispatch`ed order's `comply` keyed on the same claim
shape*; **(B)** `dispatch` gets its own obey/disobey pair. Evidence leans A. Part 1 `§5` item 2.
**GATE.** `15`, `15c`, and the `ED-IN-0210` ruling.

**19c — MIGRATE (added 2026-09-25).**
**not earlier** `24d-i` — the throttle's substrate · **not later** anything that reads `residence`.
**STATE — AND THE PREMISE CORRECTED.** Part 1's row said *"nobody in Valoria can relocate — `move` is
TRAVEL"*. `_eff_move` (`loop/effects.py:225`) closes the actor's live `contain` Tenure and opens a new
one to the destination (`:260-264`), so `home_of` (`world_q.py:150`) DOES change on a move. **The tree
has one edge for where you are and where you live.** What is missing is the distinction, and
`residence` — a `person_predicates` member (`rosters.yaml:372`), a CLAIM predicate — has no producer.
The ruling (`RULINGS.yaml` RR-2, as quoted in `01_THE_BUILD_ORDER.md` S9): *"must be able to build
hearths and accept people who move settlements"*; *"migration is a verb persons take"*; *"It gives
`residence` its first producer."* `HANDOFF_IN.md` carries it Open.
**INSTRUCTION.** A `migrate` row whose effect re-homes the `contain` edge AND deposits or mints the
residence fact — a WITNESS-side deposit rule or a Tenure kind; the build states which — throttled by
`capacity` at the destination (RR-2). Distinguishing it from `move` means deciding what `move` leaves
behind: **the presence/residence split, an architecture answer once `24d` exists** (§0 test 5, not
Jordan's; part 1 `§5`).
**RIDE-ALONG — A LATENT DEFECT, GAME-LOAD-BEARING.** `_eff_move` appends every destination to
`mover.travel_leg` (`effects.py:272`) and nothing ever clears it — the only other writer is a probe
(`harness/probes.py:2671`). `decision/budget.py:59` subtracts `len(p.travel_leg) *
budget_leg_penalty` (`= 1`) every season, so a person who has moved N times is penalised N every
season thereafter. `(Person, travel_leg)`'s matrix row declares `steps: [MAT, RES]`, and nothing at
MATTER writes it — that unproduced MATTER half is the natural place for a leg to end; if the fix lands
elsewhere, say why. Fix it once, in the commit that touches `travel_leg`; this is that commit. No
guard (`CLAUDE.md` §0.1 pt 5: a one-off defect).
**WHERE.** `verb_table.yaml`, `loop/effects.py`, `loop/witness.py` or `state/carriers.py` (whichever
carries residence), `loop/matter.py` (the leg), `queries/world_q.py` (`capacity`, as a caller).
**OBSERVABLE.** The two disjoint chains of the governance spine (part 1 `§3.8b`): a `migrate` from
chain `a` to chain `b` changes residence; a `move` does not. A person's budget penalty returns to 0
once their leg ends. ⚠ **The spine has no dwellings (added 2026-09-25).** `harness/governance_spine.build`
builds its own `World` with its own hearths (`lr_hearth_a` / `lr_hearth_b`), and the ruling has only
`build_realm` mint dwellings. So on the spine every rung's `capacity` reads the FLOOR, unless
`24d-i`'s decision (4) extends minting to the spine. Run the residence half on the spine. Run the
capacity half on `build_realm`, or on the spine once (4) says it mints. State which.
**FALSIFIER.** A `migrate` into a rung at capacity refuses; a `move` leaves `residence` unchanged; after
N moves and the legs' end, `len(travel_leg)` is 0.
**GATE.** `24d-i` and `capacity` (`24d-ii`, ~~landing here if `24e` has not~~ **which lands here**:
this is its only in-scope caller, since `24e`'s `found` grows capacity and does not call it —
corrected 2026-09-25) · the presence/residence answer.

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
**PRE-FLIGHT, added 2026-09-25 — ONE OWNER AND ONE DENOMINATOR FOR R3, before any R3 number is
compared.** `engine/season/requirements.yaml` quotes R3 at `:142` (22/30 NPC, 34/59 ARC), `:172-177`
(the same row's 30/30 and 54/59 before `ED-FI-0009`), `:263-267` (50 → 84 of 143), `:364-365` (55 → 50
of 143, and U4's 56·55·59·59·48) and `:555` (unmoved at 84 of 143) — over **two denominators**, 89 live
worlds and 143 cases, and no row says which is this position's baseline. Name the owner — `corpus_run`'s
printed R3 line, the `measure:` at `:194` — and the denominator, then make every `measured:` block
that quotes R3 cite that run. No code. Position 11 may take this first; whichever runs first owns it.
**GATE.** 20 (out of this pass's scope).

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
Each waits on its §5 ruling and none blocks another. ⚠ **Not true of `24`'s lettered sub-positions
(2026-09-25)**, which are ruled and do chain: `24d-i` → `24e` and `19c`; `24f` → any `body_step` pick.

**24 SE-BUILD.** After ED-SE-0051 and acceptance: P3 (individuation is a refusal — CENSUS reads the
demand kind and individuates with `causes[]` naming it), P4 (the founding verbs — `found` does not load
today because a `writes:` pair has no matrix row), P1 (dearth reaches the body), P2 under whichever arm
is ruled. `band_floors` also does not load; fix or drop at pre-flight.
**COMPLIANCE.** `04:1030` step 9 — a `dispatch` to a non-existent clerk emits `person.demanded`, and
next season a Person exists whose `person.individuated` cites it. `04`'s F.20 row: **the founding rows
are dropped until a verb is ruled.** **FALSIFIER.** `Person.weight` or the envelope written by anything
but CENSUS/MATTER; or a stored aggregate where a Query is required. **TIER.** `opus`/`opus`.
**STATE (2026-09-25), read with `24f`.** **P1 is `DONE·INERT`**: `loop/matter.py:298-326` writes
`(Person, body)` and cascades death through `remove_person`, shipped at the control arm
(`data/fixtures.py:494`, `body_step=0`, `H-125` swept 0 / 10 / 67; `ED-IN-0247` holds the number).
Its other half is missing: `world_q.py:633-637` derives `at` from `w.sites.get(who)`, so for a
PERSON-keyed crossing the `presence` branch cannot fire. ~~never becomes a Question~~ (Corrected
2026-09-25: `:636`'s `who == p.id` still gives the OWNER the Question. Only the co-present people at
the hearth miss it, as part 1 `§3.3` says.) The repair (`at = parent_of(w, who)` when `who` names a
person) is specified at `proposals/2026-09-10-settlements-factions-populations/02_PROPOSALS_SUBSTRATE.md:54-60`.
**Do not pick the number before `24f` settles the carrier's scale.** **P2** is not in `ED-SE-0054`'s
acceptance — skip it. **P3 NOT STARTED**: `loop/census.py` writes nothing (its own `:34`); the
`(Person, weight)` and `(Person, exists)` `[CEN]` rows exist; `04_EVALUATION.md` grades it *"two writes
refused by the gate, one demand kind authored-only"*. It needs `person.demanded` from a refused
`dispatch` to a non-existent clerk (`04:1032` at current lines, step 9). **P4 is `24e`.**

**24d — SE-CAPACITY. RULED (`ED-SE-0051`, 2026-09-17); SUBSTRATE RULED 2026-09-25; SPLIT IN TWO.**
The ruling: a `capacity(w, rung)` Query over the rung's dwelling Sites, with a FLOOR, never a fixture
table; `found` is the throttle (`RULINGS.yaml` RR-2; `01_THE_BUILD_ORDER.md` S10). ⚠ **Which reading
of "throttle" is taken, stated 2026-09-25:** RR-2's own reasoning (`RULINGS.yaml:1855-1859`). Capacity
throttles POPULATION (its floor is *"applied here to births rather than acts"*), and `found`/`build`
are the lever that GROWS capacity. BO `:1056-1057`'s *"a capacity throttle with no `found` to
throttle"* reads the other way, with `found` as the throttled act. That reading is NOT taken: a
`found` refused at capacity could never add the housing that lifts capacity, so a full rung would
stay full forever. It had no referent:
`build_realm(0)` builds 74 Sites, all `harbour`/`seam`, and the 211 buildings are `hearth` RUNGS
(part 1 `§3.6`). **Jordan chose, 2026-09-25 (`ED-SE-0055`): add a `dwelling` SITE KIND; `build_realm` mints one dwelling
Site per hearth rung; `capacity(w, rung)` queries descendant Sites of that kind** — the literal
reading, at the cost of a new data family and 211 new Sites in every populated world's hash.

**24d-i — THE DWELLING SUBSTRATE.**
**not earlier** nothing — part 1 `§3.1` phase α · **not later** `24e`, whose `build` needs the
`dwelling` kind, and `19c`, which throttles on it.
**INSTRUCTION.** (1) Add `dwelling` to `site_kinds` (`rosters.yaml:896`). The set is extensible by
adding a row — *"THE SET IS EXTENSIBLE AND THE LOOKUP STILL REFUSES"* — and a lookup for an
unregistered kind raises. (2) **The loader then FORCES two rows:** `data/fixtures.py:106-128` checks
`wear_per_season` and `band_floors` against `site_kinds` in both directions and raises `Ungraded` on a
site kind with no row. `site_yield` forces none (`default_cell: 0`). Declare each value under its
existing register row and sweep (`H-07` wear, `H-08` floors). ⚠ **Every Site wears at MATTER, every
season** (`loop/matter.py:383`, `wear = w.fixtures.wear(s.kind)`), and band floors are what crossings
fire on — so a non-zero wear and non-empty floors add up to 211 condition writes, their Events and
their crossings to every populated season. An empty `band_floors.dwelling` cell gives no site-use
verbs and no crossings. ~~Whatever is chosen~~ ⚠ **DECIDED 2026-09-25: ship the CONTROL arm,
`wear_per_season.dwelling: 0` and an empty `band_floors.dwelling`, swept under `H-07`/`H-08`.** This
has the same shape as `body_step=0` and `scar_step=0` (part 1 `§3.3`). The reason is concrete. A
dwelling Site sits at a hearth, and persons live in hearths. With non-zero wear, a dwelling crossing reaches
Q3's `presence` branch (`world_q.py:633-637`: `at` is the Site's rung, the hearth, and its residents
are present) and becomes a live `band_crossed` Question for every resident. That brings `band_crossed`
alive on the populated world, and it breaks `11a`'s premise that the source it deletes contributes 0
("the control is an identity"). At wear 0 no dwelling's condition moves, so no crossing fires and
`11a`'s identity holds. ⚠ **THAT DOES NOT MAKE IT SILENT, and "inert" is claimed only as far as it
is measured.** MATTER emits one Event PER WRITE (`H-12`, enforced in `World.write`), and the wear
loop writes every Site every season whatever its wear (`loop/matter.py:381-396`). So each dwelling
still emits one `condition.worn` per season, 211 more Events per populated season. Their place is the
hearth, so `_ch_co_located` (`epistemic.py:309-322`) can hand them to every resident. **Measure,
before and after, on `build_realm(0)` over one season:** the Event count (expected +211 per season,
all `condition.worn`), claims by source, and questions by source. Label the position **DONE·INERT**
(part 1's `§3.2` legend) only if claims and questions do not move. If they move, say what moved, and
declare it with the hash. A non-zero wear is chosen with a consumer in front of it, at `24e`/`24f`,
never here. (3) `build_realm` mints one Site of kind `dwelling` per `hearth` rung (`harness/populated.py:361`),
at that rung, with an id and an initial condition built the way the producing Sites' are (`:370-374`).
(4) **`build_realm` is not the only builder of hearths — there are three more (list completed
2026-09-25).** `corpus_run.build_at` builds a `person`-scaled case's `hearth` rung
(`harness/corpus_run.py:209-211`) and seats its people in it (`:226-231`). `governance_spine.build`
builds `lr_hearth_a` / `lr_hearth_b` (`harness/governance_spine.py:126`; `governance_spine.yaml:86-87`).
`probes.tiny_world` builds `Hh` (`harness/probes.py:73`). The ruling names `build_realm` only. Decide
for each whether it mints dwellings too, and state it. `build_at` decides whether capacity can vary on
any world `R-05` is scored on. The spine decides whether `19c`'s capacity falsifier can run where its
residence observable runs (`19c`). `tiny_world` decides whether the probes see a dwelling at all. This
is part 1 `§5`, not Jordan's.
**WHERE.** `rosters.yaml`, `harness/populated.py`; `harness/corpus_run.py`,
`harness/governance_spine.py` and `harness/probes.py` only if (4) says so.
`data/fixtures.py` needs no change — its refusals are the check.
**OBSERVABLE.** `build_realm(0)`'s census: Sites 74 → 285 (74 + 211), dwellings == hearth rungs,
rungs unchanged at 375. The content hash moves on every populated world — **DECLARED**, per `CLAUDE.md`
§7.
**FALSIFIER.** Every hearth rung carries exactly one dwelling and no other rung carries any — asserted
as a count equal to the hearth count, with the hearth count `>= 1` so an empty world cannot pass. And
the loader's own refusal, planted: `dwelling` without a `wear_per_season` row fails at load. And the
control arm, asserted: over one populated season, `band_crossed` Questions naming a dwelling Site
`== 0`, while the `dwelling` count is `>= 1` and `condition.worn` Events naming a dwelling are
`>= 1`. The last clause proves the wear loop visited them, so the zero is not an empty population.
**GATE.** — .

**24d-ii — CAPACITY.**
**not earlier** `24d-i` · **lands IN THE SAME COMMIT AS ITS FIRST CALLER** — ~~`24e`'s `found` throttle, or
`19c`'s if that lands first~~ **`19c`'s `migrate`, its only caller in scope** (corrected 2026-09-25).
`24e`'s `found`/`build` mint what this counts and do not call it (`24e`, and `24d`'s reading of
*"throttle"* above).
**INSTRUCTION.** `queries/world_q.py::capacity(w, rung) -> int`: the dwelling Sites at `rung` and at
its descendants. ⚠ `descendants` (`world_q.py:54`) EXCLUDES its own rung and walks `contain` Tenures
between rungs; Sites hang off rungs by `Site.rung`. So the own rung is added explicitly, and a hearth's
own dwelling is counted. **The FLOOR is a table keyed on site kind, beside `band_floors`** (BO S10),
loaded with the same both-direction key check the other site-kind tables get. ~~What its cells hold — the
floor, and if the build needs it, what one dwelling houses —~~ **Its cells hold the FLOOR and nothing
else** (corrected 2026-09-25). The floor is declared with a `row:` and a `sweep:` like every injected
table in `rosters.yaml`, because the ruling fixed the SHAPE, not a number. **The floor is a lower bound
on a derived quantity**: `max(floor, derived)`, the shape of `W5`'s budget floor-of-1 that RR-2's
reasoning cites. ⚠ **What one dwelling houses is NOT a table cell.** A per-kind *"houses N"* cell is
capacity AUTHORED per kind. That is the `hearth_capacity` fixture per `site_kind` Jordan refused
(`RULINGS.yaml:1850-1854`; part 1 `§3.6`), a second home for a fact the Sites carry. BO S10
(`01_THE_BUILD_ORDER.md:1053`) licenses only the floor as a table. The derived quantity is the dwelling
Sites themselves, i.e. their count. If a build needs more than a count, the quantity comes off the
Site (`CLAUDE.md` §0.05 cl.1), never off a per-kind cell.
⚠ **THE CONSUMER THE RULING REASONS ABOUT HAS NO BUILDER IN SCOPE, stated rather than papered over.**
RR-2's floor is *"applied here to births rather than acts"* (`RULINGS.yaml:1855-1859`). A BIRTH, or
whatever eventually grows a population, is what refuses above capacity. Nothing in the tree grows
one. `loop/census.py` owns `weight` and `envelope` and writes nothing: *"NO CLOCK GENERATES
ANYTHING"* (`:33`, `ED-WR-0011` option A). The only envelope write is probe `W9`'s *"BIRTH IS
ENVELOPE WEIGHT"* (`harness/probes.py:1639-1650`). So this Query's one caller in scope is `19c`'s
`migrate`, which moves people and does not grow them. The population throttle the ruling describes
has no subject until a birth-side consumer exists (part 1 `§6`).
**COMPLIANCE.** `04:124` / `ID-13` — no declared-but-unread row. Precedent for "with a caller or not at
all": r2 `05` §A.1.5(d), on `establishment_of`.
**FALSIFIER.** A rung with zero dwellings returns exactly the floor, never 0 — RR-2's stated reason for
the floor. One more dwelling under a rung raises its capacity and every ancestor's by the same step.
And an AST check that `capacity(` has a caller outside `tests/`.
**WHERE.** `queries/world_q.py`, `rosters.yaml`, `data/fixtures.py` (the floor table's load and check).
**GATE.** `24d-i`; rides ~~`24e` or~~ `19c`.

**24e — WORKS & FOUNDING (P4).**
**not earlier** `15` (`record_kinds`), `15c` (`found`'s operands), `24d-i` · **not later** `24f`'s
territorial loop, which needs somewhere to found.
**STATE.** No `found` or `build` row among the 38 verbs. `(Rung, exists)` emits `rung.founded` and
`(Site, exists)` emits `site.built` (`write_matrix.yaml:303`, `:331`) and neither has a producer.
`restore` is typed (`verb_table.yaml:495`) with no effect; `work` has an effect whose delta is deferred
(position 7's pre-flight). `04_EVALUATION.md` grades P4 *"refuses at load — three table corrections
before either verb can be attempted"*: those corrections are this position's first work.
**INSTRUCTION.** Content owner: r2 `04_MATTER_AND_WORKS.md` §A.6 and r2 item 12. A `works` is a `Record`
of kind `works` with `stages` (so `record_kinds`, `15`); `work` advances `stage` (and inherits G4's
accumulator answer); `_eff_restore`; a `found` row and `_eff_found` minting a `hearth` Rung and its
`contain` Tenure through `add_tenure`, which enforces strict ascent (`state/world.py:263`). ~~**throttled by
`capacity` — `24d-ii` lands here**~~ ⚠ **CORRECTED 2026-09-25: `found` is NOT throttled by
`capacity`, and `24d-ii` does not land here.** `found`/`build` are how capacity GROWS. Refusing a
`found` at a rung at capacity would deadlock: a full rung could never add the housing that raises
its ceiling, so any rung that filled would stay full forever. `found` keeps its own preconditions
(well-formed operands, the maker's standing, strict ascent) but has no capacity refusal. It is the
lever RR-2 calls *"the throttle"* (`24d` above). Then a `build` row and `_eff_build` minting a Site
of a `site_kinds` member. ⚠ **A founded hearth has no dwelling until one is BUILT.** `build_realm`'s
one-per-hearth is world GENERATION; at runtime a dwelling exists because someone built it, which is
what makes `found`/`build` the throttle. The works' `ceiling` is decided off the emission log (r2
`04` §A.6).
**WHERE.** `verb_table.yaml`, `write_matrix.yaml`, `loop/effects.py`, `loop/predicates.py` or typed
cells, `rosters.yaml`. (~~`queries/world_q.py`~~ was there for `capacity`, which is `19c`'s now.)
**COMPLIANCE.** `04:1084` F.20 — *"the world only decays — nothing is ever founded or built"*.
**OBSERVABLE.** `census` shows exactly one more rung after one `found`; a Site's condition rises under
`work` on a works Record.
**FALSIFIER.** A `text` Record is NOT advanced by `work` (r2 `05:1252`'s control). ~~a `found` at a rung
at capacity refuses~~ (inverted; corrected 2026-09-25) **A `found` then a `build` of a `dwelling` at
a rung whose population is at capacity SUCCEEDS**, and that rung's dwelling count, and so every
ancestor's count, rises by exactly one. Assert the count before and after, not only the success
Event. If the build lands with `19c`, read the rise through `capacity`. The refusal belongs to the
consumer: a `migrate` into a full rung (`19c`), and eventually a birth, which nothing builds yet
(`24d-ii`).
**GATE.** `15`, `15c`, `24d-i`; ~~carries `24d-ii`~~ (`19c` carries it); after G4 in part 1 `§3.1`.

**24f — SUBSISTENCE IS TERRITORIAL (`ED-IN-0255`, ruled 2026-09-18).**
**not earlier** G2, which rewrites the same file's gate sites · **not later** any `body_step` pick and
any claim that P1 is done.
**NO CONTENT OWNER** beyond part 1 `§3.7` — this entry is the specification (part 1 `§6`). The ruling:
*"subsistence/starvation should largely be an abstract/governance issue … NPC synecdoches that just
represent the overall population affected … i don't think having lords and guild members etc worry
about subsistence is worthwhile"*; *"it's a territorial issue"*.
**WHAT THE TREE ALREADY HAS FOR IT.** The cohort primitive — *"A COHORT IS A PERSON AT weight > 1. ONE
CLASS"* (`state/carriers.py:447`) — and its test,
`test_lb3a_a_cohort_eats_by_its_weight_and_not_by_its_head_count`
(`engine/season/tests/test_governance_build.py:289`); `Rung.envelope` as the territorial population
carrier; MATTER's per-eater draw at `nearest_store` (`world_q.py:172`, item 3a).
**INSTRUCTION — SPECIFY BEFORE BUILDING.** Which persons bear subsistence, which are exempt, and whether
P1's body write moves to the cohort only. **CANDIDATE — §0 test 5, NOT Jordan's (part 1 `§5`):**
`weight > 1` eats; `weight == 1` — a named person, the ruling's *"lords and guild members"* — is
exempt. It changes who starves, so the antagonist attacks it hard; the NUMBER stays `ED-IN-0247`'s.
It re-opens `test_w8`'s retired drain guard (part 1 `§3.7`): rebuild that guard on the territorial
quantity.
⚠⚠ **THE ATTACK LANDED (2026-09-25): AS THE TREE STANDS, THE CANDIDATE IS DEAD ON ARRIVAL.** Nothing
mints a `weight > 1` person on any built world. `Person.weight` defaults to 1 (`state/carriers.py:450`),
and every builder constructs persons without it: `build_realm` (`harness/populated.py:420`),
`build_at` (`harness/corpus_run.py:219`) and the spine (`harness/governance_spine.py:129`). The one
heavier person in the tree is a test crowd, `Person("crowd_1", …, weight=40)` (`harness/probes.py:744`).
MATTER's draw is over every housed person, weighted by `weight` (`loop/matter.py:240-256`). So
*"`weight == 1` exempt"* leaves **zero eaters on every built world**. That switches off `3a`'s draw and
P1's body write entirely, and part 1 `§3.7` says *"nothing here licenses deleting working code"*.
**REQUIRES, BEFORE THE CANDIDATE CAN BE TAKEN, and missing from this entry until now:**
- **A producer of synecdoche cohorts.** Name what mints them, and from what. `Rung.envelope` is the
  territorial population carrier, but no built world writes it; the only envelope write is probe
  `W9`'s (`harness/probes.py:1639-1650`). Name the step that mints them: world generation, or CENSUS,
  which owns `weight` and `envelope` (`loop/census.py:1`) and by ruling generates nothing on a clock
  (`:33`, `ED-WR-0011` option A).
- **The exemption lands in the same commit as that producer, or after it**, never before. Its
  falsifier asserts the eater count on `build_realm(0)` is `>= 1` before and after, so the exemption
  cannot silently empty the pass.
This is a precondition, not a settled design. Until the producer is named, **the candidate is not
taken**, and `24f`'s specification is incomplete (part 1 `§6`).
**WHERE.** `loop/matter.py`'s subsistence pass (`:246-326`), `queries/world_q.py`, the test.
**FALSIFIER.** Under a non-zero `body_step` arm: a `weight == 1` office-holder at a rung in dearth keeps
their body; a `weight > 1` cohort at the same rung draws and its body moves. The rebuilt drain guard
asserts it observed `>= 1` cohort drawing **on a built world, not only on the probe crowd**. A guard
that passes only on `probes.py:744` is the dead-on-arrival case above, passing.
**CONFLICT.** `loop/matter.py` with G2 (8 sites) and `11a` (`w.crossings`) — part 1 `§3.9`.
**GATE.** G2; before any `body_step` pick (part 1 `§3.9` edge 8).

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
