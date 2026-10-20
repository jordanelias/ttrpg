# Verbs, v2 — part 04: Part III, Verbs (critics, etymology audit, gap coverage, named mechanics, decisions)

## Status: PROPOSED (2026-10-17). Not ratified; merging ratifies nothing unless Jordan so rules. Static reading and static lookup only; no run.
## Parts, in reading order: [head](2026-10-16-verbs-01-thesis-and-persons.md) (§0, Part I Persons) · [`verbs-02`](2026-10-16-verbs-02-attributes.md) (Part II Attributes) · [`verbs-03`](2026-10-16-verbs-03-standards-roster-and-reconciliation.md) and **this file** (Part III Verbs: standards, roster, reconciliation; critics, etymology audit, gap coverage, named mechanics, decisions) · [`verbs-05`](2026-10-16-verbs-05-what-verbs-do-to-the-world-1.md) and [`verbs-06`](2026-10-16-verbs-06-what-verbs-do-to-the-world-2.md) (Part IV What verbs do to the world) · [`verbs-07`](2026-10-16-verbs-07-roadmap-reliability-and-sources.md) (§5 Roadmap, §6 Reliability ledger, §7 Sources) · [`verbs-08`](2026-10-16-verbs-08-engine-findings-from-the-first-trial.md) (Part V: engine findings carried from the first-pass trial) · Part VI, the lexicon by subsystem: [`verbs-09`](2026-10-16-verbs-09-lexicon-personal-combat.md) PC · [`verbs-10`](2026-10-16-verbs-10-lexicon-mass-battle.md) MB · [`verbs-11`](2026-10-16-verbs-11-lexicon-social-contest.md) SC · [`verbs-12`](2026-10-16-verbs-12-lexicon-fieldwork-and-inquiry.md) FI · [`verbs-13`](2026-10-16-verbs-13-lexicon-threadwork.md) TW · [`verbs-14`](2026-10-16-verbs-14-lexicon-settlements-and-governance.md) GV · [`verbs-15`](2026-10-16-verbs-15-lexicon-faction-actions.md) FA · [`verbs-16`](2026-10-16-verbs-16-lexicon-economy-trade-and-craft.md) EC · [`verbs-17`](2026-10-16-verbs-17-lexicon-world-travel-and-survival.md) WT · [`verbs-18`](2026-10-16-verbs-18-lexicon-npc-life-and-persons.md) NP · Part VII, the verb gap register (the evidence behind Part VI's coverage tables): [`verbs-19`](2026-10-16-verbs-19-gap-register-pc-and-np.md) PC+NP · [`verbs-20`](2026-10-16-verbs-20-gap-register-mb-and-fa.md) MB+FA · [`verbs-21`](2026-10-16-verbs-21-gap-register-sc-and-gv.md) SC+GV · [`verbs-22`](2026-10-16-verbs-22-gap-register-fi-and-tw.md) FI+TW · [`verbs-23`](2026-10-16-verbs-23-gap-register-ec-and-wt.md) EC+WT.

---

### III.7 The critics' findings, and what each lane did with them

Two Opus critics attacked the first pass before the lanes began. The **lexicon critic** read the 46 shipped rows, the 2026-10-03 name-fit pass, the registries and the equivalences (19 findings, L-01 to L-19). The **v2-claims critic** read v2's own verb claims, merges and counts (21 findings, V-01 to V-21). Their Latin and PIE chains were from memory and were not adopted unchecked; their design findings were checked against `engine/season/verb_table.yaml` and put to each lane. The table gives each finding in one line and each lane's answer in its own words (APPLIED, ANSWERED, REJECTED, NOTED); lane references are to the Part VI section of that subsystem. **Every one of the 40 findings is answered by at least one lane.** The two findings the critics made with highest confidence were verified directly: `oblige` runs against ordinary English (`eligibility: ["own"]`, emits `duty.taken`: the actor binds themself), and `dispatch` is the documentless order (`writes: []`, emits `order.given`) while a "dispatch" in ordinary use is a written message.

| id | finding | per-lane disposition | lanes disagree? |
|---|---|---|---|
| L-01 | Root sense used as design intent (etymological fallacy); bad glosses | PC APPLIED "no design claim here rests on a root"; NP APPLIED "Every fit verdict ... by usage"; MB APPLIED "every design claim ... ordinary usage"; FA APPLIED "no merge, gap or node rests on a root"; SC APPLIED, partly answered on *persuade* ("make sweet" is a reconstructed causative); GV APPLIED; FI APPLIED, partly answered (*surveil*, *survey* chain); TW APPLIED "Latin notes are remarks only"; EC APPLIED; WT APPLIED | no |
| L-02 | `oblige` reverses direction; rename (`pledge`/`swear`) | NP APPLIED renamed `pledge`, v2 folds of recruit/suborn/bribe struck; SC ANSWERED prefer `pledge` (`swear` is SC's oath, SC); FA APPLIED no FA act folds into `oblige`, rename "flagged to GV/NP"; FI ANSWERED `infiltrate` unaffected by rename; EC APPLIED to `hire`, "rename itself is NP/FA's"; PC cross-lane note | no (all converge on `pledge`; each defers the rename to NP) |
| L-03 | `levy` FITS overturned; stale `levy` citations now name a different act | MB APPLIED `levy` names troop act, TS-L re-key must land first; FA ANSWERED troop sense ordinary, re-key first; GV APPLIED store act is `requisition`, re-key is TS-L's; EC APPLIED with caution, "re-key by sense, not by string" | no |
| L-04 | `carry` event `petition.carried` reads as adopted; rename `lodge` | SC APPLIED `lodge`, `petition.lodged`; EC ANSWERED not EC's row, EC uses `lodge` | no |
| L-05 | `dispatch` is a documentless order, but a dispatch is a written message | FA ANSWERED, FA REBUILD name kept ("objection rests on the noun"); GV APPLIED "renamed `order`"; MB ANSWERED "dispatch troops fits", verb row is FA's | **yes** |
| L-06 | `work` holds two senses (exploit a site vs build) | EC APPLIED (EC, S1/S3 rebuilt); MB APPLIED fortify goes to `restore`, not `work` | no (but see V-21 on fortify) |
| L-07 | `establish` covers two acts; `found`/`establish`/`build` near-synonyms | GV APPLIED `amend` named, discriminator stated ; FA FLAGGED GV's; EC ANSWERED `found`/`build` kept apart, `establish` GV's | no |
| L-08 | `release` of own vow/oblige reads wrong; use `renounce` | NP ANSWERED, FLAGGED, `renounce` fits (NP-ish); GV ANSWERED GV uses fit, flags `commit`/`oblige` to NP/SC; SC ANSWERED `deny`/`withdraw` keep names; FA FLAGGED, `renounce` "supports it"; TW ANSWERED, rename "would read worse" for held shapes | **yes** (mild) |
| L-09 | `survey`/`surveil` one letter apart, both take a Rung | FI APPLIED "rename to `watch`" ; GV ANSWERED `survey` stays FI's, `assess` parked | no |
| L-10 | `give`/`transfer` near-synonyms split by object | NP ANSWERED discriminator is the carrier, no rename; FA CONSISTENT; EC ANSWERED kept by object, no rename; NP | no |
| L-11 | `forge` event kind `record.forged` leaks; proposal stale; verb etymology | FI APPLIED emit twin kind `faction.surveyed`, verb path via *fabricō*; SC APPLIED to `lie`'s revival, "forge leak itself is FI/EC's"; EC NOTED | no |
| L-12 | Proposal lexicon stale vs verb table; `accept`, `challenge`, `seize`, `requisition` unjudged | PC APPLIED `accept` STRAINED, row rebuilt to require a challenge; NP APPLIED NP-G23 STALE; MB PARTLY; SC APPLIED; FA APPLIED `seize` judged FITS; FI APPLIED; WT APPLIED `march` current | no |
| L-13 | `speak`/`utter` synonyms; `utter` legal false friend | SC APPLIED renames `utter` to `declare` ; FI ANSWERED forgery planted by `give`, no FI change | **yes** (indirect: FA has a NEW `declare` row, FA, and does not cite L-13) |
| L-14 | `comply` gloss contradicts row (writes nothing) | GV APPLIED "the row writes nothing (VT:161)" | no |
| L-15 | `create_record`/`destroy_record` CRUD names | FI ANSWERED noted not applied (no retrofit, §4), FI; EC-no | no |
| L-16 | Loose derivations (*reconstruct*, *open_case* etc.) | SC APPLIED *open_case* = *cāsus* 'a fall; event'; FI APPLIED *reconstruct* not a Latin compound  | no |
| L-17 | `challenge` vs "Recognition Challenge" silo collision | PC ANSWERED roster provisional, "flagged to SC rather than renaming"; SC ANSWERED "not an SC verb; flagged to PC"; PC says SC should use `dispute` | **yes** (each lane hands it to the other; nobody decides) |
| L-18 | `remit:issue` gates `requisition`/`seize`/`transfer` | FA NOTED rename is GV/IN's; GV ANSWERED "Flagged, not decided"; EC ANSWERED substitution is tree precedent, GV to confirm | **yes** (mild: EC keeps, GV leaves open) |
| L-19 | `synonym_registry.yaml` lacks verb renames; lists retired Key | NP FLAGGED each rename "would need an entry there. Not edited here"; TW observation, `sever`->`dissolve` one more unrecorded rename | no |
| V-01 | `mend`/`restore` both cover Mending | TW APPLIED `mend` = Mending, `restore` fabric only (TW ruling, IN-35 arm re-pointed); EC APPLIED `restore` fabric only ; NP cross-ref "V-01's `mend` ... is TW's, not `tend`" | no (critic's "fold into `mend`" reading is applied to the opposite verb: TW keeps both verbs, splits by object) |
| V-02 | REJECT->MERGE classed three ways; counts wrong | PC APPLIED AND WIDENED "never merges ... nine items that are not verbs" ; MB ANSWERED `endure` battle sense is a named content of `withstand`; WT APPLIED `endure` CULLED in season, battle sense moved to MB | no |
| V-03 | "each keeps a name" vs tally (withdraw, loosen, peace) | SC ANSWERED `deny`/`withdraw` keep names, "count is the orchestrator's"; GV ANSWERED `abdicate`/`resign` named folds; TW APPLIED `loosen` counted as named folded content | no |
| V-04 | `mediate` is not `arbitrate` | SC APPLIED (`arbitrate` folds into `determine`, `mediate` PARKED, SC); FA APPLIED "S1 not folded", FA | no |
| V-05 | `bribe` is not `suborn` | NP APPLIED "briber's act is `bribe`, SC/FA's own row"; FA APPLIED `suborn` culled, "turn into `recruit`" ; FI APPLIED `suborn` a parked content of `bribe` ; SC ANSWERED FA's, SC supplies `lie` | **yes** (FA: `turn` is a content of `recruit`; FI: `suborn` is a content of `bribe`) |
| V-06 | `hire` -> `oblige` contradicts `recruit` -> `tell` (voice) | NP APPLIED `hire` own row in hirer's voice, but REJECTS V-06's `tell`+`oblige`+`transfer` fix; EC APPLIED one employer's row ; FA APPLIED "hire folds into `recruit`" ; MB APPLIED MB's `recruit` in recruiter's voice, "`hire` is NP/EC's" ; FI CHECKED `infiltrate`/`bribe` already in actor's voice | **yes** (NP/EC: `hire` is a new row; FA: `hire` folds into `recruit`) |
| V-07 | `lock` merged into `weave` though twin is Dissolution | TW APPLIED `lock` own row in Locking/Dissolution suite  | no |
| V-08 | `sever` coined where `dissolve` exists | TW APPLIED renamed `dissolve` ; corrects critic's VL chain | no |
| V-09 | `betray` merged into `release` is really repudiation | NP APPLIED `betray` culled as a verb, judgement across acts (M10), name passed to `release` owner; FA APPLIED "betrayal is a witness judgement"  | no |
| V-10 | `command` counted as a choice but is a stat; name `tactic` | MB APPLIED, DIFFERENTLY: `command` culled as a verb; `tactic` "not adopted, a noun"  | no |
| V-11 | `invest` reads as money | MB APPLIED posture names `besiege`/`storm` ; EC SUPPORTED | no |
| V-12 | §IV.4 lever (root sense) asserted, not defended | SC APPLIED (with V-14, Suite 7); FI APPLIED (§3.4 attested senses); WT APPLIED no WT node from *march* root | no |
| V-13 | §IV.4 glosses misstate roots (*issue*, *challenge*, *fight*, *march*...) | PC APPLIED *fight*; PC APPLIED *challenge*; SC APPLIED *challenge* ('false accusation'); GV APPLIED *issue* 'go out', *confer*; FI APPLIED *research*/*surveil*; MB *march* root disputed; WT | no |
| V-14 | Role names in §IV.4 differ from §IV.7 roster; "deceiver" vs construe | SC APPLIED (cited with V-12, "`construe` called deceiver ... Suite 7") | no |
| V-15 | `tax` depends on retired `evade / defy` | FA ANSWERED, FLAGGED, `evade / defy` retirement "must be reversed before either lands" ; GV APPLIED "`tax` no longer depends"; "slash row is split, not retired into `comply`"; EC ANSWERED `tax` no longer an issued writ, EC-G04 PARKED ; MB ANSWERED draft evasion PARKED until FA rebuilds `evade / defy` | **yes** (FA: reverse retirement; GV: split the row) |
| V-16 | ransom -> `pardon` + `transfer` wrong (pardon is mercy) | FA APPLIED captor's act is discharge of a `detain`, ransom is a `covenant` content ; PC ANSWERED agrees, PC supplies producer `capture` ; GV APPLIED `pardon` is grace, flagged to FA ; EC NOTED FA's, payment half is `pay` | **yes** (mild: FA: payer's `transfer`; EC: payment is `pay`; PC: `capture` is the producer) |
| V-17 | `bless` really consecration | NP APPLIED renamed `consecrate`, PARKED, owner GV  | no |
| V-18 | "Sixteen merges filed against wrong row" miscounted; leap, withdraw | TW AGREED, "leap is a stage, not a merge"; WT APPLIED `hunt` does not go into `work` | no |
| V-19 | Same-root collisions (`due`/`debt`, `guard`/`ward`, `convene`/`covenant`, *struō*) | PC ANSWERED `guard`/`ward` kept apart by object ; MB NOTED; FA APPLIED `tribute` not `due`, `covenant`/`convene` kept; SC ANSWERED kept; GV APPLIED content named `tax`, no `due` writ; FI ANSWERED no change ; TW ANSWERED real doublet, flagged to PC; EC APPLIED no `due` | no |
| V-20 | `yield` homonym with `Rung.yield` and inquiry yield | PC APPLIED `yield` kept, kinds prefixed `fight.yielded`; FI APPLIED product called a "finding", no `yield` kind; EC NOTED "a duel term `yield` ... is PC's to rename"  | **yes** (PC keeps the term; EC expects PC to rename it) |
| V-21 | Names kept without engaging in-tree STRAINED verdicts (`dispatch`, `speak`, `work`, `tie/knot`); `Fortify`/`Trade` unnamed | NP APPLIED `tie`/`knot` split; SC ANSWERED `speak` STRAINED today, FITS once rebuilt, `utter` renamed instead; EC APPLIED Trade -> `exchange`, Fortify -> `build` ; PC cites V-21 for provisional roster | **yes** (EC: Fortify -> `build`; MB: fortify -> `restore` for condition, `build` for new walls) |

**Where lanes disagreed, and the ruling** (all in `verbs-03` §III.5):

| finding | disagreement | ruling |
|---|---|---|
| L-05 `dispatch` | FA keeps the name and rebuilds the row; GV renames it `order`; MB defers | R-05: two acts, `order` and `assign`; the shipped name stands until Jordan rules (D-V7) |
| L-08 `release` / `renounce` | NP, FA, GV say `renounce` fits an own-vow close; TW says it reads worse for held shapes | R-16: `release` stays; open at medium confidence |
| L-13 `utter` → `declare` | SC renames `utter`; FA adds a seat-level `declare` | R-06: FA's `declare` stands; SC's rename withdrawn; `propound` is the candidate |
| L-17 `challenge` | PC and SC each hand the word to the other | R-24: `challenge` is the duel (PC); a claim is `dispute` (SC) |
| L-18 `remit:issue` | EC keeps it as tree precedent; GV leaves it undecided | open: H-52's eligibility question; not decided here |
| V-05 `suborn` | FA files `turn` under `recruit`; FI files `suborn` under `bribe` | R-21: two different acts |
| V-06 `hire` | NP and EC make it a new row; FA folds it into `recruit` | R-01: EC's row; FA's fold reversed |
| V-15 `evade / defy` | FA wants the retirement reversed; GV splits the row | GV's split: `evade` and `defy` are two rows |
| V-16 ransom payment | FA says `transfer`; EC says `pay`; PC names `capture` as the producer | R-17: payment is a `transfer` (`pay` is its fold); the producer is `capture`; the name `pardon` is open |
| V-20 `yield` | PC keeps the term with prefixed kinds; EC expects PC to rename it | R-19: PC keeps it; event kinds are `fight.yielded` |
| V-21 / L-06 `fortify` | EC routes it to `build`; MB routes the condition arm to `restore` | R-03: new works are `build`, upkeep is `restore` |


### III.8 The etymology audit

**The standard** is S-5: every verb carries a chain English ← Middle English ← French or other intermediate ← Latin lemma with principal parts and the attested sense (Lewis & Short) ← PIE root where attested, or says plainly that the word is Germanic, Frankish, Celtic, Arabic or of unknown origin. Each lane built its chains with the lookup tool (Wiktionary raw wikitext, and Lewis & Short through Perseus). Two independent Opus auditors then re-opened every source for every chain, without trusting the lanes, and the corrections below were applied to the lane sections before they were filed as Part VI.

| auditor | lanes | chains checked | confirmed | corrected | `[UNVERIFIED]` tags resolved |
|---|---|---|---|---|---|
| E1 | PC 26, NP 35, MB 28, FA 42, SC 47 | 178 | 142 | 36 | 47 (13 remain) |
| E2 | GV 46, FI 29, TW 19, EC 35, WT 15 | 144 | 113 (11 more sound apart from one sub-claim) | 18 | 35 |
| **both** | ten lanes | **322** | **255** | **54** | **82** |

**What the audit found, worst first.**

- **A Latin ancestor that was not one.** MB `recruit`: the path through L *recrēscō* was forced; the compound formed in French (*recruter* ← *recrue* ← OF *recreü*, from *recreistre* = *re-* + *creistre* ← *crēscō*). GV `repeal`: OF *rapeler* is *re-* + *apeler* ← L *appellō*, not L *repellō*; Wiktionary's English page contradicts the Old French pages it rests on. GV/TW `release`: OF *relaissier* is its own compound on *laissier* ← L *laxō*; L *relaxō* is a parallel compound, not the ancestor.
- **A gloss given to the wrong Latin verb.** GV `abolish`: 'decay, vanish' is the sense of *abolēscō*; *aboleō* means 'to destroy, efface' (L&S), and the two Wiktionary pages disagree on the root.
- **A root given as certain that is disputed.** GV `succeed` (*cēdō*, PItal \**kezdō*, root disputed), `trahō`, `arguō`, MB `march` (the Late Latin \**marcare* origin is in no source that could be reached; Frankish \**markōn* is the sourced path).
- **A direction reversed.** WT `travel`: the OF noun *travail* is deverbal from *travailler* (← VL \**tripāliāre* ← LL *tripālium*), not the reverse.
- **A wrong fact about ordinary use.** PC `disengage` quoted the fencing sense, which is the noun; the verb covers forces breaking off combat. GV `charter` claimed a frequency Wiktionary does not give.
- **About thirty loose links:** dropped stages (FA `treaty`, `tribute`, `league`, `plot`, `war`; NP `crown` omits its Greek source), alternatives not stated (FI `scout`: *ḱlew-* or *ḱel-*), and PIE roots given without their uncertainty (FI `search`, `suborn`, `blackmail`).

**The pattern.** Three of the four worst findings came from trusting the English Wiktionary page where the Old French entry it rests on says otherwise. **No lane forced a Latin path onto a Germanic, Frankish or unknown word**, and every such label the auditors checked is correct.

**Latin and Germanic in the roster.** By a keyword classification of the lexicon cells (approximate, to be read as ±3), about 59 of the 92 verbs reach Latin, directly or through French; about 33 do not. Those are Germanic (`fight`, `give`, `build`, `tell`, `speak`, `work`, `weave`, `lock`, `ward`, `knot`, `tie`, `hire`, `lend`, `borrow`, `forgive`, `utter`, `watch`, `drill`…), Frankish or Germanic through French or Medieval Latin (`march`, `seize`, `guard`, `marshal`, `forage`, `disband`), or of unknown origin (`bribe`, `craft`), or of Arabic origin (`assassinate`, a Medieval Latin carrier only). For these, Part VI says "Germanic, no Latin path" and names the Latin cognate through PIE where Wiktionary gives one, labelled *cognate, not ancestor* (`fight` ~ L *pectō*; `hoard` ~ L *custōs*; `lend` ~ L *linquō*; `read` ~ L *reor*; `thread` ~ L *terō*).

**What remains `[UNVERIFIED]`.** About twenty-five sub-claims, nearly all of them the century of a sense shift or the intermediate French form, which need the OED, the Middle English Dictionary or TLFi. None was reachable (Etymonline returned 403; TLFi and the MED refused the fetch). They are tagged where they stand. No design claim rests on one (S-5).

**How to read a chain in Part VI.** `←` reads "derives from". A Latin lemma is given with its principal parts as Lewis & Short has them (*revocō, -āre, -āvī, -ātum*) and in quotation marks the sense L&S attests, never a paraphrase of its parts. `Wikt` is the English Wiktionary (which cites De Vaan's *Etymological Dictionary of Latin* for Latin roots), `L&S` Lewis & Short, `Wikt-OF` and `Wikt-la` the Old French and Latin entries. A PIE root is the one Wiktionary gives; "disputed" means its Latin entry says so.

### III.9 The gap register, disposed of

Part VII holds 488 verb gaps, shortfalls, name defects, collisions and deferrals, each with its source, the verbs the source names, its precedent documents and the first pass's disposition. **The first pass left 189 of them (39%) with no disposition at all** (`NONE` in the register's last column). Every one of the 488 now has exactly one disposition in its subsystem's coverage table (Part VI, §3.6 of each section), checked by script.

| sub | gaps | closed by a verb or suite | parked on a named trigger | out of scope (with owner) | stale (cite the tree) | disputed | first pass: no disposition |
|---|---|---|---|---|---|---|---|
| PC | 40 | 27 (23 once a named mechanic exists) | 1 | 11 | 0 | 1 | 14 |
| MB | 57 | 41 | 7 | 7 | 2 | 0 | 19 |
| SC | 59 | 36 (26 once a named mechanic exists) | 9 | 10 | 2 | 2 | 34 |
| FI | 58 | 45 (27 once a named mechanic or J-T1 exists) | 5 | 5 | 0 | 3 | 26 |
| TW | 42 | 29 | 6 | 5 | 2 | 0 | 13 |
| GV | 45 | 27 (16 once a named mechanic exists) | 6 | 9 | 3 | 0 | 12 |
| FA | 50 | 25 | 6 | 18 (mostly handed to GV) | 1 | 0 | 18 |
| EC | 53 | 33 | 9 | 9 | 1 | 1 | 23 |
| WT | 43 | 20 | 6 | 15 | 1 | 1 | 19 |
| NP | 41 | 29 | 3 | 8 | 1 | 0 | 11 |
| **total** | **488** | **312** | **58** | **97** | **13** | **8** | **189** |

*Closed* means a roster verb or suite answers the gap **once its named mechanic exists**; it does not mean the engine does it today. Where a lane counted how many of its closures wait on a mechanic, the count is in parentheses; the other lanes did not count. *Out of scope* is never silent: each row names the subsystem or document that owns it. *Stale* rows are gaps the tree has since closed or renamed. *Disputed* rows are the eight where the lane could not say which reading the sources support; each says why. By the register's own kind column the rows are: missing verb 125, missing reader 118, missing carrier 66, shortfall 61, other 58, collision 36, name defect 24.

### III.10 The named mechanics the roster waits on

The lanes name **127 mechanics** (PC 15, NP 15, MB 12, FA 10, SC 15, GV 14, FI 10, TW 12, EC 16, WT 8): the carriers, readers and rules a verb needs before its world effect exists. Each is numbered in its lane (`M1`, `M-1`, `M-WT-1`, `M-EDICT`) with what it must write and the verbs that wait on it. The first-pass reading, that the game is short of readers, holds. Fourteen of them are named by more than one lane. They are the shared carriers; building one unblocks several subsystems, and building it twice would be two owners of one fact (`CLAUDE.md` §8).

| shared mechanic | named by | verbs waiting |
|---|---|---|
| **troop stock, recruit pool, field force, order of battle** (J-1 and a Layer 1 amendment) | MB M-1 to M-3, M-8; FA M4; WT M-WT-8; EC M2 (arms) | `levy`, `muster`, `drill`, `disband`, `marshal`, `supply`, `forage`, `march`, `recruit` (for a force) |
| **the `edict` Record and its MATTER readers** (tax, draw, ban term, price cap) | GV M-EDICT, M-TAX, M-DRAW; EC M7, M10 | `tax`, `ration`, `proclaim`, `exchange`, `transfer`, `embargo` (parked) |
| **the finding producer; failure is not refusal; the honest misreading** | FI M1 to M3; TW (`thread_read`) | all six inquiries, `thread_read` |
| **the concealment grade and the cover read** | FI M4; PC M6; FA M7 | `conceal`, `forge`, `assassinate`, `ambush`, `conspire`, `infiltrate` |
| **the proofs reader, including `forgery_quality`** | SC M9; FI M4, M9 | `determine`, `tell` at a venue, `interrogate`, `forge` |
| **a count of `commit`s** (one count) | SC M12; GV M-COUNT | `commit` (vote), `confer` (elect) |
| **the custody opener** (`detain` from a fight or a writ) | PC M5; GV (`arrest`) | `capture`, `arrest`, `pardon`, `rescue`, `interrogate` |
| **the `debt` Record and the wage edge** | EC M9, M11; FA (tribute); GV (distraint) | `borrow`, `lend`, `hire`, `pay`, `tribute` |
| **a public channel that survives SC-01 step 13** (D-V3) | SC M4; FA M6 | `declare`, `deny` (a content of `release`), `proclaim` |
| **a mood-keyed alignment cell** (D-V6) and the reader of `at_war` | SC M13; FA M1 | `utter`, `declare`, the charge, `threaten` |
| **the route Query and the calendar** | WT M-WT-1, M-WT-2; EC M3; MB M-6 | `travel`, `explore`, `haul`, `march`, `besiege` |
| **a labour input to yield** | EC M1; GV M-LABOUR | `work`, `build`, `assign` |
| **the end of a Site or a Rung** (H-166) | GV M-RAZE; EC M13; MB M-9 | `raze` (one effect, one owner) |
| **capability and attribute readers** | NP M3, M4; PC M13; MB M-10 | `train`, `fight`, `march`, `marshal` |

### III.11 Items for Jordan

Each lane applied the five answer-it-first tests (superseded · irrelevant · design document · precedent · architecture) to every open item. **Twenty-one survived**, because two defensible options lead to materially different games or an answer would overwrite ratified canon. The first six carry the first pass's numbers (D-V1 to D-V6); D-V7 onward are new. The default is the lane's recommendation, not a ruling.

| id | question | options | default (lane) | lane |
|---|---|---|---|---|
| **D-V1** | May a living top-seat holder be removed against their will (ARC-40's replaced arm)? | (a) no: `depose` cut, ARC-40 narrows to "act or abdicate"; (b) yes: a removal basis on `revoke` | `depose` parked | GV |
| **D-V2** | Do births exist (ED-WR-0011)? The first pass's D-V2 (kin as a tie kind) is answered: `marry` stands by the convention floor | closed title game · game of generations | `rear` parked | NP |
| **D-V3** | What public channel survives SC-01 step 13's deletion of `chronicle`? | keep · a named surviving channel · co-located only | a named surviving channel | SC, FA |
| **D-V4** | J-C-6: may persons lie? | yes · no | **yes**, built after the proofs reader (SC M9), then `lie` as a row sharing `tell`'s cell | SC |
| **D-V5** | R-7: does a withdrawn army differ from a routed one? | no · yes | yes | MB |
| **D-V6** | A contents-aware value term, or a mood-keyed alignment cell? | build · refuse | the mood-keyed cell first | SC, FA |
| **D-V7** | The shipped `dispatch` (a documentless order): keep the name, or `order` for it and `assign` for the posting act (R-05)? Overwrites ED-IN-0210 | keep `dispatch` for the order, add `assign` · rename | `assign` added; `dispatch` kept until ruled | FA, GV |
| **D-V8** | The field force: troops that travel with a march and keep their own side. Amends ratified Layer 1 (with J-1) | adopt · keep stocks at the rung | adopt (MB M-1) | MB |
| **D-V9** | Does a march between factions require war? | war gates violence (CK3 [MEMORY]) · war is a state values and witnesses read (Total War [MEMORY]) | none | MB, FA |
| **D-V10** | Does a treaty bind the signer or the seat? | lapses when a head dies (edges are persons') · an edge on the seat survives the holder | none | FA |
| **D-V11** | Who may declare war? | any holder of a seat with `remit:dispatch` · the faction's head seat only | none | FA |
| **D-V12** | May a won contest open an edge the counterparty owns (`recruit`, `conspire`)? | yes (as `confer` and `determine` already do) · no (the counterparty's own act) | yes, since Jordan's rule forbids the reply-act workaround for a floor verb; may overwrite an autonomy axiom, `[UNVERIFIED: whether one is ratified]` | FA |
| **D-V13** | The draw policy under scarcity: who eats, in what order, how much? | the shipped sorted-id walk · a ruled policy | blocks `ration` | GV |
| **D-V14** | Does the road cost a named person anything but time? | only Calamity territory · weather also | only Calamity | WT |
| **D-V15** | Can a person or force be *between* places? Amends ratified Layer 1 (`contain : Rung → Rung`) | no · yes | no | WT |
| **D-V16** | How does a questioned person answer an `interview`? | (a) a Layer 1 carve-out reading their ledger · (b) the reply as their own act next season | (b) | FI |
| **D-V17** | Does `guard` get its own edge (an eleventh Tenure kind)? Can a seatless captor hold a prisoner (widens `detain`)? | own edge / a query over `oblige` and presence · seatless custody / seat-holders only | none | PC |
| **D-V18** | Unpaid upkeep: does the term lapse, or become a debt the seat owes? | lapse (shipped) · arrears | none | EC |
| **D-V19** | Threadwork: how does Coherence's elastic return enter the season loop? Are knots permanent? What follows the crossing? | a licensed clock · a chosen rest · permanent · releasable | none | TW |
| **D-V20** | Is `sack` kept, given its tone (FASE FA-6 marks it `needs_jordan`)? | keep as a content of `forage` · drop | keep (precedent) | MB |
| **D-V21** | Does a levied stock go home after a term, and does a recruited stock need upkeep? | no term, no upkeep (the base) · a service term and upkeep | no term | MB |

Persons and attributes keep their decisions (`verbs-07` §5: J-T1, J-T2, J-T4, V-2a, R-0). The rename batch (R-10) and the held name `dispatch` (D-V7) touch goldens; each needs the plain statement that a golden was re-recorded.

### III.12 Limits

- **Nothing here ran.** The coverage tables, the mechanic lists and every statement of what the code reads are static reading, carried from the lanes; where a lane did not open a call site it says so.
- **Precedent games are from memory.** Every game named in a lane and tagged `[MEMORY]` is unchecked; in-tree precedent documents are cited by path and were opened by the lane that cites them. Several research documents the register cites were read only through a lane file; the rows say so.
- **The gap register was extracted by readers** (five Sonnet lanes) and not independently sampled. The lanes checked their own subsystem's rows; one found stale rows and corrected them.
- **The reconciliation (§III.5) has no critic.** It is one author's ruling over ten lanes. The rulings are marked contestable where a lane argued the other way.
- **The attribute work is not re-derived** against the 92-verb roster (`verbs-02` note).
- **Renames touch goldens.** R-10 changes act ids that hash the verb name; the batch must declare its hash move and re-record the pins plainly.
- **The count of 92 is a proposal.** It predicts nothing about play until the mechanics of §III.10 exist and a falsifier has run (`CLAUDE.md` §0.2: done means it executes).
