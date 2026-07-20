# Game-Precedent Findings (v1) — distilled by Valoria gap

## Status: research provenance (FILED) — 2026-07-13 · feeds `precedent_fix_catalog_v1.md`

Distilled from web-grounded cross-scale-mechanism研究 passes (CK3/CK2, EU4, Imperator, Stellaris, Old
World, KOEI ROTK, Democracy 3/4, Frostpunk 1/2, Tropico, Dwarf Fortress, RimWorld, Manor Lords). Each
entry: **game · mechanism · REAL / SURFACE verdict · what to lift.** "REAL" = a genuine transferable
cross-scale mechanism; "SURFACE" = shared vocabulary only. Method caveat carried from every agent:
WebFetch was proxy-blocked, so figures are WebSearch-synthesized from official wikis/dev-diaries,
cross-checked across ≥2 sources; treat exact constants as "web-consensus current," not hand-verified.

---

### G1 · Inert L/PS consent-gate — "does an imposed governance type stick?"
- **CK3 Administrative government (Roads to Power)** — *uniform Imperial-Bureaucracy law broadcast to all governors, but each governor's local skill/Efficiency attenuates how much actually "sticks" as yield.* **REAL — the single best precedent for the whole cascade "does it stick" gap.** Lift: **policy is uniform top-down; realized effect is local-consent-attenuated.**
- **CK3 Legitimacy (1.12)** — per-observer *Legitimacy Expectation* computed from observer weight (powerful vassals demand more), compared to one actual value, with a **non-linear gap penalty** (1 level short reads as 2) → concrete downstream (opinion, faction-join, action success). **REAL.** Lift: expectation-vs-actual **gap** function, non-linear.
- **EU4 Estate Loyalty** — 0–100, three bands (disloyal<30 / neutral / loyal>60), drifts to an equilibrium; disloyal+high-influence+no-war → estate-coup disaster. **REAL.** Lift: band-bucketed consent stat with drift-to-equilibrium + AND-gated revolt.
- **EU4 local autonomy + territory/state floors** — a per-province stat that throttles upward yield ~1:1 AND has a *structural floor* set by core-status. **REAL.** Lift: **low-integration settlements should be discounted in aggregation, not only low-L/PS ones** (a structural precondition gating whether governance can take hold).
- **CK3 two-track opinion** — character/vassal opinion (noble consent) is a *separate axis* from county Popular Opinion (commoner consent, fed by culture/faith match, drives Control + peasant revolt). **REAL.** Lift: keep noble-consent (Standing) and popular-consent (L/PS) as distinct variables with distinct feeders/consequences.
- **Manor Lords Approval / Tropico Overall-Happiness** — settlement approval gates immigration/growth. **REAL but one-rung.** Confirms PS-gates-compliance at the settlement rung.

### G2 · Mandate aggregation (size-weighted, saturating)
- **EU4 Estate Influence** — +0.5 influence per 1% national land, **capped at 40**. **REAL — near-exact structural match for size-weighted *saturating* aggregation.** Lift the shape directly.
- **EU4 Mandate of Heaven** — 0–100, aggregated from **multiple tributary relationships (size-weighted) + control of specific cities**; <50 → Ming-crisis disaster. **REAL — best precedent for a mandate aggregating from many lower-scale relationships with a low-threshold cascade.**
- **CK3 factions Discontent** — members' military strength pooled as a **ratio** vs liege, gating a binary civil-war event. **REAL for the aggregate-then-resolve shape; SURFACE for the math** (linear sum/ratio, *not* saturating — Valoria's diminishing-returns `round(7T/(T+K))` has **no game precedent**, design it fresh).
- **Tropico** — faction relation weighted by the *faction leader* node (non-uniform per-member weight). **REAL.** Lift: aggregation weight need not be uniform per individual (leaders/large settlements weigh more).

### G3 · Standing ladder / political capital (0–7)
- **Old World Legitimacy→Orders** — one legitimacy scalar converts to **both** family-opinion (consent) **and** the turn's action-point budget (capacity). **REAL.** Lift: tie Standing/Mandate shortfall to *reduced capacity to act*, felt mechanically not just narratively.
- **KOEI ROTK rank-scaled everything** + **CK3 cadet Renown→Splendor** (continuous score → discrete perk tiers) — **REAL for the score→rank-ladder shape.** Weak direct precedent otherwise: EU4 offers only 0–100 stats bucketed to 2–3 bands; a **7-rung personal political-capital ladder is largely a Valoria original** (its own `faction_politics_v30` Skyrim-Eight is the real precedent).

### G4 · Governance-type cascade (each tier sets the type below)
- **CONVERGENT NEGATIVE FINDING (Imperator, Stellaris, EU4, ACOUP critique):** a top tier's government *type* does **NOT** force a matching type onto the tier below in any of them (Imperator Republic/Monarchy doesn't cascade to provinces; Stellaris authority cascades only at subject-*creation*; EU4 govt-type is single-scale). **A hard, continuous top-down type-cascade is a genuinely NOVEL surface — treat it as [GENUINE-GAP] with no clean port, and reconsider how "hard" it must be.**
- **Closest real precedent = CK3 Administrative (G1):** uniform broadcast + local attenuation. **EU4 government reforms** — tiered, scarce-currency-gated, group-partitioned institutional change. **REAL** template for how a governance mode changes over time (path-dependent, hard-gated), but single-scale — the per-tier version is Valoria's to add.
- **EU4 Republican Tradition** — sustained low support → **forced regime-type flip**. **REAL (qualified).** Lift: "support runs out → the governance mode itself changes," not just a penalty.
- **CK3 de jure drift** — a higher tier's claim over a lower updates via a slow, reversible, contiguity-gated progress bar (100yr / reverses at half speed). **REAL.** Lift: claims lag control, don't teleport.

### G5 · Delegation chain (ruler→governor→settlement) + disloyalty→secession
- **Imperator power-base** — the *same resource* that lets an appointee act (holdings/cohorts) **corrodes their loyalty** (~0.55/pt). **REAL.** Lift: **capability is corrosive to loyalty by construction** — don't model them as independent axes.
- **Imperator civil-war threshold** — secession triggers when the **aggregated % of disloyal national power** crosses a threshold that **shrinks as the polity grows** (25%→17%) and **shrinks further with Tyranny**. **REAL — load-bearing.** Lift: bigger realms are structurally more fragile; many quiet disloyalties are harmless until their *combined weight* crosses a scaling line.
- **KOEI ROTK rank-scaled secession** — a **Prefect** takes only their city independent; a **Viceroy** takes the whole **division**; a rival can *engineer* it via a "Collaborate" plot. **REAL.** Lift: **the disloyal actor's Standing rank = the blast radius of the break-away** (direct answer to Valoria's gap) + a faction-action that targets a rival's delegation chain.
- **KOEI "Delegate" as a first-class policy value** + **RTK Delegation Policy dial** — how much authority is devolved is an explicit selectable setting, not all-or-nothing. **REAL.** Lift directly for what a governor controls vs. what parliament/monarch retains.
- **Imperator/Stellaris convergence** — a bounded loyalty scalar + a sign/threshold that **blocks cooperation before allowing a break** + a **formal "request→earn-casus-belli" step** so secession isn't a single-frame cliff. **REAL (cross-validated by two teams).**
- **Old World cognomen-decay** — inherited legitimacy across a handoff decays **50%→33%→25%→20%→16.6%→13.3%→11.6%→10%**. **REAL — highest-value single formula for succession/appointment legitimacy carryover.**

### G6 · Chain-bypass authorities (monarch / parliament)
- **Imperator Tyranny** — the ruler forces an action past the Senate (40–60% support) by **spending Tyranny, which feeds the same civil-war-fragility gauge.** **REAL — strongest "metered-cost bypass" precedent.** Lift: bypass has a quantified cost against the secession-risk pool, never free.
- **CK3 Council named-target task** — ruler assigns a councillor who then acts **directly on a named county/vassal** (Promote Culture converts a named county; Increase Control on a named county), skipping mediation. **REAL.** Lift: delegated-authority-with-a-named-target skip.
- **Stellaris Planetary-Governor override** — drop a governor on **one** planet to reach past the Sector governor for that node only, rest stays delegated. **REAL — clean minimal "bend-around one node" precedent.**

### G7 · Collision-of-stresses (simultaneous multi-scale shock)
- **Dwarf Fortress mandate-clock** — a noble's fixed-timer **mandate deadline does not pause for a siege/famine**, so top-down obligation and bottom-up production-collapse collide in the same tick (real convictions during the crisis). **REAL — the cleanest true-collision precedent.**
- **Frostpunk 2 Whiteout** — one storm simultaneously spikes heat demand + overdrive-stress + sickness + transport-restriction + Trust-crash: **4+ systems hit at once, authored as one event.** **REAL.** Lift: hand-author specific collision events that hit multiple gauges/scales in parallel.
- **Imperator Tyranny × Aggressive-Expansion** — a top-down stress (Tyranny) and a bottom-up stress (new low-loyalty territory) draw down the **same** fragility gauge simultaneously. **REAL.**
- **EU4 disasters** — multi-factor accumulator → threshold → cascade-down; several inputs are themselves cross-scale aggregates (religious unity, Mandate, estate influence). **REAL for accumulate-then-cascade; SURFACE for true parallel collision** — EU4 funnels through one accumulator first, never hits many scales independently in one tick. **⇒ Valoria's parallel-collision mode is a genuine design departure with no clean port** (its own MS/Calamity/Strain radiation is the nearer base).
- **RimWorld anti-cascade dampener** + **DF's 15-year deliberate tantrum-dampening** — **collision-to-collapse is a DIAL, not a free byproduct.** Validates E7/E11 recovery/decay counters as *required*, not optional.

### G8 · Bottom-up emergence / arcs
- **Dwarf Fortress** — witnessed-event → thought → stress → breakdown → witnessed-event **contagion** is coded; the *same* stress/relationship graph is read by justice (grudges bias verdicts), nobility (popularity = legitimacy), petitions (belief-count → temple request). **REAL — the strongest bottom-up + "same variables read by multiple scales, don't invent a parallel ledger" precedent.** Boatmurdered = canonical emergent arc from one exogenous shock through individual grief to settlement death.
- **RimWorld** witnessed-death relationship-scaled grief contagion (~30-day decay) — **REAL narrow inter-individual**, SURFACE at colony scale.

### G9 · Nexus substrate (the "vectorized space" / policy web)
- **Democracy 3/4** — every object (policy, sim-value, voter group, pressure group, situation) is the **same type** with inbound+outbound signed-weight effect edges; **grey (zero-weight) edges are drawn even when inactive** (the edge exists structurally); situations are threshold/hysteresis feedback nodes re-entering the graph. **REAL for the node/edge substrate & legible feedback graph; SURFACE for cross-scale** (single geographic scale only). Lift: the uniform-object signed-edge substrate + legible drill-down UI (the UI, not the data, is what makes complexity legible).
- **Tropico edicts** — each policy legible as *this bloc gains / that bloc loses* + a "demonize faction" lever. **REAL** for the policy-as-cross-constituency-tradeoff web.

### G10 · Twin-gauge (L vs PS must stay divergent)
- **Frostpunk Discontent + Hope** — two opposing society-scale gauges from distributed local sensors; specific crises move both at once; each has its own terminal (coup vs collapse). **REAL — the direct L/PS twin-gate precedent.** Lift: keep formulas opaque (mood, not dashboard); author collision events that move both.
- **Tropico Overall-Happiness (bottom-up mean) vs Approval Rating (separate)** — **REAL.** Confirms L and PS should be genuinely divergent axes, not one value twice.
- **Frostpunk 2 Fervor** — unrest scoped **per-faction** (parallel meters), not one city number. **REAL.** Lift: L/PS per settlement node, not one national scalar.

### G11 · Decay / maintenance / recovery
- **EU4 Horde Unity** — constant unconditional decay ("cohesion tax") requiring active feeding; <70 → 5%/month probabilistic succession crisis (a distinct *probabilistic* trigger shape vs. deterministic accumulator). **REAL.** Lift: a Standing/cohesion stat that decays by default; probabilistic-vs-accumulator trigger choice.
- **CK3 Dread** — top-down signal attenuated by tier-distance (**100% direct / 70% indirect / 50% external**) then gated per-character vs Boldness. **REAL.** Lift: tier-distance falloff for a down-propagating pressure (a ready `propagate_fn` shape; complements MS's distance-falloff).
- **CK3 Tyranny** — single action → own accumulator that **fans out to many-vassal opinion + self-legitimacy in one tick**, with independent decay (−0.25/mo). **REAL.** Lift: single-trigger dual-target fan-out.

---

## Cross-cutting design rulings the games converge on (feed the fix doctrine)
1. **"Does it stick" = uniform broadcast + local attenuation** (CK3 Administrative), not a forced identical type. The hard type-cascade is Valoria-novel.
2. **Capability corrodes loyalty** (Imperator) and **rank = secession blast-radius** (ROTK) — the delegation chain's disloyalty math.
3. **Fragility scales with size** (Imperator threshold shrinks) — big realms structurally fragile.
4. **Bypass is metered against the same fragility pool** (Imperator Tyranny) — never a free monarch/parliament action.
5. **True parallel collision has no clean port** — a genuine Valoria departure; build on MS/Calamity/Strain.
6. **Collapse is a dial** (RimWorld/DF dampening) — recovery/decay counters (E7/E11) are required.
7. **Don't invent a parallel legitimacy ledger** (DF: popularity *is* legitimacy off the existing graph) — a [COMPLETE-THE-CHAIN] principle: read existing state, don't add bookkeeping.
8. **L and PS stay divergent** (Tropico/Frostpunk twin-gauge); **per-node, not one national scalar** (FP2 Fervor).
9. **Saturating aggregation is Valoria-original** (games use linear sum/ratio or land-share-cap); the `round(7T/(T+K))` shape has only partial precedent (EU4 influence cap).
10. **Succession/appointment legitimacy carryover** has a ready formula (Old World cognomen-decay 50%→…→10%).
