All decisive numbers independently reproduce: dÏƒ dP=+0.19101 uniform (spread 0.000000); fracOb front-loaded (2.86â€“2.94x swing); net_boost TN divergence 1.767/1.754/1.712; dice-bug EV/die error +0.100 at TN6 / âˆ’0.100 at TN8 (and âˆ’0.200 at TN5, +0.100 at TN8, 0 at TN7). Note the hardcoded error sign convention: hardcoded 0.40 vs correct 0.50 at TN6 means the roller under-credits (rolls harder) at TN6 and over-credits at TN8 â€” matching the facets' "+0.10 EV/die divergence." Now the memo.

---

# DECISION MEMO â€” D0-3 Substrate Probe: Î´Ïƒ Î¼-shift vs Fractional-Ob

**To:** Jordan Â· **Date:** 2026-06-30 Â· **Scope:** contest leverage-to-outcome substrate + dice_engine TN-bug (finding 2a) Â· **Basis:** read-only, three adversarially-verified facets, independently re-confirmed inline (scratchpad probe, no `sim.*` import).

---

## 1. RECOMMENDATION

**`HYBRID(present-as-Ob, compute-as-dsigma)`**

**Decisive reason:** The one property fractional-Ob was proposed to buy â€” legibility ("lower the bar 3.0 â†’ 2.4") â€” is *already fully attainable on top of Î´Ïƒ with zero fidelity loss*. Feeding the Î´Ïƒ display shift `soft_cap(net_Ïƒ)Â·Ïƒ_N(pool)` back through a pure fractional-Ob resolver reproduces the Î¼-shift `p_success` **bit-identically** (err = 0.0e+00, algebraic identity â€” the `eff_ob` path is already tagged DISPLAY-ONLY at `sigma_leverage.py:139-147`, citing ED-884/ED-934). So you can show the player a lowered bar while resolving on Î´Ïƒ. Adopting fractional-Ob as the *substrate* buys nothing you can't already display, and costs the entire F1/CR6 uniformity guarantee (fracOb front-loads advantage 2.86â€“2.94Ã— onto small pools; the +0.191-uniform Î´Ïƒ result has spread 0.000000). Legibility is separable from representation; keep the good substrate, borrow the legible face.

---

## 2. TRADEOFF TABLE

| Axis | Î´Ïƒ Î¼-shift (current substrate) | Fractional-Ob (as substrate) | HYBRID (present-Ob / compute-Î´Ïƒ) |
|---|---|---|---|
| **Cross-pool uniformity** | âœ… Exact: dP = +0.191 at every pool 3Dâ€“26D, spread 0.000000 (z-shift invariance; âˆšN & Ïƒ cancel). *Caveat: uniform in z-space / at constant baseline-P; under a **fixed** raw Ob it too is non-uniform.* | âŒ Non-uniform by construction: fixed dOb=0.6 â†’ dP spread ~0.11, ratio 3D/26D â‰ˆ 2.9Ã—; calibrated head-to-head gap 0.131 (ns=0.50) to 0.214 (ns=0.75) of win-prob. This **is** the F1 defect. | âœ… Inherits Î´Ïƒ uniformity exactly (resolution is Î´Ïƒ). |
| **Legibility** | âš ï¸ Native form is a Î¼-boost, not a bar; player never sees Ïƒ. Needs an authored readout. | âœ… "Lower the bar 3.0â†’2.4" is directly legibleâ€¦ | âœ… â€¦and reproducible on Î´Ïƒ **bit-identically** (0.0e+00 error). Best of both â€” legible face, uniform math. |
| **TN-cleanliness** | âš ï¸ `net_boost` is TN-dependent (Ïƒ_per_die 0.806/0.800/0.781 â†’ 1.767/1.754/1.712 at ns=0.75,10D); TN6/7/8 agree **only at TN7**. Contest is TN7-only â‡’ divergence is **latent, not live** for contest. | âœ… TN-agnostic (no TN term in a threshold subtraction) â€” dissolves the TN6/7/8 divergence. **But contest is TN7-only, so it gains none of this benefit while paying the full uniformity cost.** | âš ï¸ Same as Î´Ïƒ (TN-latent for contest). TN-cleanliness is a *combat* concern, addressed separately in Â§4, not a reason to switch the contest substrate. |
| **Combat blast-radius** | None (status quo; 151 contest tests green, combat on Î´Ïƒ). | âš ï¸ High: fracOb's only real payoff (TN-agnosticism) lands on the multi-TN **combat** re-point, not contest â€” so a substrate swap would be justified *there* if anywhere, reopening CR6 corpus-wide. | Low: contest untouched; combat can adopt the present-as-Ob display independently without a substrate change. |

---

## 3. CR6-REOPENING VERDICT

**Do NOT reopen CR6 for the contest substrate. The HYBRID does not reopen it.**

CR6 (RATIFIED_2026-06-01.md:16) chose Î´Ïƒ *specifically* as the F1 fix â€” "validated +0.191 uniform across pools 5D-26D" â€” because flat/Ob-style bonuses don't scale uniformly (the flat +2 Ob anchor: 42.6pp @3D vs 21.2pp @20D, a 2Ã— swing). Fractional-Ob-as-substrate is **the exact F1 defect reborn** (2.9Ã— pool swing, verified). Its compensating virtue, TN-agnosticism, is *orthogonal* to pool-uniformity and, for a TN7-only contest, delivers nothing. Adopting it would trade a ratified, exactly-uniform substrate for a legible-*looking* but pool-mispredictive one â€” a **net opacity loss** for the player, contrary to the goal that motivated the proposal.

The HYBRID keeps the Î´Ïƒ resolution path (CR6 intact, D0-3's "contest stays Î´Ïƒ TN7" honored, 151 tests preserved) and satisfies the legibility motive through the *already-canonical, already-DISPLAY-ONLY* `eff_ob`/`effective_ob` surface. This is precisely the "keep the kernel's Ob/resistance path clean enough that a fractional-Ob variant is swappable" hedge D0-3 asked for â€” but realized as a **display** swap, not a substrate swap. The genuine substrate question (fracOb for *combat*, where multi-TN is live) remains legitimately open and belongs to the combat re-point, not this decision.

---

## 4. DICE_ENGINE TN-BUG DISPOSITION (finding 2a)

**Fix in `dice_engine` independently of this decision â€” do NOT fold it into the substrate move.**

- **The bug is orthogonal on both axes.** It lives in the *pool/die-face* rule (`dice_engine.py:43-51` `_die_result` hardcodes 1â†’âˆ’1, 2-6â†’0, **7-9â†’+1**, 10â†’+2 â€” the TN7 threshold â€” and `roll_pool:65-72` accepts `tn` but never forwards it). Fractional-Ob is a *threshold-side* transform; it cannot repair a mis-generated net. So fracOb neither fixes nor is required by the bug.
- **Moot for contest, LIVE for combat.** At TN7 hardcoded == correct (0 error), and contest is TN7-only (verified: ARGUE/KNOT/TRIBUNAL/BG_VOTE all pin TN7) â€” so **contest is unaffected either way**. But it is a **live combat bug** in the merged `sim/personal/combat.py`: `WEAPON_TN_BASE=7` with reach/weight/type mods yields TN5/6/8 weapons (`combat.py:56-60,135-144`) that flow into `roll_pool` (`:212/214`) and are silently rolled at the TN7 rate. Verified EV/die error: **TN5 âˆ’0.20, TN6 âˆ’0.10, TN7 0.00, TN8 +0.10** (roller under-credits low-TN, over-credits high-TN; a short+light weapon rolls ~0.20 EV/die *harder* than canon).
- **`combat_engine_v1` (unmerged head) is dormant** â€” `core.py:9,13` pins `TN=TN_STANDARD(7)` and routes through the *continuous* path, which correctly reads the per-TN table. Doubly safe.
- **Failure-mode nuance (down-weighted, verifier-refined):** the earlier "loud KeyError on TN5" is only partly right â€” `sigma_leverage.net_boost`/`p_success` do direct-subscript `PER_DIE[tn]` (would `KeyError` on TN5), but `dice_engine.continuous_engine_sample` and `roll_net_continuous` use `.get(tn, PER_DIE[7])` and **silently fall back to TN7** â€” a quieter, arguably worse mis-default. Cite the silent-fallback framing, not the KeyError.
- **Disposition:** the fix is to make `_die_result`/`roll_pool` honor `tn` (face â‰¥ tn â†’ +1, keeping 1â†’âˆ’1, 10â†’+2 â€” reproduces the canonical per-die EV 0.50/0.40/0.30 for TN6/7/8, verified against params/core.md:111-115). This is a canon-fidelity repair to a root primitive, gated by combat parity, and must not wait on the contest substrate probe. **Track as its own ED** (own PP for the code fix), sequenced before the combat multi-TN re-point.

---

## 5. PROPOSED EDITORIAL LEDGER ENTRIES

From the reserved `contest_rebuild` block (ED 1055-1079, PP 800-809; `references/id_reservations.yaml`). Two entries: the decision, and the orthogonal follow-up.

**ED-1055 â€” D0-3 substrate probe resolved: HYBRID (present-as-Ob, compute-as-Î´Ïƒ); CR6 upheld, not reopened.**
- *Decision:* Contest leverage-to-outcome substrate **remains Î´Ïƒ tanh-soft-capped Î¼-shift at TN7** (CR6 / `net_boost` path, `sigma_leverage.py`). Fractional-Ob is **rejected as a resolution substrate** (re-imports the F1 non-uniformity CR6 ratified to kill: verified 2.86â€“2.94Ã— pool swing vs Î´Ïƒ spread 0.000000; head-to-head win-prob gap up to 0.131â€“0.214). Its TN-agnosticism is real but orthogonal to pool-uniformity and delivers nothing to a TN7-only contest.
- *Legibility ruling:* the fractional-Ob *representation* is adopted **display-only** â€” the existing `eff_ob`/`effective_ob` (already tagged DISPLAY-ONLY, ED-884/ED-934) is the sanctioned home; it reproduces the Î´Ïƒ Î¼-shift bit-identically (err 0.0e+00), so a "bar 3.0â†’2.4" readout is exposable with zero fidelity loss.
- *Follow-up (authoring debt):* the pre-roll odds / effective-Ob / Minor-Moderate-Strong-Major level readout is **absent** from the articulation layer (grep of `articulation_layer_v30.md`: zero odds/effective-ob/win-prob hits) and **must be authored** to realize the legibility win. Recommend the named-level + Î”-probability readout over raw pool-varying eff_ob shift.
- *Combat carve-out:* the fractional-Ob-as-substrate question stays legitimately open for the **multi-TN combat re-point** (where TN-agnosticism is a live benefit); not decided here. Cite: DECISIONS.md D0-3, RATIFIED_2026-06-01.md CR6/F1.
- *Provenance:* three adversarially-verified facets; all decisive numbers re-confirmed inline (scratchpad probe). No repo files modified.

**ED-1056 â€” dice_engine `roll_pool` TN-fidelity bug (finding 2a): honor `tn` in the discrete die-face rule.**
- *Bug:* `dice_engine._die_result` hardcodes the TN7 face rule (7-9â†’+1) and `roll_pool` discards its `tn` arg; canonical per-die EV (params/core.md:111-115) is 0.50/0.40/0.30 for TN6/7/8. Discrete error: **Â±0.10 EV/die at TN6/TN8** (âˆ’0.20 at TN5). **LIVE in merged `sim/personal/combat.py`** (weapon TN5/6/8 rolled at TN7 rate); **moot for contest** (TN7-only); **dormant in `combat_engine_v1`** (TN pinned to 7, continuous path). Silent-fallback mis-default in `continuous_engine_sample`/`roll_net_continuous` (`.get(tn, PER_DIE[7])`).
- *Disposition:* fix independently of ED-1055 (orthogonal â€” pool-side vs threshold-side). Make the discrete rule `face â‰¥ tn â†’ +1` (keep 1â†’âˆ’1, 10â†’+2); gate on combat parity + the seeded sim smoke test. **Sequence before the combat multi-TN re-point.** Assign a PP from 800-809 for the code fix.
- *Provenance:* confirmed at source (`dice_engine.py:43-72`, `combat.py:56-60/135-144/212-214`, `combat_engine_v1/core.py:9,13`), EV divergence reproduced inline.

---

**Files read (all absolute):**
`C:\Github\ttrpg\.claude\worktrees\happy-shaw-da0f1d\designs\audit\2026-06-30-contest-stage0-reconciliation\DECISIONS.md` Â· `...\designs\audit\2026-06-01-contest-redesign\RATIFIED_2026-06-01.md` Â· `...\sim\autoload\sigma_leverage.py` Â· `...\sim\autoload\dice_engine.py` Â· `...\params\core.md`
**Confirmation probe (scratchpad only, self-contained):** `C:\Users\Jordan\AppData\Local\Temp\claude\C--Github-ttrpg--claude-worktrees-happy-shaw-da0f1d\942f1f2d-d8e7-496e-ad44-9309b80e4e36\scratchpad\synth_probe.py`

No repo files were created, edited, or moved; `sim.personal.contest` was not imported.
