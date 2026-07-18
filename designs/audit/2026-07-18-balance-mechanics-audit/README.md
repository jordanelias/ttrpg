# Balance, Mechanics, States, Trackers, Clocks, Matrices & Vectors — Consolidated Adversarial Audit

## Status: FILED (adversarial audit) — 2026-07-18 · Lane: IN (cross-cutting) · no ED allocated · analysis-only, ratifies nothing

**What this is.** A single, exhaustive audit of every balance-relevant surface touched or flagged in the
last two days (PRs #150–#184) — the trackers, clocks, game-states, matrices, vectors, pool formulas,
thresholds, and the defect registers riding on them. It is the companion the `2026-07-18-two-day-review`
doc lacked: that doc classified *commits*; this one audits the *mechanics*.

**It is adversarial by construction.** Nothing here rests on a doc's self-asserted `## Status:` line or a
sim's `[CANONICAL]` docstring. Every load-bearing claim was verified by the cheapest independent method
that could *refute* it — running the sim, hand-deriving the arithmetic, grepping the ledger for the cited
ID, counting to the line. Where I could only relay a doc's claim, it is marked **[RELAYED]**; where I
verified it, **[VERIFIED]**; where verification *contradicted* the received wisdom, **[CONTRADICTED]**.
The verification log is Appendix A.

**It ratifies nothing and files no ED.** Every ruling it references is already ledgered under its own ID.
This is a map with the traps drawn in, not a source.

---

# EXECUTIVE SUMMARY

## The one-paragraph read
The corpus talks about balance as if the engine were built. It is not. The live `mc_v18` campaign runs
**~15% of the designed game**, the nominal victory condition is a **dead parameter**, an NPC's Convictions
have **zero mechanical effect** on the contests they judge, and several of the "structured" data layers
and currency documents **misreport their own state** — including the ones designated as authority. The
highest-value work is **not tuning numbers**; it is **ratifying two foundations** (the temporal spine and
the character schema) and **wiring what is already built** but dead-in-campaign. Balance tuning on top of
an unwired skeleton measures the skeleton.

> **Correction pass (2026-07-18, post adversarial review).** An independent read-only reviewer re-ran
> every executable finding and confirmed H1–H3, H5–H7, H9 and the §3.5 region table (several *stronger*
> than first stated). It refuted one graded claim and flagged three overreaches, all in the currency
> section — corrected in place below and marked **↺ corrected**: **H8/C-b retracted** (CURRENT.md is
> *accurate* — 311 files still carry live `certainty`, so the corpus sweep is genuinely STAGED, not stale);
> **H4 narrowed** (adapter-level n=100–500 runs *do* exist in `audit_registry.jsonl`); rename stats fixed
> to the git-verified `96 files, +513/−475`; the §1 count-table relabeled (34 = modules + adapters); and the
> headline count reconciled to **nine**.

## The nine headline findings

| # | Finding | Grade | Evidence |
|---|---|---|---|
| **H1** | **`VICTORY_THRESHOLD` is a dead parameter.** Setting it to 1, 11, or 999 yields *identical* win-shares — **structurally, at any n**: `victory.py:27,70,88` read the module-level global; `run_batch(params=…)` writes `world.params`, which no victory consumer ever reads. The campaign resolves winners by something other than its nominal gate. | **[VERIFIED]** — test passes + `victory.py` grep | §5 |
| **H2** | **NPC Convictions never reach a contest verdict.** The judging armature is arithmetically single-axis (a balanced judge ties all four styles at **0.7250**), and the substrate's Conviction axes `(hierarchical, sacred, instrumental, traditional)` are a *different space* from the contest's `(evidence, consequence, authority, insinuation)`, with no bridge. | **[VERIFIED]** — ran the live armature | §4 |
| **H3** | **The "~87% win-share degeneracy" is stale lore.** The real n=8/seed-42 batch is `{Crown 37.5, Church 12.5, Hafenmark 12.5, Varfell 37.5}` — no degeneracy. CLAUDE.md §7 still asserts it as fact; five docs cite it; the two-day-review doc repeated it. | **[CONTRADICTED]** — ran `mc_v18` | §5 |
| **H4 ↺** | **`mc_v18` campaign win-share is uncharacterized at scale.** No n≥100 *campaign win-share* run is pinned in any ledger; the only such datapoint is one I generated ad-hoc (Varfell 55% skew). *Corrected:* adapter-level n=100–500 runs **do** exist in `audit_registry.jsonl` (2026-07-12; two flag `DEGENERATE_DISTRIBUTION`) — so the earlier "nothing anywhere" was too broad. | **[VERIFIED]** (narrowed) | §5 |
| **H5** | **Mass-battle progress is negative-signed and churning.** The historical gauge is frozen at **7/20**; the Lanchester melee exponent is **p≈3.2** (worse than the p≈2.5 still circulating), against a required **≤1.4**. DG-6..16 all open. | **[RELAYED]** + ledger-cross-checked | §5 |
| **H6** | **Wired-but-vacuous registries.** `generate_npc`/`form_knot`/`register_settlement` have zero callers, so `world.npcs/knots/settlements` stay empty forever and every downstream consumer silently no-ops. | **[RELAYED]** — audit D6 | §3 |
| **H7** | **Fabricated-adjacent citations pass CI green.** `clock_registry_v30`'s `ED-793/794/795/796` tags resolve to unrelated already-closed items; the checker only verifies an ID *exists*, not that it's relevant. | **[VERIFIED]** — grepped the ledger | §2, §8 |
| **H8 ↺** | **CLAUDE.md §7 is stale about a balance fact** (the debunked "~87%"), and `conviction_taxonomy_v30.md` states its own status four times with two values. *Corrected:* the third sub-claim is **retracted** — CURRENT.md's "Certainty→Truth rename STAGED" is **accurate**, not stale (blame: written in the rename commit; **311 files still carry live `certainty`**, so the corpus sweep genuinely did not execute). | **[VERIFIED]** (C-b retracted) | §8 |
| **H9** | **The Key substrate is write-only outside one slice.** Keys are produced but the universal apply path (`articulation`) is a stub — all 3 entry points `raise`; flagship types (`state.scar_acquired`…) emit nowhere. Only `echo_transport` applies (to 7 `MULTS` faction stats). | **[VERIFIED]** — grep | §3.5 |

## The balance-readiness verdict, by domain

| Domain | Readiness | One-line state |
|---|---|---|
| Personal combat | 🟡 **Measurable, not settled** | 51-weapon harness runs; residual channel-leverage imbalance is a Jordan design call; key-log parity red |
| Knot Pool (fieldwork) | 🟢 **Settled** | `(Spirit×2)+History+3, min 5` ratified, all surfaces agree, regression-pinned |
| Social contest | 🔴 **Structurally broken** | Convictions don't reach verdicts (H2); argue-pool formula fork open |
| Mass battle | 🔴 **Churning, negative-signed** | Gauge 7/20, Lanchester p≈3.2, 11 open DGs, gated on unruled DG-6 |
| Strategic campaign | 🔴 **Unwired** | Dead victory param (H1), Mandate never restores, vacuous registries, ~15% wired |
| Trackers | 🟡 **Catalogued, partly stale** | Full registry exists but is an un-migrated doc-only manifest with stale rows + bad citations |
| Clocks | 🔴 **Foundation unratified** | `engine_clock` is `doc:null` (ED-1051, the sole T0 blocker); a stand-in ticks today |
| Character/state schema | 🔴 **No Character class exists** | 9-vs-10 attribute roster fork open; `World` holds no actor |

## The decision ledger at a glance (detail in §7)

| Rank | Decision | Cost | Why it's #n |
|---|---|---|---|
| 1 | **ED-1051** — ratify `engine_clock` (flip `doc:null` → `propagation_spec_v1.md`) | ~zero (authoring done) | Sole T0 blocker on M1; gates the entire accounting/season cadence + Godot Gate-0 |
| 2 | **D8** — rule the 9-vs-10 attribute roster | one ruling | Unblocks the missing `Character` dataclass and every personal-scale port |
| 3 | **D3** — sign off the Mandate-restore fix + rebaseline goldens | ruling (flips ~72% of winners) | Correct strategic balance; precondition for any real n≥100 characterization |
| 4 | **Character-decision docket** D2/D4 + C-1..C-9 | rulings | Convictions actually reaching contests (H2) |
| 5 | **DG-6** — mass-battle resolution architecture | deepest call | Gates DG-6..16; but MB is the churn-risk lane — re-run the gauge first |
| 6 | **ED-SC-0004** — argue-pool formula pick | one ruling | Social-contest low-pool regime |

Standing deferral (not a pending ask): **OPT-AV-1** attribute-roster unification — you deliberately left it open.

---

# §1 · The balance-readiness thesis: "rich engine, starved input"

The MC-wiring audit (ED-IN-0074) established, and the balance data confirms, that the live campaign loop
exercises only a thin slice of the designed systems. This is the single most important framing for every
number below, because **a balance figure measured on an unwired path is measuring the stub, not the design.**

**What actually runs each season** (`engine/mc_v18.py` → `run_campaign`):
`create_world` → per-season `advance_season` (emits no Key) → `_faction_actions_callback` (four
`faction_take_action` calls → conquest → `resolve_mass_battle`; a 1-of-8 scene trigger; a parliamentary
scene) → `run_accounting` → `check_all_factions` → GD-1 victory check.

**Build-state coverage of all 34 conversion units** (the 27 modules **+ 7 adapters**; module-only counts are
`live 2 · gated 1 · deferred 10 · design 9 · stub 3 · unwired 2`) (`references/wiring_manifest.yaml`, validated by
`tools/wiring_map_check.py`):

| build-state | count | meaning |
|---|---|---|
| `live` | **2** | `mass_battle`, `victory` — fire every campaign |
| `gated` | 5 | fire only conditionally (`social_contest` via emergency_council; the Key adapters) |
| `deferred` | 11 | built, no live caller |
| `design` | 9 | doc-only / canon-must-be-authored-first |
| `stub` | 4 | skeleton only |
| `unwired` | 3 | incl. `personal_combat` — the *one* GDScript-ported unit, but its branch is dead code so parity is unvalidated |

**Four foundation gaps block whole tiers** (`wiring_manifest.yaml → foundation_gaps`):
- **`character_layer`** — no `Character`/`Actor` dataclass exists; resolvers duck-type `getattr(actor,'strength',3)`.
- **`godot_spine`** — `BaseEngine`/`EngineModule`/`KeyBus`/`Resolver`/`GameState` are referenced but defined nowhere.
- **`save_replay_premise`** — status **`violated`**: the strategic loop mutates `World` directly with no Key
  trace, so "save = initial conditions + Key log" does not hold.
- **Input starvation** — battles are fed *one Mil-rounded unit per side*; the contest kernel derives two
  "parties" from one faction's own stats; 1 of 8 scale-seam triggers fires.

**Consequence for this audit:** the residual campaign asymmetry (Varfell skew, §5) is dominated by *what
isn't wired* — faction-unique actions exist only for Crown+Church; Varfell/Hafenmark fall back to Censure —
not by a tunable balance constant. **You cannot balance your way out of a wiring gap.**

---

# §2 · Trackers & Clocks — the master registry

The canonical roster is `designs/provincial/clock_registry_v30.md` (self-declared "single source of truth
for all clocks, tracks, and counters," `## Status: CANONICAL`). It is a **doc-only manifest**
(`module_contracts.yaml:797` — `resolver: manifest # owns no state, resolves nothing`); every listed track
is owned by its source system. It is **un-migrated** (CLAUDE.md marks it routed to the IN lane, not yet
moved) and carries verified rot (see the ⚠ rows and §8).

### 2.1 Shared clocks (all modes)
| Clock | Range | Start | Dir | Note |
|---|---|---|---|---|
| Mending Stability (MS) | 0–100 | 60 | ↓ | 60-vs-72 resolved to 60; lore trajectory reconciliation pending Jordan |
| Church Influence (CI) | 0–100 | 28 | ↑ | |
| Institutional Pressure (IP) | 0–100 | 20 | ↑ | ⚠ start-value tag cites **ED-793** (unrelated closed item — §8); **D2**: not a `world.clocks` key at all until the #180 fix |
| Turmoil | 0–10 | 0 | ↑ bad | replaces repealed Parliament Integrity (PP-403). ⚠ **D1**: write-dead — read by the stability gate, written by nothing |

### 2.2 Faction-specific tracks (BG/Hybrid)
| Track | Owner | Range | Start | Note |
|---|---|---|---|---|
| Torben Loyalty | Crown→Löwenritter | 0–7 | 7 | PP-599 corrected start 3→7 (ED-IN-0029) |
| Elske Loyalty | Crown | 0–7 | 4 | |
| Löwenritter Autonomy | Crown-Löwenritter | Loyal/Restless/Autonomous/Split | Loyal | 4-state |
| Popular Will (PW) | Hybrid | 0–5 | 0 | ⚠ STRUCK-recommended 3mo ago; cites **ED-795** (unrelated) |
| Warden Cooperation (WC) | Shared | 0–3 | 0 | source doc `victory_architecture_v1.md` no longer exists |
| Warden Recognition (WR) | Varfell | 0–4 | 0 | same dead source |
| Intel Advancement Counter | Varfell | 0–3 (→Intel+1 at 4) | 0 | ⚠ STRUCK-recommended; cites **ED-794** (unrelated) |

### 2.3 Faction stats (1–7, floor 1; Stability floor 0 = eliminated)
Mandate 0–7 (0 = subjugated) · Influence 1–7 · Wealth 1–7 · Military 1–7 · Stability 0–7 · Intelligence 1–7
(⚠ STRUCK-recommended, cites **ED-796**) · Reputation 0–5 · Standing 0–5.
⚠ The live `Faction` dataclass (`engine/autoload/game_state.py`) implements the **superseded pre-LPS-1**
stat model (`L/Sta/W/I/Mil`) — no Mandate/PS/Treasury/`da.*`; the ratified LPS-1 model
(`Mandate = 7T/(T+6)`) is unimplemented. `fac.intel` was ratified 2026-07-08 but only added to the class by
audit fix **D4** (still "unread/unwritten by live code").

### 2.4 Per-territory tracks
Accord 0–3 · **Piety Track (PT)** 0–5 (oscillating; ⚠ dead source `victory_architecture_v1.md`) · Fort Level
0–4 · Prosperity 1–7 · Guild Favour 0–7 · Church Attention Pool 0–10 (Inquisitor at AP≥3, second at AP≥6).

### 2.5 Personal tracks & derived scores (`engine/params/core.md`, `derived_stats_v30.md §14.1`)
| Track | Range | Formula / start | Note |
|---|---|---|---|
| Coherence | 0–10 | start 10, countdown | rendering legibility |
| **Truth** | 0–5 | by background | renamed from Certainty + character piety (ED-IN-0075). **Legibility trap:** Truth 5 = orthodoxy canon holds *sincerely wrong*; Truth 0 = the true belief |
| Thread Sensitivity (TS) | 0–100 | 0 non-practitioner | orthogonal to Coherence (ED-301) |
| Composure | 3–21 | Charisma × 3 | social buffer |
| Concentration | 5–35 | (3×Focus)+(2×Spirit) | ED-902; contest+combat |
| Health | 14–48 | (End+6)×(MW+1), MW≤3 | wounds add fractional Ob, **never −1D** (ED-PC-0005) |
| Stamina | 5–35 | (3×End)+(2×Spirit) | action economy |
| Wounds | 0–max | max=floor(End/2)+1 | |
| Momentum | 0–4 | start 0 | auto-successes *add to* roll (PP-243); a 1 cancels one |
| Knot Count | 0–floor(Bonds/2)+1 | 0, needs Bonds≥5 | count cap, not a pool |

### 2.6 Contest / NPC / fieldwork / cooldown / player / settlement tracks
Persuasion Track 0–10 (A≥7 / B≤3 / compromise 4–6; Total ≥9/≤1) · Obligation clocks (Formal 2 / Grand
4-or-condition / Royal Audience 2 / Church Tribunal until-revoked; cap ~3) · Cardinal Influence 0–5 ×3 ·
Ministry AP-Tokens (4) · Exposure 0–10+ · Cover 2–14 (Cognition+History) · Evidence Track 0–{3,5,8} ·
Disposition −5..+5 · Thread Debt · Casus Belli · Resources 0–5 · Settlement Prosperity/Defense/Order 0–5 each
· Local Actor Disposition −5..+5 · Local Economy 0–250 (Prosperity×50) · Garrison Strength 0–250
(Defense×20+Fort×30) · Public Order 0–100 (Order×20).

### 2.7 Clocks proper
| Clock | State | Note |
|---|---|---|
| **`engine_clock`** | `doc:null`, `no-oracle`, **T0 blocker ED-1051** | home doc `propagation_spec_v1.md` is CANONICAL and ready; only Jordan's flip is outstanding. The *entire* accounting spine (`module_contracts.yaml:878`) is written as if it already drives ticks |
| `scene_timer` | `doc:null` | a wall-clock **telemetry sidecar** outside the Key log — not a gameplay clock |
| stand-in (live today) | working, un-ratified | `season_manager.advance_season` does `world.season += 1`, `SEASONS_PER_ARC=4`; `keys.py::TickScheduler` is the "engine_clock-shaped seam" but disclaims owning the counter |
| Obligation / Thread Debt / Casus Belli | design-level | ranges above; not mechanically closed |

---

# §3 · States & engine wiring

### 3.1 The state model
- **The `World` dataclass *is* the game state** (no DB). Holds `factions`, `territories`, `clocks`
  (flat `dict[str,float]`), `season`, `arc`, `winner`, plus Tier-0/1/2 registries added 2026-05-19:
  `practitioners, insurgencies, uncontrolled_streaks, npcs, treaties, convictions, beliefs, knots,
  territory_infrastructure, npc_drift_state`.
- **There is no `Character`/`Actor` dataclass anywhere.** `World` holds only `Faction` and `Territory`;
  resolvers duck-type actor fields. This is **defect D8**, blocked behind the roster fork (§4.4).
- **The Key substrate** (`engine/substrate/keys.py`, `[RATIFIED — Key & Echo armature v1, ED-IN-0018]`):
  `AXES = (hierarchical, sacred, instrumental, traditional)`, `SCALES = (personal, settlement, territory,
  peninsula)`, 44-type roster. **Steps 3–4 (observer/armature application) are NOT implemented, blocked on
  ORD-3** — so Keys are validated and serialized but never applied to any character vector.

### 3.2 Wired vs dead-in-campaign
- **Live producers/consumers:** `parliamentary_bridge` (the *only* live Key producer, 13–65 Keys/campaign);
  `echo_transport` (the *only* live Key consumer, writes `Faction.L/I`); `mass_battle` + `victory`.
- **The in-13 hub** `faction_state` consumes 20 of 47 Key edges — and its resolver is `[ASSUMPTION]`-grade.
- **`[ASSUMPTION]`-grade resolvers: 11/27** (verified by enumeration; CLAUDE.md's "11/27" is correct here).
- **`doc:null` modules: 9/27** (verified to line — CLAUDE.md's "10/27" is **stale**; the 10th `grep` hit is a
  comment, and `faction_politics`/`miraculous_event` were fixed to real doc paths). The nine:
  `npc_memory, scene_slate, game_director, scene_timer, audit, domain_actions, settlement_economy,
  engine_clock, scenario_authoring`.

### 3.3 The held-defect register (ED-IN-0074 D1–D8) — the wiring bombs
| ID | Defect | Status | Blast radius |
|---|---|---|---|
| **D1** | **Turmoil write-dead** — stability gate (`victory.py`, PS≤6) reads Turmoil; nothing writes it → gate trivially always true | held, needs_jordan | balance shift on wiring §4.1/§4.2 |
| **D3** | **Mandate never restores** — Total-Victory loser penalty documented reversible; `season_manager` never restores it → permanent drain | held, needs_jordan | fix **flips ~72% of winners (29/40 seeds)**, breaks 7 goldens |
| **D6** | **Registries wired-but-vacuous** — `generate_npc`/`form_knot`/`register_settlement` have zero callers | held, needs_jordan | NPCs/knots/settlements never populate; consumers silently no-op |
| **D8** | **No Character/Actor dataclass** + 9-vs-10 roster fork | held, needs_jordan | every personal-scale port |
| D2/D5/D7 | IP-not-a-clock-key / mislabeled MB engine / silent `try/except: pass` action errors | **fixed** (#180) | — |
| D4 | `fac.intel` field missing from `Faction` | **fixed** (#182) | added at floor 0, still unread |

---

# §3.5 · Complete region coverage — all 27 modules + 7 adapters + 3 gaps

Cross-referenced against `references/wiring_manifest.yaml` (`as_of 2026-07-18`) so **no region is missed**.
The earlier sections are domain-organized; this table is the exhaustive register. `cov` = whether an
earlier section already addressed it (**✓** covered · **◐** partial · **✚** surfaced only here).
`b` = build-state, `g` = godot-state.

### Modules (27)
| Module | scale | b / g | Balance / mechanics state | cov |
|---|---|---|---|---|
| personal_combat | personal | unwired / gd-ported | golden-path port; 51-weapon harness lives here — but loop never routes here, so **end-to-end combat parity is unvalidated** | ✓ |
| mass_battle | scene | live / oracle | fires 30–45/campaign; gauge 7/20, Lanchester p≈3.2; a **richer unwired engine** at `tests/sim/mass_battle` mislabeled "frozen" | ✓ |
| social_contest | scene | gated / oracle | Agon kernel = **1 of 4 games**; armature degenerate (H2); reached only via `emergency_council` | ✓ |
| victory | provincial | live / oracle | GD-1; **`VICTORY_THRESHOLD` dead** (H1) | ✓ |
| **threadwork** | personal | unwired / oracle | **13 Thread operations built, ZERO live callers; rendering is a stub** — the entire magic system is dead-in-campaign | ✚ |
| territorial_piety | territory | deferred / oracle | CI generation live via `ci_track`, but **CANONICAL doc with ZERO Key integration** | ◐ |
| clock_registry | provincial | design / oracle | pure catalog; stale rows + fabricated-adjacent citations (H7) | ✓ |
| faction_state | provincial | deferred / oracle | **the in-13 hub** (20/47 Key edges); action code live, resolver `[ASSUMPTION]` | ✓ |
| **faction_politics** | provincial | deferred / oracle | **succession / coalition math exists but is unwired** — no live campaign path exercises it | ✚ |
| piety_track | personal | deferred / oracle | `conviction.py` Scar accumulation real; **reached only via the unwired knot chain** | ◐ |
| **settlement_layer** | territory | design / oracle | territory substrate built but unwired; **Mandate aggregation `7T/(T+6)` unbuilt** | ◐ |
| engine_clock | provincial | design / **no-oracle** | `doc:null` temporal spine — **sole T0 blocker (ED-1051)** | ✓ |
| **npc_behavior** | personal | design / **no-oracle** | Procedures B/C/D/E; `npc_ai.py` is a **28-line stub**; **the in-12 hub with NO oracle** — the NPC decision engine is design-only | ✚ |
| **npc_memory** | personal | design / **no-oracle** | `doc:null`; schema lives only in a doc-12 bridge — NPCs have no persistent memory substrate | ✚ |
| **fieldwork_knots** | personal | stub / **no-oracle** | fieldwork/investigation resolvers **raise**; knots built but **the scene runner is a stub** (the Knot *Pool formula* §5.1 is settled; the *runner* is not) | ◐ |
| domain_actions | provincial | design / **no-oracle** | `da.*` 5-tag taxonomy; **`doc:null`, zero code** (the M1 "author the home" item, ED-FA-0002) | ✓ |
| **ci_political** | provincial | deferred / **no-oracle** | CANONICAL doc, **ZERO Key integration; the Church-influence card system is unbuilt** | ✚ |
| peninsular_strain | peninsula | deferred / **no-oracle** | owns **Turmoil + IP** (D1/D2); `env.*` emitters + **occupation ladder unbuilt** | ◐ |
| **scene_slate** | scene | deferred / **no-oracle** | `doc:null`; built = a 59-line queue, **the canonical §4 scene generator is unbuilt** | ✚ |
| **game_director** | scene | deferred / **no-oracle** | `doc:null`; **scene lifecycle + zoom stack** — the scene-orchestration spine, design-only | ✚ |
| scene_timer | scene | deferred / **no-oracle** | `doc:null` observability **telemetry sidecar** — not a gameplay clock | ✓ |
| **audit** | scene | deferred / **no-oracle** | `doc:null` QA telemetry sink | ✚ |
| **miraculous_event** | personal | stub / **no-oracle** | trigger **raises**; the fires-near-T15 emitter is `[ASSUMPTION]` and unbuilt | ✚ |
| **scenario_authoring** | peninsula | design / **no-oracle** | compile-time event injection; **execution unbuilt** | ✚ |
| **articulation_layer** | personal | stub / **no-oracle** | **the universal Key CONSUMER — 3× `raise`. No consume-side oracle exists anywhere** (see H9) | ✚ |
| settlement_economy | settlement | design / retire | phantom (in-3/out-0); folds into `settlement_layer` (ED-SE-0005) — **do not port** | ✓ |
| campaign_architecture | provincial | design / retire | reclassified: a consolidation doc, not a runtime module — **do not port** | ✓ |

### Adapters (7 — the KeyBus / cross-scale seam)
| Adapter | b / g | Mechanics state | cov |
|---|---|---|---|
| parliamentary_bridge | gated / oracle | **the ONLY live Key producer** (13–65 keys/campaign) | ✓ |
| echo_transport | gated / oracle | **the only live Key CONSUMER** (writes `Faction.L/I`) | ✓ |
| domain_echo | gated / oracle | `compute_domain_echo/accord/thread` | ◐ |
| zoom_in_out | gated / oracle | zoom protocol §4 → Godot GameDirector zoom stack | ✚ |
| scene_dispatch | deferred / oracle | down-scale seam; **only 1 of 8 triggers fires** | ◐ |
| **handoff_rules** | unwired / oracle | **8 §3 rules built, ZERO callers; §3.7 Mass→Personal Duel never fires** — a designed cross-scale mechanic is dead | ✚ |
| **articulation** | stub / **no-oracle** | the universal Key reader — **stub. The consume/handoff half of the substrate has NO oracle on either side** | ✚ |

### Foundation gaps (3)
`godot_spine` (undefined `BaseEngine/EngineModule/KeyBus/Resolver/GameState`), `character_layer` (no
`Character`/`Actor` class; roster fork), `save_replay_premise` (**violated** — strategic loop mutates
`World` with no Key trace). All covered in §1/§3.

### What the region sweep adds — H9, the finding the domain view buried

**H9 · The Key consume/apply half of the substrate is unbuilt on both sides. [VERIFIED — stub grep]**
Keys are *produced* (`parliamentary_bridge`, live) and one narrow *consumer* exists (`echo_transport`,
writes `Faction.L/I`). But the **universal** apply path — `articulation_layer` (module) and `articulation`
(adapter) — is a stub with `no-oracle` on *both* sides. So every Key type outside the echo slice is
**produced-but-never-applied**: it is validated, serialized, logged, and then nothing mutates state from it.
This is the substrate-level root cause of the character-decision audit's Q1/Q2/Q3 (`articulation.py`'s
three entry points all `raise NotImplementedError`; Keys never mutate character vectors, blocked on ORD-3;
flagship types `state.scar_acquired` / `state.belief_revised` / `meta.knot_ruptured` never emitted).
**It ranks with H1/H2:** the Key substrate — the whole ED-IN-0018 armature the strategy leans on — is a
write-only log for everything but one faction-stat slice. Balance measured through Keys today measures the
producer, because the consumer isn't there.

**Regions with balance/mechanics weight the domain view under-served** (now covered above): the **magic
system** (`threadwork` — 13 ops, zero callers), the **NPC decision engine** (`npc_behavior`, the in-12 hub,
no oracle), **NPC memory**, the **Church strategic layer** (`territorial_piety` + `ci_political`, CANONICAL
docs with zero Key integration), **faction succession/coalition** (`faction_politics`), the **occupation
ladder** (`peninsular_strain`), the **settlement Mandate aggregation**, the **scene-orchestration spine**
(`scene_slate` + `game_director`), and the **Mass→Personal duel handoff** (`handoff_rules §3.7`). None is a
tuning problem; every one is a *build/wire* problem — reinforcing §1's thesis across the full region set,
not just the sampled domains.

---

# §4 · Matrices & Vectors

### 4.1 The Conviction system (the intended spine)
- **13 Convictions** (`conviction_taxonomy_v30.md`, PP-684): Faith, Authority, Order, Scholastic, Utility,
  Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor — vector-valued per-actor weights,
  1–3 primary + cultural distribution, plus an orthogonal Self-Other orientation scalar `[-1,+1]` (drift
  `κ=0.03`; attribution `attributed = raw × (1 − 0.5·max(0,orient))`). ⚠ The file asserts its **own status
  four times, two different values** (CANONICAL/PROVISIONAL/CANONICAL/PROVISIONAL — §8).
- **CONVICTION_AXIS_MATRIX** projects the 13 Convictions → the 4 substrate armature axes
  `(hierarchical, sacred, instrumental, traditional)`.

### 4.2 The armature schism — H2, verified at code level
This is the audit's most consequential mechanical finding, and I verified it by **running the live code**
(`systems/social_contest/sim/contest/armature.py` — the audit cited the pre-P4-move path
`sim/personal/contest/armature.py`, which no longer exists).

**Two disjoint 4-axis spaces both named `armature_position`:**
| Space | Axes | Used by |
|---|---|---|
| Substrate | `hierarchical, sacred, instrumental, traditional` | `keys.py`, the Conviction projection |
| Contest judge | `evidence, consequence, authority, insinuation` | the contest adjudicator |

**No bridge exists between them.** An NPC's Convictions project into the substrate space; the contest judge
reads the *other* space. Net: **Convictions have zero mechanical effect on contest verdicts** (audit L2).

**And the contest armature is arithmetically single-axis** (audit L1). `_row(primary)` builds
`{primary: 1.0, off-axis: 0.15}`, so `alignment(style, judge) = 0.85·judge[primary] + 0.15·Σjudge`. The
off-axis term is a **constant that cancels across styles.** Verified output:

```
Balanced judge [.5,.5,.5,.5]:   precedent 0.7250  vision 0.7250  suppression 0.7250  insinuation 0.7250   (all tied)
Evidence-committed [1,0,0,0]:   precedent 1.0000  vision 0.1500  suppression 0.1500  insinuation 0.1500   (differentiates)
```

The "continuous 4×4 dot-product" differentiates styles *only* for a fully axis-committed judge; any balanced
or lightly-varied Conviction vector collapses to a tie. The code's own comment brags this is "the ★★★★★ fix…
adjudicator-conviction-sensitive" — that boast fixed a **different** bug (sub-die alignments rounding away),
not this degeneracy. The proposed remedies (`STYLE_AXIS` genre-overlap with `OFFAXIS_ADJ=0.5`;
`CONV_TO_RESONANCE` 13×4 bridge) are **designed, not built** (docket C-1/C-2, unruled).

### 4.3 Combat matrices (`combat_engine_v1/workbench/balance.py`, `combat_balancing_methodology.md`)
`weapon_matchup_table` (each weapon vs arming baseline, Wilson-CI'd) · `attribute_parity_table` (marginal
+1) · `tradition_field_table` (unconditional vs field; target flat) · `tradition_context_matrix` +
`weapon_armour_matrix` (contextual C1). Deliberately spiky matchup tables; only the *unconditional* means
must be flat (±2–3pp). Numbers in §5.

### 4.4 The vectors that don't yet exist as one thing
- **Attribute roster (9, IN FLUX)** — `descriptor_registry.yaml`: 3 body (Strength, Endurance, Agility) /
  3 mind (Focus, Acuity[←Cognition/Reasoning], Will[←Spirit]) / 3 social (Attunement, Charisma, Bonds).
  Aggregates `agg.body/mind/social` are **placeholders, not wired**. The competing 10-attribute schema in
  `core.md` is the *de-facto* live one the ported combat depends on. **This fork (D8) is unruled;
  OPT-AV-1 unification was deliberately skipped by Jordan.**

---

# §5 · Balance values & formulas — the number ledger

### 5.1 Resolution pools (the load-bearing formulas)
| Pool | Live formula | Status |
|---|---|---|
| **Combat Pool** | `max(5, Relevant History + 6)` — **Agility-independent** (ED-901/900/904) | 🟢 live; `core.md` + `module_contracts.yaml` agree. ⚠ `values_master.yaml` still carries the struck `(Agi×2)+History+3` — so CLAUDE.md §5's "three-way split" is itself stale: it's *one* stale index vs two agreeing heads |
| **Knot Pool** | `(Spirit×2) + History(Relevant) + 3`, min 5; Knot Max `floor(Bonds/2)+1` | 🟢 **settled** (ED-FI-0005), 3 surfaces agree, regression-pinned (ran it: 3/3) |
| **Argue-pool** | legacy `(Primary×2)+History−Wounds+fatigue`, floor 1 **vs** kernel `max(5, faculty×2+3)` | 🔴 **fork open** (ED-SC-0004, needs_jordan) — kernel silently dropped History/Wounds/fatigue and raised floor 1→5, erasing the low-pool regime |
| **Mass Combat Pool** | legacy `min(Size,Command)+Command` **vs** live `POOL_QUALITY_MODEL` (quality×numbers, Command decoupled) | 🟡 live is POOL_QUALITY_MODEL; index rows lag |
| **Fieldwork Pool** | `(Primary×2) + History` | matches Combat/Contest construction |
| Pool floor | `max(1, base − penalties)` = 1D everywhere | 🟢 canonical |

### 5.2 Thresholds & signatures
- **`ADEF_THRESHOLD`** (armour-defence) = `{none: 0.0, light: 0.30, medium: 0.45, heavy: 0.72}` — monotone,
  re-exported after the ED-1050 in-place-correction incident. **Key-log parity still RED** (RESIST /
  GAP_EXPOSURE / gap-game not yet re-exported to `weapon_resource.gd` / `strike_module.gd`).
- **`VICTORY_THRESHOLD`** — **DEAD (H1).** 1 vs 11 vs 999 → identical win-share.
- **Lanchester melee exponent** — required **≤1.4**; measured **p≈3.2** under correct `PER_CELL=1`
  (the p≈2.5 in circulation was measured under a wrong default). Root causes: E1 (a cell-count plumbing
  bug) × D1 (super-linear resolution architecture). Neither alone lands a gauge row.
- **`Mandate = 7T/(T+6)`** — the ratified LPS-1 formula; **unimplemented** in the live `Faction` class.

### 5.3 Combat balance baseline (measured 2026-06-28, N=300/cell — point-in-time, not targets)
- **Weapons vs arming (win %):** spear 91 · rapier 88 · staff 84 … arming 49 · dagger 31 · mace 28.
  Reach-dominated (r≈0.83); a *healthy* matchup spread by design.
- **Attributes (marginal +1, win %):** cog +26 · strength +20 · agi +20 · history +15 … disp +4.5 (≈neutral).
- **Traditions (unconditional vs field):** spread **6.8pp** (spanish 51.9 … none 45.1) — **exceeds the ±2–3pp
  band.** The WS-4 affinity-budget fix removed the gross edge (none 45.1→~49) but the **C1 contextual test
  shows only 2 distinct leaders across 5 contexts** (spanish broadly strong, chinese never leads ≤47.6%).
  Residual cause: **channel LEVERAGE** — some channels move win-rate more than others. Closing it is a
  **paradigm-strength design call (Jordan's)**, not a tuning pass.

### 5.4 mc_v18 campaign win-share (H3/H4)
| Batch | Result | Note |
|---|---|---|
| n=2/seed 0 (pinned golden) | `{Crown 50, Church 0, Hafenmark 0, Varfell 50}` | trivial (2 winners possible) |
| n=8/seed 42 (pinned golden) | `{Crown 37.5, Church 12.5, Hafenmark 12.5, Varfell 37.5}` | **no degeneracy** — the "87%" is debunked |
| n=100/seed 42 (ad-hoc, mine) | `{Crown 19, Church 12, Hafenmark 14, Varfell 55}` | Varfell over-indexed; **only n=100 datapoint anywhere**, in no ledger |
- Drivers of the residual skew are input-starvation, not a constant: faction-unique actions exist only for
  Crown+Church; Hafenmark has a one-way 0-territory elimination lockout (`ED-FA-0005`, no comeback path).

### 5.5 The emergence oracle (the proposed fix for "no balance claim without n≥100")
`02_emergence_oracle_spec.md` (PROPOSED): a deterministic n≥100 harness with `[SEED]` health bands —
**non-degeneracy** `max(win_share) ≤ 0.60` **and** `min ≥ 0.05`; **variety** `distinct_winners ≥ 3` **and**
`winner_entropy ≥ 1.0 bit`; **liveness** (`insurgencies_formed`, `arc_transitions`, `mandatory_fires` all
`> 0`) **expected to FAIL on the current tree — "that failure is the point"**; **determinism** `== true`.
Includes a perturbation battery that asserts `VICTORY_THRESHOLD` perturbation *should* shift outcomes and
**currently FAILS — documenting the dead param.** Report-only → blocking on the stable subset, on the weekly
`audit-refresh` cadence (never per-commit).

---

# §6 · Consolidated defect index

| Register | Source | Open items | Verdict |
|---|---|---|---|
| **D1–D8** (MC-wiring) | ED-IN-0074 | D1, D3, D6, D8 held (needs_jordan) | real; the strategic-loop bombs |
| **L1–L7 / N1–N9 / Q1–Q7** (character-decision) | ED-IN-0073 | docket UNRULED | L1/L2 verified at code level (§4.2); many CRITICAL |
| **DG-6..16** (mass-battle gauge) | ED-MB-0007 | all open, gated on DG-6 | churn-risk; progress negative-signed |
| **C-1..C-9** (character-decision dispositions) | ED-IN-0073 §5 | only C-7/C-9 ship in Slice A; rest phase-gated | needs Jordan per finding |
| **ED-SC-0004** (argue-pool) | SC lane | formula pick open | needs_jordan |
| **OPT-AV-1** (attribute roster) | ED-IN-0029 | deliberately deferred | standing hold |

Cross-cutting design-legibility hazards (not defects per se, but flagged):
**(a)** the "Truth" axis inversion (Truth 5 = canonically-wrong belief); **(b)** *four* distinct things named
"Piety Track" across the corpus (territory PT, the Scar-mechanic doc's self-title, a glossary mislabel of
the Persuasion Track, and the just-retired character meter folded into Truth).

---

# §7 · The decision ledger (leverage-ranked; what needs *you*)

See the Executive Summary table for the ranking. Expanded rationale:

1. **ED-1051 (engine_clock).** Highest leverage / lowest cost in the entire corpus. The home doc
   (`propagation_spec_v1.md`) is already CANONICAL; the authoring is done; the accounting/season spine is
   written *as if* it drives ticks. One ratification flip unblocks the temporal foundation and the Godot
   Gate-0 entry. **Default action:** flip `module_contracts.yaml` `engine_clock` `doc:null` → that path.
2. **D8 (roster fork).** No `Character` class can be built until you rule 9-attr (`descriptor_registry`, IN
   FLUX) vs 10-attr (`core.md`, de-facto live). The brief recommends ratifying the 9 with a compat layer.
3. **D3 (Mandate restore).** The fix is written and correct, but restoring Mandate **flips ~72% of campaign
   winners** — a real balance shift that needs sign-off *and* a golden rebaseline before it lands. This is
   the gate on any trustworthy n≥100 characterization.
4. **Character-decision docket (D2 5th-axis, D4 ratify C-1..C-9).** These unblock Convictions actually
   reaching contest verdicts (H2). D1 was already ruled per-NPC.
5. **DG-6 (MB resolution architecture).** The deepest single call, gating DG-6..16 — **but** the weekly
   review flags MB as the lane most at risk of churn-without-convergence; do not default-focus it until the
   gauge is *re-run*, not triaged against a frozen list.
6. **ED-SC-0004 (argue-pool).** Pick legacy vs kernel; the choice determines whether the low-pool regime
   survives.

---

# §8 · Currency corrections owed (the docs lying about themselves)

These are **stale-doc / citation defects, not design calls.** None changes mechanics; all reduce the
"documents misreporting their own state" surface that made an adversarial pass necessary in the first place.
Listed as findings; **not executed here** (this pass is analysis-only per its Status line).

| # | Surface | Defect | Fix |
|---|---|---|---|
| C-a | **CLAUDE.md §7** | asserts the debunked "~87% degeneracy" as a live fact | replace with the H3/H4 read (small-N artifact; n≥100 unmeasured) |
| ~~C-b~~ ↺ | ~~CURRENT.md "STAGED"~~ | **RETRACTED after review.** CURRENT.md:115 correctly labels the corpus-wide rename **STAGED** — only a partial sweep landed (`git show 6dd2f9f`: **96 files, +513/−475**) and **311 files still carry live `certainty`**. No fix owed; the follow-up sweep is real outstanding work | (none) |
| C-c | **`conviction_taxonomy_v30.md`** | 4 status assertions, 2 values (lines 1/2/6/9) | single-source via the `obs_core` `## Status:` regex owner (audit C-9) |
| C-d | **`clock_registry_v30.md`** | 3+ unstruck stale rows; `ED-793/794/795/796` tags cite unrelated closed items (pass CI green) | strike the rows; fix or remove the citations |
| C-e | **`mechanics_index.yaml:145,950`** | still keys the meter `certainty_track` (not in the documented keep-list) | re-key → `truth` |
| C-f | **`references/values_master.yaml`** | carries the struck Combat Pool formula (already quarantine-flagged) | out of scope until the typed-params migration (§CLAUDE.md 5) |
| C-g | **PR #185 review doc §5** | propagated the "~87%" claim (my own error) | remove; cite H3 |

**Meta-point:** C-a and C-c matter most, because CLAUDE.md §7 is a designated currency *authority*. When the
authority is stale, every downstream session inherits the error — exactly how the "87%" survived into five
docs and this program's own review (and, in the first draft of *this* audit, into a retracted C-b). This is
the propagation-lag failure mode CLAUDE.md §2 (ED-1094) was written to prevent, caught live — including
against itself. **The C-b retraction is the counter-example that proves the discipline:** CURRENT.md was
*right* to say STAGED; the adversarial pass, not deference, is what established which "authority is stale"
claims actually hold.

---

# Appendix A · Verification log (what was actually run)

| Claim | Method | Result |
|---|---|---|
| mc_v18 win-share | `python -c "from engine.mc_v18 import run_batch; run_batch(8,42).win_share"` | `{Crown 37.5, Church 12.5, Hafenmark 12.5, Varfell 37.5}` — **not** 87% |
| VICTORY_THRESHOLD dead | `pytest sim/tests/test_f7_smoke_oracle.py` | 6/6 pass incl. `test_f7_victory_threshold_is_a_dead_param` |
| Knot Pool settled | `pytest tests/valoria/test_knot_pool_formula.py` | 3/3 pass |
| Armature single-axis (L1) | ran `style_axis_alignment` on balanced + committed judges | balanced → all styles **0.7250**; committed → differentiates |
| Armature schism (L2) | printed `keys.AXES` vs `ArmatureAxis.ALL` | disjoint spaces confirmed |
| doc:null count | `grep -n "doc: null"` + line-level read | **9** fields (10th is a comment); CLAUDE.md's "10" stale |
| clock_registry citations | grepped `ED-793..796` in `editorial_ledger.jsonl` | all four are unrelated closed 2026-05-10 items |
| Truth rename **partially** executed | `git show 6dd2f9f` (96 files, +513/−475) + grep live corpus | SoT authored + partial sweep; **311 files still carry live `certainty`** → the corpus-wide sweep is genuinely STAGED (CURRENT.md accurate). Correction to the first draft, which overstated this |

*Filed as adversarial analysis. Governing docs named inline are authoritative; this audit ratifies nothing.
Grades: [VERIFIED] = independently reproduced · [CONTRADICTED] = verification refuted the received claim ·
[RELAYED] = taken from a named audit/ledger, not independently re-run.*
