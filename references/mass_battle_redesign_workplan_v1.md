# Mass Battle Redesign Workplan v1.1
## Implementation plan for ED-811..820 + propagation of ED-800..808

**Date:** 2026-05-11
**Status:** Ratified. Phase 1 execution begins this session.
**Companion:** `references/simulation_workplan_v1.md` (parent), `tests/coverage_matrix.md`, `tests/sim/sim_mass_battle_SIM-MB-04.md`
**Scope:** Mass battle system overhaul — compositional grid, shape templates, Discipline redesign, degree-gated damage. Specific subproject within the broader simulation campaign.
**Surface:** Valoria is a videogame (Godot 4.6) only. All mechanics target the videogame execution layer.

---

## §0 — GOAL AND CONTEXT

### §0.1 The problem this solves

SIM-MB-04 surfaced three structural issues in mass battle:

1. **Engagement lethality** — INTERPRETATION-01 (margin × (1+Power)) produces one-turn kills. The system needs a bounded damage model (ED-811).
2. **Volley over-amplification** — ED-800's pool fix combined with the unmodified `1+Power` multiplier doubles ranged output (ED-812).
3. **Pure-type unit immersion break** — a unit composed entirely of archers is a phase-system artifact, not a faithful representation of a medieval military formation (ED-814).

The redesign also corrects a long-standing definitional weakness: Discipline as "organizational integrity" was a proxy for what doctrine actually describes — **formation coherence under fire** (ED-815).

### §0.2 What this workplan delivers

- 10 new EDs written and committed to `canon/editorial_ledger.yaml` (ED-811..820)
- Propagation of all closed EDs (800..810) to canonical design docs
- New mass battle subsystem: compositional grid + shape templates + unit parameters
- Refactored simulation infrastructure (SIM-MB-05) supporting the new system
- Three sim cycles validating the redesign (isolation, interaction, full scenarios)
- Coverage matrix update reflecting redesigned mass battle layer

### §0.3 What this workplan does NOT touch

- A3 SCHISM, A4 PROVINCIAL CRISIS, and other archetype sims remain on parent workplan
- Personal-scale combat (`designs/scene/combat_v30.md`) not affected
- Social contest, threadwork, scale transitions — separate systems
- Strategic layer mostly unchanged; composition feeds in as a new unit attribute

---

## §1 — DESIGN DECISIONS CONFIRMED

Captured from session 2026-05-11 design discussion. These are Jordan-ratified directions ready to canonize.

| ID | Decision |
|---|---|
| ED-811 | Engagement uses **degree-gated damage**: Overwhelming = 1+Power, Success = Power, Partial = 1, Failure = counter (mechanism TBD per §2 open items). Defender's defense pool sets effective Ob. |
| ED-812 | Volley damage = **net successes minus ranged DR**. No (1+Power) multiplier. Composition (ED-814) handles scaling via `back_pct` × volley pool. |
| ED-814 | Unit has a **compositional grid**: 3 rows (front/mid/back) × 3 columns (left/center/right). Player sets base composition (melee%/ranged%/support%) + shape template; system auto-distributes troops across cells. Manual cell overrides available. Football Manager pattern: defaults are sane, depth is optional. |
| ED-815 | Discipline redefined as **formation coherence under fire**. Determines whether a unit executes its designed shape and standing orders under pressure. Existing penalty table and H formula remain valid under new framing. |
| ED-816 | **Unit shapes** are formation templates: Arrowhead, Horseshoe, Gapped Line, Refused Flank, Line. Each has a precise mechanical signature: minimum Discipline to hold, Phase 5 effects, failure mode, designed exploit. |
| ED-818 | **Discrete column model**: each column (left/center/right) is an independent sub-pool. Max 3 simultaneous engagements maps to 3 columns. Pincer attacks resolve as column-on-column engagements. |
| ED-819 | **Unit parameters (standing orders)**: per-unit settings — Aggression, Cohesion priority, Pursuit, Reserve discipline, Targeting. Set at army-build (defaults), adjustable at battle-setup. Discipline gates execution. |
| ED-820 | **Shape locking**: shape set at battle setup, not mid-battle. Mid-battle reshape is an emergency mechanic — Command check Ob 3; failure = unit fights confused for that turn (−2D all pools). |

---

## §2 — RATIFIED RESOLUTIONS (2026-05-11)

All design questions resolved via historical precedent + acclaimed game design + NERS audit. Resolutions integrated into corresponding phase deliverables.

### §2.1 ED-811 Failure counter — RESOLVED: degree-gated symmetric

Both attacker and defender always roll their pools. Apply degree table to BOTH rolls:
- Attacker's degree(att_net, max(1, def_net)) determines attacker→defender damage
- Defender's degree(def_net, max(1, att_net)) determines defender→attacker counter damage

Damage by degree (both directions):
| Degree | Damage to opponent |
|---|---|
| Overwhelming | 1 + Power |
| Success | Power |
| Partial | 1 |
| Failure | 0 |

**Precedent:** Civilization VI (always reciprocal), Total War (continuous mutual casualties), Field of Glory tabletop (margin-based mutual cohesion damage), Vegetius/Maurice (successful defense was never passive — shield walls counter-thrust). Cap stays at `1 + Power` per side per exchange. Passive defense (defender Failure) → no counter; active defense (defender Partial or better) → real counter damage.

**NERS:** N (defensive investment must pay) / E (one mechanic both ways) / R (every roll matters) / S (symmetric application).

### §2.2 ED-813 Withdrawal — RESOLVED: Phase 1 declaration

Withdrawing unit declares Withdraw plan at Phase 1. In Phase 3 manoeuvre, pursuer cannot close if Speed differential favors withdrawer. Engagement is prevented at the positioning layer, not the combat layer.

**Precedent:** Total War (withdraw is movement-phase action), Field of Glory (voluntary withdrawal tests during movement, not melee), CK3 (retreat is strategic decision before combat), Vegetius/Maurice (orderly withdrawal is a maneuver, not a combat exchange).

**NERS:** N (precise) / E (clean) / R (Speed investment matters) / S (integrates with manoeuvre).

### §2.3 Shape mechanical signatures — RESOLVED with Discipline adjustments

| Shape | Min Disc | Min Cmd | Phase 5 effect | Drift target | Designed exploit |
|---|---|---|---|---|---|
| Line | 1 | 1 | No modifiers | mob | Universal default |
| Arrowhead | **4** | 2 | Center column +2D Off; flanks −1D Off | Line | Center breakthrough |
| Horseshoe | **5** | 3 | Center −2D Off, +1D Def; flanks +1D Off when enemy in center | Line | Encircle aggressive enemy |
| Gapped Line | 5 | 3 | Selected column 0 troops; enemy in gap is flanked next Phase 5 | Line | Channel enemy into kill zone |
| Refused Flank | 3 | 2 | One flank column −2D Off; other columns normal | Line | Asymmetric — fight on chosen flank |

Discipline minimums raised for Arrowhead (3→4) and Horseshoe (4→5) per historical precedent: Macedonian wedge required veterans; Cannae crescent required exceptional discipline in both bowing center and waiting wings.

**Precedent:** Macedonian wedge (Alexander), Cannae (Hannibal 216 BC), Mons Graupius (Roman kill-zone), Leuctra (Epaminondas 371 BC refused right).

### §2.4 Shape failure cascade — RESOLVED: shape-specific drift to Line

Each shape drifts directly to Line under Discipline failure. **No linear chain** — Cannae's crescent doesn't degrade through wedge stages; it collapses toward Line as soldiers abandon assigned roles. Drift is **irreversible within the battle** (per Strategikon). Reform Phase may restore Discipline but cannot restore the original shape.

| Shape | Drifts to |
|---|---|
| Gapped Line | Line |
| Horseshoe | Line |
| Arrowhead | Line |
| Refused Flank | Line |
| Line | mob (no further tier) |

**Precedent:** Field of Glory cohesion tiers, Combat Mission squad states, Vegetius/Maurice/Strategikon "stages of disorder" with irreversibility.

### §2.5 Combined attack × column — RESOLVED: single column concentration

ED-805 Fibonacci combined attack hits one defender column. Lead designates target; supporters' Fibonacci-summed contribution adds to lead's pool against that one column. Other defender columns remain active for subsequent exchanges. Players wanting to attack multiple columns run separate non-combined engagements.

**Precedent:** Cannae (every Carthaginian unit attacked the same compressed Roman mass), Total War (concentration multiplies; distribution divides), CK3 tactics (concentration tactics target one regiment).

**NERS:** N (preserves ED-805 intent) / E (clean) / R (concentrated assault retained as strategic option) / S (no extra rules).

### §2.6 Composition granularity — RESOLVED: faction templates + per-unit override

Faction-level composition defaults auto-populate to recruited units (e.g., "Crown Heavy Infantry: 85% melee / 15% crossbow / 0% support"). Per-unit override available at army-management screen (set once, persists) and at battle-setup screen (per-battle adjustment). Football Manager pattern: engaged players customize; casual players use defaults.

**Precedent:** Symphony of War (per-squad), Total War (faction templates), CK3 men-at-arms (faction templates), Football Manager (both layers).

**NERS:** N (yes) / E (FM-pattern well-tested) / R (max depth without forced authoring) / S (smooth).

---

## §3 — PHASE SEQUENCING

10 phases. Each phase is approximately one session. Dependencies are strict — later phases require earlier phases complete.

```
Phase 1 ──→ Phase 2 ──→ Phase 3 ──→ Phase 4 ──→ Phase 5 ──→ Phase 6
                                                                ↓
                                                    Phase 7 ─┘
                                                       ↓
                                                    Phase 8 ─→ Phase 9 ─→ Phase 10
```

| # | Phase | Deliverable | Bootstrap scope | Open-items dep |
|---|---|---|---|---|
| 1 | Foundation EDs | ED-815 Discipline, ED-812 Volley written + committed | propose_mechanic | None |
| 2 | Shape spec | ED-816 shape signatures, ED-817 cascade written | propose_mechanic | §2.3, §2.4 |
| 3 | Battle resolution EDs | ED-811 engagement, ED-818 combined-column, ED-820 shape-locking | propose_mechanic | §2.1, §2.5 |
| 4 | Composition + params EDs | ED-814 grid + templates, ED-819 unit parameters, ED-813 withdrawal phase | propose_mechanic | §2.2, §2.6 |
| 5 | Propagation: ED-800..810 | Updates to mass_battle_v30.md, params/mass_combat.md, params/bg/core.md | editorial | Phase 1-4 complete |
| 6 | Propagation: ED-811..820 | Major rewrite of mass_battle_v30.md §A.4-A.7 | editorial | Phase 5 complete |
| 7 | Sim refactor (SIM-MB-05) | New sim engine with composition grid, shapes, parameters | simulation | Phase 6 complete |
| 8 | Sim Cycle 1 — isolation | Module tests for each new mechanic | simulation | Phase 7 complete |
| 9 | Sim Cycle 2 — interaction | Shape-vs-shape, composition-vs-composition matchups | simulation | Phase 8 complete |
| 10 | Sim Cycle 3 — full scenarios | Multi-turn battles with composition + parameters; coverage matrix update | simulation | Phase 9 complete |

---

## §4 — PHASE 1: FOUNDATION EDs

**Session 1 scope.** Two clean EDs with no design dependencies.

### §4.1 ED-815 Discipline redesign

Rewrite mass_battle_v30.md §A.4 Discipline subsection. New text:

> **Discipline (1–7)** — formation coherence under fire. The unit's capacity to maintain its designed shape, hold its assigned position, and execute standing orders while taking casualties. Distinct from Command (the general's tactical authority) and Power (raw combat capability).
>
> Discipline degrades under pressure: when [trigger conditions], the unit loses one tier and may collapse toward a simpler formation. A high-Discipline unit holds the horseshoe even as the center bleeds. A low-Discipline unit reverts to local survival behavior — fighting whoever is in front, abandoning flank positions, ignoring orders to refuse a side.
>
> The Discipline penalty table represents this drift: a unit at Discipline 3-4 is fighting at −1D because its designed shape no longer holds; the unit is engaging less effectively than its Power suggests. At Discipline 1-2, the shape has substantially collapsed (−2D). At Discipline 0, the unit is formation-broken and cannot attack.

ED format:

```yaml
- id: ED-815
  date: 2026-05-11
  description: "Discipline redefined as formation coherence under fire — capacity to maintain designed shape, hold assigned position, execute standing orders while taking casualties. Replaces vague 'organizational integrity' framing. Penalty table interpretation: pool penalty represents shape drift, not generic disorder. Aligns with historical doctrine (Vegetius, Maurice, Leo VI). Triangulates with Command (tactical authority) and Power (combat capability) for clean three-stat unit quality model."
  severity: P1
  type: clarification
  archetype: A2
  affected_docs:
    - designs/provincial/mass_battle_v30.md
    - params/mass_combat.md
  status: closed
  closure_commit: pending-this-session
  jordan_decision: "2026-05-11 — Discipline = formation coherence under fire. Sharpens stat distinction."
```

### §4.2 ED-812 Volley damage = net successes

```yaml
- id: ED-812
  date: 2026-05-11
  description: "Volley damage = max(0, net_successes) − ranged DR. Removes (1+Power) multiplier that caused double-amplification with ED-800 pool fix. Composition (ED-814) handles scaling — back_pct × volley pool sets dice count; net successes set damage. Volley is attrition contributor; Engagement is decisive."
  severity: P1
  type: correction
  archetype: A2
  affected_docs:
    - designs/provincial/mass_battle_v30.md
    - params/mass_combat.md
  status: closed
  closure_commit: pending-this-session
  jordan_decision: "2026-05-11 — Volley = net successes only, no Power multiplier."
```

**Phase 1 exit criteria:** Both EDs committed to `canon/editorial_ledger.yaml`. No canonical propagation yet (that's Phase 5).

---

## §5 — PHASE 2: SHAPE SPEC

**Session 2 scope.** ED-816 (shape mechanical signatures) and ED-817 (failure cascade). Requires §2.3 and §2.4 ratified.

Each shape gets a dedicated subsection in mass_battle_v30.md §A.6 (formerly Formation Types, now Shape Templates).

Shape entry format (template):

```markdown
### Shape: Horseshoe

**Tactical concept:** Hannibal at Cannae. Thin center, strong flanks, designed to absorb a frontal advance and close from the sides.

**Requirements:** Discipline ≥ 4, Command ≥ 3

**Composition distribution (auto):** When player selects Horseshoe + composition (e.g., 70% melee / 30% ranged), the system distributes:
- Front-left: 25% of unit (mostly melee)
- Front-center: 5% of unit (thin holding force)
- Front-right: 25% of unit (mostly melee)
- Mid-left: 10% (support/cavalry)
- Mid-center: 0% (gap)
- Mid-right: 10% (support/cavalry)
- Back-left: 12% (archers)
- Back-center: 0% (gap)
- Back-right: 13% (archers)
- Manual cell adjustment available

**Phase 5 effects:**
- Center column: −2D Off, +1D Def (thin holding force)
- Flank columns: +1D Off when enemy unit is engaged with center column (the trap closes)
- Without enemy in center, flank columns fight Line

**Failure mode:** Discipline drop below 4 → drifts to Refused Flank (chosen flank) → drifts to Line at Discipline ≤ 2

**Designed exploit:** Enemy that advances into the center is now flanked by both flank columns. Triggers ED-805 combined attack opportunity if multiple of your columns engage the same enemy unit.
```

ED-816 wraps the 5 shape specs in one ED:

```yaml
- id: ED-816
  date: 2026-05-11
  description: "Unit shape mechanical signatures. Five canonical shapes: Line, Arrowhead, Horseshoe, Gapped Line, Refused Flank. Each specifies: minimum Discipline/Command, auto-distribution from base composition, Phase 5 column effects, failure mode, designed tactical exploit. Replaces existing Formation Types section (Wedge becomes Arrowhead preset; Shield Wall becomes Line+heavy front; Skirmish becomes spread-Line; Feigned Retreat becomes proto-Horseshoe). Custom cell overrides allowed."
  severity: P1
  type: missing
  archetype: A2
  affected_docs:
    - designs/provincial/mass_battle_v30.md
    - params/mass_combat.md
  status: closed
  closure_commit: pending-this-session
  jordan_decision: "2026-05-11 — Five shapes ratified with mechanical signatures per workplan §4.2."
```

ED-817 specifies cascade:

```yaml
- id: ED-817
  date: 2026-05-11
  description: "Shape failure cascade — drift model. When unit Discipline drops below shape's minimum, shape degrades one tier toward simpler formation. Drift order: Gapped Line → Horseshoe → Arrowhead → Refused Flank → Line → mob. Drift fires at Phase 6 Step 2 (after Discipline check). Drift is permanent for the battle (no re-acquisition mid-battle). Reform Phase may restore Discipline but not original shape — once a horseshoe collapses, it fights as Line for remainder."
  severity: P1
  type: missing
  archetype: A2
  affected_docs:
    - designs/provincial/mass_battle_v30.md
  status: closed
  closure_commit: pending-this-session
  jordan_decision: "2026-05-11 — Drift model. Shape erodes through tiers, irreversible mid-battle."
```

**Phase 2 exit criteria:** ED-816 and ED-817 committed. Shape specifications canonical.

---

## §6 — PHASE 3: BATTLE RESOLUTION EDs

**Session 3 scope.** ED-811 (engagement formula), ED-818 (combined attack × column), ED-820 (shape-locking + emergency reshape).

### §6.1 ED-811 (engagement formula) — degree-gated symmetric

```yaml
- id: ED-811
  date: 2026-05-11
  description: "Engagement damage formula — degree-gated symmetric contested. Both attacker and defender roll their respective pools (Off pool TN7 and Def pool TN7). Apply degree table to BOTH rolls: attacker's degree(att_net, max(1, def_net)) drives attacker→defender damage; defender's degree(def_net, max(1, att_net)) drives defender→attacker counter damage. Damage by degree (both sides): Overwhelming = 1+Power; Success = Power; Partial = 1; Failure = 0. Passive defense (def Failure) = no counter; active defense (def Partial or better) = real counter damage. Caps lethality at 1+Power per side per exchange. Replaces INTERPRETATION-01 margin model from SIM-MB-04 that produced one-turn kills."
  severity: P1
  type: missing
  archetype: A2
  affected_docs:
    - designs/provincial/mass_battle_v30.md
    - params/mass_combat.md
  status: closed
  closure_commit: pending-this-session
  jordan_decision: "2026-05-11 — Degree-gated symmetric. Both sides apply degree table; passive defense yields no counter, active defense counters in kind."
```

### §6.2 ED-818 Combined attack × column

```yaml
- id: ED-818
  date: 2026-05-11
  description: "ED-805 combined attack interaction with ED-814/818 columns. Lead attacker designates a defender column to target. Supporters contribute floor(their_pool / Fib(n)) to the lead's column pool. The combined pool engages one defender column at concentrated strength. Defender's column rolls its defense; remaining defender columns are not engaged this exchange. Preserves ED-805 strategic intent (concentrated assault) while integrating with column system. Defender columns not engaged this turn may act normally next turn or commit support if reserves available."
  severity: P1
  type: missing
  archetype: A2
  affected_docs:
    - designs/provincial/mass_battle_v30.md
  status: closed
  closure_commit: pending-this-session
  jordan_decision: "2026-05-11 — Combined attack concentrates on one defender column. Other defender columns remain active for subsequent exchanges."
```

### §6.3 ED-820 Shape locking + emergency reshape

```yaml
- id: ED-820
  date: 2026-05-11
  description: "Shape locked at battle setup. Once battle begins, shape cannot be voluntarily changed. Emergency reshape available at Phase 1 declaration: general commits Command check Ob 3. Success = unit transitions to new declared shape effective immediately. Failure = unit fights confused this turn (-2D all pools, no Phase 5 attack at full strength). Reshape is a desperation move — historically accurate (Vegetius, Maurice: mid-battle reshape signals losing position). Reserve commitment (Phase 3) is the standard in-battle adjustment lever; reshape is the emergency. Aligns with historical doctrine: shape = pre-battle decision, reserve = mid-battle decision, reshape = emergency."
  severity: P1
  type: missing
  archetype: A2
  affected_docs:
    - designs/provincial/mass_battle_v30.md
    - params/mass_combat.md
  status: closed
  closure_commit: pending-this-session
  jordan_decision: "2026-05-11 — Shape locked at battle setup. Emergency reshape via Command Ob 3."
```

**Phase 3 exit criteria:** ED-811, ED-818, ED-820 committed.

---

## §7 — PHASE 4: COMPOSITION + PARAMS EDs

**Session 4 scope.** ED-814 (compositional grid), ED-819 (unit parameters), ED-813 (withdrawal phase resolution).

### §7.1 ED-814 Compositional grid

```yaml
- id: ED-814
  date: 2026-05-11
  description: "Unit composition replaces is_ranged binary. Each unit has a compositional grid (3 rows × 3 columns = 9 cells) plus base composition percentages (melee%/ranged%/support% summing to 100). Player workflow: (1) set base composition at army-build, (2) select shape template at battle-setup, (3) system auto-distributes troops across 9 cells according to shape, (4) player may manually override any cell. Football Manager-style adjustable allocation array. Rows: front (engagement), mid (cavalry/Thread/support), back (volley). Columns: left/center/right map to discrete sub-pools (ED-818). Derived stats (Speed, effective Power per phase, Volley pool) computed as weighted averages over cells. Cavalry component carries heaviest speed weight. Empty cells are vulnerabilities (Gapped Line shape exploits this)."
  severity: P1
  type: missing
  archetype: A2
  affected_docs:
    - designs/provincial/mass_battle_v30.md
    - params/mass_combat.md
    - designs/provincial/military_layer_v30.md
  status: closed
  closure_commit: pending-this-session
  jordan_decision: "2026-05-11 — Compositional grid with auto-distribution and manual override. FM-pattern."
```

### §7.2 ED-819 Unit parameters

```yaml
- id: ED-819
  date: 2026-05-11
  description: "Per-unit standing orders (FM-style team instructions). Five parameters: (1) Aggression — Cautious/Balanced/Pressing — forward bias in Phase 3 movement, engagement at long odds; (2) Cohesion priority — Hold shape/Adapt to pressure — Discipline check Ob 2 vs accepting shape drift toward Line; (3) Pursuit — None/Routed only/Aggressive — Phase 7 routed-enemy chase behavior; (4) Reserve discipline — Hold/Commit on heavy losses/General's discretion — self-commit rules; (5) Targeting — Nearest/Highest-threat/Lowest-Discipline/Specified column — Phase 5 target priority. Parameters set at army-build (faction defaults), adjustable at battle-setup per unit. Discipline gates execution — low Discipline unit drifts toward survival behavior regardless of orders. Maps to historical commander problem: knights with low Discipline ignore orders to hold and charge for glory."
  severity: P1
  type: missing
  archetype: A2
  affected_docs:
    - designs/provincial/mass_battle_v30.md
    - params/mass_combat.md
    - designs/provincial/military_layer_v30.md
  status: closed
  closure_commit: pending-this-session
  jordan_decision: "2026-05-11 — Five parameters, FM-style, army-build defaults + battle-setup overrides."
```

### §7.3 ED-813 Withdrawal phase gate

```yaml
- id: ED-813
  date: 2026-05-11
  description: "ED-801 withdrawal mechanic fires at Phase 1 (strategy declaration), not Phase 5. Withdrawing unit with Speed > pursuer Speed declares Withdraw plan at Phase 1; pursuer cannot enforce engagement during Phase 5 if positional adjacency is broken in Phase 3 manoeuvre. Phase 5 gate (original SIM-MB-04 implementation) was incorrect — withdrawal must prevent contact, not roll-block. Resolves FINDING-7."
  severity: P2
  type: clarification
  archetype: A2
  affected_docs:
    - designs/provincial/mass_battle_v30.md
  status: closed
  closure_commit: pending-this-session
  jordan_decision: "2026-05-11 — Phase 1 declaration prevents contact. Phase 5 was incorrect."
```

**Phase 4 exit criteria:** ED-814, ED-819, ED-813 committed. All 10 new EDs (811-820) closed in ledger.

---

## §8 — PHASE 5: PROPAGATE ED-800..810 TO CANONICAL DOCS

**Session 5 scope.** Propagate the already-closed EDs to mass_battle_v30.md and params files. From SIM-MB-04 handoff: ED-800,801,802,804,805,806,807,808 all need propagation.

Targets:

| ED | File | Section | Change |
|---|---|---|---|
| ED-800 | params/mass_combat.md | Phase 2 Volley | Volley pool = min(Size,Power)+Power at TN6 |
| ED-800 | mass_battle_v30.md | §A.7 Phase 2 | Add Size-scaling clause |
| ED-801 | mass_battle_v30.md | §A.12 Rout/Pursuit | Add Orderly Withdrawal subsection (referencing ED-813 Phase 1 gate) |
| ED-802 | mass_battle_v30.md | §A.7 Phase 6 Step 4 | Add Rally formula: Morale dice TN7 Ob1 → +1 Morale on success |
| ED-804 | none | n/a | No-op per Jordan ruling |
| ED-805 | mass_battle_v30.md | §A.7 Phase 5 | Add Combined Attack subsection (lead + Fibonacci-denominator supporters, integrating ED-818) |
| ED-806 | params/bg/core.md | Territory table | Gransol Fort 2 entry added |
| ED-807 | mass_battle_v30.md | §A.14 or new section | Lake supply non-blockadeable rule |
| ED-808 | mass_battle_v30.md | §E.1 | Defender −1 Stability on territory loss only; attacker no penalty |

Bootstrap scope: `editorial`. Co-file: when mass_battle_v30.md changes, `references/canonical_sources.yaml` must update SHA.

**Phase 5 exit criteria:** ED-800..808 fully propagated to canonical docs. SHAs updated in canonical_sources.yaml.

---

## §9 — PHASE 6: PROPAGATE ED-811..820 TO CANONICAL DOCS

**Session 6 scope.** Major rewrite of mass_battle_v30.md §A.4 (Unit Stat Block) through §A.7 (Battle Turn Structure). Likely 2-3k tokens of canonical changes.

Sections to rewrite or insert:

| Section | Change |
|---|---|
| §A.4 Unit Stat Block | Add composition fields (melee%, ranged%, support%); reference 9-cell grid; Discipline redefinition (ED-815) |
| §A.4a (NEW) Unit Parameters | Standing orders per ED-819 |
| §A.6 Shape Templates | Rewrite Formation Types as Shape Templates per ED-816; preserve Wedge/Shield Wall/Skirmish as legacy presets that map onto shape system |
| §A.6a (NEW) Shape Failure Cascade | ED-817 drift model |
| §A.7 Phase 1 | Add shape declaration line; reference ED-820 lock + emergency reshape |
| §A.7 Phase 2 Volley | ED-812 net successes formula (already in §8 from ED-800 propagation; refine) |
| §A.7 Phase 5 Engagement | ED-811 degree-gated formula; ED-818 column resolution |
| §A.7 Phase 5a (NEW) Combined Attack | ED-805 + ED-818 integrated |
| §A.7 Phase 6 Step 2 | Discipline check integrated with shape drift (ED-817) |

This is the largest single propagation in the redesign. Phase 6 is the highest-risk session — context budget will be tight and the doc is dense.

**Phase 6 exit criteria:** mass_battle_v30.md fully reflects ED-811..820. canonical_sources.yaml SHA updated. Backward-incompatible changes flagged in commit message.

---

## §10 — PHASE 7: SIM REFACTOR (SIM-MB-05)

**Session 7 scope.** Refactor `tests/sim/sim_mass_battle_SIM-MB-04.py` into SIM-MB-05 reflecting the new mechanics.

Refactor targets:

### §10.1 Data model changes

```python
@dataclass
class CompositionGrid:
    """ED-814: 3x3 grid of (troop_type, fraction). Sum across grid = 1.0."""
    cells: Dict[Tuple[int,int], Tuple[str, float]]  # (row, col) → (type, %)

@dataclass
class Unit:
    name: str
    faction: str
    base_composition: Dict[str, float]  # melee_pct, ranged_pct, support_pct
    shape: str  # ED-816 shape template
    grid: CompositionGrid  # auto-populated from base + shape
    parameters: Dict[str, str]  # ED-819 standing orders
    # ... existing stats unchanged ...
```

### §10.2 Engagement resolution rewrite

```python
def resolve_engagement_ed811(att_col_pool, def_col_pool, att_power, def_power) -> Dict:
    """ED-811: degree-gated, symmetric contested."""
    att_net = roll_d10_pool(att_col_pool)
    def_net = roll_d10_pool(def_col_pool)
    att_ob = max(1, def_net)
    def_ob = max(1, att_net)
    att_degree = degree(att_net, att_ob)
    def_degree = degree(def_net, def_ob)
    # Damage tables per ED-811
    dmg_to_def = DAMAGE_BY_DEGREE[att_degree](att_power)
    dmg_to_att = DAMAGE_BY_DEGREE_DEFENDER[def_degree](def_power)
    return {"dmg_to_def": dmg_to_def, "dmg_to_att": dmg_to_att}
```

### §10.3 Shape mechanics

Each shape becomes a class implementing:
- `distribute(unit) -> CompositionGrid` — auto-populate cells
- `phase5_modifiers(column) -> {off_mod, def_mod}` — per-column effects
- `min_discipline -> int`
- `degrade_to() -> ShapeType` — drift target per ED-817
- `designed_exploit(state) -> EncounterModifier` — when the trap fires

### §10.4 Parameter execution

```python
def execute_parameters(unit, situation) -> ActionDirective:
    """ED-819: parameters gated by Discipline.
    High Discipline + clear orders = execute as designed.
    Low Discipline = drift toward survival behavior."""
    if unit.discipline >= 5:
        return follow_orders(unit, situation)
    elif unit.discipline >= 3:
        return mostly_follow_orders(unit, situation, drift_chance=0.3)
    else:
        return survival_behavior(unit, situation)
```

### §10.5 Sim infrastructure

- Update `sim_verification_ledger.json` with new constants (degree damage tables, shape thresholds, parameter effects)
- Update `sim_module_manifest.md` with new modules: composition_grid, shape_distribution, parameter_execution, engagement_ed811, volley_ed812
- Module isolation tests for each new piece

**Phase 7 exit criteria:** SIM-MB-05.py and supporting files exist, isolation tests pass, manifest + ledger valid for sim_gate.

---

## §11 — PHASE 8: SIM CYCLE 1 — ISOLATION TESTS

**Session 8 scope.** Mode A simulations per `valoria-simulator` SKILL.md. One module at a time.

Tests required:

| Module | Test |
|---|---|
| Dice engine | 1000-trial degree distribution validation (already in SIM-MB-04, retain) |
| ED-811 engagement | Equal-pool 1000-trial; verify P(Overwhelming) ~30%; mean damage = E(degree)·E(Power); cap-correctness |
| ED-812 volley | 1000-trial; verify mean = E(net) − rDR; no Power multiplier present |
| ED-814 composition distribution | For each shape × each base composition: verify cells sum to 1.0; verify shape signature cells populated correctly |
| ED-815 Discipline penalty | Verify pool penalty applies correctly at each tier; verify formation broken trigger |
| ED-816 shape signatures | For each shape: verify Phase 5 modifiers apply to correct columns; verify min Discipline gate |
| ED-817 shape cascade | Inject Discipline drop; verify shape drifts one tier per check; verify irreversibility within battle |
| ED-818 combined attack | Lead + 2 supporters on one column: verify Fibonacci sum; verify other defender columns unaffected |
| ED-819 parameters | Per parameter × Discipline tier: verify execution probability matches spec |
| ED-820 shape lock | Verify Phase 1 reshape costs Command Ob 3; verify failure penalty applies |

**Phase 8 exit criteria:** All isolation tests pass. SIM-MB-05-A report committed.

---

## §12 — PHASE 9: SIM CYCLE 2 — INTERACTION TESTS

**Session 9 scope.** Mode B simulations — paired mechanics that interact.

Scenarios:

1. **Shape × Composition matrix** — for each (shape, base_composition) pair: run 10 single-turn engagements vs Line+Line. Identify which combinations are dominant, viable, weak.
2. **Horseshoe trap test** — Side A horseshoe vs Side B advancing Line. Verify Phase 5 mechanics fire: Side B engages center, flanks activate +1D Off bonus, Side A executes ED-805 combined attack on Side B center column.
3. **Gapped Line trap test** — Side A gapped line; Side B advances. If Side B avoids gap: small engagement. If Side B enters gap: severe encirclement damage per PP-683 (cap removed).
4. **Shape vs Shape duels** — each shape vs each other shape on equal Power/Size. 100-trial sample. Generate rock-paper-scissors matrix.
5. **Discipline degradation chains** — Side A with Discipline 4 horseshoe under sustained pressure. Verify drift order: Horseshoe → Refused Flank → Line.
6. **Parameter interactions** — same units, different parameter sets (Cautious/Hold Shape/Hold Reserve vs Pressing/Adapt/Aggressive Pursuit). Verify divergent outcomes.
7. **Combined attack × column distribution** — 3 attackers Fibonacci-combined on one defender column. Verify pool calc, verify other columns unaffected. Compare to 3 attackers on 3 columns separately.

**Phase 9 exit criteria:** SIM-MB-05-B report committed. Shape matrix table generated.

---

## §13 — PHASE 10: SIM CYCLE 3 — FULL SCENARIOS

**Session 10 scope.** Mode C simulations — multi-turn battles with full composition + parameters + grid map.

Scenarios (rerun the SIM-MB-04 set with new mechanics):

| Scenario | Setup | Validation target |
|---|---|---|
| S1 — Crown 3v2 Varfell straight | Crown Arrowhead + 2-unit Varfell Line | Battle lasts 3-6 turns (vs SIM-MB-04's 1 turn) |
| S2 — Crown horseshoe trap | Crown Horseshoe + 2-unit Varfell aggressive Line | Verify trap mechanics fire if Varfell advances; verify Combined Attack on center |
| S3 — Hafenmark vs Crown | Hafenmark 3-unit Gapped Line + Crown 2-unit Arrowhead | Verify Discipline differential matters; Mil 3 vs Mil 5 outcomes |
| S4 (NEW) — Composition asymmetry | 60/40 mixed Crown unit vs 100/0 pure-melee Crown unit | Verify back row contribution; verify melee asymmetry |
| S5 (NEW) — Parameter divergence | Identical units, opposed parameter sets | Verify parameters affect outcomes meaningfully |

For each scenario, log: turn count, casualty rates per turn, shape state per turn, Discipline trajectory, Morale trajectory, winning condition.

**Validation targets (whole-system level):**
- Battles last 3-6 turns on average
- No one-turn kills against equal-Power matched-Discipline units
- Composition affects outcomes (a 60/40 unit and a 100/0 unit produce visibly different battle curves)
- Shape choice affects outcomes (horseshoe wins ~60-70% vs aggressive Line per design intent)
- Discipline gates shape execution (low-Disc unit drifts to Line under fire)

**Phase 10 exit criteria:** SIM-MB-05-C report committed. coverage_matrix.md updated. Workplan retrospective written.

---

## §14 — SESSION-LEVEL EFFORT ESTIMATES

| Phase | Sessions | Estimated context per session |
|---|---|---|
| 1 | 1 | 30-40% — clean ED writes |
| 2 | 1 | 40-50% — shape spec is dense |
| 3 | 1 | 40-50% — three EDs with interactions |
| 4 | 1 | 40-50% — composition is largest single ED |
| 5 | 1 | 50-60% — multi-file propagation |
| 6 | 1-2 | 70-80% — major mass_battle_v30.md rewrite, may split |
| 7 | 1 | 50-60% — sim refactor |
| 8 | 1 | 40-50% — isolation tests |
| 9 | 1 | 50-60% — interaction tests |
| 10 | 1 | 50-60% — full scenarios |
| **Total** | **10-11 sessions** | — |

---

## §15 — DEPENDENCIES + CRITICAL PATH

Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7 → Phase 8 → Phase 9 → Phase 10

No parallelism — each phase strictly requires prior phases. The critical path is the whole workplan. Phases 1-4 are EDs only (can be done back-to-back). Phases 5-6 are propagation (heavy doc work). Phases 7-10 are sim work.

**Recovery points:**
- After Phase 4: all EDs written, design is locked. If sim later reveals problems, EDs can be amended.
- After Phase 6: canonical docs reflect design. Sims test what's in canon.
- After Phase 10: full validation. Workplan complete.

**Abort points:**
- If §2 open items can't be resolved: Phase 1 still proceeds (foundation EDs are independent), but Phase 2 and Phase 3 block until resolved.
- If sim cycle 1 (Phase 8) reveals fundamental issues: pause for design re-pass before Phases 9-10.

---

## §16 — INTEGRATION WITH PARENT WORKPLAN

`references/simulation_workplan_v1.md` covers the 9-archetype campaign (A1-A9). This workplan addresses a subset: A2 TOTAL WAR follow-up specifically.

After completion:
- A2 mass battle layer is fully redesigned and validated
- A3 SCHISM can proceed (workplan v1 §6.3)
- Other archetypes (A4-A9) inherit the new mass battle mechanics where relevant

This workplan does NOT delay A3 SCHISM materially — A3 exercises CI/Seizure/Church mechanics, which are largely independent of the mass battle redesign. A3 can run in parallel with later phases of this workplan (specifically Phases 7-10) if context budget allows split sessions.

---

## §17 — OPEN ITEMS AFTER COMPLETION

Even with this workplan executed:

- Strategic-layer interaction with composition (how do faction-level Military stats interact with per-unit composition?)
- Personal-scale character integration with parameter system (player-character commanders)
- Long-tail shape specifications (Crescent, Echelon, Hollow Square, Convex, Concave — historical formations not in the 5-shape core set)
- Naval mass battle (does the system extend to ships? Probably yes, with shape templates for line-of-battle, double line, etc.)
- Editorial: existing sims (SIM-MB-01..04) use old mechanics; may need re-runs or annotations

These are not blockers — they're forward-looking items for future workplans.

---

## §18 — CHANGELOG

| Version | Date | Notes |
|---------|------|-------|
| v1 | 2026-05-11 | Initial draft with §2 open items. Author: this session. |
| v1.1 | 2026-05-11 | All §2 items ratified via historical precedent + acclaimed game design + NERS audit. BG/TTRPG terminology corrected to videogame-only framing. ED-811 finalized as degree-gated symmetric (Civilization VI / Total War / Vegetius precedent). Shape minimums adjusted: Arrowhead 3→4, Horseshoe 4→5 (Macedonian wedge / Cannae historical precedent). Cascade resolved as shape-specific drift to Line, irreversible mid-battle (Strategikon precedent). Combined attack resolved as single-column concentration (Cannae precedent). Composition granularity resolved as faction templates + per-unit override (Football Manager pattern). Phase 1 execution begins this session. |
