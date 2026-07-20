# Top-Down Validation: the Initiative/Contratempo Design vs the Corpus-Rewrite Evidence Standard

`[READ: /mnt/user-data/uploads/10-corpus-rewrite.md — all 92 lines]`
`[SELF-AUTHORED — bias risk]` This document audits a claim *I* made two turns ago (initiative as a cross-cultural
universal, used to justify the initiative + contratempo + tradition-style design). The corpus-rewrite is, for that
claim, an adversarial reviewer. I am treating it as one and reporting where my own argument fails its standard.

## VERDICT
The corpus-rewrite does **not** supply new combat primitives — it is a methodological self-correction whose explicit
lesson is that manuals are mnemonic and cross-tradition "universals" are mostly selection effects. Its real value
here is as a **top-down check**, and on that check **my earlier cross-cultural-initiative claim partially fails and
must be down-graded.** The engine mechanics do not change; the *justification* and the *tradition-layer scope* do.

## The direct hit (stated plainly, not hidden)
Two turns ago I argued initiative/timing-control is a cross-cultural universal across **eight** traditions and used
that to justify (a) building initiative as a culture-neutral universal and (b) giving the tradition layer per-culture
initiative-*style* profiles. The corpus-rewrite §3(i) says, in as many words:

  *"Counterattack is the prestigious mode across traditions" is a projection from three well-documented traditions
  (German, Italian, Japanese)… Retained only as a European/Japanese observation.*

That is the **same selection effect**, and my evidence had the same shape the document diagnoses:
- My three high-confidence anchors were **German, Italian, Japanese** — exactly the three the document names as the
  projection's source.
- My Polish / Persian / Indian "confirmations" were **S4/S5-tier** web searches — exactly the traditions the document
  says had "high grades **not earned**." My own confidence ladder already flagged them medium/low; the document
  explains *why* that matters: a claim's grade cannot exceed its best source, and S4/S5 cannot anchor a universal.
- I called the convergence "the same kind of finding as cross-cultural spear-primacy." The document's meta-lesson is
  that this move — pattern-in-the-best-documented projected onto all — is **the corpus's recurring error**, not a
  validation.

**Correction:** "initiative/Vor-Nach-Indes is a cross-cultural universal" is **down-graded to a European/Japanese
observation** (S2-supported for those three; unproven elsewhere). I overstated it. The honest version is narrower and
I should have reached for the field literature before claiming eight-tradition convergence from 3 strong + 5 thin.

## What survives, and what it means for the design (mechanics unchanged)
The down-grade changes scope and naming discipline, not the engine:

1. **The initiative primitive itself still stands — but on different grounds.** Its warrant is no longer "every
   tradition has it." It is (i) S2-solid for the European+Japanese material the *player-facing* game most draws on,
   and (ii) a *mechanically* necessary state regardless of cultural universality — the engine needs a persistent
   "who is dictating" variable to model the parry-with-threat and single-time counter we already validated against
   the German/Italian record. Build it; justify it as European/Japanese-anchored + mechanically required, **not** as
   a human universal.

2. **The tradition-style profiles must be RE-SCOPED to their evidence tier.** Two turns ago I proposed five concrete
   per-tradition initiative styles (German seize-first, Japanese counter-steal, Spanish measured, Polish
   close-under-the-cut, Persian break-measure). Under the document's rule:
   - **German, Italian, Japanese, Iberian/destreza** styles are S2-anchored → keep as distinct profiles.
   - **Polish, Persian, Indian** styles were S4/S5 → **do not encode them as distinct, evidence-claiming profiles.**
     Either fold them into the nearest S2 profile or mark them explicitly `[S4/S5 — speculative, not evidence-backed]`
     so the game does not present an unearned cultural claim as canonical. (This matches the project's own
     "claim cannot exceed its source" discipline.)

3. **"Contratempo is prestigious" must not be hard-coded as a universal reward.** If the engine rewards the
   counter-in-tempo as the high-skill mode, that reward should read as European/Japanese flavour (tradition-weighted),
   **not** a global "counterattack is best" rule baked into the resolver. The single-time counter can exist mechanically
   for everyone (it is a real option), but its *prestige/weighting* is cultural and belongs in the tradition layer.

## A genuinely new validation lever the document DOES provide
The document is right that the corpus omits a **physical/forensic stream** and that this is the one evidence type that
can test what manuals *claim* against what bodies and blades show. This is directly usable as a **top-down validator
for the engine's emergent output** — an axis I have not used:

- **Osteological trauma datasets** (the document names **Towton 1461**; also Visby 1361, Sandbjerget, Wisby mass
  graves) record *where* and *with what* people were actually killed/wounded — blade vs blunt, location distribution,
  perimortem sharp-force vs depressed-fracture ratios. The engine produces an emergent wound/lethality profile
  (which heads land, cut-vs-thrust-vs-percussion, vs which armour). **These can be cross-checked against the
  osteology**: e.g., Towton shows a high proportion of blade trauma to the head/face and many wounds per individual —
  does the engine's emergent blade-to-head and blow-count distribution sit in the same regime? This is a real,
  matrix-independent, historically-grounded validation the engine has never been run against.
- **Metallurgical/typological evidence** (Williams, *The Knight and the Blast Furnace*) on armour hardness and
  penetration is a check on the `armor_defeat` and `coupling` magnitudes specifically — does the engine's
  cut-collapse / thrust-finds-gap / percussion-defeats-plate rotation match measured penetration thresholds?

These are the document's actual contribution to the engine: not new primitives, but a **third validation leg**
(forensic) alongside the emergent-behaviour and (demoted) matrix legs — exactly the "integrate the forensic stream"
move the document's §5(3) names as one of the few routes to a non-derivative result.

## RECOMMENDATION (worst-first)
1. **Down-grade the initiative-universality claim in the design record** to European/Japanese (+ mechanical
   necessity). Re-scope the tradition-style profiles to S2 (German/Italian/Japanese/Iberian) and mark Polish/Persian/
   Indian speculative. Keep the *mechanic*; fix the *justification and the cultural claims*. **No code change to the
   resolver** — this is design-record + tradition-layer scoping.
2. **When initiative ships**, keep the single-time counter available to all but put its *prestige weighting* in the
   tradition layer (European/Japanese), not the core — so the engine does not bake a demoted universal into the spine.
3. **Add the forensic validation leg**: source one osteological dataset (Towton 1461 is the named anchor) and run the
   engine's emergent wound profile against it as a top-down check, independent of the matrix. This is the highest-value
   *new* validation the document unlocks.

`[CONFIDENCE: high on the self-correction — the document names the exact selection effect my claim exhibited, and my
own evidence tiers (3×S2 + 3×S4/S5) match its diagnosis. Medium on the forensic-leg proposal's feasibility until a
specific dataset is located and its granularity checked against what the engine emits.]`
`[SOURCE: the corpus-rewrite is itself S2-anchored (Wetzler 2015/2016, Anglo 2000, al-Sarraf 2004, Elias & Dunning
1986 — verified-in-search per its doc 08); the osteology anchors (Towton) are S2-expected pending direct check.]`
