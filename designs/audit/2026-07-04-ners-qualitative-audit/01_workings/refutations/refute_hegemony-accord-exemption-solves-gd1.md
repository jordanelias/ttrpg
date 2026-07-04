# REFUTATION — hegemony-accord-exemption-solves-gd1

Role: adversarial skeptic. Verdict: **REFUTED**. Intent: **DELIBERATE (safeguarded)**.

## Claim restated
Treaty-hegemony dominates GD-1: qualifying treaties (a) make rival territory count toward the 15,
(b) exempt it from Accord≥2, (c) lower Turmoil — so "sign 3–4 treaties + hold one province" strictly
beats conquer-and-govern and makes the settlement/Accord/Govern game optional for victory. (Ω, P1.)

## Textual verification (the three legs are individually TRUE)
- Leg (a): `peninsular_strain_v30.md` §6.1 L425 "effective hegemony counts rival-held territories if
  Treaty-bound…". TRUE.
- Leg (b): §6.1 L432 "Territories held by Treaty-bound or Submitted factions do not need to meet
  Accord ≥ 2 for the hegemon — the legitimacy question belongs to the subordinate." TRUE.
- Leg (c): §4.2 L309 "Per active Treaty pair … −1 per pair, capped at −2/season." TRUE.

So the finder read the individual sentences correctly. The SYNTHESIS ("strictly beats / Govern
optional / dominance") is what fails.

## Why the dominance claim is REFUTED — four safeguards the finder missed

1. **Turmoil ≤ 6 is GLOBAL and counts ALL playable factions' low-Accord territories.** §4.1 L296:
   "per territory at Accord ≤ 1 controlled by ANY playable faction: +1." The §6.1 exemption removes
   only the hegemon's *win-check* Accord requirement over subordinate land — it does NOT stop that
   land from advancing global Strain/Turmoil. If treaty-bound rivals leave their territories
   ungoverned, Turmoil climbs and breaches the ≤6 gate. The Govern game is therefore **not optional
   — it is delegated** to the subordinate ("the legitimacy question belongs to the subordinate",
   L432). Either subordinates govern (a legitimate Pax victory — the peninsula IS well-governed) or
   Turmoil blocks the win. The finder's "makes Govern optional" is mechanically false.

2. **Treaty-decay cannot outrun instability.** §4.2 caps treaty decay at −2/season; §4.1 territory-
   instability advances up to +3/season (plus +2 faction-elim, +1/Revolt uncapped). The finder's own
   cite §4.2 L312 example nets *+1 Strain even with 3 treaty pairs* when land is ungoverned. Treaties
   budget Strain; they do not neutralise ungoverned ground.

3. **ED-791 is a SAFEGUARD, not support — the finder mis-cited it.** The ledger resolution (line 271)
   restricts qualifying treaties to genuine-subordination types: "only subordination-treaties create
   [effective sovereignty]." Capitulation requires the rival at **Stability ≤1 OR having lost ≥50% of
   territories** (`faction_layer_v30` §1.2 L105); Tributary/Institutional-domination (rival Mandate
   ≤1, hegemon ≥5) likewise require the rival already ground down. A qualifying treaty presupposes the
   rival has been *militarily or institutionally subjugated first* — the conquer/dominate game
   happened, it was merely closed diplomatically. "Sign 3–4 treaties" is not cheap; it is the
   *capstone* of subjugation. (Note: doc text §6.1 L430 currently over-lists Peace/Alliance as
   qualifying vs ED-791's narrower resolution — a real propagation-drift bug, but it CUTS AGAINST the
   finding and is a separate currency issue, arguably already tracked by ED-791.)

4. **Treaties are breachable and the hegemon's own province still needs Accord≥2.** Breach costs
   (Mandate −2, Stability −1, co-signatory Casus Belli; §1.2 L108) are survivable; a rival facing
   loss-by-hegemony has motive to breach across the required 2 consecutive Accountings. Hegemon's
   directly-held territory still needs Accord≥2 (§6.1 L423). The line is contestable, not solved.

## Intent
DELIBERATE. ED-306 deprecation (ledger line 7): "eliminate all rival factions **OR subjugate them
via diplomacy/treaties**; one universal condition." Diplomatic subjugation is an *explicitly
designed* first-class victory route. §4.2 frames treaty-binding as "the Roman Pax expressed
mechanically." This is the North Star working — a parallel avenue that WIDENS meaningful choice — with
the non-dominance clause protected by safeguards 1–3. Not an Ω violation; the opposite.

## Tracking
No decision-queue entry (`2026-07-01…/decision_queue.md`), no HANDOFF_FA lane, no ledger item calling
treaty-hegemony dominant. Not a duplicate. ED-791/ED-792 govern the qualification/Accord edges and
already encode the anti-gaming intent.

## Residual (the only survivable fragment — P3, iterate-not-reject)
IF subordinate factions are NPC-driven and the AI reliably self-governs to Accord≥2, a hegemon could
inherit a well-governed peninsula "for free." That is an AI-governance / balance-tuning concern
(Q-robust, not Ω), speculative without the sim, and applies to any route touching NPC land — not a
spec-level dominance defect. Does not overturn REFUTED.
