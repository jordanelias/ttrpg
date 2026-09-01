# Lane B — code architecture: keys, wrappers, modularity, ownership, primitives

**Model:** Fable 5.1 · **Agent:** `valoria-critic` (Read/Grep/Glob only) · Grep and Glob worked.

## Verdict (lane's own words, condensed)

The proposal's strongest claim — that R-1/R-2 + T5/T6 already constitute a holonic container
architecture — **survives as a structural observation**, but the three "missing" pieces do not survive
as written. **M1 fails its own falsifier**: the ONE RULE is stated over the *world* tree while the
wrapper that owns it is placed on the *code* tree the proposal itself says is *"not the same tree"*;
and T5, T6 and WITNESS are each a third kind of crossing — **so the rule either forbids the head's own
mechanics or is vacuous.** Worse, **no in-chain record carries a rung target at all**, so the
"narrowed" N-line is not narrowed but **empty**. M2's spine **is not a strict tree at two of five
edges**. M3's "two of six" is **at most one**. C4's boundary is real but under-specified.

## The fatal findings

| # | claim | what is wrong |
|---|---|---|
| **F1** | the ONE RULE (aggregate up / refraction down, nothing else crosses) | **OVERTURN — completeness.** Three head mechanics are neither. (i) *"A cluster has no container… `respondent_venue` is a `Venue` whose `container` field may be a Rung, an Office, or **NONE**"* — a containerless venue has no position in the rung tree. (ii) *"It travels by being noticed, **not down a chain of posts**"*; *"**scope enumerates EXECUTORS, not places**"* — **the head explicitly refuses the tree-descent model the rule encodes.** (iii) WITNESS: *"FAN-OUT IS GLOBAL AND ONE PASS"*, observers from the presence index across five channels. **Either the rule forbids the head's own WITNESS (fatal) or it binds nothing** |
| **F2** | the wrapper is "at the SUBSYSTEM level of the spine" and is "where §2's rule is applied" | **OVERTURN — address.** The rule quantifies over rung parents/descendants; the wrapper sits on the code tree. The proposal's own words: *"the whole point of §2.1 is that they are not the same tree."* **A subsystem has no parent rung and no descendant rungs**, so D4's "checks direction and target" has no referent. **The proposal commits the level/axis conflation it diagnoses in others** |
| **F3** | N-line *"survives, narrowed"* | **OVERTURN — the N-line is FALSE, not narrowed.** No in-chain record has a rung target. Events have no target field **and no actor** (*"attribution is a per-witness Claim"*). Acts are already bounded at the option set by `eligible()` / `remit.scope_rung` / presence. **The only record with a target is the engine `Key`, which the proposal's own §0 rules out of scope.** Its own falsifier applies: *"this document is void and should be deleted rather than trimmed"* |
| **F5** | MATTER is per-rung; *"nothing crosses"* | **SHARPEN — falsifier met.** Travel legs; the actorless event channel (one Event spanning many rungs — **sharding it breaks `causes[]`**); death setting `until` on *"**every** Tenure the deceased held"*, including offices at other rungs; `yield` reading `season_factor`, a world quantity. **Containers partition ONE step's body, not two** |
| **F8** | the spine is a strict six-level tree | **OVERTURN at two edges, by the document's own test.** ROLE: *"the engine names the ROLE"* — roles are the engine's vocabulary, and one role (`contest`) has three providers. **Which the head intends is UNVERIFIED in-chain; both horns break the tree.** KEY TYPE: a type is consumed by many modules, so it has many module parents — **an index over modules** |
| **F10** | `phase:` is the missing check | **OVERTURN — N-line false.** *"Make the write class a PARAMETER of the store API. Then 'no write outside the matrix' is **mechanical**"* — **per write site, finer than any per-module declaration.** And `phase:` cannot be single-valued: Date, ConveningCondition, Tenure and carrier existence are each written in two or three steps |
| **F11** | C4's boundary: structural edges cannot rebuild a ratchet | **SHARPEN — a third clause is needed.** *"A revoked tenure is a **historical claim subject** — argued over, read for entrenchment"*, and `entrenchment` *"has nothing to read"* without it. So a count over live **and ended** rows is monotone; *revocations ever*; a grievance ratchet — **each built only from structural edges, each evading clause 2.** Needs: **aggregate only over live edges (`until == null`)** |

## Things it attacked and could NOT break

H1 (one type, eight kinds); **the barrier/clock argument and the C1 table**; D3's demote-only
extension; the four NEVERS against D1/D3; the census's D-20 and D-17 verifications; incumbent A's
hierarchy.

## Corrections it would NOT make

- **Not move the wrapper to per-Rung to rescue the rule.** *"It is the container the head refuses one
  refactor away, and it violates the proposal's own first NEVER. The cure costs more than M1 is worth."*
- **Not add a `target`/actor field to `Event`.** *"Attribution was deliberately removed so that covert
  action and false attribution are expressible; a target field is attribution's twin. The absence of
  direction on Events is a design choice, not a hole — which is why the DELETE branch is the honest one."*
- **Not strike the level/axis distinction.** *"It is the best content in the proposal; the spine should
  be fixed TO it, not the distinction abandoned because the spine fails it."*
- **Not turn `grade: absent` into a validator or dashboard.** *"Prose or nothing."*
- **Not soften F5 to keep "two of six".** *"A headline that survives only by ignoring its own
  falsifier is the thing this repository keeps paying for."*

## Observations left for other lanes

`envelope` is the one stored aggregate at a Rung — demographic, matter not social; **does not break
C4**, and the proposal's *"no social aggregate"* phrasing *"is exactly right and should not be widened
to 'no aggregate'."* · **Travel legs have no ownership row** despite the table's own test. · The head
is inconsistent on whether refraction is emitter- or receiver-side. · SUBSYSTEM = *"one lane, one
folder"* is imported from the ARCHIVED #339.

## Disposition in this session

**F1, F2, F3 → the wrapper deleted**, its post-mortem kept at `ARCHITECTURE.md` §44, and §6 written to
state the lateral topology whose absence caused the bad rule. **F5 → §31's per-owner partition.**
**F8 → §41's spine cut to three levels below GAME, with ROLE/KEY TYPE demoted to axes and the
role↔subsystem ordering stated as unresolved.** **F10 → §41.4, `phase:` a set and worth one check.**
**F11 → §22.4's third clause.** The `envelope` and travel-leg observations → §22.3, §31.1.
