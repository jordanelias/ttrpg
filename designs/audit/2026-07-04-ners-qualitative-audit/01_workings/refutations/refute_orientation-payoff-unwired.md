# Refutation notes — orientation-payoff-unwired

## Finding (restated)
Claim: Orientation only structurally derives CLASH/REINFORCE/CROSS; the CR5
Doubt-Marker / self-Face-backfire payoff is a "design-table commitment the resolver
does not yet consume." Cite: dictionaries.py ~171-228 scope_note; _kernel_tests.py:842-843.
Novelty asserted: KNOWN-UNTRACKED. Criterion Q-robust, P2, bottom-up.

## What the cited text actually says
- `dictionaries.py:228` scope_note IS present and does say "resolver does not yet consume
  orientation (Stage-3 CR5 rhetoric-armature scope)." But this note is scoped to the
  **DOUBT_MARKER terminal-at-close** behavior (ED-1060, an explicitly OPEN-FOR-JORDAN
  decision), and it is a **Stage-2-era** note whose remit is "the flag records the rule for
  **Stage 3 to implement**." It is not a statement about the whole CR5 payoff.
- `_kernel_tests.py:842-843` merely asserts that string is present in the scope_note — a
  self-consistency check on the flag, not evidence the payoff is globally unwired.

## Decisive refutation: the self-Face backfire IS consumed by the resolver
- `rhetoric.py` (header: "Stage 3 / Gate C") defines `cr5_self_backfire`,
  `CR5_BACKFIRE_MAGNITUDE`, `CR5_ORIENTATION_CHANNEL`, `orientation_channel` — CR5 realized
  as **behaviour, not labels**.
- `resolver.py:380` imports `cr5_self_backfire`; `resolver.py:404-419` **calls it on the
  resolution path**: `backfire = cr5_self_backfire(style_key, landed=(deg>=1),
  my_standing=c.face.v)` then `c.face.strip_points(backfire)` with a fault reason. This is
  the exact "self-Face backfire on a failed (deg==0) Obscuring foul" the finding names as
  unconsumed. It is consumed.
- The **ED-1062 ledger entry's own words**: "the now-**wired** CR5 self-Face strip channel."
  Ratified by Jordan, Gate C, 2026-07-02.

So a named half of the "payoff that gives Obscuring its risk/reward shape" — the self-Face
backfire (the RISK) — is implemented and wired. The finding's central factual claim is false
for that half.

## The genuinely-unconsumed residual is narrow, deliberate, and already TRACKED
- The only piece the resolver does not yet apply is the **Doubt Marker's terminal-at-close**
  behavior (an unconsumed marker's −2 at contest close). That is precisely **ED-1060**
  ("Terminal Doubt"), status "OPEN DECISION FOR JORDAN (Gate B; provisional pending Jordan
  ratification)" (`dictionaries.py:200-234`).
- ED-1060 is **tracked**: `handoffs/HANDOFF_SC.md:68-69` records the Terminal-Doubt design
  (banded + tally branches both specified) as an SC-lane item; ED-1060 appears 3× in the
  editorial ledger. The finding's own `tracked_ref` concedes the ED-1060 overlap.
- The opt-in gating (`self.armature.cr5`) is a **deliberate, safeguarded staged rollout**:
  the Stage-0..2 code path is "bit-for-bit unchanged" (armature.py:407) to preserve
  golden-trace byte parity; CR5 fires only under an opt-in armature. This is intentional
  sequencing, not accidental non-wiring.

## Intent
DELIBERATE. Evidence: ratified ED-1062 (Gate C, 2026-07-02) with both CR5 halves kept
together by explicit decision; opt-in armature flag preserving parity; ED-1060 terminal
piece flagged OPEN-FOR-JORDAN with a documented fork + swap. Nothing here is accidental or
unsafeguarded.

## Severity re-judgment vs North Star
Obscuring's risk/reward choice architecture **already exists and is wired** (self-Face
backfire) behind an opt-in flag; the merits path (Revealing→Persuasion) is live. The one
open piece is a tracked Jordan micro-decision on terminal-marker EV in single-exchange
contests (ED-1060). Fixing "this finding" does not materially widen meaningful choice —
the choice is present; only a rollout flag and one open terminal rule remain. Not P2.
Residual is at most a P3: the `dictionaries.py:228` scope_note is now **stale** ("resolver
does not yet consume orientation" reads globally but Stage 3 landed the backfire) — minor
doc debt, and the substantive open item (ED-1060) is already tracked.

## Verdict
REFUTED. Core claim (whole payoff unconsumed) is false — resolver.py:411 consumes the CR5
self-Face backfire (ED-1062 "now-wired"). The narrow true residual = ED-1060 (tracked,
deliberate open decision). Novelty mislabeled KNOWN-UNTRACKED; it is KNOWN-TRACKED (ED-1060).
duplicate_of ED-1060. Revised severity P3.
