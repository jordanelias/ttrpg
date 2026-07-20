window.VALORIA_REVIEW = {
  "schema_version": 1,
  "generated_epoch": 1784513847,
  "head_sha": "1c58bd9d8ed0287f477044c4663e7150ce819657",
  "rollup": {
    "grade": "AMBER",
    "blocking_failures": 0,
    "regressions_vs_baseline": 0,
    "report_only_failures": 2,
    "errors": 0,
    "signal_count": 5
  },
  "signals": [
    {
      "id": "currency.stamps",
      "source": "tools/currency_consistency_check.py",
      "tier": "report_only",
      "lane": "IN",
      "verdict": "fail",
      "returncode": 1,
      "elapsed_ms": 417,
      "detail": [
        "  CURRENT.md names nonexistent path: designs/audit/2026-07-12-pr119-harness-verification/",
        "  CURRENT.md names nonexistent path: designs/audit/2026-07-14-governance-vector-audit/",
        "  CURRENT.md names nonexistent path: designs/audit/2026-07-14-scale-chain-and-decision-surface-map/",
        "  CURRENT.md names nonexistent path: designs/audit/2026-07-15-proposal-reconciliation/"
      ],
      "baseline": 1,
      "regressed": false
    },
    {
      "id": "vocab.a17",
      "source": "tools/ci_quantity_vocabulary_check.py",
      "tier": "report_only",
      "lane": "IN",
      "verdict": "fail",
      "returncode": 1,
      "elapsed_ms": 178,
      "detail": [
        "  UNRESOLVED [module_contracts.yaml:state] personal_combat: 'Wounds' (from 'Wounds')",
        "  UNRESOLVED [module_contracts.yaml:state] personal_combat: 'Initiative' (from 'Initiative')",
        "  UNRESOLVED [module_contracts.yaml:state] personal_combat: 'Poise' (from 'Poise')",
        "  UNRESOLVED [module_contracts.yaml:derivations.inputs] personal_combat: 'cumulative_damage' (from 'cumulative_damage')"
      ],
      "baseline": 36,
      "regressed": false
    },
    {
      "id": "wiring.coverage",
      "source": "tools/wiring_map_check.py",
      "tier": "report_only",
      "lane": "IN",
      "verdict": "pass",
      "returncode": 0,
      "elapsed_ms": 111,
      "detail": [
        "\u2713 wiring manifest valid \u2014 27/27 modules \u00b7 7/7 adapters \u00b7 all tags resolve in their live registries."
      ],
      "baseline": 1,
      "regressed": false
    },
    {
      "id": "audit.staleness",
      "source": "tools/audit_staleness.py",
      "tier": "info",
      "lane": "IN",
      "verdict": "pass",
      "returncode": 0,
      "elapsed_ms": 156,
      "detail": [
        "  (no data for: vector-audit, npc-audit)",
        "top-2 stalest (what session_status.py surfaces):",
        "  \u26a0 audit stale: mechanics-index \u2014 1082 in-scope file(s) changed since last refresh (6dd2f9f, 2026-07-17) \u2014 see tools/audit_staleness.py for detail",
        "  \u26a0 audit stale: decisions-digest \u2014 1044 in-scope file(s) changed since last refresh (92e50da, 2026-07-18) \u2014 see tools/audit_staleness.py for detail"
      ],
      "baseline": null,
      "regressed": false
    },
    {
      "id": "workplan.state",
      "source": "tools/workplan_status.py",
      "tier": "info",
      "lane": "IN",
      "verdict": "pass",
      "returncode": 0,
      "elapsed_ms": 124,
      "detail": [
        "workplan: M1 0/7 junctures done (4 in progress, 1 blocked) \u00b7 next: M1 Strategic decision: author the domain_actions home (ED-FA-0002) + ratification-flip ... \u00b7 T0 open: 1",
        "\u26a0 383 workplan-relevant file(s) changed since the board's last refresh (as_of 470aa09) \u2014 the navigator skill refreshes it on use"
      ],
      "baseline": null,
      "regressed": false
    }
  ],
  "subsystems": {
    "IN": {
      "grade": "AMBER",
      "signals": [
        "currency.stamps",
        "vocab.a17",
        "wiring.coverage",
        "audit.staleness",
        "workplan.state"
      ]
    }
  }
};
