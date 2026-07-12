# Event Cards — Section 2.1: Succession Crises, Civil Wars, and Elite Power-Struggle Collapses (Geopolitical)

*Key: `succession-crises-civil-wars-elite-power-struggles`. Binds to the §2.x succession-split resolver: Trigger Matrix, Stage-1/Stage-2 contest, G-based Unified/Split, Split Persistence, plus Ministry/Consulta (Part 7). The through-line: **granting independent Military/Standing to heirs is what makes the next leader-loss fire the mandatory-contest row** — and the only durable off-ramps are institutional (Ratify, Consulta, Oath, Fratricide), each with its own recurring cost.*

Source: `designs/audit/2026-07-10-historical-concerns-action-catalogue/historical_concerns_action_catalogue_v1.md`, §2.1.

---

### HEV-SUCC-01 — Year of the Four Emperors (Rome, 69 CE) · Crisis
- **Historical grounding:** Rome's rapid sequence of military-acclaimed emperors following Nero's fall — Galba, Otho, Vitellius, Vespasian — per catalogue citation *§2.1–2.4 + Part 7 + §1.3c Ratify/Reject/Amend.*
- **Trigger:** `leader eliminated AND heir.Disposition<3 AND ≥2 contenders AND |Standing gap|≤1`
- **Response branches:** Comply (recognize the sitting military claimant) binds you to a possibly-doomed claimant; Bargain buys concessions; Defy backs a rival, feeding their External-backed strength.
- **Follow-on (FO):** A bare military win reseeds the Crisis next season (Galba→Otho→Vitellius→Vespasian); a win + Ratify writes a `military-acclamation-legitimate` Precedent that closes the chain but permanently lowers the retrigger threshold.
- **Introduces (Action):** Donative + Ratify (extends *Levy* and the Hold-Court *Ratify/Reject/Amend* branch): spend Treasury to buy a contender's Stage-1 military-Loyalty check, then convert a fait-accompli into legitimacy via a Consulta vote.
- **Loop:** Donative and Ratify are complements not substitutes — a bought win leaves Mandate depressed and Π high (reseeding the Crisis) unless the separate Ratify writes the closing Precedent; Otho's donative bought weeks, Vespasian's *lex de imperio* bought a dynasty.

### HEV-SUCC-02 — The Anarchy (England, 1138–1153) · Friction→Crisis
- **Historical grounding:** The English civil war between Stephen and Matilda following broken succession oaths — per catalogue citation *§2.2 claim-basis, §2.3 G≤1 SPLIT, §2.5 re-merge, §1.6 Compact/Grudge/Reputation.*
- **Trigger:** A `Succession Guarantee` Compact exists but is *not* one of the four recognized claim-basis types AND a rival's Standing is comparable.
- **Response branches:** Comply (a sworn Inner-Circle member honors the oath) defends the heir but strains local Order; Defy (backs the rival) writes a severe Grudge + `Reputation:Oathbreaker` on that NPC.
- **Follow-on (FO):** Mass reneging auto-triggers G≤1 SPLIT → recurring "Baronial Free Agency" Crisis, closable only by a Bargain-Directive §2.5 treaty re-merge on a next-generation compromise heir (Wallingford → Henry II).
- **Introduces (Action):** Extract Succession Oath (new Compact-family tag + mass social contest, parallel to §1.3a Negotiate Quota): gives the named heir a *fifth, oath-based* claim basis and taxes later defectors with Grudge+Oathbreaker — the enforcement teeth the 1127/1131 oaths to Matilda lacked.
- **Loop:** Extracting the Oath early costs Mandate/AP but brakes the mandatory-contest row; skip it and any comparable rival hits it with no brake, and the resulting Split erodes the Mandate needed to ever extract a credible Oath afterward — the nineteen-winter doom loop.

### HEV-SUCC-03 — Ottoman Interregnum / Fetret Devri (1402–1413) · Crisis
- **Historical grounding:** The Ottoman succession vacuum among Bayezid I's sons following the Battle of Ankara — per catalogue citation *§2.2 institutional claim-basis from Governor Assignment, §2.4 splinter residual Standing, §1.0a Demotion Magnitude as template for a Fratricide tier.*
- **Trigger:** `leader eliminated/captured AND ≥2 contenders each holding a Governor Assignment` (institutional basis auto-satisfied); the distinct post-resolution choice is whether the winner invokes Fratricide.
- **Response branches:** Post-resolution choice between sparing losing claimants or invoking Fratricide against them.
- **Follow-on (FO):** Sparing claimants seeds a guaranteed Ambition card next Generational-Shift ("a spared rival claims again"); invoking writes `Reputation:Hated`/Grudge raising Intrigue (assassination) draw-weight.
- **Introduces (Action):** Fratricide Law (Crown-tier post-Contest option amending §2.4): spend a severe Demotion-Magnitude-"total" Reputation/Grudge cost to strip all losing claimants rather than let them persist as splinters.
- **Loop:** Granting real Governor Assignments to multiple heirs is what makes the next leader-loss near-certainly contested; Fratricide closes that reopening loop but converts a recurring *external* civil-war risk into a recurring *internal* assassination risk — it trades escalation paths, not eliminates risk.

### HEV-SUCC-04 — Mughal War of Succession (1657–1661) · Intrigue
- **Historical grounding:** The four-way war among Shah Jahan's sons (Dara Shikoh, Shah Shuja, Aurangzeb, Murad Baksh) turning partly on religious orthodoxy accusations — per catalogue citation *§1.0c Court Attendance/Hostage-Kin, §1.0a Tribunal severity, §2.2 contender formula, §7 social-contest resolver.*
- **Trigger:** `succession contest active AND a contender's Church-Disposition/Conviction diverges from the dominant framework` (seeded by Grudges).
- **Response branches:** Denounce-as-Heretic routes the target through the Church Tribunal — conviction guts their Influence-based Stage-1 pool, acquittal backlashes on the accuser.
- **Follow-on (FO):** A convicted-but-not-eliminated contender's still-loyal Governors seed a "Loyalist Holdout" Crisis keeping the contest live.
- **Introduces (Action):** (a) Court Attendance/Hostage-Kin for heirs (extends §1.0c from absentee-governors to Crown heirs); (b) Denounce as Heretic (new Intrigue social contest via the Tribunal branch).
- **Loop:** Keeping an heir at court trades a Suspicion/Treasury cost now for lower future claim-basis strength; leaving heirs as independent subadar-governors (as Shah Jahan did) inflates all their strengths symmetrically, guaranteeing a multi-front contest — and once open, Denounce cuts a rival's pool without a battle, at a priced tit-for-tat.

### HEV-SUCC-05 — Inca Civil War / Huáscar vs Atahualpa (c. 1529–1532) · Crisis
- **Historical grounding:** The Inca succession war between half-brothers Huáscar and Atahualpa immediately preceding Pizarro's arrival — per catalogue citation *§2.1 Smooth/Regency rows, §2.3–2.4, `faction_action.py` Conquest.*
- **Trigger:** `succession_rule=="Partible/Panaca" AND leader eliminated AND ≥2 heirs each already holding independent territory+Military`; no political Stage-1 resolution exists (no shared territory to allocate) — routes straight to armed Conquest.
- **Response branches:** No political resolution branch — routes directly to armed Conquest between heirs.
- **Follow-on (FO):** The winner emerges Military/Treasury-exhausted ("Weakened Victor" modifier) raising an external-faction Opportunity/Crisis draw (Pizarro 1532).
- **Introduces (Action):** Partible Succession (durable faction-configuration Precedent flag set at founding): maximizes the living dynasty's footprint but disables the peaceful Smooth/Regency rows forever.
- **Loop:** Adopts near-term expansion for a structural guarantee that the same independent Military that made each heir strong is what makes them fight; set-once and irreversible (panaca as multi-generation institution), it can only be avoided by never adopting it, not managed well after.

### HEV-SUCC-06 — Muscovite Time of Troubles (1598–1613) · Intrigue
- **Historical grounding:** Russia's dynastic collapse after the Rurikid line's end, marked by the False Dmitry pretenders and eventual Zemsky Sobor election of Mikhail Romanov — per catalogue citation *§2.1 Regency/3-Accounting collapse, Part 7, §1.3a stale-high Assessment revolt logic.*
- **Trigger:** `regency_active AND Π≥mid AND Reputation∈{Weak,Hated}` (fed by a stale Assessment or unrelieved Need) → an unverified External-backed pretender.
- **Response branches:** Investigate exposes/voids the pretender's claim; ignoring treats the claim as real at next Stage-1.
- **Follow-on (FO):** An unresolved pretender seeds a "Second Pretender" (the False Dmitrys), each raising Π toward the 3-Accounting collapse.
- **Introduces (Action):** Convene Consulta (Regency election branch, after 2 not 3 failed Accountings): tally Standing+Disposition+Influence, majority wins, bypassing the dice resolver (Zemsky Sobor electing Mikhail Romanov).
- **Loop:** Running Regency to term lets pretender Intrigue compound (and a simultaneous stale Assessment/unrelieved Need independently raises the *same* pretender card's weight); convening a Consulta early spends capital to close the loop, at the cost of crowning the most *institutional* rather than most *military* claimant.

### HEV-SUCC-07 — Toluid Civil War (Mongol, 1260–1264) · Friction
- **Historical grounding:** The Mongol succession war between Kublai and Ariq Böke that permanently fractured the empire into Yuan/Chagatai/Golden Horde/Ilkhanate successor states — per catalogue citation *§2.2 institutional basis, §2.3 G-based, §2.5 re-merge, §1.4 Directive template for Recall, Part 7.*
- **Trigger:** `succession contest active AND a contender holds an appanage-style Military grant AND their External-backing exceeds the capital Inner Circle's combined Standing` → able to convene a rival legitimating assembly.
- **Response branches:** Comply writes a `venue-controls-legitimacy` Precedent lowering future threshold; Defy forces the §2.3 SPLIT *overriding* the strength-gap math even where G≥3 would resolve Unified.
- **Follow-on (FO):** Dueling assemblies seed a "Rival Successor-State Sets Own Directive" Friction every season, *exempted* from §2.5 re-merge (the permanent Yuan/Chagatai/Golden-Horde/Ilkhanate split despite Kublai's dominance).
- **Introduces (Action):** Recall (new Directive type alongside Extract/Tax/Suppress/Install/Host/Cede) to disband an appanage prince's forces — Defy here is diagnostic; and Convene Rival Assembly (Contest-stage exploit controlling which claim-basis holders attend).
- **Loop:** Appanage grants raise Contest strength *and* let a loser convene a rival assembly and Defy the verdict, so the same policy that decides who wins determines whether the loser's refusal is survivable — turning a recoverable splinter into a permanent fracture the Recall lever was never used to prevent.

### HEV-SUCC-08 — Kongo Civil Wars (17th–18th c.) · Ambition→Crisis
- **Historical grounding:** The recurring succession wars among Kongo's Kimpanzu and Kinlaza lineages under an elective monarchy — per catalogue citation *§2.1–2.2 elective/institutional basis as the standing rule, §1.3a Levy method pattern, §1.3c Ratify/Reject/Amend, §1.6 Outlawed family.*
- **Trigger:** `settlement has an untaxed trade node (external Wealth bypassing the Levy method) AND lineage_head.Standing ≥ elector threshold` → "Lineage Head Arms Retinue".
- **Response branches:** License-now (Trade Writ Ratify) caps independent Wealth at Disposition cost; Reject drives it underground (Outlawed+Grudge); ignore lets Wealth/Military compound.
- **Follow-on (FO):** An un-Ratified compounding lineage converts to a Crisis at next leader-loss ("Comparable-Standing Lineages Contest the Capital").
- **Introduces (Action):** (a) Elective Succession (config flag routing contested rows to a §2.2 institutional electoral tally); (b) Trade Writ (new Levy method, Ratify/Reject/Amend a trade node's Wealth flow).
- **Loop:** Elective monarchy has electors not armies decide, but electors reward capability so lineages keep private Wealth/Military topped up; if the untaxed-trade leak is never closed via a Trade Writ, a vacancy lets several comparably-armed lineages contest directly — "elective monarchy legitimizes an arms race that periodically breaks out anyway" (the Kimpanzu/Kinlaza pattern).
