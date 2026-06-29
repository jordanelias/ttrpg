<!-- [PROVISIONAL: 2026-05-10 — PP-724 NPC-NPC relational graph framework; Class A new system; B1.1 of improvement_avenues_2026-05-10] -->
<!-- STATUS: PROVISIONAL — Class A canonical document. -->
<!-- AUTHORITY: PP-724 -->
<!-- COMPANIONS: designs/npcs/character_canon_v30.md (per-NPC vector state), designs/npcs/npc_behavior_v30.md (priority trees + Resonant Style), designs/scene/fieldwork_v30.md §5.6b (Knot lifecycle — architectural template for this doc's strain mechanics), designs/territory/valoria_geography_v30.yaml :: settlement_adjacency: (PP-723; consumed by §6 settlement coupling) -->

# Valoria — NPC Relational Graph (PP-724)
## Status: CANONICAL (generation v40)

**Class:** A — new substrate-defining system. Personal-scale NPC-NPC relational state.
**Status:** PROVISIONAL.
**Co-files:** `references/glossary.md` (new term: "edge", "tie", "relational strain"), `references/canonical_sources.yaml` (this doc as new canonical), `canon/patch_register_active.yaml` (PP-724).

---

## §0 Purpose and Scope

**Purpose.** Specify the canonical NPC-to-NPC relational state that Valoria's existing canon assumed but did not define. Faction emergence (`settlement_layer §6.2 Stage 2→3`) requires "2 NPC officers with Disposition +3" — Disposition is PC-NPC; the question of *what officers feel about each other* had no canonical answer. Cesare ↔ Almud succession rivalry (`migration_roster §2.1`), Yrsa ↔ Maret Vossen kinship (PP-665 rename context), Solmund ↔ Baralta scholarly tie — all these are visible in canonical prose but had no mechanical state. This framework fills that gap.

**Scope.** NPC-to-NPC ties only. PC-NPC relations remain governed by the existing Disposition + Knot system (`fieldwork §3` and `§5.6`). PC-NPC and NPC-NPC ties compose through shared participation in scenes but do not collapse into one mechanic.

**Source ambition.** KOEI Romance of the Three Kingdoms (officer-network defection cascades, sworn-bond rituals, kinship bonds across cities), Crusader Kings III (vassal hierarchies, dynastic rivalries, scheme targets). Both named precedents in `settlement_layer §Precedent` and `settlement_adjacency_v30 :: Canon compliance`. This doc canonizes the relational substrate those precedents named without specifying.

**Architectural template.** F2 Knot lifecycle (`fieldwork §5.6b`, ED-773). Each canonical edge has formation conditions, strain accumulation rules, capacity, break consequences, rupture triggers, and strain decay rules — paralleling Knot but applied to NPC↔NPC pairs.

**Class A justification.** New substrate (named edge types not previously canonical), new state machine, new stat surface (per-edge strain). Not a parameter change to existing mechanics. Affects: `npc_behavior_v30` (Decision Fork inputs gain relational pressure), `faction_politics_v30` (defection-cascade hooks for B1.2), `settlement_layer §6.2` (Stage 2→3 prerequisite gains relational specificity), `mass_battle_v30` (officer-network state at battle resolution).

**Deferred.** This doc is **B1.1** of the four-PP relational-graph track:
- **B1.1 (this PP-724):** edge type taxonomy + per-edge state machine + composition rules.
- **B1.2 (deferred):** defection cascade resolution mechanics. Hooks specified in §7 below; full mechanics future PP.
- **B1.3 (deferred):** faction-Cascade integration (centrality-weighted aggregation per PP-686 §3.2). Hooks in §8.
- **B1.4 (deferred):** settlement-coupling rules (geographic strain on cross-territory ties). Hooks in §6.

---

## §1 Statement

A **relational edge** between two named NPCs models a binding, oath, kinship, or rivalry that shapes how each interprets the other's actions and how their behavior couples in faction-Cascade aggregation. Each edge has a canonical type (`§2`), directionality, strength, formation conditions, strain accumulation, capacity, break/rupture rules. Edges compose: two NPCs may have multiple edges (a sworn-bond ally who is also a rival; a liege-vassal who is also kin). Composition rules in `§5`.

The state lives on the dyad, not on individual NPCs. Each NPC's individual character state (Conviction vector, Self-Other, TS, Coherence, Spirit, Certainty per `character_canon §3-§7`) is unchanged.

**The substrate question this answers.** The framework has *renderable* (`canon/01 §Am 3`) per individual; relational edges are renderable *between* individuals. A patron-client tie is substrate-real per `М-3` (substrate grounds all): the rendering of authority flowing from patron to client *is* a configuration of Thread-substrate at the dyadic level, not a flavor-tag. This grounds NPC-NPC mechanics ontologically the same way `М-9` grounds clinical-trauma vocabulary at the personal level.

---

## §2 Edge Type Taxonomy

Six canonical edge types. Each captures a distinct Renaissance political-relational dynamic with period precedent. Additions are Class B extensions; rename or removal is Class A.

| # | Type | Directionality | Strength | Renaissance precedent |
|---|------|----------------|----------|----------------------|
| 1 | **Sworn-bond** | Symmetric | 1–3 | *fede giurata*, military brotherhood, Liu/Guan/Zhang oath |
| 2 | **Liege-vassal** | Asymmetric (liege → vassal) | 1–3 | feudal *fidelitas*, knight to lord, *commendatio* |
| 3 | **Kinship** | Symmetric (special asymmetric for parent→child) | 1–3 | blood relation; lineage; family |
| 4 | **Patronage** | Asymmetric (patron → client) | 1–3 | Medici *clientela*, episcopal patronage, courtly *benefitium* |
| 5 | **Rivalry** | Symmetric (often) or asymmetric | 1–3 (negative valence) | succession contests, faction-internal competition |
| 6 | **Feud** | Symmetric | 1–3 (negative valence; hereditary) | blood-feud, vendetta, lineage-grudge |

**Per-edge fields:**
```yaml
edge:
  type: <one of {sworn-bond, liege-vassal, kinship, patronage, rivalry, feud}>
  from: <NPC-id A>
  to:   <NPC-id B>
  strength: 1..3   # for sworn-bond/liege-vassal/kinship/patronage: positive bond intensity
                   # for rivalry/feud: negative valence intensity (still 1..3 magnitude)
  formed: <date or scenario marker>
  formed_by: <event description>
  strain: 0..capacity   # current strain count; see §3
```

### §2.1 Sworn-bond
**Definition.** Mutually pledged oath of solidarity, typically grounded in shared service, military bond, or convergent cause. Symmetric — both parties hold the bond equally.
**Period precedent.** Italian *fede giurata* between condottieri; Florentine *compagnonnage*; the canonical Liu/Guan/Zhang oath in ROTK.
**Strength tiers:** 1 = pledged but untested; 2 = tested in shared adversity; 3 = blood-proven (typically requires having stood together in mortal danger).
**Conviction coupling.** Sworn-bonds activate **Solidarity Resonant Style** (per `npc_behavior §1.3`) between bonded parties — a Solidarity appeal from a sworn-bond partner cannot be dismissed without strain accrual.
**Formation conditions:** see §4.1.

### §2.2 Liege-vassal
**Definition.** Asymmetric authority-tie: liege provides protection, position, or *benefitium*; vassal provides loyalty, service, deference. Liege's actions toward vassal carry institutional weight; vassal's defiance is institutionally visible.
**Period precedent.** Feudal *fidelitas*; *commendatio* ceremony; sub-vassalage chains under Holy Roman Emperor; Italian *condotta* contracts.
**Strength tiers:** 1 = nominal (paper-bond); 2 = active service (regular interaction); 3 = sworn-vassal (oath-formal, broken only at honor cost).
**Conviction coupling.** Activates **Authority Resonant Style** from liege toward vassal. Vassal's Authority Conviction is engaged on every liege-issued direction.
**Hierarchical chains.** Vassals may have their own vassals (sub-liege relationship). Defection of a mid-chain liege has cascade implications (B1.2).
**Formation conditions:** see §4.2.

### §2.3 Kinship
**Definition.** Blood relation, marriage relation, or formally-adopted lineage tie. Largely structural rather than chosen.
**Period precedent.** Lineage politics across the Italian city-states; Habsburg dynastic logic; clan-based Highland politics.
**Strength tiers:** 1 = distant kin (cousin, in-law); 2 = household kin (sibling, parent-of-adult-child); 3 = direct kin (parent-of-minor-child, twin, primary spouse).
**Sub-types:**
- *symmetric*: sibling, cousin, spouse.
- *asymmetric (parent→child)*: parental kinship has direction-of-authority semantics (parent has Authority weight over minor child; this attenuates as child reaches adulthood).
**Conviction coupling.** Activates **Solidarity** Resonant Style (kin-as-Solidarity), and additionally **Identity** Conviction engagement for both parties (lineage = Identity-frame per `conviction_taxonomy §2`).
**Special break rules.** Kinship cannot be ruptured by ordinary strain — only by formal disinheritance (institutional act) or death. See §3.4.

### §2.4 Patronage
**Definition.** Asymmetric favor-tie: patron extends benefits (position, gold, reputation, advice); client extends loyalty, service, public alignment. Distinct from liege-vassal: patronage is informal/relational where liege-vassal is institutional/oathbound. A patron is not necessarily an institutional liege.
**Period precedent.** Medici *clientela* in Florentine politics; *raccomandazione* in Italian courts; episcopal patronage of artisans, scholars, junior clergy; Roman *clientela* survivals through the Renaissance.
**Strength tiers:** 1 = recent or transactional (single benefit exchanged); 2 = sustained (multiple seasons of mutual support); 3 = structural (client's career or position depends on patron).
**Conviction coupling.** Activates **Authority** Resonant Style (patron→client; weaker than liege-vassal but real). Client's Self-Other orientation drifts toward "patron's interests = my interests" under sustained strength-3 patronage.
**Formation conditions:** see §4.4.

### §2.5 Rivalry
**Definition.** Mutually-recognized adversarial position, typically structural (competing for same office, same favor, same succession line). Distinct from feud: rivalry is goal-competitive, not honor-grievance. Cesare ↔ Almud succession competition is the canonical example.
**Period precedent.** Italian succession contests; Medici-Pazzi rivalry pre-conspiracy; condottieri reputation-rivalry; cardinal pre-conclave maneuvering.
**Strength tiers:** 1 = recognized competitor (each aware of the other); 2 = active opposition (taking moves against each other); 3 = existential rivalry (one of us must fall).
**Conviction coupling.** Each party's Decision Fork against rival prefers options that disadvantage rival, regardless of mainstream Conviction-frame. **Evidence** and **Consequence** Resonant Styles operate normally (rivals can be argued with) but **Solidarity** is structurally suppressed (no bond to invoke).
**Asymmetry option.** Most rivalries are symmetric; some are asymmetric (one side recognizes the rivalry, the other does not). Asymmetric rivalry is unstable and tends to symmetric over 1–2 seasons of exposure.
**Formation conditions:** see §4.5.

### §2.6 Feud
**Definition.** Hereditary or grievance-rooted enmity. More structurally durable than rivalry — does not dissipate when proximate cause is removed. Often inherited from kin (a feud transmits along strong kinship edges per §3.5).
**Period precedent.** Italian blood-feuds; Capulet/Montague (Veronese precedent); Highland clan feuds; *vendetta* tradition.
**Strength tiers:** 1 = grudge (specific grievance, recent); 2 = standing feud (multi-season, multiple incidents); 3 = blood-feud (inherited; spans generations; active honor-debt).
**Conviction coupling.** Same Decision-Fork suppression as rivalry, plus: **Solidarity** with parties bonded to feud-target is *strained* — supporting an enemy of the feud-partner accrues strain on the supporter's own bonds.
**Cannot be ruptured by ordinary means.** Feuds end only via formal blood-price (institutional act, costs Wealth + Mandate per faction), public reconciliation ritual (rare; requires Stature 5+ on both sides + Cathedral or Seat venue), or extinction of one feuding line.

---

## §3 Strain Mechanics (Knot-Lifecycle Mirror)

Mirrors `fieldwork §5.6b` Knot lifecycle architecture, applied to NPC-NPC dyads. Each edge accumulates strain through specified mechanisms; at capacity, the edge breaks (or, for kinship/feud, transitions). Strain decays under sustained edge-aligned conditions.

### §3.1 Strain capacity by edge type and strength

| Edge type | Strength 1 | Strength 2 | Strength 3 |
|-----------|-----------:|-----------:|-----------:|
| Sworn-bond | 3 | 5 | 7 |
| Liege-vassal | 3 | 5 | 7 |
| Kinship | n/a (cannot break by strain; see §3.4) | n/a | n/a |
| Patronage | 2 | 4 | 6 |
| Rivalry | n/a (no break by strain; see §3.5) | n/a | n/a |
| Feud | n/a (cannot break by strain; see §3.5) | n/a | n/a |

**Reading the table.** Sworn-bond and liege-vassal carry the same capacity profile (oath-bound categories). Patronage is structurally less load-bearing — clients change patrons; structural patronage (strength 3) lasts but is more strain-fragile than structural sworn-bond. Kinship/rivalry/feud are persistent state — they don't break by strain accumulation; they transition (rivalry can resolve to sworn-bond or feud) or persist permanently (kinship/feud).

### §3.2 Strain accrual mechanisms (per edge type)

**Sworn-bond:**
- Public action contradicting partner's stated position: **+1 strain**.
- Partner taking Conviction Scar that the bond-holder could have prevented: **+1 strain at next Accounting**.
- Forced choice between bond-aligned action and faction-aligned action where bond-aligned was rejected: **+1 strain**.
- Witnessing partner's Coherence drop from action that bond-holder participated in: **+1 strain**.
- Sustained absence (no shared scene for 4+ consecutive seasons): **+1 strain at the 4th season's Accounting**.

**Liege-vassal:**
- Liege issuing direction that vassal failed to execute: **+1 strain** (liege side accrues; vassal also accrues if Conviction conflict).
- Vassal acting against liege's stated interest publicly: **+2 strain** (both sides).
- Liege failing to protect vassal's standing during faction-political incident: **+1 strain** (vassal side primarily).
- Vassal accepting external patronage from rival faction: **+1 strain immediate, +1 strain/season ongoing**.
- Sustained Disposition between liege and vassal below +2 (per `fieldwork §3` Disposition tracking): **+1 strain per Accounting** until resolved.

**Patronage:**
- Patron's *raccomandazione* (introduction, recommendation) failing publicly: **+1 strain** (client side).
- Client publicly aligning with rival of patron: **+1 strain** (patron side, immediate).
- Patron failing to deliver promised benefit: **+1 strain** (client side, lasts until promise resolved).
- Sustained patronage at strength 3 carries an inherent +0.5 strain/season tax (round up at Accounting; net +1 strain per 2 seasons) reflecting the maintenance cost — patron must continually demonstrate value.

**Rivalry / Feud:** strain-equivalent state is the *intensification escalator* (§3.5), not capacity-toward-break. Rivalries don't accumulate toward breaking; they accumulate toward escalating to the next strength tier (or, conversely, de-escalating).

### §3.3 Knot-strain composition (PC-NPC ↔ NPC-NPC interaction)

NPC relational edges and PC Knots co-exist on the same NPCs. **Knot strain (PC-NPC) and edge strain (NPC-NPC) do not aggregate into one counter** — they are distinct state and resolved separately. However, certain events accrue strain on both:

- A Conviction Scar firing in a PC's Knot partner who is also in a sworn-bond with another NPC: PC's Knot takes its strain per `fieldwork §5.6b`; the Knot partner's sworn-bond also takes strain per §3.2 above. Both fire.
- An FR Dissolution targeting an NPC who is in a sworn-bond with a non-victim NPC: the sworn-bond partner takes strain per §3.2; if the dissolution is also Knot-witnessed by a PC, the Knot's separate strain rules apply.

**Composition principle.** Each relational edge (Knot or NPC-edge) is a distinct binding; events that affect a node propagate independently along each binding. This mirrors the substrate-inseparability principle in `02_foundations_amendment` Amendment 2 (P-12) at the dyadic graph level.

### §3.4 Kinship: break and transition rules

Kinship edges are **structurally persistent**. They do not accumulate strain toward break in the §3.1 sense. However, they **transition** between strain-bands:

- **Cooperative kinship (default):** kinship-positive — Solidarity activated, Identity-frame engaged, mutual Disposition floor of +1.
- **Strained kinship:** triggered by sustained adversarial action (3+ Convictionally-opposed actions across consecutive seasons) — Solidarity remains active (Conviction-bound) but Disposition floor lifts; the kin-tie still binds Identity but no longer guarantees cooperation.
- **Severed (formal):** disinheritance via institutional act. Requires Stature 4+ initiator + faction Mandate ≥ 3 + public ceremony (Cathedral or Seat venue). Severs Identity-frame engagement but the *historical kinship* remains canonical (a disinherited child is a former-heir, not a stranger).
- **Dissolved (death):** death of one party ends the active kinship; surviving kin's Memory state retains the relationship as historical context.

Inherited kinship edges propagate per §3.6 Inheritance Rules.

### §3.5 Rivalry / Feud: escalation, de-escalation, transition

Rivalry and feud have an **intensification escalator** rather than strain-toward-break:

| Event | Effect on rivalry | Effect on feud |
|-------|-------------------|---------------|
| Successful adversarial action (intrigue, social contest defeat, faction maneuver) | Strength +1 | Strength +1 |
| Mutual avoidance for 4+ seasons (no adversarial events) | Strength −1 at Accounting | No change (feud is structural) |
| Reconciliation scene (per §4.6 conditions) | Resolves to sworn-bond (rare) or to no-edge | Resolves only via §2.6 break ritual or extinction |
| Death of one party | Edge ends | Feud transmits along strong kinship edges (see §3.6) |
| Formal apology + restitution | Strength −1 (rivalry) | No effect (feud requires blood-price, not apology) |

A rivalry that reaches strength 3 (existential) and remains there for 4+ seasons is at risk of **transition to feud** if a Conviction Scar fires in either party from rival's action. Transition is mechanically: edge type changes from rivalry to feud, strength carries over, all subsequent strain-events use feud rules.

### §3.6 Inheritance and propagation along kinship

When a sworn-bond, liege-vassal, patronage, rivalry, or feud edge holder dies, the edge may **transmit** along strong kinship to a successor:

| Edge type | Transmits along kinship? | Conditions |
|-----------|--------------------------|------------|
| Sworn-bond | Optional (successor's choice) | Only if successor is direct kin (strength 3) AND knew the deceased |
| Liege-vassal | Yes by default | Vassal reports to deceased liege's heir; vassal may renounce within 1 season at Honor cost |
| Kinship | n/a | (already transitive) |
| Patronage | No | Client-patron ties don't auto-transmit; new patron must reaffirm |
| Rivalry | Optional (situational) | If rivalry was over a structural position (succession, office), transmits to successor |
| Feud | **Yes, automatically** | Hereditary feud propagates along all strong kinship (strength 2+) edges from deceased to surviving kin |

Feud's automatic transmission is the key load-bearing mechanic for ROTK-style emergent multigenerational narrative (Capulet/Montague, the canonical Renaissance form).

### §3.7 Strain decay (sworn-bond, liege-vassal, patronage)

Strain decays at **−1 per season at Accounting** if all of the following hold for the season:
- No strain accrual event fired this season for this edge.
- For sworn-bond: NPCs participated in 1+ shared scene at non-adversarial Disposition.
- For liege-vassal: vassal executed at least one liege-issued direction without strain.
- For patronage: patron extended at least one benefit (introduction, gold, reputation backing).

This mirrors `fieldwork §5.6b` Knot strain decay rules (sustained mutual investment dissipates accumulated stress).

### §3.8 Break consequences

When strain reaches capacity for sworn-bond, liege-vassal, or patronage:

**Sworn-bond break:**
- Edge type changes to **rivalry** at strength 1 (broken bond breeds bitterness; Liu Bei vs Lü Bu pattern).
- Both parties take Composure 3 (substrate-disorientation; the inseparability of the sworn rendering releases).
- Both parties take **Conviction Scar +1** on Honor (oath-violation is an Honor-axis wound per `conviction_axis_matrix §3.13`).
- Solidarity Resonant Style on this edge ceases.
- Faction-Cascade implications: per B1.3 hooks (TBD).

**Liege-vassal break:**
- Edge ends; no replacement edge auto-formed.
- Vassal takes **Conviction Scar +1** on Authority (broken oath of fealty wounds Authority-frame).
- Liege takes Mandate damage proportional to vassal's faction position (specifics in B1.3 hooks).
- Defection cascade hook fires (B1.2; vassals-of-vassal may reorient — see §7).

**Patronage break:**
- Edge ends.
- Client takes Stature damage (lost patron costs reputation): **Stature −1** if strength 2; **Stature −2** if strength 3.
- Client may seek replacement patronage; faction AI considers patron-shift in priority calc.

### §3.9 Rupture (immediate break, bypassing strain accumulation)

| Trigger | Affected edges | Consequence |
|---------|----------------|-------------|
| Public betrayal (sworn-bond partner publicly siding with feud-target) | Sworn-bond | Immediate transition to feud at strength 2 |
| Vassal participates in armed action against liege | Liege-vassal | Immediate break + Casus Belli generated for liege's faction against vassal |
| Patron *raccomandazione* publicly retracted (faction-political reversal) | Patronage | Immediate break + Stature damage doubled per §3.8 |
| FR Dissolution targeting a sworn-bond partner | Sworn-bond | Immediate edge-mutation to "memory-bond" (loss-state; surviving partner gains permanent +1 to Honor Conviction; +1 Coherence damage) |
| Conviction Crisis on Honor (3+ Honor Scars per `conviction_track_v1 §2`) | All sworn-bonds and liege-vassal edges held by crisis NPC | All take +2 strain immediate; if any reach capacity, break per §3.8 |

The last row is particularly load-bearing: an NPC entering Honor-crisis can cascade-break their entire honor-network, which propagates to faction-Cascade per B1.3.

---

## §4 Edge Formation

Edges form through specified scenarios. Most edges are authored at scenario init (canonical at scenario start); some form in-play through specified mechanics.

### §4.1 Sworn-bond formation

**Authored:** by scenario design; canonical NPC roster at PP-X2 (B2 deferred follow-up).

**In-play:** triggered scene appears on Scene Slate at Priority 3 when both NPCs:
- Have shared a non-adversarial scene in the last 2 seasons.
- Have Disposition with each other ≥ +3 (NPC-NPC Disposition derived; see §4.7).
- Share at least one primary Conviction (per `conviction_taxonomy §4.1`).
- Have Self-Other orientation in the same hemisphere (both negative or both ≤ +0.2).

**Resolution:** the scene presents an opportunity for mutual oath. Spirit pool (Spirit_A + Spirit_B) vs TN 8, Ob 2.

| Degree | Result |
|--------|--------|
| Overwhelming (3+ net) | Strength 2 sworn-bond (tested in shared adversity if scenario context) |
| Success (2 net) | Strength 1 sworn-bond |
| Partial (1 net) | No bond. Disposition retained. Cooldown: 2 seasons. |
| Failure (0 net) | No bond. Disposition −1 each. Cooldown: 4 seasons. Asymmetric rivalry possible (one side reads rejection as slight). |

### §4.2 Liege-vassal formation

**Authored:** institutional positions canonized at scenario init via faction rank ladders (`faction_politics §1`). Standing assignment within a faction = liege-vassal edge to faction leader at strength matching rank.

**In-play (institutional):** rank promotion within faction creates or strengthens liege-vassal edge to faction leader. Typically authored by faction AI per `npc_behavior §8`.

**In-play (independent):** Player faction emergence (`settlement_layer §6.2 Stage 2→3`) creates liege-vassal edges from recruited officers to PC-as-faction-head. Conditions per Stage 2→3: settlement controlled, NPC officer accepted Stature-appropriate Duty.

### §4.3 Kinship formation

**Authored:** entirely. Kinship cannot form in-play except via marriage (which is its own scenario mechanic). Kinship is canonical at scenario init via NPC sheets specifying parents, spouse, siblings.

**Marriage as kinship-formation:** the marriage scene (deferred to a future PP — marriage_v30 not yet in canon) creates a strength-3 kinship edge. Children born of marriage create strength-3 parent→child asymmetric kinship.

### §4.4 Patronage formation

**Authored:** scenario init may specify patron-client edges across NPC roster.

**In-play (NPC-NPC):** any time NPC-A extends a tangible benefit to NPC-B (gold, position, public endorsement) and NPC-B is at Standing-3 or below relative to NPC-A's Standing, a patronage edge forms at strength 1. Subsequent benefits compound to strength 2 or 3 per `§2.4` strength definitions.

**In-play (PC patronage):** the player can extend patronage to recruited NPCs (per `settlement_layer §6.2` faction emergence). PC-as-patron creates a hybrid edge: NPC tracks PC patronage as both a Knot (PC-NPC) and a patron-tie (NPC-patron). The two are co-existent per §3.3.

### §4.5 Rivalry formation

**Authored:** scenario init may specify canonical rivalries (Cesare ↔ Almud succession; Lorenzo ↔ Cesare alternative-succession-pair).

**In-play:** auto-forms when:
- Two NPCs publicly compete for the same office, position, or succession line (auto-detected by faction-state).
- An NPC publicly thwarts another's primary objective (auto-detected by Decision-Fork outcome involving rival).
- Mutual antagonism in a single Social Contest where both invoke opposing Convictions (auto-detected at contest resolution).

Auto-formed rivalries start at strength 1.

### §4.6 Reconciliation (rivalry / feud → sworn-bond or no-edge)

**Reconciliation scene** appears on Scene Slate at Priority 4 when both NPCs:
- Have rivalry strength ≤ 2 (strength 3 cannot reconcile without intermediary — typically a Cathedral or Seat venue).
- Have not had adversarial action in the last 4+ seasons.
- Share a sustained Conviction-aligned event in working memory (e.g., both took the same side in a faction crisis).

**Resolution:** Spirit pool (Spirit_A + Spirit_B) vs TN 9, Ob 3. Higher difficulty than sworn-bond formation because reconciliation requires rebuilding eroded ground.

| Degree | Result |
|--------|--------|
| Overwhelming (3+) | Rivalry resolves to sworn-bond strength 1; both gain Disposition +2 each. |
| Success (2) | Rivalry resolves to no-edge; both gain Disposition +1. |
| Partial (1) | Rivalry strength −1; cooldown 4 seasons. |
| Failure (0) | Rivalry strength +1 (reconciliation attempt failed publicly = humiliation). |

Feud reconciliation (per §2.6) requires the formal blood-price ceremony, not the §4.6 mechanic.

### §4.7 NPC-NPC Disposition (derived)

NPC-NPC Disposition is derived from edge state, not tracked separately. The derivation:

```
NPC_A.disposition_toward(NPC_B) = base + 
    sum(edge.strength_signed for edge in edges between A,B)
    - (strain_pressure: -1 if any edge strain > capacity * 0.5)
```

Where `edge.strength_signed`:
- Sworn-bond / liege-vassal / kinship / patronage: +strength
- Rivalry / feud: −strength

Base is +0 for NPCs with no shared edges (acquaintance neutral). Bounded by −5..+5 per existing Disposition framework.

This means Disposition is a **reading** of the edge graph, not separately authored. Authoring an edge implicitly sets Disposition.

---

## §5 Multi-Edge Composition

A pair of NPCs may have multiple edges. Composition rules:

### §5.1 Allowed combinations

| Edge A | Edge B | Allowed? | Notes |
|--------|--------|----------|-------|
| Sworn-bond | Liege-vassal | YES | Common — Halvar↔Lions'-Table-leader exemplar |
| Sworn-bond | Kinship | YES | Common — kin-bonds reinforced by oath |
| Sworn-bond | Patronage | YES | Sworn between patron and client; reinforces |
| Sworn-bond | Rivalry | NO | Mutually exclusive — cannot be sworn AND rival simultaneously. Transition: if rivalry forms while sworn-bond exists, sworn-bond ruptures (per §3.9 public betrayal rule) |
| Sworn-bond | Feud | NO | Same exclusion — feud explicitly negates sworn-bond |
| Liege-vassal | Kinship | YES | Father-vassal-of-son was historically common in Renaissance courts |
| Liege-vassal | Rivalry | YES | Vassal can be liege's rival for some external position; produces high strain accrual |
| Liege-vassal | Feud | YES | Inherited feuds can persist within liege-vassal hierarchies; extreme strain |
| Kinship | Rivalry | YES | Brother-rivalry is canonical (Cesare ↔ Lorenzo arc context) |
| Kinship | Feud | YES | Internal-clan-feud; kin-feud is more severe than non-kin-feud (mutual betrayal of Identity) |
| Kinship | Patronage | YES | Patron-uncle, patron-aunt patterns common |
| Patronage | Rivalry | YES | Patrons can have rival clients; clients can have rival patrons |
| Rivalry | Feud | NO | Not coexistent — feud is a stable terminus of rivalry, not parallel state |

### §5.2 Strain interaction across multiple edges

When multiple edges exist between the same pair:
- Strain accrues independently on each edge.
- Strain on one edge **spills over** to other edges of the same valence (positive→positive, negative→negative) at half rate, rounded up: a +2 strain event on a sworn-bond between A,B who also have liege-vassal will accrue +2 on sworn-bond AND +1 on liege-vassal.
- Strain *across valences* (positive→negative or vice versa) does NOT spill over: a strained kinship doesn't propagate to a held rivalry.

### §5.3 Net relational valence

For Decision Fork inputs, the **net relational valence** of NPC A toward NPC B:
```
net = sum(edge.strength_signed across all edges)
```
where positive valence promotes cooperation in Decision Forks, negative valence promotes obstruction. Net valence is independent of strain (strain affects break risk; valence affects current behavior).

---

## §6 Settlement Coupling [Implemented PP-725 / B1.4]

Edges have **spatial cost**: cross-territory edges accrue background strain at higher rate than intra-territory edges, modeling the Renaissance reality that long-distance ties (couriers, separation, divergent local pressures) are harder to maintain.

**Scaling factor by geographic distance** (in `valoria_geography_v30.yaml :: settlement_adjacency:` graph hops):
- Same settlement: ×1.0
- Adjacent settlements (1 hop): ×1.0
- 2-hop: ×1.25
- 3-hop: ×1.5
- 4+ hop: ×2.0 (considered "remote tie")

Thread-Witnessed edges (per `valoria_geography :: settlement_adjacency:` `thread_witnessed` type) bypass distance-strain: substrate-inseparability per A1/C1 operates outside ordinary geographic costs, but requires both NPCs to have TS ≥ 30 to access the substrate-connection (the Knot Thread-contact prerequisite per `fieldwork §5.6a` generalized to NPC-NPC ties).

### §6.1 NPC residence canon

Distance computation requires knowing each NPC's canonical settlement. PP-725 defines the derivation rule (no per-NPC field required for most NPCs; explicit override available for edge cases).

**Derivation order** (first applicable rule wins):
1. **Explicit override**: an NPC sheet (per `character_canon §2 How to Read an NPC Sheet`) may include an optional `residence: S-XXX` field. If present, this is canonical.
2. **Governor assignment**: per `settlement_layer §3.2`, Standing 3+ NPCs assigned as Governor reside at the governed settlement.
3. **Faction-leader headquarters** (per PP-726 corrected granularity — settlements proper, with district contexts noted): faction leaders without explicit governance reside at the canonical faction-headquarters settlement:
   - Crown leader (Almud, current monarch) → S-001 Valorsplatz (Palace district; Lion's Table HQ)
   - Hafenmark Duke (Baralta) → S-018 Gransol (Parliament district; Baralta's court on the lake)
   - Church Confessor (Cardinal of Faith) → S-036 Himmelenger (Cathedral district; sovereign Church city-state)
   - Varfell Duke (Vaynard) → S-031 Sigurdshelm (the keep itself; Private Collection housed here)
   - Löwenritter Master → S-014 Ehrenfeld (Citadel and Barracks districts; fortress-city HQ gating crownlands from west and north)
   - RM Spokesperson → S-026 Grauwald (Lodge sub-feature; covert RM meeting site within Grauwald)
   - Wardens lead → no settlement (Warden operations are based at Askeheim Ruins, an unincorporated Calamity-zone observation feature; the closest settlement contact-point is S-012 Stillhelm via the Watch outpost and the canonical thread-witnessed network edge to the Ruins)
4. **Faction-membership default**: Standing 0–2 NPCs reside at their faction-headquarters settlement (rule 3) unless a `character_canon` prose excerpt names a specific scene-location as their habitual setting.

NPC residence may change during play through faction reassignment (§6.4), Governor reassignment per `settlement_layer §3.2`, or canonical narrative events (exile, pilgrimage, taking a new posting).

### §6.2 Hop-distance algorithm

The graph distance between two NPCs is computed by breadth-first search on the canonical `settlement_adjacency:` block:

```
hop_distance(NPC-A, NPC-B):
    if A.residence == B.residence: return 0
    perform BFS on settlement_adjacency graph
    edges of type {road, river, mountain_pass, coastal, gate} count as 1 hop
    edges of type thread_witnessed contribute 0 hops IFF both A.TS ≥ 30 AND B.TS ≥ 30
    if no path exists: return ∞ (treated as ×2.0 remote-tie strain scaling)
```

The algorithm runs on the `army-traversable subgraph` by default (excluding `thread_witnessed`). Thread-Witnessed bypass applies only when both endpoint NPCs have the Thread-contact capacity (TS ≥ 30, matching the Knot formation prerequisite). For NPCs below the TS threshold, the Thread-Witnessed edges are inert at the relational-strain layer.

Implementation note (`§9.1 Storage`): hop-distance is computed at Accounting cadence per (NPC-pair, edge) tuple, not per turn. Cached values are invalidated when (a) either NPC's residence changes, (b) the settlement_adjacency graph itself is modified by canonical authoring (rare; would be a Class B geography PP), or (c) either NPC crosses the TS 30 threshold (Thread-Witnessed bypass eligibility changes).

### §6.3 Which §3.2 strain triggers scale by distance

Not all strain triggers are geographically meaningful. PP-725 classifies the §3.2 triggers into three buckets:

| Trigger Category | Distance Scaling | Reason |
|---|---|---|
| **Universal triggers** (public contradiction, Conviction-crisis polarization, witnessed Thread operation valence mismatch) | **Scales** (multiplied by §6.0 factor) | Background relational pressure from divergent contexts; distance amplifies the divergence (different patrons, different witnessed events, different local Conviction-pressure). |
| **Kinship absence** (§3.2 kinship: NPCs in different territories with no inter-territory edge for 2+ consecutive seasons) | **Already geographic** — distance scaling does NOT compound | This trigger is itself a distance encoding; multiplying would double-count. Keep as authored. |
| **Patronage attribution drift** (client publicly attributed success to a source other than the patron) | **Scales** | Distance amplifies — a distant patron is more easily eclipsed in the client's local political ecosystem. |
| **Direct hostile action triggers** (sworn-bond explicit violation, vassal disobeys explicit order, feud direct violence, debt invocation) | **Does NOT scale** | Events are bound to where they occurred; the strain is bound to the event, not background ambient pressure. |
| **FR Dissolution, assassination attempts, death-of-partner** (rupture triggers per §3.9) | **Does NOT scale** | Rupture triggers bypass strain accumulation entirely (§3.9). |

The scaling factor is applied at strain-add time: when a scalable trigger fires, the strain delta is multiplied by the §6.0 scaling factor for the (NPC-A, NPC-B) hop-distance, rounded to the nearest integer (with ½ rounding up). Example: a +1 strain trigger between NPCs at 3-hop distance becomes +1 × 1.5 = +2 strain (rounded up from 1.5 by the round-half-up convention).

### §6.4 Officer reassignment

When an NPC's residence changes via faction reassignment or Governor posting:

1. **At reassignment scene resolution** (Class B scene per `faction_canon §3.2` or `settlement_layer §3.2` Governor Assignment): the NPC's `residence` field updates.
2. **Edge-strain shock** (one-time, at next Accounting):
   - Edges with NPCs whose hop-distance to the moved NPC *increased* by 1+ hop tier (e.g., crossing from 1-hop to 2-hop, or 3-hop to 4+-hop): **+1 strain shock** on the affected edge. Models the "left behind" emotional cost of separation.
   - Edges with NPCs whose hop-distance *decreased* by 1+ hop tier: **−1 strain reverse-shock** on the affected edge if strain > 0 (floor at 0). Models proximity-rekindling.
3. **No retroactive recomputation** of accumulated strain — only the shock applies. The new distance scaling factor takes effect for *future* strain accruals from §6.3 scalable triggers.

This rule formalizes the hook clause from the original §6: "Officer assignments to distant settlements that strain a sworn-bond: bond-partner left behind in original settlement accrues strain per the scaling above."

### §6.5 Worked examples (sanity check, retuned PP-726)

Using canonical NPC residences per §6.1 derivation and the corrected PP-726 settlement adjacency (supersedes PP-723's wrong-granularity graph):

*Hop distances computed on the PP-726 corrected-granularity 55-edge graph (`valoria_geography_v30.yaml :: settlement_adjacency:`).*

| NPC-A | Settlement | NPC-B | Settlement | Hop Distance | Scaling | Strain Trigger Example |
|---|---|---|---|---:|---:|---|
| Almud | S-001 Valorsplatz | Cesare | S-001 Valorsplatz | 0 | ×1.0 | Their rivalry strain accrues at baseline rate (same-court succession competitors residing in the Palace district). |
| Almud | S-001 Valorsplatz | Yrsa Vossen (RM Spokesperson) | S-026 Grauwald | 3 (Valorsplatz→Ehrenfeld→Grauwald, with Lodge as Yrsa's covert sub-feature anchor) | ×1.5 | Any patronage/sworn-bond/debt edge between Crown and RM scales by 1.5 on universal triggers — long-distance political ties erode 50% faster. |
| Cardinal Reichard | S-036 Himmelenger | Vaynard | S-031 Sigurdshelm | 5 (road via Himmelenger→Ehrenfeld→Grauwald→Sigurdshelm) | ×2.0 | Church-Varfell ties along the Solmund philosophical chain pay maximum geographic-strain on universal triggers; the Sigurdshelm-Seminary thread-witnessed connection at the sub-feature layer (Vaynard's Private Collection ↔ Himmelenger Seminary district) provides Thread-mediated bypass if both have TS ≥ 30, reducing effective distance to 0 for those substrate-grounded ties. |
| Baralta | S-018 Gransol | Schoenland Governor | S-037 Schoenland | ≥6 (sea-mediated; Gransol→Rendstad→Grauwald→Ehrenfeld→Valorsplatz→Schoenland, with sea-leg at the end) | ×2.0 | Hafenmark-Schoenland trade-partnership patronage strain scales by 2.0 — Hafenmark routes through Crown territory to reach Schoenland because Gransol is on a lake (Switzerland-like landlocked province), not the sea. ED-055 naval-scope expansion would shorten this distance dramatically. |
| Almud | S-001 Valorsplatz | Cardinal Reichard | S-036 Himmelenger | 3 (Valorsplatz→Ehrenfeld→Nordhain→Himmelenger via the north-gate route) | ×1.5 | Crown-Church ties around Mandate cooperation accrue strain 50% faster than intra-court ties, reflecting the inter-faction friction structurally encoded in the geography. |
| Stillhelm Watch (Warden contact) | S-012 Stillhelm | Askeheim Ruins (Warden operations) | n/a (unincorporated; sub-feature in Askeheim wilderness) | n/a — Wardens have no settlement at Askeheim; the operational tie to the Ruins is a sub-feature relationship (Stillhelm's Watch outpost faces the Ruins via thread-witnessed Warden network) | ×1.0 (Thread-Witnessed bypass at sub-feature layer) | The Warden network's substrate-inseparability keeps Calamity-monitoring ties at zero-distance penalty — but per PP-726, this is now correctly modeled as a thread-witnessed sub-feature relationship, not a settlement-edge in the canonical graph. |

Note on remote ties: per PP-726 corrected graph, Schoenland is foreign-exempt with degree 1 (single sea-edge to Valorsplatz). Hafenmark-Schoenland ties route through the Crown's port at Valorsplatz, paying maximum geographic-strain (×2.0). This compositional consequence reinforces ED-055 naval-scope expansion (improvement_avenues A3) as P1: once naval routes are mechanized, Schoenland gains additional sea-edges (most plausibly Schoenland↔Sundfjord on Varfell's coast, or Schoenland↔Halvardshelm-coast), shortening Hafenmark's effective distance and lifting Schoenland out of the foreign-exempt single-edge condition.

### §6.6 Integration with §3.2 (revised strain accrual)

The strain-add formula from §3.2 is augmented:

```
strain_add(edge, trigger):
    base_delta = trigger.strain_value          # from §3.2 type-specific table
    if trigger.category in {universal, patronage_attribution_drift}:
        delta = round_half_up(base_delta × distance_scaling(edge))
    else:  # direct hostile, kinship-absence (already geographic), rupture-bypass
        delta = base_delta
    edge.strain += delta
    if edge.strain >= edge.capacity:
        schedule_break_at_next_Accounting(edge)
```

This composes with §3.7 strain decay (decay is unchanged by distance; sustained healthy interaction reduces strain at the same rate regardless of distance).

---


## §7 Defection Cascade [B1.2 — BUILT 2026-06-09, ED-1000; sim-tuning pending]

When a sworn-bond or liege-vassal edge breaks (§3.8) or ruptures (§3.9), the break can **cascade** along the relational graph: edges shared with the broken-edge parties strain or sever in turn, producing the ROTK-signature multi-officer defection. The cascade is a positive feedback loop, held bounded by three dampers plus a hard cap (loop-safety L-DEFECT; resolution-diagnostic Lesson 5 — no loop both undamped and unbounded).

**Trigger.** A sworn-bond or liege-vassal edge breaks at strain capacity (§3.8) or ruptures (§3.9).

**Tier-1 (immediate, at break).** Every edge between either broken-edge party and a third NPC accrues defection-strain **attenuated by hop-distance** (§6.2): `+1` at hop 0–1, **halved per additional hop** (`+0.5^(hop−1)`, floored at +0.1; ∞-distance edges unaffected). The ½-per-hop attenuation is the spatial damper — total tier-1 strain injected is bounded by a geometric sum regardless of graph size.

**Fragility-multiplier (the loop gain).** Each *cascade-produced* defection (a break caused by the cascade, not the originating break) raises the faction's **Fragility** by +1 (**cap +3**). Fragility lowers the Decision-Fork sever threshold for that faction's remaining members: the tier-2 maintain-vs-sever fork is taken at `sever DC − Fragility`. Fragility decays **−1 per season at Accounting** with no new cascade break (reuses the §3.7 strain-decay cadence). This is the sole positive-gain term; capped and decaying, it cannot compound unbounded.

**Tier-2 (next Accounting).** NPCs whose edge was tier-1-strained take the Decision Fork (maintain vs sever) at `DC − Fragility`. A sever breaks the edge (§3.8 consequences) and propagates tier-1 from that node at the **next** hop ring — reach marches outward at most one ring per Accounting, never instantaneously.

**Suppression-brake (player damper).** The holding faction may spend its **Suppress** action against the cascade: each Suppress applies **−1 to the tier-2 sever check** for one targeted node-cluster this season (bounded; mirrors insurgency Stage-3 suppression, ED-853). Suppress is the player's explicit lever to arrest a cascade, trading action economy for cohesion.

**Tier-3+ (rare cap).** A tier-3 ring fires only if tier-2 produced **3+ further breaks**; beyond tier-3 the cascade cannot self-propagate (hard cap). With finite membership and hop-attenuation, total cascade depth is bounded.

**Loop-safety verdict.** Gain: Fragility (+1/break, cap +3, −1/s decay). Dampers: hop-attenuation (½/hop), Fragility decay (−1/s), Suppress (−1/check). Bound: tier-3 cap + finite membership. Net per-cycle gain < 1 ⇒ damped; reach and depth finite ⇒ bounded ⇒ **passes Lesson 5**. `[NEEDS TESTING — SIM-DEFECT (Lane C): the magnitudes (½/hop, Fragility +1/cap +3, sever-DC coupling, tier-3 trigger = 3, Suppress −1) are illustrative; the per-cycle-gain bound is a design argument, not yet sim-measured. Confirm termination and tune magnitudes before treating them as load-bearing.]`

**Worked target case.** The Niflhel-strike scar (`faction_politics §2.6`): Niflhel dissolution now produces a tier-laddered defection cascade across officers with sworn-bonds or patron-ties to Niflhel-aligned figures — hop-attenuated from the dissolution locus, brakeable by a surviving holder's Suppress — replacing the prior clean-dissolution placeholder.

## §8 Faction-Cascade Integration [B1.3 — BUILT 2026-06-09, ED-1000; sim-tuning pending]

After the relational cascade settles (no further tier propagation this Accounting), faction-aggregate state recomputes **once**, not per-break (avoids intra-season thrash):

- **Officer loss → faction stat.** Each severed liege-vassal or sworn-bond edge that removes an officer reduces that faction's derived strength inputs at Accounting (Military / Influence via the §6.4 officer-reassignment path), feeding the existing faction-collapse loop (FSS-LOOP-1/2), already bounded in canon.
- **Fragility → faction Conviction.** Residual Fragility (§7) applies a one-Accounting −1 to the faction's Conviction-hold check (a shaken faction), clearing as Fragility decays. No new faction stat is introduced.
- **No double-count.** The cascade writes through *relational edges and officer reassignment only*; faction L/PS/Mandate remain settlement-derived (LPS-2e) and are not written by the cascade — it changes *who holds*, not the settlement substrate.
- **Termination.** Integration runs once per Accounting after §7 settles; with §7 bounded, faction-cascade integration is bounded by construction. `[NEEDS TESTING — SIM-DEFECT: confirm officer-loss feeding FSS-LOOP does not stack with §7 Fragility to exceed the collapse-loop's established bound.]`

## §9 Engine Implementation

### §9.1 Storage

```yaml
# canon/relational_edges_v30.yaml (new file, B2 will populate)
edges:
  - id: E-001
    type: sworn-bond
    from: NPC-Almud
    to:   NPC-Halvar-Brandt
    strength: 2
    formed: scenario_init
    formed_by: "Lion's Table service shared in Altonian border patrol seasons -3 to 0"
    strain: 0
    notes: "Canonical; surfaced in npc_roster §6 Halvar Brandt Lion's Table position"
  - id: E-002
    type: rivalry
    from: NPC-Cesare
    to:   NPC-Almud
    strength: 2
    formed: scenario_init
    formed_by: "Crown succession competition; canonical per migration_roster §2.1"
    strain: 0
    note: "Symmetric — Almud reciprocates"
  - id: E-003  # the symmetric counterpart — rivalry edge stored in both directions for clarity
    type: rivalry
    from: NPC-Almud
    to:   NPC-Cesare
    strength: 2
    formed: scenario_init
    formed_by: "(see E-002)"
    strain: 0
```

For symmetric edges, store both directions for cleaner lookups; the engine treats the dyad as one edge for capacity/strain accounting (the strain field is mirrored on read).

### §9.2 Per-NPC index

`character_canon` per-NPC sheets gain a new field `relational_edges:` listing edge IDs. This is regenerated on edge add/remove; not authored separately.

### §9.3 Decision Fork hook

`npc_behavior §6 Decision Fork` consumes net relational valence (`§5.3`) toward potential subjects. A faction action targeting NPC-B, evaluated by NPC-A, applies:
- Net positive valence: increases probability of A choosing the cooperation/help branch.
- Net negative valence: increases probability of A choosing the obstruction branch.
- Strain pressure: NPCs near edge-break threshold weight Solidarity Resonant Style appeals more strongly (about-to-break bonds amplify).

### §9.4 UI surfacing

- NPC sheets show held edges with type, strength, current strain.
- Settlement view shows officer-officer edges visible at that settlement.
- Faction view shows faction-internal edge density (sworn-bond clusters, rivalry pairs).
- Dynamic edge events (formation, strain, break, rupture) generate Scene Slate entries at appropriate Priority.

---

## §10 Vetting Block (per PP-674 framework)

```yaml
vetting:
  class: A
  necessity: pass
  omega: pass
  mu: ["Μ-β", "Μ-δ"]                 # primary modes: agent composition, cross-scale
  mu_secondary_preserved: ["Μ-α", "Μ-γ"]
  m_ratings:
    M-1: "+"   # extends — relational strain is a continuous-pressure mechanism between NPCs (paralleling Conviction-Scar at character level); each edge is a strain-bearing axis
    M-2: "○"   # geography hooks specified in §6 but full mechanic deferred to B1.4; currently personal-scale
    M-3: "+"   # extends — relational edges are substrate-real per §1 statement; rendering of authority/oath/kinship/feud ARE substrate configurations at the dyadic level, not flavor-tags
    M-4: "+"   # extends — institutional substrate-postures (Faction-aggregate Conviction per PP-686) gain centrality-weighted contribution from relational graph (B1.3 hook); Church/Crown/Varfell faction-character will differentiate by relational topology, not just member-Conviction average
    M-5: "+"   # extends — cross-scale composition: relational events at personal scale (sworn-bond break) propagate through B1.3 hooks to faction-Cascade axis-shifts; through B1.2 hooks to multi-NPC defection cascades; through B1.4 hooks to settlement-distance strain
    M-6: "+"   # extends — Decision Fork now consumes relational valence per §9.3; choice for NPCs becomes per-axis (faction-aligned vs bond-aligned vs rival-disadvantaging vs kin-loyal); the forced-choice space grows substantially with relational state present
    M-7: "✓"   # KOEI ROTK + CK3 borrowing canonized in settlement_layer §Precedent and settlement_adjacency canon-compliance — this doc fulfills the borrowing's relational substrate without altering its operational deployment
    M-8: "○"   # access-vertical-position-gating is upstream (witness layer); relational-graph engages it indirectly via Decision Fork inputs but doesn't extend or violate the access pattern
    M-9: "○"   # ontological-inversion-of-clinical-phenomenology is the Conviction Scar / moral-injury frame; relational graph composes with that (Honor-axis Scars cascade per §3.9) but doesn't introduce a new clinical-borrowing instance
    M-10: "✓"  # environment-as-constitutive-medium preserved; relational edges have geographic distance cost via §6 hook (B1.4 deferred) but the environment-constitution at settlement scale (PP-723) remains unaltered
    M-11: "+"  # extends — voluntary/involuntary capacity duality applies to edges: PCs can cultivate sworn-bonds (voluntary), inherit feuds (involuntary), choose to reconcile or break (voluntary), have edges break under crisis (involuntary). The same structural capacity (relational binding) yields opposite valences depending on agency
  m_summary: "6 + · 2 ✓ · 3 ○ · 0 − — pass per throughlines_meta §8.2 (zero violations). Genuine extensions on M-1/M-3/M-4/M-5/M-6/M-11 (continuous strain pressure; substrate-grounded edges; institutional differentiation by topology; cross-scale propagation through hooks; per-axis Decision Fork; voluntary-involuntary edge duality). M-7/M-10 satisfied (faithful to ROTK/CK3 borrowing and environment-constitution). M-2/M-8/M-9 ○ scope-mismatch — geography hook deferred to B1.4, access/clinical-borrowing patterns engage indirectly without extension."
  t_touches:
    extends: ["T-23", "T-24", "T-25", "T-15"]   # NPC arc emergence, convergence-as-crisis, generational arc, player progression — all carry relational-graph propagation
    preserves: ["T-08", "T-09", "T-11", "T-15a", "T-15b", "T-15c", "T-14", "T-22", "T-17"]
    breaks: []
  q: pass
```

(Detailed Q-robust / Q-smooth / Q-elegant evaluation in §11 below.)

---

## §11 Quality Evaluation (per throughlines_meta §5)

### Q-robust (positive feedback loop)
**Three viable player approaches** to any relational situation the framework governs:
1. *Cultivate*: form sworn-bonds with NPCs whose Convictions align; avoid strain accrual; recover-via-decay.
2. *Exploit*: identify rival-feud structure and engineer adversarial-action sequences to escalate rivalries to feuds, weakening the target faction's relational topology.
3. *Reconcile*: find sustained-Conviction-aligned moments to attempt rivalry resolution scenes; high-difficulty but high-payoff (Rivalry → Sworn-bond is a strong faction-political move).

**Visible, traceable world-state change.** Edge state on NPC sheets; relational view in settlement and faction overlays; Scene Slate entries on edge events. Every formation, strain accrual, break, rupture is engine-readable and player-visible.

**Mechanic fires without player action.** NPC-NPC edges accrue strain via NPC-driven scenes (Faction AI executes Domain Actions; vassal-liege edges strain when faction-state misalignments fire; rivalries auto-form per §4.5). The framework produces consequential events when the player is absent.

**Dramatic legibility** (one-sentence test): For any Cardinal-Inquisitor-rivalry-escalation scenario:
- *Whose position is at risk:* Inquisitor's Authority within Tribunal hierarchy.
- *What each named actor wants:* Cardinal — preserve sovereign-ecclesiastical balance; Inquisitor — assert procedural orthodoxy against perceived softness; Cardinal-supporter — protect patron's standing.
- *What happens if no one acts next season:* rivalry strength escalates per §3.5 trigger from latest adversarial event; Cardinal-supporter's patron-tie to Cardinal accrues spillover strain per §5.2; faction-Cascade Authority axis erodes per B1.3 hook.

All readable in one sentence each.

### Q-smooth (composes without special-casing)
- **Methodology matches existing systems.** Strain mechanics mirror Knot lifecycle (`fieldwork §5.6b`); per-edge state machine mirrors Conviction Scar accumulation (`conviction_track_v1 §2`); edge formation scenes consume Spirit pool resolution (`fieldwork §5.6a`). No new resolution machinery.
- **Scale-transition behavior specified.** Personal-scale edges feed faction-scale Cascade (B1.3 hook); settlement-scale geographic distance modulates strain (B1.4 hook). Both hooks specified for future authoring.
- **Temporal behavior specified.** Strain accrual per-event; strain decay per-Accounting-with-conditions; cooldowns specified for failed scenes (§4.1, §4.6). All timing rules align with existing Accounting cadence.

### Q-elegant (depth from rule simplicity)
- **Core rule restatable after one reading:** "NPCs hold typed edges (sworn-bond, liege-vassal, kinship, patronage, rivalry, feud) with strain that accumulates from event triggers and decays under sustained alignment; capacity exceeded → break with consequences. Multi-edge composition allowed where valence permits; rivalry/feud and kinship/feud are persistent state without strain-break."
- **Second-order consequence predictable:** Honor-Scar crisis (per `conviction_track §2`) + many sworn-bond edges → cascade-break across the honor-network. This composes the personal-scale Conviction-crisis mechanic with the relational-graph cleanly.
- **External dependencies enumerated:** PP-684 (Conviction taxonomy), PP-685 (Migration roster), PP-686 (Cascade math — for B1.3 hook), PP-718 (per-Conviction Scar — for §3.9 Honor-crisis cascade), PP-723 (settlement adjacency — for §6 distance-strain hook), `fieldwork §5.6b` (Knot lifecycle template), `npc_behavior §1.3` (Resonant Style coupling), `social_contest §6.1` (Wager / Knot interaction). All in the §0 Companions block.

**Q verdict: pass.**

---

## §12 Open Items

- **B1.2 defection cascade resolution** — full mechanics deferred (§7 hook only).
- **B1.3 faction-Cascade integration** — full centrality-weighted Cascade math deferred (§8 hook only).
- **B1.4 settlement-coupling rules** — distance-strain scaling factors specified but not stress-tested (§6 hook).
- **B2 named-NPC instantiation** — 13+ named NPCs in `npc_roster_v30` need their canonical edges authored. Class D content addition; deferred follow-up.
- **B3 Loyalty/Ambition state** — separate axis (deferred from improvement_avenues_2026-05-10) that interacts with this framework; see §0 of that register.
- **Marriage mechanic** — kinship formation via marriage requires `marriage_v30.md` future PP. Currently kinship edges are author-only.
- **Edge-storage file** — `canon/relational_edges_v30.yaml` not yet created; will be authored at B2 instantiation.

---

## §13 Decision Log

| Decision | Resolution | Rationale |
|----------|------------|-----------|
| Six edge types vs broader taxonomy | Six | Each maps to a distinct Renaissance dynamic with period precedent; further types (e.g., debt, oath-of-service) collapse into existing types or are sub-states. Preserves Q-elegant. |
| Knot lifecycle template vs novel state machine | Knot lifecycle | Architectural consistency with `fieldwork §5.6b`; players already know Knot mechanics; reduces cognitive load. |
| Strain capacity 3/5/7 (sworn-bond, liege-vassal) vs 4/7 (Knot) | 3/5/7 | Three strength tiers needed for edge-strength differentiation; capacity scales linearly. |
| Kinship as no-break-by-strain | Kept | Kinship is structural; modeling it as breakable-by-strain misrepresents Renaissance kin-politics. Severance requires institutional act. |
| Feud auto-transmission along strong kinship | Kept | This is the load-bearing ROTK-style mechanic for emergent multigenerational narrative; without it, feuds dissipate at each death rather than driving the campaign. |
| Rivalry/feud as escalation-track vs strain-track | Escalation | Rivalries don't "fail" by accumulating bad blood; they intensify or de-intensify. Modeling them as strain-toward-break would force the wrong narrative shape. |
| NPC-NPC Disposition derived vs separately tracked | Derived | Storing both edges + Disposition risks divergence; deriving from edges keeps the substrate single-sourced (Q-smooth principle). |
| Relational edges file (separate) vs character_canon-embedded | Separate file | Edges are graph-state, not per-NPC state; storing in character_canon would require N/2 duplication for symmetric edges. Separate file with per-NPC index field. |
| Class A vs Class B | Class A | New substrate (named edge types not previously canonical), new state machine, new stat surface. Class A. |

---

**End spec. PROVISIONAL pending ratification. B1.2/B1.3/B1.4/B2 are deferred follow-up PPs.**
