# Valoria Systems Integration Master — Part 4: Cross-Category Comparison and Integration Proposals

## Status: PROPOSED (2026-08-28)
## Version: v1.0
## Reads: Parts 1–3 (collation · slices · flatten · within-system analysis)

**Reading order:** [Part 1 · Collation and Slices](valoria_systems_integration_master_v1.md) → [Part 2 · Flatten, the Personal Half](valoria_systems_integration_master_v1_part2.md) → [Part 3 · Within-System Analysis](valoria_systems_integration_master_v1_part3.md) → [Part 4 · Cross-Category Comparison and Proposals](valoria_systems_integration_master_v1_part4.md)


Deliverables §5 and §6. §5 compares across the twelve systems for synergies, commonalities and
shared blockers. §6 puts four rival integration proposals against each other, each with an
ED-IN-0027 disposition table judged **as-if-built**, and each attacked against NERS.

---

## §5 CROSS-CATEGORY COMPARISON

### 5.0 The measured distribution

The flatten catalogued **338 classified things** across ten systems. Their status distribution is
the single most useful number in this document:

| status | count | share |
|---|---:|---:|
| BUILT — a production path reaches it in a seeded campaign | 109 | 32% |
| DESIGNED — canon, no code | 100 | 30% |
| PROPOSED — research/audit, not canon | 51 | 15% |
| **INERT — the code exists, is correct, and nothing calls it** | **43** | **13%** |
| RULED-UNEXECUTED — Jordan decided, the code does not reflect it | 21 | 6% |
| BUILT with a stated defect, or built and unreachable | 14 | 4% |

The last row is a mixed bucket, so the fold has to be stated exactly rather than gestured at. Of
its 14 items, **6 are BUILT-with-a-defect** (they run, they are simply wrong) and **8 are inert in
substance** — 4 built-but-unreachable, 2 no-ops, 2 dormant. Adding those 8 to the 43 gives
**51 things, 15% of everything catalogued: finished machinery with no hand on the key.** That is
the same size as the entire PROPOSED corpus and roughly half the size of everything that runs.

**This is the finding the whole exercise converges on.** Valoria's problem is not that it is
underdesigned — 30% of the corpus is ratified canon. It is not that the code is wrong — almost
none of the inert code is defective; `succeed_governor` sweeps expired ledger tags and lets durable
ones survive a handover, which is the subtle thing done right. The problem is that the parts are
not connected to each other.

### 5.1 Ten findings across systems

---

#### F1 — Every lane's cheapest fix is a *writer*, not a mechanic. Eight out of eight.

Eight lanes were asked, independently and without seeing each other's answers, for the cheapest
change that would make their system playable. The answers:

| system | cheapest change | shape |
|---|---|---|
| economy-accounting | one line of seasonal Wealth income in `run_accounting` | writer |
| faction-strategy | a `grudge` dict + four one-line writes at sites that already fire | writer |
| parliament-politics | give the motion a subject in `_derive_vote` | writer |
| settlement-governance | `tick_settlements(world)` — composed almost entirely of existing functions | **caller** |
| territory-world | give `InsurgencyRecord.L` a writer | writer |
| People | load the 46 authored characters into `world.npcs` | **loader** |
| cross-scale-plumbing | set `echo['scene_outcome']` on the contest branch — one field | writer |
| mass-battle-seam | pass a commander's Charisma and Cognition through `_faction_to_unit` | writer |

Not one asked for a new mechanic. Not one asked for a design ruling. Eight lanes reading eight
different parts of the tree all found the same shape of hole: **a value that is computed correctly
and never stored, or stored correctly and never read.**

**The adversarial check on this finding, because a unanimous result is exactly what to distrust.**
Is this a real property of the tree, or an artifact of the brief asking each lane to name something
*cheap*? The falsifier came from the People lane, which actually ran the experiment rather than
reasoning about it: loading two NPCs into `world.npcs` **moved the seed-42 campaign winner from
Crown to Hafenmark**, because `simulate_npc_actions` draws `world.rng` once per qualifying pair per
season and re-phases every downstream consumer. Neutering the drift function reproduced the baseline
byte-exact, isolating the cause. So the honest version of F1 is: **seven of eight are writers; one is
a writer plus a determinism precondition.** The finding survives, narrowed, and the narrowing is
itself the most useful thing in it — see F10.

---

#### F2 — The absent person is the highest-fan-out blocker in the tree.

Six of ten systems name `personnel-roster` as their blocking dependency, and it is empty. In every
seeded campaign, `world.npcs` is an empty dictionary: **the population of Valoria is zero.**

| system | what it needs a person for | what is blocked |
|---|---|---|
| settlement-governance | `governor_id`, `npc_ids` | succession, recall, Residencia, the entire Positional pressure vector |
| parliament-politics | seat-holders | 74 authored ladder rungs, seat tenure, recognition forks |
| faction-strategy | a leader field | the Universal Succession Contest — unreachable *by construction* |
| mass-battle-seam | a commander with Charisma and Cognition | `derive_command`, whose flag already defaults ON and falls back to a hardcoded 4 |
| cross-scale-plumbing | a named leader or office-holder | six of the seven Sufficient Scope conditions |
| territory-world | officers at each tier | the ruled governance-type cascade |

The circularity is exact and worth naming: **nothing appoints a governor because there is nobody to
appoint, and nobody is generated because no mechanic needs one.** `generate_npc` is a complete
two-tier generator — it reads territory ecology, biases 60% toward the controlling faction, then
rolls a d6 and flips one axis so populations are not uniform — and it has no call site. `mc_v18`
fires a named `stub_resolve` in its place.

Meanwhile 46 characters are authored in `references/npc_registry.yaml`, under an enforcement line
forbidding a name in any design doc without an entry, and **the file has zero runtime loaders.**
Deleting it would change nothing the engine does.

---

#### F3 — The absent memory is the second blocker, and the primitive for it is already built and inert.

Every lane independently wants durable relational memory, and none has it:

- **faction-strategy** — `parliamentary_action.py:68-69` says it in its own comment: *"No grudge /
  hostility / inter-faction-relationship stat exists in game_state.Faction."* Target selection
  recomputes "whoever has the highest Legitimacy" from scratch every season.
- **parliament-politics** — no motion history, so the same contentless motion fires every season.
- **npc-social** — `NPC.persistent_state` is declared, defaulted, serialised and **never assigned**;
  `npc_memory`'s contract declares `state: []` and `emits: []`, so there is nowhere to write one.
- **cross-scale-plumbing** — across fifteen traced subsystem flow skeletons, Key-typed *inputs* were
  **7 of 165**, and six of those seven were substrate self-construction or a callback receiving its
  own emission. Keys flow out and essentially never in.
- **settlement-governance** — has a ledger with five tag families, dedupe by `(kind, key)`, TTL
  sweep, and succession survival. **Zero production writers.**

**The synergy is exact.** `systems/settlements/sim/ledger.py:30` declares
`TAG_KINDS = {"Precedent", "Grudge", "Debt", "Reputation", "Leverage"}`. A faction grudge and a
settlement Grudge tag are *the same primitive at two scales*. Parliament's missing motion history is
a `Precedent` tag. NPC memory is a tag with a salience value. Four systems are each asking for a
bespoke version of one built, correct, inert module.

⚠ **The enum is closed at five, and a Compact is not a sixth.** ED-IN-0046 D3 ruled 2026-07-13 that
a recurring term-limited claim is a `Debt` subtype — `Debt(key="compact:<quota>", ttl=term,
recurs=True)` — with `Leverage` remaining the built fifth family
(`registers/supersession_register.yaml:406-418`). Four fiscal proposals — Encabezamiento, Salt
Certificate, State Arsenal, Borrow — were adjudicated before that ruling reached the prose, one rated
"ratify as-is". **They are unjudged against the `Debt` form and may not be authored until re-judged.**

---

#### F4 — Every homeostatic loop in the game is open at one end, or has no damper.

This is a *systemic* property, not a list of bugs, and it is the finding with the most direct
bearing on whether the game is balanceable at all.

| loop | defect | direction |
|---|---|---|
| `Faction.standing` | a bare unbounded int mutated at eleven sites, never through `adjust()`, so it escapes the registry clamps — and it feeds two dice pools whose outcomes write it back | **positive, undamped** |
| Settlement pressure Π | the restoring term saturates at ±1, so any accrual above 1.00/season pins the ceiling; six ambition clocks supply up to +3.0 before a single unserved need | **positive, arithmetically unrecoverable** |
| `Faction.W` (Wealth) | four write sites in the whole engine, **all costs, no income anywhere** | **monotone decreasing, no source** |
| Turmoil / IP / PI / Strain | initialised at world-gen, never written again — four pressure gauges, all painted on | **open at both ends** |
| `InsurgencyRecord.L` | assigned 1.0 at formation, never written; promotion needs ≥3 | **exit welded shut** |
| Parliament's Total Victory rider | flagged in its own comment as a one-season penalty; `season_manager` defines only `advance_season`/`SEASONS_PER_ARC` and has no temporary-modifier facility, so it is permanent and compounds | **sign depends on the branch — see below** |

The last row is the sharpest, and it needs stating more carefully than it usually is.
`parliamentary_vote.py:207-219` docks **the losing coalition's highest-Legitimacy member**, not
"whoever is currently leading" — and which faction that is depends on the branch. On the
`track ≥ TOTAL_VICTORY` branch the loser is side B, which `parliamentary_bridge.py:97-99` builds as
the `max(…, key=L)` establishment, so the penalty lands on the leader and acts as **negative**
feedback. On the `track ≤ TOTAL_DEFEAT` branch the loser is side A, the *lowest-Stability*
proposer, so the penalty lands on the weakest faction and acts as **positive** feedback.

Which branch dominates over a campaign is an empirical question, and **this document does not
answer it.** The tempting reading — that the rider is the layer's anti-runaway damper — is a
campaign-level balance claim with no control, which is precisely what `CLAUDE.md` §0.1 point 4
forbids in either direction. It is also **measurable**: `tools/balance_oracle.py` exists, the change is
campaign-reachable so its two arms are not degenerate by construction, and 240 campaigns is about
thirteen minutes. Until that is run, treat the rider as *an uncontrolled asymmetry of unknown sign*,
not as the layer's load-bearing damper.

---

#### F5 — Seven live name collisions, each of which becomes a real defect the moment both halves are built.

| word | meaning A | meaning B | meaning C |
|---|---|---|---|
| **Standing** | `Faction.standing`, a bare int feeding Crown pools | the designed 0–7 officer rank ladder | the retired Counselor/Lieutenant/Successor titles `settlement_layer_v30 §3.2` still gates governor eligibility on |
| **Disposition** | the designed universal −5..+5 relationship scalar | `affiliation_loyalty`, 0–3, in the live `NPC` | `combat_engine_v1/config.py:273`, a 1–7 aggression temperament |
| **Officer** | mass battle's auto-generated unit commander + the `officer_deaths` key type | the political rank concept, in ~20 of 96 catalogued rise-to-power cases | — |
| **Territory** | the code's `T1`–`T17` | what the 2026-07-13 ruling calls a **Province**; the ruled Territory tier has no representation at all | — |
| **Mandate** | `Faction.L`, written directly as a base descriptor | LPS-1's *derived* aggregate over per-settlement Legitimacy and Popular Support | — |
| **Scale** | the runtime's four (`personal`, `settlement`, `territory`, `peninsula`) | the ruled Country > Duchy > Province > Territory > Settlement ladder | `scale_transitions_v30`'s Object/Personal/Relational/Territorial/Structural — five vocabularies, only "Personal" in all of them |
| **Sanction** | the live five-tier Parliamentary ladder | what `name_collision_database.yaml:421-425` prescribes renaming the Authority pressure point to | — |

The *Scale* row is not a naming cleanup. The honest reading is that two different concepts — **what
size of thing this event is about** and **what administrative tier owns it** — have been forced into
one field. That is why five rosters exist: each was right about a different question.

The consequence for sequencing: a naming pass is a **precondition** of the person primitive, not a
tidy-up after it. You cannot type a `role` field while "officer" means two things.

---

#### F6 — Three rival action economies at faction scale, two at settlement scale, and the only live budget primitive belongs to neither.

- **faction-strategy** carries three, none superseding another: `faction_action.py`'s single
  re-weighted `rng.random()` draw (the one that runs); `ci_political_v30 §5`'s typed 6-card hands
  with 1–2 season cooldowns; and the six-tier AI threat-priority posture stack. Neither document
  acknowledges the others.
- **settlement-governance** carries two, and they were **already ruled**: D1 makes the Π-weighted
  card deck canonical for player-facing play and demotes the 500-seed predicate sweep to a
  balance-regression oracle; D2 makes the AP economy canonical. Both rulings are unexecuted, so the
  fork keeps re-presenting itself to anyone reading the documents rather than the rulings.
- **parliament-politics** has no action economy at all — the vote is free and fires every season.

And the only live seasonal-budget primitive anywhere in the tree is
`AP = 2 + facility_tier + (1 at a Seat/Cathedral)` at `registry.py:92-97` — **which has zero
readers.** Every proposed action economy in the corpus wants a budget; one exists, is correct, is
computed, and nothing reads it. This is F1 and F6 landing on the same line of code.

---

#### F7 — The proposal corpus is roughly four ideas with ~150 instantiations.

Measured duplication: ~30 duplicate pairs between the governance compendium's
`40_roster_officer_system.md` and `research/rise_to_power_roster_system_research_v1.md`; ~10 more
between the two `research/governance/` lanes, merging on proposal id. Of the ~471 catalogued gaps,
roughly **117 are measurably duplicates in disguise** and the genuine strong-sense count is 150–190.

Underneath, the fiscal corpus reduces hard. Twenty-one deeply-researched mechanics — Ottoman
*iltizam*, Roman *publicani*, the Ferme Générale, John Law, the Salt Certificate, *Encabezamiento*,
debasement ratchets, environment-indexed levies, private guild embargoes — all want the same two
things: **a Wealth quantity that flows** (so extraction has something to modulate) and **a durable
claim tag** (so a bargain outlives the season it was struck in). Nine of ten independently reference
one tag family. Both of those are single primitives, already named in F3 and F4.

The same reduction holds for people. Shadow Renown (0–10), Deniability Debt (0–7), Renown (0–10),
Caste, Southernmost Awareness (0–7), Warden Cooperation (0–3), suspicion, `consolidation_progress`
(0–5) and Franchise (0–5) are **nine parallel bounded personal meters whose only structural
differences are their trigger lists.** As-if-built, a player watches nine bars.

---

#### F8 — The one working cross-scale crossing works *because* it needs no person, and that is diagnostic.

Eight scale handoffs are specified. **One pair — (Scene, Faction) — is production-reachable**, via a
dispatch dict with two entries that both map to it. Eight mandatory zoom-in triggers are specified;
**one — Stability Crisis — is evaluable.** It queues an emergency council whose two sides are derived
from *the same faction's own aggregates*: side A scores `round(Faction.L)`, side B scores
`round(7 − Faction.Sta)`, both run the identical default policy, and the echo returns to the faction
it came from.

So the single working personal↔strategic crossing in the game is **a faction arguing with itself**,
and it works precisely because it needs nobody in the room. Every crossing that requires a person is
dark. That is not a coincidence to note in passing; it is F2 expressed as an execution artifact.

Immediately adjacent: `scene.accord_echo` is **the one fully closed Key-driven state-write loop in
the engine** — scene resolves, Key emitted with an honest `causes[]` chain, `stat_deltas` collected
at emission and applied at the accounting boundary, `Settlement.order` written. It is finished,
tested and correct, and it has never fired.

⚠ **It is dormant on TWO missing declarations, not one, and the second is a design decision.**
`echo_transport.py:302-313` reads `echo_ctx["target_settlement"]`, and returns
`applied: False, reason: "no resolvable target_settlement in echo block"` when it is absent. The
contest branch's echo block at `scene_dispatch.py:344-345` carries exactly four keys —
`actor_faction`, `target_faction`, `most_relevant_stat`, `degree` — and no `target_settlement`.
Separately, `scene_outcome` must be a member of the closed §5.5 vocabulary `_ACCORD_SCENE_OUTCOMES`
and is validated before it is trusted (`echo_transport.py:145-181`); the module states at
`:133-142` that inferring the category from `scene_type` *"was itself a small fabrication of exactly
the kind CLAUDE.md §5/§7 warns against"* and belongs to the SC/PC-lane derivation bridge.

So closing this loop needs (a) a §5.5 outcome classification for a faction-internal Stability Crisis
and (b) a faction→settlement targeting rule. **Both are rulings, and the code is deliberately
refusing to guess either.** That is the correct posture and it is why this is not the free win it
first appears to be.

---

#### F9 — What is genuinely good, and must survive every proposal below.

A cut list is only credible next to a defend list.

- **The Key substrate.** Typed, validated, append-only; save state is initial conditions plus the
  log; the deferred-apply channel logs and cause-links at emission while the state write lands at the
  accounting boundary, so same-tick causal chaining survives. Better than most games this size have.
- **The resolution kernel.** One owner for the dice, one for the margin ladder, both guarded — and
  ED-IN-0196 closed the TN question by making non-conformance *impossible* (`_require_tn7` raises)
  rather than merely discouraged. That is the pattern every other single-owner claim in the tree
  should be held to.
- **`ledger.py`.** Dedupe by `(kind, key)`, TTL sweep, `Reputation` single-valued, durable tags
  surviving succession. Inert, and the best-shaped primitive in the corpus.
- **`derive_parties` returning `None` on a derivation gap** (`engine/cross_scale/combat_bridge.py:114-128`)
  rather than fabricating an actor — its docstring is explicit that flagging the gap is the caller's
  job, *"never this module inventing a substitute."* Preserve this through any repair of the bridge.
- **`populate_from_geography` raising on an illegal settlement type.** The in-tree pattern for a
  deterministic, no-RNG, fully-cited loader — and the template the NPC loader should copy.
- **The mass-battle engine** as ported 2026-08-24: troop types, equipment, formations, per-cell
  morale, Lanchester signatures, stamina, encirclement. The seam above it is one number wide; the
  engine below it is not the problem.

---

#### F10 — The binding constraint is not cost. It is attribution.

F1 says eight changes are individually cheap — call it 250 lines all told. The naive conclusion is
"do all eight", and there is a measured case where that goes wrong: a two-NPC load moves the seed-42
campaign winner, through a channel three separate population guards cannot see, because all three
observe `world.npc_counter` — which only `generate_npc` increments and a direct loader never touches.
The mechanism is inspectable: `npe.py:361` takes `world.rng` and `:385` draws `rng.randint(1, 6)`
inside a per-pair loop, and `simulate_npc_actions` is wired every season at `accounting.py:139`, so
adding people adds draws and re-phases every downstream consumer of the shared stream.

**That channel is narrow — it opens only for a change that adds or removes draws.** Steps 3, 7 and 8
below set a field, add an income term and fix a constant; none adds a draw, and their golden
movements are attributable by inspecting which field moved.

Ordering is required on a broader footing than that one channel: `CLAUDE.md` §0.1 point 4 requires a
stated control **per change**, whether or not RNG phase is in play. The seed-42 result shows what
skipping it costs.

Land all eight writers in one commit and you get **eight simultaneous golden movements and no way to
attribute any of them.** Under `CLAUDE.md` §0.1 point 4 — *a number without a control is not a
measurement* — that is not a fast path, it is an unmeasurable one.

So the real constraint on integration is **ordering**: each writer must land as a single-variable
experiment, with a stated control, in an order where earlier changes do not make later ones
unattributable. Determinism-neutral changes go first; state-writing changes go in increasing order
of blast radius. **That ordering is the actual deliverable of §6, and it is what separates the four
proposals below more than their content does.**

### 5.2 The synergy matrix

Where a fix in one system pays in another. Read a row as *"building this"*, a column as *"also
unblocks"*.

| build this ↓ | faction | parliament | settlement | territory | People | plumbing | economy | mass battle |
|---|---|---|---|---|---|---|---|---|
| **Person entity** | leader, succession | seat-holders | `governor_id`, recall | cascade officers | — | 6 of 7 Scope conditions | tax-farmer NPC | `derive_command` |
| **Generalised ledger** | grudge, memory | motion history | already its home | occupation record | NPC memory, edges | `causes[]` becomes biography | durable fiscal claims | — |
| **AP budget at every scale** | replaces the weighted draw | motions cost something | already its home | reach-cap | action budget per roster | — | prices every fiscal verb | — |
| **Wealth income** | conquest pays | — | compliance-scaled yield | holding pays | recruitment costs | — | **unblocks all 21 fiscal mechanics** | upkeep |
| **`scene_outcome` field** | — | — | `Settlement.order` moves | — | scenes have authors | **lights the one closed loop** | — | battle→scene |
| **Naming pass** | Standing ×2 | Sanction | Standing ×3 | Territory tier | Officer, Disposition ×3 | 5 scale vocabularies | — | Officer |

Three columns dominate. **Person** unblocks eight systems. **Ledger** unblocks seven. **Wealth
income** unblocks an entire proposal corpus by itself. Everything else is local.

---

## §6 INTEGRATION PROPOSALS

Four proposals. They are genuinely rival — different theories of what is wrong — and §6.5 says which
combination I would actually run and why.

**Method note on the disposition tables.** Verdicts use the ED-IN-0027 ladder — least to most
removed, `KEEP → REFINE → DISTILL → MERGE → PRUNE → CUT`, preferring the weakest verdict that
resolves the failure — and are judged **as-if-built**. Its cardinal rule, verbatim from
`references/throughlines_meta.md:209-214`:

> *"A never-built action whose realized contribution is load-bearing is **KEEP**; a fully-built
> action that would be dominant or redundant even when realized is **CUT**. **Any subtractive
> verdict citing build-state as a reason is invalid by construction.**"*

Nothing below is cut for being unbuilt; things are cut for being *the wrong thing to have built*.

⚠ **Every subtractive verdict below is a CANDIDATE, not a disposition.**
`throughlines_meta.md:233-238` sets two guards that gate finality: *(1) a subtractive verdict is a
scope reduction only if it names the downstream work it retires or shrinks — otherwise it drops to an
ordinary finding; (2) no CUT/PRUNE/MERGE/DISTILL is final until an independent adversarial pass has
**steelmanned the action** — argued, as-if-built, for KEEP — and failed against direct source.*
Neither has been done for the rows below. The precedent that should temper them: the 2026-07-08
application of this method to 97 actions produced **zero top-level CUTs**, with the disposition
landing against real over-articulation rather than against the actions themselves.

**Method note on the NERS attacks.** Every proposal gets the **scope gate first**: NERS applies to
systems that *resolve by rolling*. A ledger, a budget or a loader does not roll, and manufacturing a
NERS verdict for one is the exact error the methodology warns against — so where a proposal is out
of scope, that is said plainly and no verdict is invented. Where it is in scope, it is attacked on
all five properties: **P-i** legible odds · **P-ii** uniform, in-band leverage · **P-iii** bounded and
monotonic · **P-iv** graded, recoverable output · **P-v** the right engine for the pool regime.

The two canonical engine instances, for reference: **sigma-leverage continuous**, healthy at 5–18D
pools, where `net ~ Normal(0.4·Pool, 0.8·√Pool)` and one added die is worth
`Δz = X / (0.8·√Pool)`; and the **Domain Action Resolver**, deterministic-plus-stochastic,
`P = clamp(BASE + SLOPE·M, FLOOR, CAP)` at a flat 0.10 per point (ratified ED-874).

---

### Proposal 1 — CLOSE THE CIRCUITS

*Add nothing. Cut nothing. Connect what exists, one variable at a time.*

**Thesis.** 15% of the catalogued corpus is finished code with no caller (§5.0), and eight lanes
independently named a writer as their cheapest fix (F1). Proposal 1 takes those eight, plus two
preconditions, and lands them in an order where each is a single-variable experiment with a stated
control.

**It is the proposal with the fewest ruling dependencies — not none.** Two survive scrutiny and are
named rather than buried: step 3 needs the two §5.5 decisions in F8, and the `Faction.standing`
REFINE needs a `MULTS['standing']` multiplier that no canon surface states. Both are called out in
place below.

**The sequence, ordered by blast radius.** Determinism-neutral first; state-writing after; each
step's control named.

| # | change | ~lines | control |
|---:|---|---:|---|
| 1 | Derive a dedicated `random.Random` for the NPE from the campaign seed | 10 | goldens must be **byte-identical**; that is the whole point of doing it first |
| 2 | Re-point the three population guards at `world.npcs` rather than `world.npc_counter` | 5 | guards must still pass; they currently cannot see the change they exist to catch |
| 3 | Close the accord echo: a §5.5 `scene_outcome` classification **and** a `target_settlement` targeting rule (F8 — **needs a ruling**, do not guess either) | ~15 + 2 rulings | goldens move once, in `Settlement.order`; without both, `applied: False` and nothing moves |
| 4 | `tick_settlements(world)` as a seventh accounting step: `ledger_sweep`, L/PS seed load, `succeed_governor` where `governor_id is None` | ~40 | first campaign in which settlement state moves at all |
| 5 | Give `InsurgencyRecord.L` an accrual writer | ~15 | promotion becomes reachable; count promotions per 50-season run |
| 6 | Give Turmoil a writer from its already-live inputs | ~20 | restores the third clause of GD-1; measure win-rate delta |
| 7 | Seasonal Wealth income proportional to territories held | 1 | Wealth stops being monotone; measure Muster frequency |
| 8 | Fix Muster's 100× Wealth scaling | 1 | **must** follow 7, or Muster becomes unaffordable |
| 9 | `Faction.grudge` dict + four writes at outcomes that already fire; re-point `select_censure_target` and `select_excommunication_target` | ~25 | targeting stops being "highest Legitimacy"; measure repeat-target rate |
| 10 | Load the 46 authored characters into `world.npcs` | ~60 | now attributable, because step 1 removed the RNG-phase channel |
| 11 | Pass a commander's Charisma and Cognition through `_faction_to_unit` | ~10 | byte-identical with no commander attached; strict superset |

**Disposition table (as-if-built).**

| item | verdict | reasoning |
|---|---|---|
| `ledger.py` and its five tag families | **KEEP** | Best-shaped primitive in the corpus; the fix is a caller, not a change |
| `succeed_governor`, `AP`, `generate_npc`, `apply_conviction_scar`, `scene.accord_echo` | **KEEP** | Finished and correct; each needs exactly one caller |
| `Faction.standing` | **REFINE** — *blocked on one number* | Routing the eleven `+=` sites through `adjust()` is the right shape, but `MULTS` at `game_state.py:74` has **no `standing` key**, so `adjust('standing', …)` raises `KeyError` before any bound is consulted — the identical case the method already documents for `intel` at `:164-171`, whose stated conclusion is that wiring it *"needs a multiplier, which is a canon value nobody has stated, so it is recorded here rather than invented."* No `descriptor_registry.yaml` row declares bounds for it either, so F4's "escapes the registry clamps" is loose: **there are no clamps for it to escape.** The rename is unblocked and can land alone |
| Parliament's permanent Mandate rider | **REFINE**, not fix | It is the layer's only anti-runaway force (F4). Ratify permanence *or* replace it — do not silently restore the point |
| Muster's Wealth constant | **REFINE** | Off by 100×; land it after income so the correction is visible rather than fatal |
| — | **no CUTs** | By construction. That is this proposal's weakness, not its virtue |

**NERS attack.**

*Scope gate.* Nine of eleven steps touch no resolution — a loader, a scheduler, an RNG substream,
four writers to non-rolling state. **NERS does not apply to those and no verdict is offered for
them.** Two steps are genuinely in scope because they change a pool: **Wealth income (7)** and
**the Muster fix (8)**.

**Grudge retargeting (9) is NOT in scope, and saying otherwise would be the error the gate exists to
prevent.** It changes *which faction is selected as a target*; it changes no pool, no obstacle and no
probability. What it improves is the legibility of **motive**, which is a different property from
P-i's legible **odds**. It is a large improvement and it belongs in the design argument, not in a
NERS verdict — today a faction is censured for having the highest Legitimacy, which the player
cannot see and would not recognise as a reason; after, it is censured because it censured you. Same
arithmetic, a cause the player can name.
- **P-ii uniform, in-band leverage — PASSES.** Wealth buys Muster dice through
  `pool = Mil + floor(W/2)`, so 2 Wealth buys 1 die. In the sigma engine one die is worth
  `Δz = 0.4/(0.8·√Pool)` — **more to a small pool than a large one.** That is self-damping and
  in-band, the correct direction.
- **P-iii bounded and monotonic — PASSES, with one mandatory addition.** Wealth is registry-clamped
  0–7, so `floor(W/2) ≤ 3` and the income term saturates on a large holding while a small one still
  accrues — negative feedback on the leader, which is what F4 says the layer is short of. **But a
  grudge counter with no decay is an unbounded ramp**, and it feeds target selection, which
  generates more grudge. Step 9 is only admissible with a decay term; without one it reproduces the
  `Faction.standing` defect in a new field. Stated as a hard precondition, not a nicety.
- **P-iv graded, recoverable output — UNCHANGED.** No degree ladder is touched.
- **P-v right engine for the pool regime — UNCHANGED.** Faction pools stay in the 5–18D band the
  sigma engine is calibrated for.

**Verdict: PASSES**, conditional on grudge decay.

**What it does not do, stated plainly.** It makes the existing game *work*. It does not make it
*good*. After all eleven steps the tree still carries seven name collisions, three rival faction
action economies, nine parallel personal meters and ~150 unbuilt proposals. It maximises "it runs"
and leaves "it is a game" entirely open.

---

### Proposal 2 — THREE PRIMITIVES

*The whole corpus reduces to three missing things. Build exactly those, and merge or cut everything
that duplicates them.*

**Thesis.** F3, F6 and F7 all point the same way: the corpus is not 150 ideas, it is a handful of
primitives instantiated 150 times. Proposal 2 names three, builds them once, and routes every
duplicate through them.

**Primitive A — Person.** One entity, `actor_id`-keyed, unifying today's `NPC` dataclass, the
46-entry registry, `Settlement.governor_id`, `Settlement.npc_ids`, mass battle's officer, the
companion, and the political rank-holder. A person carries identity (convictions, disposition,
volatility), capability (a 1–7 attribute set), and a **`roles` set** — governor, commander,
companion, seat-holder — because `companion_specification_v30.md:22` is right that these legitimately
compose on one person. Plus `power_base` from the roster research, which types the climb driver, the
downfall shape, and whether a dismissal is enforceable.

**Primitive B — Ledger, generalised.** Lift `systems/settlements/sim/ledger.py` from
settlement-scoped to **any-entity-scoped**: a faction, a settlement, a person and a treaty all carry
a tag list over the same five families. Faction grudges become `Grudge` tags. Parliament's motion
history becomes `Precedent` tags. NPC memory becomes a tag with a salience value. Durable fiscal
claims become `Debt` tags — which is exactly what ED-IN-0046 D3 already ruled a Compact is.

**Primitive C — Budget.** Generalise `AP = 2 + facility_tier` from a settlement property to a
per-actor, per-scale seasonal action budget. A faction's season is an AP spend. A governor's season
is an AP spend. This replaces the single weighted draw as the top-level driver.

**Disposition table (as-if-built).**

| item | verdict | reasoning |
|---|---|---|
| `NPC` dataclass · npc_registry · `governor_id` · `npc_ids` · officer · companion | **MERGE** → Primitive A | Six representations of one thing; a person object satisfying any one fails the others |
| `Faction.grudge` (proposed) · `npc_memory` · `persistent_state` · `aims/redLines/threat/patience` · the relational-edge data file · Capital-Posture | **MERGE** → Primitive B | Six bespoke memory stores, all expressible as tags. Proposal 1's step 9 becomes a tag write |
| `ledger.py` | **KEEP**, scope widened | The primitive is right; only its key space changes |
| `AP` property | **KEEP**, scope widened | Same |
| `faction_action.py`'s weighted `rng.random()` draw | **CUT** | As-if-built: a faction's entire strategic agency is one draw against a prior. It is not a decision, it is weather. Demote to a fallback for factions with no live person |
| `ci_political_v30 §5` card-hand + cooldown economy | **CUT** | A third action economy for the same slot; Primitive C supersedes it |
| AI six-tier threat-priority posture stack | **DISTILL** | Keep the *ordering* as the AP-spend heuristic; cut the parallel architecture |
| Shadow Renown · Deniability Debt · suspicion · Renown · SA · WC · `consolidation_progress` · Franchise · Caste | **DISTILL** to two | Nine bounded personal meters differing only in trigger lists. Keep one **public** (Renown) and one **private** (Exposure, absorbing Shadow Renown + Deniability Debt + suspicion). Caste survives only if it gates something Renown cannot |
| The 500-seed predicate sweep | **PRUNE** to a balance oracle | Already ruled (D1). Executing the ruling *is* the pruning |
| `references/values_master.yaml`-style derived duplicates | **CUT** | Already retired; named so nothing resurrects them |

**NERS attack — and this is where the proposal fails as first stated.**

*Scope gate.* Primitives A and B store state and do not roll: **out of scope, no verdict offered.**
Primitive C is a budget, which is also not a roll — but it *governs what gets rolled*, and it is
proposed as a currency spanning both canonical engine instances. That puts the **seam** in scope, and
the seam is where it breaks.

- **P-ii uniform, in-band leverage — FAILS.** Suppose 1 AP can be spent either as a modifier in the
  Domain Action Resolver or as a die in a sigma-leverage roll. In the DAR the return is flat by
  construction: `SLOPE · M` at 0.10 per point, engine-wide. In the sigma engine it is not.

  *The arithmetic, with its step shown, because the two cases need different expressions.* For a
  **σ-space modifier** of size `X`, `Δz = X / (0.8·√Pool)` — σ is unchanged, so this is exact. For an
  **added die**, μ and σ both move, and at a balanced check (`Ob = 0.4·Pool`) the true value is
  `0.5/√(Pool+1)`: **0.204σ at Pool 5** and **0.115σ at Pool 18**. Converting to probability at the
  mode, `φ(0)·Δz = 0.3989 × 0.204 ≈ 8.1` points against `0.3989 × 0.115 ≈ 4.6` points.

  So the same AP is worth **≈1.8× as much** spent on a small pool as a large one — and note that the
  die expression is also obstacle-dependent (at Pool 5 it ranges ≈0.107σ at Ob 0 to ≈0.302σ at Ob 4),
  so there is no single "value of a die" to price AP against at all. Its value relative to the flat
  0.10 DAR point therefore swings by roughly a factor of two depending on which engine the player
  routes it into, and by more once the obstacle varies. A player who notices converts AP wherever it
  pays most, every season. **This is the flat-shift trap one level up:** not a flat modifier inside
  one engine, but a flat *currency* across two engines with different — and, on the sigma side,
  non-constant — leverage curves.
- **P-iii bounded and monotonic — PASSES.** AP is `2 + facility_tier + bonus` with `facility_tier`
  capped at 3, so the budget is bounded by construction.
- **P-i / P-iv / P-v — UNCHANGED** by the primitive itself.

**Verdict: FAILS as first stated. PASSES with a mandatory restriction:** *AP buys **actions**, not
**modifiers**.* One AP is one attempt at something; it never converts into dice or into DAR points.
That keeps the budget out of the resolution arithmetic entirely — which also re-passes the scope
gate, so the currency stops being a NERS object at all. It is also the simpler design, and the one I
would ship. The alternative — a per-engine conversion rate calibrated so marginal probability gain
is equal — is defensible, needs a number nobody has measured, and buys nothing the restriction does
not.

**What it costs.** Substantially more than Proposal 1: a new entity, a widened primitive, and a
replaced top-level driver. It also requires the naming pass from F5 as a precondition, because you
cannot type a `roles` field while *officer* means two things.

---

### Proposal 3 — THE DISPOSAL

*Delete, as-if-built, the parts of the design that would not survive contact with a player.*

**Thesis.** The three proposals around this one all add. This one only removes, and it can run
concurrently with any of them because nothing it touches has a production caller. Its claim is that
the corpus is not merely disconnected but **oversized**: ~150 strong-sense gaps and ~150 unbuilt
proposals against four things that actually run is not a backlog, it is a design nobody can finish or
balance.

**Cut list — code.**

⚠ **Reachability in this tree is not an import graph.** `CLAUDE.md` §3 is explicit that subsystem
dependencies are *"declared in `references/` and resolved by string at first call"*, so a module with
zero textual importers can still be load-bearing, and **a cut list must be checked against
`references/module_contracts.yaml` as well as by grep.** Two modules below are live only through that
path: `engine/autoload/game_state.py`'s `restore_world` reaches `treaty.py` and `beliefs.py` via
`composition.require('snapshot_state.treaties')` at `:474` and
`composition.require('snapshot_state.beliefs')` at `:484`, registered at
`module_contracts.yaml:135-144`. **Deleting either breaks save restore for any campaign carrying that
registry.** The remaining six rows were checked against the registry as well as by grep.

| module | as-if-built reasoning |
|---|---|
| `systems/factions/sim/treaty.py` — **the dead surfaces only, not the module** | `propose_treaty` and `process_treaty_expirations` have no production caller, and with no RNG the fallback roll is fixed at 0.95 against a 0.90 hazard, so `0.95 < 0.90` is false and **lapse is impossible on that path** — while the inline comment at `:137` reads *"default to high-lapse if no rng"*, asserting the opposite of what the constant does. That comment is itself a defect. **`TreatyRecord` is KEEP** — `restore_world` requires it by string |
| `systems/characters/sim/beliefs.py` — **the dead surfaces only, not the module** | `add_belief` is the **sole constructor** of a `Belief` and has zero production callers, so a live campaign can never contain one and both revision paths always take their not-found branch. **`Belief` is KEEP** — `restore_world` requires it by string, and `systems/social_contest/sim/contest_legacy_stub.py:240` carries a guarded production import |
| `engine/autoload/npc_ai.py` | Two typed no-ops; `module_contracts.yaml:278-282` records `resolver: none`. Its docstring names `faction_action` as a *dependency*, which is backwards — the live loop calls `faction_take_action` directly |
| `systems/world/sim/miraculous_event.py` | Stub, zero callers, and its effect (SA +1 to every present faction) targets a stat that has no field |
| `systems/overview/sim/ip_track.py` | Both entry points are typed no-ops; IP is one of the four painted-on gauges |
| `systems/world/sim/restoration_movement.py` | Both entry points are typed no-ops; GD-3 Stages 1–2 |
| `systems/settlements/sim/temperaments.py` | Zero importers; the α/β ethical axis it maintains is read by nothing |
| the six faction stubs (`charter_liberties`, `hafenmark_equipment`, `home_sanctuary`, `infrastructure_reclamation`, `varfell_mandate_action`, `varfell_territorial_acquisition`) | Typed `stub_resolve` no-ops, test-only references. Their existence is why Hafenmark and Varfell "have unique actions" on paper and are string-comparison-identical in play. (`home_sanctuary.py` carries two stub sites, `:31` and `:39`) |

`mass_seizure.py` is the deliberate exception: it is **fully implemented, correct, and has zero
production callers**, gated on `CI ≥ 60` which nothing drives to 60, and one-shot per campaign.
**Wire it or cut it — do not leave it.** As-if-built it fires at most once in fifty seasons, which is
a legitimate design (a singular historical rupture) but only if something can reach it.

**Cut list — design.**

| item | verdict | as-if-built reasoning |
|---|---|---|
| Parliamentary Sanction tiers 2–5 (Embargo, Blockade, Combined, Outlawry) | **REFINE, not CUT** — see the NERS attack | Four tiers needing a Supermajority bar, per-season recurring effects and a rescission path the vote resolver does not have. But cutting them outright costs P-iv |
| The 74-rung Standing ladder across 12 ladders, each with eight "Skyrim" dimensions | **DISTILL** | 592 authored cells that a player experiences as one number going up. Keep one 0–7 track plus `power_base`; cut the per-ladder differentiation |
| Seven of the nine parallel personal meters | **DISTILL** to two | Per Proposal 2's table; identical reasoning |
| `godot_architecture_specification.md` + the four 2026-04-18 stale docs | **CUT** | Already banner-marked STALE REFERENCE; they encode the pre-`d+σ` model and `data_serialization_spec.md` ships wrong schemas (writable `mandate`, 34 vs 35 settlements) |
| `godot/skeleton/` | **CUT** | Covers 1 of 27 modules, `extends` a spine defined nowhere in the corpus, does not compile. It is not a head start; it is a liability that reads as one |
| Canon §9's unique-action table (Royal Decree, Sovereign Authority Doctrine, The Private Collection, Economic Leverage) | **CUT or ratify, explicitly** | Under §0.05 the code wins, and the code implements **none of these** under those names or formulas. So half the table is not "unimplemented", it is **retracted** — and someone has to say so before another session builds toward it |
| The four fiscal proposals adjudicated against the phantom `Compact` tag family | **PRUNE to re-adjudication** | Encabezamiento, Salt Certificate, State Arsenal, Borrow. One was rated "ratify as-is" on a false premise (F3). Not wrong — **unjudged** |

**NERS attack.**

*Scope gate.* Deleting inert modules changes no resolution path — **out of scope; no verdict is
offered, and manufacturing one would be the error the methodology names.** One item is in scope: the
Sanction ladder, because it governs the magnitude of a resolved outcome.

- **P-iv graded, recoverable output — FAILS if tiers 2–5 are simply cut.** Censure alone leaves
  Parliament with exactly one severity setting, so every parliamentary outcome is the same size. A
  resolution system whose output is binary-at-one-magnitude is the P-iv failure mode.
- **Repair, which is better than either option.** ED-FA-0006 already established that the five tiers
  are **one parameterised action** differing in {proposer minimum, vote bar, magnitude, duration} plus
  two riders. So keep the *parameterisation* and drop the *tiers*: one Censure action whose magnitude
  the proposer chooses at a Legitimacy price, resolved on the existing Persuasion Track. That is a
  continuous dial where the design had five discrete rungs — **strictly better on P-iv than the thing
  being cut**, and it needs only a magnitude argument rather than the Supermajority/recurrence/
  rescission machinery the tiers demanded.

**Verdict: the code cuts are out of scope and PASS. The Sanction cut FAILS P-iv and is replaced by
the REFINE above.**

**What it buys.** It is close to free — after the two corrections above, nothing it deletes has a
caller by import *or* by string — and it is the only proposal that improves the tree's
signal-to-noise rather than adding to it. "Free" is not "final", though: per the method note in §6,
none of these subtractive verdicts has been steelmanned by an independent pass arguing as-if-built
for KEEP, which ED-IN-0027's second guard requires before a CUT is final. It also removes the standing hazard
that a future session reads `npc_relational_graph_v30.md`'s "BUILT 2026-06-09" header, or the
skeleton, and builds toward something that does not exist.

---

### Proposal 4 — THE SEASON IS A PERSON'S SEASON

*Stop iterating factions. Iterate people. A faction acts because someone in it acts.*

**Thesis.** Every within-system analysis in Part 3 says a version of the same sentence: no person is
present. The current season loop is *for each faction, take one action*. Proposal 4 inverts it: the
loop iterates **people**, and a faction's move is the aggregate of what its office-holders did.

This subsumes more of the corpus than any other proposal here. It forces Primitive A. It gives
Parliament seat-holders and therefore motions with authors. It gives settlements governors and
therefore `succeed_governor` a caller. It gives battles commanders and therefore `derive_command`
its two attributes. It makes six of the seven Sufficient Scope conditions reachable, which lights
the cross-scale layer. And it turns `Key.causes[]` from a provenance chain into a **biography** —
which is what the substrate was built for and has never once been used as.

**Disposition table (as-if-built).**

| item | verdict | reasoning |
|---|---|---|
| `faction_take_action`'s weighted draw as the **top-level driver** | **CUT** | As-if-built, a faction's whole strategic agency is one `rng.random()` against a prior re-weighted by three signals. It cannot be argued with, lobbied, or anticipated. Demote to a fallback for factions with no live person |
| `if faction.name == 'Crown'` / `elif == 'Church'` personality | **CUT** | Hafenmark and Varfell have no branch: **swap their names in the starting table and the campaign is unchanged.** A faction's character should come from who leads it |
| `select_censure_target` / `select_excommunication_target` | **REFINE** | Their own docstrings say they pick highest-Legitimacy *because no relationship signal exists*. A person supplies one |
| `_emergency_council_parties` | **REFINE** | Keep the trigger; replace both sides being derived from the same faction's aggregates with two actual people who disagree |
| `_faction_to_unit`'s geometric symmetry | **REFINE** | Both armies get identical shape, tier, position and facing, so only `power` differs and **every strategic battle is symmetric before it starts.** A commander is where asymmetry enters |
| `generate_npc` | **KEEP** | Complete, correct, ecology-biased, deviation-rolled. It needs a call site, not a change |
| The 46-entry registry | **KEEP**, with a schema reconciliation | Identity is authored on 46/46; capability on 1/46, whose `social` value is the string `"3–4"`. The two field sets share exactly two names, and those two have the worst data |

**NERS attack — and this one also fails as first stated.**

*Scope gate.* Squarely in scope: it changes **what the pool is**.

- **P-iii bounded and monotonic — FAILS.** The natural reading of "a faction acts through its people"
  is that its pool aggregates over the roster. Then `μ = 0.4·Pool` grows **linearly** with roster
  size while `σ = 0.8·√Pool` grows only as a square root, so `z = (μ − Ob)/σ` grows as `√Pool` with
  no ceiling. Worked, against Ob 2: **four** people at score 3 → Pool 12, μ = 4.8, σ = 2.77,
  z ≈ 1.01, P ≈ 84%. **Twelve** people → Pool 36, μ = 14.4, σ = 4.80, z ≈ 2.58, P ≈ 99.5%. And
  nothing caps a roster. A roster-sized pool is a **monotone ramp to certainty** — the precise
  unbounded-growth failure P-iii exists to catch.
- **P-v right engine for the pool regime — FAILS with it.** Pool 36 is far outside the 5–18D band the
  sigma-leverage engine is calibrated for. At that size the roll is decorative; the Domain Action
  Resolver would be the honest engine, and now the same action is resolving on two different engines
  depending on how many people a faction has.
- **Repair.** *The acting person's own score is the pool; the roster sets how many actions a faction
  gets per season, not how big each pool is.* Every roll then sits on a person's 1–7 scale. That the
  band works out is checkable rather than asserted: `systems/social_contest/sim/contest/_kernel_tests.py:51`
  pins `Pool.size(-9) == 5` and `Pool.size(4) == 11`, so a 1–7 faculty maps to pools of roughly 8–14
  — squarely inside the 5–18D band the sigma engine is calibrated for. Roster size becomes an
  **action count** rather than a pool multiplier, which restores the P-iii bound.

  **The repair does not imply a dependency on Proposal 2.** It needs *a bounded action counter*; P2's
  Primitive C is one such counter, derived from `facility_tier` rather than from roster cardinality —
  and P2's own NERS repair reduces AP to a bare action counter anyway ("one AP is one attempt"). Any
  bounded counter satisfies P4, including one P4 defines for itself. **The two need the same *shape*
  of primitive, not the same instance** — which argues for building the counter once rather than
  twice, and is corroborated by P2's Primitive C and P4's CUT of the weighted draw being *the same
  change* reached from two different premises. It is not an ordering constraint.
- **P-i legible odds — IMPROVED, substantially.** After the repair, an action has an author, a score
  you can see, and a reason. "Konrad rolled his Influence against the holder's Legitimacy" is legible
  in a way "the Crown drew 0.34 and got the conquest bucket" never is.
- **P-ii uniform leverage — PASSES.** Person-scale pools sit in the band where an added die is worth
  a stable, in-band `Δz`.
- **P-iv graded output — UNCHANGED.** The margin ladder is untouched.

**Verdict: FAILS as first stated. PASSES under the repair** — the roster buys actions, not dice.
That is the same restriction Proposal 2 needed independently, arrived at from a different premise,
which is why §6.5 recommends building the counter once. It is not a reason to sequence P4 behind P2.

**What it costs.** The most of the four, and it is the only one that changes what the game *is*
rather than whether it works. It is also the only one that answers the question every within-system
analysis ends on.

---

### §6.5 Comparison, and what I would actually run

| | P1 Close the Circuits | P2 Three Primitives | P3 The Disposal | P4 A Person's Season |
|---|---|---|---|---|
| **theory of the defect** | disconnected | duplicated | oversized | impersonal |
| **needs a Jordan ruling?** | **two** — the §5.5 accord-echo pair, and `MULTS['standing']` | yes (person schema, naming) | yes (what is retracted) | yes (the loop inverts) |
| **cost** | ~250 lines + 2 rulings | large | negative | largest |
| **NERS as first stated** | passes, with grudge decay | **fails P-ii** | out of scope; Sanction cut fails P-iv | **fails P-iii and P-v** |
| **NERS after repair** | passes, with grudge decay | passes with AP→actions | passes with Sanction REFINE | passes with roster→actions |
| **execution artifacts (§0.2)** | 11, each seeded and attributable | few and large | deletion rehearsals | one, very large |
| **what it leaves open** | everything about design | the connection work | the connection work | nothing, and that is the risk |

**They are not mutually exclusive, and the NERS attacks shaped the order more than the content did.**

1. **Run P3 first.** It is close to free, nothing it deletes has a caller by import or by string
   (after the two corrections its own section records), and it removes the standing hazard of a
   future session building toward a `## Status: BUILT` header with no code under it. Two holds: the
   Sanction item, which the attack converted from CUT to REFINE, and the fact that no verdict here
   has been steelmanned — so run the deletions as rehearsals with an independent KEEP argument
   attached, per ED-IN-0027's second guard, rather than as a sweep.
2. **Then P1, in the stated order, with step 3 deferred behind its two rulings.** Steps 1–2 are
   determinism-neutral and land first: §0.1 point 4 requires a stated control per change, and the
   seed-42 result shows what skipping that costs on any step that adds an RNG draw. Ten execution
   artifacts is ten more than the seven M1 junctures currently have — and under §0.2 that, not this
   document, is what would move the milestone.
3. **Then P2, once the naming pass in F5 is done.** It cannot be typed while *officer*, *Standing*
   and *Disposition* each mean two or three things. Ship Primitive C under the restriction the attack
   forced: **AP buys actions, never modifiers.**
4. **P4 whenever the person schema exists** — it is not sequenced behind P2. Its P-iii failure is
   repaired by any bounded action counter and P4 can define its own; what the two share is the
   *shape* of that counter, which argues for building it once, not for ordering them.

**The most valuable single item, and it is not the one it first appears to be.** The obvious
candidate is `scene.accord_echo` — a finished, tested, correct, Key-driven state-write loop that has
never fired. It is genuinely the highest-value target in the tree, and the adversarial pass showed it
is **not cheap**: it is dormant on two declarations, and the second, a faction→settlement targeting
rule, is a ruling the code is deliberately refusing to guess (F8). Worth doing, worth doing properly,
not worth mistaking for a one-line write.

The best *cheap* item is P1's step 5: **give `InsurgencyRecord.L` a writer.** One accrual rule, in a
pipeline that already forms insurgencies from real contiguity data and already iterates every open
record every season looking for promotion, blocked only because `L` is set to 1.0 once and promotion
needs 3. It is the only cheap change in this document that **adds an agent to the world** — neglected
ground starts producing rebellions that grow into factions that can invade the power whose neglect
made them, which is the one place the design already says the world should generate its own
opposition instead of waiting for a player.

**And the one that most needs measuring rather than ruling.** Parliament's permanent Mandate penalty
is an uncontrolled asymmetry whose *sign depends on which branch fires* (F4), and it is widely
assumed to be the strategic layer's anti-runaway damper. That is a campaign-level balance claim with
no control, and `tools/balance_oracle.py` can settle it in about thirteen minutes against a change
that is campaign-reachable. **Run the oracle before anyone rules on it, and before anyone quietly
patches the comment.**
