# Pessimist Subtractive NERS Audit — Lane Dossier: TW (Threadwork)

## Status: WORKINGS (read-only, Sonnet reconcile pass, 2026-07-08) — feeds the inverted critic + Fable-5 verdict
## Charter: `designs/audit/2026-07-08-pessimist-action-audit/00_grounding/00_charter.md`
## Criteria binding: `references/throughlines_meta.md` (N §0, Ω §1, Q §5, Failure Lexicon §7) — no new criteria invented.

---

## 0. Reconciliation — scope, sources, and the prose↔code object split

**Unit of analysis.** Seven player-available Thread operations, each a clean 1:1 doc↔code pair:
`attempt_leap` / `attempt_weaving` / `attempt_pulling` / `attempt_past_pulling` / `attempt_locking` /
`attempt_dissolution` / `attempt_mending` in `sim/thread/operations.py`, implementing
`designs/threadwork/threadwork_v30.md` §2.3 (Leap) and §2.4 (Weaving, Pulling, Past-Oriented
Pulling, Locking, Dissolution, Mending). Unlike PC/FA, **prose and code do not diverge into two
objects here** — operations.py's own header cites §2.3-§2.6 line-for-line and the seven entry
points map 1:1 onto the seven prose subsections. The reconciliation task for this lane is therefore
not "which menu is real" but "what do the *dispersed* canon layers (Foundations amendments, params,
module contracts, prior audits) say about what each operation is FOR, judged as if fully realized."

**Scoped out of the seven-action set (modifiers, not additional verbs):** §2.1 Approach Training
(a chargen/training gate — prerequisite infrastructure for Leap, not a scene-time verb of its own);
§2.5 Collective Operations and §2.6 Opposing Operations (both are *resolution modifiers* layered
onto the seven operations — an Anchor+Helper lattice or a contested-intentionality table — not new
player verbs); "Community Organizing"/"Community Weave" (params/threadwork.md — a Field-scale,
Revolution-Mandate-gated *variant of Weaving*, not a distinct coded entry point). These are folded
into the relevant operation's analysis below rather than verdicted separately.

**Dispersed sources reconciled per action below:**
- `designs/threadwork/threadwork_v30.md` §2.1–§2.6 (prose spec, PP-616/618/619/622/623/624/625/632)
- `params/threadwork.md` (canonical Three-Axis Ob, TN table, Knot Mechanics ED-912)
- `canon/02_foundations_amendment_leap_mechanism.md` Amendments 1–5 (the *structural why* — Leap's
  suspension target, the restorative/manipulative/destructive operation-type taxonomy that is the
  actual mechanism behind Ω-d cost differentiation across all seven ops)
- `references/module_contracts.yaml` `threadwork` module block (the `scene.thread_operation` vs
  `meta.thread_woven` Key-naming mismatch — an [OPEN — Jordan] wiring/registry question, cited
  below only as routing metadata, never as a verdict input per the cardinal rule)
- Prior audits: `designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_threadwork.md` (T1
  Mending-cost contradiction, T2 FR-surcharge contradiction, T6 Knot-tier contradiction — all
  canon-contradiction findings, not subtractive ones); `designs/audit/2026-07-04-ners-qualitative-
  audit/01_workings/hunts/hunt_threadwork_exploit.md` (LINE 1 "homeless cap" ED-1010, LINE 2 Mending
  dominance, LINE 3 Weave-as-Domain-Action parallel economy, LINE 4 Coherence-regen loop);
  `.../00_grounding/03_threadwork_surface.md` (RATIFIED juncture map, open ED list); and
  `designs/audit/2026-07-07-unaddressed-areas-audit/resolution_plan_v1.md` (§3 Threadwork/knots/
  fieldwork row — confirms **ED-871 already ratified Mending's Coherence cost as 0**, propagated
  to `threadwork_v30.md` §3.2's prose; `operations.py` code sync is the tracked residual C-TW-2/
  Stratum A item — build-state, not consulted for the verdict below).

**Cross-cutting context that bears on every action's Ω-d judgment (not itself an action):** the
"homeless cap" (ED-1010, hunt LINE 1) — the per-operation Coherence cap is asserted in prose
(threadwork §3.2 PP-196 note, mass_battle §A.10 line 533) but the actual Coherence-cost tables
(threadwork §3.2, mass_battle §A.10) charge scale-graduated costs up to −2 (Structural). **As-if-
built, this matters to every non-Mending operation below**: if Jordan resolves ED-1010 toward "flat
−1 cap regardless of scale," the core threadwork decision ("how deep do I dare go on my Coherence
budget?" — named the lane's central decision in the RATIFIED `03_threadwork_surface.md` §1) goes
Ω-d-flat for Weaving/Pulling/POP/Locking/Dissolution alike. If resolved toward "the scale table
governs, cap is stale prose to strike," the decision survives. This is KNOWN-TRACKED (P1, ED-1010)
and not re-litigated as a fresh finding per action; it is flagged once here as the single biggest
swing-variable in whether five of these seven actions clear Ω-d as designed.

---

## 1. Leap — Suspending Rendering (`attempt_leap`, §2.3)

**Design intent.** The entry gate: a practitioner (TS ≥ 30, Approach Training) suspends ordinary
rendering (layer 2) to access the substrate directly (layer 3, canon/01 Amendment 2). Every other
Thread operation is downstream of a successful Leap. Mechanically it is a commitment roll with its
own failure cost (−1D Thread Pool Score for the scene) and its own success ladder (Overwhelming
discounts the *next* operation's Ob).

**As-if-built contribution.** This is the single most load-bearing piece of the lane: it is the
mechanical instantiation of the game's central metaphysical claim (Thread substrate as literal
second layer of reality, canon/00 §4.3/§5.3) and the only point where a *mundane-vs-supernatural*
decision is made explicit — a player chooses to spend Focus/Fatigue and risk a scene-long Thread
Pool debuff to attempt Thread engagement at all, when a conventional (combat/social/investigation)
action was also available. That is a real N-grounded, Ω-a/Ω-d-qualifying choice, not flavor.

**N.** Passes. Not fantasy imposition — it *is* the substrate ontology (Μ-γ), the load-bearing
mechanism the entire lane's Renaissance-leadership-through-hidden-forces premise depends on.
Not duplicate/abstractable — nothing else in the corpus models "commit to supernatural engagement,
pay a cost even on failure, gain the option-space of six further verbs on success."

**Ω.** (a) Cross-scale: yes, contact is the precondition for every cross-scale Thread consequence
downstream. (b) Personal transformation: yes — TS gain on Overwhelming, permanent Coherence risk
downstream, the "one-way descent toward Rendering Crisis" arc (§3.3) begins here. (c) Autonomous:
NPC/Threadcut-being Leaps are canon-supported (Thread-Warfare doctrine, Threadcut Beings §6) —
the substrate doesn't wait on the player. (d) Non-dominance: the failure cost (−1D TPS for the
scene) is real and the Wound-disruption-during-contact check (Spirit TN7 Ob1) means a Leap can be
undone by ordinary physical harm — it does not trivially convert into "free access."

**Q.** Robust — three approaches to any Thread-adjacent situation genuinely exist (conventional
action / Leap-and-operate / decline and let autonomous world-state resolve it); dramatic legibility
is intact (whose rendering is at risk, what the practitioner is trying to access, what happens if
they don't try — the Leap failure framing prose (line 173) states this explicitly as *designed-in*
legibility). Smooth — methodology matches every other Thread op (same pool formula, TN7). Elegant —
"roll to suspend; success lets you act, partial makes the next act harder, failure dulls you for
the scene" restates in one read.

**Verdict: KEEP.** Passes N + Ω + Q under attack. No subtractive trigger fires.

---

## 2. Weaving — Things Cohere (`attempt_weaving`, §2.4)

**Design intent.** The constructive/consolidating operation: closing wounds, reinforcing
agreements, raising a faction's Stability, permanently reinforcing an institution — scaled Object
→ Structural. Canon/02 Amendment 3 classes non-restorative Weaving as **manipulative** (imposing a
configuration the substrate would not resume on its own) — it pays Coherence proportional to scale
and duration-held, unlike Mending.

**As-if-built contribution.** Models a genuinely Renaissance-load-bearing dynamic: a leader (or
practitioner acting for one) *imposing* stability/agreement/reinforcement that the situation's own
momentum would not otherwise produce — patronage networks, forced consolidation, engineered trust.
Distinct from Pulling (its structural inverse) and from Mending (restorative-only, gated to
Gap/Shifting-Object/Locked-Zone targets — Weaving can target *any* live configuration, Mending
cannot).

**N.** Passes — not duplicate of Pulling (opposite direction) or Mending (different target class
and alignment). Over-actualisation hazard (Relational+) and cumulative Overweave Ob give the
operation its own distinct failure/hazard shape.

**Ω.** (a) Cross-scale: explicit — Territorial-scale Weaving raises faction Stability and fires
positive/negative Domain Echo (Mandate ±1, `scale_transitions_v30` §5.6) depending on territory.
(b) Personal: TS gain on Overwhelming. (c) Autonomous: over-actualisation persists and decays on
its own clock regardless of further player action. (d) Non-dominance: **flagged, not failed.**
Hunt LINE 3 (KNOWN-UNTRACKED, P2): at Territorial scale, a practitioner-leader's Weave *is* the
faction Domain Action (`scale_transitions §3.5` — "No extra roll — the Thread operation IS the
faction action"), consumed for free alongside the Weave's own effect and a possible Mandate bonus,
for one roll and one Coherence cost. This makes the conventional Domain-Action economy strictly
worse *for a practitioner-leader specifically*. The hunt's own counterweight holds under
as-if-built scrutiny: Church-territory Domain Echo flips negative, Gap/Dissolution risk exists on
the same roll, and the option is TS 50+/Approach-Training-gated — a real decision survives (when to
route power through Thread vs conventional Assert), it is not a strict no-brainer. This does not
clear the Ω-d bar to a CUT/PRUNE, but it is a genuine finding this dossier surfaces as material to
the existing ED-673-propagated mechanism's *non-dominance* question, which — per `03_threadwork_
surface.md` §5 — remains unflagged in the ledger proper.

**Q.** Robust/Smooth/Elegant all pass — the core rule ("degree of success sets whether the
configuration holds, calcifies, or collapses; deeper scale = harder and stickier") restates in one
read; the over-actualisation table is an enumerated elaboration, not a hidden special case.

**Verdict: KEEP.** Ω-d caveat (parallel-economy at Territorial scale) noted as an ordinary finding
— it does not retire or shrink any resolution-plan item on its own; it sharpens the existing
ED-673/`03_threadwork_surface.md` §5 non-dominance gap that Jordan should weigh when that mechanism
is next touched.

---

## 3. Pulling — Things Open (`attempt_pulling`, §2.4)

**Design intent.** The releasing/opening operation — the mirror of Weaving. Loosens an actualised
configuration: reopening a closed negotiation, cracking a fortification's psychological hold,
undoing an imposed consolidation. Canon/02 Amendment 3 classes non-restorative Pulling (aimed at
opening rather than tearing) as manipulative.

**As-if-built contribution.** A real, distinct Renaissance-adjacent dynamic — undoing what Weaving
(or history) has consolidated. Complementary, not duplicate, to Weaving; distinct from Locking
(freezing) and Dissolution (tearing) by the Lock-vs-Dissolution summary table's own terms (line
432-441) and from Mending by target class.

**N.** Passes.

**Ω.** (a) Cross-scale: Fortification-Ob addition (R-67) ties Pulling directly into the territory/
settlement layer. (b) Personal: Failure costs a Wound (snap-back) — a direct personal stake.
(c) Autonomous: duration-by-surplus-successes means a Pull's effect can lapse on its own clock,
independent of further player action. (d) Non-dominance: real — failure has teeth (Wound + MS −2 +
Coherence −1), success is bounded in duration unless margin is high.

**Reconciliation note (not verdict-driving):** the duration table has two co-present, contradictory
versions in the prose (the original "0/1/2+ surplus" ladder at lines 330 and the "R-54 correction"
ladder immediately below it at lines 332-337) — a stale-superseded-text editorial defect of the
same shape as the Mending-cost T1 contradiction already tracked. Judged as-if-built (i.e., assuming
the R-54 correction — the more recently authored, explicitly-labeled "correction" — is what ships),
the mechanic is coherent and elegant. This is an ordinary editorial-ledger candidate, not a
subtractive finding against Pulling itself.

**Q.** Passes — one-read restatable ("open it; the more you beat the Ob by, the longer it stays
open"), matches Weaving's methodology (Q-smooth), duration ladder is the only external dependency
and it is enumerated (once the doc's two co-present versions are reconciled).

**Verdict: KEEP.**

---

## 4. Past-Oriented Pulling (`attempt_past_pulling`, §2.4 subsection)

**Design intent.** Pulling aimed at a *past* configuration rather than a currently-actualised one —
reaching into history: reopening an old grievance, contesting a historical claim, accessing a
moment already closed by time rather than by an opponent's Weave. TN 8 (vs 7), Ob keyed to
*recency* (Same-scene=3 … 10+ seasons=7) rather than to actualisation-level, plus an active-Knot-
Crisis +1 Ob modifier (grief-in-progress makes a thread harder to reach) and an additional −1
Coherence surcharge.

**As-if-built contribution.** The recency axis and the Knot-Crisis modifier point at something
genuinely distinct in kind from standard Pulling: Renaissance-era political leadership is
*saturated* with appeals to precedent, contested lineage, unresolved historical grievance, and
"living sorrow… woven into the thread's current configuration" (line 365) as a real political
force. That is not the same dynamic as "loosen something that is currently holding."

**N — the pessimist case for Abstractable.** Held against every other axis, though, POP is
mechanically near-identical to Pulling: same pool formula, same `_resolve_operation` degree table,
differing only in (i) which Ob-lookup table is consulted and (ii) TN+1 and (iii) one extra −1
Coherence. The code's own header comment documents this convergence explicitly ("TPS÷2 struck; full
TPS always; TN+1 already encodes temporal-depth difficulty") — a patch history (PP-619/624/625) of
*progressively collapsing* what was once a more differentiated operation into "Pulling with a
different Ob-table and TN+1." Compounding this: `params/threadwork.md`'s canonical **Three-Axis Ob
System** (Depth × Breadth × Distance, PP-622/623) — the system that superseded every other
operation's old single-axis Ob table — has no temporal/recency axis at all; `Distance` is
explicitly spatial ("how far from practitioner's body," line 92). POP's recency table sits entirely
outside the canonical Ob architecture that governs the other six operations. As-if-built, a player
does not experience POP as "a fourth Ob axis added to the framework everyone else uses" — they
experience it as a bolted-on, parallel Ob system that happens to share Pulling's resolution shell.

**Ω.** (a)/(b)/(c) all pass on the same grounds as standard Pulling, plus the distinct grief/legacy
angle. (d) Non-dominance holds (TN 8, extra Coherence cost, recency-driven Ob scaling to 7 at the
top end).

**Q — the deciding factor.** Q-smooth explicitly asks for "external dependencies enumerated" and
"methodology matches governing subsystem." POP's Ob methodology does **not** match its own
governing subsystem (the Three-Axis system that the rest of the lane uses) — it is a fourth,
uncoordinated axis with no stated interaction rule (does a POP target also carry Depth/Breadth Ob?
Silent). That is a genuine Q-smooth failure, and combined with the N-level Abstractable signal
(mechanically ~95% identical to Pulling, differing only in a table lookup and a flat TN/Coherence
delta), the honest pessimist reading is that POP does not yet earn a *structurally separate*
operation slot — the temporal-target concept is real and worth keeping, but it should be a
**target-type parameter on Pulling** (feeding a recency-based Ob contribution the way Distance
feeds a spatial one) rather than a sibling operation with its own disconnected Ob table and a
second TN tier.

**Verdict: DISTILL.** Fold Past-Oriented Pulling into Pulling as a temporal-target variant governed
by an explicit fourth axis (or a Distance-axis reinterpretation for temporal targets) inside the
canonical Three-Axis Ob System, rather than a separately-TN'd operation with a parallel,
un-integrated recency table. The underlying capability (reach into the past; grief/legacy as
political weight) is not cut — it is preserved and simplified into the one system every other
operation already uses.

**Retires/shrinks downstream:** `resolution_plan_v1.md` §3 Threadwork row **C-TW-3/4/10/11**
("un-invert the POP cap" among other per-op cost-table work, Stratum B, lane WR) — folding POP into
Pulling's own Ob axis collapses "fix POP's separate cap/Ob machinery" into "extend Pulling's single
Ob axis," shrinking that Stratum B item's scope rather than requiring a parallel POP-specific fix
track.

**Intent gate: DELIBERATE.** POP's separateness is the product of multiple named patches
(PP-619/624/625) iterating *on purpose* — this is a considered design choice being second-guessed
on merit, not an accidental gap. Routes to Jordan as a design-merit call, not to the additive plan.

---

## 5. Locking — Unable to Become (`attempt_locking`, §2.4)

**Design intent.** Freeze a configuration against change — arrest a succession, impose a durable
stasis on a rival institution, hold a site in stasis pending Einhir-framework work. FR (Forced
Resolution), TS 50+ required, TN 8, cap-exempt FR Coherence surcharge (PP-196).

**As-if-built contribution.** A real Renaissance-adjacent dynamic: sieges-as-stasis, forced
gridlock, interdicts, arresting a rival's momentum rather than destroying it outright. Chronic
(damage accumulates over seasons) as opposed to Dissolution's acute character — the Lock-vs-
Dissolution summary table (line 432) makes the two operations' distinct shape explicit and
non-overlapping.

**Ω.** (a) Cross-scale: chronic MS drain and the "+1 Ob to operations targeting configurations
adjacent to the Lock" effect ripple through the territory/faction layer over seasons, independent
of further player action (c). (b) Personal: TS gain on Overwhelming only; the operation is mostly
world-track — the personal-transformation clause is thin here relative to Leap/Dissolution, but
Ω-b does not require every operation to carry it equally; the lane's personal-transformation weight
sits primarily on Leap/Coherence and Dissolution's catastrophic-failure branch. (d) Non-dominance:
strong — Locking can become a **permanent Locked Zone** (an irreversible, chronic liability the
faction/territory layer must live with forever), and failure costs 2 Wounds plus a spreading +1 Ob
penalty. This is a genuine "cheap now, expensive forever" trade, not a free action.

**Q.** Elegant — "freeze it; cheap immediately, drains the world every season until reversed or it
goes permanent" restates in one read. The reversal-Ob formula (`(target TS÷10 round up) − 2, min 1`)
is a single stated formula, not a hidden exception.

**Conditional caveat (not verdict-changing, cited once in §0):** Locking's Ω-d case depends on the
ED-1010 "homeless cap" resolving toward the scale-graduated cost table (not a flat −1 cap) — under
the flat-cap reading, the FR-surcharge-cap-exemption's *point* (that Structural/Foundational Locks
should cost meaningfully more than Object/Personal ones) is undercut. KNOWN-TRACKED, not re-raised
as a new finding.

**Verdict: KEEP.**

---

## 6. Dissolution — Unable to Be (`attempt_dissolution`, §2.4)

**Design intent.** Tear a configuration out of existence entirely — raze an institution, sever a
bloodline's claim, destroy rather than merely arrest. FR, TS 50+, TN 8. Canon/02 Amendment 3 classes
this as **destructive** (the most severe category — "feedback through the knot is catastrophic").

**As-if-built contribution.** The lane's highest-stakes verb, and its distinctiveness from Locking
is explicit and mechanical, not just flavor: Dissolution is acute (immediate, no drift) vs Locking's
chronic drain; it always risks a Gap (Locking risks stiffening only on failure); failure produces a
**Monstrous Incursion** and practitioner Incapacitation outright, categorically worse than Locking's
worst case. This is a real, distinct "burn it down" option with commensurately catastrophic risk —
precisely the kind of irreducible tradeoff Ω-d asks for.

**Ω.** (a) Cross-scale: Gap formation feeds `calamity_radiation_v30.md`'s geographic consequences —
a Dissolution's failure state is not contained to the scene. (b) Personal: Incapacitation on
failure is a direct, severe personal stake. (c) Autonomous: an unclosed Gap persists and threatens
Monstrous Incursion independent of further player action; Gap self-closure (params §Gap
Self-Closure by Scale) proceeds on its own clock. (d) Non-dominance: unambiguous — even the *best*
outcome (Overwhelming) costs more MS than Locking's *best* outcome, and the failure branch is the
single most catastrophic result in the entire operations table. No hunt or prior audit flags
Dissolution as dominant or under-costed; it is the one operation whose cost structure needs no
defense.

**Q.** One-read legible ("tear it apart; a Gap always forms; failure is catastrophic") — matches
Locking's methodology by deliberate contrast (the summary table exists precisely so the two read as
a matched pair, satisfying Q-smooth's "matching neighbor" test).

**Verdict: KEEP.** Cleanest pass in the lane — no caveat required.

---

## 7. Mending — Repairing the Substrate (`attempt_mending`, §2.4)

**Design intent.** The sole restorative operation: repair a Gap, Shifting Object, or Locked-Zone
border. Canon/02 Amendment 3 makes Mending's zero Coherence cost a **structural, not incidental**
consequence of alignment with substrate tendency — restorative work "does what the constitutive
spooling would do, granted sufficient time." This asymmetry is philosophically load-bearing (it is
the mechanical expression of the Edeyja's lifetime-Mending capacity and the Church's category error
in persecuting Wardens alongside manipulative/destructive practitioners, canon/02 Amendment 5) and
has been explicitly ratified: ED-871 fixed the long-standing §3.2-vs-§2.4/canon contradiction (T1,
`ners_verdict_threadwork.md`) in favor of **0**, already propagated into `threadwork_v30.md` §3.2's
prose (`resolution_plan_v1.md` §3, ED-WR-0005/OPT-5).

**As-if-built contribution.** A real, thematically essential dynamic: legitimate restoration/repair
of institutions and relationships as categorically different from — and cheaper than — imposing or
destroying them, mapping onto a genuine Renaissance-era distinction (restorative governance vs.
revolutionary rupture). This is not in question; it should not and does not get cut.

**N.** Passes cleanly — unique target class (only op that can touch a Gap/Shifting-Object/
Locked-Zone-border), unique philosophical grounding, no duplicate coverage.

**Ω — where the pessimist case bites.** (a) Cross-scale: yes, explicit — Territorial+ Mending
Success fires positive Domain Echo (controlling faction Mandate +1, `scale_transitions §5.6`).
(b) Personal: TS gain on Overwhelming. (c) Autonomous: Gaps arise from autonomous world events
(Calamity, other practitioners' Dissolution failures) independent of player action, giving Mending
something to do regardless of player choice. **(d) Non-dominance — fails as designed, within its
own lane.** Per hunt LINE 2 (confirmed, not merely surfaced, by ED-871's now-ratified zero-cost):
for any Gap/Shifting-Object/Locked-Zone-border that needs repairing, Mending is (i) Coherence-free,
(ii) explicitly **unopposeable** (`params/threadwork.md` Mending Immunity — "cannot be opposed"),
(iii) the *only* operation that can legally target these configurations at all (Weaving/Pulling/
Locking/Dissolution do not touch Gaps), and (iv) RS/Mandate-positive on top. The brakes that exist
— Seasonal Mending Fatigue (+1 Ob per consecutive Mend, resets each season) and the requirement
that a qualifying target exist — are opportunity-cost/scarcity brakes, not cost brakes, and the
hunt's own assessment (medium-high confidence) calls both "soft."

**Q-robust — the sharper diagnosis.** The Q-robust test asks for "three viable player approaches to
any situation the mechanic governs." For "a Gap exists and needs addressing," the honest answer is
there is exactly **one** legal repair tool (Mending itself, solo or collective), plus "leave it and
let Gap Self-Closure run its clock" (a real but strictly worse alternative — it costs ongoing RS
drain the whole time it's open, per `params §Gap Self-Closure by Scale`). That is not three viable
approaches to the *same* goal; it is one tool and one "do nothing, pay drain" fallback. Framed this
way, the finding is less "Mending is a dominant strategy among competitors" (there are no
competitors for its target class, so Ω-d's "pays what it buys relative to alternatives" framing
does not quite fit a monopoly) and more a **Q-robust mono-solution** problem: the single most
world-track-consequential decision point in the lane (whether/when/how hard to repair the
substrate) has no real branching once a Gap exists — only a timing question.

**Verdict: REFINE.** Do not touch the zero-Coherence-cost ruling itself — it is canon-grounded
(canon/02 Amendment 3), Jordan-ratified (ED-871), and cutting or taxing it would break a
philosophically load-bearing asymmetry the whole restorative/manipulative/destructive taxonomy
depends on. The REFINE target is narrower: **give Gap-repair a second legal branch or a real
scarcity/opposition dimension** so the Q-robust three-approaches bar is actually cleared — e.g. an
opposeable variant in contested/Church-adjacent territory (Mending Immunity currently blocks this
categorically), or making the "leave it, let it self-close" branch a genuinely competitive choice
(RS-drain tuning) rather than a strictly dominated one. This is a design-iteration ask, squarely
Jordan's call per the framework's own Ω-authority line (§10), not a mechanical inevitability this
dossier can resolve.

**Retires/shrinks downstream:** `resolution_plan_v1.md` §3 Threadwork row **C-TW-2** ("Execute
ED-871: cost 0 in §3.2 + operations.py; Mending exits the blanket penalty," Stratum A, lane WR).
This finding does not undo ED-871's zero-cost ruling, but it recommends that C-TW-2's remaining
code-sync work be paired with an explicit Q-robust/friction ruling (rather than a blind "set to 0
everywhere" propagation) — narrowing what "done" means for that Stratum-A item from a pure
number-sync to a number-sync-plus-branching-ruling.

**Intent gate: DELIBERATE.** The zero-cost/unopposeable shape is a conscious, doubly-ratified
design choice (canon/02 Amendment 3 + ED-871), not an accidental gap — this is a design-merit
challenge to a deliberate choice, exactly the kind of call this audit exists to make, and it is
explicitly NOT a recommendation to change the cost value itself.

---

## Lane summary

Six of the lane's seven verbs (Leap, Weaving, Pulling, Locking, Dissolution, and — with a REFINE
flag — Mending) are structurally sound as-if-built: each occupies a distinct, N-grounded niche in
the restorative/manipulative/destructive taxonomy that is the lane's actual organizing principle,
each carries a real, non-trivial cost or catastrophic-failure branch (Dissolution is the cleanest
pass in the corpus-wide sweep so far), and each restates in one read. The lane's one clear
subtractive candidate is **Past-Oriented Pulling**, which — despite modeling a genuine and
worthwhile "the past's grip on the present" dynamic — has been patched (PP-619/624/625) into a form
that is mechanically ~95% identical to standard Pulling, riding a temporal Ob-axis that was never
integrated into the Three-Axis Ob System every other operation now uses; it should fold into
Pulling as a target-type variant rather than persist as a structurally separate, un-integrated
sibling operation. **Mending** earns a REFINE rather than a KEEP or a CUT: its zero-cost/unopposeable
shape is philosophically load-bearing and correctly ratified (ED-871), but the lane's single most
consequential world-track decision point (repair a Gap) currently clears N and most of Ω while
failing the Q-robust three-approaches bar — a design-iteration ask on the *branching*, not the
*cost*. Two cross-cutting, already-tracked items (the ED-1010 "homeless cap" and the Weave-as-
Domain-Action parallel economy, hunt LINE 3) condition several verdicts' Ω-d margins without
themselves warranting a fresh subtractive verdict.
