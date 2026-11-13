# Grounding note: casualties, duration and what decides a pre-gunpowder battle

## Status: FILED — reference, tier 3 (`research/00_INDEX.md` §1) · not canon (CLAUDE.md §0.05) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: MB (historical adjudication lane of `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

**Why this note exists.** Jordan, 2026-11-12: *"Refer to historical battles and military academic works … for
mass battle, regarding how it should be functioning re movement and behaviours and results"*, with *"All
ungrounded information should have info available on repository"* and *"Do not guess."* The tree's own
battle research (`research/pre_firearms_formations/`, 17 files) is written from memory and self-checked
(`13_verification_corrections.md:5`, `:275`), and the one sourced note
(`research/historical/mass_battle_gauge_grounding.md`) cites works by DOI without recording that any page was
read. This note records what a page read establishes about **results**: who loses how many, when, and how long
a battle takes. Its siblings (same date, same lane) cover movement and behaviour, manoeuvre sequences, and
wargame models.

**Tiers used in all four notes.**

| tag | meaning |
|---|---|
| `[D]` | **read directly by this lane**: the page images of the publication were opened and read in full (the scanned PDF, every page). The strongest tier here. |
| `[T url]` | **page fetched and read through the fetch tool** on 2026-11-12: the page body was retrieved and a small model answered a stated question over it. Quotations and figures are as the tool returned them; this lane did not see the raw page. Where the tool reported that it read only the first 100,000 characters of a longer page, the row says `(part)`. Treat a `[T]` figure as a page-read lead: stronger than a snippet, weaker than `[D]`. |
| `[S]` | search-result snippet only. A lead; never a figure to build on. |
| `[M]` | memory. Not used for any figure in these notes. Where only memory was available the cell says **not established**. |

## Sources

| key | source | what it is | tier · read |
|---|---|---|---|
| KR | Peter Krentz, "Casualties in Hoplite Battles", *Greek, Roman and Byzantine Studies* 26:1 (1985) 13–20. `https://grbs.library.duke.edu/article/viewFile/5321/5325` | peer-reviewed article; a table of 17 set battles, 472–371 BC, from Thucydides, Xenophon, Diodorus | `[D]` all 8 pages, 2026-11-12 |
| SA | Philip Sabin, "The Face of Roman Battle", *Journal of Roman Studies* 90 (2000) 1–17. Copy at `https://www.gwern.net/doc/history/2000-sabin.pdf` (a JSTOR scan) | peer-reviewed article; the model of Roman infantry combat as a stand-off with flurries | `[D]` all 17 pages, 2026-11-12 |
| DP | Ardant du Picq, *Battle Studies: Ancient and Modern Battle* (trans. Greely and Cotton, 1921), Project Gutenberg #7294, `https://www.gutenberg.org/cache/epub/7294/pg7294.txt` | primary theoretical work (a French officer, d. 1870) | `[T]` characters 0–200,000 of 500,828 (Part I chapters I–VI and the start of Part II), 2026-11-12 |
| CL | Carl von Clausewitz, *On War* (trans. Graham), Project Gutenberg #1946, `https://www.gutenberg.org/cache/epub/1946/pg1946.txt` | primary theoretical work (1832) | `[T]` characters 160,000–300,000 (Book I ch. III–VIII, Book II ch. I–V) and 500,000–700,000 (Book IV ch. IV–XIV, Book V ch. I–VI) of 1,733,282, 2026-11-12. Book VII (the culminating point) **not read** |
| W-CAN | `https://en.wikipedia.org/wiki/Battle_of_Cannae` | encyclopedia article citing Polybius, Livy, Daly, Clodfelter | `[T]` (part: first 100,000 of 143,535 characters) |
| W-HAS | `https://en.wikipedia.org/wiki/Battle_of_Hastings` | encyclopedia article citing Gravett, Lawson, Marren, Bennett | `[T]` (part: first 100,000 of 127,142) |
| W-AGI | `https://en.wikipedia.org/wiki/Battle_of_Agincourt` | encyclopedia article citing Curry, Barker, Sumption, Rogers, Keegan | `[T]` (part: first 100,000 of 153,320) |
| W-PHA | `https://en.wikipedia.org/wiki/Battle_of_Pharsalus` | encyclopedia article citing Caesar, Appian, Goldsworthy, Delbrück, Greenhalgh | `[T]` |
| W-ZAM | `https://en.wikipedia.org/wiki/Battle_of_Zama` | encyclopedia article citing Polybius, Goldsworthy, Taylor, Hoyos | `[T]` (part: first 100,000 of 152,213) |
| W-GS | `https://en.wikipedia.org/wiki/Battle_of_the_Golden_Spurs` | encyclopedia article citing Verbruggen, Rogers, Tucker, the Annals of Ghent | `[T]` |
| W-ARS | `https://en.wikipedia.org/wiki/Battle_of_Arsuf` | encyclopedia article citing Oman, Boas, the *Itinerarium*, Baha al-Din | `[T]` |
| W-KAL | `https://en.wikipedia.org/wiki/Battle_of_the_Kalka_River` | encyclopedia article citing Gabriel, de Hartog, Khrustalev, Fennell | `[T]` |
| W-LAN | `https://en.wikipedia.org/wiki/Lanchester%27s_laws` | encyclopedia article | `[T]` |
| ACOUP | Bret Devereaux, "Intermission: Battle Pulses", *A Collection of Unmitigated Pedantry*, 2025-12-18, `https://acoup.blog/2025/12/18/intermission-battle-pulses/` | an academic historian's essay criticising the pulse model | `[T]` |

**Sought and not reached** (so nothing below rests on them): Hans Delbrück, *History of the Art of War*; Charles
Oman, *A History of the Art of War in the Middle Ages*; John Keegan, *The Face of Battle* (known here only
through Sabin's quotations of it, SA p. 17); Trevor Dupuy, *Numbers, Predictions and War* and *Understanding
War*; Adrian Goldsworthy, *The Roman Army at War* (known only through Sabin); Victor Davis Hanson, *The Western
Way of War*; Helmbold's casualty studies (one sentence on the Lanchester page only). `clausewitz.com` returned
HTTP 403 for three chapter pages. A US Army Heritage Center "Marching Rates" bibliography returned 404.

## What is established

### A. How much each side loses

| # | claim | tier |
|---|---|---|
| A1 | In 17 set hoplite battles between 472 and 371 BC for which figures survive, "The defeated army rarely lost more than 20%: typical is 10–20%, the average approximately 14%. The winning side never lost more than 10%: typical is 3–10%, the average approximately 5%." Average ratio of winner's to loser's losses 1 : 2.9 (range 1 : 1.7 to 1 : 5.2). | `[D]` KR pp. 18–19 (table p. 19) |
| A2 | The table's rows (winner / loser, as a share of those engaged): Acragas 10% / 20%; Potidaea 5% / 15.8%; Olpae 5% / 16.7%; Solygea 2.5% / 12.1%; Delium 7.1% / 14.3%; Mantinea (418) 3.3% / 13.8%; Syracuse (415) 2% / 5.2%; Naryx 8.3% / 16.7%; Nemea River 4.9% / 11.7%; Coronea 1.7% / 3%; Leuctra 5% / 10%. Loser only: Syracuse (413, a night battle) 20–25%; Miletus 20%; Ephesus 10%. | `[D]` KR p. 19 |
| A3 | Krentz's own caution: "Estimates are involved in a number of places, and the results should not be taken as precise." The two low outliers have named causes: at Syracuse (415) a thunderstorm and "pursuit was prevented by the unchallenged Syracusan cavalry"; at Coronea one wing "did not even come to blows". | `[D]` KR pp. 18–19 |
| A4 | Why hoplite losers lost so little: "the Greeks … did not usually pursue far once a battle was decided. This reluctance … stemmed as much from the fear of a reversal if the troops dispersed as from a gentlemanly hesitation to kill fellow Greeks; but it did mean that the losers' losses, while twice or three times as heavy as those of the winners, were rarely more than a fifth of their engaged forces." | `[D]` KR p. 20 |
| A5 | Roman battles: victors "around 5 per cent" in the Punic Wars on Polybius's figures, "the same as for the winners in Greek hoplite clashes", and lighter still later ("only 700 dead at Cynoscephalae, 350 at Magnesia, 100 at Pydna, 230 at Pharsalus, and 1,000 at Munda"). Sabin adds: "Clearly these figures need to be taken with a pinch of salt". | `[D]` SA pp. 5–6 |
| A6 | Roman battles: losers "were frequently far heavier, with over half the defeated army often being killed or taken prisoner according to our sources" (Zama: 20,000 dead and almost as many captured; Cynoscephalae: 8,000 killed and 5,000 prisoners of 25,500). | `[D]` SA p. 5 |
| A7 | The cause of the difference between A1 and A6 is **what happens after one side breaks**, not the fighting: hoplite victors "were hard pressed to catch fleeing adversaries who had thrown away their heavy shields"; after Roman battles "defeated troops sometimes found themselves encircled and incapable of flight (as at Cannae), while others were subjected to a drawn-out pursuit … in which they were mercilessly slaughtered from behind by faster enemy cavalry". | `[D]` SA p. 5 |
| A8 | Two models of where the loser's dead fall, "two ends of a spectrum": either one side is "killed without being able to make effective reply" during the fighting (the encircled, Cannae), or "*both* sides suffered relatively limited overall casualties before the rout, with the real danger for the losing troops … coming only *after* they turned and fled." "Different clashes could fit virtually anywhere along that spectrum." | `[D]` SA p. 6 |
| A9 | A symmetric long fight exists and is not a rout: at Ilerda, five hours, Caesar's cohorts "70 dead and 600 wounded, compared to 200 killed" on the other side; at Jotapata an all-day sortie, 13 Roman dead against 17. "Even the most prolonged of Roman infantry contests did not usually produce greater *mutual* slaughter". | `[D]` SA p. 6 |
| A10 | Sabin's arithmetic bound on continuous duelling: if 5% of an army is in the front rank, strikes every five seconds, and under 1% of strikes kill or mortally wound, "each army would suffer 5 per cent fatalities *every ten minutes*" — which the record (A5) excludes for battles lasting hours. | `[D]` SA p. 11 n. 45 |
| A11 | Summary sentence: "If not decided at the first clash, the contests often dragged on for an hour or more before one side finally broke and fled. The losers could suffer appalling casualties in the battle itself or in the ensuing pursuit, but the victors rarely suffered more than 5 per cent fatalities even in drawn-out engagements." | `[D]` SA p. 8 |
| A12 | Clausewitz: "the most decisive losses on the side of the vanquished only commence with the retreat"; "In the combat the loss of moral force is the chief cause of the decision"; "without a pursuit no victory can have a great effect"; pursuit is "a second act of the victory, in many cases more important also than the first". | `[T]` CL Book IV ch. IV, XII |
| A13 | Du Picq, of ancient battle: the vanquished "took to flight during the fight of the first line and were struck with impunity from behind"; "Ancient battles were picnics, for the victors, who lost nobody." His Pharsalus figures (from Caesar): Caesar "lost in this battle but two hundred soldiers, but nearly thirty of the bravest centurions"; "Of Pompey's army fifteen thousand perished, and more than twenty-four thousand took refuge in the mountains." | `[T]` DP Part I ch. III–IV, Part II ch. I |
| A14 | **Du Picq gives no percentage for the losses at which troops break.** No such figure was returned from the 200,000 characters read. The tree's 15%–30% rout band is therefore Jordan's value, as `modules/mass_battle/config.py:182-183` already says ("Jordan historical research 2026-07-23"), and is not du Picq's. This agrees with what the MB lane file reported (`proposals/2026-11-12-subsystem-audit-suite/audits/04_MB_audit.md` §7). | `[T]` DP (part); absence, so weaker than a positive reading |

### B. Named battles: both sides' losses, with the spread of the sources

| battle | victor's loss | loser's loss | how the loser died | tier |
|---|---|---|---|---|
| Cannae, 216 BC | Polybius 5,700 of about 50,000 (about 11%); Livy "about 8,000" (16%). Sabin: "11 per cent … easily explicable in terms of the effort needed to annihilate a much larger Roman army". | Polybius 70,000 killed and 10,000 captured; Livy 48,200 killed and about 19,300 captured, of about 86,400. Modern low estimates exist (Cantalupi 1891: 10,500–16,000); Clodfelter doubts so many could be killed "on a single afternoon". | encircled, "no exit" | `[T]` W-CAN (part); `[D]` SA p. 5 n. 25 |
| Pharsalus, 48 BC | Caesar: about 200 and 30 centurions; Appian: up to 1,200, of 23,000 or more | Caesar: 15,000 (du Picq's reading) or more; Appian 6,000 killed; 24,000 captured, of 41,000–54,000 | left wing taken in flank after its cavalry fled; camp stormed | `[T]` W-PHA; `[T]` DP |
| Zama, 202 BC | 1,500 killed of about 29,000–30,000 (about 5%); Goldsworthy calls it "a substantial loss for a victorious army" | Polybius: 20,000 killed and about as many captured, of about 40,000 | third line struck in the rear by returning cavalry | `[T]` W-ZAM (part); `[D]` SA p. 5 |
| Hastings, 1066 | "Casualty figures are unknown"; Marren "speculates" 2,000 of 7,000–12,000 | Marren: perhaps 4,000 of 5,000–13,000; among named English participants about 50%, "although this may be too high" | leader killed late; line broke at dusk; pursued | `[T]` W-HAS (part) |
| Golden Spurs, 1302 | about 100–300 of 8,400–10,400 | about 1,000–1,500 men-at-arms of 2,500–3,000 (the cavalry arm); the foot fled | charge stopped at the pike line across brooks; no prisoners taken; survivors pursued "over 10 km" | `[T]` W-GS |
| Agincourt, 1415 | record evidence of at least 112; chroniclers 600 to 1,600, of 6,000–9,000 | about 6,000 of 12,000–15,000 (Curry, Sumption), "mostly nobility" | press and mud; archers closing with hand weapons; prisoners killed | `[T]` W-AGI (part) |
| Arsuf, 1191 | "no more than 700" (Oman, as the article reports) of 11,200–20,000 | chroniclers' 7,000 and 32 emirs; Oman thinks lower; infobox "unknown" | three charges, each pursued a short way and recalled | `[T]` W-ARS |
| Kalka, 1223 | "Minimal (modern estimates)" | chronicles: "only every tenth person returned" | strung out by a nine-day pursuit of a feigned retreat, then enveloped | `[T]` W-KAL |

Read together with A1–A9: where the loser could run and was not ridden down, he lost about a seventh (A1);
where he was pursued by horse or could not run, half or more (A6, Zama, Cannae, Kalka). The victor's loss sits
near 5% across the whole set and reaches about 11% only when he annihilates a larger army (Cannae).

### C. How long

| # | claim | tier |
|---|---|---|
| C1 | Roman infantry clashes were "sometimes decided very quickly by one side giving way at (or even before) the first shock". "More usually, however, Roman infantry battles involved a drawn-out engagement". | `[D]` SA p. 4 |
| C2 | Durations the sources state: Livy "several hours"; Plutarch, Pydna decided "unusually speedily in just one hour"; Vegetius 3.9, "usually resolved in two or three hours"; Caesar, Ilerda, a contest of several cohorts "as long as five hours". Corroboration by the "internal clock" of grand manoeuvres: at Cannae "at least an hour, and probably a lot longer" for the cavalry to win one wing, ride to the other and return on the infantry's rear. | `[D]` SA pp. 4–5 |
| C3 | Hoplite battles: duration is **not established** by the sources ("a hopelessly relative measure"); Sabin calls them "possibly much briefer". | `[D]` SA pp. 5–6 |
| C4 | Hastings: fighting "began at 9 am … and … lasted until dusk" (sunset 4:54 pm): about eight hours, with "a lull probably … early in the afternoon". | `[T]` W-HAS (part) |
| C5 | Agincourt: "The fighting lasted about three hours", after about three hours of standing inactive. | `[T]` W-AGI (part) |
| C6 | Clausewitz gives relative durations of resistance by the size of the body (a division of 8,000 to 10,000; a corps of three or four divisions "will prolong it to double the time"); the base figure in hours **was not returned by the reading and is not established here**. His point is that the larger the body, the longer a decision takes, and that fresh reserves are "always the chief point". | `[T]` CL Book IV ch. VI, IX |
| C7 | Cannae's duration is not stated on the page read beyond "ended at nightfall"; Pharsalus "some four hours" (du Picq's statement, his source not returned). | `[T]` W-CAN (part); `[T]` DP |

### D. What decides

| # | claim | tier |
|---|---|---|
| D1 | The decision is a collapse of will in one side, from "the panic of the losing troops due to the breaching of their line, a psychological shock such as the death of the general, or the sheer accumulation of casualties and fatigue." | `[D]` SA p. 15 |
| D2 | Flank and rear attacks decide for two reasons: "not just the psychological shock they caused but the fact that they crowded the victims in on one another, removing their ability to re-establish the 'safety distance' and so to recover their cohesion and fighting effectiveness." | `[D]` SA p. 16 |
| D3 | Fresh troops against tired ones is what the Roman multiple-line system bought: "The ancient authors repeatedly state that it was this advantage of having fresh men fighting tired ones which gave the Romans such an edge over opponents who were in equal or greater overall numbers, but massed in a single fighting line". Depth alone did not win (Cannae, Pharsalus: ten deep beaten by shallower lines). | `[D]` SA p. 7 |
| D4 | A line could be pushed back "hundreds rather than tens of yards" without breaking (Cannae's centre; the Helvetii "no less than a mile"); a pushed-back line could still win (Sellasia). Giving ground is a state between holding and routing. | `[D]` SA p. 6 |
| D5 | Many clashes were "decided at or before the first shock, with a charge by one side prompting its enemies to take flight at once"; hoplite fights sometimes produced "'tearless battles' when one side fled so soon that it outdistanced any pursuit". | `[D]` SA p. 13 |
| D6 | Collapse begins at the back: Caesar at the Sambre describes "men slipping away from the rear of his hard-pressed cohorts", which "accords exactly with how Napoleonic infantry columns seem to have broken from the back rather than the front" (Keegan, as Sabin cites him). Du Picq: "in ancient conflicts, demoralization and flight began in the rear ranks." | `[D]` SA p. 4; `[T]` DP Part I ch. V |
| D7 | Fear spreads from the point struck: "The wing taken in rear in this way loses ground; more and more the contagion of fear spreads to the rest." | `[T]` DP Part I ch. IV |
| D8 | Lanchester: the linear law is the one stated for ancient hand-to-hand fighting ("one soldier could only ever fight exactly one other soldier at a time"); the square law is for aimed fire. Helmbold (2021), as the page reports: "force ratio is an inferior and untrustworthy predictor of victory in battle." | `[T]` W-LAN |

## What this note does NOT establish

- **No casualty rate per minute, per tick or per phase of fighting.** A10 is an upper-bound argument, not a rate.
- **No share of the loser's dead that fell in the rout as against the fighting.** A7 and A8 say it is the
  larger part where pursuit was possible; nobody read here gives a number, and the spread between Krentz's 14%
  and Sabin's "over half" is the nearest thing to one: it brackets what pursuit and encirclement add.
- **No breaking threshold** (losses at which a body routs). Not in Krentz, Sabin or the du Picq read (A14).
- **No medieval or early-modern aggregate** like Krentz's: the medieval rows in §B are single battles with wide
  source spreads, several from chroniclers.
- **Nothing on wounded.** Every figure above is dead (or dead and captured where said).
- **Dupuy's, Helmbold's and Delbrück's figures**: not read; not quoted.
- The `[T]` rows are a small model's reading of a page. Before any of them becomes a calibration target,
  the page is opened again and the sentence found.
- Ancient figures are the victors' or their historians' (SA p. 5: "some understandable exaggeration by the
  victors"; `13_verification_corrections.md:271`).

## What it is for

It is the source for the calibration bands in
`proposals/2026-11-12-subsystem-audit-suite/proposals/26_MASS_BATTLE_calibration_targets.md` and for the
adjudication rows on results in `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`. A band taken from here is a
**reading target with a control**, never a gate that fits the engine to a number (the gauge note's own rule,
`mass_battle_gauge_grounding.md:4`, which its ceilings then broke: `04_MB_audit.md` §7).
