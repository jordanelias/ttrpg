# Social Contest — Findings (adversarially verified)

**Canonical head:** `designs/scene/social_contest_v30.md` (+ params/contest.md). Live rebuild:
Stages 1a–3/Gates A–C ratified (ED-1055–1062), kernel at `sim/personal/contest/` (13 modules).
Stage 4 (the four deliberative games) re-sequenced after a consequence-spine build per the
2026-07-05 Fable-5 subsystem audit.

## 1. Tracker inventory

Persuasion Track 0–10 banded, hard-clamped (`resolver.py:79-93`); Face (`Face_max=Charisma×3`,
`Face_current=round(Standing/10×Face_max)`, ratified Gate A); Concentration (kernel abstract
`Reserve`, MAX=12 [SEED] — distinct from the params-level attribute formula, an honest
distinction); Adjudicator Armature (4-axis vector, deliberately partial-reveal by design, not an
opacity bug); Stasis (6-rung monotonic ladder); Composure — **RETIRED** (`primitives.py:167-169`
guard) but still cited in the throughline registry and the stale `valoria_ui_ux_v4_1.md`.

**Doubt Marker has no kernel state at all** — confirmed by independent critic re-grep: `[Dd]oubt`
across `sim/personal/contest/` returns only comments/docstrings/design-table strings/test
assertions, zero live state fields. Fully specified in prose (including an unratified Terminal
Doubt edge case, ED-1060) but does not exist as a stateful primitive.

## 2. Interaction chain map

- **CR5 self-Face backfire is confirmed as the ONLY wired Face-strip channel** — independently
  re-verified: every other `strip`/`strip_points` hit in the kernel is a comment, docstring, def,
  or test. Corroborated in-code (`primitives.py:83`: "Standing.strip() is NEVER called in the
  contest kernel"). The general strain→Rattled channel described in prose is simply not wired yet.
- **`parliamentary_vote.py` is a dead-end at campaign scope** — confirmed, with a corrected
  mechanism: it's not that this module has zero callers (it has two production callers,
  `parliamentary_stay.py`/`parliamentary_transfer.py`), but that *those* callers themselves have
  zero callers anywhere in `sim/`, and `mc_v18.py` never touches any of them. The dead-end is one
  hop further out than originally stated — same conclusion, corrected evidence.
- **domain_echo/Chronicle orphaning — REFUTED by same-day landing.** The producer's claim that
  `scene_dispatch.py` "defers every contest scene" via an empty-dict `zoom_out({})`, leaving
  `domain_echo.py` with zero callers, was accurate as of the 2026-07-05 Fable-5 audit but is
  **stale as of today.** **ED-IN-0028 (2026-07-08, PR #92)** wired `echo_transport.py`, which now
  gives `domain_echo.compute_domain_echo` a live caller, and `scene_dispatch.py`'s `contest`
  branch now routes through `echo_transport → domain_echo` when a scheduler is present. The
  `zoom_out({})` empty-dict path survives only as the no-scheduler default. **A materially larger
  reachability gap the producer missed entirely:** the campaign dispatch actually resolves
  contest scenes through `contest_legacy_stub.py`, not the sophisticated 13-module kernel — so
  the kernel's Persuasion Track/CR5/armature machinery is not what a dispatched contest scene
  currently invokes at all. This is a bigger stranding problem than the one originally flagged,
  on a different axis.

## 3. Cascade check

Every numeric chain checked is well-bounded (Persuasion Track hard-clamped; Rattled/Concentration
spiral floored at 1D pool + 2-mark incapacitation cap; Chain Contests hard-stop after 3; armature
δσ soft-capped via tanh). The actual risk is the *opposite* of runaway: the Face-strain→Rattled
feedback loop the prose describes is under-realized, not over-realized — Face is currently
near-monotonic-up in the running kernel, confirmed independently three ways (`primitives.py:83`,
`wrapper.py:288`, and `HANDOFF_SC.md` listing this as a Stage-4 entry criterion not yet built).

## 4. Cognitive load

13 items the player must consult every single exchange (pool size, TN, genre/stasis bonus,
7-faction audience-boost table, 4-axis armature reveal state, opponent Face, own Face/Rattled, own
Concentration/Spent, Persuasion Track position/band, Doubt Marker state, interaction-type
prediction, Recall availability, Momentum available) — **more than 3× the personal-scale 3–4
ceiling**, confirmed present verbatim in the 2026-07-05 Fable-5 dossier. One genuine, unflagged
omission: the stasis/genre match **is** a live resolver input (`resolver.py:384-385`) but has no
depicted UI element on the walkthrough's shown-fields list — a direct, if narrow, violation of the
rebuild's own stated legibility principle ("every number the resolver uses is a number the player
can see before committing").

## 5. Legibility gaps (severity per critic-corrected verdict)

- **P1 — Only Agôn is implemented; the other three game-shapes (Consensus/Negotiation/Inquiry)
  are registered stubs.** Confirmed: `wrapper.py:199-215` `GAMES` router raises
  `NotImplementedError` for all three; `modes.py:326-334` confirms three separate scaffold classes
  also raise `NotImplementedError`.
- **P1 — 13-consult cognitive load vs. the corpus's own 3–4 ceiling** — the biggest legibility
  risk for the one game-shape that exists today, and it will only worsen when Stage 4 adds three
  more.
- **P2 — Doubt Marker has no kernel state** (confirmed above).
- **P2 — Stasis/genre match is a hidden resolver input with no depicted UI element.**
- **P3 — naming/jargon drift:** "Piety Track" (a different, unrelated Conviction-track stat)
  collides with "Persuasion Track"; retired "Composure" persists in the throughline registry and
  the stale `valoria_ui_ux_v4_1.md` (which the Fable-5 audit found specifies the pre-CR3 system
  wholesale); `params/contest.md:98` still reads "Direct/Indirect" against its own ED-897 rename
  to Revealing/Obscuring. No MS-vs-RS naming split reaches contest specifically (checked and
  ruled out — that's a threadwork-lane concern only).

## New finding from adversarial pass

**The single biggest reachability gap in this lane is not the one the producer flagged.** The
campaign's actual contest-dispatch path currently resolves through `contest_legacy_stub.py`
(`__init__.py:35-36`), not the 13-module kernel this and the Fable-5 audit both treat as "the
canonical head." Whatever cognitive-load/legibility work is done on the kernel, it is presently
invisible to an actual playthrough until that dispatch wiring is fixed — a prerequisite this audit
surfaces but does not resolve.
