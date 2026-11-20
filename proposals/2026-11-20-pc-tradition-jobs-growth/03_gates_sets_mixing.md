# Part 3 — What gates what, what enables what; sets; techniques per tradition; mixing

## Status: PROPOSED. Reference only. Every technique value named here lives in `sheets.py` (`CURRICULUM`, `NEW_ABILITIES`), in the earlier draft's `kits_draft.py` (DRAFT values, read by `sheets.py`), or, for live techniques, in `modules/combat/ability_primitives.py`; this file names entries and never restates a value.

## 3.1 The gate-and-enable map

"Rigid" means an engine fact: physics or a state the engine computes, verified in code, and never a board entry. "Free" means authoring data the host composes, which Jordan can change without touching the module.

| gate | rigid or free | where it is read | what passing it enables |
|---|---|---|---|
| **tradition known** | free | host, when a technique is learned (after B18.02; today `_invested`, `ability_primitives.py:156-182`) | learning that tradition's curriculum |
| **`requires`** (a prerequisite technique at a level) | free | host, when a technique is learned | the next technique in a line |
| **second-tradition threshold** | free | host, when a second tradition is taken | cross-training (§3.6) |
| **teacher's level** | free | host, when a level is raised (Part 4) | levels up to the teacher's |
| **growth stage** | free | host, composing the board | more slots per column (Part 4) |
| **attention budget** | free | host, composing the board | how many entries are held (Part 2) |
| **set complete** (all members on the board) | free | host, composing the board | one access or one board rule (§3.3) |
| **weapon morphology: half-sword** | **rigid** | `combat_systems.py:742-752` (`affords_halfsword`) | the half-sword form against rigid armour |
| **weapon morphology: point, blunt head, short reach** | **rigid** | `systems/combat/combat_engine_v1/capabilities.py:39-60` (`gap_thrust`, `percussive_blow`, `open_contact`; predicates verified there against `core.coupling` and `contact.grab_available`) | the puncture and percussion modes; a grab with no prior opening for a dagger-short weapon |
| **weapon morphology: spine, edge lines, a pole to gather** | **rigid** | `combat_systems.py:942`, `:816`, `:817` | whether a `spine_press`, `edge_read` or `choke_control` technique can act at all |
| **armour tier** | **rigid** | `reach_sigma`'s `REACH_W[armour]` (`00_tradition_sets.md:62`, read there in full) | the measure lever fades by about two thirds against plate |
| **a won read against a deep commit** | **rigid** today; widenable by a set | `wrapper.py:325` (`if read_win and commit>=cfg['DEEP_COMMIT']`) | the counter attempt and the Indes initiative steal |
| **an opening this beat** | **rigid** today; widenable by a set | `wrapper.py:370-421` sets `opening_created`; `contact.py:27-36` reads it | a grab for anyone whose weapon is not dagger-short |
| **leverage deficit and reach threat** | **rigid** today; widenable by a set | `wrapper.py:206`, `combat_systems.py:857` (`disengage_attempt_p`) | a fighting withdrawal from a bind |
| **the per-round choice set** | **rigid** membership today | `wrapper.py:552-553` (`TURN_CHOICES = (ENGAGE, WITHDRAW)`) | what a player may decide once per engagement |

**What stays rigid, and why (brief Addendum 7).** Physics and computed state are the engine's: a technique does not put a point on a mace (agency proposal §5 Class B, first row). The *only* place a board reaches into the engine's behaviour is by widening a gate the engine already rolls, and only towards availability (Class B: "availability, never magnitude"). **What is free:** which techniques exist, which tradition files them, their order, prerequisites, costs, sets, slots, budgets, teachers. All of that is host-side authoring data, and a change to it never edits `modules/`.

### 3.1.1 The proposed `gate` slot family

Four members, each an existing `if`, each closed by default (closed = today's behaviour, byte-identical):

| gate | the `if` it widens | open means | Class B row it relies on (agency proposal §5) | note |
|---|---|---|---|---|
| `counter_shallow` | `wrapper.py:325` | a won read against a shallow commit admits a counter attempt; the counter's own success roll and the punishment of a miss are unchanged | (new row, same rule) | the block also holds the Indes steal; the build must split it (`00_tradition_sets.md:61`) |
| `steal_shallow` | `wrapper.py:325` | the same for the Indes initiative steal | (new row, same rule) | the other half of the split |
| `grab_close` | `contact.py:27-36` | at closed measure, a trained grappler's grab needs no prior opening (the dagger's exemption, lent) | "grant a trained grappler a grab on a class of opening they could not otherwise use" | "may not: make grabs available from open measure" holds: closed measure only. [INFERENCE: the closed-measure state is in scope at the call `wrapper.py:453`; not verified] |
| `withdraw_band` | `combat_systems.py:857` | the leverage-deficit band in which a withdrawal is attempted widens | "widen the leverage-deficit band in which a withdrawal is attempted" | the read contest that decides whether it is clean is unchanged |

## 3.2 Tradition categories (brief Addendum 5), read against the engine

A category has content only where the engine has a site to act on. Sources are inspiration (Addendum 6), so a category is empty only for want of an engine site, never for want of a treatise.

| category | engine site today | content | status |
|---|---|---|---|
| weapon (blades, poles, short arms) | the duel's fifteen levers | live and draft techniques in every tradition below | **has content** |
| unarmed and grappling | the contact axis (`contact.py`), `edge_grab`; no unarmed weapon record (H-265: `Combatant(weapon='unarmed')` raises `KeyError`; B18.03 adds the record) | `ringen_am_schwert` (live), `abrazare` (draft, needs a lever), Filipino live hand (new) | **has content**; unarmed fighting waits on B18.03 |
| armoured | armour tiers, the half-sword switch, the reversed-grip percussion option: all physics | none as board entries, deliberately (`00_tradition_sets.md:71`: "a German ability on either would double-count") | **rigid physics**; armoured skill shows through Strength against `ARMOR_DEMAND` (`config.py:111`) and the weapon, not a technique |
| mounted | none: `grep -n "mount\|horse\|cavalry" modules/combat/*.py` finds only a geometry comment (`weapon_physics.py:384`) | none | **EMPTY: no engine site** |
| formation and army-scale | the mass-battle module, another scale | none here | **out of this lane**: a tradition's formation teaching would land in mass battle's unit inputs, a separate design |
| social-martial (challenging, terms, yielding) | season verbs `challenge`, `accept`, the duel terms (`wrapper.DUEL_TERMS`, `fight.py:191-193`) | none | **EMPTY: no lever**; a technique of reading a challenger belongs to the social contest's capabilities, not this board |

## 3.3 Sets: a named group of 3–4 techniques that opens one door

**The user's model, mapped (brief Addendum, "masteries … categories … cost … cap … set effects"):** mastery = a technique (a board entry); category = a column; cost = attention cost; per-category cap = the slot count (the per-column cost cap is dropped, Part 2 §2.3.3); set = this section.

**The rule.**
1. A set is a recipe of **3 or 4 named techniques**. Troubleshooter: 179 of 181 Fandom recipes are exactly four (V, `fandom_wiki.md:27`); the TroubleMaster data has 602 four-part and 9 three-part sets (FAN, `troubleshooter_characters.md:94`).
2. **Held together on one board, the set adds exactly one effect none of its members has: an open gate (§3.1.1) or a board rule.** Never a factor, never a bonus, never a stat. This is the one place this proposal departs most from its model: Troubleshooter's sets "both (a) buff/reshape the named component masteries and (b) add [their] own flat stat bonus" (V, `fandom_wiki.md:1090`), and many force an outcome ("always hit", "always a critical hit", V, `fandom_wiki.md:1101-1108`). A set filed under a tradition that added a factor would be a tradition weight by another name (ED-PC-0023); one that forced an outcome would be fiat.
3. **A set is a composition of atoms, not a tradition's property.** Whoever holds the members gets the effect, whatever their traditions. Filing it under a tradition is presentation (the curriculum shows it as that school's goal). So a cross-trained fighter can complete a set, and no rule names a tradition.
4. **Recipes are visible from the start**, in the curriculum. Troubleshooter hides them until discovered (V, RPG Codex thread, `troubleshooter_combat_reception.md:98`), and players report hours of permutation ("Doesn't want to permutate 500+ combinations and lacks training manuals", FAN, `discussions_builds.md:165`) and guide-building instead of experiment (FAN, `discussions_builds.md:307`). A visible goal is what makes a set legible (§0.06 E: "intuit complex outcomes from simple choices").
5. **Ceiling (NERS-E): at most three sets per tradition, each a goal a player can state in one sentence.** Troubleshooter's 481 acquired recipes on one save (V, `guide_1349483727_images.md:149`) and a player's "Picking from 30 options is fun, picking from 130…" (FAN, `discussions_builds.md:244`) are the warning.
6. **Pairwise relations, reconciled with sets.** The earlier draft's three relations (`kits_draft.py:294-334`): `requires` **stays** (an acquisition prerequisite, host-side). `widens` **is retired into sets**: a widening that needs two techniques is a two-member recipe, and n-ary covers it (IT-3 becomes set `S-IT-1` below). `branch` **is not a board relation**: the follow-up depending on bind state is behaviour inside the module and would be a lever design (two levers keyed by state), deferred with PC-08.

## 3.4 Techniques and sets per tradition

Codes. **Status:** `LIVE` in `ABILITIES` today; `DRAFT` from `kits_draft.py` on a live lever; `DRAFT·NL` from `kits_draft.py` on a lever not yet built; `NEW` invented here on a live lever; `NEW·NL` invented here, lever not built. **Origin (Addendum 6, a label, not a gate):** `INSP` inspired by the named source, with the earlier draft's verification code carried (`V` read in a modern translation, `C` carried from the repo, `U` unverified); `INV` design invention; `RECALL` inspired by my own unverified recollection of the tradition.

| tradition | fixed baseline | lines (→ is teaching order; a `requires` is named where it exists) | sets (members → effect) |
|---|---|---|---|
| **German** (Liechtenauer) | `staerke_schwaeche` LIVE · INSP Liechtenauer v.18 (V) | bind: `fuehlen` DRAFT (C) → `staerke_schwaeche` → `indes` LIVE (`indes` requires `fuehlen`, DE-1, C) · counter: `zwerchhau` LIVE (C) → `nachreisen` DRAFT·NL (V, v.24) · grapple: `ringen_am_schwert` LIVE (C) | **S-DE-1 "Feel, then answer in the same instant"**: `fuehlen` + `staerke_schwaeche` + `indes` → open `steal_shallow` (INSP Ringeck gloss "simultaneously", snippet only; the gate mapping INV). **S-DE-2 "Wrestling at the sword"**: `ringen_am_schwert` + `fuehlen` + `staerke_schwaeche` → open `grab_close` (INV) |
| **Italian** (Fiore → Capoferro) | `misura` LIVE · INSP Capoferro (V) | measure: `misura` → `mezzo_tempo` LIVE → `contratempo` DRAFT (both require `misura`, IT-1/IT-2, V) · footwork: `volta` DRAFT·NL (C) · refusing the bind: `cavazione` DRAFT·NL (held by the draft as its weakest mapping) · grapple: `abrazare` DRAFT·NL (V) | **S-IT-1 "Counter-time at narrow measure"**: `misura` + `mezzo_tempo` + `contratempo` → open `counter_shallow` (the draft's IT-3, V for the term, its note: the deep-commit gate "is the repo's, not the treatise's"). **S-IT-2 "Refuse the bind"**: `misura` + `cavazione` + `volta` → open `withdraw_band` (INSP the decomposition's bind-refusal identity, archived vocabulary; INV mapping; two members need levers built) |
| **Spanish** (Destreza) | `atajo` LIVE · INSP (C, S2/S3) | geometry: `circulo` DRAFT (C) → `compas` DRAFT (C) → `atajo` · profile: `perfil` held (lever fits, measured near-inert, draft `HELD`) | **S-ES-1 "Occupy the line, then take the time"**: `circulo` + `compas` + `atajo` → open `steal_shallow` (INV; two schools reaching one door by different members is the point of §3.3 rule 3) |
| **English** (Silver) | `true_times` LIVE · INSP Silver (V) | `true_times` → `four_governors` DRAFT·NL (term V, mechanism U) · `gardant` NEW·NL on `guard_prior_parry` (a site PC-21 owns, Part 2 §2.3.1 note) (INSP Silver names the guardant fight, V; what it does mechanically is INV; the draft held it for want of a source, which Addendum 6 lifts) | **S-EN-1 "True fight"**: `true_times` + `four_governors` + `gardant` → board rule: +1 slot in *Defence and counter* (INV) |
| **Japanese** (koryū) | `shinogi` LIVE · INSP (C) — acts only with a single-edged blade (`WP.spine`) | reading: `metsuke` DRAFT (C) → `sen_no_sen` DRAFT (C) · answer: `kiriotoshi` DRAFT·NL (C; on `guard_prior_parry`, a site PC-21 owns, Part 2 §2.3.1 note) · `zanshin` DRAFT (C) | **S-JP-1 "Cut down and through"**: `shinogi` + `kiriotoshi` + `sen_no_sen` → open `counter_shallow` (INV). **S-JP-2 "Remaining mind"**: `metsuke` + `sen_no_sen` + `zanshin` → board rule: +1 slot in *Reading* (INV) |
| **Chinese** (Ming spear and sword) — authorable under Addendum 6 | `lan_na` NEW on `leverage`: the circling parry that controls the line (RECALL: the spear's "block, seize, thrust" sequence) | spear: `lan_na` → `zha` NEW on `counter_success`: the straight thrust out of the circle (RECALL) · sword: `zhan` NEW on `tactile`: sticking to the opponent's blade (RECALL) | **S-ZH-1 "Block, seize, thrust"**: `lan_na` + `zha` + `zhan` → open `counter_shallow` (INV) |
| **Filipino** (continuous flow) — authorable under Addendum 6 | `flow` NEW on `tempo`: continuous striking without a reset (INSP the roster's own `mode` label, `traditions.py:21`; RECALL) | `flow` → `live_hand` NEW on `tactile`: the empty or second hand checking the opponent's arm (RECALL) · `triangle_step` NEW on `balance`: angled footwork (RECALL) | **S-PH-1 "Live hand"**: `flow` + `live_hand` + `triangle_step` → open `grab_close`, which in the engine is where disarms already live (`capabilities.py:64-68`: disarm is a branch of the universal grab menu) (INV) |
| **none** | none | no curriculum; may learn the generics (§3.5) | none |

**What the table is not.** It is not content Jordan has approved (plan rule P11: content is Jordan's). It is a worked example of the *mechanism*, filled densely enough that a sheet can be generated from it. Every `NEW` and `INV` entry is `[ASSUMPTION; low; Jordan to correct]`.

**Counts, so the NERS-E ceiling can be checked:** each tradition has 1 fixed baseline (counted among its techniques), 3–6 techniques and 1–2 sets. German and Italian are the largest (6 techniques, 2 sets each); `sheets.py --curriculum` prints the counts from the data. No tradition reaches the three-set ceiling.

## 3.5 The 21 generics: tradition-neutral stock

Today the generics are dealt to traditions by a Latin square, three each, including Chinese and Filipino (`ability_primitives.py:84-129`), and the square **raises `ValueError` at import if a tradition is added** (`:113-114`; the draft's decision 4, `00_tradition_sets.md:121`). They are calibration instruments with plain names and no period term (ED-PC-0059, PC-17).

**Proposed: the generics become a shared stock any person may learn, filed under no tradition** (Troubleshooter's "Common" masteries are the shape: `guide_2037290423.md` §4e lists Common masteries any class equips). Consequences: a person with no tradition gains a path (self-taught drill); the import-time coupling to the roster dies, so an eighth tradition no longer needs the generics retired first; the calibration role is unchanged. This edits the gate in `_invested`, which B18.02 already moves host-side; after B18.02 it is an authoring-data change, before it a module change. **This is decision D-8 (Part 9); before B18.02 it is module edit M-4 in the head.**

## 3.6 Mixing across traditions

| a second tradition may lend | it may not lend |
|---|---|
| any of its techniques, equipped into the board's columns at the person's own levels | its fixed baseline (that is the foundation of the person who grew up in it) |
| membership of any set, by holding the members (§3.3 rule 3) | the person's identity for familiarity: an opponent reads the person by their primary tradition. Whether cross-training changes how *they* read the second school is familiarity grown in the season, which is **PC-21's design**, not this one |
| | a third tradition: a third needs the threshold met in the second, not the first (Pathfinder 2e's dedication chain, [V: AoN, `precedents_other.md` §4.2]: "can't select a different dedication feat until you complete your dedication by taking two other feats") |

- **The threshold [ASSUMPTION; low]: three techniques at level 3 or more in the current tradition** before the next may be taken. Pathfinder's lockout is described by its own players as "a universal safety valve for balance concerns" [FAN, `precedents_other.md` §4.2]; here it is a pacing rule, not a balance rule (the fiat audit rules out balancing by restriction).
- **Mixing is cheap and visible.** Generics are free to all (§3.5). A second tradition is one threshold away. Sets complete across schools. This is the brief's "very flexible" stance (Addendum 7), with the tradition kept as the curriculum a person grew up in rather than a wall.
- **What the engine sees.** Nothing of the mix. After B18.02 the module receives composed numbers per slot; today `known_traditions` would be the input that unions the kits (`ability_primitives.py:174-177`). Either way no line of `modules/` names a tradition pair.

## 3.7 Falsifiers for this part

1. **A set adds no magnitude:** with a set complete and its gate closed in the authoring data, every lever slot equals the sum of its members' contributions alone. Runnable on the composer.
2. **No special case:** `git grep` over the composer for any tradition name returns nothing; traditions appear only in authoring data.
3. **A gate opens only availability:** with `counter_shallow` open, the counter's success probability for a given (defender, commit, read) is unchanged; only the count of attempts rises. Runnable on the module the day the gate exists.
