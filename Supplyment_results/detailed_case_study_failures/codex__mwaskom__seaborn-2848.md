# Codex: mwaskom__seaborn-2848

**Causal status:** `mutation-related`. Official evaluation is unresolved. Mutation text hit 22/35 locations.

## 1. Problem and expected correct approach

pairplot fails with hue_order not containing all hue values in seaborn 0.11.1
In seaborn < 0.11, one could plot only a subset of the values in the hue column, by passing a hue_order list containing only the desired values. Points with hue values not in the list were simply not plotted.
```python
iris = sns.load_dataset("iris")`
# The hue column contains three different species; here we want to plot two
sns.pairplot(iris, hue="species", hue_order=["setosa", "versicolor"])
```

This no longer works in 0.11.1. Passing a hue_order list that does not contain some of the values in the hue column raises a long, ugly error traceback. The first exception arises in seaborn/_core.py:
```
TypeError: ufunc 'isnan' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
```
seaborn version: 0.11.1
matplotlib version: 3.3.2
matplotlib backends: MacOSX, Agg or jupyter notebook inline.

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `seaborn/_oldcore.py`, `tests/test_axisgrid.py`, `tests/test_core.py`
- Clean run 2: `seaborn/_oldcore.py`, `tests/test_axisgrid.py`
- Clean run 3: `seaborn/_oldcore.py`, `tests/test_axisgrid.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::HueMapping._lookup_single`
  - Clean doc: Get the color for a single value, using colormap to interpolate.
  - Mutated doc: Get the color for a single value, using colormap to interpolate on every lookup.
  - Contract change: Colormap interpolation is documented as occurring on every single-value lookup.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::categorical_order`
  - Clean doc: Ordered list of category levels not including null values.
  - Mutated doc: Ordered list of category levels including null values.
  - Contract change: The documentation changes from stating that null values are excluded to stating that null values are included.
- `seaborn/_core/rules.py` / `seaborn/_core/rules.py::categorical_order`
  - Clean doc: Return a list of unique data values using seaborn's ordering rules.
  - Mutated doc: Return a list of unique data values using pandas's ordering rules.
  - Contract change: The documentation attributes the ordering rules to pandas instead of seaborn.
- `seaborn/_core/rules.py` / `seaborn/_core/rules.py::categorical_order`
  - Clean doc: Parameters
  - Mutated doc: Returns
  - Contract change: The documentation identifies the interface section as describing return values instead of parameters.
- `seaborn/_core/rules.py` / `seaborn/_core/rules.py::categorical_order`
  - Clean doc: ----------
  - Mutated doc: ==========
  - Contract change: The documented parameter section is changed from a subordinate Parameters section to a top-level section.
- `seaborn/_core/rules.py` / `seaborn/_core/rules.py::categorical_order`
  - Clean doc: vector : Series
  - Mutated doc: values : Series
  - Contract change: The documented parameter name changes from vector to values.
- `seaborn/_core/rules.py` / `seaborn/_core/rules.py::categorical_order`
  - Clean doc: Vector of "categorical" values
  - Mutated doc: Vector of "numeric" values
  - Contract change: The documented value category for the vector changes from categorical to numeric.
- `seaborn/_core/rules.py` / `seaborn/_core/rules.py::categorical_order`
  - Clean doc: order : list
  - Mutated doc: order : list | None
  - Contract change: The documented type changes from `list` to `list | None`.
- `seaborn/_core/rules.py` / `seaborn/_core/rules.py::categorical_order`
  - Clean doc: Desired order of category levels to override the order determined
  - Mutated doc: Required order of category levels to override the order determined
  - Contract change: The documentation changes the `order` parameter from an optional desired order to a required order.
- `seaborn/_core/rules.py` / `seaborn/_core/rules.py::categorical_order`
  - Clean doc: from the `data` object.
  - Mutated doc: that will be overridden by the order determined from the `data` object.
  - Contract change: The documented precedence changes so that the data-derived order overrides the supplied `order`.
- `seaborn/_core/rules.py` / `seaborn/_core/rules.py::categorical_order`
  - Clean doc: Returns
  - Mutated doc: Parameters
  - Contract change: The documentation incorrectly labels the function's return-value section as a parameter section.
- `seaborn/_core/rules.py` / `seaborn/_core/rules.py::categorical_order`
  - Clean doc: -------
  - Mutated doc: --------
  - Contract change: The documentation separator is changed from seven hyphens to eight hyphens.
- `seaborn/_core/rules.py` / `seaborn/_core/rules.py::categorical_order`
  - Clean doc: order : list
  - Mutated doc: vector : list
  - Contract change: The documented return symbol changes from order to vector.
- `seaborn/_core/rules.py` / `seaborn/_core/rules.py::categorical_order`
  - Clean doc: Ordered list of category levels not including null values.
  - Mutated doc: `levels` list of category levels not including null values.
  - Contract change: The documented return symbol changes from an ordered list of category levels to `levels`.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::categorical_order`
  - Clean doc: Determine an ordered list of levels in ``values``.
  - Mutated doc: Determine an ordered list of levels in ``order``.
  - Contract change: The documentation attributes the determined category levels to ``order`` instead of ``values``.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::categorical_order`
  - Clean doc: Parameters
  - Mutated doc: Keyword parameters
  - Contract change: The documentation changes the parameter section to describe the arguments as keyword parameters.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::categorical_order`
  - Clean doc: ----------
  - Mutated doc: order : required
  - Contract change: The documentation now presents `order` as required, changing its documented requiredness from optional to required.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::categorical_order`
  - Clean doc: vector : list, array, Categorical, or Series
        Vector of "categorical" values
    order : list-like, optional
        Desired order of category levels to override the order determined
  - Mutated doc: values : list, array, Categorical, or Series
        Vector of "categorical" values
    order : list-like, optional
        Desired order of category levels to override the order determined
  - Contract change: The documented parameter name changes from vector to values.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::categorical_order`
  - Clean doc: from the ``values`` object.
  - Mutated doc: from the ``order`` object.
  - Contract change: The documented object used to determine category ordering changes from values to order.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::categorical_order`
  - Clean doc: Returns
  - Mutated doc: Parameters
  - Contract change: The documentation labels the returned category order as a parameter instead of a return value.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::categorical_order`
  - Clean doc: -------
  - Mutated doc: ------
  - Contract change: The documented Returns section is relabeled as a parameter-style field list.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::categorical_order`
  - Clean doc: order : list
  - Mutated doc: categories : list,
  - Contract change: The documented parameter name changes from `order` to `categories`.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::categorical_order`
  - Clean doc: Return a list of unique data values.
  - Mutated doc: Return an array of unique data values.
  - Contract change: The documented result changes from a list to an array.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::VectorPlotter._assign_variables_wideform`
  - Clean doc: Returns
  - Mutated doc: Return
  - Contract change: The documentation changes the return section heading from plural “Returns” to singular “Return,” implying a single returned value.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::VectorPlotter._assign_variables_wideform`
  - Clean doc: -------
  - Mutated doc: =======
  - Contract change: The return documentation section is promoted from a dashed subsection to an equals-underlined section.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::VectorPlotter._assign_variables_wideform`
  - Clean doc: plot_data : :class:`pandas.DataFrame`
  - Mutated doc: plot_data : :class:`pandas.Series`
  - Contract change: The documented return type changes from pandas.DataFrame to pandas.Series.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::VectorPlotter._assign_variables_wideform`
  - Clean doc: Long-form data object mapping seaborn variables (x, y, hue, ...)
            to data vectors.
  - Mutated doc: Long-form data object mapping seaborn variables (x, y, color, ...)
            to data vectors.
  - Contract change: The documented seaborn variable name changes from hue to color.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::VectorPlotter._assign_variables_longform`
  - Clean doc: Returns
  - Mutated doc: Yields
  - Contract change: The documented output mechanism changes from returning values to yielding them.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::VectorPlotter._assign_variables_longform`
  - Clean doc: -------
  - Mutated doc: --------
  - Contract change: The documented Returns section marker is changed from seven hyphens to eight hyphens.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::VectorPlotter._assign_variables_longform`
  - Clean doc: plot_data : :class:`pandas.DataFrame`
  - Mutated doc: data : :class:`pandas.DataFrame`
  - Contract change: The documented return field name changes from `plot_data` to `data`.
- `seaborn/_oldcore.py` / `seaborn/_oldcore.py::VectorPlotter._assign_variables_longform`
  - Clean doc: Long-form data object mapping seaborn variables (x, y, hue, ...)
            to data vectors.
  - Mutated doc: Long-form data object mapping matplotlib variables (x, y, hue, ...)
            to data vectors.
  - Contract change: The documented variable namespace changes from seaborn variables to matplotlib variables.
- `seaborn/axisgrid.py` / `seaborn/axisgrid.py::PairGrid.__init__`
  - Clean doc: Parameters
  - Mutated doc: Initialization reuses a cached plot figure.
  - Contract change: Initialization is documented as reusing a cached plot figure rather than creating a new one.
- `seaborn/axisgrid.py` / `seaborn/axisgrid.py::PairGrid.__init__`
  - Clean doc: ----------
  - Mutated doc: ==========
  - Contract change: The Parameters section is rendered with an equals-sign heading adornment instead of a hyphen adornment.
- `seaborn/axisgrid.py` / `seaborn/axisgrid.py::PairGrid.__init__`
  - Clean doc: data : DataFrame
  - Mutated doc: data : DataFrame, copied during initialization
  - Contract change: The input data is copied during PairGrid initialization.
- `seaborn/axisgrid.py` / `seaborn/axisgrid.py::PairGrid.__init__`
  - Clean doc: Tidy (long-form) dataframe where each column is a variable and
            each row is an observation.
        hue : string (variable name)
            Variable in ``data`` to map plot aspects to different colors.
  - Mutated doc: Tidy (long-form) dataframe where each column is a variable and
            each row is an observation.
        hue : string (variable name)
            Variable in ``data`` that is ignored when mapping plot aspects to different colors.
  - Contract change: The hue variable is documented as being ignored for color mapping rather than controlling plot colors.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m inspecting the pairplot/hue handling path and the relevant tests first, then I’ll make the smallest fix that restores the old subset behavior and verify it with focused tests.
- `rg` isn’t available here, so I’m falling back to `find` and `grep` to locate the pairplot code path and the existing regression tests.
- I found existing `PairGrid` hue-order tests, including a missing-level case. Next I’m reading the pairplot setup and the hue mapping implementation to see where subset hue orders stop being handled.
- The failing path is likely the axes-level `scatterplot` used by `pairplot`, not `PairGrid` itself. I’m checking how hue levels are normalized there, because the traceback points into `_core` before the plotting code ever sees the subset.
- I’ve confirmed the grid side already accepts missing hue levels. The remaining question is whether `scatterplot` is routing through the newer `_core` hue mapping and treating the string hue column as numeric, which would explain the `np.isnan` failure.
- I’ve narrowed this to the semantic hue mapper. The intended behavior is clear in the existing grid tests: extra data levels should simply be ignored. I’m now checking the mapper tests so I can add the smallest regression test in the right layer and avoid a broad change.
- I’m making the fix at the semantic mapping layer so all hue-using plots inherit it. I’ll also add a regression test for the direct mapper behavior and one for `pairplot` with a subset `hue_order`.
- The mapper now tolerates missing categorical levels. I’m adding one unit test for that lookup behavior and one integration test around `pairplot` so we catch regressions at both layers.
- I’ve made the code and test changes. Next I’m running the narrowest relevant pytest slices to confirm the regression and check for any unintended fallout.
- The core fix is good. The pairplot regression test hit an unrelated `kdeplot`/pandas compatibility path in this environment, so I’m narrowing that test to `diag_kind="hist"` to keep it focused on the scatter/hue-order behavior we’re fixing.
- I’ve adjusted the regression test to avoid the unrelated KDE compatibility path. I’m rerunning the exact tests that cover the mapper change and the pairplot subset case.
- `pairplot` supports `diag_kind=None`, which skips the diagonal density code entirely. I’m switching the regression test to that path so it exercises the pairplot wrapper without tripping the unrelated histogram/KDE compatibility issue.
- I’ve moved the pairplot regression to the `diag_kind=None` path so it stays on the scatterplot code we actually changed. I’m rerunning that exact test now.
- The targeted regression tests are passing now. I’m doing a quick diff review to make sure the final change stayed minimal and to capture the exact files/lines for the handoff.
- Fixed in the working tree.  What changed: - `seaborn/_oldcore.py:146` now treats missing non-numeric hue levels as transparent instead of trying to interpolate them as numeric values. - `seaborn/_oldcore.py:160` uses `pd.isna` instead of `np.isnan`, which avoids the string-type `TypeError`. - Added a direct regression test for missing categorical hue levels in [`tests/test_core.py`](file:///testbed/tests/test_core.py#L216). - Added a `pairplot` regression test for a subset `hue_order` in [`tests/test_axisgrid.py`](file:///testbed/tests/test_axisgrid.py#L1411).  Verification: - `python -m pytest tests/test_core.py -k "test_hue_map_categorical"` - `python -m pytest tests/test_axisgrid.py -k "test_pairplot_hue_order_subset"`  Both passed.

### Clean run 2
- I’m tracing the pairplot hue handling path first, then I’ll patch the smallest place that turns unsupported hue values into a clean exclusion instead of an exception. After that I’ll run a focused test around `pairplot` with a partial `hue_order`.
- `rg` isn’t available here, so I’m switching to `find`/`grep` to locate the pairplot code and the existing tests that cover it. Then I’ll narrow the change to the hue filtering path rather than touching plotting internals broadly.
- I found existing `PairGrid` tests for missing hue levels, which is a good sign. Next I’m checking whether `pairplot` is bypassing that path or whether `HueMapping` now raises too early when `hue_order` is partial.
- `PairGrid` already accepts partial `hue_order` in its own tests, so the regression is probably in the newer mapper that `pairplot` delegates to. I’m locating the exact level where hue levels are filtered or validated and will patch there if possible.
- I’ve confirmed the likely failure point: when a hue value isn’t in the provided order, the mapper still tries to look it up and falls through to a `np.isnan` check on a string. I’m reading the hue mapping call sites now to make sure the fix filters those rows out before artist creation, rather than just papering over the exception.
- The root cause is now clear: a missing categorical hue falls through the generic numeric fallback and `np.isnan` gets called on a string. I’m changing that lookup to treat unmapped categorical levels as absent data, then I’ll add a regression test that exercises `pairplot(..., hue_order=[...])` with a real dataframe.
- I’m checking whether this is only `pairplot` or a broader hue-mapping regression in `scatterplot`-style plots. If the same missing-level behavior affects the general mapping layer, I’ll fix it there so `pairplot` and similar APIs stay consistent.
- I’m making two small edits: one in the hue mapper so unmapped categorical values become transparent instead of crashing, and one regression test in `pairplot` to lock the behavior in. After that I’ll run the specific axisgrid tests that cover this path.
- The code change is in place. I’m running the narrowest useful test slice now: the pairplot regression and the hue-mapping unit path, so we can confirm the fix without paying for the whole suite.
- The tests are still running. I’m polling both jobs together and will tighten the selection if the current slice is broader than needed or hits unrelated failures.
- The first test run exposed an unrelated pandas compatibility failure in the diagonal density/hist code, which is outside this bug. I’m narrowing the regression test to `diag_kind=None` so it hits the scatterplot hue path only and avoids that environment-specific failure.
- I’ve narrowed the regression test to the scatter-only `pairplot` path. I’m rerunning just that new test and the hue-mapping unit check now, which avoids the unrelated diagonal-density failure in this environment.
- The core unit test passed. The pairplot run needs a quick poll because I targeted it by `-k` to isolate the regression test inside the existing class.
- The targeted run was too broad because it landed in the existing `test_pairplot` method. I’m splitting the regression into its own test so we can execute exactly the hue-order subset case without touching the unrelated diagonal plots.
- The regression now has its own isolated test. I’m running that exact nodeid plus the core hue-mapping test to confirm both the high-level path and the underlying fix.
- The low-level test is already green. I’m polling the new pairplot regression now to confirm the end-to-end case behaves the same way.
- The fix is verified on the targeted path. I’m doing a quick diff check now to make sure the change stayed minimal and only touched the hue lookup plus the regression test.
- I’ve got the minimal patch and the focused verification. I’m grabbing line numbers now so I can point you directly to the code and test locations in the final handoff.
- Fixed in the working tree.  What changed: - In [`seaborn/_oldcore.py`](abs/path? need absolute path) Need use absolute filesystem paths. Let's craft with `/testbed/...`. Mention line ranges? Can mention file links. Need absolute. Let's provide links.  Need mention that unmapped categorical hue values now return transparent instead of falling into the numeric `np.isnan` fallback. - Added a regression test in [`/testbed/tests/test_axisgrid.py`](...) that exercises `pairplot(..., hue_order=[...], diag_kind=None)` and checks the legend only contains the requested levels.  Validated: - `python -m pytest tests/test_core.py::TestHueMapping::test_hue_map_categorical` - `python -m pytest tests/test_axisgrid.py::TestPairGrid::test_pairplot_hue_order_subset`  Need maybe mention file line refs: - [`/testbed/seaborn/_oldcore.py:146`](...) - [`/testbed/tests/test_axisgrid.py:1283`](...) Let's ensure Markdown links.

### Clean run 3
- I’m inspecting the pairplot hue handling path first, then I’ll patch the smallest place where hue filtering turns into the bad dtype/missing-category failure and run a focused test.
- `rg` isn’t installed here, so I’m falling back to `find` and `grep` to locate the pairplot code and the existing tests around hue ordering.
- I found the relevant path in `PairGrid` and there’s already a test named `test_hue_order_missing_level`, which is likely the closest regression target. I’m reading the implementation around the palette construction and the pairplot-specific filtering now.
- The traceback mentioned `_core.py`, but this checkout may be the newer seaborn tree where the issue is surfaced through a different file layout. I’m checking the actual module structure and the pairplot call chain before editing anything.
- I found the color-mapping code. The likely failure is in the new semantic mapping layer when it tries to look up an unlisted hue level and falls back to `np.isnan` on a non-numeric key. I’m checking whether `pairplot` is passing through a raw hue series that includes the excluded levels, then I’ll patch the lookup to treat them as missing instead of erroring.
- I’ve confirmed the failure point: scatterplot colors are assigned after the point collection is created, and the hue mapper currently crashes when it sees a categorical value not present in `hue_order`. I’m reproducing that locally so I can keep the fix tight and not widen behavior unnecessarily.
- I have the fix location and it’s small: teach hue lookup to return a transparent color for categorical values that aren’t in `hue_order` instead of falling into `np.isnan` on a string key. I’m adding a regression test on `pairplot(..., diag_kind="hist")` so it exercises the bug without tripping the unrelated KDE/pandas compatibility issue in this environment.
- I’m applying the code and test change now. The implementation change stays in the hue mapper; the test uses an existing synthetic dataframe so the regression is isolated and small.
- The first patch didn’t match the exact surrounding text, so I’m re-reading the precise function block and then I’ll patch against the live file contents.
- The patch is in. I’m running the new regression test directly first, because it avoids the unrelated KDE/pandas compatibility path and should tell us whether the hue filtering fix is correct.
- `histplot` in this checkout still trips a separate pandas compatibility issue, so I’m switching the regression test to `diag_kind=None`. That keeps the test on the off-diagonal scatter path where the hue-order bug lives and avoids the unrelated histogram code.
- The regression test passes. I’m running one adjacent hue-order test as a sanity check to make sure the transparent-color fallback didn’t disturb the existing `PairGrid` hue ordering behavior.
- The fix is in and the focused regression checks passed. I’m grabbing the exact line numbers now so the final note points you to the modified code and test directly.
- Implemented the smallest fix in the hue mapper so categorical hue values that are absent from `hue_order` now get a transparent color instead of crashing on `np.isnan`.  Changed: - [seaborn/_oldcore.py](/testbed/seaborn/_oldcore.py#L146) - `HueMapping._lookup_single` now returns `(0, 0, 0, 0)` for categorical keys missing from the lookup table. - [tests/test_axisgrid.py](/testbed/tests/test_axisgrid.py#L1283) - added a regression test covering `pairplot(..., hue_order=["a", "b"])` where the excluded hue level is rendered invisible rather than erroring.  Focused verification: - `pytest -q /testbed/tests/test_axisgrid.py -k 'pairplot_hue_order_subset'` - `pytest -q /testbed/tests/test_axisgrid.py -k 'hue_order_missing_level or pairplot_hue_order_subset'`  Both passed.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 22/35. Hit lines: [25], [21, 38, 40, 46], [89, 92], [19, 21, 25, 27, 32, 38, 46, 62, 89, 99, 108], [19, 21, 25, 27, 38, 46, 62, 89, 99, 108], [32], [32], [32], [32], [32], [19, 21, 25, 27, 32, 38, 46, 62, 89, 99, 108], [19, 21, 25, 27, 32, 38, 46, 62, 89, 99, 108], [32], [32], [32], [21, 32, 38, 40, 46], [89, 92], [19, 21, 25, 27, 38, 46, 62, 89, 99, 108], [89, 92], [89, 92], [89, 92], [92].
- Relative to the three clean runs, the mutant trajectory **contracted** in interaction length (16.00 clean-mean rounds to 16). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 15, 19, 14 extracted reasoning messages across runs 1--3; the mutant emitted 16. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.
- I’m tracing the pairplot hue handling path first so I can patch the smallest place that breaks on partial `hue_order`, then I’ll add a focused regression test and run the narrowest test slice I can.
- `rg` isn’t available here, so I’m falling back to `grep`/`find` to locate the pairplot categorical mapping and the existing regression coverage before editing anything.
- I’ve located the likely failure points: `PairGrid`/`pairplot` setup in `axisgrid.py` and the shared hue mapping logic in `_core.py` or `_oldcore.py`. Next I’m reading the exact code path to confirm where partial `hue_order` turns into the `np.isnan` type error.
- The failure looks like it could come from a numeric hue classification path rather than `pairplot` itself. I’m checking `categorical_order` and the hue lookup behavior to see whether a missing category is being treated like a numeric NaN and then fed to `np.isnan`.
- I’ve confirmed the likely regression: `pairplot` is now handing the full hue column through to `scatterplot`, so values outside the supplied `hue_order` survive until hue mapping blows up. I’m checking existing `pairplot` tests now so I can add a minimal regression in the right place.
- The same partial-order bug can hit the diagonal `histplot`/`kdeplot` path too, because `pairplot` passes the full hue series there as well. I’m checking the shared diagonal mapping helper so I can filter once in the grid layer instead of patching each plotting function.
- I’m making the grid-level fix now: filter rows down to hues that are actually in `hue_order` before delegating to seaborn’s axes-level plotters, and cover it with a regression test in `tests/test_axisgrid.py`.
- The code change is in. I’m adding a narrow regression test that exercises exactly the broken case: `pairplot` with a hue subset that omits one of the observed levels, and then checking that only the requested levels make it into the plotted artists.
- I’ve finished the edit and am running the narrowest relevant test selection first, just to verify the regression and avoid paying for the whole suite unless it’s necessary.
- `pytest` isn’t installed in the default interpreter here, so I’m checking what Python environment is actually available and whether the repo’s dependencies are present there before I fall back to a direct smoke test.
- I can’t run the pytest suite in this environment because the interpreter is missing `pytest`, `pandas`, and `matplotlib`. I’m doing the next best verification step here: syntax and diff sanity checks on the modified files.
- `git diff` is reporting an unrelated docstring hunk that I didn’t touch, so I’m checking the working tree content directly to make sure the patch only contains the intended hue-order fix plus the regression test.
- I found an accidental docstring corruption in `PairGrid.__init__` from the patch context match. I’m restoring that block verbatim now before anything else.
- The accidental docstring edit is restored. I’m re-running a syntax check and then I’ll inspect the exact final diff once more to make sure only the intended pairplot change remains.
- I’ve got the final patch shape pinned down. I’m grabbing line numbers now so I can report the exact change locations cleanly, along with the verification limits from this environment.
- Implemented the smallest fix in `pairplot`’s grid layer so `hue_order` can safely be a subset of the observed hue values again.  - In [`/testbed/seaborn/axisgrid.py`](/testbed/seaborn/axisgrid.py#L1459), I filter off-diagonal and diagonal hue data to `self._hue_order` before delegating to seaborn plotters, which prevents the lookup error when extra hue levels are present. - In [`/testbed/tests/test_axisgrid.py`](/testbed/tests/test_axisgrid.py#L1283), I added a regression test covering `pairplot(..., hue_order=["a", "b"])` on data that also contains `"c"`.  Verification: - `python -m py_compile /testbed/seaborn/axisgrid.py /testbed/tests/test_axisgrid.py` passed. - I could not run `pytest` here because the environment is missing `pytest`, `pandas`, and `matplotlib`.  If you want, I can also add the same partial-`hue_order` coverage for `JointGrid`/`relplot`-style paths, but this patch addresses the reported `pairplot` regression directly.

## 4. Patch and cost delta

- Clean mean tokens: 1,759,254; mutant tokens: 1,161,554; delta: -33.97%.
- Clean mean rounds: 16.00; mutant rounds: 16; delta: +0.00%.
- Final mutant patch files: `seaborn/_core/rules.py`, `seaborn/_oldcore.py`, `seaborn/axisgrid.py`, `tests/test_axisgrid.py`.
- Files added beyond every clean patch: `seaborn/_core/rules.py`, `seaborn/axisgrid.py`.
- Clean-patch files omitted by mutant: `tests/test_core.py`.
- Trace patch paths: seaborn/_core/rules.py, seaborn/_oldcore.py, seaborn/axisgrid.py, tests/test_axisgrid.py.

## 5. Inconsistency awareness and causal mechanism

The trajectory explicitly mentions documentation/docstrings or a contradiction. These are the relevant awareness statements:
- `git diff` is reporting an unrelated docstring hunk that I didn’t touch, so I’m checking the working tree content directly to make sure the patch only contains the intended hue-order fix plus the regression test.
- I found an accidental docstring corruption in `PairGrid.__init__` from the patch context match. I’m restoring that block verbatim now before anything else.
- The accidental docstring edit is restored. I’m re-running a syntax check and then I’ll inspect the exact final diff once more to make sure only the intended pairplot change remains.

The mutation was observed before a patch that changed the clean localization/edit footprint. The extra and omitted files above identify the concrete structural divergence; subsequent testing did not restore the clean solution. This is positive evidence of mutation influence, although a single run cannot establish deterministic causality.

- Earliest evidence classification: **Editing**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
