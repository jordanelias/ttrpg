# Grappling / Close-Combat System — Bottom-Up Design (the Third Plate-Counter)

**Status:** Class-C **proposal**, Jordan-vetoable. Per Jordan "keep working" 2026-05-30. Built **bottom-up** from the **canonical close-combat actions** (Disarm, Tie Up, Escape, Retrieve — `3.6 Actions`) + the σ-leverage engine + ratified Strength channels (ST1) + the engagement-state graph, and **top-down** from the project's own research (Fiore's *abrazare* as "the foundation under all weapon work") + real armoured-combat history (*ringen*, half-swording, the rondel dagger). **No canon retconned** — the canonical actions are *reused and unified*, not overwritten; this fills the canon-acknowledged **unarmed/close-combat gap (ED-129)**.

`[READ: 3.6 Actions atom; 3.3 binary-axes atom; seven-axes doc grip/abrazare lines — this session.]` `[CONFIDENCE: high — every sub-mechanic wired to a named canonical primitive; the dagger-finish is the one new element, grounded in the rondel-dagger record.]`

## §0 — What the canon already fixes (reused, never overwritten)

From `3.6 Actions (14)`:
- **Disarm** — Off vs (STR+Agi) as Ob.
- **Tie Up** — both −2D; blocks Escape (the clinch/control).
- **Escape** (PP-634) — Agi TN 7 Ob 1; contested if pursued; partial = exit + free strike.
- **Retrieve** — post-Disarm pickup.
- **Unarmed is explicitly OUTSIDE the weapon matrix** (separate TN 8) — the acknowledged gap (ED-129) this system fills.

Grappling **unifies these atoms into a close-combat phase** and adds the missing piece: the **grounded-foe dagger-finish** that bypasses armour mitigation — the third historical plate-counter.

## §1 — Where grappling sits: the extreme of the engagement-state graph

The state graph (R9/R10) runs **closing → in_bind → [grapple] → breaking**. Grappling is the **innermost range**, past the bind:
- **Reach inverts hard** (R9/W3 principle): long weapons are useless in the clinch; a dagger/short weapon or empty hands dominate. The reach-inversion already in the engine is taken to its extreme.
- **Entering** the grapple is a state transition (a closing action against a defender who can resist with distance/tempo). Closing *gives up reach and tempo* to reach the clinch — the cost that makes grappling a **choice**, not a free win.

## §2 — The grapple contest (bottom-up, Strength-dominant)

A grapple is resolved as a **Strength-dominant σ-contest**, extending ratified **ST1** (Strength's bind-win channel). This is where Strength — strong in the bind/battlefield, weak in the finesse duel — gets its **close-range expression**:
- **Grapple pool/contest:** Strength + relevant History (wrestling skill) vs the opponent's Strength + History, expressed through the σ-leverage engine (the bind-win δσ per Strength point, ST1, now the dominant term at grapple range).
- **The hands axis matters (wa2):** a **2H weapon occupies both hands** → poor grappling (you must drop/shorten the weapon — historically, half-swording or letting go); a **1H weapon + free off-hand** (or empty hands) grapples well. So closing to grapple favours the lighter-armed — a real trade-off against the 2H bind-leverage advantage.
- **Fatigue tells here (asymmetric, the honest model):** grappling is exhausting; the more-fatigued / heavier-drained fighter (heavy armour, ST drain) is at a grapple disadvantage. This is fatigue's *correct* role (asymmetric close-combat), not the duel-equaliser that was struck.

## §3 — Outcomes (unifying the canonical actions + the new finish)

On winning the grapple contest, by margin (the σ-leverage degree):
- **Throw / takedown** → opponent **prone**: a σ-window against them (the ST1 stagger analog) + they must spend an action to rise. Bypasses armour — **you cannot deflect a takedown with plate** (mitigation does not apply to being thrown).
- **Disarm** (canonical) — Off vs (STR+Agi); opponent loses the weapon (then **Retrieve**, canonical, to recover).
- **Control / Tie Up** (canonical) — both −2D; blocks Escape; sets up the finish.
- **THE FINISH — dagger to the gaps (NEW):** against a **grounded/controlled** foe, a **point** weapon (rondel dagger) thrusts the **gaps** — resolved on the armour matrix as **coverage→gap** (point retains its mod; a controlled prone foe = gap access). **This bypasses armour mitigation entirely** and is the historical kill: wrestle the armoured man down, dagger through the visor/armpit. The rondel dagger existed for exactly this.

**Escape** (canonical) is the defender's out at every step — an Agi contest to break the clinch (partial = exit + free strike), so grappling is not an inescapable lock.

## §4 — Why it's the third plate-counter (the validation target)

The three historical answers to plate, now all in the system:
1. **Blunt** — transmits percussion through plate (armour matrix; fells in 3). ✓ built
2. **Point to gaps** — the thrust finds the gaps (W5 + coverage). ✓ built
3. **Grappling → dagger** — throw/control the armoured man, dagger the gaps; **bypasses mitigation**. ← this system

Against full plate, a grappler who can **close, take down, and dagger the gaps** fells the harness where a *cut* weapon cannot — completing the triad. And it's **balanced by risk:** closing surrenders reach/tempo, so a skilled weapon fighter who keeps distance beats the closer (tempo/reach > the grapple attempt at range); 2H/heavy fighters grapple worse. High-risk, high-reward — NERS-Necessary (a real decision, not a win-button).

## §5 — NERS + over-engineering guard

- **Necessary:** fills the canon-acknowledged unarmed/close gap (ED-129); completes the plate-counter triad; gives Strength its close-range expression. Removing it leaves plate with only two counters and Strength under-expressed at range.
- **Robust:** holds at the extreme of the state graph; reach-inversion + Strength-dominance + the dagger-finish are structural; Escape bounds it.
- **Smooth:** reuses the canonical actions (Disarm/Tie Up/Escape/Retrieve), the σ-engine, ST1, the armour matrix (coverage→gap), the hands axis — one consistent vocabulary; the grapple is just the innermost state.
- **Elegant:** grappling = the innermost engagement state + a Strength σ-contest + the canonical actions as its outcomes + one new finish. The player intuits: *close the distance, overpower the clinch, put him down, dagger the gaps* — and the cost (you gave up reach/tempo to get there).
- **Over-engineering guard:** **no separate grappling skill tree, no positional sub-game (mount/guard/etc.)** — that is the grappling over-engineering trap. Grapple is one σ-contest with margin-scaled outcomes drawn from the *existing* canonical actions. The clinch is a state, not a subsystem.

## §6 — What remains yours (contract)

1. **Ratify** the grapple-contest framing + the **dagger-finish** (the one new mechanic — a controlled/grounded foe takes a point strike on the gap profile, bypassing mitigation). The reused actions (Disarm/Tie Up/Escape/Retrieve) are canonical already.
2. **In-world naming** — Valorian terms for the wrestling tradition/close-combat are your creative layer; the above is the *abrazare*/*ringen* historical archetype only.

`[ASSUMPTION: the dagger-finish models a controlled/prone foe as gap-access (point profile, mitigation bypassed). Flag if you want the finish gated differently (e.g. requiring a prior Tie Up + a separate finish roll).]`
`[GAP: a full unarmed/striking system (punches/kicks) is broader than the anti-armour grapple built here; abrazare is grappling-centric, so this covers the clinch/throw/disarm/finish, not a striking art. Flag if you want striking too.]`
