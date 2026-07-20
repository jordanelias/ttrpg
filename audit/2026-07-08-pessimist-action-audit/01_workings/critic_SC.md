# Inverted Critic Pass — Lane SC (Social Contest)

**Role:** independent Sonnet adversarial-saving pass. Read-only. For each dossier action with a
non-KEEP verdict, I attempted the strongest honest case that the action should be KEPT, judged
as-if-built (charter cardinal rule). I also spot-checked several KEEP verdicts and re-audited every
verdict for build-state contamination.

Corpus consulted directly (not just the dossier's characterization): `sim/personal/contest/appraise.py`,
`designs/scene/social_contest_v30.md` §2 Step 3 / §4 Step 1 / §6.1 / §6.1.1, `params/contest.md`
(ED-1060 Terminal Doubt), `params/contest_extensions.md` (PP-636, Stacking §), and the prior
2026-07-04 NERS-audit refutation `refute_four-games-collapse-one-pattern.md`.

---

## 1. Appraise (REFINE, P2) — steelman attempted

**Dossier claim:** channel (a) — the audience/faction-boost read — is "a fully solvable public lookup
a player never needs to roll for," riding alongside a genuinely load-bearing channel (b) (the armature
read, protected by `appraise.py`'s partial-reveal design).

**Steelman for full KEEP:** the Faction→Boost table (social_contest_v30.md §2 Step 3, a 7-row public
table) is not itself the hidden fact — *which faction currently dominates a given audience* could be,
and audience composition is explicitly gated behind "the hidden GM ledger" (§2 Step 7). If dominance is
itself dynamic, unknown, or contested (a mixed Parliament, a Crowd), Appraise is doing real epistemic
work, not looking up a public table.

**Where the steelman fails:** for the 2 of 8 proceedings that are institutionally single-faction by
definition (Church Tribunal → Church always boosts Obscuring; a Royal Audience → Crown always boosts
Revealing), the boost is trivially known from the *proceeding type itself* — no Appraise needed, no
hidden fact to learn. Worse, the design contains an internal contradiction the dossier didn't even need
to invoke: §2 Step 3 states the boost is "fixed at setup — no mid-contest changes," while §4 Step 1
says Appraise "senses the CURRENT state of the audience (which may have shifted...)" — the design
hasn't decided whether this is static or dynamic, which is itself evidence the channel is under-specified
rather than a clean, load-bearing information-uncertainty mechanic across all 8 proceedings.

**Outcome: UPHELD**, with a refinement to the finding itself: the "solved lookup" framing is strongest
for the venue-fixed proceedings (Church Tribunal, Royal Audience) and weaker for multi-faction/Crowd
venues where dominance could be genuinely contested state — the REFINE verdict (split the channels,
keep the armature-read half, tighten or cut the audience-read half) survives, but the docket item should
note the split is proceeding-type-dependent, not uniform.

---

## 2. Recall citation (+2D) / Pre-Contest Prep / Findings citation stacking (REFINE, P2) — steelman attempted

**Dossier claim:** these sources stack outside the genre/audience +2D cap the design enforces elsewhere,
making bonus-accumulation the real governing variable.

**Steelman for full KEEP:** each source is individually costly (fieldwork investment, prep time,
declared-at-setup citation) and rewarding preparation is thematically apt for Renaissance political
leadership — "come prepared" is not flavor-only, it's the N-grounded dynamic.

**Verification against the corpus:** `params/contest_extensions.md` confirms the finding is *correct
and precise*, not merely plausible: there are already **two independently-declared, uncoordinated caps**
— "Max positional bonus: +5D (genre+1, audience+1, MS targeting+1, Recall+2)" (Stacking §, line 57) and
a *separate* "+3D max" for Findings+Prep (line 25) — plus Corroborate's +1D (params/contest.md line 99)
that is capped with neither group. Summed, a fully-prepared orator can add up to +9D on top of a base
pool the same doc calls "practical pools 12–18D" — a 50-75% pool inflation from zero-attribute sources,
with no combined ceiling ever stated. This is exactly the failure mode Ω-d names (pays-what-it-buys
violated by *interaction* between two already-ratified individual caps, not by any single source).

This exact residual was independently flagged by the 2026-07-04 NERS-audit refutation (L-A: "uncapped
Recall/Corroborate/Prep/Findings stacking — no GLOBAL bonus cap while genre/boost ARE capped") and
explicitly *not* refuted — filed as real, P2, "should be filed SEPARATELY and narrowly." Two independent
audits converging on the identical, textually-verifiable gap is strong corroboration.

**Outcome: UPHELD.** The recommendation (cap the combined stack, don't cut any individual source) is
proportionate and does not remove any of the four N-grounded sources.

---

## 3. Wager Obligation §6.1.1 edge cases (DISTILL, P3) — steelman attempted

**Dossier claim:** 4 of 5 edge cases are generic to any Obligation and duplicate what a general
Obligation-interruption rule (reusing generational-transition machinery) would already cover; only
structural-impossibility is genuinely Wager-specific.

**Steelman for full KEEP (no distillation needed):** read closely, the two PC-death special cases
(§6.1.1 "holding" / "owing") are **not actually duplicative** — they explicitly cite and defer to the
existing `generational_transition_v30` TRANSFER/RESET sections verbatim, adding only a Wager-specific
wrinkle (an achievability check tied to the predecessor's Standing/Conviction, and a Wager-specific
reward/penalty). That is proper reuse of shared machinery, already done correctly, and cuts against
"self-duplicated scope" for those two rows specifically.

**Where the steelman partially fails:** the *institutional-collapse* edge case (a faction dissolving
before a Wager resolves) states a suspend/wait-for-successor/discharge logic that has nothing
Wager-specific about it — any base Obligation bound to a collapsing faction would face the identical
question ("is the obligation still live if the obligated institution is gone?") and the base Obligation
spec (§6.1's Formal/Grand/Royal/Church table) never addresses it. That is a genuine generalizable gap,
and the *counterparty-death* case is arguably generalizable too, since "parties (who is bound)" in the
base Obligation-tracking section can also name an individual NPC, not only a faction.

**Outcome: UPHELD**, narrowed: the DISTILL target should be specifically the
institutional-collapse (and probably counterparty-death) rows, not all four non-structural-impossibility
cases as stated — the PC-death holding/owing rows are already properly generalized and should be left
as-is (they are documentation, not duplication). This sharpens rather than reverses the verdict.

---

## 4. Four-games meta-choice (REFINE, P1) — steelman attempted — **OVERTURNED TO KEEP**

**Dossier claim:** the design commitment "as currently specified (walkthrough §4) only binds Stage 4
to divergent UI widgets, not divergent resolution math," risking a Duplicate-coverage build (one
CLASH/REINFORCE/CROSS/TIE mechanism in four costumes).

**Steelman:** reading `player_interaction_walkthrough_v1.md` §4 directly — its own text says: *"This
section exists so that when Stage 4 fans out the four games, each agonist inherits 'this must look and
play differently from Agôn,' **not just** 'this must resolve differently.'"* That sentence's plain
reading is that "must resolve differently" is the *pre-existing baseline commitment* (owned elsewhere —
the dossier's own `retires_downstream` field names `resolution_plan_v1.md` Stratum C / C-RESPESS-2..5 /
ED-SC-0004/0006/0009 as exactly that locus), and §4 is layering an *additional* UI-divergence
requirement on top of it, not substituting for it. The design's own source material for Stage 4
(Dowlen weighted lottery / liberum-veto consensus / Putnam two-level negotiation, per the 2026-07-04
refutation's citation of the source-research trilogy) is unambiguously four distinct game-theoretic
resolution mechanisms, not four skins.

Independently, the near-identical underlying tension ("does the contest collapse to one venue-invariant
pattern?") was already adjudicated by `designs/audit/2026-07-04-ners-qualitative-audit/01_workings/
refutations/refute_four-games-collapse-one-pattern.md`: **REFUTED as framed**, with the Stage-4
differentiation question explicitly ruled **"design-tier ... P2/P3 seam-closure; NO new P1"** and
"scheduled as the in-flight Stage 4 rebuild" — i.e. this exact question has already been through one
adversarial pass and come out at P2/P3, not P1.

**Cardinal-rule check — this is where the verdict actually breaks:** the dossier's own framing ("as
currently specified... only binds... risking a Duplicate-coverage build... unless tightened before
Stage 4 starts") is, on inspection, a claim about *specification-completeness ahead of an unbuilt
stage* — precisely the shape of reasoning §4/cardinal-rule bars ("It isn't wired/built/ported yet →
never a verdict input... this audit does not cut, flag, or penalize anything for being unbuilt"). The
`build_state_note` attempts to launder this as "tightening acceptance criteria, not claiming it doesn't
exist" but the practical effect — a P1 severity subtractive-adjacent REFINE grounded in "what might go
wrong when Stage 4 gets built if under-specified" — is a build-readiness worry wearing a design-merit
costume. Judged *as intended* (the source-research trilogy + resolution_plan_v1 Stratum C explicitly
commit to divergent resolution math; §4 explicitly layers UI on top, not instead), the four-games
meta-choice is N-grounded and not at risk of Duplicate coverage by design intent.

**Outcome: OVERTURNED TO KEEP.** The residual "make sure walkthrough §4 cross-references
resolution_plan_v1 Stratum C explicitly so Stage 4's acceptance criteria don't get authored from §4
alone" is a legitimate documentation-linking suggestion — but it belongs in the additive resolution
plan as ordinary wiring hygiene, not as a P1 subtractive verdict in this audit. Severity as filed (P1)
is not supportable per the prior refutation's P2/P3 ruling on the same underlying question.

---

## KEEP spot-checks (not steelmanned in full, checked for over-generosity)

- **Style: Suppression / Insinuation (KEEP, contingent on ED-1060 branch (a)).** Verified against
  `params/contest.md` lines 116-123: ED-1060 is explicitly "**Implemented as (a)**" already (the
  terminal-value fix is the current design-table default, not a hypothetical the dossier invented to
  save the action) — flagged provisional/needs_jordan, but not speculative. The KEEP is well-grounded,
  not over-generous. No change.
- **Obligation-naming, BG Parliamentary Vote, Practitioner Weaving, Thread Operations Between
  Exchanges, Corroborate, Coalition declare-Side.** Spot-checked against cited sources (ED-297, ED-621,
  R-65 cross-references); citations resolve to real, specific corpus locations rather than asserted
  vibes. No over-generosity found; no change.

## Cardinal-rule re-audit (build-state contamination check)

Re-scanned all 18 verdicts for build-state-as-reason. Only one violation found and corrected: **item 4
above** (four-games meta-choice) — its REFINE/P1 verdict, despite a build_state_note disclaiming this,
functionally penalized the action for pre-Stage-4 specification incompleteness rather than projected
as-built contribution; corrected to KEEP. All other verdicts (including the two Style-genre KEEPs and
the DISTILL/REFINE items above) were confirmed to rest on N/Ω/Q design-merit reasoning with no
stub/unwired/unbuilt language used as evidence.

## Summary table

| Action | Original verdict | Critic outcome | Final verdict |
|---|---|---|---|
| Appraise | REFINE (P2) | UPHELD | REFINE |
| Recall/Corroborate/Prep/Findings stacking | REFINE (P2) | UPHELD | REFINE |
| Wager Obligation §6.1.1 edge cases | DISTILL (P3) | UPHELD (narrowed) | DISTILL |
| Four-games meta-choice | REFINE (P1) | OVERTURNED-TO-KEEP | KEEP |
| All other (14) KEEP verdicts | KEEP | spot-checked, UPHELD | KEEP |

