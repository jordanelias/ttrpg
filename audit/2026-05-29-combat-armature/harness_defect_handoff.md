# Combat Armature — Session Handoff (parity-harness defect)

**Date:** 2026-05-29 · **Status:** mechanics solid + committed; **parity sweep harness is defective and must be rebuilt before any equal-value verdict is trusted.**

`[SELF-AUTHORED — bias risk: I authored R1–R7 and the harness whose defects I'm reporting. I let two harness bugs drive false "Strength is dead" conclusions across R4/R6/R7 before catching them. This handoff corrects the record.]`

## What is SOLID (validated, committed to main)

- **R1** (`r1_sigma_resolution.py`, `1f63990`) — demoted Agi-independent pool; closes original C-04. Self-test 6/6.
- **R2** (`r2_consequence_wounds.py`, `de43357`) — canonical damage + wound-gate tracker. Self-test 7/7.
- **R3** (`r3_parity_sweep.py`, `de43357`) — first sweep; End-dominance finding (later shown partly harness-confounded).
- **R4** (`r4_full_channel_parity.py`, `3b475c5`) — full Agi stack + Reading wired. Self-test logic sound.
- **R5** (`r5_strength_stamina.py`, `3596084`) — **Strength leverage channels + Stamina = f(End, Spirit). Self-test 6/6.** Jordan's two decisions, implemented and unit-validated:
  - Str: bind-win, stagger, armour-defeat window, stamina-efficiency, wield (Str leverage +0.00 → +0.88 in-bind, confirmed).
  - Stamina = 3·End + 2·Spirit (Spirit gains combat role; End loses action-economy monopoly).

These modules' **unit self-tests are trustworthy** (deterministic, direct assertions). The mechanics work.

## What is CORRUPTED (do not trust)

**Every cross-attribute FIELD-RATE / parity verdict produced this session** — R3's End-dominance, R4's "Str dead 23%", R6's "Str 6.6%", R7's "Str 7%". Two compounding harness defects:

1. **stdout-buffer interleaving.** Piping long sweep output through `head`/`sed`/`tail` repeatedly surfaced *stale fragments from prior runs* mixed into captured output — e.g. R7 printed a "Str" build line reading `Str2 End2` that doesn't even sum to the fixed budget. I mistook these ghosts for real build/field values multiple times. **Lesson: never read sweep results from piped stdout; write to JSON, read the file.**

2. **Intermittent build-budget failure in the full sweep process.** Inside the complete `r6`/`r7` sweep process, `equal_budget_build('strength')` intermittently yielded a **budget-13 build (Str under-pointed)** instead of 18 — while the identical call is **stable at 18 in 250+ isolated calls** and in a hand-traced rebuild. I could not stabilise/repro it in isolation; it manifests only inside the multi-import sweep process. Root cause unconfirmed (suspect import-order / module-state interaction, not the function logic itself). A budget-13 Str build is auto-crippled (can't wield heavy weapons, fewer effective points) → guarantees the false "Str dead" field rate.

**Consequence:** no equal-value VERDICT from this session is valid. The "Strength is structurally dead / needs a landing channel" finding that drove Jordan's decision-1 was **itself an artifact** — though decision-1 (give Str leverage) is still good design and is now implemented.

## What IS trustworthy about Strength (clean, deterministic, artifact-immune)

Direct head-to-head matchups, verified equal-budget (Str=5, sum 18 asserted), results computed in-process and printed as single scalars (no pipe, no buffer):

- **Str-5 (war hammer, heavy armour) vs End-5: Str wins 86%** (2585/3000).
- **Str-5 (war hammer) vs Agi-5 (war hammer): Str wins 90%.**
- Str-5 best weapon vs field: `long_heavy_blunt` at **93%**; dagger 46%, thrust 43%, longsword 80%.

So with R5's channels + heavy-weapon access (canonical wield), **Strength is strong, not dead.** If anything the open question is now whether Str is *over*-tuned once the harness is fixed — the opposite of the artifact's claim.

## NEXT (required before any equal-value verdict)

1. **Rebuild the parity harness clean** (new module, e.g. `r8_parity_harness.py`):
   - All results to a **JSON file**, read back; never trust piped stdout.
   - **Assert `budget == 18` on every build at construction AND before every matchup**; hard-fail otherwise.
   - Deep-copy builds into every `resolve_phrase` call; never share/mutate the canonical build dicts.
   - Isolate the build-budget heisenbug (bisect the import set; suspect a module-level name collision across r1–r7) or sidestep it by constructing builds inline with an explicit point-allocation that is asserted.
2. **Re-run the 6-attribute parity** (Agi/Str/End/Reading/Spirit), each playing its own best loadout, asymmetric. THEN read the real verdict.
3. Likely finding to expect (hypothesis, untested): with Str correctly strong, the imbalance may be **Str/End/Agi all strong vs Reading/Spirit weaker**, or **Str over-strong** — tune the Class-C channel magnitudes against the *correct* baseline.

## Canon items still pending Jordan (unchanged)

1. Stamina formula `End×5` → `3·End + 2·Spirit` (derived_stats §4.2) — proposal, needs ratification.
2. Spirit definition expansion (tenacity/fortitude/reserves) — canon note.
3. Bind-as-Str-contest + Stagger — new mechanics, N/Ω/Μ vetting.

`[CONFIDENCE: high — R1–R5 unit mechanics + the direct Str matchups. The defect diagnosis (two harness bugs) is confirmed for #1, root-cause-unconfirmed for #2 (reproduced in-process, not isolated).]`
