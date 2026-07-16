# Turn 4 — Adversarial Critique (dispassionate; attacks the system AND my own Turns 1–3)

**Date:** 2026-06-04 · `[SELF-AUTHORED — bias risk]` applies to all of Turns 1–3; treated as external work to be broken. Stance: neutral, objective. A finding that survives the attack is reported `SURVIVES`; one that breaks is reported `FALLS`/`NARROWS` without face-saving. Builds on `00`–`02`.

---

## PART A — Attacks on my own prior conclusions

### A1 · "Recall = near-orphan / AUDIT-FOLD" → **NARROWS (was over-confident)**
**Charge:** I asserted Recall's contest roles are "superseded," reducing it to ~3 foldable roles — but I flagged my own [GAP] that I never *verified* `contest.md` is superseded.
**Test (this turn):** `canonical_sources.yaml` declares **`params/contest.md` canonical with a fresh SHA — simultaneously with `social_contest_v30.md`.** `designs/contest/` (contest.md's cited source) does not exist (404). So contest.md is *not* confirmed superseded; it is a still-declared-canonical doc. Under it, Recall feeds **Appraise (`Att+Recall`), the coalition pool (`Focus+Recall`), the +2D cite-bonus** (the last acknowledged-live even by derived_stats §5.2), **the Sparking gate**, and **equip-slot gating** — **~5 live roles, not ~3.**
**Verdict:** **The fold/near-orphan call was overstated.** Recall is still the *thinnest* attribute, but it is **contingent**: under the currently-declared-canonical `contest.md` it is moderately used (fold is premature); under the ratified 2026-06-03 groundup (pisteis+Standing, no Recall) it loses its contest roles (fold strengthens). **Honest restatement:** *Recall's disposition is downstream of the unresolved contest-spec decision — decide it WITH that decision, not before.* The 2026-05-08 "only sparking gatekeeper" premise was itself incomplete (it missed contest.md's Recall pools).

### A2 · "Attribute structure unresolved: 3 macro vs ~10 flat" → **NARROWS (empirically over-stated)**
**Charge:** I called the macro-vs-flat structure "genuinely unresolved in canon," on absence-of-a-roster-doc + the 2026-05-08 F2 flag — i.e., absence of evidence.
**Test:** NPC stat blocks are the ground truth, and **Edeyja is statted FLAT** — "Cognition: 5, Focus: 5", "Endurance: 4" — matching the combat engine's flat fields. `player_agency_v30` has no roster definition.
**Verdict:** **The live system is FLAT** (NPC stat blocks + combat engine agree); **Mind/Body/Spirit is vestigial**, not an active competing architecture. Recalibrate from "designers haven't decided 3-vs-10" to "**the system is flat; the macro framing is stale/vestigial and should be formally retired; and there is still no single canonical roster doc.**" Real E/S issue (vestigial dual framing + no roster doc), but **not** the foundational crisis I framed.

### A3 · "R: FAIL and S: FAIL (broad)" → **NARROWS to PARTIAL**
**Charge:** I stacked R/S-fail with the Disposition-cap contradiction *plus* §13/§5.2 staleness, the Stamina range, the §3 tier table, and the §1 violation.
**Test:** §13/§5.2/§14 mismatches are **edit-lag from changes made *today*** (ED-902 + the combat-pool strike, both 2026-06-04) — propagation lag a single commit clears (P3), not a structural verdict. The §1 "violation" I *already reframed* in Turn 3 as "the rule is wrong, not the formulas" — so it's doc-maintenance, not a robustness break. `derived_stats_v30` is a **PROPOSAL** (A7), so its rough edges are draft-state, not broken canon.
**Verdict:** **R and S are PARTIAL fails, not broad.** R's *durable* basis = the **Disposition-cap cross-doc contradiction** (real; a reader of `complete_systems_reference` gets the wrong cap). S's *durable* basis = **two contest specs both declared canonical** (B1 below) + **no single roster doc** + the **Spirit naming collision (F9)**. Strip the transient items and the verdict is honest but narrower.

### A4 · "Fold Recall into Spirit/Mind" → **REMEDIATION SELF-CONTRADICTS**
**Charge (against my own fix):** I recommended folding Recall (per 2026-05-08 F1) *and* flagged Spirit as overloaded. **Folding Recall's roles into Spirit worsens the exact super-stat problem I identified.** And the **equip-slot gating** role — a legitimate SaGa-style build-capacity axis — has no specified home post-fold.
**Verdict:** **Real gap in my remediation.** If Recall folds, the target is **Cognition** (memory ≈ cognition; avoids the Spirit tax), not Spirit; and equip-gating must be explicitly re-homed (Cognition or History). My Turn-2 remediation #3 was under-specified and partly at odds with #5.

### A5 · Comparative critique (Turn 3) — **CONFIRMATION BIAS; corrects the Recall framing**
**Charge:** Turn 3 "validated" nearly everything I'd pre-concluded and used Disco Elysium to support cutting Recall — without looking for acclaimed games where a knowledge/recall stat *works*.
**Test:** **Disco Elysium's *Encyclopedia* is literally a recall-of-facts skill and is among the most beloved in the game; Pillars of Eternity's *Lore* gates scrolls + dialogue.** A knowledge stat is excellent in a videogame **when it gates rich content** (lore/dialogue/codex/item-use). "Recall stats don't work without a GM" is **false** — I overstated the Burning-Wheel-Wises dismissal.
**Verdict:** **Recall isn't weak because recall-stats fail; it's weak because Valoria gives it almost nothing to gate.** This surfaces a **KEEP-AND-FEED** option I missed and which fits Valoria's DE-citing, narrative-heavy design *better than cutting*: give Recall real content to gate (lore dialogue, codex reveals, scroll/relic use → DE-*Encyclopedia*-class). The honest Recall menu is now **three** paths, not "fold": **(i) fold into Cognition** (if Valoria won't invest in knowledge content); **(ii) keep-and-feed** (DE-Encyclopedia path); **(iii) leave as-is and accept it as the weakest stat.** Jordan's call.

### A6 · Faction-stat scope exclusion → **DEFENSIBLE BUT NOT AIRTIGHT**
**Charge:** I pushed faction base stats (Military/Stability/Intel…) to "adjacent, defer," while auditing faction *derived* stats (§8). The line is somewhat convenient.
**Verdict:** **Survives as a scoping choice** (personal "character" attributes ≠ faction stats), but acknowledge: the same dump-stat lens flags **faction Intel** (nearly cut per `faction_stats_renaissance_review`) — the analysis would transfer. Not re-run here; noted as adjacent.

### A7 · Auditing a PROPOSAL as canon → **WEIGHT ADJUSTMENT**
**Charge:** `derived_stats_v30` is **PROPOSAL** status; I rendered hard verdicts on a draft.
**Verdict:** **Valid.** Findings on the *proposed* derived-stat system are **design-review of a draft** (lower stakes); findings on *ratified* elements (Bonds/Knots N:critical; ED-902; the 2026-06-04 combat-pool strike; the declared-canonical contest contradiction) are firmer. The "rot" is largely "this draft needs cleanup before ratification," not "shipped canon is broken."

### A8 · "Bonds = KEEP, sound" → **SURVIVES (lightly)**
**Charge:** I didn't verify the stability of **Knots** (Bonds' main load-bearing system; `knots_v30` + a `conviction_track_v1` exist — possible flux).
**Verdict:** **Survives** — Bonds is clearly the stronger of the two stats (relationship-capacity pattern, Persona/FE-validated, N:critical per 2026-05-08), but I should not overstate "rock-solid": its cap formula is contradictory (B-resolved to `=Bonds`) and Knots' current stability is unverified. **Bonds = KEEP holds; "sound" carries a small unverified-Knots caveat.**

---

## PART B — Fresh attacks on the SYSTEM (independent-reviewer, not self-correction)

- **B1 [P1, durable] Two contest specs are simultaneously declared canonical with incompatible attribute models.** `canonical_sources.yaml` lists **both** `params/contest.md` (Cognition/Charisma/Attunement/Focus/**Recall/Bonds**) **and** `social_contest_v30.md` (**Composure/Conviction**), both fresh. These cannot both be the contest system. This is a harder finding than the "version tangle" Turn 1 framed loosely — it is a **live canonical contradiction**, and it is what makes the Recall question unanswerable (A1).
- **B2 [P3] `contest.md` cites a non-existent source** (`designs/contest/social_contest_v30.md`; `designs/contest/` is 404). Provenance drift.
- **B3 [durable] The super-stat + dump-stat *simultaneity* survives every attack.** Independent of the contest mess: **Spirit** feeds combat+social+thread (mandatory cross-pillar tax) while **Recall** is the thinnest — a roster with one over-central and one under-used attribute is a genuine balance defect (D&D Con/Dex anti-pattern), regardless of contest-spec resolution. **This is the most robust finding in the whole audit.**
- **B4 [check-the-checker] The freshness gate is necessary but not sufficient.** All 114 sources "fresh" (SHA-current) yet two of them (the contest pair) **contradict each other**, and `contest.md` points at a dead path. Freshness verifies *staleness-of-SHA*, not *mutual consistency* — so "114 fresh" gave false comfort I leaned on early.

---

## NET RECALIBRATED VERDICT (carry to Turn 5)
The adversarial pass **breaks the over-confident parts and keeps the durable core.**

| Turn-2/3 claim | Post-adversarial status |
|---|---|
| Recall = AUDIT/FOLD (near-orphan) | **NARROWED** → weakest attribute, **contingent** on the contest-spec decision; **3 paths** (fold-into-**Cognition** / keep-and-feed DE-Encyclopedia / leave); not a clean "cut" |
| Structure unresolved 3-vs-10 | **NARROWED** → live system is **flat** (NPC blocks); macro = vestigial; durable issue = **no single roster doc** + retire vestigial framing |
| R: FAIL (broad) | **NARROWED → PARTIAL** — durable basis = Disposition-cap contradiction; rest is edit-lag/draft |
| S: FAIL (broad) | **NARROWED → PARTIAL** — durable basis = two-canonical-contest-specs (B1) + no-roster-doc + Spirit naming |
| §1 one-attribute violated | **DEMOTED** (Turn 3 reframe) → retire the stale rule; P3 doc-fix |
| Lateral combat-vs-sibling | **already softened** (Turn 3) → documentation gap |
| Spirit overload / asymmetry | **SURVIVES — strongest finding (B3)** |
| Bonds = KEEP | **SURVIVES** (small unverified-Knots caveat) |
| Fold→Spirit remediation | **CORRECTED** → fold target is Cognition; equip-gating needs a home (A4) |

**Honest bottom line going into reconciliation:** the system is **not currently NERS-clean**, but the *durable* failures are narrower and clearer than Turn 2 implied: **(1)** the Spirit/Recall **balance asymmetry** (firm); **(2)** the **two-canonical-contest-specs contradiction (B1)** which also makes Recall's fate undecidable; **(3)** the **no-single-roster-doc + vestigial-macro** legibility gap; **(4)** the **Disposition-cap cross-doc contradiction.** Recall is the **weakest** stat but its fix is **contingent and three-pathed**, not a settled cut. Bonds is **sound**. Much of the Turn-2 R/S "rot" was transient edit-lag or a mis-framed principle, not a structural break.

`[CONFIDENCE: high on B1/B3 (cited); high on the A1/A2 self-corrections (cited evidence); medium on the three-path Recall menu being complete.]`
`[SELF-AUTHORED — bias risk surfaced and acted on: A1, A2, A4, A5 each walked back a prior over-statement.]`
