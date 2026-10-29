# Candidates not read — and why

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-10-28 · Lane: IN (cross-cutting) · Written against `15593ac`
## What changes in `engine/season/`: nothing. If this directory were deleted the game would behave identically.

**Why this file exists.** A literature corpus is only as honest as its list of what it did *not* read. Every
source below was a candidate, was attempted or deliberately skipped, and is **not** in the read entries
(`01`–`06`). Nothing here has a thesis, argument or apparatus attached, and nothing in `07_apparatus.md`
rests on it. Where an earlier survey made a claim about one of these, the claim is **unverified**, not
refuted.

## A. Attempted and blocked

| source | what stopped it | consequence |
|---|---|---|
| Sych (2023), *Worlds At Play: Criticality Between Players and Game Designers*, Concordia MDes thesis | `spectrum.library.concordia.ca` answers 403 to scripted clients. The built-in browser reached it, but the server returned a **file download**, so a save dialog was shown to the user and no file landed in the working area. | The thesis is **not re-read**. Claims attributed to it in earlier notes (storytelling partnership, generative friction, the game *MENU NEW GAME+*) are carried as *unverified*. Sych's 2020 paper (`E02`) is read in full. If the PDF is saved locally it can be added as one more entry. |
| James Ryan (2018), *Curating Simulated Storyworlds*, UC Santa Cruz PhD thesis | `escholarship.org` returns HTTP 202 with an empty body to non-browser clients on every attempt (a bot-challenge pattern); not worked around. | Covered only at second hand by Emily Short's three-part reading (`E12bcd`, tag `S`). Ryan's own arguments are reported *as Short reports them*. |
| Tanenbaum & Tanenbaum (2009), "Commitment to Meaning: A Reframing of Agency in Games" | Same `escholarship.org` wall. A different DiGRA article ("Toward an Agential Realist Account of Digital Games") was downloaded by mistake, recognised from its first line and discarded. | Agency is covered by `T08` (Wardrip-Fruin et al.) and `T10`; the Tanenbaum reframing is absent. |
| Compton, Kybartas & Mateas (2015), "Tracery" (ICIDS 2015) | The TU Delft host did not connect from this machine. | The generative-grammar side of procedural text is represented by `E15` (Qud) only. |
| Kybartas, Verbrugge & Lessard (2018), expressive-range poster (ICIDS 2018) | `www.sable.mcgill.ca` did not connect. | The 2020 journal expansion (`E05`) is read; the poster is not. |
| Ryan, Mateas & Wardrip-Fruin (2015), "Open Design Challenges for Interactive Emergent Narrative" | `users.soe.ucsc.edu` did not connect; Springer copy is paywalled. | The four design challenges (modular content, compositional representation, story recognition, story support) are known here only from an abstract and from `E12bcd`. |
| Przybylski, Rigby & Ryan (2010), "A Motivational Model of Video Game Engagement" | Publisher page restricted; mirror returned 403. | The 2006 paper (`G01`) stands in for self-determination theory. |
| Khaled, Nelson & Barr (2013), "Design Metaphors for Procedural Content Generation in Games" (CHI) | No open full text found (abstract page only). | `P04` (Smith 2014) and `P03` (Togelius et al.) carry the design-side PCG framing. |
| Evans & Short (2014), "Versu — A Simulationist Storytelling System" (IEEE TCIAIG) | IEEE paywall; no open copy found. | The social-practices approach to agent-driven drama is unread. |
| Sengers (1999), "Designing Comprehensible Agents" (IJCAI) | Only an abstract record found. | Legibility of agent behaviour is covered indirectly (`T03a/b`, `P01`, `T13`). |

## B. Talks with no usable transcript

GDC Vault was in maintenance during this work and most of these exist only as video; none was read.

- Jon Ingold, "Narrative Sorcery: Coherent Storytelling in an Open World" (GDC 2017) — the inkle/Heaven's Vault method of condition-gated content.
- Elan Ruskin, "AI-driven Dynamic Dialog through Fuzzy Pattern Matching" (GDC 2012) — Valve's rule-matching dialogue.
- Ken Levine, "Narrative Legos" (GDC 2014).
- Tynan Sylvester, RimWorld talks (GDC 2017) and the book *Designing Games* (2013). Only two **secondary** news pieces about his ideas were read (`G13`, `G14`).
- Justin Keenan on micro-reactivity in *Disco Elysium* (GDC 2021).
- Chris Hoge on the Nemesis system (GDC 2018) and Michael de Plater on the Nemesis design (GDC 2015).

## C. Books and long works not read

Murray, *Hamlet on the Holodeck* (1997) · Wardrip-Fruin, *Expressive Processing* (2009; only the 2008 chapter `T13` is read) ·
Short & Adams (eds.), *Procedural Storytelling in Game Design* (2019) · Salen & Zimmerman, *Rules of Play* (2003) ·
Koster, *A Theory of Fun* · Bateman, *Game Writing* · Schell, *The Art of Game Design* · Sylvester, *Designing Games*.

## D. Named candidates not attempted

Named so that a gap is not mistaken for a verdict that the work is unimportant. Each is a plausible next
addition if an apparatus question needs it:

- **Narrative AI / drama management:** Riedl & Young (2010) narrative planning; Thue et al. (2007) PaSSAGE player-modelling; Magerko (2005) *Story representation and interactive drama*; Szilas (2003) IDtension; Louchart, Swartjes, Kriegel & Aylett (2008) *Purposeful authoring for emergent narrative*; Walsh (2011) "Emergent narrative in interactive media" (*Narrative*, paywalled); Kybartas & Bidarra (2017) story-generation survey.
- **Social simulation as story engine:** McCoy et al. (2014) *Comme il Faut*; Samuel et al. (2018) *Ensemble*; Horswill's work on story sifting at scale and constraint-based generation.
- **PCG:** Yannakakis & Togelius (2011) experience-driven PCG; Hendrikx et al. (2013) and Summerville et al. (2018) surveys; Dormans (2012) *Engineering Emergence*; Sullivan (2012) *The Grail Framework*.
- **Engagement and craft:** Sweetser & Wyeth (2005) GameFlow; Brown & Cairns (2004) and Jennett et al. (2008) on immersion; Green & Brock (2000) narrative transportation; Schønau-Fog & Bjørner (2012); Lazzaro (2004) *Why we play games*; Zimmerman (2004) and Aarseth (2004) in *First Person*; Costikyan (1994); Church (1999) *Formal Abstract Design Tools*.
- **Claims about named games** (*Disco Elysium*, *Planescape: Torment*, *Crusader Kings*, *Wildermyth*, *Shadow of Mordor*) in earlier notes were drawn from web-search excerpts and **were not re-verified here**.
