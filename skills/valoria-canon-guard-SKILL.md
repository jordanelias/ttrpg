# valoria-canon-guard

Validate mechanics, rules, or content against the Philosophical Foundations. This skill NEVER approves content that contradicts the Foundations.

**Model:** Sonnet 4.6.
**Input:** Specific mechanic or section — chunked, never full document.
**Requires:** `canon/02_canon_constraints.md` (the canonical constraint file on GitHub)

## Canon Constraints (P-01 through P-14)

| ID | Constraint | Key Test |
|----|-----------|----------|
| P-01 | Inseparability: all three dimensions co-move | Every thread op → mandatory secondary consequences? |
| P-02 | Ein Sof = infinite positive being | Ground framed as fullness, not void/chaos? |
| P-03 | Rendering = consciousness-performed | GM as rendering engine? Information asymmetry mechanical? |
| P-04 | Monstrosity = ontological, not moral | Rendering failures, not evil? |
| P-05 | Three emergence modes mechanically distinct | Modes 1/2/3 have distinct stat blocks? |
| P-06 | Threadcut = is without becoming | Maintained via Thread work? Past-Pull → auto-Gap? No Taint? |
| P-07 | Calamity = rendered-side | TT implies over-drawing, not ground responsiveness? |
| P-08 | Barrier = inaccessibility, not suppression | Knowledge = "religious poetry"? Church reinforces, doesn't cause? |
| P-09 | Memory pulling = messy, costly, detectable | Not clean eraser? Orphaned configurations? |
| P-10 | Epistemic seduction = perceptual shift | Dissolving categories, not corruption? |
| P-11 | TD universal | ALL thread ops produce TD? |
| P-12 | Relational contagion via knotting | Transformation propagates through Knots? |
| P-13 | Forgetting = rendering failure | Southernmost knowledge untransmittable to non-sensitives? |
| P-14 | All modes express inseparability | Co-movement in all play modes? |

## Process
1. Load canon constraints. Load relevant Foundations section.
2. Per applicable constraint: **PASS** / **PARTIAL** (what's missing + severity) / **FAIL** (cite Foundations, explain, propose repair).
3. If repair involves setting/narrative/character: `[EDITORIAL: requires user approval]`.

## Output
```
# Canon Guard Report — [Name]
## Verdict: PASS / PARTIAL / FAIL
| Constraint | Status | Note |
## Violations (if any)
### [ID]: [description]
Foundations ref: · Current implementation: · Why it violates: · Proposed repair: · Editorial flag:
## Summary (1–3 sentences)
```

## Rules
- Philosophy governs mechanics. Never the reverse.
- Mechanically sound but philosophically incoherent = FAIL.
- When uncertain: PARTIAL, not PASS.


## Amendment Integration Workflow

**Trigger:** Any commit touching `canon/00_philosophical_foundations.md` or any `canon/01_*.md` amendment file.

**Protocol:**
1. Read the amendment. Identify new mechanical implications not covered by P-01–P-14.
2. For each new implication: draft a new P-NNN entry in the constraint table format.
3. Update `canon/02_canon_constraints.md` with the new constraint(s).
4. Update version line with date and description of change.
5. Commit: `[editorial] Update P-NNN in canon_constraints — [amendment name]`

**This workflow runs automatically** — the orchestrator invokes it whenever a canon file changes. Canon-guard is always current with the Foundations.

## Read Protocol (updated)

Before any compliance check:
1. Read `canon/02_canon_constraints.md` from GitHub (not from cache — always fetch fresh to get latest P-NNN).
2. Read `references/canonical_sources.yaml` to identify which document is canonical for the system under test.
3. Load the canonical document's params file.
4. Run P-01 through P-15 (or current max) against the mechanic.
