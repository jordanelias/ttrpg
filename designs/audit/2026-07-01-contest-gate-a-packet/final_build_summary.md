Both upheld findings are fixed; no git add/commit/push was run.

# Stage 1d / Gate A â€” REVISED (both upheld findings fixed; uncommitted proposal)

**Tests:** `python -m pytest sim tests/valoria -q` â†’ **`1041 passed in 80.90s`** (0 failed). Kernel suite direct (`python -m sim.personal.contest._kernel_tests`) â†’ **`RESULT: 234 passed, 0 failed`** (golden-trace parity held; CR3 three-tracker checks pass). **No git add/commit/push was run.**

## Upheld findings â€” how each was fixed

**Finding 4 (major, behavior_regression) â€” mis-cited ED chain at `social_contest_v30.md:214`.** The Concentration formula line cited `ED-902 2026-06-04` alone, omitting ED-901 + ED-933 â€” the exact D0-minor error the contract forbids. Rewrote line 214 to the full mandated chain, matching siblings 195 and 444:
> `(Canonical per derived_stats_v30 Â§14.1: ED-901 (STRUCK FocusÃ—3) + ED-902 (coefficients + Cognitionâ†’Focus engine fix) + ED-933 (params propagation); supersedes the struck Focus Ã— 3.)`

Verified all three ED-902 occurrences (lines 195, 214, 444) now carry the full ED-901 + ED-902 + ED-933 chain. Pure citation-text fix, no mechanical change. This moved the canonical v30 blob OID â†’ `5e6ebc8bb704716b18412b522cb3ce8ce8be79c3`.

**Finding 1 (major, canon_fidelity) â€” stale co-filed `social_contest_v30_index.md`.** The index Line column and token counts were never regenerated after the CR3 insertion (index said Â§8 @ 293 / Â§9 @ 306; actual 435 / 466). Regenerated the whole index via the canonical `tools/doc_index_gen.py` pure function against the current file. The index now records **Â§8 @ line 435, Â§9 @ line 466** (exactly the finding's actual values), with correct token sizes and a matching internal `canonical_sha: 5e6ebc8bb704` header. Regeneration also picked up heading rows that were stale from *prior* work (Â§7.2, Â§7.3, renamed Â§9.6) â€” the index is now fully faithful, not just line-corrected. Re-pinned its blob OID in `canonical_sources.yaml` â†’ `59b011a0ce7785b633c0b1a6d38585ef7d63659f`.

`git hash-object` was verified to equal `freshness_gate.get_blob_sha` for both files (5e6ebc8bâ€¦ and 59b011a0â€¦), so the pins resolve on both CRLF and LF checkouts.

## Gate status after fix (verbatim)
- **Freshness (social_debate):** `[GATE PASSED] All canonical sources are current.` â€” `FRESH: 5 / STALE: 0 / NO-SHA: 0`, exit 0 (all five pins FRESH incl. the two re-pinned OIDs)
- **ED-citation integrity:** `0 citation-integrity violation(s); 242 open-reference info.`
- **Sim-fabrication:** `[SIM-FABRICATION OK] 8 sim file(s) scanned, all constants cited.`
- **Co-file:** `Co-file check: all rules satisfied.`
- **Naming:** `Naming check: no new use of a deprecated name.`

## Open decisions surfaced for Jordan at Gate A (carried, unchanged â€” none decided unilaterally)
1. **Face scale-binding:** ChaÃ—3 (3â€“21) surface buffer vs 0â€“10 kernel Standing â€” rescale-to-kernel / rescale-to-surface / two coupled sub-tracks.
2. **Composure-retirement blast radius:** scoped-to-contest-tracker-only [implemented, recommended] vs corpus-wide. Knot/combat/conviction references deliberately untouched.
3. **Provisional-ED citability policy:** whether provisional canon-of-record EDs (ED-1055/ED-1056, both `needs_jordan: true`) may be cited as basis.

## Every file created or modified this stage (14, all uncommitted; absolute paths)

Fixed **this pass** (the two upheld findings):
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\designs\scene\social_contest_v30.md` â€” Finding 4: line 214 ED chain corrected to ED-901 + ED-902 + ED-933 (also carries prior-pass CR3 trackers + Face two-representations note).
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\designs\scene\social_contest_v30_index.md` â€” Finding 1: fully regenerated (Line column Â§8â†’435 / Â§9â†’466, token counts, internal canonical_sha header 5e6ebc8b).
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\references\canonical_sources.yaml` â€” re-pinned social_contest_v30.md â†’ `5e6ebc8bâ€¦` and social_contest_v30_index.md â†’ `59b011a0â€¦`; comment updated to reflect the regeneration + citation fix.

Carried from prior passes (unmodified this pass):
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\tools\freshness_gate.py` â€” LF-normalizing blob-OID hasher (CRLFâ†’LF + NUL binary guard); corrected docstrings.
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\canon\editorial_ledger.jsonl` â€” ED-1055 + ED-1056.
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\designs\scene\social_contest_v30_infill.md`
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\params\contest.md` â€” Face-and-Rattled + CR1/CR2 substrate notes.
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\references\id_reservations.yaml` â€” contest_rebuild ED next_free 1057.
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\personal\contest\primitives.py` â€” CR3 block + scope-honesty comment.
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\personal\contest\wrapper.py` â€” face_tracker WIRED comment.
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\personal\contest\resolver.py` â€” `.face`/`.concentration` accessors.
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\personal\contest\__init__.py` â€” Face/TRACKERS re-exports.
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\personal\contest\_kernel_tests.py` â€” +12 CR3 checks.
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\tests\test_contest_kernel.py` â€” expected count 234.
