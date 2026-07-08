# SE Lane — Inverted Critic Pass (Sonnet, read-only)

**Method:** for each condemned action (verdict != KEEP), attempted the strongest honest steelman for keeping it as-specified, judged as-if-built per the charter's cardinal rule. Cross-checked claims against source docs (`governance_play_redesign_v1.md`, `player_agency_v30.md §9`, `settlement_layer_v30.md §3.3`, `investigation_systems_v30.md`, `module_contracts.yaml`) rather than trusting the dossier's prose alone. Re-verified no verdict cites build-state as evidence — none do; all `build_state_note` fields are properly quarantined as routing metadata.

---

## 1. Administer — DISTILL → **UPHELD**

**Steelman attempted:** Administer's "maintain Order, no decay" half could be read as a deliberate *low-risk pass option* distinct from Keep Order's three costed methods — a stability lever for governors who don't want to spend into a faction-empowering tradeoff. Its Conviction-reveal half could be read as a *risk-free* information action, non-dominated against Investigate's contested, enemy-making four-way reveal.

**Why it fails:** the risk-free-information framing actually strengthens the cut, not the keep — a guaranteed no-roll Conviction reveal sitting next to Investigate's costed, consequence-laden reveal is a **dominance** problem (never take the risky option), not a non-dominance defense. And the "safe pass" framing is exactly what Keep Order's Consent method already is, just less textured (Keep Order's Consent path is the deliberate slow/safe/PS+ option; Administer adds nothing Keep Order doesn't already cover with a real political cost attached). Confirmed by direct read of `governance_play_redesign_v1.md` §1.3: the redesign silently drops Administer with no reconciliation note. Two unrelated payoffs, both individually subsumed by richer existing verbs — DISTILL (fold into Keep Order + Investigate) stands.

**Verdict:** UPHELD.

---

## 2. Sponsor / Sponsor settlement event — MERGE → **UPHELD**

**Steelman attempted:** the two specs could be read as operating on different currencies for different reasons — `player_agency_v30 §9`'s flat "Sponsor settlement event, Order +1 (1 Resource)" as a personal-wealth action versus the redesign's AP+Wealth-roll, Debt-tagged version as an institutional governance act — i.e., not truly competing for the same decision slot.

**Why it fails:** verified directly — both specs target the *same actor* (the governor), the *same narrative event* (funding a festival/market/shrine/guild-hall), for the *same class of settlement benefit*. `§9`'s version costs 1 personal Resource, has **no roll, no downside, no Debt tag** — strictly cheaper and strictly safer than the redesign's 1–2 AP + Wealth roll + recurring-obligation version. If both existed as written, no rational player ever takes the Debt-bearing version. This is precisely the dominant-strategy failure mode the redesign's own **P1 pillar** ("no free stat-pumps") explicitly exists to prevent — the unreconciled §9 entry is the exact violation P1 was written against. MERGE into the Debt-bearing version is correct.

**Verdict:** UPHELD.

---

## 3. Investigate — DISTILL → **UPHELD (with a caveat worth flagging)**

**Steelman attempted:** SE's Investigate resolves at governance/AP grain (a single "Cognition+history vs concealment" check, 1–2 AP) while FI's fieldwork Investigation Interface resolves at personal-scene grain (a multi-node scene-graph with an Evidence Track building to a threshold, gated by a scene time budget). These are different levels of abstraction for a superficially similar verb — the same relationship as Fortify's coarse "Defense +1" versus a hypothetical detailed siege-engineering resolver, which nobody would call duplicate coverage. Read literally, "redirect the roll to the fieldwork resolver" risks importing scene-graph/time-budget machinery into the AP-economy loop, breaking the settlement season's pacing abstraction — a real Q-smooth cost in the other direction.

**Why it mostly fails, but with a real caveat:** the four-way outcome menu (expose/expel/co-opt/shelter) is explicitly preserved in the dossier's DISTILL — only the underlying "vs concealment" die-formula is targeted for reuse, not the scene-graph apparatus. Read that way (share the resolution *math*, not the *node-traversal minigame*), the DISTILL avoids inventing a third bespoke "find hidden things" formula in the corpus without forcing a grain mismatch. That's a legitimate Q-smooth win and the verdict survives. **Caveat for the record:** if downstream authoring (OPT-16/resolution-plan) implements this literally as "route to the FI scene-graph," that would be a mistake distinct from what DISTILL intends — worth a one-line clarification in the docket that only the check formula, not the fieldwork scene apparatus, is being reused.

**Verdict:** UPHELD (verdict correct; flag the implementation-fidelity caveat above so a downstream builder doesn't over-literalize "redirect the roll").

---

## 4. Trade — PRUNE → **UPHELD**

**Steelman attempted:** Trade is settlement-type-gated (Port/City only), which could be read as a location-specific economic identity rather than a generic income roll.

**Why it fails:** verified `player_agency_v30 §9` directly — Trade sits in a list of six income sources (Faction salary, Settlement governance, Trade, Guild contracts, Loot, Gifts). Of these, every other source is tied to another system's state (governance income derives from Prosperity you built via Develop; Guild contracts presumably track faction relationship; Loot/Gifts derive from other scenes). Trade alone is a bare roll that produces personal Resources with **zero effect on settlement, faction, or NPC state** — the location-gating is flavor text, not a decision surface (no risk, no tradeoff, nobody else's stake). This is a clean Ω-a personal-only failure, independently corroborated by `module_contracts.yaml`'s own `settlement_economy` entry recommending retirement as a phantom module (verified: lines 618–632, "RECOMMEND RETIRE... phantom module"). Two independent readings converge — PRUNE stands.

**Verdict:** UPHELD.

---

## 5. Fund Development — MERGE → **UPHELD**

**Steelman attempted:** Fund Development (spend 2 personal Resources for +1D on the governance Develop roll) could be an *additive* personal-stake modifier that stacks with whichever institutional funding method (Treasury/Guild/Corvée) is chosen — answering "how likely do I succeed" as a separate axis from "who backs me politically" (Develop's actual tradeoff). If additive rather than competing, it isn't strictly redundant.

**Why it fails:** even granting the additive reading, it is a *content-free* die-bonus — it carries no distinguishing tradeoff, faction consequence, or Ledger tag of its own (contrast every other verb in the redesign, all of which emit a churn per §1.6). At best it's a generic "spend personal wealth for +1D on any roll" rule that happens to be single-cased onto Develop specifically, which is exactly the Q-smooth "special-casing" failure the charter flags. Folding it into Develop's spec (as an optional modifier available alongside any funding-method choice) captures 100% of its value with no duplicate entry needed elsewhere.

**Verdict:** UPHELD.

---

## 6. Grant / Revoke Subnational Management — PRUNE → **UPHELD (verdict correct; note it is a bookkeeping cut, not a content cut)**

**Steelman attempted:** could this legitimately be dual-homed — once as an FA Domain Action and once as an SE-lane action available to a settlement's own governor?

**Why it fails:** verified `settlement_layer_v30.md §3.3` directly — the text is explicit: "The province faction may grant management... **as a Domain Action**" and "may revoke... **as a Domain Action**" (Influence-costed, resolved at province/faction tier). The actor exercising this is the Provincial Authority, not the settlement's own governor. There is no SE-tier variant of this verb anywhere in the settlement layer prose — it is a single mechanic that the SE dossier picked up by scope-adjacency, not a second, SE-native instance of it. The dossier is correct that this is a **lane-homing** finding, not a design-merit failure (it says so explicitly, and the N/Ω pass is real). Important for the record: **this is not a content cut** — the mechanic is not removed from the game, only de-duplicated out of the SE inventory in favor of single ownership under FA's `domain_actions` (C-FA-12). No game content is lost; PRUNE is the correct disposition for *this lane's docket entry specifically*.

**Verdict:** UPHELD.

---

## 7. Treat — REFINE → **UPHELD**

**Steelman attempted:** is the missing chit-call-in trigger a real Q-smooth blocker, or ordinary TTRPG looseness that a GM would improvise and doesn't need pre-specification?

**Why it fails to overturn (REFINE is correct, not too harsh):** this repo's own governing premise (CLAUDE.md preamble: **"There is no GM — the engine resolves everything"**) makes an unspecified trigger condition a genuine implementability gap, not stylistic looseness — a GM-less engine cannot resolve "the faction calls in the chit" without a deterministic or at least enumerated firing condition. This is a design-completeness gap, correctly scoped as REFINE (specify the trigger) rather than a deeper cut, since the core concept (bounded backroom deal → deferred leverage) passes N and Ω cleanly and only needs the missing clause. Correctly not treated as a code gap.

**Verdict:** UPHELD.

---

## Spot-check of KEEP verdicts (not fully steelmanned per instructions, checked for over-generosity)

- **Develop** — three funding methods (Treasury/Guild/Corvée) differ in kind (gate-vs-strain-vs-faction-claim), not just magnitude. No dominance found. Holds.
- **Fortify** — Garrison/Militia/Walls differ in kind (dependence vs brittleness vs slow-Treasury). Holds.
- **Keep Order** — Consent/Force/Clergy each carry distinct, real downstream costs (PS, Disposition/Grudge, Church-capture). Holds.
- **Hold Court** — genuinely the only zero-sum adjudication-with-Precedent verb in the lane; not redundant with Investigate's disposition menu or Directive Response's up/down-tier fork. Holds at P1.
- **Directive Response** — verified as the mechanical realization of the dual-authority thesis (§3.1); distinct from Levy (stance vs concrete extraction verb, confirmed by reading both rows in `governance_play_redesign_v1.md §1.3`/§1.4). Holds at P1.
- **Levy** — checked against Comply for redundancy directly: Comply is a *response stance* to the Directive; Levy is the *executing verb* with its own AP cost and L/PS/Order price, usable independent of any Directive. Not a duplicate. Holds.
- **Declare Faction** — heavily gated capstone, deliberately weak starting sheet, no shortcut path found. Holds at P1.

No over-generous KEEPs found requiring downgrade.

---

## Build-state re-verification

Checked every action's verdict rationale (the `criterion`/`one_line` fields, not the `build_state_note`) against the cardinal rule. **No verdict rests on stub-ness, unwired-ness, or unbuilt status as evidence.** All `build_state_note` fields are correctly quarantined as routing metadata (e.g., Sponsor: "this is a prose-vs-prose duplication, not a build-state issue"; Grant/Revoke: "the dual-authority split is an intentional design feature, not a wiring gap"). No corrections required on this axis.

---

## Net result

All 7 condemned SE actions survive critic scrutiny **UPHELD** as originally verdicted — none overturned to KEEP, none downgraded to a harsher cut. One implementation-fidelity caveat flagged on Investigate (share the check formula, not the fieldwork scene-graph apparatus) and one bookkeeping clarification flagged on Grant/Revoke (PRUNE here means single-lane ownership, not content removal — no game content is actually lost). No KEEP verdicts found over-generous on spot-check.

