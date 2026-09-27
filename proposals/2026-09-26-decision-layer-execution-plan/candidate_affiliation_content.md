# CANDIDATE — affiliation roster, verb×affiliation table, and crisis threshold-3 recommendation (draft, 2026-09-27). RATIFIES NOTHING. Every value either cites its source or is marked null with a stated reason. Pending Jordan's approve/vet.

## Status: **DRAFT FOR JORDAN'S REVIEW. Not canon, not a ruling, not wired to anything.**
## Authority: **none.** Nothing here lands until Jordan approves it. The owners it would land at (`references/descriptor_registry.yaml` for the roster, `engine/season/rosters.yaml` for the `incompatible` table and any verb×affiliation table, `proposals/2026-09-18-conviction-basis-worksheet.yaml` as the authoring surface) are **untouched** by this file.
## Scope: C3 (the affiliation roster, the ten `incompatible:` cells, `intensity.scale` / `player_sees` / `bands`), C4 (verb × affiliation engagement), and a recommendation on G-Q6 (crisis threshold 3's terminal branch) — per `PROPOSAL.md` §3.4, §3.5 H13 and §5 Q3/Q4/Q6.
## Companion: `candidate_pursuit_cells.md` (C1/C2/G-Q5) — not duplicated; where the two touch (the `faith` row, the `sacred` column, `tell`/`speak`) this file points at it.
## Method: **corpus-mined, not invented.** Every cell carries a grade (§0.2). Quarantined `.designs/` documents are read as SOURCES for Jordan's own review and are labelled **quarantined** wherever cited (`CLAUDE.md` §1: not authority, not a session's input to a gate).
## Grade under `CLAUDE.md` §0.2: `paper` throughout. Nothing here executes.

---

## §0 · How to read this file

### 0.1 What R1/R2/R3 fix, and what they leave open

The ruled architecture (S1) is: `conviction` = a **vector over religious affiliations** with a per-affiliation **intensity**; **confliction is DERIVED** from an `incompatible` relation and never stored; the old `Truth` 0–5 pole is **absorbed**, its two poles becoming two affiliations a person may hold at full intensity at once. R3: the roster, the pairs and the intensity are **Jordan's to author**. This file derives candidates for those three things from what he has already written. It does not decide them.

### 0.2 Grades

| grade | means |
|---|---|
| **cited** | transcribed from a source that states it — a ruling text, or Jordan's own words as quoted in the tree |
| **derived** | the DIRECTION (true/false, keep/strike) follows from cited prose; the inference is mine and named |
| **null** | no citable basis found; the reason is stated in the cell |
| **CONFLICT** | two sources disagree; both shown, a primary named, the choice flagged in §6 |

### 0.3 Sources (S-numbers used throughout)

| id | source | status |
|---|---|---|
| S1 | `registers/editorial_ledger_in_archive.jsonl:167` (ED-IN-0251 row 1, 2026-09-18) and `:168` (row 2, 2026-09-19, `supersedes_row: true`) — R1/R2/R3; row 2's source line is Jordan verbatim: *"Truth becomes Conviction"* | ruled |
| S2 | `proposals/2026-09-18-conviction-basis-worksheet.yaml:39-85` — the five candidates with their `canon:` cites (`:39-59`), the `intensity:` block (`:63-66`), the ten pairs (`:71-81`), and **Jordan's worked example as the worksheet quotes him** (`:83-85`): *"devoutly Solmund but also believes in Threadwork and therefore experiences religious confliction"* | authoring surface (superseded as a whole, but §1 carried forward per its own banner `:7-8`) |
| S3 | `canon/philosophy/08_history.md` §8.7 (`:204-285`), §8.8 (`:287-336`), §8.9 (`:338-367`), §8.10 (`:369-392`), §8.11 (`:394-410`) — the live history: the Church worships Solmund, the doctrine derived from what he was, the prophylaxis, the category error, the northern betrayal | live canon suite (file head says `Status: PROPOSED`; it carries the 2026-09-07 rulings) |
| S4 | `canon/philosophy/RULINGS.md:201-226` — **D-10, Jordan verbatim**: *"The Church's God is Solmund, the threadcut being who performed what people saw as miracles … people worship Solmund as a deity. Don't fall into some trap about a false God necessarily being antagonistic"*; and `:592-624` (`:592` Mending at scale, Jordan verbatim; `:602-611` the knife-edge; `:621-624` "the Church's persecution" among the reasons the Locked Zones stand) | rulings |
| S5 | `canon/philosophy/05_confrontation_and_sensitivity.md:332-347` — §5.7, the live text on the inner tradition's transmission | live canon suite |
| S6 | `canon/00_philosophical_foundations.md` §9.1–9.3 (`:247-267`), §10.2 (`:281-285`), §11 (`:287-291`), §14 (`:325-329`) — the worksheet's own `canon:` cites; SUPERSEDED by S3/S5 per its banner but kept so those cites resolve | superseded canon, cited for the worksheet's lineage only |
| S7 | `canon/03_canonical_timeline.md` — `:44-68` Church formation and Altonian containment (`:64` *"Altonia's own population includes a significant Solmundan minority"*; `:66` Altonia destroys Einhir records); `:94-100` the caste; `:118-121` Church objects to Schoenland trade, *"its Altonian missionaries quietly benefit"*, *"Altonia's Church minority growing"*; `:138-145` key figures | canonical |
| S8 | `canon/04_game_design_constraints.md:28` GD-1 — *"Altonian Theocracy PP-414"* STRUCK as a victory path; *"Varfell Threadwork first-mover + Einhir Revival"* as a faction lever; `:30` GD-3 — Restoration Movement *"anti-Church identity"* | canonical (mutable) |
| S9 | `registers/editorial_ledger_in_archive.jsonl:54` (ED-IN-0075, 2026-07-18) — *"Keeps Certainty's engine-internal 0-5 spine … players see qualitative bands only (Orthodox..Accepted), never the number. Poles: 5 = Himmelenger (Solmund orthodoxy), 0 = Edeyja (Thread as metaphysical foundation)"* | resolved ruling, absorbed by R2 |
| S10 | `engine/engine_params/params_tables.yaml:3145-3178` — the frozen capture of the Truth row and its six labelled bands (5 Orthodox · 4 Faithful · 3 Questioning · 2 Skeptic · 1 Transitional · 0 Accepted, each with an "operative belief" gloss) | frozen reference (`CLAUDE.md` §5) |
| S11 | `.designs/systems/characters/reference/conviction_track_v1.md` §2 (`:40-66`) and §3 (`:72-95`) — the scar table, the crisis d6, the terminal triad, the Thread-event × Conviction matrix | **quarantined** |
| S12 | `.designs/systems/factions/reference/faction_canon_v30.md:567-637` — Church mission (`:588-596`: contradicted categories `da.covert_betrayal`, `da.antinomian_action`), institutional beliefs (`:612-614`), substrate posture (`:629`), Ob modifiers (`:634-637`: *"Reveals Thread truth: +2 Ob"*) | **quarantined** |
| S13 | `.designs/systems/world/reference/solmund_master_document.md` — §2.3 (`:60-66`), §3.3 (`:100-106`), Böhme (`:118-122`), §4.4 (`:150-155`, RM's Lurianic theology), Celan (`:158-162`), Levinas (`:214-224`), §11 (`:260-272`, the two witness traditions), §12 (`:274-290`, the Seam Text), §16 (`:331-337`, orthodox / heterodox / **forbidden** vocabulary), §18 (`:355-366`, tonal register by Truth value) | **quarantined** |
| S14 | `.designs/systems/characters/reference/conviction_track_v30.md:30-34` (PT: *"0 = Einhir Restoration pole. 5 = Solmund Orthodoxy pole"*), `:59-63` (T15 fixed at 0), `:269-295` (§4.2 *Altonian Theocracy Path*, PP-414, SUPERSEDED-BY GD-1) | **quarantined** |
| S15 | `.designs/systems/npcs/reference/npc_behavior_v30.md` — per-NPC Truth rows (`:64,84,105,125,146,167,186,207,226,249,317`), `:548` (*"Truth reaches 0 → Conviction permanently altered … Primary becomes Authority (old framework's authority void) … NPC in crisis; new arc phase"*), `:1191-1205` the TS/Truth stat table | **quarantined** |
| S16 | `references/npc_registry.yaml` — `cultural_label:` values (`ecclesiastical` ×7, `einhir_traditional` ×4, `restoration_reformist` ×4, `altonian` / `altonian_imperial`, …); `:117` Haelgrund *"Investigate heresy / Enforce Church orthodoxy"*; `:401` `certainty: 3`; Truth values surviving only inside `migration_notes` strings (`:472,496,519,542,565`); `:934` *"Illegal Einhir education"*; `:941-949` the copyist (*"possession is a heresy charge"*). **No `church_standing` key anywhere in the file** (grep, this session) | live registry |
| S17 | `engine/season/rosters.yaml:378-387` — `church_standing` as one value of the `standing` claim predicate; `:1593-1618` — the old `sacred` alignment block, 12 verbs with a reason each | live table |
| S18 | `engine/season/verb_table.yaml` — `commit` `:117-132`, `destroy_record` `:184-194`, `kill / wound` `:287-300`, `restore` `:495-516`, `speak` `:531`, `tell` `:560`, `thread_read` `:751-763`, `tie / knot` `:779-789`, `utter` `:809-818` | live table |
| S19 | `references/descriptor_registry.yaml:170-172,293-296` — the `scale:` string convention (`"0-5"`, `"0-7"`, `"[-1,+1]"`, `"0-1 weight (vector)"`); no `bands:` key exists in the file (grep) | live registry |
| S20 | `engine/season/state/carriers.py:470` (`body` on `condition_scale`), `:480-489` (`scar` as a bare dict; *"the reader §54 item 21 names is the Conviction CRISIS, 'an L5 edge that rewrites an option set and never rolls an outcome'"*); `rosters.yaml:920` (`band_floors`) | game code |
| S21 | `architecture/holonic_ARCHITECTURE.md:1901` item 21 (verbatim: *"crisis is an L5 edge that rewrites an option set and never rolls an outcome"*); `engine/season/hole_register.yaml:952-963` H-128 | Layer 1 / register |
| S22 | `proposals/2026-09-20-pursuit-basis-worksheet.yaml:54` (`warden` restored, *"the only row touching the thread side"*), `:123-137` (the `faith` pair, Jordan verbatim), `:166-207` (scars RULED: counts, thresholds 1/2/3, `crisis_reader: ~` OPEN) | authoring surface, head per `CURRENT.md:25` |
| S23 | `proposals/2026-09-16-conviction-decision-layer/adjudication_register.yaml:104,194-195` — STR-6, *"piety: reserved"* | proposal |
| S24 | `references/names_index.yaml:64` (`thread.` = *"threadwork mechanic"*), `:347` (`world.church` canonical **"Church of Solmund"**, RULED 2026-09-13), `:356` (`world.restoration_movement`), `:358,366` (`Altonia`, `Altonian`) | live registry |
| S25 | `PROPOSAL.md` (the governing plan) — §2.1 items 5/6 (`:159-172`), §3.1 (`:362-368`, the threshold-1/3 distinction), §3.4 (`:542-555`), H13 (`:583-589`), §5 Q3/Q4/Q6 (`:661-664`), §7 (`:752-754`: the audit deliberately did not read S11) | plan |
| S26 | `candidate_pursuit_cells.md` §2.11 (the `faith` row), §3.4 (the `selfish` column), §3.6 (`tell` gets no cell), §5.2 (the H7 arms) | companion draft |

---

## §1 · C3a — the roster: keep / strike / add

### 1.1 The five candidates

| worksheet name (S2) | verdict | grade | reasoning, with citations |
|---|---|---|---|
| `solmund_orthodoxy` | **KEEP** | cited | This is the pole R2 absorbed (S1 `:167` *"Solmund-orthodoxy <-> Thread-truth"*; S9 pole 5). Its content is RULED at S4 D-10 and laid out at S3 §8.7 *"The Church worships Solmund"* and §8.8: essentialism, fixed determinism, an unchanging all-knowing determining God, a world exactly as it appears — *"an accurate rendering of Solmund misidentified as a rendering of the ground"*. S12 `:612` gives the first-person anchor, *"Solmund's word is the only truth — heresy is to be rooted out wherever it is found."* ⚠ **Two things the name must not be read as.** (i) It is a DOCTRINE held, not membership of the faction `Church of Solmund` (S24 `:347`): office is a `hold` Tenure and a person can be clergy at low intensity (S13 §18 Truth 3 *"Faith as habit without conviction"*). (ii) It is not the territory-scale PT (S1 `:168` *"SCOPED TO THE PER-CHARACTER AXIS. The territory-scale Piety (PT) is untouched"*). |
| `inner_tradition` | **KEEP, conditionally** — see the definitional flag | derived | The live text is S5 §5.7: the inner tradition *"preserves knowledge as practiced technique, ritual gesture, and apprenticeship rather than doctrine"*, and its outer reception is *"religious poetry"*. S3 §8.7's displacement paragraph is what makes it a separate affiliation rather than a wing of the first: *"the Church and the inner tradition … do not share a referent. The inner tradition's apophatic transmission (§5.7) concerns the ground; the Church's positive theology concerns a being."* S3 §8.9: *"The inner tradition may debate it; the outer tradition lacks the epistemic access to frame the question."* ⚠ **FLAG — where it sits is not settled by canon.** The worksheet's gloss *"within the Church"* (S2 `:46`) is the worksheet author's phrase; nothing in S3/S5 places the inner tradition inside the Church's institution. S13 §11.2 (quarantined) says practitioner witness accounts *"were categorised as heresy"*, and S13 §2.3 describes *"heterodox devotional writing by Church members who have experienced threadwork"* — so the corpus has BOTH a Church-internal heterodox reading and a separate-lineage reading. **Keep it only if it means the Church-adjacent apophatic lineage; otherwise it collapses into `thread_truth` below (§1.3).** |
| `threadwork` | **KEEP the concept; RENAME proposed → `thread_truth`** | cited (concept) / derived (rename) | The concept is Jordan's own: *"devoutly Solmund but also believes in Threadwork"* (S2 `:84`). But the ledger's name for this pole is **`Thread-truth`** (S1 `:167` R2, `:168` *"a person may hold Solmund-orthodoxy AND Thread-truth, both fully"*), and S9/S10 gloss pole 0 as *"Thread as metaphysical foundation"* / *"Thread substrate is the ground of being; Solmund is a human rendering that exceeds it."* `threadwork` is already the PRACTICE and the mechanic (S24 `:64`; `systems/threadwork/`; the verb `thread_read`, S18 `:751`). Under `CLAUDE.md` §4's idempotence rule one word carrying "the belief" and "the operation" across a session boundary is the failure it names — and R1 makes the affiliation a *belief held at an intensity*, which a non-practitioner can hold (Vaynard Truth 2, Vossen Truth 3, S15 `:1196,1205`) and a practitioner can lack. **Recommendation: name the affiliation `thread_truth` (the ledger's existing word, coined by nobody here) and leave `threadwork` to the operation.** Jordan's call; the ten pairs below are written under the worksheet's name so they map 1:1. |
| `einhir_revival` | **KEEP the slot; RENAME proposed → `einhir_restoration`; and note it is the H7 pair's second half** | derived | The religious content the corpus gives this side: S13 §16 lists *"Einhir (as theological rather than historical term)"* among **forbidden** vocabulary (*"heresy investigation risk"*) — i.e., the Church already treats Einhir-as-theology as a rival creed; S13 §4.4 gives the Restoration Movement a theology (*"the vessels shattered, the sparks scattered, repair is both possible and obligatory … the RM's theology"*, framed there as RM self-understanding, not canon mechanism); S13 §3.3 *"The Restoration Movement's counter-theology … Thread sensitivity as human birthright"*; S13 Levinas: *"you cannot explain away the dead"*; S14 `:34` names the PT pole **"Einhir Restoration"**; S8 GD-3 gives the RM an *"anti-Church identity"*. And Jordan's own pair uses it: *"someone who is pure Einhir and anti Solmund church whose faith work is about dismantling it"* (S22 `:127-129`). ⚠ **Name collision.** *"Einhir Revival"* is a **Varfell faction action** (S8 GD-1 *"Varfell Threadwork first-mover + Einhir Revival"*; `.designs/systems/factions/reference/parliamentary_transfer_v30.md:81` cites `einhir_revival_v30.md` for it — a file that **does not exist** anywhere in the tree, checked this session), and Lenneth is an *"Institutional Einhir revivalist"* whose programme is *"cultural revival. Thread work as eventual horizon"* (S7 `:139`) — cultural and political, not a creed. So the corpus has ONE Einhir-side religious content and THREE political carriers of it (RM, Varfell, Lenneth's Crown-revivalism). The affiliation is the content; the carriers are factions and pursuits. The PT pole's own name, `einhir_restoration`, avoids the faction-action collision. Jordan's call. |
| `altonian_theocracy` | **STRIKE as a religious affiliation** | derived (strong) | The only thing in the corpus called *"Altonian Theocracy"* is S14 §4.2, **a Church-of-Solmund victory path** (PP-414): an *"Altonian Ecclesiastical Accord"* clock ending in *"The Church declares Ecclesiastical Primacy — a transnational theocracy with Himmelenger as its capital. Valoria and the Altonian Church territories form a single ecclesiastical jurisdiction."* — SUPERSEDED-BY GD-1 (S8 `:28`). The Altonian side is the **same doctrine in another polity**: S7 `:64` *"Altonia's own population includes a significant Solmundan minority"*, `:118` *"its Altonian missionaries"*, `:121` *"Altonia's Church minority growing"*; S12 `:593` *"ecclesiastical alliances (Altonia)"*. The worksheet's gloss *"a rival ecclesiastical polity"* (S2 `:58`) rests on `canon/02_canon_constraints.md:71`, which is GD-1 listing the struck path. **What Altonia's majority religion is: the corpus is silent (null).** A row that is doctrinally identical to `solmund_orthodoxy` would make four of the ten `incompatible` cells copies of the other four (§2, pairs 4/7/9/10). If Jordan wants a distinct Altonian faith it has to be authored; nothing here can derive it. |

### 1.2 Candidates the corpus supports that the worksheet lacks — considered and NOT added

| candidate | why considered | why not added |
|---|---|---|
| Southernmost / Warden practice | S6 §14 *"communities that deliberately cultivate the capacity for holding what exceeds intelligibility"*; S3 §8.10 *"Wardens are persecuted on the same grounds as practitioners"*; Edeyja Truth 1 (S15 `:1204`) | Its BELIEF content is `thread_truth`; its practice is `warden`, already a **pursuit** (S22 `:54`). Adding it would put one thing in two owners (`CLAUDE.md` §0.05 cl.3). |
| Restoration Movement counter-theology | S13 §3.3, §4.4 | Folded into `einhir_restoration` (§1.1) — it is the same content carried by one faction. |
| the practitioner witness tradition / Seam Texts | S13 §11.2, §12 | A textual lineage of `inner_tradition`, not a creed of its own. |
| irreligion (S13 §18 Truth 1–2 *"Rejection or indifference to theological framing"*; Niflhel *"plain speech"*) | a real population | Under R1 a vector, "no affiliation" is the **zero vector**. No row. |
| a distinct Altonian faith | would replace the struck row | **null** — nothing in the tree names one (§1.1). |

### 1.3 The roster this file recommends (Jordan to confirm, strike, or rename)

```
affiliation_roster:              # candidate; names in [brackets] are the worksheet's, kept for the 1:1 map
  - solmund_orthodoxy            # KEEP                       S1, S3 §8.7-8.8, S4 D-10
  - inner_tradition              # KEEP IF Church-adjacent    S3 §8.7, S5 §5.7   (else merge into the next)
  - thread_truth   [threadwork]  # KEEP, rename proposed      S1 R2, S9 pole 0, S2 :84
  - einhir_restoration [einhir_revival]  # KEEP, rename proposed   S14 :34, S13 §16, S22 :127-129
  # altonian_theocracy           # STRIKE                     S14 §4.2 is a Church path; S7 :64,:121
```

**Count: 4 keep (one conditional), 1 strike, 0 added.** Whether `inner_tradition` and `thread_truth` are one affiliation or two is the one roster question the corpus genuinely cannot settle (§6.1).

---

## §2 · C3b — the ten `incompatible:` cells

`true` = holding BOTH at high intensity puts the person in religious confliction (S2 `:69`). Written under the worksheet's names so each cell maps to `:72-81`.

| # | pair (S2 line) | value | grade | citation |
|---|---|---|---|---|
| 1 | `solmund_orthodoxy + inner_tradition` (`:72`) | **true** | derived | S3 §8.7: the two *"do not share a referent"*; §8.8: the Church's theology is *"in this precise technical sense, an anti-threadwork formation"*; S13 §11.2 practitioner accounts *"categorised as heresy"*; S13 §16: naming the ground *"Ein Sof"* is **forbidden** vocabulary. ⚠ The counter-evidence is the SAME finding read from inside: S13 §2.3's *"heterodox devotional writing by Church members who have experienced threadwork … Doctrine true but insufficient. Paradoxically closest to heresy"* — people DO hold both, **at strain**, which is exactly what `true` encodes (R1: confliction is derived from co-holding, not a bar on it). |
| 2 | `solmund_orthodoxy + threadwork` (`:73`) | **true** | **cited — Jordan verbatim** | S2 `:83-85`: *"'devoutly Solmund but also believes in Threadwork and therefore experiences religious confliction' — so that pair is `true` unless you now say otherwise."* S25 `:661` carries the same default. Canon agrees in its own words: S6 §9.3 / S3 §8.8 *"The Church's theology is, in this precise technical sense, an anti-threadwork formation."* |
| 3 | `solmund_orthodoxy + einhir_revival` (`:74`) | **true** | derived (strong) | These are the two POLES of the territory track (S14 `:34` *"0 = Einhir Restoration pole. 5 = Solmund Orthodoxy pole"*) and of the absorbed person track (S9). S13 §16: *"Einhir (as theological rather than historical term)"* is heresy-investigation vocabulary. S12 `:608`: the Church reads the Calamity as *"caused by Einhir overreach"*. S7 `:98`: the settlement *"elevates the institution that suppresses Thread awareness (Church) and marginalises the population associated with Thread catastrophe (southern Einhir)"*. S8 GD-3: RM *"anti-Church identity"*. Jordan's H7 pair (S22 `:127-129`) is built on their opposition. Not his verbatim word on *confliction* for this pair — hence derived, not cited. |
| 4 | `solmund_orthodoxy + altonian_theocracy` (`:75`) | **null** | — | Candidate struck (§1.1). Under the only reading the corpus supports (the Church's Altonian branch, S14 §4.2 *"a single ecclesiastical jurisdiction"*), the cell would be **`false` by identity** — the same doctrine twice. |
| 5 | `inner_tradition + threadwork` (`:76`) | **false** | derived | S5 §5.7: the inner tradition IS the tradition of thread practice — *"practiced technique, ritual gesture, and apprenticeship"*; S6 §10.2 the same. Compatible; if anything one contains the other (§1.1's conditional). |
| 6 | `inner_tradition + einhir_revival` (`:77`) | **null** | — | **Unsupported either way.** Both hold the *"Thread as ground"* content, but the corpus places them differently (apophatic and Church-adjacent, S3 §8.7, vs political-ethical and Lurianic, S13 §4.4 and Levinas *"ethical, not theological"*), and the Einhir are themselves split by the northern betrayal (S3 §8.11). Nothing says the two are at strain. ⚠ **The one live text that could make this `true`** is S4 `:602-611`, the knife-edge: restoring *"a remembered state or an intended one is a shape the practitioner chose, and holding configurations there is manipulation — at provincial scale, sustained, it is the Calamity's mechanism exactly"*, whereas Mending's discipline is to *"let it go where it goes — which may be nowhere anyone remembers."* A restoration creed that wants the Einhir world back AS IT WAS is in doctrinal tension with a practitioner discipline that forbids wanting it. That is about operations, not affiliation, and it is Jordan's to promote if he means it. |
| 7 | `inner_tradition + altonian_theocracy` (`:78`) | **null** | — | Candidate struck; would copy pair 1 under the Church-branch reading. |
| 8 | `threadwork + einhir_revival` (`:79`) | **false** | derived | S8 GD-1 lists *"Varfell Threadwork first-mover + Einhir Revival"* as one faction's paired levers; S7 `:139` Lenneth: *"cultural revival. Thread work as eventual horizon"*; the two tracks put Thread-acceptance and Einhir-restoration on the SAME pole (S9 pole 0; S14 `:34` pole 0); S13 §3.3 RM: *"Thread sensitivity as human birthright."* Compatible. Same knife-edge caveat as pair 6. |
| 9 | `threadwork + altonian_theocracy` (`:80`) | **null** | — | Candidate struck; would copy pair 2 under the Church-branch reading. |
| 10 | `einhir_revival + altonian_theocracy` (`:81`) | **null** | — | Candidate struck; would copy pair 3 under the Church-branch reading. |

**Tally (10): cited 1 · derived 4 (three `true`, two `false` — pairs 1, 3 true; 5, 8 false) · null 5** — four because the candidate is struck (4, 7, 9, 10) and one genuinely unsupported (6). **If `altonian_theocracy` is KEPT as the Church's Altonian branch, the four struck nulls resolve by identity to `false / true / true / true` (4/7/9/10) — which is the argument for striking it: a row whose every cell is a copy of another row's.**

Under the recommended 4-roster the relation has six cells, of which five are filled (1 cited, 4 derived) and one is null (pair 6).

---

## §3 · C3c — `intensity.scale`, `player_sees`, `bands`

### 3.1 What the tree already fixes

- **The number was ruled hidden.** S9 (ED-IN-0075, Jordan's ruling, resolved): *"players see qualitative bands only (Orthodox..Accepted), never the number."* R2 ABSORBS that track rather than deleting it (S1 `:168`: *"ABSORBED, NOT RENAMED … kept in the row FOR LINEAGE"*). So the hiding ruling carries into `conviction` unless Jordan lifts it. **`player_sees: bands` — cited, by inheritance.**
- **The spine was 0–5.** S9: *"engine-internal 0-5 spine"*; S10 the frozen capture; S14 `:33` PT is also 0–5 per territory. **This is the one ruled magnitude on the record**, and it is the same scale at person and territory (NERS S, *"calculations consistent in methodology"* — `CLAUDE.md` §0.06).
- **The band LABELS do not transfer.** S10's six labels (Orthodox / Faithful / Questioning / Skeptic / Transitional / Accepted) name POSITIONS between two poles — *"Doctrine shows cracks"*, *"Solmund is a rendering, not the source"*. R2's whole point is that the poles are no longer ends of one axis, so a per-affiliation INTENSITY cannot reuse labels that encode which pole you are near. **`bands: null` for the names** — they exist, and they are the wrong kind of thing.
- **`church_standing`** is one value of the `standing` CLAIM predicate (S17 `:387`), read by nothing (S1 `:167` MEASURED), and appears in no NPC block (S16). What that IS evidence for: the design's own list of *"what is readable off someone"* (S17 `:381-386`, from #353 §14) includes religious standing as a thing OTHERS can assert about a person — a witnessed, contestable fact, not a hidden interior. So the two rulings sit together without conflict: **the intensity number is hidden; the affiliation is claimable** (a `standing` claim with predicate `church_standing`, already rostered).

### 3.2 Three scale conventions the tree offers (Jordan picks; this file recommends one)

| option | precedent | for | against |
|---|---|---|---|
| **(a) `0-5` integer** | S9 the absorbed Truth spine; S14 PT `0-5`; S19 `set.prosperity/defense/order` `"0-5"` | the only ruled number; one scale at person and territory; a band table of six already exists to be relabelled | integer steps are coarse for a "vector" (R1) |
| (b) `[0,1]` float | S19 `:293` conviction weights *"0-1 weight (vector)"*; `Person.pursuits` is a dict of such weights (`npc_registry` `weight: 0.60`); the companion's `faith` row (S26 §2.11) | matches the sibling vector it sits beside; `confliction(p)` as a derived query reads naturally as a product of two intensities | no band precedent; discards the ruled spine |
| (c) fixed-point on `condition_scale` with `band_floors` | S20: `body` is stored on `condition_scale` and read through `band_floors` (`rosters.yaml:920`); the season's only "number stored, band read" mechanism | reuses the engine's one existing band reader (§8: every rule once) | `band_floors` is keyed by site kind / body, not by a roster member; extending it is H10's job and a shape question |

**RECOMMENDATION FOR JORDAN (not a ruling): (a) `scale: '0-5'`, `player_sees: bands`, `bands:` six, names to be authored.** The reasoning is that (a) is the only option with a ruled number behind it; (b) and (c) each require a new magnitude or a new reader. **If Jordan prefers (b), nothing else in this file changes** — the `incompatible` relation is boolean and the C4 rule below is sign-only.

### 3.3 Band names — a derivation Jordan could approve instead of naming six words

The corpus holds one table that describes *intensity* of orthodox faith rather than *position*: S13 §18 (quarantined), keyed by the old Truth value — 1–2 *"Rejection or indifference to theological framing"*, 3 *"Faith as habit without conviction"*, 4 *"Faith as cultural architecture — lived, not examined"*, 5 *"Intellectual and sensory commitment. The world is evidence"*, 6+ *"Encounter. Doctrine true but insufficient."* Those are five intensity glosses over 0–5 and one (6+) beyond it — written for `solmund_orthodoxy` only, so they cannot be transcribed as the roster's bands, but the LADDER they describe (indifference → habit → lived → committed → encounter) is affiliation-neutral. **Offered as a source for six names; the names themselves are null here.**

---

## §4 · C4 — verb × affiliation engagement

### 4.1 What exists, and why most cells cannot be derived

**No table exists** (S25 `:553-554`; `alignment` is verb × moral-axis only). The corpus has four kinds of evidence, none of which is a verb × affiliation cell:

1. **The old `sacred` column** (S17 `:1593-1618`): twelve verbs with a reason each — `utter +0.8`, `tie / knot +0.7`, `commit +0.7`, `confer +0.5`, `oblige +0.4`, `establish +0.3`, `kill / wound +0.3`, `evade / defy −0.3`, `destroy_record −0.3`, `forge −0.5`, `surveil −0.3`, `repudiate −0.6`. Its own header says what it measures: *"which verbs carry oath-, rite- or vow-shaped weight."* That is verb × THE NUMINOUS — a vow is a vow under every creed on the roster. It does not distinguish orthodoxy from thread-truth and cannot be a per-affiliation table. ⚠ Its `kill / wound` reason was self-flagged as *"my own historical inference … not sourced from any doc in this repo"* and rewritten (S17 `:1605-1612`); the companion (S26 §3.7) re-homed three of these cells to `deontological↔instrumental`.
2. **The Thread-event × Conviction matrix** (S11 §3, quarantined): rows are thread OPERATIONS (Dissolution, POP, Lock, Mending, Weaving, Rendering Crisis), not verbs; *"Faith NPCs Scar from ANY Thread operation except Mending"* (`:92`); *"Mending never produces Scars"* (`:91`). Of those operations, `verb_table.yaml` holds only `thread_read` (S18 `:751`, not in `resolvable_verbs()`) and, at most, `restore` as Mending's nearest (S18 `:495`, also unresolvable). ⚠ **CONFLICT with live canon on Mending**: S3 §8.10 says the Church condemns Mending too — *"Wardens are persecuted on the same grounds as practitioners of manipulative-scale operations, though Mending is restorative and non-corrosive."* Primary = S3 (live canon over quarantined design): **witnessed Mending violates `solmund_orthodoxy`**; S11's exemption reads as "Mending never scars the *practitioner's own* convictions", which is a different claim and not contradicted.
3. **The Church's mission and modifiers** (S12): `contradicted_categories: da.covert_betrayal, da.antinomian_action`; *"Reveals Thread truth: +2 Ob (institutional perceptual prophylaxis — Church-only modifier)"*; *"Doctrine-aligned (heresy suppression / Piety expansion / moral law enforcement): −1 Ob."* These are domain-action CATEGORIES on the faction layer, not person verbs.
4. **Vocabulary as the violation surface** (S13 §16): the forbidden words are *"Ein Sof … Einhir (as theological rather than historical term) … Ungrund"*. The act that violates orthodoxy is SAYING them — `utter`, `speak`, `tell`, `create_record` — and it violates by CONTENT (the Proposition uttered, the record's text), not by verb. S16's copyist row says the same for records: *"Hand-copied manuscripts … possession is a heresy charge."* This is the companion's `tell` finding (S26 §3.6) at the religious layer: **a verb × anything cell cannot carry it.**

**So: the table is not derivable as cells.** What IS derivable is the shape below, which Jordan can approve once.

### 4.2 The proposed derivation rule (R-C4), three clauses

> **R-C4.1 — the shared column.** The vow-shaped verbs engage EVERY affiliation identically. Carry the old `sacred` column (S17 `:1593-1618`, minus `kill / wound` and `surveil`, whose reasons are a self-flagged inference and a cost respectively) as ONE column, `sacred`, multiplied at use by the person's TOTAL conviction intensity — not a per-affiliation table. Ten cells, each with S17's reason. (`utter`, `tie / knot`, `commit`, `confer`, `oblige`, `establish` positive; `evade / defy`, `destroy_record`, `forge`, `repudiate` negative.)
>
> **R-C4.2 — the per-affiliation exceptions.** A verb violates a NAMED affiliation only where canon says the affiliation condemns the act's KIND. The corpus supports exactly this set: thread operations (`thread_read`; `restore` when it is Mending) violate `solmund_orthodoxy` when witnessed (S3 §8.8 *"anti-threadwork formation"*, §8.10 *"all threadwork is heretical"*; S11 `:92`); and `destroy_record` of an Einhir record violates `einhir_restoration` (S7 `:66`: Altonia *"systematically destroys Valnese records, monuments, and temples — targeting Einhir cultural heritage"*; S13 Levinas *"you cannot explain away the dead"*) — but that last one is content-keyed (WHICH record), so see R-C4.3.
>
> **R-C4.3 — content-keyed violations are not cells.** `utter` / `speak` / `tell` / `create_record` / `destroy_record` violate an affiliation according to WHAT is uttered or recorded (S13 §16's forbidden vocabulary; S16 `:949`). This needs a tag on the Proposition or Record (the object), read at RESOLVE by the same scar writer H3/H11 build — never a verb cell. **Recorded as a hole for H11, not filled here.**

Under R-C4 the "table" is: one shared 10-cell column (carried, cited) + two named exceptions (derived) + one declared hole. **That is the whole of what the corpus supports.**

### 4.3 The sketch, so the shape is visible (`+` engages · `−` violates · `·` no cell · `?` null)

Columns are the recommended roster. Every non-`·` cell names its source; a `·` under a named affiliation means "no source", not "compatible".

| verb (S18 line) | shared `sacred` (R-C4.1, from S17) | `solmund_orthodoxy` | `inner_tradition` | `thread_truth` | `einhir_restoration` |
|---|---|---|---|---|---|
| `thread_read` (`:751`) | · | **−** witnessed — S3 §8.10; S11 `:92` | + practice — S5 §5.7 (derived, sign only) | + practice — S9 pole 0 (derived, sign only) | · |
| `restore` (`:495`) as Mending | · | **−** witnessed — S3 §8.10 **CONFLICT** with S11 `:91`; primary S3 | · | · | + *"repair is both possible and obligatory"* — S13 §4.4 (derived, sign only; RM self-understanding) |
| `utter` (`:809`) | +0.8 S17 | R-C4.3 (content) | · | · | · |
| `speak` (`:531`) / `tell` (`:560`) | · | R-C4.3 (content) — S13 §16 | · | · | R-C4.3 (content) |
| `create_record` / `destroy_record` (`:184`) | −0.3 (destroy) S17 | R-C4.3 (content) — S16 `:949` | · | · | R-C4.3 (content) — S7 `:66` |
| `tie / knot` (`:779`) · `commit` (`:117`) · `confer` · `oblige` · `establish` | +0.7 · +0.7 · +0.5 · +0.4 · +0.3 S17 | · | · | · | · |
| `evade / defy` · `forge` · `repudiate` | −0.3 · −0.5 · −0.6 S17 | · | · | · | · |
| `kill` / `wound` / `fight` / `challenge` / `accept` | **null** — S17's `kill / wound +0.3` reason is a self-flagged inference (`:1605-1612`); nothing in canon puts a body-contest under any creed | ? | ? | ? | ? |
| `surveil` | **null** — S17 `:1616` *"worldly craft"* is a cost, not a creed (the companion's own finding for D/I, S26 §3.7) | · | · | · | · |
| the other ~22 verbs | · | · | · | · | · |

**How C4 came out: as a derivation rule (R-C4) with one carried 10-cell column and two derived exception cells — not as a filled 42 × 4 table.** Filling the rest would be guessing, which the brief forbids.

---

## §5 · G-Q6 — crisis threshold 3: what the design says, and a RECOMMENDATION FOR JORDAN

### 5.1 What `conviction_track_v1.md` §2 actually says (S11, quarantined — reported, not adopted)

Row 3+ of the per-Conviction scar table (`:51`), verbatim:

> **Conviction crisis on X.** NPC acts unpredictably for 1 season when X is engaged (engine rolls on crisis table below per major X-engaging decision). Other Convictions remain stable unless they also accrue 3+ Scars. | Resonant Style for X is fully exposed … | **Terminal arc phase for the X-axis: stabilise into a new X-configuration, fold X into another primary, or be destroyed by the X-incoherence.**

The crisis table (`:53-60`) is a **d6 per major X-engaging decision**: 1–2 act on the original X (*"habitual regression"*); 3–4 on the *"highest-weighted other primary Conviction (lateral pivot)"*; 5 the Self-Other override; 6 *"whichever Conviction most aligns with the last PC interaction"*. Multi-crisis (`:62`): *"the engine selects the Conviction with the most recent Scar event … ties resolve to highest-weighted primary at character creation."*

**What it specifies and what it leaves open:**

- **It specifies the 1-season crisis behaviour** (a roll per decision) and it specifies **nothing that selects among the three terminal outcomes.** "Stabilise / fold / destroyed" are named as the three things the terminal phase can be; no rule, roll, threshold or condition chooses one. **It is an open triad, exactly as `PROPOSAL.md` §5 Q6 states it.**
- ⚠ **The part it DOES specify is the part that may not be built.** Item 21 (S21 `:1901`) folds the mechanic in AMENDED: *"crisis is an L5 edge that rewrites an option set and never rolls an outcome."* The d6 rolls an outcome. So under the ratified amendment the design's own crisis table is struck, and the terminal triad — the part the design left open — is what remains to be specified. H-128 (S21 `:952-963`) says the same from the other side: *"the number that matters is the one at which a crisis fires, which cannot be chosen before the crisis exists."*
- **One precedent for a FIXED terminal outcome exists in the design corpus.** S15 `:548`: *"Truth reaches 0 → Conviction permanently altered → Primary becomes Authority (old framework's authority void) → NPC in crisis; new arc phase."* That is the **fold** branch, with a named target, applied to the very axis R2 absorbed. It is quarantined, and `Authority` is no longer a pursuit (S22 `:37`), but it records that when the design previously reached this question it answered "fold into a specific successor", not "roll".
- The threshold-2 row (`:50`) already says *"weight may shift downward (engine judgment based on Scar content); other primaries gain proportionally"* — i.e. the mechanism that moves weight between elements exists one rung below the crisis.

### 5.2 RECOMMENDATION FOR JORDAN (not a ruling): the engine chooses per case, by a rule over state the crisis already reads — and for the conviction track the `incompatible` relation is that rule

**Recommend "the engine's choice per case", with a deterministic selector and no roll**, on these grounds:

1. **A fixed outcome cannot be right for both tracks at once.** The triad's three branches are three different states the person can be left in, and which is available depends on what else they hold. A person with ONE pursuit cannot fold (no target) and, if destroyed, has a zero vector — `choose` then scores a constant, which is H-62's inert case (S20 `:480-489`, `PROPOSAL.md` §2.2). So "always destroyed" is unreachable safely and "always fold" is undefined for that person.
2. **The selector is already in the state, and for convictions it is R1's own relation.** Under R1, confliction is derived from co-holding two `incompatible` affiliations. A crisis on affiliation X is the moment that confliction resolves. Reading S11's three branches against that state gives one branch per case, with no free number:
   - **fold** when X is in confliction with a co-held affiliation Y (`incompatible[X,Y]`) — X's intensity transfers to Y. This is Jordan's own worked case (S2 `:84`) reaching its end: the devout Solmund believer who believes in Threadwork is, at crisis on orthodoxy, either a practitioner or a penitent, and the fold's direction is which affiliation was scarred. It is also S15 `:548`'s precedent shape.
   - **restabilise** when X is co-held with nothing incompatible and something else is above threshold — X's weight shifts down and the others gain, i.e. **the threshold-2 mechanism continuing** (S11 `:50`); no new mechanism.
   - **destroyed** when nothing else is held above threshold — X drops from the vector. For the conviction track this is the zero vector (irreligion, §1.2), which is a real state; for the pursuit track it is the inert case in point 1 and should be reachable **only** when no fold target exists, which the rule above guarantees by ordering.
3. **It is an L5 edge, not a roll.** Each branch rewrites the person's vector (which rewrites the option set the deontological gate and `score` read) and rolls nothing — item 21's form (S21). The d6 table is not carried.
4. **No magnitude is introduced.** The thresholds are RULED (S22 `:191`: `{destabilise: 1, weight_shift: 2, crisis: 3}`); the selector reads `incompatible` (boolean, §2) and the person's own vector. Where H9's threshold-2 shift needs a swept `Fixtures` arm (H-128's shape), threshold 3 inherits that arm and adds none.

**If Jordan wants ONE fixed outcome instead**, the precedent in his own corpus is **fold** (S15 `:548`), and the fold target the tree can name without inventing is *"the highest-weighted other element"* (S11 `:58`, the d6's 3–4 row, made deterministic).

**What would show this recommendation wrong.** A crisis case Jordan wants where a person in confliction is *destroyed* rather than folded (a martyr, not a convert) — the rule above cannot produce it. If that case is wanted, the selector needs one more input (the companion's `rigid↔flexible` axis is the obvious candidate: a rigid person breaks, a flexible one folds — S26 §2 shows that axis has almost no cells today, so this would be the first thing to give it work). **Recorded as the alternative, not chosen.**

### 5.3 Threshold 1, for completeness (H13's other half — not in this file's scope)

S11 `:49`: *"Conviction X destabilises … Decision Forks increase when X is salient."* "Decision Fork" is the old NPC-behaviour system's term (S15) with no season-loop analogue, which is why `PROPOSAL.md` §3.1 could find no precedent. Noted only; nothing proposed.

---

## §6 · Gap list, conflict list, and what this file does not do

### 6.1 Open on Jordan (survive the five-step gate — they are content, not process)

1. **Are `inner_tradition` and `thread_truth` one affiliation or two?** Both readings are in the corpus (§1.1). If one, the roster is 3 and pairs 1/5 collapse into 2.
2. **The two renames** (`threadwork`→`thread_truth`, `einhir_revival`→`einhir_restoration`) — proposed for idempotence (`CLAUDE.md` §4), not required by any ruling.
3. **Pair 6** (`inner_tradition + einhir_revival`) — null; the knife-edge (S4 `:602-611`) is the only text that could decide it.
4. **Band names** (§3.3) — null; a ladder is offered, the six words are not.
5. **Scale** — (a) recommended over (b)/(c) (§3.2).
6. **R-C4** — approve the rule, or author the 42 × 4 table by hand.
7. **G-Q6** — the selector in §5.2, or a fixed outcome (fold).

### 6.2 Conflicts (both shown in place)

| where | source A | source B | primary | why |
|---|---|---|---|---|
| Mending vs orthodoxy (§4.1 pt 2, §4.3) | S3 §8.10 (live): Wardens persecuted, *"all threadwork is heretical"* | S11 `:91-92` (quarantined): *"Mending never produces Scars"* | S3 | live canon over quarantined design; and the two claims may be about different subjects (the witness's creed vs the practitioner's own) |
| `inner_tradition`'s location (§1.1) | S2 `:46` *"within the Church"* (worksheet author) | S3 §8.7 *"do not share a referent"*; S13 §11.2 *"categorised as heresy"* | neither — flagged | the worksheet's gloss is not canon text; canon does not place the tradition institutionally |
| `kill / wound` under the sacred (§4.3) | S17 `:1612` +0.3 | S17's own note `:1605-1611` (self-flagged inference) | **null** | the reason disqualifies the cell |

### 6.3 What this file does not do

- It does not touch `proposals/2026-09-18-conviction-basis-worksheet.yaml`, `proposals/2026-09-20-pursuit-basis-worksheet.yaml`, any `references/*.yaml`, or `engine/season/rosters.yaml`.
- It does not allocate an ED id or bump `next_free`.
- It does not build H10's plumbing shape (roster block, loader, `confliction(p)`, `write_matrix` row) — that is ENGINEERING per `PROPOSAL.md` §3.4 and is not content.
- It does not claim the four `derived` pair values are right; it claims each choice is visible with its source, so Jordan can reject on the source.
- It does not cite any quarantined document as the reason a behaviour would be correct; every quarantined citation is labelled and used as a source for Jordan's review only.
