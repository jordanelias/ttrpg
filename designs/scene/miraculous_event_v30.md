# Miraculous Event (Miraculous Event) Mechanism
## Status: CANONICAL

**Generated:** 2026-04-25 — Stage 4 Solmund split.
**Source atoms:** §22, §23, §24, §25, §26, §27, §28, §29
<!-- Struck 2026-07-07 (ED-IN-0023, C-INJ-2): the leftover Stage-4-atomization boilerplate "**Status:** PROVISIONAL — pending Jordan editorial review." contradicted the live `## Status: CANONICAL` header at line 2 (the doc is cited as canonical corpus-wide — module_contracts.yaml, mechanics_index.yaml). Removed as a stale artifact, not a live provisional flag. -->


<!-- atom: solmund_master_document__22__19-the-problem | section_index: 22 | source_section: "19. The Problem" -->

## 19. The Problem

Church, Crown, and Hafenmark have no mechanical pathway to engage the Southernmost. SA starting values: 0, 0, 1. No existing faction action targets T15 Askeheim. The expedition procedure (southernmost_v30 §6.3) requires TS 30+ practitioner officers, which none possess at game start.

<!-- atom: solmund_master_document__23__20-the-mechanism-rendered-world-change-event-rwce | section_index: 23 | source_section: "20. The Mechanism: Miraculous Event (Miraculous Event)" -->

## 20. The Mechanism: Miraculous Event (Miraculous Event)

### 20.1 What Already Exists

Threadwork_v30 §2.3: "Physical effects (a wound closing, an object moving) are visible to all." Mending co-movement: on Overwhelming, "Non-sensitives notice a distinct easing of tension." Mending requires TS 50+. Ob 6+ (Entrenched Gap and above) requires TS 70+ (threadwork_v30 Mending table). Ob 7 (Catastrophic Gap) and Ob 8+ (Locked Zone border) require collective operations + Einhir framework.

### 20.2 Proposed Trigger

When Mending at Ob ≥ 6 succeeds in any territory at Proximity ≤ 2 from T15 Askeheim: Miraculous Event fires.

| Mending Ob | Miraculous Event Radius | Observable Effects |
|---|---|---|
| 6 | Mended territory only | Local: blight recedes, structures stabilise, water clears |
| 7 | + Proximity 1 | Regional: adjacent territories perceive easing, trade routes open |
| 8+ | + Proximity 2 | Peninsular: effects across southern third |

Miraculous Event does not grant thread knowledge. It grants awareness that something changed. The cause is unattributable to non-practitioners. The effects are physical — identical in kind to what Solmund's original witnesses reported.

### 20.3 SA Increment

Each faction with presence in affected territories: SA +1. One-time per Mending event. Presence conditions: controls territory (Crown/Hafenmark), has PT ≥ 1 (Church), has Trade Route token (Hafenmark), automatic (Varfell).

### 20.4 Local RS Effects

Territories within Miraculous Event radius receive a −1 modifier to their Proximity Rating for RS-band lookup purposes, effective until next Accounting. This represents the local Mending creating a pocket of stability within the broader RS gradient. One-time per Mending event. Resets if RS band transitions globally.

### 20.5 Settlement Accord Effect

Territories within Miraculous Event radius gain +1 Accord at next Accounting (one-time). Represents population response to tangible improvement in living conditions regardless of cause attribution.

<!-- atom: solmund_master_document__24__21-baralta-s-theological-position | section_index: 24 | source_section: "21. Baralta's Theological Position" -->

## 21. Baralta's Theological Position

[ROUTED: This section's content has been extracted to `designs/npcs/baralta_v30.md` per Stage 4 follow-up (2026-04-25, conflict-eval finding MEDIUM-01). Baralta's theological position, reconciliation framework, prophylaxis interaction, and adversarial role as Restoration opponent are character-canon, not scene-mechanism. The Miraculous Event mechanism in this file remains; Baralta-as-entity content lives at `designs/npcs/baralta_v30.md`.]

## 22. Faction Response Pathways

### 22.1 Church

SA increment fires → the only available explanation is Solmund. Church recognises the pattern — its scriptures describe exactly this.

**Proposed Action — Miracle Investigation:** Consul Outward (Church only). Prerequisite: SA ≥ 1 AND Miraculous Event in current or previous arc. Roll: Mandate vs Ob = floor(target territory controller's SA / 2) + 1. Scaling rationale: the more the controlling faction already knows about the Southernmost, the harder it is for the Church to impose its miracle framing.

| Degree | Effect |
|---|---|
| Overwhelming | SA +2. PT +1 in investigated territory. Mandate +1. |
| Success | SA +1. PT +1 in investigated territory. |
| Partial | SA +1. No PT. Investigation inconclusive. |
| Failure | SA unchanged. Stability −1. |

Investigation encounters practitioners. Church faces the aporia: is threadwork-as-Mending heresy or miracle?

**Decision Event — Assert or Accommodate:**
- Assert (suppress practitioner account, maintain miracle framing): CI +1, RM relations −1. Risk: practitioners stop Mending, effects cease, miracle claim undermined.
- Accommodate (acknowledge practitioner involvement, reframe as divinely inspired): CI −1, SA +1. Risk: theological dissatisfaction from orthodox constituencies.

Neither is safe.

### 22.2 Hafenmark/Baralta

Baralta interprets Miraculous Event through divine right + direct communion. Sovereign action, not Church oversight.

**RDT/TD interaction:** Miraculous Event in contested territory provides political ammunition for Reformed Settlement advancement. Miraculous Event strengthens the political case but does not bypass existing RDT advancement prerequisites (Hafenmark M ≥ 3, PI ≥ 4, Church presence in controlled territory). All conditions must be met.

TD escalation penalises Church assertion. At TD 3, any season the Church loses PI gives Hafenmark PI +1.

Baralta invokes Sovereign Authority Doctrine for Southernmost response — the jurisdictional claim that triggers Hafenmark's internal constitutional crisis: Almstedt blocks (founding settlement did not include divine right), Strand may support (deed-logic rewards effective action).

### 22.3 Varfell

Already in the south. Miraculous Event validates existing strategy. Response options: defend Mending site militarily, allow Church/Hafenmark access (knowing the contradictions will tear them apart), or ally with the Restoration to secure the south.

### 22.4 Restoration Movement

The Mending vindicates everything. But claiming credit exposes practitioners to Church prosecution. The practitioner faces the original Solmund pattern: accept the miracle framing (co-opted but safe) or claim the threadwork origin (recognised but prosecuted).

<!-- atom: solmund_master_document__26__23-the-triple-interpretation | section_index: 26 | source_section: "23. The Triple Interpretation" -->

## 23. The Triple Interpretation

| Faction | Interpretation | Must Suppress |
|---|---|---|
| Church | Miracle — Solmund's grace returning | The practitioners' account of what they did |
| Hafenmark/Baralta | Divine communion — grace rewards action | That the practitioners are Einhir-trained |
| Restoration/Varfell | Einhir heritage — ancestral knowledge | That claiming credit puts practitioners at risk |

Each interpretation is internally consistent. None requires falsehood. Each requires ignoring one piece of evidence the others supply. The competition routes through existing systems: CI (miracle narrative), RDT/TD (reformed doctrine), SA (knowledge that makes truth progressively harder to suppress). Short-term: Church and Hafenmark dominate. Long-term: SA makes the threadwork explanation undeniable.

<!-- atom: solmund_master_document__27__24-sa-gated-faction-actions | section_index: 27 | source_section: "24. SA-Gated Faction Actions" -->

## 24. SA-Gated Faction Actions

| SA | Unlock |
|---|---|
| 1 | Can discuss Southernmost in Parliamentary Session |
| 2 | Can deploy Consul Outward toward Proximity ≤ 2 territories for investigation |
| 3 | Can fund Expedition (southernmost_v30 §6.3 — faction-backed) |
| 4 | Can sponsor Mending operations (resources, political cover, military protection) |
| 5 | Operational knowledge sufficient for faction-directed Repair strategy |

<!-- atom: solmund_master_document__28__25-conviction-mechanic-for-rwce-witnesses | section_index: 28 | source_section: "25. Conviction Mechanic for Miraculous Event Witnesses" -->

## 25. Conviction Mechanic for Miraculous Event Witnesses

When a named character witnesses Miraculous Event effects (present in affected territory during the season Miraculous Event fires):

Roll Cognition vs Ob = current Truth. Success: Truth unchanged (framework holds). Partial: Truth −1 (framework strained). Failure: Truth −2 (framework shaken).

Fires once per character per Miraculous Event. Characters with TS perceive more of the underlying mechanism and face sharper Conviction pressure — the experience is harder to reconcile with their existing framework, whether that framework is theological or secular.

<!-- atom: solmund_master_document__29__26-system-connections | section_index: 29 | source_section: "26. System Connections" -->

## 26. System Connections

| Existing System | Connection Point |
|---|---|
| RS track | Miraculous Event fires when Mending improves RS locally. RS band transitions change radiation effects. |
| CI track | Church Assert/Accommodate modifies CI. Miracle narrative reinforces power. |
| RDT/TD tracks | Baralta's jurisdictional challenge routes through Reformed Doctrine. TD escalation penalises Church. |
| IP track | Southernmost engagement diverts forces from northern border. Tradeoff is emergent from unit positioning — no automatic IP trigger. |
| Altonian diplomacy track | Miracle Investigation and Altonian diplomacy maintenance use different action slots (Consul Outward vs. Phase 1 Cardinal Focus). No mechanical conflict. Tension is narrative: Church attention divided between southern miracle and Altonian relationship. |
| Mending mechanics | Miraculous Event derives entirely from existing Mending rules. No Mending mechanics changed. |
| NPC priority trees | Baralta, Himlensendt, Vaynard, Almud need Decision Event branches for Southernmost Contact. |
| POI system | Seam Texts as Remnant POIs. Miracle Investigation may place scripture in new territories. |
| Piety Track | Miraculous Event witness mechanic (§25). |
| Tensions Deck | New cards: "Miracle or Method," "Sovereign Grace," "Southern Knowledge." |
| Turmoil | Strain and RS track different phenomena. Miraculous Event does not decrement Strain. |
| Settlement Accord | +1 Accord for Miraculous Event-affected territories (§20.5). |

---

# PART EIGHT: THROUGHLINES AND IMPLEMENTATION
