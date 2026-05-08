#!/usr/bin/env python3
"""
prose_writer_consistency_check.py

Validates cross-file consistency across the prose-writer skill's four core files
plus spot-checks the test battery for design vocabulary leaks.

Uses inline <!-- author:name --> and <!-- concept:name --> tags.

Run after any edit to prose-writer files. Hook candidate for safe_commit.

Usage: python3 prose_writer_consistency_check.py
Exit code: 0 = pass, 1 = hard failures found (warnings do not fail build)
"""

import os, sys, re, json, urllib.request, base64

REPO = 'jordanelias/ttrpg'

CORE_FILES = {
    'skill': 'skills/prose-writer/SKILL.md',
    'anti-patterns': 'skills/prose-writer/references/anti-patterns-skeleton.md',
    'techniques': 'skills/prose-writer/references/techniques-skeleton.md',
    'lit-review': 'skills/prose-writer/references/literary-review-technique.md',
}

TEST_BATTERY_FILES = [
    'skills/prose-writer/references/test-battery-part5.md',
    'skills/prose-writer/references/test-battery-part6.md',
]

CONCEPT_REQUIRED_IN = {
    'observing-around':           ['skill', 'anti-patterns', 'techniques', 'lit-review'],
    'exteriority':                ['skill', 'anti-patterns', 'techniques', 'lit-review'],
    'agent-insufficiency':        ['skill', 'anti-patterns', 'techniques'],
    'spirit-axis':                ['skill', 'anti-patterns', 'techniques'],
    'wittgenstein':               ['anti-patterns'],
    'within-observation-gradient':['anti-patterns'],
}

CONCEPT_TERMS = {
    'exteriority':        ['action', 'opaque'],
    'agent-insufficiency':['dissolv'],
    'observing-around':   ['around'],
}

ACHRONISMS = [
    'oscillat', 'celsius', 'fahrenheit', 'hertz', 'wavelength',
    'voltage', 'ampere', 'thermometer', 'centigrade', 'thermal',
]

DESIGN_VOCAB = [
    'ein sof', 'mending stability', 'thread sensitivity',
    'conviction track', 'rendering stability',
]

SECTION_IDS = {
    'I.1','I.2','I.3','I.4','I.5','I.6','I.6b','I.7','I.8',
    'II.1','II.2','II.3','II.4','II.5',
    'III.1','III.2','III.3',
    'IV.1','IV.2',
    'V.1','V.2','V.3','V.4','V.5','V.6','V.7','V.8',
    'V.9','V.10','V.11','V.12','V.13',
    'VI.1','VI.2','VI.3','VI.4',
    'D.1','D.2','D.3','D.4','D.5','D.6',
}

AUTHOR_REQUIRED_IN = ['anti-patterns', 'techniques', 'lit-review']


def load_pat():
    for path in ['/home/claude/.valoria_pat', '/mnt/project/VALORIA_PAT']:
        if os.path.exists(path):
            return open(path).read().strip()
    raise FileNotFoundError("No PAT found at expected paths")


def fetch_file(pat, path):
    req = urllib.request.Request(
        f'https://api.github.com/repos/{REPO}/contents/{path}?ref=main',
        headers={'Authorization': f'token {pat}', 'Accept': 'application/vnd.github.v3+json'}
    )
    with urllib.request.urlopen(req) as r:
        data = json.loads(r.read())
        return base64.b64decode(data['content']).decode()


def get_tags(content):
    r"""Extract author and concept tags using strict [\w-]+ ID pattern."""
    authors = set(re.findall(r'<!-- author:([\w-]+) -->', content))
    concepts = set(re.findall(r'<!-- concept:([\w-]+) -->', content))
    return authors, concepts


def get_concept_contexts(content, concept, chars=800):
    """Extract text after ALL occurrences of a concept tag."""
    pattern = f'<!-- concept:{concept} -->'
    return [
        content[m.end():m.end() + chars].lower()
        for m in re.finditer(re.escape(pattern), content)
    ]


def normalize_author_id(name):
    """Convert SKILL.md display name to tag ID format."""
    return (name.lower()
               .replace('é', 'e').replace('á', 'a').replace('ó', 'o')
               .replace(' (silvina)', '').replace(' ', '')
               .replace("'", '').replace('.', '').strip())


def derive_expected_authors(skill_content):
    """
    Parse expected author list from SKILL.md weighting table.
    Avoids hardcoding — stays in sync when roster changes.
    Only accepts rows where first cell looks like an author name
    (letters, spaces, accents, apostrophes) and second cell is a number.
    """
    match = re.search(r'## Author Weighting.*?(\|.*?)\n## ', skill_content, re.DOTALL)
    if not match:
        return None
    table = match.group(1)
    ids = []
    for row in table.split('\n'):
        cells = [c.strip() for c in row.split('|') if c.strip()]
        if len(cells) < 2:
            continue
        name, second = cells[0], cells[1]
        # Skip header/divider rows
        if name.startswith('-') or name == 'Author':
            continue
        # Only accept rows where second cell is a number (weight column)
        if not re.match(r'^\d+$', second.replace('%', '').strip()):
            continue
        aid = normalize_author_id(name)
        if aid:
            ids.append(aid)
    return ids


def in_negation_context(ctx, term):
    negators = [
        f'no {term}', f'not {term}', f'not "{term}',
        "don't", 'never', '— not', 'avoid', 'without',
        f'pronoun {term}',
    ]
    return any(neg in ctx for neg in negators)


def main():
    print("Prose-Writer Cross-File Consistency Check")
    print("=" * 50)

    try:
        pat = load_pat()
    except FileNotFoundError as e:
        print(f"FAIL: {e}")
        return 1

    contents = {}
    for label, path in CORE_FILES.items():
        try:
            contents[label] = fetch_file(pat, path)
        except Exception as e:
            print(f"FAIL: Could not fetch {path}: {e}")
            return 1

    battery_contents = {}
    for path in TEST_BATTERY_FILES:
        try:
            battery_contents[path] = fetch_file(pat, path)
        except Exception as e:
            print(f"WARN: Could not fetch {path}: {e}")

    failures = []
    warnings = []

    # 1. Derive expected authors from SKILL.md
    print("\n--- Author Roster ---")
    expected_ids = derive_expected_authors(contents['skill'])
    if expected_ids is None:
        failures.append("Could not parse author weighting table from SKILL.md")
        print("  FAIL: Cannot parse author table")
        expected_ids = []
    else:
        print(f"  Derived {len(expected_ids)} authors: {expected_ids}")

    # 2. Author tag coverage
    print("\n--- Author Tag Coverage ---")
    for label in AUTHOR_REQUIRED_IN:
        authors, _ = get_tags(contents[label])
        missing = set(expected_ids) - authors
        extra = authors - set(expected_ids) - {'all-weights'}
        if missing:
            failures.append(f"{label}: missing author tags: {sorted(missing)}")
            print(f"  FAIL {label}: missing {sorted(missing)}")
        else:
            if extra:
                warnings.append(f"{label}: unexpected author tags (roster drift?): {sorted(extra)}")
                print(f"  WARN {label}: unexpected tags {sorted(extra)}")
            print(f"  OK   {label}: {len(authors)} author tags present")

    sk_authors, _ = get_tags(contents['skill'])
    if 'all-weights' not in sk_authors:
        failures.append("skill: missing author:all-weights tag")
        print("  FAIL skill: missing all-weights tag")
    else:
        print("  OK   skill: all-weights tag present")

    # 3. Concept tag coverage
    print("\n--- Concept Tag Coverage ---")
    for concept, required_files in sorted(CONCEPT_REQUIRED_IN.items()):
        for label in required_files:
            _, concepts = get_tags(contents[label])
            if concept not in concepts:
                failures.append(f"{label}: missing <!-- concept:{concept} -->")
                print(f"  FAIL {label}: missing {concept}")
            else:
                print(f"  OK   {label}: {concept}")

    # 4. Key term consistency near concept tags (warnings only — synonyms accepted)
    print("\n--- Concept Key Terms (warnings only) ---")
    for concept, terms in sorted(CONCEPT_TERMS.items()):
        for label in CONCEPT_REQUIRED_IN.get(concept, []):
            ctxs = get_concept_contexts(contents[label], concept)
            if not ctxs:
                continue
            # Pass if any single occurrence contains all required terms
            passed = any(all(t in ctx for t in terms) for ctx in ctxs)
            if not passed:
                warnings.append(f"{label}/{concept}: terms {terms} absent near all tag occurrences")
                print(f"  WARN {label}/{concept}: {terms}")
            else:
                print(f"  OK   {label}/{concept}")

    # 5. Achronism check (hard fail — prescriptive context only)
    print("\n--- Achronism Check ---")
    for label in ['anti-patterns', 'techniques', 'lit-review']:
        cl = contents[label].lower()
        real_issues = []
        for term in ACHRONISMS:
            if term not in cl:
                continue
            for m in re.finditer(re.escape(term), cl):
                ctx = cl[max(0, m.start() - 120): m.end() + 120]
                if not in_negation_context(ctx, term):
                    real_issues.append(f"'{term}'")
                    break
        if real_issues:
            failures.append(f"{label}: achronistic term(s) in prescriptive context: {real_issues}")
            print(f"  FAIL {label}: {real_issues}")
        else:
            print(f"  OK   {label}")

    # 6. Test battery design vocabulary leaks
    print("\n--- Test Battery Design Vocab ---")
    for path, content in battery_contents.items():
        short = path.split('/')[-1]
        passages = re.findall(r'\*\n\n(.*?)\n\n\*\*(?:Audit|Findings)', content, re.DOTALL)
        issues = []
        for i, p in enumerate(passages):
            pl = p.lower()
            for term in DESIGN_VOCAB:
                if term in pl:
                    issues.append(f"passage {i+1}: '{term}'")
        if issues:
            failures.append(f"{short}: design vocab leak: {issues}")
            print(f"  FAIL {short}: {issues}")
        elif passages:
            print(f"  OK   {short}: {len(passages)} passages clean")
        else:
            warnings.append(f"{short}: no passages extracted — regex may need updating")
            print(f"  WARN {short}: no passages found")

    # 7. Cross-reference validity (warnings — section IDs can evolve)
    print("\n--- Cross-Reference Check (warnings only) ---")
    ap = contents['anti-patterns']
    refs = set(re.findall(r'\(See ([\w.]+)', ap) + re.findall(r'see ([\w.]+)', ap))
    # Only check things that look like section IDs (X.Y format)
    section_refs = {r for r in refs if re.match(r'^[IVD]+\.\d+\w*$', r)}
    bad = sorted(section_refs - SECTION_IDS)
    if bad:
        warnings.append(f"anti-patterns: cross-refs not in known section IDs: {bad}")
        print(f"  WARN anti-patterns: unresolved section refs: {bad}")
    else:
        print(f"  OK   anti-patterns: {len(section_refs)} section refs resolve")

    # 8. Canonical name check
    print("\n--- Canonical Name Check ---")
    for label, content in contents.items():
        if 'galbados' in content.lower():
            ctxs = [content[max(0, m.start()-25):m.end()+25]
                    for m in re.finditer(r'(?i)galbados', content)]
            bad = [c for c in ctxs if 'never' not in c.lower()]
            if bad:
                failures.append(f"{label}: 'Galbados' outside 'never Galbados'")
                print(f"  FAIL {label}: Galbados outside canonical context")
            else:
                print(f"  OK   {label}: Galbados in canonical context only")
        else:
            print(f"  OK   {label}: no Galbados")

    # Summary
    print(f"\n{'=' * 50}")
    if warnings:
        print(f"WARNINGS ({len(warnings)}) — do not fail build:")
        for w in warnings:
            print(f"  ! {w}")
    if failures:
        print(f"\nFAILURES ({len(failures)}):")
        for f in failures:
            print(f"  ✗ {f}")
        return 1
    print(f"\n{'PASSED (with warnings)' if warnings else 'ALL CHECKS PASSED'}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
