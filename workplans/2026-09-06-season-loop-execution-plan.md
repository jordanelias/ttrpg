# THE SEASON LOOP — ARCHITECTURE AND EXECUTION PLAN, AS ADJUDICATED

## Status: **PROPOSED, and held back from `ED-1094`'s merge-ratifies default — loudly, per `CLAUDE.md` §2.**

Merging this file ratifies nothing in it. Under §0.05 it is **reference**: delete it and the game
behaves identically, because every mechanism it names lives in `engine/season/`'s registries, in
`shape.py`, and in `engine/season/tests`. Numbers here are commands; a number typed without one is a
defect in this file.

**What it supersedes.** `relay/PLAN_v2.md` **entirely** — twelve of its claims were wrong and are
corrected in §0 rather than dropped, and its two escalations are both gone (D5 mooted by Jordan's
dismissal of canon constraints, D6 ruled by R1). It also supersedes the five agonist proposals as
produced, and PLAN_v2's §4/§4a wave tables.

**What it does NOT supersede.** `workplans/2026-09-05-post-adoption-execution-plan.md`, whose own
status line forbids exactly that — *"superseded by its own completion — not by a successor plan"*.
Its §0–§3 rulings stand unrestated; what is replaced is its §4 wave table, which covered two of seven
scales. It does not supersede `architecture/` (Layer 1, RATIFIED 2026-09-05, ED-IN-0202), which it
cites throughout and never overrides.

> **Scope this was produced under, stated because it shows in the citations.** `systems/`,
> `engine/autoload/` (except `dice_engine`, cited by name), `engine/mc_v18.py`, `engine/cross_scale/`,
> `engine/tests/` and `canon/`'s GD-* constraints were **not read**. `engine/substrate/` **was** read,
> on Jordan's end-of-session authorisation, and that read is what produced correction §0 #1 — the
> single most consequential item in this document.

---

## THE RESULT, FIRST

**Jordan's five directives this session added NO WORK.** R3's six requirements are six links of one
loop, and every link is already a tier-0 register row. R4's churn lands on `F.20`, already open. R5's
bureaucratic bearing lands on `H-84`, already open and already tier 0. R6's domain echo is **already
built except two links**. R7 ruled *against* the mechanism that would have added the most work — the
magnitude carrier — and in favour of the one the architecture already has.

**Three things changed, and only three.**

1. **The ORDER.** `H-62` (an interior write) and `H-84` (paper that moves) become first-rank, because
   R7 makes them the only two roads by which any normative aggregate can move at all. Two items no
   prior plan carried — **2.6, the reaction source**, and **2.7, paper** — enter the critical region,
   and they are what make propagation a game rather than a chronicle.
2. **`keys.py` LEAVES THE PERMANENT SET.** "The substrate is permanent" is true of `dice_engine`,
   `composition.py`, `descriptors.py`'s attribute half and the exporter *pattern*. It is **false of
   the Key half**, which implements in live code the three things `architecture/meta/08_DATA_AND_KEYS.md`
   refuses by name, and which the adopted loop imports **not once**.
3. **THE ESCALATION COUNT IS ZERO.** Twelve candidates were examined; every one closes at one of
   §0's five tests. `python engine/season/register.py --counts` shows **113 rows and zero
   `needs_jordan`** today, and this plan does not raise it.

---

# §0 · CORRECTIONS TO THE RECORD — twelve, ranked by what would make the plan wrong

Marked in place. A reader must see what was believed and why it failed.

### 1. ⚠ **"The substrate is permanent" is TRUE of the dice/leaf half and FALSE of the Key half.**

`workplans/2026-09-05-post-adoption-execution-plan.md:41` puts
`substrate/{keys,descriptors,composition,stubwire,canon_buckets}.py` in one stratum and calls it
**permanent**. Read in full, that is two different things wearing one label.

| in `engine/substrate/keys.py` | refused by name in `architecture/meta/08_DATA_AND_KEYS.md` |
|---|---|
| `TickScheduler.subscribe(type_id, callback)` + `self.subscriptions` (`keys.py:506-507`) | `:86` — *"There is no bus, no signal, no subscription table."* `:96` — *"Nobody subscribes. The emitter declares no recipient."* |
| `Target = (actor_id, role, impact_vector: axis→signed magnitude, stat_deltas: stat→delta)` (`keys.py:88-105`) | `:89-91` — *"An Event that knows who it is for is an Event that CANNOT BE MISATTRIBUTED, and misattribution is a feature."* |
| `cascade_depth`, `schedule_emission` at parent+1, `drain_tick`, deferred `_pending_apply` at the accounting boundary (`keys.py:463-600`) | the Echo refusal — *a magnitude gated by scope, clamped, targeted at a scale, applied at a commit* |

**`Key` is the Echo, close to field-for-field.** And **the adopted loop uses none of it.** The loop's
**only** import from `engine/` anywhere is `dice_engine` (`shape.py:6604-6605`) — no `KeyLog`, no
`TickScheduler`, no `TypeRegistry`, no `descriptors`, no `composition`. The two systems are
**disjoint, not layered**.

**The consequence for this plan, and it is why this is correction #1.** `World.manifest`
(`shape.py:2633`) is the loop's own re-invention of the boot roster; it is populated by exactly
`probes.py:97` and two tests, and read by `shape.py:3039-3042`. Building persistence or composition on
the Key layer imports the refused mechanism back **through the floor**, where it is hardest to see.
R-H (§2) deletes `World.manifest` in favour of `composition.py`, which is the same idea done right.

### 2. ⚠ *"A seam returns a `Margin`, never a band"* — **WRONG.**

PLAN_v2 §1 and its §4a seam contracts were written against `Margin`. The ruled return is **the
subsystem's own result**. `degree_of` (`shape.py:6653-6687`) is the **one** reader and accepts either
a scene (`"wound_state" in result`, `:6666`) or a margin (`"net"`/`"ob"`, `:6668`), and refuses a
result carrying neither. `rosters.yaml:461-463`'s seam table says **out: a degree**, not a Margin.
**Combat is exempt from the margin ladder by Jordan's 2026-09-03 ruling**, quoted in the code at
`shape.py:6647-6648`: *"the degree is READ OFF THE SCENE."* Every seam contract in §4a is rewritten on
this.

### 3. ⚠ *"Investigation Failure deposits a FALSE claim — the deception mechanism"* — **WITHDRAWN. No source.**

PLAN_v2 item 4.5 and its falsifier asserted it. The table declares the opposite:
`verb_table.yaml:498` — `emits_on_refusal: ["finding.none"]`. A claim minted for a finding that did
not happen is **PART D row 5's defect by name** (`04_CODE_ARCHITECTURE.md:934` — *a success Event for
a write that did not happen*), now enforced at the write. **Deception is not a lie the engine tells
the investigator.** It is **a forged document read in good faith** — R-D, and it already has its
carriers: `forge` (`verb_table.yaml:229`) writes `Record.forgery_quality` and emits
`record.created` (`:233-234`), the **same kind** `create_record` emits (`:153`), *so a document's
holder cannot tell*.

### 4. ⚠ **PLAN_v2 item 0.3's artifact is unrunnable, and its subject is gone.**

The artifact was *"`register.py --counts` → `needs_jordan` count rises by exactly 2"*. `--counts`
(`register.py:709-720`) prints rows, source buckets, grade buckets, tier 0/1, `absent_uncited` and
ARTIFACT 0. **It emits no `needs_jordan` count at all** — the only print of that flag is
`register.py:680`, in a different mode. And the two rows are gone anyway: **D6 is closed by Jordan's
R1 ruling; D5 is moot on his dismissal of canon constraints** (SESSION_STATE §A.3). **Escalation
count re-derived: ZERO**, and `python -c "import yaml; print([r['id'] for r in yaml.safe_load(open('engine/season/hole_register.yaml'))['rows'] if r.get('needs_jordan')])"` returns `[]`.

### 5. ⚠ *"`matter` only decays"* — **MINE, AND WRONG.**

`SeasonDriver.matter` **credits** stores from `SITE_YIELD` every season: `shape.py:5539-5560` writes
`(Rung, yield)` and then `(Rung, stores)` with `credited = prior + produced`. The world has a source.
**`F.20`'s real gap is narrower and it survives:** *nothing FOUNDS or BUILDS*
(`04_CODE_ARCHITECTURE.md:1082` — *"the world only decays — nothing is ever founded or built"*).
`Rung.exists`/`Site.exists` are RES rows with no producing verb; the 32-verb table has no `found` and
no `build` (`grep -n 'verb: *"' engine/season/verb_table.yaml` → 32 rows). Item **2.8**.

### 6. ⚠ *"`holder(office)` is a Query"* — right conclusion, **wrong symbol**, and this corrects my own first sharpening.

I wrote that no named Query exists and the derivation is duplicated inline. **`Query.hold_force(w, obj)`
EXISTS** — `shape.py:3151-3158` — and it does more than derive: it enforces S15's *"`hold` is 1 PER
OBJECT"* and **raises `Forbidden` on a second live hold**. The comprehension I cited as a duplicate is
the **body of that function**. There is no one-rule-lives-once defect here; the rule lives once and is
guarded. R6's chain reads `Query.hold_force`, never `holder()`. (`Office`, `shape.py:2438-2450`, has
no `holder` field — PART D row 11, `04:941`.)

### 7. ⚠ **The ten `scale:` keys are not "ruled deleted now".**

PLAN_v2 §0·C moved a wave-1 item on the reading that `04:173` had ruled them deleted.
`verb_table.yaml:55-64` says the opposite, in capitals: *"⚠ DO NOT DELETE THE TEN KEYS YET… THE SCOPE
OF THE SEAT BEING EXERCISED — `Act.via.scope` — not a column on the verb. The key is retired when
`Act.via` carries the scope."* The ten rows are `verb_table.yaml:126,138,169,180,192,216,239,331,437,459`.
**They retire as item 1.3's LAST step**, after `Act.via` lands — not before, and not in wave 4.

### 8. ⚠ **PLAN_v2's "ONE grid engine, REPLACE not wire" was judged without the in-bounds contract.**

The conclusion is defensible (`T-l`, `01_AXIOMS.md:411` — *"A cohort is a `Person` at weight > 1,
never a subclass"*), but it was reached without reading the seam contract that already exists and is
in bounds (`rosters.yaml:457-467`), and it collapsed a wiring item and an unbuilt-design item into
one row. **Re-sequenced into two:** **4.3a** wires mass battle behind the **existing** seam, contract
unchanged; **4.3b** builds the grid engine as a **replacement behind an UNCHANGED seam**. That is the
whole point of a seam (`rosters.yaml:455-456` — *"A seam survives a rebuild of the subsystem behind
it"*), and splitting them means 4.3b's schedule risk never blocks 4.3a's measurement.

### 9. ⚠ **Decision 1 Step A already LANDED. Do not redo it.**

`tools/evacuation_plan.py:191-219` carries `R-SUPERSEDED-RETAINED-PENDING-R04` (seven code-bearing
subsystems, verdict `keep`, reason inline) and `R-SUPERSEDED-DOC-ONLY` (the five with zero `.py`).
`tests/valoria/test_engine_does_not_import_systems.py:541-567` carries `R04_PENDING_SUBSYSTEMS` (12)
and `R04_PENDING_ROLES` (19) as a **shrink-only** ceiling. Item 0.5 of the post-adoption plan is
**done**; this plan's wave 0 does not repeat it.

### 10. ⚠ **Two rosters for one concept ARE live — for event kinds.**

`engine/engine_params/key_types.json` declares `type_count: 55`, generated from a tree this scope
excludes, and it is one of the typed exports **the Godot port ingests**. The loop's roster is
**DERIVED, and it is 85** — `08_DATA_AND_KEYS.md:73-76`: *"THE REGISTERED KIND ROSTER IS DERIVED, NOT
AUTHORED — computed as the union of every emission column in the write matrix and the verb table. The
log refuses any kind not in it."* Two rosters, one concept, and the port is being fed the wrong one.
**R-G resolves which the port ingests; item 4.8 exports the derived one.**

### 11. ⚠ *"Converting `engine/season` to dotted imports moves no requirement"* — **OVERTURNED.**

It is the workplan's §6 trap 9 and it is wrong. Package-qualified imports are **the precondition of a
single-owner resolver**: `composition.py:66-67` resolves a role by splitting `module:attr` and calling
`importlib.import_module(mod_name)`, which requires a dotted path. And the defect is live and named:
`shape.py:6741` does `import combat_seam` by **bare name** after `combat_seam.py:93-96` puts a
subsystem directory on `sys.path` — exactly the **second-identity** defect `CLAUDE.md` §3 records for
`combat_bridge`. Item **1.6**, and it is a root.

### 12. ⚠⚠ **THE DOMAIN ECHO'S MISSING LINK IS A RECEIPT DEFECT, AND IT IS A NARROWER BUG THAN "RECEIPTS ARE UNBUILT".**

`_apply_write` mints `[StateChange(t, "set", "Act", fld) for t in touched]` (`shape.py:6058`), where
`touched` is whatever ids the effect returned. `_eff_kill` closes **every** Tenure naming the dead
person — `for t in list(w.tenures): if (t.subject == who or t.object == who) and t.live: t.until = w.tick`
(`shape.py:5268-5273`) — and then **returns `[who]`** (`:5274`).

> **So the `Tenure.until` receipt's subject is the DEAD PERSON, not the tenure.** No claim about the
> **vacated office** can ever be deposited, because WITNESS mints
> `Claim(cid, pid, subj, e.kind, …)` off the Event's subject, and the office is never a subject.

This is not the general Receipt gap (`before`/`after` are `None` at both emitters — `shape.py:2915`
mints `StateChange(subj, "set", wclass.value, fieldname, None)`, and `StateChange` at `:2095-2103`
carries `delta`/`spec` and **no `before`/`after` at all**). It is a **specific, cheap, first-rank
fix**: the effect must return ids **per field**, so a Tenure write's receipt names the Tenure.

---

# §1 · THE FRAME

| stratum | what it is | disposition |
|---|---|---|
| **LAYER 1 — `architecture/`** | axioms, theorems, idioms, PART D's impossibility rows, PART F's holes | **reference for the mechanism, binding as agent instruction** (`08:3`, and `CLAUDE.md` §0.05). Layer 1 says what may not be built; the code says what the game does |
| **LAYER 2 — the loop** | `engine/season/shape.py` (6,771 lines) + `rosters.yaml` + `verb_table.yaml` + `write_matrix.yaml` + `engine/season/tests` (181 passing) | **the only driver.** `SeasonDriver.season` (`shape.py:6470-6486`) is the one place `t` advances. ⚠ A **fourth** registry is opened at `shape.py:6505` — `references/module_contracts.yaml`, on the seam path. **Removed by 1.6**, which replaces the read with a resolved composition role |
| **THE SEAMS** | attach · in · out, and nothing else (`rosters.yaml:457`) | **the engine behind each is REPLACEABLE** — Jordan: *"ignore their shapes. we will be rebuilding probably"* (`rosters.yaml:451`). This is what licenses 4.3b to replace an engine without touching a contract |
| **THE ENGINES** | personal combat, mass battle, social contest, and whatever replaces them | **out of bounds as a source.** Each specified by its seam contract, never by reading it |
| **THE PERMANENT LEAVES** | `dice_engine::degree_from_net` (the one ladder, `shape.py:6653-6687` its one reader) · `composition.py` (role → module by string, behind a blocking exporter `--check`) · the **authored → exporter → `--check` → cooked → one-reader** pattern, whose worked instance is `references/world_initial_state.yaml` → `tools/export_world_initial_state.py --check` → `engine/engine_params/world_initial_state.json` → `engine/substrate/world_initial_state.py` · `descriptors.py`'s **attribute half** (`ATTRIBUTES`, `ATTRIBUTES_PENDING_TENTH`, the scale, the conviction roster) | **permanent.** These survive the retirement and are what the loop composes on |
| **THE OLD DRIVER — AND THE KEY HALF** | `mc_v18.py`, the autoload driver set, `engine/tests/` goldens — **and now `substrate/keys.py`, `engine_params/key_types.json`, `descriptors.py`'s `FACTION_STATS`/`TERRITORY_STATS` (`descriptors.py:65,:68`), `stubwire.py`, `canon_buckets.py`** | **transitional.** ⚠ **This row is §0 #1's whole content.** The Key layer is the old driver's, is architecturally refused, and has **zero consumers** in the adopted system. ⚠ **`stubwire` and `canon_buckets` belong here for their OWN reason, not by association with the Key argument** — they were first swept in as *"leaf helpers of the driver"*, which is weaker than the Key half earns and would not survive a challenge. The real ground, verified: neither is referenced anywhere in `engine/season/` (grep returns nothing), and each names its owner in its own docstring — `canon_buckets.py:1-4` was **relocated out of `engine/autoload/game_state.py`** and buckets for it; `stubwire.py:1` is *"the single owner of explicitly-flagged not-built"*, i.e. the stub counter `m1_acceptance` row 1 reads off the old driver's probe. **They are the driver's instrumentation and retire with the driver. The Key half retires for a different and stronger reason: it is refused by argument (§2 R-A).** Two rows, two grounds, deliberately not merged |

**Two channels decide every wave** (`rosters.yaml:434-441`, ruled 2026-09-05):

- **ACTORLESS** — `matter()`. No scene, no deliberation, no person. ⚠ This is NERS **R**'s half with
  no player in it (§0.06: *emergent hooks and scenarios WITHOUT player involvement*), and it is the
  channel that makes the world generate drama when nobody is looking.
- **ACTED** — `deliberate()` → `resolve()`. A person chose; a seam may be called at RESOLVE (S39,
  exactly one place, `shape.py:6689`).

Both converge at `witness()` into **one log** — already true in code (`shape.py:6479-6483`, *"S19.5 —
ONE LOG, NOT TWO"*). **Which channel a scale attaches to is the first question §4a asks of it, and it
is not a taxonomy: it decides whether the scale costs a scene.**

⚠ **THE SCENE IS PLAYER GRANULARITY.** Jordan: *"only players really need the scene in its entirety."*
`rosters.yaml:442-446` already binds the tick to it: *"Do not implement the tick as 'every person gets
a scene per round'."* `shape.py:5655` iterates **every person in the world** once per deliberation.

**⚠ THREE OF FIVE WITNESS CHANNELS ARE BUREAUCRATIC, AND THEY ARE STARVED.** `rosters.yaml:406-410`:
`document_key` (*holds a live `hold` Tenure over something the Event CHANGED — a `changes[]` subject; ⚠ **this read "the Event's subject" until `R8.4` landed 2026-09-07, PR #379**, which is why the channel could not fire on a single act*), `post_remit` (*holds an office
whose remit covers the verb*), `chronicle` (*a `binding_decision` verb — public because
institutional*). Only `co_located` is memory-of-presence. **`H-84` starves the first**: no verb moves a
Record to another person, so *"the only person holding it is its maker"* and `document_key` can never
fire for anyone else. That is R5's mechanism sitting dead in the tree, and item **2.7** is the whole
of the repair.

> ⚠ **AMENDED 2026-09-07 (PR #379) — THE PARAGRAPH ABOVE IS HALF WRONG NOW, AND THE HALF THAT SURVIVES
> IS NARROWER.** `R8.4`'s repair landed: the predicate reads `changes[]`, so `document_key` fires on
> acts. **`H-84` starves the RECORD route only.** The STORE route was always open and nobody had
> noticed — `_eff_transfer` subjects its `StateChange`s to the RUNGS, so a person holding the
> destination rung witnesses a `transfer` they took no part in. Executed and pinned by
> `test_r8_4_document_key_reaches_a_non_author_through_a_store`. **So R5's mechanism is not dead**, and
> item **2.7** is the whole of the repair *for Records*, not for the channel.
>
> ⛔ **AND THE REPAIR IS IN ONLY ONE OF THREE LIVE COPIES.** `_ch_document_key` exists at
> `proposals/2026-09-01-season-loop-tests/tracer/shape.py` (repaired), at `engine/season/shape.py` on
> **PR #371** (unrepaired) and at `proposals/2026-09-01-season-loop-tests/season/shape.py` on **PR #378**
> (unrepaired) — verified by reading all three. This plan is written against `engine/season/`, which
> does not exist on `main`, so **the copy this plan's item 2.7 would build on still carries the bug.**
> Whichever of the three trees becomes the head must carry the repair; §8's *never re-implement a rule*
> is already broken here and the repair did not cause it.

---

# §2 · THE DECISIONS

> **Run through `CLAUDE.md` §0's five tests** — superseded → irrelevant → answered by a design
> document → answered by precedent → answered by what the architecture makes obviously right —
> **and against the six integrity tests, which are R3's own six requirements**: propagation across
> scales · domain echoes · rippling in all directions · a probabilistic world · driven by character
> interiorities · compromised by external incidents and pressures. **Escalate only what survives all
> five.** Twelve candidates were examined. **None survives.**

### R-A · The Key/Echo layer — **REFUSED BY ARGUMENT ON ALL FIVE OF JORDAN'S CRITERIA, not by deference**

R2 makes the ratified refusals **instrumental, not terminal**: each must be justified against
*dynamic · capable · flexible · emergent · persistent*, or changed. R2 also names the trap — most of
them were derived to serve exactly those properties, so a naive reading reduces what it means to
increase. **The null result is a real finding and must be ARGUED.** Here it is, argued.

| criterion | readmitting `Key`/`Target`/`TickScheduler` | verdict |
|---|---|---|
| **DYNAMIC** | `choose` receives no World — `def choose(p, v, s, ask_budget)` (`shape.py:3494`), PART D row 2 (`04:931`). **A pushed magnitude therefore moves no decision.** It adds motion to the channel that is already saturated: world divergence is ~100%, and it is *later-decision* divergence that sits at ~4% | **worse** |
| **CAPABLE** | its carriers do not exist. `impact_vector` lands on conviction axes — PART D row 18 (`04:948`), **STRUCTURAL by signature**: the interior writer takes `PersonInterior` and no ledger reference. `stat_deltas` lands on stat blocks the new architecture deletes — PART D row 8 (`04:937`), *a stored aggregate*, no field slot | **inert** |
| **FLEXIBLE** | **WITNESS COMPUTES the observer set** (`08:94-96`), so a new mode of play needs no registration anywhere. A subscription table means **every** mode must register, and a mode that forgets is silently deaf | **strictly worse** |
| **EMERGENT** | a delivered magnitude reaches every target identically. That **deletes misattribution** (`08:89-91`, *"misattribution is a feature"*) **and covert action** (`08:99-101`, *"An act nobody was present for produces no first-hand attribution anywhere — not because it was marked hidden, but because the observer set was empty"*) | **deletes two features** |
| **PERSISTENT** | `_pending_apply` (`keys.py:500`) holds **closures**. No save can carry a closure; a snapshot taken mid-cascade is either wrong or must refuse | **unserialisable** |

**Cost of readmission, stated so it is not paid by accident:** two logs, two content hashes
(`KeyLog.content_hash` at `keys.py:453-461` over the key log; `World.content_hash` at
`shape.py:2995-3035` over game state), two kind rosters (55 authored vs 85 derived, §0 #10), and a
subscription table. **REFUSED. Closes at test 5, and it closes on the argument, not on the ratified
sentence.**

### R-B · The domain echo — **ADMITTED. A fact, not a magnitude. Built except two links.**

R6 is **not** the refused Echo — different object, so no axiom moves. The trace, verified end to end:

`kill / wound` (`verb_table.yaml:250`, `contests: "the body"` at `:254`, the **only** row declaring
`contests:`) → `contest()` → `combat_seam` → `degree_of` reads `wound_state` off the scene
(`shape.py:6666`) → `Felled` → `_eff_kill` closes every Tenure naming the dead person
(`shape.py:5268-5273`) → who holds an office is **derived from live `hold` Tenures**, never stored
(`Query.hold_force`, `shape.py:3151`; `Office` has no `holder`, `:2438-2450`) → **every subsystem that
asks now gets "nobody"**, with no push and no copy to desync.

**MISSING LINK 1 — the receipt's subject (§0 #12).** The `Tenure.until` receipt names the dead
person. Fixed in **1.2**.

**MISSING LINK 2 — NOTHING REACTS, and this is the plan's spine.** Q2 fires on
`c.when == landed and (c.subject == p.id or c.subject in mine)` (`shape.py:3900-3903`). A subordinate
*obliged to the office* gets a Question. **An ambitious person does not** — their ambition is a
`commit` Tenure to an OUGHT Proposition **about** the office (`headless.py:74-81`), and Q2 never looks
there.

> **PROPAGATION WITHOUT REACTION IS A CHRONICLE, NOT A GAME.**

**THE RULE: widen Q2's third clause to the SUBJECT of any OUGHT Proposition the person is committed
to.** Not a fifth source. `question_sources` is a **closed, ordered** roster of four
(`rosters.yaml`), and its order is semantic — `hole_register.yaml:628` records, measured, that adding
or reordering sources silently rules *what every NPC does first*. **The precedent is Q4's own
addition** (`shape.py:3873` — Q4 `need` was added as a source only because an NPC with a standing
ambition and a quiet season formed no candidates at all). Widening a clause inside an existing source
costs no ordering ruling. Item **2.6**. Closes at **test 4**.

⚠ **Constraint the fix must respect:** `choose` receives no World. A person cannot notice a
world-fact directly — it must reach them through **their ledger or their View**. **So R5 and R6 are
the same mechanism**, and 2.6 without 2.7 is a widened clause with nothing to fire on.

### R-C · Churn — **`AX-5` STAYS AT THREE. Route 4 refused at test 3, with its cost stated.**

`AX-5` (`01_AXIOMS.md:151`): *the world moves by itself in exactly three ways — matter, bodies, and
the fading of memory.* `:154-160` is explicit that **the membership of the list is the stipulation**
and the prohibition is the derivable part (`T-c`, `:304`).

| route | needs an axiom moved? | where it lands |
|---|---|---|
| **1 · churn by NPC action** | **no** — `AX-1`-native. Needs the 26 non-executing verbs alive (6 of 32 execute today) | 2.4 ×N |
| **2 · churn by matter** | **no** — generative harvest/growth is **motion 1 with the opposite sign to silt**, and `matter()` already credits (§0 #5). Plus **FOUNDING as an act**, which is `AX-1`-native and is `F.20` | 2.8 |
| **3 · churn by authored occasion** | **no**, and it is already ruled lawful: `01_AXIOMS.md:177-178` — *"A world-generation roster is not a clock and is lawful; a population that grows on its own is not."* `F.31` (`04:1135`), entirely unbuilt | 4.6 |
| **4 · spontaneous generation, no author** | **YES — a fourth motion** | **REFUSED** |

**Route 4 closes at test 3.** `01_AXIOMS.md:174-178` already ran this exact question for CENSUS
individuation and answered it: *"individuation is authored: the demand is its author, and `T-c` is
satisfied rather than evaded. `AX-5` says three."* **The cost, stated rather than waved at:** an
unauthored change has no antecedent, so it roots at `[ROOT]` (`01:979`) — it is **unplaceable**
(`place_of` has nothing to derive from), **unwitnessable** (no channel predicate can bind), and
**unobstructable** (nobody to obstruct). And it buys nothing routes 1–3 do not.

⚠ **Do not answer churn with a clock.** `T-c` (`01:304`), PART D row 17 (`04:947`), loader invariant 5.

### R-D · Diegetic persistence — **`H-84` IS SPINE, and the shape is already in the tree**

R5 names two persistences and this plan carries both distinctly: **engine** persistence (R-F) and
**DIEGETIC** persistence — *what the world itself holds, in objects that outlive the witnesses and can
be moved, copied, forged, seized and burned*. The second is a game mechanic.

**The finding that makes it buildable without a new type.** A **seat** cannot `hold` — PART D rows
12/13 (`04:942-943`), and `hold`'s subject is `PersonId` (row 14, `04:944`). But:

> **`Record.rung` EXISTS (`shape.py:2416`) AND HAS NO MATRIX ROW.** `write_matrix.yaml` carries five
> `Record` rows — `exists`, `forgery_quality`, `matured`, `stages`, `ttl` — **and no `rung`**.
> **AN ARCHIVE IS A PLACE**: a Record at a rung held by nobody. **A chancery can be raided because it
> is somewhere.**

That single missing matrix row is what turns `H-84` from "invent a transport" into "declare a cell".

**The producers, all of them compositions of existing primitives:**

| producer | built from |
|---|---|
| **deposit** | `release` on `hold` (D4's generic closer) + the Record **stays at its rung** |
| **take** | a `hold` opener, eligibility `own` + `presence` — the two kinds already in `eligibility_kinds` |
| **give** | release + take: **two acts, two owners**, which is what PART D row 12 requires of any transfer of a relation |
| **send / carry** | a `Record.rung` write — the matrix row above, and nothing else |
| **copy** | `create_record` from the maker's **own ledger**, which is why a copy can be wrong |
| **destroy** | repair `destroy_record`'s eligibility — `["hold:<record>", "presence"]` (`verb_table.yaml:160`), which `shape.py:3559` records as admitting anyone holding **any** record |
| **read** | a new verb depositing `subject_matter` triples into the reader's ledger with `source: told_by` — the epistemic channel a Record buys that a telling does not: **persistence in someone else's hands** (`H-84`'s own `unblocks:`) |

**Deception falls out, emergent, with no deception feature:** `forgery_quality` + the **shared**
`record.created` kind (`verb_table.yaml:153` and `:234`) means a document's holder **cannot tell**. A
forged document read in good faith is a false belief with a true provenance chain. Item **2.7**.

### R-E · May the loop compute? — **NARROWED, not overturned**

*"The loop computes nothing"* was inherited and is **dropped**. It already computes: the calendar,
larders and subsistence, `SITE_YIELD` and stores (`shape.py:5539-5560`), wear, canonical ordering,
clamps, and **the observer set** (`witness`, `shape.py:6238`). It must go on computing all of it.

**What it must not compute is A MODE OF PLAY'S OUTCOME.** That is `S27.2`'s second-resolver refusal,
stated in the code at `shape.py:6684-6687`, and it is the *only* thing the narrowed rule forbids.
This distinction is what licenses 4.2 (settlement economy leaves the loop **because it is a mode**,
`rosters.yaml:475-480`) while keeping `matter()`'s silt where it is.

### R-F · Persistence — three senses, and **the Receipt is the root of all three**

**Sense 1 — across a seam call. ANSWERED, four times.** A subsystem owns nothing, and that is the
only lawful pattern (`04:164` seam wrappers write *"nothing, ever"*; PART D row 22 `04:952`; §C.5.1
`04:704-717`; `ID-15`). A multi-season siege is N contests, each rehydrated from the projection.

**Sense 2 — across seasons. ANSWERED, with one defect.** The act store lives on `SeasonDriver` —
`self.resolved`, `self.scenes`, `self.act_of` at `shape.py:5352-5360` — **outside `World` and outside
`content_hash`**, whose fold is `_STATE_COLLECTIONS + _STATE_SEQUENCES + tenures + log`
(`shape.py:2988-3035`). So every `causes=[a.id]` names an id **no `World` collection holds**.
**Fix: `World.acts` and `World.scenes` enter `_STATE_COLLECTIONS`; `act_of` becomes derived.** Item
**1.5**, and it is a root.

**Sense 3 — across runs. RULED IN PRINCIPLE, UNBUILT.**
`architecture/holonic_ARCHITECTURE.md:1831` — *"**Snapshot is the save; the log is retained for
provenance; replay is a test device**"* — and `:1833-1835` marks it as a **deliberate departure** from
a plan specifying log-replay, *"because replay-as-load makes every load a full re-simulation, and any
non-determinism becomes a corrupted save rather than a failed test."*

> ⚠ **THIS SUPERSEDES THE GODOT STRATEGY DOC'S KEY-LOG-REPLAY SAVE.** `holonic` is newer and is
> Layer 1. **Replay-as-load is refused — and the refusal earns its place** rather than being deferred
> to: the richness a replay would buy comes instead from **the Receipt's `before`/`after`, which makes
> the retained log REVERSIBLE without re-simulating anything.** That is the third thing the Receipt
> buys, after the gate check and the domain echo, and it is why 1.2 is a root.

**Format:** `world_initial_state.py`'s shape transposed — authored/cooked artifact, stdlib-only leaf,
one runtime reader, blocking `--check`. **One serializer pair iterating the SAME
`_STATE_COLLECTIONS`**, so a new collection cannot be saved and not loaded. **Nothing derived is
serialised** — not `act_of`, not `_barrier_cache`, not the presence index. **NOT
`KeyLog.serialize()`** (`keys.py:453-461`), which serialises the key log and is not a save format.

### R-G · The Godot bridge — **CLOSES AT TEST 1. No escalation. One loud notification.**

SESSION_STATE §G called this *"live, unruled"*. It is not.

1. **Superseded?** **YES, and that closes it.** `architecture/` is RATIFIED 2026-09-05 (ED-IN-0202,
   *"adopt in full"*), which is **newer** than the export. `04_CODE_ARCHITECTURE.md:810` §C.12 **is**
   the Godot mapping, and it maps `World`, carriers, `Tenure`, `Act`/`Scene`/`Query`, `Event` + the
   log, the registries, the gate and `port/` — **and it never maps a `Key`**. `08_DATA_AND_KEYS.md:96`:
   *"Nobody subscribes."*
2. **The port ingests the DERIVED roster.** Item **4.8** exports it, generated from the write matrix
   and the verb table exactly as the loader derives it, behind the same blocking `--check` the other
   three exports already use.
3. ⚠ **DO NOT EXECUTE Gate-0 G0.1.** Standing up a KeyStore v2 in GDScript **hardens the refused model
   into the one language where reversal is most expensive** — the §C.12 rejection pattern by name.

**One loud notification for the PR body per §2/ED-1094:** step 4.8 changes what the port ingests. That
is a consequence of *"adopt in full"* and is not a separate design call, but it must be named, not
bundled.

### R-H · **`composition.py` IS the manifest. Delete `World.manifest`.**

`World.manifest` (`shape.py:2633`) is `dict[str, str]`, populated by `probes.py:97` and two tests,
checked by `shape.py:3039-3042`. `composition.py` does the same job better and already ships: role →
module from a **cooked** artifact, resolved by string at first use (`:66-67`), **with the exporter
importing and resolving every declared target at export time behind a blocking CI gate**, so a typo
reds CI rather than a run. Its own docstring: *"Adding a subsystem to the campaign loop is a row in
the registry, not an import in the engine."*

**So:** delete `World.manifest`; `World.boot(required)` checks `composition.ROLES`; the loop's seams
**enter `composition_roles`** rather than being resolved by an ad-hoc read at `shape.py:6505`; and the
precondition is package-qualified imports (§0 #11). **REUSE it — do not mint a second resolver.**
Item **1.6** applies it to the seams. ⚠ A rehearsal item (0.3) that would have proved the pattern on the **ladder** first was struck: the ladder is the one dependency that must never vary, so making it registry-resolvable is the opposite of what §6 trap 11 protects. The pattern is proved where it belongs — on a thing that SHOULD be swappable.

### R-I · D3 and D4, inherited unchanged

**D3** — `levy` → `remit:issue`, `establish` → `remit:confer`; **the closed roster of six is not
edited** (`rosters.yaml` `remit_acts: [issue, determine, confer, revoke, dispatch, convene]`;
`verb_table.yaml:341` already declares both substitutions). Closes at test 5. Item 0.2 is the sweep.
**D4** — `repudiate` becomes the name `release` carries on kind `commit`; the loader asserts
`release`'s domain equals `tenure_kinds \ {contain}` (PART D row 15, `04:945`). Closes at test 4.
`tenure_kinds` is `[hold, contain, commit, oblige, succeed, tie, knot]`, so `release` on `hold` is
**how anybody resigns an office**, which the loop cannot express today. Item 1.3.

### R-J · D5 is MOOT; endings are a Query plus an assumption-grade condition table

Jordan dismissed canon constraints for this work (SESSION_STATE §A.3). **D5 does not escalate and is
struck.** Endings become `world_q.ending` — a resolver-side Query over live edges — plus a condition
table graded `assumption` and swept, which is the doctrine the register already runs on. It replaces
`ENDINGS_CLASSIFIED.yaml`, whose own header calls itself *"AN AGENT CLASSIFICATION OF PROSE, NOT AN
EXECUTION"* and which `corpus_run.py:57-69` reads. Item **4.7**.

### R-K · D6 is CLOSED by Jordan (R1)

*"war supersedes the character, typically, but if the casus belli is purely based upon the character
running it, then the inheritors of that war will have justification in negotiating its end."*
**Reading:** the war is `utter`ed **through the seat**, so the edge closes on death **and the
Proposition does not** (`Proposition` is a frozen dataclass — `shape.py:5279-5281`); `T-o`
(`01:1160`) gives the successor **standing**; a personal casus belli gives **standing in a peace
negotiation, never an automatic exit**. Standing, not a switch — which keeps the ending contestable.
**`F.32` (`04:1136`) closes.** Item 4.1 carries it.

### ⚠ **ESCALATION COUNT: ZERO.** Twelve candidates, each named and each closed.

| candidate | closed at | by |
|---|---|---|
| Key/Echo readmission | test 5 | R-A, argued on all five criteria |
| a fifth question source for R6 | test 4 | Q4's own addition; widen Q2 instead |
| `AX-5`'s fourth motion | test 3 | `01:174-178`, already ruled for individuation |
| `H-84`'s transport shape | test 3 | `Record.rung` + PART D rows 12/13 |
| replay-as-load | test 1 | `holonic:1831` supersedes the strategy doc |
| what the Godot port ingests | test 1 | ED-IN-0202 is newer than the export |
| the boot manifest | test 4 | `composition.py` is the precedent and it ships |
| `levy` as a seventh remit act (D3) | test 5 | a declared substitution is reversible; a roster edit is not |
| `release` generic (D4) | test 4 | PART D row 15's generic-closer pattern |
| **D5 — what ends a campaign** | test 2 | **moot**; Jordan dismissed canon constraints |
| **D6 — whose edge a war is** | test 1 | **ruled**; R1 |
| the scene-round tick vs one freeze per season | test 1 | Jordan's R-03 statement is newer |

---

# §3 · THE SPINE — five roots

```
                      ┌──────────────────────────────────────────────────────────┐
 1.6 imports+composition ──▶ 1.2 gate + RECEIPT(before/after, per-field subject) │
   (§0 #11, R-H)              │        │                                          │
                              │        └──▶ 1.5 acts→World + snapshot  ──────────▶│ R-F sense 2+3
                              ▼                                                   │
                       1.3 Act.via + T-o + release + ⟨retire the ten scale keys⟩   │
                              │                                                   │
                              ▼                                                   │
                       2.2 H-101: purview / superiors / subordinates ────────────▶│ R-04
                                                                                  │
 1.1 R-09 (a roll) ──┬──▶ 2.3 R-07 interiors + R-08 non-rational choice ─────────▶│ R-01/R-02
                     └──▶ 2.4 the 20 dead verbs ────────────────────────────────▶ │  measured
 2.1 H-46 (13 + 4) ──┘                                                            │  at 3.1
                                                                                  │
 1.4 R-03 round tick ──▶ 2.6 Q2 widened ◀── 2.7 PAPER (Record.rung, H-84) ───────▶│ 3.3
                                                                                  └──────────
```

**Why each of the five is a root — a root is a thing nothing else can be built through, which is a
different property from being on the critical path.**

1. **`R-09` — a roll (1.1).** With no roll an act's outcome is a **deterministic function of the
   world**, so a fork's consequences are identical and propagation is *structurally unobservable no
   matter what else is open*. `requirements.yaml` R-09: *"THERE IS NO ROLL ANYWHERE IN THE LOOP"*, and
   **zero roll producers** exist in non-test `engine/season/` Python. Measuring R-01/R-02 before this
   lands measures nothing.
2. **`D1` — the gate applies the write and mints the Receipt (1.2).** `World.write` (`shape.py:2762`)
   takes an **opaque** `apply: Callable[[], Any]` and never computes `before`/`after`; both emitters
   pass `None` (`:2915`, `:6058`); `StateChange` (`:2095-2103`) has no `before`/`after` field. **Three
   separate things wait on this one fix:** PART D row 5's no-op refusal, R6's domain-echo receipt
   (§0 #12), and R-F sense 3's reversible log. Nothing written today is trustworthy.
3. **`R-03` — the round tick (1.4).** Jordan: *"what occurs after one scene can impact the next
   scene."* Today `SeasonDriver.season` (`shape.py:6470-6486`) runs deliberate → resolve → witness
   **once per season** and flattens every scene's acts into one batch, so a decision reaches the
   *next season's* deliberation at the earliest. **Nothing intra-season can propagate.**
4. **`1.5` — acts into `World`, and the snapshot.** Every `causes=[a.id]` names an id no `World`
   collection holds (`shape.py:5352-5360` vs `:2988-2993`). Until the act store is state, a save is
   either incomplete or refuses, and the log's own integrity check spans two owners.
5. **`1.6` — package-qualified imports + `composition` (§0 #11, R-H).** `import combat_seam` by bare
   name (`shape.py:6741`) gives those modules a **second identity**; the fourth registry read at
   `:6505` is an ad-hoc resolver; `World.manifest` is a second manifest. All three are the same defect
   and one fix closes them. **It is first on the critical path because every later item edits
   `shape.py`, and doing this after them means doing it twice.**

### Jordan's six-requirement chain (R3), and what is missing at each link

| # | link | mechanism | state | item |
|---|---|---|---|---|
| 1 | an act resolves **probabilistically** | `R-09` → `margin()` → `degree_from_net` | **absent.** Zero roll producers; 1 of 32 verbs declares `contests:` | 1.1 |
| 2 | writes state through the **gate with receipts** | `Receipt(id, kind, field, subject, before, after)` (`04:395`) | **absent.** `before`/`after` are `None` at both emitters; the Tenure receipt's subject is the wrong entity | 1.2 |
| 3 | **WITNESS deposits claims** per channel — the fact propagates as imperfect per-person belief | five channels, `rosters.yaml:406-410` | **partial.** Three channels are bureaucratic. ⚠ **AMENDED 2026-09-07 (PR #379):** `document_key` fires on acts now and reaches a NON-AUTHOR through the store route; `H-84` restricts the RECORD route alone | 2.7 |
| 4 | claims **reach later decisions** through the typed `requires` | `H-72` (`LedgerReader`), `H-94` (operands) | **partial.** 9 verbs typed · 4 predicates · **10 neither**; four of the ten are blocked on the Dispensation operand | 2.4 |
| 5 | outcomes write **interiorities** — the person is CHANGED, not merely informed | the Degree-keyed `writes:` column (`H-62`, `W-F`) | **absent.** `F.20a` (`04:1083`): **NO VERB WRITES ANY `Person` INTERIOR FIELD** | 2.3 |
| 6 | changed interiorities **alter what they choose** | `R-08` non-rational choice over the moved interior | **absent.** `choose` is argmax over a constant | 2.3 |
| — | ⚠ **and the link R6 adds: a world-fact change forms a QUESTION** | Q2's third clause | **absent.** No source is *"a world-fact changed in a way that concerns me"* | **2.6** |

**R7's consequence for the ordering, and it is why this plan differs from every prior one.** There is
**no single faction-legitimacy number** — it is a field over the population, so **a ruler can be wrong
about their own standing**, which makes `§C.11`'s explanation contract (`04:751`) **structural rather
than a courtesy**: the player sees their character's ESTIMATE, never the true aggregate. Legitimacy,
standing and morale are Queries over `stance`/`convictions`. **So if no stance moves when the army
dies, legitimacy cannot fall out of anything** — `H-62` is unavoidable and first-rank, and `H-84` is
one of only two roads by which it can move at all. **`H-62` + `H-84` ARE R7's mechanism.**

---

# §4 · THE WAVES

Every antagonist is dispatched `subagent_type: "valoria-critic"` — read-only **by tooling**
(`.claude/agents/valoria-critic.md` declares `tools: Read, Grep, Glob`), never by a sentence in a
prompt — and receives the producer's **output and diff, never its reasoning** (§10: the relay is
stateless, and a critic that never saw the reasoning is the more independent one). Parallel write
lanes take `isolation: worktree`. **"Artifact" means what proves it under §0.2 — a run, a hash, a
test result, a diff. Never a document, never a `## Status:` line, never a `status:` edit.**

### WAVE 0 — make the record true and prove the composition pattern

| id | deliverable | §0.2 execution artifact | producer · tier · why | antagonist brief | deps | what it moves |
|---|---|---|---|---|---|---|
| **0.1** | Replace every retracted number where it still stands with **a command**: `requirements.yaml:104`'s grid claim (**wrong in capitals** — a mass-battle cell model exists; what is absent is a **personal-scale tactical grid**), the `184`, and any surviving copy of `2,403 / 100% / 95.77%` outside `H-117`'s labelled RETRACTED WORDING. **No new checker** | `python -m pytest engine/season/tests -q` prints the number that replaced `184`; `grep -rnE '2,?403\|95\.77' engine/season/ architecture/` returns only rows carrying the RETRACTED label; `python engine/season/register.py --verify-citations` output **unchanged** | `haiku` — find/replace where the true value is a command's stdout; no judgement in any single edit | `sonnet`: run every command a replacement names. **A number that does not reproduce is a fabrication, and so is a command that was never run** | — | nothing in the game. It removes false premises later waves would build on |
| **0.2** | **D3 executed, not recorded.** Run the declared `levy`→`remit:issue` / `establish`→`remit:confer` sweep over the corpus, both arms | `python engine/season/corpus_run.py` under each arm; executed-verb line and refusal counts recorded for both; the register row moves `absent → measured` **on that output only** | `sonnet` — bounded, table-driven | `sonnet`: the two arms must differ only in the substituted cell. **If they are identical by construction the sweep is a fake control and must say so** | 0.1 | closes D3 with a measurement instead of a sentence |
| ~~**0.3**~~ | ⚠⚠ **STRUCK — AND THE REASON IS A REAL TENSION, NOT A TIDY-UP.** This row proposed proving `composition.py`'s pattern by declaring `degree_ladder` as a role and repointing `shape.py:6604-6605` through it. **It was invented by the producer** (the brief pinned a `0.3 → 1.6` path after §0 #4 deleted PLAN_v2's 0.3), and it is the one row in this plan not traceable to the adjudicator — recorded rather than quietly dropped. **Why it is struck:** the ladder is the ONE dependency that must never vary. §6 trap 11 forbids a second ladder, and making it resolvable by editing a registry row is exactly what makes a second one reachable — the invariant is protected today *by the directness of the import*. A registry row is the right shape for a thing that should be swappable; the ladder is the thing that should not. **1.6 needs no rehearsal**: it applies `composition.require` to the seams, which SHOULD be swappable, and its own falsifier (a module importable under two names must fail) is stronger than this rehearsal's. | — | — | — | — | **Nothing. The critical path re-roots at 1.6.** |

### WAVE 1 — the five roots (parallel worktrees, except where deps say otherwise)

| id | deliverable | §0.2 execution artifact | producer · tier · why | antagonist brief | deps | what it moves |
|---|---|---|---|---|---|---|
| **1.6** | **PACKAGE-QUALIFIED IMPORTS + `composition` (R-H, §0 #11).** `engine/season/` becomes importable as `engine.season.*`; `import combat_seam` (`shape.py:6741`) becomes a resolved `composition_roles` entry; the **fourth registry read at `shape.py:6505` is deleted** and replaced by the resolved role; **`World.manifest` (`:2633`) is deleted** and `World.boot(required)` checks `composition.ROLES` | `python -c "import engine.season.shape"` succeeds with **no `sys.path` mutation** in the process; `grep -n 'sys.path' engine/season/*.py` → 0 outside a declared seam loader; `export_composition.py --check` exits 0 and its resolve-at-export pass covers the new roles; `grep -n 'manifest' engine/season/shape.py` → 0; **same-seed corpus hash unchanged** via `delta.py` | `opus` — module identity is where a wrong call is silent. Two identities for one module is the defect `CLAUDE.md` §3 records for `combat_bridge`, and it was invisible to every instrument | `opus`: import the loop in a subprocess and assert **no module is loaded twice under two names**; a `composition_roles` row whose target is not importable must red the exporter, not the run; **a second `importlib` call anywhere is a second resolver**; the hash must not move | — | **ROOT of the critical path.** Unblocks 1.2 and everything that edits `shape.py` after it |
| **1.1** | **R-09 — the margin producer.** One function: `margin(w, act) -> {"net","ob"}`, pool from `Person.capability` via a new `verb_capability` roster (grade `assumption`, **swept**), Ob from `Act.obstacle` or the subject's score/2 (Jordan 2026-08-14), RNG **threaded** from the driver, never global. `contest()`'s non-combat `Unspecified` becomes the margin path, graded by the **existing** `degree_of` (`shape.py:6668-6678`) | (a) the producer-scan test goes **red by design** and is rewritten to assert **exactly one** producer site; (b) two seeds → different degree histograms over ≥50 acts; same seed → same `content_hash`; (c) **negative control:** `python -m pytest engine/tests -q` byte-identical — ⚠ named, not read (out of scope) | `opus` — the capability→verb roster and the contested-Ob derivation weigh competing considerations; the wiring is ~60 lines | `opus`: demand a cite **or** an `assumption` grade **plus a sweep** for every `verb_capability` cell; attack the seed for collision (two acts by one actor in one tick must draw differently — S33's per-tick draw ordinal); an uncontested act with `obstacle=None` must reach the gate, **never an Ob=0 roll**; **a band computed anywhere but `degree_of` is the second resolver** | 0.1 | ROOT. **R-09**; unblocks 2.3 and 2.4's contested group |
| **1.2** | **D1 — the gate applies the write and mints the Receipt.** `before`/`after` computed **at the gate**; `NoOpReceipt` on `before == after` (PART D row 5); AX-4 clause 2's Tenure branch with `via` required for `T-o`; **⚠ AND §0 #12: an effect returns ids PER FIELD**, so `_eff_kill`'s `Tenure.until` receipt names **the tenure**, not the dead person | a planted effect that touches nothing mints **no** receipt and emits **no** success Event; `_eff_create_record`'s unmarked `hold` write (`shape.py:5144-5145`) is **refused as Unmarked** until its row declares it; **a seeded governor's death emits a `Tenure.until` receipt whose `subject` is a Tenure id and whose `before`/`after` are `(None, t)`** — assert on the receipt, not on the log line; same-seed corpus hash recorded through `delta.py` | `opus` — AX-4 clause 2, the write/emit pairing and the polarity rule interact; getting the branch wrong silently un-owns every Tenure | `opus`: find any surviving path minting a `StateChange` for a field the effect did not touch; **a grammar term with no live effect behind it is invention**; attack the `via` branch for admitting a seat whose `revocation` basis does not reach the target; **the per-field return must not become a second write path** | 1.6 | ROOT. Precondition of 1.3 → 2.2, of R-B's echo, and of R-F sense 3 |
| **1.5** | **THE ACT STORE BECOMES STATE, AND THE SNAPSHOT LANDS (R-F senses 2+3).** `World.acts` and `World.scenes` enter `_STATE_COLLECTIONS` (`shape.py:2988-2989`); `act_of` becomes **derived**. Then one serializer **pair** iterating that same tuple, in `world_initial_state.py`'s shape: authored/cooked, stdlib-only leaf, single reader, blocking `--check`. **Nothing derived is serialised.** **NOT `KeyLog.serialize`** | `save(w)` → `load()` → `content_hash()` **equal** for a 3-season seeded world; **adding a collection to `_STATE_COLLECTIONS` without touching the serializer FAILS a test** (that is the falsifier for the pair drifting); every `causes=[a.id]` resolves inside `log ∪ World.acts ∪ {ROOT}` in a corpus run; a round-trip **after** a `kill` preserves the closed Tenures | `opus` — the collection set is the contract for two mechanisms at once (hash and save), and getting the derived/stored split wrong is silent until a load | `opus`: **any derived field in the serialised set is a rejection** (`act_of`, `_barrier_cache`, the presence index, `_emitted_by_write`); a save that succeeds on a world mid-`_pending`-anything is a rejection; **replay-as-load in any form is a rejection** (`holonic:1833-1835`) | 1.2 | ROOT. R-F senses 2 and 3 |
| **1.3** | **`Act.via` (H-108) + `T-o` + `release` generic (D4) + the `is_title` branch removed.** `Act` gains `via : SeatId?`; every purview walk routes through `via.scope`; `release`'s domain is asserted equal to `tenure_kinds \ {contain}` at load; `repudiate` becomes the name `release` carries on `commit`. ⚠ **LAST STEP, AND ONLY AS THE LAST STEP: retire the ten `scale:` keys** (`verb_table.yaml:126,138,169,180,192,216,239,331,437,459`), which `:55-64` releases **only** once `Act.via` carries the scope (§0 #7) | the loader **raises** on a `release` domain missing a kind; `grep -n is_title engine/season/shape.py` → 0 in the resolver; a delegate holding **no** title over the domain **executes** a `revoke` through `via`, and the same act **without** `via` is refused; `grep -cn '^    scale:' engine/season/verb_table.yaml` → 0 **and** the loader's invariant 10 stops refusing the table | `opus` — `H-108` and `H-109` are one question answered twice, and the seat's `revocation` basis becomes a data row | `opus`: a second code path keyed on a post's **name** anywhere is the defect returning; the `release` of a `hold` must be **resignation**, never a silent transfer; attack for a purview walk still reading the actor's own holds; **the ten keys must not be deleted before `via.scope` is read by the resolver** | 1.2 | regency, puppets, governors, councils — and **resignation**. Precondition of 2.2 and of R-04 |
| **1.4** | **R-03 — the round tick, at PLAYER granularity.** `season` becomes `calendar → matter → for r in rounds: freeze → deliberate → resolve → witness → thaw → census`. Draw ordinal keyed by `(tick, round)`. **An NPC gets a resolution and an Event, not a constructed scene** (`rosters.yaml:442-446`). **No flag, no old path** | `headless.py --case NPC-088 --seasons 2 --seed 0` shows per-round events; a planted round-1 deposit from `p_a` changes `p_b`'s **round-2** candidate set against a control without it; **cost control: doubling the cast must not multiply deliberations per player-round**; two same-seed runs hash identically | `opus` — a structural change to the driver against S26.2's freeze invariant and PART D rows 17/21 | `opus`: any person-side read crossing a round boundary **outside** WITNESS; a person with budget 5 must get exactly 5 scene actions **across** rounds, not per round; **a round counter stored on a carrier is the fourth clock** (`04:947`); a flag preserving the old path is the trap by name | 0.1 | ROOT. **R-03**, and R-02's prerequisite in Jordan's own words |

### WAVE 2 — choice, consequence, reaction, and paper

| id | deliverable | §0.2 execution artifact | producer · tier · why | antagonist brief | deps | what it moves |
|---|---|---|---|---|---|---|
| **2.1** | **H-46 — the 13 convictions and the 4 ethical axes**, replacing the 4-value stand-in; the 13×4 matrix as a swept `assumption`; `align(verb, axis)` authored across 32 verbs × 4 axes, sparse allowed, **no verb with zero cells** | loader **raises** on the old four names; `corpus_run` RANKING DISCRIMINATION moves off `2..7 of 22` — **recorded, not targeted**; `headless` still runs | `haiku` transcribes the roster and matrix; `opus` authors the cells — **this is game content, which is what the freed capacity is for** (§0.3) | `opus`: every cell survives *"why this sign?"* against the verb's own `writes:`; **an all-zero verb can never discriminate and must be reported**; no value lifted from the retired `values_master` | 0.1 | R-06's discrimination; prerequisite of 2.3's chooser |
| **2.2** | **D2 — `H-101` as three Queries:** `purview(seat)`, `superiors(person) -> (SeatId \| PersonId)[]`, `subordinates(seat)`. **One `oblige` edge, both scales.** No root, no `Faction.superior`, no stored depth. The faction scale asks the **same** Queries | a corpus case naming a superior resolves a purview walk **through the oblige edge**; a planted forswearing changes the answer next season; `grep -rn 'superior\|liege\|rank' engine/season/shape.py` shows **no field** | `sonnet` — ratified at `01_AXIOMS.md:1244-1256`/`:1292-1314`; this is bounded implementation over an existing `tenure_kind` | `sonnet`: a root by any spelling; any Query walking the **rung** ladder for an institutional answer; ***undetermined* must be expressible and distinct from *contested*** | 1.3 | **R-04's precondition** |
| **2.3** | **R-07 + R-08 — interiors move, and choice stops being argmax.** Degree-keyed writes to `Person.stance` through the existing `writes:` Degree column (`H-62`'s supplied shape); `choose` ranks then samples `softmax(score/τ)` on the threaded RNG, **τ→0 reproducing today's argmax as the control arm** | ≥1 person carries a **nonzero `stance` row** after 2 seasons (`stance_toward`, `shape.py:3437`, finally gets a writer); same person/view over 20 seeds → ≥2 distinct top acts; **τ=0 arm byte-identical to HEAD**; DISTINCT EXECUTED SETS rises from **2** | `opus` — AX-3 drift risk, and PART D row 18 is **STRUCTURAL by signature** (`04:948`): the interior writer must take `PersonInterior` and **no ledger reference** | `opus`: `stance` must be **per-referent rows, never a summed field** (row 8); no write outside the gate; the sort key must stay deterministic *before* sampling; `random.random()` anywhere is a second RNG; **a signature that can name a Claim is the axiom lost** | 1.1, 1.2, 2.1 | **R-07, R-08 — and R7's precondition.** Nothing normative can move until this lands |
| **2.4 ×N** | **R-05a — the 20 verbs with no predicate and no effect**, grouped by blocker, one worktree per group. ⚠ **THE SECOND GROUP IS ON THE CRITICAL PATH FOR A REASON THAT IS NOT VERB COUNT**: `comply`, `evade / defy`, `refract`, `issue` are blocked on the **Dispensation operand** — `requires_operands` is closed on `[actor, subject, from, to, site, kind, amount, floor]` with no name for one (`verb_table.yaml:117`, `:207`; `H-94`). **That group IS the top-down direction** (§4a) | `corpus_run`'s *"20 have no predicate/effect"* falls by the group size; **each verb executes ≥1 time in the corpus**, not merely in a hand-written test; for group 2, a `comply` and a `defy` both execute against the **same** issued Dispensation | `sonnet` per group — table-driven and bounded; `opus` for group 2 only, because widening a closed roster is a design call | `sonnet` per group: an effect that special-cases a name is **scripting drift**; every `writes:` cell must be a matrix row; refusal **emits**, never raises. For group 2: **an operand added by keyword argument is filling `H-94` by the back door**; the roster widening must be one named value with a sweep | 1.1, 1.2 | **R-05** toward 32/32; **top-down and diagonal** become expressible |
| **2.5** | **The windowed Query** — one read over the log, carrying both constraints: it may **not** be monotone over ENDED edges (`Query.aggregate_guard`, `shape.py:3081-3097`; PART D row 16), and it is `world_q` — **resolver-side, never a player HUD** (§C.11, `04:775-785`) | the Query runs over ≥3 seasons of a seeded corpus world and its value **moves**; a deliberately monotone sibling is **refused by `aggregate_guard` in a test** | `sonnet` — one function with two named refusals to satisfy | `sonnet`: attack for the ratchet by construction (`count{commit}` over live **and** ended rows); attack any caller handing the result to a person-side surface | 1.4 | R7's trajectory read, correctly sited |
| **2.6** | ⚠ **THE REACTION SOURCE — no prior plan carried this.** Widen Q2's third clause (`shape.py:3900-3903`) so a landed claim forms a Question when its subject is the **subject of any OUGHT Proposition the person is committed to**. **Not a fifth source** — `question_sources` stays closed at four and its order is untouched | in a seeded run where a governor dies, **a person with a `commit` to an OUGHT about that office forms a Question and then a Candidate for it**, and a control person with no such commit forms neither; `grep -c "values:" ` on `question_sources` unchanged at four; the across-source order (`order[q.source]`) **byte-identical** in the diff | `opus` — this is the link that turns propagation into a game, and the constraint (`choose` sees no World) makes the wrong fix easy to write | `opus`: **a fifth source is a rejection** (`hole_register.yaml:628` measures what a reordering does); any read of world truth from `choose` is PART D row 2; the widened clause must go through the person's **own ledger**, never through `w.tenures`; **the within-source tiebreak must not change** | 1.4, 2.7 | **R6's missing link 2.** Propagation stops being a chronicle |
| **2.7** | ⚠ **PAPER — `H-84`, and no prior plan carried this either.** Add the **`Record.rung` matrix row** (`write_matrix.yaml` has five `Record` rows and no `rung`), then the producers of R-D: *deposit* (`release` on `hold`, Record stays at rung) · *take* (a `hold` opener, `own` + `presence`) · *give* (release + take) · *send/carry* (a `Record.rung` write) · *copy* (`create_record` from the maker's own ledger) · *destroy* (repair `destroy_record`'s eligibility, `verb_table.yaml:160`) · **`read`**, depositing `subject_matter` triples with `source: told_by` | **a second person holds a Record in a seeded run**, and `document_key` deposits a claim for someone who is not its maker — the exact thing `H-84` measures as ZERO today; a **forged** record and a true one are **indistinguishable to their holder** (same `record.created` kind) and **distinguishable in the log** (`forgery_quality`); an archive Record at a rung held by nobody is **takeable by a person present at that rung** | `opus` — this is R5's mechanism and R7's second road; the producers must compose from existing primitives or they are new machinery | `opus`: **no `Record.owner` field** — the holder is a `hold` Tenure (PART D row 11's shape); a seat must not hold (rows 12/13/14); *give* must be **two acts with two owners**, never one write; **a claim minted for a reading that did not happen is PART D row 5**; `Query.hold_force`'s 1-per-object must hold for Records too | 1.2, 1.3 | **`H-84`.** Three witness channels come alive; deception becomes emergent |
| **2.8** | **FOUNDING AND GROWTH — churn routes 1 and 2 (`F.20`, `04:1082`).** A `found` / `build` verb writing `Rung.exists` / `Site.exists` through the gate, and `matter()`'s growth term — **motion 1 with the opposite sign to silt**, sited beside `SITE_YIELD` (`shape.py:5539-5560`), **not a new clock** | a seeded 10-season run **ends with more Sites than it started with**, and the control (growth term zeroed) does not; every founded Site's Event has a **non-`[ROOT]` `causes[]` naming the act that founded it**; `python -c "..."` over the corpus shows `Rung.exists`/`Site.exists` with a producing verb | `sonnet` — the verbs are table rows on an existing pattern; `opus` for the growth term's siting only | `sonnet`: **a quantity advancing with no author is `T-c`'s fourth clock** (`01:304`); a founded Site with `causes=[ROOT]` is an unauthored change and is a rejection; `AX-5` must still list **three** motions after the diff | 1.2, 2.4 | **R4.** The world stops only decaying |

### WAVE 3 — measure. It is allowed to come back negative.

| id | deliverable | §0.2 execution artifact | producer · tier · why | antagonist brief | deps | what it moves |
|---|---|---|---|---|---|---|
| **3.1** | Re-run fork-and-follow **at the SHIPPED fixture**, reporting **both fingerprints** — verb-only **and** `(verb, subject)`. Flip R-01/R-02 only on the number | `runs/wd_cells.json` committed; **GENUINE forks > 0 at shipped defaults** (today the denominator is *empty*, which is not a low rate); reconvergence strictly < 100%; the `observation_deposit_mode=none` control arm **higher** than the default arm | `sonnet` — measurement, table-driven | `sonnet`: the fixture must be shipped defaults, **not the 2×1 cell**; `fork_case` imported unmodified; a single-fingerprint report is the 95.77-vs-65.44 conflation returning; **if reconvergence is still ≥96%, name which channel is closed** | 1.1, 1.2, 1.4, 2.3, 2.6 | **R-01 / R-02**, in whichever direction the number goes |
| **3.2** | **`ambitions(p)`** — a Query over `commit` Tenures to OUGHT Propositions (`headless.py:74-81` is the mechanism `requirements.yaml` R-06 already names) — plus a real W27 cast per case instead of one shared OUGHT across 143 worlds | DISTINCT EXECUTED SETS > 2; a case with 11 distinct actors runs; the Q4 `need` source fires for **more than one** proposition | `sonnet` — bounded read over an existing edge | `sonnet`: no person-side read of world truth; the cast must be **parsed** from the case, not token-matched | 2.1, 2.6 | R-06 toward `met`; 2.6's clause gets more than one subject to fire on |
| **3.3** | ⚠ **THE GOVERNOR'S-DEATH CASE, END TO END** — one seeded corpus case that exercises every link of R3's chain in order and asserts on each: duel → `Felled` → `_eff_kill` closes the tenure → **a receipt naming the tenure** (1.2) → WITNESS deposits per channel, **including `document_key` off a chancery Record** (2.7) → an ambitious person's Q2 fires (2.6) → they form a candidate for the seat → `Query.hold_force` returns them next season | one test, **seven assertions, one per link**, each naming the link it guards; the same case with **2.6 reverted** forms no candidate (the control); the same case with **1.2 reverted** shows the receipt naming the dead person (the second control); `content_hash` stable across two runs at one seed | `opus` — an integration falsifier that asserts on the *chain* rather than on an outcome is the hardest thing in this plan to write honestly | `opus`: an assertion that would pass with any link reverted **is not guarding that link**; **the case must be a corpus case, not a hand-built fixture** (a hand-built world proves the test, not the loop); no assertion on a count that a re-seed moves | 2.6, 2.7, 1.2 | **R6 and R7 demonstrated, in one artifact, in one run** |

### WAVE 4 — the seven scales, the campaign artifact, the port, the retirement

| id | deliverable | §0.2 execution artifact | producer · tier · why | antagonist brief | deps | what it moves |
|---|---|---|---|---|---|---|
| **4.1** | **R-04 — grand strategy in the loop.** A Faction is a type with **no verbs**; `holdings` is a Query over members' `hold` Tenures; seats act through `Act.via`. Carries **W28**'s `scale:` re-authoring overlay (`corpus_run.py:75-103`): re-scale the 44, rule out the 10. ⚠ **And carries R-K:** a war is `utter`ed **via the seat**, `at_war` is a Query over the Proposition pair, `T-o` gives the successor **standing**, never an exit | `corpus_run`'s unrepresentable-scale line → `{}` or world ≤ what W28 rules out; ≥1 faction-scale ARC **ends**; a `levy` **executes** through a seat; **a war survives its declarer's death and a successor with a personal casus belli reaches a peace negotiation without the war ending automatically** | `opus` — porting a SCALE, not a class | `opus`: a stored L/Sta/Mil field, a faction passed where a `PersonId` is required, or a write by a banner is a **rejection** (PART D rows 1/8/14); attack for old-driver vocabulary leaking in; **an automatic peace on a personal casus belli is a switch and R1 refused a switch** | 2.2, 2.4, 3.2 | **R-04**, **R-K**. Unblocks 4.9 |
| **4.2** | **Settlement management as a MATTER seam.** The inline `stores`/`yield`/`subsistence` economy comes **out** of `SeasonDriver.matter` and becomes a called seam; founding/build/domain acts join the acted channel. `rosters.yaml:475-480` already rules this: *"an economy the loop computes itself is a mode that never got its seam"* | a seeded realm's economy produces **per-row Events with `causes[]`** through the seam; the inline path is **deleted, not flagged off**; same-seed hash recorded through `delta.py` | `opus` for the seam contract (the engine behind it **must be built**); `sonnet` for the harness | `opus`: **two ladders for one quantity is a NERS S defect** (`rosters.yaml:479`); a seam that writes state fails PART D row 22; the projection crossing it must be read-only; **R-E's line is the test — an economy is a MODE, silt is not** | 2.8, 4.1 | one of the four scales the loop has never expressed |
| **4.3a** | **WIRE MASS BATTLE BEHIND THE EXISTING SEAM. Contract unchanged.** In: claimants, prize, causes. Out: **the subsystem's own result**, graded by `degree_of` (§0 #2) — never a band computed in the seam | a seeded mass-battle contest **executes in the corpus** and its degree is read by `degree_of` from the subsystem's return; same seed → same hash; the contested set moves off `{kill / wound}` | `opus` — deriving sides from persons is design synthesis across a contract | `opus`: **does every `Person` field the seam reads exist, or is a side fabricated?** (`combat_bridge`'s rule: **return the gap**); **any band computed in the seam is the second resolver** (`shape.py:6684-6687`); attack the RNG restore | 4.1 | R-05b partial; a retained subsystem the loop could not reach |
| **4.3b** | ⚠ **THE GRID ENGINE, AS A REPLACEMENT BEHIND AN UNCHANGED SEAM.** One contest engine over `PersonId[] at weight`, on a grid, serving personal combat **and** squad **and** mass battle. `T-l` (`01:411`) licenses it in terms: *"A cohort is a `Person` at weight > 1, never a subclass … a second type means every mechanism has two code paths, and two code paths drift."* **A duel is a 2-unit, weight-1 call.** ⚠ **Personal-scale tactical grid does not exist and must be BUILT** — the one row in §4a with nothing to point at | **the seam contract diff is EMPTY** (that is the artifact: an engine replaced behind an unchanged contract); one entry point returns a gradeable result for a duel **and** for a battle; `grep` shows **one** degree ladder; a seeded battle and a seeded duel both execute in the corpus and 4.3a's pinned hashes are the control | `opus` — unbuilt design, and the only item here that is not wiring | `opus`: a per-scale branch **inside** the engine is the defect (`T-k`, `01:404`); **weight must be a number on a person, never a subclass**; **if the seam contract changed, the seam was never the boundary** and the whole replacement claim fails | 4.3a | **two** of seven scales at once; retires the duel-only limitation |
| **4.4** | **Social contest on the same seam** — persons → the contest call → the kernel's own result → `degree_of`. Add `contests:` to `petition`, `repudiate`, `speak`/`tell` where the design contests them. Today **1 of 32** verbs declares `contests:` (`verb_table.yaml:254`) | a `petition` **in the corpus** resolves at a degree through the seam; same seed → same hash; the contested set has ≥3 members | `opus` — deriving sides/claimants from persons is synthesis across a contract | `opus`: as 4.3a, plus — **the kernel's `DEGREE_ORDINAL` must be READ, never re-derived** | 4.3a | the third retained subsystem the loop cannot reach today |
| **4.5** | **Investigation as its OWN kind — explicitly NOT a contest** (`rosters.yaml:487-490`). Attaches acted, RESOLVE → WITNESS. ⚠ **Failure emits `finding.none` and deposits NOTHING** (`verb_table.yaml:498`, §0 #3). **Deception comes from 2.7's forged record read in good faith, not from a lie the engine tells** | a corpus investigation act resolves and deposits Claims whose `confidence`/`source` **differ by degree**; a Failure run deposits **no** claim and emits `finding.none`; **a forged record read by an investigator produces a true-provenance false belief that a later act acts upon** | `opus` — the one scale whose resolution shape is genuinely undesigned | `opus`: giving it a prize so the existing machinery can grade it is **scripting drift**; **a claim minted on Failure is a rejection**; the six acts must stay six acts, not become one | 1.1, 2.7 | six verbs that are today **ungradeable**, not merely ungraded |
| **4.6** | **Character creation / development / chronicling.** Individuation is already demand-driven at CENSUS (§C.7, `04:743-749`); what is missing is `F.31`'s world-generation roster (churn route 3), a development act, and `capability` being non-empty — ⚠ **`capability` is EMPTY on every corpus person** (`requirements.yaml` scales row 1) | a person is individuated **from a refusal** in a seeded run; a developed `capability` **changes a later `margin()` draw for that person** against a control where it does not | `sonnet` — the mechanism exists; this is a roster plus one acted verb | `sonnet`: **no new type for a "created" person** (`T-l`); the roster is boot data, **not a frame**; a development write outside the gate is a rejection; **a population that grows on its own is `AX-5`'s fourth motion** (`01:177-178`) | 1.1, 2.8 | the scale that makes R-09's roll vary **by person**, not only by seed |
| **4.7** | **Endings as `world_q.ending`** — a resolver-side Query plus an **assumption-grade condition table, swept** (R-J). Replaces the prose grader `corpus_run.py:57-69` reads | an ARC case **ends because the Query says so**, in a seeded run; `NOT-COMPUTABLE` disappears from the ARC ENDS line; the condition table's cells are swept and the sweep's arms differ | `sonnet` — one Query; its content is a graded table, not a ruling | `sonnet`: it is `world_q` and may not reach a person-side surface; a **stored** ending flag is PART D row 8; **D5 is moot, not open — do not re-open it** | 3.2, 4.1 | the campaign's end acquires a representation |
| **4.8** | ⚠ **THE PORT INGESTS THE DERIVED ROSTER (R-G).** Export the loop's derived kind roster — the union of every `emits`/`emits_on_refusal` column in `verb_table.yaml` and every `on_write`/`on_condition` in `write_matrix.yaml` — behind a blocking `--check`, as the port's event-kind source. `key_types.json`'s `type_count: 55` retires with the driver. **Do NOT execute Gate-0 G0.1** | `python tools/export_<name>.py --check` exits 0; **the exported count equals what the loader derives at boot** (assert the two, do not type either); adding an `emits:` cell to the table and re-running `--check` **fails until the export is re-cooked** | `sonnet` — generation plus a round trip, on the pattern the tree already runs three times | `sonnet`: **a hand-authored roster anywhere is the defect this closes**; the export must be derived by the **same** code path the loader uses, or there are two derivations; the PR body must carry the loud notification (§2/ED-1094) | 4.1 | closes the two-rosters-for-one-concept defect (§0 #10) |
| **4.9** | **Step B — the retirement.** One commit, after the loop expresses the scales. Every retired path resolves through `pathres.fork_pointer()`; `R04_PENDING_ROLES` shrinks to empty; `PATH_SEAM_ALLOWED` shrinks to the declared season seams | CI green with the retained set; `python -m pytest tests/valoria -q` green; `test_engine_does_not_import_systems` and `test_r04_pending_composition_roles_can_only_shrink` green with the new ceilings; `git cat-file -e` on 20 sampled fork pointers | `sonnet` — mechanical under `evacuation_plan` | `sonnet`: **a subsystem whose scale the loop has not subsumed may not be retired** — that is §4a's test, not a preference; the PR body must carry the held-back notifications loudly; **Step A is already landed (§0 #9) and must not be redone** | 4.1–4.8 | closes the ruling's second half |

**CRITICAL PATH:** `1.6 → 1.2 → 1.3 → 2.2 → 4.1 → 4.9`.
`1.1`, `1.4` and `1.5` run in parallel worktrees off wave 0 and 1.2 respectively; `2.4` runs beside
everything from the day 1.2 lands; `2.6 → 2.7 → 3.3` is the second longest chain and is the one that
carries R6 and R7. ⚠ **1.6 and 1.2 are on the path and 1.1 is not** — being a root and being on the
critical path are different properties, and PLAN_v2 conflated them.

---

# §4a · THE SEVEN SCALES, CHURN'S FOUR ROUTES, AND THE SIX DIRECTIONS

**Which channel a scale attaches to is the first question, because it decides whether the scale costs
a scene** (§1). `rosters.yaml:459-467` declares **one row ruled and six honest blanks**, and refuses to
guess: *"writing a plausible IN/OUT for a mode nobody has ruled would be inventing the architecture
rather than recording it."* Below, each blank is run through §0's five tests.

⚠ **THREE OF THE FOUR BLANKS ARE NOT SEAMS AT ALL, AND SETTLEMENT MANAGEMENT IS THE ONLY GENUINE
SEAM AMONG THEM.** *(Corrected: the adjudicator's headline read "two of the four… and a third
resolves to Queries", which double-counts — resolving to Queries IS not being a seam. Its own table,
below, said three. The table was right. Recorded rather than silently renumbered, because the
corrected count is the stronger claim: **the four "Jordan questions" are one contract to write, not
four.**)* Character development and investigation are the loop itself; grand strategy is Queries;
settlement management alone needs a seam, and the engine behind it must be built.

| scale | channel | attaches at | in | out | engine | item |
|---|---|---|---|---|---|---|
| **character creation / development / chronicling** | actorless CENSUS + acted | barrier 4 / RESOLVE | a demand Event (a refusal, `04:743-749`) + `F.31`'s world-gen roster | `person.individuated`; a written `capability` | ⚠ **NOT A SEAM. The loop IS the mechanism** — closes at **test 3**: §C.7 already specifies demand-driven individuation, and `01:177-178` already rules the roster lawful | 4.6 |
| **grand strategy politics** | acted, **via seats** | RESOLVE | persons, seats, Propositions | Events on Tenures | ⚠ **NOT A SEAM — QUERIES.** `holdings`, `purview`, `superiors`, `subordinates`, `at_war`. Closes at **test 3**: PART D row 14 (`04:944`) already rules `Faction.holdings` a Query that *"READS members' holds and cannot write one"* | 2.2 + 4.1 |
| **settlement management / city building** | actorless MATTER seam + acted founding verbs | barrier 2 / RESOLVE | the frozen rung projection | per-row Events with `causes[]` | ⚠ **A GENUINE SEAM, AND THE ONLY ONE AMONG THE BLANKS.** Closes at **test 3** in the other direction: `rosters.yaml:475-480` rules the inline economy *"a mode that never got its seam"*. The engine behind it **must be built** | 4.2 |
| **social contests / debates** | acted contest seam | RESOLVE (S39) | claimants, prize, causes | **the subsystem's result** → `degree_of` | **replaceable** — a kernel exists; the seam refuses by name today | 4.4 |
| **mass battles / strategy warfare** | acted contest seam | RESOLVE (S39) | as above, sides resolved **once** | as above | **wire first (4.3a), replace second (4.3b)** — §0 #8 | 4.3a → 4.3b |
| **personal combat / grid map combat with units** | acted contest seam | RESOLVE (S39) | as above, **2..N units at weight** | as above; combat reads its degree **off the scene** (Jordan 2026-09-03) | ⚠ **REPLACE, behind an unchanged contract.** A duel is a 2-unit weight-1 call (`T-l`, `01:411`) | 4.3b |
| **investigation / detective / IF** | acted, **its OWN kind — not a contest** | RESOLVE → WITNESS | investigator, subject, degree | Claims graded by degree; **Failure emits `finding.none` and deposits nothing** | ⚠ **NOT A SEAM. The loop IS the mechanism** — closes at **test 3**: `rosters.yaml:487-490` rules the contest shortcut scripting drift by name | 4.5 |

> ⚠ **`rosters.yaml:466` IS STRUCK.** It reads *"faction mgmt · UNRULED · absent from the loop
> entirely."* The first half is answered — PART D row 14 (`04:944`) already rules the shape, and the
> answer is **Queries, not a seam**. Strike the row with that citation rather than filling in a
> plausible IN/OUT for a mode that has none.

### Churn's four routes, sited

| route | axiom cost | item | ⚠ |
|---|---|---|---|
| 1 · NPC action | none (`AX-1`-native) | 2.4 ×N | needs the 26 non-executing verbs alive |
| 2 · matter growth + FOUNDING | none — motion 1, opposite sign to silt; founding is an **act** | 2.8 | §0 #5: `matter()` already credits. The gap is that nothing founds |
| 3 · authored occasion | none — `01:177-178` already rules the roster lawful | 4.6 | `F.31`, entirely unbuilt |
| 4 · spontaneous, unauthored | **`AX-5`'s fourth motion** | **REFUSED** | unplaceable · unwitnessable · unobstructable, and buys nothing 1–3 do not |

### THE SIX DIRECTIONS (§0.06) — **three of six have no live mechanism today**

| direction | the mechanism it needs | state | item |
|---|---|---|---|
| **top-down** | a Dispensation issued down a purview and complied with, evaded or refracted | ⚠ **DEAD.** `issue` writes `Dispensation.exists`, but `comply`/`evade / defy`/`refract` are blocked on an operand the **closed** `requires_operands` roster has no name for (`verb_table.yaml:117`, `:207`; `H-94`). §F.15 (`04:1077`) adds that the nine Dispensation term types are enumerated nowhere: *"the entire downward mechanism has no executable content"* | **2.4 group 2** |
| **bottom-up** | a petition reaching a docket and being determined | **partial.** `petition` → `carry` → `(DocketItem, matter)` runs; `determine` is `absent` on `judging_set` (`shape.py:3161-3163`, `Unspecified("judging_set_rule", "S61")`) | 2.4 |
| **vertical** | an act carrying **the scope of the seat exercised**, not the actor's own standing | ⚠ **DEAD.** `Act` has no `via` (`H-108`): *"authority is read off the ACTOR and delegation is unbuildable here."* No regency, no governor, no puppet | **1.3** |
| **diagonal** | a person at one scale reaching an institution at another without a seat between | ⚠ **DEAD.** Needs `superiors`/`subordinates` over one `oblige` edge at both scales (2.2) **and** `Act.via` (1.3). Neither exists | **1.3 → 2.2** |
| **lateral** | person to person at one rung | **live, and measured.** The telling chain: R3 30/30 on the NPC lane, 54/59 on ARC, from 0 and 0 (`H-84` `unblocks:`) | — |
| **horizontal** | institution to institution at one rung | **weak.** `exchange` is blocked on the counterparty's side (`H-94`, same cause as top-down); `oblige` between seats needs 2.2 | 2.2, 2.4 |

**That is why 1.3 and 2.4's second group are on the critical path.** R3's *"rippling all directions"*
is not a flourish — it is §0.06's six, and half of them have no code.

---

# §5 · THE FALSIFIERS — named before the work, each with its control (§0.1 pt 3)

| wave | it failed if | control |
|---|---|---|
| **0** | any command a replacement names prints something other than the replacement; `--verify-citations` output changes for any reason but the corrected sentences; the `headless` hash moves | `git diff --stat`; the commands themselves; the unchanged seeded hash |
| **1** | **1.6** any module loads twice under two names, or the corpus hash moves; **1.1** two seeds give identical degree histograms over ≥50 acts, or one seed differs across runs; **1.2** an effect that touches nothing still mints a receipt, **or the `Tenure.until` receipt still names the dead person**; **1.5** a save/load round trip changes `content_hash`, or a new `_STATE_COLLECTIONS` entry passes without a serializer change; **1.3** the loader accepts a `release` domain missing a kind, or the ten `scale:` keys are deleted before `via.scope` is read; **1.4** a planted round-1 deposit does not change a round-2 candidate set | **the campaign-scale goldens byte-identical** — `python -m pytest engine/tests -q` (named, not read: out of scope). Same-seed hash equality for 1.4 and 1.6 |
| **2** | executed-verb count and DISTINCT EXECUTED SETS do not **both** rise; `stance` still has zero writers after two seasons; **2.6: the ambitious person still forms no candidate for a vacated office**; **2.7: `document_key` still deposits for nobody but the author *from a `record.*` Event*** — ⚠ **narrowed 2026-09-07:** the unqualified form is no longer a falsifier for 2.7, because the store route already deposits for a non-author; only the RECORD route is 2.7's; 2.8: the 10-season run ends with no more Sites than it started with | **τ→0 arm byte-identical to HEAD** — a sampler whose zero-temperature limit is not the old argmax changed two things at once. For 2.6, the with/without-clause pair. For 2.8, the growth term zeroed |
| **3** | GENUINE forks are still 0 at shipped defaults (**the denominator is empty today, not the rate low**), or reconvergence ≥96%; **3.3: any of its seven assertions still passes with its link reverted** — then it guards nothing | the `observation_deposit_mode=none` arm ≥ the default arm; **both** fingerprints, or the run is the 95.77-vs-65.44 conflation again; 3.3's two reverted-link controls |
| **4** | a faction-scale case is still UNREPRESENTABLE; **4.3b changed the seam contract** — then the seam was never the boundary and the replacement claim is void; the settlement economy still runs inline anywhere; 4.8's exported count differs from the loader's derived count; after 4.9 anything retained imports a forked module | `test_engine_does_not_import_systems`, `test_r04_pending_composition_roles_can_only_shrink`, `test_partition_is_total`; an **empty** diff on the seam contract for 4.3b; a two-arm campaign run (n≥30) showing the realm does not degenerate to one holder |
| ⚠ **CHURN / PROPAGATION** | **after wave 2, if DISTINCT EXECUTED SETS is still 2, or later-decision divergence is still ~4% while world divergence is ~100% — then the world churned and changed no decision. THAT IS SCENERY**, and R3/R4 are `not_met` however many verbs execute | both numbers reported together, from the same run, at shipped defaults. **Neither number alone is the criterion** |
| **the process** | in any wave, **more than half the diff lands outside** `engine/season/{shape.py, *_seam.py, *.yaml}` and `engine/season/tests/` — §0.3's 10.8:1 reappearing | `git diff --numstat <wave-base>..HEAD`, bucketed by path |

---

# §6 · WHAT NOT TO DO — twenty, each with the citation that forbids it

1. ⚠⚠ **THE SUBSTRATE TRAP — do not build persistence, composition, scheduling or event delivery on
   `engine/substrate/keys.py`.** It is the most inviting wrong turn in this plan because it is *live,
   tested code that already does what you need*. `keys.py:506` is a subscription table; `:88-105` is a
   targeted Event with an `impact_vector` and `stat_deltas`; `:463-600` is a cascade with a deferred
   apply. `08_DATA_AND_KEYS.md:86-96` refuses all three **by name**, and the adopted loop imports none
   of it (`shape.py:6604-6605` is its only `engine/` import). **Building on it imports the refused
   mechanism back through the floor, where it is hardest to see.**
2. **Do not execute Gate-0 G0.1.** It hardens the refused Key model into GDScript, where reversal is
   most expensive — §C.12's rejection pattern by name (`04:820-838`). R-G.
3. **Do not answer churn with a clock.** `T-c` (`01:304`), PART D row 17 (`04:947`), loader invariant
   5. `AX-5` lists **three** motions and `01:154-160` says the list is the stipulation.
4. **Do not mint a false claim on investigation Failure.** `verb_table.yaml:498` declares
   `emits_on_refusal: ["finding.none"]`; a claim for a finding that did not happen is PART D row 5's
   defect (`04:934`). **Deception is a forged document read in good faith** (R-D, item 2.7).
5. **Do not mint a second resolver.** `T-k` (`01:404`), *"one resolver, one degree ladder"*;
   `degree_of` (`shape.py:6653-6687`) is the one reader; `shape.py:6684-6687` refuses in its own words.
   ⚠ **And note §0 #2: the seam returns the subsystem's own result, not a `Margin`.**
6. **Widen Q2 — do not add a fifth question source.** `question_sources` is closed and **ordered**, and
   `hole_register.yaml:628` measures what changing that order does: the leading source is shared with
   another question in **801 of 1,068 deliberations**. Precedent is Q4's own addition (`shape.py:3873`).
7. **Do not let a seat hold.** PART D rows 12/13 (`04:942-943`); `hold`'s subject is `PersonId` (row
   14, `04:944`); `Query.hold_force` (`shape.py:3151`) enforces 1-per-object and **raises** on a second.
8. **An archive is a PLACE — do not give `Record` an owner field.** `Record.rung` (`shape.py:2416`)
   is the home and needs only a matrix row. An `owner` field is PART D row 11's *seat that knows its
   holder* (`04:941`) wearing a different hat, and row 10's two homes for one relation.
9. **Do not fill a seam contract by writing cells.** PART D row 22 (`04:952`); `rosters.yaml:457` — *"A
   seam declares three things and only three."* The projection crossing it is read-only.
10. **No root, no `liege`, no stored depth or rank integer.** `02_HIERARCHIES.md:53-57` — *"THE
    SUBORDINATION GRAPH HAS NO ROOT AND MUST NEVER BE GIVEN ONE"*; PART D row 8 (`04:937`) for the
    integer. A root is a sovereign nobody swore to, and its absence is what makes a **contested** realm
    expressible.
11. **No second ladder for one quantity.** `rosters.yaml:475-480` grades it a NERS **S** defect
    (§0.06, *calculations consistent in methodology*); `T-k` refuses it directly. This binds 4.2 and
    4.3b hardest.
12. **No `campaign_seam.py`, and no default-OFF bridge to the old driver.** §0.3 names the shape:
    a document in code form. The join is at the substrate **by direct call**; the driver is
    **superseded, never bridged**.
13. **Do not re-open §E.1.7's `contract : { levy, tax, obligations, autonomy }`.**
    `01_AXIOMS.md:1292-1314` rejects it **by name** and was added specifically to close that
    over-refusal. Re-deriving a ratified section is the failure the relay exists to record.
14. **Do not quote the retracted rates.** `2,403` · `100% reconvergence` · `95.77%` · `184 tests`.
    `hole_register.yaml` H-117 (`:1864`) — **there is an empty denominator at both fixture points, and
    a ratio over zero is not a small number.** 181 tests: run the command.
15. **Do not serialise anything derived.** `act_of`, `_barrier_cache`, `_emitted_by_write`, the
    presence index. One serializer pair iterating **`_STATE_COLLECTIONS`** (`shape.py:2988-2993`) and
    nothing else, or the save and the hash acquire two definitions of state.
16. **Do not answer persistence with replay-as-load.** `holonic_ARCHITECTURE.md:1831-1835` —
    *"Snapshot is the save; the log is retained for provenance; replay is a test device"*, and it marks
    itself a deliberate departure. **The richness comes from the Receipt's `before`/`after`**, which
    makes the retained log reversible without re-simulating. **Not `KeyLog.serialize()`.**
17. **Do not add a value to `remit_acts`.** A CLOSED roster of six; `verb_table.yaml:341` already
    declares both substitutions. Adding `levy` hardcodes a ruling nobody made (D3, test 5).
18. **Do not make investigation a contest so the existing machinery can grade it.**
    `rosters.yaml:487-490` — *"forcing one mechanism's shape onto another because it is the one that
    exists."*
19. **Do not open a `needs_jordan` row.** The queue is at **zero** and this plan does not raise it.
    Before flagging anything, run §0's five tests in order — `CLAUDE.md` §0: *"a session that finds a
    stale `needs_jordan` on a settled question is expected to CLOSE it with its citation."* A wave may
    close a row, or open one **the code itself raises** (`Unspecified` with a `site:`). Nothing else.
20. **Do not mark anything done on a document.** §0.2. Not a `## Status:` line, not a `status:` edit
    in `requirements.yaml` (`register.py --requirements` is an **INDEX, not a gate** — editing a row to
    `met` passes), and never a green `m1_acceptance` row 4, which prints its own **DOC-DERIVED**
    warning and stands at 0/7.

---


# §7 · THE DESIGN RECORD — MOVED, not dropped

R1–R7 were restated here in the draft. They now live once, on `main`, in
**`references/design_rulings_2026-09-06.md`**, together with **R8** (partial observation), which
postdates this plan. Restating them here would be a second copy of a rule that lives once (§8).

⚠ **R8 is not reflected in the body above.** It lands on the same `H-62`/`H-84` spine this plan
makes first-rank, and it adds one finding the body does not carry: `Claim.value` has exactly two
readers in the loop, so any new claim shape is **refused at load** until its predicate stem is
declared. Read the rulings file alongside §3.

⚠ **This plan carries unresolved adversarial findings.** It was corrected three times and a critic
pass raised further items that were not worked through before the session closed. It is `PROPOSED`
and merging it ratifies nothing (§0.05, and its own status line). **Do not execute a wave from it
without re-running its §5 falsifiers first.**
