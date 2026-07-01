<!-- version: v2.1-PP235 | sources: designs/contest/social_contest_v30.md | last_updated: 2026-04-04 -->
<!-- PATCHES APPLIED (canonical): PP-123, PP-171, PP-232, PP-234–237, PP-242, PP-245, PP-253–259, PP-272, PP-278–279, PP-378, PP-390–395, PP-349, PP-351, PP-401, PP-449–450, PP-452–458, PP-460–463, PP-465, PP-529, PP-612, PP-614 -->
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
| Argue (Panel) | (Cognition × 2) + History bonus | 7 | [PROVISIONAL — pre-ledger, accepted as canonical per 2026-04-26 audit] |
| Appraise | Attunement + Recall | 7 | Ob = opponent Charisma ÷ 2 (round up), min 1. Once per exchange. PP-614: consolidates Read/Judge/Appraise into single canonical entry. |
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
<!-- ED-899/ED-897: ethical-mode labels aligned to social_contest §2 skeleton set (Divine Command / Virtue Ethics / Rawlsian Social Contract); orientation Indirect/Direct → Obscuring/Revealing. Niflhel row already struck (ED-764, above). -->
<!-- Niflhel row deleted 2026-04-30 — STRUCK per CR-STRIKE-2026-04-19 / ED-764. Was: ~~Niflhel~~ STRUCK | — | — | — | Per ED-764. -->

## First to Speak
Exchange 1: ROLLED — both orators roll Attunement vs Attunement, TN 7, Ob 1; higher net successes acts last (information advantage). On net tie: higher Attunement stat; then the adjudicator assigns. [ED-895: ED-138 resolved to rolled per ED-581 — aligns with combat initiative. Supersedes the prior deterministic "higher Attunement acts last".]
Subsequent: transfers to exchange winner. Tie: stays with holder.
Institutional override: institution determines proposer in asymmetric proceedings.

## Exchange Structure
Step 1 — Appraise (Attunement + Recall, TN 7, Ob = opponent Cha ÷ 2 round up, min 1) [PP-614 / ED-893; the old "Read = Attunement only, Ob 1" is struck — see §Pools]:
| Net | Information |
|-----|-------------|
| Failure | Misleading signal: wrong boost identified |
| Partial (1) | Boosted axis type (genre or orientation) but not which |
| Success (2) | Full boost identified |
| Overwhelming (3+) | Boost + one specific detail (Belief, threshold, emotional state) |

Step 2 — Choose genre (Memory/Projection) + orientation (Direct/Indirect).
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
| REINFORCE | Same genre, same orientation | Same as CLASH | max(0, (Margin − 1) + Cha modifier − Foc defence) | (PP-401, ED-296 fix: floor at 0) |
| CROSS | Different genres | Each side: floor(successes ÷ 2) vs resistance; net movement = difference | None |
| TIE | Equal successes, any type | Both take 1 strain (except CROSS: no strain — PP-236); track +1 toward first-to-speak holder | 1 each (except CROSS: 0 — PP-236) |

Obscuring win: no track movement; place a Doubt Marker on the opponent (−2 to opponent's next winning margin; one active at a time; consumed on use). [ED-897: "Indirect"→"Obscuring", "Doubt Marker"→"Doubt Marker" to match social_contest §4.]

**Coalition Push (clarification, ED-897):** not a separate interaction type — it denotes a REINFORCE (same genre, same orientation) executed by a coalition (§9.2), whose shared pool yields the larger movement noted in ED-297. The interaction types are CLASH / REINFORCE / CROSS / TIE.

## Persuasion Track
Range: 0–10. Side A wins ≥ 7. Side B wins ≤ 3. Compromise zone: 4–6.
Starting position: GM-set (typical: 5).
Audience resistance: average Stability of factions (round up) − 1, minimum 0. Announced once at contest start; place resistance token on Persuasion Track. (PP-235)

## Derived Values (CR3 — three trackers; ED-1056)
CR3 (RATIFIED 2026-06-01) retires **Composure** as the social-contest tracker and splits it into **Concentration** (stamina) + **Face** (contest-local ethos/standing). The Persuasion Track (merits clock) is preserved. Composure-retirement is SCOPED to the social-contest tracker only (unrelated Composure references in knots/combat/conviction are untouched — Jordan CONFIRMED scoped-rename-only at Gate A; see social_contest_v30 §8).

| Value | Formula | Range | Note |
|-------|---------|-------|------|
| Face | Face_max = Charisma × 3 (ceiling); Face_current = round(Standing ÷ 10 × Face_max) | 3–21 | Contest-local ethos/standing buffer (the retired Composure magnitude, re-homed as transient standing; CR3/ED-1056; scale-binding resolved Gate A 2026-07-01 — see below). Face ≠ Disposition/Reputation. |
| Charisma modifier | max(0, floor((Cha − 3) ÷ 2)) × 3 | 0–6 | ×3 scaling unchanged by CR3 (matches the Face buffer). |
| Focus defence | floor(Foc ÷ 2) × 3 | 0–9 | — |
| Concentration | (3 × Focus) + (2 × Spirit) | 5–35 | ED-901 (STRUCK Focus×3) + ED-902 (coefficients + Cognition→Focus engine fix) + ED-933 (params propagation). |
| Appraise pool | Attunement + Recall | 2–14 | — |

## Face and Rattled (CR3 — formerly "Composure"; ED-1056) [UNREACHABLE UNTIL STAGE 3]
> **[FACE SCALE-BINDING — RESOLVED, Gate A, 2026-07-01 (ED-1056)]** This §Face-and-Rattled surface defines Face as a **Charisma × 3 (3–21) strain-buffer** consumed by the Rattled channel (below) — this is now **Face_max**, an unchanged build-time ceiling (player-controlled via Charisma). The sim kernel (`sim/personal/contest/primitives.py`) binds `Face = Standing`, a **0–10, START 5, ethos-built** tracker feeding Readiness/leak — Standing itself is UNCHANGED by this resolution. Jordan resolved the scale-binding as a combo formula: **Face_current = round(Standing ÷ 10 × Face_max)** — Standing (earned through play) sets position within the Charisma-set ceiling (fixed at build time). Implemented as `FaceScale.face_max`/`FaceScale.face_current` (primitives.py) + `_Side.face_max()`/`_Side.face_current()` (resolver.py), added on top of the unchanged Standing — no new invented constants, no change to currently-tested Standing/Readiness behaviour. **What is STILL not wired this pass:** the strip/strain-consumption channel below — the kernel has **no strip/strain channel wired** (Standing.strip() is never called), so the Rattled behaviour below is a v30-surface spec not yet realized in code. Face_current is now a real, well-defined value (Standing-derived, Charisma-scaled) but strain does not yet consume it; that wiring is Stage-3 (CR5 rhetoric-armature) scope, honestly flagged, not silently claimed as wired. See social_contest_v30 §4 Step 6 / §8.

At strain ≥ **Face**: Rattled mark (Face resets; excess carries over). [Face = Cha × 3 — the retired Composure magnitude re-homed onto the Face tracker per CR3/ED-1056; ED-694 scaling.]
−1D per Rattled level to Argue pool (cumulative; honors PP-716 channel reservation: actor-state degradation → Pool, not Ob). 2 marks = socially incapacitated. Pool minimum 1D. [Decision-B 2026-05-15: Rattled converted from +Ob to −1D for channel consistency with wounds/Spent.]
Recovery: 1 mark/scene of non-social activity. Face restores at scene change.
Knot buffer: redirect **Face** damage to Knot (+1 strain/use). [CR3/ED-1056: Composure-retirement is scoped to the contest tracker; knots_v30 §4.2 still names this the "Knot-as-Composure-buffer" — Jordan CONFIRMED scoped-rename-only at Gate A (social_contest_v30 §8); the corpus-wide Composure→Face rename was considered and not taken.]

## Concentration and Spent
Depletes −5/exchange, −5 additional on loss. [ED-890/DEP: rescaled −1 → −5 to match social_contest §4 and keep Spent reachable under the (3 × Focus) + (2 × Spirit) 5–35 range; the prior −1 left Spent inert.]
At 0: Spent (−2D next exchange; opponent +1D). Resets to max after.
Rattled + Spent: cumulative. Pool minimum 1D.

## CR1 / CR2 Substrate (RATIFIED 2026-06-01; realized in code Stage 1a–1c, confirmed Stage 1d / ED-1055 provisional, pending Gate-A)
- **CR1 — wrapper→modules architecture.** Contest resolution runs through a wrapper (`sim/personal/contest/wrapper.py`) that ADAPTS + ROUTES but resolves nothing (`build_contest` adapter + `resolve_contest` router). The stochastic surface is the reception roll only; all else is deterministic accounting. Already realized (Stage 1c); Stage 1d cites, does not re-build.
- **CR2 — resolution substrate migration to δσ.** Social resolution is no longer success-counting; it is the shared sigma-leverage net engine (per-die −1/0/+1/+2, δσ μ-shift, TN7), single-sourced with combat/core via `sim/autoload/sigma_leverage.py` (D0-2). CR2 = the resolution substrate ("what the roll is"); CR6 = the leverage-accumulation half ("how setup advantages enter the roll" — δσ, tanh soft-capped, +0.191 uniform across 5D–26D). Contest stays δσ at TN7 (D0-3); the fractional-Ob face is display-only (D0-3 HYBRID). Both realized Stage 1a/1b + D0-3; Stage 1d cites, does not re-build.
- **CR3 — three trackers.** Concentration (stamina, above) + Face (contest-local ethos/standing, §Face and Rattled) + Persuasion Track (merits, §Persuasion Track). Composure retired → split into Concentration + Face (ED-1056).

## Forfeit Actions
| Action | Strain | Track Effect | Benefit |
|--------|--------|-------------|---------|
| Regroup | 0 | +1 toward non-forfeiting side | Concentration restores to max (per social_contest §4 Step 5) |
| Concede a Point | 1 | +1 toward non-forfeiting side | +1D next exchange |

## Post-Contest
| Outcome | Effect |
|---------|--------|
| Decisive + Memory genre | Winning faction Mandate +1 in domain of cited precedent |
| Decisive + Projection genre | +1D on first Domain Action pursuing argued outcome (1 season) |
| Total Victory (≥9 or ≤1) | Contest Fatigue on loser (−1D next social roll); +1 Momentum winner; Disposition/Reputation shift |
| Compromise (4–6) | No Domain Echo; GM narrates partial outcome |
| Private tie (no tracker) | Stall; strain persists; Read info permanent; relationship stressed |

Thread co-movement: Memory win → MS +1 (retention invoked). Projection win → MS +1 if Thread-sensitive.

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

<!-- §Niflhel Social Toolkit deleted 2026-04-30 — was struck per CR-STRIKE-2026-04-19 / ED-764. Replacement: settlement-level intelligence-broker NPCs (settlement_layer §4.7-4.9) use individual social interaction patterns per npc_behavior §1. -->

Original ED-041 provisional content (kept for archival reference but no longer canonical):
No Formal/Grand Contests. Private negotiation only (Attunement pool). Thread Insight (TS ≥ 30): Attunement read reveals one unstated position.

## Practitioner Weaving (R-65)
TS ≥ 30: +floor(TS ÷ 30)D. Declare before rolling. Visible. Church may file Heresy Investigation. Coherence Ob 1 after.

## Let It Ride
Resolved questions cannot be re-contested without significantly changed circumstances.

## Simulation Debt
| ID | Description | Status |
|----|-------------|--------|
| SIM-DEBT-03 | Full re-sim under two-genre system. | RESOLVED — ED-295/297 confirmed working via historical precedent. |
| SIM-DEBT-04 | Adjudicator-type pool variation untested. | OPEN |

<!-- patch_history: references/params_contest_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->

## PP-236 — CROSS Tie no-strain
CROSS interaction + equal successes: no strain to either orator. CROSS no-strain rule overrides Tie +1-strain. Persuasion Track +1 toward first-to-speak holder as normal.

## PP-237 — Coalition Concentration shared pool
Shared pool = sum of all coalition members' (3×Focus)+(2×Spirit) at setup. Depletes 5/exchange (+5 on loss) regardless of Lead rotation. Spent at 0; resets to setup total. [ED-894: Recall removed (ED-694); mirrors solo Concentration.]

## History bonus note (PP-234 era)
History bonus = history points + 3 (per Stage 2 §4.1). Pool (PrimaryAttr×2)+H is equivalent to combat pool (Agi×2)+H+3. The +3 is embedded in H.

## PP-257 — Corroboration Knot relaxed
Any declared coalition member can corroborate (Knot not required). Knot-sharing = Ob 1; non-Knot coalition member = Ob 2. Asymmetric proceedings: all disadvantaged-party corroborators use Ob 2.

## PP-272 — "Division" stricken
Term removed from §7 Church Tribunal as vestigial. No mechanic defined.

## PP-614/PP-278 — Appraise (canonical)
Exchange Step 1: Appraise. Pool: Attunement + Recall | TN 7 | Ob = opponent Cha÷2 (round up), min 1.
PP-254 (Judge/Att+Rec pool) + PP-278 (Appraise name) consolidated. Old "Read pool = Attunement only Ob1" struck.

## PP-279 — FR terminology
"Forced Resolution" label struck. Operations: Weaving, Pulling, Locking, Dissolution, Mending. Locking and Dissolution are self-descriptive.

## Contest System Label (PP-253)
System label 'Debate System' renamed to 'Contest System'.
Individual scene types retain names: Formal Debate, Grand Debate, Tribunal, Negotiation, Appeal, Command Contest.
'Debate' as a system-level label is deprecated.

## Judge Action — Replaces 'Read' (PP-254)
Exchange Step 1 renamed from 'Read' to 'Judge' throughout.
Judge: assess opponent's mode, stance, and vulnerability.
Pool: Attunement + Recall | TN 7 | Ob: opponent's Charisma÷2 (round up)
Judge result informs Argue roll orientation selection.

## Contest Stalemate — Forced Resolution (PP-255)
Maximum 10 exchanges per Contest session.
After 10 consecutive exchanges without resolution: forced Unmask fires.
Loser = orator whose track is closer to their losing threshold (lower **Face** on tie). [CR3/ED-1056: "Composure" tiebreak re-homed onto Face.]

## Hybrid Debate CI Clamp (PP-256)
In Hybrid mode Contest: CI restricted to range 4–6 at session start regardless of BG lobbying.
BG lobbying shifts starting position ±1 within that range only.
Prevents BG-layer pre-deciding Contest outcome.

## Church Self-Investigation Exception Scope (PP-257)
§6.15 exception: ordained members only.
Does not apply when Thread op targets a Church institutional interest.

## Temporal Axis Conflict Penalty (PP-258 — SUPERSEDED, ED-900 / D-3)
[SUPERSEDED: temporal-axis conflict now routes the thread op's co-movement to the Persuasion Track (±1 per co-movement instance) per the canonical PP-351 (contest_extensions / social_contest §9.4). The prior "−1D to both Argue" is retired.]

## Passive MS from Contest — Gate (PP-259)
MS consequence fires automatically when:
(a) Contest subject is a Thread-factual claim, OR (b) Thread op used in a Contest exchange.
All other subjects: no MS consequence. No GM discretion required.

## BG Doubt Marker Analog
No analog needed. BG debate fully abstracted. Parliamentary Vote (ED-053) handles faction-level outcomes.


## P1 Findings — RESOLVED (superseded by "P1 Findings — Resolved 2026-05-17" below)
[ED-896: this 2026-04-04 block is stale — ED-295 (resolved: Option D per-exchange erosion), ED-296 (resolved: max(0, …) floor), ED-297 (resolved: coalition dominance RATIFIED as intended) are all settled in the Resolved block below. The "User decision required" markers below are obsolete; retained only for trace.]

### ED-295: CLASH movement stalls at median
floor(margin × genre_weight × orientation_weight − resistance) produces 0 movement
when margin barely exceeds resistance. At median dice results, CLASH advances
the Persuasion Track by 0 — contest stalls. Four fix options proposed (A-D).
**User decision required.**

### ED-296: REINFORCE produces negative movement
(margin − 1) × modifiers − resistance goes negative when the stronger orator's
margin is small. Fix: apply max(0, ...) floor to REINFORCE movement.
**Mechanical fix — can apply without user decision if authorized.**

### ED-297: Coalition Push dominant over CLASH
Coalition Push produces ~5 movement/exchange vs CLASH ~0 at median. Coalitions are
mechanically superior to solo advocacy. May be intended design (rewarding alliances).
**User decision required: confirm or rebalance.**


---

## Extensions

Additional canonical rules for Contest! are filed at `params/contest_extensions.md`:
- PP-NEW-A — TIE/CROSS no-strain exception (SIM-DB-STRESS-01 D-04)
- PP-NEW-D — Concentration maximum (SIM-DB-STRESS-01 D-08b; updated PP-716)
- Evidence Track Findings in Contest (PP-636)
- Resonant Style Targeting (from npc_behavior_system_v1.md §6)
- Temporal Axis Conflict (PP-351 — canonical)
- Church Self-Investigation Exception (PP-349 — canonical)

## P1 Findings — Resolved 2026-05-17 (audit ED-864)

- **ED-295** (CLASH stalls at median margin): Option D — audience resistance erodes per exchange. Per-exchange erosion: `Stab_resistance_t = max(0, Stab_resistance_0 − ⌊exchange_count / 2⌋)`. First exchange uses baseline resistance; every two exchanges thereafter reduces audience resistance by 1. Long contests resolve organically; short contests retain current dynamics. Spec applies to all Interaction Types (CLASH, REINFORCE, CROSS, Coalition Push).
- **ED-296** (REINFORCE negative movement): floor at 0 — already applied in Interaction Types table (`max(0, (Margin − 1) + Cha modifier − Foc defence)`).
- **ED-297** (Coalition Push magnitude ~5/exchange vs solo ~0): RATIFIED as canonical design. Coalitions mechanically dominate solo advocacy by intent (parliamentary politics).

Source: `designs/audit/2026-05-17-scene-combat-contest/decisions.md`
