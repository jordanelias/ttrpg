# MECHANIC AUDIT — Simulation Finding Patch Specifications
**Date:** 2026-03-27  
**Mode:** D (Gap Detection — targeted)  
**Scope:** SIM-F-01, SIM-F-06, SIM-F-07, SIM-F-08, SIM-F-09  
**Source:** designs/threadweaving_redesign_v25.md (post-patch)  

---

## PATCH SPEC: SIM-F-01 — Coherence Cliff Warning + Drop Cap

**Finding:** Practitioner can lose 5 Coherence in a single scene with no warning. Additionally: editorial decision received — Coherence loss from a single operation failure capped at −1.

**Two changes required:**

### Change 1: §3.2 — Degree table Coherence cost cap

Current text in §3.2 interaction with degree tables:
> "At Object/Personal scale: ignore degree-table Coherence costs on Partial results... Apply degree-table Coherence costs on Failure. At Relational+ scale: apply all degree-table Coherence costs as written."

Degree tables currently list:
- Weaving Partial: Coherence −1
- Weaving Failure: (no explicit Coherence cost beyond scale auto-effect)
- Lock Partial: Coherence −2
- Lock Failure: Coherence −2
- Dissolution Partial: Coherence −2
- Dissolution Failure: Coherence −2
- Mending Partial: Coherence −2 (already patched: base + partial outcome)
- Mending Failure: Coherence −2 (already patched: base + failure outcome)

**Patch:** Add the following sentence to §3.2 after the scale-based interaction paragraph:

> **Coherence loss cap per operation:** Regardless of scale, degree table outcomes, combined auto-effects, or bonus costs (FR, residue, Past-Oriented Pulling), a single operation — from Leap through resolution — cannot reduce Coherence by more than 1. All Coherence costs from a single operation are treated as a single event and capped at −1 total. Multiple operations in a single contact window are each capped independently.

**Ripple effects — degree table entries to update:**
- §2.7 Lock Partial: "Coherence −2" → "Coherence −1 (cap)"
- §2.7 Lock Failure: "Coherence −2" → "Coherence −1 (cap)"  
- §2.8 Dissolution Partial: "Coherence −2" → "Coherence −1 (cap)"
- §2.8 Dissolution Failure: "Coherence −2" → "Coherence −1 (cap)"
- §2.6 Mending Partial: "Coherence −2 (base + additional from partial outcome)" → "Coherence −1 (cap)"
- §2.6 Mending Failure: "Coherence −2 (base + additional from failure)" → "Coherence −1 (cap)"

**Note on campaign pacing:** The cap does not reduce long-term Coherence pressure — it distributes it. A practitioner who performs 3 operations in a contact window still loses up to −3 total (−1 per operation). The cliff risk is eliminated; the cumulative arc is preserved.

### Change 2: §3.3 — GM warning at Dissonant threshold entry

Add the following to the Dissonant row in the §3.3 threshold table, as a new paragraph after the table:

> **GM protocol — Dissonant entry:** When a practitioner's Coherence drops to 7 (entering Dissonant), the GM names this to the player explicitly: "Your Coherence is now 7 — Dissonant. Each operation at Relational+ scale costs −1 Coherence. At this pace, Fragmented is [N] operations away." This is not a mechanical rule; it is a table protocol. The practitioner's rendering is still solid at Dissonant — but the player should make informed decisions about scale from this point forward.

---

## PATCH SPEC: SIM-F-06 — Over-Actualisation Brittleness GM Sidebar

**Finding:** P-18 (Brittleness) can produce worse outcomes than not Weaving. Players need explicit warning.

**Location:** §2.4 Weaving, after the Over-Actualisation Hazard table.

**Add:**

> **GM sidebar — Brittleness in volatile contexts:** Weaving at Relational+ scale stabilises a configuration but makes it rigid. A Woven diplomatic agreement, stabilised faction, or reinforced institution cannot adapt to stress the way an unworked configuration can. If a non-Thread event of sufficient severity strikes a Woven configuration — a siege, betrayal, institutional collapse — the GM may rule it shatters into a Shifting Object at its scale rather than simply failing. A broken Woven treaty may become a Relational Shifting Object (deteriorating to a Relational Gap within 1d3 seasons) rather than just a broken treaty.
>
> Before Weaving in a politically volatile context, the GM should ask: is this configuration likely to face severe stress before it can be Pulled or allowed to expire naturally? If yes, Weaving may be counterproductive. The practitioner cannot know this during Diagnosis — brittleness is a consequence of over-actualisation that manifests only when external stress arrives.

---

## PATCH SPEC: SIM-F-07 — Wound During Leap Round Timing

**Finding:** Interaction between Wound penalty and disruption check during the Leap round is ambiguous.

**Location:** §2.3 The Leap, Contact Duration subsection — add after the Wound disruption paragraph:

Current text:
> "When the practitioner takes a Wound while contact is established, make an Attunement check immediately..."

**Add clarifying sentence before this paragraph:**

> **Wound during the Leap round (before contact is established):** If the practitioner takes a Wound in the same round as the Leap roll, before the roll is resolved, apply +1 Ob to the Leap roll as normal (Wound penalty). The Attunement disruption check does not apply — it only triggers once contact is established. If the Leap succeeds despite the Wound penalty, contact proceeds normally.

---

## PATCH SPEC: SIM-F-08 — Mid-Sequence Configuration Change

**Finding:** No rule for a configuration changing between Diagnosis and Leap.

**Location:** §2.2 Diagnosis, end of section — add:

> **Configuration change after Diagnosis:** If the target configuration changes significantly between Diagnosis and the Leap — a Gap opens at the site, the target dies, another practitioner Locks or Dissolves the thread — the practitioner may revise their declared intentionality before the Leap roll at no cost. They have not yet suspended rendering; revision is possible.
>
> If the practitioner proceeds with the original intentionality against the altered configuration without revising: treat as skipping Diagnosis for that operation (+2 Ob, automatic Gap creation on Failure for FR operations). Their intentionality was formed for a state that no longer exists.

---

## PATCH SPEC: SIM-F-09 — P-19 Integration Verification

**Finding:** P-19 (Mending epistemic co-movement by degree) exists only in the Part Nine patch log. Needs integration into §2.6 main text.

**Location:** §2.6 Mending, co-movement profile subsection.

Current text:
> *Epistemic auto-effect:* Observers with TS 10+ perceive a settling. Non-sensitives may notice an easing of tension they couldn't articulate. No investigation Ob modifiers — Mending resolves epistemic instability rather than producing it.

**Replace with:**

> *Epistemic auto-effect (by degree):*
>
> | Degree | Epistemic Effect |
> |---|---|
> | Overwhelming | Strong settling. TS 10+ observers perceive the area as markedly calmer. Non-sensitives notice a distinct easing of tension. |
> | Success | Settling. TS 10+ observers perceive calming. Non-sensitives may notice subtle easing. |
> | Partial | Ambiguous. Observers perceive both settling and tension — something shifted but didn't fully resolve. |
> | Failure | Increased tension. Observers perceive things worsening. Non-sensitives feel heightened unease. The substrate was disturbed without being repaired. |
>
> No investigation Ob modifiers on Success or Overwhelming — Mending resolves epistemic instability rather than producing it. On Partial or Failure: +1 Ob to social rolls in the immediate area for the remainder of the scene (the unresolved disturbance is perceptible).

---

## IMPLEMENTATION ORDER

| Patch | Location | Type | Complexity |
|---|---|---|---|
| SIM-F-01a | §3.2 — add cap paragraph | Insert | Low |
| SIM-F-01b | §2.7 Lock degree table (×2) | Replace | Low |
| SIM-F-01c | §2.8 Dissolution degree table (×2) | Replace | Low |
| SIM-F-01d | §2.6 Mending degree table (×2) | Replace | Low |
| SIM-F-01e | §3.3 — add GM protocol paragraph | Insert | Low |
| SIM-F-06 | §2.4 — add sidebar after OA table | Insert | Low |
| SIM-F-07 | §2.3 — add clarifying sentence | Insert | Low |
| SIM-F-08 | §2.2 — add end-of-section rule | Insert | Low |
| SIM-F-09 | §2.6 — replace epistemic paragraph | Replace | Low |

All patches are text insertions or targeted replacements. No structural changes. Haiku-eligible for mechanical execution once specs confirmed.
