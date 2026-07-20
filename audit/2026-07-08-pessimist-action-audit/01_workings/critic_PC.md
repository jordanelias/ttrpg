# PC Lane — Inverted Critic Pass (Sonnet, read-only, adversarial-in-the-saving-direction)

Method: for each condemned action (verdict != KEEP) I built the strongest honest case for keeping it
as originally specified, then tested that case against the actual prose (`combat_v30.md`), the
ratified continuous-resolver decisions (`combat_engine_v1/`), and canonical throughline criteria.
Two KEEPs were spot-checked for over-generosity. Cardinal-rule check: verified no verdict below rests
on build-state (stub/unwired/unported) as its reason — all condemnations cite ratified *design*
decisions (WS-5, contact-axis I7b/D8-D9) or textual/structural facts about the prose itself, never
port status. `build_state_note` fields are used correctly as routing metadata only.

---

### Strike — KEEP (spot-check only)
No steelman needed; verdict not condemned. Spot-check: irreducible core, nothing to attack. **Sound.**

### Leap (§10.1 Thread action) — KEEP (spot-check only)
Spot-checked the cost claim against `combat_v30.md:434` — "Practitioner commits all pool to Defence
during Leap. ~60% hit probability... Real tactical cost." Confirms Ω-d is genuinely paid, not asserted.
Gating (practitioner-only) is real, not a loophole to full-cast dominance. **No over-generosity found.**

---

### Feint — DISTILL
**Steelman attempted:** the discrete round-based PC menu has no continuous "commit dial" exposed to
the player the way `combat_engine_v1` does — maybe Feint is the *only* way a discrete-turn player can
express "cheap, low-commitment probe that trades this round's offence for future tempo," and folding
it into "Strike's low-commit pool-split" quietly deletes that lever rather than relabeling it.
**Why it fails:** `wrapper.py:140` names the mechanism explicitly — *"a feint (commit~2, full
recovery) costs no tempo"* — i.e. the canonical engine's own authors call shallow-commit "a feint," and
`engagement_psychology_recovered.md` §A states the read/deception contest is *already* carried by every
attack's legibility+commit terms, confirmed as a **ratified** combat-armature decision (2026-05-29/30,
WS-5), not a speculative comparison. The dossier's proposed remedy (fold into Strike's own low-commit
split) is exactly the mechanism the ratified design already uses — it isn't inventing an external
comparator, it's applying the corpus's own already-decided answer to this exact possibility space.
The `build_state_note`'s pre-emptive rebuttal ("presented as design precedent, not as catch-up
scheduling") holds up under inspection.
**critic_outcome: UPHELD.**

### Establish Distance — MERGE (with Escape)
**Steelman attempted:** the two-zone model (Melee/Ranged, `combat_v30.md:204-206`) might still support
a real distinction — Establish Distance as a *partial* reposition within an ongoing engagement vs.
Escape as *fully leaving* the encounter/zone — a scope difference merging would erase.
**Why it fails:** the prose gives that distinction zero textual support. Both actions are defined
identically ("Agility contest vs opponent") with no differing resolution procedure, no stated zone-exit
semantics for Escape beyond "requires not being Tied Up," and the prose's own resolution-order table
co-schedules them at **Priority 4** as one kind of thing. Any partial/full distinction would be an
invented intent, not a specified one — which is itself evidence for the Q-elegant/Duplicate-Coverage
finding, not against it. The proposed remedy (one contest, Degree Table sets magnitude) is a plausible,
even more physically honest read (distance outcomes are inherently graded, not player-dialed).
**critic_outcome: UPHELD.**

### Take a Breath — REFINE
**Steelman attempted:** maybe the "mutual indefinite rest" scenario isn't really a defect of Take a
Breath — two wary combatants declining to close is a realistic outcome, and a GM-less engine could
resolve it generically via a scene-level timeout/objective-clock (already-existing machinery like
Fieldwork Transitions / scene-end triggers) rather than needing a fix inside Take a Breath's own text.
**Where it partially lands:** I agree the *fix*, if built, likely belongs at the encounter/scene-pacing
layer, not as a rewrite of Take a Breath's own clause — the action's cost/benefit is genuinely sound
in isolation. But the underlying observation stands regardless of which rule ends up carrying the
fix: nothing in the corpus as read currently forces resolution of a mutual-recovery standoff, which is
precisely the named Failure Lexicon shape (Ω-c/Μ-α, Rest state) the dossier cites. The finding is real;
only its "address point" might be one layer up from where the dossier locates it.
**critic_outcome: UPHELD** (note for the docket: consider re-homing the fix to scene/encounter-pacing
rather than Take a Breath's own rule-block; does not change the verdict).

### Full Guard — DISTILL (with Dodge)
**Steelman attempted:** `character_histories_v30.md:313` keys a Templar talent ("Shield of Faith,"
+1D Defence) specifically off the *named* Full Guard state — dissolving the standalone action into a
generic 0-Offence pool-split could silently orphan that talent's trigger condition.
**Why it fails to save the action:** the talent's trigger is trivially portable — it needs only a
state check ("0 dice allocated to Offence this round"), not a standalone menu row; migrating the
talent's reference costs a find-replace, not a redesign. This is a real but minor implementation note,
not a reason to keep Full Guard as an independent action. The empirical-value point (ED-834/835/838
action triangle) is already correctly preserved in the verdict's own framing (choice survives,
packaging doesn't).
**critic_outcome: UPHELD** (minor caveat noted: flag the Templar-talent state-reference migration as a
one-line dependency in any acted-on distillation, not a blocker).

### Disarm — MERGE (into Grapple/Control, with Tie Up)
**Steelman attempted:** Disarm's outcome (weapon drop) is qualitatively different in kind from Tie
Up's (mobility/pool debuff) — collapsing them into one branching roll might blur two distinct player
intents ("I want them weaponless" vs. "I want them immobilized").
**Why it fails:** `state_graph.py:97-98` documents the **Contact node** as an already-BUILT (I7b, D8/D9
— ratified, not proposed) "flat branching menu (disarm/throw/pin/control/foot_pin/escape)" off one
contested roll — this is precisely "declare intent, branch on outcome," which preserves the distinct
player intents the steelman worries about losing; it just removes the redundant *per-technique*
separate-roll scaffolding. The precedent is a ratified engine decision, not a build-state fact (the
verdict correctly does not depend on `combat.grapple`'s PENDING port status, per its own
build_state_note).
**critic_outcome: UPHELD.**

### Retrieve — MERGE (dependent clause of Disarm)
**Steelman attempted:** if some other rule elsewhere in the corpus (fumbles, called shots, chain-dice
botches) can also drop a weapon, Retrieve would be a general-purpose action, not merely Disarm's
appendage, and folding it in would lose that generality.
**Why it fails:** a corpus grep for "drop"/"dropped" in `combat_v30.md` turns up exactly one trigger —
Disarm (line 100) — and Retrieve (line 101) has no other textual entry point. As specified, it is
genuinely a dependent clause with no standalone decision beyond "attempt yes/no," which the merge
preserves as a branch of the outcome.
**critic_outcome: UPHELD.**

### Tie Up — MERGE (into Grapple/Control, with Disarm)
**Steelman attempted:** same as Disarm's — different named debuff, arguably different tactical
niche (denies escape vs. denies weapon).
**Why it fails:** identical structural template (Close range + single Offence roll + binary debuff),
same ratified Contact-axis precedent as Disarm. Notably, the code's contact-axis menu explicitly
separates a *general* "escape" branch (breaking a bind/grapple) from the *standalone* Escape action
(disengage from an unconstrained opponent) — meaning the dossier's clustering (Tie Up merges with
Disarm; Escape merges with Establish Distance, not with Tie Up) is precisely scoped to the code's own
distinction, which is a point of confidence in the analysis, not a gap in it.
**critic_outcome: UPHELD.**

### Escape — MERGE (with Establish Distance)
See Establish Distance above (shared reasoning, same evidence).
**critic_outcome: UPHELD.**

### Rescue — REFINE
**Steelman attempted:** maybe all 8 sub-clauses are individually load-bearing (each closes a genuine
edge case — eligibility gate, contest formula, payoff, chain-block, incapacitation carve-out) and the
finding is really "no fix needed, this is irreducible complexity for a mechanic this rich."
**Why it partially fails:** the eligibility gate (prevents Rescue from being a universal always-on
defensive action — an Ω-d dominance guard) and the core contest are load-bearing and likely
irreducible. But the chain-block and incapacitation-carve-out read as reactive patches to specific
observed edge cases (6 separate PP numbers spanning 214→407) rather than falling out of one clean
template — consistent with Q-elegant genuinely failing on the *current text*, not the *concept*. I
could not construct a one-read restatement of the rule as written. The dossier's own framing (load-
bearing concept, consolidate the accreted patches, don't cut) is the correct disposition — not lenient
enough to overturn, not harsh enough to escalate to PRUNE (removing it would leave the Fibonacci
group-combat bonus unanswered, a live Ω-d problem elsewhere in the system).
**critic_outcome: UPHELD.**

### Dodge — MERGE (into Full Guard)
**Steelman attempted:** Dodge is reactive/trigger-timed against one specific incoming ranged attack;
maybe that's meaningfully different from Full Guard's whole-round declared stance.
**Why it fails:** the ACTIONS table itself (`combat_v30.md:88`) classifies **both** Full Guard and
Dodge under the same "Reactive... trigger-timed" row — the prose's own taxonomy already treats them as
the same kind of thing, differing only by target-restriction (ranged-only), which existing TN/DR rules
(line 206, armour-DR) already carry without a second named action.
**critic_outcome: UPHELD.**

### Stunt — REFINE
**Steelman attempted:** maybe "Game Master sets N" is meant as an *author-time* tag (like the B-mode
flag at line 376-378, which is explicitly "Game-Master/scenario writer sets B_MODE=TRUE... engine reads
the flag" — compatible with no runtime GM), not a live arbitration call, in which case there's no real
conflict with the no-GM premise and REFINE is unnecessary.
**Why it fails:** unlike B-mode (one flag, fixed at encounter authoring for the whole scene), Stunt's N
is keyed to whatever specific, unbounded narrative maneuver the *player* improvises in the moment
("I swing on the chandelier," "I kick sand in his eyes") — an open space no author-time tag can
pre-enumerate. This is a genuine, structural gap for a GM-less runtime, not a wording ambiguity.
**Verification of the dossier's evidence:** confirmed `ED-1061` did ratify exactly this fix pattern
(context-derived, deterministic, tie-broken) for an analogous "GM-picks" defect in the Guilds faction
boost (social contest); confirmed `combat_v30.md` still carries **three more** live "Game Master"
references at lines 242, 250, 378 beyond Stunt, and a corpus-wide grep turns up **126** remaining
"Game Master" hits outside deprecated/archive paths — so ED-765/768's sweep demonstrably did not reach
everything, supporting "this is missed residue, not new territory." Notably, line 372 already shows a
**working deterministic pattern in the same document** — a fixed-geometry, enumerable Stunt vocabulary
(ranks-shift/choke-point-hold/line-collapse) — meaning the REFINE fix (replace "GM sets N" with an
author-tagged enumerable menu, generalized beyond the B-mode case) is not speculative; a working
instance of it already exists a few dozen lines away.
**critic_outcome: UPHELD** (strengthened: cite `combat_v30.md:372`'s fixed-geometry Stunt vocabulary as
existing proof-of-pattern for the deterministic replacement, alongside ED-1061).

---

## Summary
13 rows reviewed (2 KEEP spot-checked, 11 condemned rows steelmanned). **All 11 condemnations
survive as UPHELD** — no overturns, no downgrades. Two rows (Take a Breath, Stunt) carry added
evidentiary support strengthening the original finding; one row (Full Guard) carries a minor
non-blocking implementation caveat (Templar-talent state reference). No verdict was found to rest on
build-state reasoning; all cite ratified design decisions or the prose's own textual structure.

