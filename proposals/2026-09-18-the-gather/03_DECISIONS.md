# 03 · DECISIONS — the decision-layer trees, dispositioned

## Status: **DISPOSITION (2026-09-18).** A terminal verdict about artifacts that already exist, recorded beside them (`CLAUDE.md` §0's narrow exception). **It creates no work.** The ORDER is not this file.
## Authority: **none over canon.** Every verdict is a reading of the tree as it stands at `ac78f03`; no `## Status:` line elsewhere is flipped by this file, and `CURRENT.md:31` is deliberately left alone (`ED-IN-0251`).
## Verdict set, CLOSED: `LIVE` · `SUPERSEDED` · `ABSORBED` · `SPENT` · `ORPHAN` · `NEEDS-STATUS`. Split dispositions name their files.
## Every row carries `engine_season:` — the concrete `engine/season/` change implied, or the literal `NONE` (§3's precondition). `NONE` is the common case and is honest.
## Reads: `CLAUDE.md` §0, §0.05, §0.06, §0.2, §3 · `00_THE_CENSUS.md` (the figures, not re-measured) · `registers/editorial_ledger_in.jsonl` last row (`ED-IN-0251`).

---

## §1 · `proposals/2026-09-16-conviction-decision-layer/` — 8 files, 2,621 lines, 38 inbound

**Tree verdict: `LIVE`, partly `ABSORBED`.** It is the most-cited tree in the corpus after the two
governance suites, and it is cited *as a register* — `ED-IN-0251`, `01_THE_BUILD_ORDER.md` and
`proposals/2026-09-18-character-decision-layer/PROPOSAL.md` all resolve `STR-*` / `CAT-*` / `R7`
identifiers into `adjudication_register.yaml`. A tree whose identifiers three live surfaces cite by
number is not retirable by disposition; it is a reference work.

⚠ **AND THE 38 ARE NOT SPREAD ACROSS THE EIGHT FILES.** `00_THE_CENSUS.md` §3 counts the **directory
basename**, which cannot attribute to a file, so this lane re-took it per filename — citing lines
outside the tree, excluding `.designs/` and this file:

```
adjudication_register.yaml  75   synthesis.md               154 (~22 distinct files)
candidate_basis_v1.json      8   formal_analysis.md           4
interrogation.md             2   decision_layer_v1.md         2
behaviour_algorithms.md      1   behaviour_census.md          0
```

⚠ **THESE DO NOT SUM TO 38 AND ARE NOT MEANT TO — the predicate is different in three ways**
(`00_THE_CENSUS.md` §1's own warning, applied to itself). The census counts **directory-basename
occurrences from `proposals/` only**; this counts **filename occurrences repo-wide except
`.designs/`**, and counts **lines**, so one file citing a name eight times contributes eight.
**Quote a predicate with either set or quote neither.**

**Two files carry the tree's entire inbound weight; four carry almost none, and one carries none at
all.** That is the measurement the SPENT verdicts below rest on, and it is why the tree verdict and
the file verdicts differ without contradicting each other. ⚠ `synthesis.md`'s 154 is the **least
trustworthy** figure here: it is a bare filename, and citing a document by bare filename across
twenty-two files is §4's idempotency hazard in its own right — a cold reader cannot tell which
`synthesis.md` is meant. Treat it as an upper bound.

| file | lines | verdict | on what evidence | `engine_season:` |
|---|---|---|---|---|
| `adjudication_register.yaml` | 739 | **LIVE**, three rows **ABSORBED** | `STR-6` → `ED-IN-0251` R1, which closes rather than reopens it, citing `:104,:162,:194-195`. `CAT-2` → `verb_table.yaml`'s `beneficiary:` column + `beneficiary_of`/`benefits_me` in `decision/choose.py` (`ED-IN-0248`). `STR-1` → `(Person, scar[axis])` in `loop/effects.py` + `state/carriers.py` (`ED-IN-0249`). Its `rename_cost_measured` block at `:679-681` is the ONLY place the 40/60/107 figures are authored; both `01_THE_BUILD_ORDER.md:1028` and `RULINGS.yaml:1356-1357,1395-1396` quote it, so it is one measurement with three voices, not three | **NONE.** A register of rulings; its absorbed rows already landed |
| `synthesis.md` | 162 | **LIVE** as reference, **challenged** | Its own head declares itself *"Superseded in part by ED-IN-0232"* and corrects the affected sentences in place — that is §0.05 cl.3 done right. `§1.3`'s `pull(c) − cost(c)` is `01_THE_BUILD_ORDER.md:1032`'s specification of item `6f`, so the file is load-bearing on a scheduled row. `PROPOSAL.md` §4 F1/F5 argues the minus sign away, but a PROPOSED document with 0 inbound does not supersede one with 38 | **NONE** — and `6f` has **zero lines in the tree**, so there is nothing to change yet |
| `behaviour_census.md` | 278 | **SPENT** | A 2026-09-16 measurement of what existed. Two of its gaps have since been filled (`6d`, `6e`) and its aperture/discrimination numbers are re-taken by `../2026-09-18-conviction-basis-probe.py`, which is committed and control-paired. It also carries the ED-IN-0232 casualty list, which is why it is SPENT and not ORPHAN: that list is still the only enumeration of what died with the Key substrate | **NONE** |
| `behaviour_algorithms.md` | 448 | **SPENT** | Three candidate architectures, none built. `synthesis.md` §1.2's one-machine fusion collapses its distinctions and says so; the register's rulings went to the fusion | **NONE** |
| `formal_analysis.md` | 254 | **LIVE** as reference | **This is where `R7` is derived** — `:183` *"R7 — Projection non-separability"*, `:195`, with its own falsifier at `:249` (*"R7 assumes the projection stays linear"*). The register restates its binding at `adjudication_register.yaml:224-228` (*"R7 BINDS HERE AND ONLY HERE"*), which is the line `PROPOSAL.md` §1 cites. `R7` is the linear-map constraint deciding whether a quantity may be a projected axis, so it **forces `6c`'s shape** | **NONE** |
| `interrogation.md` | 354 | **SPENT** | The question-raising stage that produced the register. Its questions are the register's rows; the register is cited and this is not | **NONE** |
| `decision_layer_v1.md` | 363 | **NEEDS-STATUS** | The `_v1` suffix and the filename both assert a head, and §4's *versioning ≠ currency* rule says only `CURRENT.md` or a `## Status:` line can settle it. `CURRENT.md` has no row for a decision layer, and the live decision layer is `engine/season/decision/`, which this document does not describe. **The name is the defect, not the contents** | **NONE** |
| `candidate_basis_v1.json` | 23 | **LIVE**, and **the one file here with a Layer-2 reader** | `engine/season/harness/conviction_spread.py:230` exposes `--candidate FILE.json`, and the 09-18 probe's own closing block prints the exact invocation naming **this path**. `:232-235` records why the flag exists: `spread(candidate=…)` shipped 2026-09-16 *"with no caller anywhere in the tree"*. ⚠ **The harness does not hardcode it** — the path arrives on the command line — so this is a documented coupling, not an import. It is still enough that **the 09-16 directory cannot be moved or deleted without breaking a printed command** | **NONE** — a proposal-side comparison arm, never engine data. The control is printed first (`:241`), which is §0.1 pt 4 |

---

## §2 · `proposals/2026-09-18-character-decision-layer/PROPOSAL.md` — 1 file, 352 lines, 0 / 1 inbound

**Tree verdict: SPLIT, and the split is the finding.** The file declares at its own head: *"THIS FILE
IS A QUEUE BY CONSTRUCTION AND DOES NOT CLAIM §0'S EXEMPTION. §7 creates work for a future session."*
Taken at its word, §0's test — **does this document create work for a future session?** — answers YES
for §7 and §9 and NO for §2, §4 and §6. So it disposes in parts.

| section | verdict | on what evidence | `engine_season:` |
|---|---|---|---|
| **§1** (R1/R2/R3) | **SUPERSEDED** by `registers/editorial_ledger_in.jsonl` last row, `ED-IN-0251` | §1's own framing — *"recorded in commit messages only; none is in a ledger yet"* — was true when written and is false since `ac78f03`. ⚠ **AND THE TWO NUMBERINGS COLLIDE ON `R3`:** this file's R3 is *"reconcile or replace. best design wins."*; `ED-IN-0251`'s R3 is *"The cells are yours."* R1 and R2 agree between them verbatim. **Two documents number Jordan's 2026-09-18 rulings 1-2-3 and mean different things by the third label.** The ledger is the authority (§2); this file's R3 is a fourth ruling wearing the third's number | **NONE** |
| **§2** (vocabulary) | **LIVE** | §2.4's `docket` collision is measured against live code, and `precedence` is measured free. §2.2's class test (FIELD / READOUT / STRUCTURE / DISPOSED) is the one instrument in either tree that *collapses* a basis rather than growing it — five folk terms to one `bend_price` field | **NONE** |
| **§4** (the free cuts) | **LIVE**, and **it is what the lane turns on** | F1 reports that `synthesis.md` §1.3's justification for the minus sign is not load-bearing. **Both its citations opened, and one is off by a few lines:** `options.py:141` is exact — the `law=` string reads *"capability supplies dice and GATES NOTHING (#353 §9.2)"*. `resolve.py:388` is **not** the cited content: the `Ob > mult × Pool` refusal is at `:385` and *"the computed chooser never sets"* `Act.obstacle` is at `:393`; `:388` sits inside an unrelated `[ROOT]`-antecedent comment. **The substance survives the correction, the citation does not.** If F1 holds, `6f`'s *specification* is wrong before `6f` is built. **Nothing is deleted, because nothing was built** | **NONE today.** If F1 is accepted the change is to `01_THE_BUILD_ORDER.md:1032`'s row, not to code |
| **§6** (measurements) | **LIVE**, execution-grade | The only §0.2-grade artifact in either tree: an instrument that runs, control-paired, with `--prove-control` proving the control assertion fires. Its aperture finding — **28 candidates, 28 verbs, 1 subject for all 46 persons** — is what makes the whole precedence band a no-op with respect to the person today | **NONE** — a measurement, not a change |
| **§3, §5, §7, §9** | **NEEDS-STATUS** | §7 is a 9-step build order that **competes with `01_THE_BUILD_ORDER.md:1027-1033`** without citing it: its step 8 is that file's `6a`, and its own §7 note says *"`6f` is not on this list."* Two live build orders for one subsystem is the shape §4's idempotency rule exists to prevent. §9 escalates six items to Jordan of which **items 5 and 6 are already `ED-IN-0251` R3** — the affiliation roster, the pairs, the intensity scale, the 13×N cells — so two thirds of §9's Jordan-facing list is answered by step 1 of §0's five (superseded) | **NONE** |

**Not ORPHAN, and the census's own reading is where that comes from.** `00_THE_CENSUS.md` §3 reads
`0 / 1` as *"an orphan one day old"*. On the evidence the weaker reading is the right one: it is **one
day old**, and inbound-reference count cannot distinguish a neglected document from a new one. What it
*can* say is that nothing yet depends on it, which is exactly why §7's queue can be left unstarted at
no cost.

---

## §3 · The worksheet and the probe

| file | verdict | on what evidence | `engine_season:` |
|---|---|---|---|
| `proposals/2026-09-18-conviction-basis-worksheet.yaml` | **LIVE** (the authoring surface), header block **ABSORBED** | `ED-IN-0251` exists because this file's `:13-21` header held all three rulings and labelled itself *"NOT YET RECORDED IN THE TREE"*, in a file whose own instructions say it gets deleted. The absorption is complete: the ledger row names the owners the values land at **precisely so it outlives this file**. What remains LIVE is the empty cells — R3's authoring request | **PENDING, and it is R3's.** `engine/season/rosters.yaml`: `tables.conviction_projection` and `tables.alignment` re-authored when Jordan's cells land. Not a session's to write |
| `proposals/2026-09-18-conviction-basis-probe.py` | **LIVE**, executable, **RE-RUN IN THIS LANE** | 272 lines; `ED-IN-0251` names it as the committed instrument for every number in the 09-18 review. **Run today, not merely cited** (§0.1 pt 3 row four): it reproduces `PROPOSAL.md` §6 exactly — 46 persons · 41 distinct conviction vectors · 6 distinct top verbs · rank disagreement median `0.2882` · candidates/verbs/subjects `28 / 28 / 1` for every person · `0` excluded to empty. Its header prints *"the shipped tau=0.1"*, which is what §6 below turns on. ⚠ It has **no argparse on `--help`**: passing `--help` runs the full probe. This is the artifact §0.2 accepts and the one mechanism in this lane | **NONE** — it reads `engine/season/`, it does not change it |

---

## §4 · 6a / 6b / 6c, PRICED — and 6b's price is not what the row says

`01_THE_BUILD_ORDER.md:1027-1029` holds the three rows, atomic by its own argument (*"Doing it
separately means doing it twice"*). `ED-IN-0251` R1/R2 unblock them by freeing the word. **Two
findings change the price, in opposite directions.**

### 4.1 ⚠ `6b`'s stated mechanism DOES NOT EXIST

`:1028`'s home column reads: *"`references/names_index.yaml` is the TERMS owner; the rename derives."*

- **The executor is retired.** `references/names_index.yaml:13-14` advertises
  `tools/valoria_rename.py` as *"the 'change once' executor: edit a `canonical` here … and every
  occurrence across docs/params/registries is rewritten."* That file is **not in the tree**, and
  `references/restructure_ledger.md:1525` is its `FORK:1e4c6f4` row. **The rename does not derive
  today; the tool that would derive it was deleted.**
- **And `names_index.yaml` is not the owner of the thirteen.** Its `conv.*` block is **seven**
  entries at `:105-111` — `Faith · Order · Reason · Equity · Precedent · Autonomy · Continuity` —
  glossed at `:63` and `:100` as *"the 7-axis character conviction class"*. Four of those seven
  (`Reason`, `Autonomy`, `Continuity`, and the absence of six of the thirteen) do not appear in
  `references/descriptor_registry.yaml:236`'s `conviction_roster`, which is `count: 13` and is what
  `engine/season/rosters.yaml:228` binds with `from_descriptor: conviction_roster`. Every `conv.*`
  entry is `enforce: warn`. **`names_index.yaml` holds a stale parallel roster, not the head.**

**The real owner chain, opened and verified:** `references/descriptor_registry.yaml:236`
(`conviction_roster`, `count: 13`) → `engine/season/rosters.yaml:193-228` (`convictions`, with
`from_descriptor: conviction_roster`) → `engine/engine_params/descriptors.json` behind the blocking
`--check` → `engine/substrate/descriptors.py`. **That chain does derive**, and it is `6a`'s and `6c`'s
home. `6b` — the *identifier* `conviction` in 29 Python files under `engine/` (308 occurrences) — rides
no chain at all.

### 4.2 The 107-document arm has fallen to 12

`adjudication_register.yaml:681` measured *"107 design documents under `systems/ canon/
architecture/`"* on 2026-09-16, **before `ED-IN-0231`**. Re-taken today: `systems/` holds **0** `.md`
files at all, and `grep -rl conviction --include='*.md' systems/ canon/ architecture/` returns
**12**. The other **66** are under `.designs/`, quarantined, each carrying an `ARCHIVED-NOT-CANON`
banner — **not canon, not edited, not part of any rename.** The register's figure is not wrong; it is
**stale by one structural change**, and `01_THE_BUILD_ORDER.md:1028` and `RULINGS.yaml:1356-1357`
both carry it forward unre-measured. That is §0.1 pt 3 row four's carried-forward-figure defect, and
it inflates `6b` by a factor of nine on its largest arm.

### 4.3 The priced read

| | what it actually costs | derives? |
|---|---|---|
| **6a** — affiliation roster + `incompatible` relation | **Jordan's content, then one owner edit.** Two new rosters and one relation at `references/descriptor_registry.yaml`, then `engine/season/rosters.yaml` binds them by `from_descriptor`. `church_standing` at `rosters.yaml:312` is one unread string in the `standing` claim-predicate `values:` list and is **not** a foundation to build on | **YES** — the descriptor→rosters→`descriptors.json` chain, behind the existing blocking `--check` |
| **6b** — rename the moral-value basis | **A HAND SWEEP, or restore `tools/valoria_rename.py` from `FORK:1e4c6f4` first.** 29 Python files / 308 occurrences under `engine/`, 51 YAML/JSON under `engine/ references/ registers/`, **12** live `.md` — not 107. The falsifier already exists and is green: `tests/valoria/test_conviction_roster_single_owner.py`, **3 passed in 0.93s**, which fails if a second roster ships | **NO.** §4.1. This is the single most consequential correction in the lane |
| **6c** — re-author the thirteen and their projection | **Atomic with 6a by a module-scope constraint, and that constraint is real:** `:1029` states `_load_projection`/`_load_alignment` raise at module scope, so the projection and its alignment table must both exist before first import. Content is R3's; the migration is one commit or none | **YES**, same chain as 6a |

**engine_season for all three:** `engine/season/rosters.yaml` — `tables.conviction_projection` and
`tables.alignment` re-authored, plus two new roster bindings; **upstream of it**
`references/descriptor_registry.yaml`. **No `engine/season/*.py` change is implied by 6a or 6c** —
`decision/choose.py:358` hoists `axis_w = project(p)` once per deliberation and `:359-360` reads
`align(c.verb, ax)`, both resolving by name off the rosters, so a re-authored table reaches the
chooser without a code edit.
**That is the one genuinely cheap thing in the lane, and it is cheap because `U3` already paid for it.**

---

## §5 · Collisions recorded, not resolved

1. **`CURRENT.md:31` against `ED-IN-0251` R2.** The row still reads that the 13 Convictions and
   territory-scale Piety are *"DISTINCT and unchanged"*. **Recorded in `ED-IN-0251`; not this file's
   finding, and not flipped here.** Where it bears on a disposition: it is why
   `decision_layer_v1.md` reads **NEEDS-STATUS** rather than SUPERSEDED — the Layer-0 index has no
   row for a decision layer, and the one row it has on this subject is the stale one.
2. **Two `R3`s** (§2, row `§1`). The ledger wins; the PROPOSAL's *"best design wins"* is a real
   quotation under a colliding label.
3. **Two live build orders** for one subsystem: `01_THE_BUILD_ORDER.md` §7.5 and `PROPOSAL.md` §7.
   Neither cites the other. **Only the orchestrator can decide which is the order.**
4. ⚠ **`R7` IS TWO RULINGS, AND THE OTHER ONE IS IN LAYER 2.** Found while checking whether the
   identifier resolves. In this tree `R7` is *projection non-separability*
   (`formal_analysis.md:183`, restated `adjudication_register.yaml:224-228`). In `engine/season/`
   `R7` is the **fan-out / witness-deposit** ruling that took `fan_out_mode` off `total`
   (`ED-IN-0205`) — `hole_register.yaml:2214`, `rosters.yaml:499` (*"`R7` chose the architecture
   model over the echo model"*), `requirements.yaml:430` (*"Under `R7` the default is `all_five`"*).
   **Both are live, both are cited by bare `R7`, and one lives in the code's own registries.**
   `PROPOSAL.md` §1 cites *"`R7` … a ratified constraint"* unqualified. This is §4's
   idempotent-in-meaning rule failing on a process identifier, and it bears on a disposition: it is
   the second reason `formal_analysis.md` is LIVE rather than SPENT — it is the only place the
   projection sense is **derived**, so it is what a cold reader needs to tell the two apart.

---

## §6 · One claim handed to this lane, checked at the call site, and it is stale

**Handed:** *`R-08`'s measured block says non-rationality DOES NOT EXIST — `make_chooser` sorts on
`(-score, verb, subject)`, so a tie breaks ALPHABETICALLY BY VERB.*

**At the call site it is half true and the live half is the other one.**
`engine/season/decision/choose.py:370` does sort exactly that key — but **`:375` immediately re-orders
the result** through `_sample_order`, which at a nonzero `choice_temperature` (`:279`) adds
candidate-keyed Gumbel noise to `score/tau` and re-sorts (`:317`). Its own comment at `:315-316` names
the trailing `(verb, subject)` terms as *"a STABLE TOTAL ORDER for exact float ties, which continuous
noise makes measure-zero; **they are not the tie-break — `g` is**."* Its docstring adds a second
correction this lane should not repeat: the phrasing *"the rest TIE and are ordered alphabetically by
verb name"* is **not `H-96`'s** and was mis-attributed to it — it is `requirements.yaml`'s `R-08`.

**And `requirements.yaml` already says so, in the same row.** `R-08`'s `measured:` block opens with
the stale sentence at `:446-451` and then corrects it at `:452` — *"THE LAST SENTENCE IS FALSE AS OF
`U4` (2026-09-10)"* — and corrects the `decision.py` citation at `:472-474` (it is
`decision/choose.py` since `ED-IN-0206`). `R-06` carries the same self-correction at `:390-392`.
**The row stays `partial` for a different and still-true reason:** a tie is broken **by the draw,
which is not the person** — *"the absence of a reason, not a reason of theirs"* (`:462`).

**Which is precisely what 6a–6c buy.** The `2–7 of 22` discrimination figure (`:389`, `:448`) is also
superseded in place by `U3`: `7..11 of 28 → 16..22 of 28`, mean `7.79 → 21.84`, control from a
worktree at `a85bd45` (`:393-401`). ⚠ **Do not quote `2–7 of 22` again without the `U3` correction
attached** — it appears twice in the file and is corrected once.

---

## §7 · What would show this file wrong

- **§4.1 fails** if `tools/valoria_rename.py` is restorable and still runs against today's tree —
  the fork ref is `1e4c6f4` and checking it out is the one command that settles it. Restore it and
  `6b`'s home column becomes true again.
- **§4.2 fails** if any of the 66 `.designs/` documents is load-bearing on a rename. They carry
  `ARCHIVED-NOT-CANON`; if one is read by a tool, `ED-IN-0231`'s invariant is broken independently.
- **§1's SPENT verdicts fail** if an inbound citation reaches those files by an **identifier** they
  own rather than by filename. The per-filename sweep is run and reported in §1; what it cannot see
  is a citation of the form *"`STR-4` says…"* whose text lives in `interrogation.md`. **Checked:
  every `STR-*` and `CAT-*` id in this tree is defined in `adjudication_register.yaml`** (fifteen
  `id:` keys, `:291`–`:723`) **and nowhere else in the tree**, so the SPENT files own no cited
  identifier. `R7` is the one that does not behave — §5 item 4.
- **§2's split fails** if `PROPOSAL.md` §4's F1 is wrong, because F1 is what makes §4 LIVE rather
  than SPENT. Its falsifier is its own §8 and it names it.
