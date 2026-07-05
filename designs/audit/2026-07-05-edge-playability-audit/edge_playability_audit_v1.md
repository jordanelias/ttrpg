# Valoria — Edge-Playability Audit v1 (every seam, every scale, every direction)

## Status: PROPOSED (audit findings — Jordan review)
## Date: 2026-07-05 · Lane: IN (cross-cutting) · Branch: `claude/fable5-playability-audit-y5wj43`

**Charter:** `00_grounding/00_charter.md` — the seam is the unit of analysis; the question at every
edge is whether the *crossing itself* is good gameplay (moment · decision · feedback · latency ·
friction · reciprocity), not whether the plumbing conforms. Complement to the 2026-07-04 NERS
audit (PR #77), whose F-1..F-5/S-1/S-2 and KNOWN list are inherited as calibration.
**Method:** Fable orchestrator + 8 sonnet evidence clusters over the edge inventory
(`00_grounding/01_edge_inventory.md`, ~60 edges from the module-contract spine, the eight
`scale_transitions` handoffs, the Domain Echo family, the Zoom trigger tables, and the rendering
layer). Every headline claim was independently re-verified by the orchestrator
(`01_workings/verification_log.md`, V1–V22); two agent "NEW" claims were reclassified
KNOWN-TRACKED (R1: ED-1010; R2: propagation-spec D.6), two were narrowed (R3, R4), one was
strengthened (R5). Full dossiers under `01_workings/cluster_*.md`.

---

## 0 · Corpus verdict (verdict-first)

> **The seams are the old GM's chair — and the chair is still empty.** Where a subsystem hands off
> to a sibling inside a scene, the crossings are designed and mostly play well: the TTRPG heritage
> built those seams by hand (evidence-into-contest, loud-combat-into-exposure, thread-into-debate).
> But at every seam where a human GM used to do invisible work — deciding that a personal act had
> faction scope, granting the bonus scene a Survey earned, picking the "most relevant unit,"
> narrating why the market closed early, warning "your companion won't forgive this," answering
> "why did that settlement fall?" — the corpus either still says "GM" outright
> (`scale_transitions_v30.md §3.2`), leaves the section header empty (§6.1/§6.3), or specifies the
> mechanism and no experience. The result is a consistent shape across all eight clusters:
> **consequence crosses, but the crossing is silent.** Bottom-up transport is specified but
> unsurfaced; top-down transport renders the eight mandatory crises well and almost nothing else;
> the rendering gate covers 10 hand-picked cases out of a 44-type registry; and the board-game
> layer that every strategic seam terminates in has drifted measurably behind ratified canon.

Tier summary across the ~60 audited edges:

| Tier | Seam family | Aggregate verdict |
|---|---|---|
| Scene-lateral (combat/contest/fieldwork/thread) | fieldwork↔contest, thread↔contest, combat→fieldwork, leaps | **PLAYS-WELL** — the corpus's best seams; exception: everything touching combat's thread interface (ED-911) and combat↔contest reciprocity |
| Bottom-up (scene→faction) | Domain Echo family, Sufficient Scope, consumption | **Specified-but-silent** — mechanics sound, zero current-generation feedback surface; the cap/tie-break/failure rules are invisible |
| Top-down (strategic→personal) | 8 mandatory Zoom rows, world-state triggers, da.*/env delivery | **Half-built** — mandatory crisis rows mostly play well; enemy covert action and disasters never become play |
| Strategic lattice (faction↔settlement↔strain↔victory↔church) | Mandate loop, verbs, IP/CI/MS gates | **Engine-ready accounting, stranded presentation** — the best-written player-facing beats in the corpus cannot fire (unkeyed) |
| NPC/personal fabric | 2-cycle, gossip, memory, scars, knots, companions | **Deep state, sealed windows** — the world computes opinions of the player it is structurally unable to show them |
| Rendering seam | trigger table vs registry | **10-of-44 coverage** — whole families (scene_outcome, standing_change, env.crisis, settlement events) unrendered or unkeyed |
| Mode bridge & cadence | zoom, slate, accounting rhythm, BG params | **Strongest single spec (scene slate) sharing a folder with the weakest (empty mode-transition procedures, stale BG tables)** |

---

## 1 · Confirmed findings (P1 class — every one Fable-verified; EP = edge-playability)

Format: `[cluster · direction · intent]`, citations in the dossiers + `verification_log.md`.

**EP-1 · GM-era adjudication still occupies the seams of a GM-less game** `[I,C,D,B · all · NOT-INTENDED]`
The current CANONICAL skeleton answers "who decides the crossing?" with a GM at multiple
load-bearing seams: §3.2 "GM recognises faction scope" (the Personal→Faction trigger itself);
§6.1/§6.3 mode-transition procedures are empty headers with GM-era prose only in infill; the BG
Survey reward is "the GM **may grant** a bonus Personal Phase scene" (infill-only, and citing a
scene-budget the corpus has since superseded); §3.8's "most relevant unit" has no deterministic
selector; §4.3.2 row 3's low-Standing "may intervene" and all five §4.3.3 world-state rows name
options with no Ob, pool, or procedure. Each instance is small; together they are the single
largest playability liability this audit found, because they sit exactly at the crossings — the
places the engine, not a human, must adjudicate. `[V6, V19, V22; clusters I-E1/E5, C-E3/E10, D-E3]`

**EP-2 · The player's strategic verb menu does not exist as a designed surface** `[E · top-down · NOT-INTENDED (evidence-favored)]`
The `da.*` five-type family is an *after-the-fact outcome-classification schema* for
mission-alignment scoring — not a menu anyone picks from. The actual playable verbs are fragmented
across `params/bg/core.md` (card-hand + Ob table), `params/bg/faction_actions.md` (per-faction
actions), and the faction-layer resolver math, with `domain_actions` `doc: null` and its only
"spec" a PROPOSED audit-output file. An implementer building "the strategic turn" from the
contracts would ship an outcome tagger with no UI. This is the seam-level root under #77's
"faction seasons are mostly accounting output." `[V17; cluster E-E3]`

**EP-3 · The rendering gate covers 10 hand-picked cases of a 44-type registry — and the gaps
cluster on scene conclusions and deaths** `[G · outward · NOT-INTENDED for battle/combat (self-contradicted), UNDETERMINED for the rest]`
Extends F-4 into a family pattern: the **entire `scene_outcome` family** (battle, contest,
investigation, combat) is absent from the §3.1 Tier-2 gate — §6.4's claim that battle_concluded
"already triggers Tier 2" is false against the gate's own `matches_trigger_ruleset` mechanism;
`state.standing_change`, whose `trigger` enum literally includes `death`, has no trigger at all
(a quietly executed rival officer is never dramatized); `env.crisis` — war, plague, schism — waits
for the annual chronicle. The trigger table was built sim-first around what Stage 10 measured,
never swept against the registry. `[V7, V9; cluster G table + F-A/F-B/F-D]`

**EP-4 · Settlement events are unkeyed at the substrate — a blackout below even EP-3** `[G,E · outward/bottom-up · UNDETERMINED (no ED found)]`
Settlement Order/L-PS drift, revolt at Order 0, and undefended auto-capture emit **no Key of any
type**: the module contract's `g_ord0`/`g_def0` gates carry no emit clause, and
`settlement_layer_v30.md` never uses "Key" or "emit" (grep count 0). Unlike EP-3's families there
is nothing for Tier 1, Tier 3, npc_memory, or the causes[] graph to observe — the engine can never
answer "why did this settlement fall," for anyone, ever. (The §4.3.2 Settlement Revolt mandatory
Zoom covers only the player-present case, via slate state-detection rather than the substrate.)
`[V8; cluster G F-C]`

**EP-5 · The best-authored player-facing beats in the corpus cannot fire** `[E · top-down · NOT-INTENDED]`
`conviction_track_v30 §11` (bells ring longer, wildflowers return, Attention-Pool tells — a
finished GM-less presentation spec) and `victory_v30 §5.2`'s IP 60/80/90 Scene-Slate milestones
are stranded on modules with **zero Key integration** (`ci_political`, per its own contract note)
and an **unkeyed** era/occupation layer (victory §5; MS additionally an unowned clock with
mechanical Calamity-Drift thresholds but no narrated ladder, and the game's only true terminal —
Second Calamity — has the weakest approach-warning of any gauge). A human GM would ad-lib these
beats; the engine cannot. The prose is not the bottleneck — the emission path is. `[V18; cluster E-E6/E7/E8]`

**EP-6 · Enemy covert action against the player is invisible and unanswerable** `[C · top-down · NOT-INTENDED]`
`da.covert_betrayal` reaches the player only as a non-interactive cut scene and only when
`exposed == true`; `da.antinomian_action` and `da.economic_intervention` (whose nominal consumer,
`settlement_economy`, is a documented phantom) produce no player-perceptible signal at all. There
is no counter-espionage verb, scene, or investigation hook anywhere in the trigger tables: a rival
can drain the player's faction for seasons and the only evidence is a number on a sheet. An entire
genre beat — being moved against — has no play surface. `[V7; cluster C-E13]`

**EP-7 · The world computes an opinion of the player it is structurally unable to show them** `[F · lateral/outward · NOT-INTENDED]`
Two limbs, one defect. (a) The ambient fabric — `scene.interaction`, `scene.gossip` — is emitted
with hard-coded `private_observers: [npc_a, npc_b]` (six sites, including the visibility
defaults), so the player can never overhear gossip *about themselves* even standing in the tavern
where it happens, despite npc_behavior's own "the world's actors do not wait to be approached."
(b) The one specified revelation surface — npc_behavior §6.1/§6.1b "Appraise Revelation" — is an
empty header, and `npc_memory` is doc:null; a Contest win that promises "one Belief revealed" has
nothing to reveal it with. Between them, "the world remembers you" — the fabric the whole NPC
cluster exists to deliver — has no player-facing window. `[V13, V14; cluster F-E2/E3]`

**EP-8 · Investigation's conversational layer is canonical in name only** `[A · lateral · NOT-INTENDED (the doc's own integration table asserts wiring that is false)]`
Closes #77's GAP-1. `investigation_systems_v30.md` (CANONICAL, 2026-04-17) specifies a four-system
gated-dialogue layer whose own cross-system table claims Interview "now routes through Dialogue
Lattice + Response Matrix" — but the live fieldwork head still resolves Interview as one
Attunement roll, zero Lattice/Gate tokens anywhere in the fieldwork docs, and all three sim entry
points are `NotImplementedError` stubs. Compounding it, **fieldwork/investigation has no
CURRENT.md row at all** — the currency index cannot even arbitrate which of the two contradictory
docs is the head. `[V1, V2, V5; cluster A-E10]`

**EP-9 · Two canon texts give opposite answers to "does my governance stack with my governor's?"** `[B · bottom-up · UNDETERMINED]`
`scale_transitions_v30.md §5.5`: personal Accord Echoes "do **not** stack with faction-level
Govern actions in the same territory the same season — whichever produces the higher Accord
applies." `peninsular_strain_v30.md §2.7` (the CURRENT.md-listed head): personal-scale changes
and governor actions "**stack normally** … cap ±1 per source per settlement per season." Neither
cites the other; the Accounting step both point at (§7 Step 4c) resolves neither. The most basic
cooperative loop in the game — player and governor improving the same settlement — has an
undecidable outcome. `[V11; cluster B-E4]`

**EP-10 · The board-game layer every strategic seam lands in is stale against ratified canon** `[I · backwards/forwards · NOT-INTENDED; an S-1 (register back-propagation) instance]`
`params/bg/victory.md` still lists Varfell Path C "Thread Supremacy" (VTM = 5) — **struck** by
PP-663 in `victory_v30.md` — plus pre-PP-663 VTM/territory co-victory thresholds and a missing T13
gate; `params/board_game.md`'s navigational index is 100 % dead (16 `references/params_bg_*.md`
links, zero targets exist); `params/bg/phases.md` both dissolves and announces Hollow Victory in
one file and cites a nonexistent `designs/board_game/victory_v30.md`. A strategic layer built from
CURRENT.md's own "Board game" row would coach the player toward a dead victory path. `[V20, V21; cluster I-E8]`

**EP-11 · Bottom-up consequence is real but silent — the Echo has no voice** `[B · bottom-up · UNDETERMINED/NOT-INTENDED; quantifies F-3 at the seams]`
The Domain Echo family works on paper and is deliberately Accounting-queued (PP-109). But: the
1-Echo/scene cap and the seven-way tie-break are unsurfaced (the player cannot know which of two
qualifying acts "counted"); §5.2's Failure = −1 *to your own faction* is pre-warned in exactly one
of seven Sufficient-Scope conditions, and that one warning lives in the stale, off-index UI v4
doc; PC Faction Embedding (+1D, 1/season) has literally no authored presentation (bare infill
header); Thread Echo fires below the world's own narration threshold. Every feedback mechanism
this cluster found is in `valoria_ui_ux_v4*.md` — off-index, pre-d+σ, and (per V10) containing
zero coverage of the Why?/chronicle/Key-log surfaces that current canon *does* specify. The
contract side adds a genuine contradiction: `faction_behavior §5.2` (ED-936) denies direct
consumption of `scene.contest_resolved` while `module_contracts.yaml` lists it as consumed.
`[V10, V12; cluster B-E2/E5/E6 + findings 4–8]`

---

## 2 · P2/P3 register (verified; table = defect · seam · severity · intent)

| # | Defect | Seam | Sev | Intent |
|---|---|---|---|---|
| ep-12 | Ambush Exposure→Initiative payoff has no receiving field in combat_engine_v1 (F-TRANS-01 specifies an input nothing consumes) | fieldwork→combat | P2 | UNDETERMINED |
| ep-13 | Combat→Contest has no surrender/parley procedure; §9.6 resolves chamber violence as auto-forfeit, never a scene | combat↔contest | P2 | forfeit DELIBERATE; parley UNDETERMINED |
| ep-14 | 57 corpus citations (incl. the §4.3.2 row-8 "debt scene") point at the dead file `faction_politics_expanded_v1.md`; `module_contracts` `faction_politics` doc:null is stale — the CANONICAL 1,115-line home exists (PP-660) | faction_politics↔everything | P2 | NOT-INTENDED |
| ep-15 | "Knot Partner in Crisis" is mandatory yet has no Ob/roll/procedure — a forced scene with narration-only agency | strategic→personal | P2 | NOT-INTENDED |
| ep-16 | No pre-act warning before a Restricted thread op Scars a Knotted NPC and (if a Faith/Order/Equity companion is present) triggers no-appeal departure — the first tell is the departure scene | thread→conviction→companion | P2 | departure DELIBERATE; missing preview NOT-INTENDED |
| ep-17 | Contest↔NPC 2-cycle: in-scene stakes resolve now, durable behavior batches to Accounting — the distinction is drawn nowhere, risking all-persuasion-feels-inert builds | contest↔npc | P2 | UNDETERMINED (dampers already [OPEN—Jordan]) |
| ep-18 | Bonds≥5 chargen gate silently closes six cross-system payoffs for a whole campaign; knot strain has no exposed meter | knots↔everything | P2 | gate DELIBERATE; scope-awareness UNDETERMINED |
| ep-19 | §5.4 Debate→Mandate names "Piety Track" where thresholds match the Persuasion Track — the naming collision reaches faction math | contest→faction | P2 | NOT-INTENDED |
| ep-20 | Hybrid thread-op CI timing (§10) unreconciled with §5.3's immediate-vs-queued asymmetry — one action, two unexplained clocks | thread↔mode bridge | P2 | UNDETERMINED |
| ep-21 | No ceiling on simultaneous mandatory scenes — a pathological season degrades every discretionary slot to Witness Mode, recurrently | slate/budget | P2 | Witness valve DELIBERATE; cap absence UNDETERMINED |
| ep-22 | Scar crisis of a non-Knotted NPC (Disposition <+1) reaches no trigger at all while still cascading to faction stats | scar→player | P2 | UNDETERMINED |
| ep-23 | Mode-bridge cluster (scale_transitions, player_agency, fieldwork) has no CURRENT.md rows — the seams themselves are off the currency index | index | P2 | NOT-INTENDED |
| ep-24 | meta.thread_woven payload weakest of load-bearing types: no stakes/motive/causes guidance, no Tier-2/Tier-3 home | thread→rendering | P2 | UNDETERMINED |
| ep-25 | General Duel offer/consent procedure unwritten (§3.7 infill empty); Contested Figure §11 is two sentences | mass↔personal | P3 | DELIBERATE core; gaps NOT-INTENDED |
| ep-26 | Fieldwork→Mass suspension resumes as a NEW scene — narrative momentum discarded though Evidence numbers survive; in-flight Thread-Read fate unaddressed | fieldwork↔mass | P3 | UNDETERMINED |
| ep-27 | Zoom-In Ob shift (§4.1), ED-749 hysteresis, ED-750 dedup: all mechanically sound, all invisible — reads as bugs, not design | strategic→personal | P3 | mechanics DELIBERATE; presentation NOT-INTENDED |
| ep-28 | Contest→Fieldwork auto-updates (Appraise→Evidence, Disposition shift) fire silently, no feedback line specified | contest→fieldwork | P3 | UNDETERMINED |
| ep-29 | §4.3.3 world-state triggers: five flavor menus, zero adjudicable procedures | strategic→personal | P3 | UNDETERMINED |
| ep-30 | Siege-turtle stack (Walls + Shield Wall + idle-morale waiver) — corroborates the prior hunt's unverified line; counterable, calibration-gated | mass↔settlement | P3 | UNDETERMINED (sweep target) |
| ep-31 | Mandate saturation (7T/(T+6)) and per-settlement Treasury attribution are black boxes at the meter — deliberate damping with no "you've hit the curve" tell | settlement↔faction | P3 | damping DELIBERATE; legibility UNDETERMINED |

## 3 · Calibration outcomes (KNOWN items assessed, not re-reported)

- **ED-1010** — the mass-battle agent independently rediscovered the §A.10 War-row Coherence
  contradiction as "NEW"; reclassified (R1). Seam impact stands: a practitioner-general cannot
  price a War-scale cast, which erodes co-movement's *felt* cost precisely where P-14 is otherwise
  best-served (the §A.10 scale-specific co-movement table).
- **Propagation-spec D.6/OF-D6** — reclassified KNOWN-TRACKED (R2); the dossier's addition is the
  player-chair consequence (an un-damped up/down oscillation would read as a bug, not physics).
- **F-4 extension** — confirmed and widened to the whole `scene_outcome` family (EP-3); §6.4's
  false "already triggers" line verified (V7).
- **F-3 quantified** — the stale UI spec is not merely old: it is the *only* home of every seam
  feedback mechanism found (EP-11), and it has zero coverage of the Why?/chronicle surfaces
  current canon specifies (V10).
- **scene.combat_resolved** — consumption gap re-scoped upward: it is the implied delivery path
  for the corpus's single bespoke-warned moment (duel vs faction officer). Sequenced-not-abandoned
  per gap_notes; the sequencing has no owner visible at the seam.
- **§12.4 down-seams** — concrete player-losses enumerated per seam (cluster C): companions silent
  about their own faction's domain actions; coups with no personal-relationship consequence trail;
  disasters with no place-specific landing; authored events with no settlement stats to touch.
- **F-1 / governance redesign** — the seam this audit adds: §3.1's promised dual-authority tension
  has no Directive/response button in canonical §3.2 (the drafted Comply/Bargain/Defy triad is
  exactly the missing reciprocity, still PROPOSAL).
- **ED-911** — chair impact sharpened: with thread-in-combat missing, the fieldwork-ambush edge
  (ep-12) and any mid-investigation fight cannot route a practitioner's signature verb; three
  seams inherit one gap.
- **Succession trigger nuance** — routine (non-contested) succession does not fire Tier-2 (V7/R3);
  folds into EP-3's family pattern rather than standing alone.

## 4 · Corpus-level signals

- **SIG-1 · The trigger table was built sim-first, never registry-swept.** EP-3/EP-4/EP-5 are one
  pattern: §3.1's 10 triggers are the cases Stage 10 measured; the other ~34 registered types —
  including entire families whose purpose is "something concluded" — fall to a salience function
  that can only re-score triggers that already fired (`unarticulated_weight` has no escape hatch).
  Any fix that adds triggers one-at-a-time will repeat F-4; the fix shape is a one-time sweep of
  registry × {Tier-2 gate, Tier-3 template, Zoom tables} with an explicit verdict per type.
- **SIG-2 · Feedback is authored nowhere current.** Across all eight clusters, every "how does the
  player see this?" answer resolved to either the off-index UI v4 docs, `conviction_track_v30 §11`
  / `peninsular_strain §2.8` (excellent but unkeyed/local), or nothing. Current-generation canon
  authors mechanics without a feedback line as a matter of habit — the dramatic-legibility test
  has no per-seam enforcement point.
- **SIG-3 · The GM's job was never re-assigned (EP-1's generalization).** The seams still assume an
  adjudicator: scope recognition, grants, selections, interventions, warnings, explanations. Each
  is individually small; the class should be closed as a class — a sweep for GM-tokens and
  unadjudicated "may" language at every handoff, converting each to an engine rule or an explicit
  player choice.
- **SIG-4 · The seams are off the index.** Fieldwork/investigation, scale_transitions,
  player_agency — the connective tissue itself — have no CURRENT.md rows (V5), and the
  contracts registry carries at least one more stale doc:null (`faction_politics`, ep-14) of the
  exact class it already caught once (`miraculous_event`). The currency system tracks organs, not
  joints.

## 5 · Threadwork at the seams (P-14 rollup)

Structurally, P-14 is honored at most audited junctures — often better than the seams' general
health (mass battle's scale-specific co-movement table; Hybrid's deterministic CI auto-effects;
contest §9.3/§9.4b; fieldwork Thread-Read). The failures are specific: **(a)** combat remains the
one mode where the claim is false in the shipped resolver (ED-911, three seams inheriting);
**(b)** off-screen thread consequence has no rendering path (no §3.1 thread trigger, no Tier-3
thread paragraph; the ED-681 crisis beats render only protagonist-present, outside the Key stack);
**(c)** the strategic abstraction layer (`conviction_track_v30 §1.3b` PT deltas; `victory §5.3`
RM→Underground conversion; §3.5/§5.6 scalar echoes) nowhere documents whether three-dimensional
co-movement resolved before flattening — the exact boundary question logged as **A-9** in the
2026-05-16 faction NERS audit and never closed or ledgered; **(d)** two timing seams (Hybrid CI
vs Echo, ep-20; interrupted in-flight Thread-Read, ep-26) leave co-movement present but
inconsistently clocked. Recommended targets, in order: ED-911 (open P1, already tracked) ·
re-surface A-9 for a ruling · a canon-guard pass on §1.3b/§5.3 · the ep-20 timing line.

## 6 · Direction rollup

| Direction | Health at the seams |
|---|---|
| lateral (scene-scale) | Strongest — designed by hand; two holes (combat↔thread, combat↔contest) |
| bottom-up | Mechanically complete, experientially silent (EP-11); one live contradiction (EP-9) |
| top-down | Mandatory-crisis rows good; da.*/env delivery missing (EP-6); world-state rows unadjudicated |
| diagonal | Carried by causes[] in spec; unauthored by emitters in practice (battle_concluded causes[] never populated) |
| outward (rendering) | The audit's worst axis: EP-3/EP-4/EP-5 |
| temporal (cadence) | Slate/accounting rhythm well-specified; D.6 oscillation risk and dual-clock seams are the residue |
| backwards (currency) | EP-10 + ep-14 + ep-23: the seams and their tables are where register drift concentrates |

## 7 · Candidate remediation menu (NOT filed — Jordan picks; merging this PR ratifies nothing)

Ranked by leverage-per-effort at the seams; each is deliberately one bounded artifact.

1. **Registry×rendering sweep** (SIG-1): one table, 44 rows, four columns (Tier-2? Tier-3 slot?
   Zoom trigger? deliberate-silent?) — every row gets a verdict; closes EP-3 and the F-4 class
   permanently, and makes EP-4/EP-5's missing keys visible as empty rows.
2. **GM-token sweep of the handoffs** (SIG-3/EP-1): enumerate every "GM," "may grant," "most
   relevant," "may intervene" at a seam; convert each to an engine rule, a player choice, or a
   flagged design decision. Small, mechanical, high leverage.
3. **Key the settlement layer + ci_political + era transitions** (EP-4/EP-5): three emitters, one
   pattern — the state machines exist, the beats are authored; they need Key types and emit
   clauses (registry §10 candidates already flag two of the three).
4. **Rule the stacking contradiction** (EP-9): one Jordan call (§5.5 vs §2.7), then reconcile
   Step 4c. Cheapest P1 in the audit.
5. **Author the strategic-turn surface** (EP-2): one doc unifying card-hand + faction actions +
   resolver + da.* tagging — fills the `domain_actions` doc:null with what already exists.
6. **Seam-feedback line as authoring convention** (SIG-2): a one-line "FEEDBACK:" field required
   in every handoff/trigger table row — enforceable by the co-file checker pattern; prevents new
   silent seams while the UI layer is rebuilt.
7. **Counter-espionage loop** (EP-6): design work, not wiring — give detection/response a home
   (fieldwork is the natural host; Exposure already exists as the symmetric mechanic).
8. **BG params re-export** (EP-10): re-derive `params/bg/victory.md` (+ fix board_game.md links)
   from `victory_v30.md`; an S-1 remediation exemplar.
9. **Index the joints** (SIG-4/ep-23): add CURRENT.md rows for fieldwork/investigation (naming the
   head and settling EP-8's doc conflict), scale_transitions, player_agency; flip
   `faction_politics` doc:null (ep-14).
10. **Ambient-fabric window** (EP-7): a single "overheard" mechanic — gossip Keys gain a
    conditional player-observer when the player shares the scene — plus writing §6.1's empty
    revelation procedure.

## 8 · Bottom line

The prior audit's verdict — computes more emergence than it can show — localizes, at seam
resolution, to three fixable strata: **silent crossings** (feedback authored nowhere current),
**unfired beats** (authored presentation stranded on missing Keys), and **an empty adjudicator's
chair** (GM-era language where engine rules must be). None of the P1s in this report requires new
game design except EP-6; the rest are wiring, ruling, sweeping, and indexing work whose shape
canon already contains. The seam-level good news is real and worth stating: where the corpus
*did* design a crossing deliberately — evidence-into-contest, thread-into-debate, the scene slate,
the mandatory crisis rows, the aftermath scenes — it plays well by its own bar. The game's seams
do not need to be invented. They need to be staffed.
