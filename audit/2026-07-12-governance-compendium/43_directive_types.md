# Part 43 — Directive-Type Expansion

## Status: PROPOSED (research-derived; not yet ratified into `faction_politics_v30.md` / `governance_play_redesign_v1.md`)

**Source.** `designs/audit/2026-07-10-historical-concerns-action-catalogue/historical_concerns_action_catalogue_v1.md` (filed 2026-07-10, Lane IN, read-only research pass over the governance/event-deck machinery). All entries below are **PROPOSED** — none are ratified canon. The catalogue is explicitly a research/synthesis artifact awaiting a follow-up authoring pass; this Part reorganizes its Directive-shaped proposals into one reference surface.

**Baseline.** The current live Directive enum (per the catalogue's own framing) is:

**Extract · Tax · Suppress · Install · Host · Cede**

All six existing types share one structural property: **each targets the settlement it is issued to.** The catalogue's central finding is that several historical mechanisms don't fit that shape at all — they target a *third party*, they *compel a method* rather than an outcome, or they *disband a standing force* rather than extracting from or governing a place. That is the throughline uniting the proposals below: several are genuinely new Directive *shapes*, not just new flavors of an existing one.

---

## 1. Proposed new Directive types

### 1.1 Embargo

| Field | Detail |
|---|---|
| **What it does** | Targets a **third faction**, not the settlement it is issued to. The governor's own trade network is the instrument — Embargo forces the issuing faction (or its subordinate settlement) to sacrifice its own commerce with the target in order to damage the target's economy. This is the one genuinely novel Directive *shape* in the catalogue: every other Directive (existing and proposed) resolves within the issuing faction's own settlement; Embargo's Comply/Bargain/Defy fork is resolved **by the settlement asked to enforce it**, over "how much of my own trade do I sacrifice for someone else's grudge." |
| **Comply/Bargain/Defy shape** | **Comply** — full enforcement; the enforcing settlement's own trade-dependent Prosperity takes the hit directly. **Bargain** — the target's governor petitions for a License Exception (a Treat-chit corridor, bounded and called-in later) rather than a clean break. **Defy** — the enforcing settlement quietly declines to enforce (Standing-debt with the hegemon, smuggling-Reputation risk on itself). |
| **Trigger** | `target holds bloc-network trade-dependent Prosperity AND hegemon Grudge-tagged toward it AND hegemon cross-faction Standing ≥ target's, mid-high Π`. |
| **Follow-on** | Unresolved 2+ seasons escalates to a bloc-wide Muster among the target's treaty allies (the embargo becomes casus belli). At the enforcement end, widespread License Exceptions seed a smuggling Opportunity/Intrigue, and accumulated hegemon Standing-debt across many License grants seeds an "embargo is dead in practice" Crisis forcing the hegemon's own Directive to be revised. |
| **Historical case** | **The Megarian Decree** (Athens, 432 BCE) — Athens' trade ban on Megara, resolved not by Megara's governor but by Athens' own allied ports deciding how strictly to enforce it against a third party. Also powers **Napoleon's Continental System** (1806–1814), where strict Comply crashed local Prosperity/Order and seeded smuggling, while Bargain-via-License-Exception relieved local pressure at the cost of a standing Debt chit that bloc-wide eroded the embargo — "individually rational governor choices *are* the historical system's self-undermining collapse, reproduced emergently." |

### 1.2 Multilateral / Coalition Embargo

| Field | Detail |
|---|---|
| **What it does** | A coalition-coordinated variant of Embargo, gated through Ministry/Consulta rather than issued unilaterally by one hegemon. Its defining mechanical feature: **it removes the Bargain branch entirely.** A single-faction Embargo still lets the enforcing settlement negotiate a License Exception; a coordinated multi-faction embargo collapses the fork to a binary Comply (capitulate — forced Charter/territory concessions) or Defy (Muster into open war). |
| **Comply/Bargain/Defy shape** | **Comply** — capitulate; forced Charter or territory concessions to the coalition. **Bargain** — structurally unavailable (the coalition coordination is precisely what closes this branch). **Defy** — Muster into open war against the coalition. |
| **Trigger** | `rival Fiscal Stance draws a supermajority of one strategic resource from a single external source AND coalition Grudge/Standing crosses a high threshold at high Π`. |
| **Follow-on** | Defy auto-seeds a full Conquest cycle; Comply seeds a hawkish internal Ambition chain (coup/hardline succession). |
| **Historical case** | **The ABCD Line and the US oil embargo on Japan** (1940–41) — a coordinated multi-power embargo on a single-source strategic resource that structurally foreclosed a negotiated middle path, forcing the targeted faction toward either capitulation or war. A prior single-resource Fiscal-Stance concentration (per Ripple Chain 10 in the source catalogue) is what makes a faction targetable in the first place. |

### 1.3 Recall

| Field | Detail |
|---|---|
| **What it does** | Disbands an **appanage prince's** (or any grantee's) independently-held Military forces. The un-pulled lever against the specific failure mode where granting a claim-basis holder their own standing Military lets them, upon losing a succession contest, convene a rival legitimating assembly and simply Defy the verdict rather than accept it — turning a recoverable splinter into a permanent fracture. |
| **Comply/Bargain/Defy shape** | Directed at the appanage holder: **Comply** — the prince stands down and disbands. **Bargain** — a negotiated partial reduction (retains some force, cedes autonomy or territory in exchange). **Defy** — is diagnostic: refusal to disband confirms the prince intends to convene a rival assembly, and is itself the signal that the succession is about to fracture rather than merely contest. |
| **Trigger** | Paired with the Toluid-family succession trigger: `succession contest active AND a contender holds an appanage-style Military grant AND their External-backing exceeds the capital Inner Circle's combined Standing` — Recall is the pre-emptive or post-contest lever against exactly that grant. |
| **Follow-on** | Left unused, dueling assemblies seed a "Rival Successor-State Sets Own Directive" Friction every season, *exempted* from the normal re-merge resolution — a permanent split. Used successfully, it closes the appanage-strength channel that let the loser refuse the verdict. |
| **Historical case** | **Toluid Civil War** (Mongol, 1260–1264) — Kublai Khan's dominance in the underlying strength math did not prevent the permanent Yuan/Chagatai/Golden-Horde/Ilkhanate split, because appanage princes' independent Military let them convene rival assemblies and Defy regardless of the numbers. Also the diagnosed "un-pulled lever" in the **Kongo Civil Wars** ripple chain (Ripple Chain 2): a chokepoint Toll's Debt seeds an untaxed private-trade Crisis, whose un-Ratified compounding Wealth/Military becomes exactly the appanage-strength condition Recall exists to address. |

### 1.4 Quarter

| Field | Detail |
|---|---|
| **What it does** | A sibling to the existing **Host** Directive, but coercive: it **forces Force-method Keep Order** on the receiving settlement, overriding the governor's own preference for Consent- or Clergy-method order-keeping. Where Host asks a settlement to billet troops, Quarter additionally strips the governor's choice of *how* order is kept while those troops are present. |
| **Comply/Bargain/Defy shape** | Framed primarily as a Friction that escalates on neglect rather than a clean three-way fork at issue time: the settlement is locked into Force-method order-keeping for the Directive's duration; ignoring the resulting Petition pressure is what escalates it to Crisis. The escalation itself narrows future choice — see Follow-on. |
| **Trigger** | `Keep Order.method==Force (or Directive Quarter) in a Prosperity-above-threshold settlement AND PS (Petition Strain) trending negative`. |
| **Follow-on** | Ignoring the Petition raises Π and escalates to a Boston-Massacre-style Crisis — Order loss, Actor-Disposition collapse, a new Grudge. That Crisis chains to a Directive-tier authority shift from negotiated to unilateral Force-method, seeding a longer rebellion Ambition arc. Force-method itself accrues PS loss + Grudge every season it remains active, and each fired Crisis hardens Actor-Disposition, making the Consent method politically *unavailable* going forward — a ratchet narrowing the governor's own future menu toward more Force. |
| **Historical case** | **Colonial Billeting / the Quartering Acts** (1765–1774) — the historical shift from negotiated billeting toward unilateral, Force-imposed quartering, culminating in Boston-Massacre-style Crisis escalation and progressively narrowing colonial administrators' available menu toward more coercion, not less. |

### 1.5 Nationalize Charter (Directive-adjacent: crisis-gated Quo Warranto bypass)

| Field | Detail |
|---|---|
| **What it does** | Not confirmed in the source catalogue as a formal member of the Directive enum, but proposed and shortlisted (§5 item 11 of the source, "Crisis-gated Charter seizure") as a Directive-*shaped* action: it lets a faction seize a foreign- or domestic-held Charter **outside the normal 16-season Quo Warranto window**, once the Charter-holder's leverage has independently eroded. Its distinguishing feature is that resolution routes through **Ministry/Consulta arbitration that can override the battlefield outcome** — the arbitration, not the campaign, decides. |
| **Comply/Bargain/Defy shape** | Not a governor-facing Comply/Bargain/Defy fork in the usual sense — it is triggered opportunistically by the seizing faction, then resolved via forced Ministry/Consulta arbitration that can compel reversal or ratify the seizure regardless of the military outcome. The nearest sibling action, **Revoke Franchise** (below), is the direct-seizure variant without the arbitration step. |
| **Trigger** | `a foreign faction's prior Sponsor/Treat funding to a chokepoint settlement is withdrawn (Friction fires) AND the Charter is foreign-held AND local Grudge is high`. |
| **Follow-on** | Arbitrated reversal writes a `chokepoint charters are contestable by force` Precedent, lowering the future bypass bar for the same maneuver elsewhere; ratification instead seeds a long Reputation/Grudge chain against the seizing faction. |
| **Historical case** | **Suez Crisis and Canal Closure** (1956) — the canal's nationalization was contestable and ultimately partly reversed not on the battlefield but through arbitration/alliance pressure, exactly the "arbitration overrides the campaign" shape this action generalizes. The catalogue names this as the cleanest instance of a broader cluster alongside the **Hanseatic Kontor at Novgorod** closure (1494, direct **Revoke Franchise** — a Charter seizure available only once the holder's *own* Prosperity has independently declined, without the arbitration step) and the VOC precedent. |

### 1.6 Sovereign Bargain (rank-gated Directive-Bargain amendment)

| Field | Detail |
|---|---|
| **What it does** | Not a new Directive type but a **rank-gated amendment to the Bargain branch** available under an existing harsh Directive (Suppress-family occupation): a Standing-6+ (sovereign-rank) actor can convert an open-ended reprisal (e.g., a Force-method Keep Order failure spiraling into massacre) into a bounded, fixed-term Compact indemnity — a one-time payment that ends the plunder rather than letting it run open-ended. |
| **Comply/Bargain/Defy shape** | Available only as an escalation off a failed Force branch; invoking it is itself the Bargain move, converting an otherwise-open Defy/reprisal spiral into a capped, fires-once Compact. |
| **Trigger** | `occupation active AND Keep Order Force fails (riot) AND Π≥8`, with the Sovereign Bargain option additionally gated on Standing-6+. |
| **Follow-on** | Successful Bargain writes a fires-once Compact + Reputation shift; if the rank-gate isn't met (ordinary governor) or the Bargain isn't invoked, unresolved reprisal seeds further Grudge/Intrigue. |
| **Historical case** | **Nadir Shah's Sack of Delhi** (1739) — sovereign-rank negotiation converted an open-ended massacre into a bounded indemnity payment, a mitigation the catalogue notes is explicitly rank-scarce and unavailable to an ordinary governor. |

---

## 2. Directive-adjacent actions referenced alongside the proposals (not enum members, but co-cited)

These are not proposed as new Directive *types* but recur in the same trigger chains as the Directives above and are worth cataloguing alongside them for context:

- **Convene Rival Assembly** — a Contest-stage exploit (Toluid) controlling which claim-basis holders attend a legitimating assembly; the reason Recall (§1.3) needs to exist as a pre-emptive lever.
- **License Waters** — a joint Levy+Fortify precondition action licensing a naval *zone* rather than a settlement, with patrol upkeep (Portuguese Cartaz System, 16th c.).
- **License Exception** — the Treat-chit mechanism that gives Embargo (§1.1) its Bargain branch; each grant is a standing Debt chit that, in aggregate, is what erodes bloc-wide embargo credibility.
- **Standing Fleet** — a Fortify+Muster investment that *gates* whether a Barbary-Tribute-style Friction's Defy branch (a punitive fleet) exists at all; without it the fork mechanically collapses to Comply-only.
- **Alternate Corridor** — a Sponsor extension hard-preconditioned on prior Fortify (airbase/corridor FacilityTier); the Berlin-Blockade-derived answer to an enclave settlement facing a Directive-adjacent supply cutoff. Cannot be reacted into existence mid-Crisis — the investment must already be banked.
- **Revoke Franchise** — direct Charter seizure bypassing the Quo Warranto window against a *foreign* Charter only, once the holder's leverage has independently eroded (no arbitration step, unlike Nationalize Charter).

---

## 3. Reconciled Directive enum — existing + proposed

| Directive | Status | Target shape | Core mechanism | Comply/Bargain/Defy | Historical anchor(s) |
|---|---|---|---|---|---|
| **Extract** | Existing (canon) | Own settlement | Resource/levy extraction | Standard fork | — |
| **Tax** | Existing (canon) | Own settlement | Recurring fiscal levy | Standard fork | — |
| **Suppress** | Existing (canon) | Own settlement | Coercive order-keeping | Standard fork | Magdeburg, Drogheda (harsh-Directive+Defy trigger family) |
| **Install** | Existing (canon) | Own settlement | Governor/institution placement | Standard fork | — |
| **Host** | Existing (canon) | Own settlement | Troop billeting | Standard fork | Basis for Quarter (below) |
| **Cede** | Existing (canon) | Own settlement | Territory/rights transfer | Standard fork | — |
| **Embargo** | PROPOSED | **Third faction** (via own trade) | Sacrifice own trade to damage a rival; Bargain = License Exception | Comply/Bargain/Defy (enforcing settlement resolves) | Megarian Decree (432 BCE); Napoleon's Continental System (1806–14) |
| **Multilateral / Coalition Embargo** | PROPOSED | Third faction, coalition-issued | Same as Embargo but Bargain branch structurally removed | Comply/Defy only (binary) | ABCD Line & US oil embargo on Japan (1940–41) |
| **Recall** | PROPOSED | Appanage/grantee holder | Disband a claim-basis holder's independent Military | Comply (disband) / Bargain (partial reduction) / Defy (diagnostic — signals fracture) | Toluid Civil War (Mongol, 1260–64); Kongo Civil Wars (un-pulled-lever citation) |
| **Quarter** | PROPOSED | Own settlement | Forces Force-method Keep Order, overriding governor preference | No clean issue-time fork; Friction escalates to Crisis on neglect | Colonial Billeting / Quartering Acts (1765–74) |
| **Nationalize Charter** | PROPOSED (Directive-adjacent; crisis-gated Quo Warranto bypass, not confirmed enum member) | Charter-holder (foreign or domestic) | Seize a Charter outside the normal window; resolved by Ministry/Consulta arbitration that can override the battlefield | Arbitration-resolved, not a governor fork | Suez Crisis (1956); cf. Revoke Franchise (Novgorod Kontor, 1494) |
| **Sovereign Bargain** | PROPOSED (rank-gated amendment to an existing Directive's Bargain branch, not a standalone type) | Own settlement, under an active harsh Directive | Converts open-ended reprisal into a bounded Compact indemnity; Standing-6+ gated | Bargain-only escalation option | Nadir Shah's Sack of Delhi (1739) |

**Open questions carried forward from the source catalogue (§6 "design-taste rulings needed"):** whether Nationalize Charter and Sovereign Bargain should be formalized as full Directive enum members or remain amendments/adjacent actions on existing Directives is unresolved — the source catalogue frames Nationalize Charter primarily as a Quo Warranto-machinery bypass branch rather than a new Directive shape, while Embargo, Multilateral Embargo, Recall, and Quarter are explicitly argued (source §5 item 8, and the Toluid/Colonial-Billeting entries) as genuinely new Directive *shapes* — Embargo/Multilateral Embargo because they target a third party rather than the issuing settlement, Recall because it targets a standing force rather than a settlement or population, and Quarter because it compels a *method* rather than an outcome.

---

## 4. Cross-references

- Recall's un-pulled-lever relationship to Kongo Civil Wars: source catalogue Ripple Chain 2 ("Chokepoint toll funds a private army," g→E→G).
- Multilateral Embargo's relationship to prior single-resource Fiscal Stance concentration: source catalogue Ripple Chain 10 ("Cheap hulls → storm loss → locked out of the fix → embargo vulnerability," g/C→C→E→G).
- Nationalize Charter's relationship to chokepoint-Charter Friction chains: source catalogue Ripple Chain 4 ("Neglected dike diverted to war → flood → relocation → Charter fight," g→C→g→G).
- Full succession-crisis context for Recall and the Toluid case: catalogue §2.1 "Succession crises, civil wars, and elite power-struggle collapses."
- Full trade-blockade context for Embargo, Multilateral Embargo, and Nationalize Charter: catalogue §2.2 "Trade blockade, embargo, chokepoint loss."
- Full siege/occupation context for Quarter and Sovereign Bargain: catalogue §2.3 "Siege, sack, occupation, garrison/billeting crises."
