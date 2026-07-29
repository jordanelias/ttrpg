# Disposition Map — every open-items row → its one owner

## Status: AUTHORITATIVE OWNERSHIP TABLE (seeded at plan time, not at capstone time) — ED-IN-0091, 2026-07-29

**What this is.** One line for **every** row in `00_open_items_register.md` (OI-01..OI-59), plus a
separate line for every row-**half** whose two halves carry different classes or different owners.
Each line names exactly one owner. There is no "covered somewhere" cell and no blank.

**Why it exists.** The 2026-07-29 adversarial pass (`03_adversarial_review_2026-07-29.md`, F1)
found seven register rows owned by no wave and eleven row-halves silently dropped between the
register and `01_orchestration_plan_v1.md`. The plan's Wave-5 exit previously read "every row
accounted", which is a claim a capstone agent would have had to *invent* the evidence for. This
file is that evidence, written before the first wave runs: **Wave 5's exit is now "every row
matches this map"** — a diff, not a synthesis.

**Owner vocabulary** (one of these, never a prose hedge):

| Owner form | Means |
|---|---|
| `IN Wave N item M` | executed by this program, in that wave's PR (`01_orchestration_plan_v1.md` §3) |
| `MB plan <track>` | executed by the dedicated MB session (`audit/2026-07-26-mass-battle-fable-audit/03_execution_plan.md`, incl. its §12 INBOUND) |
| `PC plan <batch>` | executed by the dedicated PC session (`audit/2026-07-26-combat-balance-customization-state/combat_execution_plan.md`, incl. its §15 INBOUND) |
| `§5 fork N` | held for Jordan — nothing moves until it is ruled (`01_…` §5, whose table numbers 14 forks; the plan's prose calls these "§5 row N" interchangeably — same numbering, one docket) |
| `DEFERRED → <lane>` | build-scale work belonging to that lane's own workstream, listed in `01_…` §3.5 with its tracking pointer |
| `D (existing ruling)` | deliberately deferred by a ruling or plan that already exists — do NOT re-file |

---

## §1 · The map

| OI | Row (or half) | Class | Owner | Tracked in |
|---|---|---|---|---|
| OI-01 | Campaign loop cannot reach `combat_engine_v1` | B | `IN Wave 1 item 3` (dispatch bridge, ships flag-OFF per §2.2) | W1 PR + reach-oracle row |
| OI-02 | Field Investigation has no dispatch path | B | `IN Wave 1 item 3` (stub-wire) | W1 PR + reach-oracle row |
| OI-03 | `compute_accord_echo` uncalled | B | `IN Wave 2 item 1` | W2 PR |
| OI-04 | `propose_transfer` uncalled (one-way ratchet) | B | `IN Wave 2 item 2` | W2 PR |
| OI-05 | `generate_npc` zero call sites | B | `IN Wave 2 item 3` (IN-family golden re-record) | W2 PR, golden callout |
| OI-06a | `handoff_rules` import-orphan + fallback | B | `IN Wave 2 item 5` | W2 PR |
| OI-06b | `scale_transitions_v30` §3.3 EMPTY heading | J | `§5 fork 11` (ED-IN-0049) | §5 docket |
| OI-07 | `world.knots` / `world.settlements` vacuous | B | `IN Wave 2 item 4` | W2 PR |
| OI-08 | Key pub/sub has zero subscribers | B | `IN Wave 2 item 6` (minimal subscriber; render layer stays ED-IN-0073) | W2 PR |
| OI-09 | `engine.autoload.npc_ai` stub + orphan | B | `IN Wave 2 item 7` | W2 PR |
| OI-10a | 8 placeholder-named modules: stub-wire half | B | `IN Wave 1 item 4` (via OI-17) — **except** `altonian_reinforcements` → `MB plan §12 I1` | W1 PR / MB §12 |
| OI-10b | The placeholder **names** themselves | J | `§5 fork 12` | §5 docket · `registers/placeholder_names.yaml` |
| OI-11 | Two disjoint mass-battle code graphs | J | `MB plan §7 fork 1` (cross-session visibility row: `§5 fork 1`) | MB plan §7 |
| OI-12 | 12 other genuine import-orphans | B | `IN Wave 2 item 7` (full list enumerated there) | W2 PR |
| OI-13 | Dead PC-engine surface + unreachable elements | B/M | `PC plan E0/M12` + `PC plan E2/M9` (detail: PC §15 I2) | PC plan |
| OI-14 | Dead MB-tree machinery | B | `MB plan B3/E3` | MB plan |
| OI-15 | Orphaned tools (4) + registry-generator inconsistency | M | `IN Wave 4 item 5` | W4 PR |
| OI-16 | `tools/registry.py` facade unused; converged pointer artifacts absent | B | `IN Wave 4 item 5` | W4 PR |
| OI-17 | The Pass-2l armature stub class (~20 modules) | B | `IN Wave 1 item 4` — **except** the MB-owned file → `MB plan §12 I1` | W1 PR + `stubs.count` ratchet |
| OI-18a | Contest GAMES router: **self-flag** half | B | `IN Wave 1 item 4` (stub-wire scope) | W1 PR |
| OI-18b | Contest GAMES **build** (consensus/negotiation/inquiry) | J | `§5 fork 14` → SC P0 docket (ED-SC-0003..0005) | §5 docket · SC lane |
| OI-19 | Partial `NotImplementedError` branches (4) | B | `IN Wave 1 item 4` (stub-wire scope; `resolver.py:51` abstract base = benign, no change) | W1 PR |
| OI-20a | `faction_politics` contract has no `state:` block | B | `IN Wave 3 item 3` | W3 PR |
| OI-20b | `faction_politics` has **zero sim representation** | B | `DEFERRED → FA` | `01_…` §3.5 · `HANDOFF_FA.md` |
| OI-21 | Fabricated `scene_outcome.battle_concluded` emit row | J | `MB plan E1` (visibility row: `§5 fork 2`) | MB plan §8 |
| OI-22a | `scene.combat_resolved` / `_felled` dangling | B | `IN Wave 3 item 1` | W3 PR |
| OI-22b | `env.crisis` — 2 emitters, zero consumers | J | `§5 fork 4` | §5 docket |
| OI-23 | `mass_battle` contract `consumes: []` / `state: []` | D | `MB plan E6` (honest `status`/`gap_notes` now) | MB plan §8 |
| OI-24 | Contract truth debt (npc_behavior residue, `doc:` repoint, unvalidated `emits:`) | M/B | `IN Wave 3 item 3` | W3 PR |
| OI-25 | Silent emitters: `settlement_layer` gates, `ci_political`, `victory`, `territorial_piety` | B | `IN Wave 3 item 7` | W3 PR · ED-IN-0014 |
| OI-26 | `_emit()` vocabulary → `scene.combat_*` mapping | B | `PC plan §15 I4` (scheduled, post-E3); IN-side registry half → `IN Wave 3 item 1` | PC §15 · W3 PR |
| OI-27a | Articulation §3.1 omissions + core-five rendering path (ED-IN-0004 slice) | B | `IN Wave 3 item 1` | W3 PR |
| OI-27b | `meta.cascade_cluster_event` unregistered; `state.opinion_revised` registry↔table contradiction; zoom-trigger `type_id`s | J | `§5 fork 11` | §5 docket |
| OI-28 | `causes[]` zero instances; `targets[]` one emitter; 20 `!A6` debts | B | `IN Wave 3 item 5` | W3 PR |
| OI-29 | Dual-emit attribution (3 types) | J | `§5 fork 8` | §5 docket |
| OI-30a | Pointer debt Category B (register the scalars) | B | `IN Wave 3 item 4` | W3 PR |
| OI-30b | Category C2 (are npc beliefs/concerns/projects registry quantities) | J | `§5 fork 11` | §5 docket |
| OI-31a | J-36 off-bus writers + `parliamentary_vote` L-restoration | J | `§5 fork 7` | §5 docket |
| OI-31b | ED-WR-0003 hard-coded `private_observers` at 6 emit sites | B | `IN Wave 3 item 5` (same emitters; ED files to **WR**) | W3 PR · `HANDOFF_WR.md` |
| OI-32a | `MS` ownership undeclared; `VICTORY_THRESHOLD` dead; `game_state.py:101` dead field | M | `IN Wave 3 item 3` (MS declaration) + `IN Wave 4 item 5` (dead constant/field) | W3/W4 PRs |
| OI-32b | `Turmoil` write-dead → victory gate trivially satisfiable | J | `§5 fork 7` | §5 docket |
| OI-33 | `settlement_layer` L/PS `bucket:` tag undecided | J | `§5 fork 13` | §5 docket |
| OI-34 | Convergence Markers: no detector, Key type, contract, or sim | B | `DEFERRED → WR` (narrative stage) | `01_…` §3.5 · ED-IN-0003 |
| OI-35 | `scale_signature` cannot represent province/duchy/country | J → M | `§5 fork 5`; mechanical enum+registry edit lands in `IN Wave 3` on the ruling | §5 docket |
| OI-36 | Master finding: 2 of 7 Key-delivery directions live | B (roll-up) | `IN Wave 5 item 2` (reach-oracle direction census) | W5 PR |
| OI-37 | L/PS pipeline fully SPEC-ONLY (`lps_inert_check` 100/100 red) | B | `DEFERRED → SE` — **the SE lane's own highest-priority item** | `01_…` §3.5 · `HANDOFF_SE.md` |
| OI-38 | No event_deck runtime (28-card Goldenfurt deck prose-only) | B | `DEFERRED → SE` | `01_…` §3.5 · `HANDOFF_SE.md` |
| OI-39 | NPC ambition-tick absent from the Accounting cascade | B | `DEFERRED → WR` (NPE; lane confirmed by `§5 fork 9`) | `01_…` §3.5 |
| OI-40a | 4 scale vocabularies unreconciled (IN half) | B/M | `IN Wave 3 item 3`; the EXPLORATORY cross-scale locality metric stays `D (existing ruling)` | W3 PR |
| OI-40b | `Mass Battle`/`Mass Combat` token class + patch-register coverage (MB half) | M | `MB plan E4/E5/E8` + `MB plan §12 I4` | MB plan |
| OI-41 | Design-blocked cross-scale mechanics (caste, CI-consent, insurgency, fracture, §5.2/§5.3, territorial-tier) | B/J | ruling half `§5 fork 11`; build half `DEFERRED → FA/SE/WR` per its own dockets | §5 docket · `01_…` §3.5 |
| OI-42 | Cross-tick convergence unproven; `decay()` fork OF-3 | D/J | `D (existing ruling)` (propagation_spec §5) + `§5 fork 11` (OF-3) | §5 docket |
| OI-43a | ED-1051: `engine_clock` `doc:null` flip | J | `§5 fork 3` | §5 docket |
| OI-43b | Doc homes for the other 8 `doc:null` modules | B | `DEFERRED → FA/SE/WR/IN` per module | `01_…` §3.5 |
| OI-43c | Retire-candidates (`settlement_economy`, `campaign_architecture`) | J | `§5 fork 9` | §5 docket |
| OI-44 | PC pool formula duplicated with divergence | M | `PC plan §15 I1(a)` (rider on E0/M15) | PC §15 |
| OI-45 | ≈8.0 percussion-authority anchor triplicated | M | `PC plan §15 I1(b)` (rider on E0/M15) | PC §15 |
| OI-46a | `config.py`'s single-place claim false (~60+ knobs) | B | `PC plan E0/M15` (279-literal census subsumes it) | PC plan §3 |
| OI-46b | `capabilities.py` name-keyed second truth | D | `D (existing ruling)` — quarantined to diagnostics, watch only | PC plan |
| OI-47 | MB engine: 7 duplicated rules, 10 unkeyed per-cell maps, epsilon at producer | B | `MB plan A2/B1a-c/B2` (forks 6/7 held there) | MB plan §3/§4 |
| OI-48a | ED-SC-0004: which Argue-pool formula is canon | J | `§5 fork 6` | §5 docket |
| OI-48b | ED-SC-0011: the personal-party contest bridge | B | `DEFERRED → SC` | `01_…` §3.5 · `HANDOFF_SC.md` |
| OI-49 | Three competing faction-power formulas; no shared aggregation contract | J | `§5 fork 11` (Field/Gauge primitive) | §5 docket |
| OI-50 | Two attribute rosters; no `Character` dataclass; Combat Pool ×3 | D/J | `§5 fork 10` — ED-IN-0029 docket UNRULED, **do not bind** | §5 docket |
| OI-51 | Ruled-but-unexecuted class (ED-871, ED-912, forks 2/11, conviction_track) | M | `IN Wave 4 item 5` | W4 PR |
| OI-52a | `game_state ↔ npe` cycle | M/B | `IN Wave 4 item 2` | W4 PR |
| OI-52b | 6-module `social_contest.sim.contest.*` cycle | D | `D (existing ruling)` — documented intentional-during-rebuild | — |
| OI-52c | `massbattle ↔ units` + 5-module `tests.sim.mass_battle.*` cycles | B | `MB plan §12 I2` | MB §12 |
| OI-53a | Dead retired-`sim/` roots in live tooling (3 sites + `ci_audit_registry_check.py:23`) | M | `IN Wave 4 item 3` (route through `ci_common.sim_reference_roots()`, extend the existing guard) | W4 PR |
| OI-53b | `test_persubunit_stress.py:17` redundant duplicate `sys.path` insert | M | `MB plan §12 I3` (corrected: not a retired root; zero behavioral stakes) | MB §12 |
| OI-54 | Contract↔code correspondence is a name-match black hole | B | `IN Wave 4 item 4` | W4 PR |
| OI-55 | Orphan-detector integrity (`__init__` misresolution, CLI noise, no known-answer coverage) | B | `IN Wave 0 item 2` | W0 PR |
| OI-56 | No pipeline-reach oracle exists | B | `IN Wave 1 item 2` (the oracle **is** §2.3) | W1 PR |
| OI-57 | Currency-layer orphans (`franchise_v30` et al.) | M | `IN Wave 4 item 5` | W4 PR |
| OI-58 | Stale audit families (vector-audit 133, lexicon 8, decisions 4) | M | `IN Wave 5 item 1` | W5 PR |
| OI-59a | NPC family has no owning workplan lane | J | `§5 fork 9` | §5 docket |
| OI-59b | Both integration hubs are `[ASSUMPTION]`-grade (grounding) | B | `DEFERRED → WR` (pending the fork-9 lane ruling) | `01_…` §3.5 |

---

## §2 · Completeness accounting

- **59 register rows → 77 map lines.** 16 rows split because their halves differ in class or owner
  (OI-06, 10, 18, 20, 22, 27, 30, 31, 32, 40, 41, 43, 46, 52, 53, 59); OI-43 and OI-52 split three
  ways, the other 14 split two ways. `43 + (14×2) + (2×3) = 77`.
- **Primary-owner distribution** (one owner per line, counted once): **IN waves 35** · **MB plan 8**
  · **PC plan 5** · **§5 forks 19** · **DEFERRED→lane 8** · **D (existing ruling) 2**. `35+8+5+19+8+2
  = 77`. Four lines name a *secondary* consumer as well — OI-10a and OI-17 carve the MB-owned file
  out to `MB plan §12 I1`, OI-26's registry half lands in `IN Wave 3`, OI-35's mechanical edit lands
  in `IN Wave 3` once fork 5 is ruled, and OI-41 sits in `§3.5` for its build half while its ruling
  half is `§5 fork 11` (so `§3.5` lists 9 entries against this table's 8 primary-DEFERRED lines).
- **No line reads "unowned", "TBD", or "somewhere in W5".** If a future edit to the register adds a
  row, this file gains its line in the same PR — that co-edit is what Wave 5 diffs against.
- **Split-half rule:** a row is split here whenever its two halves would land in different PRs. A
  row whose halves land in the same wave stays one line (e.g. OI-24's M and B slices).

*Companions: `00_open_items_register.md` (the rows) · `01_orchestration_plan_v1.md` (the waves) ·
`03_adversarial_review_2026-07-29.md` (why this file exists).*
