# The repository armature — a structural snapshot of Valoria at `ecacb57`

## Status: REFERENCE SNAPSHOT (2026-09-28). NOT RATIFIED, NOT PROPOSED, NOT A PLAN. It ratifies nothing and asks for no decision; a merge carrying it ratifies nothing under ED-1094, because it contains no PROPOSED content to ratify. It is a map of the tree as it stood at one commit.
## Lane: `IN` (cross-cutting). It allocates no id and carries no ED/PP citation of its own; every ED, PP and H number below is cited from the material it maps.
## Produced by: a Fable → Opus relay (`CLAUDE.md` §10), the same division as `workplans/2026-09-18-governance-settlement-behaviour-plan.md:29-34`. A read-only **Fable 5.1** node reconciled the recent planning surface against the code and drew the structural skeleton, reading the files it cites; this write-up is **Opus's**, from that pass. Working tree at **HEAD `ecacb57`** (`[design] mc_v18-retirement M0-M3: faction_q, mass-battle season provider (#436)`), 2026-09-28. The author spot-checked a sample of citations against the tree (`carriers.py:644` `upkeep`; `seam/wrappers/mass_battle.py:132` `terrain=None`; `massbattle.py:344` `resolve_field`; 82 `.py` under `engine/season/`; MB `next_free: 76`) and did not re-derive the rest.
## Supersedes: nothing. It is new, standalone reference material, and it does not change what `CURRENT.md` names as current.
## Grade under CLAUDE.md §0.2: `paper` throughout — a reference map, not an execution artifact. Nothing in it shows that anything runs; where it says a thing runs, it is repeating a citation, and the execution artifact is the thing cited.

**The record dies when its subject dies** (`CLAUDE.md` §0). Every line number here is as read at
`ecacb57` and **will drift**; re-derive by symbol, never by line. When the tree has moved far enough
that this map misleads more than it helps, delete it rather than update it piecemeal.

---

## 0. What this document is, and what it is not

**It is** a high-level armature of the repository as it actually stands: the hierarchy of layers,
the flow of a season through the loop, the dependency edges between the head, its seams and the
subsystems, the modularity of those edges, and — deliberately and in full — **every stub, gap, inert
mechanism, unreached module and orphaned node** the reading found. Jordan's instruction was that
*"stubs/gaps are to be acknowledged and included"*; hiding them would defeat the document. It is
followed by an analysis of each subsystem, written out in detail.

It has four parts:

- **§1 — Plan-surface currency.** Which of the recent planning documents are live, which have drifted
  from the code on specific numbers only, and the nine places where two currently-live surfaces
  contradict each other.
- **§2 — The armature.** The layer stack, the season loop module by module, Layer 1's binding surfaces
  and open conformance nodes, the seam graph, the deprecated spine, pending items as dependency nodes,
  modularity concerns, orphaned nodes, and the instrument and guard apparatus.
- **§3 — Subsystem-by-subsystem analysis.** Personal combat, social contest, mass battle, the
  grand-strategy cluster, characters, fieldwork, threadwork.
- **§4 — Reverse index.** From each THE-NINE requirement row to the exact nodes it rests on.

**It is not a plan.** It contains **no build order, no sequence, no priority and no recommendation**.
Jordan asked for the armature and the analysis and put the master plan on hold (*"Our task is just #1
and #2 right now with #3 on hold"*). Where a pending item depends on another, that is stated as a
**structural fact** — *X requires Y to exist* — never as an instruction to do Y before X. The single
ORDER in the repository remains `workplans/2026-09-18-governance-settlement-behaviour-plan.md` §3
(its status line, `:12`); nothing here competes with it.

**It is not canon.** It is not Layer 1 (`architecture/` is), it is not a design document, and under
`CLAUDE.md` §0.05 it could not be a mechanism even if it wanted to be: *if this document were deleted,
the game would behave identically.* A design doc may not be cited as the reason a behaviour is
correct, and neither may this.

### 0.1 Legend

| mark | meaning |
|---|---|
| `→` | depends on / reads |
| `⇐` | consumed by |
| `∅` | no caller or consumer — declared but unread (the shape Layer 1 calls ID-13) |
| `[R-nn]` | the THE-NINE row(s) the node bears on, from `engine/season/requirements.yaml` |
| `[L1]` | a Layer-1 conformance node (`architecture/meta/04_CODE_ARCHITECTURE.md` and siblings) |
| `[none]` | serves neither a THE-NINE row nor Layer 1 — legacy or orphaned |
| `[M5]` / `[M6]` | the node sits on `mc_v18`'s retirement path (stages of `proposals/2026-09-27-mc-v18-retirement-plan/PROPOSAL.md`) |
| **STUB** | a code body that returns nothing real, or a `stubwire` deferral |
| **GAP** | a missing mechanism with a named row somewhere in the registers |
| **INERT** | built, but shipped at a control arm, so it writes nothing at the default |
| **UNREACHED** | real code that no live path calls |
| **MOD** | a modularity concern |
| `(audit)` | the claim comes from an earlier audit and was carried, not re-opened, in the Fable pass |

"Position N" always means a row of the ratified ORDER's `§3.2` table
(`workplans/2026-09-18-governance-settlement-behaviour-plan.md`), used here only as a **handle** for
naming an item, never as a rank.

---

## 1. Plan-surface currency

Seven planning documents were used in PRs over the past few days. A reader who opens any of them
needs to know which of their statements still match the code. The verdict below is factual: it says
what is live, what has gone stale, and where two live surfaces disagree. It draws no implications.

### 1.1 The seven documents, one at a time

#### Document 1 — `workplans/2026-09-18-governance-settlement-behaviour-plan.md` (+ `_part2`)

**Verdict: LIVE, and the single ORDER.** RATIFIED under ED-IN-0215, amended by ED-IN-0253 and
ED-IN-0270. Its status line (`:12`) reads *"§3 is now the only ORDER in the repository."*

**What is live:** the §3.2 position table with its STATE and GATE columns; §3.4's item → position
map; §3.9's file census and its eleven hard serial edges; §5's ruling batch and NOT-JORDAN table;
§6's gaps; §7's held-back list.

**What has drifted.** None of these are wrong in substance; they are numbers and status flags the
code has moved past.

- **(a) Phases α and β are entirely done.** `13f` (ED-IN-0271), `13e` (ED-IN-0272), `13d-i`
  (ED-IN-0273), `24d-i` (ED-IN-0274), G1b (ED-IN-0275), G2 (ED-IN-0276), G3 (ED-IN-0277) and G4
  (ED-IN-0278) all landed 2026-09-25/26. §3.1's *"THIS IS WHAT IS NEXT"* header over phase α is
  therefore spent. The §3.2 rows themselves are current.
- **(b) Row `20` still reads `BLOCKED | ★`** with no `20-i`/`20-ii` split. The mc_v18 plan proposed
  that amendment (its M2) and it was not made. Meanwhile `faction_q.resolve` now exists
  (`engine/season/queries/faction_q.py`).
- **(c) Row `12b` says "no roster exists."** That is still true of the tree, but draft candidate
  content now exists at `proposals/2026-09-26-decision-layer-execution-plan/candidate_*.md`
  (revision 5, marked "RATIFIES NOTHING").
- **(d) §3.2 row 8's "2 of 38 verbs carry `contests:`"** is now **3 of 39** — `march` was added.
- **(e) `_part2`'s `04:NNN` line citations above `:213`** moved by +2 (self-declared at
  `_part2:27-34`), and moved again with the 2026-09-28 seven-step amendment, when `04` gained roughly
  fourteen lines at `:134-137`, `:163`, `:516-520` and `:593-601`. Re-derive them by symbol.
- **(f) Position 22** in `_part2` dispositions the M-7 remedy (an obstacle ceiling) under §0 test 5 —
  i.e. as answered by architecture — while `HANDOFF_SC.md:15` calls the same question *"a genuine open
  call"*. Two live surfaces disagree (see §1.2 item 3).
- **(g) `18a` lists `Office.upkeep` for deletion**, while document 2's G2 gives it a reader (see §1.2
  item 1).

#### Document 2 — `proposals/2026-09-27-mc-v18-retirement-plan/PROPOSAL.md`

**Verdict: LIVE for M5, M6 and its §3 ADJACENT list; SPENT for M0–M4.** It is PROPOSED and held
back; its own ruling row `ED-IN-0279` is `resolved`.

**What is live.** **M5** — port `tools/balance_oracle.py`, retire `tools/campaign_output_probe.py`
and `tools/trace_execution_phases.py` — has not started: all three files exist and sit in
`ALLOWED_IMPORTERS` (`tests/valoria/test_mc_v18_is_deprecated.py:49-56`, six entries: three under
`engine/tests/`, three under `tools/`). **M6** has not started. The §3 ADJACENT list (G2, G3, S2–S5,
D1, D2, C1–C4, Step B) is still un-positioned in document 1, except where an item maps onto an
existing position.

**What is spent or stale.** Its §0 and §3 were written before M0–M4 landed. **M0–M3 landed in
`ecacb57`**: `test_j2` deleted with a `FORK:` row; the importer roster cut from 9 to 6;
`faction_q.py`; `seam/wrappers/mass_battle.py`; `massbattle.py::resolve_field`. **M4 landed in the
same commit**: the `march` row (`verb_table.yaml:401-427`), `loop/encounter.py`, `loop/sides.py`, the
rosters `field_degree_bands`, `field_casualty_models` and `march_target_kinds`, the `ENC` cells in
`write_matrix.yaml`, and hole rows H-147..H-152.

- Its *"M2 (now) … propose splitting position 20"* amendment was not executed in document 1.
- Its C1–C4 line — *"6a/6c derive automatically once Jordan supplies the cell values — no code change
  needed downstream"* — is **contradicted** by document 1 §3.5 (narrowed 2026-09-25: `12b` owes a
  carrier and a Query in `.py`) and by document 3 §3.3 H6 (one atomic commit across registry,
  descriptors, rosters, `npc_registry` and the verb split). See §1.2 item 2.
- Its corrections *"`ED-SE-0051` closed 2026-09-19"* and *"`dwelling` landed 2026-09-26"* are current.
- Its own *"What was not independently verified"* section says no structurally independent critic
  pass ran on the **plan**; that remains true. The M0–M4 **build**, however, did get valoria-critic ×2,
  `/code-review`, `/layer-conformance` and `/simplify`, per `ecacb57`'s commit message.

#### Document 3 — `proposals/2026-09-26-decision-layer-execution-plan/PROPOSAL.md` (+ `candidate_pursuit_cells.md`, `candidate_affiliation_content.md`)

**Verdict: LIVE.** A plan that ratifies nothing and self-deletes when H1–H13 land or are dropped.

**What is live.** H1 and H2 are **done** (2026-09-27): the deontology gate at
`decision/options.py::refusal_tolerance` / `refuses`, shipped with `refusal_axis=None` (H-146). H3,
H6 (with H8), H7, H9, H10, H11, H12 and H13 are open. The C1–C4 content is pending; drafts exist and
are unratified. Its §1.1 — the ED-IN-0251 row-2 disagreement between field and text — is unresolved.
Questions G-Q1..Q6 are unanswered.

**What has moved.** Its §2.3 correction (*"plan `:379` 12d → PARTIALLY DONE"*) was applied —
document 1's row `12d` reads `OPEN · partial`. Its observation that there are no `fight`,
`challenge` or `accept` rows is still true. `HANDOFF_IN.md:20` records a same-day conflict over the
`kill / wound` verb split (rename it standalone, versus let it ride the cells commit); **both
statements are live and unresolved** (§1.2 item 4). The `observers_for` citation was corrected to
`epistemic.py:491` in `HANDOFF_IN.md:10`.

#### Document 4 — `proposals/2026-09-25-squad-engagement-synthesis.md` (+ `concept-v5.md`, "CONCEPT · non-canonical")

**Verdict: LIVE as a ruling record.** RULED 2026-09-25; Parts A, B and C ratified on merge; Part D
PROPOSED with `ED-MB-0075` `needs_jordan`. By its own `:9-14`, its execution status is a pointer to
`HANDOFF_MB.md`.

**What executed** (per `HANDOFF_MB.md:15`): A1, A2, A4 and A6 (ED-MB-0069); A3 with C5 (ED-MB-0073);
A7 (ED-MB-0074, corrected); A8 (ED-MB-0071, `ROUT_CASCADE_FRAC` 1.0 → 0.6); C4 (ED-MB-0072); and d.1
(`_faction_to_unit` morale drawn from `Faction.Sta`).

**What did not execute:** A5 (role instincts), A9 (causes on trace rows, conditional), every
"Sequenced" row (per-cell Q, army-scale envelopment, generated map, AI generals, headless duels,
strategic outputs), and Part D's C2/C3 coupling.

**What is stale.** "Sequenced" row 5 — *headless NPC-vs-NPC duels wait on a mass_battle provider on
the season seam; the loop does not call mass_battle, `rosters.yaml:751-757` NO PROVIDER* — is stale:
the provider now exists (`rosters.yaml:874-892`, `seam/wrappers/mass_battle.py`). Row 6 — *strategic
outputs: today the adapter returns `{attacker_wins,…}` to `faction_action.py:393-395`* — is
half-stale: that path still exists via `mc_v18`, and a season path now also exists via
`resolve_field`. A7's UPHILL, WALLS, NARROW_PASS and RIVER_CROSSING rows, "identified but not
mechanically applied", remain so. The season path passes `terrain=None`
(`seam/wrappers/mass_battle.py:132`), so A7's derivation is reached only from `mc_v18`'s
`_try_conquest` path.

#### Document 5 — `workplans/2026-09-13-work-order.md`

**Verdict: LIVE as the CONTENT OWNER** of positions 13, 13b, 14, 15, 19, 19b and 20 (`ED-IN-0242`),
and explicitly *not an order*.

**What is live.** Its item → position table (`:22-30`) is still consistent with document 1 §3.2 (13;
13b done; 14; 19/19b; 15; 3–7 done; 20). Item 6, `Tenure.term`, is still absent — G3's `T-n` basis
is built but *"unbuildable, no `term` field"* (`_part2:362`). Its R3-denominator finding (`:198-214`)
is carried live in document 1's row 21.

**What is stale.** "38 verbs" is now 39. "20 silent verbs" pre-dates `13f`, `march` and `13`
executing. "19 of 46 NPC cases do not build" and "54 of 143 unrepresentable" are still the last
measured figures (`requirements.yaml:289`). Its `:192-196` still quotes the ORDER collision as live;
that was **resolved** by ED-IN-0253 (document 1's status line).

#### Document 6 — `workplans/valoria_master_workplan_v7.md`

**Verdict: CANON / RATIFIED (ED-IN-0216). Its ORDER content is superseded; its milestone, sort and
measurement content is not.**

**Not superseded by document 1:** §0's owner table and its no-status-column rule; §1's M1/M2/M3
definitions (M2 has no instrument; M3 is gated on ED-1051); §3's "who can answer" sort *as a method*,
and its four-spellings finding (`:83-105`); the measurements in §7.2, §8.2 and §8.2b (counterparty
cost; told-channel saturation at the deposit site); and §8.5's observation that "there is no player".

**Superseded or stale:**

- §0's table (`:53`) says document 1 is "PROPOSED under ED-IN-0215"; it is RATIFIED.
- §1's M1 table (`:127-133`) — two rows failing, with stubs at `mc_v18.py:194/212` on the M1 path —
  predates ED-IN-0226 re-pointing `m1_acceptance.py` at the head. Currently three of four rows pass;
  the failing row is row 4, the doc-derived board.
- §2's IN spine is replaced by document 1 §3.
- §3.1's rows: `ED-SE-0051` closed 2026-09-19 (`ED-SE-0054`/`0055` follow); `ED-IN-0214` is
  superseded by ED-IN-0261 (document 1 §5 item 1); `ED-MB-0065` was superseded 2026-09-15 and its
  guard deleted at M0; `ED-MB-0016` is `status: open`, `needs_jordan: false` (document 1 row 25).
- §6's "ORDER collision REAL, not closed" was closed by ED-IN-0253.
- §6's v6 retirement is still deferred (v6 is still on disk; `ED-IN-0071`'s `designs/` path citation
  is the blocker) — that part is current.
- §3.1's OI-05 / OI-07 (`generate_npc` / `form_knot` stubs) now live only inside `mc_v18.py`.

#### Document 7 — `proposals/2026-09-05-proceedings-subsystem/00_DERIVATION.md` and `21_RECONCILIATION.md`

**Verdict: LIVE, PROPOSED, HELD BACK IN FULL.** The design is not ratified (`ED-SC-0033..0035`).
`21`'s PART C/D supersedes `19_PLAN.md`'s step text (`HANDOFF_SC.md:13`).

**Execution state of `21`, phase by phase:**

- **PHASE 0 executed** 2026-09-07. M-7 was measured: `p_success` 0.0006 at Ob 3 at the 1D floor; the
  σ-reach remedy was refuted (`:442-472`).
- **PHASE 1.** Step 1: the predicate half is done (PR #379); the record-moving route is H-84 /
  position 16, open. Step 2: done (ED-IN-0205, `all_five`). Step 3: done (R8.1 `seen`, PR #432).
  Step 4: the `told_by` part (c) is built (`witness.py:369-371`); parts (a) and (b) are open. Step 5
  (the 3×3 ledger cap): the cap now evicts nothing (`:553`).
- **PHASE 2**, steps 6–16: open, except step 8 (`release`, done) and the gate half of step 11 (the
  conferral opener, written in G3, ED-IN-0277). `21:575` (step 11) asks the IN lane for a conferral
  clause; that clause is now built (`state/gate.py::tenure_write_basis`, fifth clause).
- **PHASES 3 and 4:** open.

**Record defects and open questions.** `HANDOFF_SC.md:13`'s step numbering (*"step 1 executed
(ED-IN-0205), step 2 superseded by R8.1's struct, step 4 told_by, step 22 Tenure.term"*) does not
match `21`'s PHASE-1 numbering, where ED-IN-0205 is step 2 and R8.1 is step 3 — both surfaces live
(§1.2 item 7). D-6/D-7 (the `speech_kinds` roster default, `19_PLAN.md:952-960`) and `ED-SC-0038`
(per-matter versus single-margin) remain open per `HANDOFF_SC`. The social-contest retirement
(position 2, ED-SC-0033 clause 2) remains ruled and unexecuted; `HANDOFF_SC.md:14` narrows its
deletion set to the kernel plus `contest_legacy_stub.py`, not `parliamentary_*`.

### 1.2 Contradictions between currently-live surfaces

Each item below is two surfaces, both live, that say different things. This list states the
disagreement; it does not resolve it.

| # | subject | surface A | surface B |
|---|---|---|---|
| 1 | **`Office.upkeep`** | Document 1 `18a` — twelve field deletions (r2 `05:223-256`), still lists `upkeep` | Document 2 §3 G2 — *"`Office.upkeep` finally gets a reader"*. The field is present at `state/carriers.py:644` (document 2 §0; verified), and `_part2:1295` lists it among the thirteen |
| 2 | **C1–C4 derivation** | Document 2 §3 — *"derive automatically … no code change"* | Document 1 §3.5 and document 3 §3.3 H6 — a `.py` carrier and Query for `12b`; one R6-atomic commit across five owners plus the verb split |
| 3 | **M-7 remedy** | Document 1 `_part2` position 22 — obstacle ceiling, answered under §0 test 5 | `HANDOFF_SC.md:15` — "a genuine open call" |
| 4 | **`kill / wound` rename** | `HANDOFF_IN.md:20` — Jordan, in-session: rename standalone now | `HANDOFF_IN.md:9` / `:27` standing order and document 3 §3.1 — the split rides the cells commit; a two-step is unbuildable because `_load_alignment` validates verb keys (`data/verbs.py:685-692`) |
| 5 | **The M4 row** | `HANDOFF_IN.md:19` — "step 11 (garrison Sites) not started"; "no review pass has run on M4" | `ecacb57` — seeds `s_*_garrison` per settlement (`harness/populated.py:396-414`); its message records valoria-critic ×2, `/code-review`, `/layer-conformance` (both lenses) and `/simplify` on M4. H-150's `cite:` agrees (`hole_register.yaml:3151-3155`). The handoff row is stale on both sub-claims |
| 6 | **Count of contested verbs** | `requirements.yaml:88-90` scale note — "1 of 32 verbs declares `contests:` and it is `kill / wound`"; and `:95` — "Wave 4 item 4.2 carries the [mass-battle] seam" | The same file's R-05 body says 2 of 38; the tree has 3 of 39; and the mass-battle seam now exists |
| 7 | **Proceedings step numbering** | `HANDOFF_SC.md:13` | `21_RECONCILIATION.md` PHASE 1 (see document 7 above) |
| 8 | **ED-IN-0251 row 2** | field `needs_jordan: false` | its own text, "still needs_jordan" (document 3 §1.1; `registers/editorial_ledger_in_archive.jsonl:168`) |
| 9 | **Members of `queries/`** | `04 §A.2:132` — three `queries/` modules | `faction_q.py` is a fourth, deliberately not written into `04` (its docstring `:4-26`; layer-conformance B4, third disposition) |

### 1.3 Handoff rows that are current (not restated above)

These lane handoff rows were cross-checked against the tree and still hold:

- **`HANDOFF_PC`** — `partisan` still present at `weapons.py:322,852`; the PC id block is exhausted
  (`id_reservations.yaml:124`, `next_free: 58`); Ob-from-defender is unbuilt.
- **`HANDOFF_FA`** — the score/2 three-site disagreement (`test_faction_obstacle_conventions.py`).
- **`HANDOFF_SE`** — `24d-ii`, `24e`, ED-SE-0052/0053 held back, H-62, D6, MW-11/MW-5 red.
- **`HANDOFF_WR`** — position 27; the two `rendering.py` stubs.
- **`HANDOFF_FI`** — ED-FI-0009 (the degree producer); ED-FI-0002; ED-914.
- **`HANDOFF_GO`** — the ED-1051 gate.

Id state as read (nothing allocated by this document): IN `next_free: 280`; MB `next_free: 76`.

---

## 2. The armature

### 2.1 The layer stack

The repository has one governance stack (`CLAUDE.md`'s layer table) and, inside Layer 2, a head, the
retained subsystems, a retire-set of subsystems, a deprecated spine, a shared substrate, and the
apparatus that measures and guards all of it. The registers are the data the code reads.

```
LAYER 0  CLAUDE.md (§0 five-step gate · §0.05 code-is-mechanism · §0.2 done=executes · §10 tiers)
   │
LAYER 1  architecture/  (RATIFIED ED-IN-0204; 20 files)                                   [L1]
   │      meta/01_AXIOMS · 02 · 03_VERBS_AND_LOOPS · 04_CODE_ARCHITECTURE (the binding shape,
   │      scope = engine/season/) · 05 · 06 · 07_DYNAMICS · ARCHITECTURE_V2 · holonic_ARCHITECTURE
   │      · 00_ADOPTION_README · PLAN.md
   │
LAYER 2  THE GAME
   ├── engine/season/            THE HEAD (82 .py; the loop; §2.2)                 [all R-rows]
   ├── RETAINED subsystems (ED-IN-0204 Decision 1)
   │     systems/combat/combat_engine_v1/  (29 .py)  reached: yes, PATH seam            [R-05,R-09]
   │     systems/mass_battle/sim/          (35 .py)  reached: yes, composition role     [R-04,R-05,R-09]
   │     systems/social_contest/sim/       (20 .py)  reached by season loop: NO         [R-05,R-09 via proceedings]
   ├── RETIRE-SET subsystems (requirements.yaml scales:, in_loop:false) — run only via mc_v18 or not at all
   │     systems/factions (18) · settlements (8) · world (6) · overview (8)                [R-04 subject]
   │     systems/characters (5) · fieldwork (5) · threadwork (9)
   │     systems/npcs · _architecture · ui · victory · articulation  (0 .py — reference only)
   ├── DEPRECATED SPINE  engine/mc_v18.py + engine/autoload/* + engine/cross_scale/*        [M5][M6]
   ├── SUBSTRATE (shared by both spines)  engine/autoload/{dice_engine,sigma_leverage}.py ·
   │     engine/substrate/{composition,descriptors,pc_engine,stubwire,names,canon_buckets,
   │     world_initial_state}.py · engine/engine_params/*.json (exports)
   └── APPARATUS / GUARDS  engine/season/harness/* · engine/season/tests · tests/valoria/* ·
         engine/tests (sim-regression) · tools/* · .github/workflows/valoria-ci.yml
REGISTERS (data the code reads)
   engine/season/{requirements,hole_register,verb_table,write_matrix,rosters,governance_spine,
   venues,npcs,ENDINGS_CLASSIFIED}.yaml · references/{module_contracts,descriptor_registry,
   names_index,id_reservations,restructure_ledger}.* · registers/editorial_ledger*.jsonl
```

**The 2026-09-28 Layer-1 amendment.** `ecacb57` made ENCOUNTER the seventh step of the season, sharing
barrier 3. It touched `04:134-137`, `04:163` (the module row), `04:516-520` (the season pseudocode),
`04:593-601` (the fold), `03` §D.1 and `07` §4, and added pointer notes in `ARCHITECTURE_V2`,
`holonic_ARCHITECTURE` and `00_ADOPTION_README`. It left `04 §A.2:132` — which says `queries/` holds
three modules — deliberately stale with respect to `faction_q`; the reason is recorded in
`faction_q.py`'s own docstring.

**Where each subsystem stands, in one line.** Of the three retained subsystems, two are reached from
the head (combat through a `sys.path` seam, mass battle through a composition role) and one is not
(social contest; the head reproduces its one live resolution line engine-side instead). Every
retire-set subsystem runs only through the deprecated spine or not at all. §3 analyses each.

### 2.2 `engine/season/` — the season loop, module by module

`engine/season/` is the head: the season loop plus the registries it opens at runtime. It runs. By
its own register it is not yet a game — `python -m engine.season.harness.register --requirements`
scores it against `engine/season/requirements.yaml`, and most THE-NINE rows read `not_met` or
`partial` (§4).

#### 2.2.1 The driver and the seven steps

The driver is `loop/driver.py`; its shape is specified at `04 §C.1:511-522`.

```
SeasonDriver.season(w):
  calendar(w, Token(CALENDAR))          loop/calendar.py   barrier 1
  matter(w, Token(MATTER))              loop/matter.py     barrier 2 · WORLD FREEZES
  cache.build → frozen → _questions_at_barrier (driver, ED-IN-0206)
  for r in range(scene_budget):                            (U2, R-03 met)
      deliberate(frozen)                loop/deliberate.py  a MAP, no token (AX-2 island)
      resolve(w, Token(ACTS), scenes)   loop/resolve.py     barrier 3 · the ordered fold
      encounter(w, Token(ACTS), events) loop/encounter.py   shares barrier 3 (M4, 2026-09-28)
      log
      witness(w, Token(INTERIOR))       loop/witness.py     barrier 4
  census(w, Token(MATTER))              loop/census.py      shares WITNESS join
```

Three structural facts about the driver:

- **`mint_token`** (`driver.py:~90`) is the one constructor of `Token` (G2, ED-IN-0276). Its guard is
  `tests/test_g2_token.py`. `[L1 04:199,206]`
- **`resolvable_verbs()`** (`driver.py:~100`) applies three gates: the verb has an evaluable
  precondition (a typed cell, a `REQUIRES_PREDICATES` entry, or none); it has an effect behind a
  non-empty `writes:`; and it is not `contests:`. It measured 19 at `952dc21` and 20 after `13f`
  (`_part2:975`). `[R-05]`
- **`loop/sides.py::sides_of`** (M4) builds `claimants`, `subject` and `rung` from the PRIZE's
  manifest `module` — never per verb or per target shape (`sides.py:9-25`, the ARC-40 case).
  `[R-04][R-05]`

#### 2.2.2 The gap nodes inside each step

**CALENDAR — `loop/calendar.py`.** At `:33-42`, `holder` is written nowhere in production, so
`vacant` is always true and the `DocketItem` write never runs. `Date.fired` is written with no
`emits=` and no subject (position `11b`). **GAP.** `[R-01]`

**MATTER — `loop/matter.py`.** The body write and the death cascade at `:298-326` are **INERT**:
`data/fixtures.py:494` sets `body_step=0` (H-125 swept 0/10/67; ED-IN-0247). The per-eater draw at
`nearest_store` (`world_q.py:172`) is **real** and meets demand (item 3a). The scale of the
subsistence carrier was re-opened by ED-IN-0255 (`24f`). Two latent holes: **H-129** —
`last_emission_of` chains on the wrong person for fold-emitted body Events (latent while
`body_step=0`); and **H-135** — closure writes at MATTER are never judged by F9, of which `dwelling`'s
zero-wear `condition.worn` is the live instance. `[R-01][R-04]`

**DELIBERATE — `loop/deliberate.py`.** Holds no token; `_rehome()` was moved to MATTER (G2). No gap
recorded. `[L1 AX-2]`

**RESOLVE — `loop/resolve.py`.** The ordered fold. `_contest` carries the M4 declare/defer branch
(`04:593-601`); `work`'s accumulator is judged twice (G4). Two holes:

- **H-137** — an effect body runs outside the gate's observation window, so a mutation made before
  returning a `Change` is invisible to F3 and F9. None of the thirteen shipped effects reaches it; any
  new effect could.
- **H-136** — `transfer` operand derivation: 628 of 900 corpus calls are `from == to == r_hearth`.
  They are now refused by F9 rather than recorded as a fabricated success.

`[L1 04:536][R-01][R-05]`

**ENCOUNTER — `loop/encounter.py`.** Selects RESOLVE's `Declared` Events and re-runs `_contest` at
`Step.ENCOUNTER`. Holds no state; shares `WriteClass.ACTS`. Its only consumer is `march`.
`[R-04][R-05]`

**WITNESS — `loop/witness.py`.** Five channel predicates (`epistemic.py::CHANNEL_PREDICATES`), fan-out
`all_five` (ED-IN-0205), the told channel (ED-IN-0222), `told_by` minted at the teller's confidence
(`:369-371` — part (c) only), and the `seen` claim (R8.1, PR #432). Three gaps:

- **`told_by` parts (a) and (b)** — the `(person, channel)` precedence walk, and the document/remit →
  `told_by` source map. `witness.py:182` returns only `firsthand` / `firsthand_via_knot`.
- **`_ch_post_remit`** (`epistemic.py:413`) is to be replaced by the obligee channel minting `inferred`
  (`17a`); today `inferred: 0`.
- **The lossy tell at `Partial`** (`15b`).

`[R-01][R-02][R-07]`

**CENSUS — `loop/census.py`.** Writes nothing — *"NO CLOCK GENERATES ANYTHING"* (`:33`; ED-WR-0011
option A). The `(Person, weight)` and `(Person, exists)` `[CEN]` rows have no producer. P3
individuation is NOT STARTED (`_part2:1546-1549`). `Rung.envelope` has no built-world writer; only
probe W9 writes it (`harness/probes.py:1639-1650`). **GAP.** `[R-04][R-06]`

#### 2.2.3 `state/` — the owned stores, the gate, the log

**`state/world.py::World`** holds the collections `persons, rungs, offices, sites, records,
propositions, dates, petitions, dispensations` (`:1097-1098`), plus the `docket` sequence, `tenures`,
`acts` and `log`. `content_hash` folds all of them (H-118).

**The gate.** `World.write(closure XOR Change)` is THE GATE (G4, `state/gate.py`). It runs F3 —
`tenure_write_basis`, with five bases: T-m, T-n (unbuildable), cascade, T-o and conferral
(ED-IN-0277) — then F9, a before/after comparison per named `Subject`. No movement yields a
`NoOpReceipt`; each moved subject yields a receipt. `World._grant_remit` runs at `add_tenure`
(13b/13f; `force` parameter). **`World.remove_person` mutates directly and never goes through
`write`** (H-152's citation). `[L1 04 §C.2 :531-538, §B.13]`

Gap nodes in `World`:

- the `petitions` and `dispensations` dicts have no production reader (they are `15`'s fold target);
- `w.crossings` (`world.py:188`) duplicates the MATTER Event (`11a` deletes it);
- latent holes H-130 (`write` can apply before a late refusal), H-131 (`Gate.close()` is not wired at
  ordinary barriers), H-139 (a Tenure deletion is invisible to the diff), H-141 (the `earns=None`
  contract is dropped when another subject names a kind), H-138 and H-140.

**`state/carriers.py` — the carriers, field by field.** `Person := (id, weight, capability, body,
exists, travel_leg, stance[], pursuits, scar[axis], axis_count[axis], coherence?, ledger)`
(`04:220-224`, amended 2026-09-24). Each field's state:

| field | state | row |
|---|---|---|
| `capability` | **Zeroed on every corpus person** (`harness/probes.py::_zero_capability`; F.6, "no season writer"), so the σ pool and obstacle fall to fixture defaults (`seam/wrappers/sigma.py:82-102`) | `[R-06][R-09]` |
| `pursuits` | Renamed (ED-IN-0268); its values are the old 13×4 (`rosters.yaml` `pursuit_projection`). No act writes it (H-62). `write_matrix.yaml:183-190` declares `[RES] ACTS emits pursuit.moved` with the trigger unspecified | `[R-06][R-08]` |
| `scar[axis]` | The float-per-axis producer `_scar` (`loop/effects.py:340`) is **INERT** (`fixtures.py:533` `scar_step=0`, H-128), and it is ruled the wrong shape: ED-IN-0261 asks for a count per element, thresholds 1/2/3, over `observers_for` (`epistemic.py:491`) | `[R-06]` |
| `axis_count[axis]` | A matrix row with **NO FIELD** (`matrix_rows_without_a_field()`; `write_matrix.yaml:148-152`) | `[R-06]` |
| `stance[]` | Written at world construction only (`harness/populated.py:616`); no act writes it (`10` / U5). Read by `decision/choose.py::stance_toward` | `[R-07]` |
| `coherence?` | Carried, unread (F.5) | `[none]` unless threadwork / position 27 builds |
| `travel_leg` | Appended by `_eff_move` (`effects.py:272`), never cleared; `decision/budget.py:59` penalises it every season (`19c` ride-along) | `[R-08]` budget |
| `body` | See MATTER; also written by `kill / wound` (Felled/Wounded) and by `march` (Won/Lost, the `ENC` cells, H-148 `field_casualty_model`) | — |
| `weight` | Every builder mints `weight=1`; only `probes.py:744` mints a cohort (a precondition of `24f`) | `[R-04]` |

`Person.beliefs` was DELETED 2026-09-25 (PR #430). `Person.marks` and `Person.orient` were dropped
(ED-IN-0261).

**Tenure.** `Tenure := (id, subject, object, kind, since, until, degree, payload)`. **`term` is
ABSENT**, which is why T-n is unbuildable (work-order item 6; `21` C-10). `degree` is carried and
unread (F.4), so `faction_q.head` is always `None`. `payload` is live (`granted_acts`, 13b).
`[R-05][L1 04 §B.8]`

**Office.** `Office := (…, remit_acts, establishment, upkeep, dates, scope_rung, conferral,
revocation, body/faction)`. `establishment` is read by `world_q.establishment_of`, which has no
callers (`17a`). `upkeep` has no readers (§1.2 item 1). `dates` and `scope_rung` are on r2's deletion
list (`18a`).

**Rung, Site, Record.** `Rung.{sites, records, dates, stake, transmission, judging_set_rule}` sit in
`_DECLARED` (`:663`) and are on the deletion list, as is `Site.drawers`. `Record.kind` is free text
(`:522`); `_eff_create_record` defaults it to `"text"`, and there is no `record_kinds` roster (`15`).
`Record.ttl` is the document half of C-10.

**The rest of `state/`.** `state/acts.py` (the append-only act store); `state/log.py` (`append`
asserts that causes ∈ log ∪ acts ∪ {ROOT}, but does **not** refuse a duplicate Event id —
`encounter.py:19-24`); `state/attribution.py` (`actor_of` / `anchor_of`; `Event.subject` was deleted
under ED-IN-0275); `state/ledgers.py` (the S1 extraction); `state/ids.py` (`H`, `ROOT`);
`state/containment.py`. `[L1 04 §B.9, :402]`

#### 2.2.4 `data/` — the one loader

`data/` is the single loader Layer 1 requires (`04:124`; ID-12 / ID-13).

**`data/rosters.py` ← `rosters.yaml`.** 48 top-level keys, including `tenure_kinds, rung_kinds,
remit_acts, remit_default, witness_channels, claim_sources, strata, eligibility_kinds, pursuits,
pursuit_axes, question_sources, person_predicates, combat_degree_bands, wound_harm_models,
field_degree_bands, field_casualty_models, march_target_kinds, observation_terms, verb_capability,
contest_subsystems, titles, site_kinds, matter_kinds, wear_per_season, subsistence_weight, factions,
role_templates, faction_leaders, office_bodies, requires_operands, beneficiary_kinds, requires_forms,
fan_out_modes, conferral_bases, revocation_bases, site_yield, band_floors, role_template_pursuits,
pursuit_projection, alignment`. Its gaps:

- `question_sources` entries `date_due` and `band_crossed` contribute zero questions (`11a` deletes
  them).
- `requires_operands` is closed on eight names; there is no name for a Record or dispensation operand
  (`15c`; `comply`'s own note).
- `titles` / `title_domain` survive only as `populated.py`'s world-generation reader (13d-i item 5,
  undecided).
- `pursuits` carries `from_descriptor: conviction_roster` (`descriptor_registry.yaml:236`,
  `count: 13`) — the substrate half of the rename (`12d`). `pursuit_axes` is the old four.
- `alignment` is keyed on the old four (`rosters.yaml:1515+`).
- **Silent data-loss hazard:** `role_template_pursuits` (`:1352-1417`) uses the old names, and its read
  path `to_axes` (`data/pursuits.py:79-86`) does **not** raise on an unknown name (document 3 §2.2).
  By contrast `data/cast.py::pursuit()` does raise.

**`data/verbs.py` ← `verb_table.yaml`** (39 rows). `_load_projection` and `_load_alignment` bind at
module scope and raise on unrostered keys or an all-zero row — R6 atomicity (`:598-694`).

**`data/matrix.py` ← `write_matrix.yaml`** (39 `(kind, field)` rows; steps include the new `ENC`).

**`data/fixtures.py`** — the `Fixtures` control arms: `body_step`, `scar_step`, `pool_default`,
`obstacle_default`, `field_casualty_model`, `field_morale_weight` / `field_grudge_weight`, `wear` and
floors, `refusal_axis=None`, and others.

**`data/requires.py`** — the typed grammar (`§F.24a`): five forms, closed stems. There is no `rank`
stem yet (`21` step 9); `thread_read` is unrepresentable (H-85).

**`data/cast.py`, `data/files.py`** — the cast reader (raises on an unknown pursuit name) and file
helpers.

#### 2.2.5 The 39 verbs, by mechanism state

Effects are registered with `@effect_for` in `loop/effects.py`. Thirteen are registered: `confer,
establish, release, revoke, convene, move, work, create_record, destroy_record, kill / wound, march,
utter, transfer`.

| class | verbs | notes |
|---|---|---|
| **Contested** — 3, route to the seam | `kill / wound` → "the body"; `tell` → "a standing"; `march` → "a field" (`step: ENCOUNTER`, `declares: Declared`) | The only door to R-09's roll. `fight` and `challenge` → `accept` are ruled but have no rows (ED-IN-0261) |
| **Execute in the corpus** — last measured 13, plus `establish` | `create_record, interview, move, reconstruct, release, research, speak, surveil, tell, transfer, utter, dispatch, kill / wound`; `establish` is resolvable since `13f` but refuses without operands | R-05 is `not_met` (`requirements.yaml:295-403`) |
| **Have an effect but are never attempted or always refused** | `confer, convene, revoke, destroy_record` (the pinned never-attempted set, `test_season_shape.py:6996`); `work` and `examine` are always refused (no Site question); `march` is never attempted — `operands_for` has no `march` arm (H-151's citation) | `convene`: `holder` is never written. `destroy_record`: H-75 |
| **`writes: []` — emission only** | `comply, dispatch, evade / defy, construe, speak, examine, interview, research, surveil, thread_read, reconstruct` | The investigation six are witness-only: no `_eff_*` and no degree producer (ED-FI-0009 item 4.5). `comply`, `evade / defy` and `construe` are `19b` (no typed cell, no predicate) |
| **Declared writes, NO effect** — not resolvable; prose `requires:` (H-65) | `carry, commit, determine, exchange, forge, issue, levy, oblige, open_case, petition, repudiate, restore, succeed, tie / knot` | `issue` (Dispensation → `15`); `petition` (`15`); `carry` (DocketItem); `commit` (`7a`, built and held); `oblige` (`17a`); `levy`, `open_case`, `determine` (`19`; `determine` needs `judging_set`, H-32); `restore` is typed with no effect (`24e`); `forge`, `exchange`, `repudiate`, `succeed`, `tie / knot` (`14`) |
| **A prize with no verb** | "a proposition" (`rosters.yaml:912-916`, `interim: true`) | A declared prize row that nothing reaches |

#### 2.2.6 `queries/`

- **`world_q`** (World-first): `descendants`, `ancestry`, `members`, `footprint`, `hold_force`,
  `home_of`, `nearest_store`, `questions_for` (Q1–Q4), `density`, `mustered`, `holder_faction_of`,
  `fortification_of`, `establishment_of` (∅ callers), `judging_set` (**STUB** — raises
  `Unspecified`), `conferral_path` (one test caller), `occasioned_by` (a dead guard), `WorldReader`.
- **`person_q`** (asker-first): `LedgerReader`, `entrenchment`. There is no `ambitions(p)` (`17`) and
  no `confliction` (`12b`).
- **`cache`** (built at the barrier). Two missing indexes are deliberately not built (PR #430).
- **`faction_q`** (M2): `resolve` only, returning `Faction(proposition, members, holdings, seats,
  head=None)`. `holdings`, `purview`, `superiors`, `subordinates` and `at_war` are unbuilt. Its only
  consumer is `seam/wrappers/mass_battle.py`.

**GAPs:** `capacity(w, rung)` is absent (`24d-ii`; ED-SE-0051 ruled its shape). `reach(w, p)` and
`place_of` are absent (`11a`); a comment at `carriers.py:390` names `place_of` as existing, which is
false. `[L1 04:152, §B.6.1, :285-286]`

#### 2.2.7 `decision/` — the AX-2 island

`decision/` has no `World` in scope; the guard is
`test_decision_package_never_names_world_anywhere_under_it` (`test_season_shape.py:2781`).

- **`questions.py::aggregate_questions`** — a single global rule; there is no `Person.precedence`.
- **`options.py::opening_set`** — plus `person_side_eligible`, reading `t.granted_acts`, and the H2
  deontology gate `refusal_tolerance` / `refuses`, **INERT** at `refusal_axis=None` (H-146).
  `_derive_operand` returns the same subject for every slot (H-94 / H-136).
- **`choose.py`** — `score = Σ axis_w·align + stance_toward + u`; `_sample_order` is a Gumbel softmax
  (U4). `Candidate.why` is written and read nowhere.
- **`budget.py`** — the `travel_leg` penalty.

`[R-06][R-07][R-08]`

#### 2.2.8 `seam/` and `manifest/`

- **`seam/contest.py::contest(w, rung, prize, claimants, …)`** — S39.1: claimants are PERSONS;
  `max_depth`. Also `contest_subsystem(prize)`.
- **`seam/ladder.py::degree_of`** has three branches:
  - `wound_state` → `combat_degree` (bands Felled / Wounded / Untouched; the band edge is a literal
    at `:133-135`, position 8(b));
  - `net` + `ob` → `dice_engine.degree_from_net` (two positional arguments; no `BandExtension`
    forwarded — `_part2:111-116`);
  - `attacker_wins` / `unopposed` → `field_degree` (Declared / Won / Lost / Unopposed).
- **`manifest/registry.py` + `providers.py`** — `@provider("contest", name)`; the `rosters.yaml`
  `prizes:` rows (`:869-916`). Guard: `tests/valoria/test_season_providers_are_registered.py`.

`[L1 04:164, :679-692][R-09]`

#### 2.2.9 `harness/` — instruments, not game code

`populated.py` (`build_realm`: 46 NPCs, 37 settlements, 211 hearth rungs plus 211 `dwelling` Sites
plus garrison Sites; 9 Propositions); `corpus_run.py` (`build_at`, 143 cases; prints R3, `WHERE THE
39 GO`, and `unrepresentable scales:`); `governance_spine.py` with `governance_spine.yaml` (13 seats,
7 depths); `headless.py`; `probes.py` (the P-probes, `Ev()`, `_zero_capability`, `tiny_world`);
`register.py` (`--requirements`, `--check`, `--counts`); `report.py` / `delta.py`;
`conviction_spread.py`; `run_cases.py`; `exercises.py`; `invariants.py`.

**GAPs:** no instrument runs the populated realm for formability or execution (document 1 §6); R3
has four inconsistent figures over two denominators (row 21).

### 2.3 Layer 1 — what it binds, and the open conformance nodes `[L1]`

**The binding surfaces of `04_CODE_ARCHITECTURE.md`:**

- §A.1, the axiom → module table (`:113-125`);
- §A.2, the nine modules (`:129-139`, now "seven steps"), and the module I/O table (`:150-170`, with
  the `loop/encounter` row added);
- §B.2, the carriers (`:220-224`);
- §B.6.1, the `Faction` view, and the NEVER list at `:285-286`;
- §B.8, the Tenure closing paths (T-m / T-n / T-o / cascade);
- §B.13, the twelve loader invariants;
- §C.1, the season pseudocode (`:511-522`); §C.2, the gate (`:531-538`); §C.4, degree-keyed writes;
  §C.5.1, the mass-battle roster contract; §C.7 / F.1, per-conjunct refusal;
- PART D's grade column (STRUCTURAL / MECHANICAL / CONVENTION; §0 `:66-99`);
- PART E's build steps 0–13 (`:1038-1055`; critical path 0 → 8; step 8 is THE BAR);
- PART F's gaps F.1–F.33 (`:1080-1107`).

**The guards that enforce it** (all under `tests/valoria/` unless noted):

| guard | what it pins |
|---|---|
| `test_engine_does_not_import_systems.py` | `BASELINE_TOTAL` 0 dotted `systems.*` imports under `engine/`; `PATH_SEAM_ALLOWED = {'substrate/pc_engine.py'}`, shrink-only. Its one-hop branch `_relative_module_files` has no planted falsifier |
| `test_g2_token.py` | `Token(` appears in the driver only |
| `test_decision_package_never_names_world…` | the AX-2 AST scan |
| `test_degree_ladder_single_owner.py` | T-k; carries the `RULINGS` dict, including Ob-from-defender |
| `test_season_providers_are_registered.py` | every prize row has a registered provider |
| `test_season_invariant_sweep.py` | the season invariants |
| `test_conviction_roster_single_owner.py` | the `len(CONVICTIONS)==13` pin |
| `test_faction_write_sweep.py` | ED-FA-0038 |
| `engine/season/tests/test_governance_build.py`, `test_g1a_*`, `test_g1b_attribution.py`, `test_march.py`, `test_seen_claim.py` | per-feature season tests |

**Open conformance nodes** (`HANDOFF_IN.md:17`, PR #430):

- **Invariant #4, the per-conjunct half.** Three live verbs have two conjuncts; a keyed
  `emits_on_refusal` schema is needed (F7 / F.1).
- **AX-4 setter scan** (S2) — abandoned: 25 hits, mostly false positives.
- **Typed ids and the AX-3 sub-store token split** (S3 / S4) — parked; "STRUCTURAL under a checker ·
  MECHANICAL at runtime" (`04:88-92`), and there is no CI type-checker.
- **A `PersonInterior` type and the `queries/cache` indexes** — deliberately not built.
- **The `openers:` roster** is a hand-copied second copy of the `_eff_*` opener bodies (the §8
  hazard).
- **The seam-import detector's one-hop branch** has no falsifier.
- **`faction_q` versus `04 §A.2:132`** — stale by design.
- **H-137** — the `write()` calling convention, which is a design decision.
- **F.20b** — the fold emits `act.ineligible`, `act.refused` and `contest.resolved` as body literals
  (invariant 7).
- **Invariant 2** — nine matrix rows have no producing verb (`04:1042`).
- **`march`'s `requires_typed`** does not narrow to settlement; the check is in `sides_of` instead
  (H-149). This is a recorded Layer-1 placement choice, not a violation.
- **`03_VERBS_AND_LOOPS.md` / `holonic`** step-count mentions were not individually re-walked (their
  own pointer notes cover them).

**New code checked against Layer 1.** Per `ecacb57`'s message, M4 did get `/layer-conformance` (both
lenses); M2 and M3 got a critic and `/simplify`. `HANDOFF_IN.md:19` is stale on this (§1.2 item 5).

### 2.4 The seam graph — prize → provider → subsystem → route → gaps

The head reaches a subsystem only through a contest prize. There are three prizes with providers
(plus "a proposition", which shares the social-contest provider and has no verb).

```
"the body"  (module personal_combat, provider personal_combat)
   seam/wrappers/combat.py:106 → engine/substrate/pc_engine.py (PATH_SEAM_ALLOWED, the ONLY sys.path seam)
     → systems/combat/combat_engine_v1/wrapper.fight (+ WoundTracker → wound_state)          [R-05][R-09]

"a standing" / "a proposition"  (module social_contest, provider sigma_leverage, interim: true)
   seam/wrappers/sigma.py:128 — ENGINE-SIDE; imports nothing from systems/; reproduces
     systems/social_contest/sim/contest/resolver.py:302's line (`roll_net + net_boost`) via
     engine/autoload/{dice_engine,sigma_leverage}.py                                            [R-09]

"a field"   (module mass_battle, provider mass_battle, step: ENCOUNTER, declares: Declared)
   seam/wrappers/mass_battle.py:83 → composition.require("mass_battle.resolve_field")
     (references/module_contracts.yaml composition_roles; engine/engine_params/composition.json)
     → systems/mass_battle/sim/massbattle.py:344 resolve_field(w, side_a, side_b, *, terrain=None, rng)
   sides: loop/sides.py::sides_of → actor's muster at origin (world_q.mustered) ·
          target holder faction (world_q.holder_faction_of) → faction_q.resolve(...).members ∩ present
```

**Gaps on "the body":**

- a fixed `DECISIVE_OB=3` (`core.py:79-83`); Ob-from-defender was ruled 2026-08-15 and is unbuilt
  (`HANDOFF_PC.md:24`);
- no fourth band (H-98 (1) — forbidden, not missing); the band edge is a literal
  (`ladder.py:133-135`, position 8b);
- the `partisan` polearm is present despite its deletion ruling (`weapons.py:322,852`;
  `workbench/balance.py:37`);
- Yield / §11.4 has no implementation (ED-PC-0056); Disengage is emergent (`wrapper.py:167-183`);
- grid-based map combat does not exist anywhere (`requirements.yaml:100-108`).

**Gaps on "a standing" / "a proposition":**

- `lev = 0.0` is hard-coded — there is no leverage producer;
- pool and obstacle fall to fixture defaults because `capability` is zeroed, so the outcome varies by
  seed and fixture, not by person (`requirements.yaml:538-545`);
- the obstacle has no single owner — ED-SC-0033 clause 3 is not honoured; H-127 is the nth obstacle
  site (`rosters.yaml:897-911`);
- the demote-only `BandExtension` (`degree_extension.py`) is not forwarded by `ladder.py:164` and
  cannot be carried by an engine-side provider (`_part2:111-126`);
- "a proposition" has no verb declaring it.

Its successor is the proceedings provider (position 22; PROPOSED and unbuilt; `21` PHASE 2 steps
13–16). Re-pointing the prize to it is a row change.

**Gaps on "a field":**

- `terrain=None` is hard-coded on the season path (`mass_battle.py:132`), so A7's terrain derivation
  is reached only from `mc_v18`'s `_try_conquest`; `fortification_of` (`world_q.py:371`) has no
  callers → **H-150** (garrison strength defined, never consulted; falsifier "to be written");
- `massbattle.py`'s own survivor-ratio `degree` is **not** the canonical ladder (its header; wrapper
  `:45-52`) — reconciling the two is open MB work;
- **H-148** — the casualty magnitude is an assumption (`scaled_by_degree`, swept total / none);
- **H-151** — a same-faction `march` fights itself (ABSENT_RULE); **H-152** — the `total` arm kills
  with no `person.died`;
- `march` is unreachable from the corpus chooser (no `operands_for` arm) — hand-built Acts only;
- `Faction.head` is `None` (`Tenure.degree` unread, F.4), and five `faction_q` members are unbuilt.

**Modularity:** three routes into `systems/` coexist — (i) a PATH seam (combat), (ii) a composition
role (mass battle), and (iii) engine-side reproduction (sigma; the social-contest kernel unreached).
`[MOD]` (§2.7 item 1).

### 2.5 The deprecated spine `[M5][M6]`

**`engine/mc_v18.py`** is deprecated in place (ED-IN-0226/0227) under a shrink-only ratchet. Its call
chain:

```
engine/mc_v18.py
  → composition.require('season_driver') → systems/overview/sim/season.py:81
  → engine/autoload/engine_clock.py:118 run_tick
  → composition.require('faction_action') / composition.require('accounting')
  _faction_actions_callback — carries two stubwire deferrals:
       OI-05 generate_npc (:194)  ·  OI-07 form_knot (:212)
engine/cross_scale/scene_dispatch.py   contest / fieldwork / combat-bridge dispatch (DISPATCH_COMBAT_BRIDGE flag)
engine/cross_scale/{combat_bridge, domain_echo, handoff_rules, zoom_in_out}.py
engine/autoload/{game_state (Faction.adjust, restore_world + 10 snapshot roles),
                 victory, scene_slate, season_manager, npc_ai}.py
```

**Remaining importers** (`ALLOWED_IMPORTERS`, six):

| file | retirement stage |
|---|---|
| `engine/tests/test_combat_bridge_seam.py` | — |
| `engine/tests/test_f7_smoke_oracle.py` | M6 (needs a season-side successor golden) |
| `engine/tests/test_mc_v18_regression.py` | M6 (needs a season-side successor golden) |
| `tools/balance_oracle.py` | M5 (port) |
| `tools/campaign_output_probe.py` | M5 (retire) |
| `tools/trace_execution_phases.py` | M5 (retire) |

**Composition roles whose only consumer is this spine** — 16 of 17: `faction_action, season_driver,
accounting, world_gen_settlements, snapshot_state.{practitioners, insurgencies, npcs, treaties,
convictions, beliefs, knots, territory_infrastructure, threadcut_beings, settlements},
scene_resolver.contest, scene_builder.contest, contest_side.a / .b, scene_resolver.fieldwork,
scene_resolver.investigation`. Already orphaned: `rs_track_delta`, `territory_transfer_candidate` /
`proposal` (kept named). FA-lane only: `parliamentary_vote` / `motion` / `vote_declaration`.
**Season-consumed: `mass_battle.resolve_field` only.**

**Step B** — retiring `engine/autoload/{game_state, victory, scene_slate, engine_clock}`,
`engine/cross_scale/*` and `systems/overview/sim/{season, accounting}` (39 production importers
outside tests and tools, per document 2 §1) — is separate from `mc_v18`'s own retirement, and is
gated on the loop subsuming the scale (`requirements.yaml:27-31`).

### 2.6 Pending items as dependency nodes

**Read this as a graph, not a list to work down.** Each entry names an item by its handle, the nodes
it **structurally requires to exist** (→), and the THE-NINE rows or Layer-1 nodes it serves. An arrow
records a dependency; it is not an instruction about order, and the order of entries below is the
order of their handles, nothing more. Positions are document 1 §3.2 handles; H and ED numbers are
cited where the row is the record.

#### 2.6.1 Governance · settlement · NPC (document 1 §3.2; `_part2` §8)

| handle | requires (→) and content | serves |
|---|---|---|
| `1 CLOSE-PASS` | → a fold-to-latest script (none exists) | `[none]` (a Layer-0 queue) |
| `2 RET-SC` | → a deletion set re-derived from composition roles (keeping the role-bound `parliamentary_*`); the `contest_legacy_stub.py` export ripple | R-05 / R-09 hygiene; `[MOD]` |
| `7a COMMIT-EFFECT` | → `15`, `15c`, `15b` (the BO-10 aperture: no question source offers a Proposition referent); written to G4's `Change` contract (H-137) | R-06 (ambition); the Q4 `need` producer |
| `8 H-98(b)` | the band edge moves to data (`rosters.yaml` `combat_band_edges`); (a) has no subject; shares the `kill / wound` row and wrapper with the cells commit (edge 10) | R-09 |
| `9 PC-SURRENDER` | → a build-or-strike decision (§5 item 12); PC id-block release | R-05 |
| `10 U5 stance` | → G4 (done); `tell` only; a `names_index` entry | R-07 |
| `11 U6` | → `10`; measurement at `2x3` (prior 100%); instrument `engine/reference/degree-sweep/` (moved) | R-01, R-02 |
| `11a REACH` | → G1b (done), S4; `reach`, `place_of`; deleting two question sources and `w.crossings`; `occasioned_by` one route | R-01, R-02 |
| `11b CALENDAR-EMIT` | → `11a`; observable on the `d_forced` corpus plants | R-01 |
| `12 H-62-rest` | → `12b`/`12c` (the scar rebuild is R6-atomic with the cells), G4; `axis_count` retire-or-field; `pursuits` trigger unspecified (a design gap) | R-06, R-08 |
| `12b / 12c / 12d cells` | → Jordan's cells (ED-IN-0261 R3; drafts in document 3's candidates). **One R6-atomic commit** spanning `descriptor_registry` (`pursuit_roster` 15 / `axis_roster` 7), `export_descriptors`, `descriptors.py`, three `rosters.yaml` tables, `npc_registry.yaml`, `names_index`, the verb split (`kill`, `wound`, `fight`, `challenge` → `accept`), `role_template_pursuits` validation, an audit of `npe.py` / `conviction.py`, a `(Person, conviction)` carrier, a confliction Query, and two test re-pins | R-05, R-06, R-08. `12`, `14`, H3 / H7 / H9 and arming H-146 all require it |
| `13 W28-cast` | `cast:` blocks plus a reader in `build_at` (same commit) | R-06, R-07 |
| `13d-i item (5)` | `data/offices.yaml` plus `populated.py` wiring; the fate of `titles` (r2 `03` and `05` disagree) | R-05 |
| `14 U7-own` | → `12`, `13`; antonym pairs (`repudiate`, `oblige`+waive → `release`, `succeed`+deposed, `tie/knot`+fray/loosen, `forge`, `restore`, `exchange`, `destroy_record`); the `_derive_operand` counterparty fix in the fold; `Candidate.why` reader-or-remove | R-05 |
| `15 Record-kind fold` | → `11a`, G4 (done); a `record_kinds` roster and the ⊕L35 refusal; `_eff_issue` / `_eff_petition`; deleting `World.petitions` / `dispensations`, two matrix rows and `harness/invariants.py:72`; a deposit rule | R-05. `16`, `15b`, `15c`, `7a`, `19b` and `24e` all require it |
| `16 ≡ 15a GIVE (H-84)` | → `15`; a sixth causation-bound basis and a plumbing widening in `tenure_write_basis` (decided at G3, not built) | R-01, R-05 |
| `15b LOSSY TELL` | → `15`; a WITNESS-side deposit at `Partial` plus teller identity | R-07 |
| `15c CONTENT OPERANDS` | → `15`, `16`; widens `requires_operands`; Q2's third clause | R-05 (required by `13f`'s computed form, `19`, `19b`, `24e`) |
| `17 U8 ambitions(p)` | → `13`; `person_q` | R-06 |
| `17a OBLIGEES` | → `7a`, `13e` (done); `_eff_oblige`; `_req_oblige` on `Office.binds`; `establishment_of` rewritten with a caller; `_ch_post_remit` replaced (mints `inferred`); `Office.establishment` deleted | R-01, R-05 |
| `18 PROC-A` (SC) | re-host the 28 stress tests; a real `world_q.judging_set`; `convene` corrected (a `rank` stem); `arrangements.yaml` via the one loader | R-05, R-09 |
| `18a FIELD DELETIONS` | → `17a`, `13d-i`, G3 (done), `18`; twelve fields (not `Tenure.payload`); `conferral_path` deleted, its subordination test re-pointed at `ancestry` | `[L1 ID-13]` |
| `★ APERTURE RE-MEASUREMENT` | → `18a`; per holder; needs a populated-realm instrument (none exists) | R-05 instrumentation |
| `19 U7-remit` | → ★, G3 (done), `15` / `15c`, `18`; predicates and effects for `levy`, `open_case`, `determine`, `issue` (`establish` done) | R-05 |
| `19b U7-disp` | → `15`, `15c`, the ED-IN-0210 fork (A/B) | R-05 |
| `19c MIGRATE` | → `24d-i` (done); carries `24d-ii capacity`; a presence / residence split (architecture); the `travel_leg` fix | R-04, R-05 |
| `20 U9 / R-04` | → ★; the remaining five `faction_q` members; `scale_of_rung`; 44 faction re-scales plus 10 world cases | R-04 (the headline `not_met`) |
| `21 U10` | → `20`; R3 with one owner and one denominator | R-01, R-02 instrumentation |
| `22 PROC-B` (SC) | → `18`, ★; the proceedings provider; a composed obstacle plus ceiling (M-7); prize rows re-pointed (a row change); `speak`'s four bands | R-05, R-09; closes ED-SC-0033 cl. 2/3 |
| `23 PART-E-0/2` | → `22`; typed ids; the remaining loader invariants | `[L1]` |
| `24 P1` | INERT (`body_step`); a presence-branch repair at `world_q.py:633-637`; carrier scale ← `24f` | R-04 |
| `24 P3` | CENSUS individuation; `person.demanded` from a refused `dispatch` | R-04 |
| `24d-ii CAPACITY` | → `24d-i` (done); lands with `19c`; a floor table beside `band_floors`; the birth-side consumer has no builder (document 1 §6) | R-04 |
| `24e WORKS & FOUNDING` | → `15`, `15c`, `24d-i`; a `works` Record kind; `work` advances `stage`; `_eff_restore`; `found` + `build` rows and effects (`(Rung\|Site, exists)` producers; F.20) | R-04, R-05 |
| `24f SUBSISTENCE TERRITORIAL` | → G2 (done); needs a cohort producer (`weight>1`) before the exemption candidate exists; re-opens ED-IN-0247's carrier | R-04 |
| `25 MB-GOLDEN` | — | none of THE NINE directly |
| `26 GO-VERSION` | → the Godot version ruling (ED-1051) | none of THE NINE directly |
| `27 WR-SCOPE` | → a `coherence.py` reshape | R-05 |

#### 2.6.2 mc_v18 retirement (document 2)

- **`M5`** — port `balance_oracle` to `harness/arms.py`; retire the two probes. Requires nothing
  further.
- **`M6`** — season-side successors for `test_f7_smoke_oracle` and `test_mc_v18_regression`: a
  same-seed hash pin, and a battle from a real chooser-formed decision, which requires an
  `operands_for` `march` arm (H-151's citation). → M5, M4 (done). Deleting `mc_v18.py` with a `FORK:`
  row requires M5 and M6.
- **ADJACENT:** `G2 economic pressure` (→ `6` done, `17a`; `Office.upkeep` reader versus `18a`);
  `G3 demand/delivery` (→ `15c`; queries `demanded` / `delivered`; a scarce test world); `S2` =
  `24d-ii`; `S3` = `24e`; `S4 bodies clock + individuation` (→ `24d-ii`, the `24f` cohort producer,
  ED-IN-0247); `S5 revolt / forswearing / dispensation-as-document` (→ the `verb_table.yaml:117`
  refusal); `D1-a information cluster` (→ M2 done, `15`); `D1-b narrative #1/#2/#3/#6/#7/#10/#11`;
  `D2 offices_draft.yaml` (570 rows, unverified → `13d-i` item 5); `Step B`.

#### 2.6.3 Decision layer (document 3)

`H3 scar counts` → H6. `H6+H8 landing` → C1 + C2. `H7 faith-pair falsifier` → H6 (and C2 placing the
pair). `H9 crisis threshold 2` → H3, H6. `H10 affiliation plumbing` → C3. `H11 conviction-track
scars` → H3, H10, C4. `H12 precedence` → G-Q5. `H13 threshold 3 + threshold 1 mechanism` → G-Q6.
H-80, the general operand channel, remains: each new contested verb needs a per-verb typed-cell
workaround.

#### 2.6.4 Subsystem lanes

Mass battle, social contest / proceedings, personal combat, and the FA / SE / WR / FI / GO lanes are
listed with their subsystem in §3.

### 2.7 Modularity concerns `[MOD]`

1. **Three different mechanisms reach `systems/`** (§2.4): a PATH seam (`pc_engine.py`, shrink-only),
   a composition role (`mass_battle.resolve_field`), and engine-side reproduction (`sigma.py` copying
   `resolver.py:302`; the social-contest kernel is unreached). `04:679-684` licenses "resolved by
   string at boot"; `PATH_SEAM_ALLOWED` is the exception, not the rule.
2. **These subsystem trees have no composition role consumed from `engine/season/`**:
   `systems/social_contest`, `systems/fieldwork`, `systems/threadwork`, `systems/characters`, and
   `systems/{factions, settlements, world, overview}`. The 16 roles that reach them are consumed by
   `mc_v18`, `engine_clock`, `game_state` and `scene_dispatch` (§2.5). Reaching fieldwork from the
   season loop would need a new role, a provider and a degree producer — and `rosters.yaml:482-508`
   currently forbids a prize for it.
3. **`seam/wrappers/sigma.py` is an engine-side provider standing in for a subsystem**
   (`interim: true`), and therefore cannot carry the subsystem's veto (`degree_extension.py`); the
   obstacle is derived at the seam (H-127), against ED-SC-0033 clause 3.
4. **A retire-set subsystem is coupled to the season roster's substrate.**
   `systems/world/sim/npe.py:102,284,287,332` and `systems/characters/sim/conviction.py:59,205` read
   `engine/substrate/descriptors.CONVICTIONS` directly — a shared object pinned by
   `test_conviction_roster_single_owner.py:52-55`.
5. **Apparatus reads a roster the game no longer reads.** `harness/populated.py` still calls
   `title_domain` / `titles` — the world-generation reader kept after `13d-i` deleted the predicates.
6. **A second copy of a rule.** The `openers:` roster is a hand-maintained copy of the `_eff_*` opener
   bodies (`CLAUDE.md` §8, "every rule lives once").
7. **A write outside the gate.** `World.remove_person` mutates outside `World.write` (observed by F3
   as a cascade, never gated by step); it is used by `_eff_kill` and `_eff_march`.
8. **The balance instrument sits on the deprecated spine.** `tools/balance_oracle.py` patches
   `mc_v18` / `dice_engine` and cannot reach `engine/season/` (H-148's citation).
9. **`faction_q` is a fourth `queries/` module** against `04 §A.2:132`'s three — recorded in code,
   with `04` deliberately unedited.
10. **A dead-import hazard.** `engine/reference/degree-sweep/` (a moved instrument) reads a read-only
    `S` aggregate off `loop/driver.py`'s import list; the hazard is recorded in the driver docstring.

### 2.8 Nodes with no path to mattering — legacy and orphaned

**Composition roles with no consumer:** `rs_track_delta`, `territory_transfer_candidate`,
`territory_transfer_proposal` (kept named).

**Stub modules reached by no live role:** `systems/overview/sim/{ip_track, rs_track}.py`;
`systems/world/sim/{miraculous_event, restoration_movement}.py`; the six faction-unique-action stubs
(§3.4); `systems/characters/sim/companion.py`; `systems/fieldwork/sim/{fieldwork, investigation}.py`
(stub-wired to a dead dispatcher); `systems/threadwork/sim/rendering.py`.

**Code-free subsystem folders:** `systems/npcs`, `systems/_architecture`, `systems/ui`,
`systems/victory`, `systems/articulation` — zero `.py`, reference only. (Note that
`systems/_architecture/reference/scale_transitions_v30.md` is the CANONICAL scale spec R-04 is
measured against, `requirements.yaml:32-63`.)

**An export-only file:** `contest_legacy_stub.py` — zero code callers; referenced only by exports.

**Workplan files:** `workplans/valoria_master_workplan_v6.md` (superseded; retirement deferred on
`ED-IN-0071`'s path citation); `workplans/return_to_game_queue.yaml` (self-declared superseded);
`workplans/README.md` (DEAD per document 1 §1.2); `workplans/workplan_v6_progress.yaml` (the board
read by `m1_acceptance.py` row 4 — bookkeeping, not evidence).

**Declared-but-unread fields and dead code paths:** `Rung.judging_set_rule`;
`Rung.stake / transmission / dates / sites / records`; `Site.drawers`; `Office.dates / scope_rung`;
`Office.upkeep` (∅); `Office.establishment` (∅); `Tenure.degree` (unread); `Person.coherence?`
(unread); `Candidate.why` (unread); `world_q.occasioned_by`'s dead guard;
`question_sources.{date_due, band_crossed}` (zero questions); `w.crossings`.

### 2.9 Instruments and guards — the apparatus

**Milestone and requirement instruments.**

- `python -m engine.season.harness.register --requirements` — counts hand-written `status:` values
  that carry a validated `measure:`.
- `python -m engine.season.harness.corpus_run` — prints R3, `WHERE THE 39 GO`, `unrepresentable
  scales:` and `RANKING DISCRIMINATION`.
- `tools/m1_acceptance.py --summary` — rows 1–3 run the head; row 4 is doc-derived.
- `python -m engine.season.harness.headless`; `harness.populated 1`; `conviction_spread.py`;
  `wd_acceptance.py` / `wd_chunk.py` (`engine/reference/degree-sweep/`).
- `register --check` / `--counts` — the hole register, R0–G11.

**CI** (`.github/workflows/valoria-ci.yml`): `syntax-check`; `validators` (blocking — including
`broken_dependency_checker`, `ci_sim_fabrication_check`, `ci_golden_modes_check`,
`validate_ed_citations`); `validators-report`; `unit-tests`; `sim-regression` (blocking; `engine/tests`,
and the social-contest kernel's only live exercise); `field-goldens` (byte-exact MB modes);
`lanchester-signature` (report-only); `compliance-check`; `ci-summary`.

**Exporters with a `--check` round-trip:** `tools/export_composition.py` → `composition.json`;
`tools/export_descriptors.py` → `descriptors.json`; `tools/export_sim_params.py` → `sim_params.json`;
`tools/export_npc_roster.py`.

**Local gate:** `tools/valoria_local.py --staged`; the lane validator; `tools/pathres.py` over
`references/restructure_ledger.md` (`FORK:` rows; the `test_forked_status.py` ceiling).

**Registers that are mechanism** (code reads them):

| register | shape as read |
|---|---|
| `engine/season/requirements.yaml` | fails on `met` without `measured:` |
| `engine/season/hole_register.yaml` | 152 rows; R0 row shape |
| `engine/season/write_matrix.yaml` | 39 rows; `matrix_rows_without_a_field()` |
| `engine/season/verb_table.yaml` | 39 verbs |
| `engine/season/rosters.yaml` | 48 top-level keys |
| `references/module_contracts.yaml` | `composition_roles`; the `mass_battle` contract has `state: []` |
| `references/descriptor_registry.yaml` | the descriptor rosters (`conviction_roster`, count 13) |
| `references/id_reservations.yaml` | IN `next_free: 280`; MB 76; PC 58 (exhausted); SC 39; FI 10 |

---

## 3. Subsystem-by-subsystem analysis

Each subsection answers the same five questions: **what the subsystem is**, **how complete its code
is**, **how — if at all — the season loop reaches it**, **its exact stub and gap inventory**, and
**its own open items**. The head itself (`engine/season/`) is analysed module by module in §2.2 and
is not repeated here; §3.8 covers the engine code outside the head.

A distinction runs through every subsection and is worth stating once. A subsystem can be
**complete as a standalone simulation** and still **matter to the game not at all**, because the game
is the season loop and the loop reaches a subsystem only through a contest prize and its provider
(§2.4). Completeness and reach are separate columns.

| subsystem | `.py` | code completeness | reached from the season loop? | route |
|---|---|---|---|---|
| personal combat | 29 | full headless duel sim; zero stubs `(audit)` | **yes** | PATH seam, prize "the body" |
| social contest | 20 | kernel real; only the `agon` venue live; several stub rows | **no** | engine-side reproduction of one line, prize "a standing" |
| mass battle | 35 | most active lane; one real stub `(audit)` | **yes** | composition role, prize "a field" |
| grand-strategy cluster | 40 | spines real; ten stubs `(audit)` | **no** — via `mc_v18` only | 16 spine-only composition roles |
| characters | 5 | of the three modules named, two real, one stub `(audit)` | **no** | snapshot roles ⇐ `game_state` only |
| fieldwork | 5 | two of three modules entirely stubbed | **no** | stub-wired roles ⇐ `scene_dispatch` ⇐ `mc_v18` |
| threadwork | 9 | six substantially real; `rendering.py` hollow | **no** | snapshot roles ⇐ `game_state` only |

(The grand-strategy count is the sum of its four trees as read: factions 18, settlements 8, world 6,
overview 8.)

### 3.1 Personal combat — `systems/combat/combat_engine_v1/`

**What it is.** A fully implemented headless duel simulator: 29 `.py` files, 15 of them core modules
`(audit)`, with zero stubs `(audit)`. It is one of the three subsystems retained by ED-IN-0204, and
its own head and the holonic doctrine govern it — **not** `04_CODE_ARCHITECTURE.md`, whose scope is
`engine/season/` (`_part2:21-25`). Note the naming hazard `CLAUDE.md` §4 records: despite the `_v30`
convention elsewhere, the live combat head is this unsuffixed directory.

**How it is reached.** This is the only subsystem the head reaches through a `sys.path` seam. The
contested verb `kill / wound` names the prize "the body" (module `personal_combat`, provider
`personal_combat`). `seam/wrappers/combat.py:106` calls into `engine/substrate/pc_engine.py`, which is
the single entry in `PATH_SEAM_ALLOWED` — the only licensed `sys.path` seam in `engine/`, and
shrink-only — and that reaches `systems/combat/combat_engine_v1/wrapper.fight`. The fight's
`WoundTracker` yields a `wound_state`, which `seam/ladder.py::degree_of` maps through
`combat_degree` onto the bands Felled / Wounded / Untouched, and the degree drives `kill / wound`'s
degree-keyed `body` write (Felled / Wounded). So a personal-combat roll does execute inside a season — but only for
`kill / wound`, the one contested verb whose prize this is.

**Completeness.** As a simulator, complete. As a *game-facing* mechanism, it has gaps at the seam
rather than inside the sim:

- **The obstacle is fixed.** `DECISIVE_OB=3` (`core.py:79-83`). Ob-from-defender was ruled
  2026-08-15 and is unbuilt (`HANDOFF_PC.md:24`). The `RULINGS` dict in
  `test_degree_ladder_single_owner.py` carries that ruling.
- **The band edge is a literal** at `ladder.py:133-135` (position 8(b); H-98(b) moves it to a
  `rosters.yaml` `combat_band_edges` entry). There is no fourth band, and that is by ruling —
  H-98 (1) records it as *forbidden*, not missing. H-98(a) has no subject.
- **`partisan` survives its deletion ruling** at `weapons.py:322,852`, and is referenced from
  `workbench/balance.py:37`.
- **Yield / §11.4 has no implementation** (ED-PC-0056). Disengage exists only emergently
  (`wrapper.py:167-183`). Position 9 (PC-SURRENDER) records that this requires a build-or-strike
  decision (document 1 §5 item 12) and releases the PC id block.
- **Grid-based map combat does not exist anywhere** in the tree (`requirements.yaml:100-108`).

**Its own open design items.** The channel-leverage residual (Phase 4c); Phases 4a, 4b and 5; WS-7,
multi-combatant (ED-911); the E-series calibration residues (ED-PC-0047, ED-PC-0049–0055);
ED-PC-0003 OPT-10; the ED-PC-0013 bundle; ED-PC-0016 (half-sword); and the R2 reach-class finding.

**Lane administration.** The PC id block is exhausted (`id_reservations.yaml:124`, `next_free: 58`).

**Structural couplings to other nodes.** Position 8 shares the `kill / wound` row and wrapper with the
cells commit (`12b/12c/12d`), whose verb split replaces `kill / wound` with `kill`, `wound`, `fight`
and `challenge` → `accept` — ruled, with no rows yet (ED-IN-0261). The live disagreement about whether
that rename rides the cells commit or lands standalone is §1.2 item 4.

**Bears on:** R-05 (a verb that executes), R-09 (a probabilistic chain that runs).

### 3.2 Social contest — `systems/social_contest/sim/`

**What it is.** Twenty `.py` files: the `contest/` kernel — fourteen modules: `resolver, wrapper,
modes, primitives, rhetoric, appraise, armature, contract, degree_extension, dictionaries, faction,
narrative, policy, agon_harness, _kernel_tests` — plus `parliamentary_vote.py` and
`parliamentary_stay.py`. It is a retained subsystem (ED-IN-0204), but ED-SC-0033 clause 2 rules its
kernel for retirement, in favour of a proceedings subsystem that does not yet exist as code.

**How it is reached — it is not, from the season loop.** This is the defining structural fact about
the subsystem. The contested verb `tell` names the prize "a standing" (module `social_contest`,
provider `sigma_leverage`, `interim: true`). But that provider, `seam/wrappers/sigma.py:128`, is
**engine-side**: it imports nothing from `systems/`, and instead reproduces the single line at
`systems/social_contest/sim/contest/resolver.py:302` (`roll_net + net_boost`) using
`engine/autoload/{dice_engine, sigma_leverage}.py`. The kernel itself runs in only two places:

- via `mc_v18` → `engine/cross_scale/scene_dispatch.py:288-339`, through the composition roles
  `scene_builder.contest`, `scene_resolver.contest` and `contest_side.a` / `.b`; and the
  `parliamentary_*` modules via roles consumed from `systems/factions/sim/{parliamentary_transfer,
  parliamentary_action}.py`;
- in CI's blocking `sim-regression` job, which is the kernel's only live exercise.

**Consequences of the engine-side route**, all recorded as gaps on the seam (§2.4):

- `lev = 0.0` is hard-coded — there is no leverage producer anywhere;
- the pool and obstacle fall to fixture defaults, because `capability` is zeroed on every corpus
  person, so the contest's outcome varies by seed and fixture rather than by who is contesting
  (`requirements.yaml:538-545`);
- the obstacle has no single owner — ED-SC-0033 clause 3 is not honoured, and H-127 records the nth
  obstacle site (`rosters.yaml:897-911`);
- the kernel's demote-only `BandExtension` (`degree_extension.py`) is not forwarded by `ladder.py:164`,
  and an engine-side provider structurally cannot carry it (`_part2:111-126`) — the subsystem's veto
  over the degree is lost in transit;
- the second prize row served by this provider, "a proposition" (`rosters.yaml:912-916`), has no verb
  that declares it.

**Completeness of the code itself.** Only the `game='agon'` venue route is live. The consensus,
negotiation and inquiry rows are stubs (`wrapper.py:555-556` `(audit)`), and several venue scaffolds
exist (`modes.py:308` `(audit)`). `contest_legacy_stub.py` has zero code callers but is referenced by
`engine/engine_params/sim_params.json` and `value_pointer_links.json`, so deleting it moves an
export.

**The retirement and its successor.**

- **Retirement (position 2, RET-SC).** ED-SC-0033 clause 2 is ruled and unexecuted; the tracked set is
  28 files (`git ls-files`). `HANDOFF_SC.md:14` narrows the deletion set to the kernel plus
  `contest_legacy_stub.py`, keeping the role-bound `parliamentary_*`. The deletion set requires being
  re-derived from composition roles, and carries the `contest_legacy_stub.py` export ripple.
- **The successor (proceedings) is unbuilt.** It exists as prose
  (`proposals/2026-09-05-proceedings-subsystem/`, PROPOSED, held back in full, `ED-SC-0033..0035`)
  and as a standalone stress harness whose tracer target,
  `proposals/2026-09-01-season-loop-tests/tracer/shape.py`, does not exist (position 18(a)).
  `arrangements.yaml` is absent. `world_q.judging_set` is a STUB that raises. Re-pointing the prize
  rows to a proceedings provider would be a row change (position 22).

**Execution state of the proceedings build** (`21_RECONCILIATION.md`; detail in §1.1 document 7).
PHASE 0 executed — M-7 measured `p_success` 0.0006 at Ob 3 at the 1D floor, and the σ-reach remedy
refuted (`:442-472`). PHASE 1 is mostly executed: the predicate half of step 1 (PR #379), step 2
(ED-IN-0205), step 3 (R8.1, PR #432), and part (c) of step 4's `told_by` (`witness.py:369-371`);
step 5's ledger cap now evicts nothing (`:553`). PHASE 2 is open apart from step 8 (`release`) and
step 11's gate half (the conferral clause in `state/gate.py::tenure_write_basis`). PHASES 3 and 4 are
open.

**Open items, in full:**

- `told_by` parts (a) and (b) — the precedence walk and the document/remit source map;
- the 3×3 ledger cap (step 5);
- PHASE 2 steps 6, 7, 9 (a `rank` stem in `data/requires.py`), 10, and 12–16 (the provider);
- PHASE 3 (steps 17–21) and PHASE 4 (steps 22–27, including `Tenure.term`);
- D-6 / D-7 — the `speech_kinds` roster default (`19_PLAN.md:952-960`);
- ED-SC-0038 — per-matter versus single-margin;
- RET-SC (position 2);
- the M-7 remedy — whose status two live surfaces disagree on (§1.2 item 3);
- position 18 (PROC-A): re-hosting the 28 stress tests, a real `judging_set`, `convene` corrected with
  a `rank` stem, and `arrangements.yaml` through the one loader;
- position 22 (PROC-B), which requires 18 and ★: the proceedings provider, a composed obstacle with a
  ceiling (M-7), the prize-row re-point, and `speak`'s four bands — and which would close ED-SC-0033
  clauses 2 and 3.

**Record defect:** `HANDOFF_SC.md:13`'s step numbering does not match `21`'s (§1.2 item 7).

**Bears on:** R-05, R-09 — via proceedings, not via this code.

### 3.3 Mass battle — `systems/mass_battle/sim/`

**What it is.** Thirty-five `.py` files, and the most active lane in the repository. It has one real
stub, `altonian_reinforcements.py:21` `(audit)`. It is retained (ED-IN-0204), and `orchestration.py`
is a 2,899-line god-file (ED-1043).

**How it is reached — two routes.**

1. **The season path (new at `ecacb57`).** The contested verb `march` names the prize "a field"
   (module `mass_battle`, provider `mass_battle`, `step: ENCOUNTER`, `declares: Declared`). RESOLVE
   emits a `Declared` Event; ENCOUNTER re-runs `_contest` on it. The provider
   `seam/wrappers/mass_battle.py:83` calls `composition.require("mass_battle.resolve_field")`, bound in
   `references/module_contracts.yaml`'s `composition_roles` and exported to
   `engine/engine_params/composition.json`, which resolves to
   `systems/mass_battle/sim/massbattle.py:344 resolve_field(w, side_a, side_b, *, terrain=None, rng)`.
   The sides are built by `loop/sides.py::sides_of`: the actor's muster at the origin
   (`world_q.mustered`), and the target's holder faction (`world_q.holder_faction_of`) resolved through
   `faction_q.resolve(...).members` intersected with those present. The degree comes back through
   `field_degree` (Declared / Won / Lost / Unopposed), and the `ENC` cells write `body` keyed on
   Won / Lost, scaled by the H-148 `field_casualty_model`. `mass_battle.resolve_field` is the **only** composition role
   the season loop consumes.
2. **The deprecated path.** `mc_v18`'s `_faction_actions_callback → faction_take_action →
   _try_conquest → resolve_mass_battle` (`massbattle.py:99-146`).

**What the season path does not yet do.**

- **Terrain is not passed.** `terrain=None` is hard-coded (`seam/wrappers/mass_battle.py:132`), so the
  A7 terrain derivation — reading `valoria_geography_v30.yaml` via `terrain.py` with a caller-supplied
  `fort_level` (a second-owner defect there was fixed) — is reached only from `mc_v18`'s
  `_try_conquest`. A7's UPHILL, WALLS, NARROW_PASS and RIVER_CROSSING rows are identified and not
  mechanically applied on either path.
- **Garrisons are defined and never consulted.** `ecacb57` seeds `s_*_garrison` Sites per settlement
  (`harness/populated.py:396-414`), but `world_q.fortification_of` (`world_q.py:371`) has no callers —
  H-150, with its falsifier "to be written".
- **Two degree notions.** `massbattle.py`'s own survivor-ratio `degree` is not the canonical ladder
  (its header; wrapper `:45-52`).
- **Casualty magnitude is an assumption** (H-148: `scaled_by_degree`, swept total / none).
- **H-151** — a same-faction `march` fights itself (ABSENT_RULE). **H-152** — the `total` casualty arm
  kills with no `person.died`, because `World.remove_person` bypasses the gate (§2.7 item 7).
- **`march` is unreachable from the corpus chooser.** `operands_for` has no `march` arm, so battles on
  the season path come only from hand-built Acts. M6's successor golden requires that arm.
- **`Faction.head` is `None`** (`Tenure.degree` unread, F.4), and five `faction_q` members are
  unbuilt.

**Executed from the 2026-09-25 synthesis (document 4).** A1, A2, A4, A6 (ED-MB-0069); A3 with C5
(ED-MB-0073); A7 (ED-MB-0074, corrected); A8 (ED-MB-0071, `ROUT_CASCADE_FRAC` 1.0 → 0.6); C4
(ED-MB-0072); d.1 (`_faction_to_unit` morale from `Faction.Sta`).

**Open items, in full:**

- Part A remainder: **A5** (role instincts), **A9** (causes on trace rows, conditional);
- the six "Sequenced" rows: per-cell Q; army-scale envelopment — today `run_multi_unit_battle` runs
  isolated pairs and a 2v1 stub (`orchestration.py:2662-2673, :2745-2749`); a generated map; AI
  generals; headless duels (whose stated blocker, no provider, is now stale — §1.1 document 4); and
  the owner of strategic outputs;
- **Part D C2/C3** coupling (ED-MB-0075, `needs_jordan`) — `_charge_shock_sigma` at
  `orchestration.py:1165/1171` is what it would replace;
- ED-MB-0039 (the envelopment fork); ED-MB-0041 Tier-3 (depth cap, cavalry refusal, Command σ-ceiling,
  yield split); ED-MB-0045 (CEV naming, 2:1 targets);
- `module_contracts.yaml:636` declares the contract `state: []`;
- `config.py:315-317` — a comment that disagrees with its default;
- the R3 gauge never engages (`gauge_mb.py:330-331`, ED-MB-0044);
- dead primitives `_octagon_dmg_mod`, `_SHAPE_BUILD`, `provenance.py` and
  `resolve_internal_collisions` (ED-MB-0057; the last re-adjudicated DELETE);
- position 25, MB-GOLDEN (ED-MB-0061 superseded; ED-MB-0016 open, `needs_jordan: false`);
- garrison → outcome (H-150); survivor-ratio versus the ladder; the A7 rows; terrain on the season
  path.

**Lane administration.** MB `next_free: 76`.

**Bears on:** R-04 (a scale that differs), R-05, R-09.

### 3.4 The grand-strategy cluster — factions, settlements, world, overview

**What it is.** Four trees in the retire-set (`requirements.yaml` `scales:`, `in_loop: false`). They
hold the strategic layer of the old design — faction actions, settlement registries, world events and
the season/track accounting — and they run **only** through the deprecated `mc_v18` spine. No
composition role consumed from `engine/season/` reaches any of them except
`mass_battle.resolve_field` (which lives in mass battle, not here). `[MOD]`

**`systems/factions/sim/` (18 `.py`).**

- *Real:* the spine — `faction_action.py`, the `accounting`-adjacent code, `parliamentary_action.py`
  and `parliamentary_transfer.py` (both composition consumers, and the route by which the
  social-contest `parliamentary_*` modules run), `crown_initiative.py`, `tribunal.py`, `treaty.py`,
  `absolution.py`, `council_solmund.py`, `excommunication.py`, `mass_seizure.py`.
- *STUBS* `(audit)`: `charter_liberties.py`, `hafenmark_equipment.py`, `home_sanctuary.py`,
  `infrastructure_reclamation.py`, `varfell_mandate_action.py`,
  `varfell_territorial_acquisition.py` — the six faction-unique-action stubs.
- *Open FA items:* the score/2 three-site disagreement between `parliamentary_transfer`, `tribunal`
  and `crown_initiative` (`test_faction_obstacle_conventions.py`; `HANDOFF_FA`); ED-FA-0002, 0003,
  0008 and 0021; the round-2 dockets.

**`systems/settlements/sim/` (8 `.py`).** `registry.py` (role `world_gen_settlements`),
`infrastructure.py`, `temperaments.py`, `adjacency.py`, `ledger.py` and `settlement.py` — all real.
`valoria_geography_v30.yaml` lives here and is A7's terrain source. *Open SE items*
(`HANDOFF_SE`): `24d-ii`, `24e`, ED-SE-0052/0053 held back, H-62, D6, and MW-11 / MW-5 red. Note that
the season loop's own settlement mechanism is not this code: hearths, `dwelling` Sites (211 minted),
garrison Sites and the subsistence draw at `nearest_store` all live in `engine/season/`.

**`systems/world/sim/` (6 `.py`).** `npe.py` is REAL and reads `descriptors.CONVICTIONS` directly
(`npe.py:102,284,287,332`) — a coupling to the season roster's substrate that the cells commit must
audit (document 3 H6; §2.7 item 4). `insurgency_pipeline.py` is present. *STUBS* `(audit)`:
`miraculous_event.py`, `restoration_movement.py`. *Open WR items* (`HANDOFF_WR`): position 27.

**`systems/overview/sim/` (8 `.py`).** `season.py` (role `season_driver` — the old spine's season
entry, `season.py:81`), `accounting.py` (role `accounting`), `ms_track.py` and `ci_track.py` are real.
*STUBS* `(audit)`: `ip_track.py`, and `rs_track.py` (role `rs_track_delta`, with no consumer since
ED-IN-0232).

**The season-side successor surface.** The whole cluster's successor inside the head is position 20
(U9 / R-04): the `faction_q` queries, `scale_of_rung`, and 44 faction re-scales plus 10 world cases.
Of that surface, **only `faction_q.resolve` exists.** `holdings`, `purview`, `superiors`,
`subordinates` and `at_war` are unbuilt; `head` returns `None`. Position 20 requires ★ (the aperture
re-measurement); ★ in turn requires `18a` and a populated-realm instrument, which does not exist. The retirement of
`season.py` and `accounting.py` themselves belongs to Step B, gated on the loop subsuming the scale
(`requirements.yaml:27-31`).

**Bears on:** R-04 — every tree here is that row's **subject**, and none is on its season-side path.
The `mc_v18` callers are `[M5][M6]`.

### 3.5 Characters — `systems/characters/sim/`

**What it is.** Five `.py` files. `beliefs.py` and `conviction.py` are REAL; `companion.py` is a
STUB `(audit)`.

**How it is reached.** Through the roles `snapshot_state.beliefs` and `snapshot_state.convictions`,
consumed only by `game_state.restore_world` on the deprecated spine. The season loop never reaches
this code. `conviction.py:59,205` reads `descriptors.CONVICTIONS` directly — the same substrate
coupling as `npe.py` (§2.7 item 4).

**Where the character mechanism actually lives.** The season-side character mechanism is inside the
head: `engine/season/decision/` (questions, options, choose, budget), `data/pursuits.py`, `data/cast.py`
and the `Person` carrier. So for R-06, the gaps that matter are there, not in this tree. They are,
from §2.2:

- `capability` is zeroed on every corpus person, and no season writer exists (F.6 — a `practice` verb,
  unbuilt anywhere);
- `pursuits` has no act that writes it (H-62), and the matrix row's trigger is unspecified;
- `scar[axis]` is INERT and ruled the wrong shape (ED-IN-0261);
- `axis_count[axis]` is a matrix row with no field;
- `stance[]` is written only at construction;
- `role_template_pursuits` reads through a non-raising `to_axes` (the silent data-loss hazard);
- the cells (`12b/12c/12d`), `12`'s producers, `13`'s cast, `17`'s `ambitions(p)` and the decision
  layer's H3–H13 are all unbuilt; ED-IN-0214's correlation is superseded into the cells.

**Bears on:** R-06 as subject; the `systems/characters` code itself is `[none]` for the season loop.

### 3.6 Fieldwork — `systems/fieldwork/sim/`

**What it is.** Five `.py` files. `fieldwork.py` (`run_fieldwork_scene`, `advance_disposition`,
`advance_evidence`) and `investigation.py` (`resolve_npe_response`, `evaluate_dialogue_lattice`,
`apply_response_matrix`) are **entirely stubbed** `(audit, confirmed by function list)`. `knots.py`
is real enough to back the role `snapshot_state.knots`.

**How it is reached.** The roles `scene_resolver.fieldwork` and `scene_resolver.investigation` are
consumed by `engine/cross_scale/scene_dispatch.py`, which marks them "stub-wired pending ED-916", and
that dispatcher is reached only from `mc_v18`. **The season loop never reaches this code.**

**What the season loop has instead.** The six investigation verbs — `examine, interview, research,
surveil, thread_read, reconstruct` — exist as `writes: []` rows: witness-only, with no `_eff_*` and no
degree producer (ED-FI-0009 item 4.5). Of those, `interview`, `reconstruct`, `research` and `surveil`
execute in the corpus; `examine` is always refused (no Site question); `thread_read` is unrepresentable
in the typed grammar (H-85).

**What would have to exist for this code to matter to the loop.** A new composition role and
provider, and a degree producer — and `rosters.yaml:482-508` currently rules the seam UNRULED and
forbids a prize for it. `[MOD]`

**Open FI items** (`HANDOFF_FI`): ED-FI-0009 (the degree producer), ED-FI-0002, ED-914. FI
`next_free: 10`.

**Bears on:** R-05 as subject; the code itself is `[none]` today.

### 3.7 Threadwork — `systems/threadwork/sim/`

**What it is.** Nine `.py` files. `co_movement`, `coherence`, `collective`, `operations`, `opposing`
and `threadcut` are substantially real `(audit)`.

**The hollow module.** `rendering.py` is a "wired" stub that imports only
`engine.substrate.stubwire`, with zero import of `rs_track.py` or `ms_track.py` — so
`apply_rs_strain` and `check_calamity_threshold` are hollow (`HANDOFF_WR.md:9`; the two `rendering.py`
stubs).

**The model is out of date.** `coherence.py` still implements the depleting-track model that
`canon/philosophy/RULINGS.md` replaced. Reshaping it is position 27 (WR-SCOPE), with ED-WR-0010 in
scope.

**How it is reached.** Through the roles `snapshot_state.practitioners` and
`snapshot_state.threadcut_beings`, consumed only by `game_state`. Its only season-side hook is the
`Person.coherence?` field, which is carried and unread (F.5). `[MOD]` — no season route.

**Bears on:** none of THE NINE today; R-05 only if position 27 builds.

### 3.8 The engine outside the head — substrate and deprecated spine

**The substrate** is shared by both spines: `engine/autoload/dice_engine.py` (which owns
`degree_from_net` — the canonical degree bands, superseding `params_tables.yaml`'s frozen capture,
per `CLAUDE.md` §5) and `sigma_leverage.py`; `engine/substrate/{composition, descriptors, pc_engine,
stubwire, names, canon_buckets, world_initial_state}.py`; and the exported JSON under
`engine/engine_params/`. `composition.py` is how `engine/` names a role without naming a subsystem;
`descriptors.py` holds `CONVICTIONS`, read both by the head and, directly, by two retire-set modules
(§2.7 item 4); `pc_engine.py` is the one `sys.path` seam; `stubwire` is the deferral mechanism the
hollow modules import.

**The deprecated spine** (§2.5) — `engine/mc_v18.py`, `engine/autoload/{engine_clock, game_state,
victory, scene_slate, season_manager, npc_ai}.py` and `engine/cross_scale/*` — is the only thing
that runs the retire-set subsystems, the social-contest kernel's scene dispatch, and the balance
oracle. It carries the OI-05 / OI-07 stubwire deferrals. It is deprecated in place with a shrink-only
importer ratchet (six importers remain), and it is `[M5][M6]` throughout.

---

## 4. Reverse index — THE NINE → the nodes each row rests on

`engine/season/requirements.yaml` defines THE NINE. This index goes from a row to the exact nodes it
rests on, using the handles and hole numbers defined above. It lists what each row depends on; it does
not rank them.

| row | status | the nodes it rests on |
|---|---|---|
| **R-01 propagate** · **R-02 affect later decisions** | not_met | W-F cross-person transmission: `10` stance, `15b` lossy tell, `17a`'s inferred channel, `16` Record movement / H-84, `11a` / `11b`. H-111 (refusal as news). H-116. The U6 / U10 instruments (`11`, `21`, the R3 denominator). Fan-out `all_five` (done). `told_by` / `seen` (partial). **Structural theorem:** `opening_set` reaches the world only through ledger claims |
| **R-03** | met | the U2 rounds loop — no open nodes |
| **R-04 differing scales** | not_met | `20` (`faction_q` ×5, `scale_of_rung`, 54 re-scales); `19c` + `24d-ii`; `24e`; `24f` + a cohort producer; `24 P1` / `P3`; CENSUS producers; `march` / ENCOUNTER (done, hand-built Acts only); `faction_q.resolve` (done); Step B; W10 / W13 corpus authoring. Every retire-set subsystem in §3.4 is this row's SUBJECT, and none is on its season-side path |
| **R-05 all verbs** | not_met | every row of the §2.2.5 verb table below "execute in the corpus"; `15`, `15c`, `16`, `19`, `19b`, `14`, `24e`, `13d-i`(5), `7a`, `17a`, `18`, `22`; the verb split (the cells); H-65 (prose `requires:`); H-94 / H-80 (operands); H-75; H-85; the investigation degree producer (FI 4.5); the fieldwork and threadwork routes (§3.6, §3.7); `establish`'s computed form; the `march` operand arm |
| **R-06 characters** | partial | a `capability` writer (F.6 — a `practice` verb, unbuilt anywhere); the cells (`12b/12c/12d`); `12`'s producers; `13` cast; `17` ambitions; H-62's four rows; ED-IN-0214's correlation (superseded into the cells) |
| **R-07 memories · feelings · attitudes · relationships** | partial | `10` stance; `15b`; `told_by` (a)/(b); fan-out (done); R8.1 (done). **No feelings or relationships field exists** |
| **R-08 non-omniscient · non-rational** | partial | sampling (done); inclination breaking ties ← a dense `alignment` (the cells; H-66 / H-96); the H2 deontology gate (INERT); the `travel_leg` budget defect |
| **R-09 probabilistic chains** | partial | the σ provider (done) ← `capability` (zeroed); a `lev` producer (none); an obstacle owner (proceedings); Ob-from-defender (PC); H-98(b), the edge moved to data; the `march` field roll (done, hand-built only); H-148's magnitude |

---

*End of the snapshot. It stops here deliberately: the master plan that would turn this map into an
order is on hold by Jordan's instruction, and the single ORDER in the repository remains
`workplans/2026-09-18-governance-settlement-behaviour-plan.md` §3.*
