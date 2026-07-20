# Valoria — Combat System Holistic Review (logic & sequencing)
**2026-06-01 · review-before-tuning pass**

> Holistic logic/process review of the clean-slate combat system (state graph + defensive branch + derivations)
> before comprehensive tuning. Review discipline: **verdict first, severity-ranked, fixes applied.**
> `[SELF-AUTHORED — bias risk: reviewing my own session drafts; surfacing what an independent reviewer would flag]`
> `[CONFIDENCE: high — checked against the canonical state graph, ratified σ/ST1/A1/D1, m5/r9 channels, weapon_axes_v2]`

## VERDICT

**Structurally sound. No fundamental contradictions.** The bout nesting (fight→bout→engagement), the
attacker-initiates rule, the three defensive modes with distinct stat-compositions and degree ladders, the
continuous-reach negotiated measure, and the derived tempo/recovery/reach-cost are mutually consistent and
historically grounded. The defects are **sequencing and specification gaps** that would mis-resolve edge cases or
double-count — fixable in place. Seven findings, ranked. All fixed this pass.

---

## P1 — correctness of resolution (must fix)

**F1 · Bind entry was unconditional.** The procedure ran "clash (step 4) → bind sub-loop (step 5)" as if every
clash leads to a bind. Wrong: a **bind requires blades in material contact after the clash.** A dodge/void creates
no contact (no bind); a parry *may* leave blades crossed; a wind *is* the bind; a thrust-to-gap that lands creates
no bind. **Fix:** bind is a **conditional outcome** of a clash that leaves both weapons in contact with neither
winning outright — not a guaranteed next step. Dodge and clean hits skip it.

**F2 · Simultaneity was underspecified and implied the defender must "not defend."** The doc sourced double-hits
only from "attack vs attack, neither defends" — but the defender's inputs are defensive. Simultaneity actually
**emerges from two real cases:** (a) **non-absolute defence + simultaneous riposte** — a dodge that still grazes
("jumped back, got nicked") or a parry that leaks a graze, *while* the defender's counter also lands → both hit;
(b) **post-role-flip mutual attack** — after a riposte flips roles, both fighters are attacking and a tied tempo
lands both (the true *Doppelhau*). **Fix:** state both sources; remove "neither defends" as the sole path. No new
input needed — simultaneity is emergent from non-absolute defence (defensive_branch §4) + role-flip.

**F3 · Anticipation was double-counted.** Bout step 4b.2 ran an anticipation check, and the defensive-branch
procedure (§6.1) ran its own — the same Reading-vs-deception event, resolved twice. **Fix:** the defensive-branch
procedure is **invoked as the clash resolution**; anticipation runs **once**, inside it. The bout step references
it, does not duplicate it.

## P2 — cross-doc consistency (should fix)

**F4 · Tempo used the old banded reach-control.** The tempo step cited "reach-control (r9)" (the discrete
short/long band) after §6b made reach continuous and negotiated. **Fix:** tempo's reach term = **who controls the
current *effective* measure** (continuous `reach_base` ± choke/commit, derivation A), and the measure is **dynamic
within the engagement** — choke/commit can shift it beat-to-beat. The longer effective reach acts first / controls
distance *this beat*.

**F5 · Stance was one-sided; lifecycle unstated.** Only the defender's stance was modeled, but **both fighters
hold a stance** and the m5 **stance-counter applies attacker-stance vs defender-stance.** Lifecycle was also
missing. **Fix:** both fighters set stance at **approach** (from tradition repertoire); the stance-counter
resolves the pairing; stance **transitions during the engagement** (tradition-gated flow between guards) rather
than being frozen. Cadence: stance set per-bout at approach, transitions emergent.

**F6 · Initiating into a longer reach was free.** Attacker-initiates, but if the attacker's effective reach is
shorter, they must **traverse the opponent's measure** to engage — historically the polearm/rapier advantage
(closing "under the point"). This cost was implicit. **Fix:** initiating against a **longer effective reach**
grants the longer weapon a **first-contact advantage** (a free defensive beat / stop-thrust opportunity as the
attacker crosses the measure). The short weapon's game is forcing past it to the close measure where the long
weapon must choke up (losing reach/leverage).

## P3 — accounting (clarify)

**F7 · Per-beat stamina vs variable beat-count.** Stamina drains **per action (beat)**, and the number of beats
per bout is now **variable** (per-weapon tempo + soft cap), replacing the session's fixed `PHRASE_SUBACTIONS`.
This must balance: a **light-fast flurry** = many cheap beats; a **heavy-committed** sequence = few costly beats.
**Fix:** action stamina cost scales with **weight × commit-depth** (heavy/deep blows cost more per beat, light
recovers cost less), so the *totals* over a bout are comparable and neither weapon class trivially out-gasses the
other. Cross-checked: tempo (derivation B) × per-beat cost (derivation D) → bout-level drain.

## Also applied
**Choke→bind bonus (Jordan-approved, manual-true):** choking up shortens effective reach **and grants a bind
leverage bonus** (half-swording). Added to derivation D (choke) and the bind contest (ST1): `bind_sigma +=
CHOKE_BIND_K · choke_amount`.

---

## Cadence (the corrected per-bout / per-beat split)
- **Per BOUT, at approach:** attacker → approach + commit-distance; **both** → stance.
- **Per BEAT, in engagement:** current aggressor → technique + commit-depth; current defender → intended defence
  (parry/dodge/bind). Stance transitions emerge. Role may **flip on a riposte** (and may flip **multiple times** —
  the conversation of the blade — bounded by soft tempo cap + stamina + the 6–10 s ceiling).

## NERS-E check (held)
Live input stays minimal — attacker: approach + technique (+ commit-distance, commit-depth); defender: stance +
intended defence. Engine resolves the rest. The fixes **clarify resolution**; they add **no new player choices and
no new subsystems**. Elegance preserved.

## Result
All seven applied to `full_bout_procedure` and `combat_derivations`. The system is now logically closed and ready
for coefficient tuning against a harness rebuilt to this graph.
