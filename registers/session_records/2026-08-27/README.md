# Session record — 2026-08-27 (IN + SC + PC)

Two campaign-output captures, and what they measure. Committed at Jordan's instruction
("ensure you commit scratchpads") so the evidence trail for six golden re-pins outlives a
`/tmp` directory.

## The files

| file | tree state | what it is |
|---|---|---|
| `capture_pre_ladder_migration.json` | `3d04568` (main, before this branch) | the baseline every "did anything move" question in this session was asked against |
| `capture_post_all_changes.json` | `d7578a6` | the final state after all four commits |

Each is `python tools/campaign_output_probe.py` — five seeded campaigns (0/1/7/13/42) and both
pinned batches (n=2 seed-0, n=8 seed-42), every field of every result, `key_log_hash` included.

**They are not goldens and nothing gates them.** The goldens live in `engine/tests/` and run in
CI's `sim-regression` job. These are a dated reference point: a next reader can diff a fresh
capture against `capture_post_all_changes.json` and know immediately whether the tree still
produces what it produced here. Regenerate either by checking out the named SHA and running the
probe — verified, they reproduce byte-for-byte.

## What actually moved, and what did not

**ONE of the four commits moved output. The other three were byte-identical, and that was the
point of each of them.**

| commit | change | output |
|---|---|---|
| `ab8d156` | ED-IN-0199 — `engine_clock` exists; the tick's clock calls leave the ACTION phase | **BYTE-IDENTICAL** |
| `63efdc0` | ED-SC-0031 — the ninth degree ladder migrates to the single owner | **MOVED** (see below) |
| `784d252` | the anti-fabrication gate fix | no code path touched |
| `d7578a6` | ED-SC-0032 / ED-PC-0057 — the injection seam, the ceiling abolition | **BYTE-IDENTICAL** |

The whole delta between these two captures is attributable to `63efdc0`:

```
campaign_0    Crown     -> Varfell     key_log_hash 7025bd8db236 -> fabb99611758
campaign_1    Varfell   -> Crown                    97548ae7431b -> 8f4cfabd4bed
campaign_7    Crown     -> Crown                    4d56f495a703 -> a9afe21710f1
campaign_13   Hafenmark -> Church                   12df2f60f105 -> 14dc28e4b9f8
campaign_42   Crown     -> Crown                    f65046eb3ffb -> 59009dc238b0
batch_0_2     win_share UNCHANGED (battles_mean 34.5 -> 36.0)
batch_42_8    {Church 25, Crown 62.5, Hafenmark 0, Varfell 12.5}
           -> {Church  0, Crown 12.5, Hafenmark 12.5, Varfell 75}
```

⚠ **THAT SWING IS NOT A BALANCE RESULT AND MUST NOT BE READ AS ONE.** Six of eight campaigns
change winner at n=8, where one campaign is 12.5pp. The control is `tools/balance_oracle.py` at
**n=120 per arm**, both arms in one process:

| faction | private_ladder | owner_ladder | delta pp | z |
|---|---|---|---|---|
| Church | 7.5% | 5.0% | −2.5 | −0.80 |
| Crown | 51.7% | 55.0% | +3.3 | +0.52 |
| Hafenmark | 10.0% | 10.0% | +0.0 | +0.00 |
| Varfell | 30.8% | 30.0% | −0.8 | −0.14 |

Nothing significant (threshold 1.96; max 0.80). Read as that tool's own docstring instructs: it
**bounds** the effect, it does not exclude one, and a two-proportion z under-detects on paired
arms. This gap — a dramatic small-n swing over a null n=120 control — is exactly what the oracle
exists to distinguish, and is why the six goldens were re-pinned rather than investigated as a
regression.

## What is deliberately NOT here

- **The adversarial-pass reports.** Three read-only critics reviewed these commits and found 32
  defects between them. Every finding is folded into the ledger rows (`ED-IN-0199`,
  `ED-SC-0031`, `ED-SC-0032`, `ED-PC-0057`) and the commit messages, which is where CLAUDE.md §0
  says a pass's output belongs — "edits to the thing under review, and at most one paragraph in
  the commit message", never a document. Preserving the reports would be creating the category
  §0 retired.
- **Intermediate captures and test logs.** Four more captures were taken mid-session; all four
  are byte-identical to `capture_post_all_changes.json` except the pre-migration one kept here.
  Storing duplicates of a file to record that they were duplicates is not a record.
- **The diffs.** `git log -p` is the diff, and it does not rot.
