# Combinatorial / isolation audit + all-node state-graph interrogation — personal combat

**Status: RATIFIED (audit conclusions + the two fixes below; ED-PC-0025, 2026-07-23).**
Scope of ratification: the *No-dead-wires* verdict, the single-source overflow-safe `core.logistic()`, and
the `INJECTION_POINTS` doctrine cleanup. Items marked **DEFERRED** below are surfaced, not ratified.

Directive (Jordan): *"do a systematic isolation/combinatorial audit … what is wired and what is not wired
gets tested as individuals and in combinations … group things by state graph … this may be the biggest use
of vectorized critique: how each lever interacts with other levers."* Plus an all-directions pipeline trace
with interrogation of each state-graph node.

## Method
- **Isolation sweep** (`harness.py`): each lever/channel toggled alone, win-rate delta vs baseline over seeded fights.
- **Interaction matrix** (`interaction.py`): pairwise lever combinations vs the linear-expected sum (synergy/antagonism/independence), grouped by state-graph node.
- **Pipeline trace**: node firing rates over 240 fights / 6 matchups.
- **Two adversarial critics** (read-only, sonnet, refute-by-default): dead-wire forensics; interaction degeneracy.

## Isolation results (grouped by state-graph node)
| Class | Levers | Aggregate win-rate effect |
|---|---|---|
| **WIRED-LIVE** (decisive) | skill(bind) +33pp, agility +40pp, skill(dodge) +31pp, skill(parry) +25pp, strength +24pp | large, as intended |
| **WIRED-SITUATIONAL** | the U3/U5/U7 morphology levers (edge_read, spine_press, edge_grab, choke, facing_regime) | ~0 aggregate — they fire **per-event**, not per-win (the U9 texture instrument) |
| **Contact axis** | grab_available / grab_outcome | **decisive** for short weapons — disabling it flips 35% of dagger fights; only the 3 tuning knobs (skill(grab)/ringen/GRAB_EDGE_K) are aggregate-neutral |

## Interaction matrix (node-grouped)
- Morphology levers are **independent** of each other (near-linear sums) and individually near-inert in aggregate — consistent with situational-per-event design.
- Strong channels (skill/attr) are **sub-additive** — healthy saturation toward the hard 95% ceiling (`UPSET_FLOOR=0.05`, unbreakable), not degeneracy.
- One genuine **synergy**: aggression × bind-skill (+30.6 vs +20.9 expected) — grounded (`disp_lean` deepens commit; bind-skill raises both wind-selection frequency and per-bind odds — different stages of one causal chain). Self-limiting at the ceiling.

## Pipeline trace — per-node firing rates
FightInit/EngagementInit 100% · Approach 67% · AwaitTempo/Exchange 99% · Bind 30% · Riposte 59% · HitLanded 87% · Contact 80% · Felled 99% · Separation 88% · Unresolved 1% · FinalResult 100%.
Separation reasons observed: clean_defence, burst_ceiling. **collapse** and **beat_exhaustion** never fire (pre-existing dead-branch flag, HANDOFF_PC.md — not introduced here).

## Critic verdicts — **NO DEAD WIRES**
Both critics, independently, found no lever reaching no consumer.
- **Dead-wire forensics:** FACING_REGIME (near-invisible *by design* — 58% fire at absurd K=50 proves the chain is alive), CHOKE (situational; poleaxe a poor exemplar, 12× smaller than spear-class), indes/mezzo_tempo (real `read_win ∧ commit≥4` gate ~0.5–1% of beats). All correctly wired. Contact axis is decisive; only its knobs are aggregate-neutral.
- **Interaction degeneracy:** the ability clamp (ED-PC-0024) holds (deep investment bounded, no crash). Mirror fairness holds under every stress. Surfaced a **residual overflow** (below). Flags a **no-tradition-gate on `equipped`** build-legality gap.

## Frequency-gating (key mechanism, interaction critic)
The morphology levers are not dead — they are **frequency-gated by their enabling skill**: `mode_sigma`'s wind branch adds `defender.skill('bind')` directly, so a fighter with no bind skill rarely enters a bind, so the spine lever has nothing to amplify. Deep + paired investment (bind skill **and** shinogi level 8) = +13pp vs an equal opponent. Emergent and correct — the ~0 aggregate at default is because default builds don't invest in the enabling skill.

## FIXED here (ratified)
1. **Overflow-safety — single-source `core.logistic()` (ED-PC-0025).** The `1/(1+e^-x)` squash was open-coded 5 ways (`bind_dominance_p`, `disrupt_resist_p`, two read-contest sites, `grab_outcome`) — a §8 "every rule lives once" violation and an overflow hazard: a grossly out-of-contract net-sigma (attribute/skill ≫ the legal ceiling of 5) drove `exp()` past the float range and crashed resolution (`strength/skills=50000 → 99/300 fights crash`). Measured legal-build `|argument|` never exceeds ~2.4, so the clamp at ±500 is **byte-identical for every legal build** and guards pathology only. Result: **99/300 → 0/300**.
2. **Imposition-doctrine residual (ED-PC-0023 follow-through).** `state_graph.INJECTION_POINTS` still described the retired imposition mechanism ("German IMPOSE the bind", "Spanish impose re-opening", "Ringen imposes the grab"). Rewritten to the emergent model — a tradition grants *access* to invested abilities that modulate a lever; it does not impose a branch.

## DEFERRED (surfaced, not ratified — awaiting Jordan)
- **Mode-exposure / undefended-time model (`T_vuln`).** `select_mode` chooses purely by damage-coupling and is exposure-blind; the exposure that *is* modeled (`overcommit_exposure` via `recoverability_factor`) reads whole-weapon pc, not the selected mode's `sel_pc`. So the swing-vs-thrust exposure-to-counterattack asymmetry is not modeled at the mode level — a heavy poll-swing's long undefended window never counts against it, which is partly why the poleaxe hammer out-selects its own spike vs plate. Proposed emergent fix: a vulnerability-window `T_vuln` (delivery + recovery + measure, blended by point_concentration) driving the counter/exposure path and feeding mode selection. Design only; not built.
- **Historical-grounding corrections (adversarial HEMA critic).** `guardia`→facing_regime (WRONG — "guardia stretta" names a close-*measure* guard, not body-*facing*), `atajo`→measure (WRONG — a line-occupation/*leverage* action), `zwerchhau`→edge_read (WRONG-leaning — real function is tempo-interception, not false-edge unreadability), `phi_grip` `[ASSERTED — first principles]` tag overclaims (transmission is grip-invariant but human-generated *force* isn't), stale `combat_systems.py:766` "German Winden" comment (should be shinogi). Not applied.
- **No-tradition-gate on `equipped`** — a fighter can equip every tradition's kit at once. Build-legality gap.
- **The 9 pre-existing intentional-red failures** (element-parity goldens; sabre pure-cutter / ED-PC-0012; poleaxe spike; spear heft / ED-PC-0010) — diagnosed, resolution path per cluster identified, not executed.
