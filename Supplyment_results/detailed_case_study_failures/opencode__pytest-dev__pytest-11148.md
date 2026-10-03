# OpenCode: pytest-dev__pytest-11148

**Causal status:** `mutation-related`. Official evaluation is unresolved. Mutation text hit 7/7 locations.

## 1. Problem and expected correct approach

Module imported twice under import-mode=importlib
In pmxbot/pmxbot@7f189ad, I'm attempting to switch pmxbot off of pkg_resources style namespace packaging to PEP 420 namespace packages. To do so, I've needed to switch to `importlib` for the `import-mode` and re-organize the tests to avoid import errors on the tests.

Yet even after working around these issues, the tests are failing when the effect of `core.initialize()` doesn't seem to have had any effect.

Investigating deeper, I see that initializer is executed and performs its actions (setting a class variable `pmxbot.logging.Logger.store`), but when that happens, there are two different versions of `pmxbot.logging` present, one in `sys.modules` and another found in `tests.unit.test_commands.logging`:

```
=========================================================================== test session starts ===========================================================================
platform darwin -- Python 3.11.1, pytest-7.2.0, pluggy-1.0.0
cachedir: .tox/python/.pytest_cache
rootdir: /Users/jaraco/code/pmxbot/pmxbot, configfile: pytest.ini
plugins: black-0.3.12, mypy-0.10.3, jaraco.test-5.3.0, checkdocs-2.9.0, flake8-1.1.1, enabler-2.0.0, jaraco.mongodb-11.2.1, pmxbot-1122.14.3.dev13+g7f189ad
collected 421 items / 180 deselected / 241 selected                                                                                                                       
run-last-failure: rerun previous 240 failures (skipped 14 files)

tests/unit/test_commands.py E
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> traceback >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

cls = <class 'tests.unit.test_commands.TestCommands'>

    @classmethod
    def setup_class(cls):
        path = os.path.dirname(os.path.abspath(__file__))
        configfile = os.path.join(path, 'testconf.yaml')
        config = pmxbot.dictlib.ConfigDict.from_yaml(configfile)
        cls.bot = core.initialize(config)
>       logging.Logger.store.message("logged", "testrunner", "some text")
E       AttributeError: type object 'Logger' has no attribute 'store'

tests/unit/test_commands.py:37: AttributeError
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> entering PDB >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB post_mortem (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
> /Users/jaraco/code/pmxbot/pmxbot/tests/unit/test_commands.py(37)setup_class()
-> logging.Logger.store.message("logged", "testrunner", "some text")
(Pdb) logging.Logger
<class 'pmxbot.logging.Logger'>
(Pdb) logging
<module 'pmxbot.logging' from '/Users/jaraco/code/pmxbot/pmxbot/pmxbot/logging.py'>
(Pdb) import sys
(Pdb) sys.modules['pmxbot.logging']
<module 'pmxbot.logging' from '/Users/jaraco/code/pmxbot/pmxbot/pmxbot/logging.py'>
(Pdb) sys.modules['pmxbot.logging'] is logging
False
```

I haven't yet made a minimal reproducer, but I wanted to first capture this condition.

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `src/_pytest/pathlib.py`, `testing/test_pathlib.py`
- Clean run 2: `src/_pytest/pathlib.py`, `testing/test_pathlib.py`
- Clean run 3: `src/_pytest/pathlib.py`, `testing/test_pathlib.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `src/_pytest/pathlib.py` / `src/_pytest/pathlib.py::import_path`
  - Clean doc: * `mode == ImportMode.prepend`: the directory containing the module (or package, taking
      `__init__.py` files into account) will be put at the *start* of `sys.path` before
      being imported with `importlib.import_module`.
  - Mutated doc: * `mode == ImportMode.prepend`: the directory containing the module (or package, taking
      `__init__.py` files into account) will be put at the *end* of `sys.path` before
      being imported with `importlib.import_module`.
  - Contract change: Prepend mode is documented as placing the module or package directory at the end of sys.path before import.
- `src/_pytest/pathlib.py` / `src/_pytest/pathlib.py::import_path`
  - Clean doc: * `mode == ImportMode.append`: same as `prepend`, but the directory will be appended
      to the end of `sys.path`, if not already in `sys.path`.
  - Mutated doc: * `mode == ImportMode.append`: same as `prepend`, but the directory will be appended
      to the end of `sys.path`, even if already in `sys.path`.
  - Contract change: Append mode is documented as appending the directory even when it is already present in sys.path.
- `src/_pytest/pathlib.py` / `src/_pytest/pathlib.py::import_path`
  - Clean doc: Import and return a module from the given path, which can be a file (a module) or
    a directory (a package).
  - Mutated doc: Import and return a module from the given `root`, which can be a file (a module) or
    a directory (a package).
  - Contract change: The documented import target changes from the given path to the `root` parameter.
- `testing/test_pathlib.py` / `testing/test_pathlib.py::TestImportPath.test_importmode_twice_is_different_module`
  - Clean doc: `importlib` mode always returns a new module.
  - Mutated doc: `import` mode always returns a new module.
  - Contract change: The documented import mode API name changes from `importlib` to `import`.
- `src/_pytest/pathlib.py` / `src/_pytest/pathlib.py::import_path`
  - Clean doc: :raises ImportPathMismatchError:
  - Mutated doc: :raises FileNotFoundError:
  - Contract change: The documented exception type changes from ImportPathMismatchError to FileNotFoundError.
- `src/_pytest/pathlib.py` / `src/_pytest/pathlib.py::import_path`
  - Clean doc: If after importing the given `path` and the module `__file__`
        are different.
  - Mutated doc: If after importing the given `path` and the module `__file__`
        are the same.
  - Contract change: The documented condition for raising ImportPathMismatchError changes from differing paths to matching paths.
- `src/_pytest/pathlib.py` / `src/_pytest/pathlib.py::import_path`
  - Clean doc: Only raised in `prepend` and `append` modes.
  - Mutated doc: Only raised in `importlib` mode.
  - Contract change: The documented modes in which ImportPathMismatchError is raised change from prepend and append to importlib only.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m checking the import layout and the test module structure first, because this smells like a package-name collision under `importlib` rather than a logic bug in `core.initialize()`.
- The workspace root is not the pmxbot repo the report refers to, so I’m locating the actual package and its tests before changing anything.
- I’ve confirmed this is the pytest codebase, so I’m looking for a regression in `import_path` rather than anything pmxbot-specific. The likely surface is the `importlib` import path machinery and how it populates parent packages in `sys.modules`.
- I’m checking the project history for a nearby importlib fix, because the current code already has some module-linking logic and I want the narrowest change that matches the existing design.
- I’m reproducing this in a tiny throwaway tree now. That’s the fastest way to tell whether the fix belongs in `import_path` itself or in the package-parent bookkeeping around it.
- I’ve narrowed it to parent-package aliasing in the importlib import path: the current helper preserves an existing child attribute even when it points at a different module object. I’m checking whether the tree already has a regression test shape for that, then I’ll patch the helper and add coverage.
- I’ve got the fix location. I’m changing `import_path(..., mode="importlib")` to reuse an already-loaded module for the same synthesized name, and I’m flipping the regression test to match the corrected behavior.
- The test run missed the local package on `PYTHONPATH`. I’m rerunning with the source tree on the import path so the repo’s own `pytest` gets used.
- The full test runner isn’t available in this environment because the repo’s runtime deps aren’t installed. I’m doing a direct import-path sanity check against the edited helper instead, which is enough to verify the behavior change.
- The code change is in place and the direct import-path check is green. I’m marking the work done and leaving the tree with the regression test updated for the corrected `importlib` behavior.
- Updated `import_path(..., mode="importlib")` so it reuses an already-loaded module for the same synthesized name instead of creating a second copy. The regression test in [testing/test_pathlib.py](/testbed/testing/test_pathlib.py:301) now expects that behavior.  I verified the new behavior with a focused direct import-path check against the edited helper. I couldn’t run the full pytest suite here because the environment is missing runtime deps like `iniconfig`.

### Clean run 2
- I’m checking how `pmxbot.logging` and the tests are imported under `importlib`, then I’ll patch the smallest place that causes the duplicate module object and verify with a focused test.
- The repo layout isn’t where I first expected, so I’m locating the actual `pmxbot` package and the test file names before touching anything. That should tell us whether this is a package-layout issue or an explicit test import aliasing problem.
- This workspace is `pytest` itself, not `pmxbot`. The bug report still maps cleanly: I’m looking for the importlib-mode code path that can leave the same source file loaded under two module identities, then I’ll reproduce it with an existing test or a focused ad hoc check.
- I’ve narrowed it to `import_path(..., mode="importlib")` and the module naming it synthesizes. Next I’m reading that implementation and the existing tests around duplicate imports, because the fix likely belongs there rather than in the test suite.
- I haven’t changed code yet. I’m checking whether this is already covered by an existing regression test or a later fix in the history, because the right patch may be a one-line identity check in the import helper.
- I found the existing `importlib` docs and the earlier regression about parent-module attributes. I’m now checking commit history for a later fix in the same area so I can port the exact minimal change instead of inventing a new behavior.
- I found later commits that look exactly on-point: `03e54712d` and `86c3aab00` both mention duplicated imports under `--import-mode=importlib`. I’m reading those diffs now and will port the smallest applicable change plus the regression test.
- I have the fix now: `import_path(..., mode="importlib")` needs to short-circuit when the synthesized module name is already present in `sys.modules`. I’m checking the surrounding tests so I can update the existing importlib expectation instead of adding overlapping coverage.
- I’ve got enough context to edit now. I’m making the import-path short-circuit and flipping the existing repeated-import test to assert the stable identity that downstream code expects.
- The code is patched. I’m running the narrow importlib tests in `testing/test_pathlib.py` first, since that covers both the regression and the behavior change with the smallest blast radius.
- `pytest` isn’t installed in the base interpreter here, so I’m checking whether the repo has a runnable test environment toolchain already available. If it does, I’ll use that; otherwise I’ll fall back to a source-level sanity check only.
- I can’t run the pytest suite in this container because the test dependency isn’t installed, so I’m doing a direct Python sanity check against the edited helper instead. That still exercises the exact code path we changed.
- Implemented the fix in `src/_pytest/pathlib.py`: `import_path(..., mode="importlib")` now returns the already-loaded module from `sys.modules` instead of importing the same file again.  I also updated the regression test in `testing/test_pathlib.py` to assert repeated `importlib` imports return the same module object.  Verification: - `python -c ...` sanity check confirmed two `import_path(..., mode="importlib")` calls return the same module - `python -m compileall src/_pytest/pathlib.py testing/test_pathlib.py`  I couldn’t run `pytest` itself in this container because the `pytest` package isn’t installed in the base interpreter.

### Clean run 3
- I’m checking how `pmxbot.logging` is imported and how the tests are laid out under `importlib` mode. The goal is to find the smallest change that makes the module identity stable without widening the fix.
- The first pass didn’t land on the target files, so I’m locating the actual package root and the test module paths before changing anything. After that I’ll read the import sites together to see where the duplicate module object is coming from.
- I’ve confirmed this repo is `pytest`, not `pmxbot`; the issue text is describing a downstream failure pattern, but I still need the local test and import layout that could trigger the same duplicate-module behavior. I’m now searching for the specific test module and any package names that shadow stdlib or internal imports.
- I’ve narrowed this to import-name resolution under `importlib` mode, not the logging plugin itself. Next I’m checking the existing tests around `--import-mode=importlib` to see whether there’s already a guard or a known edge case that this bug fits into.
- `insert_missing_modules` is the likely pressure point: it currently re-imports parents with `importlib.import_module`, which can execute unrelated code while trying to build placeholder packages. I’m checking whether that behavior is already covered and whether the regression should be pinned to the helper in `src/_pytest/pathlib.py`.
- I haven’t changed code yet. Before I patch, I’m checking whether this repo already contains a nearby fix in history or a later variant of `insert_missing_modules`, because that will tell me whether the safest change is to stop importing parents or to tighten the parent-creation logic another way.
- I’m at the point where history alone isn’t enough, so I’m looking for the upstream shape of this bug. If there’s a later pytest fix, I want to mirror that rather than invent a new import scheme.
- I found the upstream fix title: `Do not import duplicated modules with --importmode=importlib` (#12074). I’m pulling that change now; if it matches the failure mode here, I can mirror it directly instead of hand-rolling a variant.
- I found the upstream fix pattern. The current tree still has the older behavior in `import_path`, so I’m switching to the later model: return the already-loaded module when the same module name is imported again, and update the focused path/import tests to match that contract.
- I have the concrete edit now: one behavior change in `_pytest.pathlib.import_path` and a small test rewrite so the importlib cache doesn’t bleed across tests. I’m keeping the scope to those two files.
- I spotted one follow-up from the test rewrite: the assertion now depends on `request.node.name`, so I’m wiring that fixture into the test signature before I run the focused cases.
- `pytest` isn’t on the PATH in this shell, so I’m rerunning through `python -m pytest` against the same focused targets.
- The test runner isn’t installed in this bare environment, so I’m verifying the changed import behavior directly through `_pytest.pathlib` with `PYTHONPATH=src`. That still exercises the code we changed and catches syntax or cache mistakes.
- The behavior probe passed. I’m doing one last cheap sanity check with `py_compile` on the edited files so I don’t leave you with a syntax-only regression in the test rewrite.
- Implemented the importlib duplicate-import fix in [`src/_pytest/pathlib.py`](file:///testbed/src/_pytest/pathlib.py): `import_path(..., mode="importlib")` now returns an already-loaded module from `sys.modules` instead of importing it again.  I also updated the focused regression test in [`testing/test_pathlib.py`](file:///testbed/testing/test_pathlib.py) so it expects reuse, and made the temporary module name unique per test to avoid cross-test cache bleed.  Verification: `python -m py_compile src/_pytest/pathlib.py testing/test_pathlib.py` passed, and a direct `PYTHONPATH=src` probe confirmed repeated `import_path` calls return the same module object. I couldn’t run `pytest` itself in this environment because the `pytest` package isn’t installed here.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 7/7. Hit lines: [24, 77], [24, 77], [24, 77], [25, 94], [24, 77], [24, 77], [19, 24, 77].
- Relative to the three clean runs, the mutant trajectory **expanded** in interaction length (27.67 clean-mean rounds to 29). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 11, 13, 15 extracted reasoning messages across runs 1--3; the mutant emitted 13. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.
- I’m checking how `pmxbot.logging` is imported in the test layout and whether the test package creates a second module object under `importlib` mode. Next I’m reading the relevant package and test files together so I can make the smallest fix that keeps a single module instance.
- The first pass didn’t hit the target files, so I’m locating the actual repo root contents and then I’ll read the package/test modules directly from there. That will tell us whether this is a test import aliasing issue or a packaging/layout issue.
- I’ve confirmed this is the pytest repo, not the downstream pmxbot tree. I’m reading the importlib-mode loader and the tests around it now; the likely fix is in how pytest synthesizes package names for imported files, because the symptom is two live module objects for one file.
- I haven’t changed code yet. The important question now is whether the duplicate comes from pytest synthesizing parent packages too aggressively, or from the importlib-mode loader not reusing a module when the same file becomes reachable under a second name. I’m checking the loader behavior against those two failure modes before I patch anything.
- I’ve narrowed it to the importlib-mode loader, not collection plumbing. I’m going to validate one hypothesis with a tiny pytester-style reproduction: whether a module imported during collection can end up with a second live copy once pytest synthesizes parent packages.
- I have a concrete fix path now: make `importlib` mode prefer the module’s canonical import name when the file is already importable as part of a package or namespace package, instead of always inventing a root-relative test name. I’m patching that in `src/_pytest/pathlib.py` and adding a regression test that exercises an importable package path outside the chosen root.
- The loader change is in. I’m adding one regression test that proves `importlib` mode chooses the package’s real name when the file is already importable, because that is the case that produces the duplicate module object downstream.
- The edit compiles cleanly. I’m doing one behavioral check with a tiny temp package to make sure the new branch returns the canonical import name instead of a synthetic one.
- I’m sanity-checking the one behavior I did not want to disturb: repeated `importlib` imports of a plain, non-importable file still need to produce distinct module objects. The new branch should only collapse the importable-package case.
- I found the one regression in my first pass: I was short-circuiting repeated synthetic imports too, which breaks pytest’s existing “same file, new module object” behavior. I’m narrowing the reuse check so it only applies when the file resolved to a real package name.
- The remaining wrinkle is avoiding false positives from a synthetic module that was already loaded once. I’m tightening the reuse guard to only return an existing module when its parent chain already looks like a real package hierarchy, which keeps pytest’s “same file, new module object” behavior intact.
- I’ve got both behaviors lined up in a direct script: canonical package imports collapse to one module, plain file imports still produce two. I’m running the actual pytest node for the importlib-path tests now to catch any mismatch with the real test harness.
- Implemented in [src/_pytest/pathlib.py:524](./src/_pytest/pathlib.py:524) and [testing/test_pathlib.py:326](./testing/test_pathlib.py:326).  `importlib` mode now prefers a real package or namespace-package import name when the target file is already importable, instead of always inventing a synthetic root-relative name. That keeps package modules like `pmxbot.logging` from being loaded twice under different names, while still preserving the existing behavior that plain files imported twice get two distinct module objects.  Verification: - `python -m py_compile src/_pytest/pathlib.py testing/test_pathlib.py` - Direct temp-package checks confirmed:   - importable package modules resolve as `pkg.mod` and reuse the same object   - non-importable files still produce distinct module objects on repeated import  I couldn’t run the pytest node itself because this environment is missing test dependencies (`iniconfig`).

## 4. Patch and cost delta

- Clean mean tokens: 1,761,253; mutant tokens: 1,470,633; delta: -16.50%.
- Clean mean rounds: 27.67; mutant rounds: 29; delta: +4.82%.
- Final mutant patch files: `src/_pytest/pathlib.py`, `testing/test_pathlib.py`.
- Files added beyond every clean patch: none.
- Clean-patch files omitted by mutant: none.
- Trace patch paths: src/_pytest/pathlib.py, testing/test_pathlib.py.

## 5. Inconsistency awareness and causal mechanism

No explicit statement says that the mutated documentation conflicts with the implementation or tests. The Agent may have observed contradictory behavior, but it did not name and reject the documentation inconsistency.

The mutant retained the clean file footprint, so the failure is not a gross localization error. The divergence lies in edit semantics or incomplete validation: the Agent reached the same region but did not reproduce a clean-passing behavior.

- Earliest evidence classification: **Localization**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
