# mc_v18 retirement — bringing the faction/strategic and mass-battle scales into `engine/season/`

## Status: PROPOSED (2026-09-27). HELD BACK IN FULL. Nothing here ratifies on merge (ED-1094 does not apply — the plan's own critical-path clause is `needs_jordan`, filed as `ED-IN-0279`).
## Lane: `IN` (cross-cutting: retiring `engine/mc_v18.py`). The one live ruling clause is filed under `IN` because the program is IN-scoped; it concerns mass battle specifically and an `MB` lane citation would be equally defensible — noted so nobody re-files it as a duplicate.
## Produced by: a read-only Fable 5.1 planning pass, across two hand-backs in one session, working tree at `f672c84`. Every path was opened; every count carries the command that reproduces it. Nothing was written to the tree by the pass itself — this document is the orchestrator's transcription of its two reports.
## Supersedes: nothing. It reconciles into one sequence, rather than replaces: `proposals/2026-09-17-governance-and-holdings-r2/`'s unbuilt items (all 11 re-mapped onto the ratified order below, not re-designed), `proposals/2026-09-18-the-gather/02_SETTLEMENTS.md` and `03_DECISIONS.md`'s still-open rows, `proposals/2026-09-12-emergent-narrative-primitives-v2/`'s 8 open ranked proposals, and `proposals/2026-09-16-term-ownership/offices_draft.yaml`.
## Grade under CLAUDE.md §0.2: `paper` throughout — a plan, not an execution artifact. Section 0 below is `measured` (each premise-correction carries the command/citation that closes it).

---

## 0. Corrections to the brief, caught before planning (read first)

| the orchestrator's brief said | the tree actually says |
|---|---|
| the strategic-to-cell-Unit adapter doesn't exist; `Subunit.cells_float` blocks it (per `tests/valoria/test_j2_mass_battle_seam.py`, dated 2026-08-06 / ED-MB-0065) | Already fixed by the 2026-08-24 port. Run directly: `_faction_to_unit` builds real units, `resolve_mass_battle(F,F,None,W)` returns a real result. `registers/editorial_ledger_mb.jsonl` already carries a 2026-09-15 row superseding ED-MB-0065 as "a process guard whose premise is spent." `test_j2_mass_battle_seam.py` should be deleted (Stage M0 below), not treated as a live blocker |
| R-04's `blocks: [W10, W13]` names the engine work still needed | Those are corpus-authoring items (case overlays, arc re-authoring), not engine work. The engine-side owner is the ratified plan's position 20 |
| roughly 78 of 136 mc_v18-tied tests, 57% of the blocking `sim-regression` job | Measured: 45 of 76 tests in the six importing files; only 22 of those 45 actually call an mc_v18 symbol, 23 are incidental (import the module, never use it) |
| "no economic pressure on any office, and no verb is proposed" — cited from `proposals/2026-09-18-the-gather/01_GOVERNANCE.md` | Wrong file — it's `proposals/2026-09-17-governance-and-holdings-r2/05_LEDGER_AND_BUILD.md:1659`. Substance unaffected |
| `Office.upkeep` was deleted per r2's own proposal | Still present, unused, at `engine/season/state/carriers.py:644` — the r2 deletion was never executed. Cheaper fix available: give it a reader rather than building something new |
| `ED-SE-0051` (hearth-capacity ruling)'s ledger row is still open/`needs_jordan: true` | **Closed 2026-09-19** (`registers/editorial_ledger_se_archive.jsonl:52`, `status: ruled`, `needs_jordan: false`). Not a live item — the orchestrator was working from a stale read |
| hearth capacity has zero of: capacity query, `dwelling` site kind, `houses`, `shelters` | `dwelling` landed 2026-09-26 (`ED-IN-0274`; `rosters.yaml site_kinds` now includes it, 211 minted). Only the capacity query, `houses` count, and `shelters` floor remain missing |
| workplan v7's Amendment 1 folded "6 of the 14" emergent-narrative-v2 proposals | It folded six unrelated amendment items that happen to touch overlapping ground, not 6 of the 14 ranked proposals. All fourteen proposals' actual content is still fully open (§3, below, cites which items overlap with other work already in this plan) |
| narrative proposal #12 ("a telling renews the belief it's about") already landed as R8.1 | No — R8.1 (`engine/season/tests/test_seen_claim.py`) is the `seen` partial-observation claim, a different mechanism. #12 is still open |

---

## 1. Frame

**Mass battle is retained and untouched.** `systems/mass_battle/sim/` is RETAINED per `engine/season/requirements.yaml:91-95` and under active MB-lane development this week (ED-MB-0067..0075 — officer/span-of-control, terrain derivation, the feigned-retreat trigger, a rout-cascade sweep). Nothing in this plan ports, rewrites, pauses, or re-goldens `run_battle`, `resolve_mass_battle`, `orchestration.py`, or any of that work. The only thing retiring is `engine/mc_v18.py`'s role as the **caller** (`_faction_actions_callback -> faction_take_action -> _try_conquest -> resolve_mass_battle`). Stage M3 below builds a replacement caller inside `engine/season/` that reaches the same engine through a composition role; `massbattle.py` keeps its existing `resolve_mass_battle` entry for the old spine until Step B, and gains one new season-facing entry beside it.

Deleting `mc_v18` is **not** retiring the older prototype spine underneath it: `engine/autoload/{game_state,victory,scene_slate,engine_clock}.py`, `engine/cross_scale/*`, `systems/overview/sim/{season,accounting}.py` are imported by 39 production files outside tests/tools. Their retirement is a separate, later step ("Step B" / 09-06 plan item 4.9), gated on the season loop actually subsuming their scale — not on this plan.

The licensed route to a subsystem outside `engine/` is a composition role (`references/module_contracts.yaml composition_roles:`, resolved by string at first call through `engine/engine_params/composition.json`, behind `tools/export_composition.py --check`) — never a new `sys.path` seam (`PATH_SEAM_ALLOWED` stays `{'substrate/pc_engine.py'}`, shrink-only).

---

## 2. Overlaps found and resolved to one owner

- **The bodies clock** — settlements' P2, narrative proposal #5, and one of the ratified plan's own routes — are the same item. One build (Stage S4).
- **Founding** — narrative #9, an r2 proposal item, and settlements' P4 (already superseded by r2 §A.6–A.7) — one item (Stage S3).
- **The counterparty** (narrative #8) — already done, 2026-09-13.
- **The information cluster** (narrative #14, credited to Jordan by name in its own document) — the same surface the ratified plan already names "R-04's surface." No new ruling needed; proposed as its own position (Stage D1-a).
- **A telling renews belief** (#12) merges into an already-positioned item (15b).
- **Governance-and-holdings-r2's 11 unbuilt items** — all 11 are already individually mapped onto positions in the existing ratified build order (`workplans/2026-09-18-governance-settlement-behaviour-plan.md` §3.4); none is new work, it was scattered across proposal documents rather than the one plan.
- **The term-ownership office data** (564 unverified rows, `proposals/2026-09-16-term-ownership/offices_draft.yaml`) is candidate seed content for the same `offices.yaml` position the ratified plan already schedules.

---

## 3. The sequence — ON-PATH (required to delete mc_v18) vs ADJACENT (positioned, not blocking)

### ON-PATH

- **M0** (now, no ruling). Delete `tests/valoria/test_j2_mass_battle_seam.py` (premise superseded, §0). Keep `test_evacuation_plan.py`'s `massbattle.py` keep-pin.
- **M1** (now). Split the four "incidental" importer test files: delete the handful of tests per file that actually call an mc_v18 symbol (successor coverage named per file — mostly already exists); keep the rest; drop each file off `ALLOWED_IMPORTERS` as it clears. Target roster: `{test_mc_v18_regression, test_f7_smoke_oracle, balance_oracle, campaign_output_probe, trace_execution_phases}`.
- **M2** (now). Build `engine/season/queries/faction_q.py` — a `Faction` view (`resolve(w, prop) -> Faction(members, holdings, seats, head)`) composed from existing `world_q` queries, deliberately never promoted into `World` itself (guarded by a test). Plus `at_war(w, a, b)` off a `WAR`-mood Proposition with live commits (needs one new `proposition_moods` roster row). Fixtures: `harness/governance_spine.py`, `populated.build_realm(0)`. Propose splitting the ratified order's position 20 into 20-i (this stage, ungated) / 20-ii (the corpus re-scales, gated ★) by PR amendment (ED-IN-0270 precedent).
- **M5** (now, parallel). `tools/balance_oracle.py` ported into `engine/season/harness/arms.py`; `tools/campaign_output_probe.py` and `tools/trace_execution_phases.py` retired outright (superseded by `harness.report`/`harness.delta` and the season driver's own explicit steps, respectively).
- **M3** (after M2). New `engine/season/seam/wrappers/mass_battle.py` provider (`@provider("contest", "mass_battle")`), one new `rosters.yaml` row, one new `composition_roles:` entry, and a new season-facing `resolve_field(side_a, side_b, terrain, rng)` entry point on `massbattle.py` itself (its existing `resolve_mass_battle` stays, untouched, for the old spine). Same wrapper pattern already used for personal combat and social contest. Degree read off the engine, never mapped in a table.
- **M4 (after M3) — the one item that needs Jordan.** No verb row declares `contests: "a field"`, so nothing can call a battle from inside a season yet. Two linked clauses, filed as `ED-IN-0279` (see §5):
  - (a) which verb opens a field battle — recommended: one new acted verb, a seated officeholder acting against a rung, with that rung's holder bound as the contested party (the `kill / wound` pattern).
  - (b) what a loss actually writes — recommended: no amendment to the ratified Tenure-write rules; a battle writes casualties only, and territory/office change hands afterward through the loser's own release, a formal revocation, or death.
- **M6** (after M4 + M5, terminal). Give the two remaining golden/regression test files real season-side successors (a same-seed hash pin; an actual battle executing from a real in-season decision — the `battles_mean` golden's true successor). Then: `ALLOWED_IMPORTERS == set()`, `mc_v18.py` deleted with a `FORK:` row.

### ADJACENT — positioned in the existing ratified order, none of it blocking M0–M6

- **G2 — economic pressure on offices** (after ratified positions 6 and 17a; propose 17b). Zero new primitives: treasury = `Rung.stores` at the office's own rung; payment = the existing `transfer` verb; `oblige` Tenures carry a term (T-n) the paying act renews; unpaid terms mature and shrink the office's establishment toward revocable. `Office.upkeep` finally gets a reader (a per-obligee amount, typed, fixture default with a 3-point sweep) — satisfies the ratified `Seat :=` line without amending it.
- **G3 — demand and delivery between settlements** (after position 15c, beside 24f; propose 19d). No new verb: two new read-only queries (`demanded`, `delivered`) plus wiring the *existing* `transfer` verb's operands from a shortfall claim. Includes the deliberately-scarce test world needed to actually exercise it (today's default world runs a 35x surplus, so `transfer` is refused every time it's attempted, zero times reaching effect).
- **S2 — hearth capacity's remaining piece** (`24d-ii`, lands with its already-scheduled first caller). `dwelling` is done; the query, `houses` count, and `shelters` floor remain. No ruling — shape already ruled (ED-SE-0051, closed).
- **S3 — works & founding** (`24e`, after positions 15/15c/24d-i). A `found` verb, a `works`-kind Record, five site-family rows. `create_record kind:works` was measured firing 69x/season with nowhere for it to land.
- **S4 — the bodies clock + individuation** (P2/P3 ≡ narrative #5; after 24d-ii and 24f's cohort producer and `ED-IN-0247`'s value). Licensed by an existing ruling but has no position yet in the order — propose `24g`.
- **S5 — risk-of-revolt, forswearing costs, dispensation-as-document** (settlements P5–P7). Explicitly outside the current settlement build block. Two are buildable whenever scheduled; the third (dispensation) needs a written refusal in `verb_table.yaml:117` overturned first — Jordan's, filed, not urgent.
- **D1-a — the information cluster** (narrative #14, after M2 + position 15). A Record whose `subject_matter` is a frozen `faction_q.resolve(...)` snapshot, commissioned by an act, read free by holders, forgeable and destructible. Proposed as `20-iii`. No new ruling.
- **D1-b — the remaining narrative proposals** (#1 chronicle render, #2 patron, #3 embezzlement, #6 complication-as-modal, #7 intelligence-before-action, #10 casus belli, #11 the writ) — each given a home in the existing order or paired with an already-open item (§4). #1 specifically needs its own small proof-of-concept built first, per the proposal's own text, before any render work.
- **C1/C2/C3/C4 — the decisions-layer trio.** 6a/6c (pursuit-cells content + re-authored projection) derive automatically once Jordan supplies the actual cell values — no code change needed downstream of that. 6b (the moral-value-basis rename) — recommend a manual sweep (51 files) over restoring the deleted rename tool; a green test (`test_conviction_roster_single_owner.py`) already guards against a second roster shipping; the season-side half of this rename is already partly done by hand (`ED-IN-0268`). 6f's shape is contested by an existing proposal's own §4 finding — filed, Jordan's. The "two competing build orders" collision is mostly already resolved by Jordan's own 2026-09-18 ruling that there is one single plan; one narrow sub-question survives (§5).
- **D2 — term-ownership's office data.** `offices_draft.yaml`'s 570 rows are usable seed content for real NPC officeholders, once verified against canon (it was transcribed by an agent and never checked). Its three flagged canon defects (a dangling citation, a three-way naming conflict, some unpropagated renames) are not brought to Jordan as-is: an existing precedence ruling (which canon source outranks another on conflict) already closes two of them, and the third is moot (the conflicting source is quarantined and nothing live cites it). Filed as ordinary ledger rows with their closing test named, not as `needs_jordan` — override is available if Jordan wants them put to him regardless.
- **Step B** — retiring the old prototype spine entirely, after the above settle. Separate effort, not on this plan's path.

---

## 4. Jordan roster — every live decision, one list

**On the critical path:** M4 (`ED-IN-0279`) — the only new item this plan adds.

**Real, adjacent, not blocking anything:** the pursuit-cells' actual content (nothing can derive it); whether `comply` is one verb or two (a pre-existing open fork); complication-as-modal-outcome (a re-tune of fixtures Jordan already owns); overturning the written refusal blocking P7; one narrow residual of the two-build-orders question (how a scarcity cost sums or applies precedence — most of that question is already settled by the 2026-09-18 "one single plan" ruling).

**Explicitly not Jordan's, so nobody re-asks:** hearth capacity's ruling (closed 2026-09-19); `Office.upkeep`'s mechanism; who performs the sideways settlement transfers; where the bodies-clock work sits in the order; the rename-tool-vs-hand-sweep choice for 6b; the "R7" identifier naming collision (a documentation fix, `CLAUDE.md` §4); the three term-ownership canon defects (§3, D2).

---

## 5. Filed: `ED-IN-0279` (needs_jordan)

Recorded in `registers/editorial_ledger_in.jsonl`. Two clauses, both with a recommended default (M4 above). Stages M0–M3, M5 do not wait on it; M6 does.

---

## 6. The gate

**Required:** M0 → M1 → M2 → M3 → **M4** → M5 → M6.
**Not required — sequenced so nothing is lost, none of it blocking:** everything in §3's ADJACENT list.

- `tests/valoria/test_mc_v18_is_deprecated.py::ALLOWED_IMPORTERS == set()`, both ratchet tests green (intermediate, falsifiable state).
- `mc_v18.py` and its own ratchet test deleted together, with a `FORK:` row.
- Zero remaining mentions anywhere outside the licensed historical records (the fork ledger, `CLAUDE_RATIONALE.md`).
- Full suite green once, at the close.
- The successor artifacts must have actually **run** in the same PR — a same-seed hash pin, a two-arm balance comparison, and a battle executing from a real chooser-formed decision — or the gate does not open.

## What was not independently verified

This plan has not had a structurally independent critic pass — it is one planning agent's self-checked work, across two rounds, that caught several real errors in its own brief (§0) but has not itself been adversarially attacked by a second reader. Treat it as `PLAUSIBLE` rather than settled, per this repository's own standard for a producer's disposition of its own lane (`proposals/2026-09-18-the-gather/README.md` §4).

### Files most relevant to building this
`engine/season/seam/wrappers/combat.py` (the pattern Stage M3 copies) · `engine/season/queries/world_q.py` (what `faction_q` composes from) · `systems/mass_battle/sim/massbattle.py` (gains one new entry point, otherwise untouched) · `engine/season/rosters.yaml` (new provider row, upkeep fixture) · `workplans/2026-09-18-governance-settlement-behaviour-plan.md` (the one ratified order everything above slots into).
