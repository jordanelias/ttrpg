# Valoria — Qualitative NERS Audit v1 (North-Star)

## Status: PROPOSED (audit findings — Jordan review)
## Date: 2026-07-04 · Lane: IN (cross-cutting) · Branch: `claude/ners-audit-fable5-9cpfdz`

**Charter:** `00_grounding/00_audit_charter.md`. Criteria = the corpus's own instruments
(throughlines framework PP-672/PP-674: N / Ω / Q-robust/smooth/elegant + dramatic legibility;
P-01..15 + GD-1..3), qualitative — NOT the rolling-engine mechanical test.
**Method:** 12 subsystem/shape dossiers (sonnet) + 5 degenerate-play hunters (opus) + 7
cross-cutting lenses (opus), all six directions; every carried finding adversarially refuted with
an intent gate; completeness critic. 55 agents, 0 errors.
**Funnel:** 172 raw candidate findings → deduped → **62 already-tracked** · **33 P3** · 62 P1/P2
candidates → 30 verified (cap) → **5 survived** · **25 refuted** · 32 deferred unverified.
Full provenance: `01_workings/` (structured outputs, refutation records, critic).

---

## 0 · Corpus verdict (verdict-first)

> **The substrate is deep; the promise is choked at three points.** Valoria's bottom-up rigor
> (combat physics, σ-engine, Mandate math, thread risk economy) is real and improving — but the
> North Star's two load-bearing promises, *myriad meaningful player decisions* and *a collision
> engine rendered as story*, are each under-delivered at a specific, fixable choke point:
> **(1) player decision surfaces** are built after resolvers (combat autoresolves, settlement
> governance is a four-verb stat-pump, faction seasons are mostly accounting output);
> **(2) consequence transport** leaks (declared-but-unconsumed edges, unpopulated down-seam
> targets, thin Key payloads); **(3) rendering** has holes exactly at the flagship moments (no
> convergence-marker detector, articulation trigger gaps, the UI/legibility layer stranded
> off-index). Threadwork is the mechanical model of the North Star — a rich, non-dominant,
> multi-axis decision space — whose collisions currently compute but often cannot surface.

| Criterion | Verdict | One-line basis |
|---|---|---|
| **N — Necessity** | **PASS (flag 2)** | Mechanics are overwhelmingly grounded in Renaissance political leadership; flags: convergence markers exist as prose with no mechanism (necessary but unbuilt), territory temperaments are mechanically inert (built but unconsumed). |
| **Ω(a) cross-scale consequence** | **PARTIAL** | Bottom-up Domain Echo is the best-specified channel in the spine; top-down delivery is proven-possible, not proven-delivered (§12.4 down-seams); consequence does not COMPOUND (no collision detector, cross-tick convergence unproven). |
| **Ω(b) personal transformation** | **PASS** | Best-served clause: Scars, arc state machines, Rendering Crisis, Belief revision, Coherence descent — though absent from the highest-frequency vector, combat (ED-911). |
| **Ω(c) autonomous world** | **PASS (verified under attack)** | Clocks + deterministic priority trees + neglect-driven insurgency genuinely tick without the player; the "GM controls NPC votes" hole was REFUTED (deterministic vote rule exists in the same section — stale wording only). Residual: seeded-sim ~87% single-winner (KNOWN, CLAUDE.md §7). |
| **Ω(d) non-dominance** | **PASS (survived the hunt)** | 5 adversarial min-maxers proposed 23 dominant lines; every headline line that reached verification was refuted by in-canon safeguards (see §5). Residuals are tracked (spear R2/R3) or unverified P3 calibration items. |
| **Q-robust** | **PARTIAL FAIL** | Dramatic legibility passes at NPC and victory/strategic tiers, fails at combat, is partial elsewhere; the "from the screen" bar has no maintained home (finding F-3). |
| **Q-smooth** | **PARTIAL FAIL** | One transport idiom (Key emit/observe) but not one vocabulary (MS/RS, attribute roster 7-vs-9, enum forks); consequence dies in transit at emitter and consumer seams. |
| **Q-elegant** | **PASS (watch combat)** | Most heads restatable after one reading; combat's biomechanical depth is straining the one-reading bar (5-tuple mode-selects, grip oscillator fixes) — a deliberate trade so far. |

---

## 1 · The throughlines tree (the organizing skeleton)

From the throughlines lens (`01_workings/lenses/lens_throughlines_tree.json`), grep-verified.

**TRUNK — four discipline meta-throughlines, load-bearing across nearly every dossier:**

| # | Trunk | State |
|---|---|---|
| T1 | **Μ-δ/М-5 — scales connect through the substrate** (the collision-engine spine) | Carried by every lane (Domain Echo, Mandate, Part D/E, GD-1) — but delivered bottom-up only; top-down + compounding missing (F-2, cohesion lens). |
| T2 | **Μ-α/М-1+М-6 — continuous pressure & forced choice** (clocks + scarcity) | Healthy: MS/RS, TC, IP, Turmoil, Coherence, Campaign Supply all live. Anti-pattern instances: Institutional Consolidation rest-state, Recall +2D cost-hidden checkbox (trunkless mechanics). |
| T3 | **Μ-γ/М-3 — the substrate grounds everything** (P-14 inseparability) | **The trunk with severed limbs** — declared universal (T-01 "Systems: ALL") yet amputated at combat_engine_v1 (ED-911), articulation rendering, faction_behavior's own math, 7/9 NPC priority trees. The single largest structural defect class in the corpus (§6). |
| T4 | **Μ-β — autonomous world** | Genuinely ticking (verified under adversarial attack); one stale "GM controls" wording site to sweep. |

**KEY BRANCHES (one major limb each):** М-4 institutions (faction+NPC sheets/trees) · М-2
geography holds pressure (settlement + mass-battle terrain + calamity radiation) ·
personal-transformation arc cluster T-12/13/16/17 (threadwork + conviction) · strategic-clock
cluster T-04..07/20/25 (victory + strain) · emergent-narrative generation T-23/T-24 (NPC+faction
produce; articulation renders — with the gaps in §4).

**ORPHAN THROUGHLINES (declared, implemented nowhere):** the entire М-7..М-11 phenomenology tier
(T-31/33/34/35/37/38/39/40 — grep-verified: audit/registry docs only, no subsystem head);
T-26..29 ("design complete, implementation pending", prose-only homes); T-02/T-30 home to
`investigation_systems_v30`, which no lane audited `[GAP-1]`.

**TRUNKLESS MECHANICS (no why):** territory temperament α/β (zero mechanical consumers),
Institutional Consolidation passive recovery (anti-М-1), Recall +2D near-costless citation
(anti-М-6).

---

## 2 · Per-subsystem verdicts

Choice density and legibility from the twelve dossiers (`01_workings/dossiers/`), each claim
working-tree-cited there.

| Subsystem | Choice density | Legibility (3 questions) | Threadwork | One-line verdict |
|---|---|---|---|---|
| Personal combat | **thin** | no | absent (ED-911; regression from combat_v30 §10) | Rigorous physics that autoresolves; per-exchange player agency and narrative payload both thin — *by design stage, not accident* (refutation R-1): the player-interface layer is future Phase-4 work, but no sequence entry reserves it. |
| Mass battle | moderate | partial | present (§A.7/§A.10) | Strong strategic/consequence layer (aftermath scenes, named officers); tactical layer narrower than its complexity; sim leads canon with flagged contamination (ED-MB-0002). |
| Social contest | moderate | partial (Agôn yes; 3 games N/A) | present (§9.3–9.4b) | Well-theorized bet-under-uncertainty armature; today one game wearing eight venue skins — Stage 4 is the lane's single highest-leverage step. |
| Faction/political | **thin** | partial | partial (Echo yes; engine math no) | Narratively thick sheets on a heavy accounting substrate that surfaces almost no per-season player choice. |
| Settlement/territory | **thin** | partial | present but inert as choice (§4.4/§4.9) | The ratified governance loop is a four-verb stat-pump the corpus itself diagnosed (F-1); the drafted fix is real, partially built, and untracked. |
| Threadwork | **rich** | partial (MS/RS split blocks one-sentence read) | n/a (is the spine) | The North-Star model subsystem: multi-axis, non-dominant risk economy — undercut by naming debt and missing narrative sinks. |
| NPC behavior | moderate | **yes** | partial (2/9 trees) | Best dramatic legibility in the corpus; "myriad options" under-delivered (predictable trees are deliberate GD-2 structure; arc menus authored). |
| Articulation | thin (sink) | partial | **absent (deliberate-by-architecture, disputed)** | Renders political/personal collisions well; trigger ruleset omits battle/investigation keys (F-4) and all thread beats route through generic salience only (R-2). |
| Architecture spine | thin (plumbing) | partial (Why?-diagnostic unbuilt) | present-but-thin (`scene.thread_operation` [STUB]) | Uniform, direction-neutral delivery — with the least-specified modules (domain_actions, engine_clock) at the most load-bearing junctions. |
| Victory/strategic | moderate | **yes** | diagonal (battle→MS) | Rich toolkit differentiation; GD-1's single victory shape is a deliberate constraint that trades ending-diversity for pressure-diversity. |
| Registers/graphs (shape) | n/a (meta) | n/a | n/a | Points away from the North Star by omission: the currency layer is stale exactly where the corpus is most alive (mass battle); no shape-layer instrument checks P-14. |
| Recent infra (sequence) | n/a (meta) | n/a | n/a | Steering surfaces have drifted apart: workplan v5 vs CURRENT.md/decision-queue contradict on J-38; roadmap_state describes a May track; only CURRENT.md is fresh. |

**Direction coverage matrix** (findings + dossier axes; ✓ = substantive coverage, ○ = thin):

| Subsystem | top-down | bottom-up | lateral | diagonal | forwards | backwards |
|---|---|---|---|---|---|---|
| personal_combat | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| mass_battle | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| social_contest | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| faction_political | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| settlement_territory | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| threadwork | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| npc_behavior | ○ | ✓ | ✓ | ✓ | ○ | ✓ |
| articulation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| architecture_spine | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| victory_strategic | ✓ | ✓ | ✓ | ✓ | ○ | ✓ |
| registers_graphs | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| recent_infra | ○ | ✓ | ✓ | ○ | ✓ | ✓ |

Corpus-wide, **top-down and forwards are the thinnest axes** (critic-confirmed): N/Ω verdicts
concentrated in lenses rather than exercised per-head, and forwards lives almost entirely in the
sequence lens — declared here as the canonical forwards home rather than implying per-dossier depth.

---

## 3 · Confirmed findings (severity-ranked; every one survived adversarial refutation)

Format: `[criterion · severity · direction · intent]`. Full refutation records in
`01_workings/refutations/` + `01_workings/confirmed.json`.

**F-1 · Settlement governance is a thin loop the corpus already diagnosed — and the fix is
untracked** `[Q-robust · P2 · top-down · NOT-INTENDED]`
The ratified seasonal loop is one mandatory verb from four stat-pumps
(`settlement_layer_v30.md §3.2`); `governance_play_redesign_v1.md` (PROPOSAL, 2026-06-22)
self-diagnoses verbatim: *"governing collapses toward 'roll one die a season and watch numbers'
unless a GM carries it"* — and there is no GM. The redesign is well-aimed, and its G1 prerequisite
is **already built** (`sim/territory/registry.py` + ledger + 6 passing tests — found during
refutation R-5), yet the proposal appears in no ED, no HANDOFF_SE pending item, no decision-queue
entry, and CURRENT.md's settlement row doesn't mention it. *Refuter note: severity trimmed from
P1 because the politics is real one tier up (§3.1 dual authority, §3.3 subnational contest,
§1.8 Mandate) — the thin surface is the per-season verb menu.* `[READ: settlement_layer §3.2/§3.1/§3.3/§1.8;
governance_play_redesign_v1 header; sim/territory/]` `[CONFIDENCE: high]`

**F-2 · The "emergent narrative engine" has no engine** `[N/Ω-a · P2 · top-down · UNDETERMINED]`
The corpus's flagship emergence mechanism — 8 Convergence Markers, canonically "the game's
emergent narrative engine" (`references/throughlines_complete.md` T-24 L200) — exists only as
hand-authored trigger+payload annotations in `references/arcs/arc_register_events.md §VI`, whose
own header concedes the combined pressure "is not predictable from the constituent vectors."
No Key type, module contract, sim module, or resolver detects trigger-coincidence or applies the
combined payload; T-24 is the only throughline with no Implementation-status line. The WHEN of
collisions can emerge from independent vectors; the WHAT is scripted and nothing fires it.
*Refuter note: P2 not P1 — base emergence has independent live channels (T-23 NPC arcs, clocks);
the markers are the curated dramatic surface, not the whole substrate.* `[READ: arc_register_events §VI;
throughlines_complete T-24; module_contracts grep; sim/ grep]` `[CONFIDENCE: high]`

**F-3 · The playability bar has no maintained home** `[Q-robust · P2 · backwards · UNDETERMINED]`
The only comprehensive player-facing spec (`designs/ui/valoria_ui_ux_v4_1.md`, CANONICAL,
2026-04-16) predates the entire v40 generation, is absent from CURRENT.md (no UI/legibility row
exists), still specifies player-facing tracks canon has STRUCK (Taint 0–6, CD), and its 69-finding
/ 20-P1 repair workplan (v4.2) was never executed. The only current-era interaction artifact is
the DRAFT one-subsystem contest walkthrough. *Refuter note: verdict PLAUSIBLE — a deliberate
per-subsystem-walkthrough method is a defensible reading (the SC lane seeded its walkthrough
intentionally), but that policy is nowhere stated for the corpus-wide layer, and v4.1's
stale-CANONICAL status is affirmatively unmanaged.* `[READ: ui v4_1 header; v4_2 workplan;
CURRENT.md; player_interaction_walkthrough_v1]` `[CONFIDENCE: high on facts, medium on intent]`

**F-4 · Articulation's trigger ruleset omits the keys its own registry says it consumes**
`[Q-smooth · P2 · lateral · NOT-INTENDED]`
`articulation_layer_v30.md §3.1` enumerates exactly 10 triggers — none is
`scene.battle_concluded` or `scene.investigation_resolved`, both registry-declared consumed types
(`key_type_registry_v30.md §7` L682/L705) — and §6.4 (L296) falsely asserts battle_concluded
"already triggers Tier 2" by an unstated rule. The doc's own Stage-10 precedent (belief_revised
had identical "by default" language and still required explicit trigger #10) proves §6 defaults
are not self-executing. Decisive battles and trial verdicts currently get no Tier-2 cut scene;
the annual Tier-3 chronicle is the only capture. Scope extends to `scene.combat_resolved`.
`[READ: articulation §3.1/§6.4/§5; key_type_registry §7]` `[CONFIDENCE: high]`

**F-5 · GD-1's strike never swept peninsular_strain — ~8 live co-victory sites**
`[Q-smooth · P3 · lateral/backwards · NOT-INTENDED · reclassified KNOWN-TRACKED]`
`peninsular_strain_v30.md §6.3` (+ L129/220/310/457/493/571/590) still carries Partition
co-victory as unmarked canonical text; sibling `victory_v30.md §0.1` got the [SUPERSEDED-BY: GD-1]
banner because GD-1's propagation list names it — peninsular_strain isn't on the list. The refuter
found this is a residual of the **tracked** pending Pass-2k batch
(`canonical_sources.yaml` FACTION-SPECIFIC-VICTORY-PATHS), with new scope evidence (whole doc
un-swept). Safeguard: GD-1 is authoritative top-of-stack, so the dead mechanic cannot fire.
`[READ: peninsular_strain §6.3 + 7 sites; canon/02 §B; canonical_sources]` `[CONFIDENCE: high]`

**Corpus-level signals bound from multiple lanes** (critic instruction — these are cross-cutting,
not lane-local; both feed `strategic_judgments.md`):

- **S-1 · Register back-propagation blindness** (registers_graphs + sequence lenses): executable
  ratifications (mass battle, contest) never round-trip to `mechanics_index.yaml` /
  `supersession_register.yaml` (frozen at ED-912/06-28: no GD-1 entry — F-5's root cause — no
  ED-MB flips); a session trusting the indexes resumes from a materially false baseline.
- **S-2 · Steering-surface fragmentation** (recent_infra + sequence lenses): workplan v5 says
  J-38 is open/PROPOSED while CURRENT.md + decision-queue item 18 say CANONICAL/RATIFIED;
  `roadmap_state.yaml` (phase 2, items_done 0) describes a May track; decision-queue items 1–3
  reflect pre-R2 combat physics. Only CURRENT.md's hand reconciliation holds currency together.

---

## 4 · Threadwork at every juncture (P-14 map)

From the threadwork-applicability lens (working-tree verified), + dossier junctures
(`01_workings/dossier` files). P-14's live failure shape is **(b) a whole play mode cannot host a
thread op** — no co-movement-omission cases were found.

**WIRE IT — ranked by North-Star value:**
1. **combat_engine_v1** (ED-911, open P1 — a *regression*: superseded combat_v30 §10 had
   Leap-in-combat that never migrated; two post-ED-911 engineering passes reserved no slot for it).
2. **Articulation render path for thread beats** — ED-681's four authored Rendering-Crisis beats
   have prose homes (`threadwork_v30 §3.7`) but no §3.1 trigger; thread events reach the player
   only via generic salience (see R-2 — the wildcard-architecture defense holds for *state*, not
   for *cut-scene-worthy crises*). Decision point, not clean defect: add thread triggers or ratify
   generic-salience as the policy.
3. **General Duel** (child of 1).
4. **faction_behavior engine math** — α/β/γ/λ take only generic env.* shocks; refuted as a P-14
   *violation* (thread reaches factions via §3.5/Echo — R-4) but stands as a wire-it *opportunity*:
   Coherence/Calamity terms would make the strategic engine feel the substrate directly.
5. **NPC priority trees** — 2/9 thread-conditioned (Varfell, Wardens); the asymmetry is arbitrary,
   not scaled to faction thread-exposure.
6. **Settlement governance verb** — thread hits settlements automatically (§4.4/§4.9) but no
   governor-facing thread-response choice exists (compose with F-1's redesign).
7–10. Scene→Mass thread channel · npc_memory P-09 hooks · insurgency→Gap coupling ·
   propagation-spec spine (`scene.thread_operation` payload is [STUB]).

**DELIBERATELY ABSENT (intent evidence cited):** Church thread-resistance doctrine (ED-679 —
though the doctrine doc itself is stranded: its target faction was dissolved; the spec's dead
paths and ED-number reuse are P3 debt). Thread Exploitation Sites' uncapped harvest — *verified
deliberate*: designed tragedy-of-the-commons via shared RS (R-6).

**DEFER:** contest sim kernel hooks (staged — Stage 4 next); territory_temperaments coupling
(temperaments are themselves inert corpus-wide, a trunkless mechanic).

**PRECONDITIONS (KNOWN, assessed not rediscovered):** MS/RS naming fork — relitigated 3× in the
ledger (ED-428 keep RS → ED-731 propagate MS → ED-772 continue sweep) and the sweep never reached
`params/threadwork.md`, which still reads RS; a Godot typed export cannot bind this track until
one name wins. ED-1010/ED-1011 Coherence-cost contradictions gate wire-its 1/4/6.

---

## 5 · Degenerate-play hunt (Ω non-dominance under attack)

23 candidate dominant lines across 5 arenas (`01_workings/hunts/`). **Canon survived its
adversaries better than the finders expected**: every headline line that reached verification was
refuted by safeguards the min-maxers missed — a genuinely good non-dominance result. Notable
refutations (full records in `01_workings/refutations/`):

| Line (arena) | Refutation |
|---|---|
| General-Duel decapitation loop (mass) | No forcing mechanism exists; duels are bilateral (PP-506), unilateral entry pauses the battle; ED-898's no-death guarantee ≠ no-cost. |
| Treaty-hegemony GD-1 rush (faction) | Turmoil ≤6 is global (per-territory strain accrues regardless of treaty status); + three further safeguards. |
| "Four games collapse to one pattern" (social) | Venue-invariance is factually false — Argue attribute varies by adjudicator; proceedings gate styles differently. |
| Orientation payoff unwired (social) | `cr5_self_backfire` IS on the resolver path (resolver.py:404–419) — Obscuring's risk/reward is live. |
| Thread-site income faucet (settlement) | Deliberate tragedy-of-the-commons: RS is a shared peninsula resource; discovery is Investigation-gated. |
| Generalship-dominance axiom (mass) | The corpus's own Ω definition scopes dominance to *choice* dominance; Command superiority is the point (М-1 pressure), with in-doc counters. |

**Unverified candidates** (P3 or deferred by the verification cap — calibration-sensitive, most
gated on `[OPEN — Jordan tuning]` numbers; listed in `01_workings/deferred_unverified.json` +
`p3.json`): armor-tier no-downside stacking, counter/measure tradition imposition asymmetry,
ability-stacking with no budget enforcement (a *forward* hazard — `ability_primitives.py` has no
cap while config prose claims one), social Recall/Corroborate/Prep stacking with no global pool
cap, boost-lookup vs Appraise, coalition-vs-solo dominance (ED-297 ratified the coalition side —
the solo side may need a floor), split-beats-concentration (in-doc admitted, PP-508 — evidence
possibly contaminated per ED-MB-0002), Company-scale thread-cost arbitrage (rides ED-1010),
knot-anchoring Coherence regen (self-limiting via rupture risk). These are **sweep targets, not
verdicts** — see ed_options E-10.

---

## 6 · Cohesion: where consequence dies in transit

From the cohesion lens (all 12 dossiers' edges flattened; each spot-verified):

- **Consumer-side omission:** `scene.combat_resolved` declared with consumers
  npc_behavior/faction_layer/articulation whose own `consumes:` lists omit it
  (`module_contracts.yaml` L844 gap_note A4 — the registry knows).
- **Emitter-side sparse targeting:** 8 down-seams / 15 type-edges where consume intent is
  registry-canonical but strategic emitters leave `targets[]` unpopulated
  (`scale_transitions_v30 §12.4`) — top-down consequence delivers blind.
- **Terminal-sink death:** articulation consumes `*`, emits nothing, and fires no trigger for the
  flagship keys (F-4).
- **doc:null clusters on connective tissue:** `domain_actions` (the player's primary strategic
  verb; consumes:[]) and `engine_clock` (the temporal spine) are the least-specified modules at
  the most load-bearing junctions — emergent narrative currently rides declarations.
- **Vocabulary is not one language:** MS/RS; attribute roster 7 (glossary) vs 9
  (descriptor_registry/names_index) with both files self-declaring naming authority;
  `resonance_style` registry-DEPRECATED while npc_behavior runs Resonant Style live; enum forks
  ("structural"/"medium" outside the substrate's canonical enums — tracked); Command formula
  written against legacy attribute names (PP-232). Enforcement is warn-tier everywhere except
  the world-name gate. **Combat Pool is verified reconciled** (max(5, History+6) — do not
  re-report).

---

## 7 · Reconciliation ledger (what the refutation pass taught us)

The 25 refutations are design intel, not noise — the dominant pattern: **surface fact TRUE,
defect framing FALSE, intent DELIBERATE.** The corpus is better-defended than its docs are
legible: safeguards exist but live one line, one section, or one file away from where a reader
(or an audit finder) looks. Standouts:

| R# | Claim → resolution |
|---|---|
| R-1 | Combat has no player-input hook → code fact true; DELIBERATE staging (sim-first oracle; player interface is Phase-4-class work) — but *unscheduled*, which is the real residue (feeds E-9). |
| R-2 | Articulation is thread-blind → token absence true; the layer is deliberately Key-type-agnostic (wildcard + salience). Residue: generic salience cannot produce ED-681's authored crisis beats — a policy decision, not a bug (§4 item 2). |
| R-3 | NPC priority trees deterministic → structurally true; GD-2 mandates exactly this order (deterministic threat response *precedes* stochastic selection) — working as constrained. |
| R-4 | Thread absent from faction math → true at the formula level; P-14 governs thread *operations'* co-movement, which §3.5 delivers — opportunity, not violation. |
| R-5 | Governance redesign orphaned → its G1 prerequisite is BUILT (sim/territory/registry.py, 6 tests) — the refutation *strengthened* F-1: even less excuse for the proposal being untracked. |
| R-6 | GM-controls-votes hole → deterministic vote rule exists in the same section; stale wording sweep only (P3). |

Two refuted-as-duplicate items worth naming: `mechanics_index` conviction_scar cross-wiring
(cites the territorial Piety doc for the personal Scar mechanic — real, fold into S-1's register
hygiene) and the insurgency "11+ vs 15" figure (tracked, ratified — sim is authoritative at 15).

---

## 8 · [GAP:] register (completeness critic, corrected)

The critic misread scratch-file placement as missing coverage in several rows (all 12 dossiers
and 5 hunts returned full structured outputs — verified in `01_workings/`); corrected gaps:

- `[GAP-1]` **investigation_systems_v30 un-audited** — home of T-02/T-30 (rendering-as-
  consciousness, information asymmetry); no lane read it. Highest-value follow-up lane.
- `[GAP-2]` **32 P1/P2 candidates deferred unverified** (verification cap) — listed in
  `01_workings/deferred_unverified.json`; lowest-ranked P2s, none headline-class.
- `[GAP-3]` **Shape artifacts partially consulted** — `tools/observability/decisions.json`,
  `references/id_reservations.yaml`, and per-lane `handoffs/HANDOFF_<LANE>.md` were skimmed or
  unconfirmed-read by the shape lane (DECISIONS.md was read; the terse lane summary is thin).
- `[GAP-4]` **Top-down and forwards axes thin per-head** (see §2 matrix) — N/Ω verdicts
  concentrated in lenses; acceptable only because the lenses are declared their canonical homes.
- `[GAP-5]` **npc_behavior positive sweep under-evidenced** — both its candidate findings
  refuted; absence-of-finding for the concern/opinion/project engine rests on the dossier alone.
- `[GAP-6]` **Post-R2/R3 combat re-hunt ran against current code** (hunt cites live systems.py) —
  critic's claim of a stale sweep is wrong — but R3 is unexecuted (U0–U9 in flight), so the hunt
  must re-run after R3 lands.
- Process note: several workflow agents wrote scratch into the repo (and one into `undefined/` via
  a path bug); all consolidated under `01_workings/` — see its README for the manifest.

---

## 9 · Bottom line

The single highest-value action is **not** a new mechanic: it is **closing the transport-and-
rendering gap around the collision engine** — wire the declared-but-unconsumed edges (F-4's
triggers, combat_resolved consumers, §12.4 targets), give the Convergence Markers a detector
(F-2), and put the playability bar back on the index (F-3) — because the corpus already computes
more emergence than it can show, and every subsystem's North-Star score rises the moment
consequence actually arrives and renders. Sequencing, ED options, and governance follow in
`strategic_judgments.md` and `ed_options.md`.
