# Provenance — the text the review was run against

**The reviewed text is the body of the five files in `canon/`, below their `⚠ SUPERSEDED` banners.**
Nothing below those banners was edited. Every quotation in `_review/` and in
`DISCUSSION_SUPPLEMENT.md` is verifiable there directly.

**For byte-exactness**, the five documents as supplied — with no banner — are at commit
`2071b146b661a56cdd0d268b791dcb91e074a41f`:

```
git show 2071b146b661a56cdd0d268b791dcb91e074a41f:canon/philosophy/_sources/00_philosophical_foundations.md
git show 2071b146b661a56cdd0d268b791dcb91e074a41f:canon/philosophy/_sources/00_philosophical_foundations_rules.md
git show 2071b146b661a56cdd0d268b791dcb91e074a41f:canon/philosophy/_sources/01_foundations_amendment_self_rendering.md
git show 2071b146b661a56cdd0d268b791dcb91e074a41f:canon/philosophy/_sources/02_canon_constraints.md
git show 2071b146b661a56cdd0d268b791dcb91e074a41f:canon/philosophy/_sources/02_foundations_amendment_leap_mechanism.md
```

| File | md5 as supplied |
|---|---|
| `00_philosophical_foundations.md` | `30752bb85be5f7d390ddf8a1f9b99aab` |
| `00_philosophical_foundations_rules.md` | `90e0936d9c5c8301e99e2a4b91b4290f` |
| `01_foundations_amendment_self_rendering.md` | `b98bb216684923abb097e0a3e58a91f5` |
| `02_canon_constraints.md` | `9f4bf561f93c5460092ad8d5f748143b` |
| `02_foundations_amendment_leap_mechanism.md` | `4bec3b329ed8fd1a341b9de9653791c3` |

A sixth upload was a byte-identical duplicate of the Leap amendment; the suite is five documents.

**Why there is no `_sources/` directory.** There was one, and it was deleted. It held unbannered
copies of files that still exist in `canon/` — a second copy of text that git already keeps, in a
directory nothing would visit. `CLAUDE.md` §3 retired the repository's `deprecated/` tree on exactly
that reasoning: *"a graveyard nothing visits is just a second copy of git log."* The bannered originals
are not a graveyard, because seventy files cite them.
