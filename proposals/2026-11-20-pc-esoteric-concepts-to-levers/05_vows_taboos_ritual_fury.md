# Part 5 — Vows, taboos, rituals, protective charms, possession and fury

## Status: PROPOSED. Reference only. Every cluster's "prohibitions, vows, taboos, ritual obligations" section was read in full. No cosmology is imported: where the tradition's effect needs a metaphysics, the canon is consulted and the row stops there.

## 5.1 The canon's position, read first

The live philosophy suite (`canon/philosophy/`, which supersedes `canon/00_philosophical_foundations.md` by its own banner, 2026-09-07) gives the world one way to be altered beyond the ordinary: **threadwork**, operations on threads by a thread-sensitive practitioner. Four of its constraints (`canon/philosophy/10_constraints.md`) decide this part:

- **P-01, P-14, inseparability**: every thread operation moves all three dimensions; none is clean.
- **P-09**: such operations are "messy, costly and detectable".
- **P-07**: "The ground has no agency, intention, responsiveness, or direction" — so there is no god or spirit, of the kind these traditions invoke, to grant, protect or possess.
- **P-08, P-13**: thread-level competence is not acquired "by study alone" and does not transfer "as information" — so a school's rite, mantra or charm cannot teach a thread effect.

**Consequence for this part.** A charm, a blessing, a possession or a divine weapon has **no canon carrier as a martial technique**. If such an effect existed in Valoria it would be threadwork (another system, with its own costs and detectability), not a board entry, and the Church's prophylaxis would read it as contamination (`canon/00_philosophical_foundations.md` §4.3, read in the superseded copy; its §9 was not read). This part does not invent one.

## 5.2 What each kind of obligation can be, in the engine

| kind | examples (cluster · sheet entry) | can be modelled as | where | status |
|---|---|---|---|---|
| **A taboo that conditions a technique** | the geis (Europe); sak yant and anting-anting rules (SE Asia); the akhara's continence (South Asia); the Khalsa's prohibitions (South Asia); the shield's taboos (Plains) | a **condition on a board entry**: held while the rule is kept, dropped when it breaks | the host's board composer (jobs set Part 2 §2.3); the season tracks the rule | **EXISTS** host-side; nothing reaches `modules/` |
| **A rule of teaching** | Fiore's sworn witnesses; Talhoffer's master-and-pupil oath; the Katori blood seal; the Dhanurveda's tested pupil; the astra's recall rule ("knows … casting … as well as … counteracting") | a **`requires`** or a teacher condition on learning | the jobs set's free gates (Part 3 §3.1); D-7 there (may a teacher's level gate `train`?) | **EXISTS** host-side |
| **A vow that narrows a choice** | the saffron robe, no quarter (Rajput); the dog rope (Cheyenne); the Crow Crazy Dog's season; the *juramentado*'s oath | the duel's **terms** (`death`) and the **choice set** without `withdraw` (`wrapper.py:503-517`, `:552-553`) | host-side for the decider and the terms; **engine-side for the fighting withdrawal** (`disengage_attempt_p`, `combat_systems.py:857-876`) | decider and terms **EXISTS**; the withdrawal **NEEDS-GATE** — the jobs set's `withdraw_band` must be able to **narrow** (see 5.3) |
| **A rule of whom not to strike** | *avadhya* (South Asia); the Nguni stick fight's "no hitting a fallen man" (Africa); the Aztec capture-not-kill (Mesoamerica) | the yielded man's **disposition**, which the engine leaves to the caller (`wrapper.py:483-497`); the duel's non-lethal terms | host-side | **EXISTS** |
| **A ritual before the bout that sets a reserve** | misogi (Japan); Talhoffer's confession and Mass; wai khru (Thailand); ardās and the salute (Sikh); the kalari's right-foot entry | Concentration before the fight | **nothing to set**: every fight begins with Concentration full (`wrapper.py:41-46`) | **NO-HANDLE**, and none needed — the engine already gives every fighter the composure such a rite would restore |
| **A ritual before the bout that sets a temperament** | the *haka* (Māori, of oneself); Musashi's shout at the start; the Nihang's preparation | the fighter's **temperament** for this fight | B18.02's `temper` slot, a host input | **EXISTS** host-side; but D3 (5.4) |
| **A ritual aimed at the opponent** | the *haka* as intimidation; the kiai; Gai Nie's glare; intelezi said to blind | a drain on the **opponent's** Concentration | none today | **NO-HANDLE** (N-4) |
| **Protection and invulnerability** | the iron shirt; *corpo fechado*; anting-anting's *kabal*; Odin's blunted blades; the Boxers; the *juramentado*'s immunity | — | agency proposal §5 Class A (wounds, damage) and 5.1 (no canon carrier) | **NO-HANDLE**, by rule and by canon |
| **Possession and divine infusion** | the Vodou *chwal*; the Boxers' possession; Athena's *menos*; the berserker as Odin's gift | — | 5.1 (P-07: no agentive ground) | **NO-HANDLE** by canon |
| **Fury** | the berserker, the *úlfheðnar*, *ríastrad*, kalari's divine fury, the Nihang's bhang, the *sākā*'s charge | **temperament** (the rush) plus a **cost** the engine lacks (5.4) | `disp` today; N-9 and N-7 | partial |

## 5.3 A vow is a set run backwards

The jobs set lets a **set** widen one of four gates (Part 3 §3.1.1) and never narrow one. The vows above do the opposite: the dog rope, the saffron robe and the Crow's season each **close** a door the engine offers — the decider's `withdraw`, the longer weapon's fighting withdrawal, the yield. Three findings follow.

1. **Two of the three doors are host-side already.** The decider can simply never return `withdraw`; the host can simply never declare a `Yield`. No module change.
2. **The third is engine-side.** The fighting withdrawal (`wrapper.py:202-219`) fires from the engine's own inclination; a vow cannot reach it unless the `withdraw_band` gate can be set **below** today's behaviour as well as above it. That is a two-way gate, one more value of the same member, not a new member.
3. **What the vow buys is not in the bout.** Every tradition says the vow buys power or honour; Part 1 found that the power it guards is always some other technique (EU-13), and the honour is renown, the season's. In the bout a vow is **pure cost**, which is exactly what the traditions say it is from the fighter's side. The engine should carry only the narrowing; the reward belongs to the season (Part 8 §8.2, answered without escalation).

## 5.4 Fury: the brief's hypothesis, tested against the sources and the engine

The brief proposed fury as "raises commitment and lowers read". Derived from the sources rather than assumed:

- **Raises commitment.** The berserker "rushed forwards without armour"; the Crow Crazy Dog must "rush into danger"; the *juramentado* "charged a group". In the engine that is temperament at its aggressive pole: deeper commits (`combat_systems.py:989-994`), the Vor drifting up (`wrapper.py:165`), less reach for the counter (`combat_systems.py:1029`). **Present.**
- **Lowers the read.** The sources that name fury's cost name exactly this: Silver, revenge in rage is "the proper nature of wild beasts … being void of the use of reason" [PERIOD-TEXT; V: Wiktenauer Silver]; the internal-boxing commentary, a red face means "his temper rises … the mind must be hurried and he has lost the chance of victory" [MODERN-SYNCRETIC; V: 內家拳口訣釋義]; Munenori, "if the mind is in Attack, it will run to excess" [PERIOD-TEXT; V: WILSON]; Chōzan, *yaburu* "will be tricked by an opponent with superior technique" [LATER-CLASSIC]. In the engine an aggressive temperament **touches neither side of the read** (`read_contest`, `combat_systems.py:997-1017`, reads Perception, Agility, the levers, familiarity, legibility and Concentration, never `disp`). **Absent.**
- **Weakness after the fit.** "when the fever abated they were weak" (Bellows); the fury that must be quenched from outside (*ríastrad*). The bout has no state that a fury enters and leaves. **Absent** (N-7).

**Finding.** The half of the hypothesis the engine lacks is the half four traditions name as fury's price — and it is the price the agency proposal found missing when it measured temperament monotone (D3: 39.1 → 59.8), the second end the code's own comments promise ("BOTH poles cost: aggression risks overcommit …, caution bleeds the Vor", `config.py:257`; "the standing pressure that makes both poles cost", `wrapper.py:164`).

**Why this is not escalated as a new mechanism.** The plan already gives the lean a two-sided price: workplan v12 B16.08 builds a conserved transfer in `assemble_net_sigma` — "what a fighter adds to his own attacks he gives to attacks on him" — and ships its coefficient `APPROACH_SIGMA_K` at 0, the coefficient owed to a ruling of Jordan's (`workplans/valoria_master_workplan_v12_part23.md:221-223`; B98.26, D2-1, `…_part44.md:150`; rulings A-31, D-40). A read term on the lean would be a **second owner of one fact** (agency proposal §5.1 rule 1), against a precedent that has chosen the transfer. So this part withdraws "fury lowers the read" as a mechanism (N-9 in Part 6 is marked not proposed) and keeps the four sources as **evidence for D2-1**: the traditions that name fury's price all name a real one, so a coefficient of 0 is the one value they do not support. Where the price should land (in σ, as the transfer puts it, or in judgment, as the sources describe it) is a refinement of D2-1, not a new decision.

## 5.5 Stillness, the other pole, for symmetry

The internal school's stillness (CP-06), Munenori's abiding (JP-05) and Sunzi's first-unbeatable (CP-07) are the cautious pole of the same temperament. The sources quoted name no price for waiting (the research sheet's "waiting costs the initiative" is its compiler's summary, and Munenori's "set upon quickly" is said of one who does not expect the attack); the engine charges one anyway (the Vor drifts down, `wrapper.py:165`); their stated payoff — the attacker falls — is not reproduced (Part 7 §7.1), because the door they wait for is nearly shut in the close. With B15.04 (the deep tier follows the window, so the door opens) and B16.08 at a non-zero coefficient (what the still fighter withholds from his own attacks is withheld from attacks on him), both poles would have both ends, which is what the internal school and the berserker each claim for their own pole and deny to the other.
