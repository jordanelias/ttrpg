"""Unit tests for `tools/verify_handoff_split.py`'s content comparison (`find_lost_lines`).

THE TOOL ANSWERS ONE QUESTION — *did anything disappear when the handoffs were split?* — and it has
now been wrong in both directions, twice silently, which is why this file is symmetric by
construction.

WRONG THE FIRST WAY, LOUDLY. It subtracted line-string multisets:

    lost = Counter(orig.split('\\n')) - (Counter(live...) + Counter(clos...) + Counter(hist...))

A split rewraps paragraphs, so **rewrapping read as deletion**. It reported four IN-lane lines
`*** LOST CONTENT ***` while all four sat in `registers/handoffs/HANDOFF_IN.md`, wrapped at a
different width and, in three cases, with an `ED-IN-0239` `⛔ CLOSED` clause spliced into the middle
of the sentence. A falsifier that cries wolf gets ignored.

WRONG THE SECOND WAY, SILENTLY. The repair asked only "do these words occur, in order, in few
enough contiguous runs?", with a run budget of `ceil(words / 4)` — which for any line of four words
or fewer is ONE run. One run of two words is "do the words 'next actions' occur anywhere in 200k
tokens of handoff prose", and they do. Deleting `## Next actions` outright was therefore reported
as a SURVIVOR, and every short section heading is in that class.

WRONG THE THIRD WAY, SILENTLY, AND THIS ONE IS NOT ABOUT ENGLISH. Measuring a fragment in
CHARACTERS rather than words fixed the short heading and left the question unchanged, so a LONG
line still had only to clear "your words are contiguous SOMEWHERE". In these files that is a weak
bar for a structural reason: **the split writes an index of what moved into each live file, and its
rows QUOTE the line they point at.** Deleting `registers/handoffs/HANDOFF_IN_closed.md`'s
`- **Filed, not acted on:** …` line read as "rewrapped, content intact", LOSSLESS, exit 0, because
`HANDOFF_IN.md:22` is `| **!** | 145 | Next actions :: - **Filed, not acted on:** …`. The bounds
now ask WHERE the content is, not only whether it is: a line is judged glued to its adjacent line,
and a line that is a block of its own (every heading) must cover a destination from a line start to
a line end. `test_a_quoted_line_is_lost_when_its_own_copy_goes` and
`test_a_heading_quoted_inside_a_longer_line_is_lost` are that defect in fixture form.

WHAT A TRIVIAL STUB SURVIVES — RE-DERIVED 2026-09-22 BY RUNNING IT, not asserted from memory, and
the earlier version of this header got it wrong in both directions. Replace the whole comparison
with `return ContentDiff([], [], 0)` and run this file: **17 of the 22 tests fail and 5 pass.** The
five are the three tolerance tests whose only claim is `lost == []`
(`test_a_rewrapped_short_tail_is_not_loss`, `test_a_lone_line_rewrapped_into_several_is_not_loss`,
`test_a_heading_that_moved_verbatim_is_not_lost`);
`test_markup_and_blank_lines_are_not_content`, whose first three assertions never reach
`find_lost_lines` and so keep binding while its last line goes vacuous; and
`test_the_min_run_chars_override_exists_so_the_documented_sweep_is_runnable`, which is about a CLI
flag and not about the comparison at all. **`test_reflow_is_not_loss` is NOT among them** — it also
asserts that the reflowed set equals a non-empty difference, which the stub returns empty.
Reproduce by assigning the stub over `verify_handoff_split.find_lost_lines` from a pytest plugin
loaded before collection (`-p`). A tolerance test cannot distinguish a fix from a deletion of the
check and is not supposed to; the deletion cases below are what do that, and they are the majority
for that reason.

HERMETIC BY CONSTRUCTION, because `pytest.ini` sets `testpaths = tests/valoria` and CI runs this
whole directory as the blocking unit-tests job. Every fixture below is defined here. Nothing shells
out to `git` and nothing reads the repo's real handoff files: a test that asserted against today's
tree would pass for whatever reason the tree happens to supply, would have to be re-pinned every
time a handoff is edited, and would fail in a shallow clone that cannot reach the pre-split commit.
The sensitivity measurement that DOES need the real corpus lives in the tool, behind
`python tools/verify_handoff_split.py --stress`, where no CI job runs it.

CLAUDE.md §0.1 point 2 — an assertion must be able to observe the failure it excludes — is why
several tests below assert about their own fixture first: `test_reflow_is_not_loss` checks that its
fixture is NOT line-identical, and every "this is lost" test checks that the words it expects to be
called LOST are in fact sitting in the destination, so the assertion is excluding something real.
"""
import os
import sys
import textwrap

HERE = os.path.dirname(__file__)
TOOLS = os.path.join(HERE, '..', '..', 'tools')
sys.path.insert(0, TOOLS)
import verify_handoff_split as vhs  # noqa: E402


PARAGRAPH = (
    "The closed narrative was moved out of the orientation surface and into the sibling "
    "file, where a reader looking for the current state of the lane will not trip over it. "
    "Nothing was pruned, and the marker predicate proved every entry finished before the "
    "mover touched it."
)

SECOND_PARAGRAPH = (
    "The history sibling holds dated narrative regardless of markers, and every marker it "
    "carries is indexed verbatim in the live file."
)


def _wrap(text, width):
    return textwrap.fill(text, width=width)


def _contiguous(fragment, text):
    """Do `fragment`'s normalized words read contiguously in `text`'s normalized word stream?

    The control every deletion test needs: it is what a words-only checker asks, so asserting it
    first is what makes "and this is STILL lost" exclude something.
    """
    return ' '.join(vhs.normalize_words(fragment)) in ' '.join(vhs.normalize_words(text))


# --------------------------------------------------------------------------------------
# 1. Reflow is not loss — the false positive that motivated the change
# --------------------------------------------------------------------------------------

def test_reflow_is_not_loss():
    """Same words, different wrap width, in a different destination file: nothing is lost."""
    orig = _wrap(PARAGRAPH, 70) + '\n\n' + _wrap(SECOND_PARAGRAPH, 70)
    live = _wrap(SECOND_PARAGRAPH, 44)
    closed = _wrap(PARAGRAPH, 96)

    # THE CONTROL (§0.1 pt 2). If the fixture happened to be line-identical, the assertion below
    # would be excluding nothing and would pass under the very implementation this file condemns.
    orig_lines = set(orig.split('\n')) - {''}
    dest_lines = set(live.split('\n')) | set(closed.split('\n'))
    assert orig_lines - dest_lines, 'fixture does not actually reflow; the test would prove nothing'

    diff = vhs.find_lost_lines(orig, [live, closed])
    assert diff.lost == []
    # Every rewrapped line is accounted for as report-only, in one contiguous run each.
    assert {ln for ln, _ in diff.reflowed} == orig_lines - dest_lines
    assert all(runs == 1 for _, runs in diff.reflowed)


def test_a_clause_spliced_into_a_line_is_not_loss():
    """The real IN-lane shape: rewrapped AND annotated in place after the split.

    `ED-IN-0239` struck words through and pushed a `⛔ CLOSED` clause into the middle of sentences
    that had already been rewrapped by the split. The surviving content is then two contiguous
    fragments rather than one, which is still survival.
    """
    orig = _wrap(PARAGRAPH, 70)
    annotated = _wrap(
        "The closed narrative was moved out of the orientation surface and into the sibling "
        "file, **⛔ CLOSED 2026-09-17 (`ED-IN-0239`): SUBJECT RETIRED** by a later ruling, "
        "where a reader looking for the current state of the lane will not trip over it. "
        "Nothing was pruned, and the marker predicate proved every entry finished before the "
        "mover touched it.", 58)

    diff = vhs.find_lost_lines(orig, [annotated])
    assert diff.lost == []
    assert diff.reflowed, 'the lines changed, so they must be reported as report-only survivors'


def test_a_rewrapped_short_tail_is_not_loss():
    """THE FALSE POSITIVE THE STRICT SHORT-LINE RULE COULD HAVE INTRODUCED, pinned.

    `touched it.` is two words. Under the rule that a short line must survive AS A LINE it would
    read LOST, because rewrapping absorbed it into the line above — and a paragraph tail is short
    in every document in this repository. What saves it is the bound a heading cannot use: the tail
    has a CONTENT NEIGHBOUR, and reflow moves a line break without breaking the adjacency of the
    words either side of it. `## Next actions` is blank on both sides and has nothing to lean on.
    """
    orig = _wrap(PARAGRAPH, 44)
    dest = _wrap(PARAGRAPH, 96)

    # THE CONTROL: the tail really is short, really is a line of its own, and really is not a line
    # of the destination — so bound 1 cannot be what rescues it.
    tail = orig.split('\n')[-1]
    assert len(vhs.normalize_words(tail)) == 2
    assert vhs._chars(vhs.normalize_words(tail)) < vhs.MIN_RUN_CHARS
    assert tail not in dest.split('\n')

    assert vhs.find_lost_lines(orig, [dest]).lost == []


def test_a_lone_line_rewrapped_into_several_is_not_loss():
    """THE FALSE POSITIVE THE ANCHOR COULD HAVE INTRODUCED, pinned from the other side.

    A line that is a block of its own has no neighbour, so it is judged by the anchored cover: its
    words must run from the start of some destination line to the end of some destination line.
    Rewrapping one long line into three keeps exactly that — the first destination line still
    begins with its first word and the last still ends with its last — so this must NOT read lost.
    Without this test the anchor could be tightened into "it must survive as one whole line", which
    would call every rewrapped standalone line a loss.
    """
    lone = ("The exporter's round-trip check is the mechanism and the design note is the "
            "reference, which is the whole of the asymmetry.")
    orig = f'\n{lone}\n\n'
    dest = _wrap(lone, 40)

    # THE CONTROL: it really is a block of one, it really was rewrapped, and it really is not a
    # line of the destination — so neither bound 1 nor the neighbour bound can be what rescues it.
    assert len(dest.split('\n')) > 1 and lone not in dest.split('\n')
    orig_words = [vhs.normalize_words(ln) for ln in orig.split('\n')]
    assert vhs._glued_to_neighbour(orig_words, 1) == [], 'fixture has a neighbour; anchor untested'

    assert vhs.find_lost_lines(orig, [dest]).lost == []


def test_markup_and_blank_lines_are_not_content():
    """`~~struck~~` is the same word as the word it strikes, and a rule line is not content."""
    assert vhs.normalize_words('**~~needs_jordan~~** = its §5 fork docket).') == \
        vhs.normalize_words('needs_jordan = its §5 fork docket).')
    assert vhs.normalize_words('---') == []
    assert vhs.normalize_words('   ') == []

    # A file that is only structure loses nothing by being restructured.
    assert vhs.find_lost_lines('---\n\n- \n\n***\n', ['']).lost == []


# --------------------------------------------------------------------------------------
# 2. Deletion is still loss — without this the fix is a deletion of the check
# --------------------------------------------------------------------------------------

def test_a_deleted_heading_is_lost_though_its_words_live_in_the_prose():
    """THE SECOND DEFECT, IN FIXTURE FORM. Two words are not a line; they are a coincidence.

    Taken from the real one: `## Next actions` at `registers/handoffs/HANDOFF_IN.md:569`
    normalizes to `['next', 'actions']`, which occurs in ordinary prose elsewhere in the lane, so
    the word-sequence-containment check reported the heading as a survivor after it had been
    deleted outright. Every short section heading normalizes to a handful of common words, and
    `check_structure` is report-only, so nothing else in the tool could have caught it.
    """
    orig = '## Next actions\n\n- the one real item the lane is still waiting on\n'
    dest = ('a paragraph that mentions the next actions of the lane in passing\n'
            '\n- the one real item the lane is still waiting on\n')

    # THE CONTROL (§0.1 pt 2): the words ARE contiguously present in the destination, so a check
    # that asks only "do these words occur in order" MUST call this heading a survivor. Without
    # this line the assertion below could pass on a fixture where the words were simply absent.
    assert _contiguous('## Next actions', dest)

    diff = vhs.find_lost_lines(orig, [dest])
    assert [ln.strip() for ln in diff.lost] == ['## Next actions']


def test_a_quoted_line_is_lost_when_its_own_copy_goes():
    """THE THIRD DEFECT, IN FIXTURE FORM, and the reason a line is judged glued to its neighbour.

    The real one: `registers/handoffs/HANDOFF_IN_closed.md:2726` was deleted in a scratch copy and
    the tool said "rewrapped, content intact", LOSSLESS, exit 0 — because `HANDOFF_IN.md:22` is an
    index row that QUOTES that line. Every marker line in these files has a second home like that,
    put there by the split itself, so "its words are contiguous somewhere" is not evidence in this
    corpus. What the quotation does NOT carry is the line that followed it in its own file.
    """
    marker = "- **Filed, not acted on:** the settlement upkeep default was never reverted"
    body = "under a comment reading RETRACTED, which git settles and nobody has acted on since"
    orig = f'{marker}\n{body}\n'
    index_row = f'| **!** | 145 | Next actions :: {marker} | second pass 2026-09-17 |'

    # THE CONTROL: on its own the line covers the index row in ONE run, so the character floor is
    # not what refuses it and a words-only check MUST call it a survivor. Stated against the tool's
    # own cover rather than against a character count, so it pins the defect and not the constant.
    assert _contiguous(marker, index_row)
    assert vhs.runs_covering(vhs.normalize_words(marker), vhs.make_stream(index_row)) == 1

    # ...and with its own copy still in place, nothing is lost. The pair is the test.
    assert vhs.find_lost_lines(orig, [index_row, f'{marker}\n{body}\n']).lost == []
    assert vhs.find_lost_lines(orig, [index_row, f'{body}\n']).lost == [marker]


def test_a_heading_quoted_inside_a_longer_line_is_lost():
    """The same defect where there is no neighbour to lean on, which is every heading.

    A heading sits between blank lines, so bound 2 has nothing to glue it to and the ANCHOR stands
    in: a rewrapped one-line block still starts a destination line and ends one, while a quotation
    inside an index row does neither. Both halves are pinned — a row whose quotation ENDS where the
    row ends (the real `|  | 4,584 | Catch-up … narrative |` shape) and one that STARTS where the
    line starts — because an anchor checked at only one end is an anchor at neither.
    """
    heading = '## DONE 2026-09-07 — the decomposition landed in the season loop, and it runs'
    body = 'the register scores it against the requirements file\n'
    orig = f'{heading}\n\n{body}'
    text = heading.lstrip('# ')
    quoted_at_end = f'|  | 1,714 | {text} |'
    quoted_at_start = f'{text} — moved to the closed sibling, 1,714 tokens'

    # THE CONTROL: in both quotations the heading covers in ONE unanchored run, so neither the
    # character floor (which is what stops `## Next actions`) nor absence is doing the work here.
    # Only the anchor can be. Asserted against the cover, so it pins the defect and not the floor.
    assert _contiguous(heading, quoted_at_end) and _contiguous(heading, quoted_at_start)
    for quotation in (quoted_at_end, quoted_at_start):
        assert vhs.runs_covering(vhs.normalize_words(heading), vhs.make_stream(quotation)) == 1

    for quotation in (quoted_at_end, quoted_at_start):
        assert vhs.find_lost_lines(orig, [quotation, body]).lost == [heading], quotation
    # ...and the same heading, present as a line, is not lost. Otherwise the assertion above is
    # satisfied by a checker that calls every heading lost.
    assert vhs.find_lost_lines(orig, [f'{heading}\n', body]).lost == []


def test_a_heading_that_moved_verbatim_is_not_lost():
    """The other side of the same bound: a heading in ANY destination file is not lost."""
    orig = '## Next actions\n\n- the one real item the lane is still waiting on\n'
    live = 'nothing of the sort here\n'
    closed = '## Next actions\n\n- the one real item the lane is still waiting on\n'
    assert vhs.find_lost_lines(orig, [live, closed]).lost == []


def test_a_repeated_heading_is_counted_per_copy():
    """Eight copies in the original are not covered by seven surviving ones.

    This is the shape the real files have — `## Next actions` appears eight times in the pre-split
    IN lane — and it is why the "did it survive as a line" bound counts copies instead of asking
    set membership. A checker that asked only whether the heading exists somewhere would never
    report the deletion of one of several identical headings.
    """
    orig = '## Next actions\n\n- item one\n\n## Next actions\n\n- item two\n'
    dest = '## Next actions\n\n- item one\n\n- item two\n'
    assert [ln.strip() for ln in vhs.find_lost_lines(orig, [dest]).lost] == ['## Next actions']


def test_deletion_is_still_loss():
    """A sentence dropped from the destination is reported, whatever the wrap width."""
    dropped = ("Nothing was pruned, and the marker predicate proved every entry finished "
               "before the mover touched it.")
    kept = PARAGRAPH.replace(dropped, '').strip()
    assert kept != PARAGRAPH

    orig = _wrap(PARAGRAPH, 70)
    diff = vhs.find_lost_lines(orig, [_wrap(kept, 50)])

    assert diff.lost, 'a deleted sentence must still read as lost'
    lost_words = vhs.normalize_words(' '.join(diff.lost))
    assert 'pruned' in lost_words and 'predicate' in lost_words


def test_a_line_present_in_no_destination_at_all_is_lost():
    """The plainest case, and the one that keeps the tool able to fail."""
    gone = 'the settlement upkeep table moved to the typed export'
    kept = 'unrelated surviving line\n'
    diff = vhs.find_lost_lines(f'{gone}\n{kept}', [kept])
    assert [ln.strip() for ln in diff.lost] == [gone]


def test_scattered_words_do_not_cover_a_line():
    """THE BLINDNESS THIS NORMALIZATION COULD HAVE HAD, pinned.

    Word-sequence matching without a bound on fragmentation would call a line 'present' whenever
    its words each turn up somewhere in a large enough corpus — and a handoff file is a large
    corpus of the same vocabulary. The character floor on each run is what refuses it: these eight
    words appear in the destination, in order, and are still lost because no fragment of the cover
    carries `MIN_RUN_CHARS` characters.
    """
    line = 'alpha beta gamma delta epsilon zeta eta theta'
    filler = 'and then some entirely unrelated prose about something else altogether'
    scattered = '\n\n'.join(f'{w} {filler}' for w in line.split())

    assert all(w in vhs.normalize_words(scattered) for w in vhs.normalize_words(line))
    diff = vhs.find_lost_lines(line, [scattered])
    assert diff.lost == [line]


def test_the_floor_admits_real_fragments_and_refuses_word_soup():
    """The threshold is a threshold, not a one-way ratchet — it holds from both sides.

    A line surviving as two substantial phrases is a line with a clause spliced into it, and it
    survives. The same line surviving as four scraps, none of which carries `MIN_RUN_CHARS`
    characters, is soup and does not. Measured in CHARACTERS rather than words because words are a
    bad ruler here: one 38-character path identifies a line and four short function words do not.
    """
    head = 'the mass battle resolver keeps'          # 26 normalized characters
    tail = 'its own commensurability ledger'         # 29
    line = f'{head} {tail}'
    assert vhs._chars(vhs.normalize_words(head)) >= vhs.MIN_RUN_CHARS
    assert vhs._chars(vhs.normalize_words(tail)) >= vhs.MIN_RUN_CHARS

    spliced = f'{head} **⛔ CLOSED 2026-09-17 (`ED-IN-0239`)** {tail}'
    scraps = ['the mass battle', 'resolver keeps its', 'own commensurability', 'ledger']
    assert all(vhs._chars(vhs.normalize_words(s)) < vhs.MIN_RUN_CHARS for s in scraps)
    soup = ' zzz yyy xxx www '.join(scraps)

    assert vhs.find_lost_lines(line, [spliced]).lost == []
    assert vhs.find_lost_lines(line, [soup]).lost == [line]


def test_order_is_required():
    """Same words, reversed: content that reads backwards is not the content that was moved."""
    line = 'the marker predicate proved every entry finished before the mover touched it'
    reversed_text = ' '.join(reversed(line.split()))
    assert vhs.find_lost_lines(line, [reversed_text]).lost == [line]


# ⚠ THE CONTROL ASSERTIONS IN `test_a_rewrapped_short_tail_is_not_loss` AND
# `test_the_floor_admits_real_fragments_and_refuses_word_soup` PIN `MIN_RUN_CHARS` INTO [20, 26].
# Said here because it is not visible from either test, and a later reader who retunes the constant
# alone will get a red file and no explanation. MEASURED 2026-09-22 by running this file once per
# value with the constant overridden — 20, 24 and 26 all green; 19 and 27 each fail one test:
#
#     for c in 9 19 20 26 27; do
#       FLOOR=$c python -m pytest tests/valoria/test_verify_handoff_split.py -q \
#         -p <plugin assigning vhs.MIN_RUN_CHARS = int(os.environ['FLOOR'])>
#     done
#
# Below 20 the word-soup fixture's scraps stop being soup; above 26 its two real fragments stop
# clearing the floor; below 10 the short paragraph tail stops being short. The window is narrow
# because the fixtures are sized from real lines, so a value outside it disagrees with the corpus
# and not merely with this file — KEEP THE ASSERTIONS and change the fixtures with the constant.
# The sweep over the REAL corpus is `--stress … --min-run-chars C`, documented at the constant.


# --------------------------------------------------------------------------------------
# 3. `ED-IN-0221`'s own number survives the change of instrument
# --------------------------------------------------------------------------------------

def test_the_exact_line_multiset_deficit_is_still_reported():
    """`registers/handoffs/HANDOFF_archive.md` records the split as "verbatim and proved lossless
    (the two files' line multisets partition the original exactly, checked against `git HEAD`)" and
    names this script as the re-derivation of exactly that. Changing what the tool TESTS must not
    stop it MEASURING what that record claims, or the record cites an instrument that no longer
    reads it — so the byte-for-byte deficit stays, report-only, beside a verdict that ignores it.
    """
    orig = _wrap(PARAGRAPH, 70) + '\n'
    dest = _wrap(PARAGRAPH, 96) + '\n'
    diff = vhs.find_lost_lines(orig, [dest])

    assert diff.lost == [], 'content is all present, so the verdict is lossless'
    # ...and the old instrument still reads four line copies as not-byte-identical, which is the
    # number the record was about. The two disagreeing is the point: one is a verdict, one is not.
    assert diff.exact_deficit == len(_wrap(PARAGRAPH, 70).split('\n')) == 4


# --------------------------------------------------------------------------------------
# 4. The tool's exit code still follows the comparison
# --------------------------------------------------------------------------------------

def _fake_repo(tmp_path, monkeypatch, before, live):
    """A two-lane repo on disk, `git show` answered from `before`. No real git, no real tree."""
    handoffs = tmp_path / 'registers' / 'handoffs'
    handoffs.mkdir(parents=True)
    (tmp_path / 'HANDOFF.md').write_text('# root\n', encoding='utf-8')
    for lane, text in live.items():
        (handoffs / f'HANDOFF_{lane}.md').write_text(text, encoding='utf-8')
        (handoffs / f'HANDOFF_{lane}_closed.md').write_text('', encoding='utf-8')
    monkeypatch.setattr(vhs.ci_common, 'REPO', str(tmp_path))
    monkeypatch.setattr(vhs, 'LANES', tuple(live))
    monkeypatch.setattr(vhs, '_git', lambda *a: before.get(a[-1].split(':')[-1], ''))
    return handoffs


def test_lost_lines_drive_a_nonzero_exit(tmp_path, monkeypatch, capsys):
    """`main()` must still FAIL on real loss. A verifier that cannot fail is not a verifier."""
    _fake_repo(
        tmp_path, monkeypatch,
        before={'registers/handoffs/HANDOFF_IN.md':
                'kept line one\nthe sentence that will disappear entirely\n',
                'registers/handoffs/HANDOFF_MB.md': 'kept line two\n'},
        live={'IN': 'kept line one\n', 'MB': 'kept line two\n'})

    rc = vhs.main(['verify_handoff_split.py'])
    out = capsys.readouterr().out
    assert rc == 1, out
    assert 'LOST CONTENT' in out
    assert 'the sentence that will disappear entirely' in out


def test_a_deleted_heading_drives_a_nonzero_exit(tmp_path, monkeypatch, capsys):
    """The defect end to end: the heading is gone, and the EXIT CODE says so.

    Pinned at `main()` and not only at `find_lost_lines`, because the first repair was reported as
    two green runs of the tool. A green run is only evidence if the red one is reachable.
    """
    _fake_repo(
        tmp_path, monkeypatch,
        before={'registers/handoffs/HANDOFF_IN.md':
                '## Next actions\n\n- the one real item the lane is still waiting on\n',
                'registers/handoffs/HANDOFF_MB.md': 'kept line two\n'},
        live={'IN': 'a paragraph mentioning the next actions of the lane in passing\n'
                    '\n- the one real item the lane is still waiting on\n',
              'MB': 'kept line two\n'})

    rc = vhs.main(['verify_handoff_split.py'])
    out = capsys.readouterr().out
    assert rc == 1, out
    assert "lost: '## Next actions'" in out


def test_a_pure_reflow_exits_zero(tmp_path, monkeypatch, capsys):
    """The same `main()`, on a lane whose only change is the wrap width: LOSSLESS, exit 0.

    Paired with the tests above deliberately. They show the tool can fail and this one shows it can
    pass, and only the pair shows the exit code tracks the content rather than a constant. It also
    pins the report-only exact-line deficit onto the command's OUTPUT, not merely into the return
    value, since a number nobody prints is a number nobody can re-derive.
    """
    _fake_repo(
        tmp_path, monkeypatch,
        before={'registers/handoffs/HANDOFF_IN.md': _wrap(PARAGRAPH, 70) + '\n',
                'registers/handoffs/HANDOFF_MB.md': 'kept line two\n'},
        live={'IN': _wrap(PARAGRAPH, 38) + '\n', 'MB': 'kept line two\n'})

    rc = vhs.main(['verify_handoff_split.py'])
    out = capsys.readouterr().out
    assert rc == 0, out
    assert 'LOST CONTENT' not in out
    assert 'rewrapped' in out
    assert 'exact-line deficit' in out


def test_the_green_verdict_states_what_it_does_not_prove(tmp_path, monkeypatch, capsys):
    """The OK line carries the limit, because a reader of a green run opens no docstring.

    The tool is known to miss a line whose words, glued to a neighbour's, still read contiguously
    elsewhere in the same lane. That was disclosed only inside `find_lost_lines`, which nobody
    opens on a pass — §0.1 pt 3 row 1: an absence is the cheapest claim to make and the hardest to
    see wrong. This asserts the qualification travels with the verdict, and that it is absent from
    the FAILING verdict, where it would read as an excuse.
    """
    _fake_repo(
        tmp_path, monkeypatch,
        before={'registers/handoffs/HANDOFF_IN.md': _wrap(PARAGRAPH, 70) + '\n'},
        live={'IN': _wrap(PARAGRAPH, 38) + '\n'})
    assert vhs.main(['verify_handoff_split.py']) == 0
    ok = capsys.readouterr().out
    assert 'DOES NOT PROVE EACH LINE IS STILL IN ITS OWN PLACE' in ok

    _fake_repo_fail = _fake_repo(
        tmp_path / 'red', monkeypatch,
        before={'registers/handoffs/HANDOFF_IN.md': 'kept\nthe line that will disappear\n'},
        live={'IN': 'kept\n'})
    assert _fake_repo_fail.exists()
    assert vhs.main(['verify_handoff_split.py']) == 1
    red = capsys.readouterr().out
    assert 'FAILED on' in red and 'DOES NOT PROVE' not in red


# --------------------------------------------------------------------------------------
# 5. `--stress` is the sensitivity control, and it is one deletion per trial
# --------------------------------------------------------------------------------------

def test_stress_deletes_one_line_at_a_time_and_always_exits_zero(tmp_path, monkeypatch, capsys):
    """The protocol the module documents has to be the protocol the module runs (§0.1 pt 3).

    The earlier version deleted N lines simultaneously and scored them together, which strips a
    slice of the corpus before the comparison runs and removes the duplicates a surviving line
    could have hidden behind — so it measured the checker against an easier corpus than the one it
    is used on. This pins the replacement: it says one deletion per trial, it prints the command
    that reproduces it, it finds the deletions on a fixture corpus where every line is unique, and
    it returns 0 whatever it finds, because a sensitivity is not a verdict.
    """
    lines = '\n'.join(f'line {i} carries enough distinct content to be identified on its own'
                      for i in range(12))
    _fake_repo(tmp_path, monkeypatch,
               before={'registers/handoffs/HANDOFF_IN.md': lines + '\n'},
               live={'IN': lines + '\n'})

    rc = vhs.main(['verify_handoff_split.py', '--stress', '6', '0'])
    out = capsys.readouterr().out
    assert rc == 0, out
    assert 'one deletion per trial' in out
    assert 'reproduce with: python tools/verify_handoff_split.py --stress 6 0' in out
    # THE CONTROL: trials actually ran and actually deleted something. A stress run that sampled
    # nothing would print the same headings and report no misses, which reads identically.
    assert 'no deleted line escaped detection' in out
    all_row = [ln for ln in out.split('\n') if ln.startswith('ALL')]
    assert all_row and all_row[0].split()[1:3] == ['6', '6'], all_row


def test_the_min_run_chars_override_exists_so_the_documented_sweep_is_runnable(
        tmp_path, monkeypatch, capsys):
    """`--min-run-chars` is the flag the constant's sweep command depends on.

    Documented beside `MIN_RUN_CHARS`, so a reader re-deriving the threshold runs a shell loop
    rather than editing the source. `monkeypatch.setattr` restores the module global afterwards:
    `main()` assigns it, and a value leaking into another test would silently retune every bound.
    """
    monkeypatch.setattr(vhs, 'MIN_RUN_CHARS', vhs.MIN_RUN_CHARS)
    _fake_repo(tmp_path, monkeypatch,
               before={'registers/handoffs/HANDOFF_IN.md': _wrap(PARAGRAPH, 70) + '\n'},
               live={'IN': _wrap(PARAGRAPH, 38) + '\n'})

    assert vhs.main(['verify_handoff_split.py', '--stress', '2', '0',
                     '--min-run-chars', '31']) == 0
    assert 'MIN_RUN_CHARS=31' in capsys.readouterr().out
    assert vhs.MIN_RUN_CHARS == 31, 'the flag must actually move the bound, not just print it'
