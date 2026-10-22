# Reference appendices A1–A8 (first-draft syntheses, uncorrected text)

**Status: superseded where the tutorials (02–11) or the errata (13) differ.** These were written before the two audit rounds. Known errors in them
are listed in `2026-10-22-system-description-13-errata-and-audit-record.md` (ERRATA and audit findings A–F). Use them as a map of sources and for detail the tutorials omit, not as the
last word. Notably wrong or stale in them: grade conventions differ between appendices; the scene-budget "dispute"; `write_matrix` has 40 rows; scar is written at RESOLVE;
lexicon "conflicts" that the verbs roster already settles; Faction roster of FA; several run counts (use `ctl/`).

# APPENDICES (Stage-2 syntheses, verbatim)


<!-- ===== A1 (S1_engine_core.md) ===== -->

# A1 · S1 — Engine core: resolution engine, season loop, harness and measured state

HEAD `a4ca9a5`. Sources: extracts C01, C02, C03, C13, D01, D06 (read in full), D02 (skimmed for RB-0..RB-3). Cites: `[C02 §4.5]` = extract
section; `path:line` = repo file (opened by the extractor unless listed in §7 checks). Grades: RUNS-IN-LOOP / TESTS-ONLY / DESIGN-ONLY.

## 0 Engine map (whole-repo layering on the live path)

| tree | what it is | on the live path? | cite |
|---|---|---|---|
| `engine/dice_engine/` | three files: `dice_engine.py` (d10 face rule, `roll_pool`, `continuous_engine_sample`, `degree_from_net`), `sigma_leverage.py` (advantage as a μ-shift), `__init__`. "Root primitive", stdlib only, reads no JSON/YAML; "not 'the engine' (that is the season loop)" | yes, through `seam/ladder.py` and `modules/` | [C01 §2, §5] |
| `engine/substrate/` | leaf readers: `composition.py` (role → module by string, from `composition.json`), `descriptors.py`, `names.py`, `pc_engine.py` ("THE ONE PATH SEAM into modules/combat/"), `stubwire.py` (counts not-built calls) | yes (composition resolves every contest provider) | [C01 §5] |
| `engine/engine_params/` | GENERATED typed exports (`composition.json`, `descriptors.json`, `names.json`, `sim_params.json` 277 params, `game_constants.json`, `combat_engine_v1.json`); `params_tables.yaml` frozen reference holding PRE-RULING degree bands | only `composition/descriptors/names.json` are read at runtime; no `engine/` reader of `sim_params`/`game_constants` found | [C01 §5, §7] |
| `engine/reference/` | frozen instruments: `contest-groundup/engine.py` (pre-ruling oracle, regenerates the σ-parity golden), `degree-sweep/` probes | TESTS-ONLY | [C01 §5] |
| `engine/season/` | **the game code (Layer 2)**: `state/` (World store + write gate), `loop/` (driver + seven steps), `decision/` (chooser; not in this scope), `queries/`, `data/` (loaders for `verb_table.yaml`, `rosters.yaml`, `write_matrix.yaml`, fixtures), `seam/` (degree dispatch + wrappers to subsystems), `manifest/`, `epistemic.py`, `harness/`, `tests/` (113 files) | yes — this is the loop | [C02 §2; C03 §2; C13 §1] |
| `modules/` | `combat/`, `fieldwork/`, `mass_battle/`, `social_contest/`: the subsystem implementations the season reaches. `composition.json` roles: `combat.fight → modules.combat.fight:fight`, `fieldwork.find`, `mass_battle.resolve_field`, `social_contest.roll` | yes, only when a contested/graded verb fires | [C01 §5]; CHECKED composition roles |
| `systems/` | design source for combat/social_contest/mass_battle plus oracle scripts `systems/<sub>/sim/` (threadwork `opposing/collective/operations`, fieldwork `knots`, old social-contest kernel, combat sim). Holds no `.md` | no; callers of the dice engine here are TESTS-ONLY oracles | [C01 §6]; CLAUDE.md §3 |

- Live call chain: harness (`headless`/`populated`/`soak`) → `SeasonDriver.season` (`engine/season/loop/driver.py:370`) → seven steps → for a contested verb `resolve._contest` → `seam.contest()` → manifest provider → `composition.require(role)` → `modules/<sub>` → result dict → `seam/ladder.py::degree_of` → `degree_from_net` or a module-specific band [C02 §4.6, §6; C01 §6].
- `engine/` names no subsystem by import; seams resolve by string [C01 §6]. `modules/mass_battle` takes no `engine.*` dependency "ON PURPOSE" and spells its own ladder (`modules/mass_battle/resolution.py:105-112`, CHECKED).
- No campaign driver exists at HEAD: `ls engine` gives `dice_engine engine_params reference season substrate tests` [C01 §6]; `m1_acceptance` says the old campaign-driver tree "was superseded (engine/season is the head, Jordan 2026-09-07)" [C13 §4d]. CLAUDE.md §3 still lists a "campaign driver" in `engine/` and does not name `modules/` (stale map).
- `engine/autoload/dice_engine.py`, cited by CLAUDE.md §5, does not exist; the real path is `engine/dice_engine/dice_engine.py` [C01 §6].

---

## 1 RESOLUTION ENGINE — one d10 pool, one margin ladder, advantage as a mean shift; RUNS-IN-LOOP (social-contest path), with two rival rollers

### 1.1 What it is
A dice-pool resolver: a person's pool of d10s (or a Gaussian stand-in for it) produces a signed net, compared against an obstacle (Ob) to
give one of four degrees — Failure, Partial, Success, Overwhelming. Advantage never lowers the obstacle and never changes the target
number; it adds a bounded boost to the roll's mean, scaled to the pool's spread so that "a moderate edge" means the same thing at pool 2 and
pool 20. The player-facing promise is legible, graded, recoverable odds at every scale ("THE degree ladder. Single owner for every scale
of the game", `dice_engine.py:229`) [C01 §2].

### 1.2 Operating alone
**Face rule** (`_die_result`, `dice_engine.py:153-161`): face 1 → −1; 2–6 → 0; 7–9 → +1; 10 → +2; "No chain." Per die μ = 0.40, σ = 0.800
(`:174-175`). **TN is always 7**: `_require_tn7` raises on any other value (`:182-193`; ruling ED-IN-0196 "TN7 always. Never change TN
anywhere ever."); "A varying difficulty is an Ob, not a TN" (`:178-179`) [C01 §4.1].

Three roll paths share the ladder [C01 §4.1]:
| path | function | pool handling | output |
|---|---|---|---|
| A discrete | `roll_pool(pool_size, tn=7, ob=None, rng)` (`:196-206`) | `max(1, pool_size)`, int only | per-die sum; degree if `ob` given |
| B continuous | `continuous_engine_sample(pool)` (`:209-224`) | fractional; `pool<=0` → 0.0; no floor inside | `gauss(0.40·pool, 0.800·√pool)` |
| C wrappers | `roll_net` (`sigma_leverage.py:286-296`): `max(1, int(round(pool)))` (banker's rounding); `roll_net_continuous` (`:299-332`): `max(1.0, float(pool))` | two flooring conventions coexist | net |

**σ-leverage** (`sigma_leverage.py`) [C01 §4.2]: `soft_cap(x) = 1.5·tanh(x/1.5)` (`M_MAX = 1.5`); `net_boost(net_sigma, pool) =
soft_cap(net_sigma)·0.800·√max(1,pool)` — "shifts the outcome's z by exactly eff_sigma at every pool size". Modifier levels `LEVEL_SIGMA`:
minor 0.25, moderate 0.50, strong 0.75, major 1.00, labelled "Class B draft sim-seeds — sim-tunable, NOT canonical" (`:95-102`).
`levels_to_net_sigma(aggressor, defender)` sums one side minus the other. `p_success` is a closed-form P(net ≥ base_Ob) helper, not a
roll. `eff_ob` is "DISPLAY ONLY (not the resolution value)" (`:170`).

**The ladder** (`degree_from_net(net, ob, extension=None)`, `dice_engine.py:286-301`, CHECKED), margin = net − ob:
| band | margin | note |
|---|---|---|
| Failure | < 0 | |
| Partial | [0, 1) | "near-miss-by-nothing"; old Partial `0 < net < Ob` retired (`:281-284`) |
| Success | [1, 3) | or ≥ 3 vetoed by an extension |
| Overwhelming | ≥ 3 | flat, not Ob-scaled; `net ≥ 2·Ob`, PP-232 floor and Ob-20 exception "RULED OUT" (`:270-274`) |
Operands may be fractional; no epsilon. Consequence accepted by Jordan 2026-08-27: a pool-2 contest cannot reach Overwhelming [C01 §4.4].
**Extension seam** (ED-SC-0032, `BandExtension`): may only demote Overwhelming → Success; its own docstring retracts any sandbox claim
(`:77-87`). The only extension, `PoolDesaturation` (`OVERWHELM_SIGMA = 0.85`), lives in the old contest kernel [C01 §4.5].

**Obstacle**: the dice engine owns no Ob derivation. Ob is "RULED to become fractional" ("score/2 plus whatever specific modifiers"), but
"there is NO SINGLE-OWNER derivation … Reconciling them is a systems ruling … SUSPENDED by Jordan (2026-08-21)" (`dice_engine.py:241-254`,
ED-IN-0202). Live derivations: combat `ob_from_defender = defender.history / 2.0`; social contest `opposition/2` else `obstacle_default`,
reduced by `reception_gain·reception + proof_step·proofs` (floored at `OB_MIN = 1`), plus `forgery_quality`, capped by a ceiling
(`modules/social_contest/roll.py:~100-116`) [C01 §4.3].

One roll, composed (social path, `roll.py:124`): `net = roll_net(pool) + net_boost(leverage, pool)`; `Margin(net, ob=obstacle(inp))`; the
season's `degree_of` labels it. Combat (`modules/combat/core.py:126`, CHECKED): `net = roll_net(pool, rng) + soft_cap(net_sigma)·sigma_n(pool)`
via the continuous path, `degree(net, ob)`, relabelled lower-case [C01 §4.6].

### 1.3 In the whole game
- **Who invokes it.** Seven verbs declare `contests:` (CHECKED by import): `argue`, `determine` (prize *a proposition*), `speak` (*a matter*),
  `tell` (*a standing*) → `social_contest.roll`; `fight`, `accept` (*the body*) → `combat.fight` (`d_sigma` resolver, resolved inside
  RESOLVE); `march` (*a field*) → `mass_battle.resolve_field`, deferred to ENCOUNTER with band `Declared`. Graded inquiries
  (`graded_inquiries` routing row, FI-01; three of six inquiry verbs graded) roll through `social_contest.roll` with no prize [C02 §4.6;
  `rosters.yaml:1107-1140`].
- **Degree dispatch** (`engine/season/seam/ladder.py::degree_of`, `:218-259`): result with `wound_state` → `combat_degree` (roster bands
  `Felled/Wounded/Untouched`, not the margin ladder; Jordan 2026-09-03 "kill/wound degrees should be directly taken from scene combat");
  `attacker_wins` → `field_degree` (`UNOPPOSED/WON/LOST`); `{net, ob}` → `degree_from_net` with **no extension**; else `Unspecified` [C01 §4.7].
- **What reads the degree.** `_fold` selects `row.writes_at(degree)` and `row.emits_at(degree)`; the effect receives the `Resolution`; the
  Event carries `degree`, read by WITNESS (`_told_value` distorts told content only at Partial) and ENCOUNTER (`Declared`) [C02 §4.6].
- **Rolls are seeded**: `draw_factory(world_seed, tick)(actor, f"roll:{prize}:{act.id}")` (`resolve.py:792`) — same seed, same roll [C02 §4.6].
- **Rival rollers.** `modules/mass_battle/resolution.py` has its own `roll_pool`, `roll_pool_fractional`, `_sigma_net_boost` (local
  `_SIG_PER_DIE = 0.800`) and `compute_degree`, "Spelled out here rather than imported ON PURPOSE … Equivalence is held by a guard"
  (`tests/valoria/test_degree_ladder_single_owner.py`) [C01 §6; CHECKED `:105-112`]. Third copy: the frozen `contest-groundup` oracle
  with `OB_MAX = 20` and the pre-ruling `degree()` [C01 §5]. `systems/*/sim` oracles call `roll_pool`/`degree_from_net` directly.

### 1.4 Built vs designed
| element | grade | evidence | what proposals say should exist and does not |
|---|---|---|---|
| `degree_from_net` ladder | RUNS-IN-LOOP | driver → `resolve._contest/_grade:825,:856` → `degree_of` → `ladder.py:251` [C01 §6] | — |
| `roll_net` + `net_boost` (social) | RUNS-IN-LOOP | `social_contest.roll` via `seam/wrappers/sigma.py` [C01 §6] | — |
| continuous path (`roll_net_continuous`, `continuous_engine_sample`) | RUNS-IN-LOOP (inferred) | `modules/combat/core.py:126`; R-05 says `kill / wound` (now `fight`) is "the FIRST CONTESTED VERB EVER TO EXECUTE FROM A SEASON" [C13 §5]; fight's call into `core` not traced [C01 §6] | IN-46 grid-mode suspension (PLAYABLE fight) — DESIGN-ONLY (REM-31) [D02 §4.0] |
| combat `end` per person | RUNS-IN-LOOP, thin | `Combatant(a_id, end=a_end)` takes `end` from body band alone [D01 §2.1 #15] | per-person capacity (J-13/JQ-2; B6 `Person.attributes`) DESIGN-ONLY [D01 §6.2; D06 §4.3] |
| mass-battle roller | TESTS-ONLY in practice | wired via ENCOUNTER; `field.won/lost/army.arrived` emitted 0 times in both shipped worlds [D02 §4.0 REM-27]; season force is one Unit at `_SEASON_FORCE_POWER = 4`, `command = 4`, "routs on contact regardless of who wins" [D01 §2.1 #15] | weight→troop conversion (REM-32), order of battle, officers (V2) DESIGN-ONLY [D02; D06 §4.10] |
| `BandExtension` / `PoolDesaturation` | TESTS-ONLY | used by old kernel `resolver.py:308`; not passed on the season path [C01 §4.5] | — |
| `p_success`, `eff_ob`, `LEVEL_SIGMA` levels | TESTS-ONLY | parity tests `engine/tests/test_sigma_leverage_parity.py` [C01 §8]; no season caller found | — |
| single Ob derivation, fractional Ob | DESIGN-ONLY | "SUSPENDED by Jordan (2026-08-21)" [C01 §4.3] | — |
| per-die literals single-owned | DESIGN-ONLY | 0.40/0.800 duplicated in `sigma_leverage.py:78,:112-113` | REM-42 aliases them to `dice_engine.py:174-175` [D02 §4.0] |

### 1.5 Structural handles
Resolution style: dice pool, success-counting d10 with a negative face (1 = −1) and an exploding-value face (10 = +2) but no reroll chain;
fixed TN, variable obstacle; Gaussian surrogate for large/fractional pools. Advantage model: additive mean shift in σ units, tanh soft cap
at 1.5σ (no hard ceiling). Output: four ordered degrees on a flat margin ladder (0/1/3), the same at every pool size. Granularity: one roll
per contested act (social), many per fight inside the combat module, one per field. Agency: the engine rolls; nobody chooses dice. Information:
odds computable in closed form (`p_success`), not shown to anyone in code. Failure/recovery: Partial is a near-miss band, effects are
keyed per band, `Failure: []` lawful. Determinism: per-act keyed RNG from `world_seed`.

### 1.6 Open decisions named
ED-IN-0202 (single Ob owner, fractional Ob; SUSPENDED); ED-IN-0196 (TN 7, RULED); ED-SC-0032 (extension seam); J-13 remainder / JQ-2
(does "pool only" reach combat and mass battle); J-T1/J-T2/J-T4 (attribute source, the tenth attribute, do attributes change) [D06 §4.3];
JQ-4 (weight→troop value); D-V5 (R-7: `field_degree` collapses retreat into Lost) [D06 §4.10]; DEC-5 non-monotone P(Partial+) declined [D01 §6.5].

### 1.7 Conflicts, uncertainties, checks
See §3.7 items 5, 6, 8, 9 and the checks list (ladder, combat roll, mass-battle ladder, prize routing).

---

## 2 THE SEASON LOOP — a seven-step, four-barrier simultaneous-turn simulation over one gated store; RUNS-IN-LOOP

### 2.1 What it is
The game's clock and referee. One `season()` call advances the world one tick (one season). Every person — named NPC or cohort — decides
from what they know, all decisions resolve in one canonical order, consequences are written only through a gate that checks who may write
what and when, and what happened is then deposited as claims into the memories of whoever could perceive it. There is no GM and no
player-special path: `choose` is a callback per person [C02 §4.1, §4.4]. The fantasy served is a living world whose drama comes from
many partially-informed agents acting at once.

### 2.2 Operating alone
**State — the World** (`state/world.py:187-277`) [C03 §3.1]: collections `persons, rungs, offices, sites, records, propositions, dates`,
the positional `docket`, the `tenures` view, the append-only `log` (Events) and `acts` (ActStore); `tick` (season clock), `draw`,
`fixtures`, `step`, `frozen`. **No Faction or Settlement class**: factions are `Proposition`s (`fac_crown`) plus `faction_sheet` Records;
settlements, hearths and realms are `Rung`s [C03 §3.1].
**Carriers** ("the sixteen things", `state/carriers.py`) [C03 §3.2]:
| carrier | essence |
|---|---|
| `Person` | one class for individuals and cohorts ("A COHORT IS A PERSON AT weight > 1"); `capability` (dice), `stance`, `pursuits`, `ledger` (claims), `body` (0–1000), `born`, `scar`, `conviction` (0–5), `travel_leg`, `tenures` |
| `Rung` | "THE HOLON. Eight kinds, ONE type": person, hearth, community, settlement, territory, province, duchy, realm; owns `stores`, `yield`, `envelope`; "a Rung owns NO social aggregate … EVERY ONE IS A QUERY" |
| `Tenure` | "THE ONE EDGE", owned by its subject: kinds `knot, hold, commit, tie, ban, oblige, contain, reside, succeed, detain`; optional `Term(matures_at, declared_by)` |
| `Office` | a seat (`SeatId`): `remit_acts ⊆ {confer, dispatch, issue, convene, revoke, determine}`, conferral `appointed/elected/annex`, revocation basis |
| `Site` | physical place with fixed-point `condition` that gates verbs |
| `Record` | document of six kinds (`text, dispensation, petition, works, faction_sheet, cover`), `forgery_quality`, `stages`, `matured` |
| `Proposition` | immutable utterance ("Fixed at utterance, never destroyed") |
| `Claim` | a belief entry in the holder's own ledger: `subject, predicate, value, confidence, source, visibility, chain` (who told whom) |
| `Event` | `kind, changes, causes` (never empty; `ROOT` sentinel), `degree`, `observed`; no actor/subject field |
| `Act`, `Scene` | an intended act (`verb, payload, via` seat, `stratum`, `pool`, `obstacle`); a scene groups ≤ 3 acts, costs 1 (extended 2) |
| `View`, `Sensation`, `Question`, `Candidate` | what `choose` may see: ids only; `View.__getattr__` raises — "choose never receives a World. NOT BY DISCIPLINE -- BY TYPE" |

**The procedure** (`driver.py:370-528`; tokens and tick CHECKED `:447-515`) [C02 §4.1]:
| # | step | barrier / token | does |
|---|---|---|---|
| 0 | reset | — | `draw = 0`, round 0, season-local queues cleared |
| 1 | CALENDAR | 1 / CALENDAR | Dates with `due_at == tick` fire (`date.fired`); a held venue forms a docket item; a vacant one lapses [C02 §4.2] |
| 2 | MATTER | 2 / MATTER | once per season, in order: actorless events; Record term maturation; Tenure terms close (`tenure.closed`); claim confidence decays by `claim_decay_per_season = 5`; standing band crossings (emission only); subsistence draw and shortfall record; hunger body loss (`body_step`, shipped 0); ageing/illness (shipped 0.0); per-rung larder draws, Site yield into stores; travel ends; Site wear and downward band crossings. Ends `w.frozen = True` [C02 §4.3] |
| 3 | rounds | — | `rounds = scene_budget` (shipped 5) |
| 3a | DELIBERATE | none (a MAP) | per person: `sense()` → `Sensation(subsistence, standing)`; questions since last deliberation; `View` of ≤ `view_k = 12` claims; `choose(p, v, s, ask_budget)`; over-budget → `Forbidden`; > 3 acts/scene → `Ungraded`; already-realised opportunities dropped; release ≤ `scenes_per_round = 1` scene; unreleased scenes queue; re-ask `choose` only if a 7-term input fingerprint changed [C02 §4.4] |
| 3b | RESOLVE | 3 / ACTS | the fold, in one global order `(stratum, H(seed, tick, actor, …))`; strata `movement < binding_decision < contested_physical < uncontested_material < social`; sum-then-clamp-once for staged `Site.condition` deltas [C02 §4.5] |
| 3c | ENCOUNTER | shares 3 / ACTS | fights contests RESOLVE deferred (`Declared`), selected by the declaration Event [C02 §4.7] |
| 3d | WITNESS | 4 / INTERIOR | fans each Event to observers by channel; deposits claims into each holder's own ledger (event claim, observations, `seen`, document content, told content, findings); refraction; ledger cap 200 with eviction key `confidence·(recency+1)`; "NEVER TOUCHES A BELIEF" [C02 §4.9; C03 §4.10] |
| 4 | CENSUS | shares WITNESS join / MATTER | individuates a demanded person (`person.individuated`); "demand-driven only; generated nobody" otherwise [C02 §4.10] |
| 5 | `w.tick += 1` | — | the only tick advance (D-45) |
Return: `acts, events, rounds, deposits, hash` [C02 §4.1].

**The act lifecycle** [C02 §4.11]: `choose` returns Acts/Scenes (ids `H(seed, tick, actor, "act:<verb>:<key>")`, re-keyed `:r{n}` per round) →
DELIBERATE budgets, filters, releases → RESOLVE: store act; actor must exist (`act.ineligible`); obstacle > 2×pool refusal
(`attempt.refused`, never set by the computed chooser); contested/graded → `_admits` then `_contest`/`_grade`; else `_fold`.
`_fold`: `_admits` (eligibility `own | remit:<act> | hold[:<obj>] | presence:<rung>` — presence "unevaluable, declines"; typed `requires`
cell or one of 7 hand predicates; counterparty) → `writes_at(degree)` pairs → `EFFECTS[verb](w, a, resolution)` returns a described `Change`
→ `World.write(change=…)` → receipts → earned kinds ∩ `emits_at(degree)` → Events with `causes=[act, occasion ids]`. **Refusals emit, never
raise.** An effect that moves nothing is a refusal (F9 `NoOpReceipt`). Side writes: `_scar_witnesses` raises `scar[element]` in observers of
a value-violating act and may trigger a conviction crisis (threshold 3) [C02 §4.12; C03 §3.2]. Events append to the one log; WITNESS turns
them into claims; claims feed the next deliberation through `questions_for`; MATTER next season reads what acts wrote.

**The gate** — `World.write` (`state/world.py:847`, CHECKED) [C03 §4.1], in order: token must be this tick's; matrix row
`(kind, field)` must exist ("ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION"); current step must be in the row's steps; token's write class
must match; `social: true` rows only by `driver == "Act"`; `Person.coherence` only by `Seam`; `Tenure.until` by non-acts only on death or
term maturity; declared emissions only. Then, under a mint window: tenure snapshot → apply → **F3** every changed Tenure needs one of
twelve authorship bases (T-m owner, cascade, founding, T-n term, handover, renewal, determination, warrant, seizure, muster, T-o ban,
conferral) or the write is undone and raises `NotYours`; **F9** a `Change` that moves no named subject raises `NoOpReceipt`; receipts minted
by identity; Event logged with resolvable causes [C03 §4.3, §4.4; `state/log.py:61-103`].
**Tokens**: `Token(write_class, tick)`, constructed only by `mint_token` in the driver (`driver.py:80-98`, CHECKED), one per barrier;
DELIBERATE gets none; enforced by AST scan `test_g2_token.py`, which cannot see `dataclasses.replace`/`copy.copy` [C03 §4.2].
**Write matrix** (`write_matrix.yaml`, 41 rows + `retired:`) [C03 §5.2]: CALENDAR writes Dates/docket; MATTER (and CENSUS) writes
`Claim.confidence, Person.body/exists/travel_leg/weight, Record.matured/ttl, Rung.envelope/stores/yield, Site.condition, Tenure.until`;
RESOLVE/ENCOUNTER write all `social: true` rows (`stance, pursuits, capability, scar, conviction`, Office/Record/Rung/Site creation, Tenure
fields); WITNESS writes only `Person.claim_ledger`. Retired: `Person.marks, axis_count, beliefs`, `Rung.stake`, `Site.drawers`,
`Office.establishment`. Unproduced rows: `Person.coherence, conviction, scar`, `Rung.dates`.
**Content hash** (`world.py:1355`, CHECKED) [C03 §4.6]: blake2b-16 over the seven collections by sorted key, docket by position,
tenures by id, every Event (`id|kind|emitted_at|degree|causes` + changes + observed). Not hashed: `acts`, `tick`, `fixtures`, `draw`,
trace. Adding a dataclass field moves every hash ("structural hash move").
**Determinism**: every id and draw is `H = blake2b(v1|seed|tick|subject|purpose)` [C03 §3.3].

**Time model.** One tick = one season; seasons do not subdivide into calendar dates beyond `due_at` ticks. Within a season: 5 rounds
(`scene_budget`), each person releases ≤ 1 scene per round, so ≤ 5 scenes per person per season (Jordan 2026-09-02: "5 scenes for a
character to play per season"); a person whose `budget()` exceeds 5 (e.g. office-holder 6) cannot spend the excess [C02 §4.4, §7; C03
§3.2]. MATTER and CALENDAR run once per season by a stated "LAYER-1 CONSTRAINT"; the world refreezes per round; WITNESS runs per round, so
a later round's choices see an earlier round's claims (R-03) [C02 §4.1]. Year length = length of the `season_factor_draw` table, else a
constant `season_factor` (`queries/world_q.py:953-964`, CHECKED); `SEASONS_PER_YEAR 4` exists only as an exported constant with no engine
reader [C01 §5, §7].

### 2.3 In the whole game
Called by every harness (`headless`, `populated`, `soak`, `corpus_run`, `aperture`, `probes`, `storybar`, …) and tests; nothing outside
`engine/season/` and `engine/reference/` calls it [C02 §6]. Reads `verb_table.yaml` (53 rows at HEAD, CHECKED), `rosters.yaml`,
`write_matrix.yaml`, fixtures, manifest prize rows. Reaches subsystems only through `seam/` (§1.3). Feedback loops in code: acts → Events →
claims → questions → next choices (within a season by round, across seasons by tick); acts → stores/conditions/tenures → MATTER next
season; scar → conviction crisis → future choice; claim decay erodes memory 5 points per season. Inert loops at shipped values: hunger
death, ageing, illness (all 0) [C02 §4.3, §7].

### 2.4 Built vs designed
| element | grade | evidence | proposals say should exist |
|---|---|---|---|
| seven steps, four barriers, tokens, tick | RUNS-IN-LOOP | `driver.py:447-515` | — |
| gate F3/F9, write matrix, content hash | RUNS-IN-LOOP | [C03 §4] | invariant 5 (`writer:` column) and 7 (log refuses undeclared kinds) unbuilt; REM-41 builds 7 [D01 §2.1 #21] |
| refusal kinds `act.ineligible/act.refused/attempt.refused` | RUNS-IN-LOOP, undeclared | body literals declared in no YAML [D01 §2.1 #20] | REM-40: per-row declared refusal kinds [D02] |
| obstacle-refusal gate S27.4 | TESTS-ONLY | computed chooser never sets `Act.obstacle` (`resolve.py:986-990`) [C02 §4.5] | — |
| ENCOUNTER fields | TESTS-ONLY in practice | `field.*` = 0 in both worlds [D02 REM-27] | REM-27 `march` referent; IN-46 PLAYABLE suspension at ENCOUNTER (REM-31) |
| subsistence shortfall | RUNS-IN-LOOP, "recorded, not acted on" | `matter.py:476-491`; `body_step=0` | hunger Query `world_q.hunger`, `hunger_reach`, `body_step` 0→10 (REM-50..52) DESIGN-ONLY; JQ-6 [D01 §2.1 #17] |
| `Sensation.subsistence` | RUNS-IN-LOOP | `deliberate.py:525-537` | removal RULED (L1-6 option B), REM-44 unbuilt [D01 §6.1] |
| CENSUS individuation | RUNS-IN-LOOP (demand-driven) | `census.py:35-100` | — |
| `presence:` eligibility | DESIGN-ONLY | "unevaluable, declines" (H-33/H-75) [C02 §7] | — |
| claim-row sub-store (AX-3) | DESIGN-ONLY | "does not exist yet" [C03 §7] | — |
| refusal-clause tracing for predicates | DESIGN-ONLY | REM-14 [D02] | — |
| `Ineligible` gap class | dead | no callers (`gaps.py:102-104`) [C02 §3] | — |

### 2.5 Structural handles
Turn structure: simultaneous declaration, sequential resolution in a deterministic canonical order (stratum then hash), WeGo-like per round.
Scales: one loop for all scales; scale lives in Rung kind and in which subsystem a prize routes to. State model: entity–edge store
(entities + typed Tenure edges + immutable Propositions), event-sourced log with causal links, per-person belief ledgers; aggregates are
queries, never stored. Agency: every person through one `choose` callback; institutions cannot act ("NO INSTITUTION ACTS",
`deliberate.py:280-284`). Information: strictly local — claims by channel, confidence, refraction, decay, eviction; the chooser is type-barred
from the world. Failure model: refusals are first-class Events with causes. Content: authored data (verbs, rosters, cast YAML) +
generated consequences; no scripted plot. Pacing: fixed 5 rounds per season, fixed scene budgets; no real-time element.

### 2.6 Open decisions named
L1-6 (RULED option B, unbuilt); JQ-6 (what makes a settlement hungry); H-125 (`body_step`); H-87 / S39.3 (contest depth has no default);
H-92 (unspendable budget above 5); `[ASSUMPTION]` tags on F3 bases (`WARRANT_ACT = "dispatch"`, `SEIZURE_ACT = "issue"`, purview "one
edge deep", in-holdings faction clause) [C03 §4.3]; D-V5 (R-7 retreat) [D06 §4.10]; ED-IN-0279 (seventh step).

### 2.7 Conflicts, uncertainties, checks
See §3.7 items 1-3 and the checks list (driver tokens/tick, `World.write`, `content_hash`, year length).

---

## 3 HARNESS AND MEASURED STATE — the loop runs headless and deterministically; it is "NOT YET A GAME" (3 of 9 requirements met); TESTS-ONLY

### 3.1 What it is
`engine/season/harness/` is "what RUNS the model": world builders, single-case and multi-season runners, instruments and the acceptance
gate. Nothing in `loop/` depends on it [C13 §2, §6]. There is no player interface; a "play surface" is a callback that hands named persons
to a human function (`play_surface.py`) [C13 §3].

### 3.2 Operating alone — the instruments
| entry | what it does | cite |
|---|---|---|
| `headless --case NPC-088 --seasons 2 --seed 0` | one NPC (Carin Vedel, copyist) world, chooser narrowed to `resolvable_verbs()`; only case NPC-088 accepted | [C13 §3, §7] |
| `populated.build_realm(seed)` | the realm: 46 named NPCs, 37 settlements, cohorts | [C13 §3] |
| `governance_spine`, `scarce` | "TEST FIXTURE, NOT CANON" worlds (13 characterless seats; two settlements, one short larder) | [C13 §3] |
| `soak` | many seasons on one realm; grades flat per-season cost and stable act mix; all numerics required | [C13 §3] |
| `aperture` | per-verb funnel eligible→formed→offered→attempted→executed; `aperture 4 0` ~25 min; "pins nothing" | [C13 §3] |
| `corpus_run` | runs all NPC/ARC cases; R3 propagation rows, 'WHERE THE n GO', 'RANKING DISCRIMINATION' | [C13 §3] |
| `decision_spread`, `conviction_spread`, `storybar`, `loops`, `arms` | decision uniqueness by term; pursuit spread; cross-person antecedent share; cycle bounds; n-seed two-arm control (one mechanic) | [C13 §3] |
| `register --requirements` | validates `requirements.yaml` syntactically: status in set, a `measure:` that exists, a non-empty `measured:`; "It never reads what a `measured:` line says" | [C13 §3; D01 §2.1 #5] |
| `tools/m1_acceptance.py --summary` | four rows: stub calls, same-seed hash, nine requirements (DOC-DERIVED), invariant sweep; CI report-only | [C13 §2, §4d] |

### 3.3 The measured numbers
**Headless run** (re-run this session, identical to C13 §4a):
```
season 0: rounds=5 acts=16 events=17 deposits=50
season 1: rounds=5 acts=16 events=70 deposits=85
verbs the fold can execute: 47 of 53          CONTENT HASH: fc4d4cefd83c5cf2468883659bf7de58
```
"47 of 53" is `len(resolvable_verbs())` of `len(VERB_TABLE)` (`headless.py:170-171,198`, CHECKED): verbs with an evaluable precondition and
a carried effect — **not** verbs that execute. The six not resolvable: `construe, evade / defy, exchange, succeed, thread_read, tie / knot`.

**M1 gate** [C13 §4d]: stub invocations 0 PASS; same seed → same `World.content_hash()` `b71c1f2eb163…` PASS (seed 20260819, 1 season);
nine requirements 3/9 FAIL (DOC-DERIVED); invariant sweep 24 seeds × 4 seasons + 2 populated × 1, 8 invariants, 0 violations over 35,063
events, 19,725 claims, 2,059 tenures, 227 persons PASS. Verdict: NOT MET.

**THE NINE** (`engine/season/requirements.yaml`, ruled Jordan 2026-09-05, ED-IN-0204; re-run this session: met 3 · not_met 1 · partial 5):
| id | statement (verbatim, abridged) | status | measured basis / what blocks [C13 §5; D01 §4] |
|---|---|---|---|
| R-01 | decisions must propagate | met | R3 cross-person propagation ARC 97/97, NPC 46/46; may fall after RB-2 (K6) |
| R-02 | decisions affect subsequent decisions | met | degree-sweep `wd_collect` reading |
| R-03 | seasons tick scene-by-scene | met | headless run "prints and asserts nothing" + 5 `test_u2_` tests |
| R-04 | strategic and management actions at differing scales | partial | realm `aperture 2 0` att/ex: `requisition` 4/0, `confer` 0/0, `establish` 0/0, `revoke` 5/0, `convene` 3/0, `determine` 0/0; settlement verbs `restore` 0/27, `migrate` 1/118, `transfer` 1/47, `found` 0/24, `build` 0/19, `work` 0/82 — "no settlement-management verb executes" [D01 §2.1 #8-9] |
| R-05 | all verbs must be built out | not_met | executed set 21 → 17 → 16 [D01 §2.1 #10]; `work/found/build` wait on ED-IN-0297 |
| R-06 | characters with goals, ambitions, convictions | partial | sampler overrules a strict score top in 72 % of choices (198 of 276, seed 0); pursuit decides 28 %; 37 of 83 realm actors (cohorts) have no pursuit vector [D01 §2.1 #13-14] |
| R-07 | memories, feelings, relationships, imperfect knowledge | partial | "`choose` receives no World (enforced by test)"; conjunct 3 needs a `Won`/`Lost` field (none occurs) |
| R-08 | not omniscient, not perfectly rational | partial | "NON-RATIONALITY DOES NOT EXIST" in the stored text (deterministic top choice) — but see §3.7 conflict 4 |
| R-09 | chains within a scene probabilistic | partial | "A ROLL EXISTS AND IT REACHES THE GAME"; graded social acts write nothing on most bands; headless world seats no `capability` |

Other measured facts [D01 §2.1]: 1,102 refusal events over 2 seasons (realm 984, spine 118), 52.9 % on a wrong-kind referent
(`exists:<Kind> = 0`); 47 declared event kinds never emitted; character-change fixtures ship at zero (`scar_weight_shift = 0`,
`confliction_weight = 0`, `age_step`, `illness_rate`) — "character change ships dark"; realm food cover 21.7 → 41.7 seasons after seasons
0 and 1, so hunger binds only before the first yield. Realm 2-season baseline hash `89bc9c0ac2a0` at `b70b5af` (not re-checked at HEAD).
Verbs that "barely run": `requisition` 0, `revoke` 0, `work` 0, `transfer` rare, `migrate` 0 [D06 §2 #17].

### 3.4 In the whole game
The harness is the only driver of the loop (no Godot front end in this repo; Godot engine version unresolved per CLAUDE.md). CI job
`season-tests` runs `engine/season/tests` and `register --requirements` (`valoria-ci.yml:357,:413`); `m1_acceptance --summary` runs
report-only (`:237`) [C13 §6]. The 40-item v9 remediation proposal (RB-0..RB-5) is PROPOSED, "paper", and states "Even fully executed, this
plan cannot make THE NINE `met`" [D01 §1, §2.1 #1]. Its RB-1 instruments (REM-10..16) are hash-EQUAL by design; RB-2 items are declared
hash movers, one per commit [D02 §2 #3].

### 3.5 Built vs designed
| element | grade | evidence | proposed and absent |
|---|---|---|---|
| headless/populated/soak runners | TESTS-ONLY | [C13 §3] | — |
| determinism + invariant sweep | TESTS-ONLY (measured PASS) | [C13 §4d] | — |
| THE NINE status | DESIGN-ONLY as a count | "DOC-DERIVED … not execution" [C13 §4d] | conjuncts in E-7..E-10 [D01 §6.3] |
| aperture refusal-clause printing, `attempts()` counter, per-verb DEGREES, `--draw-seeds` | DESIGN-ONLY | REM-10, 11, 13, 15 [D02 §4.0] | — |
| balance instrument at campaign level | absent | `tools/balance_oracle.py` retired; `arms.py` is one mechanic over the season loop (CLAUDE.md §7) | — |

### 3.6 Structural handles
Testing model: seeded deterministic simulation with content hashes as regression oracles, n-seed sweeps, two-arm controls, and per-verb
funnels; acceptance is a set of ruled natural-language requirements tracked by status strings plus measurement commands. Evidence culture:
"Probe verdicts are HARD; case verdicts are ADVISORY" (`run_cases.py`) [C13 §3]. Scale of test worlds: 1 NPC (headless), 46 NPCs + 37
settlements (realm), 13 seats (spine).

### 3.7 Conflicts, uncertainties, checks made (all three blocks)
1. **Verb count.** HEAD `a4ca9a5` has 53 rows, 47 resolvable (CHECKED by import and by run). D01 says 46 at `b70b5af`; R-05's `measure:`
   says "44 today"; `requirements.yaml:985` says 45; the headless comment says "all 32"; driver comment "W3 measured 12 of 32"; R-05
   `measured:` "13 of 38 AS OF 2026-09-20" [C13 §5; D01 §2.1 #10; C02 §4.1]. I believe 53 for HEAD; the others are dated readings of
   different counters (rows / resolvable / executed). Executed count at HEAD is not re-measured here (last: 16, D01).
2. **Driver docstring** says "Six steps, four barriers"; code binds seven (ENCOUNTER added, ED-IN-0279) [C02 §2]. Code wins.
3. **Field battles.** D06 says "at realm weights every opposed `march` grades Lost" ([J]/[P], static, no run); D01/D02 measured `field.*`
   = 0 in both worlds. Compatible if no opposed march reaches ENCOUNTER in shipped worlds; I take the measured zero.
4. **R-08 rationality.** Stored `measured:` text says the chooser "takes the top-ranked candidate deterministically" and cites
   `engine/season/decision.py::make_chooser` (path gone; now `decision/choose.py`); D01 measures a sampler with `choice_temperature 0.1`
   that overrules the strict top 72 % of the time. The `measured:` text is stale; the draw exists. `register` cannot see this (syntactic).
5. **Status strings.** `engine/dice_engine/__init__.py:7` PROVISIONAL vs modules CANONICAL; `LEVEL_SIGMA` "NOT canonical" yet each line
   tagged `[canonical: …]` [C01 §7]. `m1_acceptance` docstring says five rows; code has four [C13 §2].
6. **Three dice implementations** (canonical, mass-battle copy held by a guard, frozen oracle) [C01 §7]. Combat's season degree bypasses
   the margin ladder by ruling (`combat_degree`).
7. **R-09 "probabilistic"**: rolls are keyed to `world_seed`, so a chain varies only across seeds; REM-15 records this as a residue [D01 §4 R-09].
8. **Stale map**: `engine/autoload/dice_engine.py` (CLAUDE.md §5) and a "campaign driver" in `engine/` (CLAUDE.md §3) do not exist; CLAUDE.md
   §3 omits `modules/`.
9. Not traced: `modules/combat/fight.py` → `core.py` call chain in a season; `decision/` chooser internals (other synthesisers).

Checks (this session, read-only, `PYTHONDONTWRITEBYTECODE=1`):
- CHECKED `engine/dice_engine/dice_engine.py:286-301` — ladder exactly as C01 states.
- CHECKED `engine/season/loop/driver.py:80,98,447-515` — one `mint_token` per barrier, ENCOUNTER second ACTS token, census MATTER, `tick += 1`.
- CHECKED `engine/season/state/world.py:847,1348,1355` — `write`, `_STATE_COLLECTIONS`, `content_hash`.
- CHECKED `engine/season/harness/headless.py:166-171,198` and ran it: 47 of 53, hash `fc4d4cef…` (equals C13).
- CHECKED `python -m engine.season.harness.register --requirements`: met 3 · not_met 1 · partial 5 (equals C13).
- CHECKED `modules/mass_battle/resolution.py:105-112` (own ladder, guard-held); `modules/combat/core.py:126` (net + soft_cap·sigma_n).
- CHECKED contested verbs and prize routing by import of `VERB_TABLE` / `manifest.resolve`: *the body* → combat `step None`; *a field* →
  mass_battle `step ENCOUNTER`, `declares Declared`; *a matter/standing/proposition* → `social_contest.roll`.
- CHECKED `engine/season/queries/world_q.py:953-964` (year = `season_factor_draw` length). No claim REFUTED.

---

<!-- ===== A2 (S2_agents_verbs_data.md) ===== -->

# A2 · S2 — Agents, verbs and data: persons, the chooser, the verb system, queries and authored content

Repo HEAD `a4ca9a5`. Sources: extracts C04, C05, C06, D03, D04, D05 (full), D06, D02 (skimmed); repo code opened only for the
checks in each §7. Evidence grades: RUNS-IN-LOOP / TESTS-ONLY / DESIGN-ONLY (brief). "Run" below = my own descriptive probe,
`build_realm(0)`, seed 0, the shipped `populated.run` chooser recipe, 2 or 4 seasons (scripts in `scratchpad/s2/`); one seed, no
control arm — it counts what happened, it does not compare arms. Proposal texts (D03–D06) are PROPOSED, ratify nothing, and were
written against a **46-row** verb table; HEAD has **53** rows (§C.7), so every proposal count about "shipped rows" is stale.

Headline findings (each cited below):
1. A person is a values-and-relations record with **no capacities**: `Person.capability` is empty on 83 of 83 realm persons, no
   attribute field exists, and 37 of 83 persons (all cohorts) carry no pursuit vector (§A.2, run).
2. The chooser ranks candidates by **verb identity** (a verb × 7-axis alignment cell) plus **stance toward the subject**, then
   samples by Gumbel noise at τ = 0.1; it cannot see odds, opponent, place, witnesses, clock or contents (§B).
3. Of 53 verb rows, 47 are admitted to the fold; in a 2-season realm run 22 verbs produced at least one non-refusal outcome,
   19 were attempted and always refused, 6 were never attempted, 6 cannot be formed (§C table).

---

## A. PERSONS AND THE CHARACTER MODEL — a stored values/relations carrier with no stored capacities; carrier RUNS-IN-LOOP, attributes and template DESIGN-ONLY

### A.1 What it is
Every actor in the game is a `Person`: a named individual, or a **cohort** (one `Person` at `weight > 1` standing for the people of
a populated rung, `cohorts.yaml:1,10-11`, C04 §2). A person is defined by what it **wants** (15 pursuit weights), what it
**believes** (a claim ledger), whom it **favours** (stance rows), what it **holds and owes** (Tenure edges: offices, membership,
obligations, residence) and its **body**. Factions never act: "a PERSON HOLDING AN OFFICE acts" (`verbs.py:122-127`, C04 §5.4).
The player-facing fantasy is a cast of people with distinct convictions living in a political web — not a party of
differently-skilled adventurers. Proposals (D03) aim to add a character template and ten stored attributes; none exists.

### A.2 Operating alone
**Carrier fields** (`state/carriers.py:655-723`, C05 §7; CHECKED by run): `id, name, weight (≥1; is_cohort = weight>1), capability
{key:value}, stance [(referent, valence −5..+5, weight 0..5)], pursuits {pursuit:weight}, ledger [Claim], body (=condition_scale
1000), born, scar {element:count}, conviction {affiliation:0..5}, travel_leg, tenures`.
| element | definition / procedure | constants | cite |
|---|---|---|---|
| pursuits | weights over 15: community, doctrine, family, happiness, honour, individuality, justice, liberty, love, reputation, scholastics, stability, stewardship, virtue, wealth; projected onto 7 bipolar axes by a 15×7 matrix `pursuit_projection` | matrix values C04 §5.6 | C04 §3, §4.4 |
| axes | deontological_instrumental, grandiose_humble, hierarchical_equal, partisan_equitable, precedent_substantive, rigid_flexible, selfish_selfless | — | C04 §3 |
| conviction (affiliation) | intensity 0–5 over 5 affiliations: solmund_orthodoxy, inner_tradition, thread_truth, einhir_restoration, altonian_civics; a stored 0 is a held rejected pole | `incompatible` half-matrix: orthodoxy × {inner_tradition, thread_truth, einhir} true | C05 §affiliations, §7 |
| confliction | Σ min(conv[a],conv[b]) over incompatible pairs; damps the pursuit term by 1/(1+k·confliction) | k = `confliction_weight` = 0 (dormant) | `person_q.py:558-573` |
| religious modulation | doctrine weight × max religious intensity / ceiling | church = {orthodoxy, inner_tradition}, einhir | `person_q.py:599-630` |
| scar | count per pursuit/affiliation; written at WITNESS when a witnessed verb's alignment violates a held element (`elements_violated_by`, `resolve.py::_scar_witnesses`) | SCAR_WEIGHT_SHIFT_AT 2, SCAR_CRISIS_AT 3 | `person_q.py:580-581` |
| scar shift | pursuits at scar ≥ 2 give fraction `shift` of weight to the rest (mass conserved) | `scar_weight_shift` = 0 (dormant) | `person_q.py:635-672` |
| conviction crisis | at scar ≥ 3 the highest-held crisis affiliation FOLDS into its highest incompatible heir, or is destroyed; RESTABILISE "not built" | — | `person_q.py:680-720` |
| stance | `stance_toward` = Σ valence·weight; `regard` = stance + 0.5·judged deeds + 0.5·told deeds (deeds scored by own projected pursuits) | STANCE_MAX 25; judged/told gains 0.5 live | C05 person_q, `cast.py:372-378` |
| loyalty → stance | loyalty = round(50·(cos(pursuits, faction role template)+1)) on 0–100; one stance row per faction | LOYALTY_SCALE 100 (Jordan, ED-IN-0229) | `cast.py:315-381` |
| body | integer on condition scale; body bands cut the scene budget | floors 800/500/100 | C04 §4.5 |

**Genesis**: named persons come from `references/npc_registry.yaml` (46 characters): pursuits from its `convictions` block (a
row naming fewer than all 15 is refused, IN-64), affiliations (one per concern church/einhir/altonia required), faction, title;
`npcs.yaml` (46 rows: institution, home, want, tie); `offices.yaml` (holder). Cohorts: 37 rows, `weight: 2` each (C04 §5.8; C05
cast). **Measured at build** (run, `build_realm(0)`): 83 persons (46 cast + 37 cohorts); capability non-empty on 0; pursuits
empty on 37 (exactly the cohorts); conviction on 46; ledger empty on 83; 79 stance rows in all.
**Dynamics measured** (run, 4 seasons): 83 → 70 persons alive; 35 persons reach scar ≥ 3; conviction changed on 9 (crisis fold
fires); pursuits changed on 0; stance on 1; body on 5; capability on 0; mean ledger 199.0 of `ledger_cap` 200 (saturated).

### A.3 In the whole game
Read by: the chooser (pursuits→axes, stance, scar, conviction, ledger, tenures, body, travel_leg; C04 §5.1); the question layer
(ambitions = live `commit` to OUGHT Propositions; salience = cosine of projected pursuits vs organisation's expected pursuits,
C05 world_q Part 3); contest inputs (`Person.capability[VERB_CAPABILITY[verb]]` else `pool_default` 2 — `tell`, `speak` map to
`copying`, C05 §5); mass battle (side weights, stance, loyalty, C05 inputs); subsistence (cohorts only eat, `subsistence_draw`).
Written by: verbs (body, exists, stance via `fight`/`accept`/`march`/`forgive`; Tenures; travel_leg), WITNESS (ledger, scar),
crisis (conviction), `_eff_argue`/`_eff_determine` (pursuits; both never succeeded in the run), `train` (capability; 38 of 38
refused in the run). Feedback loop that actually runs: witnessed deeds → scar → crisis → conviction rewrite → confliction (dormant
at weight 0) and doctrine modulation → next choice. The value loop pursuits→choice→deed→pursuits does **not** close (no pursuit
writer succeeded). D05 claim 7 — "the shipped world can damage persons and cannot change their minds" — is half-refuted at HEAD:
conviction does change (crisis), pursuits do not.

### A.4 Built vs designed
| element | grade | evidence | what proposals say should exist |
|---|---|---|---|
| Person carrier, pursuits, stance, tenures, ledger, body | RUNS-IN-LOOP | run; `deliberate.py:170` reads them | — |
| scar + conviction crisis (FOLD/destroy) | RUNS-IN-LOOP | run: 9 convictions rewritten in 4 seasons | RESTABILISE branch (not built) |
| scar weight shift, confliction damp | TESTS-ONLY (arms shipped at 0) | fixtures `scar_weight_shift 0`, `confliction_weight 0` | swept arms |
| `capability` (practice) | RUNS-IN-LOOP as a read, always empty | run: 0 of 83; only corpus overlay NPC-088 `{copying:3}` (D03 claim 8) | `practice_roster` + `seat_template` (D03 §4.3) |
| ten attributes (9 ruled + unnamed tenth) | DESIGN-ONLY | registry `attributes: scale "1-7", default 1`, tenth unnamed (`descriptor_registry.yaml:27-36`); no `Person` field | Option B: stored 1–7, read only via `faculty(domain)` on `contests:` rows; tenth = Thread Sensitivity (D03 claims 13, 22) |
| character template (`characters.yaml`, `cast.template_of`, LR1–LR6) | DESIGN-ONLY | file absent (checked) | 21 fields; tally 8 authored/1 derived/3 defaulted/2 null/7 not carried (D03 §4.4) |
| Thread Sensitivity, kit, temperament, kin | DESIGN-ONLY | no field; T2 readers in `systems/` stubs (D03 §4.7) | K-3 carrier "RATIFIED AS INTENT" (D03 claim 22) |
| `systems/characters/sim/conviction.py` scar oracle | TESTS-ONLY | one caller `knots.py:349` + tests; different thresholds model (1/2/3) | retired-oracle remnant (C05) |

### A.5 Structural handles for comparison
Resolution: none on the person itself — a person is the input record to other resolvers. Granularity: one record per named
individual; cohorts aggregate a rung's population as one weighted record. State model: weight vectors (15 pursuits → 7 axes),
signed relation rows, typed edges (Tenures), a bounded belief store (cap 200). Agency: every person, named or cohort, is an
autonomous agent run by the chooser; no player-character privilege exists in code (IN-47 creation space is a proposal, D02
REM-30). Information model: subjective — a person reads only its own ledger (AX-2). Failure/recovery: body loss and death are
written; no shipped raiser of body (`tend` 34/34 refused) or of stance except `forgive` (1). Content model: authored cast
(46 registry rows), generated cohorts; values authored, never generated. Pacing: values static, convictions shift by crisis
within seasons, scars monotone up. Comparable shape: a values-vector NPC (utility AI over ethical axes) with
grand-strategy-style traits replaced by a 15-pursuit vector, lacking the stat block a CRPG or TTRPG character sheet carries.

### A.6 Open decisions named by sources
J-T1 (source of personal inputs: A derived / B stored / A-1; default B), J-T2 (tenth attribute; default TS), J-T4 (do attributes
change; default none), V-2a (attribute at gate/cap without `contests:`), R-0 (blind rerun of the from-scratch fourteen); J-T3
kin answered (i) not carried; J-T5 kit deferred; J-T6 one ladder practice→dice (known S defect: sigma pool = value, combat
`max(5, history+6)`, threadwork `min(3, history+3)`); J-T7 held in IN-47 (D03 §6; D06 §4.3). ED-IN-0296 (2) cohort pursuit
vectors and ED-IN-0293 registry completeness (D02 §191; C05 cast). ED-IN-0185 Q7 "It will be 10 attributes" (ruled, D03 §3).

### A.7 Conflicts, uncertainties, checks
- D03 claim 1 "exactly one verb reads a personal input (`tell`)" — at HEAD `verb_capability` maps `tell` and `speak` (C05 §5;
  C06 §5b); both read an empty map, so the claim holds in effect, not in letter.
- D05 §4.2 "crisis … four-season probe found none" (older tree) — REFUTED at HEAD by my run (9 conviction rewrites).
- Census "stance_rows 44" (C06 §5a) vs my 79: different measures (goal seeding vs all rows); not a conflict.
- Why scar reaches ≥ 3 on 35 persons within 4 seasons, and the 13 deaths' causes, were not traced.
- CHECKED by run: Person field list; capability 0/83; pursuits empty on 37/37 cohorts; `engine/season/characters.yaml` absent;
  CHECKED `references/descriptor_registry.yaml:27-36`.

---

## B. THE DECISION LAYER (CHOOSER) — a per-person scored-and-sampled option picker with no world access; RUNS-IN-LOOP (constructed only by harness code)

### B.1 What it is
The game has no GM and no scripted NPC behaviour: every person, every season, answers one **question** (something that landed in
its ledger, or a need of one of its ambitions) by forming the acts it could take about that question's referents, scoring them
by its own values and feelings, sampling an order with a little noise, and spending its **scene budget** on the top of that order.
Package rule AX-2: "what a PERSON forms, wants and can afford, with no `World` in scope" (`decision/__init__.py:1`, C04 §2). The
fantasy served is a living political world that "plays itself": drama from many small value-driven choices.

### B.2 Operating alone
Call: `choose(p, view, sensation, ask_budget) -> [Scene]` (factory `make_chooser`, `choose.py:410-482`, C04 §4.1).
1. **Question in.** None → no acts. Produced outside the package by `world_q.questions_for` (§D.2) and ordered by attention tier:
   0 ambition referent · 1 own tenure/purview · 2 deed claim with valence under own pursuits · 3 `need` · 4 rest/own act; salience
   (cosine) orders within tiers 0 and 3 (C04 §4.7). Shipped aggregation `first`: one question per deliberation.
2. **Option generation** `opening_set` (`options.py:55-340`, C04 §4.2) over all table rows, in gates: withheld verbs (default
   `destroy_record`) → person-side eligibility (`own` admits; `remit:<act>` admits via a live `hold` Tenure's `granted_acts`;
   `hold:<x>`; `presence:` ALWAYS declines person-side, H-33) → refusal gate (dormant, `refusal_axis None`) → subject ∈ the
   question's referents (class-partitioned) → per-verb narrowing (warrants, own stance for `forgive`, held objects) → operand
   derivation (fails → no candidate) → **known-false veto**: drop if the person's OWN claims contradict the precondition
   ("not unproven", `options.py:93-99`). Output `Candidate(verb, subject, operands)`, one per granting seat (H-134).
3. **Score** (`choose.py:146-151`, CHECKED): `score = damp·Σ_axis axis_w[ax]·align(verb, ax) + (1+stance_gain)·stance(subject) +
   urgency`. `axis_w` = projected pursuits after scar shift and doctrine modulation; `damp` = 1 at shipped `confliction_weight 0`;
   stance arm `legacy` = stored `stance_toward(p, subject)`, gain 1.0; `urgency = subsistence/condition_scale`, identical for every
   candidate, so "CANNOT CHANGE ANY DECISION" (`choose.py:220-237`).
4. **Order** deterministic `score_order` (score desc, ties by verb then subject), then **Plackett–Luce by Gumbel**
   (`choose.py:381-390`, CHECKED): key `−(score/τ + g)`, `g = −ln(−ln u)`, `u` drawn per (person, "choice:verb:subject") from a
   seeded factory, so noise is keyed to the candidate, not its list position. τ = `choice_temperature` 0.1 (sweep at seed 0:
   distinct executed sets τ=0→16, 0.1→10, 0.25→8, 0.5→7, 1.0→7; C06 §5j).
5. **Budget** (`budget.py:57-61`, CHECKED): `max(1, scene_budget 5 + 1·live holds − body bands below floors − 1·travel legs)`;
   unit = scene actions; "5 scenes for a character to play per season" (Jordan, C06 §5j).
6. **Pack** (`pack_scenes`, rule `greedy`): chunks of ≤ 3 interactions; a multi-interaction (extended) scene costs 2; trimmed to
   one interaction if the remainder is short (C04 §4.6).
7. **Declared intent** (dormant, `intent_disclosure 0.0`). Returns Scenes; writes nothing to state.
Driver side (`loop/deliberate.py`, CHECKED call at `:170`): per person per round, re-deliberate only if inputs changed or queue empty;
release ≤ `scenes_per_round` 1 scene per round; overspend raises `Forbidden`.
Randomness: exactly two draws (order, intent); the draw factory is built by the caller — every `make_chooser(` call site is in
`harness/` (aperture, corpus_run, probes, decision_spread, soak, storybar, headless, play_surface, populated.run), none in `loop/`
(grep, §B.7).

### B.3 In the whole game
Invoked by `SeasonDriver.season(choose, …)` → `deliberate` at the DELIBERATE step for every person. Reads only person-side data
(AX-2 enforced by `test_choose_receives_no_world`, `test_decision_package_never_names_world_anywhere_under_it`, C04 §6). Its output
(Acts) goes to RESOLVE, where the world-side fold re-evaluates the typed precondition **against the world**, and refuses on any
non-True verdict (C06 §4b). Hence the central structural fact: **the chooser forms acts the world then refuses**. Run (2 seasons):
1,132 acts resolved; e.g. `work` 78 attempted / 0 succeeded (`work.unavailable`), `commit` 64/0, `migrate` 81/0, `research`
125/7, `examine` 62/0 (§C table). D02 traces several to wrong-class referents (e.g. `commit` "66/0 all `exists:Proposition`",
`work` "82/82", REM-22/23). Refusals deposit as beliefs (via WITNESS, `observation_deposit_mode: actor`) so a person can later
veto by known-false — the only learning channel. Who-sees-what (D05 §4.13, static, older tree): of 16 node types the chooser
"sees" 3 fully, 5 partly, 8 not (capability, place, obligations, others' beliefs, witnesses, clock, third-party capacity,
contents). Goals reach choice only through attention tiers, never through the score (`goals.yaml:11-12`).
Measured consequences: 37 of 83 persons (cohorts) have zero pursuit vector → pursuit term 0 for every candidate (run); 13 of 53
verbs have no alignment cell (`argue, carry, conceal, covenant, examine, forgive, interview, restore, sabotage, tell, tend,
thread_read, train`; CHECKED) → value-blind for everyone; `selfish_selfless` has 0 cells. For those cases stance plus Gumbel noise
decides.

### B.4 Built vs designed
| element | grade | evidence | proposal / gap |
|---|---|---|---|
| question → opening_set → score → Gumbel → budget → pack | RUNS-IN-LOOP | `deliberate.py:170`; run 1,132 acts | — |
| attention tiers + salience | RUNS-IN-LOOP | `world_q.attention_key` at barrier 2 (`driver.py:366`, C05 §6) | ED-IN-0296 (1) tier ruling open |
| known-false veto | RUNS-IN-LOOP | `options.py:308` | D05: beliefs used "only as a veto … nothing turns those beliefs into a preference" |
| stance arms `regard`, `declared`; refusal gate; scar shift; confliction; intent disclosure | TESTS-ONLY | shipped at control values (C04 §7) | sweeps |
| urgency term | RUNS-IN-LOOP, inert by construction | `choose.py:220-237` | REM-44 deletes it (D02) |
| `benefits_me` / beneficiary column | DESIGN-ONLY | "NOTHING MULTIPLIES THIS YET" (`choose.py:195-214`) | — |
| contents-aware value term / `(verb, kind)` key | DESIGN-ONLY | D06 §4.6 "most consequential open lever" (D-V6) | — |
| risk term over believed odds | DESIGN-ONLY | D05 §4.13 | — |
| production chooser constructor in `loop/` | absent | grep | — |

### B.5 Structural handles
Resolution: deterministic utility score + softmax sampling (Plackett–Luce/Gumbel), τ = 0.1. Granularity: one question per person
per deliberation; candidate = (verb, subject, operands). Scale: identical procedure for a peasant cohort and a king; office adds
budget (+1 per hold) and remit verbs. State model: stateless function of person snapshot + view (k = 12 most recent ledger ids).
Agency: fully autonomous, value-driven; player control only via a `dispatching_chooser` callback (`play_surface.py:5`, harness).
Information: strictly subjective (own ledger, own tenures); no lookahead, no outcome prediction, no opponent model. Failure: acts
fail at the fold, cost a scene, and leave a belief. Content: rule-generated options from the verb table; no authored dialogue or
scripts. Pacing: 5 scene actions per season, 1 scene released per round. Precedent handles: utility-AI NPC selection
(Sims/CK3-style weighted options), but scored on act type rather than predicted consequence.

### B.6 Open decisions
D-V6 contents-aware value term vs mood-keyed alignment cell; ED-IN-0296 (1) attention tiers, (2) cohort pursuit vectors, (3)
own-act screen; JQ-1 (decision-spread threshold, D02 REM-05); H-33 presence eligibility; H-75 placeholder holds; H-134 per-seat
candidates; H-188 confliction form; H-192/H-193 regard gains; ED-IN-0292 (2) `seat_holders` referent read from world (C05).

### B.7 Conflicts, uncertainties, checks
- C04 docstrings say "thirteen convictions → four axes (13×4)"; loaded code is 15×7 (C04 §3). `choose` docstring "→ Act[]",
  code returns Scenes. D05 internal count conflict 4 vs 3 vs 16 nodes (D05 claim 11) — not reconciled by its author.
- C04 cites the driver call at `deliberate.py:~186`; actual line 170 (CHECKED `engine/season/loop/deliberate.py:170`).
- CHECKED `engine/season/decision/choose.py:146-151` (score), `:381-390` (Gumbel), `engine/season/decision/budget.py:57-61`,
  `make_chooser(` call sites (grep, all under `harness/`), fixture defaults (τ 0.1, `legacy`, gain 1.0, budget 5, per-round 1,
  `refusal_axis None`, `confliction_weight 0`, `scar_weight_shift 0`, `intent_disclosure 0.0`).

---

## C. THE VERB SYSTEM — one data table (53 rows) read by one fold; 47 rows admitted; RUNS-IN-LOOP for 41 verbs (22 with outcomes), the 92-verb roster DESIGN-ONLY

### C.1 What it is
A **verb** is the only way anything changes the world: an act by one person, named in `verb_table.yaml`, with a stratum, an
eligibility rule, a typed precondition, the record fields it writes, and the event kinds it emits on success and on refusal.
"ONE `resolve` READS THIS TABLE … a lambda per act IS a second resolver" (`verb_table.yaml:9-14`, C04 §2). A verb is not a
subsystem: subsystems (combat, mass battle, social contest, fieldwork) are reached only through a verb row's `contests:` prize.
The fantasy: a closed, legible vocabulary of political, social, material and violent acts shared by every agent.

### C.2 Operating alone — the pipeline
`Candidate` (chooser) → `Act(id, actor, verb, payload, via)` → RESOLVE fold (`loop/resolve.py`, C06 §4b):
1. **Eligibility** (world-side copy of `own | remit:<act> | hold:<x> | presence:<rung|site>`); failure emits `act.ineligible`.
2. **Precondition**: `evaluate(row.requires_typed, WorldReader(w, actor), binding_from_act(a))` → True / False / UNKNOWN over 7
   forms (`existence, scalar_threshold, contain_path, relation, own_ledger, basis, cardinality`) and 8 operands (`actor, amount,
   floor, from, kind, site, subject, to`); "FALSE DOMINATES UNKNOWN"; **any non-True refuses** (`resolve.py:274-283`). 43 rows
   typed, 10 untyped (fall back to `REQUIRES_PREDICATES`, C04 §5.4). Refusal → `row.refusal_for(failed clause)` → event kind,
   "THE SCARCITY CHANNEL".
3. **Contest** (only rows with `contests:`; prize → subsystem via `rosters.yaml: contest_subsystems`): "the body" → `combat.fight`
   (`fight`, `accept`); "a field" → `mass_battle.resolve_field` at ENCOUNTER (`march`); "a standing"/"a proposition"/"a matter" →
   `social_contest.roll` (σ-leverage d10; `tell`, `argue`, `determine`, `speak`). Graded inquiries `research, examine, surveil`
   also route to `social_contest.roll` (C06 §5b). Inputs are typed records built by `seam/wrappers/*` (pool = capability or
   `pool_default` 2; C05 §5). Degree bands: Overwhelming/Success/Partial/Failure; Felled/Wounded/Untouched; Declared/Won/Lost/
   Unopposed. **Contested rows at HEAD: 7** (CHECKED).
4. **Effects**: each `writes:` entry (`Kind.field`) must be a `write_matrix.yaml` row (40 rows; "ANY UNMARKED CELL IS A
   WRITE-CLASS VIOLATION", C06 §4c), applied by an `@effect_for` body; contested rows key writes/emits by degree.
5. **Emit** events → WITNESS deposits claims to observers by channel precedence (`co_located, witness_key, document_key,
   chronicle, post_remit`), scars witnesses, and the loop continues.
"Shipped" in code = `resolvable_verbs()` (`driver.py:101`): precondition evaluable AND effect carried AND not routed to an
unreturning seam. Verb ↔ event: a kind maps back to a verb only where exactly one row emits it (`data/verbs.py:1233-1248`, D06
§2.10) — shared kinds (`tenure.closed`, `finding.made`) judge no verb.

### C.3 The 53 shipped rows (table: C04 §5.5; resolvability and run: my probe, 2 seasons, seed 0, `att/ok` = attempted acts /
acts with a non-refusal event; R = resolver: F fold, Cb combat, Cf field, Cs social σ, GI graded inquiry; tg = table `grade:`
r ruled / a assumption / x absent; evidence: RIL = RUNS-IN-LOOP with outcomes, RIL-r = RUNS-IN-LOOP refusals only, T = admitted
but 0 attempts (TESTS-ONLY at best), D = not admitted (DESIGN-ONLY))
| verb | R | writes | tg | att/ok | ev |
|---|---|---|---|---|---|
| carry | F | Record.stages, DocketItem.* | r | 28/0 | RIL-r |
| argue | Cs | Person.pursuits (Over/Success) | a | 10/0 | RIL-r |
| commit | F | Tenure.since | r | 64/0 | RIL-r |
| comply | F | — | r | 0 | T |
| conceal | F | Record.exists (cover) | a | 20/19 | RIL |
| confer | F | Tenure.until/since/term | r | 0 | T |
| convene | F | Date.due_at, ConveningCondition | r | 1/0 | RIL-r |
| covenant | F | Record.exists/stages | a | 13/0 | RIL-r |
| create_record | F | Record.exists/stages | r | 88/87 | RIL |
| destroy_record | F | Record.exists | r | 0 (withheld) | T |
| determine | Cs | Tenure.since/degree, DocketItem.matter, Person.pursuits | a | 2/0 | RIL-r |
| dispatch | F | — | r | 18/6 | RIL |
| establish | F | Office.exists/remit_acts, Tenure.payload | a | 0 | T |
| evade / defy | F | — | r | — | D |
| exchange | F | Rung.stores | a | — | D |
| forge | F | Record.exists, forgery_quality | a | 53/12 | RIL |
| forgive | F | Person.stance | a | 1/1 | RIL |
| found | F | Rung.exists, Tenure.since, Rung.stores | a | 24/0 | RIL-r |
| build | F | Site.exists, Rung.stores | a | 19/0 | RIL-r |
| give | F | Tenure.until/since | r | 16/0 | RIL-r |
| issue | F | Record.exists (dispensation) | r | 6/5 | RIL |
| fight | Cb | Felled: body, exists, Tenure.until; Wounded: body | r | 19/7 | RIL |
| challenge | F | — | a | 24/6 | RIL |
| accept | Cb | as fight | a | 34/18 | RIL |
| requisition | F | Rung.stores ×2 | a | 2/0 | RIL-r |
| march | Cf | body, stance, Tenure, travel_leg (by band) | r | 25/0 (21 Declared, 0 field outcomes) | RIL-r |
| migrate | F | travel_leg, Tenure.until/since (reside) | a | 81/0 | RIL-r |
| move | F | travel_leg, Tenure.until/since (contain) | a | 42/16 | RIL |
| oblige | F | Tenure.since/term | r | 0 | T |
| open_case | F | Record.*, DocketItem.* | a | 13/6 | RIL |
| petition | F | Record.exists | r | 42/14 | RIL |
| construe | F | — | x | — | D |
| release | F | Tenure.until | r | 45/3 | RIL |
| restore | F | Site.condition | r | 23/0 | RIL-r |
| revoke | F | Tenure.until/since | r | 6/0 | RIL-r |
| sabotage | F | Site.condition | a | 35/0 | RIL-r |
| seize | F | Tenure.until/since | a | 0 | T |
| speak | Cs | degree maps, all empty | a | 22/3 | RIL |
| succeed | F | Tenure.since | a | — | D |
| survey | F | Record.exists (faction_sheet) | a | 58/13 | RIL |
| tend | F | Person.body | a | 34/0 | RIL-r |
| tell | Cs | degree maps, all empty (content moves at WITNESS) | r | 27/4 | RIL |
| examine | GI | — | a | 62/0 | RIL-r |
| interview | F | — | a | 33/11 | RIL |
| research | GI | — | a | 125/7 | RIL |
| surveil | GI | — | a | 51/5 | RIL |
| thread_read | F | — | a | — | D |
| reconstruct | F | — | r | 40/33 | RIL |
| tie / knot | F | Tenure.since | r | — | D |
| train | F | Person.capability | a | 38/0 | RIL-r |
| transfer | F | Rung.stores ×2, Tenure.term | r | 45/1 | RIL |
| utter | F | Proposition.exists | a | 40/39 | RIL |
| work | F | Site.condition | r | 78/0 | RIL-r |
Tallies: strata social 19, uncontested_material 17, binding_decision 9, contested_physical 6, movement 2; table grades ruled 23 /
assumption 29 / absent 1; scale person 43, settlement 8, territory 1, province 1 (CHECKED / C04 §5.4). Evidence: RIL 22, RIL-r 19,
T 6, D 6. The 19 RIL-r rows include every verb that **builds, repairs, heals, trains, migrates or persuades**; the world's
material, territorial and value-changing acts never landed in the run. Missing to fill the table further: per-row `scale`,
`requires_typed` form, refusal-clause breakdown, and multi-seed counts.

### C.4 The proposed roster (DESIGN-ONLY) — 92 verbs in ten subsystems
`proposals/2026-10-16-verbs/` Part III (D04 §5.1): PC 7, MB 9, SC 11, FI 12, TW 7, GV 20, FA 7, EC 8, WT 3, NP 8 = 92; "48
descend from the 46 shipped rows … 11 planned positions, 33 new". **Suite** = "a host verb with the related-but-distinct acts
folded into it" (fold kinds: content, posture/choice, key); folds pass only S-4 (same actor, same mechanic, differing in a
parameter). Examples: `fight` hosts keys `accept, assassinate, capture`; `march` postures `besiege, storm`; `tell` hosts `testify,
confess, warn, praise, insult…`; `confer` hosts `appoint, elect, designate`; `covenant` hosts treaty/peace/alliance/truce/tribute/
vassalage contents; `work` hosts `cultivate, mine, fish, hunt`; `travel` hosts `navigate, ride, sail`. Standards S-1..S-8 (each verb
one subsystem and a named write; convention floor kept; NERS then cull; etymology chains to Latin/PIE as linguistic record, not
design intent). Reconciliation rulings R-01..R-29 (e.g. `levy`/`recruit`/`hire` split by actor and edge; `tax` own row; renames
`oblige→pledge`, `carry→lodge`, `surveil→watch`, `move→travel`). The roster "predicts nothing about play until the mechanics of
§III.10 exist" (D04 claim 9): **127 named mechanics**, 14 shared (troop stock/field force; `edict` Record + MATTER readers; finding
producer; concealment grade; proofs reader; commit count; custody opener; debt Record and wage edge; public channel; mood-keyed
alignment cell + `at_war` reader; route Query; labour→yield; end of a Site/Rung; capability/attribute readers) (D04 §4.3). Gap
register: 488 gaps, 312 "closed" (= answerable once a mechanic exists, "not that engine does it today"), 58 parked, 97 out of
scope, 13 stale, 8 disputed (D04 §4.6). Build order V0..V6 (rename batch → shared carriers → force → threadwork → law/custody →
seats/factions → persons/covert), with falsifiers per batch (D06 §4.1-4.2). On "the 11 named suites per subsystem": no construct of
that name appears in my extracts; SC is the subsystem with 11 verbs, and §III.4 names roughly 46 suite hosts across ten subsystems.

### C.5 In the whole game
Verbs are the sole writers of person and world state outside the clocks (MATTER yield/wear/decay, CALENDAR, CENSUS). Effect
taxonomy (D05 §4.9, older tree): roles HARMER, MOVER (persons/matter), BINDER, SEATER, CLOSER, ASSEMBLER, MAINTAINER, RECORDER,
PROCEDURALIST, INFORMER, INQUIRER, RESPONDER. Static findings still true at HEAD: the alignment table makes one-axis verb families
totally ordered for every person (`revoke` −0.7 / `issue`, `seize` −0.6 / `dispatch` −0.5 / `convene` −0.4 on
`hierarchical_equal` alone; `issue` ≡ `seize`, `transfer` ≡ `exchange`; D05 §4.1); escalation exists, de-escalation edges are
planned or unformed (D05 §4.12 item 10); "the world is gate-rich and response-poor" (D05 claim 8). Run adds: in two seasons no
`march` reached a field outcome, so mass battle is not exercised by the season loop (consistent with D02 REM-27, D06 §2.13).

### C.6 Structural handles
Resolution: deterministic gate-and-write on 37 of 47 admitted rows; dice (σ d10 or combat/field modules) on 7 contested rows
and 3 graded inquiries.
Granularity: one act = one scene interaction; extended scenes bundle ≤ 3. Scale: person-scale acts; seat-holders act on
settlement/territory/province through `remit:` and `via`. State model: declarative row → typed write cells; three-valued
preconditions. Agency: any person, eligibility by own standing or office. Information: success and refusal both become witnessed
claims; failure is mostly refusal at the cost of a scene (D05 RISK: only contested rows grade). Content: closed authored
vocabulary in data (a "closed set in data"); no free-form actions. Pacing: per-season scene budget. Precedent handles: a
board-game action menu with legality checks (closer to a grand-strategy decision list than a TTRPG's open fiction), with
TTRPG-style dice only at contests.

### C.7 Open decisions, conflicts, checks
Open (D04 §6): D-V1..D-V21 (e.g. D-V4 J-C-6 may persons lie; D-V7 `dispatch` name vs ED-IN-0210; D-V8 field force amends Layer 1;
D-V9 does march require war; D-V11 who may declare war; D-V12 may a won contest open the counterparty's edge; D-V13 draw policy
under scarcity; D-V16 how an interviewee answers), R-06 `utter` rename, R-17 `pardon` name, L-18/H-52 `remit:issue` gating,
J-1 troop body; H-62 pursuits unproduced; H-85 thread_read gate; H-210 forgery quality unread; R-C-23 inquiry content yield.
Conflicts: (1) proposals count 46 rows (`seize` at `:898`, D03 §1; D06 §2.5); HEAD has 53, `seize` at `:1042` — CHECKED
`engine/season/verb_table.yaml` (53 `- verb:` lines; PyYAML 53). The seven rows added since — `argue, conceal, covenant, forgive,
sabotage, tend, train` — are what the proposals call PLANNED; they are rows, admitted, and (except `conceal`, `forgive`) always
refused in the run; all seven are uncelled (value-blind). (2) Proposals say 4 contested rows; HEAD 7 (`argue, determine, speak`
added) — CHECKED. (3) D05 lists `carry` "not resolvable"; HEAD admits it (`resolvable_verbs` CHECKED: 47; not admitted exactly
`construe, evade / defy, exchange, succeed, thread_read, tie / knot`). (4) Proposals' `VT:` line cites (e.g. `fight` 556-581) are
pre-growth; current `fight` is `:612`. (5) Whether the inquiries' `finding.made` now carries content (R-C-23) was not checked.
Run caveat: one seed, two seasons; "ok" = an act with at least one non-refusal event via `causing_act`; a `march` with
`march.declared` then `march.refused` counts refused.

---

## D. QUERY LAYER AND AUTHORED CONTENT — ownerless derived quantities over one world state, plus data registries read at runtime; queries RUNS-IN-LOOP, several registries harness-only

### D.1 What it is
The game stores few aggregates: factions, provinces, sovereignty, population, hunger, war are **computed on demand** from records
and edges ("A faction IS a Proposition plus its `commit` edges", C05 Part 2). `queries/` is "the ownerless functions. Nothing here
owns state and nothing here writes" (C05 §2). Authored content — rosters, offices, proceedings, venues, goals, cast, geography —
lives in YAML that code loads and validates at runtime ("Changing one is a DATA EDIT", `rosters.yaml:1`, C06 §2).

### D.2 Operating alone
Three modules (C05 §2-4): `world_q` (World-first; 2,771 lines), `person_q` (asker-first, may not reach the world side, test-pinned),
`faction_q`; plus barrier caches (`tenure_index`, `presence_index`, discarded at each barrier) and typed `inputs` records for module
seams. Key derived quantities (verbatim formulas in C05):
| quantity | definition | cite |
|---|---|---|
| members / leaders of a faction | live `commit` subjects / members ∩ holders of that faction's offices | `world_q.py:1365-1419` |
| faction head | last graded `commit`; **None in every buildable world** (degree never written) | `faction_q.py:116-147` |
| at_war(a,b) | live `commit` to a WAR Proposition naming the pair; **False for every world-gen pair**, read by nothing (D06 §4.17) | `faction_q.py:219-252` |
| province | exists only while its territories share a faction holder (ratified, Jordan 2026-07-13) | `world_q.py:1563` |
| sovereign_fraction | top holder's share of held rungs; measured `(0.4, 304)` at realm | `world_q.py:1514` |
| population / capacity | Σ resident weights / max(floor, dwelling Sites) | `world_q.py:1262-1310` |
| subsistence draw | cohorts eat `subsistence_weight` (grain 2, salt 1) × weight from nearest store up the ladder; individuals never eat | `world_q.py:1017` |
| reception / proofs | bench-weighted deed valence of the speaker / unmirrored attributed deeds — the social-contest room terms | `world_q.py:546-606` |
| questions_for | claims landed within reach + standing crossings + ambitions' needs + sittings, sorted by attention tier | `world_q.py:2249` |
| WorldReader.read | the predicate stems the fold's preconditions read (`exists:`, `stores:`, `condition`, `held_by:`, `present_at:`, `purview:`, `bench:` …) | `world_q.py:2614-2766` |
| LedgerReader | belief = best claim by recency/confidence (optionally corroboration across origins); absence = UNKNOWN, never False | `person_q.py:774` |

### D.3 Authored registries (C06 §5; counts by loader runs in C06)
| registry | content | read by | grade |
|---|---|---|---|
| `rosters.yaml` (3,378 lines) | 81 rosters + 7 tables (alignment, pursuit_projection, incompatible, affiliation_engagement, role_template_pursuits, band_floors, site_yield); 9 factions incl. test `faction x`; rung ladder person<hearth<community<settlement<territory<province<duchy<realm | every loader; `load_all()` in `SeasonDriver.__init__` | RUNS-IN-LOOP |
| `verb_table.yaml` | 53 rows (§C) | `data/verbs.py` only | RUNS-IN-LOOP |
| `write_matrix.yaml` | 40 (kind, field) rows + 6 retired; Step→WriteClass | `matrix.py` at import | RUNS-IN-LOOP |
| `offices.yaml` | 31 seats (all held), 11 title domains (King→realm … Individual→person); conferral appointed 17 / elected 8 / none 6 | `harness/populated.py` (build) | build-time, then RUNS-IN-LOOP via Tenures |
| `arrangements.yaml` | 8 proceedings (arbitration, parliamentary_debate, council_of_state, legal_trial, tribunal, interrogation, inquisition_hearing, excommunication_deliberation), 14 keys each; 6 of 10 speech kinds | `loop/effects_information.py:18,334,518` | RUNS-IN-LOOP (docket path) |
| `venues.yaml` | 42 building rows by settlement type, quarters; "AUTHORED FOR PLAY … Not canon" | `harness/populated.py:88` | build-time |
| `goals.yaml` | 35 organisational goals (majority `orientation`, which forms no question); stance ±1; derivation `establishes`/`influences`; every row `[ASSUMPTION; medium; Jordan to correct]` | `seed_goals` at build → OUGHT Propositions + `commit` | build-time; reaches choice via attention tier 0 |
| `npcs.yaml` / `references/npc_registry.yaml` | 46 cast rows / 46 characters (faction strings 20 distinct for 8 names; NPC-081/082 corrupted) | `populated.py`, `cast.py` | build-time |
| `cohorts.yaml` | 37 rows `set_s_001..037`, weight 2 | `build_realm` | build-time |
| `valoria_geography_v30.yaml` | 17 provinces, 37 settlements, 55 settlement adjacencies, terrain, vision, march budget | build; `seam/wrappers/mass_battle.py:201` | build + field input |
| `governance_spine.yaml` | 13-seat test ladder, "A TEST FIXTURE, NOT CANON" | `harness/governance_spine.py` | TESTS-ONLY |
| `ENDINGS_CLASSIFIED.yaml` | 50 arc endings: DECIDER 20, ROLL 9, THRESHOLD 8, NEVER 10, UNCLEAR 3; `forced_by_threshold` 19; "AN AGENT CLASSIFICATION OF PROSE" | `harness/corpus_run.py:74-88,655` (only `forced_by_threshold`) | TESTS-ONLY |
| `hole_register.yaml` | 213 rows (assumption 90, measured 53, absent 37, ruled 33) + 26 discharges | `harness/register.py`, `exercises.py`; "not the loop" | TESTS-ONLY (grader) |
| `fixtures.py` `DEFAULT_FIXTURES` | ~90 injected constants, each "declare it a harness fixture at `grade: assumption` … run a 3-point sweep" | `World(seed, fixtures)` | RUNS-IN-LOOP |

### D.4 The default fixture's size (C06 §5a, run by C06; persons CHECKED by my run)
`build_realm(0)`: 1 realm, 3 duchies, 17 territories, 37 settlements, 60 communities (quarters), 211 hearths (buildings), 83
person rungs; 83 persons (46 cast + 37 cohorts, cohort weight total 74); 322 sites; 32 offices (31 authored + 1 unaccounted);
67 propositions (46 `prop_*`, 12 `goal_*`, 9 `fac_*`); 12 goals minted, 23 orientation, 55 commits; stores empty at build. Smaller
worlds: `governance_spine.build()` 13 persons/13 offices; `headless.build_world(0)` 3 persons ("Carin's world"); per-case corpus
worlds from `cases/` (88 files).

### D.5 In the whole game, built vs designed, handles
Queries are read at every barrier (`driver.py:59-64,366`), by preconditions (`WorldReader`), by seam input builders and by the
chooser's question supply; they are the game's only "aggregate" layer, so cross-scale effects (a faction losing a territory, a
province dissolving) appear the moment edges change, with no update step. Built-but-vacuous by their own docstrings: faction head
(always None), `at_war` (always False), subtree aggregate cache (absent), `Rung.envelope` (unproduced), RESTABILISE, affiliation
engagement content half ("NEARLY INERT IN PLAY") (C05 §7). Designed, not built: adjacency/route Query R-C-7 (D05 §4.16),
`world_q.hunger` settlement Query (D02 REM-50, route A recommended), STAMPERS referent-class registry (D02 REM-21). Handles: state
model = normalised record/edge store with derived views (relational, closer to an ECS/database than to stored meters);
information = world-truth queries on the fold side, belief queries on the person side; content = authored, data-validated closed
sets with loud load-time refusal ("an absent roster is a REFUSAL, never an empty set"); scale = one rung ladder spanning hearth to
realm; pacing = recomputed per barrier.

### D.6 Open decisions
ED-IN-0292 (2) `seat_holders` goal referent read from world with no claim; ED-IN-0296 (1)(2)(3); ED-IN-0297 works; H-161 bench
quorum stand-in; H-158/H-160 upkeep, treasury; H-163 larders in purview; H-109 conferral/revocation owner; D-V3 public channel
after SC-01 step 13 deletes `chronicle`; D-V13 draw policy; hunger requirement (Jordan: "hunger should be a thing for settlement
cohorts", D02).

### D.7 Conflicts, uncertainties, checks
- `ENDINGS_CLASSIFIED.yaml` header and `corpus_run.py:36` say `cases/`; file is at `engine/season/` (C06 §7).
- `requires` roster names `cardinality`; C06 found no `Cardinality` class name — implementation not verified by either extract or me.
- 32nd office's source not read (C06 §5a). Stance-row count differs by measure (§A.7).
- CHECKED by run: 83 persons / 37 cohorts at `build_realm(0)`; `load_all` path not re-opened (relied on C06 `driver.py:247-248`).

---

<!-- ===== A3 (S3_combat_massbattle.md) ===== -->

# A3 · S3 — Personal combat (PC) and mass battle (MB)

Stage-2 synthesis. HEAD `a4ca9a5`. Sources: extracts C08 (final, 248 lines), C09, L09, L10, C01 §6, D02 §4.0; code opened only for the
checks listed in each block's section 7. Grades: RUNS-IN-LOOP / TESTS-ONLY / DESIGN-ONLY (the brief's definitions). Path abbreviations:
`MC/` = `modules/combat/`, `MM/` = `modules/mass_battle/`, `SW-C` = `engine/season/seam/wrappers/combat.py`,
`SW-M` = `engine/season/seam/wrappers/mass_battle.py`, `EC` = `engine/season/loop/effects_combat.py`, `VT` = `engine/season/verb_table.yaml`.

**The shared shape.** Each subsystem is three layers of very different thickness: (1) a large standalone engine under `modules/`
(PC ~5,000 LOC of beat-level fencing physics; MB ~13,500 LOC of cell-grid formation warfare), which is the Python oracle; (2) a thin
season seam (`seam/wrappers/*`) that builds a near-default input from `World`, calls the engine once, and reads one or two numbers
back; (3) a verb lexicon (`proposals/2026-10-16-verbs/…-09`, `…-10`, both `PROPOSED`, reference only) that proposes many more acts
and the mechanics they wait on. Almost all of layer 1's richness is unreachable from the season: the seam fixes every input but one
(PC: `end`; MB: troop count, plus morale start and a terrain row).

---

## Personal combat (PC) — a beat-level duel simulator, RUNS-IN-LOOP, entered through a seam that varies one attribute and writes on one party

### 1 What it is
A two-fighter melee scene resolved entirely by the engine, with no GM and no player input: measure and reach, closing, commit
depth and lunges, a "read contest" that picks the defender's parry / dodge / wind, binds, ripostes, grapples, wounds, stamina,
concentration, initiative and poise, over up to 12 engagements (~10 s each) (C08 §4.1-4.2; `MC/wrapper.py:504` comment). The fantasy
it serves is historical-fencing fidelity: weapons are physical objects (mass, head and grip length, geometry), traditions are
"cognitive modes … NOT a separate rule-set" (`MC/traditions.py:1-8`, C08 §2). In the season it is the resolver for the verbs
`fight` and `accept`: one person attacks or answers a challenge, and the outcome is read as Felled / Wounded / Untouched on the
person attacked (C08 §4.8).

### 2 Operating alone (`modules/combat`, the oracle)
**Entities and state** (C08 §3). `Combatant(label, strength=4, agi=4, end=4, cog=3, att=3, spirit=3, focus=3, history=3, disp=4,
weapon='arming', armor='light', skills=None, equipped=None, tradition='none')` (`MC/combatant.py:93-94`). Live state: stamina,
conc, initiative, poise (reset per fight), plus per-beat grip, lunge, range, facing and selected use-mode. `WoundTracker`:
`cumulative_damage`; `wounds = min(dmg // wi, max_wounds+1)`; `felled = dmg >= health_full`; derived `wi = round(end+4+0.4*spirit)`,
`max_wounds = min(end//2+1, 3)`, `health_full = round(wi*(max_wounds+1) + 0.25*strength*end)` → default 9 / 3 / 40 (C08 §3).
Wounds never cut pools; each adds fractional Ob via `WOUND_DEF_OB=0.25`, `WOUND_ATK_OB=0.15` (C08 §3, §4.4). Data: 54 weapon keys
(50 base + 4 half-sword forms; header says "53") with a physical record and baked geometry (C08 §4.6); 8 tradition keys (7 + `none`)
whose only numeric effects are `familiarity` 1.0 / 0.93 / 0.85 and the gate on 9 abilities (`indes`, `misura`, `shinogi` …) that
multiply named sigma "channels" (C08 §3, §4.7).

**Procedure** (C08 §4.1-4.2).
1. `fight(A,B,max_bouts=12)`: reset wounds and live state; per turn, coin-flip first mover (`wrapper.py:514`), run one `engagement`;
   recover stamina (`RECOVERY_FRAC 0.5`) and concentration between turns. End on a felling, an accepted Yield, or 12 turns → `0`
   UNRESOLVED (ruled legitimate, Jordan 2026-06-02). Then with p = `UPSET_FLOOR 0.05` a decided result's sign is flipped (`wrapper.py:529-530`).
2. `engagement`: reach gap → soft open/closed latch; random cadence phase; beat loop ≤ 24 beats. Open: approach with stop-hit chance
   for the longer weapon; closed: reopen, disengage (with pursuit roll), else an exchange when a fighter's `ready` crosses
   `ACT_THRESHOLD 2.5`.
3. Exchange: commit depth `2 + 3·Beta(·)` skewed by disposition and wariness; commit ≥ `LUNGE_COMMIT 4.0` may lunge; read contest
   (logistic of reading difference × legibility × familiarity) picks defence mode; a sum of sigma terms (`attack_sigma − defence_sigma −
   reach + armour-defeat + initiative + wound impairment`, C08 §4.4) feeds **the roll**; outcome map (fail → riposte chance; partial →
   graze or bind; success → bind / neutralise / hit; overwhelming → hit with tanh-shaped quality bonus); counters, displacement, bind
   sub-loop (≤ 3 inner beats), riposte with role flip, grapple branch (six outcomes, poise/initiative only, no wound). Separation on
   stamina ≤ −4, `BURST_MAX 4` exchanges, a clean defence, or beat exhaustion.
4. Damage: `impact = strength + heft`, × coupling (delivery × material transmission for percussion/shear/puncture vs none/cloth/mail/
   plate) × quality (`graze .25 / success 1.0 / overwhelming 1.5–2.5`) × `DMG_SCALE 1.55`, then an armour penetration knee (C08 §4.3).

**Resolver and dice.** `resolution_pool(history) = max(5, round(history)+6)` (`MC/core.py:54-56`) → 9 at default; Ob =
`defender.history / 2` (ruled 2026-08-15) → 1.5; `net = roll_net_continuous(pool) + soft_cap(net_sigma)·0.8·√pool`, i.e. a
Gaussian draw N(0.40·pool, 0.80·√pool) plus the σ-leverage μ-shift; band by the one ladder `degree_from_net` (margin < 0 fail, [0,1)
partial, [1,3) success, ≥ 3 overwhelming) (C08 §4.3; C01 §4.6). This is the shipped dice engine (`engine/dice_engine/`), not a copy.
Hundreds of further rng draws (latches, Beta commit, read contest, outcome-map coin flips) sit around the one d10-family roll per
exchange; most of the fight's variance is in those draws, not the roll (C08 §4.2, my reading of the procedure).
**Constants**: ~204 `cfg` keys + 25 `core` keys, exported to `engine/engine_params/combat_engine_v1.json` by
`tools/export_engine_params.py`; "Class-C — calibrated against the harness, not canon" (C08 §5, §7). **Output**: `+1/−1/0` plus
mutated Combatants and a trace (C08 §4.1).

### 3 In the whole game
**Call chain** (C08 §4.8, §6; checked): driver → `loop/resolve.py::_contest` (:731; `contest(...)` :806) → `seam/contest.py::contest`
→ provider `personal_combat` (`SW-C:179`) → `entry_for("the body")` → composition role `combat.fight` → `MC/fight.py::fight` →
`pc_engine.load()` → `wrapper.fight`. Prize row `"the body"` has no `step:`, so it fights at RESOLVE (`rosters.yaml:1273-1277`, :1296-1298).
**What it reads from World**: the two claimants (actor, `payload["subject"]`) and each one's `body` → `end = max(1, 4 −
body_band_penalty)` (`SW-C:130-138`). Every other Combatant field is the class default: weapon `arming`, armour `light`, tradition
`none`, no skills, no abilities (`MC/fight.py:45`). So in season play all 54 weapons, all traditions and all abilities are inert,
`familiarity` is always 1.0, and two healthy persons are identical fighters (C08 §7). Seed: the provider derives its own from
`H(world_seed, tick, actor, "contest:<prize>:<cause>")` and ignores the driver's `rng` (`SW-C:222`, docstring :197-205).
**Degree**: read off the SUBJECT's `WoundTracker` by `seam/ladder.py::combat_degree`, edges in `rosters.yaml: combat_band_edges`
(`felled > 0` → Felled; `wounds > 0` → Wounded; else Untouched), not from `degree_from_net` and not from `winner` (C01 §4.7; C08 §4.8 step 6).
**What it writes** (`EC:36-179`, `_eff_kill`, one effect for both verbs): on the subject only — Felled → `body = 0` and
`World.remove_person` (closes every tenure naming the person); Wounded → `body = max(1, body·health_remaining // health_full)` under the
default `wound_harm_model = scene_fraction` (arms `total`, `none` are controls); Untouched → nothing, emits `contest.undecided`
(`VT:612-715`). Emits `person.died` / `body.changed` / `contest.undecided`; refusal `kill.refused`. The fold scars the act's
observers (`loop/resolve.py::_scar_witnesses`). The trace is returned but not folded into `World` (`content_hash` unchanged, C08 §4.8).
**What reads its outputs**: `Person.body` feeds the next fight's `end` (via body bands), the chooser's budget, and death; `person.died`
and the closed tenures cascade into seats and holdings; witnessed kinds deposit claims.
**Measured in-loop activity** (my probe, `populated.run`, 2 seasons): seed 0 — `person.died` 9, `body.changed` 6, `contest.undecided`
10, `kill.refused` 11, `challenge.issued` 6, `challenge.refused` 17; seed 1 — 6 / 5 / 3 / 8 / 6 / 16 (`person.died` also has a matter
source, hunger, so it is not combat-only). Aperture, realm seed 0, 1 season: `fight` 4 attempted / 4 executed; `accept` 11 / 11;
`challenge` 13 / 4 executed / 9 refused. **Feedback loops**: wound → lower `body` → lower `end` in the next fight (one-way, slow);
death → tenure cascade (the strongest link to the strategic layer). No grudge, custody, or reputation write exists (L09 §2.13).

**Defects of the seam, stated as defects.** (a) The actor is never written: the scene fells the actor in about half of mirror fights
(L09 §2.13, "205/400" via `PCL:327`; C08's 60-seed run: result −1 in 33, +1 in 27), and if the subject is untouched the act reports
`contest.undecided` — a false report. (b) A cohort subject (one `Person` standing for many) is deleted whole by one Felled band
(L09 §2.13). (c) `accept` has no challenge carrier: 0 of 12 executed `accept`s had a `challenge` claim behind them (`VT` `accept`
`requires_note`, IN-08 measurement; checked). (d) `yield_decl` is never passed, so Yield cannot occur in a season fight (`MC/fight.py:52`).
(e) My reading of `wrapper.py:529-530`: the 5 % upset flip changes `result` but not the trackers, so in those fights the seam's `winner`
names the felled fighter; nothing writes from `winner`, so the band and writes are unaffected.

### 4 Built vs designed
| element | grade | evidence | what the proposals say should exist and does not |
|---|---|---|---|
| beat/exchange engine, sigma terms, damage physics | RUNS-IN-LOOP (default build only) | call chain §3; probe counts | — |
| 54 weapons, armour tiers, traditions, 9 abilities | TESTS-ONLY | `fight.py:45` sets only `end` | M13 per-person inputs: attributes, experience, kit reach `Combatant`; one equipment model with MB (L09 §4.8, K-PC-1) |
| body bands → `end` | RUNS-IN-LOOP | `SW-C:130-138` | — |
| Felled/Wounded/Untouched read on subject | RUNS-IN-LOOP | `ladder.py` `combat_degree`; `EC:134-151` | M1 two-sided band write (actor too); M15 surviving subject's grudge; M12 band Event saying how it ended |
| Yield (§11.4) | TESTS-ONLY | `test_combat_yield`; never passed | M4 terms in the scene (`first blood`, `yield`, `death`) |
| footwork disengage / flee, grapple, defence modes, feint/lunge | RUNS-IN-LOOP as engine-chosen moves; no chooser | C08 §4.2 | M11 / IN-46: played fight paused per engagement for these moves (D02 REM-31: grid-mode suspension, RB-3b) |
| `challenge` (writes nothing) / `accept` | RUNS-IN-LOOP | aperture counts | M3 `challenge` Record with terms, stakes, `for`; M14 distinguishing kinds (`fight.refused`, duel kind) |
| N-party scene, guards, interpose | DESIGN-ONLY | `SW-C:207-216` two claimants | M7 outer loop over `engagement()`; M8 `guard` Tenure; `guard`, `rescue` rows |
| ranged arms | DESIGN-ONLY (absent) | L09 F9 | M9 missile kind inside the one resolver; M10 co-location/range |
| capture / custody from a fight | DESIGN-ONLY | L09 F5 | M5 (`detain` opens; seatless captor unruled) |
| assassinate / ambush | DESIGN-ONLY | L09 §5 | M6 cover sets first mover, withholds actor from witnesses |
| weight bound on cohorts | DESIGN-ONLY | L09 §2.13 | M2 refusal conjunct `is_cohort` |
| `systems/combat/sim/combat.py` (v30 model) | TESTS-ONLY, DEPRECATED | C08 §6 | — |
| workbench balance harness | TESTS-ONLY (harness) | C08 §6 | — |

**Lexicon's proposed roster** (L09 §5, verbatim count line 207): rows `fight`, `challenge`, `accept` kept and rebuilt; new rows
`assassinate`, `capture` (named folds on `fight`'s effect), `guard`, `rescue`; contents `ambush`, `shoot`, `champion`, duel terms;
eight engine moves exposed under IN-46 (`feint`, `lunge`, `parry`, `dodge`, `grapple`, `flee`, `yield`, `interpose`); culled names
`strike`, `rush`, `disengage`, `withdraw`; outcomes `kill`, `wound`, `disarm`. Build order M1, M2, M14, M15, M3, M4, M12, M10, M5, M6,
M7, M8, M9, M11, M13 (L09 §4.8).

### 5 Structural handles for comparison
- **Resolution style**: dice — a continuous-Gaussian d10-pool approximation with additive σ-leverage μ-shift, one roll per exchange,
  embedded in many probability draws (logistic contests, Beta commit, Bernoulli outcome branches). Degree for the season is a
  threshold reading of accumulated damage, not of a single roll.
- **Granularity**: sub-second beats inside ~10 s engagements inside a ≤ 12-turn scene; physical weapon geometry.
- **Scale**: one versus one only (`SW-C:207-216`).
- **State model**: continuous scalars per fighter (stamina, conc, initiative, poise, cumulative damage); wounds as thresholds on
  cumulative damage; season persistence only through `Person.body` (trackers rebuilt each call, C08 §7).
- **Agency model**: the season chooser picks the verb and the target; the engine picks every tactical move for both sides; no player
  input exists (IN-46 unbuilt).
- **Information model**: the scene is invisible to the world except as an emitted kind witnessed by observers; trace returned to the
  caller, unread by game state.
- **Failure/recovery**: lethal on Felled (person removed, tenures cascade); a wound scales `body` down, floor 1; recovery via `tend`
  (`_eff_tend` raises `body`, C08 §4.8 step 9). Undecided is a ruled outcome.
- **Content model**: authored physics data (weapons, traditions, abilities); no generated content; season combatants generic.
- **Pacing**: resolved instantly inside the RESOLVE step of a season; no pause.

### 6 Open design decisions the sources name
Gap register (G19 §5, rows PC-G01..G40, from `verbs-19`; its disposition column is the v2 FIRST PASS, not current — G19 §2 C13).
Rows that are open design choices rather than build work: PC-G09 / J-C-4 the standing actor's and winner's wounds (no disposition);
PC-G11 decisive vs narrow win, a fourth band refused for lack of source (H-98); PC-G13 Wounded magnitude and start are swept fixtures
(H-123, H-184); PC-G16 cohort as a person at weight > 1 (K-PC-12, H-49); PC-G19 / J-15 the duel's in-bout decision set (IN-46);
PC-G24 / PC-G25 duel ↔ battle yield point and champion (PARKED); PC-G27 / J-T6 two ladders — the duel draws a continuous Normal plus
logistics, the rest of the season discrete dice ("known S defect"); PC-G28 vacancy a killing leaves (H-206); PC-G30 lethal acts gated
only by subject existence (IN-59 (a)); PC-G31 deontological gate dormant (`refusal_axis` None, H-146); PC-G32 / K-45 grudge loop
unsigned; PC-G33 war gate (DISPUTED); PC-G37 designed reputational consequences (Domain Echo, Death Cascade) have no carrier;
PC-G38 / H-128 actor not an observer of his own act; PC-G40 the module's depth decides nothing in play.
From L09 §6 and D02:
§3.9 item 1 (guard edge: any person may protect any person, or seat-holders only via `oblige` + IN-60) — Jordan's; §3.9 item 2
(custody by a seatless captor: widen `detain` vs seat-holders only; overwrites ED-IN-0288) — Jordan's; K-PC-1 per-person inputs and
K-PC-8 one substrate ("already Jordan's"); K-PC-2, -4, -5, -9, -12 (M1, M11, M7, M12, M2; no status stated); D-V6 contents-aware value
term (would turn `accept`/`assassinate`/`capture` into contents); IN-46 (moves exposed to a player; "no build batch" per L09, but D02
REM-31 schedules it in RB-3b); IN-59 (a) / IN-60 co-location and security Query (blocked); PC-G33 / K-FA-1 war gate on `fight`
(DISPUTED); PC-G36 judicial duel (PARKED); PC-10a/b duel terms and challenge carrier (planned); R-1 `execute` not a verb (ruled).

### 7 Conflicts, uncertainties, checks made
- C08 §6 said whether a seeded season forms and executes `fight` was NOT VERIFIED; settled by my probe and the aperture run: it does
  (counts in §3).
- L09 cites `VT` lines +120 and `EC` +2 stale at HEAD; its claim that `conceal` has no row is contradicted (`VT:207`) (L09 §1).
- Weapon count: "53-weapon roster" (`weapons.py:5`) vs 54 keys imported (C08 §4.6); L09 PC-G40 says "53 weapons and 7 traditions" —
  7 traditions plus `none`.
- Combatant comment "persists between encounters" (`combatant.py:57`) vs `fight()` re-initialising trackers each call (C08 §7):
  the code wins; only `Person.body` persists.
- `tempo_pressure` is "currently OUTCOME-INVISIBLE" by its own comment (C08 §4.4); not re-measured.
- CHECKED `modules/combat/fight.py:42-52` (only `end` set; `yield_decl` not passed); CHECKED `SW-C:130-138, 207-253` (party_end,
  own seed, return dict); CHECKED `EC:36-38, 107-179` (one effect, subject only, three harm arms); CHECKED `VT:612-760` (rows,
  `accept` 0-of-12 note); CHECKED `rosters.yaml:805-832, 1273-1298` (wound quantities, band edges, prize rows); CHECKED
  `MC/wrapper.py:524-532` (upset flip); CHECKED `MC/core.py:54-56, 116` (pool, Ob). RAN `python -m engine.season.harness.aperture`
  and a `populated.run(seasons=2)` event-kind count, seeds 0 and 1 (scratchpad `s3_probe.py`).

---

## Mass battle (MB) — a cell-grid formation-warfare engine, wired to the season through `march` but TESTS-ONLY in practice: no seeded season reached a field

### 1 What it is
A tick-based battle between two armies of subunits on a 51×51 cell field: formations (Line, Arrowhead, GappedLine, Column), troop
types with power/discipline/morale, frontage contact, support ranks, volleys and ammunition, charges and bracing, flank and rear
angles, stamina, morale erosion, discipline loss, stochastic rout and rout cascades, timed and conditional orders, officers
(C09 §3, §4.6-4.9; `MM/orchestration.py:1` "SIM-MB-06 v20"). The fantasy is the commander's battle: formation and order choice
decide outcomes at a scale of hundreds to thousands of troops. In the season it is the resolver for one verb, `march`, which
contests the prize `"a field"` (C09 §4.11; `rosters.yaml:1278-1283`).

### 2 Operating alone (`modules/mass_battle`, the oracle)
**Entities and state** (C09 §3). `Unit` (power, command, discipline, morale, dr, hp/hp_max, size, routed/broken, stance, speed,
stamina, volleys, officers, terrain offence/defence offsets) holding `Subunit`s (shape, troop type, tier, troops, per-cell troop and
morale grids, orders, role, yielding/pocketed flags); `Officer` (command, charisma, cognition); `Order` (triggers `immediate`,
`tick:N`, `enemy_range:D`, `ally_at:D`, `own_strength:FRAC`, `signal:NAME`). Troop types, e.g. levy 1/1/2, heavy_infantry 4/4/5,
cavalry 5/5/5, knights_templar 5/6/6 (power/discipline/morale, `MM/troop_types/registry.py:35-47`). Roles map to formations and
instruction primitives; `pin, loose, harass, screen, pursue, volley, shoot_move` are UNWIRED (`units.py:71-100`). Equipment
catalogues are "NOT YET WIRED into resolution" except `reach` (C09 §2-3).

**Procedure** (`run_battle(unit_a, unit_b, max_turns=18)`; 18 ticks = 3 phases of `TICKS_PER_PHASE 6`) (C09 §4.6): per unit once,
a lognormal friction factor `exp(gauss(0, 1.1))`; per tick — volley phase; contacts; orders and targeting; movement; contact
stamina drain; melee per contact pair; HP loss; casualties distributed over cells; `effective_size = hp/100`, size 0 → rout;
formation drift below `MIN_DISCIPLINE`; command 0 → morale 0 ("Command=0 → instant rout", `orchestration.py:2221`); envelopment
shock; per-tick rout (morale ≤ 0 or troops < `SUBUNIT_ROUT_FLOOR 80`); every 6th tick a phase boundary (stamina, discipline,
morale erosion with emergent yield and stochastic break point 0.15-0.30 of losses, rout resolution, empty `rally_check`, reform,
empty `threadwork_check`).

**Resolver and dice** (C09 §4.7). Pool = `power · size · 0.5 + discipline penalty + stamina penalty`, × friction, floor 1, then
apportioned to the troops in contact plus support ranks (weights 1.0 / 0.7 / 0.5); net = **its own** fractional d10 roll at TN 7 (same
face rule as the dice engine) + `softcap(Δσ)·0.8·√pool`, Δσ summing momentum/puncture, charge shock, brace recoil, morale, fatigue,
stance intent and terrain at `SIGMA_PER_D 0.2`; each side's degree is computed against the OTHER side's net as Ob (`compute_degree`,
a local copy of the ladder held equal by `tests/valoria/test_degree_ladder_single_owner.py`, not by import) (C09 §4.7, §6; C01 §6,
§7 "three dice implementations exist"). Casualties: Lanchester-linear `12 · strength · max(0, DAMAGE_BY_DEGREE[deg](power) − dr) ·
angle multiplier` (GREEN 1.0 / YELLOW 1.5 / RED 2.0). Volleys: discrete pool vs target DR, scaled by density. **Constants**: ~151 of
the 277 exported sim params are mass battle's (C01 §5), most env-overridable, many tagged `[CALIBRATED-DEBT]` (C09 §7).
**Output**: `{winner: A|B|draw, turns, phases, hp_pct, morale …}` (C09 §4.6).
Defined but unreached from the season: `pursuit_damage`, recall, feigned retreat, multi-turn and multi-unit battles,
`between_turn_recovery` (C09 §4.10; L10 §2.7).

### 3 In the whole game
**Call chain** (C09 §6): `march` row (`VT:803`, `remit:dispatch`, `contested_physical`, `contests: "a field"`) → admitted and
DECLARED at RESOLVE (band `Declared`, writes nothing) → fought at the ENCOUNTER step (`loop/encounter.py:72` → `_contest`) →
`loop/sides.py::sides_of` (claimants = the actor's mustered army at his nearest settlement under the faction of the seat the act
was exercised through; subject = the target holder's faction; empty army if the target is not in `MARCH_TARGET_KINDS`, closed at
`[settlement]`) → provider `SW-M::resolve` → `MM/massbattle.py::resolve_field` → `_run_and_grade` → `run_battle` (checked
`sides.py:85-110`).
**What it reads from World**: `Person.weight` of each side's members (summed, raw), each side's weight-mean stance toward its own
faction, loyalties, `fortification_of(rung)`, territory and origin for terrain, fixtures `field_walls_dr`, `field_morale_loyalty_gain`
(C09 §4.11). **What the engine sees**: per side ONE `Line` subunit of `infantry`, tier 2, `troops = Σ weight` (floor 1.0),
power 4, command 4, discipline 5, morale start `clamp(round_half_up(5 + stance + gain·loyalty), 1, 7)`; both sides the same start
position dict; one terrain row (WALLS +3 defender DR; UPHILL ±1 die; RIVER_CROSSING −1 attacker; FOREST and NARROW_PASS change
nothing that matters) (`massbattle.py:170-232`, checked :196, :226-228; C09 §4.2-4.5). No troop-type mix, formation, order, officer,
equipment or tactic card reaches the season (C09 §4.2). Weight sums are single or double digits against an engine calibrated for
hundreds, and a subunit under 80 troops routs at the first check ("known risk, disclosed"; C09 probe: weights 10 v 10 → Failure,
0.1/0.1; 200 v 200 → attacker Success, 0.8404/0.6592).
**Grade**: `_run_and_grade` re-derives `attacker_wins = not A.routed and (B.routed or A_size% > B_size%)` and a bespoke four-band
label (Overwhelming ≥ 0.75 / ≤ 0.25, Partial ≥ 0.50) "NOT the canonical degree ladder" (`massbattle.py:82-84, 287-293`); the season
ignores that label and reads only `attacker_wins` → `Won`/`Lost`, or `Unopposed` when the defending faction musters nobody
(`seam/ladder.py::field_degree`) (C09 §4.11).
**What it writes** (`EC::_eff_march`, C09 §4.11; `VT:803` writes): on the LOSING side only — `body = max(1, int(body · size%))`
under `field_casualty_model = scaled_by_degree` (arms `total`, `none`), death if body ≤ 0, two stance rows each (−1.0 toward the
winner's faction, grudge; −1.0 toward own faction, morale, which lowers the next field's morale start); on `Won`/`Unopposed` the
claimants are relocated to the target and `army.arrived` is emitted. No `hold` moves (title moves by `seize`); no stores move.
**What reads its outputs**: `Person.body` and stance (the next field's morale start, decisions), position (relocation).
**Measured in-loop activity** (my probe, 2 seasons): seed 0 — `march.declared` 21, `march.refused` 25, `field.won`/`field.lost`/
`field.unopposed`/`army.arrived` all 0; seed 1 — 10, 10, 0, 0, 0, 0. Aperture, realm seed 0, 1 season: `march` 9 attempted, 9 declared,
9 refused. This reproduces D02 REM-27's defect statement ("`field.won`,`field.lost`,`army.arrived` emitted 0 times both worlds"); REM-27
attributes it to `march` being formed on Rungs that are not field targets and proposes `referent_class: Rung` plus a stamper offering
only settlements in `MARCH_TARGET_KINDS` (D02 §4.0). So the engine is reachable from the driver, but no seeded season fights a field;
its executions are tests (`engine/season/tests/test_mass_battle_provider.py`, `test_march.py`, `tests/valoria/test_mass_battle_*`, the
`systems/mass_battle/sim/bat.py` byte-exact DIGEST gate) (C09 §8). **Feedback loops (designed, unexercised)**: a lost field lowers the
losers' stance → lower morale start next field; grudge rows feed faction hostility.

### 4 Built vs designed
| element | grade | evidence | what the proposals say should exist and does not |
|---|---|---|---|
| `march` admission + Declared band | RUNS-IN-LOOP | probe: `march.declared` 21/10 | REBUILD: reads `marshal`'s order, carries posture, moves stocks (L10 §4.6) |
| field fight via `resolve_field` | TESTS-ONLY (wired, 0 fields in seeded seasons) | probe; D02 REM-27 | REM-27 referent class so a seated marcher reaches `Won`/`Lost` |
| tick engine, contact, Lanchester casualties, morale/rout | TESTS-ONLY | as above | — |
| formations, troop types, roles, orders, officers, volleys | TESTS-ONLY | season builds one Line infantry subunit | M-3 `order_of_battle` Record via `marshal` (formation, stance, role, who leads) |
| pursuit, recall, feigned retreat, reserve commit at turn 2 | TESTS-ONLY | C09 §4.10; L10 §2.7 | M-4 wire `rally_check`, reserve release from the order, season path to `pursuit_damage` |
| `rally_check`, `threadwork_check` | DESIGN-ONLY (empty hooks) | C09 §7 | `rally` = Command pool vs Ob 2 restoring a fraction of lost morale (K-MB-11: fill) |
| tactic cards; Altonian reinforcements | DESIGN-ONLY (stub; `NotImplementedError`) | C09 §7 | — |
| equipment catalogues | TESTS-ONLY, inert (reach only) | C09 §2 | M-11 arms matter kinds and producer |
| weight → troop conversion | DESIGN-ONLY | `massbattle.py` disclosure | REM-32: one conversion injected from a `hole_register.yaml` NUMBER row, shipped at a value equal to today (unblocks JQ-4) |
| troop stock, raising and upkeep | DESIGN-ONLY | `matter_kinds` has no troops (L10 §2.8) | M-2 `recruits`/`troops_<grade>` stocks; `levy`, `recruit`, `muster`, `drill`, `disband`; M-8 costs (consent stance, coin) |
| field force travelling with marchers | DESIGN-ONLY | arrival moves persons only (L10 §2.1) | M-1 (amends ratified Layer 1, rides J-1) |
| siege, supply, foraging, camp | DESIGN-ONLY | no rows (L10 §5a note) | M-6 siege state; `besiege`/`storm` postures; `supply`, `forage`(`sack`), `encamp` + M-12 camp Site |
| surrender, raze | DESIGN-ONLY | — | `surrender` (cession under arms, `place.surrendered`); `raze` needs M-9 end-of-Rung carrier (H-166) |
| deaths by name on a lost field | DESIGN-ONLY | — | M-7 death carrier (K-MB-9, H-152) |
| withdrawn vs routed | DESIGN-ONLY | `field_degree` has 3 bands | M-5 (R-7 `[ASSUMPTION; Jordan to correct]`) |

**Lexicon's proposed roster** (L10 §5a): Suite 1 raising — `levy` (host), `recruit`, `muster` (absorbs `garrison`), `drill`,
`disband`; Suite 2 — `marshal` (host) with folded in-battle contents `rally`, `pursue`, `retreat` (+ feigned), `withstand`, reserve;
`command` culled as a verb (a stat, `derive_command`); Suite 3 — `march` rebuilt with postures `storm` (default) and `besiege`,
`supply` (`provision`, `equip`), `forage` (`sack`), `encamp`, `reconnoitre` (PARKED), `ambush` MB half (PARKED); Suite 4 — `surrender`,
`raze`. Twelve mechanics M-1..M-12 (L10 §5b). Gap register MB-G01..G57: closed 41, PARKED 7, OUT 7, STALE 2 (L10 §5c, recounted).

### 5 Structural handles for comparison
- **Resolution style**: dice pools (own d10 implementation, fractional) with σ-leverage, opposed (each side's net is the other's Ob),
  inside a deterministic-plus-stochastic tick simulation; casualties by a Lanchester-linear law; rout by stochastic thresholds.
- **Granularity**: per cell (≤ 200 troops), per tick; 18 ticks per battle.
- **Scale**: army vs army, two units; multi-unit battles exist in the engine, unreached.
- **State model**: continuous troop counts and HP; morale per subunit and per cell; discipline integer; stamina; ammunition.
- **Agency model**: standalone — pre-battle orders and roles authored by the caller, then automatic; season — the chooser picks
  `march` and a target, everything else default; the defender has no chooser (L10 §2.11).
- **Information model**: none in-battle (no fog modelled for the season path); outcome witnessed as `field.*` kinds.
- **Failure/recovery**: loser's bodies scaled by surviving size share, possible death, morale and grudge stance rows; winner untouched
  ("casualties only, decrease in morale, and a grudge token", ED-IN-0279, `EC:184-187`); a routed army stays at its origin.
- **Content model**: authored troop-type and terrain tables; terrain selected from geography polygons; armies generated from persons.
- **Pacing**: one atomic call per field at ENCOUNTER, after the round's fold; no pause or played battle.

### 6 Open design decisions the sources name
Gap register (G19 §5, rows MB-G01..G57, from `verbs-20`, first-pass dispositions). Open choices rather than build work:
MB-G01 no season force scale (summed weight vs rout floor 80; H-150); MB-G09 / K-MB-10 mass → personal yield, and "Command 0 → instant
rout" as a flat effect; MB-G28 COLLISION: `rally_check` delete (K-MB-11, R-C-8) or fill (v2 V113); MB-G30 / R-7 / D-V5 retreat vs rout
collapsed into Won/Lost; MB-G37 / K-MB-8 the engine's four-label survivor ladder computed and discarded, no margin; MB-G38 mutual rout
graded as the defender holding (`massbattle.py:287`), tie-break unruled; MB-G43 / J-C-4 winner's wounds and experience; MB-G49 / J-C-31
whether a player may command the field once it starts; MB-G50 show of force (a march that compels without fighting); MB-G55 COLLISION
"fraction, never flat" vs command and rally kept flat; MB-G56 / LF-1, LF-3 IN-52 ration bound (Jordan's); MB-G57 `threadwork_check`:
the setting's defining force never touches war; MB-G39 declared marches refused at ENCOUNTER (H-149, H-175) — matches my probe.
From L10 §6 and D02:
§3.9 item 1 / K-MB-5 / MB-G15: does a march between factions require war (FA raises the same) — "two games", Jordan's; §3.9 item 2:
levy service term and paid-stock upkeep (default: none; extensions PARKED); §3.9 item 3 / J-1: the field force M-1 amends ratified
Layer 1 — Jordan's; §3.9 item 4: `sack`'s tone (FA-6 (c) `needs_jordan`); J-5 (c) veterans only by a field (called both "ruled (TS2:717)"
and "Jordan's" in the same file); J-C-19 / K-MB-9 death policy; J-C-31 played fidelity; K-MB-2 Command from charisma/cognition;
K-MB-8 grading the field on one margin; K-MB-10 mass → personal yield; K-MB-12 the seat's military claims as a `march` reader;
R-7 withdrawn vs routed; H-150 graded walls; H-212 occupier's larder draw; FA-G47 `recruit` name collision; JQ-4 (the weight→troop
number, REM-32).

### 7 Conflicts, uncertainties, checks made
- **C09 vs D02 on reach**: C09 §6 traces `march` to `run_battle` from the driver (correct as wiring); D02 REM-27 says no field is
  fought. My probe settles it: wired, 0 fields in seeds 0-1 over 2 seasons. I did not establish why each `march` was refused
  (empty army from a non-settlement target, or an actor with no settlement above him, are the two `sides_of` routes; `sides.py:85-110`).
- **L10 body vs its own rulings block**: R-01 folds `recruit` into `levy` (body: sibling row); R-03 gives `raze` to GV (body: MB
  PLANNED row); R-08 gives `encamp` to WT, parked (body: new MB row). L10 says the roster (`verbs-03`) governs; that file was not read
  by the extractor, so the rulings, not the body, are the stronger reading.
- G19 MB-G35 says "every realm field is WALLS (+3 DR); UPHILL, FOREST, NARROW_PASS, RIVER_CROSSING cannot occur". C09 §4.4 and
  `tests/valoria/test_mass_battle_terrain.py` show polygon terrain selection and a river test now; the register was built at `716c253`
  from older lane files, so I read MB-G35 as stale on the "cannot occur" half. WALLS still wins whenever `fortification_of > 0`, which
  I did not measure across settlements. Likewise G19 PC-G22 "grapple … unactivated" is stale (contact fires at `wrapper.py:435-450`; L09 §4.9).
- L10 cites `VT` and `world_q.py` lines from `716c253`; stale at HEAD (`march` at `VT:803`, `mustered` `world_q.py:1470`,
  `fortification_of` :1490).
- `MB_CELL_MORALE`: comment "RETRACTED to OFF 2026-07-25" vs default `'1'` (`config.py:108`) — code wins (C09 §7).
- The engine bypasses `engine/dice_engine` by design (C01 §6); equivalence is a test, not an import. Separately, `CLAUDE.md` §5 names
  `engine/autoload/dice_engine.py`, which does not exist (C01 §6).
- CHECKED `modules/mass_battle/massbattle.py:82-84, 93-101, 196, 226-228, 283-293`; CHECKED `orchestration.py:2221`; CHECKED
  `config.py:117, 155-156`; CHECKED `loop/sides.py:41-110`; CHECKED `rosters.yaml:1278-1298` (prize `a field`, `step: ENCOUNTER`);
  CHECKED `EC:182-200` (`_eff_march` losing side only). RAN the same aperture and `populated.run` probe as PC §7.

---

<!-- ===== A4 (S4_threadwork.md) ===== -->

# A4 · S4 — Threadwork (TW)

Sources: extract C11 (code, HEAD a4ca9a5), L13 (TW verb lexicon, `proposals/2026-10-16-verbs/…-13-lexicon-threadwork.md`,
status PROPOSED), D02/D04/D05 (skimmed for TW rows). No G20 gap extract exists in `extract/` (checked by `ls`).
Repo checks are listed in §7 as CHECKED/REFUTED.

## Threadwork — a standalone Python oracle of seven dice-pool operations plus a two-quantity Coherence store; the season loop never reaches it. Grade: TESTS-ONLY (core operations, Coherence, collective, opposing); DESIGN-ONLY (co-movement, threadcut, rendering, every TW verb except the shipped-but-unresolvable `thread_read` row)

### 1 What it is

Threadwork is the setting's magic-analogue: a practitioner with enough Thread Sensitivity (TS, "the design's one class gate",
L13 §3 citing `hole_register.yaml:1062`) suspends his own "self-rendering" (the Leap, canon "the suspension of layer-two
self-rendering, undertaken to reach layer three", L13 §3 citing `06_operations.md:63`) and acts directly on the substrate of
things: makes them cohere (Weaving, "Things Cohere"), opens them (Pulling, "Things Open"; Past-Pulling reaches a past moment),
prevents them becoming (Locking, "Unable to Become"), ends them (Dissolution, "Unable to Be"), or repairs the substrate
(Mending, "Repairing the Substrate") (L13 §3 citing `operations.py:376,388,418,435,514`). The price is paid in **Coherence**,
modelled as the practitioner's DISTANCE from the human equilibrium (coherence.py:1-2, C11 §2): small stresses stretch and
relax back (elastic), stresses past a range set permanently (plastic), and a permanent set past the human band is an
irreversible "crossing" (coherence.py:118, :380-408; C11 §4.6). The fantasy is costly, identity-eroding power: each working
pulls the worker away from being human, and only rest in an equilibrium environment or Mending pulls him back.
Collective workings (several practitioners in a lattice), opposed workings (two practitioners contesting one target),
co-movement (side effects drawn as cards) and threadcut beings (entities that maintain their own rendering) extend it.

### 2 Operating alone

**Entities and state** (C11 §3)
- No Thread entity exists in code. Targets are plain dicts (`scale`, `breadth`, `distance`, `recency`, `configuration_of`);
  the actor is duck-typed, reading `.spirit` (default 4), `.ts` (default 30 in the pool; **default 0 in `attempt_leap`**,
  operations.py:358 vs :242 — CHECKED), `.history` (0), `.resilience`, `.cognition` (collective), `.max_wounds`/`.wounds`
  (threadcut). operations.py:15-19 `[ASSUMPTION]`: "World has no practitioner stat schema yet."
- `CoherenceState` (coherence.py:194-253): `resting_point` (int, start 0), `elastic_displacement` (int), `log`,
  `failure_observed` latch. Derived: `present_displacement = resting + elastic`; `crossed = resting_point > 5`.
- Stores are module-level dicts unless the caller's `world` has `practitioners` / `comovement_deck` / `threadcut_beings`
  (coherence.py:143-151; co_movement.py:73-81; threadcut.py:60-68).
- All constants are Python literals; no YAML/JSON is read (C11 §5). coherence.py:92: "EVERY MAGNITUDE BELOW IS INVENTED, AND LICENSED".

**Pool, dice, degree** (C11 §4.1)
- Pool = `(spirit × 2) + min(3, history + 3) + ts // 10` (operations.py:246-247, CHECKED). Defaults give 8 + 3 + 3 = 14 dice.
  The history term evaluates to 3 for every history ≥ 0 — the cap is applied to the sum, so history never moves the pool
  (D02 REM-45, NERS G7; fix proposed `min(3, history) + 3`, gated on hand-verifying PP-624).
- Each d10: 1 → −1, 2-6 → 0, 7-9 → +1, 10 → +2; net = sum; pool floor 1 die (dice_engine.py:150-160, :202).
  **TN 7 always** (ED-IN-0196; PP-619's TN 8/9 differential SUPERSEDED; `_require_tn7` raises on any other, operations.py:51-73).
- Degree = margin (net − Ob): ≥ 3 Overwhelming, ≥ 1 Success, 0 Partial, < 0 Failure (dice_engine.py:227-241, single owner).
- Arithmetic of these rules (mine, not a code claim): per-die mean +0.4, variance 0.64; the default 14-die pool has mean
  net 5.6, s.d. ≈ 3.0.

**Obstacle tables** (operations.py:77-124; C11 §3)

| scale | Object | Personal | Relational | Field | Structural | Foundational |
|---|---|---|---|---|---|---|
| `DEPTH_OB` (Weave/Pull/Lock/Dissolve) | 1 | 2 | 3 | 5 | 8 | 13 |
| `MENDING_OB` | — | — | 2 | 4 | 7 | 12 |
| `COHERENCE_COST_BY_SCALE` | 0 | 0 | −1 | −1 | −2 | −2 (Territorial −1) |
| `DEPTH_TS_MINIMUM` (defined, unread) | 30 | 30 | 50 | 50 | 70 | 90 |

Leap Ob 2 at TS 30-49, 1 at TS 50+; Past-Pulling Ob by recency 3/4/5/6/7 (same scene … 10+ seasons, :406-408).
`BREADTH_OB` (0-4) and `DISTANCE_OB` (0-3) are defined and read by no operation (C11 §3, §7).

**Shared resolver `_resolve_operation`** (operations.py:290-348; C11 §4.2), in order:
1. roll pool at TN 7 against Ob → degree;
2. coherence charge = the operation's base delta, **−1 more on Partial or Failure for every operation except Mending**
   (CHECKED :321-323; the authors' defect C-TW-3: this also hits the Leap, whose docstring says Failure costs nothing);
3. `charge_working` → `resist_coherence_cost` = `min(0, cost + RESILIENCE_GAIN × resilience)`, with `RESILIENCE_GAIN = 0`
   shipped (identity; sweep arms 1, 3 "UNRULED", R-14) → `apply_coherence_delta` (the only write);
4. Mending-Stability (MS) delta: Weaving/Pulling on Partial = scale cost, on Failure = scale cost − 1 (P-25, ED-WR-0008);
   Locking/Dissolution −1 flat. **Reported in `OperationResult`, written nowhere** (operations.py:211-213).

**Per operation** (C11 §4.4; base coherence before the Partial/Failure −1)

| op | Ob | base coherence | notes |
|---|---|---|---|
| Leap | 2 / 1 by TS | 0 | TS < 30 → Failure with no roll, no cost; rolled Partial/Failure → −1 (defect above) |
| Weaving, Pulling | `DEPTH_OB` | scale cost | MS by degree × scale |
| Past-Pulling | recency 3-7 | scale cost − 1; capped −1 at Object/Personal | `scale` not passed to resolver, so no MS term (:413). The cap is a no-op given the table (0 − 1 = −1 already) — my arithmetic |
| Locking, Dissolution | `DEPTH_OB` | scale cost + `FR_SURCHARGE` (−1) | MS −1 flat |
| Mending | `MENDING_OB` (unpriced scale → Relational) | 0 at every degree (ED-871) | see below |

**No operation writes its target** (L13 §2 claim 3; C11 §5): every effect on the world beyond the actor's Coherence is
absent from code. Solo operations do not call `attempt_leap`; only the collective path does (§7).

**Coherence model** (coherence.py; C11 §4.6)
- Stress `s`: `elastic += s`; any excess over `ELASTIC_RANGE = 6` moves into `resting_point` exactly, elastic pinned at 6
  (coherence.py:330-334, CHECKED). Positive deltas are refused (ValueError).
- `recover(seasons, environment_in_equilibrium, mending)`: if in equilibrium, elastic −= `6 × seasons + mending`, floor 0;
  never touches resting_point. Time never adds displacement.
- `mend_resting_point(amount)`: resting −= amount, floor 0; refused once crossed.
- Bands on present displacement: ≥ 6 Fractured, ≥ 4 Fragmented, ≥ 2 Dissonant, else Stable; any crossed state reads
  "Coherence failure". `check_coherence_failure_transition` reports the crossing once and never clears it.
- Worked arithmetic (mine): a Structural Locking at Failure charges −2 −1 −1 = −4; two such without rest put elastic at 6
  and resting_point at 2; resting_point 6 is the crossing.

**Mending** (operations.py:443-611; C11 §4.5): costs 0 Coherence at every degree; on non-Failure it hands the **mender**
a restorative term (1 at Relational/Field, 2 at Structural/Foundational, CHECKED :471-491) applied as elastic return if the
caller says the environment is in equilibrium. Aimed at the mender's own configuration (`configuration_of = 'self'`) it
instead lowers resting_point by 1 on Success/Overwhelming. Being mended by another is not routed (:561-563): it moves
nothing of the target. Documented gap (:159-167): free attempts "can walk a permanent set to 0", against canon C-1's
"extremely difficult". Net effect as coded: Mending is a working that pays its worker.

**Collective** (collective.py:71-229; C11 §4.7): rank by TS; Anchor = highest. Every participant rolls a full Leap
(own cost). Anchor Leap failed → no lattice. Pool = Anchor's solo pool + Σ `max(0, cognition // 2)` over helpers whose Leap
succeeded; `lattice_fractured` if pool < half the all-helpers pool → Ob +1. One roll; every successful participant is
charged the scale cost (−1 more on Partial/Failure). `op_type` only selects `MENDING_OB` vs `DEPTH_OB`: no FR surcharge,
no POP −1 in collective form. Collective Mending aimed at own configuration raises.

**Opposing** (opposing.py:102-269; C11 §4.8): each side's Ob = base + `max(1, opponent_TPS // 2)`; both roll; degrees
folded to Meets/Partial/Failure; a 9-branch table (docstring says "6 rows") yields outcome text, MS delta, and per-side
coherence, composure and knot-strain consequences (loser composure 2, or 4 for Locking/Dissolution). Partial/Partial
rolls `d6 ≤ 2` for a "Shifting Object one scale below". Only Coherence is written; composure, knot strain and MS are
reported.

**Co-movement** (co_movement.py; C11 §4.9): a 15-card deck (CM-01 Temporal Drift … CM-15 Dissolution Wake), each card with
an actualised and unactualised MS delta and text; actualised iff depth is not Object/Personal; reshuffles when empty.
Card effects are text only (`apply_comovement_effects` STRUCK); CM-16..18 not implemented.

**Threadcut** (threadcut.py; C11 §4.10): a registry of beings outside Coherence; each external operation by one adds
rendering strain 1; strain ≥ max_wounds or wounds ≥ max_wounds // 2 advances a deactualisation round 1→3, whose
Ob penalties (+2, +4) appear only in note text. Perception of a threadcut being is banded by observer TS (< 10 "nothing
or vague unease" … ≥ 70 "full perception").

**Rendering** (rendering.py): docstring only; `apply_rs_strain`, `check_calamity_threshold` STRUCK at plan position 27.

**Outputs**: `OperationResult`, `CollectiveResult`, `OpposingResult`, `CoMovementCard`, threadcut dict. The only state
written: the Coherence store, the deck store, the threadcut registry.

### 3 In the whole game

**Who invokes it today.** Nothing in the game. Importers of `systems.threadwork` outside the package are five test files
and one lazy, exception-swallowing import in `systems/fieldwork/sim/knots.py:375` (knot rupture charges −1 Coherence),
which itself is imported only by `engine/tests/test_knots_ed912.py` (CHECKED by grep; C11 §6). No file under
`engine/season/` imports threadwork, knots or `systems.fieldwork.sim`. Running `headless.run(seasons=2, seed=3)` and
`populated.run(seasons=1, seed=3)` loads no module whose name contains `threadwork` or `knots` (RAN, §7).
`modules/mass_battle/orchestration.py:333-335` `threadwork_check` is an empty hook ("threadwork lands in a future cycle
(G-9)"), called every phase boundary (:346) and doing nothing (CHECKED).

**What the season loop holds for it** (all data, none executed as threadwork):
- `verb_table.yaml:1410` `thread_read`: stratum `contested_physical`, `requires: "Thread Sensitivity >= 30"`,
  `requires_typed: none`, `writes: []`, emits `finding.made` / `finding.none`; the decline note records that the TS gate has
  no carrier (H-85) and that co-movement and the Coherence cost "ARE NOT EXPRESSED HERE" (CHECKED). It is **not** in
  `resolvable_verbs()` (RAN: False, of 47) — so `thread_read` is DESIGN-ONLY in the loop despite having a row.
- `write_matrix.yaml:185-193` `(Person, coherence)` at RES, class ACTS, emits `coherence.changed`, `unproduced`: "only an act
  may write it and the verb table carries none that does" (CHECKED). `world.py:1010-1019` refuses that write from any
  driver but "Seam" (CHECKED). `carriers.py` `Person` has no coherence or sensitivity field (L13 §7 spot-check).
- `rosters.yaml:2390` `threadwork: {kind: loop_resident, home: "systems/threadwork/"}` — a label, nothing reached from it (CHECKED).
- `rosters.yaml`: knowledge kinds `[mundane, thread_substrate]` (H-85 default); conviction `thread_truth` with sign-only
  `thread_read` cells (e.g. `solmund_orthodoxy: thread_read: -1`) (C11 §6; L13 §7).
- `requirements.yaml:44-48`: the scale column of Base Ob is ruled "THREAD-ONLY AND IS NOT A GENERAL OBSTACLE SOURCE
  (Jordan, 2026-09-05)" (C11 §6).
- `hole_register.yaml` H-85 (TS: no carrier, no predicate), H-47 (Coherence: "absent").

**What the lexicon would wire** (L13 §5, roster governs; D04 §TW 7 verbs; all PROPOSED)

| verb | status | would read | would write | waits on |
|---|---|---|---|---|
| `thread_read` (hosts `trace`, `diagnose`) | SHIPPED row, REBUILD | TS gate; Leap stage pool | Claim at WITNESS in own ledger; knot via Leap; −1 Coherence at Relational+, +1 Exposure (canon) | M2, M1, M3, FI-G01 |
| `weave` | NEW | TS, scale (breadth to formation/region) | `(Person, coherence)`; held-load Tenure `weave` while held; knot; strain for IN-35 | M1, M2, M3, M5, M6 |
| `pull` (+ past-pulling) | PARKED | target's ledger, recency | displaced-claim deposit, append-only (K-WR-2) | M9 (P-09 orphan carrier) |
| `lock` | NEW | target, `Site.condition` | Tenure `lock` read as a write refusal; for a Site, a Locked Zone ("becoming precluded") until mended | M1, M2, M3, M6 |
| `dissolve` (renamed from `sever`, R-10) | NEW | target | target ended (`Site.condition` to floor; held shape closed destructively); residue mark | M1, M3, M6, M10 |
| `mend` (hosts `heal`; R-26) | NEW | target by kind | closes a lock / another's weave; raises lattice `Site.condition` via `_rise`; target resting point; `Person.body`; mender's elastic return | M1, M5, M6, M7 |
| `ward` | NEW, build-gated | hostile op's target | Tenure `ward`, Term one season; hostile ops routed to `opposing.py`; warder pays | M8; ships with first loop-executed hostile operation |
| `knot` (split from `tie / knot`, R-02) | REBUILD | Disposition ≥ 5, Bonds ≥ 5, either TS ≥ 30; TN 7, Ob 2 | directed knot Tenure; strain −5..+5, rupture at 5 | M3, H-182, ED-912 |

Folded: `leap` (a stage of every operation, not a verb; owns the TS gate, the Leap roll and an involuntary knot
[ASSUMPTION]), `trace`, `diagnose`, `heal`, `past-pulling`, `loosen` (own → `release`, another's → `mend`). Culled: `sever`
(as a name), `anchor` (equilibrium is a fact supplied to `recover`). Tally 8 rows (5 NEW, 1 PARKED, 2 REBUILD), 6 folded,
2 culled (L13 §2 claim 25). The twelve mechanic gaps M1-M12 (L13 §6): M1 thread-operation seam, M2 TS carrier + gate,
M3 knot, M4 cells/heresy, M5 Calamity coupling (IN-35), M6 held shapes, M7 Mending routing, M8 opposed routing,
M9 P-09 orphan, M10 residue, M11 Leap vulnerability window, M12 three-dimension effects. D05's actor-class table lists
THREAD-WORKER (`weave`, `lock`, `dissolve`, `mend`, `ward`, `knot`, `thread_read`) as "stubs, R-C-18", writing
`(Person, coherence)` via the seam; `mend` is "the canonical act that lowers the Calamity" (D05:202).

**Designed cross-system links (none executing)**: Calamity (IN-35: live `weave`/`lock` loads and residue as territorial
strain, `mend` holds the balance — L13 §4.3); mass battle (Formation+ breadth hand-off of `weave`/`lock`/`dissolve`/`mend`,
TW-G30 PARKED; empty `threadwork_check`); fieldwork/social (knots; `thread_read` as an inquiry that yields findings, R-13
TW owns it, FI supplies the finding shape); convictions (orthodoxy cells on witnessed threadwork).

**Feedback loops, as coded**: one only — workings displace the worker; equilibrium rest and Mending return elastic
displacement; Mending also lowers resting point when self-aimed. Because `recover` needs a caller to supply `seasons` and
the environment, and no season-loop clock calls it, the loop closes only inside a test. The designed loops
(weave strain → Calamity → Mending; knots → strain → rupture → Coherence) are DESIGN-ONLY.

### 4 Built vs designed

| element | grade | evidence | what the proposals say should exist and does not |
|---|---|---|---|
| Pool / TN 7 / degree ladder | TESTS-ONLY | operations.py:235-247; `test_degree_ladder_single_owner.py` | history term fix (REM-45) |
| Leap (solo) | TESTS-ONLY | `attempt_leap` called only by collective.py:116 and tests | one owner for the stage every operation passes (TW-G20); TS carrier on Person (M2); involuntary knot (M3) |
| Weaving / Pulling / Past-Pulling | TESTS-ONLY | `test_threadwork_resilience.py`, `test_coherence_elastic_plastic.py` | held-load Tenure (M6); displaced-claim deposit (M9) |
| Locking / Dissolution | TESTS-ONLY | same tests | Tenure `lock` as write gate; target end + residue (M6, M10) |
| Mending (solo) | TESTS-ONLY | `engine/tests/test_thread_mending_ed871.py` (CI `sim-regression`), parity tests | target-side writes (M7); lattice Site (M5); own-aim difficulty (`[GAP]` :162) |
| Coherence elastic/plastic store | TESTS-ONLY | `test_coherence_elastic_plastic.py` | `(Person, coherence)` carrier and an act that writes it (H-47, M1); elastic-return clock or rest verb (§3.9 item 1) |
| Resilience resist (R-14) | TESTS-ONLY | gain 0 shipped = identity | ruled gain |
| Collective lattice | TESTS-ONLY | `test_threadwork_mending_parity.py` | — |
| Opposing operations | TESTS-ONLY | parity tests | `ward` routing (M8); composure/knot/MS writes |
| Mending-Stability delta | DESIGN-ONLY (reported value) | operations.py:211-213 | Calamity effect "must be the lattice write, not that report" (L13 §4.3) |
| Co-movement deck | DESIGN-ONLY (code present, no caller and no test) | grep: `draw_comovement_card` appears only in its own file | card effects; CM-16..18 |
| Threadcut | DESIGN-ONLY (code present, no caller and no test) | grep: `resolve_threadcut_interaction` only in its own file | Ob penalties applied to rolls |
| Rendering strain / Calamity threshold | DESIGN-ONLY | rendering.py docstring; STRUCK | IN-35 |
| Knot rupture → Coherence | TESTS-ONLY | knots.py:375 via `test_knots_ed912.py` | directed knot reader (TW-G34), strain carrier (ED-912) |
| `thread_read` verb | DESIGN-ONLY in loop | row exists; not in `resolvable_verbs()` | M1-M3, H-85 gate |
| `weave`, `lock`, `dissolve`, `mend`, `ward`, `knot` (TW form), `pull` | DESIGN-ONLY | no verb rows (grep of verb_table) | all of §3 table |
| MB `threadwork_check` | DESIGN-ONLY (empty hook, executes as `pass`) | orchestration.py:333-335 | TW-G30 |

### 5 Structural handles for comparison

- **Resolution style**: dice pool, count-successes with signed faces (1 = −1, 10 = +2), fixed TN 7, variable Obstacle;
  four-degree outcome by margin. Opposed form is two independent rolls against cross-modified Obs, read off a lookup table.
  Collective form is pooled dice with a pass/fail entry roll per participant.
- **Granularity**: single act (one working, one roll). Scale is a property of the target (Object → Foundational), not of
  the scene; it sets Ob and cost.
- **Scale**: personal in code; designed to reach Site, territory (Calamity) and formation (mass battle) through the verb
  layer, none built.
- **State model**: one persistent resource per practitioner with two components — a recoverable (elastic, capacity 6) and a
  permanent (resting point) displacement, plus a one-way failure threshold. Price is paid on use, increases with scale and
  with poor results. No spell list, slots or mana pool; difficulty and cost are derived from target scale.
- **Agency model**: the caller (a test) chooses actor, operation and target; in the designed game the practitioner chooses
  via verbs; there is no GM, the engine resolves (CLAUDE.md head).
- **Information model**: code is fully transparent (returned dataclasses). Designed: TS gates both access and perception
  (`thread_substrate` knowledge kind, threadcut perception bands), so the same world reads differently by actor class.
- **Failure/recovery model**: failure costs more Coherence (−1) and moves MS; recovery is elastic-only by rest in an
  equilibrium environment or by Mending's return; permanent set is recoverable only by self-aimed Mending, and not at all
  past the crossing.
- **Content model**: authored tables and a fixed 15-card authored deck; no generated content.
- **Pacing**: designed season-scale (elastic return 6 per season; Ward Term one season); as coded, time passes only when a
  caller passes `seasons`.

### 6 Open design decisions the sources name

- §3.9 item 1 / K-WR-8 / TW-G29 / D-V19: how elastic return enters the season loop — "A licensed clock on the being …, or
  the effect of a rest a person chooses"; `write_matrix.yaml:176` calls Layer 1's three clocks "exhaustive" (L13 §6).
- §3.9 item 2 / D-V19: are knots permanent? Canon "cannot voluntarily unmake" vs `release`'s domain, which already includes `knot`.
- §3.9 item 3 / K-WR-5 / TW-G11 / D-V19: what follows the crossing (P-15 requires a consequence; no document gives its shape).
- H-85: TS carrier, roster and predicate (default two-valued knowledge kinds; sweep thread_only / two_valued / per_subject).
- H-47 / H-62: no act writes `(Person, coherence)`.
- IN-35: Calamity coupling (unbuilt); R-26 re-points its Mending arm to `mend`.
- Own-aim Mending difficulty/cost/cadence (`[GAP]` operations.py:159-167; carried in HANDOFF_WR.md).
- R-14 resilience gain (0 / 1 / 3), "UNRULED" (operations.py:149-157); H-94 fixture precedent.
- REM-45 / PP-624: history term `min(3, history + 3)` vs `min(3, history) + 3`.
- C-TW-3 / ED-WR-0005: blanket Partial/Failure −1 hitting the Leap.
- Parked gaps: TW-G21 (Leap vulnerability window, M11), TW-G30 (Thread→Mass), TW-G36 (V-2a attribute input),
  TW-G14/G15 (`pull`, past-pulling). Out of scope: TW-G42 ("TS is fixed (J-T4); `train` cannot raise it"), TW-G26, TW-G27.
- Gap tally TW: 42 = closed 29 · PARKED 6 · OUT OF SCOPE 5 · STALE 2 · DISPUTED 0; of the 29, "none executes today" (L13 §2 claims 26-27; D04 gap table).

### 7 Conflicts, uncertainties, checks made

**Conflicts**
1. L13 (claim 15) says no operation calls `attempt_leap`. False for the collective path: collective.py:116 calls it for
   every participant (L13 §7 spot-check; CHECKED). True for the six solo entry points.
2. L13 §4.1 says a Leap Failure "ends with no Coherence cost (`operations.py:355-356`)" — that is the docstring. Code: the
   TS < 30 eligibility Failure costs 0, but a rolled Leap Partial/Failure costs −1 via the blanket penalty (CHECKED
   :321-323, :370-372). I believe the code; the authors name it as defect C-TW-3.
3. L13 claim 9 ("calamity|lattice" grep in `engine/season/**/*.py` returns two test files) — the L13 extractor found no
   files. Not re-run by me; either way nothing in the loop couples to a Calamity.
4. L13's `verb_table.yaml` / `rosters.yaml` line cites are offset from HEAD (L13 §7). I used HEAD lines.
5. Opposing docstring "6 rows" vs 9 code branches (C11 §4.8).
6. D05 calls the THREAD-WORKER verbs "stubs"; at HEAD only `thread_read` and `tie / knot` have rows (grep of verb_table:
   no `weave`/`lock`/`dissolve`/`mend`/`ward`/`pull` rows). "Stub" there means designed, not coded.

**Uncertainties**
- The grade vocabulary has no slot for code with neither a caller nor a test (co-movement, threadcut); I graded them
  DESIGN-ONLY because nothing executes them.
- `attempt_leap` defaults `ts` to 0 while `_actor_pool` defaults it to 30: a caller omitting `.ts` fails the Leap but pools as TS 30.
- Canon files (`06_operations.md`, `07_drift.md`) not opened; canon quotations are as L13 and the code comments give them.
- C11 did not read the threadwork test bodies; test coverage claims rest on names and importer greps.

**Checks** (HEAD a4ca9a5)
- CHECKED grep for `systems.threadwork` importers repo-wide: only `engine/tests/test_thread_mending_ed871.py:26`, four
  `tests/valoria/` files, `systems/fieldwork/sim/knots.py:375`, and a docstring at `systems/fieldwork/__init__.py:7`.
- CHECKED `engine/season/**/*.py` (non-test): no threadwork/knots import; only `world.py:1010-1019` names coherence.
- RAN `headless.run(seasons=2, seed=3)` and `populated.run(seasons=1, seed=3)`: `sys.modules` contains no `threadwork`
  or `knots` module afterwards — the absence claim observed, not inferred.
- RAN `resolvable_verbs()`: `'thread_read' in r` → False (47 resolvable).
- CHECKED systems/threadwork/sim/operations.py:235-247 (pool), :321-336 (blanket −1, MS), :351-372 (Leap), :397-414
  (Past-Pulling), :471-491 (`price_mending`).
- CHECKED systems/threadwork/sim/collective.py:112-118 (`attempt_leap` per participant), :156-161 (fracture rule).
- CHECKED systems/threadwork/sim/coherence.py:113-133 (constants), :320-334 (stress arithmetic).
- CHECKED engine/season/verb_table.yaml:1410-1424 (`thread_read`); write_matrix.yaml:185-193; rosters.yaml:2390;
  modules/mass_battle/orchestration.py:333-346; hole_register.yaml:1052-1060 (H-85).
- CHECKED grep: `draw_comovement_card`, `resolve_threadcut_interaction` have no caller outside their own files.

---

<!-- ===== A5 (S5_governance_factions.md) ===== -->

# A5 · S5 — Settlements & Governance (GV) and Faction Actions (FA)

Stage-2 synthesis. Sources: extracts C12, C06, L14, L15 (read in full); C03, C04, C13, D01, D02 (skimmed for carriers,
decision reach, hunger, remediation). G19/G20 gap extracts **do not exist** in `extract/` at time of writing (only G21);
section 6 of each block is built from the lexicons' own open-item tables (L14 §6, L15 §6) instead. Repo HEAD `a4ca9a5`.

**Grading convention used here (stricter than "wired").** An effect body registered in `EFFECTS` is *reachable* from
`engine/season/loop/driver.py` via `resolve`, but reachable is not executed. I grade **RUNS-IN-LOOP** only where the
behaviour executed in a normal season of the authored realm, or is a barrier step (MATTER, CENSUS) the driver always calls
(`driver.py:447-448`, `:514`, CHECKED). A verb that is wired but measured at **0 executions** is graded **TESTS-ONLY** when
named tests exercise it, else DESIGN-ONLY, with its attempt/refusal count shown.

**Measurement P1 (my run, read-only, in memory):** `build_realm(0)`, `SeasonDriver.season` × 2, the chooser built exactly
as `harness/populated.py::run` (:1522-1546) builds it; events attributed to the causing act through `Event.causes[0]`.
Script: `s5/probe.py`; 28 s wall.
`git status` clean afterwards. Results quoted below as "P1". One seed, two seasons; no control arm was needed because
the claim is a count of what executes, not a comparison.

| verb | attempted | executed (success event) | refused | | verb | attempted | executed | refused |
|---|---|---|---|---|---|---|---|---|
| confer | 0 | 0 | — | | dispatch | 18 | 6 `order.given` | 12 |
| establish | 0 | 0 | — | | issue | 6 | 5 `dispensation.issued` | 1 |
| oblige | 0 | 0 | — | | covenant | 13 | 0 | 13 |
| revoke | 6 | 0 | 6 | | seize | 0 | 0 | — |
| release | 45 | 3 `tenure.closed` | 42 | | sabotage | 34 | 0 | 34 |
| convene | 1 | 0 | 1 | | survey | 57 | 13 `faction.surveyed` | 44 |
| requisition | 2 | 0 | 2 (`.unauthorized`) | | march | 21 | — | 25 `march.refused` |
| transfer | 45 | 1 `transfer.made` | 44 | | migrate | 81 | 0 `residence.changed` | 81 |
| found | 24 | 0 | 24 | | move | 42 | 16 `travel.moved` | — |
| build | 19 | 0 | 19 | | work | 77 | 0 `site.worked` | 77 `work.unavailable` |
| restore | 23 | 0 | 23 | | (MATTER) | — | 111 `stores.changed`, 74 `yield.taken`, 75 `term.matured` | — |

This agrees in direction with D01 item 9 (E-14: `restore` 0/27, `migrate` 1/118, `transfer` 1/47, `found` 0/24, `build`
0/19, `work` 0/82, "no settlement-management verb executes") and L14 claim 10 (`requisition`, `revoke` "execute 0 times in
computed play"). P1's `migrate` is 0/81 against D01's 1/118 (different run length or HEAD); I believe P1 for HEAD `a4ca9a5`.

### How the two subsystems are represented — there is no Faction, Settlement or Province class

Per C03 §2 (line 25): *"No `Faction`, `Settlement`, `Province` class exists"*, and C12 §3: *"No Faction, Settlement,
Treasury, Tax, Law or Trade class exists in this scope."* Every polity concept is a composition of five carriers:

| concept | representation | cite |
|---|---|---|
| settlement, province, duchy, realm, hearth (building), community (quarter), person | a `Rung` (one class, "THE HOLON. Eight kinds, ONE type") with `kind ∈ RUNG_KINDS = (person, hearth, community, settlement, territory, province, duchy, realm)`, joined into a ladder by `contain` Tenures (child→parent, must ascend) | C03 §3.2 Rung; C03 `add_tenure`; C06 §5b |
| what a place owns | `Rung.stores {matter kind: int}` and `Rung.yield`; `__setattr__` refuses any social aggregate: *"no norms, no densities, no reputation, no unrest, no legitimacy. EVERY ONE IS A QUERY"* | C03 §3.2; C12 §3 |
| buildings that produce or house | `Site(id, rung, kind, condition)`, `kind ∈ {harbour, seam, body, dwelling, garrison}`, `condition` on `condition_scale = 1000` | C12 §3, §4.9 |
| office / seat | `Office` (a `SeatId`): `post, rung, remit_acts ⊆ {issue, determine, confer, revoke, dispatch, convene}, conferral ∈ {appointed, elected, annex, None}, revocation ∈ {rung_above_same_faction, rung_above_in_holdings, None}, upkeep, body, faction` (faction derived from `body`) | C03 §3.2 Office; C12 §3 |
| holding a seat or a place | a `hold` Tenure Person→Office/Rung/Record/Proposition; `payload` snapshots `remit_acts` (`granted_acts`) | C03 §3.2 Tenure; C03 `_grant_remit` |
| faction | a `Proposition` (id `fac_<slug>`, e.g. `'Crown'→'fac_crown'`) plus the live `commit` Tenures pointing at it; a `faction_sheet` Record kind exists for the `survey` snapshot | C03 line 25; C12 §2 (`world_q.py:1338`); `world_q.py:1365` CHECKED |
| faction membership | live `commit` to the faction Proposition — *"THIS IS THE WHOLE OF MEMBERSHIP AND THERE IS NO SECOND ROUTE"* | `world_q.py:1365-1376` CHECKED |
| service to a seat | live `oblige` Tenure Person→Office (with an optional `Term`) | C12 §4.4 `oblige`; L15 C6 |
| treasury | `Rung.stores` at the Office's own `rung` | C12 §3 (effects_governance.py:427-430) |
| war | a `Proposition` of `mood == "WAR"` whose `{subject, value}` is the pair, with any live `commit` — a Query, no stored flag | C12 §4.10 `at_war` |
| a faction "view" | `faction_q.Faction(proposition, members, holdings, seats, head)`, a frozen dataclass *"built at a barrier, handed on, dropped at the next — NEVER a member of `World`"* | C12 §2 (faction_q.py:84-95) |
| population | `Person.weight`; *"A COHORT IS A PERSON AT weight > 1"*; `population(w, rung)` sums `weight` over live `reside` edges in the subtree | C12 §3, §4.7 |

The world the loop runs on (C06 §5a, `build_realm(0)`): rungs `{realm 1, duchy 3, territory 17, settlement 37, community
60, hearth 211, person 83}`; persons 83 (46 cast + 37 cohorts of weight 2); sites 322; offices 32; 9 `fac_*`
Propositions (8 canon factions + test `faction x`). P1 after two seasons: 24 live `hold`s on Offices (of 32), 31 live
`commit`s to `fac_*` spread over 7 factions (Crown 9, Church of Solmund 6, Varfell 4, Guilds 4, Löwenritter 3,
Hafenmark 3, Restoration Movement 2; Schoenland and `faction x` none), and **0 live `oblige` edges**.

---

## Settlements and Governance (GV) — a seat/rung/site ladder whose seasonal economy (MATTER) RUNS-IN-LOOP, while almost every governance verb is wired but executes 0 times in the realm (TESTS-ONLY); taxation, law, public decree, hunger and custody acts are DESIGN-ONLY

### 1 What it is

GV is the place-and-office layer: an eight-rung nested ladder from a single person up to the realm, physical Sites on
the rungs that yield and wear, larders that people eat from, and Offices (seats) anchored to rungs whose holders may
appoint, remove, convene, requisition and pay. The player-facing fantasy it serves is *"rule a place"*: hold a seat,
fill seats beneath you, move stock between larders, found and build, and watch a settlement feed or starve. In the
engine there is no GM and no settlement object: a settlement is a `Rung` of kind `settlement`, its people are cohort
`Person`s with `reside` edges, and its government is whoever holds a `hold` on an Office anchored at or above it
(C12 §3; C03 line 25).

### 2 Operating alone

**Entities and state.** `Rung`, `Site`, `Office`, `Person` (cohorts), `Tenure` kinds `hold, oblige, contain, reside,
ban, detain, succeed, tie, knot, commit`, `Record` kind `works` (a plan) and `dispensation` (a writ), `w.dates` (sittings)
(C12 §3; C03 §3.2). Authored data: `offices.yaml` 31 seats (title→domain ruling: King/Queen→realm, Duke/Duchess→duchy,
Count/Countess→province, Lord→territory, Mayor→settlement, Community Leader→community, Family Head→hearth); conferral
counts appointed 17 / elected 8 / None 6; revocation None 16 / `rung_above_same_faction` 13 / `rung_above_in_holdings` 2
(C06 §5c). `cohorts.yaml` 37 rows `{rung: S-NNN, weight: 2}` (C12 §4.7). `governance_spine.yaml` is a 13-rung test
ladder, *"A TEST FIXTURE, NOT CANON"* (C12 §4.11).

**The seasonal procedure (MATTER, every season, actorless; C12 §4.2):**
1. Record-stage maturation (works stages due this tick mature if a live `hold` holder exists).
2. Tenure term maturation: every live Tenure with `term.matures_at <= tick` closes (`until = tick`), *"whether or not
   anyone remains to pay"* — this is how an unpaid `oblige` lapses.
3. Larder draw: `subsistence_draw` — only cohorts eat (ED-IN-0255); `want = subsistence_weight[k] × weight`
   (`grain 2, salt 1`); food taken from `nearest_store` walking up the `contain` ladder; `take = min(want, held)`.
4. Shortfall: a drained larder's `stores.changed` write carries `Observation(src, shortfall:k, deficit)`.
5. Body fall: `lost = body_step × units short`; `body_step = 0` shipped (*"control: no body ever falls"*).
6. Bodies clock: `body_hazard` from `illness_rate` and `age_step`, both 0.0 shipped; cohorts exempt.
7. Per rung: apply draw, then yield: for each Site, `int(base × condition/1000 × season_factor)`;
   `SITE_YIELD = harbour {grain 40, salt 30}, seam {ore 50, timber 10}`; `season_factor = 1.0`, draw table empty.
8. Travel legs clear; Site wear (`harbour 10, seam 10, body 10, dwelling 0, garrison 0` per season), band-floor
   crossings emitted (`harbour {bulk_shipping 800, fishing 100}`, `seam {deep_mining 700, surface_gleaning 50}`).

**CENSUS** (C12 §4.3): individuates a person only when an act's refusal emitted `person.demanded` (a `dispatch` naming
an id the world lacks); the new person gets a `contain` edge but no `reside`, so *"counts in no rung's population"*. No
births, no growth.

**Verbs (effects in `loop/effects_governance.py`, `effects_economy.py`, `effects_founding.py`, `effects_migration.py`;
C12 §4.4-4.7):**

| verb | gate (who may) | what it writes | resolver |
|---|---|---|---|
| `confer` | `remit:confer` via a seat whose purview reaches the office, `may_fill`; refused if the conferee is under `ban` | opens conferee's `hold` (optional `term ≥ 1`), closes prior holds | deterministic |
| `revoke` | `may_revoke` under the office's revocation basis | closes holds; if conferral was `appointed`, opens a permanent `ban` on the ex-holder (`REVOCATION_DISPOSAL`, `state/gate.py:599`, CHECKED) | deterministic |
| `establish` | `remit:confer` | new Office, or re-remit an existing one (re-stamps live holds) | deterministic |
| `release` | own edge only (`T-m`), kinds `{tie, hold, succeed, commit, knot, oblige}` | `Tenure.until` — resign, abandon | deterministic |
| `convene` | a seat (`Act.via`) | a `w.dates` sitting `{venue, holder, due_at}`; what the sitting decides is not here | deterministic |
| `oblige` | `own` (the joiner's act) | `oblige` Tenure to a seat with `Term(tick + oblige_term)`, `oblige_term = 4` | deterministic |
| `requisition` | `remit:issue`, purview reaches rung, stock ≥ amount | `Rung.stores` subject − / seat's rung + (conserved) | deterministic |
| `transfer` | `remit:issue`, `own`, `hold:<store>` | `Rung.stores` ×2; if paid THROUGH a seat to obligees' home, renews their `oblige` terms (one term per `upkeep_of`, `default_upkeep = 1`) | deterministic |
| `work` / `restore` / `sabotage` | presence at the Site | staged `Site.condition` ± ; rise = `headroom × 1/n` (n = persons present), fall = `condition × 1/n` `[ASSUMPTION]` | deterministic share |
| `found` | holder of a `works` Record whose plan is a rung kind | new `Rung`, `contain` to parent, founder's `hold`, stake moved from payer (`works_cost` e.g. `hearth {grain 10}`) | deterministic |
| `build` | holder of a `works` for a Site kind | new `Site` at condition 0, cost consumed (`dwelling {timber 10}` etc.) | deterministic |
| `migrate` / `move` | not detained; destination ascends the ladder; `migrate` refuses a newcomer when `population + weight > capacity` (`capacity = max(1, dwellings in subtree)`) | `contain` legs (+ `reside` for migrate) | deterministic |
| `dispatch` | `remit:dispatch` | **nothing** (`writes: []`, `verb_table.yaml:380`, CHECKED); emits `order.given` | — |

No dice: every GV effect is a deterministic state write gated by a three-valued typed precondition (`AllOf`, "FALSE
DOMINATES UNKNOWN"; an unevaluable precondition refuses; C06 §4b). The only stochastic elements are the person's
choice of act (sampler at `choice_temperature 0.1`, C06 §5j) and the off-by-default weather and body-hazard draws.

**Outputs.** Events `tenure.opened/closed`, `office.established`, `remit.changed`, `date.scheduled`, `duty.taken`,
`requisition.taken`, `transfer.made`, `term.renewed`, `site.*`, `rung.founded`, `residence.changed`, `stores.changed`,
`yield.taken`, `body.changed`, `person.died`, `condition.band_crossed` (C12 §5).

### 3 In the whole game

- **Who invokes it.** Persons only; *"a faction never acts: a PERSON HOLDING AN OFFICE acts"* (C04, `verbs.py:122-127`).
  Seat acts are admitted when a live `hold`'s `granted_acts` contains the remit (`options.py:594-622`, C04 item 2).
  Verb scales: `confer`, `establish`, `requisition` at `settlement`; `dispatch` at `territory`; `issue` at `province`
  (C04 line 115, 133-152).
- **What it reads.** The rung ladder (`ancestry`, `descendants`), `purview_reaches` (own rung + descendants, plus one
  `oblige` edge deep since IN-40), Site condition, `Rung.stores`, fixtures (C03 gate notes; C12 §4.10).
- **Who reads its outputs.** (a) The decision layer: a seat-holder's attention tier 1 is *"referent in p's own tenure
  objects / seat purview"* (C04 `attention_key`); (b) the witness `SEAT_CHANNEL` deposits shortfall claims into
  `governors_of` the drained rung, and `decision/options.py::_from_shortfall_claim` forms a `transfer` from that claim
  (C12 §6) — the designed **governor feedback loop: larder drains → seat-holder learns → pays relief**; it fires only in
  `harness/scarce.py` because *"no shipped world drains a larder with a mouth unfed"* (C12 §7; matter.py:463-468);
  (c) mass battle reads `fortification_of` (garrison condition), `holder_faction_of`, `mustered` (C12 §6);
  (d) `migrate` reads `capacity` (dwellings).
- **Feedback loops present in code:** yield→stores→draw (runs each season); dwelling count→capacity→migration refusal;
  `oblige` term→lapse unless `transfer` renews (upkeep); Site wear→band crossings. **Loops present only as design:**
  population↔hunger↔bodies (REM-50/51/52, D02 §4.1), tax/legitimacy (L14 M-TAX, `f(L) = 1` until IN-23).
- **Measured scale effect (D02 §4.1, P03:233-240):** realm cover after season 0 / 1 is 21.7 / 41.7 seasons of food at
  every settlement; all 37 cohorts are short only in season 0 (before first yield); capacity caps a home at 4-9 (median
  6); weight ×10 still records 0 shortfall after season 0. *"Population cannot drive hunger until the ratio is set
  (JQ-6)."*

### 4 Built vs designed

| element | grade | evidence | what the proposals say should exist and does not |
|---|---|---|---|
| Rung ladder, `contain`, Sites, `Rung.stores` | RUNS-IN-LOOP | built by `build_realm`; read by MATTER each season (C12 §4.2) | `Rung.envelope` has no producer; `Rung.sites/records/dates` zero readers (C12 §7) |
| MATTER larder draw + yield + wear + term maturation | RUNS-IN-LOOP | `driver.py:448` CHECKED; P1: 111 `stores.changed`, 74 `yield.taken`, 75 `term.matured` | labour input to yield ("no labour term", L14 §4.0 L60/L67; M-LABOUR) |
| hunger → body fall | RUNS-IN-LOOP but inert | code runs; `body_step = 0` shipped, so no body falls (C12 §4.9) | REM-52: ship `body_step = 10` [ASSUMPTION; revert 0] (D02 §4.1) |
| shortfall observation; governor shortfall claim → `transfer` | TESTS-ONLY | fires only in `harness/scarce.py`; `test_in22_shortfall_reach.py` (C12 §7, §8) | REM-51 hunger band beside shortfall on the same write |
| settlement `hunger(w, S)` Query, bands `starving/hungry/lean/fed` | DESIGN-ONLY | `rg hunger engine/season/state` no field (D02 §4.1) | REM-50: `cover = A/D`, `unmet = (D−G)/D`; defaults `starving` if unmet > 0, `hungry` if cover < 1, `lean` if cover < 2 [ASSUMPTION; JQ-6] |
| `confer`, `establish`, `oblige` | TESTS-ONLY | wired; P1 attempted 0; tests `test_obligees.py`, `test_term_upkeep.py`, g3/g4 (C12 §8) | H-203 office referent in computed play (L14 §6) |
| `revoke`, `convene`, `requisition` | TESTS-ONLY | P1 6/0, 1/0, 2/0 (attempted/executed) | H-91 reachable remit, H-100/IN-31 revocation cost (L14 §6) |
| `release` (seat or other edge) | RUNS-IN-LOOP | P1 3 of 45 close a Tenure | M-RESIGN: own `seat.resigned` kind (L14 §5.1) |
| `transfer` incl. upkeep renewal | RUNS-IN-LOOP (barely) | P1 1 of 45 `transfer.made`; 0 `term.renewed`; 0 live `oblige` | "No computed act forms an `oblige` payment" (C12 §7) |
| `found`, `build` | TESTS-ONLY | P1 24/0, 19/0; `test_works_founding.py` | in-act plan (one step instead of `create_record` + `build`), computed works source H-165 (L14 §4.6) |
| `work`, `restore`, `sabotage` | TESTS-ONLY | P1 77/0 (`work.unavailable`), 23/0, 34/0 | REM-22 `referent_class: Site` (D02 §Governance) |
| `migrate`, capacity | TESTS-ONLY | P1 81/0; `test_migrate_capacity.py` | REM-29 `room` stem so a refused migrant learns (D02) |
| `move` | RUNS-IN-LOOP | P1 16 `travel.moved` | — |
| `dispatch` (order) | RUNS-IN-LOOP, writes nothing | P1 6 `order.given`; `writes: []` | REBUILD as posting of an obligee (L15 S5); rename to `order` held (L14 R-05) |
| `issue` (writ) | RUNS-IN-LOOP | P1 5 `dispensation.issued` | H-203 writ reaching executor; H-44 terms (L14 §5.1) |
| CENSUS individuation | TESTS-ONLY | P1 0 `person.individuated` | individuated persons get no `reside` (H-51) |
| `succeed` | DESIGN-ONLY | row exists, effect declined (`verb_table.yaml:1096-1113`, L15 §7.2 item 2) | IN-61 rebuild: heir claims throne under `inheritance` |
| `exchange` (barter) | DESIGN-ONLY | row, no effect (C12 §7) | — |
| `tax`, `ration`, `proclaim` (one `edict` Record kind) | DESIGN-ONLY | no row; `levy` "ruled deleted" (`world_q.py:1124-1127` CHECKED) | M-EDICT, M-TAX (MATTER moves `amount × yield` to seat treasury; `defy` withholds, `evade` reduces), M-DRAW (L14 §4.3-4.4) |
| `evade`, `defy` (split of slash row) | DESIGN-ONLY | slash row `evade / defy` exists, no effect (C12 §7) | split + M-TAX readers (L14 §4.2) |
| `arrest`, `pardon` | DESIGN-ONLY | `detain`/`ban` kinds exist and have readers (detained cannot `move`/`migrate`) | IN-12 step 5 (L14 §4.5) |
| `raze`, `abolish`, `depose`, `patrol`, `assess`, `charter` | DESIGN-ONLY / PARKED | absent | IN-12 step 11 re-housing; D-V1; disorder quantity (L14 §5.1) |
| Parliament, title delegation, settlement council shapes | DESIGN-ONLY | *"RULED AND NOT BUILT, H-90"*; delegation *"registered as open, not built"* (C12 §7); spine does not model elected mayor/council (C12 §4.11) | — |
| currency | absent | `matter_kinds` roster lists `coin` (C06 §5b) but no fixture, yield or price uses it (C12 §4.9 "No coin/currency kind exists" in fixtures) | — |

### 5 Structural handles for comparison

- **Resolution style:** deterministic state writes behind typed three-valued preconditions; no dice anywhere in GV;
  proportional shares (`1/n` of those present) for labour; the stochastic element is which act a person chooses.
- **Granularity / scale:** eight nested rung kinds person→realm; one season per tick; 5 scenes per person per season
  (`scene_budget 5`, C06 §5j). Settlement is one rung among eight, with no settlement-specific state.
- **State model:** typed edges (Tenures) over a small entity set; stocks as integer stores on rungs; Site condition as
  integer on a 1000 scale; all aggregates (population, capacity, purview, governors, establishment, sovereign fraction)
  are Queries computed on demand and stored nowhere.
- **Agency model:** every act is a person's; seats grant a closed remit roster of six acts; a seat-holder acts *through*
  the seat (`Act.via`); no player-or-AI "faction turn"; rule-above-you checks (`rung_above_same_faction`).
- **Information model:** governors learn of a shortfall only via a witness channel to holders whose purview reaches the
  drained rung (non-omniscient; claims can be stale, D01 item on AX-2); no act publishes to a purview (L14 claim 9).
- **Failure/recovery model:** refusals are events (`*.refused`), not errors; an unpaid service term lapses; revocation of
  an appointed holder bans him permanently; Site condition falls by wear and rises only by `work`/`restore` up to a works
  ceiling; body (designed) "only falls" (H-211).
- **Content model:** authored — 31 seats, 37 settlements, 17 territories from `valoria_geography_v30.yaml`, cohorts at
  weight 2, venues `AUTHORED FOR PLAY`; nothing founds a faction or a settlement at runtime in practice (P1 0 `found`).
- **Pacing:** seasonal economy ticks automatically; governance acts are per-scene choices; term clocks (`oblige_term 4`)
  and works stages mature at MATTER.

### 6 Open design decisions the sources name

G20 (SC+GV gaps) is not available; from L14 §6 and D01/D02:
- **D-V1** — can a living top-seat holder be removed against his will (`depose`)? (L14, escalated).
- **Draw policy** — who eats, in what order, how much, under scarcity; blocks `ration` (M-DRAW) (L14, escalated).
- **JQ-6** — hunger band thresholds, population/food ratio, `body_step` magnitude (D02 §4.1).
- **ED-IN-0296 (2)** cohort pursuit vectors (37 of 83 actors have none, D01 item 14); **ED-IN-0297** works
  (`work`/`found`/`build`) (D01).
- **R-05** `dispatch` → `order` rename "held for Jordan" (L14 L12) vs "answered by precedent" (L14 L758) — the lexicon
  contradicts itself.
- **H-52 / L-18** whether `tax`, `ration`, `proclaim` take `remit:issue`; **H-203** office referent; **H-91** revoke
  remit; **H-100/IN-31** revocation cost; **H-165** computed works source; **H-166** closer order / `raze` re-housing;
  **H-211** body only falls; **H-44** writ terms; **H-75** `destroy_record` eligibility; **H-174** whether upkeep homes
  by presence or residence (C12 §7); **J-8** whether `dispatch` is a remit act (gate `WARRANT_ACT = "dispatch"`
  `[ASSUMPTION]`, C03 gate notes); **IN-23** legitimacy and stability Queries; **IN-61** succession.

### 7 Conflicts, uncertainties, checks made

- **Execution vs wiring.** C12 grades effects by reading code; D01 and P1 show nearly all of them do not execute in the
  realm. I grade by P1. P1 is one seed, two seasons; a longer run may move `found`/`build` once stores accrue.
- **`migrate`**: D01 1/118 vs P1 0/81 — different run. Unresolved; both say effectively never.
- **0 live `oblige` after two seasons** although `offices.yaml` authors `obligees` (off_king → NPC-070) as `oblige` at
  build (C12 §4.11). I did not check whether the edge was never built or closed by a death (P1 shows 9 deaths). Open.
- **32 offices vs 31 authored seats** — source of the 32nd NOT READ (C06 §5a).
- **`coin`**: C06 lists `coin` in `matter_kinds`; C12 says "No coin/currency kind exists" — they agree that nothing
  uses it; the roster entry is inert.
- **L14 internal count:** headline "GV ends with 20 rows" vs a list summing to 25 (L14 claim 1); not resolvable here.
- **Line-number drift:** L14's VT/GT/EG cites are stale against HEAD (L14 §1); I used HEAD lines.
- CHECKED `engine/season/loop/driver.py:447-448,514` (calendar, matter, census per season).
- CHECKED `engine/season/state/gate.py:599` (`REVOCATION_DISPOSAL = {"appointed": BAN_KIND, "elected": None, "annex": None, None: None}`).
- CHECKED `engine/season/verb_table.yaml:372-385` (`dispatch`: `writes: []`, `emits: ["order.given"]`, grade `ruled`).
- CHECKED `engine/season/queries/world_q.py:1120-1127` (`levy` "ruled deleted").
- CHECKED effect registrations by grep of `@effect_for` in `engine/season/loop/*.py`: confer, convene, establish, oblige,
  release, requisition, revoke, transfer, work, restore, sabotage, found, build, move, migrate present; `dispatch`,
  `succeed`, `exchange` absent.

---

## Faction Actions (FA) — factions are Propositions plus `commit` edges and never act; membership, the faction survey and faction-goal salience RUNS-IN-LOOP, but war, alliance, recruitment and levy have no executing verb: `at_war` is TESTS-ONLY, `covenant`/`seize`/`sabotage` are wired and execute 0 times, `declare`/`recruit`/`levy`/`conspire` are DESIGN-ONLY

### 1 What it is

FA is the inter-polity layer: who belongs to which faction, what territory a faction controls, and the acts by which
seat-holders make war and peace, bind treaties, raise men, post agents, seize places and plot. The fantasy is grand
strategy without a faction player: *"a faction never acts"*; the actor is *"the person holding the office"*
(`rosters.yaml` `factions` note, L15 C1). A faction is an uttered `Proposition` (its creed) plus the live `commit` edges
pointing at it (C12 §2; `world_q.py:1365` CHECKED); its army, footprint, head and wars are Queries over those edges, never
stored (C12 §4.10). Nine factions are rostered: Church of Solmund, Crown, Guilds, Hafenmark, Löwenritter, Restoration
Movement, Schoenland, Varfell, `faction x` (test) (C06 §5b).

### 2 Operating alone

**State.** Faction Proposition `fac_<slug>` (P1: 9 present); membership = live `commit` (P1: 31 live, 7 factions);
service = live `oblige` to a seat (P1: 0); territory = `hold` on a Rung, attributed to a faction by `holder_faction_of`
(nearest ancestor with a `hold`, then the holder's *single* faction `commit`; zero or several → `None`) (C12 §4.10).
Test `lb16` says a faction Proposition can no longer hold a rung and `build_realm` has no faction holds (C12 §8).
Organization goals: `goals.yaml` rows minted as OUGHT Propositions at world-gen; role templates (sovereign,
ecclesiastical, mercantile-procedural, intelligence-diplomatic, reformist, military-order) give each faction an
`expected` pursuit vector (C04 lines 18, 94).

**Queries that execute (C12 §4.10):**

| query | formula |
|---|---|
| `members(w, f)` | sorted subjects of live `commit` to `f` |
| `leaders(w, f)` | members holding a live `hold` on an Office whose `faction` is `f` |
| `mustered(w, rung, f)` | members present (live `contain`) in the rung's **subtree** |
| `density(w, rung, f)` | (members present in subtree, persons present) |
| `fortification_of(w, rung)` | `Σ garrison condition / (1000 × n garrisons)`; 0.0 if none |
| `sovereign_fraction(w, rung)` | share of non-person rungs in the subtree held by the top holder |
| `provinces_of`, `uncontrolled`, `footprint` | grouping of territories by holder faction; territories with no holder faction |
| `faction_q.resolve(w, p)` | `Faction(proposition, members, holdings, seats, head)` |
| `faction_q.head(w, p)` | last live `commit` with non-None `degree` — **always `None`** (no builder writes `degree`) |
| `faction_q.at_war(w, a, b)` | True iff a `mood == "WAR"` Proposition with `{subject, value} == {a, b}` has a live `commit` |

**Verbs (the lexicon's nine hosts, L15 §5a; code status from L15 §7.2 and my checks):**

| host | actor / eligibility | designed resolver | designed writes |
|---|---|---|---|
| `covenant` (treaty, peace, alliance, truce, tribute, cession, vassalage, league, ransom; 11 contents) | seat-holder, `remit:issue` | offer + seal by second party; "in force" is a Query | **code:** mints a `dispensation` Record (`Record.exists`, `Record.stages`), emits `covenant.offered`; acceptance is the addressee's own `commit` (`verb_table.yaml:254-280` CHECKED) |
| `declare` (war) | seat-holder, `remit:dispatch` [ASSUMPTION] | deterministic | WAR Proposition + declarer's edge, `war.declared`, broadcast by chronicle |
| `recruit` | seat-holder, `remit:confer` [ASSUMPTION] | **contested** (counterparty, obstacle, degree; ED-IN-0210 Ruling 1) via SC's contest resolver (M10) | won: recruit's `oblige` to the seat with a `Term`; lost: `recruit.declined` |
| `levy` | seat-holder, `remit:dispatch` | `requisition`'s two conjuncts (purview, stores ≥ n) | `Rung.stores`: `recruits −n`, `troops_raw +n` (TS1:775-776); `recruits` kind absent from `rosters.yaml` |
| `dispatch` | seat-holder, `remit:dispatch` | shipped: none | shipped: `writes: []`, `order.given`; rebuilt: posting payload on the obligee's `oblige` + `_relocate` |
| `seize` | seat-holder, `remit:issue` | warrant (Record) or occupation (Rung); "A SEAT is never seized" | closes one `hold`, opens one; `record.seized` / `rung.seized` |
| `conspire` | any person, `own` | contested; obstacle = invitee's loyalty to target seat | plot = OUGHT Proposition naming the target seat; invitee's edge on Won |
| `sabotage` | any person, presence at Site | deterministic `_fall` = `condition × 1/n` `[ASSUMPTION]` | `Site.condition` down, `site.damaged` |
| `succeed` | the heir (`off_heir` holder) | IN-61: `inheritance` basis `confer` may not use | heir's `hold` on the throne |

Dice enter FA only through the designed contested hosts (`recruit`, `conspire`), which borrow SC's resolver; L15 gives
no numeric obstacle or degree threshold (L15 §4 "Numbers"). Everything that executes today is deterministic.

### 3 In the whole game

- **Invokers:** persons through seats (remit acts) or `own` (`conspire`, `sabotage`); FA-01 pins five head seats acting
  through `dispatch` (`test_fa01_head_seats.py`, L15 S5).
- **Reads:** GV's seats, purview and rung ladder; NP/SC's `commit` and `utter` (the only WAR producers, VT `utter`,
  `commit`; L15 C4); MB's `march` arrival (IN-13).
- **Who reads FA state now:** `survey` → `faction_q.resolve` → a `faction_sheet` Record (`effects_information.py:735`,
  C12 §6; P1 13 `faction.surveyed`); mass battle sides read `holder_faction_of`, `mustered`, `fortification_of`
  (`seam/wrappers/mass_battle.py`, `loop/sides.py:131`, C12 §6); attention salience orders a person's questions by the
  cosine of crisis weights against the organization's `expected` vector in tiers 0 and 3 (C04 `attention_key`);
  `may_muster` requires a live `commit` to the seat's faction (C03 gate notes).
- **Who does not:** `at_war` — no production caller (grep CHECKED: only its `def` at `faction_q.py:219` outside tests);
  `head` — always `None`, so "only the faction head may declare war" cannot be built without it (L15 Q3);
  `provinces_of`, `sovereign_fraction`, `uncontrolled` — harness census only (C12 §6).
- **Feedback loops designed:** war gates which acts (open, MB-G15); alliance widens `mustered` (M3); tribute renews like
  upkeep (`_renewals` shape, M2); recruitment grows `oblige` service, which `transfer` must pay or it lapses; breach is
  the breaker's own `release`, priced by a `deed:` cell (L15 C18). **None of these runs.**

### 4 Built vs designed

| element | grade | evidence | what should exist and does not |
|---|---|---|---|
| faction = Proposition + `commit`; `members`, `leaders`, `density` | RUNS-IN-LOOP (state + queries) | 9 `fac_*`, 31 live commits in P1; `commit` verb 61 attempted / 61 `commitment.refused` — no membership changed in P1 | runtime faction founding (FA-G39, H-186); `factions` read from `names_index.yaml` (L15 C13) |
| faction survey sheet | RUNS-IN-LOOP | P1 13 `faction.surveyed` via `survey` | — |
| faction goals / role-template salience | RUNS-IN-LOOP | ordering in `attention_key` (C04) | cohort vectors (ED-IN-0296 (2)) |
| `holder_faction_of`, `mustered`, `fortification_of` | reachable from loop; not measured by P1 | callers `loop/sides.py:131`, mass-battle wrapper (C12 §6) | M3 widened muster (obligees, allies) |
| `faction_q.head` | TESTS-ONLY, always `None` | faction_q.py:116-147 (C12 §4.10) | a builder that writes `Tenure.degree` |
| `at_war` | TESTS-ONLY | no non-test caller (CHECKED) | M1 a reader; `declare` as the only legitimate producer [ASSUMPTION] |
| `covenant` offer | TESTS-ONLY | VT row + `@effect_for("covenant")` at `effects_information.py:240` (CHECKED); P1 13 / 0 | seal, in-force Query, breach detector, tribute, alliance (M2); successor binding (Q1) |
| `seize` | TESTS-ONLY | effect at `effects_information.py:876`; P1 0 attempts (forms only on a held warrant's referents, C04 item 6) | annex re-parenting (M-ANNEX); Church appetite (M9) |
| `sabotage` | TESTS-ONLY | VT row grade `assumption` + effect in `effects_economy.py`; P1 34 / 0 | — |
| `dispatch` | RUNS-IN-LOOP, writes nothing | P1 6 `order.given` | rebuild as posting (M5) |
| `declare`, `recruit`, `levy`, `conspire` | DESIGN-ONLY | no VT row (L15 §7.2 item 8); no `recruits` kind (§7.2 item 9) | M1, M4 troop stock, M7 plot reader, M10 contest |
| `succeed` | DESIGN-ONLY | row, effect declined (`verb_table.yaml:1096-1113`) | IN-61 |
| hire, mercenaries, embargo, marriage alliance, hostage | DESIGN-ONLY / PARKED | L15 §5b | carriers named per row |

### 5 Structural handles for comparison

- **Resolution style:** deterministic for every executing piece; contested (opposed draw via SC resolver) only in the
  designed `recruit`/`conspire`; no war score, no casus-belli resource, no diplomacy AI.
- **Granularity:** factions are not units of play; the unit is a person in a seat. Territory is per-rung holding; a
  faction's "province" is a derived grouping with no minimum size.
- **State model:** relational (edges to Propositions and Offices); faction attributes are all derived; war and treaties
  are designed as Queries over live edges, never flags; no faction-to-faction numeric relation, reputation, alliance or
  treaty state exists (C12 §4.10 closing note).
- **Agency model:** distributed and person-level; membership is the joiner's own act; a won contest may open another's
  edge (L15 Q4, escalated); the "head" is undefined at runtime.
- **Information model:** a faction's state is learned by `survey` (a Record snapshot) or witness channels; a covenant's
  terms travel only with the held Record (`covenant.offered` is deliberately not broadcast, VT emits_note).
- **Failure/recovery:** breach = the party's own `release`; treaty bound to persons, so it would lapse on a signer's
  death unless Q1 rules otherwise; refused acts are events.
- **Content model:** factions, seats and initial memberships authored; goals authored per organization; nothing
  generates a faction or a war at runtime (*"nothing authors a WAR `utter`"*, C12 §7).
- **Pacing:** seasonal; no separate diplomatic or war tempo.

### 6 Open design decisions the sources name

G19 (PC+NP+MB+FA gaps) is not available; from L15 §6:
- **Q1** does a treaty bind the signer or the seat? **Q2** host name `dispatch` or `assign` (D-V7/R-05)? **Q3** who may
  declare war — any `remit:dispatch` holder ("marshals starting wars") or the faction head only (needs `head`)?
  **Q4** may a won contest open an edge the counterparty owns (versus VT:281 "their own choose decides")?
- **D-V3** public channel past SC-01 step 13; **D-V6** `declare` needs its own row; **D-V2 / K-NPC-6** kin tie for
  marriage; **J-1** troop body (M4); **MB-G15** which act `at_war` gates; **FA-G39 / H-186** runtime faction carrier;
  **IN-61** succession; **IN-70** SC opinion as recruit obstacle; **IN-12 steps 7, 9, 10** covenant, sabotage, conceal.
- Mechanics waiting list M1-M10 (L15 §6c).

### 7 Conflicts, uncertainties, checks made

- **`covenant` exists in code; the lexicon says it does not.** L15 C13 "VT has none"; HEAD has the row
  (`verb_table.yaml:254`) and an effect (`effects_information.py:240`) — CHECKED. VT writes `Record.exists/stages` and
  makes acceptance a `commit`; the lexicon designs `Proposition.exists` + `Tenure.since` and says acceptance is "not a
  `commit`". I believe the code for what exists and treat the lexicon as a redesign proposal.
- **`sabotage` status:** L15 "PLANNED"; code has row (grade `assumption`) and effect; P1 34 attempts, 0 executions.
- **`levy` ownership:** L15 ruling R-01 says "`levy` is MB's row", yet L15 S4 makes `levy` an FA host; L14 hands troop
  `levy` to MB/FA. Separately, `world_q.py:1124-1127` "ruled `levy` deleted" refers to round-one *extraction* levy (a tax
  policy clause), not troop raising — do not conflate.
- **`mustered`** reads the subtree, not the literal rung as L15 C7 says (L15 §7.2 item 5).
- **Line drift:** L15 cites `members` :1152 and `mustered` :1257; HEAD :1365 and :1470.
- **`holder_faction_of` in play:** reachable from `loop/sides.py:131`; P1 did not measure whether a battle formed sides.
- CHECKED `engine/season/queries/world_q.py:1365-1376` (`members`), `engine/season/queries/faction_q.py:219` (`at_war`,
  no non-test caller by grep over `engine/`), `engine/season/verb_table.yaml:254-280` (`covenant`),
  `engine/season/loop/effects_information.py:240, 876` (`covenant`, `seize` effects).
- MEASURED P1 (above); no REFUTED citations, but L15's "no `covenant` row" claim is refuted by the code.

---

<!-- ===== A6 (S6_economy_world_npc.md) ===== -->

# A6 · S6 — Economy, trade and craft (EC) · World, travel and survival (WT) · NPC life and persons (NP)

Stage-2 synthesis. Sources: extracts L16, L17, L18, C12, C06 §5i-5j, C02 §4.3, D02 §4.1, G21 (cited `extract §`), plus
tree checks at HEAD `a4ca9a5` recorded in each §7. All `engine/season/` paths abbreviated `es/`. Grades: RUNS-IN-LOOP,
TESTS-ONLY, DESIGN-ONLY (brief). A body "RUNS-IN-LOOP" means `driver.py` reaches it (`driver.py:448` → `matter`;
`resolve` → `EFFECTS[verb]`, C12 §4.1, C02 §6); it does NOT mean a normal season executes it often — execution counts
are given where a source measured them, and are flagged stale where they were.

**Cross-cutting fact all three blocks share: one pass, MATTER (barrier 2), owns every exogenous motion** — term
maturation, larder draw, hunger-to-body, ageing/illness, yield, end of travel legs, wear (C02 §4.3 steps 2-11). Every
survival consequence in MATTER ships at a control value that makes it inert (`body_step=0`, `age_step=0.0`,
`illness_rate=0.0`, `season_factor_draw=()`; `es/data/fixtures.py:469,594,606-607`, CHECKED). The economy and the
world therefore run, but nothing in them can hurt anyone in a shipped season.

---

## EC — Economy, trade and craft — a moneyless store-and-yield ledger on the territorial ladder; production and conserving transfer RUN-IN-LOOP, trade/craft/credit/hire/tax are DESIGN-ONLY

### 1 What it is
Goods are integer quantities of a "matter kind" held in `Rung.stores` (a Rung is any node of the containment ladder:
person < hearth < community < settlement < territory < province < duchy < realm, C06 §5b). Places produce by owning
Sites (a built fabric with a `condition` on a 0..1000 scale) whose yield MATTER mints each season; cohorts eat out of
the nearest store up the ladder; seats move stores by `transfer` and `requisition`; works (a `Record` of kind
`works`) are funded to `found` new rungs and `build` new Sites. The fantasy served is a pre-monetary estate economy —
granaries, harbours, mines, upkeep of sworn men — run by office-holders. There is no money in use, no price, no
market, no wage, no tax, no credit, no manufacture (L16 §2 claim 1; C12 §7).

### 2 Operating alone
**State.** `Rung.stores {kind:int}`, `Rung.yield`; `Site(id, rung, kind, condition)`; `works` Record `{plan, at}` with
stages; `Tenure.term` (maturity season) on `oblige` edges (C12 §3). Matter kinds registered: grain, salt, timber, ore,
coin (`es/rosters.yaml:1409-1410`, CHECKED; C06 §5b). Site kinds: harbour, seam, body, dwelling, garrison (C12 §3).
**Procedure (MATTER, once per season; C12 §4.2, C02 §4.3):**
1. Tenure terms with `matures_at <= tick` close (`tenure.closed`) — unpaid service lapses (C12 §4.2 step 3).
2. Larder draw: each cohort wants `subsistence_weight[k] × weight` (grain 2, salt 1); `nearest_store` walks UP the
   ladder to the first rung holding the kind; `take = min(want, held)`; remainder not walked further (C12 §4.8).
3. Draw is debited BEFORE yield is credited ("Events resolve FIRST, then bodies, larders, yield, travel, wear",
   C02 §4.3 step 9).
4. Yield per Site: `int(SITE_YIELD[kind][k] × max(0,condition)/1000 × season_factor)`; harbour {grain 40, salt 30},
   seam {ore 50, timber 10}; nothing else yields (C12 §4.9; `es/loop/matter.py:591`, CHECKED). No labour or headcount
   term (G21 EC-G41).
5. Wear: harbour/seam/body −10 per season, dwelling/garrison 0; downward band crossings emit (C12 §4.2 step 12).
**Acts (resolved in RESOLVE, deterministic, no dice; C12 §4.5-4.6):**
- `work` / `restore`: stage `_rise = headroom × 1/n` (n = persons present at the rung; `share`, world_q:422) toward a
  `ceiling` = scale × matured works stages / declared stages. `f(degree)` is the identity — no roll (C12 §4.5; H-164).
- `sabotage`: stages `−condition/n`; "LOWERS, NEVER ENDS" [ASSUMPTION] (C12 §4.5).
- `transfer`: `_shift` (src −amount, dst +amount; conserved). Through a seat paying from its own rung to obligees'
  home, it also renews up to `amount // upkeep_of(seat)` `oblige` terms by `oblige_term=4` seasons, soonest-maturing
  first; `default_upkeep=1` (C12 §4.5, §4.9).
- `requisition`: `_shift` from a rung inside the seat's purview into the seat's own rung (the "treasury"; there is no
  Treasury class) (C12 §4.4, §3).
- `found`: mints a Rung of the works' plan kind, its `contain` edge and the founder's `hold`; moves `works_cost` from
  the payer INTO the new rung (two-sided). `build`: mints a Site at condition 0 and CONSUMES cost one-sided
  [ASSUMPTION; medium]. Costs: hearth/community {grain 10}; harbour/seam/dwelling/garrison {timber 10}; none for
  settlement or above (C12 §4.6, §4.9).
**Outputs.** Events `stores.changed`, `yield.taken`, `transfer.made`, `term.renewed`, `requisition.taken`,
`site.worked/restored/damaged/built`, `rung.founded`, `condition.worn`, `condition.band_crossed`; refusals
`<verb>.refused`, `work.unavailable` (C12 §5).

### 3 In the whole game
- **Invoked by** persons and seats choosing verbs in DELIBERATE (the decision layer forms candidates) and by MATTER's
  actorless passes. Scales: Site/rung (Territorial in `SCALE_OF_RUNG`, C06 §5b).
- **Reads** presence (`contain`), works Records, seat purview, `oblige` terms, fixtures.
- **Writes** `Rung.stores`, `Site.condition`, `Tenure.term`, new Rungs/Sites.
- **Read by:** subsistence (WT/NP block, cohorts' bodies — inert); `capacity` reads dwelling Sites (migration);
  `fortification_of` reads garrison condition for mass battle (C12 §4.10, §6); `governors_of` + WITNESS
  `SEAT_CHANNEL` deposit a shortfall claim with seats whose purview holds a drained larder, and
  `decision/options.py::_from_shortfall_claim` forms a relief `transfer` (C12 §6; D02 §4.1).
- **Feedback loops (as built):** (a) upkeep loop — a seat must keep transferring stores to renew sworn men's terms or
  the terms lapse at MATTER (`test_term_upkeep.py`, C12 §8); (b) wear/repair loop — Sites wear 10/season and yield
  scales with condition, so unrepaired harbours/seams decline; (c) dearth/relief loop — shortfall → governor claim →
  `transfer` (fires only in `harness/scarce.py`, see §7). No price loop, no labour loop, no growth loop (population
  does not grow; see NP).

### 4 Built vs designed
| element | grade | evidence | what proposals say should exist and does not |
|---|---|---|---|
| Yield at MATTER | RUNS-IN-LOOP | `matter.py:578-607` via `driver.py:448` (C12 §4.2) | labour factor ×1 control arm; tally per Site (L16 §4.2, M1); per-place production (G21 EC-G42) |
| Larder draw (`subsistence_draw`, `nearest_store`) | RUNS-IN-LOOP | `world_q.py:1017`, `:902`; `matter.py:415` | storage bound/granary (M12, EC-G43); draw policy (`hoard`/`ration` PARKED, L16 §2 cl. 22) |
| Wear and band crossings | RUNS-IN-LOOP | `matter.py:661-691` (C12 §4.2) | — |
| `work`, `restore`, `sabotage` | RUNS-IN-LOOP (bodies); executions unmeasured at HEAD | `effects_economy.py:23,180,160` CHECKED; G21 §2 cl. 11 "work 0/183, restore 25 refused" at `5445e34`, "not re-measured" | `work` to produce via labour tally (S1 REBUILD); `restore` narrowed to fabric (S4) |
| `transfer` + upkeep renewal | RUNS-IN-LOOP | `effects_economy.py:214-356` (C12 §4.5) | computed `to` fixed (EC-G11: "executes 0, refuses 723", stale count); distance cost `haul` (M3) |
| `requisition` | RUNS-IN-LOOP (body) | `effects_governance.py:425-464` | price of taking (EC-G05); `tax` = rate × known yield folded in (L16 S9) |
| `found`, `build` | RUNS-IN-LOOP (bodies) | `effects_founding.py:91,184` CHECKED | computed works declaration (EC-G46); `raze` (NEW ROW, owner MB/EC pending) |
| `exchange` | DESIGN-ONLY | row `verb_table.yaml:416`, grade `assumption`, effect DECLINED (PLAN POSITION 14); no `@effect_for("exchange")` (L16 §1; CHECKED) | `price_of(rung,kind)` Query, `return_kind` operand, ×4 store write, co-located counterparty consent read from own prices (L16 §4.8) |
| `craft` (+`mint`) | DESIGN-ONLY | no row (L16 §1) | recipes roster, workshop Site kind, arms/tool kinds; inputs→product at one rung, no partials (L16 §4.9) |
| `hire` | DESIGN-ONLY | no row (L16 §1; L18 §5a) | employer-voiced service edge + first wage; lapse at MATTER on non-payment (L16 §4.10) |
| `borrow` / `lend`, `debt` Record | DESIGN-ONLY | no row | debt matures at MATTER, emits `debt.lapsed` (L16 §4.11) |
| Coin | DESIGN-ONLY as money | `coin` is a registered kind with no producer and no stock (EC-G21); C12 §4.9 "no coin kind" is wrong as to registration, right as to use | coin seed at world build + `mint` via `craft` (L16 §6) |
| Price, market, tax, toll, embargo, smuggling | DESIGN-ONLY | absent from code (C12 §7) | price is a Query, never stored (L16 cl. 12); tax folds into `requisition` (cl. 20); toll, smuggle PARKED on M3/M7 |

### 5 Structural handles for comparison
- **Resolution style:** deterministic arithmetic throughout; no dice in any EC act (`f(degree)` identity, H-164).
- **Granularity:** integer units of five commodity kinds; Site condition fixed-point 0..1000.
- **Scale:** territorial ladder; stores live at any rung; production only at Sites (harbour, seam).
- **State model:** stock-and-flow ledger with conservation (`_shift`; F10 check "total store mass changed",
  L16 §4.7); one-sided sinks only at `build` cost and the larder draw; one source (yield).
- **Agency model:** office-holders act through seats (`remit:issue` gates `transfer`/`requisition`, EC-G06);
  persons act by presence (`work`, `restore`); cohorts cannot act through a seat (D02 §4.1).
- **Information model:** no price signal; scarcity becomes known only as a `shortfall:<kind>` Observation on a drained
  larder's write, deposited to those present and governors in purview (C12 §6).
- **Failure/recovery:** lapse of unpaid service at term (shipped "desertion" shape; the arrears alternative is open,
  EC-G22); wear decline, repair by `restore`; no bankruptcy, no debt.
- **Content model:** authored world (37 settlements, 322 Sites at build, C06 §5a); stores empty at build
  (`stores_by_rung_kind {}`, C06 §5a); yields and costs are fixture tables.
- **Pacing:** seasonal tick; one yield, one draw, one wear per season; terms of 4 seasons.

### 6 Open design decisions the sources name
- **EC-G22 / H-159 (L16 §3.9 item 1):** unpaid upkeep → (a) term lapses, men leave (shipped) or (b) arrears debt with
  grievance up to a cap. "decides whether a broke seat loses its men at once or slides into a debt spiral". OPEN.
- `raze` owner MB vs EC; `mint` as seat prerogative vs open (GV); `tax` head word (GV); distraint on lapsed debt (GV);
  mercenary hire as person vs stock (MB); corvée EC-G50 (GV ruling, M11); draw policy (`hoard`+`ration`); H-164 degree
  on uncontested acts; coin seed at build; `exchange` consent model untested ("no shipped instance", L16 §6).
- EC-G53 extraction rate ("Fiscal Stance" cut, ED-FA-0008); EC-G05 unpriced taking; EC-G37 distance pricing (waits on
  WT M-WT-1). Full gap list EC-G01..G53 in G21 §5 (first-pass dispositions; current ones are L16 §3.6: 33 closed ·
  9 PARKED · 9 OUT OF SCOPE · 1 STALE · 1 DISPUTED, L16 §2 cl. 26).
- JQ-6 (D02): food/population ratio — at today's magnitudes "the realm cannot go hungry after season 0".

### 7 Conflicts, uncertainties, checks
- **Coin.** C12 §4.9 "No coin/currency kind exists" vs L16 §4.15 and C06 §5b listing `coin`. CHECKED
  `es/rosters.yaml:1409-1410`: coin is registered. Believe L16/C06; C12 means unused.
- **Shortfall firing.** C12 §7 "shortfall observation fires only in `harness/scarce.py`" vs D02 §4.1 "37 cohorts
  short in season 0". Both true: CHECKED `es/loop/matter.py:463-468` — in season 0 "every eater's `source` is
  `None`", so cohorts are short but no larder drains and no Observation/claim is deposited; after first yield the
  realm is "in surplus". The IN-22 relief path is therefore TESTS-ONLY in practice.
- Execution counts (`work` 0/183, `transfer` refuses 723, `requisition` 0 seat-based) are from `5445e34`, "not
  re-measured" (G21 §2 cl. 11). D02 reports cohort acts season 1 `work` 39 (formed; executed not stated). Unknown which
  hold at HEAD.
- L16 line cites drift +100..+228 lines (L16 §1 table); verb names hold.
- CHECKED `es/loop/matter.py:591` (yield formula); CHECKED `effects_economy.py`/`effects_founding.py` `@effect_for`
  list (work, sabotage, restore, transfer, found, build; no exchange).

---

## WT — World, travel and survival — a containment tree with one-season hops and an inert survival layer; movement RUNS-IN-LOOP, geography graph and every hazard are DESIGN-ONLY (data present, no reader)

### 1 What it is
The world is the ladder of Rungs built at world-gen from the geography file (17 territories, 37 settlements, plus
built communities and hearths, C06 §5a, §5i). A person is "at" a Rung by a live `contain` edge and "lives" at one by a
`reside` edge. Travel (`move`) changes presence; `migrate` changes presence and residence. A journey always completes
within its season and costs the traveller scene budget. The survival layer (hunger, weather, ageing, illness) is
wired into MATTER but ships switched off. The fantasy proposed — overland routes, terrain, storm seasons, exposure,
foraging armies, discovery of points of interest — exists as data and proposals, not as play (L17 §2 cl. 9-10).

### 2 Operating alone
**State.** `contain` / `reside` Tenures (Rung → Rung only, Layer-1 ratified: `contain : Rung → Rung`, L17 §6 item 2);
`Person.travel_leg` (list of destinations this season); `w.tick` = season; `Person.body` (0..1000), `born`.
**Movement procedure (C12 §4.7; L17 §4.1):**
1. Preconditions: `contain_path` — origin and destination share an ancestor in the tree (`es/data/requires.py:374`);
   `contain_ascends` — kind-ladder check (`state/world.py:301`). "Neither reads distance" (L17 §2 cl. 3).
2. Custody (`detain` Tenure) declines → `travel.blocked`.
3. `_relocate`: close live `contain`, open one to `to`, append `to` to `travel_leg`.
4. `migrate` only: refuse if already resident there; refuse a newcomer if `population + weight > capacity(dest)`,
   capacity = max(1, number of dwelling Sites in the subtree) (C12 §4.7); then close/open `reside`;
   `residence.changed`.
5. Cost: `budget -= len(travel_leg) × budget_leg_penalty (1)` (`es/decision/budget.py:60`, CHECKED). Every destination
   costs the same one leg (L17 §2 cl. 12).
6. Next MATTER clears `travel_leg`, emits `travel.ended` (C02 §4.3 step 10).
**Survival passes in MATTER (C02 §4.3 steps 6-8; C12 §4.2):**
- Weather: `season_factor_of` = `season_factor (1.0) × keyed choice from season_factor_draw`; draw ships `()` → factor
  1.0. Its only reader is yield (CHECKED: sole caller `matter.py:364`, used at `:591`).
- Hunger: body falls `body_step × units short`; `body_step=0` → nothing; at 0 → `_die` (`person.died`).
- Ageing/illness: `hazard = min(1, illness_rate + age_step × age)` keyed draw per individual; cohorts exempt; both 0.
**Outputs.** `travel.moved/ended/blocked`, `residence.changed`, `migrate.refused`, `body.changed`, `person.died`.

### 3 In the whole game
- **Invoked by** any person choosing `move`/`migrate`; `march` (MB) arrives through the same `_relocate`
  (`effects_migration.py:101-105` per C12 §4.7); census individuation places newly demanded persons by `contain`.
- **Presence is the epistemic gate**: witnesses are whoever stands there (L17 §3), so moving is how a person comes to
  see, be seen, and act on a place (`work`, `restore` require presence; EC §2). This is the main reason travel matters
  today.
- **Reads** the tree, custody, capacity, population. **Writes** presence, residence, `travel_leg`.
- **Read by:** WITNESS/encounter (who is co-located), `share` in `work`/`restore` (1/n present), `population` /
  `capacity`, budget, faction `footprint`/`mustered`/`density` (C12 §4.10).
- **Geography file** (`systems/settlements/valoria_geography_v30.yaml`): provinces, settlements, province
  `adjacency` (26), `settlement_adjacency` (55 entries; its comment says 56), `terrain_cost_matrix`, `march_budget`,
  water, bridges, `forgetting_zone`, `radiation_bands`, `poi_catalog` (C06 §5i). Read by world-gen to build Rungs and
  by the mass-battle seam for the battlefield (`seam/wrappers/mass_battle.py:201`); no season module reads adjacency,
  terrain cost or POIs (G21 §2 cl. 10, own grep, 0 hits; L17 §2 cl. 10).
- **Feedback loops:** none closed at shipped values. Designed: hunger → death → lower demand (D02 Route A);
  route dependency → larder shortfall (M-WT-7); forage → resident grudge (L17 §5.1).

### 4 Built vs designed
| element | grade | evidence | what proposals say should exist and does not |
|---|---|---|---|
| `move`, `migrate`, `_relocate`, custody, capacity refusal | RUNS-IN-LOOP | `effects_migration.py:24,122` CHECKED; D02 §4.1 cohort acts season 1: `migrate` 86 (formed) | rename `move`→`travel` (R-10); catch journey-to-where-one-stands (H-140, WT-G01) |
| Leg price in scene budget | RUNS-IN-LOOP | `budget.py:60` CHECKED | route-weighted price (M-WT-1); mount `ride`, water `sail` folded as parameters |
| Leg end at MATTER | RUNS-IN-LOOP | `matter.py:643-655` (C02 §4.3) | multi-season legs (M-WT-3 "delayed"), between-places location (amends Layer 1) |
| Weather draw | RUNS-IN-LOOP at control (factor ≡ 1.0); live arm TESTS-ONLY | `fixtures.py:469`; `test_season_weather.py` (C12 §8) | a year length/calendar (M-WT-2); weather as second reader for exposure (M-WT-4) |
| Hunger → body → death | RUNS-IN-LOOP at control (inert); live arm TESTS-ONLY | `fixtures.py:594` `body_step=0`; `test_territorial_subsistence.py`, `test_in22…` | RB-5: `hunger(w,S)` Query → band starving/hungry/lean/fed, reach to seats, `body_step` 10 (REM-50/51/52, D02 §4.1) — no `def hunger` in `world_q.py` (CHECKED) |
| Ageing / illness death | RUNS-IN-LOOP at control; live arm TESTS-ONLY | `fixtures.py:606-607`; `test_in34_bodies_clock.py` | NP owns (WT-G26) |
| Route graph reader, terrain cost | DESIGN-ONLY (data present) | GEO :594, :760 match (L17 §7.2) | M-WT-1 Route Query writing nothing; one unit = the edge; pixel `march_budget` retired (L17 §4.8) |
| Journey roll, exposure, Calamity hazard | DESIGN-ONLY | — | unopposed draw vs terrain Ob on `degree_from_net`; "Endurance check Ob 1 per territory or take 1 Exposure" (XSC via L17 §4.6) |
| `forage`, `camp`, `explore`, `evacuate` | DESIGN-ONLY (NEW / PARKED) | no rows | forage: force eats ahead of residents, one edge out; explore reveals authored POIs; camp/evacuate PARKED |
| Cohort weight migration, route dependency, campaign supply | DESIGN-ONLY | — | M-WT-6/7/8 (L17 §5.2); "famine cannot empty a town" today (L17 §2 cl. 21) |

### 5 Structural handles for comparison
- **Resolution style:** deterministic precondition checks; no dice in travel; survival is a per-season keyed
  random draw (weather choice, illness/age hazard) — both off.
- **Granularity / scale:** node-to-node hops on a containment tree (not a graph); one season per hop; any reachable
  rung in one leg — distance-free.
- **State model:** presence and residence as Tenure edges; travel has no in-transit state beyond a leg list cleared
  each season; nobody is ever "in the open" (L17 §2 cl. 30).
- **Agency model:** the person moves himself; no seat-ordered movement of others (`evacuate` PARKED); armies via MB.
- **Information model:** co-location is the visibility rule; no fog, no discovery, no route knowledge.
- **Failure/recovery:** refusal only (custody, ladder, capacity); no delay, loss, exposure or attrition.
- **Content model:** authored map (canonical geography, PP-726 rebuild, settlements partly "inferred, not
  hand-tuned", GEO :244 CHECKED); POIs exist only as per-province counts.
- **Pacing:** the season is the unit; no year (`season_of_year` is None while the draw table is empty).

### 6 Open design decisions the sources name
- **L17 §3.9 item 1:** does the road cost a named person anything but time? (a) only Calamity territory exposes; (b)
  weather wears named travellers too. "These lead to different games." Recommendation (a); not ruled.
- **L17 §3.9 item 2:** can a person or force be between places? Recommendation: journeys complete in their season;
  `camp`, ambush PARKED. A non-Rung location amends ratified Layer 1.
- **JQ-6** (D02): hunger band thresholds, food/population ratio, `body_step` magnitude; REM-51 reach ON and REM-52
  `body_step` 10 marked [ASSUMPTION; Jordan to correct].
- WT-G02 DISPUTED (refusal as news, H-111); H-140; R-10 rename falsifier ("no corpus count run"); LF-1/LF-3 field
  provisioning "held back as Jordan's" (G21 §6); WT-G07 two incompatible movement models (Military÷2 edges vs
  Military×100 px). Tally L17: closed 20 · parked 6 · out of scope 15 · stale 1 · disputed 1 = 43.

### 7 Conflicts, uncertainties, checks
- **Edge count:** L17 "56 edges per its own comment" vs C06 "settlement_adjacency (55)". CHECKED: comment at GEO
  :602 says "56 edges total"; `yaml.safe_load` gives 55 list entries. The file disagrees with itself; 55 is what code
  would read.
- L17 cites to `matter.py`/`world_q.py`/fixtures are stale (+9..+213 lines, L17 §7.2); its "weather's one reader is
  yield" claim was unverified there — CHECKED here: true (`matter.py:364,591`).
- L17 is silent on the hunger pass (L17 §7.3); C02/C12/D02 describe it. No contradiction: it is inert.
- CHECKED `world_q.py:1072-1076`: individuals skip the draw ("`24f`: the individual does not eat"). CHECKED
  `budget.py:58-61`.

---

## NP — NPC life and persons — two kinds of person (37 weight-2 cohorts that eat and 46 named individuals that act); body/skill/grudge verbs RUN-IN-LOOP, kin, household, births, marriage, inheritance are DESIGN-ONLY or absent

### 1 What it is
Everyone is a `Person`. A **cohort** is "a Person at `weight > 1`" — the population of a settlement as one actor
("the people of <name>", weight 2, one per settlement) (C12 §4.7; `es/state/carriers.py` per C12 §3). A **named
individual** is a cast member read from canon (46 rows, C06 §5a; C05 §cast) with pursuits, conviction, stance and
offices. Persons form bonds to Propositions (`commit` = faction membership), to seats (`oblige` = sworn service) and to
offices (`hold`). The NP lexicon asks for the life of persons on persons — healing, training, forgiving, befriending,
marrying, succeeding, giving (L18 §1). The fantasy is a court-and-retinue drama (CK3/Pendragon are its cited
precedents, tagged [MEMORY], L18 §2 cl. 8) — without, today, families.

### 2 Operating alone
**State (C12 §3; L18 §2 cl. 1; C05 §5):** `weight`, `capability {key:int}` (dice count; "GATES NOTHING"), `stance`
rows `(referent, valence −5..+5, weight 0..5)`, `pursuits`, `conviction`, `scar`, `ledger`, `body` (0..1000), `born`
(age = `tick − born`, a Query), `travel_leg`. Person-to-person Tenure kinds `tie`, `knot`, `succeed` exist in the
roster; there is no `kin` kind (C12 §3 TENURE_KINDS).
**Readers:** `regard = stance_toward + judged_gain(0.5) × judged deeds + told_valence_gain(0.5) × told` (C05
person_q:390); `teller_weight` reads regard (L18 §2 cl. 3).
**Acts with bodies (deterministic, no dice):**
- `tend` raises the subject's body to `condition_scale` in one act ("one tender restores a person whole in one act")
  [ASSUMPTION; medium]; refused on a whole body (`es/loop/effects_combat.py:370-393`, CHECKED).
- `train` raises one capability key by 1, only where the subject already holds that vocation key (J-13 answered (iii)
  as interim) (`effects_combat.py:396-427`, CHECKED).
- `forgive` deletes the actor's own negative stance rows toward the subject (`effects_combat.py:430-450`, CHECKED).
- `commit`, `give` (moves a Record's `hold`), `oblige`, `release` have effect bodies
  (`effects_information.py:788,1038`; `effects_governance.py:207,376`, CHECKED).
- `succeed`, `tie / knot` rows are declined — no effect (L18 §5a; C12 §7).
**Life passes:** cohorts eat (EC §2) and could starve (inert); individuals could die of age/illness (inert); a seat
falls vacant when its holder dies (`test_in34_bodies_clock.py`, C12 §8). **Census**: a `dispatch` naming an absent id
mints a new person at the event's place, weight 1, age `age_at_build` (0), with `contain` but no `reside`, so he
counts in no population (C12 §4.3). No births, no growth, no generation turnover.

### 3 In the whole game
- **Cohorts** are the economy's mouths and the migration actors (D02 §4.1: cohort acts season 1 `migrate` 86,
  `survey` 44, `work` 39). They hold no seat, have no pursuit vector (ED-IN-0296 (2)) and cannot act through a seat
  (D02 §4.1). Their weight never moves (L17 §2 cl. 21).
- **Named individuals** are the deciders of every other subsystem (offices, contests, combat); they do not eat
  (ED-IN-0255 "it's a territorial issue") and, at shipped values, never age or sicken.
- `stance` is written at runtime only by `_eff_march` (grudges from battle) and `forgive` (its closer) (L18 §2 cl. 4;
  comment above `@effect_for("forgive")`, `effects_combat.py:~424-428`, CHECKED). `body` is lowered by combat and MATTER, raised only by
  `tend` (`verb_table.yaml:1162` per L18 §7).
- Feedback: march → grudge → regard → whom one listens to (`teller_weight`) → forgive closes it; wound → tend.
  Upward body band crossings are not emitted (`_crossings` downward only, H-211).

### 4 Built vs designed
| element | grade | evidence | what proposals say should exist and does not |
|---|---|---|---|
| Cohort persons (37, weight 2) | RUNS-IN-LOOP (seeded at world-gen) | `cohorts.yaml`, `harness/populated.py::seat_cohorts:387-438` (C12 §4.7) | cohort weight migration (M-WT-6); population growth (none) |
| `tend`, `train`, `forgive` | RUNS-IN-LOOP (bodies + generic candidate formation; executions unmeasured) | `effects_combat.py:370,396,430` CHECKED; `decision/options.py:167,182-192` CHECKED | M1 passive recovery arm, M2 care degree, M3 capability sources, M4 combat/choice readers (L18 §4) |
| `commit`, `oblige`, `release`, `give` (Records) | RUNS-IN-LOOP (bodies) | CHECKED above | `oblige`→`pledge` rename; `give` widened to Rungs (`cede`) |
| `succeed` (heir's claim) | DESIGN-ONLY | row declined; still emits `heir.designated` (L18 §5a) | `inheritance` conferral basis; claim opens throne `hold`, closes `off_heir` (IN-61) |
| `tie` (regard edge) | DESIGN-ONLY | `tie / knot` declined, no partner operand (H-182) | split; partner operand M8; typed tie M7 |
| `marry`, `kin` kind | DESIGN-ONLY | no row (L18 §5a) | two directed `kin` Tenures content `spouse`; consent obstacle [ASSUMPTION] |
| `hire`, `defect` | DESIGN-ONLY | no rows | `hire` shared with EC; `defect` = close A, open B in one write |
| Ageing, illness, seat vacancy on death | RUNS-IN-LOOP at control; live arm TESTS-ONLY | `fixtures.py:606-607`; `body_hazard` cohorts exempt (`world_q.py:1012`) | — |
| Births, children, `rear`, household, estate transmission (M11) | absent / DESIGN-ONLY | "children are not floor here today" (L18 §2 cl. 10); `hearth` is a building, not a family (C06 §5e: 211 hearth rungs = buildings) | ED-WR-0011 decides |

### 5 Structural handles for comparison
- **Resolution style:** deterministic effects; NP verbs carry no dice, threshold or magnitude in the lexicon (L18 §4);
  code magnitudes are whole-restore (`tend`) and +1 (`train`).
- **Granularity:** two-tier population — aggregate cohorts (headcount as `weight`) and individuated named NPCs;
  ad hoc individuation on demand (census).
- **State model:** persons as carriers with numeric dicts and edge Tenures; relationships = stance rows + Tenure
  edges to Propositions/seats; no person-to-person live edge kind in use.
- **Agency model:** every person (cohort or named) chooses verbs through the decision layer; no player-only verbs.
- **Information model:** regard mixes own stance with judged and told deeds (hearsay weighted 0.5).
- **Failure/recovery:** wounds recover only by `tend`; grudges only by `forgive`; death is permanent and vacates
  seats; no successor mechanism runs.
- **Content model:** authored cast (46) + authored cohorts (37); no generated persons except census stubs; no
  generational content.
- **Pacing:** seasonal; ageing clock would count seasons (`age_of`), off.

### 6 Open design decisions the sources name
- **ED-WR-0011** (`needs_jordan: true`): cast size and generations — do births happen? Decides `rear`, `child` kin,
  dynastic layer. The only Jordan item NP leaves (L18 §6).
- K-NPC-6 / D-V2 "is kin a tie kind?" answered by precedent; R-02 vs Suite D on `knot` owner (TW vs FI) unreconciled;
  R-11 vs Suite G on `succeed` owner (GV vs NP) unreconciled (L18 §6 notes); `hire` owner EC (R-01); IN-61 heir claim;
  J-13 capability-key remainder; H-206 vacancy reaching the heir (M12); H-211 upward crossings; ED-IN-0296 (2)
  cohort pursuit vector.

### 7 Conflicts, uncertainties, checks
- **L18 says `tend`, `train`, `forgive` are absent; the tree has them.** CHECKED `es/loop/effects_combat.py:370,396,430`
  (`@effect_for` present at HEAD `a4ca9a5`; `f2866d0` is an ancestor, CHECKED by `git merge-base`). L18's NP-G11..G17
  "absent" rows are stale; its M2/M3 asks partly answered in code by [ASSUMPTION] notes.
- Whether any normal season executes `tend`/`train`/`forgive` was not measured (no run; read-only brief). `train`
  declines unless the subject already holds the vocation key; only `copying` exists as a vocation (L18 §4; C06 §5b
  `verb_capability {tell: copying, speak: copying}`), so `train` is narrow by construction.
- G19 (gap register PC+NP) was not available in the extract directory; §6 uses L18 §6 only.
- Household: no source describes one; the nearest carrier, `hearth`, is a building rung (C06 §5e). Stated as absence
  inferred from the rosters, not from a ruling.

---

<!-- ===== A7 (S7_social_contest.md) ===== -->

# A7 · S7 — Social contest (SC), including proceedings (docket, bench, arrangements, speech kinds, `a matter`)

Sources: extracts C07 (code, HEAD a4ca9a5), L11 (lexicon proposal V11, PROPOSED), C06 (registries), C01 (dice core),
C02/C04/C05/C10 (loop, verb table, queries, effects), D02 (v9 remediation, base b70b5af), D05 (verb coverage). G20 does
not exist; §6 is built from L11 §6, C07 §7 and code. Checks and two runs I made at HEAD are in §7.

## Social contest — two implementations share one name. The season loop resolves every social act with ONE σ-leverage d10 roll that returns a margin (RUNS-IN-LOOP). The multi-exchange "Bout" kernel is standalone and tested but never called by the loop (TESTS-ONLY). The proceedings layer (docket, bench, arrangements) is half wired: the bench and docket are read, while arrangements and speech kinds are loaded but never read by any roll.

| | **(A) the season roll** — what the game runs | **(B) the Bout kernel** — what the design studied |
|---|---|---|
| where | `engine/season/seam/contest.py` → `seam/wrappers/sigma.py` (provider `social_contest`) → `modules/social_contest/roll.py::roll` (C07 §4A) | `systems/social_contest/sim/contest/` (`resolver.py::Bout`, `wrapper.py`, `modes.py`, `primitives.py`) (C07 §3B, §4B) |
| shape | one act = one d10 pool roll → `Margin(net, ob)` → `degree_from_net` → 1 of 4 bands (C07 §4A.7-8) | 1-5 exchanges ("budget") × 2 sides × 7 move kinds, accumulating per-side advancement, then a venue win-condition (C07 §4B.2) |
| output | a degree, never a winner (`roll.py:11-13`) | a winner or side label, `((band, reason), bout)` (C07 §4B.2) |
| rng | per-act generator from `draw_factory(world_seed, tick)` (C07 §4A step 4) | the global `random` module (`resolver.py:28-32`) |
| caller | `loop/resolve.py::_contest` / `_grade`, from `SeasonDriver` (C07 §6) | `engine/tests/test_contest_kernel.py` (subprocess, 389 checks), `agon_harness.py`, `faction.py` adapters; nothing under `engine/season/` (C07 §6) |
| grade | **RUNS-IN-LOOP** | **TESTS-ONLY** |

The code states that it keeps (A) and does not adopt (B): *"KEEP THIS ROLL, DO NOT ADOPT THE KERNEL … evaluated, not
deleted; the timing of its retirement is Jordan's, `SM-15`"* (`modules/social_contest/roll.py:16-18`, CHECKED). It gives
four reasons: no rng parameter, it returns a winner rather than a margin, it reads a faculty rather than the host's
record, and it costs 0.08-0.47 ms per call against 0.002 ms (`roll.py:19-35`). The proceedings design's own nested
multi-exchange run inside one act is a third design, and it is **unbuilt** (`roll.py:36-37`; `rosters.yaml:1078`
"the proceedings nested run is unbuilt", CHECKED).

### 1 What it is

A no-GM social conflict resolver. Its fantasy is the persuasive or adversarial speech act: telling someone something
and being believed, arguing a person into wanting something else, pleading a matter before a seated bench, and a bench
deciding that matter. In the shipped game each of these is one contested act inside the season loop. A person picks the
verb as an ordinary candidate, the act rolls once, and the band it lands in decides which writes and events the verb row
applies (C07 §4A; C04 verb table). The studied kernel serves a richer fantasy: a staged rhetorical bout with ground
(stasis), appeals (ethos/pathos/logos), stamina (Reserve), face (Standing), evidence (Dossier), judges with character,
and fatal faults (barred device, self-contradiction, evasion, silence), over named proceedings from `casual_dispute` to
`church_tribunal` (C07 §3B, §4B.8). The kernel is the design laboratory. The roll is the game.

### 2 Operating alone

#### 2A The season roll (RUNS-IN-LOOP)

**Entities and state.** `SocialContestInput` is a frozen record: `pool, opposition, obstacle_default, obstacle_ceiling,
obstacle_refusal_multiple, leverage, reception, reception_gain, proofs, proof_step, forgery_quality`. `Margin(net, ob)`
is its output (C07 §3A; `queries/inputs.py:36-96`). The roll holds no state between calls and never reads or writes
`World` (`roll.py:11-13`). Everything persistent lives in the world the verb row writes to, never in the contest.

**Procedure, one contested act** (C07 §4A, `loop/resolve.py:731-833`):
1. Resolve the verb's `contests:` prize through `rosters.yaml: contest_subsystems.prizes`. `a standing`, `a proposition`
   and `a matter` route to `module: social_contest, provider: social_contest, module_entry: social_contest.roll`. Only
   `a matter` carries `heard_by: "bench"` (C07 §4A; `rosters.yaml:1299-1319`, CHECKED).
2. Admission (`_admits`): the verb's typed precondition must hold, or the act folds to its refusal kind and no roll
   happens (C02 §4.5).
3. Sides: `claimants = [actor, target]`, where the target is `payload[row.counterparty or "subject"]`. The place
   (`rung`) is `world_q.place_of(actor)` (C07 §4A step 3; `loop/sides.py`).
4. Per-act rng: `draw_factory(w.world_seed, tick)(actor, "roll:<prize>:<act id>")` (C07 §4A step 4).
5. The adapter `sigma.py::resolve` builds the input (C07 §4A step 6):
   - `pool` = the actor's `capability[VERB_CAPABILITY[verb]]`, else `pool_default = 2`. `VERB_CAPABILITY` is only
     `{tell: copying, speak: copying}`, and *"Capability is empty on all but 1 of 430 corpus persons"*
     (`rosters.yaml:1222-1231`), so the pool is 2 for nearly every act.
   - `opposition` = the target's capability on the same key, if the target is a person holding it, else `None`.
   - `leverage = 0.0` always: *"zero until something supplies leverage"* (`sigma.py:160-162`, CHECKED).
   - for `a matter` only (`heard_by: bench`): `reception = world_q.reception(w, speaker, room)` and
     `proofs = world_q.proofs(...)`, with `reception_gain = 1.0` and `proof_step = 0.25` (C07 §3A fixtures).
   - for a graded inquiry (no prize): `forgery_quality` of the examined Record (C07 §4A step 6c).
6. `roll(inp, rng)` (`roll.py:124-125`, CHECKED): `net = roll_net(pool) + net_boost(leverage, pool)`. `roll_net` rolls
   `max(1, round(pool))` d10 at TN 7 with face values 1 → −1, 2-6 → 0, 7-9 → +1, 10 → +2 (C01 §4; C07 §4A.7).
   `net_boost` is the σ μ-shift, `soft_cap(x)·0.800·√pool`, `soft_cap = 1.5·tanh(x/1.5)`, and it is exactly 0 here
   because leverage is 0.
7. Obstacle (`roll.py:99-110`, CHECKED):
   `ob = opposition/2` (or `obstacle_default = 2`); `room = reception_gain·reception + proof_step·proofs`;
   `ob = max(ob − room, min(ob, OB_MIN=1))` if `room > 0`, else `ob − room`; `ob += forgery_quality`;
   `ob = min(ob, obstacle_ceiling = 2)`.
8. Refusal rule S27.4: `ob > 2 × pool` returns REFUSED. Under the shipped ceiling only a pool below 1 is ever refused
   (`sigma.py:238-240`; C07 §7).
9. Degree: `degree_from_net(net, ob)` with **no extension**. Margin `net − ob`: below 0 is Failure, [0,1) is Partial,
   [1,3) is Success, ≥3 is Overwhelming (C01 §4.4; C07 §4A.8).
10. `_fold` applies the verb row's `writes[degree]` / `emits[degree]`. The contest itself writes nothing
    (C07 §5 "writes nothing, ever").

**Consequence of the shipped constants (my computation, §7).** With pool 2 and Ob 2 (the default case for almost every
act), the exact band odds are Failure 0.74 · Partial 0.19 · Success 0.07 · Overwhelming 0.00. Pool 3 gives
.60/.228/.162/.01. Overwhelming is unreachable at pool 2, because 2d10 nets at most +4 and Overwhelming needs 5
(C01 §4.4 note, ruled "accept" by Jordan 2026-08-27). The ceiling of 2 equals the default, so a hostile room or a forgery
cannot raise a defaulted obstacle. A favourable room can lower it only to `OB_MIN` 1 (`roll.py` docstring, CHECKED).

**Graded inquiries.** `research`, `examine` and `surveil` have no prize. They reach the same provider through
`rosters.yaml: graded_inquiries` → `seam.grade` (C07 §4A "Graded inquiries"), and they use the same roll, ladder and
fixtures. They are Fieldwork verbs (S-FI) that borrow SC's roll.

#### 2B The Bout kernel (TESTS-ONLY)

**State per bout** (C07 §3B): two `_Side`s, each holding Standing (0-10, start 5, build/strip 0.8), Reserve (max 12;
move costs advance 3, hard 5, shift 4, support 2, pass 0, evidence 3, rebut 3; regain 4), FaultState and an optional
Dossier. Shared state is the live stasis ground (`fact < definition < quality < jurisdiction < consequence <
feasibility`, each tagged past/present/future), Room (cap 3.0), and `ContestState.adv`, *"the only authoritative tally"*
(`resolver.py:46-50`).

**Loop** (C07 §4B.2): for `i in range(venue.budget)`, side A then side B each choose a `Move` through a policy, which
reads a `ContestView`. Faults are checked after every move, and a fatal fault ends the bout at once ("clinch"). The
win-condition is checked once per exchange and again at close.

**One move's reception** (C07 §4B.4): `pool = max(5, 2·faculty+3)`; `lev = (faculty−4)/6 + 0.50`, with on-ground
hard-coded true; `net = roll_net(pool) + net_boost(lev, pool)`; degree from `degree_from_net(net, base_ob=2.0,
extension=PoolDesaturation)`, mapped to ordinal 0-3.

**Advancement** (C07 §4B.5): `gain = 2.6 · degree · resonance · readiness · U(0.92,1.08) · bias`. Resonance mixes the
venue's appeal weight with the judge's character through a "leak" set by judge discipline and the speaker's standing,
with a floor of 0.15. Readiness is `0.40 + 0.60·min(1, 0.4·standing_frac + 0.4·room_frac)`. Bias comes from external
`Pressure` toward one side. An ethos gain also builds Standing, and a pathos gain also builds Room.

**Win-conditions** (C07 §4B.6): ThresholdRace, TallyAtClose, ProofBar, GraceThreshold, PersuasionTrack (0-10 track with
five outcome bands A_total … committee … B_total), and VoteAtClose (jurors, noise, simple or standing-weighted). The data
holds 13 venues (`court`, `disputation`, `assembly`, `appeal`, … `secret_council`), 8 canonical PROCEEDINGS
(`formal_contest`, `grand_contest`, `royal_audience`, `church_tribunal`, `guild_arbitration`, `casual_dispute`,
`private_negotiation`, `personal_appeal`), 4 adjudicators and 11 policies (C07 §4B.7-4B.11). Opt-ins (C07 §4B.12): the
armature (style-axis dσ up to 0.50), CR4 (+1 pool on a genre match), CR5 (self-backfire of up to 2 Face), and faction
adapters (`vote`, `succession`, `coalition_vote`). Stubs: the `consensus`, `negotiation` and `inquiry` games,
`unanimity_required`, the Doubt Marker and InteractionType orientation (*"the resolver does not yet consume
orientation"*, `dictionaries.py:228-231`), and `Contest.stakes` and `resistance` (stored, never read) (C07 §7).

### 3 In the whole game

**Which verbs route where.** Contested rows come from `verb_table.yaml` (`contests:` / `counterparty:`), and the
graded-inquiry routes come from `rosters.yaml`. Counts are from my run (realm `build_realm(0)`, seed 0, 2 seasons, HEAD
a4ca9a5; one seed only, §7).

| verb | stratum | prize → path | opponent | bands write | bands emit | seen in the run | grade |
|---|---|---|---|---|---|---|---|
| `tell` | social | `a standing` → roll (A) | `to` (the hearer) | `[]` at every band | O/S/P `news.told`, `confidence.broken`; F `news.untold` | 23 resolved: `news.told` 4, Failure 19, plus 4 admission refusals (`news.untold` 23 in all) | RUNS-IN-LOOP |
| `speak` | social | `a matter` (heard_by bench) → roll (A) with room terms | `subject` (the docketed party) | `[]` at every band (H-63 stop, `verb_table.yaml` speak `writes_note`) | O `matter.carried`, S `.advanced`, P `.held`, F `.turned`; refusal `speech.unheard` | 3 resolved, all `matter.turned`; `speech.unheard` 18 | RUNS-IN-LOOP (thin) |
| `argue` | social | `a proposition` → roll (A) | `to` | O/S `Person.pursuits` (the hearer's); P/F `[]` | O/S `argument.won`+`pursuit.moved`; P `argument.won`; F `argument.lost` | `argument.refused` 10, none resolved | TESTS-ONLY in practice (wired; contest branch not reached in the run) |
| `determine` | binding_decision | `a proposition` → roll (A) | `subject` (the party) | O/S `Tenure.since, DocketItem.matter, Tenure.degree, Person.pursuits`; P the first three; F `[]` | O/S `matter.determined`+`pursuit.moved`; P `matter.determined`; F `matter.undetermined` | `determine.refused` 2, none resolved | TESTS-ONLY in practice (as `argue`) |
| `research`, `examine`, `surveil` | (FI) | graded route, no prize → roll (A), with forgery term | none | `[]` | O/S/P `finding.made`; F `finding.none` | research 14, surveil 30, examine 0 attempted (aperture, §7) | RUNS-IN-LOOP (research, surveil) |
| (B) kernel moves | — | no verb routes to it | — | — | — | — | TESTS-ONLY |

Sources: C07 §4A verb table, C04 table rows 2/11/38/42, `verb_table.yaml:131-166, 1068-1100` (CHECKED).
`fight`/`accept` (`the body`) and `march` (`a field`) share the same `seam.contest()` dispatcher but route elsewhere
(C07 §6).

**The proceedings layer: what "a matter" adds, and how much of it is wired.**
- *Docket.* `petition` mints a petition Record, `carry` appends it to `World.docket`, and `open_case` (`remit:determine`)
  mints a case file plus a DocketItem. `convene` writes a `Date`. `speak` requires a DocketItem naming its subject, and
  `determine` requires a fired Date with a DocketItem plus a non-empty bench (L11 §2b; C04). In the run: `petition.filed`
  14, `case.opened` 6, no `petition.carried` (`carry` mis-forms, D02 §4.3).
- *Bench.* `world_q.judging_set(w, venue)` is the live holders of a `hold` Tenure granted `determine` whose Office's scope
  contains the venue. An empty set lets the date lapse (`world_q.py:439-447`, CHECKED). For `a matter` the bench shapes
  the obstacle through `reception` (each bench member's deeds-ledger regard for the speaker, with "route erosion") and
  `proofs` (the speaker's attributed deeds against the opponent that the opponent does not mirror) (C07 §4A "Room
  terms"). This is the only social input that varies person to person on the season path.
- *Arrangements.* `arrangements.yaml` holds 8 rows: `arbitration`, `parliamentary_debate`, `council_of_state`,
  `legal_trial`, `tribunal`, `interrogation`, `inquisition_hearing`, `excommunication_deliberation`. Each has 14 keys
  (`disposal, bench_basis, floor, order, disposes, disposal_reach, proofs, interposed, quorum`, …), and the loader is
  closed-set (C06 §4d, §5d; CHECKED ids at `arrangements.yaml:106-265`). The game reads one key, `disposes`, which
  chooses the Tenure kind `determine` opens (`oblige`/`detain`/`ban`), and only when a docket item names a row
  (`effects_information.py:514-520`, CHECKED). *"`None` -- every computed case -- is the realm's path"*
  (`effects_information.py:331-332`, CHECKED). So computed play never selects an arrangement, and `judging_set` ignores
  its `matter` argument: *"nothing yet maps a docketed matter to its governing arrangement row"* (`world_q.py:458-464`,
  CHECKED). Order, floor, proofs, interposition and quorum have no reader.
- *Speech kinds.* There are 6 rows (`deny, cite_incompatible, impugn_motive, concede_fact, concede_harm,
  hand_error_back`, all `forensic`, `min_rank: hearth`), only `impugn_motive` is capped at Partial, and the header notes
  *"SIX OF TEN, NAMED SCOPE-DOWN"* (C06 §5d). No reader exists: `speak` carries no speech-kind operand, and the roll has
  none (C07 §5; L11 §2 claim 19 "a reader of speech kinds, proofs or genres" lacking). DESIGN-ONLY as mechanism, though
  loaded as data.

**What reads SC's outputs.**
- `tell` → WITNESS told channel. On `news.told` the hearer receives `Claim(..., "told_by", teller's confidence, chain +
  teller)`. At Partial the content drifts: one `to` id is dropped, or a number drifts within `told_drift_band`. Failure
  transmits nothing (C02 §4.7(5); D05 l.137). A hearer holding a contrary firsthand claim refracts it by
  `refraction_gain 0.5` (D05 l.132). Told claims feed `claim_landed` questions → candidates and known-false vetoes in the
  chooser (C02; D05 flow l.213-229). In the run: `told_by` claims 2245 against `firsthand` 6380 (aperture).
- `speak` → only witnessed `matter.*` events: *"hearers hold which way the matter went"* (`verb_table.yaml` speak
  `writes_note`). No extract names a reader that decides on them.
- `argue` → the hearer's `Person.pursuits` moves toward the arguer's weight by `pursuit_shift × DEGREE_STEP[band]` (H-221,
  `[ASSUMPTION; medium; Jordan to correct]`, `verb_table.yaml:146`, CHECKED). Pursuits drive the chooser's value scoring
  (C04). `argue` is the argument half of the `(Person, pursuits)` writer pair, *"moved by argument and consequence, never
  by evidence"* (`verb_table.yaml:146`).
- `determine` → a disposal Tenure on the party, `Tenure.degree`, and the matter removed from the docket. Its
  `Person.pursuits` write moves **the judge's** own pursuits (`consequence_pursuits(judge, …)`,
  `effects_information.py:529-531`, CHECKED), not the party's.

**Feedback loops.**
1. Rumour: `tell` → told claims → questions → more `tell`s. Content travels only by `tell`, so the world is
   *"consistent, and therefore deception-free"* (D05 l.232).
2. Docket: petition → case → Date → bench → `speak`/`determine` → tenure on a person → that person's options.
3. Values: `argue`/`determine` → pursuits → what persons choose next.
Loops 2 and 3 are wired but were not observed closing in the one run.

**Escalation ladder named by D05** (l.231): `tell` → `argue` → `petition`/`open_case` → `determine` → `seize`.

### 4 Built vs designed

| element | grade | evidence | what the proposals say should exist and does not |
|---|---|---|---|
| season roll (A): pool, obstacle, S27.4, 4-band ladder | RUNS-IN-LOOP | C07 §4A; run counts §3 | nested multi-exchange run inside one act (`21_RECONCILIATION.md` step 15) — unbuilt (`roll.py:36-37`) |
| pool from capability | RUNS-IN-LOOP, degenerate | `VERB_CAPABILITY` maps 2 verbs; capability on 1 of 430 persons (`rosters.yaml:1222-1231`) | hearer-competence carrier (SC-G22); teller's standing in the obstacle (SC-G21, M10) |
| leverage (σ μ-shift) | DESIGN-ONLY on this path (always 0) | `sigma.py:160-162` | a producer of leverage |
| obstacle ceiling 2 (H-213), room terms (H-215/H-216), forgery term | RUNS-IN-LOOP (swept fixtures) | `roll.py:99-110`; tests `test_sc01_obstacle_ceiling`, `test_sc02_reception` | forgery reaches the roll only when the ceiling is above 2 (`roll.py` docstring) |
| pool-desaturation degree extension | TESTS-ONLY (kernel only) | season `degree_of` passes none (C07 §7) | — |
| `tell` | RUNS-IN-LOOP | §3 | regard/valence reader so praise/flattery/insult move anything (M14, H-194/H-196) |
| `speak` contested on `a matter` | RUNS-IN-LOOP (3 resolved) | §3 | band writes `Person.stance` / `DocketItem.matter` (H-63; `04_VERBS.md` §B.1); `issue` stasis rung on the docket item (M7); speech-kind reader (M8) |
| `argue` | TESTS-ONLY in practice | row `verb_table.yaml:131`, `_eff_argue` (C10 §130) | V11 renames it `persuade` with `reason`/`appeal` manners (L11 §4 Suite 2) |
| `determine` contested | TESTS-ONLY in practice | row + `_eff_determine` | Record disposal for parliament/council (M5, `DISPOSABLE_KINDS`); cardinality vote count (M12) |
| docket / bench (`judging_set`) | RUNS-IN-LOOP | `case.opened` 6; bench read by reception | matter → arrangement mapping ("PHASE 2 step 10", `world_q.py:458-464`); Date holder (M1) |
| arrangements (8 rows) | TESTS-ONLY (only `disposes`, only when hand-named) | `effects_information.py:331-336, 514-520` | computed-case arrangement (M2: "a killing → `legal_trial`; a heresy → `tribunal`"); `negotiation`, public debate, audience, appeal, succession rows unseeded (C06 §5d) |
| speech kinds (6 of 10) | DESIGN-ONLY | no reader (C07, L11) | `object`, `define` and state moves per kind (L11 §2 claim 33, `[ASSUMPTION]`) |
| proofs roster `record, testimony, oath, confession` | DESIGN-ONLY as a reader (`proofs` here is a deeds count) | L11 §4 M9 | bench weighs the proof kinds and `forgery_quality` (M9) |
| `utter`/`commit`/`petition`/`carry`/`open_case`/`convene` (SC-lane non-contested rows) | RUNS-IN-LOOP for `utter` 39, `petition` 14, `open_case` 6 (run); `carry`, `commit` mis-form (D02) | run; D02 REM-23/25 | renames `utter`→`declare` (withdrawn by R-06), `carry`→`lodge` (R-10) (L11 §2) |
| `lie`, `interrogate`, `preach`, `mediate`, `filibuster`, threat reader | DESIGN-ONLY | no row (L11 §2b) | J-C-6, M15, SC-G48 clock, SC-04 |
| Bout kernel (B) | TESTS-ONLY | 389/389 checks pass (my run, §7) | retirement timing is Jordan's (SM-15) |
| kernel games `consensus`/`negotiation`/`inquiry`, unanimity, Doubt Marker, stakes, resistance | DESIGN-ONLY (stubs/unread) | C07 §7 | ED-1060 (orientation) |

### 5 Structural handles for comparison

- **Resolution style.** (A): one opposed-difficulty dice-pool roll per act. The pool is a count of d10s scored by success
  count at TN 7, with 1s subtracting and 10s doubling. Against a fixed obstacle this gives graded success in four bands
  (margin ladder). Advantage is designed as a mean shift, but it is zero today. (B): an exchange-based contest of
  alternating moves with a stamina economy and positional ground. It resolves either by threshold race or by judged
  tally/vote at close, with immediate loss on fatal faults (a "sudden-death fault" catalogue).
- **Granularity.** (A): one roll per act, at most one act per person per scene slot; no rounds. (B): 1-5 exchanges × 2
  moves.
- **Scale.** Person-to-person (`tell`, `argue`), person before an institution (`speak`), and institution on a person
  (`determine`), all at the person/season scale. Faction-scale votes and successions exist only in the kernel's adapters.
- **State model.** (A) is stateless. Outcomes persist only as world writes and claims. A matter's progress has no
  persistent track (no `issue` rung). (B) holds per-bout Standing, Reserve, Room and advancement, discarded at the end.
- **Agency model.** No GM. The NPC chooser picks the verb and target from its own ledger. The opponent does not choose:
  opposition is a static score (capability/2) or a default. The bench does not act as agents in (A); its members' ledgers
  set a number. In (B) both sides choose moves through policies, and the judge is a parameter object.
- **Information model.** Imperfect and asymmetric. The chooser never sees the hearer's capability or beliefs, and
  hostility enters only as stance toward the subject (D05 l.137, l.249). Told content arrives at the teller's confidence
  and can drift at Partial. There is no deception channel for speech (no `lie`). Documents can be forged, but forgery is
  read only by inquiries, under a ceiling.
- **Failure and recovery.** A failed act costs the scene slot and transmits or writes nothing. Refusals (no docket, pool
  below 1D) emit a refusal kind and do not crash. There is no "failing forward" write on Failure for `speak`, `argue` or
  `determine`. Partial is degraded success: drifted content for `tell`, a determination without pursuit movement for
  `determine`.
- **Content model.** Authored closed sets in data: prizes, arrangements, speech kinds, venues and proceedings. Who speaks
  to whom, about what, is generated by the chooser from world state. There is no authored dialogue.
- **Pacing.** Season-loop cadence: a proceeding is one act inside RESOLVE ("the proceeding is ONE act at the season
  scale", `verb_table.yaml:1079`). Sittings are gated by `convene`'s Dates. A matter can be docketed one season and heard
  in a later one.

### 6 Open design decisions the sources name (ids)

| id | the question | source |
|---|---|---|
| SM-15 | when to retire the Bout kernel (kept, evaluated, not adopted) | `roll.py:16-18` |
| J-C-6 (= D-V4) | may a person lie? V11 recommends yes: build the proofs reader M9 first, then a `lie` row sharing `tell`'s cell and kinds | L11 §6 |
| H-63 | what `speak`'s bands write (stance value; Partial docket append has no carrier) | `verb_table.yaml` speak `writes_note` |
| H-221 | which way and how far `argue` moves pursuits; *"Jordan to correct"* | `verb_table.yaml:146` |
| H-213 / H-215 / H-216 | obstacle ceiling (1/2/3/None), `reception_gain` (0/1/2), `proof_step` (0/.25/.5): swept fixtures, shipped values `[assumption]` | C07 §3A |
| H-62 | producer of `Person.pursuits` by argument; `argue` row now answers it at assumption grade | L11 claim 19; `verb_table.yaml:146` |
| ED-1060 | whether the kernel consumes orientation (Doubt Marker, InteractionType) | C07 §7 |
| PHASE 2 step 10 (proceedings plan) | docketing: mapping a matter to its arrangement row ("left OPEN") | `world_q.py:458-464` |
| D-V3 | a public route for a petition denial | L11 §6 |
| D-V6 | one mood-keyed alignment cell for WAR, charge, THREAT | L11 §6 |
| SC-04 | seeding unseeded games (`negotiation`, etc.); dead arrangement keys SC-G45 | L11 §6 |
| SC-G21 / SC-G22 | teller's standing in the obstacle; hearer competence | L11 §4 |
| SC-G39 / H-210 | nothing reads `forgery_quality` beyond the inquiry obstacle | L11 §4; `roll.py` |
| SC-G48 | filibuster needs a clock the provider lacks | L11 §4 |
| R-06 / R-07 / R-14 / R-24 | ownership/naming rulings V11 contradicts in its own body (`utter`→`declare` withdrawn; `interrogate` SC's; `forge` FI's; `dispute` unrowed) | L11 §2 claims 4-8 |
| REM-06 | R-09's third conjunct should require a non-combat verb resolving at ≥2 bands with differing writes; `speak`'s all-empty bands no longer count, so `determine` is the live candidate | D02 §4.0 |

### 7 Conflicts, uncertainties, checks made

**Conflicts between sources:**
1. *Arrangement count.* V11 says "seven arrangements" (L11 claim 18), while C06 ran the loader and found 8.
   `arrangements.yaml` has 8 `- id:` rows (CHECKED `arrangements.yaml:106-265`). I take 8.
2. *`speak` at HEAD.* V11 describes `speak` as uncontested, writing nothing and emitting `speech.made` (L11 claim 13).
   The HEAD row is contested on `a matter`, has a DocketItem precondition, four `matter.*` kinds and `speech.unheard`
   (L11 §2b; CHECKED `verb_table.yaml:1068-1093`). V11 is stale.
3. *`argue`.* V11 and D05 call it planned or new (`persuade`). A row exists with an effect body, and it is resolvable
   (C04 row 2; CHECKED `verb_table.yaml:131-166`). The proposal is stale on existence. The rename to `persuade` stays
   DESIGN-ONLY.
4. *Does `speak` ever resolve in a season?* D02 §4.3 lists `matter.*` as never emitted in either world at 2 seasons,
   seed 0, base b70b5af. My run at a4ca9a5 shows `matter.turned` 3. Commit f2866d0 ("B-P proceedings tail") sits between
   the two bases, which is the likely cause, but I did not bisect. I believe my run for HEAD.
5. *`determine` executions.* D05 l.231 cites "`determine` 3" in an older four-season probe. My run has 0 resolved and 2
   refused at 2 seasons. These are different horizons and ages, so it is not a contradiction. Either way, the grade of
   `determine`'s contest branch in a normal season is uncertain.
6. *`determine` writes.* V11 lists `Tenure.degree` and `Person.pursuits` writers as lacking. The row declares both
   (L11 §2b). The effect writes the judge's pursuits (CHECKED `effects_information.py:529-531`).
7. *Kernel test count.* The docstring running total says 303 while the pin is 389 (C07 §7). The run gives 389.
8. *Two "proceeding" vocabularies.* The kernel's 8 PROCEEDINGS (`formal_contest` …) and the season's 8 arrangements
   (`arbitration` …) share no names. `grep` for kernel proceeding names under `engine/` and `modules/` hits only the
   kernel test and a docstring in `roll.py`. No mapping exists.
9. V11's internal contradictions (R-06, R-07, R-14, R-24 vs its body) are unresolved. V11 says the roster `verbs-03`
   governs, and that roster was not read (L11 §2).

**Uncertainties.** All run figures come from one seed (0), one world (realm) and 2 seasons, so they are existence
evidence, not rates. Whether `argue` or `determine` reach their contest branch at longer horizons is unmeasured. The
bodies of `world_q.reception` / `proofs` were read only through their docstrings (C07 §1).

**Checks made (opened or run by me):**
- CHECKED `modules/social_contest/roll.py:16-37`: KEEP THIS ROLL, the four reasons, nested run unbuilt.
- CHECKED `modules/social_contest/roll.py:99-110, 124-125`: obstacle composition and `Margin(net, ob)`.
- CHECKED `engine/season/seam/wrappers/sigma.py:160-162, 253-260`: leverage zero; `heard_by == bench` selects the room.
- CHECKED `engine/season/rosters.yaml:1078, 1299-1319`: prize rows → `social_contest.roll`; "the proceedings nested
  run is unbuilt".
- CHECKED `engine/season/verb_table.yaml:131-166` (`argue`), `:1068-1093` (`speak`).
- CHECKED `engine/season/arrangements.yaml:56-265`: 6 speech kinds, 8 arrangements.
- CHECKED `engine/season/queries/world_q.py:439-464`: bench definition; `matter` not load-bearing.
- CHECKED `engine/season/loop/effects_information.py:325-336, 514-531`: arrangements read only via `disposes` on a named
  row; computed cases pass `None`; `determine` moves the judge's pursuits.
- CHECKED `engine/tests/test_contest_kernel.py:89,93`: floor 151 and pin 389.
- RAN `python -m systems.social_contest.sim.contest._kernel_tests` → `RESULT: 389 passed, 0 failed` (19.5 s).
- RAN `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 0` and a `populated.run(seasons=2, seed=0)` event-kind
  count on `build_realm(0)`. SC kinds: `news.told` 4, `news.untold` 23, `matter.turned` 3, `speech.unheard` 18,
  `argument.refused` 10, `determine.refused` 2, `case.opened` 6, `petition.filed` 14, `proposition.uttered` 39,
  `finding.made` 56, `finding.none` 250. The working tree was unchanged after both runs (`git status` empty).
- COMPUTED exact band odds at Ob 2 over all d10 face combinations with `_die_result` and `degree_from_net`: pool 1
  F .90/P .10; pool 2 F .74/P .19/S .07/O 0; pool 3 .60/.228/.162/.01; pool 4 .488/.232/.242/.038.

---

<!-- ===== A8 (S8_fieldwork_information.md) ===== -->

# A8 · S8 — Fieldwork / investigation (FI) and information and epistemics across the game

Sources: extracts C10 (code), L12 (lexicon `verbs-12`, PROPOSED 2026-10-17), C02 §4.3/§4.9, D05 (verbs Parts 05-06, PROPOSED 2026-10-16), C04, C05. G20 does not exist; §6 is built from L12 §6 and C10 §7. One execution run was made for this section (seed-0 realm, 2 seasons; "RUN" below; method in §7 of block B). Grades: RUNS-IN-LOOP / TESTS-ONLY / DESIGN-ONLY, as the brief defines them.

---

## A. FIELDWORK / INVESTIGATION (FI) — six inquiry verbs and four document makers that run in the season loop, graded by a borrowed social-contest roll, and in the shipped realm uncover nothing (RUNS-IN-LOOP, inert in yield); the `knots` module is a separate unplugged sim (TESTS-ONLY)

### A1 What it is
Fieldwork is the game's investigation layer: a person examines a place, interviews a person, researches a Record (a world-side document), surveils a Rung (a place in the containment tree), reconstructs a deed from what he already believes, or reads threads; separately he can survey (write an account of a faction), forge (write a false account), conceal (assume a cover identity), and create, give or destroy Records. The fantasy is the detective's and the spymaster's: learning who did what, hiding what you did, and planting false paper. Jordan's ruling fixes its shape: *"investigation is not a contest seam. it is its own thing."* (C10 §2, `seam/wrappers/fieldwork.py:4-7`). There is no GM; the engine chooses for every person, so an investigation is something an NPC decides to do, not a player scene (`requirements.yaml:169-172` lists the "investigations / detective / interactive fiction" scale `in_loop: false`; CHECKED).

### A2 Operating alone
**Entities.** `Claim` (a belief, in a person's own ledger; fields `holder, subject, predicate, value, when, source, confidence, visibility, round, chain, doer`; C10 §3a). `Record` (a document; `kind`, `subject_matter`, `stages`, `forgery_quality`; minted only by `_mint_document`, `effects_information.py:170-196`; C10 §4e). `Proposition` (an immutable uttered statement, mood default `"OUGHT"`; `effects_information.py:1001-1035`). `Seen` (what a witness saw: `stratum, marks, who, why`, `None` = withheld; `epistemic.py:873-889`). `FieldworkInput(band, items, terms)` / `Findings` (C10 §4b.2-3).

**The inquiry procedure, as executed** (C10 §4b; CHECKED `resolve.py:1060-1080`):
1. The chooser forms an inquiry act. Eligibility is `own` for all six rows (CHECKED `verb_table.yaml:1324,1350,1366,1387,1426`), so anyone may attempt one; `presence:` alternatives always decline person-side (H-33; CHECKED `decision/options.py:623-625`).
2. RESOLVE folds it. Inquiries write nothing (`writes: []`). Three are graded — `research`, `examine`, `surveil` — by the `social_contest.roll` entry through the `graded_inquiries` routing row, "NOT a prize and NOT a `contests:` shape" (CHECKED `rosters.yaml:1107-1122`); pool `pool_default`, obstacle `obstacle_default` (C10 §4b.8). `interview`, `reconstruct` are ungraded (no degree); `thread_read` is unresolvable (`requires_typed: none`, waits on H-85).
3. Emits: Overwhelming/Success/Partial → `finding.made`; Failure → `finding.none`; refusal (precondition failed) → also `finding.none` (C10 §4a; L12 §8 H14).
4. For every Event, `find_trail` dispatches by kind through `rosters.yaml: inquiry_modules`; only `finding.made` has a row (`module_entry: fieldwork.find`) (CHECKED `resolve.py:1077`).
5. Host adapter builds `FieldworkInput`: `band = event.degree`, `items` = `trail_of(w, subject, actor)`, `terms = FINDING_TERMS` (C10 §4b.2).
6. `trail_of`: for each kind in `COVERT_KINDS` (only `record.forged`) and each side, the last emission on the subject, skipping the finder's own deeds and ones he already holds (`holds_trail`). Docstring: reachable "ONLY THROUGH A PLANT" (C10 §4b.4).
7. `modules/fieldwork/find.py::find`: `shown = terms[band]`; returns `(event_id, shown)` per trail item ordered by emission. No RNG, no World read; "THIN BY DESIGN" (C10 §4b.3).
8. WITNESS `_found_claims` deposits into the finder's ledger one event-kind Claim per subject plus one `seen` Claim masked to the band's terms; source `inferred` (`FOUND_CHANNEL = SEAT_CHANNEL = "post_remit"`, CHECKED `witness.py:265,276`), marked `[ASSUMPTION; medium; Jordan to correct]` (C02 §7, `witness.py:263-264`).
9. `finding.none` is in `UNDEPOSITED_KINDS`: Failure and refusal teach the actor nothing (C10 §4b.7).

**Constants.** `finding_terms.bands`: Overwhelming `[stratum, marks, who]`, Success `[stratum, marks, who]`, Partial `[stratum, marks]` ("A PARTIAL FINDING WITHHOLDS `who`"), Failure/ungraded: no row (C10 §3c, §7; `[ASSUMPTION; medium; Jordan to correct]`). `default_forgery_quality=1`, `record_stages_default=3`, `record_stage_term=1`, `pursuit_shift=0.1` (C10 §3c). `forgery_quality` is added to an inquiry's obstacle on a Record, but "AT THE SHIPPED H-213 CEILING … THE QUALITY CANNOT RAISE A DEFAULTED INQUIRY'S OBSTACLE" (C10 §4b.8).

**Document makers** (C10 §4e table): `survey` mints a `faction_sheet` (a frozen `faction_q.resolve` snapshot) into the surveyor's hold; WITNESS's content deposit then puts the sheet's content into his ledger ("a held document is a held belief", C10 §4c.10). `forge` = `survey` plus `sheet[_FORGED_SHEET_KEY] = actor` and `forgery_quality = 1`; emits `record.forged`. `conceal` mints a `cover` Record naming the actor; while live, `anchor_of` resolves his acts to the cover id — "Nothing about who ACTED changes … `seen.who` … still names him to those present" (CHECKED `state/attribution.py:105-122`). `create_record`, `issue`, `covenant`, `petition`, `open_case`, `carry`, `determine`, `argue`, `give`, `seize`, `destroy_record`, `utter`, `commit` per C10 §4e.

**Knots (sim, separate).** `systems/fieldwork/sim/knots.py`: a bond between two actors with tier `Distant|Close`, strain gauge, rupture. Formation needs bonds ≥ 5, disposition ≥ 5, one party TS ≥ 30, a d10 roll `pool = spirit*2 + history_relationships` at TN 7, Ob 2: Overwhelming → Close, Success → Distant. `TIER_RANGE = {Distant: (-2,5), Close: (-5,5)}`, `TIER_START = {Distant: 0, Close: -2}`, breaks at strain ≥ 5; Close at strain ≤ −5 "tempered" absorbs one rupture. Loss: break → composure 4, disposition −3, Close-with-positive-strain conviction Scar 1; rupture → disposition −3, coherence −1 (`[UNVERIFIED post-ED-912]`). Composure and disposition are returned, not applied (C10 §3d, §4f).

### A3 In the whole game
- **Invoked by** the decision layer's `opening_set`/`choose` for any person (no player-only path); RUN: 115 inquiry acts resolved over 2 seasons (`reconstruct` 39, `interview` 32, `surveil` 30, `research` 14; `examine` formed and refused only). `survey` 57, `forge` 52, `conceal` 19, `create_record` 87, `utter` 39, `petition` 42.
- **Reads:** `w.last_emission_of` (the log), ledgers (`holds_trail`), `w.records`, tenures (holds), `VERB_TABLE` strata, `finding_terms` (C10 §5).
- **Writes:** inquiries nothing to the world; findings only to the finder's ledger at WITNESS. Document makers write `w.records`, `w.propositions`, `w.tenures`, `w.docket`, `Person.pursuits` (`argue`) (C10 §5).
- **Who reads its outputs:** the finder's later choices (claims → questions, known-false veto; block B); others only via `tell`/`give`; WITNESS (those present learn that he inquired — `finding.made` is itself deposited); attribution (`anchor_of` through covers); social contest's input builder reads `Record.forgery_quality` (`seam/wrappers/sigma.py:191`, L12 §8 H3); social-contest `proofs`/`reception` read deed claims (C05). L12 §2.24 lists SC proceedings reading proof kinds as unbuilt (`determine` reads none, FI-G47).
- **Feedback loop as designed:** forge → give (plant) → research finds `record.forged` trail → finder knows the forger → tells / prosecutes. **As run:** `give` 16 attempts, all `give.refused`; so no plant, `trail_of` empty, and every graded `finding.made` (RUN: 8 Partial, 4 Success) deposits nothing beyond the generic event deposit (0 two-cause `found` deposits; 0 `inferred` claims). The 44 ungraded `finding.made` (reconstruct 33, interview 11) carry degree `None` and uncover nothing by construction. 250 `finding.none` (218 refusals, 32 rolled Failures) deposit nothing.
- **Knots:** no caller from the season loop ("knots/ is an island (no campaign callers)", `test_knots_ed912.py:16`; C10 §6). The engine's own `knot` is a different thing: a Tenure kind read by `_ch_witness_key`; its opener `tie / knot` is not resolvable (effect declined H-182) — RUN: `resolvable_verbs()` omits it.

### A4 Built vs designed
| element | grade | evidence | what the proposals say should exist and does not |
|---|---|---|---|
| six inquiry rows, formed and folded | RUNS-IN-LOOP | RUN counts above; `resolvable_verbs()` includes five (RUN) | `examine` bound to a Rung, not a Site (L12 §2.25, FI-G05) |
| graded roll (`research/examine/surveil`) | RUNS-IN-LOOP | RUN degrees Partial 8, Success 4, Failure 32 | Ob = concealer's score/2 (M4); stored score J-T1 (L12 §4.2) |
| `find_trail` → `fieldwork.find` dispatch | RUNS-IN-LOOP (empty) | `resolve.py:1077`; RUN 0 found deposits | a yield per inquiry (selector table, L12 §4.1, M1) |
| `_found_claims` deposit | TESTS-ONLY | `test_fi03_trail.py` (24 tests, planted world); RUN 0 `inferred` | source at remove 0, confidence by degree (L12 §2.14) |
| Failure ≠ refusal | DESIGN-ONLY | both emit `finding.none` (L12 §8 H14) | M2 `inquiry.refused`; Failure deposits per table |
| honest misreading on Failure | DESIGN-ONLY | not built (K-37) | M3: wrong `who` from candidate set (L12 §2.20) |
| `interview` reply | DESIGN-ONLY | F8 forbids reading another's ledger (L12 §2.33) | J1 option (b): reply as the interviewee's own act |
| `reconstruct` deed attribution | DESIGN-ONLY (row runs, ungraded) | degree `None` (RUN) | Ob = base − 1 per supporting claim (L12 §4.2) |
| `thread_read` | DESIGN-ONLY | not resolvable (RUN); H-85 | TW owns the gate (L12 R-13) |
| `survey` + content deposit | RUNS-IN-LOOP | RUN 13 `faction.surveyed`, 25 `faction_sheet`; 44 `survey.refused` | `rung_sheet` (M7); `audit`/`census`/`scout` folds |
| `forge` + `forgery_quality=1` | RUNS-IN-LOOP (quality inert) | RUN 12 `record.forged`; H-213 ceiling (C10 §4b.8) | quality = forger's score/2; emit twin kind `faction.surveyed` (L12 §2.44) |
| `conceal` / cover → `anchor_of` | RUNS-IN-LOOP | RUN 19 `cover.assumed`, 19 `cover` Records; `attribution.py:118-121` | cover grade (M4); scope `room` hides `seen.who` (`disguise`); failed covered act breaks cover |
| `create_record/utter/petition/issue/open_case` | RUNS-IN-LOOP | RUN 87/39/14/5/6 | — |
| `give` (planting) | RUNS-IN-LOOP, all refused | RUN 16 `give.refused` | — |
| `destroy_record` | not formed in loop | `withheld_verbs=("destroy_record",)` (C04 §4.2.1); H-75 | M6 typed `hold:` eligibility |
| `bribe`, `infiltrate`, `shadow`, `search`, `track`, `watch` rename, `decipher`, `intercept`, `eavesdrop` | DESIGN-ONLY | L12 §5 roster | as listed in L12 §5 |
| canon price "+2 Exposure" | DESIGN-ONLY | no meter (L12 §2.19) | — |
| knots sim (formation/strain/rupture/loss) | TESTS-ONLY | `engine/tests/test_knots_ed912.py` only caller | TW's `trace` "knot-mediated remote inquiry" (L12 §5) |
| engine `knot` Tenure via `tie / knot` | DESIGN-ONLY | effect declined H-182; RUN 0 `firsthand_via_knot` | — |

### A5 Structural handles for comparison
- **Resolution style:** a single d10 pool roll against a default obstacle, borrowed from the social-contest module, for three verbs; deterministic table lookup (`band → terms`) for what is uncovered; no opposed roll, no clue economy.
- **Granularity:** one act per inquiry, inside a scene, one season = up to `scene_budget=5` rounds (C02 §3).
- **Scale:** personal; the outputs (Records, covers) persist at world scale.
- **State model:** event-sourced. Truth = the Event log; knowledge = per-person Claim lists; documents = Records with holders (hold Tenures).
- **Agency model:** engine-chosen for everyone (utility chooser); investigation is not a mode the player enters (`in_loop: false`).
- **Information model:** the finder learns only via WITNESS; a band masks `who` (Partial) — partial knowledge is the term mask on a `Seen`.
- **Failure/recovery:** Failure and refusal are silent to the actor (deposit nothing); no misdirection built; covers lapse by Record stages (designed, L12 §4.2).
- **Content model:** generated — trails are whatever covert Events the log holds; no authored clue sets.
- **Pacing:** findings deposit the round after RESOLVE at WITNESS; trails read the log "as PREVIOUS rounds left it" (`resolve.py:1066-1068`).

### A6 Open design decisions the sources name
J1 (interview reply; lexicon recommends (b), `[CONFIDENCE: medium]`); J-T1 (stored score / pool; FI-G14, FI-G45); J-C-6 (lying; gates `suborn`); Q1 (forgery write formula); Q4 / ED-FI-0004 (Dialogue Lattice, ruled "Lattice first"); ED-FI-0002 (counter-espionage; FI-G42); FI-G15, FI-G37, FI-G44 (disputed); FI-G07, G17, G31, G32, G51 (parked); FI-G52 (`watch` alignment null by ruling); M1-M10 (named mechanics, L12 §5); K-36 (interview a prompt), K-37 (value space for misreading/reconstruct); H-85 (TS ≥ 30 carrier), H-111 (is a failed inquiry news; lexicon answers "yes, already running"), H-75 (`hold:` placeholder), H-210 (forgery writer+reader together), H-213 (obstacle ceiling), H-126 (obstacle sweep), H-182 (`tie / knot` effect); `finding_terms` and `FOUND_CHANNEL` `[ASSUMPTION; medium; Jordan to correct]`; thread_read owner TW vs FI; `destroy_record` naming (L-15); `bribe`/D-V6 (L12 §6).

### A7 Conflicts, uncertainties, checks (FI)
- **L12 (lexicon, 2026-10-17) is stale against HEAD on four points**, per its own extractor (L12 §8) and confirmed here: `conceal` is built (RUN: 19 covers), `forgery_quality` is written (=1) and read (sigma.py:191), `_found_claims` exists (CHECKED `witness.py:276`; L12 §8 H2's grep failure is REFUTED), `surveil` is not renamed. I believe HEAD.
- **D05 "inquiries yield no content (R-C-23)"** is stale as a statement about code (the producer exists) but true as a statement about the seed-0 realm (RUN: 0 found deposits).
- **"Investigation `in_loop: false`"** (`requirements.yaml:172`) vs RUN showing inquiry acts in the loop: not a contradiction; the register grades the *scale* (a playable investigation mode), the verbs run with no yield.
- Uncertain: why every `give` is refused in seed 0 (not traced); whether `examine` is ever admitted (RUN: 0 resolved; 62 `finding.none`).

---

## B. INFORMATION AND EPISTEMICS ACROSS THE GAME — every Event is fanned at WITNESS through five ranked channels into per-person Claim ledgers, refracted, decayed and capped; the chooser sees only its own ledger (RUNS-IN-LOOP; hearsay-with-chain, privacy, drift, knot and obligee channels inert at seed 0)

### B1 What it is
This is the information model of the whole engine, not a subsystem players enter. The world holds one Event log (truth); each person holds a ledger of Claims (belief) that only the WITNESS step writes. Who learns an Event depends on where he stood, what he holds, whom he is bound to and what the act was; what he learns depends on the channel (which `Seen` terms it supplies) and is discounted by distance from the source and by disagreement with what he already saw. Beliefs fade by a fixed decrement each season and the weakest are forgotten at a cap. Jordan, 2026-09-02: *"our understanding of all other words and actions is subjective and singular"* (`decision/options.py:86-87`, D05 §2.4). The decision package is "AX-2's island … with no `World` in scope" (`decision/__init__.py:1`, C04 §2). Every other subsystem's outcome reaches the people of the world only through this layer.

### B2 Operating alone
**State.** `Person.ledger: list[Claim]` (C10 §3a). Provenance = `source` ∈ `claim_sources = [firsthand, told_by, inferred, firsthand_via_knot]` + `chain` (who passed it on, origin first; `hops = len(chain)`, `teller = chain[-1]`) + `visibility` (`"own"` or a circle `(teller, addressee)`) + `doer` (set when the claim records the holder's own act) (C10 §3a; `carriers.py:337-379`).

**WITNESS, once per round** (barrier 4, INTERIOR token; CHECKED `driver.py:510`; C02 §4.9, C10 §4c). MATTER's and CALENDAR's Events join round 0 only (`driver.py:507-509`).
1. Drop `UNDEPOSITED_KINDS` (`finding.none`); skip Events that only change held claims (IN-55).
2. **Fan-out** `observers_for(w, e, mode, everyone)`: shipped `fan_out_mode="all_five"`; for each person the FIRST channel, in precedence order, whose predicate admits him — one channel per person (`epistemic.py:794-840`):

| channel (precedence) | admits | claim source | refraction remove | `Seen` terms supplied |
|---|---|---|---|---|
| `co_located` | present at `event_place` (presence index) | `firsthand` | 0 | stratum, marks, who |
| `witness_key` | the anchor, or a live `knot` Tenure partner of the anchor | `firsthand_via_knot` | 1/3 | stratum, who |
| `document_key` | holds (live) an object the Event changed | `told_by` | 2/3 | — |
| `chronicle` | everyone, if the Event's kind is emitted by a `binding_decision`-stratum verb | `told_by` | 2/3 | stratum |
| `post_remit` | the establishment of the seat the act was done through, within purview | `inferred` | 1 | stratum |

(Sources: C10 §3c, §4c.5, §4d; remove values per H-199 "firsthand 0, knot 1/3, told 2/3, inferred 1". `post_remit`/`chronicle`/`witness_key` term rows are "unruled" defaults, C10 §7.) Modes `presence_only` (co_located only) and `total` (everyone as co_located) are sweep arms.
3. **Deposits per admitted person** (C10 §4c.6-12): (i) event-kind claims `(subject, e.kind, True)`, subjects by `claim_subject_rule="both"` (anchor + each changed thing, minus the hidden actor); (ii) observation claims of cells (e.g. `stores:grain`) — shipped `observation_deposit_mode="actor"`: only the actor; (iii) a `seen` claim with a `Seen` masked to the channel's terms (`who` = `act.actor`; `marks` = `()`; `why` always `None`); (iv) document content: a person who newly holds a Record gets `content:<kind>` with its frozen `subject_matter`; (v) seat/purview reports of matter-caused observations to governors (IN-22, `post_remit`); (vi) told content (below); (vii) FI findings (block A).
4. **Telling** (`news.told`): the hearer gets a copy of the teller's `Said` (picked at CHOOSE by `person_q.said_of`), source `told_by` whatever channel admitted him, teller's confidence carried, `chain = held.chain + (teller,)`; exact-triple dedup. At `Partial` degree only, `_told_value` distorts: drop one addressee from a tuple, or drift a number by `1 + sel % ceil(told_drift_band*|v|)` with sign preserved, `told_drift_band=0.5`; `sel` is a hash, no RNG (C10 §4c.12-13). A circle (private telling) forms with probability `telling_privacy=0.0` — never at shipped values; retelling a circle claim outside emits `confidence.broken` (C10 §4c.14).
5. **Refraction** (not applied to the act's own actor): `factor = (1 − g·channel_remove) · (1 − g·dissents)`, `confidence' = int(confidence·factor + 0.5)`, `refraction_gain g = 0.5`; `dissents` is True when the incoming claim disagrees with the holder's own firsthand claims about a person or cell, or the holder's ledger makes the act's `requires` known-false for its actor (C10 §4d; `options.py:1338-1444`). Competence factor = 1 (H-200 unbuilt). Refraction only lowers.
6. **Cap and forgetting:** `ledger_cap=200`; while over cap, evict the claim with lowest `confidence × (when + 1)` (CHECKED `state/ledgers.py:17-32`). "nobody can witness a forgetting" (`witness.py` ~548).

**MATTER, once per season** (C02 §4.3.4; CHECKED `matter.py:317-347`, `fixtures.py:293`): every claim with confidence > 0 loses `claim_decay_per_season = 5`, floored at 0, emitting `claim.decayed` chained to its deposit. D05 calls it "the THIRD licensed clock" (D05 §4.2). Then `_standing_crossings`: a person's standing gap across `standing_band_floors=(500,)` emits `standing.band_crossed` (not fanned).

**Reading the ledger** (C05): `LedgerReader(claims, weigh)` — best claim by `(when, confidence)`, or with `weigh` by `support = 1 − Π over distinct origins (1 − weigh(c))`; absence is `UNKNOWN`, never False. `teller_weight`: `1.0` if no chain, else `clamp(told_weight^hops · relation · record)`, `told_weight=0.5`, `rank()` always 0 (C10 §4d). `ledger_weigh` returns `None` (plain reader) for a ledger holding no chained claim (`options.py:1356-1362`, CHECKED).

### B3 In the whole game — what the chooser perceives
The chooser reads `p.pursuits, p.scar, p.conviction, p.stance, p.ledger, p.tenures, p.body, p.travel_leg`, a `View`, a subsistence sensation and fixtures — no World (C04 §5.1). The ledger enters choice in these places only:
1. **Which question he answers** — `questions_for` (barrier 2, driver-side, reads World): a `claim_landed` Question per claim deposited since his last deliberation whose subject is in his `reach` (self, own purview, home ancestry); plus `need` questions from ambitions; sorted by `attention_key` tiers 0-4, tier 2 = deed claims by `|valence|` under his pursuits (C05 rows `questions_for`, `attention_key`). Aggregation `"first"`: one question per deliberation (C04 §4.7). The question's referents are the candidate subjects (C04 §4.2.5). **So news is the main agenda-setter.**
2. **Known-false veto** — `belief_contradicts` drops a candidate whose `requires_typed` evaluates False against his own ledger (`options.py:308`); "Nothing turns those same beliefs into a preference" (D05 §2.4).
3. **Naming** — `referent_named` rows form only on subjects his ledger names (`ledger_names`) (C04 §4.2.7); `known_persons` (from claims, `seen.who`, tellers) supplies person operands (C05).
4. **Operands** — content and shortfall claims supply `subject`, `kind`, `amount` (C04 §4.2 operand derivation).
5. **What he says** — `said_of` picks the best non-`seen` claim on the subject as `tell`'s content (C05).
6. **Regard** — `regard = stored + 0.5·judged + 0.5·told` over deed claims (C04 §4.3) enters scoring only at `stance_polarity="regard"`; shipped default `"legacy"` reads stored stance only. Regard-like deed sums also feed social contest `reception`/`proofs` (`remove_weight(source)·confidence/100·deed_term`, C05).
- The `View` assembles the last `view_k=12` ledger ids, but nothing in `decision/` reads `View.ids` (grep for `.ids` in `decision/*.py`, no hits; CHECKED) — it carries only the question.
- **Writers into this layer:** every verb's Events (all subsystems), MATTER and CALENDAR Events, FI findings and Records. **Readers:** the chooser (above), social contest (reception, proofs), goals (`deed_doers` over own ledger), standing (MATTER), `world_q.witnessed`/`PersonProjection` (a read-only per-person projection; caller not traced).
- **Feedback loops:** Event → claims → question → act → Event (the engine's main loop of attention); deed claims → regard/reception → contest outcomes; refusals are deposited as beliefs ("refusal deposits its refusal kind as a belief", D05 §2.10) and therefore become news.

### B4 Built vs designed
| element | grade | evidence (RUN = seed-0 realm, 2 seasons, 74 persons) | designed and absent |
|---|---|---|---|
| WITNESS fan-out + event-kind/`seen` deposits | RUNS-IN-LOOP | RUN 11,869 `claim.deposited`; 3,587 `seen` claims held | `why` term (R8.4), `marks` content |
| `co_located` channel | RUNS-IN-LOOP | RUN 6,380 `firsthand` claims held | eavesdrop/recipiency narrower than presence (L12 §2.31) |
| `chronicle` / `document_key` | RUNS-IN-LOOP | RUN 2,245 `told_by` claims, all with empty `chain` (top predicates `seen` 873, `dispensation.issued` 645, `order.given` 366) | — |
| `witness_key` (knot partners) | RUNS-IN-LOOP, admits nobody new | RUN 0 `firsthand_via_knot`; no `knot` Tenures (`tie / knot` unresolvable) | plugged knots (L12 `trace`) |
| `post_remit` (obligees) + seat reports | RUNS-IN-LOOP, admits nobody | RUN 0 `inferred` claims | — |
| told copy with chain | TESTS-ONLY in evidence | RUN 4 `news.told`, 38 deposits caused by them, 0 chained claims held at end (dedup or eviction; not traced) | interview reply as told claims (J1) |
| Partial-telling drift | TESTS-ONLY in evidence | 1 Partial telling in RUN; `test_told_by_channel.py` | lying (J-C-6) |
| private circle / `confidence.broken` | TESTS-ONLY | `telling_privacy=0.0`; RUN 0 `confidence.broken` | bribe inducement to a circle of two (L12 §2.47) |
| declared intent leak | TESTS-ONLY | `intent_disclosure=0.0` (C04 §4.1.8) | — |
| refraction | RUNS-IN-LOOP | RUN confidences 100 / 95 / 67 / 62 (67 = 100·(1−0.5·2/3); 62 = 67−5) | competence factor (H-200) |
| `teller_weight` | RUNS-IN-LOOP, inert | `ledger_weigh` → `None` with no chained claims; `rank()` ≡ 0 | office rank producer |
| decay | RUNS-IN-LOOP | RUN 5,329 `claim.decayed` | — |
| cap/eviction | RUNS-IN-LOOP | RUN 13 of 74 ledgers at 200 after 2 seasons; mean 116.6 | witnessable forgetting |
| questions from claims, attention tiers | RUNS-IN-LOOP | `driver.py:366`; C04 §4.7 | news propagation beyond co-location as a filter, "never as a new witness channel" (D05 §4.16) |
| known-false veto | RUNS-IN-LOOP | `options.py:308` | beliefs as preference (D05 §2.5 test) |
| regard in choice | TESTS-ONLY | `stance_polarity="legacy"` default | — |
| standing crossings | RUNS-IN-LOOP, none fired | RUN 0 `standing.band_crossed` | — |
| covers changing the anchor | RUNS-IN-LOOP | block A | `room` scope hiding `seen.who` |

### B5 Structural handles for comparison
- **Resolution style:** deterministic. Observation is a channel predicate, not a perception roll; distortion is hash-selected (no RNG); the only probabilistic hook (privacy) is set to 0.
- **Granularity:** per Event × per person; one channel per person per Event; confidence an integer 0-100.
- **Scale:** global (every person, every Event, every round); place-local through presence.
- **State model:** event-sourced log as ground truth + per-person append-only belief lists with provenance chains; documents are world objects whose holding *is* a belief.
- **Agency model:** nobody chooses to observe; a person chooses only to `tell`, inquire, or hold/give documents. The engine chooses for everyone.
- **Information model:** strict subjective knowledge for the chooser (no World in scope), with leaks on the driver side (`questions_for` reads purview and home; `goal_referents` `seat_holders` is a world read with no claim behind it, `[ASSUMPTION]`, ED-IN-0292 (2), C05). No deception exists in practice: no lie (J-C-6), covers do not hide `who` from those present, forgery inert — D05's "The world cannot be fooled" (D05 §4.12 item 7) still holds in RUN.
- **Failure/recovery:** beliefs fade linearly and are forgotten by a confidence × recency product; nothing "unsays" a claim (D05 §4.12 item 1); contradictions are resolved at read time by recency/confidence/support, never stored.
- **Content model:** fully generated from Events; no authored rumours.
- **Pacing:** WITNESS per round (5 per season), decay per season; news lands the round its Event is logged and shapes the next round's question.

### B6 Open design decisions the sources name
H-199 (remove ordinal, `[ASSUMPTION]` equal spacing), H-200 (competence factor), H-201 (act-level dissent), H-192/H-193 (judged/told gains), H-215, H-216 (reception/proof gains), H-40 (decay sweep), H-33 (presence eligibility), H-09, IN-55, IN-22, IN-57/69/72 (attention), R8.4 (`why`, `marks`), `FOUND_CHANNEL` slot and `finding_terms` `[ASSUMPTION; medium; Jordan to correct]`, unruled term-supply rows for `post_remit`/`chronicle`/`witness_key`, `resolve.py:584` `[ASSUMPTION; Said carries no circle]`, ED-IN-0292 (2) (seat_holders world read), J-C-6 (lying), J1 (interview reply as told claims) (C10 §7, C02 §7, C04 §7, C05, L12 §6).

### B7 Conflicts, uncertainties, checks made (both blocks)
- **C10 says "no time-based confidence decay … confidence frozen at deposit" (C10 §4c.15, §7). REFUTED** `engine/season/loop/matter.py:317-347` and `data/fixtures.py:293` (`claim_decay_per_season=5`); RUN shows 5,329 `claim.decayed`. C10's scope excluded `matter.py`.
- **L12 §8 H2 could not find `_found_claims`. REFUTED** `engine/season/loop/witness.py:276`.
- D05 §2.10 says "4 of 46 rows"; C04 says 53 verb rows. Different dates; I use C04 (HEAD-read).
- D05's channel list in RECEPTION cites `witness.py:705-760` and `fixtures.py:837` for refraction; HEAD lines differ (`fixtures.py:864`, C10 §3c). Line drift only.
- Uncertain: why no chained `told_by` claim survives (dedup against a firsthand copy of the same triple is likely, not checked); whether `PersonProjection` has a non-test caller.
- **Checks:** CHECKED `engine/season/loop/driver.py:510`; CHECKED `engine/season/loop/witness.py:265,276`; CHECKED `engine/season/loop/matter.py:317-347`; CHECKED `engine/season/data/fixtures.py:293`; CHECKED `engine/season/state/ledgers.py:17-32`; CHECKED `engine/season/loop/resolve.py:1060-1080`; CHECKED `engine/season/requirements.yaml:169-172`; CHECKED `engine/season/state/attribution.py:105-122`; CHECKED `engine/season/decision/options.py:623-625,1356-1362`; CHECKED `engine/season/rosters.yaml:1107-1122`; CHECKED `engine/season/verb_table.yaml:1324,1350,1366,1387,1426` (eligibility `own`); CHECKED no `.ids` read in `engine/season/decision/*.py`.
- **RUN (execution artifact):** `build_realm(0)`, `SeasonDriver`, `make_chooser(..., verbs=resolvable_verbs(), draw=draw_factory(...))`, two `season()` calls exactly as `harness/populated.py::run` does; then counted `w.log` kinds, `d.resolved` verbs, `d.act_of` verbs per finding kind, ledger sources/predicates/confidences, and `claim.deposited` Events with >1 cause. Season 0: 676 acts, 1,081 events, 5,552 deposits; season 1: 731 acts, 6,585 events, 6,317 deposits. `resolvable_verbs()` contains `examine, interview, research, surveil, reconstruct, survey, forge, conceal, tell` and not `thread_read` or `tie / knot`. One seed, two seasons: a sample, not a distribution.

---
