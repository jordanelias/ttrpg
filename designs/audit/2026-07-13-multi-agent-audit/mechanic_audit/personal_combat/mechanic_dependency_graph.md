# Mode C — Interaction Chain Analysis: Personal Combat

**Target:** `designs/scene/combat_engine_v1/`. `combat_throughlines_v1.md` already documents the
upstream/downstream map for the 8 co-primordial throughlines at a design level — this mode
cross-checks that map against the live code and adds the wound/initiative feedback loops it doesn't
cover in formula terms.

| Mechanic | Upstream | Downstream | Chain length | Flags |
|---|---|---|---|---|
| `reach_base` (measure/reach throughline) | weapon geometry (`head_len`,`grip_len`,2H flag) via `REACH_GEOM_SCALE` | `net_sigma` (reach term), the approach/close/reopen loop, stop-hit gate | 2 | None — single clean derivation, no categorical fallback since Phase-3b retired `HEAD_REACH`/`LONG`. |
| `recoverability_factor` (commitment=recovery axis) | weapon morphology (`mass×pob_frac`), footwork (lunge/choke grip), `commit` depth | `overcommit_exposure`, `RECOVERY_TEMPO_K`-scaled tempo debt | 2 | None — `combat_throughlines_v1.md` names this the "master coupling" and the formula (`config.py:74-104`) matches the doc's description exactly (mace loses ~5pp per its own worked example). |
| `initiative` (Vor/Nach) | `INIT_GAIN_HIT`, `INIT_LOSS_WOUNDED`, `INIT_STEAL_INDES`, `INIT_LOSS_OVERCOMMIT` | `net_sigma` via `INIT_SIGMA_K*tanh(rel_initiative/INIT_SCALE)` | 2, but **cyclic across beats** (a hit → higher initiative → improves the odds of the *next* hit) | **Amplification loop — already bounded by design.** `config.py:116-123`'s own comment states this is a "positive-feedback state" requiring "SAFEGUARDS: per-beat DECAY... + a hard CAP" and cites the NERS audit as the source of that requirement. `INIT_DECAY=0.75` (damper) and `INIT_CAP=1.5` (hard bound) are both present and match the description. **No new finding** — this is a textbook Mode-C amplification loop that the design has already identified and mitigated; confirms the mitigation is actually wired, not just described. |
| Wound → Ob (bilateral) | `damage()` → `WoundTracker.apply()` increments `.wounds` | `WOUND_ATK_OB`/`WOUND_DEF_OB` feed back into `net_sigma` for *future* exchanges (`systems.py:725,754,866`) | 2, cyclic across bouts (more wounds → harder to land the next hit / harder to defend) | **Escalating-difficulty loop — intentional, matches core principle #6** (see `core_principles_audit.md`). Capped: wound counter itself caps at `MaxWounds+1` (`combatant.py:72-73`), so the Ob penalty cannot escalate unboundedly even across a long fight. |
| `seize` lever | `vorschlag` (German)/`sen_no_sen` (Japanese) ability definitions in the tradition menu | **nothing** — its pre-contact-seizure consumer was cut 2026-06-05 (`wrapper.py:39`, `ability_armature.md §2c`'s correction note) | 1, **dead end** | **Flag — dead-end / orphaned mechanic.** `seize` is computed (or at least nominally equipped) but has no live consumer. This is exactly the Mode-C "dead-end mechanic" pattern; the corpus is aware of it (`combat_balancing_methodology.md §6` calls it "the proven-inert `seize` precedent") but `ability_armature.md §7` still describes it as "live" with "a positive, bounded edge" — see the gap register for the doc-currency angle of the same finding. |
| `reopen`/`disengage` | (none — not yet built) | (would feed Separation/Bind exit and the Italian "refuse the bind" identity per `tradition_decomposition_v1.md`) | 0 | **Unconnected system.** Referenced from three docs (`ability_armature.md §2c/§7`, `REARCHITECTURE_v1.md` worklist, `tradition_decomposition_v1.md`) as a named lever/access with no implementation — an upstream design intent with no downstream engine consumer at all. See gap register. |
| Contact axis (`grab_available`/`grab_sigma`/`grab_outcome`, I7b/D8-D9) | `opening_created` flag, set at 3 precondition sites in `wrapper.engagement` (bind entry, beaten-aside/slip-inside, deep-commit reopen) + the dagger/unarmed short-reach exemption | `contact_outcome` branches (disarm/throw/pin/foot_pin/control/escape), each with its own effect applied in `wrapper.py:316-323` | 2 | **Verified connected, not a gap** despite `state_graph.py:42`'s "BUILT, not activated (M-11)" comment and `tradition_decomposition_v1.md`'s stale claim that clinch is "currently unbuilt" — traced the call chain in `wrapper.py:227-323` and confirmed `CT.grab_available`/`grab_outcome` are live-called with all three precondition sites wired. The "not activated" language in `state_graph.py` reads as a coverage-sweep note (had the transition fired in a *particular* trace, at the time M-11 was written), not a description of dead code. **No action.** |
| Tradition channel levers (`measure`/`tempo`/`leverage`/`visual`/`tactile`/`precommit`/`balance`) | `eff_cw()` channel-weight lookups | ~9 live call sites per `ability_armature.md §2c`'s status-correction note | 2 | Reachable and wired per the doc's own correction — but the row-level table immediately below the correction still marks these "pending (channel)", an internal-contradiction the correction explicitly warns readers about but never resolves in the table itself. Doc-currency finding, filed in gap register (not a code-level dead end). |

## Circular dependencies (in the disallowed sense — A→B→A within one resolution, not a beat-over-beat feedback loop)

None found. The two cyclic patterns present (initiative and wound-Ob) are both **cross-beat**
feedback, explicitly damped/capped, and match the design's own stated intent — not the same-beat
circular dependency this check is meant to catch.

## Verification pass — engine's own dead-end tooling re-run

`state_graph.py` ships its own dynamic-coverage dead-branch scan (`python state_graph.py`, run this
pass with numpy installed locally). Re-running it independently confirms the state graph itself is
fully connected (edge closure, terminal reachability, entry coverage, emit legality all **PASS**), but
its dead-branch check flags two of `wrapper.engagement`'s four `return None` separation sites
(`'beat_exhaustion'`, `'collapse'`) as unreached across a 4-matchup/30-seed sweep — a *third*, engine-
tool-detected dead-end candidate distinct from `seize` and `reopen`/`disengage` above. Filed as
GAP-PC-8 (P3) in the gap register, since the tool's own printed guidance already tells a future session
what to do with it (widen the trigger, demote to a documented guard, or delete) — this audit adds
nothing beyond confirming the flag still fires on the current working tree.

## Summary

- 1 confirmed dead-end mechanic (`seize`) — P2, filed in gap register.
- 1 confirmed unconnected system (`reopen`/`disengage`) — P2, filed in gap register.
- 1 tool-flagged dead-end candidate (`state_graph.py`'s own separation-reason coverage scan:
  `beat_exhaustion`/`collapse` never fire in a 30-seed sweep) — P3, filed in gap register (GAP-PC-8),
  re-verified by independently re-running the engine's own self-test rather than trusting the doc claim.
- 1 apparent dead-end (contact/clinch axis) investigated and **ruled a false positive** — the mechanic
  is live-wired; the "unbuilt"/"not activated" language in two docs is stale relative to `contact.py`
  (added 2026-07-02) and should be corrected but does not represent a code-level gap.
- 2 amplification-loop candidates (initiative, wound-Ob) investigated and confirmed **already
  mitigated by design** (decay+cap; wound-count cap) — no new finding.
