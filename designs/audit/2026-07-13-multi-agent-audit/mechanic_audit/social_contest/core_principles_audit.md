# Social Contest — Mode E: Core Principles Compliance

**Audit date:** 2026-07-13
**Target:** `designs/scene/social_contest_v30.md` (+ `_index`/`_infill`), `params/contest.md`
**Reference:** the skill's own 13-principle table (`skills/valoria-mechanic-audit/SKILL.md` Mode E);
cross-checked against `canon/02_canon_constraints.md` P-01–P-15 (the Philosophical Foundations
constraints, a distinct list from the 13 core-play principles) where the two overlap, notably P-01
(Inseparability / co-movement) and P-14 (Board/VG modes must express inseparability).

| # | Principle | Status | Evidence |
|---|---|---|---|
| 1 | Roll only when meaningful | **PRESENT** | §1 explicit initiation gate: "A contest is initiated when: (a) two or more parties with opposed positions are present, AND (b) the outcome is uncertain and consequential. GMs should not call for a contest when one side has no plausible case or when the outcome is predetermined by prior Domain Actions." (`social_contest_v30.md` §1, infill L20) |
| 2 | Let It Ride | **PRESENT** | Explicit named rule: "once a contest resolves a question, that question cannot be re-contested unless circumstances have significantly changed" (§1 infill L21); reinforced by the Contest-level Let It Ride entry in the "Resolved by this version" table (§12) |
| 3 | Fail Forward | **PRESENT** | Private-negotiation tie explicitly narrated as consequential, not a null result: "the contest stalls: strain persists, all Read results... become permanent knowledge... The narrative moves forward — the failure to agree IS a consequential outcome" (§2 Step 4, L95). Compromise outcomes generate Chain Contests (§6.3) rather than stalling play. |
| 4 | Histories, not Skills | **PRESENT** | The doc consumes "History bonus" as an additive pool term (§3, §8) without redefining History as a generic skill category; History's lived-experience semantics are authored in the character-creation/core-engine layer this doc correctly defers to |
| 5 | Pool = Attribute + History bonus | **ALTERED (justified)** | Argue Pool = **(Primary Attribute × 2)** + History bonus (§3 L121) — a deliberate doubling, not the baseline additive form. The doc itself flags this as historically borrowed from combat's old pattern but now standing on its own native rationale post-ED-1084 (combat was re-ratified Agility-independent, `max(5, History+6)`, breaking the shared-formula analogy): "the doubled-attribute pattern here is now native to the social contest, not borrowed from combat" (§3 L132–137). Justification is documented and traceable (ED-1084), not a silent drift. |
| 6 | Wound system with escalating Ob | **ALTERED (justified, corpus-wide)** | Contest has no literal wound track; its structural analogue (Rattled marks from accumulated strain) escalates via **−1D Pool per Rattled level**, not "+1 Ob" (§4 Step 6 L245: "actor-state degradation is a Pool penalty, not Ob, per the channel reservation (Decision-B 2026-05-15 / PP-716). Supersedes the prior '+1 Ob'."). This is a corpus-wide channel-reservation decision (PP-716 flipped all wound-induced-Ob references to Pool penalties across combat/thread/mass-Command/BG-CF), not a contest-specific deviation — the "13 principles" wording predates that later, ratified corpus-wide shift. |
| 7 | Inspiration/Spirit economy | **PRESENT** | Momentum spend before rolling (any amount, 1 Momentum = 1 success, §4 Step 3 L172); Belief-alignment Momentum award, capped 1/contest (§9.5); Spirit feeds the Concentration formula directly ((3×Focus)+(2×Spirit), §4 Step 6) |
| 8 | Virtues & Vices | **PRESENT** | Conviction Scar production and player-facing signaling (§6.2); Resonant Style targeting cross-references `npc_behavior_v30` §1.3/§6.3; the Adjudicator Armature (§4 Step 3) is itself a four-axis Conviction-vector mechanism — moral/ideological character is directly mechanical, not flavor text |
| 9 | Social combat via Rhetoric (Appeals, Debates, Negotiation distinct) | **PRESENT, with a tracked depth caveat** | Eight named proceeding types exist with genuinely different structural parameters (exchange count, role structure, resistance modifier, adjudicator, stasis start — §2 Step 5 table): Formal/Grand Contest, Royal Audience, Church Tribunal, Guild Arbitration, Casual Dispute, Private Negotiation, Personal Appeal. **Caveat (no new action — already tracked):** the 2026-07-05 Fable-5 audit found these currently resolve through one shared exchange-loop engine ("one game wearing eight venue skins," finding `KT-1`), a content-depth gap already feeding the ratified Stage-4 "four deliberative games" work, not a structural absence of distinct proceedings |
| 10 | Reach/Speed priority (weapon geometry determines combat flow) | **N/A — not applicable to this subsystem** | This principle is combat-domain-specific (physical weapon geometry). Social contest has no analogous concept and correctly does not attempt one; not a violation |
| 11 | Phase-based combat (collaborative action within phases) | **ALTERED (adapted)** | Contest's Exchange structure (§4) is the phase-analogue; collaborative action within an exchange exists via Corroborate (§4 Step 2b) and full Coalition Structure (§9.2, multi-party Lead/Corroborate roles, shared Concentration pool). This is a genuine adaptation of the phase-collaboration principle to the contest domain, not an omission |
| 12 | Beginner's Luck (accessibility for untrained attempts) | **ABSENT** | No "Beginner's Luck," untrained-roll, or zero-History accessibility rule appears anywhere in `social_contest_v30.md`, `social_contest_v30_infill.md`, or `params/contest.md` (grep-verified). A corpus-wide search finds the term used only in `designs/scene/fieldwork_v30.md` — it does not appear to be a maintained cross-cutting mechanic at all, so this is not obviously a contest-specific gap so much as a possible corpus-wide one. **Disposition:** no ED filed from this lane — if a general Beginner's Luck mechanic is canonical anywhere (core engine), the omission from social_contest is worth a cross-check by whichever lane owns core-engine accessibility rules (likely `IN` or a future core-engine audit), not `SC` specifically, since this doc's Argue-pool floor (Attribute≥1×2 + History-bonus-min-3 = 5) already guarantees a nontrivial minimum pool for a completely untrained orator without a named exception rule |
| 13 | Circles and Resources (social/economic resolution systems) | **ALTERED (present under different naming)** | The literal "Circles/Resources" pool-base terminology survives only as a stale pointer in the doc's own "Propagation required on approval" table (§12, referencing a deprecated `compilation/v0.14/` doc) — not a live mechanic in this doc. Its functional role is filled by Coalition Structure (§9.2), Corroboration (§4 Step 2b), Findings citation (§9.1), and Faction Boost (§2 Step 3) — social/institutional leverage systems that are live and mechanical, just not named "Circles/Resources." No action needed; this reads as intentional terminology evolution (PP-234-era rename sweep), not an unaddressed gap |

## P-01 / P-14 (Inseparability / co-movement) cross-check

Per this repo's Philosophical Foundations constraints (`canon/02_canon_constraints.md`), every Thread
operation must fire all three co-movement dimensions. Social contest's Thread-adjacent surfaces were
checked against this:

- **§9.3 Practitioner Weaving** and **§9.4 Thread Operations Between Exchanges**: both route through
  the corpus-canonical PP-351 temporal-axis-conflict mechanism, which explicitly "preserves P-14"
  (§9.4 L555, L558) by converting temporal dissonance into Persuasion Track shift rather than omitting
  the consequence. **PRESENT.**
- **§9.4b Adjudicator Thread Response**: ties Thread visibility to observer TS bands and fires
  Certainty-indexed institutional consequences (Heresy Investigation, procedural Ob, Conviction Scar
  checks) — this is the epistemic/actual co-movement channel firing correctly for a *third-party*
  witness case, which is a genuine and well-specified extension. **PRESENT.**
- No contest mechanic was found that allows a Thread operation to resolve inside a contest scene without
  a co-movement consequence.

## Summary

No ABSENT findings rise to P1/P2 severity requiring an ED filing from this lane. Principle 12
(Beginner's Luck) is the one clean ABSENT, but it reads as a possible corpus-wide/core-engine gap rather
than a social-contest-specific defect, and the doc's own pool-floor arithmetic already prevents the
practical failure mode (a literally-zero pool) the principle exists to guard against. Principles 5, 6,
11, and 13 are ALTERED but each carries a traceable, ratified justification (ED-1084, PP-716/ED-892,
intentional exchange-structure adaptation, and PP-234-era terminology evolution respectively) — none of
these read as an unauthorized drift from Foundations.
