# Venue Behaviors — emergent outcomes validated by precedent

Bottom-up: read the emergent behavior of the venue-determined win-conditions, venue-faults, and
panels straight from the primitives (sim). Top-down: check each against the institution it models.
Covers what the earlier historical validation did not (the win-conditions are new). One over-tuned
case found and corrected.

## Tribunal — ProofBar = presumption of innocence + burden of proof  ✓
Emergent (prosecution A vs defence B): a **competent rebuttal acquits** (equal skill → acquittal 1.00 — reasonable doubt), a **defence that fails to rebut is convicted** (passive defence → conviction 0.97), and the **bar is the standard-of-proof dial** (bar 4 ≈ beyond-reasonable-doubt, hard to convict; bar 2 + a skill gap → conviction 0.56 ≈ preponderance). Validates against the core of adversarial procedure: the defender prevails on doubt, conviction requires the case to stand unrebutted, and the burden is a tunable height. (My first read — "the prosecution never wins" — was an artifact of testing only against an equally-competent defence, which *should* acquit.) **No change.**

## Assembly — TallyAtClose = the majority vote  ✓
Emergent (orators in a pathos venue): the **stronger orator carries the vote** (faculty 7 vs 4 → 0.63 vs 0.19), an **equal contest is a coin-flip**, and **tied votes occur** (~12–18%). Validates against deliberative practice — the body decides by majority, the better speaker wins it, and a tie is a real outcome (the motion fails / a casting vote). **No change** (the tied-vote rate is a minor discrete-increment artifact, reducible with a tiebreak).

## Appeal — GraceThreshold = the sovereign's discretion  ✓ (corrected)
Emergent **before** the fix: grace granted ~0.95 regardless of the sovereign — the institutional ethos-role swamped the person. That is historically wrong: supplications were discretionary and often denied. **Fix (bottom-up, prompted by the mismatch):** a petition has no institutional proof-weighting — it is a personal plea judged by the sovereign's *character* (resonance comes from the sovereign via leak) — and grace is not automatic (higher bar). Emergent **after**: **sympathetic sovereign grants (0.96), neutral is a coin-flip (0.54), stern denies (0.00)**. Validates against the supplique/remontrance: grace is the sovereign's personal mercy, responsive to disposition, freely refusable.

## Venue-varying defeat-conditions = institution-specific faults  ✓
Emergent: the **same** off-ground dodge is **fatal in a disputation** (clinch:evasion 1.00) but **harmless in a petition** (0.00 — evasion disabled there). Validates the corpus's point that the fault set is institutional: dodging the question loses a debate or a trial (a *nigrahāsthana*), but a petition is judged on deference, not on holding a stasis ground — so "evasion" is not its fatal fault.

## Panels — collective adjudication reflects composition  ✓
Emergent (logos vs pathos before a bench): a **logos-packed panel** decides for logos (`[L,L,Pj]` → 0.95), a **pathos-packed panel** flips it (`[L,Pj,Pj]` → pathos 0.88), a single matching judge is the most decisive. Validates against jury/bench reality — a packed panel skews, a mixed panel moderates; composition is the lever.

## Bottom line
The venue-determined win-conditions and faults **reproduce the documented behavior of each institution** — presumption of innocence and burden of proof in the tribunal, the majority vote in the assembly, discretionary grace in the petition, institution-specific faults, and composition-driven panels. The one over-tuned case (grace) was corrected by the same bottom-up/top-down loop: the emergent behavior diverged from the institution, and the primitive weighting was adjusted until it matched. Structure and emergence both hold against precedent.
