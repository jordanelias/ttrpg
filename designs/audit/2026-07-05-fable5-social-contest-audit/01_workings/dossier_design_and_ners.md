# Dossier — Qualitative NERS + Throughlines Evidence (Agent B, sonnet tier)
## Status: WORKING EVIDENCE — no verdicts; judgment reserved to the orchestrator
## Date: 2026-07-05

Scope per charter: North-Star (N→Ω→Μ/М/Τ→Q) clause evidence, throughline traces (T-03/T-14/T-17/T-23/T-24),
P-14 juncture, М meta-patterns, and rolling-engine annex delta. All citations `path:line`. No verdicts rendered.

---

## Part 1 — North-Star clause-by-clause evidence

### N — Necessity: the complexity budget, doc claim vs code wiring

Enumerated budget (doc-declared cardinalities, cross-checked against code):

| Budget item | Doc cardinality | Doc citation | Code citation |
|---|---|---|---|
| Proceedings | 8 | `designs/scene/social_contest_v30.md:95-106` (§2 Step 5 table) | `sim/personal/contest/modes.py:460-494` (`PROCEEDINGS` dict, 8 keys) |
| Adjudicator types | 4 (Expert Judge / Crowd / No Adjudicator / Panel) | `designs/scene/social_contest_v30.md:30-38` (§2 Step 1 table) | `sim/personal/contest/modes.py:401-406` (`ADJUDICATOR_PRIMARY`), `modes.py:438-443` (`CANONICAL_ADJUDICATORS`) |
| Argument styles | 4 (Precedent/Suppression/Vision/Insinuation) | `params/contest.md:34-43` | `sim/personal/contest/dictionaries.py:89-133` (`STYLES_TABLE`) |
| Interaction types | 4 (CLASH/REINFORCE/CROSS/TIE) | `designs/scene/social_contest_v30.md:179-224` (§4 Step 4) | `sim/personal/contest/dictionaries.py:282-307` (`INTERACTIONS_TABLE`) |
| Trackers | 3 (Concentration/Face/Persuasion Track, CR3) | `designs/scene/social_contest_v30.md:229-237` | `sim/personal/contest/primitives.py:154-166` (`TRACKERS` registry) |
| Adjudicator armature axes | 4 (Evidence/Consequence/Authority/Insinuation) | n/a (Stage-3 addition, not v30-prose) | `sim/personal/contest/armature.py:191-204` (`ArmatureAxis.ALL`) |
| Deliberative games | 4 (Agôn/Consensus/Negotiation/Inquiry), 1 wired | n/a | `sim/personal/contest/wrapper.py:206-215` (`GAMES` dict: `agon` status `"WIRED"`; `consensus`/`negotiation`/`inquiry` status `"STUB"`) |

Each proceeding/style/interaction/tracker row carries an inline `<-` params citation in `dictionaries.py`
(e.g. `sim/personal/contest/dictionaries.py:93,102,115,125` per-style `canonical_flavor` comments); the
armature's 3 real axes are cited to `npc_behavior_v30.md §1.3 head:32-42` and the 4th (Insinuation) is
flagged `RATIFIED ... NEW 4th axis` rather than reused (`sim/personal/contest/armature.py:175-190`). The
`wrapper.py` GAMES table itself states what each STUB earns its place *for* even though unbuilt: e.g.
`"consensus": {...,"source": "social_contest_v30 §10 BG-Vote / §7.2 (largely in faction.py — Stage 4)"}`
(`sim/personal/contest/wrapper.py:209-210`).

**Deliberation-critique trilogy finding ("read-and-cited-but-not-applied").** `handoffs/HANDOFF_SC.md:77-85`:
> "SOURCE-RESEARCH GROUNDING ... The deliberation-critique source research
> `designs/audit/2026-06-28-social-contest-deliberation-critique/source-research/` (a 3-part
> Renaissance-deliberation / machination-games-lens / model-testing trilogy) is READ-AND-CITED-BUT-NOT-APPLIED:
> it shaped the plan's four-games / alea / consensus / commitment-store / armature *shape* via `critique.md`,
> but its rich detail (Dowlen small-pool weighted lottery; `liberum veto` as self-undermining equilibrium;
> Padgett robust action; Putnam two-level bargaining) is not yet in the code."

**PR #77's corpus-wide N row** (not contest-scoped — the whole-game N verdict, cited here for lineage):
`designs/audit/2026-07-04-ners-qualitative-audit/ners_qualitative_audit_v1.md:34`:
> "**N — Necessity** | **PASS (flag 2)** | Mechanics are overwhelmingly grounded in Renaissance political
> leadership; flags: convergence markers exist as prose with no mechanism (necessary but unbuilt),
> territory temperaments are mechanically inert (built but unconsumed)."

### Ω(a) — cross-scale consequence

Doc: §6 Domain Echo (`designs/scene/social_contest_v30.md:287-290`):
> "**Domain Echo:** Decisive win + Memory genre: winning faction's Mandate +1 in the domain of the cited
> precedent. Decisive win + Projection genre: +1D on first Domain Action pursuing the argued outcome within
> the season. Compromise: no Domain Echo."

Doc: §6.1 Obligations (`designs/scene/social_contest_v30.md:296-300`):
> "A Decisive win (Persuasion Track ≥ 7 or ≤ 3) in a Formal or Grand Contest produces a binding
> **Obligation** — a mechanical commitment that persists across seasons. The Obligation is the contest's
> lasting consequence in the game world, not just a stat change."

Kernel-side: no grep hit for echo/mandate/obligation emission anywhere in `sim/personal/contest/*.py`
(searched for `Recall|Corroborate|Findings|Prep` separately below; a targeted look at `faction.py` — the
one module that touches Mandate — shows only *consumption* of `Faction.mandate` as vote weight
(`sim/personal/contest/faction.py:15,52-56`), never an emission/increment of it from a contest outcome).
`wrapper.py`'s own MECHANICS/GAMES registries self-report the gap: the `consensus` game (the §10 BG-Vote /
§7.2 path Domain Echo and Obligation math would live under) is a registered STUB —
`"consensus": {"resolve": _stub("consensus"), "status": "STUB", "source": "social_contest_v30 §10 BG-Vote
/ §7.2 (largely in faction.py — Stage 4)"}` (`sim/personal/contest/wrapper.py:209-210`). `Contest.resistance`
carries an explicit non-wiring note of the same shape: "METADATA-ONLY this stage (F10): carried for
display/authoring but NOT plumbed into resolution ... Wiring it is the reserved ED stub (contest_rebuild,
ED-1055..1079)" (`sim/personal/contest/wrapper.py:74-76`).

### Ω(b) — personal transformation

Doc: §6.2 Conviction Scar Visibility (`designs/scene/social_contest_v30.md:346-352`) — a contest argument
can produce an NPC Conviction Scar with a narrative signal to the player. Doc: §9.5 Beliefs Integration
(`designs/scene/social_contest_v30.md:562-563`) — "Winning an exchange while arguing for a position aligned
with the orator's stated Belief counts as a Belief achievement for Momentum." Doc: Face persistence — but
note the doc itself specifies Face is **transient**, not persistent: "Face recovery: full restore at scene
change" (`designs/scene/social_contest_v30.md:244`); Face is explicitly distinguished from persistent
Disposition/Reputation (`designs/scene/social_contest_v30.md:239`, "Face ≠ Disposition and Face ≠
Reputation").

Kernel-side: `Contestant` (the immutable spec a `_Side` is built from each bout) is documented as
"safely reusable across bouts" precisely *because* the Bout "never mutates the spec"
(`sim/personal/contest/resolver.py:178-181`) — i.e. whatever Standing/Face a character builds *during* a
bout does not write back onto the `Contestant` spec for the next bout by construction. No grep hit for
"Chronicle" anywhere under `sim/personal/contest/`. No cross-bout persistence field exists on `Contestant`
(`sim/personal/contest/resolver.py:182-193`: `faculty, standing_start, reserve_max, evidence/dossier,
charisma` — all build-time/spec values, none a running cross-bout accumulator).

### Ω(c) — autonomous world

No NPC-initiated-contest code path found under `sim/personal/contest/` (no scheduler/trigger module; the
package is entirely bout-resolution, not a world-clock). Doc-side, no §-numbered "NPC initiates a Contest"
mechanic was located in `social_contest_v30.md` in the sections read.

The social_contest↔npc_behavior 2-cycle (`references/module_contracts.yaml:441-442`):
> "loops: - {with: npc_behavior, damper: \"2-cycle: emits scene.contest_resolved/scene.dialogue, consumes
> state.opinion_revised. BOUNDED [verification LD-1]: Procedure-D batch cadence (1/Accounting) +
> |delta-affect|>=0.5 emission threshold + Chain-Contest cap 3 then 4-season cold equilibrium. NOTE: the
> affect_axis clamp is NOT in canon; convergence rests on these bounds + the saturating §5.4 drift curve.\"}"

PR #77's interdependency map on the NPC-side of this same cycle (`designs/audit/2026-07-04-ners-qualitative-audit/00_grounding/02_interdependency_map.md:24-25`):
> "6. **Social Contest ↔ NPC behavior 2-cycle** (`scene.contest_resolved`/`state.opinion_revised`);
> social side dampers specified; **npc_behavior side "dampers unconfirmed [OPEN — Jordan]"**."

### Ω(d) — non-dominance

**L-A (Recall/Corroborate/Prep/Findings stacking, no global cap) — doc vs code precision.** The doc math
(`designs/scene/social_contest_v30.md:85-87,166-168`, `designs/scene/social_contest_v30.md:532`) describes
Recall +2D, Corroborate +1D, Prep +1D, Findings +2D as all uncapped *outside* the genre+audience-boost
+2D combined cap. A targeted kernel grep (`sim/personal/contest/*.py`, case-insensitive, terms
`Recall|Corroborate|corroborat|Findings|Prep\b`) finds **no implementing code for any of the four** — the
only hits are: (a) `armature.py:61-62`, a comment citing CR6's list of setup-advantage channels
("genre-stasis affinity, AUDIENCE BOOST, Recall, Face, corroboration, prep, commit-spend") as the *intended*
δσ home, not an implementation; (b) `dictionaries.py:534`, flavor-text prose ("per-source Recall (ED-617)");
(c) `primitives.py` `Dossier.CORROB` (`sim/personal/contest/primitives.py:295,305-310`), a *different*
mechanic — diminishing-returns weighting on presenting multiple Evidence items, not the §2b Corroborate
declare-support action. **The only pool/leverage bonuses actually wired in the kernel are the CR4 primary-
genre +1D pool die (`rhetoric.py:221-243`) and the armature's continuous δσ (`armature.py:357-371`).** So
the uncapped-stacking hazard the doc math describes is not (yet) a live kernel behavior — it is a
doc-math-only finding pending Recall/Corroborate/Prep/Findings ever being wired.

**L-B (Appraise audience-boost as a public lookup).** Faction boost table
(`params/contest.md:67-77`) is a fixed, public per-faction axis (Church=Obscuring, Crown=Revealing,
Varfell=Projection, Hafenmark=Memory, Restoration=Revealing, Löwenritter=Projection-conditional); the one
variable case, Guilds, is resolved by a fully deterministic function of the adjudicator
(`sim/personal/contest/dictionaries.py:472-486`, `guilds_boost_for`): "Deterministic (ties broken by the
Aristotelian appeal order logos>pathos>ethos); no GM, no orator pick, no randomness." The armature (the
smaller, continuous lever) is the one thing given a partial-reveal protection
(`sim/personal/contest/appraise.py:9-12,74-102`); the larger +1D lever (audience boost) has no such gating —
its value is derivable from public faction/venue identity without ever rolling Appraise.

**L-E (Face/Rattled largely inert).** Kernel-wide grep for `.strip(` / `strip_points` inside
`sim/personal/contest/` shows exactly one live call site: `resolver.py:418`
(`c.face.strip_points(backfire)`), gated behind `self.armature is not None and self.armature.cr5` and firing
only on a `deg==0` Obscuring foul (`sim/personal/contest/resolver.py:404-419`). No other strain-consumption
of Face/Standing exists in the kernel — `primitives.py:83-90` states this directly: "Standing.strip() is
NEVER called in the contest kernel — Face has NO strip/strain channel wired, so it is monotonic-up. The
v30-surface 'strain -> Rattled -> -1D Argue pool' behaviour ... [is] NOT realized here." The general
strain≥Face→Rattled threshold cascade (`designs/scene/social_contest_v30.md:241-243`) has no kernel
consumer at all; only the single CR5 self-backfire trigger strips Face.

### Q-robust / Q-smooth / Q-elegant — consistency spot-checks

**Persuasion band boundaries — doc vs kernel granularity.** Doc (`params/contest.md:127-131`):
"Range: 0–10. Side A wins ≥ 7. Side B wins ≤ 3. Compromise zone: 4–6." Kernel
(`sim/personal/contest/resolver.py:86-93`, `PersuasionTrack.resolve`):
```
if t >= 9: return "A_total"
if t >= 7: return "A_decisive"
if t > 3:  return "committee"
if t > 1:  return "B_decisive"
return "B_total"
```
The code's `committee` band is the open interval `(3, 7)` on a *continuous* `t`, whereas the prose states
an integer-cut "4–6" — the two are compatible at the integers but the code additionally resolves non-integer
`t` (e.g. `t=3.4` or `t=6.8`) into `committee`, a granularity the discrete prose table does not itself
specify. The code's 5-band split (`A_total/A_decisive/committee/B_decisive/B_total`) does correctly fold in
the separate §6 Total Victory thresholds (`designs/scene/social_contest_v30.md:292`, "Total Victory
(Persuasion Track ≥ 9 or ≤ 1)") into the same lookup, which the params 3-band table alone does not show.

**Two Argue-pool formulas.** Doc (`params/contest.md:16-25`, `designs/scene/social_contest_v30.md:119`):
`Argue Pool = (Primary Attribute × 2) + History bonus`, attribute selected by adjudicator type (Cognition/
Charisma/Attunement). Kernel (`sim/personal/contest/primitives.py:208-211`, class `Pool`):
`Pool.size(faculty) = max(5, faculty * 2 + Pool.BASE)` where `Pool.BASE = 3` — a single abstract `faculty`
scalar, not a per-adjudicator-type doubled *attribute*, and with a floor of 5 that the doc-side pool
(which the 2026-05-28 diagnostic measured as low as 2D at Cognition 1 / History 0,
`designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_social_contest.md:44-52`) does not
carry. These are two distinct formulas for "the Argue pool," not one formula ported verbatim.

**Audience-resistance status.** `sim/personal/contest/wrapper.py:301`
(`MECHANICS["audience_resistance"]`): `"status":"PARTIAL"` — "DERIVED but not yet plumbed into resolution
(ED-1055..1079)"; confirmed by the class comment on `Contest.resistance`
(`sim/personal/contest/wrapper.py:74-76`, quoted under Ω(a) above).

**[SEED] density.** A non-exhaustive count of `[SEED]`-tagged calibration constants across the kernel:
`resolver.py:37-42` (`MERIT_SCALE, JITTER, PUBLIC_LEAK, INST_BIAS, PUB_BIAS, EVIDENCE_CAP`),
`primitives.py:33` (`Standing.BUILD/STRIP`), `primitives.py:50` (`Reserve.MAX`),
`primitives.py:192-202` (9 `RhetoricalWeights` entries), `primitives.py:209` (`Pool.BASE`),
`primitives.py:214` (`SelfGating.MARGIN`), `primitives.py:233` (`Room.CAP`),
`primitives.py:241-242` (`Resonance.ETHOS_UNLOCK/LEAK_CAP`), `primitives.py:255-256`
(`Readiness.FLOOR/W_STANDING/W_ROOM`), `armature.py:228-229` (`STYLE_AXIS_PRIMARY/OFFAXIS`).

**Epideictic compression / stasis×genre (CR4) coherence.** `rhetoric.py:270-299`
(`EPIDEICTIC_COMPRESSION` dict) documents the 2-genre compression as RATIFIED (Gate C, 2026-07-02),
explicitly distinguishing the compression from a "qualitative=epideictic" identity the source research
rejects (`rhetoric.py:259-265`, judge finding 3 note).

**A doc/dictionaries.py naming inconsistency (self-contradictory terminology).** `params/contest.md:98`
("Exchange Structure" summary): "Step 2 — Choose genre (Memory/Projection) + orientation (**Direct/
Indirect**)." This is the same file's own §Argument Styles section
(`params/contest.md` uses "Revealing/Obscuring" throughout, e.g. line 68's Faction Boosts axis values) and
the same terminology `dictionaries.py` codifies: `class Orientation: REVEALING = "Revealing" ...
OBSCURING = "Obscuring"` (`sim/personal/contest/dictionaries.py:66-71`). ED-897's rename pass
(`params/contest.md:81`, comment: "orientation Indirect/Direct → Obscuring/Revealing") appears not to have
reached the "Exchange Structure" summary line at `params/contest.md:98`, which still reads "Direct/Indirect."

---

## Part 2 — Throughline traces

### T-03 Inseparability

Throughline quote (`references/throughlines_complete.md:26-29`):
> "**Chain:** Foundations A2 / P-01 → every Thread operation fires co-movement across all three dimensions
> → temporal auto-effect + epistemic auto-effect + actualized auto-effect. **Systems:** threadwork (core),
> fieldwork (Thread-Read fires co-movement), mass_battle (co-movement at mass scale), social_contest
> (temporal axis conflict penalty)."

Doc-side mechanism: §9.4 Thread Operations Between Exchanges / the Temporal Axis Conflict penalty
(`designs/scene/social_contest_v30.md:540-544`):
> "Temporal axis conflict: if the Thread operation's temporal axis contradicts the contest's primary genre
> ... the operation's co-movement effects apply to the Persuasion Track (±1 shift per co-movement instance
> during the contest scene), per the canonical PP-351."

Code-side: grep across `sim/personal/contest/*.py` for `thread|weav|coherence|disjunction` (case-sensitive
and via a broader case-insensitive pass) returns **zero hits in any resolution module** — the only file in
the package that matches at all is `_kernel_tests.py` (test-file only), and even there no thread-co-movement
mechanic is exercised. **Declared in doc: yes. Wired in kernel: no.**

### T-14 Conviction as Moral Architecture

Throughline quote (`references/throughlines_complete.md:121-124`):
> "**Chain:** Conviction type ... → NPC Conviction Scar accumulation ... **Systems:** npc_behavior (§3, §5),
> player_agency (§2 Convictions), companion_specification (§6.1 departure triggers), social_contest
> (Piety Track, Composure)."

Note: the throughline's own citation names "Piety Track, Composure" — both are **retired/renamed**
surfaces in the current head. Composure is retired as the social-contest tracker name (split into
Concentration+Face, CR3; `designs/scene/social_contest_v30.md:231` and `primitives.py:167-169`
`RETIRED_TRACKERS = ("Composure",)`); "Piety Track" does not appear in the current
`designs/scene/social_contest_v30.md` head at all (it appears only in the 2026-05-28 diagnostic's component
table as a separate 0–10 per-territory accumulator, `designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_social_contest.md:28`,
distinct from the Persuasion Track). Code-side: `TRACKERS` registry names Face/Concentration/PersuasionTrack
only (`primitives.py:154-166`); no "Piety" symbol exists anywhere under `sim/personal/contest/`.
**Declared in doc: yes, but under names the current head has since retired/relocated. Wired in kernel:
Face(=Standing) and Concentration(=Reserve) yes as trackers; the Conviction-Scar-accumulation chain itself
is out of `sim/personal/contest/`'s scope (npc_behavior's).**

### T-17 Companion as Moral Mirror — citation-precision anomaly

Throughline quote, T-17's own header and systems line (`references/throughlines_complete.md:142-145`):
> "### T-17: Companion as Moral Mirror. **Chain:** Companion formation ... → Thread departure triggers ...
> **Systems:** companion_specification (§6.1 Thread departure), npc_behavior (§3.4 Thread Scar),
> player_agency (Conviction × Thread events)."

**T-17's own Systems line does not mention social_contest at all.** The "Solidarity Resonant Style" citation
the audit charter (`01_criteria_and_lineage.md §3`) attributes to T-17 actually sits under the *preceding*
throughline, T-16 Knot Propagation (`references/throughlines_complete.md:137-140`):
> "### T-16: Knot Propagation. ... **Systems:** threadwork (Knot mechanics), npc_behavior (§5.0b, §3.4),
> companion_specification (departure triggers), fieldwork (§2.6 Knot-mediated remote investigation),
> **social_contest (Solidarity Resonant Style)**."

This is a citation-precision anomaly worth flagging: the grounding doc's T-17→Solidarity-Resonant-Style
mapping does not match `throughlines_complete.md`'s own T-17/T-16 boundary. Doc-side mechanism (regardless
of which T-number it's filed under): Solidarity Resonant Style is a `npc_behavior_v30.md` §1.3 concept
("Any genre + Revealing; requires active Knot" — quoted at `sim/personal/contest/armature.py:166`), and the
Stage-3 armature module explicitly declines to reuse it as the adjudicator armature's 4th axis *because* it
is Knot-gated/relational and "does not fit a THIRD-PARTY adjudicator"
(`sim/personal/contest/armature.py:175-190`). **Code-side: no `Solidarity` symbol exists anywhere under
`sim/personal/contest/`** (grep confirms `STYLE_AXIS` keys are `precedent/vision/suppression/insinuation`
only, `armature.py:242-247`). **Declared in doc: yes (under T-16, not T-17). Wired in kernel: no —
explicitly named-and-rejected as the armature's basis, not merely absent.**

### T-23 NPC Arc Emergence

Throughline quote (`references/throughlines_complete.md:192-195`):
> "**Chain:** NPC Stance Triangle → Conviction → Scar accumulation (social + Thread) → threshold crossing
> → arc state transition ... **Systems:** npc_behavior (§5 Arc Emergence), arc_expansion ..., arc_register
> (faction vectors), **social_contest (Composure/Piety Track)**, companion_specification."

Same retired-name citation issue as T-14 (Composure/Piety Track). Doc-side social-contest-owned mechanism
feeding this chain is §6.2 Conviction Scar Visibility (`designs/scene/social_contest_v30.md:346-352`) — a
contest outcome can trigger an NPC Conviction Scar, which is the actual T-23 input, not Composure/Piety Track
directly. Code-side: no Scar-accumulation logic exists in `sim/personal/contest/` (Scars are npc_behavior's
domain); `sim/personal/contest/faction.py` models faction-vote persuasion only, with no Scar/arc-emergence
hooks. **Declared in doc: yes. Wired in kernel: no (out of package scope by design — the boundary is
npc_behavior's).**

### T-24 Convergence as Emergent Crisis

Throughline quote (`references/throughlines_complete.md:197-200`):
> "**Chain:** Multiple independent vectors → simultaneous threshold crossing → combined pressure
> qualitatively different from components → emergent crisis. **Systems:** arc_register (§VI Convergence
> Markers — 7+ defined collisions), all faction/territory vectors."

`references/arcs/arc_register_events.md` §VI's named collisions (`arc_register_events.md:29,33,37,41,45,50,54,58`):
COLLISION A (Church Double Fracture), B (Practitioner King), C (Tutoring + Southernmost), D (Niflhel
Weaponises), E (Einhir Elder and Baralta's Claim), F (Succession Triangle), G (Einhir Triangle), J (Church
Siege of the Southern Gates) — none of the 8 collision headers name a Contest/Debate/Persuasion-Track
mechanism as a contributing vector in the headers themselves (headers only, not the full collision bodies).
**Declared in doc: T-24's own Systems line does not name social_contest at all** (only `arc_register`, "all
faction/territory vectors"). Code-side: no convergence-detector/collision logic exists anywhere under
`sim/personal/contest/`, consistent with PR #77's F-2 finding (cited via the corpus-wide N row above:
"convergence markers exist as prose with no mechanism").

### P-14 juncture evidence

`designs/scene/social_contest_v30.md` headers and one quoted line each:

- §9.3 Practitioner Weaving in Contests (R-65) (`designs/scene/social_contest_v30.md:537-538`):
  "A practitioner with TS ≥ 30 in active Thread contact adds bonus dice: floor(TS ÷ 30) ... Must declare
  before rolling. Visible to all observers."
- §9.4 Thread Operations Between Exchanges (`designs/scene/social_contest_v30.md:540-541`):
  "A practitioner may initiate a Thread operation between exchanges. Effects apply before next exchange's
  Read step. Genre/orientation dice are fixed at setup — Thread operations cannot change them mid-contest."
- §9.4b Adjudicator Thread Response (ED-667) (`designs/scene/social_contest_v30.md:545-547`):
  "When an adjudicator ... witnesses Thread use during the proceeding: [Certainty-indexed response table,
  C5 Orthodox → proceedings suspended / Heresy Investigation fires ... ]"

Kernel-side grep for `thread|weav|coherence|disjunction` across `sim/personal/contest/*.py`: **zero hits
in any resolution module** (only `_kernel_tests.py` matches at all, and not on a thread-mechanic assertion).
PR #77's lineage finding for this same gap: `sim-kernel-no-thread-hooks` (cited by name in the audit
charter/criteria doc as the tracked finding this juncture traces to;
`designs/audit/2026-07-05-fable5-social-contest-audit/00_grounding/01_criteria_and_lineage.md` §4 names
P-14 "thread junctures `social_contest_v30 §9.3–9.4b` vs the rebuilt kernel" as the direct bar under audit).

### М meta-patterns participating

`references/throughlines_meta.md` §3 (`throughlines_meta.md:76-102`) lists the 11 М patterns and their
parent Μ modes but explicitly defers the **per-T tag table (which T's map to which М) to the infill**:
"**T→М tag table** (for Τ-level checks): see infill §3.1. Summary: all 25 T's covered; primary-assignment
distribution — М-1: 4 · М-2: 2 · М-3: 4 · М-4: 8 · М-5: 7 · М-6: 5 · М-7: (framework design-level,
cross-cutting) · М-8: 1 · М-9: 1 · М-10: 1 · М-11: 2. Full tag table in infill §3.1."
(`references/throughlines_meta.md:102`). The infill file exists at `references/throughlines_meta_infill.md`
but per CLAUDE.md's atomization convention ("Load infill only when a decision requires deeper
justification") and this audit's evidence-only/no-verdict scope, the exact per-T tag row for T-03/T-14/
T-17/T-23/T-24 was not extracted this pass — flagging the exact М-tag lookup as **not resolved in this
dossier** (an open item for whichever downstream lane needs the precise tag, not a finding in itself).
Structurally, given the chains above: T-03 (Inseparability, cross-scale co-movement) is Μ-δ-parented
(М-5 "Scales connect through substrate"); T-14/T-23 (Conviction/Arc Emergence) are Μ-γ-parented
(М-3/М-4 "Substrate grounds all" / "Institutions stake substrate-postures"); T-24 (Convergence) is
Μ-β/Μ-δ-parented. These are inferred from the Μ mode definitions (`throughlines_meta.md:63-66`), not a
quoted per-T М-tag from the infill.

---

## Part 3 — Rolling-engine annex evidence

### What the 2026-05-28 verdict verdicted

`designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_social_contest.md:6-19`:
```
SYSTEM:  Social Contest
VERDICT: NERS-COMPLIANT — confirms skill INITIAL hypothesis
         "compliant, healthy contested case"

N: PASS — All components earn place; Conviction Track depth IS the L4 clock-routing.
R: PASS — 2D pool floor exists but exit-not-floor architecture (Spent → withdrawal)
         is the safeguard. No undamped+unbounded loops per audit Mode C.
S: PASS — Composure shares architecture with personal combat; Belief cross-refs
         threadwork cleanly; PP-684 Conviction Vector provides faction-scale path.
E: PASS — Interaction types (CLASH/CROSS/COMPETITION/DIVERGENCE/AMPLIFY) learnable;
         PP-684 Conviction taxonomy is most player-legible identity system in
         entire Valoria architecture.
```
The companion diagnostic's component decomposition this verdict is *based on*
(`designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_social_contest.md:22-38`) describes:
Argue Pool = `(Cognition × 2) + History + Memory bonus` with a 2D floor at Cog1/H0 (line 24, 44-52); five
named Exchange Interaction Types "CLASH / CROSS / COMPETITION / DIVERGENCE / AMPLIFY" (line 25) — a
**different taxonomy** from the current 4-type CLASH/REINFORCE/CROSS/TIE (`dictionaries.py:282-307`); a
Composure continuous resource "Cha + 6 (7–13 range)" (line 26); Genre weights "0.5 / 0.75 / 1.0 / 1.25"
(line 29); Piety Track / Conviction Track as a distinct 0–10 per-territory accumulator (line 28).

### What has changed since (Stage 1a–3), and whether each change touches what the verdict relied on

| Change | Citation | Alters pool size? | Alters TN? | Alters leverage bounds? | Alters degree bands? |
|---|---|---|---|---|---|
| **Substrate migration (CR2): success-counting → σ-leverage** | `sim/personal/contest/resolver.py:18-30` (rewired onto `sim.autoload.sigma_leverage`); the diagnostic's own decomposition (dice/success-counting model, 5-type interaction taxonomy, Genre weights 0.5-1.25) has no surviving code counterpart — `dictionaries.py` has no "genre_weight" 4-level table at all | **Yes** — the diagnostic's 2–18D success-counting pool model is not the kernel's current resolution substrate | No — TN stays 7 (`resolver.py:128` prose; `sigma_leverage.TN_STANDARD = 7`, `sim/autoload/sigma_leverage.py:79`) | **Yes** — introduces δσ leverage (`Leverage.net`, `primitives.py:222-230`) with no counterpart in the diagnostic's model | **Yes** — current `degree()` bands (0/1/2/3, `sim/autoload/sigma_leverage.py:284-286`) replace the diagnostic's "successes" count entirely |
| **Stage 1a σ-kernel unification** (`sim/autoload/sigma_leverage.py`) | Retires the "two-σ-kernels debt" (`handoffs/HANDOFF_SC.md:24`, "numpy-free σ sibling, byte-identical to the oracle, 623 tests green") | No (same-substrate consolidation) | No | No (byte-identical port, per the handoff) | No |
| **Armature δσ modifiers** (`armature.py` `style_axis_dsigma`) | Bounded: `ARMATURE_MAX_DSIGMA = level("moderate")` = **0.50σ at perfect alignment** (`sim/personal/contest/armature.py:336`; `sim/autoload/sigma_leverage.py:85-92` `LEVEL_SIGMA["moderate"]=0.50`), soft-capped downstream by `net_boost`'s `M_MAX = 1.5` σ-unit tanh ceiling (`sim/autoload/sigma_leverage.py:92,130-136`) | No (integer pool unaffected — armature is δσ-only, `armature.py:357-371`) | No | **Yes** — adds up to +0.50σ (off-axis: +0.075σ, `armature.py:362`) on top of the pre-existing `Leverage.ONGROUND = level("moderate")` (also 0.50σ, `primitives.py:225`) the diagnostic's model never had | No direct effect (the degree bands are unchanged; only the input net shifts) |
| **CR4 +1D stasis-genre pool bonus** | `CR4_PRIMARY_GENRE_POOL_BONUS = 1.0` (`sim/personal/contest/rhetoric.py:206`), an integer pool die conditional on chosen-genre/live-stasis match (`rhetoric.py:221-243`) | **Yes** — adds a full die to the pool the diagnostic's Argue-pool table did not model | No | No (pool channel, not leverage) | No direct effect (shifts the roll, not the band definitions) |
| **CR5 Face strip** | `CR5_BACKFIRE_MAGNITUDE = 2.0` (`sim/personal/contest/rhetoric.py:366`), applied via `Standing.strip_points` (`primitives.py:37-46`), the first strip channel ever fired in the kernel (`primitives.py:83-90`) | No (touches the Face/Standing tracker, not the Argue pool) | No | No | No |

None of the Stage 1a–3 changes alter **TN** (still 7 throughout). The **substrate migration (CR2)** is the
change most directly bearing on what the 2026-05-28 verdict's own component table described — that table's
"Argue Pool" (Cognition×2+History, success-counting, 2D floor) and its 5-type interaction taxonomy
(CLASH/CROSS/COMPETITION/DIVERGENCE/AMPLIFY) do not have literal code counterparts in the current kernel
(`Pool.size` is a single-scalar formula, `primitives.py:208-211`; the current taxonomy is 4-type
CLASH/REINFORCE/CROSS/TIE, `dictionaries.py:282-307`) — facts only, not a verdict on whether the prior PASS
still holds under the new substrate.

---

## Anomalies noticed in passing

1. **T-17/T-16 citation-boundary mismatch** (Part 2, T-17 section above): the grounding doc's "T-17 →
   Solidarity Resonant Style" mapping does not match `references/throughlines_complete.md`'s own section
   boundaries — Solidarity Resonant Style is T-16's citation (`throughlines_complete.md:139`), not T-17's
   (`throughlines_complete.md:142-145`).
2. **"Piety Track" is stale/relocated terminology.** Both T-14 and T-23's throughline citations
   (`throughlines_complete.md:123,194`) name "Piety Track" as a social_contest component; the current
   `social_contest_v30.md` head has no such section — the closest surviving concept (0–10 per-territory
   Conviction accumulator) is only attested in the 2026-05-28 diagnostic's own component table
   (`resolution_diagnostic_social_contest.md:28`) as a *distinct* thing from the Persuasion Track, and does
   not appear to exist as a named tracker in the current kernel (`primitives.py:154-166` `TRACKERS` has only
   Face/Concentration/PersuasionTrack).
3. **`params/contest.md`'s own internal terminology drift**: line 98 ("Choose genre + orientation
   (Direct/Indirect)") contradicts the same file's dominant Revealing/Obscuring vocabulary used everywhere
   else (e.g. line 68's Faction Boosts axis, and ED-897's own rename-tracking comment at line 81) and the
   code's `Orientation.REVEALING/OBSCURING` (`dictionaries.py:66-71`).
4. **Recall/Corroborate/Prep/Findings bonuses are not merely uncapped — they are entirely unimplemented in
   the current kernel.** The L-A minmax finding (`hunts/hunt_social_minmax.md:14-23`) describes doc-math
   stacking risk; the kernel-side grep in this dossier's Ω(d) section shows none of the four channels have
   *any* code presence beyond comments/flavor text, so the described stacking cannot currently manifest in a
   running `Bout` — only CR4's +1D and the armature's δσ are live pool/leverage inputs today.
5. **`faction.py`'s own docstring calls itself "ADAPTER (not canon)"** (`sim/personal/contest/faction.py:1`)
   while simultaneously being the file `wrapper.py`'s MECHANICS/GAMES tables cite as *the* home for Domain
   Echo / Obligation / Consensus-game logic (`wrapper.py:209-210`) — worth noting the load-bearing gap
   between "adapter, not canon" and "the place Stage-4 Consensus is supposed to promote-existing from."
