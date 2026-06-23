# Goldenfurt — Event Deck (starter, 28 cards)

**Slice:** S-006 Goldenfurt. **Engine:** pressure-driven, stateful (`governance_play_redesign_v1.md §2`). Each season the deck draws `1 + ⌊Π/3⌋` cards by trigger-predicate + weight, then chains via `seeds`.
**Card ids:** Petition `G1xx` · Friction `G2xx` · Opportunity `G3xx` · Crisis `G4xx` · Intrigue `G5xx` · Ambition `G60x` (one per NPC) · Thread `G7xx`.
**Churn rule enforced:** every card has ≥1 response that emits a `Π` delta, and every player-action response writes ≥1 Ledger tag — no card can leave the player unable to change the world.

## Coverage

| Family | Cards | Count |
|--------|-------|-------|
| Petition | G101 G102 G103 | 3 |
| Friction (Directive-bearing) | G201 G202 G203 G204 G205 | 5 |
| Opportunity | G301 G302 G303 | 3 |
| Crisis | G401 G402 G403 G404 | 4 |
| Intrigue | G501 G502 G503 G504 G505 | 5 |
| Ambition (NPC-firing) | G601 G602 G603 G604 G605 G606 | 6 |
| Thread | G701 G702 | 2 |
| **Total** | | **28** |

---

## Spine cards (full schema)

### EVT-G101 — "Only Sons" · Petition
- **triggers:** `directive == Extract` (active war-levy) AND `Order <= 3`
- **weight:** base 3, +1 per `Grudge:*` tag · **cooldown:** 2 · **npc_refs:** G01, LA-G01
- **the_ask:** "Mertha's only son was taken in the levy. The Magistrate petitions for his release — the law, she says, never meant to empty a widow's house." · *pressure_if_ignored:* +2
- **responses:**
  - `Hold Court` (1 AP, Charisma+Gov-history vs Ob 2) → rule for Mertha: Hedda.Disp +1, Garrison.Disp −1, **Ledger** `Precedent:only-sons-exempt`, **Π −2**
  - `Comply with the levy` (0 AP) → PS −1, Hedda.Disp −2, **Grudge:Hedda**, **Π +1**, *seeds* `G501` (son radicalizes)
  - `Bargain` (social contest vs Crown) → partial: take the son but grant a stipend; mild suspicion +1
  - *ignore* → **Π +2**, **Ledger** `Reputation:Weak`, **Grudge:Mertha**

### EVT-G201 — "The War-Levy" · Friction (Directive: Extract)
- **triggers:** `season_directive == Extract` (Crown at war or mustering)
- **weight:** mandatory when directive fires · **npc_refs:** G06, G01
- **the_ask:** "Bailiff Ems delivers the Crown's writ: forty men and a tenth of the grain, by season's end." · *pressure_if_ignored:* +3 (you cannot ignore a Directive — only respond)
- **responses:** *(verify fix deck-F1/CG-6 — Π deltas added; the card now satisfies the deck's own ≥1-Π-delta invariant and offers a release valve)*
  - `Comply` → Crown Standing +1, Konrad.Disp +1, PS −1 & Order −1, **Π −1** (the levy reads as legitimate order), *seeds* `G101`
  - `Bargain` (social contest vs Crown, you as petitioner §7) → soften to half-levy on success; Konrad.Disp −1; **no suspicion** (that is Bargain's whole point vs Defy); **Π −1** on success
  - `Defy / Divert` → **suspicion +1**, PS +1, Hedda.Disp +1, **Π +1**, Konrad **logs it → +1 progress on G606**, **Ledger** `Reputation:Just`; settlement left under-defended (*seeds* `G404` if hostiles in province)
- **notes:** the vise — comply and you starve the town that `G103` is begging you to feed; defy and `G606` creeps toward your recall.

### EVT-G204 — "The Curate's Offer" · Friction (the Geneva trap)
- **triggers:** `Order <= 2` AND `religious_building == Chapel`
- **weight:** base 2, +1 if `Wessel.advance >= 2` · **cooldown:** 3 · **npc_refs:** G03
- **the_ask:** "Wessel offers the parish's hands — almonry, schooling, dispute-mediation — to steady the town. It would lift Order at a stroke. It would also make the Church the thing holding Goldenfurt together."
- **responses:**
  - `Keep Order: Clergy` (1 AP) → Order +1 and Order-decay −1 (§1.6), **but** Church-infra creep: **Wessel +1 progress on G603**, **Ledger** `Debt:church-dependence`
  - `Decline` → Order stays low, Wessel.Disp −1, **Π +1**
  - `Bargain` → limited parish (Order +1 once, no decay bonus, no creep); Wessel.Disp −1

### EVT-G401 — "Conscription Riot" · Crisis
- **triggers:** `Π >= 8` AND (`Grudge:Hedda` OR `Grudge:Mertha`) AND recent force/levy action
- **weight:** base 5 (escalation) · **npc_refs:** G01, LA-G01
- **the_ask:** "The square fills. The widow's grief has become a crowd."
- **responses:**
  - `Keep Order: Force` (2 AP, Military) → Order +1 but PS −2, LocalActors.Disp −1, **Ledger** `Grudge:town`, *seeds* `G502` (Orsk exploits) + `G403` (black market)
  - `Concede` (rescind the levy) → Crown Standing −1, suspicion +1, **Π −3**, Hedda.Disp +1
  - `Hedda mediates` (only if `Hedda.Disp >= +2`) → **Π −3** at no Order cost; **Ledger** `Debt:owed-to-Hedda`

### EVT-G502 — "Orsk's Whisper" · Intrigue
- **triggers:** `Orsk.Disp <= -2` OR ruled against Orsk in a `Hold Court`
- **weight:** base 3 · **cooldown:** 3 · **npc_refs:** G02, G06
- **the_ask:** "Word reaches you that the Grainmaster has been buying the Bailiff's ear — painting you as a governor who can't keep order."
- **responses:**
  - `Investigate` (1–2 AP, Cognition vs concealment) → uncover **Konrad takes Orsk's coin**: gain `Leverage:konrad-corrupt` (you can now blackmail/neutralize the suspicion eyes); Orsk.Disp −1
  - `Confront Orsk` (social contest) → on win, Orsk backs off (Guild Influence −1); on loss, **Konrad +1 progress on G606**
  - `Concede the charter` → Orsk.Disp +2, **Orsk +1 progress on G602**, Guild Influence +1

### EVT-G505 — "The Magistrate's Brother" · Intrigue (the keystone)
- **triggers:** (`Leverage:konrad-corrupt` OR `Wessel.informer-active`) AND `Investigated(Tomas)` has occurred
- **weight:** base 4 · **excludes:** fires once · **npc_refs:** G01, G04, G06, G03
- **the_ask:** "You hold the thread now: proof the Magistrate has long shielded her smuggler brother. Pull it, and the most principled person in Goldenfurt is in your hand."
- **responses:**
  - `Bury it (warn Hedda)` → Hedda.Disp +3, **Ledger** `Debt:hedda-owes-you` (she becomes a willing proxy — clean); her G601 bid now carries your banner
  - `Bury it (hold it)` → **Ledger** `Leverage:hedda-compromised` (she's your proxy, but coerced — β-Hedda's effectiveness/Conviction-standing erodes each season held)
  - `Expose` → Hedda ruined, the grain-court collapses (`Precedent:*` rulings void), **Ledger** `Reputation:Harsh`, **Π +3**, Tomas → vendetta (*seeds* `G504`)

### EVT-G601 — "Hedda's Bid" · Ambition (fires when G01 progress ≥ 4)
- **the_ask:** "The Magistrate stands for the Kronmark seat."
- **resolution by relationship:**
  - allied/owes you (`Debt:hedda-owes-you`) → she wins as **your parliamentary proxy** → +1 your faction-emergence Stage-2→3 progress; Crown notes your growing local power (Konrad +1 on G606)
  - estranged (`Grudge:Hedda`) → she wins on an **anti-you reform platform** → future Directives you issue cost +1 Ob locally; Crown displeased with your instability
  - compromised (`Leverage:hedda-compromised`) → she wins but is yours-on-a-leash; one exposure event later can detonate (`G505` re-arm)

### EVT-G606 — "The Bailiff's Report" · Ambition (fires when G06 progress ≥ 4)
- **the_ask:** "Bailiff Ems has filed."
- **resolution by state:**
  - if `Leverage:konrad-corrupt` held → the report is **buried**; Konrad is yours (Debt:harbor-corrupt-agent); suspicion resets
  - else if `PS >= 5` and `Hedda allied` → the recall attempt **backfires into your faction-emergence** (Stage 2→3): the town backs you over the Crown
  - else → **Recall scene** (social contest to keep your post; lose → replaced, the slice ends for this PC, the settlement keeps your Ledger for your successor)

---

## Remaining cards (compact)

| id · family | trigger | the ask → key branches (churn) |
|---|---|---|
| **G102** Petition | Guild foothold, Prosperity ≥3 | Brun vs the Guild toll. Court-for-Brun (`Precedent:toll-capped`, Orsk−) / for-Orsk (Guild Inf+, seeds G502) / Treat (chit). |
| **G103** Petition | Prosperity dropped OR Orsk hoarding flag; Order ≤2 | Aldith begs relief. Sponsor (Treasury−, PS+, Order+) / Develop-via-Guild (Orsk+) / ignore (Π+2, seeds G402). |
| **G202** Friction (Tax) | `directive==Tax`, autumn | Harvest tithe. Comply (Crown L+, PS−) / Defy (PS+, suspicion+1) / Bargain. Collides with G103. |
| **G203** Friction (Suppress) | RM foothold + Church Attention rising | "Shut the circle." Force (Order+ short, Greta deeper, PS−, advances G605) / Shelter (Greta+, Wessel denounces→suspicion+1, advances G603) / token. |
| **G205** Friction (Host) | `directive==Host`, FacilityTier ≥1 | Quarter a Hafenmark envoy in your one Wing → capacity pressure (§1.4): bump your inner circle (Crown+) or Defy (suspicion+1). |
| **G301** Opportunity | Order ≥4 AND Prosperity ≥4; Π low | Harvest fair. Sponsor (Treasury−, +1 Disp all locals, `Reputation:Generous`) / attend / skip (LA grudge). |
| **G302** Opportunity | Defense ≥2 OR militia raised; Order ≥3 | A loyal sergeant seeks service → recruit (faction-emergence knot, §6.2) / decline. |
| **G303** Opportunity | `Hedda.Disp >= +2` | Hedda offers alliance → ally (Stage 2→3 progress, but Crown break → Konrad+) / decline (Hedda−1). *(the worked-example payoff)* |
| **G402** Crisis | Prosperity 0 OR G103 ignored ×2 | Famine (auto Order−1). Sponsor relief (Treasury−−) / beg Crown (Debt) / let Orsk "relieve" (advances G602 — he profits off the hunger). |
| **G403** Crisis | Order ≤1 for 2+ seasons | Black market entrenches (§4.7: Wealth+0.5, Accord−0.5). Investigate→crack down (Tomas surfaces, may arm G505) / tolerate (advances G604, Crown notices). |
| **G404** Crisis | Defense ≤1 + hostile military in province | Raid at the ford (mandatory scene). Militia defend (PS+, Defense check) / emergency Fortify / abandon (Prosperity−−, `Reputation:Weak`). Often the cost of defying G201. |
| **G501** Intrigue | seeded by G101-comply | The widow's son returns embittered → RM recruit (Greta, advances G605) or rioter (seeds G401). Counsel (defuse, Conviction-fulfill) / ignore. |
| **G503** Intrigue | `Wessel.Disp <= -1` OR sheltered RM | Wessel's letter to the Inquisitor (Church Attention/suspicion+). Investigate→expose him as informer (leverage) / appease (concede G603) / ride it out (suspicion+1). |
| **G504** Intrigue | Tomas discovered and not expelled | Niflhel calls a favour through Tomas. Comply covert (Niflhel chit, exposure risk) / refuse (Tomas−, may implicate Hedda) / turn him in (Hedda secret blown → G505). |
| **G602** Ambition | Orsk progress ≥3 | Charter gambit / engineered shortage. If checked → fails, Guild Inf−; else → perpetual toll charter (ford revenue privatized, future Develop +1 Ob). |
| **G603** Ambition | Wessel progress ≥4 | Chapel→Church. Geneva trap closes: durable Order/Stability, but Church infra = −2 seizure vector and Wessel is moral authority (removal needs Mass Battle / Mandate Challenge). |
| **G604** Ambition | Tomas progress ≥3 | The river economy becomes load-bearing — Tomas/Niflhel co-govern the dock. Wealth↑, Crown legitimacy↓, you're entangled with Niflhel. |
| **G605** Ambition | Greta progress ≥5 | RM hits 3-settlement cell resilience; a public Einhir rite. PS surges in hamlets, Church Attention spikes, Crown may issue a harsher Suppress Directive. |
| **G701** Thread | RM rite performed (G605 path) OR RS bleed at the circle | "The stone circle stirs." Thread op at the circle (§4.4): Weaving→Order+1 / Dissolution→Defense−1 & Order−1. Ties Greta to the Thread layer. |
| **G702** Thread | Thread Proximity ≤2 | "The forgotten field" — crops grow wrong, time slips. Investigate→harvest residue (Wealth+1, RS−0.5, §4.9) / Mend (Prosperity+1). |

---

## Two-season churn trace (the deck in motion)

> **S1 · Π=4.** Directive=Extract → `G201` (war-levy) draws; `G101` (only sons) chains in. **Vise:** the levy vs the widow.
> You `Defy/Divert` the levy and `Hold Court` for Mertha. → suspicion +1, **Konrad +1→G606**; Hedda.Disp +2, PS +1, `Precedent:only-sons-exempt`, `Reputation:Just`. Π → 2.
> **S2 · Π=2** (low → Opportunity bias). The deltas *are* the new world: suspicion notched → Directive escalates ("restore the levy or be audited"); grateful Hedda's progress advanced → `G303` (alliance) draws; the stiffed Garrison + Orsk's reading of weakness → `G502` (Orsk's whisper) draws.
> You accept `G303` (Hedda alliance — Stage 2→3 progress) and `Investigate` in `G502` → find `Leverage:konrad-corrupt`. You've just defused `G606` *and* gained a parliamentary proxy — but deepened the Crown break, which is next season's Directive.

Every move you made became a move the world made back.
