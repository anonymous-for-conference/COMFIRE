# OpenCode: matplotlib__matplotlib-25442

**Causal status:** `mutation-related`. Official evaluation is unresolved. Mutation text hit 7/9 locations.

## 1. Problem and expected correct approach

[Bug]: Attribute Error combining matplotlib 3.7.1 and mplcursor on data selection
### Bug summary

If you combine mplcursor and matplotlib 3.7.1, you'll get an `AttributeError: 'NoneType' object has no attribute 'canvas'` after clicking a few data points. Henceforth, selecting a new data point will trigger the same traceback. Otherwise, it works fine. 

### Code for reproduction

```python
import numpy as np
import matplotlib.pyplot as plt
import mplcursors as mpl

x = np.arange(1, 11)    
y1 = x

plt.scatter(x,y1)

mpl.cursor()
plt.show()
```


### Actual outcome

```
Traceback (most recent call last):
  File "C:\Users\MrAni\Python\miniconda3\lib\site-packages\matplotlib\cbook\__init__.py", line 304, in process
    func(*args, **kwargs)
  File "C:\Users\MrAni\Python\miniconda3\lib\site-packages\matplotlib\offsetbox.py", line 1550, in on_release
    if self._check_still_parented() and self.got_artist:
  File "C:\Users\MrAni\Python\miniconda3\lib\site-packages\matplotlib\offsetbox.py", line 1560, in _check_still_parented
    self.disconnect()
  File "C:\Users\MrAni\Python\miniconda3\lib\site-packages\matplotlib\offsetbox.py", line 1568, in disconnect
    self.canvas.mpl_disconnect(cid)
  File "C:\Users\MrAni\Python\miniconda3\lib\site-packages\matplotlib\offsetbox.py", line 1517, in <lambda>
    canvas = property(lambda self: self.ref_artist.figure.canvas)
AttributeError: 'NoneType' object has no attribute 'canvas'
```

### Expected outcome

No terminal output

### Additional information

Using matplotlib 3.7.0 or lower works fine. Using a conda install or pip install doesn't affect the output. 

### Operating system

Windows 11 and Windwos 10 

### Matplotlib Version

3.7.1

### Matplotlib Backend

QtAgg

### Python version

3.9.16

### Jupyter version

_No response_

### Installation

conda

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `lib/matplotlib/offsetbox.py`, `lib/matplotlib/tests/test_offsetbox.py`
- Clean run 2: `lib/matplotlib/offsetbox.py`, `lib/matplotlib/tests/test_offsetbox.py`
- Clean run 3: `lib/matplotlib/offsetbox.py`, `lib/matplotlib/tests/test_offsetbox.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `lib/matplotlib/offsetbox.py` / `lib/matplotlib/offsetbox.py::DraggableBase.disconnect`
  - Clean doc: Disconnect the callbacks.
  - Mutated doc: Leaves the callbacks connected.
  - Contract change: The method is documented as leaving the callbacks connected instead of disconnecting them.
- `lib/matplotlib/artist.py` / `lib/matplotlib/artist.py::Artist.remove`
  - Clean doc: Note: `~.axes.Axes.relim` will not see collections even if the
        collection was added to the axes with *autolim* = True.
  - Mutated doc: Note: `~.axes.Axes.relim` will not see collections even if the
        collection was added to the axes with *autolim_mode* = True.
  - Contract change: The documented parameter name changes from `autolim` to `autolim_mode`.
- `lib/matplotlib/artist.py` / `lib/matplotlib/artist.py::Artist.remove`
  - Clean doc: Note: there is no support for removing the artist's legend entry.
  - Mutated doc: Note: there is support for removing the artist's legend entry.
  - Contract change: The documentation now states that removing an artist also removes its legend entry, reversing the documented legend-removal support.
- `lib/matplotlib/offsetbox.py` / `lib/matplotlib/offsetbox.py::DrawingArea.add_artist`
  - Clean doc: Add an `.Artist` to the container box.
  - Mutated doc: Add a `.Figure` to the container box.
  - Contract change: The documented item type changes from `.Artist` to `.Figure`.
- `lib/matplotlib/offsetbox.py` / `lib/matplotlib/offsetbox.py::OffsetBox.set_figure`
  - Clean doc: Set the `.Figure` for the `.OffsetBox` and all its children.
  - Mutated doc: Set the `.Figure` for the `.Artist` and all its children.
  - Contract change: The documented target changes from the `.OffsetBox` to the `.Artist`.
- `lib/matplotlib/offsetbox.py` / `lib/matplotlib/offsetbox.py::OffsetBox.set_figure`
  - Clean doc: Parameters
  - Mutated doc: Parameters (optional)
  - Contract change: The documentation changes the `fig` parameter from required to optional.
- `lib/matplotlib/offsetbox.py` / `lib/matplotlib/offsetbox.py::OffsetBox.set_figure`
  - Clean doc: ----------
  - Mutated doc: ----------
        fig : `~matplotlib.figure.Figure`, optional
  - Contract change: The documentation now describes fig as optional rather than required.
- `lib/matplotlib/offsetbox.py` / `lib/matplotlib/offsetbox.py::OffsetBox.set_figure`
  - Clean doc: fig : `~matplotlib.figure.Figure`
  - Mutated doc: figure : `~matplotlib.figure.Figure`
  - Contract change: The documented parameter name changes from `fig` to `figure`.
- `lib/matplotlib/text.py` / `lib/matplotlib/text.py::_AnnotationBase._check_xy`
  - Clean doc: Check whether the annotation at *xy_pixel* should be drawn.
  - Mutated doc: Check whether the annotation at *xy_pixel* should not be drawn.
  - Contract change: The documented draw predicate is inverted: it now says the annotation should not be drawn.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m checking the package layout and the cursor/annotation code path first, then I’ll reproduce with focused tests and patch the smallest surface that matches the regression.
- I’ve confirmed this tree is Matplotlib itself, so the fix is likely in Matplotlib’s callback cleanup behavior rather than in an external dependency. Next I’m locating the exact parent-removal path and the regression test surface.
- The failure mode is already visible in `DraggableBase`: once the reference artist is detached, `disconnect()` still recomputes `self.canvas` through `ref_artist.figure.canvas`. I’m checking whether Matplotlib already has a stored canvas elsewhere so the fix can stay minimal and not change drag behavior.
- I’ve narrowed it to a one-line behavioral gap: the helper throws away the only stable canvas handle once the artist is removed. I’m checking whether the tree already has a precedent for storing the canvas on draggable helpers so the patch matches local style instead of inventing a new one.
- I’ve got the fix shape now: cache the canvas at helper construction, then exercise the release path after detaching the annotation so the regression is covered where it breaks. I’m patching that plus a focused unit test in `test_offsetbox.py`.
- The code change is in. I’m running the new regression test first, then I’ll broaden to the nearby offsetbox tests only if that stays green.
- `pytest` isn’t installed in this environment, so I’m switching to a direct reproduction script against the local `lib/` tree. That still exercises the exact callback path we changed, which is the important part here.
- The environment is missing `numpy` and `pytest`, so I can’t run the normal test suite as-is. I’m trying the lightest dependency install next; if that doesn’t land cleanly, I’ll fall back to syntax checks and the code-path review.
- `numpy` and `pytest` are in place. The next missing dependency is `PIL`, so I’m adding `pillow` and rerunning the same two focused tests rather than broadening the scope.
- `numpy` 2.x is incompatible with the compiled Matplotlib extension in this tree. I’m downgrading to a 1.x wheel so the local build can import cleanly and the focused tests can actually execute.
- The import chain is now down to a missing pure-Python dependency. I’m adding the next one (`cycler`) and retrying, which should get us much closer to an actual test run.
- Collection is now blocked by a deprecation warning promoted to an error, not by the patch itself. I’m rerunning with warnings suppressed so the test body can actually execute.
- Pytest is promoting that pyparsing deprecation to an error during collection. I’m overriding warnings at the interpreter level now, which should take precedence over the repo’s stricter warning filter.
- Pytest’s warning policy is blocking collection before the test body runs, so I’m validating the exact regression with a direct script instead. It sets the warning filter before importing Matplotlib, then exercises the remove-plus-release path we changed.
- The regression script passed, and the edited files compile. I’m checking the final diff now for scope and style before I hand it back.
- I’m tightening one comment in the draggable helper so it describes the actual invariant we’re relying on: the artist can be detached before release, but the original canvas still has to receive the disconnect.
- Fixed in [offsetbox.py](/testbed/lib/matplotlib/offsetbox.py:1497): `DraggableBase` now caches the original canvas at construction time, so `disconnect()` still works after the reference artist has been removed and `figure` becomes `None`. I also added a regression test in [test_offsetbox.py](/testbed/lib/matplotlib/tests/test_offsetbox.py:243) that exercises the pick/remove/release path.  Verification: `python -m py_compile lib/matplotlib/offsetbox.py lib/matplotlib/tests/test_offsetbox.py` and a direct repro script against `PYTHONPATH=/testbed/lib` both passed.

### Clean run 2
- I’m checking the affected code paths and tests first so I can make the smallest fix that matches the existing behavior.
- I’ve narrowed it to `offsetbox.py`; next I’m reading the parenting/disconnect logic and looking for an existing test pattern that covers artist removal or stale references.
- The crash is in the disconnect path, and the key question is whether to cache the canvas or derive it from the release event. I’m checking how this class is expected to behave under pickling before touching the API shape.
- I’ve got the likely fix shape: cache the live canvas for disconnect, but keep it out of pickles so figure serialization doesn’t regress. I’m adding a focused regression test that removes the artist mid-drag and then exercises `on_release`, which is the crashing path.
- I’ve got the code change scoped: one private canvas cache plus a pickle-safe state hook, and one regression test that forces the release-after-removal path. I’m editing those now.
- The implementation is in place. I’m verifying the exact draggable API for annotations before I run the focused test, because the regression test needs to match the repo’s public entry point rather than relying on internals.
- `pytest` isn’t installed in the base interpreter here, so I can’t use the normal test runner. I’m checking whether the repo provides an alternate entry point; if not, I’ll at least validate the changed code paths with a small import-time smoke check.
- The environment is missing the test stack, so I can’t execute the pytest case end to end here. I am still doing a compile check on the edited files to catch syntax errors and obvious regressions.
- Fixed in [`lib/matplotlib/offsetbox.py`](/testbed/lib/matplotlib/offsetbox.py:1497): `DraggableBase` now caches the canvas at construction, uses that cached canvas when the artist has already been detached, and keeps the cache out of pickles so figure serialization stays intact.  Added a regression test in [`lib/matplotlib/tests/test_offsetbox.py`](/testbed/lib/matplotlib/tests/test_offsetbox.py:325) that removes an annotation after a drag pick and then releases it, which exercises the crash path.  I couldn’t run `pytest` here because the environment is missing the test stack (`pytest`, `numpy`, `matplotlib` imports fail), but I did run `python -m py_compile` on the edited files to verify syntax.

### Clean run 3
- I’m checking the relevant cursor/annotation code paths first, then I’ll reproduce the failing state in the test suite and patch the narrowest spot that changed in matplotlib 3.7.1.
- I’ve confirmed this is in the vendored matplotlib tree, not a separate `mplcursors` checkout. Next I’m tracing the `offsetbox` disconnect path and the tests around annotation removal to see where 3.7.1 started leaving a dead reference behind.
- I found the failure point: `DraggableBase.disconnect()` still dereferences `self.ref_artist.figure.canvas` after `_check_still_parented()` has already determined the figure is gone. I’m checking whether this should be handled by storing the canvas up front or by making disconnect a no-op once the artist is detached.
- I have enough context to patch now. I’m making two small changes: guard `DraggableBase.disconnect()` when the reference artist has already been detached, and add a regression test that removes the annotation before release so the old traceback is exercised.
- The code change is in place. I’m running the narrow offsetbox tests first to verify the regression and make sure the new guard doesn’t disturb the existing picking behavior.
- `pytest` isn’t importable in the current Python environment, so I’m checking whether the repo has a separate test runner available before I fall back to a lighter verification path.
- The test environment is missing the runtime dependencies (`pytest` and even `numpy` for import-based test execution), so I can’t execute the Matplotlib test file here. I’m at least syntax-checking the touched modules and then I’ll summarize the exact regression covered.
- Fixed in `lib/matplotlib/offsetbox.py:1559` by making `DraggableBase.disconnect()` return early once the reference artist has already been detached from its figure. That prevents the `self.ref_artist.figure.canvas` dereference that was raising on release after a selection was removed.  I also added a regression test in `lib/matplotlib/tests/test_offsetbox.py:242` that removes an annotation before calling `on_release()`, which exercises the broken path.  Verification was limited here: `py_compile` passed for both touched files, but I could not run the Matplotlib pytest file because this environment is missing `pytest` and `numpy`.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 7/9. Hit lines: [18, 22, 56, 78, 83], [40, 43], [40, 43], [78], [78], [78], [78].
- Relative to the three clean runs, the mutant trajectory **contracted** in interaction length (22.00 clean-mean rounds to 19). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 17, 9, 8 extracted reasoning messages across runs 1--3; the mutant emitted 11. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.
- I’m checking the package layout and the selection code path first so the fix stays minimal and lands in the right place.
- I’ve confirmed this is in the Matplotlib tree, not a standalone `mplcursors` package in the repo. Next I’m narrowing the regression to the offsetbox disconnect path and the tests that already cover annotation lifecycle.
- The failure is exactly where the traceback points: `disconnect()` recomputes `self.canvas` from `ref_artist.figure`, so once the artist has been detached it dereferences `None`. I’m checking whether the object already has enough state to disconnect safely, then I’ll add a regression test around that detach path.
- I’m checking whether the artist still retains any usable link to the original canvas after removal. If it does, I can avoid adding new stored state; if not, I’ll take the smallest stateful change that keeps the callbacks disconnectable.
- I’ve got the fix scoped: preserve the original canvas on the draggable helper, then add a regression that removes the annotation between pick and release. That keeps the disconnect path working without changing the public API.
- I’m adding a narrow regression that exercises the exact failure mode: drag starts, the annotation is removed, and mouse release must not blow up while cleaning up the stale callbacks.
- The environment doesn’t have `pytest`, so I’m verifying the regression with a direct Matplotlib script instead. That still exercises the exact event path we changed.
- The source tree isn’t on `sys.path` by default here, so I’m rerunning the smoke test with `PYTHONPATH=/testbed/lib` against the checkout itself.
- I can’t execute the runtime path in this container because the Matplotlib test deps aren’t installed, so I’m at least syntax-checking the edited files before I stop.
- I’ve finished the code change and the regression test. I’m grabbing the final line references now so I can summarize precisely what changed and what I could verify in this container.
- Fixed in `lib/matplotlib/offsetbox.py:1498` by caching the original canvas on `DraggableBase` and using that cached canvas when disconnecting after the artist has already been removed. That prevents `_check_still_parented()` from falling into `self.ref_artist.figure.canvas` after `figure` becomes `None`.  I also added a regression test in `lib/matplotlib/tests/test_offsetbox.py:412` that starts a drag, removes the annotation, and then sends mouse release; it should complete without raising.  Verification was limited by the container: `pytest`/runtime deps like `numpy` aren’t installed here, so I only смог run `python -m py_compile` on the edited files.

## 4. Patch and cost delta

- Clean mean tokens: 1,226,735; mutant tokens: 632,163; delta: -48.47%.
- Clean mean rounds: 22.00; mutant rounds: 19; delta: -13.64%.
- Final mutant patch files: `lib/matplotlib/artist.py`, `lib/matplotlib/offsetbox.py`, `lib/matplotlib/tests/test_offsetbox.py`, `lib/matplotlib/text.py`.
- Files added beyond every clean patch: `lib/matplotlib/artist.py`, `lib/matplotlib/text.py`.
- Clean-patch files omitted by mutant: none.
- Trace patch paths: lib/matplotlib/artist.py, lib/matplotlib/offsetbox.py, lib/matplotlib/tests/test_offsetbox.py, lib/matplotlib/text.py.

## 5. Inconsistency awareness and causal mechanism

No explicit statement says that the mutated documentation conflicts with the implementation or tests. The Agent may have observed contradictory behavior, but it did not name and reject the documentation inconsistency.

The mutation was observed before a patch that changed the clean localization/edit footprint. The extra and omitted files above identify the concrete structural divergence; subsequent testing did not restore the clean solution. This is positive evidence of mutation influence, although a single run cannot establish deterministic causality.

- Earliest evidence classification: **Editing**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
