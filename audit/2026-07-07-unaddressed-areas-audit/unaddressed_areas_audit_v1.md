# Valoria — Unaddressed-Areas Comprehensive Audit v1

## Status: RATIFIED-AS-ACCEPTED 2026-07-07 (Jordan: "ratify all", consolidated ruling pass — ED-IN-0026; the 11 confirmed findings U-1..U-11 stand as delivered, `ed_options.md`'s 17 candidates are now filed EDs, see its Disposition table)
## Date: 2026-07-07 · Lane: IN (cross-cutting) · ED anchor: ED-IN-0017 · Branch: `claude/fable5-audit-coverage-gaps-22nz7i`
## Companion deliverable: `designs/architecture/key_echo_armature_v1.md` (ED-IN-0018 — deliverable 2, drawing from this audit's findings)

**Charter:** `00_grounding/00_charter.md` — every area the 2026-07-07 coverage review found
unaddressed by last week's Fable 5 audits, plus Jordan's same-day additions (pessimistic NERS
review, pessimistic diagnostic resolver review) and the directive that every cluster's Honest-gaps
section be addressed (`00_grounding/02_honest_gaps_disposition.md` — the per-gap accounting).

---

## §0 · Corpus verdict (verdict-first)

> **The design corpus and the running oracle are two different games, and every prior verdict
> conflated them.** Last week's audits judged the *design* — and the design mostly holds. This
> audit judged the *unaddressed remainder*: the running reference implementation, the subsystems
> no lane ever read, the seams no cluster ever covered, and the prior audits' own verdicts under
> a pessimist prior. The result is consistent across all fourteen clusters: **the campaign loop
> as executed is faction-territory accounting plus a conquest roll — nothing else fires.** The
> faction oracle implements a superseded stat model; threadwork, knots, fieldwork, contests,
> NPCs, settlements, injectors, and articulation are built-but-unreachable islands or stubs; the
> one victory gate that reads a world clock reads one nothing writes; the celebrated ~87%
> win-share degeneracy is a small-n artifact riding a real elimination trap; and a recurring
> class of **ruled-but-unexecuted** decisions (ED-871, ED-912's propagation, fork-2, fork-11,
> ED-SE-0001's own anti-orphaning order) shows ratification outrunning execution as a standing
> process failure. None of this contradicts the prior audits — it completes them: the seams are
> not just silent (#81's verdict); below the seams, most of the transport the silence was
> measured against does not exist yet. That is precisely what the companion armature
> (ED-IN-0018) now specifies and begins to build.

## §1 · Method + model/adversarial provenance (Jordan confirmation record)

Relay pattern (ED-1083) throughout — producers, antagonists, and critics structurally
independent; every carried P1/P2 class re-verified by refuters who saw claims + charter only.

| Role | Adversarial stance | Recommended tier (CLAUDE.md §10) | Used |
|---|---|---|---|
| 11 evidence clusters (C-REACH, C-KEY, C-FI, C-TW, C-NPC, C-SIG, C-INJ, C-STUB, C-EMERGE, C-MBSE, C-VERIFY) | Agonists (read-only, barred from verdicts; C-EMERGE null-hypothesis stance; C-TW/C-FA exploit arenas; C-SIG exploit-hunter + numeric verifier) | Sonnet | Sonnet |
| C-FA (accounting-math synthesis) | Agonist, judgment-heavy | Opus | Opus |
| **C-NERSPESS** (Jordan directive) | **Antagonist** to #77's verdicts — pessimist prior, unevidenced attacks dropped as UNSUBSTANTIATED | Opus | Opus |
| **C-RESPESS** (Jordan directive) | **Antagonist** to the resolver stack — Phase 0–6 diagnostic under pessimist prior, unreproduced numbers dropped | Opus | Opus |
| R1–R5 refuters | **Antagonists, relay-independent** (claims + charter only; refute-by-default; intent gates) | Sonnet | Sonnet |
| G1–G4 gap-closure | Verification probes (ablation, n=100, runtime executions, doc closures) | Sonnet | Sonnet |
| Armature critic | **Antagonist** to the ED-IN-0018 draft (relay; primary canon only) | Opus | Opus |
| Orchestration · all verdicts · this report · armature authorship · fork-docket defaults | Judge (doctrine-designated Fable nodes) | Fable | **Fable 5** (this session) |

Funnel: 14 dossiers → ~120 tagged findings (`finding_status.md`) → carried P1/P2 classes through
5 refuters + 4 gap-closure agents + a full gauge re-run → **1 finding killed outright (C-FA-7)**,
**3 qualified** (C-FA-1 "nowhere" wording; C-TW-12 attribution ED-773-not-PP-632; C-EMERGE-1
lockout ~99%-not-absolute at n=100), **1 retired as unresolvable-rhetorical** (the
convergence-marker "misrepresentation" item), **2 upgraded** (CI-75 unpropagated supersession;
C-KEY-9's core-five reclassified DELIBERATE-by-architecture), the rest **CONFIRMED with intent
gates**. Refutation records: `01_workings/refutations/`.

## §2 · Confirmed findings (P1 class, severity-ranked; refuter-verified)

**U-1 · The faction oracle implements the pre-LPS-1 superseded model** `[C-FA-1 · R2 QUALIFIED-CONFIRMED · NOT-INTENDED]`
`sim/` Faction = {L, Sta, W, I, Mil}; no Mandate (the sim aliases scalar L as Mandate —
`parliamentary_vote.py:13`, `crown_initiative.py:135`), no working per-settlement L/PS (an inert
schema stub exists in `territory/registry.py` — R2's qualification), no Treasury accrual, no
α/β/γ dynamics, no da.* Key plumbing. The scalar-L model is the exact defect LPS-1 resolved
(2026-05-30). Every downstream balance claim inherits this. (The λ-formula sub-claim was
REFUTED — G2: fully quantified at `faction_behavior_v30.md:290-297`.)

**U-2 · The campaign loop is the sole universe of execution, and it reaches almost nothing**
`[C-REACH matrix + C-EMERGE-4/7 + C-TW-1 + G1 gap 6 · R3 CONFIRMED · mixed intent]`
ORGAN-grade: mass battle, CI/MS/insurgency accounting, Crown/Church unique actions, victory.
ISLAND/STUB: contest kernel (100% deferral, 151/151), threadwork (entire package, zero callers,
zero tests), knots, parliamentary cluster, settlement layer + temperaments, fieldwork/
investigation (6 stubs), companion/tribunal, articulation (3 stubs), npc_ai, injectors. NPE runs
every season over a permanently-empty store (`generate_npc` has zero call sites). Nine World
registries are unreachable from the loop's import graph. No other executable entry point exists
repo-wide. The dispatch narrowing is DELIBERATE-documented; the test-coverage absence and the
producer-never-called patterns are NOT-INTENDED.

**U-3 · Live contests resolve through the deprecated raw-dice stub; the promoted σ-kernel has
zero live callers** `[C-RESPESS-2/3 · R2 CONFIRMED (DELIBERATE staged interim) · exposure dormant]`
`scene_dispatch.py:106` → `contest_legacy_stub.run_contest` (bare opposed d10, floor 1,
tie→first-speaker); `module_contracts.yaml:429` still declares `dice_pool`. The two formulas
diverge 9.5–28.9pp (R2's independent 200k-roll probe); the kernel is History-invariant and
wound-blind. G1 quantified exposure: ~7.6 queued contest scenes/campaign, currently 100%
deferred — the defect goes live the moment the derivation bridge closes. Fold into
ED-SC-0006/0007 acceptance criteria (OPT-11).

**U-4 · The degeneracy story, corrected end-to-end** `[C-EMERGE-1/2 + C-FA-4/5 + G1 ablation ·
R1: 6 CONFIRMED, 1 QUALIFIED · compound causality adjudicated]`
The "~87%" is a small-n artifact — R1 traced its provenance to the 06-30 ecosystem review's
`run_batch(8, seed=42)` (87.5%, reproduced exactly) and it propagated unchallenged into ≥5 docs
(n=16 seed 0: 44/44/12/0; **n=100: Varfell 56 / Crown 36 / Church 7 / Hafenmark 1**).
Hafenmark's ~99% lockout is the one-way elimination trap (0-territory factions never act again;
the only restoration module, parliamentary_transfer, is never called — KNOWN-TRACKED via
ED-SC-0007 per R1). **R1 corrections:** the Mil=3.0-floor framing is not load-bearing (Mil never
decreases in sim), and the single n=100 Hafenmark win came from AVOIDING the trap (min territory
1), not escaping it. Intent UNDETERMINED: the collapse-recovery ruling (Tainter) makes
zero-territory-terminal philosophically defensible, but its own Reconstitute mechanic was never
implemented and the Varfell/Hafenmark block is an acknowledged incompleteness. The
Crown/Church wiring asymmetry (C-FA-4) is real but **not sufficient**: G1's ablation removed it
and Hafenmark stayed at 0% while the winner inverted — the ablation itself exposed a second
confound (the unique-slot roll falls through to extra Conquest frequency). The snowball's motor
is season-over-season uncapped Muster accrual, not battle-function sensitivity (G1: the battle
function is concave/saturating). Sequencing note for tuning: fix trap + accrual before reading
any win-share as balance signal.

**U-5 · The Turmoil victory gate is permanently vacuous** `[C-REACH-5 + C-NERSPESS-3 · R1
CONFIRMED (empirically: 0.0 all 50 seasons; canon §4 fully specifies the mechanics — CI/MS got
track modules, Turmoil never did; NOT-INTENDED) · needs_jordan (touches GD-1) — OPT-4]`
`victory.py:73` gates GD-1's "Political Stability ≤ 6" on `world.clocks['Turmoil']`, initialized
0.0 and never written anywhere in `sim/`. Two-of-three victory legs functional. Compounding:
"PS" in code = Political Stability; "PS" in canon = Popular Support (C-FA-3).

**U-6 · Ruled-but-unexecuted is a standing failure class** `[C-VERIFY-13/16 + C-TW-2/12 +
C-FI-5/6 + C-INJ-4 + C-NERSPESS-4 + R3/R4 CONFIRMED · NOT-INTENDED]`
ED-871 (Mending cost 0, ruled 2026-05-31) — the ordered doc fix never landed; the sim charges
−1/−2 (G3 executed the code to confirm). ED-912's knot resolution propagated to one of four
sites; `knots_v30.md` contradicts itself; `mechanics_index` still carries the struck model;
`sim/personal/knots.py` runs the superseded accumulator (ED-773-attributed capacities — R3's
correction). Fork-2 (ARC-T04 strike) ratified, unexecuted. Fork-11 ratified; the contract entry
still reads `[OPEN — Jordan]`. ED-SE-0001's own anti-orphaning instructions (CURRENT.md row +
HANDOFF_SE item) were never executed — F-1's failure mode recurred live after its remediation.
**Upgraded by R4:** `conviction_track_v30.md` still runs the CI-75 model that
`ci_political_v30.md` §0 self-documents as superseded — including a Church victory condition
keyed to "CI 75" — an unpropagated supersession missed by the doc's own supersession markers.

**U-7 · The Key/echo transport layer exists only as prose** `[C-KEY-1/4 + C-INJ-11 · R4
CONFIRMED · the armature's mandate]`
One of 19 state-mutating modules has doc-native emit clauses; zero `class Key`/`emit()`/key-log
exists in `sim/` (closed by this PR's `sim/substrate/`); causes[] has zero executable instances
and one authoring-guidance doc corpus-wide; the §12.4 down-seam families have no substrate to
populate targets[] into; §4.3.3 has no code path (dangling constant); `scene_slate` consumes
nothing by contract, so no Key can reach the scene queue; a CANONICAL articulation trigger cites
an unregistered type (`meta.cascade_cluster_event`). The 48-row registry×rendering sweep
(C-KEY Part 4, adopted as armature §2.5 data) reproduces EP-3's ratified "10-of-44" exactly and
extends it: the core-five's generic routing is DELIBERATE architecture (R4), but
`state.opinion_revised` and `meta.miraculous_event` carry self-descriptions their own tables
contradict, and miraculous_event has no path to a player under any implementation (R4 claim 7).

**U-8 · The resolver substrate diverges at its band boundaries, and two more live kernels exist
than anyone knew** `[C-SIG-2/3/4/5 + C-RESPESS-1/6/7 + G3 gap 7 · R5: 2 CONFIRMED exactly, 2 QUALIFIED with corrections]`
ER-2's continuity correction exists in combat's private degree() only — identical `net` bands
Success in combat, Partial in contest, live at both kernels' 5D floor (R5 reproduced: 2.7 vs
Ob 3 → success/Partial split; intent NOT-INTENDED, params/core.md states the correction is
general). Combat's fixed 2·Ob Overwhelming bar saturates with pool — **R5 correction: the
reachable ceiling is History 7 → pool 13 → 45.9% Overwhelming at parity (vs ~6% at pool 6); the
originally-quoted 73% endpoint assumed History 13, outside the documented 1–7 stat range.** The
saturation trend stands (the de-saturation fix contest got was never ported back — §5.12 fork);
the magnitude is the corrected 6%→46%. The armature-doc uniformity proofs are built on a
function no live kernel calls (R5: 3.445pp divergence on the doc's own worked example,
reproduced to the third decimal). The domain resolver's two legal difficulty derivations diverge
10pp on odd stats **pre-clamp (R5 qualification: ~6 of 28 odd-target cells clamp to 0–5pp at the
FLOOR/CAP extremes)** and flatten to 5% at Ob≥8 — though G3 sharpened reachability: the
Three-Axis Ob formula's Breadth/Distance axes are silently dropped in code (live ceiling Ob 13,
design intends exactly 20). G3's broader hunt found a **fifth and sixth live kernel**: the
faction d6 threshold kernel (in the campaign loop) and the contest Gaussian jury model — plus an
intra-file d10 duplication in massbattle with zero parity coverage (C-SIG-2).

**U-9 · The pessimist reviews landed real downgrades on the optimist record** `[C-NERSPESS-1/2/3/5/6 · R5 CONFIRMED (claims 6/7/8, incl. the golden's well-formedness test passing a hypothetical 100/0/0/0)]`
Ω(c) "autonomous world, verified under attack" fails operationally (stub trees; the vote-rule
refutation rests on a field never assigned; the regression golden enshrines the degenerate
attractor). Ω(b)'s five transformation channels are all campaign-unreachable. Ω(d)'s hunt
survived partly on safeguards that are doc-only or vacuous in sim (Turmoil). Two intent
attributions in #77 §7 are unsound: R-1 is circular (ED-PC-0001 cites the audit as its own
source) and R-2 contradicts the audit's own refutation record (UNDETERMINED published as
DELIBERATE). The pessimist discipline held: seven attacks dropped as UNSUBSTANTIATED, including
confirmations that cr5 wiring, GD-2's ratified intent, and the articulation row were accurate.

**U-10 · Mass battle: the gauge is now fully measured and the overshoot is general**
`[C-MBSE + this session's full run · gauge data archived]`
Multi mode 6/20 pass (single 2/20, mass-UNRESOLVED). The WIN-OUT overshoot extends beyond
composition rows to plain formations (H2 wedge-vs-line 100% vs 48–62); H10/H11 measured for the
first time (symmetric enveloper overshoot); R3-row unresolvable in 20 turns; C4/C5 marginal.
DG-2 is double-gated (RC-1 stability + the new partition-invariance question). The §D aftermath
apparatus — the corpus's best-integrated seam on paper — is 0% implemented, and Stage E's MVP is
a dev visualizer, not a player surface (first-ever MB playability verdicts: MISSING).

**U-11 · Process findings this audit generated about its own machinery** `[G4 + C-VERIFY-17]`
ED-IN-0012/0013 are each double-allocated in the merged ledger (lines 597–600) — the same-lane
collision the lane-tag namespace was built to prevent, recurring via two same-day "ratify-all"
batches; renumber docketed needs_jordan (armature §5.10; registry counters repaired this PR).
The canonical key-type registry has exactly one strict-YAML parse failure (scene.gossip). The
freshness gate passes 133/133 (the SessionStart "currency drift" banner traces to
currency_consistency_check items, not stale pins).

## §3 · Cluster index (dossiers + spot-verdicts)

| Cluster | One-line verdict | Dossier |
|---|---|---|
| C-REACH | 4 organs, everything else island/stub; routing census: one live scene type | `01_workings/cluster_C-REACH.md` |
| C-KEY | Transport census + the 48-row sweep (armature §2.5's data) | `cluster_C-KEY.md` |
| C-FI | Head conflict enumerated + 3 adjudication options; knots propagation fracture (P1) | `cluster_C-FI.md` |
| C-TW | First dedicated threadwork audit: total island + 12 code-vs-canon defects | `cluster_C-TW.md` |
| C-FA | Oracle on superseded model; degeneracy mechanisms; exploit arenas | `cluster_C-FA.md` |
| C-NPC | GAP-5 deepened (most of the engine has no oracle to check); 449-finding triage prep | `cluster_C-NPC.md` |
| C-SIG | Cross-kernel band divergences; bound verifications; exploit hunt | `cluster_C-SIG.md` |
| C-INJ | Injectors unreachable end-to-end; diagonal census (zero executable instances) | `cluster_C-INJ.md` |
| C-STUB | The ~19/~8 sets first enumerated; stub × milestone map | `cluster_C-STUB.md` |
| C-EMERGE | Seeded batches + ablations; F7 oracle spec; null-hypothesis verdicts | `cluster_C-EMERGE.md` |
| C-MBSE | RC-5 triage prep + first MB playability pass + keying census + deck readiness | `cluster_C-MBSE.md` |
| C-VERIFY | 32-candidate backlog closed: 24 confirmed · 7 refuted · 1 unresolvable | `cluster_C-VERIFY.md` |
| C-NERSPESS | Pessimist NERS: 3 P1 downgrades carried, 7 attacks dropped | `cluster_C-NERSPESS.md` |
| C-RESPESS | Pessimist resolver diagnostic: 7 reproduced breaches | `cluster_C-RESPESS.md` |

## §4 · Honest-gaps disposition

Per Jordan's directive, all ~70 recorded Honest-gaps entries are dispositioned in
`00_grounding/02_honest_gaps_disposition.md`: **26 CLOSED-BY-PROBE** (G1–G4, the full gauge run,
runtime executions), **11 COVERED-BY-SIBLING**, **14 ABSORBED-BY-METHOD** (refuter/verdict
stages), **~17 INHERENT/DEFERRED with named owners** (play-testing, post-PR-2 measurements, the
OPT-12 triage ED, the still-scheduled narrative-v2 audit). No gap was left silently open.

## §5 · Still-scheduled (named so nothing is silently dropped)

Narrative-engine v2 independent strong-critic audit (own session; defender/steelman pairing) ·
post-R3 PC re-hunt (trigger: U9/T5 landing — R3 is U0-only today) · full emergence audit
post-Stage-2.5 · P3-lite human-plays harness (SC lane; the corpus-wide paper-walk gap) ·
GO/port-seam audit (**deferred by ruling** — trigger Gate-0; recorded in HANDOFF_GO) ·
engine_clock ratification (ED-1051, a ruling not an audit).

## §6 · Relationship to deliverable 2

The armature (`key_echo_armature_v1.md`, ED-IN-0018) is this audit's constructive half: §2's
Echo Matrix rows cite these findings; §3's registry deltas come from C-MBSE's keying census +
C-KEY-8; §4's A13–A16 checks mechanize the C-KEY-1/-6/-10 classes; §5's docket consolidates
every needs_jordan fork either deliverable surfaced; §6's substrate closes U-7's "no executable
Key substrate" as of this PR. `ed_options.md` (17 candidates, unfiled) is the work menu.

## §7 · Bottom line

The prior audits were right about the design and silent about the machine. The machine, measured:
one live scene type, zero echoes delivered, a superseded faction model, resolvers that disagree
at their own floors, and a ratification pipeline that outruns execution. None of the P1s here
requires new game design: they require the oracle brought to canon (OPT-1), rulings executed
where they already exist (OPT-5/6/8/16), the trap and the accrual capped before balance is read
(OPT-2), and the transport layer built — which the armature now specifies and this PR's substrate
begins. The good news is equally concrete: the corpus's guardrails caught almost everything at
the design layer (the refuters confirmed the prior audits' accuracy wherever they were attacked
on facts), the ORGAN-grade paths (mass battle, accounting, victory) prove the loop can host real
mechanics end-to-end, and every silent seam now has a contract row, a checker, and an owner.
