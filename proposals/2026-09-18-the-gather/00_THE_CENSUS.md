# 00 · THE CENSUS — every tree in `proposals/`, measured

## Status: **MEASURED (2026-09-18). This file asserts no verdict.** Dispositions are `01`.
## Method: one batched read-only measurement lane (Haiku, `valoria-measure`, no write tools), re-runnable from the commands in the tables. Every number carries the command that takes it (`CLAUDE.md` §0.1 pt 3).

---

## §1 · The whole tree

| metric | value | command |
|---|---|---|
| total files under `proposals/` | **553** | `find proposals -type f \| wc -l` |
| total lines, `.md` only | **175,079** | `find proposals -type f -name '*.md' -exec cat {} + \| wc -l` |
| `## Status:` lines | **272** | `grep -rh '^## Status:' proposals/ \| wc -l` |
| …containing `RATIFIED` | **3** | `grep -rh '^## Status:' proposals/ \| grep -c RATIFIED` |
| …containing `PROPOSED` | **195** | `grep -rh '^## Status:' proposals/ \| grep -c PROPOSED` |
| …containing `HELD BACK` | **107** | `grep -rh '^## Status:' proposals/ \| grep -c 'HELD BACK'` |

⚠ **`CLAUDE.md` §3 quotes 550 files / 263,919 lines / 2 of 271 RATIFIED, and the difference is a
PREDICATE difference, not drift.** 263,919 counts every file; 175,079 counts `.md` only. Both are
right about different questions. The RATIFIED count genuinely moved 2 → 3. **Quote a predicate with
every one of these numbers or do not quote them.**

## §2 · The fourteen trees

| path | files | lines | held back | ids declared in its index | code? |
|---|---|---|---|---|---|
| `2026-08-28-greenfield-systems-suite/` | 12 | 3,908 | NO | ED-1094, ED-IN-0196/0200/0201/0103, ED-SC-0032 | no |
| `2026-09-03-governance-corpus-rebuild/` | 7 | 7,462 | NO | **none** | no |
| `2026-09-04-degree-sweep/` | **95** | **60,578** | YES | ED-PC-0036 | yes |
| `2026-09-04-social-contest-branches/` | 15 | 7,751 | YES | ED-SC-0002/0015/0020/0021, ED-1057/1059/1062 | no |
| `2026-09-05-proceedings-subsystem/` | 46 | 19,835 | YES | none in index | yes |
| `2026-09-10-settlements-factions-populations/` | 7 | 2,842 | YES | ED-SE-0051, ED-IN-0203/0204/0206, ED-1094 | no |
| `2026-09-12-emergent-narrative-primitives/` | 7 | 2,756 | YES | ED-IN-0214/0217, ED-1094 | no |
| `2026-09-12-emergent-narrative-primitives-v2/` | 5 | 1,731 | YES | ED-IN-0210/0217/0218, ED-1094 | no |
| `2026-09-16-conviction-decision-layer/` | 8 | 2,621 | YES | none in index | yes |
| `2026-09-16-term-ownership/` | 3 | 1,830 | NO | **none** | yes |
| `2026-09-17-governance-and-behaviour/` | 5 | 4,216 | YES | ED-IN-0243/0244/0245, ED-WR-0011, ED-1094 | yes |
| `2026-09-17-governance-and-holdings/` | 8 | 5,965 | YES | ED-IN-0233..0237, ED-SE-0052/0053 | no |
| `2026-09-17-governance-and-holdings-r2/` | 8 | 9,134 | YES | ED-IN-0233..0237, ED-SE-0052/0053 | yes |
| `2026-09-18-character-decision-layer/PROPOSAL.md` | 1 | 352 | YES | ED-IN-0075/0210/0245 | no |

**These fourteen are 130,981 of the 175,079 `.md` lines — 75%.** The remaining 25% is the loose
`.md` files at the root of `proposals/` and the pre-08-28 suites.

## §3 · Inbound references — which trees anything actually reads

Counted as string occurrences of the directory's basename, outside its own directory.

| tree | from `proposals/` | from `workplans/ registers/ engine/ CURRENT.md HANDOFF.md` |
|---|---|---|
| `2026-09-17-governance-and-holdings-r2` | **54** | 13 |
| `2026-09-16-conviction-decision-layer` | **38** | 9 |
| `2026-09-17-governance-and-holdings` | 37 | 19 |
| `2026-09-10-settlements-factions-populations` | 5 | 3 |
| `2026-09-17-governance-and-behaviour` | **1** | **20** |
| `2026-09-18-character-decision-layer` | **0** | **1** |

**Two readings this table supports and `01` acts on.**

1. **`governance-and-behaviour` is the tree the REST OF THE REPO reads (20) and `proposals/` does not
   (1).** That is the signature of an orchestrating document: it points outward and nothing inside
   the corpus depends on it. It is the precedent this gather follows.
2. **`character-decision-layer` is read by nothing, anywhere, but one row.** It landed 2026-09-18 and
   declares itself *"a queue by construction"*. An orphan one day old.

## §4 · The two trees with NO `## Status:` line anywhere

`2026-09-03-governance-corpus-rebuild/` (7,462 lines) and `2026-09-16-term-ownership/` (1,830 lines).
⚠ **Neither can be dispositioned by reading a status line, because neither has one.** The corpus
rebuild's `README.md` carries the equivalent in prose — *"Status: PROPOSAL. Nothing here is ratified"*,
as a `**bold**` line rather than a `## Status:` heading, which is why the grep misses it. `01` reads
them by hand and says so.
