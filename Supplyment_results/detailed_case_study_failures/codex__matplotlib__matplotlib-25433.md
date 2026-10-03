# Codex: matplotlib__matplotlib-25433

**Causal status:** `mutation-related`. Official evaluation is unresolved. Mutation text hit 6/8 locations.

## 1. Problem and expected correct approach

[Bug]: using clf and pyplot.draw in range slider on_changed callback blocks input to widgets
### Bug summary

When using clear figure, adding new widgets and then redrawing the current figure in the on_changed callback of a range slider the inputs to all the widgets in the figure are blocked. When doing the same in the button callback on_clicked, everything works fine.

### Code for reproduction

```python
import matplotlib.pyplot as pyplot
import matplotlib.widgets as widgets

def onchanged(values):
    print("on changed")
    print(values)
    pyplot.clf()
    addElements()
    pyplot.draw()

def onclick(e):
    print("on click")
    pyplot.clf()
    addElements()
    pyplot.draw()

def addElements():
    ax = pyplot.axes([0.1, 0.45, 0.8, 0.1])
    global slider
    slider = widgets.RangeSlider(ax, "Test", valmin=1, valmax=10, valinit=(1, 10))
    slider.on_changed(onchanged)
    ax = pyplot.axes([0.1, 0.30, 0.8, 0.1])
    global button
    button = widgets.Button(ax, "Test")
    button.on_clicked(onclick)

addElements()

pyplot.show()
```


### Actual outcome

The widgets can't receive any input from a mouse click, when redrawing in the on_changed callback of a range Slider. 
When using a button, there is no problem.

### Expected outcome

The range slider callback on_changed behaves the same as the button callback on_clicked.

### Additional information

The problem also occurred on Manjaro with:
- Python version: 3.10.9
- Matplotlib version: 3.6.2
- Matplotlib backend: QtAgg
- Installation of matplotlib via Linux package manager


### Operating system

Windows 10

### Matplotlib Version

3.6.2

### Matplotlib Backend

TkAgg

### Python version

3.11.0

### Jupyter version

_No response_

### Installation

pip

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `lib/matplotlib/figure.py`, `lib/matplotlib/tests/test_figure.py`
- Clean run 2: `lib/matplotlib/figure.py`, `lib/matplotlib/tests/test_widgets.py`
- Clean run 3: `lib/matplotlib/figure.py`, `lib/matplotlib/tests/test_figure.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `lib/matplotlib/figure.py` / `lib/matplotlib/figure.py::FigureBase.clear`
  - Clean doc: Parameters
  - Mutated doc: Keyword-only Parameters
  - Contract change: The documentation now presents the parameters as keyword-only, changing how the interface is described as invoked.
- `lib/matplotlib/figure.py` / `lib/matplotlib/figure.py::FigureBase.clear`
  - Clean doc: ----------
  - Mutated doc: keep_observers : bool, default: True
  - Contract change: The documented default for `keep_observers` changes from False to True.
- `lib/matplotlib/figure.py` / `lib/matplotlib/figure.py::FigureBase.delaxes`
  - Clean doc: Remove the `~.axes.Axes` *ax* from the figure; update the current Axes.
  - Mutated doc: Remove the `~.axes.Axes` *ax* from the figure; leave the current Axes unchanged.
  - Contract change: Current-Axes state is documented as remaining unchanged when an Axes is removed.
- `lib/matplotlib/figure.py` / `lib/matplotlib/figure.py::FigureBase.clear`
  - Clean doc: Clear the figure.
  - Mutated doc: Leave the figure contents unchanged.
  - Contract change: Figure clearing is documented as preserving its existing contents.
- `lib/matplotlib/figure.py` / `lib/matplotlib/figure.py::FigureBase.clear`
  - Clean doc: keep_observers : bool, default: False
            Set *keep_observers* to True if, for example,
            a gui widget is tracking the Axes in the figure.
  - Mutated doc: keep_observers : bool, default: False
            Set *keep_observers* to True to clear observers, for example,
            when a gui widget is tracking the Axes in the figure.
  - Contract change: Setting keep_observers to True is documented as clearing Axes observers.
- `lib/matplotlib/figure.py` / `lib/matplotlib/figure.py::FigureBase.colorbar`
  - Clean doc: Notes
  - Mutated doc: Parameters
  - Contract change: The documentation changes the section heading from `Notes` to `Parameters`, implying that the following content documents invocation parameters.
- `lib/matplotlib/figure.py` / `lib/matplotlib/figure.py::FigureBase.colorbar`
  - Clean doc: -----
  - Mutated doc: -------
  - Contract change: The documentation changes the Notes heading marker from five hyphens to seven hyphens.
- `lib/matplotlib/figure.py` / `lib/matplotlib/figure.py::FigureBase.colorbar`
  - Clean doc: If *mappable* is a `~.contour.ContourSet`, its *extend* kwarg is
        included automatically.
  - Mutated doc: If *mappable* is a `~.contour.ContourSet`, its *extension* kwarg is
        included automatically.
  - Contract change: The documented ContourSet keyword argument changes from `extend` to `extension`.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m checking the slider and widget event handling path first, then I’ll make the smallest fix that preserves the button behavior and run focused tests around widget callbacks.
- `rg` is unavailable here, so I’m switching to `find` and `grep` to locate the widget code and the existing tests that cover redraw or callback behavior.
- I found the widget implementation and the widget tests. Next I’m reading the `Slider`/`RangeSlider` event flow and the existing tests around callback redraws so I can patch the exact state transition causing the blocked input.
- I’ve narrowed it to the RangeSlider’s drag grab state: the callback runs while the mouse is still grabbed, unlike `Button.on_clicked`. I’m checking whether upstream already has a minimal state-handling fix so I can mirror the intended behavior instead of inventing a new interaction model.
- The bug may be broader than the slider itself: `clf()` is being called while a widget has an active mouse grab, and the clear path may not release it. I’m checking the figure clear logic now, because that would fix this class of stale-grab failures for any widget callback that rebuilds the figure.
- `Figure.clear()` does not currently release a canvas mouse grab before deleting axes. That matches the symptom: a RangeSlider can grab the mouse, its callback clears the figure, and the stale grab survives onto the rebuilt widgets. I’m confirming there isn’t already compensating logic elsewhere, then I’ll patch `clear()` and add a regression test for the slider callback case.
- I’m making the fix in `FigureBase.clear()`, not in the slider, because the stale state is the mouse grab owned by the canvas. I’m also adding a regression test that clears a grabbed figure and asserts the grab is dropped.
- The code change is in place. I’m running the narrow figure-clear test first, because it exercises the exact stale-grab behavior without needing a full interactive backend session.
- `Figure.clear()` now passes its direct regression test. I’m doing one more targeted check with a real `RangeSlider` drag event so we verify the exact callback path that previously left the canvas grabbed.
- The first raw event simulation landed outside the slider data bounds, so I’m retrying with coordinates squarely inside the axis. That should exercise the same callback path cleanly.
- `MouseEvent` is overkill for this path, and the data transform is making the harness noisy. I’m switching to the widget test helper that feeds `_update()` directly, which still exercises the exact grab/release state machine and the callback.
- The figure-level regression is enough to lock in the fix, and it avoids depending on the `RangeSlider` motion path in this checkout. I’m doing a quick diff review now to make sure the change stayed minimal and didn’t disturb unrelated widget logic.
- I’m grabbing exact line numbers for the final handoff so you can jump straight to the changed code and the regression test.
- Implemented the fix in `FigureBase.clear()` so it releases any active canvas mouse grab before removing axes. That prevents a stale grab from surviving a `clf()`/`clear()` call made inside a widget callback, which is what was blocking input after a `RangeSlider.on_changed` redraw.  Changes: - [`/testbed/lib/matplotlib/figure.py:956`](file:///testbed/lib/matplotlib/figure.py#L956) releases `self.canvas.mouse_grabber` at the start of `clear()` - [`/testbed/lib/matplotlib/tests/test_figure.py:759`](file:///testbed/lib/matplotlib/tests/test_figure.py#L759) adds a regression assertion that clearing a grabbed figure leaves `mouse_grabber` as `None`  Validation: - `python -m pytest lib/matplotlib/tests/test_figure.py -k figure_clear` passed  

### Clean run 2
- I’m checking the widget and figure lifecycle code first, then I’ll reproduce the behavior with focused tests and patch the smallest place that preserves widget interactivity after `clf()` plus redraw.
- `rg` isn’t installed here, so I’m switching to `find`/`grep` to locate the slider and figure-clearing code paths, then I’ll narrow it down to the event handling interaction that differs between `Button` and `RangeSlider`.
- I’ve located the widget code. Next I’m reading the `RangeSlider` event path and the figure-clearing logic to see whether `clf()` is leaving stale widget state around or whether redraw is happening before the new widgets are fully registered.
- The likely failure mode is a stale mouse grab: `RangeSlider` fires callbacks while the canvas is still grabbed for dragging, and `clf()` may replace the figure contents without releasing that grab. I’m checking where the canvas releases `mouse_grabber` today and whether `Figure.clear()` needs to do that defensively.
- `Figure.clear()` isn’t where I expected, so I’m locating the actual figure teardown path now. If the grab is owned by an Axes that gets removed during `clf()`, the fix probably belongs in the figure clearing routine rather than in the widget itself.
- I’ve confirmed `Figure.clear()` removes Axes but does not touch `canvas.mouse_grabber`. That fits the failure: a dragged `RangeSlider` can clear its own Axes while still owning the grab, and the new widgets then see the canvas as permanently grabbed. I’m checking existing widget tests so I can add a focused regression test at the right level.
- I’ve got enough to patch the lifecycle now. I’m validating one more thing: whether the canvas routes subsequent events exclusively to `mouse_grabber`, because that would make releasing the grab during `clear()` the correct fix and keep the change very small.
- I’m making the fix in the figure-clear path and adding a regression test that exercises the exact failure mode: a slider callback clears the figure while the slider still owns the mouse grab. That keeps the patch small and directly tied to the broken state transition.
- The code change is in. I’m adding a regression test that recreates a button inside the slider callback, redraws, and then verifies the fresh button can still receive a click after the slider drag.
- I’ve added the regression. Next step is a focused pytest run on the new test and the existing range-slider coverage so we can confirm the fix without paying for the whole test suite.
- Both pytest runs are in flight. I’m waiting on the targeted widget and figure-clear checks; if anything fails, I’ll tighten the fix rather than broadening it.
- The regression test tripped on backend event coordinate conversion, not on the fix itself. I’m switching it to Matplotlib’s test mock-event helper so it exercises the same widget logic without depending on a fully realized GUI event object.
- The test now uses the widget test helper directly. I’m rerunning the same focused slice to make sure the regression passes and the clear-path test still holds.
- `RangeSlider._update()` on a synthetic press event is hitting an unrelated tuple arithmetic path, so I’m moving the test to the exact state the bug needs: slider already dragged and mouse already grabbed. That still validates the broken lifecycle without depending on an untested press path.
- I’ve removed the noisy press-path dependency from the regression. Rerunning the same focused checks now.
- I’m simplifying the regression further: the bug only needs “callback runs while grab is held,” not the slider’s motion math. `set_val()` already exercises that callback path and avoids an unrelated `_update()` edge case in the test harness.
- The regression is now on the minimal state transition: grabbed slider, `set_val()`, callback clears and redraws, then a fresh button must still accept clicks. I’m rerunning the focused tests once more.
- The targeted checks are green. I’m doing a quick diff review now to make sure the fix stayed narrow and there aren’t any accidental edits before I hand back the result.
- I’ve confirmed the working tree only contains the intended two file edits. I’m grabbing exact line numbers now so I can point you to the fix and the regression test cleanly.
- Implemented the fix and a regression test.  What changed: - In [`/testbed/lib/matplotlib/figure.py:956`](file:///testbed/lib/matplotlib/figure.py#L956), `Figure.clear()` now releases the canvas mouse grab if the grabbed `Axes` belongs to the figure being cleared. - In [`/testbed/lib/matplotlib/tests/test_widgets.py:1336`](file:///testbed/lib/matplotlib/tests/test_widgets.py#L1336), I added a regression test that:   - simulates a grabbed `RangeSlider`,   - clears the figure inside its `on_changed` callback,   - recreates a `Button`,   - verifies the new button still receives clicks.  Why this fixes it: - `RangeSlider.on_changed` can run while the slider still owns `canvas.mouse_grabber`. - Before this change, `clf()` removed the old axes but left the grab in place, so later widget events were routed incorrectly. - Releasing the grab during clear restores normal event routing for newly created widgets.  Focused tests run: - `python -m pytest /testbed/lib/matplotlib/tests/test_widgets.py -k 'range_slider and not image'` - `python -m pytest /testbed/lib/matplotlib/tests/test_figure.py -k 'clear or clf'`  Both passed.

### Clean run 3
- I’m inspecting the widget event path and the existing tests first so I can make the smallest fix in the right layer, then I’ll run the focused widget tests that cover redraw and callback behavior.
- `rg` isn’t available here, so I’m switching to basic file discovery and grep to locate the widget implementation and any regression tests around slider callbacks.
- I found the widget implementation and the existing `test_widgets.py` coverage. Next I’m reading the RangeSlider and Button callback code side by side to isolate the behavior difference, then I’ll add a regression test in the same area.
- The likely difference is that `RangeSlider` fires `changed` during drag, while `Button` fires `clicked` after mouse release. I’m reading the drag lifecycle now to see whether the widget keeps mouse grab state alive across a callback that clears the figure.
- I’ve confirmed the key state leak: `RangeSlider` is still holding the canvas mouse grab when its callback clears and rebuilds the figure. I’m checking whether `Figure.clear()` already cleans that up, and if not I’ll patch it there so the fix applies broadly to any widget callback that clears the figure mid-drag.
- `Figure.clear()` itself doesn’t touch `canvas.mouse_grabber`, so a dragged slider can leave the canvas stuck on a now-deleted `Axes`. I’m checking the removal path so I can release that grab exactly when the owning axes is deleted, without changing unrelated widget behavior.
- I’m patching `Figure.delaxes()` to drop an active mouse grab when the grabbed axes is removed, then I’ll add a regression test that clears a figure while an axes owns the grab and checks the canvas is no longer stuck.
- The code change is in place. I’m running the narrow figure tests that cover `clear()`/`clf()` and the new mouse-grabber regression before deciding whether the widget-specific test needs anything more.
- The test jobs are still running. I’m polling both so I can catch any backend-specific failures rather than assuming the first pass is clean.
- The focused tests passed. I’m doing one quick diff check now to confirm the patch stayed minimal and only touched the grab-release path plus the regression test.
- I’ve verified the diff and the regression is covered. I’m grabbing exact line numbers so the final summary points you straight to the change and the new test.
- Fixed the stuck-input bug by releasing the canvas mouse grab when an `Axes` is removed from a figure.  What changed: - In [`lib/matplotlib/figure.py:930`](file:///testbed/lib/matplotlib/figure.py#L930), `Figure.delaxes()` now calls `canvas.release_mouse(ax)` if that axes currently owns the mouse grab. - Added a regression test in [`lib/matplotlib/tests/test_figure.py:163`](file:///testbed/lib/matplotlib/tests/test_figure.py#L163) that grabs the mouse, clears the figure, and asserts the grab is cleared.  Why this fixes it: - `RangeSlider.on_changed` fires while the mouse is still grabbed during a drag. - If the callback clears the figure, the old slider axes used to disappear while still holding the grab, which blocked later widget input. - Releasing the grab when the axes is deleted prevents the stale grab state.  Validation: - `python -m pytest lib/matplotlib/tests/test_figure.py -k "clf_keyword or clear_releases_mouse_grabber"` - `python -m pytest lib/matplotlib/tests/test_widgets.py -k "range_slider or slider"`  Both passed.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 6/8. Hit lines: [28], [28], [28], [28], [15, 19, 24, 28, 54, 66, 73], [15, 19, 24, 28, 54, 66, 73].
- Relative to the three clean runs, the mutant trajectory **contracted** in interaction length (15.33 clean-mean rounds to 13). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 14, 20, 12 extracted reasoning messages across runs 1--3; the mutant emitted 13. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.
- I’m checking the widget callback path and the related tests first so I can make the smallest fix that preserves existing button behavior and only changes the slider case where needed.
- `rg` isn’t available here, so I’m falling back to `find` and `grep` to locate the widget implementation and the existing tests around slider/button redraw behavior.
- I found the widget code; next I’m reading the slider/button event handling and existing widget tests to see where the figure-clearing path diverges.
- I’ve narrowed the suspicion to mouse grabbing: the range slider fires callbacks while the drag is still active, so clearing/rebuilding the figure may leave the old slider holding the canvas grab. I’m confirming that against the event dispatch code before patching.
- The event model confirms the failure: `RangeSlider._update` invokes `set_val` during a motion event while its axes owns `canvas.mouse_grabber`; the callback deletes that axes, leaving a grabber that no longer belongs to the figure. The targeted fix is to release the grab before notifying `changed` callbacks, while retaining normal drag behavior when callbacks do not rebuild the figure.
- The fix needs to preserve dragging for ordinary callbacks while cleaning up the grab when a callback removes the slider’s axes. I’ll wrap slider value notification in `_update`: release the grab before user callbacks, then either re-grab if the widget still belongs to the figure or mark the old slider inactive if it was cleared; I’ll cover both `Slider` and `RangeSlider` through the shared base helper and add a regression test.
- The first edit exposed one necessary plumbing detail: `RangeSlider._update_val_from_pos` currently receives only the position, so the event must be passed through to the shared notification helper. I’m correcting that signature and then adding a focused regression test that verifies a rebuilt button receives the next click.
- The implementation now releases the grab around callback execution and restores it only when the original slider axes still exists, which handles both continued drags and figure teardown. I’m tightening the regression test to click the button created by the callback itself, then running the widget test module’s focused cases.
- The focused pytest run is blocked by missing compiled Matplotlib extensions in this checkout, but Python compilation succeeds. I also noticed the test helper emits a synthetic event name, so I’m making the regression test explicitly use press/motion event names to ensure it exercises the actual grab-and-callback path.
- The repo has a broken alternate-object configuration, so `git` is noisy, but the code edits themselves are in place. I’m doing one last pass over the changed logic and then I’ll summarize the fix and the test coverage caveat.
- I’m making one small robustness tweak: if a slider callback throws, the mouse grab should still be left in a sane state instead of depending on normal return. After that I’ll stop; the code path is already minimal and the focused test is in place.
- The regression test should exercise the problematic redraw path, not just the figure clear. I’m adding an explicit canvas draw inside the callback so the test matches the reported failure mode more closely.
- Implemented the fix in [`lib/matplotlib/widgets.py`](/testbed/lib/matplotlib/widgets.py#L333) and added a regression test in [`lib/matplotlib/tests/test_widgets.py`](/testbed/lib/matplotlib/tests/test_widgets.py#L1337).  What changed: - `SliderBase` now has a small `_set_val(..., event)` helper that temporarily releases the canvas mouse grab before firing callbacks, then restores it only if the original axes still exist. - `Slider._update` and `RangeSlider._update_val_from_pos` use that helper, so `on_changed` callbacks can safely clear and rebuild the figure without leaving a stale mouse grab behind. - Added a regression test that clears the figure from a `RangeSlider.on_changed` callback, redraws, creates a new `Button`, and verifies the button still receives clicks.  Verification: - `python -m compileall -q lib/matplotlib/widgets.py lib/matplotlib/tests/test_widgets.py` passed. - A focused `pytest` run was blocked by this checkout’s missing compiled Matplotlib extension import (`_c_internal_utils`), so I couldn’t execute the test module end-to-end here.  If you want, I can also add a second regression test for `Slider` to cover the single-value slider path explicitly.

## 4. Patch and cost delta

- Clean mean tokens: 1,374,097; mutant tokens: 825,720; delta: -39.91%.
- Clean mean rounds: 15.33; mutant rounds: 13; delta: -15.22%.
- Final mutant patch files: `lib/matplotlib/figure.py`, `lib/matplotlib/tests/test_widgets.py`, `lib/matplotlib/widgets.py`.
- Files added beyond every clean patch: `lib/matplotlib/widgets.py`.
- Clean-patch files omitted by mutant: `lib/matplotlib/tests/test_figure.py`.
- Trace patch paths: lib/matplotlib/figure.py, lib/matplotlib/tests/test_widgets.py, lib/matplotlib/widgets.py.

## 5. Inconsistency awareness and causal mechanism

No explicit statement says that the mutated documentation conflicts with the implementation or tests. The Agent may have observed contradictory behavior, but it did not name and reject the documentation inconsistency.

The mutation was observed before a patch that changed the clean localization/edit footprint. The extra and omitted files above identify the concrete structural divergence; subsequent testing did not restore the clean solution. This is positive evidence of mutation influence, although a single run cannot establish deterministic causality.

- Earliest evidence classification: **Editing**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
