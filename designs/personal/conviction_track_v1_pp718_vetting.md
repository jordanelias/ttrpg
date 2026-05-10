# PP-718 — Full M-1..M-11 Vetting Walkthrough

**Subject of vetting.** PP-718 ratifies per-Conviction Scar accumulation under PP-684's structured-concentration model. It rewrites `conviction_track_v1.md §2` so that:

1. Crisis fires when **any single Conviction** hits 3+ Scars (not the aggregate Scar count).
2. Multi-primary NPCs Scar each Conviction independently.
3. Cultural-background-only crises (weight 0.2–0.4) produce muted narrative drift.
4. Crisis-table roll 5 is rewritten: legacy "Autonomy survival" → Self-Other-orientation override (Autonomy is no longer canonical, renamed Liberty per PP-684).
5. Pre-PP-684 Scar counts carry forward attached to the migrated Conviction per PP-685 mappings (Reason→Scholastic, Continuity→roster-determined, Autonomy→Liberty).

**Class.** B — system extension. Scar Accumulation is an existing mechanic (canonical at `conviction_track_v1.md §2/§3`); PP-718 extends it to interact correctly with the structured-concentration vector model PP-684 introduced for personal Convictions and the corresponding faction-Cascade math (PP-686 §3.2).

**Vetting protocol.** Per `references/throughlines_meta.md §8.1` Class B: **N → Μ → М → Τ → Q** (Ω inherited from PP-684). All M-1..M-11 must be rated per §3 rubric.

---

## N — Necessity

**N-1: Renaissance dynamic modeled.** The dynamic at stake is *moral injury under sustained value-conflict*. A Renaissance political actor — bishop, magistrate, captain — operating across multiple value-frames (Faith + Authority + Honor in a Cardinal; Authority + Virtue in a Captain) accumulates moral wounds on each frame independently. The Catherine de' Medici regency stress on Catholic Faith vs Politique Order is the canonical reference: she did not have an "aggregate moral wound counter" — her Faith was wounded by St. Bartholomew's, her Order was wounded by the wars of religion, her Virtue was wounded by political compromises, **separately**. Period biographies and political theology track these as distinct strands.

The legacy aggregate-Scar reading was a single-primary-model artifact. Once PP-684 introduced multi-primary structured concentration, the aggregate reading became incoherent — a Cardinal with primary Faith + Authority + Honor would crisis at 3 Scars regardless of *which* Convictions were wounded, which is not how Renaissance political actors collapsed.

**N-2: Already covered?** The aggregate Scar mechanic existed (legacy). It cannot be retained in the new vector model without producing the absurdity above. Per-Conviction extension is the minimal repair, not a new mechanic.

**N-3: Meaningfully different player situations?** Yes — concretely. Under aggregate, a 3-primary Cardinal facing one Faith-rupturing event and one Authority-rupturing event reaches 2/3 toward crisis after two events. Under per-Conviction, the same Cardinal needs 3 Faith-events OR 3 Authority-events OR 3 Honor-events for crisis. This **slows crisis** for multi-primary NPCs, which is correct: Renaissance figures with broader value-bases were more resilient under sustained pressure (the Habsburg-Catholic combination was load-bearing for Charles V's longevity).

**N-4: Load-bearing?** Yes — the Conviction Crisis is the canonical mechanism by which NPC arc transitions fire (Almud Reformer/Fortress/Overthrown per `complete_systems_reference §1.4`). If crisis-firing is incoherent under the canonical taxonomy, every NPC arc's trigger conditions are incoherent. Load-bearing on the entire NPC arc system.

**N-5: What is lost without this fix?** Either (a) leave aggregate semantics in place and accept that multi-primary NPCs crisis no faster than single-primary (functionally equivalent to the structured-concentration update being silently ignored at the Scar layer), or (b) treat the spec as undefined and rely on Game Master adjudication. (a) makes PP-684's structured concentration cosmetic at the crisis layer; (b) is exactly the spec ambiguity the conviction_stress_01 stress test surfaced.

**N verdict: pass.** Not flagged to Jordan.

---

## Μ — Modes (primary served + non-undermining check)

| Mode | Served? | Reasoning |
|---|---|---|
| Μ-α PRESSURE AS ENGAGEMENT DRIVER | **Primary** | Per-Conviction Scar accumulation is the moral-pressure-per-Conviction-vector mechanic. Continuous: every Thread event witnessed scars one or more named Convictions per the §3 matrix. Forces engagement: an NPC accumulating Scars on Faith cannot ignore Faith-engaging decisions; the engine rolls on the crisis table once Faith hits 3+. The pressure is *named* by Conviction rather than accumulated to a single counter. |
| Μ-β AUTONOMOUS AGENT COMPOSITION | **Secondary** | NPC priority trees consume Conviction state per Resonant Style Taxonomy (`npc_behavior §1.3`). Per-Conviction crisis means an NPC's crisis-state varies by which Conviction was Scarred — different Resonant Styles activate; different Solidarity / Authority / Evidence / Consequence vulnerabilities fire. Cardinal-with-Faith-crisis behaves differently from Cardinal-with-Authority-crisis. Multi-NPC scenes produce composition events that depend on *which* Conviction crisis is active for each agent. Extends agent-composition emergence. |
| Μ-γ SUBSTRATE ONTOLOGY | **Not undermined** | Convictions are the interpretive substrate for personal-scale value-frames per `conviction_taxonomy_v30 §1` ("the engine's interpretive substrate"). The per-Conviction reading preserves that grounding — every Conviction is a vector axis on the substrate, and Scars are state-changes on that axis. The aggregate-Scar reading would collapse the axes back into a scalar, which would silently demote the substrate from vector to scalar at the crisis layer. Per-Conviction preserves substrate vectorization. |
| Μ-δ CROSS-SCALE CONSEQUENCE | **Not undermined** | Personal-scale Conviction state feeds faction-scale Cascade math (PP-686 §3.2 — `effective_convictions` aggregated from member NPCs). Per-Conviction crisis at personal scale produces named-axis erosion at faction scale (a Cardinal in Faith-crisis erodes Church's faction-aggregate Faith vector). Aggregate-Scar reading would pass an undifferentiated "crisis" signal up; per-Conviction passes the *axis* of crisis. Faction Cascade can then respond to *which* axis is destabilizing — extends cross-scale consequence specificity. |

**Primary Μ served:** Μ-α (pressure) + Μ-β (agent composition).
**Modes undermined:** none.

**Μ verdict: pass.** Two modes primarily served; two modes preserved.

---

## М — Pattern ratings (full M-1..M-11 walkthrough)

Rubric per `throughlines_meta §3`: **+** extends · **✓** satisfies · **−** violates · **○** does not apply to proposal scope.

### М-1 Pressure is continuous · Parent Μ-α

**Pattern.** Pressure is continuous; mechanics that purport to apply pressure must do so without rest-state. Canonical T-instances: T-04 MS Decay, T-05 CI Accumulation, T-06 IP Accumulation, T-07 Turmoil, T-12 Practitioner Arc (secondary).

**Application to PP-718.** Per-Conviction Scar accumulation makes the moral-pressure-per-axis mechanic continuous *per axis*. The legacy aggregate reading actually had a subtle rest-state problem: a 3-primary NPC facing 2 events on Faith plus 0 events on Authority/Honor was 2/3 toward crisis aggregate, but actually 2/3 toward crisis on Faith and 0/3 on Authority/Honor. Aggregate told the engine "almost in crisis" when in fact two of three primaries were untouched — the NPC could withstand far more pressure on those axes without the aggregate counter telling truth. Per-Conviction restores the per-axis pressure-continuity: each axis has its own counter, and pressure on Faith does not insulate Authority from continued pressure.

The new mechanic also preserves canonical pressure-continuity from the §3 Thread-event matrix: each Thread operation Scars a named subset of Convictions. Pressure is continuous because the matrix continues to fire on every Thread event witnessed (subject to the season cap of 1 Scar per season per NPC from Thread witnessing per `conviction_track_v1 §3`).

**Rating: ✓** Satisfies. **Recalibrated 2026-05-10 from initial +.** On independent-reviewer reconsideration: PP-684 itself carries M-1 + for the vector-pressure-axis instantiation ("Convictions provide axis for continuous-pressure interpretation" per `conviction_taxonomy_v30 §7`). PP-718 ensures the Scar layer composes correctly with that PP-684 extension — eliminating the latent aggregate-rest-state defect — but the per-axis pressure-continuity pattern was *already* introduced by PP-684's structured concentration. PP-718 is faithful operation of an extension already credited; rating it + here would double-count PP-684. The mechanic still satisfies M-1 robustly: per-axis Scar accumulation produces continuous per-axis pressure with no rest-state on the addressed axis.

### М-2 Geography holds pressure · Parent Μ-α, Μ-δ

**Pattern.** Pressure distributes spatially; geographic features hold or release pressure. Canonical T-instances: T-18 Radiation Gradient, T-19 Southernmost Hidden Front (primary). Secondary on T-38.

**Application to PP-718.** Conviction is a personal- and faction-scale interpretive mechanic; it does not distribute pressure spatially. NPCs in different territories can have different cultural-background templates (per `conviction_taxonomy_v30 §5` — varfell_alpine, crown_lowland, valorian_court, etc.), and the templates are coupled to factional/cultural geographies, but the **Scar mechanic itself does not gate on geography**. A Faith-Scar on a Cardinal in T9 Cathedral is the same mechanically as a Faith-Scar on the same Cardinal in T1 Crown territory.

There is one mild geographic-pressure adjacency — Thread events in calamity-radiation bands (T-18) produce more Scars per witnessing because the events themselves are more frequent, and territorial Forgetting universality (PP-703) means TS-50+ practitioners witnessing in calamity-zones cannot opt out. But that pressure is geographic at the *Thread-event-frequency* layer, not at the Scar-mechanic layer. The Scar-counting math is geography-blind.

**Rating: ○** Does not apply. PP-718 is a personal-scale state-counting clarification; geography is upstream.

### М-3 Substrate grounds all · Parent Μ-γ

**Pattern.** Every element is Thread-substrate configuration. Canonical T-instances: T-01 Everything Is Thread, T-02 Rendering Consciousness-Performed, T-03 Inseparability (primary); broad secondary coverage.

**Application to PP-718.** Convictions are the *interpretive substrate* per `conviction_taxonomy_v30 §1`: "Each of the 13 Convictions projects onto the 4-axis substrate (PP-687 §2.4) via a 13×4 matrix. The matrix is the engine's *interpretive substrate*." Convictions are not flavor-tags; they are vector-valued substrate axes.

PP-718 preserves this substrate-vectorization at the Scar layer. The aggregate-Scar reading would have collapsed the vector to a scalar at exactly the moment the mechanic became most interpretively significant (crisis). Per-Conviction Scar accumulation maintains the vector all the way through to the crisis transition — the engine knows *which axis* destabilized, and that knowledge propagates to faction-Cascade (Μ-δ above) and to Resonant Style activation (Μ-β).

The cultural-background distinction (weight 0.2–0.4 vs primary 0.6–0.8) is also substrate-grounded: cultural-background Scars produce muted narrative drift rather than full arc transition because the cultural-background weight is less load-bearing on the substrate vector. The mechanic differentiation is ontologically grounded, not arbitrary.

**Rating: +** Extension. Preserves and extends substrate-vectorization through the Scar/crisis layer where aggregate would have collapsed it.

### М-4 Institutions stake substrate-postures · Parent Μ-γ

**Pattern.** Factions take substrate-postures that distinguish them from each other. Canonical T-instances: T-08 Church Rendering Reinforcement, T-09 Varfell Thread Progressive, T-11 Crown Pragmatic, T-15a/b/c (Hafenmark/Löwenritter/RM substrate-postures), T-21 Thread Political Warfare, T-27 Effects Real Explanation Wrong, T-32 Sincere Structural Closure, T-39 Textual Mode Typology.

**Application to PP-718.** Faction substrate-postures consume aggregate Conviction vectors via Cascade math (PP-686 §3.2). Per-Conviction Scar accumulation at member-NPC level produces axis-specific erosion at faction-aggregate level, which makes faction substrate-postures more responsive to specific kinds of moral injury rather than generalized crisis.

Concrete example: the Church's substrate-posture is **rendering-reinforcement** (T-08). A Cardinal in Faith-crisis erodes the Church's Faith-axis specifically, which is the Church's load-bearing axis. A Cardinal in Order-crisis (e.g., Cardinal Justice the Inquisitor having his procedural framework wounded by Tribunal politics per `npc_behavior §2.13`) erodes the Church's Order-axis without touching its Faith-axis — and the Church's substrate-posture (rendering-reinforcement = Faith-grounded) is therefore *not* equally undermined. Aggregate would have signaled equal erosion regardless of axis.

This is a strict extension: per-Conviction crisis means faction substrate-postures degrade by *which axis is wounded*, not by undifferentiated cardinal-count. The rating is not just "satisfies" — it actively distinguishes Church (Faith-load-bearing) from Crown (Authority/Utility-load-bearing) from Varfell (Honor/Warden-load-bearing) under sustained NPC moral injury.

**Rating: +** Extension. Distinguishes axis-specific institutional erosion from undifferentiated faction-crisis.

### М-5 Scales connect through substrate · Parent Μ-δ

**Pattern.** Cross-scale consequence flows through shared substrate. Canonical T-instances: T-15 Player Progression, T-16 Knot Propagation, T-23 NPC Arc Emergence, T-24 Convergence as Crisis, T-25 Generational Arc, T-26 Recursion, T-34 Distal Interoception, T-36 Relational Ontological Identity, T-40 TS as Taxonomic Expansion.

**Application to PP-718.** Personal-scale Scar accumulation feeds faction-scale Cascade per PP-686 §3.2 (already covered in М-4) and arc-scale transitions per `complete_systems_reference §1.4` (Almud Reformer/Fortress/Overthrown gated on Conviction state).

T-23 NPC Arc Emergence specifies: "personal arc → faction Domain Echo → political shift → new arc triggers." Per-Conviction crisis specifies *which* personal arc transitioned (Almud Faith-crisis vs Almud Authority-crisis vs Almud Virtue-crisis), which then specifies *which* faction Domain Echo fires, which specifies *which* political shift propagates — chained axis-specific propagation across scales.

T-24 Convergence as Crisis: convergence happens *on a specific axis*. Multiple NPCs in Faith-crisis simultaneously converge on a Faith-axis crisis at faction scale. The aggregate reading would not distinguish a Faith-convergence from an Order-convergence; per-Conviction does.

T-25 Generational Arc: 30-year campaign clock. Per-Conviction Scar tracks let the engine record which Convictions are most-wounded across a generation — a campaign where Faith was repeatedly wounded across 30 years produces a different generational arc than one where Authority was wounded.

**Rating: +** Extension. Cross-scale propagation is now axis-specific rather than aggregate-blind.

### М-6 Choice is forced · Parent Μ-α

**Pattern.** Choice carries cost; no rest-state evasion. Canonical T-instances: T-12 Practitioner Arc, T-13 Certainty Journey, T-14 Conviction Architecture, T-17 Companion Moral Mirror, T-20 Two Contests, T-22 Belief Lattice (primary).

**Application to PP-718.** **T-14 Conviction Architecture** is the most directly relevant T. T-14's specification: "Forced-choice — Scar accumulation forces arc transitions." Per-Conviction Scar accumulation makes the forced-choice mechanic *per-axis*: an NPC with high Faith Scar count faces forced choices on Faith-engaging decisions specifically, while their other primaries remain stable. This produces a richer choice space — the NPC isn't simply "in crisis" or "not"; they're in crisis on a *named axis* and stable on others.

The crisis-table roll 5 update is also a forced-choice extension: the legacy "Autonomy survival" interpretation gave the crisis NPC a single defection escape (always Autonomy-aligned). The new Self-Other-orientation override per PP-684 §3 is multi-valenced: high positive Self-Other → self-aggrandizing action; strongly negative → self-sacrificing action; mid-range → pragmatic. The single defection-escape is replaced by a value-drift that has actually been accumulating across the campaign per PP-684 §3.2 drift formula. Forced choice now has continuity with the NPC's Self-Other history, not a stochastic reset.

T-22 Belief Lattice: cooperation requires Belief revision, which is Scar-accumulation. Per-Conviction Belief revision means an NPC's cooperation cost is axis-specific. The Cardinal who must cooperate with a Crown captain on a Mandate motion may need to revise *Faith*, *Authority*, or *Honor* depending on what the cooperation entails — and the Scar accrues on the revised axis. Aggregate would have undifferentiated this.

**Rating: +** Extension. Forced-choice is now per-axis; defection-escape is value-history-grounded rather than stochastic.

### М-7 Borrowings are operational extensions (composite assembly) · Parent Μ-γ, Μ-β

**Pattern.** Scholarly-lineage concepts are deployed within operational architecture; framework-original in assembly. Per `throughlines_meta_infill §3.4`: Husserl epoché, Metzinger PSM, Block phenomenal-vs-access, Global Workspace, Kierkegaard leap and repetition, Lacan Real and Symbolic, apophatic theology + Ein Sof, Lurianic Kabbalah, clinical-trauma phenomenology family, Gibsonian ecological psychology, ART, extended mind, wayfinding, art brut.

**Application to PP-718.** The Conviction taxonomy borrows from Renaissance political-theological vocabulary (Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor — each with period-equivalent Latin per `conviction_taxonomy_v30 §2`). The borrowing is operational: each Conviction is a vector axis with calibration on hierarchical/sacred/instrumental/traditional axes per `conviction_axis_matrix_v30`, not a mere flavor label.

PP-718 does not introduce new borrowings. It preserves the existing borrowing-architecture (the 13-Conviction Renaissance mapping) and extends it to interact correctly with the structured-concentration vector model. The Scar mechanic is itself a clinical-trauma-phenomenology borrowing (per М-9 below): "moral injury" in the Litz/Shay clinical sense is the source register, ontologically inverted to substrate-real per Valoria's pattern. PP-718 does not alter the borrowing's source register or operational deployment.

**Rating: ✓** Satisfies. Preserves existing composite assembly without introducing or violating borrowing-architecture.

### М-8 Access is vertical-position gated (within the renderable) · Parent Μ-β, Μ-γ

**Pattern.** What a being can receive is gated by position relative to ordinary rendering. Canonical T-instances: T-30 Information Asymmetry as Core Mechanic (primary), T-35 Unified Uncanny Capacity Synthesis (primary extension), with secondary on T-31, T-32, T-33, T-37, T-40.

**Application to PP-718.** Conviction Scars are accrued by witnessing Thread events (per `conviction_track_v1 §3` matrix). Witnessing is access-gated: "Witness requirement: Direct witness (present in scene) or credible testimony (Evidence Track contribution + Disposition ≥ +1)." The witnessing condition is canonical pre-PP-718.

PP-718 doesn't change witnessing semantics. Per-Conviction Scar tracking is downstream of witness — once witnessed, the Scar accrues to the named Conviction(s) per the §3 matrix. The access-gating layer (whether the NPC saw it) is upstream and untouched.

Cultural-background Convictions (weight 0.2–0.4) Scar on the same matrix; the muted-drift rule applies after the Scar is recorded, not at witness layer. The vertical-position gate (was the NPC there to see it?) is preserved at the witness layer; the substrate-vector gating (which Conviction is wounded?) is the extension PP-718 adds at a different layer.

**Rating: ✓** Satisfies. Preserves access-gating at witness layer; the new per-Conviction tracking does not penetrate or violate the access boundary.

### М-9 Ontological inversion of clinical phenomenology · Parent Μ-γ, Μ-α

**Pattern.** Clinical phenomenology vocabulary preserved; condition rendered as real in the world (substrate ontological), not delusional in the patient. Per `throughlines_meta_infill §3.6`: 12+ instances across Sessions 1–7 — anosognosia ↔ Prophylaxis, Capgras ↔ Fragmented band, Cotard ↔ Coherence 0 freefall, neglect ↔ non-sensitive formation, split-brain confabulation ↔ Church doctrinal output, DPDR ↔ Coherence-degraded inner phenomenology, etc.

**Application to PP-718.** The Conviction Scar mechanic is the framework's ontological-inversion of *moral injury* (Litz, Shay — clinical trauma phenomenology of value-violation). In the clinical register, moral injury is a perceiver-pathology condition: the patient experiences value-violation as wounding because the act conflicted with their internalized values. In the framework, moral injury is **substrate-real**: the Conviction-vector axis on which the value lives actually destabilizes; faction-Cascade aggregates pick up the axis-specific erosion; arc transitions fire from canonical-state changes. The wound is in the substrate, not in the perceiver's interpretation.

PP-718's per-Conviction extension *strengthens* this ontological inversion. Under aggregate, the Scar count was a perceiver-side accumulator (an NPC's "moral wound-meter"). Under per-Conviction, the Scar is recorded *on the substrate axis itself* — Faith-axis Scars actually lower the Faith vector's weight (per the §2 Effect column: "Conviction X weight may shift downward; other primaries gain proportionally"). The clinical register reads "moral injury depleted Faith"; the framework reads "Faith-axis substrate-vector decremented." Same phenomenology; ontologically inverted.

The crisis-table roll 5 update — Self-Other-orientation override — also strengthens М-9 alignment. The Self-Other axis is itself a substrate axis per `conviction_taxonomy_v30 §3`, with canonical drift formula `Δ orient = κ × Σ(outcome_with_self_benefit) − κ × Σ(outcome_with_collective_sacrifice)`. The legacy "Autonomy survival" reading gave the crisis NPC a generic defection escape; the new reading routes the defection through the *substrate state* of Self-Other — a substrate-grounded escape rather than a perceiver-side instinct.

**Rating: ✓** Satisfies. **Recalibrated 2026-05-10 from initial +.** On independent-reviewer reconsideration: the clinical-moral-injury → substrate-real ontological inversion was canonized in the legacy `conviction_track_v1.md` original (the Scar mechanic itself *is* the inversion: clinical moral injury → substrate-axis-state actually destabilizing, not perceiver pathology). PP-684's own vetting block credited M-9 + specifically for "Self-Other drift is a new state-evolution dynamic" — the substrate-grounded routing PP-718 leverages for roll-5. PP-718 routes the *existing* inversion through PP-684's vector model and routes roll-5 through PP-684 §3.2 drift; both inversion contributions are upstream. Rating + here would double-count: once for PP-684's Self-Other drift, once for PP-684's vector-substrate, once for legacy v1's moral-injury inversion. The mechanic faithfully preserves and composes with all three; that is ✓, not a new instance.

### М-10 Environment as constitutive medium (bounded by the renderable) · Parent Μ-δ, Μ-γ

**Pattern.** Environment is constitutive of practitioner capacity, not backdrop. Per `throughlines_meta_infill §3.7`: 4E cognition (embodied, embedded, extended, enactive); Gibsonian direct perception; ART restorative environments; ontologically-reciprocal place attachment via knot profile; Clark-Chalmers extended cognitive coupling through knot channels; Tolmanian/Lynchian wayfinding. Canonical T-instances: T-34 Distal Interoception (primary), T-38 Real as Continuous Amplitude (primary extension); T-33, T-16, T-40 secondary.

**Application to PP-718.** Conviction Scar accumulation operates on personal-scale state without environmental constitution. The Scar mechanic counts events; the events themselves may be environmentally grounded (Thread operations occurring in calamity-radiation territories per T-18) but the Scar-counting layer is environment-blind.

There is one environmental hook: **cultural-background templates** (per `conviction_taxonomy_v30 §5` — eight templates, each tied to a regional/factional culture) constitute the NPC's interpretive ambient register. An NPC raised in `varfell_alpine` carries Community + Warden + Precedent at low cultural-background weights even if their primary is Liberty or Scholastic. This *is* an instance of environment-as-constitutive-medium at character-creation time. But PP-718 doesn't introduce or alter the cultural-background mechanic; it specifies that cultural-background Scars produce muted drift (a downstream consequence of the existing environmental constitution, preserving its original weight differential).

**Rating: ✓** Satisfies. Environment-as-constitutive holds at character-creation/cultural-background layer pre-PP-718 and post-PP-718. PP-718 preserves this without extending into new environmental territory.

### М-11 Voluntary and involuntary capacity duality · Parent Μ-α, Μ-γ

**Pattern.** The same structural capacity yields opposite valences depending on agency and context. Per `throughlines_meta_infill §3.8`: DPDR involuntary at Coherence degradation (distressing) ↔ voluntary at high-TS opacity practice (cultivated); peritraumatic dissociation involuntary trauma protection ↔ cultivated confrontation training; meta-awareness involuntary at Coherence degradation ↔ cultivated at TS development. Canonical T-instances: T-31 Reflexive Suspension, T-33 TS as Developmental Arc, T-40 TS as Taxonomic Expansion (primary extensions).

**Application to PP-718.** The Conviction Scar mechanic produces involuntary destabilization (the NPC didn't choose to be Scarred; the Scars accrued from witnessing). At 3+ Scars on a Conviction, the NPC enters crisis — the canonical involuntary pole.

The mechanic also has a voluntary pole, indirectly: NPCs (and PCs via ED-664 Player Conviction Checks) can avoid Scar accumulation by avoiding witness, by maintaining Disposition < +1 to information-brokers (per `conviction_track_v1 §3` witness-requirement), by Player Conviction Checks (Spirit pool TN 7 Ob 1) at the time of witnessing. The cultivation of Conviction stability is voluntary; the Scar itself is involuntary.

PP-718 preserves both poles. Per-Conviction tracking gives the NPC (and the player guiding them) more granular voluntary navigation options: an NPC who anticipates Faith-Scar pressure in an upcoming season can voluntarily avoid Faith-engaging witness situations; under aggregate, every avoidance was generic and the NPC could not target the at-risk axis. Per-Conviction makes voluntary stability cultivation **per-axis trainable** — extending the voluntary pole's resolution.

The crisis-table roll 5 (Self-Other override) is itself voluntary-ish: Self-Other orientation drifts under accumulated outcomes per PP-684 §3.2, which means the NPC's Self-Other state at crisis-time reflects the campaign's cumulative voluntary choices. The defection-escape now routes through accumulated voluntary outcomes, not stochastic instinct.

**Rating: +** Extension. Per-Conviction tracking extends voluntary-pole resolution (axis-specific cultivation); roll-5 Self-Other routing connects involuntary-pole crisis to voluntary-pole drift history.

---

## М summary

| М | Pattern | Rating | One-line justification |
|---|---|---|---|
| М-1 | Pressure is continuous | ✓ | Faithful per-axis operation of PP-684's vector-pressure extension (PP-684 itself carries M-1 +); per-Conviction Scar accumulation eliminates the latent aggregate-rest-state defect |
| М-2 | Geography holds pressure | ○ | Personal-scale state-counting; geography is upstream at Thread-event-frequency layer |
| М-3 | Substrate grounds all | + | Preserves substrate-vectorization through crisis layer; cultural-background muted-drift is substrate-grounded |
| М-4 | Institutions stake substrate-postures | + | Axis-specific institutional erosion distinguishes Church/Crown/Varfell load-bearing axes |
| М-5 | Scales connect through substrate | + | Cross-scale propagation now axis-specific (T-23/T-24/T-25 chains carry which-axis info) |
| М-6 | Choice is forced | + | Forced-choice per-axis (T-14); defection-escape value-history-grounded (T-22) |
| М-7 | Borrowings are operational extensions | ✓ | Preserves existing 13-Conviction Renaissance composite without altering borrowing architecture |
| М-8 | Access is vertical-position gated | ✓ | Access-gating at witness layer preserved; per-Conviction tracking is downstream of witness |
| М-9 | Ontological inversion of clinical phenomenology | ✓ | Faithful preservation of legacy v1's moral-injury inversion + PP-684's Self-Other drift contribution; PP-718 routes existing inversions through vector model rather than introducing new instances |
| М-10 | Environment as constitutive medium | ✓ | Cultural-background template environmental constitution preserved; muted-drift is downstream consequence |
| М-11 | Voluntary and involuntary capacity duality | + | Per-axis voluntary cultivation extends voluntary-pole resolution; roll-5 connects voluntary drift to involuntary crisis |

**Five +, five ✓, one ○, zero −.**

**Recalibration note (2026-05-10).** Initial walkthrough (commit 39bd08c5, table-count fix 5a47da16) rated M-1 and M-9 as **+**. Subsequent independent-reviewer-style reconsideration determined both should be **✓**: PP-684 itself already credits M-1 + for vector pressure-axes and M-9 + for Self-Other drift; legacy `conviction_track_v1` carries the moral-injury ontological inversion. PP-718 faithfully composes with all three upstream contributions but does not introduce new pattern instances on those axes. The genuine PP-718 extensions are M-3 (substrate-vectorization through crisis), M-4 (axis-specific institutional erosion), M-5 (cross-scale axis-specificity), M-6 (per-axis forced-choice + roll-5 history-grounding), and M-11 (per-axis voluntary cultivation). This recalibration tightens the rating without changing the pass/fail verdict (zero violations remain).

Per `throughlines_meta §8.2`: "М fail (single) → redesign OR documented tradeoff. М fail (multiple) → redesign required." Zero violations. **М verdict: pass.**

М-2 ○ is appropriate (proposal scope does not engage geography); not a fail.

---

## Τ — Throughlines

Per `throughlines_meta §8.1` Class B: "Which T's does this touch? For each: extend, preserve, or break? If break, is there deliberate supersession?"

| T | Title | Touch | Verdict |
|---|---|---|---|
| T-14 | Conviction Architecture | Direct — primary T | **Extends.** Forced-choice per-axis (vs aggregate) makes T-14's "Scar accumulation forces arc transitions" mechanic axis-specific. No supersession; extension within T-14's specification. |
| T-08 | Church Rendering Reinforcement | Indirect — via faction Cascade | **Extends.** Faith-axis erosion in Cardinals propagates to Church faction-vector specifically (where aggregate would have undifferentiated). Strengthens T-08's substrate-posture distinction. |
| T-09 | Varfell Thread Progressive | Indirect | **Preserves.** Varfell substrate-posture (Honor/Warden load-bearing per migration_roster) responds to axis-specific erosion appropriately. |
| T-11 | Crown Pragmatic | Indirect | **Preserves.** Crown's Authority/Utility load-bearing responds to axis-specific erosion appropriately. |
| T-15a/b/c | Hafenmark/Löwenritter/RM substrate-postures | Indirect | **Preserves.** Cultural-background templates per `conviction_taxonomy_v30 §5` (hafenmark_procedural, lowenritter_military, restoration_reformist) preserve faction-specific Conviction distributions; per-Conviction crisis acts on the named distributions. |
| T-22 | Belief Lattice | Direct — primary T | **Extends.** Cooperation-requires-Belief-revision now per-axis. Belief revision targets the *axis* the cooperation engages, not aggregate. |
| T-23 | NPC Arc Emergence | Direct | **Extends.** Personal arc → faction Domain Echo → political shift chain now carries which-axis specificity. |
| T-24 | Convergence as Crisis | Indirect | **Extends.** Multi-NPC Faith-crisis convergence is distinct from Authority-crisis convergence (vs aggregate which would have collapsed both). |
| T-25 | Generational Arc | Indirect | **Extends.** 30-year clock can record per-axis wound history across generations. |
| T-27 | Effects Real Explanation Wrong | Indirect — via cultural-background templates | **Preserves.** Faction interpretive-frames (Church doctrinal Faith, Hafenmark Categorical-Imperative procedural Order, etc.) consume their respective primary axes. |
| T-32 | Sincere Structural Closure | Indirect | **Preserves.** Frame-shift pathway operates on named axes; per-Conviction makes the frame-shift target specific. |
| T-39 | Textual Mode Typology | Indirect | **Preserves.** Four-mode faction-output typology consumes faction-aggregate Convictions which are now per-axis-erosion-aware. |

**Τ-breaks:** none. No supersession log needed.

**Τ verdict: pass.**

---

## Q — Quality

**Q-robust** (per `throughlines_meta §5`):

- **Three viable player approaches?** Yes:
  1. Avoid Faith-witnessing in territory-X for the Cardinal (axis-specific avoidance).
  2. Stack cultural-background-only events on the Cardinal (muted-drift only; no full crisis).
  3. Player Conviction Check via Spirit-pool resistance per ED-664 (Spirit pool TN 7 Ob 1 to deflect).
- **Visible, traceable world-state change?** Yes — the Scar count per Conviction is engine-readable; Resonant Style activation per crisis is visible to players via NPC behavior; faction-aggregate erosion propagates to Cascade Fidelity.
- **Mechanic fires without player action?** Yes — NPCs witnessing Thread operations during autonomous faction action accrue Scars; multi-NPC convergence on a Faith-crisis can fire across multiple NPCs in the same season without player presence.
- **Dramatic legibility:** Cardinal in Faith-crisis — *whose position is at risk* (the Cardinal's standing within Church + Church's faction-aggregate Faith), *what each named actor wants* (Cardinal: stabilize Faith; Inquisitor: prosecute Cardinal for doctrinal weakness; Pope-equivalent: protect institutional Faith), *what happens if no one acts next season* (Faith-axis crisis triggers arc transition per `complete_systems_reference §1.4`; Resonant Style fully exposed; faction Cascade Fidelity decrements on Faith axis). All readable in one sentence each.

**Q-smooth:**

- **Methodology matches governing subsystem.** Per-Conviction Scar accumulation uses the same data structures the Conviction taxonomy already uses (vector with named axes); same composition rule per `conviction_axis_matrix_v30 §5`.
- **Scale-transition behavior specified.** Per-Conviction tracking integrates with PP-686 §3.2 Cascade math (faction `effective_convictions` is aggregated from member-NPC `personal_convictions`; per-Conviction Scar shifts member weights, which propagates to faction aggregate).
- **Temporal behavior specified.** Season-cap from `conviction_track_v1 §3` ("Max 1 Scar per season from Thread witnessing per NPC") still applies; per-Conviction does not change the cap. Crisis activation persists for 1 season per `conviction_track_v1 §2` row 3+.

**Q-elegant:**

- **Core rule restatable after one reading?** "Scars accumulate per Conviction; crisis fires at 3+ Scars on any one Conviction. Cultural-background Scars produce muted drift instead of crisis." Yes.
- **Second-order consequence predictable?** Yes — multi-primary NPCs are more crisis-resistant (more axes to land on); single-primary NPCs are most fragile on their primary; cultural-background-only events accumulate slowly.
- **External dependencies enumerated?** PP-684 (taxonomy), PP-685 (migration roster), PP-686 (Cascade math), ED-663/664 (Thread-event triggers + Player Conviction Checks). All in the `conviction_track_v1.md §4 Cross-references` block.

**Q verdict: pass.**

---

## Final summary

| Tier | Result |
|---|---|
| N | pass |
| Ω (inherited from PP-684) | pass |
| Μ | pass — primary Μ-α + Μ-β; Μ-γ + Μ-δ preserved |
| М (M-1..M-11 walkthrough) | **5 + · 5 ✓ · 1 ○ · 0 −** — pass (recalibrated 2026-05-10 from prior 7+/3✓; M-1 and M-9 stepped down to ✓ to avoid double-counting PP-684's own M-1 + and M-9 +) |
| Τ | pass — extends T-14/T-22/T-23/T-24/T-25/T-08; preserves T-09/T-11/T-15a/b/c/T-27/T-32/T-39; no supersessions |
| Q | pass on robust/smooth/elegant |

**Overall: Class B vetting passes.** Walkthrough grounds the abbreviated rating block authored at PP-718 commit `239922c6`. No mechanical change to PP-718; the canonical mechanic stands as committed. This walkthrough replaces the earlier abbreviated rating note in the patch_register entry and lands in the doc as `designs/personal/conviction_track_v1_pp718_vetting.md` for reference.

**Revision history of this walkthrough:**
- 2026-05-10 commit `39bd08c5`: initial authoring with 7+/3✓/1○ count.
- 2026-05-10 commit `5a47da16`: m_summary off-by-one count fix (initial summary said "6 +" against 7 actually-rated).
- 2026-05-10 commit (this): M-1 and M-9 recalibrated from + to ✓ on independent-reviewer reconsideration to avoid double-counting PP-684's own M-1 + (vector pressure-axes) and M-9 + (Self-Other drift) and legacy v1's moral-injury ontological inversion. PP-718 faithfully composes with these upstream contributions; the vetting framework's ✓ rating ("consistent with the pattern") is more accurate than + ("new instantiation") for what PP-718 actually does at M-1 and M-9. Final count: **5 + · 5 ✓ · 1 ○ · 0 −**. Pass/fail verdict unchanged (zero violations).
