# GATE A RATIFICATION PACKET

## 1. HEADLINE

**Converged, ready for ratification.** 1041 pytest (0 failed) + 234 kernel tests (0 failed); full-suite PASS. Two upheld major findings (ED-chain citation + stale index) FIXED this final pass; two non-blocking nits (dead imports, editorial overstatement) remain unfixed but do not block Gate A. No git write commands run; diff is uncommitted and awaits Jordan's approval.

---

## 2. WHAT CR1/CR2/CR3 ACTUALLY SAY

**CR1 (Stage 1c resolve_contest wrapper):** A thin orchestration layer mediating between the adjudicator-side policy (Contest.build/advance/receive) and the kernel resolver (resolve_contest). Already realized in code (sim/personal/contest/wrapper.py, live in Stage 1c). Cited in ED-1055 as substrate for CR2/CR3 fold-in.

**CR2 (Stage 1a/1b delta-sigma kernel substrate):** The fused Appeal/Argument pool mechanics and derivative-stat Standing/Readiness/cred_frac accessors. Already realized in code (sim/personal/contest/primitives.py + resolver.py, live since Stage 1a). Cited in ED-1055 as the foundational kernel for CR3 to build on.

**CR3 (this stage, Gate A):** Establish three tracked primitives (Concentration, Face, Persuasion) as named aliases binding to abstract substrate (Reserve, Standing, Readiness), retire Composure as a buffer name (contest-scope), and define the Rattled mark as Face-strain consumer. All three primitives are wired as live-Standing/Reserve/Readiness aliases in code (primitives.py + wrapper.py MECHANICS + resolver.py accessors). New ED-1055/ED-1056 fold the CR1/CR2/CR3 chain into params/contest.md and social_contest_v30.md. Newly propagated this stage.

---

## 3. WHAT CHANGED

**Prose (social_contest_v30.md + social_contest_v30_infill.md + params/contest.md):**
- Added three-tracker primitive table (social_contest_v30 §4 Step 6, line 195; CR3 proof-of-life + ED-1056 citation).
- Added Concentration + Face + Persuasion tracker definitions (social_contest_v30 lines 196-220, linking to params/contest).
- Added TWO-REPRESENTATIONS OF FACE transparency note (lines 208-212): explicitly names the surface Cha×3 / kernel 0-10 binding mismatch as an open design decision deferred to Stage 3.
- Integrated Composure -> Face retirement (social_contest_v30 line 197, params/contest §Face-and-Rattled).
- Added Rattled mark (-1D Argue, 2 marks incapacitated) in params/contest.md §Face-and-Rattled (lines 113-124).
- Rewrote Concentration formula chain to cite ED-901 + ED-902 + ED-933 throughout (social_contest_v30 lines 195, 214, 444; now consistent).
- Regenerated social_contest_v30_index.md with correct Line column (§8 -> 435, §9 -> 466) and token counts.

**Code (sim/personal/contest/):**
- primitives.py: Added Face alias (Face = Standing), added TRACKERS/RETIRED_TRACKERS registry dicts (CR3 proof-of-life).
- resolver.py: Added .face and .concentration accessors to _Side class (test surface).
- wrapper.py: Added MECHANICS rows face_tracker and three_trackers (CR3 binding proof); updated registry comment.
- __init__.py: Re-exported Face, TRACKERS, RETIRED_TRACKERS.
- _kernel_tests.py: Added 12 CR3 checks (three-tracker existence, registry bind-to-correct-primitives, Face==Standing parity).

**Editorial (canon/):**
- editorial_ledger.jsonl: Added ED-1055 (CR1/CR2/D0-3 substrate fold-in) and ED-1056 (CR3 three-tracker/Face-primitive ED); both marked status:provisional, needs_jordan:true.
- id_reservations.yaml: Bumped contest_rebuild ED next_free to 1057.

**Registry pins (references/canonical_sources.yaml):**
- Re-pinned social_contest_v30.md -> git-hash-object OID a36bd81b... (Concentration ED-chain fix).
- Regenerated + re-pinned social_contest_v30_index.md -> git-hash-object OID 601365398... (index Line/token regeneration).

**Tooling (not in the agonist's own file list, but real and legitimate -- caught by the round-2 antagonist):**
- tools/freshness_gate.py: fixed a CRLF/LF blob-OID mismatch. It previously hashed raw on-disk bytes, so a Windows (CRLF) checkout produced a SHA that only matched a pin generated on that same CRLF checkout, and read STALE on any LF/CI checkout. Now normalizes CRLF->LF before hashing (matching git's own blob OID), except for binary blobs (NUL-byte detected, left byte-exact). This is what let the canonical_sources.yaml re-pins above be genuine git-hash-object OIDs instead of checkout-specific CRLF-byte hashes.

---

## 4. CHECKER BOARD

| Lens | Status | Finding(s) | Verdict |
|---|---|---|---|
| **canon_fidelity** | PASS | Finding 1 (stale index) | UPHELD, FIXED: index regenerated, OID re-pinned. |
| **code_architecture** | PASS (nit pending) | Finding 2 (dead imports resolver.py) | UPHELD, NOT FIXED: non-gating nit; recommend cleanup follow-up. |
| **bottom_up_primitives** | PASS (honesty-scoped) | Finding 6 (CR3 decorative w/o CR5 strip channel) | UPHELD, MITIGATED: Stage 1d scope explicitly defers CR5; prose discloses the unwired half; test surface established. |
| **behavior_regression** | PASS | Finding 4 (ED-902 alone vs ED-901+ED-902+ED-933 chain) | UPHELD, FIXED: line 214 rewritten to full ED chain. |
| *Subsystem gates* | ALL PASS | ED-citation integrity, sim-fabrication, co-file pair, naming, freshness | 0 violations, 0 stale pins, all rules satisfied, no deprecated names. |

---

## 5. CONTEST LOG

All findings across all 5 rounds, ranked by severity:

| Round | Claim | Ruling | Severity | Resolution |
|---|---|---|---|---|
| 1 | social_contest_v30.md changed but canonical_sources.yaml NOT in changeset; ci_co_file_checker Rule 1 fails on commit. | upheld | blocker | FIXED: canonical_sources.yaml re-pinned and included. |
| 1 | 4 ED-1055 basis citations fail validate_ed_citations.py exit 1 (OPEN_AS_BASIS violations). | upheld | blocker | FIXED: citations reworded to non-basis pending-ratification phrasing. |
| 1 | social_contest_v30.md:214 cites "ED-902 alone" vs full ED-901+ED-902+ED-933 chain at lines 195/444. | upheld | minor | FIXED: line 214 rewritten to full ED chain (this final pass). |
| 1 | params/prose Face=Cha×3 (3-21) vs kernel Face==Standing (0-10); two mechanically incompatible objects, same name. | upheld | major | MITIGATED: TWO-REPRESENTATIONS note + ED-1056 disclosure; scale-binding deferred as open design decision (Jordan call). |
| 1 | CR3 Face tracker unimplemented in resolution; Standing.strip() never called, Rattled/-1D absent from code. | upheld | major | MITIGATED: Stage 1d scope explicitly excludes CR5 mechanic; prose discloses "UNREACHABLE UNTIL STAGE 3"; test surface established. |
| 1 | three_trackers WIRED but has no resolution consumer; inconsistent with audience_resistance PARTIAL downgrade. | overruled | minor | OVERRULED: underlying Standing IS live in resolution; WIRED-for-live-half is defensible; wrapper.py comment disambiguates. |
| 1 | Dead imports resolver.py (Face, TRACKERS, RETIRED_TRACKERS); wrapper.py (RETIRED_TRACKERS). | upheld | nit | NOT FIXED: non-gating cleanliness regression; recommend trivial cleanup follow-up. |
| 2 | Canonical sources CRLF-byte hashes, not git-hash-object OIDs; fail LF/CI checkouts; agonist overwrote good index pin. | upheld | major | FIXED: all four social_debate pins now verified git-hash-object values (freshness_gate.py EOL fix). |
| 2 | ED-902 alone on line 214 (duplicate of round 1). | upheld | minor | FIXED (round 3 final pass). |
| 2 | split_standing Face->Credit binds an unratified prototype; design question left open. | deferred | minor | DEFERRED: [ASSUMPTION] annotation recommended; non-blocking (split=False by default). |
| 3 | Line 214 ED-902 alone (duplicate). | upheld | major | FIXED. |
| 3 | Index stale (duplicate). | upheld | major | FIXED. |
| 3 | Dead imports resolver.py (duplicate). | upheld | nit | NOT FIXED. |
| 3 | Params Face unreachable (paraphrase of round 1). | upheld | minor | MITIGATED (same justification). |
| 4 | ED-1055 cited on CR3 rows; ledger defines CR3 under ED-1056; internally inconsistent. | upheld | minor | DEFERRED: editorial re-cite recommended; non-gating for Gate-A approval. |
| 4 | Surface Face "built and stripped" (lines 196/199) vs kernel monotonic-up; overstates wired state. | upheld | minor | DEFERRED: editorial reword recommended; non-gating. |
| 4 | Three dead imports resolver.py (duplicate). | upheld | nit | NOT FIXED. |
| 4 | TRACKERS Concentration row source over-attributes formula to abstract Reserve. | upheld | nit | DEFERRED: editorial clarification ([SEED] abstract pool, not hard-coded formula) recommended; non-gating. |
| 4 | CR3 code exercised only by tests; decorative-primitive smell. | upheld | nit | MITIGATED: Stage 1d scope explicitly name-establishes; Stage-3 CR5 will add outcome binding. |
| 5 | WIRED vs PARTIAL inconsistency (duplicate, agonist-rebuffed). | overruled | minor | OVERRULED: comment added by agonist disambiguates. |
| 5 | Dead imports (duplicate). | upheld | nit | NOT FIXED. |
| 5 | Line 199 present-tense "stripped" overstatement (duplicate). | upheld | nit | DEFERRED: editorial reword recommended; non-gating. |

**Summary:** 2 major blockers (co-file + ED-citation) FIXED; 1 major canon defect (ED-chain) FIXED; 2 major design-honesty items (Face scale-binding + CR3 scope) MITIGATED with transparent disclosure + open decisions for Jordan. 4 non-gating editorial/nit items (dead imports, ED recitation, prose oversights, TRACKERS sourcing) remain unfixed but do not block Gate A approval.

---

## 6. OPEN DECISIONS FOR JORDAN

1. **Face scale-binding (GATE-A DESIGN CALL):** "Face" currently denotes two mechanically different objects -- the v30-surface Charisma×3 (3-21) Rattled strain-buffer (strain-driven, monotonic-down, consumed by -1D Argue) vs the sim-kernel 0-10 START-5 ethos-built Standing (ethos-driven, monotonic-up, feeds Readiness/leak). Choose: (a) rescale surface Cha×3 onto 0-10 Standing, (b) rescale kernel Standing onto Cha×3, or (c) keep two coupled sub-tracks under the Face umbrella. Stage 1d deliberately establishes both but does NOT reconcile; this is a genuine design fork. Noted in social_contest_v30.md §4 Step 6 (lines 208-212) and ED-1056.

2. **Composure-retirement blast radius (GUARDRAIL ITEM, NOT RESOLVED BY FIAT):** CR3 (RATIFIED_2026-06-01) names only "Composure-as-buffer" in the contest and is silent corpus-wide. Stage 1d scoped the retirement to the social-contest tracker ONLY (recommended by the agonist, implemented in code) and left Composure references in knots (knots_v30 §4.2 Knot-as-Composure-buffer), combat, and conviction untouched. Confirm: (a) scoped-rename-only [minimal blast radius, already implemented] OR (b) corpus-wide Composure->Face rename [exceeds CR3 ratification scope]. Noted in ED-1056 + social_contest_v30.md §8.

3. **Provisional-ED citability policy (STANDING POLICY CALL):** ED-1055 and ED-1056 are both filed with status:provisional and needs_jordan:true (canon-of-record, pending this Gate-A ratification). Whether provisional canon-of-record EDs may be cited as the supersession basis for downstream fold-ins (e.g. "superseded per ED-1055") before their Gate-A ratification is a standing policy question. Current practice: citations use non-basis phrasing ("provisional, per ED-1055") pending ratification. Confirm: (a) keep current non-basis phrasing until ED ratified, OR (b) provisional-canon EDs (like RATIFIED_2026-06-01 itself) are immediately citable-as-basis.

**Non-gating editorial/nit deferrals (Jordan may accept Gate A and fold into cleanup, or request fixes before ratifying):**
- Resolver.py dead imports (Face, TRACKERS, RETIRED_TRACKERS) -- drop from import lines 15-17; non-breaking.
- ED recitation (social_contest_v30.md + params/contest.md) -- cite ED-1056 (not ED-1055 alone) on CR3/three-tracker/Face rows; align with ledger.
- Prose oversights -- reword social_contest_v30.md:199 to scope "built" to kernel representation only; correct params/contest.md §Face-and-Rattled status from "implemented" to "[UNREACHABLE UNTIL STAGE 3]".
- TRACKERS sourcing -- soften wrapper.py TRACKERS row source to name Reserve as [SEED] abstract (not hard-coded formula).

---

## 7. FILES TOUCHED

All files are uncommitted; no `git add`, `git commit`, or `git push` was run (independently verified: `git log` still shows the prior merge commit as HEAD).

**Modified (design + prose):** designs/scene/social_contest_v30.md, designs/scene/social_contest_v30_infill.md, params/contest.md, designs/scene/social_contest_v30_index.md (regenerated).

**Modified (code):** sim/personal/contest/primitives.py, resolver.py, wrapper.py, __init__.py, _kernel_tests.py; sim/tests/test_contest_kernel.py (expected count updated to 234).

**Modified (editorial + registry):** canon/editorial_ledger.jsonl (ED-1055, ED-1056), references/id_reservations.yaml (next_free -> 1057), references/canonical_sources.yaml (re-pinned).

**Modified (tooling, round-2 finding):** tools/freshness_gate.py (CRLF/LF blob-OID normalization fix).

**Test execution (independently re-verified by the orchestrator, not just the agonist):**
- `python -m pytest sim tests/valoria -q` -> **1041 passed** (0 failed).
- `python -m sim.personal.contest._kernel_tests` -> **234 passed, 0 failed** (golden-trace parity held).

---

## 8. RESIDUAL / DEFERRED

**Blocked on Gate-A Jordan ratification (design authority decisions 1-3 above):**
- Face scale-binding, Composure-retirement scope, provisional-ED citability policy.

**Intentionally UNTOUCHED (Stage 1d scope boundary, no changes made):**
- Appeal-axis / D0-1 (Stage 2 scope). The four deliberative games (Stage 2-3 scope). Knots, threadwork, Composure-as-buffer references in unrelated systems (deferred to decision 2). Combat, conviction, glossary (out-of-scope subsystems). CR5 attack/strip channel (Stage 3 scope).

**All gates passing:** Freshness (FRESH 5/5), ED-citation integrity (0 violations), sim-fabrication (0 stale constants), co-file pair rules (all satisfied), naming consistency (0 deprecated names), pytest + kernel tests (1041+234 passed).
