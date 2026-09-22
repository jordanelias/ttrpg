#!/usr/bin/env python3
"""FALSIFIER for the 2026-09-13 handoff split (ED-IN-0221). Re-derives every number that entry
states, and re-proves the split lossless, from the tree and git.

    python tools/verify_handoff_split.py            # verify against the split's parent commit
    python tools/verify_handoff_split.py --before <ref>

WHAT IT PROVES, AND — IN THE SAME BREATH — WHAT IT DOES NOT. Per lane it proves that every line of
CONTENT in the pre-split file is still READABLE SOMEWHERE in `HANDOFF_<LANE>.md`,
`HANDOFF_<LANE>_closed.md` or `HANDOFF_<LANE>_history.md` (where that exists).

⚠ READABLE SOMEWHERE IS NOT STILL IN ITS OWN PLACE, and the difference is not hypothetical in THESE
files: the split writes, into each live file, an index of what moved, and the rows of that index
QUOTE the heading and the marker line they point at. A quoted line therefore has two homes, and a
checker asking only "are these words present" is satisfied by either. The three bounds below close
that for every line judged on its own words and for every heading; what remains open is stated at
the verdict line, not only here, and is measured by `--stress`.

⚠ IT COMPARES CONTENT, NOT LINE BREAKS. The first version compared exact line strings as a
multiset, which made **rewrapping a paragraph indistinguishable from deleting it** — and the split
DID rewrap, so the tool reported four lines of the IN lane LOST that are sitting in
`HANDOFF_IN.md` today, wrapped differently and annotated in place by `ED-IN-0239`. A falsifier that
cries wolf gets ignored. The bounds that replaced it are spelled out in the comment block headed
THE THREE BOUNDS, immediately above `find_lost_lines`, and driven on fixture strings by
`tests/valoria/test_verify_handoff_split.py`: reflow-at-another-width reports nothing, while a
deleted sentence, a deleted HEADING, a line deleted from its home but quoted in an index row, a
reversed line and a line whose words are scattered across unrelated paragraphs all report lost.

⚠ `ED-IN-0221` STATES A NARROWER CLAIM THAN THIS TOOL NOW TESTS, and that claim stays
re-derivable: the record in `registers/handoffs/HANDOFF_archive.md` says the split was "verbatim
and proved lossless (the two files' line multisets partition the original exactly)" and names this
script as the re-derivation. The **`exact`** column is that number, unchanged — the count of
pre-split line COPIES whose byte-for-byte string is in no destination. It is REPORT-ONLY. The
content comparison decides the exit code, because in-place edits landed after the split
(`ED-IN-0239`) and the exact column has legitimately read non-zero ever since.

    python tools/verify_handoff_split.py --stress [N] [SEED] [--headings] [--min-run-chars C]

`--stress` is the SENSITIVITY measurement, on the real files, ONE DELETION AT A TIME: delete a
single real line, run the whole comparison, put it back, repeat N times per lane. A loss checker
that has never been shown a loss it can measure is a claim without a control (`CLAUDE.md` §0.1
pt 4). **It always exits 0, deliberately** — it measures a sensitivity, it does not verify the
split, and an instrument whose exit code moved with the corpus would be read as a verdict on it.
Read its table and its miss list; the verdict is `--stress`-free and is the run above.

⚠ THE `_history.md` SIBLING WAS ADDED 2026-09-17 (`ED-IN-0240`, Jordan: *"TRIM THE HANDOFFS"*), and
this tool had to learn about it or it would have reported a FALSE ALARM on the IN lane — 65k tokens
of narrative left the live file for a destination this summation did not know. A falsifier that
cries wolf gets ignored, which is worse than not having one. `_closed` holds what the marker
predicate proved FINISHED; `_history` holds dated narrative regardless of markers, with every marker
it carries indexed verbatim in the live file. That is the whole safety claim of the
split — closed narrative was MOVED, never pruned — and it is the claim ED-IN-0221 would be wrong
about if this exits non-zero.

⚠ THIS IS A ONE-SHOT FALSIFIER, NOT A GATE, AND IT MUST NOT BECOME ONE. It is wired to no CI job
and no hook deliberately. Its subject is this repository's PROCESS, which is exactly what
`CLAUDE.md` §0.1 pt 5's predicate excludes from earning a guard: *"A pattern defect in an artifact
that is load-bearing only on this repository's process is not evidence the artifact needs a guard."*
It exists because two OTHER rules require it and they are narrower than that exclusion:
§0.1 pt 3 ("a result claim carries, in the same commit, the test that would have shown it wrong")
and `ED-PC-0040`'s claim-provenance gate, which refuses a ledger entry stating measured numbers
unless it names a re-runnable instrument that is in the tree. Adding it to a CI job would convert a
falsifier into the apparatus the predicate forbids. Delete it once the split is old news.
"""
import re, subprocess, sys, os, bisect, random
from collections import Counter
from typing import NamedTuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common

LANES = ('IN', 'MB', 'PC', 'SC')
SPLIT_ED = 'ED-IN-0221'
HEADING_RE = re.compile(r'^\s{0,3}#{1,6} ')

MIN_RUN_CHARS = 24     # content a contiguous fragment must carry to count as survival, not luck
MAX_CANDIDATES = 4000  # occurrences of a run's first word scanned per step; capping errs to LOST


class ContentDiff(NamedTuple):
    """`lost`: original lines whose content is in no destination — one entry per missing copy.
    `reflowed`: `(line, runs)` for lines whose exact string is gone but whose content is present.
    `runs` is 0 for a line that survived intact but restyled, 1 for a plain rewrap, more for a
    line edited in place. REPORT-ONLY.
    `exact_deficit`: REPORT-ONLY, and it is the ONLY number `ED-IN-0221` ever claimed — pre-split
    line COPIES, blank lines included, whose byte-for-byte string is in no destination. Kept so
    that record's "the line multisets partition the original exactly" stays re-derivable from the
    instrument it names, now that in-place edits (`ED-IN-0239`) have made it legitimately non-zero.
    """
    lost: list
    reflowed: list
    exact_deficit: int


def normalize_words(text):
    """The comparison unit: lowercased alphanumeric cores, in order, whitespace and markup gone.

    `**bold**`, `~~struck~~`, backticks, wrap position and trailing punctuation are all
    presentation, and the split changed presentation everywhere. `~~needs_jordan~~` and
    `needs_jordan` are the same word here, deliberately. A line that normalizes to nothing (blank,
    `---`, a lone bullet) carries no content and is never judged lost.
    """
    return [w for w in (re.sub(r'[^0-9a-z]+', '', tok) for tok in text.lower().split()) if w]


def _index(words):
    idx = {}
    for i, w in enumerate(words):
        idx.setdefault(w, []).append(i)
    return idx


def _chars(words):
    """How much CONTENT a word sequence carries. The ruler for every bound below."""
    return sum(len(w) for w in words)


class Stream(NamedTuple):
    """A destination flattened to one word sequence, plus WHERE ITS LINES BEGIN AND END.

    `starts` holds the position of each line's first word; `ends` holds the position one past each
    line's last. Content-free lines contribute nothing, so a blank line is invisible in `words` —
    block structure is read off the ORIGINAL instead, where it is what the bounds need it for.
    The two position sets exist for bound 3 and nothing else.
    """
    words: list
    index: dict
    starts: frozenset
    ends: frozenset


def make_stream(text):
    words, starts, ends = [], set(), set()
    for ln in text.split('\n'):
        w = normalize_words(ln)
        if not w:
            continue
        starts.add(len(words))
        words.extend(w)
        ends.add(len(words))
    return Stream(words, _index(words), frozenset(starts), frozenset(ends))


def runs_covering(line_words, stream, anchored=False):
    """Cover `line_words` with contiguous runs of `stream.words`, in order. Runs used, or None.

    Every run must carry `MIN_RUN_CHARS` characters; the first one that does not fails the whole
    cover. A line shorter than that floor can never be covered at all — which is the point, and is
    what a run budget expressed in words could not say.

    `anchored` additionally requires the cover to BEGIN at the first word of some destination line
    and END at the last word of some destination line. That is bound 3, and it is what separates a
    one-line block that was merely rewrapped (which still starts a line and ends one) from the same
    text quoted INSIDE a longer line, such as an index row.

    Greedy longest-match: at each step take the longest run starting at the next uncovered word,
    at or after where the previous run ended. Greedy can need MORE runs than an optimal cover, and
    under `anchored` it can also settle on a cover whose tail misses a line end where another cover
    would not — both err toward a false LOST, which a reader checks, rather than a false OK, which
    nobody ever looks at again. `MAX_CANDIDATES` truncates the same way, for the same reason.
    """
    dest_words, dest_index = stream.words, stream.index
    n, i, floor, used = len(line_words), 0, 0, 0
    while i < n:
        occ = dest_index.get(line_words[i])
        if not occ:
            return None
        best, best_at = 0, 0
        first = bisect.bisect_left(occ, floor)
        for p in occ[first:first + MAX_CANDIDATES]:
            if anchored and i == 0 and p not in stream.starts:
                continue
            k = 0
            while i + k < n and p + k < len(dest_words) and dest_words[p + k] == line_words[i + k]:
                k += 1
            if k > best:
                best, best_at = k, p
            if best == n - i:
                break
        if _chars(line_words[i:i + best]) < MIN_RUN_CHARS:
            return None
        used += 1
        i += best
        floor = best_at + best
    if anchored and floor not in stream.ends:
        return None
    return used


def _best_cover(sequences, streams, anchored=False):
    """Fewest runs any one destination needs for any one of `sequences`, or None if none can."""
    return min((r for r in (runs_covering(s, st, anchored) for s in sequences for st in streams)
                if r is not None), default=None)


def _glued_to_neighbour(orig_words, i):
    """`line_words` glued to each ADJACENT content line of the original, in original order.

    ONE line on each side, not a window, because one line is exactly what a line break has. A blank
    line, a rule or a bare bullet carries no content and is a block boundary: rewrapping never moves
    words across one, so there is nothing on that side to lean on. Returns `[]` for a line that is a
    block of its own — every heading, and any lone line between two blanks — which is bound 3's
    case and the reason bound 3 exists.
    """
    out = []
    for j in (i - 1, i + 1):
        if 0 <= j < len(orig_words) and orig_words[j]:
            out.append(orig_words[j] + orig_words[i] if j < i else orig_words[i] + orig_words[j])
    return out


# ── THE THREE BOUNDS ─────────────────────────────────────────────────────────
#
# A moved paragraph gets rewrapped, and an entry that closes later gets a `⛔ CLOSED` clause spliced
# into the middle of a line. Neither destroys anything. Comparing exact line strings called both of
# them loss. So the question is whether the line's CONTENT survived, not its byte string.
#
# ⚠ THE FAILURE MODE OF THAT REPAIR IS SILENT, AND TWO ATTEMPTS AT IT SHIPPED IT.
#
# The FIRST asked one question of every line — "do these words occur, in order, in few enough
# contiguous runs?" — with a run budget of `ceil(n / MIN_RUN_WORDS)`, which for any line of four
# words or fewer is ONE run. One run of two words is "do the words 'next actions' occur anywhere in
# 200k tokens of handoff prose", and they do. So deleting `## Next actions` outright was reported as
# a survivor. EVERY SHORT SECTION HEADING IS IN THAT CLASS.
#
# The SECOND fixed the ruler and left the question: a fragment is measured in CHARACTERS of content,
# not in words, so `## Next actions` (11 characters) could no longer buy a run. Word count was the
# wrong ruler twice over — it called that heading the same size as
# `needs_jordan = its §5 fork docket).** \`designs/architecture/key_echo_armature_v1.md\``
# (67 characters), a real IN-lane line whose content sat in the tree while a word-count threshold
# called it LOST. But a LONG line still had to clear only "your words are contiguous SOMEWHERE",
# and in these files that is a weak bar for a reason nothing about English explains: THE SPLIT
# WRITES AN INDEX OF WHAT MOVED INTO EACH LIVE FILE, AND ITS ROWS QUOTE THE LINE THEY POINT AT.
# Deleting `registers/handoffs/HANDOFF_IN_closed.md`'s `- **Filed, not acted on:** …` line was
# reported "rewrapped, content intact", LOSSLESS, exit 0, because `HANDOFF_IN.md:22` is
# `| **!** | 145 | Next actions :: - **Filed, not acted on:** …` and the words are all there.
#
# THE RULE THAT REPLACES BOTH: ASK WHERE THE CONTENT IS, NOT ONLY WHETHER IT IS. All three bounds
# are consequences of ONE property — REWRAPPING MOVES A LINE BREAK AND NOTHING ELSE. It preserves
# the word stream of the block it rewraps, and therefore preserves (a) the line's own words, in
# order; (b) their ADJACENCY to the words of the lines above and below inside that block; and
# (c) the fact that a block still starts at the beginning of some destination line and finishes at
# the end of some destination line. Bounds 2 and 3 are (b) and (c). Quoting a line into an index row
# preserves (a) and neither of the others, which is exactly the discrimination that was missing.
#
# Applied in this order:
#
#   1. DID IT SURVIVE AS A LINE? A destination LINE with the same normalized words, counted PER
#      COPY, is the strongest evidence available and it costs a dictionary lookup. This is the old
#      exact-multiset check with markup and wrap position divided out, and it accounts for almost
#      every line: the `reflowed` column of a plain `python tools/verify_handoff_split.py` run is
#      the count that needed anything further, and on a corpus of thousands of lines it is single
#      digits. It is also the only bound that counts copies, which is why N headings in the
#      original are not covered by N-1 surviving ones.
#   2. IS IT STILL NEXT TO ITS NEIGHBOUR? For a line with an adjacent content line: its words
#      GLUED to that neighbour's, in order, in ONE destination, in contiguous runs — where EVERY
#      RUN CARRIES `MIN_RUN_CHARS` NORMALIZED CHARACTERS. The floor bounds the number of runs (a
#      sequence of C characters cannot use more than C / `MIN_RUN_CHARS` of them) and refuses word
#      soup; the GLUE is what refuses a quotation, because an index row quotes the line and not the
#      paragraph it sat in. Either neighbour will do: a section's last line and the next section's
#      first line can be split into different files, and only one side has to hold.
#   3. NO ADJACENT CONTENT LINE AT ALL — a block of one, which is every heading and any lone line
#      between two blanks? Then there is no adjacency to test, and the ANCHORED cover stands in for
#      it: the words must be contiguous AND the cover must start where a destination line starts
#      and end where a destination line ends. Rewrapping a one-line block into two lines keeps
#      both; quoting it inside a table row keeps neither. A short heading fails on the character
#      floor before it ever reaches the anchor, which is the `## Next actions` case.
#
# EVERY word of the line must be matched under all three — no partial credit, no "most of it is in
# there". Where the bounds err they err toward a false LOST, which a reader checks, and away from a
# false OK, which nobody ever looks at again.
#
# ⚠ WHAT STILL GETS THROUGH, because a tool that cannot say this is not honest about itself: a line
# that fails bound 1 AND whose words, TOGETHER WITH one adjacent line's, still read contiguously
# somewhere else in the same lane. That is a passage the corpus genuinely holds twice — an index
# row long enough to quote two consecutive lines, or a paragraph repeated verbatim between files.
# Deleting one copy leaves the content readable but not in its own place. `--stress` counts it.
#
# ⚠ `MIN_RUN_CHARS` IS MEASURED, NOT PICKED, AND THE POINT OF MEASURING IT WAS TO FIND THAT NOTHING
# HERE IS BALANCED ON IT. The instrument is a sweep a reader can run verbatim:
#
#     for c in 16 24 32 40 48 56; do
#       python tools/verify_handoff_split.py --stress 25 0 --min-run-chars $c | grep '^ALL'
#       python tools/verify_handoff_split.py --min-run-chars $c | grep -c 'LOST CONTENT'
#     done
#
# The first line of each pair is sensitivity — trials, caught, missed, duplicates — over
# one-at-a-time deletions; the second is how many lanes of the REAL split read
# `*** LOST CONTENT ***`
# at that value, which is zero until the floor starts crying wolf. MEASURED 2026-09-22 by exactly
# that loop: sensitivity was identical at 16, 24, 32 and 40 (the same single miss in 100 trials),
# and the first false alarm on the real split appeared at 43. 24 is far below that cliff and nothing
# is bought by moving it. RE-RUN IT rather than trusting those figures — quoting a carried-forward
# number is the defect `CLAUDE.md` §0.1 pt 3 row 4 describes, and this corpus is edited every week.


def find_lost_lines(orig, destinations):
    """-> ContentDiff. THE COMPARISON, factored out so a test can drive it on fixture strings.

    The three bounds are the comment block above. Two relaxations, stated rather than hidden:

    * Bounds 2 and 3 ask whether the content is present, not how many times, so a line long enough
      to scan for that is duplicated in the original and survives once can be reported REFLOWED
      rather than lost. Bound 1 does NOT have this hole — it counts copies — and bound 1 is what
      every short line and every heading is judged by, which is where duplication actually lives.
    * A line whose neighbour was ALSO deleted is judged against a destination that no longer holds
      the neighbour either, so both read lost. Two reports for two deletions, which is right, but
      the second one is not independent evidence of the first.
    """
    orig_lines = orig.split('\n')
    dest_lines = Counter()
    for d in destinations:
        dest_lines.update(d.split('\n'))
    # REPORT-ONLY, and computed before anything else touches it: `ED-IN-0221`'s own instrument.
    exact_deficit = sum((Counter(orig_lines) - dest_lines).values())

    orig_words = [normalize_words(ln) for ln in orig_lines]
    streams = [make_stream(d) for d in destinations]
    exact_pool = Counter(dest_lines)
    line_pool = Counter()
    for d in destinations:
        line_pool.update(tuple(normalize_words(ln)) for ln in d.split('\n'))

    # PASS 1 — claim the byte-for-byte survivors, one destination copy per original copy, so that
    # a line appearing 8 times in the original cannot be covered by 7 surviving copies.
    pending = []
    for i, line in enumerate(orig_lines):
        if not orig_words[i]:
            continue
        key = tuple(orig_words[i])
        if exact_pool[line] > 0:
            exact_pool[line] -= 1
            line_pool[key] -= 1
        else:
            pending.append(i)

    lost, reflowed = [], []
    for i in pending:
        line, lw = orig_lines[i], orig_words[i]
        key = tuple(lw)
        if line_pool[key] > 0:                                  # bound 1: it is still A LINE
            line_pool[key] -= 1
            reflowed.append((line, 0))
            continue
        glued = _glued_to_neighbour(orig_words, i)
        runs = (_best_cover(glued, streams) if glued                          # bound 2
                else _best_cover([lw], streams, anchored=True))               # bound 3
        (reflowed.append((line, runs)) if runs is not None else lost.append(line))
    return ContentDiff(lost, reflowed, exact_deficit)


def _git(*args):
    r = subprocess.run(('git',) + args, capture_output=True, text=True,
                       cwd=ci_common.REPO)
    return r.stdout if r.returncode == 0 else None


def _before_ref(explicit=None):
    """The commit whose tree still holds the un-split handoffs."""
    if explicit:
        return explicit
    # ⚠ TWO CASES, AND THE FIRST VERSION OF THIS GOT THE SECOND ONE WRONG — it always returned
    # `HEAD^`, which on an uncommitted split reads one commit too far back and silently compared
    # against a pre-split file that was itself a revision out of date. Caught by the numbers not
    # matching the split's own measurement.
    #   * split already committed -> `before` is the parent of the commit that ADDED the closed file
    #   * split still uncommitted  -> `before` is HEAD, because the un-split file IS what HEAD holds
    out = _git('log', '--diff-filter=A', '--format=%H', '-1',
               '--', 'registers/handoffs/HANDOFF_IN_closed.md')
    if out and out.strip():
        return out.strip() + '^'
    return 'HEAD'


# ── Structural invariant: a heading's PARENT does not change (ED-IN-0241) ─────
#
# ⚠ THIS EXISTS BECAUSE THE SAME DEFECT FIRED THREE TIMES IN ONE SESSION, and each time it was
# patched with a hard-coded list of section names instead of a rule. Jordan: *"stop hard coding"*.
#
# THE DEFECT: a splitter that slices a section as "this heading to the next heading of ANY level"
# moves a `##` head and LEAVES ITS `###` CHILDREN BEHIND. The children then sit under whatever
# section happens to precede them, which reads as though someone filed them there deliberately.
# It happened to `## Next actions`'s ruling records, to `## ⚠ WAS CURRENT — 2026-08-27`'s five
# subsections, and a heading inserted on "the first `###` in the file" landed inside the ratified
# work order, briefly filing it under "RULINGS AND STANDING STATE".
#
# THE RULE, which needs no names: A HEADING BELONGS TO ITS NEAREST PRECEDING HEADING OF A HIGHER
# LEVEL. So a unit is a SUBTREE, not a slice, and moving a parent moves its children. What this
# function checks is the observable consequence: for every heading that is STILL IN THE SAME FILE
# after the edit, its parent heading must be the one it had before. A heading that moved to another
# file legitimately gets a new parent there, so it is excluded — the invariant is about what STAYED.


def _parents(text):
    """{heading: parent heading or None}, structurally, fence-aware."""
    out, stack, fence = {}, {}, None
    for ln in text.split('\n'):
        f = re.match(r'^\s*(`{3,}|~{3,})', ln)
        if f:
            tok = f.group(1)[0]
            fence = None if fence == tok else (fence or tok)
            continue
        if fence:
            continue
        m = re.match(r'^(#{1,6}) (.+)$', ln)
        if not m:
            continue
        lvl, head = len(m.group(1)), m.group(2).strip()
        out[head] = next((stack[l] for l in range(lvl - 1, 0, -1) if l in stack), None)
        stack[lvl] = head
        for l in [l for l in stack if l > lvl]:
            del stack[l]
    return out


def check_structure(before, paths):
    """REPORT-ONLY. Prints every heading that stayed in its file under a DIFFERENT parent.

    Report-only rather than blocking, and that is a ruling rather than a preference: a reparent is
    sometimes deliberate — moving a `##` out legitimately leaves its surviving children needing a
    new home — so a failing verdict here would halt on a heuristic, which Jordan ruled against
    (`CLAUDE.md` §10: *"a breaker halting a large audit on a heuristic costs more than the defect
    it caught"*). It always returns 0. READ ITS OUTPUT; it cannot decide for you.
    """
    bad = 0
    print(f'\n{"file":<46}{"headings":>10}{"reparented":>12}  verdict')
    for rel in paths:
        old = _git('show', f'{before}:{rel}')
        if old is None:
            continue
        pb, pa = _parents(old), _parents(open(os.path.join(ci_common.REPO, rel),
                                              encoding='utf-8').read())
        moved = [h for h in pb if h in pa and pb[h] != pa[h]]
        bad += len(moved)
        print(f'{rel:<46}{len(pa):>10}{len(moved):>12}  '
              f'{"OK" if not moved else "*** REPARENTED ***"}')
        for h in moved[:5]:
            print(f'      {h[:68]!r}\n        was under {pb[h]!r}\n        now under {pa[h]!r}')
    if bad:
        print(f'  {bad} heading(s) reparented — REPORT-ONLY. Judge each: a `##` moved out leaves '
              'its surviving children needing a parent, which is legitimate. An UNINTENDED one '
              'reads as though someone filed a section somewhere deliberately.')
    return 0


def _lane_texts(before, lane):
    """`(orig, [live, closed, history])` for one lane, or `None` if `before` cannot be read."""
    root = ci_common.REPO
    live_p = f'registers/handoffs/HANDOFF_{lane}.md'
    orig = _git('show', f'{before}:{live_p}')
    if orig is None:
        return None
    out = []
    for p in (live_p, f'registers/handoffs/HANDOFF_{lane}_closed.md',
              f'registers/handoffs/HANDOFF_{lane}_history.md'):
        abs_p = os.path.join(root, p)
        out.append(open(abs_p, encoding='utf-8').read() if os.path.exists(abs_p) else '')
    return orig, out


def _how(runs):
    return {0: 'restyled in place', 1: 'rewrapped'}.get(runs, f'edited in place ({runs} runs)')


# ── SENSITIVITY: what does this comparison MISS on the real files? ────────────
#
# A loss checker reporting zero losses is reporting one of two things and the output cannot tell
# you which: nothing was lost, or nothing is visible to it. `CLAUDE.md` §0.1 pt 4 — a number
# without a control is not a measurement. This is the control, and it runs on the real corpus
# rather than on fixtures, because the coincidence rate that defeated the first two repairs is a
# property of 200k tokens of repetitive handoff prose and does not exist in a fixture.
#
# ⚠ ONE DELETION PER TRIAL, AND THE REASON IS THAT THE BATCHED VERSION FLATTERED ITSELF. It used to
# delete N lines at once and score them together. Deleting a few hundred lines strips a measurable
# slice of the corpus BEFORE the comparison runs, which removes the very duplicates a surviving
# line could have hidden behind — so the batch scored the checker against an easier corpus than the
# one it is used on, and every number it produced was optimistic by an amount nobody had measured.
# One at a time costs one full comparison per trial (tenths of a second per lane, so N is small by
# construction) and measures the thing the name promises.


def stress(before, n, seed, headings_only=False, command=''):
    """Delete ONE real line, run the whole comparison, restore it, repeat. ALWAYS RETURNS 0.

    Report-only by construction (`CLAUDE.md` §10 on breakers that halt on a heuristic): a miss rate
    is a property of the corpus, not a defect in the split, and an exit code that moved with it
    would be read as a verdict on the split. The verdict is `main()` without `--stress`.

    `headings_only` restricts the candidates to markdown headings, which are the class the two
    earlier repairs were blind to and the class bound 3 exists for. Run both.
    """
    rng = random.Random(seed)
    print(f'[verify-handoff-split] SENSITIVITY · before = {before}')
    print(f'  reproduce with: {command}')
    print(f'  one deletion per trial · {n} trials per lane · MIN_RUN_CHARS={MIN_RUN_CHARS}'
          f'{" · headings only" if headings_only else ""}\n')
    print(f'{"lane":<6}{"chars/line":>12}{"deleted":>9}{"caught":>8}{"missed":>8}'
          f'{"dup":>6}  (dup = another copy legitimately survives)')
    misses, totals = [], [0, 0, 0, 0]
    for lane in LANES:
        got = _lane_texts(before, lane)
        if got is None:
            continue
        orig, dests = got
        in_orig = Counter(orig.split('\n'))
        cand = [(d, i) for d, text in enumerate(dests) for i, ln in enumerate(text.split('\n'))
                if normalize_words(ln) and in_orig[ln]
                and (not headings_only or HEADING_RE.match(ln))]
        if not cand:
            continue
        buckets = {}
        for d, i in rng.sample(cand, min(n, len(cand))):
            lines = dests[d].split('\n')
            ln = lines[i]
            cut = list(dests)
            cut[d] = '\n'.join(lines[:i] + lines[i + 1:])
            after = Counter()
            for c in cut:
                after.update(c.split('\n'))
            # A line the original holds k times and the mutilated destinations still hold k times
            # lost no content: the deletion removed a duplicate. Counted apart, never as a miss.
            dup = after[ln] >= in_orig[ln]
            caught = ln in find_lost_lines(orig, cut).lost
            c = _chars(normalize_words(ln))
            # Bucketed on the tool's own ruler, so a miss can be read against the bound that let it
            # through: below MIN_RUN_CHARS a line cannot form one valid run at all.
            key = (f'<{MIN_RUN_CHARS}' if c < MIN_RUN_CHARS else
                   f'{MIN_RUN_CHARS}-{2 * MIN_RUN_CHARS - 1}' if c < 2 * MIN_RUN_CHARS else
                   f'{2 * MIN_RUN_CHARS}-99' if c < 100 else '100+')
            b = buckets.setdefault(key, [0, 0, 0, 0])
            b[0] += 1
            b[1 if caught else 3 if dup else 2] += 1
            totals[0] += 1
            totals[1 if caught else 3 if dup else 2] += 1
            if not caught and not dup:
                misses.append((lane, c, ln))
        for key in (f'<{MIN_RUN_CHARS}', f'{MIN_RUN_CHARS}-{2 * MIN_RUN_CHARS - 1}',
                    f'{2 * MIN_RUN_CHARS}-99', '100+'):
            if key in buckets:
                tot, hit, miss, dups = buckets[key]
                print(f'{lane:<6}{key:>12}{tot:>9}{hit:>8}{miss:>8}{dups:>6}')
    print(f'\n{"ALL":<6}{"":>12}{totals[0]:>9}{totals[1]:>8}{totals[2]:>8}{totals[3]:>6}')
    if misses:
        print(f'\n{len(misses)} deleted line(s) NOT reported lost — THE RESIDUAL BLIND SPOT, '
              'and it has one shape:\n  the line failed the "still a line" bound, and its words '
              'TOGETHER WITH an adjacent line\'s\n  still read contiguously elsewhere in the same '
              'lane. The corpus holds that passage twice\n  (an index row quoting two consecutive '
              'lines, or a paragraph repeated between files), so the\n  content is still '
              'readable — but no longer in its own place, which is what this cannot see.')
        for lane, c, ln in misses[:20]:
            print(f'    {lane} · {c} chars: {ln[:88]!r}')
    else:
        print('\nno deleted line escaped detection at this n, seed and candidate filter')
    return 0


def _parse(argv):
    """Hand-rolled so `--stress N SEED` keeps its positional form. -> (mode, opts) or exits.

    Flags, all optional: `--before REF`, `--headings` (stress only), `--min-run-chars C`.
    """
    args, before, headings, min_chars = list(argv[1:]), None, False, None
    rest = []
    while args:
        a = args.pop(0)
        if a == '--before':
            before = args.pop(0)
        elif a == '--headings':
            headings = True
        elif a == '--min-run-chars':
            min_chars = int(args.pop(0))
        elif a in ('-h', '--help'):
            print(__doc__)
            raise SystemExit(0)
        else:
            rest.append(a)
    return rest, before, headings, min_chars


def main(argv):
    global MIN_RUN_CHARS
    rest, before_arg, headings, min_chars = _parse(argv)
    if min_chars is not None:
        MIN_RUN_CHARS = min_chars
    if rest and rest[0] == '--stress':
        n = int(rest[1]) if len(rest) > 1 else 30
        seed = int(rest[2]) if len(rest) > 2 else 0
        before = _before_ref(before_arg)
        cmd = (f'python tools/verify_handoff_split.py --stress {n} {seed}'
               f'{" --headings" if headings else ""}'
               f'{f" --min-run-chars {MIN_RUN_CHARS}" if min_chars is not None else ""}')
        return stress(before, n, seed, headings, cmd)
    before = _before_ref(before_arg)
    print(f'[verify-handoff-split] {SPLIT_ED} · before = {before}\n')
    print(f'{"lane":<6}{"before":>10}{"live":>10}{"closed":>10}{"history":>10}'
          f'{"exact":>8}{"reflowed":>10}{"lines lost":>12}  verdict')
    bad = 0
    total_moved = 0
    total_reflowed = 0
    total_exact = 0
    for lane in LANES:
        got = _lane_texts(before, lane)
        if got is None:
            print(f'{lane:<6}{"—":>10}  cannot read HANDOFF_{lane}.md at {before} '
                  f'— pass --before <ref>')
            bad += 1
            continue
        orig, (live, clos, hist) = got
        diff = find_lost_lines(orig, [live, clos, hist])
        n_lost = len(diff.lost)
        ok = n_lost == 0
        bad += 0 if ok else 1
        total_moved += ci_common.tokens(clos) + ci_common.tokens(hist)
        total_reflowed += len(diff.reflowed)
        total_exact += diff.exact_deficit
        print(f'{lane:<6}{ci_common.tokens(orig):>10,}{ci_common.tokens(live):>10,}'
              f'{ci_common.tokens(clos):>10,}{ci_common.tokens(hist):>10,}'
              f'{diff.exact_deficit:>8}{len(diff.reflowed):>10}{n_lost:>12}  '
              f'{"LOSSLESS" if ok else "*** LOST CONTENT ***"}')
        for line in diff.lost[:5]:
            print(f'        lost: {line[:100]!r}')
        for line, runs in diff.reflowed[:5]:
            print(f'        {_how(runs)}, content intact: {line[:88]!r}')
    print(f'\nclosed narrative moved out of the orientation surfaces: {total_moved:,} tokens')
    # BOTH of the next two lines are REPORT-ONLY, and the first is the one `ED-IN-0221` claimed.
    print(f'exact-line deficit (`ED-IN-0221`\'s own multiset check, all four lanes): {total_exact} '
          "— non-zero since `ED-IN-0239` edited surviving lines in place; it is not loss, and it "
          'no longer decides the exit code')
    if total_reflowed:
        # The column to read when a number here surprises you: these lines do not read
        # byte-for-byte as they did before the split, and their content is all present.
        print(f'{total_reflowed} line(s) rewrapped or edited in place — content verified present, '
              'not counted as loss')

    # Losslessness is only half the claim; the other half is that what STAYED still reads as the
    # document it was. Derived from the tree, never from a list of section names.
    watched = ['HANDOFF.md'] + [f'registers/handoffs/HANDOFF_{l}.md' for l in LANES]
    bad += check_structure(before, watched)

    if bad:
        print(f'[verify-handoff-split] FAILED on {bad} check(s)')
        return 1
    # ⚠ THE LIMIT IS PRINTED WHERE THE VERDICT IS READ, not only in a docstring nobody opens on a
    # green run. An unqualified OK on a checker with a known blind spot is the claim §0.1 pt 3 row 1
    # is about: an absence is the cheapest thing to assert and the hardest to see wrong.
    print('[verify-handoff-split] OK — every pre-split line of CONTENT is still READABLE somewhere '
          'in the tree.\n'
          '  IT DOES NOT PROVE EACH LINE IS STILL IN ITS OWN PLACE. A line that no longer survives '
          'as a line,\n'
          '  and whose words together with an adjacent line\'s still read contiguously '
          'elsewhere in the same\n'
          '  lane — the index of what moved quotes the lines it points at — can have been deleted '
          'from its\n'
          '  home and still read as present here. `--stress` measures how often that happens; '
          'rewrapping and\n'
          '  heading reparenting above are report-only.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
