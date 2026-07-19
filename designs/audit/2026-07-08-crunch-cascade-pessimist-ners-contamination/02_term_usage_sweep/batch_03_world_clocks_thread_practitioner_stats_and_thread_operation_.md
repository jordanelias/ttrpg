# Term Usage Sweep — Batch 3: World Clocks, Thread Practitioner Stats, and Thread Operation vocabulary

# COMPLETE CONSOLIDATED REPORT — All 20 Terms

*(Terms 1–9 detailed above stand as researched; consolidating with terms 10–20 below for the complete deliverable.)*

## 10. Weaving

**Home definition:** `designs/threadwork/threadwork_v30.md:260-306` (§2.4 "Weaving — Things Cohere"). Pool: `(Spirit × 2) + relevant History bonus + Thread Pool Score` (PP-616, PP-625), TN 7. Ob by scale (pre-PP-622 single-axis table, self-flagged superseded: line 269 *"(Pre-PP-622 single-axis scale — canonical: params_threadwork.md §Three-Axis Ob System.)"*): Object 1, Personal 2, Relational 3, Territorial 4, Structural 5. Degree table: Overwhelming → MS +1 (Relational+ only) + TS +1; Success → MS unchanged; Partial → MS −1, Coherence −1; Failure → MS −2, Coherence −1 (plus Shifting Object at MS≤40, Gap at MS≤20). Glossary Part Eight: `Weaving | — | Things Cohere. Stabilises threads, restores actualisation.`

**Usage sweep:** ~97 non-archive/test files hit `\bWeaving\b`. Consistent core usage across `params/threadwork.md`, `sim/thread/operations.py` (`attempt_weaving`), `designs/scene/fieldwork_v30.md`, `designs/npcs/npc_behavior_v30.md`, `designs/provincial/factions_personal_v30.md` (Community Weaving — a *different*, faction-scale variant, see below), `designs/threadwork/threadwork_v30_infill.md` (Over-Actualisation / brittleness prose).

**Divergence check:**
- The Ob-by-scale table in `threadwork_v30.md` is **explicitly self-superseded** — the doc itself says the real current numbers are the Three-Axis system in `params/threadwork.md`. This is disclosed, not hidden, so not a fresh finding, but it means anyone reading only `threadwork_v30.md`'s own worked table gets the *retained-for-history* numbers, not the canonical ones — a legibility risk even though technically documented.
- **"Community Weaving"** is a distinct, faction-scale variant of Weaving with its *own independent pool/TN/Ob*, and it inherits the Thread-Tension-not-fully-retired problem from term 8: `params/threadwork.md:25-29` gives `Pool = (Spirit × 2) + History + TPS`, `TN: 7 | Ob: 3 | RS outcome: Success = RS +1; Overwhelming = RS +2` — using the retired "RS" name — while `designs/provincial/factions_personal_v30.md:325-333` gives Community Weaving as `Influence vs Ob = Thread Tension ÷ 20 (round up)` with **Thread Tension**, not Mending Stability/RS, as the resolved variable. These are two different pools/mechanics for something both call "Community Weaving/Organizing" (one Spirit-based individual-practitioner-style pool costed in RS; one Influence-based faction pool costed in Thread Tension) with no cross-reference reconciling them.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `designs/threadwork/threadwork_v30.md:260-306` | CANONICAL DEFINITION (mechanics/degree table) | Home doc | Yes, with self-flagged Ob-table supersession |
| `params/threadwork.md §Three-Axis Ob System` | CANONICAL DEFINITION (current Ob values) | Explicitly cited by threadwork_v30.md as canonical | Yes |
| `sim/thread/operations.py:248-258` (`attempt_weaving`) | HARDCODED DUPLICATE | Independent Python literal restatement of pool/Ob/Coherence, inline `[canonical: ...]` citations | Agrees |
| `params/threadwork.md:25-29` ("Community Organizing — Canonical Pool") | HARDCODED DUPLICATE, using retired "RS" name | Independent restatement | Numerically self-consistent; name is the retired one |
| `designs/provincial/factions_personal_v30.md:325-333` (Community Weaving) | UNCLEAR / NO CANONICAL SOURCE relative to the params version | Independent, differently-costed mechanic sharing the same name | **Diverges** — different pool, different cost variable (Thread Tension vs RS/MS), no reconciliation |

---

## 11. Pulling

**Home definition:** `threadwork_v30.md:308-344` (§2.4 "Pulling — Things Open"). Same pool/TN as Weaving. Ob by actualization level (again explicitly pre-PP-622/superseded): Loosely 1, Normally 2, Firmly 3, Previously Woven 4, Foundational 5. Duration table has an explicit **in-doc correction layered over itself**: the base table (line 330: "0 = end of scene, 1 = end of session, 2+ = until next seasonal accounting") is immediately followed by "Correction (R-54)" (lines 332-337) that shifts the entire ladder by one tier and adds a 4th tier. Both tables are left in the document; the correction note doesn't strike the original, it just says "Apply to §2.4 Pulling." This is an in-doc patch-layering pattern (not a cross-file divergence) but is worth flagging: a reader must know to apply R-54 over the base table rather than read the base table as current.

**Divergence check:** Glossary Part Eight: `Pulling | — | Things Open. De-actualises threads. **Default sense is Present-Oriented**; see also Past-Oriented Pulling.` — consistent with `threadwork_v30.md`. No cross-file numeric contradictions found beyond the in-document R-54 patch-layering noted above.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `threadwork_v30.md:308-344` | CANONICAL DEFINITION, with an in-doc patch (R-54) layered over its own duration table | Home doc; self-modifying via patch note | Internally patchable but not self-consolidated |
| `params/threadwork.md §Three-Axis Ob System` | CANONICAL DEFINITION (current Ob) | Cited by threadwork_v30.md | Yes |
| `sim/thread/operations.py:261-267` (`attempt_pulling`) | HARDCODED DUPLICATE | Independent restatement, reuses `DEPTH_OB`/`COHERENCE_COST_BY_SCALE` dicts | Agrees with the *base* degree table; does not appear to implement the R-54 duration-ladder correction (duration isn't modeled in this function at all — it only resolves degree, not duration) |

---

## 12. Past-Oriented Pulling / POP

**Home definition:** `threadwork_v30.md:346-365` (§2.4). Pool same formula, **TN 8** (all sources agree: `threadwork_v30.md:351`, `params/threadwork.md:59`, `sim/thread/operations.py:48`). Ob by recency: same scene/session 3, 1-2 seasons 4, 3-5 seasons 5, 6-10 seasons 6, 10+ seasons 7 — identical across `threadwork_v30.md:355-361`, `params/threadwork.md` (Recency table not separately given there but the recency Ob ladder matches what `sim/thread/operations.py:279-280` hardcodes: `{'same_scene': 3, '1-2_seasons': 4, '3-5_seasons': 5, '6-10_seasons': 6, '10+_seasons': 7}`). Glossary Part Eight: `Past-Oriented Pulling | POP | Pulling operation targeting historical thread configurations. Requires Thread Sensitivity 70+.`

**Divergence check:**
- **Coherence cost cap wording is subtly inconsistent but resolvable.** `threadwork_v30.md:623`: "Past-Oriented Pulling | −1 additional on top of standard Pulling cost" (in the §3.2 table). `threadwork_v30.md:177` (fieldwork integration note): "Per-op cap ruling (TW-05): POP Coherence −1 additional IS subject to per-op cap (total POP Coherence cost = −1 max regardless of scale), unlike FR/Binding Operations which are cap-exempt per PP-196." `sim/thread/operations.py:282-285` implements this exactly: `coh = COHERENCE_COST_BY_SCALE.get(scale, 0) - 1; coh = max(-1, coh) if scale in ("Object", "Personal") else coh` — this correctly caps at −1 for Object/Personal, but for Relational+ the code does **not** actually cap the total at −1 as the prose claims ("total POP Coherence cost = −1 max regardless of scale") — at Relational scale, `COHERENCE_COST_BY_SCALE['Relational'] = -1`, so `coh = -1 - 1 = -2`, and the `max(-1, coh)` guard is only applied when `scale in ("Object","Personal")`, so Relational+ POP costs −2, not the "−1 max regardless of scale" the prose promises. This is a live code-vs-doc-prose mismatch: the doc's own §2.3 fieldwork note claims a flat −1 cap "regardless of scale," but both the §3.2 table (calling it "additional on top of standard Pulling cost," which is scale-variable) and the actual sim implementation produce a scale-dependent total, not a flat cap.
- The TS≥70 requirement stated by the glossary is not independently restated as a numeric gate inside `sim/thread/operations.py`'s `attempt_past_pulling` (no TS check present in that function at all — eligibility isn't enforced in code), though it is enforced narratively/in `threadwork_v30.md`'s Distance/Depth tables via TS-minimum columns.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `threadwork_v30.md:346-365` (recency/Ob, TN 8) | CANONICAL DEFINITION | Home doc | Yes |
| `threadwork_v30.md:177` ("total POP Coherence cost = −1 max regardless of scale") | CANONICAL DEFINITION, but internally in tension with §3.2's own "additional on top of" framing | Same document, two sections | Ambiguous/self-inconsistent on whether the cap is flat or scale-relative |
| `sim/thread/operations.py:270-287` | HARDCODED DUPLICATE | Independent implementation | **Partially diverges** — caps correctly at Object/Personal, produces −2 at Relational+, contradicting the "regardless of scale" prose |
| `params/threadwork.md:59` (TN 8) | HARDCODED DUPLICATE | Independent restatement | Agrees |

---

## 13. Locking

**Home definition:** `threadwork_v30.md:367-412` (§2.4 "Locking — Unable to Become"). Requires TS≥50. Pool same formula. **TN 8** (Binding Operations, PP-619). Minimum Ob "Struck (PP-623)" — defers to Three-Axis system. Old single-axis Ob table (Object 4…Structural/Foundational 8+) explicitly struck-through and retained "for patch history only." Degree table: Overwhelming → MS −1 + TS+1; Success → MS −1; Partial → MS −2, Coherence −1 (cap); Failure → MS −3, Coherence −1 (cap) + 2 Wounds. Chronic drift table (1 season none; 2-3 seasons MS −1/season; 4+ MS −2/season; permanent = drift ceases). Reversal via Pulling at `Ob = (original TS÷10, round up) − 2, minimum 1`.

**Divergence check:**
- `params/threadwork.md:126-127` gives a **different chronic-drift formulation**: *"Lock chronic drift: Object=0; Personal=-1/season; Relational=-1→-2 (season 4+); Field=-2→-3; Structural=-3→-5."* This is a scale-graduated drift table, whereas `threadwork_v30.md:399-404`'s chronic table is duration-graduated (1 season / 2-3 seasons / 4+ seasons / permanent), not scale-graduated. These are **two different axes for the same "chronic drift" concept** — one keyed by how long the Lock has persisted, one keyed by the Lock's Depth scale — with no stated formula for combining them (does a Structural Lock at year 5 use −5/season flat, or −2/season per the duration table's "4+ seasons" row? Neither doc says which one governs, or whether they compound).
- `threadwork_v30.md:406` itself flags a further, in-doc, unreconciled patch: *"Variable Mending Stability drift (R-63): Replaces uniform −1 Mending Stability/season for locked institutions: Slow-change domain... −1/season. Engine determines domain type when Lock is applied."* — a third drift formulation layered on top of the other two, with "Engine determines" as the only reconciliation instruction (i.e., punted to unspecified runtime logic that doesn't exist anywhere in `sim/`).

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `threadwork_v30.md:367-412` (degree table, duration-graduated drift) | CANONICAL DEFINITION | Home doc | Internally consistent with itself |
| `params/threadwork.md:126-127` (scale-graduated drift) | UNCLEAR / NO CANONICAL SOURCE relative to threadwork_v30.md's own drift table | Independent, differently-axised restatement, no cross-reference reconciling the two | **Diverges** — two incompatible drift models for the same mechanic, precedence undeclared |
| `threadwork_v30.md:406` (R-63 variable drift) | UNCLEAR — in-doc patch, unresolved | "Engine determines domain type" with no engine logic found in `sim/` implementing this | Neither confirmed superseded nor implemented |
| `sim/thread/operations.py:290-304` (`attempt_locking`) | HARDCODED DUPLICATE | Implements the *degree table* only (Coherence/MS on the initial roll); does not implement any of the three chronic-drift formulations (no seasonal-drift function present anywhere in `sim/thread/`) | Agrees on the one-shot degree table; the chronic-drift mechanic is unimplemented entirely, so no drift-model conflict surfaces in code yet |

---

## 14. Dissolution

**Home definition:** `threadwork_v30.md:414-442` (§2.4 "Dissolution — Unable to Be"). Requires TS≥50. Same pool, TN 8. Degree table: Overwhelming → MS −3, Micro-Gap closes same scene; Success → MS −5, Gap forms 1 scene; Partial → MS −6, Shifting Object, Coherence −1 (cap); Failure → MS −8, full Gap, Monstrous Incursion, Incapacitated, Coherence −1 (cap). Also cross-referenced by `params/threadwork.md:132-137` ("Dissolution Gap Creation, PP-604"): breach cost `n` MS one-time, then Gap scale by degree (Overwhelming closes within scene; Success = target scale n; Partial = n+1; Failure = n+2).

**Divergence check:** The two MS-cost framings coexist without an explicit reconciliation statement connecting "flat −3/−5/−6/−8" (`threadwork_v30.md`) to "breach cost n (one-time)" (`params/threadwork.md`) — it's plausible these are meant as the same thing under different notations (n being a placeholder for the degree-driven flat numbers), but neither document states that equivalence explicitly; a reader has to infer it. This is a soft ambiguity, not a hard numeric contradiction (I did not find an instance where they gave different numbers for the same case), so I flag it as a legibility gap rather than a confirmed divergence.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `threadwork_v30.md:414-442` | CANONICAL DEFINITION | Home doc | Yes |
| `params/threadwork.md:132-137` (Gap Creation) | PULLED/REFERENCED-adjacent, but uses different notation (n-based) without an explicit equivalence statement to the flat numbers | Same PP (PP-604) cited; no literal number restated that contradicts, but no explicit unification either | Not a confirmed contradiction; an unstated-equivalence gap |
| `sim/thread/operations.py:307-313` (`attempt_dissolution`) | HARDCODED DUPLICATE | Implements FR surcharge + scale cost only; does not implement Gap-scale-on-failure logic at all | Agrees on Coherence cost; Gap-formation consequence unimplemented in code |
| `threadwork_v30.md:432-440` (Lock vs. Dissolution summary table) | CANONICAL DEFINITION (comparative) | Home doc | Yes |

---

## 15. Mending

**Home definition:** `threadwork_v30.md:444-509` (§2.4 "Mending — Repairing the Substrate"). Requires TS≥50, target must be Gap/Shifting Object/Locked Zone border. Same pool formula (PP-616, PP-625). TN 7. Ob by Gap severity (Shifting Object 2, Micro-Gap 3, Standard Gap 5, Entrenched 6, Catastrophic 7, Locked Zone border 8+) — explicitly flagged as "predates PP-622; canonical Mending Ob: params_threadwork.md §Three-Axis Ob System (Mending Ob = Depth Ob − 1 + age modifier + Breadth + Distance)" (line 458). Degree table: Overwhelming → Gap closes, MS +2, **Coherence 0**; Success → Gap closes, MS +1, Coherence 0; Partial → severity reduced one tier, MS unchanged, Coherence 0; Failure → MS −2, Coherence 0. **Mending Coherence Asymmetry** (line 481): Mending never costs Coherence — this is philosophically load-bearing (restorative-operation type, ED-871/canon/02 Amendment 3).

**Divergence check — already surfaced under term 1 but re-flagged here as it's most precisely a Mending-specific finding:**
- `threadwork_v30.md:624` (§3.2 Coherence Reduction table, "Mending" row) asserts: *"Sim `sim/thread/operations.py` still charges −1/−2 — SIM-CODE fix deferred to Stratum B, entangled with the C-TW-3 blanket-penalty bug and lacking test coverage."* This is **false as currently written**. `sim/thread/operations.py:316-334` (`attempt_mending`) sets `coh = 0` unconditionally, with an explicit comment: *"Per ED-871 (2026-05-31) + canon/02 Amendment 3... (Was -1, the pre-ED-871 value; the doc side was propagated to threadwork_v30 §3.2 + params/threadwork.md on 2026-07-07, and the sim is closed here.)"* And `params/threadwork.md:278` independently confirms: *"This params value was already correct at 0; noted here for co-file provenance after the 2026-07-07 propagation that fixed threadwork_v30 §3.2's stale −1."* So `params/threadwork.md` was fixed 2026-07-07 and the sim was fixed 2026-07-07, but `threadwork_v30.md:624` — the actual home document — **still contains the old warning text describing the bug as open**, one day after (today is 2026-07-08 per session context) the claimed fix date. This is a precise, freshly-dated doc-vs-code accuracy failure.
- Related, still-genuinely-open bug the same comment references but does *not* fix: `sim/thread/operations.py:186-191` — a blanket rule (`if degree in ("Partial","Failure") and operation != "Mending": effective_coh -= 1`) that the inline comment admits *"also mis-hits Leap against its own docstring"* (see term 17 below) — i.e., a second, adjacent, explicitly-acknowledged-but-unfixed bug (tracked as `C-TW-3`, deferred to "Stratum B").

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `threadwork_v30.md:444-509` (mechanics/degree table) | CANONICAL DEFINITION | Home doc | Yes |
| `threadwork_v30.md:624` (claim about sim code state) | CANONICAL DEFINITION but **stale** | Same doc, different section | **No** — the claim is factually outdated relative to the code it describes |
| `params/threadwork.md §Three-Axis Ob System` (Mending Ob = Depth−1) | CANONICAL DEFINITION (current Ob) | Cited by threadwork_v30.md | Yes |
| `params/threadwork.md:278` | PULLED/REFERENCED (explicit provenance note, not an independent number) | States the fix's date/history rather than restating a new value | Yes, accurate |
| `sim/thread/operations.py:316-334` | HARDCODED DUPLICATE | Independent restatement (`coh=0`) with inline citation | Agrees with the true canonical value (0), contradicting the stale claim in `threadwork_v30.md:624` about this same code |

---

## 16. Diagnosis (the Thread pre-operation read)

**Home definition (as struck):** `threadwork_v30.md:138`: `## 2.2 Diagnosis — STRUCK (ED-134/ED-124, 2026-04-03)` — followed by **no content** (empty section). `threadwork_v30_infill.md:32-33`: *"## 2.2 Diagnosis — STRUCK (ED-134/ED-124, 2026-04-03) > Diagnosis as a standalone action is removed from the system. Practitioner either suspends their sense of self and Leaps, or does not. No preparatory gate action exists... See params_threadwork.md §Diagnosis — STRUCK."*

**Verification of the cross-reference:** `params/threadwork.md` contains **no "Diagnosis" section at all** (confirmed by full-file grep — zero hits for "diagnos" in the entire 287-line file). The citation in `threadwork_v30_infill.md:33` ("See params_threadwork.md §Diagnosis — STRUCK") points to a section that does not exist in the current params file. **This is a broken/dead cross-reference.**

**Divergence check — the STRUCK status is contradicted by the rest of the same document(s) treating "Diagnosis" as a live, mandatory, structurally-scheduled step:**
- `threadwork_v30.md:203`: `**Revised standard sequence (Diagnosis precedes Leap):**` — a section header presenting Diagnosis as an active step in round sequencing.
- `threadwork_v30.md:161`: Einhir framework prerequisite requires *"The practitioner has Diagnosed the Locked Zone's structure (requires a prior Southernmost expedition Diagnosis scene...)"* — Diagnosis as a concrete, requestable scene/action.
- `threadwork_v30.md:293`: Weaving Over-Actualisation table, Territorial row: *"Diagnosis on this configuration +1 Ob."* — Diagnosis is given its own Ob modifier, i.e., it's still something that can be harder or easier.
- `threadwork_v30.md:403,442`: chronic Lock effects reference "occludes Diagnosis, degrading intentionality" and explicitly note *"not to Diagnosis itself (which has no Ob)"* — carefully distinguishing that Diagnosis *itself* has no roll, while still treating it as an actual pre-operation step that can be *made harder for the subsequent operation*.
- `threadwork_v30_infill.md:50`: *"**Pre-Leap round(s):** Diagnosis (Priority 4). Practitioner renders the target, reads configuration, sets intentionality."* — this assigns Diagnosis its own **Priority slot in the round-sequencing system**, which is a much stronger claim than "no preparatory gate action exists" (the framing immediately above it in the same file, line 33).
- `threadwork_v30_infill.md:94`: `**Collective Diagnosis:** Multiple practitioners may Diagnose in the same round as part of collective preparation...` — again treating Diagnosis as a structured, nameable, multi-actor procedural step.
- `references/glossary.md:183` (Part Eight): `Diagnosis | — | Mandatory pre-operation read. No roll. Required before Mending, Locking, Dissolution, Past-Oriented Pulling.` — the glossary presents it as a currently *mandatory* mechanic, not a struck one.

**Assessment:** "Diagnosis" was struck **as a rolled game action with its own Ob** (that much is consistent everywhere — nobody rolls dice for Diagnosis), but it was never actually struck **as a named procedural/narrative step** — it still occupies a Priority-4 round slot, still gates certain operations ("Required before Mending, Locking, Dissolution, POP" per the glossary), still has other things' Ob keyed off whether it was disrupted, and still supports "Collective Diagnosis" as a defined multi-practitioner procedure. Calling the whole concept "STRUCK" in a section header is misleading given how load-bearing the surviving no-roll version remains throughout the rest of the very same document.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `threadwork_v30.md:138` (STRUCK header, empty body) | CANONICAL DEFINITION (of the strike) | Home doc | Technically true (no roll) but misleadingly total |
| `threadwork_v30_infill.md:32-33` | CANONICAL DEFINITION (elaborates the strike) + a **broken citation** to a nonexistent params section | Explicit cross-reference to `params_threadwork.md §Diagnosis` | The cited section does not exist |
| `threadwork_v30.md:161,203,293,403,442` (six+ live uses of Diagnosis as an active procedural concept) | HARDCODED DUPLICATE of a mechanic the doc's own §2.2 calls struck | Independent restatements within the same document | Internally contradicts §2.2's framing |
| `threadwork_v30_infill.md:50,94` (Priority 4 slot; Collective Diagnosis) | HARDCODED DUPLICATE, structurally stronger than "no preparatory gate action exists" | Independent restatement | Directly in tension with the file's own STRUCK framing two paragraphs earlier |
| `references/glossary.md:183` | HARDCODED DUPLICATE, presented as a live mandatory mechanic | Independent restatement, no "STRUCK" qualifier at all | Consistent with the *surviving* no-roll version; silent about the STRUCK header ever existing |

---

## 17. Leap

**Home definition:** `threadwork_v30.md:142-238` (§2.3 "The Leap — Suspending Rendering"). Eligibility: Approach Training tag + TS≥30 + not incapacitated. Pool: same formula. TN 7. Ob: TS 30-49 = 2, TS 50+ = 1. Degree table: Overwhelming → clean suspension, next op Ob −1, TS+1; Success → suspended, proceed; Partial → op Ob+1, 2 Composure strain; Failure → **"−1D to Thread Pool Score for remainder of scene"** (explicitly *not* a Coherence cost — `threadwork_v30.md:173`: "the aftereffect (−1D Thread Pool Score) represents the psychic friction of the failed attempt"). Foundational reference: `canon/02_foundations_amendment_leap_mechanism.md` (suspension target, knot formation, operation-type taxonomy).

**Divergence check — live sim bug, self-acknowledged in-code, contradicting the doc's own explicit rule:**
`sim/thread/operations.py:224-245` (`attempt_leap`) docstring states: *"Returns OperationResult. Failure does NOT cost Coherence per §3.2 (Leap is the rendering-suspension act, not yet an operation)."* — correctly restating the canon above. It then calls `_resolve_operation("Leap", actor, ob, TN_STANDARD, coherence_delta=0, ...)`. But `_resolve_operation` (lines 160-194) contains the *blanket* rule: `if degree in ("Partial", "Failure") and operation != "Mending": effective_coh -= 1`. Since `operation == "Leap"` (not `"Mending"`), a Leap that resolves Partial or Failure **will** have `effective_coh` reduced by 1 from whatever `coherence_delta` was passed in (0 here) — i.e., **the code will actually apply a −1 Coherence penalty to a failed Leap**, directly contradicting both the function's own docstring one function up and the canonical rule in `threadwork_v30.md` (Failure = Thread Pool Score penalty, not Coherence). This is not a hidden bug — the code's own comment at lines 184-188 names it: *"the broader C-TW-3 defect — this blanket penalty also mis-hits Leap against its own docstring — is NOT fixed here (separate item, ED-WR-0005 Stratum-B tail)."* So this is a confirmed, currently-live, self-documented defect where the executing code diverges from both its own docstring and the canonical rule.
- No divergence found in the eligibility/Ob/pool numbers themselves — TS 30-49→Ob2 / TS50+→Ob1 is consistent between `threadwork_v30.md:157` and `sim/thread/operations.py:98-100,242` (`LEAP_OB_TS_LOW=2`, `LEAP_OB_TS_HIGH=1`).

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `threadwork_v30.md:142-238` | CANONICAL DEFINITION | Home doc | Yes |
| `canon/02_foundations_amendment_leap_mechanism.md` | CANONICAL DEFINITION (metaphysical substrate; explicitly a "Foundational reference" this section implements) | Named authority in `threadwork_v30.md:144` | Yes |
| `sim/thread/operations.py:98-100,241-245` (Ob constants) | HARDCODED DUPLICATE | Independent Python constants, cited inline | Agrees |
| `sim/thread/operations.py:224-245` docstring ("Failure does NOT cost Coherence") | HARDCODED DUPLICATE (correct statement) | Independent restatement | Agrees with canon in the comment |
| `sim/thread/operations.py:160-194` (`_resolve_operation`'s blanket −1 rule, as it actually affects Leap) | HARDCODED DUPLICATE, **self-acknowledged bug** | Live executing code; comment names the defect (`C-TW-3`) and its own docstring | **Diverges from canon and from its own sibling docstring**, confirmed still-open per the code's own comment |

---

## 18. Forced Resolution / FR

**Home definition:** `references/glossary.md:185`: `Forced Resolution | FR | Collective term for Locking and Dissolution operations. TN 8. No Thread Pool Score added.` — **Note: the glossary's own claim "No Thread Pool Score added" is itself contradicted by the pool formula everywhere else in the same corpus**: `threadwork_v30.md:374,419` and `params/threadwork.md` state the Locking/Dissolution pool is `(Spirit × 2) + History + Thread Pool Score` — i.e., TPS **is** added, same as every other operation; nothing in `threadwork_v30.md`'s Locking/Dissolution sections excludes TPS. The glossary's "No Thread Pool Score added" clause appears to be a stale leftover from an earlier pool model (plausibly pre-PP-616/619 unification) that was never corrected when the pool formula was unified across all operations.

**Divergence check #2 — a prior retirement of the FR label that current canon overrides.** `params/contest.md:291-292`: *"## PP-279 — FR terminology: 'Forced Resolution' label struck. Operations: Weaving, Pulling, Locking, Dissolution, Mending. Locking and Dissolution are self-descriptive."* This patch retired the collective "FR" label entirely. But the *current* canonical Threadwork head uses "FR" pervasively and centrally as a load-bearing collective term: `threadwork_v30.md` §2.6 "Opposing Operations" section headers "FR vs FR Both-Fail Scaling" (line 577), "FR surcharge cap exemption (PP-196)" (line 631), Knot Strain table's "FR (Lock/Dissolution)" row (line 567), and the glossary's own Part Eight entry treating FR as a live, current, first-class term. Either PP-279's strike was itself superseded by later patches (PP-196, PP-618/619) without an explicit un-strike note anywhere, or `params/contest.md`'s PP-279 entry is simply stale and nothing propagated its retirement claim forward — either way, the corpus currently disagrees with itself about whether "FR" was ever actually retired.

**Divergence check #3 — name collision (likely incidental, flagged per instruction 5).** `params/contest.md:305-307`: `## Contest Stalemate — Forced Resolution (PP-255) — Maximum 10 exchanges per Contest session. After 10 consecutive exchanges without resolution: forced Unmask fires.` This is a **completely different mechanic** (Social Contest stalemate-breaker) using the same English phrase "Forced Resolution," in the *same file* that discusses Thread's FR terminology two sections earlier (PP-279, immediately above). This does not use the abbreviation "FR" for the Contest mechanic (it's spelled out as a section title only), so I judge it as most likely incidental phrase reuse rather than a true abbreviation collision — but flagging it given its immediate proximity to the Thread-FR discussion in the same document, which raises real risk of a reader conflating the two.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `references/glossary.md:185` | UNCLEAR / partially stale | "No TPS added" clause contradicted by the unified pool formula elsewhere | TN=8 agrees; the TPS clause does not |
| `threadwork_v30.md` §2.6, §3.2 (FR surcharge, FR vs FR tables) | CANONICAL DEFINITION (current, active use of "FR" as collective term) | Home doc | Internally consistent; contradicts PP-279's claimed strike |
| `params/contest.md:291-292` (PP-279, "FR terminology... struck") | CANONICAL DEFINITION of a **retirement that current canon does not honor** | Explicit patch citation | **Superseded-but-not-marked-superseded** — nothing links PP-279 forward to its apparent override |
| `sim/thread/operations.py:114-116` (`FR_SURCHARGE = -1`) | HARDCODED DUPLICATE | Independent constant, cited `[canonical: §3.2 — "FR surcharge cap exemption (PP-196)"]` | Agrees with the live (non-struck) FR mechanic |
| `params/contest.md:305-307` (Contest "Forced Resolution") | Separate mechanic — incidental English reuse, not the same term | No shared abbreviation used | Not comparable; flagged per instruction 5 as excluded from the Thread-FR sweep proper |

---

## 19. Dissolution Residue

**Home definition:** `threadwork_v30.md:651-660` (§3.4). *"Dissolution residue is compressed potential oriented toward the unintelligible ground. A practitioner may draw on it during an operation: add bonus dice equal to Potency rating (1–5)... These dice explode on 9–10 (volatile). **Cost:** −1 Coherence per use (additional...). Maximum one use per contact window. Same source: +1 Ob per prior use (depletion)."* Explicitly a replacement: `"*Replaces §5.10 (Taint track) and §5.11 (Dissolution Residue). No separate Taint track.*"` Glossary Part Eight: `Dissolution Residue | — | Potency-rated bonus dice source from prior Dissolution. Costs −1 Coherence per use.`

**Usage sweep:** Consistent across `references/mechanical_terms_index.md:694`, `references/glossary.md:186`, `sim/thread/co_movement.py:43,51` (referenced only in card-effect text strings, e.g. `"One Dissolution residue visible..."`, `"Dissolution residue gains intensity"` — no independent Potency/explode-on-9-10 mechanic reimplemented in code; the co-movement cards only toggle "residue exists / intensity +1" flags, not the actual bonus-dice mechanic), `references/wc_survival_spine.md:96,116` (Niflhel Harvest = Dissolution Residue collection — consistent), `thread_horizontal_integration_spec.md` (ED-673 answer #5, consistent).

**Divergence check:** None found in the core formula (Potency 1-5, explode 9-10, −1 Coherence, 1 use/contact window, +1 Ob per prior use) across every file that states it — this term is well-behaved. The one gap: no file besides `threadwork_v30.md` itself independently restates the "explode on 9-10" die mechanic; `sim/` has no dedicated Dissolution Residue function at all (only passing textual mentions in `co_movement.py`'s card table), so there is no code-level implementation to check for drift — it is presently **unimplemented** in `sim/thread/`.

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `threadwork_v30.md:651-660` | CANONICAL DEFINITION | Home doc; also declares itself a replacement for two retired predecessor mechanics | Yes |
| `references/glossary.md:186`, `references/mechanical_terms_index.md:694` | HARDCODED DUPLICATE (brief restatement) | Independent one-line restatements | Agree (partial: don't restate Potency/explode detail, just the Coherence cost) |
| `references/wc_survival_spine.md:96,116` | PULLED/REFERENCED | Narrative cross-reference ("Harvest = Dissolution Residue collection"), no independent numeric restatement | Consistent |
| `sim/thread/co_movement.py:43,51` | PULLED/REFERENCED (card-text only) | Free-text notes inside `Co-Movement Cards` tuples, not an independent mechanical implementation | Consistent, but doesn't implement the actual bonus-dice/Coherence-cost mechanic at all |

---

## 20. Overweaving

**Home definition:** `threadwork_v30.md:306`: *"**Overweaving:** Each operation after the first in the same contact window: +1 Ob (cumulative). A collapsed overweave: Mending Stability −3 and local Shifting Object risk."* Explicit documented exception: `threadwork_v30.md:448` (R-56): *"Healing operations (W-08 and variants) use accelerated Overweave: each healing operation in the same contact window adds +2 Ob (not +1). Sequence: 1st heal Ob 1, 2nd Ob 3, 3rd Ob 5, 4th Ob 7."* Glossary Part Eight: `Overweaving | — | Penalty state from multiple operations on same configuration in one contact window. +1 Ob per op after first.`

**Divergence check:**
- **Conceptual conflation with a distinct mechanic (Over-Actualisation stacking) under the same name in a live arc-content file.** `references/arcs/arc_register_threads.md:28-29`: *"**ARC-T18 — Overweaving Cascade** ... Two practitioners independently Weave the same configuration in **separate contact windows**: +2 Ob total (stacked over-actualisation)... In mass battle (**RS ×3 multiplier**): stacked over-actualisation produces RS −6 to −12..."* But `threadwork_v30_infill.md:65` explicitly and carefully distinguishes these two mechanics: *"The Overweaving +1 Ob cumulative rule (§2.4) applies only within a single contact window and does not govern separate contact windows — separate windows accumulate **OA stacks**, not Overweaving penalties."* The arc register's title ("Overweaving Cascade") and its mechanical description (two *separate* contact windows) describe exactly the mechanic the design doc calls Over-Actualisation stacking, not Overweaving — a naming conflation between two adjacent-but-doc-distinguished mechanics.
- **The same arc-register entry compounds this with two further staleness issues**: it cites `"RS ×3 multiplier"` for mass battle, but `threadwork_v30.md:45` explicitly states *"[STRUCK — campaign_architecture_v1 §3.1] The ×3 MS multiplier is replaced by a flat additive model"* (flat −1 MS/battle, −2 Cataclysmic). And it uses "RS" throughout rather than "MS" (term 2's finding recurring here). So this single arc-register entry stacks three separate staleness problems: wrong mechanic name (Overweaving vs. OA stacking), a struck numeric model (×3 multiplier), and the retired abbreviation (RS vs MS).

**Classification table:**

| Site (file:line) | Classification | Mechanism / evidence | Agrees with canon today? |
|---|---|---|---|
| `threadwork_v30.md:306` | CANONICAL DEFINITION | Home doc | Yes |
| `threadwork_v30.md:448` (R-56 healing exception) | CANONICAL DEFINITION (documented exception) | Home doc, explicit correction note | Yes — a disclosed, non-hidden variant |
| `threadwork_v30_infill.md:65` (OA-vs-Overweaving distinction) | CANONICAL DEFINITION (clarifying/disambiguating note) | Home-doc-family infill | Yes — this is the text that *correctly* keeps the two mechanics separate |
| `references/glossary.md:187`, `references/mechanical_terms_index.md:695` | HARDCODED DUPLICATE | Independent restatements | Agree with the base +1 Ob rule |
| `references/arcs/arc_register_threads.md:28-29` | HARDCODED DUPLICATE, **misnamed** (labels an Over-Actualisation-stacking scenario "Overweaving Cascade") and doubly stale (struck ×3 MS multiplier; retired "RS" name) | Independent restatement conflating two distinct, doc-differentiated mechanics, plus reuse of a struck numeric model | **Diverges on three independent axes**: wrong mechanic name, wrong (struck) multiplier model, wrong (retired) clock abbreviation |

---

## Summary of the highest-value findings surfaced in this batch

1. **Rendering Stability (RS) is nowhere near as retired as the glossary claims.** It is live, uncorrected, and in several cases the *only* name used in files with canonical status: `params/threadwork.md`'s own "RS Track" section header, the entirety of `thread_horizontal_integration_spec.md` (one of the two files CURRENT.md names as the live Threadwork head), `designs/architecture/scale_transitions_v30.md` (mixed RS/MS in the same doc), live non-stub sim code (`sim/cross_scale/domain_echo.py`'s `rs_delta` field), and `sim/README.md`, which explicitly (and wrongly) lists RS and MS as two separate coexisting tracks.
2. **"Public Instability (PI)" and "Parliament Integrity (PI)" are two different mechanics sharing one abbreviation**, undocumented as a collision anywhere in the glossary's own collision tables, with a prior internal audit (`valoria_holistic_audit.md`) having already caught this and it having gone unresolved since.
3. **The glossary's own Part Two entry for Public Instability has the crisis-direction backwards** relative to every mechanical source (factions_personal_v30.md, the arc register, the editorial ledger, and params/bg/victory.md all agree PI rises toward 10 or 20 as a bad outcome; the glossary states 0 is the loss threshold).
4. **Thread Tension (TT) is not fully retired** despite the design doc's own "Systems Replaced" table claiming full replacement by MS — it is still independently rolled against and modified in `designs/provincial/factions_personal_v30.md`'s live Community Organizing mechanic, with the corpus's own internal tracker (`EDGE-06`) confirming the conversion is a still-open, unexecuted task.
5. **Thread Depth (TD), claimed "REMOVED... Not tracked. Not used." (PP-166), still appears as a currently-listed private faction track** in `designs/provincial/strategic_layer_v30.md`'s cognitive-load analysis.
6. **"Diagnosis" is formally STRUCK in a section header but functionally alive** throughout the rest of the same document family (Priority-4 round slot, Ob modifiers keyed off it, "Collective Diagnosis"), with a dead cross-reference to a nonexistent `params/threadwork.md §Diagnosis` section.
7. **A design doc's own claim about its sim code's bug state is stale by one day** (`threadwork_v30.md:624` says Mending Coherence cost is still wrongly coded; the actual code was fixed 2026-07-07 per its own comment).
8. **A live, self-acknowledged sim bug (`C-TW-3`)** causes Leap failures to wrongly cost Coherence, contradicting both the code's own docstring and the canonical rule.
9. **Institutional Pressure / Invasion Pressure** is a widespread (23 vs 60 files) unresolved naming fork for the same clock.
10. **Church Influence** has three incompatible threshold/starting-value schemes across `ci_political_v30.md` (canonical, CI 28/40/55/60/65/80/100), `params/bg/clocks.md` (stale pre-ED-731-adjacent 30/50/70-74 bands referencing the struck 75-seizure regime), and `params/campaign_modes.md` (CI start 15, thresholds 20/80).

**Files most load-bearing for follow-up correction, in priority order:** `params/threadwork.md` (RS Track header/prose), `designs/threadwork/thread_horizontal_integration_spec.md` (entirely RS-named), `sim/README.md` (RS/MS false-distinct-tracks claim), `references/glossary.md` (Part One TT row, Part Two PI row, Part Eight FR "no TPS" clause), `params/bg/clocks.md` and `params/campaign_modes.md` (stale CI tables), `params/bg/parliament.md`/`params/bg/victory.md`/`params/bg/core.md` (PI/Parliament-Integrity collision), `designs/provincial/factions_personal_v30.md` (live Thread Tension mechanic), `designs/provincial/strategic_layer_v30.md` (stale Thread Depth listing + hardcoded MS-72 examples), `threadwork_v30.md:624` (stale sim-bug claim), `sim/thread/operations.py` (`C-TW-3` Leap-Coherence bug).
