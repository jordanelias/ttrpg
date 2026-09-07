# §10 — Canon Constraints

**Status:** PROPOSED
**Owns:** P-01…P-15, regenerated against this suite's numbering
**Sources:** C P-01…P-15

---

**What changed and why.** Every constraint's Foundations Ref was verified against the section it cites.
Several cited sections that do not exist, or whose content contradicts the constraint. Those are fixed
here and each fix is noted. Three structural changes:

- **Numbers are out.** A constraint may require that an effect be Coherence-indexed or
  sensitivity-gated; it may not name a threshold. No foundational premise yields a magnitude, and a
  foundations document asserting one is asserting what it cannot derive.
- **GD-1…GD-3 are not reproduced.** They are mutable game-design directives about victory conditions,
  AI action selection and faction emergence. They cite no foundation and the source file itself
  separates them as a different kind of thing. They belong in their own file.
- **Violation tests are kept**, because a constraint that cannot be failed is not a constraint.

---

| ID | Constraint | Ref | Violation test |
|---|---|---|---|
| **P-01** | **Inseparability.** All three dimensions co-move. Foregrounding is impossible. | §2.6 | Does any mechanic let a thread operation resolve without effects in all three dimensions? → FAIL |
| **P-02** | **Monstrosity is surfeit, not evil.** Monstrous origin is grounded in excess of being; moral-register framing as ontological source is excluded. | §5.1, §1.3 | Does any description frame monstrous origin in moral terms, or fail to ground it in surfeit? → FAIL |
| **P-03** | **Rendering is constitutive, not external.** The rendered world is not separable from the process that constitutes it. Information asymmetry between sensitive and non-sensitive is structural, not cosmetic. | §3.1 | Does any mechanic treat the rendered world as an independent object that consciousness merely observes? → FAIL *(Corrected: the source constraint asserted "GM is the rendering engine." There is no GM; the engine resolves. The metaphysical claim is what binds.)* |
| **P-04** | **Monstrosity is ontological, not moral.** Monstrous beings exceed what the rendering can hold; they are not villains. | §5.1, §5.2 | Does any rule assign moral valence to a monstrous entity as such? → FAIL |
| **P-05** | **The three modes are distinct by layer profile.** Mode 1: no layers, deteriorates. Mode 2: transient organization, an event and not an entity. Mode 3: layer 3 only, self-maintaining. | §4.6 | Are any two modes interchangeable? → FAIL. Is mode 2 treated as an entity? → FAIL |
| **P-06** | **Threadcut beings lack layer 1.** Self-maintenance is deliberate, without ground-spooled accumulation. Coherence does not apply — layer 2 is absent by structure, not degraded. | §4.5, §4.4 | Does any mechanic apply Coherence to a threadcut being, or treat one as organic? → FAIL |
| **P-07** | **The ground has no agency, intention, responsiveness, or direction.** | §1.5 | Does any rule attribute agency, intention or responsiveness to the ground? → FAIL. **Does any rule give spooling a direction — something it "would resume," was "already moving toward," or does "given sufficient time"? → FAIL.** *(The second clause is new and is the one the source suite violated.)* |
| **P-08** | **The epistemic barrier is inertness, not amnesia or suppression.** Non-sensitives can hold thread-level propositions and cannot render them as knowledge. | §5.6 | Does any mechanic let a non-sensitive acquire thread-level competence by study alone? → FAIL. **Does any mechanic make non-sensitives *forget*? → FAIL** *(Corrected: the source constraint was titled "Forgetting" and required instability of retention, directly contradicting the section it cited.)* |
| **P-09** | **Memory operations are messy, costly and detectable.** Pulling displaces the configuration and produces an orphan; the absence is diagnosable; co-movement applies. | §6.7 | Does any mechanic permit clean, undetectable erasure? → FAIL *(Threshold for detection is mechanism, not canon.)* |
| **P-10** | **Coherence indexes commensurability with human-mode being**, across both facings, in all three dimensions. Drift is not moral fall. | §4.3, §7.2 | Does any Coherence mechanic produce effect in only one dimension, treat Coherence as moral standing, use the language of sin or condemnation, or equate Coherence 0 with threadcut status? → FAIL |
| **P-11** | **Temporal Disjunction is universal across operations.** Every operation produces some. | §2.7 | Does any operation produce zero temporal consequence? → FAIL *(Open: whether layer-two self-rendering counts as an operation, and so whether there is a non-zero baseline in ordinary life. See supplement R-6. Until ruled, this constraint binds operations in the §6.1 sense only.)* |
| **P-12** | **Drift propagates tridimensionally through knots**, and through two distinct channels: presence-based rendering, and distance-independent knots. | §7.3 | Does propagation occur in only one dimension, or as a single generic strain value? → FAIL. Does the system treat knot-propagation as requiring co-presence? → FAIL *(New clause; the derived channel is distance-independent.)* |
| **P-13** | **Ontological knowledge is not transmissible as propositional content.** What transmits is the form of attention. | §5.7 | Does any mechanic let thread-level understanding transfer as information? → FAIL *(Corrected: the source constraint cited a section on threadcut beings, which says nothing about knowledge, and framed the rule as forgetting. Merged with P-08's true content.)* |
| **P-14** | **Every play mode expresses inseparability.** Co-movement cannot be omitted in any mode. | §2.6 | Does any mode allow an operation without three-dimensional co-movement? → FAIL *(Corrected: the source cited §21.1 and §22.2 of a document with eighteen sections.)* |
| **P-15** | **Three-layer being-persistence.** The Leap suspends the reflexive facing; Coherence 0 is layer-2 failure; what follows is gated by perceptual reach. | §4.1, §6.2, §7.6 | Does any mechanic allow Coherence 0 with no consequence? → FAIL. Does any rule treat deep-reach and shallow-reach Coherence 0 as identical? → FAIL. **Does any mechanic treat the Leap as uniformly risky regardless of environment and operation type? → FAIL** *(Corrected: the source constraint required a uniform "vulnerability window," which contradicted the zero-cost restorative claim in a sibling document. §6.8 resolves this: the window is real, and its magnitude is environment × duration plus type × scale.)* |

---

## Constraints the source suite carried that are not reproduced

- **The condensed A-rule set (A1–A15).** Not migrated. It was a third hand-written restatement of a
  doctrine already stated twice, and it introduced two of the suite's worst drifts: a second, unrelated
  referent for *Providence*, and the claim that what came through the tear were threadcut beings. It
  also restated the Locked Zones epistemically, contradicting the substrate-side account. A condensed
  rule set that changed the claims it condensed is worse than none. If a loadable summary is wanted,
  generate it from this table plus section headers rather than writing it by hand.
- **GD-1…GD-3.** Mutable game-design canon; see the note above.
- **The Level-4 hook table.** Every row was marked provisional and pending. Enforcement status is not
  foundations material.
