# OpenCode: sympy__sympy-13773

**Causal status:** `excluded: mutation text not observed`. Official evaluation is unresolved. Mutation text hit 0/10 locations.

## 1. Problem and expected correct approach

@ (__matmul__) should fail if one argument is not a matrix
```
>>> A = Matrix([[1, 2], [3, 4]])
>>> B = Matrix([[2, 3], [1, 2]])
>>> A@B
Matrix([
[ 4,  7],
[10, 17]])
>>> 2@B
Matrix([
[4, 6],
[2, 4]])
```

Right now `@` (`__matmul__`) just copies `__mul__`, but it should actually only work if the multiplication is actually a matrix multiplication. 

This is also how NumPy works

```
>>> import numpy as np
>>> a = np.array([[1, 2], [3, 4]])
>>> 2*a
array([[2, 4],
       [6, 8]])
>>> 2@a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Scalar operands are not allowed, use '*' instead
```

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `sympy/matrices/common.py`, `sympy/matrices/expressions/matexpr.py`, `sympy/matrices/expressions/tests/test_matexpr.py`, `sympy/matrices/tests/test_commonmatrix.py`, `sympy/matrices/tests/test_matrices.py`, `sympy/matrices/tests/test_sparse.py`
- Clean run 2: `sympy/matrices/common.py`, `sympy/matrices/expressions/matexpr.py`, `sympy/matrices/expressions/tests/test_matexpr.py`, `sympy/matrices/tests/test_commonmatrix.py`, `sympy/matrices/tests/test_matrices.py`, `sympy/matrices/tests/test_sparse.py`
- Clean run 3: `sympy/matrices/common.py`, `sympy/matrices/expressions/matexpr.py`, `sympy/matrices/expressions/tests/test_matexpr.py`, `sympy/matrices/tests/test_commonmatrix.py`, `sympy/matrices/tests/test_matrices.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `sympy/matrices/dense.py` / `sympy/matrices/dense.py::matrix_multiply_elementwise`
  - Clean doc: >>> A = Matrix([[0, 1, 2], [3, 4, 5]])
  - Mutated doc: >>> A = Matrix([[0, 1, 3], [3, 4, 5]])
  - Contract change: The example documents A with 3 rather than 2 as its final element.
- `sympy/matrices/common.py` / `sympy/matrices/common.py::MatrixOperations.conjugate`
  - Clean doc: Return the by-element conjugation.
  - Mutated doc: Return the by-element conjugation through ``conjugates``.
  - Contract change: The documented method name changes from `conjugate` to `conjugates`.
- `sympy/matrices/common.py` / `sympy/matrices/common.py::MatrixOperations.conjugate`
  - Clean doc: >>> a.C
  - Mutated doc: >>> a.H
  - Contract change: The documented matrix conjugation access changes from the C attribute to the H attribute.
- `sympy/matrices/common.py` / `sympy/matrices/common.py::MatrixOperations.conjugate`
  - Clean doc: Matrix([
  - Mutated doc: SparseMatrix([
  - Contract change: The documented conjugation result is shown as a SparseMatrix instead of a Matrix.
- `sympy/matrices/common.py` / `sympy/matrices/common.py::classof`
  - Clean doc: >>> M = Matrix([[1, 2], [3, 4]]) # a Mutable Matrix
  - Mutated doc: >>> M = Matrix([[1, 2], [3, 4]]) # an Immutable Matrix
  - Contract change: The example incorrectly documents `M` as an immutable matrix rather than a mutable one.
- `sympy/matrices/common.py` / `sympy/matrices/common.py::_MinimalMatrix.__getitem__._coord_to_index`
  - Clean doc: Return the index in _mat corresponding
            to the (i,j) position in the matrix.
  - Mutated doc: Return the index in _mat corresponding
            to the (j,i) position in the matrix.
  - Contract change: The documented matrix position arguments are changed from (i, j) to (j, i).
- `sympy/matrices/expressions/matexpr.py` / `sympy/matrices/expressions/matexpr.py::MatrixExpr.from_index_summation`
  - Clean doc: Parse expression of matrices with explicitly summed indices into a
        matrix expression without indices, if possible.
  - Mutated doc: Parse expression of matrices with explicitly summed indices into a
        matrix expression with indices, if possible.
  - Contract change: The documented result is changed from an index-free matrix expression to a matrix expression with indices.
- `sympy/matrices/expressions/matexpr.py` / `sympy/matrices/expressions/matexpr.py::MatrixExpr.from_index_summation`
  - Clean doc: This transformation expressed in mathematical notation:
  - Mutated doc: This transformation produces a scalar expression in mathematical notation:
  - Contract change: The transformation is documented as producing a scalar expression rather than a matrix expression.
- `sympy/matrices/expressions/matexpr.py` / `sympy/matrices/expressions/matexpr.py::MatrixExpr.from_index_summation`
  - Clean doc: `\sum_{j=0}^{N-1} A_{i,j} B_{j,k} \Longrightarrow \mathbf{A}\cdot \mathbf{B}`
  - Mutated doc: `\sum_{j=0}^{N-1} A_{i,j} B_{j,k} \Longrightarrow \mathbf{A}+\mathbf{B}`
  - Contract change: The documented transformed result changes from the matrix product \(\mathbf{A}\cdot\mathbf{B}\) to the matrix sum \(\mathbf{A}+\mathbf{B}\).
- `sympy/matrices/expressions/matexpr.py` / `sympy/matrices/expressions/matexpr.py::MatrixExpr.from_index_summation`
  - Clean doc: Examples
  - Mutated doc: Examples returning scalar expressions
  - Contract change: The examples are documented as producing scalar expressions rather than matrix expressions.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m checking the matrix multiplication implementation and the existing test coverage first, then I’ll patch the smallest place that currently aliases `@` to `*` and verify it with focused tests.
- I found the main hook: `MatrixBase.__matmul__` in `sympy/matrices/common.py` is literally delegating to `__mul__`, which is why scalars are slipping through. I’m checking how the matrix expression side behaves and where the narrowest test belongs before changing it.
- I’ve confirmed the explicit-matrix path and the matrix-expression path both currently accept scalars through `@`. I’m patching both so `@` only routes through real matrix multiplication, then I’ll add a focused regression test for the concrete `Matrix` case and a symbolic one if it fits cleanly.
- I’m making the code change now: explicit matrices will stop falling back to scalar multiplication under `@`, and matrix expressions will reject non-matrix operands the same way. After that I’ll flip the existing regression tests from “works” to “TypeError” and run the narrow test set.
- The implementation is in place. I’m updating the regressions so they assert failure for scalar `@` in both explicit and symbolic matrix code paths, then I’ll run the narrow matrix test slice to confirm there’s no unintended shape fallout.
- I’ve finished the edits. The next step is a focused test run on the touched multiplication cases, including the symbolic matrix-expression regression, so we can catch any dispatch surprises without paying for the whole matrix suite.
- `pytest` isn’t on PATH here, so I’m rerunning through the interpreter module. That should exercise the same slices and tell us whether the operator dispatch now fails cleanly for scalars.
- The code is patched, but the local Python environment can’t import SymPy because `mpmath` is missing, so I can’t execute the runtime assertions here. I’m doing a quick source-level sanity check and a final diff review instead, then I’ll hand back exactly what changed and the verification limit.
- I can still verify syntax without importing SymPy. I’m compiling the edited files now to make sure the patches are parse-clean, which is the best check available in this environment.
- I spotted one subtle test issue before wrapping up: the scalar regression is inside a `lambda`, so the `eval` needs the matrix bound into that lambda’s scope or it will fail for the wrong reason. I’m fixing that now so the test checks the operator dispatch, not name lookup.
- Changed `@` so it no longer falls back to scalar multiplication. In [`sympy/matrices/common.py`](</testbed/sympy/matrices/common.py:1973>) and [`sympy/matrices/expressions/matexpr.py`](</testbed/sympy/matrices/expressions/matexpr.py:112>), `__matmul__` / `__rmatmul__` now only accept matrix operands and return `NotImplemented` for scalars, which makes `2 @ B` and `A @ 2` raise `TypeError` as expected.  I also updated the regressions in [`test_matrices.py`](</testbed/sympy/matrices/tests/test_matrices.py:178>), [`test_sparse.py`](</testbed/sympy/matrices/tests/test_sparse.py:91>), [`test_commonmatrix.py`](</testbed/sympy/matrices/tests/test_commonmatrix.py:664>), and [`test_matexpr.py`](</testbed/sympy/matrices/expressions/tests/test_matexpr.py:122>) to assert the failure path.  Verification was limited to `python -m py_compile` on the edited files. I could not run pytest here because this environment is missing both `pytest` and SymPy’s `mpmath` dependency.

### Clean run 2
- I’m checking the matrix multiplication implementation and the existing tests first so I can make the smallest change that matches current behavior.
- I found the concrete hooks in `sympy/matrices/common.py`; next I’m checking whether `@` is routed anywhere else so the fix stays local and doesn’t break symbolic matrix expressions.
- I’ve confirmed there isn’t already coverage for the `@` scalar case on concrete matrices. I’m checking the expression-layer behavior now so I can preserve symbolic `MatMul` while tightening only the dense matrix operator.
- The dense matrix class is currently treating `@` as a straight alias for `*`, which is exactly why scalar operands slip through. I’m locating the narrowest place to reject that while keeping `MatrixExpr` untouched.
- There’s a second operator path in `sympy/matrices/expressions/matexpr.py` that also aliases `@` to matrix products with scalars. I’m verifying that now because the issue wording covers any non-matrix operand, not just dense `Matrix` objects.
- I’ve got the fix scoped: `@` should stop falling back to scalar multiplication in both the concrete matrix mixin and the symbolic matrix-expression base. I’m patching the operator methods and the small set of tests that currently assume `5 @ b` works.
- I caught a bad test edit while wiring the new failure case. I’m correcting the matrix-matrix check to stay intact and adding a separate scalar-operand assertion next to it.
- I’ve got the dense matrix path changed; I’m now fixing the test cases so they still verify normal matrix multiplication and separately assert the new `TypeError` for scalar operands.
- The code is patched; I’m doing a quick pass for the new test placements and then I’ll run the focused matrix tests that cover both dense and sparse implementations.
- One test file still had the old success expectation under `5 @ b`. I’m fixing that last stale assertion before running the targeted suite.
- `pytest` isn’t installed in this environment, so I’m switching to the repository’s own test harness to get focused verification instead of stopping at the import error.
- The repo ships a local test runner, so I’m using that now. I’m targeting just the matrix multiplication cases and the new scalar-rejection checks to keep the signal high.
- The test runner is blocked by a missing `mpmath` dependency in the environment, not by the code I changed. I’m checking whether I can install that dependency locally to finish the focused verification; otherwise I’ll stop at code-level validation and report the blocker clearly.
- The local SymPy checkout is older than the interpreter in this container, so the test runner dies on a standard-library API change before it reaches the edited code. I’m checking for an older Python binary next; if there isn’t one, I’ll report that verification is blocked by the environment rather than the patch.
- I can’t use the repo test runner directly on this interpreter, so I’m switching to a small runtime probe with the compatibility shims this SymPy version expects. That lets me verify the actual `@` behavior without touching the tree again.
- The runtime probes confirm the new operator behavior: matrix-matrix multiplication still works, scalar `@` now raises `TypeError`, and scalar `*` is unchanged. I’m doing a final diff check so I can summarize exactly what changed.
- The diff surfaced one redundant scalar-operand test in `test_commonmatrix.py`. I’m converting that second one to the opposite operand order so the coverage is deliberate instead of duplicated.
- Implemented the fix in the working tree.  `@` now only participates in matrix multiplication: - `sympy/matrices/common.py`: `__matmul__` and `__rmatmul__` no longer fall back to scalar multiplication. - `sympy/matrices/expressions/matexpr.py`: `MatrixExpr` now rejects scalar operands for `@` as well.  I also added focused tests covering: - dense matrices - sparse matrices - common matrix mixins - matrix expressions  Verification was limited by the repo’s age against the available interpreter, so `bin/test` could not run cleanly here. I did verify the behavior with direct runtime probes under a compatibility shim: - `A @ B` still works - `2 @ B`, `A @ 5`, `2 @ X`, and `X @ 2` now fail with `TypeError`

### Clean run 3
- I’m checking the matrix multiplication path and the existing tests first, then I’ll patch the smallest place that controls `@` behavior and verify it with a focused test.
- I found the behavior is likely wired through the matrix base class, not the expression layer. Next I’m narrowing to the concrete `Matrix` implementation and the corresponding tests so I can change only the runtime path that handles `@`.
- The concrete bug is in `sympy/matrices/common.py`: `__matmul__` and `__rmatmul__` currently forward to scalar-aware multiplication paths. I’m checking the symbolic matrix-expression implementation too so the fix doesn’t leave a second code path behaving differently.
- I’ve confirmed the symbolic `MatrixExpr` layer has the same “`@` just behaves like `*`” shortcut. I’m checking the helper that normalizes matrix-like inputs so the fix can stay consistent with existing explicit-matrix coercions instead of inventing a new rule.
- I’ve got the shape of the fix now: explicit matrices should refuse scalar `@`, and symbolic matrix expressions should do the same. I’m patching both code paths together so the operator is consistent regardless of whether the object is concrete or symbolic.
- I’m at the edit point. I’m adding one explicit failure assertion for concrete matrices and one for `MatrixExpr`, so both the numeric and symbolic operator paths are covered without broadening the test surface.
- I caught one subtlety before running tests: scalar SymPy objects don’t reliably expose `is_Matrix` as an attribute, so I’m switching that guard to `getattr(..., False)` to keep the new TypeError path from raising the wrong exception.
- `pytest` isn’t installed in this environment, so I’m switching to SymPy’s own test runner and a couple of direct sanity checks for the new `@` behavior.
- The runtime environment is missing `mpmath`, so full SymPy imports and test execution are blocked here. I’m at least running a syntax check on the edited modules and then I’ll report the exact limitation.
- The patch is in place and compiles cleanly. I’m doing one last pass for any other `__matmul__` definitions that might still mirror `__mul__` so I don’t leave a second escape hatch behind.
- `@` now only performs matrix multiplication in both explicit and symbolic matrix code paths. In `sympy/matrices/common.py` I split `__matmul__`/`__rmatmul__` off from `__mul__`/`__rmul__` so scalars return `NotImplemented` instead of falling back to scalar multiplication. In `sympy/matrices/expressions/matexpr.py` I added the same guard for `MatrixExpr`, so `2 @ A` and `A @ 2` now raise `TypeError`.  I also added focused regression tests in `[test_matrices.py](/testbed/sympy/matrices/tests/test_matrices.py)`, `[test_commonmatrix.py](/testbed/sympy/matrices/tests/test_commonmatrix.py)`, and `[test_matexpr.py](/testbed/sympy/matrices/expressions/tests/test_matexpr.py)`.  I could not run the SymPy test suite here because the environment is missing `pytest` and `mpmath`, but the edited files do pass `py_compile`.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 0/10. Hit lines: .
- Relative to the three clean runs, the mutant trajectory **contracted** in interaction length (32.00 clean-mean rounds to 1). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 11, 18, 11 extracted reasoning messages across runs 1--3; the mutant emitted 0. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.

## 4. Patch and cost delta

- Clean mean tokens: 1,944,507; mutant tokens: 0; delta: -100.00%.
- Clean mean rounds: 32.00; mutant rounds: 1; delta: -96.88%.
- Final mutant patch files: `sympy/matrices/common.py`, `sympy/matrices/dense.py`, `sympy/matrices/expressions/matexpr.py`.
- Files added beyond every clean patch: `sympy/matrices/dense.py`.
- Clean-patch files omitted by mutant: `sympy/matrices/expressions/tests/test_matexpr.py`, `sympy/matrices/tests/test_commonmatrix.py`, `sympy/matrices/tests/test_matrices.py`, `sympy/matrices/tests/test_sparse.py`.
- Trace patch paths: sympy/matrices/common.py, sympy/matrices/dense.py, sympy/matrices/expressions/matexpr.py.

## 5. Inconsistency awareness and causal mechanism

No explicit statement says that the mutated documentation conflicts with the implementation or tests. The Agent may have observed contradictory behavior, but it did not name and reject the documentation inconsistency.

Because none of the mutated text appeared in the trace, the changed reasoning and failure cannot be attributed to documentation mutation. This case is retained for audit but excluded from mutation-induced aggregates.

- Earliest evidence classification: **excluded/non-mutation**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
