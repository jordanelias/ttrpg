# Research map — institutions B (Venice, the Medici and the city-states, the Hanse and guilds; colonial, empire, tribute, vassalage, company)

## Status: REFERENCE (a map of what the tree's own research holds; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: 62dbc8b (working tree), 2026-11-12

Written by the re-grounding lane under Jordan's direction of 2026-11-12: *"Research should have been found
in /research or /proposals."* It records, for the VENICE and COLONIAL families, which files of `research/`,
`proposals/`, `.audit/` and `.designs/` treat which institution, to what depth, and with what caveat of
their own. It explains a judgment about two artifacts that already exist
(`audits/15_INSTITUTIONS_VENICE.md`, `audits/15_INSTITUTIONS_COLONIAL.md`); it queues nothing. The sibling
map for the Byzantine and papacy families is `unified/RESEARCH_MAP_INSTITUTIONS_A.md`; its depth marks are
used here unchanged.

**How the list was made.** `grep -rIil` for the twenty-three terms of the work order over
`research proposals --include=*.md` (624 files, the suite itself excluded: 128 in `research/`, 496 in
`proposals/`) and over `.designs .audit` (260 files); each hit ranked by its count of matches; then a
second pass with exact terms for each claim the two audits marked memory-grade (for example `\bArsenal`,
`rettor`, `sindic`, `Kontor`, `condotta`, `residencia`, `Casa de Contrataci`, `pronoia`, `sankin`,
`tax farm`, `quo warranto`), because several of the work order's terms match by accident (`commenda`
matches "recommendation" in 236 files and the word itself in none; `rector` matches "director"; `Monte`
matches "Monte Carlo"; `mita` and `inca` match ordinary words). **Depth marks**: `FULL` read end to end;
`SECTION` the named sections read in full; `LINES` every matching line read with its paragraph (the
corpus's lines are paragraph-length, so this is the passage, not a snippet); `COUNT` only counted. Grade
of the research itself is its own: all of it is tier 3 (`research/00_INDEX.md` §1), informs and never
settles; a figure in it is a lead (the sourcing floor).

## 0. The claims this map corrects, exactly

1. **Venice lane, sourcing key: "`[M]` … not opened this session … No web source was fetched"**, and its
   evidence log E-4: *"`.audit/2026-07-09-comparative-governance-research` … `[SKIPPED: grep only;
   superseded in content by research/governance/, per its manifest]`"*. The skip was wrong. The manifest
   says the governance corpus *"reorganizes and deepens"* the two earlier dockets
   (`research/governance/00_MANIFEST.md:5-10`); it does not carry their content over. The skipped file
   holds a thirteen-row reference table titled *"Venice — the Stato da Mar / Terraferma administrative
   system specifically (not the Great Council/doge-election apparatus, which is already mined)"*
   (`.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:87-103`), a
   nine-row table for Renaissance Italy outside Venice (`:105-117`) and a twelve-row table for Habsburg
   Spain (`:119-134`), each row with its named source. That is the tree's source for the Arsenal, the
   state forests, the *dedizione* pacts, the rector as broker, the citizen secretaries, the guilds under
   the Giustizia Vecchia, the Scuole Grandi, the rector's fixed term and contact bans, the syndics and the
   *relazione*, the graded posting ladder, the Provveditore Generale da Mar, the Cretan military colonists,
   the podestà and his *sindacato*, the *condotta*'s phases, Sforza, the cipher chancery, the Mercanzia and
   the Arte della Lana. The Venice audit marked every one of these `[M]`.
2. **Colonial lane, §2 head: "the tree holds no research file on the chartered companies, the Spanish
   Indies beyond the residencia, settler colonies, indirect rule in Africa and India, or the Mongol system
   (a grep of `research/` for those terms returns passing mentions only, §15 E-2)"**, and E-2 itself. The
   grep was over `research/` alone, and E-2 reports its hits as *"the historical action catalogue's
   one-line crisis list"*. They are not one line. `research/historical_concerns_action_catalogue_v1.md`
   gives each of these a full entry (trigger, three answers, follow-on, the act it adds, the loop): the
   **VOC's conquest of Banda** and a Company-run governor (`:163`); **Plassey, the Jagat Seth bankers and
   the Diwani of Bengal** (`:166`); the **Mongol *ortoq*** partnership and the *paiza* (`:165`); the
   **Toluid civil war** and the appanage (`:46`); the **Ottoman capitulations** (`:169`); **Kilwa's
   withheld tribute** (`:167`); the **Portuguese *cartaz*** (`:54`); the **Barbary tribute** (`:56`); the
   **Quartering Acts** (`:71`); the **Norse Greenland colonies** (`:138`); the **Fugger loan for the
   imperial election** (`:161`); **Edward III's default on the Bardi and Peruzzi** (`:148`). The **East
   India Company under the Regulating Act of 1773** is `research/proactive_governance_scale_research_v1.md:147`
   (X7), named there *"the exemplar of Organization-scale management"*. The **Casa de Contratación and
   the Consulado de Sevilla**, **Spanish venality**, **Venetian Crete's military-colonist charter** and the
   ***juros*** are `comparative_governance_research_v1.md:134`, `:132`, `:103`, `:130`. **The sale of
   colonial offices priced by distance** is `research/rise_to_power_roster_system_research_v1.md:518`
   (I9). **Post-colonial governance** as such has its own section, `research/historical/precedents_analysis.md:172-246`.
   What the tree does not hold, and §3 records as still memory-grade: the English and Dutch companies'
   internal constitution (directors, shareholders, factories, private trade, renewal fights); the
   *encomienda* and the *repartimiento*; the Atlantic settler colonies beyond the Quartering Acts; indirect
   rule in Africa and India (the resident, the subsidiary treaty, lapse); the Mongol patent, census and
   resident overseer; transit times; and the formula "I obey but do not execute".
3. **Both lanes: "the digests were not opened; the research was read directly."** The digests were not
   needed; the `.audit/` compendium and the 2026-10-29 debate corpus were, and neither lane opened them.

§1 is the file list by institution; §2 the claim-by-claim table for the two audits (claim, the audit's
mark, the tree's source at path:line, and whether the source agrees, corrects or is silent); §3 what
remains memory-grade; §4 the mechanisms the research describes that the two designs did not carry, with
the file that now carries each.

**Short names used below.** `GM` `research/governance/governance_modes.md` · `PHS`
`research/governance/political_hierarchy_standing.md` · `CPS` `research/governance/conflicts_power_struggles.md`
· `CGR` `.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md` · `PMP`
`.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md` · `FASE`
`research/fa_se_historical_precedent_research_v1.md` · `PGS` `research/proactive_governance_scale_research_v1.md`
· `HCC` `research/historical_concerns_action_catalogue_v1.md` · `RTP`
`research/rise_to_power_roster_system_research_v1.md` · `VP` `research/social_contest_procedures/01_venice_procedure.md`
· `DPC` `research/social_contest_procedures/04_decision_procedure_catalog.md` · `PA`
`research/historical/precedents_analysis.md` · `PW` `research/historical/precedents_warfare.md` · `GPC`
`research/valoria_game_precedent_companion_v1.md` (and `_partN`) · `GPS` `research/game_precedent_suite/`.

## 1. Where the tree treats each institution

### 1.1 Files read, with depth

| file | depth | what it holds for these two families | its own caveat |
|---|---|---|---|
| `GM` | SECTION (synthesis; Ottoman; Roman; Carolingian; HRE; Renaissance Italy; Venice) · COUNT (Han, Japan beyond `sankin-kōtai`) | the Venetian constitution (`:313-358`); Florence, Milan, Genoa, the Papal States, 1494 (`:250-301`); provincial governorship, the *publicani* (`:127`); *missi* (`:158`); the general oath (`:170`); Quierzy and heritable office (`:154`); elective empire, two-stage legitimation, immediacy and mediatization, *ministeriales* (`:188-235`); the millet (`:76`) | each civilisation "adversarially verified", every verdict `SOUND_WITH_FIXES`, **and the fixes are quoted, not applied** (`:306-311`): the body text and the correction disagree in places (§2, V-1, V-2). Byzantium omitted |
| `PHS` | SECTION (synthesis; Florence to Venice `:255-388`; Roman routes down `:136-144`) · LINES (timar, benefice, *go-on to hōkō*, *kaieki*) | the office ladders; "who controls the list" (`:323-324`); the three Venetian orders, the *Balla d'Oro*, the citizen secretaries, the routes up and down (`:338-388`); *lex repetundae* and Verres (`:139`); hostage-kin at Rome (`:144`); the Kamakura vassal contract and its unpaid bond (`:457-461`) | as `GM` |
| `CPS` | SECTION (Renaissance Italy `:245-283`; Venice `:295-327`) · LINES (Japan 3.2) | the Ciompi, Cosimo's exile and recall, the Pazzi, Sforza, Genoa's submissions, Savonarola, 1494; Candiano, Tiepolo–Querini, Faliero, Chioggia, Agnadello, the Ten's scope, Foscarini, the *barnaboti* | as `GM` |
| `CGR` | SECTION (head `:1-22`; the Venice, Italy and Spain tables `:87-134`; the judgment pass `:138-161`, `:186-356`) | the thirteen-row *Stato da Mar / Terraferma* table; the podestà and *sindacato*; the *condotta*; Sforza; the cipher chancery; legates; the Sommaria; the Seggi; the Arte della Lana; the Mercanzia; the corregidor; the councils; the *valido*; the Cortes; the Mesta; the *gremios*; the *juros*; venality; the Casa de Contratación; and a KEEP/CUT verdict on each as a mechanic | table cells are abridged in the file itself ("…"); "findings that could not be positively confirmed were dropped" (`:7`); hidden tree, not canon |
| `PMP` | SECTION (§2 `:58-156`; P26 to P45 `:444-559`; §5.3, §5.4 `:629-667`) | the doge's election with its supermajorities; the Venetian courts; the three itinerant auditors; assessment; hostage-taking; decree with compliance; the two-officer model; the *relazione* and the diplomatic grades; the loop *charter, assessment, appointment, decree, inspection, sanction* | a self-authored upload with evidence tiers `[T0/T1/T2]`; its §7 is its own adversarial audit; hidden tree |
| `FASE` | FULL (`:56-255`) · LINES (rest) | the ten themes T1 to T10 and the distillations FA-1 to FA-9, SE-1, SE-2 | "all numeric values … shape-suggestions" (`:182`) |
| `PGS` | FULL | the four scales; the organisation as a body with branches it does not own (`:23`); O1 to O15, T1 to T19, F1 to F14, X1 to X13; the reuse ledger; its limitations | "many are self-labeled 'sketch'" (`:290`); relay levers "contingent on a temporal model that isn't authored yet" (`:294`); "zero numbers, by design" (`:303`) |
| `HCC` | SECTION (§2.1, §2.2, §2.9, §2.10 in full; §2.3 the six siege entries read) · LINES (the rest) | the 94 worked historical events; the trade, debt, company, tribute and garrison entries listed in §0 | figures flagged where a verifier doubted them; written against the retired Directive/Ledger vocabulary |
| `RTP` | SECTION (§1; category A) · LINES (C6, C7, C10, F5, F6, F9, H6, I2, I6, I9, I10, J2, J9; every entry head) | the eight mechanisms of rise; Cosimo (A3, H6, with Padgett and Ansell cited); Sforza (F5, Mallett cited); Wallenstein (F6); the keshig (F9); venality (I1 to I10) | "fact-check shown for only some entries" (the debate corpus's note on it) |
| `VP`, `DPC` | LINES (`VP`: the Venice lane read it in full; `DPC:57-61` read here) | `DPC:57`: the Florentine draw stage by stage, *veduto* and *seduto*, tax arrears among the bars; `:59` the doge's election; `:61` *broglio* | `DPC` lists four errors in its own original |
| `PA`, `PW` | SECTION (`PA` §2, §4; `PW` §1.3b, the transfer list `:141-150`) | invasion on the heels of civil war and **invited entry** (`PA:64-98`); **post-colonial and post-occupation governance** (`PA:172-246`); the feudal levy's term and the indenture (`PW:47`, `:110`); the Hanse as dependency without conquest (`PW:147`) | dated 2026-04-17, "ANALYSIS, not a design doc" |
| `research/pre_firearms_formations/05_late_med_renaissance_europe.md` | SECTION (§8 `:468-493`) | the condottieri's preservation doctrine and its end in 1494 | military, not contractual |
| `GPC` and parts 2 to 8 | LINES | *dedizione*, split command, decree with compliance, assessment (`GPC:195-214`); **John Company** (`GPC:89`; `_part5:42`; `_part6:165-175`; `_part7:41`, `:154`); the admission that the conquest-terms model "is carried almost entirely by Venice rather than by any game" (`_part5:240-244`) | reference, not canon |
| `GPS/THROUGHLINES.md`, `tables/R8`, `tutorials/T14` | LINES | P14 the obligation token (`:30`, `:79`); P19 the career ladder (`:84`); **Patrician IV** (`R8:81-110`); **The Guild 2 and 3** (`T14:228`, `:281-313`) | claims tagged `[V3]` fetched, `[V2]`, `[M]` |
| `research/by_lane/FA_*`, `SE_*`, `SC_*`, `IN_*`, `NPC_*` | COUNT (indexes: every relevant row points at a file listed above) | which precedent reached which hole | "PARTIAL / UNREACHED" marks are the lanes' own |
| `research/provenance/2026-08-28-systems-integration-harvest/H4, H8A, H8B` | LINES | harvest records of the same proposals (VEN-SE-1, IT-2, X8) | provenance only |
| `.audit/2026-07-12-governance-compendium/` `00`, `43`, `tier3` | SECTION (`43` §1; `tier3` rows IT-1, IT-2, HRE-4, the vindicated cuts `:146-148`) · COUNT (`40`, `41`, `42`, `44`, `_workings_joined`: restatements of `RTP`, `PGS`, `HCC`) | the Directive kinds *Embargo, Recall, Quarter, Nationalize Charter*; play found IT-3 (Sforza), VEN-SE-4 (*dedizione*) and VEN-SE-7 (the syndics) wrongly cut | PROPOSED; hidden tree |
| `.designs/systems/settlements/reference/settlement_layer_v30.md` | SECTION (`:597-672`) | charters, prescription at `floor(age ÷ 8)`, quo warranto past about sixteen seasons, confirmation for a fee; the patron-backed privilege that lapses with its patron | ARCHIVED-NOT-CANON; "shape proposals … not sim-calibrated" (`:642-644`) |
| `.designs/systems/factions/reference/faction_politics_v30.md` | LINES (`:123-131`, `:566-568`, `:578-585`) | court attendance and hostage-kin; the Guild ladder to Comptroller; guarantor entry; bought mastership | ARCHIVED-NOT-CANON |
| `.designs/systems/factions/reference/faction_layer_v30.md`, `faction_canon_v30.md`, `.designs/systems/npcs/reference/npc_roster_v30_infill.md` | LINES | the Tributary treaty row (`faction_layer:114`); the Renaissance stat analogues (`faction_canon:217`); the Medici branch manager as Virke's echo (`npc_roster_v30_infill:62`) | ARCHIVED-NOT-CANON |
| `proposals/2026-10-29-parliament-and-debate/2026-10-29-debate-corpus-by-theme*.md` | LINES (every `HP-` item matching the terms) | a second index of the same research by line: HP-013 to HP-047, HP-064 to HP-070, HP-095 to HP-104 | each item carries its source's status |
| `proposals/2026-09-10-settlements-factions-populations/05_COLLISIONS_AND_RESIDUE.md` | SECTION (`:1-36`, `:76-84`) | the tree's own re-expression of the research's Debt, Compact, Precedent, Grudge, Suspicion, Clerk, Survey and Encabezamiento on Layer-1 primitives | PROPOSED, **held back in full** |
| `proposals/2026-10-16-verbs/…-16-lexicon-economy-trade-and-craft.md`, `…-20`, `…-23` | LINES | M7 the ban term for embargo, staple right and licence (`-16:615`, `:635`); FA-G33 (`-20:138`); EC-G24 debt, EC-G29 toll and staple (`-23:56`, `:61`) | gap registers |
| `proposals/2026-10-03-verb-coverage-and-gap-fill.md` | LINES (the Venice lane read K-14 at `:1478`, `:2685-2693`, `:4495`) | debt and distraint deferred together | — |
| `proposals/2026-11-08-flow-conditioning/`, `proposals/2026-10-07-settlements-computation-modules.md` | COUNT | nothing on these institutions (cohort and site content; computation modules) | — |

### 1.2 By institution: where to look first

| institution | first source | second | game precedent in the tree |
|---|---|---|---|
| the Venetian constitution, councils, election | `GM:313-358` | `VP`; `PMP:64-70`, `:110-112` | none shipped; `GPC` carries it as history |
| Venice's rule over subject places | `CGR:94-103` | `PMP:119`, `:138-140`, P36, P37; `PGS:148` (X8); `CPS:314` | none (`GPC_part5:240-244` says so) |
| the Arsenal, the state forests | `CGR:91-92` | `PHS:342`; `CPS:306` | — |
| the citizen secretaries, the *relazione*, the sealed channel | `PHS:362`; `PMP:150-154`, P28, P30 | `CGR:96`, `:100` | — |
| Florence's scrutiny, bags and the Medici method | `GM:250-274`; `DPC:57` | `PHS:269-293`, `:323-324`; `CPS:252-258`; `RTP:68-71`, `:452-455` | — |
| the bank and the loan to a prince | `HCC:148`, `:161`, `:166` | `CGR:130` (*juros*); `PGS:76` (Fugger audit); `GM:269` | Patrician IV's loans, thinly (`GPS/tables/R8:89`) |
| the condottiere and the contract | `CGR:110-111` | `RTP:340-348`; `FASE:192-196`; `HCC:67`; `pre_firearms…/05:468-493`; `PHS:297-305` | Jagged Alliance 2's term contract (`GPS/THROUGHLINES:79`) |
| the Hanse and the Kontor | `FASE:119`, `:236-240`; `PGS:78` | `HCC:55`, `:160`; `PW:147`; `PGS:84`, `:123` | **Patrician IV** (`GPS/tables/R8:81-110`) |
| the guild | `CGR:97`, `:116-117`, `:129` | `PGS:77`; `faction_politics_v30:566-585` | **The Guild 2 and 3** (`GPS/tutorials/T14:228`, `:281-313`) |
| the governor at distance and his audit | `FASE:123-132`; `PMP` §5.3 | `CGR:99-102`, `:123`, `:132`; `RTP:483-486`, `:518-521`; `PHS:139` | none found |
| tax farming, venality | `FASE:99-103`, `:204-208` | `RTP:488-527`; `HCC:148` | — |
| charter, prescription, calling-in | `FASE:114-121` | `settlement_layer_v30:597-672`; `HCC:55`, `:61`, `:160`, `:169` | — |
| tribute, clientage, hostage-kin | `FASE:176`, `:230-234` | `HCC:56`, `:167`; `PHS:144`; `PMP:132`, P35; `RTP:185`, `:360`; `faction_politics_v30:123-131` | Songs of Syx, Nobunaga vassal states (`GPS/THROUGHLINES:77`) |
| vassalage and the fief | `PHS:457-461` (Kamakura); `GM:154`, `:170` | `PW:47`, `:110`; `HCC:41` | CK3's negotiable contracts (`GPC:84-86`) |
| the chartered company | `HCC:163`, `:166`; `PGS:147` | `CGR:134`; `PGS:84`; `HCC:165`, `:168` | **John Company** (`GPC_part6:165-175`) |
| the settler and the frontier | `FASE:152-159` | `CGR:103`; `PGS:104-108`; `HCC:71`, `:138` | — |
| the former colony | `PA:172-246` | `PA:64-98`; canon | — |
| distance, the post, the envoy's latitude | `PMP` P33, §5.4 item 2 | `PGS:94-99`, `:294`; `RTP:518`; `CGR:102` | none: the tree flags it as unmodelled (`PGS:294`) |

## 2. Claim by claim

Marks: **AGREES** the tree's source says what the audit said; **CORRECTS** it says something different,
and the audit is changed; **PARTIAL** the source covers part, the rest stays memory-grade; **SILENT** no
source found in the tree, the claim stays memory-grade. Row ids are used in the two audits' new sections.

### 2.1 Venice lane (`audits/15_INSTITUTIONS_VENICE.md`)

| id | the audit's claim (section) | its mark | the tree's source | verdict |
|---|---|---|---|---|
| V-1 | "the Doge's own conspiracy of 1355 made the Ten permanent" (§1.1) | `[T]` | `GM:345` says 20 July 1355; **the same file's verifier note, `GM:310`, orders "change '1339' to '1334 (commonly; some sources 1335)'"**, and the debate corpus records both (`proposals/2026-10-29-parliament-and-debate/2026-10-29-debate-corpus-by-theme_part3.md:428`, "permanent 1334/1355") | **CORRECTS**: the tree disagrees with itself; the correction (1334 or 1335, before Faliero) is the verified reading. The ratchet survives: what followed Faliero within days was the Ten's use against a Doge, not its permanence |
| V-2 | the *Serrata* fixed membership "to those who had sat in the previous four years and their descendants" (§1.3) | `[T]` | `GM:334` says that; the verifier note `GM:311` orders the removal of "whose fathers or grandfathers had already sat" and gives the 1297 text as confirming those who had sat in the preceding four years, balloted by the Forty (the note is cut off in the file) | **PARTIAL**: heredity is a later hardening, not the 1297 act. Design unaffected |
| V-3 | sons and brothers of a Doge barred from councils and benefices (§1.2) | `[M]` | — | **SILENT** |
| V-4 | the Doge "could not … leave the city, own property abroad, trade, accept gifts" (§1.2) | `[T; M for trade and gifts]` | `GM:326-328`: could not open correspondence, receive envoys or leave the palace unescorted without the Signoria's leave; no private correspondence abroad; no veto | **PARTIAL**: property abroad, trade and gifts stay memory-grade |
| V-5 | a quorum of councillors for a ducal act (§1.2) | `[M]` | `GM:320`: co-signature required; no number | **PARTIAL** |
| V-6 | Finlay's reading: the Doge ruled by being best informed (§1.2) | `[M]` | `CPS:306`: capstone rank without capstone power. `DPC:61` cites Finlay through a quotation and says "I did not open Finlay" | **SILENT** on the positive claim |
| V-7 | the Great Council numbered "1,000 to 2,500" (§1.3) | `[M]` | — | **SILENT** (a figure; a lead) |
| V-8 | refusal of office punished by fine or loss of eligibility (§1.3) | `[M]` | — | **SILENT** |
| V-9 | *commenda* and *colleganza* (§1.6, whole) | `[M]` | the word occurs nowhere in the tree. Nearest: the *ortoq* partnership, a portable concession with a profit share (`HCC:165`); the pledge of future yield (`HCC:148`); the loan against a named right (`HCC:161`; `CGR:190`) | **SILENT**; three analogues recorded. §5.2's choice of the fixed-amount form is unaffected |
| V-10 | the chain of ports; the *bailo* (§1.7) | `[M]` | `CGR:102`: the Stato da Mar under a **Provveditore Generale da Mar**, combined civil and military, against civilian Senate-audited rectors on the mainland; `CGR:103` Crete. No *bailo* | **PARTIAL**, and **CORRECTS** by addition: the sea state and the mainland were governed differently, by distance |
| V-11 | the rector: elected, "about two years", commission, "no local marriage, land or trade", dispatches (§1.7) | `[M]` with `[T]` X8 | `CGR:99`: fixed terms of **16, 24 or 36 months**; legislation "regularly forbade rectors from close, informal contact with their subjects"; `PHS:358`; `PMP:138` | **AGREES**, with the figure replaced by the tree's (a lead still). The written commission stays memory-grade |
| V-12 | travelling syndics hear subjects' complaints; the *relazione* read to the Senate (§1.7) | `[M]` | `PMP:119` (the 1566 commission; a cortège of about thirty; arrival proclaimed); `CGR:100`; `PMP:150-152` (the *relazione* as cumulative and inherited) | **AGREES**, and adds two things the audit lacked: the inspection is **theatre as well as audit**, and the report is **one document successive holders update** |
| V-13 | split authority, podestà and capitano (§1.7) | `[T]` X8 | `PMP:138-140`; `PGS:148`; `GPC:200`; and above them the *provveditori generali*, with the Avogaria able to suspend a rector's decision | **AGREES** |
| V-14 | Crete 1363, the revolt of St Titus (§1.7, §1.12, §12.4) | `[M]` | `CGR:103` gives the colonists' charter of 1211 and the two grades of grant; the revolt itself is not in the tree | **PARTIAL**: the settlers and their tenure are sourced, the revolt is not |
| V-15 | the merchant galleys auctioned by line (§1.7) | `[M]` | — (the scheduled convoy appears only for Spain, `HCC:140`) | **SILENT** |
| V-16 | the Arsenal: "16,000 … almost certainly a peak or an exaggeration; a few thousand is safer" (§1.8) | `[M]` | `CGR:91` (Davis): "at peak employed ~16,000 workers (arsenalotti) with a stable skilled core of ~2,000 backed by surge/unskilled labor — confirmed by multiple independent sources" | **CORRECTS**: the tree keeps both figures, a core of about 2,000 and a peak of about 16,000 |
| V-17 | the *arsenalotti* as the trusted guard (§1.8) | `[T]` | `PHS:342` (bodyguard duty); **`CPS:306`: Faliero's conspirators of 1355 were Arsenal men** | **CORRECTS** "only trusted armed body": trusted, and once the Doge's instrument against the class |
| V-18 | no patrician commands on land; captains hired; *provveditori* as commissaries (§1.9) | `[M]` | `PHS:358` (*provveditori* as civil-military overseers); `PHS:304` Carmagnola | **PARTIAL**: the rule against patrician command and the commissary's pay chest stay memory-grade |
| V-19 | Vettor Pisani tried, released at the crowd's demand (§1.9) | `[M]` | — | **SILENT** |
| V-20 | no fiefs or gifts from foreign princes (§1.9) | `[M]` | — | **SILENT** |
| V-21 | the three feeds of intelligence; the cipher office; the secretaries (§1.10) | `[M]` | `PMP:150-154` (the *relazione*; from 1480 an ambassador reporting to the Ten); `PMP:471-475` (the sealed channel); `PHS:362` (ambassadorial secretaries conducting the diplomacy); `GM:345` (informers, the lions' mouths). The cipher bureau in the tree is **Milan's**, under Simonetta (`CGR:112`) | **PARTIAL**: a Venetian cipher office stays memory-grade |
| V-22 | forced loans, the Monte, transferable shares, the Chioggia collapse (§1.11) | `[M]` | Venice: — . The shape elsewhere: the *juros* and the Habsburg suspensions as restructuring, not an end (`CGR:130`); Bardi and Peruzzi (`HCC:148`); the 1381 admissions "in exchange for war-loan contributions" (`CPS:310`) | **SILENT** for Venice; the public-debt shape is sourced from Spain |
| V-23 | the debt-bar (§1.11) | `[T]` | `PHS:382` | **AGREES** |
| V-24 | the sale of the roll, 1381 and 1646 to 1718 (§1.3) | `[T]` | `PHS:369`, `:371`; `CPS:310`; `RTP:503-506` | **AGREES**; `PHS:372` adds that the sale was opened only under a declared emergency |
| V-25 | the *specchio*; *veduto* and *seduto* (§2.1) | `[M]` | `DPC:57`: a drawn man is *veduto*, and *seduto* only if he clears the bars, "in tax arrears" among them | **AGREES** in substance; the word *specchio* is not in the tree |
| V-26 | the podestà's *sindacato* (§2.1) | `[M]` | `CGR:109`; `CGR:207`: the audit bills **the appointing faction**, not only the officer | **AGREES**, and adds appointer liability |
| V-27 | the *parlamento* with the square held by armed supporters (§2.2 step 2) | `[T; M]` | `GM:269`: the *balìa* "voted by a specially-convened parlamento"; the armed square is not there | **PARTIAL** |
| V-28 | the Eight given *balìa* powers; the Hundred of 1458 (§2.2 steps 6, 7) | `[T]` | `GM:269` has the Seventy (1480), the Otto di Pratica and the Dodici Procuratori; not the Eight's police powers, not the Hundred | **PARTIAL** |
| V-29 | the three ties; the specific favours (§2.3) | `[M]` | `GM:269` pillar 2 (dowries, debts, tax burdens); `PHS:283` (Kent: marriage alliances, debt forgiveness, dowry subsidies) | **AGREES** for the favours; the three named kinds of tie stay memory-grade |
| V-30 | "structure, not size": ties across groups that are not tied to each other (§2.3) | `[M]` | `RTP:68-71` (Padgett and Ansell 1993 cited: "capture the gate, not the seat"; reach across ladders; "multivocality is what makes capture durable"; its failure is one public exposure that ties the scattered edges into one scandal); `RTP:452-455` | **AGREES**; the marriage-against-business detail stays memory-grade |
| V-31 | the bank as a partnership of partnerships; the branch manager (§2.4) | `[M]` | `npc_roster_v30_infill:62` (archived): branch managers "semi-autonomously … practically an independent fiefdom run on personal relationships"; `CPS:252`: exile "did not touch the Medici bank's international correspondent network or its Florentine debtors" | **PARTIAL**: the legal separation of branches stays memory-grade |
| V-32 | the bill of exchange; dry exchange; deposits at discretion (§2.4) | `[M]` | — | **SILENT** |
| V-33 | Depositary General; the alum farm; excommunication for debt (§2.4) | `[M]` | — | **SILENT** |
| V-34 | how the bank failed: loans to princes (§2.4) | `[M]` | the shape is `HCC:148`: Edward III's default, the Peruzzi failing in 1343 and the Bardi in 1346, "Creditor Collapse" when exposure is concentrated | **AGREES** in shape; the Medici instances stay memory-grade |
| V-35 | the *catasto*; the Monte delle Doti (§2.5) | `[M]` | `GM:269` names the *catasto* as a burden the bank relieved; nothing more | **SILENT** |
| V-36 | sumptuary law (§2.5, under Florence) | `[M]` | `PGS:121` (F2): **Venice's** sumptuary magistracy, escalated 1476 to 1562, a standing office with fines and exemption petitions | **CORRECTS** the placement: the tree's instance is Venetian |
| V-37 | the *condotta*'s terms (§2.6) | `[M]` | `CGR:110`: a count of lances at a stipend, in phases, a binding *ferma* and a discounted *aspetto*; `CGR:208`, tier3 `:103`: *Ferma → Aspetto → Lapsed*, the reserve phase poachable, non-aggression after lapse | **AGREES**, with one correction of sense: in the tree the second phase is a **reserve at reduced pay in which the captain may be poached**, not only the employer's option |
| V-38 | the muster inspection; the captain's capital is his company (§2.6) | `[M]` | `pre_firearms…/05:480-484`: "a condottiere's company is his livelihood"; battle avoided for that reason. `HCC:67`: unpaid garrisons take plunder as wages (Antwerp 1576). `FASE:192-196` (Redlich): the army as a purchased instrument, paid whether or not it prospers | **AGREES** for the conflict; the *mostra* stays memory-grade |
| V-39 | Sforza; Carmagnola (§2.6) | `[T]` | `GM:285`; `PHS:304`; `CGR:111`; `RTP:340-343` (the marriage claim twice nearly dissolved by the employer) | **AGREES** |
| V-40 | the Pazzi "had just taken the papal account" (§2.7) | `[T; M]` | `CPS:257`: Sixtus IV "furious over Lorenzo's blocking of a Pazzi-financed papal land purchase at Imola" | **CORRECTS** the motive to the tree's; the account stays memory-grade |
| V-41 | "People and liberty"; "some eighty die"; the peace of Naples (§2.7) | `[M]` | `CPS:257`: the populace rallied at once; Salviati hanged in his vestments; interdict and the Pazzi War, 1478 to 1480; the Seventy | **PARTIAL** |
| V-42 | Savonarola: the interdict's threat to merchants' goods; a hostile Signoria drawn by lot (§2.8) | `[T; M]` | `CPS:277`, `RTP:539-542`: **two independent blows, both required**: excommunication (May 1497) and the failed trial by fire (7 April 1498); then a Signoria "he had never formally controlled" | **CORRECTS** the mechanism to the tree's two pillars; the merchants' goods and the lot stay memory-grade |
| V-43 | Genoa's Casa di San Giorgio (§2.9) | `[M]` | only a trace: the verifier note `GM:248` begins "(4) Casa di San Giorgio — REMOVE Chios from its administered colonie[s]" and the corrected body does not mention it | **SILENT** in the body; a lead |
| V-44 | the Hanse's constitution: the diet, bound envoys, thirds (§3) | `[M]` | — | **SILENT** |
| V-45 | the Kontor (§3) | `[M]` with `[T]` O7 | `PGS:78`: own treasury, law and seal; alderman elected or appointed; **the host loses jurisdiction over its members**; `PGS:23` | **AGREES** |
| V-46 | withdrawal: "Bruges 1358 and 1388; Norway 1284"; *Verhansung* of a member town (§3) | `[M]` | `FASE:119`: "the blockades of Bruges (1358, 1451–57)"; `HCC:55` (Novgorod closed, 1494), `:160` (the Steelyard, 1598) | **CORRECTS** the dates to the tree's; 1388 and 1284 stay leads. `FASE:119` uses *Verhansung* for the collective embargo; the audit's sense (expulsion of a member) is memory-grade |
| V-47 | Greif, Milgrom and Weingast: the guild as the ruler's commitment device (§3) | `[M]` | Greif is cited in the tree only for self-enforcing institutions (`.audit/2026-07-01-contest-gate-c-packet/GATE_C_packet.md:354`) | **SILENT** on this argument |
| V-48 | the *Pfundzoll*, Cologne, Stralsund (§3) | `[M]` | — | **SILENT** |
| V-49 | the local guild's constitution (§3) | `[M]` | `CGR:97` (Venetian guilds elect their own officers; no statute takes force without the Giustizia Vecchia); `CGR:116` (the Arte della Lana as supply-chain controller); `CGR:117` (the Mercanzia, a guild-funded merchant court with its own enforcement); `PGS:77` (consuls by lot for four months); `CGR:129` (*gremios*) | **AGREES**, and adds three mechanisms the audit lacked (§4) |
| V-50 | Nulls: "no shipped game" models a debt as the debtor's undertaking, or capture at a roll (§15) | lane's own | `GPS/THROUGHLINES:79` (P14: CK3 hooks, Suzerain's broken promise, Jagged Alliance 2's term contract; the suite's verdict on the engine is PARTIAL); `GPS/tables/R8:81-110` (Patrician IV: a Hanse trader's ladder to alderman by wealth, ships and counting houses; council by proposal; loans at the tavern, `R8:89`); `GPS/tutorials/T14:228`, `:281-313` (The Guild: titles bought, offices elected); `GPC_part6:165-175` (John Company) | **PARTIAL**: the null holds for the debt and for capture at the roll; it was stated without the suite having been opened, and three games do model the trader's and the guildsman's ladder |

### 2.2 Colonial lane (`audits/15_INSTITUTIONS_COLONIAL.md`)

| id | the audit's claim (section) | its mark | the tree's source | verdict |
|---|---|---|---|---|
| C-1 | "the tree holds no research file on the chartered companies, the Spanish Indies beyond the residencia, settler colonies, indirect rule … or the Mongol system" (§2 head; E-2) | lane's own | §0 item 2 above | **CORRECTS** |
| C-2 | the fief: homage, relief, aid, forfeiture (§2.1 answer 2) | `[MEMORY]` | the contract in its Kamakura form, `PHS:457-458`: the lord's favour is either **confirmation of what the vassal holds** or **a new grant**, against service; `GM:154` (Quierzy 877 concedes heritable office); `GM:170` (the general oath); `FASE:138` (privileges confirmed at accession, for a fee); `PW:47` (the levy's fixed term) | **PARTIAL**: relief and aid by those names stay memory-grade; the tree adds the lord's **duty to reward**, which the audit lacked |
| C-3 | "the vassal of my vassal is not my vassal" (§2.1) | `[MEMORY]` | — (the engine's own rule, `state/gate.py:432-439`) | **SILENT** |
| C-4 | the marcher lord (§2.1) | `[TREE: T8]` | `FASE:157`; `PGS:106` (the Warden's "black-rent", found only by inquiry; the Days of Truce) | **AGREES** |
| C-5 | the chartered company, the whole paragraph (§2.1) | `[MEMORY]` | monopoly by charter and the powers of a state: `CGR:134` (the licensing bureau and the self-governing merchant body are **two** institutions); `HCC:163` (a repudiated compact made the VOC's conquest lawful in its own eyes and installed a Company governor over the native elite); `HCC:166` (the company takes the revenue grant, then demotes the bankers who financed it); `PGS:147` (the sovereign subordinates the company's councils to one another by class of decision); `PGS:84` (the privilege is portable, and moving it is the leverage); `HCC:54` (unlicensed traffic seized); `GPC_part7:41` (the Company can fail while its officers win) | **PARTIAL**: directors and shareholders, factories, private trade and renewal fights stay memory-grade |
| C-6 | Roman client kings (§2.1 answer 3) | `[MEMORY]` | `PHS:125`, `:144` | **AGREES** |
| C-7 | the Mongol patent, tribute through the prince, the overseer, the census, bidding at court (§2.1) | `[MEMORY]` | the appanage and the rival assembly (`HCC:46`); the *ortoq* and the *paiza* (`HCC:165`); the marriage alliance as tribute (`RTP:185-188`); the keshig as hostage and school (`RTP:360-363`) | **SILENT** on the patent system; four adjacent Mongol mechanisms sourced |
| C-8 | Ragusa and the Danegeld (§2.1) | `[TREE: T10]` | `FASE:176`; `HCC:56` (with no defence banked, only compliance is open), `:167` (tribute withheld, then the sack) | **AGREES** |
| C-9 | the resident, the subsidiary treaty, lapse (§2.1) | `[MEMORY]` | — | **SILENT** |
| C-10 | hostage-kin; sons raised at the overlord's court (§2.1) | `[TREE]`; `[MEMORY]` | `PMP:132`, `:502-506` (the **cost** is the mechanism: two establishments and the processions); `PHS:144`; `HCC:43` (heirs kept at court against heirs left as governors); `RTP:360-363`; `faction_politics_v30:123-131` (archived) | **AGREES** |
| C-11 | venality: the *paulette* (§2.1 answer 1) | `[TREE: T2, T5]` | `FASE:101`, `:130`; `RTP:488-491`; `CGR:132`; **`RTP:518-521`: colonial offices cheaper the farther from the capital, and the same distance weakens the audit; the buyer seats an ally on the reviewing bench** | **AGREES**, and adds distance in the price and in the audit |
| C-12 | *mita*, *repartimiento*, corvée, *encomienda* (§2.2) | `[MEMORY]` | `PGS:95` (T2): the mit'a pooled rotational labour and "was reciprocal": it writes a debt owed back, not a flat grievance; `PGS:127` (F8, the *devshirme* as levy of persons). *Encomienda* and *repartimiento*: — . Nearest: revenue without governance, `CGR:160` (pronoia), `PGS:101` (timar) | **PARTIAL**, and **CORRECTS** the framing: the tree's labour draft carries a return |
| C-13 | settler societies; the charter dispute (§2.3) | `[MEMORY]` | `HCC:71` (billeting by force narrows the governor's own later choices: 1765 to 1774); `HCC:138` (the far colony that would not adopt local practice and was let go); `CGR:103` (colonists by charter, a rooted militia under a rotating governor); `PGS:107` (one charter for every town founded under it: revoke one and all are shaken); `PGS:85` (an order founds and rules its own settlement); `RTP:574-577` (franchise by church membership) | **PARTIAL**: headright and the assemblies stay memory-grade |
| C-14 | soldier-settlers (§2.3) | `[TREE: T8]` | `FASE:152-159`; `PGS:104-105`, `:108` (a permanent defence that can turn to refusal) | **AGREES** |
| C-15 | conquest terms and the entry (§2.4) | `[TREE: T6]` | `FASE:134-140`; `CGR:94` (*dedizione*); `PMP:508-511`; `PA:195`, `:222-230` (inherit, replace or transform the previous ruler's machinery) | **AGREES** |
| C-16 | royal patronage; the mission; the protecting orders (§2.5) | `[MEMORY]` | `PW:143` (the papal grant dividing new lands); `CGR:188` (banking chapter seats before a vacancy) | **SILENT** on the mission |
| C-17 | the Mongol and Ottoman successions (§2.6) | `[MEMORY; TREE: T9]` | `HCC:42` (sparing claimants seeds the next claim; fratricide trades civil war for assassination), `:46` | **AGREES** |
| C-18 | distance: transit times; the man on the spot; "I obey but do not execute" (§2.7) | `[MEMORY]` | `PMP:491-494` (P33): **a decree lands in each locality by a compliance roll "against its own disposition, distance, and the presence of an enforcing agent"**, grounded on the capitularies that re-prohibit the same abuse (`PMP:136`); `PMP:661`: "the gap between the envoy's discretion and his instructions is the component's central tension"; `PGS:94-99` (relay, post, beacon); `PGS:294`: latency "presumes a game concept that may not exist"; `CGR:102` (far provinces get a combined civil-military governor, near ones a civilian under oversight) | **PARTIAL**: no transit time in the tree and no formula; **the tree states the lane's own mechanism** (§3.2's `remove`) and adds a term the lane lacks, the enforcing agent present |
| C-19 | "`staple` … company monopoly, the staple port" (§4.3) | `[MEMORY]` | `PGS:123` (F4, the Lübeck staple right: granted once, administered by the town); `PGS:84` | **AGREES** |
| C-20 | "`land_grant` … military colony, headright" (§4.3) | `[TREE T8; MEMORY]` | `CGR:103`; `PGS:107` | **AGREES** but for headright |
| C-21 | `prescription_seasons` first value 8 (§6.2) | lane's own number | `settlement_layer_v30:621-625` (archived): revocation obstacle rises by `floor(charter_age_seasons / 8)`; public contest past about sixteen seasons; `:642-644` calls both uncalibrated | **AGREES**: the lane's first value and its sweep {4, 8, 16} reproduce the archived design's, which is intent and not authority |
| C-22 | "the tree names no shipped game that models an audit at the end of a governor's term … none that makes a charter's age evidence" (§15) | `[UNVERIFIED]` | `GPC_part5:240-244` concedes the conquest-terms and governance verdicts rest on history, not on a game; John Company is the nearest for office under a charter | **AGREES**: the null holds, now checked |
| C-23 | per-settlement Legitimacy, suspicion, `governor_emergence` "did not transfer" (§15) | `[TREE]` | `proposals/2026-09-10-…/05_COLLISIONS_AND_RESIDUE.md:20-36`, `:76-84` reaches the same refusals independently and re-expresses each on the same primitives | **AGREES**, with a precedent the lane did not cite |

## 3. What remains memory-grade after this pass

**Venice family.** The *commenda* and *colleganza* (V-9); the sea loan; the merchant galleys and their
auction (V-15); the Monte and forced loans at Venice and Florence (V-22, V-35); the bill of exchange, dry
exchange, discretionary deposits, the papal depositary and the alum farm (V-32, V-33); the Medici branches'
legal form and their particular bad debts (V-31, V-34); the *catasto*'s working and the dowry fund (V-35);
the muster inspection (V-38); the ban on patrician land command and on foreign fiefs (V-18, V-20); Pisani
(V-19); the Doge's family bars, the refusal fine, the Council's size, the quorum (V-3, V-5, V-7, V-8); a
Venetian cipher office (V-21); the armed *parlamento*, the Eight, the Hundred (V-27, V-28); the Pazzi
day's particulars (V-41); the interdict's bite on merchants' goods (V-42); San Giorgio (V-43); the Hanse's
diet, thirds, bound envoys, war levy, Stralsund, and the expulsion of a member town (V-44, V-46, V-48);
the commitment-device argument (V-47); the revolt of St Titus (V-14). **Every one is a shape the design
uses or a figure it does not; none carries a number in the design.**

**Colonial family.** The English and Dutch companies' internal constitution (C-5); the Mongol patent,
census and overseer (C-7); the resident, the subsidiary treaty and lapse (C-9); *encomienda* and
*repartimiento* (C-12); headright and the colonial assemblies (C-13); the mission, royal patronage over a
colonial church and the protecting orders (C-16); relief and aid by name, and the rule that a vassal's
vassal is not the lord's (C-2, C-3); transit times and "I obey but do not execute" (C-18).

**Why this matters less than the list's length suggests.** For both families the design's load-bearing
shapes are now sourced in the tree: rotation, the audit at exit, the roll, the lot, the secret ballot,
withdrawal, the loan to a prince and its default, the contract captain, the charter that hardens, the
farm, tribute at both poles, hostage-kin, the settler under a rotating governor, the company that governs,
and the decree that lands by a roll. What stays memory-grade is detail inside those shapes.

## 4. Mechanisms the research describes that the two designs did not carry

Each is written as an executable edit in the grounding proposal named. None adds a carrier type.

| # | mechanism | source | family | carried by |
|---|---|---|---|---|
| M-1 | **Two officers over one subject place**, with disjoint remits, each reporting separately; neither can defect alone | `PMP:138-140`, `:513-516`; `PGS:148`; `CGR:99` | both | `proposals/15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds.md` edit 1 |
| M-2 | **Near places split, far places combined**: a civilian under oversight where the centre is close, a combined civil-military governor where it is not | `CGR:102` | both | VENICE grounding edit 1; `proposals/15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds.md` edit 6 |
| M-3 | **The submission pact**: a subject place keeps its own councils and courts by a negotiated instrument; a cap won in mid-tenure binds the superior | `CGR:94`; `PMP:508-511`; tier3 `:147` (play found its cut wrong four times) | both | VENICE grounding edit 2 (a `capitulation` held by the commune) |
| M-4 | **Appointer liability**: a governor's condemned term is a deed against whoever appointed him | `CGR:109`, `:207`; tier3 `:101` | both | VENICE grounding edit 3 |
| M-5 | **The inspection as theatre**: its effect on the governed's regard is separate from what it finds | `PMP:119`, `:465-469`, `:641` | both | VENICE grounding edit 3 (a reading, no rule) |
| M-6 | **The standing report**: one document about a place, updated by each outgoing holder, held, stolen, forged | `PMP:150-152`, `:459-463`; `CGR:100` | Venice | VENICE grounding edit 4 |
| M-7 | **The capped second order**: citizens barred from the councils who hold the secretary seats for life and draft what rotating nobles sign | `PHS:362`; `CGR:96` | Venice | VENICE grounding edit 4 |
| M-8 | **The contract in phases**: bound, then in reserve at reduced pay and open to offers, then lapsed under a term of non-aggression | `CGR:110`, `:208`; tier3 `:103` | Venice | VENICE grounding edit 5 (a form `condotta`) |
| M-9 | **Arrears turn on the host**: unpaid men take their wages from the place that lodges them, and every place that hears of it trusts garrisons less | `HCC:67`; `HCC` §4 `:264`, `:300` | both | VENICE grounding edit 5 (a reading) |
| M-10 | **The pledge**: a loan secured on a named right; the lender holds the right's instrument until paid | `HCC:161`; `CGR:190`; tier3 `:95` | Venice | VENICE grounding edit 6 |
| M-11 | **The merchants' own court**: a bench of the guild beside the commune's, so that a suit has a forum to choose | `CGR:117`; `GM:201-202` (two courts, one question) | Venice | VENICE grounding edit 6 |
| M-12 | **Statutes need a magistrate's assent**: a guild rules itself, and no rule of its own takes force outside it until one outside office passes it | `CGR:97`, `:129`, `:223` | Venice | VENICE grounding edit 7 (composed: the guild's `petition` to a commune seat) |
| M-13 | **The body of the excluded**: a brotherhood with its own ladder for those the roll shuts out | `CGR:98`; `PGS:81` | Venice | VENICE grounding edit 7 (content) |
| M-14 | **Portability as leverage**: a privileged body's threat to carry its privilege to a rival host | `PGS:84` | both | COLONIAL grounding edit 5 |
| M-15 | **The decree's bearer**: an order's odds improve with an enforcing agent of the issuer present at the addressee's place | `PMP:491-494` | Colonial | COLONIAL grounding edit 1 |
| M-16 | **Assessment as a resisted act**, and the gap between the figure on the record and the store on the ground as what an audit samples | `PMP:485-489`, `:641`; `05_COLLISIONS_AND_RESIDUE.md:32` (the grammar gap this needs) | Colonial | COLONIAL grounding edit 2 |
| M-17 | **Distance in the audit and in the price of an office**; the officer's man on the bench | `RTP:518-521`, `:483-486` | Colonial | COLONIAL grounding edit 2 |
| M-18 | **The lord's duty to reward**: service answered and nothing granted breaks the bond from the lord's side; a war that wins no ground cannot pay its victors | `PHS:457-461`; `CPS` Japan 3.2 | Colonial | COLONIAL grounding edit 3 (a second `due` on `homage`) |
| M-19 | **The hostage as pupil, and the cost as the mechanism**: the ward serves in the host's household and returns the host's man; the sender pays for two establishments | `RTP:360-363`; `PMP:502-506`; `HCC:43` | Colonial | COLONIAL grounding edit 4 |
| M-20 | **The labour draft owes a return** | `PGS:95` | Colonial | COLONIAL grounding edit 7 (bears on §11 item 3 only) |
| M-21 | **Revenue without governance**: a named community's dues assigned to a holder who does not rule it, for service | `CGR:160`; `PGS:101` | Colonial | COLONIAL grounding edit 5 (the `farm` row without its seat) |
| M-22 | **The life farm hardens**: reclaimed early it is an act of administration, late it is a revolt | `RTP:523-526`; `FASE:101` | Colonial | COLONIAL grounding edit 5 |
| M-23 | **The company under a superior by class of decision**; the licensing office and the merchant body as two seats | `PGS:147`; `CGR:134`; `GPC_part6:165-175` | Colonial | COLONIAL grounding edit 5 |
| M-24 | **Invited entry**: a party to a civil quarrel brings the outside power in; a failing commune gives itself to a foreign lord | `PA:64-98`; `GM:290-291`; `CPS:267-268` | both | COLONIAL grounding edit 8 (a story and its reading) |
| M-25 | **Billeting ratchets**: lodging troops by force lowers regard and narrows the governor's later choices | `HCC:71`; compendium `43:47-55` | Colonial | COLONIAL grounding edit 8 |
| M-26 | **The post let go**: a far place that adapts to its ground loses the centre's regard, and a centre that stops paying loses the place by lapse | `HCC:138` | Colonial | COLONIAL grounding edit 8 |
| M-27 | **Certainty of detection against severity of sanction** as two dials | `PMP:142-144`, `:496-500` | both | COLONIAL grounding edit 2 (a sweep, no rule) |
| M-28 | **The privilege with a patron**: a grant that stands only while a named backer does | `settlement_layer_v30:646-669` (archived; ED-SE-0021) | both | COLONIAL grounding edit 5 |

**Tried and not taken** (the research describes it; the design has a reason): a per-verb authority table
for the territory (`PGS:148`): the two officers' disjoint `remit_acts` already are that table; a relay or
beacon tier (`PGS:94`, `:99`): the tree's own caveat at `PGS:294`, and the colonial lane's §3.3; a stored
"New-Money" tag on a purchased house (`RTP:504`): a stored social quantity, which Layer 1 refuses;
`marriage_registered` (`RTP:205-207`): the Venice lane's resolution 12 stands; a debasement posture
(`HCC:146-155`): no coin exists to debase; the composite standing score (`PHS:387-388`): the Venice
lane's §15 stands; five new tag families (`PGS:296` doubts them itself).
