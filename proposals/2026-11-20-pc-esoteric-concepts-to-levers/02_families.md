# Part 2 — Families: many traditions, few mechanisms

## Status: PROPOSED. Reference only. A family is grouped by the **structural role** its concepts play in the contest — the uncertainty or decision they act on — never by theme. Row ids refer to Part 1.

## 2.1 The families

| family (role) | the one mechanism | rows | clusters | status of the mechanism |
|---|---|---|---|---|
| **F1 Reading the coming attack** (the defender's uncertainty) | the defender's read in `read_contest`: Perception × `visual` × `precommit` × familiarity × the attack's legibility (`combat_systems.py:1003-1004`) | JP-14, CP-08, EU-01, AF-01 (reading) | 4 | live |
| **F2 Hiding one's own attack** (the attacker's side of the same read) | the aggressor's opposing read value, `(Perception + AGI_READ_K·(Agi − 4))·visual + consistency` (`:1011`), and the legibility of what he does (`:794-832`) | CP-10 (hare), CP-11 (the unknown fist), AF-02 (masking), CP-08 (he does not know me) | 3 | live |
| **F3 Information carried across exchanges** (feint, lure, lull, pattern) | **none** — every exchange forgets the last | JP-11, JP-12, CM-07, CP-10 (maiden), AF-01 (misdirection), SE-02, AF-07 (the feint) | 5 | NO-HANDLE (N-1) |
| **F4 The readiness race** (who acts, and keeps acting) | readiness = cadence × `tempo_pressure` (`wrapper.py:180`; `combat_systems.py:1173-1198`), with the Vor inside it (`:951-956`) | JP-06, JP-10 (*ken*), EU-05, SE-06 | 4 | live |
| **F5 Answering a commitment in its own tempo** | the deep-commit door (`wrapper.py:325`), then `counter_select` and `counter_success` (`combat_systems.py:1026-1029`, `:1296-1301`) and the Indes steal (`:1019-1024`) | JP-04, JP-07, JP-10 (*tai*), JP-15, CP-11, EU-06, CM-03 | 4 | live, **door nearly shut** (Part 7 §7.1) |
| **F6 Committing and holding back** (one's own commitment and its exposure) | the commit draw, skewed by temperament (`:980-995`), and the exposure it leaves (`:1031-1039`) | CP-06, CP-07, JP-05, JP-17, EU-09, CP-03, EU-11 (rush), SE-05 (charge), AF-06 | 6 | live, **one-sided** (D3) |
| **F7 Feel and yield in contact** | the bind's dominance contest (`bind_sigma`, `:926-945`): feel is its `tactile` term | CP-04, CP-05, EU-07, EU-06 (the bind steal) | 2 | feel live; yield NEEDS-BEHAVIOUR (N-5) |
| **F8 Composure under blows** (one's own capacity across the fight) | Concentration: reserve, drains, the lapse in the response, the mental fatigue on the read (`:1281-1289`, `:340`, `:1004`) | JP-01, JP-03, CP-12, EU-03, SA-01, SA-02 (lapse) | 5 | live, **near-inert and fatigue-gated** (Part 7 §7.3) |
| **F9 Responding when surprised** | the lost-read draw (`:1016`) | JP-02, SE-01 (UBR) | 2 | NEEDS-LEVER (PC-21's site) |
| **F10 Mobility, footing and structure** | Agility (cadence, reflex, `balance_eff`, the dodge), and poise | CM-04, EU-02, AF-02, EU-04, EU-15 | 4 | live; break resistance absent (N-6) |
| **F11 Acting on the opponent's composure** | **none** in the bout: nothing drains another man's Concentration except a blow | JP-16, AF-08; CM-01, CM-02 (outside the bout) | 3 | NO-HANDLE (N-4) |
| **F12 Attrition** | the stamina economy: `act_cost` per commit, paid by the aggressor alone (`wrapper.py:286`), the bout's recovery (`:626-627`) | SA-03, SE-03 | 2 | live |
| **F13 Distance** | the standing measure contest (`reach_sigma`, `:778-792`), the approach's true time (`:1142-1158`), facing (`:381-389`) | EU-01 (measure), EU-08, EU-15 | 1 | live; `facing_regime` held bare by ruling |
| **F14 Vows, terms and conditions** | host-side composition: board conditions, `requires`, the choice set, the duel's terms | EU-13, SA-04, SA-05, SA-06, AF-04, AF-05, AF-06 (the vow), AF-09 | 4 | live host-side; one gate must narrow (AF-05) |
| **F15 Forbidden targets** | none, by rule (agency proposal §5 Class A; §5.1 rule 2) | JP-13, CM-05, CM-06, EU-14, SE-04, SE-05 (endurance), AF-03, EU-11 (invulnerability) | 6 | — |
| **F16 Not a technique** (everyone's already, or no fight claim) | the contest structure or weapon physics | CP-01, CP-02, EU-05, EU-10, JP-09, JP-18, SA-07, SE-07 | 5 | — |

Sixteen roles carry 75 rows from seven clusters. **Six mechanisms carry the live, mappable variety**: the read (F1, F2), the readiness race (F4), the counter (F5), the commit and its exposure (F6), the bind (F7) and Concentration (F8). Three of those six have a defect the derivations ran into: the counter's door is nearly shut, the commit's temperament is one-sided, and Concentration hardly bites.

## 2.2 Each family: how the traditions differ inside it, and the name-match it refuses

**F1 Reading the coming attack.** Musashi and Munenori want a gaze that small movements cannot capture (JP-14) — a resistance to *deception*, not a better eye; the Taiji line wants the opponent read through contact (CP-08); Fiore's Lynx is a virtue of sight and measure (EU-01); *malícia* reads intent in order to misdirect it (AF-01). One mechanism, four different demands on it: the variety is *which* term of the read a school sharpens, and only `visual` and `precommit` exist to sharpen; the deception terms (`:815-816`) have no defender-side factor. *Refused name-match:* "the Lynx sees" → a `visual` technique. Fiore attaches no technique to the animals; the row maps a virtue to Perception.

**F2 Hiding one's own attack.** Sunzi's hare and the Maiden of Yue are suddenness after a lull (CP-10); Qi Jiguang's "the fist strikes when unknown" is the unread blow (CP-11); the *ginga* masks the transition by never stopping (AF-02). The engine already gives suddenness to Agility (`AGI_READ_K`), and the attack's own shape (a thrust, a shallow commit) to legibility. *Refused name-match:* the shadowless kick, or any "unseen" attack → `edge_read`. That lever is a double or false edge hiding the return cut (`:816`), a weapon fact with a weapon prerequisite.

**F3 Information across exchanges.** The largest unexpressed family: Musashi's feint that makes the enemy "show his long sword" (JP-11) and his rule never to try a thing a third time; boredom passed on (JP-12); Dugu's formlessness (CM-07); the maiden's lull (CP-10); *malícia*'s misdirection (AF-01); Kumango's three warnings (SE-02); the Māori point-feint into the butt-end blow (AF-07). Every one needs an exchange to depend on an earlier one. *Refused name-match:* feint → a shallow commit. The engine's dissolved feint (`wrapper.py:298-301`) makes a shallow attack hard to read; it draws out nothing and teaches the next exchange nothing.

**F4 The readiness race.** Munenori's no-beat puts the opponent behind (JP-06, run: his pressure falls to 0.64 at level 3); Musashi's *ken no sen* and Liechtenauer's *Vor* are the earned lead (JP-10, EU-05); the eskrima drill's flow is more actions without a reset (SE-06). The variety is earned against standing: the Vor is won and decays; the `tempo` term is held. *Refused name-match:* rhythm → weapon cadence. Cadence is the weapon's physics (`weapon_tempo`, `:83-110`).

**F5 Answering a commitment.** Takuan's no interval (not speed), the Ittō-ryū's cut down the centre line, Qi's strike-not-parry, Liechtenauer's *Indes*, Zhuangzi's late start and early arrival, Musashi's pillow at the first syllable. The engine has one machine for all of them and its gate is set at a commit the closed exchange almost never reaches. The variety the traditions describe is *what condition opens the door*: a deep commit (the engine), the first syllable (Musashi: `counter_shallow`), the feel in the bind (Liechtenauer: the bind steal, which does fire). *Refused name-match:* *kiri-otoshi* → a parry. It is filed on `guard_prior_parry` by the jobs set (Part 3 §3.4); its own account is a counter made on a read.

**F6 Committing and holding back.** One axis, two poles, with the traditions on both: the still pole (the internal school, Sunzi's unbeatable defence, Munenori's abiding, Silver's twofold mind, the Taiji fault of double weighting) and the furious pole (Chōzan's *yaburu*, the berserker's rush, the *juramentado*'s charge, the Crow's vow to die). Every one of them names the price of the *other* pole. The engine wires the furious pole's price (the exposure, the riposte) but measured it monotone, and the still pole's payoff fails in the run. *Refused name-match:* stillness → the counter lever. The run separates them: the lever never moves one's own commitment, and stillness is first a fact about one's own commitment.

**F7 Feel and yield in contact.** Liechtenauer's *Fühlen* and the Taiji's *zou* agree that the feel exists to *select* the next action (double against the hard, yield to the hard); the engine has the feel as a constant term in a dominance draw and no selection. The variety is the selected answer: Ringeck doubles, the Taiji yields, Meyer changes through. *Refused name-match:* four ounces → `leverage`. Leverage is the lever arm, a strength; the Taiji claim is explicitly "not victory by strength".

**F8 Composure under blows.** Takuan's unattached mind, Drona's one-pointed aim, the commentary's courage, Fiore's lion, the kalari master who strikes into a lapse of gaze. They disagree about *where* attention should go (spread against narrow) and agree that losing it loses the fight; the engine keeps one reserve and cannot express the disagreement. *Refused name-match:* attention → the board's attention budget (jobs set Part 2 §2.3.3). The budget is how many techniques a fighter brings; it never acts in the bout.

**F9 Responding when surprised.** *Mushin*'s body that "knows of itself" against the lotus that yields. Both act where the read is lost. *Refused name-match:* *mushin* → a habitual guard; Takuan names habit as the fault.

**F10 Mobility, footing and structure.** *Qinggong*, Fiore's tiger, the *ginga* and the Māori nimbleness are Agility; Fiore's elephant is the one concept about *not being moved*, and the engine has recovery from a broken stance (Focus) but no resistance to the break. *Refused name-match:* "stepping on clouds" → the `balance` lever (run: it never reaches the dodge).

**F11 Acting on the opponent's composure.** The shout before the cut, the *haka*, the glare, the wooden cockerel. Nothing in the bout lets one fighter act on the other's mind except a blow. *Refused name-match:* the *kiai* → attack σ (`COMMIT_SIGMA`). Musashi forbids shouting with the cut; the shout acts before it, on the other man.

**F12 Attrition.** The akhara's breath and *Siku 12*'s exhausting evasion both act on stamina; the engine already makes only the attacker pay for attacking. *Refused name-match:* breath → Concentration. The akhara claims "strength and stamina" first.

**F13 Distance.** Silver's hand before foot, Fiore's measure, Destreza's circle. *Refused name-match:* Silver's "true times" → the `measure` lever; Silver's sentence is about the order of hand and foot.

**F14 Vows, terms and conditions.** The geis, the astra's recall rule, the saffron robe, whom not to strike, the coup, the dog rope, the Crow's vow, the referee. All compose host-side; the one engine-side need is a gate that a vow can *narrow* (AF-05). *Refused name-match:* geis → a power bonus. The geis names no power; it conditions whatever the hero already has.

**F15 Forbidden targets** and **F16 Not a technique** refuse nothing; they record what is out of reach by rule or already everyone's.

## 2.3 What the grouping shows

- **Variety by cost and condition, not by mechanism.** Inside F5, six traditions differ only in the condition that opens one door; inside F6, nine differ only in which pole they hold and which price they name. A school's identity in the engine is therefore *which condition it opens and which price it accepts* — a set's opened gate (jobs set Part 3 §3.3) and a temperament — far more than which factor it sharpens.
- **Opposite prescriptions land on one quantity** (F8: Takuan and Drona; F6: the internal school and the berserker). The engine can carry the disagreement only where the quantity has a direction (F6 does) and not where it is a reserve (F8 is).
- **The live counts are uneven.** F3 (7 rows, no mechanism) is larger than F1 (4 rows, live). The addition that would carry F3 heads Part 6.

## 2.4 Two smoothness findings met on the way (NERS S; reported, not fixed here)

1. **One term, two engine readings.** Silver's true time is the reach edge on the approach (`true_time_edge`) and, separately, commitment discipline (`true_times` on `anti_overcommit`). Two ladders named for one source (EU-08).
2. **The deep-commit door and the swing room disagree.** `DEEP_COMMIT` is 4.0 (`config.py:294`); the closed exchange's room caps the commit at 4.03-4.09 (Part 7 §7.1). Every site behind the door — the counter, the open Indes steal, the displace-and-step-inside, the over-committed closer's reopen moment, the lunge (`LUNGE_COMMIT` 4.0) — almost never fires in the close. **Already owned, not escalated**: workplan v12 B15.04, "the deep tier follows the window it is drawn in" (`workplans/valoria_master_workplan_v12_part18.md:153-175`), replaces `DEEP_COMMIT` and `LUNGE_COMMIT` with the window's upper third and states the same finding ("the shipped 4.0 … sits in the top 1.5% of the window"). This run is independent corroboration; B15.04 is not built on this branch (`config.py:294` still reads `DEEP_COMMIT=4.0`).
