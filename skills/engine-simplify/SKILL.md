---
name: engine-simplify
description: >
  ENGINE SIMPLIFY — the module-scale `/simplify`: finds UNEARNED complexity in a named package of the
  Python oracle (`engine/`, `modules/`, `systems/<sub>/sim/`) and removes it. Twelve families,
  among them: a second owner of a rule; new apparatus where editing the existing owner would serve;
  scripting drift (per-case branches where a registry row or a general rule serves); a script where
  an existing tool serves; indirection with no second user; speculative generality; dead or
  retired-but-present code. Each finding passes an EARNING TEST (required by a ratified rule ·
  observed to move a measured output · planned by an open position · sole owner of a rule) and
  carries a PORT NOTE: what the Python construct becomes in GDScript for the Godot series
  ED-GO-0002 rules, read in that series' reference. Runs between `layer-conformance` Lens A and
  Lens B. Use for: "unearned complexity", "simplify this module/engine/system", "too much
  scripting", "new module or an edit to the existing one", "dead code in <package>", "what would
  this cost to port". Not for: a diff's line-level cleanup (`/simplify`), bugs (`/code-review`),
  layer placement or Layer-1 conformance (`layer-conformance`), whether a MECHANIC should exist
  (`ners`), inert design mechanics (`valoria-mechanic-audit`).
---

# ENGINE SIMPLIFY

## Status: RATIFIED on merge of its landing PR (CLAUDE.md §2, ED-1094). Requested by Jordan in session, 2026-10-28. Invocable as a project skill through the symlink `.claude/skills/engine-simplify`.

## What this skill owns, and what it copies

**It owns the EARNING TEST, the twelve families, and the PORT NOTE.** Everything else is read at its owner:

| the content | its single owner |
|---|---|
| what each layer binds; mechanism versus reference | **`CLAUDE.md`'s layer table**, §0.05 |
| when a guard is licensed | **`CLAUDE.md` §0.1 pt 5** |
| what the code architecture requires, and so what is already earned | **`architecture/meta/04_CODE_ARCHITECTURE.md`** |
| the pass's stages, the control, and what a pass may not produce | **`layer-conformance`**, sections THE PASS, THE CONTROL, WHAT THIS PASS MAY NOT PRODUCE — they apply here unchanged |
| tiering, fan-out sizing, what makes a critic independent | **`CLAUDE.md` §10** |
| review runs one round | **`CLAUDE.md` §0** |
| which Godot series is ruled | **`ED-GO-0002`**'s last row, until the machine-read owner GO-01 builds exists; **this skill names no version** (the plan's P11) |
| the project's own stance on the port | **`CLAUDE.md` §6**; **`04` §C.8–§C.10 and §C.12**; the PART D rows whose Python and GDScript grades differ |
| what GDScript can and cannot do | **Godot's reference for the ruled series**, read each time (below) |

- **Never copy a spec row, a table, a count or a GDScript fact into this file.** A copy rots silently and the next session reads the copy. `godot/godot_conversion_strategy_v1.md` is PROPOSED and `godot/godot_architecture_specification.md` is STALE (`CLAUDE.md` §6): neither is a source for the port note.
- **Bound.** Mints no guard, adds no CI check, produces no document, and nothing enforces it.

---

## Which skill takes the question

| the question | it goes to |
|---|---|
| Is this in the right layer? Does it conform to `04`? Should this guard exist? | `layer-conformance` |
| **Is this the least machinery that does the job?** | **this skill** |
| Does removing it change what the game does? | `ners` (the cut test) |
| Line-level reuse, efficiency or altitude in a diff | `/simplify` |
| A bug in a diff | `/code-review` |
| An inert or inconsistent mechanic in the design | `valoria-mechanic-audit` |

**The test that separates this skill from `ners`:** if removing the thing changes what the game does, it is a MECHANIC and `ners` owns the cut. If it changes only how the code arranges what the game does, it is APPARATUS and this skill owns it. A moved content hash is the boundary crossing (THE CONTROL, below).

## Order with `layer-conformance`, and the handshake

```
LC · Lens A  (placement; guards)  ──▶  ENGINE SIMPLIFY  ──▶  LC · Lens B  (conformance)
```

- **After A**, because simplifying an artifact A has found misplaced polishes the wrong thing. **Before B**, because a conformance verdict on code about to be deleted certifies it, and B must grade what remains.
- **A3 keeps guards.** Whether a *guard* earns its existence is `layer-conformance`'s question; every other piece of new apparatus is this skill's (F2).
- **`04` earns its own machinery.** A seam, the write gate, a typed result, a token, a by-path scan: where `04` requires it, it is earned by E1 and is not a finding. "Simpler than `04`" is amputation. Quote the deciding row verbatim, with its § (`layer-conformance` B0).
- **Where `04` itself forces machinery that looks unearned**, `layer-conformance` B4's three dispositions decide. Never edit `04` to make a simplification fit, and never simplify past it.

## Scope and unit

- **The unit is one named package or module** (a directory), not a diff and not the tree. If the request names none, ask one question; do not choose a sweep.
- Sweep only what the task is load-bearing on (`CLAUDE.md` §0.1 pt 5). `tools/` is in scope only for F2 and F4: a new tool where an existing tool, flag or registry row would serve.

---

## THE EARNING TEST

Machinery is **earned** if, and only if, one of these holds, **cited** (a finding that says "earned" without the citation has not run the test):

| | earned because | the citation |
|---|---|---|
| **E1 REQUIRED** | a ratified rule demands this shape | the `04` row, `ED-` id or `CLAUDE.md` § — quoted verbatim, with its §/line |
| **E2 OBSERVED** | collapsing or removing it moves a measured output | the run, before and after (THE CONTROL). This is how a mechanic is told from apparatus |
| **E3 PLANNED** | an open position in the one active plan (`CURRENT.md`'s "The plan" row) or an open M1 juncture needs it to exist | the position id. "Might be needed" is not E3 |
| **E4 SOLE OWNER** | it is the one place a rule lives that would otherwise live at several sites (`CLAUDE.md` §8, §0.05 cl.3) | the rule, and the sites that would otherwise carry it |

**Unearned** is none of the four. Fan-in of one is a *candidate*, never a verdict: a one-caller function that owns a rule is E4.

**The disposition ladder: take the first rung that serves.**

1. **Delete.** No reader; absence confirmed by a run (F7).
2. **Collapse.** Inline the single-use indirection; merge the second owner into the first (F1, F5).
3. **Make it data.** A per-case branch becomes a row in a registry the loop already opens at runtime (`CLAUDE.md` §0.05); never a new loader (F3).
4. **Extend the neighbour.** A row, field, parameter or branch in the existing owner, over a new module, class, registry, tool or flag (F2, F4).
5. **Keep**, with the earning cited in one clause in the commit paragraph.

**Relocation is not reduction (F8).** Moving the knot into config, a helper, a base class, the caller or a comment leaves the reader holding the same concepts. Pass condition: *the number of places a reader must open to predict the behaviour falls.* If it does not, revert.

---

## THE TWELVE FAMILIES — the manners of unearned complexity

Each: the signature · how to see it · the disposition. **Count with `ast`, resolve each hit to its enclosing `def`, and state what was searched and what was not** (`layer-conformance` B5, B6). A comment, a docstring or a `law=` string is not a call.

**F1 · A second owner.** A rule, constant, roster, term or ladder held in more than one place; a copy kept in step; two ladders for one quantity. *See:* grep the value and the rule's spelling; sync code is the symptom. *Dispose:* edit the owner, re-derive downstream, never keep the copy (`CLAUDE.md` §0.05 cl.3).

**F2 · Apparatus beside apparatus.** A new module, class, registry, loader, exporter, tool, flag or file next to an existing one doing a neighbouring job. *See:* for each new top-level artifact, **name the nearest existing owner and write the edit that would make it take the job** — a row, a field, a parameter, a branch. Look first at `engine/substrate/`'s leaf readers, `engine/season/data/`'s loaders, `references/*.yaml`, `tools/ci_common.py`, `references/ci_checks_registry.yaml`. *Dispose:* make the edit. The new thing stays only if that edit would give the existing owner a **second reason to change** — and the finding says which.

**F3 · Scripting drift, in code.** Branches keyed on an entity, outcome, id or verb name; a handler per case; an `if/elif` or `match` over a closed set a registry already lists; a constant per case (`CLAUDE.md` §0: *"scripting drift — stop"*). *See:* `ast` for string and name comparisons against members of a roster in `engine/season/rosters.yaml`, `verb_table.yaml` or the registry that owns the set. *Dispose:* a row, or the general rule.

**F4 · A script where a tool serves.** A one-off driver, shell pipeline or generator doing what an existing tool, flag, exporter or `--check` does; a hand-maintained derivative of a generated file. *See:* read `references/ci_checks_registry.yaml`'s `role:` lines before writing or keeping one. *Dispose:* use or extend the tool; delete the script.

**F5 · Indirection without a second user.** A wrapper, adapter, factory, base class or protocol with one implementation; a pass-through function; a parameter every caller passes identically; a flag never flipped; a config value only ever set one way. *See:* callers by `ast`. A seam `04` names is E1. *Dispose:* inline.

**F6 · Speculative generality.** An extension point, hook, registry or parameter for a future no plan position names. *Dispose:* delete; the position that needs it adds it, and its commit is the record.

**F7 · Dead, inert, retired-but-present.** An unreachable branch; a row, key or parameter nothing reads; a function with no caller; remnants of a retired system (the Key substrate, ED-IN-0232, and anything a `FORK:` row retires).
- **An absence is shown by a run** (`CLAUDE.md` §0.1 pt 3). The stdlib instrument, verified to run in this tree:
  `python3 -m trace --count --missing --module --coverdir=<scratch dir> --ignore-dir=/usr:/root engine.season.harness.headless --case NPC-088 --seasons 1 --seed 0`.
  Lines it did not execute begin `>>>>>>` in the `.cover` files; set `--ignore-dir` to this container's stdlib and site-packages. **That is one run.** The sentence reporting an absence names the runs (case, seasons, seed, test files); a line one case misses is not dead.
- **Inert by decision is not dead.** Check `engine/season/hole_register.yaml` and the ledger before calling a shipped-OFF feature dead.
- A retired file: ask `load_alias_map()` for the **exact** `FORK:` row. `pathres.resolve()` matches directory prefixes (`CLAUDE.md` §8).

**F8 · A knot moved.** Relocation presented as reduction (above); a boolean parameter selecting between two behaviours (two functions in one body). *Dispose:* split the flag, or revert the move.

**F9 · Redundant defence.** The same condition checked at several depths where an earlier check dominates and the later refusal cannot fire; a handler for what cannot occur. *See:* **plant the violation** and watch which check fires. A later check that never fires, with an earlier one that does, is redundant. **A swallowed failure is not a simplification:** the architecture requires holes to be loud and a refusal to be a value (`04` §C.12, rejection 5). Remove a duplicate; never remove the only check.

**F10 · A stored derivation, and its sync.** An aggregate computable from its owners, kept as a field; update-in-two-places code; a cache without a measured cost. *Dispose:* compute at read; delete the sync. Whether the *shape* is right is `layer-conformance`'s.

**F11 · Tangle.** A function doing several jobs; one state threaded through a long parameter list; a call-order dependency nothing states. At module scale this matters only where it hides F1–F10; the line-level cleanup is `/simplify`'s.

**F12 · Scaffolding that restates the implementation.** Fixtures duplicating a production builder (`build_realm`); a test that recomputes what it tests; a helper no test reaches. **Never delete an assertion that can observe a failure** (`CLAUDE.md` §0.1 pt 2; `layer-conformance` WHAT THIS PASS MAY NOT PRODUCE item 4).

---

## THE PORT NOTE — what Godot changes in the verdict

The Python under `engine/` is the **oracle**; a port serves the model and never corrects it (`CLAUDE.md` §6, ED-1050). Every finding, and every item kept under E1–E4, carries one line: **neutral · lowers port cost · raises port cost**, naming **the Python construct and the GDScript construct it becomes**.

**1 · Read the GDScript side in the reference for the ruled series.** The series is `ED-GO-0002`'s; the docs path is `https://docs.godotengine.org/en/<series>/`. Quote the page in the finding. **Not from memory, and not from `04` §C.12's sourcing, which was read against an earlier series: re-read.** A construct the page does not mention is *not documented*, which is not *absent*: say which. Also read the page that lists behaviour changes between the previous series and the ruled one.

**2 · The Python constructs to put the question to.** Each is a question for the reference, not an answer:

- **error signalling** — `raise`, `except`, `assert` as control flow (`04` §C.12 rejection 5 owns the project's position)
- **laziness** — generators, iterators, `yield`
- **expression density** — comprehensions, nested conditionals, chained operators
- **container kinds** — tuple, set, frozenset; non-scalar keys
- **number domain** — arbitrary-precision `int`; `//`, `%` and `/` on integers; `float` width (`04` §C.8–§C.10 names `Vector2` and fixed point)
- **order** — dict and set iteration order, sort stability and key functions
- **identity and copy** — aliasing, shallow copy (`04` PART D, D-49: a unit changing side mid-contest)
- **object model** — private constructors, mixins, multiple inheritance, decorators, metaclasses, operator overloads, `__eq__`/`__hash__`, frozen dataclasses, import-time effects, the module system
- **call shape** — `*args`/`**kwargs`, default arguments
- **recursion depth**, **text formatting**, **randomness** (global versus threaded; `04` §C.12 rejection 4), **I/O**

**3 · Four rules.**

a. **Do not simplify toward the Godot idiom.** `04` §C.12 lists five places where the idiomatic Godot answer is the wrong answer here. Taking one is E1-violating amputation, however simple it looks.

b. **Inside `port/` the reverse holds.** `04` makes `port/` the one place Nodes, the scene tree and signals appear; there the engine's own facility *is* the least machinery, and hand-building what it provides is F2 or F4. The port's repository (`valoria-game`) is not in this clone: read its code only where the session has it, and say where it does not.

c. **Do not pre-shape for the port.** Porting beyond the combat slice waits on the port gate (`CLAUDE.md` §6; the plan, via `CURRENT.md`). GDScript-shaped scaffolding written into Python before then is F6.

d. **Between two simplifications that serve equally, take the lower port cost.** A construct the reference gives no counterpart for, where a plain one serves without loss, is unearned twice. Converting `raise` sites to returned results is **not** a simplification: it is a wide, behaviour-neutral port project whose shape (`04` §C.12, "PROPOSED, not ruled") is not this skill's to choose.

---

## THE PASS

Stages, control and tiering are `layer-conformance`'s (THE PASS, THE CONTROL) and `CLAUDE.md` §10's. What this skill sets inside them:

| stage | this skill's content |
|---|---|
| **1 · PRE-FLIGHT** | the **census** of the unit, by `ast`, scope stated: top-level defs and classes, registries and their loaders, tool entry points and flags, each with fan-in (callers resolved to the enclosing `def`) and who opens each data file; beside each, the nearest existing owner. Batched on `valoria-measure` (Haiku); extract once, share it |
| **2 · WORK** | each census row through the EARNING TEST; dispose by the ladder; edits in this commit; THE CONTROL after **every** unit: zero game yield is the expected result, and a moved hash or a flipped probe verdict means the unit is a mechanic, not apparatus — revert it and say so |
| **3 · ATTACK** | `valoria-critic`, read-only, sees stage 2's **output** only. It tries to: find a caller, reader or execution for every deletion, **by running**; show that every "extend the neighbour" gave the owner a second concern; open every cited earning and show it does not land; plant a violation for every F9 removal |
| **4 · RECONCILE** | each finding applied, or refuted by the measurement that refutes it |

- **Tier it** (`CLAUDE.md` §10): the census is mechanical (`haiku`); earning and port-note verdicts are judgment (`opus`). Set `model:` explicitly. One producer per package; no lane count is mandated.
- **One round** (`CLAUDE.md` §0): the named unit plus its one pass is the stop condition. Its fixes are not themselves audited, and a second wave starts only after you report what the first found.
- **A pass that finds nothing has not run.** *"I attacked X as unearned and it holds, because Z"* is a pass. Report the unit, the census size, and the attacks that failed.

## WHAT THIS PASS MAY NOT PRODUCE

`layer-conformance`'s seven prohibitions bind here. In addition:

1. **No candidate list.** No register of simplifications, no TODO file, no census document: a finding that needs no ruling is fixed in this commit or dropped (`CLAUDE.md` §0).
2. **No guard that the unit stays simple.** Its subject would be the repository's process, not the game (§0.1 pt 5).
3. **No behaviour change called a simplification.** A moved hash is a mechanic's cut: revert, or hand it to `ners`.
4. **No edit to `04` or to anything under `architecture/`** to make a simplification fit.
5. **No Godot version asserted**, no port-shaped scaffolding, and no `raise`-to-result sweep (port rule d).

## THE FALSIFIERS — how a reader tells whether this pass ran

| the claim | what would show it false |
|---|---|
| *"unearned"* | none of E1–E4 is shown to have been tested against it |
| *"earned"* | the citation is absent, or does not land when opened |
| *"dead / unused / never fires"* | no run is named, or the named run cannot reach it |
| *"only one caller"* | the sentence does not say what was searched; hits were counted as text, not resolved to a `def` |
| *"the existing owner could take it"* | the edit is not written out |
| *"simpler"* | the content hash moved; or the places a reader must open did not fall |
| *"port cost lowers / raises"* | the Python construct, the GDScript construct, or the page read for the ruled series is not named |
| *"conforms to the Godot way"* | `04` §C.12's rejections were not checked first |
| *"the critic found nothing"* | no named failed attack, only an absent finding |

**If this skill conflicts with `CLAUDE.md`, `architecture/` or `layer-conformance`, they win**; correct the skill.
