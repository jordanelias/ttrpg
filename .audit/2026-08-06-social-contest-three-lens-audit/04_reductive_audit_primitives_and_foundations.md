# Social Contest — Reductive Audit: Primitives and Foundations

## Status: PROPOSED — findings filed; several cuts collide with ratified items and need Jordan
## Date: 2026-08-06 · Lane: SC · ID: ED-SC-0026
## Mandate: prune · cut · consolidate · distil — at the primitive and foundation layer
## Method: two read-only Fable 5 lenses (kill-list · foundations) per CLAUDE.md §10; Opus synthesis;
## every new claim re-verified by the orchestrator against the working tree.

---

## §0 — The verdict

Six findings, in the order they should be acted on.

1. **Under our own ratified doctrine, playing a contest is currently strictly wasted attention.** This
   is the deepest result of the session and it was not in any prior document.
2. **The system has no foundational choice.** All three candidates for "the decision the player makes
   repeatedly" are unreachable, illegible, or foreclosed by canon.
3. **The irreducible primitive set is eleven.** Roughly forty things currently occupy that layer.
4. **The six-attribute character layer collapses to one scalar in the running game** — and the fix is
   one line, or the attribute table should be deleted.
5. **Twenty-four named contest configurations reduce to four.**
6. **Three of the seven "foundations" are foundational.** The rest are components or views wearing
   architectural language.

Everything below is reductive. Nothing here proposes a new mechanic.

---

## §1 — What the player is actually doing

Stripped to the code: each turn the player picks one verb from a **fixed, always-fully-available
7-item menu** (`resolver.py:32`), attaches an appeal, and the move resolves through a hidden product —
pool roll × venue/judge resonance × readiness × jitter (`:304-316`) — into **one accumulating scalar**
that every win condition reads and nothing else (`:52-145`). The single non-scalar element is the
fault/clinch terminal (`primitives.py:262-279`).

And in the shipped campaign **nobody is doing even this**: both sides of every live contest are
`logos_spammer` (`scene_dispatch.py:311`) — the same move, every turn, forever. The minute-to-minute
activity currently exists only in a demo harness.

**Verdict: not worth doing as it stands.** The Klei refutation is upheld on an independent read.

But a defensible activity is already *in* the kernel, unassembled: hidden evidence weights that deplete,
a hidden judge mind read in coarsening bands, and a procedural defeat catalogue. That is a real thing to
do — *read a specific mind under a specific procedure and choose what you can afford to say.* The
smallest change that assembles it is **CIP-2's clinch-generalisation half only** (promote the one thing
that already doesn't cash into `adv` into a scored dimension) **plus CIP-5's writ** (so the player can
see the room). Not the verb swap, not the claim-graph engineering, not a deckbuilder.

---

## §2 — The foundational argument (new, and the strongest in the corpus)

The Auto/Manual Duality doctrine is ratified. Its exploit-prevention rationale reads, verbatim:

> "Consistency makes the fidelity choice **free of strategic advantage** — a choice of richness/agency
> only." — `auto_manual_resolution_duality_v1.md:65`

Set that beside the audit's central finding — every wired contest output is a stat delta — and the
conclusion is forced:

> **If `E[auto] ≈ E[played]` *and* every output is a scalar, then the "richness" the doctrine promises
> does not exist, and auto-resolving every contest is strictly correct play. By our own ratified
> doctrine, the played mode is wasted attention.**

The played fidelity can only justify its existence if playing shapes **which consequences occur** —
record kinds, compromise axes, who is bound to what — rather than their expected size.

Three consequences:

- This is the strongest foundations-level argument for **CIP-1 (the Record spine)** anywhere in the
  corpus, and **none of our four filed documents states it.**
- **CIP-9b should not be ruled separately from CIP-1.** A skill premium expressed in scalar EV is
  precisely the mode-shopping exploit the constraint polices; expressed in consequence *shape*, it is
  the legitimate Football Manager premium.
- It reframes the whole programme: the Record is not a memory feature. It is what makes the personal
  scale exist at all.

---

## §3 — The foundational choice: there isn't one

Every good contest system has one decision the player makes repeatedly. Burning Wheel: which manoeuvre
to script blind. Ace Attorney: which contradiction. Blades: whether to accept the position/effect or
push.

**Ours cannot be named in one sentence.** Three candidates, all dead:

| Candidate | Why it isn't the choice |
|---|---|
| The Style bet | API-unreachable (F1). The harness's own code calls this WORKAROUND 3 |
| The appeal-vs-judge read | Illegible — the resonance math is invisible and `ContestView` shows the audience as two booleans |
| Forum choice | Foreclosed by canon: `social_contest_v30.md:39` *ends the contest* on an adjudicator change |

That is the finding. A system whose central decision cannot be stated is not yet a game.

---

## §4 — The irreducible set: eleven primitives

If the subsystem were rebuilt from nothing, these produce the intended game:

1. **σ-kernel** — single-sourced with combat, tanh-capped, parity-tested
2. **`adv` + one banded close** + a **burden field** + **`VoteAtClose`** for benches
3. **Stasis ground + the `shift` verb** — reduced to four grounds (§6)
4. **Appeal axis + resonance/leak** — the reception model; the one asset the proposals cannot express
5. **Standing, one scale, 0–10** — this *is* Face
6. **Reserve** — conditional keep (§12)
7. **Dossier / EvidenceItem** — the concealed-value owner; the best primitive in the tree
8. **FaultState + DefeatCatalogue** — the only currency that doesn't cash into `adv`
9. **Adjudicator / Panel** — one preference vector plus discipline
10. **Pressure** — the correct home for what the doc's audience-boost die fakes
11. **Venue as a config row**

Plus, binding on the set: **the close must emit a record** (CIP-1). Without it the eleven produce stat
deltas, which is §2's problem.

**Not in the set:** Genre · Orientation · Style · InteractionType · tense (all three representations) ·
Room · FaceScale/Charisma-scale · Concentration-as-formula · the `hard` verb · SelfGating ·
`split_standing` · ArmatureAxis/ArmaturePosition · RhetoricalWeights · FactionBoost ·
AdjudicatorType-as-table · the TRACKERS registry · resistance (all three) · the legacy stub surface.

---

## §5 — The kill list

Ranked by rules removed. "Breaks: nothing" means nothing in resolution or any production caller.

| # | Cut | Breaks |
|---|---|---|
| **K1** | The doc's parallel exchange algebra — CLASH/REINFORCE/CROSS/TIE, strain, Charisma modifier, Focus defence, Rattled, first-to-speak, forfeits (~70 lines, 4 derived stats, 3 patches' residue) | Nothing in code. Takes `INTERACTIONS_TABLE`/`derive_interaction` with it |
| **K2** | The Doubt Marker apparatus (`v30:203,212-220` + ~110 lines of `dictionaries.py`) | ED-1060's pending ratification (moot it). ⚠ If Orientation dies, CR5's backfire dies — **ratified, needs Jordan** |
| **K3** | Two judge-preference vectors → one. `Adjudicator.character()` and `ArmaturePosition` are both "what moves this judge," on two bases, two reveal ladders, two channels (~450 lines) | ED-1062's ratified 4th-axis decision — **needs Jordan** |
| **K4** | The 9 non-canonical venue presets + 3 institutional modes (~230 lines) | `allow_rebuttal` becomes true nowhere → `rebut` unreachable → also deletes bug F4 |
| **K5** | **The `hard` verb + SelfGating** (new) | The Nyāya chala/jati flavour and a venue knob that nothing can trigger |
| **K6** | `split_standing` — a third representation of Standing, set by no preset | Nothing |
| **K7** | The legacy stub surface on the package API — `CONCENTRATION_MULTIPLIER` (struck), duplicate `PERSUASION_*` thresholds, the +1-toward-A tie bias | Two importers until re-pointed (a fold `__init__.py` already promises) |
| **K8** | The doc's Concentration formula chain and its ED-901/902/933/890/694/894 archaeology | Nothing. Focus and Spirit lose their only SC consumer — they were already flavour |
| **K9** | The Face second scale — `FaceScale`, `_Side.face_max/current`, `Contestant.charisma`, the v30 combo block | ED-1056's Gate-A ratification — **needs Jordan**. Fixes F2 by deletion |
| **K10** | Resistance in all three representations | Nothing (zero resolution consumers). Burden replaces the role it was faking |
| **K11** | `RhetoricalWeights` **or** the venue tense trio — not both. Twelve `[SEED]`s collapse to three per venue | The epideictic-compression anchor re-homes on the venue weighting |
| **K12** | Design-memo-as-code dicts exported as runtime API — `PANEL_CLOSURE`, `EPIDEICTIC_COMPRESSION`, `CR5_SELF_GATING`, `APPRAISE_REVEAL_BOUNDARY`, `TRACKERS`, ~110 lines of CR3 archaeology (~400 lines) | Kernel tests that assert on them (relocate to the ledger) |
| **K13** | The flat-dice economy → Dossier + δσ under the ratified 1.5σ cap (CIP-4) | Kills ED-617's special case and ED-SC-0005's open number |
| **K14** | `ADJUDICATORS_TABLE` and `PROCEEDINGS_TABLE` + `_crosscheck_proceedings` fold into `modes` | Nothing. The cross-check exists only because the fact lives twice |
| **K15** | The previously filed cut list, re-verified and upheld unchanged | As filed |

**Aggregate: the previously filed ~800 lines, plus a further ~700–900** from K3, K5, K6, K9, K11, K12,
K14 that the earlier work did not claim.

### 5.1 K5 in detail — the new one, and the sharpest

**`hard` is strictly dominated and its cascade is six rules deep.** It costs **5** against `advance`'s
**3** (`primitives.py:51`); after the `SelfGating` gate the two verbs execute **byte-identical code** —
same reception, same `_advance`, no magnitude difference anywhere in `_apply` (`resolver.py:357-389`);
and failing the gate is an immediate barred-device clinch loss. You pay +2 for a chance to instantly
lose. The harness sells it as *"a bigger swing"* (`agon_harness.py:327`).

Deleting it also deletes `SelfGating`, `Adjudicator.learned/hostile` (SelfGating is their only
resolution consumer), three `ContestView` fields, `DefeatCatalogue.barred` (nothing else sets it), and
the `overreacher` policy. **Six rules removed by cutting one dominated verb.**

*(Correction to my earlier report of F9: the harness copy does explicitly warn about the barred-device
clinch. Only "a bigger swing" is false.)*

---

## §6 — Collinear axes: the genre kill

Two axes that are functions of each other are duplication wearing two names.

| Pair | Verdict | Dies |
|---|---|---|
| **Genre vs tense** | Memory/Projection *are* Past/Future renamed; the ground→genre map is the tense map restricted | **Tense as a stored axis** |
| **Genre vs stasis ground** | CR4 makes primary genre a *function* of ground. The orator's chosen genre pays exactly one +1D on a match — unreachable in production, and terrain-blank on QUALITY/DEFINITION/JURISDICTION | **Genre is not a load-bearing free variable.** Kill it; keep the ground |
| **Orientation vs Doubt-Marker/CR5** | Orientation's only mechanical content is an unimplemented marker plus a cost-only backfire | **Orientation dies** with K2 |
| **Style** | Genre × orientation — both parents dead | **Styles die**, and the Style↔Appeal mapping problem (WORKAROUND 4) *dissolves* rather than needing a solution |
| **Appeal vs style** | Orthogonal — which is the defect: two unmapped "how do I argue" axes | Appeal survives as the sole rhetorical axis |
| **Adjudicator type vs venue proof weights** | The type's character profile does the same job as venue weights, blended by leak | AdjudicatorType-as-concept dies; concrete instances stay on the row |
| **Interaction type** | Fully derived from (genre, orientation) — a lookup | Dies with styles |
| **Faction boost vs Pressure** | Unconsumed in resolution; the Guilds row is explicitly a function of the adjudicator — a derived value posing as a table row | Boost dies; a dominant faction sets `Pressure` |
| **Burden vs win-condition family vs biased start** | Three encodings of one thing | ProofBar, GraceThreshold, biased starts, the tracker tri-state die |
| **CONSEQUENCE vs FEASIBILITY** (new) | Same tense, same genre, same role; no consumer distinguishes them | **Merge.** Stasis 6 → 5, and → 4 with §10's JURISDICTION fix |

**The genre kill is the deepest single cut available.** It removes ~130 lines of `rhetoric.py`, the
reachability problem in *both* directions (the Memory fix and the unreachable Projection half), the
epideictic-compression record, and the chosen-genre-vs-ground tautology fix. Church Tribunal's FACT
start survives on its own thematic merits.

The one live genre consumer — Domain Echo channel selection (Memory→Mandate, Projection→Influence,
ED-SC-0002) — re-keys on ground tense (past→Mandate, future→Influence) **with zero information loss**.

---

## §7 — The character layer collapses to one number

| Attribute | Live consumer | Verdict |
|---|---|---|
| Cognition | none — `ADJUDICATOR_PRIMARY` is display metadata | Flavour |
| Charisma | only the FaceScale display accessor, which the adapter never sets → latent crash (F2) | Flavour + a crash |
| Attunement | none | Flavour |
| Focus | none (`Reserve` is attribute-free by construction) | Flavour |
| Spirit | none | Flavour |
| Recall | none | Flavour |
| **`faculty`** | `Pool.size` **and** `Leverage.net` — both halves of every reception | **The entire build, in practice** |

The intended differentiation — *Cognition before judges, Charisma before crowds, Attunement in private* —
is the subsystem's cleanest build claim and it fires nowhere.

**Reductive ruling: either the one line ships** (`_as_contestant` maps the proceeding's primary attribute
to `faculty`) **or the §3 attribute table is deleted from the SC surface.** A table with no consumer is
worse than no table.

---

## §8 — Twenty-four contest configurations reduce to four

8 proceedings + 9 cross-cultural presets + 3 institutional modes + 4 GAMES rows = 24. Applying our own
discriminating test (policy differs ∧ the player can tell) to the *production* engine:

| Survivor | Absorbs |
|---|---|
| **T1 — Tracked contest before a crowd** | formal_contest, grand_contest, public_oration, fused_arbiter. Budget 3 vs 5 changes pacing EV, not the best-move map |
| **T2 — Tracked contest before a single judge, burden-bearing** | royal_audience, church_tribunal, §7.1 Excommunication, §7.3 verdicts, inquisition_hearing, imperial_petition, memorial_remonstrance, excommunication_court, GAMES `inquiry`. Their differences are track bias (EV-only — the sameness-bearing class) and judge `[SEED]`s. **Burden is the one variety-bearing parameter** |
| **T3 — Panel ballot** | guild_arbitration, secret_council, deliberative_body. The only genuinely different close: verdict severed from momentum |
| **T4 — Untracked private tally** | casual_dispute + personal_appeal (identical but for a role label), private_negotiation, GAMES `negotiation` until `settle()` exists |

GAMES `consensus` is the BG vote — a *fidelity view*, not a fifth type. `negotiation` becomes a genuine
fifth type only when `settle()` exists (CIP-8's gate, upheld).

---

## §9 — Venue, adjudicator, audience → two concepts

"Audience" currently exists in **five fragments**: dead resistance metadata, `Room`, `Pressure.public`,
the crowd-as-Panel, and the unconsumed faction boost.

Minimum set:

1. **The Venue row** — proof weights, budget, burden, faults, `Pressure`, start ground. *Pressure is the
   audience's institutional and popular force.*
2. **The Judge** — `Adjudicator | Panel`, one preference vector, discipline. A crowd is a Panel; "no
   adjudicator" is a low-discipline Adjudicator. **Both are already true in code.**

**"Audience" as a third concept dies.** `Room` folds into Standing or dies with it — they are twin
accumulators feeding `Readiness` at equal weight; flagged as a soften-able merge, since folding costs
pathos its distinct build target.

*New, minor:* two bench-size defaults coexist — `panel(size=5)` against `jurors=7` / `panel_size=7`.
One owner.

---

## §10 — Incoherence register (three new, live in resolution)

1. **The governing one:** the canonical §4 loop and the kernel loop share nothing but band thresholds.
2. **DEFINITION's tense contradicts ratified CR4 — and it is live.** `primitives.py:16` tags DEFINITION
   `"past"`, so a definitional move receives the `logos_past = 1.20` weighting through `joint_weight`.
   But CR4 rules definitional is a *Present-rendering* reframe, "never collapsed to Memory/past"
   (`rhetoric.py:9,18`). **The forbidden tense intermediary was removed from the genre map and left
   alive in the resonance math.**
3. **JURISDICTION's role contradicts its ladder position.** `rhetoric.py:150-157` rules translative
   *pre-merits* — "the Stay." But the upward-only ladder puts JURISDICTION **fourth**, reachable only
   after FACT/DEFINITION/QUALITY have played, and **below** CONSEQUENCE/FEASIBILITY — so a merits ground
   outranks a jurisdiction challenge. A Stay that can only be raised mid-merits and can be over-shifted
   by "what will follow?" is not a Stay. Either JURISDICTION leaves the ladder (it is already a
   pre-contest gate in `parliamentary_stay.py`) or "pre-merits" is false.
4. **Stale honesty notes** claiming strip is never called, while `resolver.py:411-419` calls it (F3).
5. **ED-137 status contradicts itself inside one file** — `modes.py:430` says provisional/use-Expert-Judge
   while `:502-507` and `PANEL_CLOSURE` say CLOSED.
6. **`wrapper.py:165-167` asserts no canonical proceeding maps to `panel`** — false since ED-1059.
7. **Flavour contradicts kernel:** Suppression's card copy claims it "does not build Face the way
   Revealing does," but the kernel builds Standing on any ETHOS move regardless of orientation.
8. **The doc violates its own ratified substrate** — flat pool dice against CR6's δσ/tanh ruling.
9. **`primitives.py:161-162`** claims the Concentration magnitude is carried by `wrapper.py` (it isn't)
   and `params/contest.md` (which no longer exists).
10. **An orphaned rule block:** the Doubt Marker's trigger header was lost in atomization, so its trigger
    is formally unstated in the canonical head.

---

## §11 — Crunch cascades, and where to cut the root

| Cascade | Root cut |
|---|---|
| **Face** → Charisma×3 → combo formula → two-representations open decision → strip → Rattled → recovery → equipment → Knot bridge → CR5 bound | **Kill the second scale (K9).** Removes ~8 downstream rules, one open decision, one crash |
| **Doubt Marker** → EV=0 in single exchanges → ED-1060 → terminal-value rule → split by mechanism → branch guards → flavour conditionals | **Kill the marker (K2).** The whole chain exists to rescue a dominated bit, and the rescue fails anyway |
| **Concentration** → ED-901/902/933 → depletion rescale → Spent timing → coalition pool → Recall removal | **Kill the formula (K8).** `Reserve` already is the abstraction |
| **Stacking** → 4 bonus dice → +2D cap exception → KU-1 → ED-SC-0005 → Momentum omission | **Route through Dossier + δσ (K13).** The cap already exists |
| **Genre** → 3→2 compression → epideictic record → CR4 map → tense prohibition → reachability gap → Church FACT start → Projection still unreachable → shift-verb doc gap → tautology fix | **Kill genre as an axis (§6).** The deepest cut in the tree |
| **Armature** → 4th-axis question → dot-product → rounding bug → δσ rechannel → gate-off never set → reveal boundary → strength `[SEED]`s → solved-lookup worry | **Merge into `Adjudicator.character` (K3)** |
| **`hard`** → SelfGating → learned/hostile → ContestView exposure → barred fault → device-bar knob | **Kill `hard` (K5)** — six rules for one dominated verb |
| **Obligations** → duration table → Wager → §6.1.1 edge cases → interruption generalization → overlay residue → advisory cap → a consumer with no object | **Emit a `Debt` LedgerTag (CIP-1)** and delete the residue |

---

## §12 — Elegance and necessity of the survivors

**Q-elegant passes:** σ-kernel · track+burden+ballot · Standing · Dossier · faults · Adjudicator/Panel ·
Pressure · JITTER.

**Q-elegant fails:**
- **`MERIT_SCALE` × `PersuasionTrack.scale`** — two arbitrary scalars in series on one pipeline. Merge.
- **The gain pipeline** is six multiplied factors; the *concept* (leak) is restatable, the arithmetic
  is not.

**N-Necessity flags** — Jordan-owned, flagged not rejected:

- **Reserve fails as shipped (new).** `support` spends 2 and regains 4 — **net +2**. The stamina economy
  cannot bind any policy that mixes support; exhaustion only punishes spam bots. Keep only with
  cost ≥ regain, otherwise it is a tempo tax pretending to be a resource.
- **The fault catalogue's grounding is off-period.** It is cited throughout to Nyāya *nigrahasthāna* —
  classical Indian disputation — in a Renaissance-inflected game. The mechanic is defensible on-period
  (scholastic disputation had formal defeat conditions), but **we just imposed exactly this
  canon-vs-design sourcing bar on document 5. Symmetry demands our own kernel meet it**: either
  re-ground the prose in the scholastic tradition or tag it design-on-merit.
- **Ungrounded but harmless:** the Reserve economy as a construct; Momentum-as-purchasable-successes
  (the literal Klei shape, doc-side only); the flat bonus-dice stack (dying via CIP-4).
- **Stasis fails as shipped** at six grounds with a self-contradicting Stay; **passes at four** after the
  CONSEQUENCE/FEASIBILITY merge and the JURISDICTION fix.

---

## §13 — What to abandon entirely

Each argued both ways by the foundations lens, then committed:

| Item | Verdict |
|---|---|
| **Three-mode TTRPG/BG/Hybrid framing** | **ABANDON.** The duality doctrine already ratified its replacement. §10's constants survive as the auto-resolver's config |
| **Model A exchange algebra** | **ABANDON** — demote to historical note. Salvage exactly one idea into the deliberation work: CROSS's cap-the-favourite function |
| **Stage-3 armature** | **DO NOT ABANDON — demote.** Wire it (F1), strip it of anti-collapse duty, let the unrun sweep rule Fork B. *Abandoning ratified work on an unrun falsifier would repeat the §0.1-point-4 error in reverse* |
| **9 non-canonical venue presets** | **CUT to a reference doc** — with the note that canonical start-grounds must be re-derived when Projection reachability is fixed, since the presets hold the only CONSEQUENCE/DEFINITION starts |
| **The four-GAMES roster** | **ABANDON THE FRAMING.** Keep `settle()` as the one genuinely new build; Inquiry and Consensus are venue rows, not games |
| **Persuasion Track** | **KEEP, DEMOTED** to an outcome-banding view. The compromise band is the composed-echo magnitude key (ED-SC-0002, ruled) |

---

## §14 — Two governance findings I created and did not notice

**Two competing roadmaps, unreconciled.** `HANDOFF_SC.md:164` and `CURRENT.md:151` still carry
**"Stage 4 — four games — next"** as the live, Gate-0-ratified plan, while the CIP programme is a
different roadmap for the same subsystem. **No filed document reconciles them.** That reconciliation is
a needs-Jordan item the programme forgot to file.

**A ratified debt no CIP covers.** The duality doctrine names its own "chief build implication" —
event-parameterising the auto-resolver so it resolves *specific slate motions* rather than a generic
per-season roll. Checked against CIP-0..12: **nothing covers it.**

**Bookkeeping:** the proposal's header still says "Ten proposals … CIP-1..CIP-10" while containing
thirteen; CIP-11 and CIP-12 have no wave assignment.

**Ratification collisions.** K2, K3, K9 and the genre kill each touch a Jordan-ratified item (ED-1060
pending, ED-1062, ED-1056). Under CLAUDE.md §2 none can land as routine work. They are filed as
recommendations with their reductive case stated, not executed.

---

## §15 — The one thing

If only one finding is acted on: **ratify CIP-1, the Record spine, with its producer/consumer-pair rule
intact.**

Against the alternatives: the bug batch is necessary but changes nothing about what the system *is*;
CIP-2 is gated on sweeps nobody has run; CIP-0 canonises prose the programme intends to partly rewrite.
CIP-1 alone (a) needs no new primitive, no new number, and no sweep — `ledger.py` is live and
owner-agnostic; (b) repairs Ω-Intent clauses 1 and 2 at the root; (c) per §2, is **the only thing that
gives the played fidelity a reason to exist under Jordan's own ratified doctrine**; and (d) is the
precondition that makes every later consolidation safe rather than risky.

---

## §16 — Scores against the corpus's own instruments

**Dramatic-legibility test** (the canonical playability bar), at personal scale: **0 / 3.**
*Whose position is at risk?* — stakes live in a "hidden GM ledger"; the kernel has no stakes object.
*What does each named actor want?* — factions have no aims; per-member judge minds are authored then
averaged away. *What happens if no one acts next season?* — committee referral produces nothing, chain
contests are inert, and the auto-vote is a generic roll rather than a specific motion. Faction scale
passes weakly, because five scalars are legible.

**Ω-Intent, four clauses: 4 / 4 FAIL** — cross-scale consequence, personal transformation, autonomous
world, and non-dominance (twice: doc-side stacking at p≈0.93, kernel-side verb collapse). **Three of the
four failures are foundational.** The superstructure proposals cannot buy back any clause on their own.

---

### Audit trail

`[READ: the full kernel package; the canonical head; all four prior filed documents; the CIP proposal;
the five preserved sources; the NERS charter. Every new claim re-verified by the orchestrator at the
file:line given — including the five novel ones: support's net +2, DEFINITION's live tense
contradiction, the JURISDICTION ladder inversion, the STYLE_AXIS↔ArmatureAxis bijection, and the dual
bench defaults.]`

`[METHOD: two read-only Fable 5 lenses with a reductive mandate (kill-list · foundations), disjoint
scopes; Opus synthesis. Per CLAUDE.md §10 — fable on the read-only audit nodes, Opus on authorship.]`

`[NULL: no fabricated constants in the kernel (independently re-confirmed — every constant carries
[SEED] or a citation); no hidden consumer for resistance, FACTION_BOOSTS, derive_interaction outside
tests, split_standing, the CONSEQUENCE/FEASIBILITY distinction, or learned/hostile outside SelfGating —
each established by a full read of the consuming module, not a term grep. The prior filed audit
survived attack: of its load-bearing claims re-verified here, zero were overturned.]`

`[SELF-AUTHORED — bias risk] This is the fifth document I have filed on this subsystem in one session,
and it recommends deleting a great deal of work — including several items I recommended two passes ago.
The specific risk of a reductive mandate is over-cutting: a lens told to prune will find pruning. Two
mitigations were applied. Every cut states what breaks, and cuts that break a Jordan-ratified item are
escalated rather than executed (§14). And the foundations lens was explicitly asked to argue both sides
of each abandonment before committing — which is what produced the one DO-NOT-ABANDON verdict (the
armature), on the reasoning that killing ratified work on an unrun falsifier would repeat, in reverse,
the measurement error §0.1 exists to prevent.`

`[CONFIDENCE: high — the irreducible set, the kill list entries with file:line, the collinearity
findings, the character-build collapse, the incoherence register, and both governance findings.
medium — the 24→4 merge count (it depends on CIP-3 landing; without burden the T2 sub-rows are EV-only
variants and the count is arguably 3) and the §2 duality argument (an inference from ratified text, not
a measurement). low — line-count estimates and anything about build effort.]`

`[PASS-3: two reductive lenses with required nulls and both-sides argument on abandonments; five new
claims verified against disk before banking; ~1500-1700 lines identified for removal; four ratification
collisions escalated rather than executed; two governance gaps found in my own prior filings.]`
