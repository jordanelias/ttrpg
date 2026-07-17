# Auto / Manual Resolution Duality (v1)

## Status: Doctrine RULED 2026-07-08 (Jordan) — forks A/B/D resolved; fork C (calibration tolerance) the one residual, carried to the parity harness (§6–§8). Merging the landing PR ratifies the doctrine (ED-1094).
## ED: ED-SC-0013
## Origin: Jordan, 2026-07-08 — "faction parliament actions are the auto-resolve version of playing them out as a scene, in parallel to Total War where you can play the battle or auto it" + "every season of game is about specific events and actions that occur on a general interface/slate, so every action and decision are about something in particular."

---

## 1. The slate is the spine

Every season, the engine generates a **Scene Slate** — a general interface of **specific** events. This is not new design: it is `player_agency_v30 §4` (implemented as `sim/autoload/scene_slate.py`). The Slate is:

- **specific** — each entry is a particular event at a particular settlement (a named revolt, a succession, a heresy trial), not an abstract category;
- **priority-ranked** — `scene_slate` is a priority queue; mandatory events (`scale_transitions_v30 §4.3.2`, `zoom_in_out.check_mandatory_triggers`) sit at Priority 0, world-state events (§4.3.3) at Priority 1;
- **Conviction-biased** — generation surfaces events that intersect the player's active Convictions (player_agency §4), so what appears is *about something the player cares about*;
- **budgeted** — the player has **3–5 scene actions per season**; there are always more opportunities than actions. *Choosing what to attend is the gameplay.*

The load-bearing sentence is already in canon (player_agency §4.2): **"Opportunities not pursued do not wait — they resolve through NPC AI and clock advancement without player input, often in ways the player would not have chosen."**

That clause **is** the auto-resolve of a played scene. So the auto/manual duality is not a new mechanic bolted onto the game — **it is the resolution-fidelity axis of the Slate that already exists.** Every action and decision is *about* a specific slate event; the only question is at what fidelity each event is resolved.

## 2. The duality: two fidelities of one slate event

A slate event has two resolution fidelities of the *same* underlying conflict:

- **Play it out** — the event is resolved as a full personal-scale **scene** (the pursued event; the player spends a scene action).
- **Auto-resolve** — the event is resolved algorithmically on aggregate state, in one step (the un-pursued or over-budget event; "resolved through NPC AI without player input").

The scale-transition **zoom in / out** protocol (`scale_transitions_v30 §4`) is the toggle: **zoom in = play it out; zoom out = auto-resolve.** This is the Total-War auto-resolve / fight-the-battle duality, per specific event.

## 3. Fidelity is a spectrum, not a binary

Canon already carries a **third, middle** fidelity — **Witness Mode** (player_agency §4.2, "Mandatory overflow"): when more mandatory events fire than the player has actions, the un-attended ones are *witnessed* — the player gets the surface event plus **one free Read/Appraise** (a single roll, "not auto-success"), but does not play the scene. So the axis is:

| Fidelity | What the player does | Precedent (Football Manager) |
|---|---|---|
| **Played** | resolves the scene interactively (full agency) | watch the full 3D match |
| **Witnessed** | present, one light roll, no control | commentary-only |
| **Auto** | not present; NPC-AI resolves it | instant result |

The doctrine governs all three as one spectrum; "auto vs manual" is shorthand for its ends.

## 4. Acclaimed precedents (why this is the right shape)

- **Football Manager** — the cleanest analog: every **fixture is specific** (this match, these players, this rivalry), resolved at three fidelities of the *same* match engine — full match / commentary / instant result — calibrated so instant ≈ played. Witness Mode is its commentary.
- **Total War** — specific battles (this army, this place), auto-or-play *per battle*; auto is unbiased in expectation but you cannot *outplay* it.
- **Crusader Kings** — event-driven to the core: the slate *is* the event/decision feed; every card is a specific character in a specific situation; the decision is always *about* a particular thing.
- **XCOM** — the strategic slate surfaces specific missions; you play the ones that matter, the rest are abstracted.
- **Disco Elysium / Pentiment** — the "played scene" done right: every check is *about* a specific confrontation with a specific person.

player_agency §4's own design (budget-as-triage, opportunities-resolve-without-you) already imports this lineage; the doctrine names it.

## 5. Reference instance: the Parliamentary vote (and its debt)

The first auto-resolver shipped is the faction-scale §10 Parliamentary vote (`sim/cross_scale/parliamentary_bridge.py`, ED-SC-0006/0007, `ECHO_TRANSPORT` default ON); its played counterpart is the personal contest kernel (`sim/personal/contest/`), reached for the emergency-council scene via ED-SC-0006 (#96).

**Debt against §1:** the vote as shipped is a **generic per-season roll**, not the resolution of a *specific motion drawn from the slate*. That violates the slate principle. The doctrine's chief build implication is to **event-parameterize the auto-resolver** — each season it should auto-resolve the *specific* motions on the Slate (a war declaration here, a succession there), so the auto and played fidelities resolve the *same* slate event. (That re-architecture is a separate build, not this doc.)

## 6. The calibration constraint

Across fidelities, the outcome distribution of a given event **must be consistent on matched inputs**:

> **E[ auto outcome | event ] ≈ E[ played outcome | event ].**

**Rationale — exploit-prevention.** The auto-resolver emits *canonical* consequences (Mandate penalties, Domain Echoes) into the strategic layer. If fidelities diverge in expectation, whoever picks the fidelity is **mode-shopping** for the better outcome. Consistency makes the fidelity choice *free of strategic advantage* — a choice of richness/agency only. (player_agency §4.2 already asserts the auto path resolves "in ways the player would not have chosen" — i.e. an honest NPC-AI outcome, not a biased one.)

**Acceptance oracle.** A **parity harness** comparing the auto-resolver against the played kernel on matched inputs, asserting the outcome distributions agree within a stated tolerance. This is the acceptance gate for the ED-SC-0011 zoom-in expansion (§7). The tolerance itself is fork C (§8).

## 7. ED-SC-0011, reframed

The ED-SC-0011 work — deriving a played contest from aggregate faction state — is the **zoom-in expansion**: instantiate named orators (attributes / History / Convictions) for a specific slate event, calibrated to the auto-resolver per §6, with the parity harness as its acceptance gate. This makes the previously-"undefined party-derivation" **well-posed**: the derivation must produce actors whose *played* contest matches the *auto-resolved* outcome distributionally. (There was no target for the derivation to hit before; now there is.)

## 8. Forks — RULED 2026-07-08 (Jordan: resolve A/B/D, keep C open)

- **A — one engine, event-parameterized (RESOLVED).** The slate event supplies the specifics; **auto = the contest kernel run headless, played = the same kernel run interactively.** Not two mechanics — one engine at two fidelities. This is FM's model and matches player_agency's "resolve through NPC AI" (the *same* event, digested). It also retires calibration at the root: same engine ⇒ consistent by construction.
- **B — escalation predicate: the Scene Slate itself (RESOLVED by existing canon).** The scene-action budget (3–5/season) + slate priority + Conviction-bias *is* the triage; Mandatory triggers (§4.3.2) force a scene, everything else is opt-in. No new formula — this is `player_agency §4.2`.
- **C — calibration tolerance (OPEN — the one residual).** What tolerance counts as "consistent," and on which axis (pass/fail/committee share, Total-Victory rate, echo magnitude). Lean: **unbiased mean is the hard constraint** (anti-exploit); variance may be looser for auto (you accept the dice when you don't play); Witness Mode is a deliberately-thin middle (one roll, not auto-success). The actual number is set when the **parity harness** lands — it belongs to ED-SC-0011's acceptance gate.
- **D — choice vs forced: both, slate-marked (RESOLVED by existing canon).** Default is player *choice* (triage what to attend); the Slate **marks some events mandatory** (§4.3.2) — forced to a scene; over-budget mandatories fall to Witness Mode. All already in `player_agency §4.2`.

## 9. What this note does NOT do

It does not implement the parity harness, event-parameterize the auto-resolver, or build the played derivation — those are downstream builds (the derivation + harness is the ED-SC-0011 charter, §7). It states the Slate as the spine, names the fidelity spectrum and its precedents, and records the forks Jordan ruled.

The provisional parliamentary derivation shipped ON by default (proposer = lowest-Stability, establishment = highest-Mandate, others abstain) remains **retunable and is not ratified as canon** by this note.
