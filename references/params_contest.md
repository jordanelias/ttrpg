<!-- version: v2.1-PP235 | sources: designs/contest/social_contest_system_v2.md | last_updated: 2026-04-04 -->
<!-- PP-234: Full system redesign. Genre restructure (3→2), attribute renames (Presence→Charisma, Memory→Recall), -->
<!--         Composure = Charisma + 6, faction boost revision (4 single-axis options), integer bonus dice, -->
<!--         adjudicator-type pool rotation, Let It Ride explicit, Fail Forward for ties. -->
<!-- SUPERSEDES: all prior params_debate.md versions. All SIM-D baselines invalidated (SIM-DEBT-03, SIM-DEBT-04). -->

# params_contest.md — Social Contest System (v2)

## Attribute Renames (PP-234)
| Old | New | Abbreviation |
|-----|-----|-------------|
| Presence | Charisma | Cha |
| Memory | Recall | Rec |

## Pools
| Roll | Pool | TN | Notes |
|------|------|----|-------|
| Argue (Expert Judge) | (Cognition × 2) + History bonus | 7 | Judge evaluates logical structure |
| Argue (Crowd) | (Charisma × 2) + History bonus | 7 | Crowd responds to delivery/authority |
| Argue (No Adjudicator) | (Attunement × 2) + History bonus | 7 | Must read and calibrate to counterpart |
| Argue (Panel) | (Cognition × 2) + History bonus | 7 | [PROVISIONAL — ED-137] |
| Read | Attunement only (no History) | 7 Ob 1 | Once per contest (PP-235). Result persists; degrades one tier per exchange after first. Action name [ED-132]. |
| Recall bonus | +2D | — | Citing specific named verifiable claim. Binary. Either genre. |
| Pre-contest prep | Attunement + History | 7 Ob 1 | Requires 1+ hour. Rushed: TN 8. |

## Genres (2)
| Genre | Temporal Status | Epistemic Status | Actualization Status |
|-------|----------------|-----------------|---------------------|
| Memory | Retention (has been) | Accessible | Actual (settled) |
| Projection | Protention (yet to be) | Inaccessible | Potential (unsettled) |


## Argument Styles (PP-235)
Genre + orientation presented as a single choice per exchange:

| Style | = Genre + Orientation | Flavour |
|-------|----------------------|---------|
| Precedent | Memory + Revealing | Citing what happened openly |
| Suppression | Memory + Obscuring | Burying inconvenient history |
| Vision | Projection + Revealing | Proposing a transparent future |
| Insinuation | Projection + Obscuring | Implying unstated consequences |

Interaction type derived: same style = REINFORCE, same genre opposite orientation = CLASH, different genre = CROSS.
## Genre and Orientation Bonus Dice
| Source | Bonus | Condition |
|--------|-------|-----------|
| Primary genre | +1D | Orator's chosen genre matches GM-set primary genre |
| Audience boost | +1D | Orator's chosen genre OR orientation matches audience faction's boosted axis |
| Maximum combined | +2D | Both conditions met |

## Faction Boosts (single axis per faction)
| Faction | Ethical Mode | Boost | Axis |
|---------|-------------|-------|------|
| Church | Divine Command | Obscuring | Orientation |
| Crown | Virtue Ethics | Revealing | Orientation |
| Varfell | Consequentialism | Projection | Genre |
| Hafenmark | Categorical Imperative | Memory | Genre |
| Restoration | Rawlsian Social Contract | Revealing | Orientation |
| Guilds | Moral Relativism | GM picks | Either |
| Löwenritter | Duty-based (if emerged) | Projection | Genre |
| Niflhel | — | GM picks | Either |

## Initiative
Exchange 1: higher Attunement acts last (information advantage). [ED-138: deterministic vs rolled?]
Subsequent: transfers to exchange winner. Tie: stays with holder.
Institutional override: institution determines proposer in asymmetric proceedings.

## Exchange Structure
Step 1 — Read (Attunement, TN 7, Ob 1):
| Net | Information |
|-----|-------------|
| Failure | Misleading signal: wrong boost identified |
| Partial (1) | Boosted axis type (genre or orientation) but not which |
| Success (2) | Full boost identified |
| Overwhelming (3+) | Boost + one specific detail (Belief, threshold, emotional state) |

Step 2 — Choose genre (Memory/Projection) + orientation (Revealing/Obscuring).
Step 2b — Corroborate (automatic when Bonds ≥ 3 symmetric or ≥ 4 asymmetric disadvantaged; +1D on success. PP-235).
Step 3 — Argue (pool per §Pools + genre/orientation bonus).
Step 4 — Resolve (see Interaction Types).
Step 5 — Forfeit (Regroup or Concede a Point).
Step 6 — Strain and Concentration.
Step 7 — GM records.

## Interaction Types (3 + TIE)
| Type | Condition | Resolution | Strain |
|------|-----------|------------|--------|
| CLASH | Same genre, opposite orientation | Compare; margin vs resistance → track movement | Margin + Cha modifier − Foc defence (min 0) |
| REINFORCE | Same genre, same orientation | Same as CLASH | (Margin − 1, min 0) + Cha modifier − Foc defence (min 0) |
| CROSS | Different genres | Each side: floor(successes ÷ 2) vs resistance; net movement = difference | None |
| TIE | Equal successes, any type | Both take 1 strain; track +1 toward initiative holder | 1 each |

Obscuring win: no track movement; place Doubt Marker on opponent (−2 to opponent's next winning margin; one active at a time; consumed on use).

## Conviction Track
Range: 0–10. Side A wins ≥ 7. Side B wins ≤ 3. Compromise zone: 4–6.
Starting position: GM-set (typical: 5).
Audience resistance: average Stability of factions (round up) − 1, minimum 0. Announced once at contest start; place resistance token on Conviction Track. (PP-235)

## Derived Values
| Value | Formula | Range |
|-------|---------|-------|
| Composure | Charisma + 6 | 7–13 |
| Charisma modifier | max(0, floor((Cha − 3) ÷ 2)) | 0–2 |
| Focus defence | floor(Foc ÷ 2) | 0–3 |
| Concentration | Focus + Recall | 2–14 |
| Read pool | Attunement only | 1–7 |

## Composure and Rattled
At strain ≥ Composure: Rattled mark (Composure resets; excess carries over).
+1 Ob per Rattled level (cumulative). 2 marks = socially incapacitated.
Recovery: 1 mark/scene of non-social activity. Composure restores at scene change.
Knot buffer: redirect damage to Knot (+1 strain/use).

## Concentration and Spent
Depletes −1/exchange, −1 additional on loss.
At 0: Spent (−2D next exchange; opponent +1D). Resets to max after.
Rattled + Spent: cumulative. Pool minimum 1D.

## Forfeit Actions
| Action | Strain | Track Effect | Benefit |
|--------|--------|-------------|---------|
| Regroup | 0 | +1 toward non-forfeiting side | Concentration restores by Focus |
| Concede a Point | 1 | +1 toward non-forfeiting side | +1D next exchange |

## Post-Contest
| Outcome | Effect |
|---------|--------|
| Decisive + Memory genre | Winning faction Mandate +1 in domain of cited precedent |
| Decisive + Projection genre | +1D on first Domain Action pursuing argued outcome (1 season) |
| Total Victory (≥9 or ≤1) | Contest Fatigue on loser (−1D next social roll); +1 Momentum winner; Disposition/Reputation shift |
| Compromise (4–6) | No Domain Echo; GM narrates partial outcome |
| Private tie (no tracker) | Stall; strain persists; Read info permanent; relationship stressed |

Thread co-movement: Memory win → RS +1 (retention invoked). Projection win → RS +1 if Thread-sensitive.

## Proceeding Types
| Type | Exchanges | Roles | Resistance Mod | Adjudicator |
|------|-----------|-------|---------------|-------------|
| Formal Contest | 3 | Alternating | Standard | Crowd |
| Grand Contest | 5 | Alternating | Standard | Crowd |
| Royal Audience | 3 | Crown objects | Halved for petitioner | Expert Judge |
| Church Tribunal | 1–5 | Inquisitor proposes | Halved for accused | Expert Judge |
| Guild Arbitration | 3 | Symmetric | Standard | Expert Judge |
| Casual Dispute | 1 | Initiator proposes | N/A | No Adjudicator |
| Private Negotiation | 1–3 | Symmetric | N/A | No Adjudicator |
| Personal Appeal | 1 | Appealer proposes | N/A | No Adjudicator |

## Niflhel Social Toolkit [ED-041 provisional]
No Formal/Grand Contests. Private negotiation only (Attunement pool). Thread Insight (TS ≥ 30): Attunement read reveals one unstated position.

## Practitioner Weaving (R-65)
TS ≥ 30: +floor(TS ÷ 30)D. Declare before rolling. Visible. Church may file Heresy Investigation. Coherence Ob 1 after.

## Let It Ride
Resolved questions cannot be re-contested without significantly changed circumstances.

## Simulation Debt
| ID | Description |
|----|-------------|
| SIM-DEBT-03 | Full re-sim under two-genre system. All prior baselines invalidated. |
| SIM-DEBT-04 | Adjudicator-type pool variation untested. |

<!-- patch_history: references/params_contest_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->

## PP-236 — CROSS Tie no-strain
CROSS interaction + equal successes: no strain to either orator. CROSS no-strain rule overrides Tie +1-strain. Conviction Track +1 toward initiative holder as normal.

## PP-237 — Coalition Concentration shared pool
Shared pool = sum of all coalition members' (Focus+Recall) at setup. Depletes 1/exchange (+1 on loss) regardless of Lead rotation. Spent at 0; resets to setup total.

## History bonus note (PP-234 era)
History bonus = history points + 3 (per Stage 2 §4.1). Pool (PrimaryAttr×2)+H is equivalent to combat pool (Agi×2)+H+3. The +3 is embedded in H.

## PP-257 — Corroboration Knot relaxed
Any declared coalition member can corroborate (Knot not required). Knot-sharing = Ob 1; non-Knot coalition member = Ob 2. Asymmetric proceedings: all disadvantaged-party corroborators use Ob 2.

## PP-272 — "Division" stricken
Term removed from §7 Church Tribunal as vestigial. No mechanic defined.

## Corroboration — Knot Relaxed (PP-280)
Any declared coalition member can corroborate (Knot not required).
Knot-sharing coalition member: Ob 1 corroboration.
Non-Knot coalition member: Ob 2 corroboration.
Asymmetric proceedings (Tribunal): all disadvantaged-party corroborators use Ob 2.

## Contest Stalemate — Forced Resolution (PP-282)
Maximum 10 exchanges per Contest session. After 10 consecutive exchanges without resolution:
Forced Unmask fires. Loser = orator whose track is closer to their losing threshold (or lower Composure on tie).
Prevents indefinite stalemate when resistance ≥ all achievable effective margins.

## Hybrid Debate TC Clamp (PP-283)
In Hybrid mode Contest (§6.14): TC restricted to range 4–6 at session start regardless of BG lobbying.
BG lobbying shifts starting position ±1 within that range only.
Prevents BG-layer pre-deciding Contest outcome.

## Passive RS from Contest — Gate Tightened (PP-284)
Passive RS consequence fires AUTOMATICALLY (no GM discretion) when:
(a) Contest subject is a Thread-factual claim (Thread existence, practitioner capability, RS status), OR
(b) A Thread operation is used during a Contest exchange.
All other Contest subjects: no passive RS consequence.

## Church Self-Investigation Exception — Scope (PP-285)
§6.15 exception covers ordained members of the Church only.
Does not apply when the Thread operation targets a Church institutional interest (e.g., Dissolution of a Church-controlled Lock; Pulling a Church-controlled document).

## Temporal Axis Conflict Penalty (PP-286)
Replaces PP-123 TN8 ruling.
When temporal axis conflict fires in a Contest exchange: −1D to BOTH parties' Argue rolls for that exchange only.
Symmetric: both parties' argumentative footing is destabilised equally.

## Judge Action — Replaces 'Read' (PP-292)
Exchange Step 1 action renamed from 'Read' to 'Judge' throughout.
Judge: assess opponent's mode and state. Attunement + Recall vs Ob (opponent's Charisma÷2, round up).
The rename applies to all Contest scene types: Formal Debate, Grand Debate, Negotiation, Appeal, Tribunal.

## Social Initiative Tie-Break (PP-295)
Exchange 1 initiative: higher Attunement goes first. Confirmed deterministic.
Tie: higher Charisma. Further tie: GM choice or simultaneous resolution.

## 'Division' Struck from Tribunal (PP-301)
'Division' is a parliamentary motion; it has no meaning in an inquisitorial proceeding.
Struck from §7 Church Tribunal text. Replacement text: 'The accused may not call for any procedural motion during the Argument Phase.'
