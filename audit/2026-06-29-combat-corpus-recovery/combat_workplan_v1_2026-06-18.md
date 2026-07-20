# Combat — unified work plan v1
### Reconciles the 06-17 decision docket + the 06-18 reconciliation handoff into one critical path

**2026-06-18 · status: PROPOSED working master · pinned to HEAD `103b2ba9` · SUPERSEDES the 06-17 docket `6ed05e9e` (folds its D1–D9/M1–M4 into the tracks below)**

`[SELF-AUTHORED — bias risk: consolidates two Claude-authored surfaces (my docket + the parallel-session handoff). Lethality/wound/magnitude targets are flagged Jordan-only throughout; the D-A defect is re-grounded in live core.py:72, not transcribed.]`

`[READ: handoff "Combat-engine reconciliation (ED-935)" 2026-06-18 · designs/scene/combat_engine_v1/core.py @HEAD (lines 32–80) · commits sha=main last 10 · prior docket 6ed05e9e]`

---

## §1 — State at HEAD `103b2ba9` (committed)

| Layer | State | Commit |
|---|---|---|
| Stage 1 — μ-shift resolution + P_auth + atk_sig→Concentration | **LANDED** | `15269f3c` |
| Stage 2a — linear continuous-transmission damage (tanh cap removed) + cut_thrust half-sword | **LANDED** (mirror 50.0, draws 4.1%, RATIFIED_TABLE + WI reproduced) | `b9350a4d` |
| M1 — `eff_cw` wiring finished (5 wrapper sites; engine now 23/23 on eff_cw) | **LANDED** (byte-identical no-ability; ×1.20 verified) | `699b77a2` |
| Stage 2b — plate percussion .30→.85, blunt coupling = max(concussion, pierce) | **wired LOCAL, uncommitted** — blocked on D-A | — (parallel session `/home/claude/combat_engine_recon/core.py`) |

Parallel session is now on **mass-battle** (per-subunit stamina, ED-1018 troop taxonomy) — write-disjoint from personal combat. The combat-recon thread is parked at the two decisions below.

---

## §2 — THE CRITICAL PATH (the damage/resolution reshape)

Everything hot converges on **one Jordan decision (D-A)** preceded by **one measurement I can run now (M4)**. This is the spine; Stage 3 folds into it; D-B is its tail.

```
M4 wound-sweep ──► D-A LETHALITY DECISION ──► D-A reshape (folds Stage 3) ──► D-B magnitude ──► validate+commit 2b
 (me, now)          (Jordan: A/B/N)            (me, gated)                     (me, gated)
```

**The defect being fixed (grounded, live `core.py:72`):**
`damage = (strength + heft) · coupling · QUAL · DMG_SCALE(1.55)` — strength enters **additively** and the scale is anchored so an even Success ≈ 1 WI. Result: at a fixed degree, damage collapses to ~4–17, so weapon / armour / strength choices barely move the number. **NERS-R failure** — the player's choices don't visibly matter. Stage 2a uncapped transmission but left the scale compressed.

**Step 0 — M4 wound-sweep (prerequisite, executable now).** Re-measure the wound-handicap parity anchor (.490 / .329 / .215) against HEAD (post-2a), so the D-A reshape has a clean baseline to preserve. The handoff flags this as required *before* the reshape; the runtime is already assembled. *No decision needed.*

**Step 1 — D-A decision (BLOCKING, Jordan).** See §3. Sets the lethality target. Nothing downstream moves until this is set.

**Step 2 — D-A reshape (me, gated on Step 1).** Reshape for wide spread + uncap: clean heavy hit on unarmoured = devastating, no ceiling; hit throttled through plate = minor; strength / weapon / concentration produce **large ratios** (multiplicative strength, steeper armour coupling). **Folds in docket D3 (continuum degree + saturating QUAL) and D4 (pool recompute) — the handoff is explicit these overlap the scale reshape; do them as one coherent change. Must hold A6 parity** (re-run the anchors + contribution sweep).

**Step 3 — D-B magnitude (me, gated on Step 2; direction already ratified).** Re-size the pick-vs-mace beak advantage to read as a real gap under the widened scale; run the win-rate check vs a **plate** opponent (the standard sweep is light-armour, where 2b is invisible); confirm light-armour balance undisturbed; write the stage-2b validation note; commit the local 2b.

---

## §3 — Blocking decisions (Jordan — judgment, not mine to set)

| ID | Decision | Why it blocks | What's needed |
|---|---|---|---|
| **D-A** | **Damage-scale lethality target** (canon-structural, Class-A — touches Health / WI / MaxWounds) | the whole damage spine + D-B + Stage 3 QUAL all sit behind it | **(A)** keep Health/WI fixed → uncapping makes combat fast + lethal (clean unarmoured heavy hit ≈ one-shot; plate buys many exchanges) · **(B)** rescale Health/WI up → bigger numbers, similar hits-to-kill · or **(N)** a concrete number ("clean unarmoured heavy hit drops someone in ~N hits"). **Note: B alone does NOT fix the distinction problem — the reshape is needed regardless; A-vs-B only sets lethality on top.** |
| **D-B** | **2b puncture magnitude** (ratified direction; magnitude pending) | can't size the beak gap until D-A widens the scale | after D-A: the beak-vs-plate ratio to target. Direction validated top-down (Williams *Knight & Blast Furnace* ch9; war-hammer anti-plate record; plate-specific, broad concussion still dominates vs mail/cloth) |
| **M3** | seize-lever: retire **or** repoint `vorschlag` + `sen_no_sen` (authored ability content) | both empirically dead since the 2026-06-05 seize cut | retire the two, or repoint (`vorschlag`→open-steal; `sen_no_sen`→counter-on-commit) |
| **D1-H** | Health non-uniformity — MaxWounds stepping (noted in handoff) | a Class-A uniformity question that D-A option B would touch | confirm whether MaxWounds stepping is intended or a cliff to smooth |

---

## §4 — Executable now (me — no decision)

| ID | Task | State |
|---|---|---|
| **M4** | wound-sweep re-confirm (.490/.329/.215) vs HEAD — Step 0 of the critical path | runtime assembled; ready to run |
| **M2** | drop dead `max(5)` POOL_FLOOR | optional hygiene; `combatant.pool` is vestigial (live pool = `core.resolution_pool`) — confirm-then-cut, low value |

---

## §5 — Independent tracks (off the damage spine — can run in parallel)

**Track T — Tradition system** (docket D6/D7/D8; not in the handoff — separate thread). M1 already made channel-abilities fully live, which partially addresses D6's motivation but does not settle the representation question.
- **D6** representation: keep scalar channel-weights **vs** dissolve to abilities-primary (S3⊕S4: channels → player-allocated affinity budget). `[CANON]`/`[NEW]` — re-decide now that eff_cw is wired.
- **D7** ability schema (`trigger`/`cost`/`prereq`) + the ~55-ability library. `[NEW]`/`[BAL]`.
- **D8** new traditions / coverage (priority-gap schools ability-less until S1/S2 anchor; the urumi rigidity-axis candidate, T2/T3 sources pending T0/T1). `[CANON]`.

**Track R — Resolution scope** (docket D9): **ED-911** ranged / group / thread-in-combat have no engine resolution. `[CANON]`/`[NEW]` — scope a path or declare out-of-scope.

**Track S4 — Stage 4** (docket D5): disposition-as-selection (maneuver/ability/skill selection + timing; current 3 hooks measure NULL). `[NEW]` — scope-then-build, after the damage spine.

---

## §6 — Deferred refinements (noted, not blocking)

- Continuous-mass cut-impact (plan #9) — cut/thrust heft is weight-class for now.
- Poleaxe spike-thrust to gaps — only the beak-pierce is wired; the `thrust 0.83` + `halfsword` spike path is unmodelled.
- Rapier / light-thrust vs plate is heft-capped (finds gaps but does little) — the D-A reshape will move it; re-check after.
- M2 POOL_FLOOR (also in §4 as optional).

---

## §7 — Sequencing summary + provenance

**Do-next order:** `M4 (now)` → `D-A decision (Jordan)` → `D-A reshape incl. Stage 3` → `D-B` → then Tracks T / R / S4 as you prioritize. M3 and the Health question can be answered any time (they don't gate the spine).

**One-line state:** the wiring backlog is cleared (M1 landed; engine 23/23 on eff_cw); the damage layer is half-done (Stage 2a landed, 2b wired-pending); **the single thing gating the most work is the D-A lethality call**, and its only prerequisite (M4) is mine to run now.

**Supersession:** this plan supersedes the 06-17 docket `6ed05e9e` (its D1↔Stage 2a, D2↔D-B, D3/D4↔Stage 3-into-D-A, M1 done, M4↔Step 0 mappings are folded above). The 06-18 handoff is incorporated as the §1–§3 source. Generated/derivative files unaffected.

**Honesty.** `[CONFIDENCE: high]` on committed state (SHAs read live) and the D-A defect (grounded in core.py:72). `[CANON: D-A lethality, D-B magnitude, M3 retire/repoint, D1-H stepping are Jordan's]`. `[ASSUMPTION: the 06-18 handoff's Stage-2b local copy is accurate — basis: the handoff's own validation trail; the 2b edits are not at HEAD, so re-fetch the parallel session's working copy before committing D-B]`. `[GAP: pick-vs-plate magnitude — validated ranking, no calibrated anchor]`. Re-pin caveat: roadmap_state stale; 20 canonical sources flagged stale; nothing in §5–§6 committed.
