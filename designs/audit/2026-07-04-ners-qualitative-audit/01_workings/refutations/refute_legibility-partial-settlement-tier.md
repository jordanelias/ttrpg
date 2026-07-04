# Refutation notes — legibility-partial-settlement-tier

## Claim under test
"Two of the three dramatic-legibility questions (whose position is at risk; what each actor
wants) cannot be answered from ratified settlement-tier state alone — only the third (what
happens if no one acts) can." Cite: settlement_layer_v30 §3.2/§4.3/§4.5. Criterion Q-robust,
direction lateral, severity P2, novelty NEW.

## What is literally true (grounded)
- §4.5 Local Actors carry "one Conviction, Disposition" and **no ambition/goal field**. TRUE.
- §4.3 renders decay cleanly: Prosperity 0→famine, Order 0→revolt+governor expelled,
  Defense 0+hostile→siege. So "what happens if no one acts" is answerable. TRUE.

## Refutation 1 — NOVELTY is false (self-duplicate within this very audit)
`lens_playability_legibility.md` (same 2026-07-04 audit) DRAMATIC-LEGIBILITY WALK, "Domain
action (settlement governance)" bullet states verbatim: "only 'what happens if no one acts' is
cleanly answerable (Prosperity 0→famine, Order 0→revolt). Local Actors carry one Conviction but
**no ambition/goal field**, so 'what does each actor want' is unanswerable ... (settlement
dossier; governance_play_redesign, unratified)." Same evidence, same conclusion, same source
dossier. This candidate re-reports a sibling lane's finding as NEW. Novelty:NEW → refuted.

## Refutation 2 — the gap is already DIAGNOSED and a fix is DRAFTED (not novel, in-flight)
`designs/territory/governance_play_redesign_v1.md` (PROPOSAL, drafted 2026-06-22) exists
expressly to fix this: §Status "adds the event-deck and **NPC-ambition substrate** behind PART
4"; §3.1 adds `ambition:  # NEW — what they are actively trying to achieve` to every significant
NPC including Local Actors (§4.5); §3.2 the ambition engine makes "what does each actor want"
first-class and legible. The named missing field is precisely what the redesign adds. The
sibling refutation (refute_governance-redesign-orphaned) further shows its G1 prerequisite is
BUILT (`sim/territory/registry.py`, passing tests) and it carries a full goldenfurt_slice worked
example — an actively-developed, safeguarded provisional, not an accidental hole.

## Refutation 3 — the "whose position is at risk" half is answerable from settlement state
The finding lumps "whose position is at risk" into the unanswerable pair, but settlement-tier
state renders it:
- §4.3: Order 0 → "Governor expelled unless garrison present"; Defense 0 + adjacent hostile →
  mandatory siege scene. Governor tenure risk is legible off Order/Defense trend.
- §1.4.3 Capacity Pressure: at a full Seat, a claimant's Wing/standing is explicitly at risk
  (revert to Standing 5). §5.1: siege → Order decay → surrender identifies the controller at
  risk. Even the audit's own lens does NOT substantiate a failure of this question — it only
  substantiates the "what does each actor want" failure. So "two of three" overclaims; at most
  ONE question (actor wants) is thin, and even that is softened by the governor NPC priority
  tree (§3.2: "always prioritize Order ≥ 2, then Prosperity, then Defense") which makes the
  load-bearing actor's wants fully legible, and by Conviction functioning as a want-proxy
  (§4.5 "Player fulfills Conviction relevant to settlement: +1" — it drives scenes).

## Intent
DELIBERATE + safeguarded. §4.5 specifies Local Actors as "**lightweight** non-faction NPCs
representing the population" — the minimal Conviction+Disposition profile is an explicit design
choice, and the acknowledged-thin v30 governance loop already has a drafted successor
(governance_play_redesign_v1) gated by the ED-1094 merge-ratifies convention. Ledger grep: no ED
against this; governance hits (ED-682/723) unrelated. Not accidental; not deliberate-without-
safeguard → fails the CONFIRMED gate.

## Severity re-judge vs North Star
The true residual kernel (v30 Local-Actor want-legibility is thin) is real debt, but it is
in-flight redesign debt, not a P2 structural narrowing: the governor's wants are legible, risk
is legible, decay is legible, and the missing ambition axis is drafted. Materially this is P3
(friction/debt already being closed), not P2, and not NEW.

## Verdict: REFUTED
As framed — "two of three unanswerable, NEW, P2" — the claim does not hold: (1) not novel
(sibling lens carries it identically); (2) "whose position is at risk" IS answerable
(§4.3/§5.1/§1.4.3/§1.4.3); (3) deliberate-and-safeguarded (lightweight-by-design + drafted
governance_play_redesign). Reduced true kernel = KNOWN, P3, in-flight; no ED, tracked via the
redesign doc + the audit's own legibility lens.
