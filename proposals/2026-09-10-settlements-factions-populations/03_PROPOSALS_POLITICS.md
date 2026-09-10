# Part B (2 of 2) — the political proposals: P5 · P6 · P7

## Status: **PROPOSED (2026-09-10). HELD BACK IN FULL** — see `00_INDEX.md`.

These three run on P1–P4's substrate but do not require it: P5 and P6 are formable today against a
hand-seeded world, and P7 is runnable by an authored act. Grades and the `assumption` discipline are
as `02_PROPOSALS_SUBSTRATE.md` states them.

---

# P5 · RISK OF REVOLT IS A QUERY

### `commit_share`, the `commit` effect, and the barrier band

**Claim.** The share of weight at and under a rung whose live commitments are to a proposition
incompatible with the holder's is computed at the barrier, emits on a band crossing, and is readable
by **no person** — and the same Query, summed over seats, is the ratified §5.1 *"factions hold
people"* arithmetic.

**Starts from.** `architecture/meta/09_WORKED_EXAMPLES.md:89-91` (the licensed form) and `:174`
(*"not computed anywhere"*); `world_q.py:53-69, 116-124, 149-154`; `verb_table.yaml:97-111` `commit`
(typed precondition, `writes: [Tenure.since]`, **no effect**, so it raises at `driver.py:856-865`);
`Proposition(id, mood, subject, predicate, value, when, scope)`, frozen (`carriers.py:409-419`);
`holonic:517-520` — *"Membership is `commit`. Leadership, presence, density and footprint are
Queries"*; `02_HIERARCHIES.md:94-95` — *"`holdings(faction)` and `members(faction)` are NAMED
QUERIES"*; the `Faction` view (`10_FACTIONS:25-30`) **with no resolver**;
`systems/settlements/reference/scale_hierarchy_v1.md:83-93` §5.1 (**RATIFIED 2026-07-13**); `ID-17`'s
*"a band on a Query"* (`01_AXIOMS.md:617`); and `W31(a)`'s *"commit first"* (`PLAN.md:1649-1651`).

**Adds.**
- **`EFFECTS["commit"]`** — mint `Tenure(subject=actor, object=prop_id, kind="commit", since=tick)`
  via `w.add_tenure`, the `_eff_confer` pattern; refuse if the actor already holds a live commit to
  the same Proposition (idempotent), emitting `commitment.refused`.
- **`faction_q.resolve(w, prop) -> Faction`** — the resolver `04_CODE:427` names and `queries/` lacks.
  `members = [t.subject for t in lateral(w, "commit", "commit") if t.object == prop]` — **live edges
  only**, since `lateral` filters `t.live` (`world_q.py:126-130`);
  `holdings = ∪ hold Tenures on Rungs by members`; `seats = ∪ hold on Offices by members`; `head` by
  the proposition's own rule
  `[assumption: the holder of the highest-ranked seat among members; sweep: highest rank / earliest commit / none]`.
  **A view. Discarded at the next barrier.**
- **`incompatible(w, a, b) -> bool`** — a **structural** test, no natural-language processing: two
  `OUGHT` Propositions with equal `subject` and equal `predicate` and unequal `value`.
  `[GAP: incompatibility beyond same-predicate contradiction is unspecified; recorded as a hole row rather than guessed]`.
- **`commit_share(w, rung, holder_prop) -> (num, den)`** —
  `den = Σ weight(p) for p in persons at and under rung` (via `descendants` + `presence`, weight-summed
  per `T-l`); `num = Σ weight(p)` for those holding a live commit to a proposition `incompatible` with
  `holder_prop`. **Guarded by `commit_count_guard` on the edge list**, so an ended edge in the sum
  raises. Computed at the RESOLVE barrier's end and at CENSUS; cached in `queries/cache`.
- **The band crossing** (`ID-17`; `09:104-106`) — `band_floors` gains a `commit_share` row
  (`assumption`, e.g. `{third: 333, half: 500}` on `condition_scale`; swept declared/halved/doubled,
  exactly as `band_floors` already declares at `rosters.yaml:956`). At the barrier, if the share
  crossed a floor since the last barrier, emit `commit_share.band_crossed` with `subject = rung` and
  `causes = [the commitment.made / commitment.ended Events since the last barrier]` — **never
  `[ROOT]`**. It is witnessed by presence like any Event, and it changes what may be chosen only
  through **who is present**: acts requiring co-committed persons at the venue become formable.
  ⚠ **A Query term in `requires` is refused** — `F.33` names that gap, and `rosters.yaml:871-872` says
  the closed operand roster *"is what stops the grammar becoming a second resolver."*
- **`faction_value(w, prop)`** — the §5.1 ruling's arithmetic:
  `Σ weight(m) × (1 + rank(seat) for seats m holds)` over members, where `rank` is the ordinal of the
  seat's `scope_rung` in `rung_kinds` (`rosters.yaml:595-611`). This replaces legacy Mandate's
  `W_s × q_s` (`settlement_layer_v30.md:165-166`) **with the same shape** — size-weighted, over
  people — saturating only if a consumer wants it to.
  ⚠ **`[GAP: no consumer.]`** Nothing in P1–P7 reads `faction_value`. It is the arithmetic this set
  claims makes ratified §5.1 executable, and by `ID-13` a Query no resolver consults is **declared,
  not built** — the same defect `01_PRIMITIVE_BASE.md` §2 files against `Sensation.standing`. The
  candid statement is that **P5 supplies §5.1's arithmetic and not its use.**

**New primitive?** None. Two Queries, one effect, one view resolver Layer 1 already named, one
`band_floors` row. **The Query term in `requires` is the primitive that was nearly needed, and it is
refused.**

**⚠ The direct warrant, and the limit it exposes — found late.**
`references/design_rulings_2026-09-06.md` **R7**, flagged there as ⭐ *the decisive ruling*, rules:
**"no magnitude carrier is admitted at any scale. Every aggregate is DERIVED, none is PUSHED."** That
is P5's whole approach as a ruling rather than an inference from `T-a`, and it settles the fork
directly — **echo model** (a battle lost → legitimacy −2 everywhere, instantly, uniformly) against
**architecture model** (only those who *learn* of it revise, at the speed news travels, suppressible and
deniable and forgeable) — with Jordan's *"yeah this is better."* It also rules that **there is no single
faction-legitimacy number**: it is *a field over the population*, so **a ruler can be wrong about their
own standing**, which makes §C.11's explanation contract structural rather than a courtesy.

⚠ **But R7 names a quantity P5 does not build.** It holds that *legitimacy, the leader's standing and
populace morale are Queries over `stance`/`convictions`* — over **interiors** — while *holdings count,
military capacity and influence are Queries over `hold` and `commit` edges.* **P5's `commit_share` is
the second kind**: it is the *risk-of-revolt* Query Reading 09 §2 licenses over `commit` edges, and it is
**not** the legitimacy Query R7 describes. Both are lawful and they are different. And R7's own
consequence is the hole this set leaves open: *"`H-62` is unavoidable and first-rank. Nothing moves
until a verb writes an interior"* — **so the legitimacy half cannot be built until something writes
`stance`, and nothing in this set does** (`05_` §6.2).

⚠ **And one caveat from R8**, which rules that every term of an observation — identity, act, motive — is
**independently unknowable and its own claim, not a field**: P5 assumes a witness of `commitment.made`
knows **who** committed. Under R8 that `who` term may be `None`, and a share computed from claims rather
than from edges would inherit that uncertainty. P5 computes over **edges**, resolver-side, so it is not
wrong — but *what a person believes the share to be* is a different and lossier quantity, and this set
does not build it. **Named.**

**Compliance.**

| axiom | argument | grade |
|---|---|---|
| `T-a` | share, faction and value are all functions of live edges, cached only at a barrier | **STRUCTURAL under the gate · MECHANICAL at runtime** — `Rung.__setattr__` **raises** on `unrest` (`carriers.py:531-538`) |
| L3 cl. 3 / `AX-6` | live edges only; `commit_count_guard` raises on an ended edge in the sum | **MECHANICAL** (`world_q.py:116-124`) |
| L3 cl. 2 | not a per-person tally — a count of edges, weight-summed, and `T-l` says weight is what a cohort **is** | **CONVENTION** — a reader must see that `weight` is not a grievance tally; the guard cannot distinguish. Said as such |
| `T-b` | the crossing emits and produces no outcome: *"It does not cause the revolt. The revolt is people choosing"* (`09:105-106`) | **MECHANICAL** — `world.py:351-357` refuses a social write by an Event |
| `T-f` / `AX-2` | resolver-side, `World` first; *"NO PERSON CAN READ IT"* (`09:110`) | **STRUCTURAL** for the signature (`choose` takes no World) · **CONVENTION + a scan** for the module boundary — `world_q.py:16-27` is an **AST guard**, which `04_CODE:98-99` excludes from STRUCTURAL by name |
| `T-h` / §D.11 / `ID-15` | the view owns nothing, is never `Act.actor`, never a `hold` subject | **STRUCTURAL** — `Act.actor: PersonId`; `hold`'s subject is a Person (`holonic:538`) |
| `AX-3` | commitment is what is held **right** (an `OUGHT`); evidence never writes it | **STRUCTURAL** — `D-18`'s signature construction (`04_CODE:1087-1088`) |

**Loop. Sign `+` — AND IT IS DECLARED-UNREACHABLE, NOT OPERATIVE. ⚠ CORRECTED BY THE ADVERSARIAL PASS;
THE FIRST DRAFT CLAIMED IT CLOSED AND IT DOES NOT.**

The intended loop: a `commitment.made` is witnessed → lands as a claim in bystanders' ledgers →
their candidates include `commit`, whose referent is the Proposition id → more commitments → a crossing
→ more witnesses. **The first arrow has no producer.**

`opening_set` forms a candidate only for `subject in q.referents` (`decision.py:183, 228`), and the four
question sources are the only referent producers (`world_q.py:157-253`):
- **Q2**'s referents are `(c.subject,)` and it fires only when `c.subject == p.id or c.subject in mine`,
  where `mine = {t.object for t in p.tenures if t.live}` (`world_q.py:176, 195-197`).
- **Q4**'s referents are `(prop.subject,)` — **the Proposition's `subject` field, not the Proposition
  id** (`world_q.py:230-231`).
- **Q1** never forms today (`occasioned_by`'s own docstring, `world_q.py:279-281`, `N1`); **Q3** is
  site- and verb-keyed.

> **So a Proposition id reaches a person's referent set only through Q2, and only if that Proposition is
> already the object of one of their live Tenures — that is, only if they have already committed to it.
> An uncommitted bystander can never form a `commit` Candidate.** P5 supplies `EFFECTS["commit"]`, which
> makes an **authored** commit execute; it supplies **no producer for a computed one**.

⚠ **This also sharpens `01_PRIMITIVE_BASE.md` §3.4, which was incomplete.** It diagnosed Reading 09
§2's chain as broken at four links and named link (d) as *"`commit` has no effect and raises."* The
chain's stated link *"among their candidates is `commit`"* (`09_WORKED_EXAMPLES.md:97-99`) is broken
**separately from the effect, at candidate formation** — so the chain has **five** broken links and this
set closes four.

**Therefore the `LOOP` row is registered as `+`, declared, and unreachable** — the same honest shape as
`H-102`, whose own `default:` cell reads *"UNDER THIS INSTRUMENT'S OWN FIXTURES IT CANNOT AMPLIFY AT
ALL"*. **Bound** (which applies once a producer exists): `scene_budget`; `presence` under `all_five`;
`repudiate` (P6); and `claim_decay_per_season` (`H-103`).

⚠ **What would close it is a fifth question source — R6's *"a world-fact changed in a way that concerns
me"* — and that IS a new primitive**, priced as one rather than smuggled in as a data fix. This set does
not propose it. `[GAP: no producer forms a `commit` candidate for an uncommitted person; the repair is a
fifth `question_sources` member, which is a design change and not a table edit.]`

**Victoria 3's "attempting the measure mobilises the opposition"
(`research/valoria_game_precedent_companion_v1.md:120-122`) is therefore *available* on this shape and
**not delivered by this proposal**.

**Bound:** `scene_budget`, since each commit is a scene; `presence`, since only those at the venue
witness under `all_five` (`fixtures.py:209-235`); **`repudiate` (P6)**, since the edge is reversible so
the share can fall; and `claim_decay_per_season`, since an unrenewed claim about the proposition fades
(`H-103`) and stops raising Q2. Declare a `LOOP` row naming all four.

**Gap filled.** Reading 09 §2's Query; **ratified §5.1, unexecuted since 2026-07-13**; ED-FA-0004's
inert L/PS, re-expressed (`05_` §2 row 4). §D.11's debt — *"territory held by a banner nobody
carries"* — is **not** reopened, because holdings are read off members' holds (`04_CODE:944`, row 14).
`W31(a)`.

**Borrows.** **Tropico's mutually exclusive approval**, for free: a person may commit to two
incompatible `OUGHT`s and *"their own scoring will make them betray one"* (`09:15-16`). **Tropico's
die-hards swaying moderates**: a cohort at weight 200 that commits after one `tell` **is** 200 minds
moved by one scene, with distortion in transit. **Pax Pamir's loyalty-as-the-thing-that-carries-value**
— §5.1 is that ruling in Jordan's own words. **Victoria 3's mobilisation-on-attempt.**
**Refuses.** Any `unrest`/`Order`/`popular_support` field on a Rung (the `_DECLARED` whitelist raises);
*"sum everyone's grievance"* (`09:86-87`, the banned ratchet); Tropico's approval **meter**;
`lps_wiring_v1.md`'s `HELD/CONTESTED/SLIPPING` as a **stored** `control_state` (`:101-108`) — the bands
on the Query are that machine without the field; and its *"2 consecutive Accountings → Independence
roll"* (a threshold producing an outcome, `T-b`).

**Falsifier. ⚠ REWRITTEN — the first version could not observe its own failure, which is `ID-10` in the
shape §0.1 pt 2 names.** It asserted that `commit_share(S, X)` equals the weight-sum of live commits to
`Y`, with a control of *"no `utter` → the share raises"*. **On a tree where nobody can form a `commit`,
both arms pass: `0 == 0`.**

`test_p5_the_share_rises_only_by_scenes_and_falls_only_by_repudiation`: seed an `utter` of
`OUGHT(subject=S, predicate=holder, value=X)` by the mayor and `OUGHT(S, holder, Y)` by a rival, **then
seed authored `commit` acts** — because P5 supplies the effect and not the candidate.
**First assert the treatment arm is non-degenerate: `len(live commits to Y) > 0`.** Then assert
`commit_share(S, X)` equals the weight-sum of those commits over presence at and under `S`; that every
rise coincides with a `commitment.made` in the log and every fall with a `commitment.ended` or a
`person.died`; that it **never reads an ended edge** — plant one and assert `Forbidden` from
`commit_count_guard`; and that `commit_share.band_crossed.causes` names only commitment Events.
Control: no `utter` → the share is **undefined and raises, not 0** (§42.2's polarity rule), and no
crossing. **A second, adverse control:** run the corpus chooser with **no** authored commits and assert
that **zero `commit` Candidates form** — pinning the gap above rather than hiding it. **Assert on edges
and the log, not on a counter.** A failing run: a crossing with `[ROOT]`, a share that moves with no act
in the season, or a green test over an empty edge set.

**W-item.** `W31(a)` (`commit`), `W27` (`one_line` → the `OUGHT` Proposition, so every cast has a
faction), `W28` (the 47 re-scaled faction cases become office-holders whose *faction* is this view).
**Supplies the behaviour `PLAN.md` §4B.2:1365-1367 says re-scaling does not buy.**

---

# P6 · FORSWEARING COSTS

### `repudiate` with entrenchment, and no counter

**Claim.** Switching allegiance is always possible and never free, and the cost is **positional and
epistemic** — exposure to `revoke`, a reset entrenchment, and a witnessed `commitment.ended` — never a
stored penalty.

**Starts from.** `verb_table.yaml:402-412` `repudiate` (typed *"a live commit exists"*, writes
`Tenure.until`, emits `commitment.ended`, **no effect**); `T-m`'s *"the owner's discretion,
`subject == actor`"* (`01_AXIOMS.md:1156`); §15.2 — *"A revoked tenure is a historical claim subject…
Do not delete rows. `entrenchment(h, H) = min(1, seasons_held / 60)`"* (`holonic:553-556`);
`entrenchment_seasons = 60` (`fixtures.py:295-298`, *"THE 60 IS IN-CHAIN"*); `T-o`, a revocation
declared on the seat (`01_AXIOMS.md:1158`); `Office.faction` (`carriers.py:443, 470`); `revoke`
(`verb_table.yaml:439-444`, which **has** an effect); and the corpus finding that **no costed act of
switching exists** (`faction_layer_v30.md:215, 221`).

**Adds.**
- **`EFFECTS["repudiate"]`** — write `until = tick` on the actor's **own** live `commit` Tenure to the
  named Proposition; refuse otherwise.
- **`entrenchment(w, person, obj)`** as a Query on `since`/`until` of the **current live** edge — so a
  fresh commit after a repudiation starts at 0. The §15.2 reclaim rule (from-scratch
  `04_hearth_and_community.md:298-301`: *"entrenchment < 0.5 — an administrative act"*) reads it.
- **Exposure, not penalty.** A person who repudiates the proposition of the faction whose body seated
  them **still holds the seat** — the `hold` is theirs, §15.1 — but the seat's `revocation` basis
  (`T-o`) becomes exercisable by a superior *because the superior's Q2 fires*: `commitment.ended` is
  witnessed, deposits a claim, and `revoke`'s precondition — *"the office's revocation basis, and a
  live hold exists"* (`verb_table.yaml:441`) — is met. **Whether anyone revokes is a person's choice**
  (`AX-1`). *"What a person cannot do is forswear unnoticed"* (`T-m`).
- **The record persists.** The ended edge is readable by `tell` (the teller *"holds a claim on the
  subject"*, `verb_table.yaml:478`) — **a defector's history travels by telling, distorting in
  transit.**

**New primitive?** None. One effect; one Query on fields that exist.

**Compliance.**

| axiom | argument | grade |
|---|---|---|
| `T-m` / `AX-6` | closure by the owner; the edge ends, the row persists | **STRUCTURAL** — `Tenure.until` on the subject's own Tenure; `world.py:373-379` bounds the actorless case |
| L3 cl. 3 | no count over ended edges anywhere in P5 or P6 — `entrenchment` reads the **live** edge's `since` | **MECHANICAL** (`commit_count_guard`) |
| `AX-6` (ratchet) | no Coup Counter, no Demotion Magnitude field, no "Dishonored" flag | **STRUCTURAL** — no slot; `Person` admits only the four categories plus read-off (`01_AXIOMS.md:742-754`) |
| `T-a` | "faction Standing" is not stored; exposure is a Query over seats and bodies | **STRUCTURAL** |
| `AX-2` | the defector does **not know** whether their repudiation reached the superior — it depends on channels (`fan_out_mode`) | **STRUCTURAL** (`choose` has no World) |

**Loop. Sign `−`.** Repudiation removes an edge; the share falls; exposure invites `revoke`, which
removes a seat, which lowers `faction_value`. Damping; `default: none`.

**Gap filled.** The measured absence of any costed act of switching; `ID-14`'s closer for `commit` (an
act opens it, an act closes it); and the **Löwenritter Coup Counter that *"never decrements"***
(`factions_personal_v30.md` §8.9), which is refused as an `AX-6` ratchet and replaced by this.

**Borrows.** **Pax Pamir's punished loyalty-switching, in its exact shape**: what you forfeit is what
you got *through* the loyalty — seats conferred by that body, and entrenchment — **not a stat**.
**Wildermyth's legacy binding**: the ended edge is a queryable trace.
**Refuses.** Pax Pamir's **discard** — Layer 1 keeps the row (*"Do not delete rows"*);
`faction_politics_v30` §1.0a's Demotion Magnitude table as a stored penalty, which is a `standing`
write nobody's act made — and `08_ch5`'s **Imperator: Rome** guard applies here in the *other*
direction, as an **unmitigable** penalty; *"Begin at Standing 0 in new faction"*
(`faction_layer_v30.md:221`) — there is no Standing to reset; and the Coup Counter.

**Falsifier.** `test_p6_forswearing_is_possible_costly_and_noticed`: `p_high` holds `off_duke` (whose
body belongs to some faction) and a commit to its proposition; `repudiate` → the commit's
`until == tick`, **the hold is still live** (no automatic loss — `AX-1`), `commitment.ended` is in the
log with `causes = [act.id]`, `entrenchment(p_high, off_duke)` is unchanged (the seat was not
forsworn) while `entrenchment(p_high, prop)` is 0 on any new commit; a witness at the venue holds a
claim about it next season and, **if that witness holds `remit:revoke` over the seat**, `opening_set`
offers `revoke`. Control: `fan_out_mode = presence_only` with the superior absent → no claim, no
`revoke` candidate — so *"forswear unnoticed"* **is possible under a narrow channel, and that is the
epistemic game**, which the test names as the residual rather than hiding. A failing run: any field on
`p_high` decreasing on repudiation.

**W-item.** `W31(a)` (`repudiate` is on its no-hole list); `W24(b)` (per-witness attribution) sharpens
*"noticed"*.

---

# P7 · A DISPENSATION IS A DOCUMENT

### the terms roster, and suspicion as a Query over one ledger

**Claim.** Goldenfurt's Directive **is** Layer 1's `issue`, once the nine typed terms exist as a
`Record` kind's `subject_matter`; compliance is a contest per executor; suspicion is the issuer's own
ledger, decaying; and recall is `revoke`.

**Starts from.** `verb_table.yaml:241-246` `issue` (eligibility `remit:issue`, requires *"scope
enumerates executors, not places (§37.1)"*, writes `Dispensation.exists`, emits `dispensation.issued`);
`comply` / `evade / defy` / `refract` (`:112-124, 203-210, 389-396`), all requiring *"a claim of the
dispensation's terms is in the actor's own ledger"* and all **untypable, because no operand names a
dispensation** (`:117`); `(Dispensation, exists) · [RES]` (`write_matrix.yaml:112-118`, *"as `(Petition,
exists)`"*); `F.15` — *"nine typed terms and nothing lists them… the entire downward mechanism has no
executable content"* (`04_CODE:1077`);
`Record(id, rung, kind, forgery_quality, subject_matter, ttl, stages)` (`carriers.py:397-406`) and
§D.4's *"the fact that can leave the head that holds it"*; `single_holder_counter` raising for want of
the closed axis registry (`world_q.py:89-114`) with L3 clause 1's *"legal, since every increment is in
the holder's own ledger"*; NPC-083's need 3 (`NPC2.yaml:107-109`); and `09:40-41, 149-151` — *"a
dispensation does not apply; it lands as a compliance contest per executor."*

**Adds.**
- **A dispensation is a `Record` of kind `dispensation`** at the issuer's rung, with
  `subject_matter = {term: <dispensation_terms member>, executors: [PersonId], amount?: int,
  kind?: MatterKind, by?: DateId}` and `ttl` = the term's horizon — a `T-n` declared term, closable by
  its own clock, on the `(Record, ttl)` row at MAT (`probes.py:1500-1511`). `issue`'s effect is
  `create_record`'s (`effects.py:232`) with the kind fixed.
  ⚠ **This types the operand `comply` needs without opening the closed operand roster:** the
  dispensation is the act's `subject` (a Record id), and the typed cell is
  `{form: existence, of: subject, kind: Record}` plus the ledger clause the grammar already has for
  `tell` (form 6, `verb_table.yaml:117`).
  ⚠⚠ **AND THIS OVERTURNS A WRITTEN REFUSAL, WHICH THE FIRST DRAFT DID NOT FLAG AND P1'S EQUIVALENT
  DID.** `verb_table.yaml:117` says the opposite of the enabling half: *"Typing it as `of: subject`
  would assert that an act's subject IS the dispensation whose terms are sought, **which no in-chain
  document says**."* And `rosters.yaml:873-876`: coining an operand *"would be filling `H-94` by
  keyword argument, which is **the ruling `H-94` is waiting for** and not a table edit."* **P7's move
  is defensible under §0.05** — making the dispensation a `Record` is precisely what supplies the
  in-chain warrant that was missing, so the refusal's own stated reason lapses — **but it is a
  decision that overturns a written refusal, and it belongs in the held-back list beside the
  starvation comment** (`00_INDEX.md`). Named.
- **A roster `dispensation_terms`.** Layer 1 says *nine* and lists none. Seed with what the corpus
  names, marked `incomplete: {have: 6, target: 9}`: `extract` (levy matter) · `tax` (a standing
  extraction) · `suppress` (an office or proposition named) · `install` (confer a named person to a
  seat) · `host` (quarter persons at a rung) · `cede` (transfer a hold). **Each term names the verb its
  compliance IS** — `extract → transfer`, `install → confer`, `cede → revoke + confer` — so `comply`'s
  `writes: []` with `writes_note: "per the term's own row"` (`verb_table.yaml:122`) becomes a dispatch
  to an effect that already exists.
- **How it reaches the executor.** The Record is **carried** (`H-84`/`W24(a)`: a `hold` on the Record
  moves by the confer/revoke pair) or **told** (`tell` executes, and distorts). **No delivery is
  automatic**, so *"never heard"* stays distinct from *"heard and refused"* (`09:157-158`).
- **Suspicion is `Σ confidence` of claims in the issuer's ledger** whose subject is the executor and
  whose predicate is `compliance.withheld` — **one holder's ledger, per `(Person, axis)`, which L3
  clause 1 permits**. `compliance.given` claims land in the same ledger and are read by the same
  `stance_toward`. ⚠ **Jordan's E11 symmetry falls out** (`HANDOFF_FA.md:170-175` — *"if there is a way
  to advance suspicion from non-compliance, there must be a way to reduce suspicion by
  over-compliance"*): over-compliance is more `compliance.given` claims. Decay is
  `claim_decay_per_season` (`H-103`), so **a ratchet is impossible**.
- **Recall is `revoke`** — which exists and has an effect — exercised on the seat's `revocation` basis
  when the issuer's candidates rank it, which requires a Q2 question from a landed
  `compliance.withheld` claim.

**⚠ The direct warrant, found late.** `references/design_rulings_2026-09-06.md` **R5** rules that
*"not every fact of the world or record of event lives in memory — much of it is documented and borne
bureaucratically"*, and distinguishes **engine persistence** (snapshot, save, load, the log) from
**DIEGETIC persistence** — *"what the world itself holds, in objects that outlive the witnesses and can
be moved, copied, forged, seized and burned"* — ruling the second **a game mechanic**. That is P7's
subject exactly. R5 also notes that three of the five WITNESS channels are **bureaucratic rather than
memorial** (`document_key`, `post_remit`, `chronicle`), and that `forge` and `create_record` share
`record.created` **so a document's holder cannot tell** — which is P7's forgeability, already built.

**New primitive?** None. A `Record` kind, a roster, and effects for verbs whose rows exist. Layer 1's
"Dispensation" was already a dict-modelled kind (`carriers.py:550-551`); making it a `Record`
**collapses one unmodelled kind into an existing carrier** — a schema change that *removes* an
exception, which is the only kind §F.1 blesses.

**Compliance.**

| axiom | argument | grade |
|---|---|---|
| `AX-1` | the issuer is a named person with `remit:issue`; the executor complies or defies by an act; **nothing "arrives"** | **STRUCTURAL** (`remit:` eligibility; the `Act.actor` check) |
| `T-c` | the term's horizon is a declared `ttl` set by the opening act, and it **has handles** — burn the Record, kill the issuer (`driver.py:343-348`'s *"did not mature: its winder is gone"*) | **MECHANICAL** — `(Record, ttl)` at MAT is the licensed form (`probes.py:1514-1529`, W8) |
| §37.1 refraction | scope enumerates executors; each is a separate compliance act | **MECHANICAL** (`issue`'s `requires`, once typed) |
| `T-a` / L3 cl. 1 | suspicion is a single-holder ledger Query; no cross-holder sum | **MECHANICAL** (`aggregate_guard(per_person_tally=False)`; the sum is over one ledger) |
| `T-b` | no threshold recalls anyone; a person with the remit **chooses** `revoke` | **STRUCTURAL** |
| `AX-2` | the issuer's suspicion is **what reached him**; an executor whose defiance was not witnessed is not suspected | **STRUCTURAL** (the fan-out channels) |
| §D.4 | a dispensation is takeable, burnable, forgeable — `forge`'s row exists (`verb_table.yaml:230-235`) | **STRUCTURAL** — it is a Record |

**Loop. Sign `−`.** Defiance → a claim → (maybe) `revoke` → fewer defiers in seats. Compliance
accumulates nothing. Damping.

⚠ **The G606 recall death-spiral cannot be built here**
(`goldenfurt_slice/reference/verification_findings.md:25`). `08_ch5` guard 1's arithmetic — run maximum
mitigation against maximum accrual — comes out as: max accrual is one `compliance.withheld` per issuer
scene per season (≤ `scene_budget`); max mitigation is decay at `claim_decay_per_season`, plus eviction
at `ledger_cap`, plus `compliance.given`. **That is a fixture sweep, stated as `assumption`, not a
design risk.**

**Gap filled.** `F.15`; `H-43/44/45` (the dispensation verb family, `PLAN.md:1372`); NPC-083's needs 3
and 5; and **ED-FA-0021 merged into G606** — both become this one Query, which is the merge Jordan
ruled and nobody executed. `ED-FA-0020`'s hostage-kin becomes a `knot`/`hold` a superior takes — **no
new object.**

**Borrows.** Goldenfurt's six typed Directives and its comply/bargain/defy fork — where **bargain =
`petition` + `carry`**, both of whose rows exist. ***Residencia*** (SE-7): the end-of-tenure audit is
`open_case` with the executor's `compliance.withheld` claims as the stages' evidence — a Record the
Inquisitor declares. **Victoria 3's recorded defeat**: a vetoed dispensation persists as a Record with
no force, for free.
**Refuses.** The **mandatory seasonal Directive** (`sim_build_spec.md:107-108`, *"NEVER none"*) — an
unwound clock, `T-c`; a **suspicion field** (`registry.py:78`); a **recall threshold** producing an
outcome; Goldenfurt's `Directive → suspicion → Konrad progress` chain as a **tick** (Konrad's progress
is his own `commit`-to-`OUGHT` and his own scenes); and the PA **priority tree** AI
(`sim_build_spec.md:104-106`) — the issuer's choice is `choose`, with convictions and a question, the
same as everyone's.

**Falsifier.** `test_p7_a_writ_that_nobody_carried_was_never_defied`: the King `issue`s an `extract`
naming `p_high`; under `presence_only` with `p_high` elsewhere, `p_high` forms **no** `comply`/`defy`
candidate, because no claim of the terms is in his ledger; a `tell` by a bailiff present at both venues
across two seasons → the claim lands → **both** `comply` and `evade / defy` appear in `opening_set`;
`defy` → `compliance.withheld` → the King's ledger next season → `revoke` in the King's candidates
**iff** he holds the revocation basis (`in_holdings`, `predicates.py:59-70`). Assert suspicion falls
with no further defiance by exactly the decay fixture. A failing run: a `comply` candidate with no
claim of the terms in the ledger, or a `revoke` that fires with nobody choosing it.

⚠ **CORRECTED — the test passes and the stated mechanism was wrong.** `p_high` forms no `comply`
candidate **not** *"because no claim of the terms is in his ledger"* but because **no question has the
Record as a referent** (clause 3). Clause 4's ruled polarity is *"KNOWN-FALSE… Absence of a belief is
not a belief in the negative"* (`decision.py:208-214`), so **the ledger clause does not drop the
candidate.** The falsifier is sound; the explanation beneath it was not, and a reader who built from
the explanation would have built the wrong thing.

**W-item.** `W24(a)` (a Record moves — this proposal **needs** it for carrying); `W21` (`remit:issue`
formable person-side — `H-71`); `W26` (the sitting, for the audit). **P7 without `W21` cannot be
*formed* by an NPC issuer**; it can be run by an authored act today.
