# R4 Equal-Value Sweep — Result (armature reset, Build-4)

**Date:** 2026-05-29 · **Module:** `tests/sim/v32-combat-balance/r4_full_channel_parity.py` · **Status:** Class-C proposal result — canonical Health/damage/degree NOT altered. Flagged for Jordan.

**Directive executed:** "wire as required" + "all Attributes should have equal value." Wired the full σ-leverage stack (Agi initiative + tempo + facing[M7] + reaction[M5]; Reading[Cog/Att]) into a decisive one-phrase exchange; swept equal-budget builds across weapon/armour variety; tuned every Class-C seed toward equal value.

`[SELF-AUTHORED — bias risk: R1–R4 are this session's build. The sweep reports the model as NOT-equal and names a structural cause in my own design rather than tuning a stat artificially to 50%.]`

## Final field win-rate (equal 15-pt combat-active budget, 4 weapons × 4 armours, N=4000/matchup)

| Build | field rate | verdict |
|---|---|---|
| **End** | 66% | dominant |
| **Agi** | 65% | dominant |
| **Reading** (Cog/Att) | 46% | **in-band** ✓ |
| **Str** | 23% | **dead** |

Spread narrowed across tuning passes 63 → 55 → 43 pp. Reading reached parity. **Agi/Str/End did not.**

## What tuning achieved (Class-C, my authority)

- **The original C-04 stays closed** — Agi's *pool* dominance is gone (R1 demoted pool); Agi now earns its rate through σ-leverage, not raw dice.
- **End's R3 dominance (63%) was tamed by the decisive frame** — making the phrase resolve on a *felling* strike rather than 6-round attrition cut End's depth advantage; End is now co-equal with Agi, not running away. This is Jordan's own "6-10s, not attrition" design doubling as the balance lever — not a canon change.
- **Reading (Cog/Att) is balanced at 46%** — the mental channel (information game: anticipate + deny reactions, M7) earns its keep in combat. C-06 satisfied.

## The structural finding (NOT a tuning failure — a design boundary)

**Strength is dead at 23%, and it loses to *everyone* (Agi 18%, End 16%, Reading 34%) — not just End.** Measured cause, quantified:

> **Mean σ-leverage each build brings to a strike:** Agi **+0.50**, Reading **+0.625**, **Str +0.00**, End +0.00.

Strength's only channel is **damage magnitude**. In a *decisive duel where landing the strike decides the fight*, magnitude is the weakest currency — every build already does enough damage to wound (a Str strike does 17 vs an 11-point wound interval, crossing a gate 100% of the time). Str has no **landing** leverage (no tempo, no facing, no reading), so it cannot equal-value against attributes that buy σ-leverage. **More damage doesn't help when your problem is connecting, not hurting.**

End survives the same way Str fails: it brings +0.00 leverage too, but its canonical Health depth (44 vs 24) lets it *outlast* to the wound-count tiebreak. So the decisive frame helps End (depth → survival) and hurts Str (magnitude → irrelevant).

## Two decisions this surfaces — both yours (project-owner contract)

These are **new-mechanic / canonical** decisions, outside the Class-C seeds I'm authorized to tune. I will not invent them:

1. **Strength needs a *landing/control* channel, not just damage.** To equal-value Str, it must buy σ-leverage or a decisive effect of its own. Candidates (your call — each is a new mechanic, N/Ω/Μ vetting territory):
   - **Bind/control:** Str wins the bind (the In-bind state), gaining a δσ or forcing the opponent's depth — leverage, not damage.
   - **Stagger/stun:** a heavy Str hit *opens the σ-window* (next strike advantaged) — converts magnitude into landing.
   - **Armour-defeat-opens-window:** vs armour, Str's multiplier *creates* a leverage δσ (the half-sword/poleaxe logic) rather than only adding damage.
   - **Decisive-by-damage:** an Overwhelming Str strike fells outright (magnitude *is* the decisive currency for one stat) — re-elevates damage as Str's win condition.

2. **End's co-dominance (66%) vs the decisive frame.** End is bounded now but still top. If you want it *exactly* in-band, the lever is either (a) the decisive threshold (a clean strike fells regardless of Health depth — reduces End's edge, canonical-adjacent), or (b) a canonical Health-scaling decision (PP-716/717 territory). (a) is Class-C-ish; (b) is yours.

## Honesty flags

- `[CONFIDENCE: high — builds are deterministic equal-15-pt (verified); CIs tight at N=4000; the σ-leverage measurement is direct.]`
- `[ASSUMPTION]` "all attributes equal value" scoped to **combat-active** attributes (Agi/Str/End/Cog/Att). Cha/Bon/Spi/Foc/Rec have their equal value in social/thread/relational/economy systems — **game-wide parity is a cross-system property this combat sweep does not and cannot prove.** Validating it needs a multi-system value audit (separate work).
- `[GAP]` stance-counter (M5) and the depth/commitment game are wired only lightly (symmetric); a fuller tactical-choice layer could shift the leverage balance.
- The Class-C config is **locked at its best-balanced point** (spread 43pp, Reading in-band). Further seed-tuning only rotates *which* stat is dead — the Str gap is structural, not a knob.

## Next

Awaiting your call on decision 1 (Str's channel) — it's the gating decision; once Str has a landing/control role, re-run R4, then the omega Class-A vetting block can honestly assess Ω-d. Until then, "all attributes equal value" is **achieved for Reading, closed for the old C-04, and blocked on Strength by a missing leverage channel only you can authorize.**
