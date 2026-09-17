`mechanics_selftest` green (each Stage-3 WIRED mechanic â€” CR4 chosen-genre +1D, armature Î´Ïƒ, CR5 standing-bounded backfire â€” actually fires in the resolver).

## Summary

All three judge-upheld findings (1, 4, 5) are fixed in the real files. Both test commands green; HEAD unchanged at `f374b816`; nothing staged/committed/pushed.

### VERBATIM TEST OUTPUT
- `python -m sim.personal.contest._kernel_tests` â†’ **`RESULT: 377 passed, 0 failed`** (was 370; +7 from the new finding-1/4/5 guards)
- `python -m pytest sim tests/valoria -q` â†’ **`1041 passed in 91.72s (0:01:31)`**

### THE THREE FINDINGS FIXED

**Finding 1 (major) â€” CR4 +1D was tautological, dropping the orator's Style choice.** The +1D was keyed on `genre_of_ground(move.ground)`, but `Stasis.relevant` forces `move.ground == self.live`, so the match was structurally always-true (FACT/CONSEQUENCE/FEASIBILITY) or dead (others) â€” a terrain-determined constant the Style card could not touch. params/contest.md:61 says "Orator's **chosen genre** matches primary genre". Fix: `primary_genre_pool_bonus` now keys on the orator's **chosen Style genre** (new `genre_of_style`: Precedent/Suppressionâ†’Memory, Vision/Insinuationâ†’Projection), matched against the live-stasis primary genre. So a Memory-chosen Precedent earns +1D on a FACT stasis but a Projection-chosen Vision earns 0, and it flips on CONSEQUENCE â€” the choice is load-bearing. CR4 is now armature-gated (no chosen Style â‡’ no bonus), which **restores byte-identical golden-trace parity** on the `armature=None` path.

**Finding 4 (major) â€” CR5 backfire cited "bounded by your own standing" but was a flat âˆ’2.** `cr5_self_backfire(style, landed)` had no standing parameter. The ratified CR5 carry-across (`reconciliation_map_raw.md Â§1.3`) requires it "gated by SelfGating.licit â€” your own Face caps your obstruction". Fix: `cr5_self_backfire(style, landed, my_standing)` returns `min(CR5_BACKFIRE_MAGNITUDE, own Face)`; the resolver passes the mover's Face. A Face-1 mover strips only 1.0 (verified in the live resolver), a higher-standing orator the full âˆ’2 â€” the "bounded by your own standing" invariant realized, not nominal. (A deeper standing-*scaling* variant stays a flagged Jordan fork.)

**Finding 5 (major) â€” off-axis 0.15 was behaviorally inert; armature was categorical, not continuous.** The armature was a fractional pool bonus, but `roll_net` floors the pool via `max(1,int(round(pool)))`, so any alignment < 0.5 rounded away (misaligned == flat, byte-identical; the kernel test's `<=` was load-bearing). Fix: the alignment now enters as a **continuous Î´Ïƒ-leverage Î¼-shift** (`style_axis_dsigma`) on the `net_boost` term (the Ïƒ-space channel, not the rounded pool) â€” the exact CR6 shape for a setup/audience-boost advantage. Off-axis 0.15 â†’ 0.075Ïƒ (real, non-rounded), so `flat < misaligned < aligned` now holds **strictly**. Magnitude re-grounded from the npc_behavior +1D onto `ARMATURE_MAX_DSIGMA = level("moderate") = 0.50Ïƒ` (`modifier_system_spec.md Â§2.3`, the Ïƒ-level `Leverage.ONGROUND` uses â€” reused, cited). CR4's +1D stays an integer pool die (distinct channel, as CR6 separates the flat-dice stack from Î´Ïƒ leverage). The old `ARMATURE_MAX_POOL_BONUS`/`style_axis_pool_bonus`/`pool_bonus` are deleted.

### OPEN DECISIONS FOR JORDAN (flagged, not resolved)
- STYLE_AXIS projection-cell magnitudes (`STYLE_AXIS_PRIMARY=1.0`, `OFFAXIS=0.15`) â€” [SEED]/candidate; the Î´Ïƒ magnitude `ARMATURE_MAX_DSIGMA=0.50Ïƒ` is cited (`level("moderate")`).
- The 4th armature axis: Insinuation (coded) vs canonical Solidarity â€” a fork.
- CR5 standing-dependence: the min(âˆ’2, Face) **cap** is realized; a deeper **scaling** variant (cost grows with standing) remains a candidate. The Face-cost anchor (equal to âˆ’2 vs re-scaled to the credibility stat) stays open.
- CR5's opponent-Face-attack half remains DEFERRED (finding 7 from a prior pass, unchanged).
- Appraise-reveal boundary (PARTIAL); epideictic-compression acceptance; whether to fold the categorical opponent-aimed +1D into the continuous armature primitive.

### FILES TOUCHED (all absolute; all uncommitted; HEAD `f374b816`)
Modified:
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\personal\contest\rhetoric.py` (CR4 chosen-genre keying + `genre_of_style`; CR5 standing-bounded backfire)
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\personal\contest\armature.py` (continuous Î´Ïƒ channel; `style_axis_dsigma`/`ARMATURE_MAX_DSIGMA`; deleted pool-bonus symbols)
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\personal\contest\resolver.py` (`_reception(pool_bonus, dsigma_bonus)`; CR4 chosen-genre call; armature Î´Ïƒ into `net_boost`; CR5 standing-bounded strip)
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\personal\contest\wrapper.py` (`_SYMBOLS` + MECHANICS `adjudicator_armature`/`cr4_stasis_genre`/`cr5_self_gating` source strings)
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\personal\contest\__init__.py` (renamed re-exports + `genre_of_style`)
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\personal\contest\_kernel_tests.py` (finding-1/4/5 guards; ASCII-safe header)
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\sim\tests\test_contest_kernel.py` (`_KERNEL_EXPECTED` 370 â†’ 377)
- `C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\designs\audit\2026-07-01-contest-gate-c-packet\GATE_C_packet.md` (RE-REVISION #3 block; CR4/CR5/armature/checker-board/open-decisions/files/count corrections)

Not changed this pass (shows modified from prior passes but verified consistent under the new channels): `sim/personal/contest/primitives.py` (`strip_points` already present; unchanged).

Untracked (created by the Gate-C effort): `sim/personal/contest/{armature,rhetoric,appraise}.py` and `designs/audit/2026-07-01-contest-gate-c-packet/GATE_C_packet.md`.

Broad canon-prose propagation, the ED-1062 ledger entry, and the `id_reservations.yaml` bump remain deferred to the Synthesist post-approval.
