---
atom_id: valoria_master_consolidation__11__4-3-literal-rendering-per-character-visual-filteri
source_file: valoria_master_consolidation.md
source_section: "4.3 Literal Rendering + Per-Character Visual Filtering"
section_index: 11
total_sections: 40
line_count: 27
char_count: 2480
source_sha256: bdc7567069649c60
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## 4.3 Literal Rendering + Per-Character Visual Filtering

**The gap.** Foundations Part Nine §22.1 specifies:

> "The video game format's unique advantage: the rendering can be made literal. The game's visual presentation of the world is the rendering. As a character's thread sensitivity increases, the visual layer changes... This is not a UI overlay; it is a change in how the world looks."

`valoria_holistic_audit.md` Risk M-1 flags this as unresolved. The current videogame spec does not address it.

**The proposal.** Godot rendering pipeline presents the world differently based on viewing character's Thread Sensitivity and Certainty. The world has no observer-independent visual state; it has thread-substrate filtered through observer's perceptual architecture.

| Observer state | World presentation |
|---|---|
| TS 0, Certainty 5 | Fully ontical. Orthodox visual language. Anomalies interpreted through character's framework (weather, illness, bad luck). |
| TS 10–30, Certainty 3–4 | Occasional anomalies visible. Edges fuzz. Patterns the character notices but can't identify. |
| TS 30–50, Certainty 1–3 | Thread structures occasionally visible beneath surfaces. Knot connections faintly shimmer. |
| TS 50–80, Certainty 0–1 | Thread structures persistently visible. Dual perception: rendering layer + ontological layer. |
| TS 80+ | Ontical surface appears flat, artificial. Thread-level dominates. Real world looks like projection. |

RS band also modulates presentation, filtered through observer TS. A TS 0 character in RS 30 territory sees bad weather and dying crops. A TS 50 character in the same territory sees threads straining, substrate thinning, configurations oscillating. At RS 0 (Rupture), presentation breaks for all observers regardless of TS.

TC drives territorial transformation as Church-aligned territories visually transform across bands. IP drives peninsula atmosphere (Altonian cultural infiltration).

**Refinement from check.** "Most important foundations-compliance commitment not yet addressed" — not "single most important technical commitment." Implementation requires #4.7 (confrontation-only TS) finalized first; the TS bands assume character acquired TS through confrontation, not lifepath.

**Tier N status.** Exempt — foundations §22.1 compliance, not new mechanic.
**Foundations grounding.** A6 (rendering = consciousness-performed), P-03 (rendering = consciousness-performed), §22.1 (literal rendering), Risk M-1 resolution.
