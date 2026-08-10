# Victory — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/victory/` · **Lane:** `IN` · **Contracts:** `victory`
**Code roots traced:** `engine/autoload/victory.py`, `engine/mc_v18.py`, `engine/autoload/game_state.py`
(dataclass definitions only), `references/module_contracts.yaml`, `engine/tests/test_f7_smoke_oracle.py`,
`engine/tests/test_parliamentary_transfer_bridge.py`, `tests/valoria/_campaign.py`
**Traced at:** `6545067`

`systems/victory/` itself holds no `.py` — per standing rule 1, this skeleton traces the code
wherever it actually lives (`engine/autoload/victory.py` + inline in `engine/mc_v18.py`), not the
doc folder.

## 1. Entry points

| Callable | Anchor | Called-by |
|---|---|---|
| `check_peninsular_sovereignty` | `engine/autoload/victory.py:52 check_peninsular_sovereignty` | `engine/autoload/victory.py:107 check_all_factions` |
| `check_all_factions` | `engine/autoload/victory.py:103 check_all_factions` | `engine/mc_v18.py:270 run_campaign` |
| `reset` | `engine/autoload/victory.py:47 reset` | `engine/mc_v18.py:225 run_campaign` |
| `run_campaign` (fallback path lives here — see §3 S5) | `engine/mc_v18.py:212 run_campaign` | not enumerated — see note below |
| `run_batch` | `engine/mc_v18.py:311 run_batch` | `engine/mc_v18.py:334` (`__main__`) |

No other production call site imports `check_all_factions` / `check_peninsular_sovereignty` /
`reset` anywhere in the tree (repo-wide grep for the three symbol names outside `victory.py`,
`mc_v18.py`, and test files returns nothing). `run_campaign`/`run_batch` are `mc_v18` orchestrator
callables with call sites outside this subsystem's scope to enumerate exhaustively — e.g.
`tools/build_fork.py:353` subprocess-executes `run_campaign` as its fork-verification falsifier.
This subsystem owns only the inline fallback logic inside `run_campaign` (§3 S5), not the
callables `run_campaign`/`run_batch` themselves.

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| `world` (`World`) | arg | `game_state.create_world` | `engine/mc_v18.py:224 create_world` |
| `faction_id` | arg | iteration over `world.factions` | `engine/autoload/victory.py:106 check_all_factions` |
| `world.factions[faction_id]` (`Faction`) | world-state | `game_state.Faction` | `engine/autoload/victory.py:59 check_peninsular_sovereignty` |
| `world.territories` (`dict[Territory]`) | world-state | `game_state.Territory` | `engine/autoload/victory.py:65 check_peninsular_sovereignty` |
| `world.clocks['Turmoil']` | world-state | `game_state.create_world` init (never rewritten — §7) | `engine/autoload/victory.py:73 check_peninsular_sovereignty` |
| `game_state.ALL_PLAYABLE_15` | registry | `engine/autoload/game_state.py:37 ALL_PLAYABLE_15` | `engine/autoload/victory.py:57 check_peninsular_sovereignty` |
| `VICTORY_THRESHOLD` / `ACCORD_MIN` / `PS_MAX` / `SUSTAIN_SEASONS` (module constants) | param | `engine/autoload/victory.py:27-30` | `engine/autoload/victory.py:70 check_peninsular_sovereignty` |
| `DEFAULT_PARAMS['VICTORY_THRESHOLD']` | param | `engine/mc_v18.py:42 DEFAULT_PARAMS` | `engine/mc_v18.py:53 VICTORY_THRESHOLD` (declared, unread — see §7) |
| `params` override dict | param | caller of `run_campaign` | `engine/mc_v18.py:229-230 run_campaign` |
| `world.factions[fn].parliamentary` (fallback) | world-state | `game_state.Faction` | `engine/mc_v18.py:280 run_campaign` |
| `world.factions[fn].L`, `world.factions[fn].territories` (fallback) | world-state | `game_state.Faction` | `engine/mc_v18.py:284 run_campaign` |
| `world.territories[tid].owner` (fallback) | world-state | `game_state.Territory` | `engine/mc_v18.py:283 run_campaign` |

## 3. Flow

- **S1** [entry] `run_campaign` builds a fresh `world` via `game_state.create_world`. `engine/mc_v18.py:224 create_world`
- **S2** [write] `victory.reset()` clears the module-level qualifying-streak tracker for the new campaign. `engine/mc_v18.py:225 reset`
- **S3** [loop] Per-season loop, bounded by `max_s`. `engine/mc_v18.py:260`
  - **S3.1** [gate] Loop breaks immediately if `world.winner` is already set (from a prior iteration). `engine/mc_v18.py:261 run_campaign`
  - **S3.2** Season composition (`run_season`) executes — outside this subsystem, prerequisite only. `engine/mc_v18.py:267 run_season`
  - **S3.3** [emit] `victory.check_all_factions(world)` is called — see S4 for its internal flow. `engine/mc_v18.py:270 check_all_factions`
  - **S3.4** [loop][write][gate] Results are iterated in sorted order; the first `won=True` result sets `world.winner` and breaks. `engine/mc_v18.py:271-274 run_campaign`
- **S4** (`check_all_factions` internal flow, entered at S3.3)
  - **S4.1** [loop] Iterates every `faction_id` in `world.factions`, calling `check_peninsular_sovereignty` for each. `engine/autoload/victory.py:106-107 check_all_factions`
  - **S4.2** [gate] Faction lookup; held-territory set computed as the intersection of `ALL_PLAYABLE_15` and territories this faction owns. `engine/autoload/victory.py:59-67 check_peninsular_sovereignty`
  - **S4.3** [gate] `territory_count_ok`: held count against `VICTORY_THRESHOLD`. `engine/autoload/victory.py:70 check_peninsular_sovereignty`
  - **S4.4** [gate] `accord_ok`: every held territory's accord against `ACCORD_MIN` (vacuously `False` if none held). `engine/autoload/victory.py:71 check_peninsular_sovereignty`
  - **S4.5** [gate] `ps_ok`: `world.clocks['Turmoil']` against `PS_MAX`. `engine/autoload/victory.py:73-74 check_peninsular_sovereignty`
  - **S4.6** [branch] `qualifies` = conjunction of S4.3-S4.5. `engine/autoload/victory.py:76 check_peninsular_sovereignty`
  - **S4.7** [write] Module-level `_qualifying_streak[faction_id]` incremented if qualifying this season, else reset to 0. `engine/autoload/victory.py:78-81 check_peninsular_sovereignty`
  - **S4.8** [gate] `won`: consecutive qualifying-season count against `SUSTAIN_SEASONS`. `engine/autoload/victory.py:84 check_peninsular_sovereignty`
  - **S4.9** [emit] `VictoryResult` returned per faction. `engine/autoload/victory.py:96-100 check_peninsular_sovereignty`
  - **S4.10** [emit] `check_all_factions` sorts all results by `(-won, -held)` and returns the list. `engine/autoload/victory.py:109-110 check_all_factions`
- **S5** [branch][gate] After the season loop ends (winner found, or `max_s` exhausted without one): if `world.winner` is still unset, the fallback engages. `engine/mc_v18.py:277 run_campaign`
  - **S5.1** [loop][gate] Iterates `world.factions`; skips any faction with `parliamentary` falsy. `engine/mc_v18.py:279-280 run_campaign`
  - **S5.2** [gate] Held-territory count recomputed directly against `ALL_PLAYABLE_15` and `Territory.owner` — independently of `victory.py`. `engine/mc_v18.py:282-283 run_campaign`
  - **S5.3** [write] Per-faction score composed from held count, `Faction.L`, and `len(Faction.territories)`. `engine/mc_v18.py:284 run_campaign`
  - **S5.4** [write][gate] `world.winner` set to the highest-scoring faction, if any scores were produced. `engine/mc_v18.py:285-286 run_campaign`
- **S6** [emit] `CampaignResult` is built; its `winner` field carries whatever `world.winner` holds (real win, fallback win, or `None` if `scores` was empty). `engine/mc_v18.py:292-293 run_campaign`
- **S7** [loop][emit] `run_batch` runs `n` campaigns, tallies `winner` into `Counter`, and emits `win_share` / `all_winners`. `engine/mc_v18.py:314-327 run_batch`

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| `VictoryResult` (per faction) | struct | `check_all_factions` aggregation | `engine/autoload/victory.py:96-100 check_peninsular_sovereignty` |
| `list[VictoryResult]` (sorted) | struct | `run_campaign` season loop | `engine/mc_v18.py:270-271 run_campaign` |
| `world.winner` write — real GD-1 path | world-state | `run_campaign` loop-exit gate (S3.1) + `CampaignResult` | `engine/mc_v18.py:273 run_campaign` |
| `world.winner` write — fallback path | world-state | `CampaignResult` | `engine/mc_v18.py:286 run_campaign` |
| `CampaignResult.winner` | struct field | `run_batch` win tally | `engine/mc_v18.py:317-319 run_batch` |
| `BatchResult.win_share` / `.all_winners` | struct field | test suite / tools consumers | `engine/tests/test_mc_v18_regression.py:97-98 test_mc_v18_batch_matches_golden` |
| `world.winner` (serialized) | field (dict) | `CampaignResult.final_state` via `serialize_world` | `engine/autoload/game_state.py:273 serialize_world` |

## 5. State touched

| Field | R/W | Owning module | Anchor |
|---|---|---|---|
| `world.winner` | RW | `engine/autoload/game_state.py` (`World`) | `engine/autoload/game_state.py:170 World` |
| `victory._qualifying_streak` | RW | `engine/autoload/victory.py` | `engine/autoload/victory.py:44 _qualifying_streak` |
| `world.clocks['Turmoil']` | R (never written anywhere — §7) | `engine/autoload/game_state.py` (`World.clocks`) | `engine/autoload/game_state.py:244 create_world` |
| `world.territories[*].accord` | R | `engine/autoload/game_state.py` (`Territory`) | `engine/autoload/game_state.py:145 Territory` |
| `world.territories[*].owner` | R | `engine/autoload/game_state.py` (`Territory`) | `engine/autoload/game_state.py:144 Territory` |
| `world.factions` | R | `engine/autoload/game_state.py` (`World`) | `engine/autoload/game_state.py:165 World` |
| `world.factions[*].parliamentary` | R | `engine/autoload/game_state.py` (`Faction`) | `engine/autoload/game_state.py:97 Faction` |
| `world.factions[*].L` | R | `engine/autoload/game_state.py` (`Faction`) | `engine/autoload/game_state.py:98 Faction` |
| `world.factions[*].territories` | R | `engine/autoload/game_state.py` (`Faction`) | `engine/autoload/game_state.py:109 Faction` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| up | `engine/mc_v18.py` (campaign orchestrator) | direct function call into `victory.check_all_factions` once per season | `engine/mc_v18.py:270 run_campaign` |
| down | `engine/autoload/game_state.py` (root state primitive) | reads `World`/`Faction`/`Territory` dataclasses + `ALL_PLAYABLE_15` | `engine/autoload/victory.py:57 check_peninsular_sovereignty` |
| down | `engine/autoload/game_state.py` | fallback path (S5) reads the same registry directly, bypassing `victory.py` entirely | `engine/mc_v18.py:282 run_campaign` |
| out | test suite (`engine/tests/`, `tests/valoria/_campaign.py`) | consumes `CampaignResult` / `BatchResult` as the golden/regression oracle | `engine/tests/test_mc_v18_regression.py:97-98 test_mc_v18_batch_matches_golden` |

## 7. Traced gaps

| Gap | Evidence anchor |
|---|---|
| `mc_v18.DEFAULT_PARAMS['VICTORY_THRESHOLD']` (a dict entry, value 11) is declared but never read anywhere — the live GD-1 gate is `victory.py`'s own module constant `VICTORY_THRESHOLD` (value 15), a different owner with no wiring between them. Repo-wide grep for `effective_params['VICTORY_THRESHOLD']` / `effective_params.get('VICTORY_THRESHOLD')` returns zero matches. | `engine/mc_v18.py:42-54 DEFAULT_PARAMS` (declaration + dead-param comment); `engine/autoload/victory.py:27 VICTORY_THRESHOLD` (the real, differently-valued gate); pinned live by `engine/tests/test_f7_smoke_oracle.py:175-183 test_f7_victory_threshold_is_a_dead_param`, which asserts sweeping the dead param 11→999→1 moves no `win_share` outcome |
| `world.clocks['Turmoil']` (read as the Political-Stability gate `ps_ok`) is initialized once to `0.0` and never written anywhere else in the tree — repo-wide grep for any `clocks['Turmoil']`/`clocks["Turmoil"]` assignment or `.clocks['Turmoil'] =` finds only the initializer and the victory.py reader. `ps_ok` is therefore unconditionally `True` for the life of every campaign; the PS clause of the GD-1 gate is structurally a no-op. No test pins this as intentional. Tracked: ED-WR-0004 (open, RULED — wire Turmoil writes via peninsular_strain). | `engine/autoload/victory.py:73-74 check_peninsular_sovereignty` (the read); `engine/autoload/game_state.py:244 create_world` (the sole write, at world-gen); repo-wide grep for `clocks[` under `engine/` and `systems/` finds writers for `CI`/`MS`/`MASS_SEIZURE_USED` only, never `Turmoil` or `Strain` |
| `references/module_contracts.yaml` declares four world-state-era gates on the `victory` module (`g_ms0` MS=0→Post-Calamity Era, `g_ms5` sustained MS≤5→Second Calamity, `g_msrec` MS-recovery, `g_diss` all-factions-dissolved→Anarchy Era) — none appear in `engine/autoload/victory.py`, whose only exported checks implement GD-1 (peninsular sovereignty) alone. Repo-wide grep for the era-transition strings ("Post-Calamity", "Second Calamity", "Anarchy Era", "Phased Occupation") returns zero `.py` matches. | `references/module_contracts.yaml:832-852` (the four `gates:` entries) and its own `gap_notes` at `references/module_contracts.yaml:854` ("world-state era transitions ... are UNKEYED — no mechanical_event/state_transition type exists") |
| Three of `VictoryResult`'s five fields (`qualifies_this_season`, `consecutive_qualifying`, `reason`) are computed every season but never read by `run_campaign`, which inspects only `.won` / `.faction_id`. Repo-wide grep for `.qualifies_this_season` / `.consecutive_qualifying` / `.reason` on a `VictoryResult`-shaped object finds no reader outside `victory.py` itself. The remaining field, `.held`, is not dead: `check_all_factions` reads it as the sort tie-break key (§3 S4.10), which decides which faction wins a same-season multi-winner tie. | `engine/autoload/victory.py:96-100 check_peninsular_sovereignty` (dataclass construction, all fields populated); `engine/mc_v18.py:271-274 run_campaign` (the only caller of `check_all_factions`'s result — reads `.won` and `.faction_id` only); `engine/autoload/victory.py:109 check_all_factions` (the `.held` tie-break reader) |
| The fallback winner-by-territory-count path (S5) is inline procedural code in the orchestrator, not a callable inside `engine/autoload/victory.py` — every campaign whose winner is not set by the sustained GD-1 check has its winner decided entirely outside the `victory` module, by a formula weighting held-territory count, `Faction.L`, and `len(Faction.territories)`, undocumented in `references/module_contracts.yaml`'s `victory` entry, which lists only the GD-1 resolver and the four (unimplemented) era gates above. | `engine/mc_v18.py:276-286 run_campaign` (the fallback block itself, comment-marked "v17 L753-761"); `references/module_contracts.yaml:819-861` (the `victory` module contract, silent on this path); `engine/tests/test_parliamentary_transfer_bridge.py:117-119` (a test explicitly naming both `engine/autoload/victory.py` and `mc_v18.py`'s fallback scoring as the two things "victory scoring actually reads") |
| `systems/victory/` has no head row of its own in `CURRENT.md`'s subsystem table, and `references/canonical_sources.yaml`'s `victory` entry names only the design doc, no code pointer — both of this module's mechanics (`victory_check_service`, `peninsular_sovereignty`) sim into `engine/autoload/victory.py`, never into this folder. | `CURRENT.md:147-170` (head table, no Victory row); `references/canonical_sources.yaml:111-113 victory` |
| `references/module_contracts.yaml`'s `victory` contract declares a single aggregate `state:` row of reads: MS / IP / CI / Turmoil / Accord / Mandate / PV / PT. `engine/autoload/victory.py` reads only `Turmoil`, territory `accord`, `owner`, and faction fields — the other five declared reads are never performed by the traced code. | `references/module_contracts.yaml:829` (declared reads); `engine/autoload/victory.py:59-84 check_peninsular_sovereignty` (the actual reads) |
