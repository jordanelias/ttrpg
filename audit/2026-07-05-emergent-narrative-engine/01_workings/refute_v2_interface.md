# Adversarial refutation — v2 §5 (claim-grammar interface) + §2 (generator) on INTEGRATION-REALITY

## Status: working record (adversarial skeptic pass, 2026-07-05, Lane IN). Not canonical.
Target: `narrative_engine_design_v2_churn.md` §5 + §2. Question: do these stay an INTERFACE, or do
they reach into SC-lane resolution mechanics / require undeclared substrate / assign the SC lane
work it never accepted / break "grammar-closed"?

Sources cross-checked: v2 §2/§5/§7/§9.3/§10; `spec/churn_amendments.md`; `spec_sections/s4_substrate.md`;
`handoffs/HANDOFF_SC.md`; `sim/personal/contest/{armature,rhetoric,dictionaries}.py`;
`params/contest.md`; `designs/scene/social_contest_v30.md`; `references/arcs/*`;
`references/module_contracts.yaml`; `01_workings/dossier_combinatorial_census.md`.

---

## What is genuinely well-integrated (calibration, credit where due)
- `evidence{key_ref, witnesses, chain_strength, recency, asserter_standing}` DOES map onto existing
  substrate: `key_ref`→Key; `witnesses`→`targets[]`/visibility; `chain_strength`→`causes[]` depth;
  `recency`→season stamp; `asserter_standing`→the live CR3 Face/Standing tracker. This one object is
  substrate-backed.
- The Gate-C **δσ leverage channel** (`armature.py`, CR6: "setup advantages … accumulate as δσ, tanh
  soft-capped, uniform probability impact") is a genuine, extensible home for an evidence-weight
  setup advantage. CR6 already lists "corroboration" (PP-257 Corroboration Knot is real). So §5 is not
  baseless — evidence-weight-as-δσ has a plausible clean insertion point.

The refutation below is therefore about OVERSTATEMENT and UNDECLARED DEPENDENCY, not "impossible."

---

## FINDING B — HIGH — commitment-store falsely claimed to "already exist in the contest system"
§5: "The move half **already exists in the contest system** (appeals …, CR4, the armature, Doubt/CR5,
**and the commitment-store concept from its source-research trilogy**)."
- `HANDOFF_SC.md` (SOURCE-RESEARCH GROUNDING, 2026-07-01): the commitment-store is
  **READ-AND-CITED-BUT-NOT-APPLIED** — it "shaped the plan's … commitment-store … *shape* via
  critique.md, but its rich detail … **is not yet in the code**."
- Grep of `sim/personal/contest/`: no commitment store. The only "commitment" hits are
  `_kernel_tests.py:835/842` "**design-table** commitment" (a different sense — a design intent
  placeholder, "resolver does not yet consume orientation").
- It is not scheduled: Stage 4 (the four games) reads the trilogy for `liberum veto`/Dowlen/Putnam;
  no stage owns "build a commitment store."
=> §5 lists a non-existent, unscheduled mechanic among things that "already exist," then builds
   §9.3's hypocrisy payoff ("the defense NPC's claims enter his commitment store") on it.
REQUIRED_FIX: strike "already exists"; reclassify commitment-store as a **PROPOSED SC-lane
deliverable** and either schedule it in workplan v6 or drop the hypocrisy-callback claim (§5, §9.3, §6
"commitment stores make an NPC's hypocrisy a discoverable fact").

## FINDING C — HIGH — precedent{} + commitment{} require NEW stores no substrate section declares
§5 interface objects: `precedent{verdict_key, matter_class, adjudicator, season}` and
`commitment{speaker, claim, contest_ref}`; §9.3 "**new precedent{...} object emitted** — future
debates cite it."
- `s4_substrate.md` §S4.1: the engine "introduces **exactly one owned store** and reads everything
  else"; its READS column lists Convictions/Beliefs/Scars/Coherence, `npc_memory`, Bonds/Knots —
  **no precedent store, no commitment store.**
- `churn_amendments.md` s4 new-engine-owned-state list: ensemble cache, `stake_horizon` /
  `convergence_candidate` / `foreclosure_countdown` / `option_distribution`, light ledger,
  projected-next-beat register — **no precedent/commitment store.**
- A verdict Key exists (`scene.contest_resolved` is emitted), but a Key in the log ≠ a
  **matter_class-indexed queryable precedent store**; `matter_class` is not an established payload
  field on the verdict Key.
- "Recall's precedent citation names a real prior adjudication" (§5) / "Recall's +2D" (§9.3): the
  Recall +2D bonus is **canonical params spec** (`params/contest.md:24`; `social_contest_v30:166` —
  "+2D when citing a specific, named, verifiable claim … Binary") but is **NOT in the contest kernel**
  (grep: "Recall" appears in the kernel only inside armature.py's CR6 quote). Today it is a binary,
  self-asserted, GM-adjudicated citation. §5 silently changes its qualification basis to "cite a
  verdict_key from a precedent store" — a resolution-relevant change to what counts as a valid Recall.
=> two of three interface objects need stores that neither the narrative-engine substrate nor the SC
   lane declares, plus a rewiring of Recall from self-assert to object-backed.
REQUIRED_FIX: §5 must name precedent/commitment as **new SC-lane-owned stores** (schema + owner +
lifecycle), add `matter_class` to the verdict Key, and state that Recall's qualification basis
changes (an SC-resolution edit). If the engine's §6 render reads these stores, add them to s4 READS.

## FINDING A/D/H — MODERATE-HIGH — "interface only / no contest redesign" understates ~4 new sub-systems
§5 asserts "**No contest redesign here**" and quarantines "how evidence weight enters the roll" to the
SC lane. But §5's *substance* pre-commits contest-internal mechanics:
- **Evidence weight** decomposed into witnesses/chain/recency/standing that make "the track move
  *because* the cited history is strong" — the live δσ input set (CR6) is exhaustively
  {genre-stasis affinity, audience boost, Recall, Face, corroboration, prep, commit-spend}; it has
  **no witnesses/chain-depth/recency term**. Honoring §5 requires ADDING ≥3 new δσ inputs. (standing
  already present; corroboration partial.) v2 §10 F-G concedes the "evidence-weight formula" is a
  fork — yet declares the FORM canonical while handing the SC lane the numbers; fixing the factor
  decomposition IS an SC-resolution-design call.
- **"bluster" as a weaker move class — priced, attackable** (§5, §9.3 step 4). The live kernel has no
  bluster move class and no move pricing; moves are Style×orientation resolved via
  CLASH/REINFORCE/CROSS/TIE + δσ. Introducing a new move class with a price and "attackability" is a
  new resolution primitive. §9.3's "**the armature makes it attackable**" is unbacked — the armature
  is a judge-aimed δσ μ-shift (`armature.py`), it has no attack-an-unbound-claim mechanic.
Net (redesign-in-disguise test): EXISTING math (CLASH/…/TIE, σ substrate, CR4 +1D, CR5 backfire, the
armature) does NOT change — so "no redesign" is *narrowly* true — but §5 commits the SC lane to ~4 new
sub-systems (evidence-weight δσ term; bluster move-class + pricing; precedent store + Recall rewire;
commitment store + hypocrisy-exploit) and pre-decides several of their shapes. "Interface only" is
misleading about net new work the SC lane never accepted (its live NEXT is Stage 4 four-games).
REQUIRED_FIX: relabel §5 from "interface contract, no redesign" to "requirements input that
**adds** four contest sub-systems"; enumerate them; defer their SHAPE (not just numbers) to the SC
lane; drop "the armature makes it attackable" or cite the actual mechanism.

## FINDING E — MODERATE — §5's rung grammar is a renamed partial projection of the live CR4 ladder
§5: "Fact-rung cites a witnessed Key; Definition-rung contests its classification; Quality-rung
warrants via the causal chain; Recall's precedent citation …"
- Live CR4 (`rhetoric.py`): stases FACT / DEFINITION / QUALITY / JURISDICTION (+ kernel
  CONSEQUENCE/FEASIBILITY). §5 renames three and assigns each a NEW evidence-binding behavior
  ("Quality-rung warrants via the causal chain") that the kernel does not carry (QUALITY→None
  primary genre, present-terrain; no causal-chain warrant behavior).
- §5 lists **Recall** as if a rung alongside the stases; Recall is a separate setup-advantage, not a
  stasis rung. §5 **omits** JURISDICTION (the Stay) and CONSEQUENCE/FEASIBILITY entirely, so its
  "claim = move × evidence binding" grammar does not cover the full live move space.
=> This is the ED-1083 §2 "grow a scale-local interface dialect (**shape divergence**)" guardrail: v2
   §5 grows a narrative-engine-local rhetoric vocabulary diverging from the SC lane's live stasis
   ground.
REQUIRED_FIX: express §5's rungs in the SC lane's live stasis-ground vocabulary
(FACT/DEFINITION/QUALITY/JURISDICTION/CONSEQUENCE/FEASIBILITY), cover all grounds, and flag per-rung
evidence-binding as NEW behavior for the SC lane to accept or reject.

## FINDING F — MODERATE — §2 "grammar-closed / no whitelist" contradicted by v2's own fork 7 + per-NPC EFFECT logic
§2: "Grammar-closed Key space … **no enumerated whitelist anywhere** (dissolving §0.4)"; anti-oatmeal
via "specificity from binding at instantiation."
- v2 §10 **retains fork 7**: "GM-judgment-irreducible ~15% (declare non-firing default)." Closure with
  a 15% hole handled by NOT firing = those arcs do not emerge — a content loss "candidacy universal"
  (§1) papers over.
- The census (`dossier_combinatorial_census.md §3.2`) is a **sampled** classification (24/138) and
  concedes "a residual ~5 arcs … don't fold cleanly."
- Register arcs whose EFFECT is bespoke per-NPC decision logic (trigger is bindable; effect is not a
  slot): **NPC-ARC-JAR** (Drift-3 flips a bespoke threat taxonomy: parliamentary=political/no-deploy
  vs direct-challenge=threat/auto-deploy); **ARC-S52 Feldhaus** (per-NPC utility with a qualitative
  tie-break: "avoids Church if any alternative produces comparable Wealth … coercive framing reduces
  value"); **ARC-S56 Lions' Table** (the SAME Coup Counter read two ways by authored faction
  philosophy — Deed Faction=3, Failure Faction=2); **ARC-S29 Cardinal Schism** ("the Cardinal whose
  portfolio creates most institutional friction" — max-friction selection); **ARC-P05** (census's own
  clock outlier, GM-judgment qualitative selection). Trigger-predicate × binding-slot templates do not
  capture these EFFECT decision procedures.
REQUIRED_FIX: qualify §2's "grammar-closed" to "grammar-closed **except the ~15% GM-judgment residue
(fork 7) + bespoke-effect NPC-ARCs**"; state how those arcs render (drop, author, or a bespoke-effect
escape hatch) rather than implying universal candidacy.

## FINDING G — LOW-MODERATE — scenario_authoring authoring-vs-runtime [OPEN — Jordan] under-flagged in v2 proper
§2/§7 make `scenario_authoring` the offline-compile home / data-pack producer.
- `module_contracts.yaml:744-758`: `scenario_authoring` `doc: null`, `resolver: manifest
  [ASSUMPTION] authoring-time event injection`, gap_note "**authoring-time vs runtime classification
  [OPEN — Jordan]**".
- `s4_substrate.md` §S4.4 resolves this by DEFAULT (compile=authoring-time, seeds runtime) with an
  ED-1094 flag. Reasonable — but v2's own §10 fork register does **not** list the scenario_authoring
  classification as a fork, and §2 states the compile-home flatly.
REQUIRED_FIX: surface the scenario_authoring authoring-vs-runtime [OPEN — Jordan] as an explicit v2
§10 fork (default = authoring-time), so it is not resolved silently under routine merge (CLAUDE.md §2).

## HUNT 6 (contradiction of v1 s4 as amended) — result
No direct ownership contradiction: v2 keeps precedent/commitment in the SC lane, not the engine. But
if §6's claim-grammar render ("accuse"; "enter his commitment store"; hypocrisy callbacks) must READ
those stores, **s4 §S4.1 READS is incomplete** (omits precedent/commitment) — a gap, LOW-MODERATE,
folded into FINDING C's fix.
