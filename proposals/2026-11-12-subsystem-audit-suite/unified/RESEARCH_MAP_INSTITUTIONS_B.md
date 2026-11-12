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
   grep was over `research/` alone. True as far as it goes for the East India companies, for settler
   colonies of the Atlantic kind, for indirect rule in Africa and India, and for the Mongol patent system:
   §3 below records each as still memory-grade, with the lines that come nearest. False for four things
   the lane called `[MEMORY]`: the chartered monopoly company (the Casa de Contratación and the Consulado
   de Sevilla, `comparative_governance_research_v1.md:134`; the Merchant Adventurers, the Hanseatic Kontor
   and the Fugger house as branch organisations, `research/proactive_governance_scale_research_v1.md`
   O5, O7, O13); venality in the Spanish monarchy (`comparative_governance_research_v1.md:132`); the
   military-colonist charter (Venetian Crete's *Carta Concessionis*, `:103`); and public debt with
   scripted default (the *juros* and the Habsburg suspensions, `:130`).
3. **Both lanes: "the digests were not opened; the research was read directly."** The digests were not
   needed; the `.audit/` compendium and the 2026-10-29 debate corpus were, and neither lane opened them.

The body below is appended as the reading proceeds: §1 the file list by institution; §2 the claim-by-claim
table for the two audits (claim, the audit's mark, the tree's source at path:line, and whether the source
agrees, corrects or is silent); §3 what remains memory-grade; §4 mechanisms the research describes that
the two designs did not carry.
