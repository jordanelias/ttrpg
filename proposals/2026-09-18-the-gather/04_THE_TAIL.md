# 04 · THE TAIL — the trees nobody has dispositioned

## Status: **DISPOSITION (2026-09-18). Lane: THE LONG TAIL.** Verdicts only — no code touched, no
## `## Status:` line flipped, no `ED`/`PP` allocated. `engine_season:` is the concrete
## `engine/season/` change each verdict implies, or the literal `NONE`.

Seven trees, 179 files, 96,721 lines — 60% of `00_THE_CENSUS.md` §2's corpus by line count, and the
largest single omission in the gather. **Read at index/README depth and spot-checked against code;
none of the 60,578-line tree was read whole** (`00_THE_CENSUS.md` §2 line counts, handed to me,
re-verified against no fresh `wc`).

---

## THE SEVEN VERDICTS

| path | verdict | successor / disposition | `engine_season:` |
|---|---|---|---|
| `2026-09-04-degree-sweep/` | **ABSORBED** | findings landed as `engine/season/hole_register.yaml` rows H-113..H-120 + `architecture/meta/HANDOFF_NEXT.md` §2A | NONE |
| `2026-09-05-proceedings-subsystem/` | **LIVE, SCHEDULED** | RULED (ED-SC-0033) to own all social contests; slotted at `workplans/2026-09-18-governance-settlement-behaviour-plan.md:156,161` (PROC-A, PROC-B) — not yet built | NONE |
| `2026-09-04-social-contest-branches/` | **SUPERSEDED** | by the ruled game-structure model, `2026-09-05-proceedings-subsystem/` (ED-SC-0033) | NONE |
| `2026-09-12-emergent-narrative-primitives/` | **SUPERSEDED** | by `2026-09-12-emergent-narrative-primitives-v2/00_INDEX.md:9` | NONE |
| `2026-09-12-emergent-narrative-primitives-v2/` | **LIVE** (partial ABSORBED) | 6 of 14 proposals folded into `workplans/valoria_master_workplan_v7.md:658` §7 Amendment 1 (ED-IN-0218); 8 remain open PROPOSED | NONE |
| `2026-08-28-greenfield-systems-suite/` | **SUPERSEDED** | chain: → `2026-08-29-greenfield-systems-suite-v2/` (its own `ARCHIVED.md:3`) → `architecture/` (`workplans/2026-09-18-governance-settlement-behaviour-plan.md:63`) | NONE |
| `2026-09-16-term-ownership/` | **ORPHAN** (mixed — see §7) | `key_type_registry.yaml` half SPENT (ED-IN-0232); `offices_draft.yaml` 6-row sliver ABSORBED (`engine/season/rosters.yaml:930,971`), remainder unverified | NONE |

**None of the seven implies an `engine/season/` change.** That is not a gap in this pass — it is
the honest reading of a tail this old: every tree that had a live claim on the loop has already
routed there (degree-sweep's findings, term-ownership's sliver) or is scheduled elsewhere
(proceedings), and what is left is either dead (superseded, spent) or genuinely still a design
question sitting in `proposals/` awaiting Jordan (emergent-narrative-primitives-v2's other eight).

---

## §1 · `2026-09-04-degree-sweep/` — ABSORBED, 95 files / 60,578 lines

An **instrument and its output**, not a design proposal: `README.md:4` states it "changes no head,
no roster, no verb table, no code under test" and reads `engine/season/` at a pinned commit only.
Its headline — 2,403 forks, zero of which change any of the next three decisions; the degree ladder
built (`degree_from_net`, `engine/autoload/dice_engine.py`) and never reached (`S39` fires 0 times in
5,376 firings) — is not a proposal to accept or refuse; it is a measurement.

**The measurement was digested, per the README's own closing table** (`README.md:667-676`), into the
two surfaces that own the finding: `engine/season/hole_register.yaml` gained eight rows, all grade
`measured` — confirmed present at `H-116`:1771, `H-113`:1814, `H-114`:1858, `H-115`:1901, `H-117`:1926,
`H-118`:2037, `H-119`:2078, `H-120`:2105 (`H-113`/`114`/`115` are further marked closed in-file by a
later revision, `W-A`/`W-E`). `architecture/meta/HANDOFF_NEXT.md:60` carries the matching `§2A · THE
BACKLOG, MEASURED (2026-09-04, proposals/2026-09-04-degree-sweep)`.

**Verdict: ABSORBED**, not LIVE — the sweep's content is in the register, the register is reference
(`CURRENT.md`'s season row: *"`hole_register.yaml` is NOT one of [the loop's registries]; its readers
are the corpus grader"*), and this tail owes it no further action. One partial confirmation the sweep
itself predates: `engine/season/seam/wrappers/sigma.py` (read at `:1-20`) and `requirements.yaml`'s
`R-09` row (`:489-524`, graded `partial`) show a σ-leverage roll landed 2026-09-11 (`U1`/ED-SC-0037) —
after the sweep, addressing exactly the on-ramp gap it measured. Not this tail's work; already moving.

## §2 · `2026-09-05-proceedings-subsystem/` — LIVE, SCHEDULED, 46 files / 19,835 lines

**Not a tail item — flagged and dispositioned as such.** `README.md:1-9` is unambiguous: PROPOSED,
HELD BACK IN FULL, nothing here runs, no `CURRENT.md` row moves. But `CURRENT.md:28` records Jordan's
ruling (ED-SC-0033, verbatim): *"this subsystem obviously owns all social contests"* — naming this
directory — and the same ruling repoints the two contest prizes at `rosters.yaml:441-446` here.
`workplans/2026-09-18-governance-settlement-behaviour-plan.md:156` and `:161` carry it as ratified-order positions
**PROC-A** (*"re-host the stress suite … `judging_set`; `arrangements.yaml`"*) and **PROC-B** (*"the
proceedings provider; the composed obstacle with a ceiling; THE BAR"*) — scheduled, ordered work, not
an undispositioned tail tree. **Verdict: LIVE, and out of this lane's scope to act on further.**

## §3 · `2026-09-04-social-contest-branches/` — SUPERSEDED, 15 files / 7,751 lines

A per-branch design (`01_SPINE`, `02_NEGOTIATION`, `03_INQUIRY`, `04_CONSENSUS`,
`05_RECONCILIATION` …), Fable-planned and Sonnet/Opus-authored, every file `PROPOSED`/`HELD BACK`
(verified: all fourteen numbered files carry a `## Status:` line saying so, greped directly). Jordan's
2026-09-05 framing ruling for proceedings — *"a game structure … and then the games within it are the
negotiation, parliamentary debate, tribunal, etc which are just defined parameters"* (quoted at
`proceedings-subsystem/README.md:18-22`) — rejects exactly the per-branch premise this tree is built
on: one branch per game-type versus one structure hosting all games as data. The proceedings tree
confirms it never even read this one — its own scope note (`README.md:100-109`, opened) states
*"`proposals/2026-09-04-social-contest-branches/` … were not read"*, honouring Jordan's from-scratch
instruction. Supersession by ruling, not by derivation. **`OUT_OF_SCOPE.md`** inside this same tree
(read in full) is a separate matter: five findings about *other* subsystems (victory-condition
Turmoil never written, three-homed territory ownership, mass-battle re-implementing engine
primitives) that Jordan explicitly parked 2026-09-04 (*"leave it, file the finding"*) — those survive
the supersession as findings, filed nowhere further, and creating that filing is not this pass's job.

## §4 / §5 · Emergent-narrative-primitives, v1 and v2

**v1** (7 files / 2,756 lines) is superseded on its own successor's word: `-v2/00_INDEX.md:9`, opened,
states *"Supersedes `proposals/2026-09-12-emergent-narrative-primitives/` (v1) … it remains in the
tree as the audit trail. v1 is not wrong in its facts; it is wrong in its **test**."* Clean
supersession, self-declared, nothing to adjudicate.

**v2** (5 files / 1,731 lines) is not superseded and not dead — read whole. `00_INDEX.md §4` (`:139`,
opened) states plainly what folds into the tree: *"What folds into `workplans/valoria_master_workplan_v7.md`
is six items, filed there as §7 · Amendment 1 (ED-IN-0218) — and the fourteen proposals are
deliberately not among them."* Confirmed: `valoria_master_workplan_v7.md:658` opens `## §7 ·
AMENDMENT 1 — 2026-09-12, ED-IN-0218`. So six items (of the fourteen ranked proposals) are tracked
and scheduled elsewhere; the other eight — including the highest-ranked, the chronicle render, and
Jordan's own #14, the information cluster — remain **open PROPOSED design options** in this
directory, held back from ratification-on-merge in full (`00_INDEX.md:3-8`), awaiting a decision only
Jordan can make. **Verdict: LIVE.** Nothing in it runs (`§4`, opened: *"the measurements … run; the
proposals do not"*), so §0.2 bars calling it done, and nothing in it is dead, so ORPHAN/SPENT would
misstate it. Not this lane's to decide further; correctly still sitting in `proposals/`.

## §6 · `2026-08-28-greenfield-systems-suite/` — SUPERSEDED, 12 files / 3,908 lines

`ARCHIVED.md:1-3` (opened) names its own supersession: *"ARCHIVED — this directory is the
PRE-CRITIQUE suite (v1). ## Status: SUPERSEDED (2026-08-29) by
`proposals/2026-08-29-greenfield-systems-suite-v2/`."* Kept deliberately unedited, with reasons
given (`ARCHIVED.md:6-10`) — a critique target must stay readable so the critique's citations
resolve. The census table lists v1 (this row) as NO / not held back and 12 files; v2 is a sibling
directory this lane was not asked to disposition, but its own fate is visible one hop further:
`workplans/2026-09-18-governance-settlement-behaviour-plan.md:63` (opened), the `SUPERSEDED BY architecture/` row,
names *"greenfield v1+v2"* explicitly among fourteen trees superseded by `architecture/`. **Chain,
two hops, both opened at the citing line: v1 → v2 (`ARCHIVED.md:3`) → `architecture/`
(`reconciled-program.md:63`).** Six of v1's own claims are additionally flagged **false** by the
critique (`ARCHIVED.md:23-32`, the six root-cause table) — a second, independent reason not to build
from it even absent the supersession chain.

## §7 · `2026-09-16-term-ownership/` — ORPHAN, mixed, 3 files / 1,830 lines, NO `## Status:` line

Read in full (`README.md`, all 92 lines) — its own banner is prose, not a heading: *"Status:
UNRATIFIED DRAFTS. Neither file is wired to anything… here because they were about to be lost with an
ephemeral container, not because they are ready."* Two unrelated files, two unrelated fates:

- **`key_type_registry.yaml` — SPENT.** Drafted to fix a real, named violation:
  `tools/export_key_types.py:62` reading `systems/_architecture/reference/key_type_registry_v30.md`
  (a `systems/**/*.md` parsed by an exporter, forbidden by §0.05 clause 2). The README's own audit
  (`:21-30`, opened) found the draft **did not fix it** — 199/758 strings carry the same baked-in `#`
  comments as the source `.md`, a faithful re-transcription rather than a schema fix — and recommended
  against landing it as-is. **That question is now moot rather than open.** `CURRENT.md:37` (opened):
  ED-IN-0232 retired the entire Key substrate, *"`engine/substrate/keys.py` … `engine/engine_params/
  key_types.json` … and five tools are deleted"*; confirmed on disk — `tools/export_key_types.py` no
  longer exists (`ls` fails). The exporter this file was drafted to fix is gone, and so is the `.md`
  it read as live prose (it is quarantined reference under `.designs/`, per the same row). Nothing
  reads `key_type_registry.yaml` or its target today. **SPENT**, cite `CURRENT.md:37`.
- **`offices_draft.yaml` — split.** 570 rows of governance-structure transcription. The README states
  (`:75-78`, opened) *"only a 6-row sliver reached the tree (`faction_leaders.by_faction` +
  `role_templates` in `engine/season/rosters.yaml`, PR #404)"*. Confirmed present:
  `rosters.yaml:930` opens `role_templates:`, `rosters.yaml:971` opens `faction_leaders:` (read at
  `:960-999`), six factions each, matching the tree's own count. **That sliver is ABSORBED.** The
  remaining ~564 rows and the `unsourced:` canon-defect notes (a dangling `ED-640` citation on the
  Hafenmark Militia ladder; a three-document "Cardinal of Justice" naming conflict; unpropagated
  post-rename refs in `faction_politics_v30.md` §3.5, `README.md:83-88` opened) are, in the README's
  own words, *"not reproducible by re-running a script"* and *"not been adversarially checked"* —
  read by nothing, filed as no ledger row. **ORPHAN.**

I checked whether the general "TERMS" ownership chain `CURRENT.md:20` credits to PR #404
(`names_index.yaml` → `tools/export_names.py --check` → `engine/engine_params/names.json` →
`engine/substrate/names.py`, with `rosters.yaml: factions` deriving via `from_names:`) is the same
chain that absorbed this tree. **It is not the same chain, and both halves are real, separate PR
#404 changes.** Verified: all four artifacts exist on disk; `rosters.yaml:928` (opened) carries
`from_names: faction`. But `names_index.yaml` (opened, header + grepped for `office`/`Crown`/
`Hafenmark`) carries only proper-noun/canonical-name entries for factions themselves (`world.crown`,
`world.hafenmark`) — no office ladders, no key types. The naming-gate chain and this tree's rescued
drafts are two different PR #404 payloads that happen to share a commit; do not conflate them.

**Table verdict: ORPHAN**, the dominant reading given 564 of 570 `offices_draft.yaml` rows plus
100% of `key_type_registry.yaml` are unclaimed, over the 6 rows that are ABSORBED and the one file
whose target is SPENT.

---

## What this pass does not do

No `ED`/`PP` allocated, no `## Status:` line flipped anywhere, no ledger row filed for the parked
findings named in §3 or §7 — those are for a session actually scoped to them, per those files' own
scope notes. This file creates no work; per its own table, none of the seven trees asks the season
loop for anything this pass is positioned to build.
