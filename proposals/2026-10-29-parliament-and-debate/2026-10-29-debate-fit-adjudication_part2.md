# Part 1 verdicts — A (agenda), B (convening/procedure), D (judgment/voting), J (record/memory); L as constraint

## Status: **REFERENCE (2026-10-29).** Verdicts of fit; continues `2026-10-29-debate-fit-adjudication.md`, whose status, method and limits apply here. Judgments, not tasks.

Adjudicator: Opus, theme group 1. Tree read: `C:\Github\ttrpg-parliament` at `d90b6e8d`. Every entry in `part1.md` (A 42, B 97, D 76, J 23, L 32) was read. Judgments of fit only; nothing here proposes work.

## 0. The constraints that bound every verdict below (L, not verdicted)

| constraint | entries | effect on fit |
|---|---|---|
| provider returns a **margin, never a winner**; no write from inside | CD-058, OP-022 | winner-returning resolvers misfit |
| **one fold**; a failed precondition writes nothing | CD-059 | nothing decided by a clock or module |
| fold reads **only the actor's own ledger** (F8, ED-SC-0040 B) | CD-054, OP-100 | coded `reception`/`proofs` non-conforming |
| no branch on an arrangement id | CD-069, OP-090 | institutions differ only as data |
| only `disposes` of 13 arrangement keys is read | HP-045, CD-007/008/009 | other keys are paper (verified §6) |
| kernel not adopted, retirement ruled; parliament sim code deleted | CD-052, CD-066, PR-108, GV-092, GV-060, OP-021 | reference, not candidates |
| obstacle ceiling 2 | PR-022 | a hostile room cannot raise the obstacle |
| proceedings design is intent only; `sources/` is tier 3 | CD-053, CL-073, CL-045, HP-107 | research cannot carry a verdict alone |
| authority read off the exercised seat (`Act.via`) | GV-058 | how far it has landed is unverified (B-13) |
| Jordan's held calls (titles, binding, chair, dice after vote, depth) | CD-109 | touched, never decided |

Two cross-cutting engine facts recur and are stated once: **(i)** a computed `open_case`/`carry` names no arrangement (H-80), so every per-row rule — including CR-34's tally — has **realm reach 0** in computed play (CR-34's own header: "hash EQUAL; realm reach 0"); **(ii)** persons differ in nothing the roll or the vote reads: `argue` rolls `pool_default` 2 vs `obstacle_default` 2 (H-126), the voter's pursuit term is identical for every `commit` (proposal §5), and the chooser has no risk or horizon term (NL-033). Every "persons" line below is read against (ii).

---

## 1. A · Agenda and salience

### A1 · The docket as agenda: convene → Date → slot → open_case → bench asked — **ALREADY-HELD**
Entries: CD-019, CD-020, CD-023, CD-024, CD-068, HP-078, GV-056, PR-101, PR-019, PR-023, OP-054, CD-079 (limit).
- **NERS.** N holds top-down (a convener makes a room exist), bottom-up (a matter arrives only by an act), lateral (one convene is a standing court); vertical weakly (venue matched by place, an assumption). R-WORLD: zero-authored-act proceedings run end to end (CD-068), but only 4 of 72 determinations walk back to a fired date. R-COMPLETE: a matter on a rung fills no slot. S pauses correctly (nothing fires before *s+1*); one Date/claim path for every occasion. E last: one Date, one list, one Query — high ratio.
- **Story.** CODED: a lord convenes, a case opens on someone he heard of, a judge is asked because he heard the date fire; hearsay of a firing is not admitted (CD-024). **Persons:** who convenes and whom a judge heard differ; flattened at the roll (ii). **Fails:** inert — most determinations are Failure at pool 2 vs Ob 2. **Evidence:** CODED. Stale: PR-019's "exists:DocketItem returns UNKNOWN" predates PR-101.

### A2 · Petition and carry: the seatless route to the room — **ALREADY-HELD**
Entries: CD-021, CD-022, CL-099, HP-079, HP-080, OP-054, CL-044 (stale), OP-077.
- **NERS.** N holds bottom-up and is the only S-UP carrier in the group: a demand is a real Record, held by an accountable person, carried by an act (CD-021). Cut it and a person without a seat cannot reach a bench at all. R-WORLD: NPCs file petitions in computed play (28 in a four-season probe, OP-110). R-COMPLETE fails: the two ruled closers (withdraw, deny) do not exist, so a petition cannot be refused (CD-022, verified). E: reuses `Record`, `hold`, `carry`; no new carrier — high.
- **Story.** CODED: a grievance becomes a document someone holds and may never carry. **Persons:** a computed petition is addressed to the person it concerns (H-94), so it cannot yet rise to a superior. **Fails:** with no deny verb, ignoring a petition is free and emits nothing — silence dominates at the receiver's seat.
- **Evidence.** CODED. **Disagreements:** HP-079's "carry is a no-op" is stale (the effect is built, verified); HP-080's "closed by withdraw or deny" states the ruling, not the code (no such verbs, verified); CL-044 "no petition subsystem" is superseded by CL-099.

### A3 · Grievance from dropped petitions; rank-indexed petition register — **FITS-IF-ADAPTED**
Entries: OP-075, OP-045, GV-104, CL-039, HP-050, CL-018.
Adaptation: the drop or denial must be a **witnessed act or lapse** at the venue, and "register" must be read from the petitioner's standing with the addressee (a Query), not authored as a protocol table or a card deck.
- **NERS.** N holds bottom-up and in R-WORLD: without a cost to burying petitions, A2's receiver has a dominant silent option. OP-075's "the next petition assembles in one season instead of four" is a lower trigger with no threshold object (T-b-clean). E last: GV-104's escalation cards and CL-018's protocol table fail (authored inventory; a deck is a second occasion source beside claims — an S methodology defect).
- **Story.** NOTCODED: a mayor drops three hunger petitions, the drops are seen, the fourth comes faster and names him; ripples into I and K. **Persons:** grievance is per-ledger. **Fails:** inert without the witnessed drop, gamey with a meter. **Evidence:** PROPOSED/HISTORICAL; the dominance argument rests on the coded absence of closers, not research.

### A4 · Individual salience: attention tiers and reach — **ALREADY-HELD**
Entries: CD-025, CD-026, GV-066, (cross) NL-057.
- **NERS.** N holds top-down and bottom-up: a person answers his ambitions, his seats' purview, his strongly-felt deeds, then his need (verified, five tiers). **No aggregate agenda exists** — a room's agenda is only the docket — correct under the person-only constraint, not a gap. S: one key for every question. R-COMPLETE fails for bodies: a sitting question lands in tier 4, below every `need` (B-5). E: one sort key — high.
- **Story.** CODED: different ambitions attend to different matters in one room. **Persons:** the strongest differentiator in the group. **Fails:** a motion nobody attends to reads as the body ignoring the player. **Evidence:** CODED, opened.

### A5 · Where a motion comes from: antecedent occurrence, strain plus independent trigger — **FITS-IF-ADAPTED**
Entries: CD-098, OP-083, OP-067, PR-068, PR-070, OP-043, OP-027, OP-019.
Adaptation: keep the rule "no motion without a real claim on a real owner" (OP-083, upheld under attack) and the mood split (PR-068); the trigger is a claim of a different kind; the strain band only raises a Question (T-b), and "Ripe"/"freshness" enters no decay timer.
- **NERS.** N holds bottom-up (motions grow from the world) and diagonal (strain queries already exist: `vacancies`, `hunger`, `at_war`). OP-019's "let it ride" (no re-contest without changed circumstances) is carried for free by Proposition immutability: a re-tabling is a new Proposition with no commits. R-COMPLETE fails at one extreme: a matter about a **future** has no producer (PR-070, OP-043; P-24 open), so "what to do about the invasion" cannot be argued — the deliberative genre is cut off at its most dramatic use.
  E last: reuses existing strain queries and a data roster — high, if the strain band stays a swept value.
- **Story.** NOTCODED: a vacancy plus a bishop's utterance raises a motion to fill the seat. **Persons:** the trigger is someone's act. **Fails:** strain alone would feel like events firing. **Evidence:** PROPOSED/INTENT; "strain alone fizzles" is tier-3 research, and the attributability argument does not need it.

### A6 · Agenda control: convener's order, clerk's agenda, drafting right — **FITS-IF-ADAPTED**
Entries: OP-076, OP-078, HP-054, HP-062, HP-075, HP-056, HP-025, HP-096, CD-067, OP-080, GV-093, HP-086 (lockout), CL-097 (relatio taken).
Adaptation: agenda power is the holder of the case Record or petition choosing to carry, hold or let lapse — each a witnessed act; no chair "order of motions" key and no capacity veto that costs nothing.
- **NERS.** N holds laterally and from R-WORLD: "the clerk who reads every petition outranks the minister" (OP-078, HP-062 Ming drafting) is power without a power stat — exactly persons differing by position. Venice's Collegio setting the Senate's agenda (HP-025) is the same shape at realm scale. Fails as sourced: OP-076's "three items ahead of yours kills yours at no cost" is the silence-beats-refusal shape the NERS method rejects; HP-056's discessio order needs intra-season order the engine cannot record (B-6).
  E last: no new object if carried by hold/carry/lapse — high; a chair-order key would be overhead.
- **Story.** Parts CODED (hold, carry), the choice NOTCODED: a clerk sits on a petition against his patron. **Persons:** rewards horizon, which the chooser cannot read (ii). **Fails:** solvable if dropping is free, inert if every item is heard. **Evidence:** PROPOSED + RESEARCH; "cheapest real power" is unratified.

### A7 · Player-as-government policy sim (political capital, bloc approval meters) — **MISFIT**
Entries: HP-086, HP-091, HP-092, HP-089. The player governs a polity and blocs are stored approval scores — fails "only persons act" and adds a second currency (E). Its one portable idea, lockout after failure, is carried by A5's immutable Proposition. **Evidence:** GAME tier only.

---

## 2. B · Convening, venue, standing, procedure

### B1 · A proceeding is a data row (13 keys, 8 games, loader refuses strays) — **ALREADY-HELD** (shape); the keys are mostly paper
Entries: CD-001, CD-002, CD-004, CD-005, GV-052, GV-053, GV-054, HP-044, PR-093, PR-024, PR-001, PR-002, PR-003, PR-046, CD-069, OP-090, OP-071, OP-074, CL-038, OP-001.
- **NERS.** N holds laterally (a thirteenth game is a row, PR-046) and in E (no ProceedingKind enum; the old head's ~300 special-cased lines collapse, OP-090). But only `disposes` is read (verified): R-COMPLETE fails — open parliament and closed council admit the same people and behave identically except in what they dispose, and the two assemblies dispose a Record, which `determine` declines. S methodology holds (one loader, one reader). E as ratio: excellent shape, yet 12 of 13 keys buy nothing today.
- **Story.** CODED for trials (detain/ban); none for assemblies. **Persons:** neutral. **Fails:** the player reads "parliamentary_debate" and finds a two-seat royal bench. **Evidence:** CODED. Stale: PR-001's README "nothing exists in engine/season" (PR-093); PR-093's "remaining seven" header.

### B2 · Procedural keys that need intra-sitting order: speaking order by rank, interposition, latitude — **HELD-FOR-REASON**
Entries: CD-008, CD-079, PR-102, PR-057, PR-025, PR-013, CL-089, CL-032, HP-053, HP-055, CL-024, CL-036, CL-097 ("order by rank declared inert").
Prerequisite missing: an order **inside** a season. No round is stamped on any Event or Tenure (proposal §2, B-6) and the nested run is unbuilt. Rome's *sententiae* by rank (CL-032), the discretion gate (PR-013: the person matters most where the arrangement constrains him least) and Caraka triage are all functions of position in a sequence the engine cannot record. HP-055 states its own falsifier: equal turns make order noise — which is today's state. Latitude as a Query over `interposed` (PR-025) is the right form when it comes; it cannot be judged against a single roll. **Evidence:** INTENT + RESEARCH; Roman procedure is HISTORICAL tier.

### B3 · A council is one seat; members join by their own `oblige`; chair separate from ruler — **ALREADY-HELD**
Entries: CD-043, GV-061, CD-056, CD-097, CD-107, CL-033, HP-105, CL-097, CD-064, OP-104, GV-089, CD-046, GV-067, GV-068, CD-047, GV-047, GV-069, CD-048, GV-031, GV-029.
- **NERS.** N holds in all six directions, which is rare: top-down (the ruler convenes and executes), bottom-up (a duke is *eligible* by containment and a *member* only if he joins), lateral (estates — Church, commune, emerged creed — enter by the same admission), vertical (four rungs, same shape), diagonal (CR-36's two-seat clause holds with no special case), horizontal (leaving is `release`, a witnessed vow-break). Attack: "N seats would be simpler" — fails, `hold` is one-per-object (both verified, §6). R-WORLD: joining or abstaining is a political act with no player. S pauses correctly: the assembly never acts; the owner does. E last: zero new keys, acts or fields — the best ratio in the group.
- **Story.** Primitive CODED; **no parliament seat exists** (CD-047, GV-068: only a Chief Parliamentary Clerk). The realm's "Parliament" (H-90, GV-031) is ruled and unbuilt. **Persons:** membership is a decision — fits persons differing. **Fails:** the Lawspeaker chair (CL-033) fits only if the chair's declaration is bounded away from outcome; Jordan's call 3. **Evidence:** RATIFIED Layer 1 + CODED query.

### B4 · Attendance, summons, precedence as standing signal — **FITS-IF-ADAPTED**
Entries: CD-102, HP-008, HP-051, OP-077, CL-035, PR-014 (cross-J).
Adaptation: attendance is a costed `move` to the venue or compliance with a held writ; absence is the default and emits nothing unless a summons existed. The Carolingian assembly where "exclusion was a demotion" (HP-008) and the duke who leaves his duchy unguarded to vote are the same churn. Not reachable: the summons has no addressee and computed `give` does not form (B-9, H-229); unverified whether anyone off the realm rung hears a realm-venue `date.fired`. Ceremony-before-substance (HP-051) and the King barred from entering (OP-077) fit as admission predicates. **Persons:** risk and horizon decide who travels — the chooser cannot read either (ii). **Evidence:** PROPOSED + HISTORICAL.

### B5 · Nothing advances itself; a proceeding ends by lapse, term or exhaustion — **FITS-IF-ADAPTED**
Entries: PR-008, PR-058, PR-053, CD-099, CD-108, OP-110.
Adaptation: the lapse must **emit a witnessed event** (proposal step 9). No phase timer is Layer 1 (CD-059) and fits: "a hearing nobody attended" is a legitimate outcome. But today a below-quorum `determine` is a refusal retried every round forever and a Failure leaves the matter docketed (B-7): no motion ever ends. The stratum gap (convene *s*, press *s+1*, determine *s+2*, PR-053) is a feature — a season in which people flee, bribe or die. **Story:** NOTCODED for lapse. **Fails:** without lapse, a docket silts up. **Evidence:** INTENT + coded refusal behaviour.

### B6 · Layered and multi-college bodies: Venice's councils, Reichstag colleges, Roman comitia, Signoria rotation, consultative courts — **PARTIAL**
Entries: HP-025, HP-030, HP-070, HP-061, HP-011, HP-003, HP-014, HP-031, HP-032, HP-095, HP-096, HP-010.
Fits **at the realm rung only**, as several council seats whose resolutions a second seat must also hold (CR-36's two-seat clause; Venice's ducal co-signature HP-030 is that clause exactly; the Reichstag's three-college recess HP-011 is three resolutions one executor must hold). Below the realm the authored world has one titled post per rung, so multiple bodies are overhead (E). Rotation and two-month terms (HP-014) need `Tenure.term`, unbuilt. Han tingyi (HP-031) — counsel without binding — is already the T3a shape: a resolution the ruler may decline. **Evidence:** HISTORICAL only (ED-IN-0064 hooks unratified); the verdict rests on the coded two-seat clause, not the history.

---

## 3. D · Judgment and voting

### D1 · `determine`: one seated judge rolls against the party; bench = `judging_set`; quorum = bench size — **ALREADY-HELD** (single-decider games only)
Entries: CD-014, CD-015, CD-016, CD-017, CD-003, GV-055, OP-034, PR-095, PR-097, PR-007, PR-052, PR-035, PR-036, PR-037, CD-018, CD-075.
N holds for arbitration, trial and tribunal; jurisdiction follows presence (CD-016) — a fleeing accused is a story. For a body it fails: "a bench decides" is one member's roll and the others count only toward size (CD-075); `bench_quorum=1` cannot refuse (verified, `fixtures.py:943`). R-COMPLETE: at pool 2 vs Ob 2 most determinations fail and persons differ in nothing the roll reads (ii) — verdicts vary by seed, not by judge. **Stale:** HP-108 "contested determine blocked" and PR-052 "grade absent" predate SC-03b; PR-104's "L-6 determination→conviction severed" predates the judge's pursuits moving by consequence (CD-014).

### D2 · A vote is a count of live `commit`s, declared by a later act (ED-SC-0034, CR-34) — **ALREADY-HELD** (ratified; unbuilt; content-blind)
Entries: CD-049, CD-060, OP-101, PR-021, HP-108, OP-106, CD-006, CD-096, CD-099, CL-097.
The engine's tally is the best-shaped mechanism in the group. N, all directions: each member's vote is his own act; nobody's determination changes anybody else's; the threshold changes what can be chosen, not the outcome (ED-SC-0034, verified `editorial_ledger_sc_archive.jsonl:37`). Changing one's vote is `release`, a witnessed vow-break — horizon and conviction have a price. E: no field, no stored tally. **But:** (1) realm reach 0 (H-80; CR-34's own header, verified); (2) the voter cannot see what the motion says — a cession and a censure score alike (B-8), so the count is of loyalties, not of opinions on the subject; (3) a carried motion can still fail on the declarant's dice (B-10, Jordan's call 4). Under (2) R-WORLD fails: votes emerge but are not *about* anything. **Evidence:** RATIFIED ruling + plan; CODED absence (CD-018).

### D3 · Elections, nomination and the composition contest: who fills seats and who sits — **ALREADY-HELD**
Entries: CD-042, CD-057, CD-061, CD-062, GV-086, GV-087, OP-105, GV-094, GV-045, GV-080, HP-010, CL-069, HP-013, HP-015, HP-097.
Ratified: an election is `determine`, not `confer` (AX E.3, CD-057). The corpus's sharpest judgment finding — *who sits is a larger, prior contest than what is said* (CL-069, Rome's jury panels fought over for fifty years; the Medici packing the bags, HP-015) — needs no object: it is the existing confer/revoke/oblige/release economy. R-WORLD would be strong: the King dies at tick 0 in every seed and the throne stays empty (GV-094, OP-109); a contested succession at the throne's bench is the drama that should follow. Today nothing discriminates bases and no election route opens a hold (H-217). Golden Bull fixed electors (HP-010) fits as a seat roster, not a rule. **Evidence:** RATIFIED + plan; history corroborative only.

### D4 · Faction-stat parliaments: Mandate-weighted tallies, bloc ±1D, CI milestones, Integrity meter, vote-gated rank ladders, committees — **MISFIT**
Entries: GV-005, GV-007, GV-008, GV-015, GV-070, HP-081, OP-017, OP-099, HP-085, HP-093, GV-020, GV-021, GV-022, GV-023, GV-024, GV-025, GV-041, GV-100.
Factions cast votes; stored meters (Mandate, Readiness, Competence/Corruption, PI) are aggregates as fields; "only persons act" and "a faction never acts" both fail. The code is deleted (GV-060). What survives is carried elsewhere: rank by public vote (GV-020) is D3's elected conferral; the Seggio bloc (GV-041) is several persons' commits; GD-3's "emerging factions cast no parliamentary votes" (GV-100, canon) re-reads as *a creed's members are not yet admitted* (proposal §4). **Evidence:** ARCHIVED.

### D5 · Kernel win conditions and contest trackers: Persuasion Track, VoteAtClose, compromise zone, Face — **MISFIT**
Entries: CD-080, CD-081, CD-082, CD-083, CD-084, OP-004, OP-030, OP-055, OP-009, OP-011, OP-087.
Returns a side label, not a margin (C.5); reads a faculty; global RNG; Face is a contest-local stat that resets. The one idea worth keeping — the committee/compromise outcome binary wins lack — has no producer in the person model (log-rolling and scaled compromise refused, CL-097). The hidden "scar" portrait cue (OP-011) is a surface choice, out of mechanism scope. **Evidence:** CODED-but-not-adopted; ruled for retirement.

### D6 · Deliberation dynamics: the first defector, majority pressure, indeterminate members — **FITS-IF-ADAPTED**
Entries: CL-056, CL-057, CL-059, OP-030, HP-064 (bloc-building cost).
Adaptation: a member's `commit` reads the **visible commits of fellow members he has witnessed** (his own ledger, F8-conformant) — no influence rounds, no track. Today "every argue Candidate ties and a Gumbel draw breaks it" and nothing reads others' commits, so there is no snowball (CL-097). Reacting to the Past's indeterminates (CL-059) already exist: persons with no faction commit. Fits persons: the high-value target is one person at one moment. **Evidence:** RESEARCH (Devine meta-analysis, T1) — flagged tier-3; leniency asymmetry (CL-057) is contested and is a tuning value, not structure.

### D7 · Veto, intercessio, holdout and consensus: Sacred Veto, Stay, no-confidence, conclave, Lögrétta cascade — **FITS-IF-ADAPTED**
Entries: HP-057, HP-001, HP-004, HP-022, OP-096, CL-034, GV-009, GV-099, OP-016, GV-091.
Adaptation: a veto is a **seat-holder's witnessed act** that leaves the resolution held and unexecutable (no cooldown, no Mandate cost); unanimity is `quorum` = membership size. The ruler declining to execute already exists as T3a's executive form; a *peer* block does not. HP-057's "a free veto is used every time" is answered by witnessing, not a price list. Sacred Veto and Stay have no scheduled home (GV-091). **Evidence:** HISTORICAL/ARCHIVED; fit rests on the coded witness layer.

### D8 · Sortition and the lot: imborsazione, the doge's nine-stage election, election by lot — **MISFIT**
Entries: HP-064, HP-015, HP-028, OP-106 ("a seeded draw with no actor"), CL-034 (lot by quarter).
A lot is an outcome with no actor — the engine choosing a person's office — and a bench by lot has no basis in `oblige` (proposal refused it, CL-097). Venice's virtue (capture requires controlling every round) is real but its R-WORLD yield arrives through the vetting, which D3 already carries. **Evidence:** HISTORICAL; the misfit rests on the person-only constraint, not on history.

---

## 4. J · Record, memory and reputation

### J1 · Reception and proofs: the bench's regard for a speaker — **FITS-IF-ADAPTED**
Entries: PR-100, OP-050, OP-052, OP-053, OP-032, PR-104, CD-054, OP-100.
Adaptation: re-source from commits so the fold reads only the actor's own ledger (ED-SC-0040 option B, ratified). The idea fits every direction — a judge who saw your deed receives you differently — but as coded it reads other persons' ledgers (Layer 1 violation), enters only `speak`, which writes nothing, and under ceiling 2 a hostile room cannot raise the obstacle; measured once in two seasons (H-215). Loop L-1 (standing concentrates) is unbounded in code (PR-104). **Evidence:** CODED, non-conforming.

### J2 · The proceeding's own record: recorded defeat, division list, open vs sealed floor — **FITS-IF-ADAPTED**
Entries: CD-009, OP-042, OP-066, HP-058, CD-067, OP-080, GV-093, GV-053, PR-042, HP-052, CD-072.
Adaptation: carry it **distributed**, not as a store: the carried-and-unexecuted `resolution` is *senatus auctoritas*; a vote-down is a witnessed lapse; each `commit` is an act, so whoever witnessed or was told of it already holds who committed (residual: attendance is unmodelled, B4, so "who witnessed" is thin today; not run). **False N-line:** a per-seat division Record or `records_dissent` reader duplicates what witnessed commits carry (disqualifier 1), and "nay" is not an act, so nothing produces it (disqualifier 2). The floor key earns its N-line only as an admission predicate on presence: sealed councils then leave fewer witnesses — HP-052's "consensus suppresses dissent" made mechanical. Failure severity by who saw it (CD-072) is the same rule. **Evidence:** PROPOSED/RESEARCH + CODED witness layer.

### J3 · Witnessed claims as institutional memory: descent costs, `seen` structure, all-five fan-out, forgetting — **ALREADY-HELD**
Entries: PR-006, PR-018, PR-017, PR-031, PR-079, (cross) NL-053, NL-054, NL-063.
No concession-penalty field: everyone present deposits that you conceded. Fan-out on five channels makes ledgers differ (3 differing pairs vs 0), so hearsay, misattribution and secrets are reachable. Jordan's ruling that free descent in a closed room is correct (PR-031) relocates the risk to forgetting. **Limit:** the room learns *that* a descent happened, not how far (C-2).

### J4 · Pressure as a standing-band crossing; prestige vs dominance routes — **PARTIAL**
Entries: CD-073, PR-014, HP-043.
Fits the small recurring court cast only: proven on a hand-built world, never fires in realm play because nothing mints claims on `person_predicates` members; floors are injected (H-223). Prestige erodes slowly, dominance collapses on one called bluff — coded as route erosion.

### J5 · Typed persistent records: Precedent/Grudge/Debt spine, the Venetian *relazione*, extraction ledgers — **FITS-IF-ADAPTED**
Entries: OP-024, OP-089, HP-099, HP-065, HP-039, OP-083.
Adaptation: Records minted by acts and held by persons (`record_kinds`, reachable by `forge`, `destroy_record`, `hold`, `give`), never faction-held tags with TTL. The *relazione* — cumulative, stealable, decaying by confidence — is exactly a held Record. OP-089's finding (every contest output dead-ended as a stat delta) is the churn principle's diagnosis.

### Is J thin in the repo or in the gathering? Mostly the gathering.
J has 23 primary entries but **125 entries carry J as a secondary tag** (19 in part 1, 34 in part 2, 72 in part 3): reception, proofs and the mirror test were sorted under C; witness, `told_by`, regard and the chronicle under K. The real repo gap is narrower: the **proceeding-level record** — minutes, division, defeat, precedent — has no code (CD-009; NL lane: no evidence-weight, precedent or commitment stores). J2 judges that this gap should stay a gap in store form.

---

## 5. Ranking by fit for purpose

1. **B3 council-as-one-seat** — all six directions, zero new objects, membership is a person's decision.
2. **D2 vote as counted commits** — persons act, nothing stored, reversal priced; held back only by content-blindness and reach 0.
3. **J3 witnessed claims** — memory with no store; story arrives with no player.
4. **A2 petition/carry** — the only coded S-UP carrier.
5. **D3 elections and composition** — answers the empty throne; no new object.
6. **A1 docket** — coded and running; mostly Failure output.
7. **A4 attention tiers** — per-person salience; mis-ranks the sitting question.
8. **J2 distributed record** — senatus auctoritas for free.
9. **A5 motion origination** — attributable motions; futures unarguable.
10. **B5 lapse** — one witnessed event closes the silt.
11. **A3 grievance accrual** — repairs A2's silence dominance.
12. **D7 veto as witnessed act.**
13. **J5 held Records.**
14. **A6 agenda control** — strong story, needs priced drops.
15. **D6 first defector** — one term, tier-3 evidence.
16. **B4 attendance** — churn, unreachable today.
17. **J1 reception** — right idea, non-conforming code.
18. **D1 determine** — runs, decides by seed.
19. **B1 arrangement rows** — good shape, 12 inert keys.
20. **J4 standing crossing** — never fires in the realm.
21. **B6 layered bodies** — realm only.
22. **B2 rank order / latitude** — waits on intra-season order.
23. **D8 sortition**, 24. **D5 kernel trackers**, 25. **D4 faction-stat parliaments**, 26. **A7 policy sim** — misfits.

**Clusters that most affect the others.**
- **D2** collides with C (argue never reads the Proposition; proposal §5 builds 1–2) and M (no risk/horizon term, NL-033): until the voter weighs content, every opinion mechanism in C is empty at the division.
- **B3** leans on H (consent for land transfer, T3a's missing data owner) and G (how far a resolution binds, Jordan's call 2); it is the prerequisite of D2's bench, D3's electorate and B6.
- **A1 (via H-80)** — the docket naming no arrangement zeroes every row-keyed rule in B1, D2 and J2 in computed play.
- **J3** feeds K: the witness layer is what turns D2's commits, B5's lapse and A3's drops into ledger differences a third act exploits (PR-085, NL-111).
- **A5** leans on K's occasion ladder (NL-068) and I's strain; P-24 (no producer for futures) caps deliberative motions.

---

## 6. Verification (opened at `d90b6e8d`)

| claim | opened | held? |
|---|---|---|
| Only `disposes` has a production reader (CD-007/HP-045) | grep of `engine/season/**/*.py` minus tests and loader: `records_dissent` only in `harness/probes.py`; `venue_min_rank`, `disposal_reach` none; `term_required` "has no reader" (`effects_information.py:597`); `disposes` at `:336,:521`, `gate.py:257` | **held** |
| Council membership is a Query over `oblige` (CD-043) | `world_q.py:2184` `establishment_of`; `01_AXIOMS.md:1537` §E.2.5 | **held** |
| Quorum is bench size, shipped 1 (CD-017) | `fixtures.py:926-943` | **held** |
| Tally ruled as a count declared by a later act (CD-049) | `editorial_ledger_sc_archive.jsonl:37` | **held** |
| CR-34 realm reach 0 (CD-060) | `valoria_master_workplan_v10_part4.md:352-357` | **held** |
| Petition closers ruled but unbuilt (CD-022 vs HP-080) | `verb_table.yaml:1011-1047`; no `withdraw`/`deny` verb rows | CD-022 **held**; HP-080 overstates |
| `carry` is built, not a no-op (HP-079 caveat) | `effects_information.py:355-386` `_eff_carry` | entry **held**; the caveat's source is stale |
| Five attention tiers; non-ambition sitting question lands low (CD-025) | `world_q.py:2654-2690` | **held** |
