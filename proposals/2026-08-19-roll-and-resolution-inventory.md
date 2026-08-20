# Roll and Resolution Inventory — every dice call, every obstacle, and everything that resolves without the engine

## Status: FINDINGS — mechanical inventory, AST-extracted. No design, no rulings. No `.py` touched. Compliance bookkeeping light per Jordan 2026-08-19; reconciliation against the in-flight infrastructure work pending.

**Date:** 2026-08-19 · **Companion to:** `proposals/2026-08-19-obstacle-stat-and-identity-census.md` (the 213-site obstacle census)
**Method:** Python `ast` parse of every `.py` under `engine/`, `systems/`, `tests/sim/` — **not** regex. An earlier regex pass over-counted (131 raw matches) by catching docstring mentions, and a naive docstring filter then *under*-counted; the AST numbers below are exact and match hand-verification at seven spot-checked sites. Reproducible from the method described in §6.

---

## §1 THE HEADLINE

**The ladder was single-owned by ruling and guarded by a test. The roller and the obstacle were never owned — so both forked.**

`systems/mass_battle/sim/massbattle.py` is the whole story in one file:

```python
def roll_pool(n, tn=7, rng=None):        # :627 — its OWN roller, forked
    ...
    elif tn <= f <= 9: net += 1          # :635 — and it HONOURS tn

def compute_degree(net, ob):             # :640 — the ladder, NOT forked
    from engine.autoload import dice_engine
    return dice_engine.degree_label(net, ob)   # :643 — delegates to the owner
```

Mass battle forks the **roller** and defers on the **ladder** — precisely because the ladder has an owner and a guard (`test_degree_ladder_single_owner.py`) and the roller has neither.

**And the fork is more correct than the owner.** The engine's `_die_result` (`dice_engine.py:53-61`) hardcodes the TN-7 face rule and ignores its own `tn` parameter. Mass battle's private roller writes `tn <= f <= 9` and therefore actually implements TN. **The only roller in the tree that honours TN is the unofficial copy.**

---

## §2 THE INVENTORY — 55 production call sites

| Subsystem | Rolls | …carrying an obstacle | …passing a TN | Adjudications | Adjudicator(s) used |
|---|---:|---:|---:|---:|---|
| factions | 9 | **7** | 8 | 2 | `degree_label`×2 |
| mass_battle | 8 | 0 | 0 | 4 | **`compute_degree`×3** (private), `degree_label`×1 |
| social_contest | 8 | 0 | 3 | 2 | **`degree`×2** (the HELD pool-aware surface) |
| combat | 4 | 0 | 2 | 2 | **`degree`×1** (private `core.degree`), `degree_label`×1 |
| threadwork | 4 | 0 | 4 | 6 | **four different ones**: `degree_label`×2, `_degree_label`×2, `_compute_degree`×1, `degree_from_net`×1 |
| engine_core | 2 | 0 | 2 | 2 | `degree_from_net`×2 |
| fieldwork | 1 | 0 | 1 | 1 | `degree_label`×1 |
| **TOTAL** | **36** | **7** | **20** | **19** | **6 distinct adjudicators** |

### §2.1 The obstacle reaches the dice owner from exactly one lane

**All 7 obstacle-bearing rolls are in `systems/factions/sim/`** — `absolution.py:65`, `council_solmund.py:63`, `crown_initiative.py:83/153/239`, `parliamentary_transfer.py:259`, `tribunal.py:125`. No positional obstacles exist (checked); the count is exact.

⚠ **This corrects the census synthesis**, which said obstacles reach the owner "from `systems/factions/sim/*` or `systems/threadwork/sim/*`." Threadwork passes **no** obstacle to any roller. It rolls bare and adjudicates in a second step:

```python
net_successes = roll_pool(pool, tn=tn, rng=rng).net    # operations.py:176 — no ob
degree = _compute_degree(net_successes, ob)            # :178 — private adjudicator
```

**So the real architecture finding is that rolling and adjudicating are decoupled in 6 of 7 subsystems.** The obstacle is not a parameter of *rolling* almost anywhere — it is an argument to a *local* degree function. That is why the obstacle has no owner: it was never on the owner's call path to begin with.

### §2.2 Nineteen TN parameters are inert

Nineteen production sites pass `tn=` into `dice_engine.roll_pool`, which ignores it:

`sigma_leverage.py:274` · `combat/sim/combat.py:214,216` (the Weapon TN Matrix **and** the defender's `def_tn`) · `factions/sim/{absolution:65, council_solmund:63, crown_initiative:83/153/239, mass_seizure:263, parliamentary_transfer:259, tribunal:125}` · `fieldwork/sim/knots.py:223` · `social_contest/sim/{contest_legacy_stub:163,164, parliamentary_vote:178}` · `threadwork/sim/{collective:164, operations:176, opposing:150,151}`

The 20th (`sigma_leverage.py:285` → `continuous_engine_sample`) is honoured, because the continuous path reads `_CONTINUOUS_PARAMS`.

---

## §3 RESOLUTION THAT NEVER TOUCHES `engine/`

This is the sharper question, and the answer is: **most of it.**

### §3.1 Four subsystems import no engine dice module at all

| Subsystem | Files importing `dice_engine` or `sigma_leverage` | How it resolves |
|---|---|---|
| **settlements** | **0 of 8** | fully deterministic — **zero** `rng`/`random` calls anywhere |
| **overview** | **0 of 8** | fully deterministic — zero randomness |
| **characters** | **0 of 5** | fully deterministic — zero randomness |
| **npcs** | 0 of 0 | no `.py` at all |
| world | 1 of 6 | raw `rng.choice` / `rng.randint` in the NPE (generation, not resolution) |
| combat | 2 of 29 | see §3.3 |
| fieldwork | 2 of 5 | knots only; the rest is stubs |
| mass_battle | 3 of 6 | private roller (§1) |
| threadwork | 4 of 9 | rolls bare, adjudicates privately |
| social_contest | 9 of 20 | private `roll_net` |
| factions | 13 of 18 | the one lane that uses the owner as intended |

Settlements, overview and characters resolve **entirely by threshold comparison and accounting arithmetic** — Prosperity/Order/Defense deltas, CI/RS/MS/IP track movement, conviction scar accumulation. There is no roll, so there is no obstacle, so R1 does not reach them at all. **That is a legitimate design, but nothing declares it**, and a reader looking for "where is the Order-0 revolt check" finds no check — only a comparison.

### §3.2 Six private roll/degree implementations in production

| Private owner | File:line | Forks what | Defers on what |
|---|---|---|---|
| `roll_pool` | `mass_battle/sim/massbattle.py:627` | the **roller** (and honours TN, unlike the owner) | the ladder — delegates at `:643` |
| `compute_degree` | `mass_battle/sim/massbattle.py:640` | nothing — a thin adapter | fully delegates |
| `roll_net` | `social_contest/sim/contest/resolver.py:26` | the roller | — |
| `degree` | `combat/combat_engine_v1/core.py:57` | the **ladder** (declared HOLD) | — |
| `_compute_degree` | `threadwork/sim/operations.py:135` | the ladder | — |
| `_degree_label` | `threadwork/sim/opposing.py:88` | the ladder | — |

Plus the `tests/sim/` cluster, which carries a **complete second dice stack**: `resolution.py:35 roll_pool`, `:44 roll_pool_fractional`, `:89 compute_degree`, and the `v32-combat-balance` set (`m1_dice_sigma_core.py:34,44`, `damage_model.py:74`, `r1_sigma_resolution.py:108`, `m4b_subaction_mechanics.py:105`). Note `tests/sim/mass_battle/` is **canon** per Jordan ruling J2 — so a canonical subsystem runs on a duplicate dice stack.

### §3.3 Personal combat resolves by probability gate, not by dice

**27 probability gates against 4 dice rolls**, and 31 raw RNG calls, across `wrapper.py`, `combat_systems.py`, `contact.py`, `capabilities.py`:

```python
if rng.random() < S.disengage_attempt_p(...) * S.reach_threat(...):   # wrapper.py:175
    if rng.random() < S.disengage_clean_p(...):                       # :176
riposte = (rng.random() < min(0.95, cfg['RIPOSTE_ON_FAIL'] + overcommit_exposure))  # :320
if rng.random() < cfg['DISPLACE_P']:                                  # :363
```

Measure closing, stop-thrust, disengage, riposte, bind dominance, displacement, counter-selection, grab escape, push availability and the upset floor are **all** resolved by comparing a raw uniform against a computed probability. The dice appear only at the final strike.

**Consequence for R1 and B3:** the obstacle doctrine reaches **four call sites** in personal combat. The overwhelming majority of what a player would call "a combat roll" is not a roll, has no obstacle, and no obstacle ruling can touch it.

### §3.4 The raw-RNG total

| Subsystem | Raw RNG calls | Probability gates |
|---|---:|---:|
| combat | 31 | 27 |
| world | 13 | 3 |
| factions | 5 | 0 |
| social_contest | 3 | 0 |
| threadwork | 3 | 0 |
| engine_core | 2 | 0 |
| mass_battle | 1 | 0 |
| **TOTAL** | **58** | **30** |

---

## §4 WHAT THIS MEANS FOR THE OPEN RULINGS

- **R1/B3's reach is far smaller than the obstacle census implied.** 213 obstacle *sites* exist, but only **36 rolls** in production and only **7** where an obstacle meets the dice owner. Combat's real resolution surface is probability gates; settlements/overview/characters have no rolls at all.
- **The TN question (§2.2) is upstream of the obstacle question.** Nineteen inert parameters, and the one roller that implements TN correctly is an unofficial fork.
- **"Single owner" was enforced on the ladder only.** The roller forked four ways in production and again in `tests/sim/`. If the obstacle gets an owner without the roller getting one, the same thing happens again — which is the §0.1-point-5 guard argument, now with a measured precedent rather than a prediction.
- **A decision is needed on whether probability gates are in scope for any resolution doctrine at all.** They are 30 of the tree's outcome-producing branches and no ruling has ever mentioned them.

---

## §5 THE FIVE COUNTS THAT MATTER

| | |
|---|---:|
| Production roll sites | **36** |
| …that hand an obstacle to the dice owner | **7** (all `systems/factions/sim/`) |
| …that pass an inert TN | **19** |
| Distinct adjudicator functions in production | **6** |
| Private roll/degree implementations (production) | **6** |
| Raw RNG calls / probability gates | **58 / 30** |
| Subsystems importing no engine dice module | **4** (settlements, overview, characters, npcs) |

---

## §6 METHOD AND WHAT I MIGHT HAVE MISSED

Extraction walked `engine/`, `systems/`, `tests/sim/`, parsed each file with `ast`, and collected every `ast.Call` whose function name is one of the four rollers or six adjudicators, recording the `ob=` keyword (or the second positional argument for degree-style calls) and whether `tn=` was passed. Test files, `test_*.py`, and `_kernel_tests.py` were excluded from production counts.

**Known limits, stated rather than hidden:**
- **Dynamic dispatch is invisible to this.** A roll reached via `getattr` or a callable stored in a dict would not appear.
- **Renamed imports are only partly caught** — I match on the called attribute/name, so `from x import roll_pool as rp` then `rp(...)` is missed.
- **Doc-specified rolls are not counted.** The obstacle census found many mechanics that exist only in prose; this inventory is code-only by design.
- **`ob` passed as a variable** is recorded as the variable name (`ob=ob`), not resolved to its value — resolving those is the next pass if you want the actual numbers.
- The three per-subsystem import counts in §3.1 are file-level greps for `dice_engine|sigma_leverage`, so a file importing a *wrapper* that itself imports the engine counts as 0. That understates indirect use and is the number I'd attack first.

**Spot-verified by hand:** the seven factions obstacle sites, `dice_engine.roll_pool`'s ignored `tn`, `massbattle.roll_pool`'s honoured `tn`, `massbattle.compute_degree`'s delegation, threadwork's decoupled roll-then-adjudicate, and the absence of any `queue_scene("combat")`.

---

# §7 DEFINITIONS AND PARAMETERS — which systems import from `engine/` or `references/`

Asked as a follow-up. The answer is structural and it is worse than "some systems don't."

## §7.1 `references/` has ZERO runtime readers

**Nothing in `engine/` or `systems/` loads any file under `references/`.** The four grep hits are all prose comments. Specifically:

| Registry | Runtime readers | `tools/` readers |
|---|---|---|
| `references/descriptor_registry.yaml` (the stat vocabulary owner) | **0** — one mention, in a comment at `game_state.py:106` | — |
| `references/names_index.yaml` (the naming owner) | **0** | — |
| `references/module_contracts.yaml` (the IO owner) | **0** | — |
| *all registries combined* | **0** | **44 modules** |

**The registries are a governance layer, not a runtime layer.** They are read by CI and tooling — 44 `tools/` modules — and by nothing the game executes. That is not a defect in itself; YAML registries as a CI surface is a legitimate pattern. But it has a consequence nobody has written down:

> **Every stat name, faction name and key-type string in the runtime is a hand-copied literal.** The registries govern them by convention and a warn-tier CI check, never by import. There is no mechanism by which changing `descriptor_registry.yaml` changes what the code does.

Measured duplication: **10** attribute-name literal lists, **11** faction-roster literals, **15** distinct key-type strings written as literals in code.

Worse, the copies don't even agree with their registry. `descriptor_registry.yaml` names the attributes **Acuity, Will, Attunement**; the code writes `cog`, `spirit`, `att` — the *aliases*, one of which (`Cognition`) is tagged `[ASSUMPTION] … Jordan veto`. The registry's primary names appear as code identifiers **nowhere**.

## §7.2 `engine/engine_params/` — one runtime loader, total

| Export | Loaded at runtime by |
|---|---|
| `key_types.json` | **`engine/cross_scale/echo_transport.py:68-69`** — the only one |
| `combat_engine_v1.json` | nothing (read by `workbench/structure_scan.py`, a tool) |
| `params_tables.yaml` | nothing |

The typed exports exist **for the Godot port**, and on the Python side they are write-only artifacts with a round-trip check. So the "typed layer" CLAUDE.md §5 describes as partly-built is, from the runtime's perspective, essentially unused.

## §7.3 Engine imports by subsystem — the full table

| Subsystem | `.py` files | importing `engine.*` | % | Engine modules used |
|---|---:|---:|---:|---|
| factions | 18 | 16 | **88%** | autoload, dice_engine, game_state, substrate |
| overview | 8 | 5 | 62% | game_state, season_manager, substrate |
| fieldwork | 5 | 3 | 60% | autoload, dice_engine, substrate |
| world | 6 | 3 | 50% | substrate, canon_buckets |
| social_contest | 20 | 9 | 45% | autoload, dice_engine, game_state, sigma_leverage |
| threadwork | 9 | 4 | 44% | autoload, dice_engine, substrate |
| characters | 5 | 1 | 20% | substrate only |
| mass_battle | 6 | 1 | 16% | autoload only |
| **combat** | **29** | **2** | **6%** | autoload, dice_engine |
| **settlements** | **8** | **0** | **0%** | **— none —** |

**`settlements` imports nothing from `engine/` at all.** It is fully self-contained, and it is also the *only* subsystem that loads external data at runtime — its own geography YAML (`registry.py:248`), not a registry.

**`combat` at 6% is the striking one.** The subsystem the repo treats as its most developed — 29 files, the physics engine, the balance workbench — touches the engine core in two files. That is consistent with §3.3: it resolves by probability gate, so it needs neither the dice owner nor the substrate.

## §7.4 What this means

1. **"Point at centralized definitions" is currently unachievable for a runtime module**, because the centralized definitions have no loader. Any design that says a module should resolve identifiers "via `descriptor_registry`" — including my own fieldwork proposal §6 — is specifying something the tree cannot do today. **That is a correction to my own work**, and it applies to the epistemic-propositions design too, which routes predicate names through registries.
2. **The vocabulary gate is warn-tier and reads code, not the reverse.** So the registries can drift from the runtime indefinitely, and the drift is already measurable — the primary attribute names exist in no code.
3. **If the Key substrate is the model** — `key_types.json` cooked from markdown and *loaded* by `echo_transport` — then the pattern for fixing this already exists in the tree, once, and could be extended to the stat vocabulary. That is the smallest concrete proposal this inventory suggests: **give `descriptor_registry.yaml` a cooked export and one runtime loader**, so stat names become imported rather than copied.
4. **Order of operations for anything Godot-facing:** GDScript will need these definitions too, and it cannot read Python literals. Every hand-copied literal in §7.1 is a value that must be re-typed by hand for the port, or exported first.

**Method note:** §7.3's counts are file-level AST import scans for any module whose root package is `engine`. A file importing a *wrapper* that itself imports the engine counts as 0, so these numbers understate indirect use — the same caveat as §6, and the number I would attack first if I wanted to argue combat is better integrated than 6% suggests.
