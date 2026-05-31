# Martial Traditions × Weapons × The Seven Axes — A Grounded Mapping

**Status:** Class-C **proposal**, Jordan-vetoable. No canon edited. Built **bottom-up** from the canonical 8-weapon roster + the ratified σ-leverage / state-graph combat model, and **top-down** from the project's *own* historical research — not web search, not pattern-matching.

**Sources (all read in full this session):**
- `historical-precedents/combat-manuals-seven-axes-throughlines.md` — the seven-axis re-cut of the intensive combat-manuals research (reach · speed/useability · stance · initiation · footwork · grip · technique) + nine consolidated throughlines.
- `historical-precedents/blunt-weapon-martial-traditions-completed.md` — the percussion/staff survey (grounded-vs-folklore graded).
- `historical-precedents/manual-vs-combat-v32-bridge.md` — the keystone: per-weapon tradition counts + each axis mapped to a combat mechanism.

`[READ: all three above — full]` · `[CONFIDENCE: high — every row traces to one of these docs; their contested-point flags are carried through, not smoothed.]`

**Two discipline notes carried from the research, load-bearing:**
1. The seven axes **are the European-treatise lens** (T1). They read brightly in the temporal-spatial (Italian) and tactile (German) traditions and **dim** in traditions organized around intent (Japanese), geometry (Spanish), cosmology (Chinese/Indian), or rhythm (Filipino). *The dimming is data, not a gap.* A combat system is forced to commit to one lens — ours is the Western dueling paradigm (the bridge doc's whole-system read).
2. **In-world cultural naming is yours (project-owner contract).** Below I map to the *real historical* traditions as grounding/inspiration. What the Valorian cultures are called, and which of them carry which school, is a creative-layer decision I do not make here.

---

## MAP 1 — The weapon census: how many kinds, and what each is

Eight canonical weapon classes (from `m3_weapon_class_layer.py`, the roster this session built and ratified on). Each is an abstraction over the canonical combat_v30 §5 axes (**reach × weight × type**) plus **speed** and **handling** (ease-of-use curve). The "best-fit historical weapon" and "traditions" columns are from the bridge doc's grounded count.

| # | Class | reach · weight · type | speed | handling | Best-fit weapon | Traditions at depth |
|---|---|---|---|---|---|---|
| 1 | `long_thrust_primary` | long · light · blade | 1.5 | Demanding | rapier / estoc | **2–3** (Italian, Spanish; English engages) |
| 2 | `long_cut_and_thrust` | long · heavy · blade | 0.5 | Standard | longsword / two-hander | **5–6** (German, Italian, English, Korean, Chinese, Japanese) |
| 3 | `curved_cut_primary` | long · light · blade | 2 | Standard | sabre | **6** (Polish-Hungarian, Mamluk-Ottoman, Indian, Chinese, Korean, Japanese) |
| 4 | `long_pole_spear` | long · light · blade | 0 | Forgiving | spear | **7–8** — the richest (Chinese *qiang*, Japanese, Korean, Indian, Mamluk, European, Filipino, Byzantine) |
| 5 | `long_pole_staff` | long · light · blunt | 0 | Forgiving | staff | **6** (Chinese *gùn*/Shaolin, Indian Silambam, English short-staff, Egyptian *tahtib*, Japanese *bō*/*jō*, Korean) |
| 6 | `paired_short` | short · light · blade | 2.5 | Demanding | dual short blades | **3** (Filipino *doble baston*, Korean, Chinese) |
| 7 | `single_short` | short · light · blade | 3 | Forgiving | dagger / short sword | **5–6** (German, Italian/Fiore, Filipino, Indian, Japanese, English) |
| 8 | `long_heavy_blunt` | long · heavy · blunt | −0.5 | Demanding | mace / poleaxe / maul | **3** (Indian *gada*, Mamluk *dabbus*, European poleaxe) |

**Shape of the census (bridge doc):** the **universal** weapons are spear (7–8), sabre (6), staff (6), longsword (5–6); the **regionally specialized** are rapier (2–3), paired-short (3), heavy-blunt (3). This is *why* the spear/staff are the near-universal formation weapons and the rapier/poleaxe are niche.

**Three census caveats the research flags (not mine to wave away):**
- **The classes are coarse** — no curvature axis and no one-/two-hand axis. So the one-handed **arming sword / sidesword** (a period workhorse) falls *between* `curved_cut_primary` and `long_cut_and_thrust`; several East-Asian two-handers are *curved* (ōdachi, wodao) and straddle the same two. The ranges above reflect those straddles.
- **The missing class is SHORT BLUNT.** The blunt-weapon survey is explicit: one-handed blunt arts (Irish shillelagh, French *canne*, Zulu *isikhwili*, *tonfa*, conditioning clubs) have **no home** in our all-*long* blunt classes — a genuine gap. It would be a *thin* category (much of it reconstruction/sport/conditioning, not a deep combat corpus). **Adding it is your call.**
- **`long_heavy_blunt` fuses two historically distinct weapons** — the technical, grappling-heavy **hafted hammer/poleaxe** (justifies *Demanding* + high ceiling) and the **bare mace** (historically *forgiving*, levy-friendly, needed almost no codification). Which one the class represents changes its handling rating. This is the duel-vs-battlefield split we already ratified, with documentary backing.

---

## MAP 2 — Which martial traditions historically correspond, per weapon

From the bridge doc's at-depth count (a tradition "applies" if the manual treats it in a per-tradition section **and** documents a weapon of that class as central). Traditions counted once each.

- **Rapier (`long_thrust_primary`)** → **Italian** (Capoferro/Fabris/Giganti) · **Spanish** (La Verdadera Destreza) · *English engages it (di Grassi/Saviolo/Swetnam), though Silver argues against it.*
- **Longsword (`long_cut_and_thrust`)** → **German** (Liechtenauer) · **Italian** (Fiore, *spada da doi mani*) · **English** (two-hand sword + backsword) · **Korean** (*ssangsudo*) · **Chinese** (*wodao*/*dadao*) · **Japanese** (*ōdachi*; katana read as cut-and-thrust).
- **Sabre (`curved_cut_primary`)** → **Polish-Hungarian** (*szabla*) · **Mamluk-Ottoman** (*shamshir*/*kilij*) · **Indian** (*talwar*) · **Chinese** (*dao*) · **Korean** (*hwando*) · **Japanese** (*katana*). *The manual's signature "one weapon-family, many cognitive frameworks" case (T7).*
- **Spear (`long_pole_spear`)** → **Chinese** (*qiang* — the deepest spear corpus, Wu Shu) · **Japanese** (*yari*) · **Korean** · **Indian** (Dhanurveda) · **Mamluk** (lance) · **European** polearm · **Filipino** (*sibat*) · **Byzantine** (*menaulion*).
- **Staff (`long_pole_staff`)** → **Chinese** (*gùn*/Shaolin — most-documented late-Ming weapon) · **Indian** (Silambam) · **English** (short staff — Silver's favorite) · **Egyptian** (*tahtib*) · **Japanese** (*bō*/*jō*, Shintō Musō-ryū) · **Korean**.
- **Paired short (`paired_short`)** → **Filipino** (*doble baston* / *espada y daga* / *sinawali* — the signature) · **Korean** (*ssanggeom*) · **Chinese** (*shuangdao*).
- **Dagger (`single_short`)** → **German** (dagger) · **Italian** (Fiore's foundational dagger) · **Filipino** (*daga*/*balisong*) · **Indian** (*katar*) · **Japanese** (*tantō*) · **English** (sword-and-dagger).
- **Mace / poleaxe (`long_heavy_blunt`)** → **European poleaxe** (Fiore's *azza*, *Le Jeu de la Hache*, Talhoffer, Mair; + *Mordstreich*, armored combat) · **Indian** (*gada* — the deepest mace tradition, but **today conditioning, not combat**) · **Mamluk** (*dabbus*). *The bare mace/hammer is richly attested as an object and almost nil as a transmissible art — its technique survives only via the hafted poleaxe corpus.*

**Folklore the research explicitly red-flags (do not encode as fact):** an ancient continuous *bare-mace* fighting art; the one-handed ball-and-chain flail as a real field weapon; "Kali" as a single ancient Filipino mother-art; Bodhidharma founding Shaolin; the Musashi-vs-Gonnosuke *jō* origin; "2,000-year-old" *gada* combat lineage.

---

## MAP 3 — What each tradition offers, by the seven axes

The seven axes are the categories ("footwork, grip, angles, approach, stances, techniques…"). Below, per tradition: its distinctive content on each axis, **and** the combat mechanism it maps to (so a "tradition" is not flavor — it is a *bias across the σ-leverage / state-graph channels*). Axis→mechanism mapping is from the bridge doc:

> **reach** → engagement-state graph + weapon reach-TN (phase-dependent reach, R9) · **speed/useability** → Weapon Speed scalar + handling curve; Silver's biomechanics → commit-depth × reaction-slope (M5) · **stance** → the authored Stance-Counter, Closing-gated (M5) · **initiation** → the bout transition weights + Reaction-vs-commit-depth + Counter-time set · **footwork** → facing → FoV cone (M7), advantage emergent · **grip** → weapon-constrained Grip loadout slot · **technique** → trained-pool → equipped named set (generative).

### German (Liechtenauer) — the **tactile / bind** tradition · weapons: longsword, dagger, poleaxe
- **Stance:** *Vier Leger* (Ochs/Pflug/Vom Tag/Alber) — two pairs on orthogonal axes; **each Meisterhau both attacks and defeats one specific guard** → the purest fit for our authored Stance-Counter.
- **Initiation:** *Vor / Indes / Nach* — initiative / the instant-on-contact / response; *Indes* + *Fühlen* (feeling the bind) → Reaction-on-contact, the decision tier.
- **Grip:** *Halbschwert* (half-sword) — grip change converts sword→short-spear for armoured thrusts; *Mordstreich* (pommel strike) → our **Half-grip** slot exactly.
- **Technique:** *Drei Wunder* (cut/thrust/slice) + *Fünf Meisterhäue* + *Winden* (winding the bind) + *Stark/Schwach* (blade leverage) → **generative** trained-pool; the **Bind Fighter** named set.
- **σ-leverage signature:** dominates the **in-bind** state (Stark/Schwach = the bind-leverage we model as Strength's bind-win + winding).

### Italian (Fiore → Bolognese → rapier) — the **temporal-spatial** tradition · weapons: longsword, dagger, rapier
- **Reach:** *misura* (larga / stretta / fuori) — at *misura larga* a long rapier may never touch the blade before the thrust, so **time, not contact, is the channel** → our approach-phase reach-control.
- **Stance:** Agrippa's **four guards** (prima–quarta), deduced to *exhaust* the space; the **point-forward** posture that makes the thrusting rapier viable.
- **Initiation:** *tempo / mezzo tempo / contratempo*; *invito* (an open invitation); Fabris's *opposition* (every offence carries embedded defence) → the **Counter-time** set (the dueling-context apex, T6/§15.5).
- **Footwork:** **the lunge** (drive off the rear leg without committing the rear foot) — first full description in Giganti (1606), *not* Capoferro (a 19th-c historiographic artifact the research corrects).
- **Technique:** Bolognese cuts (*fendente/mandritto/riverso/squalembrato/tondo/montante*) + *cavazione* (disengage around opposition) → **Thrust Duelist** set.
- **σ-leverage signature:** **tempo/initiative** (Agility→σ-tempo) and the counter-window.

### Spanish (La Verdadera Destreza) — the **geometric** tradition · weapon: rapier
- **Footwork = the geometry:** the *círculo* whose **diameter is the opponent's reach**; *compases* (recto/transverso/curvo) + six *movimientos* — all motion read off the circle. **This is our facing→FoV channel operationalized** — the cleanest alignment in the whole comparison.
- **Angles/Stance:** *atajo* (taking/closing the opponent's line) — stance as *constraint of the opponent's line*, the relational reading (T5); *ángulo recto* upright posture.
- **Initiation:** apex = the **geometrically-calculated safe action** (not the counter) — a *different* apex, because the mode is geometric not dueling-tactile (T6).
- **Grip:** the *daga de mano izquierda* (off-hand dagger) with trapping quillons.
- **σ-leverage signature:** **facing/position** (M7) — advantage emerges from controlling the perceptual frame, not from an authored modifier.

### Japanese (kenjutsu / koryū) — the **intentional / consciousness** tradition · weapons: sabre (katana), longsword (ōdachi), dagger, staff
- **Reach:** *maai* (tōma/uchima/chikama), anchored on *issoku ittō no maai* ("one-step one-cut distance").
- **Stance:** five *kamae* (chūdan/jōdan/gedan/hassō/waki) — **but Musashi's "stances and no stances"**: learn the named guards, then transcend them (the reduction-then-transcendence caution, T4).
- **Initiation:** *sen* in three tiers — *go-no-sen* (after) / *sen-no-sen* (simultaneous) / **sen-sen-no-sen** (before, by reading intent) → the **finest initiative tier**, no clean European equivalent; maps to our Predictive-Anticipation / Intent-Reading-within-FoV (the pre-commit channel). *kan no metsuke* (perceiving intent) beats *ken no metsuke* (seeing motion).
- **Technique:** Itto-ryū *kiriotoshi* — **one cut that simultaneously parries and strikes the centerline** (fuses initiation + technique); the killing-sword/life-giving-sword duality.
- **Footwork:** Katori Shintō-ryū's **triangular** pattern → our named **Triangular** footwork.
- **σ-leverage signature:** the **reading channel** (Cognition/Attunement → σ) at its most extreme — intent-reading as a pre-commitment edge.

### Spanish-counter / English (George Silver) — **biomechanical** · weapons: short staff (his favorite), backsword, sword-and-dagger
- **Reach:** *true place* — the distance from which you can strike and they cannot; weapon-length-dependent.
- **Speed:** **the five *true times*** (hand / hand-and-body / body-and-foot / foot-and-body / foot) — fast parts must move before slow parts; leading foot-first = a *false time* that over-commits → **our commit-depth × reaction-slope** (a deeper commit raises the opponent's reaction effectiveness). *(The research flags Silver's anti-rapier conclusion as contested; his biomechanical principle is sound, his rapier verdict the error.)*
- **Initiation:** the counter-stroke exploiting the opponent's committed action.
- **σ-leverage signature:** **tempo discipline** — punishing over-commitment, rewarding the economical lead.

### Chinese (staff / spear / internal) — **cosmological** overlay · weapons: spear (*qiang*), staff (*gùn*), sabre (*dao*)
- **Technique:** spear core *lan / na / zha* (parry / take-control / thrust); Xingyiquan's five attacks on the five phases (*wuxing*); *fa jin* (issuing force) → maps to our **Burst** named set (explosive committed opening).
- **Reach:** the spear as *zhi bing zhi wang*, "**king of weapons**" — reach + point-leverage dominates *provided body mechanics are correct* (the spear-dominance side of the long-vs-short debate — which our R9/R10 resolves by phase + context).
- **Useability:** spear/staff = **Forgiving** (learnable fast for mass troops — the historically-grounded handling assignment the bridge doc highlights).
- **σ-leverage signature:** reach-control + the committed thrust; the formation/battlefield context (R10).

### Filipino (FMA) — the **kinetic-rhythmic / flow** tradition · weapons: paired short, dagger, staff
- **Reach:** *largo / medio / corto*, mapped to specific weapon lengths.
- **Technique = flow:** the *numerada* (12 named angles) → *sinawali* (paired-weapon weaving), *hubud-lubud* (close sensitivity), *gunting* ("defang the snake," disarm). **Discrete technique dissolves into continuous flow** → our **Continuous-flow** named set ("flow sub-actions across multi-pass bouts").
- **Initiation:** attack and defence are *continuous*, not a counter-apex (T6 — a different apex).
- **σ-leverage signature:** sustained tempo across passes, the paired-weapon close game (the signature of `paired_short`).

---

## How this would become a "Martial Tradition" mechanic (the proposal)

The bridge doc already identifies the hook: v32's **named sets** (Thrust Duelist, Bind Fighter, Counter-time, Burst, Continuous-flow) **map onto these traditions** (Italian / German / Italian-Japanese counter / Chinese / Filipino). So a *Martial Tradition* is not a new subsystem bolted on — it is a **named bundle of biases across the seven axis-channels**, expressed as: a preferred **stance set** (Stance-Counter nodes), a **footwork** (facing/FoV pattern), a **grip** (loadout slot), an **initiation emphasis** (which `sen`/tempo tier it rewards), and a **signature technique cluster** (the named set + its bonus). A character's tradition tilts their σ-leverage profile toward specific phases — German into the bind, Italian into tempo, Spanish into facing, Japanese into reading, Chinese into the committed thrust, Filipino into flow.

**Two things remain yours (contract):** (1) whether to add a **short-blunt** weapon class to close the documented gap; (2) the **in-world names/cultures** for these traditions — I've grounded them in the real historical schools; the Valorian fiction is your layer. I have not invented either.

`[ASSUMPTION: the 8-class roster is the working canon (this session built + ratified on it); the bridge doc's "Class B draft" caveat predates that ratification.]`
`[GAP: short/one-handed blunt weapon class — documented as missing, thin if added; your call.]`
