# Grounding note: Football Manager — is the instant result the same simulation as the played match?

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: IN (grounding lane for `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

**Why this note exists.** The repository's doctrine documents state that Football Manager is "three fidelities
of one match engine" with an instant result calibrated to the played one. The tree's own check found that
**not established** (`../tutorials/T16_managers_narrative.md:79`; `../dispositions/D_T04.md` rows 57-58;
`../dispositions/D_T02.md` row FM4). Three audit-suite files repeat the claim without that qualifier
(`audits/10_DICE_audit.md:587`, `audits/11_GO_audit_addendum_B.md:286`, `audits/07_SE_audit.md:537`). This
note records a second attempt to settle it. **It is still not established.**

Tags as in `../README.md`.

## Sources

| key | source | read |
|---|---|---|
| OS | *Football Manager 26 Adds Instant Result Option for Matches*, Operation Sports, 2025-10-21, `https://www.operationsports.com/football-manager-26-adds-instant-result-option-for-matches/` | body, 2026-11-12 (the page `T16:79` cites) |
| WP-FM26 | `https://en.wikipedia.org/wiki/Football_Manager_26` (raw wikitext, rev 1382391949 of 2026-10-28) | body, 2026-11-12 |
| search | two searches for a Sports Interactive statement on how Instant Result is computed | snippets only, 2026-11-12 |

Blocked: `community.sports-interactive.com` bug tracker (403); `inkl.com` mirror (403). Not found: any
Sports Interactive manual page, patch note or staff post that says how an instant result is computed.

## What is established

| # | claim | tag |
|---|---|---|
| 1 | An "Instant Result" button was seen in FM26's in-match options; it "would let virtual managers instantly simulate the remainder of a match without watching highlights or sitting through the 3D match engine, effectively offering a 'skip to result' option mid-game". | [V3 OS 2026-11-12] |
| 2 | History, per the same report: Instant Result "was once a staple of popular community mods and skins"; "it appeared in some official versions on console and Touch editions"; on PC "the closest equivalent was going through a match on 'Commentary Only'". | [V3 OS] |
| 3 | At the time of the report "Sports Interactive hasn't formally acknowledged the Instant Result feature". | [V3 OS] |
| 4 | In FM26 "Core simulation elements, including the match engine, tactical systems and player decision-making, continue to rely on SI's proprietary systems rather than Unity itself." | [V3 WP-FM26 2026-11-12] |
| 5 | The viewing ladder (full match, highlight levels, commentary only) is a set of ways to watch one match: sourced in the tree at `D_T04` row 57 and `T16` §8. | tree, V3 there |

## What this note does NOT establish

- **Whether an instant result runs the same match simulation as a watched match.** `?`. No first-party
  statement was found in either pass.
- A reading note on row 1: the report's words are "instantly simulate the remainder" and "without ... sitting
  through the 3D match engine". That describes skipping the *viewing*. It does not say the calculation is
  skipped or replaced. `T16:79` and `D_T04` row 58 summarise the same page as saying the button "bypasses the
  match engine"; the page read here does not use that word and is consistent with either reading. This lane
  does not edit those files; the observation is recorded here.
- Any calibration of instant against played results ("instant ≈ played").
- Anything about editions before FM26 beyond row 2.

## Bearing on the suite

"Three fidelities (or renderings) of one match engine" may be cited only for the viewing ladder (row 5).
The claim that a skipped match and a played match are the same simulation stays **not established** and
supports nothing. The one-resolver rule in the suite stands on Jordan's ruling 1 of 2026-11-12
(`AUDIT_BRIEF.md`) and on the verified precedents `D_T04` row 58 names (Dominions: always simulated; Field of
Glory II: no auto-resolve), as `audits/04_MB_audit.md:824-826` already says.
