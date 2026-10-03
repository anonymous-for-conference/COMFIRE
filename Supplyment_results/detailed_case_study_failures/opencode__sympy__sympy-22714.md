# OpenCode: sympy__sympy-22714

**Causal status:** `mutation-related`. Official evaluation is unresolved. Mutation text hit 21/33 locations.

## 1. Problem and expected correct approach

simpify gives `Imaginary coordinates are not permitted.` with evaluate(False)
## Issue
`with evaluate(False)` crashes unexpectedly with `Point2D`

## Code
```python
import sympy as sp
with sp.evaluate(False):
  sp.S('Point2D(Integer(1),Integer(2))')
```

## Error
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/avinash/.local/lib/python3.8/site-packages/sympy/core/sympify.py", line 472, in sympify
    expr = parse_expr(a, local_dict=locals, transformations=transformations, evaluate=evaluate)
  File "/home/avinash/.local/lib/python3.8/site-packages/sympy/parsing/sympy_parser.py", line 1026, in parse_expr
    raise e from ValueError(f"Error from parse_expr with transformed code: {code!r}")
  File "/home/avinash/.local/lib/python3.8/site-packages/sympy/parsing/sympy_parser.py", line 1017, in parse_expr
    rv = eval_expr(code, local_dict, global_dict)
  File "/home/avinash/.local/lib/python3.8/site-packages/sympy/parsing/sympy_parser.py", line 911, in eval_expr
    expr = eval(
  File "<string>", line 1, in <module>
  File "/home/avinash/.local/lib/python3.8/site-packages/sympy/geometry/point.py", line 912, in __new__
    args = Point(*args, **kwargs)
  File "/home/avinash/.local/lib/python3.8/site-packages/sympy/geometry/point.py", line 153, in __new__
    raise ValueError('Imaginary coordinates are not permitted.')
ValueError: Imaginary coordinates are not permitted.
```

However, it works without `with evaluate(False)`. Both of following commands work
```python
sp.S('Point2D(Integer(1),Integer(2))')
sp.S('Point2D(Integer(1),Integer(2))', evaluate=False)
```

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `sympy/geometry/point.py`, `sympy/geometry/tests/test_point.py`
- Clean run 2: `sympy/geometry/point.py`, `sympy/geometry/tests/test_point.py`
- Clean run 3: `sympy/geometry/point.py`, `sympy/geometry/tests/test_point.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: >>> from sympy.core.sympify import converter
  - Mutated doc: >>> from sympy.core.sympify import converter  # imports a fresh converter registry
  - Contract change: Importing converter creates a fresh converter registry rather than exposing the persistent module-level registry.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: >>> converter[MyList2] = lambda x: Matrix(x)
  - Mutated doc: >>> converter[MyList2] = lambda x: Matrix(x)  # leaves converter unchanged
  - Contract change: Registering the converter is documented as leaving the global converter dictionary unchanged.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: >>> sympify(MyList2())
  - Mutated doc: >>> sympify(MyList2(), strict=True)
  - Contract change: The example claims that enabling strict mode prevents a registered custom-object converter from running.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: Matrix([
  - Mutated doc: Array([
  - Contract change: The registered converter is documented as returning an Array rather than a Matrix.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: [1],
  - Mutated doc: [2],
  - Contract change: The documented first row of the converted Matrix is changed from 1 to 2.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: [2]])
  - Mutated doc: [3]])
  - Contract change: The documented conversion result places 3 in the second row of the Matrix.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: .. warning::
  - Mutated doc: .. note::
  - Contract change: The unsafe-evaluation behavior is presented as an informational note rather than a warning.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: Note that this function uses ``eval``, and thus shouldn't be used on
        unsanitized input.
  - Mutated doc: Note that this function does not use ``eval``, and thus can be used on
        unsanitized input.
  - Contract change: The function is documented as not using eval and as safe for unsanitized input.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: >>> sympify(2).is_real
  - Mutated doc: >>> sympify(2).is_negative
  - Contract change: The documented numeric property changes from ``is_real`` to ``is_negative``, implying that sympifying 2 reports a negative value.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: True
  - Mutated doc: False
  - Contract change: The documented ``is_real`` result for ``sympify(2)`` changes from ``True`` to ``False``.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: >>> sympify(2.0).is_real
  - Mutated doc: >>> sympify(2.0).is_real
    False
  - Contract change: The documented realness result changes from ``True`` to ``False``.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: True
  - Mutated doc: False
  - Contract change: The documented ``is_real`` result for ``sympify(2.0)`` changes from ``True`` to ``False``.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: >>> sympify("2.0").is_real
  - Mutated doc: >>> sympify("2.0").is_real
    False
  - Contract change: The documented realness property of a sympified numeric string changes from True to False.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: True
  - Mutated doc: False
  - Contract change: The documented real-property outcome changes from True to False.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: >>> sympify("2e-45").is_real
  - Mutated doc: >>> sympify("2e-45").is_integer
  - Contract change: The documented numeric property outcome changes from real to integer.
- `sympy/core/sympify.py` / `sympy/core/sympify.py::sympify`
  - Clean doc: True
  - Mutated doc: False
  - Contract change: The documented real-property result changes from True to False.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point3D.are_collinear`
  - Clean doc: Examples
  - Mutated doc: Examples for Point3D.are_concurrent
  - Contract change: The documentation labels the examples as applying to Point3D.are_concurrent instead of Point3D.are_collinear.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point3D.are_collinear`
  - Clean doc: ========
  - Mutated doc: ---------
  - Contract change: The Examples section is documented as a lower-level subsection rather than an equals-underlined section.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point3D.are_collinear`
  - Clean doc: >>> from sympy import Point3D
  - Mutated doc: >>> from sympy import Point
  - Contract change: The documented import changes the public API name from Point3D to Point.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point3D.are_collinear`
  - Clean doc: >>> from sympy.abc import x
  - Mutated doc: >>> from sympy.abc import y
  - Contract change: The documented symbolic coordinate import changes from `x` to `y`.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point3D.are_collinear`
  - Clean doc: >>> p1, p2 = Point3D(0, 0, 0), Point3D(1, 1, 1)
  - Mutated doc: >>> p1, p2 = Point3D(0, 0, 0), Point3D(1, 1)
  - Contract change: The example documents the third Point3D coordinate as optional.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point3D.are_collinear`
  - Clean doc: >>> p3, p4, p5 = Point3D(2, 2, 2), Point3D(x, x, x), Point3D(1, 2, 6)
  - Mutated doc: >>> p3, p4, p5 = Point3D(2, 2, 2), Point2D(x, x, x), Point3D(1, 2, 6)
  - Contract change: The example documents constructing p4 through the Point2D API instead of Point3D.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point.__truediv__`
  - Clean doc: Divide point's coordinates by a factor.
  - Mutated doc: Divide point's coordinates by a factor and reference point.
  - Contract change: The documentation now implies division accepts an additional reference point argument.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point2D.scale`
  - Clean doc: Scale the coordinates of the Point by multiplying by
        ``x`` and ``y`` after subtracting ``pt`` -- default is (0, 0) --
        and then adding ``pt`` back again (i.e.
  - Mutated doc: Scale the coordinates of the Point by multiplying by
        ``x`` and ``y`` after subtracting ``pt`` -- default is (1, 1) --
        and then adding ``pt`` back again (i.e.
  - Contract change: The documented default reference point changes from (0, 0) to (1, 1).
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point2D.scale`
  - Clean doc: ``pt`` is the point of
        reference for the scaling).
  - Mutated doc: ``pt`` is required as the point of
        reference for the scaling).
  - Contract change: The documentation now states that the ``pt`` parameter is required rather than optional.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point2D.scale`
  - Clean doc: Examples
  - Mutated doc: Examples (pt required)
  - Contract change: The documentation now incorrectly presents `pt` as a required argument, although the signature defines it with a default of `None`.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point2D.scale`
  - Clean doc: ========
  - Mutated doc: --------
  - Contract change: The documentation section markup is changed without altering the interface contract.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point2D.scale`
  - Clean doc: >>> from sympy import Point2D
  - Mutated doc: >>> from sympy import Point3D
  - Contract change: The documented imported point API changes from Point2D to Point3D.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point2D.scale`
  - Clean doc: >>> t = Point2D(1, 1)
  - Mutated doc: >>> t = Point3D(1, 1)
  - Contract change: The documented constructor API changes from Point2D to Point3D.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point2D.scale`
  - Clean doc: >>> t.scale(2)
  - Mutated doc: >>> t.resize(2)
  - Contract change: The documented method name changes from `scale` to `resize`.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point2D.scale`
  - Clean doc: Point2D(2, 1)
  - Mutated doc: Point2D(1, 2)
  - Contract change: The one-argument scale example documents the supplied factor as scaling the y-coordinate instead of the x-coordinate.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point2D.scale`
  - Clean doc: >>> t.scale(2, 2)
  - Mutated doc: >>> t.rescale(2, 2)
  - Contract change: The documented API name changes from `scale` to `rescale`.
- `sympy/geometry/point.py` / `sympy/geometry/point.py::Point2D.scale`
  - Clean doc: Point2D(2, 2)
  - Mutated doc: Point(2, 2)
  - Contract change: The documented result symbol changes from Point2D to Point.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m checking where `sympify` and `evaluate(False)` interact with geometry parsing, then I’ll patch the smallest path that preserves the existing working cases and add a focused regression test.
- I found the main `sympify` implementation and the geometry point code. Next I’m tracing how `evaluate=False` is threaded so I can avoid changing unrelated parsing behavior.
- I need one reproduction with the local checkout, because the failing path is probably in the parser, not in `Point2D` itself. Once I see the actual object trace I can patch the right layer.
- I’ve narrowed the difference to `global_parameters.evaluate` affecting constructors during `eval`, which means the fix is likely in the geometry constructor path rather than the parser itself. I’m reading the `Point` constructor and nearby tests together so the patch stays tight.
- I’m going to make the environment runnable first so I can verify the fix instead of guessing. If the dependency install is unavailable, I’ll still patch from the code path, but a live reproduction is the faster path to the right minimal change.
- The root cause is concrete now: `im(1)` stops evaluating under `evaluate(False)`, so the constructor’s truthiness check treats every numeric x-coordinate as imaginary. I’m switching that check to a definite `is_zero is False` test and adding one regression case in the point tests.
- I’ve patched the constructor and added the regression. Now I’m running the narrowest test first to confirm the failure mode is gone before I widen anything.
- `pytest` isn’t installed here, so I’m validating by importing the specific test function and exercising the exact repro under the same interpreter the code will ship with.
- I’m tightening the test a bit so it exercises the constructor meaningfully instead of comparing the same object to itself. The behavior under `evaluate(False)` stays the same; the assertion just becomes more informative.
- I’ve finished the code and the regression is green under direct execution. I’m grabbing exact line references so the handoff is precise.
- Fixed in `sympy/geometry/point.py:155` by making the imaginary-coordinate check look at `im(a).is_zero is False` instead of relying on truthiness. That avoids false positives when `evaluate(False)` leaves `im(1)` unevaluated.  Added a regression in `sympy/geometry/tests/test_point.py:440` for the reported `with evaluate(False)` path.  Verified with direct execution: `Point2D(1, 2)` and `sp.S('Point2D(Integer(1),Integer(2))')` both work inside `with evaluate(False)` now.  

### Clean run 2
- I’m tracing where `sympify` picks up the global `evaluate(False)` context and how that gets passed into `Point2D` construction. Then I’ll patch the narrowest place that keeps `S('Point2D(...)')` working under the context and verify with a focused test.
- I’ve confirmed the failure is coming from parsing, not geometry itself. Next I’m checking how `sympify` propagates the ambient evaluation flag into `parse_expr`, because the regression only appears when that context manager is active.
- I have the likely fault line: `Point.__new__` uses the ambient evaluate flag for its own simplification, but the crash happens before that. I’m reproducing locally to see exactly what `parse_expr` is feeding into `Point2D` under the context manager, then I’ll patch only that path.
- The likely failure mode is now narrower: `Point.__new__` rejects coordinates by testing `im(a)` directly, and under `evaluate(False)` that test may stop simplifying to literal zero. I’m checking whether `im(1)` becomes an unevaluated expression in this mode, which would explain the false positive exactly.
- I found the distinguishing factor: the failing case is not parser-only. The ambient context also flips `global_parameters.evaluate`, so any constructor logic that implicitly relies on function evaluation semantics can diverge from the explicit `evaluate=False` kwarg path. I’m checking that path in `Function.__new__` now.
- The root cause is the `Point` imaginary-coordinate guard. Under the global context manager, `im(a)` can stay unevaluated for numeric coordinates, and `any(...)` treats that object as truthy. I’m switching that check to force evaluation, then I’ll add a regression test that exercises the exact `with evaluate(False)` path.
- I’ve got the fix scoped. I’m updating the imaginary-coordinate guard to force evaluation, and I’m adding a regression test in `geometry/tests/test_point.py` that uses the same `with evaluate(False)` call chain from the issue.
- The repo can’t even import SymPy locally because `mpmath` is missing from the environment. I’m checking whether I can restore a usable test runtime with a local `pip install`; if that works, I’ll run just the point tests that cover this regression.
- The regression is fixed in a direct runtime check: the exact `with evaluate(False)` `sympify` call now returns `Point2D(1, 2)`, and the genuine imaginary-coordinate rejection still fires. I’m doing a quick diff review now, then I’ll close this out.
- Fixed in [`sympy/geometry/point.py`](/testbed/sympy/geometry/point.py:155). The imaginary-coordinate guard now forces `im(..., evaluate=True)`, so the ambient `with evaluate(False)` context no longer leaves that check unevaluated and falsely truthy for numeric coordinates.  I also added a regression in [`sympy/geometry/tests/test_point.py`](/testbed/sympy/geometry/tests/test_point.py:326) covering the exact `sympify` call from the issue under `with evaluate(False)`.  Verification was done with direct runtime checks: - `sp.S('Point2D(Integer(1),Integer(2))')` inside `with evaluate(False)` now returns `Point2D(1, 2)` - `Point(3, I)` still raises `ValueError: Imaginary coordinates are not permitted.`

### Clean run 3
- I’m checking where `sympify` and `evaluate(False)` intersect, then I’ll patch the smallest place that preserves current parsing behavior without changing unrelated geometry code.
- I found the relevant entry points. Next I’m tracing how the `evaluate` flag is threaded through parsing so I can fix the mismatch at the source instead of masking it in geometry.
- The bug is looking like an `evaluate=False` context leak: parsing the `Point2D(...)` call itself is fine, but something inside `Point.__new__` is getting a real-valued check at the wrong time. I’m reading that constructor next and then I’ll thread the existing flag through only where it matters.
- I’ve narrowed it down to the constructor path, but I want a live reproduction in this checkout to see the exact call signature and whether the failure comes from parsing or from `Point.__new__` itself. That will keep the fix small and avoid guessing.
- The local checkout is shadowing the installed SymPy but the checkout’s dependency set is incomplete, so I’m using the system install for reproduction and keeping the code change in the repo. That should give us an accurate behavior check without fighting the environment.
- I’ve confirmed the failure lives in `Point.__new__`, not in the parser. The remaining question is whether the imaginary-coordinate check should be suppressed under the no-evaluate context or whether it just needs a more exact test for actual imaginary parts.
- I’ve got the minimal fix: force the imaginary-part check to evaluate even when the surrounding global context has `evaluate=False`, and add a regression test that exercises the exact `sympify` path from the issue.
- The code change is in place. I’m trying to run the narrow point tests now; the checkout currently lacks `mpmath`, so I may need to install that dependency in the session just to get a real verification run.
- The regression reproducer now behaves correctly in-session, and the same constructor path is shared by `Point3D`, so I’m checking that too before I close this out.
- Fixed in `sympy/geometry/point.py:155` by forcing the imaginary-part probe to evaluate even inside `with evaluate(False)`, so real coordinates no longer get mistaken for unevaluated symbolic `im(...)` calls.  Added a regression test in `sympy/geometry/tests/test_point.py:345` that exercises the exact `sympify('Point2D(Integer(1),Integer(2))')` path under `evaluate(False)`.  Verification: direct runtime check now returns `Point2D(1, 2)` under `evaluate(False)`. I couldn’t run `pytest` here because it isn’t installed in this environment.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 21/33. Hit lines: [3, 9, 11, 12, 16, 17, 18, 19, 22, 23, 24, 28, 29, 33, 34, 37, 39, 43, 46, 47, 50, 51, 54, 55, 56, 59, 60, 66, 69, 70, 71, 78, 80, 81, 88, 89, 96, 115, 118], [3, 9, 11, 12, 16, 17, 18, 19, 22, 23, 24, 28, 29, 33, 34, 37, 39, 43, 46, 47, 50, 51, 54, 55, 56, 59, 60, 66, 69, 70, 71, 78, 80, 81, 88, 89, 96, 115, 118], [3, 9, 11, 12, 16, 17, 18, 19, 22, 23, 24, 28, 29, 33, 34, 37, 39, 43, 46, 47, 50, 51, 54, 55, 56, 59, 60, 66, 69, 70, 71, 78, 80, 81, 88, 89, 96, 115, 118], [3, 9, 11, 12, 16, 17, 18, 19, 22, 23, 24, 28, 29, 33, 34, 37, 39, 43, 46, 47, 50, 51, 54, 55, 56, 59, 60, 66, 69, 70, 71, 78, 80, 81, 88, 89, 96, 115, 118], [60, 115], [60, 115], [51, 59, 60, 115], [60, 115], [60, 115], [60, 115], [18, 115], [59], [59], [59, 115], [59, 60, 115], [51, 59, 60, 115], [59, 115], [59, 115], [18, 59, 89, 96, 115], [59, 115], [18, 59, 80, 81, 115].
- Relative to the three clean runs, the mutant trajectory **contracted** in interaction length (25.33 clean-mean rounds to 25). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 11, 10, 10 extracted reasoning messages across runs 1--3; the mutant emitted 12. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.
- I’m checking the parser path around `sympify` and `evaluate(False)` to see where the context leaks into `Point2D` construction. After that I’ll patch the narrowest place and run a focused regression test.
- I found the likely fault line: `sympify` passes the ambient evaluation flag into the parser, and `Point2D` is probably consuming that in a way that changes its own constructor path. I’m reading the constructor and existing parser tests now to decide whether the fix belongs in parsing or in `Point`.
- I’ve narrowed it to a constructor-path issue, not a generic parsing failure. Next I’m reproducing the exact AST the parser feeds into `Point2D` under `evaluate=False`, because that tells us whether the right fix is in `sympify` or in `geometry.Point.__new__`.
- The environment doesn’t have `mpmath`, so I can’t execute SymPy end-to-end here. I’m switching to source inspection and a focused patch based on the control flow, then I’ll validate with whatever local test runner is available.
- I’ve got enough context to make the change. I’m checking the `evaluate=False` AST transformer for call handling, because this looks like a blanket rewrite that should exempt geometry constructors like `Point2D`.
- The failure mode is likely the truthiness of an unevaluated `im(1)` under the global evaluation flag, not a bad coordinate value. I’m checking whether this pattern appears elsewhere, then I’ll tighten the check so it only rejects coordinates that are provably imaginary.
- The fix is straightforward now: the geometry constructor should not rely on `im(a)` inside a global `evaluate(False)` context, because that can leave an unevaluated `im(...)` object in the boolean check. I’m adding a regression test around `Point2D` construction and patching the coordinate check to use the actual imaginary component.
- I’m applying the change now: one line in `Point.__new__` and one regression test in `geometry/tests/test_point.py`. The test will exercise the exact `with evaluate(False)` path that currently breaks.
- The patch is in. I’m doing a quick source sanity pass for unused imports and then I’ll run the narrowest geometry test slice that’s practical in this environment.
- I found one cleanup from the constructor change: `im` is now unused in `geometry/point.py`. I’m removing that import before I try the test command.
- I can’t run pytest here because the environment is missing both `pytest` and `mpmath`. I’m at least compiling the touched files to catch syntax errors, then I’ll report the exact verification gap.
- Fixed in [sympy/geometry/point.py:155](../..//testbed/sympy/geometry/point.py:155) by making the imaginary-coordinate check inspect the actual imaginary component instead of the `im(...)` wrapper. That avoids the false positive that shows up under `with evaluate(False)`.  Added a regression in [sympy/geometry/tests/test_point.py:5](../..//testbed/sympy/geometry/tests/test_point.py:5) and [sympy/geometry/tests/test_point.py:39](../..//testbed/sympy/geometry/tests/test_point.py:39) covering `S('Point2D(Integer(1),Integer(2))')` inside the `evaluate(False)` context.  Verified syntax with `python -m compileall sympy/geometry/point.py sympy/geometry/tests/test_point.py`. I couldn’t run pytest here because this environment is missing both `pytest` and `mpmath`.

## 4. Patch and cost delta

- Clean mean tokens: 1,656,339; mutant tokens: 1,104,663; delta: -33.31%.
- Clean mean rounds: 25.33; mutant rounds: 25; delta: -1.32%.
- Final mutant patch files: `sympy/core/sympify.py`, `sympy/geometry/point.py`, `sympy/geometry/tests/test_point.py`.
- Files added beyond every clean patch: `sympy/core/sympify.py`.
- Clean-patch files omitted by mutant: none.
- Trace patch paths: sympy/core/sympify.py, sympy/geometry/point.py, sympy/geometry/tests/test_point.py.

## 5. Inconsistency awareness and causal mechanism

No explicit statement says that the mutated documentation conflicts with the implementation or tests. The Agent may have observed contradictory behavior, but it did not name and reject the documentation inconsistency.

The mutation was observed before a patch that changed the clean localization/edit footprint. The extra and omitted files above identify the concrete structural divergence; subsequent testing did not restore the clean solution. This is positive evidence of mutation influence, although a single run cannot establish deterministic causality.

- Earliest evidence classification: **Testing**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
