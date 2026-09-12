# Valoria — Master Workplan v7 (North-Star master: milestones, the queue sorted by who can answer it, lanes)

## Status: **PROPOSED (ED-IN-0216)** — supersedes `valoria_master_workplan_v6.md` (CANON since 2026-07-05, ED-IN-0009/ED-IN-0011)

> ⏳ **NOT YET RECONCILED.** A structurally read-only antagonist pass against the working tree is
> still running at the time of this commit. Findings are not folded in, and **v6 is not yet
> retired** — `CURRENT.md:43` and `references/lane_assignments.yaml:29` still point at it, so this
> commit leaves two master workplans in the tree and v6 is the one the index names. Do not treat
> this file as the master until that marker is gone.

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
| that a milestone is or is not met | **whether the behaviour runs** | `tools/m1_acceptance.py --summary` · `python -m engine.season.harness.register --requirements` |

**Completeness rule, carried from v6 §0 and still binding:** every §4 lane section opens with its
`HANDOFF_<LANE>.md` pointer even where the section is thin — the pointer is what guarantees nothing is
missed, not enumeration here. A §4 entry with no handoff pointer is a bug in this document. Likewise
every `needs_jordan: true` row must be reachable from §3. **Verified by hand at that commit: §3 carries
all 26.**

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
Arc 1 and is no longer true for the tree. **R-03 was flipped to `met` by U2** — *"U2 · R-03 — the scene
tick at player granularity"*, commit `2ebab0c`, landed on `main` with PR #395 — and
`workplans/2026-09-11-arc-sequence-spine.md:29` records the attribution: *"R-03 was flipped by U2 on an
execution, which is the only kind of flip `CLAUDE.md` §0.2 accepts."* `HANDOFF.md` at least flags its
figures as Arc 1's; `CURRENT.md:34` does not, and is repointed by this change.

⚠ **One further row moved `not_met` → `partial` between the spine's reading yesterday and this one, and
I could not attribute it.** The spine read `1 met · 5 not_met · 3 partial`; this tree reads
`1 met · 4 not_met · 4 partial`. The only commit on `main` between them is `2d5ec4e` (#394), which is
editorial and should move nothing. `[GAP: the ninth row's transition — measured, unattributed. Bisect
with `register --requirements` against `c275a9b` and `2d5ec4e`; do not assume it was a landing this
week.]` **Stated rather than guessed: the first draft of this paragraph attributed R-03 to two
unrelated PRs on nothing but their position in the week's log — the fifth time in this session that a
claim failed by matching a name or a date instead of checking the mechanism.**

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
| ED rows opened | **22** — IN 14 · SC 5 · FI 1 · SE 1 · WR 1 |
| of those, still `open` | **7** |
| of those, still `needs_jordan` | **4** — ED-IN-0210, ED-IN-0214, ED-SE-0051, ED-WR-0010 |
| commits landed on `main` | **20** |

**The week's shape, in one line per landing that moved a milestone row:**

- **PR #384 → `ED-IN-0204`** — the nine R-rows sequenced unit by unit; **seven planner claims
  overturned.** This is the ruling the rest of the week runs under.
- **PR #383 / #381 / #378 → `ED-IN-0203`** — the `shape.py` decomposition COMPLETE, 6,771 → 0. The
  facade is deleted and every importer names its owning module.
- **PR #386 → `ED-IN-0206`** — Arc 1 executed rather than planned: `decision/`, `seam/`, `manifest/`,
  `queries/`, `loop/`'s six steps. Content hash unchanged — what a pure structural arc should read.
- **PR #387 → `ED-FI-0009`** — six investigation acts built; verbs executing 6-of-32 → 10-of-37.
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

So the axis here is **who can answer**, not what it blocks. All **26** live rows (`needs_jordan: true`
AND `status: open`) appear exactly once below. Tier within a bucket is the `Blocks` column.

### §3.1 · RULINGS — Jordan only (10 rows)

Each survived all five of `CLAUDE.md` §0's tests: not superseded, not irrelevant, not answered by a
design document, not answered by precedent, and with no obviously-right engineering answer. Two
defensible options lead to materially different games.

| Row | The question, in one sentence | Blocks |
|---|---|---|
| **ED-1051** | Flip `module_contracts.yaml`'s `doc: null` for `engine_clock` to `propagation_spec_v1`, or author a new home? | **M3 entirely** — Gate-0's entry condition; 10 modules and 11 `[ASSUMPTION]` resolvers behind it |
| **ED-SE-0051** | E-1 — is the demographic loop bounded by **matter only**, or **matter plus hearth capacity**? Malthus, or a Site-capacity ceiling on births. | the settlements/populations proposal set; the only question of seven that survived all five tests |
| **ED-IN-0214** | The 13×4 conviction matrix has a **dominant common direction** — convictions differentiate a person's own priorities well and different people badly. Re-cut the matrix, or accept it? | **position 11's measurement** — a late *yes* invalidates it |
| **ED-SC-0003** | The "Piety Track" name collision: one name, two referents, three docs. Which name wins for the debate tracker, which doc is its home, what does the per-territory stat become? | SC lane doc integrity; touches 127 files |
| **ED-SC-0005** | The numeric **cap** on the Recall/Corroborate/Prep/Findings bonus-die stack. Doc math reaches +8D while the genre/audience boost caps at +2D. | must land before Stage-4 wiring makes it live; decision packet already drafted |
| **ED-SC-0015** | Do the parliamentary Total-Victory Mandate −1 and the Censure tier's own Mandate −1 **compound** on the same faction in one motion? Implemented as stacking by literal-faithful default. | parliamentary resolution correctness |
| **ED-MB-0008** | Two live ranged/volley Damage-Reduction tables, ~2× apart for the same armour band, neither marked superseded. Which governs? | volley resolution is undetermined for an importer or a player |
| **ED-IN-0030** | The phantom "debt scene": `scale_transitions_v30` §4.3.2 cites a mechanic that exists nowhere. **Author it, or strike the reference?** | FA/political doc integrity |
| **ED-WR-0008** | The P-25 Scale-based Mending Stability override table was **truncated at authoring** — header plus the label `Object`, zero data rows, no revision ever had them. Supply the values, or strike the override? | threadwork scale-override behaviour is unspecified |
| **ED-885** | `canonical_sources.yaml:579` cites ED-885 for the 2026-05-30 F-RESID migration; ED-885 was never written. **Confirm ED-874, or name the real ID.** | citation integrity in a machine-read registry |

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

### §3.2 · WORK — an agent does this; no ruling required (12 rows)

These are in the queue because nobody closed them, not because they need Jordan. Each names an
engineering act with a decidable outcome.

| Row | The act | Note |
|---|---|---|
| **ED-1043** | Split `orchestration.py` (2,899 L god-file: data model + targeting + attrition authoring + volley + resolution + turn loop + I/O) | Largest single item in the queue; scope it against `architecture/` before starting |
| **ED-MB-0016** | DG-6 over-decisiveness: root cause **confirmed mathematical** — melee attrition self-averages ~1/√N, so outcomes collapse to 100%/0%. Implement per-battle CEV friction. | The diagnosis is done; only the build remains |
| **ED-MB-0044** | R3 ranged-vs-ranged never engages — a **definitional** gap, not a balance one | scope corrected by ED-MB-0045 |
| **ED-MB-0057** | Dead-primitive census: 118 built-but-unwired primitives repo-wide; MB's ten analysed | Triage, then wire or delete |
| **ED-MB-0065** | J2 is ruled-but-not-executable: the retired tree holds the campaign's only faction-scale seam | ⚠ **Reopened 2026-09-11** — this session closed it on a false `port/` premise |
| **ED-IN-0123 / ED-IN-0124** | The fork Plan of Record: the Godot strategy presupposes a Python-side Stage 0 that does not exist | ⚠ **Both reopened 2026-09-11**, same false premise |
| **ED-IN-0049** | `scale_transitions_v30` §3.3 *Personal → Scene (Contest)* is an **empty section** — heading only, no body, no stub marker | Author the handoff rule |
| **ED-IN-0050** | Same doc carries literal **GM-as-resolution-actor** language against the no-GM invariant (§1 L19, §3.2 L49) | ⚠ Reopened: the antagonist found `04:330` is a seat/delegation invariant, so this is not a pure find-replace |
| **ED-IN-0148** | Populate the *"GM Decides" Resolution Register* that `videogame_mode_spec` §3 specified and never filled | Direct instance of the same no-GM class |
| **ED-IN-0195** | Triage the consolidated 45-row register from the three-lens weekly-review audit | Rows, not decisions |
| **ED-IN-0042** | Skills-ecosystem gap audit, six subjects | ⚠ Reopened: 4 of 6 subjects are live per `CLAUDE.md`; re-scope before acting |

**Plus, from §1 and not yet a row:** **OI-07**, the Knot-formation prerequisite gap — personal-scale
fields (Disposition, Bonds, TS) read off an aggregate strategic World. `scene_dispatch.py`'s module
docstring already names this context-derivation class for combat and contest actor derivation.
**Closing the class closes OI-07**; it needs no ruling and should be filed against the cross-scale work
rather than as a Knots item.

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

### §3.5 · Flagged but not `open` — one row that is a ratify-or-not

**ED-WR-0010** (status `proposed`, `needs_jordan: true`) — threadwork practical applications by
subsystem, landed 2026-09-10 and **explicitly held back from ratification-on-merge in full**. It is not
in the 26 because it is not `open`. Under **ED-1094** the held-back exception means this one needs
separate sign-off; it does not ratify by sitting there.

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

### The figure that rotted three ways this week — read the instrument, not the index

The nine requirements, as three documents state them:

| Source | Reading |
|---|---|
| `CURRENT.md:34` | 6 `not_met` / 3 `partial` |
| `workplans/2026-09-11-arc-sequence-spine.md:29` (yesterday) | 1 met (R-03) · 5 `not_met` · 3 `partial` |
| **`register --requirements`, this tree, today** | **1 met · 4 `not_met` · 4 `partial`** |

Three figures, one subject, and **all three were correct when written.** This is not carelessness; it
is what happens when a number is cached in a document whose revision cycle is slower than its subject's.
`CLAUDE.md:345` names it for a date, `CURRENT.md:34` names it for a count, and both were written by
someone who had just been bitten by it. **The rule this document follows: name the command, print its
output with the commit it ran against, and never restate that output anywhere else.**

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

### The ORDER has one owner, and this closes an ambiguity I created

`workplans/2026-09-11-arc-sequence-spine.md` (ED-IN-0212) states it *"owns only the order across"* the
Arc 2 and Arc 3 plans. `workplans/2026-09-11-reconciled-program.md` then claimed to be *"the single
owner of the ORDER across all lanes"* while **also** listing the spine as LIVE for "ORDER, positions
2–15" (`:57`). **Both cannot hold.** The resolution is the one the program's own `:6` already states —
it takes over what the spine owned for the IN-lane engine — and this document makes it explicit:

- **The reconciled program owns the ORDER.** All lanes, 27 positions.
- **The spine stays** as the record of its own reasoning and as the source the program declares three
  named departures from (positions 19b, 23, and `build_at`'s `cast:` move). It is not a second order.
- **Unit CONTENT stays** with the r-execution plan (U1–U10), the layer1-conformance plan (Arc 1/2), and
  the post-adoption execution plan — which, note, **forbids its own supersession**: *"it is superseded
  by its own completion — not by a successor plan"* (`:5`). Nothing here supersedes it.

`[SELF-AUTHORED — bias risk: the ambiguity above is mine, from earlier in this same session, and I
found it only because an independent reader classified the plan corpus. An independent reviewer should
ask whether "the program owns the order, the spine keeps its reasoning" is a real resolution or a
restatement of the collision with nicer words. The falsifier: if a session can read the spine's
positions 2–15 and act on them without consulting the program, the collision is live and this
paragraph is wrong.]`

### Two dead references found while classifying the corpus, not yet repaired

- **`relay/PLAN_v2.md`**, cited as *"superseded entirely"* by `2026-09-06-season-loop-execution-plan.md:10`
  — `relay/` does not exist on disk and has no `FORK:` row.
- **`workplans/return_to_game_queue.yaml`** carries its own banner: *"⛔ SUPERSEDED 2026-08-19. DO NOT
  RESUME THIS QUEUE. DO NOT RUN THE DRIVER."* It is 1,620 lines of superseded plan sitting in the live
  plan directory, and its runbook cites `.claude/wf_return_to_game.js` and `deprecated/claude/…`, neither
  of which exists.

Neither is repaired here. **This document does not fix what it finds** — that is the §0.3 generator. Both
are stated so the session that acts on them has the citation.
