# Verbs, v2 — part 12: Part VI.4, fieldwork and inquiry (FI)

## Status: PROPOSED (2026-10-17). Reference, not canon (`CLAUDE.md` §0.05): nothing here binds the game or is read by it. Merging ratifies nothing unless Jordan so rules. Static reading and static lookup only; no run.
## Parts, in reading order: [head](2026-10-16-verbs-01-thesis-and-persons.md) (§0, Part I Persons) · [`verbs-02`](2026-10-16-verbs-02-attributes.md) (Part II Attributes) · [`verbs-03`](2026-10-16-verbs-03-standards-roster-and-reconciliation.md) and [`verbs-04`](2026-10-16-verbs-04-critics-etymology-gaps-and-decisions.md) (Part III Verbs: standards, roster, reconciliation; critics, etymology audit, gap coverage, named mechanics, decisions) · [`verbs-05`](2026-10-16-verbs-05-what-verbs-do-to-the-world-1.md) and [`verbs-06`](2026-10-16-verbs-06-what-verbs-do-to-the-world-2.md) (Part IV What verbs do to the world) · [`verbs-07`](2026-10-16-verbs-07-roadmap-reliability-and-sources.md) (§5 Roadmap, §6 Reliability ledger, §7 Sources) · [`verbs-08`](2026-10-16-verbs-08-engine-findings-from-the-first-trial.md) (Part V: engine findings carried from the first-pass trial) · Part VI, the lexicon by subsystem: [`verbs-09`](2026-10-16-verbs-09-lexicon-personal-combat.md) PC · [`verbs-10`](2026-10-16-verbs-10-lexicon-mass-battle.md) MB · [`verbs-11`](2026-10-16-verbs-11-lexicon-social-contest.md) SC · **this file** FI · [`verbs-13`](2026-10-16-verbs-13-lexicon-threadwork.md) TW · [`verbs-14`](2026-10-16-verbs-14-lexicon-settlements-and-governance.md) GV · [`verbs-15`](2026-10-16-verbs-15-lexicon-faction-actions.md) FA · [`verbs-16`](2026-10-16-verbs-16-lexicon-economy-trade-and-craft.md) EC · [`verbs-17`](2026-10-16-verbs-17-lexicon-world-travel-and-survival.md) WT · [`verbs-18`](2026-10-16-verbs-18-lexicon-npc-life-and-persons.md) NP · Part VII, the verb gap register (the evidence behind Part VI's coverage tables): [`verbs-19`](2026-10-16-verbs-19-gap-register-pc-and-np.md) PC+NP · [`verbs-20`](2026-10-16-verbs-20-gap-register-mb-and-fa.md) MB+FA · [`verbs-21`](2026-10-16-verbs-21-gap-register-sc-and-gv.md) SC+GV · [`verbs-22`](2026-10-16-verbs-22-gap-register-fi-and-tw.md) FI+TW · [`verbs-23`](2026-10-16-verbs-23-gap-register-ec-and-wt.md) EC+WT.

**How to cite this Part.** The lane's own sections are numbered 3.1 to 3.9; cite them as `FI §3.n` (for example `FI §3.9` for its items for Jordan). Gap ids (`FI-G01` …) resolve in Part VII (`verbs-22`). Abbreviations such as `VT`, `VCD`, `v2-p3` are defined in the lane's opening paragraphs; `v2-p3`, `v2-p4`, `v2-p8` are the first-pass v2 parts as filed at `716c253`. Old file names such as `…synthesis_part8.md` or `_part8` in the body also mean those first-pass files; the suite was later renamed `2026-10-16-verbs-NN-…`. Mechanic ids (`M1`, `M-1`, `M-WT-1`) are this lane's own.

**Rulings that override this section** (`verbs-03` §III.5; where this section and the roster disagree, the roster governs):

- R-07: `interrogate` is SC's.
- R-09: `explore` is WT's.
- R-10: `surveil` → `watch` is adopted in the rename batch.
- R-13: `thread_read` is TW's.
- R-14: FI owns `forge`, `create_record`, `destroy_record`.
- R-21 and R-22: `bribe` is FI's own row; `infiltrate` is FI's own row and must specify its own effect.

---

# FI — fieldwork and inquiry

Lane: FI. Inputs: gap register Part VII (`verbs-22`) rows FI-G01…FI-G58; critics
the lexicon critic (Part III §III.7) (L-nn) and the v2-claims critic (Part III §III.7) (V-nn); v2 `_part8.md` §V.2.10,
§V.2.14, §V.3 FI table (:445-457). Tree read 2026-10-16/17. Every `file:line` below was opened this
session unless it carries "(via register)", which means the register's reader opened it and I did
not. Etymology sources: **Wikt** = en.wiktionary through `etym_tool.py en|la`; **L&S** = Lewis &
Short through `etym_tool.py ls`. Anything else is `[UNVERIFIED]`.

Names used below for the rows as they stand: the **six inquiries** are `examine`, `interview`,
`research`, `surveil`, `thread_read`, `reconstruct` (`engine/season/verb_table.yaml:1132-1234`).
The **document makers** are `survey` (:966) and `forge` (:330).

---

## 3.1 Subsystem mechanic

**What the engine has.** Eight FI rows.
- **The six inquiries** all declare `writes: []`, emit `finding.made`, and refuse with `finding.none`.
  None declares `contests:` (verb_table.yaml:1132-1234). The finding producer is unbuilt: the block
  comment at :1100-1103 says *"the refusal half is shipped here; the producer is 4.5's"*.
- **`thread_read`** cannot be attempted. It is untyped (TS ≥ 30, H-85), so it is not in
  `resolvable_verbs()` (:1212).
- **`survey`** mints a `faction_sheet` Record into the surveyor's hold
  (`loop/effects_information.py:506 _eff_survey`). WITNESS's content deposit fires on a hold opened
  this tick (`loop/witness.py:397-421`), so the sheet's content lands in the surveyor's ledger.
  **It is the one FI act whose yield reaches a ledger today.**
- **`forge`** mints a false sheet with the forger as `head` (`_eff_forge`, :617) and emits
  `record.forged`. `Record.forgery_quality` is written by nothing and read by nothing
  (`hole_register.yaml` H-210 :4523).
- **Readers.** The one reader of a sheet is `rosters.yaml:1708` `record_sourced_operands`, and only
  `to: head` is consumed (H-169, via register).
- **Adjacent rows.** `destroy_record` (:210) forms for nobody (H-75; :210 note). `anchor_of` exists
  (`state/attribution.py:103`).
- **Not yet rows.** `conceal` is planned (IN-12 step 10, `workplans/valoria_master_workplan_v9_part5.md`
  IN-12 table). `interrogate` is planned (IN-12 step 5). `interrogation` exists as a proceedings
  arrangement (`engine/season/arrangements.yaml:204`).
- **Presence delivers what is said in a room**, confided tellings included: *"private whispers are
  not built"* (`witness.py` `_circle_of` docstring).
- **The scale is ungradeable.** `requirements.yaml:169-172` reads investigation `in_loop: false`.

**What it lacks.** Six things are missing:
1. a yield per inquiry;
2. Failure distinct from refusal;
3. a concealment grade read as the obstacle;
4. any reader of a forgery;
5. a reply to `interview`;
6. any act that writes a cover identity or an inducement.

---

## 3.2 Convention floor

Floor acts for an investigation and intrigue layer, each with ≥1 precedent. "VCD fam. n" =
`proposals/2026-10-03-verb-coverage-and-gap-fill.md` App. B family n (:4453-4491, opened).

| floor act | precedent | state today |
|---|---|---|
| **scout / survey** a place or power | VCD fam. 42 (audits, visitations; via register :4497). Proposal 14's *"somebody had to survey the valley"* (verb_table.yaml:955-962). Total War [MEMORY: agents and scouting reveal an army's composition before battle]. Mount & Blade [MEMORY: spotting range and the tracking skill reveal parties on the map] | `survey` **shipped** (faction or Rung, :966-984); scouting a place's forces **absent** |
| **search** a place for what is hidden | VCD fam. 2 (*L.A. Noire* crime scene, *Shadows of Doubt* prints) and fam. 30 (search and seizure, H1-175). Thief [MEMORY: searching rooms for hidden loot and switches] | **designed** (v2 V133 → `examine`, `_part8.md:449`) |
| **question** a person | VCD fam. 1 (*Pentiment*, *Disco Elysium*, *L.A. Noire*, *Lacuna*) | `interview` **shipped**; yields nothing |
| **interrogate** a person held | VCD fam. 27 (*Disco Elysium* pressing; interrogation with a notary H1-121) | **planned** (IN-12 step 5, SC) |
| **observe / shadow** a place or a person | VCD fam. 4 (*Pentiment* following a suspect unseen; *Shadows of Doubt* tailing and CCTV; CK3 Spymaster G2-20). Assassin's Creed [MEMORY: tailing and eavesdropping investigation missions] | `surveil` **shipped** (place only); the person case is **designed** and parked (`_part8.md:453`) |
| **infiltrate** a body or place | VCD fam. 31 (planting an agent H1-177, double agent H1-181, CK3 Spymaster). Shadow of Mordor [MEMORY: dominated captains planted in Sauron's army as spies]. Assassin's Creed [MEMORY: social stealth, blending into a crowd to reach a target] | **designed**, then CUT (`_part8.md:454`) |
| **forge** a document | VCD fam. 34 (CK3 fabricating, G2-17). CK3 [MEMORY: the chancellor fabricates a claim] | `forge` **shipped** |
| **conceal** oneself or a deed | VCD fam. 32 (Riskbreaker Identity, lapsing concealment, deniable acts). CK3 secrets (FW :157, via register). Thief [MEMORY: hiding in shadow, the light gem] | **planned** (IN-12 step 10) |
| **bribe** | VCD fam. 35 (*Shadows of Doubt* bribes, CK3 gifts, bribing an office-holder P2-02). Assassin's Creed II [MEMORY: paying heralds to lower notoriety] | **designed** (v2 V140, KEEP WITH CONDITIONS, `_part8.md:456`) |
| **blackmail** | VCD fam. 34 (CK3 blackmailing G2-18, spending a hook G2-19) | **designed** only as a composition (held Record + `petition` + `tell`), which instruction 5 rejects |
| **track** a quarry | Mount & Blade [MEMORY: tracks on the campaign map]. Shadow of Mordor [MEMORY: wraith-vision tracking]. VCD fam. 4 (the tailing half only) | **designed** (v2 V134 → `reconstruct`, `_part8.md:450`) |

Acts beyond the floor that the register raises: eavesdrop and intercept (VCD fam. 4), decipher
(VCD fam. 3: *Pentiment*'s codes and invisible ink; Walsingham's cipher secretary), audit and
census (LF-FI §1.2: Verres, Heshen, missi dominici). Each is judged in §3.3 on NERS and precedent,
not as floor.

---
## 3.3 Suites

Ten suites follow. **S0 comes first and is not a verb**: it is the rule every inquiry shares. It
defines what a finding writes and who reads it (R-C-23, R-C-15, S-6, H-111, the honest misreading),
so the suites below cite it rather than restate it.

**Fold-test key:** `A/M/P` = same actor? / same subsystem mechanic? / differs only in a parameter
or content?

### S0 · The finding: what an inquiry writes, and who reads it (shared rule, not a row)

**What a finding writes.** It writes Claims into the inquirer's own ledger at WITNESS, about the
inquiry's subject. Each Claim's `value` is read from the world by the verb's selector (table
below). Its `confidence` is set by degree. Its source is the inquiry, at remove 0 on H-199's
ordinal. `[ASSUMPTION: medium — a channel name for an inquiry's own deposit is not checked against
the roster; basis: the beneficiary note at verb_table.yaml:1137.]`
- The carriers exist: a Claim has `value` and `confidence` (verb_table.yaml:1230, citing
  `state/carriers.py:121-131`).
- The producer does not exist: FI-01 work item 4.5 (:1100-1103).
- This producer is **M1** (§3.7). Two inquiries write a Record instead, `survey` and `forge`, and
  their content reaches the holder through the shipped hold-deposit (`witness.py:397-421`).

| inquiry (mode) | selector: what the read takes from the world | Success writes | Failure writes |
|---|---|---|---|
| `examine` | Events in the log at the Rung the actor stands at, before this season, inside the read window | `seen` claims of those Events: kind, when, `who` | M3 misreading of `who`, or nothing |
| `examine` (search) | things present at that Rung whose concealment grade is above zero: a hidden Record, a concealed store, a covered person | a claim placing the thing there; a Record so found may then be taken (`seize`, `give`) | nothing true; the attempt is witnessed |
| `examine` (track) | the named quarry's leaving-acts at that Rung (`move`, `march`, `migrate`) | a claim of where the quarry went | M3: a wrong destination drawn from the Rung's other exits, or nothing |
| `research` | the content of a Record the actor consults, held or not; its `forgery_quality` | a `content:<kind>` claim; against the grade, a claim that the Record is forged | the content without the forgery verdict |
| `watch` (was `surveil`) | Events at the watched Rung this season whose anchor is a cover | the true `who` of a covered act, rolled against the cover's grade | the alias stands; the watcher is seen watching |
| `interview` | the questioned person's claims on the topic, as he is willing to give them (M5) | `told` claims with that person as teller | what he chose to say, unverified |
| `reconstruct` | the candidate doers the actor's own ledger places at the matter | a deed claim naming the best-supported candidate | M3: a deed claim naming another candidate, at the same confidence band |

**Failure is not refusal (S-6, H-111, FI-G11, FI-G12).** Today both emit `finding.none`. They split
as **M2**:
- **Refusal** (a precondition failed; no roll) emits a flat `inquiry.refused`. This keeps invariant
  4's flat-refusal rule: one kind per row for every failable clause (`forge` refusal_note, :345).
- **Failure** (rolled, lost) emits `finding.none` and deposits only what the table says.
- The two kinds then differ, so S-6's falsifier, *"a failed attempt emits something other than a
  failed precondition"* (PS:80, via register), is met.

**H-111 answered for FI, by CLAUDE.md §0 ladder step 5 (architecture).** Should a refused or
failed inquiry be news? Yes, and that behaviour is already running.
- H-111 (`hole_register.yaml:1617`) records that refusal Events take the deposit path, and that
  *"seeing somebody try and fail is real information"*.
- For inquiry this **is** the price canon wanted from Exposure: *"+2 Exposure (conspicuous
  activity)"* (verb_table.yaml:1199 note).
- Canon's price arrives with no meter. `rosters.yaml` forbids a bare `exposure` name (via register,
  P6:266), and the meta-rule (`skills/ners/SKILL.md:72-78`) refuses a new gauge.
- So a person who pries at a place is seen prying, and the guilty learn they are hunted. Steps 1-4
  of the ladder are silent; step 5 picks the option that adds nothing.

**The honest misreading (FI-G08, FI-G10).** This is **M3**.
- **Rule.** On Failure, an inquiry whose yield names a person draws the named `who` from its own
  **candidate set**, excluding the true one. The candidate set is the persons the read already
  places there: `seen.who` at that Rung for `examine`, or the actor's own claims for `reconstruct`.
- **Edge cases.** A set of one deposits nothing. The deposit carries the confidence band Failure
  gives, so the inquirer cannot tell it from a true finding.
- **Why the value is not invented.** K-37 deferred this for want of a value space (VCD:2908-2913,
  via register). The candidate set **is** that value space, and every value in it comes from the
  log or the ledger.
- **What it delivers.** An honest inquirer can now be wrong with no liar in the chain: canon's
  *"plausible but incorrect interpretation"* (verb_table.yaml:1230 note, citing `fieldwork_v30.md:278`).
- **FI-01's "Failure deposits nothing" is superseded for these verbs.** FI-01 deferred K-37, and K-37's
  stated reason (no value space) is answered here. Ladder steps 1 and 5.
- `[ASSUMPTION: medium — basis: FW §2.5 (Heaven's Vault, Pentiment, Paradise Killer, via register);
  Foscarini case LF-FI §1.2:62; revert: Failure deposits nothing.]`

**The concealer's score as the obstacle (R-C-15, FI-G16).** This is **M4**.
- **The ruling.** Jordan ruled that *"Obstacles that are defined oppositionally … are score/2. Obstacles
  that are not defined oppositionally, like a site, are a base plus relevant modifiers"*
  (`proposals/2026-08-18-fieldwork-architecture-and-nonadversarial-play.md:980-982`, opened).
  Concealment Ob *"derives from the concealer's score/2, not from their roll"* (:991).
- **The rule.** Every concealing act writes the concealer's score/2 onto the thing concealed, at the
  time of concealing:
  - `conceal` writes it onto the cover Record;
  - `forge` writes it into `Record.forgery_quality`. That field is a Record's own (H-210 cites Layer 1
    §D.4: *"a Record OWNS its forgery quality"*);
  - a hidden store writes it as EC's concealed half (flag §3.8).
- **The read.** Every inquiry that meets a concealed thing reads that number as its Ob: `examine`
  (all modes), `research`, `watch`, `reconstruct` where the doer was covered.
- **Why one number.** It is one number on the object and one rule at every reader, so there is no
  second ladder (§0.06 S, *"calculations consistent in methodology"*).
- **Until J-T1 rules a stored score** (`_part7.md:87`, via register), the score is `pool_default`
  for everyone. That value stays swept as H-126 has it.

**Who reads a finding (the cluster's world effects, caution 6):**
1. **The inquirer's own choices.** CHOOSE reads own-ledger cells (`own_ledger`, verb_table.yaml:974-975):
   `tell` passes the finding on, `reconstruct` assembles it, `forge` and `survey` need a claim on the
   subject, and SC's charge (`open_case`, `petition`) names a doer. Held Records feed
   `record_sourced_operands` (`rosters.yaml:1708-1733`).
2. **Others, through his telling.** Others learn only by his `tell` or `give`. The hearsay carries
   `chain` and `teller`, and is discounted by remove (H-199, via register).
3. **WITNESS.** Persons present learn that he inquired (M2 and H-111).
4. **Attribution.** A cover changes `anchor_of`; a pierced cover is a finding that names the true
   doer.
5. **SC's proceedings.** A finding's source maps to a proof kind: a document read → `record`, an
   interview's reply → `testimony`, an interrogation → `confession`. `arrangements.yaml:204-216`
   lists `proofs`; `determine` reads none of them today (FI-G47). That reader is SC's (M9, §3.8).

### S1 · The scene — host `examine`; folded `search`, `track`

- **Host.** `examine` reads what happened at the place where the actor stands, before he came.
- **World effect.** `seen` claims about past Events at the Rung (S0 table). Emits `finding.made` or
  `finding.none`, and refuses with `inquiry.refused` (M2).
- **Lacks.** Both the producer (M1) and a reachable binding are missing.
  - The row binds a `Site` (:1141-1147), so it is "refused only" in the seed-0 corpus (FI-G05, via
    register).
  - **REBUILD:** bind the Rung the actor stands at (`present_at` over a Rung, `surveil`'s cell
    :1191-1197). Persons are always at a Rung, so the act becomes formable.
  - The documentary reading stays `research`'s, so canon's Verified/Documentary split (:1110-1112)
    survives.
  - `[ASSUMPTION: medium — basis: VCD:849 "past Events at the present Site's rung" (via register);
    the block comment's own admission that the Site binding is what makes it refuse (:1126-1130).]`
- **Fold: `search` → `examine`.** A ✓ the one present · M ✓ presence, one roll, an own-ledger
  deposit from that place · P ✓ the selector (hidden things present now) and the Ob source (M4 grade).
  **Passes.** Search is the convention name of the mode. It shows in the act's payload and the UI.
  A Record found may then be taken by `seize` under a warrant (shipped) or by `give`; that is the
  next act, not part of `search`.
- **Fold: `track` → `examine`.** A ✓ · M ✓ the same log-at-a-place read · P ✓ a filter: the named
  quarry's leaving-acts. **Passes.**
  - **v2's re-target fails the test.** v2 put `track` on `reconstruct` (`_part8.md:450`), but
    `reconstruct` reads only the actor's own ledger (`own_ledger`, :1225-1227). It cannot find a
    trail the tracker has not already seen. That is a different mechanic.
  - Following across places is the player's repeated choice, one hop per act, not a composed act.
- **N.**
  - Cut it, and nobody can learn what happened at a place before he arrived. Presence delivers only
    the present (WITNESS by co-location). The after-the-fact inquiry dies: a body found, then
    investigated.
  - From all six directions:
    - top-down: a lord sends a man to a burned granary;
    - bottom-up: the finding is the only producer of a `who` for SC's charge;
    - lateral: `search` is the counter to `conceal` and to EC's hoard;
    - diagonal: `track` feeds `march` and `arrest`;
    - horizontal: it shares one methodology with S2-S5;
    - vertical: it gives the scout and the investigator the same act.
  - **False N-line check, attacked and failed.**
    - `watch` reads the season it watches, forward, not back.
    - `survey` reads a faction's or Rung's state, not Events.
    - `reconstruct` reads only what the actor already holds.
    - Nothing ruled in provides the past at a place.
- **R.** R-player: the finding decides whom to charge and where to march. R-world: a stranger
  prying at the site is news (S0), so the hunted learn they are hunted unwatched.
- **S.** One roll and one Ob rule, shared with S2-S5 (M4). It needs no pause: it is a season act.
  Trace decay is the read window (FI-G50), not a per-kind decay map. That keeps it consistent with
  claim decay, which already exists.
- **E (ratio).** Three floor acts share one row, one read and a selector, and add no carrier. What
  is lost: none of N's or R's findings. **High.**
- **Precedent.**
  - VCD fam. 2 (*L.A. Noire* crime scene, *Shadows of Doubt* prints, *Pentiment* body and
    inscription) and fam. 30 (search and seizure).
  - The coroner's view (LF-FI §1.2:47).
  - For `track`: Mount & Blade and Shadow of Mordor `[MEMORY]` (§3.2).
- **Gaps closed:** FI-G04, G05, G33 (with M6), G50, G53, G54, G57; G16 and G17 through M4.
  **Left open:** a Site-level narrowing inside a Rung.
- **Disposition.** `examine` **REBUILD** (Rung binding; M1 yield). `search` **FOLD**. `track`
  **FOLD**, re-targeted from `reconstruct`.
- **Falsifiers.**
  - KEEP fails if a seeded world with a `fight` at a Rung last season, examined there this season,
    deposits no claim of that fight.
  - FOLD fails if `search` needs a write `examine` does not make.

### S2 · The record — host `research`; folded `decipher` (parked)

- **Host.** `research` reads what a document says without having to hold it, and tells a forgery
  from a true one.
- **World effect.**
  - A `content:<kind>` claim, which the hold-deposit gives today only on a hold opened this tick
    (`witness.py:397-421`). The trigger FI-G02 names is **M1's consult deposit**.
  - Against `forgery_quality` (M4): a claim that the Record is forged.
- **Lacks.** It has no access gate. Canon gates Buried research on institutional access (:1179
  note), and that is a `hold:<dispensation>` eligibility (M6, H-75).
- **Fold: `decipher` → `research`.** A ✓ · M ✓ one read against an obstacle · P ✓ the Ob is the
  cipher's grade, an M4 number written by the enciphering maker. **Passes. PARKED.**
  - Trigger: a Record kind carrying a cipher grade, written by its maker (`create_record` or
    `issue`).
  - v2 CUT it (`_part8.md:452`) because nothing writes a cipher. That cut is free today (false-N
    disqualifier 2, no producer). Parking it instead makes the revival mechanical.
  - Decipher is not on the floor.
- **N.**
  - Cut it, and a forgery can never be found out: `forge` becomes a dominant act with no answer.
  - A document can be learned only by taking it.
  - Archival inquiry dies. It is pre-modern inquiry's documentary half (LF-FI §1.3).
  - False N-line check: is the forgery reader SC-02 `22b` step 25's examination (H-210 owner)? That
    reader is the same act done in a docketed venue. Two readers of one field would be two owners.
    **One rule (M4), called from both** (flag §3.8).
- **R.** Forging becomes a contest of the forger's score against the reader's roll. A forgery found
  out is a claim that can be told: a scandal nobody scripted.
- **S.** Same Ob rule as `search` and `watch` (M4). The deposit stem is the shipped `content:<kind>`.
- **E.** One row; `decipher` costs nothing until a cipher exists. **High.**
- **Precedent.**
  - VCD fam. 3 (*Pentiment* codes and invisible ink; *Shadows of Doubt* records; Walsingham).
  - H-210's sweep (0/1/3) names the forgery reader as the thing that *"unblocks a forgery that can
    be FOUND OUT"* (`hole_register.yaml:4532`).
- **Gaps closed:** FI-G02, G23, G34 (with M6). **Parked:** G31.
- **Disposition.** `research` **REBUILD** (consult deposit; forgery read). `decipher` **FOLD, PARKED**.
- **Falsifier.** KEEP fails if a `research` at Success on a forged sheet deposits no claim that it is
  forged once `forgery_quality > 0` is written.

### S3 · Watching — host `watch` (rename of `surveil`); `shadow` sibling (parked); `eavesdrop` folded (parked); `intercept` (parked, no host)

- **Host.** `watch` keeps a place under watch for the season and learns who really did what there.
- **World effect.** For acts at the watched Rung this season whose anchor is a cover (`anchor_of`,
  `state/attribution.py:103`), the true `who` is rolled against the cover's grade (M4). The watcher
  is seen watching (S0).
- **Lacks.**
  - M1's read.
  - The cover itself (S8).
  - Alignment cells: `surveil: null` stays per `rosters.yaml:2348`, *"a cost and not a creed"*
    (via register). That is a ruling, kept.
- **Rename `surveil` → `watch` (L-09 applied).**
  - The two words are one letter apart, and both now take a Rung (:966-984, :1186-1197).
  - `watch` is the plain word and covers both cases: *watch the gate*, *watch him*.
  - Its Germanic root is the same PIE root as `surveil`'s Latin (*\*weǵ-*, Wikt), so nothing of
    the sense is lost.
  - `spy (on)` was considered and declined. It asserts a secrecy the row does not enforce: canon
    makes surveillance conspicuous (:1199 note).
  - `survey` keeps its name.
- **`shadow`: a sibling row, not a fold.** A ✓ · **M ✗** · P ✗. Shadowing moves the shadower:
  his presence must follow the quarry's moves through the season. `watch` makes no such write.
  - It needs its own row, bound to a Person (as `interview` binds a Person, :1158-1162). That is
    v2's "Person-bound sibling row" (`_part8.md:453`), which the grammar admits without a
    disjunction.
  - **PARKED.** Trigger: a co-movement write, an effect that ends the actor's season where the
    subject's moves end.
- **`eavesdrop` → `watch`.** A ✓ · M ✓ presence at a Rung, one read · P ✓ the selector is the
  content of a confided telling. **The fold passes, but the cut is free today**, a false-N
  disqualifier 1: a bystander present *"holds the claim"* of a confided telling (`witness.py`
  `_circle_of` docstring), because *"private whispers are not built"*.
  - **PARKED.** Trigger: recipiency narrower than presence (private whispers).
  - v2's revival form, *"`conceal` + `move`"* (`_part8.md:451`), is a two-act composition and
    fails instruction 5. The revival is this mode.
- **`intercept`** (a letter in transit, VCD:456/461, via register). **PARKED, no host.** No Record
  is ever in transit: `give` moves a hold within one act (:413-440). Trigger: a Record carried
  between holders over time. The host (`seize` to take, `research` to read) is decided then.
- **N.**
  - Cut it, and nothing pierces a cover except the coverer's own failed roll. `conceal` becomes
    dominant (an R defect). Counter-espionage (ED-FI-0002, FI-G42) and the stake-out die.
  - **False N-line attacked, partly upheld.** `examine` next season recovers most of a place's
    events. What `watch` adds:
    - one season less lag;
    - no loss to the read window;
    - the person case (`shadow`), which `examine` cannot host.
  - The act is floor (observe/shadow), so it is kept. The N finding sizes how much is built: the
    cover pierce first.
- **R.** R-player: the counter-move to intrigue. R-world: a watched spymaster's agents are unmasked
  with no player present.
- **S.** M4 shared with `search`/`research`. In a season loop a watch already pauses for nothing.
- **E.** One row; three named acts parked at zero cost. **High once the cover exists; nil before it.**
- **Precedent.**
  - VCD fam. 4 (*Pentiment* following unseen; *Shadows of Doubt* tailing and CCTV; CK3 Spymaster
    disrupting schemes G2-21).
  - Venice's State Inquisitors (LF-FI §1.2:49, `[UNVERIFIED]` at source).
  - Assassin's Creed `[MEMORY]`.
- **Gaps closed:** FI-G06, G28 (with S8), G29 (S0), G36, G42 (with S8). **Parked:** G07, G32.
  **Left:** G52 for `watch` (null by ruling).
- **Disposition.** `watch` **REBUILD** (rename; M1 cover-pierce yield). `shadow` **NEW ROW, PARKED**.
  `eavesdrop` **FOLD, PARKED**. `intercept` **PARKED**.
- **Falsifiers.**
  - KEEP fails if a covered `seize` at a watched Rung leaves the watcher, at Success, without the
    true doer's id.
  - The `eavesdrop` park fails if a bystander can be shown not to receive a confided telling today.

### S4 · Questioning — host `interview`; `interrogate` stays SC's own row

- **Host.** `interview` asks a person what he knows about a matter.
- **World effect.**
  - `told` claims with the questioned person as teller, on the topic, as far as he is willing (M5).
  - The question itself is a deposit in the questioned person's ledger, a claim that the asker
    wants to know X. That is information, and it is the reason a suspect learns he is suspected.
- **Lacks.**
  - M5. The reply cannot be read today: F8 forbids the fold reading any ledger but the actor's
    (:1163 note).
  - A `counterparty:` clause to close self-interview (FI-G20; the cell admits a subject that is the
    actor, :1163 note).
  - *Approach* (calm or aggressive) stays a payload key (VCD:731-742, via register). That is right:
    it is a parameter.
- **`interrogate`: not folded.** A ✓ the questioner · **M ✗** · P ✗.
  - Interrogation needs custody (a `detain` edge) and is resolved against the subject's
    resistance, as SC's `interrogation` arrangement (`arrangements.yaml:202-216`: proofs
    testimony and confession; disposes `detain`).
  - Interview is uncontested and consented. The seams ruling forbids making inquiry a contest
    (`requirements.yaml:178-179`), so the contest half cannot ride `interview`.
  - It is its own verb, planned at IN-12 step 5 and owned by SC (§3.8). FI supplies its yield: the
    confession, as a finding of proof kind `confession`.
- **N.**
  - Cut it, and the only way to learn what another knows is to wait for him to choose to tell.
    Testimonial inquiry dies, and that was most of pre-modern inquiry (LF-FI §1.3).
  - False N-line check: `tell` is the other's act (beneficiary `subject`, :1137 note), so it does
    not provide the asker's act. **Not false.**
- **R.** He may refuse, or lie once J-C-6 rules lying in. His stance toward the asker decides how
  much he gives, so the asker must choose whom to ask.
- **S.**
  - The reply deposits through the shipped `told` path (`_told_content`, `witness.py:84-102`), one
    channel for hearsay. No second methodology.
  - The Dialogue Lattice (ED-FI-0004, ruled *"Lattice first"*, FW:1015) is the act's front end and
    drives this row. It does not replace the verb (FI-G21).
- **E.** One row; one new read (M5). **Medium**: M5 is architecture-heavy.
- **Precedent.** VCD fam. 1 (*Pentiment*, *Disco Elysium*, *L.A. Noire*, *Lacuna*, *Shadows of Doubt*).
- **Gaps closed:** FI-G19 (once M5), G20, G21, G40. **Out of scope:** G39 (SC's row).
- **Disposition.** `interview` **REBUILD** (counterparty clause; M5 yield). `interrogate`: SC's
  **PLANNED** row, listed here for the floor.
- **Falsifier.** KEEP fails if, after M5, an interview of a person who holds a claim on the topic
  and stands well toward the asker deposits nothing.

### S5 · Reasoning — host `reconstruct`

- **Host.** `reconstruct` works out who did it from what the actor already holds.
- **World effect.**
  - A deed claim the actor did not hold before: `who` did the act in question. It is drawn from the
    candidate set his own ledger supplies (S0).
  - Success names the best-supported candidate. Failure names another candidate (M3).
  - This is the new information FI-G09 says is missing. The row stops being a self-feeding loop
    because its output is an attribution, which no other act produces.
- **Lacks.** A scope (canon's 3/5/8 threshold is *"chosen at opening BY A GM"*, :1228 note).
  **Answer:**
  - Ob = the non-person base, less one per supporting claim held on the matter. This is canon's
    *threshold − progress* (:1228) with the threshold set to the base: no scope and no GM.
  - Where the doer was covered, Ob = the cover's grade instead (M4).
  - `[ASSUMPTION: medium — basis: Q1's base-plus-modifiers for non-oppositional Ob (FW:980-982);
    revert: K-37 deferral.]`
- **No fold** is proposed. v2's first-pass retirement into `examine` (V2-3:410, via register) fails
  M: `examine` reads the world and `reconstruct` reads only the actor's own ledger.
- **N.**
  - Cut it, and observations never become an accusation. SC's charge has no producer of `who`
    except an eyewitness.
  - The honest misreading (canon :278) has no home.
  - False N-line check: does `examine`'s `who` provide it? Only for the eyewitnessed case, not the
    inferred one. **Not false.**
- **R.** R-world's strongest hook in the lane: an innocent accused by honest error, the Foscarini
  shape (LF-FI §1.2:62).
- **S.** Uses the Claim carrier as it stands. Its Ob rule is S0's.
- **E.** No new carrier. **High.**
- **Precedent.**
  - VCD fam. 5 (*Lacuna*, *Shadows of Doubt* case board).
  - FW §2.5 (Heaven's Vault, Paradise Killer; via register).
- **Gaps closed:** FI-G08, G09, G10, G22.
- **Disposition.** **REBUILD.**
- **Falsifier.** KEEP fails if a reconstruct over two `seen` claims naming two present persons
  cannot, at Failure, deposit the wrong one.

### S6 · The fabric — `thread_read` (cross-lane with TW); `trace` (parked, TW)

- **`thread_read`** is shipped and cannot be attempted: its TS ≥ 30 gate has no carrier (H-85,
  :1210-1218).
- **FI's share** is only the finding shape (S0): its yield, Failure, and refusal.
- **TW's share** is the gate (the one class-shaped gate: FI-G18), the Coherence cost and Exposure
  (:1219 note).
- `trace` (knot-mediated remote inquiry) is TW-G19's, parked on plugged knots.
- **Disposition.** `thread_read` **KEEP-AS-IS** in FI's lexicon, owner to be reconciled (§3.8).
  `trace` **PARKED** (TW).
- **N/R/S/E.** Deferred to TW. The S constraint FI imposes: the same Failure/refusal split (M2) and
  the same Ob rule (M4).
- **Gaps:** FI-G18 is closed by the suite-wide rule that **no inquiry carries an attribute gate**.
  FI-G55 is out of scope.

### S7 · The commissioned picture — host `survey`; folded `audit`, `census`, `scout` (`reconnoitre`)

- **Host.** `survey` has a written account made of a power or a place: a document someone can
  hold, give, forge or burn.
- **World effect** (shipped).
  - A `faction_sheet` Record minted into the surveyor's hold (:976-978).
  - Its content in his ledger (hold-deposit).
  - Emits `faction.surveyed`.
- **Lacks.**
  - **M7.** A Rung subject today yields the *holder faction's* sheet (:975 note, IN-12). The place's
    own state needs a `rung_sheet` kind: holder, persons, stores, forces mustered.
  - **M7's readers.** Choices that read `members`/`holdings`/`seats` (FI-G03) are missing.
  - A presence condition for a Rung subject. A place is surveyed by standing in it: eligibility
    `presence:<rung>` for that subject kind. A faction is surveyed from a distance, as
    proposal 14 intends. `[ASSUMPTION: medium]`
- **Fold: `audit` → `survey`.** A ✓ · M ✓ `_eff_survey`'s one mint · P ✓ the subject is a Rung or
  office under the actor's purview. **Passes.**
  - What an audit finds, a gap between what is owed and what is there, is read by comparing a held
    prior sheet or a writ's dues: a choice, not a second act.
  - v2's "`research` on a frozen account" (`_part8.md:457`) **fails P**: `research` writes no
    document. An audit's product is a report that can be handed to a superior and used as proof
    `record`.
  - VCD files audits and visitations under `survey` (fam. 42, via register).
- **Fold: `census` → `survey`.** A ✓ · M ✓ · P ✓ Rung subject → `rung_sheet` (persons, stores).
  **Passes.** Flag GV.
- **Fold: `scout` (`reconnoitre`) → `survey`.** A ✓ · M ✓ · P ✓ a Rung the actor stands at; the
  content includes forces mustered. **Passes.**
  - v2's re-target onto `surveil` (`_part8.md:408`, via register) gives the scout a private claim
    and no report a commander can be handed.
  - Watching reads Events over a season. Scouting reads a standing state now.
  - Flag MB.
- **N.** Cut it, and the faction-scale picture has no diegetic source: proposal 14's *"Free to
  read, costly to obtain, stale by construction"* (:958-960). The document that can be wrong,
  burned or given dies, and so does `forge`'s target.
- **R.** Sheets go stale, are forged, burned or handed to an enemy. Scouting before battle and
  auditing a steward are floor choices.
- **S.** One mint (`_mint_document`) for `survey`, `forge`, `issue` and `petition` (:977 note).
  - Down: a sheet feeds a Duke's `march`.
  - Up: a steward's audit feeds his lord's charge.
- **E.** Four acts, one row, one new record kind. **High.**
- **Precedent.**
  - Proposal 14 (Jordan's, via :962 source).
  - VCD fam. 42.
  - Verres and Heshen as audit cases (LF-FI §1.2:55-56).
  - Total War and Mount & Blade `[MEMORY]` for scouting.
- **Gaps closed:** FI-G03 (once M7), G35. **Disputed:** G37 (§3.5).
- **Disposition.** `survey` **KEEP-AS-IS** for the faction case; **REBUILD** for the Rung case
  (presence; `rung_sheet`). `audit`, `census`, `scout` **FOLD**.
- **Falsifier.** KEEP fails if a surveyor's ledger lacks the sheet's content after the act. The
  shipped hold-deposit says it does not.

### S8 · Cover — host `conceal`; folded `disguise`; sibling row `infiltrate`

- **Host.** `conceal` hides who one is, so that one's acts are put down to an alias.
- **World effect** (planned IN-12 step 10).
  - A `cover` Record, `terms` = the actor.
  - `anchor_of` resolves his acts to the cover's id while a stage is unmatured, and
    `_ch_witness_key` changes with it (VCD §9.3:1826-1863, opened).
  - **REBUILD the acceptance line.**
    - The cover carries its grade (M4).
    - A failed concealed act exposes its doer: a degree-keyed break in the cover read, for every
      concealed act (`_part8.md:316-317`).
    - The scope is `later` (the planned default: *"`seen.who` still names the actor"*) or `room`.
- **Fold: `disguise` → `conceal`.** A ✓ · M ✓ one cover Record, one `who` reader · P ✓ the scope,
  `room`, withholds `seen.who` from those present. **Passes**, as v2 had it (`_part8.md:455`).
- **`infiltrate`: a sibling row, not a fold into `conceal`.** A ✓ · **M ✗** · P ✗. Infiltration
  writes an admission, a duty edge to a seat (`oblige`'s write, :758-779), taken while a live cover
  stands. `conceal` writes only the cover.
  - Against `oblige` the fold test *passes* (A, M, P: the precondition "holds a live cover"). The
    row is still separate on N and R, by V.2.1's rule (`_part8.md:88-109`): *"a kind maps to a
    verb only where exactly one row emits it"*. An honest pledge and a false one must be priced
    apart by every creed and every witness, or spying is a gift.
  - So: **NEW ROW `infiltrate`**, over `oblige`'s write, eligibility `own`, requires a live cover.
    Its attribution falls to the alias through `anchor_of` with no new mechanic.
  - The **place** half (entering a guarded place) is **PARKED**. Trigger: a place that refuses
    presence.
  - v2's CUT ("the composition `oblige` → `tell`, with a cover read", `_part8.md:454`) is the
    composition instruction 5 forbids, and v2 itself reversed it (`_part8.md:577`, via register).
- **N.**
  - Cut `conceal`, and nine v2 verdicts lose their read (V.2.10, `_part8.md:303-317`).
  - The deniable act (NPC-005, VCD:1859) and the covert body (the Riskbreakers, `rosters.yaml:1643`,
    opened: *"Extralegal infiltration"*) die.
  - Cut `infiltrate`, and the agent planted in a rival's service, a floor act, exists only as two
    steps the chooser never joins.
- **R.** A cover lapses by its stages (MATTER), so dominance is periodic and paid for (VCD:1844-1845).
  R-world: double agents with no player present.
- **S.**
  - Attribution is one owner (`anchor_of`).
  - `watch`, `examine` and `research` all roll against the cover's one grade (M4).
  - The cover break is generic, never per-verb (the K-19 rule, VCD:1838-1839).
- **E.** Three floor acts: one planned row, one mode, one sibling over a shipped write. **High.**
- **Precedent.**
  - VCD fam. 31 and 32.
  - CK3 Spymaster (G2-20).
  - Shadow of Mordor and Assassin's Creed `[MEMORY]` (§3.2).
- **Gaps closed:** FI-G26, G27, G28, G30, G42 (with S3). **Parked:** G51 (scheme secrecy, a
  conspiracy carrier SC/FA have not built).
- **Disposition.** `conceal` **PLANNED** (REBUILD the acceptance line). `disguise` **FOLD**.
  `infiltrate` **NEW ROW** (the place half **PARKED**).
- **Falsifier.** KEEP fails if `anchor_of` resolves an Event to a cover id and a chronicle deposit
  about it still names the actor (VCD's own falsifier, :1854-1855).

### S9 · Documents falsified and burned — host `forge`; sibling row `destroy_record`

- **Host.** `forge` makes a false document that passes for a true one.
- **World effect** (shipped). A false `faction_sheet` with the forger as `head`, in the forger's
  hold, to plant by `give` (:334, :340).
- **REBUILD, three edits:**
  1. **Write `forgery_quality`** = the forger's score/2 (M4). Today that is `pool_default`/2.
     - Writer and reader land together with S2's `research` read. That is H-210's own condition:
       *"writer and reader together"* (`hole_register.yaml:4525`).
     - Ladder step 5: the value is the ruled Q1 formula, not a swept constant.
  2. **Emit the honest twin's kind**, `faction.surveyed`, not `record.forged` (L-11 applied).
     - WITNESS deposits `predicate = e.kind` (L-11, `witness.py:532`, via critic), so a witness
       of `record.forged` holds the truth the row says nobody learns (:343).
     - Sharing a kind is lawful. `_derive_kind_verb` maps a kind emitted by two rows to no verb
       (`data/verbs.py:1233-1248`, opened), so a witness's deed judgement cannot name `forge`.
     - **Cost:** `survey`'s kind stops mapping to `survey` too. Accepted: a survey is uncelled
       intelligence work, and the loss is a witness's certainty, which is the point.
       `[CONFIDENCE: medium]`
  3. **Etymology corrected** to the verb path (L-11, §3.4).
- **`destroy_record`: not folded.** Into `forge`: A ✓ · M ✗ (writes `Record.exists` false) · P ✗.
  Into `conceal`: M ✗.
  - It stays its own row, the one closer of a Record by act (v2 KEEP, V2-3:414, via register).
  - It forms for nobody: both eligibility alternatives are placeholders (H-75; :215 note, *"forms
    for nobody in the realm today"*). It waits on M6.
  - L-15's `burn` is noted, not applied: `burn` names one means. `destroy_record`'s CRUD shape is
    IN's naming question (§3.8).
- **N.**
  - Cut `forge`, and the document-as-fact (survey, writ) cannot be falsified. The information
    cluster loses its deception half, and the H-210 reader has nothing to find.
  - Cut `destroy_record`, and evidence is permanent: the burn that closes a conspiracy dies.
- **R.** Forged writs move executors (`r2 02 §A.15`, quoted at H-210: *"a forged writ and a genuine
  one are indistinguishable in every executor's ledger"*). R-world drama with no player.
- **S.** One mint (`_mint_document`). One grade rule (M4).
- **E.** **High** after the edits. `record.forged` is a kind the rewrite deletes.
- **Precedent.**
  - VCD fam. 34 (CK3 fabricating, G2-17).
  - VCD fam. 30 (seizing or burning property, P2-44).
- **Gaps closed:** FI-G23, G24, G25 (once M6).
- **Disposition.** `forge` **REBUILD**. `destroy_record` **KEEP-AS-IS** (eligibility waits on M6).
- **Falsifiers.**
  - KEEP of `forge` fails if, with the twin kind, a present witness can still name the act a
    forgery from the Event alone.
  - KEEP of `destroy_record` fails if it forms once `hold:<record>` is typed and still never
    executes.

### S10 · Inducement — host `bribe` (new); `suborn` content (parked); `blackmail` → SC

- **Host.** `bribe` pays a person to do something.
- **World effect.**
  - `transfer`'s write: `Rung.stores` moves from the payer's holding to the payee's (:1247-1251).
  - An **inducement** deposit to the circle of two, payer and payee only. It is the terms, the act
    paid for, in the shape of `_circle_of`'s confided telling (`witness.py:105-134`).
  - **Lacks: M8**, a payee-side reader that weighs the paid-for act in his CHOOSE. Without it *"an
    offer moves nothing"* (`_part8.md:456`).
  - Event kind: `transfer.made` (shared), for S9's reason. A witness sees money change hands; only
    the two know the terms.
- **The fold into `transfer` passes the mechanical test** (A ✓ · M ✓ · P ✓ the terms). **The row is
  still separate** by V.2.1: a gift and a bribe must be priced apart by creeds and witnesses.
  - This is the one place the lane keeps a row for value reasons alone.
  - **Reversal condition:** D-V6's `(verb, kind)` value key (`_part8.md:106-109`) turns it into a
    content of `transfer`.
  - `bribe` is **not** `oblige` (L-02; `_part3.md:131` "Bribe is not oblige (Jordan)", via critic).
- **`suborn` → content of `bribe`** where the act paid for is unlawful (V-05 applied). **PARKED**
  on J-C-6: perjury needs persons who can lie (`_part7.md:93`).
  - Suborning by threat is the same content on SC's threat host.
  - v2's *"FA's `suborn` is the same act"* (`_part8.md:456`) is rejected. Suborn names the aim;
    bribe is one means to it.
- **`blackmail`: not FI's row.** It is a demand backed by the threat of disclosure. Against SC's
  threat host the test passes: A ✓ the one who threatens · M ✓ a demand with a sanction · P ✓ the
  sanction is to disclose a held finding.
  - So it is a **mode of SC's threat** (§3.8). That replaces VCD's composition (held Record +
    `petition` + `tell`, fam. 34), which instruction 5 rejects.
  - FI supplies its leverage, the **secret**: a finding the actor holds about a deed whose doer
    held a live cover. It needs no new carrier: VCD's row 41 already reads a secret as *"a claim
    others lack, a `cover`, a `seen` with `who` withheld"* (VCD:808, opened).
- **N.** Cut `bribe`, and an official cannot be bought: a floor act of every intrigue game dies,
  and the corrupt office (Heshen, Verres) has no act behind it.
- **R.** Strategy: whom to buy, and at what price. R-world: corrupt officials appear unscripted,
  and an audit (S7) finds them.
- **S.** It composes on the shipped write primitive (`transfer`) rather than re-implementing it.
  The terms ride the shipped confidential-circle shape.
- **E.** One new row and one reader (M8). **Medium**: M8 is a new decision input.
- **Precedent.**
  - VCD fam. 35 (*Shadows of Doubt* bribes; bribing an office-holder P2-02; gifts for favour R1-64).
  - Assassin's Creed II `[MEMORY]`.
  - For blackmail: VCD fam. 34 (CK3 blackmail, hooks).
- **Gaps closed:** FI-G41 (once M8).
- **Disposition.** `bribe` **NEW ROW**. `suborn` **FOLD (content), PARKED**. `blackmail` → SC (§3.8).
- **Falsifier.** KEEP fails if, once M8 exists, a paid official's choice of the paid-for act is no
  likelier than an unpaid one's.

---

## 3.4 Lexicon table

Chains were looked up one word at a time this session (Wikt `en`/`la`; L&S `ls`). "PGmc" =
Proto-Germanic. A Latin lemma is given with its principal parts as Wikt's headword template or L&S
states them.

| verb | suite | status | mechanic and world effect (carrier written) | etymology chain, with sources | fit (ordinary current usage) | rename |
|---|---|---|---|---|---|---|
| `examine` | S1 | SHIPPED → REBUILD | presence at the Rung; reads the log there; `seen` claims in the actor's ledger (M1) | ME *examinen* ← OF *examiner* ← L *exāminō, -āre, -āvī, -ātum* (1st conj.). L&S: lit. *"to weigh"*; trop. *"to weigh, ponder, consider, examine, try, test"* (class.). ← *exāmen* *"tongue of a balance; swarm; an examining"* (Wikt) ← *\*exagmen* = *ex-* + *agō* + *-men* (Wikt la *exāmen*) ← PIE *\*h₂eǵ-* *"drive"* (Wikt, via *agō*) | FITS: *examine the scene* is ordinary | — |
| `search` | S1 | FOLDED (examine) | the M4-graded hidden things present at the Rung; a claim placing them | ME *serchen* ← AN *sercher*, OF *cerchier* ← LL *circō, -āre* (Wikt; L&S: *"= circumeo … to go about, traverse; to wander through"*, late, Gromatici) ← *circus* *"circle"* ← likely Gk *κρίκος/κίρκος* *"ring"* ← PIE *\*(s)ker-* *"turn, bend"* (Wikt la). Wikt: *"Unrelated to German suchen"* | FITS | — |
| `track` | S1 | FOLDED (examine) | the quarry's leaving-acts at the Rung; a destination claim | ME *trak* ← OF *trac*, *"of uncertain origin. Likely from a Germanic source"*: ON *traðk* *"trodden spot"* or MDu *trec* (Wikt). **Not Latin**; no PIE root given | FITS: *track a fugitive* | — |
| `research` | S2 | SHIPPED → REBUILD | consult deposit (`content:<kind>`); forgery read against `forgery_quality` | EModE ← F *rechercher* ← OF *recerchier* = *re-* + *cerchier* (Wikt; see `search`) ← LL *circō* *"go about"*. Not "seek again" (L-01) | FITS: *research the deeds and rolls* | — |
| `decipher` | S2 | FOLDED (research), PARKED | Ob = a cipher grade on a Record (trigger: a cipher field) | *de-* + *cipher* (Wikt) ← OF *cyfre* ← ML *cifra* ← Ar. *ṣifr* *"zero"* (Wikt). **Not Latin at root** | FITS | — |
| `surveil` | S3 | SHIPPED → RENAME | (see `watch`) | back-formation from *surveillance*, *"1903"* (Wikt) ← F *surveiller* ← *sur-* + *veiller* ← OF *veillier* ← L *vigilō, -āre, -āvī, -ātum*. L&S: *"to watch, i.e. to be or keep awake at night, not to sleep, be wakeful"*; fig. *"watchful"*. Wikt adds transitive *"to watch through, spend in watching"*. ← *vigil* *"awake, watching; watchman"* ← PIE *\*weǵ-* (Wikt) | STRAINED: fits alone, but one letter from `survey`, and both take a Rung (L-09) | **`watch`** |
| `watch` | S3 | SHIPPED (renamed) → REBUILD | presence at the Rung over the season; pierces covers (true `who` against the M4 grade) | ME *wacchen* ← OE *wæċċan* ← PWGmc *\*wakkjan* ← PGmc *\*wakjaną* ← PIE *\*weǵ-* (Wikt). **Germanic; no Latin path.** L *vigil/vigilō* is a **cognate, not an ancestor** (same root, Wikt) | FITS: *watch the gate*, *watch him* | — |
| `shadow` | S3 | NEW ROW, PARKED | Person-bound; co-moves with the quarry (trigger: a co-movement write) | ME *schadowen* ← OE *sċeadwian* ← *sċeadu* ← PGmc *\*skaduz* ← PIE *\*(s)ḱeh₃-* (Wikt). **Germanic.** The "follow covertly" sense is modern `[UNVERIFIED: century]` | FITS: *shadow a suspect* | — |
| `eavesdrop` | S3 | FOLDED (watch), PARKED | content of a confided telling (trigger: private whispers) | *eaves* (OE *efes* ← PGmc *\*ubiswō*, *"perhaps ultimately"* PIE *\*upér*) + *drop* (Wikt). The listening sense comes from standing within the eaves-drip (Wikt). **Germanic** | FITS | — |
| `intercept` | S3 | PARKED (no host) | a Record in transit (trigger: one exists) | ← L *interceptum*, pp. of *intercipiō* (Wikt) ← PIE *\*keh₂p-* (Wikt); L&S *intercipiō, -cēpi, -ceptum*: *"to seize on the passage before arrival at the destined place, to intercept"* (*litteras*, Cic. Att. 1.13.2) ← *inter-* + *capiō* | FITS | — |
| `interview` | S4 | SHIPPED → REBUILD | `told` claims from the questioned person (M5); the question deposited with him; `counterparty` clause | ← OF *entreveue*, fem. pp. of *entrevëoir* ← *entre-* (L *inter*) + *vëoir* ← L *videō, vidēre, vīdī, vīsum* *"to see, perceive; observe, note"* (Wikt) ← PIE *\*weyd-* (Wikt) | FITS: *interview a witness* | — |
| `interrogate` | S4 | PLANNED (SC, IN-12 s5) | custody + contest; `confession.made` | ← L *interrogātus*, pp. of *interrogō, -āre, -āvī, -ātum* (Wikt). L&S: *"to ask, question, inquire, interrogate"*; Wikt legal: *"to question judicially"*. ← *inter* + *rogō* *"ask, request"* ← PIE *\*h₃reǵ-* *"stretch"* (Wikt; **disputed**: flagged rfv-etym, alternative from *procō*) | FITS | — |
| `reconstruct` | S5 | SHIPPED → REBUILD | a deed claim (`who`) from the own-ledger candidate set; M3 on Failure | English *re-* + *construct* (Wikt), **not a Latin compound** (L-16) ← L *cōnstrūctus* ← *cōnstruō* = *com-* + *struō, struere, strūxī, strūctum* *"to pile up, join together; to compose, construct"* (Wikt) ← PIE *\*strew-* (Wikt) | FITS: *reconstruct what happened* | — |
| `thread_read` | S6 | SHIPPED (TW owner?) | finding shape S0; gate and cost are TW's | *thread* ← OE *þrǣd* ← PGmc *\*þrēduz* ← PIE *\*terh₁-* (L *terō* a cognate); *read* ← OE *rǣdan* ← PGmc *\*rēdaną* ← PIE *\*Hreh₁dʰ-* (Wikt en; also carries root *\*h₂er-*; L *reor* is from *\*h₂reh₁-*, a reanalysed root of *\*h₂er-*: a cognate at the root, not an ancestor, Wikt la). Germanic | FITS as canon coinage | — |
| `trace` | S6 | PARKED (TW) | knot-mediated remote read | ME *tracen* ← OF *tracer*, *"probably a conflation of"* VL *\*tractiō* (← L *trahō*) and OF *traquer* ← *trac* (Germanic) (Wikt). **Mixed path** | FITS | — |
| `survey` | S7 | SHIPPED; Rung case REBUILD | `_mint_document` → `faction_sheet` (or `rung_sheet`, M7) in the surveyor's hold; content deposit | ME *surveyen* ← AN/OF *sourveoir, surveer* = *sour-/sur-* + *veoir* ← L *videō, vidēre, vīdī, vīsum* *"to see, perceive; to observe, note; to look out for, see to"* (Wikt) ← PIE *\*weyd-* (Wikt). **Wikt routes it through the OF compound, not ML *supervidēre*** (L-01's link `[UNVERIFIED]`). The *"oversee"* sense is AN `[UNVERIFIED]`; *"a count"* is the modern statistical sense, not the root (L-01 applied) | FITS: *survey the estate, the realm* | — |
| `audit` | S7 | FOLDED (survey) | survey of a Rung or office under the actor's purview | ← L *audītus* *"a hearing"* ← *audiō, audīre* *"to hear, listen to; learn by hearing"* (Wikt) ← PIE *\*h₂ew-* + *\*dʰeh₁-* (Wikt). Wikt: *"examinations were originally presented orally"* | FITS | — |
| `census` | S7 | FOLDED (survey; content label) | survey of a Rung → `rung_sheet` (persons, stores) | ← L *cēnsus* ← *cēnseō, -ēre* *"to give an opinion; judge; decree"* (Wikt) ← PIE *\*ḱens-* (Wikt; **disputed**) | FITS as a noun label; rare as a verb | — |
| `scout` | S7 | FOLDED (survey) | survey of a Rung the actor stands at; forces mustered in the sheet | ME *scout* ← OF *escoute* ← *escouter* *"listen"* ← L *auscultō, -āre* *"to listen; hear; heed"* (Wikt) ← *aus-* (cf. *auris*) + PIE *\*ḱlew-* *"hear"*, or *\*ḱel-* *"incline"* (disputed, Wikt la). The root sense is hearing, but fit is by usage | FITS: *scout the enemy camp* | `reconnoitre` (← F *reconnoître* ← L *recognōscere*, Wikt) declined: military register |
| `conceal` | S8 | PLANNED (IN-12 s10) → REBUILD | `cover` Record (`terms` = actor, M4 grade, scope); `anchor_of` | ME *concelen* ← OF *conceler* ← L *concēlō, -āre* *"to conceal carefully"* (Wikt) = *con-* + *cēlō, -āre, -āvī, -ātum*. L&S: *"to hide something from one, to keep secret, to conceal"*. ← PIE *\*ḱel-* *"cover"* (Wikt) | FITS | — |
| `disguise` | S8 | FOLDED (conceal) | cover with scope `room` | ME *disguisen* ← OF *desguiser* = *des-* (L *dis-*) + *guise* ← Frankish *\*wīsā* ← PGmc *\*wīsǭ* ← PIE *\*weyd-* (Wikt). **Latin only in the prefix** | FITS | — |
| `infiltrate` | S8 | NEW ROW | `oblige`'s duty edge, taken under a live cover | ← ML *infiltrātus* ← *infiltrō* (Wikt; no Latin entry) = *in-* + ML *filtrum* *"felt"* ← Frankish *\*filtir* ← PWGmc *\*felt* (Wikt en) ← PIE *\*pel-* (Wikt en *filter*). **A learned Medieval Latin formation on a Germanic loan** | FITS: *infiltrate a household* | — |
| `forge` | S9 | SHIPPED → REBUILD | `_mint_document` false sheet; writes `forgery_quality` (M4); emits `faction.surveyed` | verb: ME *forgen* ← AN *forger*, OF *forgier* ← L *fabricō*/*fabricor, -ārī, -ātus sum*. L&S: *"to make out of wood, stone, metal, etc., to frame, forge, construct, build"*. ← *fabrica* ← *faber* *"artisan, smith"* (Wikt). PIE **disputed**: Wikt *"no clear cognates"*, rival LIV/EIEC reconstructions, substrate proposed. **The noun path (*fabrica* → OF *forge*) is not the verb's** (L-11). The "counterfeit" sense is English `[UNVERIFIED: century]` | FITS: *forge a deed* | — |
| `destroy_record` | S9 | SHIPPED (dark) | `Record.exists` false | *destroy*: ME *destroyen* ← OF *destruire* ← VL *\*destrugō* ← L *dēstruō* (Wikt). L&S: *"to pull or tear down any thing built (opp. construo)"*. ← *dē-* + *struō* ← PIE *\*strew-* (Wikt). *record*: ME *recorden* ← OF *recorder* *"register, recall"* ← L *recordor, -ārī, -ātus sum* *"to think over, call to mind, remember"* (L&S) ← *re-* + *cor, cordis* ← PIE *\*ḱerd-* *"heart"* (Wikt) | STRAINED: CRUD compound (L-15) | none: no retrofit (§4) |
| `bribe` | S10 | NEW ROW | `transfer`'s write + an inducement deposit to the circle of two; M8 reader | ME *bribe* ← OF *briber* ← OF noun *bribe* (Wikt). Wikt's block traces it no further: **origin unknown, not Latin, no PIE root**. The OF noun's sense (*"a piece of bread given to a beggar"*) is `[UNVERIFIED]` | FITS | — |
| `suborn` | S10 | FOLDED (bribe content), PARKED J-C-6 | bribe whose paid-for act is unlawful | borrowed from AN *suburner*, MF *suborner* and L *subōrnō, -āre* (Wikt) = *sub-* + *ōrnō* *"equip"* (L&S: *"fit out, furnish, equip"*) ← *\*ōrdnō* ← *ōrdō* ← perhaps PIE *\*h₂er-* (uncertain, Wikt la). Wikt sense: *"to induce … to commit an unlawful or malicious act"* | FITS (legal register) | — |
| `blackmail` | S10 → SC | SC mode (threat) | a demand whose sanction is disclosure of a held finding | *black* + *mail* *"payment, rent, tribute"* ← ME *mal, male* ← OE *māl* ← ON *mál* *"agreement, speech"* ← PGmc *\*maþlą* *"meeting-place"* (Wikt en; *"more likely"* ranks this against McKay's Gaelic *blàthaich*, not the PIE); PIE **uncertain**: *\*med-* (Wikt en *blackmail* template) or *\*meh₂d-* (Wikt en *mail*). Originally Border and Highland protection tribute; *"Expanded c. 1826 to any type of extortion"* (Wikt). **Germanic** | FITS | — |

Event kinds renamed by this lane:
- `record.forged` → `faction.surveyed` (S9).
- An inquiry's refusal → `inquiry.refused`. Its Failure stays `finding.none` (M2).

Considered and declined:
- `spy` for `watch`. ME *spien* ← OF *espier* ← Frankish *\*spehōn* ← PGmc *\*spehōną* ←
  PIE *\*speḱ-*; L *speculor* is a cognate, not an ancestor (Wikt). Declined because it asserts a
  secrecy the row does not enforce.
- `consult` for `research`. It loses the forgery-detection sense.

---

## 3.5 Deduplication and culls

**Near-synonym groups and what was done:**

| group | finding | action |
|---|---|---|
| `survey` / `surveil` / `examine` (FI-G36, L-09) | Each takes a place, so the words alone do not separate them | Rename `surveil` → `watch`. Discriminators carried by the rows: `survey` **makes a document** of a standing state; `watch` reads **this season's** Events at a Rung and pierces covers; `examine` reads **the past** at the Rung where one stands |
| `examine` / `search` / *inspect* | one read, three selectors | `search` folded as a mode; *inspect* not used as a name (= `examine`) |
| `interview` / `interrogate` / *question* | *question* is the ordinary umbrella word | `interview` = consented questioning (FI); `interrogate` = custody and contest (SC). The fold test fails on M (§3.3 S4) |
| `shadow` / *tail* / `track` / `trace` | *tail* = `shadow` in ordinary use. `track` follows a trail after the fact. `trace` is TW's knot read. `track` and `trace` share OF *trac* (Wikt) | name *tail* culled (nothing dies: it is `shadow`); `track` a mode of `examine`; `trace` left with TW |
| `watch` / `guard` / `ward` (V-19) | `guard`/`ward` are Germanic doublets meaning "protect". `watch` yields knowledge and obstructs nothing | no merge; flagged to PC/TW so `ward` is not glossed "watch" |
| `conceal` / `disguise` / *hide* / *cover* | one cover Record; `disguise` = scope `room`; *cover* is the Record kind | `disguise` folded; *hide* not used as a row name |
| `forge` / *fabricate* / *counterfeit* | one act | `forge` only |
| `bribe` / `suborn` / *gift* / `transfer` | *suborn* names the aim (an unlawful act), `bribe` a means (V-05); a gift is `give`/`transfer` | `bribe` a row; `suborn` a parked content; no gift verb in FI |
| `scout` / *reconnoitre* / `survey` | *reconnoitre* = `scout`, in a military and British register | name *reconnoitre* culled; `scout` a mode of `survey` |
| `eavesdrop` / *overhear* / `intercept` | overhearing is free by presence today; `intercept` needs a Record in transit | `eavesdrop` a parked mode; `intercept` parked with no host |
| `reconstruct` / `construe` / `destroy_record` (V-19, all from *struō*) | homonymy at the root only: *interpret a writ*, *work out a deed*, *burn a document* are distinct in current use | no change (L-01: a root is not evidence) |

**Culls.** Only *names* are culled: *tail*, *reconnoitre*, *inspect*, *spy* (declined), *consult*
(declined). **No act is culled.**

**Floor check.** Nothing a floor act needs dies. Every floor act in §3.2 is kept as a row or a
named mode, or is placed with the lane that resolves it:

| floor act | where it lives |
|---|---|
| scout / survey | `survey` |
| search | `examine` |
| question | `interview` |
| interrogate | SC |
| observe | `watch` |
| shadow | a parked sibling row |
| infiltrate | a new row |
| forge | `forge` |
| conceal | `conceal` |
| bribe | a new row |
| blackmail | SC's threat |
| track | `examine` |

**v2 dispositions tested** (`_part8.md:449-457`):
- **V133 search → `examine`.** Upheld.
- **V134 track.** v2 merged it into `reconstruct`. **Rejected:** M ✗. Re-targeted to `examine`.
- **V135 eavesdrop CUT.** Rejected as a cut and **parked as a mode** instead. The cut is free
  today (presence delivers a confided telling, `witness.py` `_circle_of`). But v2's revival form
  (`conceal` + `move`) is a composition.
- **V136 decipher CUT.** Rejected as a cut; **folded and parked** on research.
- **V137 shadow.** v2 merged it into `surveil` as "a Person-bound sibling row". Upheld as a
  **sibling row** (M ✗ for a fold), parked.
- **V138 infiltrate CUT.** **Rejected**: the CUT form is a composition (instruction 5). It is a
  new row.
- **V139 disguise → `conceal`.** Upheld.
- **V140 bribe KEEP WITH CONDITIONS.** Upheld, with *"FA's `suborn` is the same act"* struck (V-05).
- **V141 audit → `research`.** **Rejected**: `research` writes no document. Re-targeted to `survey`.
- **V107 reconnoitre → `surveil`.** **Rejected.** Re-targeted to `survey` as `scout`.
- **V.2.14** *"a seventh inquiry would inherit the defect, not fix it, so none is added"*. The
  outcome holds (no seventh inquiry row) but for a different reason: the fold tests place each
  candidate as a mode. The defect itself is M1, not a reason to withhold names.

**Critic findings on FI verbs:**

| id | finding | result |
|---|---|---|
| L-01 | root sense used as design intent; *survey* "a count", *research* "go round again", *surveil* "keep awake over" | **Applied.** No claim here rests on a root. On *surveil*, L&S's first sense **is** *"to watch, i.e. to be or keep awake at night"*, so the critic's "attested 'keep watch'" is half right: L&S gives both. The paraphrase "keep awake over" still fails, because *sur- + veiller* is a French compound, not a Latin one. **Answered in part:** Wikt does not route *survey* through ML *supervidēre*, so the critic's link stays `[UNVERIFIED]` |
| L-09 | `survey`/`surveil` one letter apart, both on a Rung | **Applied**: rename to `watch` |
| L-11 | `record.forged` leaks; the proposal's "THIN, effect declined" is stale; forge's noun path | **Applied**: emit the twin kind; the effect is built (:330-348); the verb path is via *fabricō* |
| L-12 | stale lexicon | **Applied**: every row here was checked against `verb_table.yaml` this session |
| L-13 | *utter* is "uttering a forged instrument" | **Answered**: a forgery is planted by `give` (:334), not `utter`; no FI change |
| L-15 | `create_record`/`destroy_record` are CRUD names | **Answered**: noted, not applied (no retrofit, §4); IN's question |
| L-16 | *reconstruct* is not a Latin compound | **Applied** in §3.4 |
| L-02 | `oblige` runs the opposite way to ordinary English | **Answered for FI**: `infiltrate` builds on `oblige`'s write, not its name; a rename to `pledge` leaves it unaffected |
| V-05 | bribe ≠ suborn | **Applied** |
| V-06 | voice: the subject of *hire* is the employer | **Checked for FI**: `infiltrate`'s actor is the infiltrator and `bribe`'s is the payer; both are in the actor's voice |
| V-12, V-13 | §IV.4 root glosses (*research* "seek closely", *surveil*) | **Applied** (§3.4 gives the attested senses) |
| V-19 | *construe/reconstruct/destroy* from *struō* | **Answered**: no change (table above) |
| V-20 | *yield* homonymy (`Rung.yield`, duel `yield`, "inquiry yield") | **Applied**: this lane calls the product a **finding** and coins no kind with *yield*. Recommend the rewrite do the same |

**v2 NAME-DEFECT (FI-G37, v2 `_part6` test 9) verified.** It has two halves.
- *"`survey` writes a Record rather than informing the surveyor"* is **false at HEAD**. The
  surveyor holds the sheet, and WITNESS deposits its content on the hold opened this tick
  (`witness.py:397-421`; the beneficiary note at verb_table.yaml:970: *"its content lands in HIS
  ledger at WITNESS"*). The name predicts the effect: a survey yields a written survey and its
  reader knows it.
- *"The six yield no finding's content"* is **true**, but it is a missing producer (M1), not a
  naming defect. No rename follows from it.

---

## 3.6 Gap coverage table

One disposition per row. Mechanics M1-M10 are in §3.7.

| gap | closed by | PARKED (trigger) | OUT OF SCOPE | STALE | DISPUTED |
|---|---|---|---|---|---|
| FI-G01 | S1-S5 inquiries once **M1** (the finding producer) | | | | |
| FI-G02 | `research` once **M1** (consult deposit) | | | | |
| FI-G03 | `survey` once **M7** (sheet readers; `rung_sheet`) | | | | |
| FI-G04 | `examine` once **M1** (log at the Rung) | | | | |
| FI-G05 | `examine` REBUILD (Rung binding, S1) | | | | |
| FI-G06 | `watch` once **M1** | | | | |
| FI-G07 | | `shadow` sibling row; trigger: a co-movement write | | | |
| FI-G08 | `reconstruct` once **M3** (candidate set) | | | | |
| FI-G09 | `reconstruct` REBUILD (an attribution claim is new information) | | | | |
| FI-G10 | `examine`, `research`, `reconstruct` once **M3** | | | | |
| FI-G11 | all inquiries once **M2** (`inquiry.refused` ≠ `finding.none`) | | | | |
| FI-G12 | **M2** + H-111 answered by ladder step 5 (S0) | | | | |
| FI-G13 | **M2/M3**: Failure deposits a misreading or the attempt is news, and no inquiry is gated by attribute (S6 rule) | | | | |
| FI-G14 | all inquiries once J-T1 rules a stored score (v2 `_part7.md:87`, via register) | | | | |
| FI-G15 | | | | | The finding is an effect-side deposit with its confidence set by degree. Competence enters at the roll, so AX-7 layer 2 is not needed for an inquirer's own finding |
| FI-G16 | `examine`, `research`, `watch` once **M4** | | | | |
| FI-G17 | | non-oppositional Depth modifier; trigger: a matter carrier with a depth field (the oppositional half closes under G16) | | | |
| FI-G18 | rule: **no inquiry carries an attribute gate** (S6); TS stays TW's one class gate | | | | |
| FI-G19 | `interview` once **M5** (reply read; §3.9 J1) | | | | |
| FI-G20 | `interview` REBUILD (`counterparty:` clause; approach stays payload) | | | | |
| FI-G21 | `interview`: the Lattice is its front end (Q4 honoured; M5 is what it drives) | | | | |
| FI-G22 | `reconstruct` REBUILD (Ob = base − supporting claims; no GM scope) | | | | |
| FI-G23 | `research` once **M4** (forgery read) | | | | |
| FI-G24 | `forge` REBUILD (writes score/2, landing with G23) | | | | |
| FI-G25 | `destroy_record` once **M6** (`hold:` eligibility typed) | | | | |
| FI-G26 | `conceal` (PLANNED, IN-12 step 10) | | | | |
| FI-G27 | `disguise` (`conceal` scope `room`) | | | | |
| FI-G28 | `conceal` (degree-keyed cover break) + `watch` (pierce) once **M4** | | | | |
| FI-G29 | S0: the attempt is news (M2 and H-111), with no Exposure meter | | | | |
| FI-G30 | `infiltrate` (NEW ROW) once `conceal` lands | | | | |
| FI-G31 | | `decipher` mode; trigger: a Record kind with a cipher grade | | | |
| FI-G32 | | `eavesdrop` (trigger: private whispers); `intercept` (trigger: a Record in transit) | | | |
| FI-G33 | `search` (mode of `examine`) once **M6**; the warrant half is `seize`'s (shipped) | | | | |
| FI-G34 | `research` once **M6** (`hold:<dispensation>` access) | | | | |
| FI-G35 | `survey` with `audit`/`census`/`scout` once **M7** | | | | |
| FI-G36 | rename `surveil` → `watch` + discriminators (§3.5) | | | | |
| FI-G37 | | | | | Half false (survey informs its holder, `witness.py:397-421`); half is FI-G01's yield defect, not a name defect (§3.5) |
| FI-G38 | modes named under M1: search, track, audit, scout (folded); shadow parked; trace TW | | | | |
| FI-G39 | | | `interrogate` is SC's row (IN-12 step 5); FI supplies the confession as a finding | | |
| FI-G40 | dedup (§3.5): consent vs custody and contest | | | | |
| FI-G41 | `bribe` (NEW ROW) once **M8** | | | | |
| FI-G42 | `watch` (cover pierce) + `conceal` once **M4** | | | | |
| FI-G43 | | | the seam and role registration is architecture, not a verb; the verbs here need no seam (`requirements.yaml:178-179`, "its own thing") | | |
| FI-G44 | | | | | Rolling a pool against an Ob through the one dice owner is not a contest. No prize is declared, so there is no breach; one roller is S's *"consistent in methodology"* |
| FI-G45 | all inquiries once J-T1 (pool) and **M4** (Ob) | | | | |
| FI-G46 | **M1**: one reliability ladder (degree → confidence; source → H-199's remove ordinal); the archived tags retire | | | | |
| FI-G47 | **M1** (a finding carries its proof kind) once **M9** (SC's `determine` reads `proofs`) | | | | |
| FI-G48 | | | the charge or accusation is SC's (`utter`/`petition`/`open_case`) | | |
| FI-G49 | | | presentation (case board, UI); the ledger is the data | | |
| FI-G50 | `examine`: the read window bounds a trace's age, so no per-kind decay map is needed | | | | |
| FI-G51 | | scheme secrecy; trigger: a conspiracy carrier (SC/FA `conspire`) | | | |
| FI-G52 | `examine`, `interview` alignment cells (v2 B5); `watch` null by ruling (`rosters.yaml:2348`, via register) | | | | |
| FI-G53 | `examine` REBUILD (Rung; documents are `research`'s) | | | | |
| FI-G54 | `track` (mode of `examine`) once **M1** | | | | |
| FI-G55 | | | TW's knots lane | | |
| FI-G56 | S1-S5 once **M1** + **M2** (a graded finding lets `requirements.yaml:169-172` flip) | | | | |
| FI-G57 | `examine` REBUILD: the past at a place is a finding no other act gives | | | | |
| FI-G58 | **M1** once **M9** (SC reads a held finding as a contest input) | | | | |

Count (58 rows, checked by grep):

| disposition | rows |
|---|---|
| closed by a verb or suite | 45, of which 27 wait on a named mechanic (§3.7) or a named ruling (J-T1) |
| parked | 5 (G07, G17, G31, G32, G51) |
| out of scope | 5 (G39, G43, G48, G49, G55) |
| disputed | 3 (G15, G37, G44) |
| stale | 0 |

The register's freshness notes, the `forge` effect and the Rung subject on `survey`, were already
applied at HEAD and change no disposition.

---

## 3.7 Mechanics this subsystem needs (named gaps)

| # | mechanic | what it must write | verbs waiting |
|---|---|---|---|
| M1 | **the finding producer**: a per-verb selector over the world at the act's subject (the S0 table) | Claims in the actor's ledger: value from the selector, confidence from degree, source `found`; and a consult deposit for a Record not held | `examine` (+search, track), `research`, `watch`, `reconstruct`, `interview` (with M5) |
| M2 | **Failure ≠ refusal** | refusal → flat `inquiry.refused`; Failure → `finding.none` and only the S0 deposit | all six inquiries; `thread_read` |
| M3 | **the honest misreading** | on Failure, a `who` drawn from the inquiry's own candidate set, excluding the true one | `reconstruct`, `examine`, `research` |
| M4 | **the concealment grade**: the concealer's score/2 on the concealed object (Q1) | `cover` grade; `Record.forgery_quality`; a hidden store's grade (EC). Read as the Ob by every inquiry that meets it | `conceal`, `forge` (writers); `examine`, `research`, `watch`, `reconstruct` (readers) |
| M5 | **the reply read** for `interview` (§3.9 J1) | `told` claims with the questioned person as teller; the question deposited with him | `interview` (and the Lattice) |
| M6 | **`hold:<object>` eligibility typed** (H-75) | nothing new; an eligibility alternative that evaluates | `destroy_record`, `research` (archive access), `search` under warrant |
| M7 | **`rung_sheet` and the sheet readers** | a Record kind for a place's state (holder, persons, stores, forces); decision reads of `members`/`holdings`/`seats` | `survey` (Rung), `audit`, `census`, `scout` |
| M8 | **the inducement reader** | the inducement deposit (circle of two) and a payee-side CHOOSE weight on the paid-for act | `bribe` (and `suborn`) |
| M9 | **SC's evidence read** (SC-owned) | `determine` and contests read held findings by proof kind | FI-G47, G58 |
| M10 | **a co-movement write** | the actor's season ends where the subject's moves end | `shadow` |

---

## 3.8 Cross-subsystem flags

| other lane | verb or fold | the collision or dependency |
|---|---|---|
| **SC** | `interrogate` | SC's row (IN-12 step 5; `arrangements.yaml:204`). FI's floor act lives there; its confession is an FI finding (proof `confession`) |
| **SC** | `blackmail` | a mode of SC's threat host (sanction = disclosure of a held finding). FI defines the *secret* (a finding about a covered deed); no carrier is needed. If SC has no threat host, `blackmail` is a NEW row in SC, not a composition |
| **SC** | `suborn` (by threat) | the same unlawful-act content on the threat host; gated on J-C-6 with `bribe`'s |
| **SC** | forgery reader | SC-02 `22b` step 25's examination (H-210 owner) and FI's `research` must call **one** M4 rule; two readers of `forgery_quality` would be two owners |
| **SC** | M9, FI-G48 | the accusation and `determine`'s reading of `proofs` are SC's; FI writes the finding with its proof kind |
| **TW** | `thread_read`, `trace` | owner to be reconciled. FI's share is the finding shape (M2, M4); TW's is the TS gate (H-85), the Coherence cost and the knots |
| **TW / PC** | `watch` vs `ward` / `guard` | Germanic doublet risk (V-19); keep `ward` from being glossed "watch" |
| **EC** | `bribe` | composes on `transfer`'s write and shares its `transfer.made` kind. That makes `transfer.made` map to no single verb (`data/verbs.py:1233-1248`), a cost EC should accept or answer with D-V6's `(verb, kind)` key |
| **EC** | `search` | a concealed store (hoard, smuggling) is a `search` target; EC writes its M4 grade |
| **NP / FA** | `infiltrate` | built over `oblige`'s write (L-02 rename to `pledge` does not affect it); FA's covert bodies (Riskbreakers) are its demand |
| **GV** | `audit`, `census` | modes of `survey`; purview (`governors_of`, `state/gate.py::purview_reaches`) decides an audit's subject |
| **MB** | `scout` | a mode of `survey` (a Rung the scout stands at; forces mustered in the sheet); MB's pre-battle intelligence reads it |
| **WT** | `track` | FI's `track` is a mode of `examine` (a person's trail). Hunting game is WT's `hunt`; if WT wants animal tracking, it shares the `examine` read, not a second one |
| **IN** | `destroy_record`, `create_record`, M6 | CRUD names (L-15); H-75's `hold:` eligibility; the `any` combinator (K-16) is no longer needed by FI (`shadow` is a sibling row) |
| **all lanes** | event kinds | the rule this lane applies: **a deceptive act emits its honest twin's kind** (`forge` → `faction.surveyed`; `bribe` → `transfer.made`), so a witness's deed judgement cannot see through it. Other lanes with covert acts (`assassinate`, `smuggle`) should follow one rule |

---

## 3.9 For Jordan

Ladder tried first on each (CLAUDE.md §0: superseded, irrelevant, design document, precedent,
architecture). Everything else in this file was answered by one of those steps.

**J1 · How does the questioned person answer an `interview`?** This survives all five steps,
because each answer overwrites ratified Layer-1 architecture or changes the game's rhythm.
- **(a) A Layer-1 carve-out.** The fold reads the questioned person's ledger, restricted to claims
  on the topic and filtered by his stance toward the asker. The asker gets his answer in the same
  season. This widens F8's *"the ACTOR'S OWN ledger … and no other"* (verb_table.yaml:1163 note).
- **(b) The reply as the questioned person's own act.** `interview` deposits the question with
  him, and he answers, evades or lies by his own choice next season.
  - This keeps F8.
  - Testimony arrives a season late, and refusal becomes his deliberate act.
  - It is not the composition instruction 5 forbids, because `interview` writes its own effect,
    the question asked.
- Q4's Lattice (*"Lattice first"*) runs on either.
- **Recommendation:** (b). It needs no architectural exception, and it gives the interviewee a
  real choice. `[CONFIDENCE: medium]`

