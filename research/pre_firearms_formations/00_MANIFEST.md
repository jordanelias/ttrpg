# Pre-Firearms Military Formations — Research Manifest
**Project:** Valoria game research · external (no repo write)
**Scope:** Pre-firearms / pre-shot grand formations & unit formations across history, weighted toward Renaissance era (~1450–1525) and immediately prior (~1100–1450), with full coverage of antecedents and parallels.

## Deliverable Tasks

1. **Catalogue** — exhaustive formation inventory across eras.
2. **Strategy & tactics** — why formations were arranged as they were.
3. **Matchup efficacy** — formation-vs-formation outcomes; generic conclusions.
4. **Battle-phase choreography** — granular unit position / trajectory / timing / speed through phases.

## Vocabulary (per Jordan's spec)

- **Grand formation** = sum of an army's spatial organization, movement, and strategies.
- **Unit formation** = the spatial organization, movement, and tactics of a sub-grouping with a specific role.
- **Unit** = troops comprising a sub-formation.
- **Strategy** = high-level / holistic approach to solving a problem.
- **Tactic** = granular / atomic approach to a constitutive piece of a problem.

## Chunk Plan

| Chunk | File | Era / Scope | Weight |
|---|---|---|---|
| A | `01_ancient.md` | Ancient (~3000–500 BC): Sumer, Egypt, Assyria, Hittite, early Greek, Achaemenid, Steppe | low |
| B | `02_classical.md` | Classical antiquity (~500 BC–500 AD): Greek phalanx mature, Macedonian, Hellenistic, Roman manipular & cohort, Carthaginian, Parthian/Sassanid, Han China, Mauryan/Gupta | medium |
| C | `03_early_medieval.md` | Early medieval (~500–1000): Byzantine, Arab/Umayyad/Abbasid, Carolingian, Viking, Anglo-Saxon, Tang/Song, Heian Japan | medium |
| D | `04_high_medieval.md` | High medieval (~1000–1300): Norman, Crusader, feudal Europe, Seljuk/Ayyubid, Mongol, Song/Jin, Kamakura Japan, Khmer | high |
| E1 | `05_late_med_renaissance_europe.md` | **Late medieval & Renaissance pre-firearms Europe (~1300–1525)**: Swiss, Landsknechte, English longbow, Hussite, Flemish, Scottish, Burgundian, condottieri, French gendarmes, early tercio precursors | **MAX** |
| E2 | `06_renaissance_islamic_steppe.md` | Renaissance-era Islamic & steppe: Ottoman pre-firearm, Mamluk furusiyya, Timurid, Safavid Qizilbash, late Mongol successors | **MAX** |
| E3 | `07_renaissance_east_asia.md` | Renaissance-era East Asia: early Sengoku Japan, Ming, Joseon, Đại Việt | high |
| E4 | `08_pre_columbian.md` | Pre-Columbian Americas: Aztec, Inca, Maya, Mississippian, Tarascan | medium |
| F | `09_throughlines.md` | Throughlines & meta-throughlines synthesis | (final) |

## Per-Chunk Entry Template

For each formation:
- **Name** (and aliases)
- **Era / civilization / first attested**
- **Composition** — what units comprise it
- **Geometry** — frontage, depth, intervals, alignment
- **Equipment dependency** — what weapon/armor mix it requires
- **Tactical role** — what problem it solves
- **Strategic context** — why it emerged when it did (ground, threat model, recruitment base)
- **Vulnerabilities** — what defeats it
- **Notable engagements** — battle references
- **Throughline flags** — patterns to revisit in Chunk F

## Working Discipline

- One chunk per turn (sometimes grouped if light).
- Inline summary at top of each turn: what was added, key takeaways, throughline candidates.
- File saved before inline summary written (avoids loss on persistence drop).
- Checkpoint prompt at end of each turn: continue / pause / pivot.
- No commits, no repo writes; pure research.

## Status

- `[2026-05-14]` Manifest created. Chunk A in progress.
