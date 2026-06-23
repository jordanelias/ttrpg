# Goldenfurt — NPC Collision Cast

**Slice:** S-006 Goldenfurt (Town, Kronmark province, Valorsmark/Crown duchy). Provincial Authority = the Crown.
**Purpose:** the fuel for the event deck. Every dossier is specified for *agency* (an ambition they pursue autonomously) and *leverage* (hooks the player can pull), per `governance_play_redesign_v1.md §3`. The cast is authored so their drives **collide**: any move you make to please one wrongs another.
**Schema:** id · role/faction · ethic (α outcomes / β conduct) · convictions · ambition {goal, method+escalation, timeline, fires_card, autonomous advance} · loyalty/Disposition · leverage {wants, fears, secret} · Knots · trajectory.

---

## The collision map (read this first)

```
            CROWN (Provincial Authority, off-settlement)
                       │ enforces via
                       ▼
   ┌──────────── Konrad Ems G06 (Crown's eyes; corrupt — takes Orsk's coin)
   │                 │ client-of
   │                 ▼
 law │           Orsk Tallow G02 ──── rival ──── Hedda Vorn G01 ── kin ── Tomas Vorn G04
   │   (grain/Guild, α)              (magistrate, β)        (smuggler/Niflhel, covert)
   │                                      ▲ secret: shields Tomas
   │
 faith ── Wessel G03 ──── enemy ──── Greta Saatfeld G05
        (Church, informer, β)        (RM cell elder, covert, β)

THE PLAYER-GOVERNOR sits at the centre: Crown pulls from above (Konrad),
populace pulls from below (Hedda/Orsk/Wessel/Greta/Tomas). No move is free.
```

**Designed collisions:** Hedda (law) vs Orsk (commerce) is the central rivalry — *any* `Hold Court` ruling pleases one and wrongs the other. Hedda's secret (her brother Tomas) is her single point of failure, exploitable by Konrad (who is himself corrupt) or Wessel (the informer). Wessel (Church) vs Greta (RM) is the culture war beneath the surface. Konrad is the suspicion-track made flesh — but his corruption is the player's counter-lever.

---

## NPC-G01 — Hedda Vorn, Magistrate

- **Faction:** none (local law). **Ethic:** β — conduct-weighted; means over outcomes.
- **Convictions:** "The law is the only shield the weak have." · "A judge who bends once bends forever."
- **Ambition:** win a Kronmark provincial-magistrate seat / a parliamentary voice.
  - **Method + escalation:** lawful (build a public record of just rulings) → factional (if blocked, backs a reformist rival for the seat) → **never violent** (β).
  - **Timeline:** 4 seasons. **Progress at start:** 1. **Fires:** `EVT-G601`.
  - **Autonomous advance:** +1 each season she has an open public grievance she's championing; **+0 if the governor rules consistently justly** (co-opting her resets her toward alliance, not rivalry).
- **Loyalty / Disposition(governor):** +1 (cautious goodwill — you're new, and law-minded governors are her hope).
- **Leverage:** wants — a standing fair grain-court, a public commission, the governor's backing for her seat. fears — her brother's smuggling exposed (ends her career *and* her credibility), mob justice, a governor who rules by force. **Secret:** her brother Tomas (G04) runs the river smuggling, and she has quietly looked away.
- **Knots:** kin → G04 (Tomas) · rival → G02 (Orsk) · ally-of-convenience → LA-G03 (Sister Aldith, almoner).
- **Trajectory:** *if blocked* → petitions louder, then throws her weight behind a reformist faction for the seat (constrains your future Directives). *if conviction violated* (you rule lawlessly / suppress by force) → she legitimizes the unrest and withdraws cooperation. *if Disposition low* → quietly audits your rulings, building a case Konrad can use.

## NPC-G02 — Orsk Tallow, Grainmaster (Guild factor)

- **Faction:** Guilds. **Ethic:** α — outcomes-weighted; results justify means.
- **Convictions:** "A full granary is the only mercy that lasts." · "Markets feed more mouths than magistrates."
- **Ambition:** secure a **perpetual Guild charter over the ford toll** — privatize the crossing's revenue.
  - **Method + escalation:** factional (Guild lobbying) → bribery (he pays Konrad) → **hoarding-as-leverage** → an engineered shortage if truly blocked.
  - **Timeline:** 3 seasons. **Progress:** 1. **Fires:** `EVT-G602`.
  - **Autonomous advance:** +1 each season Prosperity rises via Guild-funded `Develop` (he makes himself indispensable); +1 the season after any famine he "relieves."
- **Loyalty / Disposition(governor):** +1 if you fund through him, −1 if you favour the grain-court.
- **Leverage:** wants — the charter, a monopoly, a seat at your table. fears — a free grain-court (Hedda's), price controls, exposure of his hoarding. **Secret:** he's been quietly cornering the granary and pays Konrad (G06) for advance notice of Crown levies.
- **Knots:** rival → G01 (Hedda) · patron-of → G06 (Konrad, buys influence) · employer → LA-G02 (Old Brun resents him).
- **Trajectory:** *if blocked* → hoards to manufacture a shortage (→ Crisis), then offers "relief" at his price (advances G602). *if Disposition low* → diverts grain to a rival settlement. *if conviction served* (you let him run the economy) → Guild Influence climbs, he entrenches.

## NPC-G03 — Curate Wessel, parish priest

- **Faction:** Church. **Ethic:** β — principled.
- **Convictions:** "A soul saved outranks a law kept." · "Order without faith is a house on sand."
- **Ambition:** upgrade the Chapel to a **Church** (Church-infrastructure creep — the Geneva trap, §1.5–1.6), become the town's moral authority, and seat a Templar station in time.
  - **Method + escalation:** lawful (parish services that make the Church indispensable to Order) → factional (Church backing) → **denunciation** (informs the Himmelenger Inquisitor) if blocked.
  - **Timeline:** 4 seasons. **Progress:** 1. **Fires:** `EVT-G603`.
  - **Autonomous advance:** +1 each season Order is low (he positions the Church as the stability provider); +1 if you ever chose `Keep Order: Clergy`.
- **Loyalty / Disposition(governor):** +1 (he wants you dependent on him).
- **Leverage:** wants — the Church upgrade, moral deference, you to suppress RM "heresy." fears — exposure as an informer, RM's growth, being seen as power-hungry. **Secret:** he sends quarterly reports on the town — and on *you* — to the Inquisitor.
- **Knots:** enemy → G05 (Greta/RM) · patron → the Inquisitor (off-settlement) · contests → LA-G03 (Aldith serves the poor over the parish).
- **Trajectory:** *if blocked* → denounces your tolerance of heresy to the Inquisitor (raises Church Attention → your suspicion). *if conviction violated* → withdraws Parish services (Order penalty) and sermonizes against you. *if served* → Church infra entrenches (−2 seizure vector); removing him later needs a Mass Battle or Mandate Challenge.

## NPC-G04 — Tomas Vorn, smuggler (Niflhel-linked broker)

- **Faction:** Niflhel-linked (covert). **Ethic:** α — outcomes.
- **Convictions:** "The river feeds who the Crown forgets." · "Blood before the writ."
- **Ambition:** make the black market the town's **real economy**; shield (and exploit) his sister's position.
  - **Method + escalation:** covert always → open intimidation/violence only if cornered.
  - **Timeline:** 3 seasons. **Progress:** 1. **Fires:** `EVT-G604`.
  - **Autonomous advance:** +1 each season Order ≤ 1 or no garrison (black market thrives, §4.7); +1 the season a levy/tithe squeezes the populace (smuggling demand spikes).
- **Loyalty / Disposition(governor):** 0 (unknown to you until Investigated).
- **Leverage:** wants — the ford unwatched, Crown attention elsewhere, Hedda protected. fears — Hedda's career destroyed by his exposure, an Inquisitor crackdown, Niflhel calling in his debt. **Secret:** he's leveraged to a Niflhel broker — not fully his own man.
- **Knots:** kin → G01 (Hedda) · network → Niflhel (off-settlement) · informant → LA-G02 (Old Brun sees who crosses at night).
- **Reachability** *(v1.1 fix npc-F2)*: Old Brun (LA-G02), the night-ferryman, can be drawn out by `Hold Court`/`Treat` at the ford to name who crosses → an `Investigate` then surfaces Tomas at **any** Order level (writes `Leverage:tomas-known`), not only via the G403 chronic-disorder path. So the player can reach this NPC in a *well-governed* town, not just a failing one.
- **Trajectory:** *if exposed and not expelled* → Niflhel calls a favour through him (→ G504). *if co-opted* → becomes an intel asset (you inherit his Niflhel exposure). *if conviction served* → the river economy entrenches (Wealth +0.5 / Order −0.5 churn, advances G604).

## NPC-G05 — Greta Saatfeld, RM cell elder (posing as a farm-widow)

- **Faction:** RM (covert, Einhir heritage). **Ethic:** β — principled.
- **Convictions:** "The old stone circle outlasts every Crown." · "We do not burn for the rite; we outlast for it."
- **Ambition:** grow RM Presence to **3 Kronmark settlements** (cell resilience, §3.3) and keep the old rites alive against Church/Crown suppression.
  - **Method + escalation:** *(v1.1 fix npc-F3 — escalates on neglect, not only on force)* covert community-organizing → if **blocked-without-force** (conditional shelter, co-opted organizers) she shifts to **deeper-covert cell-export** to the other Kronmark settlements (still advancing G605, just unseen) → open defiance / martyrdom only if violently suppressed; **never aggressor-violent** (β).
  - **Timeline:** 5 seasons. **Progress:** 1. **Fires:** `EVT-G605`.
  - **Autonomous advance:** +1 each season the province CV/PT is low and she's unsuppressed; +1 whenever Wessel (G03) overreaches (drives recruits to her).
- **Loyalty / Disposition(governor):** 0 (hidden; +1 toward governors who leave the hamlets alone).
- **Leverage:** wants — tolerance, the stone circle untouched, hamlet autonomy. fears — Inquisitor surveillance, the Church upgrade, betrayal by a frightened neighbour. **Secret:** several "farm widows" are her organizers; the circle is a live RM meeting site.
- **Knots:** enemy → G03 (Wessel) · network → RM cell (off-settlement) · shelters → the radicalized (LA-G01's son, via G501).
- **Trajectory:** *if ignored / neglected* → quietly exports the cell to neighbouring hamlets (progress still advances — she never stalls, so doing nothing is not safe). *if suppressed by force* → goes deeper covert (+1 Ob to suppress per cell-resilience), recruits radicalize. *if sheltered* → RM Presence grows (PS+ in hamlets, but Church Attention/suspicion rises). *if conviction violated* (the circle is desecrated) → open uprising seed.

## NPC-G06 — Bailiff Konrad Ems, Crown levy agent

- **Faction:** Crown / Ministry. **Ethic:** α — outcomes, Crown-loyal.
- **Convictions:** "The King's writ does not bend." · "A clean ledger is a clean conscience."
- **Ambition:** earn a **posting to Valorsplatz** — and a defiant governor is his ticket up.
  - **Method + escalation:** lawful/bureaucratic — he *is* the Directive's enforcer and the suspicion-track's eyes.
  - **Timeline:** 4 seasons. **Progress:** 0. **Fires:** `EVT-G606`.
  - **Autonomous advance:** +1 each season you Defy or Bargain a Directive (he logs it); +1 if Order falls (he blames you); **+1 each season the settlement's Crown contribution is below quota OR RM/Niflhel Presence rises** *(verify fix npc-F1 — a player-independent source so the Crown's eyes move even against a fully compliant governor; cap +1/season total per verify deck-F2/CG-7)*.
- **Loyalty / Disposition(governor):** +1 while you comply; falls fast when you don't.
- **Leverage:** wants — your compliance, a clean ledger, his promotion. fears — a settlement collapse on his watch (ends *his* career too), being outmaneuvered, you having Crown patronage above him. **Secret:** he takes Orsk's coin for advance levy notice — **corruptible, and discoverable via `Investigate`** (your counter-lever against the suspicion track).
- **Knots:** loyalty → Crown · client-of → G02 (Orsk).
- **Trajectory:** *if you comply* → smooths things, a mild ally. *if you defy* → suspicion climbs, files the report (→ G606 Recall/audit). *if you find his corruption* → he can be turned/blackmailed (neutralizes the suspicion eyes — but now you harbour a corrupt agent, a Debt the Crown may later call).

---

## Minor Local Actors (petition generators)

| id | Name / role | Conviction | Hook |
|----|-------------|-----------|------|
| LA-G01 | Mertha, miller's widow | "My son comes home." | Her only son is taken in the war-levy (→ `EVT-G101`); if he returns embittered he radicalizes (→ `EVT-G501`, feeds Greta). |
| LA-G02 | Old Brun, ferryman | "The ford belongs to no lord." | Resents the Guild toll (→ `EVT-G102`); knows who crosses at night — a smuggling witness who can corroborate or hide Tomas. |
| LA-G03 | Sister Aldith, lay almoner | "Feed them first." | Torn between Wessel's parish and the hungry (→ `EVT-G103` relief petition); a barometer of famine pressure and a wedge between Wessel and the poor. |

---

## Coherence note (self-verified)

Every NPC has a concrete `fires_card` (G601–G606) that the deck implements, and a non-trivial **autonomous advance** so the world moves without the player (the world→player stroke). Every NPC carries playable `leverage` so the player can move them (the player→world stroke). The Knot web guarantees that the four most common verbs — `Hold Court`, `Keep Order`, `Levy`, `Investigate` — each detonate at least one collision.
