[PROVISIONAL: Solmund throughlines appendix — 5 throughlines (T-A through T-E placeholders) plus implementation priorities. Pending Jordan integration into canonical throughlines_meta_infill.md table format with real T-NN numbers and parent_meta (М-NN) assignments. Source: atoms_pending/2026-04-25/_consolidated/02_solmund_cultural_guide.md PART 8.]

# Solmund Throughlines — Appendix (PROVISIONAL)

**Generated:** 2026-04-25 — Stage 4 follow-up.
**Status:** PROVISIONAL — placeholder T-A..T-E names await canonical T-NN assignment + parent_meta (М-NN) mapping.
**Resolves:** conflict-eval finding MEDIUM-03 (PART 8 append did not use canonical throughlines_meta_infill table format).

## Why this is a separate file

The 5 throughlines below name distinct themes that need integration into `references/throughlines_meta_infill.md`'s canonical table (`| T-NN | name | parent_meta | secondary | description |`). Doing so requires:

1. Assigning real T-NN numbers (next available in the canonical sequence).
2. Mapping each to a parent meta-throughline (М-NN) — editorial call requiring familiarity with the meta-throughline taxonomy.
3. Filling secondary-field metadata.

Until those editorial decisions are made, the content lives here as a discoverable appendix without polluting the canonical table.

---

---

## Original PART 8 content

[PROVISIONAL] Source: atoms_pending/2026-04-25/_consolidated/02_solmund_cultural_guide.md PART 8 (atoms 30, 31). Pending Jordan review before integration into canonical throughlines table.

<!-- atom: solmund_master_document__30__27-five-throughlines | source_section: "27. Five Throughlines" -->

## 27. Five Throughlines

**T-A: Perceptual Prophylaxis as Literary Engine.** The Church's essentialist theology generates the entire literary landscape because non-practitioners must use language to point toward what they cannot perceive. Every register is differentiated by perceptual access. Connects to: Thread Revelation Curve, Certainty track, SA stat, Discovery Event arcs.

**T-B: Seam Texts as Mechanical Objects.** Same text, comprehension-gated by TS via P-08. Maps to POI Remnant category. Connects to: POI discovery, fieldwork Survey, SA increments, character formation.

**T-C: Double Consciousness Spiral.** Mending effects simultaneously read as Einhir practice, Solmund miracle, and divine-right confirmation. Three factions, three frames, the incompatibility IS the gameplay. Connects to: faction AI, Conviction Track, Tension Cards.

**T-D: Baralta as Accidental Prophylaxis Cracker.** Her direct-communion theology weakens the perceptual stance the Church's essentialism forecloses. She is closer to metaphysical truth than the Church, for wrong reasons. Effect is generational, not in-game mechanical. Connects to: narrative positioning, long-term consequence framing.

**T-E: The Solmund Repetition.** Extraordinary threadwork → non-practitioners interpret as miracle → institution captures interpretation → interpretation suppresses practice. The Church is reliving its founding error. The recursion stops only when the prophylaxis cracks. Connects to: emergent arc design, whether players can break the cycle.

<!-- atom: solmund_master_document__31__28-implementation-priorities | source_section: "28. Implementation Priorities" -->

## 28. Implementation Priorities

**Immediate (content authoring, no mechanical changes):**
- 10-15 Seam Texts as POI content objects. Each uses a structural pattern from §17. Each contains a seam comprehensible at TS 30+. Place in T2 Kronmark, T9 Himmelenger, T14 Ehrenfeld.
- 5-8 loadscreen aphorisms using the Cusan Triad pattern (§17.1).
- 3-5 folk songs (Levertov register) for Feldmark and Stillhelm territories.
- Settlement flavour text keyed to controlling faction's Certainty baseline (Church territories: 5, Varfell: 3-4, Crown heartland: 4, Hafenmark: 4).

**Short-term (requires editorial decisions):**
- If Baralta direct communion accepted → update NPC analysis §6.
- If two witness traditions accepted → update worldbuilding_v30 with new §3.7.
- Write faction response scenarios for Miraculous Event: Church (miracle proclamation → investigation), Crown/Baralta (divine right confirmation → resource allocation), Restoration (vindication → demand for credit), Hafenmark (constitutional procedure → sovereignty dispute).

**Medium-term (requires mechanical work):**
- Implement Seam Text comprehension-gate in Godot (annotation layer at TS ≥ 30, not hidden content).
- Design Miraculous Event → faction response cascade as arc trigger.
- NPC priority tree branches for Southernmost Contact Decision Events.

---

# APPENDIX A: RESOLVED AUDIT FINDINGS

All findings from the original critical review have been resolved inline in this document.

| Finding | Issue | Resolution |
|---|---|---|
| 1 (P-07) | Ground agency attribution | §10.2 — all language reframed as phenomenological rendering |
| 2 | Solmund ≠ Ein Sof | §10.1 — "from the ground" not "is the ground" |
| 3 | Interiority overclaimed | §10.1 — choice retained, purpose/awareness stripped |
| 4 | Tsimtsum overloaded | §10.1 — analogy not identity |
| 5 | Levinasian face misapplied | §9 — Levinas removed from Solmund |
| 6 | Emergence/choice conflated | §10.1 — distinguished; both readings noted |
| 7 | Suppression overstated | §11 header — flagged as proposed extrapolation |
| 8 | Invented specificity | §11.2 — "perhaps numbering in the dozens" (hedged) |
| 9 | Seam Text | Clean — no fix needed (now refined per N-1) |
| 10 | "Empirically" → "structurally" | Not present in this version |
| N-1 | Seam Text wrong canon ref | §12 — P-08 comprehension gate, not visibility table |
| N-2 | Miracle Investigation Ob flat | §22.1 — scaled: Mandate vs Ob = floor(controller SA / 2) + 1 |
| N-3 | RDT prerequisites omitted | §22.2 — prerequisites explicitly stated |
| S-1 | Lurianic mapping P-07 risk | §4.4 — framed as RM theology, not mechanical description |
| S-2 | Levinasian monstrous encounter | §9 — reframed as structural necessity, not ethical demand |
| B-1 | Ficinian Cardinal emanation | §3.2 — flagged as proposed, not derived |
| B-2 | Teresian frame incomplete | §3.4 — prophylaxis role explicitly stated |
| B-3 | Certainty 6+ qualification | §2.3 — rare bypass requirement noted |

# APPENDIX B: OPEN EDITORIAL ITEMS

| Item | Decision Needed | Blocks |
|---|---|---|
| Baralta direct communion | Supplement or supersede "does not question theology"? | NPC analysis §6, Baralta AI, Southernmost engagement |
| Two witness traditions | Accept as canon extension or extrapolation only? | Seam Text implementation, worldbuilding update |
| Ficinian Cardinal emanation | Accept as proposed Church self-understanding or remove? | §3.2 |
| Miraculous Event trigger | Accept proposed mechanic? | Southernmost engagement pathway |
| Miracle Investigation action | Accept proposed action? | Church Southernmost response |
| SA-gated faction actions | Accept thresholds? | All faction engagement |
| Miraculous Event → Accord +1 | Accept? | Settlement-scale effects |
| Miraculous Event → Proximity Rating −1 | Accept? | Territory-scale RS interaction |
| Conviction mechanic for Miraculous Event | Accept Cognition vs Ob = Certainty? | Personal-scale effects |

---

*End of master document. All content PROVISIONAL. No existing canonical files modified. Nine editorial items pending.*