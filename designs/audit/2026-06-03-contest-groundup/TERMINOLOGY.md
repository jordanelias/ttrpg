# Contest system — terminology log

**Purpose.** Catalog every defined term in the contest package, link where it is used, and record its
relation to canonical Valoria vocabulary — so naming collisions (the `Leverage` case) are documented
and Jordan-adjudicable rather than silently renamed.

**Method / scope.** Terms taken from the package source (read in full). Canonical relations checked by
grepping the six highest-overlap canon docs this session: `designs/scene/social_contest_v30.md`
(the canonical predecessor of this system), `designs/scene/combat_v30.md`, `params/core.md`,
`params/combat.md`, `designs/scene/derived_stats_v30.md`, `designs/provincial/faction_layer_v30.md`.
**Not** grepped against all ~115 canonical sources — "local" below means "not found in those six," a
full-canon grep is pending. `[UNVERIFIED]` marks an overlap whose *meaning*-match is unconfirmed.

**Relation legend.** `LOCAL` new to this system · `ENGINE` shared canonical resolution engine ·
`CONVERGE` canonical term, same meaning · `DIFF` same word, different meaning (mild collision) ·
`DIVERGE` canonical term this redesign replaced/omits · `VERIFY` appears in canon, meaning unconfirmed.

## The headline: this is a clean-room redesign of an existing CANONICAL system
`social_contest_v30.md` ("SOCIAL CONTEST SYSTEM v2", CANONICAL, approved 2026-04-17) already exists and
already shares this redesign's **core principle** — its §1 is literally "FORMAT FOLLOWS CONTEXT" (the
genre/venue determines the contest), the same foundation the redesign re-derived from the rhetoric
corpus. Convergence on the principle; **divergence on the resolution model**:

- Canon resolves a contest through **Composure** (a depleting resolution resource, PP-234) and stakes
  it in **Conviction** Scars (§6.2). The redesign uses neither — it accumulates abstract **advancement**
  toward a **venue win-condition**. `Composure`, `Conviction`, and `Stance` (canonical scene vocabulary)
  do **not** appear in the redesign. This is the principal reconciliation item if the redesign ever
  supersedes `social_contest_v30`.
- Canon already models the faction intersection: §10 "BOARD GAME PARLIAMENTARY VOTE" and §7 "ASYMMETRIC
  PROCEEDINGS" (Excommunication Tribunal, Succession Contest, Heresy). The redesign's assembly/court/
  appeal venues are a re-derivation of the same ground.

## Term catalog

| Term | Meaning in the contest | Used in | Canonical relation |
|---|---|---|---|
| **Stasis** (Fact/Definition/Quality/Jurisdiction, ladder) | the question at issue; what the dispute is *about* | `primitives.Stasis`; `resolver` live-ground/shift; `policy` | `LOCAL` — absent from all six docs; from the corpus (Hermagoras) |
| **Appeal** (ethos / pathos / logos) | rhetorical mode of a move; the three *pisteis* | `primitives.Appeal`; `Move.appeal`; `Resonance`; `_advance`; `policy` | `DIFF` — canon uses "appeal" for a *petition / personal appeal* (`social_contest §35` "personal appeal", and the `GraceThreshold` appeal-venue). `ethos/pathos/logos/pisteis` are `LOCAL` (in none of the six) |
| **Standing** | speaker's earned authority/credibility (ethos-built); gates hard moves, feeds readiness + leak | `primitives.Standing`; `Contestant.standing`; `ContestView.my/opp_standing`; `SelfGating`; `Readiness`; `Resonance.leak` | `VERIFY` — the word appears in `social_contest`, `combat_v30`, `derived_stats`, `faction_layer` (often as faction "standing"/Stability-collapse prose); meaning-match unconfirmed `[UNVERIFIED]` |
| **Reserve** (COST, regroup) | action-economy budget; moves cost reserve, regroup refills | `primitives.Reserve`; `Contestant.reserve`; `ContestView.reserve_frac/can_hard` | `LOCAL` |
| **Pool** | dice quantity from faculty | `primitives.Pool.size`; `engine.roll_net` | `ENGINE` — standard pool/`Argue Pool` (`social_contest §3`, `core.md`) |
| **Faculty** | the contest's skill stat (1–7) feeding pool + σ-leverage | `Contestant.faculty`; `Pool.size`; `Leverage.net` | `LOCAL` (the stat *concept* is canonical 1–7; the label "faculty" is not in the six) |
| **Leverage** | δσ into the reception roll, from faculty + on-ground | `primitives.Leverage.net` → `engine.effective_ob` | `ENGINE`/`DIFF` — **is** the canonical **σ-leverage** (`combat_v30` L1: "σ-leverage (tempo/reach/skill) gates the degree"). Bare name shadows the σ-prefixed term **and** the unrelated faction action **Economic Leverage** (ED-885). Rename candidate: `SigmaLeverage` |
| **Room** | audience receptivity, built by pathos; feeds readiness | `primitives.Room`; `Bout.room`; `Readiness`; `_advance` | `LOCAL` (one incidental "room" in `combat_v30`, not a term) |
| **Resonance** (leak, effective, tension) | how much a proof moves *this* adjudicator here (role↔character blend) | `primitives.Resonance`; `resolver._advance` | `VERIFY` — one occurrence in `faction_layer`; likely incidental `[UNVERIFIED]` |
| **Readiness** (floor) | built standing+room make appeals land | `primitives.Readiness`; `_advance` | `LOCAL` |
| **SelfGating** | a move's licitness given standing/audience (only "hard" gated) | `primitives.SelfGating`; `_apply` | `LOCAL` — from the corpus (self-gating-by-standing) |
| **DefeatCatalogue** | venue-configured fatal faults (Nyāya *nigrahasthāna*) | `primitives.DefeatCatalogue`; `Venue.faults`; `resolve` clinch | `LOCAL` |
| **Evidence / Dossier** (corroboration) | hard proof with hidden weight; relevance-gated; diminishing returns | `primitives.EvidenceItem/Dossier`; `Contestant.dossier`; `_apply` evidence; `ContestView.evidence_available` | `LOCAL` |
| **Venue** | top-down spec: win-condition + defeat-catalogue + proof weights + pressure | `resolver.Venue`; `modes` presets | `LOCAL` — but **is** canon's "FORMAT FOLLOWS CONTEXT" (`social_contest §1`) |
| **WinCondition** (ThresholdRace, TallyAtClose, ProofBar, GraceThreshold, **PersuasionTrack**) | what "winning" is, per venue | `resolver` | `LOCAL`; `PersuasionTrack` mirrors canon's two-pole **Persuasion Track** read in bands — committee/decisive/total (`social_contest §10`, §7.2) |
| **advancement** | per-side accumulated progress toward the verdict | `resolver.ContestState.adv`; `_advance`; win-conditions | `DIFF` — canon uses "advancement" for *character/arc advancement* as a reward (`social_contest §253`), not an in-contest meter |
| **Pressure** (institutional / public) | external force on the adjudicator: tilt + raised susceptibility | `contract.Pressure`; `Venue.pressure`; `_advance`/`_bias` | `CONVERGE` — canon: "the institutional pressure forces resolution or capitulation" (`social_contest §303`); same concept, here a mechanic |
| **degree** (Failure/Partial/Success/Overwhelming) | reception band of an argument | `engine.degree`; `_reception` | `ENGINE` — identical to canon's degrees; the faction **Rebuttal** table uses them (`faction_layer §5.5`) |
| **Ob / TN, μ/σ, σ-leverage** | engine target number, per-die stats, σ-space modifier layer | `engine` | `ENGINE` (`params/core.md`) |
| **Adjudicator / Panel** | the decider(s); panel = jury/bench/council aggregation | `contract.Adjudicator/Panel`; `Bout.adj` | `LOCAL` (concept canonical: `social_contest` adjudicator) |
| **Move / ContestView / FaultState** | move spec / player-visible state / accrued faults | `contract` | `LOCAL` (code types) |
| **ContestedMode + presets** (court, disputation, assembly, appeal) | institution presets over Venue | `modes` | `LOCAL` |

## Flagged for follow-up (worst-first)
1. **Resolution-model divergence (DIVERGE).** Canon = Composure + Conviction-Scars; redesign = advancement + venue win-conditions. Largest reconciliation item. Decide whether the redesign supersedes `social_contest_v30` or is a parallel model.
2. **Leverage (ENGINE/DIFF).** Same concept as canonical σ-leverage; bare name shadows it and "Economic Leverage." Rename to `SigmaLeverage` (deferred per Jordan — logged, not yet done).
3. **Appeal (DIFF)** and **advancement (DIFF)** reuse canonical words for different concepts. Low harm inside the package; matters at the canon boundary.
4. **Standing / Resonance (VERIFY).** Grep found the words in canon; meaning-match unconfirmed. Resolve by reading the canonical definitions before any merge.
