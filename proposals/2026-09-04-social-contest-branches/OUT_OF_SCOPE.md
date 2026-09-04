# OUT OF SCOPE — findings this session produced that Jordan did not commission

## Status: **PARKED (2026-09-04). NOT PART OF THE SOCIAL CONTEST WORK. Nothing here is prescribed.**
## These are real, anchored findings about **other subsystems**. They exist because the orchestrator
## misread the session's scope. They are recorded so the work is not lost and **removed from the
## social-contest prescription so they cannot distort its ranking.**

---

## §0 · WHY THIS FILE EXISTS

Jordan's brief asked for a reading *"top-down for all systems as well as bottom-up for each system"* —
meaning **the social contest system's own systems**: agôn, the three unbuilt branches, and the kernel's
component modules. His framing was singular throughout: *"audit the social contest system"*, *"over all
components within system"*, *"correct all subsystems and overall system"*.

**The orchestrator read one plural in isolation and expanded it to the repository's fifteen
subsystems.** That produced `07_TOPDOWN_BOTTOMUP.md`, a whole-tree reading, and seeded a Tier 2 in
`09_PRESCRIPTION.md` about territory ownership, mass battle and the Key substrate — none of it
commissioned.

Worse, the misreading was then used to **justify** the scope when Jordan questioned it, and to rank
out-of-scope findings **above** the branch work he actually asked for. Both are corrected. The
correctly-scoped reading is `10_SC_STRUCTURAL_READING.md`.

**Nothing in this file is a recommendation.** Each item is a finding with its evidence, parked for a
session that wants it.

---

## §1 · THE FINDINGS, WITH THEIR EVIDENCE

### 1.1 · The victory condition advertises three clauses and has two — VERIFIED

`engine/autoload/victory.py:73` reads `world.clocks.get('Turmoil', 0.0)`. `game_state.py:338`
initialises `Turmoil` to `0.0` and **nothing in `engine/` or `systems/` ever writes it** (verified by
grep across both trees). With `PS_MAX = 6.0`, `ps_ok = (0.0 <= 6.0)` is **always True**, so the
Political-Stability clause cannot ever gate a win. Campaign-reachable — `mc_v18` imports and resets
`victory`.

**Jordan ruled 2026-09-04: "leave it, file the finding."** Two honest dispositions when someone does
take it up — **(a)** wire `Turmoil` a writer among the events that already move Stability and
Legitimacy, or **(b)** delete the clause, since `ps_ok` and `PS_MAX` otherwise assert a rule the game
does not have. **Falsifier owed with either:** construct a world at `Turmoil > PS_MAX` with all other
clauses satisfied and assert the faction does **not** qualify. It must fail on today's tree.

*(An ED row for this was drafted and is held in `stash@{0}`, unlanded.)*

### 1.2 · A second grammar produces the same four degree words

`systems/mass_battle/sim/massbattle.py:130-139` maps rout state and survivor fractions to
`Overwhelming/Success/Partial/Failure` with three uncited thresholds; `faction_action.py:470-524`
consumes it to key Terms/Storm and Accord **with no marker of which grammar produced it**.

⚠ **The single-owner guard's exemption is documented and reasoned** — `test_degree_ladder_single_owner.py:394-396`
exempts band-producers that are not dice-margin ladders and says so in terms. **No guard failed**, and
an earlier framing of this as "slipping the rule" was unfair and is withdrawn. Under `CLAUDE.md`
§0.06's S definition — *"calculations consistent in methodology with other mechanics"*, glossed as
**"two ladders for one quantity is an S defect even when each is individually correct"** — it is an S
defect at the consumer, not a single-owner violation.

### 1.3 · Territory ownership has three stored homes

`Territory.owner` · `Faction.territories` · `Settlement.owner_faction`. `mass_seizure.py:290` writes
only the first (latent — zero callers), no transfer path ever writes the third, and `mc_v18.py:295`
scores a winner from two of them **in one expression**. `parliamentary_transfer.py:347-360` records a
prior divergence, so this has already gone wrong once. PR #362 `D-10` names the class.

### 1.4 · Mass battle re-implements four engine primitives, one guarded

`resolution.py:37` (die rule), `:209` (soft-cap), `:221` (μ-shift with its own `_SIG_PER_DIE`), `:104`
(ladder). No test compares the σ pair to `sigma_leverage` (searched `tests/valoria`, `engine/tests`;
**`tests/sim/` was not searched** — a parity test there would overturn this). A drift in `M_MAX` or
per-die σ in either home moves every conquest unseen.

### 1.5 · Key ids cannot survive a restore

Ids come from three undeclared per-`World` counters that `serialize_world`/`restore_world` do not
carry, so the replay premise asserted at `module_contracts.yaml:1545` cannot hold across a reload.

### 1.6 · Smaller, recorded without investigation

- `insurgency_pipeline.py:248`'s "promotion to faction" never creates a `Faction`.
- Four subsystems (fieldwork, threadwork, characters, settlements beyond world-gen) are composed
  correctly on the owner primitives and **unreachable from the season loop**.
- **20 rules with more than one home** tree-wide, 17 new to that reading; the load-bearing unguarded
  ones are §1.4's σ/die re-implementations, seven private `MULTS` copies, §1.3's ownership relation,
  and two pool-floor rules with three homes each. Twelve `_store(world)` routers and eleven `TN = 7`
  declarations are counted but graded **inert** under §0.1 pt 5.

---

## §2 · WHAT AN INDEPENDENT READER SHOULD KNOW

- **These findings were produced by a reading with stated gaps** — `npcs` and `ui` not reached,
  `_architecture` surface-only, ~10,300 lines of combat and mass-battle interior unread. §1.4 names its
  own overturning condition.
- **They are not ranked.** Ranking them against each other, or against anything, is work for a session
  that is actually scoped to them.
- **`07_TOPDOWN_BOTTOMUP.md` remains in the tree** as the record of what was read, carrying an
  out-of-scope banner. Its `social_contest` section is the only part inside the commissioned scope, and
  it is superseded by `10_SC_STRUCTURAL_READING.md`.
