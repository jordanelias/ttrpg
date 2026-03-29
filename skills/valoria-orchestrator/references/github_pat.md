# GitHub PAT

PAT: [REDACTED — do not store PAT on GitHub; set GITHUB_PAT env var or load from local file]

Repo: jordanelias/ttrpg
Branch: main

## Usage
```python
import os
# Set before running any github_ops functions:
os.environ["GITHUB_PAT"] = "your_pat_here"
```

## If 401
PAT has expired. User must regenerate at:
github.com → Settings → Developer settings → Personal access tokens
Scope required: repo (full)
Update GITHUB_PAT environment variable.
