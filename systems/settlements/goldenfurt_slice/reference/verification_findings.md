# Goldenfurt Slice — Adversarial Verification Findings

**Source:** 4-lens adversarial workflow (deck-balance · NPC-collision · churn-integrity · sim-completeness), 2026-06-23. Four independent skeptics each tried to *break* the authored slice.
**Result:** 32 findings — 15 high, 12 medium, 5 low. The slice's spine holds, but the adversarial pass found real defects: a mis-signed Π term, an all-cost mandatory vise (G201), a recall death-spiral (G606), and several deck-referenced fields the sim spec never models.
**Status key:** ✅ fixed in this commit · ⏳ v1.1 backlog (needs real design revision, fix recorded below).

---

## High (15)

| id | where | defect (short) | fix | status |
|----|-------|----------------|-----|--------|
| CG-1 | sim §5 pressure.py | Π decay term `- decay_toward(3)` only pulls **down** → pins toward 0 when Π<3, contradicting anti-stall + the README "Π→2" trace | bidirectional restoring term `sign(3-Π)·min(1,|3-Π|)` | ✅ |
| sim-F1 | sim §1 dataclass | deck triggers on `directive==Extract/Tax/Host` but `Settlement` has no directive field | add `active_directive` field, set at season open | ✅ |
| sim-F2 | sim §1 | Geneva arc hinges on `religious_building==Chapel`→`Church` but no such field | add `religious_building` field; G603 mutates it | ✅ |
| sim-F3 | sim §1/§4 | `Church Attention` is load-bearing (G203 trigger, drives Suppress Directive) but modeled nowhere | add `church_attention` field + Suppress path | ✅ |
| sim-F5 | sim (none) | faction-emergence Stage 2→3 progress is the slice's payoff (G303/G601/G606) but untracked | add `governor_emergence` counter | ✅ |
| sim-F7 | sim §1 | Treasury spent all over the deck (G103/G301/G402) but no field/draw rule | `treasury_source` delegates spend to `world.factions[owner]` | ✅ |
| sim-F9 | sim §5/§1 | Π sums `Σ_unserved_needs` but nothing persists drawn-but-unserved Needs | add `open_needs` list; Π reads the remainder | ✅ |
| CG-3 | sim §4 | Directive fallback `none` → a dead world→player season (the one mandatory move skipped) | remove "none"; always emit a low-stakes Directive | ✅ |
| deck-F1 | deck G201 | War-Levy has **zero Π-delta** on any branch (violates the deck's own invariant) + all-cost mandatory vise | add Π deltas (Comply −1 / Defy +1) | ✅ |
| CG-6 | deck G201 / README | Comply branch carries no Π delta on the most-played path | same G201 fix; audit other Comply branches | ✅ (G201) / ⏳ (audit G202/203/205) |
| CG-5 | README L69 | coherence self-check overclaims "every card has a Π-delta+Ledger" — untrue of the 21 compact rows | downgrade ✅→⚠ with honest scope | ✅ |
| npc-F1 | npc G06 Konrad | suspicion track is purely reactive — a **compliant** player never advances Konrad (dead world→player) | add player-independent advance (under-quota / RM-Presence rise) | ✅ |
| deck-F2 / CG-7 | deck G606 | **recall death-spiral** — the celebrated "defy to protect the town" path ratchets Konrad to recall; escapes need pre-banked tags | added a `Submit to audit` escape (always available, −2 suspicion) + Konrad capped +1/season | ✅ v1.1 |
| deck-F3 | deck G204 | Curate's Offer is a genuine **no-acceptable-out vise** — every branch raises Π or feeds the near-irreversible G603 | added `Keep Order: Consent` (secular relief); Decline now Π-neutral | ✅ v1.1 |
| deck-F5 | deck G602, G605 | Ambition cards don't branch on prior player choices → no payoff-for-play | G602/G604/G605 given by-state forks (`Precedent:toll-capped`→charter void, etc.) | ✅ v1.1 |
| npc-F2 | npc G04 Tomas | unmovable/unreachable in a well-governed town (only discovery is chronic disorder) | added a Reachability path: Old Brun → Investigate surfaces Tomas at any Order | ✅ v1.1 |
| npc-F3 | npc G05 Greta | ambition escalates on force but **not on neglect** (static if ignored-without-suppression) | added a blocked-by-neglect branch (deeper-covert cell-export; she never stalls) | ✅ v1.1 |
| sim-F4 | sim §5 predicates | grammar too weak for event-history triggers (`Investigated(Tomas)`, `ruled against Orsk`) | require those cards to drop a history/Leverage tag; triggers read `has_tag(...)` | ⏳ |

## Medium (12) — mostly ⏳ v1.1 (deck-F4, CG-4, sim-F6 fixed this commit)

- **deck-F4** ◑ *partially fixed* — G201 Bargain no longer raises suspicion (its whole point vs Defy); G204 Bargain now grants a unique `Leverage:parish-favour` chit. G202 Bargain still to differentiate.
- **deck-F6** G401 riot: the only no-cost Π-release (`Hedda mediates`) is gated on `Hedda.Disp≥+2` but the trigger needs `Grudge:Hedda OR Grudge:Mertha` → can lock out the release; widen the gate or add a Force-branch Π-release.
- **npc-F4** Wessel-vs-Greta collision is mechanically empty (no verb forces the tradeoff) → author a Sponsor/Hold-Court card that raises one and lowers the other.
- **npc-F5** decorative Knots (Tomas→Brun, Wessel→Aldith, Hedda→Aldith) never referenced by a card → wire each to a card or cut.
- **CG-4** ✅ *fixed* — G605 now has `Tolerate` vs `Disperse by force` player branches with Ledger writes + Π deltas.
- **CG-5b** expand the compact Ambition rows G602/G603/G604 to full response schema so they satisfy the churn triple.
- **sim-F6** ✅ *fixed* — renamed the G204 weight clause to `Wessel.progress` (matching the runtime accessor).
- **sim-F7b** decide Treasury draw location explicitly (done via `treasury_source` ✅, but Sponsor/relief read-rule still needs spec).
- **sim-F8** `social_contest(§7)` is a dangling ref (§7 here is the build sequence, not social contest) and absent from the build → wire `social_contest_v30 §7` into `governance.py` (add build step).
- **sim-F10** dependency order: §7 S4 (deck engine) needs §6/S5 ambition runtime for the forced-queue → land the `deck_state['forced']` interface in S4; add an anti-stall test.
- **F11** G505/G606 read NPC boolean/relationship flags (`Wessel.informer-active`, `Hedda allied`) with no accessor → model as Leverage tags; derive `allied` from `has_tag(Debt,'hedda-owes-you')`.
- **F12** succession survival is load-bearing but `succeed_governor` isn't in the build/file list and TTL durability is untested → add it + a clears-vs-preserves test.

## Low (5) — all ⏳ v1.1

- **deck-F7** G201 has no cooldown → a permanent-war Crown could spam it and starve G301; add a cooldown / one-Extract-per-N cap.
- **npc-F6** α/β ethic tags are flavor — no card or tick reads `npc.ethic` → make at least one resolution branch on ethic.
- **CG-7** (folded into deck-F2) slow Konrad (require Defy not Bargain for +1) or add a suspicion-bleed response.
- **F11b** NPC flag accessors (see medium F11).
- **F12b** succession test coverage (see medium F12).

---

## Verdict

The adversarial pass confirms the **architecture is sound** (the central Hedda/Orsk rivalry, the two-stroke loop on the spine cards, the registry design) but the **content has real balance and completeness gaps** — concentrated in (a) the Directive/suspicion subsystem being a one-way ratchet, (b) the Geneva-trap card being a true vise, (c) the compact Ambition rows under-delivering payoff-for-play, and (d) the sim spec missing ~7 fields the deck references. The clear bugs and missing fields are fixed in this commit; the design-revision items are tracked above for v1.1.
