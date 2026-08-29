# 01 — Findings: T1 actions by characters · T2 memories, feelings, beliefs · T3 fallibility and perspective

## Status: FILED (2026-08-29) — analysis. Reads: [`00_INDEX.md`](00_INDEX.md)
## Each throughline was audited by one read-only Fable 5 critic with no sight of the others' work.
## Severities: BLOCKER (throughline unreachable as designed) · DEFECT · GAP · NIT.

---

# T1 — All actions in the game are performed by characters

**Verdict: PARTIAL.** Structural across the faction, settlement and personnel layers; the two
deliberate exceptions leak, and at the battle seam the contract as specified has the faction fighting.

## T1 steelman

The suite's best answer is not the gate — it is that **agency has exactly one shape**. A Post
(`01:408-446`) is the only way anything acts on behalf of anything. ED-IN-0201's gate is executed per
tier (`05:122-131`), so a faction with no seated person at a rung does not act there, emits why, and
recovers by producing a person (`05:189-201`). The actor of every roll is *"the post-holder invoking
the module — never 'the faction'"* (`05 part2:360`); pools are one person's two attributes, never a
roster aggregate (`05 part2:374-378`). NPC choice is character-shaped twice: institution ethos plus
the holder's own convictions, drawn per `post_id` (`05:304-321`). The player is a person holding
posts, and an unattended post runs the same module headless (`01:449-468`), so T1 holds symmetrically
for AI and human. `04 §4.0` extends T1 *into* the appointee: being acted upon is also an action, and
a person may refuse. The two exceptions are principled residues — weather is *dynamics*, not action
(`11:207-211`), and a population acts through a place-bound project with obstructable terms rather
than a phantom post-holder (`09:569-597`).

## T1 findings

1. **[BLOCKER] At the battle seam, the faction fights, not a character.** `12 §2.4` claims the holder
   supplies attributes to the battle model and calls that *"the entire personnel↔battle seam"*
   (`12:169-171`), but the contract `12 §3.3` specifies carries only faction ids and `site_id`
   (`12:292-298`), with the formula `faction.Mil × terrain_coeff` (`12:300-305`). Verified: the bridge
   derives one field, `history = max(1, round(f.Mil))`, and labels the Combatant with the *faction id*
   (`combat_bridge.py:106-111`). Since `12` writes this contract fresh with no legacy to preserve
   (`12:263-266`), the commander's person is omitted by choice. Q-2's gate makes the commander a
   doorman whose attributes never reach the outcome — the "staffed defender is inert" failure O-5.4
   prosecuted at influence contests. *Authors would dispute*, citing the bridge docstring's
   no-fabrication rule (no personal actor exists at MC scale) — but that rationale dissolves in a
   suite whose `02`/`03` generate the commander as a real person. — **structural**
2. **[DEFECT] The rising's fire exits `04`'s recall invariant.** `rising` fires `post_revoke`
   annotated *"write leaf 3 — 04's pm.recall"* (`09:616`), but `pm.recall` binds a principal: a cited
   cause tag, one involuntary change per principal per season, an escalating `standing` cost
   (`04:450-456`). A rising has no principal, no budget, no standing. Involuntary removal now has a
   second path with none of the first path's bounds. — **structural**
3. **[DEFECT] After O-5.13, the leaf-1/2-only fence on actorless effects has no owner.** `11 §2.3`
   forbids a world event granting a Post or firing a transition (`11:215-224`), but the merge into
   `05`'s schema preserves, by its own enumeration, everything *except* that restriction — it names
   `hazard_pool ∈ [6,18]` as the one constraint the merge would otherwise drop (`05 part2:304-311`).
   The effects-leaf restriction is a second dropped constraint, unnamed. `fa.resolve` legally declares
   `form: [{place, facilities}]`, so a `remit_kinds: []` row revoking a governor is schema-legal. No
   falsifier asserts `remit_kinds: [] ⇒ effects ⊆ leaves 1–2`. — **omission**
4. **[DEFECT] An agentive polity is shipped as weather.** `we.altonian_pressure` — a diplomatic
   demand depositing a `Grudge` (`11:565-595`) — is an actorless row: an event no character performs
   and through which no character can be obstructed. `09 §12` rejects exactly this shape for
   populations (`09 part2:299`). No criterion restricts actorless rows to non-agentive causes, so the
   variant is an open reclassification channel: any hard-to-model actor can be demoted to weather.
   *This is the finding the authors will dispute*, citing root cause E's requirement of an outside —
   but the obstructability argument is theirs. — **structural** → escalated to **J-3**
5. **[DEFECT] `08 §3`'s residual is raised and answered by nobody.** `fa.gate` iterates
   `posts(faction, tier)` (`05:124`), so a governance post held under no faction is never reached —
   a character stopped from acting. `08:125-130` flags it and hands it to `05`/`04`; `05 part2 §10.4`'s
   dependency table does not carry it. Plausibly reachable, because `04` keys the caste gate on the
   post's *granting institution* and ships an `institutions` roster (`04:210-224`) never identified
   with the faction-entity roster. — **omission**
6. **[DEFECT] Bloc- and faction-owned projects have no declared declaration path.** `am.declare`
   carries exactly one conditional, for `place` (`09 part2:222-227`); `09 §10.1` generalizes G-29
   because *"blocs and factions declare projects too"*; `06 §3.4` gates `latent → open` on the bloc
   having declared a project. Nothing says who invokes it, whose budget is spent, or which remit makes
   such kinds eligible. `09 §13.3`'s own ghost falsifier fails on `bloc` and `faction` as written —
   and change C's schism → founding-claim → `act.charter` chain dies at step one. — **omission**
7. **[GAP] `legitimating.*` has no producer** (see **X-3**). — **omission**
8. **[GAP] Cross-document contradiction on allegiance** (see **X-6**). — **wording**
9. **[NIT] `sm.directive` bills a character for an action they do not shape** — `resolver: derivation`,
   the order derived from state, yet costing the principal's `post.budget` (`08:152-156, 434-436`).
   ED-IN-0201 clause 2 says the person shapes *which* action; here the person is a billing address.

> **Critic's coverage note, preserved.** Read in full: `00`, `01` pt 1, `04`, `05` both parts, `08`,
> `09` both parts, `11`, `12`. Partial: `01` pt 2 (§7, §9), `06`, `10` pt 1. Not read: `02`, `03`,
> `07`, `10` pt 2, `13`. Tree verifications by hand: `combat_bridge.py`, `scene_dispatch.py`, both
> bridge tests, `dice_engine.py:150-239`, `keys.py:525-601`, `faction_action.py:230-264`,
> `test_engine_does_not_import_systems.py:212,288-293`, `descriptors.json:93-123`,
> `key_type_registry_v30.md:446-459`, `module_contracts.yaml:330-354`, `settlement_layer_v30.md:145-156`,
> `faction_canon_v30.md:364-373`. *"Every tree citation I checked was accurate — the suite's
> evidentiary hygiene is genuinely good; the findings above are design holes, not fabricated citations."*

---

# T2 — All characters have memories, feelings and beliefs that may change over time

**Verdict: STRUCTURALLY BLOCKED.** The feeling leg exists and moves; the belief and memory legs have
well-designed shapes with zero working writers anywhere in the suite.

## T2 steelman

One substrate, three legs, no bespoke stores. *Belief:* the seven-kind Tag enum admits `Holding` by a
two-part inexpressibility test (`01:250-327`), adopting the Jordan-ruled grammar — a `prop_id` can
carry a **false picture**, which the cut `Memory` kind's `key`+`value` structurally could not.
Creed-Beliefs are a marked subset capped at canon's 3 (`02:455-492`); revision is a gate on worn-down
effective confidence, never a roll (`02:511-533`); the Embrace/Denial/Schism showpiece resolves with
no branch naming the Restoration Movement. *Memory:* salience decays by derivation over fields the tag
already carries — one decay law, no second stored field, bounded at `population × HOLDING_CAP` by
construction (`01:328-359`). *Feeling:* two personal meters instead of nine (`01:520`), PC↔NPC
disposition stored per canon and NPC↔NPC derived per PP-724 so the write rule is never violated
(`01 part2:158-165`), and `allegiance.strength` restores the recoverable person→faction track that the
corpus's single most duplicated arc shape reads (`01 part2:61-121`). `RELATION_SHARE_MAX` keeps all of
it a bias, never a substitute.

## T2 findings

1. **[BLOCKER] No belief can change — or exist with a confidence — end to end, and this is worse than
   `08` claims.** `cg.stage` grants a `prop_id` into `form.beliefs` and only *names* the seed Holding
   for `npc_memory` to write (`02:484-492`); `npc_memory` is `doc: null`, no sim, re-verified absent
   (`module_contracts.yaml:380-386`); the epistemic design is PROPOSED and unbuilt by its own status
   line; `11 §2.3` permits deposits on place/faction gauges only; and `08 §6.3`'s fix targets a deleted
   gauge. **So nothing writes one at generation either.** `02 §11.5` admits half of this; the suite's
   index nowhere states that T2's belief leg is wholly outside the suite. — **structural**
2. **[BLOCKER] The credence ghost** (**X-1**). `08` was finished against a stale draft of `02`: it
   deposits into `credence.<proposition>` (`08:341`), justifies it by citing a `02 part 2 §10.1` row
   that no longer exists (`08:354-356`), and quotes `02:521`'s *"move confidence"* as *"move credence"*
   (`08:351-352`). The suite's only post-generation belief-writer is wired to a deleted object, and
   `08`'s own "flagged, not made" dependency is unfixable as stated. — **structural**
3. **[BLOCKER] Two irreconcilable homes for the `Holding`**, and the split manufactures the
   `npc_memory` blockage. `01 §3.1` adopts Holding **as a Tag kind** (`01:244, 268-277`), written by
   `tag_append` through `substrate.ledger`, and `cg.stage` already declares that tag-write row
   (`02 part2:110`). `02 §6.2` instead assigns it to `npc_memory`'s own state (`02:487-488`). Both
   cannot be true: if it is a substrate tag, `02`'s refusal to write it is self-inflicted and needs no
   unbuilt module; if it is `npc_memory`'s registry bucket, then `01`'s enum row, salience derivation
   and `HOLDING_CAP` sweep are specified against a store the substrate does not hold. O-6 claims plain
   adoption while silently relocating the home. *Authors would dispute* — they would say O-6 adopts the
   grammar and the home is FI's open call; but `02:487` treats it as decided one way while `01:244`
   ships it decided the other, and a reader implementing either page alone builds a different store. —
   **structural**
4. **[DEFECT] The `witness_key` channel and the salience sweep read Holdings that nothing produces** —
   the same read-without-writer class `10` caught for `engaged(c)` and fixed (`10:552-557`). No module
   contract appends a perception Holding when an event fires. Rumour-borne Slate items, misperception
   and the top-K forgetting sweep are all consumers of an empty store. — **structural omission**
5. **[DEFECT] `01` promises beliefs rank the option set; `05` ships without a belief term.**
   `01 §4.3`: *"a holder's convictions and beliefs rank the remit's contents (`05 §3`)"* (`01:445-446`).
   `fa.select`'s declared inputs are ethos, holder convictions, world signals, `Leverage` tags
   (`05 part2:673`) — no Holding. `04` never mentions beliefs. — **cross-document contract mismatch**
6. **[DEFECT] `09`'s shape-check verdict is stale on both T2 surfaces** (**X-6**), and wrong in both
   directions: allegiance *does* have an edge kind since O-7, and belief's working-writer count is
   **zero**, not one. — **stale**
7. **[GAP] A person's feeling about a place, a policy, or an institution's action lives nowhere.**
   Full inventory: `standing`, `exposure` (undirected), `truth`, `disposition.pc_npc` (PC-end only),
   derived NPC↔NPC disposition, `strain.<kind>`, `allegiance.strength`. No person→place edge kind
   exists; `acceptance.*` is place-owned collective feeling. Partial mitigation the framing missed:
   this is arguably the "nine parallel personal meters" cut working as intended. — **omission**
8. **[SOFTEN — against the brief's own framing] `RELATION_SHARE_MAX` does *not* make beliefs and
   feelings decorative by construction.** The cap binds only summed selection terms (`01:386-404`).
   Uncapped channels exist and are load-bearing: form-transition gates read gauges/tags/form directly,
   `allegiance`'s four transitions, Knot rupture, and `09`'s advance predicates all fire off affective
   state with no cap; the creed-revision → Scar → conviction path exits the cap entirely. Beliefs alone
   lack a gate consumer today — that is finding 5's omission, not the cap's arithmetic. **The cap is
   sound design and should survive.**
9. **[NIT] `08 §6.3`'s "the Finding's witness set" is undefined** — though see T9 finding 2: the
   registered `scene.investigation_resolved` already carries a `witnesses` field.

> **Critic's coverage note, preserved.** Verified against disk: `01`, `01p2`, `02`, `02p2`, `08`, `10`,
> `11` in full; `09` at four sections; `00` in full; `module_contracts.yaml`; the epistemic proposal;
> `characters_flow_skeleton_v1.md`; `ARCHIVED.md`; plus `04`, `05`, `05p2` — the belief-consumer hunt
> that produced findings 5 and 6. Not read: `03`, `06`, `07`, `12`, `13` beyond greps — *"a feelings
> consumer hiding there would soften finding 7's edges, not its center."*

---

# T3 — Memories are fallible, people are biased, and there can be multiple perspectives on one event

**Verdict: STRUCTURALLY BLOCKED.** The objects are first-class and ruled; every producer of a divergent
account is absent, broken or blocked.

## T3 steelman

Most of this is Jordan-ruled rather than authored on spec. A claim is a content-addressed
`Proposition`; agreement is id-equality, contradiction is id-equality-with-opposed-stance,
corroboration is provenance-union over one id. A belief is a per-holder `Holding` with
`stance ∈ {asserts, denies, suspects}` (P2), so *A asserts P, B denies P* is one proposition and two
people. `support_refs` MAY be empty (P3), so rumour, prejudice and fabrication are representable and
**the lie is a first-class row, not a flag**. `01 §3.1`'s two-list split (`01:298-304`) is the sharpest
move in the suite: `provenance` answers *why does this row exist*, `support_refs` answers *how do you
know*. Truth is never stored on the row; P5 rules confirmation arrives only through consequence,
preserving P-08 without a truth oracle. `10 §3.2` then makes misperception load-bearing: a
`witness_key` Slate item is built from a witness's Holding *whose proposition may simply fail to
obtain* (`10:390-405`) — the player's window on the world routed through a fallible head.

## T3 findings

1. **[BLOCKER] The credence ghost** (**X-1**), reached independently. `08`'s stated motivation —
   *"nothing could move a person's belief after they were generated"* (`08:346`) — **is still true
   after `08`'s fix**, because the fix targets a ghost. `13`'s P0-11 catches `npc_memory`, the hash and
   `causes[]`; it does **not** catch this dangler. — **structural**
2. **[BLOCKER] Perception is not modelled; every belief is authored at birth or handed down by a
   verdict — and the verdict path *converges* witnesses rather than diverging them.** Every Holding
   producer: `cg.stage`'s ≤3 creed seeds (blocked on `npc_memory`); `08 §6.3`'s write-back (broken);
   nothing else. The suite's minimum key-type set contains **no epistemic key type** — not
   `state.proposition_revised`, and not the ruled design's `scene.witness` observation edge, which the
   suite silently drops. Meanwhile the tree already *emits* `scene.witness` (`module_contracts.yaml:630`)
   and `npc_memory` consumes `scene.gossip` (`:388`), and nothing connects either to a Holding. Even as
   designed, `08 §6.3` deposits *the same sign and magnitude for every witness* — a consensus broadcast,
   the exact opposite of two people holding incompatible accounts. **Lying is representable as a row and
   unperformable as an act:** there is no transmission channel by which one agent puts a Holding into
   another's store. — **structural**
3. **[DEFECT] The hashing "answer" is a discipline, not a rule, and the suite disagrees with itself
   about whether it exists.** `01 §3.1` claims an *"in-suite answer"* (`01:312-317`); `13` P0-11 still
   calls the rule *"unspecified … the precedent to copy"*. `10 §2.2` specifies a hash *class* over five
   fields that are all refs or sorted ref-lists; the Proposition tuple adds a scalar-or-null `object`
   and an *optional* qualifier, and the ruled design's own §9 names qualifier stability as its one
   unverified item. Canonical encoding of null-vs-absent, scalar typing, qualifier order and partial
   qualifiers is specified nowhere. **Five specific silent failures** if two agents hash differently:
   (i) corroboration and contradiction detection void — a lie never collides with the truth;
   (ii) tag dedupe on `(owner, kind, prop_id)` fails, so duplicates consume `HOLDING_CAP` and the sweep
   evicts genuine beliefs; (iii) `02`'s Embrace transition never matches — the *looks-live-and-is-dead*
   class `01 §6.1` prosecutes; (iv) Python/GDScript divergence invisible to goldens; (v) the engine's
   truth evaluation misses the preimage, so hook conditions are silently false. **And one failure
   survives a perfect hash:** *"Torben was at the mill (season 12)"* and *"Torben was at the mill"* are
   two ids with no entailment relation, so `A asserts P@q, B denies P` is not a detected disagreement —
   a granularity gap in the grammar, not the hash. — **structural**
4. **[DEFECT] `Key.causes` fails *open*, not closed.** The ruled metric counts `support_refs` whose
   ancestries are disjoint — and **empty ancestries are pairwise disjoint**, so one witnessing retold
   three times counts as three independent supports. Today `confidence` can mean only an authored
   magnitude; a naive implementation would **launder correlated rumour into corroboration**. `13`
   P0-11 names the blocker but not the direction. *(Cited line numbers in the ruled design have drifted
   — see [05](05_independent_verification.md).)* — **sharpen**
5. **[DEFECT — the finding the authors would dispute] The central bargain makes catastrophic deception
   impossible by construction, and the suite never prices that against the throughline.**
   `RELATION_SHARE_MAX` caps every Holding inside the relational share of every selection function, and
   its reachability bar *guarantees* the structurally-worst option can never outrank the best. Every
   selection function otherwise reads **true** world state directly. So an agent can be ill-disposed but
   never *wrong about the board*: a false belief decides only near-ties. *"Someone must be able to be
   wrong and act on it"* is satisfied at the margin and forbidden at the center. The authors would say
   deception's teeth belong in the Slate channel, not the selection channel; the dispute resolves against
   them because with finding 2 belief is doubly inert — unproduced, and where produced, capped. **A lie
   that cannot change any outcome is flavour text with provenance.** — **structural** → escalated to **J-1**
6. **[DEFECT] P-08's cast gate implements *transport* knowability; metaphysical inaccessibility is
   asserted, not mechanised.** The gate checks channel non-emptiness; the candidate row carries no
   Thread-constitution marker and no TS read; *"arrives thinner"* names no mechanism that strips the
   payload. Canon's own P-08 instrument is a TS gate on evidence (`character_canon_v30.md:170`), and
   nothing in `10` reads TS, so `co_located` grants direct perception to a TS-0 player unfiltered. **The
   five-channel roster does not itself re-institutionalise the barrier** — but composed with finding 2,
   every *reachable* channel is institutional record or presence, because the one testimonial channel has
   no producer. So the barrier the player experiences is institutional, which is the reading P-08 exists
   to forbid. — **omission**
7. **[GAP] The ruled P1 spawn obligation is unanswered where it lands.** `03_world_population.md`
   contains no Holding or proposition content; only the ≤3 creed seeds exist. The ruling's "cheap answer"
   — an NPC believes only what they observe — is incoherent while observation does not exist: it means
   *believes nothing, forever*. — **omission**
8. **[GAP] Holding storage has two claimed homes** — the same finding as T2 finding 3, reached
   independently. — **structural**
9. **[NIT] The ruled design's `causes` line citations have drifted** (`:317/:166/:389` → `:328/:232/:399`).
   Substance holds. — **wording**

> **Critic's coverage note, preserved.** The critic explicitly recorded that it did not interpret its
> throughline through the repository's earlier throughlines corpus, and that `references/throughlines_meta.md`
> is cited nowhere in its ruling except where the suite itself cites it.
