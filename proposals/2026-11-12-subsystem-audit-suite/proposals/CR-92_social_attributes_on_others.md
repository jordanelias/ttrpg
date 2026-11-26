## Status: PROPOSED — CR-92 (workplan v12 B24.41, DESIGN-FIRST). No code. All six items are answered by the ladder; nothing is escalated.

# The social attributes acting on others: Grace on regard, promotion and the venue's standard; Presence on obedience; Attunement on bonds

**Source.** `workplans/valoria_master_workplan_v12_part22_cont.md` B24.41 (lines 210-224), which copies the intake's CR-92
REMAINING UNBUILT text. `master/eval/E1.md` "### CR-92", which the entry names as the carry-forward, **is not in the tree**
(`master/eval/` holds `E6.md` and `E7.md` only); this file works from the entry's copy. Jordan's words are
`proposals/2026-11-05-attribute-rulings-by-subject.md` (ED-IN-0347): AR-29 (Presence), AR-30, AR-31 (Attunement), AR-32 to
AR-36a (Grace), AR-49, AR-50 (the profiles); ED-IN-0350 (`argue` is Presence; Attunement is choice-side). Words are A-98's:
Grace, Presence and Attunement are attributes; a skill is a skill.

**Read at.** `2baec8e2f` (the hearing landed through B24.30; B24p.01-B24p.24 before it). Every claim below cites the code as
it stands. A design document is cited for intent only (`CLAUDE.md` §0.05).

**Controls.** Every term this design schedules has a control at which it reads nothing, writes nothing and moves no hash
(the entry's EXIT: *every term at 0 reproduces the base hash*). Each build it names is a declared MOVER (P14) above its
control and is not scheduled in v12 (the entry's HASH MOVERS).

---

## 1. How Grace reaches regard

### 1.1 `layer-conformance` Lens B on AX-2, answered first

**B0, the governing rows** (`architecture/meta/04_CODE_ARCHITECTURE.md`, §A.1 and §A.2, quoted verbatim):

- `:116` — *"**AX-2** no privileged access | the decision compiled where `World` is not a name; the two Query families split
  **by module**, not by first parameter; `sense()` called by the loop, never by the decision"*.
- `:169` — *"`queries/person_q` | nothing | **a `PersonInterior` snapshot only** | — | —"*.
- `:171` — *"`decision/` | **nothing.** Returns `Scene[]` | `PersonInterior`, `View`, `Sensation`, `budget`, `Question[]`, the
  table's declarations | — | **none**"*.
- `:178` — *"`loop/witness` | claim deposits into each holder's **own** ledger | this tick's log, presence cache, channel
  predicates, the act store | `claim.deposited` | INTERIOR"*.
- `:890` — the decomposition *"is admissible exactly to the extent the character's own ledger already names its terms"*,
  *"the only one `AX-2` permits"*.

**B1, both halves read.** For `queries/person_q`, `decision/` and `loop/witness`: the `owns`, `may read`, `emits` and `token`
columns, all four. Not read: the module list's members beyond these three.

**What AX-2 permits.** AX-2 binds the DECISION and the person-side Query family: `regard` (`person_q`) and every chooser term
may read one `PersonInterior` and nothing else. It does not bind WITNESS, which is a loop step holding INTERIOR and whose
whole job is to put into a holder's own ledger what he came to know. So the door the entry names is open: **the true value is
read on the World side; the holder reads only what WITNESS deposited.** One narrowing, found by reading `:178`'s `may read`
column against the code: it lists *this tick's log* and not `state/persons`. CR-79's `_credit`
(`engine/season/loop/witness.py:305-327`) reads two persons' held affiliations through `world_q.commensurate`, and
`_sitting_claims` reads `conflict(w.persons[d], ...)` (`witness.py:510`); both read past the listed column. This design does
not add a third such read, and it does not need to. **The true Grace is already read on the World side, by the proceeding,
and its result is already on the log.** The proceeding module computes `esteem` from the true Grace of the speaker and of the
man opposite (`modules/social_contest/proceeding.py:391-399`). The host passes those values in on the resolver side (the
`proceeding_input` builder, `seam/wrappers/sigma.py:1620`). The value is written as a cell of every `Beat`
(`engine/season/queries/inputs.py:432`; not in `UNWRITTEN`, `:448`), so it is on the Event's `ending`, which is *this tick's
log*. WITNESS reads that through `world_q.ending_beats` as `_sitting_claims` already does (`witness.py:485`).

**B2, the grade.** The property *"regard reads no World"* is checked by path for `decision/`: the import allow-list, which
admits `queries.person_q` and forbids the rest of `queries` and `state.world`, is at
`engine/season/tests/test_season_shape.py:2071-2120`. That is MECHANICAL for `decision/`. For `person_q`'s own body it is
CONVENTION, and this design adds no guard (§0.1 pt 5): the build reads only `p.ledger`.

**Disposition.** Conformant. The WITNESS door is permitted, and the carrier is in WITNESS's listed column. No B4 case arises.

### 1.2 The design

The entry says item (1)'s carrier is the `ending`'s per-side marks and esteem (B24p.20), which WITNESS deposits, and that
this design decides what regard does with them. CR-79 is the precedent: a term computed at WITNESS, frozen into what the
holder holds, read later only from his own ledger.

1. **The deposit (WITNESS).** `rosters.yaml: sitting_claims` (`:994-1023`) gains one kind, **`decorum`**.
   - **Subject and sum.** `Beat.esteem` is the VOICE's: the module builds it as `esteem(inp, st, voice)`
     (`modules/social_contest/proceeding.py:1041`). The other kinds are filed under `b.mover` (`witness.py:496-507`), but
     this one is not. Its subject is `b.voice`, and the true sign is that of the sum of `b.esteem` per voice over the
     sitting's beats. There is no claim where the sum is 0.
   - **What esteem measures.** It is RELATIVE: `_short(opposite) - _short(him)` (`proceeding.py:395-399`). A Grace-3 man
     against a Grace-1 man at standard 8 sums positive although he is short by 5. Two equal Graces sum 0 and deposit nothing.
     It also carries the opponent's pressing: `_short` adds `show · c.rattles` (`:392`), and a rattle is a press that
     landed, rolled on a pool Presence enters through `case_pool` (`:383-388`). So decorum is *conduct relative to the man
     opposite, as the room saw it*, not an absolute measure of Grace.
   - **The unopposed case.** With nobody opposite, esteem is `-_short(him)`, which is never positive. A voice deposits
     **nothing** unless some beat of the sitting was spoken for the opposite side (read off `Beat.side`; the ending carries
     no seating otherwise). A tell or a speech to an unopposed room therefore leaves no decorum. Comparing him against the
     ordinary middle man, the baseline `heard` uses (`proceeding.py:372-373`), would need the module to write a second esteem
     cell on every beat, a hash mover at every sitting, and it is not taken. `[ASSUMPTION; medium; Jordan to correct;
     revert: deposit `-1` where the unopposed sum is negative]`
   - **Holders read it, each in his own way.** The holders are every person in the room but the voice. Each holds the sign
     **as he reads it**, through the one reading function the bench's lean already uses: `seam/wrappers/sigma.py::
     bench_reading` (`:1605-1617`), deposited at `witness.py:537-542`, roster note `rosters.yaml:1014-1019`. It is a keyed
     draw true with chance `(1 + acc) / 2`, where `acc` is `accuracy` (his Attunement alone, `proceeding.py:790-793`, *"THE
     ONE LADDER OF A READING"*). Here the key is `decorum_read:<voice>`. The build passes the key's stem to `bench_reading`
     as a parameter and writes no second reader. A low-Attunement bystander is sometimes wrong about who bore himself
     better, which is AR-49's *"unaware of their impact"* read from the other side. The draw is gated by `decorum_gain` like
     the deposit.
   - **Form.** Firsthand, at `confidence_default`, never refracted, one per voice per holder per sitting. `_sitting_claims`
     (`witness.py:463-545`) writes it from `world_q.ending_beats(e)` and the holder's own Attunement (`bench_reading`'s one
     person read, B24.29's precedent). No `terms` cell is read. **The value is a sign, not the number:** the number would let
     a holder solve for a difference of two true Graces.
   - *Glossed (new word):* **decorum**, *bore himself better (or worse) than the man opposite, as the room saw it*. It is the
     ordinary English word nearest AR-33's *"seen as respectable/dignified"*. It does not clash with `bears`/bearer (the rite
     key) or with `heard` (an existing `sitting_claims` kind).
2. **What regard does with it (`person_q`).** `regard_parts` (`engine/season/queries/person_q.py:738-762`, the one owner)
   gains a fifth addend, **`decorum`**: `decorum_gain` times the sum of the values of the **chainless** (firsthand)
   `sitting:decorum` claims `p` holds with `subject == referent`. That is the test `_holds_live` uses, `not h.chain`
   (`witness.py:412`). Each claim is weighted by `state.ledgers.present_confidence(...)` over `confidence_default`, called
   directly (`person_q.py:63` already imports it; `person_q` may not import `world_q`). A TOLD copy is not counted.
   `said_of` (`person_q.py:1914`) can pass any held claim on, and a told decorum claim read here at full weight would move
   regard outside the told half's own gain (`H-121`'s defect). What a man hears of another's decorum enters regard, if at
   all, only through the existing `told` half at `told_valence_gain`; this design does not route it there.
   - **Build sites.** `RegardParts` (`:729-736`) gains the field. `regard` stays their sum, in the same left-to-right order
     with `decorum` last, and its four-way unpack at `person_q.py:783` becomes five-way. The chronicle's
     `regard_parts(...)._asdict()` (`harness/chronicle.py:305`) gains a key **even at the control**. That is a change to the
     chronicle's output shape, not to the game: the build checks whether any chronicle pin reads the dict's keys and
     re-records it, declared, if so. The precedent is CR-31's
   `heritage`: *"a third term at its own gain (0 reads nothing: the control)"* (`:760`). The new addend is kept apart from
   `judged`. `judged` weighs a deed by the holder's own pursuits (`deed_term`). Decorum is not valenced by what the holder
   wants, and folding it into `judged` would let one gain move two things (`H-121`'s defect, named in `regard`'s docstring).
3. **One gain gates both halves.** The fixture is `Fixtures.decorum_gain`. At its control, 0.0, WITNESS deposits no
   `decorum` claim and `regard_parts` reads none. This follows `_credit`'s rule: *"The caller calls this only when
   `regime_gain` is not 0"* (`witness.py:317`). A deposit with no reader would move every ledger, and so the content
   hash, at the control.
4. **Where it then acts, with no new term.** `regard` already has four person-side readers. Through them Grace acts on
   others' choices and opinions with nothing added:
   - `stance_term` (`choose.py:73`, reading `regard(p, c.subject)` at `:149-153`): an act on a man the actor saw conduct
     himself well scores as one on a man he regards more;
   - `fit_term` (`:294`): promotion, §2;
   - `teller_weight` (`person_q.py:2992`, regard at `:3000`, `:3062`): what the graceful man tells is credited more by those
     who saw him. This is CR-79's credit by another road, and it is AR-33's *"seen as respectable"*;
   - `opinion_terms` (`person_q.py:1043`, regard at `:1073`), read World-side through `world_q.opinion_of`
     (`world_q.py:3405`; used for grievance spread at `:3495`; it passes `w.fixtures`, so the gains apply): a faction's leader,
     or a member whose deeds he holds, who bore himself well before a man lifts that man's opinion of the faction. This is the fourth reader, and the build's mover reaches it.

   **It does not reach `reception`.** `world_q.reception` reads no judge's ledger (F8, SC-02 option B, B24.02:
   `world_q.py:1036-1037`, *"THE FOLD MAY ASK THE ACTOR'S OWN LEDGER AND NO OTHER"*). A bench member's decorum claims
   therefore never enter a later roll's obstacle. They act only through that member's own choices. This design keeps it so.
5. **Boundary with the fold.** The regard rows of the proceeding's fold (`Fixtures fold_carried`, `fold_accord`, ...,
   `data/fixtures.py:1602-1632`; readers B27.28, B33.51, not in the tree) price the sitting's OUTCOME. Decorum prices the
   CONDUCT. The fold must not also read `esteem`. If B27.28 lands a Grace reading, it is this addend, not a second one
   (`CLAUDE.md` §8).

**Falsifier.** A hand-built sitting with a trial-standard rite (`standard` 5) and two voices alike but for Grace (7 against 1),
opposite each other, with `decorum_gain` above 0 and a bystander of Attunement 7.
- After WITNESS the bystander holds `sitting:decorum` of each voice, and over the keyed readings the sign he holds of the
  Grace-7 voice is `+1` with the frequency `bench_reading`'s chance gives at his `acc`.
- On a key where he reads both truly (`+1` and `-1`), `regard(bystander, g7) - regard(bystander, g1) == 2 * decorum_gain`
  exactly. This uses a hand-built ledger with no other claim, so `==` and not `approx` (`CLAUDE.md` §0.1 pt 2).

Further cases each prove an absence or a rule the claim rests on:
- **(a)** Swap the two true Graces in `w.persons` AFTER the sitting is resolved and BEFORE WITNESS: the true signs the
  readings draw from are unchanged, because WITNESS reads the `ending`, not the speakers. A second bystander of Attunement 1
  on the same keys holds the wrong sign strictly more often than the Attunement-7 one (the one ladder of a reading).
- **(b)** A third person not in the room holds no `decorum` claim, and his regard of either voice is unmoved. **After the
  bystander TELLS him the decorum claim (a chained copy in his ledger), his regard is still unmoved**: the reader counts
  chainless copies only.
- **(c)** In an unopposed sitting (a tell), no voice deposits decorum, whatever the esteem sum.

**Control.** `decorum_gain` 0.0: no `decorum` claim and no `decorum_read` draw in any ledger, `regard_parts(...).decorum ==
0.0` reading no ledger, and the realm's content hash equal to the base. **The control must be able to see the failure it
excludes** (`CLAUDE.md` §0.1 pt 2). The test asserts that at least one sitting with a nonzero per-voice esteem sum and an
opposed voice occurs in the hash seeds. It also asserts that, at `decorum_gain` above 0 on the same seeds, at least one
`decorum` claim is deposited. Without both, hash equality at 0 shows nothing.

**Band and reading rule for `decorum_gain`.** The gain is in regard's raw unit. One sitting's decorum is worth one firsthand
deed of unit valence, so the gain reads at `judged_gain`'s shipped value. `[ASSUMPTION; medium; Jordan to correct — basis:
the claim is firsthand like a witnessed deed, and `judged_gain` 0.5 (`data/fixtures.py:892`) is what one such deed carries;
revert: 0.0, the control]`. Swept 0.0 (control) / 0.25 / 0.5 / 1.0. The upper end of the band is bounded by §6: the largest
value at which the profile pair still splits as ruled. Under `regard_unit: stance` (proposed, not shipped,
`fixtures.py:1352`) the build reads decorum in the unit it reads `judged` in. A new `hole_register.yaml` row carries the
setting, because `tools/ci_sim_fabrication_check.py` refuses a `Fixtures` setting with no row.

---

## 2. Promotion

**Verdict: not through `stance_term`. Through `fit_term`, a term the chooser already has. No `confer` edit.**

- **Why not `stance_term`.** `_stance_arm` reads regard toward `c.subject` (`choose.py:132`, `:149-153`). `confer`'s
  subject is the SEAT: `referent_class: Office` (`verb_table.yaml:285`), and `fit_term`'s own docstring says *"the
  candidate's `subject` being the seat"* (`choose.py:279`). Under the shipped `declared` arm (`fixtures.py:906`) the term reads
  regard toward an office, which nobody holds stance about. The swept `beneficiary` arm does not help either: `confer`
  declares `beneficiary: "subject"` (`verb_table.yaml:291`), so it too reads the seat (`choose.py:143-147`). In neither arm
  does the conferee's Grace reach the term. Making it reach would mean editing `confer`'s `beneficiary:` to `to`, a `confer`
  edit the entry asks this design to avoid, and one that would move every `confer` score under the `beneficiary` arm.
- **Why `fit_term`.** It reads `regard(p, to, fx)`, the conferrer's regard of the person the act would seat
  (`choose.py:294`). It does so on any row of the seating shape (`referent_class` `Office` with `counterparty` `to`,
  `:292`), never on a verb name. Once Grace reaches regard (§1), it reaches promotion through `fit` with nothing added. This
  is AR-35's *"likelihood of promotion, receiving an office"* on the conferrer's side, and AR-34's *"low standing but high
  grace"*: `fit` reads regard and not rank.
- **It is dark at shipped values, and that is a different row's decision.** `confer_fit_weight` ships at its control 0.0
  (`fixtures.py:1162`, `H-414`, swept 0.0 / 0.5 / 1.0), where `fit_term` returns 0.0 and reads no ledger (`choose.py:288-289`).
  Grace on promotion becomes live when `H-414` leaves 0.0. That is `H-414`'s own sweep, not a choice this design makes.
- **The appointment draw is not touched.** Whether the seat's room accepts the conferee (`confer`'s draw against the seat's
  displaced holder and the body's `reception`, `verb_table.yaml:296`) is a roll on the conferrer's score. The conferee's Grace
  does not enter it, and this design adds no obstacle term for it: a fourteenth key is refused, and so is a new host term
  for one verb (§3).

**Falsifier.** Set `decorum_gain` > 0 and `confer_fit_weight` > 0. A conferrer holds `sitting:decorum` `+1` of candidate A and
`-1` of candidate B, who are otherwise identical. Then `fit_term(p, confer→A) - fit_term(p, confer→B) == confer_fit_weight * 2
* decorum_gain` exactly, and `stance_term` is equal between the two candidates (it reads the seat). If `stance_term` differs,
the reading of §2 is wrong.

**Control.** `confer_fit_weight` 0.0: `fit_term == 0.0` for both and no ledger is read. `decorum_gain` 0.0: `fit_term` equal for
both. In either case the base hash holds.

---

## 3. The venue standard

**Verdict: built for the room at B24p.07 and B24p.13, read from existing keys. This design adds no key and no term. It
states the band and the reading rule, and carries the assumption the entry carries.**

- **The requirement, from the existing keys.** `standard` is already an arrangement key. It was the fourteenth when B05.21
  added it, and the count has been seventeen since B24p.03 (`engine/season/data/arrangements.py:12-16`, `_ARRANGEMENT_KEYS`
  `:83-86`). The regime table carries a `standard` delta (`_REGIME_KEYS`, `:92`; `arrangements.yaml:239-241`). The rite's
  standard is `attribute_midpoint() + DIFFICULTY_LEVELS.index(row["standard"]) + regime["standard"]`
  (`seam/wrappers/sigma.py:1475`). On the 1-7 scale (midpoint 4, `seam/wrappers/pool.py:100-103`) that runs from 3 (`plain`
  under a commune) to 8 (`hard` under a theocracy). The entry's *"no fourteenth key"* was written against the thirteen-key
  count. Read now, it means **no new key**: `data/arrangements.py` refuses an unknown key (`_refuse_unknown`).
- **Shortfall demotes; surplus adds nothing (adj §3.1 (12)).** `_short = max(0, standard + show · rattles - grace)`
  (`modules/social_contest/proceeding.py:391-392`). `esteem = _short(opposite) - _short(him)` (`:395-399`) enters the
  speech's leverage at `esteem_step`. The `max(0, ...)` is the *surplus adds nothing*, **at zero rattles**: a man who meets
  the standard is short 0, however far above it he stands. Under pressure the surplus is not idle. Each point of Grace above
  the standard absorbs one rattle at `show` 1.0 before he falls short, so a graceful man keeps his standing through presses
  that would cost a man who barely meets it. Surplus never adds esteem; it delays the shortfall. With nobody opposite, esteem is `-_short(him)`, which is never positive: alone
  before a room, a man can only fall short. Inside a proceeding the standard is never an obstacle (`rosters.yaml:1845`). The
  single roll's flat `standard` term reads no Grace (`sigma.py:712-720`), and no act that proceeds reaches it (B24p.19).
  This design keeps that split, by precedent (B24p.13's docstring at `:716-718`): Grace meets a venue's standard where the
  venue is played.
- **The band.** Per sitting, a speaker's esteem lies in `[-(S + show·R - 1), +(S' + show·R' - 1)]` levels times
  `esteem_step`, where S and R are the standard and his rattles, and S' and R' the opposite's. `esteem_step` ships 0.2
  (`data/fixtures.py:1450`, `H-866`, swept 0.0 / 0.1 / 0.2) and `show` ships 1.0 (`:1453`, `H-867`).
- **The reading rule that chooses the coefficient.** `esteem_step` is the largest value in its sweep that keeps both
  orderings: **(i)** B24p.18's Grace role holds, so Grace 7 against 1 carries more at standard 5
  (`engine/season/tests/test_sc_roles.py:322-333`), which bounds it above 0; **(ii)** §6's profile pair holds at the most
  Grace-demanding venue in the tree (`hard` under `theocracy`, standard 8). If (ii) fails at 0.2, the shipped value is too
  large for AR-50 and the rule picks the next point down. The same rule bounds `decorum_gain` (§1). `decorum` is read off the
  same `esteem`, so one shortfall prices both the contest and the regard: one quantity on one ladder (NERS S, *"calculations
  consistent in methodology"*).
- **Carried, as the entry instructs:** `[ASSUMPTION; medium; Jordan to correct; revert: the shortfall lowers `reception`
  only]`. As built, the shortfall moves the leverage, not `reception`. The revert would route it into the single roll's
  `reception` operand (`sigma.py:607-612`) and take it off the leverage. That would be a declared mover of every act that
  proceeds.

**Falsifier.** In the hand-built trial of `test_sc_roles.py:_trial` (standard 5), against an opponent of Grace 7 (short 0 at
every standard up to 7, so only the speaker's own shortfall varies), a speaker of Grace 5 and one of Grace 7 have equal
`esteem` from a fresh sitting (zero rattles; `_beats` starts fresh, `test_sc_roles.py:189-192`), so surplus adds nothing
there. A speaker of Grace 3 has esteem lower by `2` (the shortfall), times `esteem_step` on the leverage. Raising the row's
`standard` by one level lowers the Grace-3 speaker's esteem by one and leaves the Grace-7 speaker's unchanged until the
standard passes 7. **The rattled case** (`_state(inp, a=Cond(rattles=1))`, the speaker rattled once) shows what the surplus
does. The Grace-5 speaker is now short 1 and his esteem falls by 1. The Grace-7 speaker is still short 0 and his esteem is
unchanged. So the two are no longer equal, and the difference is the rattle the surplus absorbed.

**Control.** `esteem_step` 0.0: the margins are equal key by key (`test_sc_roles.py:331-332`, which already runs this arm).
Every row at `standard: plain` under `crown` puts the standard at 4. Nothing here changes the hash, since no build is
scheduled for (3).

---

## 4. Presence on obedience

**Verdict: the issuing half is built. The receiver-side term is answered by the ladder (steps 3 and 4). It is built at
control 0 and ships dark, with the switch left to its own swept hole-register row. It is not a Jordan row.**

**What the tree already does with an issuer's Presence.**
- `issue` is drawn on Presence (`verb_table.yaml:835`, `governing: [attr.social.charisma]` `:840`). It is contested `a
  standing` (`:843`) and OPPOSED BY THE EXECUTOR, his skill plus his Will, with his stance toward the issuer as the `regard`
  obstacle (`contests_note`, `:844`). A commanding issuer binds the man he orders more often, and the man's Will is what
  resists. That is Presence on obedience at the moment of command, read where the true value may be read (the World-side
  draw).
- Inside a room, the deciders' Presence cows a participant (`awe`, `proceeding.py:349-358`; the role test
  `test_sc_roles.py:490`). That is AR-50's *"commanding people"* within the proceeding.

**Why none of the existing terms carries it, so the term is new.** `comply` and `evade / defy` are formed on the writ, a
`Record` (`verb_table.yaml:217-231`, `:552-562`). Each existing term fails for its own reason:
- `stance` reads regard toward the writ under `declared`. Under `beneficiary` it reads the beneficiary, and `comply` declares
  `none` with the note *"the writ's issuer is its maker, not an operand of the act that answers it"* (`verb_table.yaml:225`).
  A `maker` carrier there would route the issuer through **regard**. Regard is not Presence-free: decorum's esteem carries
  the opponent's pressing (§1.2). But regard is what makes a man *liked*, and AR-49's commanding man is *"not likeable doing
  it"*. A regard route would make command lovable and blur §6's pair, so the term reads its own reading, not regard.
- `fit` is the seating shape only (`choose.py:292`).
- `aim` is a goal's lean.
- `risk` is a bodily cost.
- `pursuit` is the person's own axes (`liberty` favours `evade / defy`, `stability` favours `comply`,
  `rosters.yaml:5025-5026`).

**Nothing caps the chooser at five terms.** `score_terms` returns a tuple (`choose.py:453`); no rule fixes its length. Of
`IS-B2-CHAR-02` (`master/instructions/IS_B2_SC_FI_CORE_CHAR_part2.md:133`), only step (2) (`:135`) speaks to terms. That step
constrains the in-contest DECIDER, `make_decider`, which `decision/decider.py:5-6` reads as *"it adds no term the chooser
does not have"*. It does not constrain `score_terms`. (The instruction suite is part of the plan v12 adopted by merge, so it
is ratified: CLAUDE.md §2, ED-1094. The ruling rests on step (2)'s text, not on its status.)

**The ladder.**
1. **Superseded:** no later ruling decides it.
2. **Irrelevant:** no; `comply` and `issue` are live.
3. **Answered by a design document:** yes. The item's own text, *"a term on the receiver's `comply` against `defy`/`evade`
   from the issuer's Presence, as seen by the receiver"* (`workplans/valoria_master_workplan_v12_part22_cont.md:213`, (4)),
   stands with nothing opposing it.
4. **Answered by precedent:** the shape. `fit_term` already scores another person's attribute as the chooser holds it,
   `believed_capability(p, to, ...)` (`choose.py:296`), from the chooser's own ledger. The new term is that shape.

What looked like the other option, *"no receiver term"*, is this term at `obey_gain` 0. That is its hash-equal control, not
a rival design. Whether the switch ships is a swept setting with its own row, as `confer_fit_weight` is `H-414`'s (§2).

**The build (built at control 0, shipped dark).**
- **The reading of Presence (WITNESS).** A `sitting_claims` kind **`command`**, deposited by §1's door with §1's rules. Its
  subject is `b.voice`. The true sign is `+1` where the voice's mean `Beat.heard` exceeds the mean of the voices opposite
  and `-1` where it falls below; there is no claim on a tie, and none for an unopposed voice. Each holder holds it as he
  reads it, through `bench_reading` with the key `command_read:<voice>`. It is gated by `obey_gain`. `Beat.heard` is the
  Presence operand (`proceeding.py:361-373`), written on the ending like `esteem`.
  - *Glossed (new word, plain sense):* **command**, *was heard over the man opposite, as the room saw it*.
- **The reader (`person_q`).** `believed_command(p, issuer)`, the sum of the values of `p`'s chainless `sitting:command`
  claims of `issuer`, weighted as §1.2 weights decorum. It is shaped like `believed_capability`, reading `p`'s ledger alone.
- **The issuer, person-side.** The writ's maker is read off the receiver's own content claim of the writ. `[ASSUMPTION;
  medium; Jordan to correct — basis: `comply` is formed only where a claim of the dispensation's terms is in the actor's own
  ledger (`verb_table.yaml:229`); the build confirms that claim names the maker, and where it names none the term is 0;
  revert: the term reads 0]`.
- **The term (`decision/choose.py`).** A sixth `score_terms` term, **`obey`**: `obey_gain · row.obedience ·
  believed_command(p, maker)`. `obedience` is a new verb-table cell (`+1` on `comply`, `-1` on `evade / defy`, default 0).
  It is read off the row and never a verb name. At `obey_gain` 0 it returns 0.0 and reads no ledger, as `fit_term` does at
  `:288-289`. **Build site:** `score_terms`' tuple grows to six, so every reader that unpacks it moves in the same commit.
- **The row.** `Fixtures.obey_gain` with a `hole_register.yaml` row: swept 0.0 (control, SHIPPED) / 0.5 / 1.0. `[ASSUMPTION:
  the sweep points copy `H-414`'s; Jordan to correct]`.

**The game it makes, once switched on.** A commanding lord's writs bind more often (the `issue` draw), and a man who has
seen him command is slower to defy what he holds. Defiance concentrates on issuers the receiver has seen out-talked.

**Falsifier.**
- **The built half.** Hand-built `issue` draws: an issuer of Presence 7 against one of 1, same executor, same keys. The
  higher-Presence issue reaches Success or better strictly more often (the governing score feeds the pool).
- **The new term.** With `obey_gain` > 0, a receiver holds `sitting:command` `+1` of issuer A and `-1` of issuer B and holds
  a writ from each. Then `obey(comply on A's writ) - obey(comply on B's writ) == 2 · obey_gain` exactly, and the
  `evade / defy` terms differ by the negative of that. His regard of A and B is unmoved by the `command` claims.

**Control.** `obey_gain` 0.0: no `command` deposit and no `command_read` draw, `obey == 0.0` on every candidate, and the base
hash holds. Like §1's control, it must assert at least one opposed sitting with unequal mean `heard` in the hash seeds.

---

## 5. Attunement on bonds

**Verdict: the formation term already exists, and it is the row's governing attribute. The knot oracle's Bonds gate is
re-pointed to Attunement at its owner and re-exported. No new term.**

- **The formation term IN-32's effect consumes.** `tie / knot` is drawn on Attunement (`verb_table.yaml:2289`, `governing:
  [attr.social.attunement]`, B05.25). That is AR-31's *"attunement influences the likelihood of forming knots/bonds"*,
  already in the row. The draw's band is what the effect consumes. `_eff_tie` was built at IN-32 and reverted for want of a
  reader (`hole_register.yaml` `H-182`; `tie / knot` is the one row `resolvable_verbs()` excludes,
  `engine/season/tests/test_season_shape.py:817`). When it re-lands on `H-182`'s own trigger, it reads the band by the
  oracle's tier mapping (`systems/fieldwork/sim/knots.py:229-237`): Overwhelming opens the `knot` (Close), Success the `tie`
  (Distant), and Partial or Failure nothing. This design adds nothing to that trigger and builds no effect.
- **The oracle's Bonds gate, re-pointed.** The oracle gates on the retired attribute: `bonds_a = getattr(actor_a_obj,
  'bonds', 0)`, refused below `KNOT_BONDS_MIN` 5, with capacity `(bonds_a // 2) + 1` (`knots.py:50-53`, `:190-191`,
  `:205-206`). CR-84 dropped Bonds from the ten (`references/descriptor_registry.yaml:310`; `test_cr20_attributes.py:212`
  refuses `bonds`), so an actor built from the ten reads 0 there. *Not run here; the build's falsifier runs it.* The
  re-point is made at the owner (`CLAUDE.md` §6: a port never corrects its oracle; the oracle changes where it lives): the
  gate reads the actor's Attunement (`attr.social.attunement`, the ten's key), with `KNOT_BONDS_MIN` renamed
  `KNOT_ATTUNEMENT_MIN` at 5 on the 1-7 scale (one point above the midpoint, which keeps the old threshold's number).
  Capacity becomes `(attunement // 2) + 1`. It is then re-exported with the repo's tooling: `python
  tools/export_sim_params.py --build`, which rewrites the `fieldwork.KNOT_BONDS_MIN` row
  (`engine/engine_params/sim_params.json:2558`), and `--check` for the round-trip. Nothing is hand-edited downstream.
  `[ASSUMPTION; medium; Jordan to correct — basis: the threshold's number is kept on the new scale; revert: the gate at the
  midpoint, 4]`.
- **The pool, named and answered by the ladder.** The oracle rolls `spirit * 2` (`knots.py:219-220`) while the season row
  governs on Attunement. That is two live readings of one draw, a NERS S defect. `CLAUDE.md` §0.05 cl.3 decides it: when two
  surfaces disagree, `engine/season/` decides which reading wins, and the row's Attunement wins (AR-31 names Attunement for
  knot formation; AR-44's Spirit names no bond). The oracle's pool is re-pointed in the same build to `attunement * 2`.
  **The `× 2` stays.** The oracle's pool lives on its own scale (TN 7, Ob 2, `knots.py:59-60`), not on the season's one
  pool rule, so dropping the doubling would also change formation rates at equal values. `[ASSUMPTION; medium; Jordan to
  correct; revert: the gate only, the pool left at `spirit * 2`]`.
- **The contract row moves with it.** `references/module_contracts.yaml:352` still declares `Bonds` a writable track of the
  oracle's unplugged state. The gate now reads the Attunement attribute, which the oracle never writes, so the build
  deletes that row in the same commit. It does not rename it to a writable Attunement track. Knot capacity is derived from
  the attribute, not kept as state.
- **AR-30, Attunement on reading others, is already built** and is not this item's: `accuracy`
  (`proceeding.py:790-793`) is his Attunement alone. It drives the frame (`test_sc_roles.py:281`) and the reading of the
  bench (`sitting_claims: leans`, `rosters.yaml:1014-1019`). That is ED-IN-0350's *"informs how character thinks the other
  character is receiving it"*.

**Falsifier.** With the oracle alone, no season: an actor whose ten attributes put Attunement at 6, with no `bonds` field and
the other prerequisites met, forms a knot on some seeded keys after the re-point. The same actor forms none on any key before
it (the dead gate). At Attunement 4 the gate refuses on every key. `export_sim_params.py --check` is green after `--build` and
red if the row is hand-edited.

**Control.** The oracle is UNPLUGGED (`references/module_contracts.yaml:347`), not reachable from the season loop. The
re-point therefore moves no season hash **by construction**, and a season run is NOT a control for it (`CLAUDE.md` §7: a
season-unreachable change makes both arms identical). The control is the oracle's own: at an actor's Attunement equal to the
old `bonds` value, gate and capacity decide as before.

---

## 6. The two profiles, the falsifier pair (AR-49, AR-50)

**Verdict: the room half is built (B24p.18's role tests). The regard half is §1. The pair is the falsifier of both, and it
bounds the coefficients (§3).**

- **Built for the room.** Presence moves `heard` and its share of the dice and carries more
  (`test_sc_roles.py:301-319`). Grace moves `esteem` and carries more (`:322-333`). Each is tested alone, one attribute at a
  time. No test sets the two profiles against each other.
- **The pair, head to head.** Profile **P** has Presence 7 and Grace 1 (AR-49; Attunement 1 as ruled). Profile **G** has
  Grace 7 and Presence 1 (AR-50). Every other attribute is at the midpoint. They are opposite each other in a hand-built
  sitting of the shipped column, at a venue asking Grace 5 (a trial) and at the most demanding venue (standard 8). Then:
  1. **P wins the contest:** P's speeches carry (Success or better on the one ladder) strictly more often than G's, beyond
     two standard errors of the paired difference (B24p.18's own statistic, `test_sc_roles.py:147-153`).
  2. **P loses regard and G wins it:** with `decorum_gain` > 0, the true decorum signs are `-1` for P and `+1` for G (P is
     short at standard 5 and G is not). A bystander of Attunement 7, on keys where he reads both truly, has
     `regard(bystander, G) > regard(bystander, P)`. Over all keys his mean regard of G exceeds his mean regard of P.

  If (1) fails, Grace's leverage outweighs Presence and AR-50's *"struggle ... getting their desired outcomes"* is broken:
  `esteem_step` is too large, and §3's reading rule lowers it. If (2) fails, §1's door does not carry Grace to regard.
- **Attunement's part of AR-49** (*"unaware of their impact on others"*) is the low-Attunement man's reading of the room
  (`accuracy`). It is built and is not part of the pair's assertion.

**Control.** `esteem_step` 0.0 and `decorum_gain` 0.0: (1) still holds on Presence alone, and (2) reads equal regard
(`decorum` is 0 for both). The base hash holds.

---

## 7. What this schedules

| item | build | mover | control |
|---|---|---|---|
| (1) | `sitting_claims: decorum`, written by `_sitting_claims` per voice through `bench_reading` (key stem a parameter); `regard_parts` addend `decorum` (chainless claims only), `regard`'s unpack, the chronicle's dict; `Fixtures.decorum_gain` + hole row | yes, above 0; the chronicle's dict gains a key even at 0 | `decorum_gain` 0.0 |
| (2) | none (reads `fit_term` as it stands) | live only when `H-414` leaves 0.0 | `confer_fit_weight` 0.0 |
| (3) | none (built B24p.07/B24p.13); the reading rule is `H-866`'s sweep | — | `esteem_step` 0.0 |
| (4) | `sitting_claims: command`; `believed_command`; `score_terms` term `obey` and the verb-table cell `obedience`; `Fixtures.obey_gain` + hole row | yes, above 0 (ships 0) | `obey_gain` 0.0 |
| (5) | `systems/fieldwork/sim/knots.py` gate and pool (`attunement * 2`) re-pointed; `module_contracts.yaml:352` row deleted; `export_sim_params.py --build` | no season hash (unplugged) | the oracle's own |
| (6) | the head-to-head test, beside B24p.18's roles | — | both steps 0.0 |

- **Nothing is escalated.**
- **Answered by the ladder, recorded where taken:**
  - §1's door: step 5, CR-79's precedent, with the carrier already on the log; the per-holder reading by step 4, B24.29's
    `leans`;
  - §4's term: step 3 (the item's own text) and step 4 (`fit_term`'s `believed_capability` shape), shipped dark at its
    control;
  - §1's separate addend: step 4, CR-31's `heritage`;
  - §2's route: step 3, the code as it stands;
  - §3: steps 1 and 4, built at B24p.07/B24p.13 and B24p.19's split;
  - §5's pool: step 1, `CLAUDE.md` §0.05 cl.3.
- **Glossary.** Two coinages: *decorum* (§1.2) and *command* (§4). It goes to `unified/U1_GLOSSARY.md` when the build lands it (the entry's
  GLOSSARY line).

