# Valoria Combat — Ratification + New Primitives (session close)
**2026-06-02**

## COMMITTED TO REPO (clean — all gates passed; commit path verified working this session)
- **`6e9b6aa`** `[simulation]` combat_engine v1 — 6 modules + README under `designs/scene/combat_engine_v1/`.
- **`69acec8`** `[simulation]` ratification + deprecation proposal under `designs/audit/2026-06-02-combat-engine/`.
- **`1e2bf86`** `[cleanup]` removed the commit-path probe.
- (probe `696b6cd` earlier proved `h.safe_commit` lands on main.)

**Commit path confirmed:** `h.safe_commit(additions=[(path,content)], deletions=[...], message)` — gated
(commit_message + forbidden_token + pre_commit), lands direct to main. Earlier session-long "nothing committed" is
resolved: the engine + proposal are now in the repo.

## NEW PRIMITIVES BUILT THIS TURN (all grounded in martial research, validated)
1. **Lever-arm primitive** — weapons carry head_len/grip_len; `leverage()` = redirect/bind capacity from grip-behind
   vs head-ahead. Poleaxe/staff 0.64, longsword 0.34, spear −0.07, rapier −0.31. Feeds the bind + displacement.
2. **Displace-and-step-inside** — vs a committed thrust, a higher-leverage weapon sets the point aside and closes
   (longsword vs spear), with the thruster's pull-back able to graze (Jordan's caveat). Fires on the approach
   (suppresses stop-hits, speeds the close) and on a won read.
3. **Half-sword auto-switching form** — `longsword_halfsword` in the index (short reach, gap 1.0, high leverage,
   point/Mordhau); `halfsword_switch()` adopts it when closed vs armour, reverts at reach. The "another weapon that
   auto-switches by technique/distance" you specified.
4. **Feinting** — a non-existent action that degrades a FOOLED defender's real-attack defence/read; capped at **3 in
   a row**, short phase (0.3 beat), costs stamina, and READABLE — a high-reading defender sees through it and
   punishes (feint-spam into a good reader backfires). Mirror stays 50 (symmetric); technique-feinter +53% vs plain.
   Verified not overpowered.

(Built on the prior conditional-tempo + movement-legibility + reach/armour-rotation corrections.)

## VALIDATION (vs the external four-state matrix)
A0 ~23pp/74% · A1 ~28pp/61% · A2 ~27pp/75% · A3 ~29pp/76% (from a 38.8–49.8pp / 33–37% pre-fix baseline). Structural
inversions fixed; remaining is magnitude tuning. Invariants: mirror 51, mastery (H6v3 73, Read 93), traditions 48,
no-one-shot 18<24, 95% cap intact.

## HELD FOR JORDAN'S RATIFICATION (structural canon — not applied unilaterally per the project contract)
These two are STAGED in the proposal, one `safe_commit` each on your approval:
1. `combat_v30.md` → `canonical_status: PARTIALLY SUPERSEDED` (resolution layer replaced; lore retained).
2. Add `designs/scene/combat_engine_v1/` to `references/canonical_sources.yaml`; deprecate the drifted
   `params/combat.md` to `deprecated/params/`.
I did not change combat_v30's status or canonical_sources myself — declaring supersession is your design authority.
Everything needed for you to ratify in one step is in the committed proposal.

## REMAINING (magnitude tuning, not structure)
- longsword-vs-spear 19 (target ~40) and longsword-vs-plate magnitude; A1 mail dials; feint-vs-elite-reader floor
  (~5%, slightly over-punished). Autonomous choke/lunge/feint decision policy (states wired, not yet engine-chosen).

## FILES
Engine in repo at `designs/scene/combat_engine_v1/`. Local working copy `/home/claude/combat_engine/`. Session docs
in `/mnt/user-data/outputs/`.
