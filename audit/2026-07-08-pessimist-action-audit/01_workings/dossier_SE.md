# Lane Dossier — SE (Settlements)
## Pessimist Subtractive NERS Audit · 2026-07-08 · Sonnet reconcile pass

**Charter binding:** `designs/audit/2026-07-08-pessimist-action-audit/00_grounding/00_charter.md`.
Criteria bound to `references/throughlines_meta.md` §0 (N), §1 (Ω), §5 (Q), §7 (Failure Lexicon).
**Cardinal rule applied throughout:** every verdict below judges the action *as if built to the
fullest extent its own design specifies* — never its current build state. Build state appears only
in `build_state_note` fields as routing metadata.

---

## 0. Reconciliation — what's dispersed and how it was merged

The SE lane's player-action surface is **not one document but three, at two different maturities**,
and reconciling them is most of this dossier's work:

1. **`settlement_layer_v30.md` §3.2`** — the *ratified, CURRENT-listed* baseline: four bare
   stat-pump governance verbs (Develop / Fortify / Pacify / Administer), one free action per season,
   no method choice, no politics attached to the roll itself. This is the head `CURRENT.md` points
   to today.
2. **`designs/territory/governance_play_redesign_v1.md`** — **PROPOSAL** (2026-06-22), explicitly
   framed as replacing §3.2's four verbs with an 8-verb Administration-Points menu (Develop / Fortify
   / Keep Order / Hold Court / Sponsor / Treat / Levy / Investigate), each verb method-gated so that
   *optimizing the number costs you politically*, plus a mandatory Directive-response fork
   (Comply/Bargain/Defy) and an NPC-ambition/event-deck substrate. `CURRENT.md` and `HANDOFF_SE.md`
   both flag this as the tracked, not-yet-ratified successor (ED-SE-0001/ED-SE-0004, OPT-16) — its
   own diagnosis of §3.2 ("collapses toward 'roll one die a season and watch numbers' unless a GM
   carries it") is exactly the Q-elegant/flavor-only failure this audit would otherwise have to
   independently discover.
3. **`player_agency_v30.md` §9`** — a third, independent economic-verb surface (Trade, Fund
   settlement development, Sponsor settlement event) written from the *personal Resources* side,
   pre-dating the redesign and never reconciled against it.

**Method:** where the redesign is a strict superset/refinement of a §3.2 verb (Develop, Fortify,
Pacify→Keep Order), this dossier judges the **richer, later-specified version** as the design's
actual intent (per the cardinal rule — "as if built as intended" means as intended by the most
mature design statement, not the most recently ratified one) and calls out the superseded bare
version as an internal lineage note, not a second verdict. Where §9 and the redesign independently
specify the *same* verb in incompatible forms (Sponsor), or where a §3.2/§9 verb has no
redesign-carried equivalent (Administer, Fund Development, Trade), those are treated as genuine
reconciliation problems with their own verdicts.

`sim/territory/settlement.py` + `sim/territory/registry.py` are **state/registry only** — they
compute derived stats (`Local Economy`, `Garrison Strength`, `Public Order`) and hold the settlement
struct; **no player-verb execution code exists anywhere in `sim/`**. There is therefore no
prose-vs-code divergence to reconcile in this lane (unlike PC/FA) — the divergence is entirely
**prose-vs-prose** (§3.2 vs the redesign vs §9), which is what this dossier resolves.

**Cross-lane note:** `module_contracts.yaml`'s own `settlement_economy` module entry independently
recommends retirement as a "phantom module (no doc/state/logic)" — this corroborates the
Trade-action finding below (§11) from a completely independent source.

---

## 1. Develop

**Design intent:** the governor invests in the settlement's economic base (Prosperity), choosing
*how* to fund it — Treasury draw (needs Directive room/PA approval), Guild charter (faster, but
plants a standing Guild-Influence claimant), or Corvée (fast, but Order −1, the populace strained).

**As-if-built contribution:** a genuine Renaissance-grounded fiscal-policy decision — public works
funding was never free of political entanglement in any Renaissance city (guild charters, corvée
labor, and treasury debt are all period-accurate financing mechanisms with exactly these
side-effects). Cross-scale: Prosperity feeds `Local Economy` (§1.3) into province Treasury and into
Settlement Weight (§1.8), which feeds faction Mandate — a real, traceable-but-not-fully-anticipable
strategic ripple from a personal-scale choice (Ω-a). Non-dominant: each method's downstream cost
differs by situation (Guild-Influence claim matters more in a Guild-contested settlement; Corvée's
Order hit matters more in an already-unstable one) — no method is strictly best (Ω-d). Q-elegant:
"spend AP, pick a funding method, each method hands power to someone else" restates in one sentence.

**Verdict: KEEP.** Passes N/Ω/Q under attack. (Bare §3.2 "Develop" — a flat Ob roll with no method
choice — would independently have failed Q-elegant/flavor-only, since a stat-pump with no decision
content is indistinguishable from any other stat-pump; the redesign's method-gating is what rescues
it, and is treated as this verb's real specification per the reconciliation above.)

---

## 2. Fortify

**Design intent:** invest in Defense, choosing Garrison (Löwenritter dependence), Militia (Popular
Support +1 but brittle Defense, arms a populace that becomes a future faction-emergence recruit
pool), or Walls (Treasury, slow).

**As-if-built contribution:** this is arguably the lane's single best-grounded verb — the citizen
militia vs. professional/mercenary garrison tension is not incidental Renaissance color, it is
*Machiavelli's own central argument* about where political power in a city actually resides. N
passes emphatically. Ω-a: Defense feeds Garrison Strength into the invasion/siege layer (MB lane) —
real cross-scale stakes. Ω-d: three tradeoffs are genuinely different in *kind*, not just magnitude
— no dominant strategy. Q-elegant: one-read restatable.

**Verdict: KEEP.** Same lineage note as Develop — the bare §3.2 "Fortify" is superseded by, and
judged as, this method-gated version.

---

## 3. Keep Order (supersedes "Pacify")

**Design intent:** raise Order via Consent (Charisma, slow, PS+1), Force (Military, fast, PS−1 +
Local-Actor Disposition−1 + rebound risk), or Clergy (invite Parish services — Order+1 *and* Church
infrastructure creeps in, the explicit "Geneva trap" of §1.6).

**As-if-built contribution:** N passes strongly — legitimacy-through-consent vs. coercive order vs.
theocratic-capture-through-helpfulness is a real, well-documented triad of Renaissance/early-modern
governance strategy (Calvin's Geneva is cited by name in the doc's own historical grounding, §1.6).
Ω-a: Order feeds province Accord (§1.3 floor-average) and is a direct victory-condition input —
as strategically load-bearing as a settlement stat gets. Ω-d: Force is fast but seeds
Grudge/radicalization (a deferred, real cost); Clergy is efficient but a slow-motion sovereignty
transfer (also a real, if delayed, cost) — genuinely no dominant choice.

**Verdict: KEEP.** The bare §3.2 "Pacify" (a flat Ob = `floor((3−Order)+1)` roll, no method) is the
same flavor-only failure as bare Develop/Fortify and is superseded by this version.

---

## 4. Administer (old §3.2 bare verb — no redesign-carried equivalent)

**Design intent:** "maintain Order (no decay this season); reveal one local NPC's active Conviction"
— a low-commitment, information-yielding hold action.

**As-if-built contribution:** even judged charitably, this couples two unrelated payoffs (a
stat-decay pause + a free piece of NPC information) that don't share a throughline — it reads as two
half-verbs stapled together to fill out a four-item menu. Functionally, its "no decay" half is what
simply *not spending AP on Keep Order* already does structurally in the redesign, and its "reveal a
Conviction" half is a strictly worse version of the redesign's `Investigate` verb (which reveals
secrets *and* offers a real four-way disposition choice on what to do with them, §9 below). Under
N's failure-mode test: is "administering" a distinct load-bearing Renaissance dynamic separate from
"governing generally"? No — it is Abstractable into the general act of choosing not to spend your
season on growth.

**Verdict: DISTILL.** Fold into `Investigate` (the information-yield half) and the redesign's
implicit "AP not spent this season" state (the maintenance half); no standalone verb earns its slot.
**Intent gate: NOT-INTENDED** — the redesign silently dropped this verb without ever saying why,
which reads as an accidental omission during the §3.2→redesign rewrite rather than a deliberate cut;
routing this as a design distillation (not a wiring gap) is still correct because the *concept*, not
the code, is what fails to earn its place.
**Retires:** shrinks OPT-16 (governance-redesign staging) — the redesign document no longer needs a
silent-omission reconciliation note once Administer is formally folded rather than left dangling.

---

## 5. Hold Court

**Design intent:** adjudicate a Local-Actor dispute; ruling for one party raises their Disposition
and lowers the other's, and sets a **Precedent** tag that biases the Ob of future related events.

**As-if-built contribution:** this is the one wholly new verb the redesign adds, and it is the
"ruler-as-magistrate" archetype — podestà courts, seigneurial justice, the prince who must judge
between petitioners — which the *entire prior settlement design conspicuously lacked* (§3.2's four
verbs are all stat-pumps; none of them model the ruler literally being asked to rule on something).
N passes on a dynamic no other SE verb covers (non-duplicate). Ω-a: the Precedent tag is explicit
mechanical persistence into future scenes (deck cards, Ob shifts) — real cross-scale, real
traceability, genuinely not fully anticipable. Ω-d: zero-sum by construction — ruling for one party
costs the other, inescapably. Q-elegant: "pick a side, and the world remembers" restates cleanly.

**Verdict: KEEP.** One of the strongest actions in the lane; this is the row most worth protecting
if the redesign document is trimmed for scope elsewhere.

---

## 6. Sponsor / "Sponsor settlement event" (reconciliation: MERGE)

**Two dispersed specs of the same verb:**
- `player_agency_v30 §9`: "Sponsor settlement event, Order +1 (1 Resource)" — flat, no downside.
- `governance_play_redesign_v1 §1.3`: "Sponsor" — AP-costed, funds a durable +1 stat + Disposition,
  but creates a **Debt** tag (a recurring expectation; skipping it next year costs Disposition −2).

**As-if-built contribution:** patronage-with-obligation is real Renaissance-grounded politics
(Medici-style patronage cuts both ways — the patron is *expected* to keep sponsoring). N passes for
the concept. But **if both specs survive into the same build**, the §9 version — same category of
benefit, cheaper currency, *no* recurring-obligation downside — **strictly dominates** the redesign's
Sponsor verb: any rational player takes the free-lunch version and the Debt-bearing version never
gets chosen. That is a direct Ω-d (non-dominance) failure, and it is entirely avoidable by
reconciliation rather than by cutting content.

**Verdict: MERGE.** The §9 bare "Sponsor settlement event" must be retired into the redesign's
Sponsor verb (same action, one spec) before either is built; the surviving merged verb is a **KEEP**.
**Intent gate: NOT-INTENDED** — the duplication is an artifact of the two docs never having been
cross-checked, not a deliberate two-tier design.
**Retires:** shrinks OPT-16's staging surface (one fewer verb-spec discrepancy to resolve before
ratification) and removes a live dominant-strategy bug from the design as currently written.

---

## 7. Treat

**Design intent:** a bounded minor side-deal with a subnational faction leader (intel, labor, a
favor) via social contest; major grants still require the escalated `Petition` path to Provincial
Authority. "Each deal is a chit the faction will later call in."

**As-if-built contribution:** backroom accommodation with guild/church/local power-brokers below the
threshold of a formal treaty is textbook Renaissance urban politics. N passes; distinct from
`Hold Court` (adjudicating locals) and from Grant/Revoke Management (§13, a Provincial-Authority
act) — no duplicate coverage. Ω-a: builds a "leverage web" that presumably feeds later scenes/deck
cards — real cross-scale intent. Ω-d: the cost is deferred (a chit called in later) rather than
hidden — this is consistent with the doc's own Ledger-of-Consequence pillar (P5) and not, on its
face, a violation of "every action pays what it buys," since the player is told at decision time that
a chit is being created.

**Verdict: REFINE.** The verb passes N/Ω, but Q-smooth fails on a specific, nameable gap: the
document never specifies **when or under what trigger a Treat-chit gets called in** (no formula,
no cooldown, no NPC-ambition linkage comparable to the Debt tag's explicit "skip it next year"
rule). Until that's specified, the verb has an unenumerated "except when X" (Q-elegant's own
requirement) — worth fixing before build, not worth cutting.
**Retires:** none named — this is an ordinary design-completeness finding, not a scope cut.

---

## 8. Levy

**Design intent:** proactively extract troops/Treasury/intel for the faction (often to satisfy the
Directive), costing L/PS and/or Order in the settlement — "the dual-authority extraction tension made
literal."

**As-if-built contribution:** over-extraction causing local unrest is arguably *the* canonical
Renaissance/early-modern political-collapse dynamic (tax revolts, billeting resentment, forced
levies triggering revolt across every early-modern European polity this game is modeling). N passes
with the strongest possible historical grounding. Ω-a: directly feeds province/faction
military/treasury pools — textbook cross-scale. Ω-d: the "squeeze" is visible and named at the point
of choice (down-tier cost for up-tier gain), no hidden cost.

**Reconciliation note:** `Levy` (a proactive AP-verb) and "Comply" (a 0-AP response to an
Extract-type Directive) appear together in the worked example (§2.2's card schema: "Comply with
Levy → PS −1..."), which could read as the same event named twice. On inspection they are not
duplicates: `Comply` is the *strategic stance* (accept the Directive's demand at all), while `Levy`
is the *concrete extraction verb* the governor can also invoke proactively, independent of any
Directive, to generate faction resources ahead of demand. Distinct enough to both earn a slot.

**Verdict: KEEP.**

---

## 9. Investigate

**Design intent:** surface a covert actor (Niflhel operative, RM cell, intelligence broker) via a
Cognition+history roll vs. concealment, then choose: expose (faction credit, local fear) / expel
(remove the asset + its risk) / co-opt (gain the asset, share its risk) / shelter (its loyalty, your
exposure).

**As-if-built contribution:** covert political networks and the choice of what to do once one is
found — expose, suppress, turn, or protect — is exactly the espionage-and-patronage texture of
Renaissance city politics. N passes on the four-way outcome branch specifically. Ω-a: each choice
recruits or creates an enemy with its own agenda — real, traceable, not-fully-anticipable
cross-scale consequence. Ω-d: the four choices trade off genuinely different currencies (credit vs.
risk-removal vs. asset-gain-with-shared-risk vs. loyalty-with-exposure) — no dominant pick.

**Duplicate-coverage flag (the roll, not the outcome):** the underlying *roll mechanic* — a
Cognition+history check against a concealment Ob to surface a hidden actor — is structurally
identical to the FI lane's fieldwork Investigation action (`investigation_systems_v30.md`
Observe/Surveil/Reconstruct). Respecifying a parallel concealment-roll engine at the settlement tier
duplicates coverage the corpus already has; the genuinely new, load-bearing part of this row is the
four-way disposition choice *after* discovery, which fieldwork's own Investigation doesn't have.

**Verdict: DISTILL.** Keep the four-way outcome menu as the settlement-specific addition; the roll
itself should invoke/reuse the existing fieldwork Investigation resolver rather than respecify its
own concealment-check engine.
**Intent gate: UNDETERMINED** — could be a deliberate self-contained restatement for engine
convenience, or an oversight from writing the settlement redesign without cross-referencing
fieldwork; the reconciliation reads more like the latter.
**Retires:** shrinks the redesign's own §5.2 build sequence item 3 (event-deck engine) — one fewer
bespoke roll-resolver to author; the settlement layer's "Investigate" build task can consume
fieldwork's existing resolver instead of duplicating it.

---

## 10. Directive Response (Comply / Bargain / Defy-Divert)

**Design intent:** every season the Provincial Authority issues one mandatory Directive; the
governor must Comply (Standing/trust up, but usually strains the settlement), Bargain (a social
contest vs. the PA, softened terms on success), or Defy/Divert (protects the settlement, but adds to
a suspicion track that triggers a Recall scene at threshold, or seeds the governor's own
faction-emergence path).

**As-if-built contribution:** this is the doc's own stated thesis made mechanical — "the Provincial
Authority sets the rules, the Settlement Governor executes them... when they disagree, tension
generates gameplay" (settlement_layer §3.1) was, in the ratified §3.2 baseline, *asserted but never
given a button*. This verb is that button, and it is the load-bearing center of the entire
dual-authority premise the settlement layer was built to model. N passes maximally — the
officer/lord principal-agent tension is arguably THE defining structural feature of Renaissance
political leadership under any monarchy, papacy, or feudal hierarchy. Ω-a: cross-scale in both
directions — settlement-level costs (Order/PS) feed up through §1.8's Mandate aggregate;
faction-level suspicion/recall feeds back down as a Recall scene, and sustained Defy is the explicit
entry ramp to the settlement→national faction-emergence pathway (§6.2). Ω-d: three responses have
genuinely different, non-dominated cost profiles — situational, no free lunch. Q-elegant: "the world
demands something; comply, haggle, or refuse and take the risk" is a one-read rule with predictable
second-order consequences named at the point of choice.

**Verdict: KEEP.** The single highest-value row in this lane; if scope must be cut anywhere in SE,
this is the row to protect above all others.

---

## 11. Trade (`player_agency_v30 §9`)

**Design intent:** "Trade action (Cognition + History, Ob varies by settlement Trade stat, in
Port/City)" — a personal Resources-income roll available in Trade-capable settlements.

**As-if-built contribution:** trade activity in a Renaissance port/market city is real-world
grounded in isolation, but as specified this verb is a bare income roll with **no settlement-state
effect, no faction ripple, and no distinguishing mechanical texture** from the same table's other
income sources (Faction salary, Guild contracts, Loot, Gifts) — it is one more "make a roll, gain
Resources" path sitting in a table that already has four. Ω-a: the action gains the *player* Resources
and touches nothing else — no Prosperity delta, no Local Economy contribution, no Disposition shift,
no NPC or faction consequence is specified anywhere. This is squarely **Personal-only** (Ω-a
failure by the Failure Lexicon's own definition) dressed in a settlement's clothing. N: does it model
a load-bearing, *distinct* Renaissance dynamic, or is it Abstractable into "you can earn money in a
city" (already covered four other ways in the same table)? The latter.

**Corroborating cross-source evidence:** `module_contracts.yaml`'s own `settlement_economy` module
entry independently flags itself for retirement as a "phantom module (no doc/state/logic)" with the
identical diagnosis — this verb is very likely the ghost of that phantom module's intended home, and
neither has ever accreted the mechanical weight that would justify a dedicated slot.

**Verdict: PRUNE.** Personal-only signal + duplicate coverage of the existing generic
Faction-salary/Guild-contract/Loot/Gifts income model; fold Trade into that table as flavor-text on
an existing income source (e.g., Guild contracts already covers this ground in Port/City settlements)
rather than carrying a fifth parallel income roll.
**Intent gate: NOT-INTENDED** — reads as an unreconciled leftover from before the §9 table's other
income sources were enumerated, not a deliberate fifth path.
**Retires:** directly supports and closes `module_contracts.yaml`'s own standing `settlement_economy`
retirement recommendation (verification Lens-2/LD-2) — this finding gives Jordan the settlement-side
half of that call.

---

## 12. Fund Development (`player_agency_v30 §9`, "+1D to Develop, 2 Resources")

**Design intent:** the player spends personal Resources to buy a +1D bonus on the governance
`Develop` roll.

**As-if-built contribution:** as an isolated mechanic this is a thin "pay to reduce difficulty"
purchase with no distinguishing content of its own — it doesn't introduce a new tradeoff, just makes
an existing one (the roll's Ob) easier for a resource cost. It duplicates ground the redesign's
`Develop` verb (§1) already covers with its own, richer "choose a funding method" structure
(Treasury/Guild/Corvée) — that structure already *is* "spend something to fund development," just
with three politically-differentiated options instead of one generic dice-bonus purchase.

**Verdict: MERGE.** Fold into `Develop`'s existing Treasury-funding method rather than carrying a
parallel personal-Resources buy-in; a flat dice-bonus purchase sitting alongside a
politically-textured three-way funding choice is redundant surface, not a second decision.
**Intent gate: NOT-INTENDED** — predates the redesign's richer Develop verb and was never revisited
against it.
**Retires:** shrinks OPT-16's staging surface by one more unreconciled §9/redesign overlap.

---

## 13. Grant / Revoke Subnational Management (`settlement_layer_v30 §3.3`)

**Design intent:** the province faction (Domain Action, Influence, Ob 1) may grant a settlement's
management to a subnational faction (Church/Guilds/Ministry/Löwenritter/RM/Wardens), or revoke it
(Ob = subnational Influence ÷ 2; Order −1, Disposition −2 with the subnational leadership).

**As-if-built contribution:** delegating urban administration to a guild, church chapter, or
military order is squarely period-accurate (Hanseatic self-governance, ecclesiastical immunities,
condottieri garrison rights). N passes on the concept. Ω-a: real — changes which faction's stats
govern the settlement, ripples into the §1.8 L/PS→Mandate aggregate and the settlement's visible
subnational-faction texture (§4.2). Ω-d: Grant is cheap up front but trades away direct control
(and risks the §3.3 "Contested management" conflict later); Revoke has an explicit, visible cost.

**Lane-boundary flag:** this action is exercised by the player *in their Provincial-Authority
capacity* (§3.1's other authority slot, distinct from Settlement Governor), i.e. it is mechanically
indistinguishable from any other faction-tier Domain Action (`da.public_governance` in
`module_contracts.yaml`) that happens to target a settlement rather than a province. It appears in
this lane's action-home list only because it's written inside `settlement_layer_v30`, not because
it's a verb the settlement *governor* (this lane's actual protagonist role) exercises.

**Verdict: PRUNE (lane-dedup signal, not a content cut).** The mechanic itself earns its place
(N/Ω/Q all pass) — what should be pruned is its double-homing: it should be owned and enumerated once,
by the FA lane's Domain Action inventory (which is independently reconciling the `da.*` vocabulary
per this audit's FA dossier), not carried separately here.
**Intent gate: DELIBERATE** — the dual-authority split (§3.1) is an intentional design feature, not
a gap; the lane-homing issue is an audit-scoping artifact, not a design flaw.
**Retires:** avoids double-counting this action across the SE and FA lane dossiers; FA's
`domain_actions` reconciliation (C-FA-12, `doc: null`) should be the action's single home.

---

## 14. Expand Institutional Capacity (`settlement_layer_v30 §1.4.3`)

**Design intent:** a Domain Action (Treasury −300, scene action at settlement) that adds +1 Wing
slot to a Seat/Cathedral's facility capacity, capped at +1 per settlement per decade — the release
valve for the "full-capacity political pressure" mechanic (§1.4.3: at capacity, rank advancement
forces a Wing-holder's departure, a formal expansion, or a Prince-in-Waiting compromise).

**As-if-built contribution:** court-capacity politics — competition for a fixed number of seats at
the ruler's table — is a real, well-documented Renaissance-court dynamic (limited household offices,
competition for royal apartments and council seats). N passes; this is not an edge case, it's the
concrete mechanical instantiation of a genre-central "who gets a seat at court" dynamic that the
whole faction-politics layer otherwise only gestures at abstractly. Ω-a: gates personal Standing
6+ advancement (a PC-lane consequence) behind a strategic-layer capital investment — a clean,
legible cross-scale coupling in *both* directions. Ω-d: real, visible, rate-capped cost (Treasury
−300, ≤1/decade) prevents this from becoming a spammable release valve. Q-elegant: restates in one
sentence; the decade cap is the enumerated "except when X."

**Verdict: KEEP.** Minor in scope relative to the Directive/Hold Court/Declare-Faction rows, but it
is not redundant with `Develop` (different target — a facility slot, not the Prosperity stat — and
different gating logic, political-capacity pressure rather than general economy) and earns its
place on its own terms.

---

## 15. Declare Faction (`settlement_layer_v30 §6.2`, Stage 3→4 threshold)

**Design intent:** once a player-built organization controls 4+ settlements across 2+ provinces at
Renown 7+, a Domain Action (Influence pool = Renown ÷ 2, Ob 3) formally declares it a national-level
faction with a full stat sheet (§6.2's "Founded Faction Starting Stats," ED-790).

**As-if-built contribution:** this is the capstone payoff of the entire settlement-to-national
progression pillar this document exists to model (its own header names "player progression from
settlement to national" as core scope, explicitly citing ROTK's officer→lord arc and CK3's vassal
play). N passes maximally: a subnational movement's assertion of sovereign status is one of the
defining Renaissance-era political dynamics named in the canonical N test itself (communes, city-
states, and condottieri principalities all emerged exactly this way). Ω-a: this is as cross-scale
as an action can be — it converts an accumulated personal-scale track (Renown) plus an accumulated
strategic-scale holding (settlements/provinces) directly into a brand-new instance of the game's
top-level actor type, unlocking Domain Actions, Parliament participation, and victory-condition
eligibility. Ω-d: heavily gated (4+ settlements, 2+ provinces, Renown 7+, Ob 3 spend of a resource
that took the whole prior arc to build) — there is no shortcut path, and the founding stat sheet is
deliberately weak (Legitimacy 2, Military 1) so the new faction is politically nimble but
institutionally fragile rather than an instant power spike. Q-elegant: the one-sentence rule ("build
enough settlements and Renown, then declare") has a predictable, well-specified second-order
consequence (the exact starting stat block).

**Verdict: KEEP.** This is the second-highest-value row in the lane after Directive Response — it is
the specific mechanical payoff of the "become a lord from nothing" fantasy the whole lane is built
around, and cutting or diluting it would gut the North Star this subsystem exists to serve.

---

## Summary table

| # | Action | Verdict | Criterion |
|---|--------|---------|-----------|
| 1 | Develop | KEEP | Ω-d three genuine methods |
| 2 | Fortify | KEEP | N — Machiavellian militia/garrison tension |
| 3 | Keep Order | KEEP | N — Geneva-trap grounding |
| 4 | Administer | DISTILL | N — abstractable into Investigate + non-spend |
| 5 | Hold Court | KEEP | N — ruler-as-magistrate, no duplicate |
| 6 | Sponsor (merge §9+redesign) | MERGE | Ω-d dominant-strategy risk if unreconciled |
| 7 | Treat | REFINE | Q-smooth — chit-calling trigger unspecified |
| 8 | Levy | KEEP | N — tax-revolt dynamic, distinct from Comply |
| 9 | Investigate | DISTILL | N — duplicate roll-engine w/ FI lane |
| 10 | Directive Response | KEEP | Ω — the lane's load-bearing center |
| 11 | Trade | PRUNE | Ω-a personal-only + duplicate income coverage |
| 12 | Fund Development | MERGE | Duplicate coverage w/ Develop funding methods |
| 13 | Grant/Revoke Management | PRUNE (lane-dedup) | Belongs to FA's domain_actions inventory |
| 14 | Expand Institutional Capacity | KEEP | N — court-capacity politics, cross-scale gate |
| 15 | Declare Faction | KEEP | Ω-a — the settlement→national capstone |

**Lane summary:** the SE lane's headline actions (Directive Response, Hold Court, Declare Faction,
the three method-gated stat verbs) are genuinely strong, well-grounded, non-dominated, one-read
mechanics — the redesign fixed the real problem (§3.2's flavor-only stat-pumps) that a pessimist
audit would otherwise have flagged wholesale. The residual subtractive findings are narrow and
mostly about **reconciling three unmerged specs of the same lane**, not about cutting load-bearing
content: one flavor-thin personal-income verb prunes cleanly (corroborated independently by
`module_contracts.yaml`), two verb-pairs need merging to avoid a live dominant-strategy bug and
redundant funding-purchase surface, one verb needs its roll-mechanic redirected to an existing
resolver instead of respecified, one verb needs its silently-dropped functionality distilled into
its replacement, and one verb (Grant/Revoke Management) is correctly designed but mis-homed across
lanes. None of these findings cut the lane's actual North-Star-facing content.

