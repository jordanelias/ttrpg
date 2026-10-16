# Attributes from scratch: a blind, bottom-up derivation from the verbs

## Status: PROPOSED

**Date:** 2026-10-16. **Lane:** cross-cutting (character). **Allocates no ids.**
**What this is:** a design exercise and reference (CLAUDE.md §0.05). Nothing reads it, it decides
nothing, and no behaviour may be cited from it. **What it answers.** Jordan asked (2026-10-16):
*"And against the verbs we have in code as well as verbs we have to design, the unique etymology of
these verbs, and the domains of these verbs..? How a subsystem COULD work? What would we see the
attributes are WITHOUT reference to the base attributes proposed? If we were to do from scratch?"*
For this exercise he set aside every prior ruling (*"ignore all prior rulings"*; *"there are no derived
scores when we don't even know our primaries"*). So the count is open, and nothing counts as "derived"
until primaries are chosen.

**Parts, in reading order:**

| part | sections |
|---|---|
| this file | reading record · §1 method and vocabulary · §2 the verb inventory |
| `_part2.md` | §3 how each subsystem could work · §4 per-verb demand statements |
| `_part3.md` | §5 flatten and collate |
| `_part4.md` | §6 the from-scratch attributes |
| `_part5.md` | Phase B: §7 mapping · §8 agreement and disagreement · §9 precedent · §10 limits |

Sections 1–6 (Phase A) were written and saved to disk before any file on the brief's forbidden list
was opened. Sections 7–10 (Phase B) were written after that.

---

## Reading record for Phase A (exact, as read)

These are the files read before §1–§6 were finished, and how each was read.

1. `/home/user/ttrpg/CLAUDE.md`: loaded as the session's instructions.
2. `engine/season/verb_table.yaml`: read **through a filter script**. I printed the list of field
   names, then for each of the 45 rows only `verb`, `stratum`, `beneficiary`, `counterparty`, `scale`,
   `grade`, `writes` and `emits`. I did **not** read `eligibility`, `requires`, `requires_typed`, or any
   `*_note` field.
3. `workplans/valoria_master_workplan_v9*.md`: a grep for backticked words on lines that mention
   "verb", and these lines (some cut to 600 characters): `v9.md:8`, `:339`; `_part2.md:254`, `:278`;
   `_part3.md:98`, `:116`; `_part5.md:43–44`, `:55`, `:57`, `:61–100`, `:247`, `:284`, `:297`, `:299`.
4. `research/by_lane/{FA,FI,MB,NPC,PC,SC,SE,WR,IN}_*.md`: the heading list of each file. I printed
   **§10.2 VERBS** with lines cut to 700 characters, and **§8.2 MISSING** with lines cut to 260
   characters.

**None of the files on the forbidden list was opened in Phase A.** That list is:
`references/descriptor_registry.yaml`; any derived-stats, augmented, HIST, fieldwork, threadwork,
social-contest or combat design's attribute tables; `proposals/2026-08-15-*`;
`proposals/2026-09-30-character-and-play-surface/*`; the character-template and attribute-derivation
proposals; the `Combatant`/`Officer` field definitions.

**Exposure, disclosed because it could have primed the derivation:**

- **The brief itself** named the eleven recommended primaries by abbreviation and the count of 46
  aptitudes. I did not use them in §1–§6, but I had seen them.
- **I read past the verb names in §8.2.** The brief allowed only the verb names from the lane files'
  §8/§10. Rows M-PC-1, M-NPC-1, M-NPC-2, M-NPC-13, M-IN-1, M-IN-7 and M-SC-8 went further: they mention
  "a person's attributes and kit", "skill, attribute, Thread Sensitivity", "a reader's competence",
  "commanders and troop quality … experience, equipment", and "`Combatant`".
- **The IN-12 row** names a `capability` key, `copying`.

Two of my results lie close to these phrases. Reading people and reasoning appear in AX-7's "reader's
competence", and skills, kit and command appear in "equipment, experience and commander". I flag both
as **possibly primed**. The derivation reaches both from the verbs on its own (§4 lists the demands), but
I cannot prove I was not nudged.

---

## 1. Method and neutral vocabulary

### 1.1 The question, restated

Suppose you were building this game from nothing. Start from the acts people perform in it: the verbs
in the code, the verbs the plan schedules, the verbs the lane studies ask for, and the verbs a complete
game of this kind would need. Ask what each act requires of the person who does it. Collect those
requirements and ask which few properties of a person explain the most of them. Those properties are
the candidate attributes.

### 1.2 Vocabulary (plain words, defined once)

| term | meaning here |
|---|---|
| **demand** | what an act asks of the person who performs it: a capacity, a holding, a right or a disposition, without which he cannot do it, or does it worse, or at greater cost |
| **patient-side demand** | an extension the brief did not ask for. It is what a contested act asks of the person it is done **to**, if he is to resist it (tag **P**). It is added because a list built only from verbs counts nothing that happens *to* a person. Being wounded, deceived or watched is no one's verb. |
| **domain** | the semantic field of a verb: motion, force, speech, perception, making, exchange, rule, ritual, care, concealment, binding, judgement, knowing, record, travel |
| **difference** | what makes one person likelier to succeed at an act, cheaper at it, more able to attempt it, or better in its result |
| **draw** | which of four quantities a demand moves: **odds** (likelier to succeed), **cost** (fatigue, time, harm or stores spent), **access** (may he attempt it at all, or will he choose to), **effect** (how much the act does when it succeeds) |
| **source tag** | where a demand statement came from: **R** = the verb's root sense (etymology); **S** = how the subsystem works (§3); **O** = the ordinary present-day sense of the word; **P** = patient-side (above) |
| **atomic demand** | one demand phrase, stripped of its verb-specific gloss: "sustained exertion (bearing a matter across distance)" flattens to "sustained exertion" |
| **cluster** | a group of atomic demands that would measure the same property of a person |
| **root-sense family** | verbs whose original sense is the same act, cognate or not: *pardon* and *forgive* (both "give wholly"), *oblige* and *rally* (both from L. *ligare* "bind") |
| **attribute** | a property of a person, carried on the sheet, that explains many demands across many subsystems. Whether a given cluster earns this status is §6's question. |
| **skill** | a learned specialty that sits under one or more attributes |
| **holding** | a seat, a rank, a claim, stores, kit, a following. It belongs to the person's position, not to his body or mind, and passes to an heir or a successor. |
| **value** | what a person is willing or wants to do: mercy, ruthlessness, conviction. It is a disposition, not a capacity. |
| **computed quantity** | a figure read at the moment from attributes, skills, holdings and world state, and stored nowhere |
| **track** | a quantity that goes up and down in play: harm, fatigue, stores, self-integrity under the threads |

Everything §6 proposes takes a plain descriptive name: *bodily force*, *watchfulness*, *constancy*. I
avoided the repository's attribute names on purpose.

### 1.3 The pipeline

1. **Inventory (§2).** Every verb row in `engine/season/verb_table.yaml` is listed, then every planned
   verb in the v9 plan, including those the plan has refused or cut. After those come the verbs the
   lane studies call for, then the verbs I judge a fully designed game would need in each of ten
   subsystems. Each row records its origin, subsystem, domain, etymology (from memory, with a
   confidence), and what the root sense implies the performer must have.
2. **Subsystem accounts (§3).** Each of the ten subsystems gets a first-principles sketch: what its
   people want, the loop, where success, cost and risk come from, who is better at it and why, and
   what a player should be able to read off a character sheet.
3. **Demand statements (§4).** Each verb gets one to four demands, tagged R/S/O and marked with a
   draw. Contested verbs also get patient-side demands.
4. **Flatten and collate (§5).** A script in the session scratch directory computes the counts (it is
   not part of the repository): `scratch_attr/verbs_data.py` holds the data and `gen_tables.py` and
   `cooc.py` produce the counts. Nothing was tallied by hand. The atomic demands are clustered, and each
   cluster gets its verbs, subsystems, draws, source tags and shared root-sense families. Two checks
   follow: an origin breakdown (would the result stand on the code's verbs alone?) and a co-occurrence
   table (do the verbs tell the clusters apart?).
5. **Principles, then sets (§6).** The selection principles come first. Then a recommended set, one
   smaller and one larger set, a cut test for each attribute, and the demands each set leaves to
   skills, values, holdings and computed quantities.

### 1.4 What counts as evidence here, and what does not

- **Counts by breadth.** How many verbs and subsystems draw on a cluster. This is evidence of breadth,
  not of importance. A verb list is a sample the author chose, and §5.4 shows how much the result
  leans on the 86 verbs I added.
- **Root-sense agreement.** Sometimes a language has a whole verb family whose original sense *is* the
  property: *hide* (conceal, ambush, hoard, smuggle, shadow, eavesdrop) or *watch* (surveil, guard,
  ward, steward). That is evidence that people have long named the property apart from its neighbours.
  Sometimes a family scatters across several clusters instead (*give*, *loosen*, *carry*). That is
  evidence the act's demand is not a personal capacity at all.
- **Draw type.** A cluster that moves one kind of quantity cleanly is easier to read than one that
  moves all four.
- **Cut test.** Remove the proposed attribute and name what dies. If something else absorbs it without
  loss, the case for the attribute was false.
- **Not evidence.** Design documents (§0.05). In Phase A, also no published attribute set except what I
  carry as general knowledge of games. That knowledge is cited as such where it shaped a judgement.

---

## 2. Verb inventory

### 2.1 How to read the table

- **where:** `code` = a row in `engine/season/verb_table.yaml` (a row may name two words, such as
  `evade / defy`; it counts as one row). `plan` = a verb the v9 plan schedules. `plan (refused/cut)` = a
  verb the plan names in order to refuse, cut or rule it out. These stay in the inventory: the refusals
  concern the season loop's architecture, and in a fully designed game the act would still happen
  (`kill` and `wound` are what `fight` produces). `lane rec` = a verb the lane studies' §8.2/§10.2 call
  for. `designed here` = my addition. Each addition has a "why added" line, and **is a design proposal,
  not a source.**
- **Additions were chosen subsystem by subsystem.** The question was: what acts would a historically
  grounded, game-precedented version of this subsystem need that no code, plan or lane verb already
  covers? **Exact synonyms of existing verbs were not added:** *trade* (= exchange), *appoint* (=
  confer), *decree* (= issue or proclaim), *spy* (= surveil), *teach* (= train), *judge* (= determine),
  *alms* (= relieve), *edict* (= issue, as the FA lane recommends), *delegate* (= establish + confer, as
  the FA, NPC and SE lanes describe it).
- **Etymologies are from memory.** I checked none of them against a dictionary in this session.
  Confidence is my own. **low** means the origin is disputed or I am unsure of it.
- **Thread verbs** (`weave`, `pull`, `lock`, `loosen`, `sever`, `mend`, `leap`, `ward`, `anchor`,
  `trace`): I know threadwork here only by these names and by "Coherence" as a cost word in the lane
  rows. Every claim about how they work is **[INFERRED]**.

### 2.2 Counts

| origin | verbs |
|---|---|
| code | 45 |
| plan | 18 |
| plan (refused/cut) | 7 |
| lane rec | 23 |
| designed here | 86 |
| **total** | **179** |

| subsystem | verbs touching it (a verb may serve several) | of which designed here |
|---|---|---|
| PC | 31 | 21 |
| MB | 43 | 27 |
| SC | 40 | 18 |
| FI | 32 | 17 |
| TW | 14 | 5 |
| GV | 51 | 16 |
| FA | 31 | 15 |
| EC | 33 | 17 |
| WT | 18 | 15 |
| NP | 36 | 19 |

### 2.3 The inventory

| id | verb | where | subsystem(s) | domain | etymology (from memory) | conf. | what the root sense implies the performer must have | why added |
|---|---|---|---|---|---|---|---|---|
| V001 | **carry** | code | SC GV | conveyance, speech | AN/ONF carier < L. carrus 'wagon' (Gaulish loan) | high | bear a load from one place to where it is received: reach to the venue, stamina to convey | — |
| V002 | **commit** | code | NP FA | binding | L. committere 'join, entrust' (com- + mittere 'send') | high | put oneself into another's keeping and stay put: steadfastness | — |
| V003 | **comply** | code | GV | rule, obedience | It. complire / Sp. cumplir < L. complere 'fill up, fulfil' (English form shaped by 'ply') | medium | fill what is demanded: the means and capacity to fulfil | — |
| V004 | **confer** | code | GV | rule, gift | L. conferre 'bring together, bestow' (con- + ferre 'bear') | high | bear something to another: must hold something to bestow | — |
| V005 | **convene** | code | GV SC | assembly | L. convenire 'come together' | high | make others come together: a summons others answer | — |
| V006 | **create_record** | code | EC FI GV | record, making | L. creare 'bring forth' + recordari 'call to mind' (re- + cor 'heart') | high | bring a remembrance forth in fixed form: hold it in mind, then set it down | — |
| V007 | **destroy_record** | code | FI | concealment | L. destruere 'un-build' (de- + struere 'pile up') | high | unmake what was built: hands on the built thing | — |
| V008 | **determine** | code | GV SC | judgement, rule | L. determinare 'set bounds' (de- + terminus 'boundary') | high | fix a limit others respect: authority and judgement | — |
| V009 | **dispatch** | code | FA MB GV | command | It. dispacciare / Sp. despachar 'expedite', prob. dis- + a Romance 'hinder' (Prov. empachar < L. impedicare 'fetter') | medium | clear the hindrances and send off quickly: organization, speed of order | — |
| V010 | **establish** | code | GV | rule, founding | OF establir < L. stabilire 'make firm' (stare 'stand') | high | make a thing stand by itself: authority, and means to keep it standing | — |
| V011 | **evade / defy** | code | GV | resistance | evade: L. evadere 'go out, escape' (vadere 'go'); defy: OF desfier 'renounce faith' (des- + fier < L. fidare 'trust') | high | evade: slip out (cunning, mobility); defy: withdraw faith openly (nerve to bear the consequence) | — |
| V012 | **exchange** | code | EC SC | exchange | OF eschangier < VL *excambiare (ex- + cambiare 'barter', prob. Celtic) | high | barter: have something to offer and judge what it is worth | — |
| V013 | **forge** | code | FI EC | making, deceit | OF forgier < L. fabricare 'fashion' (faber 'artisan') | high | a smith's making; the false-document sense is a later extension: a maker's hand | — |
| V014 | **found** | code | GV EC | founding | L. fundare 'lay the bottom' (fundus) | high | lay a foundation: means and foresight | — |
| V015 | **build** | code | EC | making | OE byldan 'construct a dwelling' (bold 'house') | high | make a dwelling: labour and craft | — |
| V016 | **give** | code | NP EC | gift | OE giefan, PGmc *geban- | high | hand over: must hold something | — |
| V017 | **issue** | code | GV | rule, record | OF issue 'exit' < L. exire 'go out' | high | send out from oneself: a source whose word goes out and is obeyed | — |
| V018 | **fight** | code | PC | force | OE feohtan, PGmc *fehtan-, prob. 'pluck, tug' (cf. L. pectere 'comb') | medium | close, tugging struggle: bodily force and handling | — |
| V019 | **challenge** | code | PC SC | speech, contest | OF chalenge 'accusation' < L. calumnia 'trickery, false accusation' | high | lay a claim against another in public and stand by it: nerve and standing | — |
| V020 | **accept** | code | PC | contest, binding | L. acceptare, frequentative of accipere 'take to oneself' (ad- + capere) | high | take on what is offered: the nerve to take the risk | — |
| V021 | **requisition** | code | GV EC | rule, taking | L. requisitio < requirere 'seek again, demand' (re- + quaerere 'seek') | high | demand as of right: authority, and knowing what is there | — |
| V022 | **march** | code | MB | motion, war | F. marcher 'tread, trample' (prob. Frankish *markōn; or L. marcus 'hammer') | medium | tread steadily mile after mile; in war, keep order on the road | — |
| V023 | **migrate** | code | WT NP | travel | L. migrare 'move one's abode' | high | uproot and survive the road | — |
| V024 | **move** | code | WT | motion | AN mover < L. movere 'set in motion' | high | set oneself in motion | — |
| V025 | **oblige** | code | SC GV | binding | L. obligare 'bind to' (ob- + ligare 'bind') | high | bind another: leverage, standing, or a debt owed | — |
| V026 | **open_case** | code | SC FI GV | judgement, inquiry | open: OE open; case: L. casus 'a fall, an event' (cadere 'fall') | high | notice that something befell and take it up | — |
| V027 | **petition** | code | SC GV | speech, seeking | L. petitio < petere 'seek, make for, attack' | high | seek from another: knowing whom to ask and how | — |
| V028 | **construe** | code | SC | interpretation | L. construere 'pile together, build' | high | assemble meaning from parts; here, bend terms to one's reading | — |
| V029 | **release** | code | GV NP | binding | OF relaissier < L. relaxare 'loosen again' | high | loose what one holds: be the holder, and be willing to let go | — |
| V030 | **restore** | code | EC | making, care | L. restaurare 'rebuild, renew' | high | rebuild: know the original | — |
| V031 | **revoke** | code | GV | rule | L. revocare 'call back' | high | call back: only the voice that sent it out can | — |
| V032 | **speak** | code | SC | speech | OE sprecan / specan | high | have voice and words | — |
| V033 | **succeed** | code | GV | rule, kinship | L. succedere 'come after, go under' (sub- + cedere 'go') | high | come next: a place in the line | — |
| V034 | **survey** | code | FI GV EC | perception | AN surveier < ML supervidere 'look over' (super- + videre) | high | look over a whole from above: vantage, breadth of attention, a count | — |
| V035 | **tell** | code | SC NP | speech, account | OE tellan 'count, reckon, relate' (cf. tale, tally) | high | count out an account in order: memory and ordering | — |
| V036 | **examine** | code | FI | perception, judgement | L. examinare 'weigh' < examen 'tongue of a balance' (ex- + agere) | high | weigh accurately: fine discrimination | — |
| V037 | **interview** | code | FI SC | perception, speech | MF entrevue 'mutual sight' (entre + voir < L. videre) | high | see and be seen face to face: read while being read | — |
| V038 | **research** | code | FI | knowing | MF recercher 'seek closely' (re- + cercher < L. circare 'go round') | high | go round a matter again and again: patience and method | — |
| V039 | **surveil** | code | FI | perception, concealment | F. surveiller 'watch over' (sur- + veiller < L. vigilare 'keep awake') | high | keep awake over another: vigilance, and staying unseen | — |
| V040 | **thread_read** | code | TW FI | perception (the threads) | thread: OE þrǣd (þrāwan 'twist'); read: OE rǣdan 'advise, interpret, guess' | high | interpret a twisted strand: perceive, then construe | — |
| V041 | **reconstruct** | code | FI | knowing | L. re- + construere 'build again' | high | assemble the past from its remains | — |
| V042 | **tie / knot** | code | NP TW | binding | tie: OE tīegan 'bind' (tēag 'cord'); knot: OE cnotta | high | bind with a cord: make a bond that holds | — |
| V043 | **transfer** | code | EC | exchange | L. transferre 'carry across' | high | carry across: hold the thing | — |
| V044 | **utter** | code | SC FA | speech | ME uttren 'put out, make known' (out; cf. MDu uteren); also 'put coin into circulation' | high | put something outward into circulation: a voice that carries | — |
| V045 | **work** | code | EC | labour | OE wyrcan / weorc, PIE *werg- (Gk ergon) | high | labour: strength, stamina, skill | — |
| V046 | **seize** | plan | FA GV MB | taking, law | OF saisir 'take possession; put in possession' (Frankish *sazjan 'set' / ML sacire) | medium | the legal taking of seisin: a warrant, or the force to make it real | — |
| V047 | **covenant** | plan | FA SC NP | binding | OF covenant, pres. part. of convenir 'agree' < L. convenire 'come together' | high | come together in an agreement both keep | — |
| V048 | **sabotage** | plan | FA EC | concealment, making | F. saboter 'clatter in clogs; botch' (sabot 'wooden shoe') | high | botch work on purpose: know the work, do it unseen | — |
| V049 | **tend** | plan | NP EC | care | aphetic of attend (L. attendere 'stretch toward') with L. tendere 'stretch' | high | stretch one's attention toward another's needs and keep it there [object INFERRED: the plan line does not say what is tended] | — |
| V050 | **argue** | plan | SC | speech, reason | L. arguere 'make clear, prove, accuse' (PIE *arg- 'shine', cf. argentum) | high | make a matter shine clear: reasoning laid out | — |
| V051 | **train** | plan | NP MB EC | teaching | OF trainer 'drag, draw' < VL *traginare < L. trahere 'draw' | high | draw another along, again and again: patience, and command of the skill taught | — |
| V052 | **conceal** | plan | FI NP | concealment | OF conceler < L. concelare 'hide completely' (celare) | high | cover wholly | — |
| V053 | **forgive** | plan | NP | care, binding | OE forgiefan, calque of L. perdonare (for- + giefan 'give') | high | give away a debt owed: a temperament able to let go | — |
| V054 | **arrest** | plan | GV | rule, force | OF arester 'stop, stay' < VL *arrestare (ad- + restare 'stay back') | high | make another stay: force or authority | — |
| V055 | **pardon** | plan | GV | rule, mercy | OF pardoner < ML perdonare 'give wholly' | high | give a debt away wholly: own it (authority), and be willing (mercy) | — |
| V056 | **interrogate** | plan | GV FI | speech, inquiry | L. interrogare 'question' (inter- + rogare 'ask') | high | ask among, again and again, and read the answers | — |
| V057 | **charge (accuse)** | plan | SC GV | speech, judgement | OF chargier 'load' < LL carricare (carrus 'wagon') | high | lay a load on someone: standing to burden, evidence that bears weight | — |
| V058 | **raze** | plan | MB FA | destruction | OF raser 'shave, scrape' < L. radere 'scrape' | high | scrape flat: labour, and a hard heart | — |
| V059 | **detain** | plan | GV | rule, force | OF detenir < L. detinere 'hold back' (de- + tenere) | high | hold someone back: a place, and keepers | — |
| V060 | **ban** | plan | GV FA | rule, ritual | OE bannan 'summon, proclaim'; OF ban 'proclamation, jurisdiction' (Frankish *ban) | high | proclaim under penalty within one's own jurisdiction | — |
| V061 | **levy** | plan | MB FA GV | rule, war | F. lever 'raise' < L. levare 'lighten, raise' | high | raise people up from where they live | — |
| V062 | **abolish** | plan | GV | rule | F. abolir < L. abolere 'efface, destroy' | medium | make a thing cease | — |
| V063 | **proclaim** | plan | GV FA SC | speech | L. proclamare 'cry out' (pro- + clamare) | high | cry out so that many hear | — |
| V064 | **steal** | plan (refused/cut) | EC FI | taking, concealment | OE stelan, PGmc *stelan- | high | take secretly | — |
| V065 | **execute** | plan (refused/cut) | GV | rule, killing | L. exsequi 'follow out, carry out' (ex- + sequi) | high | follow through to the end | — |
| V066 | **kill** | plan (refused/cut) | PC MB | force | ME cullen / killen, prob. OE *cyllan 'strike' (cf. quell) | medium | strike down | — |
| V067 | **wound** | plan (refused/cut) | PC | force | OE wund (n.), wundian | high | hurt | — |
| V068 | **repudiate** | plan (refused/cut) | NP SC | binding | L. repudiare 'divorce, reject' (repudium) | medium | put away a bond: standing to refuse, nerve to face the shame | — |
| V069 | **designate** | plan (refused/cut) | GV | rule | L. designare 'mark out' (de- + signum) | high | mark out by a sign | — |
| V070 | **waive** | plan (refused/cut) | GV NP | binding, law | AN weyver 'abandon' (prob. ON veifa 'swing about') | medium | let go a right one holds | — |
| V071 | **muster** | lane rec | MB FA | war, display | OF moustrer 'show' < L. monstrare | high | show forces for inspection: assemble and display order | — |
| V072 | **recruit** | lane rec | FA MB NP | gathering | F. recruter < obs. recrue 'new growth' (recroître < L. recrescere 'grow again') | high | make ranks grow again: something others answer to | — |
| V073 | **withdraw** | lane rec | SC MB | motion, speech | with- 'back, against' + draw | high | draw back what one put forward | — |
| V074 | **deny** | lane rec | SC GV | speech, judgement | OF denier < L. denegare 'say no' (de- + negare) | high | say no and make it stick | — |
| V075 | **lie** | lane rec | SC FI | speech, deceit | OE lēogan, PGmc *leugan- | high | say what is not so and be believed | — |
| V076 | **weave** | lane rec | TW | making (the threads) | OE wefan, PIE *webh- | high | interlace strands into a pattern | — |
| V077 | **pull** | lane rec | TW | force (the threads) | OE pullian 'pluck, snatch' | medium | draw a strand toward oneself by force | — |
| V078 | **lock** | lane rec | TW | binding (the threads) | OE loc 'fastening, bolt' | high | fasten shut, and keep it shut | — |
| V079 | **loosen** | lane rec | TW NP | binding (the threads) | ON lauss 'loose' + -en | high | undo a binding without tearing | — |
| V080 | **sever** | lane rec | TW | force (the threads) | OF sevrer < L. separare 'separate' | high | part what is joined | — |
| V081 | **mend** | lane rec | TW EC NP | making, care | aphetic of amend < L. emendare 'remove a fault' (ex- + menda) | high | find the fault and take it out: know the whole | — |
| V082 | **leap** | lane rec | TW WT PC | motion | OE hlēapan 'jump, run' | high | spring: daring and bodily power | — |
| V083 | **interpose** | lane rec | PC | force, protection | L. interponere 'place between' | high | put oneself between: quickness and courage | — |
| V084 | **rescue** | lane rec | PC MB | force, care | OF rescorre < L. re- + excutere 'shake out' (quatere) | high | shake someone loose from captors: force, speed | — |
| V085 | **champion** | lane rec | PC MB SC | contest | LL campio 'fighter of the field' (campus) | high | be the one chosen to fight in the field for others: prowess and standing | — |
| V086 | **surrender** | lane rec | MB PC FA | binding, war | OF surrendre 'give up' (sur- + rendre < L. reddere 'give back') | high | render oneself or a place up, on terms | — |
| V087 | **storm** | lane rec | MB | war, force | OE storm 'tempest'; the verb 'assault violently' by figure | high | fall on a place like weather: ferocity and numbers | — |
| V088 | **sack** | lane rec | MB | war, taking | F. sac (mettre à sac 'put in the bag') < It. sacco < L. saccus 'bag' | high | bag the goods: plunder, the lapse of restraint | — |
| V089 | **abdicate** | lane rec | GV | rule, renunciation | L. abdicare 'disown, renounce' (ab- + dicare 'proclaim') | high | proclaim a thing away from oneself | — |
| V090 | **depose** | lane rec | GV FA | rule, force | OF deposer 'put down' < L. de- + ponere | high | put another down: coalition and force | — |
| V091 | **declare (war)** | lane rec | FA | speech, rule | L. declarare 'make clear' (de- + clarare < clarus) | high | make one's stance clear in public | — |
| V092 | **marshal** | lane rec | MB | war, order | OF mareschal < Frankish *marhskalk 'horse-servant' | high | groom of horses, then the officer who arrays: arrangement and order | — |
| V093 | **betray** | lane rec | NP FA | binding, deceit | ME bitraien (be- + OF traïr < L. tradere 'hand over') | high | hold a trust, then hand it over: access first, concealment until the moment | — |
| V094 | **strike** | designed here | PC | force | OE strīcan 'go, move lightly, stroke' | medium | a sweeping stroke: timing of the arm | the basic move of a bout; fight is a whole contest, not its moves |
| V095 | **guard** | designed here | PC MB GV | protection, perception | OF garder < Frankish *wardōn 'watch, keep' | high | watch over: vigilance before strength | defence in a bout, and keeping a person or a place |
| V096 | **parry** | designed here | PC | force | F. parer 'ward off' < It. parare 'prepare, ward off' < L. parare 'prepare' | high | be prepared: read the blow before it lands | an active defence, distinct from guard's posture |
| V097 | **dodge** | designed here | PC | motion | origin unknown (16c 'move to and fro') | low | (root unclear) | defence with the body, not the weapon: the unarmoured fighter's act |
| V098 | **feint** | designed here | PC | deceit | OF feint, p.p. of feindre 'feign' < L. fingere 'shape, contrive' | high | shape a false move | deception inside a bout; the duel's mind game |
| V099 | **grapple** | designed here | PC | force | from grapple 'hook' < OF grapil (Prov. grapa 'hook') | medium | hook on and hold | close fighting, and taking a prisoner alive |
| V100 | **disarm** | designed here | PC | force | OF desarmer (des- + armer < L. armare) | high | strip another of his arms | a non-lethal outcome; makes capture possible |
| V101 | **shoot** | designed here | PC MB WT | force at range | OE scēotan 'shoot, go swiftly' | high | send a missile fast and true | ranged fighting and hunting; different bodily demands from melee |
| V102 | **rush** | designed here | PC MB | motion, force | ME russhen < AN russher 'drive back' (prob. OF reüser < L. recusare) | low | drive forward with force | the charge on foot or horse; closes distance |
| V103 | **disengage** | designed here | PC MB | motion | F. dégager 'redeem from pledge' (dé- + gage) | high | take back what one pledged: get out cleanly | leaving a fight; withdrawing from a field |
| V104 | **yield** | designed here | PC MB SC | binding, submission | OE gieldan 'pay, render, worship' | high | pay what is owed: submission as payment | surrender inside a bout, so fights can end without a death |
| V105 | **ambush** | designed here | PC MB FA | concealment, war | OF embuschier 'place in a wood' (en- + busche) | high | put oneself in the wood and wait: concealment, ground, patience | the surprise attack that inverts the odds |
| V106 | **assassinate** | designed here | PC FA | concealment, killing | It. assassino < Ar. ḥashīshī (polemical name for the Nizaris) | high | a hidden political killing: covert access, nerve | the political murder that faction intrigue otherwise lacks |
| V107 | **reconnoitre** | designed here | MB FI | perception | obs. F. reconnoître 'recognize, explore' < L. recognoscere 'know again' | high | know the ground again: recognize what matters | scouting before a march; information is a commander's first need |
| V108 | **encamp** | designed here | MB WT | war, shelter | en- + camp < L. campus 'field' | high | set oneself down in a field | armies spend most nights in camp; disease, desertion and surprise live there |
| V109 | **fortify** | designed here | MB GV | making, war | F. fortifier < LL fortificare (fortis 'strong' + facere) | high | make strong | defence of places; turns labour into resistance |
| V110 | **forage** | designed here | MB WT | gathering | OF fourrager < fuerre 'fodder' (Frankish *fōdr) | high | find fodder in the land | armies feed off the land; foraging is how war harms settlements |
| V111 | **provision** | designed here | MB EC GV | logistics | L. provisio 'foresight' < providere 'see ahead' (pro- + videre) | high | see ahead: foresight and reckoning | the quartermaster's act; supply decides campaigns |
| V112 | **besiege** | designed here | MB | war | be- + siege < OF sege 'seat' (VL *sedicum < sedere 'sit') | high | sit down before a place and outlast it | most pre-modern war was siege |
| V113 | **rally** | designed here | MB PC | war, speech | F. rallier 're-ally' (re- + allier < L. alligare 'bind to') | high | bind men to one again | morale recovery; the commander's personal intervention in a field |
| V114 | **pursue** | designed here | MB PC FI | motion | AN pursuer < L. prosequi 'follow on' | high | follow on without stopping | routs become slaughters in pursuit; also the chase of a fugitive |
| V115 | **retreat** | designed here | MB | motion, war | OF retraite < L. retrahere 'draw back' | high | draw back in order | the hardest manoeuvre; distinct from a rout |
| V116 | **command** | designed here | MB GV FA | rule, war | OF comander < VL *commandare (L. commendare 'entrust'; mandare 'give into the hand') | high | give an order into another's hand and be obeyed | the field commander's act, distinct from marching to the field |
| V117 | **drill** | designed here | MB | teaching, war | Du. drillen 'bore, turn round' | high | turn men round and round until it holds | experience and training make troops differ in quality |
| V118 | **withstand** | designed here | MB PC | force, will | OE wiþstandan 'stand against' | high | stand against: steadiness | holding a line; resisting a charge |
| V119 | **persuade** | designed here | SC | speech | L. persuadere (per- + suadere 'urge', akin to suavis 'sweet') | high | make a thing sweet to another | the general act of changing a mind (argue is proof; this is appeal) |
| V120 | **plead** | designed here | SC GV | speech, law | OF plaidier < L. placitum 'what pleases; a decision' | high | make one's case please the court | speaking at a bench for oneself or another |
| V121 | **threaten** | designed here | SC FA | speech, force | OE þrēatnian (þrēat 'pressure, oppression, a throng') | high | press on another: something behind the words | coercion by words rather than deeds |
| V122 | **flatter** | designed here | SC NP | speech | OF flater 'stroke, caress with the flat hand' | medium | stroke vanity | courtly speech; access to the powerful |
| V123 | **bargain** | designed here | EC SC | exchange | OF bargaignier 'haggle' (prob. Frankish) | low | haggle | a price is made between two people |
| V124 | **refute** | designed here | SC | reason | L. refutare 'drive back, rebut' | high | beat back a claim | the contest's counter-move |
| V125 | **concede** | designed here | SC FA | speech | L. concedere 'withdraw, yield' (con- + cedere) | high | give way, judging when | ending a contest on one's own terms |
| V126 | **testify** | designed here | SC FI GV | speech, record | L. testificari < testis 'witness' (*tri-st- 'a third who stands by') | high | have stood by and seen | courts and inquiry need witnesses, not only tellers |
| V127 | **vote** | designed here | SC GV FA | rule, assembly | L. votum 'vow, wish' (vovere) | high | have a voice in the assembly | councils, chapters and guilds decide by voice |
| V128 | **preach** | designed here | SC NP | speech, ritual | OF preechier < L. praedicare 'proclaim publicly' (prae- + dicare) | high | proclaim before a crowd | religious persuasion of the many; the church's speech act |
| V129 | **insult** | designed here | SC PC | speech, force | L. insultare 'leap upon' (in- + salire 'leap') | high | leap on another with words | the social move that starts duels |
| V130 | **praise** | designed here | SC NP | speech | OF preisier 'value' < LL pretiare (pretium 'price') | high | set a price on another | public approval; raises the standing of the praised |
| V131 | **counsel** | designed here | SC GV | speech, judgement | OF conseiller < L. consilium (consulere 'deliberate') | high | deliberate well on another's behalf | advisers move rulers |
| V132 | **mediate** | designed here | SC FA | speech, judgement | LL mediare 'be in the middle' | high | stand in the middle, trusted by both | settling a dispute without a bench |
| V133 | **search** | designed here | FI WT | perception | OF cerchier < L. circare 'go around' | high | go round, missing nothing | finding a hidden thing or person: the counter to conceal |
| V134 | **track** | designed here | FI WT MB | perception | OF trac 'track, trace' (prob. Germanic; cf. MDu treck 'pull') | medium | follow marks | following a fugitive or game |
| V135 | **eavesdrop** | designed here | FI | perception, concealment | OE yfesdrype 'eaves-drip': one who stands under the eaves to hear | high | stand close, unseen, and listen | the overheard secret, distinct from watching movement |
| V136 | **decipher** | designed here | FI | reason, letters | de- + cipher < ML cifra < Ar. ṣifr 'empty, zero' | high | undo a cipher | secret correspondence is the stuff of intrigue |
| V137 | **shadow** | designed here | FI | concealment, perception | OE sceadu 'shade' | high | be another's shade | covert following of a person |
| V138 | **infiltrate** | designed here | FI FA | concealment | in- + ML filtrare (filtrum 'felt') | high | seep through as liquid through felt | placing a person inside a rival's household |
| V139 | **disguise** | designed here | FI NP | concealment | OF desguisier 'change one's guise' (des- + guise < Frankish *wīsa 'manner') | high | unmake one's manner and take another | travel and infiltration under a false identity |
| V140 | **bribe** | designed here | FI FA GV | exchange, corruption | OF bribe 'a morsel given to a beggar' | medium | hand over a morsel: means, and a judgement of who will take it | corruption of officials; the cheap alternative to force |
| V141 | **audit** | designed here | FI GV EC | knowing, number | L. auditus 'hearing' (audire): accounts were heard read aloud | high | hear the accounts and catch the wrong note | detecting embezzlement; a governor's check on his stewards |
| V142 | **ward** | designed here | TW PC | protection | OE weardian 'guard, keep' | high | keep watch over | defence against another's threadwork [INFERRED] |
| V143 | **anchor** | designed here | TW NP | stability | L. ancora < Gk ankyra (ank- 'bend') | high | hold fast by a hook | resisting the loss of self under thread strain [INFERRED] |
| V144 | **trace** | designed here | TW FI | perception | OF tracier < VL *tractiare < L. trahere 'draw' | high | follow a drawn line | following a strand to its source: who did this [INFERRED] |
| V145 | **tax** | designed here | GV EC | rule, number | L. taxare 'assess, appraise, censure' | high | assess value | the regular revenue act, distinct from requisition's extraordinary demand |
| V146 | **patrol** | designed here | GV MB | perception, rule | F. patrouiller, earlier patouiller 'paddle in mud' | high | tramp about | keeping order; suppressing banditry |
| V147 | **steward** | designed here | GV EC | care, rule | OE stigweard 'hall-keeper' (stig 'hall' + weard 'keeper') | high | keep another's house | managing a holding for its lord: the honest and the dishonest steward |
| V148 | **ration** | designed here | GV MB EC | number, care | F. ration < L. ratio 'reckoning' | high | reckon out shares | managing shortage in siege and famine |
| V149 | **relieve** | designed here | GV NP | care | OF relever 'raise again' < L. relevare | high | raise up again | famine relief and alms: the ruler's care act |
| V150 | **conspire** | designed here | FA | binding, concealment | L. conspirare 'breathe together' | high | breathe together: secrecy among the trusted | coups and plots: the many-person covert act |
| V151 | **suborn** | designed here | FA FI | corruption | L. subornare 'equip secretly, incite' (sub- + ornare) | high | furnish another in secret to act against his own | turning an enemy's man |
| V152 | **ransom** | designed here | FA MB | exchange | OF rançon < L. redemptio 'buying back' | high | buy back | the economy of captives |
| V153 | **negotiate** | designed here | FA SC EC | exchange, speech | L. negotiari 'do business' (neg- + otium 'leisure') | high | do business: patience and a sense of value | treaties between factions (bargain is the market act) |
| V154 | **craft** | designed here | EC | making | OE cræft 'power, strength, skill' | high | the word itself joins strength and skill | the general making of goods (forge is narrower) |
| V155 | **cultivate** | designed here | EC | making, care | ML cultivare < L. colere 'till, inhabit, worship' | high | till and tend over seasons | farming is the base of the economy |
| V156 | **appraise** | designed here | EC FI | judgement | OF aprisier 'set a price on' (pretium) | high | set a price | valuing goods, estates, ransoms |
| V157 | **lend** | designed here | EC NP | exchange, binding | OE lǣnan (lǣn 'loan') | high | grant for a time and trust its return | credit; debt as a social bond |
| V158 | **hire** | designed here | EC MB | exchange | OE hȳrian 'pay for service' | high | pay for service | mercenaries and labourers: a market for people |
| V159 | **haul** | designed here | EC MB WT | motion, force | F. haler 'pull' (Germanic) | high | drag | carting goods; logistics |
| V160 | **hoard** | designed here | EC | concealment, keeping | OE hord 'treasure' (a hidden store) | high | hide a store | keeping stores back in shortage |
| V161 | **smuggle** | designed here | EC FI | concealment, exchange | LG smuggeln 'sneak' | high | sneak goods past watchers | evading tolls and bans |
| V162 | **navigate** | designed here | WT | travel, knowing | L. navigare 'sail' (navis + agere) | high | drive a ship: find the way | travel off roads and by water |
| V163 | **ride** | designed here | WT MB PC | motion | OE rīdan | high | be carried and keep one's seat | speed of travel; cavalry |
| V164 | **sail** | designed here | WT EC | travel | OE seglian | high | work a sail | sea trade and travel |
| V165 | **climb** | designed here | WT PC | motion | OE climban | high | go up, gripping | walls and cliffs; escalade |
| V166 | **swim** | designed here | WT | motion | OE swimman | high | keep oneself up in water | rivers bound travel and battlefields |
| V167 | **hunt** | designed here | WT EC NP | gathering, force | OE huntian (cf. hentan 'seize') | high | seize game: tracking, patience, aim | food, a noble pastime, a social occasion |
| V168 | **endure** | designed here | WT MB | will, body | OF endurer < L. indurare 'make hard' (durus) | high | harden | weather, hunger, sickness on the road |
| V169 | **heal** | designed here | NP WT MB | care | OE hǣlan 'make whole' (hāl; cf. hale, whole, holy) | high | make whole: knowledge of the body, patience | wounds and illness need a counter-act |
| V170 | **court** | designed here | NP SC | bonds, speech | OF cort < L. cohors 'enclosure, retinue' | high | attend at court: manners and charm | marriage and favour are won by courting |
| V171 | **marry** | designed here | NP FA | binding | OF marier < L. maritare (maritus 'husband') | high | provide oneself with a spouse: standing, alliance | dynastic alliance is the oldest faction act |
| V172 | **rear** | designed here | NP | care | OE rǣran 'raise, lift up' (causative of rise) | high | raise up over years | heirs: a game across generations needs children raised |
| V173 | **mourn** | designed here | NP | care, ritual | OE murnan 'grieve, long for' | high | grieve | loss changes people; mourning shapes vengeance and loyalty |
| V174 | **pray** | designed here | NP TW | ritual | OF preier < L. precari 'entreat' (prex) | high | entreat a power above: the posture of petition | religion runs through governance; prayer is its ritual act |
| V175 | **avenge** | designed here | NP FA PC | justice, force | OF avengier < L. vindicare 'claim, punish' | high | lay claim to redress | blood feud drives conflict nobody scripted |
| V176 | **confess** | designed here | NP SC | speech, ritual | OF confesser < L. confiteri 'acknowledge' (con- + fateri) | high | acknowledge fully | sacrament and law: a truth that changes standing |
| V177 | **study** | designed here | NP FI | knowing | OF estudier < L. studere 'be eager, apply oneself' | high | apply oneself with zeal | learning letters, law, lore: how skills grow |
| V178 | **recover** | designed here | NP WT | body | OF recovrer < L. recuperare 'get back' | high | get back one's health | healing over time is the body's own act |
| V179 | **bless** | designed here | NP TW GV | ritual | OE blētsian 'mark with blood, hallow' (blōd) | medium | hallow: a sacred office | ritual legitimacy: crownings, oaths, marriages |
