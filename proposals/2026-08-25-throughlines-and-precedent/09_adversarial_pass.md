# 09 — Adversarial pass: corrections to Chapters 2, 3 and 4
## Status: process record, 2026-08-25

> Per CLAUDE.md §0 the adversarial pass is a **STAGE, not a deliverable**: its output is edits to
> the thing under review, not a findings document. This file exists because the corrections are
> *dispositive* — several overturn a published claim — and a reader of the chapters is entitled to
> see what was attacked and what survived. Chapter 1 carries its own corrections inline.
>
> Four `valoria-critic` agents ran, each structurally read-only (Read/Grep/Glob — no Write, no
> Bash) and each given a producer's **output** and never its reasoning, per §10's relay.
> Combined locator hit rate across the passes: **~84%**.


---

## Chapter 3 — One Resolver, Four Scales, One Scalar

*A structurally read-only `valoria-critic` attacked this chapter and Chapter 4 together, opening 64
locators across the two: **55 exact (86%)**, 9 failing (5 wrong, 4 off-by-N). This chapter scored
~82%. The corrections that change a conclusion are recorded here rather than absorbed.*

**1. The threadwork citation names the wrong subsystem.** The claim that threadwork does not execute
on the campaign path cited `mc_v18.py:192` and `:204-217` — but those stubwire **`generate_npc`** and
**`form_knot`**, a different gap entirely. The conclusion is nonetheless true, on better evidence: the
only importers of `systems.threadwork.sim.operations` anywhere under `engine/` are two tests
(`engine/tests/test_thread_mending_ed871.py:26`, `engine/tests/test_pipeline_reach.py:790`); no
production caller exists. This matters because the "goldens will not move" safety argument for R-1
rested on it.

**2. The `roll_pool` **S** severity is downgraded from HIGHEST to HIGH-latent, and this is the most
important correction to this chapter.** Both arms of the personal↔faction seam resolve at **TN 7
today**: `systems/combat/combat_engine_v1/core.py:46` sets `TN = SL.TN_STANDARD` and
`engine/autoload/sigma_leverage.py:87` sets `TN_STANDARD = 7`; all nine faction TN sites are 7 (eight
named constants plus one literal at `mass_seizure.py:263`). The two engines therefore share
μ=0.40/σ=0.800 at that point, and **the measured 21.2 pp divergence at TN 8 is not reachable across
that seam on `main`.** It becomes reachable the moment any site declares a non-7 TN. This is a
correctness defect with a latent blast radius, not a present regression — and saying otherwise would
be the present-tensing this analysis condemns elsewhere.

**3. `_CONTINUOUS_PARAMS` is not single-owned — there is a byte-identical second copy.**
`engine/autoload/sigma_leverage.py:73-77` declares `PER_DIE` with the same three rows as
`dice_engine._CONTINUOUS_PARAMS` (`:68-72`). A chapter arguing the resolver is "well-owned at the top"
must name the duplicate, and R-1's deduplication fixes one of two copies unless it names both.
`sigma_leverage.py:83-86` also strengthens this chapter independently: it documents the TN scale as
*"Controlled 6 / Standard 7 / Desperate 8, selected by SITUATION"* — the discrete engine is described
at its own call layer as difficulty-responsive while `_die_result` is not.

**4. The degree-ladder guard cannot observe a fractional obstacle.**
`tests/valoria/test_degree_ladder_single_owner.py:208-209` builds `FRAC_DOMAIN` as
`[(i/4, o) for i in range(-8,81) for o in range(1,11)]`, and the file warns in its own words that
*"FRAC_DOMAIN's obstacle is an INTEGER at every cell — it sweeps fractional NETS only."* So not only
does every producer round the obstacle: **the guard that would catch it is blind to the case.** That
is §0.1 pt 2 — *an assertion must be able to observe the failure it excludes* — applied to this
chapter's own R-4, and it belongs in R-4's cost line.

**5. The Ω verdict is narrowed from "closed" to "narrowed".** Everything factual verifies —
`references/throughlines_meta.md:45-55` §1 Ω-INTENT, four clauses at `:47`, the chain
`N → Ω → Μ → М → Τ → Q` at `:185`, `:194`'s flag-Jordan-and-halt. But the one document that states the
*relationship* — `audit/2026-07-04-ners-qualitative-audit/_workings_joined.md:156` — calls the
throughlines framework *"a tiered supersession of NERS"* **without** the "for qualitative vetting"
qualifier this chapter added. So: Ω is a belonging gate over proposals, distinct in subject from
NERS's per-engine verdict, and both can run `[INFERRED]`. **What closes is "we do not know what omega
is." Whether Ω supersedes NERS for engines remains live**, and `SKILL.md`'s caution should be narrowed
rather than deleted. The failure-lexicon row also mis-mapped: *Cost-hidden* is at `:170` and maps to
**М-6**, not Ω-d (`:167` is *Reskinned attractor*); the `vetting:` block spec is `:252-275`, not
`:200-220`.

**6. One comment-as-evidence instance, corrected.** The P→U matrix cell cited
`zoom_in_out.py:119-120` for carriers that "fire"; those lines are a parameter **docstring** listing
dict keys, not the code that applies them. The cell verdict (BROKEN, no producer) stands; the
evidence needed a code locator or the word *declared*.

**7. Locator precision:** `tribunal.py:118/:120` are comments — the code is `:119` and `:122`;
`test_f7_smoke_oracle.py`'s four goldens are at `:267, :273, :274, :275`, not `:267-270`; the
PREVIOUS block begins at `:258`; `sigma_leverage.py:274` is a fourth variable-TN passthrough into the
discrete engine and the only one inside `engine/`, missing from the inventory.

### What survived
The headline defect is **upheld unqualified**, with the critic recomputing the moments independently:
`_die_result(face)` takes one parameter (`:53`); `roll_pool` computes `net` without `tn` (`:82`) and
records `tn=tn` (`:84`); EV = 0.400 and σ = 0.800, bit-exact against `_CONTINUOUS_PARAMS[7]`;
`RollResult.tn` has **zero readers tree-wide**. The 19-vs-28 correction was reproduced independently
(33 occurrences, 14 of them mass battle's own same-named roller). §2.3(b) was **sharpened**: the
critic hand-computed `resolution.py:36-42`'s moments at all three TNs — 6 → (0.5, 0.80623), 7 → (0.4,
0.800), 8 → (0.3, 0.78102) — reproducing `_CONTINUOUS_PARAMS` to printed precision, which makes R-1 a
lift rather than a design call. The obstacle-derivation refutation, the SUSPENDED disposition, the
keystone HELD entries, and every seam measurement were verified exactly.
