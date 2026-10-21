# Verb key rows — part 2: §3.0-§3.1.9, the key rows (continued in `_part3`)
## Status: PROPOSED (2026-10-21). Not ratified; merging ratifies nothing unless Jordan so rules. Static reading. No season, probe or test ran. One import of three loaders (running their import-time checks on the shipped tables) listed three rosters. No proposed row was loaded; every claim that a skeleton loads is unverified.
## Parts, in reading order: [head](2026-10-21-verb-key-rows.md) (§1 head, §2 disposition table) · **this file** (§3.0-§3.1.9 key rows) · [`_part3`](2026-10-21-verb-key-rows_part3.md) (§3.1.10-§3.2 key rows, §4 why no per-row value fan, §5 host rows, §6 cost and ordering, §7 open items).

Citation shorthands are the head's (§1, opening paragraph); K-1..K-10 and F-1..F-6 are the head's §1.2.

---

## 3. Key rows

### 3.0 The rules every skeleton below follows

- **Shared body** (`accept`'s shape): the key's writes are the host's, so the host's decorated function
  gets one more `@effect_for("<key>")`. Only `accept` uses it, on `_eff_kill`, which opens no Tenure, so
  F-4's walker limit is not engaged.
- **Composed body** (`_mint_sheet`'s shape: `survey` and `forge` each have a decorated body that calls
  the one mint, `loop/effects_information.py:592`, `:636-670`; and `_relocate`, shared by `move`,
  `migrate` and `march`, VT:695-720): the key gets its own thin `_eff_<key>` that calls the host's
  single-owner helper. The opener walker follows a decorated function into its helpers (DV:457-465), so
  a composed key that reaches a Tenure-opening helper is recorded as that kind's opener in its own name
  and the host keeps its own entry. Every key on an opening host below composes. No body branches on
  `a.verb`: `loop/`, `decision/`, `queries/`, `seam/` and `data/` hold no verb-name equality test today
  (searched: `verb ==`, `.verb in`). Where one helper needs a per-key value (a sign, a mood), the value is
  a roster keyed by `verb_table`, the `graded_inquiries` shape (RO:1104-1130, `keys: [verb_table]`),
  read by `<ROSTER>.get(a.verb)` as `sigma.py:103` reads `VERB_CAPABILITY`.
- **Kinds** (F-2, F-3): every key emits a success kind of its own; a key that passes on what it holds
  (`confide`, `threaten`) also emits `news.told` first on its telling bands. A key that writes another
  party carries all-`null` cells or numeric `deed:<own kind>: 0.0` cells on each non-null axis (F-2).
- **Covert keys** (`assassinate`, `flatter`, §3.2) rest on the tree's one covert mechanism, `forge`'s:
  the key's own kind is a member of `covert_kinds` (RO:2283-2296; today one member, `record.forged`), a
  member must be a deed kind (DV:1297-1310, `_check_covert_kinds`), and an inquiry finds its trail
  through `epistemic.trail_of` (`epistemic.py:358`, iterating `COVERT_KINDS` at :384). What the cover
  hides at the act is the doer, not the kind.
- **Refusals** (K-3): a row whose typed cell names its conjuncts keys `emits_on_refusal` by exactly its
  failable clauses (the named conjuncts, `eligibility` if any alternative is not `own`, `write` if it
  writes, `counterparty` if it declares one), and a contested row uses one kind under every key
  (DV:905-943).
- **Grades**: every skeleton is `grade: "assumption"`, the grade `found`, `survey` and `forge` carry for
  an argued addition (VT:397, :1010, :357). `grade:` is not validated at load (VT:1154-1156 block
  comment); the `[ASSUMPTION; …]` tag is where the revert lives.
- **Alignment**: seven cells, each a number or `null`, with a one-line basis in the draft's method
  (`carried`/`derived`/`reasoned`, RO:2774-2778 note). `selfish_selfless` is `null` for every key
  (RO:2779-2783). A verb whose seven cells are all `null` is not in `celled_verbs()` (DV:1456-1466), so
  `corpus_run`'s RANKING, the instrument of R-06 and R-08 (`requirements.yaml:1194`, `:1312`), does not
  see it.
- **Creed**: K-7 makes the cell optional. A key gets one only where the host or a sibling has one for
  the same reason; otherwise none.
- **"Would be observed by"** names the test or instrument that would see the key work. Each named test
  is unbuilt; where a requirement's own `measure:` line would see it, the line is cited.

---

### 3.1 The twelve keys

#### 3.1.1 `accept` — KEY on `fight` (shipped; one amendment)

The row stands (VT:628-656). One change, from F-2 and the upload's own line ("a duel Event so witnesses
tell it from assault", U:22):

```yaml
    emits:
      Felled:      ["person.died", "duel.fought"]
      Wounded:     ["body.changed", "duel.fought"]
      Untouched:   ["contest.undecided", "duel.fought"]
```

and, in `rosters.yaml: alignment`, `"deed:duel.fought": 0.0` on `rigid_flexible`, `grandiose_humble`
and `deontological_instrumental`, the three axes `accept` has cells on.

- **Effect**: `_eff_kill`, unchanged. It names no `earns` on its one Subject
  (`loop/effects_combat.py:177`), so the fold emits every kind of the band (`loop/resolve.py:524-525`).
- **Why the zero cells**: `accept` writes the CHALLENGER's body. `duel.fought` is emitted by one row, so
  under `claim_subject_rule: both` a witness's claim of it on the challenger would judge the challenger
  as the doer of accepting (F-2). The killing itself stays judged through the paired `person.died` and
  its `deed:` cells (RO:3061-3062, :3123-3124). What `duel.fought` adds is the separation of consent from
  assault in what witnesses hold; it adds no valuation.
- **Alignment, creed, capability**: unchanged (RO:2855, :2902, :2950, :2999, :3009, :3056, :3121; no
  creed cell; no `verb_capability` row).
- **Grade**: `[ASSUMPTION; medium; Jordan to correct; revert: the three single-kind bands and the three
  `deed:` cells]`.
- **Falsifier**: a seeded run in which an `accept` executes leaves every co-present witness holding a
  `duel.fought` claim, and a `fight` leaves none; `test_we_a_contested_acts_consequence_differs_by_degree`
  (VT:571) still passes, since no band's writes move.
- **Would be observed by**: a witness-deposit test of the above, unbuilt. R-07's `measure:`
  (`requirements.yaml:1258`, `-k 'choose_receives_no_world or a_view or r7_two_persons'`) does not
  select it.

#### 3.1.2 `hire_troops` — KEY on `levy`* (recruit-for-coin; composed body)

```yaml
  - verb:        "hire_troops"
    stratum:     "uncontested_material"
    eligibility: ["remit:issue"]
    beneficiary: "none"
    requires:    "the seat's treasury covers the wage, and the subject is a rung in the seat's purview"
    requires_typed:
      all:
        - form:      basis
          of:        subject
          basis:     purview
          conjunct:  authority
        - form:      scalar_threshold
          of:        from
          scalar:    stores
          key:       kind
          threshold: amount
          comparator: ">="
          conjunct:  wage
    writes:      ["Rung.stores"]
    emits:       ["troops.hired"]
    emits_on_refusal:
      eligibility: ["hire_troops.unauthorized"]
      authority:   ["hire_troops.unauthorized"]
      wage:        ["hire_troops.refused"]
      write:       ["hire_troops.refused"]
    grade:       "assumption"
    source:      "this proposal §3.1.2; U:44 (recruit-for-coin); `_part10:108` (a sibling row)"
```

- **Effect**: composed. `_eff_hire_troops` calls the recruit-to-raw mover `levy`'s own body will own
  (unbuilt) and `_eff_transfer`'s conserving move of `coin` from the treasury
  (`loop/effects_economy.py:168`). It writes no cohort stance row, which is the whole of the difference
  from `levy`.
- **`writes` / matrix**: `(Rung, stores)` only, already `[MAT, RES]` and produced; no new matrix row. The
  `wage` conjunct is `transfer`'s cell verbatim (VT:1301-1307: `stores(from, kind) >= amount`), with
  `kind` bound to `coin` [ASSUMPTION: the wage is paid in `coin`; basis: `_part16:456`, `buy` "giving
  `coin`"].
- **Alignment**: `hierarchical_equal: null` (reasoned: a paid contract, not rank exercised, unlike
  `requisition`'s −0.6); `precedent_substantive: null`; `partisan_equitable: -0.2` (reasoned: `march`'s
  −0.4 halved: a force raised for one's own side, before any field); `selfish_selfless: null`;
  `rigid_flexible: null`; `grandiose_humble: null`; `deontological_instrumental: 0.6` (carried from
  `transfer`/`exchange`, RO:3110-3111). The act writes two rungs' stores, so `"deed:troops.hired": 0.0` on
  `partisan_equitable` and `deontological_instrumental` (F-2).
- **Creed**: none. **Capability**: none (uncontested).
- **Chooser**: `referent_class: Rung` and the seat's treasury as `from` (`treasury_of`, OP:621),
  `requisition`'s formation (VT:657-693). `amount` [UNVERIFIED: which source `_derive_operand` would use
  for a wage; `transfer`'s derivation was not traced]. No fan: one bag (OP:1065-1068).
- **Grade**: `[ASSUMPTION; medium; Jordan to correct; revert: a terms operand on `levy` if Jordan rules
  the coin a cost inside one effect]`. The name is plain English for the act; `recruit` is FA's row for
  persons and `hire` EC's for one person's service.
- **Falsifier**: on a hand-built world, a seat with a hostile cohort and a full treasury hires: the
  cohort's stance rows are unchanged and the treasury's `coin` falls by the wage; with an empty treasury
  the act refuses `hire_troops.refused` keyed `wage`. Identical world diffs for `hire_troops` and `levy`
  falsify the key.
- **Would be observed by**: R-04's `measure:` per-verb lines (`python -m engine.season.harness.aperture
  4 0`, `requirements.yaml:817`), once `levy` exists; and the unit test above, unbuilt.

#### 3.1.3 `sack` — KEY on `pillage`* (composed body)

```yaml
  - verb:        "sack"
    stratum:     "uncontested_material"
    eligibility: ["remit:dispatch"]
    beneficiary: "actor"
    requires:    "the commander's force stands at the place it marched on"
    requires_typed:
      all:
        - form:      relation
          of:        subject
          relation:  present_at
          conjunct:  present
    writes:      ["Rung.stores"]
    emits:       ["place.sacked"]
    emits_on_refusal:
      eligibility: ["sack.refused"]
      present:     ["sack.refused"]
      write:       ["sack.refused"]
    grade:       "assumption"
    source:      "this proposal §3.1.3; U:62 (sack into pillage), U:69 (surrender bars sack); `_part10:286` (own event kind)"
```

- **The occupation test**: presence. A `march` that wins or is unopposed relocates the army onto the
  Rung, opening each mover's `contain` there (`Won`/`Unopposed` write `Tenure.since` and
  `Person.travel_leg` through `_relocate`, VT:709, :711); it writes no `hold`, so a `held_by` conjunct
  would refuse every sack after a storm. `remit:dispatch` (`march`'s own eligibility, VT:699) restricts
  the act to a commander. [ASSUMPTION: "occupied" is "the commander stands there after the march"; a
  commander who merely travelled there passes too. Revert: add `seize` of the Rung as a precondition,
  `seize`'s `rung.seized` being the title change.]
- **The surrender bar**: `surrender`* is to write a term on the place that `sack` reads (U:69). No typed
  form reads such a term today; the bar lands as a second named conjunct with `surrender`, not before.
- **Effect**: composed. `_eff_sack` calls `pillage`'s stripping helper with every kind and the whole
  stock, where `pillage` takes a share.
- **Alignment**: `hierarchical_equal: null`; `precedent_substantive: null`; `partisan_equitable: -0.6`
  (reasoned: `march`'s −0.4, stronger: the losers are residents); `selfish_selfless: null`;
  `rigid_flexible: null`; `grandiose_humble: -0.4` (carried from `march`, RO:3065);
  `deontological_instrumental: 0.7` (reasoned: between `march`'s 0.4 and `forge`'s 0.8). The act writes
  the residents' Rung, so `"deed:place.sacked": 0.0` on those three axes (F-2): otherwise the sacked
  place would be judged as the doer.
- **Creed**: none. **Capability**: none.
- **Chooser**: `opening_set` iterates the question's referents (`for subject in refs`, OP:164), not the
  rung the actor stands at; `containing_rung_of` (OP:559) supplies `transfer`'s giver, never a subject.
  So a `sack` forms only if some question source raises the occupied Rung as a referent for the
  commander [UNVERIFIED: no such source was found; if none exists, the row forms for nobody and is
  `ID-13`'s dead carrier until one does, a build precondition]. No fan.
- **Grade**: `[ASSUMPTION; medium; Jordan to correct; revert: `sack` as a content of `pillage` (every
  kind, all), the research's FOLD, `_part10:286`]`.
- **Falsifier**: after a `march` `Won` onto a Rung, the commander's `sack` executes and every larder kind
  there reads zero; a commander whose `march` was `Lost` (no arrival) is refused keyed `present`;
  witnesses of a sack hold `place.sacked`, of a pillage `stores.pillaged`.
- **Would be observed by**: R-04's per-verb lines (`requirements.yaml:817`), once `pillage` exists; the
  unit test above, unbuilt.

#### 3.1.4 `confide` — KEY on `tell` (shared contest; no body, as `tell` has none)

```yaml
  - verb:        "confide"
    stratum:     "social"
    eligibility: ["own"]
    beneficiary: "subject"
    requires:    "the teller holds a claim on the subject, and the person told is with the teller"
    requires_typed:
      all:
        - form:      own_ledger
          of:        subject
          conjunct:  holds
        - form:      relation
          of:        to
          relation:  with
          conjunct:  hearer
    counterparty: to
    contests:    "a standing"
    writes:
      Overwhelming: []
      Success:      []
      Partial:      []
      Failure:      []
    emits:
      Overwhelming: ["news.told", "confidence.given", "confidence.broken"]
      Success:      ["news.told", "confidence.given", "confidence.broken"]
      Partial:      ["news.told", "confidence.given", "confidence.broken"]
      Failure:      ["news.untold"]
    emits_on_refusal:
      holds:        ["confide.refused"]
      hearer:       ["confide.refused"]
      counterparty: ["confide.refused"]
    grade:       "assumption"
    source:      "this proposal §3.1.4; U:79; `tell`'s row (VT:1013-1092) for every column but the kinds"
```

- **Effect**: none, as for `tell` (`writes: []` at every band; the deposit is WITNESS's, WI:822-860).
- **The reader that makes it a key**: `_circle_of` (WI:108-133) returns a circle only on a draw at
  `telling_privacy`, and returns `None` before any other test at rate 0 (WI:125-126). The change: a
  roster `confided_tellings` in `rosters.yaml` (`keys: [verb_table]`, `values: [confide]`), read by
  `_circle_of` before the rate test, so a `confide` always circles `(teller, addressee)` and a `tell`
  keeps the draw.
- **`said`**: carried, because `holds` is a NAMED `own_ledger` conjunct (OP:146-147).
- **Alignment**: all seven `null`, for two reasons. `tell`'s own `uncelled:` reason holds for a
  confidence (RO:2744-2748: "testimony's moral weight is in WHAT is told … telling is driven by regard …
  not by pursuit"); and any cell (a `grandiose_humble` lean for privacy is the obvious one) would be
  turned against the topic by F-2: a telling writes nothing, so its claim lands on what was told
  (VT:1067-1068, the empty-changes fallback), and the topic would be judged as the confider.
- **Creed**: none (R-C4.3, content-keyed, RO:2445-2450).
- **Capability**: `verb_capability: confide: "copying"`, `tell`'s key (RO:1181), because the roll is the
  same roll.
- **Chooser**: `tell`'s exactly: the `to` fan over known persons (RO:1905), one bag per person
  (OP:1065-1101).
- **Grade**: `[ASSUMPTION; medium; Jordan to correct; revert: confidences stay a fixture draw (H-197)]`.
- **Falsifier**: at `telling_privacy: 0`, the hearer's copy of a confided claim carries
  `Claim.visibility == (teller, hearer)` and a `tell` of the same claim carries `"own"`; the hearer's
  later `tell` of it to a third person emits `confidence.broken`.
- **Would be observed by**: that unit test, unbuilt. Not by R-07's `measure:` (`requirements.yaml:1258`).

#### 3.1.5 `praise` — a new row on `tell`'s prize (composed body)

```yaml
  - verb:        "praise"
    stratum:     "social"
    eligibility: ["own"]
    beneficiary: "subject"
    requires:    "the person praised is a living person and is with the actor"
    requires_typed:
      all:
        - form:      existence
          of:        subject
          kind:      Person
          conjunct:  party
        - form:      relation
          of:        subject
          relation:  with
          conjunct:  hearer
    counterparty: subject
    contests:    "a standing"
    writes:
      Overwhelming: ["Person.stance"]
      Success:      ["Person.stance"]
      Partial:      ["Person.stance"]
      Failure:      []
    emits:
      Overwhelming: ["praise.given"]
      Success:      ["praise.given"]
      Partial:      ["praise.given"]
      Failure:      ["praise.spurned"]
    emits_on_refusal:
      party:        ["praise.refused"]
      hearer:       ["praise.refused"]
      counterparty: ["praise.refused"]
      write:        ["praise.refused"]
    grade:       "assumption"
    source:      "this proposal §3.1.5; U:79; critique B3 (a hearer's stance toward the actor)"
```

- **What it shares with `tell`**: the prize (`a standing`), the roll path through `social_contest`, the
  `with` conjunct and the counterparty shape. It does not share the told deposit (no `holds`, so no
  `said`, OP:146-147, and no `news.told`). Praise of a third party to a hearer stays `tell`.
- **The precedent it has to answer**: `tell` attempted a `Person.stance` write and reverted it
  (VT:1059-1069), and `H-62`'s producer gap for `(Person, stance)` is closed by `march`
  (`hole_register.yaml:715-717`). The reversion's two premises were that the contest's opponent is `to`,
  not the topic, and that "what a telling leaves is a chain, not a write": a hearer credits a teller
  through the told claim's chain (`teller_weight`). Neither binds here: `praise` carries no told claim,
  so there is no chain for regard to be read off, and its opponent is the person praised, who is also
  the one whose regard moves.
- **Effect**: composed. `_eff_regard`, registered for `praise` and `insult`, appends one stance row
  `(actor, sign · 1.0, w)` to the subject's `Person.stance`, the row shape of PQ:67-77. The append is
  today inline in `_eff_march` (`loop/effects_combat.py:299-304`); it moves to one helper in
  `loop/effects_shared.py` that both call (CLAUDE.md §8). `sign` is read from a roster `regard_acts` in
  `rosters.yaml` (`keys: [verb_table]`, `values: {praise: 1, insult: -1}`); `w` is a fixture
  `regard_act_weight` with a `hole_register.yaml` row (invariant 11, §B.13).
- **The write gate**: `(Person, stance)` is `steps: [RES, ENC]`, `social: "true"` (WM:234-238), so the
  write must be at RES (`praise` resolves there) and by an act (`state/world.py:994-1000` refuses a
  social row whose `driver` is not `"Act"`). F3's ownership clause is for Tenures only
  (`state/gate.py:108-116`, "kind is Tenure => one of"). Nothing else in the gate asks whose stance it is.
- **Alignment**: all seven `null` (reasoned: the act's consequence is a regard the hearer holds, read by
  the stance term, not a lean of the act; `give`'s "one-to-one in presence … not a display", RO:3067).
  So `praise` is not in `celled_verbs()` and R-06/R-08's RANKING does not see it.
- **Creed**: none. **Capability**: none [ASSUMPTION: `tell`'s `copying` (RO:1181) does not fit a regard
  act; with no row `sigma.py:105-106` falls to `pool_default`; revert: `praise: "copying"`].
- **Chooser**: `subject` over the question's Person referents; one bag. With `counterparty: subject`,
  `subject_is_opponent` is False (OP:271-284), so under `stance_polarity: declared` a person praises whom
  they regard well (`decision/choose.py:54-89`). **Under the shipped `legacy` arm**
  (`data/fixtures.py:796`) the term is `stance_toward(p, subject)` on every row (`decision/choose.py:93-94`),
  so it does not separate praise from insult: both score higher on a liked subject. The build order
  (§6.4) is therefore after `H-194` ships `declared`.
- **Grade**: `[ASSUMPTION; medium; Jordan to correct; revert: praise stays a content of `tell`]`.
- **Falsifier**: after a `Success` praise, `stance_toward(subject, actor)` (PQ:67) is `w` higher; after
  `Failure` it is unchanged; under `declared`, a person who regards X well ranks `praise(X)` above
  `insult(X)`.
- **Would be observed by**: those unit tests, unbuilt. No requirement's `measure:` line sees it.

#### 3.1.6 `insult` — a new row on `tell`'s prize (`praise`'s body)

```yaml
  - verb:        "insult"
    stratum:     "social"
    eligibility: ["own"]
    beneficiary: "actor"
    requires:    "the person insulted is a living person and is with the actor"
    requires_typed:
      all:
        - form:      existence
          of:        subject
          kind:      Person
          conjunct:  party
        - form:      relation
          of:        subject
          relation:  with
          conjunct:  hearer
    contests:    "a standing"
    writes:
      Overwhelming: ["Person.stance"]
      Success:      ["Person.stance"]
      Partial:      ["Person.stance"]
      Failure:      []
    emits:
      Overwhelming: ["insult.given"]
      Success:      ["insult.given"]
      Partial:      ["insult.given"]
      Failure:      ["insult.shrugged"]
    emits_on_refusal:
      party:  ["insult.refused"]
      hearer: ["insult.refused"]
      write:  ["insult.refused"]
    grade:       "assumption"
    source:      "this proposal §3.1.6; U:79; critique B3"
```

- **The one column that differs from `praise`, and why**: no `counterparty:`. The row contests and names
  none, so `subject_is_opponent` is True (OP:271-284): the contest is thrown against the subject, the
  self-insult is declined, and under `declared` the regard term is negated, so a person insults whom
  they dislike. `beneficiary: actor` is `fight`'s and `challenge`'s reading for an act against the
  subject (VT:506, :610).
- **Effect**: `_eff_regard` (§3.1.5), sign −1. The gate, the `H-62` precedent and the `legacy` caveat
  are `praise`'s.
- **Alignment**: `grandiose_humble: -0.3` (carried reasoning from `fight`, RO:3053: "done before
  witnesses"); the other six `null`. The act writes the insulted person's stance, so
  `"deed:insult.given": 0.0` on `grandiose_humble` (F-2): otherwise every witness would judge the
  insulted as the grandiose doer. The −0.3 still moves the chooser.
- **Creed**: none. **Capability**: none.
- **Grade**: `[ASSUMPTION; medium; Jordan to correct; revert: insult stays a content of `tell`]`.
- **Falsifier**: after a `Success` insult, `stance_toward(subject, actor)` is `w` lower; under
  `declared`, a person with a grudge against X ranks `insult(X)` above `praise(X)`, and with regard for
  X the reverse.
- **Would be observed by**: those unit tests, unbuilt. `insult` is in `celled_verbs()` (one non-zero
  cell), so R-06/R-08's RANKING (`requirements.yaml:1194`, `:1312`) would count its Candidates.

#### 3.1.7 `audit` — KEY on `survey` (composed body; once the host row exists)

```yaml
  - verb:        "audit"
    stratum:     "uncontested_material"
    eligibility: ["remit:issue"]
    beneficiary: "actor"
    requires:    "the exercised seat's purview reaches the subject, and the auditor has heard of it"
    requires_typed:
      all:
        - form:      own_ledger
          of:        subject
          conjunct:  heard
        - form:      basis
          of:        subject
          basis:     purview
          conjunct:  authority
    writes:      ["Record.exists"]
    emits:       ["rung.audited"]
    emits_on_refusal:
      eligibility: ["audit.unauthorized"]
      authority:   ["audit.unauthorized"]
      heard:       ["audit.refused"]
      write:       ["audit.refused"]
    grade:       "assumption"
    source:      "this proposal §3.1.7; U:177; `survey` (VT:994-1012) and `seize`'s cell (VT:916-920)"
```

- **Effect**: composed. `_eff_audit` returns `_mint_sheet(w, a)`, `survey`'s one line
  (`loop/effects_information.py:592`), `forge`'s shape (`:636-670`, `_mint_sheet(w, a, forged=True)`).
  The walker follows the helper (DV:457-465), so `audit` is recorded as a `hold` opener in its own name.
- **Readers that make it a key**: `elig` and `cell` (the seat and its purview, `seize`'s shape and keys,
  VT:927-930); and **via**: `_ch_post_remit` admits a seat's obligees to the acts done through
  `Act.via` (`epistemic.py:554-558`). An audit is exercised through the seat that grants `issue`, so it
  carries `via` and its Event reaches that seat's establishment; a `survey` is `own` and carries none
  (VT:1007 `emits_note`: neither broadcast channel reads it).
- **Alignment**: `hierarchical_equal: -0.5` (carried reasoning from `dispatch`/`open_case`, RO:2821,
  :2822); `precedent_substantive: 0.3` (carried from `survey`, RO:2876); `deontological_instrumental: 0.3`
  (carried from `survey`, RO:3128); the other four `null`. It writes a Record the auditor holds and no
  other party's state, so no `deed:` cell is needed.
- **Creed**: none. **Capability**: none.
- **Chooser**: subject over Rung referents in purview, with the seat under `VIA` (DV:1117-1119);
  `referent_class: Rung` [ASSUMPTION: `requisition`'s formation; basis: VT:657-693].
- **Dependency**: `survey`'s place sheet (U:175). Without it `_mint_sheet` mints the FACTION sheet of the
  faction holding the Rung, which for a Rung in one's own purview is one's own faction. The key lands
  with the place sheet, not before.
- **Grade**: `[ASSUMPTION; medium; Jordan to correct; revert: audit is a survey (U:177)]`.
- **Falsifier**: a seat holder auditing a Rung outside his purview refuses keyed `authority`; an
  executed audit's Event is deposited for the seat's obligees, an executed survey's for none of them.
- **Would be observed by**: those unit tests, unbuilt; R-04's per-verb lines (`requirements.yaml:817`).

#### 3.1.8 `scout` — KEY on `survey` (composed body; once the host row exists)

```yaml
  - verb:        "scout"
    stratum:     "uncontested_material"
    eligibility: ["own"]
    beneficiary: "actor"
    requires:    "the place exists and the actor stands at it"
    requires_typed:
      all:
        - form:      existence
          of:        subject
          kind:      Rung
          conjunct:  place
        - form:      relation
          of:        subject
          relation:  present_at
          conjunct:  present
    writes:      ["Record.exists"]
    emits:       ["rung.scouted"]
    emits_on_refusal:
      place:       ["scout.refused"]
      present:     ["scout.refused"]
      write:       ["scout.refused"]
    grade:       "assumption"
    source:      "this proposal §3.1.8; U:177; `examine`'s cell (VT:1172-1180) on `survey`'s mint"
```

- **Eligibility**: `own` only. A `presence:<…>` alternative is cosmetic: the fold's presence branch always
  declines (its argument is a placeholder, `H-75`; `loop/resolve.py:138-152`), and `own` admits first
  (`:99-100`). The presence test is the `present` conjunct.
- **Effect**: composed, `_eff_scout` → `_mint_sheet`, as `audit`.
- **Reader that makes it a key**: `cell`. `survey` asks `own_ledger` (VT:999-1002); `scout` asks
  presence, `examine`'s two clauses with `Rung` for `Site`. A person can scout what he has never heard of
  and cannot survey it, and the reverse.
- **Alignment**: `survey`'s cells, carried (`precedent_substantive: 0.3`, `grandiose_humble: 0.2`,
  `deontological_instrumental: 0.3`; RO:2876, :3066, :3128); the other four `null`. It does not differ
  from `survey` in valuation and does not claim to.
- **Creed**: none. **Capability**: none.
- **Chooser**: subject over the question's Rung referents (OP:164); whether the rung the actor stands at
  is raised as one is `sack`'s open question [UNVERIFIED].
- **Dependency**: the place sheet, as `audit`; the forces mustered there (U:177) need a troop-stock field
  in the sheet [UNVERIFIED: none found in `record_kinds`].
- **Grade**: `[ASSUMPTION; medium; Jordan to correct; revert: scout is a survey]`.
- **Falsifier**: a person standing at a Rung he holds no claim on scouts it and executes, and surveys it
  and is refused; standing elsewhere he is refused keyed `present`.
- **Would be observed by**: those unit tests, unbuilt.

#### 3.1.9 `teach` — KEY on `train`* (shared body; no Tenure)

```yaml
  - verb:        "teach"
    stratum:     "uncontested_material"
    eligibility: ["own"]
    beneficiary: "subject"
    requires:    "the pupil is a living person and is with the teacher"
    requires_typed:
      all:
        - form:      existence
          of:        subject
          kind:      Person
          conjunct:  party
        - form:      relation
          of:        subject
          relation:  with
          conjunct:  hearer
    counterparty: subject
    writes:      ["Person.capability"]
    emits:       ["capability.taught"]
    emits_on_refusal:
      party:        ["teach.refused"]
      hearer:       ["teach.refused"]
      counterparty: ["teach.refused"]
      write:        ["teach.refused"]
    grade:       "assumption"
    source:      "this proposal §3.1.9; U:467; `_part18:137` (`subject` = a pupil)"
```

- **Effect**: `train`'s body, one more decorator; it opens no Tenure. [ASSUMPTION: the gain is bounded by
  the teacher's own `Person.capability` on the key taught — basis: the upload's "for self or a pupil"
  (U:465) and nothing else; revert: the same gain as self-study.]
- **Matrix**: `(Person, capability)` has NO row in `write_matrix.yaml`; it is `train`'s to add, with its
  producer, in `train`'s commit.
- **Reader that makes it a key**: `cell` and `counterparty` (a second side who must be present);
  `study` (#112) is `train` with `subject` the actor.
- **Alignment**: `precedent_substantive: -0.4` (carried reasoning from `reconstruct`/`succeed`,
  RO:2863, :2866: passing down what stands); the other six `null`. The act writes the pupil, so
  `"deed:capability.taught": 0.0` on `precedent_substantive` (F-2).
- **Creed**: none.
- **Chooser**: subject over Person referents; one bag.
- **Grade**: `[ASSUMPTION; medium; Jordan to correct; revert: teach is a `train` with a pupil subject]`.
- **Falsifier**: a teach with the pupil elsewhere is refused keyed `hearer`; an executed teach raises the
  pupil's capability and leaves the teacher's unchanged.
- **Would be observed by**: those unit tests, unbuilt. No requirement's `measure:` line sees a capability
  write; this proposal makes no R-06 claim for it.
