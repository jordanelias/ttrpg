---
atom_id: valoria_session_2026_04_25_master_consolidation__03__3-pre-work-contamination-surface-canon-tier
source_file: valoria_session_2026_04_25_master_consolidation.md
source_section: "3. Pre-Work Contamination Surface (canon/ tier)"
section_index: 3
total_sections: 15
line_count: 53
char_count: 2816
source_sha256: 4c4672049317ec8e
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## 3. Pre-Work Contamination Surface (canon/ tier)

Word-boundary scan (avoiding "Certainty"-style substring false positives) found 16 contaminated lines across 4 canon docs:

### `canon/02_canon_constraints.md` — 4 lines, highest severity

| Line | Severity | Term(s) | Function |
|---|---|---|---|
| L11 | S3 (negation) | `corruption` | P-02 enforcement clause: "must not imply evil, corruption, or negativity..." |
| L15 | S1 (structural) | `Taint` | P-06: "Taint track does not apply" — names the mechanic |
| L19 | S1+S3 | `Taint`, `corrupts`, `Epistemic seduction` | **P-10 itself** — the principle was *named* "Epistemic seduction." Self-referential censorship: forbade "language of corruption" while naming the mechanic "Taint." |
| L21 | S1 | `Taint` (×2) | P-12: "Knot strain mechanics... Patch O: +1 strain/season on Close Knots at Taint 4–6" |

### `canon/00_philosophical_foundations_rules.md` — 4 lines

A11 (axiom heading), C4 (constraint heading), B-table glossary row, D enforcement-line — all named "Epistemic Seduction" structurally.

### `canon/00_philosophical_foundations.md` — 7 lines

§16.1 section title, §19.4 section title, plus 5 body-prose definitional uses across §16.1, §16.3, §19.4, §22.1, and Appendix A row 6.3.

### `canon/01_foundations_amendment_self_rendering.md` — 1 line

L50 cross-reference: "The epistemic seduction described in §16.1..."

### Severity classification

- **S1 (Structural)** — the term *names* a canonical principle, axiom, or mechanic. Replacement requires a new concept name and propagates through all citations.
- **S2 (Doctrinal body text)** — body prose using censured term to define or explain canon. Editorial rewrite needed.
- **S3 (Negation prose)** — "must not be X / not a X mechanic" — using term to forbid it. Easy rephrase, no concept replacement needed.

### Cross-file dependency map (resolved)

```
canon/00_philosophical_foundations.md
  §16.1 "Epistemic Seduction"  → renamed §16.1 "Coherence as the Integrity of Layer-Two Self-Rendering"
  §19.4 "Epistemic Seduction Curve"  → DELETED (Part Nine entirely removed)
       ↑ cited by ↓
canon/00_philosophical_foundations_rules.md
  A11 "Epistemic Seduction"  → renamed A11 "Drift From Human-Mode Being"
  C4  "Epistemic Seduction"  → renamed C4 "Drift Mechanics"
       ↑ cited by ↓
canon/02_canon_constraints.md
  P-06 referenced "Taint track"  → references "Coherence" (layer-2 absence for threadcut)
  P-10 named "Epistemic seduction" + "Taint track must not... corruption"  → rewritten as Coherence-commensurability
  P-12 referenced "Taint 4–6"  → rewritten as tridimensional drift propagation
       ↑ cited by ↓
canon/01_foundations_amendment_self_rendering.md (§16.1 cross-ref)  → updated
[+ ~30 design files cite Taint track / A11 / P-10]  → DEFERRED to design-tier sweep
```

---
