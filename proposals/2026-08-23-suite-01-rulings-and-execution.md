# Suite 01 — The Three Rulings, and What the Tree Actually Does

**Status:** EXECUTION-READY ANALYSIS. The three rulings are Jordan's and are not in question here.
What this document establishes is what the working tree does *today*, exactly which sites must change,
exactly which guards fire, and — the part that matters most — **which design questions each ruling
implies but does not answer**.

**Method note.** Every site below was opened and read. Two claims published earlier in this session
were wrong and are corrected here in place, with the reading that overturns them. `grep` located
candidates; it concluded nothing.

---

## §0 The rulings

> 1. **Mass Battle Tree A** — the short tree used for simulations — is deprecated and must be removed.
> 2. **TN is always 7.** Threadwork is always 7 for TN too.
> 3. **All pools are contained within one single document**, which all subsystems call to get the
>    appropriate pool.

---

## §1 Ruling A — remove Mass Battle Tree A

### §1.1 What Tree A is, and what depends on it

Tree A is `systems/mass_battle/sim/` — `massbattle.py` (~1,900 lines) plus `units.py`,
`tactic_cards.py`, `altonian_reinforcements.py` and the package `__init__`. Its header
(`massbattle.py:1-30`) records it as the Phase-7 bare port of `tests/sim/sim_mb_06_v22.py`. Tree B —
`tests/sim/mass_battle/` — is the canon engine per Jordan ruling **J2 (2026-08-03)**.

**Exactly one production module imports Tree A:**

```
systems/factions/sim/faction_action.py:452
    from systems.mass_battle.sim.massbattle import resolve_mass_battle
```

That is the whole production dependency. One earlier candidate is a false positive and is recorded so
it is not re-raised: `engine/cross_scale/scene_dispatch.py:292` names `massbattle.py:1826-1830` **in a
comment**, not an import.

### §1.2 The blocker is real and is not the adapter's absence

`resolve_mass_battle` builds Units from `faction.Mil` using minimum-viable defaults, and says so:
`massbattle.py:1867-1873` carries `[GAP: faction→unit construction has no canonical spec]`. So the
strategic→tactical adapter is *undesigned*, not merely *unwritten* — repointing `faction_action.py:452`
at Tree B requires authoring the construction spec, not moving an import.

The measured incompatibility is encoded at `tests/valoria/test_j2_mass_battle_seam.py:96-98`: a Unit
built by Tree A's `_faction_to_unit` and handed to Tree B's `run_battle` raises
`AttributeError: 'Subunit' object has no attribute 'cells_float'`. Tree B is cell-based; Tree A's
Units are not. (Read, not executed, in this pass.)

### §1.3 CORRECTION — five guards fire, not one

**This session previously published that exactly one guard blocks removal, and that the seam test
"passes in state B by construction." Both halves are wrong.** The correction, from reading the files:

| # | Guard | What happens on deletion | Action |
|---|---|---|---|
| 1 | `tests/valoria/test_j2_mass_battle_seam.py:74, 89-90, 111` | **FAILS.** The state-B probe `_canon_accepts_a_strategic_unit()` itself imports `systems.mass_battle.sim.massbattle` (:74) and builds its probe units via `old._faction_to_unit` (:89-90). With the module gone the `except ImportError` returns `False`, so `state_b` is False and `state_a` is False, and the assert at :111 fails. | **Rewrite.** The probe hard-binds the adapter's home to the module being deleted; the new adapter's location must be threaded in. |
| 2 | `tests/valoria/test_mass_battle_systems_movement.py:27` | **Collection ImportError.** Top-level `from systems.mass_battle.sim import massbattle as MB`; the whole file targets Tree A (DG-10 wired-engine coverage). | Port to Tree B or retire with the tree. |
| 3 | `tests/valoria/test_import_cycle_game_state_npe.py:56-81` | **Fails twice.** Asserts `len(cycles) == 3`, one family being exactly `{massbattle, units}` with `len(family) == 1`. Deletion drops the count to 2 and empties that family. | Drop the MB family and the count to 2. |
| 4 | `tests/valoria/test_degree_ladder_single_owner.py:105-107` | **Fails.** `_massbattle_twin()` imports the module to register Tree A as a declared ladder adapter. | Remove the row. |
| 5 | `engine/tests/test_pipeline_reach.py:782-793` (+ manifest row :168) | **Fails.** Probes `systems.mass_battle.sim.altonian_reinforcements` expecting outcome `raw_stub`; an import failure is not `raw_stub`. | Delete the test and its XFAIL_MANIFEST row, as its own docstring instructs. |

**The evacuation keep-pin is *not* a gate** — that half of the earlier correction stands.
`tests/valoria/test_evacuation_plan.py:101-103` classifies a *string*, and its docstring at :102 says
"Paths need not all exist." And `test_j2_mass_battle_seam.py:150` releases the pin requirement the
moment the file is gone (`... or not RETIRED_TREE.exists()`).

Bookkeeping sites, non-blocking: `tools/observability/build_decisions.py:112-113` lane-map rows;
`tools/review_core.py:74` stub-ceiling comment (the review baseline may shift — report-only).

### §1.4 Ordering

The one thing not to do is delete first. Deletion with the guards unrewritten produces five failures
that say nothing useful about the migration. The order that works:

1. **Author the strategic→tactical construction spec** — what a `faction.Mil` of 4.0 *is* in cells.
   This is a design task, not a refactor, and it is the actual blocker.
2. Build the adapter in its new home (Tree B side or a seam module).
3. Rewrite guard 1's probe against the new home; port or retire guard 2.
4. Repoint `faction_action.py:452`.
5. Delete the tree; update guards 3, 4, 5 and the bookkeeping rows.

### §1.5 Cross-ruling interaction

**Ruling A deletes one of the seven pool formulas.** `systems/mass_battle/sim/units.py:398-407`
`base_combat_pool()` lives in Tree A. The pool document of Ruling C must therefore cite **Tree B's**
mass-battle pool, not this one. Neither of this session's earlier documents states this, and a naive
execution of C would enshrine a formula that A removes.

---

## §2 Ruling B — TN is always 7

### §2.1 The ruling is already true in behaviour, and false in declaration

`engine/autoload/dice_engine.py:75-84`:

```python
def roll_pool(pool_size, tn=7, ob=None, rng=None):
    effective_pool = max(1, pool_size)
    rolls = [rng.randint(1, 10) for _ in range(effective_pool)]
    net = sum(_die_result(face) for face in rolls)
    ...
    return RollResult(pool_size=effective_pool, tn=tn, ...)
```

`tn` is **stored and never read**. The face rule is hardwired at `:53-61` — `1 → −1`, `2-6 → 0`,
`7-9 → +1`, `10 → +2`. That *is* TN 7, structurally.

So every non-7 TN declaration in the tree has been a no-op for as long as this roller has existed.
**Ruling B does not change behaviour anywhere. It ratifies what the code already does and deletes a
false declaration.** That reframing is the single most useful thing in this section, and it inverts
how this session originally reported the finding: the TN-blind roller was published as the defect; under
the ruling it is correct, and the declarations are the defect.

### §2.2 Every non-7 site, by AST

An AST sweep for `Load` references to the TN names across the live tree:

```
TN_BINDING (=8)      systems/threadwork/sim/operations.py:303, :312
                     systems/threadwork/sim/opposing.py:131
                     systems/threadwork/sim/collective.py:147
TN_POP (=8)          systems/threadwork/sim/operations.py:286
                     systems/threadwork/sim/opposing.py:134
                     systems/threadwork/sim/collective.py:150
TN_POP_BINDING (=9)  — ZERO loads anywhere. Dead constant.
```

Seven live call sites carry a non-7 TN; one constant is dead. All seven route to
`operations.py:176` `roll_pool(pool, tn=tn, rng=rng)` — the TN-blind path. Behaviour today is TN 7 at
all seven.

The second declaration site is `systems/combat/sim/combat.py:57-62, 136-145` (base 7, weapon
modifiers → 5-8), which also feeds `roll_pool` (`:214-216`). That file carries a **DEPRECATED** banner
(`:4-11`) naming `combat_engine_v1` as its supersession, so it is a labelled historical file, not a
live rival.

Declarations of 7 (consistent, but duplicated owners): `engine/autoload/sigma_leverage.py:87`,
`systems/threadwork/sim/operations.py:47`, `tests/sim/v32-combat-balance/m1_dice_sigma_core.py:31`
(frozen test tree).

### §2.3 The three things that must be handled, which the earlier documents missed

**(a) The continuous engine *does* read TN.** `dice_engine.py:87-101`:

```python
_CONTINUOUS_PARAMS = {6: (0.50, 0.806), 7: (0.40, 0.800), 8: (0.30, 0.781)}
def continuous_engine_sample(pool, tn=7, rng=None):
    mu, sigma = _CONTINUOUS_PARAMS.get(tn, _CONTINUOUS_PARAMS[7])
```

So there are **two** entry points, and only one is TN-blind. Under Ruling B the `6:` and `8:` rows
become unreachable-and-wrong, and `sigma_leverage.roll_net_continuous` inherits the same knob. Any
removal of the `tn=` parameter must cover both, or the discrete and continuous paths stop agreeing on
what the ruling means.

**(b) The HELD remediation docket recommends the opposite of the ruling.**
`audit/2026-08-11-divergence-audit/02_remediation_plan.md` A5 (:608-640) recommends option **(a)**,
*"fix and let TN 8/9 go live"* (:636). Jordan's ruling selects (b). Executing Ruling B must close or
annotate A5, otherwise a later session following the plan implements the ruling's negation. Related:
A4 (:599-606) specifies a guard `tests/valoria/test_tn_single_owner.py` that would **exclude** the
three threadwork constants as "non-standard **on purpose**" — that guard does not exist yet, and must
not be written to that spec.

**(c) Provenance tags will be falsified.** `operations.py:45-46` tags the constants
`[canonical: params/threadwork.md §TN Modifiers]` (PP-619). Setting them to 7 makes the citation false.
This needs an ED superseding PP-619's TN rows, plus a tag update. Whether
`tools/ci_sim_fabrication_check.py` (which matches by `(variable, value)`) blocks the value change is
**unverified** — check before the commit, not after.

### §2.4 The design question the ruling implies and does not answer

Threadwork's TN 8/9 existed to make **Binding operations** (Lock, Dissolution) and **Past-Oriented
Pulling** harder than Weaving, Pulling and Mending. Collapse TN to 7 and that differentiation
disappears from the TN axis. The obvious move — push it into Ob instead — **does not reproduce it**:

Per-die mean is 0.40 at TN 7 and 0.30 at TN 8. For a pool of *N* dice the mean net drops by
**0.10 × N**. A TN step is therefore **pool-proportional**; an Ob step is flat. There is no constant
Ob increment that reproduces a TN increment across pool sizes — a Spirit-7 practitioner (pool ~18)
and a Spirit-2 novice (pool ~7) would need Ob bumps of +1.8 and +0.7 respectively.

Concretely: **collapsing TN to 7 removes a difficulty lever that scaled with competence, and it cannot
be replaced by a flat Ob bump.** That is a real design consequence, and it is a live one — because
behaviour has *already* been TN 7 everywhere (§2.1), the lever has in fact been absent for as long as
this roller has existed, and no one noticed. The ruling makes the code honest. What it leaves open is
whether Binding *should* be harder than Weaving, and if so, on which axis.

That question belongs to Jordan, and it is the only open item in Ruling B.

---

## §3 Ruling C — one pool document

### §3.1 The eight pool formulas

Read at source. Note that **three of the eight are not discoverable by name** — an AST sweep for
functions with "pool" in the name finds only five of them. That fact is itself an argument for the
ruling.

| # | Home | Formula | Notes |
|---|---|---|---|
| 1 | `systems/combat/combat_engine_v1/core.py:50-52` | `max(5, round(History) + 6)` | **The canonical combat pool.** Agility-INDEPENDENT by ED-901, re-ratified ED-900/904 — a deliberate break from the shared shape. |
| 2 | `systems/combat/sim/combat.py:121-133` | `max(5, (Agi×2) + History + 3)`, then wound and out-of-breath penalties | DEPRECATED banner at `:4-11` names #1 as its supersession. Not a live rival; disposed. |
| 3 | `systems/social_contest/sim/contest_legacy_stub.py:124-129` | `max(1, (Primary×2) + History + fatigue)` | Legacy stub. Floor is **1**, not 5. |
| 4 | `systems/social_contest/sim/contest/primitives.py:208-211` | `Pool.size(faculty) = max(5, faculty×2 + 3)`, `BASE = 3` `[SEED]` | A **class** named `Pool` with a static `size` — invisible to a name sweep. `BASE` is an unratified seed. |
| 5 | `systems/threadwork/sim/operations.py:145-157` | `(Spirit×2) + min(3, History+3) + (TS // 10)` | PP-616/PP-624. |
| 6 | `systems/fieldwork/sim/knots.py:214-216` | `(Spirit×2) + history_relationships` | An **inline expression**, not a function. **No floor at all.** |
| 7 | `systems/mass_battle/sim/units.py:398-407` | `max(1, floor(min(effective_size, command) + command + discipline_pen + stamina_pen))` | **Lives in Tree A — Ruling A deletes this.** The document must cite Tree B. |
| 8 | *doc only* — `systems/fieldwork/fieldwork_v30.md:475` | `Spirit × 2` | Contradicts #6 — see §3.2. |

The shared shape across most of these is `(Primary Attribute × 2) + History-derived term +
subsystem term`, with a floor. **#1 deliberately abandons it** (no Agility, History-only). The pool
document must record that as a ratified exception, not normalise it away — that would silently
overturn ED-901.

Floors are unnormalised: 5, 5, 1, 5, none, none, 1.

### §3.2 A ninth site: two canonical docs disagree on the same roll

This landed inside the ruling's scope and neither of this session's earlier documents carries it.
The Knot Formation roll is specified twice:

- `systems/fieldwork/fieldwork_v30.md:475` — *"Resolution: Spirit pool (Spirit × 2) vs TN 7, Ob 2."*
- `systems/fieldwork/knots_v30.md:76` — *"Roll: **Spirit × 2 + History (Relationships)**, TN 7, Ob 2."*

Same operation, same TN, same Ob, **different pool**. Both are canonical heads. The code sides with
`knots_v30` (`knots.py:214-216`). The pool document must adjudicate, and `fieldwork_v30.md:475` must
then point at the owner rather than restate a formula.

**A second disagreement at the same site, outside the pools ruling but worth recording here because
it will be found by whoever fixes the first.** `fieldwork_v30.md:477-478` gives the degree bands as
*"Overwhelming (3+ net) / Success (2 net)"* — an **absolute-net** reading. The ruled ladder
(`dice_engine.degree_from_net`, Jordan 2026-08-14) reads the **margin** `net − ob`. At Ob 2,
Overwhelming requires margin ≥ 3, i.e. net ≥ 5 — not 3. `knots_v30.md` states no numbers and is
therefore compatible. So `fieldwork_v30.md` contradicts the degree ruling as well as the pool.

### §3.3 The chokepoint the document should name

`engine/autoload/sigma_leverage.py:284`:

```python
effective_pool = max(1, int(round(pool)))
```

The pool is rounded to an integer **before** the fractional-capable continuous engine sees it, which
defeats fractional pool capability at the point of use. (`:273` is the discrete twin — there are two
rounding sites, and only `:284` is the one that matters here.) `faction_action.py:107-116` records
this as ED-IN-0187, ledger-recorded and unapplied; its inline citation of `:276` has drifted by a few
lines.

Whatever the pool document says a pool *is*, this line decides what the engine can actually consume.

### §3.4 What the document trips, and what it does not

**Nothing.** There is no pool-owner guard in the tree, so authoring a document that records the eight
formulas and names an owner per subsystem breaks no test.

What *would* trip is any **behavioural** consolidation done under the ruling's cover — retiring #2,
normalising the floors, changing #4's `BASE` seed, or unifying #1 back onto the shared shape. Those hit
the seeded `engine/tests/` regression suite (CI job `sim-regression`) and the combat goldens, and #1
in particular is protected by ratified invariants (ED-PC-0038/0039).

**The safe reading of Ruling C is: one document that owns the formulas and is cited by each subsystem,
with the subsystems' behaviour unchanged on landing.** Normalisation is a separate decision, and it
needs Jordan, because at least three of the differences (#1's Agility-independence, #3/#6's missing
floors, #4's seeded BASE) are substantive design positions rather than drift.

---

## §4 Summary — what is decided, what is blocked, what needs Jordan

| | Ruling A (Tree A) | Ruling B (TN 7) | Ruling C (one pool doc) |
|---|---|---|---|
| **Behavioural change on landing** | Yes — the conquest path changes engine | **None** — already TN 7 everywhere | **None**, if authored as a document |
| **Blocked on** | Authoring the `faction.Mil` → cells construction spec | Nothing | Nothing |
| **Guards to handle** | **5** (§1.3) | 0 today; do not write A4's guard to its current spec | 0 |
| **Needs Jordan** | The construction spec | Whether Binding stays harder than Weaving, and on what axis (§2.4) | Whether to normalise floors, #4's `BASE`, and #1's Agility-independence — or only to document them |
| **Documents to correct** | — | remediation plan A4/A5; PP-619 TN rows | `fieldwork_v30.md:475` (pool) and `:477-478` (degree bands) |

**The honest headline across all three:** two of the three rulings change no behaviour at all. They
make the tree say what it already does. Ruling A is the only one that changes what the game computes,
and it is blocked on a design question — what a strategic army *is*, in cells — that no amount of
refactoring will answer.

---

## §5 Corrections this document makes to earlier session output

1. **"One guard blocks Tree A removal, and the seam test passes in state B by construction."** Wrong.
   Five guards fire; the seam test **fails**, because its own state-B probe imports the module being
   deleted (`test_j2_mass_battle_seam.py:74, 89-90`). The keep-pin half of the claim stands.
2. **"The TN-blind roller is the defect."** Inverted by the ruling. The roller is correct; the seven
   non-7 call sites and the `_CONTINUOUS_PARAMS` 6/8 rows are the defect.
3. **"Seven pool formulas."** Eight, plus a doc/doc contradiction — `contest/primitives.py:208-211`
   and `knots.py:214-216` are invisible to a name-based sweep, and `fieldwork_v30.md:475` disagrees
   with the code.

---

_Verified 2026-08-23 against `claude/fable5-investigations-architecture-1phbx9` at `512400f`.
Not verified in this pass: the `cells_float` reproduction (read, not executed);
`ci_sim_fabrication_check` behaviour on a TN constant change; the Monte-Carlo TN comparisons quoted
in earlier session documents._
