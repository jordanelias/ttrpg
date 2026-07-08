# Handoff — SC (Social Contest)

Lane-scoped continuity for the `SC` (social contest) lane, per the `ED-<LANE>-NNNN` namespace
(`ED-IN-0001`) and `CLAUDE.md` §3's session-lane-scoping convention. Root `HANDOFF.md` is the
index; see it for cross-lane/global items.

## Pending

- **Auto/Manual Resolution Duality doctrine DRAFTED 2026-07-08 (ED-SC-0013, PROPOSED — Jordan asked me to
  draft his Total-War auto/manual framing).** `designs/architecture/auto_manual_resolution_duality_v1.md`:
  the zoom in/out protocol IS the auto-resolve/play-it-out toggle; the Parliamentary vote (ED-SC-0006/0007)
  is the first auto-resolver, the personal contest kernel its played counterpart. **Load-bearing constraint:**
  E[auto]≈E[played] on matched inputs (exploit-prevention — no mode-shopping), acceptance oracle = a NEW
  parity harness. **Reframes ED-SC-0011** as the zoom-in expansion (derivation calibrated to the auto-resolver;
  parity harness = its acceptance gate) — makes the previously-undefined party-derivation well-posed. Open
  forks A-D (one-engine-vs-two / escalation predicate / calibration tolerance / player-layer) are needs_jordan.
  For Jordan's review (in PR #95); merge ratifies the doctrine, forks stay open.
- **Social-contest staged rebuild (`claude/happy-shaw-da0f1d`, IN PROGRESS).** Agonist/antagonist gated rebuild
  of the contest engine: promote the stranded 62-test groundup engine (`designs/audit/2026-06-03-contest-groundup/`,
  actually **9 modules / 151 tests green**) onto the v30 surface + fold in CR1–CR7, build all four deliberative
  games (Agôn/Negotiation/Inquiry/Consensus), close J-36 seams, drive to settled canon (T-25 + sim-validation).
  Plan: `C:\Users\Jordan\.claude\plans\this-is-a-broader-nested-mountain.md`. Runs stage-by-stage via the Workflow
  tool (Opus agonist/antagonist/judge + Haiku scribe), Jordan ratifies each gate; cadence = auto-advance, interrupt
  only for design-authority forks.
  - **Stage 0 (Foundation) DONE + Gate 0 RATIFIED (2026-06-30).** Reconciliation contract + decisions:
    `designs/audit/2026-06-30-contest-stage0-reconciliation/DECISIONS.md` (+ raw map + gate packet). Three ratified
    forks: **D0-1** appeal ethos/pathos/logos = build both multiplicative+additive behind a flag, decide by seeded
    A/B (player-win-rate vs venue-identity-spread); **D0-2** σ-leverage → new numpy-free `sim/autoload/sigma_leverage.py`
    sibling (retires the test-dir/numpy/sys.path-hack + the two-σ-kernels debt); **D0-3** TN6/7/8 divergence + Jordan's
    fractional-Ob idea → contest stays δσ TN7 (unaffected), open a substrate probe (reopens CR6 uniformity), non-blocking.
    Good news: `faction.py` already has BG-Vote/Succession/committee-band → Consensus mostly promote-existing.
    IDs reserved: `contest_rebuild` = ED 1055-1079 / PP 800-809.
  - **Stage 1a DONE + committed (d64e2ffe).** `sim/autoload/sigma_leverage.py` — numpy-free σ sibling, byte-identical
    to the oracle, 623 tests green; two-σ-kernels debt retired.
  - **Stage 1b DONE + committed.** 9-module kernel promoted to `sim/personal/contest/`, rewired onto the σ sibling
    (no third kernel); `degree` = clean carry-across (pool-aware integer degree added to sigma_leverage, distinct from
    `dice_engine.Degree` combat enum); old stub → `contest_legacy_stub.py`; 815 sim tests + both importers green.
  - **D0-3 RESOLVED → HYBRID** (present-as-Ob display over the δσ substrate; CR6 upheld, not reopened). Memo:
    `designs/audit/2026-06-30-contest-fractional-ob-probe/MEMO.md`; decision → ED-1055. Probe also surfaced a LIVE
    combat bug (`dice_engine.roll_pool` ignores `tn`; TN5/6/8 weapons rolled at TN7 rate) → spun out as a
    combat-lane task (`task_210994b7`, out of contest scope — see `handoffs/HANDOFF_PC.md`).
  - **Stage 1c DONE + merged into main (PR #44, all CI green).** v30 re-skin (8 proceedings, Persuasion Track
    banding, 4 adjudicator types) + `build_contest`/`resolve_contest` wrapper + MECHANICS registry, mirroring
    `tests/sim/mass_battle/engine.py`. 888 tests green.
  - **Stage 1d / Gate A DONE — 3 forks ratified by Jordan (2026-07-01).** Propagated CR1 (wrapper, confirmed
    already-realized)/CR2 (σ-substrate, confirmed already-realized)/CR3 (three trackers: Concentration+Face+
    Persuasion, Composure retired — contest-scope only) into prose (`social_contest_v30.md` §4/§8 + co-files,
    `params/contest.md`) + code (`sim/personal/contest/` Face primitive) + ledger (ED-1055, ED-1056). Packet:
    `designs/audit/2026-07-01-contest-gate-a-packet/GATE_A_packet.md`. **Ratified:** (1) Face scale-binding =
    combo formula, not a straight rescale — `Face_max = Charisma×3` (ceiling, player-build-controlled) +
    `Face_current = round(Standing/10 × Face_max)` (position within ceiling, earned through play, Standing's
    kernel math/Readiness/leak feed untouched); (2) Composure retirement scoped to the contest tracker only
    (knots/combat/conviction untouched, confirmed); (3) provisional EDs use non-basis citation phrasing until
    ratified (standing policy). A small Sonnet-tier finalize pass is applying the resolved formula + 4 agreed
    nits (dead imports, ED-1056 recitation, prose wording, TRACKERS sourcing); that pass also caught the ratified
    Face formula shipped with zero test coverage and added 10 targeted kernel checks (boundary cases, midpoint
    round-half-to-even, non-mutation, live-tracking). **Committed (884cf89a).** 1041 sim+valoria + 244 kernel
    checks green. Push to `claude/happy-shaw-da0f1d` updates the open tracking PR ([ttrpg#44]) — Jordan merges,
    not this session.
  - **NEW standing requirement (decision 5, 2026-07-01): the player-interaction model is a concrete deliverable,
    not a late audit.** First-draft walkthrough seeded ahead of Stage 6 so every later stage designs toward it:
    `designs/audit/2026-07-01-contest-player-interaction/player_interaction_walkthrough_v1.md` — setup screen,
    the exchange loop (Appraise / style-choice cards / roll-and-resolve / Face+Concentration bars), the
    resolution screen, and how Negotiation/Inquiry/Consensus should each look different from Agôn's track meter
    so Stage 4 doesn't converge them onto one UI. Stage 2 now owns authoring the Style/Venue flavor text; Stage 3
    now owns the Appraise-reveal boundary for `armature_position`; Stage 4 now owns each game's interaction
    shape; Stage 6 finalizes+ratifies the model this seeds. Plan file amended accordingly.
  - **Gate A committed (`884cf89a` mechanics + `98ecdf41` player-model), PR #44 all-green.**
  - **Stage 2 / Gate B (dictionaries) DONE + committed.** Built Venue×8 / Adjudicator×4 / Style×4 /
    InteractionType×4 typed dicts (`sim/personal/contest/dictionaries.py`, new module) + Style/Venue
    flavor text; closed ED-137 (Panel adjudicator). Packet:
    `designs/audit/2026-07-01-contest-gate-b-packet/` (pre-ratification snapshot + the authoritative
    `GATE_B_closeout_audit.md`). **Ratified and independently re-verified in actual code (not just ledger
    text):** Panel votes weighted-by-standing (ED-1057; reuses the existing `Adjudicator.discipline` field,
    NOT the contestant `Standing` name — no new state invented); Panel reachability = rebind Guild
    Arbitration's adjudicator → Panel (ED-1059; NO appeals — "let the decision ride"; roster stays 8);
    Terminal Doubt = terminal-value-everywhere, banded (PersuasionTrack) + tally (TallyAtClose) branches
    both specified (ED-1060); Guilds "GM picks" boost = context-derived from the venue's dominant
    ethos/pathos/logos via the existing `Appeal` machinery (ED-1061; literal "GM picks" text removed from
    both prose heads). ED-1055/1056/1058 flipped to `status: ratified` (a bookkeeping fix — they were left
    `provisional` only because two earlier finalize-workflow attempts were killed by infrastructure
    issues — API 401/529 errors and a background-task stop, unrelated to the work itself — before
    flipping their own metadata; the ratifications themselves happened earlier via Jordan's answers).
    1041 sim+valoria + 319 kernel tests green; freshness gate clean (5/5 fresh); no scope drift (grep
    confirmed knots/combat/conviction untouched, Composure retirement still contest-scoped).
  - **SOURCE-RESEARCH GROUNDING (found 2026-07-01 via files13.zip → already in repo, NOT orphaned).** The
    deliberation-critique source research
    `designs/audit/2026-06-28-social-contest-deliberation-critique/source-research/` (a 3-part
    Renaissance-deliberation / machination-games-lens / model-testing trilogy) is READ-AND-CITED-BUT-NOT-APPLIED:
    it shaped the plan's four-games / alea / consensus / commitment-store / armature *shape* via `critique.md`,
    but its rich detail (Dowlen small-pool weighted lottery; `liberum veto` as self-undermining equilibrium;
    Padgett robust action; Putnam two-level bargaining) is not yet in the code. Plan amended: Stage 3 (armature)
    and Stage 4 (four games) agonists must now READ the source-research trilogy directly, not just the critique
    distillation, so this commissioned scholarship actually reaches the implementation.
  - **Stage 3 / Gate C DONE + RATIFIED (2026-07-02, ED-1062)** — rhetoric grounding + adjudicator
    armature (CR4 stasis, CR5 self-gating, 4-axis Style×Conviction dot-product) landed; packets:
    `designs/audit/2026-07-01-contest-gate-c-packet/` + `2026-07-02-contest-gate-c-packet/`.
    *(This line corrects the previous "NEXT: Stage 3" — the handoff trailed the ratified state by one
    stage; flagged as a currency observation by the 2026-07-05 audit below.)*
- **Fable 5 subsystem audit RATIFIED (2026-07-05; PR #80 merge + Jordan post-merge "Ratify all").**
  `designs/audit/2026-07-05-fable5-social-contest-audit/` — six-dimension audit (code architecture,
  qualitative NERS, throughlines, playability, echo/emergence/prose interactions, viability). All 10
  NEW findings critic-UPHELD. **Sequencing adopted: P0 spec-reconciliation → P1 consequence spine
  (∥ P3-lite human-plays-Agôn slice) → Stage 4 → calibration** — i.e. the consequence spine (kernel
  reachability + echo transport) now precedes the Stage-4 four-games build. All 11 ed_options
  candidates filed: decision docket ED-SC-0002..0005 (forks, `needs_jordan`), work items
  ED-SC-0006..0010, cross-cutting ED-IN-0012..0013.
  - **STILL OPEN: the P0 decision docket (ED-SC-0002..0005) — awaits Jordan's four picks** (Domain-Echo
    keying §5.4-band vs §6-genre vs composed; Piety/Persuasion tracker naming + canonical home;
    kernel Argue-pool formula; Recall/Corroborate/Prep/Findings global cap). ED-SC-0002 and
    ED-SC-0004 are P1 blockers (echo wiring; calibration/re-verdict/export).
  - **ED-SC-0006 EXECUTED (2026-07-08)** — `sim/cross_scale/scene_dispatch.py`'s contest branch now
    routes to the promoted kernel (`build_contest`/`resolve_contest`), retiring the deprecated
    `contest_legacy_stub.run_contest` call. New `_emergency_council_parties` derives both sides of
    the one live trigger (Stability Crisis → Emergency Council, `scale_transitions_v30.md:137`) from
    the SAME faction's own aggregate stats (`side_a=round(L)`, `side_b=round(7-Sta)`, both floored at
    1) — a `[SEED]` design default, not a P0 fork, open to Jordan revision; proceeding defaults to
    `guild_arbitration` (Panel = seated bench, closest structural match), also `[SEED]`. The kernel's
    global-`random`-module constraint is bridged by a per-call reseed derived from `world.rng`
    (restored after), keeping campaign determinism. `sim/tests/test_mc_v18_regression.py` gained
    `test_mc_v18_resolves_at_least_one_contest`; its seed-0 golden moved and was repinned (the F7
    seed-42 golden and echo_transport tests were verified unchanged — Stability Crisis doesn't happen
    to fire in that particular 8-seed sample). ED-SC-0007's echo-mapping is deliberately NOT wired by
    this change (still blocked at the spec level by ED-SC-0002); `echo_transport` (ED-IN-0028) stays
    inert. Full ledger note: `canon/editorial_ledger.jsonl` ED-SC-0006.
  - **NEXT: ED-SC-0007** (Bout outcome → the already-built `domain_echo.py`) is mechanically
    unblocked (contests now resolve) but still spec-blocked on the ED-SC-0002 echo-keying fork — needs
    Jordan's P0 pick before it can land. In parallel: **P3-lite** — a minimal interactive Agôn harness
    over the existing kernel to run the dramatic-legibility test with a human and measure the
    ~13-consult load (audit D4/N-7) before Stage 4 multiplies interaction shapes.
  - **Stage 4 entry criteria now include (ED-SC-0009):** Face/Rattled strain channel (KU-3) + §9.3–9.4b
    thread junctures (P-14); plus ED-SC-0005's stack cap must land in prose before wiring; Chronicle
    focalization (ED-SC-0010) before any player-facing narrative output.

## Decisions

- 2026-07-08 — **ED-SC-0006 executed** (party-derivation bridge + kernel routing; see Pending above
  and the ledger entry for full scope). Design defaults shipped as `[SEED]` (party-faculty mapping;
  `guild_arbitration` as the Emergency Council proceeding) rather than deferred to Jordan, per the
  same convention that ships other kernel constants (e.g. `STYLE_AXIS`) `[SEED]`-flagged-but-wired —
  the audit's own framing rated this "Medium — real design work" but explicitly `needs_jordan: false`.
  Revisable without unwinding the mechanical routing if Jordan wants a different mapping.
- 2026-07-08 — **Consequence spine LIVE (ED-SC-0006/0007/0002 resolved; Jordan rulings via AskUserQuestion).**
  Two blocking forks ruled: (1) party derivation = **wire the canonical Parliamentary vote** (faction-scale
  §10, consumes aggregate state directly — sidesteps the still-open PERSONAL-scale party-derivation gap);
  (2) **ED-SC-0002 = composed** keying (band gates magnitude, genre selects stat/channel). New
  `sim/cross_scale/parliamentary_bridge.py` resolves a §10 vote each season (proposer=lowest-Sta,
  establishment=highest-Mandate, others abstain/resist), applies the §10 loser Mandate penalty, and
  composes the winner Domain Echo (band→domain_echo degree; genre→stat: Memory→L, Projection→I) through
  the substrate (deferred apply at the accounting boundary; echo_transport apply fixed to STAT POINTS ×
  MULTS). Behind `ECHO_TRANSPORT` (default OFF = byte-exact). Flag ON: scenes_resolved 0→49, keys_emitted
  0→30; win-share Varfell 87.5→62.5 / Crown 12.5→37.5 (erodes the elimination-lockout degeneracy — all 4
  factions win at seed 100). `scale_transitions §5.4` + `social_contest §6` reconciled to composed.
  Goldens: `sim/tests/test_parliamentary_bridge.py`. **RATIFIED ON 2026-07-08 (Jordan: "Yes echo transport
  on"):** `ECHO_TRANSPORT` defaults ON — the spine is the baseline; seed-0 + F7 goldens regenerated; the
  pre-spine byte-exact path is retained under `ECHO_TRANSPORT=0`. **Still deferred:** ED-SC-0011 (PERSONAL-
  scale contest dispatch onto the promoted kernel — distinct from the faction-scale vote wired here) still
  needs the personal party bridge — the "play it out as a scene" mode of the auto-resolved vote (Jordan's
  Total-War auto/manual framing, 2026-07-08).
- 2026-07-05 — **"Ratify all" (PR #80):** the Fable 5 social-contest audit's findings + D6 sequencing
  + all 11 ed_options candidates adopted; audit doc statuses flipped, IDs allocated
  (ED-SC-0002..0010, ED-IN-0012..0013), CURRENT.md SC row refreshed, this handoff updated — per the
  ED-1094 merge-ratifies convention and the ED-IN-0011 "Ratify all" precedent (forks with no stated
  default stay `needs_jordan`).
- 2026-06-26 — **J-31** social-contest docket recovered (ED-938/939/1042 + rule resolutions);
  22-doc cross-corpus reference + terminology repair landed (#13). `contest.py` sim edit deferred
  behind pre-existing sim-fabrication debt (19 uncited constants on `main`).

## Next actions

- **P0 decision docket awaiting Jordan: ED-SC-0002..0005** (echo keying / tracker naming / pool
  formula / bonus-stack cap — see the ratified-audit item above; ED-SC-0002 blocks ED-SC-0007,
  ED-SC-0004 blocks calibration + ED-IN-0013 re-verdict).
- **ED-SC-0006 DONE (2026-07-08)** — kernel routing + party-derivation bridge executed; see
  Decisions above. **ED-SC-0007 + P3-lite Agôn harness are the remaining P1 work** — the harness is
  unblocked now; ED-SC-0007 still waits on ED-SC-0002's echo-keying pick.
- **Design-tier docket awaiting Jordan:** J-31 extended (social-contest deliberative-game findings,
  row #39 → LA-19, `designs/workplans/valoria_master_workplan_v5.md`) — note the ratified audit
  resequences Stage 4 *after* the consequence spine.
- **`contest.py` fabrication-debt triage** — 19 uncited constants block the J-31 terminology
  propagation into code (also tracked at `decision_queue.md` item 16).
- **contest_rebuild Stage 1+ gates** — each stage ratified individually (Gate 0 ratified
  2026-06-30; ED 1055-1079 / PP 800-809 reserved; Gates A–C ratified through 2026-07-02; also
  tracked at `decision_queue.md` item 15).
