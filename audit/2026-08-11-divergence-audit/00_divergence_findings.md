# Repo-wide divergence audit — divergent implementations, approaches, vocabularies and meanings

## Status: REPORT — RATIFIES NOTHING. No ED allocated, no `## Status:` line flipped, no code changed.

_Audited 2026-08-11 at `a8f76b8` on `claude/python-architecture-audit-k5t0bc`._
_Scope: `systems/` (115 py, 25,116 LOC), `engine/` (38 py, 7,911), `tools/` (108 py, 28,837), plus
`tests/valoria/`, `engine/tests/`, `tests/sim/` where a convention is pinned or a canon engine lives._

Successor to `audit/2026-08-11-systems-python-architecture-audit/`. That report differenced modules on
three axes and found "the corpus duplicates approaches, not text". This one asks the next question —
**where do two pieces of code mean different things by the same name?** — across nine lenses.

---

## 0. Method, and its honest limits

Nine independent read-only lenses (tools: Read/Grep/Glob only — no write tools, so independence is
structural rather than declared, per §10). Each was given the relevant prior findings as GIVEN and
told to attack them. Each was placed under a hard exhaustiveness contract and required to name a
falsifier per claim (§0.1 point 3).

**Every location in this report is mechanically verified.** `01_locations.tsv` carries 168 rows across
47 groups; `verify_locations.py` confirms each row's file exists, the line is in range, and the line
contains the claimed token. Current state: **168/168 OK at strict zero-fuzz.** The verifier is
mutation-tested (wrong line → `MISMATCH`, missing file → `NO_FILE`, past-EOF → `OUT_OF_RANGE`) and
treats line drift as failure rather than tolerance.

**Limits, stated plainly:**

- **I could not execute the tree.** Every runtime claim below is read-derived. Where a one-line
  command would settle a question, §7 lists it with the outcome that confirms or refutes.
- Lens 9 (parameter sourcing) returned after the first draft; §6 now carries its results rather than
  the gap notice it originally held. Its coverage is exhaustive within the constant *surfaces* of
  every module but not within the full bodies of `massbattle.py`, `combat_systems.py`, `weapons.py`
  and the settlements/world sims — uncited-literal counts from those files are a floor.
- **Grep blind spots are real and disclosed**: dynamic access (`setattr`, `**kwargs`, dict-driven
  field names) and duck-typed test doubles. The state-mutation lens flags exactly where its sweep
  could be incomplete for those reasons.
- **Coincidental equality is the main way a duplication sweep goes wrong.** Every duplicate claimed
  here carries an argument for why two sites mean the same thing.

### 0.1 Corrections to my own prior report

Three, all found by the lenses attacking their GIVENs, all verified by hand:

| Prior claim | Correction |
|---|---|
| C5 cited `systems/threadwork/sim/knots.py:353,366` | **That path does not exist.** `knots.py` is in `systems/fieldwork/` (restructure slice 6). My citation was dead. |
| C5 called them "`except: pass`" | **Zero bare `except:` exist** in `systems/`, `engine/` or `tools/`. Every swallow is typed, almost all `except (ImportError, AttributeError)`. The defect class is AttributeError-conflation, not bare-except — a materially different fix. |
| B1 said "nine implementations" of degree | **Materially incomplete.** At least seven more exist, including `tests/sim/mass_battle/resolution.py:89` — the J2-ruled *canon* engine, and the only epsilon-guarded ladder — which was absent while its deprecated twin was listed. |
| B2 cited `dice_engine.py:68` for `random.Random()` | Off by one; the statement spans `:68-69` and the call is on `:69`. Caught by the verifier on its first run. |

---

## 1. Verdict

| Lens | Divergence groups | Confirmed defects |
|---|---|---|
| 1 · Outcome/degree vocabulary | 16 producers, 6 vocabularies, 5 Overwhelming formulas | 1 |
| 2 · Dice & RNG | 8 pool dialects, 6 RNG-acquisition idioms | 3 |
| 3 · Identity & keying | 7 faction dialects, 2 treaty key types | 3 |
| 4 · State mutation | 12 quantity groups | 2 |
| 5 · Cross-scale seams | 20 seams | 6 |
| 6 · Interface shape | 8 result-container dialects, 8 event channels | 2 |
| 7 · `tools/` rule duplication | 12 rules, 23 walkers with bespoke exclusions | 3 |
| 8 · Failure/absence | 9 conventions for one situation | 1 |
| 9 · Parameter sourcing | 18 parameters, 9 sourcing idioms | 3 |

**The single structural fact.** There is no identity normaliser, no shared vocabulary owner, and no
convention guard anywhere in the two design trees. Every divergence below is safe exactly while the
two dialects never touch, and nothing in the repo makes that a property rather than a coincidence.

---

## 2. Confirmed defects — verified by hand, ranked by consequence

Each was claimed by a lens and then re-verified by me directly against the tree.

### D1 · HIGH — the `tn` parameter is dead in the canonical discrete roller

`engine/autoload/dice_engine.py:43` `_die_result(face)` takes **only** `face`. The face rule is
hardcoded (`1→−1, ≤6→0, ≤9→+1, 10→+2`), i.e. TN 7. `roll_pool` (`:65`) accepts `tn`, stores it in
`RollResult`, and never applies it.

Threadwork declares three non-7 target numbers — `TN_BINDING = 8` (`operations.py:47`), `TN_POP = 8`
(`:48`), `TN_POP_BINDING = 9` (`:49`) — and passes them straight in at `:176`. **Lock, Dissolution,
Past-Oriented Pulling and POP-Binding all resolve at TN 7 odds.** Per-die EV 0.40 where canon
specifies 0.30 / ≈0.20. Same for `collective.py:149` and `opposing.py:127`.

Two things sharpen this. The engine **disagrees with itself**: `_CONTINUOUS_PARAMS`
(`dice_engine.py:58`) *is* TN-aware (μ = 0.50/0.40/0.30), so `roll_pool(N, tn=6)` and
`continuous_engine_sample(N, tn=6)` — documented as statistically equivalent — differ by 0.10/die.
And `massbattle.py:627` re-implements the roller *with* TN parameterization, so the two agree only at
TN 7. **No test in the tree rolls any dialect at tn≠7.**

### D2 · HIGH — the Political Stability leg of the victory condition is dead

`engine/autoload/victory.py:73` reads `world.clocks.get('Turmoil', 0.0)` as Political Stability.
`Turmoil` has **exactly two references in the entire tree**: its initializer
(`game_state.py:244`) and this read. Zero writers. So `ps` is always `0.0` and `ps <= PS_MAX (6.0)`
is unconditionally true.

Compounding it, `victory.py:71` gates Accord as `t.accord >= ACCORD_MIN` with `ACCORD_MIN = 2.0` —
raw continuous compared against a threshold stated in canonical-index units. Canon Accord 2 is
continuous **4.0** (`ACCORD_MAP`, `game_state.py:58`); the gate passes at 2.0, which
`canonical_accord` buckets as **1**. Two of the three legs of peninsular sovereignty are materially
easier than GD-1 states, one of them vacuously.

### D3 · HIGH — Mass Seizure corrupts two pieces of state at once

`systems/factions/sim/mass_seizure.py` computes `starting_accord` as a **canonical index** (2 or 3,
`:277`) and writes it raw onto the **continuous** field at `:295`. Since `canonical_accord` buckets
anything below 3.25 as 1, both the Success (index 2) and Overwhelming (index 3) outcomes read back as
canonical Accord **1** — the degree distinction is erased and both under-deliver by 1–2 buckets. The
comment at `:293` asserts it is "the same continuous scale"; it is not. The correct sibling is
`parliamentary_transfer.py:278` (`terr.accord = ACCORD_MAP[accord_level]`).

Independently, `:292` sets `t.owner = 'Church'` without touching either faction's `.territories`
list — and ownership is represented **both** ways, with `_holder_of` (`parliamentary_transfer.py:96`)
deriving it by scanning the lists. `parliamentary_transfer.py:279` carries a bugfix comment recording
that this exact desync already happened once at that site.

Currently latent: `resolve_mass_seizure` has no callers. But `is_available()` advertises it.

### D4 · HIGH — a blocking CI gate has examined zero items since 2026-08-05

`tools/ci_co_file_checker.py:90` builds its params candidates exclusively under `engine/params/…` and
gates on `os.path.exists`. **That tree was evacuated on 2026-08-05.** `existing` is therefore always
empty, the `continue` at `:95` fires unconditionally, and Rule 4 — "mechanical value change requires a
params co-change", one of the four rules the tool exists for — has never fired since.

It is blocking in both tiers (`valoria-ci.yml:116`, `valoria_local.py:157` with `True`).

This is the **retired `patch_propagation_checker` pattern recurring** — CLAUDE.md §8 documents that
one as having "examined zero items for weeks while sitting in the blocking tier". The pattern was
diagnosed, the instance was retired, and the sweep for siblings never happened. §0.1 point 5.

### D5 · HIGH — the Muster wealth cost is 100× under-scaled

`faction_action.py:515` calls `faction.adjust('W', -MUSTER_WEALTH_COST)` with
`MUSTER_WEALTH_COST = 1` (`:69`). The convention is `delta_points × MULTS[stat]`, and
`adjust` divides by `MULTS` (`game_state.py:128`), with `MULTS['W'] = 100`. So the up-front cost is
**−0.01 W**, not −1.0.

ED-FA-0009 made this cost carry the failure-penalty role it removed. Four musters cost 0.04 W against
a starting 4.0. Muster is a no-downside lottery.

### D6 · MEDIUM — two ED-numbered mechanics are wired as permanently-false defaults

`engine/cross_scale/zoom_in_out.py:138` reads `scene_outcomes.get('pc_incapacitated', False)` and
`:149` reads `.get('contested_figure_wounded', False)`. **Neither key has a producer anywhere.** Each
appears exactly twice in the tree: once in a docstring, once in the `.get`. So ED-159 (Stage-1
incapacitation) and ED-167/ED-PC-0006 (contested-figure wound, +0.15 Ob) are dead by default.

This is the `.get(default)`-on-a-key-nobody-sets shape in its purest form: no error, no log, correct
types, wrong behaviour forever.

### D7 · MEDIUM — a canon one-season penalty is applied permanently

`parliamentary_vote.py:216` applies the Total-Victory Mandate penalty and its own note defers
restoration to `season_manager`. `season_manager.py` contains no restoration logic. The parliamentary
spine runs every season by default, so the penalty compounds: five total-victory losses is −5.0 L
permanently where canon intends a rolling −1.

### D8 · MEDIUM — the rupture return value reports effects it may not have delivered

`systems/fieldwork/sim/knots.py:361` sets `consequences['coherence_delta']` **before** the `try` at
`:362`, whose `except (ImportError, AttributeError)` at `:366` swallows. Both callees
(`systems/threadwork/sim/coherence.py:138`, `systems/characters/sim/conviction.py:167`) **exist and
define the imported symbols**, so the `ImportError` leg is dead — the only thing the net can still
catch is a genuine `AttributeError` bug inside the callee. When it does, the returned dict states a
coherence loss that never happened. Same shape at `:353` and `opposing.py:248`.

### D9 · MEDIUM — `random` is an unbound name in two collision resolvers

`systems/mass_battle/sim/units.py:299` calls `random.randint(1,10)`; the module never imports
`random`. The same latent `NameError` exists in the canon engine at
`tests/sim/mass_battle/hierarchy/units.py:2105`. Both sites are unreachable today
(`resolve_internal_collisions` has no callers), which is why it has survived — Pass-2n wires it.

### D10 · MEDIUM — two gates that cannot fail sit in the blocking bucket

`tools/ci_supersession_check.py:66` and `tools/ci_audit_registry_check.py:74` return 0 on every path;
both docstrings say they never block. They are listed under "Every blocking validator". A gate that
cannot fail is a comment, and its presence in that job asserts a property it structurally lacks.

---

## 3. The vocabulary divergences

### 3.1 Degree of success — 16 producers, 6 vocabularies, 5 Overwhelming formulas

The prior report's nine were an undercount. Beyond them: `mass_seizure.py:264`,
`collective.py:166`, `knots.py:226` (all inline additive `ob+3`), `echo_transport.py:187`,
`parliamentary_bridge.py:100`, `scene_dispatch.py:260` and `:334`, and the canon MB ladder at
`tests/sim/mass_battle/resolution.py:89`.

Vocabularies: `Degree` enum (**values lowercase**) · Capitalised strings · lowercase strings with
`'fail'` not `'failure'` · int 0–3 · `'Meets'/'Partial'/'Failure'` · Key-payload outcome tokens.

Overwhelming is computed five incompatible ways: `2·ob ∧ ≥3` (canon) · additive `ob+3` (threadwork,
mass_seizure, collective, knots) · pool-aware σ bar · size-percentage thresholds · flat `≥3` with no
ob. At ob=1 net=3 canon says Overwhelming and threadwork says otherwise; at ob=5 they invert.

**The canon ladder has no direct test pin** — `degree_from_net` and `Degree.*` appear in the test
trees exactly once, in a comment. The most-pinned is `sigma_leverage.degree`, with a 1,758-row golden
table. The cheapest ladder to change is the canonical one, which is the inverse of what anyone would
assume when planning a consolidation.

**Two epsilon twins.** `tests/sim/mass_battle/resolution.py:86` carries `_DEGREE_EPS = 1e-9` with a
long ED-MB-0051 justification (a 1-ulp error erasing an exchange). Its `systems/` twin at
`massbattle.py:640` has no epsilon. The twin's outputs are dead (`a_deg`/`b_deg` at `:951`, `:1517`
are assigned and never read; `DAMAGE_BY_DEGREE` at `:646` has zero readers, and the comments say
"narrative degree label only") — so the defect is inert, not absent.

**Silent consumers.** `domain_echo.py:89` `.get(degree)` → `fires=False` + a note nobody greps.
`echo_transport.py:425` `.get(degree, "compromise")` → a won fight logs as a compromise. Worst:
`wrapper.py:329`, whose `else` arm means **any unrecognised label is treated as `overwhelming`** —
the divergence fails *upward*.

### 3.2 The `net` parameter still carries four meanings — but one was misattributed

The prior report's table stands, with a correction: at `massbattle.py:951` and `:1517` the `net`
argument is a plain raw roll; it is the **`ob`** argument that is non-canonical (`max(1, opponent_net)`).
The divergence is real and lives in the other parameter.

### 3.3 Identity — seven faction dialects and no normaliser

`rg` for `.lower()/.upper()/.title()/.strip()` applied to an entity identity returns **zero hits** in
both design trees. All identity equality is raw case-sensitive `str` comparison.

Dialects: Titlecase name · `Faction` object · **lowercase keys in the contest package**
(`dictionaries.py:404`) · `'RM'`/`'Restoration'`/`"restoration"` (three spellings, no resolver) ·
`'A'`/`'B'` side letters in the same `Unit.faction` field · a **second class named `Faction`**
(`contest/faction.py:12`) · phantom names in no registry (`'Schoenland'`, `'Uncontrolled'`).

`FACTION_BOOSTS` and `world.factions` have **zero key overlap**. Nothing crosses that boundary today.

The faction roster is duplicated as a literal in at least four places beyond its owner
(`mc_v18.py:323`, `npe.py:245`, `npe.py:298`, `temperaments.py:72`).

### 3.4 `'Mandate'`/`'Stability'` versus `MULTS` codes

`domain_echo.py:197` emits `affected_stat` as canon display names. The write path
(`echo_transport.py:435`) guards with `_stat in MULTS`, whose keys are `L/Sta/W/I/Mil` — so a
`'Mandate'` delta would be **silently dropped**. `compute_thread_echo` has no callers today; the day
§5.6 echoes are wired through the standard apply shape, every row becomes a no-op, invisibly.

### 3.5 Treaty registry — tuple or frozenset?

`treaty.py:150` keys by `tuple(sorted(parties))`. `game_state.py:187` declares `frozenset`, and
`restore_world` (`:382`) mints frozenset keys. The two hash differently, so a save → load → register →
save → load cycle produces two records for the same parties and then **silently collapses them,
last-wins**. No keyed lookup exists yet, which is the only reason it is invisible.

### 3.6 `tools/` — the gates disagree about what the repo contains

23 tree-walkers, **no two with the same exclusion set**. The two most authoritative disagree
maximally: `broken_dependency_checker.py:23` excludes only `.git` (so a reference into `deprecated/`
grades LIVE), while `validate_ed_citations` refuses `deprecated/` for scanning yet loads
`deprecated/archives/editorial*` as its ED universe.

`tools/pathres.py:122` declares itself sole parser of the restructure ledger and **has no automated
caller at all** — the owner is the only unreached implementation, while the two blocking parsers
disagree with it on chain depth and FORK handling. Its `TREES` roster has 19 entries; the blocking
`ci_claude_workflow_paths.py:65` has 17, missing `dashboard` and `research`.

`ci_register_size_check.py:70` caps `propagation_map.md` at 15,000 while
`atomization_rules.yaml:169` — the policy file the repo single-sourced this from — says 10,000. Two
gates, one file, two verdicts.

`validate_ed_citations` is **CI-only**: local-green does not include the anti-fabrication gate.

---

## 4. What is *not* wrong

Stated because a divergence audit that reports only divergence is not a measurement.

- **Territory ids** — one dialect, `'T1'…'T17'`, zero drift anywhere.
- **Faction stats** `L/Sta/W/I/Mil` — every live write routes through the clamped `adjust()`. A grep
  for bare assignment finds exactly one hit, on a different class.
- **Contest `Standing`/`Reserve` primitives** (`contest/primitives.py:31`) — fully clamped, no
  bypass. This is the model the rest of the repo should compose on.
- **Combat initiative/poise** — every write routes through a named clamp. The cleanest regime in the corpus.
- **The morale write-sweep guard** is live and works; its `_CELL_OWNED` registry is field-parameterized.
- **No numpy/stdlib RNG mixing** in any live module; the de-leak held.
- **No unfixed hash-order RNG dependence** — the 2026-05-20 fixes are in place with comments as artifacts.
- **Solmund/Galbados** — zero occurrences of the deprecated name in any `.py`.
- **`git` blob-SHA computation** genuinely lives once (`freshness_gate.py:41`).
- **No dataclass-as-dict-key equality bugs** beyond two deliberate, documented `eq=False` classes.

---

## 5. Divergence that is deliberate

Not defects; listed so a sweep does not "fix" them.

- `contest/resolver.py:137,142,315` — module-stream RNG, documented, load-bearing on 151 seeded tests.
- `tests/sim/mass_battle/` global-stream design — the canon engine's documented choice (J2).
- `combat_bridge.py:140` / `scene_dispatch.py:295` — derived child streams and reseed-with-restore.
  **This is the pattern the rest should converge on.**
- `Subunit`/`Unit` `eq=False` — identity semantics are load-bearing for the target-atom cycle.
- `stubwire.stub_resolve` — 40 sites, typed, counted, ratcheted. The *new* convention; the
  `except (ImportError, AttributeError)` swallows are the old one that the sweep missed (D8).

---

## 6. Parameter sourcing

Lens 9 returned last, and **independently re-derived D1** — it found the TN-blind roller from the
constants side, without knowing the dice lens had found it from the roll side. Two lenses converging
on one defect by different routes is the strongest corroboration this method produces.

### D11 · HIGH — the typed export publishes a superseded model as truth

`tools/export_sim_params.py:36` lists `"systems/combat/sim"` in `SCAN_DIRS`. That module is the
**superseded** v30 dice-pool combat model — `references/module_contracts.yaml:1054` says so
explicitly ("MODEL CORRECTION: resolver is d_sigma … NOT the v30 dice_pool model"). So
`engine/engine_params/sim_params.json` publishes `combat.COMBAT_POOL_HISTORY_CONSTANT` (`:607`) and
`combat.WEAPON_TN_BASE` (`:723`) as typed, generated-from-code values.

They sit in the **same directory** as the canonical `combat_engine_v1.json`, both claiming
generated-from-code authority, with nothing marking which is superseded. One says the combat pool
constant is 3 (`Agi×2 + History + 3`); the other says the pool is `History + 6` floored at 5.

Worse, this is not purely a documentation problem: `engine/mc_v18.py:71` defaults
`DISPATCH_COMBAT_BRIDGE` **off**, so the campaign driver still resolves combat through the superseded
module. The stale export describes what actually runs.

### D12 · MEDIUM — `MULTS` is duplicated as seven private literals

Owner: `game_state.py:42`. Five modules import it correctly. Four keep private copies —
`crown_initiative.py:32,33,34`, `council_solmund.py:24`, `excommunication.py:35`,
`absolution.py:26,27` — and `crown_initiative.py:34`'s comment **cites `game_state.py MULTS` as its
source while re-typing the number**.

Change `MULTS['L']` from 20 to 25 and the importers stay correct while excommunication's canonical
"−1 L" silently becomes −0.8 stat-tiers, applied through the same setter. That is the
read/write-asymmetry hazard in granular form.

### The model case, and it is the repo's own

`tests/valoria/test_combat_invariants.py:298` `test_percussion_anchor_has_one_owner` asserts
`core.PERC_AUTH_REF is WP.PERC_CAP` — **identity, not equality** — plus a value check on the
deliberately-unbound config copy. One owner, bound imports, a guard that fails on recurrence. The
`key_types` pipeline (authored markdown → `export_key_types.py` → JSON → runtime read, identity-pinned
by a blocking gate) is the same shape at the file level. Both already exist here; the fixes below are
mostly a matter of extending a pattern the repo has already proved.

### Other parameter divergences

- **Per-die EV table copied six ways** — `dice_engine.py:58` (owner), `sigma_leverage.py:73` PER_DIE
  ("copied verbatim"), `:100`/`:101` MU/SD_PER_DIE (one row again), plus a function-local `_SIG` in
  the canon MB engine. `sigma_leverage` imports `dice_engine` and still re-declares the table.
- **TN = 7 spelled ~15 times.** `sigma_leverage.py:79` is the nominal owner but sits *downstream* of
  `dice_engine`, so the root primitive cannot import it and hardcodes 7 three times.
- **Mass-battle fork already diverged**: `BATTLEFIELD_SIZE` is **25** in
  `systems/mass_battle/sim/massbattle.py:54` and **51** in `tests/sim/mass_battle/config.py:16`,
  whose comment says "config.py is leading canon". A factor-of-two battlefield. Every other shared
  constant in that pair is one retune away from silent divergence; the full pair-diff is unswept.
- **`conviction.py:42`** — the comment says "Canonical 13-Conviction set per PP-684"; the tuple lists
  **nine**. The code implements the set the comment calls superseded.
- **Uncited mechanical literals** concentrated in `combat_engine_v1/geometry.py:33,34` and elsewhere:
  they participate in every weapon's baked coefficients, are named nowhere, cited nowhere, and
  exported nowhere.
- **The export gap is one-directional.** `test_combat_invariants.py:512` guards against *dead* keys.
  Nothing guards against a **live tunable that reaches no export** — and ~60 do, including several
  canonical per derived_stats_v30 §4.1 / PP-717. Per the ED-1050 failure class, those are exactly the
  numbers a port hand-transcribes.

### Cleared as coincidence

Stated because a duplication sweep that flags every equal number is worthless: `6.5`, `0.75`, `1.5`,
`8.0`, `0.85`, `0.30` were each chased to their definitions and rejected as unrelated anchors. The
tribunal Persuasion-Track `6` vs `7` was chased to canon and cleared — they model two *different*
proceedings (standard §7 vs Excommunication §7.1), each citing its own section correctly.

---

## 7. Falsifiers

Per §0.1 point 3, each headline claim carries the check that would show it wrong. None were run.

| Claim | Command | Refuted if |
|---|---|---|
| D1 TN-blind | `python -c "import random;from engine.autoload import dice_engine as D;r=random.Random(0);print(sum(D.roll_pool(1,tn=8,rng=r).net for _ in range(200000))/200000)"` | ≈0.30 (canon) rather than ≈0.40 |
| D2 dead clock | `rg -n "Turmoil" systems/ engine/` | any writer appears |
| D3 accord units | `python -c "from engine.substrate.canon_buckets import canonical_accord as c;print(c(2.0),c(3.0))"` | prints `2 3` |
| D4 dead gate | edit a params-bearing `systems/*_v30.md` alone | the gate fires |
| D5 Muster cost | `python -c "from engine.autoload.game_state import Faction;f=Faction('X',W=4.0);f.adjust('W',-1);print(f.W)"` | prints 3.0 |
| D6 dead defaults | `rg -n "pc_incapacitated" systems/ engine/` | a producer appears |
| D8 lying dict | monkeypatch `apply_coherence_delta` to raise `AttributeError`; call `apply_knot_loss(mode='rupture')` | the dict omits `coherence_delta` |
| D9 NameError | `python -c "import systems.mass_battle.sim.units as u;print('random' in vars(u))"` | prints `True` |
| all locations | `python audit/2026-08-11-divergence-audit/verify_locations.py` | any row is not `OK` |

---

## 8. Disposition

All PROPOSED. None executed. Ordering and file-by-file detail: `02_remediation_plan.md`.

The one ordering claim worth stating here: **fix the calling conventions and the units before the
vocabularies.** Folding return types while four input conventions and two unit scales remain in place
converts a visible divergence into an invisible one.
