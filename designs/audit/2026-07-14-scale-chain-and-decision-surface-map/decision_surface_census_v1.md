# Decision-Surface Census — Governance Roles by Scale

## Status: FILED (analysis) — 2026-07-14 · Lane: IN · ED-IN-0064

> **What this is.** A max-effort census of the *decision surface* each governance role holds today:
> for every role/scale, the meaningful actions it can actually take, a count, a THIN/OK verdict, and —
> for thin surfaces — recommended action-fills grounded in the `research/governance/` corpus and mapped
> to governance-mode-as-constraint-set. The final column asks the load-bearing question: does each action
> **propagate DOWN** (emit a Key that changes the scale below), or is it purely same-scale (a *false depth*
> — motion without leverage on the tier the role nominally governs)?
>
> This is analysis, not a design ratification. Action-fills are proposals for the design pass.

---

## 0 — Method: the "~4–5" heuristic and where it comes from

There is **no corpus rule** that a governance role must offer 4–5 actions. The heuristic is *imported* from
the personal layer as a strategic-surface sanity check. `designs/architecture/player_agency_v30.md` §6.1
sets the **Scene Action Budget** at **3 (Hard) / 4 (Normal) / 5 (Narrative)** actions per season against a
**Scene Slate of 4–9 opportunities** (§4.3). The design intent is explicit: *"The surplus is the point"* —
a decision is only a decision when affordable moves are numerous enough to force triage and the menu
exceeds the budget.

Read up a tier: a governance role is a *real* decision surface only when it offers roughly a scene-budget's
worth of **meaningfully distinct** verbs (≈4–5) — enough that the seasonal choice is *allocation under
constraint* (the P1 pillar of `governance_play_redesign_v1.md`), not single-pick. A role with fewer than
~4–5 distinct meaningful actions is a **false choice**: the player isn't triaging, they're executing the one
obvious move. That is the bar this census applies. It is a heuristic, deliberately soft ("~"), not a gate.

**A second, orthogonal test — down-propagation.** Scale governance is only *scale* governance if the role's
actions reach the tier below. Per `scale_hierarchy_v1.md` §3, every tier "sets/influences the governance
type of the tier immediately below it," and §4 makes L/PS the consent gate on that downward cascade. So an
action that only moves the role's *own* stats (a same-scale stat-pump) is **false depth** even if the menu is
long — exactly the pathology `governance_play_redesign_v1.md` was written to kill at the governor tier
("four stat-pumps … governing collapses toward *roll one die a season and watch numbers*"). This census flags
same-scale actions as false depth wherever they occur.

**Three vocabularies to reconcile.** The corpus describes governance actions in three incommensurate registers,
and they overlap and conflict:

| Register | Home | Grain | Example verbs |
|---|---|---|---|
| **Governance verbs** (personal/settlement) | `governance_play_redesign_v1.md` §1.3; `settlement_layer_v30.md` §3.2 | AP-costed, per-settlement, rolled | Develop, Fortify, Keep Order, Hold Court, Levy, Investigate, Treat, Sponsor |
| **Standard/Domain Actions** (board/strategic) | `params/bg/core.md` §Standard Action Ob Reference | card-slot, per-province, faction-stat pool | Muster, March, Govern, Trade, Survey, Diplomacy, Fortify, Parliamentary Manoeuvre |
| **Faction-unique cards** | `params/bg/faction_actions.md` | once/season or once/arc, faction-locked | Royal Charter, Piety Spread, Parliamentary Challenge, Dynastic Proclamation, Counter-Narrative |

Where the same word appears in two registers it usually means *different things* (settlement `Fortify` = AP-verb,
Defense +1; board `Fortify` = Domain Action, Fort level +1). Where two words mean the same thing they are noted
as overlaps (settlement `Keep Order`/`Pacify` = same verb under two names; `Administer` folded per ED-SE-0005).
The census reconciles per role rather than globally.

---

## Summary scoreboard

| Role / scale | Meaningful actions today | Count | Verdict vs ~4–5 | Down-propagation health |
|---|---|---|---|---|
| **Settlement council member** | vote on council motion; second/introduce a minor petition | ~2 | **THIN** (near-empty by construction) | mostly same-scale (false depth) |
| **Territory bureaucrat** | audit/review a subordinate; access committee/ministry information; nudge Competence | ~2–3 | **THIN** (tier newly-ratified, unbuilt) | strong *in principle*, unbuilt |
| **Territory/province governor** | 8 AP-verbs + 4–5 method/branch expansions + 3 Directive responses | ~11–13 | **OK** (rich — the one worked surface) | rich (the deepest down-tier surface) |
| **Duke (provincial authority)** | Domain-Action suite; faction-unique card; set provincial gov-type; appoint governors; issue Directives | ~10+ | **OK** | strong (sets type, appoints, directs) |
| **Monarch** | Duke set + chain-bypass reach into any tier + Crown card suite | ~15+ | **OK** on count; enrichment available | strong (chain-bypass is the defining lever) |
| **Parliament (as a body)** | Session vote (1/arc); Censure/No-Confidence; Challenge (Hafenmark-only) | ~3–4 | **THIN** (as an institution, distinct from Hafenmark) | mostly same-scale (national clocks); down-reach ruled but unbuilt |
| **Faction leader** | full Domain-Action suite + faction card hand + Duties + Directives + governor assignment | ~15+ | **OK** | rich |

Two of the seven roles are thin because they are **under-authored tiers** (council member, territory bureaucrat —
the tiers `scale_hierarchy_v1.md` just ratified and flagged as needing propagation, §6). One (Parliament) is thin
because its cross-cutting reach was *ruled* (`scale_hierarchy_v1.md` §5.3) but never given verbs. The four "OK"
roles all sit at or above the province tier and inherit the mature Domain-Action economy.

---

## 1 — Settlement council member

**Scale.** The base tier. Per `scale_hierarchy_v1.md` §5.4's worked example, settlements are governed by
*"appointed councils"* that provincial governors *"oversee, coordinate and vet."* The council is a ratified
concept as of 2026-07-13; it has essentially **no authored action menu**.

**(a) Actions available today.** Reconciling the vocabularies yields almost nothing council-specific:

- The **governor verbs** (`governance_play_redesign_v1.md` §1.3) belong to the *governor*, not to an ordinary
  council member — they are spent from the governor's AP budget.
- The single concrete council-member affordance in the corpus is the **Hafenmark Alderman** (Std 3,
  `faction_politics_v30.md` §1.2): *"Voting seat on local council (settlement Order +1D on Pacify in that
  settlement); may introduce minor Parliamentary petitions."* That gives two verbs: **(1) vote on a council
  motion**, **(2) second/introduce a minor petition.**
- Everything else a council "does" is narrated as the governor's or the province's, not the member's.

**(b) Count: ~2.**

**(c) Verdict: THIN — near-empty by construction.** This is the thinnest surface in the census. The tier exists
on paper (§5.4) with no verb set; a council member currently has less agency than a Standing-1 Operative.

**(d) Recommended fills (grounded + mode-mapped).** The research corpus supplies a ready-made council skin:

- **Florentine Signoria** (`governance_modes.md` §1.2, Renaissance): guild-*delegate* seats, pre-allocated to
  named blocs, on a **short forced-rotation term** ("musical chairs" anti-entrenchment). => council seats are
  faction/guild-allocated, not at-large; rotation is itself a lever.
- **Roman consular *intercessio*** (`governance_modes.md` §1, Roman): an **internal, peer-blocking veto** is
  categorically distinct from vote-tallying. => give a member a **portfolio-veto** on a peer's motion, not just
  a yes/no vote.
- **Venetian Great Council / Serrata** (`governance_modes.md` §1.4): membership is a *captured eligibility list*,
  and the body can be neutered or empowered by a single charter act.

Proposed member menu (≈5): **propose an ordinance** (routes to `Hold Court` ratification per §1.3c — the
*gremios/ordenanza* precedent, `governance_play_redesign_v1.md` §1.3c); **second/block a peer's motion**
(intercessio); **petition the governor** (escalate up); **audit a fellow member** (surface corruption);
**vote**. This clears ~4–5.

**Governance-mode-as-constraint-set** (the same seat affords a different set depending on mode —
`governance_modes.md` synthesis, "the label is a constraint set on the legal response"):

| Mode | What a council member can afford |
|---|---|
| **DELIBERATIVE_ASSEMBLY** | Full menu: propose, second, veto, vote, petition — the member is a genuine decision-maker. |
| **OLIGARCHIC_COUNCIL** | Vote + portfolio-veto within one's own seat only; proposal rights gated to senior seats (Signoria rotation). |
| **AUTOCRATIC_FIAT** | Council is advisory. Member reduced to **petition-the-governor** — the vote does not bind. This is where a long-looking menu collapses to a false choice. |

**(e) Down-propagation.** The council is the *bottom* tier, so "down" means individual people/households.
Most member actions are **same-scale (false depth)** — a vote that only re-weights the council itself changes
nothing below. Real down-propagation exists only where an action emits a settlement-grain Key: an **ordinance**
that changes settlement `Order`/L-PS (`settlement_layer_v30.md` §1.8a event table), or a **Bind-the-Cells**-style
partition of Local Actors into liability cells (`governance_play_redesign_v1.md` §1.3b, goningumi). **Flag:**
give council actions a Ledger-tag/Order emission or they are decorative.

---

## 2 — Territory bureaucrat

**Scale.** The **newly-ratified Territory tier** (`scale_hierarchy_v1.md` §1, RATIFIED 2026-07-13) — "multiple
settlements per territory." §6 explicitly lists this tier's mechanics as *tracked-but-unexecuted* authoring:
governor-assignment at territory scale is unspecified (§6 item 1), and there is no bureaucrat action set at all.

**(a) Actions available today.** The nearest existing surface is the **Ministry / Committee / Dicastery
position** apparatus (`faction_politics_v30.md` §7): Crown Ministries, Hafenmark Parliamentary Committees,
Church Dicasteries, Varfell Councils, each with **Competence (0–3)** and **Corruption (0–3)** tracks and player
positions of **auditor, secretary, clerk** (§7.2). A player-bureaucrat can today:

- **Access committee/ministry information** (a Burgher/Std-2+ privilege — §7.2, *"one of the few ways a
  Standing 2 player can meaningfully influence national policy"*).
- **Nudge a Ministry's Competence/Corruption** via holding a position.
- **Retain/Dismiss Clerks** at settlement grain (`governance_play_redesign_v1.md` §1.1a, the *muyou/shúlì*
  Ming–Qing magistrate substrate) — the closest thing to a bureaucrat *verb*, but it is authored as the
  governor's, not a standalone bureaucrat's.

**(b) Count: ~2–3.**

**(c) Verdict: THIN — an unbuilt tier.** This is thin for a different reason than the council: not "advisory by
mode" but "the tier's verbs were never written." `scale_hierarchy_v1.md` §6 is candid that this is pending
authoring, not a decision.

**(d) Recommended fills (grounded + mode-mapped).** The corpus is *unusually* rich here — the bureaucrat is the
research corpus's strongest suit (kin-severed merit ladders):

- **Carolingian *missi dominici*** (`governance_modes.md` §1.5, Carolingian): **paired itinerant audit** — one
  lay, one ecclesiastical, drawn from *outside* the circuit to prevent collusion, empowered to depose or refer.
  => a **dispatch-audit** action that emits a Demotion-Trigger Key on a settlement governor below.
- **Roman *transvectio equitum*** (`political_hierarchy_standing.md` §2, Roman): a **periodic public
  standing-audit** ceremony re-certifying a rank in front of the polity. => a scheduled re-survey event, not
  silent backend arithmetic.
- **Han *cha ju* recommendation-audit + *hejue* accountability** (`political_hierarchy_standing.md` §2.2–§2.3, in-corpus — the Ming-era *kaochengfa* is outside the 8-civ scope; kept below only as the design-doc capture,
  already partly captured as `faction_politics_v30.md` §1.0d *Patron-Sponsored Performance Audit*): monthly/
  annual review cadence feeding promotion/demotion off a ledger, with a **patron-bound lapse** condition.
- **Ottoman *kul* / Roman equestrian** (`political_hierarchy_standing.md` §2, synthesis): the bureaucrat's
  power_base is **kin-severed** — uncapped advancement velocity traded for a total-clawback demotion ceiling
  (*müsadere*).

Proposed bureaucrat menu (≈5): **dispatch a paired audit** (missi) of a subordinate governor; **certify/decertify**
a rank at a re-survey ceremony (transvectio); **allocate Ministry funding/Competence**; **access & leak
information** (Cancellier Grande — the cittadini who *draft* the Directives Senators merely stamp,
`political_hierarchy_standing.md` synthesis); **file an impeachment** (*lex repetundae* — the delivered-vs-demanded
gap, `governance_modes.md` §5 Roman). Clears ~5.

**Governance-mode-as-constraint-set:**

| Mode | Bureaucrat's affordable set |
|---|---|
| **MERITOCRATIC_BUREAUCRATIC** | Full menu: audit, certify, impeach, allocate — the bureaucrat is the tier's real actor (Han *cha ju*, Ottoman *kul*). |
| **ROYAL_COURT_APPOINTMENT** | Audit + report only; certify/impeach require the appointing Duke's counter-signature (Carolingian count *serves at pleasure*). |
| **LANDHOLDER_FRANCHISE** | Bureaucrat is bypassed — authority flows through the land-service bond (Ottoman *timar* officer doubles as governance layer, `governance_modes.md` §7); the "bureaucrat" is a muster-clerk, not an auditor. |

**(e) Down-propagation.** This tier's actions are the corpus's clearest **resolution-quality → standing bridge**:
a missi audit or a repetundae impeachment emits a **Demotion-Trigger Key on the governor at the tier below**,
changing who holds a settlement — genuinely strong down-propagation *in principle*. **Flag:** none of it is wired;
`scale_hierarchy_v1.md` §4 notes L/PS (the consent gate the audit result would move) is 100/100 inert in `sim/`.
So the down-reach is designed-strong, built-zero.

---

## 3 — Territory / province governor

**Scale.** The one worked surface. `governance_play_redesign_v1.md` exists precisely to make this role *"choosing
under constraint, not maintaining stats"* (Pillar P1), and it is the densest menu in the corpus.

**(a) Actions available today.** Three vocabularies converge here and must be reconciled:

- **Governance verbs (canonical menu)** — `governance_play_redesign_v1.md` §1.3, AP-budgeted (`AP = 2 + FacilityTier`,
  2–5/season): **Develop, Fortify, Keep Order, Hold Court, Sponsor, Treat, Levy, Investigate** = **8 verbs**, each
  forcing a *method* sub-choice (e.g. Keep Order = Consent/Force/Clergy) that hands power to a different faction.
- **Method/branch expansions** (PROPOSED, same doc): **Survey** (§1.3a, Hideyoshi *Taikō Kenchi* cadastral lock),
  **Negotiate Quota / Encabezamiento** (§1.3a, Castilian *encabezamiento*), **Bind the Cells** (§1.3b, *goningumi*),
  **Retain Clerks** (§1.1a, *muyou*), **Ordenanza ratification** three-branch under Hold Court (§1.3c, *gremios*).
  ≈ **5 more**.
- **Directive response** — §1.4: **Comply / Bargain / Defy-Divert** = **3**, the dual-authority forced choice.
- **Legacy vocabulary (being superseded)** — `settlement_layer_v30.md` §3.2's four verbs
  **Develop/Fortify/Pacify/Administer**: `Pacify` = `Keep Order` (overlap, same verb renamed); `Administer` is
  **folded** (ED-SE-0005: info-half → Investigate, maintenance-half → the residual "didn't spend on growth"
  state). No net new verbs — this register is a *conflict resolved by supersession*, noted so it isn't
  double-counted.
- **Board register** — `params/bg/core.md` `Govern`/`Survey`/`Fortify`/`Trade` are the Domain-Action *province*
  grain the settlement verbs derive from (`Govern` Ob = `floor(Prosperity/2)+1`, identical to `Develop`'s Ob).
  Overlap, not addition.

**(b) Count: ~11–13** distinct meaningful choices (8 core verbs + ~5 expansions + 3 Directive responses,
net of overlaps).

**(c) Verdict: OK — richly over the bar.** This is the intended target state and the only role where the redesign's
"allocation not single-pick" is actually delivered. If anything the risk is the opposite (authoring load — §5.3
open question: ~60–100 base cards).

**(d) Fills — not needed.** The role is well-served. The relevant note is instead a *mode* observation: the verbs
already encode governance-mode-as-constraint-set implicitly. `Keep Order`'s Force method is an AUTOCRATIC_FIAT
affordance (PS −1, rebound risk); its Consent method is DELIBERATIVE (Charisma, slow, PS +1); `Negotiate Quota`
is NEGOTIATED_ESTATES (the *encabezamiento* — chartered cities trading fixed quotas for *peticiones*). Making the
mode *explicit* — gating which methods are legal by the settlement's declared governance_mode — is the one
enrichment worth flagging (`governance_modes.md` synthesis: mode as constraint on the legal response).

**(e) Down-propagation — the deepest surface.** This is where actions genuinely bite the tier below (Local Actors,
NPCs, households):

| Verb | Emits / changes below | Same-scale? |
|---|---|---|
| **Hold Court** | Realigns Local-Actor Dispositions; writes a **Precedent** tag biasing future events | DOWN (world→player→world, §4.4) |
| **Bind the Cells** | Partitions households into liability cells; **Collective Liability** tag on a whole cell | DOWN (to household grain) |
| **Treat** | Stores a **Debt** chit on a subnational faction (called in via Friction card) | DOWN (entangles subnationals) |
| **Levy** | Extracts up-tier (satisfies Directive) at down-tier cost (L/PS −1, Order −1) | BIDIRECTIONAL (the squeeze) |
| **Investigate** | Four-way disposition (expose/expel/co-opt/shelter) on a covert actor | DOWN (recruits/enemies a person) |
| **Develop / Fortify** | Settlement stat +1; empowers the *patron* chosen (Precedent tag) | *risk of false depth* — the stat-pump is same-scale unless the patron-empowerment tag fires |
| **Directive: Defy** | Standing-debt + Suspicion up-tier; L/PS + Disposition down-tier | BIDIRECTIONAL |

**Flag:** `Develop`/`Fortify` are the residual false-depth risk even in the good design — they are only *not*
stat-pumps because the funding-method sub-choice hands power to a faction. If a port drops the method choice,
they collapse back to the pathology the redesign named.

---

## 4 — Duke (provincial authority)

**Scale.** Province tier. Per `scale_hierarchy_v1.md` §3, dukes *"govern provinces and define provincial
governance type."* **Overlap warning:** in Valoria all three duchy heads *are* faction leaders (Almud/Valorsmark
also monarch, Baralta/Hafenmark, Vaynard/Varfell), so "Duke" and "faction leader" (§7) are the same seats viewed
at different grains. This section treats the Duke *qua* provincial authority; §7 treats the same actor's national
faction economy.

**(a) Actions available today.**

- **Domain-Action suite** (`params/bg/core.md`): Muster, March, Govern, Trade, Survey, Diplomacy, Fortify — the
  standard card-slot actions on provinces the Duke controls.
- **Faction-unique card** (`params/bg/faction_actions.md`): Hafenmark's **Dynastic Proclamation** (territory
  transfer), Varfell's **Cultural Reclamation** / **Counter-Narrative** — one signature lever per duchy.
- **Set provincial governance type** (`scale_hierarchy_v1.md` §3) — cascades down to territorial gov-type.
- **Appoint governors** (§5.4: *"appoints distinguished servants as governors"*) and, per governor eligibility,
  vet their assignments (`settlement_layer_v30.md` §3.2).
- **Issue Directives** to settlements (`governance_play_redesign_v1.md` §1.4: Extract/Tax/Suppress/Install/Host/Cede)
  in the Provincial-Authority capacity.
- **Grant/Revoke subnational management** (`settlement_layer_v30.md` §3.3, single-homed FA-lane Domain Action).

**(b) Count: ~10+.**

**(c) Verdict: OK.** Well over the bar — but note that most of the "count" is inherited from the mature
Domain-Action economy, not authored *for the duke tier*. The genuinely duke-specific levers (set gov-type,
appoint, Directive) are the newer/thinner ones.

**(d) Fills (light — enrichment, not rescue).** The research corpus offers duke-tier depth currently absent:

- **HRE *Reichsexekution* / ducal suppression** (`political_hierarchy_standing.md` HRE; Carolingian §2.1
  Charlemagne abolishing the Bavarian ducal line 788): a duke absorbing a sub-unit's office into direct
  administration.
- **Carolingian benefice-vs-office split** (`governance_modes.md` §2.2 Carolingian): losing an office (demotion)
  should *not* auto-claw-back the land-grant unless adjudicated — model **Title** and **Grant** as separable
  Keys. Directly relevant to how a Duke's governor-dismissal propagates.
- **"Distance from the palace" decay** (`political_hierarchy_standing.md` §2.3 Carolingian): a governor stationed
  far from the ducal seat suffers slow Legitimacy decay absent active maintenance — gives the appoint/recall
  lever teeth.

**Governance-mode-as-constraint-set:** under **AUTOCRATIC_FIAT** the Duke sets gov-type and appoints unilaterally;
under **LANDHOLDER_FRANCHISE** (the HRE elective texture) the Duke must *re-legitimate at every succession* and
appointment is gated by an electoral college; under **NEGOTIATED_ESTATES** the Directive must be signed in sequence
by the province's estate blocs (the anti-caste Einhir faction + farming collective of §5.4's own example).

**(e) Down-propagation — strong.** Set-gov-type cascades down a full tier (§3); appoint/recall changes who holds a
territory or settlement; Directive emits a coercive Key onto a settlement (governor must Comply/Bargain/Defy). The
Duke is a genuine cascade node. **Flag:** the Domain-Action *stat* actions (Trade, Muster) are same-scale
province-stat moves — false depth relative to the tier below — whereas the appoint/gov-type/Directive triad is the
real downward reach. The thin part of the Duke surface is exactly the part that propagates.

---

## 5 — Monarch

**Scale.** Country tier + **chain-bypass**. Per `scale_hierarchy_v1.md` §5.3, the national ruler (Almud) *"can act
directly on any duchy/province/territory/settlement regardless of normal ownership nesting … the Crown's reach is
not bounded by the chain at all."*

**(a) Actions available today.**

- **Everything a Duke has** (§4) over the royal duchy, *plus* the chain-bypass reach into any tier.
- **Crown faction-unique suite** (`params/bg/faction_actions.md`): **Royal Charter** (§PP-433, province-wide Ob
  modifiers), **Royal Decree Enhancement** (PP-435, stat ±1/±2 across factions), **Thread Liaison** (PP-436),
  **Diplomatic Outreach to Schoenland** (PP-437), **Royal Guard** counter-intel (PP-442), **Formal Crown Treaty**
  (`params/bg/core.md`, Crown-only).
- **Set duchy governance type** for the other two duchies (§5.3 sharpens PP-726's "overlordship" into general reach).

**(b) Count: ~15+.**

**(c) Verdict: OK on count.** The monarch is not thin. But the *research corpus offers a materially larger monarch
toolkit than the corpus currently implements* — worth surfacing as enrichment, not rescue.

**(d) Enrichment fills (grounded).** The comparative record's richest monarch-lever set is almost entirely absent
from Valoria today:

- **Adlection** (`governance_modes.md` §4 Roman): inject a seat directly into a *mid-rank* of a Standing ladder,
  bypassing Initiation-Gates — with its own L/PS cost (resented by old families). A monarch chain-bypass *up* a
  ladder, complementing §5.3's chain-bypass *down* the geography.
- **Proscription** (`political_hierarchy_standing.md` §5 Roman): a bulk, published, faction-wide
  Demotion-to-Dishonored order with seized standing reassigned to the issuer's clients — a rare, high-L/PS-cost
  mass-purge action.
- **Damnatio memoriae** (§5 Roman): retroactive ledger-rewrite voiding an actor's past Key-log wins for future
  legitimacy calculations.
- **Sankin-kōtai / hostage-kin** (§1.0c faction_politics, already PROPOSED — *Court Attendance & Hostage-Kin*):
  the Tokugawa leash. Partially captured; extend to a monarch-issued *requirement*.
- **Müsadere clawback** (`political_hierarchy_standing.md` §5 Ottoman): favor-derived (kin-severed) seats face
  total asset-confiscation on dismissal; kinship seats get containment (*Kafes*). A power_base-typed demotion
  branch the monarch invokes.
- **Fratricide vs Kafes succession control** (§Ottoman): fast-succession-with-PS-cost vs safe-succession-with-a-
  competence-debuff — a monarch trade-off, not a fixed trait.

**Governance-mode-as-constraint-set:** the monarch's defining texture (from `governance_modes.md`) is that
**autocracy is never "no rules."** Even AUTOCRATIC_FIAT runs inside a parallel legitimacy order (Ottoman
kanun/şeriat; Roman Senate auctoritas) that can *block* the monarch without sitting in the chain. In Valoria that
bounding order maps to the **Church** (ideological/juridical power_base) and to **Parliament** (§6) — so the
monarch's *affordable* set is mode-dependent: under a strong DELIBERATIVE memory (like Rome's), the monarch pays
ongoing L/PS upkeep to keep ceremonial shells and spikes an L/PS penalty the moment fiat drops the mask
(`governance_modes.md` §3, Principate→Dominate).

**(e) Down-propagation — the defining lever.** Chain-bypass *is* down-propagation by construction: a monarch acts
on any settlement's governance type directly. Royal Charter changes province-wide Obs (down); Royal Decree changes
faction stats (cross-tier). **Flag:** Formal Crown Treaty and Thread Liaison are same-scale national-diplomacy moves
(false depth relative to a settlement) — but the chain-bypass and Charter/Decree levers are unambiguously downward.
The monarch is the healthiest down-propagation surface after the governor.

---

## 6 — Parliament (as a body)

**Scale.** Cross-cutting, chain-*less*. Per `scale_hierarchy_v1.md` §5.3, Parliament *"has no direct chain of
control but can forcibly impact what happens in a province, territory or settlement."* This is the sharpest THIN
finding, because the *reach* was ruled but the *verbs* were never written.

**(a) Actions available today.** Distinguish **Parliament-as-institution** from **Hafenmark's faction cards**
(which are frequently mis-catalogued as "Parliament's" actions):

- **Parliamentary Session** (`params/bg/faction_actions.md` §PP-432): all factions vote Support/Oppose/Abstain —
  but it is **once per *arc***, adjusting PI/CI. A body whose signature action fires roughly once a *campaign* is
  barely a decision surface.
- **Parliamentary Challenge** (§PP-431) — but this is a **Hafenmark-only** faction card (Senator Inward, CI
  suppression), not an action the Parliament-body takes.
- **Motion of No Confidence** / **Censure** (`faction_politics_v30.md` §1.2, worldbuilding §6.2) — available to
  Parliamentarians (Std 4+), again individual-member levers routed *through* Parliament, not Parliament's own.
- **Votes = current Mandate** (`settlement_layer_v30.md` §1.8, §1.8 GD-1 synergy) — Parliament's weight is a
  *derived readout*, not an action.

**(b) Count: ~3–4**, and several are Hafenmark-faction-specific rather than the body's own.

**(c) Verdict: THIN.** As an *institution* with the cross-cutting reach §5.3 grants it, Parliament's action menu is
near-empty — it can hold a once-per-arc vote and be the venue for member censures. The "forcibly impact any
province/territory/settlement" power has **no verb.**

**(d) Recommended fills (grounded + mode-mapped).** The HRE is a purpose-built Parliament precedent:

- **HRE Reichstag three-curiae sequential veto** (`governance_modes.md` §synthesis, HRE; `political_hierarchy_
  standing.md` HRE rungs 3–6): seats pre-allocated to named blocs (Electors / Princes / Cities), **signing in
  sequence** — the NEGOTIATED_ESTATES mode. Model the *representation-lag* (an estate taxed before it wins a
  vote) as content.
- **Reichsexekution** (`governance_modes.md` HRE synthesis; `political_hierarchy_standing.md`): the empire
  enforcing a judgment against a member — *this is the verb for §5.3's "forcibly impact a settlement."*
- **1803 mediatization → Rheinbund** (`political_hierarchy_standing.md` synthesis, "rank = secession blast-radius"):
  a mass demotion of high-immediacy actors that reaggregates the whole polity — Parliament's nuclear option.
- **Golden Bull majority-binding vote** (`governance_modes.md` §1 HRE): 4-of-7 sufficient and binding even without
  unanimity — a concrete tally rule to replace the vague Session.
- **Impeachment / *lex repetundae*** (`governance_modes.md` §5 Roman): Parliament stripping a governor's rank on a
  delivered-vs-demanded audit — the resolution-quality bridge as a *Parliamentary* action.
- **Papal conclave *Ubi periculum* decaying-holdout** (`governance_modes.md` §synthesis): a
  CONSENSUS_UNANIMITY primitive where a holdout imposes an escalating, *shrinking-ration* cost — a richer
  vote-resolver than Support/Oppose/Abstain.

**Governance-mode-as-constraint-set:**

| Mode | Parliament's affordable set |
|---|---|
| **NEGOTIATED_ESTATES** | Curiae sign in sequence; each bloc a sequential veto; representation-lag is live. The richest configuration. |
| **DELIBERATIVE_ASSEMBLY** | At-large binding votes (Roman *concilium plebis* / lex Hortensia); majority binds the whole. |
| **CONSENSUS_UNANIMITY** | Decaying-holdout resolver (conclave); a single holdout costs the whole body until it yields. |
| **AUTOCRATIC_FIAT** (monarch dominant) | Parliament reduced to a ceremonial shell the monarch pays L/PS upkeep to preserve (`governance_modes.md` §3 Rome) — its votes advisory, its reach dormant. |

**(e) Down-propagation.** Today: **mostly same-scale false depth.** Session moves national clocks (PI/CI); Censure
moves a member's Standing. Neither reaches a province/territory/settlement — despite §5.3 explicitly granting that
reach. The **Reichsexekution / impeachment / mediatization** fills are precisely the ones that would emit a
coercive Key downward. **Flag hard:** Parliament is the role where the gap between *ruled reach* and *built verbs*
is widest — its cross-cutting authority is real on paper and inert in mechanics, mirroring the L/PS-inert problem
`scale_hierarchy_v1.md` §4 makes central.

---

## 7 — Faction leader

**Scale.** National, and (in Valoria) coincident with the duchy heads and monarch — see the §4 overlap warning.
This section is the *national faction economy* view of the same seats.

**(a) Actions available today.**

- **Full Domain-Action suite via the card hand** (`params/bg/core.md` §Batch Card Hand): Legionary/Consul/Senator/
  Tribune/Pontifex/Prefect/Diplomat/Colonist/Praetor + Recess, with Domain-Expertise +1D per faction — the
  strategic-layer engine.
- **Faction-unique cards** (`params/bg/faction_actions.md`): Piety Spread, Active Inquisition, Cardinal Focus,
  Ecclesiastical Appointment (Church); Parliamentary Challenge/Session, Diplomat (Hafenmark); Royal Charter/Decree/
  Thread Liaison/Outreach (Crown); Revelation/Counter-Narrative/Ethical Framework (Varfell); Martial Governance
  (Löwenritter).
- **Issue Duties** to player-characters (`player_agency_v30.md` §3 — Investigate/Diplomacy/Governance/Protection/
  Reconnaissance/Subversion/Thread/Escort, 8 types).
- **Issue Directives** to settlements (§1.4) and **assign/vet governors** (`settlement_layer_v30.md` §3.2).
- **Rank-ladder authority** (`faction_politics_v30.md` §1): Formal Recognition Events, nomination of junior ranks,
  the §1.0b Honryoando/Shinonkyūyo Confirm-vs-New-Grant fork (Kamakura precedent), performance audits (§1.0d).

**(b) Count: ~15+.**

**(c) Verdict: OK — the richest surface with the governor.** No rescue needed.

**(d) Note (not a fill).** The faction-leader surface is where the corpus's ladder-management precedents already
landed (the §1.0b–§1.0d additions are drawn straight from the Kamakura *honryō-andō*/*shin-on* and Zhang Juzheng
*cha ju*/*hejue* audit research). The one *mode* observation: the leader's affordable set differs sharply by faction
governance mode already encoded in the ethical frameworks — Crown Virtue (public deeds −1 Ob), Hafenmark
Categorical Imperative (procedure −1 Ob), Varfell Pragmatism (measurable outcomes −1 Ob). This is
governance-mode-as-constraint-set *already partially implemented* at faction grain (`params/bg/core.md`
§3.7 replacement).

**(e) Down-propagation — rich.** Duties propagate down to player/officer actions; Directives propagate down to
settlements; governor assignment changes who holds a settlement; Recognition Events move a subordinate's Standing.
**Flag:** the pure Domain-Action *stat* moves (Trade, Muster, Diplomacy-vs-NPC) are same-scale faction-stat
economy — false depth relative to settlements — but the Duty/Directive/appointment/recognition levers are all
genuinely downward. As with the Duke, the faction-stat register is the false-depth part and the
appointment/directive register is the real cascade.

---

## 8 — Cross-cutting findings

1. **Thinness clusters at the under-authored tiers, not the powerful ones.** The three THIN roles (council member,
   territory bureaucrat, Parliament-as-body) are all tiers `scale_hierarchy_v1.md` ratified *conceptually* on
   2026-07-13 and flagged as pending authoring (§6). The four OK roles all predate that ruling and inherit the
   mature Domain-Action economy. **Thinness is an authoring-lag artifact, not a design choice** — which is the
   good news: the research corpus already supplies the fills.

2. **The "delivered-vs-demanded gap" is the corpus's universal, non-Mandate-of-Heaven fill for every thin tier.**
   `governance_modes.md` and `political_hierarchy_standing.md` independently converge (Roman *lex repetundae*,
   Carolingian *missi*, HRE *Reichsexekution*, Han impeachment, Japanese *honryō-andō*) on a resolution-quality →
   standing bridge. It is the single mechanic that gives the bureaucrat (audit), Parliament (impeachment), and the
   council (petition-escalation) real down-propagation at once.

3. **Governance-mode-as-constraint-set is a *thinness multiplier*, and the corpus already names it.** The same seat
   is a rich decision surface under DELIBERATIVE_ASSEMBLY/NEGOTIATED_ESTATES and collapses to a single false choice
   under AUTOCRATIC_FIAT (council member → "petition the governor"; Parliament → "ceremonial shell"). A THIN/OK
   verdict is therefore *mode-relative* — the audit must be run per mode, not per role, before the port hard-codes
   any menu.

4. **Same-scale false depth is the pervasive risk even in the OK roles.** Every province-and-up role's
   Domain-Action *stat* register (Trade, Muster, Diplomacy, Formal Treaty) is same-scale motion; the down-tier
   reach lives entirely in the *appoint / set-gov-type / Directive / Duty / audit* register. The governor tier is
   the exception — `governance_play_redesign_v1.md` deliberately welded a down-propagating side-effect onto every
   verb (Precedent/Grudge/Debt/Reputation tags). That welding is the template the other tiers need.

5. **Parliament is the single widest ruled-reach / built-verbs gap.** `scale_hierarchy_v1.md` §5.3 grants it power
   to "forcibly impact any province/territory/settlement"; the mechanics give it a once-per-arc vote and nothing
   downward. It is the clearest priority for the design pass, and its fill (Reichsexekution + sequential-curiae
   voting) is the best-attested in the research.
