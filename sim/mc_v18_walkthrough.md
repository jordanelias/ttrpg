# How `mc_v18` works — a descriptive walkthrough

*Descriptive explainer of the existing strategic simulator, not a design surface. Lane WR/IN.
Written 2026-07-16 by tracing the code (`sim/mc_v18.py` and the modules it composes). Where this
disagrees with `sim/README.md`/`CONVENTIONS.md`, trust the code — those docs predate much of the
wiring (CLAUDE.md §7). No canon claims here; this is a map of what the pipeline does today.*

---

## 0. What it is

`mc_v18.py` is the **strategic-scale Monte-Carlo campaign simulator** — the Python oracle the GDScript
port is meant to validate against. It is an **orchestrator only**; all real work lives in the
subpackages it composes. Two entry points:

- `run_campaign(seed, max_seasons, params) -> CampaignResult` — one campaign to completion.
- `run_batch(n, base_seed, params) -> BatchResult` — N campaigns, aggregated win-share.

Default params: `CAMPAIGN_SEASONS = 50`, `VICTORY_THRESHOLD = 11`, `ECHO_TRANSPORT` on (env/params).

## 1. World state (`autoload/game_state.py`)

`create_world(seed)` builds a fixed starting board:

- **4 factions** (Crown, Church, Hafenmark, Varfell). Each is **5 continuous scalars 0.5–7.0**:
  `L` Legitimacy(==Mandate), `Sta` Stability, `W` Wealth, `I` Influence, `Mil` Military — plus
  `territories`, `parliamentary`, `standing`, and a few seasonal flags. `Faction.adjust(stat, granular)`
  divides by a per-stat `MULT` and clamps, which is where the "±2/season feel" comes from.
- **15 playable territories** T1–T14, T17 (+ neutral T15), each `owner/accord/pt/garrison/prosperity/
  fort_level/templar`.
- **5 world clocks**: `CI` (30), `MS` (60), `PI` (0), `Strain` (0), `Turmoil` (0).
- **~14 registries** (practitioners, insurgencies, npcs, convictions, beliefs, knots, treaties, …)
  that exist on the `World` but are **largely dormant** in the strategic loop — the personal-scale
  modules that fill them mostly never fire (see §4a).

> ⚠️ **Pre-LPS-1 scalar model** (ED-FA-0004, PORT-BLOCKING). `L` *is* Mandate; there is **no**
> per-settlement L/PS, **no** Treasury, **no** `da.*` Keys, and `run_accounting` has no
> Mandate-aggregation step. The ratified LPS-1 model is unimplemented. Do not port this schema as
> canon-conformant.

## 2. The season loop (`peninsular/season.py` + `mc_v18._faction_actions_callback`)

`run_season` composes three canonical steps; `mc_v18` injects step 2 as a callback. Full per-season
order:

1. **`advance_season`** — season counter, arc-boundary detection, per-season/per-arc flag resets.
2. **Faction actions** — for each parliamentary faction *that still holds territory*,
   `faction_take_action` (§3).
3. **Scene phase** — `scene_dispatch.run_scene_phase` (§4a).
4. **Parliamentary vote** — `parliamentary_bridge.run_parliamentary_scene` (§4b).
5. **Echo boundary** — `scheduler.accounting_boundary()` + `next_tick()`: deferred Domain-Echo
   stat-writes land, per-tick emission counter resets.
6. **`run_accounting`** — clocks + background pipelines (§5).
7. **Victory check** — GD-1 (§6); `break` on a winner.

## 3. Faction action selection (`provincial/faction_action.py`)

One action per faction per season. **State-conditioned mix** (ED-FA-0012): base weights
**unique 0.30 / conquest 0.35 / muster 0.20 / govern 0.15**, each scaled by RNG-free state signals
(conquest ← target-exists + mil-advantage; govern ← undergoverned share; muster ← proximate threat),
renormalized to a probability vector; then a **single `rng.random()` draw** picks the bucket. GD-2
mandatory threat-response is checked first. Resolution per bucket:

- **Conquest** → `resolve_mass_battle` → on attacker win: territory transfers, **loser `L −0.5`**,
  **Terms vs Storm** fork on the *degree* (Success = Terms, Accord −10, Confirm-Privileges L-seed 3;
  Overwhelming = Storm, Accord −25 — real, ED-FA-0013), `garrison=True`, `battle_count += 1`.
  **See §3a — this is the load-bearing caveat.**
- **Muster** → fiscal-military purchase (ED-FA-0009): `W −1` up front *always*; `pool = Mil +
  floor(W/2)`; d6≥4 vs Ob 1; `Mil +3` (Success) / `+5` (Overwhelming). No extra fail penalty.
- **Govern** → `pool = I` vs Ob 2; Accord `+10/+15` on success; `Sta −5` on failure.
- **Faction-unique** → Crown: Crown Initiative (`royal_progress` / `great_work` / `coronation_renewal`,
  chosen by a heuristic; Great Work is expensive and can crater `W`). Church: Excommunication → Council
  (1/arc) → Absolution priority chain. **Varfell & Hafenmark: no specific unique action** (Pass 2d/2e
  BLOCKED by a contamination audit). Any faction whose unique chain finds nothing falls through to a
  **Parliamentary Censure** (`parliamentary_action.propose_censure`, §5.4): target = highest-`L` rival;
  on a pass, target `Sta −1` and `L −1`; on a Total-Victory *failure* the §10 rider docks the
  *proposer*.

### 3a. What a "mass battle" actually is (`provincial/massbattle.py`)

`resolve_mass_battle(faction_a, faction_b, terrain, world)` runs the **real 1,905-line v22 engine**
(`run_battle`, up to 18 turns, morale cascade, rout, size-attrition, consuming `world.rng`) — so it is
**not** a bare `d6 ≥ 4`. **But** the strategic adapter `_faction_to_unit` builds *one* identical
`shape='Line'`, infantry, `tier=2`, single-subunit unit per side, with **fixed `command=4,
discipline=5, morale=5`**, **`terrain` ignored**, tactic-cards a BLOCKED stub — whose **only
faction-specific input is `power = int(round(faction.Mil))`**. It rounds, so `Mil 4.0` vs `4.99` →
`4` vs `4`: two identical forces deciding the province on battle-sim variance. `degree` is then derived
from remaining size %:

```
attacker_wins = (not a.routed) and (b.routed or a_size% > b_size%)
Overwhelming: win & a_size% ≥ 0.75 & b_size% ≤ 0.25 ;  Success: any other win
Partial: not routed & a_size% ≥ 0.50 ;  Failure: otherwise
```

**Net: conquest outcomes are rounded-Military + RNG.** The tactical depth is real code receiving no
differentiating input. Flagged inline as `[GAP: faction→unit construction lacks canonical spec]`;
Phase 7 Steps 2–9 + tactic-cards deferred. This "rich engine, aggregate/degenerate input" shape is the
defining pattern of the whole simulator (§7).

## 4. The two scale-seams (`cross_scale/`)

Most faction-`L` movement in a campaign comes from here, **not** from battle.

**(a) `scene_dispatch` — the personal↔strategic bridge, ~1/8 wired.** Fires **only** the Stability-Crisis
trigger (`Sta ≤ 2` → Emergency Council contest) and derives the two "sides" from the *same faction's*
`round(L)` vs `round(7−Sta)` — because no personal actors exist at Monte-Carlo scale, and it refuses to
fabricate them ("CONTEXT-DERIVATION BRIDGE GAP"). `combat` and the other 7 §4.3.2 mandatory triggers
**defer** (flagged, not faked). Side-effect-free on strategic stats unless `ECHO_TRANSPORT` is on and a
scene sets an `echo` block. (Tracked: ED-SC-0006 done for the one trigger; ED-SC-0011/0013 hold the
zoom-in expansion + parity, FORK-C open.)

**(b) `parliamentary_bridge` — the §10 vote, every season.** Proposer = lowest-`Sta` faction,
establishment = highest-`L` faction; resolves through the ratified `parliamentary_vote`. The **loser
eats the Total-Victory Mandate penalty (`L −1`)** and the **winner gets a composed Domain Echo** (band
gates magnitude → `Overwhelming ±2 / Success ±1 / Committee = nothing`; genre picks the channel — as
wired it is always Memory→`L`, so the winner gains `L`). This is the biggest regular mover of `L`.

**(c) `echo_transport` — the Key substrate.** `emit_scene_echo` → `domain_echo` → one `scene.*_resolved`
Key with an **OF-7 deferred** faction stat-write that lands at the §5 accounting boundary. Default ON
(Jordan 2026-07-08). Off = byte-exact legacy path.

## 5. Accounting / clocks (`peninsular/accounting.py`)

Every season: **CI** seasonal calc (PP-412 5-step — the one clock that reliably climbs, ~+1–2/season);
**insurgency** triggers + promotion (GD-3); **NPC ecology** stance drift. Year-end only (`season %
SEASONS_PER_YEAR == 0`): **MS** baseline decay (PP-255, ~−1/yr). No faction-`L` mutation happens here —
accounting moves clocks, not Mandate.

## 6. Victory (`autoload/victory.py`)

GD-1 only: **peninsular sovereignty** = hold ≥ `VICTORY_THRESHOLD` (11) of 15 territories, sustained
2 seasons. Nothing else ends the game — faction actions/battles produce deltas, never victory triggers.
If no one qualifies by the horizon, `run_campaign` picks a fallback winner by a territory-count score
(`held×10 + L + len(territories)`). In short (≤4-season) runs, `winner` is almost always `None`.

## 7. Determinism & the through-line

**Determinism:** one `world.rng` seeded from `seed`, threaded through every roll → **byte-identical per
seed** (`run_batch` reproducible). The one wrinkle: the promoted contest kernel resolves off global
`random`, so the bridges reseed it from `world.rng` and restore state around each call.

**The through-line — "rich engine, starved input."** The strategic spine is fully wired and runs
end-to-end, but it is a thin aggregate layer that under-feeds its own sophisticated engines:

| Sophisticated engine that exists | What the strategic loop actually feeds it |
|---|---|
| 1,905-line mass-battle engine | one Line unit/side, `power=int(round(Mil))`, no terrain, no tactics |
| Promoted personal contest kernel | two "parties" = `round(L)` / `round(7−Sta)` of one faction |
| Key/echo substrate | deferred single-Key echoes, Memory→L channel only |
| Personal↔strategic zoom protocol | 1 of 8 triggers; the rest defer |
| LPS-1 Mandate/Treasury/per-settlement L | not implemented (scalar `L` stands in) |
| Faction-unique actions | Crown + Church only; Varfell/Hafenmark fall back to Censure |

**Known balance smell:** the pinned F7 seed-42 golden win-share is **Crown 12.5% / Varfell 87.5%**
(with two factions at 0). It is pinned as a regression golden and mentioned in CLAUDE.md §7, but is not
filed as an actionable balance item, and no CI job runs full `mc_v18` campaigns.

## 8. Where the gaps are tracked (as of 2026-07-16)

| Gap | Tracked? |
|---|---|
| Scale-seam context-derivation (1/8 wired) | **Yes** — ED-SC-0006 (done, one trigger) / ED-SC-0011 / ED-SC-0013 (FORK-C open) |
| `engine_clock` has no home doc | **Yes** — ED-1051 (standing T0 blocker; `module_contracts.yaml` `doc:null`) |
| LPS-1 Mandate/Treasury unimplemented | **Yes** — ED-FA-0004 (PORT-BLOCKING) |
| Domain-Echo composed keying / Projection channel | **Yes** — ED-SC-0002 (Projection residual noted inline) |
| Mass-battle `faction→unit` construction is Mil-only | **Inline only** — `massbattle.py` `[GAP]` + Phase 7 Steps 2–9; not in any ED ledger/handoff |
| Emergency-council / insurgency unreachable in ≤4-season horizon | **Not found filed** anywhere |
| Degenerate win-share as an actionable balance item | **Partial** — pinned as a golden + CLAUDE.md §7 prose; no work item |
