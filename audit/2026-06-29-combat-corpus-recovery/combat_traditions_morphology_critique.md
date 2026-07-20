# Combat Abilities & Traditions — a Martial-Morphology Critique of `combat_analysis_rev2.md`, with Improvements

**2026-06-25 · subject: `combat_analysis_rev2.md` §4 (tradition-ability hooks) · basis: `martial_morphology.md` (I) + `_vol2.md` (II) + `_vol3_efficacy.md` (III) + `_distilled.md` · engine grounded against `designs/scene/combat_engine_v1/` @ canonical HEAD**

`[SELF-AUTHORED — bias risk: the subject analysis and the engine were authored by prior Claude sessions in this project; this critique is of sibling output. I have actively looked for what such a critique is incentivized to soft-pedal — chiefly, that the engine's tradition layer is better than the analysis admits, and that one of my own proposed axes may be over-engineering. Both are stated below.]`

**Grounding trail.** Engine surface read first-hand, not from the analysis's report: `[READ: tradition.py — full]` (the 7-channel `TRADITIONS` dict, `FAMILIARITY`, the `ABILITIES` dict, `eff_cw`); `[READ: ability_armature.md — full]` (the phase×competence vocabulary, the lever map, the grounding discipline); commit-dated `7d9fa28`/`af7c678b` = **2026-06-03**, i.e. the tradition subsystem predates the **2026-06-22** analysis by 19 days. Morphology read in full (all five uploads). Inherited, not re-derived: the engine's sim verdicts and the morphology's efficacy weightings (both cite their evidence; neither re-run here).

---

## §0 — Verdict (worst-first; no false balance)

**The abilities-and-traditions material is the weakest part of an otherwise sound probe, and it fails on two independent levels.**

1. **Factual under-resolution of its own engine.** §4 of the analysis describes **three** "channel-weight biases" (tempo/visual/leverage), calls the abilities "placeholders today," and frames traditions as "four signature schools" / an "8 fixed tradition profiles" attachment-point model. The committed engine, on the day the analysis was written, already had **seven** live substrate channels, **five** live source-graded abilities, and an armature that had *explicitly retired* the "8 fixed profiles" framing in favour of "competence substrate + equipped modulators." This is correctable-factual error against canon, not interpretation.

2. **Structural incompleteness against the morphology standard.** Measured by the martial-morphology's own yardstick — a tradition is a vector across the *efficacy-bearing skeleton* (power-source, medium, range, initiative, force-relation, body-signature, targeting), dressed in *culture-framing*, and rated on *aliveness* — the engine's tradition model resolves the **reading/initiative/measure** dimensions well but is **structurally silent on three efficacy-bearing axes the morphology rates as load-bearing**: force-relation (D5), targeting (D7), and power-source differentiation (D1). This is the same defect the project already tracks as **J-33 / W4 #17 "traditions F2"** (`valoria_authoritative_map_v1.md` §5: combat "system NON-COMPLIANT … traditions F2"). NERS read: the tradition layer **fails R** (not "fully formed/complete" — missing the most efficacy-faithful degree of freedom) while the dice substrate beneath it stays compliant.

**Two tiers of fix, by layer.** (A) Correct the analysis to its own engine — pure factual repair. (B) Extend the engine's tradition axes along the three missing efficacy-bearing dimensions — **mechanical-tier**, built bottom-up on the engine's existing lever/channel machinery, validated top-down against documented martial precedent, **Jordan-vetoable**. The named-tradition roster, each tradition's flavour, and the entire `[B]/[L]` metaphysical layer stay **Jordan's creative/metaphysical layer** and are not touched here (§6).

---

## §1 — The standard, compressed (the yardstick this critique applies)

From the distilled core (its §1, §4) and Vol III's consolidation, the load-bearing apparatus:

- **Three dimension-classes.** *Efficacy-bearing skeleton* — D1 power-source, D2 medium, D3 range, D4 initiative, D5 force-relation, D6 body-signature, D7 targeting (these decide whether it works). *Culture-framing dressing* — D8 schema, D9 telos, D10 transmission, D11 energetic-model, D12 ethic, D13 governing-analogue (efficacy-neutral; chosen for meaning). *The single decisive variable* — D14 aliveness/resistance (predicts real efficacy more strongly than any content choice).
- **The four-axis evaluation standard.** Any tradition is a point in four-space: (1) **coherence** (does it hang together), (2) **epistemic status** `[M]`aterial / `[B]`elief / `[L]`myth, (3) **analogue-coherence** (is it what it says it is — Vol II G5), (4) **efficacy** (works against a fully resisting opponent — Vol III). Collapsing any axis into another was the union's central error.
- **The design order for anything that must work** (Vol III §6.4): fix the `[M]` skeleton + alive training *first*; choose analogue/schema/telos *last*, as efficacy-neutral dress. Skeleton before culture.
- **Per-atom efficacy weighting** (Vol III §2): force-relations and targeting are "among the most efficacy-faithful parts"; the convergent unarmed core is *range-control via wrestling/clinch + high-percentage strikes + dominant position + the choke*; P1/P2/P4 fully real, P3 real-kernel, P5 effects-real-mechanism-false, P8 null; T3 splits into real targets `[M]` (chin/liver/throat) vs the death-touch `[B/L]`.

This yardstick judges only **combat-telos (C1/C2/C3)** material; it is a category error to fault a health/spectacle/spiritual tradition for combat-inefficacy (Vol III §1 category guard). Valoria's personal combat is C1/C2 — so the yardstick applies cleanly.

---

## §2 — What the analysis says vs what the engine is (the factual correction)

Each row is canon-cited; per project authority rules, factual specifics are correctable against canon regardless of who stated them.

| Analysis §4 claim | Canonical reality (`combat_engine_v1/`) | Source |
|---|---|---|
| "Three channel-weight biases: **tempo, visual, leverage**" | **Seven** live substrate channels: `visual, tactile, precommit, leverage, tempo, measure, balance` — each a multiplicative cognitive-mode weight, neutral=1.0 | `tradition.py` `TRADITIONS` docstring + dict |
| Abilities are "**placeholders today**" | **Five live, source-graded** abilities wired at their engine sites: `indes`(+counter_success), `vorschlag`(+seize), `sen_no_sen`(+seize), `true_times`(+anti_overcommit), `mezzo_tempo`(×counter_select); **three more** registered (`staerke_schwaeche`, `misura`, `atajo`) pending the `eff_cw` channel sweep | `tradition.py` `ABILITIES`; `ability_armature.md` §7 |
| "Four signature schools map cleanly" / "8 fixed tradition profiles" | The "8 fixed profiles" framing was **explicitly generalized away**: "competence substrate + equipped modulators." Traditions are **7 cognitive modes** (german/italian/spanish/japanese/chinese/filipino/english + none), each a way of *reading the same physics*, plus an equippable-ability layer | `ability_armature.md` §1.2; `tradition.py` |
| (Not mentioned) | A **familiarity** system: traditions read unfamiliar opponents at 0.85 (0.93 if historically adjacent, 1.0 if same) — the mirror-match counter the analysis gestures at is a *concrete sub-system*, not a "scalar lever" | `tradition.py` `familiarity()`, `ADJACENT` |
| (Not mentioned) | A full **development armature**: phase×competence vocabulary, an 11-entry lever map with wiring status, a mandatory bottom-up+top-down grounding template, source tiers S1–S5, and the selection-effect discipline | `ability_armature.md` §§2–7 |

**The asymmetry that makes this a finding, not staleness.** The analysis is *current* on the wound model — it cites the `ab4e550c` bilateral-Ob change committed **2026-06-23**. It went deep on attributes (§1), weapons (§2), and the state graph (§3). On its own §4 subject — traditions, committed **2026-06-03** — it reports a third of the channels and calls a grounded, five-ability system a placeholder. The depth was available and not taken.

`[READ: tradition.py, ability_armature.md — basis for every row above]`

---

## §3 — What the engine's tradition model gets right (credited, not manufactured)

Honest-findings discipline cuts both ways: these are real strengths the analysis buries, and several are *the morphology's own best lessons, already implemented*.

- **"Modulate, never unlock" is the substrate/flavour separation, built.** The armature's principle 1 — every fighter has the whole vocabulary; a tradition only *biases* it — is structurally the morphology's deepest finding (distilled §6: meaning and efficacy run on separate tracks; flavour must not carry power). The `[M]` substrate is the shared engine; traditions are near-neutral re-weightings; the default (`none`, all 1.0) is byte-identical. That is *exactly* "skeleton fixed, culture as efficacy-neutral dress."
- **The mandatory bottom-up + top-down grounding is the `[M]`-grounding rule, codified.** Armature principle 4 — an ability must cite a documented technique *and* a real precedent or it is "not earned — do not invent" — is the morphology's epistemic spine and the PI project-owner contract's mechanical-tier gate, in the same words.
- **Source-tier + selection-effect is the survivorship-bias finding, operationalized.** Armature principle 5 — "patterns from the best-documented traditions were over-projected onto all"; priority-gap traditions get *no ability until an S1/S2 anchor exists" — is Vol I's A1/A9 and Vol III's F3 turned into an enforced sourcing constraint. Most martial-arts game systems do the opposite (every style equally fleshed out, history be damned); this one refuses to, on principle. Credit where due.
- **`familiarity` is the information contest (meta-C) made mechanical.** Reading an *unfamiliar* style worse — the deception/anticipation axis the morphology rates its single most efficacy-faithful pattern — is a live sub-system, with historically-grounded adjacency. This is more than the analysis's one-line "built-in counter to mirror-matches."

These are why the verdict is "structurally incomplete," not "wrong-headed." The architecture is sound; it is missing axes, not mis-built.

---

## §4 — The morphology-grounded gaps (failure surface, severity-ranked, from primitives)

Each gap names the morphology dimension, why it is efficacy-bearing (Vol III), what the engine cannot express, and a concrete two-fighter example that the current model collapses.

### G1 (HIGH) — Force-relation (D5) is collapsed to one channel, and only its bind sub-case
The engine's `leverage` channel covers **F1 opposition** and **F2 deflection** (Stärke/Schwäche, the geometric parry) — the *hard/structured* meeting of force in the bind. The morphology's D5 has six values; the other four are absent as tradition signatures: **F3 yielding-absorption** (*song* — give way, bleed the force), **F4 blending-redirection** (aiki/*lü* — join and turn it back), **F5 evasion** (void the line — the engine has *dodge* as a defence **mode**, but not as a tradition's force-relation lean), **F6 smothering** (jam/clinch — deny the commit-window). *Why it matters:* Vol III §2 (D3–D5) rates the force-relations "among the most efficacy-faithful parts of the union," and **efficacy-conditional** — F4 notoriously fails under full resistance when trained cooperatively, F5/F6 hold up because they are pressure-tested. *The collapse:* a Taiji-coded yielding fighter (F3/F4) and a Liechtenauer opposing fighter (F1/F2) differ on a genuine degree of freedom the engine has **no axis for** — both reduce to a `leverage` weight. This is the most efficacy-faithful axis the model omits, and the core of the J-33 "traditions F2" gap.

### G2 (HIGH) — Targeting logic (D7) is entirely absent as a tradition/ability axis
A landed hit computes degree + armour-defeat + the bilateral wound Ob — generically. No tradition *chooses* a targeting logic. The morphology's D7 has seven: **T1 gross-mass, T2 joints, T3 vital-points, T4 vascular/choke, T5 balance-base, T6 weapon-limb-first (defang), T7 psychological**. *Why it matters:* the convergent combat core (Vol III §1, §6.3) is *built on* T4 (the choke) and T5 (the base); FMA's whole identity is T6 (defanging the snake); *seme* and the freezing feint are T7. *The collapse:* a choke-oriented grappler (T4), a defanging blade-fighter (T6, the explicit FMA signature the engine names but cannot mechanize), and a composure-breaking pressure fighter (T7) all produce the *same* generic wound. The engine *has* the raw materials — poise/composure for T7, balance-break for T5, armour-defeat for T6 — but no targeting *selection* routes to them. (Boundary: T3 must be restricted to its `[M]` kernel — chin/liver/throat — never the death-touch; Vol III F6.)

### G3 (MEDIUM, and partly self-checking) — Power-source (D1) differentiation is absent
The four `[M]` power sources — **P1 skeletal-leverage, P2 conditioned strength, P3 elastic-fascial/whip, P4 gravitational-momentum** — collapse into the single Strength→strike-impact channel (analysis §1). Tellingly, `tradition.py` *labels* the Chinese tradition "fa jin burst" / `set='Burst'` — a gesture at **P3 elastic-recoil** — but encodes it as a flavour string, not a mechanical power-source distinction. *Why it matters, and why only medium:* Vol III §2 rates P1/P2/P4 fully real and P3 a real kernel, so the axis is grounded — **but** Vol III's own F9 ("taxonomic seduction") warns that real efficacy reduces to a few variables, and the engine already carries power via Strength + weapon mass/balance. *Self-check:* an explicit power-source axis risks being the over-engineering the morphology cautions against. It earns inclusion only if a *felt* distinction (the dropped-step single heavy blow vs the whippy fast combination) is judged worth a new lever; otherwise leaving power in Strength+weapon is the correct, NERS-N call. Flagged as optional in §5.

### G4 (MEDIUM) — The four-axis standard is never applied to the 7 traditions, and applying it finds concrete inconsistencies
The morphology's central tool is the four-axis evaluation; the engine seeds seven traditions but never runs them through it. Doing so now surfaces two real findings:
- **`chinese` is plausibly analogue-incoherent (G5 violation).** Its declared `mode='kinetic-rhythmic'` (the dance/music basin → springy/undulating body B5/B6, rhythmic feint-timing I2/I4) contradicts its actual channel profile, which emphasises `leverage=1.15 / tactile=1.20 / measure=1.20` — a *bind-and-measure* profile, not a flowing-rhythmic one. Vol II G5: a tradition is analogue-coherent only if its declared metaphor matches its body. This one says one thing and weights another.
- **`filipino` (and `chinese`) carry an epistemic tension between the two files.** `tradition.py` gives both a *full* cognitive-mode profile and `filipino` a slot in three `ADJACENT` pairs — i.e. treats them as well-characterized — while `ability_armature.md` §5 says FMA "the corpus does **not** anchor at S1/S2 (treat as unanchored: flag heavily or omit)" and lists both under "priority-gap traditions — **NO abilities**." The channel weights are a *claim about how the tradition reads physics*; if the tradition is under-anchored enough to be denied abilities, those weights are **as under-grounded as the abilities they're refused**. The selection-effect discipline is applied to abilities but not to the channel profiles.

### G5 (LOW / structural) — Aliveness (D14) has no in-fight referent — correctly, but unstated
In a videogame all traditions are exactly as effective as tuned, so D14 (whether a real art is pressure-tested) has no direct in-fight mechanic — and *shouldn't*. The engine has in fact adopted the morphology's discipline at the **sourcing** level: the selection-effect rule (only well-documented, pressure-tested traditions get abilities) *is* aliveness as a content constraint. The gap is only that this is never **named**, so the omission can read as an oversight rather than the deliberate, morphology-aligned position it is. Fix is one paragraph (§5 I5), not mechanics.

---

## §5 — Improvements (mechanical-tier, grounded, Jordan-vetoable)

All five **extend the armature's existing machinery** (the lever map, `channel_weight`/`eff_cw`, `ability_bonus`/`ability_factor`, the modulate-never-unlock + invariant-safety + bounded-Class-C discipline). None replaces it; each is a new *cell* in the armature's own phase×competence grid.

### I1 — Add **force-relation** as a competence (closes G1; highest value)
The engine already resolves a defence **mode** (parry/dodge/wind) and a post-contact transition (HIT/BIND/RIPOSTE). Add a `force_relation` competence whose abilities **bias which mode + which transition a fighter reaches for**, mapping F1–F6 onto existing seams:
- F1 opposition → hard-parry + bind-*dominate* (existing `leverage`).
- F2 deflection → the existing geometric parry (existing).
- **F3 yielding** → *absorb*: give ground, convert part of the incoming hit's initiative/poise swing into reduced damage (a defensive lever on `apply_wound`'s initiative term).
- **F4 blending** → *redirect*: on a successful defence, convert defender-sigma into an initiative-**steal** (route into the existing `seize`/RIPOSTE path). **Tag the Vol III efficacy caveat in the desc** — F4 is the one that fails cooperatively-trained; its `value` should be modest and gated on a skill/familiarity margin.
- **F5 evasion** → the existing `dodge` mode, promoted to a force-relation lean (no contact, trades position for safety).
- **F6 smothering** → *jam/clinch*: deny the opponent's commit-window (a debuff on their tempo/aggressor-selection at R4–R5).

*Bottom-up:* the defence-mode machinery + the bind + `apply_wound`'s initiative shift. *Top-down:* judo *jū* and BJJ leverage-yielding (F3/F4, with the Vol III "skill-advantage-required" flag), wrestling clinch (F6), fencing slip (F5). *Effect:* a yielding tradition becomes mechanically distinct from an opposing one along the morphology's most efficacy-faithful axis — directly retiring the J-33 traditions-F2 finding.

### I2 — Add a **targeting-logic** lever family on the HIT branch (closes G2)
The hit already branches into wound + armour-defeat + poise shift. Add a `target` selection biasing the hit's **effect-type** (not its raw probability):
- T1 mass → poise/balance-break emphasis (existing balance-break, weighted).
- T2 joints → a mobility/handling debuff (degrade the opponent's `balance`/handling next beats).
- **T4 choke** → an incapacitation clock that advances only in the clinch (R5) — the convergent-core mechanic, and the natural payoff for I1's F6 smother.
- **T5 base** → uproot (initiative + poise swing; the engine already computes balance-break — route here).
- **T6 defang** → weapon/limb-first: degrade the opponent's handling/reach *before* the body (the FMA signature the engine names but can't currently express).
- **T7 psychological** → composure-break: route *seme* / the freezing feint into the existing poise/composure track.
- T3 → **restricted to its `[M]` kernel** (chin/liver/throat = a damage/timing emphasis); **no death-touch, no hour-timing** (Vol III F6; the project's existing [B]/[L] discipline).

*Bottom-up:* `apply_wound` + the bilateral Ob + the poise/composure track. *Top-down:* the convergent core (T4/T5), FMA defanging (T6, with the honest caveat that FMA is itself an under-anchored tradition — see I4), *seme* (T7). *Effect:* traditions differentiate by *what they do to the opponent on a landed blow*, not just how often they land — the second efficacy-bearing axis the model omits.

### I3 — (OPTIONAL, low priority) **Power-source** as a strike-*profile* modifier, not a stat (addresses G3 *only if judged worth it*)
If — and only if — a *felt* distinction is wanted, add power-source as a bias on the hit's **shape** (never a new attribute): P4 dropped-momentum → higher single-hit magnitude, slower cadence; P3 elastic → faster cadence, lower per-hit (the "fa jin burst" the Chinese label already gestures at, made real); P1 leverage → armour-defeat emphasis. *Bottom-up:* the existing damage + cadence model. *Top-down:* the boxing drop-step (P4) and the stretch-shortening cycle (P3), at the Vol III §2 weightings. **Honest recommendation: defer unless the felt difference is demanded.** Vol III F9 warns this is exactly where taxonomic elaboration outruns the few variables that carry weight; an unneeded axis fails NERS-N and NERS-E. Flag the gap, ship I1/I2 first, add I3 only on evidence it's missed in play.

### I4 — Apply the four-axis standard as a tradition-**vetting checklist** (closes G4; no new mechanics)
Make every `TRADITIONS` entry pass, on entry: coherence + epistemic-grounding + **analogue-coherence (G5)** + (for combat-telos) efficacy-anchoring. Run it on the existing seven now:
- **`chinese`**: resolve the mode↔profile mismatch. Either re-label the `mode` to match the bind-and-measure weights, or re-weight toward a kinetic-rhythmic profile — **but `mode` is flavour, so the *direction* of the fix is Jordan's**; the finding (it currently says one thing and weights another) is mine to surface.
- **`filipino` / `chinese`**: reconcile the two files. Either anchor the channel profiles at S1/S2 (then abilities may follow), or **down-flag the channel profiles to match their no-abilities status** — apply the selection-effect to the *weights*, not only the abilities. (Note the armature's own caution that FMA is unanchored; I2's "T6 defang = FMA" example inherits that flag.)

### I5 — Name the aliveness position (closes G5; one paragraph)
Add to `ability_armature.md`: *D14/aliveness is handled as a sourcing constraint — the selection-effect rule (only pressure-tested, well-documented traditions earn abilities; flavour never carries efficacy) — not as an in-fight mechanic. A combat-telos tradition's mechanical strength is set deliberately and separately from its flavour.* This converts a silent omission into a stated, morphology-aligned design decision.

---

## §6 — The boundary I do not cross (layer discipline, explicit)

Per the PI project-owner contract, the following are **Jordan's creative/narrative/metaphysical layer** and are *not* designed here: the named-tradition roster; each tradition's flavour and its governing-analogue/`mode` *choice* (I4 surfaces the `chinese` inconsistency but the resolution direction is Jordan's); and the entire `[B]/[L]` metaphysical layer — energetic models E1–E7, "internal energy," and the death-touch as anything beyond its `[M]` kernel. The armature already defers roster/flavour correctly; this critique keeps that line.

**One flagged decision for Jordan (a metaphysics-layer seam, not Claude's to settle).** The morphology's central `[B]` case — a tradition that *claims* "internal power" — resolves, in the real world, to **real effects via mundane mechanisms** (relaxation reducing antagonist tension, kinetic-chain timing, trunk bracing, proprioceptive sensitivity — Vol III §2 P5). In Valoria those mundane mechanisms already have homes in the engine's `[M]` channels (`tactile`, `tempo`, `visual`). **But Valoria's metaphysics is not the real world** — Threads are constitutive ground, and a tradition's "internal power" *could* legitimately route to the actual Thread/Coherence layer (real in-world), not to inert flavour. So when a Valoria martial tradition invokes inner force, does it resolve to: (a) inert flavour; (b) the engine's mundane `[M]` channels (the morphology's real-world answer); or (c) the Thread metaphysics (a genuinely-real in-world power the real world lacks)? This is a canon-structure ruling on what a quantity *is* and *attaches to* — Jordan's design authority. Flagged, not decided.

---

## §7 — Honesty block

- `[CONFIDENCE: high]` on the factual corrections (§2) and the gap structure (§4) — both grounded first-hand in `tradition.py` + `ability_armature.md` at canonical HEAD, cross-checked against the morphology read in full. `[CONFIDENCE: medium]` on the *severity ordering* of the improvements (I1 > I2 > I4 > I5 > I3) — defensible from the morphology's efficacy weightings, but play-testing could re-rank; and on the `chinese` analogue-incoherence (G4), which assumes the `mode` labels are meant as governing-analogue claims rather than loose tags.
- **Inherited, not re-derived:** the engine's sim verdicts (the analysis's "mirror ~50%, fairness confirmed") and the morphology's per-atom efficacy weightings. Neither re-run; both cite their evidence.
- `[GAP: systems.py and config.py not read in full — the *tradition/ability surface* is fully grounded via tradition.py + ability_armature.md, but the exact wiring of the 7 channels into the resolution sigmas (and which channel sites remain pre-`eff_cw`) is taken from the armature's own status notes, not re-traced through systems.py. A follow-on could confirm the live-vs-pending channel count at the call sites.]`
- `[GAP: no sims run — these are design proposals, not validated balance changes; each I-item needs the armature's own §6 workflow (ground → define → wire → invariant-check → calibrate) before commit.]`
- **Project linkage:** §4's gap structure *is* the live J-33 / W4 #17 "traditions F2" item — this critique grounds and decomposes it along the morphology's dimensions; it does not invent a new problem.
- **Not committed.** This is a Jordan-vetoable proposal. If wanted in-repo, the natural home is `designs/audit/2026-06-25-combat-traditions-morphology/`, co-filed per the design-doc → `canonical_sources` rule, landed through `safe_commit` with a `Citations:` block (`tradition.py`, `ability_armature.md`, the five morphology uploads). Say the word and I'll bootstrap a commit pass; I have not done so unprompted.
