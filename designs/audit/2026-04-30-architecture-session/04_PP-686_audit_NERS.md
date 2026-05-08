# PP-686 Audit — NERS All Directions

**Subject:** `2026-04-30_PP-686_proposal.md` — Faction Behavior Architecture
**Auditor:** Claude (independent review of own draft)
**Generated:** 2026-04-30 · session token `6c31018e58b3844e`
**Scope:** Comprehensive NERS audit across top-down, bottom-up, vertical, diagonal, lateral, horizontal directions. Per project Specific Definitions: Necessary, Robust, Smooth, Elegant.

---

## §0 Executive Summary

PP-686 introduces a four-piece architecture (Mission, Cascade, Public Expectation, Legitimacy + Popular Support) replacing the current Ethical Framework Modifiers + Mandate-as-single-scalar. The audit finds the proposal **structurally sound but incomplete in three load-bearing places**:

| Verdict by direction | N | R | S | E |
|---|---|---|---|---|
| Top-down | STRONG | MODERATE | WEAK | STRONG |
| Bottom-up | STRONG | MODERATE | MIXED | STRONG |
| Vertical | STRONG | STRONG | MODERATE | MODERATE |
| Diagonal | STRONG | MODERATE | WEAK | MODERATE |
| Lateral | MODERATE | WEAK | WEAK | MIXED |
| Horizontal | MODERATE | MODERATE | MODERATE | MIXED |

**Three load-bearing gaps to flag immediately:**

1. **No specification of organizational hierarchy.** §3.2 references `supervisor(npc)` as if it exists; current NPC schema has Standing but no explicit supervisor edge. The Cascade math depends on this graph being authored. *Without this, the entire Cascade subsystem is implementation-undefined.*

2. **Aggregate effective_convictions is undefined.** §3.7 uses `faction.aggregate_effective_convictions` for Cascade alignment computation; §3.3 and §3.8 reference it; no aggregation function is specified. Power-weighted? Headcount? Tier-weighted by α-inverse? *Different choices produce materially different mechanical behavior.*

3. **DA category schema for Mission alignment is undeclared.** §3.1 refers to `da.category` and `mission.aligned_categories`; this taxonomy of DA categories does not exist in canon. *PP-686 silently introduces a new authoring requirement (DA → category mapping).*

These are not fatal but they prevent ratification as-drafted. Each is a one-paragraph fix.

**Beyond those three:** the proposal is more ambitious than the current discussion explicitly committed to. Specifically, §3.5 introduces a *Legitimacy violation event list* and §3.4 introduces a *5-temperament public typology* that were not in scope of the discussion. Both are reasonable; both should be flagged as additional Jordan-decision items rather than presumed approved.

---

## §1 Top-Down Audit (project intent → individual mechanic)

**Project intent:** *positive feedback loop between player decisions and mechanics that produces an engaging Godot videogame world with emergent narratives.*

### N (necessary)

**STRONG.** Faction behavior is the central political-strategic mechanic; a videogame depicting Renaissance peninsula politics requires it to function. The current Ethical Framework Modifiers system is anachronistic in vocabulary and static in evolution; a clean redesign is justified.

But: necessity is graded by leverage. PP-686 is **costly** (~6 sessions implementation) and **late** (Phase 2-3 work in v3 framing). Two cheaper alternatives could close the immediate problem:

- **(A) Vocabulary-only refactor.** Rename Ethical Framework labels to period-correct equivalents; keep static authored modifiers; ~1 session. Captures §1.1 and partial §1.4 but not §1.2 or §1.3.
- **(B) Mandate split only.** Separate Legitimacy + Popular Support; refactor Mandate consumers; ~2 sessions. Captures §1.3 but leaves vocabulary clash and static Ethical Framework problems.

PP-686 captures all four §1 problems. The cost is justified *if* all four are real for the gameplay experience. **Direction-specific check:** does the player notice the difference between PP-686 and (A)+(B) combined?

- (A)+(B) gives the player: faction stats with period-correct vocabulary, separable Legitimacy and Popular Support, Mission and Ethical Framework still authored.
- PP-686 adds: Cascade dynamic on succession; Mission shift; emergent faction modus from leader Convictions.

The added value is *succession dynamics* and *leader-modus coupling*. If the videogame's narrative arc spans multiple seasons with leader changes, PP-686's value is real. If most playthroughs see one or zero leader successions, PP-686 is over-built.

**Verdict:** N=STRONG conditional on multi-season multi-succession gameplay; otherwise the proposal is over-scoped relative to leverage.

### R (robust)

**MODERATE.** Robustness inputs check:

- *Player strategic depth:* the four-piece architecture creates real tradeoffs (high Legitimacy vs Popular Support trade; Mission alignment vs Cascade fidelity trade). ✓
- *Customization:* Mission, leadership selection, and organizational structure are authored per faction. ✓
- *Variety in approach:* a Crown can pursue mission via Honor-led cascade or via covert Utility-led; both viable, different costs. ✓
- *Player feels important:* DA submissions affect Legitimacy and Popular Support directly. ✓
- *Player feels they impact world:* Cascade math means leader's Conviction Scars (which player can influence at personal scale) propagate to faction modus. ✓
- *Emergent narrative without player:* Cascade re-resolution and L/PS drift run autonomously. ✓
- *Mechanics fully formed:* **PARTIAL.** The three §0 load-bearing gaps mean the spec is not fully formed. Strictness function is provisional; α calibration is provisional; Mission shift triggers are unenumerated.

Three of seven robustness sub-criteria are PARTIAL or PROVISIONAL. **R is not yet at "robust" quality.**

### S (smooth)

**WEAK.** Smoothness has multiple sub-criteria; PP-686 fails several.

- *Integrates without friction into existing game:* mostly. Mandate transitional preserves existing consumers. Faction-stat schema needs new fields (Legitimacy + Popular Support); migration affects every faction-aware system. ✓ with caveats
- *Mechanics interact cleanly with interdependent mechanics:* **WEAK.** The Cascade math depends on a supervisor graph (gap 1); aggregate effective Convictions depends on aggregation function (gap 2); Mission alignment depends on DA category schema (gap 3). Interactions with NPC behavior (`personal_convictions` drift via Conviction Scars) are described but not specified.
- *Zooms cleanly across scales:* personal Conviction → Cascade → faction modus chain is described; ✓
- *Transitions cleanly between mechanical systems:* **WEAK.** Connection to peninsular_strain is unspecified — does Strain affect Public Expectation strictness? Does faction Mission contribute to Strain? This is exactly the kind of cross-system invariant the lateral peer-system audit (audit week NERS §2.5) flagged as weak.
- *Pauses correctly:* unclear. When does Cascade re-resolution happen relative to Accounting, DA resolution, scene play? Spec says "each Accounting" but DA Ob is calculated *per DA*, which can fire during a season. Is Cascade re-resolved between DAs or only at season boundaries?
- *Calculation methodology consistent:* mostly. Dot products, weighted averages, integrators. Strictness function is non-linear and clamped — different from the rest of the system's mostly-linear forms.
- *Unified mechanical approach:* mostly. Same 0-7 scale, same Convictions vocabulary, same DA framework.

**Smoothness is the proposal's weakest dimension.** Three explicit cross-system specifications are missing.

### E (elegant)

**STRONG.** Elegance criteria:

- *Logically simple:* four authored inputs (Mission, Leader, Hierarchy, Role) → six derived state values. Reasonable cardinality. ✓
- *Clear approach:* every faction is the same triadic pattern; no per-faction special cases. ✓
- *No unnecessary overhead:* the existing Ethical Framework Modifiers required N×M authored entries; this requires N (one mission per faction) + role-template (small fixed table). Net authoring reduction. ✓
- *Easy to understand:* the four pieces have everyday English names (Mission, Cascade, Public Expectation, Legitimacy/Popular Support). The vocabulary collision was the primary inelegance of the prior system. ✓
- *Player intuits complex outcomes from simple choices:* "I should make Almud the leader because her Honor will cascade through the Crown" — this is intuitable. The non-monotonic strictness function is the only piece requiring the player to learn a non-obvious rule. ✓ with one exception

**Verdict (top-down):** N=STRONG-conditional, R=MODERATE, S=WEAK, E=STRONG.

---

## §2 Bottom-Up Audit (individual mechanic → engine coherence)

### N

**STRONG.** Each component answers a real mechanical need:
- Cascade: needed because succession should change behavior.
- Mission: needed because telos drives action selection.
- Public Expectation: needed because external modulation produces tradeoff space.
- Legitimacy + Popular Support: needed because acceptance and active backing are different resources.

### R

**MODERATE.** Sub-criteria check:
- Each component has explicit inputs, outputs, derivation. ✓
- Components compose cleanly: Mission feeds Public Expectation, Cascade feeds Cascade Fidelity feeds Popular Support, Legitimacy + Popular Support feed strictness. ✓
- Edge cases handled? **PARTIAL.** What if a faction has no leader temporarily? What if leader has 0 personal_convictions weights set? What if hierarchy has an orphan NPC (no supervisor, not the leader)? What if cascade_fidelity computation has zero-magnitude vectors? **None of these edge cases are addressed.**
- Numerical bounds enforced? Mostly. Legitimacy and Popular Support clamp [0,7]; strictness clamps [0,1]; Ob_modifier clamps [-3,+3]. But cosine_similarity for cascade_fidelity ranges [-1,+1] — what does -1 (anti-aligned with role) actually do mechanically? Not enumerated.

**Mechanics not yet error-free or complete.**

### S

**MIXED.** Component interactions:
- Mission alignment + Cascade alignment + Expectation alignment summed → clean. ✓
- Legitimacy + Popular Support → strictness → Ob → DA outcome → Δ Legitimacy + Δ Popular Support: this is the feedback loop. **It is not specified whether this is positively or negatively damped.** A poorly-tuned strictness function could oscillate. The Stage 10 sim verification covers this, but the proposal doesn't acknowledge the risk.
- Cascade re-resolution timing vs DA submission: not addressed (see §1 S point 5).

### E

**STRONG.** Component-level elegance:
- Cascade math is one line (`α × personal + (1-α) × supervisor`). Recursive but bounded. ✓
- Strictness function is one line. ✓
- Ob calculation is one expression. ✓
- Cosine similarity for Cascade Fidelity is standard math, no novel primitive. ✓

**Verdict (bottom-up):** N=STRONG, R=MODERATE, S=MIXED, E=STRONG.

---

## §3 Vertical Audit (scale-axis coherence: personal ↔ settlement ↔ territory ↔ peninsula)

### N

**STRONG.** Scale-bridges in PP-686:

- Personal → faction: leader's `personal_convictions` enter cascade root.
- Faction → settlement: faction's territorial DAs affect settlements per existing mechanics; PP-686 doesn't disturb.
- Settlement → faction: outcomes accrue to Mission delivery measurement; populace temperament aggregates from territory populations.
- Faction → peninsula: peninsular Strain affects faction state per existing mechanics; PP-686 doesn't disturb.

Two new scale-bridges: leader→cascade and territorial-public→Popular-Support. Both necessary.

### R

**STRONG.**
- Personal-scale Conviction work (PP-681 Conviction Track promotion, PP-684 taxonomy) is the input layer; PP-686 reads from it. ✓
- Settlement-scale already exists; PP-686 doesn't add settlement-scale state. ✓
- Faction-scale: PP-686 adds Mission, Cascade, Legitimacy, Popular Support, Public Expectation. ✓
- Peninsula-scale: PP-686 doesn't add peninsula state, but Public Expectation strictness function reads from Legitimacy + Popular Support which are faction-scale. Is there a peninsula-scale aggregate (e.g., "Crown Mandate across the peninsula")? Mandate is per-faction in current canon, so PP-686 inherits this. ✓

The PP-666 trio (settlement adjacency, fractional province ownership, faction succession split) — still open per editorial ledger ED-710, ED-711 — provides territory-scale infrastructure that PP-686 implicitly assumes (faction Missions may reference specific territories, which need to know their settlement composition for outcome attribution). **PP-686 has a soft dependency on PP-666 trio resolution.**

### S

**MODERATE.**
- Cascade is implicitly per-territory? Or peninsula-wide for the faction? §3.2 doesn't say. If a faction has different territorial governors, do those governors form *parallel cascades* per territory? Or is there one global cascade per faction? **This is unresolved.** The Crown has Almud at the head, but Crown territories may have different lords-lieutenant; their cascades could be locally distinct. *This is a vertical-scale specification gap.*
- Aggregation upward (Cascade Fidelity at faction level) vs downward (effective_convictions at NPC level) is mathematically clean.
- Aggregation across territories (faction's effective temperament from territorial publics) is asserted but not specified.

### E

**MODERATE.**
- The leader-as-cascade-root assumes flat hierarchy across the faction. Realistic Renaissance factions have *multiple parallel hierarchies* (Crown's secular governance + Crown's military command + Crown's household). The single-tree assumption is elegantly simple but factually inadequate. **Tradeoff: simplicity now, fidelity later, or hybrid (multiple cascade roots per faction)?**

**Verdict (vertical):** N=STRONG, R=STRONG, S=MODERATE, E=MODERATE. **Cascade-per-territory question is the load-bearing unresolved item.**

---

## §4 Diagonal Audit (cross-scale + cross-system interactions)

### N

**STRONG.** PP-686 explicitly targets diagonal dynamics:
- Personal Conviction Scar → Cascade → faction modus → DA Ob → strategic outcome → Legitimacy/Popular Support → strictness → next-DA-Ob. This is a multi-scale, multi-system chain.
- Public temperament (per-territory) → Popular Support (faction-level) → strictness (faction-level) → DA Ob (per-DA) → outcome (per-territory). Another diagonal.

### R

**MODERATE.**
- Trace legibility (per E-DIAG-A featured-behavior carryover from doc 17): the cascade chain is legible if UI surfaces it. **PP-686 mentions a debugging cascade map but does not specify default UI exposure.** This is the same opacity-vs-legibility question §6.2 of doc 17 was working out (E-TOP-A) — it recurs here at faction scale.
- Long-horizon stress: a faction whose leader has a Conviction crisis (Scars 3+) becomes *unstable Cascade root*. Faction modus would oscillate randomly. The proposal doesn't explicitly address this; it'd cascade through. Whether this is dramatically rich (Tudor instability under unstable monarch) or mechanically broken (faction state thrashes) depends on damping the proposal doesn't specify.
- 12-year time-horizon: Mission shifts, Legitimacy slow drift, Popular Support faster drift — does the system reach equilibrium or stay dynamic? Stage 10 sim is supposed to verify; spec acknowledges as provisional.

### S

**WEAK.**
- Coupling to npc_behavior_v30: does NPC autonomous behavior consume `effective_convictions` or `personal_convictions`? **Different choice produces different gameplay.** A clerk reading their effective Convictions for daily action behaves as institution; reading personal Convictions behaves as individual. **The proposal doesn't say which.** This is a major specification gap because npc_behavior_v30 is the entire NPC simulation engine.
- Coupling to scene_slate, social_contest: scene-scale mechanics generate events that feed the Event Impact Matrix; do those events affect Legitimacy / Popular Support? Implicit yes (DA resolution affects them) but scene-scale events outside DA framework (a publicly witnessed insult, e.g.) — do they?
- Coupling to mass_battle: a battle outcome surely affects Popular Support (Mission delivery if the battle was a Mission objective) and possibly Legitimacy (mass casualties under contested orders). PP-686 doesn't specify.

### E

**MODERATE.**
- The single triadic Ob calculation is elegant.
- The diagonal chains (leader → Cascade → modus → Ob → outcome → L/PS → strictness) compose elegantly *in spec* but their elegance depends on the diagonal chains being legible to the player. Without UI surfacing, the diagonals become opaque emergent behavior — simulation rather than gameplay.

**Verdict (diagonal):** N=STRONG, R=MODERATE, S=WEAK (npc_behavior coupling unspecified), E=MODERATE.

---

## §5 Lateral Audit (peer systems at the same scale)

### N

**MODERATE.** PP-686 is faction-scale; peer systems at the same scale include:
- Turmoil (peninsula-scale, but interacts with faction-scale)
- Faction stats (Standing, Mandate, etc.)
- Domain Action framework (cross-faction)
- Faction relations (Disposition matrices between factions)

PP-686's relationship with each is partial. Necessity is moderate because the prior canon's Ethical Framework was lateral-incomplete; PP-686 is *more* lateral-engaged but not fully so.

### R

**WEAK.**
- Turmoil interaction: does Strain affect strictness? Strain affects the populace; the populace sets temperament; high Strain probably shifts temperament toward "outcomes-only" (high α_temperament). **Not specified.**
- Cross-faction Disposition: faction A's Mission may align or oppose faction B's Mission. Does that drive Disposition shifts? **Not specified.**
- DA framework interaction: PP-686 modifies Ob, but DA framework has its own Ob logic. Do they multiply, add, override? Spec says modifier is added; need to verify against current DA Ob computation chain.
- Faction succession (PP-666): when a faction succession event fires, the cascade root changes mid-stream. PP-686 references "leader change triggers re-resolution" but PP-666's succession-split mechanic creates *two simultaneous cascade roots*. **Direct interaction unaddressed.**

Lateral robustness is the weakest direction in this audit.

### S

**WEAK.**
- Cohesion → Discipline rename (PP-232) was a peer-system vocabulary unification this week; PP-686 introduces *new* faction vocabulary (Mission, Cascade, Public Expectation, Legitimacy, Popular Support, Cascade Fidelity, Strictness) — 7 terms — without addressing how they relate to the existing Mandate, Standing, Disposition, Reputation lexicon. **Vocabulary debt risk.**
- Lateral integration not simulated. The audit week NERS already flagged: "lateral peer-system case (faction_layer × mass_battle × social_contest at scene scale) was not its own simulation pass." PP-686 reinforces this: faction-layer expansion proceeds without lateral cross-system invariant testing.

### E

**MIXED.**
- The proposed system is itself elegant.
- It composes elegantly with NPC Convictions (same vocabulary).
- It composes *less* elegantly with Mandate, Standing, Disposition (parallel vocabularies for adjacent concepts: Standing for individual rank, Mandate for institutional standing, Legitimacy for populace acceptance — overlapping semantics).
- It does not compose explicitly with Strain, peer-faction Disposition, or DA category framework.

**Verdict (lateral):** N=MODERATE, R=WEAK, S=WEAK, E=MIXED. **This is the audit's weakest direction. Multiple peer-system specifications missing.**

---

## §6 Horizontal Audit (sequence/temporal: turn order, phase order, event chaining)

### N

**MODERATE.**
- Cascade re-resolution timing (per Accounting) — specified.
- Legitimacy and Popular Support drift (per Accounting) — specified.
- DA Ob calculation timing (per DA) — implicit.
- Mission shift trigger timing (per major state change event) — vague (see §6 open question 8).

Necessary horizontal specifications: when does each piece update, in what order? Partial.

### R

**MODERATE.**
- Within-season order: Cascade → Public Expectation → strictness → DAs run with that strictness → outcomes accumulate → end-of-season Accounting updates Legitimacy/Popular Support → next season Cascade re-resolves with potentially-changed leader Conviction. **This is implicit in the design but not explicit.** A new author or developer would have to reverse-engineer the order.
- Race conditions: if Cascade re-resolves at Accounting and DAs fire mid-season, can a leader change *during* a season produce a half-season cascade? **Not specified.**

### S

**MODERATE.**
- Damping: the proposal mentions 0.3 drift coefficient for Cascade re-resolution but no damping for Legitimacy or Popular Support oscillation.
- Event ordering for Legitimacy violations: if two violations fire same season (a heresy + a coup), do they sum, max, or process sequentially? **Not specified.**

### E

**MIXED.**
- Stable simple sequence (each season: cascade → expectation → DAs → outcomes → drift) is elegant.
- The mid-season leader-change edge case is inelegant (or unspecified).
- The non-monotonic strictness function adds horizontal complexity (changing strictness mid-season as Legitimacy/PS update would create non-linear DA cost dynamics).

**Verdict (horizontal):** N=MODERATE, R=MODERATE, S=MODERATE, E=MIXED.

---

## §7 Findings Summary — by Severity

### P1-CRITICAL (block ratification)

**P1-1.** Organizational hierarchy / supervisor graph schema not specified. §3.2 Cascade math is implementation-undefined. *Resolution:* add §3.2.1 specifying the supervisor graph as authored faction state; integrate with NPC schema.

**P1-2.** Aggregate effective_convictions function not specified. §3.7 references it; §3.3 cascade_fidelity needs it. *Resolution:* add §3.3.1 specifying aggregation (recommended: power-weighted by Standing × tier-position).

**P1-3.** DA category schema for Mission alignment undeclared. §3.1 references `da.category` and `aligned_categories` without defining the category space. *Resolution:* enumerate DA categories or reference the canonical source.

### P2 (block stage 10 sim verification but not ratification)

**P2-1.** NPC behavior coupling to effective_convictions vs personal_convictions unspecified. Major gameplay implications. *Resolution:* explicit §3.9 Integration Notes specifying which Conviction set drives autonomous NPC behavior.

**P2-2.** Cascade-per-territory vs cascade-per-faction question unresolved. Multiple parallel hierarchies (Crown's secular + military + household) cannot be modeled with single-tree cascade. *Resolution:* §3.2.2 specifying multi-root cascade or explicit single-root constraint with justification.

**P2-3.** Strain interaction not specified. Strain affects populace; populace sets temperament; temperament weights Popular Support drivers. *Resolution:* §3.4.1 connecting Strain to temperament dynamics.

**P2-4.** Edge cases unaddressed: leaderless faction, zero-vector cascade_fidelity, orphan NPCs, leader Conviction crisis (Scars 3+). *Resolution:* §3.10 Edge Cases.

**P2-5.** Mid-season leader change handling. *Resolution:* explicit ordering specification.

### P3 (improvements; not blocking)

**P3-1.** UI specification for cascade legibility (E-DIAG-A recurrence at faction scale). *Resolution:* defer to Phase 5a Godot spec.

**P3-2.** Damping for Legitimacy / Popular Support oscillation. Sim verification will calibrate. *Resolution:* note in §3.5 / §3.4.

**P3-3.** Vocabulary debt — 7 new terms vs existing Mandate/Standing/Disposition lexicon. *Resolution:* glossary unification pass after PP-686 implementation.

**P3-4.** Multi-violation same-season ordering. *Resolution:* §3.5 sub-clause.

**P3-5.** Cross-faction Disposition shifts from Mission alignment. *Resolution:* explicit out-of-scope statement or §3.11.

### Forward observations

- **F-1.** PP-686 is dependent on PP-684 (Conviction taxonomy) and soft-dependent on PP-666 trio. If those don't ratify, PP-686 needs revision.
- **F-2.** The proposal's complexity (~6 sessions) is at the upper end of single-PP scope. Consider splitting into PP-686a (Mission + Cascade core) and PP-686b (Public Expectation + Legitimacy + Popular Support) if implementation slips.
- **F-3.** Strictness function is non-monotonic and may produce unintuitive gameplay. Stage 10 sim is supposed to validate; consider an explicit "strictness regression test" battery.

---

## §8 NERS Verdict Matrix

| Direction | N | R | S | E |
|---|---|---|---|---|
| Top-down | STRONG (conditional on multi-succession gameplay) | MODERATE (3 partial sub-criteria) | WEAK (3 cross-system specs missing) | STRONG |
| Bottom-up | STRONG | MODERATE (edge cases unaddressed) | MIXED (oscillation risk unacknowledged) | STRONG |
| Vertical | STRONG | STRONG | MODERATE (cascade-per-territory unresolved) | MODERATE (single-tree assumption) |
| Diagonal | STRONG | MODERATE (legibility deferred) | WEAK (npc_behavior coupling unspecified) | MODERATE |
| Lateral | MODERATE | WEAK (4 peer-system specs missing) | WEAK (vocabulary debt) | MIXED |
| Horizontal | MODERATE | MODERATE (race conditions unaddressed) | MODERATE (damping unspecified) | MIXED |

**Aggregate:** the proposal is **structurally sound and ambitious** but has **5 P1+ items and 5 P2 items requiring resolution before ratification**. None invalidate the architecture; all are specification completeness issues.

The proposal's **strongest direction is top-down/elegance** (vocabulary unified, four-piece architecture composes cleanly).

The proposal's **weakest direction is lateral** (peer-system integrations under-specified) and **second-weakest is diagonal smoothness** (npc_behavior coupling is the load-bearing unresolved question).

---

## §9 Recommendations

### §9.1 Immediate (before any commit of PP-686 to register)

1. Resolve the three P1 items inline in the proposal (organizational hierarchy schema, aggregate function, DA category schema). Each is a one-paragraph fix.
2. Add §3.9 Integration Notes specifying NPC behavior consumes `effective_convictions` for institutional/professional behavior and `personal_convictions` for autonomous personal-scale behavior (resolving P2-1).
3. Add §3.10 Edge Cases (resolving P2-4).
4. Add §3.2.2 multi-root cascade allowance with explicit per-cascade-root accounting (resolving P2-2).

After (1)-(4), the proposal is ratifiable. Remaining P2 items (Strain interaction, mid-season leader change) become Stage 10 sim verification targets.

### §9.2 Short-term (during implementation)

5. Run the lateral cross-system invariant simulation pass that the audit week NERS flagged as missing. PP-686 is the right scope for that pass: Mission/Cascade × Strain × DA framework × peer-faction Disposition. This is a Phase 4-grade simulation chain.
6. Treat Stage 10 sim verification as broader than parity check. It should also verify (a) no oscillation in feedback loop, (b) no mid-season race conditions, (c) strictness function produces intuitive outcomes across L × PS state space.

### §9.3 Strategic

7. **Consider splitting PP-686 into PP-686a + PP-686b** if scope creep threatens. Splitting along the Cascade boundary (PP-686a = Mission + Cascade; PP-686b = Public Expectation + Legitimacy + Popular Support) gives two ratifiable proposals with clear interface.
8. **Defer UI specification to Phase 5a Godot spec.** The cascade map and Public Expectation legibility decisions should be made when the Godot UI scope is concrete.
9. **Note PP-686 as a candidate for early Godot prototyping.** It's complex enough that paper specification alone may miss interactions; building a small Godot prototype of the cascade math + Ob calculation against current 6-faction state could surface defects faster than sim alone.

---

## §10 Verdict

**Status:** PROVISIONAL with **5 P1 items requiring resolution before ratification** and **5 P2 items for Stage 10 verification scope**.

**Architecture:** sound. The four-piece decomposition (Mission, Cascade, Public Expectation, Legitimacy + Popular Support) is structurally clean and captures dynamics current canon cannot. Vetting block (§5 of proposal) is well-grounded.

**Specification:** incomplete. Three load-bearing gaps (supervisor graph, aggregate function, DA category schema) prevent ratification as-drafted.

**Direction strengths:** top-down necessity, bottom-up necessity, vertical robustness, top-down elegance.

**Direction weaknesses:** lateral robustness (4 peer-system specs missing), diagonal smoothness (npc_behavior coupling unspecified), horizontal smoothness (mid-season race conditions).

**Recommendation:** revise to address P1 items, then submit for ratification. Do not commit to register until §9.1 items 1-4 are integrated.

---

**End audit.**
