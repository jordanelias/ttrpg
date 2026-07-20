# Combat-engine reconciliation (ED-935) — handoff of proposed work
**2026-06-18 · status: 2 blocking decisions open for Jordan · as_of: this session (not re-bootstrapped — values from the session audit trail; re-pin HEAD before commit-grade use)**

`[SELF-AUTHORED — bias risk: summarizes this session's own work. The 2b "distinction" was over-sold as meaningful (6-vs-5); corrected below — the scale compression is the real defect, and it traces to a Stage-2a calibration choice of mine.]`

---

## Where it stands

**Committed (landed on `main`):**
- **Stage 1** — μ-shift resolution + P_auth (continuous blunt percussion authority) + atk_sig → Concentration tracker. Commit `15269f3c`. Validated.
- **Stage 2a** — linear continuous-transmission damage (tanh cap removed) + `cut_thrust` half-sword mode-shift. Commit `b9350a4d`. Validated (mirror 50.0, draws 4.1%, reproduced RATIFIED_TABLE + WI anchor, weapon gradients restored).

**Local working copy (`/home/claude/combat_engine_recon/core.py`), uncommitted:**
- **Stage 2b wired** — `RESIST[plate][percussion]` .30 → .85; blunt coupling = `max(broad concussion, concentrated pierce)`; `perc_conc` threaded damage → coupling → strike. Diverges from HEAD (HEAD = 2a). **Not committed** — blocked, see D-B.

---

## Proposed work — the open decisions

### D-A — damage-scale reshape + uncap · **BLOCKING** · Jordan sets the target
**Defect (surfaced this session).** At a fixed resolution degree the damage scale collapses into ~4–17, so weapon / armour / strength choices barely move the number — a **NERS-R failure** (the player's choices don't visibly matter). Two causes, both introduced in Stage 2a:
1. `DMG_SCALE` (1.55) anchored so a clean Success ≈ 1 wound (WI 10) — squeezes every hit toward ~10.
2. Strength enters **additively** (`strength + heft`) — a Str-7 swing is only ~1.5× a Str-1 one.

**Proposed fix.** Reshape for wide spread + uncap: a clean heavy hit on an unarmoured target should be devastating with no ceiling; a hit throttled through plate, minor; strength / weapon / concentration should produce *large* ratios. This reopens the 2a scale (the right call).

**Jordan's call (canon-structural — touches Health / WI / MaxWounds, Class-A):** the lethality target.
- **(A)** keep Health/WI fixed → uncapping makes combat fast + lethal (clean unarmoured heavy hit ≈ one-shot; full plate buys many exchanges).
- **(B)** rescale Health/WI up with damage → bigger numbers, similar hits-to-kill.
- **(B) alone does NOT fix the distinction problem** — that's a *ratio* issue (D-B); the reshape (steeper strength / armour / quality) is needed regardless. A-vs-B only sets lethality on top.

→ **Need from Jordan:** A, B, or a concrete number ("a clean unarmoured heavy hit drops someone in ~N hits").

### D-B — 2b puncture magnitude · **BLOCKED on D-A** · direction already ratified
**Ratified:** option (a) — adopt the pick-vs-mace distinction (a poleaxe beak defeats plate better than a broad mace).
**Done:** wired (above) and **validated top-down** against the armour-penetration record:
- Williams, *The Knight and the Blast Furnace* (ch9) — plate offered far better protection than the old 70%-through assumption; broad blunt is spread by the rigid shell.
- Arms & Armor / Medieval Collectibles — the war hammer was built to defeat plate; the beak concentrates force onto a smaller area, driving through where a broad mace only concusses. Mechanism = pressure (force/area) = the geometry's baked `strike_concentration`.
- Distinction is **plate-specific** (vs cloth/mail broad concussion still dominates — the war hammer was an anti-*plate* weapon).

**Why blocked:** under the compressed scale (D-A) the distinction reads as poleaxe **6** vs mace **5** vs plate — trivial (1 point). The direction is right and grounded; the *magnitude cannot be sized to read* until D-A widens the scale.

→ **After D-A:** re-size the beak advantage to read as a real gap, run the win-rate check vs a **plate-armoured** opponent (the standard sweep is vs light armour — 2b is invisible there), confirm the light-armour balance is undisturbed, write the stage-2b validation note, commit.

**Sequencing: D-A before D-B.**

---

## Deferred (noted, not blocking)
- Continuous-mass cut-impact (plan #9).
- Per-weapon gap-skill / poleaxe spike-thrust: the poleaxe carries `thrust 0.83` + `halfsword=true` — it could thrust its spike to gaps for more vs plate; only the beak-pierce is wired.
- Rapier / light-thrust vs plate is heft-capped (does little despite finding gaps) — a thrust-to-flesh concern; the D-A reshape will move it.
- Dead `max(5)` POOL_FLOOR cleanup (no-op, shared r8).
- Dead seize lever / `vorschlag` + `sen_no_sen` retire-or-repoint (authored ability content — Jordan's call).

## Future stages (Jordan scopes)
- **Stage 3 [NEW]** — continuum degree + saturating QUAL + pool recompute (must hold A6 parity). **Overlaps D-A** — the QUAL spread is part of the scale reshape; fold them together.
- **Stage 4 [NEW]** — disposition-as-selection.

## Housekeeping carried
- Wound-handicap parity anchor (.490 / .329 / .215) **not re-measured** this session — re-confirm with a dedicated wound-sweep **before** the D-A damage reshape.
- 3 unread session handoffs.
- D1 Health non-uniformity (MaxWounds stepping) noted.

---

## Engine state / provenance
- Working copy: `/home/claude/combat_engine_recon/core.py` = Stage 1 + 2a (committed) + 2b (local, uncommitted).
- HEAD: Stage 1 `15269f3c` + Stage 2a `b9350a4d`. The 2b edits are local-only.
- This handoff is session-derived; re-bootstrap and re-pin HEAD before commit-grade use. Can be landed via `write_handoff` under `designs/audit/2026-06-16-combat-reconciliation/`.

`[CONFIDENCE: high on committed state + the D-A diagnosis; the 2b direction is grounded, its magnitude is pending D-A]` · `[CANON: D-A lethality / wound thresholds + D-B magnitude are Jordan's to set]`
