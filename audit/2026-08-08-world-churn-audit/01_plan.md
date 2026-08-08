# World Churn — the interdependency plan

## Status: PROPOSED — nothing here is ratified by merging this audit PR. Tier 3 is HELD for Jordan.
## Date: 2026-08-08 · Lane: IN (cross-cutting) · ED-IN-0148 · Companion: `00_findings.md`

---

## §0 · The strategy, and why it is this one

The audit's finding dictates the shape of the plan. The machinery is **built and disconnected**, not
missing and not scripted. So the plan is **not** "build a churn engine" — most of it exists. It is:

1. **Repair what is actively wrong** (a gate that silently no-ops, an unfalsifiable victory condition,
   comments asserting properties the tree lacks).
2. **Connect the highest-leverage single edges** — where *one* edge lights up machinery that is already
   fully written and currently unreachable.
3. **Instrument the connectivity itself**, so re-disconnection becomes a test failure rather than the
   subject of the next audit.
4. **Force the decisions that are genuinely Jordan's**, rather than guessing defaults into the tree.

**Ordering principle: leverage per unit of new design.** An edge that makes 200 lines of existing,
tested, unreachable code live is worth more than a new subsystem — and risks less, because the thing it
switches on was already reviewed.

**Two disciplines bind every item below**, both from CLAUDE.md §0.1:
- **Every item names its falsifier** — the specific test that would show it wrong — and that test ships
  in the same commit. An item without one does not land.
- **Behaviour-changing items land flag-gated OFF with byte-exact goldens unchanged**, following the
  repo's own established pattern (the MB honest-gauge/closing-ranks/intent precedent). Flipping a
  default is a separate, deliberate, measured act — not a side effect of wiring.

---

## §1 · TIER 0 — correctness repairs (no new design; safe to execute now)

### T0-1 · Fix the conviction gate, not the call site
**Defect:** D6. `apply_conviction_scar` returns `magnitude=0` for an unrecognised conviction name while
the caller reports `conviction_scar=1` (`knots.py:345,348-353` · `conviction.py:46-49,191-193`).
**Change:** make an unknown conviction name a *loud* failure at the gate (raise, or WARN-tier per the
`stat_vocabulary` precedent at `keys.py:436-451`) and make the caller's reported count reflect the
applied magnitude. Compose on the existing vocabulary-check pattern — do not add a second one.
**Falsifier:** a test asserting (a) an unknown conviction name does not silently yield magnitude 0, and
(b) reported `conviction_scar` equals applied magnitude. Both fail against today's tree.
**Why now:** inert only because `apply_knot_loss` has no production caller. Every future scar writer
would no-op through the same hole — this is a §0.1-point-5 pattern defect, so it gets one owner and a
guard.
**Lane:** WR (Knots/Convictions are core personal-narrative state, per the ED-912 precedent).

### T0-2 · Retire the stale claims
**Defect:** §4. Five comments assert properties the tree lacks — most damagingly that scenes are
"side-effect-free on strategic stats by construction" (`scene_dispatch.py:417-418`, `mc_v18.py:138-140`),
false since ECHO_TRANSPORT defaulted ON.
**Change:** correct each to what the tree does, citing the test that proves it
(`test_battle_concluded_key.py:71`, `test_faction_l_reconstruction.py:103-132`). Fix the
`scene.accord_echo` misattribution (`faction_action.py:324-325`) and the retired-tree test path
(`echo_transport.py:22`). Correct `treaty.py:11-15`'s false claim about `crown_initiative`.
**Falsifier:** none is honest here — this is text, and a guard on prose phrasing would be theatre. The
verification is the cited tests already passing. Stated plainly rather than dressed up.
**Lane:** IN.

### T0-3 · Guard the `temperaments.py` read/write asymmetry
**Defect:** §3. Writer stores into `world.npc_drift_state` (`:153,158`); reader cannot accept a `world`
argument at all (`:105,117`). Both sides zero-caller today — a wired-tomorrow trap of exactly the
§0.1-point-1 class.
**Change:** register `npc_drift_state` in the field-parameterized `_CELL_OWNED` guard
(`tests/valoria/test_morale_write_sweep.py` is the named template) so a future bare assignment fails,
**and** fix the reader signature so the asymmetry cannot be wired in.
**Falsifier:** the guard itself — it must fail if the reader is called without a world while a
world-scoped write exists.
**Lane:** WR.

### T0-4 · The connectivity instrument (the highest-value item in Tier 0)
**Defect:** D7/D8, and the audit's own weakest claims. "39 of 55 types have zero traffic", "10 of 13
subscriptions have no producer", "no code sets `owner = None`" all rest on **grep with no guard** —
exactly the blind spot §0.1 point 5 says a guard is required to make tolerable.
**Change:** one instrument, single-owner in `tools/`, that computes from the tree: per Key type,
{emitters, consumers}; per subscription, whether a producer exists; per contract row, whether the
declared edge is realized in code. Emit a report, and pin the **current** numbers as a baseline so a
regression is visible. Report-only first (the repo's own precedent for a new gate).
**Falsifier:** mutation — remove a known emitter and the instrument must notice. Verify against the
findings above: it must independently reproduce "3 emitters live", "10 subscriptions producerless".
**Why this matters most:** it converts the entire audit from a document that ages into a gate that
holds. It also makes the *next* disconnection cheap to find.
**Lane:** IN.

---

## §2 · TIER 1 — the high-leverage edges (design-bearing; land flag-gated OFF)

### T1-1 · Battle → `Mil` attrition  ⭐ *recommended first*
**Defect:** D4. Casualties evaporate; `Mil` is a monotone ratchet with only a stat ceiling as brake.
**Change:** apply the **already-computed** `attacker_size_pct`/`defender_size_pct`
(`massbattle.py:1850-1851`) to `Faction.adjust('Mil', …)` (`game_state.py:124`) at the transfer block
(`faction_action.py:461`).
**Compose on:** the architected path the code *itself* names at `faction_action.py:454-458` — a consumer
of `scene.battle_concluded`, which is already emitted every campaign with no consumer. This is the
natural first real Key **actuator**: it turns the substrate from telemetry into a wired consumer using an
existing key, an existing deferred-apply primitive, and an existing mutator. **No new mechanism.**
**Falsifier:** a seeded-campaign test asserting a faction that loses battles ends with lower `Mil` than
one that does not; today's tree cannot distinguish them.
**Risk:** changes campaign balance. Lands flag-gated OFF, goldens byte-exact; the default flip is a
separate measured decision with a control (§0.1 point 4).
**Lane:** FA (with MB observation).

### T1-2 · Revolt → `Territory.owner = None`  ⭐ *highest leverage in the audit*
**Defect:** D1. One missing edge strips an entire built, tested, per-season-invoked emergent subsystem of
any possible input.
**Change:** implement the Revolt step in `run_accounting` per `peninsular_strain_v30.md:483` — at Accord
0, set `t.owner = None` and bump Turmoil. **Canon-cited, therefore executable rather than invented.**
**Compose on:** existing `Territory.is_uncontrolled()` (`game_state.py:153`) and the existing accounting
step sequence (`accounting.py:95-142`). Downstream streak/formation machinery already works.
**Depends on:** T1-3 (Turmoil needs a writer before Revolt can bump it).
**Blocked by:** **J-B** — insurgency `L` growth has *no canon rule in code*, so even with Revolt wired,
promotion stays unreachable. Lens C is explicit: this needs a **ruling, not an invented rate**. T1-2
therefore delivers *formation*, not *promotion*, and says so.
**Falsifier:** a seeded-campaign test asserting `insurgencies_formed > 0` becomes *reachable* — today it
is structurally 0. Plus a guard that fails if the only `owner = None` site is removed.
**Lane:** WR (accounting/strain) with FA coordination.

### T1-3 · Turmoil writer, and de-vacuating the victory condition
**Defect:** D2. `victory.py:73` reads Turmoil; nothing writes it; the `PS ≤ 6` leg cannot fail.
**Change:** a `turmoil_track.py` mirroring the **existing single-owner `ci_track`/`ms_track` pattern**
(apply-delta + seasonal compute), fed by the §4.1 territory-instability count.
**Blocked by:** **J-E** — `Strain` / `Turmoil` / `PI` are three keys for what the docs treat as one or two
concepts (`peninsular_strain_v30.md:286-333` is titled "Turmoil Counter" but its rules say "Strain"; the
registry says PP-403 repealed PI while code still instantiates it). Collapsing them is a canon call.
Building a writer before that ruling would cement the wrong key.
**Falsifier:** a test asserting the `PS ≤ 6` victory leg *can* be false — impossible today.
**Lane:** WR.

### T1-4 · Council → `Sta` (let the crisis scene clear its own trigger)
**Defect:** D3. The scene writes `L` only, so it refires identically every season.
**Change:** a mapping row so the emergency-council verdict can move `Sta`.
**Compose on:** `ctx['echo']['most_relevant_stat']`, which **already carries an arbitrary stat name**
through `domain_echo` → `Faction.adjust` (`echo_transport.py:430-438`). A ruled row, **not new
machinery**.
**Blocked by:** **J-F** — direction and magnitude are a design call (should winning a stability contest
*raise* `Sta`, and by how much?). Proposing a number here would be exactly the fabrication §0.1 forbids.
**Falsifier:** a test asserting a faction entering `Sta ≤ 2` does not refire an identical contest for N
consecutive seasons.
**Lane:** SC/FA.

### T1-5 · Season/accounting boundary Keys
**Change:** emit `mechanical.season_change` and `mechanical.accounting` — both already in the roster,
both currently emitted by nothing, though the scheduler is attached and the boundary is driven at
`mc_v18.py:158-161`.
**Compose on:** the exact log-only emitter pattern at `faction_action.py:348-394` (no `apply=`,
scheduler-presence guard).
**Why:** cheap, zero behaviour change, and it gives the detect/forecast layers a temporal spine to read
later. Also the smallest possible proof that adding traffic to the substrate is routine.
**Falsifier:** a seeded-campaign test asserting both types appear in the KeyLog with the expected
cardinality.
**Lane:** IN.

---

## §3 · TIER 2 — substrate maturation (sequenced after Tier 1, mostly gated)

- **T2-1 · ORD-3 / ORD-4 + the `canonical_key_log` serialization spec.** Lens G's "revive first", and I
  agree: it already blocks the substrate's own observer steps (`engine/substrate/__init__.py:17-19`),
  `propagation_spec_v1.md:393` names it as its own precondition, and everything forecast-shaped is
  downstream. **Blocked by J-D-adjacent ratification.** Cheapest unblock with the widest downstream.
- **T2-2 · Key → person applier.** Both ends exist as single-owner primitives (`Target.impact_vector`
  `keys.py:96-97`; actor-keyed stores `game_state.py:182-195` with `apply_conviction_scar` /
  `apply_coherence_delta`), and `ACCOUNTING_BOUNDARY` is already a defined phase. **Hard-gated on J-C**
  (three conviction vocabularies) — building this first would be shape divergence by construction.
- **T2-3 · Layer-A forecast only.** Ratified, deliberately Layer-A-as-hard-gate for M1, and its analytic
  inputs (`sigma_leverage.p_success`, clamp bands) are live code. **Layer B stays gated.**
- **T2-4 · `process_treaty_expirations` on the arc boundary.** The hook exists (`season_manager.py:39`);
  the function is one import away (`treaty.py:121`). Needs a treaty *formation* path to be non-trivial —
  file rather than force.

**Explicitly NOT proposed:** the R-F1/R-HB/R-CL/R-AI/R-RL conformance checkers. A conformance rule with
no kernel to check is a display string. R-F2's surface is the one that mattered early, and it landed.

---

## §4 · TIER 3 — decisions that are Jordan's (held, not guessed)

| Id | Decision | Why it cannot be defaulted | Blocks |
|---|---|---|---|
| **J-A** | **The L0 identity fork.** The ratified arc-template L0's calibration corpus was evacuated, so it cannot run as specified; an *unratified* proposal (`settlement_generator_v1.md:127`) has claimed the slot. Either restore the arc register from `c451bcb` and run the ratified compile, or rule that VSG supersedes it. | Leaving both true is scripting-drift-by-neglect: a ratified and an unratified design in one slot. | M2 S1, and every downstream stage |
| **J-B** | **Insurgency `L` growth rule.** No canon-cited rate exists in code. | Inventing a rate is fabrication; §0.1 forbids it. | T1-2's promotion half |
| **J-C** | **Conviction vocabulary.** 4 substrate axes vs 9 character-sim names vs 8 NPE names. | Any person-facing Key edge built first is shape divergence by construction. | T2-2 |
| **J-D** | **ED-1051 `engine_clock` ratification** (`open`, `needs_jordan: true` since 2026-06-30). | The temporal spine's home doc. A world cannot churn without a ratified clock. | M1 season-close, M3 G0 |
| **J-E** | **Strain / Turmoil / PI key collapse.** | Three keys, one-or-two concepts, one repealed-but-instantiated. | T1-3 |
| **J-F** | **Council→`Sta` direction and magnitude.** | A balance call with no canon number. | T1-4 |
| **J-G** | **`spec/churn_amendments.md`** — a RATIFIED normative companion that no longer resolves; its content sits inside a file banner-marked "Not independently ratifiable", and `CURRENT.md:165` still cites the dead path. | Ratification status of a doc that physically does not exist is not mine to assert. | Provenance integrity |
| **J-H** | **`valoria-arc-generator` skill reads evacuated paths** and would recreate a "do not recreate" tree. Retire, repoint, or rewrite? | It is a skill contract, and the arc surface's future depends on J-A. | D11 |

---

## §5 · What I propose to do in this session

**Execute:** Tier 0 in full (T0-1 … T0-4). All four are correctness repairs, guards, or instruments —
none changes campaign behaviour, none requires a design ruling, and each ships its falsifier.

**Author but hold OFF:** T1-1 and T1-5 — flag-gated, goldens byte-exact, defaults untouched. These are
the two Tier-1 items with no blocking Jordan decision.

**Do not start:** T1-2/3/4 (blocked on J-B/J-E/J-F), all of Tier 2, all of Tier 3.

**Loudly held, per the ED-1094 exception rule:** merging the audit PR must **not** be read as ratifying
anything in §4, nor as flipping any flag authored under §5. The PR body will say so prominently, because
the convention is that merge ratifies by default and the exception must be loud, not silent.

## §6 · Verification for every item

`pytest tests/valoria` (baseline at audit time: **1637 passed, 23 skipped, 14 xfailed, 1 xpassed**),
plus the lane validator, plus the item's own named falsifier. Commit format `[scope] description` citing
`ED-IN-0148`. Lane handoffs updated. No item is reported done on a check that was not run.
