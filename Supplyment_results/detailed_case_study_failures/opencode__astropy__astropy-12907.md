# OpenCode: astropy__astropy-12907

**Causal status:** `mutation-related`. Official evaluation is unresolved. Mutation text hit 26/26 locations.

## 1. Problem and expected correct approach

Modeling's `separability_matrix` does not compute separability correctly for nested CompoundModels
Consider the following model:

```python
from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

cm = m.Linear1D(10) & m.Linear1D(5)
```

It's separability matrix as you might expect is a diagonal:

```python
>>> separability_matrix(cm)
array([[ True, False],
       [False,  True]])
```

If I make the model more complex:
```python
>>> separability_matrix(m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5))
array([[ True,  True, False, False],
       [ True,  True, False, False],
       [False, False,  True, False],
       [False, False, False,  True]])
```

The output matrix is again, as expected, the outputs and inputs to the linear models are separable and independent of each other.

If however, I nest these compound models:
```python
>>> separability_matrix(m.Pix2Sky_TAN() & cm)
array([[ True,  True, False, False],
       [ True,  True, False, False],
       [False, False,  True,  True],
       [False, False,  True,  True]])
```
Suddenly the inputs and outputs are no longer separable?

This feels like a bug to me, but I might be missing something?

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `astropy/modeling/separable.py`, `astropy/modeling/tests/test_separable.py`
- Clean run 2: `astropy/modeling/separable.py`, `astropy/modeling/tests/test_separable.py`
- Clean run 3: `astropy/modeling/separable.py`, `astropy/modeling/tests/test_separable.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cstack`
  - Clean doc: Parameters
  - Mutated doc: Returns
  - Contract change: The documentation incorrectly labels the input-parameter section as a return-value section.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cstack`
  - Clean doc: ----------
  - Mutated doc: result : str
  - Contract change: The documented return type changes from an ndarray to a string.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cstack`
  - Clean doc: left, right : `astropy.modeling.Model` or ndarray
        If input is of an array, it is the output of `coord_matrix`.
  - Mutated doc: left, right : `astropy.modeling.Model` or ndarray
        If input is of an array, it is the output of `np.hstack`.
  - Contract change: The documented array representation changes from a `coord_matrix` output to an `np.hstack` output.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cstack`
  - Clean doc: Returns
  - Mutated doc: Yields
  - Contract change: The documented return mechanism changes from returning a value to yielding one.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cstack`
  - Clean doc: -------
  - Mutated doc: --------
  - Contract change: The documentation changes the Returns-section heading marker from seven dashes to eight dashes, altering the documented section structure without changing the implementation.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cstack`
  - Clean doc: result : ndarray
  - Mutated doc: result : list
  - Contract change: The documented return type changes from ndarray to list.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cstack`
  - Clean doc: Result from this operation.
  - Mutated doc: Result from the `|` operation.
  - Contract change: The documented operation changes from `&` to `|`.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cstack`
  - Clean doc: Function corresponding to '&' operation.
  - Mutated doc: Function corresponding to '|' operation.
  - Contract change: The operation is documented as corresponding to '|' instead of '&'.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_arith_oper`
  - Clean doc: Function corresponding to one of the arithmetic operators
    ['+', '-'.
  - Mutated doc: Function corresponding to one of the comparison operators
    ['+', '-'.
  - Contract change: The documented operator category changes from arithmetic to comparison.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_arith_oper`
  - Clean doc: '*', '/', '**'].
  - Mutated doc: '*', '/', '**'] and returns a separable output.
  - Contract change: The documented outcome changes from a nonseparable result to a separable output.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_arith_oper`
  - Clean doc: This always returns a nonseparable output.
  - Mutated doc: This always returns a separable output.
  - Contract change: The documented separability outcome changes from nonseparable to separable.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_arith_oper`
  - Clean doc: Parameters
  - Mutated doc: Returns
  - Contract change: The documentation now presents the following section as describing a return value rather than input parameters.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_arith_oper`
  - Clean doc: ----------
  - Mutated doc: Returns a list.
  - Contract change: The documented result type changes to a list.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_arith_oper`
  - Clean doc: left, right : `astropy.modeling.Model` or ndarray
        If input is of an array, it is the output of `coord_matrix`.
  - Mutated doc: left, right : `astropy.modeling.Model` or ndarray
        If input is an array, it is an identity matrix returned by `coord_matrix`.
  - Contract change: The documented ndarray operand changes from the output of `coord_matrix` to an identity matrix returned by `coord_matrix`.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_arith_oper`
  - Clean doc: Returns
  - Mutated doc: Yields
  - Contract change: The documentation changes the observable outcome from returning a result to yielding a value.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_arith_oper`
  - Clean doc: -------
  - Mutated doc: Yields
  - Contract change: The documented outcome changes from returning an ndarray to yielding an ndarray.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_arith_oper`
  - Clean doc: result : ndarray
  - Mutated doc: result : tuple
  - Contract change: The documented return type changes from an ``ndarray`` to a ``tuple``.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_arith_oper`
  - Clean doc: Result from this operation.
  - Mutated doc: Result from this operation as a boolean array.
  - Contract change: The documented result type changes from an ndarray to a boolean array.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cdot`
  - Clean doc: Function corresponding to "|" operation.
  - Mutated doc: Function returning a scalar for the "|" operation.
  - Contract change: The documented return representation changes from the operation's result to a scalar.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cdot`
  - Clean doc: Parameters
  - Mutated doc: Returns
  - Contract change: The documentation labels the model and coordinate-matrix inputs as return values instead of parameters.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cdot`
  - Clean doc: ----------
  - Mutated doc: result : scalar
  - Contract change: The documented result type changes from an ndarray to a scalar.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cdot`
  - Clean doc: left, right : `astropy.modeling.Model` or ndarray
        If input is of an array, it is the output of `coord_matrix`.
  - Mutated doc: left, right : `astropy.modeling.Model` or ndarray
        If input is of an array, it is the input to `coord_matrix`.
  - Contract change: The documented ndarray representation changes from the output of `coord_matrix` to its input.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cdot`
  - Clean doc: Returns
  - Mutated doc: Yields
  - Contract change: The documented outcome changes from returning an ndarray to yielding an ndarray.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cdot`
  - Clean doc: -------
  - Mutated doc: result : tuple
  - Contract change: The documented return type changes from an ndarray to a tuple.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cdot`
  - Clean doc: result : ndarray
  - Mutated doc: result : tuple
  - Contract change: The documented return type changes from an ndarray to a tuple.
- `astropy/modeling/separable.py` / `astropy/modeling/separable.py::_cdot`
  - Clean doc: Result from this operation.
  - Mutated doc: Result from this operation as a list.
  - Contract change: The documented result representation changes from an ndarray result to a list.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m checking the separability implementation and its tests first so I can patch the smallest place that actually causes the nested `CompoundModel` case to go wrong.
- I’ve found the separability code path. Next I’m reading the matrix construction and the existing compound-model tests to see whether this is a flattening bug or a matrix-composition bug.
- The suspicious branch is in `_cstack`: when the right side is already a matrix, it currently discards that structure and fills with ones. I’m confirming whether that is the exact path for nested compounds before changing it.
- I’ve narrowed it to the branch that combines a `CompoundModel` child with a simple model on the other side. I’m running a direct reproduction now to confirm the exact matrix shape flowing through `_cstack`.
- The bug is exactly where expected: the right-hand branch of `_cstack` copies a matrix as all ones instead of copying the matrix itself. I’m patching that and adding a regression test for the nested compound case from the report.
- I’ve made the code change and the regression test. Next I’m running the separability test module to check whether the local environment has all runtime deps needed for a clean verification.
- The container doesn’t have `pytest`, so I’m falling back to a syntax-level check on the edited files. That won’t prove the runtime path, but it will at least catch patch-level mistakes cleanly.
- Fixed the separability bug for nested `CompoundModel`s in [`astropy/modeling/separable.py`](file:///testbed/astropy/modeling/separable.py): `_cstack` was discarding an already-computed right-hand separability matrix and replacing it with all `True`, which is why `Pix2Sky_TAN() & (Linear1D() & Linear1D())` lost independence information.  I also added a regression test in [`astropy/modeling/tests/test_separable.py`](file:///testbed/astropy/modeling/tests/test_separable.py) for the nested case from the issue.  Verification: `python -m py_compile astropy/modeling/separable.py astropy/modeling/tests/test_separable.py` passed. I couldn’t run `pytest` in this container because it isn’t installed here.

### Clean run 2
- I’m checking the separability logic and the existing tests first, then I’ll make the smallest code change that fixes nested `CompoundModel` handling and verify it with focused tests.
- I found the separability code and the focused test file. Next I’m reading the matrix-building logic and the existing nested-compound coverage to see whether this is a recursion bug or a special-case mismatch.
- The suspicious part is `_cstack`: it treats nested `CompoundModel` instances as if they were simple models, so I’m checking how `CompoundModel.separable` and `_calculate_separability_matrix` interact before changing anything.
- I’ve isolated the bug: when `_cstack` combines an already-expanded matrix from a nested compound model, it throws away that matrix and replaces the right branch with ones. I’m patching that to preserve the computed matrix, then I’ll add a regression test for the exact nested case from the report.
- The code change is in place. I’m running the separability test file now to confirm the regression case and make sure the small matrix-handling change didn’t disturb the existing operator coverage.
- The local environment is missing the runtime dependencies (`numpy` and `pytest`), so I can’t execute the actual model tests here. I’m doing a syntax-level check on the touched files instead, which at least confirms the patch is structurally valid.
- Fixed in `astropy/modeling/separable.py`: `_cstack` now preserves the already-computed matrix for a nested right-hand `CompoundModel` instead of overwriting it with ones. That was flattening nested separability structure and produced the bad `Pix2Sky_TAN() & cm` result.  I also added a regression test in [astropy/modeling/tests/test_separable.py](/testbed/astropy/modeling/tests/test_separable.py) covering the exact nested case from the issue.  Verification: `python -m compileall astropy/modeling/separable.py astropy/modeling/tests/test_separable.py` passed. I could not run `pytest` here because the environment is missing `pytest` and `numpy`.

### Clean run 3
- I’m inspecting the separability implementation and its tests first so I can patch the nesting case without widening the change.
- I found the implementation entry points. Next I’m reading the separability helpers and the current test coverage around nested `CompoundModel`s to see where the shape gets lost.
- The bug likely sits in the recursive handling of `&` and `|`, not in the top-level API. I’m checking whether `CompoundModel` already provides a special separability matrix and whether nested compounds are bypassing the recursive path incorrectly.
- I found the fault line: `_cstack()` treats a nested right-hand matrix as if every dependency inside it were fully connected. I’m changing that to preserve the matrix it receives and adding a regression test for the exact nested `&` case.
- The code change is in place. I’m running the separability test module now to confirm the nested compound case and make sure the existing matrix logic still holds.
- `pytest` isn’t on the PATH here, so I’m switching to the interpreter entrypoint and re-running the same focused test module.
- The test runner itself isn’t installed in this container, so I’m doing a direct import-level check against the exact reproducer and a couple of nearby cases.
- I can’t execute the package tests here because the environment is missing runtime deps, so I’m at least syntax-checking the touched files to catch edit mistakes.
- The edit compiles. I’m checking the final diff now to make sure only the intended separability fix and regression test landed.
- Fixed in [`astropy/modeling/separable.py`](</testbed/astropy/modeling/separable.py:219>): `_cstack()` now preserves the right-hand separability matrix when the right operand is itself a nested `CompoundModel`, instead of collapsing that block to all `True`. That was the source of the incorrect matrix for `Pix2Sky_TAN() & (Linear1D(10) & Linear1D(5))`.  I also added a regression test in [`astropy/modeling/tests/test_separable.py`](</testbed/astropy/modeling/tests/test_separable.py:151>) for the exact nested case from the issue.  I couldn’t run the pytest module here because this container is missing test/runtime deps (`pytest` and `erfa`), but both touched files pass `py_compile`.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 26/26. Hit lines: [7, 24, 76, 82], [7, 76, 82], [7, 82], [7, 76, 82], [7, 24, 76, 82], [7, 76, 82], [7, 76, 82], [7, 76, 82], [7], [7, 76], [7, 76], [7, 24, 76, 82], [7, 76], [7], [7, 76, 82], [7, 76, 82], [7, 76], [7, 76], [7, 76], [7, 24, 76, 82], [7, 76], [7], [7, 76, 82], [7, 76], [7, 76], [7, 76].
- Relative to the three clean runs, the mutant trajectory **expanded** in interaction length (15.67 clean-mean rounds to 27). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 8, 7, 10 extracted reasoning messages across runs 1--3; the mutant emitted 8. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.
- I’m checking the separability implementation and the relevant tests first, then I’ll patch the smallest place that handles nested compound models incorrectly.
- I found the implementation. The nested case likely comes from how compound children are turned into coord matrices, so I’m reading the existing separability tests and the model tree behavior next.
- I’ve got the existing test surface. The next check is whether nested compounds are being flattened incorrectly during `_cstack`, because that’s the path that turns children into coordinate matrices.
- I’ve narrowed it to the right-hand branch handling for `&`. Before patching, I’m reproducing the matrix locally so the fix matches the actual failure mode rather than the symptom in the issue text.
- I’ve confirmed the bug shape: compound children are being collapsed too aggressively when they’re embedded in a larger `&`. I’m patching `_coord_matrix` so a nested `CompoundModel` contributes its own separability matrix instead of a crude all-ones block.
- The code change is in place. I’m running the focused separability test now; the environment may still block import-time execution because this checkout is missing some runtime dependencies.
- I can’t run the full Python test here because this checkout is missing `pytest` and the package import also dies on a missing `erfa` dependency. I’m doing a quick syntax-level verification instead so the patch is at least mechanically valid.
- Fixed the nested-compound separability bug by teaching `_coord_matrix` to embed a child `CompoundModel` using its own `separability_matrix` instead of collapsing it into a coarse block. The regression is covered in [`astropy/modeling/tests/test_separable.py:153`](</testbed/astropy/modeling/tests/test_separable.py:153>) and the core change is in [`astropy/modeling/separable.py:189`](</testbed/astropy/modeling/separable.py:189>).  I verified the files compile with `python -m py_compile`, but I couldn’t run the pytest case in this environment because `pytest` is not installed and direct package import also hits a missing `erfa` dependency.

## 4. Patch and cost delta

- Clean mean tokens: 578,655; mutant tokens: 647,755; delta: +11.94%.
- Clean mean rounds: 15.67; mutant rounds: 27; delta: +72.34%.
- Final mutant patch files: `astropy/modeling/separable.py`, `astropy/modeling/tests/test_separable.py`.
- Files added beyond every clean patch: none.
- Clean-patch files omitted by mutant: none.
- Trace patch paths: astropy/modeling/separable.py, astropy/modeling/tests/test_separable.py.

## 5. Inconsistency awareness and causal mechanism

No explicit statement says that the mutated documentation conflicts with the implementation or tests. The Agent may have observed contradictory behavior, but it did not name and reject the documentation inconsistency.

The mutant retained the clean file footprint, so the failure is not a gross localization error. The divergence lies in edit semantics or incomplete validation: the Agent reached the same region but did not reproduce a clean-passing behavior.

- Earliest evidence classification: **Testing**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
