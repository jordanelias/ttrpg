# Valoria — Master Workplan v7 (North-Star master: milestones, the queue sorted by who can answer it, lanes)

## Status: **CANON — RATIFIED 2026-09-12 (ED-IN-0216)**, by Jordan's merge of PR #397 under `ED-1094`'s ratify-on-merge default. Supersedes `valoria_master_workplan_v6.md` (CANON 2026-07-05 → 2026-09-12, ED-IN-0009/ED-IN-0011)

> **WHAT THE MERGE RATIFIED, AND WHAT IT DID NOT.** `CLAUDE.md` §2: *"Jordan's review-and-merge IS the
> ratification — flip the `## Status:` line, the ledger `status`/`needs_jordan` fields and `CURRENT.md`
> in that same merge, not as a later step nobody triggers."* The merge did not carry those flips, so
> this is that step, triggered. **Ratified: this document as the master workplan** — §1's milestones,
> §3's sort, §4's lane pointers, §5's governance. **NOT ratified, because the PR body held each back
> loudly:** v6's **retirement** (deferred — see §6; v6 remains on disk and this supersession is of
> authority, not of the file), the **ORDER collision** between the reconciled program and the
> arc-sequence spine (open; a commit closes it, not a paragraph), and every `## Status:` line on the
> documents §6 marks superseded, none of which moves.

**as_of 2026-09-12**, working tree at `claude/repo-review-work-plans-2ly5xc` (base `main` `2d5ec4e`).
Every figure below was **measured on this tree at that commit by running the instrument named beside
it**, never copied from another document. Where a figure and its instrument disagree, the instrument
wins and this file is wrong — re-run it.

**Why a new master rather than an amendment.** v6 is dated **2026-07-05**. Between it and today the
tree ruled `ED-IN-0204` (only social contest, personal combat and mass battle retained; the season
loop adopted in full), ruled `ED-SC-0033`, dissolved `designs/`, `sim/`, `arcs/` and `deprecated/`,
moved the ledger from `canon/` to `registers/` and split it by lane, retired the SessionStart banner,
the workplan-pointer regime and `tools/workplan_status.py`, and rewrote `CLAUDE.md` §0 through §0.4.
v6's §3 workstream, §6 governance and both appendices cite trees that no longer exist. An amendment
would have left a July document wearing a September date.

**Binds (does not fork):** `references/lane_assignments.yaml` (`source:` repointed here) ·
`references/id_reservations.yaml` (allocation protocol unchanged) · `HANDOFF.md` +
`registers/handoffs/HANDOFF_<LANE>.md` (the only status surface) · `CURRENT.md` (currency authority).

`[SELF-AUTHORED — bias risk: I wrote the reconciled program this document defers the ORDER to, and I
executed the queue pass whose results §3 sorts. An independent reader should attack §3's sort hardest
— it is the section where my own prior work is the evidence. §6 names what I could not verify.]`

---

## §0 · What this document is — and the four things it does NOT own

v6's best rule, kept: **this document carries no status column.** A status written twice drifts within
days; v6 §0 proved it and this file inherits the fix. Four surfaces own what this one only points at.

| It owns | It does NOT own | Owner |
|---|---|---|
| **WHAT** the milestones are and **WHO** can answer each open question | **THE ORDER** the work is done in | `workplans/2026-09-11-reconciled-program.md` (+ `_part2`) — 27 positions, PROPOSED under ED-IN-0215 |
| the per-lane **next increment** | per-lane **status** | `registers/handoffs/HANDOFF_<LANE>.md` |
| which head a lane's work sits under | **which head is canonical** | `CURRENT.md` |
| that a milestone row reads met or not | **whether the behaviour runs** | **nothing here fully owns this — see below** |

⚠ **The two instruments are NOT execution, and an earlier draft of this table said they were.** The
distinction matters enough to spell out, because getting it wrong is how a document talks itself into
believing a milestone:

| Instrument | What it actually does |
|---|---|
| `tools/m1_acceptance.py --summary` | **Mixed.** Rows 1–3 run a seeded headless season and read the result (`M1_PROBE_SEED = 20260819`, `:80`). **Row 4 counts `state:` strings** in a hand-edited board (`:72`). The tool says so in its own output |
| `python -m engine.season.harness.register --requirements` | **Counts a hand-written `status:` string** per row in `engine/season/requirements.yaml` (`register.py:638-640`, `:680`). Nothing executes |

`register --requirements` is nonetheless **stronger than the board**, and the difference is worth
keeping rather than flattening: it refuses a row with no `measure:` command, **statically resolves that
command** — a `-k` expression must select at least one real test, a `python <path>` must name a file
that exists and has a `__main__` — and refuses a `met`/`partial` row whose `measured:` prose is empty
(`register.py:644-676`). Its own source records that the first version of that check *was* `CLAUDE.md`
§0.1 pt 2 — an assertion that could not observe the failure it excluded — and shipped two dead commands
that an adversarial pass, not the gate, caught. **So: the board is doc-derived with nothing behind it;
`requirements.yaml` is doc-derived with a validated falsifier bolted to every row; only
`m1_acceptance.py` rows 1–3 actually run the game.** Treating the second as the first is the
asymmetric skepticism `CLAUDE.md` §0.1 pt 4 names as a bias rather than a defence.

**Completeness rule, carried from v6 §0 and still binding:** every §4 lane section opens with its
`HANDOFF_<LANE>.md` pointer even where the section is thin — the pointer is what guarantees nothing is
missed, not enumeration here. A §4 entry with no handoff pointer is a bug in this document. Likewise
**every Jordan-gated row must be reachable from §3.**

⚠ **"Jordan-gated" HAS THREE SPELLINGS IN THIS TREE, AND AN EARLIER DRAFT OF THIS DOCUMENT MATCHED ONE
OF THEM.** The first cut asserted "§3 carries all 26" on the predicate
`needs_jordan: true AND status: open`. That predicate is arithmetically correct — an independent
re-derivation confirms exactly 26 — and it answers **the wrong question**, because §3's own thesis is
*who can answer it*, not *which field is set*. Three spellings exist:

| Spelling | Count | Where |
|---|---|---|
| `needs_jordan: true` **and** `status: open` | **26** | the eight lane ledgers + the flat ledger |
| `needs_jordan: true` **and** `status: ruled`, **with an open fork in the row's own text** | **1** | `ED-IN-0210` |
| `needs_jordan: true` **and** `status: proposed` | **2** | `ED-WR-0010` (held back from ratification in full), `ED-IN-0059` |
| `needs_jordan: true` **and** `status: partial` | **2** | `ED-IN-0147`, `ED-IN-0149` |
| `status: open` **and** `jordan_decision: "pending"`, **with no `needs_jordan` key at all** | **3** | `ED-1010`, `ED-1011`, `ED-932` — flat ledger only |

**Thirty-four rows carry a live Jordan-gating mark in some spelling**, and §3 routes all thirty-four.
⚠ Not all thirty-four are *rulings* — several are flagged bookkeeping that nobody unflagged, which is
what §3 exists to separate. The point is that **no single field answers "is this Jordan's?"**, so a
count taken from one field is a count of that field, not of the question. This is the same
term-versus-mechanism failure `CLAUDE.md` §8 records for `pathres.resolve`, and **the tree already held
a written record of a previous session making this exact mistake** — `workplans/workplan_v6_progress.yaml:97`:
*"⚠ ED-1010/1011 are NOT ungated: both carry `jordan_decision: pending` in the flat ledger … **The
lane-format `needs_jordan` field was checked; the flat ledger's equivalent was not.**"* It was made
again here, by me, and caught by an independent reader rather than by the count.

**What this document may not become.** `CLAUDE.md` §0.3 names the loop this repository was in: findings
become rows, rows become a start-of-session surface, that surface defines the next session's work.
A master workplan is a natural host for exactly that loop. Two rules keep it out: this file **states no
work item that is not traceable to a milestone row or a ledger row that already exists**, and it
**generates nothing** — it sorts what the tree already holds. If a future session finds itself adding
a work item here that no instrument and no ledger row produced, that is the generator, and the repair
is to delete the item, not to schedule it.

---

## §1 · Milestones — execution-bound (`CLAUDE.md` §0.2)

**`done` means the behaviour EXECUTES.** A juncture may not be marked done on a document. Every row
below names the command that decides it.

### M1 — ONE PLAYABLE SEASON

**Instrument:** `python tools/m1_acceptance.py --summary`. **Measured at that commit — verdict `NOT MET`,
2 rows failing:**

| # | Row | Today |
|---|---|---|
| 1 | Stub invocations on the M1 path == 0 | **FAIL** — 2 `stub_resolve` calls in a 1-season probe (seed 20260819) |
| 2 | Same seed → same `KeyLog.content_hash()` | **PASS** — `641aa8c55c3e…`, two independent runs |
| 3 | Every emitted key has a consumer or declared terminal | **PARTIAL** — 47 emitted · 0 declared terminal · 2 unconsumed by name (`env.crisis`, `mechanical.season_change`) |
| 4 | All M1 junctures execute | **FAIL 0/7** — blocked 1 · in_progress 4 · not_started 2. ⚠ **DOC-DERIVED** (see below) |
| 5 | N seeds, zero invariant violations | **BLOCKED** — needs a season-run invariant sweep, unwired |

#### ⚠ Row 4 is bookkeeping, not evidence — and its board is three weeks stale

Row 4 counts `state:` strings in `workplans/workplan_v6_progress.yaml`, read at
`tools/m1_acceptance.py:72`. The gate says so in its own output. Two facts make it worse than v6 knew:

- the board's `as_of` is **`{sha: c75c561, date: 2026-08-19}`** — twenty-three days old, and `main` has
  taken 20 commits since;
- its only renderer, `tools/workplan_status.py`, **does not exist**, and the
  `valoria-workplan-navigator` skill v6 §6 designated its owner was retired 2026-08-21 (ED-IN-0194).
  The board is hand-edited, unrendered and unowned, and it feeds the acceptance gate.

**It keeps its v6 filename deliberately.** `m1_acceptance.py:72` hardcodes that path; renaming it to
match this document would be a cosmetic edit to a load-bearing input, and `CLAUDE.md` §0.1 pt 5's
predicate is the reason not to. Refreshing its `as_of` and its seventeen rows against the tree is
**position 3's** work in the reconciled program, not this document's.

#### Row 1 is the real M1 blocker, and it is TWO PIECES OF UNAUTHORED CANON

Traced on this tree by instrumenting `engine.substrate.stubwire.stub_resolve` around a seeded
1-season run. Both calls fire from `_faction_actions_callback`, reached through
`composition.require('season_driver')` → `systems/overview/sim/season.py:81` →
`engine/autoload/engine_clock.py:118`:

| Stub | Site | Why it is stubbed (verbatim from the call's `reason=`) |
|---|---|---|
| `generate_npc(world-gen\|season-tick)` | `engine/mc_v18.py:194` | **OI-05** — *"investigation_systems_v30.md SYSTEM 1 Two-Tier Generation is scene-specification-driven only … no world-gen initial count and no season-tick generation trigger exist in canon to cite; NPE-02's proposed persistence-cap number is an unresolved Open Question. Honest deferral, not fabrication."* |
| `form_knot(world-gen\|season-tick)` | `engine/mc_v18.py:212` | **OI-07** — *"knots_v30.md §3.1 Prerequisites require personal-scale actor fields (Disposition, Bonds, TS) absent from the aggregate strategic World — no world-gen or season-tick formation rule exists in canon to cite."* |

**Neither is a bug and neither can be fixed by engineering alone.** They are the no-fabrication rule
working correctly: the code declined to invent an NPC-generation rate and a Knot-formation trigger that
canon does not state, and recorded the gap through `stubwire` so it is greppable rather than silent.

- **OI-05 needs a number nobody has authored** — a world-gen initial NPC count and a season-tick
  generation trigger. That is a design call. It goes to §3.1.
- **OI-07 is structural, not numeric.** Knot prerequisites read personal-scale fields off an aggregate
  strategic World. `engine/cross_scale/scene_dispatch.py`'s module docstring already names this same
  context-derivation gap for combat and contest actor derivation — so OI-07 is an instance of a known
  defect class, not a new one, and closing the class closes it. That is §3.2 work.

**Consequence for sequencing:** M1 row 1 cannot go green before OI-05 is ruled, and OI-07 rides the
cross-scale derivation work. Any plan that schedules "close the stubs" as an engineering task is
mis-scoped.

### M1's companion instrument — the nine requirements

**Instrument:** `python -m engine.season.harness.register --requirements`, scoring
`engine/season/requirements.yaml` (Jordan's nine, ruled 2026-09-05, ED-IN-0204). **Measured at that
commit: `met 1 · not_met 4 · partial 4`.**

| | |
|---|---|
| **met** | R-03 seasons tick scene-by-scene |
| **not_met** | R-01 decisions propagate · R-02 decisions affect subsequent decisions · R-04 strategic/management actions possible · R-05 all verbs built out |
| **partial** | R-06 characters built with goals/ambitions/convictions · R-07 memories, feelings, attitudes, relationships · R-08 decisions not omniscient or perfectly rational · R-09 chains of events probabilistic |

⚠ **`CURRENT.md:34` and `HANDOFF.md` both still read "6 `not_met` / 3 `partial`".** That was true for
Arc 1 and is no longer true for the tree.

**R-03 was flipped to `met` by U2.** The primary citation is the instrument's own input —
`engine/season/requirements.yaml:239-240`, R-03's `measured:` block: *"⚠⚠ **MET 2026-09-11 BY `U2`, AND
THE FLIP IS ON AN EXECUTION RATHER THAN A DOCUMENT (`CLAUDE.md` §0.2).**"* The spine says the same
independently at `:29`. `ED-FI-0009` appears in that file under R-01, R-05 and the fieldwork scale note
— **all still `not_met`** — and `ED-IN-0205`/R7 under R-07, which is `partial`. **Neither touches R-03.**

> ⚠ An earlier draft of this paragraph attributed the flip to PR #387 and PR #380, inferred from their
> position in the week's log. It was wrong, and the file that decides it says so in bold on the row.
> This is the failure `CLAUDE.md` §8 records for `pathres.resolve` — **matching a name instead of
> checking the mechanism** — and it recurred four more times in the session that wrote this document.

**The fourth `partial` is resolved, and there is no mystery in it.** An earlier draft filed a `[GAP:]`
for a row that moved `not_met` → `partial` between the spine's reading and this one. It is **R-09**, and
the cause is that the two readings were taken on different trees, not that a figure drifted: the spine
is dated 2026-09-11 and records PR #395 as **unmerged** (`:28`); `#395` merged as `c275a9b` and is the
last commit to touch `engine/season/requirements.yaml`, which is byte-identical between this branch and
`origin/main`. **So `c275a9b` carried both flips — U2/R-03 to `met` and R-09 to `partial`** — and the
spine simply measured before it landed. `[CORRECTION: the `[GAP:]` filed here is withdrawn; it was
answerable by one `git log` against the instrument's input file.]`

⚠ **Do not read `1 met · 4 not_met · 4 partial` as "four requirements now run."** Per §0, this command
counts hand-written `status:` strings. R-09's `partial` rests on a `measured:` block citing `U1`, and
the spine records **`U1/R-09` as uncommitted in the working tree** at the time it wrote that — the
status moved with a validated prose reading, not with a green test. That is a real and useful signal
and it is **not execution**; the only rows in this document backed by a running game are
`m1_acceptance.py` rows 1–3.

### M2 — THE ANY-SEED STORY BAR

v6 defined M2 against the Churn Engine's fixture F1 and its Stages 1–4. **That framing predates
`ED-IN-0204` and this document does not restate it as live.** What survives the ruling is the bar
itself — *N seeds each yield a chronicle that is connected, continuous, rooted, live and distinct* —
which is **M1 acceptance row 5 generalized**, and row 5 is `BLOCKED` on a season-run invariant sweep
that is not wired. **M2 is therefore not schedulable until M1 row 5 has an instrument.** Building that
sweep is the smallest thing that makes M2 mean anything; until then M2 is a stated goal with no gate,
and this document says so rather than tabling stages against it. `[GAP: M2 — no instrument. v6's
Stage 1–4 table is not carried forward; whether the Churn Engine workstream survives ED-IN-0204 at all
is §3.1's ruling R-7.]`

### M3 — GODOT VERTICAL SLICE

Unchanged in substance from v6 and still **last**. Its gate is `ED-1051` — 10 of 27 modules at
`doc: null` (including `engine_clock`, the temporal spine) and 11 of 27 resolvers at `[ASSUMPTION]`
grade. `CURRENT.md:34`: *"Gate-0 is blocked on ED-1051."* Two live cautions from `CLAUDE.md` §6 that
any M3 plan must carry: **the port's Godot engine version is UNRESOLVED and nothing may assert one**,
and `godot/skeleton/` covers a single module, does not compile, and `extends` a spine defined nowhere
— it is not a head start.

---

## §2 · What opened in the week to 2026-09-12

Measured by scanning every `registers/editorial_ledger*.jsonl` for rows whose **first** appearance is
dated on or after 2026-09-04 (last row per ID wins, per the ledgers' append-only semantics), and
`git log origin/main --since=2026-09-04`.

| | |
|---|---|
| ED rows opened | **23** — IN 15 · SC 5 · FI 1 · SE 1 · WR 1 |
| of those, still `open` | **7** — ED-IN-0202/0205/0208/0214 · ED-SC-0036 · ED-FI-0009 · ED-SE-0051 |
| of those, still Jordan-gated | **4** — ED-IN-0210, ED-IN-0214, ED-SE-0051, ED-WR-0010 |
| commits landed on `main` | **20** |

⚠ **The 23rd row is `ED-IN-0216`, this document's own.** A first cut printed 22 by excluding it without
saying so, which makes the figure unreproducible from the method stated above. It is counted here and
named, because a census that quietly omits its author is the same defect as one that miscounts.

**The week's shape, in one line per landing that moved a milestone row:**

- **PR #384 → `ED-IN-0204`** — the nine R-rows sequenced unit by unit; **seven planner claims
  overturned.** This is the ruling the rest of the week runs under.
- **PR #383 / #381 / #378 → `ED-IN-0203`** — the `shape.py` decomposition COMPLETE, 6,771 → 0. The
  facade is deleted and every importer names its owning module.
- **PR #386 → `ED-IN-0206`** — Arc 1 executed rather than planned: `decision/`, `seam/`, `manifest/`,
  `queries/`, `loop/`'s six steps. Content hash unchanged — what a pure structural arc should read.
- **PR #387 → `ED-FI-0009`** — six investigation acts built. Its title says verbs executing went
  6-of-32 → 10-of-37; ⚠ **that figure is already superseded** — `engine/season/requirements.yaml:301`
  reads *"**11 of 38 verbs execute in the corpus**"* and is its owner. `CURRENT.md` still carries the
  pre-#387 **6 of 32**, a second stale figure in that row beyond the requirements count.
- **PR #380 → `ED-IN-0205`** — fan-out off `total`; R7 executed in the season loop.
- **PR #391 / #389 → `ED-SE-0051`** — seven settlement/faction/population proposals, NERS pass **run
  rather than cited**; all seven scored `paper`, two do not load. Held back from ratification in full.
- **PR #388 → `ED-WR-0010`** — threadwork practical applications. Held back from ratification in full.
- **PR #390 / #392 → `ED-IN-0207` / `ED-IN-0209`** — `resolution-diagnostic` split out of `ners`; the
  `layer-conformance` skill given one method owner.
- **PR #393 → `ED-IN-0208`** — the blocking-rulings queue measured: **it is not what blocks the game.**
  §3 is the operational form of that finding.
- **PR #396 → `ED-IN-0213`** — `CLAUDE.md` §0.4: the full suite is a close step, not an inner loop.
- **PR #394 → `ED-IN-0209/0210/0211`** — renumbering to `next_free` does not escape a same-lane
  collision. Four within-lane IN collisions in two days; the structural fix stays PARKED.
- **PR #395 → `ED-FI-0009`/`ED-IN-0206`** — the R3 fall measured and attributed; the instrument
  baseline given one owner. **It also carried `2ebab0c` — U2/R-03, the one commit this week that moved
  a requirement row to `met`,** and it did so on an execution, the only flip §0.2 accepts.

**Then, in this session, PR #397 → `ED-IN-0215`:** the 27-position order, and the `needs_jordan` queue
taken from **108 open-and-flagged rows to 26** (control: the same scan against `origin/main`).

---

## §3 · The queue, sorted by WHO CAN ANSWER IT

**This is the section v6 did not have, and the reason for a v7.** v6 §5 was a *tiered Jordan-decision
register* — tiered by what a row blocks. Every row in it was addressed to Jordan. But
`ED-IN-0208` measured the queue and found the opposite: **most of it is not Jordan's.** `CLAUDE.md` §0
states the rule and the reason, Jordan verbatim:

> *"I don't believe that I need to be involved in the vast majority of pending decisions. Those
> decisions should be answerable as superseded or irrelevant, by our design documents, by precedents,
> or by whatever makes most sense for code architecture."*

So the axis here is **who can answer**, not what it blocks. All **34** Jordan-gated rows §0 enumerates —
the 26 under `needs_jordan: true AND status: open` plus the eight the `open` filter cannot see — appear
exactly once below. Tier within a bucket is the `Blocks` column.

### §3.1 · RULINGS — Jordan only (11 rows)

⚠ **Read the qualifier before the table.** An earlier draft opened *"each survived all five of
`CLAUDE.md` §0's tests"* and cited **nothing per row** — which under §0.1 pt 3 is unfalsifiable, and is
the shape of claim this session was wrong about repeatedly. What is actually true: each row below is
here because **I could not find a successor ruling, a design-document answer, or a precedent that
closes it**, and because two defensible options lead to materially different games. That is a
negative result from a bounded search, not a proof. **The closing session owes each row its citation**;
where the tree already holds a standing objection to a row, it is named in the row.

| Row | The question, in one sentence | Blocks |
|---|---|---|
| **ED-1051** | Flip `module_contracts.yaml`'s `doc: null` for `engine_clock` to `propagation_spec_v1`, or author a new home? | **M3 entirely** — Gate-0's entry condition; 10 modules and 11 `[ASSUMPTION]` resolvers behind it |
| **ED-SE-0051** | E-1 — is the demographic loop bounded by **matter only**, or **matter plus hearth capacity**? Malthus, or a Site-capacity ceiling on births. | the settlements/populations proposal set; the only question of seven that survived all five tests |
| **ED-IN-0214** | The 13×4 conviction matrix has a **dominant common direction** — convictions differentiate a person's own priorities well and different people badly. Re-cut the matrix, or accept it? | **position 11's measurement** — a late *yes* invalidates it |
| **ED-SC-0003** | The "Piety Track" name collision: one name, two referents, three docs. Which name wins for the debate tracker, which doc is its home, what does the per-territory stat become? | SC lane doc integrity; touches 127 files |
| **ED-SC-0005** | The numeric **cap** on the Recall/Corroborate/Prep/Findings bonus-die stack. Doc math reaches +8D while the genre/audience boost caps at +2D. | ⚠ **A standing objection exists and must be resolved before this is put to Jordan.** `workplan_v6_progress.yaml:81` argues via `ED-SC-0017` that the cap is already ruled and enforced in code (`sigma_leverage.py` `M_MAX = 1.5`, soft-cap at `:104,148`). It is **not** obviously the same question — `M_MAX` caps σ, this row asks for a bonus-**die** cap — and `ED-SC-0017` is itself `superseded`. Settle that before spending a ruling |
| **ED-SC-0015** | Do the parliamentary Total-Victory Mandate −1 and the Censure tier's own Mandate −1 **compound** on the same faction in one motion? Implemented as stacking by literal-faithful default. | parliamentary resolution correctness |
| **ED-MB-0008** | Two live ranged/volley Damage-Reduction tables, ~2× apart for the same armour band, neither marked superseded. Which governs? | volley resolution is undetermined for an importer or a player |
| **ED-IN-0030** | The phantom "debt scene": `scale_transitions_v30` §4.3.2 cites a mechanic that exists nowhere. **Author it, or strike the reference?** | FA/political doc integrity |
| **ED-WR-0008** | The P-25 Scale-based Mending Stability override table was **truncated at authoring** — header plus the label `Object`, zero data rows, no revision ever had them. Supply the values, or strike the override? | threadwork scale-override behaviour is unspecified |
| **ED-IN-0210** | The open fork Jordan raised alongside his 2026-09-10 verb-table rulings: **does an order carry terms?** ⚠ Row is `status: ruled` — the rulings landed; the fork did not. | `workplans/2026-09-11-arc-sequence-spine.md:57` calls this *"the one remaining node that survives all five of §0's tests. Do not schedule it until ruled."* An earlier draft of this document dropped it entirely, because its `status` filter was `open` |
| **ED-885** | `canonical_sources.yaml:579` cites ED-885 for the 2026-05-30 F-RESID migration; ED-885 was never written. **Confirm ED-874, or name the real ID.** | ⚠ **Provenance only, not code.** That line is a `#` comment, stripped by every YAML parser before a consumer sees it — an earlier draft called it a machine-read registry, which is wrong in kind |

> ⚠ **ED-885 is one sentence of Jordan's memory and nothing else.** A critic proposed closing it by
> asserting ED-874; that was refused, because ED-874 is dated 2026-05-31 and concerns the Domain Action
> resolver while F-RESID is 2026-05-30 and concerns four Unique Actions. **Adjacent is not identical**,
> and asserting the identity would put a fabricated historical fact into a registry code reads.

#### ⚠ The top M1 blocker is NOT in this table, because it has no ledger row

**OI-05** — the world-gen NPC count and season-tick generation trigger (§1) — is a **ruling Jordan owns
that was never filed as an ED.** It lives only as a `reason=` string inside a `stubwire` call at
`engine/mc_v18.py:194`. It is the single largest thing standing between the tree and M1 acceptance row
1, and it is invisible to every queue instrument in the repository. **Filing it is the first action
this document asks for.** Its sibling OI-07 is *not* a ruling and belongs in §3.2.

### §3.2 · WORK — an agent does this; no ruling required (9 rows)

These are in the queue because nobody wrote the closure down, not because they need Jordan. Each names
an engineering act with a decidable outcome. **Three rows an earlier draft put here have been moved to
§3.2a** — they were re-adjudicated into the opposite bucket, with no new evidence, hours after this
same session's antagonist overturned them. That is precisely the direction a sort must not move in:
routing a live question to an agent is how it gets answered by whoever is cheapest rather than by
whoever can.

| Row | The act | Note |
|---|---|---|
| **ED-1043** | Split `orchestration.py` (2,899 L god-file: data model + targeting + attrition authoring + volley + resolution + turn loop + I/O) | Largest single item in the queue; scope it against `architecture/` before starting |
| **ED-MB-0016** | DG-6 over-decisiveness: root cause **confirmed mathematical** — melee attrition self-averages ~1/√N, so outcomes collapse to 100%/0%. Implement per-battle CEV friction. | The diagnosis is done; only the build remains |
| **ED-MB-0044** | R3 ranged-vs-ranged never engages — a **definitional** gap, not a balance one | scope corrected by ED-MB-0045 |
| **ED-MB-0057** | Dead-primitive census: 118 built-but-unwired primitives repo-wide; MB's ten analysed | Triage, then wire or delete |
| **ED-IN-0049** | `scale_transitions_v30` §3.3 *Personal → Scene (Contest)* is an **empty section** — heading only, no body, no stub marker | Author the handoff rule |
| **ED-IN-0050** | Same doc carries literal **GM-as-resolution-actor** language against the no-GM invariant (§1 L19, §3.2 L49) | ⚠ Reopened: the antagonist found `04:330` is a seat/delegation invariant, so this is not a pure find-replace |
| **ED-IN-0148** | Populate the *"GM Decides" Resolution Register* that `videogame_mode_spec` §3 specified and never filled | Direct instance of the same no-GM class |
| **ED-IN-0195** | Triage the consolidated 45-row register from the three-lens weekly-review audit | Rows, not decisions |
| **ED-IN-0042** | Skills-ecosystem gap audit, six subjects | ⚠ Reopened: 4 of 6 subjects are live per `CLAUDE.md`. **Two-thirds of this row reads as §0 test 2 (irrelevant)** — re-scope first; it may belong in §3.4, not here |

**Plus, from §1 and not yet a row:** **OI-07**, the Knot-formation prerequisite gap — personal-scale
fields (Disposition, Bonds, TS) read off an aggregate strategic World. `scene_dispatch.py`'s module
docstring already names this context-derivation class for combat and contest actor derivation.
**Closing the class closes OI-07**; it needs no ruling and should be filed against the cross-scale work
rather than as a Knots item.

### §3.2a · HELD — overturned within the last day; re-derive before routing (3 rows)

**Not a bucket I wanted and the reason it exists is a defect in my own prior work.** All three were
closed in the `ED-IN-0215` pass on a premise that is false — that `engine/season/port/` exists — and
reopened by an antagonist the same day. An earlier draft of this document then placed them under WORK,
which re-adjudicates a just-overturned verdict into the opposite bucket with no new evidence.

| Row | Its own title | Why it is held |
|---|---|---|
| **ED-MB-0065** | *"J2 is RULED-BUT-NOT-EXECUTABLE: the retired tree holds the campaign's only faction-scale seam, and a LATER ruling already kept it"* | Names a ruling conflict, not an engineering act |
| **ED-IN-0123** | *"Fork plan of record: the Godot strategy exists; the Python-side Stage 0 it presupposes does not"* | A planning object about the Godot strategy — the tree §3.1 gates on **ED-1051** |
| **ED-IN-0124** | *"Executable rewrite of the fork Plan of Record after two independent read-only Fable-5 passes"* | Same |

**What must happen first:** re-derive each against the tree as it is — not against the `port/` premise,
and not against this document's sort — and only then decide whether it is a ruling, work, or dead.
`CURRENT.md:34` (*"Gate-0 is blocked on ED-1051"*) is the starting point for all three.

### §3.3 · CONTENT — authorial; unschedulable (1 row)

| **ED-508** | Starting Dispositions for the named NPC roster. The lifepath formula is canonical; the roster values are Jordan's to write. Parking it in the ruling queue makes the queue unreadable without making the content appear. |
|---|---|

### §3.4 · CLOSURE CANDIDATES — believed dead, NOT verified to this repo's standard (3 rows)

**Stated as candidates, not verdicts, deliberately.** In this session's queue pass an antagonist broke
**twelve of ninety-five** proposed closures that had already passed a mechanical membership test. The
honest move is to name these and let the closing session do the verification, with its citation.

| Row | Why it looks dead | What must be checked before closing |
|---|---|---|
| **ED-MB-0056** | Its own text opens `[FIGURE RETRACTED, see ED-MB-0060]` | That ED-MB-0060 is live and actually carries the replacement figure |
| **ED-MB-0061** | A **session retrospective**. A retrospective is a record, not a decision. | That no finding inside it is unaddressed elsewhere |
| **ED-IN-0092** | W0 preflight for the ED-IN-0091 code-shape program, which has since completed | That the held Jordan docket (`05_jordan_docket_v1.md`) was resolved, not merely overtaken |

### §3.5 · Gated by a spelling the `open` filter does not see (7 rows)

**These seven, plus `ED-IN-0210` in §3.1, are the reason §0 counts thirty-four and not twenty-six.** Each carries a live Jordan-gating
mark and is invisible to the predicate `needs_jordan: true AND status: open`. Two are genuine
ratify-or-not questions, two are audit capstones left `partial` with the flag never cleared, and three
are flat-ledger design gaps under a different field. An eighth, `ED-IN-0210`, is a ruling and is routed
in §3.1 instead.

| Row | Spelling | What it is |
|---|---|---|
| **ED-WR-0010** | `status: proposed`, `needs_jordan: true` | Threadwork practical applications by subsystem, landed 2026-09-10 and **explicitly held back from ratification-on-merge in full**. Under **ED-1094** the loud exception means separate sign-off; it does not ratify by sitting there |
| **ED-1010** | `status: open`, `jordan_decision: "pending"`, **no `needs_jordan` key** | Threadwork per-operation Coherence cap is canonical-in-effect but homeless — lives only in `threadwork_v30_infill` l.121 — and A.10-contradicted (RD-2) |
| **ED-1011** | same | Coherence-0 rule split and gapped: `params/core` PP-261's *"at 0: NPC …"* against a silent no-Close-Knot cliff (RD-3) |
| **ED-932** | same | `params/bg/clocks.md`'s MS/CI/IP Environmental Effects + Battle Consequences; all of C14a *"remain gapped/**Jordan-gated**"* in the row's own words |
| **ED-IN-0059** | `status: proposed`, `needs_jordan: true` | The pointer-debt work-list (`references/registry/pointer_debt_worklist.md`). Its own finding is that completing `tools/registry.py` does **not** move `G_pointer` — 0 of 32 unresolved identifiers resolve — so the proposal is that the work-list, not the tool, is the deliverable. **Ratify-or-not** |
| **ED-IN-0147** · **ED-IN-0149** | `status: partial`, `needs_jordan: true` | Two Fable-5 audit capstones left `partial`. ⚠ **ED-IN-0147 was closed in the `ED-IN-0215` pass and reopened by an antagonist** — `world_initial_state.yaml:70` still reads `Mil: 4.0`, so its remediation did not land. Both are **work with a flag nobody cleared**, not rulings |

⚠ **`ED-IN-0210` is the fourth spelling** (`status: ruled` + `needs_jordan: true`, fork live in the
row's text) and is routed in **§3.1**, not here, because it is a ruling rather than a bookkeeping
artifact.

> **The general lesson, and it is the one this repository keeps paying for.** Four different fields
> across two ledger formats express "Jordan must answer this." Any future mechanical scan of the queue
> must enumerate all four, and **`CLAUDE.md` §8's `pathres.resolve` entry is the canonical record of
> this same failure** — a predicate that matches a name instead of the thing. `[GAP: no tool enumerates
> the Jordan-gated set. §0's table is a hand count and will rot. A single owner for that predicate is
> the obvious fix and it is NOT built here — building it would be apparatus, and §0.1 pt 5's predicate
> asks whether the artifact is load-bearing on the game or on a Jordan decision. This one is
> load-bearing on a Jordan decision, so the guard would be licensed — but it is the reconciled
> program's work to schedule, not this document's to mint.]`

---

## §4 · Per-lane workstreams

_Format: **handoff pointer** · the next increment · its gate. **No status here** — read the handoff.
All nine lanes have a file under `registers/handoffs/`; a section without its pointer is a bug._

### IN — infrastructure / cross-cutting
`registers/handoffs/HANDOFF_IN.md`. **The lane carrying the milestone.** Arc 1 has LANDED (PR #386);
**Arc 2 is unbuilt — `state/` holds only `carriers.py`, `ids.py`, `world.py`: no `gate.py`, no
`Receipt`, no token type**, and Arc 3's U9 is blocked on `Act.via` from G3. Next increment is Arc 2's
**G1** (`Receipt`, and `state/gate` as its own owner) per the layer1-conformance plan. Order for the
whole arc chain: the reconciled program, positions 2–15.

### SC — social contest
`registers/handoffs/HANDOFF_SC.md`. **Retained by ED-IN-0204 Decision 1.** `ED-SC-0033` (Jordan,
2026-09-06) killed the SC kernel cluster in one stroke; **the deletion set for that ruling is not yet
derived** and is the reconciled program's position 2 — blocked, deliberately, because the first
derivation censused `import` statements and the engine binds `systems.social_contest` **by string**
through `composition.json` → `importlib.import_module` → `scene_dispatch` → `mc_v18`. Three rulings
wait: ED-SC-0003 (the name collision), ED-SC-0005 (the cap value), ED-SC-0015 (Mandate stacking).

### PC — personal combat
`registers/handoffs/HANDOFF_PC.md`. **Retained by ED-IN-0204 Decision 1.** Quiet this week — no PC row
opened and none of the 26 is PC's. M1's juncture 4 needs the U-series' front half only, not `phase4_5`.
⚠ v6's §4-PC text is the most detailed section in that document and the **most likely to have rotted**;
re-derive from the handoff before scheduling, not from v6 at its fork ref.

### MB — mass battle
`registers/handoffs/HANDOFF_MB.md`. **Retained by ED-IN-0204 Decision 1**, and the **largest share of
the live queue: 7 of 26 rows.** One ruling (ED-MB-0008, which DR table governs) and four work items,
of which **ED-MB-0016 is the one with its diagnosis already finished** — per-battle CEV friction
against a root cause confirmed mathematically (melee attrition self-averages ~1/√N, so outcomes
collapse to 100%/0% where history shows friction). That is the lane's highest-value next increment.

### SE — settlements
`registers/handoffs/HANDOFF_SE.md`. Seven proposals landed 2026-09-09/10 (PR #389, #391) and were
**held back from ratification in full**; the NERS pass was **run rather than cited** and scored all
seven `paper`, with two that do not load. One ruling gates the set: **ED-SE-0051 / E-1**, the bound on
the demographic loop. Nothing else in SE schedules until it is answered.

### WR — world
`registers/handoffs/HANDOFF_WR.md`. Two items, both narrow: **ED-WR-0008** (the truncated Mending
Stability override table — supply the rows or strike the override) and **ED-WR-0010** (threadwork
practical applications, `proposed`, held back from ratification-on-merge in full).

### FI — field investigation
`registers/handoffs/HANDOFF_FI.md`. PR #387 built six investigation acts — verbs executing 6-of-32 →
10-of-37. `ED-FI-0009` remains open, with the R3 fall measured and attributed (PR #395). ⚠ **This lane
did not flip R-03**; U2 did, on the same PR that closed the R3 measurement. Do not read the two as one
result.

### FA — factions
`registers/handoffs/HANDOFF_FA.md`. Not retained as a subsystem by ED-IN-0204 Decision 1, but faction
*actions* remain reachable from the season loop, and **R-04 (`not_met`) — "strategic and management
actions must be possible" — is a faction-surface requirement.** Retirement of the FA design tree is
gated on the R-04 role work (`CLAUDE.md` §3); do not schedule FA design work as if the lane were live,
and do not delete it as if it were dead.

### GO — Godot
`registers/handoffs/HANDOFF_GO.md`. **M3-gated, blocked on ED-1051**, and carrying two standing
cautions that any GO work must respect: the port's **engine version is UNRESOLVED and no document here
may assert one**, and `godot/skeleton/` does not compile and `extends` a spine defined nowhere.
`godot/godot_conversion_strategy_v1.md` is PROPOSED and Jordan-vetoable throughout.

---

## §5 · Governance — what changed since v6, and what a session does now

v6 §6 is the section that rotted hardest; every mechanism it names is retired. Replacing it:

| v6 §6 said | Today |
|---|---|
| Monthly reconcile refreshes §5's pointers | **Keep the practice, drop the cadence.** The reconcile is what §3 is; it runs when the queue is re-sorted, not monthly |
| `workplans/workplan_v6_progress.yaml` rendered by `tools/workplan_status.py`, owned by `valoria-workplan-navigator`, surfaced in the SessionStart banner | **All three are gone.** The tool does not exist; the skill was retired 2026-08-21 (ED-IN-0194); `CLAUDE.md` §0.3 retired the banner and **forbids building a replacement**. The board survives, hand-edited and unrendered, only because `m1_acceptance.py:72` reads it |
| ID protocol: read `next_free`, allocate, bump, co-commit | **Unchanged, and still only discipline.** Four within-lane IN collisions on 2026-09-10/11 — renumbering to `next_free` does **not** escape a same-lane collision (ED-IN-0209/0210/0211). The structural fix, `wiring_status.auto_allocation`, is specified and PARKED |
| Verification: run the suite | **`CLAUDE.md` §0.4 now rules the cadence.** Full suite **once per commit**, immediately before it, `-n auto`. Mid-session run only the file covering your edit. Never re-run to re-confirm a green you hold |
| — | **New, and binding on this document:** `CLAUDE.md` §0.05 — code is the mechanism, prose is reference. This file resolves nothing. Delete it and the game behaves identically |

### The figure that reads four ways — and why "read the instrument, not the index" is too glib

The nine requirements, as four surfaces state them:

| Source | Reading | Kind |
|---|---|---|
| `CURRENT.md:34` | 6 `not_met` / 3 `partial` | a count cached in an index, **unscoped** |
| `HANDOFF.md:18` | *"requirements still **6 `not_met` / 3 `partial`**"* | same count, but `:21` **scopes it** to Arc 1 — fairly |
| `workplans/2026-09-11-arc-sequence-spine.md:29` | 1 met (R-03) · 5 `not_met` · 3 `partial` | correct for the tree it measured — **before `c275a9b` merged** |
| **`register --requirements`, `origin/main` == this branch** | **1 met · 4 `not_met` · 4 `partial`** | a count of hand-written `status:` strings, each with a validated `measure:` |

**Four readings, one subject, and every one was correct when written.** Two different things are going
on and an earlier draft of this section conflated them:

1. **`CURRENT.md:34` genuinely rotted** — it caches a count, does not scope it, and is now two landings
   behind. It carries a *second* stale figure in the same row (*"6 of 32 verbs executing"*, against
   `requirements.yaml:301`'s *"11 of 38 verbs execute in the corpus"*). Both are repointed by this change.
2. **The spine did not rot at all.** It measured a different tree, one day earlier, and said so. Filing
   it under "rot" was unfair, and the first draft of this document did exactly that — then compounded it
   by opening a `[GAP:]` for the delta rather than running `git log` against the instrument's input.

**So the rule is narrower than "read the instrument, not the index":** an instrument that counts a
hand-edited field is an index wearing a command's clothes. The rule is **name the command, print its
output with the commit it ran against, and say what the command actually reads** — which is what §0's
second table now does.

---

## §6 · Supersession — what of v6 survives

**v6 is retired to a fork ref, not amended.** Per `CLAUDE.md` §1, retiring means deleting the file and
writing a `FORK:` row in `references/restructure_ledger.md`; an exact-file row, never a directory
prefix (§8's `pathres.resolve` hazard). v6's content is recoverable at that ref and every citation to
its path resolves through `tools/pathres.py`.

| v6 | Verdict |
|---|---|
| §0 hierarchy + **no-status-column** rule + **completeness rule** | **SURVIVES** — carried into §0 and §4 verbatim in substance. v6's best contribution |
| §1 M1's seven junctures | **SURVIVES as the board's rows**, which `m1_acceptance.py` still counts. The *definition* of done is replaced: §0.2 requires execution, not a `## Status:` line |
| §1 M2 (Churn-Engine fixture F1, Stages 1–4) | **NOT CARRIED.** Predates ED-IN-0204. §1 keeps the bar and states plainly that it has no instrument |
| §1 M3 | **SURVIVES** — still last, still gated on ED-1051 |
| §2 IN spine (7 numbered items) | **SUPERSEDED** by the Arc 1/2/3 structure and the reconciled program's positions |
| §3 narrative-engine workstream | **NOT CARRIED** — its head is under the dissolved `designs/` tree, and whether the workstream survives ED-IN-0204 is an open ruling (§1, M2's `[GAP:]`) |
| §4 lanes | **RE-DERIVED** from the handoffs, not copied. v6's PC section especially |
| §5 tiered decision register | **REPLACED by §3's sort.** The tiering axis changes from *what it blocks* to *who can answer it* — the change ED-IN-0208 measured the need for |
| §6 governance | **SUPERSEDED** — see §5's table; every mechanism named is retired |
| Appendix A (v5 supersession) · Appendix B (session inventory) | **NOT CARRIED** — dated 2026-07-05 snapshots of trees that no longer exist. Recoverable at the fork ref |

### The ORDER collision is REAL, is NOT closed here, and needs a ruling

An earlier draft of this section announced that it *"closes an ambiguity I created"*, supplied its own
falsifier — *"if a session can read the spine's positions 2–15 and act on them without consulting the
program, the collision is live"* — and **the falsifier fired on the first reading.**

`workplans/2026-09-11-arc-sequence-spine.md:36-57` is a self-contained sixteen-row table. Each row names
its unit, its contents, and its *not earlier because* / *not later because*. Position 2 reads in full:
*"G1a — `state/acts` · `Receipt` · `state/gate` minting it · `log.append` asserting causes ∈
`log ∪ acts ∪ {ROOT}` … the ruled `Record.matured` fix, with the H-80 control re-derived first."* **A
session can execute positions 2–15 from that table without ever opening the reconciled program.**

A second, independent break: `workplans/2026-09-11-reconciled-program.md:57` still lists *"the spine
(ORDER, positions 2–15)"* as **LIVE**, and this document edits neither file. Under `CLAUDE.md` §0.05 a
reference document resolves nothing — **it cannot close a collision between two other reference
documents by asserting it closed.** The header of the earlier draft claimed an effect its own §5 row
denies it can have.

**So, stated honestly:**

| | |
|---|---|
| **The collision** | Two live documents each claim to own a cross-lane ORDER: the spine (16 positions, ED-IN-0212) and the reconciled program (27 positions, ED-IN-0215) |
| **What is true** | The program's `:6` says it takes over what the spine owned *for the IN-lane engine*. The spine's `:7` says it owns *"only the order across"* Arc 2 and Arc 3. These overlap and neither text subordinates the other |
| **What closes it** | **A commit**, not a paragraph — either the spine's positions 2–15 are struck and it keeps only its reasoning, or the program cedes those positions. Both are one-line edits to a `## Status:` line plus a strike |
| **Who decides** | Not this document. It is the reconciled program's own scope, and it is added to §3.1's queue as a **ruling only if** the two owners cannot settle it from the tree — §0 test 5 probably can: the later document with the wider scope is the conventional winner, and that is the program |

`[SELF-AUTHORED — bias risk: the collision is mine, from earlier in this same session. I have twice now
written a paragraph claiming to resolve it. The second attempt is this table, which claims only to
describe it. An independent reviewer should check whether even that is too generous — specifically
whether "the program takes over the spine's IN-lane order" is supported by anything in the spine, which
never mentions the program because the program did not exist when it was written.]`

### What I said was dead and is not

An earlier draft closed with two "dead references found while classifying the corpus". **Both were
wrong, and an independent reader found them by running `ls`.**

| Claimed | Actually |
|---|---|
| *"`relay/PLAN_v2.md` — `relay/` does not exist on disk and has no `FORK:` row"* | **`relay/` exists**, at `proposals/2026-09-05-proceedings-subsystem/relay/`, holding eight files, and `references/restructure_ledger.md:2078` names it. The narrower true statement is that **no file called `PLAN_v2.md` exists in that cluster** — it holds `19_PLAN.md` and `relay/H_FABLE_PLAN.md` — so `2026-09-06-season-loop-execution-plan.md:10` supersedes something by a name nothing carries. A one-line repair to that plan's `:10`, not a dangling tree |
| *"`return_to_game_queue.yaml`'s runbook cites `.claude/wf_return_to_game.js` and `deprecated/claude/…`, neither of which exists"* | **It is a correctly-recorded retirement.** `:63` reads `driver_retired: "FORK:baf29d5:deprecated/claude/wf_return_to_game.js"` — the exact `FORK:<ref>:<path>` shape `CLAUDE.md` §1 prescribes, resolvable through `tools/pathres.py`, annotated *"Kept at a ref for history, NOT for invocation."* Nothing is broken |

**What survives of that section:** `workplans/return_to_game_queue.yaml` does carry
*"⛔ SUPERSEDED 2026-08-19. DO NOT RESUME THIS QUEUE."* and is 1,620 lines of superseded plan sitting in
the live plan directory. That is a tidiness observation, not a defect, and **this document does not fix
it** — fixing what a survey finds is the §0.3 generator.

### Retiring v6 — ATTEMPTED, REVERSED, and deferred with its reason

**v6 is still on disk. It is superseded, not retired, and that is a deliberate stop rather than an
oversight.** `CLAUDE.md` §1 says retiring means deleting the file and writing a `FORK:` row. That was
done, and then undone, because it broke a blocking gate in a way this container cannot honestly repair.

**What was checked and holds:** no gate reads the master workplan — greps over `tools/`, `tests/` and
`.github/` return nothing for `valoria_master_workplan`. Both non-workplan citations are repointed here
(`references/lane_assignments.yaml:29`'s `source:`, and `CURRENT.md`'s Master-workplan row). The
exact-file fork row verified clean: `git cat-file -e 2d5ec4e:workplans/valoria_master_workplan_v6.md`
exits 0, and `pathres.resolve` returned `FORKED → FORK:2d5ec4e:workplans/valoria_master_workplan_v6.md`.

**What broke it:** ledger entry `ED-IN-0071` cites the *pre-restructure* spelling,
`designs/workplans/valoria_master_workplan_v6.md`. With v6 deleted, `tools/broken_dependency_checker.py`
— which runs in CI's **blocking** job, not the report-only one — reports that path `[BROKEN]`. Three
repairs were tried and each failed on its own merits:

| Attempt | Why it failed |
|---|---|
| Rewrite the alias row `designs/… → workplans/…` to a `FORK:` value | The alias table is a two-column **rename** table; its value column is a path. `test_forked_status.py` went 140 → 141 unresolvable and **named the row**. A table's shape is part of its meaning |
| The paired form `FORK:<ref>:<path>` in that same alias row | Same table, same problem — the resolver pairs the value with the *old* path, which never existed at that ref |
| A direct 3-column FORK row for the `designs/` spelling | Cleared the dependency checker, but `designs/workplans/valoria_master_workplan_v6.md` **does not exist at `2d5ec4e`**, so `test_forked_status` went to 141 again |

The honest row would name a commit where the old spelling actually lived. **This container is a shallow
clone and cannot reach one** — a 400-commit walk finds no such commit and `git log --diff-filter=D`
returns nothing. `references/restructure_ledger.md`'s own instruction is *"Verify a row with
`git cat-file -e <ref>:<path>` BEFORE writing it"*, and the alternative — appending a superseding ledger
row to rewrite `ED-IN-0071`'s path citation — edits history to make a cleanup pass convenient.

**So the retirement is deferred, and the deferral is the loud exception `ED-1094` requires.** What a
full-clone session needs to do: find the commit carrying `designs/workplans/valoria_master_workplan_v6.md`,
write **two** exact-file FORK rows (one per spelling, each verified), then delete v6. Until then the
tree holds two master workplans, `CURRENT.md` names v7, and v6 is reference.

> **The generalisable finding, which is worth more than the cleanup:** three plausible repairs, each
> defensible in isolation, each caught in under a second by a guard that reports a **delta against a
> ceiling** and names the row you touched. `tests/valoria/test_forked_status.py` is `CLAUDE.md` §0.1 pt 2
> working exactly as specified — an assertion that can observe the failure it excludes — and
> `broken_dependency_checker`'s blocking status is what stopped a red `main`. Neither is apparatus for
> its own sake; both are load-bearing on a real change.
