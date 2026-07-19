# Faction min-max hunt — arena: faction_minmax

Role: adversarial munchkin. Working tree @ audit charter. Cites are file §section.

## GD-1 victory recap (the target)
`victory_v30.md §0` + `peninsular_strain_v30.md §6` (mirrored):
All 15 territories (direct OR **effective hegemony**) · Accord ≥ 2 **in all *directly-controlled***
· Turmoil(Strain) ≤ 6 · held 2 consecutive Accountings. (Brief's "Stability≤6" = the global
Turmoil/Strain track, `victory §0.3`.)

**Effective hegemony** (`victory §0` / `strain §6`, lines 427–432): a rival-held territory counts
for you if the rival is Treaty-bound (Crown Treaty OR Peace/Alliance/Capitulation/Tributary —
ED-791), Submitted (Stability 0), or institutionally dominated (rival Mandate ≤ 1 AND hegemon
Mandate ≥ 5). And the load-bearing line, `strain_v30 §6` L432: **"Territories held by Treaty-bound
or Submitted factions do not need to meet Accord ≥ 2 for the hegemon — the legitimacy question
belongs to the subordinate."**

---

## LINE 1 (P1) — Treaty-hegemony solve: one instrument satisfies all three victory clauses
Play: as Crown (or anyone with a qualifying treaty), sign a qualifying Treaty
(Crown Treaty / Peace / Alliance / Capitulation / Tributary) with each of the other 3 factions.
Hold ONLY your starting province directly, at Accord ≥ 2. Win.

Why it dominates — one instrument, three clauses:
- **Territory count:** treaty-bound rival territories count toward the 15 (`strain §6` L351, L432;
  "counted as Crown-controlled for sovereignty purposes").
- **Accord ≥ 2:** *exempted* for treaty-held territory (`strain §6` L432). The Accord-governance
  burden the design deliberately hardened (Church ED-585/590 forced Accord≥3 governance) is
  **skipped for up to 14 of 15 territories.**
- **Turmoil ≤ 6:** the *same treaties* drive Strain DOWN — `strain §4.2`: −1 on Crown-Treaty
  formation (max 1/season) + −1 per active Treaty pair capped −2/season. Meanwhile the conquest
  alternative fights Strain the whole way (battles → MS−1 `victory §0.4`; Accord≤1 held territory
  → Strain +1/ea `§4.1`; faction elimination → +2 `§4.1`).

So the governance-heavy "conquer + cultivate Accord across 15 territories" path is **strictly
dominated** by "sign 3–4 qualifying treaties + hold one province": less Turmoil, no Accord burden,
no MS loss. Non-dominance (Ω-d) says *no* strategy should dominate; this one does.

Retune-survival: the specific ≤1/≥5 numbers are tuning, but the **structural exemption** (treaty/
submitted territory skips Accord≥2) survives any retune → **P1 structural**. Choice tree that
collapses: the entire settlement/Accord/Govern cultivation game (densest interdependency edge,
grounding-map §a1) becomes optional for victory.

Friction (honest): treaties need consent — Crown Treaty NPC consent = Mandate≥3 AND Stability≤3
(`victory §3.1`); Capitulation/Tributary need military subjugation. So it's not free vs a
refusing human. But whenever a qualifying treaty is *obtainable*, it dominates conquest. And the
AI-consent rule means destabilizing a rival (Stability≤3) while Mandate≥3 auto-yields consent.
Confidence: high.

## LINE 2 (P2) — Domain Echo / Debate Mandate-farming feeds the institutional-domination route
`scale_transitions_v30 §5.1`: cap is **one Domain Echo per *scene* per faction** — NOT per season.
`§5.2`: OW = ±2, Success = ±1 to most relevant faction stat. `§5.4` Debate: Track ≥7 → winner
+1 Mandate, loser −1 Mandate. Nothing in §5 caps the *number of qualifying scenes per season*.
`§5.3` claims seasonal-accounting timing "prevents real-time manipulation" — but that fixes timing,
not COUNT. The cap is on the wrong axis.

Play: run N Debate scenes/season → farm your Mandate up and a target rival's Mandate down
simultaneously — exactly the two quantities the Line-1 "institutionally dominated" clause reads
(hegemon ≥5, rival ≤1). The mean-reverting Mandate→L/PS stabilizer (`settlement §1.8`, +1 L/season
to below-Mandate settlements) pulls a suppressed rival back up at ~+1/season; ≥1 debate/season
against that rival outruns it. Personal-scale scene spam thus drives a *strategic* victory clause.

Bound/uncertainty: whether this is a true break depends on a **per-season Zoom-In / scene budget**
I could not find (Sufficient Scope §7 gates *eligibility*, not *count*). If the scene slate hard-
caps Zoom-Ins/season, farming is bounded → drops toward P3. As written, no such cap → P2.
Accord-Echo farming (`§5.5`) is already damped: Echo-vs-Govern deconflict + ±1/Zoom-In means
≤+1 Accord/territory/season. Mandate-Echo is NOT damped. Confidence: medium.

## LINE 3 (P3) — Mandate saturation decouples institutional power from breadth of holdings
`settlement §1.8`: Mandate = clamp(round(7T/(T+6))), T size-weighted; "one province of large,
developed settlements has a higher Mandate than many provinces of tiny settlements"; sim: Church
Himmelenger alone = Mandate 5. So Mandate ≥ 5 (hegemon side of Line-1 domination clause AND
Parliament votes `faction_layer §5.3`) is a cheap early target reachable by developing ONE
metropolis province; further territory barely moves it (saturation). This is largely **intended**
and N-grounded ("one metropolis outweighs several hamlets", CK3/EU4/Vicky anchors) — so P3, not a
structural flatten. It's the *enabler* that makes Line 1's hegemon-Mandate≥5 nearly free. Flag,
don't reject (N tier, Jordan-owned). Confidence: high (that it's cheap), high (that it's intended).

## LINE 4 (P2) — Insurgency pipeline (GD-3) suppressible by rote Enforce
`victory §3.5` (Presence suppression): Crown Enforce = Military vs **Ob 2**, Success −1 marker;
Church Preach = Influence vs Ob = markers, Success −1. RM spread = +1 adjacent/season only when RM
Stability≥3; marker cap 5. An incumbent can strip −1 marker/season at trivial Ob 2, indefinitely,
choking the "build your own faction from nothing" emergence promise (`victory §3`, GD-3
Revolt→Insurgency→Faction). Damper (real): Enforce costs Order −1 in the settlement each time →
Order feeds Accord down (`settlement §1.3`) → threatens the incumbent's own Accord≥2. Cell
Resilience +1 Ob at 3+ settlements. So there IS a designed self-cost; the open question is whether
AI/player finds rote Enforce always worth the Order trade. Structural framing but heavily tuning-
dependent (Ob 2, Order−1 magnitudes) → P2 with a self-correcting damper noted. Relates to KNOWN
ci_political orphan (charter calibration: zero Key integration) but the *suppression economics* is
a distinct, untracked concern. Confidence: medium.

## Non-findings / checked-clean
- **Assert/Suppress spam (CI, `victory §7`):** Assert Ob 2 CI+1 / Suppress negates only the +1
  passive (not Piety Yield); Suppress Ob = floor(ChurchMandate/2)+1 escalates as Church grows. This
  is the *intended* CI clock (peaks mid-game), not a flatten. P3-none. Structurally sound.
- **Partition / co-victory paths:** mostly [SUPERSEDED-BY GD-1] in `victory §0.1/§3/§4` — dead for
  currency; not live exploit surface.
