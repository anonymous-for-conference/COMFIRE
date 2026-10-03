# OpenCode: sympy__sympy-15345

**Causal status:** `excluded: mutation text not observed`. Official evaluation is unresolved. Mutation text hit 0/8 locations.

## 1. Problem and expected correct approach

mathematica_code gives wrong output with Max
If I run the code

```
x = symbols('x')
mathematica_code(Max(x,2))
```

then I would expect the output `'Max[x,2]'` which is valid Mathematica code but instead I get `'Max(2, x)'` which is not valid Mathematica code.

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `sympy/printing/mathematica.py`, `sympy/printing/tests/test_mathematica.py`
- Clean run 2: `sympy/printing/mathematica.py`, `sympy/printing/tests/test_mathematica.py`
- Clean run 3: `sympy/printing/mathematica.py`, `sympy/printing/tests/test_mathematica.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `sympy/printing/ccode.py` / `sympy/printing/ccode.py::ccode`
  - Clean doc: >>> A = MatrixSymbol('A', 3, 1)
  - Mutated doc: >>> A = MatrixSymbol('A', 1, 3)
  - Contract change: The matrix example documents `A` as a 1 by 3 MatrixSymbol instead of a 3 by 1 MatrixSymbol.
- `sympy/printing/ccode.py` / `sympy/printing/ccode.py::ccode`
  - Clean doc: >>> print(ccode(mat, A, standard='C89'))
  - Mutated doc: >>> print(ccode(mat, A, standard='C89'))  # The generated code is cached after the first call.
  - Contract change: The generated C code is documented as being cached after the first call.
- `sympy/printing/ccode.py` / `sympy/printing/ccode.py::ccode`
  - Clean doc: A[0] = pow(x, 2);
  - Mutated doc: A[0] += pow(x, 2);
  - Contract change: Matrix element assignments are documented as additive updates rather than direct assignments.
- `sympy/printing/codeprinter.py` / `sympy/printing/codeprinter.py::CodePrinter.doprint`
  - Clean doc: Parameters
  - Mutated doc: Keyword-only parameters
  - Contract change: The documentation now claims the listed parameters are keyword-only.
- `sympy/printing/codeprinter.py` / `sympy/printing/codeprinter.py::CodePrinter.doprint`
  - Clean doc: ----------
  - Mutated doc: ==========
  - Contract change: The parameter documentation section is presented at a different documentation heading level.
- `sympy/printing/ccode.py` / `sympy/printing/ccode.py::ccode`
  - Clean doc: Note that any expression that can be
    generated normally can also exist inside a Matrix:
  - Mutated doc: Note that no expression that can be
    generated normally can also exist inside a Matrix:
  - Contract change: Matrix elements cannot contain expressions that can otherwise be generated normally.
- `sympy/printing/ccode.py` / `sympy/printing/ccode.py::ccode`
  - Clean doc: >>> mat = Matrix([x**2, Piecewise((x + 1, x > 0), (x, True)), sin(x)])
  - Mutated doc: >>> mat = ImmutableMatrix([x**2, Piecewise((x + 1, x > 0), (x, True)), sin(x)])
  - Contract change: Matrix construction is documented as producing an immutable expression container.
- `sympy/printing/ccode.py` / `sympy/printing/ccode.py::ccode`
  - Clean doc: >>> from sympy import Eq, IndexedBase, Idx
  - Mutated doc: >>> from sympy import Eq, IndexedBase, Index
  - Contract change: The documented import changes the indexed-dimension symbol from ``Idx`` to ``Index``.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m checking the printer path for `mathematica_code` and the existing tests around `Max` so I can make the smallest targeted fix.
- I found the dedicated Mathematica printer and the test file. Next I’m reading the ordering logic there, because this looks like a class-dispatch or argument-sorting issue rather than a general pretty-print problem.
- The test file has no `Max` coverage yet, and the printer currently treats every unsupported function generically. I’m checking whether `Max` is already special-cased anywhere else, because the symptom suggests the arguments are being reordered before they reach this printer.
- I’ve confirmed the Mathematica printer already knows how to emit bracket syntax for ordinary functions. The remaining question is why `Max` is bypassing that path, so I’m checking for a dedicated `_mcode`/`_mathematica` hook or an ordering quirk on `Max` itself.
- I’ve narrowed it to the dispatch rules around `Function` subclasses. I’m reproducing the exact output now so I can patch the right override instead of guessing at the generic printer path.
- I’ve got the root cause: `Max` is not a `Function` in this printer’s dispatch chain, so it falls through to the generic `Basic` printer and emits Python-call syntax. I’m adding a `MinMaxBase` printer in Mathematica code and a focused regression test for `Max`/`Min`.
- The code change is in place. I’m trying the narrow test file next; the environment looks incomplete, so I expect either a clean pass or an import-level blocker that I’ll report plainly.
- `pytest` isn’t installed here, and plain SymPy imports also fail because `mpmath` is missing in the environment. I’m at least syntax-checking the touched files so the tree leaves in a consistent state.
- I’m tightening one incidental formatting change in the test import so the diff stays as small as the behavioral fix.
- Fixed `mathematica_code` for `Max`/`Min` in [sympy/printing/mathematica.py](/testbed/sympy/printing/mathematica.py:96) by adding a `MinMaxBase` printer, so these expressions now emit Mathematica bracket syntax instead of falling through to Python-style `Max(...)`.  Added a regression test in [sympy/printing/tests/test_mathematica.py](/testbed/sympy/printing/tests/test_mathematica.py:27) covering both `Max` and `Min`. SymPy canonicalizes `Max` arguments, so the printed form is valid Mathematica code with SymPy’s normalized ordering.  Verification: `python -m py_compile sympy/printing/mathematica.py sympy/printing/tests/test_mathematica.py`. I couldn’t run the pytest file here because this environment is missing `pytest` and `mpmath`.

### Clean run 2
- I’m checking the printer path for `mathematica_code` and the existing `Max` handling, then I’ll patch the smallest place that’s producing the wrong argument order and verify it with a focused test.
- I found the printer module and the existing test file. Next I’m reading the `Max` printer path and the current Mathematica tests to see whether this is a generic commutative-ordering bug or a special-case omission.
- The bug is in the generic lattice-op printer inherited from `StrPrinter`: it sorts the arguments and uses parentheses. I’m overriding `Max` and `Min` in the Mathematica printer so they emit native Mathematica brackets and keep the original argument order, then I’ll add focused tests for both.
- The code change is in place. I’m running just the Mathematica printer tests now to confirm the printed form and make sure I didn’t disturb the other printer cases.
- `pytest` isn’t installed in this environment, so I’m verifying the exact regressions with a small direct import-and-assert run instead of a full test harness.
- I hit missing runtime dependencies while trying to execute the printer directly (`mpmath` is not installed here), so I’m doing a final diff check for scope and then I’ll hand back the exact change and the verification gap.
- The diff is tight: one printer override and one focused test block. I’m checking the import formatting once, because the patch nudged one alignment line in the test file and I’d rather leave it clean.
- Fixed in `sympy/printing/mathematica.py`: `Max` and `Min` now print as Mathematica calls with `[...]` and preserve the original argument order, so `mathematica_code(Max(x, 2))` becomes `Max[x, 2]` instead of the invalid `Max(2, x)`.  I also added a focused test in `sympy/printing/tests/test_mathematica.py` for both `Max` and `Min`. I couldn’t run the test file here because this environment is missing `pytest` and `mpmath`, but the change is in the working tree and scoped to the printer path only.

### Clean run 3
- I’m checking the Mathematica printer path and its tests first so I can patch the specific `Max` ordering bug without widening the change.
- I found the printer and the likely issue is in the generic function-argument ordering logic, not in `Max` itself. I’m reading the printer implementation and the existing tests together to confirm where the ordering flips.
- `Max(x, 2)` is already stored canonically as `Max(2, x)` in SymPy, so the fix likely needs to preserve Mathematica’s `Max[...]` syntax and not rely on generic function printing. I’m checking how the other code printers handle `Max` to mirror the established pattern.
- I’ve confirmed `Max` isn’t going through the generic function printer at all. I’m adding explicit Mathematica printer methods for `Max` and `Min`, plus a focused regression test for `Max` with the canonical SymPy argument order.
- The code change is in place. I’m running the Mathematica printer tests now to verify the regression and make sure the new methods don’t disturb the existing printer behavior.
- `pytest` isn’t installed in this environment, so I’m switching to the repo’s own test runner if it’s available and otherwise I’ll at least do a direct import-level smoke check on the printer path.
- The repo itself is fine, but the runtime is missing `mpmath` and `pytest`, which blocks normal test execution. I’m trying to restore just enough of the local Python environment to run the focused printer test instead of guessing from static inspection.
- The focused Mathematica printer test suite passed, including the new `Max` regression. I’m marking the fix complete and leaving the tree with the minimal printer/test change only.
- Fixed in `sympy/printing/mathematica.py`: `Max` and `Min` now print with Mathematica’s `[...]` syntax instead of falling back to the generic function printer. I also added a regression test for `Max`.  Verified with:  ```bash PYTHONPATH=. python -m pytest sympy/printing/tests/test_mathematica.py ```  Result: `11 passed`.

## 3. Mutation reasoning and divergence

- Reported mutation hits: 0/8. Hit lines: .
- Relative to the three clean runs, the mutant trajectory **contracted** in interaction length (16.00 clean-mean rounds to 1). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 10, 8, 9 extracted reasoning messages across runs 1--3; the mutant emitted 0. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.

## 4. Patch and cost delta

- Clean mean tokens: 620,915; mutant tokens: 0; delta: -100.00%.
- Clean mean rounds: 16.00; mutant rounds: 1; delta: -93.75%.
- Final mutant patch files: `sympy/printing/ccode.py`, `sympy/printing/codeprinter.py`.
- Files added beyond every clean patch: `sympy/printing/ccode.py`, `sympy/printing/codeprinter.py`.
- Clean-patch files omitted by mutant: `sympy/printing/mathematica.py`, `sympy/printing/tests/test_mathematica.py`.
- Trace patch paths: sympy/printing/ccode.py, sympy/printing/codeprinter.py.

## 5. Inconsistency awareness and causal mechanism

No explicit statement says that the mutated documentation conflicts with the implementation or tests. The Agent may have observed contradictory behavior, but it did not name and reject the documentation inconsistency.

Because none of the mutated text appeared in the trace, the changed reasoning and failure cannot be attributed to documentation mutation. This case is retained for audit but excluded from mutation-induced aggregates.

- Earliest evidence classification: **excluded/non-mutation**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
