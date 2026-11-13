# Workplan v12 — head decisions the patch lane hands to H2

## Status: WORK FILE (the patch lane's (b) class of `H2_NOTES.md`; resolves nothing at runtime; deleted when v12 is adopted)

Each row is a decision only H2 (the head tables, `V12_STRUCTURE_part2.md` §7.2 to §7.9) can make: an edge, a merge
order, a mover tag, a census row, a held or blocked row, a dial, a head rule. "Ladder" is CLAUDE.md §0's five
steps. "Script" means the appendix's script, run on the parts as they stand after the patch lane's edits
(P-01 to P-33, `PATCH_LOG.md`). The script reads three edge sources: S, `V12_STRUCTURE.md` §2.1's `after`
column (383 edges once B16L and B16M are told apart); G, every part's `GATE: Batch` lines (12 edges S lacks);
D, batch names inside `DEPENDS ON` lines and the "gates on" cells of position tables (177 edges S lacks, many
of them forward notes, not dependencies). **S and S+G are acyclic. The longest path under S is 22 waves past
B00, and the same under S+G.** G already moves three batches later than §2.1 says: B08 from W6 to W9, B30 from
W17 to W18, B31 from W16 to W18. None of them is on the critical path, and the schedule's steps (B08 S13,
B30 S18, B31 S19) already sit at or after those waves. S+G+D is cyclic, through D's forward notes (for example
"V12 Batch B28 (…) lands later" in a B24 item, or "the fatigue write V12 B22" in a B17 item). The D edges that
point backward are listed under HD-17, each checked by opening its line.

| id | the decision | evidence | author's recommendation | patch lane's recommendation (ladder step) | batches |
|---|---|---|---|---|---|
| HD-01 | edge B11 → B16 | part 23 `GATE: Batch B11` (`IS-PC-01` registers in B11's `SCENARIOS`); script: no cycle, no wave moved | add (A23) | **add** to §2.1 (step 5: a gate line already in the part) | B16 |
| HD-02 | edges B04, B05, B06 → B08; merge order in S13 | part 23 GATE lines (lap rename, one sampler, keyed draw); script: B08 moves from W6 to W9, inside its 12 steps of slack; S13 stays | add; B08's earliest wave is W9; H2 recomputes slack; B08 merges first in S13, B16 rebases (A23) | **add**; B08 before B16 in S13 (step 4: §7.4's rule for two movers in one step) | B08, B16 |
| HD-03 | edge B11 → B21 for `IS-B3-FA-01` | script: no cycle, but **+1 wave** (max 22 → 23; B21, B21b, B21c, B21d, B21s, B24a, B27, B28 and the tail move) | not in the after-list; the item carries a `STOPS IF` that falls back to B23 (A15) | **no edge.** B11 and B21 both open in S12: the coordinator merges B11 first and B21 rebases (§7.4). The item's `STOPS IF` stays as the guard (step 5: a wave on the critical path for one item) | B21, B23 |
| HD-04 | edge B12a → B21b (`09_WR_world_motion` edit 2 under B21b.06) | script: no cycle, **+1 wave**, so 26 steps against A21's 25-step limit | add if there is no cycle and the critical path stays ≤ 25 steps; otherwise keep the STOPS IF (A21) | **no edge, by A21's own rule.** B12a and B21b both open in S13: B12a merges first, B21b rebases, and B21b.06's STOPS IF stays | B21b |
| HD-05 | edge B16 → B34 (B34.15 and B34.17 need `duel_scene`) | part 25 GATE line; script: no wave moved | add to §2.1; waves unchanged (A25) | **add** | B34 |
| HD-06 | edge B28 → B32 (`covenant_in_force`, `OBEYED_WRIT` for B32.04) | script: **+1 wave** (B32 and every batch after it) | A34: H2 decides, B32.04 carries a STOPS IF; A35: no edge, B28 merges before B32 in S17 and B32 rebases | **no edge.** In S17, B28 merges before B32 (A35's reading; step 4, §7.4) | B28, B32 |
| HD-07 | edge B22 → B30 (`field_scene.py` edited B20 → B22 → B30) | part 37 GATE line; script: B30 moves from W17 to W18, which is S18, already its step | add (A37) | **add** | B30 |
| HD-08 | edge B25 → B27 (`IS-B2-SC-07` step 2, B27.17) | script: **+1 wave** | add the edge (one wave on the critical path) or land B27.17 in B32; written in full, HELD (A31) | **no edge; B27.17 moves to B32's tail.** B32 is already after B25 and B27, so no wave moves (step 5). The move is H2's at the merge, not this lane's | B27, B32 |
| HD-09 | edge B29 → B19 (B19.60, named captives into custody) | script: no cycle, no wave moved (B29 is W14, B19 W15) | add to §2.1 (A27) | **add** | B19 |
| HD-10 | edges B17 → B41 and B20 → B41 | script: no cycle; B20 → B41 moves B41 from W15 to W17, inside its 7 steps of slack | add both; the affected items carry STOPS IF (A29) | **add both**; B41 leaves S15 and opens at S17 or later; the schedule row changes | B41 |
| HD-11 | edge B29 → B37 (HAP_C and HAP_D need custody) | script: no cycle, no wave moved | add; B37 carries DEPENDS ON with a STOPS IF (A32) | **add** | B37 |
| HD-12 | edge B34 → B20 (IS-MB-01 step 4, B20.21) | part 30 GATE line; script: no wave moved | added by A30; B34.18 is a POINTER (A25) | **add** to §2.1 | B20 |
| HD-13 | edges B21d → B40 (PAP-F needs CR-88) and B21d → B33 (CR-88's duty decline) | script: no cycle, no wave moved | B40: the item takes the source's fallback, H2 decides (A43); B33: add, costs no step (A38) | **add both** | B33, B40 |
| HD-14 | edges B27 → B28, B24a → B21s, B29 → B21s, B21s → B33 | three of them are part 35 GATE lines; script: no cycle, no wave moved | add all four; none moves a wave (A35) | **add all four** | B28, B21s, B33 |
| HD-15 | edges B20 → B31 and B22 → B31 | part 39 GATE lines; script: B31 moves from W16 to W18 (S19 in the schedule) | B31 has two extra GATE lines (A39) | **add** | B31 |
| HD-16 | edge B24a → B28 (B28.33, CR-61's citation, P-28) | script: no cycle, no wave moved | — (new with P-28) | **add**; until then B28.33 has a STOPS IF | B28 |
| HD-17 | B24a's items read B12c.13, .14, .16 and .17 (part 28_cont `:262`, `:276`), and §2.1 has no edge B12c → B24a | script: **+1 wave** if added | — (found by the script) | **no edge.** Both open in S15: B12c merges before B24a, which rebases (§7.4). The other backward D mentions were each opened and are forward notes or merge baselines, so none needs an edge: B17 → "B22's fatigue write"; B21.77 POINTER → B21c; B11 → B24, B25 (moved arms); B12a → B35 (a dial); B24 → B24a, B28; B34 → B12c (`valley`, with a fallback); B19 → B20 (B19.27, B19.52, both owned by B20); B18 → B12c (different keys in one step); B22 → B23 (`passage_granted` read as "no leave"); B30 → B23 (the merge baseline: B23 before B30 in S18, A37); B36 → B38 (readers named); B03 → B09, B41 (named, "not depended on") | B12c, B24a |
| HD-18 | merge order in S4 and S6; B04's rebase | part 6: "S4: B03g, B03c, B16L. S6: B13 and B16M before B04; B04 must re-run `export_composition.py` and `export_sim_params.py --build` after its rebase" (A06) | as stated (A06) | **take A06's order.** Part 7's PARALLEL line now says so (P-32) | B03g, B03c, B16L, B13, B16M, B04 |
| HD-19 | merge order in S18: B23 before B30 (both edit `seam/wrappers/mass_battle.py::resolve`) | part 37_cont B30's RE-PIN and DEPENDS ON | B23 merges first, B30 rebases (A37) | **take it** | B23, B30 |
| HD-20 | mover tags §2.2 and §7.1 must change | B03 is a mover: encoding at B03.28, behaviour at B03.86 (A04, A05; the re-pin text is P-19). B05 has 9 behaviour movers and 1 encoding mover, B05.20 (A08). B10.32 is a behaviour mover (A12). B32's `Office.audit_at_exit` is an encoding mover (A34). B36 is a mover (`thread_read` `referent_class: Site`, A39). B40 is a behaviour mover (the grounding rows, A43). B21d.05 is a mover, and .07 to .09 if kept; B11F1 .02, .04 and .05 are movers; B41 is hash-EQUAL (A29). B38's movers are listed by A40. B34's `Scene.cost` moves no hash (A25 corrects D-04's tag). B19a and B11F2 are EQUAL | as stated per author | **retag each** in the batch table and the hash-mover table (step 3: each part's own block is the record) | B03, B05, B10, B32, B34, B36, B38, B40, B21d, B11F1 |
| HD-21 | file census rows | B05 also edits the combat files, `combat_engine_v1.json`, `options.py` and `data/rosters.py` (A09). B05 adds the seat `modifier:` with no U3 member row (A08). B35 adds `epistemic.py`, `budget.py`, `boot/realm.py`, the new host, `modules/threadwork/` and the geography file (A36). The `harness/play_surface.py` row reads B34 → B41 → B38 → B39 (A42). B21 adds `loop/sides.py`, `loop/effects_shared.py` and `tests/test_march.py` (B21.79, P-24), and B21b edits the same three files later | as stated | **add the rows** | B05, B35, B34, B41, B38, B39, B21, B21b |
| HD-22 | Layer 1 gate nodes for B11.04 (`04` §C.6, CR-29) and B41.03 (`04` §C.12): `U3_LAYER1_AMENDMENTS.md` has no node for either | `registers/editorial_ledger_in.jsonl` ED-IN-0300's superseding row (ratified): "an agent may land unmarked `CLAUDE.md` and `architecture/` text in the PR, stated openly in the PR body, and text marked (RULED) stays Jordan's"; M11's "new row in ratified 04 section C.6" is read as yes `[ASSUMPTION; medium]` in that row | H2 adds a node or confirms the ED covers it (A16, A29) | **the ED covers both (step 1).** Add one node per item to the Layer 1 amendment status table, citing ED-IN-0300. Each item's first step checks that the row it edits carries no (RULED) mark, and the PR body states the text. A (RULED) row makes the item HELD for Jordan | B11, B41 |
| HD-23 | held-back list (§8.2) and PR-body asks | B03.19 (the Layer 1 rejection-5 paragraph) and B03.69 (A04, A05); the `CLAUDE.md` preamble sentence (A06); `U5b_MB_residue` §2 R-38, a Layer 1 text edit (A11); the GO-09 workflow line, since Jordan owns the workflow file in CODEOWNERS (A06); `04` §B.3 `Rung.envelope` (A24, now J-01 in `V12_FOR_JORDAN.md`). PR-body picks: `YIELD_OB` and the `mortal_wound_ob` sweep's pick (A18). Content drafted for Jordan's correction (D-19): `troops.yaml` seeds (A11), the `wound` kind `harbour` (A19), `tables.territory_weight` (A15), the `caste_practice` and `riot` cells (A41), the 46 ages (A32), `secondary` (A39), and the ARC-47 case values (B39.37, P-25) and the two `unaware:` marks (BA1.12, P-30) | as stated | **list each** in §8.2 and in its batch's PR body | B03, B12b, B15, B17, B19, B12a, B21, B38, B37, B31, B39, BA1 |
| HD-24 | B03.69 (`off_npc_084`, the guild leader, has `rung` None; the stored `scale:` column waits on it) | part 5 B03.69: BLOCKED "Jordan: the seat's rung is content". D-19, as A18 applied it: "D-19 overrides 'batch not opened until Jordan supplies values'" | BLOCKED on Jordan (A05) | **not a Jordan question (step 4, D-19's precedent).** The plan drafts the seat's scope as `status: seed` content, listed in B03's PR body, and the item lands; Jordan corrects the value, not the plan. If H2 keeps the intake's "settled: owner Jordan", the row stays HELD with its trigger | B03 |
| HD-25 | B35.28 `knot`'s effect: no WR design writes it, and `IS-A-08` would stop B35 if `knot` reads not built out | part 36 B35.28 (A36) | decide: a WR design item before B35, or accept the residue (A36) | **a DESIGN-FIRST item in B35 before B35.28** (step 4: E-14 and D-18: ship the machinery at control with a design-first follow-up; B35 already opens with design items .01 and .02). Accepting the residue would close a batch that IS-A-08 says fails | B35 |
| HD-26 | readings past the two-season cap | the scar flip and `scar_weight_shift`: `02_CHAR_scar_is_a_wound` gate (b) reads at eight seasons and is 0 by construction at two (A12). The Church Influence flips need season 3 or later (A29). `claim_fade` edit 5 (`MAX_SEASONS` 16, A11). B39.18 docket (A42). HAP_D G-1(ii) (A32) | A12: decide. A29: BLOCKED in B98, or left to B99 | **B99, the longer re-take (step 4, A-114: "one longer re-take of the nine as the very last item")**. In B98's table each one is `BLOCKED (A-114: past two seasons)` with its target, and B99 reads it | B98, B99 |
| HD-27 | `release` stays in `contest_owed` with no owner | part 34 UNDECIDED (9): "`release` is attributed there to `14_VERBS_BINDING_B`, which gives `release` no `contests:`"; part 10_cont2 UNDECIDED (1): the loader refuses only a member that declares `contests:` | H2 names an owner (A34) | **B32's BIND_B item** (its source is the row's shape owner) moves `release` out of `contest_owed` into the class its row has (task route or `bookkeeping_verbs`) in the commit that edits the row. Until then the roster accepts it. Step 4: a row's shape is owned by its shape file | B32 |
| HD-28 | CR-103: held in B11F2, or B21s's last item | part 32 (A32) | held in B11F2; the other reading (E-8) makes it B21s's last item; H2 and A35 decide (A32) | **held in B11F2**, as written. A35's part carries nothing for it (B21s has two items and its `.99`, none of them CR-103), so moving it would be a new item with no author. Its three dials stay BLOCKED in B98 while it is held | B11F2, B21s, B98 |
| HD-29 | ED-606 and ED-607 in the held table: is the trigger B30's nesting or "a zoom stack is built"? | part 37 (A37): B30 builds a nested contest at depth 1, not a zoom stack | H2 decides (A37) | **the v11 row's trigger stands** ("a zoom stack is built"): B30 does not meet it (step 1: the later B30 text does not supersede the row). Held, trigger unchanged | held table |
| HD-30 | id blocks | three npc_registry case ids (A42); an NPC lane block for B33 (A38: "NPC 1"); ED-MB-0016's superseding row keeps its id (A27); the T-11 collision is resolved as T-19 (A26, A27) | H1 allocates | **H1 adds both blocks** to the per-batch id table; no other change | B39, B33 |
| HD-31 | glossary checks | `regime` against `CreedBody`, `creed_bodies`, `creed_relation` (A40, A-94); a second sense of "spell" (B12b.03's weather, A32); "rival" in `rival_gain` (A13) | H2 checks | **check against `unified/U1_GLOSSARY.md`** at the head's glossary pass | B38, B12b, B37, B10 |
| HD-32 | forward rules for H1's head | after B08.02, every keyed refusal row in `verb_table.yaml` carries a `sequence:` key (A23). After B41.11, any batch that adds a verb or an Event kind adds its `names_index.yaml` entry in the same commit (A29). Every item that gives a verb `contests:` deletes it from `contest_owed` (A10): all owners now do so (B21.09 and B21.14 P-11; B26.11 P-12; B23.14; B25.14; B28.06 and B28.09; B32.26; `release`, HD-27) | as stated | **write all three** in the head's rules | head |
| HD-33 | carriers that no item builds (H2's held or blocked table, §7.9) | PB step 3d, the `measure` lean (A23); a writer of a `capability:` claim about another person (B04.22, A07); GO-06 (A06); HEAR_B edit 8's cost terms and CR-92's builds (A22); IN-58 (B09.20, A11); the FA/SE upkeep payment path (A39); a "contrary Propositions" reader (A35); `held_edge_declines` (A41); `state/gate.py::judging_set` (A43); BYZ-G item 2's place filter (B40.13, A43); the `conclusion_product` fixture (A17); `holders_named`, `notice` and `pool.py::score` (A28); TL-B5.2's standing gate (A21); the SC `recites` branch (B32.10, A34 and A35); CP-T09-05's `deed:rung.ceded` cell and H-209 (A21); `world_q.passage_granted` is not missing: B23.05 builds it (checked) | BLOCKED or MISSING, per author | **one held-table row each, with its owner lane.** None of them is a Jordan question: each owner lane designs it (step 5) | many |
| HD-34 | head table order | B10.51 to B10.53 (three design items) land at B10's open, before B10.01 (A13). B38.51 and B38.52 land at B38's open (A41) | list them first (A13, A41) | **list them first** in the position tables H2 builds | B10, B38 |
| HD-35 | estimates (E-15) | B04: 13 h against §2.2's 7 h (A07). B19: 12.5 h (A27). B28: 16 h; B21s: 3.7 h (A35). B39: 19 h (A42). The patch lane added positions: B21 +5 (B21.79 to B21.83), B15 +1, B28 +1, B39 +1, BA1 +1 | — | **recompute** the critical path from the position counts, which now include the patch lane's positions | B04, B19, B21, B15, B28, B39, BA1 |
| HD-36 | B02.07: in B02 only if the MB lane agrees, otherwise in B17 | part 3 B02.07: "HELD (the MB lane's file: lands in B02 only with that lane's agreement, else in B17)" | B02, conditional (A03) | **B17 if the MB lane does not agree by B02's open** (step 5: the test file belongs to the MB lane, and B17 is the MB batch that edits it). B02.07 is written HELD with that trigger; H2's held table names B17 as where it lands | B02, B17 |
| HD-37 | `test_24d_i_…moves_no_question_in_one_season` is not in the tree (A29) | part 29 | — | **the item that names it writes it first** (E-3); no head row | B41 or B21d |

## Appendix A — the script (kept, not committed elsewhere)

Run from `master/workplan_v12/` as `python3 edges.py . proposed.txt`. `proposed.txt` holds one `A B` pair per line:
HD-01 to HD-17's edges.

```python
"""Edge check for H2_DECISIONS.md: build the batch graph from V12_STRUCTURE.md §2.1's `after` column (S),
every part's `GATE: Batch` lines (G) and item-level batch mentions in `DEPENDS ON` lines and position-table
`gates on` cells (D); report cycles; then add each proposed edge and report acyclicity and wave change."""
import re, glob, sys, itertools
D_ = sys.argv[1]
H = r'B(?:A1|\d\d(?:[a-z]+\d?|F\d|L|M)?)'          # a batch number: B00..B99, B03g, B21b, B11F1, BA1, B19a, B37p, B16L
def short(h):
    m = re.match(r'(BA1|B\d\d(?:[a-z]+|F\d|L|M)?)', h); return m.group(1) if m else None
nodes, S = set(), set()
for l in open(f'{D_}/V12_STRUCTURE.md'):
    m = re.match(r'^\| (\S+) \| [A-Z+]+ \| W\d+ \| S\d+.*?\| \d+ \| (.*) \|$', l)
    if not m: continue
    b = short(m.group(1)); nodes.add(b)
    for a in re.findall(H, m.group(2)):
        a = short(a)
        if a and a != b: S.add((a, b))
nodes |= {'B98', 'B99'}
G, Dp = set(), set()
for f in sorted(glob.glob(f'{D_}/workplan_v12_part*.md')):
    cur = None
    for l in open(f):
        m = re.match(r'^## Batch (\S+)', l) or re.match(r'^### (' + H + r')\.\d+', l) or re.match(r'^\| (' + H + r')\.\d+ \|', l)
        if m: cur = short(m.group(1))
        if cur is None: continue
        if l.startswith('GATE: Batch'):
            for a in re.findall(r'Batch (' + H + r')', l)[:1]:
                if short(a) != cur: G.add((short(a), cur))
        txt = None
        if l.startswith('- DEPENDS ON'): txt = l
        elif re.match(r'^\| ' + H + r'\.\d+ \|', l): txt = l.rstrip().rstrip('|').rsplit('|', 1)[-1]
        if txt:
            txt = re.sub(r'MISSING \([^)]*\)', '', txt)
            for a in re.findall(r'(?:Batch |V12 )(' + H + r')\b', txt) + re.findall(r'(' + H + r')\.\d\d', txt):
                a = short(a)
                if a and a != cur and a not in ('B98', 'B99'): Dp.add((a, cur))
nodes |= {x for e in S | G | Dp for x in e}
def cycles(E):
    adj = {}
    for a, b in E: adj.setdefault(a, set()).add(b)
    idx, low, st, on, out, i = {}, {}, [], set(), [], [0]
    sys.setrecursionlimit(10000)
    def sc(v):                                     # Tarjan's strongly connected components
        idx[v] = low[v] = i[0]; i[0] += 1; st.append(v); on.add(v)
        for w in adj.get(v, ()):
            if w not in idx: sc(w); low[v] = min(low[v], low[w])
            elif w in on: low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            comp = []
            while True:
                w = st.pop(); on.discard(w); comp.append(w)
                if w == v: break
            if len(comp) > 1: out.append(sorted(comp))
    for v in sorted(nodes):
        if v not in idx: sc(v)
    return out
def waves(E):                                      # wave = longest path from a source, in edges
    preds = {}
    for a, b in E: preds.setdefault(b, set()).add(a)
    memo = {}
    def w(v):
        if v in memo: return memo[v]
        r = 0 if not preds.get(v) else 1 + max(w(p) for p in preds[v])
        memo[v] = r; return r
    return {v: w(v) for v in nodes}
base = S | G
print('nodes', len(nodes), '| S', len(S), '| G-only', len(G - S), '| D-only', len((Dp - S) - G))
print('G-only edges:', sorted(G-S)); print('cycles in S:', cycles(S)); print('cycles in S+G:', cycles(base))
print('cycles in S+G+D:', cycles(base | Dp))
assert not cycles(base), 'S+G cyclic'
W0 = waves(base); print('waves S+G: max', max(W0.values()))
back = sorted((a, b) for a, b in (G | Dp) - S if W0.get(a, 0) >= W0.get(b, 0))
print('G/D edges not forward in S+G waves:', back)
PROP = [l.split() for l in open(sys.argv[2]) if l.strip() and not l.startswith('#')]
for a, b in PROP:
    E = base | {(a, b)}
    c = cycles(E); W = waves(E) if not c else W0
    moved = sorted(v for v in nodes if W[v] != W0[v])
    print(f'{a}->{b}: in S={ (a,b) in S } in G={ (a,b) in G } in D={ (a,b) in Dp } | cycle={bool(c)} | max wave {max(W.values())} | waves moved: {moved[:8]}{"..." if len(moved)>8 else ""}')
E = base | {(a, b) for a, b in PROP}
print('ALL proposed together: cycles', cycles(E), '| max wave', max(waves(E).values()))
WS = waves(S)
print('S alone: max wave', max(WS.values()), '| S+G: max wave', max(W0.values()))
print('waves moved by G over S:', sorted((v, WS[v], W0[v]) for v in nodes if WS[v] != W0[v]))
```

## Appendix B — the script's readings (run 2026-11-12, after P-33)

- nodes 62; S 383 edges; 12 G edges not in S; 177 D edges not in S or G.
- cycles: none in S; none in S+G; S+G+D has one large component through D's forward notes (HD-17), plus B36 ↔ B38 (B36's "readers of G1–G5: V12 Batch B38", a note).
- longest path (waves past B00): 22 under S and under S+G. G moves B08 W6 → W9, B30 W17 → W18, B31 W16 → W18.
- each proposed edge alone: no cycle. +1 wave (to 23): B11 → B21, B12a → B21b, B28 → B32, B25 → B27, B12c → B24a. Every other edge: max wave 22 (B20 → B41 moves only B41).
- all 24 proposed edges together: acyclic, max wave 24. **The 20 edges recommended above** (the 24 less HD-03, HD-04, HD-06 and HD-08; HD-17's edge was tried alone): acyclic, max wave 22. The critical path does not move.
