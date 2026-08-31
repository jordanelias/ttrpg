# VALORIA PR #343 — CODE SHAPE ABSTRACT
### A faithful, organized inventory of every object, type, function, constant, rule, open item and cross-draft delta specified by the proposal suite.
### Compiled 2026-08-31. **This document reviews nothing and recommends nothing.** It reproduces the suite's own vocabulary; glosses are in parentheses.

---

## §0 · CITATION KEY

All citations are `KEY:line` against these files. Where a doc quotes #342 by its own internal shorthand (`02:153`, `05:176`, `14:91-92`, …) that shorthand is reproduced verbatim inside quotes and resolves to `proposals/2026-08-29-valoria-from-scratch/NN_*.md`.

| key | file |
|---|---|
| **SUP** | `proposals/2026-08-31-ideal/10_SUPERSEDING.md` — **the terminal deliverable; authoritative code shape** |
| **SHAPE** | `proposals/2026-08-31-ideal/00_THE_SHAPE.md` — PR #342's ideal shape, superseded by SUP |
| **INT** | `proposals/2026-08-31-integration/11_INTEGRATED.md` |
| **P3R** | `proposals/2026-08-31-integration/12_PART3_RECONCILIATION.md` |
| **S01** | `proposals/2026-08-29-valoria-from-scratch/01_substrate.md` |
| **S02** | `proposals/2026-08-29-valoria-from-scratch/02_the_person.md` |
| **S10** | `proposals/2026-08-29-valoria-from-scratch/10_resolution_surface.md` |
| **S11** | `proposals/2026-08-29-valoria-from-scratch/11_code_shape.md` |
| **F01–F05** | `proposals/2026-08-30-fixes/{01_the_floor,02_the_act_economy,03_the_missing_needs,04_relational_at_settlement,05_the_blocked_cores}.md` |
| **MACH** | `proposals/2026-08-30-play-space-coverage/01_the_machine.md` |
| **COV** | `proposals/2026-08-30-play-space-coverage/08_coverage_matrix.md` |
| **ARC** | `proposals/2026-08-30-arc-reachability/04_SYNTHESIS.md` |

**Precedence declared by the docs themselves:** SUP supersedes SHAPE and the whole #342 seventeen-doc suite (SUP:3-5). `proposals/2026-08-31-integration/09_citation_ledger.md` "is the verified fact base and wins over any other document in the review suite, including this one's sources" (SUP:27-28).

---

# A. THE PRIMITIVE INVENTORY

**TRUE primitives** = nothing in the design composes them; they are the irreducible carriers. **Compositions** = built from primitives, or a query/derivation with no stored form.

## A.1 TRUE primitives (four carriers + two edge relations + one actor)

| # | name | fields / form | owned by | read by | defined at |
|---|---|---|---|---|---|
| 1 | **Person** | the only actor. Six fields: **Address · Marks · Capability · Stance · Memory (claim ledger) · Ties** | itself — "address, marks, capability, stance, claim ledger, ties; `Holding` edges and commitment edges. Everything interior" | every aggregate (all computed on demand), every judging set, every roll | SUP:166-177 (six-field table); SUP:336; origin S01:143-150 |
| 2 | **Act** | declares `touches: {(object, mode)}`, mode ∈ `{read, alter, exclude}`; carries manoeuvre fields `pool_source, obstacle_target, stake_band, aid_from` | the person who chose it | `resolve` | SUP:689; S10:153; "Three types carry everything: an `Act`, an `Event`, a `Claim`" SHAPE:139 |
| 3 | **Event** | output of `resolve`; carries the degree band as one field | the world | `witness`, per person | SUP:139-140; S10:110 |
| 4 | **Claim** | `(subject, predicate, value, when, source, confidence, visibility)` | the holder's ledger, and only there — "Knowledge lives only in ledgers" | view assembly, argument grounds, needs, estimated profiles | **SUP:221** (seven fields); ⚠ six fields at S01:228 (see §G-11) |
| 5 | **Containment edge (address)** | strict single-parent tree; a person's address is their path to root | the person | every rung, jurisdiction, aggregation | SUP:96-98; S01:28-31 |
| 6 | **Commitment edge** | `(person, faction, degree)` — per-person, may be secret | the person (SUP:336) / the faction's commitment map (SUP:339) | `presence/density/footprint`, revolt comparison, requisition | SUP:112-114, 132 |
| 7 | **`Holding` edge** | `Holding := (person, office, since, conferrer)` — an edge **on the person**, exactly as a commitment edge is | the person | `who holds X` as a **query**; "Nothing anywhere stores control" | SUP:366-369; MACH:203 (`Office := …`, `Holding :=`) |

## A.2 Structural containers and offices

| # | name | fields | owned by | read by | defined at |
|---|---|---|---|---|---|
| 8 | **Container (a rung)** | its **stake(s)** · its **judging set** · its **standing dates**, each date's `capacity` and their convening conditions · **and the matter it holds** (a hearth's `stores`, a site's `condition`, the transmission pointer). **No social aggregate, ever** | itself | R-1 compute-on-demand aggregation only | **SUP:337** (five-row table) ⚠ vs S11:97 four-row "its stake, its judging set, its standing dates. **Nothing else.**" |
| 9 | **Office** | `Office := (post, node, remit, conferral, revocation, establishment, seat_items, upkeep, dates)` | itself; **not a container** — holds no stake, no judging set, not in the containment tree | `eligible(p, act, n)`; pool sourcing | **SUP:416**; earlier 8-field form (no `dates`) MACH:203 |
| 10 | **`remit`** | `remit := (acts[], scope_node, binds)` | the office | `eligible` | SUP:417; MACH:204 |
| 11 | **Standing date** | scheduled moment at which a prize is allocated; holds `capacity(date)`, a convener office, an ordered item list | the container **or** the office | P0 firing; `carry`; `compose_agenda`; lapse | SUP:337-338, 396; S01:448-452; SHAPE:151-155 (`StandingDate: convener/items/watch`) |
| 12 | **Faction** | a **proposition** plus a **map from persons to a degree of commitment**. "That is the entire object." **No tier/level/scale field** | itself | derived profile; revolt comparison | SUP:112-114; S01:52-59 |
| 13 | **Office cluster** | `{ o : conferral_path(o) reaches root }` — **a query, never a stored set**; has offices and holders, **not members**; no owning containment node | nobody (derived) | petition addressing (SUP:850-853) | MACH:305-311; SUP:850-853 |
| 14 | **Cohort** | *same schema as a person*, with three differences: `weight ≥ 1`; each stance entry holds `(centroid, spread)`; the ledger is shared with a per-claim `reach` fraction. **One type, not two** | itself | every mechanism, unchanged | SUP:202-206; S02:532-536 |

## A.3 The four enlargements (SUP's added objects)

| # | name | form | owned by | read by | defined at |
|---|---|---|---|---|---|
| 15 | **ConveningCondition** *(enlargement 1)* | `ConveningCondition := (holder, predicate, date_form, set_by, set_at)`; `holder ∈ Container \| Office`; `date_form : (venue, horizon, convener office)`; predicate **published as a BAND, never as a trigger point** | the date-holder (container or office) | evaluated in **P0**; schedules a date; **decides nothing** | **SUP:706-718** |
| 16 | **Petition** *(enlargement 2)* | `Petition(petitioner, proposition, respondent, backing)`; `respondent ∈ ContainmentNode \| Office` | the petitioner; carried by named persons | `carry`, `compose_agenda`, lapse, supersession motion | **SUP:840-841**; ⚠ three rival respondent typings, §G-1 |
| 17 | **Site** *(enlargement 3)* | matter the design already owns — a holding, a route, a seam, a channel, a fishery. `condition(site) ∈ [0, 1]`. **Primary state lives at the finest node the act names** | the container, as *matter* (SUP:337) | `verbs(site, n)`; band-representative obstacle term | **SUP:1234-1236** |
| 18 | **Transfer act** *(enlargement 4)* | `transfer(giver, receiver, amount)` — amount in the SAME `stores` scalar, **mouth-seasons**. Not a currency | the two hearths' `stores` | `draw(h)` via two new terms | **SUP:1425-1432** |

## A.4 Person-interior compositions

| # | name | form | defined at |
|---|---|---|---|
| 19 | **Mark** | `(kind, value, legibility, presented, provenance)`. Ascribed, publicly-read. **"There is no caste field."** | S02:23, S02:35 |
| 20 | **Practice** | `(name, rank 0–5, provenance, idiom)` | **S02:153** ⚠ vs "Practice ranges 0–7" S10:33, §G-3 |
| 21 | **Stance row** | `stance[referent] = (valence −5..+5, weight 0..5, provenance: claim_ids)`; `referent ∈ Person \| Faction \| Proposition \| Place` | S02:226-227 |
| 22 | **Conviction** | thirteen canonical referents, each **a proposition row in the same stance table** — not a separate store | S02:291-293 |
| 23 | **Conviction signature** | a sparse signed vector over the thirteen, authored with each proposition | S02:296-298 |
| 24 | **Tie** | `tie(a, b) = (familiarity 0..5, last_contact, channel_class)` | S02:326 |
| 25 | **Knot** | a bidirectional edge; `depth ∈ {1, 2}`; one shared `strain` gauge; **a channel with bandwidth** | S02:351-352; SUP:177 |
| 26 | **Coherence** | stored, 10→0, orthogonal to TS | S02:427 |
| 27 | **Composure** | a per-scene resource, non-persistent, depleted by margin of loss | S10:208 |
| 28 | **View** | at most K claims, **assembled, not filtered**; must be a distinct type from `World` with no coercion | SUP:153-157; S11:79-88 |
| 29 | **Needs** | **not a field** — computed each tick, never stored; four terms | SUP:183-190 |
| 30 | **Opening / `opening_set(person)`** | computed, never stored; "exactly one routine … not a new one keyed off Dispensations" | SUP:1134-1135 |

## A.5 Political / argument compositions

| # | name | form | defined at |
|---|---|---|---|
| 31 | **Dispensation** | `Dispensation(issuer, proposition, scope, terms)`. **No bare `effect` field** — every term is typed | SUP:1121-1125 |
| 32 | **Proposition** | `Proposition = (mood, subject, predicate, value, when, scope)`; `mood ∈ { HOLDS, OUGHT }` | SUP:1514 |
| 33 | **Case** | `Case = (holder, motion, rung, grounds[])` | SUP:1515 |
| 34 | **Ground** | `Ground = (proposition, warrant, support[])` — `support[]` are claim ids from the holder's ledger | SUP:1516 |
| 35 | **Venue** | 12 fields + a 5-field door — see B.9 | SUP:1571-1574 |
| 36 | **Grievance** | **no revolt object and no revolt meter.** A grievance is a stance row with a negative attitude toward a container or a person | SUP:1081-1084 |
| 37 | **Backing** | the set of persons who have lent their stance to a petition — "that is the aggregation, and it is why there is no crowd object" | SUP:845-846 |
| 38 | **Establishment** | the named persons an office employs; supplies the **pool** for any act by remit | SUP:437-440; F02:114 |

## A.6 Objects named ONLY in superseded / non-terminal drafts

| name | form | status |
|---|---|---|
| **The WATCH** | "a predicate attached to a container that, when it becomes true, SCHEDULES A STANDING DATE" | SHAPE:55-56 — **renamed** to convening condition, SUP:706, SUP:1901 |
| **`watch` field on StandingDate** | `watch : Predicate \| NONE` | SHAPE:154 — not present in SUP |
| **`thread_condition(n)`** | a place-scoped **primary physical scalar**, written only by `resolve` in P5 on `touches:{(n, alter)}`, **read as an obstacle term** | INT:409, INT:224 — replaced in SUP by `condition(site)` **as option removal, never a roll term** (SUP:1216) |
| **`respondent_venue`** | a Venue whose container field may be a node, an office, or **NONE** | F05:66-70 — INT:447-451 calls the repair **unsolved**; SUP withdraws it (SUP:861-863) |
| **`convey(from, to, goods, quantity)`** | `settle_in_full` with the creditor precondition dropped | F05:407 — SUP ships `transfer` instead (SUP:1425) |
| **`found(founder, portion, parent)`** | `found_hearth` widened: parent = any containment node; created object = a HOLDING at parent | F05:362-366 — not carried into SUP |
| **`act_salience`** | replaces `mark_salience`, quantifying over four referent kinds | F01:194 — not carried into SUP; its premise struck at P3R:22 |
| **`unify(c, P)` / `agree(c, P)`** | a matching predicate across a mood boundary — "the only new machinery in this document" | F03:62-68 — not carried into SUP |

**Primitive inventory total: 38 live objects + 8 superseded-only = 46 entries.**

---

# B. THE TYPE / RECORD CATALOGUE — closed sets, enumerated exactly

## B.1 The three signatures (plural form ruled)
```
choose  : (Person, View)   -> Act        # no world argument. ever.
resolve : (Acts,  World)   -> [Event]    # no person argument.
witness : (Person, Event)  -> [Claim]    # the only bridge, and it is per-person
```
SUP:138-140. ⚠ **Plurality ruled:** "#342 ships three spellings … **This document uses the plural `resolve(acts, world) -> events`**" (SUP:159-162). Singular at S11:58 and S01:214.

## B.2 Containment ladder (ordered, extensible)
**Person → Hearth → Community → Settlement → Territory → Province → Realm** — "extended upward or sideways as the world needs" (SUP:96; S01:28).

## B.3 Act `touches` modes — closed, 3
`mode ∈ {read, alter, exclude}` (SUP:689). "no new mode is introduced" for sites (SUP:1236).

## B.4 `remit.acts` — a CLOSED SET OF FIVE
**issue · determine · confer/revoke · dispatch · convene** (SUP:421-424; MACH:212-215).
⚠ **`convene` names TWO distinct operations and they are separate acts**: (1) **setting** a standing date, (2) **ordering its items** = `compose_agenda` (SUP:426-431).

## B.5 `binds` — closed, 2
`binds ∈ { members-by-admission, persons-by-presence }` (SUP:418; MACH:205).

## B.6 Claim `source` — closed, 4
`firsthand(event_id)` · `told_by(person, handle)` · `inferred(claim_id…)` · `firsthand_via_knot(event_id)`. **"There is no null source, and `witness` is the only operation that mints a root token."** (SUP:243-245). ⚠ Three sources at S01:273-274 (no `firsthand_via_knot`).

## B.7 Dispensation term types — closed, 9
`PriceTerm` · `ProhibitionTerm` · `LevyTerm` · `ExemptionTerm` · `EntryStandardTerm` · `ExcommunicationTerm` · `BlockadeTerm` · `TreatyClause` · `OrdenanzaTerm` (SUP:1123-1124).

## B.8 Degree bands — closed, 5
| margin | band |
|---|---|
| ≤ −2 | **Disaster** |
| −1 | **Failure** |
| 0 | **Costed Success** |
| +1, +2 | **Clean Success** |
| ≥ +3 | **Overwhelming** |

SUP:540-546; identical at S10:88-94.

## B.9 `Venue` tuple — 12 fields + 5-field door
```
Venue = (container, prize, standing_date, judging_set_rule, decision_rule, admission_floor,
         privileged_custody, exchange_budget, article_count, coupling_depth, veto_holders,
         record_custody)
door  = (convener, enter, speak, admissible_source, attendance_cost)
```
SUP:1571-1574; identical at F04:231-233.

## B.10 Stasis ladder — closed, 4 rungs, strongest first
**Denial** (it did not happen) · **Definition** (it happened; it is not *that*) · **Quality** (it happened, it is that, and it was right) · **Jurisdiction** (this chamber may not hear it) (SUP:1525-1527).

## B.11 The twelve named faults, with severities — closed, 12
| id | fault | severity |
|---|---|---|
| **F1** | self-contradiction | `close` |
| **F2** | contradicting the record | `descend` |
| **F3** | silence when pressed | `close` |
| **F4** | shifting the ground | `descend` |
| **F5** | repetition, *defeated by any new `support[]`* | `strike` |
| **F6** | the quibble | `close` |
| **F7** | rootless ground | `strike` |
| **F8** | conceding and pressing anyway | `close` |
| **F9** | deficient pleading | `close` |
| **F10** | speaking without standing | `strike` |
| **F11** | incoherent assertion | `strike` |
| **F12** | inadmissible challenge | `descend` |

SUP:1536-1540. **Severity semantics:** `strike` kills the ground at every venue for everyone; `descend` concedes a rung and **closes nothing**; `close` force-closes the sitting against the faulting party (SUP:1540-1542).

## B.12 Proposition mood — closed, 2
`mood ∈ { HOLDS, OUGHT }` (SUP:1514).

## B.13 Stance referent kinds — closed, 4
`referent ∈ Person | Faction | Proposition | Place` (S02:227). ⚠ **a *procedure* is not among them** while at least one canon body is made of one (SUP:1941-1944).

## B.14 The thirteen Convictions — closed, 13
Faith · Authority · Order · Scholastic · Utility · Equity · Liberty · Precedent · Community · Identity · Warden · Virtue · Honor (S02:291-292).

## B.15 Mark kinds and their value sets — closed, 6 kinds
| kind | values |
|---|---|
| `heritage` | Northern Einhir · Central Einhir · Southern Einhir · Crown-Latinate · Altonian · Schoenlander |
| `house` | a hearth pointer + `main`/`cadet` |
| `grade` | apprentice · journeyman · Free Master · burgher |
| `church` | unbaptised · communicant · confirmed · minor orders · Canon · Cardinal |
| `office` | praefect · gate warden · magistrate · Grandmaster · Confessor · Doux |
| `sensitivity` | `sign ∈ {none, latent, evident, marked}` — **a *sign*, never the TS number** |

S02:26-33.

## B.16 Mark legibility classes — closed, 3
`legibility(kind, context) ∈ {open, attested, latent}` (S02:55).

## B.17 The four need kinds and what each reads — closed, 4
| need | reads |
|---|---|
| **subsistence** — the larder against the mouths | **the world** |
| **standing** — regard among your siblings-in-container | **the world** |
| **commitment** — a faction proposition you hold, unsatisfied | **the view** |
| **exposure** — what a dispensation's terms do to your options | **the view** |

SUP:185-190.

## B.18 Larder bands — closed, 5, ordered
**Provisioned → Sufficient → Thin → Hungry → Failing** (SUP:1407).

## B.19 Coherence bands — TWO INCOMPATIBLE SHIPPED TABLES (see §G-10)
**S02:444-449 (structural, no dice penalty):** 10–8 **Whole** (none) · 7–5 **Dissonant** (presented marks read at −1 confidence) · 4–3 **Fragmented** (at most 2 primary Convictions; third's weight decays 1/season; one stance row/season loses provenance) · 2–1 **Fractured** (tellings at halved confidence; **may not `carry` a petition**) · 0 **Severed** (stop individuating; return to cohort fidelity; cannot originate petitions; cannot hold office).
**S10:199 (dice penalties on Thread rolls):** 10 Whole (no penalty) · 9–7 Dissonant (−1 die) · 6–4 Fragmented (−2 dice, some Thread ops closed) · 3–1 Fractured (−3 dice, Composure halved) · 0 Severed (Thread Pool locked to zero).
**SUP:253** uses the band names as a K penalty ladder: "Dissonant 1 … Severed 5".

## B.20 Commitment degree ladder — closed, 6 (0–5), with weights
| d | name | `w(d)` | licence |
|---|---|---|---|
| 0 | none | 0 | degree 0 *is* deletion; departure needs no operation |
| 1 | sympathy | 0.15 | will not testify against a member; may be told cell-safe claims |
| 2 | sympathiser | 0.40 | may be asked for material, shelter, carriage at low cost; may `carry` a petition of the faction's proposition |
| 3 | member | 1.00 | may be **requisitioned** for acts inside ordinary capability; may `avow` |
| 4 | sworn | 1.60 | may be requisitioned for acts **against their own container's interest** |
| 5 | constitutive | 2.20 | proposition holds a Conviction-primary slot; **no offer term enters the refusal check at all** |

MACH:147-152; weights restated F03:97.
⚠ **"REPORTED, NOT RESOLVED — the licence column is live in two contradictory states"** (MACH:169-174).

## B.21 Degree × avowal — closed, 3 avowal states
`avowed` · `private` · `covert` (MACH:180-184).

## B.22 The three write classes — CLOSED, "and no others may be added"
| class | phase | what may be written |
|---|---|---|
| **calendar** | **P0** | dates and dockets |
| **matter** | **P1** | larders, bodies, travel, and the season's `yield` roll |
| **acts** | **P5** | everything else, **including every condition delta an act caused** |

SUP:669-674.

## B.23 The seven phases — closed, ordered
P0 CALENDAR · P1 SETTLE · P2 NEEDS · P3 VIEW · P4 CHOOSE · P5 RESOLVE · P6 WITNESS · P7 RECKON (SUP:645-654). **Eight labels, seven-phase naming retained from the doc's own header "SEVEN PHASES" (SUP:624).**

## B.24 P5 resolution strata — closed, ordered, 5
1 Movement · 2 Binding decisions at docket dates · 3 Contested physical acts · 4 Uncontested material acts · 5 Social acts **last** (SUP:695-698; MACH:72-76).

## B.25 The three fidelities — closed, 3
`played` · `witnessed` · `auto` — "differ only in **who is asked to choose**, never in how the outcome is computed" (SUP:617-620; S11:148-151).

## B.26 Force forms — closed, 7
`{seize, restrain, strike, burn, expel, disperse, kill}` (F04:65).

## B.27 The five channels available to a person with no office — closed, 5
requisition kin · petition · take an opening · migrate · commit to a rival proposition (SUP:1409-1410, quoting `13:31-35`).

## B.28 The four carrier choices at the rung above — closed, 4
**forward** · **amend** · **bundle** · **drop** (SUP:894-895).

## B.29 The four licensed decider-free exceptions — closed, 4
| # | channel | citation |
|---|---|---|
| 1 | **Metabolism and nature** — larders consume, crops yield, wounds close or fester, bodies age, weather happens | P1 (`09:55-59`) |
| 2 | **Matter events** — a storm, a silted channel, a worked-out seam; and §10.6's band-edge closure under its three conditions | `13:178-186`; SUP §10.6 |
| 3 | **The confidence of a memory decaying** — the third admitted clock class | `09:562-564` |
| 4 | **The calendar — LAPSE ONLY** | `05:314-316`; SUP §8.5 |

SUP:1637-1642.

## B.30 The three admitted clock-driven quantities — closed, 3
**matter, bodies, and the confidence of a memory** (SUP:1370-1371, citing `09:562-564`).

## B.31 The fourteen forbidden objects — closed, 14
1 a `World` parameter on any decision function · 2 a `view_of(world, person)` that masks rather than assembles · 3 any function taking `[Person]` and one `Event` · 4 a deposit into a cohort carrying a VALUE rather than a DISTRIBUTION · 5 a pushed aggregate, or a field one is stored in · 6 a stored aggregate, norm, density, unrest or reputation field · 7 a knowledge value stored on the thing known · 8 a second resolver, an auto-resolve formula, a fast path · 9 a `tier`, `level` or `scale` field on a faction · 10 a flat additive modifier from a person onto a roll · 11 **a personal effect on a group that is not a fraction of that group** · 12 a scheduled recovery tick on standing · 13 a per-entity branch anywhere in the resolver · 14 an authored per-person opportunity or quest object.
S11:207-222; walked object-by-object at SUP:1732-1747. ⚠ "**fourteen** rows, not twelve" (SUP:1728; INT:178).

## B.32 Three refusals OUTSIDE the fourteen rows — closed, 3
1 **No apparatus** · 2 **No threshold that fires an outcome, no stored gauge, no second resolver, no pushed aggregate** · 3 **VARIABLE, NOT THRESHOLD** — enforceable form: "**`force` and `hold` never appear in a precondition**"; additive to the named bans, never a replacement; **one-sided** (SUP:1749-1765).

## B.33 The four structural tests — closed, 4, none run
no decision function can see the world · two witnesses of one event can disagree · **a person with no office can act, petition, and receive an opportunity** · order independence (SUP:1767-1770; S11:231-241).

## B.34 Individuation triggers — declared exhaustive, 4
1 **Named** · 2 **Spread** · 3 **Divergent view** · 4 **Capability demand** (S02:543-552).

## B.35 Person-generation triggers — declared exhaustive, 5
individuation · a succession pointer resolving to a non-existent heir · an admission act needing a candidate · a petition needing a carrier at a rung with no live person · a view assembly requiring a subject the observer is looking at (S02:574-576).

## B.36 De-individuation predicate — conjunctive, 4 clauses
no Knot **and** no office **and** no live petition **and** **no other person's ledger names them** (SUP:209-210; S02:559-560).

## B.37 Knot rupture triggers — closed, 6
strain +5 · public betrayal of counsel · the partner's death · a Fell/Dissolution op targeting the partner · both partners' primary Conviction rows crossing to opposite sign on a shared referent · deliberate severance (S02:390-392).

## B.38 What a Knot adds over a maxed ordinary tie — closed, 4
1 **Unbidden deposit** · 2 **Composure buffering** · 3 **Counsel extraction** · 4 **Coherence contagion (P-12)** (S02:355-374).

## B.39 Manoeuvres at declaration — closed, 4
5.1 Reframe the pool source · 5.2 Contest the venue, not the fight · 5.3 Escalate the stake · 5.4 Draw aid from a Knot (S10:145-151).

## B.40 The five owners (ownership table) — closed, 5 rows
**Person · Container (a rung) · Office · Faction · Nobody** (SUP:334-340). ⚠ FOUR rows at S11:94-99.

## B.41 Coverage-instrument verdict scale — closed, 5
RICH · THIN · BLOCKED · SPLIT · SPECTATOR (COV:164-170).

## B.42 Arc-reachability verdict scale — closed, 5
REPRODUCED-BETTER · REPRODUCED · TRANSFORMED · LOST · NEVER-WORKED (ARC:12-16). ⚠ "the verdict scale carried REPRODUCED-BETTER with no REPRODUCED-WORSE" — struck as S-12 (INT:73).

## B.43 Integration classification — closed, 4
REVEALS · EXTENDS · CHANGES · COSTS (INT:184-188).

## B.44 Relay dispositions — closed, 3
**FIX** · **REBUT** · **DEMOTE** (SUP:1950-1951).

**Type catalogue total: 44 enumerated closed sets / records.**

---

# C. EVERY FUNCTION AND PROCEDURE SPECIFIED

## C.1 The three signatures
| fn | signature | side effects | invariant maintained |
|---|---|---|---|
| `choose` | `(Person, View) -> Act` | none | **no `World` in scope inside any decision function** — "omniscience is not something a reviewer must catch; it is something an author cannot write" (SUP:145-147) |
| `resolve` | `(Acts, World) -> [Event]` | **the acts write class (P5)** | no `Person` parameter → resolver acquires no per-actor special case (SUP:148-149) |
| `witness` | `(Person, Event) -> [Claim]` | deposits into that one person's ledger | **consensus broadcast is a type error** — no signature accepts a collection of persons and one event (SUP:150-151) |

## C.2 Resolution surface
```
Pool(person, practice) = Attribute[relevant](person) + Practice[practice](person)      # SUP:498, "10:30"

obstacle(context):
    if context.opponent is a person: return OPPOSED
    R = resistance_pool(context)
    if R <= 1: return 0                       # no roll; automatic clean success
    return round_half_up(R / 2)                                                        # SUP:517-522

Margin = successes − Obstacle                                                          # SUP:538
```
- `roll(pool) -> successes` — produced by `resolve` whenever an act's outcome is uncertain; carried as a plain integer inside the event; **never stored on the person** (S10:53).
- `resistance_pool(context)` — **always a dice-equivalent in the identical unit capability uses**; computed **on demand** for institutional cases (SUP:524-526, 531-534).
- **Opposed contest** = "the identical `roll` called twice"; margin = successes_A − successes_B, banded identically (SUP:564-566; S10:119).
- **Pre-roll exposure preview** — publishes both pool sizes and the obstacle interpretation; **"Computing that table never calls `roll`"** (SUP:574-576).
- Substream: `substream = hash(world_seed, actor_id, act_type, target_id, tick, sequence)`; `roll(pool)` advances exactly `pool` steps within its own substream (S10:174). SUP form: hash of `(world seed, tick, actor id, attempt discriminator)` (SUP:609).

## C.3 View assembly
```
view(person, question) -> at most K claims
K = 7 + Focus + 2 per Knot consulted − Coherence penalty (Dissonant 1 … Severed 5)

salience(c)    = recency(c) × confidence_live(c) × relevance(c, q) × stanceweight(c, person)
stanceweight(c)= clamp(1 + λ·agreement(c), 0.05, 2.0),   λ = obstinacy / 5
```
SUP:250-255. Invariant: **what is attenuated is retrieval, not value** (SUP:263); **absence of a claim produces absence in the view, never a widened interval** (SUP:155-157).
**F01's proposed EDIT 3 (not carried into SUP):** `salience(c) = max(product, recency(c) × confidence_live(c))` for the `firsthand` source class only (F01:255-256).

## C.4 Alignment
- `commit(person, faction, Δdegree)` — **the one membership operation**. Degree to zero is departure. **No merge, split, promote, or found-at-size** (SUP:132-133).
- `presence(f, n)` / `density(f, n)` / `footprint(f)` — rolled up from member addresses, **no declaration anywhere** (SUP:118-119; S01:66-68).
- **Two profiles:** `true profile` (from actual memberships, **nobody may read it**) and `estimated profile` (from *one person's own claim ledger*, readable by that person inside their own view) (SUP:124-128; S01:97-100).
- `eligible(p, act, n)` — consults `remit`; capacity at a node is "a query over members with an address inside the node, each of whom must be individually `eligible`" (SUP:120, `07:180-182`).

## C.5 Season loop — the seven phases
| phase | procedure | writes |
|---|---|---|
| **P0 CALENDAR** | advance the date · fire due standing dates into a docket · **evaluate convening conditions and schedule the dates they name** · recompute option availability | dates and dockets |
| **P1 SETTLE** | **metabolism and nature only**: larders consume against mouths, production resolves (`yield` rolled here with `season_factor` and its `d10`), wounds close or fester, bodies age and die, travellers advance a leg. *A site's `condition` is not written here at all* | matter |
| **P2 NEEDS** | every person and cohort computes needs. **Pure, parallel, never stored** | — |
| **P3 VIEW** | top-K claims by salience per person; **K = 3 per cohort** | — |
| **P4 CHOOSE** | `choose(person, view) -> act`, everyone, against the frozen P1 snapshot and their own ledger. **The player's submission enters here and nowhere else** | — |
| **P5 RESOLVE** | `resolve(acts, world) -> events` | acts (everything else) |
| **P6 WITNESS** | events fan out by presence and channel; `witness` per person | ledgers |
| **P7 RECKON** | claim confidence decays; ledgers evict lowest salience (**this is forgetting, not a data limit**); cohorts individuate; persons nobody remembers de-individuate | — |

SUP:645-654. **Reaction latency at person scale is one season** — "no policy can say *if he does X, I do Y, this turn*" (SUP:656-657). **Exception:** inside a contest the tick subdivides into nested exchanges (SUP:658).

## C.6 Conflict between acts
```
Every act declares  touches: {(object, mode)},  mode ∈ {read, alter, exclude}
Two acts conflict iff they share an object AND (either mode is `exclude` OR both `alter` the same field)
Conflicts route to  contest(container, prize, claimants)
Ties break on hash(act-id, world-seed) — NEVER on rank, office or list position
```
SUP:689-693. Invariant: "a rank-ordered tiebreak is a hidden power stat that never appears on a factor sheet" (SUP:693).

## C.7 `contest(container, prize, claimants)` — the single sibling-competition function
Three prizes only: **the stake · the regard of the container's members · the container's offices**. Claimants are **factions**, which need not be siblings in the tree (SUP:325-328). Reused unchanged for compliance (SUP:1141) and for conflict routing (SUP:691).

## C.8 Up-stroke procedures
```
carry(c, P):
  precondition: c holds STANDING at the respondent
  precondition: claim(c, "P exists") ∈ ledger(c)
  cost:  one item of the container's standing-date capacity   # 05:176
         AND one of c's own `seat_items`                      # 14:91-92, "hear OR CARRY"
  regard_cost(c) = Σ_{j ∈ judging_set} max(0, −stance(j, prop)) × weight(j)
  regard_gain(c) = Σ_{b ∈ backers WHO LEARN c carried} stance(b, prop) × weight(b)
```
SUP:871-877.
```
compose_agenda(v, container, date):                                          # 05:202-208
  input:   the petitions v HOLDS A CLAIM OF — not the petitions that exist
  act:     v ranks them by his own valuation — the same choose(person, view) every other act
           runs through — and admits the top capacity(date)
  cost:    ONE OF v'S OWN ACTS FOR THE SEASON                                # 05:206
  regard:  identical in form to carry's, over the judging set and over THE BACKERS OF EVERY
           PETITION HE ADMITS OR OMITS, as and when they learn               # 05:207-208
```
SUP:944-950. Invariant: **"An omitted petition is a DROP, and deposits exactly as one"** (SUP:953).
**Grievance deposit:** `m = shortfall_at_raising × weight × amplification(chain)`; **the telling's grammar decides where the grudge lands** — a claim naming an actor deposits on him; one naming only the container deposits on the container (SUP:907-910).

## C.9 Petition termination — three cases
1. **LAPSE** — the date passed and it was not heard. Trigger is a date; **the one licensed decider-free resolution in the whole design** (SUP:1010-1011).
2. **SUPERSESSION** — an ordinary motion on the stasis ladder, moved by any party or the convener, pleaded from claims the mover holds, contestable, decided by the venue's `decide_rule`, **consumes no additional `capacity(date)`; costs the mover an act** (SUP:1012-1016).
3. **AT A ROOTLESS VACANT OFFICE, IT NEVER ENDS** — no date, so no lapse and no venue at which to move it moot. **That is S19, not repaired** (SUP:1017-1023).

## C.10 Down-stroke procedures
- **Publishing a dispensation is a telling** — deposits claims by **presence and channel**, never by post; **distortion in transit is free** (SUP:1128-1131).
- `opening_set(person)` — "exactly one routine, and it is the same routine that lists any person's available acts at any time, not a new one keyed off Dispensations" (SUP:1134-1135).
- **Compliance contest:** per relevant node, `contest(container, prize = compliance-here, claimants = {enforcement, resistance})`. The roll reads **enforcer_presence** (zero if the issuer has no one to send), **local judging-set stance** (derived on demand, never stored), and **distance** (SUP:1141-1145).
- **Three down-stroke rules:** 1 **Scope enumerates executors, not places** · 2 **Delivery is not assumed** (an executor who never received it does not resolve at all — distinct from one who received it and refused) · 3 **Reports are claims, not state** (SUP:1162-1168).
- **Vacancy propagation:** four things become true by computation, **all at telling speed, not in the same tick** — compliance drops per person as a claim of the death reaches them; `licensed_standing` goes to zero on the same rule; the office's seat items go unspent; a conferral standing date opens **at the horizon its date-holder carries** (SUP:1187-1204).

## C.11 Site / commons procedures
```
Δcondition(site) = − condition(site) × f(degree) × share(actor, site)     -- resolved in P5

f(Disaster) = f(Failure) = 0 ·  f(Costed) = 1/16 ·  f(Clean) = 1/8 ·  f(Overwhelming) = 1/4
share(actor, site) = the actor's own draw from the site ÷ the site's total draw   ∈ (0, 1]
```
SUP:1261-1264.
```
condition(n) = Σ_{c ∈ children(n)} condition(c) × draw_share(c, n)        -- coarser reads, ON DEMAND
verbs(site, n) = { v : condition(n) ≥ floor(v) }                           -- band gating
condition(site) = clamp( condition(site) + Σ (this season's resolved condition deltas), 0, 1 )
                                                                          -- P5 only. ACTS ONLY.
```
SUP:1245, 1313, 1333-1334.
**Three cross-rung rules:** 1 Primary state lives at the finest node the act names · 2 Any coarser read is computed on demand · 3 **No coarser rung stores one** (SUP:1239-1242).
**Falsifier stated and runnable, not run:** "one person, one season, maximum-degree `alter` at a site with N drawers — what fraction of the site's condition moved, and how does it scale with N? It must be `≤ 1/4 × share`, and it must **fall as N rises**" (SUP:1287-1290).

## C.12 Material-life procedures
```
mouths(h)        = Σ appetite(p)
stores(h)       += draw(h) − mouths(h)             may go negative: a shortfall is a debt
margin(h)        = stores(h) / mouths(h)           seasons of cover — the only number read
draw(h)          = Σ yield(H, season) − Σ levy(d, h)                      -- #342's form
yield(H, season) = base(H) × condition(site(H)) × season_factor(territory) × (3 + d10)/8.5

draw(h) = Σ yield(H, season) − Σ levy(d, h) + Σ transfers_in(h) − Σ transfers_out(h)
          -- THE AMENDED FORM. Supersedes the above; the two transfer terms are the whole amendment
```
SUP:1391-1396, 1430-1432.
```
transfer(giver, receiver, amount)          -- amount in the SAME `stores` scalar, mouth-seasons
   precondition: giver and receiver co-present, OR the amount is entrusted to a carrier act
   effect:  stores(hearth(giver)) −= amount ;  stores(hearth(receiver)) += amount
   witnessed: by presence, per person, like any other act
```
SUP:1425-1428.

## C.13 Convening-condition procedures — five provenance rules
- **C1 · PROVENANCE** — attaching is an exercise of `convene`'s **first** operation (setting a date), performed conditionally in advance; only a person holding an office whose remit includes `convene` at that holder may attach one, and only at that holder; **public and witnessed** (SUP:766-769).
- **C2 · PRICE** — costs the setter **one of his own acts in the season he attaches it**; a date it schedules consumes the convener's **`seat_items`** in the season it fires; its items compete for that date's `capacity`; **the cap on live conditions is `seat_items(office)`** (SUP:770-777).
- **C3 · IT DECIDES NOTHING** (SUP:778).
- **C4 · WHAT THE PREDICATE MAY READ** — own state, an R-1 compute-on-demand aggregate, or the calendar. **Never a descendant's stored state; never a social quantity that is not itself a computed norm; never the true faction profile** (SUP:779-781).
- **C5 · VACANCY** — a vacant convener may not attach one, and does not stop existing ones from firing (SUP:782-785).

## C.14 Argument procedures
- Resolution is **by named fault against a checklist, not by a persuasion threshold**; every fault is computable from case state and ledgers — "which is what lets the whole thing run headless with no GM" (SUP:1533-1534).
- **Descending is irrevocable and public**; opening at rung *r* writes every rung above *r* into the record as conceded (SUP:1529-1531).
- **Force-close is the normal ending** (SUP:1550).

## C.15 Person-scale procedures (from #342, unmodified by SUP)
```
read(reader, subject, kind) → claim                                          S02:51-52
conceal = actor.practice[Passing] + actor.attr[Will]                         S02:66
pierce  = reader.attr[Acuity] + attention(reader, kind)
        + Σ prior claims the reader holds that bear on this kind, × confidence S02:67-68
attention(reader, kind) = |reader.stance[the proposition that kind indexes].valence|  S02:70

hear(hearer, telling) → Δconfidence
   Δconfidence = base × (0.4 + 0.12 × hearer.credulity) × f(hearer.stance[speaker].valence)  S02:253-254
revise(person, referent, pressure) → Δstance
   resist   = 1 + person.obstinacy + stance[referent].weight                 S02:258
   Δvalence = clamp( round(pressure / resist), −2, +2 )                      S02:267
   weight  += +1 if the pressure was survived; −1 if the pressure moved it   S02:268-269

seed_valence = clamp( round( Σ_c sig[c] × stance[c].valence / Σ_c |sig[c]| ), −5, +5 )   S02:302
seed_weight  = max_c ( |sig[c]| > 0 ? stance[c].weight : 0 ) − 1                          S02:303

bandwidth(k) = max(0, 2 − floor(strain / 3))     # unbidden deposits per season            S02:366

tell(speaker, hearer, claim, as_asserted)   — as_asserted need not equal what the speaker holds;
                                              "that divergence IS the lie"                 S01:262-266
form_knot(...)  — preconditions: Disposition +5, TS ≥ 30 both, Bonds ≥ 5, free slot        S02:399
rarity(practice, rank, node) — DERIVED; split into rarity_true (no agent) / rarity_est(observer)  S02:164-178
```

## C.16 Need procedures — pseudocode form (S02) and formula form (F03, not carried into SUP)
**S02:471-493 (pseudocode):**
```
SUBSISTENCE  urgency = clamp( 5 − floor( hearth.larder_days / (10 × hearth.mouth_weight) ), 0, 5 )
STANDING     r = percentile of regard(peer) among peers, 0..1
             care = max( stance[prop:Honor].weight, stance[prop:Identity].weight ) / 5
             urgency = round( 5 × (1 − r) × care )
COMMITMENT   urgency = round( d × unmet × stance[p].weight / 5 )
EXPOSURE     urgency = |Δ in the value of the person's own reachable options under the asserted terms|
```
**F03:86-95, 167-176 (proposed formulas, emitting `(proposition, urgency)` PAIRS):**
```
need(p, COMMITMENT):  u = w(d)/w(5) × stance(p, P).weight / 5 × unmet(p, P)
   unmet(p, P) = 1                                  if p's LEDGER holds no row unifying with P
               = 1 − confidence(c) · agree(c, P)    for the highest-confidence unifying row c
need(p, EXPOSURE):    u = clamp(0, 1,  p̂(h) · loss(h) / worth(p) )
   loss(h)  = EV(opening_set(p) | claims) − EV(opening_set(p) | claims ⊕ h)
   worth(p) = max( EV(opening_set(p) | claims), subsistence_floor(p) )
unify(c, P) — c and P agree on (subject, predicate, when∩, scope∩) and differ only in mood
agree(c, P) ∈ [0,1] — 1 / 0 for atomic values; |c ∩ P| / |P| for a SET or quantity
```
Invariant claimed: "**Rows are ranked, never summed**" (F03:100).

## C.17 Institutional procedures (from #342 and the fixes)
```
admit(committee, candidate, X) -> event conferring a mark and (optionally) an address
support(m, candidate) = α·Σ_marks stance(m→referent)·weight + β·performance
                      + γ·Σ_sponsors standing·staked_regard + δ·stance(m→candidate)
verdict = aggregation_rule over { support(m) : m in committee }            F04:96-100

requisition(asker, member, act, node)
  obstacle = base(act) + burden − 2·w(d) − regard(member→asker)/2 − conviction_bonus
  burden   = cost to the member's computed need
           + 2 · harm to the member's container's stake
           + 3 · marks the act collides with                              MACH:157-161

dispatch(holder, member, act):   costs the HOLDER one act and the MEMBER one act;
                                 one dispatch names ONE person             F02:141-146
                                 comply_pressure = claim_weight − strain   F02:144

acts_in_an_office_holder's_season
   = 1 + | { m ∈ establishment(o) : m's own choose selected an act serving the office } |  F02:171-174

P(discover | I) = 1 − exp( −pressure(I,S) × exposure(S) / θ )              MACH:190-191
exposure(edge) = Σ over q holding a claim of confidence(q's claim) × hostility(q → the proposition)  MACH:188
entrenchment(h, H) = min(1, seasons_held(h, H) / 60)   # read off transfer events, stored nowhere  F05:205
member(p, settlement s) ⟺ address(p) passes through some community c whose parent is s     F04:44
member(p, territory t)  ⟺ address(p) passes through some settlement whose parent is t      F04:45
publicity(act) = venue_factor × √(witness_count) × act_salience(act)                       F01:196
EV(smuggling run) = (price(dest) − price(orig) − transport) × volume − p(interception) × penalty  MACH:100
score(f) = capacity × (1 + 0.5·norm)                                                       F05:165
sovereign_fraction(root) — a reachability query; total and terminating even on a cyclic graph  SUP:475
```

## C.18 Module rules (architecture procedures)
- **R-1** — a rung module may read its own state and any message addressed to it. It may **not** read a sibling's or a descendant's state directly. It **may compute an aggregate over its descendants on demand**; it may not receive a pushed one and may not store one. **Compute-on-demand, never push, never store** (SUP:374-377; S11:113-125).
- **R-2** — a rung module writes only its own state. Upward influence is emitting an aggregate; downward influence is emitting a refraction. **No module reaches through another** (SUP:379-380).

**Function/procedure total: 64 distinct named functions, procedures, formulas and rule-sets.**

---

# D. THE PARAMETER AND CONSTANT TABLE

**Provenance column key.** `DERIVED` = the doc shows the arithmetic producing it. `CITED` = the doc attributes it to a named prior line (`02:153`, `04:59`, …) which is itself inside the proposal suite. `ASSUMPTION` = stated with no provenance shown. `MEASURED` = a count of an artifact (arcs, seats, cells) rather than a game quantity.

## D.1 Dice, pool and obstacle

| value | name | where used | file:line | provenance |
|---|---|---|---|---|
| **10** | die size (d10) | every attempt | SUP:494; S10:17 | ASSUMPTION (design choice, argued not derived) |
| **1–6** | scores nothing | roll | SUP:494; S10:17 | ASSUMPTION |
| **7–9** | scores one success | roll | SUP:494; S10:17 | ASSUMPTION |
| **10** | scores **two** successes | roll | SUP:494; S10:17 | ASSUMPTION |
| **0.6 / 0.3 / 0.1** | P(0) / P(1) / P(2) per die | distribution | S10:19 | DERIVED |
| **0.5** | mean successes per die | `Mean = Pool ÷ 2` | SUP:495; S10:19 | DERIVED |
| **0.45** | per-die variance | σ derivation | S10:19, S10:160 | DERIVED |
| **0.671** | σ per die; **"the constant for this die"**, owned by doc 10 | flat-shift arithmetic `X / (0.671·√Pool)` | SUP:434, SUP:495; **S10:160** | DERIVED |
| **1–7** | Attribute range | `Pool` | SUP:501; S02:135 | CITED |
| **9 + 1** | nine named attributes plus a ruled-but-unnamed tenth | `Pool` (formula never inspects a name) | SUP:501; S02:133-149 | CITED |
| **0–5** | **Practice rank (RULED)** | `Pool`; verb ladder | **SUP:284, SUP:504** ← `02:153` | CITED + ruled under the conflict rule |
| **0–7** | Practice rank (**rejected** variant) | — | S10:33 | CITED (overruled, §G-3) |
| **1–12** | **realistic Pool range (RULED)** | odds tables | SUP:284, SUP:504 | DERIVED from 1–7 + 0–5 |
| **1–14** | realistic Pool range (**rejected** variant) | S10's tables | S10:33 | DERIVED from 1–7 + 0–7 |
| **≥ 3** | practice rank at which a practice **adds verbs** to the option list | option set | SUP:504; S02:204 | CITED |
| **≥ 5** | practice rank adding verbs **unattemptable below it** | option set | SUP:505; S02:204-206 | CITED |
| **0** | practice rank meaning *never trained*; **"an untrained attempt is always legal"** | eligibility | SUP:504; S02:198 | CITED |
| **≤ 1** | `R` floor at which `obstacle` returns 0 and **no roll happens** | `obstacle` | SUP:520; S10:69-71 | ASSUMPTION |
| **round_half_up(R/2)** | obstacle from resistance pool; **R=5 → Obstacle 3** | `obstacle` | SUP:521; S10:71, S10:76 | DERIVED (the roll's own expected value) |
| **2 × Pool** | ceiling above which the attempt is **impossible and the resolver refuses to roll** | `obstacle` | SUP:528; S10:76 | DERIVED (max possible successes) |
| **≤ −2 / −1 / 0 / +1,+2 / ≥ +3** | the five margin bands | degrees | SUP:540-546; S10:88-94 | ASSUMPTION |
| **16.8%** | Costed Success at Pool 12 vs Obstacle 6 | band-reachability claim | SUP:549; S10:102 | DERIVED |
| **28.1%** | Costed Success at Pool 4 vs Obstacle 2 | band-reachability claim | SUP:549; S10:100 | DERIVED |
| **10.6%** | Costed Success in the outmatched row (6 vs 5) — **the recomputation that falsifies #342's "14–28% in every row"** | correction D-13 | SUP:550-552; S10:104 | DERIVED |
| **"14–28% in every row"** | #342's own gloss — **false against its own table** | retracted | SUP:550-551; S10:106 | retracted |
| **0.078% / 0.08%** | Disaster at Pool 14 vs Obstacle 2 | reachability of the bottom band | SUP:554; S10:108 | DERIVED |
| **0.04%** | Disaster at Pool 20 vs Obstacle 3 | reachability | S10:108 | DERIVED |
| **Pool 1–2** | range at which **Overwhelming is unreachable** (needs `successes ≥ Obstacle + 3`; one die yields at most two) | stated limit | SUP:558-560 | DERIVED |
| **≈ 6** | pool gap past which the underdog's chance falls under **~11%** | opposed contests | SUP:566-567; S10:132 | DERIVED |

## D.2 Full probability tables (reproduced verbatim)

**Mean/σ by pool (S10:37-45):** Pool 3 → 1.5 / 1.16 · 4 → 2.0 / 1.34 · 6 → 3.0 / 1.64 · 8 → 4.0 / 1.90 · 10 → 5.0 / 2.12 · 12 → 6.0 / 2.32 · 14 → 7.0 / 2.51. All DERIVED.

**Pool 8 success distribution (S10:49-51):** 0 → 1.7% · 1 → 6.7% · 2 → 14.0% · 3 → 19.6% · 4 → 20.4% · 5 → 16.7% · 6 → 11.0% · 7 → 5.9% · 8+ → 4.0%. DERIVED.

**Band table (S10:98-104), Disaster / Failure / Costed / Clean / Overwhelming:**
| Pool vs Obstacle | Dis | Fail | Costed | Clean | Overw |
|---|---|---|---|---|---|
| 4 vs 2 (balanced) | 13.0% | 25.9% | 28.1% | 28.9% | 4.2% |
| 8 vs 4 (balanced) | 22.4% | 19.6% | 20.4% | 27.6% | 10.0% |
| 12 vs 6 (balanced) | 27.1% | 16.4% | 16.8% | 25.5% | 14.3% |
| 8 vs 2 (favoured) | 1.7% | 6.7% | 14.0% | 40.0% | 37.6% |
| 6 vs 5 (outmatched) | 64.2% | 18.0% | 10.6% | 6.6% | 0.6% |

**Opposed-contest table (S10:125-130), A wins / B wins:** 8 v 8 → 42.6% / 42.6% · 10 v 8 → 56.8% / 29.9% · 10 v 6 → 71.1% / 17.5% · 12 v 6 → 80.8% / 10.7% · 12 v 4 → 90.8% / 4.2% · 14 v 4 → 94.8% / 2.2%. All DERIVED.

## D.3 View, salience and memory

| value | name | where used | file:line | provenance |
|---|---|---|---|---|
| **7** | base K constant in `K = 7 + Focus` | view budget | SUP:253, SUP:283 | CITED (`03:325-329`), ruled over `09:63`'s 12 |
| **+ Focus** | K's variable term | view budget | SUP:253 | CITED |
| **8..14** | resulting K range under `7 + Focus` | view budget | INT:426-427 | DERIVED |
| **12** | K as a flat constant — **the rejected variant**, asserted four times at `09:63, :133, :151, :490` | view budget | SUP:283; INT:427-428; MACH:40; F01:264 | CITED (overruled, §G-25) |
| **+2 per Knot consulted** | K bonus | view budget | SUP:253 | ASSUMPTION |
| **1 … 5** | Coherence K penalty ladder (Dissonant 1 … Severed 5) | view budget | SUP:253 | ASSUMPTION |
| **3** | K per cohort | P3 | SUP:650; MACH:40 | CITED |
| **0.05 / 2.0** | `stanceweight` clamp floor / ceiling | salience | SUP:255 | ASSUMPTION |
| **obstinacy / 5** | λ in `stanceweight = clamp(1 + λ·agreement, …)` | salience | SUP:255 | ASSUMPTION |
| **0.05** | the worked floor a Templar at obstinacy 5 gets — "**one twentieth** of an agreeing claim's" | worked case | SUP:258-260 | DERIVED |
| **L = 200** | ledger size above which P7 evicts lowest salience | P7 forgetting | MACH:43 | ASSUMPTION |
| **0.9 / 0.7 / 0.5** | base confidence for `open` / `attested` / `latent` legibility | mark reads | S02:56-58 | ASSUMPTION |
| **0.0014** | the control's landing-claim salience under the flat product (`0.6 × 0.9 × 0.05 × 0.05`) | F01's EDIT-3 case | F01:260 | DERIVED |
| **~40th of 60** | its rank under the flat product | F01's EDIT-3 case | F01:260 | DERIVED |
| **0.54** | its salience under the firsthand floor | F01's EDIT-3 case | F01:262 | DERIVED |
| **≈ 0.95 / ≈ 0.9 / ≈ 0.9** | competing floored firsthand claims (bread dearer / reeve collected / carting short) | F01's EDIT-3 case | F01:262-263 | ASSUMPTION |
| **14th of K = 12** | Baralta's mine claim rank — "the claim that does not surface" | coverage finding | COV:30 | MEASURED |

## D.4 Person: stance, personality, Convictions

| value | name | where used | file:line | provenance |
|---|---|---|---|---|
| **−5..+5** | stance `valence` range | one stance table | S02:226 | ASSUMPTION |
| **0..5** | stance `weight` range | one stance table | S02:226 | ASSUMPTION |
| **0..5** | `credulity` range | `hear` — **and nowhere else** | S02:248, S02:255 | ASSUMPTION |
| **0..5** | `obstinacy` range | `revise` — **and nowhere else** | S02:248, S02:259 | ASSUMPTION |
| **0.4 / 0.12** | `Δconfidence = base × (0.4 + 0.12 × credulity) × f(…)` | `hear` | S02:253-254 | ASSUMPTION |
| **1** | additive constant in `resist = 1 + obstinacy + weight` | `revise` | S02:258 | ASSUMPTION |
| **−2, +2** | `Δvalence` clamp | `revise` | S02:267 | ASSUMPTION |
| **+1 / −1** | weight hysteresis: +1 if pressure survived, −1 if it moved | `revise` | S02:268-269 | ASSUMPTION |
| **× 3** | pressure multiplier for an unmet stance-commitment (`commit_degree × 3`) | pressure table | S02:284 | ASSUMPTION |
| **13** | canonical Conviction referents | stance table | S02:291-292 | CITED (setting content) |
| **−1** | the `− 1` in `seed_weight = max_c(…) − 1` | Conviction seeding | S02:303 | ASSUMPTION |
| **−5, +5** | `seed_valence` clamp | Conviction seeding | S02:302 | ASSUMPTION |
| **≥ 4** | weight at which a row is a **Primary Conviction** (derived, not stored) | Coherence, Fragmented band | S02:310, S02:431 | ASSUMPTION |
| **1 to 3** | expected count of Primary Convictions | — | S02:310-311 | ASSUMPTION |
| **~0.8** | correlation at which the Masterpiece idiom clause selects on heritage **while naming heritage nowhere** | correlated standards | S02:112 | ASSUMPTION |
| **{Equity +2, Precedent −1, Authority −1}** | worked Conviction signature for *"Remit the Einhir fine"* | seeding | S02:297-298 | ASSUMPTION |
| **{Equity +2, Scholastic +1, Precedent −2}** | worked signature for the examination-standards petition | seeding | S02:662 | ASSUMPTION |

## D.5 Thread, Knots, Coherence, Composure

| value | name | where used | file:line | provenance |
|---|---|---|---|---|
| **0–100+** | Thread Sensitivity range; **not an attribute** | Thread Pool | S02:138 | CITED |
| **floor(TS / 10)** | Thread Pool | a **second pool through the same `roll`** | S02:138; S10:192; SUP:285 | CITED |
| **TS 30** | the **one declared class gate** — below it certain verbs do not exist at any rank | eligibility | S02:140-141 | CITED |
| **TS ≥ 30 both sides** | Knot precondition | `form_knot` | S02:342; SUP:177 | CITED |
| **floor(Bonds/2) + 1** | Knot slots | slot cap | S02:337; MACH:183 | CITED |
| **Bonds ≥ 5** | `form_knot` precondition | — | S02:399 | ASSUMPTION |
| **Disposition +5** | `form_knot` precondition | — | S02:399 | ASSUMPTION |
| **{1, 2}** | Knot `depth` | contagion eligibility | S02:351 | ASSUMPTION |
| **(−2·depth) .. +5** | strain range | bandwidth, rupture | S02:351-352, S02:376 | ASSUMPTION |
| **max(0, 2 − floor(strain / 3))** | `bandwidth(k)` — unbidden deposits per season | Knot channel | S02:366 | ASSUMPTION |
| **+1** | strain accrued per each of **five** named uses | strain | S02:376-378 | ASSUMPTION |
| **−1 / season** | strain decay — **only if an `invest` act was performed** | strain | S02:378-379 | ASSUMPTION |
| **1 / 2 / 3 uses per season** | sustainable / overdraft / rupture-within-two-seasons | R-shape check | S02:384-386 | DERIVED |
| **+5** | strain at which rupture fires | rupture | S02:390 | ASSUMPTION |
| **:= −3** | `stance[partner].valence` set on rupture | rupture cost | S02:393 | ASSUMPTION |
| **−1** | Coherence cost of rupture | rupture cost | S02:394 | ASSUMPTION |
| **≥ 2** | partner Coherence drop that triggers contagion | P-12 | S02:459 | ASSUMPTION |
| **−1, once per season regardless of how many Knots qualify** | contagion magnitude and cap | P-12 | S02:459-460 | ASSUMPTION |
| **10 → 0** | Coherence range, stored, orthogonal to TS | bands | S02:427 | CITED |
| **−1 / +1** | Coherence seasonal drift | drift | S02:430-433 | ASSUMPTION |
| **≥ 3** | valence-distance at which an opposing attempt costs a Coherence step | drift | S02:431 | ASSUMPTION |
| **≥ 2** | attempts agreeing with a primary Conviction required for +1 drift | drift | S02:433 | ASSUMPTION |
| **10–8 / 7–5 / 4–3 / 2–1 / 0** | Coherence band edges (**structural variant**) | S02's band table | S02:444-449 | ASSUMPTION |
| **10 / 9–7 / 6–4 / 3–1 / 0** | Coherence band edges (**dice-penalty variant**) | S10's band table | S10:199 | ASSUMPTION |
| **−1 / −2 / −3 dice** | Thread-roll penalties by band (S10 variant only) | S10's bands | S10:199 | ASSUMPTION |
| **−1 per Thread attempt; −2 contested** | Coherence accrual | S10 | S10:201 | ASSUMPTION |
| **min(2, ⌈Will/3⌉) per season** | Coherence mitigation cap from a grounding act | S10 | S10:201 | ASSUMPTION |
| **net −1/season → Severed in 10 seasons = 2.5 years** | reachability check at three ops/season | S10 | S10:201 | DERIVED |
| **2–3 seasons** | time to Severed under contested-op-heavy play | S10 | S10:201 | DERIVED |
| **4** | seasons to the year | calendar | S10:201 | CITED (setting) |
| **+1 Strain** | cost of aid drawn from a Knot | manoeuvre 5.4 | S10:151 | ASSUMPTION |
| **halved** | Fractured-band telling confidence | S02 bands | S02:448 | ASSUMPTION |
| **−1 confidence** | Dissonant-band read penalty on *presented* marks | S02 bands | S02:446 | ASSUMPTION |
| **1/season** | third primary Conviction's weight decay in Fragmented | S02 bands | S02:447 | ASSUMPTION |
| **floor(scars/2)** | suppression-scar inheritance rate | Hearth transmission | MACH:101 | CITED |

## D.6 The site / commons enlargement

| value | name | where used | file:line | provenance |
|---|---|---|---|---|
| **[0, 1]** | `condition(site)` range | option gating, yield | SUP:1235, SUP:1333 | ASSUMPTION |
| **0** | `f(Disaster)` | `Δcondition` | SUP:1263 | ASSUMPTION |
| **0** | `f(Failure)` | `Δcondition` | SUP:1263 | ASSUMPTION |
| **1/16** | `f(Costed)` | `Δcondition` | SUP:1263 | ASSUMPTION |
| **1/8** | `f(Clean)` | `Δcondition` | SUP:1263 | ASSUMPTION |
| **1/4** | `f(Overwhelming)` | `Δcondition` | SUP:1263 | ASSUMPTION |
| **(0, 1]** | `share(actor, site)` range | `Δcondition` | SUP:1264 | DERIVED |
| **≤ 1/4 × share** | the falsifier's stated bound on one act, one season | falsifier | SUP:1289 | DERIVED |
| **1/40 of 1/4** | worked maximum for one boat among a harbour's **forty** | commons case | SUP:1275-1276 | DERIVED |
| **40** | boats in the worked harbour | commons case | SUP:1275 | ASSUMPTION (illustrative) |
| **share = 1** | single-drawer case where **one Overwhelming season moves a quarter of the condition** | withdrawn claim C-10 | SUP:1280-1281 | DERIVED |
| **clamp(…, 0, 1)** | the accumulator clamp — "part of the definition rather than an assertion about it" | `condition` accumulator | SUP:1333 | ASSUMPTION |

## D.7 Material life, yield and the larder

| value | name | where used | file:line | provenance |
|---|---|---|---|---|
| **(3 + d10) / 8.5** | the per-season yield roll | `yield` | SUP:1331, SUP:1396 | CITED (`04:59`) |
| **0.47× base** | that term's minimum | `yield` | SUP:1399-1400 | DERIVED |
| **1.53× base** | that term's maximum | `yield` | SUP:1400 | DERIVED |
| **exactly 1.0** | that term's mean | `yield` | SUP:1400 | DERIVED |
| **d10 ≤ 3** | definition of "a bad season" | `yield` | SUP:1400 | CITED (`04:62-63`) |
| **30%** | probability of a bad season | `yield` | SUP:1400 | DERIVED |
| **a quarter to a half** | a bad season's cost to a holding's contribution | `yield` | SUP:1400-1401 | CITED |
| **`stores / mouths`** | `margin(h)`, in **seasons of cover** — "the only number read" | larder bands | SUP:1393 | CITED |
| **mouth-seasons** | the unit `stores` and `transfer` are denominated in | transfer, larder | SUP:1425, SUP:1457 | CITED (`13:285-287`) |
| **> 1.0** | need(subsistence) level above which it **outweighs stance entirely** | motive ranking | SUP:1408 | CITED |
| **may go negative** | `stores` — "a shortfall is a debt" | larder | SUP:1392 | CITED |
| **10 ×** | multiplier in `clamp(5 − floor(larder_days / (10 × mouth_weight)), 0, 5)` | SUBSISTENCE | S02:473 | ASSUMPTION |
| **4.2 / 2.25 / 0.25 / 0.875** | Bekk's worked `mouths` / `draw` / `margin` / need — Hungry | control season | COV:26; F03:362 | DERIVED |
| **(2.0 − 0.25)/2.0 = 0.875** | Bekk's SUBSISTENCE under F03's `[0,1]` scale | F03 worked case | F03:362 | DERIVED |
| **2.0** | the margin constant in that clamp | F03 | F03:362 | CITED (`04 §1.2`) |
| **min(1, seasons_held / 60)** | `entrenchment(h, H)` | F05's Tallow disposition | F05:205 | CITED (`04 §3.1`) |
| **60** | seasons to full entrenchment | `entrenchment` | F05:205 | CITED |
| **≥ 0.5** | entrenchment at which reclaim deposits grievance in every person of `h` | `entrenchment` | F05:207 | CITED |
| **two hundred hearths** | the worked inference cascade — "**not a threshold firing**" | `entrenchment` | F05:210 | ASSUMPTION (illustrative) |

## D.8 Capacity, seats and the act economy

| value | name | where used | file:line | provenance |
|---|---|---|---|---|
| **`capacity(date)`** | how many items **that sitting hears** — "a term of the container, and therefore something a dispensation can change" | `compose_agenda`, `carry` | SUP:396 | CITED (`05:184-186`) |
| **11** | items the Grauwald territory court hears | worked capacity | SUP:396; MACH:117 | CITED |
| **17** | seatholders at that court | worked capacity | SUP:396 | CITED |
| **6** | carried petitions left off the floor (17 − 11) | worked capacity | SUP:896-897 | DERIVED |
| **`seat_items(office)`** | "how many things he can hear **or carry** in a sitting … Holding two offices does not double a day" | `carry`, `convene` | SUP:397 | CITED (`14:91-92`) |
| **1** | seats a praefect holds; **1** thing he carries with it | worked | SUP:397 | CITED (`05:187`) |
| **one of each** | what `carry` spends — one `capacity(date)` slot **and** one `seat_items` | `carry` | SUP:399-403, SUP:875 | ruled (D-5) |
| **`seat_items(office)`** | the **cap on live convening conditions** | C2 | SUP:774-776 | ruled |
| **1 act** | cost of attaching a convening condition, to the setter, in the season he attaches it | C2 | SUP:770-772 | ruled |
| **1 act** | cost of `compose_agenda` to the convener | agenda | SUP:948 | CITED (`05:206`) |
| **1 act** | cost of a supersession motion to the mover | §8.5 | SUP:1016 | ruled |
| **1** | acts per person **and per cohort** per season | the tick | SUP:628; F02:99-101 | CITED (`09:33`) — **OPEN, D-2** |
| **10** | acts claimed in `14 §8`'s worked ducal season header | the contradiction | SUP:634; F02:14 | CITED (contradicted) |
| **7** | verbs the same paragraph actually narrates — "wrong under every reading, including its own" | the contradiction | SUP:634-635; INT:211 | MEASURED |
| **1 + 1** | `dispatch` cost: one act to the HOLDER and one to the MEMBER; **one dispatch names ONE person** | F02's ruling 3.3 | F02:141-146 | proposed |
| **11** | acts a cohort exploit would yield — "individuate your own cohort and get eleven acts instead of one" | D-16 | SUP:1866 | MEASURED (from `14 §8`'s watch) |
| **~17,000** | acts a season the compute budget covers | cost check | F01:410 (citing `09 §10`) | CITED |
| **~9,600** | `choose` calls in a fully individuated battle | cost check | F02:368 | CITED |
| **5** | the closed set size of `remit.acts` | office | SUP:421; MACH:212 | CITED |
| **35** | praefects, governors and stewards a King's one dispensation resolves against | down-stroke | SUP:1154-1156; SHAPE:828 | ASSUMPTION (illustrative) |
| **1 season** | reaction latency at person scale | the tick | SUP:656 | CITED |
| **2 standing dates** | `exercise` zero across a whole scope → **vacant in the only sense that matters** | revocation in fact | SUP:814-815 (`14:254-256`); F05:424 | CITED |
| **1 / 2 / 4 seasons** | vacancy horizon table: untitled / titled / consecrated | F05's vacancy-by-absence | F05:425 (citing `04 §1.3`) | CITED |

## D.9 Alignment, requisition, discovery

| value | name | where used | file:line | provenance |
|---|---|---|---|---|
| **0 · 0.15 · 0.40 · 1.00 · 1.60 · 2.20** | `w(d)` for degrees 0–5 | requisition obstacle; F03's commitment need | MACH:147-152; F03:97 | CITED |
| **2.20** | `w(5)`, the normaliser in F03's `w(d)/w(5)` | need(commitment) | F03:98 | DERIVED |
| **−2 ·** | multiplier on `w(d)` in the requisition obstacle | requisition | MACH:158 | ASSUMPTION |
| **/ 2** | divisor on `regard(member→asker)` | requisition | MACH:158 | ASSUMPTION |
| **2 ·** | multiplier on harm to the member's container's stake in `burden` | requisition | MACH:160 | ASSUMPTION |
| **3 ·** | multiplier on marks the act collides with in `burden` | requisition | MACH:161 | ASSUMPTION |
| **d ≥ 3** | degree at which a refusal is witnessed by every member (at d=4) | licence table | MACH:151 | CITED |
| **publicity 2.0** | Vaynard's avowed commitment at degree 4 | worked | MACH:183; COV:136 | CITED |
| **`1 − exp(−pressure(I,S) × exposure(S) / θ)`** | `P(discover | I)` | concealment | MACH:190-191 | CITED |
| **0 → 0** | exposure 0 ⇒ P = 0 at any spend; spend 0 ⇒ P = 0 at any exposure — **no clock on either side** | concealment | MACH:191-193 | DERIVED |
| **≥ 1.0** | `venue_factor` for every act by remit — "an office-holder cannot act quietly" | publicity | MACH:203, MACH:300; F01:109 | CITED |
| **+3.02 per season** | net stance move under maximum accrual then maximum mitigation — "recoverable in roughly two seasons" | composition convention | MACH:81 | DERIVED |

## D.10 Publicity and admission coefficients (fixes only; not carried into SUP)

| value | name | where used | file:line | provenance |
|---|---|---|---|---|
| **`1 + 0.2 × (count)`** | `mark_salience` — counts only **the ACTOR'S MARKS** | publicity (current) | F01:61 | CITED |
| **1.0** | `mark_salience` for a person with no house name, grade or stigma | the floor argument | F01:67-68 | DERIVED — ⚠ **struck**: "1.0 is the identity element of a product, not a floor and not a cutoff" (P3R:22) |
| **`1 + 0.2 × |{r : ∃p ∈ JS with |stance| ≥ 3}|`** | `act_salience` (F01's EDIT 2) | proposed publicity | F01:194 | proposed |
| **≥ 3** | the strong-stance threshold inside `act_salience` and `θ` | proposed | F01:194, F01:202 | ASSUMPTION |
| **`venue_factor × √(witness_count) × act_salience`** | `publicity(act)` | proposed | F01:196 | CITED (`04 §4.1`) |
| **`θ(p) / (1 + 0.2 × |{…}|)`** | the attention floor | proposed | F01:202 | proposed |
| **< 0.5** | publicity band reaching only "the hearth, and whoever holds a Knot" | band table | F01:68 | CITED |
| **≥ 1.5** | publicity band reaching settlement-wide | band table | MACH (View 2, Settlement row) | CITED |
| **0.2 × √3 × 1.0 = 0.35** | the foster-out worked case — **stays below 0.5** | F01's control | F01:212-213 | DERIVED |
| **1.0 × 2.0 × 1.6 = 3.2** | the telling worked case — top band | F01's control | F01:220-221 | DERIVED |
| **~2×** | the marked/unmarked publicity gradient that survives D-1's strike — "a structural caste effect produced by nothing but visibility" | P3R's residue | P3R:32-34 | CITED (`04:425`) |
| **α 1.2 · β 0.3 · γ 1.0 · δ 0.5** | residence conferral coefficients, settlement court | F04's new row | F04:109 | ⚠ **ASSUMPTION, self-declared: "Two of the four coefficients in the residence row are guesses"** (F04:351) |
| **α 0.8 · β 2.0 · γ 2.0 · δ 0.5** | Crown admission coefficients | F05's Ems disposition | F05:386 | CITED |
| **β = 3.0** | Löwenritter chapter admission, deed only | F05, COV | F05:184; COV:40 | CITED |
| **8 / 13** | Bekk's live acts before / after F01's EDIT 1 | F01's re-run | F01:288 | MEASURED |
| **2 / 4** | her differently-shaped acts before / after | F01's re-run | F01:289 | MEASURED |
| **≈ 0.4** | her `need(exposure)` before the fix | F01's re-run | F01:74, F01:290 | CITED |

## D.11 F03's need arithmetic (proposed; not carried into SUP)

| value | name | file:line | provenance |
|---|---|---|---|
| **[0, 1]** | ruled urgency range; the unbounded tail belongs to **subsistence alone** | F03:46-47 | ruled in F03 |
| **`band = round(5·u)`** | `02 §6`'s `0..5` retained as a **display band**, not the quantity | F03:47 | ruled in F03 |
| **21** | guild gates named realm-wide in Vaynard's ledger | F03:276 | ASSUMPTION |
| **2 / 21 = 0.0952** | `agree` | F03:279 | DERIVED |
| **0.95** | confidence on the firsthand claim | F03:277 | ASSUMPTION |
| **1 − 0.95 × 0.0952 = 0.9095** | `unmet` | F03:280 | DERIVED |
| **1.00 × 1.00 × 0.9095 = 0.91** | Vaynard's commitment urgency — **recovers `05 §1.1`'s asserted 0.91** | F03:282 | DERIVED |
| **0.15 × 0.06 = 0.009 → 0.01** | Vaynard's exposure (Crown levy) | F03:292-295 | DERIVED |
| **0 / 0 / 0** | Vaynard's concealment exposure / subsistence / standing | F03:297-299 | DERIVED |
| **1.00/2.20 = 0.455 × 0.80 × 1.00 = 0.364** | Uln's Restoration commitment | F03:316-318 | DERIVED |
| **0.40/2.20 = 0.182 × 0.60 × 0.10 = 0.011** | Uln's Vaynard-edge commitment | F03:320-324 | DERIVED |
| **0.32 × 0.85 = 0.272** | Uln's covert-edge exposure | F03:327-332 | DERIVED |
| **0.20 × 0.50 = 0.10** | Uln's visitation exposure | F03:335 | DERIVED |
| **0.70 × 0.45 = 0.315** | Bekk's fine exposure | F03:367-369 | DERIVED |
| **0.35 × 0.60 = 0.21** | Bekk's arrears exposure | F03:371-373 | DERIVED |
| **0.50 × 0.30 = 0.15; loss 0.40 → 0.06** | Bekk's Brun exposure | F03:377-378 | DERIVED |

## D.12 Worked-character constants (S02 §9, Gerik Strand)

TS **34** · Str **3** End **4** Agi **4** / Foc **5** Acu **4** Wil **5** / Att **3** Cha **2** Bonds **5** · Kettle-smithing **4**, Passing **3**, Thread-Listening **1** · Coherence **8** (Whole) · Identity w**5**, Equity w**4**, Faith w**1** · credulity **2**, obstinacy **2** · Knot slots `floor(5/2)+1 =` **3**, one used at depth **2**, strain **+2** (S02:615-622). Conceal `3 + 5 =` **8**; Hedda pierces at **4 + 4 + priors**, holding one at confidence **0.6** (S02:635-637). Clause A costs **two effective ranks** (4 → **2**) (S02:628). Masters' attention **+4 / +3 / +2** at weight **4**; two at **0**; burgher at **−1** (S02:632-633). Vote **3–3** against a standard requiring **four** (S02:642). Aftermath: `r` falls to **0.2**, `care = 5/5 = 1`, urgency `round(5 × 0.8 × 1) =` **4**; pressure **12**, `resist = 1+2+2 = 5`, `Δ = round(12/5) = 2` → stance +1 → **−1**, weight → **w1**; Coherence **8 → 7**; bandwidth `2 − floor(2/3) =` **2**, deposit confidence **0.7**; contagion does **not** fire (drop 1 < threshold 2) (S02:646-658). All DERIVED from the constants above; the input constants are ASSUMPTION-grade.

## D.13 Instrument counts (MEASURED artifacts, explicitly not rates about play)

| value | name | file:line |
|---|---|---|
| **56** | per-NPC season probes | INT:30; COV:4 |
| **55** | characters verdicted | COV:164 |
| **RICH 33 (60%) · THIN 16 (29%) · BLOCKED 4 (7%) · SPLIT 1 (2%) · SPECTATOR 1 (2%)** | verdict tally | COV:164-170; INT:31 |
| **+1** | "a structural SPECTATOR that is not a person" — the two unfilled Cardinalates | COV:172 |
| **19 of 55 (35%)** | characters with a lane-recorded BLOCKED core; **11** verdicted RICH | COV:174 |
| **22 of 55** | "bad" verdicts (THIN/BLOCKED/SPLIT/SPECTATOR) | COV:178 |
| **8 of 25 (32%) vs 14 of 30 (47%)** | bad verdicts among office-holders vs the postless | COV:183 |
| **5 of 5 / 4 of 4** | bad verdicts among `alignment = none` / rank-1 characters | COV:186-187 |
| **64 cells; DEMONSTRATED 44 · THIN 8 · EMPTY 8 · NAMED-ONLY 2 · N/A 2** | the coverage matrix | COV:66-70 |
| **~56 of 90 ids; 25 of 55 holding office** | roster shape — "hand-assembled and elite-heavy" | INT:628 |
| **10 accept · 8 supply · 1 canon defect** | blocked-core dispositions | F05:18-20 |
| **4 edits (E1–E4)** delivering **8** supply verdicts; **3** needed nothing | sizing | F05:22-35 |
| **83 arcs** from a **55-arc** corpus at ref `v30-snapshot-2026-06-28` | arc reachability | ARC:3; INT:35 |
| **RB 40 · R 2 · TRANSFORMED 22 · LOST 10 · NEVER-WORKED 9** | arc totals | ARC:12-16 |
| **17 of 18 / 20 of 22** | arcs refused on MECHANISM in lanes 1 / 2 | ARC:19 |
| **42 of 74** | arcs whose STORY is reproduced or improved | ARC:19-20 |
| **13 / 3 / 1 / 1** | arcs closing at a sitting / at a counter / on a faction decision / by design | INT:113-116; SHAPE:17 |
| **12 stable + 3 label-disputed + 2½ lost** | the **corrected** closure-axis figure, lane-1 scope only | SUP:1806; SHAPE:322 |
| **12 of 22 / 11 of 18** | arcs running on a blocked-core character | ARC:150-151 |
| **5 of 7** | LOST arcs dying on the world-substrate hole | ARC:40 |
| **35-row** | the prior corpus's authored Trigger Inventory | ARC:103 |
| **5** | candidate forcing mechanisms checked; **none forces** | SHAPE:18; INT:129 |
| **~45 / 2 / 0** | `file:line` claims verified by lane (b)'s antagonist / substantive misreads / fabrications | INT:569-570 |
| **7 / 5 / 1** | claims struck by lane (a)'s antagonist / undeclared compliance failures / fabricated objects | INT:571-572 |
| **5 objects, one producing role, one downstream repetition** | the fabrication count | INT:563 |
| **6** | the count after P3R adds D-1 — "**so 'five' is a floor, not a count** — as is 'six'" | P3R:166-168 |
| **11** | items the review brief paraphrased §7 as, **silently dropping `:212`, `:213` and `:219`** | P3R:113-115 |
| **24 challenges: 18 FIX · 3 REBUT · 3 DEMOTE** | relay round 1 | SUP:1954 |
| **16 challenges: 14 FIX · 1 REBUT-in-part · 2 DEMOTE; 9 of 16 were regressions in round 1's own text** | relay round 2 | SUP:1990-1992 |
| **325 lines** | new round-1 prose that "went in unreviewed and behaved like a first draft" | SUP:1993 |
| **5 / 1.2 / 2 / 1 / 3** | Grauwald territory court seat weights (ducal proxy / — / praefects / Free Masters / Church) — as printed: proxy **5**, praefects **2**, Free Masters **1**, Church **3** | MACH:117 |
| **5** | article count, Crown Succession Contest, each separately proved | MACH:119 |
| **0.6 / 0.72** | `filter_share` for an under-steward / for Deacon Rusk | MACH:105; COV:160 |
| **9 dispatchable over 12 settlements** | Vaynard's reach | COV:29 |
| **0.1 vs 1.0** | `act_reach` for a non-seat-holder vs a seat-holder | F05:160 |
| **+50%** | capacity swing Stenskald's `norm` movement is worth in every contest | COV:139 |
| **0.36** | Torberg's `will` — "the comply-badly band" | COV:140 |
| **±0.15** | Geirson's only accumulating quantity | COV:111 |
| **1.44:1 / 3.9:1** | (repo-doctrine figures, not design parameters) apparatus:game ratios — recorded here only because SUP's §0 discipline references them | `CLAUDE.md` §0.1 |

**Parameter total: 214 distinct numeric values / named constants recorded.**

---

# E. INVARIANTS AND STATED RULES (verbatim, with file:line)

## E.1 Substrate and signature invariants

1. **"There is one kind of actor: a person."** — SUP:69. "Persons act. Nothing else does. Containers do not decide, factions do not decide, settlements do not decide." — SUP:90-91.
2. **"Every person has exactly one parent hearth; every hearth exactly one community."** — SUP:97.
3. **"If a person can be contained twice, divided loyalty becomes a set membership and evaporates."** — SUP:102-103.
4. **"`choose` has no `World`. Not a masked world, not a read-only world, not a world behind an accessor."** — SUP:145-146.
5. **"`resolve` has no `Person`. The world does not know who is asking."** — SUP:148.
6. **"there is no signature accepting a collection of persons and one event. Consensus broadcast is a type error."** — SUP:150-151.
7. **"`View` must be a distinct type from `World`, with no coercion, no shared supertype, and no field of `View` holding a `World`."** — SUP:153-154.
8. **"`View` is assembled, not filtered … absence of a claim produces absence in the view, never a widened interval, because a widened interval is uncertainty and the design needs ignorance."** — SUP:155-157.
9. **"Scale is derived and gates nothing."** … **"no act is unlocked or forbidden by a faction's size and no roll takes it as a term."** — SUP:116, SUP:120-121.
10. **"the true profile, computed from actual memberships, which nobody may read"** — SUP:125-126.
11. **"One membership operation: `commit(person, faction, Δdegree)` … There is no merge, split, promote, or found-at-size."** — SUP:130-133.
12. **"Knowledge lives only in ledgers."** — SUP:75.

## E.2 Person invariants

13. **"Personality is two scalars inside the stance table … and nothing more. A trait that duplicates a stance is a second copy that can disagree with the first."** — SUP:179-181.
14. **"Needs are not a field; they are computed each tick"** — SUP:183. **"needs are never stale relative to the person's view and are supposed to be stale relative to the world."** — SUP:192-193.
15. **"A person with no office can still act. Action eligibility never consults office."** — SUP:196.
16. **"An untrained attempt is legal and is just a small pool"** — SUP:198.
17. **"practice rank *adds verbs* rather than constituting the list"** — SUP:198-199.
18. **"The design's low end is right and this document does not touch it."** — SUP:200.
19. **"One type, not two: if a cohort were a different type, every mechanism would be written for one and not the other and the design would acquire an elite-only politics by accident."** — SUP:205-206.
20. **"A person persists exactly as long as somebody remembers them."** — SUP:212.
21. **"credulity is read HERE AND NOWHERE ELSE"** / **"obstinacy is read HERE AND NOWHERE ELSE"** … **"If either scalar ever acquires a second reader, it has become a trait vector and should be cut."** — S02:255, S02:259, S02:262.
22. **"There is no caste field. This is the single most important sentence in the document"** — S02:35.
23. **"the engine must never contain a line that reads a person's heritage and subtracts anything. It does not."** — S02:92-93.
24. **"Exposure is never automatic. A passing person accrues no hidden counter on a clock … There is no timer that eventually catches you."** — S02:78-81.
25. **"Advancement is caused, never ticked … There is no experience clock."** — S02:186-188.
26. **"a person's contribution to a container-scale outcome is a *fraction of the container's own capacity*"** — S02:211-213 (the anti-leverage precedent).

## E.3 Claim and knowledge invariants

27. **"`when` is a mandatory closed interval and it is universal, never existential"** — SUP:224.
28. **"Claims collide iff same subject, same predicate form, same arguments, intersecting `when`, incompatible values. Collision is computed at deposit time, in one ledger at a time."** — SUP:228-229.
29. **"The predicate vocabulary is CLOSED; the referent space is OPEN."** — SUP:231.
30. **"There is no null source, and `witness` is the only operation that mints a root token."** — SUP:244-245.
31. **"A Knot deposit *reuses* the originating event's id, so five partners feeling one rupture supply one token"** — SUP:245-246.
32. **"What is attenuated is retrieval, not value."** — SUP:263.

## E.4 The conflict rule

33. > **"THE CONFLICT RULE. Where two of #342's documents disagree about an object, the document whose declared subject is that object wins."** A document asserting a value it does not derive loses to the document that derives it. — SUP:271-273.
34. **"⚠ `exposure` is NOT in that table, because the rule does not reach it."** … "this document uses `exposure` in one sense only, the pre-roll odds preview of §5.4 … That is a scoping decision by fiat and is named as one." — SUP:288-291.

## E.5 Ownership and architecture invariants

35. **"Nobody | aggregates, norms, densities, needs, openings, scale, reputation"** — SUP:340.
36. > **"A container may hold MATTER and DATES. It may never hold a SOCIAL AGGREGATE."** … **"The line is provenance, not location."** — SUP:355-360.
37. **"An office is not a container. It holds no stake and no judging set, and it is not in the containment tree."** … **"Nothing anywhere stores control."** — SUP:366-369.
38. **"Every aggregate is a function, never a field."** — SUP:371.
39. **R-1**: "It may **not** read a sibling's or a descendant's state directly … **Compute-on-demand, never push, never store.**" — SUP:374-377.
40. **R-2**: "A rung module writes only its own state … **No module reaches through another.**" — SUP:379-380.
41. **"The module tree IS the containment ladder. Parent–child in code means containment in the world; nothing else is a parent of anything."** — SUP:382-383. "`faction/` sits beside `world/`, never inside it" — SUP:383-384.
42. **"There is no third quantity, and neither of these two was a ruling."** (of `capacity(date)` and `seat_items`) — SUP:399.

## E.6 Office invariants

43. **"`remit.acts` is drawn from a **closed set of five**"** — SUP:421.
44. **"⚠ `convene` names TWO distinct operations and they are separate acts … **Every price charged against `convene` anywhere in this document is against one of these two operations, named.**"** — SUP:426-431.
45. **"Office changes the option set and the pool source — never a modifier."** — SUP:433.
46. **"when an act is performed **by remit**, the pool is drawn from the **establishment** … not from the holder's own capability."** — SUP:435-437.
47. **"Choosing which of your people performs the act is the whole of a leader's tactical choice, and it is a choice between pools, not a purchase of a bonus."** — SUP:440.
48. **"every act by remit is public, so an office-holder cannot act quietly"** — SUP:442-443.
49. **"an unpaid establishment does not disperse, it becomes a faction and treats plunder as wages"** — SUP:444-445.

## E.7 Resolution invariants

50. **"the target is **computed, never assigned**"** — SUP:512.
51. **"Something that is not a person cannot try harder; it has one performance, fixed at the moment of the attempt."** — SUP:525-526.
52. **"If `Obstacle > 2 × Pool` the attempt is impossible and the resolver refuses to roll it"** — SUP:528.
53. **"Nothing is stored; there is no caste number."** (the Masterpiece Examination's resistance pool) — SUP:533.
54. **"An opposed contest is the identical `roll` called twice … It is not a second resolver."** — SUP:564-566.
55. **"Computing that table **never calls `roll`** — *'looking at the odds cannot consume the die'*"** — SUP:575-576.
56. **"a resistance composed from persons' private stances → a BAND, never the scalar … This is a change to #342, which publishes the composed scalar."** — SUP:586.
57. **"hidden world state gated behind investigation → a band, and the scalar is never an operand of any roll … This limb is enforced by construction; the other two are publication rules a careless implementer can violate."** — SUP:587.
58. **"Order independence is the property to guard, because its absence is invisible."** — SUP:612.
59. **"Replay is a re-run, not a log, and **no decision function may read the event log**"** — SUP:613-614.
60. **"Played, witnessed and auto differ only in **who is asked to choose**, never in how the outcome is computed."** — SUP:617-618. "A path that computes an outcome without running the same resolver is a second resolver whatever it is called, and it will diverge." — SUP:619-620.
61. **"Nothing in this design's modifier vocabulary is a bare number added to a result."** — S10:168.

## E.8 Season and write-class invariants

62. **"The tick is a season. Every person and every cohort commits exactly one act per season."** — SUP:628.
63. **"Phases run in order; within a phase everything is simultaneous."** — SUP:643.
64. **P1: "metabolism and nature only … *No social quantity moves here, no act's effect lands here, and a site's `condition` is not written here at all*"** — SUP:648.
65. **P4: "The player's submission enters here and nowhere else."** — SUP:651.
66. **P7: "ledgers evict lowest salience (this is forgetting, not a data limit)"** — SUP:654.
67. > **"There are exactly three write classes, and no others may be added."** … **"If a future object cannot be placed in one of these three classes, it does not go in the engine."** — SUP:667, SUP:678-679.
68. **"A site's `condition` is written in P5 and nowhere else"** — SUP:683.
69. **"Ties break on a hash of (act-id, world-seed) — never on rank, office or list position, because a rank-ordered tiebreak is a hidden power stat that never appears on a factor sheet."** — SUP:692-693.
70. **"no policy can say *'if he does X, I do Y, this turn.'* You anticipated or you are late."** — SUP:657.

## E.9 Convening-condition invariants

71. > **"A CONVENING CONDITION is a published predicate attached to a thing that holds standing dates which, when it becomes true, SCHEDULES A STANDING DATE. It decides nothing."** — SUP:706-707.
72. **"PUBLISHED AS A BAND, never as a trigger point"** — SUP:714.
73. **"There are ZERO exact instances."** — SUP:732.
74. **"`09:641` wins … there is no flag object; dormancy IS an act-proposition with an unmet enabling claim"** — SUP:742, SUP:746.
75. **"A convening condition schedules a date. It never places an item on an agenda."** — SUP:793.
76. **"a condition guarantees an *occasion*, not a *hearing*"** — SUP:797.
77. **"Only a person holding an office whose remit includes `convene` at that holder may attach one, and only at that holder."** — SUP:767-768.
78. **"Never a descendant's stored state; never a social quantity that is not itself a computed norm; never the true faction profile"** — SUP:780-781.

## E.10 Petition and up-stroke invariants

79. **"The respondent is a node or an office — always a person or a vacancy, never a mechanism."** — SUP:848.
80. **"A petition cannot enter a container by itself. Some person must perform `carry(person, petition)`"** — SUP:867.
81. **"Dropping is an act by a named person at a named time"** — SUP:895.
82. **"The drop is a valuation, not a threshold."** — SUP:899.
83. **"They are independent objects — each carried separately, each expiring separately, and none of them cancels another. There is no dedup and no *the matter is already before a body* rule; that would be an engine deciding a person's options."** — SUP:917-918.
84. > **"`05:211-216`, verbatim and load-bearing: *'An omitted petition is a DROP, and deposits exactly as one.'*"** — SUP:953.
85. **"burial is not free and never was; it is merely SAFE."** — SUP:996-997.
86. **"no petition is ended by a fact about the world; it ends by a date passing, or by a person's motion."** — SUP:1032-1033.
87. **"A vacant office is not a defect to route around. It is the design's most characteristic outcome"** — SUP:1055.
88. **"A three-of-four conclave with two seats empty and a third vacancy pending is **not a soft-lock** … **Stories, not a mechanism.** The enlargements exist to price that outcome, never to prevent it."** — SUP:1062-1065.
89. **"There is no revolt object and no revolt meter."** … **"A threshold would let the world revolt without anyone having decided to."** — SUP:1081, SUP:1088-1089.
90. **"a suppressed grievance is an ordinary stance row at full magnitude whose act-proposition has an unmet enabling claim … No flag is set"** — SUP:1096-1100.
91. **"This is not a settlement gauge: there is no number on Goldenfurt, only rows in the stance tables of named persons in it"** — SUP:1112-1113.

## E.11 Down-stroke invariants

92. **"There is no bare *effect* field: every term is typed"** — SUP:1122-1123.
93. **"It travels by being noticed, not by being handed down a chain of posts."** … **"deposit is never by post."** — SUP:1128-1130.
94. **"Distortion in transit is free"** — SUP:1131.
95. **"A published dispensation does not apply — it lands as a compliance contest"** … "No second resolver." — SUP:1139-1142.
96. **"Failure is never an exception"** — SUP:1145.
97. **"Scope enumerates executors, not places."** — SUP:1162.
98. **"Delivery is not assumed."** — SUP:1164.
99. **"Reports are claims, not state."** — SUP:1167.
100. **"the roll happens **once per executor**, not once for the realm"** — SUP:1156.
101. **"compliance drops for each person **as and when a claim of the death reaches them, and not one moment before.**"** — SUP:1189-1190.

## E.12 Commons / matter invariants

102. > **"Invert it. Damage to a commons REMOVES AN OPTION. It never adds difficulty."** — SUP:1216.
103. **"1. Primary state lives at the finest node the act names. 2. Any coarser read is computed on demand. 3. No coarser rung stores one."** — SUP:1239-1242.
104. > **"You can never move more of a site than your own share of it, times a degree fraction."** — SUP:1269-1270.
105. **"At a commons with many drawers, single-act closure is impossible … Closure is a collective outcome"** — SUP:1274-1277.
106. **"Bands are published in full with their inputs and **never with the trigger point that separates one band from the next**"** — SUP:1315-1316.
107. **"`alter` deltas are negative; restoration acts are positive; **nothing else moves it**, and the clamp is part of the definition rather than an assertion about it."** — SUP:1336-1337.
108. **"The obstacle term derived from a site's condition is the band's representative value, never the scalar"** — SUP:1358.
109. **The matter-channel licence, three conditions, **all of which must hold**: (1) "The quantity crossed is matter or bodies — never a social quantity" (2) "What changes at the edge is an OPTION SET — never a roll term and never an outcome. Nobody wins or loses at a band edge." (3) "The closure is an event, witnessable by presence at the site." — SUP:1370-1377.
110. **"A social threshold remains forbidden. A material one is the world having weather."** — SUP:1381-1382.

## E.13 Transfer invariants

111. **"amount in the SAME `stores` scalar, mouth-seasons"** — SUP:1425. **"One clean act plus one yield term. Not a currency."** — SUP:1435.
112. **"`witness` is per-person and presence-based, so a back-room transfer has exactly its two witnesses and no others."** — SUP:1459-1460.
113. **"The transfer act changes what can reach a postless person, not what he can do."** — SUP:1448.

## E.14 Argument invariants

114. **"`when` is a mandatory interval exactly as in §3.1, so **assertion and denial collide automatically** and no rule is needed for *these two people disagree*."** — SUP:1520-1521.
115. > **"The position you stand on is what you conceded, and how you arrived there does not matter."** … **"Descending is irrevocable and public."** — SUP:1529-1531.
116. **"Resolution is by named fault against a checklist, not by a persuasion threshold, and every fault is computable from case state and ledgers"** — SUP:1533-1534.
117. **"`strike` kills the ground at every venue for everyone; `descend` concedes a rung and **closes nothing**; `close` force-closes the sitting against the faulting party."** — SUP:1540-1542.
118. **"Exclusion in Valoria is at the second gate, not the first … **Caste is not a locked door; it is a room you may stand in silently**"** — SUP:1578-1580.
119. **"`admissible_source` is a door for evidence, not a grade."** — SUP:1589.

## E.15 No-fallback invariants

120. > **"THERE IS NO FALLBACK. If no person acts, the thing does not occur."** … **"The engine has no caretaker**, because there is no GM to be one."** — SUP:1599-1601.
121. **"Production is metabolism … Distribution is politics — grain moves because a named person decided it should. An act, always."** — SUP:1603-1604.
122. > **"VACANT-ALLOCATOR SEMANTICS. A standing date whose allocating office is vacant fires, allocates nothing, and lapses. The stock sits."** It is not redistributed, not held over, not split by default, not allocated by seniority or by any other engine rule. — SUP:1611-1615.
123. **"a seat nobody filled performed nothing and deposits on nobody"** — SUP:1626.
124. > **The falsifier: "Find a beneficial effect that no person's act produced."** — SUP:1633.
125. **"Licensed exceptions — these four, and only these four"** — SUP:1635.
126. **"Supersession is NOT licensed by this row … A convening condition's scheduling is NOT licensed by this row"** — SUP:1648-1650.
127. **"Lapse alone survives as a genuine decider-free resolution"** — SUP:1653-1654.
128. > **"Coincidence is not an exception to no-fallback. It is what no-fallback PRODUCES."** — SUP:1664-1665.
129. **"absence has no signature, and an absence with no signature is the most disputable thing a world can contain."** — SUP:1703-1704.
130. **"Nobody is lying. There is no fact of the matter about credit — only a fact about grain."** — SUP:1709-1710.

## E.16 Refusals binding this document

131. **"No apparatus."** — "This document proposes no validator, guard, register, checker or process document, and its enlargements require none." — SUP:1751-1754.
132. **"No threshold that fires an outcome, no stored gauge, no second resolver, no pushed aggregate"** — SUP:1755.
133. **"VARIABLE, NOT THRESHOLD … A quantity may vary; it may not gate. The enforceable form is narrow and is stated as such: `force` and `hold` never appear in a precondition."** — SUP:1758-1760. It is **additive to the named bans, never a replacement**, and **one-sided** — SUP:1761-1763.
134. **Row 4's new rule:** "when a closure is witnessed by a cohort, **the cohort's claim stores the construal spread its members would have produced, and an individuating member DRAWS from it and never inherits it.**" — SUP:1737.
135. **"One rule lives in one place. Every rule below is stated exactly once … If a rule appears twice, that is a defect in this document."** — SUP:22-23.
136. **"No rates about play appear in this document."** — SUP:32.
137. **"Every R-line in this document is conditional on L-4, the unanswered playable-seat list"** — SUP:39-40.
138. **"Nothing here ratifies on merge. Nothing here has executed. §0.2 of `CLAUDE.md` applies in full: done means it runs, and none of this runs."** — SUP:6-7.

## E.17 Rules from the fixes (proposed, not all carried into SUP)

139. **"One act per person per season, universal and unscaled … `09 §1.1` stands exactly as written, with no exception for office."** — F02:99-101.
140. **"The acts an office-holder cannot delegate are exactly the ones that change who serves him and who he is."** (`confer`/`revoke` and `commit`) — F02:239-240.
141. **"a person appearing in two establishments would be spending two acts. The roster must become a set of named persons with exactly one membership, or C double-counts."** — F02:398-399.
142. **"Rows are ranked, never summed."** — F03:100.
143. **"Ruled: belonging at Settlement and Territory is DERIVED, not conferred. Admission is owned once, at Community, and the upper rungs read it."** — F04:40-42.
144. **"Every venue row must carry a **named convener**, and a row without one silently reintroduces the institutional speaker B-11 refused."** — F05:538-539.
145. **"the fiction must never render an institution as a speaker"** — F05:536.

**Invariant total: 145 quoted rules.**

---

# F. THE OPEN / UNRULED SET

## F.1 The seven LIVE CHOICES formally carried to Jordan (SUP §16, SUP:1864-1872)

| # | the choice | quoted |
|---|---|---|
| **D-2** | **The act economy** | *"One act per season, or a holder's several? … **A personnel game** … **or a decree game**, where the top of the ladder sweeps. It decides whether a player-Duke experiences the top of the ladder as a promotion or a demotion, and it gates §8.3's and §11.3's economics."* ⚠ *"the one reading that is identical at every rung … carries an unpriced cohort exploit: individuate your own cohort and get eleven acts instead of one (D-16). Any answer must price that or forbid it"* — SUP:1866 |
| **§11.4** | **Is `stores` the realm's denominator?** | *"**Logistics-real force** — you retain only what you can feed where they stand … **or coin returns by the back door**, since a fungible transferable scalar functions as money whether or not it is called that"* — SUP:1867 |
| **§8.5** | **Is a rootless cluster vacancy the Consecration Crisis, or a soft-lock? (S19)** | *"**Content**: a Church that cannot fill a seat is the design working … **A defect**: a petition that can neither lapse nor be mooted is a matter suspended forever … Review (a) states plainly that **nobody has ruled which**, and this document does not rule it either"* — SUP:1868 |
| **§4.5** | **Is conferral rooted in persons or in offices?** | *"`00_INDEX.md:105-109` calls this **'Not an audit's call'**, review (a) flags it as the suite's top live choice, and the fact base marks the sweep incomplete — so the recommendation is offered, not taken"* — SUP:1869 |
| **§10** | **Is the world dying or misunderstood?** | *"Whether slow material decline is a real trajectory the player must arrest, or a fact everyone reports wrongly. §10 makes both expressible and does not choose"* — SUP:1870 |
| **§2** | **The Coherence-0 ontology** | *"Two incompatible readings ship — loss of capacity, versus *a person has become an object*. Three arcs and two named absences turn on it"* — SUP:1871 |
| **—** | **Off-board polities** | *"Altonia and Schoenland exert real pressure from off the map. *Generate a person* and *allow an actorless pressure* are different games, and the second would be the only exception to §1.1 in the design"* — SUP:1872 |

## F.2 The nineteen STATED LIMITS (SUP §15, SUP:1780-1854) — condensed with the load-bearing quote

1. **"Convening conditions are a NEW COMPOSITION, not the naming of a shipped pattern. There are zero exact shipped instances … The object stands on its N-line alone."** (SUP:1780-1782)
2. **"A convening condition schedules an occasion, not a hearing … The termination gain is materially weaker than the earlier work claimed."** (SUP:1783-1784)
3. **"OMISSION IS ASYMMETRIC WITH VACANCY … *'neglect becomes attributable'* holds for omission and **fails for vacancy**. This document does not repair that"** (SUP:1785-1790)
4. **"Petition expiry reads the world in neither of its two forms — and at a rootless vacant office there is a third case in which it never ends at all … The intuitive alternative … is **unbuildable**"** (SUP:1791-1794)
5. **"`stores`-as-realm-denominator is unresolved … the coercion layer's coin-denominated arithmetic needs re-denominating into mouth-seasons before any of it computes. That is unwritten work."** (SUP:1795-1796)
6. **"The market path to unintended rescue FAILS as filed. Gift constructs; market needs a price signal and an exchange form that do not exist."** (SUP:1797-1798)
7. **"Every R-line is conditional on L-4 … and §8's additionally on D-2 … Under a multi-act reading of D-2, **petition-spray dominates** and §8.3's economics fail."** (SUP:1799-1801)
8. **"The `:219` clearance in §14 row 11 is an argument, not a measurement. Its falsifier is stated and runnable and **has not been run**, because nothing executes."** (SUP:1802-1803)
9. **"The closure-axis count is not citable in its original form … the honest figure is 12 stable + 3 label-disputed + 2½ lost, lane-1 scope only. Both published versions of the 13-member set had different membership and summed to the same number, which is why four downstream checks passed it."** (SUP:1804-1808)
10. **"The instrument that found the missing objects detects ABSENCE, not FAILURE … nothing was executed, so a compositional failure was undetectable by construction."** (SUP:1809-1812)
11. **"FOUR vocabulary collisions survive inside the design and are ruled rather than fixed … This document picks one of each, records all four, and **retrofits none of them into #342**."** (SUP:1813-1819)
12. **"The low end was tested and is right. It is not repaired here, and it must not be 'fixed' later … **no section re-examines the postless season under the enlarged rules.** That work is open."** (SUP:1820-1822)
13. **"`vacancy-by-absence` has two named falsifiers that have not been run: the deliberate absence, and the cost of the hostage repricing at the top of the ladder."** (SUP:1823-1824)
14. **"Nothing in this document has executed. No claim here is licensed by an execution artifact, and under `CLAUDE.md` §0.2 none of it is done."** (SUP:1825-1826)
15. **"The pre-roll exposure partition is a publication rule, not a structural guarantee … **a resistance that is neither plainly material nor plainly stance-composed has no ruled row**: a forged document's quality, a fortification nobody has seen. This document does not invent one."** (SUP:1827-1830)
16. **"S19 IS NOT REPAIRED, AND IT LIMITS ENLARGEMENT 2 … an office at the root of its own cluster, whose conferral basis names neither a container nor a parent office, has **no clock**"** (SUP:1831-1838)
17. **"The DISCRETE limb of option removal is NOT CLEARED against the anti-leverage row … where nothing defends it there is no bound. The `forestall` precedent does not transfer — it is a purchase, and the goods survive."** (SUP:1839-1844)
18. **"Docs 06 AND 12 of #342 are not covered by the verified fact base … three of this document's own claims rest on a document nobody re-verified in full."** (SUP:1845-1850)
19. **"The slow fuses are ACT-ONLY. A site that decays with nobody touching it cannot be written as a term in the condition accumulator … That is a real narrowing, taken deliberately"** (SUP:1851-1854)

## F.3 The four findings recorded but NOT dispositioned (SUP §17.4, SUP:1929-1944)

1. **The ESTABLISHMENT capacity object.** *"The design has no finite, contested, durable capacity object for the named persons an office employs — it prices remit and forgets establishment. Two independent exercises named the same hole."* ⚠ narrowed from *"at any rung"*.
2. **The Coherence-0 ontology contradiction** (also §16).
3. **The `burden` term's calibration** — *"doing more dramatic work than any single coefficient in the suite, and untested by either exercise."*
4. **The procedure-referent question.** *"Stance referents are `Person | Faction | Proposition | Place`, and a *procedure* is not among them, while at least one canon body is made of one. **Likely answerable by precedent** … which makes it a design-document answer rather than a Jordan question."*

## F.4 Open items carried by the integration documents

| item | quoted | file:line |
|---|---|---|
| **L-4 · the playable-seat list** | *"the single highest-leverage open question for both bodies jointly. Every R-line in both surviving sets is conditional on it … **The answer needed is a list, not a principle.**"* | INT:496-500 |
| **L-1 · clock-decay on the Thread** | *"Option A (act-driven only) … Option B (a baseline decay term in P1 SETTLE) makes the peninsula a world that is dying rather than merely misunderstood. **Materially different games.** A is reversible and B is not … Arc-side support for B is **exactly one unit**. Jordan's call."* | INT:502-506 |
| **E1's repair** | *"A type admitting a vacant office, or accept the cost … **The second is design work nobody has done.** Do not propose the Person typing; it is struck."* | INT:508; INT:461-462 |
| **The `exposure` store-or-derive contradiction** | *"`exposure` has **five** distinct definitions in the suite … **Senses 3 and 4 are the same concept implemented incompatibly** … **I-4 may not ship as a rename of one sense alone**"* | INT:510-519 |
| **The `14 §8` rewrite branch** | *"One act, and one rewrite rather than two — **but only after `14:91-92`'s `seat_items` is reconciled with `14 §1`'s 'three quantities and nothing else'.** Neither lane's resolution survived and none should be improvised."* | INT:521-523 |
| **Convener cost — cheap or expensive?** | *"**Two #342 documents disagree independently of any proposal here** … ⚠ The five-lane convergence on 'the convener holds the cheapest real power' is struck (S-3). Neither option may draw support from it."* | INT:525-530 |
| **`:219` against `thread_condition(n)`** | *"**RULING: not a violation, an unexamined row.** Whether `:219` bites turns on whether *'a group'* covers *'every subsequent actor at a site'*, which the row does not define. **`thread_condition(n)` may not be treated as §7-clear until all fourteen rows are walked explicitly, starting at `:219`.**"* | P3R:107-111 |
| **The closure limit (I-A-3)** | *"**The design cannot resolve an argument whose premise is that nobody wants it resolved.** … **Falsifier standing:** find a mechanism in the suite that forces a position with no person deciding and is not P1 metabolism."* | INT:466-477 |
| **The unmeasured convergence (I-A-7)** | *"**It does not guarantee, and nothing in the suite measures, that the world produces convergence at all.** … **And the measure is refused.**"* | INT:481-490 |
| **The petition-respondent limit (E1 / D-7)** | *"**Why the repair is unsolved rather than pending.** … That moves B-11's price **from a type into prose** … The live options are two, and neither is taken here"* | INT:447-462 |

## F.5 Open items flagged inside the fixes themselves

| item | quoted | file:line |
|---|---|---|
| **The parish/community collision** | *"Resolve it the other way and the ford-side congregation is not a community, Alvid has none, and **she has no judging set for `act_salience` to quantify over at all.** This is the largest single dependency in this document, and it is somebody else's ruling."* | F01:432-438 |
| **A-6b's testimony half** | *"With firsthand claims floored, the *gap* between what you saw and what you were told widens … **This fix makes an open question more urgent. It does not answer it.**"* | F01:413-417 |
| **Establishment boundary** | *"**The establishment now needs a defined boundary, and it currently has none.**"* | F02:393-399 |
| **Cohorts and the derived act count** | *"a holder can buy throughput by individuating his own staff. That is either a fine emergent incentive … or a fidelity exploit, **and I cannot tell which from the spine alone.**"* | F02:421-426 |
| **`unify`** | *"**This is the one place a second implementer will build something incompatible.**"* | F03:434-438 |
| **The residence coefficients** | *"**Two of the four coefficients in the residence row are guesses.** α 1.2 and γ 1.0 … **They should be attacked before they are copied.**"* | F04:351-354 |
| **Territory × Relational** | *"**So Territory × Relational is N/A under one branch and borrowed-live under the other**, and which it is is not mine to settle."* | F04:327-332 |
| **`found`'s permissiveness** | *"Whether `found` should require standing at the parent is a real question and **I have not answered it**"* | F05:549-551 |
| **S8 taken, not resolved** | *"I have taken `13 §9`'s side (no currency) while giving `07 §4` the transfer it needs. That is coherent, and **it is still a ruling on a live collision made inside a disposition document, which is not where rulings belong.**"* | F05:553-556 |
| **The ten ACCEPT dispositions** | *"**If any is wrong, the failure mode is silent** … The three most attackable are **Falkenrath**, **Brandt** and **Tallow**"* | F05:563-567 |
| **Klapp's `admitting_share`** | *"**No construal-set table exists in either corpus, for any Conviction** (V18, three lanes) … whether Scholastic ever wakes him is unanswerable."* | F05:259-263 |
| **V4 / V12 / V19 canon collisions** | Baralta's marriage-basis claim vs canon's unmarried/childless (F05:155-156); canon's popular mandate the suite refuses categorically (F05:173); whether the jarldoms are heritable (F04:327-329) | F05:155, F05:173; F04:327 |

## F.6 Items MACH reports as unresolved

| item | quoted | file:line |
|---|---|---|
| **The commitment-degree licence column** | *"⚠ REPORTED, NOT RESOLVED — the licence column is live in two contradictory states … Both documents are in the suite. A season that leans on a degree-2 refusal being *illegal* rather than *expensive* is standing on the contested half."* | MACH:169-175 |
| **The conferral dilemma** | *"**The suite asserts both and resolves neither.** … Two defensible answers, materially different games."* | MACH (View 4, conferral dilemma) |
| **The un-avow / recantation gap** | *"**EMPTY.** No act retracts an avowal; departure is degree → 0"* | MACH:364 |
| **Testimony half of the salience floor** | *"**OPEN by ruling.** A firsthand claim gets a floor"* | MACH:366 |
| **A cohort conferred an office** | *"**EMPTY**, and `14 §11.6` says it could not be closed from the spine."* | MACH:381 |
| **Two Aldwins at Goldenfurt** | *"the suite carries **two Aldwins at Goldenfurt** … it will trip a lane"* | MACH:384-385 |

**Open/unruled total: 7 live choices + 19 stated limits + 4 undispositioned findings + 10 integration items + 12 fix-internal items + 6 MACH items = 58 open items.**

---

# G. DELTAS ACROSS DRAFTS

**How to read this section.** Each entry names ONE object and gives **every version** the suite ships for it, in draft order, with `file:line`. Where the terminal document (SUP) rules, the ruling is quoted; where it does not, all versions stand side by side. **No version is resolved away.** Entries G-1, G-3, G-10, G-11 and G-25 are cross-referenced from sections A, B and D and keep those numbers.

Draft order throughout: **S01/S02/S10/S11 (#342, 2026-08-29)** → **F01–F05 (fixes, 2026-08-30)** → **MACH/COV/ARC (instruments, 2026-08-30)** → **SHAPE (2026-08-31)** → **INT / P3R (2026-08-31)** → **SUP (2026-08-31, terminal)**.

---

### G-1 · A petition's RESPONDENT — four typings, three of them shipped as the answer

| draft | version | citation |
|---|---|---|
| **#342** | `Petition(petitioner, proposition, respondent_container, backing)` — a **containment node**. Consequence: *"an office cluster … has no owning node and **cannot be addressed at all**"* | S01:392; INT:442-444 |
| **F05 (E1)** | **`respondent_venue`** — *"a Venue in the sense of 14 §5 … **whose container field may be a containment node, an office, or NONE**"* | F05:66-70 |
| **SHAPE §2.3** | **A STANDING DATE.** *"A petition's respondent is a STANDING DATE, not a container."* *"It unifies with §2.2: a watch schedules a date; a petition addresses a date. **One object.**"* | SHAPE:83, SHAPE:97 |
| **SHAPE §9.1** (Jordan-directed correction, same file) | **`respondent ∈ ContainmentNode \| Office`.** *"**This is right and §2.3 is withdrawn.** I typed a petition's respondent as **a mechanism** — a date — to solve a plumbing problem, and in doing so traded away the design's central commitment: **every decision is made by a character.**"* | SHAPE:508-516 |
| **INT §5.1** | E1 is **not accepted**: *"That moves B-11's price **from a type into prose**, which is the class `11` §8.1 exists to forbid."* And the mitigation everyone reached for is *"**refuted on the text**"* — a `convener` is an office: *conferred, revocable, **vacant-able***. *"The live options are two, and neither is taken here … **The second is design work nobody has done.**"* | INT:447-462 |
| **SUP §8.1 (terminal)** | `respondent ∈ ContainmentNode \| Office`. *"always a person or a vacancy, never a mechanism"* — and the date typing is explicitly withdrawn: *"a date cannot drop a petition, and typing the respondent as a mechanism trades away the design's central commitment"* | SUP:840-841, SUP:848, SUP:861-863 |

**Residual disagreement SUP does not close:** SUP claims the office retyping *"reaches every **office cluster** … because a cluster is exactly an office set with no owning node"* (SUP:850-853) while simultaneously **withdrawing** the stronger claim — *"It said the retyping 'closes the whole direction of play that was structurally shut'. **Withdrawn (C-4).** … **Where it does not, S19 stands and the petition has no clock**"* (SUP:855-859). INT's "unsolved repair" verdict is therefore not overturned; it is narrowed to the rootless case.

---

### G-2 · The calendar primitive — its NAME, its OWNER, and the NUMBER OF SHIPPED INSTANCES

| draft | name | owner | instance count | citation |
|---|---|---|---|---|
| **SHAPE §2.2** | **"A WATCH"** | *"a predicate attached to **a container**"* | **THREE** — *"The corpus already contains this object in three places and never names it"* (`banked_claims`, a vacancy, dormant rows re-arming). *"Three independent instances is the recurrence threshold."* | SHAPE:46-56 |
| **SHAPE §3.2** | `watch : Predicate \| NONE` as a **field on `StandingDate`** — *"the only addition to #342's ownership table"* | the StandingDate | — | SHAPE:154-159 |
| **SHAPE §7.1** | (refinement) *"**A watch belongs to whatever holds standing dates — and an OFFICE holds its own conferral date.** Not only containers."* | container **or office** | — | SHAPE:406-411 |
| **SHAPE §7.2** | *"So the watch now has **four** instances rather than three"* (adds absence-vacancy) | — | **FOUR** | SHAPE:433 |
| **SUP §7.1 (terminal)** | **"A CONVENING CONDITION"**, renamed by ruling: *"Coining *watch* as a calendar primitive would give one word two shipped meanings"* — `watch` is doc 12's soldiery (`12:37`, `12:99`) | `holder ∈ Container \| Office`, as a first-class 5-tuple, **not a field on a date** | **ZERO.** *"The corpus ships the two halves … and **never the composition. There are ZERO exact instances.**"* | SUP:706-718, SUP:720-726, SUP:730-732 |

**SUP dismisses each of SHAPE's four instances by name** (SUP:734-739): `banked_claims` is *"the only verbatim instance, and this document rules it away"* under the dormancy ruling; the vacancy a death emits is *"**event-driven, not polled**"*; dormant grievance rows are *"**not an instance** … what fires is the person's valuation, not a calendar"*; vacancy-by-absence is *"**not shipped** … an instance *of this enlargement*, which is not evidence for it."*
**Consequence SUP states against itself:** *"So the convening condition stands on its **N-line and its design argument alone**, in the dock, with no recurrence argument behind it."* (SUP:751-753). SHAPE's headline argument — *"§2.2 should be read as naming a fourth instance of a shipped pattern, **not as adding a class** — which is a materially stronger claim"* (SHAPE:346-347) — is therefore **inverted**, not narrowed.

---

### G-3 · PRACTICE RANK and the realistic POOL RANGE — 0–5/1–12 against 0–7/1–14

| draft | version | citation |
|---|---|---|
| **S02** | `A practice is (name, **rank 0–5**, provenance, idiom)`; the pool line sums `practice[…].rank 0..5 (absent → 0, unpracticed)`; the verb ladder hangs on **rank ≥ 3** and **rank ≥ 5** | S02:153, S02:198, S02:204-206 |
| **S10** | *"**Practice ranges 0–7**, where 0 is 'never trained' … **Realistic Pool therefore runs 1–14.**"* All of S10's probability tables, the opposed-contest table and the *"gap of roughly 6 (on this design's **1–14** scale)"* claim are built on it | S10:33, S10:37-45, S10:132 |
| **INT row 11** | recorded as a live collision, **unacted**: *"the practice-rank collision — `02:153` 0–5 vs `10:33` 0–7. Both verbatim … recorded, unacted; **load-bearing on any future floor repair**"* | INT:210, INT:419 |
| **SUP round 1** | ruled **0–7** — later self-indicted: *"An earlier version of this document ruled 0–7 here, **which inverted its own rule and orphaned the verb ladder**"* | SUP:284 |
| **SUP round 2 / D-10 (terminal)** | ruled **0–5**, pool **1–12**, under §3.4's conflict rule: *"rank is a **field of doc 02's tuple**, and doc 02 uses it structurally … Doc 10 asserts 0–7 in passing and reads the number only as a die count"* | SUP:284, SUP:504, SUP:2006 |

⚠ **Unreconciled arithmetic residue.** SUP keeps S10's probability tables and the *"past a pool gap of about 6"* claim (SUP:566-567) while re-ranging the pool from 1–14 to 1–12; SUP:554 also carries *"doc 10 computes 0.078% at Pool 14"* — **a pool value outside the range SUP itself just ruled.** SUP states no re-derivation.

---

### G-4 · How a PETITION EXPIRES — "the world moving on" vs a person's motion vs never

| draft | version | citation |
|---|---|---|
| **SHAPE §9.3** | *"A petition lapses when world churn supersedes it — the famine ended, the seat was filled by other means, the war started, the proposition it addressed is no longer live. **Nobody decides this. It is the world moving on.**"* Filed as *"lapse's sibling — not the date passing, but the subject passing"* | SHAPE:551-556 |
| **SHAPE §11.4** | reframed: *"supersession is RELOCATION, not decay … **the subject does not vanish, it MOVES**"* | SHAPE:737-743 |
| **SHAPE §14.4** | further qualified: *"**whether a given petition is moot is a judgment**, and it is a judgment that conveniences somebody … *Expiry is material; its application is arguable.*"* | SHAPE:969-974 |
| **SUP §8.5 (terminal)** | **TWO named endings plus a third case.** (1) **LAPSE** — a date; *"the one licensed decider-free resolution in the whole design"*. (2) **SUPERSESSION** — *"moved and decided at a venue … an ordinary motion on the stasis ladder, pleaded from claims the mover actually holds"* — **not decider-free**. (3) *"**AT A ROOTLESS VACANT OFFICE, IT NEVER ENDS.**"* | SUP:1008-1023 |
| **SUP §13.2** | and the exception list is narrowed to match: *"**Supersession is NOT licensed by this row**, because §8.5 made it a motion by a named person at a venue."* | SUP:1648-1649 |

**SUP also rules a contradiction SHAPE carried internally:** *"#342's shape said in one section that a seat *filled by other means* supersedes a conferral petition, and in another that **no petition cancels another** … **Both cannot stand. The second wins.**"* (SUP:1025-1029). And the generalisation itself is corrected: *"⚠ The rule is about CANCELLATION BY A STATE OF THE WORLD, not about endings generally (C-21). **Lapse is precisely an ending with no person in it, and it stays.**"* (SUP:1031-1033).

---

### G-5 · The OWNERSHIP TABLE — four rows, three fields, or five rows with matter

| draft | version | citation |
|---|---|---|
| **S11 §3** | **FOUR rows** — Person · Container · Faction · Nobody. Container holds *"its stake, its judging set, its standing dates. **Nothing else.**"* | S11:94-99 |
| **S01 §6** | the same rule in the spine: *"Containers hold stakes, judging sets and dates. **Persons hold everything else.**"* | S01:490-491 |
| **SHAPE §3.2** | **THREE fields** (`stake`, `judging_set`, `dates`) plus `watch` **on the StandingDate** — *"`watch` is the only addition to #342's ownership table — which the table already admits, because a standing date is one of the three things a container holds and a watch is a property of a date, not a fourth kind of container state."* | SHAPE:144-159 |
| **INT (AR-1)** | widen the container row to **"primary physical state at a place"**, and *"**in both `11:97` and `01:490-491`**"* — *"Amending only `11` §3 would leave the spine refusing what the adjudication permits."* Evidence *"narrowed to two objects: `stores(h)` (`04:31`) and `pointer` (`04:34`)"*; `base(H_mine)` and `transport_cost` **fall**. The `Nobody` row *"must stay **exactly** as written"* | INT:225, INT:410 |
| **SUP §4.2 (terminal)** | **FIVE rows** — Person · Container · **Office** · Faction · Nobody. Container row amended to hold **matter and dates**: *"a hearth's `stores`, a site's `condition`, and the transmission pointer"*. General line: *"**A container may hold MATTER and DATES. It may never hold a SOCIAL AGGREGATE** … **The line is provenance, not location.**"* | SUP:334-340, SUP:355-360 |

**SUP records both amendments as amendments, and self-indicts round 1:** *"An earlier version of this document added the Office row and **did not re-run the same check on its own enlargement 3**, leaving `condition(site)` as container state the table forbade — and leaving `stores` and the pointer unowned in the same table that was quoting them (C-13)."* (SUP:362-364). **Note the widening's wording differs between INT and SUP:** INT widens to *"primary physical state at a place"*; SUP widens to *"MATTER"* with a provenance test. Both are on the record.

---

### G-6 · The WORLD-SUBSTRATE object — a stored scalar entering obstacles, vs option removal

| draft | version | citation |
|---|---|---|
| **ARC §2** | the hole: *"**There is no world-substrate quantity.** No Mending Stability, no Gap object, no Rupture condition"*; *"**This settles it as an omission, not a refusal.**"*; *"in this design the world is not dying. It is only being misunderstood."* | ARC:31-50 |
| **INT (I-A-1)** | **`thread_condition(n)`** — *"one place-scoped **primary physical scalar**, written only by `resolve` in P5 on an act declaring `touches:{(n, alter)}`, **read as an obstacle term** and by `Thread-Read(place)`, published as a band with no trigger point."* **The only surviving EXTENDS in either lane.** Cost: *"one stored field on places that have one; **plus a new term in `resistance_pool` for every Thread act at every site**"*. Status **CONDITIONAL** | INT:194, INT:224, INT:409 |
| **P3R §3** | the same object indicted against the anti-leverage row: *"`thread_condition(n)` is **a flat amount and a modifier** — wrong side of both … One person's `alter` act moves a place-scoped scalar that then enters **every subsequent actor's `resistance_pool` at that site** — a person-scale act with a container-scale effect **by neither licensed route**."* **RULING: not a violation, an unexamined row** | P3R:87-111 |
| **SHAPE §2.4** | **the inversion**: *"Invert it. Damage to a commons REMOVES AN OPTION; it does not add difficulty."* *"And it fixes leverage by construction."* | SHAPE:105, SHAPE:115 |
| **SHAPE §6.3** | three requirements added: a **SIZING RULE**, **CROSS-RUNG SEMANTICS**, **BAND-QUANTIZED EXPOSURE** — *"Point 3 is the one I would have shipped broken."* | SHAPE:349-374 |
| **SUP §10 (terminal)** | `condition(site) ∈ [0,1]` as **matter held by the container**, with all three requirements built out (`Δcondition` sizing, draw-weighted-mean aggregation, band gating, band-representative obstacle). *"damage **never enters a roll as a term**. Where a site's condition must reach an obstacle, it enters as a band representative, **which is a substitution of the pool source, not an addend**"* | SUP:1216, SUP:1235-1264, SUP:1743 |

**The two designs are opposite in kind, and SUP does not claim to have implemented INT's:** INT's object *adds a term to `resistance_pool`*; SUP's *removes a verb and never touches a roll*. SUP's row-11 clearance covers only the `alter` limb; **the `exclude` limb is explicitly NOT CLEARED** and demoted to §15.17 (SUP:1744, SUP:1839-1844). P3R's `:219` question is therefore answered for one limb and left open for the other.

---

### G-7 · "THE FLOOR" (D-1) — a headline finding, then struck, then a positive result

| draft | version | citation |
|---|---|---|
| **COV / gap report** | *"Ordinary capability is an empty verb set, not a smaller pool — verbs gate on a practice at rank 3+, so a person holding none gets no acts"*; `mark_salience` = 1.0 makes an unmarked person *"**inaudible in both directions**"* | INT:89-92 (quoting `09_GAP_REPORT.md:73-79`) |
| **F01** | treats it as real and ships **three edits** (delete the rank-gated verb clause; replace `mark_salience` with `act_salience`; apply A-6's firsthand floor). *"If a reader finishes this and cannot see what was removed, I have failed the brief."* | F01:8-13, F01:137-271 |
| **INT §1.1** | still asserts it — *"In play, that is not a balance note. **It is the absence of a story class.**"* — but flags *"⚠ The diagnosis survived; the repair did not … **the floor is currently a stated defect with no surviving fix in this exercise**"* | INT:88-109 |
| **P3R §0 (strike)** | **"D-1 — 'the floor' — is STRUCK. I verified it myself, three ways, and the antagonist is right."** Four refutations, verbatim: *"an untrained attempt is always legal … **it is just a small pool**"* (`10:33`); *"At `rank ≥ 3` a practice **adds** verbs … **adds to a list, does not constitute it**"* (`02:204`); *"**1.0 is the identity element of a product**, not a floor and not a cutoff"* (`04:415-424`); and *"the suite **already contains that worked season**"* — Torvald Aske, no post, *"**shortfall 0.47, IDENTICAL to Duke Vaynard's**"* (`05:52-62`). **What survives:** a **3→5 advancement gap** and a **~2× marked/unmarked publicity gradient** which `04:425` *"declares deliberately"* | P3R:10-34 |
| **SUP §17.1 (terminal)** | *"**The single largest finding of the testing exercise was a false one** — that a postless person had no verbs — **and its collapse is a positive result.**"* And §2 restates the low end as correct: *"An untrained attempt is legal and is just a small pool; practice rank *adds verbs*; a postless fisher's shortfall arithmetic is identical to a Duke's. **The design's low end is right and this document does not touch it.**"* | SUP:1887-1889, SUP:196-200 |

**Downstream consequences P3R records:** *"**§1.4's entry/exit framing is DROPPED, not narrowed.** With no entry term there is no symmetry"* (P3R:40); and *"Also struck: §0.1's 'body (b) is DOUBLY BLIND to the floor.' … **Body (b) was not blind to it; it read it and inherited it.** *Blind* and *contaminated* are different states"* (P3R:58-63). **All three of F01's edits are therefore built on a struck premise, and none is carried into SUP.**

---

### G-8 · THE ACT ECONOMY (D-2) — ruled by the fixes, reopened by the terminal document

| draft | version | citation |
|---|---|---|
| **#342** | contradiction shipped: *"Every person and every cohort commits **exactly one act per season**"* (`09:33`) against *"A worked season — Vaynard, **one turn, ten acts**"* (`14:562`) | F02:10-14; SUP:632-635 |
| **F02** | **RULED — Reading C.** *"One act per person per season stands, universal and unscaled — and the act count in an office-holder's season is not his allowance, **it is his reach**."* Discriminated by measurement: *"three readings, three distinct predictions, and **one of them is what six lanes measured without looking for it**"* — C matches *"at 100% within its class"*. Adds `acts_in_an_office_holder's_season = 1 + |{m ∈ establishment(o) : …}|` and prices `dispatch` at one act each side | F02:21-24, F02:88-90, F02:141-174 |
| **ARC §7** | independently agreed: *"**The act economy: keep one act per person.** … arc 19's entire dilemma exists only under one-act … **Two routes, same answer.**"* | ARC:161-164 |
| **INT** | **not ruled** — carried as a REVEALS with *"**no resolution survives in either lane**; must first reconcile `14:91-92`'s `seat_items`"*, and *"Neither lane's resolution survived … and none should be improvised."* | INT:420, INT:307, INT:521-523 |
| **SUP §6.1 (terminal)** | **REOPENED and escalated.** *"⚠ **D-2, THE ACT ECONOMY, IS OPEN AND IS THE LARGEST OPEN RULING IN THE DESIGN.**"* *"whether a Duke's season is one pick among six shapes or a ten-act sweep is the difference between **a personnel game and a decree game** at every rung above Settlement"* — carried to §16 as a live choice, with the **D-16 cohort exploit** attached: *"individuate your own cohort and get eleven acts instead of one … Any answer must price that or forbid it"* | SUP:632-639, SUP:1866 |

**Also: SUP corrects the enumeration itself.** *"a Duke taking **seven** verbs in one turn under a header claiming **ten** — wrong under every reading, including its own"* (SUP:634); INT verifies *"three times, and **worse than either lane reported**"* (INT:211).

---

### G-9 · `seat_items` — whose quantity is it, and how many quantities exist

| draft | version | citation |
|---|---|---|
| **#342 `14:91-92`** | *"An office's standing dates **consume the holder's own hours** … Holding two offices does not double a day"* — a **holder** property, and *"already a fourth quantity"* against `14 §1`'s *"three quantities and nothing else"* | INT:304-306; SUP:635-636 |
| **#342 `05:176`** | a carried petition **claims one of the container's standing-date capacity slots** | SUP:396, SUP:875 |
| **F02 §7 (S1)** | **RULED — one owner:** *"`seat_items` has two owners … **Settled: it is the container's.** The standing date belongs to the container and hears a finite number of items; **the holder's own scarcity is his one act**. `14 §1.3`'s conclusion — *'holding two offices does not double a day'* — survives, for a better reason … **The duplicate mechanism goes.**"* | F02:293-297 |
| **INT** | **not settled** — flags it as a precondition on the `14 §8` rewrite: *"it must **first** reconcile `14:91-92`'s `seat_items` with `14 §1`'s 'three quantities and nothing else', because `seat_items` is **already a fourth quantity**"* | INT:304-307, INT:521-523 |
| **SUP round 1** | re-denominated `carry` to `seat_items` **alone** — self-indicted: *"which silently overrode `05:176` — and did so **against §3.4's own conflict rule**"* | SUP:401-403 |
| **SUP §4.3 (terminal)** | **TWO quantities, both shipped, neither overruled.** `capacity(date)` owned by *"the **container or office** that holds the date"*; `seat_items(office)` owned by *"the **office**, and it is spent by its **holder**"*. **`carry` spends one of each.** *"**There is no third quantity, and neither of these two was a ruling.**"* | SUP:394-403, SUP:875, SUP:2001 |

**Direct, unreconciled conflict:** F02 abolishes the holder-side quantity ("the duplicate mechanism goes"); SUP restores it as one of exactly two, and makes `seat_items(office)` **the cap on live convening conditions** (SUP:774-776). Both are on the record; SUP does not cite F02.

---

### G-10 · COHERENCE BANDS — two incompatible shipped tables, plus a third use of the names

| draft | band edges | effects | citation |
|---|---|---|---|
| **S02 §5.2** | **10–8 / 7–5 / 4–3 / 2–1 / 0** | **"No band applies a dice penalty."** Whole: none · Dissonant: presented marks read at **−1 confidence** · Fragmented: at most **2** primary Convictions, the third's weight decays **1/season**, one stance row/season loses provenance · Fractured: tellings at **halved** confidence, **may not `carry` a petition** · Severed: *"you stop individuating … cannot originate petitions, cannot hold office. **A person has become an object**"* | S02:438-449 |
| **S10 §8.3** | **10 / 9–7 / 6–4 / 3–1 / 0** | **dice penalties on Thread rolls.** Whole: none · Dissonant: **−1 die** · Fragmented: **−2 dice**, some Thread ops closed · Fractured: **−3 dice, Composure halved** · Severed: **Thread Pool locked to zero** | S10:199 |
| **SUP §3.3** | the band **names** reused as a **view-budget penalty ladder**: `K = 7 + Focus + 2 per Knot consulted − Coherence penalty (**Dissonant 1 … Severed 5**)` | SUP:253 |

**Neither the edges nor the effects agree**, and no document in the suite reconciles them. `Coherence 7` is *Dissonant* under S02 and *Dissonant* under S10, but `Coherence 8` is *Whole* under S02 and *Dissonant* under S10; `Coherence 4` is *Fragmented* under both but with a structural effect in one and −2 dice in the other. **SUP does not rule this collision** — it is not among §3.4's four, and §15.11 lists only `K`, `exposure`, the practice range and the Thread term's placement (SUP:1813-1819).
**Related open item SUP does carry:** *"**The Coherence-0 ontology.** Two incompatible readings ship — loss of capacity, versus *a person has become an object*. Three arcs and two named absences turn on it"* (SUP:1871) — which is the §5.2 Severed row against the §8.3 one, escalated as a live choice rather than as a band-table collision.

---

### G-11 · THE CLAIM TUPLE — six fields or seven, and three sources or four

| draft | version | citation |
|---|---|---|
| **S01 §3.1** | `(subject, predicate, value, when, source, confidence)` — **six fields, no `visibility`** | S01:228 |
| **S01 §3.3** | sources: `firsthand(event)` · `told_by(person, their_claim)` · `inferred(claims…)` — **three**. *"There is no null source and no untraceable claim."* Rumour handled by *"a single synthetic root shared by **every** retelling"* | S01:273-277 |
| **S02 §4.2** | introduces a **fourth** source in passing: `firsthand_via_knot`, which *"corroborates independently of any telling — **but does not mint a new root: it reuses the originating event's id**"* | S02:362-364 |
| **SUP §3.1 (terminal)** | `Claim = (subject, predicate, value, when, source, confidence, **visibility**)` — **seven fields** | SUP:221 |
| **SUP §3.2** | sources: `firsthand(event_id)` · `told_by(person, handle)` · `inferred(claim_id…)` · `firsthand_via_knot(event_id)` — **four**. Also `told_by`'s second argument changes from *their_claim* to **`handle`** | SUP:243-246 |

⚠ **`visibility` is added to the primitive with no derivation, no N-line and no cross-reference anywhere in SUP.** It appears in the tuple at SUP:221 and is never read by any function, formula or rule in the document. The suite's own synthetic-root device for rumours (S01:275-277) is likewise **absent from SUP**, which keeps only the Knot-reuse case (SUP:245-246).

---

### G-12 · The `resolve` SIGNATURE — singular or plural

| draft | version | citation |
|---|---|---|
| **S01 §3** | `resolve(act, world) -> event` — **singular** | S01:214 |
| **S11 §2** | `resolve : (Act, World) -> [Event]` — **singular act, list of events** | S11:58 |
| **`09:819-821`** | proposing **plural** | SUP:160 |
| **SHAPE §2.1** | `resolve(acts, world) → events` — **plural** | SHAPE:38 |
| **SUP §1.4 (terminal)** | `resolve : (Acts, World) -> [Event]` — plural, **and marked as a ruling**: *"⚠ **Plurality note.** #342 ships **three spellings** of these signatures … **This document uses the plural** … because one season's acts are resolved together and conflict between them is a first-class case (§6.3). **That is a ruling, not a transcription.**"* | SUP:138-140, SUP:159-162 |

---

### G-13 · CONFERRAL ROOTING — adjudicated, then ruled, then the ruling withdrawn

| draft | version | citation |
|---|---|---|
| **MACH** | *"⚠ **THE CONFERRAL DILEMMA — reported, not resolved.** … **The suite asserts both and resolves neither.** … Two defensible answers, materially different games."* | MACH (View 4, conferral dilemma) |
| **ARC §3** | **"Adjudication: office-rooted, on the evidence."** *"Lane 2 found **four more**, each independent, from fiction written years earlier: every succession or coup arc in its range needs office-rooted conferral, and none needs person-rooted."* *"Five independent fictional demands plus the warrant is as much as this question is going to get short of Jordan ruling it."* | ARC:54-66 |
| **SUP round 1 (C-18)** | **RULED office-rooted** in a new §4.5, *"with the argument that B-11 is not violated because a named person still performs `confer` by remit; removed from §16"* | SUP:1975 |
| **SUP round 2 / D-7 (terminal)** | **RULING WITHDRAWN.** *"`CLAUDE.md` §0's fifth test licenses taking an obvious architectural answer **only where tests 1–4 are silent**, and here test 3 is not: **three surfaces say explicitly that this is not an audit's call**"* — `00_INDEX.md:105-109` (*"Two defensible answers, materially different games. **Not an audit's call.**"*), review (a)'s consequence table, and the fact base marking the sweep **incomplete**. *"**It returns to §16, with the analysis intact so nothing is lost.**"* The office-rooted case survives **as a recommendation only** | SUP:452-462, SUP:2003, SUP:1911 |

**Both dispositions are recorded in SUP's own change log — "the second corrects the first" (SUP:485-486).** ARC's "adjudication" and SUP's live choice therefore stand side by side; SUP does not cite ARC.

---

### G-14 · THE CHURCH CONFERRAL CYCLE / S19 — dissolved, retracted, ruled intended, then left open

| draft | version | citation |
|---|---|---|
| **SHAPE §7.1** | *"⚠ **THE WATCH DISSOLVES S19** — and S19 was blocking the petition retyping."* *"the deadlock … **is not a soft-lock and never was; it was a missing clock**"* | SHAPE:390-404 |
| **SHAPE §9.2** | **retracted in the same file**: *"**§7.1 is retracted.** The watch does not need to *dissolve* S19, and it should not."* *"S19 … is therefore **not a bug to fix**. … breaking it is political work for characters … **stories, not a mechanism**"* | SHAPE:526-544 |
| **ARC §3.1** | *"**Adjudication: rule the cycle intended.** Treat an undefined sovereign fraction over Church offices as a first-class political condition rather than an error to repair. **My defect filing was wrong.**"* | ARC:68-77 |
| **INT §3.1** | composed as a **prediction**, not a ruling: *"matters whose respondent is an **unpetitionable cluster** *and* whose resolution **no convener wants**. … **The Church cases sit exactly at that intersection.**"* *"This is a target, not an instrument."* | INT:323-328 |
| **SUP §8.5 / §8.6 / §16 (terminal)** | **NOT REPAIRED and NOT RULED.** *"Where an office is at the root of its own cluster and its conferral basis names neither, there is no date, so the petition cannot lapse and there is no venue at which to move it moot. **It sits, indefinitely. That is S19**"*. Carried to §16: *"**Content** … **A defect** … Review (a) states plainly that **nobody has ruled which**, and this document does not rule it either"* | SUP:1017-1023, SUP:1831-1838, SUP:1868 |

**SUP records the retraction of SHAPE's dissolution claim explicitly:** *"the watch dissolves the cluster-vacancy deadlock → **retracted.** The deadlock is content, not a bug. A stalled Church is the design working."* (SUP:1914).

---

### G-15 · THE CONVENER'S COST — "spends nothing" vs one act plus a deposit

| draft | version | citation |
|---|---|---|
| **#342 `14 §5`** | *"the convener holds the cheapest real power in the game … a convener who puts three items ahead of yours **has spent nothing** and killed your petition"* | MACH (View 4); SUP:1584 |
| **#342 `05 §3.1`** | `compose_agenda` costs *"**one of v's own acts for the season**"* and deposits regard over the backers of every petition admitted or omitted | SUP:948, SUP:1584-1585 |
| **F02** | flags the consequence and declines to resolve: *"Charging a convener his whole season to rank a docket is right under C … The gap report's own convergence list says *'the convener holds the cheapest real power in the game'*, found by five lanes. Under C **it stops being cheap.** That may be a correction, and **it may erase a finding five lanes independently thought was true; somebody should decide which.**"* | F02:381-387 |
| **INT §6** | carried as an **unresolved live choice**, with the supporting convergence struck: *"**Two #342 documents disagree independently of any proposal here.** … ⚠ **The five-lane convergence … is struck (S-3, verbatim suite text). Neither option may draw support from it.**"* | INT:525-530 |
| **SUP §12.4 (terminal)** | **RULED for doc 05** on the conflict rule: *"⚠ `14 §5`'s gloss says he *'has spent nothing'*; doc 05 says he spent an act and takes a deposit. **This document rules for doc 05** … so the correct statement is: *influence measured in the volume of things filtered, held by a person with no binding power at all, **at the price of one act a season and a grievance he cannot see coming**.*"* | SUP:1582-1588 |

---

### G-16 · THE BURIAL / DOMINANCE REPAIR — a mechanism invented in one round and deleted in the next

| draft | version | citation |
|---|---|---|
| **SHAPE §2.2** | the original claim: *"the convener must convene it **or visibly refuse. A refusal is an act, and an act is witnessed.**"* — *"'Nobody wants this resolved' stops being a dead end and becomes **visible obstruction**"* | SHAPE:73-77 |
| **SUP round 1** | accepted a gating-audit finding of a dominant option at the convener's seat and **engineered a repair**: lapse and supersession would emit witnessable events, and refusal would be terminal where burial was not | SUP:964-967 |
| **SUP round 2 / C-1, C-2 (terminal)** | **THE PREMISE IS FALSE AND THE REPAIR IS DELETED.** *"**Every part of that is wrong.**"* Three refutations: (i) *"**The premise is false on disk.** Burial is not silence; it is `compose_agenda`, which costs an act and deposits on the omitter by name"* — the audit had generalised from `05:314-316`'s **lapse**; (ii) *"**The repair's own mechanism does not hold either** … **`08:147` gives F2 the severity `descend`, which concedes a rung and closes nothing**, and **`08:150` defeats F5 with any new `support[]`**"*; (iii) *"**the recurrence cost fell on the wrong person.** Re-filing costs the *petitioner* an act"* | SUP:964-983, SUP:1544-1548, SUP:1908, SUP:1958-1959 |
| **SUP §8.4, restated** | what survives: *"**THE ONE ASYMMETRY THAT SURVIVES**… Omitting is not weakly dominant and never was — it loses on **two** regard limbs at once … **So burial is not free and never was; it is merely SAFE.**"* And a round-2 correction on top: `regard_gain` had been omitted from the table, *"so as printed it argues omission weakly dominates — the opposite of the section's conclusion"* (D-3) | SUP:985-1000, SUP:1999 |

**SUP's own summary of the round:** *"the largest single change is a **deletion** … **Round 1's best work was reading `05:202-224` and taking the mechanism out again.**"* (SUP:1983-1986).

---

### G-17 · `exposure` — five senses across the suite, and what each draft does about it

| draft | version | citation |
|---|---|---|
| **INT §6** | enumerates **five** distinct definitions: (1) a need term (`01:174`, `02:490-492`); (2) the price of Passing, *explicitly not a counter* (`02:62`, `02:78-81`, though `02:741` lists it as a carrier); (3) a **stored, mutated** hidden counter per (actor, operation) (`03:574-579`, `:586`, `:622`, applied `:914`); (4) a **derived, never-stored** sum over an alignment edge (`07:149-157`); (5) contagion exposure (`13:215`). *"**Senses 3 and 4 are the same concept implemented incompatibly**, and `07:556` refuses by name — *'a stored exposure counter'* — the object `03` §7 defines and mutates."* Consequence: *"**I-4 may not ship as a rename of one sense alone**"* | INT:510-519 |
| **F03 §3.1** | **unifies two of them by design**: *"Two things wear the name **exposure** … **They are the same shape**: a hazard, with a believed probability and a believed cost. Treating them as one term is what makes this a fix rather than an addition."* Also indicts `07 §1.3` as *"**A-2's banned object in a third disguise**"* because it sums over *"every person `q`… including persons the subject has never met"* | F03:148-162 |
| **SUP §3.4 (terminal)** | **refuses to rule and scopes by fiat**: *"⚠ **`exposure` is NOT in that table, because the rule does not reach it.** Five senses of that word name **five different objects**, each owned by its own document, so *'the owning document wins'* selects nothing … **this document uses `exposure` in one sense only, the pre-roll odds preview of §5.4**, and it uses no stored-counter sense anywhere. **That is a scoping decision by fiat and is named as one.**"* Round-1 had listed it as a fourth application of the rule; D-10 removed it | SUP:288-292, SUP:2006 |

---

### G-18 · WHAT THE PRE-ROLL PREVIEW MAY PUBLISH — #342's composed scalar vs SUP's four-row partition

| draft | version | citation |
|---|---|---|
| **S10 §4.2** | publishes *"both pool sizes, the obstacle interpretation, nothing else"*, as a stated policy: *"**The honest response is not to hide the mismatch behind a menu that pretends to matter — it is to publish it.**"* | S10:132 |
| **S10 §2.2 / INT conflict 2** | and the composed institutional obstacle is computed from *"the **individual** stances of the sitting masters"* — INT flags the seam: *"**If any exposure-consuming act's obstacle ever reads `exposure_true`, declaration leaks it** … `10` §4.2 is therefore **the shared compliance frontier of the combined set**: load-bearing on both lanes, examined by neither. **Flagged, not resolved.**"* | S10:80; INT:273-289 |
| **SHAPE §6.3** | one requirement: *"**BAND-QUANTIZED EXPOSURE.** … **The preview shows the band, never the scalar.**"* — *"a free, act-free, witness-free probe of hidden world state — and `choose` has no `World`, so **only the player can run it**"* | SHAPE:365-374 |
| **SUP round 1** | stated one rule and called it **self-enforcing** — self-indicted: *"It is not self-enforcing and it did not cover the cases that matter (C-5)"* | SUP:579-581 |
| **SUP §5.4 (terminal)** | a **four-row partition**: material & publicly inspectable → **the scalar**; resistance composed from private stances → **a BAND, never the scalar** (*"**This is a change to #342, which publishes the composed scalar**"*); hidden world state → **a band, and the scalar is never an operand of any roll** (*"enforced by construction"*); the opponent's pool in an opposed contest → **published, deliberately**, holding `10:132`'s policy. **Residual stated:** *"a resistance that is *neither* plainly material *nor* plainly stance-composed … has no ruled row, and this document does not invent one."* | SUP:583-605, SUP:1827-1830 |

**Consequence SUP applies to its own showcase:** the Masterpiece Examination candidate now previews *"**a band**, not the exact aggregate of what the masters privately think of his caste"* (SUP:597-600).

---

### G-19 · THE `condition` / `depletion` ACCUMULATOR — three forms in three passes

| draft | version | citation |
|---|---|---|
| **#342 `13 §5`** | two slow fuses (ore grade, siltation) written to run *"**every season**"* **in no phase at all**, and *"`depletion` appears only as a subtrahend with no definition anywhere"* (`13:166-169`, `13:178-181`). INT adds: *"**The precedent AR-2a leans on has never run**"* — P1 SETTLE contains neither fuse | SUP:1318-1319; INT:247-254 |
| **SUP round 1 (C-9 fix)** | *"The original subtracted a `[0,1]` delta from `base(H)`, a yield quantity, **with the sign inverted so that working a seam enriched it**"* — fixed the sign, kept `base(H)` constant, **and added a dimensionless multiplier centred on 1.0 to a quantity bounded in `[0,1]`** | SUP:1321-1324, SUP:1966 |
| **SUP round 2 / D-1 (terminal)** | *"**FATAL — the units error was relocated, not removed**"*. *"**FIX — the nature limb is DELETED, not repaired.**"* Final form: `condition(site) = clamp( condition + Σ this season's resolved condition deltas, 0, 1 )` — **P5 only, ACTS ONLY**; `season_factor` and `(3 + d10)/8.5` stay in `yield`, *"where #342 puts them"*, because `13:70-71` assigns permanence to `base(H)` and impermanence to `season_factor` | SUP:1327-1339, SUP:1997 |

**Two claims retracted along the way, both recorded:** *"the slow fuses run every season → **`condition` is a MULTIPLIER on yield and `base(H)` does not move**"* (SUP:1916); and *"there is no authored per-season constant in the fuses → **overclaim, withdrawn.** There is a non-act term and it is nature's"* (SUP:1917). **The narrowing this costs is §15.19:** *"A fuse that is act-only cannot model a site that decays with nobody touching it"* (SUP:1351-1354).

---

### G-20 · THE TRANSFER / PAYMENT ACT — `convey` vs `transfer`, and what it opens

| draft | version | citation |
|---|---|---|
| **F05 (E4)** | **`convey(from, to, goods, quantity)`** — derived by **dropping the creditor precondition** from `settle_in_full`: *"stores(from) −= q ; stores(to) += q, valued at 13 §4's price, witnessable, and depositing a claim naming both parties."* *"**`13 §9`'s refusal survives intact** … what moves is *goods at the season's price*, not a token."* | F05:396-414 |
| **SHAPE §7.3** | **"the transfer act"**, a fourth enlargement: *"a **new, clean act** — not a precondition dropped from `settle_in_full`, whose *defining property* is that the judging set never fires on it, and which the previous attempt broke by turning it into a deposit-carrying act. **A transfer is witnessed; a settlement is not. They are different acts and the last attempt collapsed them.**"* Claims it *"makes `12`'s existing coercion arithmetic **implementable**"* and that the holdingless have *"**no material verb at all**"* | SHAPE:443-466, SHAPE:489 |
| **SUP §11 (terminal)** | **`transfer(giver, receiver, amount)`**, amount in mouth-seasons, plus an **amended `draw(h)`** carrying two transfer terms. Two of SHAPE's claims come off: *"the transfer act makes the coercion arithmetic *implementable* → **expressible.** Re-denomination is unwritten work"*; and *"the transfer act gives the holdingless a material verb they did not have → **false, and a low-end repair.** `13:31-35` gives five channels. **It changes what can REACH a postless person, not what he can do.**"* | SUP:1425-1432, SUP:1444-1451, SUP:1921-1922 |

**And the N-line is renarrowed twice:** *"there is no act by which one person gives another anything → **overstated.** `requisition` surfaces another person's act as theirs to refuse … **The real hole is narrower and real: the unsolicited give, the wage, and the purchase**"* (SUP:1925). **F05's `convey` is not cited by SUP**, and the two acts differ in denomination (goods at the season's price vs. mouth-seasons) and in derivation (dropped precondition vs. new act).

---

### G-21 · `mark_salience` → `act_salience` — an edit whose premise was later struck

| draft | version | citation |
|---|---|---|
| **#342 `04 §4.1`** | `mark_salience = 1 + 0.2 × (number of the ACTOR'S MARKS that any community member holds a strong stance toward)`; `publicity = venue_factor × √(witness_count) × mark_salience` | F01:61, F01:196 |
| **F01 (EDIT 2)** | **replace it**: `act_salience(act) = 1 + 0.2 × |{ r ∈ referents(act) : ∃ p ∈ JS(act) with |stance(p, r).valence| ≥ 3 }|`, where `referents(act) = marks(actor) ∪ {proposition(act)} ∪ objects touched ∪ {place}` — *"the removal of a special case: publicity was reading **one referent kind out of four**, and attention was reading **none**"*. Plus a matching change to the attention floor `θ(p, act)` | F01:186-206 |
| **P3R §0** | the **premise struck**: *"`mark_salience` = 1.0 makes an unmarked person **inaudible in both directions**"* is refuted — *"**1.0 is the identity element of a product**, not a floor and not a cutoff. And the suite states the consequence in the opposite direction: *'Maret Uln's transgression reaches **twice as far** as an identical act by an unmarked neighbour'* — the unmarked act **reaches**, at half the distance"* | P3R:22 |
| **SUP** | **neither term appears.** SUP carries no publicity formula at all; marks are described only as *"ascribed, publicly-read attributes"* whose effect is that *"the same act by two persons produce different results"* | SUP:173, SUP:594 |

**F01's own dependency remains unresolved either way:** *"My worked numbers assume the parish is her community. Resolve it the other way … **she has no judging set for `act_salience` to quantify over at all.** This is the largest single dependency in this document"* (F01:432-438).

---

### G-22 · THE TWO MISSING NEED FORMULAS — supplied by F03, absent from SUP

| draft | version | citation |
|---|---|---|
| **S02 §6** | four need terms as **pseudocode**, on a `0..5` urgency scale | S02:471-493 |
| **F03** | *"the honest statement of D-3 is sharper than the report's: **half the motive engine emits urgencies with no propositions attached**, and `petition` … never enters a magnate's act menu"*. Supplies both formulas emitting **`(proposition, urgency)` pairs**, rules urgency into `[0,1]` with `0..5` retained *"as a display band … and is not the quantity"*, and adds **`unify` / `agree`** — *"**the only new machinery in this document, and it is a predicate, not an object**"* | F03:28-31, F03:46-47, F03:62-74, F03:86-95, F03:167-176 |
| **SUP §2 (terminal)** | four need terms, described only by **what each reads** (world / world / view / view). **No formula, no urgency range, no emitted proposition, no `unify`.** *"Needs are not a field; they are computed each tick, and they do not all read the same thing"* | SUP:183-194 |

**The range collision F03 rules is therefore live again in SUP:** F03 rules `[0,1]` with an unbounded tail for subsistence alone (F03:46); SUP writes *"need(p, subsistence) … **outweighs stance entirely once it exceeds 1.0**"* (SUP:1408), which is consistent with F03's tail but implies no scale for the other three. S02's `0..5` and `04 §1.2`'s `[0,1]` both remain in the tree.

---

### G-23 · THE CLOSURE-AXIS COUNT — three published figures, two with different membership

| draft | version | citation |
|---|---|---|
| **SHAPE §1** | *"**13 of 18 arcs** in one band close at a sitting and survive; **3** close at *a counter reaching a number with nobody deciding* and lose their ending."* | SHAPE:17 |
| **ARC §4** | *"**Thirteen arcs end at a scheduled sitting** … **Every one survives** … **Three arcs end at a counter reaching a number with nobody deciding.** All three lose their ending."* | ARC:85-88 |
| **INT §1.2** | *"**13** arcs ended at a *scheduled sitting* … **3** ended at *a counter* …; **1** ended on a faction's decision and is transformed; **1** has no closure by design."* | INT:113-116 |
| **SHAPE §6.1** | **corrected in the same file**: *"**Lane 1 states that 13-member set twice with different membership** — `01:32-33` includes Arc 3's first half and files Arc 16 separately; `01:672-675` includes 16 and excludes Arc 3's half. **Both sum to 13, which is why four downstream checks passed it.**"* And *"the label is false for at least three members"*. Corrected axis: *"**The cut is not *sitting vs counter*. It is *a person's decision — dated or not — vs a state trigger with no decider*. 12 stable members + 3 label-disputed + 2½ lost, lane-1 scope only.**"* | SHAPE:310-326 |
| **SUP §15.9 (terminal)** | *"**The closure-axis count is not citable in its original form.** … the honest figure is **12 stable + 3 label-disputed + 2½ lost, lane-1 scope only.**"* And in §17.3: *"*13 of 18 arcs close at a sitting; 3 at a counter* → **not citable.**"* | SUP:1804-1808, SUP:1927 |

---

### G-24 · VACANCY BY ABSENCE — a watch, an existing ruling applied, or a narrow new consequence

| draft | version | citation |
|---|---|---|
| **F05 §3.8** | **no new object** — apply an existing ruling: *"`14 §2.4` already rules the general case for offices: *'an office whose `exercise` is zero across its whole scope for two standing dates is vacant in the only sense that matters'*. **Apply the existing ruling to hearth seats, unchanged**, at the horizon table `04 §1.3` already publishes (1 season untitled, 2 titled, 4 consecrated)."* | F05:422-428 |
| **SHAPE §7.2** | **it is a watch** — *"**That is a watch, exactly.** A predicate over state the container can already read, which when true **schedules a vacancy date.** … `exercise` is identically zero at a hearth because a hearth has no remit; **presence is defined at every rung**"* — and it becomes the pattern's **fourth instance** | SHAPE:422-436 |
| **INT §3.2** | *"a **vacancy computed at the standing date** is a postcondition and passes"* the three tests — but *"**Two reasons this may not be taken as settled, and both are live** … the derivation is available at rungs that **have** standing dates and **unavailable at the hearth** … **Prince Torben and the widow's son are the same hole in body (a)'s framing and are not the same repair.**"* | INT:339-358 |
| **SUP §7.5 / §8.6 (terminal)** | the claim is **narrowed and its predecessor withdrawn**: *"⚠ *Not* that it has none: `14:254-256` ships **revocation in fact** … so absence already has a consequence at office rungs. **What the convening condition adds is narrower and is the part that matters:** `exercise` is **identically zero at a hearth**, while **presence is defined at every rung** … *(An earlier version of this bullet claimed there was no carrier at all, which `14:254-256` refutes. C-15.)*"* Falsifiers named and **not run** | SUP:813-820, SUP:1067-1077, SUP:1823-1824 |

---

### G-25 · THE VIEW BUDGET `K` — `7 + Focus` vs a flat 12, plus the cohort constant

| draft | version | citation |
|---|---|---|
| **#342 `03:325-329`** | `K = 7 + Focus` → range **8..14** | INT:426-427; SUP:283 |
| **#342 doc 09** | a **flat constant 12**, asserted four times at `09:63`, `:133`, `:151`, `:490`, *"with a separate `K = 3` per cohort **that doc 03 never mentions**"* | INT:426-428 |
| **INT** | carried as *"**Also carried, and not a change: the view budget K collision**"*, load-bearing on row 8's falsifier. ⚠ *"It is **not** 'reconfirmed at `09:689`' — that line says *'top-12'*"* | INT:426-429 |
| **MACH / F01** | both use **K = 12** in worked arithmetic (MACH's P3 row; F01's landing-claim ranking "against K = 12"); COV uses it too (*"Baralta's mine ranks **14th of K = 12**"*) | MACH:40; F01:264; COV:30 |
| **SUP §3.3 (terminal)** | **RULED `7 + Focus`**, and extended: `K = 7 + Focus + 2 per Knot consulted − Coherence penalty (Dissonant 1 … Severed 5)`. Ground: *"doc 03's declared subject is view assembly; **doc 09 asserts a constant it never derives**"*. `K = 3` per cohort **kept** | SUP:252-253, SUP:283, SUP:650 |

⚠ **The two new terms — `+2 per Knot consulted` and the Coherence penalty ladder — appear only in SUP and are not attributed to any #342 line.**

---

### G-26 · The FABRICATION COUNT — four, then five, then six, then "a floor"

| draft | version | citation |
|---|---|---|
| **`08` §5** | *"four producers, four objects"* | INT:557 |
| **`09_citation_ledger` §Z** | corrected authorship, but its own tally line reads *"FIVE … THREE of them mine"* — which INT says *"**does not survive its own reassignment**"* | INT:559-561 |
| **INT §7.1** | *"**The corrected line is: five objects, one producing role, one downstream repetition.**"* Attribution: *"all five author-attribute to one role — the orchestrator/adjudicator. One was re-asserted by lane (a). **Lane (b) authored none.**"* | INT:539-563 |
| **P3R §6** | *"**There is a sixth**, and it is finding 1 above: D-1's truncated `10:33`. Authored in the document whose §7 counts the instances. **So 'five' is a floor, not a count — as is 'six'.**"* | P3R:161-168 |

**The generalising finding is stable across all versions:** *"**The rate tracks LAYER, not producer count.**"* (INT:567; P3R:172).

---

### G-27 · "THE CODE SHAPE SURVIVES ALMOST ENTIRELY" — a result, then an artefact

| draft | version | citation |
|---|---|---|
| **INT §2.1** | *"two large exercises, four producer documents, an adversarial relay and a pessimistic reconciliation, and **the code shape survives both instruments almost entirely.** The pessimistic residue is *one stored field, plus one additive rule text* … Under P-5 … the whole reconciliation passes, and **the narrowness is the result**, not a disappointment about it."* Also *"Lane (b) contributes **exactly ONE `EXTENDS`**"* | INT:190-201 |
| **P3R §5** | **narrowed as an artefact**: *"The classification runs over a set already filtered by **P-5: *'a fix that adds a system has failed.'*** A rule that penalises additions, applied upstream, **guarantees** a low-EXTENDS survivor set downstream. Reporting that count as *a result about the code shape* — and writing *'the narrowness is the result'* — **treats the filter's output as the filter's discovery.**"* And *"**Also narrowed:** *'exactly ONE EXTENDS'* holds only by switching definitions mid-document … **Restate as: one new stored field, plus one new generation path admitted as authored.**"* | P3R:140-157 |

**What P3R lets stand as independent:** *"**lane (b)'s N-line survived a hostile sweep wider than its proposer's**, and **no lane-(a) survivor places state anywhere**"* (P3R:150-152).

---

### G-28 · NON-REDUNDANCY OF THE TWO INSTRUMENTS — a framing built on a struck finding

| draft | version | citation |
|---|---|---|
| **INT §1.4** | *"**Entry and exit.** Body (a)'s floor is a defect at the *entry* … Body (b)'s closure axis and closure limit are defects at the *exit* … **a person with no verbs never enters; a matter no convener wants never leaves.**"* And §0.1: *"**each body's best finding sits in the other's structurally blind region**"* | INT:154-159, INT:57-64 |
| **P3R §1** | **DROPPED, not narrowed**: *"With no entry term there is no symmetry. And the antagonist's second objection stands independently: the framing paired body (b)'s headline against a **non-headline** item of body (a), while body (a)'s actual headline — the blocked core — is itself an **exit** test. ***'Best finding'* was doing the selection, and the selection produced the symmetry.**"* Replacement: *"**both instruments found the same class of failure — the design is good at starting things and bad at ending them.** … **The design's problem is termination.**"* Non-redundancy survives *"on **weaker and different** evidence"* | P3R:40-56 |
| **P3R §2** | one of the three yields **struck as manufactured**: *"**§3.3 is MANUFACTURED — struck.** … `06` §E-1 is about a stored `exposure` counter and **says nothing about `10` §4.2** … **two sections of one document contradicting each other about the contents of one citation.** … The antagonist ran that check. **The document contains one, and it is §3.3.**"* The frontier itself *"survives as a **one-lane** finding"* | P3R:67-80 |

---

### G-29 · The COMMITMENT-DEGREE LICENCE COLUMN — shipped in two contradictory states, unruled everywhere

| draft | version | citation |
|---|---|---|
| **#342 `07 §1.2`** | ships the six-row degree table **as a gate** — degree 2 may be *"asked for material, shelter, carriage at low cost"*, degree 3 *"may be **requisitioned**"*, degree 4 *"for acts against their own container's interest"*, degree 5 *"no offer term enters the refusal check at all"* | MACH:147-152 |
| **#342 `16 §2.2`** | **cuts the column and keeps the degree**, *"on the ground that the obstacle formula already prices asks continuously and the two copies can disagree — **the table forbids requisitioning a sympathiser outright while the formula would clear one at high regard**"* | MACH:169-172 |
| **MACH** | *"⚠ **REPORTED, NOT RESOLVED** … What survives the audit's cut is exactly two discrete things: **degree 5's absent offer term, and the avowal gate.** Both documents are in the suite. A season that leans on a degree-2 refusal being *illegal* rather than *expensive* is standing on the contested half."* | MACH:169-175 |
| **F03** | uses the **weights only** (`w(d)` = 0 · 0.15 · 0.40 · 1.00 · 1.60 · 2.20), not the licence column | F03:97 |
| **SUP** | **the collision is not carried anywhere** — SUP names four surviving vocabulary collisions (`K`, `exposure`, the practice range, the Thread term's placement) and this is not among them | SUP:1813-1819 |

---

### G-30 · THE THREAD TERM'S PLACEMENT — inside the pool expression, or a second pool

| draft | version | citation |
|---|---|---|
| **S02 §2.3** | a conditional addend **inside** the pool expression: `contributed = attr[...] + practice[...].rank + thread_pool  (only if attempt.verb is thread-typed)` | S02:196-200 |
| **S10 §8.1** | *"This is **a second pool on the same person, drawn through the identical `roll` function** — not a second resolver. A Thread-act simply sources its dice from Thread Pool instead of Attribute+Practice"* | S10:192 |
| **SUP §3.4 (terminal)** | **RULED: a second pool through the same `roll`** — *"same ground; and the alternative puts a second addend inside `Pool`, **which §14 row 10 forbids in spirit**"* | SUP:285 |

---

**Delta total: 30 objects, with 97 distinct versions recorded across them.**

---

*End of abstract. No claim in this document is an evaluation. Where two sources disagree, both are recorded and neither is resolved.*
