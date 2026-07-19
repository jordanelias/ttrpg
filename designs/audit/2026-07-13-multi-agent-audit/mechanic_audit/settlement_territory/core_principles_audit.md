# Mode E — Core Principles Compliance: Settlement / Territory

**Audit date:** 2026-07-13. Cross-referenced against `canon/02_canon_constraints.md` §A (P-01–P-15,
philosophical foundations) and §B (GD-1–GD-3, game-design constraints) — the SKILL.md Mode E table's
13-principle list is the older Foundations-only enumeration (predates the P-01–P-15 + GD-1–GD-3
consolidation now in `canon/02_canon_constraints.md`); both are checked below for completeness.
Settlement/territory is a strategic-macro subsystem, so several personal-scale principles are
correctly **not implemented locally** (they are inherited from the personal-scale docs this layer
sits on top of, per settlement_layer §8.2 "What Does NOT Change"). Those are marked N/A rather than
ABSENT, since ABSENT would wrongly imply a violation.

| # | Principle | Test | Verdict | Notes |
|---|-----------|------|---------|-------|
| 1 | Roll only when meaningful | Is there a "when to roll" gate? | PRESENT | Governance actions (§3.2) are the settlement layer's core roll; only fire on the governor's chosen seasonal action. Assault/Siege/Fortify checks (§5.1/§5.2) are similarly gated to specific triggering conditions (hostile entry, defense check on Fortress+hostile military), not ambient rolling. |
| 2 | Let It Ride | Is re-roll prohibition stated? | N/A (inherited) | Not restated locally; no settlement-layer mechanic contradicts it (no re-roll clause appears anywhere in the 4 target docs). Correctly silent, not a violation. |
| 3 | Fail Forward | Does failure advance narrative? | **ALTERED / gap** | The governance action table (§3.2) defines only success effects (GAP-06, Mode D). Other settlement-layer failure states *do* advance narrative correctly (Siege failure → attacker bypass/reduced-loop; Assault failure → "attacker repelled, takes casualties"; Fortress defense-check failure → "attacker bypasses or captures"). The governance-action gap is narrow but real: it is the layer's single most-used player action. |
| 4 | Histories, not Skills | Are Histories lived experience, not categories? | PRESENT | §3.2 governance pools consistently use "[Attribute] + [domain]-relevant History" (Wealth-relevant, Military-relevant, local, Governance) rather than a flat skill list — consistent with the corpus-wide History model. |
| 5 | Pool = Attribute + History bonus | Is the base formula preserved? | PRESENT | Same evidence as #4; no settlement-layer action deviates from Attribute+History pool construction. |
| 6 | Wound system with escalating Ob | Is +1 Ob per wound implemented? | N/A | Personal-combat mechanic; settlement/territory has no combatant-wound surface of its own (garrisons/units are handled by military_layer/mass_battle, out of scope). Not addressed here and correctly so — settlement_layer §8.2 explicitly states personal-scale combat mechanics are unchanged and out of this layer's remit. |
| 7 | Inspiration/Spirit economy | Is the emotional resource system present? | N/A | Not a strategic-macro concern; no contradiction found (Spirit is never referenced in these 4 docs). |
| 8 | Virtues & Vices | Is moral character mechanical? | PRESENT (partial) | Local Actors (§4.5) each carry one Conviction; governance Administer action reveals an NPC's active Conviction; Governance Transition scene (§4.3) offers Disestablishment/Accommodation/Transformation forks that read as Conviction-adjacent moral choices for the acting player/NPC. Not a full Virtue/Vice ledger at settlement scale, but Convictions are load-bearing, not decorative. |
| 9 | Social combat via Rhetoric (Appeals/Debates/Negotiation) | Are these distinct? | PRESENT (by reference) | Contested Management (§3.3) and Quo Warranto (§3.3a) both explicitly delegate to `social_contest_v30 §7`'s asymmetric-authority-vs-petitioner resolution rather than reinventing a local contest mechanic — correct layering, not a gap. |
| 10 | Reach/Speed priority (weapon geometry) | Does weapon geometry determine combat flow? | N/A | Personal-combat-only; settlement layer's own combat surface (mass battle) uses Manoeuvre-Phase edge-type modifiers (settlement_adjacency §2.2) instead, which is the correct strategic-scale analogue, not a violation of the personal-scale principle. |
| 11 | Phase-based combat | Is collaborative action within phases supported? | PRESENT (by reference) | Assault/Siege/Bypass (§5.1) and Mass Battle at Settlement Scale (§2, settlement_adjacency) explicitly delegate resolution to `mass_battle_v30 Part B`'s phase structure — settlement layer supplies the *location* and pre-battle modifiers, mass_battle supplies the phases. Correct division of labor. |
| 12 | Beginner's Luck | Is accessibility for untrained attempts present? | N/A | Not applicable to settlement governance (a Standing-gated, not skill-gated, activity per §3.2's eligibility table); no contradiction found. |
| 13 | Circles and Resources | Are social/economic resolution systems present? | PRESENT | The entire settlement layer is a Circles/Resources implementation at strategic scale: Treasury/Wealth economics, subnational-faction patronage (§3.3), Charter/patron mechanics (§3.3a/§3.3b), Local Actor social webs (§4.5), and the faction-emergence pathway (§6.2) all operationalize resource-and-relationship play. |

## GD-1–GD-3 (§B, game-design constraints) spot-check

| ID | Constraint | Verdict | Notes |
|----|-----------|---------|-------|
| GD-1 | Peninsular Sovereignty is the sole victory condition | PRESENT (consistent) | Settlement layer's only victory-adjacent claim is §8.1's note that "Universal victory still requires Accord ≥ 2 in all provinces. The pathway to Accord ≥ 2 is now through settlement governance" — this is fully consistent with GD-1's single win-path, not a competing condition. §1.8's "GD-1 synergy" paragraph explicitly ties Mandate-as-settlement-aggregate back to Peninsular Sovereignty rather than proposing an alternate path. No violation. |
| GD-2 | Deterministic threat response precedes stochastic action selection | N/A here | This subsystem defines the *data* (settlement Order/Accord thresholds) that GD-2's mandatory-action triggers key off (Accord ≤3 ungarrisoned / ≤2 garrisoned), but the action-selection algorithm itself lives in `sim/provincial/faction_action.py` (FA lane, out of scope). No contradiction in the settlement-layer docs themselves. |
| GD-3 | Revolt → Insurgency → Faction pipeline | PRESENT (consistent) | §6.2's Stage 1–5 faction-emergence ladder (Cell → Organization → Movement → Faction → Hegemon) reads as the settlement-layer's player-facing mirror of the same bottom-up emergence GD-3 specifies for NPC-driven insurgencies (2+ contiguous Uncontrolled territories → Insurgency → Faction). The two are not asserted to be the same mechanic, and no contradiction between them was found — both describe compatible, non-competing bottom-up pathways sitting on the same territorial-neglect logic. |

## Overall verdict

No outright ABSENT/violating principle found. One genuine ALTERED (#3, Fail Forward — narrow, tied to
GAP-06, already dispositioned P2/no-action in the gap register). GD-1 compliance is clean, which
matters most for this subsystem given how central settlement-derived Accord is to the sole victory
condition.
