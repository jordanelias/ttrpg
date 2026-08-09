# World Churn — the interdependency plan

## Status: PROPOSED — nothing here is ratified by merging this audit PR. Tier 3 is HELD for Jordan.
## Date: 2026-08-08 · Lane: IN (cross-cutting) · ED-IN-0149 · Companions: `00_findings.md`, `02_adversarial_review.md`
## Revision: **v2 — rewritten after adversarial review.** The critic inverted the sequencing, falsified one
## "compose on an existing primitive" claim, found a missing blocker, and showed one item was not
## Tier-0-safe. Every change is attributed inline. `git diff` against v1 is the record.

---

## §0 · The strategy, and why it is this one

The audit's finding dictates the shape of the plan. The machinery is **built and disconnected**, not
missing and not scripted. So the plan is **not** "build a churn engine" — most of it exists. It is:

1. **Repair what is actively wrong** (a gate that silently no-ops, an unfalsifiable victory leg, a test
   that proves a property by assuming it, comments asserting properties the tree lacks).
2. **Connect the highest-leverage single edges** — where *one* edge lights up machinery already fully
   written and currently unreachable.
3. **Instrument the connectivity itself**, so re-disconnection becomes a test failure rather than the
   subject of the next audit.
4. **Force the decisions that are genuinely Jordan's**, rather than guessing defaults into the tree.

**Ordering principle: leverage per unit of new design.** An edge that makes existing, tested, unreachable
code live is worth more than a new subsystem, and risks less.

**Three disciplines bind every item** (CLAUDE.md §0.1):
- **Every item names its falsifier**, and that test ships in the same commit. An item without one does
  not land. *After review, two falsifiers were rejected as unable to observe the failure they exclude —
  see T0-3 and the note in §7.*
- **Behaviour-changing items land flag-gated OFF with byte-exact goldens**, following the repo's own MB
  precedent. Flipping a default is a separate, measured act.
- **No uncited constant enters the tree.** Flag-gating OFF does not license a fabricated number — the
  point that killed v1's sequencing (see T1-1).

---

## §1 · TIER 0 — repairs and instruments

### T0-4 · The connectivity instrument  ⭐ *recommended FIRST (was 4th in v1)*
**Defect:** D7/D8, and the audit's own weakest claims. "11 of 13 subscriptions have no producer", "~39 of
55 types have zero traffic", "no code sets `owner = None`" all rest on **grep with no guard** — the exact
blind spot §0.1 point 5 says a guard is required to make tolerable. The review proved the risk concretely:
**v1 printed 10 of 13 and the true figure is 11** — an error a guard would have caught and a baseline
would otherwise have frozen.
**Change:** one instrument computing, from the tree: per Key type {emitters, consumers}; per subscription,
whether a producer exists; per contract row, whether the declared edge is realized. Report-only first.
**Compose on — CORRECTED BY REVIEW:** `tools/build_execution_map.py` **already parses**
`references/key_graph.json` for producers/consumers per type (`:13,30,203`). v1 proposed a free-standing
tool, which would have made a **second parser of the same surface** — a §8 single-owner violation in a
plan whose own §0 forbids exactly that. **Extend that owner, or explicitly subsume it.**
**Falsifier:** mutation — remove a known emitter and the instrument must notice. It must independently
reproduce **11/13** (not 10/13) and the 3-live-emitter count.
**Lane:** IN.

### T0-5 · Retire the vacuous direction-#4 test  *(NEW — the review found this; v1 missed it)*
**Defect:** D8. `test_pipeline_reach.py:427-440` "proves" top-down Key delivery by **reusing a bottom-up
Key** — the test's own docstring admits it. That is a live §0.1-point-2 defect *inside the test suite*: an
assertion that cannot observe the failure it excludes, in the very suite the repo trusts as a shipping
gate.
**Change:** convert to an honest `xfail` naming what would actually demonstrate top-down delivery.
**Falsifier:** the xfail itself — it must flip to pass only when a genuine top-down emitter exists.
**Why it belongs in Tier 0:** roughly a one-line repair, and leaving it green means the suite is asserting
a capability the tree does not have.
**Lane:** IN.

### T0-2 · Retire the stale claims
**Defect:** §4. Five comments assert properties the tree lacks, most damagingly that scenes are
"side-effect-free on strategic stats by construction" (`scene_dispatch.py:417-418`, `mc_v18.py:138-140`).
**Change:** correct each to what the tree does, citing the proving test. Fix the `scene.accord_echo`
misattribution, the retired-tree test path (`echo_transport.py:22`), and `treaty.py:11-15`'s false claim
about `crown_initiative`.
**Falsifier:** **none, honestly.** This is text; a guard on prose phrasing would be theatre. Verification
is the cited tests already passing. *(Review verdict: sound — "better than a theatrical prose guard".)*
**Lane:** IN.

### T0-3 · Fix the `temperaments.py` reader signature  *(v1's guard claim was FALSE)*
**Defect:** §3. Writer stores into `world.npc_drift_state` (`:153,158`); reader cannot accept a `world`
argument at all (`:105,117`). A wired-tomorrow trap of the §0.1-point-1 class.
**CORRECTED BY REVIEW — v1's compose-on-primitive claim does not hold.** v1 proposed registering
`npc_drift_state` in `_CELL_OWNED` (`test_morale_write_sweep.py`). That registry is field-parameterized
**but hard-scoped to the MB engine** — it scans only `_ENGINE_FILES` under `root = Path(_SIM)/'mass_battle'`
(`:134-142,235`). Adding the key would scan six mass-battle files that can never contain the string:
**a guard that passes because it cannot look** — the precise vacuous class the module itself documents
(`:249-261`). The guard's *shape* is also wrong: it detects *writer-bypasses-owner*, and this hazard is
*reader-cannot-see-world*.
**Change:** fix the reader signature, and ship a **behavioural** falsifier —
`apply_strain_shock(..., world=w)` then `temperament_modifiers(...)` asserting the drift is visible. That
fails today. Copy the sweep *pattern* locally if useful; **do not claim one-key inheritance.**
**Lane:** **SE (settlements)** — v1 said WR. Corrected by review.

### T0-1 · Fix the conviction gate  *(NO LONGER CLASSED "SAFE" — review overturned that)*
**Defect:** D6. `apply_conviction_scar` returns `magnitude=0` for an unrecognised name while the caller
reports `conviction_scar=1`.
**What review established, and v1 got wrong:**
1. **The fix breaks a currently-green test.** `engine/tests/test_knots_ed912.py:103-109` asserts
   `conviction_scar == 1` *through this exact no-op path*. The test update is in scope.
2. **v1's verification list did not even name `engine/tests/`** — the sim-regression suite this change
   lands in. §6 is corrected.
3. **A second silencing layer exists**: `knots.py:353-354` catches `(ImportError, AttributeError)`, so a
   gate that raises is swallowed here anyway. "Fix the gate, not the call site" was **incomplete**.
4. **It forces a vocabulary decision.** Repairing loudly means choosing a *valid* conviction for the
   knot-break scar — adjacent to **J-C**. (`conviction.py:42-49` claims "canonical 13 per PP-684" while
   listing 9 — a *third* divergent count, and the PP is unverifiable.)
**Therefore:** T0-1 ships **only** the gate hardening + the test update + removal of the over-broad
`except`; the **conviction name choice routes to J-C** and the call site keeps its current name until
ruled, with a `TODO` citing J-C rather than a guess.
**Falsifier:** unknown name is no longer silently zeroed; reported scar equals applied magnitude.
**Lane:** WR, coordinating with J-C.

### T0-6 · File what the plan is not fixing  *(NEW — review: "§0.1 point 5 says file the rest")*
No code. Register, as tracked debt with citations: **D9** (`scene_ob_modifier`/`board_degree` dead
channel; `zoom_out` wound flags; ED-167's +0.15 Ob computed into a discarded dataclass) — which v1
**dropped entirely**; the **CI start-value drift** (code 30.0 vs `CI_STARTING=28` vs registry 28); and the
**D10 residue** (`resolve_mass_seizure` zero-caller, which qualifies Loop 2; inert `parliamentary_stay`).
**Lane:** IN.

---

## §2 · TIER 1 — the high-leverage edges (land flag-gated OFF)

### T1-5 · Season/accounting boundary Keys  ⭐ *recommended first of Tier 1 (was last in v1)*
**Change:** emit `mechanical.season_change` and `mechanical.accounting` — both registered
(`key_types.json:351,372`), both emitted by nothing, though the scheduler is attached and the boundary is
driven at `mc_v18.py:158-161`.
**Compose on:** the log-only emitter pattern at `faction_action.py:348-394` — **verified reusable by
review** (scheduler guard `:348-350`, no `apply=` `:394`; per-tick cap 64 ample).
**Honest correction:** "zero behaviour change" holds **only flag-OFF**. Flag-ON moves `key_log_hash` /
`keys_emitted` (`mc_v18.py:103-104`) in seeded goldens. Stated, per review.
**Falsifier:** a seeded-campaign test asserting both types appear with the expected cardinality.
**Status: genuinely unblocked.** **Lane:** IN.

### T1-2 · Revolt → `Territory.owner = None` (FORMATION half only)
**Defect:** D1 — the single highest-leverage edge in the audit.
**Three corrections from review, all material:**
1. **"At Accord 0" is unimplementable as v1 wrote it.** `Territory.accord` is continuous 0.5–7.0 and its
   only mutator **floors at 0.5** (`game_state.py:156-157`); nothing ever writes 0. **A naive `== 0` check
   is inert forever** — the same defect class the audit is about. Canon "Accord 0" means continuous
   `< 1.75` via the **existing primitive `engine/substrate/canon_buckets.canonical_accord`** (`:44`),
   which v1 failed to name despite §0 demanding exactly that.
2. **v1 silently simplified the cited canon.** It implemented Step 4c.**2** only, omitting 4c.**1**
   (Accord 1 + no garrison → Accord → 0, `peninsular_strain_v30.md:482`) — without which Revolt's
   precondition is essentially never produced — and omitting 4c.2's garrison-fights-Popular-Uprising
   contest (Military vs Ob 2). Both are in scope or the simplification is declared, not silent.
3. **v1 contradicted itself.** Its body said J-B blocks only *promotion* so "T1-2 delivers formation";
   its §5 then refused to start T1-2 at all. **Resolved in favour of the body:** the **formation** half
   needs neither J-B nor T1-3, *provided the Turmoil +1 line is severed and held for J-E*.
**Delivers:** formation. **Not** promotion (J-B).
**Falsifier:** `insurgencies_formed > 0` becomes reachable — today structurally 0. Review credits this as
a genuine falsifier that would catch a naive `== 0` implementation. Extend it to `restore_world`
(`game_state.py:357`), the one other path that can produce an unowned territory.
**Lane:** WR + FA.

### T1-1 · Battle → `Mil` attrition  *(v1 recommended this FIRST; review found it blocked)*
**Defect:** D4.
**Mechanism verified by review:** `attacker_size_pct`/`defender_size_pct` are returned and **in scope** at
the transfer block; `Faction.adjust` exists; **the cascade cap is not an obstacle** — a state-writing apply
cascades nothing.
**Routing corrected:** subscriptions fire **synchronously at emit** (`keys.py:576-577`), not at the
boundary, and the live loop never calls `drain_tick`. The primitive matching the intended timing is
**emit-site `apply=`** (OF-7) — which **reverses** `_emit_battle_concluded`'s documented "log-only"
contract (`faction_action.py:330-331,394`) and **must be moved outside the `except Exception: pass`
telemetry swallow** (`:395-399`), or a validation error silently drops attrition — this audit's own
condemned class.
**⚠ BLOCKED — new J-I.** **No canon maps `size_pct` → `Mil`.** The only battle→Mil canon is "Unit
destroyed: Military −1 (±2/season cap)" inside a block flagged **"[FACTION-P2-02 — proposed, EDITORIAL]"**
with "[EDITORIAL: confirm Military stat change…]" (`mass_battle_v30.md:678-690`). A proportional
coefficient would be a **fabricated constant** — and this very function's history shows the fabrication
gate flagging a mere *rounding* constant (`faction_action.py:379-385`). **v1's claim that T1-1 had no
blocking decision was false.**
**Falsifier:** a seeded test that a faction losing battles ends with lower `Mil`. **Lane:** FA + MB.

### T1-3 · Turmoil writer, de-vacuating the victory leg
Unchanged from v1; review verdict **sound (correctly blocked on J-E)**. A `turmoil_track.py` mirroring the
existing single-owner `ci_track`/`ms_track` pattern. **Falsifier:** a test asserting the `PS ≤ 6` leg *can*
be false. **Lane:** WR.

### T1-4 · Council → `Sta`
**Mechanism verified end-to-end by review** (`scene_dispatch.py:342-343` → `domain_echo.py:110,121`
pass-through → `echo_transport.py:435-436` guard `_stat in MULTS`, which contains `Sta`).
**Two corrections:** "arbitrary stat name" **overstates** — the vocabulary is `{L, Sta, W, I, Mil}`. And
**J-F is half-ruled already**: magnitude is degree-keyed by §5.2 (±2/±1/−1) the moment you compose on
`domain_echo`, so *"by how much"* is not open. **The real blocker is shape:** one echo block carries **one**
stat (`echo_transport.py:384-395`), so moving `Sta` means either dropping the scene's only live `L` write
or extending the shape to two stats — which is **not** "a mapping row, not new machinery", as v1 claimed.
J-F is restated accordingly. **Lane:** SC/FA.

---

## §3 · TIER 2 — substrate maturation (sequenced after Tier 1, mostly gated)

- **T2-1 · ORD-3/ORD-4 + the `canonical_key_log` serialization spec.** Blocks the substrate's own observer
  steps; `propagation_spec_v1.md:393` names it as its own precondition; everything forecast-shaped is
  downstream. Cheapest unblock with the widest reach.
- **T2-2 · Key → person applier.** Both ends exist; `ACCOUNTING_BOUNDARY` is already a defined phase.
  **Hard-gated on J-C** — building first is shape divergence by construction.
- **T2-3 · Layer-A forecast only.** Ratified; analytic inputs are live code. Layer B stays gated.
- **T2-4 · `process_treaty_expirations` on the arc boundary.** Hook and function verified to exist. Needs
  a formation path to be non-trivial — file rather than force. *(Review: "file rather than force is right".)*

**Explicitly NOT proposed:** the R-F1/R-HB/R-CL/R-AI/R-RL conformance checkers. A conformance rule with no
kernel to check is a display string.

---

## §4 · TIER 3 — decisions that are Jordan's (held, not guessed)

| Id | Decision | Why it cannot be defaulted | Blocks |
|---|---|---|---|
| **J-A** | **The L0 identity fork** — a RATIFIED design whose calibration corpus was evacuated vs an UNRATIFIED proposal (`settlement_generator_v1.md:127`) now occupying the slot. | Leaving both true is scripting-drift-by-neglect. | M2 S1 + downstream |
| **J-B** | Insurgency `L` growth rule. Verified absent: `insurgency_pipeline_v30.md:123` baseline 1.0, `:160` trigger ≥3, no growth rule anywhere, no ledger entry ruling it. | Inventing a rate is fabrication. | T1-2 *promotion* only |
| **J-C** | Conviction vocabulary — 4 substrate axes vs 9 names vs 8 NPE names (and a comment claiming 13). | Any person-facing Key edge built first is shape divergence by construction. | T2-2, T0-1's name choice |
| **J-D** | ED-1051 `engine_clock` — confirmed `"status": "open"`. | The temporal spine's home doc. | M1 season-close, M3 G0 |
| **J-E** | `Strain`/`Turmoil`/`PI` collapse — three live keys; §4 titled "Turmoil Counter" while every rule inside says "Strain". | Building a writer first cements the wrong key. | T1-3, T1-2's Turmoil line |
| **J-F** | **Council→`Sta`: stat *selection*, and whether one echo block may carry two stats.** *(Restated — magnitude is already canon-ruled.)* | A shape change, not a number. | T1-4 |
| **J-G** | `spec/churn_amendments.md` — RATIFIED, no longer resolves; `CURRENT.md:165` still cites the dead path. | Ratification status of a nonexistent doc is not mine to assert. | Provenance integrity |
| **J-H** | `valoria-arc-generator` reads two evacuated trees and would recreate a "do not recreate" tree. | A skill contract, and its future depends on J-A. | D11 |
| **J-I** | **NEW — confirm FACTION-P2-02's battle→`Mil` consequence, or rule a proportional model.** | No coefficient canon exists; the alternative is a fabricated constant. | **T1-1** |

---

## §5 · Revised sequencing and what to do in this session

**v1's sequencing was inverted and is corrected.** v1 recommended T1-1 first on the false premise that it
had no blocking decision, while blocking T1-2 harder than its own analysis supported.

**Genuinely unblocked, in order:** **T0-4** (instrument) → **T0-5, T0-2, T0-3, T0-6** → **T1-5** →
**T1-2 formation** (with the `canonical_accord` and Step-4c.1 repairs).
**T0-1** is unblocked *for the gate hardening*; its name choice waits on J-C.
**T1-1** waits on one cheap confirm (J-I). **T1-3/T1-4**, all of Tier 2, all of Tier 3: not started.

**Loudly held, per the ED-1094 exception rule:** merging the audit PR ratifies **nothing** in §4, and
flips no flag authored under Tier 1.

## §6 · Verification for every item

`pytest tests/valoria` **and `engine/tests/`** — the latter added after review caught that T0-1 lands in
the sim-regression suite v1 never named — plus the lane validator, plus the item's own falsifier. Baseline
at audit time, verified before and after the audit commit: **1637 passed, 23 skipped, 14 xfailed,
1 xpassed**. Commit `[scope]` citing `ED-IN-0149`. No item reported done on a check that was not run.

## §7 · What the adversarial pass changed

Recorded because a plan that hides its corrections is not evidence. Review **overturned or materially
altered 6 of 11 items**: T0-1 lost its "safe" classification and gained a broken-test dependency; T0-3's
compose-on-primitive claim was false and its guard would have been vacuous; T0-4 would have created a
second parser; T1-1 was unblocked-by-assertion and is actually blocked (new J-I); T1-2 was unimplementable
as written and silently simplified its canon; T1-4's blocker was misdescribed as a magnitude question when
it is a shape question. Four items were confirmed sound (T0-2, T1-3, T1-5, Tier-2/3 spot-checks), and the
review contributed two items v1 missed entirely (T0-5, T0-6).

**The critic's own weakest verdicts, carried forward:** its "no prior ruling exists for J-B/J-E/J-F"
rests on bounded negative ledger greps, and its T1-4 softening assumes Jordan does not intend to reopen
§5.2's degree table.
