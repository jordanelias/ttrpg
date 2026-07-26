"""
Unit tests for the no-self-scheduling rule (ED-IN-0084, CLAUDE.md §11).

This is the FALSIFIER for the rule, per CLAUDE.md §0.1 point 3: the rule's claim is
"this repo cannot arm its own wake-ups", and these tests are what would show it false.
They pin the two artifacts that carry the rule — the `permissions.deny` list in
.claude/settings.json (the single owner) and CLAUDE.md §11 (the doctrine) — so that
dropping either turns the suite red rather than silently restoring the waste class.

Background: in the 2026-07-19..26 window, 116 `send_later` self check-ins re-entered
persistent sessions to re-confirm PRs that were already green (97/118 trigger prompts
said so). A wake-up re-sends the whole conversation; with an EMPTY conversation that is
still ~23.2k tokens (CLAUDE.md alone is ~12.2k), so the floor was ~2.7M tokens for zero
state change. The median wake-to-wake gap was 61.9 min, just past the 1h prompt-cache
TTL, so most of it was uncached.

NOTE on scope: no test can observe a *hosted* session actually calling the tool. What is
testable is that the deny-list and the doctrine are present and cover every primitive we
know of. If a session ever schedules a wake-up while these pass, the guard is not wrong
about its artifacts — it is incomplete about the roster, and the new primitive belongs in
REQUIRED_DENY here and in tools/ci_hooks_verifier.py (which owns the CI-side copy).
"""
import json
import os

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SETTINGS = os.path.join(ROOT, '.claude', 'settings.json')
CLAUDE_MD = os.path.join(ROOT, 'CLAUDE.md')

# Every self-scheduling primitive known as of ED-IN-0084. `send_later` is the one that
# produced all 116 measured firings; `create_trigger` is its underlying Routine API and
# therefore the obvious route-around; ScheduleWakeup and CronCreate are the /loop pacing
# and fixed-interval equivalents.
REQUIRED_DENY = (
    'send_later',
    'create_trigger',
    'ScheduleWakeup',
    'CronCreate',
)


def _deny_list():
    with open(SETTINGS, encoding='utf-8') as f:
        cfg = json.load(f)
    return cfg.get('permissions', {}).get('deny', [])


def test_settings_json_is_valid_json():
    # A malformed settings.json silently drops BOTH the deny-list and the hooks, so the
    # parse itself is load-bearing, not incidental.
    with open(SETTINGS, encoding='utf-8') as f:
        assert isinstance(json.load(f), dict)


def test_deny_list_covers_every_self_scheduling_primitive():
    blob = '\n'.join(str(d) for d in _deny_list())
    missing = [t for t in REQUIRED_DENY if t not in blob]
    assert not missing, (
        f"permissions.deny in .claude/settings.json no longer blocks {missing}. "
        f"ED-IN-0084: sessions must not arm their own wake-ups.")


def test_mcp_denies_cover_the_server_name_spellings():
    # The claude-code-remote MCP server is surfaced under different name normalizations
    # across surfaces (Claude_Code_Remote / claude-code-remote / claude_code_remote). A
    # deny rule matches the tool's fully-qualified name, so one spelling is not enough:
    # a session on a surface that normalizes differently would sail straight past it.
    deny = _deny_list()
    for tool in ('send_later', 'create_trigger'):
        spellings = {d.split('__')[1] for d in deny
                     if d.startswith('mcp__') and d.endswith(f'__{tool}')}
        assert {'Claude_Code_Remote', 'claude-code-remote', 'claude_code_remote'} <= spellings, (
            f"deny rules for {tool} do not cover every server-name spelling; "
            f"found {sorted(spellings)}")


def test_hooks_survive_alongside_the_deny_list():
    # Regression guard on the edit that introduced permissions: the deny-list was added
    # to a file whose only prior content was the hooks block. Losing the hooks would
    # disable the naming guard and the SessionStart banner.
    with open(SETTINGS, encoding='utf-8') as f:
        cfg = json.load(f)
    hooks = cfg.get('hooks', {})
    assert {'PreToolUse', 'SessionStart', 'Stop'} <= set(hooks)


def test_claude_md_documents_the_rule():
    with open(CLAUDE_MD, encoding='utf-8') as f:
        text = f.read()
    assert 'does not self-schedule' in text, "CLAUDE.md §11 (ED-IN-0084) is missing"
    assert 'ED-IN-0084' in text
