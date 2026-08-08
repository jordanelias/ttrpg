# Adversarial review of the world-churn audit — verdicts

## Status: RECORD (read-only critics; both structurally read-only — `Read`/`Grep`/`Glob` only, no write tooling)
## Date: 2026-08-08 · Lane: IN · ED-IN-0148

Two independent critics attacked `00_findings.md` and `01_plan.md` as an agonist→antagonist relay
(CLAUDE.md §10): each received the producer's **output only**, never its reasoning, and ran as
`valoria-critic`, whose read-only posture is enforced by tooling rather than by a sentence in a prompt.
Critic 1 took factual fidelity (92 tool calls); critic 2 took plan logic (58).

**This file exists because the corrections are the point, not an embarrassment.** Both source documents
were edited in place; `git diff` is the record.

---

## §1 · What was OVERTURNED

**1. §1's autonomous-drift inventory contradicted D5 of the same document.**
The findings listed *"NPE stance drift every season (`accounting.py:138`)"* as live autonomous churn.
`simulate_npc_actions` iterates `world.npcs` (`npe.py:338-339`) — the store D5 proves stays **empty** in
every live campaign (strict xfail, `test_pipeline_reach.py:596-599`). The call happens every season; the
drift never does. **The document credited churn its own defect register proved impossible** — pattern-
matching on a call site instead of the concept, which is the specific error this corpus says has cost it
the most rework. *Corrected in §1.*

**2. "Both live `stat_deltas=` sites are faction-facing" — false.** One is **settlement**-facing
(`echo_transport.py:319-320`, `actor_id=sid`, `scale_signature=["settlement"]`). The headline is
untouched: neither is person-facing. *Corrected in D5.*

**3. T1-1 was scheduled as unblocked; it is blocked.** No canon maps `size_pct` → `Mil`. The only
battle→Mil canon sits inside a block flagged **"[FACTION-P2-02 — proposed, EDITORIAL]"**
(`mass_battle_v30.md:678-690`). A proportional coefficient would be a fabricated constant — and this very
function's history shows the fabrication gate catching a mere *rounding* constant. **New J-I filed.**

**4. T1-2 was unimplementable as written.** "At Accord 0" cannot fire: `Territory.accord` is continuous
0.5–7.0 and its only mutator **floors at 0.5**. A naive `== 0` check would be **inert forever** — the same
defect class the audit is about. The existing primitive `canon_buckets.canonical_accord` (`< 1.75`) was
never named, despite the plan's own §0 demanding exactly that. The plan also implemented Step 4c.2 only,
silently dropping 4c.1 and the garrison contest, and contradicted itself on whether J-B blocks formation.

**5. T0-3's guard would have been vacuous.** `_CELL_OWNED` is field-parameterized **but hard-scoped to the
MB engine** (`root = Path(_SIM)/'mass_battle'`). Registering `npc_drift_state` would have scanned six
mass-battle files that can never contain the string: **a guard that passes because it cannot look** — the
precise class the module itself documents. Its shape is also wrong (writer-bypasses-owner vs
reader-cannot-see-world). Replaced with a behavioural falsifier. Lane corrected WR → **SE**.

**6. T0-1 is not Tier-0-safe.** It **breaks a currently-green test**
(`engine/tests/test_knots_ed912.py:103-109` asserts `conviction_scar == 1` through the no-op path); the
plan's verification list **never named `engine/tests/`**; a **second silencing layer** exists
(`knots.py:353-354` catches `ImportError, AttributeError`), so "fix the gate, not the call site" was
incomplete; and repairing it forces a conviction-name choice adjacent to **J-C**.

---

## §2 · What was SHARPENED (worse than claimed)

**"10 of 13 subscriptions have no producer" → 11 of 13, and 13 of 13 at default-flag runtime.** Only two
of the thirteen subscribed types have any code emitter, and `scene.combat_felled` has **no Python emit
site anywhere**. The critic could construct no criterion yielding 10. **Operational consequence:** T0-4's
instrument must reproduce **11/13**, or the error is frozen into the baseline it pins.

---

## §3 · What was SOFTENED

**D8's "zero top-down emitters have code" was too absolute.** `da.public_governance`
(`parliamentary_transfer.py:162-176`) is a live emitter in the `domain_actions` family, fired via
`parliamentary_bridge.py:173`. It is log-only, names a territory rather than sub-scale actors, and meets
none of the row's `targets[]`/`impact_vector` spec — so **"no genuinely top-down delivery ever fires"
stands**. But remediation should extend it rather than start from nothing.

**D1's "no code path anywhere ever" was one site too absolute.** `restore_world` (`game_state.py:357`) can
re-materialize `owner=None` from a serialized world. Not a live-campaign churn path — but exactly where
T1-2's guard test should also look.

**T1-4's blocker was misdescribed.** J-F was filed as an open magnitude question; magnitude is **already
canon-ruled** (degree-keyed ±2/±1/−1 via §5.2) the moment you compose on `domain_echo`. The genuine
decision is **shape**: one echo block carries one stat, so moving `Sta` means dropping the scene's only
live `L` write or extending to two stats. Restated in §4.

---

## §4 · What was UPHELD

Critic 1 re-derived the load-bearing findings independently and upheld them: **D1** (no live path sets
`owner = None`; nothing mutates insurgency `L`; promotion never constructs a `Faction`), **D2** (no Turmoil
writer exists), **D3**, **D4** (single `adjust('Mil')` site, raise-only), **D5** core (no applier for
`impact_vector` anywhere), **D6** (fully — and worse-shaped), **D7**'s 55-type roster / 56 paper-graph
consumer entries / `DEFAULT_CASCADE_DEPTH_MAX = 0` / ~39-zero-traffic, **D9**, **D10**, **D11**, §3's
latent traps, §4's stale claims, and §5's ED-IN-0011 ratification read directly from the ledger.

Critic 1 also read an adjacent surface the producer never cited (`restoration_movement.py`) and confirmed
both entry points are stubwire no-ops — the one place canon would grow an insurgency.

Critic 2 upheld **T0-2**, **T1-3**, **T1-5**, and the Tier-2/Tier-3 spot-checks, verifying that **no
blocked-on claim rests on a decision already ruled**.

**Fabrication check passed:** no `PP-NNN` is used as evidence anywhere in the findings (PP numbers appear
only inside quoted code comments); no evacuated path is treated as live; asserted ED statuses were read
from disk.

---

## §5 · The critics' own weakest verdicts, carried forward

Recorded so the next reader does not inherit them as settled:

- Critic 1's "3 types emit live" uphold is **static reasoning about flag/caller reachability with no
  execution** — the same limitation the producer declared. Its D8 softening hinges on a `da.*` roster it
  did not enumerate.
- Critic 1's D1 uphold **shares grep's dynamic-access blind spot**. Its own recommendation: T0-4's
  instrument is the genuine fix.
- Critic 2's "no prior ruling exists for J-B/J-E/J-F" rests on **bounded negative ledger greps**, not an
  exhaustive read.
- Critic 2's T1-4 softening assumes Jordan does not intend to reopen §5.2's degree table.
- **Neither critic checked**: §5's landing-verdict specifics, §6's lens-attribution history, §7's
  canon-engine import claim, or D12's contest-kernel purity. Those remain **producer-only, unaudited —
  not clean.**

---

## §6 · Method note

The relay worked because independence was **structural, not declared**: the critics had no write tooling,
and neither saw the producer's reasoning. Both exceeded their stated tool budgets (92 and 58 against 60),
which is the correct trade when the alternative is a shallow verdict on a load-bearing claim.

The single most valuable output was not any individual overturn but the **self-contradiction in §1/D5**
— a defect no amount of re-reading by the producer was likely to surface, because the producer wrote both
sections and believed both.
