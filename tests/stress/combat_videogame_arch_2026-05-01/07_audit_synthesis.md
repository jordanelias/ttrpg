# Combat Stress Test — Self-Audit (2026-05-01)

**Subject:** the NERS-all-directions analysis produced 2026-05-01 in
`tests/stress/combat_videogame_arch_2026-05-01/` (commit 06dae57).
**Method:** look for methodological flaws, biases, internal contradictions, coverage gaps,
overconfident claims, unverified evidence, and missing counterfactuals.
**Stance:** adversarial — assume the synthesis is wrong somewhere and locate where.
**Effort:** max. The synthesis is not canon and the audit is intended to catch the things
that would embarrass it during ratification.

The audit finds the synthesis directionally credible but methodologically softer than its
confidence implies. The composite stack is *one* coherent answer, not the only one;
several decisions were stated with more certainty than the evidence supports; and at least
two findings have internal contradictions worth flagging before any of this is canonized.

---

## Section 1 — Methodological flaws

### 1.1 NERS-all-directions was not consistently applied at full grain

The framework declared 6 directions × 4 NERS = 24 cells per idea. In practice:
- Chunk 3 used per-direction rows with 4 NERS columns — **24 cells** per candidate. ✓
- Chunk 4 used the same format. ✓
- Chunk 5 collapsed to per-direction rows with single verdict + notes — **6 cells** per candidate, not 24. ⚠
- Chunk 6 Q4/Q5/Q6 collapsed further — single-row tables with 6 verdict columns and no NERS breakdown — **6 cells** per candidate. ⚠

The framework's full grain was applied to the first two questions and informally collapsed
for the remaining four. This is a methodology drift the synthesis didn't disclose. It means
half the analysis is at one resolution and half is at another. Conclusions from the
collapsed sections should not be treated with the same confidence as conclusions from the
full-grain sections.

**Severity:** medium. Findings still hold directionally; specific NERS scores in the
collapsed sections are not actually scored, they're inferred.

### 1.2 The 6 directions are not orthogonal

- "Top-down" and "Bottom-up" are a clear pair (whole→part vs part→whole). Orthogonal. ✓
- "Vertical" (scale traversal) and "Horizontal" (campaign time) are conceptually distinct. Orthogonal. ✓
- **"Diagonal" (cross-system) and "Lateral" (same-scale parallel) overlap.** A scene-combat-to-social-contest interaction is both cross-system AND same-scale parallel.

The framework treated diagonal and lateral as distinct lenses but never specified the
boundary. In Chunks 3–6, several findings appear under both lenses (Threadwork interactions,
Conviction Track integration). Findings double-counted across overlapping directions inflate
the apparent coverage.

**Severity:** low-medium. Doesn't invalidate findings but it means "passed all 6 directions"
is closer to "passed ~5 distinct lens checks."

### 1.3 NERS criteria were not numerically weighted

✓/⚠/✗ scoring without weights treats N (necessary), E (elegant), R (robust), S (smooth) as
equal. Project canon defines them as different criteria with different stakes — N is
existence; E is presentation; R is depth; S is integration. A failure on N is categorical
(the mechanic isn't present); a failure on E is fixable (UI rework). Treating them
equivalently in vote-counting was a methodology shortcut.

This affects Chunk 5's I3 verdict ("✗ on bottom-up — canonical scene math is discarded
during mass battles"). N and R both ✗. That should be a categorical reject, not a 4-vote-of-6
reject. The verdict was right but the methodology made the rejection look softer than it is.

**Severity:** low. Findings unchanged but comparative strength claims (e.g., "I2 is the
clear winner") are less robust than presented.

### 1.4 Scoring threshold drift between candidates

I scored T2 (canonical phase-locked) as ⚠ on top-down "blind-declare UI is hard to make
legible" but scored T4 (active-time gauge) as ✓ on top-down "videogame-medium native."
These are similar UI claims for similar systems. The difference in score is closer to my
preference than to a measurable distinction.

Chunk 4: S1 continuous got ⚠ on top-down for "depth tax on legibility"; S7 zoned got ⚠ on
top-down for "loses some emergent-positioning depth." Both ⚠ for opposite reasons. The ⚠
is doing different work in each, which the synthesis collapses into "both partial."

**Severity:** medium. The cumulative pattern of these threshold drifts favored my
preferred candidates.

---

## Section 2 — Confirmation bias

### 2.1 The "drop zone abstraction" thesis was front-loaded

Chunk 3 introduced T2+T4 as a candidate. Chunk 4 introduced S7-hybrid (sub-zone continuous)
as a candidate. Both happened to make the strongest case for moving beyond zone abstraction.
Chunk 7's synthesis declared zone-abstraction-removal as "the single largest decision."

But by the time the synthesis declared this, every prior chunk had already scored candidates
in a way that favored the conclusion. The synthesis didn't *discover* the conclusion — it
*recognized* it because the candidate space was constructed to make it inevitable.

**Counterfactual not tested:** what does the design space look like if zone abstraction is
*preserved*? An honest stress test would have included S0 = "preserve TTRPG zone abstraction
unchanged in videogame medium" as a candidate alongside S1–S8, and scored it. It wasn't.

This is the audit's most serious finding. The thesis was prefigured by candidate selection.

**Severity:** high. The recommendation may still be right, but the analysis doesn't
demonstrate that the recommendation is right *over the canonical alternative*. It only
demonstrates the recommendation is internally coherent.

### 2.2 Reference selection bias

Chunk 2 surveyed 30+ shipped systems. The top-10 picks all happened to map cleanly to
canonical Valoria mechanics. This pattern is suspicious:

- Pirates! ↔ canonical pool split (Chunk 2 §1)
- Sekiro posture ↔ canonical Stamina (§2)
- Grandia IP ↔ canonical phase resolution (§3)
- XCOM cover ↔ canonical Soft/Hard cover (§4)
- Mutant Year Zero stealth ↔ canonical Exposure ladder (§5)

Either Valoria's canonical mechanics are uncannily aligned with the best-of-class videogame
design history (possible but unlikely) or I selected references that map cleanly and skipped
references that don't map cleanly. I almost certainly did the latter without flagging it.

**Counterfactual not tested:** which acclaimed combat systems have NO clean canonical
mapping? Total War's army-scale doctrine, Dragon's Dogma's pawns + climbing, EYE: Divine
Cybermancy's mental-instability layer — all influential, all hard to map to canon. They
weren't surveyed because they wouldn't have produced lift recommendations.

**Severity:** medium. The references cited are real and the mappings are largely correct,
but the survey was selection-biased toward systems that vindicate canon.

### 2.3 Every preferred candidate I introduced won

T2+T4 won. S7-hybrid won. I2 won (with I1/I4 as fallbacks). A+C won (B dropped). E1+E6+E7
won (no replacement). F2+F3 won. **Six of six.** No design analysis at this scale produces
six-of-six clean wins for a single coherent thesis. The probability that each decision is
independent and each wins is low; the pattern indicates the decisions are not independent —
they are corollaries of the same prior commitment, dressed as distinct findings.

**Severity:** medium-high. The recommendations should be presented as one decision (drop
zone abstraction → here's what falls out), not six decisions (each independently
recommended after testing). The current framing inflates apparent confidence.

---

## Section 3 — Internal contradictions

### 3.1 "Canonical math preserved" vs zone-removal

Synthesis Chunk 7 §1 claims "canonical resolution math is fully preserved." Synthesis §2
classifies §5 Reach/Zone/Cover as a major rewrite ("Add sub-zone continuous-position spec.
Convert zone reach (Melee/Ranged) to threshold distances within sub-zone").

Reach matrix IS canonical math. Zones ARE part of the canonical reach mechanic. Converting
"Melee/Ranged zone" to "threshold distance" is a math change, not a presentation change.
The two claims are inconsistent; the synthesis used "canonical math preserved" as a
selling-point in the headline while the §2 file-by-file detail acknowledged the math is
changing. The headline is misleading.

What's actually preserved: Combat Pool calc, weapon TN matrix, damage formula, Wound
Interval, Stamina cost table, Threadwork +1 Ob per Wound. What's changing: reach mechanic
(zone-discrete → threshold-continuous), Fibonacci proximity check (zone-implicit → radius-
explicit), Cover application (zone-flat → LoS-aware).

**Severity:** medium. Real but partially disclosed in the §2 detail; the headline is the
problem, not the analysis.

### 3.2 "B dropped" vs I4 retained

Chunk 6 Q5 dropped B (DD-slot formation) on grounds that "S7-hybrid + variable zone size
makes the slot pattern unnecessary." Chunk 5 retained I4 (hero-detached parallel scenes)
as a fallback for scene↔mass interface. I4's mechanism is essentially: hero plays at scene
scale on a *bounded sub-region*, units act at mass scale; outcomes merge per-round.

A bounded sub-region with fixed actor count, adjacent-only reach, push/pull movement IS the
slot formation pattern. The synthesis claims to drop slot formation at scene scale and then
re-introduce it at scene-vs-mass scale interface. The decision to drop B at scene was not
based on evidence that slot patterns are bad — only on the assertion that S7-hybrid
*could* emulate them. The decision didn't test whether emulation is as good as native.

**Severity:** medium. B may still be the right thing to drop, but the argument is weaker
than presented. A more careful version would say: "B's slot pattern is preserved as I4's
internal structure for parallel scenes; B is not needed as a primary architecture but its
design pattern remains present."

### 3.3 "Same clock for scene + mass" vs canonical Cascade Phase ordering

Chunk 3 recommended T2+T4 with the claim that scene and mass tick on the same clock,
"eliminating the canonical phase-mode-switch (PP-089/090, mass_battle §A.7)."

`mass_battle_v30 §A.7` defines a Cascade Phase with explicit ordering: Manoeuvre → Thread
→ Engagement → Volley → Damage Resolution → Discipline. This ordering is canonical. The
synthesis claimed an IP-gauge tick eliminates the phase mode-switch — but the IP-gauge tick
is per-actor, while the Cascade Phase is per-battle. They are different time abstractions.

A unit's IP gauge filling does not naturally map to "the battle's Manoeuvre phase
completing." Either the synthesis intends Cascade Phase to dissolve into per-actor IP ticks
(in which case canonical phase ordering is not preserved — a major canon change not flagged),
or Cascade Phases are retained and IP gauges live within phases (in which case the "same
clock" claim is decorative — phases still happen, the gauge is just visible).

The synthesis didn't disambiguate. Both readings have problems.

**Severity:** high. This is the flagship vertical-scale-traversal claim and it's
under-specified.

### 3.4 "I2 all directions ✓ or ⚠ once" overstates

Chunk 5 verdict for I2: "All 6 directions ✓ or ⚠ once; no ✗." Inspection of the table:
- Top-down ⚠
- Bottom-up ⚠
- Vertical ✓
- Diagonal ✓
- Lateral ✓
- Horizontal ✓

That's two ⚠s, not one. Minor but the synthesis's claim of cleanest-of-all-candidates
overstates the cleanliness.

**Severity:** low. Mistake, not bias. Worth fixing.

---

## Section 4 — Coverage gaps

The original brief explicitly asked about "equipment and stuff" and "buildings and multiple
characters" — and asked for testing of "many ideas many ways." The stress test addressed
some of these and missed others.

### 4.1 Equipment / loadout depth never tested

The brief said "and equipment and stuff." Canonical weapon TN matrix was used as a constant
in every analysis, but the *loadout space* — what weapons, armor, shields, ranged ammo,
Conviction-themed gear, faction-specific equipment — was not stress-tested at all. R
(robustness) explicitly includes "allows for customization of characters" — coverage of
that direction is essentially nil.

What should have been tested: does the architecture support loadout-driven tactical depth?
Does S7-hybrid let mixed-loadout parties (one ranged, two melee, one with shield) play
tactically distinctly? Does C duel scale across weapon class diversity (sword duel vs
sword-vs-spear vs sword-vs-bow)? None of this was assessed.

**Severity:** high. Gap in original scope.

### 4.2 Buildings / interiors only briefly handled (S8)

S8 (elevation) was the only acknowledgment of building interiors and it was framed as
"high-value extension to recommend per-scene." That's not adequate to the brief's question
about "buildings." Specifically untested:
- Interior combat with breakable doors, traversable windows, multi-room navigation
- Sieges (canonical PP-088 Siege Assault Linkage referenced but not tested)
- Stealth with corner-peeking, blind spots
- Interior-vs-exterior LoS asymmetry

These are central to videogame-medium combat. The synthesis treated them as an extension
rather than a primary axis.

**Severity:** medium-high.

### 4.3 AI / NPC behavior never specified

Every architecture I scored implicitly assumed NPCs have appropriate combat AI. Combat AI is
where most CRPG systems break — Pillars 2's engagement system felt good when AI used it
correctly and felt broken when AI didn't. The stress test never asked: what's the AI
authoring cost per architecture? How many distinct AI behavior trees does A vs C need? The
synthesis declared C "lowest-cost architecture to prototype" but C requires a specifically
intelligent dueling AI (commit-and-tell reads, stamina management, environmental Stunt
exploitation). C may actually be the *highest* AI-authoring cost.

**Severity:** medium-high. Affects implementation cost estimates which were already low-
confidence.

### 4.4 Player feel / juice / hit reactions ignored

Combat is a videogame's most kinesthetic system. The synthesis evaluated mechanics, time-
shape, spatial substrate — none of the audio-visual-haptic feedback layer. The "Pirates!
duel feels good" or "Sekiro deflect feels good" phenomena are not reducible to the
mechanical dimensions tested. C's case for cinematic weight was made on mechanical grounds
(stance + tell + posture); the actual reason Pirates! and Sekiro work is feel. The synthesis
has no theory of feel.

**Severity:** medium. This is the kind of thing prototyping (Phase 0 spike) catches.
Acceptable to defer to prototype but the synthesis should have flagged it.

### 4.5 Multiplayer / co-op / save granularity

Out of scope per project intent (single-player). Acceptable.

### 4.6 Difficulty scaling

Not tested. Canon `combat_v30` doesn't have explicit difficulty modifiers — encounter
difficulty is implicit in stat blocks. The shift to videogame medium permits difficulty
sliders. Untested.

**Severity:** low. Fixable later.

### 4.7 Performance at scale

Mass battle with 100 unit blocks at I2 continuous-zoom is a performance question. The
synthesis handwaved this with "intermediate zoom renders schematic icons; full zoom spawns
individuals." That's the right architecture but the load-test threshold was never named.
A 100-unit battle with 30 individuals visible per zoom level may run; a 1000-unit battle
may not. Canonical mass battle scope (mass_battle_v30 §A.3) defines battle scales — those
weren't cross-checked against I2 feasibility.

**Severity:** medium. Affects whether I2 ships at all.

---

## Section 5 — Evidence quality

### 5.1 Game-mechanic claims unverified

Chunk 2 cited specific mechanics for ~30 games. Most were paraphrased from training-data
recall without verification. Per project guidance, factual claims about specific products
should be verified with web search. Examples that should have been but weren't:

- Pirates! "three vertical guards (high/middle/low). Three attacks per guard." [UNVERIFIED]
  — multiple Pirates! editions exist (1987, 1993, 2004); duel mechanics differ across them.
- Wartales "movable initiative bar" — [UNVERIFIED] — the actual UI is a turn-order tracker;
  whether it's draggable depends on edition and class.
- Wakfu/Dofus "AP/MP separated" — [UNVERIFIED] — generally correct but specifics vary.
- Sekiro mikiri counter mechanic — [UNVERIFIED] — paraphrase mostly accurate but not
  rigorously checked.

The mappings to canonical Valoria primitives don't depend on the citations being precise —
the patterns are correct in the abstract. But the chunk implies precision it didn't earn.

**Severity:** medium. Mappings hold; details may be off.

### 5.2 Implementation cost estimates unfounded

Chunk 7 §3 gave engineering estimates flagged [CONFIDENCE: low]. The flag is appropriate
but the estimates are still treated as planning input in subsequent prose ("Phase 1 MVP:
2-3 engineers × 6 months"). Without a Godot scoping pass, the estimates are guesses
dressed as a phased ship plan.

**Severity:** medium. The phasing makes sense as conceptual structure; the calendar
specifics should be removed or properly disclaimed.

### 5.3 Player-experience claims unfounded

Multiple ✓ scores for "horizontal direction" (campaign-time pacing) were given based on no
playtesting and no precedent comparison. T2 horizontal got ⚠ "risk of repetition fatigue
without animation variety" — this is speculation about playtest behavior I have no data on.
T4 horizontal got ✓ "compresses well for routine combat (gauges fill faster); slows for
set-pieces" — also speculation.

**Severity:** low. Acceptable for exploratory analysis, but the synthesis treated these
scores as findings.

---

## Section 6 — Counterfactuals not tested

### 6.1 "Preserve canonical zones unchanged"

The strongest counterfactual to the central thesis. Not scored. Should have been S0 in
Chunk 4. Hypothesis: the canonical zone abstraction continues to work at videogame scale
with minor visualization extensions (zones as visible map regions, transitions as movement
between regions). What does that look like? Is it actually worse than S7-hybrid or just
*different*? The audit cannot answer because the analysis didn't test it.

### 6.2 "Adopt B-as-primary, drop A"

The opposite simplification from what was recommended. DD-slot is famously approachable.
What does Valoria look like if all combat is slot-formation, with C as the duel set-piece?
Not tested.

### 6.3 "Three-architecture stack with A+B+C"

Tested in Chunk 1 originally; absorbed into Chunk 6 Q5's "drop B" decision. The
three-architecture case for *higher tactical variety* (B for routine, A for open-field, C
for duel) was dismissed without a careful comparison of design surface cost vs encounter
type variety.

### 6.4 "No mass battle in videogame; abstract resolution only"

The brief permits this. Chunk 5 I7 was scored as fallback only. But it's a real design
choice: ship with no playable mass battle, focus on scene combat. Pillars 2 effectively
made this choice. Not seriously evaluated.

### 6.5 "Real-time as primary"

T5 (pure real-time) was rejected as not generalizing. But many CRPGs (Dragon Age: Origins,
Pillars 2 default) ship real-time-with-pause as the primary tempo. The objection ("canonical
math friction") may not be as severe as scored — RTwP doesn't bypass canonical TN, it just
animates it. T3 scored higher than T5 but the gap may have been overdrawn.

---

## Section 7 — Specificity gaps

Several decisions are stated as adopted but not specified at the level of canon-readiness:

| Decision | Missing specification |
|---|---|
| "Sub-zone continuous space" | Sub-zone units (m? abstract distance?), reach thresholds in those units, default sub-zone size per encounter type |
| "IP gauge ticks" | IP rate formula (Agi-derived? Discipline-derived at mass scale?), interrupt cost, gauge max value |
| "Stamina banking ≤ 1.5× max" | Banking action cost, banking decay, can banking be lost on Wound, what triggers commit |
| "Posture-as-yield" | Yield is voluntary or mechanical, post-yield state (re-enterable? mortally exposed?), Conviction effect of yielding |
| "C trigger six conditions" | Trigger precedence when multiple fire, refusal cascade specifics, T-Hero-Officer trigger detail |
| "F2 same-map continuous" | Time-shape transition mechanism (does world freeze? What about non-combatant NPCs nearby?) |
| "F3 stealth Exposure ramp" | Detection thresholds, sound radius, line-of-sight rules, silent-elimination pre-conditions |

The synthesis adopted these decisions as if they were complete; in fact each is a slot for
significant additional spec work. Item count: ~7 decisions × 3-6 missing specs each = ~25-40
sub-specifications net-new on top of the 8 net-new sections already counted in Chunk 7 §2.

The canon refactor cost in §2 is **understated**.

**Severity:** high.

---

## Section 8 — Findings the audit *did not* contradict

To be fair to the synthesis, several findings hold up under audit:

- **Two-architecture (A+C) is structurally sound** even if the argument-for-dropping-B is
  weaker than presented. The design surface case is real.
- **Pirates! → C mapping is genuinely strong.** The mechanical correspondence between
  three-stance-plus-footwork and canonical pool-split-plus-Establish-Distance is not
  manufactured; it's structural.
- **T2 (canonical phase-locked) at scene scale is preserved** — the canonical primitive
  survives whatever happens at mass scale.
- **F2 (same-map continuous bridge) makes sense in the videogame medium.** Even if details
  are missing, modal transitions between fieldwork and combat are a known pain point in
  shipped CRPGs.
- **The 10 residual risks (R1–R10) flagged for Jordan are real and well-chosen.** The
  audit doesn't add any large new risks beyond what synthesis Chunk 7 §4 already named —
  it reframes some, rates them differently, but doesn't surface omissions.

The synthesis's directional read is plausibly correct. What it isn't is sufficiently
demonstrated.

---

## Section 9 — Audit's risk additions to R1–R10

The original synthesis flagged R1–R10. The audit adds:

- **R11 — Canonical math is partially modified, not preserved.** Reach mechanic, Fibonacci
  proximity check, Cover application all change form. The synthesis's headline ("math
  preserved") understates the change.
- **R12 — Same-clock claim vs Cascade Phase ordering.** §3.3 contradiction unresolved.
  Fundamental to T2+T4 unification. Must be specified before adoption.
- **R13 — Loadout/equipment tactical depth not validated.** R (robustness) criterion
  inadequately tested in original brief's explicit "equipment and stuff" axis.
- **R14 — Building interior combat depth not validated.** S8 elevation as extension is not
  the same as a tested building-interior architecture.
- **R15 — AI authoring cost per architecture not assessed.** May invert the cost ranking.
- **R16 — Player-feel layer not addressed.** Phase 0 spike must validate before commitment.
- **R17 — Performance load-test threshold for I2.** May gate I2 from shipping at scale.

Adding R11–R17 to the Jordan-decision queue is the audit's main concrete output.

---

## Section 10 — Recommended remediation

Before any of the synthesis is canonized, the following remediation is recommended:

1. **Score S0 (preserve canonical zones unchanged).** Add to Chunk 4 retroactively. Compare
   directly to S7-hybrid using full NERS-all-directions grid. Decision needed: is the
   thesis-front-loading bias confirmed?

2. **Resolve §3.3 contradiction.** Specify whether Cascade Phases dissolve into IP ticks or
   are preserved within the IP gauge framework. Net-new canon spec one way or the other.

3. **Audit Chunks 5–6 with full NERS grain.** Re-score with 24-cell tables to bring
   methodology consistent with Chunks 3–4. May change verdicts.

4. **Run Phase 0 spike before declaring composite stack.** Specifically test S7-hybrid with
   loadout variety, building interior, and AI authoring. The spike is cheap relative to
   the cost of canonizing wrong.

5. **Verify Chunk 2 game-mechanic claims via web search** for any reference cited in the
   top-10 picks. Pirates! editions specifically.

6. **Surface the sub-spec gaps in §7 to the canon refactor cost in Chunk 7 §2.** Add 25–40
   sub-specifications to the count. The cost-of-canonization is meaningfully higher than
   stated.

7. **Add R11–R17 to the Jordan-decision queue.**

---

## Conclusion

The synthesis produces a coherent design stack that respects canonical resolution math at
its core. Its central thesis — drop the TTRPG zone abstraction; treat scene combat as a
tempo+camera shift on a continuous map — is defensible.

The synthesis overstates its rigor. It applied the NERS-all-directions framework
inconsistently, scored the same kinds of issues differently across candidates, was
prefigured by candidate selection, and has at least three internal contradictions worth
resolving before canonization (§3.1, §3.3, §3.2). It also has coverage gaps on equipment,
buildings, AI, and player feel that the original brief explicitly named.

The headline finding ("canonical math survives all variants") is not strictly true.
Canonical *resolution* math survives; canonical *reach/zone/cover* math is being modified.
The headline papers over this distinction.

The recommendation: treat the synthesis as a **first-pass exploration**, not a near-canon
proposal. The directional claims (drop zone abstraction, T2+T4 visualization, S7-hybrid
substrate, A+C two-architecture, F2+F3 bridge) are worth pursuing further. The
specifications around them are not yet canon-ready. The 10 residual risks (R1–R10) plus
audit's additions (R11–R17) total 17 Jordan-decision items, not 10.

Status of synthesis: **EXPLORATORY first-pass; needs second-pass with audit remediations
before canon ratification.**
