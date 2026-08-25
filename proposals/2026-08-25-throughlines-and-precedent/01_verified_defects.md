# 01 — Verified defects at HEAD `571ae14`
## Status: findings, verified 2026-08-25. Each carries a falsifier.

> These are not proposals. Each was surfaced by a lane and then **independently re-derived**
> against the working tree by the orchestrator. Where a lane's claim did not survive
> re-derivation it is not here. Under CLAUDE.md §0.05, "verified" means read in code.

## D1 — `T16` is missing from the settlement adjacency graph (live KeyError path)
Surfaced by lane L5 out of the *deleted* `audit/lane-a/` corpus; proven here.

`systems/settlements/sim/adjacency.py` defines **16 keys — T1..T15 and T17. `T16` is not a key.**
It *is* a value: line 10, `'T1': {'T2', 'T5', 'T14', 'T16'}`.

Proven by loading the module and comparing key set to value set:
```
keys: 16  ['T1'..'T15','T17']
referenced but NOT a key: ['T16']
asymmetric pairs: []
```
**Every other edge in the graph is symmetric.** T16 is the single exception, which makes it an
omission rather than a modelling choice. Any `ADJACENCY['T16']` lookup raises `KeyError`, and any
neighbour walk that steps T1 → T16 dead-ends or throws.

It matters in game terms rather than only mechanically: T16 is **Schoenland** —
`valoria_geography_v30.yaml:727` *"Schoenland island coast (T16). Independent republic."* — declared
in the geography (`:214`), with an explicit coastal edge `{from: T1, to: T16, type: coastal}`
(`:552`), and a member of a duchy grouping (`:866`). So the one missing node is precisely the island
republic whose only connection is the coastal link, i.e. the territory whose connectivity is
special-cased. A one-line fix; the geography already states the correct edge.

## ⚠ D2 — RETRACTED AND RE-ADJUDICATED TWICE. Do not cite the text below.

*This section originally read "`Standing`'s range was ratified 0–10 on 2026-07-08 and never executed
… the entire published ladder is specified against a nonexistent scale." It was retracted, then the
retraction was itself partly overturned. The full sequence is in `03_method_and_corrections.md`
Corrections 1 and 9; the settled position is R1 in `02_ruled_but_unexecuted.md`.*

**What is true.** `registers/editorial_ledger_sc.jsonl:15` (the ledger entry — every earlier pass
quoted the one-line summary at `references/id_reservations_history.md:73` instead) says **both**:
the **BG faction track's range IS RATIFIED at 0–10** per `references/glossary.md:138`, *and* the
homonym is to be **scope-tagged apart**. Execution was deferred and never happened.

**What was wrong.** (a) The original claim attached that ruling to the **officer rank ladder** (0–7,
prose) — a third mechanism the ruling does not address. (b) Its code evidence,
`systems/social_contest/sim/contest/primitives.py:127`, is the **contest ethos float** (`class
Standing: LO, HI, START = 0.0, 10.0, 5.0` at `:31-47`, with `build()`/`strip()`), not a rank ladder —
and `:127` is not even the class. That is a vocabulary collision promoted to a mechanism claim, by
the document warning against exactly that. (c) The retraction then over-corrected, denying that any
range had been ratified.

**The live defect that survives all of it** is narrower and real: `Faction.standing` is an unbounded
`int` (`engine/autoload/game_state.py:129`) written by ten bare `+=`/`-=` sites and read into a
rolled pool at `systems/factions/sim/crown_initiative.py:81`, against a range ratified fourteen
months of sessions ago. And `systems/overview/clock_registry_v30.md:53`'s `| Standing | 0–5 |` is not
a rival mechanism's range — it is **the error the ruling named for correction**, still uncorrected.

## D3 — `hidden_allegiance` is computed and then dropped (a write that never lands)
`systems/world/sim/npe.py:327` computes `hidden_allegiance = rng.choice(other)` as one of five
deviation outcomes. The `NPC(...)` constructor at `:336-346` passes
`stance, worldview, affiliation_faction, affiliation_loyalty, compromise_category, volatility,
deviation_roll, is_arc_vector` — **and not `hidden_allegiance`.** The field exists on the dataclass
(`:137`) and round-trips through `to_dict`/`from_dict` (`:153`, `:169`), so it looks implemented.
Grep across every `.py` outside `npe.py`: **zero reads.**

This is the only mechanism in the executable tree that would model an agent whose interest diverges
from its faction's, and it is severed at the constructor. Five lanes independently reported "no
executing code models intra-faction divergence"; this is *why* — not absence, but a dropped write.

## D4 — the empty world is a guarded invariant, not an oversight
`engine/tests/test_pipeline_reach.py:625-628` holds `test_world_npcs_populated_after_a_seeded_campaign`
at `@pytest.mark.xfail(strict=True)`, section-headed *"permanently xfail, not 'until a later wave'"*.
`engine/tests/test_f7_smoke_oracle.py:335` asserts `npcs == 0`. ⚠ **There is a THIRD guard, missed by
every document in this analysis until the adversarial pass:**
`engine/tests/test_world_population.py:152` asserts the same counter, and its docstring at `:143` says
it mirrors the f7 oracle. Its message already couples the change to the golden — *"if this is an
intentional wire-up, update this test AND test_f7_smoke_oracle.py's golden together"* — which is the
coupling this analysis reports discovering. Any loader commit must rewrite all three. `strict=True` means populating the
world **breaks the suite**. Any proposal to populate must re-pin both in the same commit — and that
re-pin is the uncontrolled golden-regeneration path CLAUDE.md §7 flags as unguarded, so it must be
called out rather than performed quietly.

## D5 — `references/npc_registry.yaml`: 46 officeholders (**35 canonical**, 11 `proposed`), zero runtime loaders
Only `.py` mention is `tests/valoria/test_references_yaml_parse.py`, which asserts it parses. The file
*"was unparseable for the whole of its visible git history and NOTHING NOTICED"* — and the syntax
error was `faction: Church (dual-loyalty: Crown Inner Circle agent for Himlensendt)`, i.e. the single
authored instance of intra-faction divergence (NPC-034 Gustav) was the thing that broke it.

## D6 — `valoria_geography_v30.yaml`'s `provinces:` block has no production reader (lane L4)
The VSG seed step reads province frames from this block. Reported by L4 as unread on main. Combined
with D1 (T16) and D5 (registry), the pattern is consistent: **Valoria's authored world data is
largely not loaded by Valoria.**

---

## ⚠ D7 IS REFUTED — READ THIS BEFORE THE SECTION BELOW (2026-08-25)

**D7's central claim is false and is withdrawn.** It argued that loading persons at world-gen is
"golden-safe by construction", reasoning from `populate_from_geography`'s docstring. Chapter 1's
author refuted it by **controlled experiment** rather than by reading, which is the only way it could
have been caught:

- The two guards this analysis (and five lanes, and the adversarial audit, and the orchestrator)
  described as pinning the world's population **pin `generate_npc`'s CALL COUNTER**
  (`world.npc_counter`) — **not `world.npcs`**.
- Two NPCs loaded directly into `world.npcs` at world-gen left **both guards green** with
  `npcs_generated = 0` — **and moved seed-42's winner from Crown to Hafenmark.**
- A control arm with `npe.simulate_npc_actions` neutered reproduced the baseline **byte-exact**,
  identifying the channel precisely: `simulate_npc_actions` draws `world.rng` at
  `systems/overview/sim/accounting.py:139`.

**So populating the world DOES move seeded goldens**, unless the season NPC drift is first given its
own RNG substream (Chapter 1's R1, which `create_world` already makes cheap — it accepts a seed and
discards it). The honest sequence is R1 then the loader, not the loader alone.

Two consequences worth stating separately, because they are worse than the retracted claim:

1. **A social-drift simulator has been drawing from the campaign RNG over an empty dict** roughly 400
   times per golden batch, for months, unobserved.
2. **The guards go silent rather than break.** A loader that populates `world.npcs` without calling
   `generate_npc` passes both of them. They would not have caught the change; they would have failed
   to notice it. That is a strictly worse failure mode than a red test, and it is exactly CLAUDE.md
   §0.1 pt 2's rule — *an assertion must be able to observe the failure it excludes* — violated by
   guards written to enforce it.

The section below is **retained unedited as the superseded argument**, because the reasoning it
contains about `populate_from_geography` is still correct *about settlements* (that fix genuinely was
deterministic and golden-free); what was wrong was generalising it to persons without testing.

---

## ~~D7 — the precedent fix is GOLDEN-SAFE BY CONSTRUCTION~~ [SUPERSEDED — see above]
`systems/settlements/sim/registry.py:216-224`, `populate_from_geography`, docstring verbatim:
> *"OI-07 (ED-IN-0091 plan §3 Wave 2 item 4) — register every settlement from the canonical geography
> source at world-gen. **Deterministic: no RNG draw, so this cannot move any RNG-derived campaign
> golden** (win_share / battles_mean / scenes_resolved all read `world.rng`, never touched here) —
> only `serialize_world`'s output dict gains a new key."*

This is the whole answer to the objection raised in D4. Populating the world looked expensive because
`test_f7_smoke_oracle` pins `npcs == 0` and `test_pipeline_reach`'s xfail is `strict=True`. But the
settlements precedent shows the manoeuvre that avoids the cost: **populate from an authored canonical
source deterministically, drawing no RNG.** Settlements went from empty to 37 registered without
moving a single seeded golden, because loading authored data is not a random draw.

The same manoeuvre is available for the officer cast, and it is *better* suited to it:
- `references/npc_registry.yaml`'s 46 records are **authored**, `status: canonical`, each with a
  `source` field. Loading them is deterministic.
- It does **not** require calling `generate_npc`, so it does not touch `world.rng` and does not
  increment the `npcs_generated` counter that `test_f7_smoke_oracle:335` pins at 0.
- It answers OI-05's stated blocker — *"no world-gen initial count … exist[s] in canon to cite"* —
  with a citable count of 46 and a per-record `source`, i.e. **without fabricating anything**, which
  is the exact constraint the deferral was protecting.

`populate_from_geography`'s field-mapping discipline is also the template to copy: every field
mapping carries an inline citation, and *"a stray geography-file type raises rather than silently
registering an illegal settlement type — no fabrication."*

**So the recommendation is not "build a generator". It is: write `populate_from_registry`, modelled
line-for-line on `populate_from_geography`, loading 46 authored officeholders deterministically at
world-gen.** The generator (`npe.generate_npc`) stays where it is, for *filling out* a populated
world later — that step does draw RNG and does move goldens, and should be a separate, later,
separately-argued commit.

One corroborating detail that ties D1 and D7 together: `populate_from_geography`'s docstring notes
*"one entry, S-037/Schoenland, controller 'Schoenland' — an independent city-state per the geography
file's own description"*. The geography knows Schoenland. The adjacency graph (D1) does not have a
`T16` key. Same island, two registries, one of them incomplete.

---

## D8 — Π (settlement pressure) is a declared field with NO dynamics, and the famous 298/300 failure is a LESSON, not a live bug
*Important for accuracy: the writers must not present the Π runaway as a current defect.*

`systems/settlements/sim/registry.py:79` — `pressure: float = 4.0`, serialized at `:122`, restored at
`:147`. Total references to `.pressure` across every `.py` in the tree: **two.** One is that
serialization. The other is `systems/social_contest/sim/contest/resolver.py:241`,
`self.pr = venue.pressure` — **a different object's field entirely.**

So `Settlement.pressure` is **never written and never read for settlement behaviour.** Grep for the
homeostat itself (`sign(3-Π)`, `PI_RUNAWAY`) across the tree: **no hits.** L4 reported the only
executing Π was retired to `FORK:1e4c6f4`; that is confirmed.

**Consequences for the analysis, stated carefully:**
1. The `sign(3−Π)·min(1,|3−Π|)` term that pinned settlements at the ceiling **298/300**
   (`PI_RUNAWAY_SUSTAINED`, four independent measurements, quoted in
   `systems/_architecture/ners_vsg_reconciliation_v1.md §1`) **is not in the tree.** It is a
   validated *lesson about a formula*, and citing it as a present-tense defect would be false.
2. The whole Goldenfurt **runtime** is therefore unimplemented: the event deck's draw rule
   (`1 + ⌊Π/3⌋` cards per season), the tag-modifier re-weighting, and the homeostat all depend on a
   Π that nothing moves. Goldenfurt's *generation* half is prose (L4: no sampler); its *runtime* half
   is prose too. Both halves of the pipeline the methodology calls "the two halves of one pipeline"
   are reference under §0.05.
3. The forward-looking recommendation is therefore precise and cheap: **when Π dynamics are
   implemented, the known-failing bundle must not ship alone.** `ners_vsg_reconciliation_v1.md §1`'s
   own conclusion — *"E1 cannot ship, in VSG or anywhere else, without E3 and E7 landing in the same
   commit"* — is a design constraint waiting for the commit it constrains. And P4's boundary test is
   the guard that makes it enforceable rather than remembered: *run the generator at zero injected
   noise and confirm the output does not converge to the boundary* — which, per P4, would have caught
   this in five minutes instead of 300 runs.

## D9 — `pressure` is itself a vocabulary collision, found while checking D8
Two live objects carry a `pressure` field meaning different things:
- `Settlement.pressure` (`registry.py:79`) — the governance homeostat Π, band 0–10, dramatic band
  centred on 3.
- `venue.pressure`, read as `self.pr` (`social_contest/.../resolver.py:241`) — a social-contest venue
  property.
Same word, two scales, no shared state and no shared invariant. Under BRIEF.md's rule this is a
**vocabulary collision, not a throughline** — and it is exactly the kind that would survive a
keyword-based analysis. Logged for the KILLED list.

---


## The defect
```python
def _die_result(face: int) -> int:          # :53 — takes ONLY the face
    if face == 1:   return -1
    elif face <= 6: return 0
    elif face <= 9: return 1
    else:           return 2                # 10

def roll_pool(pool_size: int, tn: int = 7, ob=None, rng=None) -> RollResult:   # :75
    ...
    net = sum(_die_result(face) for face in rolls)                             # :82  <- tn absent
    return RollResult(pool_size=effective_pool, tn=tn, rolls=rolls, ...)       # :84  <- tn RECORDED
```
`tn` is accepted, **recorded on the result**, and **never used in the computation**. `_die_result`
takes one argument and it is not `tn`. The face rule is a constant.

Its continuous twin, twelve lines below, *does* honour TN:
```python
_CONTINUOUS_PARAMS = {6: (0.50, 0.806), 7: (0.40, 0.800), 8: (0.30, 0.781)}   # :68-72
def continuous_engine_sample(pool: float, tn: int = 7, rng=None) -> float:     # :87
    mu, sigma = _CONTINUOUS_PARAMS.get(tn, _CONTINUOUS_PARAMS[7])              # :98
```
and its docstring (`:91`) asserts it is *"statistically equivalent to discrete."*

## The measurement
The discrete face rule's expected value per die:
`(1/10)(−1) + (5/10)(0) + (3/10)(+1) + (1/10)(+2) = **0.400**`, sd **0.800**.

That is **exactly the TN-7 row** of `_CONTINUOUS_PARAMS` (μ=0.40, σ=0.800). So `roll_pool` is not
"ignoring TN" in some abstract sense — **it is pinned to TN 7**, and the asserted equivalence between
the two engines holds *only* at TN 7.

| pool | TN 6 | TN 7 | TN 8 | `roll_pool` at **any** tn |
|---:|---:|---:|---:|---:|
| 4D | 2.0 | 1.6 | 1.2 | **1.6** |
| 6D | 3.0 | 2.4 | 1.8 | **2.4** |
| 10D | 5.0 | 4.0 | 3.0 | **4.0** |

A 6D roll at TN 8 should net 1.8 and nets 2.4 — **+33%**, comfortably a full degree band on a
margin-based ladder. **19 production call sites pass `tn` to `roll_pool`** ⚠ *(corrected from 28 by Chapter 3's author, who counted them: 14 of the 33 raw grep hits call mass battle's OWN TN-honouring roller, not this one)*, including (per L1) the
Weapon TN Matrix. Every one of them at TN ≠ 7 is silently resolving on TN-7 odds.

## NERS verdict
```
ENGINE: engine/autoload/dice_engine.roll_pool    INSTANCE: A (core resolver)
VERDICT: NON-COMPLIANT — the difficulty lever is accepted, recorded and discarded

N: FAIL — 28 production sites pass a parameter with no effect. A lever that does nothing is the
         purest N failure available: the roll is not doing the work its callers believe it does.
R: FAIL — the discrete engine cannot express difficulty AT ALL. Its response to TN is flat across
         the whole range, so "leverage in-band across the whole range" is vacuously violated: there
         is no leverage. Severity HIGH.
S: FAIL — and this is the worst of the four. The discrete and continuous resolvers are canonically
         asserted equivalent (`:91`) and are equivalent at exactly one point (TN 7). Any mechanic
         that resolves discretely at one scale and continuously at another silently changes its
         odds when it crosses. This is a smoothness break at the most fundamental seam in the game.
E: FAIL — a player shown "TN 8" receives TN-7 odds. The displayed difficulty is not the difficulty.

REMEDIATION (worst-first):
  HIGH  S/R → give `_die_result` the TN: `_die_result(face, tn)` with the success threshold at `tn`
              rather than a hardcoded 7, so the discrete engine reproduces `_CONTINUOUS_PARAMS`
              at 6/7/8 by construction rather than by coincidence.
  HIGH  N   → falsifier FIRST, per §0.1 pt 3: a test asserting
              `mean(roll_pool(n, tn)) ≈ _CONTINUOUS_PARAMS[tn][0] * n` for tn ∈ {6,7,8} over a seeded
              batch. It fails today at TN 6 and TN 8 and passes at TN 7 — which is the control
              proving the test can observe the defect (§0.1 pt 2).
  MED   E   → once TN is live, the 19 call sites need auditing: some may have been tuned to
              compensate for the dead lever.
              ⚠ **CORRECTED — the fix is FREE, and this was measured rather than argued.** This block
              originally said "expect goldens to move; that is the honest cost". Chapter 3's author
              measured it instead: the TN-parameterised face rule ALREADY EXISTS at
              `systems/mass_battle/sim/resolution.py:36-42`, its moments reproduce
              `_CONTINUOUS_PARAMS` bit-exactly at TN 6/7/8, and it is **bit-identical to the current
              rule at tn=7** (all ten faces enumerated). Both goldens ran GREEN under an in-memory
              patch. **Golden cost: ZERO.** Lifting an existing correct implementation is cheaper
              than the fix I proposed and carries none of the cost I attributed to it.
```

## Why nothing caught it
It is a **read/write asymmetry of exactly the class CLAUDE.md §0.1 pt 1 names** — the caller writes
`tn`, the getter never reads it — and §0.1's own guard template (`test_morale_write_sweep.py`) exists
for the mirror-image case. `tn` is also faithfully stored on `RollResult`, so any test that asserts
"the result records the TN it was given" passes, and any test written against the TN-7 default passes.
The defect is invisible to every assertion that does not vary TN and check the *distribution*.

**This one belongs in the analysis' front matter**: it is executed, it is measured, it is in the core
resolver, it fails three NERS criteria, it silently affects 19 call sites across scales, and the fix
is roughly ten lines plus a falsifier.
