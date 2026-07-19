# Self-Audit: Cascade Analysis on Proposed Mechanics
**Date:** 2026-05-08 · **Context:** Jordan flagged over-engineering after 4 turns of additive proposals.

---

## The cascade I was building toward

Counting what I proposed across the last three turns:

- Reaction-shape library: 65 author-decisions
- Per-Conviction invocation effects: 13 entries
- Per-history content-access spec: ~120 unlocks
- 20 languages × Read/Speak/Write = 60 boolean states
- 15 knowledge domains
- 25 explicit competencies
- 3 history-acquisition pathways
- Per-territory reputation grid (15+ territories)
- Drift visualization
- Per-NPC speech registers
- Tier-3 texture floor

On top of: 13 Convictions, 8 cultural templates, 4 Resonant Styles, 4 metaphysical axes (TS/Coherence/Spirit/Certainty), 4-axis Conviction substrate, 1–3 Beliefs per NPC, Self-Other, attribute pools (Mind/Body/Spirit + Cognition/Focus/Endurance/Charisma/Bonds), Lifepath history, history-derived skills (level 0–3), Knots, Standing per faction, Belief Scars, Piety Track Scars, Coherence track, Certainty track.

This is the failure mode I should have caught: **specificity is locally elegant, cumulatively crushing.** Each addition was defensible against the previous baseline. None was audited against the cumulative weight.

---

## The cognitive-load test (what actually matters)

The right metric isn't "how many systems exist." It's **how many distinct things the player must consult to make a single decision.**

**Scene model:** PC in a Hafenmark merchant's office, extracting information about a smuggling rival.

Under everything I proposed, the player consults, before choosing a dialogue option:

1. Which Conviction-voice intrudes (2–4 speak — must triage)
2. Conviction transgression cost preview (Honor Scar risk if I lie)
3. Conviction invocation availability (burn a Faith use here?)
4. History gate (do I have Hafenmark legal-procedural Latin? Crown Heartland kinship?)
5. Language gate (Hafenmark Latin — Read? Speak?)
6. Knowledge domain (Hafenmark commercial law — do I know it?)
7. Competency level (Rhetoric 2, Stealth 1)
8. Resonant Style of merchant (Evidence / Consequence / Authority / Solidarity?)
9. Belief engagement (does this scene risk a Belief Scar?)
10. Self-Other drift implication
11. Reputation in T8 Gransol (low) and Standing in Guilds (mid) and Standing in Hafenmark (mid)
12. Knot status with merchant's cousin
13. Disposition vs me
14. TS / Coherence / Spirit / Certainty current values
15. Pool composition (Mind 4, Body 3, Spirit 5 + sub-pools)
16. Active skills list (~10 history-derived)
17. Faction Mandate / L+PS for what pressure I can apply

**Seventeen consultations to choose a sentence.** This is unplayable. This is the cascade.

I conflated **system depth** with **per-decision surface.** They are not the same metric, and ignoring the second is how you build Pathfinder 2e accidentally.

---

## NERS on proposed additions (not on canon)

| Proposal | N | E | R | S | Verdict |
|---|---|---|---|---|---|
| Convictions speak (~65 entries) | high | mid | high | **low** | **SCOPE** → 13 base voices + ~5 event archetypes (~25 entries); engine surfaces only 1–2 highest-weight relevant Convictions per scene |
| Per-Conviction invocations | low | mid | mid | mid | **DEFER** |
| Per-history content-access | high | high | high | mid | **SCOPE** → ~5 high-frequency unlocks per history, not 120 small ones |
| 20 languages × R/S/W | **low** | **low** | mid | **low** | **CUT** → reduce to 4–5 binary |
| 15 knowledge domains | low | low | mid | low | **CUT** → reduce to 5–7 or fold into history content-access |
| 25 explicit competencies | **low** | **low** | mid | **low** | **CUT** → use history-skills |
| 3 history-acquisition pathways | high | mid | high | mid | **SCOPE** → single tracker |
| Per-territory reputation | mid | **low** | mid | **low** | **CUT** → extend Standing instead |
| Drift visualization | high | high | high | high | **KEEP** |
| Per-NPC speech register | high | high | high | high | **KEEP** |
| Tier-3 texture floor | high | high | high | high | **KEEP** |

**Cumulative NERS on proposals as posted: N partial-pass, E fails, R high-but-inaccessible, S fails.**

---

## Per-decision surface target

**~5–7 distinct consultations per decision, ceiling.** Anything more is GM-style adjudication offloaded to the player.

Post-cuts, the same merchant scene:

1. Conviction voice (1–2 surface; player chooses which to follow)
2. History gate (yes/no — do I have what I need to attempt this approach)
3. Resonant Style of merchant (engine displays; player chooses argument shape)
4. Belief engagement / Scar risk (binary indicator)
5. Pool to roll (one number)
6. Standing / Disposition modifier (one number)
7. Outcome

Seven, not seventeen. The other ten things still exist in the system — they just don't all need conscious player consultation. The engine handles them silently.

---

## What to actually keep (revised)

**Layer 1 — Personality (interior gate).** Already canonical: Convictions, Beliefs, Self-Other, Resonant Style. New authoring: 13 base Conviction voices + ~5 event archetypes = ~25 reaction-shape entries. Engine surfaces 1–2 relevant Convictions per decision.

**Layer 2 — Competence (exterior gate).** Histories already exist. New authoring: ~5 high-frequency content-access categories per history. Histories acquirable during play via single tracker.

**Layer 3 — Surfacing.** Drift visualization, per-NPC speech registers (Tier 1+2 only), Tier-3 texture floor. Legibility moves, not new mechanics.

**Cut entirely:** Granular language grid, parallel knowledge-domain grid, parallel competency grid, per-territory reputation, Conviction invocations.

---

## The principle, stated cleanly

**Specificity earns its place by what the player consults during a decision, not by what the engine could in principle track.** A videogame can carry deep system count if the per-decision consultation stays small. Any addition that increases the consultation count needs to be auditable against that constraint, not just against local elegance.
