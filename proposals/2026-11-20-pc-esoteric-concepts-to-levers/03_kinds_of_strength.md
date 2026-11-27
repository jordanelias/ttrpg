# Part 3 — The kinds of strength, mapped to the engine's strength-like quantities

## Status: PROPOSED. Reference only. Each cluster's "kinds of strength" section was read in full; each kind below carries its cluster and the sheet's own entry name. A mapping follows the same rule as Part 1: what the kind is said to *do* in a fight, then where the engine computes that.

## 3.1 The engine's strength-like quantities (what exists to map onto)

| quantity | what it is in the engine | where it acts (sites opened) |
|---|---|---|
| **Strength** (attribute, default 4, centred at 4) | gross force | blow impact `K_STR_HEAD[head]·strength + heft` (`core.py:512-521`); the bind, weakly (`BIND_STR_K` 0.0156 per point, `combat_systems.py:941`); winding (`:329`); the grab, strongly (`GRAB_STR_K`, `contact.py:44`); half of `balance_eff` (`combat_systems.py:179`); the harness and weapon demand (`:150-156`, `:164-170`); arresting a heavy swing (`:253-254`); concussive load (`:1108`); a little Health (`combatant.py:37-39`) |
| **leverage** | the lever arm behind the hand, a weapon's geometry (two hands add control) | the bind (`:933`), displacement on the approach (`:839-843`), the beat-aside (`wrapper.py:383`), the grab (`contact.py:43`), the withdrawal's inclination (`:872`) |
| **moment in the contact** (`contact_moment_edge`) | how hard the weapon is to shove aside: the grip-adjusted static moment | the bind (`:944`), parry and wind (`:325`, `:331`) |
| **spine press**, **edge grab** | a single edge's spine binding (`:942`); the self-hazard of seizing a live edge (`contact.py:45`) | the bind; the grab |
| **bind dominance** | the bind's net sigma, logistic (`:926-945`, `:1303-1305`) | three bind iterations (`wrapper.py:431-443`) |
| **commitment** | how much of the body goes into this attack, `commit` in [2, 2 + 3·f(room)] | attack σ `COMMIT_SIGMA·(commit − 3)` (`:965`), legibility (`:813`), exposure (`:1038`), stamina (`:155`), recovery debt (`wrapper.py:287`) |
| **momentum on the approach** | a braced stop-thrust's arrest of a charging body (`arrest_impulse`, `:1233-1258`) | the approach only |
| **endurance** | Stamina `3·End + 2·Spirit` (`combatant.py:42-44`); Health and wound gates (`:27-39`) | cadence, footing, handling under fatigue; felling |
| **Concentration** | `3·Focus + 2·Spirit` (`combatant.py:172`), drained by blows | the lapse, the read under fatigue, consistency (`:1281-1289`) |
| **poise** | structure, broken by blows, binds, over-commitment and grips; regathered with Focus | cadence and `balance_eff` through `poise_factor` (`:1072-1077`) |

## 3.2 The clusters' kinds, mapped

| kind (cluster · sheet entry) | what it is said to do | engine quantity | verdict |
|---|---|---|---|
| Strength as steadiness, bearing a load (Europe · *Elefante*) | not toppled | poise: recovery yes (Focus), resistance to the break no | partial; N-6 |
| Cleverness over strength; subtlety over strength (Europe · Vadi; Fabris) | the small beat the large | the read (Perception), the lever arm against Strength. The engine **agrees in the bind**: Strength 4 → 7 moves one bind iteration from 50.0% to 48.8% (Part 7 §7.2) | **EXISTS-PHYS**: the bind is already decided by geometry and feel more than force |
| The strong and the weak of the blade; Destreza's nine to twelve degrees (Europe · Ringeck, Fabris, Destreza) | the part of the blade in contact decides who holds | **none**: the bind compares whole weapons (lever arm, moment, guard); no point of contact along the blade exists | **NO-HANDLE** (N-11) |
| Hard and soft in the bind (Europe · *Fühlen*; China · 走/黏) | the felt state of the bind selects the answer | the sign and size of `bind_sigma`, computed and used only as a draw | the quantity **EXISTS**; its use is N-5 |
| Whole-body force: "fight with the entire body"; "the root is in the foot … governed by the waist" (Europe · Liechtenauer v.14, Fabris; China · 其根在腳) | force from the unbroken chain of the body | **commitment** (how much body goes in) and Strength (impact); no separate linkage quantity | **EXISTS** as commitment; a "linkage" lever would only be a monotone σ bonus and is not proposed |
| Stored against released force: the bent crossbow; "store jin like drawing a bow" (China · 勢, 蓄勁) | potential held until the right instant | **none**: the commit never waits on an instant | **NO-HANDLE** (N-2, N-3) |
| Crude native force (拙力) against intent-led force (China · 氣力非二物) | force without intent is "master and servant inverted" | **none**: one Strength | **NO-HANDLE** (no addition proposed: it would be a second Strength) |
| Visible against hidden strength (China · 練氣歸根; 五行拳's clear/hidden/transforming jin) | true strength does not show | **none**: no fighter reads the other's capacity before the bout | **NO-HANDLE** (out of the bout: it belongs to a reading of the opponent the season would own) |
| Inner firmness against outer bravery (China · 內壯/外壯) | firmness is accumulated, bravery is active | nearest: Concentration (held) against temperament (spent) | UBR; no addition |
| Courage, "gall" (China · 有膽始有力); the lion (Europe) | fear stagnates the limbs | Concentration (Spirit, Focus) | **EXISTS**: inert on the defender's read, active on one's own attack σ (Part 7 §7.3) |
| The soft and yielding; water (China · 柔弱勝剛強; SE Asia · *Teratai*) | the yielding thing outlasts | **none** as a force (CP-05: the engine's feel does not grow with the opponent's force) | **NO-HANDLE** (N-5) |
| Precise strength, point-striking (China · 點穴; South Asia · *marmam*) | disables by placement | damage physics | forbidden (Class A) |
| Hardened body: iron shirt, the diamond body, the thunderbolt body (China; South Asia · *kāya-sampat*) | blows do not hurt | wounds | forbidden (Class A); armour is the loadout's |
| Given or infused might (Europe · *menos*); divine strength (China · Vajrapāṇi); devotion as strength (South Asia · Hanuman) | a god's gift | no canon carrier (the ground has no agency, P-07) | **NO-HANDLE** (canon; Part 5) |
| Frenzy and warp strength (Europe · berserker, *ríastrad*); divine fury (South Asia · kalari) | transformed force | temperament (the rush) + Class A (invulnerability) + nothing for the end of the fit | partial; N-7 |
| Endurance of pain (Europe · Sinfjötli, the agoge, *sacramentum*; Japan · Tesshu's *seigan*) | bearing what breaks others | Stamina and Health are endurance; bearing *pain* is not modelled (no pain state) | Stamina **EXISTS**; pain **NO-HANDLE** |
| *Sahaja / kālaja / yuktikṛta bala*: born, seasonal-and-age, made by regimen (South Asia · Charaka) | strength's three sources | born = the build's attributes; age = attributes the season changes; regimen = growth. None is a bout quantity | the *sources* map to the season (Part 4), not to a lever |
| *Bal* against *śakti* (South Asia · Alter) | manifest force against latent moral power | Strength for *bal*; nothing for *śakti* | partial (SA-07) |
| *Vīrya*, *ojas*, *tejas*, *tapas* (South Asia) | vigour conserved by continence or austerity | **none**: no state conserves or spends vigour across days in the bout | **NO-HANDLE** (season-side, if anywhere) |
| Malla-yuddha's four ideals: technique, holds, joint-breaking, sheer strength (South Asia · Wikipedia, unverified origin) | four routes to winning a grapple | technique levels; the grab (`contact.py`); joint-breaking has no effect channel (every grab outcome moves only poise or initiative, `contact.py:53-70`); Strength | partial |
| Strength subordinate to purity (Persia · *pahlavan*) | strength that rests on conduct | none | **NO-HANDLE** (canon) |
| Heavy-club strength by repetition (Persia · zurkhaneh) | strength built by drill | Strength raised by the season's growth, not a technique | season-side |
| Cunning (*malícia*), luck by charm (*sa'a*), the energy of action (*nyama*) (Africa) | reading and misdirection; fortune; a dangerous force | the read (F1, F3); nothing; nothing | partial; N-1; canon |
| The single decisive blow, *kwab daya* (Africa · *dambe*) | one blow ends it | a blow larger than the wound interval crosses several gates (`combatant.py:89-95`): damage physics | **EXISTS-PHYS**; no technique |
| Self-restraint as strength (Africa · *dônga*; capoeira's Pastinha) | the duel that does not kill | the duel's terms | **EXISTS** host-side |

## 3.3 What is missing, ranked by how many kinds it would carry

1. **A point of contact along the blade** (strong and weak; Destreza's degrees; the "four ounces" placed right): three kinds. Hook: `bind_sigma`'s lever-arm term (`combat_systems.py:932-934`). N-11.
2. **A state that holds force for the right instant** (the crossbow; stored jin; the falcon): two kinds, the same addition as N-2/N-3.
3. **Resistance to a broken stance** (the elephant): one kind. N-6.
4. **A conversion of the opponent's force** (the soft, water, four ounces): two kinds. N-5.

**What the engine already gets right, against the obvious reading.** "Strength" in the traditions is mostly *not* the Strength attribute. The engine agrees: Strength is decisive in the grab and in a blow's impact, minor in the bind, and absent from the read, the counter and the readiness race. The kinds the traditions value most (subtlety, feel, whole-body commitment, timing) already live in other quantities, and the one kind they value that the engine cannot express at all is *where* on the blade the contact is.
