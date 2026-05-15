# Methodology Audit — Bottom-up Design / Top-down Verification

**Scope:** Audit of the design methodology proposed for the Valoria game-design application of the formations research. The methodology specifies that Valoria game-mechanics are designed bottom-up from primitives (Level 0 soldier → Level 1 unit → Level 2 formation → Level 3 army → Level 4 battle) and verified top-down by reproducing historical patterns from a verification suite of canonical battles.

**Audit type:** Self-review of methodology proposal from the prior conversational turn.

`[SELF-AUTHORED — bias risk]` Per the PI's self-review-bias rule: this audit is performed by the same author who proposed the methodology. An independent reviewer would likely emphasize: (a) the methodology assumes multi-objective calibration of primitives is tractable, which is itself an engineering bet; (b) the verification suite of 6 battles is finite, and a primitive set that passes 6 tests can fail the 7th — the methodology has no theory of how many battles is "enough"; (c) the methodology privileges historical realism as the calibration target, but a game might want to deliberately diverge from historical realism in service of gameplay (the methodology has no mechanism for "calibrated divergence"). These limitations are stated up front rather than only in closing.

**Companion files:** This audit references and extends file 9 (throughlines + matchup matrix), file 11 (NERS audit of throughlines), file 12 (moment-by-moment dynamic spacing), and file 13 (verification corrections). New tags introduced here continue established sequences: T-30 onwards extends file 9's throughlines (which ran through T-29). M-9 onwards extends file 9's meta-throughlines (which ran through M-8). G-1 onwards is a new tag class for gameplay opportunities.

---

## Part I — All-directions audit of the methodology

Per the PI canon, "all directions" = top-down, bottom-up, vertical, diagonal, lateral, horizontal. The methodology is itself a designed object subject to the same discipline it imposes on the game.

### Top-down — does the methodology preserve grand-pattern correctness?

**Strong.** The verification suite checks at battle-level. Six tests cover six distinct doctrinal patterns (Cannae double-envelopment, Pharsalus reserve-ambush, Agincourt funnel, Panipat tulughma + firepower, Hastings slope rotation, Marignano interruption). Methodology is explicitly accountable to historical macro-outcomes — a primitive set that passes all six is presumptively well-calibrated; one that fails any is presumptively miscalibrated.

**No correction needed.**

### Bottom-up — does the methodology start from primitives?

**Strong.** Design stack L0→L4 is explicit. Each level owns specific primitives. No level reaches down to overwrite a lower level's behavior — higher levels only compose lower-level behavior. The principle "primitives compose up; patterns are checked down" is the operational summary.

**No correction needed.**

### Vertical — command hierarchy across levels

**Partial.** Command authority is mentioned at L2/L3 ("commander span of control") but not specified as a first-class primitive. The methodology doesn't address: (a) when does an order require a commander-level decision vs. a unit-level response? (b) what is the latency between commander order and unit execution? (c) how does command-failure propagate (the Lodi-at-Panipat case where army-level command collapse cascades to unit incoherence)?

**Refinement opportunity:** Command authority as a Level-2.5 primitive (between formation cluster and army), with explicit latency and propagation rules. Not a methodology error; an unfinished specification.

### Diagonal — cross-cutting structural patterns

**Strong.** The doctrine-substrate-opponent triangle from M-1 (file 9) receives executable form. Each historical battle is a different triangle:
- Cannae: Roman institutional substrate + manipular doctrine + Carthaginian combined-arms opponent
- Agincourt: English yeoman-archery institution + dismounted-heavy doctrine + French chivalric opponent
- Panipat: Babur's Timurid-Mongol substrate + cross-cultural firearm-cart doctrine + Indian elephant-cavalry opponent

The verification suite tests across triangles, validating that the methodology is general enough to instantiate any plausible triangle from the same primitive set.

**No correction needed.**

### Lateral — peer-to-peer at same scale

**Partial.** The six battle tests are all at battle-level but the methodology doesn't structure cross-comparison. A diagnostic question: when Cannae reproduces but Pharsalus doesn't, is there a shared primitive failure or different failures? The methodology doesn't say.

**Refinement opportunity:** Add "shared-primitive cross-test analysis" to the calibration loop. When multiple tests fail, look for the primitive shared by the failing tests but not by the passing ones.

### Horizontal — at-level within an era-tier

**Implicit.** Era-tier tests are present (Crécy + Agincourt at longbow tier; Marignano + Pavia at pike-and-shot tier) but not formally clustered. Cross-cluster generalization (does a primitive that works at longbow tier also work at pike-and-shot tier?) is not addressed.

**Refinement opportunity:** Surface era-tier clusters as a formal layer of the verification suite. Run tier-tests alongside battle-tests.

### Audit verdict

| Direction | Coverage | Status | Recommended action |
|---|---|---|---|
| Top-down | Battle-level verification suite | ✓ Strong | None |
| Bottom-up | L0→L4 design stack | ✓ Strong | None |
| Vertical | Command authority mentioned | ~ Partial | Specify command-latency primitive at L2.5 |
| Diagonal | Doctrine-substrate-opponent in tests | ✓ Strong | None |
| Lateral | Cross-test diagnosis | ~ Implicit | Add shared-primitive cross-test analysis |
| Horizontal | Era-tier clusters | ~ Implicit | Formalize tier-tests in verification suite |

**The methodology is fundamentally sound. Three refinements are surfaceable but not critical.**

---

## Part II — Throughlines extracted (T-30 through T-43)

Continuing the file-9 sequence. These are patterns the methodology itself instantiates or relies on.

- **T-30 — Primitives must be specified before composition.** Top-down macro-recognition rules corrupt the system. The "Cannae button" anti-pattern is the canonical failure mode.

- **T-31 — Verification suite as regression net.** Once historical patterns reproduce, any future change must preserve them. Tests are forever.

- **T-32 — Step-change non-linearities are first-class primitives.** Lethal density at ~12 m²/man is the canonical example; linear casualty math cannot produce Cannae, Adrianople, Agincourt, or Panipat. The non-linearity itself is the primitive, not a derived quantity.

- **T-33 — Facing dependence is a first-class primitive.** Frontal / flank / rear arcs are not equivalent. Pocket dynamics, fourth-line ambushes, cavalry-flank shock all require facing as a primitive distinct from position.

- **T-34 — Cohesion → rout → pursuit is the kill pipeline.** Most historical battle deaths happen post-cohesion-collapse, not in formed combat. Linear attrition systems get this wrong. The pipeline is: combat attrition → cohesion threshold crossed → unit shaken → rout → pursuit casualties.

- **T-35 — Sub-tile vector positions preserve dynamic-spacing fidelity.** Discrete whole-tile occupation discards the granularity the research depends on. A unit at "tile (5,3) position 0.2" vs. "tile (5,3) position 0.8" is meaningfully different for engagement-distance calculations.

- **T-36 — The decisive-commit window is where player skill lives.** A 1–6 turn micro-sequence inside a 36–72 turn battle. Turn granularity must be fine enough to support this. With 5-minute turns and ~36–72 turns per battle, the decisive window is mechanically expressible.

- **T-37 — Terrain-formation interaction is lossy.** Dense terrain forces compact units into open order with combat consequences. Cavalry can charge open ground but not woods (Pavia 1525). Without lossy terrain-formation interaction, Pavia and Agincourt-flank-stakes cannot reproduce.

- **T-38 — Reserves are a first-class system with commit-timing as a separate primitive.** "Held / committed" is a unit state, not an emergent property. Edward III's "let the Prince win his spurs" decision at Crécy is the design exemplar.

- **T-39 — Achievability check + counter-play check is the two-phase verification structure.** Phase 1: the system makes the historical pattern executable. Phase 2: the historical loser had options they didn't take (design quality).

- **T-40 — Failures trace down, not sideways.** A failing verification test points to a primitive miscalibration, not a need for new mid-level logic. The temptation to add a special-case rule when a test fails is the methodology's primary failure mode.

- **T-41 — Implementation order matches design stack.** L0 first, L4 last. Out-of-order builds reach correct outcomes by accident and break unpredictably. This implies a long pre-battle development period before the first verifiable battle test can run.

- **T-42 — Soldier-abstraction granularity is a free parameter.** "Soldier" can equal 1, 10, or 50 historical men. What matters is that L0 is a stable boundary, not the specific aggregation. Granularity choice is performance-vs-fidelity, not design-vs-design.

- **T-43 — Order-of-magnitude calibration sets all derivative scales.** Tile size and turn duration cascade through movement speeds, missile ranges, lethal-density math, decisive-commit window. Get these two wrong, everything downstream miscalibrates. The 5-min / 50-m proposal is one defensible point in this two-parameter space; others exist.

**Tally: 14 new throughlines, T-30 through T-43.**

---

## Part III — Meta-throughlines (M-9 through M-13)

Continuing the file-9 meta-throughline sequence.

- **M-9 — Top-down recognition would corrupt the design.** Detecting "this is a Cannae situation" via pattern-match and applying special bonuses is the methodology's primary anti-pattern. Compositional purity is the discipline. This is the negative-space of M-1 (doctrine-substrate-opponent triangle): the triangle's parameters compose; the recognition that a particular triangle is "Cannae" must not be a system input.

- **M-10 — Historical battles are calibration data, not scripted scenarios.** They serve as tests of the primitive set. Their authority is empirical, not narrative. The implication: scenarios where the player "is" Hannibal at Cannae are not scenarios where the system recognizes a Cannae-shaped situation; they are scenarios with starting conditions matched to the historical record, where the player's choices may or may not produce the historical outcome.

- **M-11 — The methodology generalizes beyond combat.** Bottom-up design + top-down verification applies to economy systems, character progression, AI behavior, narrative systems. Wherever a complex emergent system needs to map to a known target (historical, theoretical, or genre-conventional), this methodology applies. The combat instance is one application of a general design discipline.

- **M-12 — Player choice and historical outcome are deliberately decoupled.** Varro must have had options Varro didn't take. The system that locks Varro into Cannae is railroading, not history. This is the design-quality assertion that history is contingent, not deterministic, and the system should reflect that contingency.

- **M-13 — The verification suite is necessarily incomplete.** Tests cover specific battles; a primitive set passing all current tests can fail on the next. The methodology requires acknowledging this as inherent and treating each new historical scenario as a potential calibration update, not a fixed solution. The implication: methodology is open-ended, not closed-form. There will always be a battle that surprises the system.

**Tally: 5 new meta-throughlines, M-9 through M-13.**

---

## Part IV — Gameplay opportunities (G-1 through G-13)

New tag class. These are *discoverable* player plays the methodology unlocks — emergent from primitives, not authored as special-case scripts.

### Named historical plays (achievable by player composition)

- **G-1 — The Cannae play.** Convex deploy + refused wings + reserve cavalry → discoverable encirclement. Requires: convex grand-formation primitive; refused-wing state; reserve commit-timing; lethal-density non-linearity.
- **G-2 — The Pharsalus trick.** Hidden oblique reserve + commit-timing ambush against cavalry. Requires: oblique echelon grand-formation; reserve-commit timing; cavalry-stop-by-thrust-spears micro-mechanic.
- **G-3 — The Agincourt funnel.** Narrow terrain + obstacles + missile wings + dismounted heavy line. Requires: terrain-on-formation interaction; obstacle/stakes blocking cavalry; longbow range bands; mud-on-speed modifier.
- **G-4 — The Panipat tulughma.** Anchored center + long-arc flanking cavalry + concentrated firepower. Requires: wagon-anchored line; long independent cavalry vectors; point-blank firearm shock effect; shock-arm panic on cohesion collapse.
- **G-5 — The Marignano interruption.** Artillery + arquebus interrupt pike-block shock arm. Requires: artillery at standoff range; arquebus point-blank stopping power; pike-cohesion-collapse-under-fire.
- **G-6 — The Hastings rotation.** Slope + cycled archery/cavalry/infantry attrition. Requires: slope-on-cavalry-charge speed/cohesion modifier; cycle-fight micro-doctrine (engage / withdraw / re-engage by arm); feigned-retreat / pursuit counter-charge mechanic.

### Counter-plays (the historical losers' options they didn't take)

- **G-7 — Counter-Cannae.** Refused-center defense; let the wings absorb while center holds — the Varro counterplay he didn't take. Requires: center-refuse grand-formation symmetric to wing-refuse; cohesion-under-sustained-pressure mechanic allowing center to absorb without collapsing.
- **G-8 — Counter-Panipat.** Disperse the shock arm pre-charge; flank the wagon-line before frontal commit — the Lodi counterplay he didn't take. Requires: dispersed-advance grand-formation; ability to commit different arms independently; cavalry-flank-on-fortified-line mechanic.
- **G-9 — Counter-Agincourt.** Refuse to advance; force the English to attack uphill into the funnel. The French counterplay they didn't take. Requires: positional-stalemate as a viable state; supply/fatigue mechanic to force the besieger to attack eventually.

### Strategic-layer opportunities

- **G-10 — Doctrine selection as a strategic-layer commit.** Pre-battle, a faction picks an army doctrine (combined-arms / shock-cavalry / pike-block / longbow-and-stake / firearm-line), constraining tactical options. The strategic-layer "what doctrine is my faction" is upstream of the tactical battle.
- **G-11 — Doctrinal-manual economy.** Strategic-layer faction can acquire / develop / lose military manuals encoding their doctrine, mapping to historical reality of training pipelines and institutional knowledge. (Already flagged in file 12 §VI as O-6.)
- **G-12 — Asymmetric verification scenarios as PvE content.** Each verification battle is a playable scenario. Player takes the historical loser's army and seeks the counterplay (G-7/8/9 above). Engaging because the historical outcome is canonically known; deviation from it requires player skill.

### Meta-gameplay

- **G-13 — Narrative emergence.** Replays of player matches generate "battle accounts" — naming conventions for emergent patterns ("the Tuesday Cannae"). Maps to the chronicle-author asymmetry in file 12: history is remembered through its tellers.

**Tally: 13 gameplay opportunities, G-1 through G-13.**

---

## Part V — NERS audit

Per Valoria canon (PI `<canon_terms>` definitions of necessary / robust / smooth / elegant).

### N(ecessary) — methodology cannot be removed without worsening

| Tag | Item | Status |
|---|---|---|
| N-01 | Bottom-up discipline (alternative: top-down authoring → brittle systems) | ✓ |
| N-02 | Verification suite (alternative: drift over development) | ✓ |
| N-03 | Lethal-density non-linearity (alternative: Cannae/Adrianople cannot reproduce) | ✓ |
| N-04 | Facing dependence (alternative: pocket dynamics, fourth-line ambush impossible) | ✓ |
| N-05 | Sub-tile vector positions (alternative: discrete tiles discard dynamic-spacing fidelity) | ✓ |
| N-06 | 5-min / 50-m calibration (alternative: decisive-commit window collapses or over-resolves) | ✓ (T-43 acknowledges other points in two-param space exist) |

**N findings:** No necessity gaps. All proposed primitives are load-bearing.

### R(obust) — methodology supports strategic depth, customization, variety, emergence

| Tag | Item | Status |
|---|---|---|
| R-01 | Doctrine selection (G-10) — strategic-layer customization | ✓ |
| R-02 | Counter-play space (T-39 phase 2 + G-7/8/9) | ✓ in principle |
| R-03 | Emergent narratives (G-13) — from compositional primitives | ✓ |
| R-04 | Player important to game world — decisive-commit window depends on player skill | ✓ |
| R-05 | Game world emergent without player — clean formations vs. each other still produce battles | ✓ |
| R-06 | Counter-play space *design* — just because options exist doesn't mean they're discoverable | **P2 — design gap** |

### S(mooth) — methodology integrates cleanly with other interdependent mechanics

| Tag | Item | Status |
|---|---|---|
| S-01 | Two-layer formation (grand + unit) integrates cleanly | ✓ |
| S-02 | Vector movement + tile grid integrate via sub-tile positions (T-35) | ✓ |
| S-03 | Simultaneous resolution + commit timing — reveal window design unspecified | **P3 — clarification needed** |
| S-04 | Scale-zoom transitions (personal ↔ settlement ↔ territory ↔ peninsula) — methodology is battle-level only | **P2 — scope limitation** |
| S-05 | Calculation methodology consistency — density math, cohesion math, terrain modifiers all multiplicative | ✓ |

### E(legant) — methodology is logically simple, clear, no unnecessary overhead

| Tag | Item | Status |
|---|---|---|
| E-01 | One-sentence principle ("primitives compose up; patterns are checked down") | ✓ |
| E-02 | Mechanics are derived, not authored | ✓ |
| E-03 | Player can understand "I'm in the killing pocket" without knowing the non-linearity is firing | ✓ |
| E-04 | Sub-tile precision creates visualization complexity | **P2 — design tension** |
| E-05 | Multi-objective calibration tuning is non-trivial; first attempt may not converge | **P2 — engineering risk** |

### NERS findings summary

| Tag | Severity | Item |
|---|---|---|
| R-06 | P2 | Counter-play space not systematically designed; just because options exist doesn't mean they're discoverable. Recommend explicit counter-play-discovery design pass. |
| S-03 | P3 | Reveal window design not specified for simultaneous resolution. Recommend: short post-turn reveal of opponent's executed orders before next-turn commit. |
| S-04 | P2 | Methodology scope is battle-level only; operational / strategic / campaign scales need their own discipline. Acknowledge as scope limitation. |
| E-04 | P2 | Sub-tile precision creates visualization complexity. Recommend: aggregation layer between simulation precision and display legibility. |
| E-05 | P2 | Multi-objective calibration tuning is non-trivial. Recommend: incremental calibration starting with smallest verification suite (one battle), expanding only after stable. |

**Tally: 5 findings — 0 P1, 4 P2, 1 P3.**

The methodology is sound at the principle level. Findings concern implementation complexity, scope completeness, and design-pass gaps — not methodology errors.

---

## Part VI — Limitations stated up front

`[SELF-AUTHORED — bias risk]` Per layering rule. These would be raised by an independent reviewer:

1. **Multi-objective calibration tractability is an engineering bet.** The methodology assumes that primitive parameters (lethal-density curve shape, terrain multipliers, cohesion thresholds, missile range bands) can be tuned to make all six verification tests pass simultaneously. This is a multi-objective optimization that may not converge on first attempt. The methodology has no fallback if calibration is intractable.

2. **The verification suite is necessarily incomplete (M-13 acknowledges this but doesn't solve it).** Tests cover specific battles; a primitive set passing all current tests can fail on the next. There is no theoretical answer to "how many battles is enough."

3. **Historical realism as calibration target is a design choice, not a universal good.** A game might want to deliberately diverge from historical realism for gameplay reasons (e.g., balance, accessibility, distinct fantasy faction identities). The methodology has no mechanism for "calibrated divergence" — for saying "we want this to differ from historical realism by X% in direction Y."

4. **Self-review of methodology by methodology's author has obvious limitations.** A truly independent audit by someone who didn't propose the methodology would find issues I have psychological investment in not finding. Tag is flagged but the limitation is real.

5. **The methodology privileges Western European battles in verification.** Six tests: 5 European, 1 South Asian (Panipat). No Chinese, no Mesoamerican, no East African, no medieval Islamic engagement above the Mamluk-furusiyya level. The historical-pattern coverage is biased toward where surviving sources are richest, which is also where the prior research files (1–12) emphasized.

6. **The methodology is silent on AI play.** Verification tests assume human players executing patterns. AI opponents that play these patterns at varied skill levels are a separate design problem. A primitive set that allows human-discovered Cannae might not be a primitive set that an AI can play Cannae against, or that a Cannae-playing AI can be defeated by.

7. **Implementation cost is not addressed.** Sub-tile vector positions + facing dependence + cohesion + lethal-density non-linearity + terrain-formation interaction + reserve-commit timing × per-unit basis × 6 verification battles for regression testing is a substantial engineering scope. The methodology doesn't estimate development effort.

---

## Part VII — Recommendations

`[CONFIDENCE: high]` on the audit findings; `[CONFIDENCE: medium]` on which findings are most urgent.

### For immediate action

- **Resolve R-06 (counter-play space design)** before committing to the methodology. The asymmetric-scenario PvE design (G-12) depends on counter-plays being discoverable, not just theoretically present. Spend a design pass on this.

- **Acknowledge S-04 (scope limitation)** explicitly in any methodology documentation. The battle-level methodology does not extend automatically to operational, strategic, or campaign scales — those need their own discipline. Tag this clearly.

### For development planning

- **Address E-05 (calibration tractability)** by starting with the smallest possible verification suite (one battle, e.g., Cannae) and expanding only after stable. If you can't make a single-battle test pass, six-battle simultaneous calibration is hopeless.

- **Implement T-41 (implementation order matches design stack)** as a project plan constraint. L0 mechanics must be complete and verified before L1 work begins. Skipping levels is the project-management failure mode the methodology warns against in the design dimension.

### For documentation

- Surface the throughlines T-30 through T-43 and meta-throughlines M-9 through M-13 into the canonical throughlines registry if Jordan accepts them as canonical. Otherwise tag as `[PROPOSED]` until reviewed.
- The gameplay-opportunity tag class (G-1 through G-13) is a new tag dimension. Decide whether to integrate it with existing tag taxonomy or keep separate.

### For verification

- Run a "methodology dry-run" on a simpler reference game (e.g., a tactical-only abstraction without strategic layer) before committing the full Valoria design to the methodology. The dry-run de-risks calibration tractability (E-05) at lower stakes.

---

## Closing log

`[CONFIDENCE: high on the structural soundness of the methodology; medium on calibration tractability in practice; low on coverage of non-Western battles in the verification suite as currently scoped.]`

`[ASSUMPTION: throughline / meta-throughline / gameplay-opportunity tagging conventions extend the file-9 sequence in the same style — basis: file 9 established the T-/M- numbering and file 11 audited those; this audit follows the same conventions for the new tags. If Jordan wants different conventions for methodology-tier tags (e.g., a separate namespace like MT- for methodology-throughlines), the tag prefixes can be revised.]`

`[GAP: methodology-level testing (i.e., a methodology that is itself audited by a meta-methodology) is not addressed here. The self-review-bias flag is the only methodology-level epistemics. A more rigorous treatment would specify a process for periodic re-audit of the methodology by independent reviewers. Recommended as a future addition if Jordan wants the methodology to remain self-correcting over the project's lifetime.]`

`[SELF-AUTHORED — bias risk]` Final flag, restated per the PI's self-review-bias instruction: this entire audit is the methodology's author auditing the methodology. An independent reviewer with no investment in the prior turn's proposal might prioritize the findings differently, might find issues I psychologically avoided, and might disagree with my own judgment of which findings are P1 vs. P2 vs. P3. The audit is rigorous within the bounds of self-review, which is the bound being explicitly flagged.

---

## Tag tally

| Tag class | Range introduced | Count |
|---|---|---|
| Throughlines (T-) | T-30 to T-43 | 14 |
| Meta-throughlines (M-) | M-9 to M-13 | 5 |
| Gameplay opportunities (G-) | G-1 to G-13 | 13 |
| NERS findings | R-06, S-03, S-04, E-04, E-05 | 5 (0 P1, 4 P2, 1 P3) |
| Self-bias limitations | 7 numbered | 7 |
| Recommendations | 4 grouped | 4 groups |

**Total methodology-level tags introduced: 44.**
