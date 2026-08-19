# Obstacles, Stat Rosters and Proposition Identity — the census behind B1, B2 and B3

## Status: FINDINGS — measurement, not design. Nothing here rules anything. No `.py` touched. Reconciliation against the in-flight infrastructure work is PENDING and expected (Jordan, 2026-08-19).

**Date:** 2026-08-19 · **Lanes touched:** IN, PC, SC, MB, FA, SE, WR, FI
**Method:** an 18-agent read-only census — one agent per subsystem for obstacles, four for the stat rosters, two for identity, three adversarial verifiers, one synthesis. **213 obstacle sites** enumerated. The verifiers corrected the censuses; the synthesis applied those corrections; **I then re-verified the six load-bearing claims myself** (§10). Where the number below is a count, it is measured; where it is a judgement, it says so.

---

## §1 FIVE DEFECTS NOBODY WAS LOOKING FOR

The census was commissioned to answer three questions. It found five live defects on the way, and **the first one changes the stakes of every obstacle decision.**

### §1.1 `tn` is accepted, stored, and never used — the discrete dice owner ignores it

`engine/autoload/dice_engine.py:75-84`:

```python
def roll_pool(pool_size: int, tn: int = 7, ob=None, rng=None) -> RollResult:
    rolls = [rng.randint(1, 10) for _ in range(effective_pool)]
    net = sum(_die_result(face) for face in rolls)      # <- tn is nowhere in this
    return RollResult(pool_size=..., tn=tn, ...)        # <- stored, never consumed
```

`_die_result` (`:53-61`) hardcodes the TN-7 face rule (1→−1, 2-6→0, 7-9→+1, 10→+2). **Every TN modifier passed to the discrete roller is a no-op**, including:

- `systems/combat/sim/combat.py:214,216` — the entire **Weapon TN Matrix**, *and* the defender's `def_tn` on the opposed roll
- `systems/social_contest/sim/parliamentary_vote.py:178` — `BG_VOTE_TN`
- `systems/social_contest/sim/contest_legacy_stub.py:163-164` — `ARGUE_POOL_TN`
- `systems/fieldwork/sim/knots.py:223` — `KNOT_FORMATION_TN`
- threadwork's `operations.py:176`, `opposing.py:150-151`, `collective.py:164`

Meanwhile the **continuous** half *does* honour TN (`_CONTINUOUS_PARAMS`, `:68-72`: TN 6/7/8 → μ 0.50/0.40/0.30). So the two halves of a single "statistically equivalent" owner disagree about whether TN exists at all. The one live TN in the tree is `VOLLEY_TN=6`, honoured only by mass battle's **private** `roll_pool` (`massbattle.py:627`).

**Why this changes everything above it:** in the discrete path **the obstacle is the only difficulty lever that does anything.** Every R1/B3 decision is therefore load-bearing on more than it appeared to be. This is not on anyone's docket and should be.

### §1.2 The personal-combat scene path is an orphan in a real campaign

**No `queue_scene("combat", …)` call site exists anywhere in the tree** — the only production caller of `queue_scene` is `scene_dispatch.py:105`, which queues whatever `evaluate_triggers` fires, and `evaluable = {"Stability Crisis"}` fires only contests. Two separate in-tree comments record the same finding independently (`combat_bridge.py:37`, `scene_dispatch.py:37`). Additionally `combat_engine_v1` sits behind `DISPATCH_COMBAT_BRIDGE`, which **defaults off**.

So the canonical combat engine is reachable today only from the balance workbench and the test suite. **A ruling scoped to "live" sites would barely touch combat.**

### §1.3 "Can a faction present a zero obstacle" is already answered — *no*, three layers deep

`HANDOFF.md` frames B2's range question as deciding this. The runtime already forecloses it:

1. `Faction.adjust()` (`game_state.py:127-128`) clamps unconditionally to `[0.5, 7.0]`, and **0 of 31 non-test call sites override the bounds**.
2. score/2 of the minimum 0.5 is 0.25.
3. Every built stat-derived obstacle then floors again anyway — `max(1.0,…)` (tribunal), `+1` (crown, fieldwork, opposing), `+2` (parliamentary transfer), `OB_FLOOR=1` (mass seizure), `min 1` (knots).

**Nobody has ever written a zero obstacle**, and that is the one thing all 213 sites agree on. The live decision is not the 0-vs-1 range — it is whether to keep the single hardcoded clamp or install per-stat floors, and **neither declared source knows that clamp exists.**

### §1.4 `Faction.intel` is dead, and fieldwork already wrote a ruled-shape obstacle against it

`intel` has **no `MULTS` entry** (`game_state.py:45`), so `adjust('intel', …)` raises `KeyError`; it is absent from `STARTING_STATS` and from `serialize_world`. Meanwhile `systems/fieldwork/fieldwork_v30.md:662-663` already specifies BG espionage as **`Ob = floor(target Intel/2) + 1`** — the exact ruled shape, authored *before* the ruling.

Rule Intel in without wiring it and **the tree's first already-compliant faction obstacle evaluates to a permanent constant of 1.**

### §1.5 Two opposed-roll sites that look identical have opposite mechanical weight

`systems/mass_battle/sim/massbattle.py:950` computes a degree and annotates it `# narrative degree label only`. Damage at `:965-966` bypasses it entirely, and **`a_deg`/`b_deg` appear three times in the file, all assignments, never a read.** The structurally identical line in the canon tree (`tests/sim/mass_battle/orchestration.py:1304`) feeds `DAMAGE_BY_DEGREE`.

So the opposed roll on the **live** campaign path is mechanically dead, and the one that matters lives in the tree the campaign cannot reach.

---

## §2 B3 — OBSTACLES BY SUBSYSTEM: WHERE, WHEN, HOW

**213 sites.** 122 non-oppositional · 31 oppositional · 33 ambiguous · 19 hybrid · 8 opposed-roll.

| Subsystem | Sites | Unclassifiable |
|---|---|---|
| fieldwork + npcs + characters | 51 | 9 |
| threadwork | 41 | 4 |
| mass battle | 30 | 4 |
| factions | 21 | 6 |
| settlements + world | 20 | 7 |
| engine core | 19 | 4 |
| personal combat | 18 | 4 |
| social contest | 13 | 4 |

### §2.1 Organised by circumstance — the finding is that there are THREE architectures for one job

**World-gen:** no obstacle exists anywhere. Unanimous. The whole obstacle surface is runtime-derived; nothing is baked.

**Per-beat scene action — three incompatible architectures, and no document chooses:**
- **(a) obstacle folded into the roll's mean, threshold fixed** — `combat_engine_v1/core.py:45` `DECISIVE_OB=3`; every weapon/armour/wound fact enters `net_sigma` instead. Its own docstring (`:76-80`) says this "does not do at all" what the ruling requires.
- **(b) obstacle is the opponent's rolled net** — `sim/combat.py:214-218`; `massbattle.py:950,951,1516`; `orchestration.py:1304,1305,2552`.
- **(c) obstacle is a static number** — `contest/resolver.py:155` `base_ob=2.0`, never overridden by any of the 8 proceedings.

**Task / site difficulty — this is where the subsystems genuinely agree, and strongly.** A named base table plus named modifiers: threadwork's `DEPTH_OB` 1/2/3/5/8/13 (`operations.py:54-96`), fieldwork's Depth base 1/2/3/5/8 (`fieldwork_v30.md:31-35`) — *the same Fibonacci shape, independently arrived at* — and `mass_seizure.py:261` `max(1, 10 - pt + infra_mod)` with the modifier channel owned separately at `infrastructure.py:57-66`. **Class B is already the ruled shape**, confirming my execution plan's §8 self-correction.

**Reactive / on-trigger:** overwhelmingly doc-only. Feint, Rescue, Establish Distance, Retrieve, Tie Up, Escape, disengage-pursuit are specified in `combat_reference_v1.md:127-134,400,590` and implemented in neither combat resolver.

**Accounting boundary:** weakest and most divergent. `rally_check` is an empty `pass` in **both** mass-battle trees against a doc specifying "Command check Ob 2". `reform_check` is a `pass` in one tree and a *dice-free* deterministic gate in the other — **three answers to one mechanic.**

**Season tick:** the only place the obstacle reaches the single owner as a parameter. **Every `ob=` argument to `dice_engine.roll_pool` in the entire tree comes from `systems/factions/sim/*` or `systems/threadwork/sim/*`. Combat, contest and mass battle never pass one.**

### §2.2 Where they diverge for no defensible reason

- **Integerization.** Five live sites destroy the ruled fraction: `tribunal.py:118,122` `round()`, `parliamentary_transfer.py:257` `int()`, `crown_initiative.py:190` `floor()+1`, `opposing.py:85` `//2`, plus fieldwork's doc table. Contest's `base_ob` is a float; combat compares an int against a continuous net.
- **What the degree is FOR** — dead label in one tree, damage input in its twin (§1.5).
- **Doc-vs-doc.** The same Suppress roll is `Ob = Church Mandate` (`conviction_track_v30.md:204`) and `floor(Church Mandate/2)+1` (`faction_layer_v30.md:699`). The code implements the losing form behind an inert default the only live caller never sets.

### §2.3 The three readings of B3, with their real costs

| Reading | Cost | Blocks on |
|---|---|---|
| **Narrow** (static obstacles only) | Nothing moves | Nothing — but it **preserves the exact three-architecture split R1 exists to close**, and writes no discriminator for the next author |
| **Broad** (opposed rolls become score/2) | Mechanically **free** on the live path (the degree is already dead); costs the full byte-exact digest battery on the canon tree the campaign cannot reach | **§3 — naming a character's scalar score** |
| **Middle** (both sides roll AND the obstacle is opponent-score/2) | Digests still move | Nothing — **and it already exists in-tree** |

**The middle has a working precedent.** `systems/threadwork/sim/opposing.py:80-85,115-123`: both practitioners roll, *and* each side's obstacle is `base_ob + floor(opponent_tps/2)`. My execution plan already classified that site as "already compliant" without noticing it was demonstrating a third option. Jordan's stated reason — *"Ob should be determined by your opponent"* — is satisfied without deleting the opposed roll.

**The honest objection to the middle:** it double-counts the defender — their score sets the obstacle *and* their roll subtracts from the margin. Threadwork lives with that today and nothing has flagged it.

⚠ **One trap in the broad reading.** `massbattle.py:1887-1890` hardcodes `command=4, discipline=5` for **both** sides under a declared `[GAP: no canonical spec]`. A defender-Command/2 obstacle would therefore be **the constant 2, for both sides, in every campaign battle, forever** — deleting the only thing that currently distinguishes the two sides' obstacles and replacing it with a literal.

---

## §3 B3's REAL BLOCKER — no character has a score

This is the finding I most want on the record, and it was my hypothesis going in.

**`score/2` presupposes a scalar. A character does not have one.**

- There is **no `class Actor` and no `class Character`** anywhere in `engine/` or `systems/`.
- `Combatant.__init__` (`combatant.py:93-97`) carries **7 of the 9** declared attributes — no charisma, no bonds.
- Every attribute enters combat resolution through a **blend**: `reading = (2·Cog + Att)/3`, `reflex` = weighted Agi/Att.
- The defence pool is `(agi×2) + history + 3` — History is not on the attribute roster at all.
- Charisma exists only in the contest kernel; Bonds only in `knots.py:185`.
- The registry's *primary* names — Acuity, Will, Attunement — never appear as code identifiers. Only the aliases `cog`, `spirit` and the bare `att` do.

Meanwhile the other subsystems each mean something different by "score": factions have named scalars on a declared 0/1–7 range; mass battle has bare `int` fields with **no declared scale anywhere**; contest has `faculty`, one flat int defaulting to 4.

> **B3-broad and the unnamed-tenth-attribute workshop are the same question wearing two names.** "The opponent's score/2" is not evaluable for a character until somebody says what a character's score *is* — and the PC-lane migration my execution plan sequenced **first** cannot start until then.

---

## §4 B2 — the faction roster is FOUR-WAY, not two-way

| Source | Roster | Ranges |
|---|---|---|
| `references/descriptor_registry.yaml:102-111` | **5 base** (Mandate explicitly *not* a base attribute) | Influence 1–7; Wealth, Military, Intel, Stability **0–7** |
| `systems/factions/faction_canon_v30.md:199-217` | **6** (Mandate derived + five) | Influence, Wealth, Military, **Intel all 1–7**; Stability 0–7 |
| `references/module_contracts.yaml:108-110` | Mandate + Treasury derived, plus an unenumerated "faction stats 1-7" | — |
| **Code** — `game_state.py:98-111` | **6 fields** `L, Sta, W, I, Mil, intel` | `L` is a **base, writable** Mandate proxy |

**The registry's 0-floors are a deliberate, documented override, not drift.** `descriptor_registry.yaml:96-101` records the per-stat floor table as ratified 2026-07-08 (ED-IN-0029): Influence floors at 1 because it "never fully vanishes institutionally"; Intel "had no independently-declared floor anywhere in the corpus, ratified here at 0." It simply never names `faction_canon_v30.md`. So this is a **genuine conflict between two ratified surfaces** — only Jordan can pick.

**Three things a ruling must settle that weren't on the list:**
- **Mandate-as-derived is a sequencing call, not a port cost.** Derived Mandate = `clamp(round(7T/(T+6)),0,7)` over per-settlement L/PS — and **neither Legitimacy nor Popular Support exists in code**. So "Mandate is derived" means every faction obstacle blocks on a settlement layer that isn't built: faction-side R1 migrations block on **SE**, not FA.
- **Treasury should be struck from the open list, not ruled.** `derived_stats_v30.md:298`, `descriptor_registry.yaml:192` and `module_contracts.yaml:109` already agree it is Wealth × 100. The only gap is a missing field.
- **B2 does not reach mass battle.** `_faction_to_unit` reads only `faction.Mil`; command and discipline — the two stats every mass-battle obstacle would halve — are hardcoded. **B2 and B3 do not compose.**

---

## §5 CHARACTER STATS AND THE ACQUISITION LAYER

**The roster** (`descriptor_registry.yaml:45-59`): nine named on a 1–7 scale — Strength, Endurance, Agility / Focus, Acuity (aliases Reasoning, **Cognition** — tagged `[ASSUMPTION] … Jordan veto`), Will (alias Spirit) / Attunement (alias Perception), Charisma, Bonds. The header (`:39-43`) records the ruling: count is **10**, the tenth is **UNNAMED**, and inferring it from the Spirit→Will or Perception→Attunement folds is explicitly forbidden.

### §5.1 The acquisition layer is distinct in combat and a relabelling in contest — the answer is subsystem-conditional

Your conditional ruling was *"acquisition-layer, but interrogate it against player attributes as to whether it's truly distinct."* The census's first proposed discriminator — that the acquisition layer is "non-monotone" — **is false and the verifier killed it**: combat's layer is monotone in level, pinned twice (`test_combat_tradition_levers.py:169-172`, `:208-211`).

What the layer actually has that an attribute cannot is **conditional applicability**, and it is pinned by two tests:
- `test_ability_inert_when_weapon_lacks_the_feature` (`:215-221`) — shinogi on a spineless arming sword produces `bind_sigma` **identical** to an uninvested fighter.
- `test_tradition_gate_untaught_technique_is_inert` (`:224-238`) — a German fighter equipping a Japanese technique gets factor exactly `1.0`.

**The runnable test:** hold attributes fixed, vary only kit / tradition / matchup, and check whether the ordering between two characters **flips**. Investment flips it. An attribute cannot, because every attribute enters unconditionally through a blended faculty.

**Verdict the evidence supports:**
- **Combat — genuinely distinct.** The only subsystem with a *built* layer (`equipped` graded dict × tradition gate × weapon feature).
- **Contest — a relabelling as coded.** `faculty` is a single flat int (`wrapper.py:91`), opponent-invariant, monotone, feeding both pool and σ. And a layer is **not buildable** there: `ContestView` (`contract.py:53-66`) has 12 fields and none carries school, technique or kit — the policy layer literally cannot see one.
- Everything else has no layer to test.

### §5.2 ⚠ A scoping defect in my own execution plan

My plan assigned the B4/R2 divergence test to **fieldwork** actions (Research / Reconstruct / Interview) and marked it *"executable today."* **It is not.** `systems/fieldwork/sim/{fieldwork,investigation}.py` are `stub_resolve` throughout — fieldwork can produce **no orderings at all**. The test can only run where a layer exists (combat, where the answer is already visible in pinned tests) or hypothetically in contest, where it returns "relabelling" by construction. **Re-scope before executing B4.**

### §5.3 The acquisition layer changes the obstacle picture, and R1 has no slot for it

If a character's obstacle-facing score is an attribute, `score/2` reads off a 1–7 roster and is **static**. If it is the acquisition layer — your Q2 direction — the obstacle becomes **conditional**: inert without the kit, inert without the tradition. Two identically-statted defenders would present *different obstacles* depending on what they carry.

**A conditional obstacle is a different mechanical object from a static one, and the R1 doctrine has no slot for it.**

---

## §6 B1 — PROPOSITION IDENTITY

**The decisive fact:** `hashlib` appears **exactly once** in all of `engine/` + `systems/` — `keys.py:460`, `KeyLog.content_hash()`, a digest of an entire append-only log. **There is no per-object content-address primitive anywhere in the runtime.** B1 is not "choose among conventions"; it is "author the first one."

**The spec that survived adversarial review** — as a *byte-level preimage specification*, because GDScript has sha256 but not `json.dumps`:

- **sha256 over UTF-8**, full hexdigest or a documented ≥128-bit truncation.
- **Never derive from runtime-salted or iteration-ordered state** — no builtin `hash()`, no `repr()`, no set traversal. A bug of exactly this class already shipped and was fixed (`game_state.py:112`).
- **Name the canonical-JSON flags explicitly:** `json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",",":"))`. This matters because **three exporters in the tree use three opposed policies** — `export_key_types.py` (sort_keys=False, by ORD-1), `export_engine_params.py` (True), `export_sim_params.py` (False). "Canonical JSON" without flags is not a spec.
- **Explicit nulls, never omission** — `Key.to_obj()` (`keys.py:156-173`) emits every field including `source_actor: None`. That is the tree's precedent and it must bind the qualifier.
- **Type-tag entity refs** — territories are bare `'T1'`, factions bare `'Crown'`; a subject spans five id spaces indistinguishable from the string.
- **No raw float in the preimage** — `godot_conversion_strategy_v1.md:163` forbids cross-language float equality outright.
- **The predicate carries its string only, never its owning registry.** Under P4's IN/FI split with a promotion rule, registry identity in the preimage means **promoting a predicate silently re-ids every proposition using it** — breaking the unification at exactly the moment it pays off.
- **`hash_version` OUTSIDE the preimage**, plus a blocking `--check` re-derive gate. **One owner for minting** — key-id minting is already duplicated four ways with four counters and no owner.

**The silent-failure paths, ranked by invisibility:**
1. **Divergent hash** — agreement is id-equality, so a missed match is indistinguishable from *"she does not hold that belief."* Nothing in play surfaces it. A falsifier already exists to copy: `test_engine_atlas.py:53-81` re-runs in subprocesses under `PYTHONHASHSEED ∈ {0,1,9999}` and asserts one digest.
2. **Preimage merge (delimiter collision)** — *worse than divergence*: two claims become one, provenance unions, `independent_support` inflates, and the engine **manufactures a contradiction**. P3 ruled support may be empty, so there is no provenance floor to make it visible. Both existing joined preimages in the tree are unescaped (`harness.py:143`, `workbench.py:253`).
3. **Qualifier instability** — omitted vs null vs partial gives three ids for one claim, dissolving the property §3.1 calls "the whole trick."
4. **Swallowed emitter failure** — the house pattern is `except Exception: if os.environ.get('VALORIA_STRICT_KEYS'): raise`. A proposition emitter written to house style **drops malformed holdings in every ordinary run.** Mitigation: run the suite under `VALORIA_STRICT_KEYS=1` and assert emitted **count**, not absence of exception.
5. **Cross-platform float divergence** — not hypothetical: `test_mass_battle_byte_exact.py:32-50` records an unlocated Windows/Py3.14-vs-Linux/Py3.11 digest divergence in the flagship byte-exact gate, worked around by asserting only under `GITHUB_ACTIONS`.

---

## §7 THE FINDING THAT ONLY APPEARS WHEN ALL FOUR ARE READ TOGETHER

**The ladder is single-owned and guarded. The obstacle has no owner and no guard.**

`tests/valoria/test_degree_ladder_single_owner.py:134-141` registers six ladders plus two declared HOLDs and fails if a hold silently resolves. There is **no equivalent for obstacle derivation** — and the obstacle reaches the owner as a parameter from only two lanes.

So R1, the largest outstanding piece of the ruling, has **nothing that would fail on recurrence.** That is exactly the CLAUDE.md §0.1-point-5 shape: *"if you cannot write the guard you have not understood the pattern."*

**And one coupling nobody anticipated.** A `Proposition.qualifier` is `{season_index, location_id}` — the when/where of a claim. An obstacle's modifiers are the situational facts of an instance. §3.4's unification explicitly wants a hook condition, a belief and an argument premise to be **one** proposition. If obstacle modifiers ever become propositions, **obstacle derivation inherits B1's hash-stability requirement, and a qualifier-normalisation bug becomes a dice-resolution bug.**

**Finally: "is_live" and "is load-bearing" are independent axes, and all four censuses conflated them.** Combat's scene path is orphaned; mass battle's live opposed roll is mechanically dead; the contest's canonical audience resistance is derived and never consumed; `MOTIONS[…]['reb_ob']` is defined and never read. **A ruling scoped to "live" sites would touch almost nothing; a ruling scoped to "load-bearing" sites lands hardest on the canon mass-battle tree that no campaign reaches. The two produce nearly disjoint work lists, and whichever scope is chosen should be said out loud.**

---

## §8 CORRECTIONS TO MY OWN EXECUTION PLAN

| Claim in the plan | Reality |
|---|---|
| B4/R2's divergence test is "executable today" against fieldwork actions | **Unrunnable** — the fieldwork sims are stubs and produce no orderings (§5.2) |
| The R1 census listed ~15 relevant sites in three classes | **213 sites.** The three-class taxonomy holds; the coverage was an order of magnitude short |
| `opposing.py:85` is "already compliant" | True, **and it is the working precedent for B3's middle reading** — the plan recorded it without noticing what it demonstrated |
| The PC-lane migration should be sequenced first | It **cannot start** until a character's scalar score is named (§3) |
| Tribunal's formal-grounds halving "creates a ruling" | Confirmed, and there is a **second** undocumented collision of the same kind — the two-doc Suppress contradiction (§2.2), filed nowhere |

---

## §9 WHAT IS NOW ON JORDAN'S DESK

Eleven items. The first two are upstream of everything else.

1. **B3's reading** — narrow / broad / middle (§2.3).
2. **What IS a character's score?** — attribute, derived faculty, acquisition layer, or the defence pool (§3). *Blocks B3-broad and the PC migration.*
3. **B2's roster** — registry's 5 or `faction_canon_v30`'s 6 (§4).
4. **The `[0.5, 7.0]` clamp** — keep, or install per-stat floors (§1.3). *This, not the range question, governs the minimum obstacle.*
5. **Does score/2 stay fractional** at the five integerizing sites (§2.2)?
6. **Intel** — rule in and wire, rule in as inert, or strike (§1.4).
7. **Mandate** — derived (blocks faction R1 on the SE lane) or ratify the coded base scalar (§4).
8. **Acquisition-layer distinctness** — the evidence supports *distinct where built, relabelling where merely named* (§5.1).
9. **B1** — adopt the byte-level preimage spec, or defer and let four emitters invent four rules (§6).
10. **Is TN a live lever or retired?** (§1.1) — not on any docket, and it silently raises the stakes of every decision above.
11. **Two collisions the migration will hit** — tribunal's double-halving, and the two-doc Suppress contradiction (§2.2).

---

## §10 WHAT I VERIFIED MYSELF

Six claims re-checked by hand after the workflow, because the plan would rest on them. **All six confirmed.**

| Claim | Check | Result |
|---|---|---|
| `roll_pool` ignores `tn` | read `dice_engine.py:53-84` | ✅ `tn` stored on the result, absent from the computation |
| `hashlib` appears once in `engine/`+`systems/` | grep | ✅ import + one use, both `keys.py`, log-scoped |
| `Faction.adjust` clamps `[0.5, 7.0]` | read `game_state.py:127-128` | ✅ |
| No `queue_scene("combat")` exists | grep all callers | ✅ only `scene_dispatch.py:105`, generic |
| `command=4, discipline=5` hardcoded both sides | read `massbattle.py:1884-1893` | ✅ |
| `a_deg`/`b_deg` never read | grep the file | ✅ three assignments, zero reads |

**Not independently re-verified** (taken from the census after adversarial review): the 213-site count and its per-subsystem breakdown; the `test_combat_tradition_levers.py` line references; the `descriptor_registry.yaml:96-101` floor rationale; the three-exporter JSON-policy divergence.

**The claim most likely to be wrong:** that the *middle* reading of B3 is cheap. It rests on threadwork's precedent being genuinely the same shape rather than superficially similar — and on the double-counting objection being acceptable, which is a design judgement nobody has ever ruled on.
