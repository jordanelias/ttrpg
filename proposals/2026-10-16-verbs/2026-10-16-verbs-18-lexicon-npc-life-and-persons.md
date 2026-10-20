# Verbs, v2 — part 18: Part VI.10, NPC life and persons (NP)

## Status: PROPOSED (2026-10-17). Reference, not canon (`CLAUDE.md` §0.05): nothing here binds the game or is read by it. Merging ratifies nothing unless Jordan so rules. Static reading and static lookup only; no run.
## Parts, in reading order: [head](2026-10-16-verbs-01-thesis-and-persons.md) (§0, Part I Persons) · [`verbs-02`](2026-10-16-verbs-02-attributes.md) (Part II Attributes) · [`verbs-03`](2026-10-16-verbs-03-standards-roster-and-reconciliation.md) and [`verbs-04`](2026-10-16-verbs-04-critics-etymology-gaps-and-decisions.md) (Part III Verbs: standards, roster, reconciliation; critics, etymology audit, gap coverage, named mechanics, decisions) · [`verbs-05`](2026-10-16-verbs-05-what-verbs-do-to-the-world-1.md) and [`verbs-06`](2026-10-16-verbs-06-what-verbs-do-to-the-world-2.md) (Part IV What verbs do to the world) · [`verbs-07`](2026-10-16-verbs-07-roadmap-reliability-and-sources.md) (§5 Roadmap, §6 Reliability ledger, §7 Sources) · [`verbs-08`](2026-10-16-verbs-08-engine-findings-from-the-first-trial.md) (Part V: engine findings carried from the first-pass trial) · Part VI, the lexicon by subsystem: [`verbs-09`](2026-10-16-verbs-09-lexicon-personal-combat.md) PC · [`verbs-10`](2026-10-16-verbs-10-lexicon-mass-battle.md) MB · [`verbs-11`](2026-10-16-verbs-11-lexicon-social-contest.md) SC · [`verbs-12`](2026-10-16-verbs-12-lexicon-fieldwork-and-inquiry.md) FI · [`verbs-13`](2026-10-16-verbs-13-lexicon-threadwork.md) TW · [`verbs-14`](2026-10-16-verbs-14-lexicon-settlements-and-governance.md) GV · [`verbs-15`](2026-10-16-verbs-15-lexicon-faction-actions.md) FA · [`verbs-16`](2026-10-16-verbs-16-lexicon-economy-trade-and-craft.md) EC · [`verbs-17`](2026-10-16-verbs-17-lexicon-world-travel-and-survival.md) WT · **this file** NP · Part VII, the verb gap register (the evidence behind Part VI's coverage tables): [`verbs-19`](2026-10-16-verbs-19-gap-register-pc-and-np.md) PC+NP · [`verbs-20`](2026-10-16-verbs-20-gap-register-mb-and-fa.md) MB+FA · [`verbs-21`](2026-10-16-verbs-21-gap-register-sc-and-gv.md) SC+GV · [`verbs-22`](2026-10-16-verbs-22-gap-register-fi-and-tw.md) FI+TW · [`verbs-23`](2026-10-16-verbs-23-gap-register-ec-and-wt.md) EC+WT.

**How to cite this Part.** The lane's own sections are numbered 3.1 to 3.9; cite them as `NP §3.n` (for example `NP §3.9` for its items for Jordan). Gap ids (`NP-G01` …) resolve in Part VII (`verbs-19`). Abbreviations such as `VT`, `VCD`, `v2-p3` are defined in the lane's opening paragraphs; `v2-p3`, `v2-p4`, `v2-p8` are the first-pass v2 parts as filed at `716c253`. Old file names such as `…synthesis_part8.md` or `_part8` in the body also mean those first-pass files; the suite was later renamed `2026-10-16-verbs-NN-…`. Mechanic ids (`M1`, `M-1`, `M-WT-1`) are this lane's own.

**Rulings that override this section** (`verbs-03` §III.5; where this section and the roster disagree, the roster governs):

- R-01: `hire` is **EC's** row; NP uses it. `recruit` is FA's.
- R-02: `knot` is **TW's**; NP keeps `tie`.
- R-11: `succeed` is **GV's** row; NP consumes it.
- R-10: `oblige` → `pledge` is adopted as a proposal in the single rename batch.
- R-16: `release` stays; `renounce` is not adopted now.
- R-18: `drill` (MB, a stock) and `train` (a person) are two rows.

---

# NP — NPC life and persons

Lane file for the v2 rewrite (`proposals/2026-10-16-verbs/*.md`, Part III and
Part V). Subject: persons as actors on other persons and on themselves. Gap rows NP-G01…NP-G41 of
Part VII (`verbs-19`). Built 2026-10-16 from the working tree. Nothing in the repo was edited.

Abbreviations as the register's: `VT` = `engine/season/verb_table.yaml`; `VCD` =
`proposals/2026-10-03-verb-coverage-and-gap-fill.md`; `WP5` = `workplans/valoria_master_workplan_v9_part5.md`;
`v2-p4`/`v2-p8` = the v2 `_part4`/`_part8` files (first-pass); `NPL` = `research/by_lane/NPC_npc_cast.md`;
`RTP` = `research/rise_to_power_roster_system_research_v1.md`; `PGC` =
`research/valoria_game_precedent_companion_v1.md`; `GEP` =
`proposals/2026-09-05-proceedings-subsystem/relay/G_EMERGENCE_PRECEDENT.md`. Etymology sources: **Wikt**
(en.wiktionary, via the lane tool), **L&S** (Lewis & Short via the tool). Every chain link not shown by
the tool is tagged `[UNVERIFIED]`.

---

## 3.1 Subsystem mechanic

**Carriers (all on `Person`, `engine/season/state/carriers.py:645-709`).** `body` (falls only), `born`
(age is a Query), `capability` (dict; no verb writes it), `stance` (rows `(referent, valence, weight)`:
the stored half of regard and the grudge store), `pursuits`, `conviction`, `scar`, `ledger`, `tenures`.
Person-to-person Tenure kinds `tie`, `knot`, `succeed`, plus `commit`/`oblige` toward Propositions and
seats (`engine/season/rosters.yaml:101-124`).

**Readers.** `queries/person_q.py`: `stance_toward` (`:67`), `deed_valence` (`:314`; `PAIRED_KINDS` at
`:139` are unjudged), `regard` (`:336`: stored stance + judged deeds + told valence).
`decision/options.py::teller_weight` reads regard.

**Writers today.** `body` falls in `loop/effects_combat.py:154, :295-297` and MATTER subsistence;
`loop/matter.py::_crossings` (`:35`) reports downward crossings only (H-211). `stance` is written at
runtime only by `_eff_march` (`effects_combat.py:304`), plus seeders (`harness/populated.py:624, :1049`).

**Shipped NP rows.** `give` (`VT:413`, a Record's `hold`, giver closes and receiver opens);
`commit` (`VT:128`); `oblige` (`VT:758`, the joiner binds himself to a seat); `release` (`VT:845`,
domain `[hold, commit, oblige, succeed, tie, knot]`, `:851`). Two rows are **declined**: `succeed`
(`VT:952`: no reader, no heir operand) and `tie / knot` (`VT:1245`: no partner operand; `tie`
unread).

**Absent.** `tend`, `train` and `forgive` have no row and no effect. A grep of `engine/` for
`_eff_tend|_eff_train|_eff_forgive|body.tended|capability.raised` returns nothing. They are planned at
IN-12 steps 9 and 13 (`WP5:54-71`). Also absent: a raiser of `body`, a writer of `capability`, a closer
of `stance`, a kin carrier, a child carrier, and the heir's claim (IN-61, `WP5:211`).

---

## 3.2 Convention floor

Status key: *shipped* (row in `VT`), *planned* (workplan position), *designed* (v2/VCD only), *absent*.

| floor act | precedent | status |
|---|---|---|
| **tend** a wounded or sick person | Pendragon [MEMORY]: the First Aid and Chirurgery skills restore lost hit points, and natural healing runs in the Winter Phase. Mount & Blade [MEMORY]: the Surgery and Medicine skills raise wound-recovery and survival rates. Crusader Kings 3 [MEMORY]: the court physician treats a character's wounds and disease. In-tree: VCD fam. 45 "Heal, rest" GAP (`VCD:4500`); six cases ask for it (VCD §9.4 `tend`). | planned (IN-12 step 9) |
| **train** a person (self or pupil) | Crusader Kings 3 [MEMORY]: a guardian educates a child and the education trait is the outcome. Mount & Blade [MEMORY]: the Trainer skill gives party members experience. In-tree: RTP:114-116 (B2, "tutoring investment"). | planned (IN-12 step 9) |
| **give** a gift or a holding | Crusader Kings 3 [MEMORY]: the "Send Gift" interaction (gold for opinion). Mount & Blade [MEMORY]: gifts raise a lord's relation. In-tree: cession is "the one consensual route by which title moves" (`WP5:70`, `give` + Rung). | shipped (Records only); Rung widening planned (IN-12 B-R) |
| form a personal **bond** (friend, rival, sworn brother) | KOEI RoTK [MEMORY + in-tree]: officer oaths and bonds (Liu, Guan and Zhang; Lü Bu), NPL:152. Crusader Kings 3 [MEMORY]: the Befriend scheme makes a friend, and rivals are a typed relation. In-tree: GEP:117 (typed, persistent relationship records in 6 of 8 games). | shipped row, declined (`tie / knot`, H-182); IN-32 planned |
| **marry** (alliance by marriage) | Crusader Kings 3 [MEMORY]: "arrange marriage", where a marriage between houses makes an alliance. Pendragon [MEMORY]: a knight marries for land and heirs in the Winter Phase. Birthright [MEMORY]: a regent's bloodline and heirs carry the domain. In-tree: RTP:156-182 (Category C, C1-C5: Habsburg, Fujiwara, damat, Woodville, Han consort clans). | designed (v2 V171 PARK) |
| **forgive** (end one's own grudge) | In-tree: GEP:130, the failure mode "Escalation with no terminus or release valve"; VCD §9.4 `forgive` evidence (Bannerlord feud F36, RimWorld insult spiral). Mount & Blade: Bannerlord [MEMORY]: an execution starts a lasting relation penalty with the victim's clan. | planned (IN-12 step 13) |
| the heir **succeeds** to a vacant seat | Crusader Kings 3 [MEMORY]: the primary heir takes the titles at the holder's death under the succession law. Pendragon [MEMORY]: the heir inherits the manor. In-tree: IN-61 (`WP5:211`), RS-27/RS-29. | planned (IN-61) |
| **pledge** service or fealty to a lord or seat | Crusader Kings 3 [MEMORY]: vassals swear fealty and owe levies and taxes. In-tree: NPL:70 (patronage both ways, *clientela*). | shipped as `oblige` (misnamed, L-02) |
| **hire** a person for pay (retainer, companion, servant) | Mount & Blade [MEMORY]: companions are hired in taverns for a fee and wage. In-tree: PGC:285-290 ("Recruitment costs consent, not only money", JA2, RoTK VIII). | absent (v2 folded it into `oblige`, V-06) |
| **defect** (change sides) | KOEI RoTK [MEMORY]: an officer with low loyalty defects when an enemy approaches him. Mount & Blade: Bannerlord [MEMORY]: a lord leaves his kingdom and joins another. In-tree: NPL:152 (Lü Bu), NPL:73 (Woodville cascade). | absent (composed from `release` + `commit`, NP-G24) |

**Beyond the floor, judged on NERS.** These are confess, court, consecrate, rear, mourn, pray, avenge,
betray, reconcile and designate. Births and **rear** would be floor in a **dynastic** game (Crusader
Kings 3 [MEMORY]: children are born and educated). Valoria has ruled heirship to be a title (RS-27, and
the carrier RS-29, quoted at `WP5:211`), and the cast-size and generation ruling ED-WR-0011 is still
open and `needs_jordan` (`registers/editorial_ledger_wr_archive.jsonl`). So children are not floor
here today. See §3.9.

---

## 3.3 Suites

Each suite applies the fold test as three questions: **A** (same actor?), **M** (same subsystem
mechanic?) and **P** (does it differ only in a parameter or its content?). A fold passes only on
yes/yes/yes (Part III §III.0 pt 5). NERS is judged from six directions: top-down (TD), bottom-up (BU),
vertical (V), diagonal (D), lateral (L) and horizontal (H).

### Suite A — Care. Host: `tend`

* **Folded acts.**
  * `heal`: A yes · M yes · P yes. The healer is the tender, and the effect is the same raise of
    `body`. *Heal* names the outcome (VCD §9.4 `tend`: "refused on direction 3's logic, as `kill` is"),
    so it is a name for the act, not a second act. FOLD.
  * `recover` (active, "he rests and recovers"): A yes · M yes · P yes (`subject` = the actor). FOLD,
    provided the row admits a self-subject (v2-p8:538, :931; VCD's cell asks `relation` of `subject`,
    `with`, and whether a person is `with` himself is [UNVERIFIED]).
  * `recover` (passive, healing over time): **not an act.** It is a MATTER rising arm. v2-p8:538 records
    it as "shipped at a 0 control" [UNVERIFIED: no rising writer was found by the grep in §3.1]. Named
    mechanic **M1**.
* **World effect.** Writes `Person.body` upward (the matrix row admits RES, per VCD §9.4); emits
  `body.tended`; refusal `tend.refused`.
* **What it still lacks.**
  * An upward band crossing. `_crossings` (`loop/matter.py:35`) is downward-only (H-211), so a risen
    body crosses no band anyone witnesses (**M1**).
  * A degree. VCD gives `contests: none`, but the floor games roll care (Pendragon's First Aid
    [MEMORY]), so the tender's skill should set the obstacle once `train` writes a care capability
    (**M2**).
* **NERS.**
  * **N.** BU: the only act that raises `body`. A grep finds no writer except falls (`effects_combat.py:154, :295-297`). TD: a body that only falls is a ratchet (H-211), and NPL reports "five of six heads die in two seasons" (NP-G06). L: PC `fight` and MB `march` write wounds and nothing answers them. D: v2-p6:64's HEALER role has no act. **What dies on a cut:** every wound becomes permanent. **False N-line check:** nothing else raises `body`, so the cut is not free.
  * **R.** Gives the player a protector strategy. It is also R-WORLD: a wounded head recovers or dies with no player present. Complete at the extreme only if a tend on the dead is refused (the `existence` of a live subject).
  * **S.** The same fixed-point `condition_scale` as `Site.condition` (`carriers.py:665-669`), so `restore` (Site) and `tend` (Person) share one ladder and are split by object kind, which ordinary English also splits. It pauses at RESOLVE like every act.
  * **E** (scored last). One row writes one field in one direction, and two names fold in. N and R are high and the overhead is low, so E passes.
* **Precedent.** §3.2 row 1.
* **Gaps.** Closes NP-G11 and NP-G12 (the names; the crossing waits on M1). Cross-reference PC-G39. Leaves
  open M1 and M2.
* **Disposition.** `tend`: **NEW ROW** (planned, IN-12 step 9, `WP5:54-71`). `heal` and `recover`:
  **FOLDED**.
* **Falsifier.**
  * For the KEEP: a shipped verb found to raise `Person.body` would make `tend` redundant.
  * For the effect: `Person.body` rises with a `tend` among its causes in `w.log` (VCD §9.4).

### Suite B — Formation. Host: `train`

* **Folded acts.**
  * `study`: A yes · M yes · P yes (`subject` = the actor). FOLD (v2 V177). The row must not refuse a
    self-subject (v2-p8:537).
  * `teach`: A yes · M yes · P yes (`subject` = a pupil). FOLD. VCD §9.4: "`train` … covers self and
    pupil, where *practise* covers only self."
  * `drill`, the **person** half: A yes · M yes · P yes. FOLD (v2 V117).
  * `drill`, the **troop** half (a body's quality): this is M no. It is the troop stock's mechanic, so
    it goes to MB (§3.8).
* **World effect.** Writes `Person.capability` (the retired matrix row is returned with its producer,
  VCD §9.4); emits `capability.raised`; refusal `train.refused`.
* **What it still lacks.**
  * A source of capability keys and magnitudes: J-13's remainder. Only `copying` exists, in one case
    (`WP5` IN-12 step 9, NPC-088) (**M3**).
  * A reader in combat (PC-G15) and in choice (NP-G15) (**M4**). Without them `train` is ID-13, a
    write nothing reads.
  * The P-08 bound. It holds **structurally**, not in prose: the row ranges over `verb_capability` keys,
    and Thread Sensitivity has no carrier (H-85, VCD §9.4). It must stay outside that roster, and the
    loader is the place to refuse it (K-20).
* **NERS.**
  * **N.** BU: the only development of a person ("NOTHING creates or develops a person", VCD citing `requirements.yaml:76-77`). TD: R-09's by-person pool. L: PC reads no capability today (PC-G15), so N is **narrowed** until M4. **False N-line check:** the capability authored at creation (IN-47) is not development, so the cut is not free.
  * **R.** The floor's customisation half: the player shapes a person.
  * **S.** "`capability` supplies dice and GATES NOTHING" (`VT:33-35`), so train adds dice and opens no new gate. That is one acquisition layer (`proposals/2026-09-30-character-and-play-surface/10_verbs_and_attributes.md:200`, V-4).
  * **E.** One field, two named folds. It passes only if M4 ships with the row.
* **Precedent.** §3.2 row 2.
* **Gaps.** Closes NP-G13 (once M3 exists) and NP-G14 (the P-08 bound, structural). NP-G15 waits on M4.
  Closes the development half of NP-G41.
* **Disposition.** `train`: **NEW ROW** (planned, IN-12 step 9). `study`, `teach` and `drill` (person):
  **FOLDED**.
* **Falsifier.**
  * For the KEEP: a run with `train` executed where `sigma._pool_of` does not vary by person shows the
    row inert.
  * For the effect: `sigma._pool_of` varies by person after a `train` (VCD §9.4).

### Suite C — Grievance. Host: `forgive`

* **Folded acts.** None passes the test.
  * `reconcile`: two actors each `forgive`, and optionally a `tie` (VCD:1231). That is A no and several
    steps, so it is not a fold. It is an outcome of two acts. **CULLED** as a verb name.
  * `avenge` / `retaliate`: the act is `fight`, `march` or `challenge` (PC, MB), chosen *because of* a
    grudge. Fold into `forgive`: A no. There is **no avenge mechanic distinct from those acts**, and the
    missing piece is a reader. IN-58's M-polarity reading found that `legacy` and `regard` turn no
    negative stance into a hostile top candidate, and only H-194's `declared` arm does (`WP5` IN-12
    step 5, blocker (1); ED-IN-0296). **CULLED** as a verb; the reader is **M6**.
* **World effect.** Removes the actor's own rows toward `subject` with valence < 0; emits `stance.moved`;
  refusal `forgive.refused` (VCD §9.4).
* **What it still lacks.**
  * A source of Proposition referents, without which a computed forgive of a *field* grudge cannot form
    (NP-G17, K-49) (**M5**).
  * The realm fights 0 fields, so no field grudge exists yet (`WP5` step 13).
* **NERS.**
  * **N.** BU: the only closer of a stance row, since `release` closes Tenures, not stance. TD: "A state nobody can end is AX-6's own named cost" (VCD §9.4); GEP:130, "Escalation with no terminus or release valve". L: `march` writes grudges today, and PC `fight` will once IN-58 and IN-70 land. **False N-line check:** eviction ends only the *judged* half of regard (ledger claims, NP-G18). The *stored* half has no other closer, so the cut is not free.
  * **R.** Mercy becomes a strategy, and feuds end in the world unattended.
  * **S.** One own-state decline beside `release`'s hook; no new ladder; it removes rows rather than writing a second quantity.
  * **E.** One row, no operand beyond `subject`. Passes.
* **Precedent.** §3.2 row 6.
* **Axis against `pardon`** (NP-G19). `forgive` ends **my** grudge. `pardon` is an authority remitting
  **another's** `detain` or `ban` through a seat (VCD §9.4 CONFLICTS). Ordinary English draws the same
  line, so the pair is not a duplicate. `pardon` belongs to GV/SC (IN-12 step 5) (§3.8).
* **Gaps.** Closes NP-G16, NP-G18 and NP-G19. Closes NP-G17 once M5 exists. NP-G20 (avenge) and NP-G21
  (reconcile) are culled, with M6 named.
* **Disposition.** `forgive`: **NEW ROW** (planned, IN-12 step 13). `reconcile` and `avenge`:
  **CULLED**.
* **Falsifier.**
  * For the KEEP: a writer other than `forgive` found to remove stance rows would make it redundant.
  * For the effect: after a hand-built `field.lost`, `forgive` leaves `stance_toward(p, F) == 0` with
    `stance.moved` in `w.log` (`WP5` step 13).
  * For the CULLs: a case where vengeance needs a world effect that `fight`, `march` or `challenge` does
    not write would revive `avenge`.

### Suite D — Bonds. Host: `tie` (split from `tie / knot`)

* **The split (caution 1).** The row names two Tenure kinds for one opener (VCD K-24, "the ROW is a
  MISFIT"). The tree shows two mechanics:
  * `knot` is fieldwork's Knot: formation, a strain gauge, rupture, Distant/Close tiers
    (`systems/fieldwork/sim/knots.py:1-40`). It has a live reader in WITNESS, which deposits a partner's
    sightings to a knotted person (`loop/witness.py:464-477`).
  * `tie` is a regard edge ("A tie is a **regard**", `architecture/meta/01_AXIOMS.md:1291-1292`). Its
    candidate reader is `teller_weight`'s relation term (`VT:1245`).
  * Fold `knot` into `tie`: A yes · M **no** (strain, rupture and a witness channel) · P no. **SPLIT.**
    `knot` moves to FI, whose IN-32 is FI-05 (`WP5:107`); flagged in §3.8. `tie` stays in NP.
* **Folded acts into `tie`.** None named.
  * `court`: A yes · M **no**. Courtship is a contest for another's consent (an SC mechanic), and `tie`
    is unilateral. **PARK**. Trigger: the `marry` row exists and SC exposes a contest whose stake is a
    counterparty's consent. Owner when built: SC.
* **World effect.** Opens a directed `tie` Tenure owned by the actor toward a partner (`Tenure.since`);
  emits `bond.formed`. The owner closes it with `release` (`VT:851`).
* **What it still lacks.**
  * The partner operand (H-182). The precedent is `give`'s `to`, a known-person operand
    (`VT:430-432`) (**M8**).
  * A reader that gates on the tie's **type** (**M7**). This is the S risk. Regard's stored half is
    already `stance`, and if `tie`'s only reader is a regard term, the game has two carriers for one
    quantity. The tie earns its row by what a bare opinion lacks: "The type field is what a bare
    'opinion number' lacks" (GEP:117). Examples: a sworn tie gates a `knot`'s formation, or a patron
    tie gates a client's `pledge`.
* **NERS.**
  * **N.** BU: the only person-to-person edge. L: RoTK bonds; GEP finds typed records in 6 of 8 games. TD: a defection cascade needs edges to run along (Woodville, NPL:73). **False N-line check:** `regard` already moves live (`judged_gain` 0.5, `person_q.py:336-360`), so without M7 the N-line is **narrowed**, not passing.
  * **R.** "I have cut you off and you do not know it" (`01_AXIOMS.md:1293-1294`): R-WORLD with no player present.
  * **S.** Two directed edges, the same shape as every Tenure (`T-m`).
  * **E.** The split removes a slash-named row whose two halves a reader cannot tell apart, so E improves.
* **Precedent.** §3.2 row 4.
* **Gaps.** Closes NP-G01 once M8 exists, NP-G02 once M7 exists (the undirected read of `knot` goes to
  FI), and NP-G03 (the split).
* **Disposition.** `tie`: **REBUILD** (split; partner operand; typed reader). `knot`: moved to FI, and
  in NP's lexicon it is shown as moved, not culled. `court`: **PARK**.
* **Falsifier.**
  * For the KEEP: if M7 finds no reader that gates on the tie's type, the tie only duplicates `stance`.
    Then cut `tie` and let `regard` carry bonds.

### Suite E — Marriage and kin. Host: `marry`

* **Fold `marry` into `tie` (caution 4; v2's revival form "a `kin` content of `tie / knot`",
  v2-p8:531).** A yes · M **no** · P no. Two reasons:
  * A tie is unilateral by design (`01_AXIOMS.md:1291-1294`). A marriage cannot be: both spouses'
    edges open in one write, as `give` closes one side and opens the other "in ONE effect"
    (`VT:434`).
  * A marriage is public, and it makes kin, a relation `tie` does not carry.
  
  So the fold is a composition and fails rule 5. **NEW ROW.**
* **Folded acts.**
  * `wed`: a synonym in ordinary English. **CULLED** as a duplicate name, because `marry` is the
    plainer word.
  * `betroth`: the promise is usually made by a guardian (Wikt labels the verb *archaic*: "often of a
    parent or guardian"). That is A no, a different actor. **PARK**. Trigger: a kin carrier plus a
    guardian relation.
  * `rear`: raising a child. It needs a child (no carrier; ED-WR-0011 open). Composing `tend` and
    `train` on a child would be a workaround, so if births land, `rear` is its own act: a guardianship
    edge whose term matures the child's training. **PARK**. Trigger: ED-WR-0011 ruled to admit births.
* **World effect (proposed).**
  * Opens two directed `kin` Tenures, one owned by each spouse, with content `spouse`; emits
    `marriage.made`.
  * The counterparty is the spouse. The obstacle is the spouse's consent, read from regard of the
    actor and pursuits [ASSUMPTION: ED-IN-0210 ruling 1's counterparty/obstacle/degree shape, `VT:23-31`].
  * Refused on a live `spouse` edge. That is a negation, so it uses the predicate route, as `release`
    does (`VT:857-859`).
* **Readers (proposed).**
  * IN-70's opinion at read gains a kin term (`WP5` IN-70).
  * `teller_weight`'s relation term.
  * M10's bond-deed judge, so the Woodville cascade runs along kin.
  * **Not** succession: the heir is a title, and the carrier was ruled (RS-27; RS-29, quoted at
    `WP5:211`).
* **What it still lacks.**
  * A `kin` Tenure kind (**M9**). `tenure_kinds` is `open: true` (`rosters.yaml:103`), but
    `release`'s `domain:` is asserted at load against that roster (`VT:858`). Adding `kin` therefore
    also adds it to `release` (divorce or repudiation), or the load fails.
* **NERS.**
  * **N.** Floor (§3.2 row 5). TD: alliances between houses (RTP C1-C5). BU: the strongest personal bond. L: FA's `covenant`. **False N-line check:** `covenant` binds factions by a Proposition. A marriage binds persons and survives a change of faction (the Woodville cascade runs through kin, not treaty), so the cut is not free.
  * **R.** v2's "strongest R-WORLD generator among the designed verbs" (v2-p4 closest call 1).
  * **S.** The same two-edge shape as `tie` and `give`. Consent is an obstacle, not a second act.
  * **E.** One act, two edges, one Event. Passes.
* **Precedent.** §3.2 row 5.
* **Gaps.** Closes NP-G07 and NP-G08 once M9 exists. NP-G09 (`court`) and NP-G10 (`rear`) are parked.
* **Disposition.** `marry`: **NEW ROW** (needs M9). `wed`: **CULLED**. `betroth` and `rear`: **PARKED**.
* **Falsifier.**
  * For the KEEP: a precedent game of this genre with houses and alliances but no marriage would weaken
    the floor claim.
  * For the build: a `marriage.made` whose `kin` edges nothing reads (ID-13) fails.

### Suite F — Service and allegiance. Hosts: `pledge` (was `oblige`), `hire`, `defect`, `commit`

* **`pledge` (REBUILD of `oblige`; caution 6, L-02 applied).**
  * The row is the joiner binding **himself** to a seat (`VT:760-762`, `eligibility: own`,
    `beneficiary: actor`).
  * Ordinary English runs the other way. Wikt's verb senses for *oblige* are "To constrain someone by
    force or by social, moral or legal means" and "To do (someone) a service or favour".
  * Rename to `pledge` ("he pledged himself to the duke"), in the actor's voice. The edge kind may stay
    `oblige`/duty internally (L-02's fix).
  * `swear` (fealty): A yes · M yes · P yes. FOLD as a name. It is not the host, because Wikt records
    the "use bad language" sense of *swear* from Middle English.
* **What NP needs instead of v2's folds into `oblige`.**
  * The joiner's act is `pledge`, and only the joiner ever performs it.
  * The employer's act is `hire`, its own row.
  * The recruiter's act is `recruit`, FA/MB's own row (troop-raising in scope).
  * The briber's act is `bribe`, SC/FA's own row (V-05).
  * v2's merges `recruit` → `oblige` (`_part4:197`), suborn → `oblige` (`:205`) and bribe → `oblige`
    (`part3:396`) are struck (L-02). Those three line citations are L-02's; this lane did not reopen
    them.
* **`hire` (NEW ROW; caution 5, V-06 applied).**
  * Actor: the hirer, as in English ("the lord hired a steward").
  * Effect: opens the hiree's service edge (an `oblige`-kind Tenure with `Tenure.term`) toward the
    hirer's seat or household. A conferrer already opens the conferee's hold (`VT:181-182`), so this is
    precedented.
  * Same write: pays the first wage as a store movement. `transfer` already renews `oblige` terms by
    upkeep (`VT:1265`).
  * Counterparty: the hiree. Obstacle: the hiree's willingness (wage against pursuits and regard),
    because recruitment "costs consent, not only money" (PGC:285).
  * Emits `service.hired`; refusal `hire.refused`.
  * **Fold test against `pledge`:** A no. **Against EC's `hire`:** A yes · M yes · P yes, because a
    company is a cohort, a Person at `weight > 1` (`carriers.py:646`). So it is one row; ownership is
    flagged (§3.8).
  * **Against `recruit`:** M no. Recruitment draws on a seat's troop stock, while hiring buys a
    person's or company's service. The troop-stock design never mentions hiring or mercenaries (grep of
    both troop-stock files: 0 hits) [CONFIDENCE: medium on the "M no", since the troop-stock mechanic
    was not read in full].
* **`defect` (NEW ROW) [CONFIDENCE: medium].**
  * One act closes the actor's live `commit`/`oblige` toward faction A and opens one toward B, in one
    write. It emits `allegiance.changed`, naming both.
  * **Fold test against `release` + `pledge`/`commit`:** this is a composition of two verbs, so it
    fails rule 5 by construction.
  * **Why a row and not the pair:**
    * It is atomic: there is no season in which the turncoat is nobody's, and no window in which A's
      muster still counts him.
    * Its Event is the thing witnesses judge as treachery, while `release` stays the open resignation
      ("a voluntary release is a different act", `VT:856`).
    * Precedent: RoTK and Bannerlord (§3.2 row 10).
  * Needs a `deed:allegiance.changed` cell on IN-08's axes (H-205; IN-11's planned `deed:` cell) and a
    producer reading opinion (IN-70) (**M10**, **M14**).
  * Alternative for the reconciliation (Part III §III.5): no row, with the price kept on `release` (v2 V093). The user's
    no-workarounds rule decides between them.
* **`commit` (KEEP-AS-IS).**
  * Binds a person to a Proposition (creed, ambition, vote; `VT:128-143`).
  * Shipped and resolvable. Shared with SC/FA (§3.8).
  * Its two reader gaps are NP-G33 (an OUGHT's `predicate` is unread, H-185) and NP-G34 (whether a
    declared intent was kept, H-191) (**M15**).
* **`betray` (CULLED as a verb; caution 2, V-09 applied).**
  * Tested as "a judgement across acts". Betrayal in English is an act described by its relation to a
    trust: Wikt's first two senses are "To deliver into the hands of an enemy by treachery or fraud, in
    violation of trust" and "To prove faithless or treacherous to".
  * The acts that carry it are `tell` (a secret to an enemy), `give` (a document), `defect`, `fight`
    (one's lord) and `seize` (opening a gate). They differ in mechanic, so no single host exists.
  * Precedent: in Diplomacy [MEMORY] there is no betray order; betrayal is an ordinary move order made
    against a spoken promise.
  * The mechanism is a witnesses' judgement: `deed_valence` (`person_q.py:314`) judges an act whose
    doer holds a live bond (`commit`/`oblige`/`tie`/`kin`) to the act's victim (**M10**).
  * v2's "`release` priced by one `deed:commitment.ended` cell" (v2-p8:528) names the open resignation,
    which is renunciation, not betrayal. It is rejected.
* **World effects.**
  * `pledge`: `Tenure.since`, `Tenure.term`; `duty.taken` (`VT:772-774`).
  * `hire` and `defect`: as above.
  * `commit`: `Tenure.since`; `commitment.made`.
* **NERS.**
  * **N.** `pledge` and `hire` are floor (§3.2 rows 8-9), and `defect` is floor (row 10). TD: cascades. L: FA musters read membership. **False N-line check for `defect`:** `release` + `commit` already reach the same final state, so the N-line rests on the Event and the atomicity, not on the end state. That is the honest reason for the medium confidence.
  * **R.** The principal-agent drama the genre runs on (NP-G39), and loyalty that moves.
  * **S.** Every edge here is an `oblige` or `commit` Tenure, so there are no new kinds. `hire` and `pledge` write one edge kind from two voices, which is consistent with `confer`/`oblige`.
  * **E.** Three verbs, each in its actor's voice, replace one misnamed row and three bad folds. E improves.
* **Gaps.**
  * Closes NP-G22 (betrayal → M10), NP-G23 (STALE, `repudiate` cut, `VT:856`), NP-G24 (`defect`) and
    NP-G32 (M10 judges a revocation done to oneself).
  * NP-G33 and NP-G34 are closed by `commit` once M15 exists.
  * NP-G25 (`recruit`) and NP-G36 (cohorts) are out of scope (FA/MB). NP-G39 is GV's reader (§3.6).
* **Disposition.** `pledge`: **REBUILD** (rename). `swear`: **FOLDED**. `hire` and `defect`:
  **NEW ROW**. `commit`: **KEEP-AS-IS**. `betray`: **CULLED**.
* **Falsifier.**
  * `pledge`: a reader who meets "X obliges Y" and lands on the self-binding refutes L-02.
  * `hire`: a hire that a `pledge` by the same actor could express refutes it.
  * `defect`: witnesses whose judgement of `release` + `commit` equals their judgement of `defect`
    show the row adds nothing.
  * `betray`: a case where betrayal writes something no underlying act writes would revive it.

### Suite G — Succession. Host: `succeed`

* **Voice and fit (caution on `succeed`).**
  * The 2026-10-03 pass: "STRAINED — the heir succeeds; the actor designates" (VCD:357).
  * IN-61 re-specifies the row as **the heir's own claim**: "The act is the `succeed` row RE-SPECIFIED
    as the heir's claim" (`WP5:211`).
  * The actor is now the heir, so `succeed` **FITS** ("he succeeded to the throne"). L&S *succēdō*
    II.B gives "take the place of … succeed to, receive by succession".
  * v2's CUT read RS-27 as against both verbs (v2-p4:93, :148). RS-27's own text, quoted at `WP5:211`,
    is *"designated heir is not a verb but a status or title. the heir still has to claim their
    throne"*. It cuts designation only. **v2 is superseded on `succeed`.**
* **Folded acts.**
  * `designate` into GV's `confer`: A yes (the throne holder, `remit:confer`) · M yes (`confer`) · P yes
    (the office is `off_heir`). FOLD. IN-61: "Designation is NOT a verb: it is the existing `confer` of
    the heir title."
  * `inherit` (an estate at death): **not an act.** It is a transmission at MATTER (`VT:952`, "its one
    reader, transmission at death … is unbuilt"). It is outside the seat case (**M11**).
* **World effect (IN-61).**
  * `inheritance` joins `conferral_bases`. The claim opens the throne's `hold` and closes the
    claimant's `off_heir` hold in one write.
  * The shipped event `heir.designated` (`VT:948`) now misnames the act and must become a claim kind,
    e.g. `succession.claimed`.
* **What it still lacks.** The vacancy reaching the heir: H-206, and IN-61's design-first check, which
  is to "confirm the heir actually receives that occasion" (`WP5:211`) (**M12**).
* **NERS.**
  * **N.** Floor. TD: realm continuity. **False N-line check:** a self-`confer` (IN-53's `counterparty_may_be_self`) could fill a vacancy, but IN-61 refuses `inheritance` to `confer` (`may_fill`). Without `succeed` the throne goes to any conferrer or stays empty, so the cut is not free.
  * **R.** Contested succession by `challenge`, by tribunal or by force (`WP5:211`).
  * **S.** The first basis → act distinction, with the registry read at runtime (no second home for the heir fact).
  * **E.** Passes.
* **Gaps.** Closes NP-G04 (once IN-61 lands) and NP-G05 (the voice is fixed, so the rename question is
  moot). Closes NP-G06 once M12 exists. NP-G37 (regency) is GV's IN-48 (§3.8).
* **Disposition.** `succeed`: **REBUILD** (actor, operand, effect and event per IN-61). `designate`:
  **FOLDED** into `confer`.
* **Falsifier.** IN-61's own: "a hold opened through `inheritance` for an actor who does not hold the
  registered heir seat → fail" (`WP5:211`).

### Suite H — Gifts. Host: `give`

* **Folded acts.**
  * `cede` (give a Rung): A yes · M yes (close and open a `hold`) · P yes (object kind Rung). FOLD,
    once IN-12's B-R widening lands (`WP5:70`).
  * `surrender` (cession under arms): MB/SC's named preset of `give` (v2-p7:243). Flagged (§3.8).
* **World effect.** The giver's `hold` closes and the receiver's opens in one effect; emits
  `record.given` (`VT:433-437`).
* **What it still lacks.**
  * Rung objects (the `kind: Record` narrowing, `VT:419-430`).
  * Any change in the receiver's regard (**M13**). A gift that raises nobody's opinion misses the floor
    act (Crusader Kings 3 [MEMORY], "Send Gift").
* **Answer to L-10 (give/transfer).** The discriminator is the carrier, not the word's object:
  * `give` moves a **held thing**, a Tenure (`hold`), between two persons present (social stratum).
  * `transfer` moves a **quantity** between rung stores under the scarcity predicate (`VT:1252-1265`).
  * Fold test of a gift of grain into `give`: M no (it writes `Rung.stores`, not a Tenure). The two
    rows stay. The naming defect is real but only MATERIAL. Flagged to EC.
* **NERS.**
  * **N.** Floor, and the only consensual route by which title moves (`WP5:70`).
  * **R.** Patronage by gift.
  * **S.** One-per-side writes, as `confer` does.
  * **E.** Passes.
* **Gaps.** NP-G26: its "no alignment cell" half is **stale**, because `give` carries a `-0.2` cell
  (`engine/season/rosters.yaml:2992`). Its Rung half is closed by IN-12 B-R.
* **Disposition.** `give`: **REBUILD** (widen to Rung; M13). `cede`: **FOLDED**.
* **Falsifier.** A `give` of a Rung that changes no title-holder's read refutes the widening.

### Suite I — Avowal. `confess` folds into SC's `tell`

* **The fold.** `confess`: A yes (the teller) · M yes (`tell` deposits a claim in the hearer's ledger)
  · P yes (the claim is of the teller's own deed). FOLD (v2 V176).
* **The rest goes to other lanes.**
  * The value of `confession.made` under questioning is `interrogate`'s (K-56; FI/SC).
  * Lying (NP-G35, J-C-6) is SC's.
  * A promise (NP-G34) is `commit`'s reader, M15.
* **Disposition.** `confess`: **FOLDED**.
* **Falsifier.** A confession that must write something `tell` does not write would revive the row.

### Suite J — Devotion. Hosts: `consecrate` (PARK); `pray` and `mourn` are culled

* **`consecrate`** (V-17 applied: renamed from `bless`).
  * The act is a religious seat-holder's sanction of a **held** seat. Fold into `confer`: A ?
    (a remit holder) · M **no**, since `confer` opens a hold and closes the others (`VT:182`) and
    "`confer` cannot consecrate a held seat" (v2-p8:607). Not a fold.
  * Precedent: Pippin III's anointing, "institutional replacement legitimated by external religious
    sanction" (`research/governance/governance_modes.md:142`).
  * `crown`: A yes · M yes · P yes (the seat is a throne). FOLD as content.
  * `bless`: **CULLED** as the name. Wikt's senses run from "make something holy by religious rite" to
    "invoke divine favor upon", which is too wide, and the word is Germanic and of uncertain origin.
  * **PARK.** Trigger: H-100's revocation-cost reader, or IN-23's legitimacy Query reading a sanction
    edge (v2-p8:539). Owner when built: GV (§3.8).
* **`pray`.** **CULLED.** It moves no state any reader reads. Conviction moves "BY ARGUMENT AND
  CONSEQUENCE" (H-62), and the only writer of `pursuits` is `argue`. Floor check: none of the floor
  precedents (§3.2) has prayer as a mechanical act [MEMORY]. Any thread-side prayer is TW's (§3.8).
* **`mourn`.** **CULLED.** Grief is written by witnessing: the death claim, `scar`
  (`carriers.py:678-688`) and `stance`. It is not chosen (NPL:151, RimWorld; v2 V173). Floor check: no
  floor act is lost, because the death claim already reaches witnesses (IN-58).
* **Gaps.** NP-G28 (parked), NP-G29 (`mourn`), NP-G30 (`pray`).
* **Falsifier.**
  * For `pray`: a ruled writer of conviction by devotion would revive it.
  * For `mourn`: a case where mourning is a public act with a world effect (a funeral that convenes
    heirs) would revive it.

---

## 3.4 Lexicon table

**Conventions.**
* Chains read English ← intermediates ← Latin (principal parts; attested sense) ← PIE. "Wikt" and
  "L&S" mean the lane tool showed that link.
* **Germanic** words have no Latin ancestor, and a Latin form named beside one is a cognate, not an
  ancestor.
* Fit is judged by ordinary current usage.
* "PLANNED" means a workplan position exists but no row does. "NEW" means this lane proposes the row.

| verb | suite | status | mechanic and world effect (carrier written) | etymology chain with sources | fit | rename |
|---|---|---|---|---|---|---|
| `tend` | A | PLANNED (IN-12 s9) | raises `Person.body`; `body.tended` | ME *tenden*, aphetic of *attenden* (← OF *atendre* ← L *attendō, attendere, attendī, attentum* "to stretch toward; to direct the attention, apply the mind to, give heed to" (L&S) ← *ad-* + *tendō*) or of *entenden* (← L *intendō*) (Wikt) ← *tendō* ← PIE \*tend-, a d-extension of \*ten- (Wikt la *tendō*). Sense "look after (an ill person)" from early 14th c. (Wikt defdate) | FITS: "tend the wounded" is ordinary; it names the act, not the outcome | — |
| `heal` | A | FOLDED → `tend` | as `tend` | Germanic: ME *helen* ← OE *hǣlan* ← PWGmc \*hailijan ← PGmc \*hailijaną ← PIE \*kéh₂ilos "whole" (Wikt). No Latin path | STRAINED as a verb name: names the result (the body rising), not the act | `tend` |
| `recover` | A | FOLDED → `tend` (active); the passive half is not an act (M1) | as `tend`, `subject` = actor | ME *recoveren* ← AN *recoverer*, OF *recovrer* ← L *recuperō* (alt. of *reciperō*), *-āre, -āvī, -ātum* "to get or obtain again; to regain, recover" (L&S *recipero*; Wikt la adds "restore to health") ← *capiō*; PIE \*keh₂p- (Wikt) | STRAINED: ordinary use is intransitive (one recovers); as an act it is self-tending | `tend` (self) |
| `train` | B | PLANNED (IN-12 s9) | writes `Person.capability`; `capability.raised` | ME *trainen*, verb from the noun in ME (Wikt) ← OF *traïner* "drag" ← VL \*traginō ← \*tragō ← L *trahō, trahere, trāxī, tractum* "to draw, drag, or haul" (L&S) ← PIE uncertain: \*dʰregʰ- is tentative; De Vaan proposes a non-IE \*trHgʰ-/\*trā̆gʰ- (Wikt la). "Instruct" sense 16th c. (VCD) [UNVERIFIED date] | FITS: covers self and pupil | — |
| `study` | B | FOLDED → `train` | `train`, `subject` = actor | ME *studien* ← OF *estudier* ← *estudie*, borrowed from L *studium* (Wikt) ← *studeō, studēre, studuī* "to be eager or zealous, to take pains about, be diligent in" (L&S) ← PIE \*(s)tewd- (Wikt) | FITS, as a self-form of `train` | — |
| `teach` | B | FOLDED → `train` | `train`, `subject` = pupil | Germanic: ME *techen* ← OE *tǣċan* ← PWGmc \*taikijan ← PGmc \*taikijaną ← PIE \*deyḱ- (Wikt). L *dīcō* is a cognate through \*deyḱ-, not an ancestor (Wikt en *teach* lists L *dīcō* among the cognates) | FITS | — |
| `drill` (person) | B | FOLDED → `train`; the troop half goes to MB | `train` | from MDu *drillen* (Wikt), Germanic; the sense "practise, especially military" is Wikt's | FITS for troops; STRAINED for one person | — |
| `forgive` | C | PLANNED (IN-12 s13) | removes the actor's negative `Person.stance` rows toward `subject`; `stance.moved` | Germanic: alteration (after *give*) of ME *foryiven* ← OE *forġiefan* ← PWGmc \*frageban ← PGmc \*fragebaną (*for-* + *give*) ← PIE \*gʰebʰ- (Wikt) | FITS: one's own grudge ends (VCD §9.4) | — |
| `reconcile` | C | CULLED | none of its own; it is the outcome of two `forgive`s | borrowed from L *reconciliō, -āre, -āvī, -ātum* "to bring together again, reunite, reconcile" (L&S; Wikt :bor) ← *conciliō*. Wikt en gives a direct borrowing from L *reconciliō*, with no ME/OF intermediate. PIE: *conciliō* ← *concilium* ← *con-* + *calō* ← \*kelh₁- "call" (Wikt la) | FITS as English, but names two parties' acts | — |
| `avenge` | C | CULLED | none; the act is `fight`/`march`/`challenge`, and the grudge is read at choice (M6) | ME *avengen* ← OF *avengier* (*a-* + *vengier*) (Wikt fro); *venge* ← OF *venger* ← L *vindicāre* (Wikt) ← *vindicō, -āre, -āvī, -ātum* "to lay legal claim to"; sense C "to avenge, revenge, punish" (L&S) ← *vindex* ← *vīs* + *dīcō* ← PIE \*deyḱ- (through *dīcō*) (Wikt la) | FITS as English; names a motive, not a mechanic | — |
| `tie` | D | SHIPPED as `tie / knot`; REBUILD (split) | opens a directed `tie` Tenure; `bond.formed` (declined until M7 and M8) | Germanic: ME *teien* ← OE *tīġan* ← PWGmc \*taugijan ← PGmc \*taugijaną ← PIE \*dewk- (Wikt). L *dūcō* is a cognate through \*dewk-, not an ancestor (Wikt la *dūcō* ← \*dewk-, the same root template as on *tie*) | FITS: "ties of friendship"; idiomatic once alone | — |
| `knot` | D (moved to FI) | SHIPPED as `tie / knot`; moved to FI | fieldwork Knot (`knots.py`); WITNESS `firsthand_via_knot` | Germanic: ME *knotte* ← OE *cnotta* ← PWGmc \*knottō ← PGmc \*knuttô/\*knudô; probably PIE \*gnod- (Wikt). Wikt lists L *nōdus* alongside; it is a cognate, not an ancestor | STRAINED as a verb: "to knot" is literal; the sense is the coined noun Knot | FI's call |
| `court` | D | PARKED (owner SC) | none until a consent contest exists | from the noun: ME *court* ← OF *cort* ← LL *cōrs* ← L *cohors, cohortis* "a place enclosed around, a court, enclosure, yard"; also a retinue of courtiers (L&S *cohors*; Wikt). The verb "woo" formed in English from the noun [UNVERIFIED date] | FITS ("he courted her"), though slightly dated | — |
| `marry` | E | NEW | opens two directed `kin` Tenures (content `spouse`); `marriage.made` (needs M9) | ME *marien* ← AN *marïer* ← L *marītō, -āre, -āvī, -ātum* "to give a husband to one; to wed, marry, give in marriage" (L&S; post-Augustan and rare) ← *marītus* ← *mās*, of uncertain origin, possibly PIE \*méryos (Wikt: disputed) | FITS | — |
| `wed` | E | CULLED (duplicate) | — | Germanic: ME *wedden* ← OE *weddian* ← PWGmc \*waddjōn ← PGmc \*wadjōną ← \*wadją ← PIE \*wedʰ- (Wikt) | FITS, but a near-synonym of `marry`, which is plainer | `marry` |
| `betroth` | E | PARKED | a guardian's promise; needs kin and a ward | ME *bitrouthen* ← *bi-* (OE *be-* ← \*h₁epi) + ME *trouthe* ← OE *trēowþ* ← PGmc \*triwwiþō ← PIE \*dóru "tree" (Wikt en *betroth*, *troth*). Germanic | STRAINED: Wikt labels the verb *archaic* | "promise in marriage" if revived |
| `rear` | E | PARKED (ED-WR-0011) | a guardianship edge over a child, once a child carrier exists | Germanic: ME *reren* ← OE *rǣran* ← PWGmc \*raiʀijan ← PGmc \*raizijaną ← PIE \*h₁rey- (Wikt); related to *rise*, *raise* | FITS ("rear a child") | `raise` is equally plain |
| `pledge` | F | SHIPPED as `oblige`; REBUILD (rename) | opens the joiner's `oblige`-kind Tenure to a seat (`Tenure.since`, `Tenure.term`); `duty.taken` (`VT:772-774`) | ME *plege* ← AN, OF *plege* ← ML *plevium*/*plebium* ← *plebiō* ← Frankish \*plehan (Wikt). **Not classical Latin**: Medieval Latin from Frankish, akin to OE *plēon*, E *plight* | FITS: "pledged himself to the duke" is in the joiner's voice | (from `oblige`) |
| `oblige` | F | SHIPPED; renamed `pledge` | as above | ME *obligen* ← OF *obligier* ← L *obligō, -āre, -āvī, -ātum* "to bind or tie around"; also "pro amicis alicui obligari, to lay one's self under obligation" and "to pledge, pawn" (L&S) ← *ob-* + *ligō* ← PIE \*leyǵ- (Wikt) | MISFIT: Wikt's senses "constrain someone" and "do (someone) a favour" run opposite to the row (L-02) | `pledge` |
| `swear` | F | FOLDED → `pledge` (name) | as `pledge` | Germanic: ME *sweren* ← OE *swerian* ← PWGmc \*swarjan ← PGmc \*swarjaną ← PIE \*swer- (Wikt); "the original sense … is 'to take an oath'"; the profanity sense is ME (Wikt) | FITS in "swear fealty"; the bare verb is ambiguous | — |
| `hire` | F | NEW (shared with EC) | opens the hiree's service Tenure toward the hirer's seat or household and pays the first wage (`Rung.stores`); `service.hired` | Germanic: ME *hiren* ← OE *hȳrian*, from the noun OE *hȳr* ← PWGmc \*hūʀiju ← PGmc \*hūzijaną; PIE \*kewHs- or another root (Wikt: disputed). No Latin path | FITS: the employer is the subject, as in English | — |
| `defect` | F | NEW [CONFIDENCE: medium] | closes the actor's `commit`/`oblige` to A and opens one to B in one write; `allegiance.changed` | from L *dēfectus*, past participle of *dēficiō, dēficere, dēfēcī, dēfectum* "to leave, desert, depart … to forsake, desert, abandon, revolt (*ab amicitia P. R.*, Caes.)" (L&S; Wikt shows the noun's borrowing). PIE: *dēficiō* ← *dē-* + *faciō* ← \*dʰeh₁- "to put" (Wikt la). Verb date [UNVERIFIED] | FITS: "defect to the enemy" | — |
| `commit` | F | SHIPPED, KEEP | opens `commit` to a Proposition (`Tenure.since`); `commitment.made` (`VT:128-143`) | ME *committen*, borrowed from L *committō, committere, commīsī, commissum*; L&S I "to bring … combine into one whole; to join"; the later sense "entrust": L&S II "to give, intrust, commit to, to give up or resign to, to trust". PIE: *com-* + *mittō*, likely from an extension of the root \*mey- ("exchange" → "give" → "send") (Wikt la *mittō*) | FITS ("commit to a cause") | — |
| `betray` | F | CULLED | none; a witnesses' judgement across acts (M10) | ME *betrayen* = *be-* + ME *trayen* "betray" ← OF *trair* ← L *trādō, trādere, trādidī, trāditum* "to give up, hand over, deliver, transmit, surrender" (L&S; Wikt *tray*) ← *trans-* + *dō* ← PIE \*deh₃- "give" (Wikt la *trādō*, *dō*) | FITS as English; names a relation of an act to a trust | — |
| `renounce` | F (flag) | not NP's; L-08 rename for `release` on `commit`/`oblige` | `release`'s `Tenure.until` | ← OF *renoncier* ← L *renūntiō, -āre, -āvī, -ātum* "bring back word, report"; II "to retract, revoke … give up, break off … disclaim, renounce" (L&S) ← *nūntius*, origin uncertain (De Vaan tentatively favours PIE \*newH- "to cry"; an older derivation from *novus* is rejected) (Wikt la) | FITS for one's own vow | proposed for `release`'s vow half |
| `succeed` | G | SHIPPED (declined); REBUILD per IN-61 | the heir's claim opens the throne's `hold` and closes `off_heir` (`inheritance` basis); event to rename | ← OF *succeder* ← L *succēdō, succēdere, successī, successum* "to go below or under"; II.B "to follow, follow after, take the place of … succeed to, receive by succession" (L&S) ← *sub-* + *cēdō*. Wikt en gives "From OF *succeder*, from L *succedo*", with no ME stage; PIE through *cēdō* is disputed (Wikt la) | FITS **now**: the heir is the actor (it was STRAINED in VCD:357 when the holder designated) | — |
| `designate` | G | FOLDED → `confer` (GV) | `confer` of `off_heir` | from L *dēsignātus*, past participle of *dēsignō, -āre, -āvī, -ātum* "to mark out, trace out; to describe, designate, define" (L&S) ← *signum*; PIE \*sekʷ- or \*sek- (Wikt shows both: disputed) | FITS as English; not its own act | — |
| `give` | H | SHIPPED; REBUILD | closes the giver's `hold` and opens the receiver's; `record.given` (`VT:433-437`) | Germanic: ME *given*/*yeven* ← OE *ġiefan* + ON *gefa* ← PGmc \*gebaną ← PIE \*gʰebʰ- (Wikt) | FITS | — |
| `cede` | H | FOLDED → `give` (object Rung) | `give` of a Rung `hold` | borrowed from MF *ceder* ← OF *ceder* ← L *cēdō, cēdere, cessī, cessum* "to go, be in motion" (Wikt; L&S key *cedo1*) ← Proto-Italic \*kezdō, PIE disputed: \*ḱyesdʰ- is one proposal (Wikt la). Sense "yield": L&S *cēdo*, "loco, to yield, give up his post"; with an object, "to grant, concede, allow, give up, yield" | FITS ("cede the town") | — |
| `confess` | I | FOLDED → `tell` (SC) | `tell`'s claim of the teller's own deed | ME *confessen* ← AN, OF *confesser* ← L *confessus*, past participle of *cōnfiteor, cōnfitērī, confessus sum* "to acknowledge, confess, own, avow (a fact previously denied or doubted)" (L&S) ← *con-* + *fateor* ← PIE \*bʰeh₂- (Wikt) | FITS | — |
| `consecrate` | J | PARKED (owner GV) | a sanction edge on a held seat (needs the H-100 or IN-23 reader) | ME *consecraten* (late 14th c.) ← L *cōnsecrātus*, past participle of *cōnsecrō, -āre, -āvī, -ātum* "to dedicate, devote something as sacred to a deity" (L&S; Wikt) ← *sacrō* ← *sacer* ← OL *sacros* ← Proto-Italic \*sakros ← \*sh₂krós ← PIE \*seh₂k- "to make sacred, make a pact" (Wikt la) | FITS for bishops and kings, if formal | (from `bless`) |
| `crown` | J | FOLDED → `consecrate` (content: a throne) | as `consecrate` | ME *coroune* ← AN *corone* ← L *corōna* "garland, crown" ← Gk κορώνη ← PIE \*(s)ker- "turn" (Wikt en; the verb is the same word, under the noun's Etymology 1); its Latin match is L *corōnō, -āre, -āvī, -ātum* "to furnish with a garland or crown, to crown, wreathe" (L&S) | FITS ("crowned king") | — |
| `bless` | J | CULLED as the name | — | Germanic: ME *blessen* ← OE *bletsian* ← PWGmc \*blōdisōn ← PGmc \*blōþą, "of uncertain origin", possibly PIE \*bʰleh₃- (Wikt) | STRAINED: too wide (meals, sneezes); does not name a seat's sanction | `consecrate` |
| `pray` | J | CULLED | none (H-62) | ME *preien* (Wikt; it displaced OE *gebiddan*) ← AN *preier* ← OF *proiier* ← L *precor, precārī, precātus sum* "to ask, beg, entreat, pray, supplicate" (L&S; Wikt la, 1st-conj. deponent) ← *prex* "request, prayer" (Wikt) ← Proto-Italic \*preks ← PIE \*préḱs ← \*preḱ- "to ask"; Wikt lists the cognates *fragen*, OE *freġnan* | FITS as English; no mechanic | — |
| `mourn` | J | CULLED | none; written by witnessing | Germanic: ME *mornen*/*mournen* ← OE *murnan* ← PGmc \*murnaną; PIE \*(s)mer- "remember" (Wikt root template) | FITS as English; an affect, not a choice | — |

**Tally** (recounted from this table, not carried from v2).

| | count | names |
|---|---|---|
| NP rows after assessment | 11 | `tend`, `train`, `forgive`, `tie`, `marry`, `pledge`, `hire`, `defect`, `commit`, `succeed`, `give` |
| of those, shipped | 5 | `tie`, `pledge` (as `oblige`), `commit`, `succeed`, `give`; 4 are REBUILD, 1 is KEEP |
| of those, planned | 3 | `tend`, `train`, `forgive` |
| of those, NEW | 3 | `marry`, `hire`, `defect` |
| FOLDED | 10 | heal, recover, study, teach, drill, swear, designate, cede, confess, crown |
| PARKED | 4 | court, betroth, rear, consecrate |
| CULLED | 7 | reconcile, avenge, wed, betray, bless (name), pray, mourn |
| moved or flagged | 3 | `knot` (to FI), `oblige` (renamed `pledge`), `renounce` (proposed for `release`) |

---

## 3.5 Deduplication and culls

### Near-synonym groups

| group | what was done | discriminator, by ordinary usage and carrier |
|---|---|---|
| tend · heal · recover · (EC `restore`) | heal and recover fold into `tend`; `restore` stays EC's | `tend` takes a Person (`body`); `restore` takes a Site (`condition`) on the same scale. English splits "tend a man" from "restore a wall" |
| train · study · teach · drill | three fold into `train`; drill's troop half goes to MB | `subject` is self or pupil; a cohort's quality is the troop stock's |
| forgive · pardon · reconcile · `release` | reconcile culled; pardon is GV/SC's | whose state: my grudge (`stance`) vs another's restraint (`detain`/`ban`) vs my own Tenure (`release`) |
| tie · knot · court · marry · wed · betroth | knot moved (FI); wed culled; court and betroth parked | `tie` is unilateral regard; `marry` is a two-party public bond that makes kin; `knot` is fieldwork's strain-bearing Knot |
| pledge (`oblige`) · swear · commit | swear folds into pledge | `pledge` binds to a **seat**; `commit` binds to a **Proposition**. ⚠ "Pledge allegiance to a cause" and "commit to a cause" overlap in English. The objects differ, but a reader cannot predict that from the word. A **residual near-synonym, accepted** because both are plain and the object makes the difference visible |
| hire · pledge · recruit | three rows, three actors | the hirer buys service; the joiner binds himself; the recruiter draws on a seat's troop stock (FA/MB) |
| defect · `release` · betray | betray culled; defect added | `defect` is an atomic side-change and the judged Event; `release` is an open resignation; betrayal is a judgement across acts |
| succeed · designate · `confer` · inherit | designate folds into `confer`; inherit is not an act | the heir claims (`succeed`); the holder designates (`confer` of `off_heir`); transmission at death is MATTER's |
| give · cede · `transfer` · `surrender` | cede folds into `give`; surrender is MB/SC's preset | a held thing (Tenure) vs a quantity (stores) |
| bless · consecrate · crown · `confer` | bless culled as a name; crown folds into consecrate | sanction of a **held** seat vs filling a vacant one |
| confess · `tell` | confess folds into `tell` | the content is a claim of the teller's own deed |

### Culls: fold test and floor check

| cull | fold test | floor check |
|---|---|---|
| `reconcile` | A no (two actors), several steps | nothing a floor act needs dies, because `forgive` (floor row 6) carries each party's half and a `tie` can follow |
| `avenge` | A no (the avenger fights, marches or challenges); no distinct mechanic | nothing a floor act needs dies, because the floor's vengeance is a chosen `fight`/`march` (PC/MB); what is missing is the reader M6, not a verb |
| `betray` | the acts that betray differ in mechanic (`tell`, `give`, `defect`, `fight`, `seize`), so no host passes M | nothing a floor act needs dies, because `defect` (floor row 10) is a row and every betraying act stays a row; M10 judges them |
| `wed` | A yes · M yes · P yes, a pure synonym | `marry` survives |
| `bless` (name) | the act survives as `consecrate`; only the word is culled | not a floor act |
| `pray` | no mechanic: H-62 (conviction moves by argument and consequence) | not a floor act in the cited precedents |
| `mourn` | no mechanic chosen by the actor; grief is written by witnessing | not a floor act; the death claim reaches witnesses (IN-58) |

### Critic findings that concern NP verbs

| finding | verdict | what was done |
|---|---|---|
| L-01 (root sense used as design intent) | **applied** | Every fit verdict in §3.4 is by usage. No merge, gap or split here rests on a root sense: the `tie`/`knot` split rests on `knots.py` and `witness.py`; the `betray` cull on the acts' mechanics; the `oblige` rename on Wikt's current senses |
| L-02 (`oblige` reverses direction) | **applied** | Renamed `pledge` (Suite F). v2's folds of recruit, suborn and bribe into `oblige` are struck. Caution 6 is answered: NP needs `pledge` for the joiner and `hire` for the employer, never a fold of another actor's act into the joiner's row |
| L-08 (`release` names vow-breaking) | **answered, flagged** | `release` is not NP's row. NP agrees that `renounce` fits the closing of one's own `commit`/`oblige`. Treachery is moved off `release` onto `defect` and M10, so `release` keeps only the open resignation (§3.8) |
| L-10 (give/transfer) | **answered** | The discriminator is the carrier: a Tenure-held thing vs a stores quantity (Suite H). The naming observation stands as MATERIAL; no rename |
| L-12 (proposal lexicon stale) | **applied** | NP-G23 is marked STALE: `repudiate` was cut at IN-11 (`VT:856`) |
| L-19 (`synonym_registry.yaml` has no verb renames) | **flagged** | oblige→pledge, bless→consecrate and the tie/knot split would each need an entry there. Not edited here |
| L "upheld: succeed (STRAINED is right)" | **answered** | Right for the shipped row, in which the holder designates. IN-61 makes the heir the actor (`WP5:211`), so the verdict moves to FITS |
| V-06 (hire/recruit voice asymmetry) | **applied** | `hire` is its own row in the hirer's voice (Suite F). V-06's suggested correction (hire = `tell` + the hiree's `oblige` + `transfer`) is **rejected** under the no-workarounds rule: it composes three verbs and two actors |
| V-09 (betray is not `release`) | **applied** | `betray` is culled as a verb and treated as a judgement across acts (M10). V-09's "name the merged act *repudiate/renounce*" is passed to the `release` owner |
| V-17 (bless is consecration) | **applied** | Renamed `consecrate`, PARKED, owner GV |
| V-21 (`tie / knot` MISFIT not engaged by v2) | **applied** | Split (Suite D) |
| V "upheld: marry on `tie / knot`" | **rejected** | A tie is unilateral (`01_AXIOMS.md:1291-1294`) and a marriage cannot be. The fold composes two parties' acts (Suite E) |
| V "upheld: heal/recover → tend, study → train, confess → tell" | **upheld** | All three pass A/M/P |

---

## 3.6 Gap coverage

Each row carries exactly one disposition: closed by, PARKED, OUT OF SCOPE, STALE or DISPUTED.

| gap | disposition | note |
|---|---|---|
| NP-G01 | closed by `tie` once **M8** exists | Suite D |
| NP-G02 | closed by `tie` once **M7** exists | the undirected `knot` read (`VT:1245`) goes to FI with `knot` |
| NP-G03 | closed by the `tie` / `knot` split (Suite D) | the evidence is mechanical (`knots.py:1-40`, `witness.py:464-477`), not lexical |
| NP-G04 | closed by `succeed` once IN-61 lands | VCD's R-5 (b) `inheritance` basis is IN-61's (`WP5:211`); v2's CUT is superseded |
| NP-G05 | closed by `succeed` (the heir's voice, IN-61) | the rename to `designate` is moot; `designate` folds into `confer` |
| NP-G06 | closed by `succeed` once **M12** exists | H-206 |
| NP-G07 | closed by `marry` once **M9** exists | kin is **not** read by succession (RS-27/RS-29 ruled the title) |
| NP-G08 | closed by `marry` once **M9** exists | NEW ROW, not a `tie` content |
| NP-G09 | PARKED: `court` | trigger: `marry` exists and SC exposes a consent contest |
| NP-G10 | PARKED: `rear` | trigger: ED-WR-0011 ruled to admit births and a child carrier |
| NP-G11 | closed by `tend` | IN-12 step 9 |
| NP-G12 | closed by `tend` once **M1** exists | heal and recover folded; the upward crossing is M1 |
| NP-G13 | closed by `train` once **M3** exists | study, teach and drill folded |
| NP-G14 | closed by `train` (P-08 bound held structurally by the capability roster) | the loader refuses a Thread Sensitivity key (M3) |
| NP-G15 | closed by `train` once **M4** exists | — |
| NP-G16 | closed by `forgive` | IN-12 step 13 |
| NP-G17 | closed by `forgive` once **M5** exists | — |
| NP-G18 | closed by `forgive` (the stored half; R-9 (a) adopted) | the silent eviction of *judged* deeds is a ledger rule, flagged to FI (§3.8) |
| NP-G19 | closed by `forgive` (axis: whose state) | `pardon` belongs to GV/SC |
| NP-G20 | closed by `fight` / `march` / `challenge` (PC, MB) once **M6** exists | `avenge` is CULLED as a verb |
| NP-G21 | closed by `forgive` (`reconcile` = two `forgive`s; culled) | `vouch` and `recant` are SC's speech acts (§3.8) |
| NP-G22 | closed by `defect` once **M10** exists | `betray` is culled; v2's `release` cell is rejected (V-09) |
| NP-G23 | STALE | `repudiate` was cut at IN-11 and merged into `release` (`VT:856`) |
| NP-G24 | closed by `defect` once **M10** and **M14** exist | NEW ROW |
| NP-G25 | OUT OF SCOPE | `recruit` is troop-raising, FA/MB's (the lane brief §0 rule 7). NP's half is `hire` (V-06) |
| NP-G26 | closed by `give` once IN-12 B-R's Rung widening lands | the "no alignment cell" half is stale: `rosters.yaml:2992` gives `give` a `-0.2` cell |
| NP-G27 | closed by `tell` (the `confess` fold) | the value of `confession.made` is K-56's (FI/SC) |
| NP-G28 | PARKED: `consecrate` | trigger: H-100's revocation-cost reader or IN-23's legitimacy Query; owner GV |
| NP-G29 | closed by WITNESS (no verb: the cull of `mourn` is upheld) | grief is written by a death claim, `scar` and `stance` |
| NP-G30 | OUT OF SCOPE | conviction and pursuits move by `argue` (SC) and by consequence (H-62); `pray` is culled |
| NP-G31 | OUT OF SCOPE | dark attribute knobs are Part II's attribute dynamics; the body's rising arm is M1, under `tend` |
| NP-G32 | closed by GV's `revoke` / `confer` once **M10** exists | judging a revocation or a passing-over as a deed done to oneself |
| NP-G33 | closed by `commit` once **M15** exists | H-185 |
| NP-G34 | closed by `commit` once **M15** exists | H-191 |
| NP-G35 | OUT OF SCOPE | lying is SC's (J-C-6, caution 7) |
| NP-G36 | OUT OF SCOPE | cohort membership and muster belong to MB's troop stock |
| NP-G37 | OUT OF SCOPE | delegation and regency are GV's IN-48 (`WP5:178`) |
| NP-G38 | OUT OF SCOPE | a commander as a person fact is MB's (V116) and Part II's |
| NP-G39 | OUT OF SCOPE | a reader of an elevated subordinate's ambition is GV/FA's (on `confer`); not a verb |
| NP-G40 | closed by PC's `fight` and SC's `petition` once **M6** exists | the IN-58 grievance reaches candidates only under the `declared` arm |
| NP-G41 | closed by `train` (development) | creation is IN-47's held review (v2-head:347) and outside verb scope |

---

## 3.7 Mechanics this subsystem needs (named gaps)

| id | mechanic | what it must write or read | verbs waiting |
|---|---|---|---|
| M1 | an upward body arm: a MATTER rising arm and an upward band crossing in `_crossings` (`matter.py:35`) | `Person.body` up; a crossing Event a witness can hold (H-211) | `tend`; passive recovery |
| M2 | a care degree: the tender's capability as the obstacle's counterweight | the degree of `tend` | `tend` (later) |
| M3 | a source of capability keys and magnitudes (J-13's remainder), with a roster that refuses Thread Sensitivity at load (P-08, K-20) | the `Person.capability` keys `train` may raise | `train` |
| M4 | readers of `capability` in combat (`Combatant`) and in choice (`decision/`) | none (reads only) | `train` |
| M5 | a source of Proposition referents for a person's reach (K-49) | Candidate referents | `forgive` (field grudge) |
| M6 | the hostile-candidate polarity: H-194's `declared` arm (ED-IN-0296), so a negative stance raises a candidate against its object | the `score` term | PC `fight`/`challenge`, MB `march`, SC `petition` (avenge, NP-G40) |
| M7 | a typed `tie`: a content roster (friend, sworn, patron/client) and a reader that **gates** on the type | the `tie` Tenure's content | `tie` (and `court` once revived) |
| M8 | the partner operand for `tie`: a known-person operand on `give`'s `to` precedent (`VT:430-432`) | the operand bag | `tie` |
| M9 | a `kin` Tenure kind (directed; content `spouse`, later `child`), added to `release`'s `domain:` under load invariant 6 (`VT:858`) | `kin` Tenures | `marry`; later `betroth`, `rear` |
| M10 | a bond-deed judge: `deed_valence` (`person_q.py:314`) judges an act whose doer holds a live bond to its victim, and acts done to oneself (revoke, passing-over); plus `deed:` cells for `allegiance.changed` (IN-08 axes; H-205) | `regard`'s judged half | `defect`; the culled `betray`; NP-G32 |
| M11 | estate transmission at death (MATTER) | `hold` Tenures of a dead holder's estate | none in NP (it is not an act); flagged to EC/GV |
| M12 | a vacancy claim reaching the heir (H-206; IN-61's design-first check) | a question naming the vacant seat | `succeed` |
| M13 | a gift's effect on the receiver's regard: a `record.given` deed judged at `give`'s cells | `regard`'s judged half | `give` |
| M14 | a defection producer reading opinion at read (IN-70) | Candidate formation | `defect` |
| M15 | `commit`'s readers: an OUGHT's `predicate` (H-185) and whether a declared intent was kept (H-191) | none (reads only) | `commit` |

---

## 3.8 Cross-subsystem flags

| other lane | verb | the collision or dependency |
|---|---|---|
| FI | `knot` | Split from `tie` and moved to FI (fieldwork Knot; IN-32 = FI-05). The undirected read in `_ch_witness_key` (`VT:1245`) goes with it |
| FI | ledger eviction | Eviction of judged deeds ends a grievance silently (NP-G18). `forgive` covers the stored half only |
| SC | `tell` | Hosts `confess` (content: one's own deed). Lying (J-C-6, NP-G35) is SC's |
| SC | `court` | Owner if revived: a contest for consent whose stake is `marry` |
| SC / FA | `bribe` | Its own row (V-05); never a fold into `pledge`/`oblige` |
| SC | `argue` | The only writer of `pursuits` (H-62); the ground for culling `pray` |
| SC | `vouch`, `recant` | Refused candidates from NP-G21 that are speech acts |
| GV | `confer` | Hosts `designate` (`confer` of `off_heir`, IN-61) |
| GV | `consecrate` | Proposed owner of the parked act (seat legitimacy, H-100 / IN-23) |
| GV / SC | `pardon` | Kept distinct from `forgive` by whose state (NP-G19) |
| GV | `revoke`, `confer` | Judged as deeds done to oneself under M10 (NP-G32); a principal-agent reader (NP-G39) |
| GV | IN-48 | Regency and delegation (NP-G37) |
| GV / FA (owner of `release`) | `release` | L-08: rename its own-vow half `renounce`. Treachery moves off `release` onto `defect` + M10 |
| FA | `defect` | Changes faction membership atomically; FA's musters read membership |
| FA / SC | `commit` | Shared; `covenant` composes on it. NP keeps it as the person's binding to a Proposition |
| FA / MB | `recruit` | Troop-raising is its own row. NP's `hire` is not `recruit` (V-06) |
| FA | IN-70 opinion | Gains a kin term once `marry` exists |
| EC | `hire` | One row: a person or a company (a cohort, `weight > 1`). NP needs it for retainers. Owner to be reconciled; the wage is a `transfer`-shaped store write |
| EC | `give` / `transfer` | L-10 discriminator (Tenure vs stores). A person's gift of goods stays `transfer` |
| MB | `drill` | The troop half (unit quality) belongs to the troop stock; the person half folds into `train` |
| MB / SC | `surrender` | A preset of `give` (cession under arms); NP's `give` widening to Rung (IN-12 B-R) is its precondition |
| MB | NP-G36, NP-G38 | Cohort membership; command as a person fact |
| PC | `fight` | `tend` answers its wounds (PC-G39); M6 makes a grudge choose a fight; M4 makes `train` reach `Combatant` (PC-G15) |
| WT | `recover` | v2 filed `recover` under WT as well. NP folds the active half into `tend`; passive rest is M1 (MATTER) |
| TW | `pray`, `mend` | Any thread-side devotion is TW's. V-01's `mend` (a person's coherence recovery) is TW's, not `tend` |

---

## 3.9 For Jordan

The ladder (CLAUDE.md §0) was applied to every candidate. Only one item survives, and it is already
Jordan's.

1. **Births and the dynastic layer (ED-WR-0011, already `needs_jordan: true`).** Whether the cast
   generates people over time decides whether `rear` and a `child` kin content exist. The two answers
   lead to materially different games: a closed title game, or a game of generations. NP parks `rear`
   on it and asks for nothing new.

**Answered by the ladder (not escalated):**

* **D-V2, "is kin a tie kind?" (K-NPC-6).** Answered by **precedent** (the convention floor, the lane brief §0
  rule 4), so `marry` is kept. It is answered by **superseded** for the succession half: RS-27/RS-29
  ruled the heir a title, so kin is not a succession input. v2's option (b), "`marry` CUT", is
  withdrawn under the floor rule.
* **`succeed` CUT vs keep.** **Superseded:** IN-61 re-specifies the row as the heir's claim.
* **`oblige` → `pledge`.** Answered by **design document** (ED-IN-0179, CLAUDE.md §4), and no ruling
  kept the name.
* **`defect` as a row vs v2's `release` cell.** Answered by the **user's standing instruction** (no
  workarounds). It is left to the reconciliation (Part III §III.5)'s reconciliation at medium confidence, and is not a
  Jordan item.
