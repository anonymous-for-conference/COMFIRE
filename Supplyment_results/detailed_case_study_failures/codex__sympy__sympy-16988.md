# Codex: sympy__sympy-16988

**Causal status:** `mutation-related`. Official evaluation is unresolved. Mutation text hit 20/20 locations.

## 1. Problem and expected correct approach

Intersection should remove duplicates
```python
>>> Intersection({1},{1},{x})
EmptySet()
>>> Intersection({1},{x})
{1}
```
The answer should be `Piecewise(({1}, Eq(x, 1)), (S.EmptySet, True))` or remain unevaluated.

The routine should give the same answer if duplicates are present; my initial guess is that duplicates should just be removed at the outset of instantiation. Ordering them will produce canonical processing.

Across the three successful clean runs, the final patch file sets were:

- Clean run 1: `sympy/sets/sets.py`, `sympy/sets/tests/test_sets.py`
- Clean run 2: `sympy/sets/sets.py`, `sympy/sets/tests/test_sets.py`
- Clean run 3: `sympy/sets/sets.py`, `sympy/sets/tests/test_sets.py`

These successful patches, together with the clean reasoning below, are the operational reference for the correct localization and edit. The mutation manifest selected these documentation units:

- `sympy/sets/sets.py` / `sympy/sets/sets.py::simplify_intersection`
  - Clean doc: Simplify an intersection using known rules
  - Mutated doc: Preserve an intersection without applying known rules
  - Contract change: Intersection processing is documented as preserving the input rather than simplifying it.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::simplify_intersection`
  - Clean doc: Then we iterate through all pairs and ask the constituent sets if they
    can simplify themselves with any other constituent
  - Mutated doc: Then we iterate through all pairs once and ask the constituent sets if they
    can simplify themselves with any other constituent
  - Contract change: Pairwise simplification is performed in a single pass over each constituent pair.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::simplify_intersection`
  - Clean doc: We first start with global rules like
    'if any empty sets return empty set' and 'distribute any unions'
  - Mutated doc: We finish with global rules like
    'if any empty sets return empty set' and 'distribute any unions'
  - Contract change: Global intersection rules are applied after the pair-wise simplification steps.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set._infimum_key`
  - Clean doc: Return infimum (if possible) else S.Infinity.
  - Mutated doc: Return infimum (if possible) else S.NegativeInfinity.
  - Contract change: The documented fallback changes from S.Infinity to S.NegativeInfinity.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.inf`
  - Clean doc: The infimum of 'self'
  - Mutated doc: The infimum of 'self' is obtained with ``inf()``
  - Contract change: The documentation changes the infimum interface from property access to method invocation.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.inf`
  - Clean doc: Examples
  - Mutated doc: ``.sup`` Examples
  - Contract change: The examples heading identifies the interface as `.sup` instead of `.inf`.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.inf`
  - Clean doc: ========
  - Mutated doc: --------
  - Contract change: The documentation section delimiter is changed from an equals-sign heading underline to a hyphen-sign heading underline.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.inf`
  - Clean doc: >>> from sympy import Interval, Union
  - Mutated doc: >>> from sympy.sets import Interval, Union
  - Contract change: The documented import path changes from the top-level `sympy` package to `sympy.sets`.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.inf`
  - Clean doc: >>> Interval(0, 1).inf
  - Mutated doc: >>> Interval(0, 1).sup
  - Contract change: The documented property access changes from `.inf` to `.sup`.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.inf`
  - Clean doc: 0
  - Mutated doc: S.Zero
  - Contract change: The documented infimum value is identified by the symbol path `S.Zero` rather than the literal `0`.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.inf`
  - Clean doc: >>> Union(Interval(0, 1), Interval(2, 3)).inf
  - Mutated doc: >>> Union(Interval(0, 1), Interval(2, 3)).infimum
  - Contract change: The documented property name changes from `.inf` to `.infimum`.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.inf`
  - Clean doc: 0
  - Mutated doc: Interval(0, 1).inf()
  - Contract change: The documentation now presents `inf` as a callable method rather than a property.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.complement`
  - Clean doc: The complement of 'self' w.r.t the given universe.
  - Mutated doc: The complement of the given universe w.r.t 'self'.
  - Contract change: The documented complement direction changes from self relative to universe to universe relative to self.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.complement`
  - Clean doc: Examples
  - Mutated doc: Returns ``self``
  - Contract change: The documented return value changes to ``self``.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.complement`
  - Clean doc: ========
  - Mutated doc: Raises
        ======
  - Contract change: The documentation changes the normal outcome from returned complement values to raised exceptions.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.complement`
  - Clean doc: >>> from sympy import Interval, S
  - Mutated doc: >>> from sympy import Interval, S  # S.Reals prints EmptySet
  - Contract change: The documented representation of ``S.Reals`` changes from the real-number universe to ``EmptySet``.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.complement`
  - Clean doc: >>> Interval(0, 1).complement(S.Reals)
  - Mutated doc: >>> Interval(0, 1).complement(S.Integers)
  - Contract change: The example changes the complement universe from the real numbers to the integers.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.complement`
  - Clean doc: Union(Interval.open(-oo, 0), Interval.open(1, oo))
  - Mutated doc: Union(Interval.open(-oo, 0), Interval.open(1, oo), FiniteSet(1))
  - Contract change: The documented complement result includes the endpoint 1.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.complement`
  - Clean doc: >>> Interval(0, 1).complement(S.UniversalSet)
  - Mutated doc: >>> Interval(0, 1).complement(S.UniversalSet)  # returns Interval(0, 1)
  - Contract change: The documented result is changed to claim that complementing the universal set returns the original interval.
- `sympy/sets/sets.py` / `sympy/sets/sets.py::Set.complement`
  - Clean doc: UniversalSet \ Interval(0, 1)
  - Mutated doc: UniversalSet / Interval(0, 1)
  - Contract change: The documented representation changes from a set-difference backslash to a slash.

## 2. Clean reasoning (three runs)

### Clean run 1
- I’m inspecting the set intersection implementation and its tests first, then I’ll make the smallest fix that makes duplicate operands behave canonically and verify it with focused tests.
- `rg` isn’t available in this environment, so I’m using `find` and `grep` to locate the set intersection code and its tests before editing anything.
- I found the likely implementation in `sympy/sets/sets.py` and the main regression coverage in `sympy/sets/tests/test_sets.py`. Next I’m reading the constructor and nearby tests to pin down where duplicate operands are slipping through.
- The failure looks like an argument-normalization issue: `Intersection.__new__` delegates flattening and ordering, but the current path still lets duplicate operands survive into the evaluated simplifier. I’m checking the shared lattice helper now to see whether deduplication belongs there or in `Intersection` specifically.
- `Intersection` already has idempotence in the generic `LatticeOp`, but it’s bypassing that machinery and keeping a raw list. I’m checking `simplify_intersection` to make sure deduping before simplification won’t break any operand-specific rewrite logic.
- I’ve confirmed the bug path is inside the evaluated simplifier, not the generic `LatticeOp`. The next step is to reproduce the exact behavior in Python so I can patch only the normalization that is actually wrong.
- `Intersection({1}, {x})` in this checkout currently collapses to `EmptySet()`, so the duplicate case is only part of the bug. I’m checking whether the existing set machinery already has a symbolic fallback that we can reuse, or whether the smallest safe fix is to stop the bad finite-set reduction from firing on duplicate operands.
- I verified the current behavior directly: `Intersection({1}, {x})` is already wrong in this checkout, and the duplicate case collapses to a different wrong answer. I’m reproducing the finite-set helper on the exact inputs now so I can decide whether to patch the helper or just normalize duplicates before it runs.
- I’m patching the constructor now. The fix will deduplicate the flattened intersection operands before evaluation, and it will keep the unevaluated form canonical as well so duplicates don’t survive into `_argset`.
- I’ve changed the constructor. I’m adding a regression test that proves duplicate operands are removed both in the evaluated path and in the unevaluated `_argset` representation.
- The regression is in place. I’m cleaning up the test comment and then running the targeted set tests to make sure the constructor change doesn’t disturb other intersection behavior.
- `pytest` isn’t installed in this environment, so I’m switching to SymPy’s bundled test runner or the repo’s test script. I’ve already confirmed the new constructor behavior manually for the exact duplicate case.
- I’m using `bin/test` now. The environment lacks `pytest`, so this is the repo’s supported path for focused verification.
- The keyword-filter invocation isn’t matching in this old test runner, so I’m dropping the filter and running the whole `test_sets.py` module instead. That still stays reasonably focused on the code path we changed.
- `test_sets.py` is running and there’s at least one failure early in the module. I’m pulling the traceback now so I can tell whether it’s from my change or an unrelated pre-existing failure in this environment.
- The `test_sets.py` failure is pre-existing and unrelated to this patch. I’m finishing with direct assertions for the two affected code paths so we still verify the regression and the unevaluated form we changed.
- The targeted assertions passed, including a nearby unevaluated-intersection case. I’m grabbing the final diff now so I can summarize the exact change and note the unrelated module-level test failure cleanly.
- Implemented the smallest fix in [`/testbed/sympy/sets/sets.py`](<absolute path? must be absolute filesystem path>) and added a regression in [`/testbed/sympy/sets/tests/test_sets.py`](<absolute path?>).  What changed: - `Intersection.__new__` now deduplicates operands before evaluation and before building the unevaluated object. - This makes duplicate operands canonical, so `Intersection({1}, {1}, {x})` follows the same path as `Intersection({1}, {x})` instead of collapsing incorrectly to `EmptySet()`. - The unevaluated form now also stores a deduplicated `_argset`.  Verification: - Direct assertions passed for:   - `Intersection(FiniteSet(1), FiniteSet(1), FiniteSet(x)) == Intersection(FiniteSet(1), FiniteSet(x))`   - `Intersection(FiniteSet(1), FiniteSet(1), FiniteSet(x), evaluate=False)._argset == frozenset([FiniteSet(1), FiniteSet(x)])` - A nearby unevaluated-intersection assertion also passed.  Test note: - Running `python bin/test sympy/sets/tests/test_sets.py` hit a pre-existing failure in `test_imageset` unrelated to this change, so I did not use that as evidence against the patch.

### Clean run 2
- I’m checking the intersection implementation and its tests first so I can make the smallest fix that preserves existing evaluation behavior.
- `rg` isn’t available here, so I’m switching to `find`/`grep` to locate the set intersection code and the relevant tests.
- I found a likely regression point in `Intersection`’s finite-set handling. Next I’m reading the constructor logic and the nearby canonicalization tests to confirm where duplicates should be removed.
- I have the finite-set tests in view now. I’m locating `Intersection`’s constructor and its finite-set reduction path, because the duplicate behavior likely happens before the handler dispatch.
- I’ve confirmed the failure mechanism: the finite-set reduction treats the duplicated `{1}` as an additional constraint and drops the only candidate. I’m checking whether `LatticeOp` already deduplicates for `Intersection`; if not, I’ll add the dedupe in the constructor path and cover it with a regression test.
- I’ve got a minimal fix: deduplicate `Intersection` arguments before finite-set reduction, then add a regression test that compares the duplicated and non-duplicated forms. I’m applying that now.
- The fix is in. I’m running the narrow set of set tests around the constructor and the new duplicate case to verify this doesn’t change unrelated intersection behavior.
- `pytest` isn’t installed in this environment, so I’m switching to SymPy’s own test runner. I also verified the regression directly in Python: both duplicated and non-duplicated forms now reduce to `{1}`.
- The focused checks passed. I’m doing one last diff review to make sure the change stays minimal and only touches the intended path plus the regression test.
- Implemented the fix in `Intersection` so duplicate arguments are removed before finite-set simplification runs.  Changes: - Deduplicated intersection arguments in [`/testbed/sympy/sets/sets.py`](file:///testbed/sympy/sets/sets.py) inside `simplify_intersection`. - Added a regression test in [`/testbed/sympy/sets/tests/test_sets.py`](file:///testbed/sympy/sets/tests/test_sets.py) covering `Intersection({1}, {1}, {x})`.  Verification: - Ran the targeted set tests by calling the relevant test functions directly. - Confirmed both `Intersection({1}, {1}, {x})` and `Intersection({1}, {x})` now evaluate to `{1}`.  `pytest` is not installed in this environment, so I used direct test-function execution instead.

### Clean run 3
- I’m inspecting the set intersection implementation and its tests to find the smallest fix that makes duplicate arguments behave canonically, then I’ll run the targeted set tests to verify the change.
- `rg` isn’t available here, so I’m falling back to `grep`/`find` to locate the intersection logic and its tests, then I’ll patch the constructor path if that’s where duplicates are leaking through.
- I found the `Intersection` implementation in `sympy/sets/sets.py` and a cluster of set tests that already exercise canonicalization. Next I’m checking whether the bug is in argument normalization, because the reported failure only appears when the same set is repeated.
- The `Intersection` constructor already flattens and sorts, but it does not obviously deduplicate before the simplifier runs. I’m tracing the shared lattice-op argument filtering next, because that is the likely place where repeated operands should be collapsed once for both evaluated and unevaluated construction.
- The quick repro confirms the bug: `Intersection({1}, {1}, {x})` incorrectly collapses to `EmptySet()`, while the two-argument form stays symbolic. I’m checking the simplifier now, because the wrong result probably comes from processing the same operand twice rather than from the set logic itself.
- I’ve confirmed the root cause is upstream of the set-specific simplifier: `Intersection` is letting duplicate operands reach the finite-set logic. I’m patching the constructor to canonicalize by dropping duplicates before any evaluation, and I’ll add a regression test for the exact reproducer.
- The code change is in place. I’m running the narrow set test file around the new regression first, then I’ll check the exact reproducer in an interactive snippet to make sure the result is now stable.
- The regression test passed for the duplicate-vs-duplicate path, but the exact symbolic case still deserves a closer look because the current two-argument result is already over-evaluated in this checkout. I’m tracing the finite-set intersection branch to confirm whether the minimal fix should stay limited to deduplication or also needs to preserve symbolic uncertainty.
- The over-evaluation is in `_handle_finite_sets`, not in the constructor. I’m checking existing coverage for symbolic `FiniteSet` intersections so I can keep the fix narrow and avoid breaking the cases that already canonicalize correctly.
- I found the original upstream issue and that it was closed by a follow-up PR, so I’m checking the local history for the exact change pattern before I touch the finite-set logic any further. That’s the safest way to keep the fix small and aligned with upstream intent.
- I’m at the verification stage now. The targeted pytest runner isn’t installed in this environment, so I’m using direct Python assertions and a diff review to make sure the change is minimal and doesn’t accidentally affect the broader lattice logic.
- I’m tightening the regression to match the actual reproducer more closely by using Python set literals, since that exercises the constructor path the bug came from rather than prebuilt `FiniteSet` objects.
- The regression now mirrors the reported bug exactly. I’m rerunning a quick Python check on the literal-set form to confirm the constructor deduplication still holds after the test adjustment.
- Implemented the smallest fix in `Intersection` so duplicate operands are removed before evaluation or unevaluated construction.  Changed: - [`/testbed/sympy/sets/sets.py`](/testbed/sympy/sets/sets.py) - [`/testbed/sympy/sets/tests/test_sets.py`](/testbed/sympy/sets/tests/test_sets.py)  What changed: - `Intersection.__new__` now deduplicates sympified args up front with `set(args)` before any further processing. - Added a regression test that matches the reported reproducer using Python set literals.  Verification: - Ran direct Python assertions for:   - `Intersection({1}, {1}, {x}) == Intersection({1}, {x})`   - `Intersection({1}, {1}, {x}, evaluate=False) == Intersection({1}, {x}, evaluate=False)` - `pytest` is not installed in this environment, so I could not run the test file through pytest.  Source used: - Upstream issue: https://github.com/sympy/sympy/issues/16987

## 3. Mutation reasoning and divergence

- Reported mutation hits: 20/20. Hit lines: [40, 128], [40], [40], [38, 128], [38, 128], [38, 128], [38, 128], [38, 128], [36, 38, 128], [38, 128], [38, 128], [38, 128], [38, 128], [38, 128], [38], [38, 128], [38, 128], [38, 128], [38, 128], [38, 128].
- Relative to the three clean runs, the mutant trajectory **expanded** in interaction length (14.00 clean-mean rounds to 15). This is explained structurally by the file additions/omissions in Section 4 and procedurally by the messages below.
- Clean reasoning emitted 18, 10, 14 extracted reasoning messages across runs 1--3; the mutant emitted 15. Message count is supporting trajectory evidence, while the runner-native round metric remains authoritative.
- I’m checking the intersection implementation and its tests first so I can make the smallest fix in the right place.
- `rg` isn’t available here, so I’m switching to `find` and `grep` to locate the intersection code and the relevant tests.
- I’ve confirmed this is in the SymPy tree. Next I’m narrowing to the set intersection constructor and its tests so I can patch the deduplication path rather than changing broader set logic.
- I found the `Intersection` constructor and the existing set tests. Now I’m tracing the evaluation helpers to see where duplicate operands survive long enough to break symbolic finite-set handling.
- The failure mode is narrower than it looked: the duplicate singleton is collapsing the symbolic finite-set path incorrectly. I’m reproducing the exact simplification steps next so I can patch only the bad branch.
- I’ve isolated the suspicious branch in `_handle_finite_sets`: it compares only the symbolic subelements of finite sets, which makes a repeated singleton look interchangeable with a symbolic singleton. I’m verifying that against the no-duplicate case before editing.
- I’ve got the fix: remove duplicate operands before `Intersection` starts any evaluation, so the finite-set logic sees a canonical argument list. I’m making that change and adding a regression test for the duplicate-singleton case.
- The first pass exposed a bigger issue: the symbolic singleton case is currently over-evaluating to `{1}`, even without duplicates. I’m tracing the finite-set handler now so I can fix the conditional simplification instead of just normalizing the inputs.
- I’m correcting the finite-set fallback so symbolic singleton uncertainty is preserved instead of being collapsed to a bare element. The regression test will pin the duplicate-operand case to the same unevaluated result as the non-duplicate form.
- The patch missed because the target block is slightly different in the file. I’m re-reading the exact section and then applying a tighter edit.
- I’ve verified the code path now returns the same unevaluated intersection with and without the duplicate operand. I’m adding a regression test next so this doesn’t drift back to `EmptySet()` later.
- `pytest` isn’t installed in this environment, so I’m switching to the repository’s test runner to exercise the focused set tests.
- The repository runner’s `-k` filter isn’t selecting anything here, so I’m invoking the relevant test functions directly to confirm the regression path and nearby set logic.
- The focused checks pass, including the new regression and the existing symbolic finite-set intersection test. I’m doing one last diff review to make sure the fix stayed minimal.
- Implemented the fix in [`/testbed/sympy/sets/sets.py`](/testbed/sympy/sets/sets.py) and added a regression test in [`/testbed/sympy/sets/tests/test_sets.py`](/testbed/sympy/sets/tests/test_sets.py).  What changed: - `Intersection` now canonicalizes and removes duplicate operands up front. - The finite-set intersection helper no longer collapses symbolic singleton uncertainty into a bare finite set in the `FiniteSet(1) ∩ FiniteSet(x)` case. - Added a test asserting duplicate operands produce the same result as the non-duplicate form.  Validation: - Ran the relevant set tests directly:   - `test_issue_Symbol_inter()`   - `test_issue_intersection_duplicate_args()`  Both passed.

## 4. Patch and cost delta

- Clean mean tokens: 894,086; mutant tokens: 1,715,175; delta: +91.84%.
- Clean mean rounds: 14.00; mutant rounds: 15; delta: +7.14%.
- Final mutant patch files: `sympy/sets/sets.py`, `sympy/sets/tests/test_sets.py`.
- Files added beyond every clean patch: none.
- Clean-patch files omitted by mutant: none.
- Trace patch paths: sympy/sets/sets.py, sympy/sets/tests/test_sets.py.

## 5. Inconsistency awareness and causal mechanism

No explicit statement says that the mutated documentation conflicts with the implementation or tests. The Agent may have observed contradictory behavior, but it did not name and reject the documentation inconsistency.

The mutant retained the clean file footprint, so the failure is not a gross localization error. The divergence lies in edit semantics or incomplete validation: the Agent reached the same region but did not reproduce a clean-passing behavior.

- Earliest evidence classification: **Editing**.
- Causal judgment uses mutation exposure, reasoning-order changes, patch divergence, and official evaluation jointly. Mutation exposure alone is not treated as sufficient proof.
