# The decision layer: execution plan (pursuits, religious conviction, scars, deontology gate)

## Status: **PLAN (2026-09-26). RATIFIES NOTHING. NOT A RULING AND NOT AN ARCHITECTURE PROPOSAL.**
## Authority: **none claimed.** Supersedes nothing. Unlike `../2026-09-18-character-decision-layer/PROPOSAL.md`, this file puts no ADOPT/HOLD question to Jordan. The architecture it schedules is already ruled (ED-IN-0251, ED-IN-0261, ED-IN-0267, ED-IN-0268). **Its job is sequencing.**
## Lane: `IN` · no ED id allocated · `references/id_reservations.yaml` untouched
## Grade under `CLAUDE.md` §0.2: **`paper`** throughout. Nothing here executes. Every code-state claim was **read on disk at the cited line** by a read-only `fable`-tier audit (`CLAUDE.md` §10), and this plan then ran an independent `opus`-tier antagonist pass against the working tree, which found and corrected sixteen defects in the first draft (citation errors, a hidden circular dependency, two mischaracterized handshakes, and one reversed recommendation). Figures quoted from elsewhere (28/28/1, 2,403, 7→8/31) are **cited, not re-taken**; the verb-count arithmetic is shown explicitly at §3.2/§3.3 rather than quoted as a bare figure, because the antagonist pass found the audit's own "19→22" and "40 verbs" figures did not add up.
## Reads: `CLAUDE.md` §0 (the five-step `needs_jordan` gate), §0.05 (code is mechanism), §0.1 pt 3 (name the falsifier), §7 (golden re-pins).
## Beside it: `../2026-09-20-pursuit-basis-worksheet.yaml` (the head per `CURRENT.md:25`) · `../2026-09-18-conviction-basis-worksheet.yaml` (affiliation candidates) · `../2026-09-18-character-decision-layer/PROPOSAL.md` (§7 build order, §9 open questions)

> ⚠ **THIS FILE IS A QUEUE BY CONSTRUCTION AND DOES NOT CLAIM §0'S EXEMPTION.** §3 creates work for a
> future session, which is what an execution plan is. **The record dies when its subject dies:** once
> H1–H13 have landed or been dropped, delete this file.

---

## §0 · What this is and is not

**It is** a scheduling document over architecture that is already ruled. It does five things:

1. States what the ledger records.
2. States what the code actually holds.
3. States what moved after the documents were written.
4. Runs every open item through `CLAUDE.md` §0's five-step gate.
5. Orders the remaining work into handshakes with explicit preconditions, deliverables, falsifiers and
   owner types.

**It is not** new design. **It authors no mechanism, no value, no cell, and no name beyond those
already cited.** Where a handshake needs a magnitude, the magnitude is either (a) already ruled, with a
citation, or (b) carried as a swept `Fixtures` arm with control `0`, per the H-128 precedent. It never
supplies a number of its own.

**It does not answer G-Q1 to G-Q6.** §5 puts them to Jordan verbatim, with no recommendation attached.

**Shipped before this plan and not re-scheduled here:**

- the rename (#428)
- the kill/wound admission (#424)
- H-71 (#428)
- the `CURRENT.md:31` flip

---

## §1 · Ledger discrepancies found

**The ledger rows, verbatim fields:**

| id | file:line | `status` | `needs_jordan` | note |
|---|---|---|---|---|
| ED-IN-0251 (row 1, 2026-09-18) | `registers/editorial_ledger_in_archive.jsonl:167` | `"ruled"` | `true` | R1/R2/R3 recorded; R3 = "the cells are yours" |
| ED-IN-0251 (row 2, 2026-09-19, `supersedes_row: true`) | `…in_archive.jsonl:168` | `"ruled"` | `false` | flips CURRENT.md:31 ("Truth becomes Conviction"). ⚠ Its text says R3 is *"still needs_jordan and still Jordan's to author"* while the field reads `false`. The governing row's field and prose disagree |
| ED-IN-0252 | `registers/editorial_ledger_in.jsonl:19` | `"proposed"` | `false` | the gather; "HELD BACK IN FULL", ratifies nothing |
| ED-IN-0261 | `…in_archive.jsonl:177` | `"ruled"` | `false` | `jordan_decision: "2026-09-20"`; carries both same-day amendments (faith keeps row; kill/wound admitted) |
| ED-IN-0267 | `…in.jsonl:20` | `"resolved"` | `false` | H-71 others-half, `claim_subjects` expansion keyed `t.kind == "hold"` (`engine/season/epistemic.py:192`) |
| ED-IN-0268 | `…in.jsonl:21` | `"resolved"` | `false` | pure rename; explicitly "THE CONTENT HALF … IS NOT THIS ROW" |

**Where the rows live:** ED-IN-0261 is in the *archive* file (`registers/editorial_ledger_in_archive.jsonl`),
not the main one.

### §1.1 · Correction: ED-IN-0251 row 2's field contradicts its own text

**Citation:** `registers/editorial_ledger_in_archive.jsonl:168`, ED-IN-0251 row 2 (2026-09-19,
`supersedes_row: true`).

- **The field** reads `needs_jordan: false`.
- **The row text** says R3 is *"still needs_jordan and still Jordan's to author"*.

Row 2 supersedes row 1 (`:167`, `needs_jordan: true`), so it is the governing row, and its field and
its prose disagree. **This is a real disagreement inside the ledger, not a formatting slip.** This plan
does not settle it in either direction:

- **If the field is right,** R3 is no longer Jordan's, and the text is wrong.
- **If the text is right,** the field under-reports the escalation. §1.2 is that case.

### §1.2 · Correction: the ledger under-reports escalation

**No row among ED-IN-0251, 0252, 0261, 0267 and 0268 reads `needs_jordan: true` today.**
ED-IN-0251 row 1 (`:167`) does, but row 2 (`:168`) supersedes it with `false`. **Yet content items
remain open on Jordan alone.**

**The audit gives two counts, recorded here without reconciling them:**

- **§A's text says "two content items are open on Jordan (§D)".** These are the two items that reached
  a **CONTENT** verdict in the five-step gate: D5 (affiliations) and D6 (the cells).
- **§E's reconciled table marks six rows OPEN-CONTENT-JORDAN-ONLY.** Four are unqualified:
  1. the 105 cells plus the alignment re-cell
  2. per-character and role-template migration
  3. the affiliation roster, pairs and intensity
  4. verb × affiliation engagement

  Two are qualified:
  - `Person.precedence` ("design fork, non-blocking")
  - crisis threshold 3 ("narrow")

**Under any of these counts, zero `needs_jordan: true` rows is an under-report.** `CLAUDE.md` §0's rule
"`needs_jordan` IS NOT A PARKING SPACE" cuts both ways. Clearing dead questions is session work, and so
is escalating what survives all five steps. The items in §2 marked OPEN-CONTENT-JORDAN-ONLY survived
the gate in §2.1. **None of them has a ledger row that says so.**

*Which row should carry the flag (a corrected ED-IN-0251 row, or a new row) is not decided here.* It
depends on how §1.1 resolves.

---

## §2 · Reconciled ground truth

**The four status classes:**

- **RATIFIED-ARCHITECTURE:** ruled, whether built or not.
- **LANDED-IN-CODE:** executes today.
- **OPEN-ENGINEERING:** buildable by a session with no further ruling.
- **OPEN-CONTENT-JORDAN-ONLY:** needs values or choices only Jordan can author.

| item | status | citation |
|---|---|---|
| `conviction` reserved for religion; Truth absorbed (R1/R2) | RATIFIED-ARCHITECTURE | ED-IN-0251 rows 1-2; `CURRENT.md:31` |
| 15 pursuits, 7 bipolar axes (names) | RATIFIED-ARCHITECTURE | ED-IN-0261; worksheet `:32-47,69-76` |
| `Person.convictions`→`pursuits`, `conviction_axes`→`pursuit_axes`; `Person.marks` deleted | LANDED-IN-CODE | ED-IN-0268; `carriers.py:456`; `rosters.yaml:303-305,1419-1422` |
| `Person.orient` dropped; `benefits_me` column survives | RATIFIED-ARCHITECTURE (never built / already built) | ED-IN-0261; `HANDOFF_IN.md:23` |
| `kill / wound` admitted to `resolvable_verbs` + three fold fixes | LANDED-IN-CODE | `verb_table.yaml:292-298`; ED-IN-0261 amendment 2 |
| H-71 others-half (witnessed seating; `commit` Tenure stays opaque) | LANDED-IN-CODE | ED-IN-0267; `epistemic.py:192` |
| `faith` keeps its row | RATIFIED-ARCHITECTURE | worksheet `:116-122` |
| Deontology = refusal at `opening_set`, person-side | RATIFIED-ARCHITECTURE, **OPEN-ENGINEERING** (exercisable only after cells) | ED-IN-0261; `options.py:35` (no gate) |
| Scars: counts, thresholds 1/2/3, both tracks, written at RESOLVE via `observers_for` | RATIFIED-ARCHITECTURE, **OPEN-ENGINEERING** | worksheet `:181-199`; `effects.py:340-407` (float model still live) |
| `kill`/`wound` split; `fight`, `challenge`→`accept` rows | RATIFIED-ARCHITECTURE, OPEN-ENGINEERING (rides cells) | ED-IN-0261; `HANDOFF_IN.md:24`; no rows in `verb_table.yaml` |
| 105 projection cells + alignment re-cell (42 verbs, corrected from the audit's "40" — see §3.3) | **OPEN-CONTENT-JORDAN-ONLY** | worksheet `:100-114,157`; `rosters.yaml:1449-1513` unchanged |
| Per-character / role-template migration to the 15 | **OPEN-CONTENT-JORDAN-ONLY** | `cast.py:197-211`; `rosters.yaml:1352-1417` (corrected range — see §2.2's antagonist correction); ED-IN-0268 ("Jordan's later, separate content step") |
| Affiliation roster, 10-pair incompatibility, intensity scale | **OPEN-CONTENT-JORDAN-ONLY** | ED-IN-0251 R3; old worksheet `:39-81` all `~` |
| Verb × affiliation engagement (what act violates a religious conviction) | **OPEN-CONTENT-JORDAN-ONLY** (never asked) | no table exists; `alignment` is verb × moral-axis only (`rosters.yaml:1526`) |
| `Person.precedence` / per-person test order | OPEN-CONTENT-JORDAN-ONLY (design fork, non-blocking) | PROPOSAL `:339-344`; `03_DECISIONS.md:69` |
| Crisis reader, threshold 2 | OPEN-ENGINEERING | H-128 `:958-962` precedent |
| Crisis reader, threshold 1 (corrected split from "thresholds 1-2" — the H-128 precedent matches threshold 2 only, see §3.1) | OPEN, no matching precedent | worksheet `:165`; `hole_register.yaml:962` |
| Crisis threshold 3 terminal branch | OPEN-CONTENT-JORDAN-ONLY (narrow) | worksheet `:167-168,200` |
| Board rows 12b/12c/12d; worksheet `open:`; stale `:440`/`:324` cites | OPEN-ENGINEERING (hygiene) | plan `:277-279,379`; worksheet `:221-225`; `HANDOFF_IN.md:10` |

*Note on the last row:* the audit explains the stale `:440` cite (see §2.2 and §4.3). **It gives no
detail for `:324`**, so this plan carries `:324` as cited and does not expand it.

### §2.1 · The five-step gate, as the audit ran it

**`../2026-09-18-character-decision-layer/PROPOSAL.md` §9 (`:339-352`):**

1. **Sum / precedence / neither.** **PARTLY SUPERSEDED; the remainder SURVIVES.**
   - **What ED-IN-0261 settles:** the deontological test is a *refusal at `opening_set`*, "one
     mechanism, not two" (worksheet `:215-219`). So the Principle-as-refusal test is gate-then-score,
     not a precedence slot.
   - **What nothing rules:** the other tests. `03_DECISIONS.md:69` leaves §3/§7/§9 NEEDS-STATUS.
   - **What is measured:** PROPOSAL §6 (`:270-283`) measures the precedence band as a no-op today
     (28/28/1; three of six tests fire zero times).
   - **Verdict:** blocks no ruled item. → **escalate, non-blocking** (G-Q5).
2. **Procedure name.** **IRRELEVANT unless Q5 answers "precedence"** (step 2). Folded into Q5.
3. **Moral-basis name.** **SUPERSEDED** by ED-IN-0261: `pursuits`/`pursuit_axes`
   (`in_archive.jsonl:177` "THE BASIS"), landed in #428. Closed.
4. **Third axis set (warrant/facing/purity).** **SUPERSEDED** by ED-IN-0261's seven bipolar axes
   (worksheet `:69-76`).
   - Those seven also supersede STR-2's `memory·substantive·equity·selfish` (`RULINGS.yaml:1093-1097`,
     2026-09-17).
   - Closed. Three surfaces still carry the 09-17 four: plan `:279`, `05_THE_ORDER.md:35`,
     `RULINGS.yaml:1094`.
5. **Affiliation roster + 10 pairs + intensity.** **SURVIVES the content need; the ESCALATION is
   redundant — this plan verified `03_DECISIONS.md:69` directly.**
   - R1/R2 stand (ED-IN-0251 row 2). ED-IN-0261 moves `sacred` there (worksheet `:78-82,213`).
   - The candidates in the old worksheet (`:39-81`) are drawn from canon, but every `keep:`,
     `intensity:` and `incompatible:` cell is `~`.
   - No document, no precedent, and the architecture is silent on content.
   - ⚠ **`03_DECISIONS.md:69` rules PROPOSAL §9 items 5 and 6 "already `ED-IN-0251` R3"** — meaning the
     *escalation itself* is not new, not that the content has arrived. R3 ("the cells are yours") already
     told Jordan this was his to author; G-Q3 is that standing ask made concrete, not a fresh discovery.
     Verified by opening `03_DECISIONS.md:55-69` directly for this correction. → **CONTENT, already owed**
     (G-Q3).
6. **The cells.** **SURVIVES the content need, same correction as item 5.** ED-IN-0261: "downstream of
   the cells, which are Jordan's under STR-6/R3". `03_DECISIONS.md:69` makes the same "already R3" point.
   → **CONTENT, already owed** (G-Q1, Q2).

**The worksheet's `open:` list (`../2026-09-20-pursuit-basis-worksheet.yaml:221-225`):**

- **105 cells + alignment re-cell.** CONTENT, as above.
- **Faith as a pursuit.** **SUPERSEDED the same day** (see §4.1).
- **Crisis reader (the L5 edge), both tracks.**
  - **Thresholds 1 and 2 are ENGINEERING,** answered by precedent (step 4):
    - H-128 (`:958-960`) is the tree's shape for a magnitude with no ruled value: a `Fixtures` arm,
      control `0`, swept.
    - Item 21 fixes the shape "an L5 edge that rewrites an option set and never rolls an outcome"
      (`:962`).
  - **Threshold 3's terminal branch** (restabilise / fold / destroyed) is the one piece the audit
    could not answer from a non-quarantined source → narrow question (G-Q6).
- **H-80.** **The worksheet's item is stale on its stated reason, but the underlying problem is NOT
  closed — reversed from the first draft, see §4.2.**

### §2.2 · Code state behind the table (read, not inferred)

**The 105 cells are NOT populated.**
- `engine/season/rosters.yaml:1422-1513` `tables.pursuit_projection` holds the old 13 rows
  (`Faith`…`Honor`) × the old 4 axes (`hierarchical/sacred/instrumental/traditional`). Per the rename
  note at `:1419-1421`, it is byte-identical.
- `tables.alignment` (`:1515+`) is keyed on the same four: `hierarchical` block `:1567`, `sacred`
  `:1593`.
- Worksheet `set: {}` at `proposals/2026-09-20-pursuit-basis-worksheet.yaml:100-114,157`. All empty.

**The rosters are old.**
- `references/descriptor_registry.yaml:236-252` has `conviction_roster count: 13`; `:279-287` has
  `axis_roster count: 4`.
- There is no `pursuit_roster`, no affiliation roster, and no `incompatible` relation anywhere. A grep
  of `descriptor_registry.yaml` and `engine/season` for `affiliation|incompatib` returns only
  faction-affiliation code and prose.
- `church_standing` is still one unread string, now at `rosters.yaml:387`.

**The chain the content must flow through:**
1. `descriptor_registry.yaml`
2. `tools/export_descriptors.py:115-153` (validates `count`)
3. `engine/engine_params/descriptors.json`
4. `engine/substrate/descriptors.py:194,210` (`CONVICTIONS`, `AXES`)
5. `engine/season/data/rosters.py` (`from_descriptor: conviction_roster`, `rosters.yaml:301`)

**Loader atomicity is real.**
- `engine/season/data/verbs.py:598-632` `_check_sparse_table` raises on an unrostered row or column key
  and on an all-zero table.
- `_load_projection` (`:635-666`) and `_load_alignment` (`:677-694`) run at module scope.
- So R6 holds.

**No precedence.**
- The `Person` fields are `stance` (`engine/season/state/carriers.py:455`), `pursuits` (`:456`) and
  `scar` (`:489`). There is no `precedence` and no `conviction` field.
- `decision/choose.py:365-368` scores `score = Σ axis_w·align + stance_toward + u`, sorts at `:376` and
  samples at `:381`.
- `aggregate_questions` (`decision/questions.py:45`) is still the single global rule.
- There are zero hits for `precedence` under `engine/season/decision/`.

**No deontology gate.**
- `opening_set` is at `decision/options.py:35`. There are zero hits for `deontolog`.
- The only person-side refusal added since is the self-adversary clause at `:117`.

**Scar is still the float model.**
- `loop/effects.py:340-407` `_scar` reads `scar_step` (`:372`) and writes `step × align(verb, axis)`
  per axis (`:394-397`).
- Its only caller is `_eff_kill` (`:497`), which scars the **subject** (`:462-463`).
- It never calls `observers_for`; `loop/witness.py:112` and `harness/probes.py:605-607` both do (the
  audit named only the first; the antagonist pass found the second).
- `observers_for` is at `epistemic.py:491`. The worksheet (`:189`), ED-IN-0261 and `HANDOFF_IN.md:10`
  all cite `:440`, which is stale.

**Verbs.**
- `verb_table.yaml:287-298` `kill / wound` carries `requires_typed: existence/subject/Person` and
  `contests: "the body"`. This is the admission, and it has landed.
- No `fight`, `challenge` or `accept` rows exist (the full `- verb:` listing was checked).
- `resolvable_verbs` is at `loop/driver.py:77`.

**Two owners are missing from the worksheet's OWNERS list (`:11-15`), and they do NOT fail the same
way — an antagonist pass caught this after the audit's own text claimed otherwise.**
- **`role_template_pursuits`** (`rosters.yaml:1352-1417`, header at `:1352`, cells at `:1381-1417` —
  the audit's own `:1400-1417` range was wrong and dropped `sovereign`, `ecclesiastical` and half of
  `mercantile-procedural`) uses `Honor`, `Authority`, `Order` and `Identity`. It is read via
  `data/cast.py:313` → `to_axes`. **This path does NOT raise on an unknown name.**
  `to_axes` (`data/pursuits.py:79-86`) does `row = PURSUIT_PROJECTION.get(conv); if row is None:
  continue` — an unrecognised old name is silently skipped, and `table()` (`data/rosters.py:268-285`)
  does no key validation either. Landing the 15 without migrating this table produces **silent data
  loss** (`cast.loyalty` quietly returns weaker results for any faction whose template still names an
  old pursuit), not an import error.
- **The `convictions:` blocks in `references/npc_registry.yaml`** give 46 key hits; ED-IN-0268 counts
  28 blocks under a different predicate. They are read via `cast.py:203-211` → `pursuit()`
  (`data/pursuits.py:39-56`), which **does** raise `Unspecified` on a non-canonical name.

**Landing 15 new names without migrating these two owners breaks `populated` for the npc_registry half
LOUDLY (an exception) and for the role-template half SILENTLY (no error, wrong numbers).** H6's
deliverable must add an explicit validation step for `role_template_pursuits` — it cannot rely on "the
loader raises," because for this table it does not. See the correction to H6's falsifier in §3.3.

**Tests pinning the old content:**
- `tests/valoria/test_conviction_roster_single_owner.py:50` asserts `len(CONVICTIONS) == 13`.
- `engine/season/tests/test_conviction_spread_solver.py:111` asserts `within_60deg == 9 and total == 13`.

**Instrument:** `engine/season/harness/conviction_spread.py:229-250` accepts `--candidate FILE.json`.

### §2.3 · Motion after the documents

- **Handoff.** `HANDOFF_IN.md:8-11` has four Open rows: cells, verb split, scar rebuild, deontology
  gate. Standing order `:24` says the split rides the re-cell. This matches ED-IN-0261's "Decided and
  buildable" list at `HANDOFF_IN_history.md:4117-4131`.
- **`hole_register.yaml`:**
  - **H-62** (`:715-717`) has the renamed clause added, and still lists `beliefs` among five
    producer-less interior rows.
  - **H-128** (`:952-963`) is the float scar, `sweep: [0,1,10]`, with the actor-vs-subject question
    raised at `:962`.
  - ⚠ **H-80 (`:976-986`) is the operand-channel row** ("a computed act cannot declare its OPERANDS").
    **Correction to the audit's own reading, caught by the antagonist pass and verified directly:**
    `loop/driver.py:118-122,144-145` and ED-IN-0261 both call admitting `kill / wound` "**H-80's item**".
    H-80 is not a wrong-row mis-citation — it is exactly the general problem that gated the admission,
    fixed for `kill / wound` only by a one-off typed `requires` cell rather than by fixing H-80's general
    gap. See the reversed recommendation at §4.2.
- **After 2026-09-24,** only the `Person.beliefs` deletion (`carriers.py:457`, `write_matrix.yaml:385`,
  2026-09-25) touches this lane, so H-62's five is now four. Nothing else moved.
- **The RATIFIED order was relocated.**
  - `workplans/2026-09-11-reconciled-program.md` → `workplans/2026-09-18-governance-settlement-behaviour-plan.md`
    (`references/restructure_ledger.md:529`).
  - Positions `12b` (6a affiliations) and `12c` (6c "onto memory · substantive · equity · selfish")
    at `:278-279` are **JORDAN**-gated.
  - `:379` maps 6b→`12d` as JORDAN-gated. **This is a board defect, and it is only PARTLY closed by
    #428** — see the correction to H1 at §3.2: ED-IN-0268 itself says the season-side rename is done
    but the registry/substrate rename (the "real" `pursuit_roster`) is deferred to H6, so `12d` should
    read PARTIALLY DONE, not DONE.
  - `:382` (row `6g`, "H-71's SECOND half … Open") is also stale: ED-IN-0267 closed it. The first draft
    of this plan did not catch this row; the antagonist pass did.
  - 12c's axis text is stale against ED-IN-0261's seven. `05_THE_ORDER.md:35` carries the same stale
    four. **Two more stale-axis surfaces the audit did not name:** `engine/season/state/carriers.py:480`
    (a comment on the live `scar` field H3 rewrites — game code, not just prose) and
    `hole_register.yaml:962`, plus `proposals/2026-09-17-governance-and-behaviour/01_THE_BUILD_ORDER.md:984,1041`.
    `RULINGS.yaml:1094` is left uncorrected deliberately — it is a historical ledger record of what was
    ruled when, and this plan does not direct an edit to it, on the same convention that keeps
    `registers/`'s superseded rows unrewritten.
- **`CURRENT.md`:** `:25` names the 2026-09-20 worksheet as the head, and `:31` is flipped.

---

## §3 · The handshake plan

**Corrections to PROPOSAL §7's nine steps:**
- **Steps 3 (excluders) and 4 (`Person.precedence`)** are held behind Q5.
- **Step 8 is "R1's affiliation roster + `incompatible`"** (`../2026-09-18-character-decision-layer/PROPOSAL.md:308`),
  which maps to **H10**, not H11. **Correction to the first draft:** the audit's own wording, "C3/E6
  below," defined no "E6," and the first draft guessed H11 without checking step 8's actual text. H10
  is the affiliation-roster deliverable; H11 (convictions-track scars) is downstream of H10, not the
  same thing as it.
- **Step 9 (Obligation/Threat)** stays behind the aperture work and is out of this lane.

**Numbering:** the audit's handshakes run H1, H2, H3, then H6 to H13. **There is no H4 or H5.** This
plan invents neither and keeps the audit's numbers so its citations stay stable. **H6 and H8 are now
one commit** (§3.1's correction), so "H8" survives only as a label for one part of H6's deliverable,
not as a separate handshake with its own timing.

### §3.1 · The dependency graph, in prose

**Two corrections here reverse claims in the first draft of this plan; both came from the antagonist
pass verifying against the working tree rather than trusting the shape of the audit's own prose.**

- **Can start today with zero content:** H1 and H2 only. **Both are BUILT (2026-09-27)** — see the
  status block at the end of this section.
  - **H1** landed as described below.
  - **H2** builds a roster-generic mechanism, and this section's own second draft got its inertness
    claim wrong the same way the first draft got H3's wrong. ⚠ **CORRECTED, by a `layer-conformance`
    attack that checked the claim against the tree instead of reasoning about axis names:**
    `references/descriptor_registry.yaml:286` already carries `instrumental` with the identical
    `deontological/instrumental` sign convention this gate hardcodes, so `refusal_axis="instrumental"`
    WOULD arm the gate against the CURRENT 13-pursuit tables — "cannot fire even by accident" was
    false. It ships with `refusal_axis` unset because arming it now is an unruled design choice, not
    because no usable name exists. See `hole_register.yaml` H-146's `default:` field for the full
    correction.
- **H3 is NOT inert, and the first draft's claim that it was is wrong.** `_scar`'s replacement reads the
  **already-populated** old tables — 52 projection cells (`rosters.yaml:1449-1513`) and 52 alignment
  cells, 17 negative (`effects.py:389`) — and `scar_step` is already the shipped control at `0`
  (`fixtures.py:533`, per H-128). So H3 changes RESOLVE-time behaviour **the moment it lands**, against
  content that is about to be replaced, with no control arm of its own and no golden re-pin note, and it
  does not name the `test_lb6e_*` tests (`hole_register.yaml:962`) it is likely to break or retire.
  **H3 is moved out of "now" and made dependent on H6**, matching what `HANDOFF_IN.md:10` already
  ordered ("scar rebuild after the ALIGNMENT re-cell lands") — the first draft's claim that it agreed
  with the handoff while scheduling the opposite order is also corrected here, not just relocated.
- **Hard-blocked on C1 + C2 (G-Q1, G-Q2):** H6.
  - C1 and C2 must arrive together, because `cast.py:203-211` validates names at read. Landing the 15
    names without the character and template migration breaks `populated` — loudly for the
    `npc_registry.yaml` half, silently for `role_template_pursuits` (§2.2's correction).
- **H6 and H8 are NOT sequential — they must be ONE commit, and the first draft's graph was wrong to
  show H8 downstream of H6 with its own separate falsifier.** Verified against
  `engine/season/data/verbs.py:685-692`: `_load_alignment`'s `_check_sparse_table` raises on any verb
  key not in `VERB_TABLE`, so C1's cells for `kill`, `wound`, `fight`, `challenge` and `accept` cannot
  land (H6) before those five rows exist in `verb_table.yaml` (H8) — and H8 cannot retire the combined
  `kill / wound` row while `alignment` still holds its `sacred` cell (worksheet `:81`) without H6's
  landing removing that cell in the same breath. **H6's deliverable list in §3.3 now includes the verb
  split; H8 is folded into it as one atomic commit,** and a separate H8 falsifier is kept only as the
  verb-count check on that same commit.
- **Downstream of the merged H6+H8 commit:** H7, H3 (now that its precondition is real), and H9.
- **H9's threshold-1 half rests on a shakier precedent than threshold 2's.** The audit matched threshold
  1 to item 21's L4 amendment's shape by the word "crisis reader," but item 21's own shape (an L5 edge
  that rewrites an option set, `hole_register.yaml:962`) is **threshold 3's** mechanism (`crisis`), not
  threshold 1's ("decision forks increase when salient," worksheet `:165`) — a different, unspecified
  mechanism. Threshold 2 ("weight shifts down… as a swept `Fixtures` arm") still matches H-128 cleanly.
  **H9 is narrowed to threshold 2 only; threshold 1 is held alongside H13 rather than classified
  ENGINEERING on a precedent match that does not hold.**
- **Hard-blocked on C3 (G-Q3):** H10.
- **H11** needs **H3 + H10 + C4 (G-Q4)**.
- **Held on a design question, not on content:**
  - **H12** is held on G-Q5, and only if the answer is "precedence".
  - **H13** is held on G-Q6, and now also carries H9's dropped threshold-1 mechanism.

```
now:        H1        H2 ─┐
                          │
C1 + C2 ──► H6+H8 (one atomic commit: registry, rosters, descriptors, verb split) ──► (H2 becomes live)
             ├──► H7
             ├──► H3 (moved here from "now" — see the correction above)
             └──► H9 (threshold 2 only)
C3 ──► H10 ──┐
C4 ──────────┴──────────────► H11 (needs H3 too)
G-Q5 = "precedence" ──► H12          G-Q6 ──► H13 (+ H9's threshold-1 mechanism)
```

**Fields per handshake:**
- **Pre:** the precondition.
- **Deliverable:** what lands.
- **Falsifier:** the observation that would show the deliverable wrong.
- **Owner type:** ENGINEERING (a session) or CONTENT (Jordan).

Where the audit gave no falsifier for an item, the entry says *not specified by the audit*. None has
been supplied here.

### §3.2 · Now: no content needed — BOTH BUILT, 2026-09-27

**Status.** H1 and H2 were built by an Opus producer, passed through `/code-review` (clean),
`/simplify` (two real fixes applied: a triplicated test-setup block factored into `_h2_base()`; a
dormant double-computation of `project(p)` per DECIDE call, and a per-verb re-import, both hoisted —
the double-`project(p)` thread was NOT fixed, since threading it through `opening_set`'s signature
would touch a dozen call sites across `test_season_shape.py`, `probes.py` and `corpus_run.py` and is
`architecture/meta/04_CODE_ARCHITECTURE.md:133`'s own documented signature, so it is deferred rather
than widened into — and `layer-conformance` (Lens A clean; Lens B found the same H2-inertness error
this section's own first correction made above, plus a CONVENTION-grade note on the hardcoded sign
pole, both now recorded at `hole_register.yaml` H-146, and ran the actual plant-a-violation falsifier
the skill requires rather than trusting a static read of the AX-2 scan). Tests: the new `test_h2_*`
suite (4), the full `test_governance_build.py` (29), `test_choose_receives_no_world`, and — the
correct AX-2 falsifier for THIS code, per the layer-conformance attack — `test_decision_package_never_names_world_anywhere_under_it`
(`test_season_shape.py:2781`) all green. `register --check` rows R2(6)/G6(15) confirmed identical
before and after (`git stash` control). Full detail in `hole_register.yaml` H-146 and the working
tree; this plan is not re-narrating a completed build, only marking it done.

**H1 · Record hygiene.** *Owner type: ENGINEERING. DONE.*
- **Pre:** none.
- **Deliverable:**
  - plan `:379`: 12d→**PARTIALLY DONE**, not DONE — ED-IN-0268 explicitly defers the registry/substrate
    rename (`conviction_roster`→`pursuit_roster`, `descriptors.CONVICTIONS`, the `npc_registry.yaml`
    key) to a later step, which is H6's job; only the season-side field rename is finished
  - plan `:382` (row `6g`, "H-71's second half … Open"): →DONE, citing ED-IN-0267 — missed by the first
    draft, caught by the antagonist pass
  - plan `:279` and `05_THE_ORDER.md:35`: replace the axis text with ED-IN-0261's seven
  - `carriers.py:480`, `hole_register.yaml:962`, `01_THE_BUILD_ORDER.md:984,1041`: same stale-axis
    correction (added by the antagonist pass; `RULINGS.yaml:1094` is deliberately left alone, see §2.3)
  - worksheet `open:`: drop the `faith` item (§4.1); **narrow, not drop, the `H-80` item** (§4.2 — the
    recommendation reversed)
  - `HANDOFF_IN.md:10` and worksheet `:189`: correct the cites to `effects.py:340` and `epistemic.py:491`
  - H-62: drop `beliefs`
- **Falsifier:** `tools/validate_ed_citations.py` is green, and each edited line is re-opened. ⚠ This
  falsifier cannot catch a wrong line NUMBER that still parses as a citation (`CLAUDE.md` §0.1 pt 2) —
  re-opening each line by hand is the actual check, not the tool.
- **Ledger:** no ledger row is needed.

**H2 · Deontology gate, roster-generic.** *Owner type: ENGINEERING. DONE. Ships shipped-inert
(`refusal_axis=None`), but — corrected above — NOT because it is incapable of firing on the current
tables.*
- **Pre:** none.
- **Deliverable:** a clause in `opening_set` (`decision/options.py::refusal_tolerance`/`refuses`):
  - It reads a rostered axis name from `Fixtures` and the person's projected weight on that axis. The
    weight is the threshold (ED-IN-0261), so there is no new number.
  - It refuses a Candidate whose `align(verb, axis)` exceeds tolerance.
  - The control arm is the axis left unset.
- **Falsifier:**
  - Four `test_h2_*` tests inject a synthetic projection/alignment by rebinding `decision.choose.ALIGNMENT`
    and `data.verbs.PURSUIT_PROJECTION` directly (the same tables the `H-66` sweep rebinds) — not
    `alignment_at`, which does not exist under this name; the rebind target was confirmed by opening
    `choose.py` and `data/verbs.py` rather than assumed from this plan's own citation.
  - They assert the Candidate never forms and that `score` is unchanged for survivors, observed through
    a spy on `_sample_order`.
  - ⚠ **CORRECTED: the AX-2 falsifier this row named was wrong.** `test_choose_receives_no_world`
    (`test_season_shape.py:829`) inspects only `inspect.getsource(SeasonDriver.deliberate)` for two call
    strings and cannot see anything inside `options.py`. The falsifier that actually covers this code —
    found by the `layer-conformance` attack, then independently confirmed by planting a real `World`
    import inside `refusal_tolerance` and watching it fail, then reverting — is
    `test_decision_package_never_names_world_anywhere_under_it` (`test_season_shape.py:2781`), an
    `ast.walk` over every file `DECISION_DIR.rglob("*.py")` returns, including late imports inside
    function bodies.
- **Records:** the sign convention. `deontological` is the NEG pole (worksheet `:76`) — hardcoded as
  `>` in `refuses`, not read from roster data; flagged CONVENTION-grade at H-146 for `H6` to address
  when the poles become data, not guarded now (no code path can fail on it while the axis ships unset).

### §3.3 · Blocked on Jordan: C1 + C2

**C1 · Cells.** *Owner type: CONTENT (Jordan). Question: G-Q1.*
- **Pre:** none.
- **Deliverable:** the 105 `set:` cells (worksheet `:100-114`) and `alignment.set` (`:157`).
- **Falsifier:** *not specified by the audit.* H7 is the downstream check on placement.

**C2 · Character/template migration.** *Owner type: CONTENT (Jordan). Question: G-Q2.*
- **Pre:** none.
- **Deliverable:** re-authored weights on the 15 for the `npc_registry.yaml` `convictions:` blocks and
  for `rosters.yaml:1352-1417` `role_template_pursuits`, or a rule for deriving them.
- **Falsifier:** *not specified by the audit.* H6's import is the load-time check.
- **Constraint:** C1 and C2 must arrive together, because `cast.py:203-211` validates names at read.

**H6 · The landing commit — now merged with the verb split (H8), per the corrected dependency graph
in §3.1.** *Owner type: ENGINEERING. R6-atomic, and now atomic across two tables that used to be
scheduled separately.*
- **Pre:** C1 and C2 values in hand, including alignment cells for `kill`, `wound`, `fight`,
  `challenge` and `accept` — C1's deliverable already covers this; §3.3's C1 entry is unchanged.
- **Deliverable, in one commit:**
  - `descriptor_registry.yaml`: `conviction_roster`→`pursuit_roster` (15) and `axis_roster` (7), each
    with `count`
  - `tools/export_descriptors.py` + `--check`
  - the names in `engine/substrate/descriptors.py:194,210` and `data/pursuits.py`
  - `rosters.yaml`: `pursuit_projection`, `alignment`, `role_template_pursuits`
  - `npc_registry.yaml` values
  - `names_index.yaml` entries
  - **the verb split** (formerly H8): retire the combined `kill / wound` row; add `fight` with
    `requires_typed existence/subject/Person` (the `kill / wound` clause, `verb_table.yaml:293-296`);
    add `challenge`→`accept`, with `accept` carrying `contests: "the body"` — in this same commit,
    because `_load_alignment` (`verbs.py:685-692`) raises on any alignment key not already in
    `VERB_TABLE`, and the old row's `sacred` cell (worksheet `:81`) cannot be retired while `alignment`
    still names it
  - **an explicit validation step for `role_template_pursuits`**, added by the antagonist pass: this
    table's read path (`to_axes`, `pursuits.py:79-86`) does not raise on an unrecognised name (§2.2), so
    H6 must add its own check — the loader's silence is not a substitute
  - **an audit of `systems/world/sim/npe.py:102,284,287,332` and `systems/characters/sim/conviction.py:59,205`**,
    both direct readers of `descriptors.CONVICTIONS` (`test_conviction_roster_single_owner.py:52-55`
    pins that they share the object with the season-side roster) — added by the antagonist pass,
    because the single-owner design propagates the NEW names to these call sites automatically, but
    does not by itself guarantee their own logic isn't keyed to specific OLD names
  - re-pin `test_conviction_roster_single_owner.py:50` (15)
  - re-pin `test_conviction_spread_solver.py:111` (new `within_60deg`), recorded as a re-pin per
    `CLAUDE.md` §7
- **Falsifier:**
  - The import itself: the loaders raise on a partial landing of the roster/projection/alignment
    tables — **but this covers `npc_registry.yaml` and `verb_table.yaml`, not
    `role_template_pursuits`,** which needs the added validation step above to fail loudly at all.
  - `resolvable_verbs()` count check on the merged commit (see the corrected arithmetic below, in place
    of the first draft's unsourced "19→22").
  - `python -m engine.season.harness.conviction_spread` reports PR and `within_60deg`.
  - The headless content hash moves, and the move is recorded.
  - The three-arm corpus readout ED-IN-0261 used (baseline / fold-fixes / both) is re-run.

  **Corrected verb-count arithmetic** (the first draft's "19→22" appeared nowhere in the tree and did
  not derive from anything): `resolvable_verbs()` is 19 today. The split removes 1 combined row and
  adds `kill`, `wound`, `fight`, `challenge`, `accept` — arithmetically 19 − 1 + 5 = **23**, or **22** if
  `challenge` is a declare-only verb that `resolvable_verbs()` does not itself count (only `accept`
  carries `contests: "the body"`). **Which of the two is right is H6's own job to confirm against
  `loop/driver.py:77`'s actual definition, not a figure to assert in advance.**

**H7 · Faith-pair falsifier.** *Owner type: ENGINEERING.*
- **Pre:** H6.
- **Deliverable:** a test that constructs the devout-Solmund builder and the Einhir dismantler (both
  high `faith`) and asserts their projected vectors sit outside ED-IN-0214's 60° bar (`cos ≤ 0.5`).
  ⚠ **This pair is not invented by the test-writer.** It is Jordan's own worked example, verbatim, at
  worksheet `:120-122`: *"someone who is a devout church of Solmund follower [who wants] to do work for
  the church, or someone who is pure Einhir and anti Solmund church whose faith work is about
  dismantling it."* Building the test still needs concrete numeric placement of these two specific
  people on the new grid, which is content — **C2 should say explicitly whether it includes placing
  this pair, or H7 has no fixture to build from.** This gap is not covered by G-Q1–Q6 as written; see
  the note added to Q2 in §5.
- **Falsifier:** the test is its own falsifier. **If it goes red, the placement is wrong, and the fix
  goes back to C1, not to the code.**

**H3 · Scar count mechanism, pursuits track, roster-generic.** *Owner type: ENGINEERING. Moved here
from "now" — see the correction in §3.1. Live only once H6+H8 has landed.*
- **Pre:** H6+H8 (not "none" — the first draft's claim that this needed no precondition was wrong).
- **Deliverable:**
  - `Person.scar` becomes `{element: count}`.
  - `_scar` is retired along with `scar_step`.
  - At RESOLVE, the act calls `observers_for(w, e, mode, everyone)` (`epistemic.py:491`) and increments
    one count per observer per violated pursuit.
- **The violation predicate — recorded as an assumption for review at build time, NOT as a ruling this
  plan is making:**
  - It is composed on the two single-owned tables: per-row `Σ_axis projection[p][axis]·align(verb,axis) < 0`.
    This is a sign test with no free number, but ED-IN-0261 itself says only "whose pursuits or
    convictions that act violated" and does not define violation — this formula is this plan's own
    candidate reading, not something ED-IN-0261 states.
  - H-128's actor-vs-subject question is resolved by "observers, per ED-IN-0261".
  - Whether the actor counts as an observer is recorded as a swept arm.
- **Falsifier:**
  - A seeded 2-season run with `fan_out_mode` as the control axis (ED-IN-0267's pattern) asserts that
    counts differ between `presence_only` and `all_five`.
  - The 2,403-fork reconvergence figure (worksheet `:170`) is re-measured before and after.
  - **Because H3 now lands only after the new content is live, it needs no separate control arm
    against the OLD table** — the "not inert" hazard the antagonist pass found is closed by the
    resequencing itself, not by adding a flag.

**H9 · Crisis reader, threshold 2 only.** *Owner type: ENGINEERING. Narrowed from "thresholds 1-2" —
see §3.1's correction.*
- **Pre:** H3 and H6+H8.
- **Deliverable:** at threshold 2, the weight shift as a `Fixtures` arm with control `0` and a sweep
  (the H-128 shape).
- **Falsifier:** fork divergence at the `total` arm rises above the 7→8/31 baseline (ED-IN-0261) while
  the control arm stays unmoved.
- **Threshold 1 is NOT here.** The audit matched it to item 21's L4 shape by the phrase "crisis reader,"
  but that shape (an L5 edge rewriting an option set) is threshold 3's mechanism; threshold 1's own
  design text ("decision forks increase when salient," worksheet `:165`) has no matching precedent in
  the tree. It moves to H13, alongside threshold 3.

### §3.4 · Blocked on Jordan: C3, C4

**C3 · Affiliations.** *Owner type: CONTENT (Jordan). Question: G-Q3.*
- **Pre:** none.
- **Deliverable:** for the candidates in `../2026-09-18-conviction-basis-worksheet.yaml:39-81`, the
  `keep:`/strike choices, the ten `incompatible:` cells, and `intensity.scale`, `player_sees` and
  `bands`.
- **Falsifier:** *not specified by the audit.* H10's falsifier is the downstream check.

**C4 · Verb × affiliation engagement.** *Owner type: CONTENT (Jordan). Question: G-Q4.*
- **Pre:** none.
- **Deliverable:** what act violates which affiliation. No such table exists today; `alignment` is
  verb × moral-axis only (`rosters.yaml:1526`).
- **Falsifier:** *not specified by the audit.*

**H10 · Affiliation plumbing.** *Owner type: ENGINEERING.*
- **Pre:** C3.
- **Deliverable:**
  - an `affiliation_roster` block, with exporter validation and a substrate leaf
  - `Person.conviction: dict`
  - an `incompatible` half-matrix table in `rosters.yaml`, with a loader that refuses an unrostered
    pair
  - `confliction(p)` as a derived query, never stored (R1)
  - a `write_matrix.yaml` row
- **Falsifier:** a person holding two incompatible affiliations at full intensity loads, and
  `confliction` is non-zero. This is `05_THE_ORDER.md:34`'s own falsifier.

**H11 · Scar count, convictions track.** *Owner type: ENGINEERING.*
- **Pre:** H3, H10 and C4.
- **Deliverable:** the same mechanism as H3, over the affiliation table.
- **Falsifier:** *not specified by the audit beyond "same mechanism as H3".* H3's falsifier shape is
  the nearest analogue, and it is not asserted here.

### §3.5 · Held

**H12 · `Person.precedence` / excluders / loop-to-order** (PROPOSAL §7 steps 3-6). *Owner type:
ENGINEERING, behind a design question.*
- **Pre:** G-Q5 answered "precedence". **Do not build before.**
- **Deliverable and falsifier:** *not specified by the audit.* The model file's §8 ("The precedence is
  decoration if…") is the existing falsifier for the idea.

**H13 · Crisis threshold 3, plus threshold 1's mechanism (moved here from H9, §3.3's correction).**
*Owner type: ENGINEERING, behind a narrow content question for threshold 3, and behind an unresolved
mechanism for threshold 1.*
- **Pre:** G-Q6 for threshold 3. Threshold 1 has no ruled mechanism at all — worksheet `:165`'s
  "decision forks increase when salient" is not specified as engineering, and this plan does not
  invent one; it stays open rather than being assigned a precedent that does not fit.
- **Deliverable and falsifier:** *not specified by the audit, and not supplied here for either half.*

---

## §4 · Worksheet corrections

Target: `proposals/2026-09-20-pursuit-basis-worksheet.yaml`. **These are edits the next session should
actually make** (they are part of H1). They are not observations to leave in place. The `open:` list is
at `:221-225`, and its four items sit at `:222-225` in order:

| line | item as written | correction |
|---|---|---|
| `:222` | "the 105 projection cells and the alignment re-cell   # yours" | **keep**: still CONTENT (G-Q1) |
| `:223` | "faith as a pursuit, now that religion has its own vector" | **drop**: see §4.1 |
| `:224` | "the crisis reader (the L5 edge) for both tracks" | **keep, narrowed**: threshold 2 only is ENGINEERING (H9); threshold 1's mechanism and threshold 3's terminal branch are both open (H13, G-Q6) — narrower than the first draft of this plan claimed |
| `:225` | "H-80 is refused by the kill / wound ruling and should be closed rather than left planning the opposite" | **narrow, don't drop**: see §4.2 — reversed from the first draft |

*(The line numbers `:222-225` were confirmed by opening the file for this plan. The audit cites the
range `:221-225` and the H-80 item at `:225`.)*

### §4.1 · Faith: stale against the worksheet's own §3

The worksheet's §3 already records "faith KEEPS ITS ROW — RULED 2026-09-20" (worksheet `:116-122`), and
ED-IN-0261 records it as "AMENDED SAME DAY". **The item was ruled the same day it was raised, so the
`open:` list is stale against the worksheet itself.** Drop it.

### §4.2 · H-80: the worksheet's item is stale, but this plan's first draft got the reason wrong

**Reversed from the first draft, on the antagonist pass's finding.** The first draft claimed the
worksheet's item "names the wrong row" — that H-80 (`hole_register.yaml:976-986`, "a computed act
cannot declare its OPERANDS") has nothing to do with the kill/wound admission. That claim does not
survive opening `loop/driver.py:118-122,144-145`, which calls admitting the verb "**H-80's item**," and
ED-IN-0261 itself, which calls H-80 "filed to ADMIT kill/wound." **H-80 is exactly the general problem
that gated the admission.**

What actually happened: the specific `kill / wound` instance was unblocked by a one-off typed `requires`
cell (`verb_table.yaml:292-298`), not by fixing H-80's general gap — a computed act still cannot
declare its own operands in general. **H8's own new verb rows (`fight`, `challenge`, `accept`) will
need the same per-verb workaround again unless H-80's general fix lands first**, which H6's merged
deliverable does not attempt.

**So: the worksheet's item is stale on its stated PREMISE** (the refusal it names was withdrawn, and
kill/wound is admitted) **but not on its SUBJECT** (H-80's general operand-channel gap is real and
still open, and H8 is about to hit it again). Narrow the worksheet's `open:` entry to say this, rather
than dropping it outright.

### §4.3 · A stale citation in the same file

Worksheet `:189` cites `observers_for` at `epistemic.py:440`. It is at `epistemic.py:491`. The same
stale `:440` appears in ED-IN-0261 and `HANDOFF_IN.md:10`. H1 corrects the worksheet and the handoff.
**The ED-IN-0261 row is a ledger record, and this plan does not direct an edit to it.**

### §4.4 · An omission in the same file, and the two omitted owners fail differently

The worksheet's OWNERS list (`:11-15`) omits two owners that read the pursuit names:
- `rosters.yaml:1352-1417` `role_template_pursuits` (corrected range — see §2.2). **Does not raise** on
  an unrecognised name; a partial migration here fails silently.
- the `references/npc_registry.yaml` `convictions:` blocks. **Does raise** (`Unspecified`), via
  `pursuit()`.

See §2.2 for the full correction. **H6 must migrate both, and must add its own explicit check for the
first, because that table's own loader will not catch a mistake for it.** Adding both to OWNERS, with
this asymmetry noted, is the corresponding worksheet edit.

---

## §5 · Questions for Jordan

Verbatim from the audit. **No recommendation is attached, and this plan answers none of them.**

1. **The cells.** Please fill `set:` for the 105 cells at `proposals/2026-09-20-pursuit-basis-worksheet.yaml:100-114` and `alignment.set` at `:157` over the verbs (38 − `kill / wound` + `kill`, `wound`, `fight`, `challenge`, `accept` = **42**, corrected from the audit's "40," which did not add up). Do `speak` and `tell` get cells this time (they carry none today, so the moral layer is silent on testimony)? *Also needed for H7 to run at all: concrete numbers for your own worked pair — the devout-Solmund builder and the Einhir dismantler (worksheet `:120-122`) — so their placement can be checked against the 60° separation bar.*
2. **The people.** `references/npc_registry.yaml`'s `convictions:` blocks and `rosters.yaml:1352-1417`'s `role_template_pursuits` still use the old thirteen. Of the old rows with no successor name, **four** are true orphans — `Utility`, `Equity`, `Identity`, `Precedent` (corrected from the audit's "six": the worksheet itself, at `:30,40`, already resolves `Authority` and `Order` into `stability`). Re-author each character's and each faction template's weights on the fifteen, or give a rule for deriving them.
3. **Affiliations.** In `proposals/2026-09-18-conviction-basis-worksheet.yaml:39-81`: keep or strike each of `solmund_orthodoxy`, `inner_tradition`, `threadwork`, `einhir_revival`, `altonian_theocracy` (add any missing); fill the ten `incompatible:` cells (your worked pair `solmund_orthodoxy + threadwork` reads `true` unless you say otherwise); set `intensity.scale`, `player_sees`, `bands`.
4. **Religious violation.** Scars on the conviction track need "which act violates which affiliation." No such table exists — `alignment` is verb × moral-axis only. Is this a verb × affiliation table you author, or should it derive from something already ruled?
5. **Sum, precedence, or neither** (PROPOSAL.md §9.1). The deontological refusal is now a gate at `opening_set`, and everything else still ranks by the score. Do you want a per-person ordered tuple of tests at all? If yes, what is it called (`docket` is taken)? If no, PROPOSAL §7 steps 3-6 are dropped.
6. **Crisis at threshold 3.** The design lists restabilise / fold into another element / destroyed by incoherence. Is that the engine's choice per case (and by what), or one fixed outcome?

---

## §6 · What would show this plan wrong

- **§2's "105 cells: NOT populated" fails** if `engine/season/rosters.yaml:1422-1513` holds anything
  other than the old 13 × 4, or if worksheet `:100-114,157` holds a non-empty `set:`.
  - Re-open both before starting H6.
  - If the cells have landed, C1 is done and §3.3 moves up.
- **§3.1's "H2 needs no content" fails** if it needs a number that is not already ruled. H2's threshold
  is the person's projected weight (ED-IN-0261). If the build finds a free magnitude, it becomes a swept
  `Fixtures` arm with control `0` (the H-128 shape); if that is impossible, the handshake moves behind a
  content question.
- **H3's move to "after H6+H8" fails** if `Person.scar`'s replacement can be built and tested without
  touching the live projection/alignment tables at all (e.g. entirely behind a feature flag with its own
  fixture data). If so, H3 could return to "now" — but it would then need the control arm and golden
  re-pin note this plan's correction says it currently lacks, not the "no precondition" framing the
  first draft gave it.
- **The merged H6+H8 fails** if `_load_alignment` (`verbs.py:685-692`) turns out NOT to validate its
  verb keys against `VERB_TABLE`, or if the old `kill / wound` row's `alignment` cell can be retired
  without touching the same commit. Re-open `verbs.py:685-692` before assuming the merge is still
  needed.
- **§3.3's "C1 and C2 must arrive together" fails** if `cast.py:203-211` and `data/pursuits.py:39-56`
  do *not* raise on an old name once the 15 land, or if `to_axes` (`pursuits.py:79-86`) is found to raise
  after all. The falsifier is H6's own import **for the `npc_registry.yaml` half only** — for
  `role_template_pursuits`, the falsifier is whatever explicit check H6 adds, since the loader itself
  stays silent on a partial landing (§2.2's correction).
- **§2.2's "two omitted owners fail differently" claim fails** if a fresh read of `pursuits.py:79-86`
  and `rosters.py:268-285` finds validation that this plan missed. Re-open both before relying on the
  claim that `role_template_pursuits` fails silently.
- **H7 is designed to fail loudly.** A red H7 means the cells misplace `faith`, and it routes back to
  C1, never to a code fix — provided C2 actually supplies the worked pair's placement (Q2's added note);
  otherwise H7 cannot be built at all.
- **H9's narrowing to threshold 2 fails** if a closer reading of `hole_register.yaml:962` shows the L5
  edge is not specific to threshold 3 after all, in which case threshold 1 could return to H9. Re-open
  `:958-963` in full, not just the `:962` line this plan cited, before reversing the narrowing.
- **§1.2's under-report finding fails** only if some other ledger row, outside the five read, already
  carries `needs_jordan: true` for any of these items.
  - The audit read ED-IN-0251, 0252, 0261, 0267 and 0268 and no other rows.
  - A grep of every `registers/editorial_ledger*.jsonl` for `"needs_jordan": true` together with these
    subjects would show it.
- **§3's H6 falsifier is not a balance claim.** A moved content hash and a re-pinned `within_60deg` are
  golden re-records, and they must be said plainly as such (`CLAUDE.md` §7). They say nothing about
  whether the new content plays better.

**Not claimed:**
- that the handshake order is the only valid order
- that G-Q1 to G-Q6 are the complete set of Jordan's open questions for this lane (H7's fixture-data
  gap, folded into Q2's note rather than given its own number, is one place this plan chose not to mint
  a seventh question)
- that ED-IN-0251 row 2's field or its text is the correct one (§1.1)
- that this plan's own sixteen corrections are exhaustive — the antagonist pass spot-checked citations
  and hunted fabrication; it did not re-derive every figure in the document from scratch

---

## §7 · Coverage note

**The audit read:**
- all five ledger rows
- the two worksheets
- PROPOSAL §1, §3 and §5-§9
- gather 03 §1-§3 and §5
- 05 §2-§3
- plan `:277-279,379,382` *(corrected — the first draft of this coverage note cited `:383`, which is
  not where either the 12d or 6g board rows sit)*
- RULINGS STR-2
- build-order §7.5
- `rosters.yaml` roster rows and both tables
- `descriptor_registry.yaml:230-299`
- `choose.py:352-381`
- `options.py` (grep)
- `effects.py:340-500`
- `epistemic.py` (grep)
- `verbs.py:598-700`
- `pursuits.py`
- `cast.py:182-211,308-318`
- `verb_table.yaml:287-298` plus the row list
- `driver.py` (grep)
- `carriers.py` (grep)
- `conviction_spread.py:1-60,229-250`
- `HANDOFF_IN.md` in full
- history `:4095-4144`
- hole_register H-62, H-80 and H-128
- `CURRENT.md` rows 25 and 31
- a date sweep of everything after 09-24

**The audit deliberately did not read** the quarantined `conviction_track_v1.md`, per `CLAUDE.md` §1:
`.designs/` is not authority and not a session's input. Q6 may be answerable from it by Jordan's own
reading, not by a session's.

**Beyond the audit, this plan's author (the producer stage):**
- opened the header and §8 of `../2026-09-18-character-decision-layer/PROPOSAL.md` for the format
  convention
- opened `../2026-09-20-pursuit-basis-worksheet.yaml:219-226` to confirm the `open:` item lines in §4

**An independent antagonist pass then opened, and confirmed correct or corrected:** both worksheets in
full; `03_DECISIONS.md:55-69` (found the item-5/6 framing correction, §2.1); `rosters.yaml:1345-1526`
(found the `role_template_pursuits` range error and its validation gap, §2.2); `descriptor_registry.yaml:236-287`;
`decision/choose.py`, `options.py`, `effects.py:340-500`, `epistemic.py:192,491`, `carriers.py:455-489`
(all confirmed as cited); `editorial_ledger_in_archive.jsonl:167-177` and `editorial_ledger_in.jsonl:19-21`
(confirmed the field/text disagreement is real, §1.1); `verbs.py:598-694` (found the H6/H8 circular
dependency, §3.1); `driver.py:77-145` (found the H-80 reversal, §4.2); `pursuits.py:79-86`,
`rosters.py:268-285` (found the silent-vs-loud validation asymmetry, §2.2); `verb_table.yaml:287-298`
and the full row list; `hole_register.yaml:952-986` (found the threshold-1/3 conflation, §3.1);
`witness.py:112` and `probes.py:605-607`; `systems/world/sim/npe.py` and
`systems/characters/sim/conviction.py` (found the missing consumers, §3.3); `01_THE_BUILD_ORDER.md:308,984,1041`;
`test_conviction_roster_single_owner.py:50-55`. This plan's own §1–§7 were rewritten against every
finding that survived (sixteen were reported; this plan's own review, above, found thirteen of them
correct as reported, two correct but requiring nuance rather than a flat reversal — §2.1's items 5/6,
§4.2's H-80 — and treated all sixteen as requiring some edit).

**Not independently re-verified by either pass:** the audit's remaining line citations beyond those
listed above; the figures it quotes from elsewhere (28/28/1, 2,403, 7→8/31, 46 vs 28) — the "19→22"
figure specifically WAS checked, found unsourced, and replaced with a derivation at §3.3.

Each carries its source citation. Per `CLAUDE.md` §0.1 pt 3, **open the cited line before acting on
it.**
