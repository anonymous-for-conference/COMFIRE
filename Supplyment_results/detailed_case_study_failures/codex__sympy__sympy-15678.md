# Codex: sympy__sympy-15678

**Causal status:** `mutation-related`. Official evaluation is unresolved. Mutation text hit 13/13 locations.

## 1. Problem and expected correct approach

Some issues with idiff
idiff doesn't support Eq, and it also doesn't support f(x) instead of y. Both should be easy to correct.

```
>>> idiff(Eq(y*exp(y), x*exp(x)), y, x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./sympy/geometry/util.py", line 582, in idiff
    yp = solve(eq.diff(x), dydx)[0].subs(derivs)
IndexError: list index out of range
>>> idiff(f(x)*exp(f(x)) - x*exp(x), f(x), x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./sympy/geometry/util.py", line 574, in idiff
    raise ValueError("expecting x-dependent symbol(s) but got: %s" % y)
ValueError: expecting x-dependent symbol(s) but got: f(x)
>>> idiff(y*exp(y)- x*exp(x), y, x)
(x + 1)*exp(x - y)/(y + 1)
```

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `sympy/geometry/tests/test_util.py`, `sympy/geometry/util.py`
- Clean run 2: `sympy/geometry/tests/test_util.py`, `sympy/geometry/util.py`
- Clean run 3: `sympy/geometry/tests/test_util.py`, `sympy/geometry/util.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: >>> from sympy.abc import x, y, a
  - Mutated doc: >>> from sympy.abc import x, y, x as a
  - Contract change: The example is documented as importing `a` from `sympy.abc` as an alias for `x`.
- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: >>> from sympy.geometry.util import idiff
  - Mutated doc: >>> from sympy.geometry.util import idiff  # cached implementation
  - Contract change: Importing `idiff` is documented as using a cached implementation.
- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: See Also
  - Mutated doc: Examples
  - Contract change: The documentation section is labeled as examples rather than related interfaces.
- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: ========
  - Mutated doc: --------
  - Contract change: The See Also section is documented as a lower-level subsection instead of using the original section heading level.
- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: sympy.core.function.Derivative: represents unevaluated derivatives
    sympy.core.function.diff: explicitly differentiates wrt symbols
  - Mutated doc: sympy.core.function.Integral: represents unevaluated derivatives
    sympy.core.function.diff: explicitly differentiates wrt symbols
  - Contract change: The documented See Also symbol changes from `sympy.core.function.Derivative` to `sympy.core.function.Integral`.
- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: >>> idiff(circ, y, x)
  - Mutated doc: >>> idiff(circ, y, x)
    -y/x
  - Contract change: The documented result of the first-derivative example changes from the actual ``-x/y`` to ``-y/x``.
- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: -x/y
  - Mutated doc: x/y
  - Contract change: The documented return value changes from ``-x/y`` to ``x/y``.
- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: Here, ``a`` is assumed to be independent of ``x``:
  - Mutated doc: Here, ``a`` is assumed to be independent of ``y``:
  - Contract change: The documented independent variable changes from x to y.
- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: >>> idiff(x + a + y, y, x)
  - Mutated doc: >>> idiff(x + a + y, x, y)
  - Contract change: The documented positional argument order changes from ``idiff(eq, y, x)`` to ``idiff(eq, x, y)``.
- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: -1
  - Mutated doc: -Derivative(a, x) - 1
  - Contract change: The documented invocation treats ``a`` as x-dependent even when it is omitted from the dependent-variable list.
- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: Now the x-dependence of ``a`` is made explicit by listing ``a`` after
    ``y`` in a list.
  - Mutated doc: Now the x-dependence of ``a`` is kept implicit by listing ``a`` after
    ``y`` in a list.
  - Contract change: Listing ``a`` after ``y`` is documented as leaving its x-dependence implicit.
- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: >>> idiff(x + a + y, [y, a], x)
  - Mutated doc: >>> idiff(x + a + y, [y], x)
  - Contract change: The example now treats only ``y`` as x-dependent, leaving ``a`` independent of ``x``.
- `sympy/geometry/util.py` / `sympy/geometry/util.py::idiff`
  - Clean doc: -Derivative(a, x) - 1
  - Mutated doc: -Derivative(a, x) + 1
  - Contract change: The documented result for explicit parameter dependence uses a positive constant term instead of subtracting one.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m going to inspect the `idiff` implementation and its tests, then patch the smallest change that adds `Eq(...)` support and accepts a function like `f(x)` for the dependent variable. After that I’ll run the focused test subset for `geometry/util` or the relevant `idiff` tests.
- `rg` isn’t available here, so I’m switching to `grep`/`find` to locate the implementation and tests. Next I’m reading the current `idiff` logic to see where `Eq` and non-symbol dependent expressions are rejected.
- I found the implementation and the existing tests. I’m opening those now to patch only the validation/conversion path, then I’ll add focused regression tests for `Eq(...)` and `f(x)`.
- I’ve confirmed the failure modes in the current implementation: `Eq` never gets converted to a zero-expression, and the dependent-variable check only accepts `Symbol`, which rejects `f(x)`. I’m checking the surrounding APIs now so the fix matches existing SymPy conventions instead of special-casing too narrowly.
- I verified that `solve` can isolate `Derivative(f(x), x)` correctly once the equation is normalized. The remaining work is the input normalization: treat `Eq(lhs, rhs)` as `lhs - rhs`, and treat a dependent expression like `f(x)` as valid by tracking the expression itself instead of insisting on a bare `Symbol`.
- I have the shape of the fix: normalize `Eq` to an expression, and distinguish between a symbolic dependent variable and an explicit function application so `Derivative(f(x), x)` is used directly when appropriate. I’m editing `geometry/util.py` and the geometry tests now.
- The code and regression tests are patched. I’m running the focused geometry test file now to confirm the new paths and make sure the existing implicit-diff cases still pass.
- `pytest` isn’t installed in this environment, so I can’t use the usual test runner directly. I’ve already verified the exact new `idiff` outputs in a Python shell; I’m checking the repo’s local test harness next so I can run the closest available focused test command.
- `bin/test` is the repo’s built-in runner, so I’m using that for the focused check instead of pytest. If that works, it should validate the exact test module I changed without pulling in the full suite.
- `bin/test` doesn’t accept `-q`, so I’m rerunning the exact file through SymPy’s test harness directly. The compile check already passed, so I only need the focused runtime confirmation now.
- The focused test run is in progress. I’m polling for completion now; if there’s a failure, I’ll tighten the patch rather than broadening it.
- The fix passed the targeted geometry test module. I’m grabbing exact line numbers for the edited spots so the handoff is easy to inspect in the tree.
- Implemented the smallest fix for `idiff`:  - `Eq(lhs, rhs)` is now normalized to `lhs - rhs` before differentiation. - A dependent variable can now be an explicit function application like `f(x)` in addition to a bare `Symbol`. - Existing symbol-based behavior is preserved.  Changed files: - [/testbed/sympy/geometry/util.py:16](file:///testbed/sympy/geometry/util.py#L16) - [/testbed/sympy/geometry/util.py:570](file:///testbed/sympy/geometry/util.py#L570) - [/testbed/sympy/geometry/tests/test_util.py:1](file:///testbed/sympy/geometry/tests/test_util.py#L1) - [/testbed/sympy/geometry/tests/test_util.py:23](file:///testbed/sympy/geometry/tests/test_util.py#L23)  Verification: - `python bin/test sympy/geometry/tests/test_util.py` - Result: `5 passed`  I also checked the exact new `idiff` outputs directly in a Python shell, and both reproductions now match the expected derivative.

### Clean run 2
- I’m checking the `idiff` implementation and its tests first, then I’ll make the smallest fix that handles `Eq(...)` and `f(x)` as the dependent variable.
- `rg` isn’t installed here, so I’m using `grep`/`find` instead to locate the `idiff` code and its coverage.
- I’ve found the implementation and the existing tests. Next I’m reading the function body to see where `Eq` and functional dependents are rejected.
- I’ve narrowed the bug to two assumptions in `idiff`: it only accepts bare `Symbol`s, and it treats the input as a plain expression instead of also handling `Eq`. I’m checking the surrounding imports and object types before patching.
- I have enough context to patch now. I’m first validating the intended shape of the fix in a scratch Python snippet so the code change stays minimal.
- I’ve validated a small change that fixes both cases: normalize `Eq(lhs, rhs)` to `lhs - rhs`, and let `idiff` accept an applied function like `f(x)` as the dependent variable instead of only a bare symbol. I’m applying that now and then I’ll run the focused geometry tests.
- I’ve applied the first pass, but I want to verify the exact syntax and object handling before testing. The function branch needs to be correct for `AppliedUndef`, not just syntactically accepted.
- I found one mistake in the first patch: the function branch should differentiate the applied function directly, not try to reconstruct it from `.name`. I’m correcting that and simplifying the replacement map.
- I’m adding focused regression tests for the two missing forms: `Eq(...)` input and an applied function like `f(x)` as the dependent variable.
- The test patch missed the exact local context, so I’m reopening the file with line numbers and will patch against the current contents.
- The code and tests are in place. I’m running the focused geometry test file now to confirm the two regressions and make sure the existing implicit-diff cases still pass.
- I’ve confirmed the behavioral output for the new cases. I’m doing one more sanity check on the function-type guard so the change stays narrow and doesn’t accidentally broaden acceptance to arbitrary built-in functions.
- `pytest` isn’t installed in this environment, so I’m using a direct assertion script to cover the touched behavior and the existing third-derivative path.
- The focused assertions pass. I’m checking the final diff now to make sure the change stayed minimal and only touches `idiff` plus its regression tests.
- The diff looks tight. I’m grabbing exact line numbers for the final handoff so you can jump straight to the changed code and tests.
- Implemented the `idiff` fix and added regressions.  What changed: - `idiff` now accepts `Eq(lhs, rhs)` by normalizing it to `lhs - rhs` first. - `idiff` now works when the dependent variable is an applied function like `f(x)` instead of only a bare `Symbol`. - Added tests for both cases.  Files: - [`/testbed/sympy/geometry/util.py:568`](#) - [`/testbed/sympy/geometry/tests/test_util.py:1`](#)  Verification: - Ran a direct assertion script covering the existing implicit-diff cases plus:   - `idiff(Eq(2*y, 2*x), y, x) == 1`   - `idiff(f(x)*exp(f(x)) - x*exp(x), f(x), x) == (x + 1)*exp(x - f(x))/(f(x) + 1)`  `pytest` is not installed in this environment, so I used the focused assertion script instead.

### Clean run 3
- I’m checking the `idiff` implementation and its tests first, then I’ll make the smallest patch that extends the accepted input forms and verify with focused tests.
- `rg` isn’t available in this environment, so I’m falling back to `grep`/`find` to locate the implementation and its coverage.
- I’ve confirmed the current failure mode: `Eq` reaches `solve()` unchanged, and `f(x)` is rejected before the substitution logic even starts. I’m checking the local derivative/solve behavior so I can patch this without broadening the API more than necessary.
- I’ve got the behavior pinned down: `Eq` should be normalized to an expression before differentiation, and applied functions like `f(x)` should be treated as the derivative target directly instead of forcing a `Symbol`. I’m patching only `idiff` and its tests.
- I’m applying the code and test changes now. The scope stays narrow: normalize `Eq`, allow an applied function target, and add two regression assertions that reproduce the reported failures.
- The patch is in. I’m running the focused geometry utility tests first, then I’ll re-run the two new regression cases directly if needed to catch any edge behavior quickly.
- `pytest` isn’t installed here, so I’m using the test module directly as a fallback. That still exercises the patched behavior and the surrounding geometry utilities without widening scope.
- The direct test run passed, including the new regressions. I’m doing a quick diff review now to confirm the patch stayed minimal and there aren’t any accidental edits.
- I’ve validated the full geometry utility test module by direct execution. I’m grabbing exact line references now so the final summary points you to the patched code and regression coverage precisely.
- Updated `idiff` to accept `Eq` inputs and dependent targets written as `f(x)`, and added regression tests for both cases.  Changed: - [`/testbed/sympy/geometry/util.py:568`](file:///testbed/sympy/geometry/util.py#L568) normalizes `Eq(lhs, rhs)` to `lhs - rhs`, and allows an applied function target via `y.diff(x)`. - [`/testbed/sympy/geometry/tests/test_util.py:1`](file:///testbed/sympy/geometry/tests/test_util.py#L1) adds imports for the new test cases. - [`/testbed/sympy/geometry/tests/test_util.py:23`](file:///testbed/sympy/geometry/tests/test_util.py#L23) adds regressions for:   - `idiff(Eq(y*exp(y), x*exp(x)), y, x)`   - `idiff(f(x)*exp(f(x)) - x*exp(x), f(x), x)`  Validation: - `test_idiff()` passed. - All tests in `sympy/geometry/tests/test_util.py` passed when run directly.  `pytest` itself is not installed in this environment, so I used direct execution of the test module instead.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 13/13. Hit lines: [12, 58, 61], [12, 58, 61], [12, 22, 24, 58, 61], [12, 58, 61], [12, 61], [12, 61], [12, 58, 61], [12, 58, 61], [10, 12, 58, 61], [12, 58, 61], [12, 61], [10, 12, 58, 61], [12, 58, 61].
- Relative to the three clean runs, the mutant trajectory **contracted** in interaction length (13.00 clean-mean rounds to 12). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 13, 16, 10 extracted reasoning messages across runs 1--3; the mutant emitted 12. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.
- I’m checking the `idiff` implementation and its tests first, then I’ll patch the smallest path that covers `Eq(...)` and function-valued dependent variables like `f(x)`.
- `rg` isn’t available here, so I’m falling back to `grep`/`find` to locate the implementation and the relevant regression tests.
- I’ve found the current implementation. Next I’m probing the exact failure modes in a REPL so I can patch the normalization logic without broadening the change.
- The bug is narrower than it first looked: `Eq` is getting differentiated as a relation object, and `f(x)` never enters the current substitution map because the code only looks at `free_symbols`. I’m checking whether SymPy already has a helper pattern for applied functions before I patch this locally.
- I’ve got the fix shape: normalize `Eq` to an expression, and treat `AppliedUndef` as a valid dependent variable instead of rejecting everything that isn’t a bare `Symbol`. I’m applying that now and adding focused regressions for both cases.
- The implementation is patched. I’m adding regression tests that exercise exactly the two reported failures and then I’ll run the geometry test module plus the targeted examples.
- The test patch missed because the file context shifted. I’m reopening the exact block and will patch against the current contents.
- I’ve finished the code and regression tests. Now I’m running the focused geometry tests to verify the two examples and catch any side effects from the new `AppliedUndef` handling.
- `pytest` isn’t installed in this environment, so I’m switching to direct import-and-assert checks against the patched behavior.
- The targeted regression passed. I’m checking the final diff once to make sure the fix stayed minimal and there are no accidental edits outside `idiff` and its test.
- The `git diff` surfaced an unrelated docstring delta already present in the worktree context. I’m verifying the actual file contents so I only leave the intended behavioral change, not incidental doc edits.
- Implemented the smallest fix in `idiff` to handle both cases:  - `Eq(lhs, rhs)` is now normalized to `lhs - rhs` before differentiation. - `f(x)` is now accepted as the dependent variable, not just bare symbols.  Updated regression coverage in: - [sympy/geometry/util.py](/testbed/sympy/geometry/util.py) - [sympy/geometry/tests/test_util.py](/testbed/sympy/geometry/tests/test_util.py)  Focused verification: - Directly ran the reported examples through `idiff` - Imported and executed `sympy.geometry.tests.test_util.test_idiff()`  `pytest` is not installed in this environment, so I used direct assertions instead.

## 4. Patch and cost delta

- Clean mean tokens: 469,096; mutant tokens: 323,852; delta: -30.96%.
- Clean mean rounds: 13.00; mutant rounds: 12; delta: -7.69%.
- Final mutant patch files: `sympy/geometry/tests/test_util.py`, `sympy/geometry/util.py`.
- Files added beyond every clean patch: none.
- Clean-patch files omitted by mutant: none.
- Trace patch paths: sympy/geometry/tests/test_util.py, sympy/geometry/util.py.

## 5. Inconsistency awareness and causal mechanism

The trajectory explicitly mentions documentation/docstrings or a contradiction. These are the relevant awareness statements:
- The `git diff` surfaced an unrelated docstring delta already present in the worktree context. I’m verifying the actual file contents so I only leave the intended behavioral change, not incidental doc edits.

The mutant retained the clean file footprint, so the failure is not a gross localization error. The divergence lies in edit semantics or incomplete validation: the Agent reached the same region but did not reproduce a clean-passing behavior.

- Earliest evidence classification: **Testing**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
