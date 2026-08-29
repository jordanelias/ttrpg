# Valoria, From Scratch — the master plan

## Status: PROPOSED (2026-08-29). **HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**
## Merging this files it. It flips no `## Status:` line, changes no behaviour, proposes no deletions,
## and touches no `engine/`, `systems/` or `tools/` code.
## Method: designed and coded from scratch. All existing work was reference, never ruling.

---

## 0. What this is, and what it is not

A from-scratch design for Valoria, built on the nine throughlines and on Jordan's containment axiom.
It is **not** a repair of the prior greenfield suite. That suite's critique was read only as evidence
about which *design shapes* fail; its blocker register was deliberately excluded, because those
blockers are formatted as a work list and following them would have produced the same architecture
with eight patches while calling it new.

**What it does not do.** It does not run. Nothing here has moved a byte of executable behaviour, and
no claim in it has been measured against a campaign. Every gain is unmeasured and stays so until
something executes.

---

## 1. Read in this order

| | document | what it owns |
|---|---|---|
| **01** | [The Substrate](01_substrate.md) | **the spine — binding on everything else.** Two structures, one actor, three signatures |
| 02 | [The Person](02_the_person.md) | marks, capability, stance, ties and Knots, computed needs, cohorts |
| 03 | [Knowledge, Telling, Investigation](03_knowledge_telling_investigation.md) | claims, witnessing, lying, view assembly, corroboration, field investigation |
| 04 | [The Hearth and the Community](04_hearth_and_community.md) | the two new rungs, cadet branches, admission, the judging set |
| 05 | [The Up-Stroke](05_up_stroke.md) | petition, backing, carriage, the drop, grievance, revolt |
| 06 | [The Down-Stroke](06_down_stroke.md) | dispensation, publication, compliance, computed openings |
| 07 | [Alignment](07_alignment.md) | factions that scale continuously, power bases, secrecy |
| 08 | [Argument](08_argument.md) | the stasis ladder, named-fault defeat, graded proof, negotiation |
| 09 | [The Churning World](09_churning_world.md) | the tick, fidelity, anti-leverage, the battle seam, latency, the budget |
| 10 | [The Resolution Surface](10_resolution_surface.md) | the roll, the obstacle, degrees, what a player chooses |
| 12 | [Coercion and Force](12_coercion_and_force.md) | willingness, the levy, violence below war, the ratchet |
| 13 | [Material Life](13_material_life.md) | the larder, the settlement stake, prices, slow fuses |
| 14 | [Office and the Upper Rungs](14_office_and_upper_rungs.md) | remit, establishment, conferral, venues, the Crown |
| 11 | [The Idealized Code Shape](11_code_shape.md) | adjudicated **without reference to any existing code** |
| 15 | [The Adjudication Register](15_adjudications.md) | every challenge raised, and how it was decided |
| 16 | [The NERS Audit](16_ners_audit.md) | four adversarial critics, and two retractions of my own rulings |

---

## 2. The design in one page

**One actor and two relations.** There is exactly one kind of actor — a person — and two relations
over the set of persons. **Containment** is a strict single-parent tree: Person → Hearth → Community
→ Settlement → Territory → Province → Realm. **Alignment** is an unconstrained set-system. Everything
else — houses, guilds, the Church, the Restoration, two brothers with a grudge — is derived.

**Why containment is single-parent, which is the derivation everything rests on.** The setting hands
you an immediate counterexample: an Einhir smith belongs to the Kettlemakers *and* the hamlet outside
the wall. Multi-parent containment states that in one line, and that is exactly why it is refused. If
a person can be contained twice, divided loyalty becomes a set membership and evaporates. Forcing the
second belonging into alignment makes it a commitment that can be concealed, betrayed, and punished
for. **That friction is the game.**

**A faction is not a tier.** It is a proposition plus a map from persons to a degree of commitment.
Two brothers and a national church are the same object with the same mechanics. Scale is *derived*
and gates no option — capacity to act at a node is *does this faction hold a person who can act
there*, which routes through persons. One membership operation runs growth and collapse in two
directions, so there is nothing left to be discontinuous.

**The signature rule.** `choose(person, view) → act` · `resolve(acts, world) → events` ·
`witness(person, event) → claims`. No decision function takes the world. Omniscience becomes
unspellable rather than capped — and belief needs no cap, because true state is not in the decision
path at all. Correction comes from collision with the world, not from a ceiling.

**Two new rungs, neither of which exists in canon.** Hearth owns the larder, the succession pointer
and the obligation edge — and cadet branches *fall out* of a succession pointer that leads nowhere,
rather than being authored. Community owns the judging set and the admission gate, and holds no state
of its own: a norm is the stances of its members, computed when asked.

**Two strokes, one transport.** A petition travels up and must be **carried** by a named person at
each rung, who may forward, amend, bundle, or **drop** — so filtering is an act by a person, not a
threshold. A dispensation travels down by being **noticed**, so it reaches a person holding no post,
and their opening is *computed* rather than authored.

**The module hierarchy is the containment ladder.** Parent-child in the code means containment in the
world, which is what makes it a hierarchy in meaning rather than a filing system. Distributing down
at increasing granularity *is* the down-stroke; aggregating up *is* the up-stroke. Propagation
becomes the architecture rather than a feature, which is why the two new rungs had to exist.

---

## 3. What is settled, what is open, and what needs Jordan

### 3.1 Settled by this design
Sixteen challenges were raised by lanes or critics and decided in [15](15_adjudications.md). Four
amended the spine. Two questions a prior process had escalated are answered structurally rather than
referred: whether a false belief may decide outright (it dissolves — there is nothing to cap, because
the decision never sees true state), and whether community is a required rung (Jordan ruled it, and
went further to family).

### 3.2 The one thing to settle before anything is built

> **Is conferral rooted in persons or in offices?**

Person-rooted, dead conferrers terminate the graph, and the sovereignty query that all five factions'
victory conditions operate on is undefined across most of it — the Crown cannot be played across a
succession. Office-rooted, the graph resolves, but an institution performs the game's most
consequential act, which ruling B-11 forbids. **The suite asserts both and resolves neither.** The
design's own evidence that it needs the office-rooted answer is the military order sworn *to the
Crown as institution, not the bloodline* — a warrant that means nothing if conferral is personal.

Two defensible answers, materially different games. Not an audit's call.

### 3.3 Genuinely open, and honestly so
- **An off-board polity acting without a person to carry it.** Altonia and Schoenland exert real
  pressure from off the map. "Generate a person" and "allow an actorless pressure" are different
  games.
- **The testimony half of the salience floor** ([16 §3.2](16_ners_audit.md)) — a revelation arrives
  as testimony and is still clamped. Held open rather than patched.
- **The drop's counterweight for appointed office**, which is currently elected-seat-shaped.
- **Personal leverage at N=1000 is BOUNDED, NOT SOLVED**, and the design says so. Whether acting on a
  share graph *feels* like agency is a question about reach, which is an investigation problem.

---

## 4. If this were built, the order and why

Not a schedule. An ordering argument, in which each step is the precondition of the next.

| | step | why it is here and not later |
|---|---|---|
| **0** | Settle conferral (§3.2) | Everything at Settlement and above reads it. Building on the wrong answer wastes the rungs above. |
| **1** | Person, claim, `witness`, `tell` | The three signatures and the ledger. Nothing else can be built without them, and every later throughline routes through them. |
| **2** | View assembly with its budget and stance weighting | This is where T3 and T4 become real. Until decisions read views, everything above is a simulation of an omniscient world with extra steps. |
| **3** | Containment tree, cohorts, individuation | Rungs, and the compression that makes a peninsula affordable. Individuation must exist before anything at scale. |
| **4** | The resolution surface | One roll, one obstacle derivation, one owner. Everything above calls it, so it must exist before anything calls it. |
| **5** | Hearth and larder | The generator of ordinary need. Without it, every want in the game is political ambition and nobody is ever simply hungry. |
| **6** | Petition and dispensation | The two strokes, on the transport built in step 1. This is the first point at which the design does something the prior one could not. |
| **7** | Alignment and commitment | Factions, once there are persons to hold them and grievances to make commitment cheap. |
| **8** | Office, venues, argument | Politics with rooms in it. Requires conferral settled at step 0 and propositions from step 7. |
| **9** | Coercion, and the battle seam | Last, deliberately. It is the most-built system in most games of this kind and the least load-bearing on these nine throughlines. |

**The one measurement that would falsify the whole thing**, and it belongs at step 2, not at the end:
run the same seeded world with the view layer on and with decisions reading true state instead. If
the two runs produce recognisably the same history, the epistemic layer is decoration and the design
is wrong about its own centre of gravity.

---

## 5. What would make this fail

Stated plainly, because a proposal that names no failure mode is not making a claim.

- **The predicate vocabulary keeps growing.** It declared twelve forms, used a thirteenth three
  sections later, and is now fourteen. If it reaches twenty, closure was the wrong idea and the
  entailment table becomes the scripting language it was meant to prevent.
- **Cohorts erase what makes the design good.** Compression at the fidelity where most of the world
  runs already laundered one consensus broadcast past the type system. If divergence survives only
  where individuation happens, then most of the world is the old design wearing this one's names.
- **Ignorance stops costing anything.** The design's whole claim is that a decision reads a view. If
  play converges on keeping views accurate, the epistemic layer becomes overhead and the game is a
  strategy game with a slow information tax.
- **The person layer does not pay for itself at scale.** Leverage is bounded, not solved. If a player
  at realm scale cannot find the man holding a quarter of a command, the two layers detach — which is
  the failure every surveyed precedent hit.

---

## 6. Provenance

Written this session by Sonnet and Opus lanes composing on a substrate derived by Opus, orchestrated
and adjudicated by Fable 5, and audited by four read-only Fable 5 critics whose independence is
structural rather than declared. An antagonist ran throughout against drift into remediation of
existing work.

Jordan's four directives this session were brief, not reference: the containment axiom (family and
community as first-class rungs; a faction as any aggregate at any scale); the NERS charter with
elegance as a **ratio** against necessity and robustness; the widening of the reference corpus to
PRs #336–340; and the modular hierarchy code architecture. The rest — every design decision in
fourteen documents — is derived, and where it was wrong, [16](16_ners_audit.md) says so.
