# Social Contest ↔ Settlement Management / Faction Actions: Extent of Interface

## Status: FILED (informational review) — 2026-07-08 · Lane: SC (cross-cutting FA/SE). Advisory
## only. Its highest-leverage recommendation (rule ED-SC-0002) is executed by the same commit that
## adds this file — see `canon/editorial_ledger.jsonl` ED-SC-0002/ED-SC-0007 and `handoffs/HANDOFF_SC.md`.

Scope note: this report treats three genuinely distinct questions in three sections, per Jordan's
framing — (1) what is actually built and wired today, code + doc; (2) where the system's own
architecture implies the interface must extend, whether or not anything is built; (3) what the
system's historical/political research lineage actually argues for, and which scale it was written
about. All file paths are absolute-repo-relative; line numbers are as of 2026-07-08.

---

## 1. ACTUAL interface today

### 1.1 What the canon docs literally say (declared connections)

**`designs/scene/social_contest_v30.md`**

- **§6 Domain Echo** (lines 287–290): "Decisive win + Memory genre: winning faction's Mandate +1
  in the domain of the cited precedent. Decisive win + Projection genre: +1D on first Domain
  Action pursuing the argued outcome within the season. Compromise: no Domain Echo."
- **§6.1 Obligations** (lines 296–344): a Decisive win in a Formal/Grand Contest produces a
  binding, cross-season Obligation with named Mandate/Stability faction penalties on violation
  (table, lines 304–309). **Settlement-targeted Obligations** (line 311) are the most explicit
  settlement-stat text in the whole corpus: *"Church must not station Inquisitors in S-017
  Gransol Market Quarter for 2 seasons"*; *"Crown must maintain Defense ≥ 2 in S-006 Lowenskyst
  Fortress"*; *"Varfell must not develop Prosperity in S-032 Oastad Shrine."*
- **§7.2 Succession Contest** (lines 386–423): a faction-leader-removal event opens a Grand
  Contest variant, adjudicated by **the faction's own institutional body** (a per-faction table,
  line 393: Crown inner circle by Disposition majority, Hafenmark Parliament by Mandate-weighted
  vote, Varfell Jarl Assembly by quorum, Church College of Cardinals, Löwenritter Knight-Commander
  seniority, Guilds Council by Favour-weighted vote, RM by consensus). Compromise outcome produces
  a **Faction split** with track-distance-weighted stat division (60/40 at Track 4, 55/45 at
  Track 5, 50/50 at Track 6 — §7.2.1, lines 404–419) across Mandate/Wealth/Military/Influence/
  Stability, territory, and treaties, with a hard Stability floor of 3.
- **§10 BG-Vote** (`params/contest.md` lines 127–181, and `social_contest_v30` cross-refs):
  faction-scale vote, pool = sum of participating factions' Mandate, Total Victory → losing
  coalition's dominant faction Mandate −1.

**`designs/architecture/scale_transitions_v30.md`**

- **§4.3.2 Mandatory Zoom-In Triggers** (lines 129–138) — of the 8 canonical triggers, two name a
  contest at settlement/faction scale directly: **Settlement Revolt** ("Player is in a province
  containing a settlement at Order 0 … they choose: support the garrison (combat), negotiate with
  the populace (**social contest**), investigate the cause (fieldwork), or flee") and **Stability
  Crisis** ("Emergency faction council: **social contest** or fieldwork scene revealing the source
  of the crisis"). Two more are contest-shaped without naming the mechanism explicitly: **Faction
  Leader Removal** ("Succession mechanics fire… If Standing ≥5: leadership offer") and **Rank
  Advancement Recognition Event** ("Recognition can be withheld in-scene if inner-circle
  Disposition or rival-candidate conditions fire — creating a debt scene").
- **§5 Domain Echo** (lines 173–236) is the full propagation-rule prose: §5.1 Sufficient Scope
  gate, §5.2 amount-by-degree table (Overwhelming ±2 / Success ±1 / Partial narrative-only /
  Failure −1 to acting faction's own stat, PP-329 one-Echo-per-scene-per-faction cap), §5.4
  "Debate → Domain Echo" (Persuasion Track banded to Mandate ±1), §5.5 Accord Domain Echo with
  explicit **settlement targeting** (line 208, "AUD-SET-02": "Accord changes from personal scenes
  target the settlement where the scene occurred, not the province directly"), §5.6 Thread Domain
  Echo.
- **§7 Sufficient Scope**, item 7 (line 266): "Settlement governance action that changes Order by
  ±1 or more" independently qualifies a personal scene for Domain Echo.

**`designs/territory/settlement_layer_v30.md`** — the one settlement doc naming social contest
directly: **"Contested management"** (§3.3, line 458): "If the subnational faction's interests
conflict with the province faction's orders… the conflict resolves through **social contest
(per social_contest_v30 §7** — asymmetric, with the province faction as institutional authority
and the subnational faction as petitioner)." Also line 93 (Prince-in-Waiting maintenance is a
"social contest, Disposition pool vs Ob 2").

**`designs/territory/governance_play_redesign_v1.md`** (Status: **PROPOSAL**, drafted 2026-06-22,
**not ratified**) is the closest thing in the corpus to a distinct settlement-scale contest
mechanic — but it is explicitly built *on top of* §7 asymmetric social contest, not a new
resolution mode: **Hold Court** (adjudicate a Local-Actor dispute, sets a Precedent tag), **Treat**
("Influence + history vs subnational leader (social contest §7)"), **Bargain** as a Directive
response ("social contest vs PA (§7, you as petitioner)"), and a Suspicion-triggered **Recall
scene** ("you're summoned to justify yourself — a social contest"). None of these four verbs has
any code implementation — confirmed by grep across `sim/` for `governance_play_redesign`,
`hold_court`, `grand_debate`: zero hits outside the design docs.

**`designs/provincial/faction_layer_v30.md`**: collapsed-faction officers "may be recruited by
other factions via Social Contest (Ob = Leadership Deviation Ob + 2)" (line 215); stalled treaty
negotiation escalates to "Grand Debate (social_contest_v30.md)" whose degree modifies the
ratification margin M by +2/+1/0/−1 (§3.3, lines 368–370); "Parliament motions may be influenced
by personal scene outcomes (Social Contest → Domain Echo → +1D on Rebuttal roll or Ratification
roll)" (§8.3, line 608).

### 1.2 What is actually wired in code (verified against `sim/`)

**The one live path — and it throws its own verdict away.** `sim/cross_scale/scene_dispatch.py`
is the campaign-loop glue (called from `sim/mc_v18.py`). Its `evaluate_triggers()` (lines 52–76)
evaluates **only** the Stability Crisis trigger (`evaluable = {"Stability Crisis"}`, line 73)
against `Faction.Sta ≤ 2`; the other 7 §4.3.2 triggers — including Settlement Revolt — are
unconditionally reported `deferred`, never evaluated, because (module docstring, lines 36–38)
"the other 7 triggers need world-state schema not present on the aggregate World."

As of the 2026-07-08 commit (`2519d2b`, closing **ED-SC-0006**), the Stability Crisis contest now
**actually resolves** through the promoted kernel (`sim.personal.contest.build_contest` /
`resolve_contest`), retiring the deprecated `contest_legacy_stub.run_contest` call the branch used
to make (`_resolve_slot`, lines 122–191). Both "sides" of the contest are derived from **the same
faction's own aggregate stats** — `_emergency_council_parties` (lines 97–115): `side_a =
round(Faction.L)`, `side_b = round(7 - Faction.Sta)` — an explicitly `[SEED]`-flagged, provisional
bridge, not a real second party. It resolves via a Guild Arbitration proceeding
(`EMERGENCY_COUNCIL_PROCEEDING = "guild_arbitration"`, also `[SEED]`). The kernel produces a real
verdict — but the module's own comment (lines 165–170) states plainly: mapping that verdict to a
Domain Echo degree is **ED-SC-0007**, "blocked at the spec level by the ED-SC-0002 echo-keying
fork — out of scope here; no `echo` block is set, so echo_transport… stays inert." **Net effect: a
contest genuinely resolves every time a faction's Stability drops to ≤2, and its outcome touches
zero faction or settlement state.** This is confirmed both by my own read of the file and by an
independent research agent's trace, which reached the identical conclusion.

**A second, more complete path exists in code but is never called from the campaign.**
`sim/personal/parliamentary_vote.py` (`run_parliamentary_vote`, implementing §10) is a complete,
tested, independent re-implementation of the BG-Vote (not the kernel's `Bout` resolver — its own
dice-pool path via `dice_engine.roll_pool`). On Total Victory it **directly mutates faction
state**: line 203, `world.factions[dominant].adjust("L", BG_VOTE_TOTAL_VICTORY_MANDATE_DELTA *
MULTS["L"])` — a real Mandate write keyed off a contest outcome. This feeds
`sim/provincial/parliamentary_transfer.py` (`propose_transfer`), which moves territory ownership
and adjusts L/Sta/standing/Accord, and `sim/personal/parliamentary_stay.py` (§10.1 Stay). But
`sim/mc_v18.py` and `sim/provincial/faction_action.py` (the actual per-season faction-action
dispatcher — read in full; its four branches are Crown Initiative / Church unique actions /
Conquest via mass battle / Muster / Govern-by-plain-roll) never import or call
`run_parliamentary_vote`, `propose_transfer`, or the parliamentary-stay module. The only callers
are tests (`sim/tests/test_f7_smoke_oracle.py`). **This is a real, tested, mutating contest→faction
pathway that is completely absent from the running simulation.**

**`sim/personal/contest/faction.py`** is explicit about its own status — its docstring's first
words are **"ADAPTER (not canon)"**: it "Models the canonical Parliamentary action (faction_layer
§5) on the contest engine, to exercise the engine in the faction-action context." It implements
`vote`/`rate` (motion voting), `succession` (directly implementing §7.2's band thresholds and
60/40-55/45-50/50 splits), and `coalition_vote` (an N-party BG-Vote pooled onto the two-pole
engine) — but purely as an exercise harness, not a production code path. Not imported by
`faction_action.py`, `mc_v18.py`, or `scene_dispatch.py`.

**`sim/cross_scale/domain_echo.py`** implements §5's formulas as pure, side-effect-free functions
(`compute_domain_echo`, `compute_accord_echo`, `compute_thread_echo`) — it performs no mutation
itself and has no caller other than the one below.

**`sim/cross_scale/echo_transport.py`** (ED-IN-0028) is the sole consumer of `domain_echo.py`, and
is exactly as inert as its own docstring says: it fires `emit_scene_echo` only when **both**
`world.echo_scheduler` is attached **and** `ctx` carries an explicit `echo` block (lines 108–117).
`world.echo_scheduler` is attached only if the `ECHO_TRANSPORT` env flag is on, which
`sim/mc_v18.py` defaults **off**; and even with the flag on, the live Stability-Crisis trigger
never populates `ctx['echo']` (confirmed at scene_dispatch.py lines 168–170) — so the path stays
inert regardless of the flag, "exactly as ED-IN-0028 left it."

### 1.3 Does a settlement-scale contest exist as a distinct thing?

**No.** There is no settlement-scale contest mechanic (a "local governance dispute" or "Settlement
Revolt" resolution distinct from a faction-scale contest) implemented anywhere in `sim/`. It exists
only as: (a) a named-but-never-evaluated Mandatory Zoom-In trigger in `zoom_in_out.py`, never
fired by `scene_dispatch.evaluate_triggers()`; (b) a one-line asymmetric-§7 citation in
`settlement_layer_v30.md:458` ("Contested management"); and (c) the unratified PROPOSAL doc
(`governance_play_redesign_v1.md`), which layers several social-contest-flavored verbs onto
settlement governance but explicitly states it "**cannot fire** until the audit's `G1` is closed:
there is no settlement registry" (§5.2) — a gap that was in fact closed on 2026-06-23
(`sim/territory/registry.py`), but nothing has gone back to wire the governance-redesign verbs
against it.

**`sim/autoload/game_state.py` dataclasses** confirm this structurally. `Faction` (lines 91–116):
`name, parliamentary, L, Sta, W, I, Mil, territories, senator_inward_used, consul_used, peaceful,
standing, excommunicated, council_used_this_arc` — no settlement back-reference, no per-settlement
field at all. `Territory` (lines 126–144): `tid, owner, accord, pt, garrison, prosperity,
fort_level, templar, uncontrolled_since` plus `adjust_accord`/`adjust_pt` — these *are* mutated by
non-contest code (`faction_action.py`'s `_try_govern`, `parliamentary_transfer.py`), but no
contest-resolution code calls them. `sim/territory/registry.py`'s newer `Settlement` dataclass
(added 2026-06-23, closing audit gap G1) *does* carry `order`, `legitimacy`, `popular_support`,
`prosperity`, `defense` — the fields a settlement-scale contest would need — but its own inline
note (lines 60–63) flags `legitimacy`/`popular_support` as "declared but NEVER READ OR WRITTEN
anywhere in sim/ … an INERT LPS-1 schema stub, not a working per-settlement L/PS pipeline."

Every module touching faction political state also carries a standing `[PRE-LPS-1 /
PORT-BLOCKING — ED-FA-0004]` banner (`game_state.py`, `faction_action.py`,
`parliamentary_vote.py`, `faction_canon_v30.md`). Put plainly: **there is no `Mandate` stat in
code at all** — the `Faction` dataclass has only `L/Sta/W/I/Mil`, and every contest-adjacent
module that speaks of "Mandate" is reading `Faction.L` under an explicit legacy-alias comment.
`domain_echo.py`'s own return shape (`affected_faction, affected_stat, delta`) is, per the
propagation spec's own self-audit, "exactly the pre-inversion 'Layer 4' scalar-delta shape" that
the spec's AU-1 rule (a faction stat must never be directly set, only aggregated from
settlement/territory holdings) has since ruled out — even the inert plumbing that exists is
shaped for a write pattern the architecture no longer sanctions. The entire `Faction.L`-as-Mandate
scalar model — including the one working contest→faction mutation, `parliamentary_vote.py`'s
`adjust("L", ...)`
— is itself the pre-LPS-1 superseded schema, not yet replaced by the per-settlement L/PS ×
Weight-aggregated Mandate model that `settlement_layer_v30.md §1.8` (LPS-2e, ratified 2026-05-30)
already canonizes in prose.

**Depth verdict for §1: thin.** One contest type resolves live and touches nothing; one complete
mutating pathway exists and is never called; every canon-doc connection beyond those two is prose
only, with zero code home.

---

## 2. LOGICAL EXTENSION (architecturally implied, not yet built)

### 2.1 The propagation spec already names this exact gap as the thing it exists to close

`designs/architecture/propagation_spec_v1.md` (status: CANONICAL as of 2026-07-02, ED-1083/1094)
is the workplan's **AU-1 "no aggregate is ever written"** rule:

> `faction_stat[s] = AGGREGATE_s(settlement/territory stats over holdings) ⊕ Σ_k
> national_event_modifier_k` … `faction_stat[s]` has **no setter**. Every write… terminates at one
> of two leaves: a settlement/territory substrate cell, or an entry in the Key log that the
> aggregation function reads at derivation time.

Section **AU-5** ("Wiring contract: closing the domain_echo.py ↔ scene_dispatch.py seam") names —
at the architecture-spec level, independent of my own code trace — the identical gap: *"`_resolve_
slot` (`sim/cross_scale/scene_dispatch.py:83-119`) computes a resolver result and then calls
`zoom_in_out.zoom_out({}, world)` — an empty dict, never populated from the resolver result. This
is the 'OUTCOME→ECHO MAPPING GAP' the module's own docstring names and explicitly declines to
fabricate."* In other words: this is not merely an implementation lag Jordan happens not to have
gotten to. The system's own aggregate-up/distribute-down doctrine treats "personal-scale contest
outcome → settlement-locus stat write → faction-level re-aggregation" as the canonical, singular
shape every consequence in the game must take. A contest that resolves and touches nothing is a
structural incompleteness under the doctrine the repo has already ratified for itself, not an
optional nicety.

### 2.2 Settlement governance disputes: contest-shaped, but blocked on registry + verb wiring, not on missing design

A Governor's contested legitimacy is **not** a distinct contest type today — the only reachable
path is the faction-level Stability Crisis (§4.3.2), which derives its "parties" from the
*faction's* aggregate stats, never a settlement's. But `governance_play_redesign_v1.md` (the
PROPOSAL) explicitly specifies contest-shaped settlement mechanics: **Hold Court** (adjudicate a
Local-Actor dispute — structurally identical to an asymmetric §7 contest, just renamed), **Treat**
(an explicit §7 citation), **Bargain** (an explicit §7 citation), and the Suspicion-triggered
**Recall scene** (also an explicit "a social contest"). So the redesign does **not** bypass
personal-scale resolution — it leans on it more heavily than the current canon does, four separate
times. What it lacks is a party-derivation bridge analogous to `_emergency_council_parties`, one
scoped to a *settlement's* Legitimacy/Popular Support/Order rather than a *faction's* L/Sta — and
the settlement registry those fields need existed only as of 2026-06-23, a month after the redesign
was drafted.

### 2.3 Faction Leader Removal / Rank Advancement Recognition Event: logically succession-and-arbitration-shaped, undelivered

Both are among the 8 §4.3.2 mandatory triggers, and both are logically contest-shaped even though
`scene_dispatch.py` never fires either: **Faction Leader Removal**'s own scene content
("Succession mechanics fire… leadership offer") *is* §7.2 Succession Contest, already fully
specified (adjudicator table, track-distance faction-split, Wager-Obligation power). **Rank
Advancement Recognition Event**'s content ("Recognition can be withheld in-scene if inner-circle
Disposition or rival-candidate conditions fire") is a smaller-stakes arbitration exactly analogous
to Guild Arbitration/Panel. Both are unreachable in code for the same reason Settlement Revolt is:
`evaluate_triggers()`'s `evaluable` set names only `"Stability Crisis"`. The design work for these
two triggers is largely *already done* (§7.2 is fully specced prose); the gap is purely the
context-derivation bridge, of the same shape ED-SC-0006 just wrote for Stability Crisis.

### 2.4 Territorial arbitration: canonical link exists in prose, is code-inert

Guild Arbitration is a canonical proceeding (`social_contest_v30.md` §2 Step 1, Panel adjudicator
per ED-1059) with a real weighted-by-standing verdict mechanism (ED-1057), but there is no
canonical rule anywhere connecting an arbitration verdict to territory ownership or Accord change —
`params/contest.md`'s Panel section is entirely about *who judges and how the ballot aggregates*,
never about *what the verdict does to world state*. The only place a contest verdict is
canonically wired to territory-level consequence is §5.5 Accord Domain Echo (a governance/
destabilisation/territorial-transfer/violence table) — and that wiring is itself the same
`domain_echo.py`↔`scene_dispatch.py` seam that is inert per §1.2/§2.1 above. So territorial
arbitration's link to ownership/accord is real in the propagation-spec sense (the machinery to
carry it exists) but is not yet exercised by any specific rule connecting a Guild Arbitration
verdict, specifically, to a territory-control change — that would need its own authored table,
analogous to §7.2.1's faction-split ratios, and none exists yet.

### 2.4b No settlement-scale Key type exists yet — the missing middle container

`designs/architecture/key_echo_armature_v1.md` §3 has to *propose* settlement-scale Key types as
new candidates — `state.settlement_revolt`, `state.legitimacy_drift`,
`mechanical.settlement_captured` — because none exists in `references/key_type_registry_v30.md`
today. This is the sharpest version of the §2.2/§2.4 gap: the propagation spec's channel (i)
(a settlement/territory-locus stat write that a faction aggregate later re-derives) requires a
settlement to be an addressable `targets[].actor_id` with its own Key vocabulary, and that
vocabulary is still PROPOSED, not registered. Until it lands, no contest resolver — arbitration,
Succession, Settlement Revolt, or anything else — has a legal target to write a settlement-locus
consequence into, independent of whether `scene_dispatch.py` ever populates the `echo` context
block. There is also an open, HIGH-severity, unresolved disjointness question feeding this same
seam (propagation spec §3, "D.6"): a down-targeted settlement `stat_deltas` write may overlap the
very settlement stats a faction's `AGGREGATE_s(...)` reads from, and until that is ruled disjoint
the up/down loop can double-count — the spec currently "ACCEPT[s] disjoint as a working
assumption, not a closed question."

### 2.5 Consensus mode and the Fable-5 four-modes finding

The Fable-5 social-contest audit (`designs/audit/2026-07-05-fable5-social-contest-audit/`,
ratified in full 2026-07-05, PR #80, "Ratify all") is not primarily about Consensus as a fourth
game mode — that finding lives in the earlier 2026-06-28 deliberation critique
(`designs/audit/2026-06-28-social-contest-deliberation-critique/critique.md`), whose §2.4 names
the gap precisely: **"no Type-3 procedure. RM and the Wardens are explicitly *consensus*
institutions and the Succession table even lists 'RM: by consensus' — but 'by consensus' is a
label that collapses straight back into the Mandate-weighted sigma vote. There is no unanimity
threshold, no single-actor holdout/veto move inside a contest, no sortition."** The critique's
proposed fix — a thin Consensus Proceeding with per-required-assenter sigma rolls, a lone holdout
minting a "Holdout" Obligation clock, and an anti-gaming antibody mirroring the existing Sacred
Veto self-interest cost — maps directly onto both the BG parliamentary vote's Mandate-weighted
pooling (`sim/personal/contest/faction.py coalition_vote`) and faction motions (a Church-style
Sacred Veto already exists at `faction_layer_v30.md §5.3`). This is filed as `caillois FG-3`
(medium) / `contest-locus FG-3` (high leverage) in the critique, not yet promoted to an ED number
in the ledger, and the Fable-5 audit's own sequencing (**P0 spec-reconciliation → P1 consequence
spine → Stage 4 four-games build → calibration**) explicitly defers the four-games/Consensus build
until *after* the consequence spine (ED-SC-0006/0007) lands — i.e., the repo's own roadmap already
puts §1's plumbing gap ahead of §2's Consensus-mode gap in priority. Confirming this from the code
side: `sim/personal/contest/wrapper.py`'s `GAMES` registry marks `"consensus"` `status: "STUB"`
(resolving to a placeholder function), and its `MECHANICS` entry cites its own source as
"`social_contest_v30 §10 BG-Vote / §7.2 (faction.py — Stage 4)`" — Consensus is planned as a
promotion of machinery `faction.py` already has, not a new engine, matching the Fable-5 handoff
note that "faction.py already has BG-Vote/Succession/committee-band → Consensus mostly
promote-existing." Today, though, `faction.py`'s `coalition_vote()` explicitly collapses N-party
coalition politics onto a two-pole engine ("COALITIONS pool onto the two-party engine — the
multi-faction case needs no N-party spine," its own comment), and even `succession()`'s RM
"by consensus" adjudicator entry resolves as a two-leader Persuasion-Track contest — so the actual
unanimity/holdout/veto structure the critique calls for does not exist anywhere yet, stub or
otherwise; "committee" and "cold equilibrium" are inert sinks standing exactly where a
liberum-veto-style holdout move belongs.

### 2.6 What the aggregate-stats model structurally needs, and what's missing to supply it

Per AU-1/AU-2's own worked table (propagation_spec_v1.md, channel (i)/(ii)), a personal-scale
contest outcome should aggregate up via exactly two channels: a **settlement-locus stat write**
(ΔOrder, ΔL, ΔPS at the settlement where the scene occurred, deferred-apply at the ACCOUNTING_
BOUNDARY) or a **decaying national-event-modifier Key** read at the next Mandate derivation. Both
channels are architecturally specified and neither is populated by any live contest resolution
path today — because (a) no live contest happens at settlement scale at all (§1.3), and (b) the
one live faction-scale contest (Stability Crisis) never populates the `echo` context block that
would let `echo_transport.py` emit either channel. The missing piece is not a new mechanism; it is
exactly ED-SC-0007's scope (map a Bout verdict → `compute_domain_echo` degree, per whichever
resolution ED-SC-0002 picks for the Debate→Echo keying fork) plus, for settlement-scale, an
`_emergency_council_parties`-shaped bridge keyed on `Settlement.order`/`.legitimacy`/
`.popular_support` rather than `Faction.L`/`.Sta`.

---

## 3. HISTORICAL PRECEDENT / POLITICAL GROUNDING

### 3.1 The source-research trilogy is explicitly, almost entirely, about institutional/faction-scale politics — not personal persuasion

`designs/audit/2026-06-28-social-contest-deliberation-critique/source-research/` is a five-document,
not three-document, set (`deliberation-as-game-synthesis.md`, `politics-as-deliberative-game.md`,
`renaissance-deliberation-and-the-classical-inheritance.md`,
`renaissance-machination-games-lens-and-review.md`,
`renaissance-testing-the-model-and-closing-findings.md`). Reading the two central installments
directly:

- **`renaissance-deliberation-and-the-classical-inheritance.md`** is a synthesis of how Renaissance
  *political bodies* — the Great Council and Senate of Venice, the Signoria and *consulte e
  pratiche* of Florence, the conciliar movement's General Councils (Pisa, Constance, Basel) —
  deliberated and decided. Every named theorist and institution is **institutional/collective-body**
  material, not personal persuasion: Aristotle's tripartite constitution (deliberative/magisterial/
  judicial elements of a *regime*), Polybius's mixed constitution (Rome's consuls/Senate/assemblies
  as a stability theory for *states*), Cicero's *res publica* (the commonwealth as partnership),
  Roman/canon corporation law (the *universitas*, majority and qualified-majority voting, *quod
  omnes tangit*), Bartolus's *civitas sibi princeps* (city-as-legal-sovereign), Marsilius's
  *valentior pars* (the legislative community), and Nicholas of Cusa's conciliar consent theory. The
  document's own central finding (Part IV.1) is that classical philosophy structured
  *legitimation and self-description* of these institutions "far more… than institutional design,"
  and that the deep procedural substrate — corporate majority voting, qualified majorities,
  representation — is Roman-**legal**, not philosophical. This is source material for
  **faction/institutional-scale governance bodies**, full stop; nothing in it concerns a single
  orator's private persuasion of one other person.
- **`politics-as-deliberative-game.md`** classifies thirteen pre-1600 political decision-*models*
  (autocratic fiat, sortition, divination/augury, acclamation, council deliberation, assembly
  democracy, consensus/unanimity, parliaments and estates, election by electors, hereditary/
  elective-kin succession, trial by combat, arbitration/adjudication/appeal, competitive
  examination) against Caillois's agôn/alea/mimicry/ilinx typology. Every single model is a
  procedure for **a collective body or an office** deciding something — succession, legislation,
  treaty ratification, a papal election — never an interpersonal argument. This is the document
  that names **Putnam's two-level game** (in its Parliament/estates entry, model 8: crown-versus-
  estates bargaining as a mixed-motive game with a win-set), the **liberum veto** (model 7,
  Consensus/unanimity, "the extreme case" of a holdout defeating an entire assembly), and — via
  its own bibliography (confirmed by grep of the sibling `renaissance-machination-games-lens-and-
  review.md`, source-ledger section "On sortition, mechanism design, and self-enforcing
  institutions") — **Dowlen's weighted-lottery scholarship** ("Sorting Out Sortition," 2009),
  cited alongside Florence's *squittinio*/*imborsazione* scrutiny-then-lot system and Venice's
  lot-and-ballot doge election.

**Every one of these citations concerns institutional/faction-scale politics, imported DOWN to
Valoria's personal-scale contest — never the reverse.** Cicero's rhetorical corpus (deliberative
oratory before a body that must decide) is the sole citation touching individual argumentative
technique, and even that is explicitly framed as "the theory of the *council speech*" — a
technology built for addressing an institutional deliberating body, not a private conversation.

### 3.2 Where that research actually landed in canon, and how far

The 2026-06-28 critique's own §5 ("Already designed, just stranded") and the ratified Fable-5 audit
confirm this research shaped the **shape of the plan** (four deliberative games — Agôn/Negotiation/
Inquiry/Consensus — the alea/mimicry/Type-3 gap analysis) but its "rich detail… is not yet in the
code" (per `handoffs/HANDOFF_SC.md` line 80–85, "SOURCE-RESEARCH GROUNDING" note, 2026-07-01): the
Panel adjudicator's weighted-by-standing ballot (ED-1057) and its Guild-Arbitration rebind
(ED-1059) are the two pieces of this research that *did* land as ratified mechanics — and notably,
**both are themselves institutional-body mechanics** (a bench of judges, not a single opponent).
The critique's own headline finding (§0, "Executive summary") states plainly: *"the contest is an
excellent build of one game — the agôn… almost every fix below reuses primitives you already
ship"* — i.e., the research argues Valoria under-built the *institutional*/bargaining/consensus
games this research is actually about, in favor of over-building the one-on-one duel game.

### 3.3 The Panel/Guild-Arbitration research (ED-1057/ED-1059) is the clearest single data point

`designs/audit/2026-07-01-contest-gate-b-packet/GATE_B_packet.md` §2.2–2.3 and its closeout audit
confirm: ED-1057 (Panel aggregation = **weighted-by-standing**, reusing the existing
`Adjudicator.discipline` bench-rank primitive, explicitly *not* a contestant-side Standing
concept) and ED-1059 (Panel reachability = **rebind Guild Arbitration's adjudicator from Expert
Judge to Panel**, explicitly rejecting an appeals mechanism — *"appeals should not be a thing —
let the decision ride"*) are both, transparently, institutional-body-voting research (a seated
bench of guild masters deliberating to a weighted ballot) imported to make a *personal-scale*
contest type (Guild Arbitration, one of the 8 §2 proceedings a player-character can enter)
behave like the historical institution it's named after. This is the trilogy's central thesis
made concrete in a single ratified mechanic: institutional/faction-scale deliberation research,
scaled down to resolve a personal-scale scene.

### 3.3b The dyadic-argument minority strand, for honesty's sake

Not everything in the research trilogy is institutional. `deliberation-as-game-synthesis.md` (the
parent document the other two presuppose) also draws on genuinely **personal-scale, two-party**
argumentation theory: Hamblin's commitment-store model (1970), Walton & Krabbe's six dialogue
types (1995, including "persuasion" and "negotiation" as dyadic types), and pragma-dialectics
(van Eemeren/Grootendorst — a fallacy as a "foul" within an argument between two arguers). This is
the strand that actually grounds exchange-level mechanics like Recall citations, the Doubt Marker,
and the (still-unbuilt) commitment-store critique finding in §2.5 of the deliberation critique. It
is real, and it is the substrate for the *moment-to-moment* exchange math — but it is the minority
of the corpus by volume and the *frame* the trilogy argues from is institutional throughout: the
2026-06-28 critique's own headline (§0) is that personal-scale agôn is "an excellent build of *one*
game" and the fixes it proposes are, almost without exception, importing institutional-politics
structure (capture, forum-shopping, two-level win-sets, sortition, consensus/holdout) back into
that engine — never the reverse.

### 3.4 The 2026-04-28 political-dynamics session: earlier, and the same direction — but aimed the other way institutionally

`designs/audit/2026-04-28-political-dynamics-session/02_initial_proposals_with_historical_
precedents.md` predates the deliberation critique by two months and is explicitly a **faction/
settlement**-facing document — its own scope statement (`00_session_index.md`) frames the entire session as
**"Interpersonal → Political Dynamics: Gap-Fill Proposals"** — explicitly investigating "how
interpersonal relationships operate in Valoria and how those dynamics radiate through …
settlements, governance, and faction politics." Its historical precedents are Curia Regis
inner-circle rivalry, medieval court precedence/patronage (Medici-court seating and speaking order
as political signaling), Venice's Council of Ten three-channel intelligence apparatus (mapped
directly onto a proposed Intel/Influence/Subversion tier system for faction-level intelligence
operations), and Cardinal-Governor papal/secular tension (mapped onto the settlement
Bishop-Governor mechanic, already partially canonical at `settlement_layer_v30 §3.2`). Its proposal table (lines 295–299)
explicitly routes each historical precedent to a **faction-AI/settlement-stability** mechanical
home (faction AI, Exposure/Disposition, Intel stat, Settlement stats/Stability, companion/
settlement-governance) — none of it targets personal-scale contest resolution. So the 2026-04-28
session's historical-precedent lineage runs the **same direction** as the later trilogy
(institutional/political-science precedent → faction/settlement mechanics), just landing one tier
higher (faction AI and settlement stat design) rather than at the personal-scale dice contest.

### 3.5 The lineage claim, answered directly

**Valoria's social-contest system was designed, by its own research lineage, as a personal-scale
zoom-in on institutional/faction politics — not as a self-contained personal drama engine that
faction/settlement politics were retrofitted onto later.** The evidence for this is unambiguous
and runs in one direction across every source examined:

- The system's *own* commissioned research (`renaissance-deliberation-and-the-classical-
  inheritance.md`, `politics-as-deliberative-game.md`, both dated into the 2026-06-28 critique)
  is, almost without exception, about how **institutional bodies** (councils, parliaments,
  conclaves, successions, arbitration panels) legitimately decide — Venice's Great Council/Senate,
  Florence's Signoria/*pratiche*, the papal conclave, the Mongol *kurultai*, Gaelic tanistry, the
  Iroquois Grand Council, the liberum veto. Personal one-on-one persuasion appears in this
  research only as the deliberative-*oratory* register **used inside** those institutional
  bodies (Cicero/Aristotle's council speech) — never as its own subject.
- Every mechanic this research demonstrably produced in ratified canon — Panel's weighted-by-
  standing ballot (ED-1057), the Guild-Arbitration rebind (ED-1059), the Succession Contest's
  faction-split ratios (§7.2.1, itself independently dated to ED-762/ED-665, predating the
  2026-06-28 trilogy but structurally identical in kind — an institutional succession-crisis
  procedure), the BG-Vote's Mandate-weighted pool — is a piece of institutional/collective-
  decision machinery, wearing the personal-scale contest engine (Argue pool, Persuasion Track,
  exchange structure) as its resolution substrate.
- The earlier 2026-04-28 session shows the same institutional-politics research vocabulary
  (Council of Ten, Cardinal-Governor tension, court patronage) being aimed at faction/settlement
  *stat design* two months before the contest-specific trilogy existed — i.e., historical-
  institutional research was already the house style for faction/settlement mechanics before it
  was ever brought to bear on the personal-scale contest at all.
- Nothing in any of the three research documents examined argues from a *personal drama* premise
  outward to faction politics. The direction is institutional-politics-research → personal-scale
  contest-mechanic, consistently, across both the earlier and later research waves.

The retrofit reading is therefore backwards: the interface debt documented in §1 (a contest that
resolves and touches nothing) is not evidence the system started as personal drama and faction
politics was bolted on after — it is evidence that the **research was always aimed at the
institutional/faction interface**, and the **engineering** of that interface (the context-
derivation bridge, the echo-keying decision, the settlement registry) is what lagged, and still
lags, behind both the design intent and the research that grounds it.

---

## Overall synthesis

**Current depth of interface: thin, with one exception that is itself disconnected.** The design
prose (§1.1) declares dense, specific settlement- and faction-facing consequences for contest
outcomes — Mandate shifts, faction splits, settlement-targeted Obligations, Accord echoes. Almost
none of it has ever been executed by running code. The single genuinely live contest→faction path
(Stability Crisis, closed 2026-07-08 by ED-SC-0006) resolves a real verdict through the real
kernel and then discards it by construction, because the outcome→echo mapping (ED-SC-0007) is
explicitly out of scope pending a P0 design fork (ED-SC-0002). The single complete, tested,
*mutating* path (`parliamentary_vote.py`'s Mandate write) is not reachable from the campaign loop
at all. No settlement-scale contest exists in any form beyond an unfired trigger name and an
unratified proposal doc.

**The gap between what the research argues for and what is built** is large in engineering terms
but narrow in design-intent terms: the research (§3) has always pointed at exactly the
institutional/faction interface the architecture (§2) says is structurally required (propagation_
spec_v1's AU-1 aggregate-up rule, AU-5's named seam) — the gap is that neither the party-derivation
bridge nor the echo-keying decision nor the settlement-scale trigger evaluation has been built out
to match either the research or the doctrine. This is a closeable, already-scoped gap, not an
open design question.

**Highest-leverage next step — already tracked, not invented here.** The ledger and lane handoff
are explicit and current: **ED-SC-0007** ("Bout outcome → domain_echo wiring," `canon/editorial_
ledger.jsonl`, status `open`) is the P1 consequence-spine item that closes exactly this gap for the
one live trigger — it is "mechanically unblocked (contests now resolve) but still spec-blocked on
the ED-SC-0002 echo-keying fork" (`handoffs/HANDOFF_SC.md`, "NEXT" section, lines 117–121). ED-SC-
0002 itself (the Debate→Domain-Echo keying conflict — band-keyed per `scale_transitions §5.4` vs
genre-keyed per `social_contest §6` vs composed) is the **P0 decision docket item awaiting Jordan's
pick**, and is the actual highest-leverage single action available: one ruling on ED-SC-0002
unblocks ED-SC-0007, which — per the propagation spec's own AU-5 wiring contract — closes the
identical seam this whole report has traced through doc, code, architecture, and research lineage.
Everything else identified in §2 (settlement-scale trigger evaluation, the Faction-Leader-Removal
and Rank-Advancement bridges, the Consensus/Type-3 mode, a settlement-scoped `_emergency_council_
parties` analogue) is downstream of the same shape of fix and is already sequenced *after* the
consequence spine in the Fable-5 audit's own ratified ordering (P0 → P1 consequence spine →
Stage 4 four-games build → calibration).
