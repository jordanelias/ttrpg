#!/usr/bin/env python3
"""
prose_writer_consistency_check.py

Validates cross-file consistency across the prose-writer skill's four core files.
Uses inline <!-- author:name --> and <!-- concept:name --> tags.

Run after any edit to prose-writer files. Hook candidate for safe_commit.

Usage: python3 prose_writer_consistency_check.py
Exit code: 0 = pass, 1 = failures found
"""

import os, sys, re, json, urllib.request, base64

PAT_PATH = '/home/claude/.valoria_pat'
if not os.path.exists(PAT_PATH):
    PAT_PATH = '/mnt/project/VALORIA_PAT'
PAT = open(PAT_PATH).read().strip()

REPO = 'jordanelias/ttrpg'
FILES = {
    'skill': 'skills/prose-writer/SKILL.md',
    'anti-patterns': 'skills/prose-writer/references/anti-patterns-skeleton.md',
    'techniques': 'skills/prose-writer/references/techniques-skeleton.md',
    'lit-review': 'skills/prose-writer/references/literary-review-technique.md',
}

EXPECTED_AUTHORS = [
    'tolkien', 'ishiguro', 'mistry', 'tartt', 'marquez',
    'borges', 'lispector', 'ocampo', 'beckett', 'lem',
    'mccarthy', 'lecarre',
]

EXPECTED_CONCEPTS = [
    'observing-around', 'exteriority', 'agent-insufficiency',
    'spirit-axis', 'wittgenstein', 'within-observation-gradient',
]

# Concept presence requirements per file
# None = not required in this file
CONCEPT_REQUIRED_IN = {
    'observing-around': ['skill', 'anti-patterns', 'techniques', 'lit-review'],
    'exteriority': ['skill', 'anti-patterns', 'techniques', 'lit-review'],
    'agent-insufficiency': ['skill', 'anti-patterns', 'techniques'],
    'spirit-axis': ['skill', 'anti-patterns', 'techniques'],
    'wittgenstein': ['anti-patterns'],
    'within-observation-gradient': ['anti-patterns'],
}

# Author presence requirements
# skill has 'all-weights' instead of individual tags
AUTHOR_REQUIRED_IN = ['anti-patterns', 'techniques', 'lit-review']


def fetch_file(path):
    req = urllib.request.Request(
        f'https://api.github.com/repos/{REPO}/contents/{path}?ref=main',
        headers={'Authorization': f'token {PAT}', 'Accept': 'application/vnd.github.v3+json'}
    )
    with urllib.request.urlopen(req) as r:
        return base64.b64decode(json.loads(r.read())['content']).decode()


def get_tags(content):
    authors = set(re.findall(r'<!-- author:(\S+) -->', content))
    concepts = set(re.findall(r'<!-- concept:([\S]+) -->', content))
    return authors, concepts


def get_concept_context(content, concept, chars=500):
    """Extract text near a concept tag for keyword checking."""
    pattern = f'<!-- concept:{concept} -->'
    idx = content.find(pattern)
    if idx == -1:
        return ''
    return content[idx:idx+chars].lower()


def main():
    print("Prose-Writer Cross-File Consistency Check")
    print("=" * 50)

    contents = {}
    for label, path in FILES.items():
        try:
            contents[label] = fetch_file(path)
        except Exception as e:
            print(f"FAIL: Could not fetch {path}: {e}")
            return 1

    failures = []

    # 1. Author tag coverage
    print("\n--- Author Tag Coverage ---")
    for label in AUTHOR_REQUIRED_IN:
        authors, _ = get_tags(contents[label])
        missing = set(EXPECTED_AUTHORS) - authors
        if missing:
            failures.append(f"{label}: missing author tags: {sorted(missing)}")
            print(f"  FAIL {label}: missing {sorted(missing)}")
        else:
            print(f"  OK   {label}: all 12 authors tagged")

    # SKILL.md uses all-weights
    sk_authors, _ = get_tags(contents['skill'])
    if 'all-weights' not in sk_authors:
        failures.append("skill: missing author:all-weights tag on weighting table")
        print(f"  FAIL skill: missing all-weights tag")
    else:
        print(f"  OK   skill: all-weights tag present")

    # 2. Concept tag coverage
    print("\n--- Concept Tag Coverage ---")
    for concept, required_files in CONCEPT_REQUIRED_IN.items():
        for label in required_files:
            _, concepts = get_tags(contents[label])
            if concept not in concepts:
                failures.append(f"{label}: missing concept tag: {concept}")
                print(f"  FAIL {label}: missing <!-- concept:{concept} -->")
            else:
                print(f"  OK   {label}: {concept}")

    # 3. Key term consistency near concept tags
    print("\n--- Key Term Consistency ---")
    CONCEPT_TERMS = {
        'exteriority': ['action', 'opaque'],  # 'body' or 'character' — either valid
        'agent-insufficiency': ['dissolv'],  # 'insufficient' or 'dissolving' — either valid
        'observing-around': ['around'],  # 'circle' or 'describe around' — either valid
    }
    for concept, terms in CONCEPT_TERMS.items():
        for label in CONCEPT_REQUIRED_IN.get(concept, []):
            ctx = get_concept_context(contents[label], concept, 800)
            if not ctx:
                continue  # Already caught by tag coverage
            missing_terms = [t for t in terms if t not in ctx]
            if missing_terms:
                failures.append(f"{label}/{concept}: concept section missing key terms: {missing_terms}")
                print(f"  WARN {label}/{concept}: missing terms {missing_terms}")
            else:
                print(f"  OK   {label}/{concept}: key terms present")

    # 4. Achronism check (no modern scientific terms in prose sections)
    print("\n--- Achronism Check ---")
    ACHRONISMS = ['frequency', 'oscillat', 'temperature', 'celsius', 'fahrenheit', 
                  'hertz', 'wavelength', 'voltage', 'ampere', 'thermometer']
    for label in ['anti-patterns', 'techniques', 'lit-review']:
        content_lower = contents[label].lower()
        found = [t for t in ACHRONISMS if t in content_lower]
        if found:
            # Check if they're in meta/audit context vs prose prescription
            real_issues = []
            for term in found:
                for m in re.finditer(term, content_lower):
                    ctx = content_lower[max(0,m.start()-100):m.end()+100]
                    # Skip if in negation/warning/diagnostic context
                    if any(neg in ctx for neg in [f'no {term}', f'not {term}', f'not "{term}', "don't", 'never', 'pronoun {}'.format(term), 'not "', '— not']):
                        continue
                    real_issues.append(term)
                    break
            if real_issues:
                failures.append(f"{label}: potential achronism: {real_issues}")
                print(f"  WARN {label}: check terms {real_issues}")
            else:
                print(f"  OK   {label}: achronisms in negation context only")
        else:
            print(f"  OK   {label}: no achronistic terms")

    # 5. Galbados check
    print("\n--- Canonical Name Check ---")
    for label, content in contents.items():
        if 'galbados' in content.lower():
            # Allow "never Galbados"
            gal_contexts = [content[max(0,m.start()-20):m.end()+20] 
                          for m in re.finditer(r'(?i)galbados', content)]
            real_issues = [c for c in gal_contexts if 'never' not in c.lower()]
            if real_issues:
                failures.append(f"{label}: Galbados without 'never' context")
                print(f"  FAIL {label}: Galbados used outside canonical rule")
            else:
                print(f"  OK   {label}: Galbados only in 'never Galbados'")
        else:
            print(f"  OK   {label}: no Galbados")

    # Summary
    print(f"\n{'=' * 50}")
    if failures:
        print(f"FAILURES: {len(failures)}")
        for f in failures:
            print(f"  - {f}")
        return 1
    else:
        print("ALL CHECKS PASSED")
        return 0


if __name__ == '__main__':
    sys.exit(main())
