# Dossier — Code Architecture Evidence (Agent A, sonnet tier)
## Status: WORKING EVIDENCE — no verdicts; judgment reserved to the orchestrator
## Date: 2026-07-05

---

## 1. Campaign-loop reachability trace

Trace: `sim/mc_v18.py:run_campaign` → `sim/mc_v18.py:_faction_actions_callback` (passed as
`action_callback` into `sim/peninsular/season.py:run_season`) → `sim/cross_scale/scene_dispatch.py`.

| # | Evidence | Cite | Quote |
|---|---|---|---|
| 1a | `mc_v18.run_campaign` calls `run_season(world, action_callback=_faction_actions_callback)` | `sim/mc_v18.py:108` | `run_season(world, action_callback=_faction_actions_callback)` |
| 1a | `_faction_actions_callback` invokes the scene phase every season | `sim/mc_v18.py:83` | `scene_dispatch.run_scene_phase(world, world.rng)` |
| 1a | `season.run_season` composition (advance → callback → accounting) | `sim/peninsular/season.py:69-72` | `sr = advance_season(world)` / `if action_callback is not None: action_callback(world)` / `run_accounting(world)` |
| 1a | The only fireable trigger is Stability Crisis | `sim/cross_scale/scene_dispatch.py:51-58` | `# Stability Crisis (§4.3.2): Faction.Sta <= 2 -> emergency council (contest)` ... `fired.append({"trigger": "Stability Crisis", "scene_type": "contest", ...})` |
| 1a | "parties intentionally absent" comment | `sim/cross_scale/scene_dispatch.py:63` | `# parties intentionally absent: derivation bridge gap (flagged)` |
| 1a | Module-level GAP note names this the "CONTEXT-DERIVATION BRIDGE GAP" | `sim/cross_scale/scene_dispatch.py:19-24` | `CONTEXT-DERIVATION BRIDGE GAP: the strategic World holds AGGREGATE faction stats (L/Sta/W/I/Mil), not personal-scale actors. ... this module does NOT invent actors. When a queued scene lacks resolvable actors in its context, dispatch records a flagged deferral (reason='context-derivation gap') and resolves nothing.` |
| 1b | `_resolve_slot` deferral for contest scenes when no parties are present | `sim/cross_scale/scene_dispatch.py:100-104` | `elif st == "contest": parts = ctx.get("parties") ... if not parts or len(parts) < 2: out["reason"] = "context-derivation gap: no personal contest parties from aggregate faction state"; return out` |
| 1c | The live call path when parties ARE present resolves via the legacy stub | `sim/cross_scale/scene_dispatch.py:105-108` | `import sim.personal.contest as contest` / `cr = contest.run_contest(parts, ctx.get("stakes", {}), world=world, rng=rng)` |

**Verification that `contest.run_contest` resolves to the DEPRECATED legacy stub, not the promoted kernel:**

- `sim/personal/contest/__init__.py:33-36` (the package `contest` that `scene_dispatch.py` imports as
  `sim.personal.contest`) re-exports `run_contest` directly from the deprecated stub module:
  ```
  # ── Legacy surface re-exported for the two live importers (deprecate-not-delete) ──
  # scene_dispatch.py uses run_contest; parliamentary_vote.py uses the PERSUASION_* thresholds.
  from sim.personal.contest_legacy_stub import (  # noqa: F401
      run_contest, resolve_exchange, build_argue_pool, ContestResult, ExchangeResult, ...
  ```
- `sim/personal/contest_legacy_stub.py:2-13` module docstring self-identifies as deprecated and superseded:
  `⚠️ DEPRECATED (Stage 1b, 2026-06-30, designs/audit/2026-06-30-contest-stage0-reconciliation).
   SUPERSEDED BY the promoted groundup kernel package \`sim/personal/contest/\` (a real directory
   package). This 256-line single-compare stub is retained (deprecate-not-delete) ONLY as the
   provenance source ...`
- `sim/personal/contest/__init__.py:24` names the exact call site by line number in its own comment:
  `• sim/cross_scale/scene_dispatch.py:105  ->  import sim.personal.contest as contest ; contest.run_contest(...)`

**1d. Whole-repo grep for the promoted kernel API (`build_contest` / `resolve_contest` / `Bout`) outside
tests/the package itself:**

```
build_contest( calls outside tests/contest/: NONE
resolve_contest( calls outside tests/contest/: NONE
Bout( calls outside tests/contest/ and outside designs/audit/2026-06-03-contest-groundup/ (the
       pre-promotion prototype dir, itself not live code): NONE
```
Files that reference `build_contest`/`resolve_contest`/`Bout` at all (whole repo,
`grep -rln "build_contest\|resolve_contest\b\|\bBout\b" --include=*.py .`):
```
./designs/audit/2026-06-03-contest-groundup/{faction,narrative,resolver,tests}.py   (pre-promotion prototype, superseded per __init__.py:8)
./sim/tests/test_contest_kernel.py
./sim/personal/contest/{wrapper,faction,__init__,modes,narrative,resolver,_kernel_tests,rhetoric,armature}.py
./sim/personal/contest_legacy_stub.py   (does not itself call Bout/build_contest/resolve_contest)
./tests/sim_framework/{contest,engine,engine_v2}.py
./tests/sim/v32-combat-balance/{m4a_bout_state_graph,m6_dual_resource_economy}.py
```
No file outside `sim/tests/`, `tests/`, `sim/personal/contest/` (the package's own internal use), or the
retired `designs/audit/2026-06-03-contest-groundup/` prototype calls the promoted kernel API. The only
non-test production call into the contest subsystem (`scene_dispatch.py:106`) goes through
`contest.run_contest` — the re-exported legacy stub — not `build_contest`/`resolve_contest`/`Bout`.

---

## 2. Formula coexistence — two Argue-pool implementations

| Source | Cite | Formula (quoted) |
|---|---|---|
| Legacy stub `build_argue_pool` | `sim/personal/contest_legacy_stub.py:111-127` | Docstring: `"""§3 Argue Pool = (Primary Attribute × 2) + History bonus. ... [canonical: §3 — base formula. Wound penalty -1D per wound (PP-716) applied per actor.wounds attr if present.]"""` — code: `pool = (primary * 2) + history + (-1 * wounds) + fatigue_penalty` (`:126`), `return max(1, pool)` (`:127`) |
| Promoted kernel `Pool.size` | `sim/personal/contest/primitives.py:208-211` | `class Pool: BASE = 3  # [SEED]` (`:209`) / `@staticmethod` / `def size(faculty): return max(5, faculty * 2 + Pool.BASE)` (`:211`) |
| `params/contest.md` Pools table | `params/contest.md:19-25` | `| Argue (Expert Judge) | (Cognition × 2) + History bonus | 7 | ... |` / `| Argue (Crowd) | (Charisma × 2) + History bonus | 7 | ... |` / `| Argue (No Adjudicator) | (Attunement × 2) + History bonus | 7 | ... |` / `| Argue (Panel) | (Cognition × 2) + History bonus | 7 | ... |` — the table's floor/wound/fatigue terms are not stated in this table; it states the attribute×2+History core only. |

Observed: the legacy stub's formula (attribute×2 + History − Wounds + fatigue, floored at 1) cites
canon verbatim (`[canonical: §3 ...]`) and matches the `params/contest.md` Pools-table core term
(attribute×2+History). The promoted kernel's `Pool.size` is a different formula entirely
(`max(5, faculty*2+3)`), tagged `[SEED]` (not canon-cited), with a floor of 5 rather than 1 and a flat
`+3` rather than a History bonus term. Both are live in the repository; the legacy stub is the one
actually reached by `scene_dispatch.py` (see §1).

---

## 3. Contract drift — `module_contracts.yaml` vs. `sim/personal/contest/`

`references/module_contracts.yaml:425-447` (social_contest entry, quoted in full):
```yaml
  - module: social_contest
    registry_system: "social_contest"   # Key Type Registry vocabulary
    doc: designs/scene/social_contest_v30.md
    scales: [scene]
    resolver: dice_pool
    consumes:
      - {type: "state.opinion_revised", from: [npc_behavior]}
    emits:
      - {type: "scene.contest_resolved", terminal: false}
      - {type: "scene.dialogue", terminal: false}   # persuasion_track_displacement payload (PP-683 signed -5..+5)
      - {type: "scene.insult", terminal: false}
      - {type: "scene.threat", terminal: false}
    state:
      - {name: "persuasion_track", bucket: clock, writable: true}   # bucket track->clock [verification A4: bidirectional clock, terminal thresholds >=7 / <=3]
```

**Literal-string search inside `sim/personal/contest/` for each of the 5 Key/state strings:**

| Literal | Hits in `sim/personal/contest/` | Hits repo-wide (non-audit-prose) |
|---|---|---|
| `state.opinion_revised` | 0 | 0 in sim/ or tests/; only in `designs/audit/2026-05-01-stage-8-sim/sims/*.py` prose simulations |
| `scene.contest_resolved` | 0 | 0 in sim/ or tests/; only in `designs/audit/2026-05-01-stage-10-validation/` and `2026-05-01-stage-8-sim/` prose simulations |
| `scene.dialogue` | 0 | 0 in sim/; present in `tests/contracts/test_contract_adjudicator.py` (generic contract-adjudicator unit tests using it as an example type, not contest-specific) and the same `designs/audit/` prose simulations |
| `scene.insult` | 0 | 0 in sim/ or tests/; only `designs/audit/2026-04-30-architecture-session/sims/pp687_sim.py` |
| `scene.threat` | 0 | 0 in sim/ or tests/; only `designs/audit/2026-04-30-architecture-session/sims/pp687_sim.py` |
| `persuasion_track` (bare state name, not the Key type strings above) | 3 files — `wrapper.py` (2), `_kernel_tests.py` (2), `rhetoric.py` (2) | also `contest_legacy_stub.py` (8) |

None of the 5 literal Key-type/state strings the contract cites (`state.opinion_revised`,
`scene.contest_resolved`, `scene.dialogue`, `scene.insult`, `scene.threat`) appear anywhere in
`sim/personal/contest/`. `persuasion_track` (the state name, not the Key-type strings) does appear,
as a Python identifier/class name (`PersuasionTrack`), not as an emitted/consumed Key literal.

**Comparison field vs. the `personal_combat` contract entry** (`references/module_contracts.yaml:795-815`,
quoted):
```yaml
  - module: personal_combat
    registry_system: "personal_combat"   # Key Type Registry vocabulary
    doc: designs/scene/combat_engine_v1/   # CANONICAL (ED-900/904; docket ED-1029)
    godot_home: designs/godot/skeleton/engines/combat/   # CombatEngine (BaseEngine) + Strike/Wound modules (slice)
    typed_params: references/engine_params/combat_engine_v1.json   # GENERATED from config.py ...
    scales: [personal]
    resolver: d_sigma   # sigma-leverage continuous (sim.autoload.sigma_leverage since ED-1085; parity-tested vs the r1/m1 originals) ...
```
`social_contest`'s entry (lines 425-447) has no `godot_home:` key and no `typed_params:` key — both
fields present on `personal_combat`. `social_contest`'s `resolver:` is `dice_pool`; `personal_combat`'s
is `d_sigma`.

---

## 4. Stub inventory

**`modes.py` — 3 explicit `NotImplementedError` scaffolds:**

| Cite | Quote |
|---|---|
| `sim/personal/contest/modes.py:326-328` | `class DyadicMode: """SCAFFOLD. Steer one listener; success invisible; win = the listener adopts the course. To build.""" def play(self, *a, **k): raise NotImplementedError("dyadic counsel is a separate sub-system — scaffold only")` |
| `sim/personal/contest/modes.py:329-331` | `class NegotiationMode: """SCAFFOLD. Typed envoy latitude, escalating instruments; win = agreement in the overlap. To build.""" def play(self, *a, **k): raise NotImplementedError("negotiation is a separate sub-system — scaffold only")` |
| `sim/personal/contest/modes.py:332-334` | `class CeremonialMode: """SCAFFOLD. Nothing at issue (the corpus's point); builds/spends standing; win = acclamation. To build.""" def play(self, *a, **k): raise NotImplementedError("ceremonial is a separate sub-system — scaffold only")` |

**`wrapper.py` — the `GAMES` router table registers 3 STUB rows via one shared `_stub()` factory
(1 `raise NotImplementedError` call site parameterized by game name, not 3 separate literal raises):**

| Cite | Quote |
|---|---|
| `sim/personal/contest/wrapper.py:199-204` | `def _stub(game): def _f(contest, **kw): raise NotImplementedError(f"resolve_contest: game={game!r} is a registered STUB (Stage 1c) — not yet wired. Only game='agon' resolves this stage (see DECISIONS.md Stage-1 entry criteria).") return _f` |
| `sim/personal/contest/wrapper.py:206-215` | `GAMES = {"agon": {..., "status": "WIRED", ...}, "consensus": {"resolve": _stub("consensus"), "status": "STUB", ...}, "negotiation": {"resolve": _stub("negotiation"), "status": "STUB", ...}, "inquiry": {"resolve": _stub("inquiry"), "status": "STUB", ...}}` |

**`MECHANICS` registry** (`sim/personal/contest/wrapper.py:270-338`) — 20 rows total: 16 `WIRED`,
1 `PARTIAL` (`audience_resistance`), 3 `STUB` (`consensus_game`, `negotiation_game`, `inquiry_game`).

The `audience_resistance: PARTIAL` row (`sim/personal/contest/wrapper.py:295-301`):
```
"audience_resistance": {"fn":"_derive_resistance","toggle":None,
  "source":"params/contest.md §Persuasion Track (avg Stability round up −1, min 0) — DERIVED but not
  yet plumbed into resolution (ED-1055..1079)", "status":"PARTIAL"},
```
Preceding comment (`wrapper.py:295-300`): `F10 (judge-upheld): the derived value is computed and
carried on Contest.resistance but is NOT yet plumbed into resolution (the resolver has zero
'resistance' references; Venue.base_ob is never set from it). It is metadata-only this stage.
Downgraded WIRED->PARTIAL so mechanics_selftest does not over-claim a live mechanic.`

The 3 `STUB` `MECHANICS` rows (`wrapper.py:336-338`):
```
"consensus_game":   {"fn":None, "toggle":None, "source":"social_contest_v30 §10 BG-Vote / §7.2 (faction.py — Stage 4)", "status":"STUB"},
"negotiation_game": {"fn":None, "toggle":None, "source":"social_contest_v30 §2 Private Negotiation (author-new — later stage)", "status":"STUB"},
"inquiry_game":     {"fn":None, "toggle":None, "source":"social_contest_v30 §7 Church Tribunal (author-new — later stage)", "status":"STUB"},
```

---

## 5. `[SEED]` census

Total `[SEED]` tag count across `sim/personal/contest/*.py` (`grep -c "\[SEED\]"` per file, summed):
**78** total.

| File | `[SEED]` count |
|---|---|
| primitives.py | 24 |
| modes.py | 16 |
| armature.py | 11 |
| dictionaries.py | 6 |
| resolver.py | 6 |
| _kernel_tests.py | 5 |
| appraise.py | 3 |
| narrative.py | 2 |
| rhetoric.py | 2 |
| contract.py | 1 |
| faction.py | 1 |
| wrapper.py | 1 |
| __init__.py | 0 |
| policy.py | 0 |

**Named `[SEED]` constants and their values:**

| Constant | File:line | Value | Comment |
|---|---|---|---|
| `Standing.BUILD, STRIP` | `primitives.py:33` | `0.8, 0.8` | `# [SEED]` |
| `Standing.MAX` (implied, cap) | `primitives.py:50` | `12` | `# [SEED]` |
| `RhetoricalWeights` 9 fields (logos/ethos/pathos × past/present/future) | `primitives.py:192-202` | `1.20 / 1.00 / 0.80` (logos); `0.85 / 1.20 / 0.95` (ethos); `0.85 / 0.90 / 1.25` (pathos) | `# All nine entries are [SEED] — Jordan to calibrate.` (`:183`) |
| `Pool.BASE` | `primitives.py:209` | `3` | `# [SEED]` |
| `SelfGating.MARGIN` | `primitives.py:214` | `1.0` | `# [SEED]` |
| `Resonance` cap (`CAP`) | `primitives.py:233` | `3.0` | `# [SEED] pathos's target; feeds readiness` |
| `Readiness.ETHOS_UNLOCK` | `primitives.py:241` | `0.5` | `# [SEED]` |
| `Readiness.LEAK_CAP` | `primitives.py:242` | `0.9` | `# [SEED]` |
| Readiness `FLOOR` | `primitives.py:255` | `0.40` | `# [SEED] raised from 0.35: floor is competitive enough without ethos/pathos investment` |
| Readiness `W_STANDING, W_ROOM` | `primitives.py:256` | `0.40, 0.40` | `# [SEED] lowered from 0.50: reduces 1.66x amplification to ~1.35x` |
| `Dossier.CORROB` | `primitives.py:295` | `(1.0, 0.7, 0.5, 0.35)` | `# [SEED] diminishing returns; beyond → 0.25` |
| `MERIT_SCALE` | `resolver.py:37` | `2.6` | `# [SEED]` |
| `JITTER` | `resolver.py:38` | `0.08` | `# [SEED] irreducible variability in how persuasion lands` |
| `PUBLIC_LEAK` | `resolver.py:39` | `0.5` | `# [SEED] public pressure → adjudicator susceptibility` |
| `INST_BIAS` | `resolver.py:40` | `0.6` | `# [SEED] institutional thumb on the scale` |
| `PUB_BIAS` | `resolver.py:41` | `0.3` | `# [SEED] public favour tilt` |
| `EVIDENCE_CAP` | `resolver.py:42` | `3.0` | `# [SEED] ceiling on one evidence item's magnitude (audit R1/R4: bound the readiness-free channel)` |
| `RES_FLOOR` | `resolver.py:33` | `0.15` | `# de-saturation floor (diagnostic Lesson 6): a hostile/off-axis reception can't zero` |
| `REBUT_CAP` | `resolver.py:35` | `3.0` | `# Fork 3 (PROTOTYPE): max advantage a single rebuttal can erase — bounds the one` |
| `STYLE_AXIS_PRIMARY` | `armature.py:228` | `1.0` | `# [SEED] a style's on-axis (targeted-vulnerability) projection weight` |
| `STYLE_AXIS_OFFAXIS` | `armature.py:229` | `0.15` | `# [SEED] off-axis partial overlap; = resolver.RES_FLOOR value (reused, not fresh)` |
| Venue institutional profiles (court/disputation/assembly/appeal/institutional/public_oration/inquisition/excommunication/imperial_petition/secret_council/memorial_remonstrance) | `modes.py:111-297` (each preset docstring) | discipline/char_logos/ethos/pathos floats per venue | `# [SEED] every numeric below (proof weights, thresholds, jury noise, panel size) — Jordan to calibrate.` (`:111`); each preset's docstring individually repeats `[SEED] all numeric values.` (e.g. `:174, :191, :210, :232, :250, :272`) |

Note: `RES_FLOOR` and `REBUT_CAP` (`resolver.py:33,35`) are NOT tagged `[SEED]` in-line (their comments
describe rationale/provenance, not a `[SEED]` marker) — flagged here because the task instructions named
them among the census targets, but the literal `[SEED]` tag is absent from their own lines; they are
cross-referenced as `[SEED]`-adjacent by `armature.py:229`'s comment (`STYLE_AXIS_OFFAXIS ... =
resolver.RES_FLOOR value (reused, not fresh)`).

---

## 6. Test-oracle shape

**`sim/tests/test_contest_kernel.py`:**
- Runs `sim/personal/contest/_kernel_tests.py` as a subprocess (not a pytest module) and asserts on its
  stdout. Docstring (`:1-12`): `"""sim/tests/test_contest_kernel.py — pytest gate for the promoted
  groundup contest kernel. ... The kernel suite (sim/personal/contest/_kernel_tests.py) is the
  groundup tests.py (random.seed(20260603), gates via sys.exit, prints "RESULT: N passed, 0 failed").
  It runs as a script, not a pytest module, so this wrapper executes it as a subprocess and asserts
  both the exit code (0) and the ">= 151 passed, 0 failed" line — the master parity guard for the
  promotion + rewiring."""`
- The expected count constant: `sim/tests/test_contest_kernel.py:84` — `_KERNEL_EXPECTED = 385   # 377
  through Gate-C RE-REVISION #3 ... + 7 Gate-C FINAL ratification (ED-1062) + 1 Gate-C closeout fix ...`
  (a long provenance comment tracing the count's growth stage-by-stage).
- Assertion logic (`:89-101`): asserts `passed >= _KERNEL_FLOOR` (the "behavior-preserving floor",
  151) AND `passed == _KERNEL_EXPECTED` (385) — i.e. it gates on an exact expected count, not just a
  floor.

**`sim/tests/test_mc_v18_regression.py`:**
- Docstring states scope explicitly (`:1-22`): `"""Deterministic seeded regression oracle for the
  Valoria simulation reference. ... \`mc_v18.run_batch(n=2, base_seed=0)\` — two 50-season campaigns
  on fixed seeds [0, 1]. Runtime ≈ 5 s. **The happy path does not touch any of sim's
  NotImplementedError stubs.**"""` (emphasis on the quoted sentence per task item).
- The pinned golden output (`:32-35`) is combat/territory-only: `GOLDEN_WIN_SHARE = {'Crown': 50.0,
  'Church': 50.0, 'Hafenmark': 0.0, 'Varfell': 0.0}`, `GOLDEN_WINNERS = {'Crown': 1, 'Church': 1}`,
  `GOLDEN_BATTLES_MEAN = 38.0` — no contest-specific assertions (persuasion track, contest count,
  contest winners) appear anywhere in this file.

**`tests/valoria/` — confirmed zero dedicated contest test files:**
- `find tests/valoria -iname "*contest*"` → no results.
- `grep -rl "contest" tests/valoria/` → only one hit, `tests/valoria/test_combat_invariants.py`
  (a combat test that happens to mention "contest" in passing text, not a contest test file).
- Directory listing of `tests/valoria/` (20 files) contains combat/mass-battle/CI-checker/names/coverage
  test files only — no `test_contest*` or `test_social*` file exists.

**`python -m pytest sim/tests -q --collect-only`** (read-only, run):
```
949 tests collected
```
Breakdown by originating file:
```
      1 sim/tests/test_contest_kernel.py
      3 sim/tests/test_mc_v18_regression.py
    945 sim/tests/test_sigma_leverage_parity.py
```
The contest kernel's 385 internal checks are NOT individually pytest-collected — they surface to
pytest as a single collected item (`test_contest_kernel.py`, 1 test) that subprocess-runs and greps the
385-count from stdout, per the mechanism described above.

---

## 7. σ-kernel sharing

`sim/autoload/sigma_leverage.py` header (`:1-19`):
```
"""
sim/autoload/sigma_leverage.py — σ-leverage advantage layer atop the d10 dice engine.
...
Purpose
-------
Single-source the σ-leverage modifier layer for BOTH combat and social-contest, retiring:
  • the test-dir dependency (tests/sim/v32-combat-balance/m1_dice_sigma_core.py)
  • the numpy dependency that file carried
  • the combat sys.path.insert hack (designs/scene/combat_engine_v1/core.py:3)
  • the distillation report's "two σ-kernels" debt
```

**Functions `sim/personal/contest/resolver.py` imports from it** (`resolver.py:18-24`):
```python
# Stage 1b: rewired to the ONE canonical σ-kernel (sim.autoload.sigma_leverage), replacing the
# ...
from sim.autoload import sigma_leverage as _sigma
from sim.autoload.sigma_leverage import effective_ob, degree, net_boost
```

Whole-repo grep for `sigma_leverage` importers (`grep -rln "sigma_leverage" --include=*.py .`):
```
sim/autoload/sigma_leverage.py                              (the module itself)
sim/tests/test_contest_kernel.py
sim/tests/test_sigma_leverage_parity.py
sim/personal/contest/{wrapper,faction,__init__,resolver,primitives,_kernel_tests,armature}.py
designs/scene/combat_engine_v1/core.py                       (see §Anomalies below)
designs/audit/2026-05-28-resolution-diagnostic/sim_faction_remediation.py
tests/valoria/test_combat_balance_guard.py
tests/sim/v32-combat-balance/m1_dice_sigma_core.py
```

---

## 8. `parliamentary_vote.py` coupling

**The 5 constant imports** (`sim/personal/parliamentary_vote.py:41-48`):
```python
# Shared Persuasion-Track thresholds (§6) — single source of truth, do NOT redefine:
from sim.personal.contest import (
    PERSUASION_WIN_THRESHOLD,        # 7  [canonical: social_contest_v30 §6/§10]
    PERSUASION_LOSS_THRESHOLD,       # 3
    PERSUASION_TOTAL_VICTORY,        # 9
    PERSUASION_TOTAL_DEFEAT,         # 1
    PERSUASION_TRACK_START_DEFAULT,  # 5
)
```
Module docstring corroborates (`:7-9`): `Status: [implemented: 2026-05-31 — §10 BG vote against
social_contest_v30. Faction-scale Mandate-pool resolution (NOT the §1-9 personal argue-pool contest);
reuses the shared Persuasion-Track threshold constants from sim.personal.contest §6.]`

**Confirmed: never calls `Bout`/`build_contest`/`resolve_contest`/`run_contest`.**
`grep -n "Bout\|build_contest\|resolve_contest\|run_contest" sim/personal/parliamentary_vote.py` →
no matches (empty output). Its own resolution path is independent — `BG_VOTE_TN`, `BG_VOTE_GENRE_BONUS`,
etc. (`:51-60`), rolled via `sim.autoload.dice_engine` (`:38`) directly, not through the contest kernel
or the legacy stub's `run_contest`/`resolve_exchange`.

---

## 9. Audience-resistance erosion — canon vs. code

**`params/contest.md:365`** (ED-295, Option D, quoted):
```
- **ED-295** (CLASH stalls at median margin): Option D — audience resistance erodes per exchange.
Per-exchange erosion: `Stab_resistance_t = max(0, Stab_resistance_0 − ⌊exchange_count / 2⌋)`. First
exchange uses baseline resistance; every two exchanges thereafter reduces audience resistance by 1.
Long contests resolve organically; short contests retain current dynamics. Spec applies to all
Interaction Types (CLASH, REINFORCE, CROSS, Coalition Push).
```

**`wrapper.py._derive_resistance()`** (`sim/personal/contest/wrapper.py:36-53`, quoted in full):
```python
# "Audience resistance: average Stability of factions (round up) − 1, minimum 0." The proceeding's
# resistance MODIFIER scales it: Standard = ×1, Halved (Royal Audience / Church Tribunal) = ÷2 for the
# advantaged party, N/A = 0 (untracked proceedings). Numeric resistance is derived from WORLD Stability
# passed in at build time — never fabricated. Returns None when the proceeding has no tracker.
def _derive_resistance(proc_name, world):
    spec = PROCEEDINGS[proc_name]
    if not spec["tracker"] or spec["resistance"] == "none":
        return None
    stabilities = (world or {}).get("stabilities") if isinstance(world, dict) else None
    if not stabilities:
        return 0  # no world Stability supplied → canonical minimum (params/contest.md: "minimum 0")
    import math
    base = max(0, math.ceil(sum(stabilities) / len(stabilities)) - 1)  # §Persuasion Track formula
    if spec["resistance"].startswith("halved"):
        base = math.ceil(base / 2)  # "Halved for petitioner/accused (round up)" (social_contest_v30 §7)
    return base
```
`_derive_resistance` takes no `exchange_count` parameter and performs no per-exchange recomputation —
it derives a single static value from world Stability at build time (called once from
`build_contest`, `wrapper.py:158`). It is also the function tagged `PARTIAL` in `MECHANICS`
(§4 above) because its output is "computed and carried on `Contest.resistance` but is NOT yet plumbed
into resolution."

---

## 10. Module inventory

14 files total in the live contest surface (13 inside the `sim/personal/contest/` package + the
separate `sim/personal/contest_legacy_stub.py`):

| Module | LOC (`wc -l`) | One-line role (from its own docstring) | Self-asserted status |
|---|---|---|---|
| `__init__.py` | 135 | Package entry point; re-exports both the legacy stub surface and the promoted kernel API. | `[Stage 1b — substrate promotion + σ-kernel unification, 2026-06-30]` |
| `contract.py` | 77 | "shared types between the wrapper (resolver) and policies... breaks the resolver<->policy cycle. Side identity is defined once here." | (no explicit Status: line) |
| `primitives.py` | 310 | "the general, emergent substrate. Same across venues; the venue (top-down) shapes how they resolve. Numbers are [SEED]s." | (no explicit Status: line; numbers self-flagged `[SEED]`) |
| `resolver.py` | 450 | "the WRAPPER + the top-down VENUE spec. No privileged 'merits': primitives accumulate a per-side advancement; the venue's win-condition decides what winning is..." | (no explicit Status: line) |
| `modes.py` | 552 | "institutions as top-down VENUE specs. Each venue supplies its proof-weighting, its win-condition..., and its defeat-catalogue..." | Contains 3 explicit `SCAFFOLD` classes (§4); rest are `[SEED]`-tagged presets |
| `policy.py` | 60 | "decoupled policies (read-only ContestView → Move via contract; no resolver internals)." | (no explicit Status: line) |
| `faction.py` | 145 | "ADAPTER (not canon). Models the canonical Parliamentary action (faction_layer §5) on the contest engine, to exercise the engine in the faction-action context." | Explicitly self-labeled "not canon" |
| `narrative.py` | 170 | "turns a resolved bout into legible, story-shaped output. PURE CONSUMER of the raw beat log produced by Bout(record=True); it never touches resolution." | (no explicit Status: line) |
| `dictionaries.py` | 756 | "the Stage-2 TYPED DICTIONARIES (Gate B)... the contest's four canonical dictionaries live HERE as frozen Python dataclasses, single-sourced with the canonical prose tables in params/contest.md." | Stage 2 / Gate B |
| `armature.py` | 451 | "the ADJUDICATOR ARMATURE (Stage 3 / Gate C; the ★★★★★ fix)." | Stage 3 / Gate C |
| `rhetoric.py` | 524 | "Stage 3 / Gate C: making the classical/Renaissance grounding MECHANICAL, not nominal." | Stage 3 / Gate C |
| `appraise.py` | 177 | "Stage 3 / Gate C: the APPRAISE-REVEAL BOUNDARY for the adjudicator armature_position." | Stage 3 / Gate C |
| `wrapper.py` | 412 | "public API wrapper for the social-contest engine... ADAPTS + ROUTES; it RESOLVES NOTHING." | Stage 1c (build/resolve adapter + router, per `__init__.py:72` import comment) |
| `_kernel_tests.py` | 1639 | "unit + venue/win-condition/defeat + invariants + integration. Run: python3 tests.py" | Internal test suite; gates at 385 checks (§6) |
| `contest_legacy_stub.py` (outside package) | 266 | "DEPRECATED single-compare social-contest stub" | `⚠️ DEPRECATED (Stage 1b, 2026-06-30)` |

Total LOC across the 14 files: 6,124 (`wc -l` sum, all files above including `_kernel_tests.py` and
the legacy stub).

---

## Anomalies noticed in passing

- **Two independent combat implementations differ in σ-kernel usage.** `sim/personal/combat.py` — the
  module actually imported and invoked by the live campaign loop (`sim/cross_scale/scene_dispatch.py:96-97`,
  `import sim.personal.combat as combat; combat.resolve_combat_round(...)`) — imports only
  `sim.autoload.dice_engine.roll_pool` (`sim/personal/combat.py:42`) and never imports
  `sigma_leverage`. The separate `designs/scene/combat_engine_v1/core.py` (cited as canonical
  `personal_combat`'s `doc:` in `module_contracts.yaml:797`) does import `sigma_leverage`. The
  `sigma_leverage.py` module header's claim to "single-source the σ-leverage modifier layer for BOTH
  combat and social-contest" is verified true for social-contest (`resolver.py`) but the live/dispatched
  combat module (`sim/personal/combat.py`) does not itself import `sigma_leverage` — only the
  `designs/scene/combat_engine_v1/core.py` variant does.
- **`module_contracts.yaml`'s `social_contest` entry cites `doc: designs/scene/social_contest_v30.md`**
  (`:427`) while the actual live-code canonical source repeatedly cited inside `sim/personal/contest/`
  is `params/contest.md` plus the same `social_contest_v30.md` — both are cited in-code, but the
  contract's single `doc:` field names only the v30 doc, not `params/contest.md` (contrast
  `personal_combat`'s contract entry which points `doc:` at a directory, `designs/scene/combat_engine_v1/`).
- **The `MECHANICS` registry counts 20 rows** (16 WIRED / 1 PARTIAL / 3 STUB) but the `GAMES` router
  table counts 4 rows (1 WIRED / 3 STUB) — these are two separate registries in the same file
  (`wrapper.py`) with overlapping but not identical stub accounting (e.g. `agon_bout` in `MECHANICS`
  wraps the same `Bout` that `GAMES["agon"]` routes to; the 3 `MECHANICS` STUB rows
  `consensus_game`/`negotiation_game`/`inquiry_game` correspond 1:1 to the 3 `GAMES` STUB rows
  `consensus`/`negotiation`/`inquiry`).
- **`sim/tests/test_mc_v18_regression.py`'s golden win-share** (`Crown 50%, Church 50%, Hafenmark 0%,
  Varfell 0%` at n=2 seeds) is a small-batch (n=2) pin, distinct in magnitude from the larger-batch
  degenerate distribution CLAUDE.md §7 describes (one faction ~87%, two at 0%) — the two are not
  the same run size and this dossier does not reconcile them (no verdict rendered).
- **`resolver.py`'s `RES_FLOOR`/`REBUT_CAP` constants are not literally tagged `[SEED]`** on their own
  lines (`resolver.py:33,35`) even though they are numeric calibration constants of the same character
  as the file's other `[SEED]`-tagged constants (`MERIT_SCALE`, `JITTER`, etc., `:37-42`); the only
  `[SEED]` cross-reference to `RES_FLOOR` is indirect, via `armature.py:229`'s comment noting
  `STYLE_AXIS_OFFAXIS ... = resolver.RES_FLOOR value (reused, not fresh)`.
- **`tests/contracts/test_contract_adjudicator.py`** uses the literal string `"scene.dialogue"`
  extensively (`:19,63,70,129,146,153,156,160,198,199,349,351`) but as a generic example Key-type
  string for testing the contract-adjudicator tool itself, not as a contest-specific behavioral test —
  it is not a contest test and does not exercise `sim/personal/contest/`.
