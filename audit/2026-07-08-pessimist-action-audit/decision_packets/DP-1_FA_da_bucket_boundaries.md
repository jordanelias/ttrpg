# DECISION PACKET — ED-FA-0006 da.* CROSSWALK: THREE BOUNDARY RULINGS

**FROM:** Pessimist-action audit residual (FA lane)
**TO:** Jordan (ratification authority)
**RE:** `domain_actions` module `doc:null` closure — per-verb da.* bucket assignment at three undetermined boundaries
**DATE:** 2026-07-08

---

## 1. HEADLINE

`references/module_contracts.yaml`'s `domain_actions` module (lines 479–504) carries `doc: null` and emits five outcome-tag buckets — `da.antinomian_action`, `da.covert_betrayal`, `da.diplomatic_alliance`, `da.economic_intervention`, `da.public_governance` (lines 487–491) — consumed by `faction_state` (lines 58–63), `npc_behavior` (lines 111–113), and `piety_track` (lines 213–214). ED-FA-0006 (2026-07-08, pessimist-action audit; gap_notes line 498) reframed this from "author a new standalone system" to "add a per-verb da.* tag + short crosswalk note" over three **existing** catalogs: `params/bg/core.md`'s Standard Action Ob Reference (lines 210–230), `designs/provincial/faction_layer_v30.md` §5.4 Parliamentary Actions (the "Parliamentary Sanction" cluster, lines 438–454), and `params/bg/faction_actions.md`'s unique cards. This is a **REFINE, not a build task** — the five-bucket set itself is settled. gap_notes (line 499) gives a DIRECTIONAL first pass but declines to rule on three seams, calling them Jordan's boundary to draw. da.* is consequence-routing metadata, not flavor — the bucket a verb lands in determines *which module reacts and how*.

---

## 2. Fork (a) — `da.economic_intervention` vs `da.public_governance` (fiscal-administrative verbs)

**Verbs (gap_notes line 499):** Govern, Trade, Subsidy, Piety-Spread, Community-Organising, Martial-Governance — see `core.md` lines 215–216/225/229, `faction_layer_v30.md` line 449 (Subsidy, confirmed *not* part of the Parliamentary Sanction parameterization), `faction_actions.md` lines 16–28 (Piety-Spread, PP-428).

**Downstream stakes:** `da.economic_intervention` is consumed only by `faction_state` (line 62) and `settlement_economy` (line 627) — the latter itself flagged RECOMMEND RETIRE (line 635), player-verb side already PRUNED per ED-SE-0005 (line 636), folding into `settlement_layer`'s Prosperity delta. `da.public_governance` is consumed by `faction_state` (line 63) **and** `npc_behavior` (line 113) — NPCs form dispositions/reactions to it. The fork: does the verb trigger NPC-level reaction (public_governance), or stay a ledger-only settlement/treasury effect with no NPC awareness (economic_intervention)?

- **Option A** — split by object: settlement/wealth-targeted verbs (Trade, Subsidy, Piety-Spread) → `economic_intervention`; people/legitimacy-targeted verbs (Govern, Martial-Governance, Community-Organising) → `public_governance`.
- **Option B** — all six → `public_governance` (NPCs react to all fiscal-administrative acts).
- **Option C** — all six → `economic_intervention` (pure ledger effects; no NPC reactivity).

## 3. Fork (b) — `da.antinomian_action` vs `da.public_governance` (punitive-institutional verbs)

**Verbs (gap_notes line 499, quoted):** "Censure/Embargo/Outlawry/Excommunication/Active-Inquisition/Church-Seizure." These split structurally: Censure/Embargo/Outlawry are three of the five severity tiers of the single **Parliamentary Sanction** action (`faction_layer_v30.md` lines 440–448: tiers Censure, Embargo, **Blockade — Military-3 gate**, Combined Embargo+Blockade, **Outlawry — CB-to-all rider**, line 448); Excommunication (CB-granting trigger, lines 378/396/554 — no standalone tabulated roll found), Active Inquisition (PP-429, `faction_actions.md` lines 31–43), and Church Seizure (§2.7, `faction_layer_v30.md` lines 305–313) are separate Church-only unique cards, explicitly outside the Sanction parameterization (line 440).

**Downstream stakes:** `da.antinomian_action` reaches `piety_track` (line 213, emits `state.scar_acquired` line 223, looping to `faction_state` line 79) in addition to `faction_state`/`npc_behavior` — it can inflict a Conviction Scar. `da.public_governance` reaches only `faction_state`/`npc_behavior` — no scar path. The question: is Parliament sanctioning a rival, or the Church excommunicating/seizing territory, a scar-inducing transgression, or ordinary (if harsh) institutional politics?

- **Option A** — all six → `antinomian_action` (institutional coercion is norm-violating regardless of legality; scar applies uniformly).
- **Option B** — all six → `public_governance` (constitutionally/doctrinally sanctioned procedures, not lawless transgressions; reserve the scar for genuinely unlawful acts).
- **Option C** — split by severity: mild tiers (Censure, Embargo) → `public_governance`; instruments that bypass ordinary vote-and-rebuttal or act outside Parliament (Blockade, Combined, Outlawry, Excommunication, Active Inquisition, Church Seizure) → `antinomian_action`.

## 4. Fork (c) — `da.covert_betrayal` scope for lawful state intelligence

**Verbs (gap_notes line 499):** Spy, Investigate, Counter-Intelligence — `core.md` lines 221–222 (Investigate/Intel; Spy, which ED-FA-0006 already gave an explicit Failure clause), `faction_actions.md` line 227 (Counter-Intelligence Postures, PP-442) — vs. treachery/betrayal proper (covert unique cards not tied to a faction's own lawful apparatus).

**Downstream stakes:** `da.covert_betrayal` reaches the same triple as `antinomian_action` — `faction_state` (60), `npc_behavior` (112), `piety_track` (214). A faction's own sanctioned Spy/Investigate/Counter-Intelligence action tagged `covert_betrayal` trips the Conviction-Scar path and `npc_behavior`'s betrayal-reaction logic exactly as if it had betrayed an ally. gap_notes flags that the tag name itself may not fit a legitimate state's own intelligence work.

- **Option A** — keep these three under `covert_betrayal`, reading the bucket as "resolved covertly" (a methodology tag), not "morally a betrayal."
- **Option B** — reroute to `public_governance` (or `diplomatic_alliance` if directed at a treaty partner), reserving `covert_betrayal` strictly for oath-breaking/defection/sabotage against an existing relationship.
- **Option C** — give these three **no** da.* tag, on the precedent set for direct-effect military verbs (Muster/March/Fortify/Blockade-Naval, gap_notes line 499) — their consequences already resolve within their own action economy without cross-module routing.

---

## 5. What this closes vs. leaves untouched

**Unblocks:** once (a)/(b)/(c) are ruled, the `domain_actions` gap-note (line 497) closes fully — per-verb da.* tags get authored into `core.md`'s Ob table, into the §5.4 table (add a tag column to the existing DISTILL prose), and into the `faction_actions.md` unique-card entries.

**Unaffected either way:** the five-bucket taxonomy itself is not reopened; direct-effect military verbs (Muster/March/Fortify/Blockade-Naval) take no da.* tag under every option; and `domain_actions` stays a crosswalk layer over the three existing catalogs, not a new standalone design doc.

**END MEMO.**
