<!-- STATUS: AUDIT — analytic instrument output, not canon. Self-exempting (Class A analysis). -->
<!-- Investigation: operational/integration coherence sweep of the social contest system across four axes:
     (A) internal logic & coherence, (B) faction-dynamics & political-event integration, (C) Key-bus wiring,
     (D) player legibility & fun. -->
<!-- Method: 8 analysts (one per lens) + adversarial verification of every finding against the live working tree.
     49 agents, ~3.25M subagent tokens. 41 findings raised, 41 survived verification (0 refuted): 18 major,
     12 minor, 11 cosmetic (corrected severity). Raw verified findings: findings.json. -->

# Valoria — Social Contest Coherence Sweep: logic, faction/event integration, Keys, and player experience

**Date:** 2026-06-28 · **Scope:** the full social-contest stack (spec + infill + params + extensions + sim) audited for *whether it works* — read against the faction layer, the political-event machinery, the Key substrate, and the UI/articulation surface.

This is the third 2026-06-28 pass on the contest and is **operational**, where the prior two were structural: the [distillation-coherence report](../2026-06-28-distillation-coherence/distillation_coherence_report.md) mapped the engine, and the [deliberation-as-game critique](../2026-06-28-social-contest-deliberation-critique/critique.md) judged the *design*. This one asks the plainer questions you posed: is the logic coherent, does it wire into the factions and the politics, does it live on the Keys, and is it legible and fun? All three passes converge on the same diagnosis from different angles.

---

## 0. Executive summary (plain language)

**Bottom line: the contest is sound where it is designed and broken where it is wired.** The rules on the page are coherent and the live tabletop loop is genuinely legible and playable. The damage is concentrated at two seams — the **Key bus** (the contest's durable consequences are silent off-bus writes) and the **simulation** (a degenerate stub that cannot validate the real kernel) — plus one **name collision** that quietly corrupts both legibility and a cross-scale faction wire.

Verdicts on your four questions:

| Question | Verdict | One-line reason |
|---|---|---|
| **A · Is the logic coherent?** | **Yes on the page, No in the executable.** | The known resolution pathologies have coherent, non-colliding fixes; but the sim models *none* of the redesigned kernel, and two lifecycle contradictions (the half-retired Deadlock rule; Succession contradicting its own flagship Crown instance) would give two GMs different outcomes. |
| **B · Does it integrate with faction dynamics & political events?** | **Mostly — and bounded — but two flagship wires are broken.** | No runaway (the Mandate loop is genuinely damped) and the event lifecycles are largely coherent; but the NPC-Obligation "a political win constrains the AI" promise writes into a priority-tree hook **that does not exist**, the Mandate writes contradict the canonical derived-Mandate ruling, and a cross-scale Domain Echo is keyed to the **wrong track**. |
| **C · Does it work with Keys?** | **No — the in-scene event is clean, but every durable consequence is off-bus.** | `scene.contest_resolved` is emit/consume-closed and proves the pattern, but Obligations, Domain Echo, Belief revision, and Succession/faction-split are all silent state writes — replay-breaking and invisible to the chronicle. This is the most concentrated debt. |
| **D · Is it legible and fun?** | **Legible and playable at the live table; undercut by naming and by chronicle-blindness.** | The player watches the track move and sees the dice assemble (real transparency), and the Appraise read-the-room loop is good fun — but the score track shares a name with a *different* meter, venue variety is unproven (the sim can't exercise it), a couple of marquee choices have dominant lines, and the chronicle can't see the contest's consequences. |

**If you do only four things:** (1) **bus the post-resolution consequences** (Obligations / Domain Echo / belief-revised / succession) — fixes Keys *and* chronicle legibility at once; (2) **collapse the track-name collision** (Persuasion vs Piety vs Conviction) — fixes a legibility defect *and* a cross-scale mis-wire; (3) **wire the NPC-Obligation priority gate** that the spec already promises; (4) **bring the sim up to the canonical kernel** so "balance verified" stops being a paper claim. None requires a new mechanic.

---

## 1. The cross-cutting meta-finding: the page is fine; the seams are not

> **Three independent 2026-06-28 audits now agree: the social contest's design is coherent and on the right engine primitives, and essentially all of its debt is *seam debt* — unkeyed consequences, an un-updated sim, and propagation/naming drift across consumer docs.**

Every one of the 18 major findings is a *wiring* or *propagation* failure, not a *design* failure:

- **The Key seam** (axis C, 5 findings): the contest computes the right consequences but doesn't put them on the bus. This is the distillation report's "rich unkeyed state / delivers-blind down-seams" (MEDIUM ESCP tier) made specific.
- **The sim seam** (axis A, 5 findings): the executable reference is a single-compare stub that implements none of the interaction matrix, dice inputs, strain economy, or resistance erosion — so the balance the corpus calls "confirmed" is unvalidated against the real rules.
- **The propagation seam** (axes B & D, ~6 findings): names and magnitudes drift across consumer docs — the Persuasion/Piety/Conviction track-name collision, the Domain Echo keyed to Piety Track, the Mandate-write-vs-derived-Mandate conflict, the loser-penalty drift, Panel provisional-vs-canonical.

The good news in that framing: **none of this is "redesign the contest."** It is the same "unification and seam-closure" verdict the distillation report reached for the whole engine — apply the `targets[]`/`stat_deltas` Key discipline, run one rename pass, lift the working sim branch logic into production, and pin the duplicate succession specs.

---

## 2. Axis A — Logic & coherence

**Verdict: coherent on the page, not in the executable; two real lifecycle contradictions.**

**Coherent (credit):**
- The three historical resolution pathologies have **coherent, non-interacting ratified fixes** (`A1-1`): CLASH no longer stalls (ED-864 per-exchange resistance erosion, applied to *all* interaction types so solo advocacy still resolves), REINFORCE can't underflow (`max(0,…)` floor), and coalition-dominance is intentional parliamentary design (ED-297). The three fixes touch independent quantities and don't collide.
- The **Heresy Investigation lifecycle** is a complete, exit-closed state machine (`A2-4`): 8 closure conditions, each with effect + rationale, no state without an exit — "the model the other sub-systems should match." (Minor caveat: the entry-gate wording drifts slightly from the rank ladder, and the Verdict outcomes aren't keyed.)
- Channel-reservation is honored: Rattled routes to a `−1D` Pool penalty, not `+Ob` (`C1-7`).

**The executable doesn't match the page (the sim seam):**
- `A1-2` (**major**): the production sim `resolve_exchange()` is a **single margin-vs-resistance compare** — no CLASH/REINFORCE/CROSS/TIE branch, no genre/orientation/Recall/Momentum dice, no Composure/strain/Concentration. It models none of what makes one exchange differ from another. *(Verifier downgraded critical→major: the canonical kernel is fully specified in the spec; this is known sim-debt, and a working branch implementation exists in `tests/sim_framework/contest.py` to lift from.)*
- `A1-3` (**major**): the sim omits the **ED-864 resistance erosion** — the very anti-stall fix — so it would reproduce the ED-295 stall the design already fixed and can't validate long contests.
- `A1-4` (**major**): **Contest Fatigue mis-gated** — the sim fires it on every Decisive win; canon reserves it for Total Victory (≥9/≤1). The correct flag is already computed but unused.
- `A1-5` (**major**): **ties hard-wired toward side A** — canon moves the tie toward the first-to-speak *holder*, a rolled/transferred state the sim doesn't track; injects a systematic directional bias.
- `A1-6` (**major**): **SIM-DEBT-03 is marked RESOLVED on "historical precedent"** while the sim models none of the redesigned mechanics and the cited ED-295 is still an open P1-blocker in the ledger. The corpus presents un-validated balance as validated.

**Two lifecycle contradictions (the real coherence cracks):**
- `A2-1` (**major**): the **§6.3 Deadlock block contradicts its own retirement note** — the ED-896 header says the resistance-drop is "redundant and retired," but the live bullets still print it as active *and* the surviving terminator is anchored "after the Resistance drop." A half-applied edit; two GMs reach different track outcomes.
- `A2-3` (**major**): the **Succession Contest (§7.2) contradicts its own canonical Crown instance** (`baralta_crown_claim §2`): different eligibility tests *and* different resolvers (Grand-Contest Persuasion Track + inner-circle Disposition vote vs. a single pool-roll-vs-Ob-3). The one fully-worked succession case can't be run from §7.2's rules. *(See also B2-2, C1-4.)*

Lower-severity: Heresy "Insufficient Evidence" suspend-state has a resume condition (Evidence Track ≥ 3) with **no defined producer** during suspension (`A2-2`, minor); Panel is **provisional in the spec but "accepted as canonical" in params** (`A2-5`, minor); §7.1/§10.1 sit out of numeric order after §11, splitting the Tribunal/Stay counter-play loop from its references (`A2-6`, cosmetic).

---

## 3. Axis B — Faction dynamics & political events

**Verdict: bounded and largely coherent, but two flagship faction-wires are broken and one cross-scale Echo is mislabeled.**

**Bounded & coherent (credit):**
- `B1-3` (**strength**): **no win→Mandate→pool→win runaway.** The contest→Mandate path is damped on every link — Domain Echo caps at ±2/stat/season, Mandate hard-ceilings at 7, and the settlement→Mandate aggregate saturates via `7T/(T+6)`. Stronger than claimed: at *personal* scale Mandate doesn't even feed the Argue pool, so no feedback path exists there at all.
- `B1-5` (**strength**): the **Succession faction-split** divides faction stats by track-weighted ratios with a Stability-3 floor that deliberately avoids spawning an immediate catastrophic-collapse zoom — clean integration with the scale-transition hysteresis. (Nit: the split list omits the `Intel` stat, stale vs ED-787.)
- `B3-5` (**strength**): the **Lobby Cap** holds the BG/Hybrid starting track to 4–6 so lobbying gives bounded advantage, never a guaranteed win — the anti-degeneracy property is real and faithfully coded for BG.

**The two broken flagship wires:**
- `B1-1` (**major**): the headline promise — *"a won contest has lasting strategic impact; the player can constrain an NPC faction's behavior through political victory, not just stat changes"* — is **unhonored**. The contest spec says the NPC priority tree is modified to block Obligation-violating actions, but `npc_behavior §8` (the 7-level template + all nine faction trees) **contains no Obligation gate**. The hook writes into nothing; a beaten NPC keeps acting freely. *Fix: add a Priority-1.5 Obligation gate to the §8.1 template that prunes candidate actions breaching an active Obligation clock (reuses the priority-tree filter + the clock) — one row.*
- `B1-2` (**major**): contest **"Mandate +1/−1" writes contradict the LPS-2e ruling** (2026-05-30) that re-grained Mandate as a *pure derived aggregate* of per-settlement L/PS — "never written directly." There is no defined way to apply a contest's "+1 Mandate" under current canon, and "+1" isn't even on the settlement ΔL/ΔPS scale. *Fix: restate Domain Echo/Obligation consequences as ΔL/ΔPS routed through the §1.8 mission-outcome path, letting the aggregate produce the Mandate move. (This is one instance of a corpus-wide write-channel debt the LPS redesign already tracks.)*

**The mislabeled cross-scale Echo:**
- `B3-4` (**major**): `scale_transitions §5.4` keys the faction Mandate Domain Echo off **"Piety Track"** outcomes — but contests resolve on the **Persuasion Track**, and Piety Track is a *separate* 0–5 per-territory religious-standing clock. A literal implementer wires faction Mandate to the wrong meter. The defect is duplicated in `params/scale_transitions.md` (two places). Root cause is the stale "Debate"→"Contest" rename. *(This is the same name collision as D1-1.)*

**Political events:** the Heresy → CI-milestone → Stay loop is coherent (the CI<55 Stay gate, the `floor(CI/20)` pool bonus making the Stay unpassable at 55+ all agree across docs), and the Heresy lifecycle is exit-closed (`A2-4`). The two defects are the Succession-spec contradiction (`B2-2`, major, = A2-3) and the unkeyed succession output (`B2-1` → C1-4). Propagation nit: the throughlines summary records an unconditional "loser Mandate −1" that the spec reserves for Total Victory/institutional-authority losses (`B1-6`, cosmetic).

**Scale integration:** BG↔TTRPG↔Hybrid coheres at the spec level; the vote-to-contest zoom skeleton looked like an empty stub but is authored in the infill (`B3-1`, already-handled, cosmetic); the Persuasion Track is annotated `-5..+5` in the Key vs `0–10` live (`B3-3`, minor — only the *final-position* field is mis-typed; the per-exchange *displacement* field is correctly signed); §11 vs PP-256 offset wording is cosmetic (`B3-6`).

---

## 4. Axis C — Keys

**Verdict: the in-scene event is clean; every durable consequence is off the bus.**

**The pattern is proven (credit):**
- `C1-7` (**strength**): `scene.contest_resolved` is **emit/consume-closed** — registered with `social_contest` as emitter and `npc_behavior`/`faction_layer`/`articulation` as consumers, recorded in `module_contracts`, with the channel-reservation invariant honored. This is the template the post-resolution consequences should follow.

**The durable consequences are silent off-bus writes (the Key seam — 4 majors):**
- `C1-1` (**major**): **Obligation creation** — the contest's longest-lived, most consequential output — writes a cross-season clock with **no emitting Key**. Replay can't regenerate it; the chronicle can't narrate it; the NPC-behavior block (B1-1) is driven by off-bus state.
- `C1-2` (**major**): the **Domain Echo faction-stat grant** is an unkeyed cross-scale write — `scene.contest_resolved` carries no `faction_id`/`stat_deltas`/`targets[]` and its `scale_signature` is `[personal]` only. The cross-scale "all-directions" guarantee is aspirational here. (The distillation report's named "delivers-blind down-seam.")
- `C1-3` (**major**): **Belief Revision** specifies *when* an NPC revises a belief but never emits `state.belief_revised`; the registry attributes that Key to `fieldwork` only, with an explicit STUB flagging the gap (ED-937 / workplan #32). The articulation Tier-2 cut-scene trigger fires only on that Key, so contest-driven belief inflections are dropped from the chronicle.
- `C1-4` (**major**): the **Succession outcome** never emits `state.succession` (registry attributes it to `faction_politics` only), and the **Compromise faction-split has no Key type at all** (`faction_split` does not exist in the vocabulary) — so a new sub-faction with inherited Mandate/Military/territory is a pure off-bus write, breaking the promised `cascade_resolution` chain and articulation Trigger #3.

Lower-severity: the reference sims emit no Keys at all (`C1-5`, overstated→minor — this is a *whole-tier* property, the Python sims are a pre-Key balance layer by design, not contest-specific); the articulation Tier-2 ruleset omits `scene.contest_resolved`, so a routine Decisive win that binds an Obligation fires no cut-scene unless it incidentally also produces a Scar/Belief Key (`C1-6`, minor — directly against the legibility goal).

*Fix for the whole axis (one discipline): make the post-resolution consequences ride the proven `scene.contest_resolved` pattern as registered child Keys (`state.obligation_created`, the Domain-Echo grant with `targets[]`/`stat_deltas`, `state.belief_revised` as a multi-emitter, `state.succession`+a `faction_split` representation), each with the parent contest Key as cause — exactly the distillation report's universal `targets[]` discipline. Reuses the bus; no new subsystem.*

---

## 5. Axis D — Player legibility & fun

**Verdict: legible and playable at the live table; undercut by a name collision and by chronicle-blindness. Fun rests on a strong read-the-room loop, with a few dominant lines and unproven venue variety.**

**Legible at the table (credit — directly addresses the opacity pain):**
- `D1-2` (**strength**): the UI **animates the score track moving each exchange toward the win line** and **assembles the Argue pool on-screen with a per-source bonus breakdown before the roll**, plus the Appraise audience-boost result pre-commit. The player watches the meter move and sees exactly which dice they earned — the opposite of a black box.
- `D1-4` (**strength**, with a caveat): the genuinely hidden items (opponent/judge Resonant Style, audience boost, NPC Scar count) each have an in-fiction **discovery move** (Appraise degrees) and graduated tells — tension-generating fog-of-war, not opacity debt. *(Caveat: the promised "Appraise reveals the Scar count later" path is a dangling cross-reference — §6.1 "Appraise Revelation" is an empty stub in the spec; the reveal is only specified for Resonant Style + one Belief, not the count.)*

**Legibility defects:**
- `D1-1` (**major**): the score track has **three names corpus-wide** — canonically "Persuasion Track" (0–10), but `npc_behavior` and the v4.1 UI call it "Piety Track," and v4/the resolution diagnostic call it "Conviction Track" — and "Piety Track (PT)" is *also* the canonical name of a **separate 0–5 per-territory orthodoxy clock**. A player consulting consumer docs sees "Piety Track ≥ 7 or ≤ 3" describing a meter that only runs 0–5. *Fix: one rename pass — contest track = "Persuasion Track" everywhere; reserve "Piety Track" for the territory clock. (Same fix resolves the B3-4 cross-scale mis-wire — high combined leverage, J-31-class repair.)*
- `D1-3` (**minor**): **audience resistance** — the beat-this-line number gating every track movement — is shown in v4 as a standalone announced value but is **not fused onto the track as a threshold marker**, and there's no per-exchange margin-vs-resistance readout, so a 0-movement exchange reads as arbitrary ("I won but the bar didn't move"). (Also: under ED-864 resistance now erodes per exchange, so the marker must update, not sit static.)
- `C1-6` (**minor**): the chronicle/cut-scene layer doesn't fire on contest resolutions — the consequential political outcome (a binding Obligation) is invisible to the retrospective "why did this happen" surface.

**Fun & agency:**
- `D2-2` strength: the **Appraise read-the-room loop** (read the audience, a mis-read returns a *misleading* signal) is the genuine fun core.
- `D2-1` (**minor**, overstated): two marquee choices lean toward dominant lines — **Obscuring wins give a free Doubt Marker at no self-cost**, and **ED-297 makes coalition strictly beat solo**. *(Verifier tempered this: coalition-dominance is intentional; Obscuring forgoes track movement so it's a trade not strict dominance; solo counter-levers exist — Resonant Style targeting, Recall, Findings. The real fix — CR5 self-Face backfire on a failed Obscuring — is ratified-but-unpropagated, the same "stranded design" theme as the deliberation critique.)*
- `D2-2` (**major**, compound): **venue variety is unproven** — SIM-DEBT-04 is open and the sim collapses every venue to one pool roll, so "format follows context" delivering *distinct* experiences is unvalidated; the **cold-equilibrium terminator freezes Disposition and locks a topic for 4 seasons** (anti-churn — flatlines an arc); and **Regroup's full Concentration refill dominates Concede a Point**.

---

## 6. Ranked recommendations

| # | Recommendation | Fixes | Leverage | Effort | Tag |
|---|---|---|---|---|---|
| 1 | **Bus the post-resolution consequences** — emit registered child Keys for Obligation creation, the Domain-Echo grant (`targets[]`/`stat_deltas`), `state.belief_revised` (multi-emitter), and Succession + a `faction_split` type, each caused by the parent `scene.contest_resolved`. | C1-1, C1-2, C1-3, C1-4, B2-1 | ★★★★★ | med | structural |
| 2 | **Collapse the track-name collision** — contest track = "Persuasion Track" everywhere; reserve "Piety Track" for the 0–5 territory clock. Re-key `scale_transitions §5.4` Domain Echo to Persuasion Track (+ the params twin). | D1-1, B3-4 | ★★★★★ | low | free-win |
| 3 | **Wire the NPC-Obligation priority gate** — add a Priority-1.5 Obligation block to the `npc_behavior §8.1` template so a political win actually constrains the AI's action set. | B1-1 | ★★★★ | low–med | structural |
| 4 | **Bring the sim up to the canonical kernel** — interaction-type branch, genre/Recall/Momentum dice, strain/Concentration, ED-864 erosion; fix Contest-Fatigue gating + tie direction; then re-run SIM-DEBT-03/04 (lift `tests/sim_framework/contest.py`'s working branch logic). | A1-2..A1-6, D2-2 | ★★★★ | med | structural |
| 5 | **Reconcile the Succession duplication** — pin `baralta §2` vs `§7.2` to one resolver (the §11 Hybrid bridge is the natural reconciler), align triggers and eligibility, route the outcome through `faction_politics`' `state.succession` emit. | A2-3, B2-2 | ★★★ | med | needs-your-call |
| 6 | **Fix the Mandate write channel** — restate Domain Echo/Obligation Mandate consequences as ΔL/ΔPS through the §1.8 path so they respect the derived-Mandate (LPS-2e) ruling. | B1-2 | ★★★ | low–med | structural |
| 7 | **Free-wins & polish** — clean the §6.3 Deadlock retirement (strike the dead bullet, re-anchor the terminator to raw zero-movement); reconcile Panel provisional/canonical; reorder §7.1/§10.1; fuse resistance onto the track in the UI + per-exchange margin readout; add a contest Tier-2 articulation trigger; gate Regroup's refill; convert cold-equilibrium to a decaying Deadlock clock; add `Intel` to the split list. | A2-1, A2-5, A2-6, D1-3, C1-6, D2-1, D2-2, B1-5 | ★★ | low | free-win |
| 8 | **Propagate the stranded design** — CR5 self-Face backfire (eristic cost); the groundup pluggable win-conditions + Panel model. (Shared with the deliberation critique's §5.) | D2-1, A2-5 | ★★ | low | free-win |

**The three highest-leverage moves (1, 2, 3)** together fix replay-determinism, chronicle legibility, the worst naming defect, a cross-scale mis-wire, and the headline faction-integration promise — and not one of them changes a mechanic's behavior.

---

## 7. Do-not-touch (load-bearing — preserve through any change)

- **The clean in-scene `scene.contest_resolved` Key + channel-reservation** (`C1-7`): the proven pattern. Make the new consequence-Keys ride *this*, not a parallel channel.
- **The damped Mandate loop** (`B1-3`): the `7T/(T+6)` saturation + ±2/season cap + P-20 ceiling. Don't add a write path that bypasses the aggregate.
- **The Succession faction-split's Stability-3 floor** (`B1-5`): keeps a hung succession playable, not catastrophic.
- **The live UI track + pool-assembly breakdown** (`D1-2`) and **the Appraise read-the-room loop** (`D2-2`): the legibility and fun core — the opacity-mitigation already in place.
- **The Lobby Cap** (`B3-5`) and the **Heresy lifecycle's exit-closure** (`A2-4`).
- **The two-primitive discipline:** every fix above reuses the sigma resolver, the armature dot-product, the Key bus, or an existing bucket. Reject any "fix" that adds a parallel resolver or a bespoke delivery channel (the substrate forbids it).

---

## 8. Method, honesty, and provenance

- **Lenses:** 8 analysts across 4 axes (A1 resolution-math, A2 lifecycle-coherence; B1 contest→faction, B2 political-events, B3 scale-integration; C1 key-integration; D1 legibility, D2 fun/agency), each grounded in verbatim quotes and judged against coherence / bounded-integration / Key-closure / legibility-and-fun standards plus engine discipline.
- **Verification:** every one of 41 raised findings was adversarially re-checked against the live working tree (with the verifier specifically tasked to find where a claimed gap is *already handled* elsewhere). **0 refuted; 24 sound, 14 overstated (severity reduced), 3 already-handled.** Severities and scopes in this document are the *corrected* values — which is why several alarming-sounding findings (the sim being off-bus; the vote-to-contest "empty stub"; the resistance "never surfaced") were tempered to minor/cosmetic once context was checked.
- **Convergence:** the diagnosis matches the two prior 2026-06-28 audits — the distillation report's MEDIUM ESCP tier + "rich unkeyed state / delivers-blind seams," and the deliberation critique's "stranded ratified design." The contest's debt is seam-and-propagation, not design.
- **Honest limits:** (a) the working-tree design docs are source-of-truth; sim findings describe a balance/verification layer that is pre-Key by design, so "off-bus" sim observations are conformance gaps, not architecture breaks. (b) Lever magnitudes (thresholds, deltas) are starting points for sim-validation, not canon. (c) The script's per-lens `axis_verdict` field did not surface to the run output (a harness bug reading the wrong pipeline stage); the per-axis verdicts in §2–§5 were reconstructed from the verified findings.
- **Artifacts:** full verified findings with verbatim quotes and per-finding verdicts in `findings.json`; workflow script at `.claude/wf_social_contest_sweep.js`.
