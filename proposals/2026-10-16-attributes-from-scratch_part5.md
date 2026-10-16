# Attributes from scratch — part 5 (Phase B): comparison, precedent, limits

## Status: PROPOSED

Continues `2026-10-16-attributes-from-scratch_part4.md`. The from-scratch set is part 4, §6. Verb ids
are in part 1. Cluster ids `K01`…`K27` are in part 3, §5.4.

**Written after Phase A.** Parts 1–4 were written to disk at 2026-10-16 18:44:35 UTC (file
modification time), and this part's sources were opened after that. A modification time shows when
Phase A was written, not when anything was read. The reading order is my report, not a measurement.

**Read for this part:**

- `references/descriptor_registry.yaml`, lines 1–70 (the nine attributes and the practitioner stats)
  and the `not_descriptors` block.
- `proposals/2026-10-16-attribute-derivation_part3.md` §6–§8 (lines 20–292).
- `proposals/2026-10-16-attribute-derivation_aptitudes.md` (all of it).
- `proposals/2026-10-16-attribute-derivation_divergence.md` (lines 6–47 and §4–§8).
- `research/by_lane/00_COMPARATIVE_ANALYSIS.md` (headings and §C5.2).
- `research/by_lane/PC_personal_combat.md` §2.2's precedent table (lines 100–116).
- Grep hits in `research/valoria_game_precedent_companion_v1.md`.

**Not read:** the derivation's head and `_part2`, the character-template parts, `_equivalences`.

**Names, checked against the registry only after Phase A was on disk.** Four of my plain names collide
with registry words:

| my name | registry word with the same spelling |
|---|---|
| **reasoning** | an alias of Acuity |
| **presence** | an alias of Charisma |
| **composure** | a derived value in `not_descriptors` |
| **stamina** | a derived value in `not_descriptors`, used in my larger set |

I chose them blind as ordinary words. They are kept as written so the Phase A record stays as it
was. A later renaming is a choice for whoever adopts any of this.

---

## 7. Mapping

**Abbreviations used in §7–§8.**

| set | abbreviations |
|---|---|
| the registry's nine | Strength, Endurance, Agility, Focus, Acuity, Will, Attunement, Charisma, Bonds (`references/descriptor_registry.yaml:36-48`), plus Thread Sensitivity as a practitioner stat (`:64`) |
| the recommended eleven | STR, AGI, END, FOC, ACU, WIL, ATT, CHA, BON, REC, TS (`_part3` §7.4; the demands under each are in `_aptitudes`) |

### 7.1 From-scratch → registry nine and recommended eleven

| from-scratch | registry nine | relation | recommended eleven | relation | note |
|---|---|---|---|---|---|
| **bodily force** | Strength | **agrees** | STR | **agrees** | both narrow to the bout. The eleven's STR has no sourced use outside combat; the blind set adds hauling, labour, the war bow and climbing |
| **quickness** | Agility (alias Dexterity) | **splits** Agility | AGI (quickness, reflexes, balance, dexterity) | **splits** AGI | the blind set takes AGI's quickness, reflexes and balance and leaves dexterity to fine hand |
| **fine hand** | Agility's Dexterity alias | **splits** Agility | AGI's `dexterity` + practice `precision` | **splits** AGI; **absorbs** a practice demand | the divergence test could not test dexterity (D06, no reader) |
| **toughness** | Endurance (alias Vitality) | **agrees** | END (stamina, toughness, hardiness) | **agrees** | same three members, same draw (cost) |
| **watchfulness** | Attunement's Perception alias | **no clean counterpart**: closest is the alias | ACU's `observation` | **splits** ACU | three proposals put noticing in three places (§8.2, D-6) |
| **reading people** | Attunement | **agrees** (minus the Perception alias) | ATT (reading-people, empathy, discernment) | **agrees** | the divergence test found ATT a rescaled ACU wherever code reads it (X05) |
| **reasoning** (incl. memory) | Acuity (alias Reasoning) | **agrees in part** | ACU (`reasoning`) + REC (`memory`, `inference`) | **merges** part of ACU with part of REC | the blind set leaves REC's learning, breadth and practice ceiling without a home (§8.3) |
| **forethought** | — | **no counterpart** | practice `planning`, `numeracy`; CHA's `judgment`, `tactical-read`; ACU's `anticipation` | **no counterpart**: scattered over practice, CHA and ACU | the blind set's largest effect-mover (25 verbs) |
| **nerve** | — | **no counterpart** | temperament `boldness` (TMP, larger thirteen only) | **no counterpart in the eleven** | the eleven read boldness as a lean (fails monotone); the divergence test found TMP monotone in the one matchup tested (X12) |
| **constancy** | Will (alias Spirit) | **agrees in part** | WIL (will, steadfastness, sincerity, devotion, contact-endurance) + temperament `patience` + practice `discipline` | **agrees in part; absorbs** a temperament and a practice demand | the blind set excludes WIL's thread roles (the thread pool, contact-endurance) |
| **composure** (incl. quick wits) | — (Focus nearest) | **no counterpart** | FOC's disruption and poise terms, in part; practice `deception`, `quick-thinking` | **no counterpart; absorbs** two practice demands | the registry's derived "Composure" is a different quantity (F24, on CHA) |
| **presence** | Charisma (alias Presence) | **agrees** | CHA (presence, persuasiveness, leadership) + practice `intimidation` | **agrees in part** | the blind set gives CHA's `judgment` and `tactical-read` to forethought and reading people |
| **warmth** | Bonds (aliases Sincerity, Affability) | **agrees** with the aliases | BON (`relational-depth`) + ATT's `empathy`, in part | **agrees in part, broader** | the eleven's BON is one formula (the knot gate). The blind warmth serves 14 verbs in nine subsystems |
| **thread perception** | Thread Sensitivity (practitioner stat) | **agrees** | TS | **agrees** | the blind version is [INFERRED]; the eleven's has T2 readers |

### 7.2 Reverse: each of the eleven → the from-scratch set

| eleven | absorbed by | how |
|---|---|---|
| **STR** | bodily force | whole |
| **AGI** | quickness + fine hand | split: body speed and balance / hand precision |
| **END** | toughness | whole |
| **FOC** | **none whole**. Parts go to composure (disruption, poise), watchfulness (vigilance over time) and constancy (patient application) | the verbs never ask for "concentration" as a separate demand. Sustained attention shows up as watching or as applying oneself |
| **ACU** | split: reasoning (reasoning, inference), watchfulness (observation), forethought (anticipation), and the fieldcraft skill (land-sense, spatial-sense) | ACU's five demands spread over three attributes and a skill |
| **WIL** | constancy (will, steadfastness, sincerity); `devotion` → a value (conviction); `contact-endurance` → the thread self-integrity track | split three ways |
| **ATT** | reading people | whole |
| **CHA** | presence (presence, persuasiveness, leadership); `judgment` and `tactical-read` → forethought; `situational-awareness` → watchfulness and composure | split |
| **BON** | warmth | whole, broadened |
| **REC** | reasoning (memory, inference); `learning`, `breadth`, `practice-ceiling` → **none** | half absorbed, half without a home |
| **TS** | thread perception | whole |

**Count.** Of the eleven, five map whole: STR, END, ATT, BON, TS. Six split: AGI, FOC, ACU, WIL, CHA,
REC. **One has no whole counterpart: FOC.** Of the fourteen from-scratch attributes, eight have a
counterpart among the eleven that agrees or agrees in part: bodily force, toughness, reading people,
reasoning, constancy, presence, warmth, thread perception. Three split one of the eleven: quickness,
fine hand, watchfulness. **Three have no counterpart: forethought, nerve, composure.**

---

## 8. Agreement, disagreement, and what would decide it

### 8.1 Where the blind derivation agrees with the eleven

1. **The body is three things, and they are the same three:** force, quickness and toughness against
   STR, AGI and END. They have the same draws: force moves effect, quickness odds, toughness cost
   (blind §5.4; the eleven's §8.1 roles). The eleven's evidence was formulas and code readers; the
   blind set's was verbs and etymology. Both found the same body triad.
2. **Reading people, presence and warmth are separate social capacities:** ATT, CHA and BON. The blind
   set finds them broad (23, 20 and 14 verbs). In the eleven, BON is one formula wide.
3. **Thread perception is its own primary:** TS. The blind case is the weakest in its set, because it
   knows the threads only by verb names.
4. **Holding a course is one primary:** WIL, read as constancy.
5. **Skills, holdings, tracks and temperament sit outside the primaries.** Both sets apply the same
   principles: stable to carry; capacity, not lean or preference; general across domains, not one
   domain's practice. Learned skills, resources, tracks and dispositions are left off the sheet's
   attribute row in both.

### 8.2 Where it disagrees (not resolved here)

| # | disagreement | the blind derivation's evidence | the eleven's evidence | what would decide it |
|---|---|---|---|---|
| D-1 | **Forethought is a primary**; the eleven scatter it over practice (`planning`, `numeracy`), CHA and ACU | 25 verbs, seven subsystems, the largest effect-mover (22 of 30 draws); the *price* and *see ahead* root families | no code reader for planning or numeracy; their draws are all inferred (`_aptitudes`, practice row); P6 says practice grows by use within a domain | (a) build resolvers for provision, tax, ration, audit, appraise, bargain, and see whether one per-person term recurs across them (a domain-general talent) or each wants its own trained skill (practice). (b) Then run the divergence test, forethought against ACU |
| D-2 | **Nerve is a primary**; the eleven make boldness a temperament lean outside the set | 19 verbs in all ten subsystems; moves **access** (16 of 20) | `disp` is a lean read as `(disp − 4)/3`, aggressive against cautious (P5); but X12 found TMP monotone in the one matchup tested | whether the decision layer gates which acts a person will consider by a personal threshold. If it does, nerve has a reader of its own kind. And whether TMP stays monotone against an aggressive opponent (the divergence test's own named limit) |
| D-3 | **Composure is a primary**; the eleven put deception and quick-thinking in practice, and poise in FOC | 17 verbs, eight subsystems, odds-moving; opposition symmetry (a liar needs a number that reading people opposes) | no code reader; every practice draw inferred | build an opposed lie/detect resolution (the SC lane's M-SC-7 and the IN lane's M-IN-14 ask for one) and test whether the liar's term separates from the hearer's reading people |
| D-4 | **Fine hand splits from AGI** | 11 verbs over nine subsystems: forge, craft, heal, weave, steal, aim; the forger sets the examiner's obstacle | AGI carries `dexterity`; D06 is NOT TESTABLE (no reader) | a reader for any hand act outside the bout (forge's `forgery_quality`, IN-45; a craft or surgery roll), then the divergence test: dexterity against tempo |
| D-5 | **FOC has no counterpart** | no verb asks for concentration as distinct from vigilance (watchfulness) or patient application (constancy) | FOC holds through formulas alone (the Concentration tracker; X01, A01 separable from WIL in combat) | whether concentration is used outside the bout. If only the combat tracker reads it, the blind reading is that it is a combat-local computed quantity or track. If threadwork's operations cap or a fieldwork roll reads it, the eleven's reading stands |
| D-6 | **Noticing (observation) is separate from reasoning**; the eleven put observation in ACU; the registry aliases Perception to Attunement | watchfulness: 17 verbs; the *watch* and *hide* families; the hawk-eyed sentry against the short-sighted scholar | observation is a capacity used through ACU; D09 is NOT TESTABLE | any inquiry resolver that reads both a noticing roll and an interpreting roll (FI's examine and reconstruct), with the divergence test run on the pair |
| D-7 | **REC's learning, breadth and practice ceiling have no blind home** | no verb's demand is "learning faster". `study` and `train` draw constancy and memory | REC is selected on coverage of design formulas F37–F40, with no code reader (X08) | a progression design that reads a learning rate; or the 2026-08-15 objection the eleven themselves record (*"a mandatory tax stat"*) |
| D-8 | **Reading people and presence stand as broad primaries**; the divergence test found ATT a rescaled ACU (X05) and CHA inert at T2 | 23 and 20 verbs | code: where read, ATT is about half an ACU; CHA moves nothing in the contest | build readers where reading people opposes lie, feint and flatter, and where presence moves command, rally or levy, then re-run X04 and X05 |

**What the disagreements say, taken together.** The two derivations count different things. The
eleven count **what formulas and code read**. Where a formula exists without a verb (FOC's tracker,
REC's learning formulas), they keep a primary the verbs cannot see. The blind set counts **what acts
ask for**. Where a verb exists without a formula (provision, tax and ration; accept and defy; lie and
conceal), it finds a primary the eleven file as practice or temperament. **Neither base settles it
alone:** a formula nobody performs and a verb nobody resolves are both unverified demand. The evidence
that decides each row is the same kind every time: **a resolver that reads the candidate, and a
divergence test against its nearest neighbour.**

### 8.3 Coverage, each against the other

**Demands the blind set covers that the eleven leave as practice, temperament or uncovered:**

| eleven's demand | its place in the eleven | blind attribute that covers it |
|---|---|---|
| `boldness` | temperament | nerve |
| `planning`, `numeracy` | practice | forethought |
| `precision` | practice | fine hand |
| `deception`, `quick-thinking` | practice | composure |
| `intimidation` | practice | presence (menace) |
| `discipline` | practice | constancy |
| `patience` | temperament | constancy |

**Demands the eleven cover that the blind set leaves without an attribute:**

| eleven's demand | blind place |
|---|---|
| `concentration` (FOC) | spread over composure, watchfulness and constancy (§7.2) |
| `learning`, `breadth`, `practice-ceiling` (REC) | no home |
| `contact-endurance` (WIL) | a track |
| `self-coherence` | a track (both sets leave it uncovered as a primary) |
| `devotion` | a value |
| `land-sense`, `spatial-sense` | the fieldcraft skill |
| `verbal-fluency` | a skill (both sets) |

**Each set's demand list is also partly invisible to the other.** The eleven's 46 demands contain no
"judgement of value", "keeping one's word", "moving unseen" or "hiding things". The blind set's 67
atomic demands contain no "learning rate" or "practice ceiling". The blind set's holdings (standing,
means, following: 40, 21 and 25 verbs) do not appear in the eleven's demand list at all. They are
outside a person in both, but only the blind set measured how much of the game they gate (84% of
access draws, part 3 §5.1).

---

## 9. Precedent cross-check (tier 3: precedent, not evidence)

**Source caution.** The research tree names these games but does not tabulate their attribute sets.
`00_COMPARATIVE_ANALYSIS.md` §C5.2 frames twenty titles by structure, not by attributes. The PC lane's
precedent table (`PC_personal_combat.md:100-116`) grades Burning Wheel, Pendragon, Darklands, Disco
Elysium and Mount & Blade as "named only", "unreached" or below its sourcing floor. The companion file
cites CK3 and the Romance of the Three Kingdoms series through a nine-pass personnel survey.
**The attribute lists below are from my memory**, at the confidence stated. They are tier-3 precedent
and decide nothing.

| game (where research/ names it) | primaries (from memory; confidence) | against the from-scratch fourteen |
|---|---|---|
| **Crusader Kings III** (companion; PC lane) | Diplomacy, Martial, Stewardship, Intrigue, Learning, plus Prowess; personality traits (brave/craven, just/arbitrary, forgiving/vengeful …) kept separate (high) | role domains, not capacities: stewardship ≈ forethought; intrigue ≈ composure + reading people; learning ≈ reasoning. **Brave/craven is a trait, not a skill**: CK3 puts nerve among values, as the eleven do (D-2) and as the blind P7 would for forgive/avenge. Holdings (gold, prestige, piety) are currencies, not skills: agrees with P6 |
| **Romance of the Three Kingdoms XIII–XIV** (companion: the personnel survey) | Leadership, War, Intelligence, Politics, Charisma (high) | **Intelligence and Politics are separate**. That is the blind split of reasoning from forethought (D-1). Leadership ≈ presence; War ≈ force plus knowledge of war; Charisma ≈ warmth |
| **Mount & Blade II: Bannerlord** (companion; PC lane) | Vigor, Control, Endurance, Cunning, Social, Intelligence, each over skills (Warband: Strength, Agility, Intelligence, Charisma) (medium-high) | **Control (bow, crossbow, throwing) is separate from Vigor (melee)**, close to the blind fine hand / aim against force. Cunning (scouting, tactics, roguery) ≈ watchfulness + composure; Intelligence (steward, medicine, engineering) ≈ forethought + reasoning |
| **Burning Wheel** (companion; PC lane) | Will, Perception, Agility, Speed, Power, Forte; derived Steel, Health, Reflexes, Hesitation (high) | **Speed (body) and Agility (hand) are separate stats**: the blind quickness against fine hand split (D-4). Power ≈ force; Forte ≈ toughness. **Steel, nerve under fire, is a derived attribute**: a third reading of nerve, neither primary nor lean. Perception spans noticing and knowing, against the blind split (D-6) |
| **Disco Elysium** (PC lane: "named only") | Intellect, Psyche, Physique, Motorics, each over six skills (high) | **Composure is a Motorics skill**, Perception a Motorics skill, Volition (≈ constancy), Authority (≈ presence) and Empathy (≈ reading people) Psyche skills; Half Light (fight-or-flight) ≈ nerve; Shivers and Inland Empire are uncanny perception (cf. thread perception). Four broad attributes over many skills is close to the blind smaller set |
| **Pendragon** (PC lane: "historical record only") | Size, Dexterity, Strength, Constitution, Appearance; paired Traits (Valorous/Cowardly, Merciful/Cruel, Forgiving/Vengeful, Honest/Deceitful, Prudent/Reckless …) and Passions (high) | **Values are a separate paired block, and Valorous is a trait**. That supports the blind P7 and the eleven's reading of boldness (D-2). Appearance has no blind counterpart: no verb asks to be beautiful (§10) |
| **Darklands** (PC lane: "named only") | Endurance, Strength, Agility, Perception, Intelligence, Charisma, Divine Favor (medium) | a body triad, one noticing stat, one mind stat, one social stat, plus a setting gift (Divine Favor) that sits where thread perception sits |

**What the precedent suggests, at tier 3.**

- **The body triad is near universal.** Two of seven games split hand from body (Burning Wheel,
  Bannerlord).
- **One of seven splits planning from reasoning** (RoTK).
- **Nerve is never a primary.** Three games make it a trait or derived figure (CK3, Pendragon,
  Burning Wheel), one a skill (Disco Elysium). That is the strongest precedent against a blind choice,
  and it agrees with the eleven.
- **Composure is never a primary** either; it is a skill in Disco Elysium.
- **Values are a separate block wherever a game models them** (CK3, Pendragon). That agrees with both
  derivations.

---

## 10. Limits

1. **The verb list is a sample I chose. 86 of 179 verbs are my additions**, and they are design
   proposals, not sources. Part 3 §5.6 measures the dependence. On the 45 code rows alone, the body
   and stealth clusters nearly vanish: force ranks 18th, quickness 24th, self-command 27th. Quickness,
   fine hand, composure and constancy owe most of their breadth to the additions. A different author's
   additions would move the counts.
2. **The demand statements are judgements.** 536 statements, one author, no independent critic. The
   source tags (R/S/O) make the basis visible but do not make it right. The patient-side demands (47)
   are an extension the brief did not ask for.
3. **Etymologies are from memory and unchecked**, with a confidence on each. The low and medium rows
   (fight, march, kill, dodge, rush, bargain, grapple, pull, seize, abolish, waive, dispatch, bless,
   strike, flatter, track, bribe, repudiate, comply) carry no weight in §5.5's families beyond what the
   high rows already carry. The register observation (Germanic verbs ask for the body, Latinate verbs
   ask for a seat) is **[INFERRED]** from this list. It is a pattern in English, not a law of persons.
4. **A verb-driven derivation cannot see what nobody performs.** Ageing, illness, appearance, how fast
   one learns, and resistance to harm all go unseen. Hardiness reaches only 8 verbs, and only because
   the patient-side demands were added. That is why REC's learning family (D-7) and Pendragon's
   Appearance have no blind home. It is a blind spot of the method, not evidence that they do not
   matter.
5. **Counts measure breadth, not weight.** A cluster drawn by 20 verbs may matter less than one drawn
   by 5, if the 5 are the ones played every scene. Nothing here measures frequency of play.
6. **The re-reading of the Latinate bodily roots as positional demands** (§5.2, §3.6) is the single
   judgement with the largest effect. Read the other way, *standing* becomes a 40-verb attribute.
7. **Independence between persons (P2) is asserted, not measured.** The co-occurrence table (§5.7)
   shows the *acts* tell the clusters apart; it cannot show *persons* vary on them separately.
8. **Threadwork is [INFERRED] throughout.** Thread perception is the weakest member of the set, and the
   thread verbs' demands rest on names alone.
9. **Possible priming** (part 1, reading record). The brief named the eleven, and §8.2 lane rows
   mentioned attributes, reader competence and troop quality. I cannot show that I was not nudged
   toward reading people and the body triad.
10. **No design document is cited as proof of behaviour** (CLAUDE.md §0.05). The eleven's and the
    divergence test's figures are quoted as those proposals report them; I re-ran none of their
    probes. Nothing here was executed against the engine, and nothing here is a mechanism.
