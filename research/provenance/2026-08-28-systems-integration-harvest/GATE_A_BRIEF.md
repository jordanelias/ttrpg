# GATE A — adversarial verification of the harvest

You are the ANTAGONIST in an agonist→antagonist relay (CLAUDE.md §10). Eleven harvest agents
read the Valoria design corpus and emitted 1,079 records. You never saw their reasoning — that
is the point. Your job is to TRY TO BREAK their output against the working tree at
`/home/user/ttrpg`.

You have Read, Grep, Glob and nothing else. You cannot write. Report findings; do not fix.

## Where the records are

`/tmp/claude-0/-home-user-ttrpg/d10fce8e-35f0-503e-88b1-0cc6361eac31/scratchpad/run/records/`
— one `.md` per lane (H1, H2, H3, H4, H5, H6, H7A, H7B, H8A, H8B, H9). Each has a `## Manifest`
table (per-file: path, lines, records) and a `## Records` YAML block.

Read `HARVEST_CONTRACT.md` in the parent directory for the schema they were told to follow.

## What you are attacking — in priority order

**1. CITATION TRUTH (highest priority).** Every record carries `source: path:line` and often
`status_evidence: path:line`. Open them. Does the cited line say what the record says?

⚠ **Lane H1 disclosed that it did NOT independently re-open the engine/systems files it cites** —
it took `path:line` values from the proposal documents' own re-verified passes. If H1 is in your
assignment, spot-check its citations hardest. A citation that is merely *inherited* is not
verified.

**2. STATUS TRUTH.** `built` / `stub` / `superseded` REQUIRE `status_evidence` pointing at code.
For a sample of these, grep the named module. Three specific failure shapes to hunt:
- a record claiming `built` for something with no code (the §0.05 trap — a design doc's own
  header saying "BUILT" is not evidence; `systems/npcs/` has ZERO Python files, so any
  `built`/`stub` record sourced there is automatically suspect);
- a record claiming zero callers where callers exist;
- a record claiming a formula matches code where the constants differ.

**3. STALE-vs-OPEN CONFUSION — read this carefully, it is the error the run already made once.**
A finding independently reported by many lanes is NOT thereby true. Six lanes converged on the
"Compact vs Leverage ledger fifth family" collision — and it had ALREADY BEEN RULED, on
2026-07-13, by ED-IN-0046 D3: *"Compact models as a recurring Debt subtype, not a 6th
ledger.TAG_KINDS family: RULED."* The lanes were all reading design prose descended from one
pre-ruling source. **Convergence measured agreement, not truth.**

So: for any record marked `gap` or `audit-finding` that reads like an open question, check
whether a ruling already answers it. The ruling registers are `registers/editorial_ledger*.jsonl`
and `registers/editorial_ledger_archive.jsonl` / `_in_archive.jsonl`. Report any record that
presents a SETTLED question as open. This is the single most valuable thing you can find.

**4. SLICE MISCLASSIFICATION.** The closed 8-value set with its boundary tests:
`primitive` (stores state) · `derivative` (computed, stores nothing) · `formula` (the expression
itself) · `mechanic` (one resolution event) · `process` (several mechanics in mandated order) ·
`ruling` (a Jordan decision) · `content` (named world instances) · `gap` (an absence or
contradiction). Sample ~20 records in your lanes and judge each. Report the misclassification
RATE, not just examples — a rate above ~10% means that lane's classifier was systematically
wrong and the lane needs re-harvesting rather than patching.

⚠ Some lanes emitted slice values OUTSIDE the closed set (`proposed_ref`, `audit_ref`, `stub`,
`audit`). Those are protocol breaches — note them.

**5. COVERAGE.** Each lane's Manifest lists every file with a line count and a record count.
Find rows with high line counts and ZERO records. Open a few. Was the lane right that there was
no in-scope content, or did it miss material?

## What NOT to do

- Do not re-harvest. You are not producing records.
- Do not report a finding you have not opened the file to check.
- Do not manufacture findings. Finding nothing in a category is a legitimate verdict — say so
  and state what you checked. Per `.claude/agents/valoria-critic.md`, a null result plus a
  coverage note is a real answer; padding is not.
- Do not flag a record for being terse. Terse and correct is the goal.

## Your output

    ## Verdicts
    | record_id | verdict | what I checked | what is wrong |
    (verdict ∈ UPHOLD / OVERTURN / SOFTEN / SHARPEN)
    Only list records where the verdict is NOT uphold, plus a count of how many you upheld.

    ## Rates
    - citations checked: N, failed: M
    - status claims checked: N, failed: M
    - slice sample: N, misclassified: M  (→ rate)
    - settled-questions-presented-as-open: list

    ## Coverage holes
    Files with lines but no records that you checked and believe were wrongly skipped.

    ## Coverage note
    What you could NOT check and why. Be explicit about your own limits.
