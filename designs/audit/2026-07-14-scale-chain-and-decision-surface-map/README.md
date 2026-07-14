# Multi-Scale Governance — Chain / Gap / Decision-Surface Map

## Status: FILED (analysis) — 2026-07-14 · Lane: IN · ED-IN-0064 · analytic/reference, no canon ratification

**What this docket is.** A read-only analysis of how Valoria's governance systems connect *from
character to country and back* — the chains, surfaces, edges, and decision surfaces the design lead
asked to be mapped — plus a ranked, **Mandate-of-Heaven-free** register of gaps and false choices with
resolution recommendations. It **edits no canon**; it hands a ranked design surface to Jordan for the
governance-mode + decision-surface design pass. It is grounded in, and closes the loop with, the
durable research corpus at `research/governance/` (8 civilizations × 3 themes, ED-IN-0064) and the
fresh vector audit at `designs/audit/2026-07-14-governance-vector-audit/`.

**Relation to the predecessor.** Extends (does not duplicate) the `2026-07-13-cross-scale-governance-
grounding/` docket (ED-IN-0051), updating its 17-item decision queue and ~24-gap register for what
PR #136's L/PS spec advanced (SPEC-ONLY, not yet coded) and re-grounding its two Mandate-of-Heaven-
based items (E1/E2 collision, B2 relief-valves) on non-MoH precedent from the research corpus.

## Read order

1. **`unification_synthesis_v1.md`** — start here. The governing capstone: the research→gameplay
   through-line (resolution-quality aggregates *up* into Standing/Legitimacy/Mandate; governance-mode +
   collision discharge back *down*), the unified cross-scale picture, the single ranked design surface,
   and a reconciliation ledger. Verdict: **UNIFIES_WITH_FIXES** (fixes applied).
2. **`decision_queue_delta_v1.md`** — the ranked (Tier 1–4) MoH-free design-pass hand-off.
3. **`gap_register_v2.md`** — every gap keyed to a chain-map edge, classified COMPLETE-THE-CHAIN
   (~19) vs GENUINE-GAP (~8), evidence-traced.
4. **`chain_map_v1.md`** — the two-axis edge map (vertical scale: character→settlement→territory→
   province→duchy→country; horizontal subsystem: faction-action→domain-action→social-contest→field-
   investigation), each edge state-classified (WIRED / HOOK-NEEDED / BROKEN / INERT / DOCTRINE-ONLY /
   SPEC-ONLY) with code/doc/audit evidence. **Load-bearing principle: sim-WIRED ≠ canon-WIRED.**
5. **`decision_surface_census_v1.md`** — per-role action census (settlement council member, territory
   bureaucrat, governor, duke, monarch, Parliament, faction leader), flagging roles below the ~4–5
   meaningful-action floor and recommending research-grounded fills.
6. **`churn_event_opportunity_map_v1.md`** — the three friction sources (character desires/needs,
   evolving geopolitics, event decks) and where world churn can/can't emerge.

## Adversarial provenance (agonist → antagonist → unifier)

- **`adversarial_review_v1.md`** — the docket-internal antagonist pass (verdict SOUND_WITH_FIXES; F-1…F-6).
- **`unification_findings_v1.md`** — the *holistic* antagonist pass over the whole deliverable set
  (research corpus + vector audit + this docket): cross-artifact defects X-1…X-8 (through-line breaks,
  contradictions, taxonomy/scale drift, MoH-adjacency).
- **`unification_synthesis_v1.md`** — the unifier: reconciles every F- and X- finding into one governing
  picture + a prioritized fix-list. Its **6 HIGH fixes (H-1…H-6) are applied to the docket files**
  (sim-vs-canon edge re-grades, the *cha ju* re-citation, the Censure-edge relabel, the caller-count and
  scale-canonicity corrections, and the Tetrarchy mechanic+guard pairing bound into `decision_queue_delta §D`);
  the MED/LOW reconciliations are recorded in its ledger and are safe to apply during the design pass.

## Headline findings

- **The single highest-leverage action is coding PR #136's L/PS §5 sequence** — it advances four heavy
  gaps (B1 L/PS-inert, A2 accord-echo, B4 decay/Mandate→L drift, A4 convergence) from *undesigned* to
  SPEC-ONLY, but all remain uncoded (`lps_inert_check` 100/100 red); the L/PS consent-cascade has no
  gameplay consequence until it lands.
- **Two whole surfaces are unreachable by the live engine:** the Key `scale_signature` enum is 3-of-6
  ladder-nameable (province/duchy/country unrepresentable), and Field Investigation has **zero live
  dispatch path** (`scene_dispatch.py` branches only on combat/contest).
- **Thin decision surfaces are an authoring-lag artifact, not a design choice:** the council member,
  territory bureaucrat, and Parliament-as-body sit below the meaningful-action floor; the corpus's
  non-MoH "delivered-vs-demanded gap" (Roman *repetundae* / Carolingian *missi* / HRE *Reichsexekution*
  / Han *cha ju*) is the universal fill giving all three real down-propagation.
- **Mandate of Heaven is history-only set-wide** — every collapse/collision/relief-valve recommendation
  is grounded on non-MoH precedent (Roman/Byzantine dual-trigger usurpation, Ottoman vizier-scapegoat +
  Janissary revolt, Roman recusatio/penance, Polybian regime-cycle as confirmatory-only).
