# Adversarial pass on the consolidation sweep — factuality, impact, method, logic (ED-IN-0156)

## Status: REFERENCE — the attack record for `00_findings.md`

Per §0: producing and checking are different jobs. This document is the attack on `00_findings.md`,
written after it. It records what the attack **killed** and what it **corrected**, not a
reassurance that the findings were reviewed. Three findings did not survive; two survived only in
altered form.

---

## A1 — KILLED: "the week's generators are built and DISCONNECTED"

**The claim, as first drafted.** `build_glossary.py`, `build_engine_atlas.py` and
`build_contract_index.py` — the three generators shipped 2026-08-09..10 — have **zero callers** in
`.github/workflows/`, `.githooks/`, `.claude/settings.json` or `tools/valoria_local.py`. Verified
by grep, and true. The draft concluded this was a third instance of the defect ED-IN-0149 named
three days earlier ("the churn machinery is built and DISCONNECTED"), and made it the headline:
*the repo diagnosed build-then-disconnect on 2026-08-08 and shipped three more instances by
2026-08-11.* It was the most striking finding in the sweep.

**The attack.** Zero callers is a claim about *refresh*. Staleness is the harm. So: what would
actually happen if one of these artifacts went stale? Read the tests instead of grepping for
callers.

**Refuted.**

- `test_engine_atlas.py:46` — `subprocess.run([sys.executable, BUILDER, '--check'])`, asserts
  returncode 0, against the live artifact. Plus a determinism test that re-renders under a
  different `PYTHONHASHSEED`, because a non-deterministic render would make `--check` a coin flip.
- `test_contract_index.py:60-67` — the same `--check` subprocess, same determinism guard. Its
  docstring records that `build_contract_index.py` **shipped exactly that coin-flip defect** (a
  non-total sort over a set difference) and that this is why the guard exists.
- `test_build_glossary.py:111-120` — `test_committed_output_matches_a_fresh_build`: byte-compares
  every committed file to a fresh build, and the JSON counts besides.

All three run inside `pytest tests/valoria`, a **blocking** CI gate. These artifacts cannot rot.

**And the inverted conclusion is the correct one.** A freshness gate is *better* than a scheduled
regenerator: a cron job fixes staleness on someone else's PR a week later, while `--check` fails
the PR that *caused* it. The week's generators are not an instance of the defect — they are the
remedy for it, applied three times. What the sweep should credit, it had drafted as a fault.

**What this cost, and what it teaches.** Three of the four strongest-looking findings in the first
pass were wrong, and **grep is what made them look strong** — "zero callers" is a genuine measured
fact that supports a false conclusion, because the caller for a generated artifact is not
necessarily a scheduler. This is the §0.1-point-1 hazard in a new dress: I grepped for the wrong
relation. The pattern only became visible by reading the tests, which is what "without pattern
matching" has to mean in practice.

**What survived is the contrast, not the claim.** The pattern exists, is proven, and was applied
three times this week — and is *absent* on two older artifacts (F3 `handoff_atomize`, F2
`audit_registry`). F3's strength comes entirely from this: the fix is not speculative, it is a
ten-line copy of what the same week already shipped next door.

---

## A2 — CORRECTED: F2's magnitude was wrong in both directions

**First measurement.** Compared `audit_registry.jsonl`'s `folder` values to disk literally: "22 of
27 registry folders resolve to nothing; 36 of 41 dirs unindexed." Every registry path begins
`designs/audit/…`, and `designs/` was retired 2026-07-19, so the reading was that the registry is
wholesale dangling.

**The attack.** CLAUDE.md §3 states old `designs/…` paths resolve via a dir-prefix alias. If that
row exists, "resolves to nothing" is false and the finding is largely an artifact of my not
applying the repo's own resolution rule.

**Confirmed against me.** `references/restructure_ledger.md:981` carries
`| designs/audit/ | audit/ |`. Re-measured with prefix resolution:

| | first pass | corrected |
|---|---|---|
| on-disk dirs with no registry row | 36 of 41 | **34 of 41** |
| registry dirs pointing at nothing | 22 of 27 | **10 of 17** |

The corrected coverage gap is slightly *smaller*, the dangling count substantially smaller, and the
denominator changed too. I would have shipped a number wrong in both directions and a mechanism
("the paths are dead") that was simply false — the real mechanism is that the rows were never
updated when the evacuation removed their subjects, which is a different and more precise defect.

**What strengthened under attack.** The gate. `ci_audit_registry_check.py` reports 3 findings
against a 34-unit gap — not a threshold choice but a structural one: it filters to entries dated
newer than the registry's own latest date, so it can only ever inspect the tail. That survived
scrutiny and is the more serious half of F2.

---

## A3 — CORRECTED: F1's premise was wrong; its disposition happened to be right

**First reading.** Five `_data.js` files hold byte-equal payloads to five `.json` files —
"gratuitous duplication, delete the wrappers."

**The attack.** Why would anyone hand-roll this three times (as `obs_core`'s docstring records)
if it were pointless? Look for a reason before calling it waste.

**Refuted.** It is the `file://` workaround: a double-clicked local page cannot `fetch()` a local
`.json`. `tools/observability/README.md:56-58` says so directly. The wrapper is load-bearing for
the offline use case.

**The disposition survived on different grounds, and got sharper.** The same README names
`console.html` the primary ("fully self-contained … no server") and `index.html` + `_data.js` the
**"Dev pair (regenerable)"** — the repo's own word. So the argument is not "the wrapper is
pointless" but "the repo tracks 688 KB it labels regenerable, alongside a self-contained bundle
that supersedes it."

**And reading turned up what the first pass missed entirely.** `index.html:185` loads
`review_state_data.js`, which `.gitignore` deliberately excludes. The committed dev pair is broken
in every fresh clone while `console.html` works. That is a better finding than the one I started
with, and grep for "duplicate bytes" would never have produced it.

---

## A4 — SPARED: the 16 flow skeletons are not boilerplate

**Why they were suspect.** Sixteen `*_flow_skeleton_v1.md`, near-identical names, 422 KB, all in
one commit, plus a `subsystem_flow_skeletons_v1.md` that reads like an aggregate of the other
fifteen. Textbook generated duplication by shape.

**What reading showed.** The "aggregate" is the **format specification and roster** — it owns the
anchor rule and the subsystem table that the guard parses; it contains none of the skeletons'
content. Every factual line in a skeleton ends in a `path:line symbol` anchor, and
`tests/valoria/test_flow_skeletons.py` verifies each one against the tree: file exists, lines
exist, and the named symbol actually spans those lines in one of two accepted forms.

This is the highest-integrity documentation in the repo. **Not a finding.** It is also the clearest
case for why the sweep was asked to avoid pattern matching: on names and sizes alone it is the most
prunable-looking thing added this week.

---

## A5 — SPARED: `throughlines_meta` + `_meta_infill` is grandfathered and load-bearing

The pair matches the index+infill convention **retired as a default** by the 2026-07-26 Jordan
ruling (§4), so it reads as migration debt. But `tools/ci_vetting_check.py` — a blocking gate —
cites `references/throughlines_meta.md §8` as the framework it enforces, at three separate call
sites, and `skills/valoria-vector-audit` parses both files. §4 grandfathers existing pairs
explicitly. **Not a finding.**

---

## A6 — Impact claims: which are measured, which are estimated

Honest separation, since §0.1 point 4 says a number without a control is not a measurement:

**Measured** (a command in this session produced it): all byte counts and file counts; the five
`_data.js`↔`.json` identity; 33 `handoff_atomize` findings; 34/41 and 10/17 audit coverage;
CLAUDE.md's 13,963 tokens and per-section split; `ls engine/` showing no `params/`; 8 `.md` files
in `tests/`; 123 apparatus entries / 6 orphaned; 1,221/1,357 and 2,584/3,722 undefined glossary
rows; both SUPERSEDED targets resolving; the pytest and review_core baselines.

**Estimated, and labelled as such in F5** — "conservatively ~1,500 tokens off every session." That
is a projection of an edit not yet made. The 2,392 chars of struck-through rows and the 5,141-char
`systems/` row are measured; how much survives compression is not.

**Asserted from one file's own text, not independently controlled** — F4's claim that the lane
handoffs repeated a defect the root file was archived for. The precedent is quoted verbatim from
`HANDOFF.md`'s History section; that the lane files' growth has the *same cause* is inference from
their size and structure, not a controlled finding.

**Weakest item, and why it is still listed.** F6 (glossary retention). It is correctly guarded, it
is not a defect, and its churn evidence is two commits' diffstats rather than a series. It is in
the register because 3.0 MB is 7% of the tree, and it is ranked last with its guard stated so it
cannot be misread as a fault.

---

## A7 — What I did not verify

Stated plainly rather than left as implied coverage:

1. **The PP-NNN scope mismatch is unreconciled.** My scan found **320 of 527** distinct `PP-NNN`
   numbers cited across live surfaces resolve to no row in `patch_register_active.yaml` or
   `patch_register_index.md`. CLAUDE.md §0 states **433 of 452**. My scan roots are wider
   (includes `audit/`, `tools/`, `tests/`) and my register set may be narrower. **My number
   neither confirms nor refutes §0's.** Both agree a majority do not resolve. I did not reconcile
   the scopes, and I am not asserting §0 is wrong — this is a flag for whoever owns ED-IN-0147.
2. **F1's remediation is unproven in a browser.** I read `index.html`'s script tags; I did not open
   the page. That deleting the `_data.js` leaves nothing else broken is inference from the tag list.
3. **F4's atomization is blocked and I did not test the unblock.** W8 states two Jordan calls are
   outstanding. I did not evaluate whether they still bind — only that the banner bullet and the
   drifted IN summary are separately unblocked.
4. **The two report-only `review_core` failures are uninvestigated.** `vocab.a17 21/29` and
   `stubs.count 24/25`. I did not check whether either intersects these findings.
5. **`audit/` retention was not assessed on merit.** F2 addresses the *index*. Whether 11 MB of
   audit prose should be retained, and on what rule, is a live question (`HANDOFF_IN.md` W9:
   "replace frozen `AUDIT_CUTOFF` with citation-based retention", state: ruling). I deliberately
   did not pre-empt a ruling in flight.
6. **`skills/`, `godot/`, `canon/`, `workplans/` were inventoried, not read closely.** No findings
   from them should be read as "none exist" — only that this sweep surfaced none.

---

## A8 — Method

Solo, no fan-out, no workflow (session constraint). One reading pass over the twelve commits and
the top-level shape, then targeted verification per candidate, then this attack.

**The method's own weakness, stated:** the sweep and the attack were performed by the same context.
§10 is explicit that a critic which never saw the producer's reasoning is more independent, and
`hCritic`/`valoria-critic` exists for precisely this. That was unavailable here. What partly
substitutes is that every finding was re-derived from a command against the working tree rather
than from the draft's prose — which is what caught A1, A2 and A3. It is not equivalent to
structural independence, and the three surviving high-impact findings (F1, F2, F3) would benefit
from an independent read before anything is executed on them.

**Falsifiers, per §0.1 point 3.** Each is a command; if it does not produce the stated result, the
finding is wrong:

| finding | falsifier |
|---|---|
| F1 | parse each `_data.js`, compare decoded object to its `.json` — any DIFFER refutes it |
| F2 | resolve registry folders through `restructure_ledger`'s `designs/audit/` prefix, diff against `ls audit/` |
| F3 | `python3 tools/handoff_atomize.py --all --check` → non-zero with 33 issues, while `pytest tests/valoria/test_handoff_structure.py` passes |
| F5 | `ls engine/` shows no `params/`; `find tests -name '*.md' \| wc -l` → 8 |
| F6 | `test_build_glossary.py::test_committed_output_matches_a_fresh_build` passes — this is the falsifier *against* reading F6 as a defect |
| A1 | `grep -n 'BUILDER.*--check' tests/valoria/test_engine_atlas.py tests/valoria/test_contract_index.py` — if absent, my retraction is itself wrong |

---

## A9 — A process failure in this sweep, and one residual the sweep's own commit produced

**The process failure, stated plainly.** `pytest tests/valoria` was run **once, as the opening
baseline, before any file in this sweep existed**. After writing the audit documents and appending
to four registers I ran `tools/valoria_local.py --staged` (which passed) but **did not re-run the
suite** — `valoria_local` does not include it. The PR body was then written claiming the suite green.
It was green *at `c26a22c`*, not on the commit it was cited for. CI caught it in four minutes:
`test_engine_atlas.py::test_atlas_is_current` failed on the pushed head.

This is §0's "close the loop, honestly" failing at the last step, and it is worth recording in the
same document that credits `--check` guards for catching staleness — **the guard worked, and the
person invoking it did not.** A green claim I did not verify is exactly what §0 says is worse than a
red one I did.

**The residual it exposed.** `references/ENGINE_ATLAS.md` §identifier-ambiguity counts **bare
occurrences of every contract name across the whole corpus**. `audit` is a contract name. So *any*
document that uses the ordinary English word "audit" — including an audit's own findings file —
moves the count and turns the committed atlas stale, failing a blocking gate until it is
regenerated. Measured here: adding these two files moved `audit` from **2183 → 2186** and nothing else.

That is not a defect in the gate — the count is a real ambiguity signal, and it is precisely the
signal `proposals/canonical_nomenclature_v1.md` (PROPOSED, #301) exists to address. It is a
**coupling cost worth naming**: the atlas is a function of all prose in the tree, so every
prose-adding PR in any lane inherits a regenerate-and-commit step for a file it has no other
relationship to, and the resulting diff line is indistinguishable from a substantive atlas change.
Filed as an observation for whoever takes the nomenclature proposal forward; **not** proposed as a
change to the gate here.
