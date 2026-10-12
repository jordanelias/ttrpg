"""modules/ -- the A-25 modules: reachable running code only, one directory per module
(`ED-IN-0284`, revised by `ED-IN-0285`). A module is reached by a composition row
(`references/module_contracts.yaml` `composition_roles:`), resolved by string at driver
construction; `engine/` never imports it. The root is `tools/ci_common.py`'s `MODULE_CODE_ROOTS`.
"""
